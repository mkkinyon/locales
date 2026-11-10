# Point-Free Topology — 10 November 2026 repository maintenance record

**Completed after receipt and reconciliation of the second independent blind referee report.** This is a change log and scope declaration, not a theorem proof. The original [pre-maintenance read-only review](https://github.com/mkkinyon/locales) was supplied as a separate conversation attachment; these changes implement its high-priority recommendations without moving or rewriting the historical research notes.

## Changes performed

1. **Current mathematical authority:** created [corrected coherent chain/hull canonical note](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md), [unified master theorem ledger v2.0](PointFree_master_theorem_ledger_v2_0_2026-11-10.md), [unified open-problem register v1.7](ProjectA_open_problems_register_v1_7_2026-11-10.md), and [coherent homotopy phase index](PointFree_coherent_homotopy_PHASE_INDEX_2026-11-10.md). v1.9 and v1.6 are **preserved intact as historical snapshots**. New PF-D, PF-C, PF-R theorem IDs separate independently blind-checked claims from *referee-origin additions*.
2. **Two independent blind cycles archived:** [10 November audit archive](audits/2026-11-10/README.md) has separate [Dowker](audits/2026-11-10/dowker/README.md) and [chain/hull](audits/2026-11-10/chain-hull/README.md) directories. Each contains its original blind prompt, packet, external report, internal audit, and later **separate** referee suggestions, copied in text without editorial rewriting. The original ZIP attachments remain in the conversation; the repository stores the constituent source texts. The mathematical reconciliations remain separate at root.
3. **Referee suggestions and priority:** [First referee original prioritization](PointFree_referee_post_audit_suggestions_priorities_2026-11-10.md) retained; [second referee eight suggestions triaged](PointFree_referee2_mathematical_suggestions_triage_2026-11-10.md). The suspension of \(h(S)\) and **relative finite compact-open D-side codescent** are prioritized, but not retroactively upgraded to blind-verified theorems. Technical size restriction and vague shape identification rejected as general arguments.
4. **Navigation refreshed:** [README](README.md), [unified start page](POINT_FREE_TOPOLOGY_START_HERE.md), and [legacy A start](PROJECT_A_START_HERE.md) now distinguish the unique current authoritative ledger from specialized dated notes. The old [C-frame-nerves](C-frame-nerves.md), [append-only A status index](A-research-status-index.md), and [future-questions](future-questions.md) receive **historical-status banners only**; original bodies are retained.
5. **Thematic discoverability:** [subject-wide thematic guide](POINT_FREE_THEMATIC_GUIDE.md), [phase index](PointFree_coherent_homotopy_PHASE_INDEX_2026-11-10.md), and [notation conventions](POINT_FREE_NOTATION_GUIDE.md) added. No hundreds-of-files renaming/movement or rewriting of false starts.
6. **Broken navigation repaired:** two old relative links in [W-phase index](project-a/audits/2026-11-09/Wphase/README.md) and one in [Q′ index](project-a/audits/2026-11-09/Qprime/README.md) corrected from ../../../ to ../../../../.
7. **Link-checker added:** [tools/check_relative_links.py](tools/check_relative_links.py), a read-only Python 3 utility to check **inline local Markdown file targets** in a local checkout. It intentionally does not verify heading anchors, reference-style links, or external sites. Run \`python3 tools/check_relative_links.py\` from a local clone.

## Verification and deliberate limits

- Direct GitHub reading verified **583 inline link targets in the 19 most important current/status/audit pages**, with **no broken relative targets**. A further representative sample of 12 historical A notes had 12 inline targets, all resolving. This is a **targeted** check, not a full 321-plus-file scan. Earlier scan found and this pass fixed the three known broken 9 November audit index links.
- Canonical note and ledger explicitly repair the second referee's B2 last-vertex proof gap, C3 cofibre inference, site prerequisites, G3 strictness overstatement, and Cameron–Kumar §9 attribution.
- The first referee's non-descent theorem and the second's post-report additions (UB equivalence, no-compactness closed descent, strictness of cover criteria, compactified fence W) retain **their actual verification provenance**; no original external report was silently altered.
- **Not done:** full 300-plus-file link checker run (no local git checkout in this runtime); deep rewrite of historical notes; independent proof assistant/human audit; literature-priority investigation; original ZIP binary archiving; site-size independence; automatic CI workflow.
- **Pending optional cosmetics:** a duplicated README reference to the same arithmetic counterexample, 177-byte historical W=U placeholder stub, and a consistent naming policy for future files. These pose no substantive mathematical risk and were deliberately left alone.

## Mathematical next work

**PF-Q01:** Start with the second referee's \(X(S)=S\cup\{p,q\}\) for Stone S, all \(s\le p,q\), to test \(\mathbf C(X)\simeq1\amalg_{h(S)}1\) and whether Cantor S makes this a genuinely **nonconstant sheaf homotopy** object, with \(\mathbf I(X)\simeq\mathbf D(X)\simeq1\). The sheaf-level nonconstancy still needs a proof and must be distinguished from a trivial external product example.

**PF-Q02:** Derive and audit the **D-side** relative Čech codescent for finite *compact-open upsets*. This is distinct from false unpatched lower-witness descent.

**PF-Q03/04:** Return subsequently to the comparison of finite-stage/pro-systems and Čech–Vietoris refinement with the referee's infinite-fence warning: arbitrary filtered inverse limits cannot be passed through geometric realizations.

**Disposition:** The requested prioritization, audited consolidation, and conservative repository maintenance pass are complete. Begin mathematical research on essential nonconstant sheaf-level structure next.
