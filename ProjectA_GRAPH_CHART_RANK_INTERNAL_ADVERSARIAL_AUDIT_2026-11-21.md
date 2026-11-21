> **HISTORICAL INTERNAL AUDIT, SUPERSEDED AS CURRENT STATUS (21 NOV 2026):** The [independent report](project-a/audits/2026-11-21/GRAPH_CHART_RANK/INDEPENDENT_REFEREE_REPORT.md) found the graph-extension package **correct with minor repairs, conditional on previously reviewed RC**; the [referee addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md) disproved broad finite chart rank necessity and gave a finite-exception functional graph membership theorem. Current [canonical account](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md) and [reconciliation](ProjectA_GRAPH_EXTENSIONS_REFEREE_RECONCILIATION_2026-11-21.md). This internal audit was withheld from the referee; its original analysis is retained below.

# Project A — internal adversarial audit: graph charts, finite-fiber Cantor obstruction, Michael selection
**21 November 2026 · Internal verification only; NOT an independent or external referee report**

**Items checked:** [locally closed partial-homeomorphism graph algebra](ProjectA_GRAPH_LOCAL_HOMEOMORPHISM_POSITIVE_OPEN_PROPER_NEGATIVE_2026-11-20.md), [Cantor two-to-one negative example and rank](ProjectA_FINITE_FIBRE_GRAPH_CHART_RANK_CANTOR_COUNTEREXAMPLE_2026-11-21.md), and [Michael selection open finite-to-one positive theorem](ProjectA_OPEN_FINITE_TO_ONE_STONE_MAPS_SELECTION_THEOREM_2026-11-21.md). **Imported separately:** the independently blind-refereed [finite rectangular p/q calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md). No priority claim.

## 1. Verdict

**Favorable provisional internal audit, with scope boundaries.** The positive chart-algebra mechanism (locally closed restriction, graph actions, triple-generator composition), the two-to-one Cantor counterexample, and the zero-dimensional Michael selection induction withstand targeted checks. The two-to-one negative example is **not open**; the theorem that *open + uniformly bounded finite fibers* is positive requires **compact metrizability and a zero-dimensional target**. They are not contradictory.

The zero-dimensional continuous-selection theorem is an external theorem, not a new assertion; sources state that lower semicontinuous multifunctions with nonempty **closed** values in a **complete metric** range admit a continuous selector when the domain is **zero-dimensional paracompact**:
- [Topology Proceedings, Michael zero-dimensional selection theorem discussion](https://topology.nipissingu.ca/tp/reprints/v39/tp39004.pdf)
- [Selections and representations of multifunctions in paracompact spaces](https://matwbn.icm.edu.pl/ksiazki/sm/sm102/sm10232.pdf).

## 2. Locally closed graph-action checks

For an induced point-generated spatial sublocale [B] of compact Hausdorff G and a **locally closed** U=O∩F, restriction gives
\[
[B]\wedge U=[B\cap U].
\]
This must **not** be generalized to arbitrary induced spatial sublocales U: two disjoint ordinary dense subsets of Cantor space can generate induced spatial sublocales with a **nonzero** meet.

For t∈{p,q}, the formulas
\[
t(A,B)\circ\Gamma_h=t(A,h(B\cap U_h)),\qquad
\Gamma_h\circ t(A,B)=t(h^{-1}(A\cap V_h),B)
\]
hold because restriction in one product coordinate is the actual localic pullback and the remaining map is an isomorphism, not a non-stable image surjection. Composition/inversion of locally closed partial homeomorphisms preserve locally closed domains/ranges.

All triple generator types audited: RRR by independent referee's rectangular rule; RRH/HRR by same middle overlap and outer coordinate restriction; RHR by pulling back the **middle** overlap along a homeomorphism of locally closed sectors; RHH/HHR/HRH by ordinary partial map composition/restrictions on the appropriate endpoint; HHH by partial map associativity. Each binary composite remains a generator, so finite-join closure suffices. No arbitrary-join interchange is used.

**Residual risk:** Full formalization of the localic image/pullback bookkeeping would be appropriate in an external audit. The internal proof does not prove an arbitrary-open-map-graph extension.

## 3. The Cantor-to-Cantor at-most-two-to-one negative example

Y=2^ℕ, choose pairwise disjoint closed nowhere-dense copies K_n of Cantor space meeting the nth nonempty basic clopen W_n, with selected q_n∈K_n∩W_n. The construction is possible because at stage n the finite union of previous K_i is nowhere dense. Q={q_n} is dense; I=Y\Q is dense since Q is countable and Y perfect.

Let X=(Y×{0})∪⋃_n(K_n×{1/n}). Check:
- X is a closed subspace of compact metrizable Y×({0}∪{1/n}): the only nontrivial level limit is height 0, where the whole Y base is included.
- X is zero-dimensional and **perfect**, because every point lies in one of the perfect subspaces Y×{0} or K_n×{1/n}. Therefore X itself is Cantor space.
- f=pr_Y|X has fibers of cardinality **one or two**, since the K_n are pairwise disjoint. f is proper/surjective but **not open**: each K_n×{1/n} is clopen in X with image nowhere dense K_n.
- E={(q_n,1/n)} is an ordinary **discrete subspace** of X; its induced locale [E] is discrete. The induced image of [E] under f is [Q], but its pullback of [I] is 0 because each discrete singleton maps to a point not in I.
- Both [Q] and [I] are dense sublocales of Y. Their intersection contains its nonzero least dense sublocale B(Y).

Thus for the point-generated relations R={u}×[I], F=Γ_f^smile, T=[E]×{v},
\[
(R\circ F)\circ T=0\ne\{(u,v)\}=R\circ(F\circ T).
\]
All three are relations on the compact metrizable Stone disjoint union G={u}⊔Y⊔X⊔{v}; Γ_f^smile is **closed**, despite the failure. Symmetrizing the three-factor path inside clopen level blocks gives a single reflexive symmetric point-generated relation whose threefold powers have a bracket-dependent ordinary edge (same four-level argument as the previous internal proof).

**Direct infinite-rank proof (no locale theory):** If E were covered by finitely many partial homeomorphism domains, Q=f(E) would be the union of finitely many discrete subsets D_i of perfect Hausdorff Y. But the closure of a discrete D_i has empty interior (otherwise its points in that interior could not be isolated relative to D_i), so the union of finitely many such closures is nowhere dense, contradicting the density of Q. The earlier wording invoked Baire unnecessarily: **finite unions of nowhere-dense sets are nowhere dense in any space**.

## 4. Michael theorem step-by-step

Let f:X→Y be a continuous open surjection from **compact metrizable** X onto compact metrizable **zero-dimensional** Y with all fibers cardinality ≤N. Inductively assume X_i⊆X open (hence **completely metrizable**) and Y_i=f(X_i)⊆Y open (hence **zero-dimensional paracompact**). The restriction f_i:X_i→Y_i is open and surjective. Its inverse-fiber multifunction F_i(y)=f_i^-1(y) has nonempty **closed** values in X_i and is lower semicontinuous because f_i is open. Michael's theorem produces a continuous s_i:Y_i→X_i.

The image U_i=s_i(Y_i) is **closed in X_i**: it is the equalizer/fixed-point set of id_{X_i} and s_i∘f_i in a Hausdorff space. Therefore U_i is **locally closed in X**; f maps it homeomorphically to open Y_i. Removing U_i yields X_{i+1} open in X; f(X_{i+1}) is open in Y. Each iteration removes **exactly one point from every currently nonempty fiber**. After N steps, X_{N+1}=∅, producing exactly N disjoint locally closed charts. Since one injective chart contains at most one source point from each fiber, lower bound N proves
\[
\rho_{\rm lc}(f)=\max_y|f^{-1}(y)|=N.
\]
No assumption that the later Y_i are compact is made; zero-dimensional paracompactness is preserved by their openness in metrizable Y. **Do not** misapply the selection theorem to general positive-dimensional or nonmetrizable targets.

## 5. Sharp resulting comparison

| Class of map | Graph extension |
|---|---|
| Globally injective compact→Hausdorff | Positive: one closed chart |
| Branched fold t↦t², [−1,1]→[0,1] | Positive: two closed injective charts, despite non-local-homeomorphism at branch point |
| Open, uniformly N-to-one compact metric map to zero-dimensional compact metric Y | Positive by Michael: exactly N locally closed charts |
| Nonopen at-most-two-to-one Cantor→Cantor constructed here | Negative: dense discrete selector / infinite chart rank |
| Globally open proper projection Cantor×infinite compact metric K→Cantor | Negative: previous infinite-fiber obstruction |

A **globally proper** map can fail due to restrictions to induced spatial supports; a **globally open** map can fail when infinite fiber multiplicity allows a dense discrete selector; but **open + bounded finite fibers + zero-dimensional metric base** is a new positive region.

## 6. Big-picture caution, next research

These are imposed graph relations on compact Hausdorff spaces. The intrinsic Cameron–Kumar inseparability/functional relations on these spaces are equality; the new graph examples must not be advertised as nontrivial *intrinsic* separation graphs. The role of this direction is to understand which point-free **graph path processes** retain ordinary witness structure.

**Next bounded questions:** extend finite-chart results to connected/positive-dimensional branched maps; find criteria beyond locally closed chart decomposition; examine whether point-free intrinsic specialization \(\mathcal S\) and its hulls admit related stable witness presentations; or produce a blind audit packet for the internally derived graph-algebra extension and finite-fiber dichotomy. An external audit should focus especially on the locally closed graph-action formulas (mixed p/q), the Michael recursion's completeness/paracompactness, and the negative pullback [E]∧f^-1([I])=0.

**Internal verdict is not a substitute for independent review.**
