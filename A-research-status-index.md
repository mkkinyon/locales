> **Current status correction (21 Oct 2026):** Read [external audit reconciliation](A-external-audit-reconciliation-2026-10-21.md) first. The compact theorem D=U iff frame normal and coherent normal/pm criterion supersede earlier D=U agenda. Contrary to the previous ledger, the continuous Scott/properness converse has a working proof dated 20 Oct; only its unrestricted arbitrary-frame extension remains open. D=U ⇒ U=F is false generally but true for compact locales.

# Project A — research-status index

**Updated 21 October 2026.** This is the entry point for preserving context between sessions. It is a **status guide**, not an assertion that all working proofs have received independent refereeing. When status differs across dated notes, prioritize the most recent audited correction and recheck source proofs before reuse.

## Canonical foundations and audits

- [A-consolidated-theorems.md](A-consolidated-theorems.md): master theorem outline; foundational hierarchy Δ⊆I⊆U⊆F.
- [A-external-audits-reconciliation-2026-10-20.md](A-external-audits-reconciliation-2026-10-20.md): primary correction log and reconciliation.
- [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md): localic properness, quotient effectiveness (Vermeulen), saturation operator. **Read audit qualifications**: for arbitrary closed equivalence E, r_E need not be idempotent.
- [A-fitted-diagonal.md](A-fitted-diagonal.md): fourth relation D=fit(Δ); Δ⊆D⊆U, I and D incomparable, pointwise closure-meeting interpretation. D=U belongs in its **own** research track.

## Result / status ledger

| ID | Statement / question | Current status | Source |
|---|---|---|---|
| A1 | Frame coproduct tensor pseudocomplement; Δ⊆I⊆U⊆F; I∘I⊆U | Audited foundation | consolidated outline / audits |
| A2 | Algebraic compact-pair test; coherent I=U iff K(L) conormal (Cornish-normal) | Established in project; primary-source novelty unchecked | [coherent note](A-coherent-conormality.md) |
| A3 | Continuous-frame way-below test for I=U | Established in project; classical spatial representation caveats | [continuous note](A-continuous-frames.md) |
| A4 | I=U does not generally imply U=F; cofinite-cloud and deleted-plank examples | Counterexamples in existing notes, audited with qualifications | [continuous counterexample](A-continuous-counterexample-plank.md), audits |
| A5 | Proper closed equivalence E gives effective quotient (Vermeulen 1994) and Scott-continuous idempotent r_E; proper continuous collapse under stated hypotheses | Established relative to cited theorem; hypotheses matter | proper relations note, audits |
| A6 | Arbitrary **frame products** preserve I=U | Working point-free proof by clopen locale components; not independently audited | closure-properties discussion / [coproduct note](A-coproduct-preservation-I-U.md) |
| A7 | Arbitrary **frame coproducts** preserve I=U | Working proof committed 20 Oct; independently audit zero-detection and functorial transport | [coproduct note](A-coproduct-preservation-I-U.md) |
| A8 | Subframes and surjective frame quotients do **not** preserve I=U | Finite Alexandrov counterexamples; recheck precise poset witnesses | closure-properties discussion |
| A9 | Scott continuity of r_I ⇒ idempotence, β_* Scott-continuity, or p₂ proper | **WORKING THEOREM for continuous frames; arbitrary-frame case OPEN** | [Scott ledger](A-scott-continuity-converse-status-2026-10-21.md) |
| A10 | Full arbitrary-frame property I=U equivalent to established named axiom | **NOT IDENTIFIED; literature search deferred after substantial due diligence (21 Oct)** | [literature ledger](A-literature-separation-status-2026-10-21.md) |
| A11 | D=U: cover criterion; finite Alexandrov classification; fitted U is strictly weaker | **AUDITED foundations; compact-normality proof externally checked, independent specialist verification recommended** | [D=U first results](A-D-equals-U-first-results-2026-10-21.md), [fitted note](A-fitted-diagonal.md) |

## Research tracks / priority

1. **Active A:** localic separation relations and equality conditions. Current established closure results and literature identifications to audit and integrate.
2. **Deferred A:** genuinely point-free Scott-continuity converse. Several methods (way-below interpolation, rectangles, quotient operators) have stalled; **avoid merely renaming the gap**. See Scott ledger.
3. **Active A:** D=U and diagonal fittedness; first cover test and finite-Alexandrov classification recorded. Separate later question D=U ⇒ U=F.
4. **Backlog:** [B-overlap-graphs.md](B-overlap-graphs.md) and [C-frame-nerves.md](C-frame-nerves.md).

## Corrections and risk flags

- **Continuous frames are spatial classically** (Hofmann–Lawson); do not label a classical continuous-frame example 'pointless'.
- Do not infer r_E idempotent merely from closed internal equivalence; counterexamples in audits.
- Distinguish frame products (locale disjoint unions) from frame coproducts (locale products).
- In the geometric I=clΔ argument, p₁*a∧p₂*b=0 for a∧b=0 **does not** imply p₁*a≤p₂*(b*); inverse images may not preserve pseudocomplements.
- The finite poset counterexample for nonclosure and the arbitrary-coproduct proof are working results; request independent audit before publication.
- Cornish-normality of **all** L corresponds to Stone, not to I=U. The correct coherent test applies to K(L).
- In a new session, **read this index first**, then the relevant current source note and audit reconciliation; do not reconstruct settled questions from conversational recollection alone.

## Maintenance protocol

For each substantive research segment, update one source note and this index in the **same session**, if repository write access is available. Label: **proved and audited**, **working proof**, **counterexample**, **conjecture/open**, **false**, or **deferred**. Record exact hypotheses, proof dependencies, and counterexamples to tempting false assertions. Do not silently overwrite historical exploratory notes: add an explicit dated correction or refer to reconciliation. Cite papers accurately and distinguish primary-source checks from searches/abstracts. Keep an uncertainty ledger; after a failed approach, record the obstacle rather than further equivalent formulations.

## Recent repository changes

- 20 Oct 2026: [A-coproduct-preservation-I-U.md](A-coproduct-preservation-I-U.md), commit 3f9b4ce.
- 21 Oct 2026: this index and separate literature / Scott-status ledgers; no claim of independent post-commit audit.

## Literature-search checkpoint (21 October 2026)

[The literature ledger](A-literature-separation-status-2026-10-21.md) now records direct reading of Bhattacharjee–Madinya–McGovern (2026): their CAB condition holds for all coherent frames, so it is too weak to characterize I=U. It also records the bounded conclusion from this search: **substantial corroborating evidence of no previously identified treatment of the exact arbitrary-frame I=U condition in the accessible literature inspected**, but **no definitive novelty or priority claim**. This search is **paused**; resume only on a specific lead. The D=U fitted-diagonal line remains separate.

- 21 Oct 2026: [A-D-equals-U-first-results-2026-10-21.md](A-D-equals-U-first-results-2026-10-21.md), working proofs of the cover criterion and finite Alexandrov classification; **await independent audit**.

- 21 Oct 2026: finite three-point coherent example shows **U fitted does not imply D=U**; proof in [D=U first results](A-D-equals-U-first-results-2026-10-21.md), §4.

- 21 Oct 2026: **fit(U)⊊F can occur**, by closed-point lemma and a Urysohn non-functionally-Hausdorff space; see [D=U first results](A-D-equals-U-first-results-2026-10-21.md), §7. No implication for continuous/coherent cases claimed.

## Adversarial internal review checkpoint — 21 October 2026

Priority order after validation: (0) independently audit recent categorical, coproduct and counterexample dependencies; (1) D=U ⇒ U=F, bounded initial investigation; (2) structural coherent characterization of D=U; (3) fit(U) strict/intermediate examples; (4) continuous-frame way-below criterion; (5) D=U preservation properties; (6) defer Scott-continuity converse and the I=U terminology search.

Targeted internal read found no fatal defect in the D=U square-cover criterion, finite Alexandrov classification, or the three-point fitted-U counterexample. F fitted is independently supported by the fitted-equalizer theorem for F-separated codomains (Arrieta–Picado–Pultr); cite that directly. Strict fit(U)⊊F argument is conditional on a concrete verified Urysohn/non-functionally-Hausdorff example; choose and audit one before promotion. Arbitrary frame coproduct/product closure of I=U remains a working proof pending independent audit. This is not an exhaustive second read of all foundational notes.

- 21 Oct 2026: [Lower-point plank supplement verification](A-lower-point-plank-supplement-verification-2026-10-21.md): independent checks of sobriety, compact-open characterization, arithmeticity, closure-meeting vs Urysohn relation, and function obstruction. The algebraic/arithmetic continuous example D=U⊊F has stronger support; ensure full closure/buffer argument is given in any publication draft.

- 21 Oct 2026: [Noncompact normality investigation](A-noncompact-normality-D-U-2026-10-21.md): **normal continuous frames satisfy D=U=F without compactness** (classical locally compact sober proof); the arbitrary noncompact, noncontinuous normal-frame implication remains **OPEN**. Finite-cover normality alone does not establish arbitrary-cover condition; regular nonnormal frames show converse fails without compactness.

- 21 Oct 2026: **Arbitrary-frame normal ⇒ D=U deferred after exactly two segments**. Neither proof nor counterexample found. [Noncompact-normality note](A-noncompact-normality-D-U-2026-10-21.md) §6 records exact universal-coproduct obstruction via two frame maps into a nontrivial frame. Compact and continuous cases remain proved. Next planned topic: internal transitivity of U under D=U.

- 21 Oct 2026: [D=U and transitivity of U](A-D-U-transitivity-2026-10-21.md): **continuous frames** with D=U have U an internal equivalence relation (pointwise Cm argument plus spatial closed composable-pair locale); also true compactly via U=F. **Arbitrary-frame implication OPEN.** Exact target: for far a,b, a₁∧b₃≤d_U,12∨d_U,23 in O(X³).
