# Locales and graph-theoretic separation

Research notebook inspired by P. J. Cameron and V. Kumar, *Graphs on topological spaces* ([arXiv:2610.14783](https://arxiv.org/abs/2610.14783)).

**Working research notes, not a referee-checked paper.** Proofs and any potentially new claims require independent mathematical review and a literature/priority check. For Project A, the current theorem status is in the **[consolidated theorem outline](A-consolidated-theorems.md)** rather than the dated historical notes. An external cold referee review has now been received; see the [response and corrected hypotheses](A-referee-response.md).

## Workstreams

| Track | Topic | Status |
|---|---|---|
| **A** | Three closed localic separation relations and equality theory | **Active; consolidated** |
| **B** | Graphs on nonzero elements of frames | [Backlog](B-overlap-graphs.md) |
| **C** | Frame-cover nerves, Dowker duality, homotopy | [Backlog](C-frame-nerves.md) |

## Project A — Start here

- **[Consolidated theorem outline](A-consolidated-theorems.md):** current claims, hypotheses, hierarchy, dependencies, coherent and continuous results.
- **[Independent referee response](A-referee-response.md):** accepted corrections, current scope, and remaining verification tasks.
- **[First-pass proof audit](A-proof-audit.md):** mathematical risks, tests performed, gaps still needing verification. This is an **internal** audit, not independent.
- **[Cold referee review packet](A-cold-review-packet.md):** standalone instructions and sources for an independent reviewer, preferably read **before** the internal audit.
- **[Core separation definitions](A-localic-separation.md)** and **[hierarchy, strictness and pointless examples](A-hierarchy-first-results.md)**.
- **[Equality and completely regular reflection](A-equality-characterizations.md)**.
- **[Coherent frames and conormality](A-coherent-conormality.md)**; **[coherent implication](A-coherent-implication.md)**.
- **[Continuous frame criteria](A-continuous-frames.md)**; **[kω compact exhaustion](A-kw-compact-exhaustion.md)**; **[paracompact extension](A-beyond-countable-exhaustion.md)**.
- **[Deleted Tychonoff plank / two-tag counterexample](A-continuous-counterexample-plank.md)**.
- [Future questions](future-questions.md) contains a deferred research idea.

Additional historical research notes: [reading Picado–Pultr 2021](A-reading-Picado-Pultr-2021.md), [compactness-question exploration](A-continuous-compactness-question.md), [primitive ideal spaces](A-primitive-ideal-spaces.md), [closed saturation](A-closed-saturation.md), [way-below revisited](A-way-below-revisited.md), [stable interpolation test](A-stable-interpolation-test.md), [noncompact intermediate neighborhoods](A-noncompact-intermediate-neighborhoods.md).

## Current central mathematical conclusion (working)

For all locales, definitions give

`Δ_X ⊆ I(X) ⊆ U(X) ⊆ F(X)`.

For coherent frames, `I=U` has a conormal compact-open criterion and implies `U=F`. For locally compact sober spaces, the implication also holds under compactness, σ-compactness/kω or paracompactness. **It fails for arbitrary continuous frames**: the two-tag extension of the deleted Tychonoff plank gives a locally compact sober `X` with `I=U⊊F`. Earlier notes that say the unrestricted implication is "open" are now **historical and superseded**.

## Conventions and prerequisites

A frame is a complete lattice with finite meets distributing over arbitrary joins. Write `L=O(X)`, `L⊗L=O(X×X)` for the **frame coproduct** (localic product), `a⊠b` for an open rectangle, and `a*=a→0` for pseudocomplement. `C(d)` is the closed sublocale complementary to the open `d`. Classical representation of continuous frames by locally compact sober spaces uses choice; pointwise claims lift to **closed localic relations** only with the required localic-product/spatial comparison.

This repository is a developing mathematical notebook; no originality claim has been made for standard background results or for the new connections without a systematic literature review.
