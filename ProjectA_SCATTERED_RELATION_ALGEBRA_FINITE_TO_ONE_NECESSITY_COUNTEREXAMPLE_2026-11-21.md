# Project A — scattered relation algebras and a safe two-to-one map of infinite chart rank
## Boundary exploration, 21 November 2026 · NEW INTERNAL theorem (not yet externally audited)

**Headline:** Finite locally closed chart rank is NOT necessary for safe adjunction, **even for exactly two-to-one continuous surjections of compact metrizable spaces**. There is a 2-to-1 compact scattered example of infinite chart rank whose graph and converse can be adjoined to the entire rectangular algebra—indeed, **every** localic relation on its ambient compact scattered Hausdorff space composes associatively.

This goes beyond the independent referee's [addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md), which gave a safe infinite-rank example with an **infinite constant fiber**. Here every fiber has **exactly two points**, so the addendum's finite-to-one equivalence shows that the safe graph is genuinely **outside** the known finite-join graph algebra.

**Source theorem:** The Simmons sublocale theorem in the \(T_D\) refinement of Picado–Pultr, *Axiom \(T_D\) and the Simmons sublocale theorem*, Comment. Math. Univ. Carol. **60** (2019), 541–551, states: all sublocales of \(\Omega(G)\) are precisely the sublocales induced by ordinary subsets iff \(G\) is \(T_D\) and scattered. See also Anna Laura Suarez, *Revisiting the relation between subspaces and sublocales*, arXiv:2010.05284 (2020), https://arxiv.org/abs/2010.05284. Hausdorff spaces are \(T_D\). These are established external theorems; the relation-algebra and finite-rank conclusions below are **new internal deductions from them**, with no literature priority assertion.

### 1. All localic relations on compact scattered Hausdorff spaces compose ordinarily

**Lemma 1.1.** The finite product of scattered topological spaces is scattered.

**Proof.** For nonempty \(T\subseteq X\times Y\), choose an isolated point \(x\) of its first-coordinate projection. The nonempty fiber \(T_x\subseteq Y\) has an isolated point \(y\). An open neighborhood isolating \(x\) in the projected set, times an open neighborhood isolating \(y\) in the fiber, isolates \((x,y)\) in \(T\). Induct on the number of factors. □

For compact Hausdorff G, the localic finite powers \(G^n\) coincide with the ordinary compact Hausdorff products, which are scattered by Lemma 1.1. Simmons/Picado–Pultr therefore gives an **order isomorphism**
\[
\boxed{\mathsf{S}(G^n)\ \cong\ \mathcal P(|G|^n)\qquad(n\ge1),}
\tag{S}
\]
via \(A\mapsto[A]\). Every sublocale is point-generated; its ordinary point set determines it uniquely, and meets and joins correspond to intersections and unions of point sets.

**Theorem 1.2 (INTERNAL corollary).** For arbitrary sublocales \(R,S\hookrightarrow G^2\), localic relation composition equals ordinary set-theoretic composition:
\[
\boxed{R\circ S=[\,\mathrm{pt}(R)\circ_{\rm set}\mathrm{pt}(S)\,]_{G^2}.}\tag{REL}
\]
Consequently \(\mathsf{S}(G^2)\) under localic composition, converse, and joins is **the full ordinary relation algebra** on \(|G|\): composition is associative and distributes over even **arbitrary** joins.

**Proof.** Compute the genuine composability pullback \(P=R_{12}\wedge S_{23}\hookrightarrow G^3\). The set of points of a pullback is the ordinary fiber product of point sets, so
\[
\mathrm{pt}(P)=\{(x,y,z): (x,y)\in\mathrm{pt}(R),\ (y,z)\in\mathrm{pt}(S)\}.
\]
Since \(G^3\) is scattered Hausdorff, \(P\) is the induced sublocale of this set. The projection image \(\mathrm{im}(\pi_{13}|_P)\) is the induced sublocale of the ordinary projected set: \(P\) is the **arbitrary join** of its point sublocales, and localic image is a left adjoint, hence preserves all joins. Therefore the image relation is exactly \([\mathrm{pt}(R)\circ_{\rm set}\mathrm{pt}(S)]\). All claimed relation-algebra laws now reduce to the ordinary set-theoretic identities. □

**Scope:** Compact scattered Hausdorff, not an assertion for arbitrary compact Hausdorff or for unspecified nonspatial products of noncompact locales. The result applies to **all** sublocales \(G^2\), not only point-generated graphs.

### 2. Finite unions of discrete subsets have finite Cantor–Bendixson height

For a \(T_1\) space Z, let \(Z^{(m)}\) denote its m-th Cantor–Bendixson derivative (successive removal of isolated points), for nonnegative integers \(m\).

**Lemma 2.1 (elementary, NEW INTERNAL).** If \(Z=D_1\cup\dots\cup D_m\) with each \(D_i\) **discrete as a subspace of Z**, then
\[
\boxed{Z^{(m)}=\varnothing.}\tag{CB}
\]

**Proof by induction on m.** For m=1, Z itself is discrete. Suppose m≥2 and \(Z^{(m)}\ne\varnothing\); choose \(z\in Z^{(m)}\), of color i, so \(z\in D_i\). Since \(D_i\) is discrete, choose an open neighborhood O of z with O∩D_i={z}. As Z is T1, \(V=O\setminus\{z\}\) is open in Z, and V is covered by the **remaining m−1 discrete subspaces** \(V\cap D_j\) for j≠i. By induction \(V^{(m-1)}=\varnothing\). But \(z\in Z^{(m)}\) implies that every punctured neighborhood of z meets \(Z^{(m-1)}\), so \(V\cap Z^{(m-1)}\ne\varnothing\). Since V is open, its derivatives agree with \(V\cap Z^{(r)}\), contradicting \(V^{(m-1)}=\varnothing\). □

This bound is independent of the localic algebra. In particular, any scattered \(T_1\) compactum of **infinite finite-stage Cantor–Bendixson height** cannot be partitioned into finitely many discrete subspaces. E.g. the compact countable ordinal space
\[
\boxed{Y=[0,\omega^\omega]}
\]
with the order topology has \(Y^{(m)}\ne\varnothing\) for every finite m. It is compact, metrizable, Hausdorff, zero-dimensional and scattered.

### 3. Exactly two-to-one compact metric safe map with infinite chart rank

**Theorem 3.1 (INTERNAL; refutes the finite-to-one necessity question).** There exist compact metrizable scattered Hausdorff spaces X,Y and a continuous surjection f:X→Y such that:
1. **Every fiber has exactly 2 points**.
2. \(\rho_{\rm lc}(f)=\infty\); in fact f has **no finite cover by arbitrary injective partial-homeomorphism charts**, even without locally closedness.
3. The graph \(\Gamma_f\) and its converse can be safely adjoined to the full compact-Hausdorff rectangular algebra, because on \(G=X\amalg Y\) **every** localic relation composes associatively.
4. By the independent referee's finite-to-one membership corollary, \(\Gamma_f\notin\mathcal A_{\rm lc}(G)\). Thus **safe graph adjunction does not imply membership in the known finite-join algebra, even under uniform multiplicity 2**.

**Construction.** Let \(Y=[0,\omega^\omega]\) as above; enumerate its countably infinitely many points as \(Y=\{y_n:n\ge1\}\) without repetition. Let
\[
S=\{0\}\cup\{1/n:n\ge1\}\subseteq[0,1],
\qquad
X=(Y\times\{0\})\cup\{(y_n,1/n):n\ge1\}\subseteq Y\times S.
\tag{X}
\]
Define \(f:X\to Y\) by first-coordinate projection.

**Topology and fibers.** X is **closed** in compact metrizable Y×S: every limit of selected upper points at heights tending to zero lies in the complete base sheet Y×{0}; each positive height is isolated in S. Hence X is compact metrizable Hausdorff. It is scattered: every nonempty subspace containing an upper point has an isolated such point (upper points are isolated in all X); otherwise it lies in the scattered base sheet Y×{0}. Each y=y_n has precisely two preimages (y,0) and (y,1/n). Thus f is proper and surjective, exactly 2-to-1.

**Infinite chart rank.** The upper points form a discrete subspace
\[
E=\{(y_n,1/n):n\ge1\}\subseteq X,
\]
and f(E)=Y. Suppose finitely many partial homeomorphism domains U_1,…,U_m cover X. For each i, E_i=E∩U_i is discrete, and f(E_i)⊂Y is **discrete** because f|U_i is a homeomorphism onto its image. The finitely many discrete images \(D_i=f(E_i)\) cover all of Y, contradicting Lemma 2.1 because \(Y^{(m)}\ne\varnothing\). This proves \(\rho_{\rm lc}(f)=\infty\), even allowing arbitrary domains/ranges without the local-closedness condition.

**Safety outside the known algebra.** The finite disjoint union \(G=X\amalg Y\) is compact metrizable scattered Hausdorff. By Theorem 1.2 **all localic relations on G associate**. Therefore the graph \(\Gamma_f\) and its converse may be adjoined to any relation algebra on G without destroying associativity. Since f is finite-to-one, the independent referee's [addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md) proves the equivalence \(\Gamma_f\in\mathcal A_{\rm lc}\Longleftrightarrow\rho_{\rm lc}(f)<\infty\). We have shown \(\rho_{\rm lc}(f)=\infty\), so \(\Gamma_f\) is **safe but outside** \(\mathcal A_{\rm lc}(G)\). □

**Additional exact probe observation.** For any ordinary E_0⊂X,A⊂Y, the image/pullback nonzero-reflection criterion
\[
[f(E_0)]\wedge[A]\ne0\Longrightarrow[E_0]\wedge f^{-1}([A])\ne0
\]
holds automatically: Y and X are scattered, so the middle intersection is induced by the **ordinary** set f(E_0)∩A; if nonempty choose x∈E_0 with f(x)∈A. Thus the earlier graph-probe obstruction cannot detect the safe infinite-rank example. In fact, no localic associator exists on the ambient G.

### 4. Why this changes the next necessity question

The addendum had narrowed the broad necessity question to **finite-to-one f**. Theorem 3.1 refutes even that restriction. One must exclude the **scattered fully point-determined regime** before a chart-rank necessity conjecture can be plausible.

Possible surviving refinements:
- require **perfect** or **crowded compact Hausdorff target** Y, so nonspatial (pointless) sublocales and ghost intersections can occur;
- require some nontrivial localic image/pullback behavior to be present and seek a weaker **stable-witness decomposition** than finite chart rank;
- focus on intrinsic specialization/Ins/Cm graph sublocales where the ambient is non-Hausdorff; there the point-free hierarchy has additional constraints.

A separate follow-up is the **discrete-selector criterion**: if a discrete E⊂X maps onto a countable dense-in-itself subset of a perfect closed part of Y, a nonzero pointless overlap forces a graph-probe associator. Over a scattered Y no such dense-in-itself part exists, which explains why the chart-rank obstruction is topological rather than purely cardinal.

**Audit status:** New internal result based on the published Simmons/Picado–Pultr theorem and referee's independently checked finite-to-one membership equivalence. The relational composition reduction and the explicit ω^ω+1 construction have **not yet** been independently externally audited. The earlier positive/negative Cantor results are unaffected.
