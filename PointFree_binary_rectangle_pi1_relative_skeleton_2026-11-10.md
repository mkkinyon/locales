# Point-Free Topology — Return to binary relations: rectangle presentation and first skeletal comparison

**10 November 2026 · New internally checked working mathematics, not externally audited or priority checked.** Returns to the [parked binary feedback roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md) after the bounded twisted-coefficient segment. Uses the previously independently audited coherent spectral descriptions of the higher hulls and the pointed face-poset construction. No claim of intrinsic localic shape or of a literature-priority theorem.

## 0. Setting

For coherent X, write V=h(Patch X), A_n=h(Patch Ch_n(X)), B_n^+=h(Patch I_n(X)), B_n^-=h(Patch D_n(X)). The specialization order has opens as upsets. I_n and D_n are actual coherent proconstructible sublocales consisting of common-upper and common-lower tuples respectively. Work in the fixed sufficiently large Stone-sheaf infinity-topos H, with finite jointly surjective covers, including the empty cover. Define C=|A|, I=|B^+|, D=|B^-|. The binary relations are I_1=cal I, D_1=cal D; Ch_1 is the oriented specialization relation, not the symmetric comparability relation. Write concatenated paths in traversal order.

## 1. Witness triangles and 1-connectivity

An I_1-edge (x,y) has locally a common upper witness u, by the surjective Stone witness projection (pull back over any test Stone). The I_2 triangle (x,y,u) has boundary [y,u]-[x,u]+[x,y] and identifies the edge x→y with the chain path x→u←y. Dually the D_2 triangle (z,x,y) for a common lower witness z replaces x→y by x←z→y. Thus the maps C→I,D have isomorphic component sheaves and locally surjective fundamental group sheaves at compatible basepoints. In the convention where a 1-connected map has connected homotopy fibres, both maps are 1-connected. This is not injectivity on pi_1, and is not an assertion of globally continuous witness choices. The exact result below gives a more precise proof.

## 2. Rectangle presentation of the fundamental groupoid

Let G_X be the fundamental groupoid with object sheaf V obtained from the chain nerve. Precisely, for the presheaf of simplicial sets T↦A_•(T), take the ordinary edge-path groupoid with object set A_0(T) and arrows modulo triangle and degeneracy relations. Sheafify its arrow presheaf; finite-limit preservation gives an internal groupoid in sheaves of sets. Its classifying object is tau_≤1 C, since objectwise groupoid completion followed by sheafification computes the 1-truncated realization. Use the same construction for the hulls. In particular path classes between V-valued endpoints are sheaves; every object of tau_≤1 C is locally represented by a vertex, as is true of the hulls.

**Theorem 1 (rectangle quotient).** Both hull fundamental groupoids, with their object sheaf V, are canonically isomorphic to the quotient of G_X by the normal subgroupoid generated locally by all rectangle loops
\[
r(x,y;u,v)=[x,u][y,u]^{-1}[y,v][x,v]^{-1},\qquad x,y\le u,v.
\]
Here [x,u] denotes a chain edge and paths are multiplied in traversal order. The rectangle parameter is an actual coherent proconstructible sublocale of X^4 given by four specialization inequalities, the object E_{1,1} of our bisimplicial rectangle construction. The quotient is the sheafification of the local quotient by the normal closure of the indicated loops, transported by all paths; equivalently it is the universal internal groupoid on V killing those loops. No set-theoretic global witness section is needed.

**Proof.** Let Q be that quotient. All rectangle loops vanish in the upper hull by its witness triangles, so the canonical chain map factors through Q. Conversely, given a hull edge (x,y) over a test T, pull back along its upper-witness surjection T'→T. Assign the path [x,u][y,u]^{-1} in Q(T'). Two witnesses on the overlap differ by an imposed rectangle, so the paths agree and uniquely descend to an arrow in Q(T). This is natural in T and defines a morphism of edge sheaves. The degeneracy goes to the identity (same path twice); for a chain edge x≤y take witness y, so the assignment is the chain arrow. For an arbitrary upper-hull triangle (x,y,z), pull back to choose a common witness w. The assigned paths satisfy p(x,y)p(y,z)=p(x,z) by cancellation of the middle path. Hence the assignment respects triangle relations and induces an internal groupoid map from the hull to Q. Composites are identities on edge generators, locally and therefore as sheaves. For the lower hull use paths [z,x]^{-1}[z,y]; the resulting lower-witness ambiguity is the same rectangle loop up to cyclic permutation, inverse, and change of basepoint. Thus its quotient is exactly Q as well. This proves the canonical identifications, including the component and epimorphism claims in §1.

**Corollary.** The fundamental-group maps (all local basepoints) are isomorphisms iff every rectangle loop is already trivial in G_X. For finite posets this is an ordinary normal-closure criterion on the fundamental group of the order complex in each component. In the coherent setting the kernel is the normal subgroupoid generated as a sheaf, not necessarily an abstract normal closure in the ordinary group evaluated at every test T. A rectangle with comparable upper witnesses is already trivial by chain triangles; more generally a path of comparable upper witnesses connects the two alternatives. In particular a least common upper witness for each pair (locally) suffices for pi_1-isomorphism; the dual greatest lower witness condition does also. The condition need not imply higher homotopy equivalence: the finite ordinal sum of three two-element antichains has C≃S² and I=D≃1, hence every rectangle loop is trivial but pi_2 is killed. The four-point two-bottom/two-top poset has C≃S¹ and I=D≃1, and its rectangle loop generates pi_1.

## 3. The first relative skeletal layer

For B=B^+ or B^-, let
\[
F_k^B=|\operatorname{sk}_k B|\amalg_{|\operatorname{sk}_k A|}1 .
\]
These are pointed homotopy cofibres of the maps of skeletal realizations; the maps F_k→F_{k+1} give a natural filtration whose sequential colimit is the total comparison cofibre. In degree zero F_0=1. For a coefficient ring R, define the first relative edge module
\[
L_B=\operatorname{coker}(R[A_1]\to R[B_1]).
\]
The notation R[-] is free R-module sheaf. Both simplicial objects have identical degree-zero terms and identical degenerate 1-simplices. Hence normalized relative chains in degree 1 are exactly L_B and the relative degree-zero group vanishes. Thus reduced H_1(F_1^B;R)=L_B, with other reduced homology sheaves zero: skeletal realizations consist of graphs, so their linearized relative complexes are concentrated in degree 1. In degree 2 the relative normalized boundary onto L_B is an epimorphism: locally choose a witness for each edge and use its witness triangle; its two chain edges vanish in the quotient. Consequently the induced map H_1(F_1^B)→H_1(F_2^B) is zero, and H_1(F_2^B)=0. The full relative chain complex starts at degree 1 with surjective degree-2 differential. These claims follow by applying the normalized chain construction to the sheafified simplicial free modules. All edge and triangle equalities are actual sheaf morphisms and witness maps are effective epis.

**Caution:** A_1⊂B_1 is generally a closed inclusion after Patch, not clopen. Its set-theoretic complement need not be compact/Stone. Do not assert L_B is represented by a Stone complement or that F_1 is literally a wedge indexed by such a complement. At the terminal test point *, which preserves the relevant limits and colimits, L_B(*) is the free module on the extra ordered edges and F_1(*) is a bouquet of that many circles. The ordered edge counts include the reverse of every strict chain comparison: this symmetric excess is distinct from the genuinely incomparable pairs. An endpoint-labelled presentation R[A_1]→R[B_1]→R[V×V], rather than the bare quotient module, keeps the actual binary relation labels.

## 4. The triangle-face-poset Stone-indexed benchmark

Let P=F(∂Δ²) (three vertices and three edges), choose v=v_0 minimal, and W=W_S(P,v) be the audited pointed gluing with S nonempty Stone. Set M=R[h(S)], N=R[h(S×S)] and Q=coker(M→N) along the diagonal S→S×S.

Each fibre has six strict chain comparisons. The upper-hull adds six reversed comparisons and six ordered pairs of distinct vertices joined by an edge. All such pairs stay in one fibre. The lower-hull adds six reversed comparisons and six ordered pairs of distinct maximal edges meeting in a vertex per fibre; additionally across fibres any two maximal edges incident to v have common lower witness v.

Thus for |S|=m finite:
\[
|W|=1+5m,\quad |\operatorname{Ch}_1\setminus\Delta|=6m,
\quad |I_1\setminus\operatorname{Ch}_1|=12m,
\quad |D_1\setminus\operatorname{Ch}_1|=12m+4m(m-1).
\]
The strict binary incomparable parts have |I_1\D_1|=6m and |D_1\I_1|=6m+4m(m-1). The finite counts were verified by enumerating all ordered pairs and all witnesses for m=1,2,3,4 (respectively upper extra counts 12,24,36,48 and lower counts 12,32,60,96).

**Theorem 2 (first relative edge modules).** For arbitrary nonempty Stone S,
\[
L_{B^+}\cong M^{\oplus12},\qquad
L_{B^-}\cong M^{\oplus10}\oplus N^{\oplus2}\oplus Q^{\oplus2}.
\]
Proof of lower formula: separate the four ordered label blocks of pairs of the two maximal edges incident to the shared v. Each block is S×S in the lower hull. In the two same-label blocks the chain relation meets the block along the diagonal, contributing Q each. In the two distinct-label blocks no pair is a chain, giving N each. The remaining extra edges are ten clopen S-labelled pieces: six reversed strict comparisons plus four ordered pairs of distinct maximal edges meeting at either of the other two vertices. All decompositions used here are clopen by the finite labels, with the diagonal inclusion in the same-label blocks handled as a genuine cokernel. For the upper formula the extra pairs form twelve clopen S-labelled components by the previously audited fibrewise I_n gluing. This proves the formulas without treating the off-diagonal of S×S as a compact Stone space.

The formulas also exhibit the difference between the two first relative skeletal layers at point evaluation for finite m≥2, even though total cofibres are both terminal by the audited canonical-equivalence theorem for the pointed gluing. For infinite S we do NOT infer nonisomorphism of the unmarked edge modules just from infinite ranks; the displayed labelled decompositions show where the cross-fibre contributions occur. In fact each module is nonconstant for infinite S, via its direct summand M and the identity-section infinite-image criterion.

## 5. Why rectangles vanish in this example; broader feedback

In W every pair with a common upper witness has a least upper witness. If both points are in one fibre, take the union of their faces (when a common upper face exists). If the common shared v is involved the same argument applies; if both points equal v, take v. Nonshared points in distinct fibres cannot have an upper witness. The least upper witness is below all upper witnesses, so all rectangle loops are already trivial by chain triangles. This explains the pi_1 result without appealing to the full comparison theorem. It is the same mechanism for every finite face poset. This least-witness argument is pointwise in W but suffices locally for the internal assertion: to choose a common least witness over test T, first pull back along the finite-surjection Stone cover by the finitely many closed tuple-label/order strata with a specified witness formula; in this particular upper-hull wedge the tuple strata are already clopen copies of S or the common vertex. More generally do not assume pointwise least witnesses give continuous maps on an arbitrary coherent locale.

The extra binary pairs themselves are therefore not the obstruction to pi_1; it is the **rectangle relations between alternative witness paths**. Even when these vanish, higher-dimensional obstructions may remain. The first relative filtration detects the binary excess, and its degree-two differential explains why that excess disappears in H_1. This directly links the original binary relation hierarchy to the rectangle E_{1,1} and to the first two skeletal degrees.

## 6. Next bounded direction

The roadmap still includes U,V,W,H and composition. A concrete next test is to calculate the remaining **binary** named relations on this W_S(P,v) family from the established frame definitions, including the effects of off-diagonal S×S in Patch versus spectral topology. The rectangle criterion may also be compared with I∘I and U (in the precise coherent sense already proved in earlier work), but no equivalence with binary composition identities is claimed here. A subsequent independent audit should cover the sheaf groupoid quotient proof and relative skeletal module calculations, together with other post-third-audit segments. No new audit undertaken in this segment.
