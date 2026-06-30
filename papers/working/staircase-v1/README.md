# Replication Study — Pipeline Scripts

This folder contains the full analysis pipeline for the SCH rotational coherence staircase replication. The pipeline runs in sequence: `build_sample.py` → `rar_residual_analysis.py` → `enrich_and_audit.py`, followed by a set of independent diagnostic scripts that branch off the enriched catalogue.

All scripts expect to be run from the `replication/` directory with the source FITS files present in `replication/data/`. See [`data/README.md`](../data/README.md) for download links and file sizes.

---

## Pipeline Overview

```
data/
├── SDSSDR17_MaNGA_JAM_v2.fits
├── drpall-v3_1_1.fits
├── dapall-v3_1_1-3.1.0.fits
└── manga-firefly-v3_1_1-mastar.fits
        │
        ▼
build_sample.py
        │
        ▼
manga_merged.csv  (3,650 rows × 29 columns)
        │
        ▼
rar_residual_analysis.py
        │
        ▼
manga_merged_with_rar.csv  (3,650 rows × 35 columns)
        │
        ├──────────────────────────────────────────────┐
        ▼                                              ▼
enrich_and_audit.py                    diagnostic scripts (independent)
        │
        ├── manga_enriched.csv
        └── joint_partial_audit_output.txt
```

---

## Step 1 — `build_sample.py`

**Input:** Four FITS catalogues from `data/`
**Output:** `manga_merged.csv`

Loads all four source catalogues, applies the full quality cut sequence documented in the working paper (Section 3), and merges them on `plateifu`. Includes an alignment sanity check comparing `inc_deg` between JAM HDU2 and HDU4 — the pipeline will abort if the HDU row ordering is inconsistent.

Quality cuts applied in order:
- `Qual >= 1` (JAM visual quality)
- `drp3qual == 1` (DRP reduction quality)
- `Lambda_Re > 0`, `Sigma_Re > 0` (valid kinematics)
- `Re_arcsec_MGE > 0` (valid effective radius)
- `0.01 < z < 0.15` (redshift range)
- `target in {0, 2}` (primary sample only)
- `chi2_dof_cyl < 5` (JAM NFW model convergence)
- Inner join with Firefly MaStar VAC on `plateifu`
- Inner join with DAPall on `plateifu`, `DAPDONE == 1`, `DAPQUAL` CRITICAL bit clear
- `20 < STELLAR_SIGMA_1RE < 400` km/s

Output columns include cylindrical and spherical JAM masses, spin parameter `Lambda_Re`, the `log_excess` proxy (`log_Mt_Re_cyl - log_Ms_Re_cyl`), NSA and Firefly photometric masses, DAP velocity dispersions, and DRPall structural parameters.

**Note on DAP data:** The DAP velocity dispersion maps (`STELLAR_SIGMA_1RE`) were retrieved and are present in the merged CSV, but base noise levels were too high to produce reliable baryonic acceleration estimates $g_{\text{bar}}$. The `log_excess` proxy is used in place of the full RAR residual throughout this analysis.

```bash
python build_sample.py
```

---

## Step 2 — `rar_residual_analysis.py`

**Input:** `manga_merged.csv`
**Output:** `manga_merged_with_rar.csv`

Computes four RAR residual variants from the merged sample and assigns stellar mass tertiles. The four residual columns added are:

| Column | Description |
|--------|-------------|
| `rar_resid` | Primary JAM cylindrical RAR residual |
| `rar_resid_sph` | Spherical JAM cross-check residual |
| `rar_resid_nsa` | NSA photometric mass residual (control estimator) |
| `rar_resid_firefly` | Firefly photometric mass residual (primary control estimator) |

Also assigns `mass_tertile` (Low / Mid / High) based on `log_Ms_Re_cyl` tertile boundaries:
- Low: `log_Ms_Re_cyl < 10.248`
- Mid: `10.248 ≤ log_Ms_Re_cyl ≤ 10.881`
- High: `log_Ms_Re_cyl > 10.881`

```bash
python rar_residual_analysis.py
```

---

## Step 3 — `enrich_and_audit.py`

**Input:** `manga_merged_with_rar.csv`
**Output:** `manga_enriched.csv`, `joint_partial_audit_output.txt`

Two-stage script. **Step 1 (enrich):** adds additional columns from the FITS files that were not included in the initial merge — specifically `beta_z` (from JAM HDU2, joined by row index to HDU1 `plateifu`), `LW_AGE_1Re` (light-weighted stellar age from Firefly HDU2), `LW_Z_1Re` (light-weighted metallicity), `nsa_sersic_n` (Sérsic index from DRPall), `Eps_MGE` (ellipticity), `log_Re_kpc` (effective radius in kpc), and `kin_class` (fast/slow classification at `Lambda_Re = 0.31`).

**Step 2 (audit):** runs the full joint partial correlation audit across four control sets and all subsamples. This is the source of the Table 2.1 results in Paper B and the working paper. Produces four audit sections:
- **Part A:** Progressive control sets — raw → `|Ms,Re` → `|Ms,Re,n,age` → `|Ms,Re,n,age,ε` across Full, Fast, Slow, Low, Mid, High, Mid_fast, High_slow subsamples, for both JAM and Firefly residuals
- **Part B:** Inclination mediation chain — tests whether `inc_deg_cyl` mediates the `beta_z` → RAR residual relationship
- **Part C:** Quintile staircases — confound-adjusted Q1–Q5 staircase for Full, Fast, Slow, Mid subsamples
- **Part D:** Sérsic n isolation — tests whether Sérsic index alone drives the signal

The key result from `joint_partial_audit_output.txt` — partial Spearman $\rho = +0.128$, $p = 6.98 \times 10^{-7}$ for the Full sample under the joint control set, robust to $\sigma_e$ inclusion — is reported in Paper B Section 2.3 and the working paper Section 5.

```bash
python enrich_and_audit.py
```

---

## Diagnostic Scripts

The following scripts run independently on `manga_enriched.csv` (or `manga_merged_with_rar.csv`) and do not need to be run in any particular order. They produced the diagnostic outputs that informed the methodological decisions documented in the working paper.

### `beta_z_audit.py`
Early audit of the `beta_z` signal before the full joint partial framework. Output: `beta_z_audit_output.txt`.

### `beta_z_analysis.py`
Extended `beta_z` analysis including mass tertile breakdowns and the Scenario B/B*/C classification framework described in Paper B Section 2.3.

### `sigma_projection_check.py`
Tests whether `STELLAR_SIGMA_1RE` (observed velocity dispersion) is driving the `beta_z` signal as a proxy rather than `beta_z` itself. Establishes that the signal survives $\sigma_e$ inclusion in fast rotators (Scenario C) but not slow rotators (Scenario B). Output: `sigma_projection_output.txt`.

### `sigma_classification.py`
Classifies galaxies by kinematic regime (fast/slow) and examines how the signal behaves across the classification boundary. Output: `sigma_classification_output.txt`.

### `inclination_dissection.py`
Investigates the inclination artifact identified in the JAM-based RAR residual for slow rotators. Traces the four-step mediation chain: `inc_deg → STELLAR_SIGMA_1RE → rar_resid`, and confirms the artifact is fully mediated by $\sigma_e$ in the JAM residual but absent from the Firefly residual. This is the basis for the mediation table (Table 2.2) in Paper B and the working paper Section 5.5. Output: `inclination_dissection_output.txt`.

### `inspect_columns.py`
Utility script. Prints column availability, dtypes, and non-null counts across the working catalogues. Used during pipeline development to diagnose HDU structure issues.

### `inspect_anisotropy.py`
Examines the `beta_z` distribution across kinematic subsamples. Note: filename contains a typo (`inspect_anistropy.py` on disk) — the script itself is correctly named in its docstring. Output: `inspect_anistropy_output.txt`.

### `re_projection_check.py`
Checks for re-projection effects in the effective radius and inclination estimates. Output: `re_projection_output.txt`.

---

## Intermediate Catalogues

| File | Produced by | Rows | Columns | Description |
|------|------------|------|---------|-------------|
| `manga_merged.csv` | `build_sample.py` | 3,650 | 29 | Quality-cut merged sample, no RAR residuals |
| `manga_merged_with_rar.csv` | `rar_residual_analysis.py` | 3,650 | 35 | Adds four RAR residual variants and `mass_tertile` |
| `manga_enriched.csv` | `enrich_and_audit.py` | 3,650 | ~45 | Adds `beta_z`, ages, metallicities, Sérsic n, ellipticity |

---

## Environment

```
Python 3.12
numpy
pandas
scipy
astropy
```

Install dependencies into a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy pandas scipy astropy
```

The `venv/` directory is not committed to this repository.

---

## Running the Full Pipeline

```bash
cd replication/
source venv/bin/activate

python build_sample.py               # → manga_merged.csv
python rar_residual_analysis.py      # → manga_merged_with_rar.csv
python enrich_and_audit.py           # → manga_enriched.csv + joint_partial_audit_output.txt

# Optional diagnostics (any order):
python beta_z_analysis.py
python sigma_projection_check.py
python inclination_dissection.py
python sigma_classification.py
python inspect_anisotropy.py
python re_projection_check.py
```

Total runtime on a modern desktop: approximately 10–20 minutes, dominated by loading the Firefly MaStar FITS file (~6.1 GB).

---

*June 2026 | Variable Systems*
