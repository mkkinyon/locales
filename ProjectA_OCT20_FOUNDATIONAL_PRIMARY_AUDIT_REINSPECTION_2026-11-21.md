# October 19–20 foundational audit originals: direct inspection and source reconciliation
## Point-free topology · November 21, 2026 · final identified early-audit recovery

**Scope.** The project owner supplied four original Markdown files: the 19 October internal foundational proof audit, the 20 October original external review by ChatGPT High, the 20 October original external adversarial review by Claude Opus 5.5 Extra, and the external audit request/packet. All four were read directly, compared with the [20 October dated reconciliation](A-external-audits-reconciliation-2026-10-20.md), [saturation-operator canonical correction](A-saturation-operator-nonidempotence.md), and [47-group evidence review](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md). A conversation-only ZIP preserves **all four originals byte-for-byte**, together with the checksums below. The raw files were **not published to GitHub**. No original experiment was rerun and this document is **not a new independent mathematical proof audit**.

**Outcome.** This closes the last specifically identified original-referee-report access gap (20 October). The current B15 **L / I** evidence distinction is confirmed, **not promoted**: Vermeulen's published effectivity result is L, and the strong \(r_{\mathcal I}\) counterexample is **referee-origin, later internally verified**, not an original strictly blinded theorem. The central mathematics and existing repairs in the dated reconciliation remain valid on source comparison. No theorem withdrawal or new historical 47-group identifier is warranted.

## 1. Files and actual blindness protocol

**Original internal report, 19 October:** ProjectA_foundational_audit_2026-10-19(1).md, titled *Project A — focused foundational proof audit*. It verifies eight targeted interfaces and identifies **nonidempotence of \(r_E\) for general closed equivalence relations** using an example on \(\mathbb R\), but explicitly **leaves the special relation \(E=\mathcal I=\operatorname{cl}\Delta\)** undecided. It checks the proper continuous-frame collapse relative to Vermeulen 1994, Picado–Pultr 2021 and Hofmann–Lawson, without claiming to have audited the whole project.

**External audit request:** ProjectA_external_blind_audit_packet(1).md, titled *External adversarial audit request — Project A localic relations*, 49 lines. It enumerates eight critical proof obligations and optional finite/pointless stress cases, links to eight GitHub source notes and primary literature, instructs reviewers to attempt independent derivation, and instructs them to compare the internal audit *only after* an independent verdict. Despite the word “blind” in its filename, it **does not by itself establish actual informational blindness** and does not contain a raw independent referee report.

**Claude Opus 5.5 Extra original external review, 20 October:** Project A — External Adversarial Referee Report(1).md (as identified by the [dated reconciliation](A-external-audits-reconciliation-2026-10-20.md)). It explicitly discloses: “Both uploaded files were delivered into my context together at the start, so the internal audit's text was visible before I began. I did not use it as evidence.” Therefore this review was **not strictly blind**, although its author reports independent source reconstruction and targeted subagent checks. It tests the eight obligations, 400 random finite-poset examples and the cited Vermeulen scan, and is particularly useful for an independently derived **special-form** \(r_{\mathcal I}\) counterexample, identified below.

**ChatGPT High original external review, 20 October:** ProjectA_external_independent_audit(1).md, titled *Project A: external adversarial mathematical audit*. The report says it wrote its “independent verdict” and §§1–10 before intentionally opening the full internal foundational audit; however, its §11 discloses that automatic attachment previews and a primary-source search **may already have exposed excerpts**. It too was **not demonstrably strictly blind**. The mathematical assessment and the later deliberate comparison are separately marked within this original report.

**Comparison with existing reconciliation:** The [20 October repository reconciliation](A-external-audits-reconciliation-2026-10-20.md) correctly says **both reviewers had some exposure to the internal audit**. Its characterization as independent mathematical re-derivations rather than strictly blinded reviews is appropriate. The new original-source access confirms, rather than changes, that provenance distinction.

## 2. The exact source chronology for the saturation operator

For a closed reflexive symmetric localic relation \(E\hookrightarrow X^2\), the exact adjunction formula holds without properness:
\[
r_E(u)=(p_2)_*p_1^*(u)
=\bigvee\{v\in\mathcal O(X):1\boxtimes v\le (u\boxtimes1)\vee d_E\}.
\]
It is monotone, finite-meet preserving, and deflationary. For symmetric reflexive \(E\), its fixed points are the invariant opens, but **\(r_E(u)\) need not itself be invariant**; hence idempotence is not automatic. If the projections are **proper**, the special Beck–Chevalley calculation identifies \(r_E\) with the largest saturated-open interior, idempotent and Scott-continuous, under the precise hypotheses of Vermeulen.

- **19 October internal:** produces an \(\mathbb R\) example for a **general** closed equivalence \(E\); explicitly does **not** settle \(E=\operatorname{cl}\Delta\).
- **20 October ChatGPT High:** independently illustrates the same **general-E** failure on a countable closed subspace of \(\mathbb R\), and notes the special \(E=\operatorname{cl}\Delta\) remains open on its own analysis.
- **20 October Claude:** extends the phenomenon to **\(E=\mathcal I=\operatorname{cl}\Delta=\mathcal U=\mathcal F\)** on an explicitly countable sober algebraic space with classes \(\{a,b\}\), \(\{c_n,d_n\}\) (all finite) and quotient \(\omega+1\). For \(u=\{a,b\}\cup\{d_n\}\) it proves
\[
r_{\mathcal I}(u)=\{b\}\ne0,\qquad r_{\mathcal I}^{\,2}(u)=0.
\]
The quotient is compact Hausdorff but **not a closed map**. Claude also gives a T1 variant and Scott-continuity failure despite finite equivalence classes. These stronger findings are **referee-origin in a not-strictly-blind review**, not part of the original eight submitted claims.
- **Subsequent project reconciliation:** checks the special-form example mathematically and writes [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md). This is why theorem group **B15** records **L** for Vermeulen and **I** for the project’s special counterexample, rather than an original blind E.

For ordinary quotient relations, the report and current canonical proof stress the indispensable **interior**:
\[
r_E(u)=\operatorname{int}(X\setminus E[X\setminus u]).
\]
Do not omit it absent a closed-saturation/closed-quotient hypothesis. Neither general Scott continuity of \(r_E\) nor properness of the projections is proved equivalent to the other in arbitrary locales by these reports.

## 3. Other findings: match with dated reconciliation

The two external reviewers and the October 19 internal audit agree on the foundational **frame-coproduct rectangle pseudocomplement**, finite rectangle farness, the **actual closed-sublocale** chain \(\Delta\subseteq\mathcal I\subseteq\mathcal U\subseteq\mathcal F\), functional separation via the completely-below relation, the completely regular reflection and **\(\mathcal F\) as its internal kernel pair**, and the point-free inclusion \(\mathcal I\circ\mathcal I\subseteq\mathcal U\). Vermeulen's **Proposition 5.5** and **Corollary 5.17** are the correct published proper-quotient/effectivity imports. The proper continuous-frame collapse is **conditional** on the named published Vermeulen and classical Hofmann–Lawson inputs and ZFC: properness cannot be silently replaced by merely closed quotient or finite classes.

The reviewers also accepted the principal cofinite-cloud deleted-plank \(T_1\), sober, algebraic counterexample with \(\mathcal I=\mathcal U\subsetneq\mathcal F\). Ancillary points requiring exact scope, largely recorded already in the October 20 reconciliation, include:
- **Finite vs infinite far-rectangle joins** (only the finite lemma is universal).
- **Compact nonspatial strengthening** from the proper theorem, relying on a cited compact-Hausdorff-locale regularity result: **published premise not re-derived**; do not advertise as a wholly unconditional new standalone statement.
- **Strong vs weak local compactness**, compact containment, and the separate role of sobriety when identifying all locale points with original point sets.
- **A false non-Hausdorff paracompactness aside** and a three-point **specialization-order reversal**, corrected in the original reconciliation.
- **Scott-continuity converse questions** and an extended LCH partial converse proposed by Claude: not incorporated as blanket theorems.
- Auxiliary finite-poset checks and pointless \(P\times Y\) tests: source-reported computations; no scripts or computation reruns in this recovery.

The Claude report is more extensive than the original eight obligations and explicitly labels parts of its extra supporting-note investigation as subagent-only or conditional. Do not turn those extensions into new E grades merely because they appear in the original external document.

## 4. Evidence status and archive handoff

**Direct-original inspection status:** **COMPLETED** for the specifically identified October 20 original sources. Together with separate [October 21](ProjectA_OCT21_PRIMARY_REFEREE_REPORTS_REINSPECTION_2026-11-21.md), [October 23](ProjectA_OCT23_PRIMARY_V_REFEREE_REPORTS_REINSPECTION_2026-11-21.md), and [November 11 fourth-audit](PointFree_FOURTH_AUDIT_PRIMARY_REPORTS_REINSPECTION_2026-11-21.md) direct-reinspection notes, **all four specifically requested historical batches** have now been reopened. This is **not** a claim that every audit ever conducted in the larger research project has publicly archived original bytes; these reports still exist as **private uploaded sources**, while GitHub contains reconciliations and evidence descriptions.

**B15 original/reviewer status:** **UNCHANGED**: published L plus project I (referee-origin, subsequent internal check). No evidence-grade promotion, theorem withdrawal, new claim of novel historical priority, or renewed full technical audit follows.

**Integrity:** The four original files are preserved byte-for-byte in a separate conversation ZIP, named PointFree_Oct20_original_audit_sources_2026-11-21.zip, with a MANIFEST.md recording file sizes and SHA-256. It was checked for archive integrity and the checksums were verified after reopening it. The files have not been published in GitHub, and none of the original documents or reports was rewritten.

| Original uploaded file | Bytes | SHA-256 |
|---|---:|---|
| Project A — External Adversarial Referee Report(1).md | 34,285 | 9d07b6c3e7b3e61c012f155bc2cfcaf0bd47355a1b53238f4dcd29eb06fcf614 |
| ProjectA_external_independent_audit(1).md | 23,227 | f60e42c71b930d8e1598ea42992dc48d497fe0b2200d3f76c71dcf38b840eb5b |
| ProjectA_foundational_audit_2026-10-19(1).md | 18,103 | ba1f8f9e370dec9ee3411130743e02624d14874ecbdc26371f181dea32244549 |
| ProjectA_external_blind_audit_packet(1).md | 6,401 | 866396440795fbe6ea3fc53d2a31cf4e89cf15b6f488b6339dbf6d7c774adc70 |

**Next step:** For the eventual research handoff, ensure the main [47-group ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md), [second-pass provenance review](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md), [Start Here](ProjectA_ENDGAME_START_HERE_2026-11-21.md), and [archival handoff candidate](ProjectA_ENDGAME_ARCHIVAL_HANDOFF_CANDIDATE_2026-11-21.md) link here and explicitly close the October 20 optional original-visibility task, while retaining the distinction between private original files and public mathematical reconciliations.
