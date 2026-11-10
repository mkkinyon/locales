# Point-Free Topology Project

> **CURRENT STATUS — 10 November 2026 (three independent blind audits).** Former tracks A (separation relations) and C (coherent homotopy) are one program; B is archived. **Start with the [unified index](POINT_FREE_TOPOLOGY_START_HERE.md), [theorem ledger v2.1](PointFree_master_theorem_ledger_v2_1_2026-11-10.md), [open-problem register v1.8](ProjectA_open_problems_register_v1_8_2026-11-10.md), and [thematic guide](POINT_FREE_THEMATIC_GUIDE.md).** The latest audited mathematics A1–E3 is in the [corrected nonconstant-sheaf account](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md); the original [third blind report](audits/2026-11-10/postaudit-sheaf/Referee_report_original.md) and [reconciliation](PointFree_postaudit_sheaf_EXTERNAL_referee_reconciliation_2026-11-10.md) are separate. The earlier [canonical chain/hull account](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md) remains foundational. The referee's new nonabelian full-homotopy counterexample came **after** its audited claims and has been checked internally, not blind-refereed. No complete literature-priority or intrinsic-localic-shape claim is made.

> **HISTORICAL SUBJECT INDEX (9 November):** [Project A entry point](PROJECT_A_START_HERE.md) remains useful for the separation hierarchy, W/Q′/composition, and older canonical proofs. Its dated status is not a second current master. [Previous ledger v1.9](ProjectA_master_theorem_ledger_v1_9_2026-11-09.md) and [previous problem register v1.6](ProjectA_open_problems_register_v1_6_2026-11-09.md) are preserved as snapshots. Q and Q′ remain OPEN and DEFERRED; the 9 November [W-phase reconciliation](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md) stands.

Research notebook inspired by P. J. Cameron and V. Kumar, *Graphs on topological spaces* ([arXiv:2610.14783](https://arxiv.org/abs/2610.14783)).

**Exploratory mathematics, not a submission-ready paper.** The foundational results and two principal counterexamples have now received an internal audit and two external adversarial reviews (20 October 2026). These were **not strictly blind**, and correctness of all peripheral notes and novelty/priority remain open. Start with the **[consolidated theorem outline](A-consolidated-theorems.md)** and the **[external-audit reconciliation](A-external-audits-reconciliation-2026-10-20.md)** rather than treating dated exploratory notes as current status.

> **Research continuity (21 October 2026):** Start with the [research-status index](A-research-status-index.md). It distinguishes audited results, working proofs, open problems, and corrected false leads. See also [closure properties](A-closure-properties-I-U.md), [Scott-continuity converse ledger](A-scott-continuity-converse-status-2026-10-21.md), and [Cornish/minimal-prime literature ledger](A-literature-separation-status-2026-10-21.md).

## One research program, three interlocking themes

| Theme | Primary topics |
|---|---|
| **Separation and relational algebra** | Localic hierarchy, equality theory, proconstructible composition |
| **Higher relations and nerves** | Graph powers of specialization, higher diagonal hulls, simplicial and bisimplicial locales |
| **Point-free homotopy and shape** | Frame-cover nerves, Dowker comparison, descent, refinements |

The former Project A and Project C labels survive only in historical filenames and theorem references. **Project B is archived:** [original overlap-graph notes](B-overlap-graphs.md). For active work use the [unified index](POINT_FREE_TOPOLOGY_START_HERE.md); the [former A index](PROJECT_A_START_HERE.md) is still the detailed navigation authority for the pre-Dowker separation program.

## Project A — Start here

- **[Consolidated theorem outline](A-consolidated-theorems.md):** current statements, verified qualifications, hierarchy, coherent/compact/continuous cases and counterexamples.
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
- **[Subfit arithmetic counterexample](A-subfit-arithmetic-counterexample.md):** a new working proof that subfitness and arithmeticity **together** do not rescue I=U implies U=F; gives the contrasting theorem that sober T1 arithmetic spaces are zero-dimensional.
- **[Nonidempotent inseparability saturation operator](A-saturation-operator-nonidempotence.md):** `r_I²≠r_I` even with `I=U=F`, finite classes, and compact Hausdorff quotient. **Important correction** to earlier unconditional idempotence claims.
- [Obstruction hypotheses](A-obstruction-candidates.md), [proper inseparability relations](A-proper-inseparability-relations.md), [clean Vermeulen effectiveness theorem memo](A-vermeulen-effectiveness-correction.md).

Additional historical research notes: [reading Picado–Pultr](A-reading-Picado-Pultr-2021.md), [compactness exploration](A-continuous-compactness-question.md), [primitive ideal spaces](A-primitive-ideal-spaces.md), [closed saturation](A-closed-saturation.md), [way-below revisited](A-way-below-revisited.md), [stable interpolation](A-stable-interpolation-test.md), and [noncompact intermediate neighborhoods](A-noncompact-intermediate-neighborhoods.md). Some discussions of formerly “open” questions in these files are retained **as historical records**.

[Future questions](future-questions.md) contains other deferred directions.

## Main results at a glance

For every locale X,

`Δ_X ⊆ I(X) ⊆ U(X) ⊆ F(X)`, with `I(X)=cl(Δ_X)` and `I∘I⊆U`.

For **coherent** frames, `I=U` has a conormal compact-open characterization and implies `U=F`. If `I` is an internal equivalence relation on **any compact locale**, classical compact Hausdorff locale theory and Vermeulen's results give `I=U=F`. For **continuous** frames, transitivity of `I` plus **proper localic projections** likewise gives `I=U=F`. However, **continuous, algebraic, subfit or stably continuous frames do not suffice alone**: the deleted-plank constructions give `I=U⊊F` under these individual hypotheses.

The exact frame operator `r_I(u)=(p₂)_*p₁^*(u)` exists generally but is **not generally idempotent**. Properness of the projections makes it idempotent and Scott-continuous; these properties are not themselves equivalent to `I=F`.

## Conventions

A frame is a complete lattice with finite meets distributing over arbitrary joins. Write `L=O(X)`, `L⊗L=O(X×X)` for the **frame coproduct** (localic product), `a⊠b` for a basic rectangle, `a*=a→0` for pseudocomplement, and `C(d)` for the closed sublocale complementary to the open `d`. Classical representation of continuous frames by strongly locally compact sober spaces uses choice. Lifting pointwise equality to equality of **closed localic relations** requires the appropriate product/spatial comparison.

**No originality claim** is made for established background theorems, or for independently obtained uses of classical constructions, absent a further priority study.
