# Unified Point-Free Topology — focused review of counterexamples, ranks and topology precedents
## 21 November 2026 · Endgame literature Segment 6

**Scope.** A deliberately narrow claim-to-literature review of four strongest counterexample/rank groups before beginning a full project consolidation. Each group records its exact mathematical assertion, proof/audit provenance, conventional ingredients, conceptual distinction and place in the final archive. **No general originality or priority certificate; absence of an exact result in this search does not prove novelty.**

## Executive triage

| Theme | Best authoritative project source | Correctness / proof provenance | Recommended final location |
|---|---|---|---|
| Finite-rank bars do not recover fitted inseparability | [Vfin consolidated proof](A-Vfin-negative-consolidated-proof-2026-10-23.md) | original and repair externally blind-reviewed; refined transfer proof independently checked | principal theorem/example of hierarchy track |
| Connected compact strict W/H/U diamond | [W-phase referee reconciliation](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md) and [original audited packet](project-a/audits/2026-11-09/Wphase/ProjectA_Wphase_EXTERNAL_BLIND_packet_2026-11-09.md) | positive blind review with explicit repairs; later additions separately internal | illustrative hierarchy counterexample, not central flagship |
| Finite-cover versus all-cover closed hull, Q and Q′ refuted | [dense rational bridge canonical](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) | positive blind and internal audit; exact Φ/Φ₂ correspondence checked subsequently | principal theorem/example of hierarchy track |
| Bounded graph diameter versus unbounded *localic composition* rank | [Stone clique rank canonical](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) and [referee reconciliation](ProjectA_BOUNDED_DIAMETER_RANK_EXTERNAL_AUDIT_RECONCILIATION_2026-11-20.md) | diameter 3/2 formulas blind reviewed; diameter 1 exact n+2 referee-addendum origin and independently checked *internally* | principal example in composition/graph-algebra track |

**Two different ranks, never conflate:** V-separation-tree rank is proof-tree depth for \(w\vee d_I=1\) in a **frame coproduct**; Stone-clique rank is minimum length of a **genuine image/pullback relation-composition word**, universally or existentially over parenthesizations. Classical graph diameter is neither rank. Formal connections would require a new theorem; none is asserted.

## A. V separation-tree ranks and V<V_fin

For \(L=\mathcal O(X)\), \(Q=L\oplus L=\mathcal O(X\times_{\rm Loc}X)\), let \(d_I=\bigvee_{u\wedge v=0}u\boxtimes v\). A bar is \(w\in Q\) with \(w\vee d_I=1\). Define rk(w) via well-founded **horizontal and vertical exact join cover trees**, leaves either disjointness \(u\wedge v=0\) or rectangles \(u\boxtimes v\le w\). Each node measures complexity of a **presentation proof**, not Cantor–Bendixson derivative rank.

\[ V=\operatorname{fit}(I),\quad
 V_{\mathrm{fin}}=\bigwedge_{\text{bars }w,\;\mathrm{rk}(w)<\omega}O(w).
\]
Original inductive **K-fan strips** yield arbitrarily large finite ranks and rank-\(\omega\) two-rectangle bar on a countable first-countable **Hausdorff** input \(Y\). Crucial strengthening: [Vfin negative consolidated proof](A-Vfin-negative-consolidated-proof-2026-10-23.md) constructs a countable first-countable **sober T0** \(X_0\) with \(V(X_0)\subsetneq V_{\mathrm{fin}}(X_0)\). Its witness is an **ordinary** point of the localic square, surviving all finite-rank bars but not one \(\omega\)-rank bar. An additional countable first-countable **T1** non-Hausdorff example also has strictness, but **do not assert sobriety for that T1 upgrade**: the canonical source expressly does not claim it. The T1 case uses graph-density and nucleus fixed-point reasoning rather than the same ordinary-point witness.

The distinction *arbitrary finite ranks* vs *strict V<Vfin* is essential: lack of finite bar-neighborhood cofinality alone does not imply strict fitted sublocale inequality, since the join of nuclei can stabilize beyond ordinary finite generation. This warning is already explicit in [V-rank consequences](A-V-unbounded-rank-consequences-for-fitted-relation-2026-10-22.md).

**Classical substrate:**
- C-ideal/frame coproduct and coverage generation: Picado–Pultr, *Frames and Locales* (2012), Ch. VIII; Johnstone *Stone Spaces* (1982). Tomáš Jakl and Achim Jung, *Free Constructions and Coproducts of d-Frames*, LIPIcs CALCO 2017 (DOI 10.4230/LIPIcs.CALCO.2017.14) explicitly use C-ideal/coverage universal constructions, as do localic presentation papers. These explain why well-founded proof trees are natural but do **not** provide this particular rank hierarchy.
- K-topology / Smirnov deleted-sequence topology is a **known Hausdorff nonregular** space. The selected fan input uses a countable rational version with a closed convergent sequence of isolated points; the underlying pathology is classical. Munkres, *Topology*, contains the K-topology paradigm; exact source of the *iterated K-fan rank construction* not located.
- Cantor–Bendixson ordinal ranks are standard, but the proof-tree rank here is *not* identical to Cantor–Bendixson height. Some project bounds use CB data as auxiliary controls, not as a definition.

**Literature search result:** queries for “sublocale” + “separation tree” + “rank”, “frame coproduct” + ordinal proof-tree depth, and site/coverage depth did not locate a theorem equivalent to \(V\subsetneq V_{\mathrm{fin}}\), or exact \(\omega\)-rank of these diagonal-specific bars. This is a **limited search result**, not an originality claim. **Value:** strong negative theorem about genuinely point-free neighborhood generation.

## B. Connected compact strict W/H/U diamond

**Independently reviewed** [W-phase archive](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md), with the blind packet §8 and corrections. Construct \(Z=P\times Y\): P a connected finite five-point zigzag/fence, Y a connected compact two-apex locally compact sober noncoherent space over real-line core. There is an exact strict diamond:
\[
W(Z)=H(Z)\wedge U(Z)
< H(Z),U(Z),\qquad H(Z)\vee U(Z)<F(Z)=Z^2,
\]
where H(Z) and U(Z) are incomparable and the inequalities mean each strict inclusion separately. Importantly **the independent referee showed the two strictness mechanisms are factorwise**: one from P, one from Y. Connected and non-disjoint-sum is true, **intrinsically coupled defects not shown**.

Known ingredients: finite upper-Alexandrov posets and their specialization/comparability graph calculus, point-generated cofinite apex constructions, connected non-Hausdorff gluing, and the established sublocale/fitting operations. Existing Arrieta 2024 anti-Urysohn example already gives a very strong *different* strictness \(I=\Delta<U=F=X^2\); don't claim this new diamond is first-ever separation strictness. **Exact full Z-relational pattern not located** in the searched Arrieta/Isbell classical sources. For publication, avoid making this example a major standalone theorem when its mechanism is a product of two simpler examples. It is excellent for illustrating incomparability and finite-factor transport.

Source status: W-phase main theorem received blind external review subject to detailed corrections. Later A3–A5 referee suggestions are *internally checked only* and should not be counted as originally blind-audited. Original November 9 historical texts still label Q/Q′ open; those flags are superseded by November 14.

## C. Dense-rational-bridge finite-cover obstruction, now quasi-Polish

Exact canonical external-audited theorem: second-countable, sober, locally compact, T1 non-Hausdorff **étale space** \(p:X\to\mathbb R\) with two or three points per fiber, and
\[
D(X)=\Delta,\qquad W(X)=I(X)<W_2(X)=U(X)=X\times_{\mathbb R}X.
\]
This refutes Q and Q′. The finite-cover and all-cover pre-nuclei satisfy \(\Phi(0)=\Phi_2(0)=d_U\); the strictness emerges **after** nucleus iteration. Pointwise \(D\) and \(D_2\) are the same Cameron–Kumar closure-meeting graph (elementary consequence), but in the bridge sector J the *pointless* Booleanization B(J) lies in \(D_2\) but is excluded from D, and its closed support forces W2 to fill J. See [canonical §1–7](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md).

**New precise link with published domain theory (21 Nov literature segment, not in original blind packet):**
Matthew de Brecht, *Quasi-Polish Spaces*, *Annals of Pure and Applied Logic* 164(3) (2013), 356–381, DOI 10.1016/j.apal.2012.11.001, arXiv:1108.1445, **Theorem 44**: *every countably based locally compact sober space is quasi-Polish*. This is restated with exact theorem number by Goubault-Larrecq, [*Remainders, bqos, and quasi-Polish spaces again*](https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=865) and in de Brecht–Pauly's work. Hence our X is **quasi-Polish**, despite T1 non-Hausdorffness. Precisely:
\[
\exists\ X\text{ locally compact, quasi-Polish, T1, non-Hausdorff}:\quad W=I<W_2=U.
\]
This is an **immediate corollary from the old theorem plus our audited construction**, not a freshly audited separate construction. It belongs in the canonical theorem note as an explicitly later literature corollary.

**Adjacent but non-equivalent classification:** de Brecht, *A Generalization of a Theorem of Hurewicz for Quasi-Polish Spaces*, *Logical Methods in Computer Science* 14(1) (2018), identifies four canonical countable forbidden spaces \(S_0,S_1,S_D,S_2\); the S1 cofinite topology is T1 **but not sober**, whereas our space is sober and quasi-Polish. Thus the standard S1 example does not subsume ours. The well-known non-Hausdorff line with doubled origins/étale sheaf spaces supplies a *topological* precursor, not the dense-cover Booleanization theorem.

**Pointfree classical foundation:** Isbell's least dense Boolean sublocale, dense-open intersections, and general covers/entourages in Picado–Pultr are known. The post-stabilization \(W<W_2\) remains an exact localic relation computation with no predecessor found in targeted searches.

## D. Ordinary diameter ≤1 but unbounded localic composition rank

Separate from A and C; belongs with the graph-algebra story. [Stone clique rank canonical](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) (20 Nov). Let H_n be a reflexive symmetric point-generated relation, a finite join of ordinary cliques on a Stone space G_n. Its ordinary connected components are **cliques** (diameter ≤1). But the induced spatial component sublocales U_j can have **nonzero pointless overlaps** between adjacent components, forming an overlap graph path of length n+1. Every bracketing at precisely length n+2 reaches the full localic kernel pair, and none shorter does:
\[
r_{\exists}(H_n)=r_{\forall}(H_n)=n+2.
\]
This exact formula is **referee-addendum origin, internally checked**; the original diameter-2 and diameter-3 rank formulas \(2n+4\), \(3n+4\) received independent blind audit. The independently audited compact-Hausdorff RC theorem (20 Nov) later established an associative finite-join rectangle algebra including point-generated cliques; it does not undo the independently checked exact numerical bounds. The overlap-graph pointfree criterion is a stronger general formula than a bare example.

Known ingredients: dense disjoint subsets of perfect Stone spaces, nonzero **pointless intersections** of their induced sublocales, the least dense sublocale of a locale, and familiar graph diameter/paths. The localic image/pullback rank is not classical ordinary graph diameter and is not the separation-tree rank in A. **Exact antecedent of this unbounded localic composition-rank phenomenon not located** in the searches; the underlying pointfree intersection phenomenon is classical.

## E. Literature/context matrix and no-priority warning

| Existing theory/source | Exact part inherited | What is not settled by it |
|---|---|---|
| K-topology, cofinite fans, non-Hausdorff lines | topology used in counterexamples | precise V-rank / W-H-U / finite-cover hull results |
| Cantor–Bendixson analysis | standard ordinal height and scatteredness | proof-tree V-rank or power-composition rank equivalence |
| C-ideals and frame coproduct sites (Johnstone, Jakl–Jung 2017) | frame presentation, infinitary joins, well-founded proofs | strict \(V<V_{\mathrm{fin}}\) specific family |
| de Brecht 2013 quasi-Polish theorem | Q-bridge belongs to quasi-Polish class | Q/Q′ obstruction and Boolean support computation |
| de Brecht 2018 forbidden subspaces | standard non-quasi-Polish pathologies | Q bridge, which *is* quasi-Polish |
| Isbell density, Booleanization | nonspatial dense witnesses | precise relation composition/hull rank formulas |
| Arrieta 2024 separation counterexamples | strong H versus Urysohn/fitted strictness already known | full W-H-U connected diamond |
| Picado–Pultr nearness/cover filters | finite/all cover methodology | post-stabilization finite-cover hull strictness |

**Publication judgment:** The most defensibly distinctive hierarchy examples are **V<Vfin** and the **Q/Q′ finite-cover bridge**; the connected diamond is a useful compact visual example and transition to graph interpretation, but the two mechanisms are separable. The ordinary-diameter-one/unbounded localic rank construction is the strongest pedagogical bridge to the proposed *composition paper*. These are recommendations, not originality certificates; the remaining gap is a much broader historical search in specialized topology/domain/formal-locale literature.

## F. Practical final-archive example shortlist

Recommend short proofs + maps to full sources for:
1. A minimal finite upper-Alexandrov example showing the full \(\mathcal I,\mathcal D\) diamond and specialization orientation.
2. Arrieta's **published** strongly Hausdorff anti-Urysohn space \(I=\Delta<U=F=X^2\), as *known benchmark*.
3. A two-apex or five-point-fence compact example displaying W≠U, plus a short diagram for connected Z=P×Y if desired (reviewed).
4. V<Vfin finite-rank fan and \(\omega\)-rank transfer (reviewed).
5. Dense-rational-bridge finite/all cover counterexample, with newly deduced quasi-Polish classification (reviewed underlying construction).
6. A simple p/q point-generated versus full relation example; clique overlap graph of diameter one with unbounded image/pullback rank (reviewed with addendum).
7. Optional: coherent finite comparability zigzag illustrating exact relational powers; optional higher-Dowker non-descent witness from later fourth audit.

Seven items in the expanded pool, **not** seven mandatory chapters; choose 5–6 for a concise main exposition, put extras in supplementary examples.

## G. Endgame next actions

- Consolidate canonical theorem ledger; clearly tag later post-referee additions and imported prerequisites.
- Promote quasi-Polish corollary into the Q/Q′ canonical statement as an **after-audit consequence**, without changing the audit report.
- Put the two rank definitions side by side in the research overview, with no unproved comparison.
- Keep the connected diamond's **factorwise** caveat.
- Do **not** launch new arbitrary-ordinal rank search or search for an intrinsically coupled diamond just to enhance the results count. 
- No missing primary PDF is currently blocking this focused verdict. A historical deep bibliographical review could later examine proof-theoretic inductive frame presentations, but the practical next step is consolidation.
