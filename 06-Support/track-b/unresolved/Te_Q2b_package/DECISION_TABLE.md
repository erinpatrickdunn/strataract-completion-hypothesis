# Q2b-3 Decision Table

| Gate | Question | Result |
|---|---|---|
| 1 | SOC-capable Te potential validated? | **YES** — generated via the legitimate PSLibrary recipe; confirmed by two independent checks (Dirac-relativistic calculation with explicit *j*-dependent atomic splitting in the generation log; `relativistic="full"` in the file's own UPF header metadata). Transferability beyond the internal atomic test not independently verified. |
| 2 | Zero-strain structure/SCF validated? | **NOT REACHED** — no working QE execution environment obtained in this pass. |
| 3 | $\Delta(0)$ reproduced/assessed? | **NOT REACHED** |
| 4 | H4/H5 tracked unambiguously? | **NOT REACHED** (extraction script written and ready; not run against real data) |
| 5 | $D_\Delta$ calculated? | **NOT REACHED** |
| 6 | $D_\Delta$ converged? | **NOT REACHED** |
| 7 | $D_\Delta = 0$ or $\neq 0$? | **NOT REACHED** |
| 8 | Does this advance or kill the Term-3 branch? | **NEITHER** — the physics question remains exactly as open as before this pass; what changed is that it is now fully packaged and executable elsewhere without re-deriving any of the reasoning, structure, boundary condition, or pseudopotential. |
| 9 | What is the single next physical calculation? | Execute this package (`README.md`, "How to run") on a Quantum ESPRESSO installation not subject to the two environment-specific blockers documented under "Known execution environment issues." Gate 2 (the zero-strain benchmark) is the mandatory first step and must pass before any strain point is trusted. |

## What this pass did and did not accomplish

**Did:** froze the complete physics specification into a portable, versioned,
reproducible package — 26 real QE input files (not templates or examples —
exact, ready-to-run inputs with computed strained lattice parameters),
two working analysis scripts (band identification with explicit ambiguity
detection; derivative fitting with convergence and clamped/relaxed
cross-checks), a fully-documented and independently-validated
pseudopotential with checksummed provenance, and a precise, honest account
of exactly which environment-specific obstacles blocked execution here —
so the next attempt does not have to rediscover any of them.

**Did not:** obtain a number. $D_\Delta$ remains **not yet
measured/calculated** — not zero, not nonzero, not "probably" anything.
No physics conclusion should be drawn from this pass in either direction.
