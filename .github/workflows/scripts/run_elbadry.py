import os
import requests
from astropy.table import Table
import numpy as np
from math import sqrt

# Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
M_sun = 1.98847e30  # kg
AU = 1.495978707e11  # m

# Attempt a few known public URLs (Dataverse then Zenodo variants)
urls = [
    "https://dataverse.harvard.edu/api/access/datafile/4661493?format=original&gbrecs=true",
    "https://zenodo.org/record/4609820/files/all_columns_catalog_shift.fits.gz",
    "https://zenodo.org/record/4607167/files/all_columns_catalog_shift.fits.gz"
]
fname = "elbadry_widebinaries_shift.fits.gz"

if not os.path.exists(fname):
    for url in urls:
        try:
            print("Trying:", url)
            r = requests.get(url, stream=True, timeout=30)
            if r.status_code == 200:
                with open(fname, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print("Downloaded:", fname, "from", url)
                break
            else:
                print("URL returned status", r.status_code)
        except Exception as e:
            print("Download attempt failed:", e)
    else:
        raise RuntimeError("All download attempts failed. Provide a smaller clean FITS/CSV or enable a TAP-based workflow.")

# Read table
tbl = Table.read(fname)
print("Rows:", len(tbl))
print("Columns (sample):", tbl.colnames[:40])

# Helper to select column if present
def get_col(tbl, names):
    for n in names:
        if n in tbl.colnames:
            return tbl[n]
    return None

par1 = get_col(tbl, ['parallax_1','parallax1','parallax'])
par_err1 = get_col(tbl, ['parallax_error_1','parallax_error1','parallax_error'])
rproj_au = get_col(tbl, ['r_proj_au','rproj_au','r_proj'])
sep_arcsec = get_col(tbl, ['s','sep','sep_arcsec','r_ang'])
pmra_err1 = get_col(tbl, ['pmra_error_1','pmra_error1','pmra_err','pmra_error'])
pmdec_err1 = get_col(tbl, ['pmdec_error_1','pmdec_error1','pmdec_err','pmdec_error'])

# distance in pc
if par1 is not None:
    median_par = np.nanmedian(par1)
    if median_par > 1e-3:
        dist1_pc = 1000.0 / par1
    else:
        dist1_pc = 1.0 / par1
elif par1 is None and par_err1 is not None:
    # fallback if only single parallax column name different; try 'parallax' directly
    raise RuntimeError("Parallax column not found by heuristics; inspect table.colnames and adjust.")
else:
    dist1_pc = np.full(len(tbl), 100.0)

# projected separation in meters
if rproj_au is not None:
    r_proj_m = np.array(rproj_au, dtype=float) * AU
elif sep_arcsec is not None:
    r_proj_au_calc = np.array(sep_arcsec, dtype=float) * np.array(dist1_pc)
    r_proj_m = r_proj_au_calc * AU
else:
    # try RA/Dec compute if necessary (slower)
    ra1 = get_col(tbl, ['ra_1','ra1','ra'])
    dec1 = get_col(tbl, ['dec_1','dec1','dec'])
    ra2 = get_col(tbl, ['ra_2','ra2'])
    dec2 = get_col(tbl, ['dec_2','dec2'])
    if ra1 is not None and dec1 is not None and ra2 is not None and dec2 is not None:
        import astropy.coordinates as coord
        import astropy.units as u
        c1 = coord.SkyCoord(ra=np.array(ra1)*u.deg, dec=np.array(dec1)*u.deg)
        c2 = coord.SkyCoord(ra=np.array(ra2)*u.deg, dec=np.array(dec2)*u.deg)
        sep = c1.separation(c2).arcsec
        r_proj_au_calc = sep * np.array(dist1_pc)
        r_proj_m = r_proj_au_calc * AU
    else:
        raise RuntimeError('Cannot determine projected separation: no suitable columns found. Inspect tbl.colnames and adjust mapping.')

# pm error
if pmra_err1 is not None and pmdec_err1 is not None:
    pmerr_masyr = np.sqrt(np.array(pmra_err1, dtype=float)**2 + np.array(pmdec_err1, dtype=float)**2)
else:
    print('PM error columns not found; using default sigma_mu = 0.02 mas/yr')
    pmerr_masyr = np.full(len(tbl), 0.02)

dist_pc = np.array(dist1_pc, dtype=float)
sigma_v_kms = 4.74047 * pmerr_masyr * dist_pc

# orbital speed
M_tot = 2.0 * M_sun
v_kms = np.sqrt(G * M_tot / r_proj_m) / 1000.0

mask = np.isfinite(v_kms) & (v_kms > 1e-9)
alpha_eta_limits = np.full(len(tbl), np.nan)
alpha_eta_limits[mask] = 2.0 * (sigma_v_kms[mask] / v_kms[mask])

valid = ~np.isnan(alpha_eta_limits)
vals = alpha_eta_limits[valid]

print('Computed alpha*eta limits for', np.sum(mask), 'systems')
if len(vals) > 0:
    print('alpha*eta percentiles (10,50,90):', np.nanpercentile(vals, [10,50,90]))
else:
    print('No valid limits computed. Inspect columns and mask.')

# Save CSV
import csv
outname = 'alpha_eta_limits_sample.csv'
with open(outname, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['index','alpha_eta_limit','v_kms','sigma_v_kms','r_proj_au'])
    for i in range(len(tbl)):
        if valid[i]:
            writer.writerow([i, alpha_eta_limits[i], v_kms[i], sigma_v_kms[i], r_proj_m[i]/AU])
print('Wrote sample CSV:', outname)
