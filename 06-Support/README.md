# `06-Support` 

## Data, Code, and Non-Claim Material

This folder holds the material that backs specific empirical results
in the papers, but doesn't itself make any theoretical claim. Nothing
here carries an epistemic status tier the way documents in `canonical/`
or `superseded/` do — it's infrastructure, not argument.

## `staircase-v1/`

The complete analysis pipeline behind Paper B Section 2 (the MaNGA DR17
`beta_z` partial-correlation replication): the sample-construction and
statistical-analysis scripts, their raw output logs, the merged and
enriched data tables, and the two draft/final result write-ups that
preceded Paper B's own prose account of the same result.

| Subfolder | Contents |
|---|---|
| `scripts/` | The actual analysis code — sample construction, the audits described in Paper B Section 2.5, the inclination-artifact investigation of Section 2.5, and the primary `beta_z` correlation analysis. |
| `outputs/` | Logged output from each script run, plus the merged catalogues (`manga_merged.csv`, `manga_merged_with_rar.csv`, `manga_enriched.csv`) the analysis is built on. |
| `docs/` | Draft and final write-ups of the result, produced before it was folded into Paper B's own prose. |

If you want to check Paper B Section 2's numbers rather than take them
on faith, this is where you'd rerun the pipeline. `staircase-v1/`
has its own `README.md` with more specific instructions — check there
first for anything about running the scripts themselves.

## Adding to This Folder

If a future test in Paper B or elsewhere generates its own analysis
pipeline (the JWST standard ruler test, the antipodal CMB correlation
search, and others are proposed but not yet executed), it should get
its own versioned subfolder here, following the same
scripts/outputs/docs pattern as `staircase-v1/`.
