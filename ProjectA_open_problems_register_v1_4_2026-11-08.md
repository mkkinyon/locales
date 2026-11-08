# Project A — Open-problem and deferred-question register

**Version 1.4 · 8 November 2026**

This register is an editorial map of *unresolved mathematical questions* and explicitly **deferred conceptual questions**. It is not a research agenda demanding immediate action, and it is separate from the [Master Theorem Ledger](ProjectA_master_theorem_ledger_v1_6_2026-11-08.md). The statuses reflect the GitHub notes through 7 November, the cumulative inventory v0.7, the FIRST Scott referee’s two reports and internal recheck, a separate SECOND blind L* referee report identifying and repairing a faulty C-ideal assertion, and the independent blind coherent-composition audit. The user has repeatedly opted not to reopen the extended \(\mathcal V\)-rank or ordinal-hull searches; those constraints are respected here.

## Conventions and status

\(\mathcal I=\operatorname{cl}\Delta\), \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal U\) is the Urysohn separation relation, \(\mathcal V=\operatorname{fit}\mathcal I\), \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal F\) is the real-functional equivalence, \(\mathcal H\) is the least closed fitted hull of \(\Delta\). For a finite-cover fitted approximation \(\mathcal D_2\), write \(\mathcal W_2=\operatorname{cl}\mathcal D_2\). For a bar-rank approximation write \(\mathcal V_n\); \(\mathcal V_{\mathrm{fin}}\) uses **all** finite-rank bars. These distinct subscripts ‘2’ are unrelated constructions.

- **OPEN**: no proof or counterexample accepted in the repository at this scope.
- **DEFERRED**: a meaningful question or organizing observation explicitly set aside; do not start a new search merely because it is listed.
- **CHECK**: a claimed theorem has a working proof but needs a targeted independent audit; **this is not an open mathematical problem**.
- **CLOSED**: historically posed question superseded by a theorem or counterexample; included solely to prevent it being reopened by reading older notes.

No ranking of mathematical importance or urgency is implied.

## A. Open problems in arbitrary-frame classification

| ID | Question | Known boundary / caution | Canonical source |
|---|---|---|---|
| CL-01 · OPEN | Does the exact arbitrary-frame criterion \(\mathcal I=\mathcal U\) admit a simple intrinsic lattice-theoretic characterization analogous to normal/conormal distributive lattices? | It already has a valid cp-ideal orthogonality-polar description; coherent frames are conormal, frame–coframes extremally disconnected. “Find a familiar class” is a conceptual/classification question, not a logically precise conjecture. | [Structural study](https://github.com/mkkinyon/locales/blob/main/A-I-equals-U-structural-study.md) |
| CL-02 · OPEN | Does **normality imply** \(\mathcal D=\mathcal U\) for every noncompact frame? | True in compact frames and in stated classical continuous normal cases; finite-cover normality alone is insufficient for the known general proof. This is not the false converse “\(\mathcal D=\mathcal U\Rightarrow\) normal.” | [Noncompact normality](https://github.com/mkkinyon/locales/blob/main/A-noncompact-normality-D-U-2026-10-21.md) |
| CL-03 · OPEN | Does \(\mathcal D=\mathcal U\) make \(\mathcal U\) internally transitive in arbitrary locales? | Holds in coherent/compact and the specified classical continuous cases. Withdrawn absorption arguments must not be reused. | [Transitivity notes](https://github.com/mkkinyon/locales/blob/main/A-D-U-transitivity-2026-10-21.md) |
| CL-04 · OPEN | Is \(\mathcal D=\mathcal U\) stable under unrestricted frame coproducts (locale products)? | Proven in the coherent class and some continuous cases; the general result is not established. | [Coproduct stability](https://github.com/mkkinyon/locales/blob/main/A-coproduct-stability-D-U-2026-10-21.md) |
| CL-05 · OPEN | Does \(\mathcal W_2=\mathcal U\) imply \(\mathcal W=\mathcal U\)? Does the stronger universal identity \(\mathcal W_2=\mathcal W\) hold? | Distinguish finite-cover **density** from cover; coherent \(\mathcal W=\mathcal U\); compact noncoherent examples do not resolve these implications. The second universal assertion would imply the first. | [W/U reconciliation](https://github.com/mkkinyon/locales/blob/main/A-WU-external-audit-reconciliation-2026-10-24.md) |
| CL-06 · OPEN | Is there a useful classification of arbitrary locales satisfying \(\mathcal W=\mathcal U\), beyond the exact pre-nucleus criterion? | The pre-nucleus \(\Phi(d_{\mathcal U})=d_{\mathcal U}\) is already necessary and sufficient, not itself a simpler separation axiom. | [Nucleus criterion](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-nucleus-criterion-2026-10-24.md) |

## B. Open mathematical questions about composition and categorical images

| ID | Question | Known boundary / caution | Canonical source |
|---|---|---|---|
| CO-01 · OPEN | **Does the fitted-diagonal cube associate in Arrieta's spatial strongly Hausdorff base \(Y\)?** \((\mathcal D_Y\circ\mathcal D_Y)\circ\mathcal D_Y\stackrel?=\mathcal D_Y\circ(\mathcal D_Y\circ\mathcal D_Y)\). | Externally verified: \(\mathcal D_Y^2\not\le\mathcal D_Y\), with a block reduction \(\mathcal D_Y=A\vee\Delta_N\) reducing cube equality to the corresponding equality for \(A\). **Nontransitivity does not imply nonassociativity.** | [Arrieta Boolean witness](https://github.com/mkkinyon/locales/blob/main/A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md) |
| CO-02 · OPEN | Which further exact mixed \(\mathcal I,\mathcal D,\mathcal U,\mathcal V\) composition laws survive without coherence or stable images? | \(\mathcal I\circ\mathcal D\le\mathcal U\) holds universally; the hoped-for upper bound \(\mathcal V\) fails even spatially; plain localic composition is not generally associative. Do not treat all three-letter formal words as unparenthesized. | [Mixed-composition reconciliation](https://github.com/mkkinyon/locales/blob/main/A-mixed-composition-external-audit-reconciliation-2026-11-07.md) |
| CO-03 · OPEN (broad) | Is there a useful intrinsic condition, weaker than coherence/proconstructibility, guaranteeing associativity of images of specific separation relations? | General associative calculus fails; coherent spectral proconstructible case has an internal categorical argument. This question has not been formulated as one sharp conjecture. | [Associativity audit I](https://github.com/mkkinyon/locales/blob/main/A-relational-composition-associativity-audit-I-2026-11-07.md) |

## C. Properness and functional separation beyond the settled cases

| ID | Question | Known boundary / caution | Canonical source |
|---|---|---|---|
| PR-02 · OPEN (broad) | What additional intrinsic hypotheses make the **strongly Hausdorff effective quotient** of a closed proper inseparability equivalence relation completely regular outside the continuous/compact classes? | Effectiveness is already Vermeulen's theorem; a strongly Hausdorff locale need not be completely regular. This concerns real-valued functions, not the existence of the quotient. | [Vermeulen correction](https://github.com/mkkinyon/locales/blob/main/A-vermeulen-effectiveness-correction.md) |

## D. Deferred conceptual observations and nonurgent programs

| ID | Deferred question or idea | Boundary / what is *not* asserted | Origin |
|---|---|---|---|
| DF-01 · **DEFERRED** | Is there an **intrinsically defined relation above \(\mathcal V\)** playing for \(\mathcal V\) a role dual to that of \(\mathcal U\) above \(\mathcal W\)? | The literal formal dual pair is \(\mathcal V=\operatorname{fit}(\mathcal I)\), \(\mathcal W=\operatorname{cl}(\mathcal D)\). \(\mathcal W\subsetneq\mathcal U\) is possible. No extra relation or notation is adopted; no claim it exists. | User's Nov 8 conceptual clarification; [motivation note](https://github.com/mkkinyon/locales/blob/main/A-V-conceptual-motivation-noncoherent-asymmetry-2026-10-24.md) |
| DF-02 · **DEFERRED** | Might \(\mathcal V_2\), the rank-two fitted inseparability approximation, have a natural role elsewhere in the separation hierarchy or mixed-composition theory? | No proposed theorem or new research agenda. Keep distinct from \(\mathcal W_2\) and from \(\mathcal V_{\mathrm{fin}}\). | User's Nov 8 response to the \(\mathcal V\)-program consolidation |
| DF-03 · **DEFERRED** | Is there an appropriate categorical **analogue of effectiveness for tolerances** (reflexive symmetric, not necessarily transitive localic relations) that could illuminate \(\mathcal I,\mathcal D,\mathcal U,\mathcal V\) and related relations? | Kernel pairs are always transitive, so **ordinary effectiveness cannot literally characterize a nontransitive tolerance**. One would first need to specify the desired kind of representation, quotient, span or universal property. The status of relevant categorical literature has **not been investigated**. No assertion is made about standard definitions or existence of such an analogue. | User's question, 8 Nov 2026, explicitly deferred |
| DF-04 · **DEFERRED** | Does a useful *non-tautological* arbitrary-frame description of \(\mathcal V\) exist, perhaps in terms of a manageable class of geometric or filter-based certificates? | All-bar separation trees are exact but essentially coordinatize fitting; coherent dual-far strips do not suffice in general. Do not restart the historical search. | [V consolidation](https://github.com/mkkinyon/locales/blob/main/A-V-alternative-intrinsic-duals-2026-10-22.md) |
| DF-05 · **DEFERRED** | Does the regular completion of finite-rank bar filters recover the full bar filter in *every* frame? | A specific generic-point example has a positive result; a spatial-square condition gives another sufficient case. Not to be confused with the **refuted** strongly exact or fitted finite-rank exhaustion assertion. | [Regular completion](https://github.com/mkkinyon/locales/blob/main/A-V-regular-filter-completion-full-generic-example-segment-three-2026-10-24.md) |
| DF-06 · **DEFERRED** | Can strict higher fitted stages \(\mathcal V_n\supsetneq\mathcal V_{n+1}\) be constructed uniformly for all finite \(n\)? | Strictness at ranks 2→3 and 3→4 is established/externally supported. Taking disjoint unions of high individual *bar* ranks does **not** prove strict fitted stages. | [Bridge reconciliation](https://github.com/mkkinyon/locales/blob/main/A-V-noncofinite-bridge-external-audit-reconciliation-2026-10-23.md) |
| DF-07 · **DEFERRED** | Can the closed-fitted hull's ordinal stabilization exceed \(\omega+m\) in a conceptually useful way, or can one classify its possible closure ordinals? | Coherent examples of exact \(\omega+m\) are independently audited. The user explicitly chose not to pursue additional ordinal constructions. | [Formal hull](https://github.com/mkkinyon/locales/blob/main/A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md) |
| DF-08 · **DEFERRED** | General preservation properties of \(\mathcal H\), \(T(\mathcal J)\), and the named full sublocale hulls under arbitrary locale products. | Natural comparison \(R_{X\times Y}\le R_X\times R_Y\) is known internally, but equality fails for \(\mathcal J\), even finite coherent. No universal equality for \(\mathcal H\) is claimed. | [Preservation note](https://github.com/mkkinyon/locales/blob/main/A-V-relation-hierarchy-duality-preservation-2026-10-21.md) |

## E. Independent-proof checks — deliberately **not** counted as open problems

The coherent-composition check CK-01 and the unrestricted Scott-continuity check CK-02 are both complete after distinct focused blind external reports. The referee-origin uniform hull formulas are separately recorded as E* in the theorem ledger; they are not new open problems.

| ID | Proof needing focused verification | Current classification |
|---|---|---|
| CK-01 · CLOSED | Localic \(\mathcal I=A\circ B\), \(\mathcal D=B\circ A\), and proconstructible spectral-image associativity | `E` — blind 8 Nov referee confirms, supplies the compact-preserving quotient and fitted-diagonal congruence repairs; see [reconciliation](project-a/audits/2026-11-08/ProjectA_coherent_composition_EXTERNAL_referee_reconciliation_2026-11-08.md) |
| CK-02 · CLOSED | Universal compact-fitted family K→P_U X is proper; unrestricted localic Scott converse L* | `E` — different SECOND blind referee checks FIRST referee’s proof, **with a necessary repair:** principal downsets are not generally C-ideals. See [reconciliation](project-a/audits/2026-11-08/ProjectA_Lstar_second_blind_referee_reconciliation_2026-11-08.md) |
| CK-03 | Combined **subfit + arithmetic** counterexample \(\mathcal I=\mathcal U\subsetneq\mathcal F\), including its two sobrification points | `I` (claim established internally, not externally audited) |
| CK-04 | Repaired transfer characterization and seven-of-eight associative transfer words | `I` after earlier external comparison |
| CK-05 | Supplement-filter and almost-normal/subfit \(\mathcal V\) deductions; all-class compact and regular rank bounds as standalone package | `I` (with independently audited negative examples) |
| CK-06 | General named-relation naturality, noncoherent transitive \(\mathcal H\) example, full spectral-sublocale Hochster lift | `I` (new syntheses) |

## F. Historical questions **closed**, to prevent accidental reactivation

| Former question/claim | Disposition |
|---|---|
| “Are closed proper equivalence relations effective only on compact locales?” | **CLOSED:** Vermeulen 1994 Cor. 5.17 works for arbitrary ambient locales. |
| “Does an internal equivalence relation automatically make \(r_E\) idempotent?” | **CLOSED (false):** paired-point counterexample; properness is sufficient. |
| “Is the Scott-continuity converse open even for continuous or arbitrary locales?” | **RESOLVED with independent blind verification:** the unrestricted theorem L* for arbitrary closed localic relations is E after a SECOND referee checked the FIRST referee’s proof. The false principal-downset sentence must be corrected in a final proof. This does **not** settle functional-quotient problems. |
| “Does \(\mathcal I=\mathcal U\) imply \(\mathcal U=\mathcal F\) for continuous locales?” | **CLOSED (false):** deleted-plank/cofinite-cloud examples, externally checked. |
| “Might adding both subfitness and arithmeticity restore \(\mathcal I=\mathcal U\Rightarrow\mathcal U=\mathcal F\)?” | **CLOSED as working conjecture (counterexample):** combined construction exists but external verification CK-03 remains. |
| “Can finite-rank bars always generate \(\mathcal V\)?” | **CLOSED (false):** \(\mathcal V\subsetneq\mathcal V_{\mathrm{fin}}\), independently blind audited. |
| “Is \(\mathcal W=\mathcal U\) automatic for compact locales?” | **CLOSED (false):** compact noncoherent counterexample; coherent case positive. |
| “Does almost-normality force \(\mathcal V\) closed?” | **CLOSED (false):** noncompact thickened-zigzag example. |
| “Does nontransitivity of Arrieta \(\mathcal D_Y\) establish cube nonassociativity?” | **NOT a valid inference:** cube question CO-01 remains open. |
| “Can one freely omit parentheses in localic composition of endorelations?” | **CLOSED (false):** same-locale and symmetric reflexive nonassociativity witnesses. |

## Editorial control

When using the older chronological index, **prefer the latest explicit correction** over an old heading. Never infer a theorem's external verification from a related but different referee packet. Treat mathematical openness, proof-audit status, and research priority as three independent properties. This register records questions, not commitments to investigate them. See [Scott referee reconciliation](project-a/audits/2026-11-08/ProjectA_Scott_converse_external_referee_reconciliation_2026-11-08.md) for the topological correction, and [L* reconciliation](project-a/audits/2026-11-08/ProjectA_Scott_converse_Lstar_report2_INTERNAL_reconciliation_2026-11-08.md) for the historical provisional result; the independently checked final disposition is [second blind L* reconciliation](project-a/audits/2026-11-08/ProjectA_Lstar_second_blind_referee_reconciliation_2026-11-08.md). The two new conceptual questions DF-02 and DF-03—especially tolerances/effectiveness—are intentionally left dormant.