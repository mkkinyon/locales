# Project A — Consolidation and audit of the \(\mathcal V\) program

**8 November 2026 · working consolidation; no novelty claim · not a new blind external referee report**

This document consolidates the long Session 3 investigation and subsequent corrections, using the final repository theorem notes and their audit reconciliations. It distinguishes **certificate rank**, **strictness of rank-bounded fitted sublocales**, and **the conceptual search for a dual of \(\mathcal U\)**. Earlier exploratory notes remain valuable research history, but their provisional questions and claims must not override the corrected source ledger below.

## 1. Reframe the original motivation

The coherent/spectral theory gives the paired identities

\[
\mathcal U=\operatorname{cl}(\mathcal D)=\mathcal I\circ\mathcal I,\qquad
\mathcal V=\operatorname{fit}(\mathcal I)=\mathcal D\circ\mathcal D.
\]

On arbitrary locales, however, \(\operatorname{cl}(\mathcal D)\) can be **strictly smaller** than \(\mathcal U\). Our permanent notation is \(\mathcal W=\operatorname{cl}(\mathcal D)\). Thus the literal closure–fitting dual of \(\mathcal V\) is \(\mathcal W\), *not necessarily* \(\mathcal U\). The original search tried to answer two different questions by one construction: (a) calculate \(\operatorname{fit}(\mathcal I)\) intrinsically, and (b) locate a localic analogue of the \(\mathcal U\)-phenomenon under a broader form of duality. These should be separated.

The user's further suggestion of a possible intrinsic relation lying above \(\mathcal V\), analogous to \(\mathcal W\subseteq\mathcal U\), is worth **recording, not pursuing now**. No existence or uniqueness assertion, definition, or new permanent notation is justified by the present work. The November 6–7 mixed-composition results make this a possible *future* organizing idea, not a license to replace \(\mathcal V\) inside proved statements.

**Useful perspective:** What survived of the \(\mathcal V\) search was not a new definition of its alleged 'dual', but a mathematically substantive account of how fitting an inseparability relation depends on infinitary rectangular cover proofs.

## 2. The exact intrinsic calculus (valid, but not the desired conceptual dual)

Set \(L=\mathcal O(X)\), \(Q=L\oplus L\), and

\[
d=d_{\mathcal I}=\bigvee_{a\wedge b=0}a\boxtimes b,\qquad
\mathcal I=C(d),\qquad \mathcal V=\operatorname{fit}(\mathcal I).
\]

A **bar** is an open \(w\in Q\) with \(d\vee w=1\). Equivalently, its canonical rectangular leaf family \(B_w=\{(a,b):a\boxtimes b\le w\}\), combined with the zero-meet leaves \(D=\{(a,b):a\wedge b=0\}\), generates \((1,1)\) under downward closure and arbitrary joins separately in either coordinate. This is the standard cp-ideal/C-ideal presentation of \(L\oplus L\).

The **separation-tree completeness theorem** translates that condition into a well-founded rooted tree whose internal nodes are exact horizontal or vertical coordinate covers and whose leaves come from \(D\cup B_w\). Consecutive nodes of the same orientation can be flattened. Therefore

\[
\mathcal V=\bigcap_{w:\,d\vee w=1}O(w)
\]

admits an exact *coordinate-only* presentation by all well-founded separation trees. **Status I:** straightforward C-ideal completeness proof; not a simpler conceptual separation relation. The external checks of particular constructions exercise this proof calculus but do not constitute a novelty claim.

**Finite-rank approximations.** Let \(\mathrm{rk}(w)\) be the least ordinal rank of such a tree; leaves have rank 0 and the rank of an internal node is \(\sup\{\mathrm{rk}(\mathrm{child})+1\}\). Put

\[
\begin{aligned}
\mathcal V_n&=\bigcap_{\mathrm{rk}(w)\le n,\,w\text{ bar}}O(w),\\
\mathcal V_{\mathrm{fin}}&=\bigcap_{n<\omega}\mathcal V_n.
\end{aligned}
\]

Then \(\mathcal V\subseteq\mathcal V_{\mathrm{fin}}\subseteq\cdots\subseteq\mathcal V_3\subseteq\mathcal V_2\). The inclusion of **all** finite-rank tests need not recover the meet over all bars. A strict inequality of ranks for *individual opens* does not, by itself, imply a strict inequality of the **fitted sublocales**.

**Canonical sources:** [rectangular bars](https://github.com/mkkinyon/locales/blob/main/A-V-rectangular-bar-characterization-2026-10-22.md); [separation-tree normal form](https://github.com/mkkinyon/locales/blob/main/A-V-separation-tree-normal-form-2026-10-22.md); [unbounded-rank consequences and nucleus warning](https://github.com/mkkinyon/locales/blob/main/A-V-unbounded-rank-consequences-for-fitted-relation-2026-10-22.md).

## 3. The dual-far strip search: a positive coherent theorem and a negative unrestricted theorem

A **dual-far strip** has the form \(s=(a\boxtimes1)\vee(1\boxtimes b)\) with \(d\vee s=1\). Equivalently its complementary closed rectangle is disjoint from \(\mathcal I\). Let \(\mathcal V_{\mathrm{strip}}\) be the intersection of the corresponding open sublocales; this is **temporary explanatory notation**, not a new named relation in Project A. Necessarily \(\mathcal V\subseteq\mathcal V_{\mathrm{strip}}\).

- **Coherent:** \(\mathcal V_{\mathrm{strip}}=\mathcal V\). A compact-open-filter/Priestley representation reduces all fitted neighborhoods to such strips, and Hochster order reversal exchanges the \(\mathcal U\)-point formula with the \(\mathcal V\)-point formula. The compact-strip description has a proof in the coherent sources; the full localic Hochster statement has the qualifications already recorded under C6l in the main inventory.
- **Arbitrary:** the equality fails. The audited rational two-sheet graph construction gives a nonzero closed graph residual disjoint from \(\mathcal I\) that is not excluded by any individual dual-far strip, although an unrestricted open bar excludes it. This is a *genuine localic sublocale* counterexample, not merely a failed pointwise characterization.

The broader inference is **negative**: a finitary family of strip/neighborhood tests cannot be a complete intrinsic presentation of \(\mathcal V\) for all frames. It does **not** exclude all possible non-finitary or conceptual dual descriptions.

**Sources and independent review:** [compact dual-farness](https://github.com/mkkinyon/locales/blob/main/A-V-dual-farness-intrinsic-2026-10-21.md); [October 22 external strip-audit reconciliation](https://github.com/mkkinyon/locales/blob/main/A-V-Claude-external-audit-reconciliation-2026-10-22.md). **Status:** coherent theorem I/E* by the underlying spectral package; arbitrary counterexample E (external blind referee verified the graph/rectangle mechanism).

**Editorial naming warning:** An older note used \(W\) for the **strip approximation**. That historical temporary \(W\) must never be confused with the later permanent \(\mathcal W=\operatorname{cl}(\mathcal D)\).

## 4. Rank-collapse theorems and their true scopes

| Hypothesis on \(L\) or on its point space | Result about **every** bar | Verification status / caveat |
|---|---|---|
| **Compact** locale | Rank at most 2 | I; finite rectangular cover reflection; no spatiality assumption |
| **Regular** frame | Rank at most 2 | I; direct rather-below decomposition, no compactness |
| Scott opens of a **continuous dcpo** | Rank at most 2 | I; locally supercompact cover by \(\{z:p\ll z\}\), using point evaluation only in the safe direction |
| **Algebraic** frame | Rank at most 3 | I; universal three-step horizontal/vertical interchange for arbitrary lower rectangle families |
| **Continuous** frame | Rank at most 3 | I; extends algebraic interchange by way-below finite approximation |
| Arbitrary frame | No finite bound | E for the explicit unbounded and \(\omega\)-rank family; **not** a negative universal-rank theorem for any *specified* shorter class |

These do not contradict each other: e.g. coherent frames are compact, so the **stronger rank-two** bound applies. The continuous-frame bound is three, but regular continuous frames already have rank two. The Scott-domain result is likewise stronger than the general continuous-frame bound within that subclass.

The basic obstruction to upgrading all general-frame arguments is the failure of **infinitary coordinate interchange**: finite joins may commute across the two saturation operators while unrestricted joins do not. The original proof of the algebraic and continuous bounds makes the exact finite-approximation hypothesis explicit.

**Canonical sources:** [compact](https://github.com/mkkinyon/locales/blob/main/A-V-compact-locale-universal-depth-two-2026-10-22.md); [regular](https://github.com/mkkinyon/locales/blob/main/A-V-regular-frames-universal-depth-two-2026-10-22.md); [continuous dcpo](https://github.com/mkkinyon/locales/blob/main/A-V-continuous-dcpo-universal-depth-two-2026-10-22.md); [algebraic](https://github.com/mkkinyon/locales/blob/main/A-V-algebraic-frame-universal-depth-three-2026-10-22.md); [continuous](https://github.com/mkkinyon/locales/blob/main/A-V-continuous-frame-universal-depth-three-2026-10-22.md).

## 5. Unbounded individual ranks, strict stages, and the negative finite-rank exhaustion theorem

These are **three logically different statements**.

### 5a. Arbitrarily large finite ranks and a rank-\(\omega\) bar

The iterated countable, first-countable Hausdorff **asymmetric \(K\)-fan** construction produces canonical two-rectangle strip bars \(w_m\) of unbounded exact finite ranks and an assembled bar of exact rank \(\omega\). The transfinite lower bound uses restriction to clopen fan components; the well-founded upper bound comes from the explicit rooted proof trees. External audit of the subsequent finite-rank-exhaustion packet checked the fan input.

**Crucial caveat:** On the *disjoint union* of those fans, the finite-rank fitted approximation can already equal the full \(\mathcal V\). Indeed local finite proofs can be patched with finitely supported clopen covers, and the rank-\(\omega\) bar need not create a new fitted-sublocale obstruction. The source explicitly proves that its \(\omega\)-rank bar is killed by the finite-rank nucleus. This invalidates the naive argument “high rank \(\Rightarrow\) new stage.”

### 5b. Genuine strict finite stages

A rational two-sheet bridge yields \(\mathcal V_2\supsetneq\mathcal V_3\), with a graph-null rank-three bar \(q\). The proof does **not** stop at \(\mathrm{rk}(q)=3\): it shows that every rank-two bar pulls back densely along the rational parameter graph, so the stage-two nucleus fixes \(q\), whereas the stage-three nucleus sends it to top. **Status I** (internally proved; source linked below).

A more complicated two-level noncofinite bridge yields \(\mathcal V_3\supsetneq\mathcal V_4\). **Status E*** (blind independent referee checked the main theorem, but the required exact coordinate/tail and tree-quantifier repairs must be incorporated from the reconciliation). The two examples can be put on one disjoint union to exhibit both strict inclusions, using the separate internally supported theorem that \(\mathcal V_n\) for \(n\ge2\) respects arbitrary clopen sums. These results **do not** prove strictness at every finite stage.

**Sources:** [strict second-to-third stage](https://github.com/mkkinyon/locales/blob/main/A-V-strict-V2-V3-fitted-rank-hierarchy-2026-10-23.md); [strict third-to-fourth with corrections](https://github.com/mkkinyon/locales/blob/main/A-V-noncofinite-bridge-external-audit-reconciliation-2026-10-23.md); [disjoint-union preservation](https://github.com/mkkinyon/locales/blob/main/A-V-finite-fitted-rank-stages-disjoint-union-preservation-2026-10-23.md).

### 5c. The decisive result: \(\mathcal V_{\mathrm{fin}}\supsetneq\mathcal V\)

The **independently audited negative answer to Question A** uses an additional mechanism beyond simply adjoining more fan stages:

1. Construct a countable clopen sum \(Y\) of asymmetric \(K\)-fans with disjoint closed pole sets \(C,F\) and a special strip bar \(w=(Y\setminus C)\boxtimes1\vee1\boxtimes(Y\setminus F)\) of exact rank \(\omega\).
2. **Do not** take just a larger clopen disjoint union. Instead adjoin two generic points \(\ell,r\), with opens meeting \(C\) forced to contain \(\ell\), and opens meeting \(F\) forced to contain \(r\). The resulting \(X_0\) is **countable, first-countable, sober, \(T_0\), not \(T_1\)**.
3. The largest open \(q\) omitting the ordinary product point \((\ell,r)\) is again a **two-rectangle strip bar** of exact rank \(\omega\). Every finite-rank bar must contain \((\ell,r)\), by restriction to the old \(Y\)-strip proof; \(q\) does not. Hence \((\ell,r)\in\operatorname{pt}(\mathcal V_{\mathrm{fin}})\setminus\operatorname{pt}(\mathcal V)\).
4. A different **cofinite pair of rational sheets** produces a countable first-countable **\(T_1\) non-Hausdorff** example with the same strict inequality, witnessed by a graph-null open and the graph-density/nucleus test. The proof does not assume the localic square is spatial.

The original cofinite-sheet theorem and fan input passed a **genuinely blind external audit** (90–95% reported confidence); the simpler sober two-generic-point transfer was suggested by that referee and checked in the reconciliation. Thus the *negative answer* is externally well corroborated. The two-generic-point sharpened presentation is **referee-informed internal verification**, not a separately blind audit of every line of its final prose.

**What this does *not* say:** no strictness \(\mathcal V_n\supsetneq\mathcal V_{n+1}\) at every \(n\); no formula for the actual \(\mathcal V\) avoiding fitting; no associativity result; no priority assessment.

**Canonical sources:** [final consolidated negative proof](https://github.com/mkkinyon/locales/blob/main/A-Vfin-negative-consolidated-proof-2026-10-23.md); [blind-audit reconciliation and generic-point simplification](https://github.com/mkkinyon/locales/blob/main/A-V-fin-negative-independent-audit-reconciliation-and-generic-points-2026-10-23.md); [clopen locality: why the raw fan sum does not suffice](https://github.com/mkkinyon/locales/blob/main/A-V-question-A-clopen-locality-and-fan-equality-2026-10-23.md).

## 6. Positive structural comparisons: what \(\mathcal V\) is, and is not

### 6a. Universal intermediate apartness relation

Put \(a\prec b\) iff \(a^*\vee b=1\), and let
\[
 d_2=\bigvee\{c\boxtimes f: c\prec a,\ f\prec b,\ a\wedge b=0\text{ for some }a,b\in L\}.
\]
The correct universal inclusions are
\[
 d_{\mathcal F}\le d_2\le d_{\mathcal U}\le d_{\mathcal I},
\qquad
\mathcal I\subseteq\mathcal V\subseteq\mathcal V_2\subseteq C(d_2)\subseteq\mathcal F,
\qquad
\mathcal U\subseteq C(d_2).
\]
**There is no universal order between \(\mathcal U\) and \(\mathcal V\).** The latter has finite-poset witnesses in both directions, and a blind referee's mistaken assertion \(\mathcal V\subseteq\mathcal U\) was explicitly rejected. When \(d_2=d_{\mathcal I}\), the stronger result \(\mathcal I=\mathcal V=\mathcal V_2\) follows from a direct rank-two annihilator proof, without asserting \(\mathcal I=\mathcal F\).

**Sources:** [two-step apartness](https://github.com/mkkinyon/locales/blob/main/A-V-two-step-apartness-I-U-F-hierarchy-2026-10-23.md); [fitted rank-two annihilator](https://github.com/mkkinyon/locales/blob/main/A-V-fitted-diagonal-regular-apartness-and-fan-induction-2026-10-23.md); [Fable audit corrections](https://github.com/mkkinyon/locales/blob/main/A-V-Claude-Fable-blind-audit-reconciliation-2026-10-23.md).

### 6b. Closedness of \(\mathcal V\), fittedness of \(\mathcal I\)

For \(d=d_{\mathcal I}\), let \(F_d=\{w:d\vee w=1\}\) and \(k=j_{\mathcal V}(0)\le d\). The exact arbitrary-frame classification is:

- \(\mathcal I=\mathcal V\) iff \(k=d\).
- \(\mathcal V\) is closed iff \(F_k=F_d\). In this case \(\mathcal V=C(k)\); it may still properly contain \(\mathcal I\).
- Otherwise \(\mathcal V\) is not closed, and \(\operatorname{cl}(\mathcal V)=C(k)\) is strictly larger.

These are exact nucleus/supplement-filter tests, but partially restate the general semiclosed-sublocale calculus. **Status I**, literature comparison required. Picado–Pultr call \(\operatorname{fit}(C(d))\) a *semiclosed sublocale*: this connects \(\mathcal V\) to existing terminology without settling the search for a conceptual dual of \(\mathcal U\).

For coherent \(X\), the more substantial theorem is \(\mathcal I=\mathcal V\iff\mathcal I=\mathcal U\), while \(\mathcal V\) closed \(\iff\mathcal V=\mathcal F\) (the latter in the later spectral synthesis; verification status I). Under Hochster duality these are mirrored by the corresponding \(\mathcal D\)/\(\mathcal U\) statements. The unrestricted \(\mathcal V\)-closedness equivalence is **not** claimed.

**Source:** [semiclosed/nucleus/closedness criteria](https://github.com/mkkinyon/locales/blob/main/A-V-closedness-and-fitted-inseparability-Alexandrov-classification-2026-10-23.md); [coherent Hochster synthesis](https://github.com/mkkinyon/locales/blob/main/A-V-Hochster-duality-spectral-relations-2026-10-23.md).

### 6c. Almost-normality — do not confuse \(\mathcal V_2\) with \(\mathcal V\)

If the rather-below relation interpolates (the established meaning of *almost normal* for frames), an internal proof gives
\[
 \mathcal V_2=\mathcal U=\mathcal F.
\]
It does **not** imply \(\mathcal V=\mathcal V_2\) in arbitrary noncompact locales. An audited almost-normal, countable, noncompact \(T_0\) thickened-zigzag example has a nonclosed \(\mathcal V\), with \(\mathcal V\subsetneq\mathcal U=\mathcal F\). The stronger claims in some earlier notes, particularly an asserted strict \(\mathcal I\subsetneq\mathcal V\) in a different Fable example, must be distinguished: that particular strictness was *not proved* in the blind packet and was rejected in reconciliation.

A further **internally derived** sufficient condition is that *almost normal + subfit* implies \(\mathcal I=\mathcal V=\mathcal V_2=\mathcal U=\mathcal F\), using a published Picado–Pultr approximation lemma. Its argument and literature dependence need checking before attributing it independent external status. In particular, it must not be confused with the non-subfit thickened-zigzag counterexample.

**Sources:** [almost-normal rank-two result](https://github.com/mkkinyon/locales/blob/main/A-V-almost-normal-rank-two-equals-F-2026-10-23.md); [almost-normal subfit collapse](https://github.com/mkkinyon/locales/blob/main/A-V-almost-normal-subfit-full-collapse-2026-10-23.md); [nonclosed thickened zigzag](https://github.com/mkkinyon/locales/blob/main/A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md); [post-V external reconciliation](https://github.com/mkkinyon/locales/blob/main/A-postV-external-audit-reconciliation-2026-10-24.md).

## 7. Methods tested but not canonical theorems defining \(\mathcal V\)

1. **Restricting to dual-far strips** fails for arbitrary locales (externally checked); it succeeds under coherent hypotheses.
2. **Replacing the full neighborhood filter by all finite-rank bars** fails, even for small countable spaces (externally checked). This is the central negative theorem, not an unsuccessful proof attempt.
3. **Graph-far, partial-map, or finite graph-family candidates** suggested useful obstruction probes but no general complete formula. No unproved representation theorem should be silently imported.
4. **Iterating fan height or taking clopen sums** generates high individual rank, not necessarily new fitted stages or \(\mathcal V_{\mathrm{fin}}\ne\mathcal V\). The graph/generic-point transfer is the missing mechanism.
5. **Strongly exact versus regular filter completions:** the strongly exact completion of finite bars is insufficient in the negative example, while internally checked regular-filter calculations recover the full bar filter on the *specific two-generic-point* example. A spatial-square closed-point detection condition yields regular completion at rank two in a useful subclass. These are interesting side results, but **no universal intrinsic formula** for \(\mathcal V\) has been established via regular filters.
6. **Higher finite and ordinal construction projects** have no immediate bearing on the conceptual duality question now being set aside. The \(\omega\)-rank and \(\omega\)-exhaustion counterexamples already provide the key qualitative boundary; further rank escalation is deliberately deferred.

**Filter sources:** [strongly exact first segment](https://github.com/mkkinyon/locales/blob/main/A-V-strongly-exact-filters-first-segment-2026-10-24.md); [specific full regular completion](https://github.com/mkkinyon/locales/blob/main/A-V-regular-filter-completion-full-generic-example-segment-three-2026-10-24.md); [spatial-square rank-two regular generation](https://github.com/mkkinyon/locales/blob/main/A-V-regular-filter-spatial-square-rank-two-generation-2026-10-24.md).

## 8. Corrections, audit provenance, and status ledger

| ID | Result | Status | Critical limitation / source |
|---|---|---|---|
| V1 | Exact C-ideal bar and separation-tree calculus | **I** | Formal but not a new conceptual dual |
| V2 | Coherent dual-far-strip description | **I/E*** | Uses spectral/compact-open-filter representation; not unrestricted |
| V3 | Unrestricted dual-far strips insufficient | **E** | Blind October 22 graph audit |
| V4 | All compact/regular bars depth \(\le2\); continuous/algebraic bars \(\le3\); continuous dcpo Scott bars \(\le2\) | **I** | Direct proofs in specialized notes; not one jointly blind-refereed theorem |
| V5 | Unbounded finite ranks and exact rank-\(\omega\) special strip | **E*** | Fan input included in blind October 23 V_fin audit |
| V6 | \(\mathcal V_2\supsetneq\mathcal V_3\) | **I** | Graph-density witness, not rank alone |
| V7 | \(\mathcal V_3\supsetneq\mathcal V_4\) | **E*** | Independent blind check conditional on construction/proof repairs |
| V8 | \(\mathcal V\subsetneq\mathcal V_{\mathrm{fin}}\) on countable first-countable \(T_1\) space | **E** | Independent blind external audit; not necessarily Hausdorff |
| V9 | Countable first-countable sober \(T_0\) two-generic-point strengthening | **I (referee-informed)** | Independently suggested and subsequently checked; localic square need not be spatial |
| V10 | \(d_{\mathcal F}\le d_2\le d_{\mathcal U}\le d_{\mathcal I}\); \(\mathcal V\le\mathcal V_2\le C(d_2)\) | **I** | Exact frame inclusion; no \(\mathcal V\le\mathcal U\) |
| V11 | \(\mathcal V\) closedness / \(\mathcal I\) fittedness via semiclosed-sublocale nuclei | **I** | Exact but partly reformulatory |
| V12 | Almost-normal: \(\mathcal V_2=\mathcal U=\mathcal F\) | **I** | Full \(\mathcal V\) may differ |
| V13 | Almost-normal nonclosed \(\mathcal V\) counterexample | **E*** | Post-V audit checks thickened-zigzag and its spatiality dependencies |
| V14 | Almost-normal + subfit \(\Rightarrow\mathcal I=\mathcal V=\mathcal U=\mathcal F\) | **I** | Uses published Picado–Pultr approximation lemma; independent check still useful |
| V15 | Full regular-filter recovery in the specific two-generic-point negative example | **I** | Not general formula and not \(\mathcal V=\mathcal V_{\mathrm{fin}}\) |

**External-audit corrections to preserve:** (i) an earlier blind referee erroneously asserted \(\mathcal V\subseteq\mathcal U\), disproved by a five-point poset; (ii) an earlier claim \(\mathcal I\subsetneq\mathcal V\) in the Fable construction was unsupported; (iii) a referee's optional geometric nonregularity explanation for the two-level bridge was false but repaired without changing its main fitted-stage theorem; (iv) no blanket spatiality or “point equality implies sublocale equality” principle is allowed; (v) an old note asking whether \(\mathcal V_{\mathrm{fin}}=\mathcal V\) is **open** predates the October 23 negative theorem and is superseded.

Here **E*** means an external referee checked the stated result as input or with specified repairs, but we should not claim the entire final reworked source is separately independently checked.

## 9. Recommended proof architecture for eventual exposition

1. Start with the separation problem and the **formal** \(\mathcal W\)/\(\mathcal V\) pair; explain why the intuitive \(\mathcal U\)/\(\mathcal V\) pairing is a coherent-only phenomenon.
2. Give the C-ideal/bar/separation-tree construction once. Distinguish the tautological completeness from any deeper duality question.
3. Present the positive universal-depth results and prove the rank-versus-sublocale warning using the clopen fan sum.
4. Present the audited negative finite-rank exhaustion theorem using the *short two-generic-point proof* for conceptual clarity, followed by the fully externally checked \(T_1\) cofinite-sheet version when stronger separation hypotheses matter.
5. Treat strict \(\mathcal V_2/\mathcal V_3\) and \(\mathcal V_3/\mathcal V_4\) as supporting examples, not prerequisites of the main negative theorem.
6. Put semiclosed criteria, almost normality, regular filters, and candidate dual primitives in a separate structural appendix or research ledger, unless later work provides a simpler unifying theorem.
7. **Park** the question of a new dual relation above \(\mathcal V\) and any future \(\mathcal V_n\)-rank construction. They are not prerequisites for consolidating Project A.

**Bottom line.** The original intrinsic-duality motivation is unresolved, but the \(\mathcal V\) project produced two significant negative structural conclusions—restricted strip tests and even all finite-depth tests can miss part of \(\mathcal V\)—alongside useful positive results giving exactly when low-depth normalization works. These are the results to preserve prominently. The rest is method development and archival research context, not a failed program.