# Referee report — Project A, SC+ theorem (blind packet of 15 Nov 2026)

Nov 14, 2026 · @Someone

## Verdict

Theorem 5.1 (SC+) is correct as stated: it holds for every stably locally compact locale, compact or not, in classical locale theory. I found no counterexample to Lemma 3.1, Proposition 4.1, Lemma 4.2 or formula (4.3), and I proved each of them independently. The repairs below are expository; none changes the scope of a conclusion.

Notation in this report: S, M, I, D, A stand for the packet's script-letter sublocales. pt(–) is the set of points, \[B\] the sublocale induced by a subset B, and o(u), c(u) the open and closed sublocales of an open u.

| Claim | Status | Comment |
| --- | --- | --- |
| (1.1) Δ ≤ S ≤ M, all locales | Correct after a one-line repair | The proof of A ≤ D treats only square-cover opens (issue 1) |
| §2 patch facts 1–4, noncompact case | Correct | Re-derived by adjoining a bottom point |
| §2 products and closed subspaces | Correct | Under-justified where Prop. 4.1 leans on it (issue 2) |
| Lemma 3.1, pointwise identity (3.2) | Correct | Also provable without the patch topology |
| Lemma 3.1, nucleus-join step | Correct | Uses only the trivial inequality |
| Lemma 3.1, formula (3.1) | Correct |  |
| Prop. 4.1, (4.1) and (4.2) | Correct | (4.2) can be bypassed |
| Lemma 4.2 | Correct |  |
| Formula (4.3) | Correct |  |
| Theorem 5.1 | Correct | Two point facts are unstated (issue 3); "only if" holds for all locales |
| §6 sequence control | Valid | It does not exercise Lemma 3.1 (issue 5) |
| Lemma 3.1, Lemma 4.2 and Theorem 5.1 without "stably" | False | Counterexamples under Controls |

Limits of this review: every check is a hand proof, with no machine verification. I could not open reference 1 (Tix–Keimel–Plotkin) or reference 4 (the Project A definitions file), so I worked from the packet's own definitions. I have not seen the internal audit.

## Ranked issues

No issue is fatal. Issues 1 and 2 are proof gaps to close; the rest concern wording, scope and test design.

1. **(1.1): the proof of A ≤ D covers only square-cover opens. Gap, one-line repair.** D is the meet of o(w) over all w with δ\*(w) = 1, but the packet checks only w = w\_C for covers C. Repair: write w = ⋁ aᵢ ⊠ bᵢ. Then ⋁ (aᵢ ∧ bᵢ) = δ\*(w) = 1, so C = {aᵢ ∧ bᵢ} is a cover and w\_C ≤ w. Square-cover opens are thus coinitial among open neighbourhoods of Δ, and the packet's argument gives A ≤ D.
2. **Prop. 4.1: "Y is stably locally compact" is asserted, not shown, for noncompact X. Justification gap.** The step leans on §2's sentence that finite products stay in the class. That needs two facts beyond the compact theory: the pospace correspondence for noncompact spaces, and that the upper topology of the product pospace is the product topology. Both are true. Smallest repair: prove the lifting lemma given under Verification §2, then inherit facts 1–3, products and the coordinatewise patch from the compact case.
3. **Theorem 5.1: two facts about points are used silently. Minor.** First, pt(S) = pt(A) ∪ pt(A˘) needs points to be join-prime for binary joins. That is true: a prime p = a ∧ b with a ∈ A, b ∈ B forces p = a or p = b. Second, "M and S have the same points" needs pt(\[P\]) = P, and an induced sublocale can have more points than the set inducing it. Here pt(M) = pt(I) ∩ pt(D) = P, so the claim holds. Cleaner wording: M = \[P\] is the least sublocale containing P, and P ⊆ pt(S), so M ≤ S.
4. **The scope statement in §6 is too cautious in one direction and too weak in the other. Minor.** The "only if" half of (5.1) needs no hypothesis on X. The "if" half needs stability: §6 says local compactness alone would not justify the argument, but the statements themselves are false there. Recommended: say both, and cite the examples X₁ and T under Controls.
5. **The §6 sequence control cannot detect an error in Lemma 3.1. Test design.** In that space pt(I) is exactly the set R of comparable pairs. Hence I = \[R\] ≤ S ≤ M ≤ I, and S = M follows without any reference to D. Supplement it with the tent control below, where I is the whole square and M = D.
6. **Notation and citation slips. Cosmetic.** Listed under "Simplifications and first-reading notes" and "References".

## Verification, section by section

Every displayed equation and assertion in §§1–6 checks out. This section records the reasoning, including the two arguments I had to add.

### §1 Definitions and (1.1)

- **Diagonal.** δ\*(a ⊠ b) = a ∧ b is onto, so Δ ≅ X is a sublocale. When Y is spatial, it is the sublocale induced by the diagonal subset.
- **Complement of I.** The closure of Δ is c(d) for the largest d with δ\*(d) = 0. Any a ⊠ b ≤ d has a ∧ b = 0, so d = d\_I.
- **A exists.** It equals ⋀ₐ (c(a₁) ∨ o(a₂)). Its points are the pairs (x, y) such that every open neighbourhood of x contains y, which is x ≤ y in the packet's convention.
- **(1.1).** Δ ≤ A is clear and A ≤ I is as in the packet. A ≤ D holds after the repair in issue 1. I and D are symmetric, so S = A ∨ A˘ ≤ I ∧ D.
- **Induced sublocales.** \[B\] has nucleus w ↦ int(w ∪ (Z∖B)), is the least sublocale containing the points of B, and satisfies \[B\] ≤ o(u) iff B ⊆ u.

### §2 Patch background in the noncompact case

All four facts hold without compactness, and one lemma delivers them together.

**Lifting lemma.** Let Z be stably locally compact. Form Z⊥ by adding a point ⊥ whose only neighbourhood is the whole space. Then Z⊥ is stably compact: it is sober and locally compact, and its compact saturated sets are those of Z together with Z⊥. Z is an open upper subset of Z⊥, and patch(Z) is the subspace Z of patch(Z⊥), open because {⊥} is patch-closed.

- **Fact 1.** patch(Z) is an open subspace of a compact Hausdorff pospace.
- **Fact 2.** A patch-open upper subset of Z is patch-open and upper in Z⊥, hence open.
- **Fact 3.** A compact saturated K ⊆ Z is patch-closed in Z⊥, hence patch-compact.
- **Fact 4.** This is local compactness.
- **Direction of "properly".** Compactness of the upward closure ↑K is the right condition for the packet's order convention. Downward closure fails: in the §6 control, ↓({xₙ} ∪ {x}) contains every zₙ.
- **Converse.** For a properly locally compact pospace Π, the one-point compactification with the new point as bottom has closed order. This is exactly where compactness of ↑K is used. So Π with its upper topology is an open subspace of a stably compact space.
- **Products.** Π × Π is again properly locally compact. Its upper topology is the product topology, because that holds in the compact pospace Π⊥ × Π⊥ and Π × Π is an open upper subset. So Y is stably locally compact, with patch(Y) = patch(X)² and coordinatewise order.
- **Closed subspaces.** For closed F ⊆ Z, the compact saturated subsets of F are the sets K ∩ F. So F is coherent, and patch(F) is the subspace F of patch(Z).

### §3 Lemma 3.1

Each step is valid.

- **Easy inequality in (3.2).** C ⊆ u gives Z∖u ⊆ Z∖C.
- **F = K∖w is patch-compact.** It is a patch-closed subset of the patch-compact K.
- **↓F is patch-closed.** The projection Z × F → Z is a closed map because F is compact. No compactness of Z is needed.
- **u = Z∖↓F is open.** It is patch-open and upper, so fact 2 applies.
- **C ⊆ u.** A point of C below some q ∈ F would put q in C ∩ V ⊆ w, contradicting q ∉ w.
- **z ∈ (u → w).** K ∩ u ⊆ w, so int K ⊆ (u → w).
- **Nucleus step.** Let k be the join of the nuclei j\_u. Then k ≤ j\_C, because j\_C is a nucleus above every j\_u. And k(w) ≥ ⋁ j\_u(w) = j\_C(w), because a join of nuclei dominates the pointwise join. Only this trivial direction is used, so referee instruction 4 finds nothing wrong here.
- **(3.1).** An open contains B iff it contains ↑B, so fit\[B\] = fit\[↑B\] = \[↑B\].

**A patch-free proof of the key step.** Let G = Z∖w and let K be a compact saturated neighbourhood of z inside V. I claim ↓(K ∩ G) is closed. Take p outside it, so ↑p ∩ K ⊆ w. ↑p is the filtered intersection of the compact saturated neighbourhoods Kᵢ of p, and each Kᵢ ∩ K is compact saturated by coherence. Well-filteredness gives some Kᵢ ∩ K ⊆ w. Then int Kᵢ is an upper open neighbourhood of p that misses ↓(K ∩ G). Now u = Z∖↓(K ∩ G) works as in the packet.

The side remark on perfectness is consistent: if C is patch-closed then j\_C is Scott-continuous, because K ∩ C is patch-compact. Nothing depends on it.

### §4 Proposition 4.1, Lemma 4.2 and (4.3)

- **Spatial product.** X is spatial classically, and the localic square is the spatial product because X is locally compact.
- **D = \[↑Δ\].** Lemma 3.1 applied to Y.
- **I.** It is the closed sublocale on the set of inseparable pairs, and is stably locally compact by §2.
- **(4.2).** Opens of I are restrictions of opens of Y. Since Δ ≤ I, the condition o(w) ∧ I ≥ Δ is the same as o(w) ≥ Δ. Meeting with the fixed I commutes with the meet over w.
- **Saturation inside I.** The subspace order is the restricted order, so the saturation is pt(I) ∩ ↑Δ and M = \[pt(I) ∩ ↑Δ\].
- **Lemma 4.2, easy direction.** Opens are upper sets.
- **Lemma 4.2, hard direction.** The sets K ∩ H are nonempty, filtered, and compact saturated by coherence. Their intersection is ↑x ∩ ↑y by local compactness. It is nonempty by patch compactness as in the packet, or by well-filteredness.
- **(4.3).** Follows from the two items above.

### §5 Theorem 5.1

- **"If".** P consists of comparable pairs, so P ⊆ pt(S). M = \[P\] is the least sublocale containing P, so M ≤ S. With (1.1), S = M.
- **"Only if".** A pair with r ≤ x, y ≤ s is a point of I and of D by direct inspection, in any locale. If S = M it is a point of S, hence comparable.

### §6 Cautions and the sequence control

- **The control is a properly locally compact pospace.** The order is closed because (zₙ) has no convergent subsequence. ↑K adds finitely many points to a compact K.
- **Its claims hold.** Intervals are chains, and (xₙ, yₙ) → (x, y) patchwise with (x, y) outside ↑Δ. So pt(D) is not patch-closed.

## Controls and boundary examples

Seven controls agree with the theorem inside its scope, and two examples show that it fails once stability is dropped. R denotes the set of comparable pairs.

| Control | Kind | Intervals are chains | pt(I) | pt(D) | Outcome |
| --- | --- | --- | --- | --- | --- |
| Diamond r < x, y < s | Finite | No | All pairs | All pairs | (x, y) is in pt(M) but not pt(S), so S ≠ M |
| Wedge x, y < s | Finite | Yes | All pairs | R | M = D = \[R\] = S |
| Vee r < x, y | Finite | Yes | R | All pairs | M = I = \[R\] = S |
| Spec ℤ | Spectral, compact | Yes | All pairs | R | M = D = \[R\] = S, and M ≠ I |
| Tent on \[−1, 1\] | Continuous domain, compact | Yes | All pairs | R = {(s, t) : st ≥ 0} | M = D = \[R\] = S, and M ≠ I |
| Tent on (−1, 1) | Noncompact | Yes | All pairs | R | Same as the compact tent |
| Packet's sequence space | Noncompact | Yes | R | R with the pairs (xₙ, yₙ), (yₙ, xₙ) | M = I = \[R\] = S |

- **Finite controls.** Every finite frame is spatial, so finite T0 spaces have only spatial sublocales. The point computations are complete proofs there.
- **Spec ℤ.** Closed points lie below the generic point η. Lemma 3.1 can be checked by hand for C = {η}: j\_C is double negation, and the meet of all nonempty open sublocales is the Booleanization {0, 1}, which is the point η.
- **Tent.** X = \[−1, 1\] with s ≤ t iff t lies between s and 0; opens are the Euclidean-open upper sets. This is a compact pospace, so X is stably compact, and Y is not scattered. The theorem predicts fit(Δ) = \[R\], a proper sublocale of I = Y. Here the conclusion rests entirely on Lemma 3.1.
- **Variant of the packet's control.** Add an isolated point t above x and y. Then (x, y) lies in pt(I), has no common lower bound, and is the patch limit of pairs (xₙ, yₙ) in pt(D)∖pt(I). Intervals stay chains, and the prediction is S = M = \[R\].

### X₁: SC+ fails for a compact, locally compact, sober space that is not coherent

Points: ⊥, a, p and gₙ for n ∈ ℕ. Open sets: X₁ itself, and every W not containing ⊥ such that a ∈ W implies all gₙ ∈ W, and p ∈ W implies all but finitely many gₙ ∈ W.

- **Order.** ⊥ is below everything and a < gₙ. There are no other strict comparisons.
- **Local compactness.** X₁, ↑a, the sets {p} ∪ {gₘ : m > n} and the singletons {gₙ} form a base of compact open sets. X₁ is compact.
- **Sobriety.** An irreducible closed set contains at most one gₙ, and cannot contain p together with a or some gₙ. So it is a point closure.
- **Not coherent.** ↑a meets {p} ∪ {gₘ : m > 0} in an infinite discrete set.
- **Intervals.** The only intervals with more than two points are the chains {⊥, a, gₙ}.
- **Failure.** Every neighbourhood of a contains all gₙ, and every neighbourhood of p contains some gₙ, so (a, p) is inseparable. It has the common lower bound ⊥. So (a, p) is a point of M. But a and p are incomparable, so it is not a point of S.

The same pair refutes Lemma 4.2 without coherence: a and p are inseparable and have no common upper bound.

In X₀ = X₁∖{⊥} the pointwise identity (3.2) fails for C = {p}, w = ∅, z = a. The left side is ↑a and the right side is {gₙ : n ∈ ℕ}. Yet {p} is still fitted in X₀, because applying the pointwise join twice recovers a. This is a concrete nucleus join that is not pointwise.

### T: Lemma 3.1 fails for a locally compact sober space that is not coherent

Points: all finite and infinite sequences of natural numbers, forming a set V, plus one extra point p\_s for each finite sequence s. Write ↑s for the set of sequences extending s. A set W is open iff W ∩ V is a union of sets ↑s with s finite, and p\_s ∈ W implies ↑(s⌢m) ⊆ W for all but finitely many m.

- **Order.** The prefix order on V. Each p\_s is comparable only to itself.
- **Local compactness.** The sets ↑s and {p\_s} ∪ ⋃{↑(s⌢m) : m > n} form a base of compact open sets.
- **Sobriety.** An irreducible closed set cannot contain two incomparable finite sequences, nor a point p\_s together with another point. So it is the closure of a point of V, or a singleton {p\_s}.
- **Not coherent.** ↑s meets {p\_s} ∪ ⋃{↑(s⌢m) : m > 0} in an infinite disjoint union of nonempty open sets.
- **The saturated set.** C = {p\_s : s finite} is saturated and closed, with complement V. So \[C\] ≤ c(V), and \[C\] is not dense.
- **Failure.** Every open u ⊇ C is dense. Indeed a nonempty open set N either contains some p\_s, or contains some ↑s; in the second case u contains p\_s and hence some ↑(s⌢m) ⊆ N. So fit\[C\] is a meet of dense open sublocales and contains the Booleanization. Therefore fit\[C\] ≠ \[C\].

T refutes only the lemma. I did not determine whether fit(Δ) itself can be non-spatial for a locally compact sober X.

## Hypotheses and sharpest scope

Stability is the one hypothesis that cannot be weakened to local compactness. Everything else is used as the packet says.

| Step | What it uses | Can it be weakened? |
| --- | --- | --- |
| X has enough points | Classical choice: locally compact locales are spatial | Needed to speak of intervals |
| Localic square is the spatial product | Local compactness of X | Not examined |
| (1.1) | Nothing | Holds for all locales |
| "Only if" of (5.1) | Points only | Holds for all locales |
| Lemma 4.2 | Local compactness, coherence, well-filteredness | Coherence is needed: X₀ |
| Lemma 3.1 | Local compactness, coherence, well-filteredness | Coherence is needed: T |
| (4.2) | Only Δ ≤ I | Holds for all locales |
| "If" of (5.1) | Spatiality of M and Lemma 4.2 | Stability is needed: X₁ |

Well-filteredness is where sobriety and choice enter, through the Hofmann–Mislove theorem. This is so whether one argues by patch compactness or directly. All arguments are classical; I checked no constructive claim.

Three statements I can justify, from most to least general:

1. **All locales.** If S = M, then any two points that are inseparable and have a common lower bound are comparable. In particular all intervals are chains.
2. **Sober X whose localic square is spatial**, for instance locally compact sober X. If M is spatial, then S = M iff every inseparable pair with a common lower bound is comparable. The reason is pt(M) = pt(I) ∩ ↑Δ. Without coherence this is the right criterion and the interval condition is not: X₁ separates them.
3. **Stably locally compact X.** M is spatial, and "inseparable" means "having a common upper bound". This gives (5.1).

### An exact criterion behind Lemma 3.1

For a T0 space Z, every saturated subset induces a fitted sublocale iff the following holds. For every closed G and open V with V ∩ G ≠ ∅, there is an open N with N ∩ G ≠ ∅ and

```latex
\overline{N\cap G}\;\subseteq\;{\downarrow}(V\cap G).
```

- **If the condition fails** for G and V, take C = Z∖↓(V ∩ G) and w = Z∖G. Then (u → w) = w for every open u ⊇ C, while j\_C(w) contains V.
- **If some \[C\] is not fitted**, pick w fixed by every such (u → –) but not by j\_C. Put G = Z∖w and V = j\_C(w). An N as in the condition gives u = Z∖cl(N ∩ G) ⊇ C with N ⊆ (u → w) = w, a contradiction.
- **Pointwise form.** Identity (3.2) for all saturated C is equivalent to the local version: N can be chosen around any given point of V.
- **Where it holds.** In stably locally compact spaces take N = int K. In regular spaces take N with cl N ⊆ V. So Lemma 3.1 and the fitness of regular spaces have one proof.

This criterion is my own derivation. I did not find it in the literature, and the authors should re-check it before relying on it.

## Simplifications and first-reading notes

Five changes would shorten the proof, and eight places slowed a first reading without affecting correctness.

### Simplifications

1. **Skip the second use of Lemma 3.1.** A closed sublocale of a spatial locale is spatial. So M = c(d\_I) ∧ \[↑Δ\] = \[pt(I) ∩ ↑Δ\] at once. This removes (4.2) and the claim that closed subspaces are stably locally compact.
2. **Drop the patch topology from Lemma 3.1.** The direct argument under Verification §3 uses only coherence and well-filteredness. §2 is then needed only to know that Y is locally compact, sober and coherent.
3. **Prove (3.1) in one line.** The opens containing B are the opens containing ↑B.
4. **State "only if" of (5.1) for all locales.** It never uses (4.3).
5. **Add a corollary.** For stably locally compact X, D = Δ iff X is T1 iff X is Hausdorff. Fitted diagonal and closed diagonal coincide in this class.

### First-reading notes

- **Undefined symbol.** ⊠ appears in d\_I but is never defined; elsewhere the same element is written a₁ ∧ b₂.
- **Sublocale or point set.** Δ and I each denote both. The saturation written with subscript I mixes the two readings. Fix one convention in §1.
- **Points before spatiality.** (SC+) in §1 speaks of specialization intervals of a locale. Say there that X is spatial classically and the order lives on points.
- **"The topology of Z is spatial".** In Lemma 3.1 this only means that joins of opens are unions.
- **Points of \[B\].** "Smallest sublocale containing the points in B" is right, but pt\[B\] can be larger than B. A warning would prevent the slip in issue 3.
- **Order convention.** "Upward closure of every compact subset" is correct only for the packet's convention. The reversed convention of the graph literature flips it; say so in §2.
- **"Perfect".** §3 and §6 apply the word to sublocales, and §6 tacitly equates it with a patch-closed point set. State that equivalence or drop the remark.
- **Duplicate display.** The equivalence is displayed twice, as (SC+) and as (5.1), in slightly different words.

## References and related literature

Two of the four cited references could be checked and support the packet. The other two could not be opened from this session.

| Packet reference | What I could check | Result |
| --- | --- | --- |
| 1. Tix–Keimel–Plotkin | The PDF would not open. A search listing of its contents shows §1.5 is on Lawson-compact continuous domains | The wording on properly locally compact pospaces is unconfirmed. The facts are re-derived under Verification §2 |
| 2. Bice–Starling, Prop. 2.32 | Statement read in the [arXiv version](https://arxiv.org/pdf/1809.08578) and the [journal PDF](https://link.springer.com/content/pdf/10.1007/s00233-019-10027-y.pdf) | For a stably locally compact T0 space, the patch is locally compact Hausdorff and compact saturated sets stay compact in it. The space need not be compact. This supports facts 1 and 3 |
| 3. Escardó | Abstract and introduction of the [paper](https://martinescardo.github.io/papers/patch-full.pdf) | The title has no leading "On". The paper says explicitly that stably locally compact does not include compact. I read the copy on martinescardo.github.io, not the cs.bham.ac.uk address |
| 4. Project A definitions file | The GitHub address was not reachable | Not consulted |

The packet names Cameron and Kumar without a citation, and a search did not identify the paper. Add the full reference.

Related work to cite or check:

- **Fitted diagonals.** Arrieta, Picado and Pultr study locales whose diagonal is fitted, called F-separated (Appl. Categ. Structures 30 (2022) 247–263). D = Δ is exactly that property. [Arrieta's follow-up](https://arxiv.org/pdf/2310.18522) records that fitness implies it, that it implies total unorderedness, and that the strong Hausdorff property does not imply it. Simplification 5 fits this picture.
- **Saturated sets and fitted sublocales.** [Jakl](https://arxiv.org/pdf/1910.03542) and [Jakl–Suarez](https://arxiv.org/pdf/2404.18325) relate saturated sets, filters and fitted sublocales for locally compact frames. I saw only excerpts. Lemma 3.1 or the criterion above may be implicit there, so check before any novelty claim.
- **Products.** Stable compactness is preserved by products and the patch commutes with them. [This paper](https://arxiv.org/pdf/2411.13500) attributes the fact to Alvarez-Manilla, Jung and Keimel (2004, Prop. 14). It is the compact input for issue 2.
- **From memory, not re-opened.** Johnstone, Stone Spaces, II.2.13, for the product with a locally compact factor. Gierz et al., Continuous Lattices and Domains, VI-6, for compact pospaces. Isbell's density theorem, for the Booleanization used in example T.

## Suggested next steps

The theorem is settled in its stated scope, so the open questions concern S itself and the edge of the hypothesis.

1. **Decide whether S is spatial.** The packet deliberately avoids this. Is A the sublocale induced by the graph of ≤ when X is stably locally compact? It is for regular X, where A = Δ. If it holds in general, S = \[R\] always and SC+ becomes a statement about point sets. A possible route: the order is a closed sublocale of Patch(X)², and A should be its image under the squared patch map.
2. **Aim for a point-free statement.** For C = ↑Δ, identity (3.2) says that the pointwise join of (u → –) over opens u with δ\*(u) = 1 is already the nucleus of D. This can be stated without points. Escardó's patch is constructive, so a point-free proof may exist.
3. **Settle the non-coherent case.** Find a locally compact sober X for which M is not spatial, or show there is none. Example T breaks Lemma 3.1 but says nothing about the diagonal. Statement 2 under Hypotheses is the candidate replacement for (5.1).
4. **Check the exact criterion against the literature.** Start with Jakl, Jakl–Suarez and Moshier–Pultr–Suarez on strongly exact filters.
5. **Revise the packet.** Apply the repairs for issues 1–3, add the tent control and the examples X₁ and T, and record the corollary that D = Δ iff X is Hausdorff.
