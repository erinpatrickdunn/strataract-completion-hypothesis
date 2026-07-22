# `06-Support/` — Data, Code, Verification, and Empirical Support

This directory contains the computational, empirical, and verification
materials that support the canonical SCH theory.

Unlike the documents in `04-Canonical-Theory/`, the contents of this
directory do **not** establish or extend the theoretical framework
itself. Instead, they provide the analyses, software, replication
studies, datasets, and supporting infrastructure used to evaluate,
reproduce, or test canonical claims.

Support documents are evidence and infrastructure rather than
theoretical authority.

---

## `SCH_Replication_Study_WorkingPaper_v1.md`

A working paper documenting the first independent replication pipeline
investigating rotational coherence as a gravitational source variable.

This document records the initial computational results obtained from
clean data acquisition and pipeline execution. It is explicitly a
**working paper**, not a canonical theoretical document, and should be
understood as an evolving empirical investigation pending additional
datasets and future analysis.

---

## `staircase-v1/`

The complete analysis pipeline behind Paper B Section 2 (the MaNGA DR17
`beta_z` partial-correlation replication): sample construction,
statistical analysis, audit scripts, intermediate datasets, output
logs, and the draft reports that preceded Paper B's final presentation
of the same result.

| Subfolder  | Contents                                                                                                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scripts/` | Analysis code used to construct the sample, perform statistical tests, execute audit procedures, and investigate possible observational artifacts. |
| `outputs/` | Logged output from each analysis run together with the merged and enriched catalogues used throughout the study.                                   |
| `docs/`    | Draft and final reports generated before the results were incorporated into Paper B.                                                               |

Researchers wishing to independently reproduce the Paper B analysis
should begin here. The directory contains its own `README.md`
describing the execution workflow in greater detail.

---

## `track-b/`

Supporting material associated with active Track B investigations.

Track B contains research that is intentionally separated from the
canonical corpus while undergoing further investigation, validation,
or reconstruction. Material placed here should not be interpreted as
adopted canonical theory unless explicitly promoted through the
governance process.

---

## Scope of This Directory

Typical contents include:

* computational analysis pipelines,
* datasets,
* software,
* numerical experiments,
* replication studies,
* validation reports,
* observational investigations,
* supporting documentation.

Documents in this directory may support canonical claims, challenge
them, or simply provide the infrastructure required to reproduce
published results. They do not, by themselves, establish the canonical
theory.

---

## Adding to This Directory

Future empirical investigations should generally receive their own
versioned subdirectory following the same organizational pattern as
`staircase-v1/`, separating:

* source code,
* generated outputs,
* datasets,
* and supporting documentation.

Keeping computational work isolated from the canonical papers preserves
a clear distinction between **theory**, **evidence**, and
**implementation**, while ensuring that every published result remains
fully reproducible.

