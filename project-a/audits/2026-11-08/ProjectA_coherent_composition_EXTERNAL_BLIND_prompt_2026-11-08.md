# Independent blind referee prompt — Project A coherent localic composition

**8 November 2026 — external audit, second of two separate foundational topics.**

Please read the accompanying technical packet **first and in full**, then write an independent, adversarial referee report. The packet is intended to be self-contained. You do not need to consult the Project A repository, previous ChatGPT conversations, an internal audit, or the report on the unrelated Scott-continuity question. If you do consult literature, identify precisely what it establishes and which mathematical steps are your own checks.

## Why this audit matters

Project A studies several canonical sublocale relations on a locale. Their composition is defined by taking the **localic image** of a pullback. Unlike set-theoretic relation composition, this operation is not associative for arbitrary localic relations, because locale surjections need not be stable under arbitrary pullback. Earlier coherent calculations used alternating relational words, and their legitimacy depends on a genuine categorical repair, not simply on pointwise order theory.

The candidate repair is that **proconstructible spectral relations on a coherent locale compose exactly as ordinary point relations**, forming an associative calculus under localic image composition. We also claim that the canonical specialization relations and the named diagonal hulls belong to this class and admit the claimed factorizations.

## Main tasks

Please evaluate *all* the following, treating a negative or conditional outcome as equally welcome as a positive one:

1. **Categorical foundations.** Check the ideal-completion adjunction, its use to identify `Loc` pullbacks of coherent locales along spectral maps with spectral-space fiber products, and whether any crucial claim is valid only for a coherent-map subcategory rather than in all of `Loc`.
2. **Proconstructible sublocales.** Check that a patch-closed subset of a spectral space, equipped with the spectral subspace topology, determines exactly the claimed localic sublocale; check compact-open trace surjectivity, finite meets/joins, and inverse-image pullbacks. Do **not** infer equality of arbitrary sublocales merely from equality of their ordinary points.
3. **Images.** Check that for a spectral map `f:T→Z`, its localic image is the sublocale represented by its patch-closed *set-theoretic* image; carefully analyze which part of the proof uses spatiality of the image target and why point-surjectivity suffices there.
4. **Composition and associativity.** Check the composable-triples pullback in `Loc`, the image onto the two endpoint coordinates, closure under binary composition and finite joins, and the resulting associativity and finite distributivity. Look for a counterexample among coherent locales and patch-closed relations.
5. **Named relation identifications.** Independently check that the localic specialization relation `A`, its converse `B`, `I=cl(Δ)` and `D=fit(Δ)` are the *specific* proconstructible spectral sublocales claimed, and hence that `I=A∘B`, `D=B∘A` hold as **sublocale equalities**. In particular, scrutinize the argument that the fitted diagonal is spatial/spectral; checking the point criterion alone does not suffice.
6. **Consequences and exact scope.** Evaluate the mixed-word identities, finite comparability powers and `J²=U∨V` *conditional on* the previously established coherent equalities `U=I²`, `V=D²`. State explicitly what breaks if coherence, spectrality, patch-closedness, or spectral-map hypotheses are removed. Do not use unrestricted associativity.

## Reporting standards

Please provide (a) a concise verdict table by claim, (b) all correctness issues in order of severity, including remarks and asides, (c) an independent argument or counterexample for any substantial correction, (d) a clear separation between published background, statements verified directly from the packet, and supplementary deductions, (e) exact scope of conclusions that can safely be used elsewhere in Project A, and (f) recommendations for a manuscript-ready presentation.

Pay special attention to two known dangers: **a spatial source and a closed image do not alone imply that the localic image is determined by its set of points**, and **general localic image composition is nonassociative**. If a proof only works under additional conditions, please state those conditions, rather than silently repairing the claim.

This is a *blind correctness audit*, not a request for research ideas or novelty certification. No need to work on the Scott-continuity problem or other Project A branches.

Please preserve your independent verdict before reading or requesting any prior internal audit or referee comparison.