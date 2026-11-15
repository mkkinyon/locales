# Project A — open/closed two-sheet specialization: external referee reconciliation

**15 November 2026.** Canonical mathematics: [two-sheet one-step theorem and post-referee structural corollaries](ProjectA_OPEN_CLOSED_TWO_SHEET_ONE_STEP_CONSOLIDATION_2026-11-15.md). This document records **which conclusions were independently refereed**, which were added afterward, and the stopping boundary. Correctness and literature priority are distinct questions; no originality claim is made.

## 1. What the independent blind referee checked

The reviewer was supplied the [prompt](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Blind_prompt.md) and [packet](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Blind_packet.md) but **not** the prior [internal adversarial audit](ProjectA_OPEN_CLOSED_TWO_SHEET_INTERNAL_ADVERSARIAL_AUDIT_2026-11-15.md). Its [original report](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Referee_report_original.md) gives a **positive verdict without mathematical repairs** on:

1. **Exact cross-sheet specialization**: \(\mathcal A(Z)\wedge(F\times U)=\Delta_K(P)\), using *arbitrary locale test domains*, not merely ordinary points. Same-sheet blocks are diagonal, reverse cross block zero.
2. **Arbitrary first-sheet source**: \(\operatorname{Sat}_{\mathcal A,Z}(H_F)=\operatorname{fit}_Z(H_F)=H_F\vee(P\wedge H)_U\), even when \(H\) is not closed, compact, or spatial.
3. **Finite-join propagation** of equality between saturation and fitting; the proof uses monotonicity and the coframe's finite distributivity, never preservation of arbitrary joins by saturation.
4. **One-step formula for every source**: \(\operatorname{Sat}_{\mathcal A,Z}(G)=\operatorname{fit}_Z(G)=G\vee(P\wedge(G\wedge F))_U\), and idempotence.
5. **Cantor discrete-defect example**: a nonzero pointless interface and an explicit failure of arbitrary-join preservation. The referee supplied an independent Booleanization argument for the nonzero remnant.

The referee confirmed that **compactness or spatiality of K are unnecessary** for the general theorem, while zero-dimensionality is genuinely used. Its six expository requests (block decomposition, cross projection, relative fittedness, proper coframe law, Booleanization witness, meaning of \(\Delta_K(P)\)) have been incorporated into the canonical theorem.

## 2. The later mathematical addendum: separate status

Only *after* the blind report, the reviewer supplied [additional mathematical ideas](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Referee_followup_original.txt). Those propositions were **not** part of the independently audited packet. A subsequent internal check supplied complete arguments and strengthened several statements; these appear in §§8–11 of the [canonical note](ProjectA_OPEN_CLOSED_TWO_SHEET_ONE_STEP_CONSOLIDATION_2026-11-15.md).

| Later statement | Current status | Location |
|---|---|---|
| Complete-lattice coordinates \(\mathcal S(Z)\cong\mathcal S(K)^2\) and fitted iff \(P\wedge H\le C\) | Internally checked corollary | §8 |
| Exact arbitrary-join criterion \(P\wedge\bigvee H_i=\bigvee(P\wedge H_i)\) | Internally checked corollary | §9 |
| Spatial \(K\) and nonzero pointless \(P\) force failure of arbitrary-join preservation | Internally checked strengthening | §9 |
| Realization \(L_P=\{(c,v):i^*c\le i^*v\}\) and largest-frame property | Internally checked theorem | §10 |
| Order-reversing correspondence \(L\subseteq L_P\iff P\le P_L\) | Internally checked strengthening | §10 |
| For spatial \(K\): \(T_1\iff\) all ordinary points fitted \(\iff\operatorname{pt}(P)=\varnothing\) | Internally checked strengthening | §11 |

The realization is sharp: **the interfaces of admissible zero-dimensional two-sheet gluings are exactly the fitted sublocales**. Two different subframes with the same \(P\) may have different open-set structures, despite identical saturation/fitting formulas in the sheet coordinates. The maximal representative \(L_P\) does *not* in general retain local compactness.

## 3. Important connection to an existing construction

The case \(P=B_K\), the Booleanization of Cantor space, gives the frame
\[
L_{B_K}=\{(c,v):c^{**}\le v^{**}\}.
\]
This is **already** the [Boolean lax-double control construction](ProjectA_LCPT_BOOLEAN_LAX_DOUBLE_NONLC_CONTROL_2026-11-15.md). That existing note contains an **internally checked** way-below proof of its failure of local compactness, followed by a generalization to nonzero pointless quotients over compact metrizable Hausdorff bases. It has **not** been independently blind-refereed. The maximal realization is therefore not a substitute for the independently verified *locally compact* [Cantor discrete-defect gluing](ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md), whose frame is more selective.

The relation to the pre-existing lax-double note corrects a potential chronological misimpression: the way-below obstruction was already documented in the repository before this referee follow-up, even though the new realization theorem gives it a clean universal interpretation.

## 4. Consolidation disposition and next choice

**Closed for now:** the exact four specialization blocks, all-source one-step formula, fitted classification, join-preservation obstruction, maximal realization, and ordinary-point criterion in the stated two-sheet framework. The first group is **externally confirmed**; the follow-up structural corollaries are **internally checked only**. The external referee's original packet, internal audit, original report and later addendum remain distinguishable in the [audit archive](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/README.md).

**Deferred within this branch:** smallest admissible frames for a fixed interface, wider realization hypotheses, local-compactness/coherence constraints, and classification of all join-continuous fitted interfaces.

**Agreed agenda:** only two candidates are to be compared for the next active direction: **second-countable (LC-PT)** and **the graph/homotopy connection**. Other questions stay in the background. No new external audit is asserted or implied for the post-referee deductions; if they become central to a later theorem, they remain eligible for targeted independent review.
