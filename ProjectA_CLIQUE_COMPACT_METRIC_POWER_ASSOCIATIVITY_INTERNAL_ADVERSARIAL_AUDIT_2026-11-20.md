# Project A — internal adversarial audit of compact-metric clique power-associativity

**Date:** 20 November 2026  
**Source reviewed:** [ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_WORKING_2026-11-20.md](../../../../ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_WORKING_2026-11-20.md), including the corrected section-thinness argument.  
**Related older source:** [four-vertex clique test](../../../../ProjectA_CLIQUE_ASSOCIATIVITY_FOUR_VERTEX_TEST_2026-11-20.md).  
**Independence:** This is an **internal adversarial review** of a new, post-referee argument, not an independent blind referee report. The favorable November 20 bounded-diameter referee verdict did **not** include the present saturation/associativity claims.  
**Mathematical setting:** Classical locale theory; compact metrizable Hausdorff **spatial** outer and middle locales, finite support families, sublocale pullbacks and images.

## 1. Verdict

**INTERNALLY ACCEPTABLE, WITH PROOF-EXPANSION REQUIREMENTS; NO FATAL DEFECT FOUND.**

I independently retraced the compact-metric graph-generation lemma (G), dense bipartite composition saturation (B), five-vertex sector resolution (5V), and all-length formula (PA). The closed-support separation and density arguments withstand the natural counterexample tests, including point-free supports with no ordinary points. The corrected section-thinness proof avoids the false principle that every nonzero sublocale of a spatial locale has a point. The two-colour perfect-graph fusion is viable, but should be published as an explicit topological auxiliary lemma rather than the present short paragraph.

**Conditionality:** This verdict is internal, not a proof-assistant check or a second blind external audit. The strongest new assertion (G) depends on standard facts that every sublocale of a regular locale is fitted, on compact regular support, and on the fully spelled-out fusion induction given below. It is reasonable to prepare a **blind external audit** after incorporating the proof insertions. No novel counterexample to (G), (B), or (PA) was found. The earlier externally refereed rank formulas remain unaffected if a later audit were to uncover an issue here.

## 2. Audit of (G): graph generation of a localic product

### 2.1 Exact statement

Let X,Z be compact metrizable Hausdorff spaces; A=[A_pts]≤X and D=[D_pts]≤Z induced spatial sublocales, and P=[A_pts×D_pts]≤X×Z. Let \(\mathscr G\) be the compact Cantor graphs Γ⊂X×Z with injective coordinate projections and **separately dense** A-first and D-second ordinary point traces. Then
\[
A\times D=P\vee\bigvee_{\Gamma\in\mathscr G}\mathcal B(\Gamma).\tag{G}
\]

The "separately dense" qualifier is essential: there need not be any Γ-point with *both* coordinates in the selected subsets. One must not replace the RHS with the spatialization P.

### 2.2 Easy inclusion and fitted-separator step — PASS

For every Γ in the family, inverse images of A and D along its coordinate projections contain the respective dense ordinary point traces. These pullback sublocales are dense in Γ, so both contain the least dense sublocale \(\mathcal B(\Gamma)\). Therefore B(Γ)≤A×D. The point-generated P is also ≤A×D.

Let J denote the RHS. If A×D≰J, fittedness of **the ambient regular locale X×Z** gives an ambient open O with J≤O but A×D≰O. The complementary closed F satisfies
\[
J\wedge F=0,\qquad (A\times D)\wedge F\ne0.
\]
The implication uses finite distributivity of the sublocale lattice across the complementary open/closed pair; do not infer it from merely missing ordinary points.

Let S=(A×D)∧F and K=\(\overline S\), the least **ambient closed sublocale** containing S. Because F is closed, K⊂F. K is a nonempty closed compact metrizable Hausdorff *space* and S is dense in K by definition. F contains **no** ordinary pair (a,d) with a∈A_pts and d∈D_pts, because all such point sublocales lie in P≤J.

No issue found in this step.

### 2.3 Coordinate richness — PASS

For any nonempty relatively open W⊂K, choose nonempty W'⊂K with compact closure L_K=cl_K(W')⊂W. If W contains no point with first coordinate in A_pts, then the compact projection T=pr_X(L_K) is disjoint from A_pts. The open X\T contains **all points** generating A; therefore A≤X\T as a sublocale. But S≤pr_X^{-1}A, whereas W'⊂pr_X^{-1}T. Hence S∧W'=0, contradicting density of S in K.

Thus points with first coordinate in A_pts are dense in K; the argument for D-second points is symmetric. Note the essential use of compactness to make the coordinate projection **closed**. Merely observing that ordinary A-points are dense in the closure of A would not establish this relative richness.

### 2.4 Thin vertical and horizontal sections — PASS AFTER EXISTING REPAIR

Suppose a fixed vertical section K∩({x}×Z) has nonempty relative interior W⊂K. Choose nonempty relatively open W' with compact closure L_K⊂W.

If x∉A_pts, A≤X\{x}, contradicting S∧W'≠0.

If x∈A_pts, put T=pr_Z(L_K), a compact closed subset of Z. Because L_K⊂F∩({x}×Z), and F contains no selected ordinary endpoint pair, T∩D_pts=∅. Point-generation implies D≤Z\T, whereas W' lies over T; again S∧W'=0.

Therefore every vertical section is relatively closed **nowhere dense** in K; likewise every horizontal section. In particular K has no isolated points. This is the correct argument. The *previously proposed* alternative "nonzero sublocale of a spatial point-slice has a point" is false and should never be reintroduced.

### 2.5 Two-colour Cantor graph fusion — PASS, BUT EXPAND IN MAIN PROOF

A precise form of the topological ingredient is:

> **Two-colour graph lemma.** Let K⊂X×Z be a nonempty compact metric closed subset, with every vertical and horizontal section nowhere dense in K. Let P,Q⊂K be (possibly disjoint) dense sets. Then K contains a compact Cantor subset Γ such that both coordinate projections Γ→X,Z are injective, while Γ∩P and Γ∩Q are both dense in Γ.

**Constructive induction.** At each finite node s retain a relatively open neighborhood V_s of K∩(a compact closed product rectangle R_s), an **inherited anchor** z_s∈K∩int(R_s), and coordinatewise disjoint rectangles at the current level. Inside K∩int(R_s), choose new anchors p_s∈P and q_s∈Q avoiding every previously selected first-coordinate and second-coordinate value; each forbidden section is nowhere dense, so finite exclusions do not destroy density of P or Q. Ensure z_s,p_s,q_s have pairwise distinct first coordinates and pairwise distinct second coordinates.

Process **all finitely many nodes at the current level first** and register all new coordinates globally. Then choose three small closed child product rectangles about z_s,p_s,q_s, nested strictly inside int(R_s), with pairwise disjoint first-coordinate projections and pairwise disjoint second-coordinate projections, and diameter ≤2^{-level}. These choices exist because finitely many pairwise distinct real/metric coordinates admit disjoint neighborhoods. The inherited anchor is kept in child 0; new selected anchors are kept in children 1 and 2. At later levels each old anchor persists down its all-0 descendant chain (so the limit Cantor set contains each chosen anchor).

Nested compactness and vanishing diameters give one limit point for every branch; disjoint coordinate rectangles separate branches **in both coordinates**, yielding a compact Cantor graph with injective projections. Each basic branch cylinder contains a preserved P-anchor and a preserved Q-anchor. Thus Γ∩P and Γ∩Q are dense in Γ.

**Cautions to write explicitly.** Use relative interiors in K and ambient compact metric rectangles; carry a finite list of inherited anchors; perform "select all / then shrink all" globally at each level. One cannot shrink an earlier node's rectangles before observing the new finite exclusions at later nodes without checking cross-node compatibility. Here the proof is easier than the earlier finite-fence fusion because only finite coordinate values—not comparability components—must be excluded.

Apply this topological lemma to
\[
P=\{(x,z)\in K:x\in A_{\rm pts}\},\qquad
Q=\{(x,z)\in K:z\in D_{\rm pts}\}.
\]
By §§2.3–2.4 the hypotheses hold. The resulting Γ⊂K⊂F has nonzero B(Γ), and B(Γ)≤J by definition, contradicting J∧F=0.

Thus (G) is internally supported. The primary recommendation is to **promote the topological lemma and its induction to a formal stand-alone proof**.

## 3. Audit of (B): bipartite point-generated saturation — PASS

The claimed formula is
\[
[A_{\rm pts}\times B_{\rm pts}]\circ
[C_{\rm pts}\times D_{\rm pts}]
=[A_{\rm pts}]\times[D_{\rm pts}],
\tag{B}
\]
where the middle B_pts and C_pts are dense in the **same compact metrizable** Y. The two relations are induced spatial sublocales of X×Y and Y×Z; no product spatiality of the endpoint sublocales is assumed.

**Upper bound:** all source/target maps factor through A and D, so the composite lies in A×D.

**Ordinary point-pair lower bound:** for each a∈A_pts,d∈D_pts the source contains {a}×[B_pts] and the target [C_pts]×{d}. Their middle overlap is nonzero by Isbell's density theorem, and the rectangular lemma yields {(a,d)}. Hence P_{A,D}≤R∘S.

**Booleanized graph lower bound:** For each Γ∈\(\mathscr G(A,D)\), form Γ×Y and map a point (γ,y) to (γ_1,y,γ_2). The pullback of R contains *all* ordinary points (γ,y) with γ_1∈A_pts,y∈B_pts; this subset is dense in Γ×Y. The pullback of S analogously contains those with γ_2∈D_pts,y∈C_pts, also dense. Since both pullback sublocales contain the least dense sublocale \(\mathcal B(\Gamma\times Y)\), their meet contains it. Hence that meet factors through the genuine localic composability pullback.

Projection Γ×Y→Γ is an **open surjection** because Y is inhabited and overt. The image of a dense sublocale along an open surjection is dense (this is the special image-density lemma, not arbitrary image stability); thus the projected composability image contains B(Γ). Combining all Γ with (G) yields A×D≤R∘S.

**Important non-claims:** The intersection of the two *ordinary* point traces may be empty; one cannot replace the localic meet by ordinary paths. Nor is an arbitrary closed-graph restriction of a dense relation used: density of each **actual pullback** is proved by explicit dense ordinary point traces on Γ×Y. The argument requires a common compact metrizable middle envelope for the two dense subsets.

## 4. Five-vertex test — PASS RELATIVE TO (B)

In four disjoint Cantor blocks let
\[
R=[I_0\times Q_1],\quad
S=[I_1\times Q_2],\quad
T=[I_2\times Q_3].
\]
The intermediate Q_i,I_i are each dense in C_i. Thus (B) gives
\[
R\circ S=I_0\times Q_2,\quad
S\circ T=I_1\times Q_3.
\]
Monotonicity and (B), together with endpoint support bounds, give
\[
\boxed{(R\circ S)\circ T=I_0\times Q_3=R\circ(S\circ T).}
\]
The two threefold bracketings therefore agree on the formerly unresolved clopen C_0×C_3 sector. This is not just a point-set equality and does not presume that the product I_0×Q_3 is spatial.

## 5. Audit of all-powers formula (PA) — PASS WITH A REQUIRED INDUCTION INSERTION

For compact metrizable Hausdorff G, finite nonempty ordinary sets/subsets E_i (not necessarily disjoint), let U_i=[E_i], P_i=[E_i×E_i], H=∨P_i. Define the finite overlap graph Λ by U_i∧U_j≠0. For every k≥2 and every fully parenthesized k-factor word W_k(H), the candidate claims
\[
\boxed{W_k(H)=\bigvee_{\operatorname{dist}_\Lambda(i,j)\le k-1} U_i\times U_j.}\tag{PA}
\]
For disconnected Λ, pairs in different connected components are simply omitted.

**Compact overlap support lemma.** Given nonzero W=U_i∧U_j, let K=\(\overline W\) be its least ambient closed support in G. Then E_i∩K and E_j∩K are dense **as ordinary subsets of K**. Proof: if a nonempty relatively open piece of K missed E_i, choose smaller relatively open W' with compact closure T⊂K disjoint from E_i. Then U_i≤G\T, forcing W∧W'=0, contrary to density of W in K. Likewise E_j. Consequently, the two selected middle subsets are dense in the same compact metrizable space K.

**Two-leaf case.** The relation P_i contains the spatial bipartite subrelation \([E_i\times(E_i\cap K)]\), and P_j contains \([(E_j\cap K)\times E_j]\). Apply (B), with middle K, to obtain U_i×U_j≤P_i∘P_j; support containment gives equality. If U_i∧U_j=0, actual composability is zero. This also covers i=j; alternatively P_i²=U_i² by a chosen ordinary mediator point.

**Explicit induction for arbitrary indexed words.** Consider a binary tree with leaf sequence P_{j_1},…,P_{j_k}, with all consecutive U_{j_t}∧U_{j_{t+1}} nonzero. Claim: the tree's value is **exactly** U_{j_1}×U_{j_k} for k≥2.

At the root split into subtrees L and R. Their endpoint supports across the cut are U_{j_t}, U_{j_{t+1}}, with a nonzero overlap.
- If both children have ≥2 leaves, induction gives L=U_{j_1}×U_{j_t} and R=U_{j_{t+1}}×U_{j_k}. The rectangle lemma gives the desired full outer rectangle.
- If the left child is one leaf P_i and the right child has ≥2 leaves, induction gives the right child the full rectangle U_j×U_\ell. Let K be the least closed support of U_i∧U_j. The left relation contains \([E_i\times(E_i\cap K)]\), and the full right rectangle contains \([(E_j\cap K)\times E_\ell]\). Apply (B) to these two point-generated subrelations, with middle K, to get U_i×U_\ell in the composite. Endpoint support gives equality.
- If the right child is one leaf, argue symmetrically.
- If both children are leaves, use the two-leaf case.

Conversely, if two consecutive supports U_{j_t},U_{j_{t+1}} have zero meet, their lowest-common-ancestor split has child endpoint supports inside them, so the entire indexed tree has zero composability. This is independent of the bracketing.

**Finite expansion.** Since H is a *finite* join, expand any k-word into finitely many indexed words. The nonzero words correspond exactly to walks of k−1 edges in Λ, allowing repeated vertices (each U_i≠0). Every such word equals the full endpoint rectangle as proved above. Hence precisely the index pairs with dist_Λ(i,j)≤k−1 appear, yielding (PA). No implicit associativity was used in the induction.

**Caution:** k=1 is explicitly excluded: P_i need not equal U_i×U_i when the latter is nonspatial. The result is **power-associativity of the single H**, not a claim about arbitrary heterogeneous localic relations.

## 6. Adversarial checks: false shortcuts excluded

The following tempting proof moves are **invalid** and must stay excluded from the final draft:

1. "The ambient G² is spatial, so a sublocale of it is determined by its points." False; point-generated cliques may gain nonspatial material in their square.
2. "Any nonzero sublocale of a spatial point-slice has an ordinary point." False; the corrected compact projection/closed-separator argument is needed.
3. "Two dense point sets with no common points have zero meet." False by Isbell density; this is exactly the point-free bridge.
4. "Spatiality of A and D implies A×D is spatial." False in general. The proof of (G) builds the entire localic product with Booleanized closed graphs.
5. "A dense relation stays dense when restricted to any closed graph." False. The proof of (B) restricts **before composing** and verifies density of both pullbacks using the two selected-coordinate traces.
6. "A locale-surjection remains surjective under all base changes." False. Only the **open-surjective** rectangle and projection maps are used.
7. "Unrestricted relational composition distributes over arbitrary joins." Not used. Finite-join distribution suffices because the index family is finite.
8. "A connected overlap graph makes every first power full." False; formula (PA) starts at k=2 and explicitly retains point-generated P_i at k=1.

**Remaining exposition-level tasks:** formalize the compact two-colour graph lemma as a separate proposition; state all ambient spaces for spatial and localic products; spell out the 4-case binary-tree induction above; indicate that both overlap supports and the middle envelope K are compact **closed supports**, not arbitrary noncompact intersections.

## 7. Recommendation

Retain the original working note, but **do not yet promote it to the externally audited canonical theorem ledger**. Prepare a clean proof revision incorporating §§2.5 and 5, then an independent blind referee packet with focus on the graph-generation lemma (G) and the use of a **specific compact closed support** in the clique induction. A small test case is the threefold sector [I_0×Q_1],[I_1×Q_2],[I_2×Q_3], but a referee should check (G) for **arbitrary** point-generated endpoint sublocales, not only rational/irrational Cantor partitions.

**Bottom line:** The proposed five-vertex equality and compact-metric all-powers formula pass this internal adversarial audit **subject to the explicitly expanded compact-metric fusion proof**. The central potential objection is no longer an identifiable gap or counterexample, but ensuring the fusion registry and relative-closed-support steps are written at a level that an independent reader can verify.
