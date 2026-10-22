# Spatial two-map targets collapse to diagonal for Hausdorff X

Date 22 October 2026.

Let X be a Hausdorff topological space, L=O(X), and M=O(Y) a spatial frame (take Y sober if desired). Suppose f,g:L→M are frame homomorphisms satisfying cross-disjointness: a∧b=0 ⇒ f(a)∧g(b)=0. Then f=g.

Proof: For each point y of Y, compositions ev_y f, ev_y g are frame homomorphisms O(X)→2, hence correspond to points x_f(y),x_g(y) of X (Hausdorff spaces are sober). If they differ, Hausdorffness yields disjoint neighborhoods a of x_f(y), b of x_g(y). Then y belongs to f(a)∧g(b), contradicting cross-disjointness. Thus the points agree for each y and f(a),g(a) have the same point set in spatial Y, so f=g.

It follows [f,g](w)=f(μ(w)), where μ:L⊕L→L is the diagonal homomorphism. Hence if μ(w)=1, EVERY such spatial-target two-map test gives 1, regardless of whether d∨w=1 in L⊕L. All non-diagonal information in the universal two-map characterization requires NONSPATIAL targets (unless the source locale has additional separation properties that force all f=g).

Consequence: the ideal completion Idl(L) of the underlying distributive lattice of L is spatial (assuming the usual prime ideal theorem; prime filters separate distinct ideals), so using M=Idl(L) as the proposed two-map target cannot exploit more than the diagonal condition for Hausdorff spatial X. This is a no-go for a naive ideal-completion witness built directly from G_w. This does NOT rule out more sophisticated pointless quotients or constructions from ideals which are nonspatial.

Distinguish Hausdorff as a topological space from localic separation. The rational-bridge examples are Hausdorff spatial locales but their nonspatial products retain structure invisible to point evaluations. The universal test M=↑d can be nonspatial and detects the full bar equation.

Status: This is a genuine restriction on two-map target search, not a proof or disproof of universal depth three.
