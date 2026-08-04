# scripts/run_elbadry_tap.py
import os
import numpy as np
import csv
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u
import time

# Constants
G = 6.67430e-11
M_sun = 1.98847e30
AU = 1.495978707e11

# Config from env
MAX_PRIMARIES = int(os.environ.get("GAIA_MAX_PRIMARIES", "200"))
A_MAX_AU = float(os.environ.get("GAIA_A_MAX_AU", "20000.0"))

print(f"MAX_PRIMARIES={MAX_PRIMARIES}, A_MAX_AU={A_MAX_AU}")

# 1) get a small sample of nearby primaries
adql_prim = f"""
SELECT source_id, ra, dec, parallax, parallax_error, pmra, pmdec, pmra_error, pmdec_error, phot_g_mean_mag, ruwe
FROM gaiadr3.gaia_source
WHERE parallax >= 10
  AND phot_g_mean_mag < 14
  AND ruwe < 1.4
ORDER BY parallax DESC
LIMIT {MAX_PRIMARIES}
"""
print("Submitting primary query...")
job = Gaia.launch_job_async(adql_prim)
prim_tbl = job.get_results().to_pandas()
print("Primaries:", len(prim_tbl))

def find_neighbors(primary_row, a_max_au=A_MAX_AU):
    ra = float(primary_row['ra']); dec = float(primary_row['dec']); par = float(primary_row['parallax'])
    if par <= 0 or np.isnan(par):
        return None
    dist_pc = 1000.0 / par
    ang_arcsec = a_max_au / dist_pc
    radius = (ang_arcsec/3600.0) * u.deg
    coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    # fetch minimal columns
    try:
        c = Gaia.cone_search_async(coord, radius, columns="source_id, ra, dec, parallax, parallax_error, pmra, pmdec, pmra_error, pmdec_error, phot_g_mean_mag, ruwe")
    except Exception as e:
        print("Cone search failed for primary", primary_row['source_id'], ":", e)
        return None
    tbl = c.get_results().to_pandas()
    tbl = tbl[tbl['source_id'] != primary_row['source_id']]
    if len(tbl) == 0:
        return None
    coords_neighbors = SkyCoord(ra=tbl['ra'].values*u.deg, dec=tbl['dec'].values*u.deg)
    sep = coord.separation(coords_neighbors).arcsec
    tbl = tbl.assign(sep_arcsec=sep, dist_pc=dist_pc)
    tbl = tbl.assign(r_proj_au = tbl['sep_arcsec'] * dist_pc)
    return tbl

results = []
start = time.time()
for idx, prow in prim_tbl.iterrows():
    neigh = find_neighbors(prow, a_max_au=A_MAX_AU)
    if neigh is None or len(neigh)==0:
        continue
    pmra_err = neigh['pmra_error'].fillna(0.02).astype(float).values
    pmdec_err = neigh['pmdec_error'].fillna(0.02).astype(float).values
    pmerr = np.sqrt(pmra_err**2 + pmdec_err**2)
    dist_pc = neigh['dist_pc'].astype(float).values
    sigma_v_kms = 4.74047 * pmerr * dist_pc
    r_proj_m = neigh['r_proj_au'].astype(float).values * AU
    M_tot = 2.0 * M_sun
    v_kms = np.sqrt(G * M_tot / r_proj_m) / 1000.0
    valid_mask = np.isfinite(v_kms) & (v_kms > 1e-9)
    for i in np.where(valid_mask)[0]:
        alpha_eta_limit = 2.0 * (sigma_v_kms[i] / v_kms[i])
        results.append({
            'primary_source_id': int(prow['source_id']),
            'neighbor_source_id': int(neigh.iloc[i]['source_id']),
            'r_proj_au': float(neigh.iloc[i]['r_proj_au']),
            'v_kms': float(v_kms[i]),
            'sigma_v_kms': float(sigma_v_kms[i]),
            'alpha_eta_limit': float(alpha_eta_limit),
            'primary_parallax_mas': float(prow['parallax']),
            'neighbor_parallax_mas': float(neigh.iloc[i]['parallax'])
        })

elapsed = time.time() - start
print("Completed in {:.1f}s; found {} pairs".format(elapsed, len(results)))
if len(results) > 0:
    arr = np.array([r['alpha_eta_limit'] for r in results])
    print('alpha*eta percentiles (10,50,90):', np.nanpercentile(arr, [10,50,90]))
else:
    print("No pairs found; consider raising MAX_PRIMARIES or A_MAX_AU.")

outname = 'gaia_small_alpha_eta_limits.csv'
with open(outname, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(results[0].keys()) if results else ['note'])
    if results:
        writer.writeheader()
        writer.writerows(results)
    else:
        writer.writerow({'note': 'no_results'})
print('Wrote', outname)
