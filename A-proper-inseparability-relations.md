# Project A — Proper inseparability projections and Hausdorff quotients

**19 October 2026. Status: working mathematical investigation; topological theorem proved; categorical quotient consequences cross-checked with published Manuell (2023), with the effectiveness boundary explicitly left unresolved outside the spatial setting. No novelty/priority claim.**

## Executive result

Let X be a **strongly locally compact sober topological space**, and let E=I(X)=cl_{X×X}(Δ_X) be the **closed pointwise inseparability relation**. Suppose E is **transitive** (hence an equivalence relation). If either projection p_i:E→X, with E carrying the subspace topology, is **perfect** (a closed map with compact fibers), then:

1. The quotient q:X→Q=X/E is closed with compact fibers.
2. Q is **locally compact Hausdorff**.
3. Therefore **I=U=F as closed localic relations**.

The assumption **I=U** is a convenient sufficient way of ensuring E is transitive, but is **NOT required** in the theorem. The theorem is a formal application of proper-equivalence quotient arguments, not currently a priority claim.

**Even stronger purely topological version:** for **any** topological X and **any closed equivalence relation** E⊆X×X, if p_1 or p_2 is perfect, then Q=X/E is Hausdorff; no local compactness, sobriety, or I=U is required for that result.

## 1. Proper/perfect maps: terminology in topology and locales

For ordinary topological spaces, use **perfect** to mean *continuous, closed, and all fibers compact*.

For a locale morphism f:Z→Y, with frame homomorphism f*:O(Y)→O(Z) and right adjoint f_*:O(Z)→O(Y), the **standard point-free properness condition** is:

(a) f_* preserves directed joins (Scott continuity), and
(b) **closed Frobenius/co-Frobenius**: f_*(u∨f*(v))=f_*(u)∨v for all u∈O(Z), v∈O(Y).

Convention warning: “perfect” without closedness is used by some authors for condition (a) alone; Manuell calls this *semi-proper/perfect*, while *proper* requires both (a),(b). Earlier project notes used “proper/perfect” more casually; distinguish them.

Direct published source: Graham Manuell, *Presenting Quotient Locales*, *Applied Categorical Structures* **31** (2023), art. 28, §2 (map definitions), §3 (proper coequalizers/Remark 3.8), https://link.springer.com/article/10.1007/s10485-023-09736-x . There is a 2023 publisher correction about XML syntax; no indication it changes these mathematics. Classical source J.J.C. Vermeulen, *Proper Maps of Locales*, *J. Pure Appl. Algebra* **92** (1994), 79–107, DOI 10.1016/0022-4049(94)90047-7. Manuell refers explicitly to Vermeulen and to Korostenski–Labuschagne (2007).

## 2. Perfect projections imply a Hausdorff quotient (no I=U needed)

**Theorem (topological; working proof).** If E⊆X×X is a **closed equivalence relation** and one projection p_1:E→X is a perfect map, then the quotient q:X→Q=X/E is a closed map with compact fibers, and Q is Hausdorff.

**Proof.** Because E is symmetric, swapping coordinates identifies p_1 with p_2; both are perfect. For each x, p_1^-1(x)≅E[x], so each equivalence class is compact. For every closed H⊆X, its saturation is

    E[H]=p_1(p_2^-1(H)).

Since p_2^-1(H) is closed in E and p_1 is closed, E[H] is closed. Since q^-1(q(H))=E[H], and q is a quotient map, q(H) is closed; q is thus a closed surjection with compact fibers.

Let C,D be distinct classes, which are compact. For every x∈C, y∈D, (x,y)∉E; E closed implies there exist neighborhoods U_xy of x and V_xy of y such that U_xy×V_xy misses E. Fix x, cover D by finitely many V_xy_j, and set U_x=∩_j U_xy_j, V_x=∪_j V_xy_j. Then U_x×V_x misses E and D⊆V_x. Next cover C by finitely many U_x_i; put U=∪_i U_x_i and V=∩_i V_x_i. Then C⊆U, D⊆V, and U×V misses E. Thus q(U) and q(V) are disjoint (possibly nonopen).

Because q is closed, the **saturated shrinks**

    U'=X\q^-1(q(X\U)),   V'=X\q^-1(q(X\V))

are **open saturated** neighborhoods of C,D contained in U,V. Their images under the quotient map q are disjoint open neighborhoods of their class points. Hence Q is Hausdorff. □

**Local compactness addendum.** If X is strongly locally compact and the quotient q is perfect, then Q is locally compact. Let K=q^-1(y) be compact; choose finitely many open compact-containment neighborhoods covering K, with open union U and compact union M⊇U. Then W=Q\q(X\U) is open around y and W⊆q(M), compact. This establishes (weak) local compactness. Since Q is Hausdorff, it has the strong version automatically.

**Consequence for E=I:** All continuous real maps X→R are constant on E classes (inseparability); they descend to Q. Since Q is locally compact Hausdorff, continuous real functions on Q distinguish its points. Thus E=F on points. By the hierarchy E=I⊆U⊆F, all three coincide on points. X is strongly locally compact sober, so X×X is spatial, and equality of these closed localic relations follows.

**Localic transitivity from I=U under spatiality.** For X strongly locally compact sober, X³ is spatial. The pullbacks E_12 and E_23 of the **closed** sublocale E↪X² are closed sublocales of X³; their intersection, the object of composable E-arrows, is therefore spatial. If I=U pointwise, the elementary proof of transitivity (y lies in the closures of both arbitrary x- and z-neighborhoods) shows every point of E_12∩E_23 is in E_13. Since all these sublocales are **closed in the spatial X³**, their inclusion holds localically. Reflexivity and symmetry are immediate. Hence I=U really yields an **internal equivalence relation** for continuous locales, not only a point equivalence.

**Why transitivity is essential.** For a finite T0 Alexandrov zigzag with order a<u>b<v>c (relations a<u,b<u,b<v,c<v), the inseparability relation I=clΔ satisfies a I b and b I c but not a I c. The space X is finite and thus compact; projections of the closed subspace I⊆X×X are closed (projection along a compact factor), with finite compact fibers, hence perfect. Yet I is **not an equivalence relation**; no quotient X/I is available without taking transitive closure. Therefore projection properness *alone* does not imply I=U=F.

## 3. Frame-theoretic / localic quotient: an intrinsic formula

For a localic **internal equivalence relation** E↪X×X with p_1,p_2:E⇉X, its coequalizer q:X→Q has

    B=O(Q) = {a∈L=O(X): p_1*(a)=p_2*(a)}

as a subframe of L (q* is inclusion; this is a general coequalizer fact in Loc). If p_2 is proper, define

    r(u)=(p_2)_*(p_1^*(u)),     u∈L.

The reflexive/symmetric/transitive axioms and proper base-change imply that r is a **deflationary, idempotent, Scott-continuous finite-meet-preserving operator**; its fixed points are B. Concretely, it is the **largest saturated open below u**. For topological equivalence relations this is u↦X\E[X\u]. In localic form q* q_*=r.

Proper Frobenius of p_2 and the equality p_1^*(v)=p_2^*(v) for v∈B yield

    r(u∨v) = r(u)∨v,  v∈B,

so q is a **proper quotient**. This is consistent with—and can be read directly in—Manuell (2023) §3, particularly Remark 3.8, whose proper quotient description is credited to Vermeulen (1994).

### A genuinely point-free theorem: the quotient has a closed diagonal

**Proposition (working categorical proof, assuming the standard proper-quotient results above).** If E is a **closed internal equivalence sublocale** E↪X×X, and p_1,p_2:E⇉X are proper, then the coequalizer q:X→Q is proper, and Q is **strongly Hausdorff** (its diagonal is a closed sublocale).

**Proof.** Proper maps of locales are stable under products, hence q×q:X×X→Q×Q is proper. The **image of a closed sublocale under a proper map is closed**, so the image of E under q×q is closed. Since qp_1=qp_2, this image lies in Δ_Q. By reflexivity, Δ_X factors through E, and (q×q)δ_X=δ_Qq. Because q is a proper **surjection**, its image is all of Q, so the image of δ_Qq is Δ_Q. Therefore the image of E is **exactly Δ_Q**, proving that Δ_Q is closed. □

This conclusion DOES NOT require assuming E equals the kernel pair X×_Q X: effectiveness of the given internal equivalence relation is a separate categorical issue. Thus this is a genuine localic Hausdorff-quotient result (conditional only on the standard proper-quotient theorem).

### Proper surjections preserve continuity of frames (direct calculation)

Let q:X→Q be a **proper surjection** and O(X)=L be continuous. Put B=O(Q), with q*:B→L injective and right adjoint q_*:L→B Scott-continuous. Then for any b∈B,

    q*(b)= ⋁_{u≪q*(b)} u   (directed join).

Applying q_* and using q_*q*=id_B yields

    b= ⋁_{u≪q*(b)} q_*(u).

Each q_*(u)≪b: given a directed cover b≤⋁_i b_i, apply q*; because u≪q*(b), for some i we have u≤q*(b_i), whence q_*(u)≤q_*q*(b_i)=b_i.

Hence B is continuous. This proves continuity of a proper quotient of a continuous locale **intrinsically**, without invoking its points.

**Deduction.** If X is a continuous locale, E is a closed internal equivalence relation with proper projections, then Q is continuous and strongly Hausdorff. Under classical ZFC/Hofmann–Lawson, Q is the frame of opens of a locally compact sober space, and its closed diagonal forces the space to be Hausdorff and thus completely regular. Therefore **Q is a completely regular locale**.

**Boundary for a full arbitrary-locale I=F theorem:** when Q is completely regular, `F(X)⊆kerpair(q)`, because the real maps Q→R jointly separate Q and their pullbacks belong to the defining family of F. If moreover `E⊆F(X)` (as happens for E=I), then every real map X→R coequalizes E and therefore factors through q, giving `kerpair(q)⊆F(X)`. Hence in our inseparability setting `F(X)=kerpair(q)`; nevertheless **F=E still requires E=kerpair(q)** (effectiveness). In the continuous spatial setting the earlier point-set proof supplies the needed equality. Do not silently infer effectiveness from the mere existence of a coequalizer or from the closed diagonal.

## 4. Scope, examples and implications

**Relation projection perfect ⇔ quotient map perfect (ordinary Top, for equivalence relations):** from p_i perfect the theorem gives q perfect; conversely p_i is a pullback of q along q, and perfect maps are pullback-stable. Thus either formulation is natural in ordinary topology. This equivalence is topological, not automatically an assertion about all localic relations without effectiveness.

**Comparison with our counterexamples.** Both the generic-tag and cofinite-cloud deleted-plank examples have a **closed** inseparability quotient, but their nontrivial inseparability classes are A,B (or A∪{p_A},B∪{p_B}) and are **noncompact**. Hence their relation projections are NOT proper/perfect. The new T1 subfit example demonstrates that subfitness, algebraicity, closed quotient, and even absence of isolated points do not replace compact-fiber control.

**Possible next mathematical tests:**
1. Does I=U already force I to be a **localic** internal equivalence relation (as opposed to only a pointwise equivalence) without continuity? Under strong LC sobriety, product spatiality permits checking equality on points in higher products.
2. Confirm precise conditions under which closed proper E is effective in Loc. Karazeris–Tsamis (2020, *Regular and Effective Regular Categories of Locales*, arXiv:2004.04404) cite Vermeulen (1994) Theorem 5.17 for **closed proper equivalence relations on compact locales**; no unqualified theorem for arbitrary locales is asserted here.
3. If effectivity holds, the above completely regular quotient implies **E=F** in the purely point-free setting. Otherwise, document the obstruction (failure of descent/effectivity).
4. Explore whether one projection merely **closed** plus compact classes is enough pointwise (yes: closed+compact = perfect), and whether Scott continuity without Frobenius suffices (not established).
5. Check the exact analogues with other closed localic relations U,F: without transitivity, properness of projections does not provide a quotient theorem.

## References

- G. Manuell, *Presenting Quotient Locales*, **Applied Categorical Structures** 31 (2023), article 28, https://link.springer.com/article/10.1007/s10485-023-09736-x , §§2–3 and Remark 3.8.
- J. J. C. Vermeulen, *Proper Maps of Locales*, **Journal of Pure and Applied Algebra** 92 (1994), 79–107, https://doi.org/10.1016/0022-4049(94)90047-7 .
- P. Karazeris and K. Tsamis, *Regular and Effective Regular Categories of Locales*, arXiv:2004.04404 (2020), Theorem 4.3 and citation to Vermeulen 5.17 for the compact case.
- Project A [A-obstruction-candidates.md](A-obstruction-candidates.md) and [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md).
