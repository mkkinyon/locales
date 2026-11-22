# October 21 original audit materials — direct-source reinspection
## 21 November 2026 · provenance update, not a new mathematical referee report

**Recovered source scope.** Seven uploads supplied by the project owner give **three original October 21 independent referee reports**, both related blind-audit prompt/packet sets, and a separate proof note on the deleted-plank construction. The accompanying D1–D9 archive was unpacked and its two constituent Markdown files read. All seven original files were inspected directly; no supporting scripts were provided in this upload or re-executed. A separate conversation download bundles the **unaltered** files with SHA-256 checksums. Original private reports were **not copied to this public repository**.

This fills the October 21 direct-visibility gap explicitly noted in the [47-group second provenance pass](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md). The previously dated statement that the earlier pass relied on the public reconciliations remains historically true, but direct inspection has now superseded that access limitation. **No mathematical theorem has been newly proved or formally verified by this document.**

## 1. Exactly which blind audit was which

### Broad D1–D9 audit of diagonal fitting and preservation

- **Prompt/source ZIP:** ProjectA_external_blind_audit_2026-10-21(1).zip, containing 01_EXTERNAL_AUDIT_PROMPT.md and 02_EXTERNAL_AUDIT_PACKET.md. The packet is dated **21 October**; primary notes are the fitted diagonal, D=U first results, arbitrary coproduct preservation of I=U, and the closure-property table. Background covers coherent conormality, continuous frames, relational properness and the Scott-converse working records.
- **Original report:** ProjectA_independent_audit_2026-10-21(1).md, *Independent adversarial audit — Project A (fitted diagonal, D = U, I = U closure)*, dated **21 October 2026**. The [dated reconciliation](A-external-audit-reconciliation-2026-10-21.md) identifies this report as the **Claude Opus 5.5 Extra** audit. It reports a read-only repository at commit 530fca0 and a finite-frame test of 405 isomorphism types of posets up to 6 points. The testing scripts cited by the report were not uploaded in this source-recovery batch.
- **Original scope/acceptance:** D1–D9 and the closure table, notably **arbitrary frame coproducts** of I=U, arbitrary **frame direct products**, failures under subframes and frame quotients, and auxiliary **open heredity** plus failure of blanket closed heredity. The referee marked **CP-2** (infinite-family zero detection) and **CL-1** (arbitrary products: locale extensivity) **correct with repair**, and supplied the missing arguments in its report. It also independently revisited the open-heredity theorem from the structural note. These portions were **explicitly inspected**, contrary to the uncertainty in the earlier 47-row provenance audit.
- **New results originating in that report, not originally submitted blind:** compact L: D=U iff L normal, with compact D=U implying U=F; coherent pm/normal-lattice identification; closed heredity of D=U; and a noncompact algebraic/arithmetic locally compact sober deleted-plank example claimed to have D=U strictly below F. The compact normality theorem was independently re-proved in a separate coherent report below, but no original-blind-submission label should be attached to these *referee-origin* theorems. The plank construction's supplementary note supplied below proves **sobriety** and the compact-open classification; the remaining separation and functional calculations belong to the original report, not that auxiliary note. Full independent verification of all generalizations is **not** asserted.

### Two independent reports of the coherent-relations/Hochster packet

- **Common prompt:** ProjectA_coherent_external_audit_prompt(1).md; **common source packet:** ProjectA_coherent_external_blind_audit_packet(1).md, both prepared **21 October** and listing **seven** primary GitHub notes.
- **Report 1:** ChatGPT_ProjectA_audit(1).txt, *Independent referee audit — Project A, coherent locales*, **ChatGPT High**, 463 lines. Verifies the coherent identities U=I∘I=c(D), paired I/D characterizations, Hochster exchange and five-point counterexample, subject to repairs. Critically, it **does not claim** to have independently verified the arbitrary **compact, possibly pointless** theorem D=U iff frame normal, because the proof was not in the primary source note. It verifies the **coherent** specialization.
- **Report 2:** Project A — Blind referee report coherent relations and Hochster duality(1).md, **Claude Opus 5.5 Extra**, dated **21 October**, approximately 372 lines. Gives a more exact repair to the localic-image argument: “spatial source + closed localic image implies all image points come from ordinary image points” is **false in general** (Spec Z example). The coherent theorem nevertheless survives because the **ordinary composite is already closed** and because one can use the sandwich I∘I⊆U with all U-points in the closed image. This report also re-proves arbitrary compact normality with a choice-free finite rectangle argument, and proposes the **new coherent mirror identity** fit(I)=D∘D using compact-open-filter sublocales. The additional arbitrary-compact identity U=I∘I and compact locally compact sober T1 counterexample to c(D)=U are **post-verdict referee proposals**, not part of both original blind submissions.
- **Status comparison:** These texts match the already published [two-coherent-audits reconciliation](A-coherent-external-audits-reconciliation-2026-10-21.md): the coherent packet survived, localic-image inference requires repair, and the referee-origin compact/fitted generalizations have separate proof/evidence boundaries. The reports were independent **of the internal audit**, not an audit of one another's reports.

### Supplementary plank construction

**Source:** Plank with lower points sobriety and compact opens(1).md, dated **21 October**. It proves for the specified deleted Tychonoff plank with finite unmixed lower-point indices that the extension is **sober** and has a **basis of compact opens**, with a classification of its compact-open sets. Its own §6 explicitly says that the plank lemma, the equality Ury=Cm and the final sublocale transfer occur **in the separate referee report**, not within the supplement. It strengthens documentary support for the claimed continuous-frame example, **not** by itself a fresh full cross-audit.

## 2. Required update to the A18 provenance entry

**Previous conservative ledger:** E+C for arbitrary frame coproduct preservation of I=U; I for direct products, open heredity and closed-heredity failure because the original reviewed scope had not been directly checked.

**Direct-original evidence now read:**

| Component of A18 | Original report location | Correct evidence label |
|---|---|---|
| Arbitrary frame coproducts | broad report CP-2/CP-3, in original D8 packet | **E+C**: externally checked with explicit infinitary cp-ideal repair; expanded canonical proof may be later working text |
| Arbitrary frame direct products | broad report CL-1, D8 | **E+C**: original reviewer accepted with an explicit locality/extensivity proof repair |
| Preservation by open sublocales | broad report CL-5/FN-7, referring to independently read structural theorem | **E** for the stated theorem; auxiliary/background review, not a separate focused blind theorem submission |
| Failure under closed sublocales and frame quotients | broad report CL-4 and corresponding finite witnesses | **E** for finite counterexamples and specified negative closure assertion |
| Subframe negative | broad report CL-3 | **E** for finite witness |

This is a **documentary grade correction reflecting found primary evidence**, not a promotion based on newly established mathematical truth. Do not infer that arbitrary locale limits/colimits preserve the class; the precise operations and their variance matter. Earlier attempts to keep products/heredity at I were reasonable given missing primary evidence.

## 3. Boundaries and remaining material

- **Coherent theory:** two independent October 21 blind reports were directly read and correspond to the [two-coherent reconciliation](A-coherent-external-audits-reconciliation-2026-10-21.md); no new withdrawal or proof-gap discovery from this source comparison.
- **Compact normality:** the broad D1–D9 audit proposed it and the separate coherent audit independently provided a proof. These are not the same as a new independent targeted technical review of every statement in its general compact/localic extension; the canonical source and later reconciliations retain their own qualifications.
- **A18:** evidence in the original broad audit supports the specified product, heredity and negative statements. The [current 47-group ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) is updated accordingly. **No change** to unrelated A/B/C groups merely by reason of this recovery.
- **Other original scripts:** finite_checks.py, poset_audit.py and rectangle-lemma checks are cited in the reports but **not included** in the supplied seven attachments. Computation claims are source-reported, not rerun.
- **Remaining early private evidence:** the October 20 foundational reviews (historically *not strictly blind*) and the October 23 Vfin report are still not directly supplied in this batch. Some later dated reconciliations or public independent reports exist; do **not** require these raw files to close the October 21 original-audit visibility item.
- **No source novelty determination:** Cornish normal/conormal, pm/mp, Hochster, APP 2022 and Cameron–Kumar are prior literature; no localic formulation is asserted new here.

## 4. Exact integrity inventory

The original seven uploaded files were retained **byte-for-byte**, with SHA-256 manifest in a private conversation ZIP. The prompt/source ZIP contains **two Markdown files, not a hidden referee report**. The report files remain unmodified.

| Uploaded filename | Bytes | SHA-256 |
|---|---:|---|
| ProjectA_external_blind_audit_2026-10-21(1).zip | 6,253 | 35be3dd6ba63b8aa0328c72f099609615acb22b45f568223d5bcd67a9f532d1d |
| Project A — Blind referee report coherent relations and Hochster duality(1).md | 45,843 | e7eeb891e7d0351ef132de432546aba593265eff7c27544b550059a697a9eb8a |
| ChatGPT_ProjectA_audit(1).txt | 29,314 | ef6ab0d4f9e083addec581f2c81a71ebd97bb865212b54bbe2354117b327e258 |
| ProjectA_coherent_external_audit_prompt(1).md | 2,032 | be34b12b69f6119e6d1432084af1f5654956aeadd1fc15db5af0ac1084fc5c89 |
| ProjectA_coherent_external_blind_audit_packet(1).md | 6,803 | 653e052e5149d4dc92fc5f3cfe75b17560f6384b2adecae6baff527ff74e1ce3 |
| Plank with lower points sobriety and compact opens(1).md | 17,215 | 98da7b8bdc0de8af28987c6767dbc27b760565fe95d68cdabe29e59a5666a501 |
| ProjectA_independent_audit_2026-10-21(1).md | 49,310 | 5f42f8754ad9d2f73b9e0502c668eeb68cbf88c128afbda471644c73e9e3de4d |
