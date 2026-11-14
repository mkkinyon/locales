# Project A — Post-Q/Q′ frontier consolidation, duality limits, and next priorities

**14 November 2026.** Bounded consolidation of the unified Point-free Topology project after the independently blind-refereed dense-rational-bridge theorem. The aim is to distinguish settled universal questions, positive restricted classes, new internally checked consequences, and genuinely open frontiers. This is **not** a new independent audit or an originality claim. Dated historical notes should be read with the supersession information below.

## 1. Main status change: Q and Q′ are both false

Write (\mathcal D=\operatorname{fit}(\Delta)), (\mathcal D_2=\bigwedge_{\mathscr F\text{ finite cover}}\mathfrak o(w_{\mathscr F})), (\mathcal I=\operatorname{cl}(\Delta)), (\mathcal W=\operatorname{cl}(\mathcal D)), and (\mathcal W_2=\operatorname{cl}(\mathcal D_2)), with (w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c). Let (\mathcal U) be the closed Urysohn relation.

- **Q′:** universal (\mathcal W=\mathcal W_2). **False.**
- **Q:** universal implication (\mathcal W_2=\mathcal U\Longrightarrow\mathcal W=\mathcal U). **False.**

The [canonical example](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) is a second-countable, sober, locally compact, (T_1), non-Hausdorff space (X_{\mathbb Q}), étale over (\mathbb R), with
\[
\boxed{\mathcal D=\Delta,\qquad \mathcal W=\mathcal I<\mathcal W_2=\mathcal U= X_{\mathbb Q}\times_{\mathbb R}X_{\mathbb Q}.}
\]
The main example survived internal and independent blind external audits; the exact comparison with the original \(\Phi,\Phi_2\) formulation was checked after that external audit. See the [referee reconciliation](ProjectA_Q_DENSE_RATIONAL_BRIDGE_REFEREE_RECONCILIATION_2026-11-14.md) and [audit archive](project-a/audits/2026-11-14/Q-dense-rational-bridge/README.md). Source originality has not been assessed.

The parametrized dense-bridge family (X_E), (E\subseteq\mathbb R) dense, has an [internally checked extension](ProjectA_Q_DENSE_BRIDGE_PARAMETER_FAMILY_INTERNAL_2026-11-14.md); this is not part of the blind review.

## 2. Exact compactness boundary and the limitation of duality

**Proposition (elementary, internally checked here).** For **every compact locale** (X),
\[
\boxed{\mathcal D_2(X)=\mathcal D(X),\qquad \mathcal W_2(X)=\mathcal W(X).}
\]
**Proof.** Every cover (\mathscr C) has a finite subcover (\mathscr F\subseteq\mathscr C). Since (w_{\mathscr F}\le w_{\mathscr C}), we have (\mathfrak o(w_{\mathscr F})\le\mathfrak o(w_{\mathscr C})). Consequently (\mathcal D_2\le\mathfrak o(w_{\mathscr C})) for every cover (\mathscr C), so (\mathcal D_2\le\mathcal D); the reverse inclusion always holds. Apply closure. \(\square\)

Thus **Q′ holds** on compact locales and **Q holds** there as an implication, although (\mathcal W=\mathcal U) need not hold on every compact locale. Coherent locales (spectral spaces) are compact, and stably compact spaces are compact. Neither Hochster duality of spectral spaces nor standard involutive de Groot duality of stably compact spaces can turn the noncompact bridge into a counterexample *within those categories*.

The coherent Hochster duality correctly exchanges the **named spectral sublocales** (\mathcal I\leftrightarrow\mathcal D) and (\mathcal U\leftrightarrow\mathcal V) after reversing the Priestley specialization order, with the appropriate induced dual topologies. The coherent equality-property exchange (\mathcal I=\mathcal U\longleftrightarrow\mathcal D=\mathcal U) is recorded in [Hochster duality of the equality conditions](A-Hochster-duality-I-D-2026-10-21.md), and the relation-level analysis in [spectral duality](A-V-Hochster-duality-spectral-relations-2026-10-23.md). These facts **do not** identify the finite-cover (\mathcal D_2) with an existing (\mathcal V_n) under duality, and do not license dualizing arbitrary noncoherent sublocales by point-set order reversal.

**Proposition (new elementary check).** The bridge space (X_{\mathbb Q}) is not even *stably locally compact* in the standard topological sense. Indeed,
\[
K_S=\{s_x:0\le x\le1\},\qquad
K_N=\{s_x:0\le x<1\}\cup\{b_1\}
\]
are compact: (K_S) is a compact interval in (S), and (K_N) is a compact interval in the global étale section (N_1\cong\mathbb R). Their intersection is (s([0,1))), which is not compact. As the space is (T_1), both are saturated. Thus intersections of compact saturated subsets need not be compact, violating the stability/coherence requirement in the definition of stably locally compact spaces. There is no involutive de Groot transport of this example under the standard hypotheses.

One may form a *cocompact topology* on spaces outside the stably compact class; doing so alone does not give the involution or preserve the localic relation constructions required to transport Q/Q′. A separate theorem would be necessary.

**A genuine extension that already fails:** the compact-spectral *pointwise specialization-witness formulas* cannot be extended unchanged to all locally compact sober spaces. In (X_{\mathbb Q}), the (T_1) specialization order is equality, yet (\mathcal I) contains non-diagonal inseparable bridge pairs and (\mathcal U) contains the entire nontrivial fiber square. Thus order reversal alone cannot recover these relations beyond the coherent setting.

Primary background for de Groot duality and stably locally compact spaces: J. Goubault-Larrecq, *De Groot duality and models of choice: angels, demons and nature*, *Mathematical Structures in Computer Science* (2009), §2; and [Goubault-Larrecq's detailed account](https://lsv.ens-paris-saclay.fr/Publis/PAPERS/PDF/JGL-mscs09.pdf). The relation-level Hochster claims are project results with their own stated audit qualifications.

## 3. The immediate cover-theoretic inventory

| Hypothesis on (X) or its covers | Conclusion / status | Audit level |
|---|---|---|
| (X) compact | (\mathcal D=\mathcal D_2), hence Q and Q′ hold | Elementary proof above |
| Every cover has a locally finite open refinement | (\Phi=\Phi_2) pointwise, hence (\mathcal D=\mathcal D_2) | [Internal proof](ProjectA_Q_LOCAL_FINITE_COVERS_PRENUCLEUS_EXACT_INTERCHANGE_2026-11-12.md) |
| (X) spatial hereditarily Baire and every cover has a point-finite open refinement | (\mathcal D=\mathcal D_2) | [Internal proof, not independently audited](ProjectA_Q_BAIRE_POINTFINITE_RIGIDITY_AND_FAR_REDUNDANCY_2026-11-12.md) |
| Locally compact sober metacompact space | (\mathcal D=\mathcal D_2) by the preceding internally checked result | Internal only |
| Merely \(\sigma\)-locally finite / point-countable refinements | Insufficient for Q′: (X_{\mathbb Q}) is second countable (hence Lindelöf) | Elementary deduction from audited counterexample |
| Point-finite refinement without hereditary-Baire hypotheses, including genuinely pointless cases | No general theorem or counterexample established here | Open boundary |

**The bridge does not refute the point-finite candidate.** In fact its section atlas has **no** point-finite refinement. If (G_q\subseteq N_q) is a refining member covering the unique bridge (b_q), then (U_q=p(G_q)\subseteq\mathbb R) is open and contains (q). Point-finiteness of the (G_q) forces point-finiteness of the (U_q): infinitely many (U_q) containing (x) would put either (s_x) or (t_x) in infinitely many (G_q). But for an enumeration (\{q_n\}) of (\mathbb Q), every tail union \(\bigcup_{k\ge n}U_{q_k}\) is open dense; Baire category gives an (x) in all tail unions, contradiction. This Baire proof was checked in the bounded 14 November discussion; no new external audit is claimed.

**Stopping rule:** Do not begin another protracted Q/Q′ counterexample search. Retain the point-finite/general-locale distinction as a deferred structural question.

## 4. Current map of the merged research program

| Strand | Established / consolidated | Present frontier and choice |
|---|---|---|
| Original binary hierarchy | (\Delta,\mathcal S,\mathcal I,\mathcal D,\mathcal U,\mathcal V,\mathcal W,\mathcal M,\mathcal J,\mathcal H,\mathcal F), many strictness and equality tests; [revised graph-to-locale diagram](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md) | **Highest research priority:** structural criterion for (\mathcal S=\mathcal M), first coherent, then arbitrary locales |
| Finite ranks, fitted approximations and W-phase | Unbounded separation-tree phenomena, exact coherent results, Q/Q′ negative | Consolidate and archive bounded tests; stop chasing nearby residuals without a new mechanism |
| Localic relation composition | Coherent calculus, special graph-power identities, mixed-composition and associativity controls | Maintain proofs; pursue only a clearly motivating new question |
| Higher diagonals, Dowker and coherent homotopy | Several independently audited canonical hull/groupoid statements; [phase index](PointFree_coherent_homotopy_PHASE_INDEX_2026-11-10.md) | New [classifying-anima identification](PointFree_classifying_anima_identification_2026-11-11.md), [crosscut ladder](PointFree_crosscut_connectivity_ladder_2026-11-11.md), and relative obstruction modules are **internally checked** and await a focused external audit before further expansion |
| Free-product reconstruction, internal cohomology, pro-homotopy, intrinsic localic shape | Exploratory results and literature interfaces | Deferred until after returning to the original binary structure |

The project remains **one merged A/C program**; historical B remains archived. Publication priority/novelty has not been established by mathematical audits and must be checked separately.

## 5. Next exact question: (\mathcal S=\mathcal M)

Let (\mathcal A) be the localic specialization relation, (\mathcal S=\mathcal A\vee\mathcal A^{\smile}), and (\mathcal M=\mathcal I\wedge\mathcal D). The established frame-level inclusions and hull identities are
\[
\mathcal S\le\mathcal M,\qquad
\operatorname{cl}(\mathcal S)=\mathcal I,\qquad
\operatorname{fit}(\mathcal S)=\mathcal D.
\]
For finite posets, the [Cameron–Kumar revisitation](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md) gives the benchmark (\mathcal S=\mathcal M) iff every relevant order interval is a chain. The next bounded study should:

1. Recheck the exact finite interval criterion and minimal witnesses to strictness.
2. Seek a coherent Priestley/compact-open-lattice formulation, tracking *actual spectral sublocales* rather than only point pairs.
3. Ask whether any proposed coherent criterion has a meaningful frame/nucleus formulation without compact coherence; test noncoherent controls immediately.
4. Stop after two or three substantial segments if the answer only rephrases a growing residual.

Keep formal iterates/rank overlays distinct from the core binary Hasse diagram. This segment is a **frontier and dependency consolidation**; the mathematical (\mathcal S=\mathcal M) investigation begins next.
