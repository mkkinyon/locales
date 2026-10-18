# Locales and graph-theoretic separation

Research notebook inspired by P. J. Cameron and V. Kumar, *Graphs on topological spaces* ([arXiv:2610.14783](https://arxiv.org/abs/2610.14783)).

## Workstreams

| Track | Topic | Status | Notes |
| --- | --- | --- | --- |
| **A** | Localic separation relations and the hierarchy | **Active** | [A: separation](A-localic-separation.md) |
| **B** | Graphs on nonzero elements of frames | Backlog | [B: overlap graphs](B-overlap-graphs.md) |
| **C** | Frame-cover nerves, Dowker duality, homotopy | Backlog | [C: nerves](C-frame-nerves.md) |

These are exploratory research notes, **not** a manuscript. Assertions are marked *proved (working)*, *to verify*, or *question*; “proved (working)” means the argument is included here but has not undergone independent referee checking. No originality claim is made without a literature review.

## Compact-open equality tests (new)

[**A: coherent frames and conormality**](A-coherent-conormality.md) develops an algebraic-frame criterion for I=U, identifies the coherent case with conormality of compact opens (and mp-rings for ring spectra), and gives a parallel completely-separated-compact-opens criterion for U=F. See the note for proofs, prerequisites, and the known conormal-lattice literature.

## Coherent implication resolved

[**A: coherent implication**](A-coherent-implication.md) proves I=U ⇒ I=U=F for coherent frames, using the more general compact-space theorem that equality of pointwise inseparability and Urysohn relations forces a compact Hausdorff quotient by the closed inseparability equivalence relation. The note spells out why spectrality allows the inference for closed localic relations.

## Removing compactness (partial)

[A: the continuous compactness question](A-continuous-compactness-question.md) proves the implication without compactness when inseparability is an **open equivalence relation**, and constructs a compact sober counterexample showing openness does **not** follow from I=U. The unrestricted locally compact/continuous-frame implication is **not yet settled**; see the note for the exact obstruction and research leads.

## Continuous-frame extension

[A: Continuous frames and way-below criteria](A-continuous-frames.md) develops relative compactness of way-below rectangles and necessary-and-sufficient pairwise tests for both equalities. It also extends the coherent I=U ⇒ U=F implication to compact continuous frames and gives a nonalgebraic locally compact strictness example. **Classical warning:** continuous frames are spatial by Hofmann–Lawson duality, so separate work on noncontinuous frames is needed for genuinely pointless locales.

## Current results in Track A

See [**A: first hierarchy results and proofs**](A-hierarchy-first-results.md) and [the Picado–Pultr reading notes](A-reading-Picado-Pultr-2021.md).

Working results: I⊆U⊆F for every locale; preservation under localic maps; both inclusions strictly realized by an explicit seven-point finite locale and by a product with a **pointless** Boolean locale; regularity forces I=U=Δ, while normality forces U=F. All proofs remain subject to critical verification and priority checks.


See also [A: equality characterizations](A-equality-characterizations.md) for the completely-below formula, reflection theorem, exact equality tests, and counterexamples. [Future questions](future-questions.md) keeps deferred ideas.

## Immediate aim (A)

Express three point-separation relations as closed sublocales of a locale product:
`I(X) ⊆ U(X) ⊆ F(X)`.
Check their pointwise recovery, functorial properties, equalities and connection with the existing locale-theoretic notions of strong Hausdorffness and diagonal separation.

The notes for B and C preserve ideas from the first discussion while A is developed.

## Conventions

A frame is a complete lattice with finite meets distributing over arbitrary joins. `L = O(X)` for a locale `X`; `L ⊗ L = O(X × X)` denotes the **frame coproduct** (localic product), which need not equal the opens of the ordinary topological product of a given spatial presentation. The element `a ⊠ b` denotes a basic rectangle. `a* = (a → 0)` is pseudocomplement.

## Primary reference

P. J. Cameron and V. Kumar, *Graphs on topological spaces*, arXiv:2610.14783 (2026).

For further sources see [A: separation](A-localic-separation.md).
