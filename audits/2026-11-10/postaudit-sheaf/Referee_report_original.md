# Blind audit: coherent chain nerves and nonconstant sheaf homotopy (A1–E3)

Nov 10, 2026 · @Someone

No fatal error was found: all fifteen claims A1–E3 hold, three of them only after a stated repair. The repairs are a definition fix in B1 (the literal reading has a counterexample on ℝ), an argument for the join formula in C2, and a proof of the sheaf-level Hurewicz step in C3 and D3.

One post-audit finding changes the packet's open question. For S = βN and T = βN/(a\~b), the full objects h(S)₊ ∧ S^m and h(T)₊ ∧ S^m are equivalent for every m ≥ 1, so the unmarked homotopy object cannot recover S. That argument is mine and unreviewed; it sits in the Post-audit section, not among the checked claims.

## Issue ledger

Seventeen issues: no fatal, three repairable gaps, eight minor, three literature, three presentation. Section references such as "Key verifications 4" point to the numbered arguments below.

| # | Severity | Where | Issue | Counterexample or exact repair |
| --- | --- | --- | --- | --- |
| 1 | Repairable gap | §0 → B1, Ch half | §0 defines the specialization sublocale A\_X by π₀\*k ≤ π₁\*k for compact opens k only. B1 is stated for arbitrary locales, where that condition can be empty. | Counterexample under the literal definition: ℝ has no nonzero compact open, so Ch₁(ℝ) = ℝ². With u\_i = (i−1, i+1), the join of the w\_i is the union of the squares u\_i × u\_i, which misses (0, 5). Repair: impose π\_j\*u ≤ π\_{j+1}\*u for every open u, or for a base. For coherent X this is the same sublocale and the B1 proof then runs verbatim. The D half needs no change. |
| 2 | Repairable gap | C2 | "Hence C(P⊕Q) ≃ C(P) \* C(Q)" passes from the levelwise simplicial join to the homotopy join inside the ∞-topos with no argument. | The formula is true. Proof in Key verifications 4: the classical comparison for simplicial sets, applied objectwise in presheaves, then sheafified. |
| 3 | Repairable gap | C3, D3 | "Internal Hurewicz" is used with no proof or reference, in a Čech sheaf ∞-topos that need not be hypercomplete. | True for m ≥ 2, and for m = 1 with the sheaf abelianization. Proof in Key verifications 6; it uses only exactness of sheafification. Also say that π\_m is taken at a global base point. |
| 4 | Minor | Prerequisite, D3 | The crosscut criterion asks that "the intersections of principal downsets at maximal points" be contractible. For P\_m the intersection over all m+2 facets is empty, so the hypothesis as written fails for the poset D3 uses. | Insert "nonempty". With that the criterion applies, and I verified the conclusion for P\_m directly (Key verifications 8). |
| 5 | Minor | A2 | The pushout 1 ⊔\_{h(S)} 1 is read off a two-element closed cover. After realization the maps C(Z\_p) → C(X) need not be monomorphisms, so the Čech nerve does not visibly collapse to a pushout there. | Collapse levelwise first: h(Ch\_n Z\_p) and h(Ch\_n Z\_q) are subobjects covering h(Ch\_n X), and a union of two subobjects is the pushout over their intersection. Then commute the two colimits. |
| 6 | Minor | A3, D3 | Point values of sections of the sheafified M\_S are computed in ℤ\[S\] without saying why M\_S(∗) is the free group on the set S. The point s₀ is never introduced. | Every cover of ∗ splits, so evaluation at ∗ commutes with sheafification and with all colimits (Key verifications 3). This is stronger than the §0 remark about realizations. Add "fix s₀ ∈ S". |
| 7 | Minor | B3 | Both sufficiency statements are asserted without proof. "SNC" is undefined. The case u = 0 must be excluded. | Greatest point g of U: appending g is an extra degeneracy on Ch\_•(U) and on D\_•(X) ∩ U^{•+1}, since a lower witness z satisfies z ≤ x₀ ≤ g. Both sides are then terminal. Under (LB)\_u the relative hull is U^{•+1}, a Čech nerve, so the comparison is C(U) → 1. |
| 8 | Minor | §0 site | "Closed under necessary finite products and coproducts" is not enough. Čech nerves and pullback-stability of covers need fibre products. | Say "closed under finite limits and finite coproducts". κ-small Stone spaces satisfy this. |
| 9 | Minor | B1 | The Joyal–Tierney statement is correct but degreewise and purely localic. Nothing homotopical follows for infinite covers or non-coherent X, where Patch is undefined; B2 uses only finite compact-open covers. The closing sentence refers to a projection E → D that the packet never defines. | Scope B1 as a frame identity plus open-cover gluing. Define E → D and cite the failing example, or drop the sentence. I could not check that sentence from the packet. |
| 10 | Minor | E2 | Three steps are skipped: G\_S is a subsheaf; M\_S → M\_{S\_i} is a coalgebra map; group-likeness over a test space R can be tested pointwise. | x ↦ x⊗x is a natural map of sheaves of sets, so G\_S is an equalizer. The coalgebra map is naturality of ℤ\[−\] on diagonals. For finite S\_i the sheaf M\_{S\_i} and its tensor square are constant, so equality of sections is pointwise. |
| 11 | Minor | A1 | "Clopen upsets distinguish incomparable pairs" understates Priestley separation, which is required for every x ≰ y, including p ≰ s. | The listed clopen upsets do separate all such pairs; {p} separates p from every s. Reword only. |
| 12 | Literature | Sources, A3 | "Commelin–Scholze, Lectures on Condensed Mathematics, Proposition 2.5" is paired with the URL math.commelin.net/files/LTE.pdf. The title is that of Scholze's 2019 Bonn notes; the file name points to the Liquid Tensor Experiment. I could not open the URL. | Cite Scholze, Lectures on Condensed Mathematics (results joint with Clausen), Theorem 2.2 and its proof. Other papers cite that theorem for exactly this sheafification adjunction. |
| 13 | Literature | E1 | The Clausen–Scholze citation checks out: Proposition 3.3 on p. 25, Proposition 3.5 and Question 3.6 on p. 26, with the βN example after the question. The notes give no proof, and do not say the quotient is profinite or non-homeomorphic to βN. | Keep the citation and add the short proof (Key verifications 9). The packet's own argument that T is Stone and not extremally disconnected is correct. |
| 14 | Literature | Sources, prerequisite | arXiv:2610.14783 exists: P. J. Cameron and Vinod Kumar P. B., Graphs on Topological Spaces, 32 pages, math.GN. I could not open the paper, so the §9 attribution is unverified. The criterion itself is classical. | Credit the crosscut theorem (Rota, Folkman, Björner), the nerve lemma (Borsuk), McCord for finite spaces and Dowker for I ≃ D. Cite §9 only for what it adds. |
| 15 | Presentation | Whole packet | Heavy symbol overloading: S, P, Z, A, K and O each carry two to four meanings. | Rename; list in the Notation section. |
| 16 | Presentation | A and C versus D | Σ is the unreduced suspension in A and C. D uses the reduced half-smash h(S)₊ ∧ S^m without comment. "(m−1)-connected" is not tied to a convention. | State both conventions once. (m−1)-connected here equals m-connective in Lurie's indexing. |
| 17 | Presentation | E3 caveat | "Has not been shown to be intrinsic" is weaker than what is true. | The diagonal coalgebra cannot be an invariant of the unmarked object (Post-audit 1). |

## Claim-by-claim verdicts

Every claim is correct as mathematics; B1, C2 and C3 need the repairs in issues 1–3 before their proofs are complete. "Proved here" means I re-derived the claim from the packet's §0 conventions without using the packet's proof.

| Claim | Verdict | Basis | Notes |
| --- | --- | --- | --- |
| §0 conventions | Correct | Proved here | Hulls are proconstructible with the stated points. Site needs finite limits (issue 8). |
| Edgewise arrow theorem | Accepted as premise | Not re-proved | Consistent with Dowker duality and with three direct D-side computations (A2, C2, and Post-audit 2). |
| Closed-side codescent | Correct | Proved here | The levelwise cover check is two lines; the restriction to compact-open complements is not needed for it. |
| A1 | Correct | Proved here | Wording of separation only (issue 11). |
| A2 | Correct | Proved here | D(X(S)) ≃ 1 also follows directly from the C2 extra degeneracy, without the premise. Issue 5. |
| A3 | Correct | Proved here | Nonconstancy argument is sound once M\_S(∗) = ℤ\[S\] is stated (issue 6). "Constant iff S finite" holds in both directions. |
| B1 | Correct after repair | Proved here | D half holds for all locales as written. Ch half needs the definition fix (issue 1). Descent sentence is standard and correct (issue 9). |
| B2 | Correct | Proved here | Charts are patch-clopen, jointly surjective levelwise, and intersect as claimed. |
| B3 | Correct | Proved here | All three equivalences hold; sufficiency statements proved by extra degeneracy (issue 7). |
| C1 | Correct | Proved here | Realize the bisimplicial diagram one direction at a time. The warning about I and D is right. |
| C2 | Correct after repair | Proved here, using one cited comparison | Join formula needs Key verifications 4 (issue 2). Both extra degeneracies are spectral maps and contract I and D inside the ∞-topos. |
| C3 | Correct after repair | Proved here | Needs C2 and the Hurewicz proof (issue 3). Homology computation and the cofiber are right. |
| D1 | Correct | Proved here | Minimality of v is used twice, for transitivity and for separation. |
| D2 | Correct | Proved here | Both hull descriptions stay fiberwise; the squares are sheaf pushouts along a coproduct summand. The warning about D\_n(W) is right. |
| D3 | Correct | Proved here | C → I verified directly for P\_m. C → D follows from the premise, and also directly (Post-audit 2). Issue 4. |
| E1 | Correct | Citation confirmed, and isomorphism re-derived here | The published notes state the isomorphism without proof. Non-homeomorphism proved in the packet and re-checked. |
| E2 | Correct | Proved here, independently of the cited Proposition 3.3 | The monomorphism into the inverse limit is available on this site, both by citation and by a direct lemma (Key verifications 10). |
| E3 | Correct | Proved here | Cocommutativity is not needed. The caveat is right and can be strengthened (issue 17). |

## Key verifications

These ten arguments carry the verdicts where the packet is silent or brief. Throughout, H is the sheaf ∞-topos on Stone\_κ, L is sheafification, and h is the Yoneda embedding, which lands in sheaves because surjections of compact Hausdorff spaces are quotient maps.

### 1. The hulls are the stated proconstructible sublocales (§0)

- **Closure.** A tuple lies in cl(Δ) iff compact opens k\_i containing x\_i always have a common point. Patch compactness upgrades this to a point z in every compact open that contains some x\_i, which says x\_i ≤ z for all i.
- **Fitted hull.** X is compact, so every open containing Δ contains a compact open containing Δ. Hence fit(Δ) is a meet of patch-clopen sublocales, and its patch is the intersection of the clopen upsets containing Δ, namely ↑Δ.
- **Meets.** The frame congruence generated by two lattice congruences on K(X) is generated by their join. So meets of proconstructible sublocales are intersections of patch-closed sets, and relative hulls such as D\_n(X) ∩ U^{n+1} are what the packet says.

### 2. Priestley closedness and separation, in detail

- **P(S).** The order graph is Δ ∪ S×{p} ∪ S×{q}, a closed set. An upset meeting S contains p and q, which gives the listed clopen upsets. For s ≠ s′ use U ∪ {p, q} with U clopen, s ∈ U, s′ ∉ U. The set {p} separates p from q and from every s.
- **P ⊕ Q.** The graph is ≤\_P ∪ ≤\_Q ∪ P×Q, closed. Inside P use V ∪ Q for a clopen upset V of P. Inside Q use a clopen upset of Q. Q itself separates a point of Q from a point of P.
- **W\_S(P, v).** The graph is {(v,v)} ∪ {v}×S×(↑v∖v) ∪ the union over x ≤ y of Δ\_S×{(x,y)}, closed. To separate (s,x) from (t,y) with s ≠ t, take f = ↑x on a clopen V containing s but not t, and f = ∅ elsewhere. The v-indicator of f is constantly 0 because v is minimal and x ≠ v. The remaining cases use the constant functions ↑x or ↑v.

Minimality of v is essential in D1. Without it, (s,x) ≤ v ≤ (t,y) would force comparisons across fibers.

### 3. Evaluation at the point is exact and commutes with sheafification

Any finite jointly surjective family over ∗ contains a map from a nonempty space, which has a section. So the only covering sieve of ∗ is the maximal one, and (LF)(∗) = F(∗) for every presheaf F. Evaluation at ∗ therefore preserves all colimits and finite limits.

Two consequences are used in A3, D3 and E2: M\_S(∗) is the free abelian group on the set S, and (M\_S ⊗ M\_S)(∗) = ℤ\[S×S\].

### 4. The join formula in C2 (repair for issue 2)

Write A = h(Patch Ch\_• P) and B = h(Patch Ch\_• Q), both augmented by the terminal object.

1. For simplicial sets K and L, the natural map from the homotopy pushout of K ← K×L → L to the join of K and L is a weak equivalence (Lurie, HTT 4.2.1.2).
2. The same holds for simplicial spaces, applied in each degree of the second simplicial direction, because realization commutes with pushouts and finite products.
3. Hence it holds objectwise for simplicial presheaves on Stone\_κ.
4. L preserves colimits and finite products. It turns the presheaf join of the representables into h(Patch Ch\_•(P⊕Q)), because h preserves finite coproducts and Ch\_n(P⊕Q) is the disjoint union of the clopen pieces Ch\_i(P) × Ch\_j(Q) with i + j = n − 1.

So the realization of the levelwise join is the pushout of C(P) ← C(P)×C(Q) → C(Q) in H. Nothing is evaluated at the terminal object.

### 5. The extra degeneracies in C2 are genuinely localic

Inserting p₀ is the restriction of a map X^{n+1} → X^{n+2} built from identities and a constant map, and constant maps at a point are spectral. Hulls and domains are spatial sublocales, so pointwise factorization suffices. The case analysis for both witnesses is right.

After applying h, the augmented simplicial object is split in H. Split augmented simplicial objects are colimit diagrams in any ∞-category, so I(P⊕Q) and D(P⊕Q) are terminal in H itself.

### 6. Hurewicz at the level of sheaves (repair for issue 3)

Let Y be a pointed, (m−1)-connected object of H. Let Y′ be the fibre at the base point of Y → τ\_{≤m−1}Y, both computed in presheaves.

1. Y′ is objectwise (m−1)-connected.
2. L(Y′) is the fibre of Y → τ\_{≤m−1}Y in H, which is Y. This uses that L is left exact and commutes with truncation.
3. Homotopy sheaves and homology sheaves of L(Y′) are the sheafifications of the objectwise homotopy and homology groups of Y′.
4. Classical Hurewicz is natural, so π\_m ≅ H̃\_m objectwise for m ≥ 2, and the abelianization of π₁ is H₁ for m = 1.

The argument uses only exactness of L, so it holds with or without hypercompletion. For m ≥ 2 the object is simply connected with a global point, so π\_m is a sheaf of abelian groups on H itself.

### 7. The D2 squares are sheaf pushouts

h(S × Ch\_n P) is the coproduct of h(S×{v\_n}) and h(S × (Ch\_n P ∖ v\_n)). In any category with coproducts, the pushout of 1 ← A → A ⊔ B is 1 ⊔ B. And 1 ⊔ h(S × (Ch\_n P ∖ v\_n)) is h(Patch Ch\_n W).

So each square is a pushout in H, naturally in n, and no quotient pushout of Stone spaces is used. The same holds for I\_n. The upper-witness relation stays fiberwise because an upper bound of (s,x) lies in the fiber s, and nothing but v lies below v.

### 8. The crosscut step for P\_m, checked directly

The facets are F\_i = \[m+1\] ∖ {i}. For a proper nonempty set J of indices, the intersection of the downsets ↓F\_i over i ∈ J is ↓(\[m+1\] ∖ J), which has a greatest element.

The nerve N(P\_m) is the union of the N(↓F\_i), and I\_•(P\_m) is the union of the simplicial sets of all tuples in ↓F\_i. Both unions are homotopy colimits over the same poset of proper nonempty J. The pieces are cones on one side and tuple complexes of nonempty sets on the other, all contractible. So N(P\_m) → I\_•(P\_m) is an equivalence.

### 9. E1 re-derived: ℤ\[βN\] ≅ ℤ\[T\]

Let S be Stone, a ≠ b in S, and T = S/(a\~b).

1. S ×\_T S is the disjoint union of the diagonal and the two isolated points (a,b), (b,a). So h(T) is the quotient of h(S) by the relation a \~ b. This one pushout is checked by hand, not inferred from Yoneda.
2. Applying the free functor, ℤ\[h(T)\] = M\_S / ℤ·(\[a\] − \[b\]).
3. Pick a clopen V with a ∈ V and b ∉ V. Its indicator function gives a map M\_S → ℤ sending \[a\] − \[b\] to 1. Hence M\_S ≅ ℤ\[h(T)\] ⊕ ℤ.
4. For S = βN, write βN = {0} ⊔ cl(N∖{0}) and let θ be the shift homeomorphism from cl(N∖{0}) to βN. Then T ≅ pt ⊔ T₁ with T₁ = βN/(θa \~ θb).
5. So ℤ\[h(T)\] ≅ ℤ ⊕ ℤ\[h(T₁)\], which is M\_{βN} by step 3 applied to the pair (θa, θb).

This holds for every pair of distinct remainder points. The packet's proof that T is Stone and not extremally disconnected is correct: the closure of the image of V ∖ {a} is the image of V, whose preimage V ∪ {b} is not open.

### 10. E2 without Proposition 3.3: sections of M\_S are determined by point values

**Lemma.** A section x of M\_S over R whose value at every point of R is zero is zero.

1. On some cover R′ → R, x is a finite sum of n\_k\[g\_k\] with g\_k continuous.
2. For each partition of the index set whose blocks have coefficient sum zero, let R\_π be the closed set where g\_k = g\_l whenever k and l share a block.
3. Pointwise vanishing says the finitely many R\_π cover R′. On each R\_π the sum is already zero in the presheaf. So x vanishes on a cover.

**E2 from the lemma.** A group-like x has group-like point values in ℤ\[S\], so x(r) = \[f(r)\] for a function f. The image of x in each finite quotient M\_{S\_i} is locally constant, so f is continuous. Then x and \[f\] have the same point values and are equal.

The lemma also gives the monomorphism from M\_S into the inverse limit of the ℤ\[S\_i\] on this site, which is what the packet takes from Clausen–Scholze.

## Provenance

Fourteen of the fifteen claims were proved here from §0 alone; only the C → D half of D3 was first taken from the premise, and it too has a direct proof in Post-audit 2.

**Proved independently in this audit.** A1, A2, A3, B1 (with the definition fix), B2, B3, C1, C2, C3, D1, D2, the C → I half of D3, E1 (both the isomorphism and the non-homeomorphism), E2 and E3. Also the §0 hull descriptions and the closed-side codescent prerequisite.

**Standard theorems used as inputs, recalled from memory and not re-read in this session.**

- Priestley duality and the prime ideal theorem.
- Lurie, Higher Topos Theory: Čech nerves of effective epimorphisms, universality of colimits, realization commuting with finite products, split augmented simplicial objects, the join comparison 4.2.1.2, and truncation commuting with left exact localization. Theorem numbers are from memory.
- The classical Hurewicz theorem and the classical nerve lemma.
- Joyal–Tierney descent, needed only for the wording of B1; the frame identity itself is elementary.

**Accepted conditionally.**

- The canonical edgewise arrow theorem, as the prompt instructs. I did not re-prove it. Every use of it in this packet can be bypassed (Post-audit 2), and the direct computations agree with it.
- The sentence in B1 that the lower-witness projection fails unpatched descent. The packet gives neither the object nor the example.
- Cameron and Vinod Kumar §9 and the LTE.pdf reference. I could not open either. Neither is needed for any verdict above.

**How the Clausen–Scholze text was read.** Through a fetch tool that summarizes the first part of the PDF, not by reading the raw pages. Statement numbers and page numbers are as that tool reported them. The mathematical content of the cited example was then re-derived, so no verdict rests on the summary.

**Blindness.** I used only the prompt and the packet. One web search for the Cameron–Kumar citation returned a results snippet from a GitHub repository named mkkinyon/locales. I did not open it and used nothing from it.

**Speculative material** is confined to the Post-audit section.

## Notation and first-reading confusions

The mathematics is easier than the notation: six letters are reused with unrelated meanings, and four terms are never defined.

| Symbol or phrase | Meanings in the packet | Suggested fix |
| --- | --- | --- |
| S | Stone space; index subset in U\_S (B2); sphere S^m | Use J for index sets |
| P | Patch space (§0); P(S) (A); coherent locales P, Q (C2); finite poset (D) | Keep P for the finite poset only |
| Z | Closed downsets Z\_i, Z\_p; a coherent locale in C3; the integers | Use Y for the locale in C3 |
| A | Antichain; specialization relation A\_X; generic objects in A \* B | Rename the relation, for example Sp\_X |
| K | Lattice K(X); kernel sheaf in C3; complex K\_up(P) | Rename the kernel sheaf |
| O | Frame of X in two typefaces; open sublocale O(u), O(w) | Write o(u) for open sublocales |
| Σ | Unreduced in A and C; reduced smash in D | Say which, once |
| C(X)/H | Undercategory, written like an overcategory | Write H with subscript C(X)/ |
| SNC, LB | Undefined acronyms in B3 | Define, or write the condition out |
| unmarked | Used in the prompt and E1 before any definition | Define at first use: the bare sheaf, without coalgebra structure |
| sub-constructible | Nonstandard (D2) | Proconstructible |
| E → D | Lower-witness projection, referenced in B1, never defined | Define or delete |
| Finite k-fiber controls | Obscure phrase in D3 | "For finite S with k points" |
| nonempty face poset | Means the poset of nonempty faces | Reword |

Three further points slowed the first reading.

- I\_n and D\_n are indexed by n but defined from Δ\_{n+1}. The remark "index n means arity n+1" helps, but Δ could carry the arity directly.
- "Length-(n+1) chain" in C2 means an n-simplex, that is, n+1 points with repetition allowed. Ch\_n(P) for finite P likewise includes degenerate chains.
- R with superscript ↓ and H\_n with superscript X,↓ denote the realization and the levelwise relative hull of the same object. One sentence linking them would help.

## Literature attribution and originality boundary

Every ingredient is standard; what looks specific to the packet is the choice of examples and their assembly inside the patched chain and hull framework. I made no priority search beyond checking the three citations, so I do not certify novelty either way.

| Ingredient | Used in | Standard attribution | Checked this session |
| --- | --- | --- | --- |
| Ordered Stone spaces and distributive lattices; spectral spaces and the patch topology | §0, A1, C2, D1 | Stone; Priestley (1970); Hochster (1969) | No, recalled |
| Closed and fitted sublocales; coherent locales | §0, B1 | Isbell (1972); Johnstone, Stone Spaces; Picado–Pultr | No, recalled |
| Effective descent for open surjections of locales | B1 | Joyal–Tierney (1984) | No, recalled |
| Upper-witness and lower-witness complexes are equivalent | Premise | Dowker (1952), homology of relations | No, recalled |
| Order complex versus cover nerve | Premise, D3 | Crosscut theorem: Rota, Folkman, Björner; nerve lemma: Borsuk | No, recalled |
| Two-apex suspension, layered spheres, ordinal sum as join | A, C2, C3 | McCord (1966), non-Hausdorff suspension and join; Quillen (1978); Barmak's monograph on finite spaces | No, recalled |
| Edgewise subdivision | Premise | Segal (1973); Bökstedt–Hsiang–Madsen | No, recalled |
| Čech descent, universal colimits, split simplicial objects, join comparison | A2, B2, C1, C2, D2 | Lurie, Higher Topos Theory | No, recalled |
| Condensed sets, free condensed abelian groups | §0, A3, E | Clausen–Scholze; Scholze's 2019 notes, Theorem 2.2; Barwick–Haine for the pyknotic variant | Partly: see the next three rows |
| ℤ\[S\] as a union of bounded profinite pieces | E2 | [Clausen–Scholze, Complex Geometry notes](https://people.mpim-bonn.mpg.de/scholze/Complex.pdf), Proposition 3.3 | Yes, statement and page confirmed |
| ℤ\[βN\] ≅ ℤ\[βN/(a\~b)\] | E1 | Same notes, example after Question 3.6 | Yes, confirmed; the notes give no proof |
| Finite-poset homotopy criterion | Premise | Packet cites Cameron and Vinod Kumar, arXiv:2610.14783, §9 | Paper exists; §9 not read |
| Group-like elements of a group-ring coalgebra are the basis | E2, E3 | Classical Hopf-algebra fact; Sweedler (1969) | No, recalled |
| Non-homeomorphic compact spaces with isomorphic free (abelian) topological groups | E1, Post-audit 1 | Markov; Graev (1948); Okunev's retract method (1990) | No, recalled |

Two citation points need action.

- **"Commelin–Scholze, Proposition 2.5".** Title, authors and URL do not match each other (issue 12). The sheafification adjunction is Theorem 2.2 of Scholze's Lectures on Condensed Mathematics, as cited for example in [arXiv:2109.07816](https://arxiv.org/pdf/2109.07816), Proposition 2.16.
- **Clausen–Scholze.** The 2022 notes carry the title "Liquid vector spaces, redux" for Lecture III. An arXiv version, 2605.11731, now exists; I did not compare its numbering, so keep citing the notes by statement number and add the arXiv identifier.

The last table row matters for attribution. The phenomenon in E1, and its nonabelian strengthening in Post-audit 1, is the condensed form of what the free-topological-group literature calls A-equivalence and M-equivalence of spaces.

## Post-audit: new suggestions, not checked claims

Nothing in this section was part of the packet, and none of it has been reviewed by anyone else. Item 1 answers the packet's closing open question in the negative; items 2 and 3 are simplifications; items 4 and 5 are remarks.

### 1. The unmarked homotopy object does not recover S

**Claim.** Let a, b be distinct remainder points of βN and T = βN/(a\~b). Then h(βN)₊ ∧ S^m and h(T)₊ ∧ S^m are equivalent pointed objects of H for every m ≥ 1.

**Proof sketch.**

1. For any Stone S, the reduced suspension of h(S)₊ is B Fr(h(S)), where Fr is the free sheaf of groups. Objectwise the suspension of Cont(R,S)₊ is a wedge of circles, the classifying space of the free group on Cont(R,S), naturally in R. Sheafification commutes with suspension and with B.
2. **Lemma F.** For Stone S, points a ≠ b and T = S/(a\~b), there is an isomorphism Fr(h(S)) ≅ Fr(h(T) ⊔ 1). Choose a clopen V with a ∈ V, b ∉ V. Write π for the quotient map and t for the generator from the extra point. The two maps are displayed below.
3. Φ is well defined on h(T): both branches give \[b\] at the glued point, and h(T) is the quotient of h(S) by a \~ b (Key verifications 9, step 1). Both composites are the identity on generators.
4. For S = βN, the shift trick of Key verifications 9 gives T ≅ pt ⊔ T₁. So Fr(h(T)) ≅ Fr(h(T₁) ⊔ 1) ≅ Fr(h(βN)) by Lemma F for the pair (θa, θb).
5. Apply B, then suspend m − 1 more times.

```latex
\Psi[x]=\begin{cases} t\,[\pi x] & x\in V\\ [\pi x] & x\notin V\end{cases}
\qquad
\Phi(t)=[a][b]^{-1},\qquad
\Phi[\pi x]=\begin{cases} [b][a]^{-1}[x] & x\in V\\ [x] & x\notin V\end{cases}
```

Abelianizing Lemma F returns the splitting in Key verifications 9, so the Clausen–Scholze example is its shadow.

**Consequences, if the sketch holds.**

- C(X\_m(βN)) ≃ C(X\_m(T)) for every m ≥ 1, with both canonical comparisons equivalences on each side. The locales X\_m(βN) and X\_m(T) are not isomorphic: their closed sets of minimal points are extremally disconnected in one case and not in the other.
- The sentence "full homotopy-object reconstruction remains unproved" can be replaced by "fails for this pair".
- The diagonal coalgebra on M\_S is provably not an invariant of the unmarked object. The objects for βN and T are equivalent, while E3 shows their coalgebras are not isomorphic. This sharpens the E3 caveat (issue 17).
- The same holds for the C3 objects. Since βN ≅ pt ⊔ βN, the unreduced suspension of h(βN) is the reduced suspension of h(βN)₊, and likewise for T and T₁.

### 2. The D side needs no edgewise theorem in this packet

- **Ordinal sums.** C2 already contracts D(P⊕Q) by a direct extra degeneracy. A2 is the case S ⊕ A, so A2 and C3 never need the premise.
- **W\_S(P, v).** D\_n(W) is the union of two closed simplicial pieces. A\_n holds v\_n and the single-fiber tuples whose image in P has a lower witness. B\_n holds all tuples in U\_v = {v} ⊔ S×(↑v∖v). Their realizations are h(S)₊ ∧ D(P), the terminal object, and for the intersection the terminal object again. Hence D(W) ≃ h(S)₊ ∧ D(P), compatibly with C(W).
- **P\_m.** Upsets of vertices intersect in the upset of the face they span, or in the empty set. The dual of Key verifications 8 then shows C(P\_m) → D(P\_m) is an equivalence.

So the three applications can serve as independent tests of the edgewise theorem instead of depending on it.

### 3. For m = 1 the objects are 1-truncated

By step 1 above, the D3 object for m = 1 is B Fr(h(S)), and the A2 object is B of Fr(h(S)) modulo the normal closure of \[s₀\]. Sheafification preserves truncated objects, so nothing higher appears.

D3 can therefore state π₁ itself, the free sheaf of groups on h(S), not only its abelianization.

### 4. Why the coalgebra has to be extra data

The chains of any object carry a coalgebra structure from the object's own diagonal. On a suspension the reduced diagonal is null, so every class in the bottom reduced homology is primitive. The intrinsic structure on M\_S is therefore the trivial one, never the group-like one. I state this as the standard fact; I did not write out the internal proof.

The group-like structure is visible one step earlier. For a Stone space S with trivial order, Ch\_n(S) = S, so C(S) = h(S), which recovers S by Yoneda. The information is lost at the first suspension.

### 5. Speculative questions

- Which Stone spaces S are determined by Fr(h(S)), or by M\_S? Lemma F only shows that gluing two points changes nothing once S ≅ S ⊔ pt.
- Is there a C = I = D example whose common realization is nonconstant and is not a suspension? Item 4 suggests that only such an example could carry intrinsic group-like structure.

## Sources

Only the first source was opened; the others were seen as search-result excerpts or could not be reached.

- [Clausen and Scholze, Condensed Mathematics and Complex Geometry](https://people.mpim-bonn.mpg.de/scholze/Complex.pdf), 2022 notes. Opened through a summarizing fetch of the first part of the file. Used for Propositions 3.3 and 3.5, Question 3.6 and the βN example.
- [arXiv:2605.11731](https://arxiv.org/pdf/2605.11731), the arXiv version of the same notes. Search result only; numbering not compared.
- [Scholze, Lectures on Condensed Mathematics](https://www.math.uni-bonn.de/people/scholze/Condensed.pdf). Search result only. Suggested replacement for the "Commelin–Scholze" citation.
- [arXiv:2109.07816](https://arxiv.org/pdf/2109.07816), Proposition 2.16. Search excerpt showing the free-group adjunction cited to Theorem 2.2 of Scholze's notes.
- [Peter Cameron's arXiv listing](https://arxiv.org/a/cameron_p_1.html) and [his blog](https://cameroncounts.wordpress.com/). Search excerpts confirming arXiv:2610.14783, its title, authors and length. The listing page itself returned an older snapshot when opened.
- Not reachable from this session: math.commelin.net/files/LTE.pdf and the arXiv abstract page for 2610.14783.