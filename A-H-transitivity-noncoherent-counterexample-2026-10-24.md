# Project A — Transitivity of H does not imply H=F outside coherence (24 Oct 2026)

**Status:** New deduction from previously reviewed results, self-contained argument below. Not separately externally audited. No novelty claim.

## Proposition

There exists a locally compact sober T1 scattered space X for which the localic square is fit and
```
H(X) = I(X) = U(X) < F(X),
```
while H(X) is an internally transitive relation on X.

## Proof

Let X be the *discrete double cofinite-cloud extension* of the deleted Tychonoff plank T, along its two disjoint closed non-functionally-separable edges A and B, as constructed in [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md).

The established results there give X locally compact, sober and T1 with I=U<F as **closed sublocales** of the localic square. The plank T is scattered: ordinal spaces are scattered, finite products of scattered spaces are scattered (isolate a point in the first-coordinate projection of an arbitrary subset, then a point in its fiber), and subspaces of scattered spaces are scattered. The complement X\T consists entirely of isolated cloud points, hence X itself is scattered.

The same finite-product observation makes X×X scattered; it is also T1. Since X is locally compact sober, the localic square is spatial and identified with O(X×X) by the standard locally-compact-factor product theorem. The elementary T1-scattered-fit lemma, proved in [A-postV-external-audit-reconciliation-2026-10-24.md](A-postV-external-audit-reconciliation-2026-10-24.md), shows that O(X×X) is fit: every closed sublocale is fitted. Hence I is fitted, V=fit(I)=I, and the least closed-and-fitted sublocale H containing the diagonal is exactly I.

The universal point-free composition law I∘I⊆U together with I=U implies I∘I⊆I. Reflexivity and symmetry are inherited from I=cl(Delta), so H=I is an internal equivalence relation. The resulting strict chain is H=I=U<F. QED.

## Consequence

The coherent theorem 'H internally transitive iff H=F' does **not** extend to arbitrary locales; indeed the reverse implication fails even among locally compact sober T1 scattered spaces with fit localic square. The forward implication H=F ⇒ H transitive remains universal (F is a kernel-pair intersection).

This answers the question raised in §H5(2) of the [external referee report](A-postV-external-Claude-referee-report-2026-10-24.md). The counterexample is reused, not new; only its application to H and fit squares is new in these notes.
