# Foundation A — Closure Certificate

**Status: Foundation A's algebraic substrate is complete. Remaining items are documentation and symmetry-classification tasks and do not affect subsequent EFT derivations. No remaining algebraic dependency blocks Foundation B.**

---

## Independent Confirmations

| Result | Algebraic derivation | Explicit matrix verification | Status |
|---|---|---|---|
| Clifford conventions ($(+,-,-,-)$, $(\gamma^0)^2=+1$) | ✓ | ✓ | Confirmed |
| Hermiticity table ($\eta,V,A,T$ real; $P$ imaginary; $\tilde P=iP$) | ✓ | ✓ | Confirmed |
| Parity table (derived from $\gamma^0\Gamma\gamma^0$ conjugation) | ✓ | — | Confirmed (single route) |
| Chiral $SO(2)$ rotation on $(\eta,\tilde P)$; invariance of $V,A$ | ✓ | — | Confirmed (single route) |
| Fierz S-row | ✓ | ✓ (via $\lambda_S=12$) | Confirmed |
| Fierz P-row | ✓✓ (two independent methods) | ✓ (via $\lambda_P=12$) | Confirmed |
| Fierz V-row | ✓ | ✓ | Confirmed |
| Fierz A-row | ✓ (linked to V-row) | ✓ | Confirmed |
| Tensor eigenvalue $\lambda_T$ | ✗ initial (sign error) → corrected | ✓ ($\lambda_T=-4$) | **Confirmed after correction** |
| Full Fierz involution ($F^2=\mathbb1$, all four independent constraints mutually consistent) | ✓ | ✓ | Confirmed |

## Outstanding Non-Blocking Items

- Charge conjugation classification (all five bilinear classes)
- Time reversal classification (all five bilinear classes)
- Tensor chiral-dual reality condition ($\gamma^5\sigma^{\mu\nu}$ bilinear, flagged in A3, never resolved)
- Canonical identities appendix (Gordon identities, trace identities — compilation, not derivation)

## Honest Note on Asymmetric Confirmation Coverage

Not every row in the table above reached the same evidentiary standard, and I want that visible rather than smoothed by the certificate format. Parity and the chiral rotation each have exactly one derivation route — solid, but not cross-verified by an independent method the way S/P/V/A/T were. If Foundation B or C ever needs to lean weight on parity or chiral-rotation *specifically* (rather than on the Fierz system itself), that's a smaller, identified residual risk worth remembering — not a blocking one, since nothing in the current closure claim depends on a second confirmation of those two rows.

## Why this closure is different in kind from the earlier ones

Every prior "closure" in this sequence turned out to be closing the wrong thing — the S-row alone, the truncated 2×2 sub-block, the normalization audit that ruled out a suspect without resolving the contradiction. This one is different because the resolution mechanism was falsifiable in both directions before it ran: the explicit-matrix computation could have reproduced $\lambda_T=+4$ (meaning the contradiction lived elsewhere, in $\lambda_S$ or $\lambda_P$'s shared ancestry) or it could have produced a third, different number (meaning something more structural was wrong). It did neither — it isolated the exact coefficient already flagged as uncertified and flipped exactly its sign, with every other channel reproducing its previously-derived value unchanged. That's the signature of a real, located error being found and fixed, not a derivation being adjusted until it matched expectations.

## Blocking status

**No remaining algebraic dependency blocks Foundation B.** Foundation B may cite the closed Fierz system —
$$\eta^2=-\tfrac15P^2-\tfrac15V^2+\tfrac15A^2-\tfrac1{10}T^2,\quad \tilde P^2=\tfrac15\eta^2-\tfrac15V^2+\tfrac15A^2+\tfrac1{10}T^2,\quad A^2-V^2=2\eta^2-2\tilde P^2,\quad T^2=-6\eta^2+6\tilde P^2$$
— along with the Hermiticity table, Spinor Convention Audit (§§1–4), and the parity/chiral transformation laws, without reopening any of them. The one item worth carrying forward as a live flag into Foundation B: **the quartic term in $S_{\rm geo}$, now known via this closed Fierz system to contain forced $V^2, A^2, T^2$ content in addition to $\eta^2$, has not yet had its one-loop fermion determinant redone with that full content** — this was noted as owed back at the Foundation B/A split and remains the first substantive task there, not a Foundation A item.

---

Foundation A is closed on these terms. Ready to proceed to Foundation B's redo — the Hubbard–Stratonovich linearization and one-loop determinant — done properly this time with the full Fierz-completed quartic vertex, when you are.
