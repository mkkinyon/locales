# A — Noncompact normality and D=U (21 October 2026)

**Status:** classical continuous-frame theorem proved; arbitrary-frame implication OPEN. This develops the compact-frame normality theorem from [A-external-audit-reconciliation-2026-10-21.md](A-external-audit-reconciliation-2026-10-21.md) and Claude Opus 5.5's independent audit §§3.2, 5. The full point-free noncompact implication is **not** asserted.

## 1. Positive result without compactness

**Theorem.** If L is a classically continuous **normal** frame, then D(L)=U(L)=F(L).

**Proof.** By Hofmann–Lawson L=O(X) for locally compact sober X, with O(X×X)=L⊕L. If (x,y)∉D then the point closures cl{x},cl{y} are disjoint. Normality separates these disjoint closed subsets by neighborhoods with disjoint closures; hence (x,y)∉U. Therefore the ordinary pair-point sets of U and D agree. For each open w∈O(X×X) satisfying δ*(w)=1, every U-point belongs to O(w), since every D-point does. Because U=C(d_U) is a **closed** sublocale of a spatial product, it is point-determined, so U⊆O(w). Intersecting gives U⊆D. The reverse D⊆U is universal. Normal ⇒ U=F is the established frame Urysohn lemma. □

**More general sufficient condition:** The same proof works for any *normal sober* topological space X for which the localic square agrees with the ordinary product and U is determined by its ordinary points. Do not infer arbitrary fitted-sublocale equality from equality on points.

**Noncompact examples:** Any noncompact locally compact Hausdorff space is normal only when separately assumed; in particular discrete infinite spaces are noncompact, normal and satisfy D=U=F=Δ. For a nonregular noncompact normal example, disjoint unions of finite least-point Alexandrov posets give normal, locally compact examples with D=U=F but generally D≠Δ.

## 2. The finite-cover result holds in all normal frames

For any normal frame L and any **finite** cover C, the independent audit §3.2 Proposition 3.2b proves

    d_U ∨ ⋁_{c∈C} c⊠c = 1.

This uses finite distributive lattice / finite prime-filter calculations and normality, not compactness. If L is compact, every cover has a finite subcover and thus D=U. If L is continuous, use §1 above. **No deduction for arbitrary noncompact, noncontinuous frames follows simply from finite-cover completeness.**

## 3. Why the arbitrary-frame extension is nontrivial

The criterion for D=U quantifies over *all* covers C of 1, possibly without finite subcovers. A join in Q=L⊕L can be 1 even without a finite witness; conversely the finite-cover lemma cannot be applied to a family of opens whose finite subjoins fall below 1.

A distributive-lattice prime filter of Q need not preserve arbitrary joins; showing that every point pair satisfies U⊆D is insufficient unless the closed U is determined by points in the product. Normality alone has not been shown to force that spatiality.

**Open:** Does normality of an arbitrary (possibly pointless, noncontinuous, noncompact) frame imply d_U∨w_C=1 for every cover? No proof or counterexample identified here. A point-free proof must address genuinely infinite covers or supply an independent compact/locality reduction.

## 4. Converse and relation with regularity

Noncompact D=U does **not** imply normal: every regular frame has I=U=Δ and hence D=U, while classical regular nonnormal spaces exist. Thus an arbitrary normality sufficiency would not be a characterization outside compact frames.

**Research next:** Seek a direct infinite-cover tensor argument, or a normal noncontinuous frame failing D=U. Keep the distinct question D=U⇒U internally transitive point-free as a separate line. Do not spend more work merely reproducing the continuous spatial proof in frame language without addressing the missing general case.

## 5. Bounded investigation, segment 1 of at most 2 (21 October 2026)

The arbitrary-frame normal ⇒ D=U implication remains OPEN after a direct attempt to extend the finite-cover criterion. Normality establishes d_U∨w_C=1 whenever C has a finite subcover. The exact obstruction is an arbitrary cover C with ⋁C=1 but no finite subcover, for which one would need a nonzero residual of Q below the complement of d_U∨w_C. The finite-lattice/prime-filter proof does **not** extend by choosing a prime filter containing 1=⋁C: prime filters need not respect infinite joins. Invoking completely prime filters assumes spatiality of the relevant quotient/product and is circular.

Normality of a topological space guarantees Ury=Cm for ordinary point pairs; hence a normal-frame counterexample, if one exists, must involve genuine localic nonspatial behavior (of the product or relevant closed sublocale), not just two ordinary points.

Literature checked at a high level: Arrieta–Picado–Pultr 2022 (fitted diagonal) and Arrieta 2024 (dual of closedness/fitness) give no immediate theorem equating this arbitrary normality implication, based on available descriptions. No novelty conclusions.

**One final segment permitted**, directed at either (a) an infinitary coproduct/cover proof, or (b) a concrete normal noncontinuous counterframe. If unsuccessful mark deferred, rather than prolonging the search.

## 6. Bounded investigation, segment 2 of 2: universal coproduct test (21 October 2026)

**Status: DEFERRED, unresolved.** Two-segment limit reached.

Use the universal property of Q=L⊕L. For a cover C with ⋁C=1, the failure of d_U∨w_C=1 is **equivalent** to the existence of a nontrivial frame M and frame homomorphisms f,g:L→M with

1. f(a)∧g(b)=0 in M whenever a*∨b*=1 (all far rectangles annihilated);
2. f(c)∧g(c)=0 in M for every c∈C (all cover squares annihilated).

Proof: if q=d_U∨w_C<1, the closed quotient Q→↑q, z↦z∨q, has nontrivial codomain, and its compositions with coproduct injections provide f,g. Conversely, universal factorization of f,g through Q carries q to 0_M, so q<1 whenever M is nontrivial. The equivalence is exact but **does not by itself decide the conjecture**.

Normality plus the finite-cover lemma prohibits such a pair for a finite cover, and indeed whenever C has a finite subcover. To infer a contradiction for arbitrary C using finite prime filters would silently assume preservation of infinite joins: an ordinary prime filter of the finite-distributive reduct of L may contain ⋁C=1 while containing no c∈C. Passing to completely prime filters requires a spatiality assumption. A generic frame codomain M is necessary for a genuinely point-free argument.

No direct infinitary cp-ideal derivation or explicit normal noncontinuous counterframe emerged in this segment. Existing positive cases: compact, continuous, and any setting with the relevant localic product and closed U detected by ordinary points. **Do not claim normal⇒D=U for all frames.** Close this exploration after two segments as requested; next priority is point-free transitivity of U under D=U.
