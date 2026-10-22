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

- 21 Oct 2026: **CORRECTION on U transitivity work:** prior purported universal I∘U⊆U / U∘I⊆U proof INVALID (wrongly promoted disjointness from I to U). In [transitivity note](A-D-U-transitivity-2026-10-21.md), absorption is marked unproved. Fitted + closed + symmetric + reflexive + absorption by I is not sufficient for transitivity (3-point discrete nontransitive graph). D=U⇒U transitive remains open arbitrary-frame, positive continuous/compact cases intact.

- 21 Oct 2026: Direct inequality attempt for D=U ⇒ U transitive gives on P=U_12∩U_23 only a₁∧b₃ ≤ (a*∧b*)₂ for far a,b. The residual cannot be removed by the argument; **general transitivity remains OPEN, route paused at user's request**. See [transitivity note](A-D-U-transitivity-2026-10-21.md).

- 21 Oct 2026: [D=U coproduct stability](A-coproduct-stability-D-U-2026-10-21.md): arbitrary coproducts of coherent D=U frames preserve equality (normal compact-open lattices/pm spectra); finite coproducts of continuous D=U frames preserve equality (Cm/Ury product calculation). **Arbitrary-frame coproduct preservation remains OPEN**; infinite continuous case not covered by local compactness argument.

- 21 Oct 2026: [Hochster duality of the coherent equality conditions](A-Hochster-duality-I-D-2026-10-21.md): for L coherent with L^vee=Idl(K(L)^op), **I(L)=U(L) iff D(L^vee)=U(L^vee)**, and conversely. On spectral points, I corresponds to common specialization upper bound and D to common lower bound, exchanged by the dual topology. Working theorem; novelty unchecked; not a literal identification of the two sublocales in differently topologized products.

- 21 Oct 2026: [Priestley description of U and I/D lattice operations](A-Priestley-U-and-I-D-lattice-2026-10-21.md): on spectral points, U requires intersecting downclosures of all clopen upset neighborhoods; Hochster dual uses upclosures of clopen downset neighborhoods. A five-point poset shows U differs under Hochster duality and I∨D⊊U; a diamond shows I∧D⊋Δ. Meet/join study added to agenda. Claims about sublocale joins outside finite spatial cases remain unproved.

- 21 Oct 2026 agenda reprioritization (user-approved): **ACTIVE NEXT**: intrinsic/localic meet and join I∧D and I∨D, followed by coherent/Priestley descriptions, Hochster duality, and equality conditions I∧D=Δ, I∨D=U, I=D. The ordered-spectral U result remains an input; unrestricted coproduct stability and other arbitrary-frame conjectures are deferred. Distinguish sublocale joins from unions of point sets.

- 21 Oct 2026: [Intrinsic frame theory for I∧D and I∨D](A-I-D-meet-join-frame-theory-2026-10-21.md): T(S)=cl(S)∧fit(S) is an idempotent, monotone, extensive hull; M=I∧D satisfies cl(M)=I and fit(M)=D. J=I∨D satisfies cl(J)=cl(D), fit(J)=fit(I). Explicit nuclei recorded. Next: compare J with cl(D)∧fit(I) and study interaction of these hulls; avoid assuming fittedness of U.

- 21 Oct 2026: [Alternating closed/fitted hull of diagonal](A-alternating-hull-diagonal-2026-10-21.md): define H as least simultaneously closed/fitted sublocale above Δ, transfinite alternating c,f. Always J=I∨D⊆H⊆F. **Finite Alexandrov:** H=F=union C×C over comparability components; five-point zigzag gives J⊊H and disproves J=c(D)∧fit(I). **Noncompact deleted plank:** H=U⊊F. Working proofs, independent audit pending.

- 21 Oct 2026: [Alternating hull transitivity](A-alternating-hull-transitivity-2026-10-21.md): H is always reflexive and symmetric; **D=U implies H=U**, so unrestricted H-transitivity would imply the earlier open U-transitivity conjecture. No general proof/counterexample. Finite Alexandrov and verified lower-point plank cases positive. Next prioritize J fixed-point question.

- 21 Oct 2026: [J fixed-point criterion and coproduct failure](A-J-fixedpoint-compositions-coproduct-2026-10-21.md): finite posets satisfy c(D)=I∘I and fit(I)=D∘D, hence J=T(J) iff I²∩D²=I∪D. Four-point zigzag fails fixedness. **Binary frame coproduct preservation FAILS**, witnessed by three-point V and its dual, each fixed but product nonfixed. Finite Hochster order duality preserves M, J, T(J), H point relations. General coherent/localic extensions open.

- 22 Oct 2026: [Cross-hulls and composition in spectral spaces](A-cross-hulls-composition-spectral-2026-10-22.md): for ordinary points of spectral X, topological cl(D)=I∘I and intersection of ordinary opens containing I equals D∘D, by compact patch/Priestley separation. **Not yet a localic sublocale equality**: image and fitting can be nonspatial. Frame formulas c(D)=C(j_D(0)) and f(I)=meet of O(w) with d_I∨w=1 recorded. General localic identities open.

- 21 Oct 2026, coherent cross-hull follow-up: [spectral cross-hull note](A-cross-hulls-composition-spectral-2026-10-22.md) now shows I∘I is closed for **compact locales** (proper projection of closed composable pairs), and **I∘I⊆cl(D)** for coherent locales (spatial closed source + spectral point inclusion). Reverse inclusion and coherent f(I)=D∘D remain **OPEN**, no point-to-sublocale promotion.

- 21 Oct 2026: **Coherent cross-hull first identity RESOLVED:** [cross-hull note](A-cross-hulls-composition-spectral-2026-10-22.md) proves **c(D)=I∘I=U** as localic closed sublocales for every coherent locale (spectral compact-open separation plus compact middle projection). This supersedes earlier coherent-case 'open' status; second identity fit(I)=D∘D remains open. Novelty unverified.

- 21 Oct 2026: [Coherent dual characterizations](A-coherent-dual-characterizations-2026-10-21.md): **I=U iff I fitted iff I internally transitive; D=U iff D closed iff D internally transitive**, via classical spectral unique-max/unique-min specialization. **I transitive closure is NOT generally contained in U**: five-point overlapping forks p<a,b and q<b,c give I-path a–p–b–q–c but a not U c. Prior zigzag example in chat was incorrect and corrected.

- 21 Oct 2026: [Reconciliation of independent coherent audits](A-coherent-external-audits-reconciliation-2026-10-21.md): ChatGPT High and Claude Opus 5.5 Extra endorse coherent U=I²=c(D) and both dual chains; Claude spots invalid general image-points inference and supplies repair. Claude additionally **proposes/proves in its report** coherent fit(I)=D² via compact-filter spatiality lemma, arbitrary compact U=I², and noncoherent compact c(D)≠U counterexample. New claims pending focused project-side proof verification; no novelty assertion.

- 21 Oct 2026: [Focused verification of Claude's three new claims](A-Claude-three-claims-focused-verification-2026-10-21.md): **confirmed** coherent **V=fit(I)=D∘D** via compact-open filters; confirmed **U=I∘I for all compact locales** (proper-projection/finite-rectangle argument); confirmed compact, locally compact, sober T1 noncoherent counterexample **c(D)⊊U** via 2-step fitted-diagonal nucleus. Stronger c(D)=I in example unverified. Prior coherent mirror OPEN status superseded. Novelty unverified.

- 21 Oct 2026: [V fitted companion: hierarchy, duality, preservation](A-V-relation-hierarchy-duality-preservation-2026-10-21.md). Definition V:=fit(I) for all locales; coherent characterization V=D∘D, mirrored by U=c(D)=I∘I. Universal J⊆V⊆F; coherent U,V⊆H and U,V incomparable (five-point forks; six-point zigzag gives U∨V⊊H). Spectral Hochster point dual U_X↔V_Xvee; finite coherent locale-product behavior and disjoint-union decompositions; V=I and V=D are coherent conormal/normal conditions and inherit their coproduct preservation. New preservation assertions working, targeted audit recommended.

- 21 Oct 2026: [Intrinsic dual-farness formula for V](A-V-dual-farness-intrinsic-2026-10-21.md): define compact k,h **dual far** iff d_I∨(k⊠1)∨(1⊠h)=1. For coherent L, **V=meet of open strips O((k⊠1)∨(1⊠h)) over all dual-far pairs**, a fitted open-strip counterpart to closed far-rectangle presentation of U. Spectral proof via patch compactness plus coherent-filter spatiality; dual far implies k∨h=1. Extension beyond coherent and point-free proof open.

- 21 Oct 2026: [Dual farness simplified](A-V-dual-farness-intrinsic-2026-10-21.md): for **compact frames** and arbitrary k,h, d_I∨(k⊠1)∨(1⊠h)=1 iff there are disjoint supplements a,b with k∨a=h∨b=1 and a∧b=0. Finite rectangle lemma proves the nontrivial direction. For coherent compact k,h take compact witnesses. Thus normality iff every 2-cover is dual-far. V's meet-of-strips formula remains coherent-only proved.

- 21 Oct 2026: [Dual-farness compact/infinite follow-up](A-dual-farness-compact-and-infinite-2026-10-21.md): disjoint-supplement criterion extends to arbitrary locales when closed complements C(k),C(h) are compact. It **fails for arbitrary frames**: Hausdorff nonnormal Sorgenfrey plane has disjoint closed sets not openly separable. General dual far iff disjoint rectangles cover C(k)×C(h). Strip relation W contains V universally; W=V verified for coherent and compact Hausdorff locales; **arbitrary compact-locale strip formula unresolved**, noncoherent three-limit-point example suggested test.

- 21 Oct 2026: **Compact dual Urysohn strip formula RESOLVED** in [dual-farness follow-up](A-dual-farness-compact-and-infinite-2026-10-21.md). General theorem: for ANY compact sublocale S of X×Y, fit(S) is intersection of all open vertical/horizontal strips containing S. Proof uses a finite rectangle subcover and finite distributive DNF→CNF identity. Thus for every compact locale X, V=fit(I)=meet of all dual-far strips, and using compact disjoint-supplement criterion, V=meet over k∨a=h∨b=1, a∧b=0 of O((k⊠1)∨(1⊠h)). No coherence/spatiality. Noncompact generalization remains unsettled; arbitrary-frame finite-witness criterion demonstrably fails in nonnormal Hausdorff spaces.

- 21 Oct 2026: [Noncompact strip push](A-dual-farness-compact-and-infinite-2026-10-21.md): on ordinary points, for every (possibly infinite) Alexandrov poset, the intersection of all open strips containing I is ↑I=D∘D, via strips built from complements of principal downsets. For T1 spaces, both strip intersection and ordinary open-neighborhood intersection have point set I, so points alone cannot decide the localic equality. Infinite DNF→CNF fails in general frames (lack of complete distributivity); arbitrary noncompact **localic** V=W remains open.

- 21 Oct 2026: [Nuclei-lattice reduction for noncompact V strips](A-dual-farness-compact-and-infinite-2026-10-21.md): write Φ={w:d_I∨w=1} and Σ=dual-far strips. j_V=join_Nuc{o_w:w∈Φ}, j_W=join_Nuc{o_s:s∈Σ}. Universal W=V iff each w∈Φ satisfies j_W(w)=1. Explicit directed prenucleus P(q)=∨_{finite strip meets s}(s→q) generates j_W by transfinite iteration, so a counterexample is w∈Φ with P^∞(w)≠1. No unrestricted equality/counterexample yet.

- 21 Oct 2026: [One-stage nucleus saturation (9), noncompact positive case](A-dual-farness-compact-and-infinite-2026-10-21.md): for any **spatial Urysohn space** (distinct points have neighborhoods with disjoint closures), every diagonal neighborhood w satisfies P(w)=1 at the first stage. Each off-diagonal (x,y) has an open rectangular neighborhood disjoint from some dual-far strip. Requires neither compactness nor coherence; arbitrary-frame (9) remains unresolved.

- 21 Oct 2026: [Hausdorff strip nucleus / Cantor–Bendixson](A-dual-farness-compact-and-infinite-2026-10-21.md): for diagonal neighborhood W in Hausdorff X, with closed F=X²\W, s→W=X²\cl(s∩F). Every isolated point of F is removed by its singleton-complement dual-far strip. Transfinite induction shows **Wstrip=fit(I)** whenever **X² is scattered**, with no compactness. This settles full nucleus equality in a further class but not one-stage (9) or arbitrary Hausdorff non-Urysohn cases; any obstruction must persist beyond isolated-point pruning.
