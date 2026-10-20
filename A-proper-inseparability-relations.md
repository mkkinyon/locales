# Project A — Proper inseparability projections and Hausdorff quotients

**19 October 2026. CORRECTED SOURCE CHECK:** Vermeulen (1994), **Corollary 5.17**, already proves that **every closed proper equivalence relation of locales is effective**, without assuming the ambient locale compact. Our former ``effectiveness gap'' was a misreading of the *compact-locale application* in Karazeris–Tsamis (2020). The source is https://core.ac.uk/download/pdf/82053693.pdf (search-indexed scan p. 107; direct retrieval was blocked). All proofs below are supplementary, not extensions of Vermeulen's effectiveness theorem. No claim of novelty.**

## Primary-source effectiveness correction

**Vermeulen, *Proper Maps of Locales*, JPAA 92 (1994), Corollary 5.17**: every **closed proper internal equivalence relation** on a locale is **effective**. His parenthetical compact-locale case is **only an example**. This is independently confirmed by the scan's original conclusion on p. 107, https://core.ac.uk/download/pdf/82053693.pdf, indexed at https://www.google.com/search?q=%22Closed+proper+equivalence+relations%22+Vermeulen . Manuell (2023) supplies the proper quotient interior-operator machinery. Thus, assuming I=U and the projections of I proper, no extra effective-descent hypothesis is needed. In continuous frames, the proper quotient is continuous and strongly Hausdorff, hence completely regular; the quotient is the completely regular reflection and I=U=F.

## Executive result

Let X be a **strongly locally compact sober topological space**, and let E=I(X)=cl_{X×X}(Δ_X) be the **closed pointwise inseparability relation**. Suppose E is **transitive** (hence an equivalence relation). If either projection p_i:E→X, with E carrying the subspace topology, is **perfect** (a closed map with compact fibers), then:

1. The quotient q:X→Q=X/E is closed with compact fibers.
2. Q is **locally compact Hausdorff**.
3. Therefore **I=U=F as closed localic relations**.

The assumption **I=U** is a convenient sufficient way of ensuring E is transitive, but is **NOT required** in the theorem. The theorem is a formal application of proper-equivalence quotient arguments, not currently a priority claim.

**Even stronger purely topological version:** for **any** topological X and **any closed equivalence relation** E⊆X×X, if p_1 or p_2 is perfect, then Q=X/E is Hausdorff; no local compactness, sobriety, or I=U is required for that result.

## 0. The basic relation-composition lemma is purely point-free

**Theorem (all locales, no spatial or compactness assumptions):**

    I∘I ⊆ U.

Proof. Let P=I_12∩I_23↪X³ be the locale of composable I-arrows, with projections to the first, middle, last coordinates. Let a*∨b*=1. In O(P), pullbacks of a, a*, b, b* are denoted a_1,(a*)_2,b_3,(b*)_2. By the defining relation I=C(d_I), since a∧a*=b*∧b=0,

    a_1∧(a*)_2=0,     (b*)_2∧b_3=0.

Distributing over a*∨b*=1 in the middle coordinate gives

    a_1∧b_3
      = a_1∧((a*)_2∨(b*)_2)∧b_3
      =0.

The map P→X² on first and last coordinates therefore factors through U. In particular **I=U ⇒ I is an internal equivalence relation** for *every locale*, because I is already symmetric and reflexive. This improves the earlier pointwise/spatial transitivity proof and makes the properness hypothesis immediately applicable to our main equality problem.

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

## 2½. Exact frame-theoretic signature of the obstruction: failure of Scott continuity

**Proposition (closed surjections).** Let q:X→Q be a **closed surjective quotient map** of ordinary topological spaces, with right adjoint

    q_*(U)=Q\q(X\U),     U∈O(X),

which is open because q is closed. Then

    q_* preserves directed joins  ⇔  every fiber q^-1(y) is compact.

The co-Frobenius equality q_*(U∪q^-1(V))=q_*U∪V already follows from closedness and surjectivity. Thus for a closed surjection **failure of properness is exactly failure of compactness of some quotient fiber**, detected by Scott discontinuity of q_*.

**Proof, compact⇒Scott.** If y∈q_*(⋃_i U_i) for a directed family of opens, then its compact fiber K_y lies in ⋃_i U_i, hence by compactness and directedness K_y⊆U_i for some i. Thus y∈⋃_i q_*U_i. The reverse inclusion is monotonicity.

**Proof, Scott⇒compact.** Given any open covering {U_j} of a fiber K_y, form the directed family of its finite unions U_F. Since K_y⊆⋃_F U_F, we have y∈q_*(⋃ U_F)=⋃ q_*U_F, hence K_y⊆U_F for some finite F. Therefore K_y compact. □

**Explicit witness in the deleted-plank cofinite-cloud example.** The edge A={ω1}×[0,ω) is a closed **discrete**, countably infinite subset of X, hence every subset of A is closed in X. Enumerate A={a_0,a_1,…}, set A_n={a_0,…,a_n}, and define

    U_n = X\(A\A_n).

Each U_n is open; the family is increasing and ⋃_n U_n=X. Let q:X→Q=X/I be our closed quotient, and r=q*q_* be the **saturated-open interior** operator on L=O(X). Because the class A is not contained in any U_n, no r(U_n) contains even a single point of A. On the other hand

    r(⋁_n U_n)=r(1)=1,       ⋁_n r(U_n) does not meet A.

Therefore **r fails to preserve the directed join** of the U_n. This is the precise frame-level defect that defeats properness in this counterexample. It is a sharper diagnosis than merely saying that the equivalence classes are noncompact.

**Important non-necessity:** Properness is a **sufficient** condition for relation collapse, not an exact criterion for I=U=F. The same cofinite-cloud construction over a **normal** locally compact Hausdorff T (e.g. two disjoint countably infinite discrete components with A,B the components) has noncompact E-classes and non-Scott-continuous r, but A and B are completely separated and therefore I=U=F. Consequently the diagnosed failure of Scott continuity explains why the *proper-quotient argument* does not apply to the plank; it is not by itself equivalent to functional indistinguishability.

**Terminology:** the Scott-continuity law here is the preservation of directed joins by the **right adjoint** q_* of the inverse-image map q*, not by q* itself (which always preserves arbitrary joins). The topological quotient remains closed, so its closed Frobenius law still holds.

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

**Vermeulen's Corollary 5.17 supplies effectiveness separately and unconditionally under the present hypotheses:** closed proper equivalence relations are kernel pairs of their coequalizers in Loc. The closed-diagonal image argument remains a useful short independent proof that the quotient is strongly Hausdorff.

### Proper surjections preserve continuity of frames (direct calculation)

Let q:X→Q be a **proper surjection** and O(X)=L be continuous. Put B=O(Q), with q*:B→L injective and right adjoint q_*:L→B Scott-continuous. Then for any b∈B,

    q*(b)= ⋁_{u≪q*(b)} u   (directed join).

Applying q_* and using q_*q*=id_B yields

    b= ⋁_{u≪q*(b)} q_*(u).

Each q_*(u)≪b: given a directed cover b≤⋁_i b_i, apply q*; because u≪q*(b), for some i we have u≤q*(b_i), whence q_*(u)≤q_*q*(b_i)=b_i.

Hence B is continuous. This proves continuity of a proper quotient of a continuous locale **intrinsically**, without invoking its points.

**Deduction.** If X is a continuous locale, E is a closed internal equivalence relation with proper projections, then Q is continuous and strongly Hausdorff. Under classical ZFC/Hofmann–Lawson, Q is the frame of opens of a locally compact sober space, and its closed diagonal forces the space to be Hausdorff and thus completely regular. Therefore **Q is a completely regular locale**.

**The remaining distinction is complete regularity, NOT effectiveness:** when Q is completely regular, `F(X)⊆kerpair(q)`, because the real maps Q→R jointly separate Q and their pullbacks belong to the defining family of F. If moreover `E⊆F(X)` (as happens for E=I), then every real map X→R coequalizes E and therefore factors through q, giving `kerpair(q)⊆F(X)`. Hence in our inseparability setting `F(X)=kerpair(q)`; and **Vermeulen's Corollary 5.17 already gives E=kerpair(q)** for our closed proper equivalence. Thus whenever Q is completely regular, E=I=F, with no spatial assumption. If X is continuous then Q is continuous and strongly Hausdorff, so Q is completely regular in ZFC by Hofmann–Lawson; hence **I=U=F** for all continuous locales satisfying I=U and properness of I projections.

## 3½. An independent spatial proof (now subsumed by Vermeulen 5.17)

**New working theorem (requires the standard spatial characterization of localic properness, which must be checked against Johnstone/Vermeulen before publication).** Let X be a **strongly locally compact sober topological space**. Let E↪X×X be a **closed internal localic equivalence relation** and suppose both projections E⇉X are **proper as locale maps**. Then its coequalizer q:X→Q is the **kernel-pair quotient**:

    E = X×_Q X,

and Q is locally compact Hausdorff. In particular, when E=I=cl(Δ_X), the conclusion is I=U=F.

The same pointwise argument applies to any spatial closed E when the projections satisfy the **non-Hausdorff topological properness criterion** described immediately below. The point-free-to-spatial correspondence for proper maps is the imported standard fact; it is not proved from frame adjunctions in this note.

### Step 1. Closed reflexive relations contain specialization comparisons

Write x≤y for the specialization order: every open neighborhood of x contains y. Then the specialization preorder on X×X is coordinatewise. Because E is **closed and reflexive**, whenever x≤y we have

    (y,y)∈E,    (x,y)≤(y,y),    hence (x,y)∈E.

By symmetry, (y,x)∈E as well. Hence each E-equivalence class C_x is both upward and downward closed for specialization. This is an elementary but essential non-T1 fact.

### Step 2. Proper relation projections give compact equivalence classes

The standard topological characterization of **proper maps in the non-Hausdorff sense** (see J. Goubault-Larrecq, *Proper maps, quasi-adjoints and the Smyth hyperspace*, https://topology.lmf.cnrs.fr/proper-maps-quasi-adjoints-and-the-smyth-hyperspace/ , Theorem A; Johnstone/Vermeulen for the localic version) states that a proper continuous f:Y→Z has:

1. f^-1(K) compact for every compact saturated K⊆Z;
2. **downward closure** ↓f[H] closed in Z for every closed H⊆Y.

It does **not** assert that f is closed on ordinary closed sets in a non-T1 codomain. For any x∈X, the specialization saturation ↑x is a **compact saturated subset**: a single open containing x covers all of ↑x. Properness of p_2:E→X gives a compact subset

    H_x = p_2^-1(↑x) ⊆ E.

Because x≤z entails xEz, transitivity gives the exact image identity

    p_1(H_x)=E[x].

Indeed, yEx implies (y,x)∈H_x; conversely if (y,z)∈E with z≥x, then xEz and hence yEx. Thus the class E[x] is a continuous image of compact H_x and is **compact**.

### Step 3. Proper projections give ordinary closed saturation

For a closed H⊆X, p_2^-1(H) is closed in E. Properness of p_1 implies

    ↓p_1(p_2^-1(H)) = ↓E[H]

is closed. But E[H] is already **downward closed**: if zEy with y∈H and z'≤z then, since E is closed, z'Ey. Hence E[H] is itself closed. Thus the ordinary quotient q_t:X→Q_t=X/E is a **closed map**.

Together with Step 2 it has compact fibers, so q_t is perfect in the ordinary closed+compact-fiber sense. Closedness of E and compactness of two different classes allow finite rectangular separation, giving **Q_t Hausdorff**, exactly as in §2. The strong local compactness of X and perfectness of q_t give Q_t locally compact. Hence Q_t is **Hausdorff, sober, and completely regular**.

### Step 4. Deduce genuine localic effectiveness

Since X is strongly locally compact sober, X×X is spatial; hence the **closed** E↪X×X is spatial and its points are exactly the ordinary closed E-subset. The frame coequalizer of its projections is precisely the frame of ordinary E-saturated opens,

    O(Q)= {u∈O(X):p_1^*u=p_2^*u} = O(X/E)=O(Q_t).

Because Q_t is Hausdorff and thus sober, there is no sobrifification ambiguity: Q and Q_t are the **same locale**.

The diagonal Δ_Q is closed. Consequently the kernel pair X×_Q X is a **closed** sublocale of X×X. It has exactly the ordinary pairs (x,y) satisfying q_t(x)=q_t(y), i.e. exactly E. Since closed sublocales of spatial O(X×X) are determined by their point sets,

    E = X×_Q X.

This provides an alternative spatial proof for continuous frames, but **Vermeulen 1994, Corollary 5.17 is stronger**: closed proper equivalence relations are already effective for *all locales*, including noncompact and pointless ones. The spatial argument is therefore optional.

### Step 5. The quotient is actually the completely regular reflection

Now take E=I=clΔ. Every real-valued map X→R coequalizes E (because I⊆F), so factors uniquely through q. Since Q is completely regular, its opens are generated by pullbacks of real opens. Therefore, as subframes of L,

    O(Q)=C(L),

where C(L) is the **largest completely regular subframe** generated by localic real maps. Hence q is precisely the completely regular reflection map r_X, and

    I=kerpair(q)=F.

Moreover q is a **proper quotient** in the localic sense by Manuell's / Vermeulen's result. Thus the properness hypothesis produces not merely functional separation, but a proper completely regular reflection.

**Important priority/correctness caveat:** the transposition from localic properness to the modified topological criterion in Step 2 is standard for spatial sober locales but needs a precise reference and exact hypotheses confirmed before the theorem is advertised as choice-free. The remainder is a direct proof. In the case where “proper” is assumed **explicitly for the underlying topological projections**, Steps 1–5 are unconditional point-set arguments plus established Hofmann–Lawson duality.

### Explicit internal formula for the saturation operator

For E=I=C(d_I), with d_I=∨_{a∧b=0}a⊠b, O(E)=↑d_I as a frame quotient of L⊗L. For u,v∈L,

    v≤(p_2)_*p_1^*(u)
     ⇔ p_2^*v≤p_1^*u in O(E)
     ⇔ (1⊠v)≤(u⊠1)∨d_I.

Consequently

    r_I(u)=⋁{v∈L:(1⊠v)≤(u⊠1)∨d_I}.

This is valid **for any locale** even before I is known transitive; in the equivalence-relation case r_I is the idempotent saturated-open interior, with fixed-point frame O(X/I). If the projections are proper, r_I is Scott-continuous.

### Exactly what the two-tag / cofinite-cloud examples violate

In our plank constructions the E-classes are noncompact. Equivalently, the **proper quotient's** Scott-continuity criterion fails, witnessed by the increasing sequence U_n=X\(A\{a_0,…,a_n}) in §2½: r_I(∨U_n)≠∨r_I(U_n). This is the failure of **properness**, not an exact characterization of E≠F: normal-base variants give E=F even with noncompact fibers.

## 3¾. Vermeulen's actual general effectiveness theorem — critical correction

Vermeulen (1994), **Corollary 5.14**, proves effectiveness for proper equivalence relations **weakly fitted in X×X over X**, with open proper relations as a special case. Crucially, **Corollary 5.17 (not just a compact-locale theorem) states: 'Closed proper equivalence relations (in particular closed equivalence relations on a compact locale) are effective.'** The ambient locale need not be compact. The Karazeris–Tsamis (2020) citation uses only the parenthetical compact special case, which led to our earlier erroneous restriction.

The notion “weakly fitted over X” is a relative condition, different from ordinary fitness or fitted diagonal. **Our closed relation E=clΔ does not need to satisfy it**: properness plus closedness triggers Corollary 5.17 directly. Source: Vermeulen *Proper Maps of Locales*, https://core.ac.uk/download/pdf/82053693.pdf (search-indexed full PDF, but direct fetch currently unavailable); Karazeris–Tsamis, https://cahierstgdc.com/wp-content/uploads/2021/07/Karazeris-Tsamis_LXII-3.pdf , Thm 4.3.

**Conclusion:** no special closure-of-diagonal effectiveness theorem remains to prove. Instead, the natural unrestricted question is whether the **strongly Hausdorff quotient** of a closed proper relation is completely regular without continuity of X; that does not follow in general from strong Hausdorffness alone. For continuous X, continuity passes to the proper quotient and gives complete regularity.

## 4. Scope, examples and implications

**Relation projection perfect ⇔ quotient map perfect (ordinary Top, for equivalence relations):** from p_i perfect the theorem gives q perfect; conversely p_i is a pullback of q along q, and perfect maps are pullback-stable. Thus either formulation is natural in ordinary topology. This equivalence is topological, not automatically an assertion about all localic relations without effectiveness.

**Comparison with our counterexamples.** Both the generic-tag and cofinite-cloud deleted-plank examples have a **closed** inseparability quotient, but their nontrivial inseparability classes are A,B (or A∪{p_A},B∪{p_B}) and are **noncompact**. Hence their relation projections are NOT proper/perfect. The new T1 subfit example demonstrates that subfitness, algebraicity, closed quotient, and even absence of isolated points do not replace compact-fiber control.

**Possible next mathematical tests (updated after verifying Vermeulen 5.17):**
1. Does I=U already force I to be a **localic** internal equivalence relation (as opposed to only a pointwise equivalence) without continuity? Under strong LC sobriety, product spatiality permits checking equality on points in higher products.
2. **Resolved by primary source:** Vermeulen (1994) Corollary 5.17 proves effectiveness of **all closed proper equivalence relations of locales**. There is no missing assumption E=clΔ or X compact.
3. For E=I, effectivity now holds; establish complete regularity of Q under useful hypotheses. Continuous X suffices, but arbitrary localic X need not have a completely regular quotient.
4. Explore whether one projection merely **closed** plus compact classes is enough pointwise (yes: closed+compact = perfect), and whether Scott continuity without Frobenius suffices (not established).
5. Check the exact analogues with other closed localic relations U,F: without transitivity, properness of projections does not provide a quotient theorem.

## References

- G. Manuell, *Presenting Quotient Locales*, **Applied Categorical Structures** 31 (2023), article 28, https://link.springer.com/article/10.1007/s10485-023-09736-x , §§2–3 and Remark 3.8.
- J. J. C. Vermeulen, *Proper Maps of Locales*, **Journal of Pure and Applied Algebra** 92 (1994), 79–107, https://doi.org/10.1016/0022-4049(94)90047-7 .
- P. Karazeris and K. Tsamis, *Regular and Effective Regular Categories of Locales*, arXiv:2004.04404 (2020), Theorem 4.3 and citation to Vermeulen 5.17 for the compact case.
- Project A [A-obstruction-candidates.md](A-obstruction-candidates.md) and [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md).
