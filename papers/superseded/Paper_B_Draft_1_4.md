**Paper B -- Draft 1.4 | June 2026**

**Rotational Coherence as a Gravitational Source Variable:**

**Empirical Evidence, Observational Directions, and Laboratory Tests**

**Draft 1.4 | June 2026**

*Companion paper to: Geometric State as a Gravitational Source Variable: A Multi-Scale Framework and Falsifiable Test Program (Paper A, Draft 2.0). Appendix P v8 contains the formal proofs.*

Revised from Draft 1.3: Section 2 replaced in full — the original lambda\_R quintile staircase analysis is superseded by an independent replication using the JAM velocity anisotropy parameter beta\_z and the Firefly photometric mass estimator (sample N = 3,650; Zhu et al. 2023; Lu et al. 2024; Neumann et al. 2022). The beta\_z replication resolves the Jeans estimator bias and the lambda\_R proxy definition problem identified in external review. Companion paper reference updated to Appendix P v7. All other sections unchanged from Draft 1.3. Supersedes Draft 1.3.

Prior revision summary: Draft 1.3 corrected the JWST framing in Section 4 and added the antipodal CMB correlation search in Section 7. Draft 1.2 added the JWST standard ruler topology test, post-merger lensing timescale test, Ampère force anomaly, and NANOGrav exploratory direction.

**Prefatory Note -- Draft 1.4**

Draft 1.1 presented the MaNGA DR17 RAR quintile staircase and the Earth flyby anomaly cross-scale consistency check. Draft 1.2 added four new observational and laboratory directions motivated by the closed variational framework of Paper A Draft 1.4: a JWST standard ruler topology test, a post-merger lensing timescale test, the Ampère force anomaly as a terrestrial laboratory test, and the NANOGrav gravitational wave background as an exploratory observational direction.

Draft 1.3 makes two changes. First, Section 4 is updated to correct the JWST framing in alignment with Paper A Draft 1.5: the observed anomaly is galaxies that are **too massive, too compact, and too early** relative to ΛCDM predictions, not anomalously large in angular size. The Little Red Dots open question is noted. The rest-frame UV measurement limitation at z>8 is stated explicitly. The Roman Space Telescope's relevance is reframed: its value for this framework is wide-field clustering statistics for the S³ angular diameter turnaround test across the predicted turnaround redshift range z ~ 2-8, not resolved sizes of high-z objects. Second, Section 7 is expanded with a new exploratory direction: the antipodal CMB correlation search on S³, presented with identical epistemic status structure to the NANOGrav section.

Draft 1.4 replaces Section 2 in full. The original lambda\_R quintile staircase is superseded by an independent replication using the JAM velocity anisotropy parameter beta\_z and the Firefly photometric mass estimator. The replication resolves the Jeans estimator bias and the lambda\_R = 0 proxy definition problem identified in external review. The beta\_z signal (rho = +0.128, p = 6.98e-15, N = 3,643) survives a fully JAM-independent joint control set and is robust to observed velocity dispersion inclusion. An inclination artifact in the JAM-based RAR residual was identified and fully traced to sigma\_e projection in slow rotators; it does not contaminate the Firefly result. The DES Y6 weak lensing cross-match is identified as the critical outstanding test.

The framework is not assumed to be correct. All results are presented as observational signatures requiring explanation, consistency checks, or proposed tests with explicit falsification conditions.

**Epistemic status conventions used throughout this paper:**

| **Status label** | **Meaning** |
| --- | --- |
| **RESULT** | Computed from public data; analysis presented in this paper |
| **CONSISTENCY CHECK** | Independent empirical handle on framework parameters; not primary confirmation |
| **PROPOSED TEST** | Experimental or observational programme not yet executed; falsification condition stated |
| **EXPLORATORY** | Candidate interpretation only; requires further formal development and calibration |

**Abstract**

Paper A (Geometric State as a Gravitational Source Variable, Draft 1.5) derives that the geometric organizational state of matter constitutes an independent gravitational source variable, predicting that galaxies with higher rotational coherence should produce stronger effective gravitational sourcing at fixed baryonic mass. This paper presents the observational and laboratory evidence programme motivated by that framework.

Section 2 reports an independent replication of the rotational coherence signal using the JAM velocity anisotropy parameter beta\_z and a fully photometric mass estimator (Firefly MaStar; Neumann et al. 2022), drawn from a sample of 3,650 MaNGA galaxies with JAM dynamical model fits (Zhu et al. 2023; Lu et al. 2024). The full-sample partial Spearman correlation between beta\_z and the Firefly RAR residual, controlling for photometric stellar mass, effective radius, Sersic index, and light-weighted age, is rho = +0.128, p = 6.98e-15. The signal is robust to the additional inclusion of the observed velocity dispersion sigma\_e in the control set (rho = +0.127, p = 1.38e-14), confirming it is not a sigma\_e proxy. The signal holds in fast rotators across all mass tertiles. In slow rotators and high-mass slow rotators, beta\_z and sigma\_e share sufficient variance that the signal does not survive sigma\_e inclusion, consistent with the SCH contrast class prediction for pressure-dominated systems near the isotropic gravitational ground state.

Section 3 presents a cross-scale consistency check using the Earth flyby anomaly dataset: six spacecraft exhibiting anomalous velocity changes during Earth gravity-assist maneuvers. The sign of the anomalous velocity change is exactly determined by the geometric asymmetry of each trajectory (p = 0.016 by chance). Four geometrically clean flybys yield K = (2.97 ± 0.15) × 10⁻⁶, consistent with the dimensional prediction $2\omega_E R_E/c = 3.10 \times 10^{-6}$ to within 4%.

Section 4 proposes a JWST standard ruler test of the S³ spatial topology derived in Paper A Section 2.9: the angular diameter distance turnaround on a three-sphere predicts that galaxies beyond a characteristic redshift z\_turn appear larger with increasing distance, providing a one-parameter fit with a sharp falsification condition. Updated in Draft 1.3 to correct the JWST framing and reframe the Roman Space Telescope's role.

Section 5 proposes a post-merger lensing timescale test of the spinor condensate diffusion prediction $\tau_{\text{diff}} \sim R^2 m_{\text{eff}} / \hbar$. Section 6 presents the Ampère force anomaly as a terrestrial laboratory test of Term 2 geometric coupling in ballistic electron flow, with a proposed calorimetric comparison between resistive and superconducting configurations. Section 7 presents the NANOGrav gravitational wave background and the antipodal CMB correlation search as exploratory observational directions.

# **1\. Introduction**

Paper A (Draft 1.5) derives a closed variational framework in which the geometric organizational state of matter constitutes an independent gravitational source variable. The field equation

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\left[T_{\mu\nu} + \alpha\, C_{\mu\nu}\right]$$

produces three terms: standard stress-energy (Term 1), the propagating spinor condensate $C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$ (Term 2), and the torsion contact interaction (Term 3). The framework is closed in the sense that all leading-order claims are derived from the Einstein-Cartan-Dirac action rather than postulated. The epistemic status of every claim is documented in Paper A's framework epistemic status table.

This paper serves the function defined at the outset: communicating potential directions for study. It presents one set of results computed from existing public data (Section 2), one cross-scale consistency check (Section 3), three proposed observational or laboratory tests (Sections 4, 5, 6), and two exploratory directions (Section 7). None of these results or proposals is presented as confirmation of the framework. Each is presented as an observational signature requiring explanation, a consistency check, or a proposed test with an explicit falsification condition that standard models predict will not be exceeded.

The systems absent from the anomaly cluster documented in Paper A Section 1 -- globular clusters, dwarf irregulars, pressure-supported systems, laboratory systems -- are precisely those with randomized orbital orientations and minimal rotational coherence. The contrast class is as informative as the anomaly class. Both are kept in view throughout this paper.

**2\. The Galactic Scale: MaNGA DR17 Replication \[RESULT\]**

EPISTEMIC STATUS: RESULT. Computed from public data; independent replication pipeline. Supersedes the lambda\_R quintile staircase reported in Draft 1.1.

## **2.1 Background: Why the Original Analysis Was Superseded**

The original MaNGA staircase (Draft 1.1) sorted galaxies into quintiles by 1/sigma\_star as a proxy for rotational coherence and reported a monotonic RAR residual dependence with a Q1–Q5 span of 0.44 dex. External review identified two problems that required the analysis to be rebuilt from scratch.

First, the Jeans mass estimator used to compute baryonic accelerations systematically underestimates the true dynamical mass of pressure-supported slow rotators. Because slow rotators sit in Q1 (high sigma\_star, classified as low coherence), this bias inflates the apparent RAR residual for exactly the galaxies predicted to show the strongest signal, producing an artefactual staircase in the direction predicted by the framework. Replacing sigma-derived masses with photometric masses from Firefly SED fitting (Neumann et al. 2022) removes this bias.

Second, and more fundamentally, the proxy variable was incorrectly defined. The projected spin parameter lambda\_R collapses to zero for face-on fast rotators regardless of their true rotational state, because projection removes the line-of-sight rotation signal. The identification lambda\_R = 0 with geometric coherence = 0 is therefore wrong for a significant fraction of the sample. The replacement variable beta\_z, the JAM velocity anisotropy parameter from the DynPop JAM v2 catalogue (Zhu et al. 2023; Lu et al. 2024), measures the degree to which stellar orbits are tangentially versus radially organised after full deprojection. It does not carry this inclination ambiguity.

## **2.2 Dataset and Sample Selection**

The primary kinematic and mass catalogue is the MaNGA DynPop JAM v2 release (Zhu et al. 2023, Paper I; Lu et al. 2024, Paper V), accessed from Zenodo record 17518315. The catalogue provides JAM dynamical mass modelling results for 10,296 MaNGA DR17 galaxies. We use the JAMcyl + NFW model (HDU4) as our primary source of the velocity anisotropy parameter beta\_z and the enclosed stellar mass log\_Ms\_Re\_cyl within the effective radius.

The photometric mass estimator is the MaNGA Firefly DR17 Value Added Catalogue (Neumann et al. 2022), which provides photometric stellar masses (PHOTOMETRIC\_MASS) from SED fitting using the MaStar stellar population models. Firefly masses are used as the primary mass estimator in all RAR residual computations and as the mass control variable in all partial correlations, ensuring complete independence from JAM model structure.

Structural parameters (Sersic index nsa\_sersic\_n) are drawn from the MaNGA DRP catalogue. Light-weighted stellar age (LW\_AGE\_1Re) is drawn from the Firefly GLOBAL\_PARAMETERS extension. Effective radius (Re\_kpc) is taken from the JAM v2 HDU1 catalogue.

Quality cuts applied in sequence: JAM visual quality Qual >= 1; DRP reduction quality drp3qual = 1; primary sample targeting (mngtarg1 in {0, 2}); JAM model fit quality chi2\_dof\_cyl < 5; redshift z > 0.01. Working sample: N = 3,650 galaxies.

## **2.3 The beta\_z Signal: Partial Correlation Results**

The primary test statistic is the partial Spearman rank correlation between beta\_z and the Firefly RAR residual, controlling for PHOTOMETRIC\_MASS, log\_Re\_kpc, nsa\_sersic\_n, and LW\_AGE\_1Re simultaneously. All four control variables are independent of the JAM kinematic model. An additional robustness check adds the observed velocity dispersion STELLAR\_SIGMA\_1RE to the control set.

Three scenarios are defined for classifying the robustness of the signal to sigma\_e inclusion. Scenario C: signal robust to sigma\_e inclusion (drop < 20%); strongest result. Scenario B\*: signal attenuated but remains statistically significant after sigma\_e inclusion; genuine attenuation, not washout. Scenario B: signal collapses to non-significance after sigma\_e inclusion; both specifications reported; confounder vs mediator cannot be distinguished from correlations alone.

**Table 2.1. beta\_z partial correlations against Firefly RAR residual.**

*B = partial rho(beta\_z, rar\_FF) | PHOTOMETRIC\_MASS, log\_Re\_kpc, nsa\_sersic\_n, LW\_AGE\_1Re. C = same + STELLAR\_SIGMA\_1RE. All mass controls are JAM-independent. B\* row (highlighted) = attenuated but significant. Scen. colour: green = C (robust), amber = B\* (attenuated), red = B (washed out). \*\*\* p<0.001 \*\* p<0.01 \* p<0.05 ns p>=0.05.*

| **Subsample** | **N** | **ρ (B)** | **p (B)** | **sig** | **ρ (C)** | **p (C)** | **sig** | **Scen.** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full | 3643 | +0.128 | 6.98e-15 | \*\*\* | +0.127 | 1.38e-14 | \*\*\* | **C** |
| Fast | 2829 | +0.135 | 6.67e-13 | \*\*\* | +0.137 | 2.36e-13 | \*\*\* | **C** |
| Slow | 814 | +0.122 | 4.76e-04 | \*\*\* | +0.063 | 7.41e-02 | ns | **B** |
| Low | 1217 | +0.151 | 1.19e-07 | \*\*\* | +0.158 | 3.09e-08 | \*\*\* | **C** |
| Mid | 1210 | +0.154 | 7.29e-08 | \*\*\* | +0.152 | 1.01e-07 | \*\*\* | **C** |
| High | 1216 | +0.116 | 4.88e-05 | \*\*\* | +0.076 | 7.64e-03 | \*\* | **B\*** |
| Mid\_fast | 1086 | +0.165 | 4.64e-08 | \*\*\* | +0.162 | 8.28e-08 | \*\*\* | **C** |
| High\_slow | 584 | +0.122 | 3.17e-03 | \*\* | +0.044 | 2.85e-01 | ns | **B** |

## **2.4 Key Findings**

-   Full sample and fast rotators (Scenario C). The beta\_z signal survives all controls including sigma\_e, using a fully JAM-independent control set. This is the primary result. rho = +0.128, p = 6.98e-15 (N = 3,643) without sigma\_e; rho = +0.127, p = 1.38e-14 with sigma\_e. The signal is not a kinematic dispersion proxy.
-   Low, Mid, and Mid\_fast mass subsamples (Scenario C). Signal consistent and robust across the mass distribution where the fast rotator population dominates.
-   High-mass mixed subsample (Scenario B\*). Signal drops from rho = +0.116 (p < 0.001) to rho = +0.076 (p = 7.64e-03, \*\*) after sigma\_e inclusion. Effect is attenuated but remains significant at p < 0.01. The larger slow rotator fraction at high mass pulls the mixed-population partial toward the pressure-dominated regime.
-   Slow rotators and High\_slow (Scenario B). In maximally pressure-dominated systems, beta\_z and sigma\_e encode overlapping aspects of the same dynamical state. The signal does not survive sigma\_e inclusion. Both Column B and Column C are reported. This is consistent with the SCH contrast class prediction: systems near the isotropic gravitational ground state are not expected to show a clean geometric coherence signal.

## **2.5 Methodological Note: Inclination Artifact in JAM Residual**

During the analysis, a strong correlation was identified between JAM model inclination (inc\_deg\_cyl) and the JAM-based RAR residual in slow rotators: rho = +0.465, p = 5.03e-45. Full investigation established that this is a kinematic projection artifact propagating through a four-step mediation chain.

**Table 2.2. Sigma\_e mediation chain: rho(inc, RAR residual) in slow rotators (N = 814-815).**

*Step D controls for PHOTOMETRIC\_MASS and STELLAR\_SIGMA\_1RE simultaneously. Green row = key result.*

| **Step** | **N** | **ρ** | **p** | **sig** | **Verdict** |
| --- | --- | --- | --- | --- | --- |
| A: ρ(inc, σe) | 815 | +0.168 | 1.36e-06 | \*\*\* | inc → σe confirmed |
| B: ρ(σe, rar\_FF) | 814 | +0.651 | 3.41e-99 | \*\*\* | σe → RAR residual confirmed |
| C: ρ(inc, rar\_FF) raw | 814 | +0.150 | 1.71e-05 | \*\*\* | inc → RAR apparent |
| D: ρ(inc, rar\_FF) \| $M_*$, $\sigma_e$ | 814 | +0.019 | 5.85e-01 | ns | **Fully mediated ✓** |

Step D collapses to rho = +0.019, p = 0.585, ns. The mechanism is: edge-on slow rotators present elevated line-of-sight velocity dispersion due to mild oblateness or triaxiality; elevated sigma\_e inflates the kinematic acceleration estimate g\_obs; the JAM RAR residual tracks inclination through the kinematic channel, not the mass channel. The Firefly RAR residual is free of this artifact at first order: rho(inc, rar\_resid\_firefly) = +0.006, ns, for the full sample before any controls. This confirms Firefly as the appropriate primary estimator. The JAM-based RAR residual is not used as primary evidence for the beta\_z signal.

One exception is noted. In intermediate-mass slow rotators (Mid\_slow, N = 124), both the JAM and Firefly residuals show elevated inclination correlations (rho\_JAM = +0.361, rho\_FF = +0.309), indicating that inclination enters the photometric residual through a channel independent of JAM model structure. The most plausible mechanism is dust attenuation: incomplete correction in the Firefly SED fitting for edge-on intermediate-mass slow rotators. This cell is flagged as an open question. It does not affect the full-sample or fast-rotator primary results.

## **2.6 Why LCDM Does Not Naturally Produce the beta\_z Signal**

The four LCDM mechanisms considered in the original analysis (halo assembly history, baryon feedback, IMF variation, structural non-homology) remain insufficient to produce the observed beta\_z-RAR residual relationship. None of these mechanisms predicts a monotonic dependence on orbital anisotropy at fixed photometric stellar mass, effective radius, Sersic index, and stellar age. The signal survives the full control set precisely because those controls capture the structural and evolutionary properties that LCDM assembly physics would implicate. What remains after controlling for all four is the anisotropy of the velocity ellipsoid, which LCDM has no mechanism to couple to gravitational sourcing at fixed mass.

# **3\. Cross-Scale Consistency: The Earth Flyby Anomaly \[CONSISTENCY CHECK\]**

*EPISTEMIC STATUS: CONSISTENCY CHECK*

The Earth flyby anomaly occupies an unusual epistemic position. The mainstream community largely considers it resolved by thermal recoil forces — a modelled explanation in which anisotropic heat emission from the spacecraft produces a small net force that accounts for the observed velocity residuals. That explanation is plausible and physically reasonable. It is also not directly measured: the thermal model requires specific assumptions about spacecraft surface emissivity, heat pipe geometry, and radiative pressure distribution that were not independently verified on the relevant spacecraft at the relevant epochs. The model fits the anomaly, which is not the same as eliminating it. The sign-lock result and K-cluster documented below are empirical patterns in the data. Whether the thermal recoil model genuinely accounts for those patterns, or whether it is a sufficiently flexible post-hoc fit, has not been definitively established. The anomaly is presented here as a consistency check — an independent empirical handle on the coupling constant K at a scale 14 orders of magnitude removed from the galactic analysis — with the honest acknowledgement that the community’s preferred resolution is plausible but modelled rather than proven. The sign-lock and K-cluster are observational patterns requiring explanation. They are not primary evidence for the framework, and the thermal recoil explanation is not dismissed. Both claims are held open.

## **3.1 The Anderson Formula and Sign-Lock Result**

Anderson et al. (2008) reported that six spacecraft showed velocity changes at closest approach during Earth gravity-assist maneuvers that could not be accounted for by standard gravitational models. The empirical formula Delta\_v\_inf = K \* v\_inf \* (cos\_delta\_in − cos\_delta\_out) fits five of the six flybys, where Delta\_cos\_delta = cos\_delta\_in − cos\_delta\_out is the geometric trajectory asymmetry relative to Earth's equatorial plane.

Across all six flyby events, sgn(Delta\_v\_inf) = sgn(Delta\_cos\_delta) holds without exception. The two negative-residual events (Galileo II: Delta\_v\_inf = −4.60 mm/s; Cassini: Delta\_v\_inf = −2.00 mm/s) both have negative Delta\_cos\_delta. The probability of this occurring by chance across six independent events is $2^{-6} = 0.016$.

## **3.2 The K-Cluster**

| **Spacecraft** | **v\_inf (km/s)** | **Delta\_cos\_delta** | **Delta\_v\_inf (mm/s)** | **K × 10⁻⁶** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| Galileo I | 8.949 | +0.1486 | +3.92 | 2.97 | Clean |
| Galileo II | 8.891 | −0.1699 | −4.60 | 3.05 | Clean |
| NEAR | 6.851 | +0.6254 | +13.46 | 3.14 | Clean |
| Rosetta I | 3.863 | +0.1725 | +1.82 | 2.73 | Clean |
| Cassini | 16.010 | −0.0217 | −2.00 | 5.76 | Outlier \|Delta_cos_delta\| &lt; 0.10 |
| MESSENGER | 10.389 | +0.0009 | +0.02 | 2.14 | Near-null geometry |

Four geometrically clean flybys (|Delta\_cos\_delta| > 0.10) yield $K_{\text{mean}} = (2.97 \pm 0.15) \times 10^{-6}$, consistent with $2\omega_E R_E/c = 3.10 \times 10^{-6}$ to within 4%.

## **3.3 Dimensional Structure and Scale Connection**

The dimensional estimate $2\omega_E R_E / c = 3.10 \times 10^{-6}$ was noted by Anderson et al. but not derived from first principles. The framework provides a physical interpretation: K encodes the coupling between a spacecraft trajectory and Earth's rotational geometric organizational state, and the natural scale of that coupling is the ratio of rotational surface velocity to c. The formal connection is $K \approx \alpha \times (v_{\text{rot}}/c) \times f_{\text{geom}}$, where alpha is the action coupling constant (to be fixed by the Bi-209 calibration, Paper A Section 5) and f\_geom is an order-unity geometric projection factor (Calculational Target ix of Paper A Section 6.6).

The same v\_rot/c dimensional structure appears at galactic scale: for a galaxy with $v_{\text{rot}} \approx 200$ km/s, $v_{\text{rot}}/c \approx 6.7 \times 10^{-4}$. The two independent empirical handles on the coupling constant — separated by fourteen orders of magnitude in spatial scale — are consistent with this prediction to within available precision. This consistency does not confirm the framework. Inconsistency would be a significant strike against it. It is also worth noting that the sign-lock result (sgn(Delta\_v\_inf) = sgn(Delta\_cos\_delta) across all six events, p = 0.016) is a geometric pattern that the thermal recoil model does not naturally predict: thermal recoil depends on spacecraft surface properties, not on the equatorial geometry of the trajectory. The fact that the anomaly direction tracks the equatorial asymmetry Delta\_cos\_delta rather than any spacecraft-specific property is the element of the dataset that the thermal explanation has most difficulty accounting for. This is noted without asserting that the thermal model is wrong — it may well incorporate geometric effects through secondary coupling mechanisms not yet fully modelled. It is noted because it is the honest description of what the data shows.

# **4\. The JWST Standard Ruler Topology Test \[PROPOSED TEST\]**

*EPISTEMIC STATUS: PROPOSED TEST*

This section proposes an observational test using existing JWST and HST data, with extensions identified for Roman Space Telescope and HWO. The test has not been performed. It has a single free parameter (R\_universe), a sharp falsification condition, and minimal dependence on the speculative cosmological machinery of Paper A. The angular diameter distance formula on S³ is standard differential geometry, not a claim of the framework. **Updated in Draft 1.3**: JWST framing corrected; LRD open question noted; rest-frame UV measurement limitation at z>8 stated; Roman Space Telescope role reframed.

## **4.1 The Prediction**

Paper A Section 2.9 derives that the spatial topology of the universe is compatible with S³ (the three-sphere), with the derivation grounded in the SU(2) group manifold identification and the canonical spin structure argument (Appendix P Section P.7.6). On S³ of radius R\_universe, the angular diameter distance as a function of proper distance d\_proper is:

$$d_A = R_{\text{universe}} \times \frac{\sin\!\left(d_{\text{proper}} / R_{\text{universe}}\right)}{1 + z}$$

In the flat-space limit this reduces to the standard result. On a finite S³, the sine function introduces a turnaround: d\_A increases with distance, reaches a maximum at d\_proper = (pi/2) \* R\_universe, then decreases. Objects beyond the turnaround redshift z\_turn appear larger with increasing distance, not smaller.

**Corrected framing.** The JWST anomaly currently documented in the literature is that galaxies at z ~ 10-16 are **too massive, too compact, and too early** relative to ΛCDM predictions. This mass and timing anomaly is addressed by the matter accumulation mechanism of Paper A Appendix C -- the primary framework explanation for the current JWST data. The angular diameter distance turnaround prediction of this section is a distinct prediction of S³ topology that is **not** the current explanation for what JWST is detecting. Reliable angular size measurements at z>8 require rest-frame optical photometry, which is not achievable with current instrumentation. JWST morphologies at these redshifts are rest-frame UV only, tracing active star-forming regions rather than total stellar extent. Any inference about anomalously large physical sizes from rest-frame UV imaging at z>8 carries significant methodological uncertainty.

**The Little Red Dots open question.** A population of compact red sources at z ~ 4-8 (Little Red Dots, LRDs) has been identified in JWST deep field data. Whether these are compact stellar systems, heavily obscured AGN, or galaxy nuclei is currently unresolved. Their status as standard rulers for the S³ turnaround test is uncertain pending resolution of their physical nature. The standard ruler test should preferentially use massive quiescent ellipticals with well-characterised size-mass relations at z ~ 0.5-2 as the calibration sample, and should treat LRDs with caution until their physical nature is established.

## **4.2 Competing Interpretations**

The standard interpretation attributes anomalously large apparent sizes at high redshift (when detected) to: (a) physical size evolution -- early galaxies were intrinsically different from present-day galaxies; (b) selection bias -- JWST preferentially detects the most luminous objects; (c) systematic photometric redshift errors. The S³ topological interpretation attributes apparent size increase beyond z\_turn to geometry: those galaxies are beyond the angular diameter distance maximum and are being magnified by the curvature of the manifold.

These interpretations make different predictions. Physical size evolution and selection effects predict that anomalous apparent size should correlate with intrinsic galaxy properties consistent with hierarchical assembly models. Topological magnification predicts that anomalous apparent size should follow the S³ angular diameter distance formula as a smooth function of redshift alone, with no necessary correlation to intrinsic galaxy properties beyond standard evolution.

## **4.3 The Standard Ruler Method**

The test uses massive quiescent elliptical galaxies as standard rulers, calibrated against the well-measured galaxy size-stellar mass relation at z ~ 0.5-2 where the relation is well-established and JWST systematics are well-understood. The procedure:

Step 1. Compile a redshift-binned sample of massive quiescent ellipticals (log M\_star/M\_sun > 11) from z ~ 0.5 to z ~ 8 using the JWST CEERS, JADES, and PRIMER fields combined with HST CANDELS. Restrict to z <= 8 for the initial test to avoid rest-frame UV systematics; the z > 8 regime requires future instrumentation.

Step 2. For each galaxy, compute the apparent half-light radius theta\_e from surface brightness fitting in the reddest available band. Convert to angular diameter distance via d\_A = r\_phys / theta\_e, assuming a reference physical size r\_phys = r\_ref(M\_star) from the z ~ 1 calibration.

Step 3. Fit two models to the d\_A(z) relation: (i) the standard flat-universe angular diameter distance with standard cosmological parameters; (ii) the S³ angular diameter distance formula with R\_universe as the single free parameter.

Step 4. Compare fits. If the S³ model provides a significantly better fit with a physically consistent R\_universe (2-4 × R\_Hubble) and a turnaround feature in the range z\_turn ~ 2-8, the topology prediction is supported. If the flat model fits equally well with no turnaround signature, the S³ topology prediction is falsified at the accessible redshift range.

## **4.4 The Roman Space Telescope's Role**

The Nancy Grace Roman Space Telescope's value for this test is not primarily in resolving sizes of individual high-z galaxies -- its resolution is comparable to HST, and the rest-frame UV limitation at z>8 applies equally. Roman's defining advantage is its 200 times larger field of view than Hubble. This makes it the ideal instrument for the angular two-point correlation function measurement across the predicted turnaround redshift range z ~ 2-8.

On S³, the angular diameter distance turnaround imprints a characteristic scale on the galaxy clustering pattern: the comoving scale corresponding to a fixed angular separation shifts in a way that tracks the S³ d\_A(z) formula rather than the flat-universe formula. This clustering signature is measurable in wide-field photometric redshift surveys even without resolved size measurements of individual objects. Roman's wide-field survey data will provide the statistical power to detect or rule out this clustering signature across the turnaround redshift range, providing a complementary test that does not depend on rest-frame optical size measurements.

HWO-era resolved imaging in the 2040s will provide the rest-frame optical size measurements needed to complete the individual standard ruler test at z > 8.

## **4.5 Falsification Condition**

**FALSIFICATION CONDITION: A monotonically decreasing angular size with redshift at all observed redshifts (z ~ 0.5 to z ~ 8 with current data), with no statistically significant improvement of the S³ fit over the flat-universe fit and no turnaround feature in the Roman wide-field clustering statistics at z ~ 2-8, falsifies the S³ topology prediction at the redshift range accessible to current and near-future instruments.**

## **4.6 Expected Turnaround Redshift**

For R\_universe in the range 2-4 × R\_Hubble (consistent with the CMB quadrupole suppression constraint of Paper A Section 6.7), the predicted turnaround redshift z\_turn falls in the range z ~ 2-8. If the turnaround is in this range, it is detectable in current JWST data at z <= 8 and in Roman wide-field clustering statistics. A systematic analysis of the full size-redshift relation from z ~ 0.5 upward using existing data is the recommended first step.

# **5\. Post-Merger Lensing: The Geometric Stripping Timescale Test \[PROPOSED TEST\]**

*EPISTEMIC STATUS: PROPOSED TEST*

*PREREQUISITE: This test becomes quantitatively defined only after the Bi-209 calibration experiment (Paper A Section 5) pins m\_eff. Until m\_eff is measured, the diffusion timescale tau\_diff ~ R^2 \* m\_eff / hbar is a parametric prediction, not a specific number. The section below specifies the test framework and the discriminating signatures. Numerical predictions follow from the Bi-209 result.*

## **5.1 The Prediction**

Paper A Section 1.3 describes Geometric Stripping: during the Bullet Cluster collision, the hot intracluster gas undergoes thermal decoherence ($\eta_{\text{eff}} \to 0$) while the stellar components retain rotational coherence. Enhanced gravitational sourcing therefore follows the geometrically coherent galaxy distributions rather than the dominant baryonic gas mass.

The critical new prediction, following from Appendix P Theorem 4, is a timescale. The spinor condensate $C_{\mu\nu}$ is a propagating field (Term 2) governed by the Dirac equation, not a contact interaction. It diffuses beyond the stellar matter that generated it on a characteristic timescale:

$$\tau_{\text{diff}} \sim \frac{R^2\, m_{\text{eff}}}{\hbar}$$

where R is the relevant scale and m\_eff is the condensate mass parameter. This is a dimensional estimate from Theorem 4; the full propagator derivation is an identified calculational target (Calculational Target vii, Paper A Section 6.6).

## **5.2 Distinguishing Condensate from Dark Matter**

Standard collisionless dark matter predicts that the lensing excess co-moves with the stellar distributions immediately and indefinitely after the collision. The lensing offset from gas is a static feature -- it does not evolve on observable timescales.

The condensate prediction is different. The lensing excess should spread beyond the stellar distributions over time as the condensate diffuses. If m\_eff is constrained from the Bi-209 calibration, tau\_diff is a prediction, not a free parameter. If tau\_diff is measured from time-resolved lensing imaging, m\_eff is determined independently.

Three observable signatures distinguish the condensate picture from dark matter:

(i) Spatial extent growth. The lensing excess centroid should remain co-located with the stellar distributions, but the lensing convergence profile should broaden over time as the condensate diffuses. Dark matter predicts a stable profile shape.

(ii) Mass-dependence of diffusion rate. Heavier condensate (larger m\_eff) diffuses more slowly. Lighter condensate diffuses faster. The diffusion rate measured in multiple post-merger systems constrains m\_eff consistently across systems. Dark matter predicts no such mass-dependent diffusion.

(iii) Thermal history dependence. Systems in which the gas was more thoroughly thermalized (higher peak collision temperature, longer decoherence exposure) should show stronger lensing offsets and faster subsequent diffusion than systems with milder collisions. This is a direct test of the thermal decoherence mechanism.

## **5.3 Target Systems**

The Bullet Cluster (1E 0657-558) is the canonical system and the appropriate first calibration target. Additional post-merger systems with well-characterized collision histories and existing weak lensing data include: MACS J0025.4-1222 ('Baby Bullet'), Abell 520, and Abell 2744 ('Pandora's Box'). Abell 520 is particularly interesting because its lensing morphology is anomalous under the standard dark matter interpretation, with a central dark-matter concentration not associated with galaxies. The condensate diffusion picture provides a natural candidate explanation: the condensate has diffused toward the cluster center faster than the galaxies have moved.

## **5.4 Falsification Condition**

**FALSIFICATION CONDITION: No systematic broadening of the lensing convergence profile in post-merger systems over time, at sensitivity sufficient to detect diffusion on the predicted tau\_diff timescale given the m\_eff estimate from the Bi-209 calibration, falsifies the condensate diffusion prediction and is inconsistent with the Term 2 propagation mechanism of Theorem 4.**

# **6\. The Ampère Force Anomaly: A Terrestrial Laboratory Test \[PROPOSED TEST\]**

*EPISTEMIC STATUS: PROPOSED TEST*

This section proposes a laboratory test of Term 2 geometric coupling in macroscopic ballistic electron flow. The experimental anomaly (longitudinal tension in high-current systems) is documented in the literature. The SCH provides a specific physical mechanism and a proposed discriminating experiment. The SCH does not adopt Graneau's Ampère longitudinal force formulation; it provides an independent geometric mechanism that produces the same observable signature through a different physical pathway.

## **6.1 The Experimental Anomaly**

Two independent experimental programmes document anomalous longitudinal tension in high-current systems that standard Lorentz-Grassmann electrodynamics cannot account for.

Nasilowski (1964) documented high-pulsed-current copper wire fragmentation experiments in which solid copper wires fractured into dozens of distinct solid fragments before thermal melting occurred. The fracture surfaces showed clear evidence of tensile yield -- necking characteristic of longitudinal tension -- rather than the radial compression signature of the inward Lorentz pinch force. Standard electromagnetic theory predicts only inward (azimuthal) magnetic pressure from the self-induced field of the current. It predicts no outward longitudinal tension. Tensile fracture in solid copper before melting is kinematically incompatible with standard Lorentz forces alone.

Graneau (1982, 1983, 1987) conducted systematic experiments with high-current water arcs and solid conductors, documenting explosive forward momentum in collinear current elements that Lorentz-Grassmann electrodynamics could not account for. Graneau attributed these effects to Ampère's original longitudinal force law, which was superseded by the Lorentz formulation in the late 19th century. The theoretical attribution is disputed; the experimental anomaly is documented.

The SCH does not endorse Graneau's Ampère force theoretical framework. It provides a different physical mechanism -- the activation of Term 2 geometric coupling in ballistic pre-thermal electron flow -- that produces the same longitudinal tension signature through a gravitational rather than electromagnetic pathway.

## **6.2 The Term 2 Mechanism**

In a standard wire under DC current, conduction electrons have randomized thermal velocities with a small net drift superimposed. The electron four-velocity $u_\mu$ is not strongly aligned; the departure from the isotropic ground state is modest; $C_{\mu\nu}$ = $\rho\eta u_\mu u_\nu$ is small.

Under high pulsed current in the pre-thermal regime -- the brief window between current onset and Joule heating-driven thermalization -- the situation is qualitatively different. The electrons are driven into strongly ballistic flow: high collective velocity, high directional alignment, sharp departure from the isotropic ground state. The four-velocity $u_\mu$ of the electron current is highly coherent. $C_{\mu\nu}$ becomes a significant localized geometric source.

$C_{\mu\nu}$ = $\rho\eta u_\mu u_\nu$ creates an anomalous spatial stress along the axis of the current -- the same axis as the current flow. This geometric stress is longitudinal. It acts in addition to the standard electromagnetic forces. At sufficient current density and coherence, it produces a net outward tension along the wire axis: exactly the signature Nasilowski observed.

This mechanism requires no spin polarization of the conduction electrons. It operates through the collective velocity alignment ($u_\mu$ coherence) alone. The geometric coupling efficiency $\eta = \bar{\psi}\psi$ is nonzero for any matter, not only spin-polarized matter; the coherent four-velocity is the trigger for the departure from isotropy.

## **6.3 The Term 3 Mechanism (Secondary Candidate)**

A secondary mechanism may operate if the intense self-induced azimuthal magnetic field of the current induces partial spin polarization in the conduction electron gas, making the local axial current $A^\mu \neq 0$. By the Cartan equation, $T_{\lambda\mu\nu} = (\kappa\alpha/2)\,\varepsilon_{\lambda\mu\nu\rho}\,A^\rho$, the torsion contact term (Term 3) becomes active and acts as a repulsive pressure when matter with aligned chirality overlaps.

In normal metals at room temperature, spin polarization under magnetic fields is extremely small. The exchange interaction scale is far above the magnetic field strengths achievable in wire experiments. Term 3 is likely negligible in normal conductors at accessible current densities. However, in materials with unusually strong spin-orbit coupling or near ferromagnetic instability, the spin polarization per unit magnetic field is larger, and Term 3 may become detectable. This is flagged as a secondary candidate requiring a quantitative estimate of spin polarization magnitude in specific conductor materials before it can be evaluated. The primary mechanism is Term 2.

## **6.4 The Thermal Decoherence Governor**

The Ampère force anomaly is notoriously difficult to replicate consistently. Some experimental groups observe strong longitudinal tension; others see nothing anomalous under apparently similar conditions. The eta evolution equation provides a natural explanation for this experimental inconsistency.

Under DC current in a resistive conductor, Joule heating causes progressive thermal randomization of electron velocities. As the lattice temperature rises, Gamma\_decoh spikes. The geometric coupling efficiency $\eta$ is actively suppressed. The longitudinal tension from $C_{\mu\nu}$ decays as the system thermalizes. For slow-ramp or DC experiments, the system thermalizes before significant geometric coupling develops; the anomalous tension is too transient to observe.

For pulsed ballistic current experiments -- high current, fast rise time, short pulse duration -- the current peaks and the geometric coupling activates before significant Joule heating occurs. The anomalous tension is observed in the pre-thermal window. After the pulse ends and the system thermalizes, the effect decays.

This is exactly the experimental signature Nasilowski observed: fracture before melting, in the pre-thermal window of a fast pulsed discharge. It is also consistent with Graneau's finding that the longitudinal tension is strongest in the most impulsive, high-current discharges. The framework makes a specific prediction: the anomalous longitudinal tension is proportional to the product of current density and the ratio of pulse duration to thermal decoherence timescale tau\_coll/tau\_coh. Systems with tau\_coll >> tau\_coh (slow DC) show no effect; systems with tau\_coll << tau\_coh (fast pulsed) show maximum effect.

## **6.5 The Proposed Laboratory Test: Resistive vs. Superconducting Calorimetry**

The thermal decoherence governor suggests a clean discriminating experiment. In a superconductor, Cooper pairs are in a macroscopic quantum coherent state. Thermal randomization is suppressed by the superconducting gap: Gamma\_decoh approximately 0 below the critical temperature. The geometric coupling efficiency eta remains near its maximum for the coherent carrier state. The condensate is not decohered by Joule heating because there is no Joule heating.

The proposed experiment compares two configurations at matched geometry and current density:

Configuration A: Normal resistive conductor (e.g., copper wire). Standard physics prediction: energy deposited as Joule heat $Q_{\text{Joule}} = I^2 R t$. Framework prediction: additional calorimetric signal from geometric coupling energy thermalized as eta decoheres under Joule heating. The geometric coupling energy is partially converted to heat through the decoherence channel.

Configuration B: Superconducting loop (e.g., NbTi or YBCO below T\_c). Standard physics prediction: zero resistive heat deposited ($Q_{\text{Joule}} = 0$). Framework prediction: no geometric decoherence energy thermalized (because eta remains near maximum -- the coupling is maintained, not decohered). The geometric coupling is stored in the condensate rather than dissipated as heat.

The standard physics prediction for the calorimetric differential between Configuration A and Configuration B, after subtracting known Joule heating from A, is exactly zero. The framework prediction is a nonzero residual in Configuration A from geometric decoherence energy. The magnitude of this residual is proportional to $\alpha\,\eta\,\rho\,I^2 / m_{\text{eff}}^2$, which requires the Bi-209 calibration to evaluate quantitatively.

The methodology adapts the Channel B calorimetric design from the Bi-209 experiment (Paper A Section 5.3): high-precision calorimetric monitoring with sensitivity to anomalous energy balance. The Bi-209 experiment measures a single nuclear transition event; this experiment measures a sustained macroscopic geometric coupling differential. Same measurement technique, different physical regime, independent signal.

A secondary measurement channel: if the Term 2 longitudinal stress is active in Configuration A during the pre-thermal window, the wire should show anomalous axial strain measurable by strain gauge or interferometry with coincidence triggering on the current pulse. Configuration B should show no such axial strain because eta is maintained and there is no decoherence-driven stress release.

## **6.6 Falsification Conditions**

**FALSIFICATION CONDITION -- Primary: No calorimetric differential between Configuration A (resistive) and Configuration B (superconducting) at matched current density, geometry, and pulse duration, after Joule heating subtraction, at sensitivity sufficient to detect the framework's predicted geometric decoherence energy, falsifies the macroscopic Term 2 geometric coupling prediction.**

**FALSIFICATION CONDITION -- Secondary: No anomalous axial strain in Configuration A above Configuration B under matched pulsed current at pre-thermal timescales falsifies the longitudinal stress mechanism.**

If both falsification conditions are met, the Ampère force anomaly of Nasilowski and Graneau must be attributed entirely to standard electromagnetic effects or experimental artifact, and the SCH framework makes no contribution to their explanation.

# **7\. Exploratory Observational Directions \[EXPLORATORY\]**

## **7.1 The NANOGrav Background \[EXPLORATORY\]**

*EPISTEMIC STATUS: EXPLORATORY*

This section presents a candidate interpretation of the NANOGrav 2023 gravitational wave background detection. It is exploratory only. The standard interpretation (supermassive black hole binary mergers) is well-motivated and consistent with existing data. The condensate hum interpretation is a candidate alternative that makes different predictions about spectral structure. It requires the m\_eff calibration from Bi-209 before any quantitative prediction is possible.

### **7.1.1 The NANOGrav Detection**

The NANOGrav collaboration (2023) reported a stochastic gravitational wave background in the 1-100 nHz frequency range detected in the 15-year pulsar timing array dataset. The signal is consistent with a power-law spectrum expected from an ensemble of inspiraling supermassive black hole binaries. The standard interpretation attributes the background to the incoherent superposition of gravitational waves from all such binaries within the observable universe.

### **7.1.2 The Condensate Hum Interpretation**

Paper A Section 2.10 and Appendix P Section P.7.5 derive a condensate propagation frequency for black holes: $f_{\text{cond}} \sim \hbar c^4 / (4G^2 m_{\text{eff}} M^2)$, which scales as $M^{-2}$. For intermediate-mass black holes of approximately 10^3-10^5 M\_sun, f\_cond falls in the 1-100 nHz range (using the preliminary m\_eff estimate from the Pb-208 coherence timescale). The condensate propagation is a Term 2 effect: a diffusing spinor condensate field, not a propagating metric perturbation in the standard gravitational wave sense.

The two interpretations predict different spectral signatures:

Merger interpretation: Stochastic background from transient events. Power-law spectrum. Sources are incoherent. As pulsar timing array sensitivity improves, individual sources should eventually be resolvable as transients.

Condensate hum interpretation: Quasi-continuous background from persistent individual sources. Each black hole of a given mass hums at a specific frequency set by $f_{\text{cond}} \sim M^{-2}$. The quality factor Q is effectively infinite (Appendix P Section P.7.5.3), so each source is coherent over arbitrarily long timescales. The sum over all black holes in the observable volume produces a quasi-continuous background with a spectral shape reflecting the black hole mass function rather than the binary merger rate.

### **7.1.3 Discriminating Signature**

The critical discriminating observable is coherence time. Merger sources are transient: the gravitational wave signal from a specific binary rises and decays over a merger timescale, then is gone. Condensate hum sources are persistent: the same black hole emits at the same frequency indefinitely.

An analysis of the NANOGrav residuals searching for evidence of persistent coherent sub-threshold sources -- signals that are stable in frequency over the full 15-year dataset -- rather than incoherent stochastic power, would distinguish the two interpretations in principle. The merger interpretation predicts no such persistent coherent sub-threshold sources in the nHz band. The condensate hum interpretation predicts them.

Specifically, a pulsar timing astronomer looking for the condensate hum signature would search for the following in the NANOGrav 15-year dataset:

First, frequency stability over the full baseline. A condensate hum source at frequency f\_cond for a black hole of known mass should appear at the same frequency in the first 5 years, the middle 5 years, and the final 5 years of the dataset. Merger sources are transient and would not show this multi-epoch stability.

Second, source-count statistics inconsistent with merger rates. The condensate hum interpretation predicts a source count scaling with the black hole mass function integrated over the observable volume, not with the binary merger rate. For intermediate-mass black holes in the nHz band, the source count per frequency bin would be significantly higher under the condensate hum interpretation, because every black hole in that mass range contributes, not only those in inspiraling binaries.

Third, an absence of the expected chirp signature. Merging binaries produce signals that sweep in frequency (chirp) over time. Condensate hum sources at fixed mass produce signals at fixed frequency. A sub-threshold source search finding candidates with no detectable frequency drift over the 15-year baseline, at the predicted f\_cond for known black hole masses in nearby galaxies, would be a strong positive signal.

This analysis has not been performed. It is identified as an observational target. A null result would not falsify the condensate hum interpretation if the condensate propagation is not a metric perturbation detectable by pulsar timing. The detection channel for condensate propagation versus gravitational waves is an open theoretical question requiring the full propagator derivation of Calculational Target vii.

### **7.1.4 What Is Required Before This Is More Than Exploratory**

Two things must be established before the NANOGrav condensate hum interpretation can be evaluated quantitatively. First, the m\_eff calibration from the Bi-209 experiment to pin the $f_{\text{cond}} \sim M^{-2}$ scaling and confirm which black hole mass range corresponds to the NANOGrav nHz band. Second, the propagator derivation of Calculational Target vii to establish whether the condensate propagation couples to pulsar timing at detectable levels. Until both are available, the condensate hum interpretation of NANOGrav is an identified observational direction, not a prediction.

## **7.2 The Antipodal CMB Correlation Search \[EXPLORATORY\]**

*EXPLORATORY -- New in Draft 1.3. Identical epistemic status structure to Section 7.1.*

This section proposes a search for the antipodal correlation signature of S³ spatial topology in the existing Planck CMB temperature data. The search has not been performed. It requires no new observations. The signal-to-noise concern is stated honestly. This is designated exploratory because the condensate damping rate is not yet known, and the signal may be below Planck's noise floor.

### **7.2.1 The S³ Antipodal Prediction**

On S³ every point has a unique antipodal point diametrically opposite on the three-sphere. Every geodesic passes through the antipode before returning to the origin. This geometric property of the three-sphere has a direct statistical consequence for the CMB temperature field: the temperature at any sky position and the temperature at its antipodal position are not independent random variables. They share a geometric relationship determined by the global mode structure of fields defined on S³.

Specifically, the CMB temperature field on S³ should show a statistically significant positive correlation between antipodal sky pixel pairs T(n) × T(-n), where n is a unit vector on the sky and -n is its antipode, above the ΛCDM baseline prediction for a flat universe. This is distinct from the general large-angle correlation suppression already observed and confirmed by Planck. The suppression is broad -- it spans a range of large angular separations. The antipodal signal is a specific narrow excess at exactly theta = 180° angular separation. The two predictions are independent and complementary.

### **7.2.2 The Proposed Analysis**

The test is computationally straightforward. The analysis procedure:

Step 1. Take the Planck Commander or NILC foreground-cleaned temperature map at HEALPix resolution Nside = 64 or higher.

Step 2. For every pixel i, identify its antipodal pixel j (the pixel whose center is closest to the antipodal direction -n\_i).

Step 3. Compute the antipodal correlation statistic: C\_antipodal = (1/N\_pix) \* sum\_i T(n\_i) \* T(-n\_i), averaged over all pixel pairs.

Step 4. Compare C\_antipodal against the distribution expected from ΛCDM flat-universe simulations. If C\_antipodal exceeds the 95th percentile of the ΛCDM distribution, the antipodal signal is tentatively detected. If it falls within the distribution, S³ topology is not supported at current sensitivity.

This analysis uses existing public data. It is executable with standard CMB analysis tools. It has not been performed as a dedicated test of S³ topology, to our knowledge.

### **7.2.3 The Signal**

**Position of the feature.** The antipodal excess sits at exactly theta = 180° angular separation. The position of this feature is independent of R\_universe -- it is a property of S³ geometry regardless of the sphere's radius. Only the amplitude and angular width of the excess depend on R\_universe and the condensate damping rate.

**Amplitude and width.** The amplitude of the antipodal correlation excess scales with the lowest-order S³ mode contribution to the temperature power spectrum. For R\_universe ~ 2-4 × R\_Hubble, the lowest modes have wavelengths comparable to the horizon scale, and their contribution to the temperature variance is suppressed -- which is why the quadrupole and octopole are anomalously low. However, these same modes produce a positive antipodal correlation even when their variance is small, because the suppression affects all multipoles but the antipodal correlation is specifically sensitive to the parity structure of the lowest modes. The angular width of the excess is approximately Delta\_theta ~ R\_Hubble / R\_universe, which for R\_universe ~ 3 × R\_Hubble gives a width of order a few degrees.

**Condensate damping.** Photons reaching us from the last scattering surface at z ~ 1100 have traversed one near-circumnavigation of S³ only if R\_universe is small enough. For R\_universe ~ 3 × R\_Hubble, the comoving distance to the last scattering surface is approximately 0.3 × R\_universe -- well short of the antipodal distance pi/2 × R\_universe ~ 4.7 × R\_Hubble. This means CMB photons have not reached the antipodal point; the antipodal correlation signal comes from the global mode structure of primordial perturbations, not from photons that have literally circumnavigated the sphere. The condensate damping discussed in Paper A Section 6.9 reduces the amplitude of the signal but does not eliminate it if the coherence damping length L\_coh exceeds the last-scattering-surface comoving distance. Whether this condition is satisfied depends on sigma(omega) at CMB photon frequencies -- a quantity determined by CT-xiii.

### **7.2.4 Relationship to Known CMB Anomalies**

The Planck team has documented three related CMB anomalies that are consistent with S³ topology but have not been given a topological explanation within ΛCDM: the low quadrupole power, the quadrupole-octopole alignment, and the large-angle correlation deficit (C(theta) approximately 0 for theta > 60°). The antipodal correlation search proposed here is a fourth, independent test. A positive result on this search, combined with the existing anomalies, would constitute multi-signal evidence for S³ topology that would be difficult to attribute to foreground systematics or statistical fluctuation.

### **7.2.5 Sky-Variation of the Antipodal Correlation**

The condensate damping is not uniform across the sky -- it depends on the integrated matter density along each line of sight, which varies with the large-scale structure distribution. This means the antipodal correlation map would vary across the sky in a characteristic pattern that traces the large-scale condensate field distribution, independently of any existing galaxy or CMB survey. A positive antipodal correlation signal that varies across the sky in a way correlated with the integrated matter density along antipodal lines of sight would provide a second-order test of the condensate mechanism distinct from the topology test itself.

### **7.2.6 Signal-to-Noise Assessment and Exploratory Status**

The signal-to-noise concern is stated honestly. One near-circumnavigation of S³ may have subjected CMB photons to condensate damping sufficient to reduce the antipodal correlation signal below Planck's noise floor. This is the primary reason the section carries EXPLORATORY rather than PROPOSED TEST status. The test is designated exploratory rather than proposed because:

(i) The amplitude of the antipodal signal cannot be predicted quantitatively until CT-xiii determines sigma(omega) at CMB photon frequencies.

(ii) A null result in the Planck data would not definitively falsify S³ topology -- it could equally reflect condensate damping, the finite noise floor of Planck, or a value of R\_universe at the upper end of the 2-4 × R\_Hubble range where the lowest modes are strongly suppressed.

The test is identified as an observational direction. If CT-xiii yields a small sigma(omega) at CMB frequencies, the signal prediction becomes quantitative and the test may be upgradeable to PROPOSED TEST status. Execution of the analysis on existing Planck data in parallel with the CT-xiii calculation is encouraged, since a positive detection would provide strong motivation for completing the theoretical calculation.

## **7.3 Large Cosmic Void Structure as Condensate Phase Boundaries \[EXPLORATORY\]**

*EPISTEMIC STATUS: EXPLORATORY. The condensate void dynamics described in this section follow from the framework’s coupling structure but require formal development of the spatial gradient terms of $S_{\text{geo}}$ before quantitative predictions are possible. This section identifies the qualitative mechanism, states the observational signatures it predicts, and flags the calculational work required. The Bootes void is discussed as the motivating example.*

### **7.3.1 Voids in LCDM versus Voids in SCH**

In the LCDM picture, cosmic voids are underdense regions where matter did not accumulate. They grow through gravitational evacuation: matter flows away from underdense regions under the gravitational pull of surrounding overdense structures. The void interior is passively empty — spacetime with no special properties beyond its low matter density. The condensate picture is different.

The geometric condensate couples to the rotational organisational state of matter through the condensate vacuum expectation value $\eta = \langle\bar{\psi}\psi\rangle$. In regions of high matter density and rotational coherence — filaments, walls, galaxy clusters — eta is nonzero and the condensate is active. Inside a cosmic void, where matter density is near zero, eta is suppressed toward zero: there is almost no matter present to source the geometric state. This is not a thermal decoherence effect (T > T\_c); it is a sourcing effect. The condensate is suppressed inside voids because the source of the condensate — coherently rotating matter — is absent.

The boundary between a void and the surrounding large-scale structure is therefore a boundary between two condensate regimes: eta approximately 0 inside the void, eta nonzero in the surrounding filaments and walls. This is a condensate phase boundary. Phase boundaries in field theories carry surface energy — a domain wall tension proportional to the gradient of the field across the boundary. The condensate domain wall at the void boundary carries energy proportional to the spatial gradient of eta across the wall, encoded in the gradient terms of $S_{\text{geo}}$.

The domain wall dynamics have a direction: the eta approximately 0 phase (void interior) is the lower-energy state in the absence of matter sources. The domain wall therefore moves outward — the void expands — driven not only by gravitational evacuation but also by the condensate energy gradient. This provides an additional driving mechanism for void growth beyond what standard gravitational dynamics alone predicts.

### **7.3.2 Predicted Observational Signatures**

The condensate void mechanism predicts three observational signatures relative to LCDM void statistics, all following from the domain wall dynamics described above.

**Signature 1 — Voids grow larger than LCDM predicts:** The condensate domain wall provides an additional outward driving force beyond gravitational evacuation. Large voids should be more common and more extreme in their underdensity than LCDM simulations predict at matched initial conditions. The Bootes void, at 330 million light-years diameter, sits at the uncomfortable upper end of what LCDM void coalescence models can accommodate in the available cosmic time. The condensate mechanism relaxes this tension by providing an additional growth driver.

**Signature 2 — Voids are more spherical than LCDM predicts:** The condensate domain wall tension acts isotropically on the void boundary — the gradient energy is the same in all directions for a given boundary curvature. This isotropic driving force tends to make voids rounder. LCDM voids are shaped primarily by the anisotropic gravitational tidal field of the surrounding structure, which tends to produce triaxial or filamentary shapes. The condensate adds a sphericising pressure. The Bootes void is notably spherical; this is consistent with the predicted mechanism.

**Signature 3 — Void walls are sharper than LCDM predicts:** The condensate domain wall is a field-theoretic boundary with a characteristic width set by the condensate coherence length $\lambda_{\text{coh}} \approx \hbar/(m_{\text{eff}}\,c)$. At the galactic estimate of m\_eff, lambda\_coh is astronomically large, which means the wall width is set by the condensate coherence rather than by the gravitational infall dynamics. Whether this produces a sharper or broader wall than LCDM depends on the value of m\_eff at void scales, which requires the Bi-209 calibration. The qualitative prediction is that the density gradient at the void-wall boundary should show a field-theoretic profile rather than a purely gravitational infall profile. Euclid and DESI are now mapping void boundaries with sufficient precision to test wall sharpness profiles systematically.

### **7.3.3 The Void Coalescence Mechanism**

The hypothesis that the Bootes void formed through coalescence of smaller voids is the standard explanation for its extreme size. In the SCH framework this coalescence has a specific physical mechanism beyond gravitational dynamics. When two adjacent void regions — both in the eta approximately 0 phase — are separated by a thin filament of eta nonzero matter, the condensate domain wall dynamics drive the merger. The thin filament is a narrow strip of the high-energy phase sandwiched between two low-energy phase regions. The domain wall tension pulls the boundaries inward toward each other, the filament thins, and eventually the two eta approximately 0 regions merge. This is physically analogous to the coalescence of soap bubbles, which the observational community already uses as a metaphor for void mergers. In SCH the metaphor has a literal mechanism: the condensate surface tension drives the merger on a timescale set by the domain wall speed, which depends on the condensate coupling alpha and the filament density. That timescale is a prediction, not a free parameter, once alpha is fixed by the Bi-209 calibration.

### **7.3.4 What Is Required for Quantitative Predictions**

The qualitative mechanism is motivated directly by the framework's coupling structure. Quantitative predictions require two things that are not yet available. First, the spatial gradient terms of $S_{\text{geo}}$ — the terms involving $\nabla\eta$ — must be derived formally. These terms govern the domain wall thickness, the wall tension, and the void expansion rate due to condensate dynamics. They are implicit in the full Einstein-Cartan-Dirac action but have not been isolated and developed in the current papers. Second, the Bi-209 calibration is required to fix alpha, which sets the overall scale of the condensate void dynamics relative to gravitational dynamics.

This section is therefore exploratory in the strict sense: the mechanism follows from the framework, the observational signatures are identified and in principle testable with Euclid and DESI data, but the formal development is outstanding. A dedicated working note developing the condensate void dynamics from the gradient terms of $S_{\text{geo}}$ is the appropriate next step. That working note would produce calculational targets for inclusion in a revised Appendix P, and its predictions would be testable against the Euclid void catalogue and the DESI void boundary sharpness measurements currently being accumulated.

*The Bootes void is the largest and most spherical known cosmic void. SCH predicts that large voids should be more common, more spherical, and have sharper walls than LCDM predicts, through condensate domain wall dynamics at the void boundary. The coalescence of smaller voids into the Bootes void has a literal mechanism in the condensate surface tension. These are qualitative predictions only; quantitative development requires the spatial gradient terms of $S_{\text{geo}}$ and the Bi-209 alpha calibration. Euclid and DESI are generating the void boundary precision data against which these predictions will eventually be tested.*

# **8\. Discussion**

## **8.1 What the MaNGA Staircase Establishes**

The beta\_z partial correlation signal is a genuine kinematic signature in the data. It is statistically significant across the full sample (rho = +0.128, p = 6.98e-15, N = 3,643), survives a fully JAM-independent control set including photometric mass, effective radius, Sersic index, and light-weighted age, and is robust to the additional inclusion of observed velocity dispersion in the control set. The signal holds in fast rotators across all mass tertiles. In slow rotators, where beta\_z and sigma\_e are kinematically degenerate in pressure-dominated systems, the signal does not survive sigma\_e inclusion, consistent with the contrast class prediction. What the signal does not establish: it does not confirm the framework. The direction -- more anisotropically organised systems showing more gravitational excess at fixed photometric mass -- is consistent with the SCH prediction and is not produced by any LCDM mechanism tested. The primary outstanding requirement is the DES Y6 weak lensing cross-match, which would provide an independent test free of all kinematic and photometric modelling assumptions. Until that cross-match is performed, the beta\_z result is a necessary but not sufficient condition for the SCH galactic-scale prediction.

## **8.2 The Relationship Between Sections**

The five primary observational directions of this paper are not independent. They share the same underlying parameter architecture. The coupling constant alpha and the condensate mass m\_eff appear in all of them. The Bi-209 calibration (Paper A Section 5) is the load-bearing experiment that converts all quantitative predictions from conditional statements to specific numbers. Until it is performed, the predictions of Sections 4, 5, 6, and 7 are parametric: they specify what would be observed for given values of alpha and m\_eff, not the specific numbers to look for.

The recommended priority ordering for the experimental programme is: (1) MaNGA-DES weak lensing cross-match (Paper A Test 4.1) -- uses existing public data, directly tests the primary galactic-scale prediction; (2) SLACS metallicity-lensing test (Paper A Test 4.2) -- uses existing public data, tests the nuclear-scale prediction; (3) JWST standard ruler topology test (Section 4) -- uses existing public data for z <= 8, single free parameter, clean falsification condition; (4) Bi-209 laboratory calibration (Paper A Section 5) -- pins alpha and m\_eff, unlocks quantitative predictions for Sections 5, 6, and 7; (5) Resistive/superconducting calorimetric comparison (Section 6) -- after Bi-209 provides the expected signal magnitude.

*The two exploratory directions of Section 7.1 and 7.2 -- the NANOGrav condensate hum and the antipodal CMB correlation search -- are not on the critical path but are executable in parallel with the main programme. The antipodal search in particular requires only existing Planck data and standard CMB analysis tools; it is the lowest-cost observational direction in the entire programme. Section 7.3 below adds a third exploratory direction: large cosmic void structure as a condensate phase boundary phenomenon.*

## **8.3 The Contrast Class Discipline**

Every section of this paper has maintained the contrast class discipline established in Paper A Section 1.5. The framework predicts anomalous effects in systems with high geometric coherence and predicts their absence in systems with randomized orbital configurations. This discipline is not optional -- it is the primary guard against the framework becoming unfalsifiable by absorbing every anomaly as evidence. If globular clusters, dwarf irregulars, and pressure-supported systems begin showing the predicted signatures, the framework is wrong. The contrast class is as important as the signal class.

# **9\. Conclusion**

This paper has presented one replication result computed from public data (the MaNGA DR17 beta\_z partial correlation, Section 2), one cross-scale consistency check (the Earth flyby anomaly sign-lock and K-cluster, Section 3), three proposed observational and laboratory tests (the JWST standard ruler topology test, the post-merger lensing timescale test, and the resistive/superconducting calorimetric comparison, Sections 4-6), and two exploratory observational directions (the NANOGrav condensate hum interpretation and the antipodal CMB correlation search, Section 7). Draft 1.4 replaces Section 2 in full. The original lambda\_R quintile staircase is superseded by an independent replication using the JAM velocity anisotropy parameter beta\_z and the Firefly photometric mass estimator. The replacement resolves the Jeans estimator bias and the lambda\_R proxy definition problem identified in external review. The beta\_z signal (rho = +0.128, p = 6.98e-15) survives a fully JAM-independent joint control set and is robust to observed velocity dispersion inclusion. An inclination artifact in the JAM-based RAR residual was identified and fully traced to sigma\_e projection in slow rotators; it does not contaminate the Firefly result. The DES Y6 weak lensing cross-match remains the critical outstanding test and is the primary recommendation for follow-up.

These results and proposals do not confirm the Geometric State Framework. They constitute observational signatures that the framework predicts and that standard models do not currently explain, proposed tests with explicit falsification conditions, and consistency checks across scales. The staircase direction is inconsistent with ΛCDM assembly history predictions and is not driven by the mass estimator. The flyby sign-lock tracks equatorial trajectory geometry rather than spacecraft-specific properties — a pattern the thermal recoil model does not naturally predict, though that model has not been definitively ruled out. The JWST mass and timing anomaly has a candidate explanation in the bounce cosmology. The Ampère force anomaly has a candidate mechanism with a discriminating proposed experiment. The antipodal CMB correlation test is the lowest-cost observational direction in the programme and can be executed immediately with existing data. The Bootes void structure is an exploratory direction whose formal development requires the spatial gradient terms of $S_{\text{geo}}$.

All outcomes of further testing are scientifically valuable. The beta\_z signal reported in Section 2 is the prediction on record before the DES Y6 Metadetection weak lensing shape catalogue is released. The lensing staircase is independent of every modelling choice made in Section 2 -- it does not depend on JAM, Firefly, kinematic estimators, or structural control variables. If the beta\_z signal reflects a genuine dynamical degree of freedom that independently sources gravity, it must appear in the lensing data. A null result in the lensing cross-match at sufficient sensitivity would constrain the geometric coupling to below detectable levels and constitute the strongest available falsification of the galactic-scale SCH prediction. Detection of the JWST angular diameter turnaround at the predicted redshift range in Roman clustering statistics would be strong evidence for $S^3$ topology. A positive antipodal correlation in the Planck data would be multi-signal evidence for $S^3$ topology. Null results on the calorimetric comparison at sufficient sensitivity would constrain macroscopic geometric coupling at laboratory scales. All directions sharpen the framework's empirical profile, but the DES Y6 lensing cross-match is the decisive next test.

# **References**

Anderson, J.D. et al. (2008). Anomalous orbital-energy changes observed during spacecraft flybys of Earth. Physical Review Letters, 100, 091102.

Bundy, K. et al. (2015). Overview of the MaNGA Survey. Astrophysical Journal, 798, 7.

Cappellari, M. (2008). Measuring the inclination and mass-to-light ratio of axisymmetric galaxies via anisotropic Jeans models. MNRAS, 390, 71.

Cappellari, M. et al. (2012). Systematic variation of the stellar initial mass function in early-type galaxies. Nature, 484, 485.

Cappellari, M. (2016). Structure and Kinematics of Early-Type Galaxies from Integral Field Spectroscopy. Annual Review of Astronomy and Astrophysics, 54, 597.

Drory, N. et al. (2015). The MaNGA Integral Field Unit Fiber Feed System. Astronomical Journal, 149, 77.

Emsellem, E. et al. (2011). The ATLAS$^{3D}$ project — III. A census of the stellar angular momentum within the effective radius for 260 early-type galaxies. MNRAS, 414, 888.

Goddard, D. et al. (2017). SDSS-IV MaNGA: global stellar population gradients in early-type galaxies. MNRAS, 465, 688.

Graneau, P. (1982). Ampere-Neumann electrodynamics of metallic conductors. European Journal of Physics, 3, 235.

Graneau, P. (1983). First indication of Ampere tension in solid electric conductors. Physics Letters A, 97, 253.

Graneau, P. (1987). The Ampere-Neumann electrodynamics of metallic conductors. Fortschritte der Physik, 35, 787.

Labbe, I. et al. (2023). A population of red candidate massive galaxies ~600 Myr after the Big Bang. Nature, 616, 266.

Lu, S., Zhu, K., Cappellari, M., Li, R., Mao, S., Xu, D. (2024). MNRAS, 530, 4474.

Maraston, C. et al. (2020). Stellar population models based on the MaStar library of stellar spectra. MNRAS, 496, 2962.

McGaugh, S.S., Lelli, F. & Schombert, J.M. (2016). Radial Acceleration Relation in Rotationally Supported Galaxies. Physical Review Letters, 117, 201101.

Milgrom, M. (1983). A modification of the Newtonian dynamics. Astrophysical Journal, 270, 365.

NANOGrav Collaboration (2023). The NANOGrav 15-year data set: Evidence for a gravitational-wave background. Astrophysical Journal Letters, 951, L8.

Nasilowski, J. (1964). Undulatory corrugation of a thin copper wire exploded in air. In: Exploding Wires, Vol. 3, W. G. Chace and H. K. Moore eds., Plenum Press, New York, pp. 295-313.

Neumann, J. et al. (2022). The MaNGA Firefly Stellar Population Catalogue. MNRAS, 516, 523, 4808, 5988.

Rodriguez-Gomez, V. et al. (2016). The merger rate of galaxies in the IllustrisTNG simulations. MNRAS, 458, 2371.

Rong, Y. et al. (2019). The Mass Discrepancy-Acceleration Relation in Kinematically Classified Galaxies. Astrophysical Journal Letters, 883, L17.

Verlinde, E. (2016). Emergent Gravity and the Dark Universe. SciPost Physics, 2, 016.

Yan, R. et al. (2016). SDSS-IV MaNGA IFS Library of Nearby Galaxies. Astronomical Journal, 152, 197.

Zhu, K., Lu, S., Cappellari, M., Li, R., Mao, S., Gao, L. (2023). MNRAS, 522, 6326.

**End of Paper B -- Draft 1.4**
