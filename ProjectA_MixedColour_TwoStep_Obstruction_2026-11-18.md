# Project A — a closed-support obstruction to mixed-colour two-step composition

**18 November 2026. New proof candidate; internal adversarial audit completed, not yet externally audited.** This note follows the independently audited conditional cross-gap formula and global generic-square inclusion. It isolates a mild **segment-confinement** hypothesis on the actual fences which was implicit in the proposed subdivision construction, but was not among the abstract hypotheses of the preceding audit packets. Consequently the negative result below is conditional on this extra hypothesis; it must not be attributed to the external referee.

## 1. Notation and additional geometric hypothesis

Retain the compact height-one pospace `P=[0,1]`, upper locale `X`, patch map `p`, component equivalence sublocale `H=H_G=[E_G]`, its image-based square `T=H∘H`, the quotient's generic fibre `G`, and the disjoint upper-open gap mediators `U_P,U_Q`. The finite fences are `P_n` from `f(a_n)∈K` to `a_n∈M` and `Q_n` from `b_n∈M` to `g(b_n)∈L`, where `K<M<L` and both endpoint sequences are dense in `M`. Strict edges in the `n`th pair of fences have patch-coordinate lengths `<1/n`.

Use the following additional, explicitly **geometric** condition:

> **(SC), segment confinement:** `V(P_n)⊂[f(a_n),a_n]` and `V(Q_n)⊂[b_n,g(b_n)]` for every `n`.

It is compatible with the original suggested construction: subdivide each endpoint interval monotonically into an even number of sufficiently short segments; choose interior vertices in the dense complement of `K∪M∪L` and of the previously used countable set, retaining their order along the real line. The fence *order* alternates minimum/maximum independently of the geometric ordering of its vertices. Nevertheless a full coordinate-model audit, including the previously stated strong forcing condition, is still a separate task.

The argument only needs a weaker *separated cofinal subsequence* condition: there exist numbers `r<s` and unbounded index sets `I_P,I_Q⊂ℕ` such that `V(P_n)⊂[0,r]` for `n∈I_P` and `V(Q_m)⊂[s,1]` for `m∈I_Q`, and for **each** nonempty relatively compact mediator-open interval `V` and each `N`, some index `n∈I_P`, `n>N`, has a **minimal** vertex in `V` (and likewise for `I_Q`). Condition (SC), density of the endpoints in the left and right relatively open pieces of `M`, and the shrinking mesh imply this condition.

## 2. A localic separation lemma requiring no image-base-change law

**Lemma 1 (closed mediator obstruction).** Let `Y` be a locale, `H≤Y×Y` any localic relation, and `A,B,C_-,C_+≤Y` closed sublocales. Write `F=C_-∧C_+`. Suppose

\[
H\wedge(A\times Y)\le A\times C_-,\qquad
H\wedge(Y\times B)\le C_+\times B,\qquad
H\wedge(A\times F)=0.\tag{1}
\]

Then

\[
\boxed{(H\circ H)\wedge(A\times B)=0}.\tag{2}
\]

**Proof.** In `Y³`, form the actual composable-pair sublocale `Z=π₁₂⁻¹(H)∧π₂₃⁻¹(H)`. On the inverse image of the **closed** outer rectangle `A×B`, the first two hypotheses force the middle coordinate into `C_-∧C_+=F`. The third makes that restricted triple zero. Thus the outer projection `π₁₃|_Z` has zero inverse image of the closed sublocale `A×B`. Since the inverse image of its complementary **open** sublocale is consequently top, `π₁₃|_Z` factors through that open complement. Its localic image `H∘H` is therefore disjoint from `A×B`. No equality of an image's restriction with the image of a restriction, no preservation of images under a closed pullback, and no associativity of localic composition is used. ∎

**Lemma 2 (closed restriction of a point-generated relation).** If `H=[R]` is the join of its ordinary point-pair sublocales and `A≤Y` is closed, then `H∧(A×Y)` is the join of the point-pair sublocales of `R∩(A×Y)`. In particular, if all ordinary `R`-pairs whose first coordinate lies in `A` have second coordinate in a closed `C`, then `H∧(A×Y)≤A×C`.

**Proof.** Open and closed complementary sublocales are complemented elements of the distributive sublocale lattice. Meet with such an element preserves arbitrary joins: for a complement `c'` of `c`, the map `x↦x∧c` is left adjoint to `z↦z∨c'` for `z≤c`. Apply this to `c=A×Y`, then to each ordinary point-pair. The reversed-coordinate statement is identical. ∎

## 3. A finite overlap of opposite one-sided lower supports

Choose `r<s` strictly between the two selected endpoint regions of `M`. Define the patch-compact order ideals

\[
C_-:=\downarrow[0,r],\qquad C_+:=\downarrow[s,1],\qquad F=C_-\cap C_+.\tag{3}
\]

The order on the compact Hausdorff patch space is closed, so downward images of these compact sets are patch-closed lower sets, hence closed sublocales of the upper locale `X`.

**Lemma 3 (finite early overlap).** `F` is a finite lower set consisting entirely of vertices of the finitely many fences with index at most some `N=N(r,s)`.

**Proof.** Put `δ=s-r>0`. For `z∈F` there are `y_-≤r` and `y_+≥s` with `z≤y_-` and `z≤y_+`. If `z≤r`, the second comparison is strict and has Euclidean length at least `δ`. If `z≥s`, the first comparison is strict with length at least `δ`. If `r<z<s`, both comparisons are strict and at least one has length `≥δ/2`. By the `<1/n` edge bound, such a `z` belongs to a fence of index `n<2/δ`. There are finitely many such fence vertices. No singleton component can contribute. ∎

## 4. Lower-closed Cantor supports selected by colour and endpoint region

Select two relatively open, nonempty portions `M^-`, `M^+` of the middle Cantor set such that `sup M^-<r<s<inf M^+`. Choose only high-index `P_n` with `a_n∈M^-`, and only high-index `Q_m` with `b_m∈M^+`. Under (SC) every selected `P_n` lies in `[0,r]`, and every selected `Q_m` lies in `[s,1]`. The two selected index sets are infinite and unbounded because their endpoint sequences are dense in `M`.

In each fixed relatively compact Euclidean open subinterval of `U_P`, there are selected **minimal** vertices of arbitrarily high permitted `P_n` (the even vertices remain within twice the shrinking mesh of every point traversed by the fence). The analogous statement holds for `Q_m` and `U_Q`. Thus the permitted minimal vertices form countable dense subsets `A_P^{\mathrm{min}}⊂U_P`, `A_Q^{\mathrm{min}}⊂U_Q`.

**Lemma 4 (selected lower Cantors).** There are nonempty compact perfect Cantor sets `D_P⊂U_P`, `D_Q⊂U_Q` such that

1. `D_P∩E` consists only of permitted minimal vertices from selected high-index `P_n`, and is dense in `D_P`;
2. `D_Q∩E` consists only of permitted minimal vertices from selected high-index `Q_m`, and is dense in `D_Q`;
3. `D_P,D_Q` are patch-closed **lower** sets, hence closed sublocales of `X` as well as compact closed sublocales of the patch locale.

**Proof.** Fix a compact nondegenerate interval `I` within the mediator, enumerate the forbidden vertex set `B=E\setminus A_α^{\mathrm{min}}={b_1,b_2,…}`, and let `A=A_α^{\mathrm{min}}∩\operatorname{int}I`, which is dense in `I`. Build a binary tree of nondegenerate compact intervals `I_s` with disjoint siblings and diameters tending to zero. At each node retain a distinguished `A`-anchor in one child **in the interiors of all its subsequent descendants along that branch**, and select a fresh `A`-anchor in the other child. Arrange the `k`th-level intervals to avoid `b_1,…,b_k`. This is feasible because every current interval contains arbitrarily many `A` points, and `A∩B=∅`; the finitely many forbidden points can always be avoided when shrinking. Every node has an anchor that persists in the limit `D=⋂_k⋃_{|s|=k}I_s`, so `D∩A` is dense in `D`; no point of `B` lies in `D`. Binary splitting and the shrinking diameters make `D` a perfect Cantor set. Every point is now either a permitted *minimal* fence vertex or a singleton-comparability point. Each has no strict predecessor; hence `D` is a lower set. Repeat for the other colour. ∎

For every ordinary component-equivalent pair `(x,y)∈E_G`, the membership `x∈D_P` forces either `y=x` or `x` to be one of the permitted `P_n` vertices, in which case `y∈P_n⊂[0,r]`. Likewise `y∈D_Q` forces the first coordinate into `[s,1]`. Lemma 2 therefore gives

\[
H\wedge(D_P\times X)\le D_P\times C_-,\qquad
H\wedge(X\times D_Q)\le C_+\times D_Q.\tag{4}
\]

All points of `F` belong to early nontrivial components, whereas `D_P∩E` consists only of vertices of selected late `P_n`, and its remaining points are singleton components. Thus there are **no** ordinary `E_G` pairs in `D_P×F`. Because this rectangle is closed, Lemma 2 gives

\[
H\wedge(D_P\times F)=0.\tag{5}
\]

Lemmas 1–3 yield the sharp two-step vanishing

\[
\boxed{T\wedge(D_P\times D_Q)=0\quad\text{in }X^2.}\tag{6}
\]

## 5. A nonzero generic product within the vanishing rectangle

Let `Λ_E=p⁻¹(G)` be the patch cofinite-tail fibre established in the previous conditional theorem notes, defined as the meet of patch-open complements of patch-closed sets meeting `E` finitely. Let `Z=D_P×D_Q` in the **patch** square, and let `B(Z)` be its nonzero least dense sublocale. If `C⊂P` is patch closed with `C∩E` finite, then `C∩D_P` (and `C∩D_Q`) is nowhere dense: a nonempty relatively open portion of either perfect Cantor contains infinitely many selected vertices. Consequently the relatively open sets `Z∩((P\setminus C)×P)` and `Z∩(P×(P\setminus C))` are dense in `Z`, and `B(Z)` lies in all these opens. Hence

\[
0\ne\mathcal B(D_P\times D_Q)
\le(\Lambda_E\wedge U_P)\times(\Lambda_E\wedge U_Q)
=(p\times p)^{-1}(G_P^*\times G_Q^*).\tag{7}
\]

Since the pullback of the closed upper-localic rectangle `D_P×D_Q` along `p×p` is exactly that patch-closed rectangle, (6) gives

\[
\mathcal B(D_P\times D_Q)\wedge(p\times p)^{-1}(T)=0.\tag{8}
\]

**Proposition 5 (negative mixed-colour two-step test, under (SC)).** Subject to the previously audited conditional finite-fence hypotheses **and** segment confinement (SC),

\[
\boxed{G_P^*\times G_Q^*\not\le H_G\circ H_G=T.}\tag{MC2-}
\]

Moreover the audited restricted cross-gap result places that same generic block in `T∘T`, so on this block four steps are sufficient and two steps are not. In particular `T` and `T∘T` are distinct localic subrelations of `X×X`. The inequality is witnessed by `B(D_P×D_Q)` after patch pullback.

## 6. Internal adversarial checklist and remaining scope

- **Ordinary versus localic pairs.** We did *not* infer (6) from the absence of ordinary two-edge paths. The crucial extra inputs are the **closed lower** endpoint Cantors, the complemented-closed restriction Lemma 2, and the closed mediator overlap `F`.
- **Image base change.** Lemma 1 proves that the entire composable-pair locale factors through the **open complement** of `D_P×D_Q`, before image factorization. It does *not* assert that a localic image commutes with arbitrary closed restriction; this is essential because the patch counit is not proper.
- **Finite overlap.** The overlap `F` need not be empty. It is a finite union of early fence vertices, removed from both selected Cantor traces. This avoids requiring a uniform mesh bound on the entire fence family.
- **No assumption of associativity.** The proof uses exactly `T=H∘H` and separately the previously established fixed-bracketing `T∘T` inclusion.
- **Geometric dependence.** The new (SC) condition is not a logical consequence of the abstract audit hypotheses. A fence that takes a long detour away from the segment joining its endpoints could defeat this particular separation argument even though its individual edges are small. It suffices to verify (SC), or merely the separated cofinal subsequences in §1, for the concrete realization.
- **Audit status.** The independent referee has *not* seen Proposition 5 or the construction of the two specialized closed lower Cantor supports. The internal adversarial audit below found no fatal gap, but this is **not** equivalent to independent verification.

## 7. Internal adversarial audit (18 November 2026)

**Provisional verdict: survives internal audit as a conditional proof candidate.** No fatal inference was found in (1)–(8), assuming the explicitly stated compact-pospace, quotient-fibre, and selected-fence confinement hypotheses. The following are the decisive checks and limitations.

1. **Closed restriction really preserves point generation.** The sublocale lattice is a distributive coframe, and open and closed sublocales associated with one locale open are complementary. For a complemented element `c`, the map `x↦x∧c` is a *left* adjoint on the interval below `c` and therefore preserves arbitrary joins. Hence `H=[R]` restricts to `A×X` as the join of exactly those original point pairs with first coordinate in `A`. The source for the coframe/complement fact is J. Picado and A. Pultr, *Localic maps constructed from open and closed parts*, §1.3 (https://www.mat.uc.pt/preprints/ps/p1616.pdf). **This argument would fail for an arbitrary noncomplemented sublocale**; closedness is essential.
2. **Two-step composition does not invoke unstable image base change.** Pull back the closed outer rectangle to the composable-pair sublocale *before* its image. Lemma 1 shows that this pullback is zero, so the actual span map factors through the open complement. Localic image factorization then puts `T` in that open complement. We do **not** infer that the image of a closed restriction equals the closed restriction of an image.
3. **Finite mediator overlap uses height one.** If a common predecessor belongs to both one-sided downsets, some strict edge must bridge at least half the Euclidean separation. Height one makes this a *single* edge, and the `<1/n` mesh bounds its component index. With longer strict chains the finite-overlap conclusion would require a different hypothesis.
4. **The Cantor supports require a stronger construction than just choosing perfect sets away from a countable set.** The persistent-anchor binary tree above explicitly ensures the permitted minimal vertices remain dense *in the resulting closed Cantor sets* while all other fence vertices are avoided. Their lower-closedness follows from the height-one minimal/singleton point classification, not from any assertion that arbitrary patch closures of lower sets remain lower.
5. **The Booleanization witness is nonzero and correctly typed.** For every patch-closed cutoff meeting `E` finitely, its trace on each selected Cantor is nowhere dense; hence the least dense sublocale of their patch product lies in both cofinite-tail coordinate inverse images. The rectangle `D_P×D_Q` is simultaneously closed in the upper square, and its patch inverse image is itself. Thus (7) and (8) really contradict `G_P^*×G_Q^*≤T`.
6. **Geometric conclusion remains conditional.** Segment confinement is not forced by merely requiring small individual edges and gap traversal: a very long polygonal detour with very short edges is possible. For the intended monotone subdivision realization, (SC) is natural and can be imposed explicitly. The full realization and the strong closed-saturation forcing lemma remain to be checked in a single coordinate model.

**What to do next:** Verify the segment-confined coordinate model from scratch, including the quotient's generic-fibre formula, then seek an external independent audit once the geometric realization is settled. The present turn does not create a new external audit packet.
