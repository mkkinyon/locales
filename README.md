# Point-Free Topology Project

**Current reading route (Session 11):** Begin with [the adopted two-study proof-guided mathematical account](ProjectA_ENDGAME_TWO_STUDIES_PROOF_GUIDED_ACCOUNT_2026-11-21.md), then [detailed five-example calculations](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md), [notation and exact hypotheses](ProjectA_ENDGAME_NOTATION_AND_ASSUMPTIONS_2026-11-21.md), and the [47-group theorem ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md). The two-study account passed a targeted [internal editorial/proof-interface audit](ProjectA_ENDGAME_TWO_STUDIES_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) with repairs incorporated; it is **not** a formal or human peer-review certificate. The independent MAT*/MUL*/FINMAT* blind technical review is [reconciled here](ProjectA_MATSTAR_MULSTAR_REFEREE_RECONCILIATION_2026-11-21.md). The [first editorial/source-consistency pass](ProjectA_ENDGAME_EDITORIAL_SOURCE_CONSISTENCY_REVIEW_2026-11-21.md) repaired current guidance and bibliography and verified local file references. The [second-pass 47-group provenance review](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md) traced every theorem group to its original report, dated reconciliation, published antecedent or internal source and corrected the evidence grades of A18 and B15. [Historical chronological status banners are preserved verbatim here](ProjectA_ENDGAME_HISTORICAL_STATUS_NOTICES_ARCHIVE_2026-11-21.md) and **must not be read as current verdicts**.

**Motivation:** P. J. Cameron and V. Kumar, [*Graphs on Topological Spaces*](https://arxiv.org/abs/2610.14783). This repository retains the original research chronology, but its [current mathematical account](ProjectA_ENDGAME_TWO_STUDIES_PROOF_GUIDED_ACCOUNT_2026-11-21.md), not the older indexes below, governs today's scope and proof statuses.

## Historical mathematical themes (the current exposition uses two studies)

| Theme | Primary topics |
|---|---|
| **Separation and relational algebra** | Localic hierarchy, equality theory, proconstructible composition |
| **Higher relations and nerves** | Graph powers of specialization, higher diagonal hulls, simplicial and bisimplicial locales |
| **Point-free homotopy and shape** | Frame-cover nerves, Dowker comparison, descent, refinements |

The earlier A/C tracks are now united in the **two-study** exposition; their labels persist in the research-history theorem ledger and filenames. **Project B is archived:** [original overlap-graph notes](B-overlap-graphs.md). For active work use the [current Start Here guide](ProjectA_ENDGAME_START_HERE_2026-11-21.md) and [current 47-group ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md). The [old unified index](POINT_FREE_TOPOLOGY_START_HERE.md) and [former A index](PROJECT_A_START_HERE.md) remain historical navigation aids.

## Earlier Project A library (historical source index)

- **[Early consolidated theorem outline](A-consolidated-theorems.md):** an archival milestone with hierarchy, coherent/compact/continuous cases and counterexamples; its status labels are **superseded by the current 47-group ledger**.
- **[Reconciliation of the two external audits (20 October 2026)](A-external-audits-reconciliation-2026-10-20.md):** ranked corrections, independently checked counterexamples, and remaining verification tasks.
- **[Literature/priority first-pass ledger](A-literature-priority-review.md):** sources, antecedents and priority boundaries; supplemented by the 20 October correction ledger.
- **[Earlier independent referee response](A-referee-response.md)**; **[first-pass internal proof audit](A-proof-audit.md)**; **[cold review packet](A-cold-review-packet.md)**.

### Foundational relations and equality theory

- [Core separation definitions](A-localic-separation.md), [hierarchy and finite/pointless witnesses](A-hierarchy-first-results.md), [equality and completely regular reflection](A-equality-characterizations.md).
- [Coherent frames, compact-open tests and conormality](A-coherent-conormality.md); [coherent implication](A-coherent-implication.md).
- [Continuous frame criteria](A-continuous-frames.md); [compact exhaustion and `k_ω`](A-kw-compact-exhaustion.md); [paracompact extension](A-beyond-countable-exhaustion.md).
- [Fitted diagonal](A-fitted-diagonal.md): the fourth, generally nonclosed localic relation `D=fit(Δ)`; its **original-point** relation is Cameron–Kumar's closure-meeting graph. For non-sober spaces distinguish original points from points of the sobrification.

- **[Structural study of I=U in arbitrary frames](A-I-equals-U-structural-study.md):** one-parameter pseudocomplement criterion; a universal **closure-nonexpansiveness** interpretation; complete binary orthogonality and a unary separation polar; point-free open heredity and failure of closed heredity.

### Counterexamples and the structure of the obstruction

- **[Two-tag deleted-plank construction](A-continuous-counterexample-plank.md):** `I=U⊊F` for an **arithmetic/stably continuous** frame that is not subfit.
- **[T1 algebraic subfit cofinite-cloud construction](A-subfit-continuous-counterexample.md):** `I=U⊊F` despite T1, sobriety, strong local compactness, algebraicity and subfitness; compact-open witnesses and a crowded Cantor-product strengthening.
- **[Scott-continuity converse for closed relations](A-scott-continuity-converse.md):** a new working proof that, for closed relations with weakly locally compact source, Scott continuity of the relation operator is equivalent to topological perfectness of the projection; consequently **properness** of closed relation projections is characterized by Scott continuity for classical continuous frames.
- **[Subfit arithmetic counterexample](A-subfit-arithmetic-counterexample.md):** **new working construction** disproving the **combined** hypothesis subfit + arithmetic + I=U ⇒ U=F, via two cofinite clouds and their sobrification. Includes the complementary positive theorem that sober **T1 arithmetic spaces are zero-dimensional**.
- **[Nonidempotent inseparability saturation operator](A-saturation-operator-nonidempotence.md):** `r_I²≠r_I` even with `I=U=F`, finite classes, and compact Hausdorff quotient. **Important correction** to earlier unconditional idempotence claims.
- [Obstruction hypotheses](A-obstruction-candidates.md), [proper inseparability relations](A-proper-inseparability-relations.md), [clean Vermeulen effectiveness theorem memo](A-vermeulen-effectiveness-correction.md).

Additional historical research notes: [reading Picado–Pultr](A-reading-Picado-Pultr-2021.md), [compactness exploration](A-continuous-compactness-question.md), [primitive ideal spaces](A-primitive-ideal-spaces.md), [closed saturation](A-closed-saturation.md), [way-below revisited](A-way-below-revisited.md), [stable interpolation](A-stable-interpolation-test.md), and [noncompact intermediate neighborhoods](A-noncompact-intermediate-neighborhoods.md). Some discussions of formerly “open” questions in these files are retained **as historical records**.

[Future questions](future-questions.md) contains other deferred directions.

## Selected early separation-hierarchy results (historical snapshot)

For every locale X,

`Δ_X ⊆ I(X) ⊆ U(X) ⊆ F(X)`, with `I(X)=cl(Δ_X)` and `I∘I⊆U`.

For **coherent** frames, `I=U` has a conormal compact-open characterization and implies `U=F`. If `I` is an internal equivalence relation on **any compact locale**, classical compact Hausdorff locale theory and Vermeulen's results give `I=U=F`. For **continuous** frames, transitivity of `I` plus **proper localic projections** likewise gives `I=U=F`. However, **continuous, algebraic, subfit or stably continuous frames do not suffice alone**: the deleted-plank constructions give `I=U⊊F` under these individual hypotheses.

The exact frame operator `r_I(u)=(p₂)_*p₁^*(u)` exists generally but is **not generally idempotent**. Properness of the projections makes it idempotent and Scott-continuous; these properties are not themselves equivalent to `I=F`.

## Conventions

A frame is a complete lattice with finite meets distributing over arbitrary joins. Write `L=O(X)`, `L⊗L=O(X×X)` for the **frame coproduct** (localic product), `a⊠b` for a basic rectangle, `a*=a→0` for pseudocomplement, and `C(d)` for the closed sublocale complementary to the open `d`. Classical representation of continuous frames by strongly locally compact sober spaces uses choice. Lifting pointwise equality to equality of **closed localic relations** requires the appropriate product/spatial comparison.

**No originality claim** is made for established background theorems, or for independently obtained uses of classical constructions, absent a further priority study.
