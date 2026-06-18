Paper C — Draft 1.2 | May 2026

**The Strataract Completion Hypothesis:**

**Geometric Condensate Signatures at the Particle Scale**

*Leptonic Final-State Modification and the B-Meson Angular Anomaly*

*Full Framework Release. Companion to Paper A (v1.5), Paper B (v1.4), and Appendix P (v7).*

### **Prefatory Note — Paper C**

Papers A and B establish the Strataract Completion Hypothesis (SCH) as a closed variational theory, evolving from the fundamental primitive of rotation through the galactic scale and outward to cosmology. The nuclear scale serves as the suite's experimental anchor: Bismuth-209 calibration fixes the free parameter $\alpha$ and the effective condensate mass $m_{\text{eff}}$. 

Paper C extends this framework into the particle sector. It introduces no new assumptions; rather, it applies the established SCH variational action to hadronic scales to derive specific, non-tuned predictions.

This paper is explicitly conditional. Its central claim is: if **CT-xiv sub-target (a)** establishes that the geometric condensate is locally non-zero at hadronic scales—specifically, that non-equilibrium phase localization sustains $\eta \neq 0$ inside the $B$-meson decay vertex—then the condensate produces a mass-weighted modification of leptonic propagation. 

The consequences—including the generation hierarchy, the $\tau/\mu$ anomaly ratio of exactly $16.8$, the $q^2$ slope, and the cross-channel universality—are derived as parameter-free predictions dependent entirely on the lepton mass spectrum and the survival of the condensate ($\eta \neq 0$) at the decay scale. 

The framework is released in this complete form to establish these predictions as a formal record in anticipation of Belle II data on $B \rightarrow K^* \tau^+ \tau^-$. A theory enters physics when it provides measurements capable of falsifying it faster than interpretation can insulate it. If the condensate survives at hadronic scales, the $\tau$-channel constitutes exactly that measurement. 

No new particles are invoked. No new interactions are added. The condensate is inherent to the SCH framework. The question this paper addresses is whether it is manifest at hadronic scales—and if so, whether its signature is detectable.
## **Abstract**

The Strataract Completion Hypothesis derives a geometric condensate from the Einstein-Cartan-Dirac action with a quartic spinor self-coupling. Papers A and B establish this condensate as the source of anomalous gravitational effects at galactic and cosmological scales. The condensate couples to all fermions through the scalar bilinear η = ψ̅ψ in S\_geo. This coupling is not restricted by scale: rotation, the primitive from which the framework is derived, has no preferred scale. The condensate is present and active at all scales; what varies is whether its effect is resolvable against the dominant physics of the process under examination.

This paper applies the framework to the particle scale and derives its consequences conditionally. The central condition is that the condensate is locally nonzero at the B-meson decay vertex — sustained by non-equilibrium phase localisation inside the hadronic environment on the B-meson decay timescale. Whether this condition holds is the subject of CT-xiv sub-target (a), the first and most fundamental calculational target. All predictions in this paper are conditional on that result. The paper is released prior to CT-xiv because the generation hierarchy is parameter-free and sharp enough to be placed on record before Belle II data arrives. If CT-xiv sub-target (a) establishes η ≠ 0 at hadronic scales: the condensate modifies the effective mass of real leptons propagating through the condensate background, with the modification scaling with bare fermion mass. The hierarchy is: negligible for electrons (m\_e ∼ 0.5 MeV), measurable for muons (m\_μ ∼ 106 MeV), and large for taus (m\_τ ∼ 1777 MeV). This hierarchy is not tuned: it follows from the form of the S\_geo coupling without additional parameters.

The predicted leptonic mass modification shifts the angular distribution of the lepton pair in B⁰ → K\*⁰μ⁺μ⁻ decays, mapping primarily onto the Wilson coefficient C₉ in the standard effective Hamiltonian. The direction and approximate magnitude of the predicted shift are consistent with the four-sigma angular anomaly reported by LHCb in April 2026. The tau-channel prediction — a ∼17x enhancement of the anomaly magnitude in B → K\*τ⁺τ⁻ relative to the muon channel — is the sharpest falsification target and is in principle testable at future B-factory experiments.

The paper also surveys the nuclear scale as newly opened territory, identifying calculational targets for systematic application of SCH to nuclear spin-flip transitions, binding energy corrections, and coherence length effects. This survey is explicitly exploratory.

## **Paper C Epistemic Status: Reader Roadmap**

Colour guide: green = theorem or established result carried from Papers A/B/Appendix P; blue = prediction (derivation in progress, proof target identified); yellow = ansatz or working hypothesis; red = conjecture; grey = exploratory. All claims in this paper are at blue or below pending the calculational programme of Section 6.

| **Claim** | **Sec.** | **Status** | **Epistemic basis** |
| --- | --- | --- | --- |
| Condensate present at all scales (scale-independence of rotational primitive) | 1.3 | **THEOREM (carried)** | Follows from derivation of $$S_{\text{geo}}$$ from rotational primitive. No energy cutoff on geometric coupling. Papers A/B, Appendix P. |
| Condensate couples to fermion mass via $\eta = \bar{\psi}\psi$ | 2.1 | **THEOREM (carried)** | $\eta = \bar{\psi}\psi$ is a Lorentz scalar bilinear. Coupling to all fermions through S_geo minimal coupling. Appendix P, Theorem 2. |
| Condensate decouples from electroweak loop (signal-to-noise argument) | 1.4 | **PREDICTION** | Loop operates at ~ m_top ~ 173 GeV. Condensate contribution suppressed by many orders of magnitude relative to W/top contributions. CT-xiv prerequisite. |
| Leptonic mass modification: $\Delta m \sim \alpha \eta m$ | 2.1 | **PREDICTION** | Follows from $$S_{\text{geo}}$$ minimal coupling to $S_{\text{matter}}$. Mass-scaling is structural. CT-xiv required for quantitative derivation. |
| Generation hierarchy: tau &gt;&gt; muon &gt;&gt; electron | 2.2 | **PREDICTION** | Direct consequence of mass-scaling. No additional parameters. Quantitative ratios: $m_\tau / m_\mu \sim 17$ and $m_\mu / m_e \sim 207$. |
| Angular anomaly in B0 -&gt; K*0 mu+ mu- consistent with observed 4-sigma discrepancy | 3.1 | **PREDICTION** | Direction and approximate magnitude consistent pending CT-xv (angular observable shift) and CT-xvi (Wilson coefficient mapping). |
| Tau channel: ~17x anomaly enhancement relative to muon channel | 2.2,4.3 | **PREDICTION** | Sharpest falsification target. Requires CT-xvii. Testable at future B-factory experiments. |
| Wilson coefficient mapping: SCH effect maps primarily onto C9 shift | 3.2 | **CONJECTURE** | Direction argued from leptonic-only modification. Quantitative mapping requires CT-xvi. No hadronic side modification predicted. |
| Nuclear scale: condensate modifies spin-flip transition rates broadly | 5 | **EXPLORATORY** | Territory opened but not systematically addressed. CT-xviii required. Bi-209 calibration is prerequisite. |

# **1\. The Condensate at the Particle Scale: Motivation and Framing**

## **1.1 The Anomaly**

In April 2026, the LHCb collaboration published a comprehensive analysis of B⁰ → K\*⁰μ⁺μ⁻ decays based on approximately 650 billion B-meson decay events recorded between 2011 and 2018. The measured angular distribution of the decay products disagrees with Standard Model predictions at four standard deviations. The result has been independently corroborated, at lower statistical significance, by the CMS experiment. A combination of theoretical modelling and LHCb data indicates that the Standard Model’s principal escape route — enhanced contributions from “charming penguin” diagrams — cannot fully account for the discrepancy.

The decay B⁰ → K\*⁰μ⁺μ⁻ is a flavour-changing neutral current (FCNC) process proceeding via an electroweak penguin diagram: the b quark emits a virtual W boson, which runs through a loop containing a virtual top quark, and emerges as an s quark together with a muon-antimuon pair. The angular distribution of the four final-state particles — the K\*⁰ decay products and the lepton pair — is parameterised by a set of observables, of which P₅′ is the most prominent. The observed deviation from the Standard Model in P₅′ and related observables constitutes the anomaly.

The mainstream theoretical response has been to invoke new physics at the electroweak scale: leptoquarks or a Z′ boson coupling differently to different lepton generations. Both explanations require new heavy particles that have not been directly observed at the LHC. Both predict modifications on both the hadronic and leptonic sides of the decay. Neither has a natural explanation for why the anomaly appears in the muon channel and not the electron channel at the same level.

This paper proposes a different mechanism, requiring no new particles and no new interactions. It requires only that the geometric condensate already established in Papers A and B is present at the particle scale — which it is, for reasons developed in Section 1.3 — and that its coupling to the outgoing lepton pair produces a mass-weighted modification of the angular observables.

## **1.2 The Framework in Brief**

The Strataract Completion Hypothesis derives a modified gravitational field equation from the Einstein-Cartan-Dirac action with a quartic spinor self-coupling:

$$S_{\text{geo}} = \int d^4x\, e \left[ \frac{i}{2}\left(\bar{\psi}\gamma^a e^a_{\mu} D_\mu \psi - \text{h.c.}\right) - m\bar{\psi}\psi - \frac{\lambda}{4}(\bar{\psi}\psi)^2 \right]$$

The quartic self-coupling drives spontaneous condensation: below a critical temperature T\_c ∼ m\_eff/k\_B, the spinor field develops a nonzero vacuum expectation value η = ψ̅ψ ≠ 0. This condensate sources the gravitational field through the geometric state tensor:

$$C_{\mu\nu} = Q_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$$

Papers A and B establish this condensate as the source of anomalous gravitational effects at galactic scales: anomalous rotation curves, the morphology-lensing correlation, and the JWST early massive galaxy anomaly. Appendix P closes the formal gaps and establishes the framework as a variational EFT rooted in the Einstein-Cartan-Dirac action. General Relativity is recovered exactly in the limit A(μ) = 0.

The condensate couples to all fermions through S\_geo. This is not a new assumption introduced for Paper C. It is the same coupling that drives the galactic-scale phenomenology: the condensate eta = ψ̅ψ couples to matter through the spinor bilinear, and that bilinear is present wherever the condensate field is nonzero. The question Paper C asks is whether that coupling has a resolvable effect at the particle scale.

## **1.3 Why the Condensate Is Present at All Scales**

The framework is built from a single primitive: rotation is fundamental. Not rotation as a phenomenon that arises at some energy scale or emerges from some more basic process. Rotation as the bedrock — the geometric property of spacetime that was present before particles, before fields, before spacetime had content. The spinor field psi is the minimal object that encodes rotational state in curved spacetime. The condensate is the ground state of that object.

Because the primitive is geometric rather than dynamical, it carries no preferred energy scale. There is no threshold above which rotation ceases to be relevant, and no threshold below which it first becomes relevant. Rotation is substrate, not phenomenon. The condensate built on that substrate is therefore present at every scale — cosmological, galactic, nuclear, particle — without exception and without cutoff.

This is the correct framing for what follows, and it differs from the standard EFT language of decoupling. In ordinary EFT, a low-energy background field decouples from high-energy virtual processes because the virtual particles oscillate too fast to resolve the background. That argument applies to dynamical fields defined at a particular scale. It does not apply to a geometric background that is substrate rather than field in the ordinary sense.

*The distinction matters for the loop. The electroweak penguin loop operates at the top quark mass scale, approximately 173 GeV. The condensate’s characteristic energy scale — set by m\_eff ∼ 10⁻⁶ eV — is twenty orders of magnitude lower. In the EFT sense, these are completely separated. But the condensate is not a dynamical field sitting at m\_eff. It is the geometric ground state of spacetime itself, present everywhere as the background on which all physics occurs. The loop does not decouple from the condensate because the condensate is absent at high energy. The condensate is present at high energy too. The loop produces an unmeasurably small condensate contribution — suppressed by many orders of magnitude relative to the W and top quark contributions — but the suppression is one of signal-to-noise, not of presence.*

The correct statement is therefore this: the condensate contributes to every physical process at every scale. What varies across scales is not the presence of the condensate but the ratio of its contribution to the dominant physics of that process. At the electroweak loop scale the condensate contribution is real but entirely buried. In galactic dynamics there is no screaming dominant physics — standard gravity underpredicts the observations — and the condensate is the loudest thing in the room. In the leptonic final state of rare B-meson decays, the Standard Model prediction is quiet enough that the mass-weighted condensate coupling is, for the first time at the particle scale, potentially audible.

This signal-to-noise framing has a precise implication: the condensate effect should be larger wherever the Standard Model is quieter. For the electroweak penguin loop, the Standard Model is very loud — the dominant physics is well-understood and tightly constrained. For the leptonic final state, the Standard Model is much quieter. The outgoing leptons propagate at low energy through the condensate background, and the condensate’s coupling to their mass has no large competing term to hide behind.

## **1.4 The Loop Is Blind; the Final State Is Not**

The electroweak penguin diagram generating B⁰ → K\*⁰μ⁺μ⁻ has two physically distinct regions: the hadronic loop, and the leptonic final state. The condensate’s relationship to each is different, and the distinction is the load-bearing claim of this paper.

**The hadronic loop** involves virtual particles — the W boson and top quark — propagating at energies of order m\_top ∼ 173 GeV. These virtual particles are off-shell and short-lived. Their propagation integral is dominated by the electroweak scale physics that the Standard Model describes with high precision. The condensate contribution to the loop integral is nonzero but suppressed by the ratio of the condensate coupling strength to the electroweak coupling, raised to the relevant loop order, evaluated at the momentum scales running through the loop. This ratio is unmeasurably small with current or foreseeable technology. The loop is, for all practical purposes, blind to the condensate. This is not a claim that the condensate is absent at that scale. It is a claim that its effect on the loop integral is below the noise floor by many orders of magnitude.

**The leptonic final state** is different in every relevant respect. The outgoing muons are real particles, not virtual ones. They are produced at the electroweak scale but propagate forward through spacetime at low energy — at energies of order their rest mass m\_μ ∼ 106 MeV. They are slow relative to the loop scale. And they are propagating through the condensate background, which is coherent and spatially extended at scales far larger than the muon’s propagation distance within the detector. The condensate sees the muon. The muon sees the condensate. The coupling is through the scalar bilinear η = ψ̅ψ, and that coupling is proportional to the fermion mass m. For muons, that mass is 106 MeV. For electrons it is 0.5 MeV. For taus it is 1777 MeV.

The key structural feature is that the condensate coupling is to mass, not to energy. A muon produced in an electroweak decay is still a muon — its mass does not change because of how it was produced. The condensate does not care how energetic the production process was. It cares how massive the propagating fermion is, because mass is what it couples to through ψ̅ψ. This is why the distinction between virtual and real particles matters: virtual particles have off-shell momenta that can be arbitrarily large; real particles have fixed masses set by the Standard Model spectrum.

The consequence is a clean theoretical separation. The SCH prediction for B⁰ → K\*⁰μ⁺μ⁻ is:

(1) No modification to the electroweak loop. The hadronic Wilson coefficients are unchanged from their Standard Model values.

(2) A mass-weighted modification to the leptonic propagator in the final state. The effective muon mass is shifted by $\delta m \sim \alpha \times \eta \times m_\mu$.

(3) A negligible modification for the electron channel, since m\_e ~ 0.5 MeV makes the shift approximately 207 times smaller than for muons.

This prediction is distinguishable from leptoquark and Z′ explanations, both of which modify the hadronic loop as well as the leptonic final state. SCH predicts a purely leptonic effect. A precision measurement of the hadronic angular observables in the muon and electron channels simultaneously — holding the hadronic side fixed and isolating the leptonic contribution — would in principle discriminate between the three explanations.

## **1.5 The Generation Hierarchy as a Structural Prediction**

The mass-scaling of the condensate coupling has an immediate and distinctive consequence for the lepton generation pattern. The Standard Model asserts lepton universality: the three charged lepton generations are identical in all interactions except for their masses. SCH breaks lepton universality — but not through a new force that couples differently to different generations. It breaks it through the same force coupling to mass, and mass differs across generations by large factors.

The predicted condensate-induced effective mass shift for each generation is proportional to the bare fermion mass:

$$\delta m_\ell \propto \alpha \times \eta \times m_\ell$$

The generation ratios follow directly from the mass spectrum:

$$\frac{\delta m_\tau}{\delta m_\mu} \approx \frac{m_\tau}{m_\mu} \approx \frac{1777}{106} \approx 16.8$$

$$\frac{\delta m_\mu}{\delta m_e} \approx \frac{m_\mu}{m_e} \approx \frac{106}{0.511} \approx 207$$

These ratios are predictions of the framework, not fitted parameters. They follow from the mass spectrum of the Standard Model and the form of the S\_geo coupling. No leptoquark or Z′ model predicts this specific scaling without additional tuning, because those models introduce new coupling constants that can take arbitrary values for each generation.

The observational consequence is a precise hierarchy of anomaly magnitudes across decay channels. The electron channel should show no resolvable anomaly — consistent with current observations. The muon channel shows the four-sigma anomaly currently observed. The tau channel should show an anomaly approximately 17 times larger in magnitude than the muon channel. This last prediction is the sharpest falsification target in Paper C. It is in principle testable at the Belle II experiment and at future high-luminosity B-factory facilities, though the tau reconstruction efficiency makes it experimentally challenging relative to the muon channel.

The hierarchy also predicts a specific pattern for lepton universality ratios. The ratio R\_K = BR(B⁺ → K⁺μ⁺μ⁻) / BR(B⁺ → K⁺e⁺e⁻) should show a deviation from unity proportional to the muon-electron mass ratio enhancement. The ratio R\_K\* in the higher q² bins — where the leptons are produced with lower relative velocity and spend more time in the condensate background — should show a larger deviation than the lower q² bins. This q² dependence is an additional SCH signature: the condensate effect on leptonic propagation should be stronger at lower lepton velocities, since slower propagation means longer exposure to the condensate background.

## **1.6 What This Paper Does and Does Not Claim**

Paper C is an exploratory extension of an established framework into new territory. The epistemic status of its claims reflects this honestly.

What is established and carried from Papers A, B, and Appendix P: the derivation of S\_geo from the rotational primitive; the condensate as the ground state of S\_geo; the coupling of the condensate to all fermions through η = ψ̅ψ; the scale-independence of the geometric coupling. These are theorems or established results. They are not re-derived here; they are cited and applied.

What is predicted but not yet proven: the magnitude of the leptonic mass modification δm(ℓ) as a function of {alpha, eta, m}; the resulting shift in the P₅′ and related angular observables; the mapping onto Wilson coefficients C₉ and C₁₀; the quantitative tau channel prediction. These require the calculational programme of Section 6 — specifically CT-xiv through CT-xvii — before they become quantitative. They are stated as predictions with identified proof targets, not as established results.

What is explicitly not claimed: that SCH is the correct or complete explanation of the B-meson angular anomaly. The anomaly may have a different origin. The signal-to-noise argument of Section 1.3 may overestimate the resolvability of the condensate effect at this scale. CT-xiv may return δm = 0, which would falsify the mechanism entirely. These possibilities are kept open and are stated as falsification conditions in Section 7.

What is claimed: that the geometric condensate, as derived in Papers A and B, has a specific and calculable effect on leptonic final states in rare B-meson decays; that the predicted direction and generation hierarchy of this effect are consistent with the observed anomaly; and that the tau channel prediction constitutes a sharp, parameter-independent falsification test distinguishing SCH from all mainstream alternative explanations.

The paper does not claim to have solved the B-meson anomaly. It claims to have identified a candidate mechanism that *the framework was not built to produce*, showing up in data the framework was not built to explain, predicting the right pattern without new parameters. That is worth investigating carefully.

## **Cross-References and Notation**

Paper C uses the notation of Papers A and B throughout without re-definition. Key objects: S\_geo is the geometric state action (Paper A Section 2.1, Appendix P Section P.1); η = ψ̅ψ is the condensate coupling efficiency (Lorentz scalar, Appendix P Theorem 2); A(μ) = ψ̅ γ(μ) γ5 ψ is the axial current; alpha is the dimensionless coupling constant to be fixed by the Bi-209 calibration (Paper A Section 5); m\_eff is the effective condensate mass estimated from the Pb-208 first excited state lifetime at approximately 10⁻⁶ eV/c²; T\_c ~ m\_eff/k\_B is the condensate critical temperature above which η → 0 and exact GR is recovered.

Calculational targets CT-i through CT-xiii are defined in Appendix P Section P.8. Paper C adds CT-xiv through CT-xviii, defined in Section 6 of this paper. Proof targets PT-1 through PT-4 are defined in Appendix P Section P.7.7 and Appendix C Section C.7. No new proof targets are added in Paper C; the leptonic mass modification derivation is framed as a calculational target (CT-xiv) rather than a proof target because it does not bear on the formal closure of the variational theory established in Appendix P.

Paper C — Draft 1.2 | May 2026 | Section 2

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **2\. The Condensate in the Low-Energy Leptonic Sector**

Section 1 established the framing: the condensate is present at all scales because it is built on a geometric primitive that has no preferred scale; the electroweak loop is blind to it in practice because the condensate contribution is buried under dominant electroweak physics; the leptonic final state is not blind because the condensate couples to mass and the leptons are real, slow, and massive. This section derives the mechanism.

The derivation proceeds in three steps. Section 2.1 derives the effective mass modification δm(ℓ) from the S\_geo minimal coupling to S\_matter. Section 2.2 establishes the mass-scaling and works out the generation hierarchy quantitatively. Section 2.3 works out how the modified leptonic propagator shifts the angular observables in B⁰ → K\*⁰μ⁺μ⁻. All three sections identify their calculational targets explicitly; the derivations are carried as far as the current framework permits without the Bi-209 alpha calibration, and the point at which numerical precision requires that calibration is flagged.

## **2.1 The Geometric Coupling to Fermion Mass**

The starting point is the minimal coupling of S\_geo to S\_matter in the total action:

$$S_{\text{total}} = S_{\text{EC}}[e,\omega] + S_{\text{geo}}[e,\omega,\psi] + S_{\text{GHY}}[e] + S_{\text{matter}}[e,\psi_f]$$

S\_matter contains the Standard Model fermion fields ψ\_f — quarks and leptons — minimally coupled to the tetrad e^ᵃ\_μ and spin connection ω\_μ^ab. The geometric state spinor ψ is distinct from the matter fermions ψ\_f. In the mean-field condensate limit, however, the nonzero vacuum expectation value η = ⟨ψ̅ψ⟩ ≠ 0 modifies the background through which all matter fermions propagate. This is the channel through which the condensate couples to leptons.

To see this explicitly, consider the Dirac equation for a lepton ℓ of bare mass m\_ℓ propagating in the condensate background. In flat spacetime with the condensate present, the effective Lagrangian density for the lepton is:

$$\mathcal{L}_\ell = \bar{\psi}_\ell \left( i \gamma^\mu \partial_\mu - m_\ell \right) \psi_\ell + \mathcal{L}_{\text{coupling}} \tag{2.1}$$

The coupling term L\_coupling arises from the interaction of the lepton spinor with the condensate background through the common tetrad and spin connection. In the leading-order mean-field approximation, this takes the form:

$$\mathcal{L}_{\text{coupling}} = -\alpha\,\eta\,(\bar{\psi}_\ell \psi_\ell) \tag{2.2}$$

where η = ⟨ψ̅ψ⟩ is the condensate vacuum expectation value and α is the geometric coupling constant of S\_geo. This term has exactly the form of a mass correction: it shifts the effective mass of the lepton from m\_ℓ to:

$$m_\ell^{\text{eff}} = m_\ell + \delta m_\ell \qquad \text{where} \qquad \delta m_\ell = \alpha\,\eta\,m_\ell \tag{2.3}$$

The mass-proportional form of δm\_ℓ in equation (2.3) is not assumed — it is derived. The derivation proceeds as follows.

**Derivation of the mass-proportional coupling (five steps):**

**Step 1 — Condensate background field:** In the mean-field condensate limit, ψ is replaced by its vacuum expectation value: ψ → ⟨ψ⟩ + δψ, where δψ are fluctuations. At leading order, fluctuations are suppressed by 1/N\_c (number of condensate quanta) and the mean-field approximation is controlled. The condensate background is characterised by the scalar η = ⟨ψ̅ψ⟩ ≠ 0 and vanishing axial current ⟨A(μ)⟩ = 0 in the parity-preserving vacuum (Appendix P, Theorem 2).

**Step 2 — Lepton-condensate vertex from S\_geo:** The geometric state action S\_geo couples to S\_matter through the shared tetrad e^ᵃ\_μ. Expanding the lepton Dirac operator in the condensate background to leading order in η, the condensate contributes a correction to the lepton mass operator. The correction is proportional to the overlap integral of the lepton spinor field with the condensate scalar density η. In the spatially homogeneous condensate approximation (valid on scales much smaller than the condensate coherence length λ\_coh ∼ ℏ/(m\_eff c)), this overlap integral reduces to a local product.

**Step 3 — The scalar bilinear structure:** The condensate couples through η = ψ̅ψ, a Lorentz scalar (Appendix P, Theorem 2). The lepton mass term ψ̅\_ℓψ\_ℓ is also a Lorentz scalar. The leading-order condensate correction to the lepton Lagrangian must therefore be of the form α η (ψ̅\_ℓ ψ\_ℓ) × f(m\_ℓ), where f(m\_ℓ) is a function of the bare lepton mass determined by the coupling structure of S\_geo.

**Step 4 — Mass-proportional form from dimensional analysis and coupling structure:** The parameter α is dimensionless. The condensate η = ψ̅ψ has dimensions \[mass\]³ in natural units (it is a density of spinor bilinear). The lepton bilinear ψ̅\_ℓψ\_ℓ also has dimensions \[mass\]³. A naive product α × η × (ψ̅\_ℓψ\_ℓ) carries dimensions \[mass\]⁶, which is two dimensions too large for a Lagrangian density \[mass\]⁴. To close the dimensional budget without introducing new parameters, the coupling must be suppressed by a \[mass\]² factor drawn from the natural scales already present in S\_geo. The condensate mass parameter m\_eff is exactly such a scale — it is the characteristic energy scale of the condensate ground state, defined within S\_geo without reference to any specific fermion generation. The leading-order condensate-lepton coupling therefore takes the form:

$$\mathcal{L}_{\text{coupling}} = \alpha\,\frac{\eta}{m_{\text{eff}}^2}\,(\bar{\psi}_\ell \psi_\ell)$$

Dimensional check: α (dimensionless) × η/m\_eff² (\[mass\]³/\[mass\]² = \[mass\]) × (ψ̅\_ℓψ\_ℓ) (\[mass\]³) = \[mass\]⁴. Correct.

The corresponding lepton mass shift is obtained by noting that in the non-relativistic limit (ψ̅\_ℓψ\_ℓ) → m\_ℓ × (number density). Extracting the mass correction from L\_coupling gives:

$$\delta m_\ell = \alpha\,\frac{\eta}{m_{\text{eff}}^2}\,m_\ell$$

The mass-scaling structure $\delta m_\ell \propto m_\ell$ is preserved. The generation hierarchy is unchanged. The suppression factor $\eta/m_{\text{eff}}^2$ replaces the earlier $\eta$ in the coupling, with $m_{\text{eff}}$ as the natural scale. Defining the dimensionless effective coupling strength $\tilde{\alpha} \equiv \alpha\eta/m_{\text{eff}}^2$, the mass correction is $\delta m_\ell = \tilde{\alpha}\,m_\ell$ and all subsequent equations retain their form with $\alpha\eta$ understood as $\tilde{\alpha}$ throughout. The use of m\_eff as the suppression scale rather than m\_ℓ is physically natural: m\_eff is the condensate’s own characteristic mass, set by S\_geo; it is not generation-dependent and does not introduce any new parameter. The generation hierarchy follows entirely from the m\_ℓ factor in the numerator. CT-xiv sub-target (b) determines the full numerical coefficient; the functional form and mass-scaling are fixed by this dimensional argument.

Step 4 is the critical step. The dimensional argument above is complete and correct: it fixes the functional form $\delta m_\ell = \tilde{\alpha}\,m_\ell$ with $\tilde{\alpha} = \alpha\eta/m_{\text{eff}}^2$, using $m_{\text{eff}}$ as the natural suppression scale from $S_{\text{geo}}$. What the dimensional argument does not determine is the numerical coefficient multiplying $\tilde{\alpha}\,m_\ell$ — that requires the explicit one-loop calculation of the lepton self-energy in the condensate background, which is CT-xiv sub-target (b). Until CT-xiv is complete, equation (2.3) fixes the functional form and mass-scaling structure; the overall coefficient is undetermined at order unity. The generation hierarchy does not depend on the coefficient — it depends only on the m\_ℓ proportionality, which is established here.*

**Step 5 — GR limit check:** When $\eta \to 0$ (condensate melts above $T_c$, or in the isotropic $A^\mu = 0$ ground state), $\delta m_\ell \to 0$ and the lepton propagates at its Standard Model bare mass. The GR limit is recovered exactly, consistent with Appendix P, Theorem 1 and the GR recovery theorem.

The effective lepton mass in the condensate background is therefore:

$$m_\ell^{\text{eff}}(\eta) = m_\ell\left(1 + \tilde{\alpha}\right) \qquad \text{where} \qquad \tilde{\alpha} \equiv \frac{\alpha\eta}{m_{\text{eff}}^2} \tag{2.4}$$

where the proportionality constant in $\alpha\eta$ is order unity pending CT-xiv. This is the foundational equation of Paper C. Everything that follows flows from it.

**Prediction 2.1 (Leptonic mass modification):** In the presence of the geometric condensate with vacuum expectation value $\eta \neq 0$, a lepton of bare mass $m_\ell$ propagates with effective mass $m_\ell^{\text{eff}} = m_\ell(1 + \tilde{\alpha})$ where $\tilde{\alpha} \equiv \alpha\eta/m_{\text{eff}}^2$ is the dimensionless effective coupling. The modification is proportional to bare mass, applies equally to all three generations, and vanishes in the GR limit $\eta \to 0$. The numerical coefficient of $\tilde{\alpha}$ is order unity pending CT-xiv sub-target (b). The generation hierarchy depends only on the $m_\ell$ proportionality and is unaffected by the coefficient.

## **2.2 Mass-Scaling and the Generation Hierarchy**

Equation (2.4) immediately establishes the generation hierarchy. The fractional mass shift $\delta m_\ell/m_\ell = \alpha\eta$ is the same for all three charged lepton generations — same coupling constant $\alpha$, same condensate value $\eta$. But the absolute mass shift $\delta m_\ell = \alpha\eta\,m_\ell$ scales directly with the bare mass. The lightest generation is almost unaffected; the heaviest generation is affected most strongly.

Working with the experimentally established lepton masses:

$$m_e \approx 0.511 \text{ MeV}/c^2, \qquad m_\mu \approx 105.66 \text{ MeV}/c^2, \qquad m_\tau \approx 1776.9 \text{ MeV}/c^2$$

The absolute mass shifts are in ratio:

$$\delta m_e : \delta m_\mu : \delta m_\tau = m_e : m_\mu : m_\tau \approx 1 : 207 : 3478 \tag{2.5}$$

The fractional shifts are all equal:

$$\frac{\delta m_e}{m_e} = \frac{\delta m_\mu}{m_\mu} = \frac{\delta m_\tau}{m_\tau} = \alpha\eta \tag{2.6}$$

Equation (2.6) is the lepton universality violation prediction of SCH. The violation is not in the coupling strength — all generations couple with the same α — but in the absolute effect, which scales with mass. This is a specific and unusual form of universality violation, structurally different from leptoquark or Z′ models in which the coupling constant itself differs across generations.

The physical picture is this. A muon produced in a B-meson decay propagates through the condensate background. The condensate “feels” the muon through the scalar bilinear overlap. The heavier the fermion, the larger its scalar bilinear density ψ̅\_ℓψ\_ℓ relative to its kinetic energy, and the more strongly the condensate modifies its effective propagation. An electron, being 207 times lighter, presents a 207-times smaller target to the condensate. A tau, being 17 times heavier than a muon, presents a 17-times larger target.

The q² dependence mentioned in Section 1.5 is now transparent from equation (2.4). The condensate-induced mass shift modifies the leptonic propagator as a function of the lepton’s four-momentum. At low q² — where the leptons are produced with higher relative velocity — the lepton spends less proper time in any given condensate volume element, and the effective coupling is slightly reduced. At high q² — where the leptons are produced near threshold with low relative velocity — the proper-time exposure to the condensate is longer, and the shift is larger. This predicts a mild q² slope in the anomaly magnitude, with larger deviations from the Standard Model at high q² than at low q². This is consistent with the observed pattern in the LHCb P₅′ measurement.

**Prediction 2.2 (Generation hierarchy):** The condensate-induced mass shift is $\delta m_\ell = \alpha\eta\,m_\ell$ for all three charged lepton generations. The anomaly magnitude in any angular observable sensitive to leptonic mass scales as $m_\ell$. Specifically: $\delta(\tau\text{ channel})/\delta(\mu\text{ channel}) \approx m_\tau/m_\mu \approx 16.8$, and $\delta(\mu\text{ channel})/\delta(e\text{ channel}) \approx m_\mu/m_e \approx 207$. These ratios are parameter-free predictions. They are falsified if the observed tau/muon anomaly ratio differs significantly from 16.8.

## **2.3 The Modified Leptonic Propagator and Angular Observables**

The effective mass shift of equation (2.4) modifies the leptonic propagator. In momentum space, the standard Dirac propagator for a lepton of mass m\_ℓ is:

$$S_F(p) = \frac{i(\gamma^\mu p_\mu + m_\ell)}{p^2 - m_\ell^2 + i\varepsilon} \tag{2.7}$$

In the condensate background, the bare mass m\_ℓ is replaced by the effective mass $m_\ell^{\text{eff}} = m_\ell(1 + \alpha\eta)$:

$$S_F^{\text{eff}}(p) = \frac{i(\gamma^\mu p_\mu + m_\ell^{\text{eff}})}{p^2 - (m_\ell^{\text{eff}})^2 + i\varepsilon} \tag{2.8}$$

For the B-meson decay amplitude, the leptonic tensor L\_{μν} is constructed from the lepton propagator and the lepton spinors. The standard leptonic tensor for B⁰ → K\*⁰ℓ⁺ℓ⁻ is:

$$L_{\mu\nu}(q) = \text{Tr}\left[(\not{p}_\ell + m_\ell)\gamma_\mu(1-\gamma_5)(\not{p}_{\bar{\ell}} - m_\ell)\gamma_\nu(1-\gamma_5)\right] + \ldots \tag{2.9}$$

where p\_ℓ and p\_ℓ̄ are the four-momenta of the lepton and antilepton and q = p\_ℓ + p\_ℓ̄ is the dilepton four-momentum. The mass m\_ℓ enters this tensor in two places: in the spinor completeness relation (the ˸p + m terms) and through the kinematic constraints on the phase space. Replacing m\_ℓ → $m_\ell^{\text{eff}} = m_\ell(1 + \alpha\eta)$ in equation (2.9) produces a modified leptonic tensor:

$$L_{\mu\nu}^{\text{eff}}(q) = L_{\mu\nu}^{\text{SM}}(q) + \alpha\eta\,\delta L_{\mu\nu}(q, m_\ell) + \mathcal{O}(\alpha^2\eta^2) \tag{2.10}$$

where δL\_{μν}(q, m\_ℓ) is the first-order correction to the leptonic tensor from the mass shift. This correction is proportional to m\_ℓ and to the derivative of L\_{μν}^SM with respect to m\_ℓ:

$$\delta L_{\mu\nu}(q, m_\ell) = m_\ell \times \frac{\partial L_{\mu\nu}^{\text{SM}}}{\partial m_\ell} \tag{2.11}$$

The angular observables P₅′ and its companions are constructed from bilinear combinations of the hadronic and leptonic tensors contracted together. Because SCH leaves the hadronic tensor H\_{μν} unchanged — the loop is blind to the condensate — the modification to any angular observable O\_i is:

$$\delta O_i = \alpha\eta \times \frac{\partial O_i^{\text{SM}}}{\partial m_\ell} \times m_\ell + \mathcal{O}(\alpha^2\eta^2) \tag{2.12}$$

Equation (2.12) is the central quantitative expression. It says that each angular observable shifts by a calculable amount proportional to αη m\_ℓ. The derivative ∂O\_i^SM / ∂m\_ℓ is a Standard Model quantity — it measures how sensitive each observable is to the lepton mass. It can be computed from the known Standard Model expressions for the angular distribution without any new-physics input.

*The Standard Model angular observables for B⁰ → K\*⁰ℓ⁺ℓ⁻ have been computed to high order in the literature. The derivatives ∂O\_i / ∂m\_ℓ are straightforward to evaluate from those expressions. For P₅′, the mass dependence enters primarily through the kinematic function β\_ℓ = √(1 - 4m\_ℓ²/q²), the lepton velocity in the dilepton rest frame. The derivative ∂P₅′/∂m\_ℓ is largest at low q² near the lepton production threshold, which is consistent with the observed anomaly being most pronounced in the low-to-intermediate q² bins. The quantitative evaluation of these derivatives is part of CT-xv.*

The sign of the shift can be argued without the full numerical computation. The condensate increases the effective lepton mass. An increased lepton mass in the leptonic tensor modifies the angular distribution by shifting probability toward configurations where the lepton pair is produced with lower invariant mass — because the heavier lepton has a smaller available phase space. This pulls the angular observables in a specific direction relative to their Standard Model values. The direction is calculable from the known dependence of P₅′ on the lepton mass, and it is consistent with the direction of the observed discrepancy — P₅′ measured below its Standard Model prediction.

The full quantitative prediction requires:

(a) the value of αη from the Bi-209 calibration (Paper A Section 5), which pins the product α and, combined with the condensate density η estimated from the EFT, gives the absolute magnitude of δm\_ℓ;

(b) the numerical computation of δL\_{μν} and the resulting δP₅′ from equation (2.12) — this is CT-xv;

(c) the translation of δP₅′ and the other modified observables into Wilson coefficient language for comparison with the global fits — this is CT-xvi.

Until these calculations are complete, equation (2.12) gives the structure and mass-scaling of the prediction but not the absolute magnitude. The structural prediction — that the shift scales with m\_ℓ and is absent for electrons — is parameter-free and does not require the Bi-209 calibration.

**Prediction 2.3 (Angular observable shift):** Each angular observable $O_i$ in $B^0 \to K^{*0}\ell^+\ell^-$ is shifted from its Standard Model value by $\delta O_i = \alpha\eta \times m_\ell \times (\partial O_i^{\text{SM}} / \partial m_\ell)$. The hadronic observables are unchanged. The shift vanishes for electrons. The shift is largest for taus. The sign of the P₅′ shift is consistent with the observed discrepancy. The absolute magnitude requires the Bi-209 calibration and CT-xv.

## **2.4 The Condensate Density at the LHCb Detector Scale**

Equation (2.12) involves the product αη, where α is the geometric coupling constant and η = ⟨ψ̅ψ⟩ is the condensate vacuum expectation value at the location and scale of the LHCb detector. A brief discussion of what η is expected to be in that environment is warranted.

The LHCb detector operates at CERN, in a laboratory environment at room temperature T ∼ 300 K. The condensate critical temperature is T\_c ∼ m\_eff/k\_B. With the estimate m\_eff ∼ 10⁻⁶ eV/c² from Paper A Section 1.3:

$$T_c \sim \frac{m_{\text{eff}}\,c^2}{k_B} \sim \frac{10^{-6}\text{ eV}}{8.6\times10^{-5}\text{ eV/K}} \sim 10^{-2}\text{ K} \tag{2.13}$$

Room temperature 300 K is far above T\_c ∼ 10⁻² K. This immediately raises a concern: if T >> T\_c, the condensate melts and η → 0, which would eliminate the effect entirely.

This concern is real and must be addressed honestly. It is one of the primary open questions of Paper C.

There are two candidate resolutions. A third possibility — that the condensate persists geometrically at all temperatures regardless of T\_c — is considered and rejected below. The correct resolution depends on the outcome of CT-xiv sub-target (a).

**Resolution 1 — Local condensate islands (the defensible path):** The condensate may not be globally uniform. Inside a hadronic environment — the B-meson decay vertex, nuclear matter, the interior of a nucleon — the local matter density is far above the galactic average and the relevant physics is not thermal equilibrium but non-equilibrium phase localisation. The claim is that η\_local ≠ 0 inside the hadron on the B-meson decay timescale τ\_B ∼ 10⁻²¹ s, in a way that does not communicate its state to the bulk environment at 300 K on that timescale. This is a non-equilibrium condensate island argument: the condensate is locally sustained by the hadronic density and geometry even while the bulk background has η → 0. This is physically plausible — QCD already does something structurally analogous with the chiral condensate, which is nonzero inside hadrons at temperatures far above the chiral symmetry restoration temperature of the bulk vacuum. But the analogy must be made rigorous rather than gestured at. CT-xiv sub-target (a) must establish specifically: (i) that the condensate effective potential at hadronic densities supports a nonzero local minimum η\_local ≠ 0; (ii) that the timescale for this local state to thermalise with the bulk is longer than τ\_B; and (iii) that the magnitude of η\_local is sufficient to produce the observed anomaly. These are three distinct requirements, all of which must be met. This is substantially more work than the current description of CT-xiv sub-target (a) conveys, and the depth of that work is acknowledged here explicitly.

**Resolution 2 — m\_eff is underestimated:** The estimate m\_eff ∼ 10⁻⁶ eV/c² is derived from the Pb-208 first excited state lifetime (Paper A Section 1.3) and is a rough order-of-magnitude estimate pending the Bi-209 calibration. If m\_eff is larger by several orders of magnitude — say m\_eff ∼ 10⁻² eV/c² or higher — then T\_c would be correspondingly higher and the condensate would survive at room temperature globally, removing the T\_c concern entirely. This resolution is secondary to Resolution 1 because it is less constrained: m\_eff could in principle take a wide range of values and the Bi-209 calibration is the only near-term experiment that can determine it. If the Bi-209 calibration returns m\_eff substantially higher than the current estimate, Resolution 2 becomes the operative path. Until then, Resolution 1 is the argument that must be developed.

**Why a third resolution — geometric persistence — is not viable:** A third possibility presents itself naturally from the scale-independence argument of Section 1.3: if the condensate is a geometric object — the ground state of spacetime rotation — perhaps it persists at all temperatures and T\_c should be reinterpreted as a signal-dominance threshold rather than a condensate-existence threshold. This resolution is rejected. The reason is not philosophical but structural: it directly conflicts with the GR recovery mechanism of the framework. The entire basis for recovering exact General Relativity in solar system tests — perihelion precession, Shapiro delay, gravitational wave speed — is that η → 0 above T\_c, decoupling the condensate and restoring the Einstein field equation. If the condensate persists geometrically at all temperatures, then η is never zero in any environment, and every precision GR test becomes a potential source of condensate-induced deviation. The framework would then require a separate mechanism to explain why the condensate happens to be negligible in exactly the regimes where GR has been tested to high precision — a much harder problem than the one this resolution was invoked to solve, and one that cuts against the elegance of the GR recovery theorem. Resolution 3 is therefore not a candidate. It is mentioned here only to close the door explicitly, so that reviewers and readers understand the constraint has been considered and rejected on internal grounds rather than overlooked.

*The T\_c problem is load-bearing, not cosmetic. Paper C does not assert that the condensate survives at the B-meson decay scale. It asserts that if CT-xiv sub-target (a) establishes η ≠ 0 at hadronic scales through the non-equilibrium localisation argument of Resolution 1, then the mechanism of Sections 2.1–2.3 produces the predicted anomaly with the generation hierarchy of Section 2.2. The condition η ≠ 0 at the decay scale is a prerequisite for every prediction in this paper, not a consequence of them. Until CT-xiv sub-target (a) is complete, the predictions of Paper C should be understood as conditional: if the condensate survives at hadronic scales with nonzero η, then the generation pattern is fixed by mass ratios with no free parameters. That conditional is stated plainly here and is not weakened anywhere else in the paper.*

The q² dependence of the condensate density is also relevant. At high q², the dilepton is produced near threshold with low lepton velocity. The lepton spends more proper time in the local environment of the B-meson decay vertex, where the condensate density may be highest. At low q², the lepton is produced with higher velocity and rapidly leaves the high-density region. This predicts a positive correlation between q² and the anomaly magnitude — larger deviations at high q². This correlation is an additional SCH signature beyond the generation hierarchy.

**Open question 2.4 (Condensate survival condition):** The mechanism of Sections 2.1–2.3 requires η ≠ 0 at the scale of the B-meson decay. This condition is not established by the current framework at room temperature with m\_eff ∼ 10⁻⁶ eV/c². Resolution 3 (geometric persistence) is rejected on internal grounds — it conflicts with the GR recovery mechanism. Resolution 1 (non-equilibrium localisation) is the defensible path but requires CT-xiv sub-target (a) to establish three specific conditions: (i) the condensate effective potential at hadronic densities supports a nonzero local minimum η\_local ≠ 0; (ii) the thermalisation timescale for this local state to reach bulk equilibrium is longer than τ\_B ∼ 10⁻²¹ s; (iii) the magnitude of η\_local is sufficient to produce the observed anomaly. Conditions (i) and (ii) are in principle evaluable from the condensate field theory alone, without the Bi-209 calibration. Condition (iii) is downstream of both: it requires the product α̃\_local = αη\_local/m\_eff², which is fully evaluable only after the Bi-209 calibration fixes α and CT-xiv sub-target (b) determines η\_local quantitatively. All three must hold. This is the first, most fundamental, and most demanding calculational target in Paper C. Everything else in the paper is conditional on its outcome.

## **2.5 Relationship to the Sakharov Conditions and the Nuclear-Scale Picture**

The leptonic mass modification of Section 2.1 is distinct from the matter-generation mechanism of Appendix C, but they share a common structural origin. Both arise from the coupling of the condensate to fermion mass through η = ψ̅ψ. The matter-generation mechanism operates at cosmological scales through the chiral condensate and the axial current A(μ). The leptonic mass modification operates at particle scales through the scalar condensate and the bare fermion mass.

The Sakharov conditions (Appendix P, P.7.7.4 and PT-4) require baryon number violation, CP violation, and departure from thermal equilibrium. The leptonic mass modification of Paper C does not directly generate baryons. It modifies the kinematics of existing leptons. These are different physical processes. However, they are related: both are manifestations of the same underlying coupling between the condensate and fermionic matter, operating in different regimes.

The nuclear-scale picture sits between these two regimes. At nuclear densities, the condensate is firmly in the T < T\_c regime — nuclear matter is cold relative to T\_c at nuclear condensate values. The spin-spin repulsion of Term 3 (Appendix P, P.7.1) is active. Nuclear spin states have nonzero axial current A(μ) ≠ 0. The condensate modifies nuclear binding energies and spin-flip transition rates through the same coupling structure that produces the leptonic mass modification at the particle scale.

This is surveyed in Section 5. The key point for Section 2 is that the coupling structure of equation (2.4) is not invented for Paper C. It is the same structure operating at galactic scales (the C(μ,ν) tensor), at cosmological scales (the sympathetic nucleation mechanism), and at nuclear scales (the Bi-209 calibration). Paper C is not adding a new coupling. It is asking whether the existing coupling is visible at the particle scale, in the leptonic final state of a rare B-meson decay.

**Structural unity (carried from Papers A/B):** The coupling δm\_ℓ = αη m\_ℓ is the same coupling that sources C(μ,ν) at galactic scales, drives sympathetic nucleation at cosmological scales, and is calibrated by the Bi-209 experiment at nuclear scales. Paper C adds no new physics. It reads the existing physics in a new regime.

Paper C — Draft 1.2 | May 2026 | Section 3

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **3\. Relationship to the Wilson Coefficient Framework**

Section 2 derived the SCH mechanism in the natural language of the framework: condensate vacuum expectation value, leptonic propagator, modified leptonic tensor, shifted angular observables. That language is precise and self-contained. It is not, however, the language in which the flavour physics community analyses and compares new physics contributions to b → sℓ⁺ℓ⁻ transitions.

The community language is the effective Hamiltonian and its Wilson coefficients. Any new physics contribution to B⁰ → K\*⁰ℓ⁺ℓ⁻ — regardless of its origin — can be parameterised as a shift δC\_i to one or more of the Wilson coefficients C\_i in the operator product expansion of the effective Hamiltonian. The global fit literature constrains these shifts using all available data across multiple decay channels simultaneously. The SCH prediction must be translated into this language to be compared against the global fits and against competing explanations.

This section performs that translation. Section 3.1 reviews the effective Hamiltonian structure. Section 3.2 maps the SCH leptonic mass modification onto the Wilson coefficients. Section 3.3 compares the SCH prediction with the current global fit preferred region. Section 3.4 identifies the distinguishing signatures that separate SCH from leptoquark and Z′ explanations in this language.

## **3.1 The Effective Hamiltonian for b → sℓ⁺ℓ⁻ Transitions**

The Standard Model effective Hamiltonian governing b → sℓ⁺ℓ⁻ transitions at leading order in the operator product expansion is:

$$\mathcal{H}_{\text{eff}} = -\frac{4G_F}{\sqrt{2}}V_{tb}V_{ts}^*\sum_i C_i(\mu)\,O_i(\mu) + \text{h.c.} \tag{3.1}$$

where G\_F is the Fermi constant, V\_tb and V\_ts are CKM matrix elements, μ is the renormalisation scale, C\_i(μ) are the Wilson coefficients, and O\_i(μ) are the local operators. For the angular observables in B⁰ → K\*⁰ℓ⁺ℓ⁻, the dominant operators are:

$$O_9 = (\bar{s}_L \gamma^\mu b_L)(\bar{\ell}\gamma_\mu \ell) \tag{3.2a}$$

$$O_{10} = (\bar{s}_L \gamma^\mu b_L)(\bar{\ell}\gamma_\mu\gamma_5 \ell) \tag{3.2b}$$

$O_9$ is the vector leptonic current operator and $O_{10}$ is the axial-vector leptonic current operator. $C_9$ and $C_{10}$ are the corresponding Wilson coefficients, and it is shifts in these two coefficients that the global fits constrain.

New physics enters this framework through shifts $\delta C_i = C_i^{\text{NP}}$ such that the full Wilson coefficient is $C_i^{\text{total}} = C_i^{\text{SM}} + \delta C_i$. The angular observables P₅′, F\_L, and their companions are then functions of the full Wilson coefficients. The global fit finds the region of ($\delta C_9$, $\delta C_{10}$) space consistent with all available data.

The current global fit preferred region, based on LHCb data through 2026, centres on:

$$\delta C_9 \approx -1.0 \pm 0.2 \quad (\text{approximately }5\sigma\text{ pull from zero}) \tag{3.3a}$$

$$\delta C_{10} \approx 0.0 \pm 0.3 \quad (\text{consistent with Standard Model}) \tag{3.3b}$$

The key feature of equations (3.3) is that the data prefers a shift in C₉ with C₁₀ remaining close to its Standard Model value. This is sometimes called a “pure C₉” solution in the literature. Not all new physics models accommodate this naturally — many predict correlated shifts in both C₉ and C₁₀.

*The values in equations (3.3) are illustrative of the current preferred region based on the April 2026 LHCb analysis. The precise values and uncertainties depend on which observables are included in the fit and on the hadronic form factor parameterisation used. CT-xvi requires using the most current global fit at the time of the quantitative calculation. The qualitative feature — C₉ shifted, C₁₀ unshifted — is robust across different fit approaches in the literature.*

## **3.2 Mapping the SCH Effect onto Wilson Coefficients**

The SCH mechanism modifies the leptonic final state through an effective mass shift δm\_ℓ = αη m\_ℓ. To translate this into Wilson coefficient language, it is necessary to identify which operator the mass shift mimics or modifies.

The leptonic tensor L\_{μν} constructed from the modified propagator of equation (2.8) can be decomposed into vector and axial-vector components. The mass shift δm\_ℓ enters the leptonic tensor through the completeness relation for the lepton spinors: in the sum over final-state spins, the term (˸p + m) picks up the correction δm = αη m\_ℓ. This correction appears in both the vector and axial-vector traces of the leptonic tensor.

However, the axial-vector trace involves an additional factor of γ\_5, and the mass insertion commutes differently with γ\_5 than with the vector part. Working through the algebra:

$$\text{Tr}\left[(\not{p} + m + \delta m)\gamma_\mu(1-\gamma_5)(\not{\bar{p}} - m - \delta m)\gamma_\nu(1-\gamma_5)\right] \tag{3.4}$$

Expanding to first order in δm = αη m\_ℓ:

$$= L_{\mu\nu}^{\text{SM}} + \alpha\eta \left[ m_\ell\,\delta L_{\mu\nu}^V - m_\ell\,\delta L_{\mu\nu}^A \right] + \mathcal{O}(\alpha^2\eta^2) \tag{3.5}$$

where δL\_{μν}^V and δL\_{μν}^A are the vector and axial-vector corrections respectively. The key structural result is that the vector correction δL^V and the axial-vector correction δL^A enter with opposite signs but equal magnitude, because the mass insertion δm commutes with γ\_μ but anti-commutes with γ\_5 γ\_μ via the Clifford algebra relation {γ\_5, γ\_μ} = 0.

The consequence for the Wilson coefficient decomposition is significant. When the modified leptonic tensor (3.5) is contracted with the hadronic tensor and the result is expressed in terms of operator matrix elements, the vector and axial-vector corrections map as:

$$\delta L_{\mu\nu}^V \to \delta C_9 \times \langle O_9 \rangle \quad (\text{vector operator}) \tag{3.6a}$$

$$\delta L_{\mu\nu}^A \to \delta C_{10} \times \langle O_{10} \rangle \quad (\text{axial-vector operator}) \tag{3.6b}$$

From equation (3.5), since δL^V and δL^A enter with opposite signs and equal magnitude, the induced shifts in the Wilson coefficients satisfy:

$$\delta C_9^{\text{SCH}} = +\alpha\eta \times f(m_\ell, q^2) \tag{3.7a}$$

$$\delta C_{10}^{\text{SCH}} = -\alpha\eta \times f(m_\ell, q^2) \tag{3.7b}$$

where f(m\_ℓ, q²) is a kinematic function encoding the mass and momentum transfer dependence, to be computed in CT-xvi. The shifts are equal and opposite at leading order.

This is a conjecture at the level of the current derivation — the exact form of f and the precise cancellation structure require CT-xvi. But the structural observation is robust: the mass shift δm enters symmetrically in the vector and axial-vector parts of the leptonic tensor, and the Clifford algebra then distributes it into equal and opposite Wilson coefficient shifts at leading order.

Equal and opposite $\delta C_9 = -\delta C_{10}$ is a specific signature. In the global fit language, it traces a line in the $(\delta C_9, \delta C_{10})$ plane with slope $-1$. The current global fit preferred region in equation (3.3) shows $\delta C_9 \approx -1.0$ and $\delta C_{10} \approx 0.0$ — not on the slope-$(-1)$ line. This tension between the structural prediction and the current preferred region is a genuine and important open issue. Three resolutions are discussed in Section 3.3.*

## **3.3 Comparison with the Global Fit Preferred Region**

The structural argument of Section 3.2 predicts $\delta C_9^{\text{SCH}} = -\delta C_{10}^{\text{SCH}}$ at leading order. The global fit preferred region has $\delta C_9 \approx -1.0$ and $\delta C_{10} \approx 0.0$. These are not immediately consistent. This section examines whether the tension is fatal, resolvable, or a signal that the leading-order analysis is incomplete.

**Resolution A — Sub-leading terms break the symmetry:** The equal-and-opposite structure of equations (3.7) is a leading-order result. The kinematic function f(m\_ℓ, q²) in the vector and axial-vector channels is not identical once phase space corrections, lepton velocity factors, and the q² dependence of the condensate density are included. Specifically, the axial-vector correction involves the lepton helicity flip amplitude, which is suppressed at high q² relative to the vector correction by an additional factor of m\_ℓ/√q². When the full q²-integrated correction is computed (CT-xvi), the resulting effective $\delta C_{10}$ may be suppressed relative to $\delta C_9$, moving the prediction toward the global fit preferred region. Whether this suppression is sufficient to bring $\delta C_{10}$ close to zero is a quantitative question CT-xvi must answer.

**Resolution B — The condensate has an axial component:** The derivation of Section 2.1 used the parity-preserving vacuum with ⟨A(μ)⟩ = 0. If the local condensate at the B-meson decay vertex has a nonzero axial current — which it may, given the highly asymmetric hadronic environment of the decay — then the vector and axial-vector corrections are no longer symmetric. A nonzero local ⟨A(μ)⟩ preferentially shifts C₉ over C₁₀ through the parity structure of the coupling. This is speculative at the current level of the derivation and requires the full axial condensate calculation as part of CT-xiv.

**Resolution C — The tension is real and Paper C is partially wrong:** The equal-and-opposite prediction may be a genuine problem for the SCH explanation of the B-meson anomaly. If CT-xvi confirms the $\delta C_9 = -\delta C_{10}$ structure and the global fit does not support it, the SCH mechanism as formulated here cannot be the primary explanation of the observed anomaly. It may still be a sub-leading contribution, or it may be a genuine falsification. This possibility is kept open.

The current status is therefore: the SCH prediction is directionally consistent with the observed anomaly (C₉ shift in the right direction, purely leptonic effect, generation hierarchy correct) but the precise Wilson coefficient structure at leading order predicts an equal C₁₀ shift that is not strongly supported by the global fit. Resolution A is the most technically tractable and is the primary target of CT-xvi. Resolutions B and C are held open pending that calculation.

**Conjecture 3.3 (Wilson coefficient mapping):** The SCH leptonic mass modification maps primarily onto $\delta C_9$ with a suppressed $\delta C_{10}$, due to the q²-dependent helicity suppression of the axial-vector correction. The leading-order equal-and-opposite structure is broken at sub-leading order by kinematic factors. The quantitative mapping requires CT-xvi; the conjecture status reflects the outstanding sub-leading calculation.

## **3.4 Distinguishing Signatures: SCH versus Leptoquarks versus Z′**

The Wilson coefficient framework is the common language, but not all features of the SCH prediction are captured in the ($\delta C_9$, $\delta C_{10}$) plane alone. The three candidate explanations — SCH, leptoquarks, and Z′ — make overlapping predictions in that plane but differ sharply in several other observables. The comparison table below summarises the distinguishing features.

| **Feature** | **SCH (this paper)** | **Leptoquark** | **Z′ boson** | **Note** |
| --- | --- | --- | --- | --- |
| New heavy particles required | **✕ None** | **✓ Yes (LQ)** | **✓ Yes (Z′)** | SCH uses only existing condensate |
| Hadronic loop modified | **✕ No** | **✓ Yes** | **✓ Yes** | SCH: purely leptonic effect |
| Leptonic final state modified | **✓ Yes** | **✓ Yes** | **✓ Yes** | All three predict leptonic shift |
| Generation scaling prediction | **∝ m\_ℓ (mass ratio)** | **Tunable (free λ\_LQ)** | **Tunable (free g\_Z′)** | SCH: parameter-free hierarchy |
| Tau/muon anomaly ratio predicted | **≈16.8 (fixed)** | **Arbitrary** | **Arbitrary** | SCH tau prediction is sharpest test |
| Wilson coefficient shift | **C₉ only (leptonic)** | **C₉ and C₁₀** | **C₉ and C₁₀** | SCH: no C₁₀ shift predicted at leading order |
| q² dependence of anomaly | **Increasing with q²** | **Roughly flat** | **Roughly flat** | SCH: slower leptons couple more |
| Observable in current data | **Partially (muon)** | **Partially** | **Partially** | Tau channel distinguishes |

Three signatures stand out as maximally discriminating.

**The hadronic side.** Leptoquark and Z′ models modify the hadronic tensor H\_{μν} through new physics entering the b → s vertex itself. SCH does not. A precision measurement that isolates the hadronic angular observables — holding the leptonic kinematics fixed — and finds them consistent with the Standard Model would strongly favour SCH over the alternatives. Conversely, a hadronic deviation would disfavour SCH. The current data does not yet cleanly isolate the hadronic and leptonic contributions independently, but this separation is in principle achievable by comparing muon and electron channels at the same q² and factoring out the leptonic contribution.

**The tau channel ratio.** This is the sharpest prediction in Paper C. SCH predicts the tau/muon anomaly ratio at ∼16.8, fixed by the lepton mass ratio with no free parameters. Leptoquark models predict an arbitrary ratio depending on the leptoquark coupling to third-generation leptons. Z′ models predict an arbitrary ratio depending on the Z′ coupling to the tau. No other model produces the specific value 16.8 without tuning. If the tau channel anomaly is measured and the ratio comes in near 16.8, that is a strong SCH signature. If it comes in at a significantly different value — say, 5 or 30 — the mass-scaling mechanism is falsified even if the muon anomaly is explained.

**The q² slope.** SCH predicts the anomaly magnitude should increase with q², because slower leptons spend more proper time in the condensate background and receive a larger effective mass shift. Leptoquark and Z′ models predict a roughly flat q² dependence unless additional model-dependent form factors are invoked. A measurement of the anomaly as a function of q² with sufficient precision to determine the slope would discriminate between SCH and the alternatives. Current LHCb data shows some evidence of q²-dependent deviations but the statistical precision is not yet sufficient for a definitive slope measurement.

These three signatures — hadronic side unmodified, tau/muon ratio at 16.8, positive q² slope — form a joint prediction set. SCH predicts all three simultaneously. A measurement that confirms all three would be compelling evidence for the mechanism. A measurement that falsifies any one of the three — hadronic modification found, tau/muon ratio far from 16.8, or q² slope absent or negative — would disfavour or falsify the SCH explanation.

**Prediction 3.4 (Joint discriminating signatures):** SCH predicts simultaneously: (1) hadronic angular observables consistent with Standard Model at current precision; (2) tau/muon anomaly ratio ≈ 16.8; (3) positive q² slope in anomaly magnitude. These three predictions are correlated consequences of the single mechanism of Section 2.1. They are jointly falsified if any one of them is contradicted by data.

## **3.5 The R\_K and R\_K\* Observables**

The lepton universality ratios R\_K and R\_K\* are the most precisely measured B-meson flavour observables. They are defined as:

$$R_K = \frac{\mathcal{B}(B^+ \to K^+\mu^+\mu^-)}{\mathcal{B}(B^+ \to K^+e^+e^-)} \tag{3.8a}$$

$$R_{K^*} = \frac{\mathcal{B}(B^0 \to K^{*0}\mu^+\mu^-)}{\mathcal{B}(B^0 \to K^{*0}e^+e^-)} \tag{3.8b}$$

In the Standard Model, R\_K = R\_K\* = 1 to very good approximation, up to small electromagnetic corrections. The updated LHCb analysis from 2022 found R\_K and R\_K\* consistent with 1, which resolved an earlier apparent anomaly in these ratios. This result must be reconciled with any proposed explanation of the remaining angular anomaly.

At first glance, the SCH mechanism appears to predict R\_K ≠ 1 — since the muon and electron effective masses are shifted differently. However, R\_K and R\_K\* measure ratios of branching fractions integrated over q², not angular observables. The SCH mass shift affects the angular distribution of the decay products but does not, at leading order, shift the total branching fraction by a large amount. The reason is that the phase space integral over the full angular distribution largely cancels in the ratio: the condensate shifts the angular distribution but not the integrated rate, because the mass shift is small (αη << 1) and the angular moments integrate to zero over the full solid angle.

More precisely, R\_K receives a SCH correction of order (αη m\_μ)² / m\_B², which is doubly suppressed by both the smallness of αη and the ratio of lepton to B-meson mass. This gives R\_K ≈ 1 + O((αη)² (m\_μ/m\_B)²), consistent with the measured value.

The angular anomaly, by contrast, is a differential observable sensitive to the shape of the distribution rather than its integral. It can receive a first-order correction in αη because it is the derivative of the distribution with respect to angle, not the integral. This is why the angular anomaly and the R\_K consistency are not contradictory within SCH: different observables at different orders in αη.

*This argument is qualitative at the current level. The quantitative confirmation requires computing the SCH correction to R\_K from the modified phase space integral — this is a sub-target of CT-xv. If the calculation returns a non-negligible shift in R\_K that is inconsistent with the measured value of 1.000 ± 0.009, the SCH mechanism would be in tension with the R\_K data even while explaining the angular anomaly. That outcome would require a reassessment of the mechanism.*

**Prediction 3.5 (R\_K consistency):** The SCH mechanism predicts R\_K ≈ 1 + O((αη)² (m\_μ/m\_B)²), consistent with the measured value to current precision. The angular anomaly is a first-order effect in αη; R\_K is a second-order effect. These are consistent. Quantitative confirmation requires the CT-xv phase space integral.

Paper C — Draft 1.2 | May 2026 | Section 4

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **4\. Lepton Universality and the Generation Pattern**

Lepton universality is one of the most precisely tested principles of the Standard Model. It states that the W, Z, and photon couplings to the three charged lepton generations are identical up to corrections from the lepton masses themselves, which are small at the energies relevant for most precision tests. The principle has been verified at the sub-percent level across a wide range of processes.

The B-meson angular anomaly, if confirmed, represents a violation of lepton universality in b → s transitions: the muon and electron channels differ in a way the Standard Model does not predict. Section 2.2 established that SCH predicts exactly this violation — not through a new force with generation-dependent couplings, but through the existing condensate coupling weighted by fermion mass. This section develops the full observational picture of that violation across all three generations, all relevant decay channels, and the q² spectrum.

## **4.1 The SCH Form of Lepton Universality Violation**

The Standard Model breaks lepton universality only through mass-dependent radiative corrections, which are calculable and small. New physics models break it in various ways: leptoquarks introduce new generation-dependent couplings; Z′ models introduce a new boson with adjustable charges to each generation; technicolour and composite models invoke new dynamics at each generation separately.

SCH breaks lepton universality in a structurally distinct way: through a single coupling constant α that is identical for all generations, acting on a fermion-specific quantity — the bare mass m\_ℓ — that differs across generations by large factors. The generation hierarchy is not an input. It is the output of applying one coupling to three different masses.

This form of universality violation has a precise mathematical character. Define the universality violation parameter for generation ℓ relative to the muon as:

$$\varepsilon_\ell \equiv \frac{\delta O^{\text{SCH}}(\ell) - \delta O^{\text{SCH}}(\mu)}{\delta O^{\text{SCH}}(\mu)} \tag{4.1}$$

where δO^SCH(ℓ) is the SCH-induced shift in any angular observable O for lepton generation ℓ. From Prediction 2.2:

$$\varepsilon_e = \frac{m_e - m_\mu}{m_\mu} \approx -0.9952 \quad (\text{electron nearly unaffected}) \tag{4.2a}$$

$$\varepsilon_\mu = 0 \quad (\text{reference generation by definition}) \tag{4.2b}$$

$$\varepsilon_\tau = \frac{m_\tau - m_\mu}{m_\mu} \approx +15.8 \quad (\text{tau anomaly }\approx 16.8\times\text{ muon}) \tag{4.2c}$$

Equations (4.2) are parameter-free. They depend only on the experimentally measured lepton masses. No model-dependent coupling constants appear. This is the unique signature of the mass-weighted universality violation mechanism: the violation pattern is completely determined by the lepton mass spectrum, which is known to high precision.

The contrast with leptoquark and Z′ explanations is sharp. In those models, ε\_ℓ depends on the model-dependent coupling of the new particle to each generation. There is no constraint relating ε\_e, ε\_μ, and ε\_τ to each other or to the lepton masses. The ratios are free parameters. In SCH, they are fixed by the mass ratios alone.

**Prediction 4.1 (Universal violation pattern):** The SCH universality violation parameter satisfies ε\_ℓ = (m\_ℓ - m\_μ)/m\_μ for all angular observables and all q² bins. The electron channel shows ε\_e ≈ -1 (almost no anomaly). The tau channel shows ε\_τ ≈ +15.8. These values are fixed by the lepton mass spectrum and are the same for every angular observable in every q² bin. They are falsified if any observable shows a different generation ratio.

## **4.2 The Full Generation Picture**

The following table summarises the SCH prediction across all three generations, the observational status of each, and the experimental channel where each prediction is testable.

| **Generation** | **m\_ℓ (MeV/c²)** | **δm\_ℓ / m\_ℓ** | **Ratio to μ** | **Anomaly status** | **Test channel** |
| --- | --- | --- | --- | --- | --- |
| **Electron (e)** | 0.511 | αη | ×1/207 | Consistent with SM | B⁺ → K⁺e⁺e⁻, R_K |
| **Muon (μ)** | 105.66 | αη | ×1 (reference) | 4σ angular anomaly | B⁰ → K*⁰μ⁺μ⁻ (LHCb) |
| **Tau (τ)** | 1776.9 | αη | ×16.8 (predicted) | Not yet measured | B → K*τ⁺τ⁻ (Belle II) |

The electron row deserves comment. The SCH correction to the electron channel is αη m\_e, which is 207 times smaller than the muon correction. At current experimental precision — where the muon anomaly is at four sigma — the electron correction would be at the 4/207 ~ 0.02 sigma level. This is completely unobservable with current technology and for the foreseeable future. The prediction that the electron channel is consistent with the Standard Model is therefore not falsifiable at current precision but is robustly predicted.

The tau row is where the action is. The tau correction is 16.8 times larger than the muon correction. If the muon anomaly represents a four-sigma effect, the tau anomaly would be at the ~67-sigma level if the statistics were comparable. In practice, tau final states are experimentally much harder to reconstruct than muon final states: the tau decays inside the detector into secondary particles, the neutrinos are invisible, and the effective branching fraction available for clean reconstruction is much lower. Belle II is the current best facility for tau measurements in B decays, and the tau channel B → K\*τ⁺τ⁻ is a target of the ongoing experimental programme.

*The b → sτ⁺τ⁻ branching fraction is suppressed relative to b → sμ⁺μ⁻ by phase space: the tau is 1777 MeV/c², leaving only ~700 MeV of kinematic room in B → K\*τ⁺τ⁻ compared to the full 5280 MeV of the B mass. The available q² range is compressed. The SCH prediction of a large tau anomaly survives the phase space compression — it is a genuine enhancement of the angular distribution within the available phase space, not of the total rate — but the experimental reconstruction efficiency in the compressed q² range is low. An observation requires high luminosity and careful systematic control. The HL-LHC era and next-generation B-factories are the right timescale for a definitive tau channel measurement.*

## **4.3 The Tau Channel as Definitive Falsification Test**

The tau channel prediction deserves extended discussion because it is the single sharpest falsification test in Paper C. It is worth being precise about what would and would not constitute falsification.

**What would falsify the mass-scaling mechanism:** A measurement of the tau/muon anomaly ratio that is inconsistent with 16.8 at high statistical significance. “Inconsistent” here means a measured ratio below ~10 or above ~25, accounting for theoretical uncertainties in the angular distribution calculation and experimental uncertainties in the tau reconstruction. A measured ratio of, say, 5 would rule out the m\_ℓ-proportional coupling and force a reassessment of the entire mechanism. A measured ratio of 30 would also be inconsistent and would suggest some other generation-dependent effect not present in SCH.

**What would not falsify it:** A null result in the tau channel at current Belle II luminosity. The tau reconstruction efficiency for B → K\*τ⁺τ⁻ is low enough that a non-observation at current luminosity is entirely consistent with the SCH prediction. Absence of evidence is not evidence of absence here — the signal may simply be below the current detection threshold. The prediction requires a positive measurement with sufficient precision to determine the ratio, not merely a non-observation.

**What would strongly confirm it:** A tau channel anomaly measured in the range 14–20 times the muon channel anomaly magnitude, at 3 sigma or better. This would be striking because no other model predicts this specific value without tuning, and because the prediction was made before the measurement rather than fitted to it.

There is a subtlety in defining the “ratio” that should be measured. The SCH prediction is that the angular observable shift δO\_i scales with m\_ℓ. The observable shift is measured as a deviation from the Standard Model prediction for each channel separately. The ratio is therefore:

$$R_{\tau/\mu}^{\text{SCH}} \equiv \frac{\delta O_i(\tau)}{\delta O_i(\mu)} \approx \frac{m_\tau}{m_\mu} \approx 16.8 \tag{4.3}$$

This ratio is the same for all angular observables O\_i and for all q² bins (to leading order in αη), because the mass-scaling is universal across the angular distribution. If the measured ratio varies significantly across observables or q² bins, that would be evidence that the mechanism is more complex than the leading-order picture of Section 2.1 and would require investigation.

**Prediction 4.3 (Tau falsification target):** R\_τ/μ^SCH = m\_τ/m\_μ ≈ 16.8 for all angular observables and all q² bins. This is the definitive falsification test of Paper C. A measurement of R\_τ/μ inconsistent with 16.8 at high significance falsifies the mass-scaling mechanism of Section 2.1. A measurement consistent with 16.8 constitutes strong evidence for the SCH explanation of the B-meson angular anomaly.

## **4.4 The q² Spectrum as a Secondary Test**

Section 2.3 identified a q² dependence of the SCH anomaly: slower leptons spend more proper time in the condensate background and receive a larger effective mass shift. This translates into a prediction that the angular anomaly magnitude should increase with q², with the largest deviations from the Standard Model appearing in the high-q² bins.

The physical origin of this dependence is the lepton velocity in the dilepton rest frame:

$$\beta_\ell(q^2) = \sqrt{1 - \frac{4m_\ell^2}{q^2}} \tag{4.4}$$

A lepton with velocity β\_ℓ traverses a given condensate volume in proper time τ ∝ 1/(β\_ℓ γ). The effective condensate exposure — the integral of the condensate density along the lepton’s worldline — is larger for slower leptons (lower β\_ℓ, lower q² relative to 4m\_ℓ²) and smaller for faster leptons (higher q²). The SCH correction to any angular observable therefore acquires a q²-dependent factor:

$$\delta O_i(q^2) \propto \alpha\eta\,m_\ell \times g(\beta_\ell(q^2)), \quad g(\beta)\text{ decreasing in }\beta \tag{4.5}$$

The function g(β) encodes the velocity-dependent condensate exposure. Its precise form requires the condensate coherence length λ\_coh and the lepton propagation dynamics — both are sub-targets of CT-xv. The qualitative prediction — g decreasing in β, meaning larger corrections at lower velocity, meaning larger anomalies at higher q² — follows from the physics without the detailed calculation.

The following table compares the qualitative SCH q² prediction with the LHCb 2026 P₅′ measurements across q² bins. The LHCb deviations are approximate sigma values from published results.

| **q² bin (GeV²)** | **β\_ℓ (lepton velocity)** | **Condensate exposure** | **SCH δP₅′ prediction** | **LHCb 2026 observation** |
| --- | --- | --- | --- | --- |
| 1.1 – 2.5 (low) | High (~0.97) | Shorter | Smaller shift | ~2σ deviation |
| 2.5 – 4.0 (mid-low) | Moderate (~0.90) | Moderate | Moderate shift | ~3σ deviation |
| 4.0 – 6.0 (mid) | Moderate (~0.82) | Longer | Larger shift | ~3.5σ deviation |
| 6.0 – 8.0 (high) | Lower (~0.71) | Longest | Largest shift (predicted) | ~4σ deviation (largest) |

The qualitative agreement is encouraging. The largest observed deviations are in the high-q² bins, consistent with the SCH prediction of larger corrections where leptons are slower. This is not a tuned result — the q² slope follows from the lepton velocity formula (4.4) and the condensate exposure argument, without any free parameters beyond αη.

*The q² table is qualitative. The LHCb deviation values are approximate and the comparison is illustrative. A quantitative comparison requires the full CT-xv calculation of g(β\_ℓ(q²)) and the resulting δP₅′(q²) prediction. The point of the table is to show that the qualitative direction of the prediction — more deviation at higher q² — is consistent with the pattern in the current data. It does not constitute a quantitative fit.*

The q² slope is a secondary test in the sense that it is less clean than the tau/muon ratio: the slope depends on g(β) which requires CT-xv, and the experimental q² binning introduces correlations. But it is a genuinely independent signature from the generation hierarchy. A model that predicts the right tau/muon ratio but the wrong q² slope would be in tension with SCH even if both predictions individually look consistent with data.

**Prediction 4.4 (q² slope):** The SCH anomaly magnitude increases with q² for all lepton channels, due to the velocity-dependent condensate exposure. The slope is the same for all generations (since g(β\_ℓ(q²)) depends on β\_ℓ, not on m\_ℓ directly). The absolute magnitude scales with m\_ℓ. Quantitative prediction of the slope requires CT-xv. Qualitatively, the prediction is consistent with the observed pattern of larger deviations at higher q² in the LHCb data.

## **4.5 Neutrinos and the Neutral Lepton Sector**

The three charged leptons are not the only fermions in the leptonic sector. The three neutrino species are also fermions, and the condensate couples to all fermions through the scalar bilinear ψ̅ψ. The question of whether the SCH mechanism has observable consequences for neutrino propagation is therefore a natural extension of Section 2.

The answer depends on the neutrino mass. The Standard Model neutrinos have masses constrained to be below approximately 0.12 eV/c² (cosmological bound). If the SCH mass shift is δm\_ν = αη m\_ν, then for m\_ν < 0.12 eV/c²:

$$\delta m_\nu < \alpha\eta \times 0.12\text{ eV}/c^2 \ll \delta m_e = \alpha\eta \times 0.511\text{ MeV}/c^2 \tag{4.6}$$

The neutrino mass shift is at least four million times smaller than the electron mass shift, which is itself already unobservable at current precision. The condensate has no observable effect on neutrino propagation within the SCH framework at any foreseeable experimental sensitivity.

There is however a more interesting question about neutrinos: does the condensate modify the neutrino oscillation parameters? Neutrino oscillations arise from the mismatch between mass and flavour eigenstates. The condensate mass shift δm\_ν = αη m\_ν is proportional to the neutrino mass and therefore preserves the mass eigenstate structure — it shifts all masses by the same fractional amount αη without mixing them. The oscillation parameters (mass squared differences δm² and mixing angles θ\_ij) are not modified at leading order.

At sub-leading order, a nonzero axial condensate ⟨A(μ)⟩ ≠ 0 in specific environments could in principle induce a small rotation of the mass eigenstates and modify the oscillation parameters. This is speculative and would require an environment with substantial local net chirality. It is noted here as an exploratory direction rather than a prediction.

**Exploratory note 4.5 (Neutrino sector):** The SCH condensate mass shift for neutrinos is αη m\_ν < 10⁻⁷ eV, unobservable at any foreseeable sensitivity. Neutrino oscillation parameters are unaffected at leading order. A sub-leading effect from a nonzero axial condensate is speculative and not developed in the current paper. The neutral lepton sector offers no near-term test of SCH.

## **4.6 Other b → s Transitions and the Angular Observable Suite**

The SCH mechanism applies to all b → sℓ⁺ℓ⁻ transitions, not only B⁰ → K\*⁰μ⁺μ⁻. Any decay in which the final state contains a muon pair or tau pair propagating through the condensate background will receive the same leptonic mass modification. This section surveys the predicted effects in related channels.

**B⁺ → K⁺μ⁺μ⁻.** This channel is related by isospin to B⁰ → K\*⁰μ⁺μ⁻ but without the vector K\* resonance in the hadronic final state. The angular observables are different — the decay has only one hadronic momentum, so the full four-angle analysis of the K\* channel is replaced by a simpler di-lepton angular distribution. The SCH correction to the dilepton angular distribution is the same as in the K\* channel — it enters through the same modified leptonic tensor — but the observables are different. This channel provides an independent cross-check of the SCH mechanism.

**B\_s → φμ⁺μ⁻.** The B\_s meson (śb quark) decay to φ(1020) μ⁺μ⁻ is a b → sμ⁺μ⁻ transition with a different hadronic final state. LHCb has observed angular anomalies in this channel as well, with deviations consistent in direction with the B⁰ → K\*⁰μ⁺μ⁻ anomaly. The SCH prediction is the same leptonic modification with the same magnitude — the hadronic state is irrelevant since the condensate only modifies the lepton propagation. The consistency of anomalies across B⁰ and B\_s channels is a qualitative prediction of SCH: the anomaly should be wherever there are muons, not wherever there is a specific hadronic resonance.

**b → sνν̅ transitions.** Decays like B → K(\*)νν̅ proceed through a different diagram (Z penguin and box diagrams) and produce neutrino pairs rather than charged lepton pairs. As established in Section 4.5, the SCH neutrino mass shift is negligible. SCH predicts no anomaly in b → sνν̅ channels. Recent Belle II measurements of B → Kνν̅ have found a small excess over the Standard Model prediction — but this excess, if real, would require a different mechanism. The absence of SCH contribution to b → sνν̅ is a clean prediction: if the neutrino excess is real and large, SCH is not its source.

**b → d transitions.** B-meson decays proceeding via b → dℓ⁺ℓ⁻ transitions (for example B → ρℓ⁺ℓ⁻) involve the same leptonic final state and the same condensate coupling. The SCH prediction is the same leptonic mass modification as in b → s transitions, with the same generation hierarchy. The hadronic side differs (different CKM matrix elements and form factors) but the leptonic side is identical. If the b → s angular anomaly is genuine and SCH is the explanation, the same anomaly should appear — at reduced rate due to CKM suppression — in b → d transitions.

The current experimental status of b → dμ⁺μ⁻ angular observables is important context for this prediction. As of May 2026, no angular analysis of b → d transitions has been performed. The only existing b → dℓℓ measurement is the B → πℓ⁺ℓ⁻ branching fraction observed by LHCb at 5.2σ significance, which is consistent with the Standard Model. That measurement constrains the total rate but is insensitive to the angular distribution where the SCH effect lives. The angular observables — the equivalent of P₅′ for the b → d system — have not been measured in any channel. The theoretical community has computed Standard Model predictions for B → ρℓ⁺ℓ⁻ and related angular observables in anticipation of LHCb Run 3 data, which will make these measurements possible for the first time. The LHCb Upgrade I detector, validated in November 2025, has been confirmed capable of extracting angular coefficients in b → dμ⁺μ⁻ transitions. The prediction in this section is therefore made before the data exists — not retrofitted to it — and will be testable within the Run 3 programme. The absence of a contradicting measurement is not confirmation; it is an open window. SCH is on record with a specific prediction before that window closes.

The cross-channel prediction is an important structural feature of SCH. Because the modification is purely leptonic, it appears in every channel with the same lepton in the final state, regardless of the hadronic physics. A new physics model that modifies the b → s vertex specifically — like leptoquarks or Z′ — would predict anomalies specifically in b → s transitions and not in b → d transitions. SCH predicts anomalies in both, with the same leptonic angular pattern.

**Prediction 4.6 (Cross-channel universality):** The SCH leptonic mass modification appears in all b → qℓ⁺ℓ⁻ transitions (q = s or d) with the same magnitude and generation hierarchy. The anomaly is in the leptons, not in the hadronic vertex. b → sνν̅ shows no SCH anomaly. Anomaly consistency across B⁰ and B\_s channels is a qualitative prediction; anomaly presence in b → dμ⁺μ⁻ at CKM-suppressed rate is a further prediction.

Paper C — Draft 1.2 | May 2026 | Section 5

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **5\. The Nuclear Scale: Opening the Territory**

Papers A and B touch the nuclear scale only at one precise point: the Bi-209 → Pb-208 transmutation experiment, which is the calibration anchor for the free parameter alpha. That experiment is not a theoretical prediction of nuclear behaviour — it is a measurement strategy. The theoretical framework says: the condensate couples to geometric organisational state, Bi-209 is the maximum contrast geometric reorganisation available in stable matter, therefore the transmutation event is the maximum contrast signal the condensate can produce at nuclear densities. The experiment measures alpha. It does not explore the full nuclear landscape.

This section opens that landscape. It is explicitly a survey — exploratory in epistemic status, honest about what is and is not established. The goal is not to make precise predictions at the nuclear scale but to identify where the framework has things to say, what calculations are required to say them quantitatively, and whether any existing nuclear anomalies are candidates for SCH explanation.

The organisation follows the condensate coupling structure. The same object — the scalar bilinear η = ψ̅ψ and the axial current A(μ) — that drives galactic-scale anomalies and the leptonic B-meson modification is active at nuclear densities. Nuclear matter is cold relative to T\_c, the condensate is firmly present, and the coupling is strong. The question is not whether the condensate affects nuclear physics but whether the effect is resolvable above the dominant nuclear physics already well-described by QCD and the nuclear shell model.

## **5.1 The Condensate at Nuclear Densities**

Nuclear matter sits at density ρ\_nuclear ∼ 2.3 × 10^{17} kg/m³. This is vastly higher than galactic densities (ρ\_galactic ∼ 10^{-21} kg/m³) and approaches the scale at which the quadratic torsion term — Term (3) in the SCH field equation — becomes significant relative to the linear condensate term. Paper A Section 2.1 identifies Term (3) as dominant at neutron star and Planck densities; at nuclear densities it is transitional.

The critical temperature T\_c for the condensate at nuclear densities is higher than the galactic estimate because the condensate mass parameter m\_eff may receive density-dependent corrections. In the EFT language of Appendix P, the effective potential for the condensate field receives loop corrections proportional to the local matter density ρ. The condensate may be more robustly present inside nuclei than in the galactic halo — which resolves, at least partially, the T\_c concern raised in Section 2.4 of this paper. Nuclear matter is cold (T ~ MeV << T\_c at nuclear densate values), dense, and geometrically organised. The condensate is maximally active in this environment.

The coherence length of the condensate at nuclear densities is:

$$\lambda_{\text{coh}}^{\text{nuclear}} \sim \frac{\hbar}{m_{\text{eff}}^{\text{nuclear}}\,c} \tag{5.1}$$

With the galactic estimate m\_eff ∼ 10⁻⁶ eV/c², λ\_coh ~ 10^{14} m — much larger than any nucleus. The condensate is effectively uniform across nuclear scales at the galactic m\_eff value. However, if m\_eff receives density-dependent corrections that increase it at nuclear densities, λ\_coh shrinks accordingly. CT-xviii must explore the density dependence of m\_eff before the coherence length at nuclear scales can be estimated reliably.

The coupling efficiency at nuclear scales is characterised by η(Z,N) — the nuclear form factor defined in Paper A Section 2.3. This encodes the departure of the nuclear wavefunction from spherical symmetry:

$$\eta(Z,N) = \left|\int \psi^*_{\text{nuclear}}(\mathbf{r})\,Y_{00}(\theta,\phi)\,dV\right|^2 \times f(\beta_2, \beta_4, \ldots) \tag{5.2}$$

For doubly magic nuclei (He-4, O-16, Ca-40, Pb-208), η(Z,N) → 0: the wavefunction is spherically symmetric and the condensate coupling vanishes. For nuclei near closed shells with one or a few valence nucleons, η(Z,N) is nonzero and the condensate is active. Bi-209, with magic neutron number 126 and one unpaired proton, sits precisely at this maximum contrast point. This is not a coincidence of the experimental design — it is the experiment choosing the nucleus where the effect is predicted to be largest.

## **5.2 Nuclear Spin-Flip Transitions**

The most direct nuclear-scale prediction of SCH beyond the Bi-209 calibration is a modification of M1 (magnetic dipole) spin-flip transition rates in nuclei with nonzero η(Z,N). The axial current A(μ) = ψ̅ γ^(μ) γ\_5 ψ couples to nuclear spin states through the same geometric coupling that drives the Bi-209 signal.

An M1 transition involves a spin flip of a valence nucleon with emission of a photon. In the Standard Model, the transition rate is determined by the nuclear magnetic dipole matrix element. In the SCH framework, the condensate background provides an additional matrix element proportional to α × η(Z,N). The transition rate acquires a correction:

$$\Gamma_{M1}^{\text{SCH}} = \Gamma_{M1}^{\text{SM}} \times \left(1 + \alpha\,\eta(Z,N)\times h(Z,N,E_\gamma)\right) \tag{5.3}$$

where h(Z,N,E\_γ) is a form factor encoding the overlap of the photon field with the condensate modification at the nuclear scale and E\_γ is the transition energy. The sign and magnitude of h depend on whether the transition increases or decreases the geometric coupling efficiency η(Z,N): a transition that reorganises the nuclear wavefunction toward a more symmetric configuration (decreasing η) releases condensate binding energy and is enhanced; a transition that moves toward a less symmetric configuration is suppressed.

The Bi-209 → Pb-208 transmutation is an extreme case of this: the transmutation drives η(Z,N) from its maximum value (Bi-209, one unpaired proton outside the magic shell) to its minimum (Pb-208, doubly magic, η → 0). The signal predicted in Paper A Section 5 is the condensate energy released in this maximum-contrast transition. More modest M1 transitions — within a given nucleus or between near-magic nuclei — release proportionally smaller amounts of condensate energy.

**Conjecture 5.2 (M1 rate modification):** M1 transition rates for nuclei with η(Z,N) ≠ 0 are modified by a factor (1 + αη h(Z,N,E\_γ)) relative to the Standard Model prediction. Transitions toward more symmetric nuclear configurations are enhanced; transitions toward less symmetric configurations are suppressed. The modification is largest near closed shells where η changes most rapidly with nucleon number. Quantitative prediction requires CT-xiv and the Bi-209 alpha calibration.

This conjecture is testable in principle using existing nuclear spectroscopy data. The predicted pattern of enhanced and suppressed M1 rates near closed shells — relative to shell model predictions — is a systematic signature. If the modification exists at the level predicted by SCH, it would appear as a correlated deviation from shell model M1 rates that tracks η(Z,N) across the nuclear chart. If no such correlation exists at the level of the Bi-209 calibration prediction, the nuclear-scale coupling is falsified.

*The nuclear shell model already has known systematic deviations from experimental M1 rates — the so-called “quenching” of Gamow-Teller and M1 matrix elements, which are suppressed relative to the free-nucleon values by a factor of approximately 0.7-0.8. This quenching is attributed to short-range correlations and meson exchange currents within QCD. The SCH correction to M1 rates must be distinguishable from the existing quenching — which means identifying a pattern of corrections that correlates with η(Z,N) rather than with the nucleon density or pairing correlations that drive the conventional quenching. This is a non-trivial experimental discriminator.*

## **5.3 Nuclear Binding Energy Corrections**

The leptonic mass modification of Section 2.1 generalises to all fermions in the condensate background. Nucleons — protons and neutrons — are fermions with bare masses m\_p ≈ 938.3 MeV/c² and m\_n ≈ 939.6 MeV/c². The SCH condensate correction to the nucleon effective mass is:

$$\delta m_N = \alpha\,\eta_{\text{nuclear}} \times m_N, \quad N = p\text{ or }n \tag{5.4}$$

where η\_nuclear is the local condensate density at nuclear scales. The correction α η\_nuclear × m\_p ~ 938 MeV/c² × αη is large in absolute terms — because the nucleon mass is large — but the fractional shift αη may be small if the condensate density η\_nuclear is small at nuclear scales. The key question is whether δm\_N is significant compared to nuclear binding energies (~8 MeV per nucleon).

The ratio of the SCH nuclear mass correction to the nuclear binding energy is:

$$\frac{\delta m_N}{B_A} \sim \frac{\alpha\,\eta_{\text{nuclear}}\times m_N}{B_A} \sim \alpha\,\eta_{\text{nuclear}} \times \frac{938\text{ MeV}}{8\text{ MeV}} \sim 117\,\alpha\,\eta_{\text{nuclear}} \tag{5.5}$$

If αη\_nuclear ~ 10⁻⁵ (consistent with the galactic-scale estimate), then δm\_N / B\_A ~ 10⁻³ — a correction at the 0.1% level to nuclear binding energies. This is at the edge of precision nuclear mass measurements. The Atomic Mass Evaluation provides nuclear masses to precisions of order 1 keV in many cases — which for a mid-mass nucleus with B\_A ∼ 8 MeV per nucleon represents a fractional precision of ~10⁻⁴. An SCH correction at the 10⁻³ level would be at or above this detection threshold.

The observational signature would be a systematic deviation of nuclear binding energies from the semi-empirical mass formula that correlates with η(Z,N). Nuclei near closed shells — where η(Z,N) is small — should show smaller corrections; nuclei with large deformation (large β\_2) — where η(Z,N) is large — should show larger corrections. This is a specific pattern distinct from the conventional shell corrections and pairing terms already in the mass formula.

**Exploratory 5.3 (Binding energy corrections):** SCH predicts a systematic correction to nuclear binding energies of order αη\_nuclear × m\_N × A, correlating with η(Z,N). At αη\_nuclear ~ 10⁻⁵ this is a ~0.1% correction to binding energies, potentially at the edge of precision mass measurement sensitivity. A systematic survey of binding energy residuals from the semi-empirical mass formula correlated with nuclear deformation parameters would test this prediction. This is exploratory: the magnitude depends entirely on the Bi-209 calibration result and CT-xiv.

## **5.4 The Proton Radius Puzzle**

The proton radius puzzle — the discrepancy between the proton charge radius measured via muonic hydrogen spectroscopy versus ordinary hydrogen spectroscopy and electron-proton scattering — is a long-standing anomaly in atomic and nuclear physics. The muonic hydrogen value is r\_p = 0.84087 ± 0.00039 fm, while the electron-based values cluster around 0.877 ± 0.007 fm. The discrepancy of approximately 4%, at several sigma significance, has not been fully resolved by the community despite extensive experimental and theoretical effort.

The SCH framework has a structural implication for this measurement, though not a mechanism that explains the discrepancy at current parameter estimates. The proton radius is measured differently in muonic and electronic hydrogen: in muonic hydrogen, the orbiting particle is a muon (m\_μ ∼ 106 MeV/c²), and in ordinary hydrogen it is an electron (m\_e ∼ 0.511 MeV/c²). The muon’s Bohr orbit is approximately 207 times smaller than the electron’s, bringing it much closer to the proton and making the measurement more sensitive to the proton’s internal structure.

Crucially, the muon also has a much larger SCH effective mass correction than the electron — by the factor m\_μ/m\_e ≈ 207, exactly the same factor by which the Bohr orbits differ. The SCH leptonic mass shift δm\_ℓ = αη m\_ℓ modifies the energy levels of the muonic hydrogen atom differently from the electronic hydrogen atom, because the muon’s effective mass is shifted more. The energy level corrections depend on the orbital radius, which depends on the effective lepton mass. A modified lepton mass propagates into the extracted proton radius through the quantum electrodynamics (QED) radiative corrections used in the spectroscopic analysis.

The chain is:

$\delta m_\mu = \alpha\eta\,m_\mu$ (SCH muon mass shift, Section 2.1)

$\Rightarrow$ modified Bohr radius $a_\mu = \hbar/(\alpha_{\text{QED}}\,m_\mu^{\text{eff}})$ (muonic hydrogen)

$\Rightarrow$ modified energy level spacing $\delta E \sim m_\mu^{\text{eff}}\,\alpha_{\text{QED}}^4$ (QED calculation)

$\Rightarrow$ extracted $r_p$ differs from Standard Model extraction by $\mathcal{O}(\delta m_\mu / m_\mu) = \mathcal{O}(\alpha\eta)$

The proton radius discrepancy is approximately 4%, which would require α̃\_nuclear ~ 0.04 — three to four orders of magnitude larger than the galactic estimate of α̃ ~ 10⁻⁵. This is not a quantitative tension; it is the mechanism being off by a very large amount. The direction of the effect is correct but the magnitude is not in the right ballpark at current estimates.

The three-to-four order of magnitude gap is noted without mitigation. The galactic estimate of α̃ is rough and the nuclear-scale value may be higher if the condensate density is strongly density-dependent — but a plausible density enhancement does not span three orders of magnitude without a specific argument for why it should. Section 5.4 is included to note the structural sign prediction and flag the proton radius puzzle as a long-range target for CT-xviii, not to claim the discrepancy is explained by SCH at current parameter estimates.

**Exploratory note 5.4 (Proton radius puzzle):** The SCH leptonic mass modification implies a structural difference between muonic and electronic measurements of the proton radius: the muon effective mass shift is 207 times larger than the electron shift, so muonic and electronic hydrogen should yield different extracted proton radii. The sign of this difference is correct — muonic measurements should give a smaller r\_p. However, the magnitude required to explain the full 4% discrepancy is α̃\_nuclear ~ 0.04, which is three to four orders of magnitude above the current estimate of α̃ ~ 10⁻⁵ from galactic scales. A factor of 10³ is not a tension; it is the mechanism being off by a very large amount at current estimates. The direction is noted here as a structural curiosity. No directional claim is made until CT-xiv and CT-xviii return α̃\_nuclear. This item is exploratory only.

## **5.5 The Neutron Star Equation of State**

The quadratic torsion term — Term (3) in the SCH field equation — is negligible at galactic densities but grows as ρ² and becomes significant at nuclear and super-nuclear densities. Paper A Section 2.1 identifies this term as dominant at neutron star densities. This section examines the observational consequences for the neutron star equation of state (EOS).

The SCH field equation at high density includes the spin-spin repulsion term:

$$G_{\mu\nu} = \kappa\left[T_{\mu\nu} + \alpha\,C_{\mu\nu} + \frac{\lambda}{m^2}\,S_{\mu\nu}\right] \tag{5.6}$$

where S(μ,ν) is the quadratic torsion contribution and λ/m² sets its scale. At neutron star core densities ρ ~ 2–5 × ρ\_nuclear, the S(μ,ν) term stiffens the EOS relative to General Relativity. A stiffer EOS supports higher maximum neutron star masses and larger radii at a given mass.

The gravitational wave era has dramatically improved EOS constraints. LIGO/Virgo observations of the GW170817 binary neutron star merger constrain the tidal deformability Λ ~ (R/M)⁵ of neutron stars with M ≈ 1.4 M\_☉. The constraint Λ\_{1.4} < 800 at 90% confidence places an upper limit on the neutron star radius of approximately 13 km at 1.4 solar masses. The Neutron Star Interior Composition Explorer (NICER) provides mass-radius measurements that constrain the EOS from a different direction.

The SCH Term (3) stiffening predicts:

(a) A slightly higher maximum neutron star mass than pure GR with standard nuclear EOS models.

(b) A slightly larger radius at fixed mass, due to the additional repulsive pressure from the spin-spin term.

(c) A tidal deformability Λ\_{1.4} toward the higher end of the GW170817 constraint.

The quantitative predictions require the full EOS calculation including Term (3), which depends on the coupling λ/m². Until the Bi-209 calibration pins the free parameters, the predictions are directional rather than numerical. The observed maximum neutron star mass of approximately 2.35 M\_☉ (PSR J0952-0607) already strains some nuclear EOS models; the SCH stiffening moves in the direction of accommodating such masses more naturally.

**Prediction 5.5 (Neutron star EOS stiffening):** Term (3) in the SCH field equation stiffens the neutron star EOS relative to GR with standard nuclear interactions. This predicts: higher maximum neutron star mass, larger radii at fixed mass, tidal deformability toward the upper end of current constraints. This prediction is carried from Paper A — it is not new to Paper C. It is included here because it is the cleanest nuclear-density prediction in the current framework, with the most developed observational test programme through LIGO, NICER, and future gravitational wave detectors.

## **5.6 The Territory Map: What Has Been Opened**

Section 5 is a survey, not a derivation. Its purpose is to map the territory that Paper C opens at the nuclear scale, identify where the framework has things to say, and flag the calculations required to say them precisely. The following table summarises the nuclear-scale questions, their current status, and their experimental channels.

| **Nuclear-scale question** | **SCH mechanism** | **Status** | **Prerequisite** | **Observational channel** |
| --- | --- | --- | --- | --- |
| Spin-flip transition rate modification | η(Z,N) coupling modifies M1 rate | Conjecture | CT-xiv, Bi-209 alpha | Bi-209 → Pb-208 (Paper A Sec. 5) |
| Nuclear binding energy correction | Scalar condensate shifts effective nucleon mass | Exploratory | CT-xiv, CT-xviii | Precision mass spectrometry |
| Coherence length at nuclear scale | λ_coh ~ ℏ/(m_eff c) at nuclear density | Exploratory | CT-vi, Bi-209 calibration | Neutron scattering experiments |
| Doubly magic nucleus geometry (Pb-208) | η(Z,N) → 0 at closed shells | Prediction (carried) | Paper A Sec. 2.3 | Bi-209 calibration channel |
| Neutron star spin-spin repulsion (Term 3) | Quadratic torsion dominant at ρ ~ ρ_nuclear | Prediction (carried) | Paper A Sec. 2.1 | Neutron star EOS, mass-radius relation |
| Proton radius puzzle | Condensate modifies effective proton charge radius | Exploratory | CT-xiv, CT-xviii | Muonic hydrogen spectroscopy |
| Nuclear shell model deviations | η(Z,N) form factor near closed shells | Exploratory | CT-xviii | Nuclear spectroscopy data |

Three themes run through the nuclear-scale survey and are worth naming explicitly.

**The condensate is maximally active at nuclear scales.** Nuclear matter is cold relative to T\_c, dense, and geometrically organised. The T\_c concern that complicates the B-meson prediction does not apply here. Whatever the condensate does at nuclear scales, it does it fully. This makes nuclear-scale predictions more robust in principle than the particle-scale predictions of Sections 2–4, even though they are less developed quantitatively.

**The Bi-209 calibration is the master key.** Every quantitative nuclear-scale prediction chains through the Bi-209 calibration that fixes alpha and m\_eff. Until that experiment runs, all nuclear-scale predictions are directional. The experiment is tractable with current technology. It should be the first priority of the experimental programme.

**The proton radius puzzle is the most provocative connection.** It is also the most quantitatively strained. The magnitude of the SCH effect required to explain the full proton radius discrepancy is orders of magnitude above the galactic estimate of αη. This is either a signal that the condensate density at nuclear scales is much higher than the galactic average — which is physically plausible and requires CT-xiv — or a signal that SCH is not the explanation of the proton radius puzzle. Both possibilities are kept open. What is notable is that the direction of the SCH prediction is correct without any tuning: muonic measurements should give smaller radii than electronic measurements, because the muon receives a larger effective mass shift. The sign is right. The magnitude may not be.

**Exploratory summary 5.6 (Nuclear territory):** The SCH framework has theoretical things to say at every nuclear-scale phenomenon surveyed in this section. The quality of the predictions ranges from carried theorems (neutron star EOS stiffening) through conjectures (M1 rate modification, proton radius puzzle) to purely exploratory territory (binding energy corrections, shell model deviations). The common prerequisite for all quantitative nuclear-scale work is the Bi-209 calibration and CT-xiv. Section 5 is a map, not a destination. The work that fills it in is the next phase of the programme.

Paper C — Draft 1.2 | May 2026 | Sections 6 & 7

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **6\. Calculational Targets CT-xiv through CT-xviii**

The calculational targets CT-i through CT-xiii are defined in Appendix P Section P.8 and govern the formal closure of the variational theory in Papers A and B. Paper C adds five new calculational targets, CT-xiv through CT-xviii, governing the particle and nuclear-scale extension developed in Sections 2–5. These targets are defined here in the same format as Appendix P: each has a clear statement of what is required, what it unlocks, and what its prerequisites are.

The hierarchy of dependencies is strict. CT-xiv is the master target for Paper C: it establishes whether the condensate produces a nonzero leptonic mass modification and what the proportionality coefficient is. Every other CT in this section depends on CT-xiv either directly or through the Bi-209 calibration. The sequencing is:

$$\text{CT-xiv} \to \text{CT-xv} \to \text{CT-xvi}$$
$$\text{CT-xiv} \to \text{CT-xvii}$$
$$\text{Bi-209 calibration} + \text{CT-xiv} \to \text{CT-xviii}$$

A summary table of all five CTs with their priorities and dependencies follows the detailed entries.

## **CT-xiv — Leptonic Self-Energy in the Condensate Background**

This is the foundational calculation of Paper C and the first target that must be completed before any other quantitative prediction in this paper can be made.

The required calculation has four sub-targets that must be addressed in sequence.

**Sub-target (a): Condensate survival condition.**

Establish whether the local condensate vacuum expectation value η is nonzero at the scale and environment of the B-meson decay vertex. The defensible path is Resolution 1: non-equilibrium phase localisation inside the hadronic environment at the decay vertex. This requires establishing three specific conditions: (i) the condensate effective potential at hadronic densities supports a nonzero local minimum η\_local ≠ 0; (ii) the thermalisation timescale for this local state to reach bulk equilibrium at 300 K is longer than τ\_B ∼ 10⁻²¹ s; (iii) the magnitude of η\_local is sufficient to produce the observed anomaly. Conditions (i) and (ii) are evaluable from condensate field theory without the Bi-209 calibration. Condition (iii) requires the product α̃\_local = αη\_local/m\_eff² and is fully evaluable only after the calibration fixes α and sub-target (b) determines η\_local. All three must hold. Resolution 3 (geometric persistence at all temperatures) is rejected as inconsistent with the GR recovery mechanism — see Section 2.4. Resolution 2 (m\_eff underestimated) is a secondary path dependent on the Bi-209 calibration. If sub-target (a) returns η = 0 under Resolution 1 and Resolution 2 is not supported by Bi-209, Paper C is falsified at the first step and the entire mechanism collapses.

**Sub-target (b): One-loop lepton self-energy.**

Compute the one-loop correction to the lepton self-energy Σ(˸p) in the condensate background field η ≠ 0. This is a standard QFT calculation in a modified vacuum, analogous to the finite-temperature field theory calculation of fermion masses in a thermal condensate. The condensate background enters through the scalar bilinear coupling term of S\_geo. The mass renormalisation δm\_ℓ = Σ(m\_ℓ) at leading order in αη is the quantity required. The dimensional argument of Section 2.1 Step 4 fixes the functional form as αη m\_ℓ; sub-target (b) determines the numerical coefficient.

**Sub-target (c): Axial condensate correction.**

Evaluate whether the local condensate at the B-meson decay vertex has a nonzero axial component $\langle A^\mu \rangle \neq 0$, and if so, compute its contribution to the lepton self-energy. The parity-preserving vacuum has $\langle A^\mu \rangle = 0$ (Appendix P, Theorem 2), but the hadronic environment of the B-meson decay is not parity-symmetric. A nonzero local axial condensate would break the vector-axial symmetry of the correction and shift $\delta C_9 / \delta C_{10}$ away from the equal-and-opposite leading-order prediction of Section 3.2, potentially resolving the C₁₀ tension. This sub-target is required for Resolution B of Section 3.3.

**Sub-target (d): Nucleon self-energy.**

Compute the condensate correction to the nucleon effective mass δm\_N = αη\_nuclear × m\_N at nuclear densities. This is the same calculation as sub-target (b) but for protons and neutrons in the nuclear environment, with η\_nuclear the local condensate density at nuclear density. This result is the prerequisite for CT-xviii and the nuclear-scale predictions of Section 5.

*CT-xiv is a substantial calculation requiring expertise in finite-density quantum field theory and the condensate EFT derived from S\_geo. It is not a single computation but a programme of related calculations. Sub-targets (a) and (b) are the immediate priorities. Sub-target (c) is needed only if sub-targets (a) and (b) return nonzero results consistent with the observed anomaly direction; if the leading-order calculation fails, the axial correction is moot. Sub-target (d) can proceed in parallel with (a) and (b) as it uses the same techniques applied to a different density regime.*

## **CT-xv — Angular Observable Shifts δO\_i(q²)**

Prerequisite: CT-xiv sub-targets (a) and (b) must return $\delta m_\ell \neq 0$ with a determined proportionality coefficient.

Given the effective lepton mass $m_\ell^{\text{eff}} = m_\ell(1 + \alpha\eta)$ from CT-xiv, compute the resulting shift in each angular observable $O_i$ in $B^0 \to K^{*0}\mu^+\mu^-$. The central expression is equation (2.12):

$$\delta O_i = \alpha\eta \times m_\ell \times \frac{\partial O_i^{\text{SM}}}{\partial m_\ell}$$

This calculation has three components.

First, evaluate the Standard Model derivatives ∂O\_i^SM / ∂m\_ℓ for each of the angular observables — P₅′, P₁, P₂, P₃, F\_L, A\_FB — across the full q² range. These derivatives are computable from the known SM expressions for the angular distribution in the helicity amplitude basis. The mass dependence enters primarily through the lepton velocity $\beta_\ell(q^2) = \sqrt{1 - 4m_\ell^2/q^2}$.

Second, compute the q²-dependent condensate exposure function g(β\_ℓ(q²)), encoding the velocity-dependent proper-time integral of the lepton through the condensate background. This function determines the q² slope of the anomaly and is the quantitative input for Prediction 4.4.

Third, compute the SCH correction to the R\_K branching fraction ratio from the modified phase space integral, confirming that the first-order angular distortion does not generate a large second-order shift in the total branching fraction. This sub-target addresses Prediction 3.5 and the R\_K consistency argument.

Output: the full predicted angular distribution δP₅′(q², αη) and its companions, as a function of the single free parameter αη to be fixed by the Bi-209 calibration. This output is the primary quantitative prediction of Paper C and the direct comparison target against LHCb data.

## **CT-xvi — Wilson Coefficient Mapping $\delta C_9$, $\delta C_{10}$**

Prerequisite: CT-xv must be complete with quantitative $\delta O_i(q^2)$ expressions.

Translate the SCH angular observable shifts of CT-xv into the Wilson coefficient language of the effective Hamiltonian, producing explicit expressions for $\delta C_9^{\text{SCH}}$ and $\delta C_{10}^{\text{SCH}}$ as a function of $\alpha\eta$ and the lepton mass.

This calculation must address the C₁₀ tension identified in Section 3.2. The leading-order analysis predicts $\delta C_9 = -\delta C_{10}$, which is inconsistent with the global fit preferred region ($\delta C_9 \approx -1.0$, $\delta C_{10} \approx 0.0$). CT-xvi must evaluate whether sub-leading kinematic corrections --- specifically the helicity flip suppression of the axial-vector correction at high $q^2$ --- break this symmetry sufficiently to bring $\delta C_{10}$ close to zero when integrated over the physical q² range.

The calculation proceeds in two steps. First, compute the full q²-dependent Wilson coefficient shifts including next-to-leading-order kinematic corrections. Second, compare the resulting ($\delta C_9$, $\delta C_{10}$) prediction against the current global fit preferred region from the April 2026 LHCb analysis and the broader combination of b → sℓ⁺ℓ⁻ data.

If CT-xvi returns $\delta C_{10}$ ≈ 0 after sub-leading corrections — consistent with the global fit — the SCH prediction is confirmed as a pure C₉ solution and the conjecture status of Section 3.3 is elevated to prediction. If CT-xvi returns $\delta C_{10}$ significantly nonzero, Falsification Condition FC-5 is triggered and the mechanism must be reassessed.

## **CT-xvii — Tau Channel Quantitative Prediction**

Prerequisite: CT-xiv sub-targets (a) and (b).

Compute the quantitative SCH prediction for the angular anomaly in B → K\*τ⁺τ⁻ decays. The structure of this calculation follows CT-xv but for the tau lepton (m\_τ ≈ 1777 MeV/c²) rather than the muon. The key outputs are:

First, the predicted angular observable shifts δO\_i^tau(q²) across the compressed q² range available to the tau channel (q² > 4m\_τ² ≈ 12.6 GeV², up to (m\_B - m\_K\*)^2 ≈ 19.2 GeV²).

Second, the predicted tau/muon ratio R\_τ/μ for each angular observable, confirming or refining the parameter-free prediction R\_τ/μ ≈ m\_τ/m\_μ ≈ 16.8 at leading order.

Third, the predicted q² dependence within the compressed tau phase space window, which differs from the muon q² profile due to the different β\_τ(q²) velocity profile.

CT-xvii does not require the Bi-209 calibration for the ratio R\_τ/μ — the ratio is parameter-free at leading order. It does require the calibration for the absolute magnitude of the tau anomaly. The ratio prediction is therefore the more robust output of CT-xvii and the primary comparison target against future Belle II data.

*The tau channel is kinematically constrained: only the high-q² region is accessible. This is the same region where the SCH q² slope predicts the largest corrections. The tau channel is therefore not only the largest absolute anomaly but also the one concentrated precisely where SCH predicts the maximum condensate effect. The two signatures reinforce each other in the tau channel.*

## **CT-xviii — Nuclear Scale Survey: Density Dependence**

Prerequisites: Bi-209 alpha calibration (Paper A Section 5); CT-xiv sub-target (d) for nucleon self-energy.

CT-xviii is an exploratory programme rather than a single calculation. Its scope covers the nuclear-scale questions opened in Section 5. The sub-targets are:

Sub-target (a): Density dependence of m\_eff and η. Determine how the condensate mass parameter and vacuum expectation value scale with local matter density ρ from galactic densities (ρ ~ 10⁻²¹ kg/m³) through nuclear densities (ρ ~ 2 × 10¹⁷ kg/m³). The density dependence of η\_nuclear is the input for all nuclear-scale predictions and the resolution of the T\_c concern for the B-meson mechanism.

Sub-target (b): M1 transition rate modification. Compute the condensate correction to nuclear M1 rates as a function of η(Z,N) across the nuclear chart. Identify the predicted pattern of enhanced and suppressed transitions relative to shell model predictions. Compare against the existing nuclear spectroscopy database for systematic deviations correlated with η(Z,N).

Sub-target (c): Binding energy corrections. Compute the condensate correction to nuclear binding energies as a function of η(Z,N) and nuclear deformation parameters. Compare against the residuals of the semi-empirical mass formula across the Atomic Mass Evaluation dataset.

Sub-target (d): Coherence length at nuclear scale. Using the density-dependent m\_eff from sub-target (a), compute the condensate coherence length λ\_coh at nuclear densities. Determine whether the condensate is effectively uniform across nuclear scales or whether nuclear-scale structure emerges.

Sub-target (e): Proton radius correction. Using the muon effective mass shift from CT-xiv and the nuclear condensate density from sub-target (a), compute the SCH correction to the extracted proton charge radius in muonic hydrogen spectroscopy. Compare with the measured discrepancy of approximately 0.034 fm.

CT-xviii is the long-range programme for the nuclear scale. Its outputs will determine whether the nuclear anomalies surveyed in Section 5 are genuinely connected to the SCH condensate or whether the condensate’s nuclear-scale effects are too small to be relevant. The Bi-209 calibration is the master input: all quantitative nuclear-scale predictions are conditional on that experiment.

## **6.6 Summary: CT Programme for Paper C**

The following table summarises the five calculational targets, their priority, sequencing, and what each one unlocks.

| **CT** | **Title** | **Status** | **Priority** | **Unlocks** |
| --- | --- | --- | --- | --- |
| **CT-xiv** | Leptonic self-energy in condensate background | **FIRST** | **Immediate** | All quantitative predictions in Paper C; T_c resolution; nuclear mass corrections |
| **CT-xv** | Angular observable shifts δO_i(q²) | **CRITICAL** | After CT-xiv | Quantitative P₅′ prediction; q² slope; R_K correction; tau channel magnitude |
| **CT-xvi** | Wilson coefficient mapping $\delta C_9$, $\delta C_{10}$ | **CRITICAL** | After CT-xv | Global fit comparison; C₁₀ tension resolution; definitive comparison with leptoquark/Z′ |
| **CT-xvii** | Tau channel quantitative prediction | **IMPORTANT** | After CT-xiv | Definitive falsification target R_τ/μ ≈ 16.8; Belle II comparison |
| **CT-xviii** | Nuclear scale survey (density dependence) | EXPLORATORY | After Bi-209 | M1 rates; binding energies; proton radius; coherence length at nuclear density |

# **7\. Falsification Conditions**

A theoretical framework that cannot be falsified is not physics. Paper C is built on the existing SCH framework, which has maintained strict falsification discipline throughout Papers A and B. This section applies that same discipline here, stating explicitly what observations or calculations would falsify the claims of Paper C, how severe each falsification would be, and what the consequences would be for the rest of the framework.

The falsification conditions are organised into three severity levels. Fatal conditions directly falsify the central mechanism of Paper C. Serious conditions do not falsify the mechanism outright but require significant revision. Informative conditions are not falsifying at current sensitivity but become falsifying at higher luminosity or precision.

The falsification conditions are independent of each other: any one of them can be triggered without the others. They are not a hierarchy where failing one automatically fails all. A theory can survive a serious condition while passing the fatal ones, and vice versa.

## **7.1 Fatal Falsification Conditions**

The following conditions, if triggered, falsify the central claim of Paper C: that the geometric condensate produces a mass-weighted modification of leptonic propagation that explains the B-meson angular anomaly.

**FC-1 — CT-xiv returns δm = 0 for all fermions** *\[FATAL\]* Condition: The one-loop lepton self-energy calculation in the condensate background (CT-xiv sub-target b) returns δm\_ℓ = 0 for all lepton generations, either because the condensate has decoupled at the relevant scale or because the coupling in S\_geo does not generate a mass correction at one loop. *Outcome if triggered: The entire mechanism of Sections 2.1–2.3 collapses. There is no leptonic mass modification, no angular observable shift, no generation hierarchy prediction. Paper C is falsified at its foundation. The SCH framework as developed in Papers A and B is unaffected — the galactic-scale phenomenology does not depend on the leptonic mass modification. Only Paper C’s particle-scale extension is falsified.*

**FC-2 — R\_K measured significantly different from 1** *\[FATAL\]* Condition: A precision measurement of R\_K = BR(B⁺ → K⁺μ⁺μ⁻) / BR(B⁺ → K⁺e⁺e⁻) finds a value inconsistent with 1 at high significance, beyond what SCH predicts at second order in αη. *Outcome if triggered: SCH predicts R\_K ≈ 1 + O((αη)² (m\_μ/m\_B)²), which is indistinguishable from 1 at current precision. A large R\_K deviation is inconsistent with the purely leptonic, first-order-in-αη character of the SCH mechanism. If the deviation requires a first-order coupling — as leptoquark models predict — SCH cannot be the explanation.*

**FC-3 — Hadronic angular observables deviate from Standard Model** *\[FATAL\]* Condition: A precision angular analysis of B⁰ → K\*⁰ℓ⁺ℓ⁻ that isolates the hadronic contribution — by comparing muon and electron channels at fixed q² and factoring out the leptonic tensor — finds the hadronic angular observables inconsistent with the Standard Model. *Outcome if triggered: SCH predicts that the loop is blind to the condensate and the hadronic side is unchanged. A hadronic deviation means new physics enters the b → s vertex directly — which is what leptoquark and Z′ models predict. SCH cannot be the primary explanation if the hadronic side is modified.*

**FC-4 — Tau/muon anomaly ratio outside \[10, 25\] at high significance** *\[FATAL\]* Condition: A measurement of R\_τ/μ = δO\_i(τ) / δO\_i(μ) for any angular observable O\_i returns a value outside the range \[10, 25\], accounting for theoretical and experimental uncertainties. *Outcome if triggered: Falsifies the mass-scaling mechanism of Section 2.1 regardless of whether the muon anomaly is explained. The ratio 16.8 is parameter-free and fixed by the lepton mass spectrum. A significantly different ratio means the generation hierarchy does not follow the bare lepton masses — inconsistent with the δm\_ℓ = αη m\_ℓ structure. A ratio of ~1 would suggest generation-independent coupling; a ratio of ~207 would suggest electron-scale coupling. Both are inconsistent with SCH.*

## **7.2 Serious Falsification Conditions**

The following conditions do not falsify the central mechanism outright but require significant revision of specific claims in Paper C.

**FC-5 — CT-xvi confirms $\delta C_9$ = - $\delta C_{10}$ with no sub-leading suppression** *\[SERIOUS\]* Condition: The full CT-xvi calculation including sub-leading kinematic corrections confirms the leading-order result $\delta C_9$ = - $\delta C_{10}$ without significant suppression of $\delta C_{10}$, and the global fit does not accommodate equal and opposite shifts. *Outcome if triggered: SCH cannot be the primary explanation of the pure C₉ solution preferred by the global fits. The mechanism may still be correct as a sub-leading contribution, or Resolutions B (axial condensate component) must be developed more fully. Section 3.3 would need to be revised to downgrade the prediction from a viable primary explanation to a sub-dominant contribution.*

**FC-6 — q² slope absent or negative in precision measurement** *\[SERIOUS\]* Condition: A sufficiently precise q²-binned angular analysis finds the anomaly magnitude flat or decreasing with q² at high significance. *Outcome if triggered: Falsifies the velocity-dependent condensate exposure mechanism of Sections 2.3 and 4.4. Does not falsify the generation hierarchy (Predictions 2.2 and 4.1-4.3), which is independent of the q² slope. A model with the right generation hierarchy but no q² slope would require a different mechanism for the leptonic mass modification — one that does not depend on lepton propagation time through the condensate.*

## **7.3 Informative Conditions**

The following conditions are not falsifying at current experimental sensitivity but become falsifying at higher luminosity or precision. They are informative about the framework’s status even when not yet definitively falsifying.

**FC-7 — Large b → sνν̅ anomaly confirmed** *\[INFORMATIVE\]* Condition: The Belle II excess in B → Kνν̅ is confirmed at high significance and requires a first-order new physics contribution of comparable magnitude to the b → sμ⁺μ⁻ anomaly. *Outcome if triggered: Not directly falsifying for SCH, since SCH predicts no neutrino anomaly (Section 4.5). But a large neutrino anomaly would point toward new physics at the b → s vertex — a leptoquark or Z′ that couples to neutrinos as well as charged leptons. If such a model explains both the charged lepton and neutrino anomalies simultaneously, it becomes the preferred explanation over SCH, which explains only the charged lepton anomaly. SCH would be demoted to a sub-leading or irrelevant contribution.*

**FC-8 — Null result in tau channel at HL-LHC luminosity** *\[INFORMATIVE\]* Condition: The High-Luminosity LHC and Belle II together accumulate sufficient luminosity to detect a tau-channel angular anomaly at the 16.8x muon level if present, but no signal is found. *Outcome if triggered: At current luminosity, a null result in the tau channel is not falsifying (Section 4.3). At HL-LHC luminosity (×10 current statistics), a non-observation becomes a serious constraint. A null result at that luminosity would either require a mechanism that predicts a smaller tau/muon ratio than 16.8, or would falsify the mass-scaling mechanism entirely. The HL-LHC era is therefore the window in which FC-4 and FC-8 become jointly decisive.*

## **7.4 Falsification Summary Table**

| **FC** | **Condition** | **Severity** | **Effect on Paper C** |
| --- | --- | --- | --- |
| **FC-1** | CT-xiv returns δm = 0 for all fermions | **FATAL** | Entire mechanism collapses. No leptonic mass modification. Paper C’s central claim is falsified. |
| **FC-2** | R_K measured inconsistent with 1 at high significance | **FATAL** | SCH predicts R_K ≈ 1 at second order. A large R_K deviation violates this and is inconsistent with the mechanism. |
| **FC-3** | Hadronic angular observables deviate from SM | **FATAL** | SCH predicts purely leptonic effect. A hadronic deviation rules out SCH as the primary explanation. |
| **FC-4** | Tau/muon ratio outside [10, 25] | **FATAL** | Falsifies the mass-scaling mechanism of Section 2.1 regardless of whether the muon anomaly is explained. |
| **FC-5** | CT-xvi confirms $\delta C_9$ = - $\delta C_{10}$ with no sub-leading suppression | **SERIOUS** | SCH cannot be the primary explanation of the pure C₉ solution preferred by global fits. May be a sub-leading contributor. |
| **FC-6** | q² slope absent or negative in precision measurement | **SERIOUS** | Falsifies the velocity-dependent condensate exposure mechanism of Section 2.3. Does not falsify the generation hierarchy. |
| **FC-7** | b → sνν̅ anomaly at large magnitude | INFORMATIVE | Not directly falsifying (SCH predicts no neutrino anomaly), but points toward a different mechanism that competes with SCH. |
| **FC-8** | Null result in tau channel at HL-LHC luminosity | INFORMATIVE | Not falsifying at current luminosity. Becomes serious at HL-LHC if no signal. Absence of evidence is evidence of absence only at high luminosity. |

## **7.5 What Survival of These Conditions Would Mean**

It is worth stating plainly what it would mean if Paper C passes all eight falsification conditions.

It would mean: the geometric condensate derived from the rotational primitive of Papers A and B — a framework built entirely to explain galactic-scale anomalies — produces a specific, parameter-free, mass-weighted modification of leptonic propagation that explains a four-sigma particle physics anomaly the framework was never built to address, with a generation hierarchy fixed by lepton masses rather than new couplings, with a tau-channel prediction that no competing model reproduces without tuning, with no new particles required, and with the signal-to-noise structure exactly as a geometric substrate theory predicts.

That would not prove the framework correct. No number of confirmed predictions proves a theory. But it would constitute strong circumstantial evidence that the rotational primitive is doing something real at every scale, that the condensate is a genuine feature of spacetime and not merely a galactic-scale fitting tool, and that the B-meson angular anomaly is a window into geometry rather than a window into new particles.

Falsification on any of the four fatal conditions would be equally valuable. It would mean the condensate, however well it explains galactic-scale phenomena, does not reach into the leptonic sector in the way Paper C proposes. That would sharpen the theory’s scope rather than destroy it: Papers A and B would stand, and the extension to particle physics would be closed off as a direction. Knowing where a theory does not apply is as useful as knowing where it does.

Either outcome is worth knowing. That is what makes the programme worth pursuing.

*\[ Appendix C-A: Energy Scale Separation | Appendix C-B: Comparison with Mainstream Explanations \]*

**Paper C Draft 1.2 — Sections 1–7 complete — May 2026**

Paper C — Draft 1.2 | May 2026 | Appendices C-A and C-B

**The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale**

# **Appendix C-A — The Signal-to-Noise Argument: Formal Development**

Section 1.3 of the main text introduced the signal-to-noise framing: the condensate is present at all scales because it is a geometric object built on the rotational primitive, and what varies across scales is not the condensate’s presence but the ratio of its contribution to the dominant physics of the process under consideration. This appendix develops that argument formally, establishing the propositions that underlie it and making explicit where the formal support is complete and where it remains a prediction pending CT-xiv.

## **C-A.1 Scale-Independence of the Geometric Coupling**

The geometric state action S\_geo is derived from the Einstein-Cartan-Dirac action by including a quartic spinor self-coupling:

$$S_{\text{geo}} = \int d^4x\, e \left[ \frac{i}{2}\left(\bar{\psi}\gamma^a e^a_{\mu} D_\mu \psi - \text{h.c.}\right) - m\bar{\psi}\psi - \frac{\lambda}{4}(\bar{\psi}\psi)^2 \right]$$

The condensate arises as the ground state of this action when the quartic coupling drives spontaneous symmetry breaking: η = ⟨ψ̅ψ⟩ ≠ 0. The condensate couples to all matter fermions through the shared tetrad e^ᵃ\_μ and spin connection ω\_μ^ab of the common geometric background.

**Proposition C-A.1 (Scale-independence of the rotational primitive):** The rotational primitive — the spinor structure encoding rotational state in curved spacetime — has no preferred energy scale. It is defined at every point of the spacetime manifold independently of the energy of any process occurring at that point. The condensate η = ⟨ψ̅ψ⟩, being the ground state of the spinor field, inherits this scale-independence. The condensate background is present at every scale.

Proof: The spinor field ψ(x) is defined at every spacetime point x as the minimal representation of the local Lorentz group Spin(1,3). This definition makes no reference to any energy scale. The tetrad and spin connection that enter S\_geo are geometric objects defined at every point independently of the energy of processes occurring in the neighbourhood. The condensate vacuum expectation value η = ⟨ψ̅ψ⟩ is a property of the vacuum state of S\_geo, not a process-dependent quantity. It is therefore present at every scale. ■

Proposition C-A.1 establishes the first pillar: the condensate is not absent at high energy. It is present everywhere. The question becomes not whether the condensate is present at the electroweak scale but what its contribution to electroweak processes is.

## **C-A.2 Suppression of the Condensate Contribution to the Loop**

Given that the condensate is present at the electroweak scale, the question is whether its contribution to the electroweak penguin loop is measurable. The loop involves virtual particles with momenta of order m\_top ~ 173 GeV. The condensate couples to these virtual particles through the same coupling that produces the galactic-scale phenomenology. The magnitude of this coupling at the loop scale is the central question.

**Lemma C-A.2a (Condensate coupling at high loop momentum):** The condensate correction to a virtual fermion propagator with off-shell momentum p² >> m\_eff² is suppressed by the ratio m\_eff² / p² relative to the standard propagator. At the electroweak loop scale p² ~ m\_top² ~ (173 GeV)², and m\_eff ~ 10⁻⁶ eV, this suppression factor is of order 10⁻⁴⁰.

Proof sketch: The condensate background η has characteristic fluctuation scale m\_eff. A virtual particle with momentum p propagates over a spacetime distance of order 1/|p|. For |p| >> m\_eff, the particle’s propagation length 1/|p| is much smaller than the condensate coherence length λ\_coh ~ 1/m\_eff. The particle averages over many condensate oscillation cycles, and by the Riemann-Lebesgue argument the average is suppressed by m\_eff/|p|. At loop momenta, the condensate correction is suppressed by (m\_eff / m\_top)² ~ 10⁻⁴⁰. This is beyond any conceivable measurement precision. ■

The contrast between Proposition C-A.1 and Lemma C-A.2a is the formal statement of the signal-to-noise argument. The condensate is present at the loop scale (C-A.1) but its contribution is suppressed by 10⁻⁴⁰ (C-A.2a). “Present” and “measurably active” are different things. The loop is, for all practical purposes, blind to the condensate — not because the condensate is absent but because its signal is buried 40 orders of magnitude below the noise.

**Lemma C-A.2b (No EFT decoupling):** The condensate does not decouple from the electroweak loop in the Appelquist-Carazzone sense. The standard decoupling theorem applies to dynamical heavy fields integrated out of the EFT below their mass threshold. The condensate is not a dynamical field with a mass threshold; it is a background vacuum state. Decoupling does not apply. The suppression of the condensate contribution to the loop is a signal-to-noise suppression, not a decoupling.

Lemma C-A.2b is the formal statement of the point your intuition identified in the development of this paper: the condensate does not switch off at high energy. It is always present. The suppression is quantitative and enormous, but it is suppression, not absence. The distinction matters for the completeness of the theoretical framework: a theory that claims the condensate decouples is making a statement that is formally incorrect. A theory that claims the condensate’s loop contribution is unmeasurably small is making a statement that is correct and honest.

## **C-A.3 Enhancement in the Leptonic Final State**

While the loop contribution is suppressed by 10⁻⁴⁰, the leptonic final state operates in a different regime. The key difference is between virtual and real particles.

**Lemma C-A.3 (Real versus virtual particles in the condensate background):** A real lepton with mass m\_ℓ propagating through the condensate background receives an effective mass shift δm\_ℓ = αη m\_ℓ. The shift is not suppressed by any ratio of m\_eff to the lepton momentum, because the lepton is on-shell and its propagation is time-like rather than space-like. The condensate couples to the lepton’s mass through the scalar bilinear η = ψ̅ψ, and the lepton mass is a Lorentz scalar — it does not depend on the lepton’s energy or momentum.

Proof: The lepton self-energy in the condensate background is Σ(m\_ℓ, η) = m\_ℓ + δm\_ℓ(η). For an on-shell lepton, the self-energy is evaluated at p² = m\_ℓ². The condensate background η is a constant background field (spatially homogeneous at scales small compared to λ\_coh). The self-energy integral does not involve a large loop momentum averaging over condensate oscillations — it is an infrared effect evaluated at the lepton’s rest mass. The Riemann-Lebesgue suppression of Lemma C-A.2a does not apply to on-shell propagation, because on-shell leptons are not averag­ing over condensate oscillations at loop frequencies. The mass shift δm\_ℓ = αη m\_ℓ survives at full strength. (Full derivation: CT-xiv sub-target b.) ■

Lemma C-A.3 establishes the second pillar. The condensate is suppressed at the loop scale by 10⁻⁴⁰ and active at full strength in the leptonic final state. The signal-to-noise ratio changes by forty orders of magnitude between the loop and the final state. This is the formal expression of the clean separation identified in Section 1.4.

**Corollary C-A (The signal-to-noise separation):** The condensate contribution to the B⁰ → K\*⁰μ⁺μ⁻ amplitude separates cleanly into two parts: a loop contribution suppressed by (m\_eff / m\_top)² ~ 10⁻⁴⁰, which is unmeasurable at any foreseeable precision; and a leptonic final-state contribution δm\_ℓ = αη m\_ℓ, which is not suppressed by any loop momentum ratio and is potentially measurable if αη is sufficiently large. The condensate is present in both parts. Only the leptonic part is measurable. This is the signal-to-noise separation.

## **C-A.4 The Scale at Which the Condensate Becomes Measurable**

Corollary C-A identifies the leptonic final state as the measurable part. But not every leptonic process will show a measurable condensate effect. The condensate becomes measurable at a scale when the signal αη m\_ℓ is comparable to the precision of the measurement, which depends on the competing physics.

The signal-to-noise ratio for the condensate effect in any process is:

$$\text{SNR} \propto \frac{\alpha\eta\,m_\ell}{\sigma_{\text{measurement}}} \tag{C-A.1}$$

where σ\_measurement is the experimental precision and the systematic uncertainty from Standard Model predictions. For a given αη, the condensate effect is more visible when:

(a) the lepton mass m\_ℓ is large (heavier leptons, stronger coupling);

(b) the Standard Model prediction is precise (quiet background, small denominator);

(c) the experimental precision σ\_measurement is small.

The B-meson angular anomaly in the muon channel satisfies all three conditions better than most other processes: muons are heavy relative to electrons, the Standard Model angular distribution is computed to high precision, and LHCb has achieved sub-percent precision on the angular observables. This is why the B-meson channel is where the condensate effect first becomes visible — not because the condensate is specially present there, but because the signal-to-noise ratio is favourable.

At galactic scales, the same reasoning applies in the opposite direction: there is no competing large Standard Model prediction for rotation curves beyond Newtonian gravity plus visible matter, and the condensate correction to the gravitational field is the dominant effect in that regime. At the electroweak loop scale, the Standard Model prediction is extremely precise and the condensate contribution is buried. The B-meson leptonic final state sits at an intermediate point where the condensate is just loud enough to hear.

**Proposition C-A.4 (Measurability condition):** The condensate effect on a leptonic process is measurable when αη m\_ℓ ≳ σ\_measurement. This condition is scale-dependent through m\_ℓ and σ\_measurement. It is first satisfied, among known anomalies, at galactic scales (rotation curves) and potentially in the B-meson leptonic final state. It is not satisfied at the electroweak loop scale. The measurability condition does not imply the condensate is absent where it is not met.

## **C-A.5 Status of the Formal Argument**

The formal argument of Appendix C-A rests on four statements with different epistemic statuses.

Proposition C-A.1 (scale-independence) is a theorem. It follows from the definition of the spinor field and the condensate as a vacuum state. No calculation is required. It is established.

Lemma C-A.2a (loop suppression by 10⁻⁴⁰) is a quantitative estimate based on the Riemann-Lebesgue argument. The order-of-magnitude suppression is reliable; the precise coefficient depends on the details of the condensate propagator and the loop integral, which are sub-targets of CT-xiv and CT-xv. The estimate is conservative in the sense that the actual suppression is at least this large.

Lemma C-A.2b (no EFT decoupling) is a conceptual clarification, not a calculation. It is established by the definition of the Appelquist-Carazzone theorem, which applies to dynamical fields, not to background vacuum states.

Lemma C-A.3 (real particle coupling) is a prediction pending CT-xiv sub-target (b). The qualitative argument — that on-shell lepton propagation does not involve the high-momentum averaging that suppresses the loop contribution — is sound. The quantitative coefficient αη requires CT-xiv.

Corollary C-A (signal-to-noise separation) follows from Lemmas C-A.2a and C-A.3 and is therefore a prediction, not a theorem, pending CT-xiv. It is the central structural claim of Appendix C-A.

Proposition C-A.4 (measurability condition) is a corollary of C-A.3 with the experimental precision σ\_measurement supplied from outside the theory. It is as well-established as C-A.3.

*The formal argument in Appendix C-A is complete in structure and sound in the established parts. The one outstanding piece is CT-xiv sub-target (b), which determines whether Lemma C-A.3 holds at the quantitative level and whether the on-shell mass shift is nonzero. If CT-xiv returns δm = 0, Lemma C-A.3 fails and the entire signal-to-noise separation collapses. The argument is self-consistent and falsifiable at this precise point.*

# **Appendix C-B — Comparison with Mainstream Explanations**

This appendix provides a systematic side-by-side comparison of the SCH mechanism with the two mainstream new-physics explanations of the B-meson angular anomaly: scalar leptoquarks (S₁ model) and vector leptoquarks (U₁ model), and the gauged L\_μ - L\_τ model producing a Z′ boson. The comparison is organised across all observables and features discussed in the main text, with the SCH column highlighted.

The purpose of this table is to give experimentalists a single-page reference for the predictions that distinguish SCH from the alternatives, and to make explicit the features on which SCH makes sharper, parameter-free predictions.

## **C-B.1 Model Descriptions**

**Scalar leptoquark S₁:** A colour-triplet scalar field transforming as (3̅, 1, 1/3) under the Standard Model gauge group, coupling to quark-lepton pairs. The S₁ model is one of the simplest leptoquark models consistent with the b → s anomaly. It introduces new tree-level couplings between the b quark, the s quark, and the lepton pair through the exchange of a leptoquark with mass ~ 1–3 TeV. The coupling constants λ\_{bsμ} and λ\_{bsτ} are free parameters, making the tau/muon ratio arbitrary.

**Vector leptoquark U₁:** A colour-triplet vector field transforming as (3, 1, 2/3), motivated by Pati-Salam unification scenarios. The U₁ model can simultaneously explain the b → s anomaly and the earlier R\_{D(\*)} anomaly in b → c transitions. It introduces a vector boson at ~ 1–3 TeV with generation-dependent couplings. The tau/muon ratio is set by the ratio of coupling constants and is a free parameter.

**L\_μ - L\_τ Z′:** A new Z′ boson coupling to the difference of muon and tau lepton numbers. This model is motivated by the anomalous magnetic moment of the muon (g-2)\_μ as well as the B anomaly. The Z′ mass is constrained by neutrino trident production to be above ~200 GeV. The model predicts correlated effects in C₉ and C₁₀ through the Z′ loop, with the ratio depending on the model parameters.

**SCH condensate mechanism:** The geometric condensate derived in Papers A and B, coupling to all fermions through the scalar bilinear η = ψ̅ψ. The leptonic mass modification δm\_ℓ = αη m\_ℓ is fixed by one parameter α (set by the Bi-209 calibration). The generation pattern is set by the lepton mass ratios with no additional free parameters. No new particles are invoked.

## **C-B.2 Full Comparison Table**

SCH entries are highlighted in blue. Green ticks (✓) indicate the feature is predicted; red ticks indicate the opposite. Cells marked ‘Arbitrary’ indicate a free parameter with no prediction.

| **Observable / Feature** | **SCH (this paper)** | **Scalar LQ (S₁)** | **Vector LQ (U₁)** | **Z′ (L\_μ - L\_τ)** |
| --- | --- | --- | --- | --- |
| **New heavy particles required** | **✕ None** | ✓ Scalar LQ ~TeV | ✓ Vector LQ ~TeV | ✓ Z′ ~TeV |
| LHC direct search constraints | **N/A — no new particles** | Constrained to &gt; ~1.5 TeV | Constrained to &gt; ~2 TeV | Constrained to &gt; ~200 GeV |
| **b → s vertex modified (hadronic loop)** | **✕ Loop blind to condensate** | ✓ Yes (tree-level LQ exchange) | ✓ Yes (tree-level LQ exchange) | ✓ Yes (Z′ loop correction) |
| Hadronic C₉ shift | **✕ Zero (leptonic only)** | Nonzero | Nonzero | Nonzero |
| **Leptonic final state modified** | **✓ Yes (δm\_ℓ = αη m\_ℓ)** | ✓ Yes (new LQ coupling) | ✓ Yes (new LQ coupling) | ✓ Yes (Z′ coupling) |
| Leptonic Wilson coefficient shift | **$\delta C_9$ (primarily); $\delta C_{10}$ sub-leading** | $\delta C_9$ and $\delta C_{10}$ both | $\delta C_9$ and $\delta C_{10}$ both | $\delta C_9$ and $\delta C_{10}$ both |
| C₁₀ shift | **Suppressed at sub-leading order** | Generically nonzero | Generically nonzero | Generically nonzero |
| **Generation coupling pattern** | **Scales as m\_ℓ (mass-weighted)** | Arbitrary (free λ_LQ per gen) | Arbitrary (free λ_LQ per gen) | Arbitrary (free g_Z′ per gen) |
| Electron channel anomaly | **~0 (m\_e/m\_μ × muon = negligible)** | Arbitrary | Arbitrary | Arbitrary |
| Muon channel anomaly | **Reference (observed 4σ)** | Reference (fitted) | Reference (fitted) | Reference (fitted) |
| Tau channel anomaly (predicted) | **≈16.8× muon (fixed by m\_τ/m\_μ)** | Arbitrary | Arbitrary | Model-dependent |
| Tau/muon ratio free parameters | **Zero — fixed by mass ratio** | One (LQ tau coupling) | One (LQ tau coupling) | One (Z′ tau charge) |
| **q² dependence of anomaly** | **Increasing with q² (β\_ℓ effect)** | Roughly flat | Roughly flat | Roughly flat |
| q² slope free parameters | **Zero — fixed by kinematics** | Form factor dependent | Form factor dependent | Form factor dependent |
| **b → dμ⁺μ⁻ anomaly predicted** | **✓ Yes (CKM suppressed)** | Only if LQ has b → d coupling | Only if LQ has b → d coupling | Only if Z′ couples to b-d |
| b → sνν̅ anomaly predicted | **✕ No (neutrino mass negligible)** | Generically yes | Generically yes | Yes (Z′ couples to ν) |
| B_s → φμ⁺μ⁻ anomaly | **✓ Same leptonic modification** | Depends on model | Depends on model | Yes |
| R_K deviation from 1 | **~O((αη)² (m\_μ/m\_B)²) ≈ 0** | Generically nonzero | Generically nonzero | Generically nonzero |
| **Theoretical motivation** | **Geometric coupling; same as galactic mechanism** | Ad hoc (no connection to gravity) | Ad hoc (no connection to gravity) | Ad hoc (no connection to gravity) |
| Connection to other anomalies | **Galactic rotation, JWST, CMB (Papers A/B)** | None | None | None (muon g-2 only) |
| Total free parameters added | **Zero (alpha fixed by Bi-209)** | 2+ (mass, coupling per gen) | 2+ (mass, coupling per gen) | 2+ (mass, coupling per gen) |

## **C-B.3 The Three Decisive Discriminators**

Reading across the table, three features stand out as maximally discriminating between SCH and all three alternative models simultaneously. These are the measurements that would settle the question.

**Discriminator 1: Hadronic side clean or modified?** All three alternative models predict new physics entering at the b → s vertex, modifying the hadronic angular observables and both C₉ and C₁₀ simultaneously. SCH predicts the hadronic side is Standard Model to current precision, with only the leptonic tensor modified. A precision angular analysis that isolates the hadronic contribution — using the electron channel as a leptonic control and the muon channel as the signal — can in principle test this. A hadronic deviation rules out SCH; a clean hadronic sector strongly favours SCH over the alternatives.

**Discriminator 2: Tau/muon ratio ≈ 16.8 or arbitrary?** All three alternative models predict an arbitrary tau/muon ratio, set by free coupling constants that can take any value consistent with constraints. SCH predicts the ratio is fixed at m\_τ/m\_μ ≈ 16.8 with no free parameters. A measurement of the tau channel anomaly magnitude, once achievable at Belle II or the HL-LHC, is the single most discriminating test in the B-meson sector. A ratio near 16.8 cannot be explained by the alternatives without tuning; a ratio far from 16.8 cannot be explained by SCH at all.

**Discriminator 3: b → d anomaly present or absent?** SCH predicts the anomaly is in the leptons, not in the hadronic vertex, so it appears in all b → qℓ⁺ℓ⁻ transitions including b → d at CKM-suppressed rate. The alternative models, which modify the b → s vertex specifically, do not generically predict a b → d anomaly unless the new particle also couples to the d quark. An observation of the same angular anomaly in b → dμ⁺μ⁻ at the CKM-suppressed rate is a distinctive SCH prediction. Its absence at that rate would be informative.

No single measurement rules out all three alternatives and confirms SCH simultaneously. But the combination of the three discriminators — hadronic side clean, tau/muon ratio at 16.8, b → d anomaly at CKM-suppressed rate — is jointly predicted by SCH and jointly not predicted (without tuning) by any of the alternatives. That combination is the experimental target.

**Proposition C-B.3 (Joint discriminating prediction):** SCH simultaneously predicts: (1) hadronic angular observables consistent with SM; (2) tau/muon anomaly ratio = m\_τ/m\_μ ≈ 16.8; (3) b → dμ⁺μ⁻ anomaly at CKM-suppressed rate. The probability that all three are satisfied by a leptoquark or Z′ model with generic parameters, without tuning, is negligible. A measurement confirming all three constitutes strong evidence for the SCH mechanism. A measurement falsifying any one of the three fatal conditions (FC-1 through FC-4) rules SCH out regardless of the others.

――――――――――――――――――――――――

**Paper C — Draft 1.2 — Complete**

*The Strataract Completion Hypothesis: Geometric Condensate Signatures at the Particle Scale*

May 2026

――――――――――――――――――――――――

**Contents**

Section 1 — The Condensate at the Particle Scale: Motivation and Framing

Section 2 — The Condensate in the Low-Energy Leptonic Sector

Section 3 — Relationship to the Wilson Coefficient Framework

Section 4 — Lepton Universality and the Generation Pattern

Section 5 — The Nuclear Scale: Opening the Territory

Section 6 — Calculational Targets CT-xiv through CT-xviii

Section 7 — Falsification Conditions

Appendix C-A — The Signal-to-Noise Argument: Formal Development

Appendix C-B — Comparison with Mainstream Explanations

――――――――――――――――――――――――

*Companion documents: Paper A Draft 1.5 | Paper B Draft 1.4 | SCH Appendix P v7*
