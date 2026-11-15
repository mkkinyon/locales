# Referee report — Project A (LC-A) blind external audit

Nov 15, 2026 · @Someone

## Verdict

**Correct.** The explicit \[0,1\] theorem (5.5) holds as stated, and no repair is needed.

Every lemma it rests on checks out: 3.1, 3.2, 3.3, 4.1, 5.1 and 5.2. The second witness in §6 and the optional generalization in §7 are also correct. I found no reversed order convention, no invalid pullback or sublocale inference, and no gap between topological and localic local compactness.

I re-derived each step from the universal property (1.2). As a separate check, I computed the frame of E in (5.4) explicitly, without using Booleanization. That computation agrees with the packet and is recorded under priority check 5.

The items under *Minor issues* are wording and framing only. The section after it gives a shorter proof and a sharper form of §7; those are suggestions, not part of the audited theorem.

## Major issues

**None.** No step fails, so there is no counterexample to report.

The places I tried hardest to break, and why each holds:

- **Topological versus localic local compactness (Lemma 3.2).** O(X) is a continuous frame. U\_F ≪ U\_F because U\_F is compact open, and V ≪ W whenever V ⊆ C ⊆ W with C compact. Every open is a join of opens way below it.
- **Nucleus order (Lemma 5.1).** The inequality u → a ≤ ¬¬a says the open nucleus is below the double-negation nucleus. A larger nucleus is a smaller sublocale, so β ≤ O(u). The direction is right.
- **The pullback in Lemma 4.1.** The fiber is tested against arbitrary locales Z, and the argument never restricts to points.
- **Nonzero versus pointless (5.2)–(5.4).** Nonzeroness is a frame statement and pointlessness is a statement about points of a sublocale meet. The packet keeps them separate, and both hold.
- **Spatiality inheritance (proof of the theorem).** Only closed and open sublocales are used. The false statement about arbitrary sublocales is never invoked.

## Priority checks

All seven are confirmed. Notation: p! is the constant map Z → X at p, and z∗ is the frame map of z.

### 1. Topology and separation (§2, Lemmas 3.1–3.2)

Confirmed. The family is a topology: X = U\_∅, formulas (2.1) give finite meets, and the exact union rules are U\_F ∪ V = U\_{F∖V} and ⋃U\_{F\_i} = U\_{⋂F\_i}.

Compactness and T1 are as in Lemma 3.1. Each U\_F is compact for the same reason: any open containing p misses only finitely many points.

Local compactness is the localic kind. C compact in K is compact in X, because K carries its original topology. The way-below relations in *Major issues* then show O(X) is continuous.

The sobriety proof is complete. Opens of K are open in X, so two points of C ∩ K split C. The set {p, x} is split by U\_{x} and K. Singletons are closed, and T1 gives uniqueness of the generic point.

### 2. Failure of stability (Lemma 3.3)

Confirmed. K and U\_{x} are compact, every subset of a T1 space is saturated, and K ∖ {x} is not closed in K, so it is not compact.

A frame-level check removes any dependence on convention. Put a = K ∖ {x}. Then a ≪ K and a ≪ U\_{x}, since each contains a and is compact. But K ∧ U\_{x} = a, and a ≪ a fails because a is not compact. So ≪ is not multiplicative.

### 3. Fitted fiber (Lemma 4.1)

Confirmed for arbitrary test locales. Since \[p\] ≅ 1, maps Z → F\_p are exactly the maps (p!, z) that factor through A(X).

(p!)∗u is 1 or 0 according to whether p ∈ u. The condition z∗u = 1 is precisely factoring through O\_X(u). Meets of sublocales are limits, so factoring through each O\_X(u) is factoring through the meet (4.1).

F\_p → {p} × X ≅ X is a sublocale embedding, being a pullback of A(X) ↪ X × X. So (4.2) is an equality of sublocales of X, not only an isomorphism.

### 4. Booleanization (Lemmas 5.1–5.2)

Confirmed. The computation in Lemma 5.1 is correct and the order direction is right. It is the easy half of Isbell's density theorem.

Every nonempty open of X is infinite, so it meets K and every U\_F. That gives both density claims in Lemma 5.2. β\_X is nonzero because 0 and 1 are distinct regular elements.

Explicitly, the regular opens of X are ∅, X, and the regular opens of K other than K itself.

### 5. From the fiber to nonspatiality (§4 end, §5)

Confirmed. \[p\] is the closed complement of the open K, so F\_p is the closed sublocale of A(X) cut out by ρ₁∗K. E is F\_p met with the preimage of O(K) under ρ₂, so it is open in F\_p.

A closed sublocale ↑a of a spatial frame is spatial, since meets of primes above a stay in ↑a. An open sublocale is the topology of an open subspace. Neither fact extends to arbitrary sublocales, and the proof does not need that.

**Independent check of E.** For V open in K, U\_F → V is the K-interior of V ∪ F, and U\_F → U\_G = U\_{G∖F}. Taking common fixed points over all finite F gives:

```latex
\mathcal O(E)=\{\,V\subseteq K \text{ open} : K\setminus V \text{ has no isolated points}\,\}\;\cong\;\{\text{perfect subsets of }[0,1]\}^{\mathrm{op}}
```

This frame contains ∅ ≠ K, so E ≠ 0. It has no prime element: a nonempty perfect set C lies in \[0,t\] ∪ \[t,1\] but in neither half, for t strictly between two points of C. So E is nonzero and pointless, with no appeal to β\_X.

### 6. Independent witness (§6)

Confirmed. For u = U\_F, z∗u = 1 by (6.1); for p ∉ u the left side of (1.2) is 0. So (p!, z) factors through A(X).

It lands in A(X) ∧ (\[p\] × O(K)), which is E under Lemma 4.1. That piece receives a map from the nonzero locale β\_K, so it is nonzero. The witness therefore certifies the specific locally closed piece, not just some nonspatial sublocale.

One caveat on the word "independent" is listed under *Minor issues*.

### 7. Scope of the conclusion (§5 end, §7)

Confirmed as a statement about sublocales. Δ\_X ≤ A(X) always. Δ\_X ≅ X is spatial with points the diagonal pairs, so Δ\_X = \[G\_≤\]. A(X) is not spatial, so the two differ.

A direct argument: E ∧ Δ\_X = 0 while E ≠ 0. A map (p!, z) through Δ\_X has z = p!, so z∗K = 0; landing in E needs z∗K = 1; hence Z = 0.

The §7 generalization was checked separately and is correct. K is infinite, being nonempty and T1 without isolated points, so opens at p meet K. Finite subsets of K have empty interior. C ∖ {x} is not closed in C, because x is non-isolated in the neighborhood C.

## Minor issues and presentation

None of these affects correctness.

1. **§6, "independent" is overstated.** K is dense open in X, so β\_K and β\_X are the same sublocale of X. §6 uses the same witness as §5. What §6 is independent of is Lemma 4.1: it proves the theorem without the fiber identification. The section title should say that.
2. **Lemma 3.3, "finite intersections".** Under the stably locally compact convention only binary intersections are required; the empty intersection (compactness of X) belongs to stable compactness. This is harmless here because X is compact. Adding the frame-level witness from priority check 2 would make the lemma convention-free.
3. **Lemma 3.2, statement.** "Strong (core-compact/localic) sense" merges two notions. The proof shows compact neighborhood bases, which implies core-compactness; the two agree for sober spaces. The remark on saturation is not needed for this lemma.
4. **§5, last paragraph, "spatial image of X".** This is nonstandard. Suggested wording: the image of the diagonal embedding X → X × X, a sublocale isomorphic to X. It is worth stating that Δ\_X is not closed, since X is not Hausdorff; a reader may assume otherwise.
5. **§2, unions.** "Possibly enlarged by ordinary opens" is loose. The exact formula is U\_F ∪ V = U\_{F∖V}.
6. **(5.2) is a strict inequality.** β\_X is properly smaller than E. For example, the complement of the Cantor set is a fixed element for E but is not regular open. Nothing depends on this; it only shows E is larger than the proof needs.
7. **Lemma 5.1.** A reference to Isbell's density theorem would help readers place it.
8. **Unauditable context.** The positive result (A-SC) and the §7 list of earlier tests (open-cover, semilattice-retraction, Alexandrov, Scott-domain) are not in the packet. Neither is used in the proof, and I did not assess them.

## Suggestions beyond the audited theorem

These are my own sketches. They have had no independent review and should be checked before use.

### A shorter proof

The theorem follows from §6 plus one line, with no fiber lemma and no locally closed argument.

1. Let z be the inclusion of β\_K into X. By (6.1), (p!, z) factors through A(X).
2. It does not factor through Δ\_X. That would force z = p!, so z∗K = 0, while z∗K = 1 and β\_K ≠ 0.
3. Δ\_X = \[G\_≤\] is the spatial part of A(X). So A(X) is strictly larger than its spatial part.

Any nonzero locale Z with a map z to K satisfying z∗(K ∖ {x}) = 1 for every x works in place of β\_K.

### A sharper form of §7

**Claim.** Let K be locally compact Hausdorff and X = K ∪ {p} as in §2. Then A(X) is spatial if and only if K is scattered.

Sketch:

- A(X) ∧ (K × \[p\]) = 0, because u = K gives 1 ≤ 0. So the open part A(X) ∧ (K × X) equals A(K).
- A(K) = Δ\_K for regular K. From v ≺ u and (1.2) applied to ¬v, one gets g₂∗v ≤ g₁∗u, hence g₁ = g₂.
- The closed part is F\_p, which is the point (p, p) together with its open complement E.
- So A(X) = Δ\_X exactly when E = 0. By the formula in priority check 5, which needs only T1, this holds exactly when K has no nonempty perfect subset.

Two consequences:

- **The hypothesis "without isolated points" can be weakened to "not scattered".** Lemma 5.2 fails when K has isolated points, since U\_F is then not always dense. The §6 route still works with β\_P, where P is the perfect kernel of K.
- **The weakened hypothesis is sharp.** K = ω + 1 gives a compact, locally compact, sober, T1 space X that is not stably locally compact, since K ∩ U\_{ω} = ω is not compact. Yet A(X) = Δ\_X is spatial. This is a small calibration example for the §7 remark that nonstable spaces can have spatial A(X).

### Next questions

- Lemma 4.1 uses nothing special about this X. For any locale and any point p, the fiber of ρ₁ over \[p\] is fit(\[p\]). So spatiality of A(X) forces fit(\[p\]) to be spatial at every closed point.
- Is that condition, for all points or for all compact saturated sets, also sufficient when X is locally compact and sober?
- Does stable local compactness imply it directly? If so, that would give a conceptual reading of (A-SC).

## Scope and limits of this review

- **Materials.** I read only the two files in the zip: the referee prompt and the packet, both dated 15 November 2026. I did not see the Project A repository, the internal audit, or earlier referee reports.
- **Method.** Every assertion in §1–§7 was re-derived by hand from the definitions. Nothing was machine-checked or formalized.
- **Standard facts relied on.** Sublocale meets are limits. Larger nuclei give smaller sublocales. Open and closed sublocales of spatial locales are spatial. Compact neighborhood bases give a continuous frame. A sublocale is the join of an open part and its closed complement. I used these from memory and did not look up references.
- **Logic.** Classical throughout, matching the packet's disclaimer on constructive validity.
- **Not assessed.** Publication priority, the separate result (A-SC), and the earlier tests named in §7.
