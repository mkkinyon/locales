# Project A — Theorem and dependency inventory

**Version 0.7 (properness, effectivity and Scott-continuity audit incorporated; provisional) — 8 November 2026**

A theorem-oriented inventory, not a chronological record. This revision checks the coherent package against the October 21 blind referee report, the October 24 post-V reconciliation, and the November 7 categorical audit notes. It does not certify unpublished literature priority. Prepared from the repository `mkkinyon/locales`, in particular `A-hierarchy-first-results.md`, `A-fitted-diagonal.md`, `A-coherent-external-audits-reconciliation-2026-10-21.md`, `A-postV-external-audit-reconciliation-2026-10-24.md`, `A-WU-external-audit-reconciliation-2026-10-24.md`, `A-mixed-composition-external-audit-reconciliation-2026-11-07.md`, and the associativity audit notes of 7 November. The source documents—not this overview—remain authoritative for proofs.

## Legend and methodology

- **E:** externally checked, with substantial corrections/conditions incorporated; *only* the listed theorem/packet scope is certified.
- **I:** complete working proof internally checked; independent mathematical review outstanding.
- **W:** working result with a specific unverified proof dependency or incomplete reconciliation.
- **O:** open.

Originality and correctness are independent. E does **not** mean new. Prior published definitions and background facts must be cited independently. Parenthesization is required in general localic relational composition.

## Notation

For a locale `X`, put `L=O(X)`, `Q=L⊕L=O(X×X)`, write `a⊠b` for open rectangles, `a*` for pseudocomplement, `Δ` for the diagonal image, `C(d)` for the closed complement of the open `d`, and `fit` for fitted hull. Define

- `I=cl(Δ)=C(d_I)`, `d_I=⋁_{a∧b=0}a⊠b=⋁_a a⊠a*`.
- `D=fit(Δ)`.
- `U=C(d_U)`, `d_U=⋁_{a*∨b*=1}a⊠b`.
- `F=⋀_{f:X→ℝ}ker(f)` (real-functional equivalence; **not** the F-separatedness axiom).
- `V=fit(I)`, `W=cl(D)`, `M=I∧D`, `J=I∨D`, and `H` the least simultaneously closed-and-fitted relation containing `Δ`.
- `T(S)=cl(S)∧fit(S)`.

Composition `R∘S` is in **diagrammatic order** (first R, then S), the localic image of the composable-pair sublocale. In general it need not associate.

## I. Foundational localic calculus

| ID | Theorem / statement | Scope | Status | Main dependencies / caution |
|---|---|---|---|---|
| F1 | `I=cl Δ` and the one-parameter generator formula for `d_I` | All locales | E | Frame coproduct and diagonal pullback |
| F2 | `D=fit Δ`; for ordinary pairs, `xDy` iff every open cover has a member containing both, equivalently `cl{x}∩cl{y}≠∅` | All locales / ordinary points | E | Distinguish ordinary-point behavior from sublocale equality |
| F3 | `Δ≤I≤U≤F` and `Δ≤D≤U` | All locales | E | Direct point-free frame arguments; no relational composition |
| F4 | `I` and `D` incomparable | All locales, counterexamples finite | E | Three-point V and Λ posets |
| F5 | `F` is closed, fitted and an internal equivalence relation | All locales | E | Kernel pairs of real maps; real-line regularity |
| F6 | `I∘I≤U` | All locales | I | Direct three-coordinate far-rectangle calculation; no associativity needed |
| F7 | For maps `h:X→Y`, `R_X≤(h×h)^−1 R_Y` for `R∈{I,U,F}` | All locales | E | Inverse-image frame calculations |
| F8 | `I,D≤J≤U,V`; `W≤U`; `W∨V≤H≤F`; `T(J)=W∧V` | All locales | E | Closure and fitting hull identities; post-V external referee |
| F9 | `H` exists and admits a closed/fitted iterative hull calculation | All locales | E | Lattice of sublocales; full iteration theorem in post-V packet |

**Safe core:** F1–F9 do not depend on associativity of arbitrary localic relational composition. The label E for elementary results means covered by and consistent with independent foundational/hierarchy reviews, not individually refereed in isolation.

**Source:** [foundational hierarchy](https://github.com/mkkinyon/locales/blob/main/A-hierarchy-first-results.md), [fitted diagonal](https://github.com/mkkinyon/locales/blob/main/A-fitted-diagonal.md), [post-V reconciliation](https://github.com/mkkinyon/locales/blob/main/A-postV-external-audit-reconciliation-2026-10-24.md).

## II. Coherent / spectral calculus

Let `X` be coherent, `P` its spectral space with specialization order `≤`, and `A` and `B=A^smile` the localic specialization subrelation and its converse. These are represented by patch-closed order relations; ordinary points of `I` and `D` have a common upper and common lower bound respectively.

| ID | Theorem / statement | Status | Dependencies / caution |
|---|---|---|---|
| C1p | On spectral **ordinary points**, `pt(I)=A_pt B_pt` and `pt(D)=B_pt A_pt` (with `A_pt` specialization) | E | Patch compactness, finite-intersection property, common upper/lower bounds |
| C1l | For the **localic specialization sublocales** `A,B`, `I=A∘B` and `D=B∘A` | I | Introduced as localic image formulas later than the October coherent blind audit; candidate compact-generator quotient proof given in P3a below; image verification via P4 still deserves targeted check |
| C2 | `U=I∘I=cl(D)=W` | E | Independent coherent audits; repaired invalid inference from spatial source to points of an image |
| C3 | `V=D∘D=fit(I)` | E* | Referee's **new** §3.5 argument; compact-open-filter quotient, spatiality of the composable-pair sublocale, and actual image identification; not present as a proved identity in the original packet |
| C4 | `I=U ⇔ I` fitted `⇔ I` internally transitive `⇔ K(L)` conormal | E | Coherent ordered-spectral criterion; established conormality terminology |
| C5 | `D=U ⇔ D` closed `⇔ D` internally transitive `⇔ K(L)` normal | E | Coherent spectral and point-free compact-normality arguments |
| C6p | Hochster reversal exchanges the **point relations** and the coherent normal/conormal equality classes | E | Directly covered by October coherent independent audit |
| C6l | Full named spectral-**sublocale** Hochster identifications for `I,D,U,V` (with the induced dual spectral topologies) | I | Later synthesis (23 Oct), relying on the compact-fitted/filter representation; no duality of the entire lattice of sublocales |
| C7 | `H` has a patch-closed comparability-saturated interpretation, and `H` internally transitive iff `H=F` | E | Post-V independent referee and Priestley compact-open filters |
| C8p | Two-idempotent / alternating-word formulas for **ordinary poset relations** | I | Elementary algebra of two reflexive transitive relations; direct finite checks |
| C8l | Their full coherent **localic** lift and associativity of patch-closed/proconstructible relation composition | I | Targeted internal Nov 7 categorical repair, not independently audited as a package |

Here **E\*** flags a result proved by the external referee beyond the original packet's requested theorem list, rather than independently confirming a previously complete source proof. This distinction is recorded for provenance, not to suggest a known gap.

**Sources:** [coherent audit reconciliation](https://github.com/mkkinyon/locales/blob/main/A-coherent-external-audits-reconciliation-2026-10-21.md), [coherent dualities](https://github.com/mkkinyon/locales/blob/main/A-coherent-dual-characterizations-2026-10-21.md), [Hochster spectral relations](https://github.com/mkkinyon/locales/blob/main/A-V-Hochster-duality-spectral-relations-2026-10-23.md), [two-idempotent calculus](https://github.com/mkkinyon/locales/blob/main/A-relational-composition-mixed-products-coherent-2026-11-06.md).

## III. Strictness, hulls, and constructions

| ID | Statement | Status | Dependencies / caution |
|---|---|---|---|
| X1 | Finite-poset examples realize `I⊊U⊊F`, `I` incomparable with `D`, and `U` incomparable with `V` | E | Explicit finite Alexandrov/spectral relation calculations |
| X2 | There are pointless strictness witnesses, e.g. finite poset times the locale of an atomless complete Boolean frame | E | Generalized-point tests rather than ordinary vertices |
| X3 | Post-V upper diamond: `W∨V<H` possible even coherently; `U∨V` and `H` need not be ordered outside coherence | E | Two-ray Priestley example and compact scattered T1 example |
| X4 | Post-V lower diamond: `T(J)<U∧V` is possible even compactly; **in this example `J=T(J)`** | E | Three-boundary-point example: `Δ<D=M<I=J=W=T(J)<U=V=H=F`; external referee |
| X5 | Iteration of the formal closed-and-fitted hull can first stabilize at `ω+m` for every finite `m≥1` | E | Referee-verified construction; further ordinal development intentionally deferred |
| X6 | Unbounded finite separation-tree ranks and an exact rank-ω two-rectangle bar | E* | Iterated asymmetric K-fans; independently reviewed as input to the negative finite-exhaustion theorem; high rank alone is not sublocale strictness |
| X6a | Strict fitted stages `V₂⊋V₃` and `V₃⊋V₄` | I / E* | Rational bridge graph-density witness; two-level bridge second theorem independently checked with construction repairs |
| X6b | **`V⊊V_fin`** even for countable first-countable T1 spaces; sharpened to sober T0 example | E / I (referee-informed) | Cofinite-sheet T1 version blind audited; two-generic-point sober T0 simplification checked in reconciliation; do not assume product spatiality |
| X7 | `W=cl(D)` may differ from `U` outside coherence | E | Noncoherent hull examples and post-V audit |

**Sources:** [post-V reconciliation](https://github.com/mkkinyon/locales/blob/main/A-postV-external-audit-reconciliation-2026-10-24.md), [rank hierarchy](https://github.com/mkkinyon/locales/blob/main/A-V-strict-V2-V3-fitted-rank-hierarchy-2026-10-23.md).

## IV. Arbitrary-locale classification and closure/fitting

This section is divided into three families because their degree of structural classification is **not** the same. Full proof and audit qualifications are in the companion [arbitrary-locale classification audit](ProjectA_arbitrary_locale_classification_audit_2026-11-07.md) (conversation artifact, not yet in GitHub).

### IV.A. Equality `I=U`: an orthogonality completion problem

| ID | Statement | Status | Dependencies / caution |
|---|---|---|---|
| K1a | `I=U` iff the complete binary orthogonality generated by far pairs is meet-zero disjointness; equivalently its unary polar `a↦a^◇` equals `a*` | I (foundational algebra audited in part) | Standard cp-ideal presentation of `L⊕L`, not a simple pre-existing elementwise axiom; distinguish from stronger “every disjoint pair is far” |
| K1b | `I=U` is inherited by open sublocales but **not** by arbitrary closed sublocales | E | Frame restriction proof and `Spec k[x,y]` versus `V(xy)` finite-compact witness |
| K1c | `I=U` is preserved by **arbitrary** frame coproducts and frame products | E with repaired prerequisite | Infinite-family basic-meet zero detection requires explicit finite-support cp-ideal presentation; frame products use extensivity of locale coproducts |
| K1d | `I=U` fails under general frame subframes and surjective frame quotients | E | Finite poset and adjoining a greatest point |
| K1e | Algebraic frame criterion via disjoint **compact** elements; coherent criterion `K(L)` conormal (mp orientation) | E | Compact pure rectangles, finite far-rectangle lemma, normal/conormal naming caveat |
| K1f | In a frame–coframe, `I=U` iff the frame is extremally disconnected; includes infinite Alexandrov spaces | E | Arbitrary-join distributivity in both lattice directions; rechecked in 21 October foundational audit |
| K1g | For arbitrary continuous (locally compact sober) frames, `I=U` **does not imply** `U=F` | E / I for strengthened models | Deleted-Tychonoff-plank two-tag/cofinite-cloud family; use final audited model, not obsolete “open” headers |
| K1h | Direct formula for the polarity, necessity of far-grid refinement, and possible transfinite closure ranks | O | No new search initiated; possible proximity/nearness literature overlap |

### IV.B. Equality `D=U`: all-cover criterion and compact normality

| ID | Statement | Status | Dependencies / caution |
|---|---|---|---|
| K2a | All-frame criterion: `D=U` iff `d_U∨w_C=1` for **every** open cover `C`, with `w_C=∨_{c∈C}c⊠c` | E | Fitted diagonal represented by square opens of covers; **not** merely a pointwise criterion |
| K2b | For **compact** frames, `D=U` iff frame normal; then `U=F` | E (referee-derived) | Compactness of 1 and `1_{L⊕L}`, finite rectangle lemma; Urysohn lemma for the final functional equality |
| K2c | For **coherent** frames, `D=U` iff `K(L)` is normal (pm orientation) | E | Consequence of compact normality; dual to K1e |
| K2d | `D=U` passes to **closed** sublocales but not general open sublocales | E (referee-derived) | Closed restriction of fitted diagonal and U; finite open-subspace counterexample |
| K2e | Classical continuous **normal** frames satisfy `D=U=F`; arbitrary noncompact **normal ⇒ D=U** | I for positive / **O** unrestricted | Continuous proof uses locally compact sober product; finite-cover shrinking does not handle arbitrary infinite covers |
| K2f | `D=U ⇒ U` internally transitive/equivalence, for arbitrary frames | O | True in compact and classically continuous classes; a putative universal `I U` absorption proof was withdrawn |
| K2g | Preservation of `D=U` under unrestricted arbitrary frame coproducts | O | Positive coherent arbitrary coproduct and continuous finite-coproduct results, with spectral/local-compactness dependencies |
| K2h | `D=U ⇒ U=F` is **false** without compactness; `D=U` need not imply frame normality noncompactly | E / standard regular examples | Distinguish this disproved implication from K2e and K2f |

### IV.C. Equality `W=U`: infinitary diagonal-neighborhood density

| ID | Statement | Status | Dependencies / caution |
|---|---|---|---|
| K3a | For `B={w∈Q:δ*w=1}`, `d_U=∨_{w∈B}w*`; `U=∧_{w∈B}cl O(w)` | E | Point-free diagonal-cover calculation; not arbitrary commutation of closure with meets |
| K3b | `W=U` iff `Φ(d_U)=d_U`, where `Φ(q)=∨_{w∈B}(w→q)`; equivalently each diagonal neighborhood is dense in `U` | E | `Φ` pre-nucleus, standard APP `κ_L` connection, Isbell least dense sublocale |
| K3c | Binary neighborhoods generate `U` as an intersection of **closures** in every frame; for compact frames they also generate `D` as an intersection of **opens** | E | Finite-cut identity; do not omit the compactness assumption in the second assertion |
| K3d | Compact `W=U` iff every binary square neighborhood `v(a,b)` is dense in `U` (`v(a,b)→d_U=d_U`) | E | Contrasts compact `D=U` iff `v(a,b)∨d_U=1` (total coverage) |
| K3e | `D₂` is the finite-cover fitted hull, `W₂=cl(D₂)`, and `W₂=U` iff `Φ₂(d_U)=d_U` | E | Finite-cover filter and pre-nucleus, independently reviewed |
| K3f | General `W₂=U ⇒ W=U` and stronger `W₂=W` | **O** | `D₂>D` does not force `W₂>W`; no accepted `W<W₂` example |
| K3g | `W=U` coherent but can fail compactly outside coherence; corrected two-apex model has `I<W=W₂<U` | E / I for post-referee refinement | Two-apex space is **compact** (not noncompact); external referee's false hyperconnected-rectangle claim excluded |

**Universal comparison:** `D=U ⇒ W=U`, but its converse fails even for finite coherent locales. The all-frame `I=U` and `D=U` conditions are mutually independent. Beyond coherence, `W` need not equal `U`, so no unqualified `U=cl(D)` claim should appear elsewhere.

**Sources:** [structural I/U study](https://github.com/mkkinyon/locales/blob/main/A-I-equals-U-structural-study.md), [arbitrary I/U coproduct proof](https://github.com/mkkinyon/locales/blob/main/A-coproduct-preservation-I-U.md), [D/U covers](https://github.com/mkkinyon/locales/blob/main/A-D-equals-U-first-results-2026-10-21.md), [noncompact normality](https://github.com/mkkinyon/locales/blob/main/A-noncompact-normality-D-U-2026-10-21.md), [W/U nucleus criterion](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-nucleus-criterion-2026-10-24.md), [W/U binary criterion](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-binary-cover-reduction-2026-10-24.md), [October 21 audit reconciliation](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md), [October 24 W/U reconciliation](https://github.com/mkkinyon/locales/blob/main/A-WU-external-audit-reconciliation-2026-10-24.md).

## V. Localic relational composition

| ID | Statement | Status | Dependencies / caution |
|---|---|---|---|
| R1 | Universal `I∘D≤U` (and converse-symmetric `D∘I≤U`) | E | Direct generalized-point/far-rectangle proof; independent negative-theorem audit |
| R2 | A **spatial** locale `X` exists with `I∘D⊈V`; likewise `D∘I⊈V`, `D∘D⊈D` in the transfer example | E | Arrieta's published spatial strongly Hausdorff non-F-separated base and explicit Banaschewski/Sierpiński extension maps |
| R3 | For a strongly Hausdorff base `Y`, F-separatedness characterized by every singly generated extension satisfying `I D≤V` or transitivity of `D` | I (referee-informed) | Referee flagged a missing kernel-pair/common-specialization argument; proof repaired in Nov 7 reconciliation, but the repaired statement was not itself independently re-refereed |
| R4 | Localic-image relation composition is not associative in general, even among endorelations of one locale and (by a separate construction) for a symmetric reflexive endorelation | I | Explicit failure of pullback-stable surjections; **not** a claim about named `I,D` |
| R5 | Special proconstructible / coherent relations have associative composition | I/W | Spectral image/pullback stability; focused external categorical audit not yet performed |
| R6 | For Arrieta's spatial strongly Hausdorff **base `Y`**, `D_Y∘D_Y⊈D_Y` | **E** | Explicit Boolean-valued Cantor-coordinate permutation triple; independently checked by Claude Fable 5.1, High, 7 Nov; this is the same base `Y` used for transfer `X_u` in R2 |
| R6a | For Arrieta's `Y=V⊔N`, `D_Y=A∨Δ_N` and `D_Y` cube associativity iff `A` cube associativity | **E** | Open/closed block calculation, with correct closed-pullback proof of zero mixed fibers; not needed for the nontransitivity implication |
| R6b | Permutation-pair criterion, diameter-two Boolean permutation family, singleton ordinary fibers of bracketed powers, discrete-refinement instability | **E (exact packet scope)** | External referee verified the stated results; does **not** prove failure of the specific cube base change or openness/properness of all projections |
| R7 | In the Sierpiński-transfer family, seven of eight parenthesized three-letter `I,D` words associate | I | Open/stable base-change and kernel-pair calculations; `DDD` exception |
| R8 | Is `(D_Y∘D_Y)∘D_Y = D_Y∘(D_Y∘D_Y)` for Arrieta's base? | **O** | External referee independently confirmed the reduction to `A` and did **not** settle the equality; exact cube congruence criterion remains a restatement, not a proof |

The external referee has **completed** the focused review of R6 and R6a–R6b; **R8 remains open** and R3/R7 were not in that packet. For general locales, formerly unparenthesized distributor identities should be considered *unproved* unless separately derived without associative rewrites. The 7 November mixed-composition proof remains sound independently of this issue.

**Sources:** [mixed composition reconciliation](https://github.com/mkkinyon/locales/blob/main/A-mixed-composition-external-audit-reconciliation-2026-11-07.md), [associativity counterexample and coherent repair](https://github.com/mkkinyon/locales/blob/main/A-relational-composition-associativity-audit-I-2026-11-07.md), [Arrieta Boolean witness and cube criterion](https://github.com/mkkinyon/locales/blob/main/A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md).

## VI. Dependency graph (schematic)

```
Frame coproduct, diagonal, closure, fitting
  ├─ F1–F9: universal hierarchy and hulls
  ├─ K1a–K1h: I=U orthogonality, classes and preservation
  ├─ K2a–K2h: D=U cover criterion, compact normality, hereditary and open questions
  ├─ K3a–K3g: W=U pre-nucleus, binary tests, W₂ questions
  └─ open-cover criterion for D
       ├─ finite-poset D examples
       └─ published non-F-separated Y
            ├─ R2: independently audited transfer theorem; R3: repaired characterization
            └─ explicit Boolean permutation model → R6 (externally verified)
                                                     └─ R8 (OPEN)

Coherent frame / compact opens / patch spectral order
  ├─ C1p–C6l: point formulas, localic lifts, normal/conormal criteria
  ├─ C7 and X3–X5: H/hull theory and counterexamples
  └─ spectral image stability → C1l/C8l/R5 (internally checked)

Localic images and pullback-surjection stability
  ├─ R4: general nonassociativity
  ├─ R5/R7: safe special cases
  └─ R8: exact threefold problem remains open
```

## VII. Immediate proof audits / editorial actions

1. Complete the focused **localic** proof check for C1l and C8l, and adopt the referee's compact-open-filter proof of C3 with its exact hypotheses. Preserve C1p/C6p separately from their localic lifts.
2. Produce a compact standalone foundational proof chapter for F1–F9, with original citations for the fitted diagonal, the completely regular reflection and the Urysohn lemma.
3. **Completed in §XII:** track certificate rank, strict fitted stages, and `V⊊V_fin` separately. Use the canonical K-fan/generic-point transfer and bridge proofs, not the historical search order.
4. Mark every three-factor localic composition identity with parentheses, and distinguish honest path sources from images of intermediate images.
5. The November 7 external referee completed the narrow R6 audit; retain the separate status of cube associativity R8 and of unaudited R3/R7 transfer claims.
6. Keep a separate *priority/literature* ledger. No theorem becomes novel merely because it passed a correctness audit.

**Editorial policy:** do not delete or rewrite blind external reports; record reconciliations in separate files. This inventory has not been committed to GitHub.


## VIII. Focused audit of the coherent proof architecture (version 0.2)

This section separates **point-set identification** from **actual equality of sublocales**. It is a source-and-proof audit, not a new independent expert refereeing.

### Lemmas on which the localic calculus rests

**P1. Spectral ambient products.** When `X=Spec(K)` is spectral, `X²` and `X³` as localic products are the ordinary spectral finite products. Their patch spaces are compact Hausdorff, and specialization is coordinatewise. **Source:** October 21 external coherent report, Lemma 2.1.

**P2. Fitted compact-open filter lemma.** Given a filter `G` of compact opens in a coherent frame `O(Z)=Idl(B)`, the meet `⋂_{g∈G} O(g)` is the quotient `Idl(B/θ_G)` where `b θ_G c` iff `b∧g=c∧g` for some `g∈G`. It is therefore coherent and spatial (under the classical prime-ideal theorem). Its point set is exactly the intersection of the underlying compact opens. **Source:** October 21 external coherent report, Lemma 2.2; independently reconstructed in October 24 post-V referee report.

**Important limitation:** *Arbitrary* fitted sublocales of coherent spaces need not be spatial. We may invoke P2 specifically for diagonal hulls because their neighborhoods can be reduced to a filter of **compact opens**.

**P3. Point description.** For ordinary spectral points `x,y`,
`x I y` iff they have a common upper specialization bound, and
`x D y` iff they have a common lower bound. The point sets are patch closed. The corresponding expressions for `U,V` are the two alternating paths of length four. **Source:** October 21 external coherent report and October 23 Hochster note.

**P3a. A compact-generator presentation of the specialization sublocale (focused internal proof).** Let `X` be coherent, `K=K(O(X))`, `Q=O(X²)=Idl(B)` with `B=K(Q)`. The specialization sublocale `A` is defined by imposing `a₁≤a₂` for all `a∈O(X)` on generalized points. Because every `a` is a join of compact elements, it is enough to impose `k₁≤k₂` for `k∈K`; these elements belong to `B`. Let `θ` be the bounded-distributive-lattice congruence on `B` generated by the equations `k₁=k₁∧k₂` for `k∈K`. Any frame homomorphism `Q→N` is uniquely determined by its bounded-lattice restriction to `B` (ideal-completion adjunction). It factors through `Idl(B/θ)` exactly when all these inequalities hold. Hence the **classifying quotient** of `A` is `Idl(B/θ)`: in particular `A` is coherent and spatial, with the patch-closed point set `{(x,y):x≤y}`. Reversing the equations similarly presents `B=A^smile`. This argument is a new **internal synthesis** from the existing frame presentation and the standard ideal-completion adjunction; it has not been sent to a referee. It reduces C1l's remaining dependency to the appropriate spectral fiber-product/image theorem P4 rather than an unproved assertion that `A,B` are proconstructible.

**P4. Coherent images and pullbacks.** The appropriate *proconstructible* subspaces are patch closed and spectral. Their finite spectral fiber products are the pointwise fiber products. The image under a spectral projection of a patch-closed subset of a finite patch product is patch closed. Its map onto the image is surjective on points, hence a locale surjection because the **image is a spatial spectral sublocale**. This yields localic image = pointwise composite for this class and associativity of its finite relational compositions. **Source:** November 7 associativity audit I, §3. This is an **internally checked repair**, not part of the October 21 original packet. Outside this spectral/proconstructible class, localic relational images need not associate.

**P5. Do not use the discarded inference.** A closed localic image of a spatial source need **not** have exactly the image points. The October 21 referee's `Spec ℤ` example makes this explicit. For `I∘I` we instead use P4, or directly establish the image is closed, contains every `U`-point, and lies in `U`.

### Theorem-by-theorem dependency ledger

| Claim | Point argument | Additional localic argument | Audit disposition |
|---|---|---|---|
| C1p | Common upper/lower bounds in a spectral order | None (point statement) | Confirmed from audited sources |
| C1l | `AB`, `BA` have those same point sets | Use proposed compact-generator quotient presentation **P3a** for `A,B`, then P4 | Internally supported; targeted audit still appropriate |
| C2 | `pt(U)=pt(I²)=cl(pt(D))` | Closedness of image and spatial closed sublocales; avoid discarded inference | Independent referee approved with repair |
| C3 | `pt(V)=pt(D²)=↑pt(I)` | P2 for `D,V` and composable-pair sublocale, plus image lemma P4 | External referee supplied complete proof; preserve its provenance |
| C4 | Order-theoretic transitivity/fittedness | C2–C3 identify internal transitivity and point transitivity | Independent referee approved |
| C5 | Dual normality argument | C2–C3 and compact normality theorem | Independent referee approved |
| C6p | Reverse the specialization order | None (point/equality-class statement) | Independently checked |
| C6l | Named localic sublocales on both Hochster sides | P2 and induced spectral topologies; not a literal equality of original sublocale lattices | Internally supported, later synthesis |
| C7 | Patch-closed comparability saturation | Priestley filters P2 and closed quotient arguments | October 24 external referee approved |
| C8p | Two reflexive transitive order relations simplify alternating words | None | Elementary finite-relation calculation |
| C8l | Words and finite `H`-stages as localic composites | P4 (all relevant relations must be proconstructible) | Internal categorical proof; targeted external review useful |

### What this audit changes and does not change

1. **C1 was oversold in v0.1:** October external checks covered the spectral point formulas; localic `I=AB`, `D=BA` were not separately refereed as such. P3a supplies an internal compact-element presentation of `A,B`, but does not change the provenance of the external audit.
2. **C3 remains substantially supported:** its exact localic result was proved **by the external referee** as a correction to the packet, with an explicit compact-open-filter proof. That provenance is different from externally checking an author's already finished proof.
3. **C6 needs splitting:** equality-class Hochster duality was independently audited; the full named-sublocale identifications were synthesized later.
4. **C8 needs splitting:** ordinary order algebra is elementary, whereas equality of localic images and associativity rests on P4.
5. **X4 was misstated:** the compact example has `J=T(J)`; the strictness shown is `T(J)<U∧V`.
6. **R6 was misdescribed:** Arrieta's `Y` is the same base used for the independently audited Sierpiński-transfer example `X_u`.
7. **R3 confidence has been narrowed:** the independent report found an essential proof omission and the repository supplied a repair afterward. The repaired proof should be independently checked before an unqualified E label.

**Superseded by the 7 November external report:** R6 is now independently verified; the cube associativity question remains open (R8).

## IX. Dormant conceptual observation: a possible dual of U

**Recorded 7 November 2026; no theorem, no search agenda.** The genuine formal closure/fitting pair is `W=cl(D)` and `V=fit(I)`. Since `W≤U` can be strict, it is natural to ask whether some intrinsic as-yet-unknown relation could stand above `V` in a relationship dual to `W≤U`. It could conceivably be more appropriate than `V` for some mixed-composition bounds. Neither existence nor any useful definition is asserted; no notation is adopted and investigation is explicitly **deferred**. This is conceptual context, not a new theorem or conjecture.


## X. External associative/nontransitivity audit received (7 November 2026)

The independent referee (Claude Fable 5.1, High effort) verified the explicit nontransitivity theorem on Arrieta's **strongly Hausdorff spatial base** itself, the exact `D_Y=A∨Δ_N` decomposition and cube reduction, Boolean permutation test, all-cover witnesses, and the specialized point-fiber and discrete-refinement statements. Details and **separately assessed** new ideas are in [reconciliation note](ProjectA_associativity_referee_reconciliation_2026-11-07.md) (conversation artifact; not yet uploaded to repository). Neither cube associativity, the separate Sierpiński transfer proof, the seven-of-eight-word argument, nor the arbitrary endorelation nonassociativity example was checked in this packet.

The referee also suggests `A=Δ_V∨G` with a dense, pointless, symmetric fitted `G`, a Boolean-valued sequence interpretation, and a compatibility bound for `G²`. These are **new referee-derived working contributions**, not independently confirmed results of the original blind packet. A phrase invoking **complete distributivity** of `RO(V)` must be replaced by weaker valid distributive laws: atomless complete Boolean algebras are not completely distributive. Preserve this warning in any future use of the sequence model.

## XI. Arbitrary-locale classification audit incorporated (7 November 2026)

The expanded K rows in §IV are based on a standalone **source-and-dependency review**, not a new external referee. Its file is `ProjectA_arbitrary_locale_classification_audit_2026-11-07.md` in the conversation artifacts. The chief distinctions established by this audit are:

1. `I=U` has a nontrivial **complete orthogonality** criterion and broad closure properties; coherent conormality is a recognized subclass, not the arbitrary-frame definition.
2. `D=U` has an exact **all-cover** condition and a **compact normality** theorem; arbitrary noncompact normality, internal transitivity, and coproduct preservation cannot be promoted from coherent evidence.
3. `W=U` has a nontrivial **fixed-point/density** test; the compact binary version and the general finite-cover `Φ₂` calculus are distinct, and `W₂=U ⇒ W=U` remains open.
4. The repaired October 21 and October 24 referee findings are the sources of truth for infinite-family coproduct zero detection, the withdrawn absorption proof, the false hyperconnected-rectangle criterion, and the corrected **compact** two-apex example.

**The finite-rank/`V` task is now addressed by the appended §XII and its standalone source audit.**


## XII. Consolidation of the V program (8 November 2026)

**Full proof-dependency report:** [Project A — V consolidation and audit](ProjectA_V_consolidation_2026-11-08.md) (conversation artifact; not yet uploaded to GitHub). This section records the main outcomes and corrects X6's prior conflation of tree ranks and strict fitted sublocales.

### XII.A. Motivation: two distinct duality problems

The literal closure/fitting companions are `W=cl(D)` and `V=fit(I)`; `W≤U` may be strict outside coherence. The Session 3 search for a formula for `V` was partly attempting to characterize the relation *really dual to U*. These are not the same goal. The possible existence of another relation above `V`, analogous to `W≤U`, is **dormant** and must not be adopted as a conjectured construction or used to alter the existing mixed-composition theorems.

### XII.B. Theorem clusters

| ID | Result | Status | Principal dependency / distinction |
|---|---|---|---|
| V1 | C-ideal / well-founded alternating separation-tree calculus computes **all** bars | I | Exact presentation of `fit(I)`, formally complete but not a non-tautological alternative dual |
| V2 | Coherent dual-far strips generate `V` | I/E* | Spectral compact-open filters; full localic Hochster duality requires its own scope |
| V3 | Dual-far strips insufficient for arbitrary locales | **E** | External October 22 rational graph residual audit; avoid historical symbol `W` for strip approximation |
| V4 | Uniform rank bounds: compact and regular `≤2`; continuous/algebraic `≤3`; Scott continuous dcpos `≤2` | I | Different hypotheses and direct rank normalization proofs; not jointly blind-audited |
| V5 | Unbounded exact finite bar ranks and an exact rank-ω strip bar | E* | Asymmetric K-fans; strict rank alone does **not** imply strict `V_n` |
| V6 | `V₂⊋V₃` on rational bridge | I | Graph-density fixed-point certificate, stronger than `rk(q)=3` |
| V7 | `V₃⊋V₄` on two-level bridge | E* | Independent blind audit, construction/tail and tree-quantifier repairs required |
| V8 | `V⊊V_fin` in countable first-countable T1 non-Hausdorff example | **E** | External blind audit of cofinite-sheet graph transfer and original fan input |
| V9 | Countable first-countable **sober T0**, non-T1, two-generic-point example also has `V⊊V_fin` | I (referee-informed) | Referee suggested simplification; checked in reconciliation; ordinary point witness, no ambient-square spatiality |
| V10 | `I≤V≤V₂≤C(d₂)≤F` and `U≤C(d₂)`, while `U` and `V` incomparable | I (finite witnesses E) | Two-step rather-below apartness; corrects blind report's wrong `V≤U` claim |
| V11 | Arbitrary-frame closedness of `V` and fitting of `I` have exact semiclosed/supplement-filter tests | I | Uses `k=j_V(0)`, `F_d={w:d∨w=1}`; neither a simple dual definition nor a new published operator |
| V12 | Almost-normal `⇒ V₂=U=F`, not necessarily `V=F`; almost normal+subfit `⇒ I=V=U=F` | I | Internal proofs + published Picado–Pultr subfit lemma; distinct hypotheses |
| V13 | Noncompact almost-normal `V` can be nonclosed and below `U=F` | E* | Thickened-zigzag external post-V check; earlier unsupported `I<V` for a *different* example remains retracted |
| V14 | Regular filter completion can recover all bars in the **specific** generic-point negative example | I | Does not settle arbitrary-frame regular completion or supply a new intrinsic formula |

### XII.C. The decisive negative theorem: exact dependency chain

`standard rectangular C-ideal` → `separation-tree completeness` → `asymmetric K-fan strips with unbounded finite rank` → `rank-ω strip on clopen sum Y` → **`generic-point or cofinite-sheet transfer` (not another clopen disjoint sum)** → `every finite bar fails to exclude a fixed point or graph residual` → **`V⊊V_fin`**.

Simply constructing a bar of rank `m+1` after one of rank `m` is a different theorem. A countable clopen sum with arbitrarily high-rank individual bars can nevertheless satisfy `V₂=V`. In the negative exhaustion theorem the non-clopen transfer step is essential.

### XII.D. Preserved corrections and deferred directions

- Do not infer `I⊊V` from `V⊊V₂` or high bar ranks. The Fable October 23 report's extra strictness was not established for its particular example.
- Do not infer `V≤U`: the unconditional comparisons are `V≤C(d₂)` and `U≤C(d₂)`, with finite spectral examples of incomparability.
- The all-trees presentation rewrites the neighborhood condition in coordinates; it is **not** a proven intrinsic counterpart of the far-rectangle formula for `U`.
- Keep blind reports unchanged. Distinguish the externally audited **T1 cofinite-sheet** theorem from the internally reconciled **sober T0 generic-point** proof.
- **Defer** further rank escalation and the hypothetical relation above `V`. The regular-filter calculations are not a general positive formula.

**Source policy:** Detailed source links and repairs appear in the standalone consolidation document. Neither that artifact nor this inventory has been committed to GitHub.


## XIII. Formal hull, functional reflection, and preservation audit (8 November 2026)

**Full source-and-proof ledger:** [cross-cutting hull and preservation report](ProjectA_crosscutting_hulls_preservation_audit_2026-11-08.md) (conversation artifact, not yet in GitHub). In the classification below, I means internally supported, not separately externally verified.

### XIII.A. Principal theorem inventory

| ID | Result | Status | Dependencies / caution |
|---|---|---|---|
| H1 | Universally `T(J)=W∧V`, `W∨V≤H≤F`, and the cross-hull absorption formulas | **E** | October 24 external referee; fitting preserves finite sublocale joins via coframe law |
| H2 | Coherent `H`: least patch-closed coordinatewise comparability-saturated relation; `F`: least patch-closed equivalence extending comparability | **E** | Spectral/Priestley and compact-open-filter spatiality lemma |
| H3 | Coherent `H` internally transitive iff `H=F` | **E** | H2 and point-determination of closed spectral sublocales |
| H4 | `H` need not be transitive, even coherent; `U∨V<H<F` in two convergent zigzag rays | **E** | October 24 independent audit |
| H5 | `κ` transfinite closed/fitted hull iteration computes `H`; exact `ω+m` first stabilization | **E** | Closed hull at limits; never use bare sublocale join instead |
| H6 | `U∨V` and `H` incomparable as universal constructions; `T(J)<U∧V` even compactly | **E** | Compact T1 and compact T0 boundary examples; the compact T0 example has **`J=T(J)`** |
| H7 | Noncoherent scattered `T1` example with `H=I=U<F` and `H` internally transitive | **I** | Post-referee consequence of existing plank/cofinite-cloud and fit-square results; not separately audited |
| N1 | `F=kerpair(r_X)` for the completely regular reflection `r_X:X→X_cr` | **I** (published inputs) | Picado–Pultr VI.2.2 plus categorical factorization proof |
| N2 | `F=Δ` iff `r_X` monic iff `C(L)↪L` a frame epimorphism, **not necessarily an isomorphism** | **I** | Nonregular strongly Hausdorff example and nonsurjective frame epis |
| N3 | All named `I,D,U,F,V,W,M,J,H` satisfy `R_X≤(h×h)^−1R_Y` for locale maps `h` | **I** (new synthesis) | Basic `I,U,F` naturality; pullback preserves closedness/fittedness and hull universal properties |
| N4 | Consequently `R_(X×Y)≤R_X×R_Y` for **every named relation** | **I** (new synthesis) | N3 applied to coordinate projections; not equality in general |
| P1 | Every named relation is diagonal-blockwise under arbitrary locale disjoint unions (frame products) | **I** | Extensivity/clopen block decomposition; F has component-separating real maps |
| P2 | For coherent binary locale products, `I,D,U,V,F` commute with products; also `W=U`, and `M` | **I** | Spectral point product formulas plus spatial named sublocales; 21 Oct operation note, not separately audited as a whole |
| P3 | `J` does **not** commute with binary locale products, even for finite coherent factors | **I** | Three-point upper and lower forks: `J_P= P²`, `J_Q=Q²`, but `J_(P×Q)≠(P×Q)²` |
| P4 | The fixed-point class `J=T(J)` is not closed under binary frame coproducts | **I** | Same two forks; `T(J_(P×Q))=(P×Q)²` |

### XIII.B. Audit boundaries

- The universal **comparison** `R_(X×Y)≤R_X×R_Y` is not a product-preservation **equality**. In particular `J` provides a finite strict counterexample.
- No general product-equality theorem for `H` or `T(J)` is asserted in this inventory. No infinite-product analogue of P2 is claimed.
- The categorical identity `F=kerpair(r_X)` is standard-background dependent; **`F=Δ` does not imply complete regularity** because frame epimorphisms need not be surjective.
- The 24 October post-V referee checked H1–H6. H7 is a new deduction from earlier source results, so it remains I.
- The user's possible additional role for **`V₂`** is noted as **deferred**; the previous §XII gives the actual audited rank results without reopening the topic.

### XIII.C. Completed next inventory target

The properness/effectiveness and Scott-continuity notes are now consolidated in §XIV and in the separate 8 November report. In particular, the obsolete “unresolved” continuous-case status is superseded by the 20 October proof and its 21 October retrospective check. The arbitrary-locale Scott converse remains open.


## XIV. Properness, effectiveness, and Scott-continuity audit (8 November 2026)

**Complete proof and source ledger:** [properness/effectiveness/Scott-continuity audit](ProjectA_properness_effectiveness_Scott_audit_2026-11-08.md) (conversation artifact, not yet uploaded to repository). This segment identifies **published sources**, **previous external audit**, **internally checked proof**, and **remaining unknown** separately. “Externally checked” does not mean this entire consolidated section was newly blind-refereed.

### XIV.A. Theorem and dependency entries

| ID | Exact statement | Scope | Status | Primary dependency / caution |
|---|---|---|---|---|
| Q1 | Every closed **proper** internal equivalence relation is **effective**; the quotient is proper | All locales | **Published** | Vermeulen 1994, Cor. 5.17 and Prop. 5.5; Manuell 2023, Remark 3.8. **No ambient compactness hypothesis.** |
| Q2 | `I∘I≤U`; hence `I=U` makes `I` an internal equivalence relation | All locales | **I/E (previous foundational audit)** | Direct three-coordinate frame computation; no associativity assumption |
| Q3 | For proper closed equivalence `E`, `r_E=p₂* p₁^*=q^*q_*`, idempotent and Scott-continuous | All locales | **Published + E** | Vermeulen Lemma 5.2/Prop. 5.5; requires proper projections, not just equivalence |
| Q4 | `r_E` is deflationary, finite-meet preserving; its fixed points are the `E`-invariant opens for reflexive symmetric `E` | All locales | **E** | Adjunction, symmetry, reflexivity; no idempotence asserted |
| Q5 | `I=U=F` does **not** force idempotence of `r_I` or Scott continuity, even with finite classes | Countable strongly locally compact sober algebraic example | **E** | Two-point-pair classes `{a,b}`, `{c_n,d_n}`; `r_I(u)={b}`, `r_I²(u)=0`; quotient not closed |
| Q6 | If `E⊆X×Y` is **closed**, and `X` is **weakly locally compact** topological, then `r_E` Scott-continuous **iff** `p_Y` is a **perfect topological map** | Ordinary topological spaces | **I** | Finite compact-support cover and tube lemma; no equivalence, sobriety, or Hausdorff assumption |
| Q7 | If `O(X)` is **classically continuous**, a closed localic `E↪X²` has `r_E` Scott-continuous **iff** `p₂:E→X` is **proper in Loc** | Continuous locales, ZFC | **I** | Q6, Hofmann–Lawson spatial/local-compact representation, product comparison and closed Frobenius |
| Q8 | For continuous `X`, if `I` is internally transitive and its projections are proper (or `I=U` and `r_I` is Scott), then `I=U=F`; its quotient is the completely regular reflection | Continuous locales, ZFC | **E/I (audited corollary)** | Vermeulen effectivity + proper quotient, quotient continuity and strong Hausdorffness, Hofmann–Lawson |
| Q9 | For compact `X`, internal transitivity of `I` **iff** `I=U` **iff** `I=U=F` | All compact locales, including pointless | **E/I (published inputs)** | Closed `I` projections proper automatically, Vermeulen 5.17, **Picado–Pultr–Tozzi §6.4 compact Hausdorff ⇒ regular ⇒ completely regular** |
| Q10 | The arbitrary-locale implication `r_I` Scott-continuous ⇒ `p₂` proper | General possibly noncontinuous locales | **O** | Scalar composite Scott continuity alone does not presently give co-Frobenius or Scott continuity of `p₂*` |
| Q11 | Proper projections of `I` by themselves do **not** force `I=F` in arbitrary locales | Regular non-functionally-Hausdorff space | **I** (new deduction from published examples) | Take `I=U=Δ`, `p_i=id` proper, but `F>Δ`; **effectivity is not the obstruction** |
| Q12 | Closed saturation of an equivalence quotient is strictly stronger than the real-function separation needed for `I=F`; failures of closed saturation have escaping compact witnesses | Ordinary topological class (plus spatial lifts when justified) | **I/E** | Duplicated-points open quotient, cofinite-cloud and paired-point examples; do not elevate all pointwise claims to locales |

### XIV.B. Historical status reconciliation

- The body of [A-scott-continuity-converse-status-2026-10-21.md](https://github.com/mkkinyon/locales/blob/main/A-scott-continuity-converse-status-2026-10-21.md) retains **obsolete “unresolved” statements about continuous locales**, but its opening correction explicitly supersedes them. **Q6–Q7 are internally proved, not open**; they still lack a dedicated new blind external audit. **Q10 remains open.**
- The earlier attempt to restrict Vermeulen 5.17 to compact locales is withdrawn. Distinguish Cor. 5.14 (weakly fitted) from Cor. 5.17 (closed proper).
- The **false** assertion “internal equivalence ⇒ `r_E` idempotent” is withdrawn; **Q5** is the canonical counterexample and **Q3** is the correct sufficient hypothesis.
- The former outstanding citation “compact strong Hausdorff ⇒ completely regular” can now be located specifically at **Picado–Pultr–Tozzi, chapter II §6.4**, which proves compact closed-diagonal Hausdorff ⇒ regular; §4.8 implies complete regularity. This validates the published input required for Q9. A precise bibliographic edition/page belongs in a final manuscript.
- **Q11 is logically separate from Q10:** regular non-functionally-Hausdorff spaces show that effectivity and properness are **not enough** for `I=F` without extra hypotheses, but they do **not** disprove the arbitrary-locale Scott-continuity **converse**.

### XIV.C. Follow-up status and source policy

The foundational properness package is now suitable for the inventory's **settled / working / open** classification. There is no reason to reopen Vermeulen effectivity. A short targeted independent read of the **weak-local-compactness proof** (Q6) and its **continuous-locale transfer** (Q7) would be useful before publication. No claim of new priority is made for Q8/Q9: these are applications of published machinery plus the project's explicit composition inequality.

**Optional future agenda (deferred):** General noncontinuous Scott converse Q10; tests for additional intrinsic hypotheses making effective quotients completely regular. No inference from real-map kernel pairs to arbitrary quotient effectivity should be made without the properness hypotheses.