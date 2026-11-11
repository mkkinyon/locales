# Point-Free Topology — Parked roadmap: feedback from patched homotopy to binary separation relations

**10 November 2026 · Explicitly retained alternative direction.** The user authorized choosing **either** twisted coefficients or feedback to the original binary localic relation hierarchy, on the condition that the road not taken not be lost. We chose **twisted coefficients** for the current research segment; see [Higman twisted-cohomology / continuity-threshold note](PointFree_Higman_twisted_cohomology_continuity_threshold_2026-11-10.md). This roadmap is a *concrete parked next line*, not a new independent audit or a claim that the hierarchy has been solved.

## Motivation and first concrete benchmark

For any coherent X, the localic binary diagonal hulls
\[
\mathcal I=\operatorname{cl}(\Delta_2)=I_1(X),\qquad
\mathcal D=\operatorname{fit}(\Delta_2)=D_1(X)
\]
detect common **upper** and **lower** specialization bounds in the coherent spectral/Priestley model. The already audited arrow-level theorem gives a **comparison of realizations of all higher arities** C→I and C→D, not equality of binary relations. Their equivalence can coexist with strict binary incomparability.

**Explicit test example (finite and infinite).** Let P be the face poset \(F(\partial\Delta^2)\) of the boundary of a triangle with vertices \(v_0,v_1,v_2\) and edges \(e_{01},e_{12},e_{20}\); choose v=v0 and let S be any Stone space containing at least **two** points. Set \(X=W_S(P,v)\) by gluing all copies of v across the S-indexed fibres. Then:
- Choose distinct s,t∈S and the fibre edges \(e_{01,s}\), \(e_{02,t}\). Both have **shared lower witness v**, so their binary pair belongs to \(\mathcal D(X)\). They have **no common upper witness** (the only points above e01,s lie in s-fibre, and similarly for t), so the pair does **not** belong to \(\mathcal I(X)\). Hence \(\mathcal D\nsubseteq\mathcal I\).
- In one fibre s, the two distinct minimal vertices \(v_{1,s},v_{2,s}\) have **upper witness** \(e_{12,s}\) but no common lower point, so their pair is in \(\mathcal I(X)\setminus\mathcal D(X)\). Hence \(\mathcal I\nsubseteq\mathcal D\).
- Nevertheless the **CANONICAL** maps \(\mathbf C(X)\to\mathbf I(X),\ \mathbf C(X)\to\mathbf D(X)\) are equivalences by the independently audited pointed face-poset gluing theorem and edgewise arrow theorem; their common object \(h(S)_+\wedge\underline{S^1}\) is genuinely nonconstant if S is infinite.

Thus
\[
\boxed{\mathcal I(X)\parallel\mathcal D(X)
\qquad\text{while}\qquad
\mathbf C(X)\overset{\sim}\longrightarrow
\mathbf I(X),\mathbf D(X).}
\]
This is a **working immediate consequence** of previously audited mathematics, not a new comprehensive study. It shows that **even simultaneous vanishing of the canonical homotopy cofibres does not imply a binary equality or inclusion**. We should seek information beyond the unfiltered geometric realizations if the new homotopy methods are to recover binary relation structure.

## Prioritized concrete problems for the next return to binary hierarchy

1. **Cross-fibre locus in binary D vs I.** Describe the localic/proconstructible subobject of \(\mathcal D\) consisting of pairs from distinct S-fibres above the shared ideal A. In the pointed case it is controlled by the off-diagonal \((S\times S)\setminus\Delta_S\) and the finite upper cone of v. Determine patch/topological closure issues before treating set differences as sublocales.
2. **Filtration instead of total realization.** Since the inclusions Ch→I,D realize to equivalences despite strict binary incomparability, test simplicial **skeletal filtration**, latching maps, relative 1-skeleta, or local coefficient systems on the relation groupoids for residual obstruction information. Do NOT assume the intrinsic localic shape agrees with the patched invariant.
3. **Other named relations.** Work out \(\mathcal U,\mathcal V,\mathcal W,\mathcal H\) on the same W_S(P,v) using the **established** (not guessed) locale/frame definitions in the master theorem ledger. Compare the cross-fibre witnesses, fitted/closure operations, and finite quotient/Stone parameter dependence.
4. **Composition and associativity interface.** Our earlier mixed relation-composition theorem has important nonassociativity caveats even for one locale; test whether homotopy invariants of Čech/rectangle nerves see any composition defect. First state and verify the actual diagrams and mediating maps, not merely analogies with ordinary relational composition.
5. **Separation classes vs homotopy classes.** Find coherent examples with equal (or equivalent) patched C/I/D objects but different binary inclusions/equalities; characterize which simple localization or relation-level invariants remain sensitive. Avoid trying to derive T₂/T₃ conditions merely from the vanishing of a homotopy cofibre.

**Return trigger:** At the completion of the current twisted-coefficient branch, or sooner if it becomes unproductive. The user's instruction is to **keep this as an active parked thread**, not close it in favor of homological research.

**Status and references:** The finite-poset/Cameron–Kumar type-level background and canonical arrow comparison were previously externally checked with repairs; the new precise binary benchmark is internally checked, not externally audited; and further \(\mathcal U,\mathcal V,\mathcal W,\mathcal H\) computations remain OPEN. See [v2.1 theorem ledger](PointFree_master_theorem_ledger_v2_1_2026-11-10.md), [v1.8 open register](ProjectA_open_problems_register_v1_8_2026-11-10.md), [coherent phase index](PointFree_coherent_homotopy_PHASE_INDEX_2026-11-10.md).
