# Project A — internal adversarial audit: scattered relation algebra and exact two-to-one safe graph
**21 November 2026 · INTERNAL audit, no independent referee yet**

Reviewed new [scattered relation algebra / two-to-one counterexample note](ProjectA_SCATTERED_RELATION_ALGEBRA_FINITE_TO_ONE_NECESSITY_COUNTEREXAMPLE_2026-11-21.md), with input from the [prior independently reviewed graph-phase referee addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md).

### Audit dependencies

**Externally established topological/localic theorem** (not new): Picado–Pultr, *Axiom T_D and the Simmons sublocale theorem*, Comment. Math. Univ. Carol. 60 (2019), 541–551, characterized spaces for which all sublocales are induced precisely by \(T_D\) and scatteredness; Anna Laura Suarez, *Revisiting the relation between subspaces and sublocales*, arXiv:2010.05284. Since Hausdorff implies \(T_D\), every sublocale of a scattered Hausdorff space is induced by an ordinary subset. This hypothesis is essential: do **not** generalize to arbitrary Hausdorff/Cantor spaces.

**Earlier independently verified result** (not re-audited here): finite-to-one continuous compact-Hausdorff f has graph in the finite-join locally-closed partial-homeomorphism + rectangular algebra if and only if its locally closed chart rank is finite. The graph-algebra associativity statements were conditional on the previous independently reviewed rectangular rule (RC). The present scattered-space relation-algebra proof independently obtains associative composition for **all** relations, so its positive safety claim does **not** require (RC).

### Claim-by-claim checks

1. **Finite products scattered.** For nonempty T⊂X×Y choose isolated x in projection to X; then isolated y in the corresponding T_x⊂Y; a product neighborhood isolates (x,y). Valid without compactness, with nonempty T. Iterate for G²/G³.
2. **Spatial compact-Hausdorff product.** In classical locale theory the finite localic products of compact Hausdorff spaces agree with the ordinary compact Hausdorff product topologies. Hence Simmons applies to G² and G³; no tacit spatiality of arbitrary products of spatial sublocales is needed.
3. **All sublocales point-generated.** The published \(T_D\)+scattered theorem identifies S(G^n) with P(|G|^n) by induced sublocales. Therefore a sublocale of G³ is the join of its ordinary points and equals 0 precisely when it has no points.
4. **Genuine pullback.** The composability locale P is a sublocale of G³; points of P are exactly compatible triples, because the represented point functor Hom(1,-) preserves finite limits. Since G³ scattered, P has no extraneous pointless component.
5. **Image as join of point images.** The localic image on sublocales is left adjoint to inverse image and preserves arbitrary joins. Thus π13[P] is exactly the induced sublocale of ordinary projected point pairs. No invalid arbitrary distributivity of composition is smuggled in: on this *specific scattered class* all pullbacks and images are point-set operations as a consequence of total point determination.
6. **Full relation algebra.** The sublocale lattice of G² is genuinely a powerset Boolean algebra by the Simmons equivalence, so composition is the ordinary associative set-theoretic operation and even preserves arbitrary joins in each variable. Converse and Δ behave ordinarily.
7. **Finite discrete cover implies finite derivative height.** For T1 Z=D_1∪…∪D_m with each D_i discrete in Z, prove Z^(m)=∅ by induction. For z∈Z^(m)∩D_i, isolate its own color in a neighborhood O; V=O\{z} is open T1 and has at most m−1 colors, so V^(m−1)=∅. But z a limit point of Z^(m−1) forces V∩Z^(m−1)≠∅, and derivatives commute with open restriction, contradiction. This checks the central obstruction without appealing to a possibly invalid Baire argument.
8. **Ordinal target.** Y=[0,ω^ω] order topology is countable compact metrizable Hausdorff scattered, with nonempty derivatives through every finite stage. Correct use of ordinal rank; avoid saying the height is finite.
9. **Compact source.** X=(Y×{0})∪{(y_n,1/n)} is closed in compact Y×({0}∪{1/n}), hence compact metrizable; upper points are isolated (each at a unique positive height), the base Y is scattered, so X scattered.
10. **Exactly two-to-one.** Each y appears once in the enumeration and once at the base height; no duplications or omissions. Thus every fiber has exactly 2 points and f continuous proper surjective.
11. **Infinite chart rank.** Any finite family of arbitrary homeomorphic partial charts covering X partitions the discrete upper selector E into finitely many discrete subsets E_i; their images D_i under the charts are discrete subspaces of Y, and their union equals Y. Contradicts item 7 and infinite CB rank. Does not require domains locally closed.
12. **Safety but nonmembership.** G=X⊔Y is compact scattered Hausdorff; by items 1–6 every localic relation on G associates, including Γ_f and Γ_f^smile. Independent referee addendum's finite-to-one equivalence then shows Γ_f outside the prior restricted algebra. This is an outright **negative answer** to finite-to-one chart-rank necessity.
13. **Finite-height complement.** If Y has scattered derivative height h<∞ and all fibers ≤N, each stratum Y^(i)\Y^(i+1) is discrete locally closed, its preimage is discrete locally closed when fibers are finite, and can be partitioned into ≤N injective subsets; these are locally closed in source and image. Gives \(\rho_{\rm lc}(f)\le hN\), no openness assumed.
14. **Source scattered over scattered target.** For any continuous finite-to-one f:X→Y, X Hausdorff and Y scattered, any nonempty A⊂X maps to a subset with isolated y; select and isolate a point x in finite A∩f^-1(y), then isolate x in A using continuity. Thus X scattered. If both spaces compact Hausdorff, safety follows via the full relation algebra theorem, irrespective of chart rank.

### Verdict and boundary

**FAVORABLE PROVISIONAL INTERNAL AUDIT.** All material deductions in the note follow from the stated established Simmons/Picado–Pultr theorem and elementary topological arguments. A new independent blind review is still worthwhile if this result becomes a canonical theorem, particularly the passage from total point determination on G³ to localic image-defined relation composition and the finite discrete cover derivative bound.

**Most important strategic correction:** The independent referee's open finite-to-one necessity problem has a **negative answer** when scattered targets are allowed, even with every fiber of size exactly two. The surviving question must restrict the target/ambient so that nonspatial sublocales are genuinely present (for example, non-scattered perfect compact metric targets). Do not conflate "safe adjunction" with "finite-chart membership."

No novelty or priority claim.
