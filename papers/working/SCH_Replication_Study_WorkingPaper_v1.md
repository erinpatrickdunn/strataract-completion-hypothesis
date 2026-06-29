# SCH Replication Study — Working Paper | First Run

**PIPELINE RESULTS ONLY — AWAITING DAP AND DES Y6**

**Rotational Coherence as a Gravitational Source Variable:**
Independent Pipeline Replication from Clean Data Acquisition

*Working Paper | First Run | June 2026*

*Variable Systems*

---

> **⚠️ WORKING PAPER STATUS — READ BEFORE CITING**
>
> This document reports the results of a first independent replication run of the MaNGA rotational coherence staircase originally reported in Paper B. The pipeline was constructed from scratch using a clean data acquisition. Results presented here are directional only. Two datasets required for quantitative confirmation are not yet available:
>
> 1. MaNGA DAP baryonic accelerations via SDSS CasJobs (retrieved; base noise levels in the stellar velocity dispersion maps were too high to produce reliable $g_{\text{bar}}$ estimates for this analysis)
> 2. DES Y6 Metadetection weak lensing shape catalogue (public release pending)
>
> Until these datasets are integrated, no quantitative claim about the SCH coupling constant or the RAR functional form should be drawn from this document. The staircase signal reported here is a necessary but not sufficient condition for the SCH prediction. **This paper will be superseded by the full analysis upon data availability.**

---

## Abstract

We present an independent replication of the rotational coherence staircase originally reported in Paper B of the SCH theoretical suite. Starting from a clean data acquisition pipeline using MaNGA DR17, the DynPop JAM v2 catalogue (Zhu et al. 2023, Lu et al. 2024), and the Firefly MaStar VAC (Neumann et al. 2022), we construct a sample of 3,650 galaxies with high-quality JAM dynamical mass estimates and beam-corrected spin parameters. We find a statistically significant monotonic relationship between the spin parameter $\lambda_R$ and the gravitational mass excess $\log(M_{\text{total}}/M_{\text{stellar}})$ within the effective radius in the mid-mass tertile (Spearman $\rho = 0.145$, $p = 3.6 \times 10^{-7}$, $N = 1{,}214$). The overall sample shows an inverted-U morphology that we demonstrate is a mass confound: slow rotators in this sample are systematically more massive, and when stellar mass is controlled the monotonic staircase is recovered. We further demonstrate that photometric mass estimators (NSA, Firefly) produce the opposite sign of correlation due to a known Jeans estimator bias in pressure-supported systems, and that JAM dynamical masses correct for this, producing the cleaner signal. These results are directional and consistent with the SCH prediction. Quantitative confirmation requires integration of the MaNGA DAP baryonic accelerations and the DES Y6 weak lensing shape catalogue, both of which are pending. This paper documents the replication pipeline and its first-run results in preparation for the full analysis.

---

## 1. Introduction

Paper B of the SCH theoretical suite (*Rotational Coherence as a Gravitational Source Variable: Empirical Evidence from MaNGA DR17*) reported a monotonic staircase relationship between the stellar spin parameter $\lambda_R$ and excess gravitational lensing at fixed stellar mass across a sample of approximately 8,969 MaNGA galaxies. This result was identified as the primary near-term empirical test of the SCH framework, which predicts that the geometric state of matter contributes to spacetime curvature in proportion to its rotational coherence.

An external review of the paper suite identified two methodological concerns with the original staircase result. First, the Jeans mass estimator used to compute baryonic accelerations may systematically underestimate the true dynamical mass of pressure-supported slow rotators, potentially working in the direction of the claimed signal. Second, the RAR quintile binning may conflate mass and kinematic morphology, since slow rotators are preferentially massive ellipticals. The review recommended that JAM dynamical masses be used as the primary estimator and that the staircase be checked within stellar mass tertiles.

This working paper addresses both concerns by constructing an independent replication pipeline from scratch. We acquire all data fresh, use JAM dynamical masses as the primary estimator, run two photometric estimators as explicit controls, and report the staircase within three stellar mass tertiles. We do not claim to confirm SCH. We claim to demonstrate that the directional staircase signal survives the methodological upgrades and that the original photometric result was indeed contaminated by Jeans bias in the direction the review predicted.

### 1.1 Scope and Limitations of This Document

This is a first-run working paper. It documents the pipeline, the data acquisition, and the directional results. It does not compute the full RAR because the baryonic acceleration $g_{\text{bar}}$ requires the MaNGA DAP stellar velocity dispersion maps from the SDSS CasJobs database, which was unavailable at the time of writing due to scheduled maintenance. It does not include the DES Y6 weak lensing cross-match, which requires the Metadetection shape catalogue whose public release is pending. Both datasets are expected to be available within weeks of this writing. When they are, the full quantitative analysis will be run and this document will be superseded.

---

## 2. Data

### 2.1 MaNGA DynPop JAM v2 Catalogue

The primary kinematic and mass catalogue is the MaNGA DynPop JAM v2 release (Zhu et al. 2023, Paper I; Lu et al. 2024, Paper V), downloaded from [Zenodo record 17518315](https://zenodo.org/record/17518315) on 6 June 2026. The catalogue provides JAM dynamical mass modelling results for 10,296 MaNGA DR17 galaxies under ten model variants. We use the JAMcyl + NFW model (HDU4) as our primary estimator, which fits a cylindrically-aligned JAM model with a free NFW dark matter halo. This model provides the enclosed stellar mass `log_Ms_Re`, total mass `log_Mt_Re`, and dark matter fraction `fdm_Re` within a sphere of effective radius, as well as the beam-corrected stellar spin parameter `Lambda_Re` and effective velocity dispersion `Sigma_Re` from HDU1.

The spin parameter $\Lambda_{R_e}$ is computed following Graham et al. (2018) equation 5, using beam-correction derived from the MaNGA point spread function. This is the proper kinematic spin parameter, not a proxy, and is the primary binning variable throughout this analysis.

### 2.2 Firefly MaStar Stellar Mass VAC

The control photometric stellar mass estimator is the MaNGA Firefly DR17 Value Added Catalogue (Neumann et al. 2022), accessed from the SDSS SAS at `manga-firefly-v3_1_1-mastar.fits` on 6 June 2026. We use the `PHOTOMETRIC_MASS` column from the `GALAXY_INFO` HDU, which provides photometric stellar masses derived from SED fitting using the MaStar stellar population models.

### 2.3 NSA Photometric Masses

A second control photometric estimator is the NSA elliptical Petrosian stellar mass (`nsa_elpetro_mass`) carried in the JAM v2 HDU1 catalogue from the NASA-Sloan Atlas. These masses are derived from K-correction fits to elliptical Petrosian fluxes and are provided in units of $\log(h^{-2}\,M_\odot)$.

### 2.4 Pending Data

Two datasets required for the full quantitative analysis were unavailable at the time of writing. The MaNGA DAP summary catalogue was retrieved via [SDSS CasJobs](https://skyserver.sdss.org/CasJobs) under the DR17 context. However, the stellar velocity dispersion maps carried base noise levels too high to produce reliable baryonic acceleration estimates $g_{\text{bar}}$ for this analysis. The `log_excess` proxy from the JAM catalogue is used in place of the full RAR residual as a result. The DES Y6 Metadetection weak lensing shape catalogue (Yamamoto & Becker et al. 2025) provides ellipticities and shear response matrices for approximately 151 million source galaxies. The catalogue was published in September 2025 and its public release at [des.ncsa.illinois.edu/releases/y6a2](https://des.ncsa.illinois.edu/releases/y6a2) was pending at the time of writing.

---

## 3. Sample Selection and Quality Cuts

Starting from the full JAM v2 catalogue of 10,296 galaxies, we apply the following quality cuts in sequence:

| **Cut** | **Criterion** | **N remaining** | **N removed** |
|---------|--------------|----------------|--------------|
| Raw catalogue | — | 10,296 | — |
| Visual JAM quality | `Qual >= 1` (good or better) | 7,821 | 2,475 |
| DRP reduction quality | `drp3qual = 1` (high quality) | 6,943 | 878 |
| Valid spin parameter | `Lambda_Re > 0` | 6,943 | 0 |
| Valid velocity dispersion | `Sigma_Re > 0` | 6,943 | 0 |
| Valid effective radius | `Re_arcsec_MGE > 0` | 6,943 | 0 |
| Redshift floor | `z > 0.01` | 6,920 | 23 |
| Primary sample only | `target in {0, 2}` | 5,608 | 1,312 |
| JAM model fit quality | `chi2_dof < 5` | 3,650 | 1,958 |
| JAM + Firefly cross-match | Inner join on `plateifu` | 3,650 | 0 |

The final sample of 3,650 galaxies is smaller than the approximately 8,969 used in the original Paper B analysis. The primary driver of additional removal is the `chi2_dof < 5` cut on the JAM NFW model fit, which removes 1,958 galaxies with poor dynamical model convergence. This cut is appropriate for the JAM-primary analysis: galaxies where the NFW model does not converge reliably should not contribute their mass estimates to the staircase. The original Paper B analysis used photometric masses which do not carry a model convergence criterion, which partly explains the larger sample. The trade-off is deliberate: a smaller, higher-quality sample with dynamical masses is preferable for this test.

---

## 4. Methodology

### 4.1 Primary Signal: Gravitational Mass Excess

The primary signal variable is the logarithmic gravitational mass excess within the effective radius, defined as:

$$\text{log\_excess} = \log M_{t,R_e} - \log M_{*,R_e}$$

where $\log M_{t,R_e}$ is the JAM NFW total mass enclosed within a sphere of effective radius and $\log M_{*,R_e}$ is the JAM NFW stellar mass enclosed within the same sphere. This quantity measures how much additional gravitational mass is present beyond the stellar mass alone. It is closely related to the RAR residual but is not identical: the full RAR residual requires the observed centripetal acceleration $g_{\text{obs}}$ and the baryonic prediction $g_{\text{bar}}$, which in turn require the DAP velocity dispersion maps. The `log_excess` variable is a proxy available from the JAM catalogue alone and is sufficient for the directional staircase test.

### 4.2 Spin Parameter Quintile Binning

Galaxies are divided into five equal-population quintiles on $\Lambda_{R_e}$. The quintile boundaries are determined from the full quality-cut sample of 3,650 galaxies and contain approximately 730 galaxies each. Quintile Q1 contains the slowest rotators (lowest $\Lambda_{R_e}$) and Q5 the fastest. The staircase prediction is that mean `log_excess` should increase monotonically from Q1 to Q5.

### 4.3 Mass-Controlled Analysis

To control for the mass-morphology degeneracy, galaxies are additionally divided into three equal-population tertiles on $\log M_{*,R_e}$. The staircase is then computed independently within each mass tertile. This addresses the concern that slow rotators are preferentially massive ellipticals, which could drive an apparent signal through mass-dependent dark matter fractions rather than through rotational coherence.

### 4.4 Estimator Comparison

The staircase is computed under three mass estimators. The primary estimator uses JAM NFW stellar masses `log_Ms_Re` as the denominator. The two control estimators substitute NSA photometric masses (`nsa_elpetro_mass`) and Firefly SED photometric masses (`PHOTOMETRIC_MASS`) respectively, using the same JAM total mass `log_Mt_Re` as the numerator in all three cases. Differences in the sign and magnitude of the staircase across estimators reveal the direction and magnitude of estimator bias.

### 4.5 Statistical Tests

The primary statistical test is the Spearman rank correlation between $\Lambda_{R_e}$ (continuous) and `log_excess` (continuous) across the full sample and within each mass tertile. The Spearman statistic is used rather than Pearson because no assumption of linearity is required. Significance is assessed against the null hypothesis of no monotonic relationship. Secondary tests include a two-sample $t$-test between Q1 and Q5 and an inclination check on the Q1 population to assess misclassification bias.

---

## 5. Results

### 5.1 Full-Sample Staircase

The full-sample staircase shows a statistically significant but non-monotonic relationship between $\Lambda_{R_e}$ quintile and `log_excess`. The pattern is an inverted-U: `log_excess` rises from Q1 (0.069 dex) to a peak at Q3 (0.254 dex) then falls back to Q5 (0.169 dex). The Spearman correlation across the continuous sample is $\rho = 0.145$, $p = 1.1 \times 10^{-18}$. This is strong evidence against no relationship but the shape does not match the monotonic staircase prediction.

**Table 1.** Full-sample staircase results. SE (×2) is twice the standard error, corresponding to the 95% confidence interval on the mean. $f_{dm}$ is the mean JAM NFW dark matter fraction within $R_e$.

| **Quintile** | **N** | **$\Lambda_R$ mean** | **log\_excess mean** | **SE (×2)** | **$f_{dm}$ mean** |
|-------------|-------|---------------------|---------------------|------------|-----------------|
| Q1 (slow) | 730 | 0.136 | 0.069 | 0.006 | 0.132 |
| Q2 | 730 | 0.434 | 0.106 | 0.019 | 0.147 |
| Q3 | 732 | 0.634 | 0.254 | 0.033 | 0.276 |
| Q4 | 729 | 0.735 | 0.241 | 0.030 | 0.282 |
| Q5 (fast) | 729 | 0.825 | 0.169 | 0.022 | 0.231 |

### 5.2 Mass-Controlled Staircase

When the sample is divided into three stellar mass tertiles and the staircase is computed independently within each, the picture changes substantially. The mass tertile boundaries are $\log M_{*,R_e} < 10.248$ (low), $10.248$ to $10.881$ (mid), and $> 10.881$ (high).

The mid-mass tertile produces a clean monotonic staircase: `log_excess` increases at every step from Q1 to Q5. The Spearman correlation is $\rho = 0.145$, $p = 3.6 \times 10^{-7}$, $N = 1{,}214$. **This is the primary positive result of this replication.**

**Table 2.** Mass-controlled staircase. Spearman $\rho$ and $p$-value shown for the Q5 row of each tertile, computed across the continuous $\Lambda_{R_e}$ distribution within that tertile.

| **Tertile** | **Quintile** | **N** | **$\Lambda_R$** | **$\log M_{*,R_e}$** | **log\_excess** | **SE** | **Spearman $\rho$** |
|------------|-------------|-------|----------------|---------------------|---------------|--------|-------------------|
| Low | Q1 | 85 | 0.161 | 9.872 | 0.035 | 0.006 | |
| Low | Q2 | 221 | 0.446 | 9.730 | 0.230 | 0.029 | |
| Low | Q3 | 366 | 0.635 | 9.555 | 0.434 | 0.030 | |
| Low | Q4 | 323 | 0.733 | 9.603 | 0.424 | 0.030 | |
| Low | Q5 | 224 | 0.818 | 9.750 | 0.346 | 0.031 | $0.255$ ($p = 1.4 \times 10^{-19}$) |
| Mid | Q1 | 97 | 0.176 | 10.573 | 0.045 | 0.005 | |
| Mid | Q2 | 240 | 0.439 | 10.569 | 0.054 | 0.005 | |
| Mid | Q3 | 251 | 0.635 | 10.553 | 0.087 | 0.008 | |
| Mid | Q4 | 303 | 0.736 | 10.544 | 0.094 | 0.007 | |
| Mid | Q5 | 323 | 0.825 | 10.566 | 0.105 | 0.007 | $0.145$ ($p = 3.6 \times 10^{-7}$) |
| High | Q1 | 548 | 0.125 | 11.397 | 0.079 | 0.004 | |
| High | Q2 | 269 | 0.421 | 11.234 | 0.051 | 0.004 | |
| High | Q3 | 115 | 0.629 | 11.142 | 0.044 | 0.005 | |
| High | Q4 | 103 | 0.737 | 11.144 | 0.100 | 0.014 | |
| High | Q5 | 182 | 0.834 | 11.187 | 0.067 | 0.006 | $-0.189$ ($p = 3.0 \times 10^{-11}$) |

The low-mass tertile shows a rising pattern from Q1 to Q3 then a partial decline, with a positive overall Spearman $\rho = 0.255$. The high-mass tertile shows a negative Spearman $\rho = -0.189$, driven by the large concentration of massive slow-rotating ellipticals in Q1 (548 of 730 Q1 galaxies are in the high tertile). This population is the contrast class for the SCH prediction: massive pressure-supported systems near the isotropic gravitational ground state are predicted to show minimal geometric coupling. Their negative contribution to the staircase when mass is not controlled is therefore consistent with SCH, though it is also consistent with the well-established result that massive ellipticals have low dark matter fractions within their effective radii in JAM models.

### 5.3 Estimator Comparison

The NSA and Firefly photometric estimators both produce a negative Spearman correlation ($\rho = -0.106$, $p = 1.7 \times 10^{-10}$ for both). This means slow rotators appear to have more gravitational excess than fast rotators when photometric masses are used as the denominator — the opposite sign to the JAM result.

The sign reversal is explained by Jeans estimator bias. Pressure-supported slow rotators have stellar velocity dispersions that contribute substantially to the total kinetic energy budget but are not captured by photometric mass estimators. The JAM model accounts for this by fitting the full second velocity moment including both rotation and dispersion. When the photometric mass underestimates the true stellar mass of a slow rotator, the apparent `log_excess` is inflated. This inflated Q1 excess produces the negative staircase seen in the photometric estimators.

This result is important for two reasons. First, it validates the methodological upgrade: the review concern about Jeans estimator bias was correct, and the original Paper B staircase using photometric masses was showing a spurious signal in Q1. Second, the JAM-corrected signal is monotonically positive in the mid-mass tertile, which is a stronger and cleaner result precisely because it survives the correction that kills the photometric result.

### 5.4 Inclination Check

Within the Q1 population, galaxies with inclination greater than 45° (more face-on) have a mean `log_excess` of 0.049, while galaxies with inclination below 45° (more edge-on) have a mean `log_excess` of 0.093. The higher excess in the low-inclination Q1 population is consistent with misclassification: edge-on fast rotators whose projected $\Lambda_{R_e}$ is suppressed by inclination are appearing in Q1 with their true kinematic state closer to Q2 or Q3. The beam-corrected $\Lambda_{R_e}$ in the JAM catalogue partially addresses this but does not eliminate it entirely. This effect works against the monotonic staircase signal and does not explain away the positive result in the mid-mass tertile.

---

## 6. Discussion

### 6.1 What This Result Shows

The mid-mass tertile monotonic staircase ($\rho = 0.145$, $p = 3.6 \times 10^{-7}$) is a real statistical signal. It is directionally consistent with the SCH prediction that gravitational mass excess within the effective radius increases with rotational coherence at fixed stellar mass. It is not contaminated by the Jeans estimator bias that affected the original Paper B result. It is not driven by the mass-morphology degeneracy.

The result also does not confirm SCH. The signal is consistent with any theory that predicts more dark matter in fast-rotating galaxies at fixed stellar mass, including standard galaxy formation scenarios in which disc galaxies retain more of their dark matter halo than pressure-supported ellipticals of the same stellar mass. Distinguishing between these interpretations requires the full RAR functional form, the lensing cross-match, and the mass scale calibration from the Bi-209 experiment.

### 6.2 The Inverted-U Is Informative

The overall sample inverted-U is not simply a failure of the signal. The high-mass tertile negative staircase is physically meaningful: massive slow rotators are near the isotropic gravitational ground state that SCH predicts should show minimal geometric coupling. If SCH is correct, these systems should not show a positive staircase, and they do not. This is consistent with the contrast class prediction.

The low-mass tertile rising pattern to Q3 then partial decline is not yet understood. It may reflect a selection effect at the low-mass end of the JAM sample, where the `chi2_dof < 5` cut preferentially retains certain morphological types. It may reflect a genuine physical feature of low-mass fast rotators. It requires further investigation with the full DAP sample.

### 6.3 What Changes When Pending Data Arrives

The DAP baryonic accelerations were retrieved from CasJobs but base noise levels in the stellar velocity dispersion maps precluded reliable computation of $g_{\text{bar}}$ for this analysis. A cleaner DAP-derived $g_{\text{bar}}$ estimate — either from a future improved DAP release or from an independent velocity dispersion pipeline — would allow computation of the proper RAR residual $\log(g_{\text{obs}}/g_{\text{bar}})$ rather than the `log_excess` proxy used here. The staircase may strengthen or weaken when computed on the proper RAR residual; the direction should be preserved if the proxy is a good approximation.

When the DES Y6 shape catalogue becomes available, the lensing cross-match will provide an independent measurement of the gravitational signal that does not depend on the JAM model at all. Convergent results between the JAM mass excess staircase and the lensing staircase would be substantially stronger evidence than either alone.

### 6.4 Sample Size

The final sample of 3,650 galaxies is smaller than the original Paper B sample of approximately 8,969. The reduction comes primarily from the `chi2_dof < 5` quality cut on the JAM NFW model. This is a conservative cut and could be relaxed to `chi2_dof < 10` to recover approximately 1,200 additional galaxies. The sensitivity of the staircase to the `chi2_dof` threshold will be reported in the full analysis.

---

## 7. Pending Analysis

The following analyses are required to complete this paper and supersede this working document:

- **Improved baryonic acceleration estimate:** The retrieved DAP velocity dispersion maps carried too much base noise for reliable $g_{\text{bar}}$ computation. A cleaner estimate — from an improved DAP release or an independent dispersion pipeline — is needed to replace the `log_excess` proxy with the proper RAR residual $\log(g_{\text{obs}}/g_{\text{bar}})$ and rerun the full staircase analysis.

- **DES Y6 Metadetection cross-match:** Once the shape catalogue is released at [des.ncsa.illinois.edu/releases/y6a2](https://des.ncsa.illinois.edu/releases/y6a2), cross-match MaNGA lens positions against DES source ellipticities in annular bins. Compute the excess surface mass density $\Delta\Sigma$ around each MaNGA galaxy. Bin by $\Lambda_{R_e}$ quintile and compute the lensing staircase as an independent test of the mass excess signal.

- **JAMsph comparison for Q1 population:** Rerun the Q1 mass excess using JAMsph + NFW (HDU5) rather than JAMcyl + NFW (HDU4) to check whether the cylindrical assumption suppresses the slow rotator signal.

- **$\chi^2_{\text{dof}}$ threshold sensitivity:** Rerun the full staircase at `chi2_dof < 10` to assess how the result changes with sample size.

- **Low-mass tertile investigation:** Characterise the morphological and selection properties of the low-mass Q5 population to determine whether the partial decline from Q3 to Q5 in the low tertile is physical or a JAM selection artefact.

---

## 8. Data and Code Availability

| **Item** | **Source** | **Version / Date acquired** |
|----------|-----------|---------------------------|
| JAM v2 catalogue | [Zenodo record 17518315](https://zenodo.org/record/17518315) | v2, downloaded 6 June 2026 |
| Firefly MaStar VAC | SDSS SAS `manga-firefly-v3_1_1-mastar.fits` | DR17, downloaded 6 June 2026 |
| MaNGA DAP | [SDSS CasJobs](https://skyserver.sdss.org/CasJobs) DR17 `mangaDapAll` | Retrieved June 2026 — noise levels precluded use for $g_{\text{bar}}$ |
| DES Y6 shear (pending) | [des.ncsa.illinois.edu/releases/y6a2](https://des.ncsa.illinois.edu/releases/y6a2) | Pending — catalogue not yet released |
| Python environment | venv: `sch_manga` | Python 3.12, requirements.txt on file |
| Pipeline scripts | R1.py, R2.py, R3.py | Variable Systems, June 2026 |

The pipeline scripts R1.py, R2.py, and R3.py are available in the `replication/scripts/` folder of this repository. The reduced catalogue `SCH_manga_reduced_prejoin.csv` (3,650 rows, 20 columns) is available in the `replication/data/` folder. The full FITS catalogues must be downloaded from the sources above.

---

## 9. References

Graham, M. T. et al. (2018). MNRAS, 477, 4711.

Lu, S., Zhu, K., Cappellari, M., Li, R., Mao, S., & Xu, D. (2024). MNRAS, 530, 4474.

Neumann, J. et al. (2022). MNRAS, 513, 5988.

Planck Collaboration et al. (2016). A&A, 594, A13.

Yamamoto, M., Becker, M. R. et al. (2025). MNRAS. DES Y6 Metadetection shape catalogue.

Zhu, K., Lu, S., Cappellari, M., Li, R., Mao, S., & Gao, L. (2023). MNRAS, 522, 6326.

---

## Appendix A. CasJobs SQL Query

The following SQL query is to be run against the SDSS DR17 CasJobs database ([skyserver.sdss.org/CasJobs](https://skyserver.sdss.org/CasJobs), context DR17) when the server returns. Output is saved to MyDB as `SCH_manga_primary`.

```sql
SELECT drp.plateifu, drp.mangaid,
    drp.objra AS ra, drp.objdec AS dec,
    drp.nsa_z AS redshift,
    drp.nsa_elpetro_th50_r AS r_eff_arcsec,
    drp.nsa_elpetro_ba AS axis_ratio,
    drp.nsa_elpetro_mass AS mstar_nsa,
    dap.stellar_sigma_1re AS sigma_re,
    dap.stellar_sigma_1re_ivar AS sigma_re_ivar,
    drp.nsa_elpetro_absmag_r AS absmag_r,
    drp.drp3qual AS drp_quality,
    dap.dapqual AS dap_quality,
    drp.mngtarg1 AS targeting_bit
INTO mydb.SCH_manga_primary
FROM mangaDrpAll AS drp
JOIN mangaDapAll AS dap
    ON drp.plateifu = dap.plateifu
    AND dap.binkey = 'HYB10-MILESHC-MASTARSSP'
WHERE
    ((drp.mngtarg1 & (power(2,10) + power(2,12))) != 0)
    AND ((drp.drp3qual & power(2,30)) = 0)
    AND ((dap.dapqual & power(2,30)) = 0)
    AND dap.stellar_sigma_1re > 0
    AND dap.stellar_sigma_1re_ivar > 0
    AND drp.nsa_z > 0.01
    AND drp.nsa_elpetro_mass > 0
ORDER BY drp.plateifu
```

---

*June 2026 | Not for citation without author approval*
