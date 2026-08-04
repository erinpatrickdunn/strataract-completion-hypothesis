Notebook to run Gaia El-Badry catalog analysis

This notebook downloads the El-Badry Gaia EDR3 wide-binary catalog and computes conservative 1-sigma upper limits on alpha*eta using the phenomenological mapping in the project's Paper A (G_eff = G(1 + alpha*eta)).

Usage:
- Open the notebook in Colab (use the existing COLAB file or link) or clone the repo and run locally with Jupyter.
- The notebook attempts to detect common column names; if it fails to find projected separation/pm error columns, edit the mapping section near the top where `get_col` choices are listed.

Caveats:
- It uses projected separation as an estimator for orbital semimajor axis (circular orbit assumption).
- Uses proper-motion uncertainties only (transverse velocity). For many systems spectroscopic RVs are needed for stronger constraints.
- alpha*eta limits are per-system; combine systems statistically for a population bound.
