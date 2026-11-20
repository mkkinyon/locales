# Project A — bounded ordinary diameter / localic composition rank
## Independent-referee reconciliation · 20 November 2026

**Canonical theorem note:** [Stone-locale clique overlap and composition rank](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md). **Auditing provenance:** [archive](project-a/audits/2026-11-20/BOUNDED_DIAMETER_RANK/README.md).

This reconciliation was written **after** receiving the independent blind referee's report and separate mathematical addendum, and after comparing both with the internal adversarial audit. The referee did **not** see the internal audit before submitting the independent report.

## 1. Verdict and scope

The independent referee's principal verdict was **accept the main mathematical assertions, subject to modest explanatory additions**. No fatal errors were found in the finite-rectangular lemma, exact diameter-three and diameter-two Stone chains, unbounded-rank point-clique example, or **repaired** nonassociative gadget and attachment. The referee independently ran the finite symbolic support-state test, which supports but does not prove the rank formulas.

The addendum supplied a decisive improvement to the clique-completion theorem:
\[
\boxed{r_{\exists}(H_n)=r_{\forall}(H_n)=n+2.}
\]
It also proved a general point-clique overlap theorem, formulated in terms of the diameter of the graph of **nonzero localic intersections** of spatial component supports. These are **referee-origin** results, not statements in the original candidate packet.

## 2. Claim-by-claim disposition

| Claim | Internal audit | External blind referee | Current consolidated status |
|---|---|---|---|
| Finite-rectangular composition; finite distributivity; overtness | Positive | Verified independently | Accepted, classical Loc and **finite** joins |
| Original Stone chain, ordinary diameter ≤3, rank 3n+4 | Positive | Verified | Accepted, all bracketings agree |
| Modified chain, ordinary diameter ≤2, rank 2n+4 | Positive | Verified | Accepted, all bracketings agree |
| Point-generated clique completion; ordinary diameter ≤1, unbounded rank | Positive, broad bounds only | Verified, sharpened | **Exact rank n+2**, referee addendum |
| All-bracketing point-clique overlap upper/lower lemma | Not submitted | Referee addendum | Accepted after separate internal check |
| Repaired connected Stone gadget nonassociative | Positive with explicit repair | Verified | Accepted, sixfold **upper** bound only |
| Gadget attached to chain; unbounded rank, bounded ordinary diameter | Positive | Verified | Accepted; ordinary diameter sharpened to **8** |
| Older *unmodified* Stone gadget exact six-step claim | Explicitly NOT accepted | Not adopted in corrected packet | Remains unverified; no silent reinstatement |

For the attached relation F_n the verified bounds are
\[
2n+4\le r_{\exists}(F_n)\le3\max(2n+4,6).
\]
No equality formula for r_exists(F_n) is known from this audit, and no value of r_all(F_n) is claimed. The referee noted the attached ordinary component has diameter **exactly 8**, improving the internal packet's ≤9.

## 3. Central localic typing and reasoning safeguards

**Rectangular composition.** The actual pullback of A×B and C×E is A×(B∧C)×E, whose projection to A×E is an **open surjection** when B∧C≠0 in classical Loc. This is **not** arbitrary base-change stability of a locale-surjection. The finite-rectangular subalgebra is associative; unrestricted relation composition need not be.

**Finite, not arbitrary, joins.** Every expansion in the chain and clique arguments is a **finite** join. A point can be excluded from that join by checking each finitely many primitive chain summands. No assertion is made that arbitrary image-defined relations distribute over infinite joins.

**Point-generated clique ≠ support product.** The ordinary clique on a component E_i is P_i=[E_i×E_i] and satisfies P_i≤U_i×U_i, U_i=[E_i]. Full equality is **not** assumed. The referee's all-bracketing induction uses only the **spatial one-point-legged** rectangles {x}×U_i and U_j×{y}, not a possibly nonspatial product U_i×U_j.

**Unstable graph images.** In the repaired nonassociative gadget, the verified statement is Q×{*}≤D_*², obtained by taking the **specific closed point slice** of the actual composability pullback before imaging. The stronger and unnecessary claim Q×X≤D_*² does not follow merely from the pointwise enumeration ℕ→Q. The old unmodified six-step proof attempted precisely such an unjustified enlargement.

**Nonassociativity witness.** For A=D_*∘D_*, the third-order bracketings differ on {b}×{*}: D_*∘A contains it and A∘D_* misses it, by the pullbacks Q∧I≠0 and ℕ×_Y I=0, respectively. The repair adds one ordinary singleton edge q_0↔i_0, connecting the graph without destroying this witness. The ordinary graph now has diameter at most six; every sixfold bracketing is full by ordinary paths and the **spatial ambient square**, not by a product-of-spatial-sublocales argument.

**Lax image.** The collapsing retraction to the chain respects relation composition only in the lax direction image(R∘S)≤image(R)∘image(S); this is enough for the attached-family lower bound.

## 4. The referee's new clique theorem and its meaning

For ordinary graph components E_0,…,E_{n+1}, let U_j=[E_j] and P_j=[E_j×E_j]. Then
\[
U_j\wedge U_{j+1}\ne0,\qquad U_j\wedge U_\ell=0\quad(|j-\ell|\ge2).
\]
The overlaps are **pointless**; the ordinary graph is a disjoint union of cliques. The referee's all-tree induction proves each k-factor clique word contains every point edge between components at overlap-graph distance at most k−1. The private endpoints a_0,b_n force at least n+2 factors, and spatiality of G_n² makes n+2 sufficient for **every** bracketing.

The referee's generalization applies to a **finite family of spatial supports** covering the ambient ordinary points and a spatial ambient square: if the overlap graph has diameter d, then d+1 factors always suffice; private points at diameter-realizing vertices force exact rank d+1.

**Neither theorem asserts all intermediate bracketings are equal as sublocales.** It does prove they have a common completion threshold.

## 5. New deductions AFTER the referee addendum

These deductions are included and proved in the canonical theorem note but **were not submitted for blind review**.

1. **Finite graph realization.** For each edge of any finite connected graph Λ, allocate a clopen Cantor block whose rational/irrational spatial sublocales belong to the two endpoint components; add private vertex points. The resulting clique relation has overlap graph Λ and exact rank diam(Λ)+1.
2. **Exact ordinary-point filtration.** For every bracketing W_k in this clique relation, the point pairs are exactly those between ordinary components at overlap-graph distance ≤k−1. Hence all bracketings of a fixed length have identical ordinary points and identical spatializations, even though their full localic values might differ.

The first is a short Stone-locale application of the referee's theorem; the second follows from the same all-bracketing induction plus finite-expansion support constraints. Both remain **internally checked post-audit extensions** rather than referee-certified theorems.

## 6. Open frontier and exclusions

**Next research question (deferred until after consolidation):** For the point-generated clique relations of §5, do all parenthesizations at a fixed length yield the same **localic sublocale**, not merely the same point set? Initial smallest test: the two threefold bracketings for an overlap path on 3 or 4 vertices. If they differ, the associator lies entirely in an ordinary-point-invisible part.

Other remaining problems: exact completion ranks of the repaired gadget and of the attached family; generalizations without spatial ambient square or with infinitely many component supports; constructive applicability of the nonzero-middle-rectangle lemma. In particular **no claim is made** that the original unmodified six-step gadget has been fully repaired or blind-refereed. No literature originality/priority assessment was undertaken.

## 7. Preservation protocol

The submitted **blind** packet, original independent report, referee addendum and **separate internal** adversarial audit remain distinct. This canonical record does not overwrite or retroactively reinterpret the raw reports. The original report first obtained clique bounds n+2≤r≤2n+2; the addendum subsequently upgraded them to the **exact** n+2. The result is recorded as referee-origin.

This consolidation is the preferred current reference for the bounded-ordinary-diameter program. Earlier informal chat estimates and the initial six-step unmodified gadget draft are historical and are not mathematical dependencies.
