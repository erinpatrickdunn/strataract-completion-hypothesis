Phenomenological weak-field notebook

This directory addition contains a small notebook that implements the minimal phenomenological mapping from Paper A (SCH) to weak-field observables (wide binaries and galaxy lensing).

Files added:
- 06-Support/phenom_wf_binary_and_lensing.ipynb : Jupyter notebook with formulas, example numeric scans, and plots.

Assumptions made (document these before publishing results):
- eta (the coupling efficiency) is approximately constant on the scale of the system being modeled.
- quadratic terms and torsion-quadratic terms are negligible at the densities of interest (galactic and wide-binary densities).
- axial current A_mu ~ 0 in regions tested (no strong torsion background).
- small-coupling expansion: alpha * eta << 1.

Suggested next steps:
1) Run the notebook locally and inspect numeric outputs; adjust system parameters to match the systems of interest (binary separations, galaxy masses, measurement precisions).
2) If the bounds look constraining, pick target datasets (Gaia wide-binary catalogs; published stacked-shear results from DES/KiDS/HSC) and compute conservative constraints by comparing measurement precision to the model's predicted fractional shifts.
3) For rigor: extract the action and perform the linearized derivation in Appendix P to derive PPN-like parameters and to justify dropping the quadratic/torsion terms for the systems considered.

I will open an issue summarizing the assumptions, the notebook, and follow-ups unless you want me to proceed differently.
