> **21 NOV 2026 — SCATTERED COORDINATE ABSTRACTED (NEW INTERNAL THEOREM; REFEREE PENDING).** The [balanced witness transport and scattered-index algebra](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md) gives an axiomatic (G)/(T)/(O) criterion for adjoining graph correspondences associatively to **all** finite p/q rectangles. It proves a sharp parameterized index theorem: for compact Hausdorff K, **K scattered iff for every compact Hausdorff Z,** `Sub(Z×K) ≅ ∏_{k∈K}Sub(Z)` via *closed point-fibre restriction*. Consequently **even discontinuous ordinary permutations** of K, with independently varying homeomorphisms of a perfect fibre P, induce legitimate point-generated graph relations forming a safe wreath-product group under genuine localic composition. The separate [locally finite localic relation matrix theorem](ProjectA_SCATTERED_INDEX_LOCALLY_FINITE_LOCALIC_RELATION_MATRICES_2026-11-21.md) proves the exact arbitrary binary matrix product rule and lifts **any associative finite-join base localic relation algebra** on P to row-and-column-finite matrices over scattered K, with finite-length graph-path expansion. The locally finite matrix class does **not** automatically include all global G-rectangles; that stronger adjunction holds for the balanced monomial graph class. Targeted [balanced-witness internal audit](ProjectA_BALANCED_WITNESS_MATRIX_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) and [matrix-calculus internal audit](ProjectA_SCATTERED_INDEX_MATRIX_CALCULUS_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) are provisionally favorable. **NEW RESULTS NOT YET INDEPENDENTLY REFEREED;** earlier compact-Hausdorff (RC) is an imported independently checked input. This is a substantial positive endpoint for graph boundary exploration before the planned big-picture review and specialization/Dowker work.

# Project A — safe infinite-rank finite-to-one maps BETWEEN Cantor spaces
## Tensorization of scattered pseudo-bijections · 21 November 2026 · INTERNAL candidate

**Major conclusion, pending independent audit:** There is a continuous surjection \(F:\widetilde X\to\widetilde Y\) with **both \(\widetilde X,\widetilde Y\) homeomorphic to Cantor space**, every fiber of size **1 or 2**, and **infinite** locally closed graph-chart rank, such that \(\Gamma_F,\Gamma_F^\smile\) can be adjoined **associatively** to the entire finite point-generated/full rectangular algebra of the compact Hausdorff disjoint union \(\widetilde X\amalg\widetilde Y\). Consequently this graph is also **outside** the referee's known locally closed graph algebra, by the finite-to-one graph-membership theorem, yet its adjunction is safe.

**Prerequisites:** The [independently reviewed compact-Hausdorff rectangular rule RC](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), the [independently reviewed referee finite-to-one membership criterion](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md), and the new INTERNAL [scattered-fiber/pseudo-bijection lemma](ProjectA_PERFECT_TARGET_SCATTERED_CORRIDOR_SAFE_INFINITE_CHART_RANK_2026-11-21.md). This note makes the parameterized localic-pullback argument explicit. No literature priority claim.

### 1. Sublocale matrices along a scattered coordinate

Let Z be **any compact Hausdorff space**, K compact scattered Hausdorff. The preceding scattered-fiber lemma (SF) asserts that every sublocale W≤Z×K is the join of its closed point fibers:
\[
W=\bigvee_{k\in K}W_k,\qquad W_k=W\wedge(Z\times\{k\}).
\tag{SF}
\]
This strengthens to a complete lattice isomorphism
\[
\boxed{
\operatorname{Sub}(Z\times K)\ \cong\
\prod_{k\in K}\operatorname{Sub}(Z),\qquad
W\longmapsto (W_k)_{k\in K}.
}\tag{MAT}
\]

**Surjectivity/inverse:** Given arbitrary sublocales A_k≤Z, take \(W=\bigvee_{k\in K}(A_k\times\{k\})\). Its k-fiber is precisely A_k. Indeed all summands with j≠k are supported in \(Z\times[K\setminus\{k\}]\), disjoint from \(Z\times\{k\}\) because sublocales of scattered Hausdorff K are induced and point-determined. The remaining k-summand is supported exactly at k. Finite distributivity gives equality of that fiber. Injectivity follows from (SF). Since the map is an order isomorphism, it preserves **all meets and joins**. This is a decomposition of sublocale lattices, NOT a claim that K is topologically discrete.

If D is an ordinary discrete space, the analogous decomposition
\[
\operatorname{Sub}(Z\times D)\cong\prod_{d\in D}\operatorname{Sub}(Z)
\]
follows from the topological/localic disjoint-union product \(Z\times D\cong\coprod_{d\in D}Z\).

### 2. Parameterized scattered pseudo-isomorphisms

Let P be compact Hausdorff, D a discrete ordinary set, K compact scattered Hausdorff, and b:D→K an ordinary bijection (automatically continuous). Inside some compact Hausdorff ambient G, suppose \(U=P\times D\) is an **open** subspace, \(V=P\times K\) a **closed** subspace, and U,V disjoint. Consider the continuous bijection
\[
g=id_P\times b:U\longrightarrow V
\]
and its point-generated localic graph γ⊂G².

**Lemma 2.1 (parameterized transport).** For every *compact Hausdorff parameter space Z*, the map
\[
id_Z\times g: Z\times U\to Z\times V
\]
induces an **order isomorphism on sublocale lattices** through inverse image and localic image: under (MAT) the two operators simply relabel the components by b. In particular their composites, in either order, are the identity on the respective sublocale lattices, and they preserve **all meets and joins**.

**Proof.** Since \(Z\times U=(Z\times P)\times D\) and \(Z\times V=(Z\times P)\times K\), the discrete and scattered decompositions both identify their sublocale lattices with products of \(\operatorname{Sub}(Z\times P)\). On each discrete fiber d, \(id_Z\times g\) restricts to the isomorphism \(Z\times P\times\{d\}\cong Z\times P\times\{b(d)\}\). Thus the inverse image pulls back exactly the b(d)-component. Its image pushes that component forward unchanged, and the image of an arbitrary sublocale is the **join of its component images**, because localic image preserves joins. These are inverse relabelings by the bijection b. □

**Corollary 2.2 (full p/q rectangular actions).** For either t=p or q, ordinary A,B⊂G, γ and its converse satisfy exactly the four formulas
\[
\begin{aligned}
t(A,B)\circ\gamma&=t(A,g(B\cap U)),\\
\gamma\circ t(A,B)&=t(g^{-1}(A\cap V),B),\\
t(A,B)\circ\gamma^\smile&=t(A,g^{-1}(B\cap V)),\\
\gamma^\smile\circ t(A,B)&=t(g(A\cap U),B).
\end{aligned}
\tag{PB-P}
\]
For p, locally closed restriction and the disjoint discrete D-index show the pulled-back relation remains the spatial induced sublocale of the ordinary inverse image and its image remains point-generated. For q, use the actual product pullback and the parameterized sublocale lattice transport from Lemma 2.1 with Z=G; this ensures the output is the **whole potentially nonspatial q rectangle**, not merely the spatial part.

**Overlap transport (the RHR test).** For arbitrary B,C⊆G, the two sublocale overlaps
\[
[g(B\cap U)]\wedge[C]\quad\text{and}\quad
[B]\wedge[g^{-1}(C\cap V)]
\]
are identified, after sector restriction, by the sublocale lattice isomorphism of Lemma 2.1 with Z=1. They are therefore simultaneously nonzero (or zero). This does **not** require the P-coordinate to be scattered or point-determined: its full sublocale structure is preserved in every indexed fiber.

**Localic graph inverses.** The two products \(\gamma\circ\gamma^\smile=\Delta_U\) and \(\gamma^\smile\circ\gamma=\Delta_V\) hold. For the first, the genuine fiber product U×_V U decomposes over D×D; injectivity of b makes all off-diagonal components zero and each diagonal component the P-diagonal. For the second, composability is U and its image under the diagonal of V is **the full closed spatial diagonal \(\Delta_V\)**, because g is onto all ordinary points of spatial V. The graph is not asserted to be a homeomorphism: these are image-defined relation identities in a nonregular ambient relation category.

### 3. Parameterized 15-element graph semigroup

Start with the unparameterized perfect-target map f:X→C from [the preceding note](ProjectA_PERFECT_TARGET_SCATTERED_CORRIDOR_SAFE_INFINITE_CHART_RANK_2026-11-21.md): base B=C×{0}, discrete open upper D indexed by the points of closed scattered K⊂C, graph decomposition Γ_f=Γ_h∨Γ_g.

Fix P=Cantor space. Define \(\widetilde X=P\times X,\ \widetilde Y=P\times C\), \(\widetilde G=\widetilde X\amalg\widetilde Y\), and \(F=id_P\times f:\widetilde X\to\widetilde Y\).

The original clopen component Y, closed base B, open upper D, closed K_B,K_Y, and the maps h,g,b,t from the preceding note become their **P-products**. Thus the graph of F is
\[
\Gamma_F=\Gamma_{\widetilde h}\vee\Gamma_{\widetilde g}.
\tag{GF}
\]
The 15 relations in the preceding note (zero, full identity, five partial identities, eight oriented partial bijections) are now P-parameterized. Localic binary products again match the ordinary partial-bijection multiplication table:
- Genuine locally closed homeomorphism graph composites remain genuine graph composites.
- Mixed products with \(\widetilde g\) reduce under the genuine homeomorphism to the pseudo-bijection graph, or to zero due to clopen sector mismatch.
- \(\widetilde g\circ\widetilde g^\smile=\Delta_{P\times D}\) and \(\widetilde g^\smile\circ\widetilde g=\Delta_{P\times K}\) by Corollary 2.2's graph-inverse argument.
- Every new restricted partial map is among the same list of fifteen, with all domains/ranges multiplied by P.

The **finite ordinary partial-bijection multiplication table** has 15 elements (including zero and full identity) and is associative. The same table is realized by the genuine localic composites because the individual identities above were checked by actual pullback/image calculations, not ordinary point matching alone.

### 4. Main tensorized associative algebra theorem

**Theorem 4.1 (INTERNAL; conditional on imported RC).** Let \(\mathcal A^\ast(\widetilde G)\) consist of finite joins of all p(A,B),q(A,B) rectangles on \(\widetilde G\) and the 15 P-parameterized graph semigroup relations. Then \(\mathcal A^\ast(\widetilde G)\) is closed under genuine localic composition, converse and finite joins, and **associative and unital**. In particular, Γ_F and its converse adjoin safely to the **entire** rectangular algebra.

**Proof.** The single-generator binary multiplication types are again
\[
RR\to q\text{ or }0\quad(\text{refereed RC}),\qquad
RH,HR\to R\text{ or }0\quad(\text{PH or PB-P}),\qquad
HH\to H\text{ or }0\quad(\text{parameterized graph semigroup}).
\]
The eight triple-generator patterns are verified exactly as in the referee's locally closed case: RRR by RC (allow empty outer endpoints); HHH by the semigroup; RRH/HRR by unchanged internal rectangular overlap; RHH/HHR by associative composition of the underlying partial bijections and the exact setwise support actions; HRH by commuting restrictions on independent endpoints; RHR by the **parameterized nonzero-overlap transport** supplied by Lemma 2.1 (for pseudo arrows) or a genuine localic homeomorphism (for the others). Each nonzero RHR result is the same full q outer rectangle. Finite-join distributivity then proves associativity for the algebra.

### 5. Both source and target are Cantor spaces, yet the chart rank is infinite

The spaces \(\widetilde X=P\times X\) and \(\widetilde Y=P\times C\) are compact metrizable, zero-dimensional and **perfect** (every nonempty open product neighborhood projects to a nonempty P-open neighborhood, which contains more than one point). Thus each is homeomorphic to Cantor space. The fibers of F are precisely those of f at a fixed P-coordinate:
\[
\boxed{1\le|F^{-1}(p,y)|\le2,\qquad F\text{ surjective and proper}.}\tag{FIB}
\]

If F admitted finitely many locally closed homeomorphic graph charts, intersect their domains and ranges with the closed slices \(\{p\}\times X\) and \(\{p\}\times C\) for any fixed p∈P. Each restricted chart is still a homeomorphism between locally closed subsets of those slices, and the restrictions cover \(\{p\}\times X\). They would provide a finite chart cover for f:X→C, contradicting the previous note's infinite-chart-rank proof. Hence
\[
\boxed{\rho_{\mathrm{lc}}(F)=\infty.}\tag{RANK}
\]

The independently reviewed addendum states that **for finite-to-one continuous compact-Hausdorff maps**, graph membership in the locally closed + rectangular algebra \(\mathcal A_{\mathrm{lc}}\) is equivalent to finite chart rank. Therefore Γ_F is **outside** that algebra despite being safe in the **larger** newly constructed algebra \(\mathcal A^\ast\).

**Main conclusion (strongest INTERNAL candidate):**
\[
\boxed{
\begin{gathered}
\widetilde X\cong 2^{\mathbb N},\quad
\widetilde Y\cong 2^{\mathbb N},\quad
F:\widetilde X\twoheadrightarrow\widetilde Y,\quad
|F^{-1}(y)|\le2,\\
\rho_{\mathrm{lc}}(F)=\infty,\qquad
\Gamma_F\notin\mathcal A_{\mathrm{lc}},\qquad
\Gamma_F,\Gamma_F^\smile\text{ adjoin associatively to all finite p/q rectangles}.
\end{gathered}}
\tag{CANTOR-CANTOR}
\]

### 6. Scope, stress tests, next action

The **new nontrivial ingredient** is (MAT), the complete-lattice fiber decomposition of arbitrary sublocales over a compact scattered Hausdorff coordinate. The subsequent pseudo-bijection action/overlap identities, 15-element semigroup, and two-perfect-space theorem are new INTERNAL deductions; they are not in the previous independent referee report or addendum. In contrast, the basic rectangular (RC), genuine locally closed graph (PH), and finite-to-one membership criterion are imported from their independent review cycles.

**Mandatory further audit:** challenge (MAT) against genuinely nonspatial sublocales; verify that \((id_Z\times g)^{-1}\) and image really relabel **all sublocale fibers**, especially on q(A,B); verify that graph-only products remain the 15 partial maps after tensorization and do not acquire pointless off-diagonal support; then audit all eight mixed triple patterns and restriction to a closed parameter fiber in the chart-rank proof.

If certified, the boundary question is now decisively answered: **even perfect source, perfect target, and uniform fiber degree 2 do not force finite locally closed graph-chart rank for safe adjunction**. A more promising invariant is a finite witness presentation admitting *scattered-coordinate pseudo-isomorphisms*, not merely ordinary locally invertible charts.
