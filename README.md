# Locales and graph-theoretic separation

Research notebook inspired by P. J. Cameron and V. Kumar, *Graphs on topological spaces* ([arXiv:2610.14783](https://arxiv.org/abs/2610.14783)).

## Workstreams

| Track | Topic | Status | Notes |
| --- | --- | --- | --- |
| **A** | Localic separation relations and the hierarchy | **Active** | [A: separation](A-localic-separation.md) |
| **B** | Graphs on nonzero elements of frames | Backlog | [B: overlap graphs](B-overlap-graphs.md) |
| **C** | Frame-cover nerves, Dowker duality, homotopy | Backlog | [C: nerves](C-frame-nerves.md) |

These are exploratory research notes, **not** a manuscript. Assertions are marked *proved (working)*, *to verify*, or *question*; “proved (working)” means the argument is included here but has not undergone independent referee checking. No originality claim is made without a literature review.

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
