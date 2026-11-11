# Binary feedback III — Fixed hierarchy and formal-hull rank, arbitrary finite homotopical comparison obstructions

**10 November 2026. New internally checked working mathematics; NOT externally audited.** Reverses the question from [Binary feedback II](PointFree_binary_triangle_hierarchy_formal_hull_rank_2026-11-10.md): how much can the canonical homotopy comparisons vary while the named binary hierarchy has a fixed equality/strict-inclusion pattern? The answer below is strong: the whole displayed triangle hierarchy, formal-hull rank 2, and both nonconstant hull realizations can be fixed, with the chain-to-hull arrows varying over arbitrary connected finite simplicial homotopy types. In particular, identical binary hierarchy patterns and terminal comparison cofibres do not force identical equivalence status. Uses the [canonical coherent composition calculus](ProjectA_coherent_composition_canonical_proof_2026-11-08.md), the [audited pointed Stone-indexed gluing and edgewise arrow theorem](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md), and the working calculations of Binary feedback II. No priority, site-size-independence, or intrinsic-localic-shape claim.

## 0. A universal finite-poset gadget

Let K be a nonempty connected finite simplicial complex. Choose a spanning tree L of its 1-skeleton and a vertex k0 of L. Allow K to be a singleton (then L is a singleton). Put
\[
P_K=F(K)^{op},\qquad U_L=F(L)^{op}\subseteq P_K,
\]
where F denotes the poset of nonempty faces. The maximal elements of P_K are the vertices of K. The subset U_L is an upset in P_K, since L is a simplicial subcomplex; it contains all those maximal points.

Adjoin a new minimal point v with v≤x precisely for x∈U_L, apart from reflexivity at v. Call the resulting finite poset Q_K. This is a poset because U_L is an upset.

**Lemma 1 (finite obstruction gadget).** The pointed chain realization at v has the homotopy type of (|K|,k0), whereas both hull realizations of Q_K are terminal. In particular the canonical maps are equivalent to |K|→1.

Proof. The ordinary order complex is the union
\[
\operatorname{Ord}(Q_K)=\operatorname{Ord}(P_K)\cup_{\operatorname{Ord}(U_L)}
\bigl(v*\operatorname{Ord}(U_L)\bigr).
\]
Reversal of order preserves the underlying order complex; the latter face-poset order complexes are the subdivisions of K and L, compatibly with inclusion. This is a pushout of simplicial subcomplexes, hence a homotopy pushout on realization. Since L is a tree, it is contractible. Attaching its cone leaves the original homotopy type unchanged. More precisely a contraction of |sd L| to k0 yields a map from the cone back to |sd L| fixing its base, and taking v to k0. The resulting retraction of |Ord(Q_K)| onto |sd K| is a pointed weak equivalence with the specified basepoints (as a map from v to k0). Thus C(Q_K)≃constant |K| pointed at v.

All maximal points of Q_K lie above v. Given a tuple in I_n(Q_K), extend its common upper witness to a maximal point m; since v≤m, inserting v still gives a tuple in I_{n+1}(Q_K). Insertion at the beginning is the standard extra degeneracy, including the augmentation and its section v. Therefore I(Q_K)≃1. The previously audited canonical edgewise comparison under C(Q_K) identifies the I and D arrows, so D(Q_K)≃1 as well. All arguments for these finite objects apply to constant sheaf realizations. QED.

This improves the previous ordinal-sum obstruction construction: not only suspensions but **every connected finite simplicial homotopy type** occurs as the chain realization of a finite poset with terminal hull realizations. The construction uses the reversed face order essentially: the spanning tree supplies an *upset* containing every maximal point.

## 1. Fixed nonconstant target, variable canonical arrow

Let P_triangle be the six-point triangle-boundary face poset with shared minimal vertex v and other labels a,b,p,q,r as in Binary feedback II. Form a finite poset
\[
P(K)=P_\triangle\vee_v Q_K
\]
by identifying the two indicated minimal vertices, with no comparisons between nonshared points of different pieces. Fix a Stone space S with at least two points (take S infinite for genuine nonconstancy), and let
\[
X_K=W_S(P(K),v).
\]
It is Priestley with its disjoint-union patch topology and hence defines a coherent locale. For S Cantor, K(X_K) is countable, by the audited compact-open description of finite pointed gluing.

**Lemma 2 (canonical wedge-collapse arrow).** Set
\[
E_S=h(S)_+\wedge\underline{S^1},\qquad
Y_{S,K}=h(S)_+\wedge\underline{|K|},
\]
using k0 as basepoint. Then both canonical pointed arrows C(X_K)→I(X_K) and C(X_K)→D(X_K) are equivalent, as arrows, to
\[
\boxed{E_S\vee Y_{S,K}\xrightarrow{(\mathrm{id},*)}E_S.}\tag{1}
\]
Proof. Any chain or common-upper tuple in P(K) with a nonshared coordinate belongs entirely to its piece, with v allowed, because v is minimal and an upper witness of a nonshared coordinate stays in its piece. The degreewise chain and upper-hull simplicial sets are thus wedge pushouts along the constant-v simplicial point. Realization gives C(P(K))≃C(P_triangle)∨C(Q_K) and I(P(K))≃I(P_triangle)∨I(Q_K), with the *canonical map* induced by the wedge of the canonical maps on the pieces. The audited face-poset criterion makes the triangle comparison a pointed equivalence of circle homotopy types. Lemma 1 identifies the Q_K comparison with |K|→1. Apply the already audited pointed Stone-indexed gluing theorem C(W)≃h(S)_+∧C(P), I(W)≃h(S)_+∧I(P) compatibly with the arrow. Smash preserves pointed colimits, including wedges. The canonical edgewise arrow theorem gives (1) for D as well; its equivalence under C can be regarded as pointed using the image of the shared vertex. This does NOT claim fibrewise gluing of D_n. QED.

The target E_S is genuinely nonconstant for infinite S by the audited calculation of its H_1=Z[h(S)]. The chain source retracts onto it, hence the displayed sources are also nonconstant for infinite S.

## 2. Exactly the fixed displayed binary hierarchy

**Theorem 3.** For every K above and fixed S of cardinality ≥2, the named relation equality and strict-inclusion pattern in the Hasse diagram of Binary feedback II is exactly preserved:
\[
\Delta< M< I,D< J< T(J)=U\wedge V< U,V< U\vee V<\operatorname{cl}V< H=F=\operatorname{fit}U=X_K^2,
\]
with I∥D and U∥V, W=U, and all shown inequalities strict. The scope is the displayed named relations; it does not assert equality of cardinalities, isomorphism of underlying binary relations, or preservation of additional identities such as M=symmetric comparability (the latter can fail for the new larger posets).

Proof. Let X_0 denote the original pointed triangle wedge over S. Its inclusion j:X_0→X_K and retraction r:X_K→X_0 collapsing each attached piece to v are continuous on Patch and order preserving, hence spectral. They satisfy rj=id. In coherent locales the displayed finite relations I,D,U,V,cl V,fit U are given by finite positive existential order formulas (using the established proconstructible calculus), and M,J,T(J),U∨V by finite intersections and unions, with T(J)=U∧V. Each formula is preserved by an order-preserving map. Thus on old points the restrictions of all these new relations agree with the old ones: apply j in one direction, r in the other. In particular every strictness witness in the old Hasse pattern still witnesses strictness, and every incomparability witness survives. The positive inclusions are the already established general coherent ones (not deduced from retraction alone). For the top equality: every minimal point of X_K is I-related to v. In the triangle this follows from the two incident edges; in Q_K even every point is I-related to v, because all maximal points are above v. Every point lies above a minimal point. Therefore any two points have lower extensions a,b with a I v I b, so the pair (a,b) lies in U=I² and the original pair lies in fit U=↑U. Hence fit U=X_K². Since H contains fit U and H⊆F, both H and F are X_K². This uses actual localic equalities: the finite named relations are proconstructible, and fit U is among these. Thus the complete specified pattern is fixed. QED.

Optional strengthening if one wishes to include the symmetric comparability relation as an additional node: attach the same four-element diamond (bottom v, two incomparable middle points, one top) to P_triangle before adjoining Q_K, in all examples. Its chain and both hull realizations are contractible (it has greatest and least elements), all its points are I-related to v, and it witnesses strict symmetric comparability<M. The triangle still witnesses the other strictnesses by retraction. This gives a fixed expanded pattern including Δ< symmetric comparability<M, not the original triangle equality M=symmetric comparability.

## 3. Formal-hull rank also stays exactly 2

The original triangle opposite edge r has I-distance two from v. Every Q_K point has I-distance at most one from v. No new I path can reduce the old triangle distance, by folding retraction. Hence v has eccentricity two in the I-graph on P(K).

For S with at least two points, every cross-fibre I path passes through the shared v. The I-distance between opposite edges r_s and r_t in distinct fibres is therefore four; every pair of points has distance at most four. By the previous odd-power closed-stage formula the iteration is
\[
C_0=I,\quad C_1=I^3\subsetneq X_K^2,\quad C_2=I^5=X_K^2=H.
\]
The first fixed closed stage is exactly 2, independent of K. This is the alternating closure-fitting rank, NOT the noncoherent W_2 question.

## 4. Consequences of the explicit arrow formula

Its pointed homotopy cofibre is
\[
\boxed{\operatorname{cofib}(\mathbf C(X_K)\to\mathbf I(X_K))
\simeq\operatorname{cofib}(\mathbf C(X_K)\to\mathbf D(X_K))
\simeq\Sigma_{\rm red}Y_{S,K}
\simeq h(S)_+\wedge\underline{\Sigma_{\rm red}|K|}.}
\tag{2}
\]
Indeed the cofiber of E∨Y→E with restriction id on E and constant on Y is Σ_red Y by pushout cancellation in pointed objects. Smash commutes with suspension. A cofiber does NOT in general determine whether the arrow was an equivalence.

- **Trivial obstruction:** take K a point or a contractible tree. Both canonical comparisons are equivalences with target E_S.
- **Arbitrary positive-degree homological obstruction:** take K a finite triangulation of S^n, n≥1. The map on degree-n integral homology has kernel M_S=Z[h(S)] (nonconstant for infinite S), with no other homological kernel in positive degrees. The cofiber is h(S)_+∧S^{n+1}. For n≥2 the π_1 sheaf map is an isomorphism (pointwise pointed wedges before sheafification and then truncation), while nontrivial homotopy is lost; at point evaluation the added sphere summand retracts. For n=1, both source and target are classifying objects of free group sheaves, and projection kills the second indexed family of circle generators.
- **More general connected finite complexes:** the homological kernel is computed by the reduced chain complex M_S⊗^L C̃_*(K;Z); over a field k it is R[h(S)]⊗_k H̃_*(K;k) with R=k. This allows torsion and multiple-degree obstructions. All connected finite simplicial homotopy types occur as the added finite building block; for any noncontractible K, Y_{S,K} is nonterminal since K is a retract of its point evaluation (S nonempty). The collapse map cannot be an equivalence: on point evaluation the inclusion of Y is a split monomorphism in the homotopy category (it admits a retraction collapsing E), but becomes null under the projection. No claim that arbitrary sheaf homotopy types occur.
- **Non-equivalence with terminal cofiber:** take K a connected finite integral-acyclic noncontractible simplicial complex, for example the finite simplicial model of Higman's presentation complex used in [the acyclic construction](PointFree_relative_chain_splitting_acyclic_aspherical_nonconstant_2026-11-10.md), or the balanced binary icosahedral presentation complex there. A connected acyclic finite complex has contractible reduced suspension (simply connected by van Kampen, acyclic by suspension homology, hence contractible by Hurewicz and Whitehead). By (2) both comparison cofibres are terminal, yet the arrows are not equivalences. Indeed the point-evaluated chain π_1 is the free product of the original indexed free circle group and the copies of π_1(K) indexed by S_set; projection kills the latter. Ordinary homology sheaf maps are isomorphisms: reduced chains of K vanish. In the Higman case the killed subgroup is nontrivial despite H having no finite quotients. Both this example and the K=point example share the exact displayed binary pattern, rank two, target E_S, and terminal cofibres, but differ in equivalence status.

The last contrast reinforces the earlier audited warning that equivalence of cofibres is strictly weaker than equivalence of the canonical arrows.

## 5. Finite controls actually performed

Exhaustive JS Boolean relation-matrix checks were run for finite K a point, an interval, a triangle boundary, and the tetrahedron boundary, for two and three outer fibres. The order was built with a spanning tree, I=A B and D=B A using the specialization matrix and its transpose; U=I², V=D², cl V=I³, fit U=D³, etc. Every strict inclusion, both incomparabilities, I³ proper and I⁴=fit U=full passed. The numbers of points (two/three fibres) were 13/19, 17/25, 23/34, 39/58 respectively. This is only a finite control, not a proof of the arbitrary-Stone assertions.

## 6. Interpretation and boundary

The previous direction showed fixed nonconstant canonical comparison diagrams with arbitrarily large finite formal-hull ranks. This reverse direction fixes the **whole displayed named hierarchy**, exact rank, and nonconstant targets, but allows arbitrary connected finite building-block homotopy obstructions, including acyclic ones invisible even to cofibres and ordinary homology. Thus neither coarse hierarchy equality data nor unfiltered homotopy data controls the other in general.

Next stronger question, left open: can one fix the actual binary relation structures (or e.g. the I,D pair up to a simultaneous isomorphism of the underlying patched set), not merely their Hasse pattern, and still vary the canonical higher-arity comparison? Another direction is to study relative distance- or arity-filtrations. These are not needed for the present result. This note is working, not externally audited. The prior audited gluing, edgewise and composition results are used explicitly; the new spanning-tree construction, retraction proof and comparison classification should be covered in a future independent audit along with the preceding post-audit segments.
