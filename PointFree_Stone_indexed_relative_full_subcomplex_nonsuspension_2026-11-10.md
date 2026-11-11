# Point-Free Topology — Nonsuspension common-hull homotopy from Stone-indexed gluing along full subcomplexes

**10 November 2026 · NEW internally checked research segment, NOT externally blind-audited.** Motivated by the third referee's [post-report question](audits/2026-11-10/postaudit-sheaf/Referee_report_original.md): coherent locales \(X\) with **both canonical** comparisons \(\mathbf C(X)\to\mathbf I(X)\), \(\mathbf C(X)\to\mathbf D(X)\) equivalences, whose **nonconstant shared sheaf-homotopy object is NOT a suspension nor an indexed wedge of spheres**. This note proves a stronger construction: Stone-indexed gluings of **arbitrary finite simplicial pairs** and an explicit torus-along-essential-circle example that is **not a wedge of any family of finite CW complexes**, even after evaluating at the terminal Stone point. It uses the previously independently audited [A1–E3 canonical account](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md), most notably the canonical finite face-poset comparison and the coherent edgewise arrow theorem; the present **extension to gluing along a non-singleton lower ideal has not been audited**. No literature-priority or intrinsic-localic-shape claim.

## 0. Ambient conventions

Let \(\mathscr H_\kappa=\operatorname{Shv}_\infty(\operatorname{Stone}_\kappa,\text{finite jointly surjective covers})\), including finite limits/coproducts and the empty cover of the empty locale. Choose κ sufficiently large, and let \(h(S)\) be the represented sheaf of a Stone space S. Constant homotopy types carry an underline. A coherent locale X has the localic specialization relation defined from all frame opens (equivalently compact opens when X is coherent), chain simplicial locale \(\operatorname{Ch}_\bullet(X)\), higher closed and fitted diagonal hulls \(I_\bullet(X),D_\bullet(X)\), and patched realizations \(\mathbf C(X),\mathbf I(X),\mathbf D(X)\). **Everything below concerns patched sheaf homotopy, not intrinsic shape.**

A **lower ideal** \(A\subseteq P\) of a finite poset is downward closed. Call \(A\) **upper-witness reflective in P** if
\[
\tag{WR}
I_n(P)\cap A^{n+1}=I_n(A)\qquad\text{for every }n\ge0,
\]
where finite \(I_n\) consists of tuples having a common upper bound. The condition does NOT follow from downward closure alone. For example, two vertices of a non-full subcomplex may acquire an edge as upper witness in P which is absent in A. It is necessary for the simple fibrewise closed-hull gluing below.

## 1. Generalized Stone-indexed gluing theorem

**Definition.** For a finite poset P, a nonempty **lower ideal** A satisfying (WR), and a nonempty Stone space S, put
\[
W_S(P,A)=A\sqcup\bigl(S\times(P\setminus A)\bigr)
\]
as a disjoint-union Stone space. The order restricts to P within each s-fibre (with the A part shared across fibres), and gives **no comparisons between non-A coordinates of distinct fibres**.

The lower-ideal condition makes this order transitive: no point outside A can lie below an A-point, so no chain can travel from one fibre through A to another. The order graph is patch-closed (finite union of comparisons involving A, and copies of the closed diagonal \(\Delta_S\) for non-A/non-A comparisons). For Priestley separation, noncomparable points in distinct fibres can be separated by a clopen subset V⊂S and the finite upset ↑x of P; ↑x is disjoint from A for x∉A. The same construction handles (s,x)≰a for a∈A. For a≰(s,x) use the **global** finite upset ↑a of P (with its A values identified). Thus \(W_S(P,A)\) is Priestley and determines a coherent locale X.

**Explicit bounded distributive lattice:** with \(L=\mathrm{Ups}(P)\) and \(\mathrm{LC}(S,L)\) the locally constant functions to finite discrete L,
\[
\boxed{K(X)\cong\{f\in\mathrm{LC}(S,L): f(s)\cap A\text{ is independent of }s\in S\}.}
\]
This is a bounded distributive sublattice of LC(S,L) under pointwise joins/meets; its clopen upsets are exactly those of W. If S is Cantor, K(X) is **countable** because Clop(S) is countable and L finite.

**THEOREM 1 (full lower-ideal gluing; new internally proved).** For all n≥0 there are natural strict Stone-locale identifications
\[
\operatorname{Patch}\operatorname{Ch}_n(X)
\cong\operatorname{Ch}_n(A)\sqcup\bigl(S\times(\operatorname{Ch}_n(P)\setminus\operatorname{Ch}_n(A))\bigr),
\]
\[
\operatorname{Patch}I_n(X)
\cong I_n(A)\sqcup\bigl(S\times(I_n(P)\setminus I_n(A))\bigr).
\]
Consequently
\[
\boxed{
\mathbf C(X)\simeq
\mathbf C(A)\mathop{\amalg}\limits_{h(S)\times\mathbf C(A)}
\bigl(h(S)\times\mathbf C(P)\bigr),
}
\]
\[
\boxed{
\mathbf I(X)\simeq
\mathbf I(A)\mathop{\amalg}\limits_{h(S)\times\mathbf I(A)}
\bigl(h(S)\times\mathbf I(P)\bigr).
}
\]
The canonical arrow \(\mathbf C(X)\to\mathbf I(X)\) is **exactly** the induced map between these homotopy-pushout diagrams. Therefore, **if the finite canonical maps C(A)→I(A) and C(P)→I(P) are equivalences, then the canonical C(X)→I(X) is an equivalence**. The previously independently audited coherent edgewise theorem then gives the same conclusion for canonical C(X)→D(X). No *degreewise* decomposition of D_n(X) is claimed: lower witnesses can join different fibres.

**Proof:** (1) Every chain with at least one coordinate outside A has all its outside-A coordinates in exactly one s-fibre; because A is a lower ideal, it cannot re-enter A after leaving it. Conversely a P-chain in any fibre yields a W-chain. (2) Every common-upper tuple with a coordinate outside A has upper witness in a unique s-fibre, hence lies within that fibre. A tuple entirely in A belongs to I_n(W) iff it has some upper witness in P: (WR) is **exactly** what says this is equivalent to its belonging to I_n(A). This proves the point-set decompositions. The higher-hull domains are actual coherent **proconstructible spectral sublocales** and their Patch are Stone; all displayed finite tuple-type strata are clopen Stone components, so the decompositions identify the actual patched locales, not just naked point sets. (3) Face/degeneracy maps either keep the S-coordinate or send a tuple wholly into A, collapsing S, so strict simplicial naturality holds. (4) In each degree the square
\[
\begin{array}{ccc}
S\times\operatorname{Ch}_n(A)&\to&S\times\operatorname{Ch}_n(P)\\
\downarrow&&\downarrow\\
\operatorname{Ch}_n(A)&\to&\operatorname{Patch}\operatorname{Ch}_n(X)
\end{array}
\]
(and I-version) is a pushout **along a clopen coproduct summand**. Yoneda preserves the finite coproduct/product decomposition, so it is also a **homotopy** pushout of sheaf objects; realize degreewise and commute colimits. Naturality of the canonical Ch→I inclusion identifies the induced arrow. Objectwise equivalences on A and P induce a pushout equivalence. QED.

**Warning about a potentially tempting false generalization:** A merely downward-closed ideal A which is not (WR) need not make I_n glue like Ch_n. For example, A is the downward ideal of two vertices with no edge while P adds an edge connecting them. The tuple (a,b) is in I_1(W), with upper witness in **any fibre**, but is not in I_1(A); treating the resulting shared tuple as separately indexed by S yields the wrong Stone pushout.

## 2. Arbitrary finite simplicial pairs: universality of canonical comparisons

**LEMMA 2.** Let \(K\subseteq T\) be a nonempty **full (induced) simplicial subcomplex** of a finite simplicial complex T. Set \(P=F(T)\) and \(A=F(K)\), the posets of nonempty faces. Then A is a lower ideal and is upper-witness reflective in P.

**Proof:** A is downward closed under taking nonempty subfaces. A tuple of faces \(\sigma_i\in A\) has a common upper face of T iff its union \(\bigcup_i\sigma_i\) is a face of T. Because every vertex of that union belongs to K and K is induced, the union face lies in K, furnishing an upper witness in A. QED.

**LEMMA 3 (make any simplicial pair full).** For **every** finite simplicial pair K⊆T, the barycentric subdivision \(\operatorname{sd}K\) is a **full** subcomplex of \(\operatorname{sd}T\): its vertices are the nonempty faces of K, and a simplex in sd T is a chain of such faces; if all vertices of that simplex belong to sd K, the entire chain is a simplex of sd K. Thus Lemma 2 applies after one subdivision without changing either homotopy type or inclusion homotopy type.

For **every** finite simplicial complex T, its face poset F(T) satisfies the previously independently audited canonical finite crosscut hypothesis: intersections of maximal facet downsets are either empty, or \(\downarrow(\bigcap \text{facets})\) with a greatest element. The hypothesis applies to **nonempty intersections only**. Therefore the canonical Ch→I map for both F(T) and F(K) is a weak equivalence, naturally with respect to their inclusion; the edgewise theorem also gives C→D.

**THEOREM 4 (parametrized-pair universality; internally proved).** For every finite simplicial pair K⊆T, after replacing it by one barycentric subdivision, and every nonempty Stone S, there is an explicit coherent locale \(X(S;T,K)\) such that **both canonical maps C(X)→I(X), C(X)→D(X) are equivalences**, with common sheaf-homotopy object
\[
\boxed{
\mathcal E_{T,K}(S):=
\underline{|K|}\mathop{\amalg}\limits_{h(S)\times\underline{|K|}}
\bigl(h(S)\times\underline{|T|}\bigr).
}
\]
This is the **derived** pushout in the Stone-sheaf ∞-topos, with left map projection and right map induced by K⊆T. For K a single vertex, we recover the earlier **indexed pointed wedge** \(h(S)_+\wedge\underline{|T|}\). For nontrivial K, the new object is generally **not** an indexed wedge. The existence of a single finite relative pair (T,K) with interesting gluing provides an entire coherent nonconstant family.

The statement applies to disconnected T,K if K is nonempty, but the examples below use connected finite complexes.

## 3. Concrete nine-vertex torus and a full essential-circle subcomplex

Use the **3×3 periodic square grid**. Its vertices are \((i,j)\in(\mathbb Z/3)^2\). For every (i,j) include the two triangles
\[
\bigl\{(i,j),(i+1,j),(i+1,j+1)\bigr\},
\qquad
\bigl\{(i,j),(i,j+1),(i+1,j+1)\bigr\},
\]
with indices mod 3, and all their faces. This is a finite triangulation T of the torus \(\mathbb T^2=S^1\times S^1\). It has **9 vertices, 27 edges, 18 triangles**, and Euler characteristic 0.

Let K be the full subcomplex on the three vertices \((0,0),(1,0),(2,0)\). It has exactly **three edges and no triangles**, hence K≅S¹ and is the horizontal essential circle \(S^1\times\{*\}\) in T. It is **already full**: no triangle of T lies entirely on one row.

Take P=F(T), A=F(K). Then |P|=9+27+18=54 points, |A|=3+3=6, and the Stone parameterization X(S;T,K) has Priestley patch space
\[
A\;\sqcup\;\bigl(S\times(P\setminus A)\bigr)\cong 6\sqcup(48\times S).
\]
For S=Cantor the compact-open lattice is countable, by the explicit formula in §1.

**THEOREM 5 (nonconstant, nonsuspension, non-wedge example).** For any nonempty Stone S, the two canonical comparisons for this coherent X are equivalences, with
\[
\begin{aligned}
\mathbf C(X)&\xrightarrow{\sim}\mathbf I(X),\qquad
\mathbf C(X)\xrightarrow{\sim}\mathbf D(X),\\
\boxed{\quad
\mathbf C(X)\simeq\mathbf I(X)\simeq\mathbf D(X)
&\simeq
\underline{S^1}\times\bigl(h(S)_+\wedge\underline{S^1}\bigr)
\simeq B\bigl(\underline{\mathbb Z}\times\operatorname{Fr}(h(S))\bigr).\quad}
\end{aligned}
\]
The first formula is Theorem 4 for (T,K). Its identification with a product follows from the **homotopy equivalence of pairs** \((|T|,|K|)\cong(S^1\times S^1,S^1\times\{*\})\) and the fact that product with \(\underline{S^1}\) preserves homotopy pushouts in an ∞-topos. The equivalence \(h(S)_+\wedge\underline{S^1}\simeq B\operatorname{Fr}(h(S))\) was independently reasoned following the third audit and is the standard internal wedge-of-circles computation.

Hence the common realization is an **aspherical pointed 1-type** with
\[
\boxed{\pi_1\simeq\underline{\mathbb Z}\times\operatorname{Fr}(h(S)),\qquad
\pi_j=0\quad(j>1),}
\]
and reduced/ordinary homology sheaves
\[
\boxed{\mathcal H_1\simeq\underline{\mathbb Z}\oplus\mathbb Z[h(S)],
\qquad
\mathcal H_2\simeq\mathbb Z[h(S)]}
\]
(with H₀=Z and H_i=0 for i>2). Derive these directly from the cellular chain model S¹×(indexed wedge of S¹) with one 0-cell, one constant 1-cell, one \(h(S)\)-indexed family of 1-cells, and an \(h(S)\)-indexed family of product 2-cells, all cellular boundaries zero. This avoids any unproved flatness assumption for arbitrary condensed abelian sheaves.

**Nonconstancy:** For infinite S, \(M_S=\mathbb Z[h(S)]\) is a nonconstant condensed abelian sheaf by the externally verified section \([\operatorname{id}_S]\in M_S(S)\), with infinitely many point-values \([s]\). Therefore H₂ of the common object is nonconstant, and so is the entire object.

**Not a suspension, at the sheaf level:** Evaluation at the terminal Stone point * preserves colimits and finite products on this site (the only covering sieve of * splits), so
\[
\mathcal E_{T,K}(S)(*)\simeq S^1\times\bigvee_{s\in S_{\rm set}}S^1.
\]
Choose any \(s_0\in S\); the inclusion of its torus factor has a **retraction** induced by folding all S-indexed circles onto one fixed circle. Thus \(\mathbb T^2\) is a retract, and its two degree-one classes have a **nonzero cup product** in H² of the entire space. In particular \(H^{>0}\) has nontrivial products (already with \(\mathbb F_2\) coefficients). But every suspension has zero products of positive-degree reduced cohomology classes, as does every wedge of spheres. Since point-evaluation preserves suspensions, **the sheaf object cannot be a suspension or a wedge of spheres**.

**In fact, it is not an indexed wedge of ANY family of finite connected CW complexes** when S is infinite. Its global-point-evaluation fundamental group is
\[
\boxed{\pi_1(\mathcal E(*))\cong\mathbb Z\times F(S_{\rm set}),}
\]
where F(S_set) is a free group on the infinite set of points of S. This group has **nontrivial center** (the first Z factor) and is **not finitely generated**. For any wedge \(\bigvee_i Y_i\) of finite connected CW complexes, its π₁ is the free product \(*_i\pi_1(Y_i)\) of finitely generated groups. If ≥2 factors are nontrivial, the center of that free product is trivial. If at most one factor is nontrivial, the group is finitely generated. Both alternatives contradict \(\mathbb Z\times F(S_{\rm set})\). Thus the pointwise homotopy type, and therefore the sheaf object, cannot be an indexed wedge of finite CW complexes. This is strictly stronger than the referee's requested “not indexed wedge of spheres” criterion.

**Independent explicit finite computational check:** The 3×3 periodic grid has \((f_0,f_1,f_2)=(9,27,18)\). Over \(\mathbb F_2\), boundary matrices have ranks \(\mathrm{rk}\,\partial_1=8\), \(\mathrm{rk}\,\partial_2=17\), hence Betti \((1,2,1)\). The horizontal row K has \((3,3,0)\). Let α(e)=1 iff e crosses the **horizontal coordinate** seam {i=0,i=2}, and β(e)=1 iff e crosses the **vertical coordinate** seam {j=0,j=2}; otherwise 0. Both are 1-cocycles modulo 2. Using global lexicographic vertex ordering, the Alexander–Whitney cup α∪β evaluates to 1 on the mod-2 fundamental 2-cycle (the sum of all 18 triangles), with the single nonzero contribution the ordered triangle \(((0,0),(2,0),(2,2))\). Thus the nonzero cup product can be verified without appealing only to the standard torus cohomology ring.

## 4. Broader consequences and further experiments

1. **Relative pair universality** is the most substantive conceptual outcome: **every finite simplicial pair**, after one barycentric subdivision, gives a canonical-equivalence coherent locale with a nonconstant sheaf pushout over any infinite Stone S. This extends pointed Stone-indexed wedges, not just by changing the finite homotopy type but by allowing **identification along an arbitrary noncontractible subcomplex**.
2. A closed orientable surface \(\Sigma_g\) of genus g≥2 and an embedded essential nonseparating circle K also fit Theorem 4 after subdivision. The common object is an S-indexed homotopy amalgam of copies of \(\Sigma_g\) along K. The torus's accidental product splitting need not persist; nontrivial positive-degree cup products still survive by the fold retraction to one surface, and H₂ contains the nonconstant sheaf M_S. Group-theoretic analysis of its amalgamated fundamental group would be a useful independent test if this becomes a principal example.
3. In the torus example, the full \(\pi_1\)-sheaf is \(\underline{\mathbb Z}\times\operatorname{Fr}(h(S))\) and is nonconstant, yet **aspherical**. This is a new flavor alongside our previous sphere-like higher-homotopy examples: the important information is in a nonsimple, nonfree fundamental-group sheaf and its nonzero cup products.
4. For a more complicated pair T,K the sheaf object is \(\underline{|K|}\amalg_{h(S)\times\underline{|K|}}h(S)\times\underline{|T|}\). The relative reduced homology chain complex is \(M_S\otimes_{\mathbb Z}C_*(T,K;\mathbb Z)\), even if torsion introduces extensions. Do **not** replace this by \(M_S\otimes H_*(T,K)\) without an appropriate flatness or torsion-free-splitting argument.
5. The construction does **not** compute intrinsic localic shape, does not address Stone site-size independence, and makes **no novelty/priority** assertion. The proof of the stronger poset-ideal gluing, the **(WR)** hypothesis, and the non-wedge fundamental-group argument are appropriate targets for a future independent audit, but are so far **internally checked working mathematics**, NOT retroactively part of the third referee's A1–E3 certificate.

**Background used:** standard finite simplicial face-poset and crosscut lemmas; product/coproduct/Čech operations in an ∞-topos; cup-product vanishing on suspensions (e.g. Stanford Math 215B solutions at https://web.stanford.edu/class/math215b/Sol6.pdf); standard periodic-grid triangulation of a torus (e.g. HU Berlin Topologie I 2026 notes https://www2.mathematik.hu-berlin.de/~wendl/Sommer2026/Topologie1/lecturenotes.pdf); and the previously independently audited nonconstant-sheaf and canonical-arrow results.
