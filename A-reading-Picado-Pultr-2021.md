# A — Reading notes: Picado–Pultr (2021)

**Reference:** Jorge Picado and Aleš Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021, DOI: [10.1007/978-3-030-53479-0](https://doi.org/10.1007/978-3-030-53479-0).

**Source policy:** Notes and short descriptions only. The university-library PDF supplied privately for this project is **not** to be placed in this public repository. Page numbers below are the book's printed page numbers.

**Status:** Initial reading of selected portions of Chapters III–IV; not a comprehensive literature review.

## Main conclusions relevant to Track A

1. **Our proposed `I(X)=cl(Δ_X)` is tightly connected to an established definition.** Isbell's **strong Hausdorff** axiom (sH) says that the *localic diagonal sublocale is closed* (III.5.1–5.3, pp. 49–50). Hence `I(X)=Δ_X` is just (sH), not a new separation condition. The `d_L` of III.5.3 is exactly the join of rectangles `a⊠b` with `a∧b=0`; it is the largest open disjoint from the diagonal. More exactly, `d_L` is the least element of the diagonal sublocale viewed as a subset of the coproduct frame, and the closed sublocale complementary to that open is its closure.

2. **Do not conflate localic (sH) and classical Hausdorffness.** The book emphasizes that (sH) is not conservative: classical Hausdorffness of a spatial space does not imply (sH) for its frame of opens (III.6 and IV.3.2, pp. 54–56, 76). This vindicates the warning in our initial A notes about sublocale equality versus pointwise equality.

3. **Existing hierarchy of point-free Hausdorff axioms.** Picado–Pultr distinguish weakly Hausdorff (wH), Hausdorff (H), and strongly Hausdorff (sH), with `(sH)⇒(H)⇒(wH)`, neither converse valid (III.2–6, IV.3.1, pp. 41–56, 76). (H), due to Paseka–Šmarda and Johnstone–Shu-Hao, is conservative, and can be formulated as: if `1≠a≰b`, there exist `u≰a, v≰b` with `u∧v=0` (III.3.4, p. 44). **This is a property of frames, not the assertion that the `I(X)` graph relation equals its diagonal.**

4. **Modified localic diagonal / weak product.** III.7, pp. 57–58, describes a modified product with a related closed-diagonal condition equivalent to (H). Very relevant if we try to design relations giving conservative pointwise recovery and well-behaved internal interpretations simultaneously.

5. **Further strong-Hausdorff characterizations.** III.5.3.3 (p. 51) gives a coproduct-ideal symmetry formula; III.5.4 (pp. 52–53) relates (sH) to coequalizers, and IV.2 (pp. 73–75) to weak homomorphisms and a separation condition (W). Any claimed elementary characterization or categorical novelty needs comparison here.

6. **Regularity and functional separation.** Chapter VI (pp. 107–136) develops complete regularity and cozero elements; VIII.3–4 (pp. 167–175) develops localic real-valued functions and Urysohn's lemma for *normality*. These are next reading priorities for our proposed functional relation `F(X)`. The book's uses of "Urysohn" here refer mainly to the **lemma**; our proposed `U(X)` is a different pairwise relation and needs a broader literature search before associating it with an established localic axiom.

## Questions to investigate next

- Is `U(X)=Δ_X` a known strong Urysohn or regular-diagonal axiom? Is it ever strictly weaker than (sH)? Note the direction: `I⊆U`, so `U=Δ` **implies** `I=Δ` and hence (sH); it cannot be weaker. Check possible equivalences and proper strengthenings.
- Is the proposed `F(X)` precisely the kernel pair of a known completely regular reflection, and what exactly does its diagonal equality mean?
- Can `I⊊U⊊F` hold in the **order of sublocales**, with strictness verified intrinsically?
- Compare with the paper by Arrieta, Picado, and Pultr on new diagonal separation (2022).

## Important correction to conceptual framing

The relation `I(X)` itself is well-defined without points and directly extends the ordinary inseparability graph relation, but its diagonal-equality condition is **classical locale theory** (Isbell's (sH)). The research opportunity is to study the **relations themselves and their comparisons**, not to present their associated equality conditions as novel.
