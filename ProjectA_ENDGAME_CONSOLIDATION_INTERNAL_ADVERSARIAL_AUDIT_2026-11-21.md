# Internal adversarial audit of endgame consolidation v3.0
## 21 November 2026 · adversarial source-to-summary check; repairs specified below

**Subject of audit:** [current theorem ledger v3.0](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md), [proof dependency atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md), [start-here](ProjectA_ENDGAME_START_HERE_2026-11-21.md), [open-frontier register](ProjectA_ENDGAME_OPEN_FRONTIERS_2026-11-21.md), and their relationship to canonical repository sources.

**Method and limitations:** Read these four actual files and selectively re-opened the original dated canonical theorem notes, independent-audit reconciliations and earlier ledgers. Tested exact statements against source texts; stress-tested premises, empty cases, provenance, logical status and omissions. **This is NOT an independent mathematical re-proof of every cited theorem**; it does not certify correctness of 40 entries, literature novelty or human peer review. Distinguish a *source-to-ledger contradiction* (decisive within the archive) from *an unverified mathematical premise* (still open to independent proof scrutiny). The findings below constitute the internal audit record, not a new external blind referee verdict.

## Verdict

**REVISION REQUIRED.** The organization into separation / composition / higher witness branches is workable, and the root-level navigational links are present, but there were **two direct mathematical misstatements**, **one false current "open problem"**, **three material audit-status overextensions**, and **several omissions of significant already-established project theorems**. No newly discovered fatal flaw in the *underlying canonical proof packages* is asserted; the defects are demonstrable in the **new consolidation**. Correct the current ledger and open register rather than edit historical packets.

## I. Mandatory mathematical and status corrections

### AA-01 — HIGH: the finite p/q rectangular algebra is **not asserted unital**; formula needs a zero-case guard

**Fault in v3.0 ledger B04:** “Finite joins of generators form a unital associative converse-closed algebra.” Also the multiplication is written “\(r(A,B)\circ s(C,D)=q(A,D)\) iff \([B]\wedge[C]\ne0\), else 0”, a literal iff invalid if outer q(A,D)=0.

**Source:** [compact-Hausdorff rectangular canonical](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), **§5 Theorem 5.1**, **§6 Theorem 6.1**: \(\mathscr R_\vee(G)\), the *finite joins of p/q rectangles*, is **associative, converse-closed, zero-containing, finite-join-distributive**, but: “**Neither a multiplicative identity inside \(\mathscr R_\vee(G)\) nor arbitrary-join closure is asserted.**” It is the **larger** [locally closed graph algebra](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md) §2 that explicitly contains \(\Delta_G\) and is **unital**.

**Repair B04:** State piecewise (not an iff characterization of equality to q)
\[
r(A,B)\circ s(C,D)=\begin{cases}q(A,D),&[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0.\end{cases}
\]
Add that **q(A,D) may itself be 0 if A or D is empty**; finite-join rectangular algebra is **not claimed unital**. Keep unit statement solely in B05's graph extension algebra. Need no change to original externally reviewed theorem.

### AA-02 — HIGH: global H-transitivity has already been refuted, even coherently

**Fault in open-frontier register #7:** “Global transitivity of \(\mathcal H\)” left open; cites the **21 October historical early note**, overlooking 24 October independent audit. This is plainly outdated.

**Source:** [two convergent zigzag rays](A-H-two-convergent-zigzag-rays-nontransitive-coherent-counterexample-2026-10-24.md), **§§1, 4–8**: a compact coherent spectral locale X with
\[
\mathcal U\vee\mathcal V<\mathcal H<\mathcal F,\qquad \mathcal H\circ\mathcal H\nleq\mathcal H.
\]
Explicitly **externally accepted** as a headline coherent theorem by [24 October post-V audit reconciliation](A-postV-external-audit-reconciliation-2026-10-24.md), Verdict. The same audit accepted the *coherent characterization* \(\mathcal H\) internally transitive iff \(\mathcal H=\mathcal F\). Further [H formal hull exact stages](A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md) proves exact first stabilization at \(\omega+m\), every integer m≥1, accepted in the October 24 audit.

**Repair:** Add dedicated A entry for coherent **nontransitive** H, strict U∨V<H<F, coherent transitivity iff H=F, exact stabilized \(\omega+m\) (careful: specified closed-stage \(\kappa\)-iteration, at limits take **closed hull of sublocale join**, not raw join). Mark E from post-V audit. **Delete** “Is H always transitive?” as an open problem; replace by legitimate *classification in restricted noncoherent classes* if useful. The 24 October [noncoherent counterexample](A-H-transitivity-noncoherent-counterexample-2026-10-24.md) shows transitive H<F can occur in a locally compact sober scattered T1 noncoherent locale; this addition itself is **I**, not externally audited as a separate result.

### AA-03 — MODERATE: sober T0 V_fin example is a post-verdict extension, not originally blind-reviewed

**Fault in A11:** one blanket E label covers the T1 cofinite-sheet construction **and** the sober T0 two-generic-point simplification.

**Source:** [V_fin consolidated proof](A-Vfin-negative-consolidated-proof-2026-10-23.md), opening status: the original cofinite-sheet proof and K-fan input passed internal and blind external audits; the “**simpler two-generic-point version was suggested by that auditor and independently checked during reconciliation**.” [V-fin independent audit reconciliation](A-V-fin-negative-independent-audit-reconciliation-and-generic-points-2026-10-23.md) explicitly separates them. Old v1.9 ledger listed **V06 E T1**, **V07 I sober T0**.

**Repair:** Label T1 and K-fan mechanism E; sober T0 refinement I (referee-origin, checked internally after verdict). The mathematical strictness theorem is still firmly supported. Do not assert sober for T1.

### AA-04 — MODERATE: chart-rank counterexamples and graph algebra membership have distinct provenance

**Fault in B11:** “**E for submitted/refereed finite-exception/corridor claims**”; treats addendum, original packet and later internal perfect Cantor tensor similarly. Start-here / open register claim broadly settled without indicating which subcase has which support.

**Source:** [graph extensions reconciliation](ProjectA_GRAPH_EXTENSIONS_REFEREE_RECONCILIATION_2026-11-21.md) §2 original submitted ALG/graph probe/open proper projection/Cantor two-to-one *unsafe* example received **E conditional on RC**. §3 explicitly labels the **safe infinite-chart-rank example with an infinite constant fiber** and the **finite-exception membership theorem** as **new referee addendum**, not submitted blind claims. It specifically says finite-to-one necessity *for safe adjunction* remained open at that point, whereas [scattered exactly two-to-one safe example](ProjectA_SCATTERED_RELATION_ALGEBRA_FINITE_TO_ONE_NECESSITY_COUNTEREXAMPLE_2026-11-21.md) and [perfect-source/target Cantor tensor](ProjectA_PERFECT_SOURCE_TARGET_TENSORED_SCATTERED_PSEUDO_ISOMORPHISM_2026-11-21.md) are **later internal**, not individually submitted to the graph blind audit. The independent [balanced/matrix reconciliation](ProjectA_BALANCED_WITNESS_SCATTERED_MATRIX_POSTREFEREE_RECONCILIATION_2026-11-21.md) accepts **MAT/MUL/BAL/GRP** and specific discontinuous monomial graphs, *not the entire separately drafted Cantor tensor theorem*.

**Repair:** B11 should distinguish (i) E for the submitted chart/negative graph probes (RC imported), (ii) I/referee-addendum for safe infinite-rank constant fibre and finite-exception membership, (iii) I for exact two-to-one scattered and perfect tensor constructions, noting later MAT/MUL inputs externally audited but the composite construction not itself blind reviewed, (iv) O broad necessary/sufficient graph-adjunction characterization. The broad **negative** answer to universal finite-chart necessity is correct, but the stronger finite-to-one version has **I** status.

### AA-05 — MODERATE: omit no key coherent equality dual

**Fault:** A07 records coherent \(\mathcal I=\mathcal U\iff K(L)\) conormal but neglects the equally established dual:
\[
\boxed{\text{coherent }L:\quad \mathcal D=\mathcal U\iff K(L)\text{ normal}.}
\]
Also for **compact** L, \(\mathcal D=\mathcal U\iff L\) normal, and in coherent locales \(\mathcal D=\mathcal U\iff\mathcal D\) closed \(\iff\mathcal D\) internally transitive. These are **core Project A theorems**, not minor historical examples.

**Sources:** [21 October independent audit reconciliation](A-external-audit-reconciliation-2026-10-21.md) §1, [coherent dual characterizations](A-coherent-dual-characterizations-2026-10-21.md), old v1.9 ledger **C05–C06 and K05–K07**. The compact theorem is externally checked; the stated coherent versions are reconciled from prior sources. Add a new A row (or expand A07 with full symmetry) with explicit hypotheses and reviewed status.

### AA-06 — MODERATE: H stabilization beyond ω is a noteworthy missing theorem, plus its limit convention

Separate from AA-02: the \(\omega+m\) first-fixed-stage examples are an excellent explanatory complement to the finite-rank V theorem. The source [H-formal-hull-odd-powers](A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md) gives specific \(\kappa(a)\) iteration \(a_{\alpha+1}=\kappa(a_\alpha)\), \(a_\lambda=\bigwedge_{\beta<\lambda}a_\beta\) and \(H=C(a_\infty)\). **On the sublocale side**, at limit λ, use \(\operatorname{cl}\bigvee_{\beta<\lambda}C(a_\beta)\), not the bare sublocale join. The post-V independent audit explicitly accepted the exact \(\omega+m\) ordinal claim. Our endgame overview currently downplays it; add to A row and note no need for further ordinal research.

### AA-07 — MODERATE: unconditional product/preservation/classification theorems buried under vague A14

Old v1.9 K02 listed **independently reviewed**: arbitrary frame coproducts and frame products preserve \(\mathcal I=\mathcal U\), with important nonheredity under **closed** sublocales/frame quotients, while open-hereditary property holds. Old C09 separately listed coherent binary product preservation of I,D,U,V,F with **internal** status. A14's generic “precise qualifiers” obscures the distinction.

**Repair:** Include one A entry with the main closure/failed-heredity results and scope, and an independent note on product formulas where sources are only internally checked. See [A-I-equals-U structural study](A-I-equals-U-structural-study.md), [A-coproduct-preservation-I-U](A-coproduct-preservation-I-U.md), [old v1.9 ledger K02/C09](ProjectA_master_theorem_ledger_v1_9_2026-11-09.md). Do not globally assert preservation under sublocales or arbitrary locale products.

### AA-08 — MODERATE: L* presently summarized too cryptically

B14 says only “unrestricted Scott-continuity/properness converse”; future reader cannot discern the theorem. [L* corrected canonical](ProjectA_Lstar_canonical_corrected_proof_2026-11-08.md) proves for **arbitrary locales** and a **closed** localic relation \(E\hookrightarrow X\times Y\), the induced right-adjoint saturation operator \(r_E=(p_2)_*p_1^*\) preserves **nonempty directed joins** iff the projection \(p_2:E\to Y\) is **proper in Vermeulen's sense** (directed-join preservation + closed Frobenius). Referee corrected a false principal-downset assertion in its mixed coverage-ideal proof. State exactly; avoid suggesting every nonclosed relation or arbitrary maps have this equivalence.

### AA-09 — MINOR/structural omission: other foundational results

- \(\mathcal F\) as kernel pair of completely regular reflection, **closed and fitted**, is standard plus project synthesis; \(\mathcal F=\Delta\) iff reflection is **monic**, which does **not** imply X completely regular (frame epis need not be surjective). See [equality characterizations](A-equality-characterizations.md), old F02/F03.
- Project \(\mathcal V\)-bar **positive low-rank** bounds in **compact**, **regular**, **continuous** and Scott-continuous domain frames are useful contrasts with V<Vfin. Old v1.9 V03a–d are mostly **I**, not all externally verified; keep labels and no blanket E.
- Published proper-equivalence effectiveness theorem Vermeulen 1994 and project saturation-operator nonidempotence examples are important “quotient/effectivity” foundations; currently B12/B13 have almost no point of reference. Link [Vermeulen correction](A-vermeulen-effectiveness-correction.md), [saturation nonidempotence](A-saturation-operator-nonidempotence.md); explicitly **L** for published effectiveness, not a new theorem.

These need not all become full main-text theorems; they should have discoverable entries.

## II. Checked boundaries that *do* match their sources

- **A03 / B02:** coherent actual Loc-image composition and finite word powers are appropriately restricted; \(\mathcal W=\mathcal U\) correctly marked as independently imported.
- **A04:** the stably compact I,D,V,W,J,T point formula and perfect/spatiality claim agrees with [J/T canonical §2](ProjectA_J_T_COMPARABILITY_GRAPH_STABLY_COMPACT_CANONICAL_2026-11-17.md).
- **A05/A06:** SC+ interval-chain equivalence restricted to stable local compactness; negative compact sober T1 A>Δ source matches.
- **A09:** connected compact W/H/U strict diamond agrees with the W-phase blinded reconciliation, with factorwise-defect qualification.
- **A12:** audited Q/Q′ bridge remains negative even in locally compact sober second-countable T1, and de Brecht yields quasi-Polish after the blind audit; no improper promotion found.
- **B07/B08:** independently reviewed compact scattered MAT/MUL and FINMAT/PATH correctly distinguished from general matrix associativity and referee-added one-sided results. In particular **MUL** is binary-only and respects genuine localic images via closed-sector splitting, not infinite-meet distribution.
- **B09:** broad TWIST partial-graph calculus was *not* blind accepted; complete lattice transport and postreport discrete-index comparison have distinct statuses.
- **B13:** four-step result is a **fixed bracketing**, with repaired special patch-fibre proof and qualified external verdict.
- **C04/C05/C08/C09:** four-audit distinctions E/X/I broadly correct. Chain→M 2-connective does **not** recover full 2-type; binary *maps* need M₂ preservation.
- **C10/C11:** Haine identification and crosscut ladder currently labeled internally checked or literature input, no false claim of priority or intrinsic shape.
- **Navigability:** the four new root-level consolidation files existed and their root-local markdown references resolved in a connector-level check; this does not verify every nested/remote link or render every mathematical expression.

## III. Residual limitations of this internal audit

1. The 40-row source crosswalk was **selective and theorem-oriented**, not a replay of every older proof or a new full independent mathematical audit of arbitrary localic composition and Čech/homotopy.
2. In particular, the older fourth audit invokes P1–P6 from earlier work. This segment checked their explicit provenance warnings but has **not** reconstructed each P_i from its original audit packet.
3. The exact tensorized safe two-to-one perfect-map graph result is still **I** as a combined claim despite the newer independently accepted MAT/BAL tools; an independent referee would need to inspect its geometric decomposition and ambient relation placement.
4. “No exact predecessor located” throughout the literature notes remains a limited search result and conveys **no priority verdict**.

## IV. Repair priority

**Immediate (do now):** AA-01, AA-02, AA-03, AA-04 and AA-05 in the current ledger/open-frontier register; mark repaired v3.1.

**Next brief revision:** AA-06 through AA-09; link this audit from START_HERE, README and the dependency atlas; preserve original audit packets, old master ledgers and historical bad statements **unaltered**.

**Final assessment after repairs:** Main architecture accepted **with mandatory corrections**, not yet declared final publication-ready archive. Recommend a second short consistency pass on links and statuses, then targeted example selection. No new speculative mathematics is required to close these issues.
