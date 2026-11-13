# Independent referee report — Cohen × Arrieta fitted-diagonal product (Project A)

Nov 13, 2026 · @Someone

## Verdicts

The main claim (E.1) is correct: D(Z\_C×A) is strictly smaller than Δ\_{Z\_C}×D(A). I found no error in B.1, D.1–D.3, E.1 or F. One step of D.2 needs a one-line repair, and E.1 can be proved without the strong-Hausdorff source fact (see "E.1" below).

| Claim | Verdict | Reason |
| --- | --- | --- |
| B.1, general closed-graph theorem | Correct | Every step holds for sublocales, not only for points. (1)⇒(2) needs no strong Hausdorffness; (2)⇒(1) needs some such hypothesis (Sierpiński space is a counterexample without it). |
| D.1, h and k are frame homomorphisms | Correct | u ↦ int cl(u∩Y) is O(A) → O(Y) → RO(Y) ≅ RO(C); W ↦ W×C preserves regular-open joins. |
| D.2, all-cover lemma | Correct with repair | The proof needs V ⊆ ro(V\_u), not V ⊆ V\_u. One line fixes it. |
| D.3, empty localic equalizer | Correct | The support s of any equalizing sublocale lies below every e\_n, and the Boolean meet int(Δ\_C) is 0. |
| E.1, strict product inequality over the Cohen base | Correct | Follows from B's argument given Arrieta's Corollary 4.3. I also give a direct binary cover that does not use that source fact. |
| F, the D₂ control pair | Correct | Finite covers match; the countable cover {a\_n} ∪ {a\_\*} has matching value 0. |
| G.1–G.3, separation from Q and Q′ | Logic correct; (A.3) not checkable as written | W, W₂, U, Q, Q′ are never defined in the packet. Under the natural reading the closures of both sides of E.1 agree. |
| §C source facts | Confirmed against arXiv v1 | Construction 4.2, Corollary 4.3, Proposition 4.4 and Example 4.5 say what the packet says they say. |

I found no counterexample to any claim and no missing hypothesis in the statements.

## Scope, blindness and source access

I read `EXTERNAL_BLIND_PROMPT.md` first, then `EXTERNAL_BLIND_PACKET.md`, and nothing else from the project. I did not see or ask for the internal audit.

**Source.** I read Arrieta's paper in the ar5iv HTML rendering of [arXiv:2310.18522v1](https://ar5iv.labs.arxiv.org/html/2310.18522). The direct arXiv PDF link in the prompt was not reachable from this session. My reading tool returns extracts rather than the full text, so three limits apply:

- I saw the statements of Proposition 4.1, Construction 4.2, Corollary 4.3, Proposition 4.4 and Example 4.5, and the mention of Propositions 4.8–4.9 and Corollary 4.10.
- I saw only the first half of the proof of Proposition 4.1, which is what carries strong Hausdorffness.
- I did not open the published *Topology and its Applications* version, so numbering is checked against arXiv v1 only.

**Self-contained checks.** (A.1), (A.2), Theorem B.1, Claims D.1–D.3, the pair in §F, and E.1 by the direct cover in the "E.1" section. None of these depends on the source.

**Source-dependent.** Only one fact: that A is strongly Hausdorff. The packet's own route to E.1 and to the D₂ product inequality in §F uses it. I give an independent argument for it in the "§C" section.

## First point of confusion

The first stumble is notational and is not resolved by the packet; the first mathematical one is in D.2 and is resolved.

1. **Undefined closed-level objects.** The prompt (task 7, "Research status") and (A.3) use W, W₂, U, Q and Q′. Neither file defines them. I had to guess what a "closed hull" is before I could assess §G.
2. **D.2, the step from the Y-trace to h(u).** The proof says the Y-trace of u contains V∩Y with V ⊇ K\_n, and concludes that h(u)∧k(u) meets R×S. But h(u) is built from an arbitrary V\_u with the right trace, and V\_u need not contain V or K\_n. It resolves because V∩Y ⊆ V\_u gives V ⊆ cl(V\_u), so V ⊆ ro(V\_u).
3. **Which Cohen algebra.** The prompt writes Z\_C = Loc(RO(2^ω)); the packet uses RO(2^ω×2^ω). These are isomorphic, and E.1 is invariant under isomorphism of the base, so this is only a presentational bump.

## Theorem B.1

Theorem B.1 is correct as stated, including the binary-cover clause. I checked each step as a statement about sublocales. Below, f∗ denotes the frame map of a locale map f, o(w) and c(w) the open and closed sublocales of w, and δ\_Y the open complement of the closed diagonal.

1. **(A.1).** The opens w\_C are cofinal among open neighbourhoods of Δ\_X. If w = ⋁ a\_i⊠b\_i pulls back to 1 along the diagonal, then C = {a\_i∧b\_i} is a cover and w\_C ≤ w. A map factors through a meet of sublocales iff it factors through each, and through o(w) iff it pulls w back to 1.
2. **Boolean base.** For the cover {b, ¬b}, the matching equation forces h∗(b) = h∗(b)∧k∗(b), and symmetrically, so h = k. Applied to the two projections of D₂(Z), this gives D₂(Z) = D(Z) = Δ\_Z.
3. **(A.2).** Preimage along p×p preserves meets of sublocales and sends open sublocales to open ones. D(Z)×D(X) is the meet of the two preimages.
4. **(1)⇒(2).** As in the packet. Strong Hausdorffness is not used here.
5. **E is nonzero.** o(δ\_Y) and c(δ\_Y) are complements and the sublocale lattice is distributive, so D(Y) = Δ\_Y ∨ E. If E = 0 then D(Y) = Δ\_Y.
6. **Booleanization.** B(E) is dense in E, so it is nonzero exactly when E is.
7. **Equalizer.** eq(f,g) is the pullback of Δ\_Y along (f,g), which lies below o(δ\_Y)∧c(δ\_Y) = 0. This is the genuine pullback sublocale, not a statement about points.
8. **Closed graphs.** Γ\_f is the equalizer of f∘p and q on Z×Y, that is the pullback of Δ\_Y along f×1. Pullbacks of closed sublocales are closed, so Γ\_f = c(u\_f) with u\_f as below.
9. **Complement cover.** A map (a,b) into Γ\_f∧Γ\_g has b = fa = ga, so a factors through eq(f,g) = 0. Hence c(u\_f)∧c(u\_g) = c(u\_f∨u\_g) = 0, which forces u\_f∨u\_g = 1.
10. **Matching value.** s\_f factors through c(u\_f), so s\_f∗(u\_f) = 0, and likewise s\_g∗(u\_g) = 0. The value is 0, and 0 ≠ 1 because Z is nonzero.
11. **Product factorization.** p∘s\_f = p∘s\_g = 1\_Z and (q∘s\_f, q∘s\_g) = (f,g), which factors through D(Y).

```latex
u_f=(f\times 1_Y)^*(\delta_Y),\qquad u_g=(g\times 1_Y)^*(\delta_Y),\qquad u_f\vee u_g=1,
\qquad \bigl(s_f^*(u_f)\wedge s_g^*(u_f)\bigr)\vee\bigl(s_f^*(u_g)\wedge s_g^*(u_g)\bigr)=0 .
```

**The hypothesis in (2)⇒(1) cannot simply be dropped.** Let S be Sierpiński space. Every cover of S contains the top element, so D(S) = S² ≠ Δ\_S. For Boolean Z, opens of Z×S are pairs u ≤ v in O(Z), and a cover {(u\_i, v\_i)} has ⋁u\_i = 1. Any pair of maps with a common Z-coordinate z satisfies s∗(u,v) ≥ z∗(u), so it matches every cover. Hence D(Z×S) = Δ\_Z×D(S) for every Boolean Z although (1) fails.

## §C source facts

The packet reports the source accurately, and strong Hausdorffness of A holds by two independent routes.

**What the source says** ([arXiv:2310.18522v1, §4](https://ar5iv.labs.arxiv.org/html/2310.18522)).

- Construction 4.2 starts from a Hausdorff space X and pairwise disjoint nonempty compact sets K\_n. It sets Y = X ∖ ⋃K\_n and Z = Y ⊔ ℕ, with the base the packet states. Y is open in Z, carries its X-topology, and ℕ is discrete.
- Corollary 4.3: if X is strongly Hausdorff, so is Z. The proof goes through Proposition 4.1, which needs a Hausdorff space, a strongly Hausdorff open subspace, and a closed complement that is a spatial multiplier.
- Proposition 4.4: if Y is dense and every infinite subfamily of the K\_n has dense union, any two nonempty opens of Z have intersecting closures.
- Example 4.5 takes X = {0,1}^ℕ and exactly the K\_n of the packet. It concludes Hausdorff, strongly Hausdorff and anti-Urysohn. Corollary 4.10 adds that such spaces are not F-separated.

**What I checked directly.**

- The hypotheses of Proposition 4.1 hold for A. A is Hausdorff, Y is open and is a sublocale of the regular locale C, and ω = A ∖ Y is closed and discrete.
- Cofinal density: a cylinder with prefix s of length m contains s0…0 1 000… with the 1 in place n, for every n ≥ m. So K\_n meets it for all n ≥ m, and one n serves any two cylinders.
- ⋃K\_n is the set of nonzero finitely supported sequences. The zero sequence lies in Y, which is why §F needs a\_\*.
- Corollary 4.10 agrees with D.2 and D.3, which together prove independently that D(A) ≠ Δ\_A.

**Independent route to strong Hausdorffness.** The localic square of A is spatial, so the closed diagonal of the Hausdorff space A is a closed sublocale.

1. Y is the meet S of countably many open sublocales o(u\_n) of C, one for each removed point. Such a meet in a compact Hausdorff space is spatial: if S∧o(a)∧c(b) ≠ 0, regularity gives opens t\_n with cl(t\_{n+1}) ⊆ t\_n∩u\_{n+1} that still meet S∧c(b), and compactness gives a point of Y in a ∖ b.
2. The same holds for Y×Y inside C×C, so the localic product of Y with itself is the space Y×Y.
3. A×A is the join of the four sublocales Y×Y, Y×ω, ω×Y, ω×ω. Each is spatial, and joins of spatial sublocales are spatial.

Step 1 uses dependent choice. I regard this route as a cross-check, not as a replacement for reading Proposition 4.1 in full.

## Claims D.1–D.3

All three claims are correct; D.2 needs the repair in step 2 below. Write r(u) = int cl(u∩Y), with interior and closure taken in C.

**D.1.** r is the composite O(A) → O(Y) → RO(Y) ≅ RO(C): restriction to an open subspace, then the double-negation quotient, then the isomorphism for a dense subspace. Equivalently, double negation on O(C) is constant on the fibres of the surjection O(C) → O(Y), so it descends. Then h(u) = r(u)×C and k(u) = C×r(u). The map W ↦ W×C sends regular opens to regular opens and preserves regular-open joins, because closure and interior commute with ×C. So h and k preserve finite meets and arbitrary joins of M, and r(u) = ro(V\_u) for every admissible V\_u.

**D.2.** The join in RO(P) of a family W\_i is int cl(⋃W\_i). So it equals 1 exactly when ⋃W\_i is dense in P. This is the correct criterion in the complete Boolean frame, and it puts no size restriction on the cover.

1. Fix nonempty cylinders R, S and take n at least both prefix lengths, so K\_n meets both.
2. Pick u in the cover with n ∈ u, and an open V ⊇ K\_n with V∩Y ⊆ u. Then V∩Y ⊆ V\_u, so V ⊆ cl(V∩Y) ⊆ cl(V\_u), hence V ⊆ r(u). **This is the repair.**
3. So r(u) meets R and S, and h(u)∧k(u) = r(u)×r(u) meets R×S.

The union of the opens r(u)×r(u) is therefore dense, and (D.2) holds for every A-cover.

**D.3.** h(a\_n) = {x\_n = 1}×C and k(a\_n) = C×{y\_n = 1}, since {x\_n = 1} is an admissible V for a\_n. The nucleus identity j(b) = b ∨ j(0) is right, so every sublocale of Z\_C is o(s) for some s ∈ M. If f and g agree on o(s) then s∧h(a\_n) = s∧k(a\_n), so s ≤ e\_n for every n. The meet in RO(P) is the interior of the intersection, and the intersection of the e\_n is Δ\_C, which has empty interior. So s = 0.

**What D.1–D.3 amount to.** The pair (h,k) induces a dense surjection from O(A)⊗O(A) onto the Boolean frame RO(P). So (f,g) is exactly the Booleanization B(A²) ↪ A². D.2 then says that every open neighbourhood of the diagonal is dense in A². D.3 says that the off-diagonal open δ\_A is dense.

## E.1

E.1 is correct, with the Cohen base itself. I tried to falsify the cover equation and the pullback squares and could not.

**The packet's route.** Steps 8–11 of the B.1 check apply verbatim to (Z\_C, f, g), given D.2, D.3, M ≠ 0 and the closed diagonal of A. Every object in that chain is a sublocale; no step refers to points.

**A route that does not use strong Hausdorffness.** Work in O(Z\_C×A) = M⊗O(A) and define

```latex
U_f=\bigvee\{\,b\boxtimes v \;:\; b\wedge h(v)=0\,\},\qquad
U_g=\bigvee\{\,b\boxtimes v \;:\; b\wedge k(v)=0\,\}.
```

Since s\_f∗(b⊠v) = b∧h(v), we get s\_f∗(U\_f) = 0, and likewise s\_g∗(U\_g) = 0. It remains to show U\_f ∨ U\_g = 1.

1. Fix n and put v\_n = Y ∪ {n}. This is A-open, and the v\_n cover A.
2. Take disjoint clopen R, S ⊆ C with R∩K\_n = ∅. Split v\_n = v′ ∪ v″ with v′ = ((C∖R)∩Y) ∪ {n} and v″ = R∩Y. The set v′ is A-open because C∖R is an open neighbourhood of K\_n.
3. h(v′) = (C∖R)×C is disjoint from R×S, so (R×S)⊠v′ ≤ U\_f. And k(v″) = C×R is disjoint from R×S, so (R×S)⊠v″ ≤ U\_g. Hence (R×S)⊠v\_n ≤ U\_f ∨ U\_g.
4. These rectangles R×S have dense union in P, because K\_n is finite and the diagonal is nowhere dense. So their join in M is 1, and 1⊠v\_n = ⋁(R×S)⊠v\_n ≤ U\_f ∨ U\_g.
5. Joining over n gives 1⊠1 ≤ U\_f ∨ U\_g.

Step 4 is the exact place where the complete Boolean join differs from the point-set union. The union of the rectangles misses the diagonal and K\_n×C, yet its regular-open join is 1, and b ↦ b⊠v preserves joins of M.

**Conclusion.** {U\_f, U\_g} is a binary open cover of Z\_C×A with matching value 0 under (s\_f, s\_g). By D.2 the pair factors through Δ\_{Z\_C}×D(A). This gives slightly more than (E.1):

```latex
\Delta_{Z_C}\times D(A)\ \not\le\ D_2(Z_C\times A),
\qquad\text{hence}\qquad
D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A).
```

**Same base.** M = RO(C×C) is isomorphic to RO(2^ω) through a homeomorphism C×C ≅ C, and (E.1) is invariant under isomorphism of the base. No appeal to the existential base of B.1 is made.

## §F, the D₂ control pair

§F is correct, and the pair (h₀, k₀) is a different object from the pair (h, k) of §D.

- **Finite covers.** Some member u of a finite A-cover contains infinitely many attached points. Then r(u) contains the corresponding K\_n, whose union is dense, so r(u) = C and h₀(u) = k₀(u) = 1.
- **The countable cover.** {a\_n} ∪ {a\_*} does cover A: attached n lies in a\_n, a point of Y with some bit 1 lies in some a\_n, and the zero sequence lies in a\_*. For each member, h₀ and k₀ are complementary clopens, so every matching term is 0.
- **Equalizer.** h₀(a₀) and k₀(a₀) are complements, so any equalizing support s is 0.
- **Product inequality.** D₂(Z×X) ≤ Δ\_Z×D₂(X) holds because a finite cover pulls back to a finite cover. The binary cover then comes from B's graph argument, or from the direct construction above with cylinders R that miss K\_n. A cylinder is always disjoint from its bit-flip.

The two pairs sit in different places. (h₀, k₀) is the Booleanization of the graph of the bit-flip, a nowhere dense closed subset of C×C; it lies in D₂(A) but not in D(A). (h, k) is the Booleanization of the whole square; it lies in D(A). The full-D proof of §§D–E never uses (h₀, k₀).

**One point for the author.** For the countable cover 𝒞 = {a\_n} ∪ {a\_\*}, the pair (h₀, k₀) factors through D₂(A) and through c(w\_𝒞). So D₂(A) ∧ c(w\_𝒞) ≠ 0 for X = A. That has the shape G.2 calls an internal defect, for A itself and not for Z\_C×A. Please confirm this is consistent with the stated status of Q′; I cannot, without the definitions.

## What the result does not imply

E.1 is invisible at the closed level: both sides of it have the same closure, Δ\_{Z\_C}×A². So it cannot bear on any question stated purely in terms of closed hulls.

**A density lemma I verified.** For every locale Z and every open cover 𝒞 of Z×A, the pullback of w\_𝒞 to Z×A² (common Z-coordinate) is dense.

1. Refine 𝒞 to rectangles b\_i⊠v\_i; the pullback contains ⋁ b\_i⊠v\_i⊠v\_i.
2. Take a nonzero rectangle b⊠v⊠v′ and cylinders R, S whose Y-traces lie in v and v′. Choose n with K\_n meeting R and S.
3. Pulling the cover back along z ↦ (z, n) gives ⋁{b\_i : n ∈ v\_i} = 1. So some i has n ∈ v\_i and b∧b\_i ≠ 0.
4. Then v\_i meets v and v′, and the two rectangles have nonzero meet.

**Consequence.** For Boolean Z,

```latex
B(Z\times A^2)\ \le\ D(Z\times A)\ \le\ D_2(Z\times A)\ \le\ \Delta_Z\times A^2,
\qquad
\overline{D(Z\times A)}=\overline{D_2(Z\times A)}=\Delta_Z\times A^2 .
```

The last sublocale is closed because a Boolean locale is regular, hence strongly Hausdorff.

**Reading of §G under this lemma.**

- **G.1.** If W and W₂ are the closures of D and D₂, or the meets of the closures of the o(w\_𝒞), then W = W₂ = Δ\_Z×A² follows from the lemma and is compatible with (E.1). I cannot assess U, Q or Q′: the packet does not define them.
- **G.2.** Correct. The witness (s\_f, s\_g) lies outside D₂(Z\_C×A). It says nothing about D versus D₂ inside Z\_C×A, and nothing about whether D is relatively open in D₂ there.
- **G.3.** Correct, but understated for A. B.1's canonical base B(E) equals B(A²), which is Z\_C, and its canonical pair is (f, g). The Cohen specialization is the general construction, not a separate one.

So (E.1) settles neither Q nor Q′, on any reading in which those are closed-hull statements.

## Gaps and explicit repairs

There is one real gap in a proof (item 1) and one in the presentation (item 2). The rest are omissions that a reader can fill but should not have to.

1. **D.2, containment of K\_n.** Replace "its Y-trace contains V∩Y … hence intersects both R and S" by: V∩Y ⊆ V\_u∩Y, so V ⊆ cl(V\_u), so V ⊆ ro(V\_u). Hence K\_n ⊆ ro(V\_u) and h(u)∧k(u) = ro(V\_u)×ro(V\_u) meets R×S.
2. **Undefined objects.** Define W, W₂, U, Q and Q′ in the packet, or drop (A.3) and §G.1 from what the referee is asked to confirm.
3. **(A.1) cofinality.** State that every open neighbourhood of Δ\_X contains some w\_C. Without it, "fit(Δ\_X) is the meet over covers" is an assertion.
4. **B.1, scope of hypotheses.** Say that (1)⇒(2) needs no separation hypothesis. Say that (2) is trivially true for the one-point base, so the quantifier over all Boolean Z carries the content.
5. **E.1, dependence on the source.** As written, E.1 rests on Arrieta's Corollary 4.3. The direct cover {U\_f, U\_g} removes that dependence and should be included.
6. **D.3, why the a\_n suffice.** Say explicitly that an equalizing sublocale is o(s), and that agreement on the a\_n alone forces s ≤ e\_n. The packet's "forces its Boolean support below each e\_n" is right but terse.
7. **§C wording.** Arrieta's hypothesis is "nonempty compact", which the finite K\_n satisfy. Note that the zero sequence belongs to Y.
8. **§F internal defect.** Acknowledge that (h₀, k₀) witnesses D₂(A) ∧ c(w\_𝒞) ≠ 0, and say how that relates to Q′.

No objection in this list concerns a difference between points and sublocales. Every sublocale statement in the packet is used correctly.

## Simplifications and generalizations

The main simplification is that §§D–E are B.1's own construction applied to A, with Z\_C = B(A²). Everything in this section goes beyond what the packet proves and is offered for the author to check.

- **One statement for §§D–E.** Let Y be a nonzero strongly Hausdorff locale in which every open neighbourhood of the diagonal is dense in Y² and the off-diagonal open δ\_Y is dense. Put Z = B(Y²) with its two coordinate maps. Then Δ\_Z×D(Y) is not contained in D₂(Z×Y). For Y = A the two density conditions are D.2 and D.3.
- **Booleanization is optional in B.1.** With Z = E and its coordinate maps, the same argument gives D(E×Y) strictly below D(E)×D(Y). Booleanization only serves to put the right-hand side in the form Δ\_Z×D(Y).
- **The failure is already at the D₂ level.** B.1's witness lies outside D₂(Z×Y), so the conclusion can be stated as Δ\_Z×D(Y) ≰ D₂(Z×Y).
- **D₂ analogue.** B.1 holds verbatim with D₂ in place of D, using E₂ = D₂(Y) ∧ o(δ\_Y). §F is its instance for A.
- **What the converse really uses.** (2)⇒(1) needs only a nonzero T and a pair (f, g): T → D(Y) whose graphs have disjoint closures in T×Y. A closed diagonal gives this from eq(f, g) = 0. Sierpiński space shows that some hypothesis is needed; I did not look for the weakest one.
- **Shorter proof.** I do not see a materially shorter proof of B.1 than the graph argument. The direct cover {U\_f, U\_g} is the same argument with the closure of the graph written out.

## Proof obligations still open

Seven items remain for independent verification. Only the first two affect the packet's own proof; the others concern arguments introduced in this report.

- [ ] Read the full proof of Arrieta's Proposition 4.1. I saw its statement and the first half of its proof only.
- [ ] Check the numbering (Construction 4.2, Corollary 4.3, Proposition 4.4, Example 4.5) against the published version, Topology and its Applications 342 (2024) 108785.
- [ ] Have a second reader check the direct cover U\_f ∨ U\_g = 1 in the "E.1" section. It is new here and removes the source dependence.
- [ ] Check the spatiality argument for the localic square of A, in particular that a countable meet of open sublocales of a compact Hausdorff space is spatial.
- [ ] Check the density lemma in "What the result does not imply", including that a rectangle of nonzero opens is nonzero in the frame coproduct.
- [ ] Supply definitions of W, W₂, U, Q, Q′ and re-verify (A.3) against them, including U.
- [ ] Check the Sierpiński computation D(Z×S) = Δ\_Z×S² for Boolean Z.

## Sources

- I. Arrieta, *Localic separation and the duality between closedness and fittedness*, [arXiv:2310.18522v1](https://ar5iv.labs.arxiv.org/html/2310.18522), §§2.5 and 4, read in the ar5iv rendering on 13 November 2026.
- `EXTERNAL_BLIND_PROMPT.md` and `EXTERNAL_BLIND_PACKET.md` from the supplied archive.
