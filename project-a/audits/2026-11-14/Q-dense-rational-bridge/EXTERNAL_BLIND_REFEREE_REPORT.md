# Project A — Dense rational bridge: independent blind referee report

Nov 14, 2026 · @Someone

## Verdict

**The chain survives. I found no fatal failure and no incomplete step that affects validity.** Under the definitions in packet §0, the boxed conclusion holds: W(X) = I(X) < W₂(X) = U(X) = F, where F is the fibre square of X over ℝ. Both Q′ and Q fail on this X.

I rederived every step rather than checking the packet's wording, and tried six lines of attack. All defects I found are presentation-level: a few sentences assert a true statement without the argument that proves it.

Two findings go beyond the packet and make the result more robust:

- **X is locally compact** (a second-countable non-Hausdorff 1-manifold). So the localic square X² is the ordinary topological product, and W, W₂, U, F are honest closed subspaces. Only the D₂ witness is pointless.
- **U(X) = F can be proved directly from closures**, without Lemma 5.2. The antecedent of Q therefore has two independent confirmations.

Scope: I audited against packet §0 only. I did not check that those definitions match the project's Φ, Φ₂ formulations, and I have not seen any internal audit.

## Classification of central claims

All sixteen central claims are correct; three are correct but argued too thinly in the packet. Notation: ℱ is a finite cover, F the fibre square, J the cross-chart of S and T inside F.

| # | Claim | Packet | Status | Note |
| --- | --- | --- | --- | --- |
| 1 | The basis (1.2) defines a topology with S, T disjoint and open | §1 | Correct | No quotient is taken, so no hidden identification is possible |
| 2 | p is an open local homeomorphism with fibres (1.4) | §1 | Correct |  |
| 3 | X is T₁, sober, second countable | §1 | Correct | T₁ argument is compressed |
| 4 | Each N\_q is an open global section; the atlas A has no finite subcover | (1.5) | Correct |  |
| 5 | m(ℱ) is dense in ℝ for every finite open cover ℱ of X | Lemma 2.1 | Correct | Rederived by a different route; false for countable covers |
| 6 | (h,k) is a nonzero generalized pair factoring through D₂(X) | (3.2) | Correct |  |
| 7 | The pair lands in J, inside the open rectangle S⊠T | (3.3) | Correct | Stated reason is not a proof; one-line fix below |
| 8 | The pair does not factor through D(X) | (3.4) | Correct | Redundant once (4.1) is proved |
| 9 | For regular Z: D(Z) = D₂(Z) = U(Z) = Δ | §0.4 (1) | Correct | Rests on three named facts, not quite "elementary" |
| 10 | Naturality of D, D₂, W, W₂, U along p | §0.4 (2) | Correct | Orientation checked for U |
| 11 | D(X) = Δ as a localic equality, so W(X) = I(X) | Lemma 4.1, (4.1) | Correct |  |
| 12 | W(X) < W₂(X), a closed-hull gap | (4.3) | Correct | Q′ fails |
| 13 | F is a closed spatial sublocale of X² | Lemma 5.1 | Correct | Shorter via local compactness |
| 14 | J and its transpose lie in W₂(X) | Lemma 5.2 | Correct | Needs the isomorphism ℝ ≅ J made explicit |
| 15 | W₂(X) = U(X) = F | Theorem 5.3 | Correct | U = F also holds by a direct closure computation |
| 16 | W = I < W₂ = U = F | (5.1) | Correct | Q fails |

## Independent verification, by audit item

Each item below is my own derivation; where it differs from the packet's route I say so. Stars are written ∗: s∗ is inverse image, a∗ the pseudocomplement, u∗∗ the double negation.

### 1. The topology

The space is well defined and the infinite gluing causes no problem.

- **Basis.** N(q,ε) ∩ N(q,δ) = N(q, min). For q ≠ r, N(q,ε) ∩ N(r,δ) contains no bridge point and is a union of an S-interval and a T-interval. Intersections with S- or T-opens are S- or T-opens.
- **Neighbourhood base at b\_q.** The only basis sets containing b\_q are the N(q,ε). So every open set containing b\_q contains a left S-germ and a right T-germ at q. Lemma 2.1 depends on exactly this.
- **Étale.** p maps N(q,ε) bijectively to (q−ε, q+ε), and the subspace basis of N(q,ε) goes to a basis of that interval. The preimage of an interval is open. So p is continuous, open, and a local homeomorphism, with fibres as in (1.4).
- **T₁.** Each fibre is closed (ℝ is T₁), finite, and discrete (p is étale). A point of a closed discrete subspace is closed.
- **Failure of Hausdorff.** The inseparable pairs are exactly {b\_q, s\_q} and {b\_q, t\_q}. The pair {s\_x, t\_x} is separated by S and T.
- **Sober.** X has an open cover by copies of intervals, and a space covered by sober open subspaces is sober.
- **Second countable.** Rational intervals in S and T, plus N(q, 1/n).
- **Locally compact.** Every point has a neighbourhood homeomorphic to an interval. The packet does not state this; it matters in item 5.
- **Sections.** N\_q = {b\_q} ∪ s(−∞,q) ∪ t(q,∞) is open, and p maps it homeomorphically onto ℝ.

### 2. The density lemma

Lemma 2.1 is sound for every finite open cover. My proof avoids boundaries.

Let ℱ = {c₁,…,cₙ} and let I be any open interval. Put Qᵢ = {q ∈ ℚ∩I : b\_q ∈ cᵢ}. The Qᵢ cover ℚ∩I, and a finite union of nowhere dense sets is nowhere dense, so some Qᵢ is dense in a subinterval I′.

For each q in Qᵢ, the set cᵢ contains a left S-germ and a right T-germ at q. Hence s∗(cᵢ) and t∗(cᵢ) are both open and dense in I′. Their intersection is a nonempty open subset of I contained in m(ℱ). So m(ℱ) meets every interval.

The packet's boundary argument is also correct. The index i in its proof depends on q, and (2.2) handles that properly by taking the union over i.

**Countercover attempts.** The natural attack splits S from T along a closed set K: take X minus the closure of s(K), and X minus the closure of t(K). If K contains an interval, the bridge points over its interior lie in neither set. Any further member that covers a somewhere-dense set of them picks up both sections on a dense open set. Every variant I tried hits this.

**Sharpness.** The lemma is false for countable covers: the atlas A is countable and m(A) is empty. The gap is exactly finite versus countable.

### 3. The point-free step

The Booleanization computation is correct, and the pair cannot collapse to zero.

- β∗(u) = u∗∗ is a frame homomorphism from O(ℝ) onto RO(ℝ). So β∗ of the O(ℝ)-join defining m(ℱ) equals the RO(ℝ)-join of the h(c) ∧ k(c). That is all (3.2) uses.
- The set-theoretic union of the regular opens h(c) ∧ k(c) need not be ℝ. Their join in RO(ℝ) is the double negation of that union, which is m(ℱ)∗∗ = ℝ. The packet keeps this distinction straight.
- The pair pulls every w(ℱ) back to 1, so it factors through every O(w(ℱ)), hence through their meet D₂(X).
- RO(ℝ) has 0 ≠ 1. A map from a nonzero locale cannot factor through the zero sublocale.
- Consistency check: X is T₁, so D₂(X) has no points off the diagonal. B(ℝ) has no points at all. There is no conflict; the witness is necessarily pointless.

### 4. Full diagonal and the Q′ failure

D(X) = Δ holds in Loc, and the gap survives closure.

- **D(ℝ) = Δ.** If the diagonal pulls an open ⋁ aᵢ⊠bᵢ back to 1, then {aᵢ∧bᵢ} is a cover whose cover square lies below it. So D(Z) is the meet of all open sublocales containing Δ. For regular Z the square is regular, hence fit, so every sublocale is such a meet.
- **Lemma 4.1.** Pulling back covers of ℝ gives pf = pg. The opens Vᵢ = f∗Uᵢ ∧ g∗Uᵢ cover Y by (0.2) applied to the atlas. On Vᵢ both maps factor through Uᵢ, where p is an open embedding, hence monic. Locale maps that agree on an open cover are equal. Apply this to the inclusion of D(X).
- **Disjointness.** The diagonal pulls S⊠T back to S ∧ T = 0. So Δ lies in the closed sublocale C(S⊠T), and therefore so does I(X) = W(X).
- **The gap.** The pair pulls S⊠T back to β∗(ℝ) = 1. So D₂(X) ∧ O(S⊠T) is nonzero, and W₂(X) is not below C(S⊠T). This separates the closed hulls, not just D from D₂.

### 5. The upgrade to Q

W₂(X) = U(X) = F holds.

- **F closed and spatial.** F is the pullback of the closed diagonal of ℝ. The packet's chart argument for spatiality is right. Quicker: X is locally compact, so localic X² is the topological product, and closed sublocales of a spatial locale are spatial.
- **J.** J = F ∧ O(S⊠T), and (s,t) is an isomorphism from ℝ to J with inverse p∘pr₁. Under it the pair is (s,t)∘β, so its image is the Booleanization B(J).
- **Lemma 5.2.** W₂ ∧ J is closed in J and contains the dense sublocale B(J). So it is all of J. Symmetry gives the transpose.
- **Remaining points.** The closure of the diagonal in X×X is the diagonal plus the inseparable pairs. So F is the disjoint union of I(X), J, and the transpose of J.
- **Conclusion.** W₂ is a closed subspace containing every point of the closed subspace F, and W₂ ≤ F. So W₂ = F, and the sandwich gives U = F.

**Independent check that U = F.** In a space, a∗ ∨ b∗ = 1 exactly when a and b have disjoint closures. The closure of s(x−ε, x+ε) contains b\_q for rational q in (x−ε, x+ε\]. The closure of t(x−ε, x+ε) contains b\_q for rational q in \[x−ε, x+ε). These share bridge points, so no neighbourhoods of s\_x and t\_x have disjoint closures, and (s\_x, t\_x) lies in U. With U ≤ F this gives U = F without using W₂.

## Falsification attempts

None of the attacks in audit item 6 breaks the chain. Each row says what I tried and why it fails.

| Attack | Result |
| --- | --- |
| Spatial versus localic product | No confusion. X is locally compact, so the two squares coincide. Points of X² are used only in Theorem 5.3, after spatiality of F is established. |
| Incorrect use of density | Only three facts are used: a dense open u has u∗∗ = 1; B(J) lies in every dense sublocale of J; a closed sublocale containing a dense one is everything. All standard. |
| Improper sublocale restriction | Meets of sublocales commute with meeting J. Under ℝ ≅ J, the open sublocale O(w(ℱ)) ∧ J is the open set m(ℱ). Checked directly. |
| Unsupported heredity | Lemma 4.1 never restricts D to an open subspace. It works over the base ℝ. I tried the shortcut "locally regular implies D = Δ" and it needs extra work; the packet's route avoids it. |
| Inclusion orientation | More covers give a smaller meet, so Δ ≤ D ≤ D₂. For U: (p∗a)∗ ≥ p∗(a∗), so pulled-back Urysohn rectangles are Urysohn rectangles, giving U(X) ≤ F. Both orientations are right. |
| Unnoticed finite cover | None exists; see item 2. Any finite cover must put a somewhere-dense set of bridge points in one member. |
| Collapse of the D₂ witness | D₂ ∧ J is a meet of dense open sublocales of J ≅ ℝ. It contains B(J), which is nonzero. |
| Hidden identification of S and T | Impossible. The topology is put on a disjoint union of sets with S and T declared open. |
| Vacuous antecedent in Q | Not vacuous. W₂ = U is proved twice, once via Lemma 5.2 and once by the closure computation for U. |
| Dependence on Q or Q′ | None. No step invokes either question. |

## Concerns, ranked by severity

There are no fatal or major concerns. The nine items below are ordered from most to least important; none changes a conclusion.

| Rank | Severity | Where | Concern | Fix |
| --- | --- | --- | --- | --- |
| 1 | Minor gap | §3, before (3.3) | "The two sections always differ, so the map lands in J" is not an argument. Pointwise difference says nothing about a pointless domain. | (s,t) factors through F because ps = pt, and through O(S⊠T) because s∗S ∧ t∗T = 1. Hence through J. |
| 2 | Minor gap | Lemma 5.2 | "Dense in J by construction" needs (s,t) to be an isomorphism ℝ ≅ J, so that the image of B(ℝ) is B(J). | State the isomorphism, with inverse p∘pr₁. |
| 3 | Minor gap | §0.4, import 1 | Called elementary, but it uses: regular implies fit; products of regular locales are regular; regular implies strongly Hausdorff. | Name the three facts and cite them. |
| 4 | Omission | §1, Lemma 5.1 | Local compactness of X is never stated. It removes every localic-versus-spatial worry about X² in one line. | Add it to §1 and shorten Lemma 5.1. |
| 5 | Thin argument | §1 | The T₁ sentence is compressed. | Use: fibres are closed, finite and discrete. |
| 6 | Thin argument | Theorem 5.3 | The list of leftover pairs is right but the decomposition is implicit. | State that F is the disjoint union of I(X), J and the transpose of J. |
| 7 | Cosmetic | End of §2 | Refers to a "proposed local finite-cover separation criterion" that the packet never defines. | Define it or delete the sentence. |
| 8 | Cosmetic | (3.4); Lemma 5.2 | (3.4) is redundant after (4.1). Lemma 5.2 pulls W₂ back "along J→F", but W₂ lives in X². | Mark (3.4) as illustration; write J→X². |
| 9 | Scope | §0.3 | The result is relative to the §0 definitions. Equivalence with the Φ, Φ₂ formulations is asserted elsewhere and was not audited here. | Audit that equivalence separately before changing repository status. |

## A shorter derivation

The whole result follows in six steps, with no generalized pair and no frame-map computation. It replaces §3 and §5 of the packet by one sublocale statement about J.

1. **Reduce to spaces.** X is a locally compact sober space, so X² is the topological product and its closed sublocales are closed subspaces. Naturality over ℝ places D, D₂, W, W₂ and U inside the closed subspace F.
2. **Decompose F.** The closure of the diagonal is I(X) = Δ together with the pairs (b\_q, s\_q), (b\_q, t\_q) and their reverses. So F is the disjoint union of I(X), J and the transpose of J. J is open in F and (s,t) identifies it with ℝ.
3. **Full covers.** D(X) = Δ by descent along the section atlas (Lemma 4.1). Hence W(X) = I(X) and W(X) ∧ J = 0.
4. **Finite covers.** For each finite cover ℱ, the open sublocale O(w(ℱ)) ∧ J is the open set m(ℱ) of J ≅ ℝ, which is dense by Lemma 2.1. So D₂(X) ∧ J is a meet of dense open sublocales of J. By Isbell's density theorem it contains B(J), which is nonzero.
5. **Close up.** W₂(X) ∧ J is closed in J and contains the dense sublocale B(J), so J ≤ W₂(X). By symmetry the transpose is too. With I(X) ≤ W₂(X) ≤ F this gives W₂(X) = F.
6. **Urysohn.** W₂(X) ≤ U(X) ≤ F forces U(X) = F.

```latex
W(X) \;=\; I(X) \;=\; F \setminus (J \sqcup J^{\mathrm{op}})
\;<\;
W_2(X) \;=\; U(X) \;=\; F \;=\; X \times_{\mathbb{R}} X
```

The only non-formal input is Lemma 2.1. Everything else is bookkeeping about a meet of dense opens inside a copy of ℝ.

## Theorem as I would state it, and what is imported

No correction is needed; this is the packet's result with the extra structure made explicit.

**Theorem.** Let X be the space of (1.1)–(1.2), p its projection to ℝ, F the fibre square, and J the cross-chart of S and T in F.

1. X is a second-countable, T₁, sober, locally compact, non-Hausdorff 1-manifold, and p is étale.
2. D(X) = Δ, and W(X) = I(X) is Δ together with the pairs (b\_q, s\_q), (b\_q, t\_q) and their reverses, q rational.
3. D₂(X) has no points off the diagonal, yet D₂(X) ∧ J contains the Booleanization of J.
4. W₂(X) = U(X) = F, and F is the disjoint union of I(X), J and the transpose of J.

Hence W(X) < W₂(X), so Q′ fails, and W₂(X) = U(X) ≠ W(X), so Q fails.

### Imported facts

These are the standard results I used without rederiving. Everything else in this report is my own derivation from the packet's definitions.

| Fact | Used in |
| --- | --- |
| The Booleanization is the least dense sublocale (Isbell's density theorem) | Items 3 and 5; short derivation step 4 |
| A locale is fit exactly when every sublocale is a meet of open sublocales | D(ℝ) = Δ |
| Regular implies fit; regular locales are closed under products; regular implies strongly Hausdorff | Import 1 of the packet |
| The localic product of locally compact sober spaces is their topological product | Spatiality of X² and F |
| Closed sublocales of a spatial locale are spatial | Theorem 5.3 |
| Locale maps that agree on an open cover of the domain are equal | Lemma 4.1 |

References for these are Isbell, "Atomless parts of spaces" (1972), Johnstone, *Stone Spaces* (1982), and Picado and Pultr, *Frames and Locales* (2012). I cite them from memory and did not open them in this session, so chapter and page numbers should be checked before they go into a write-up.

### Literature and limits

I know of no source that contains this construction or the D₂ computation, and I did not run a literature search. X is a non-Hausdorff 1-manifold with countably many branch points, a standard kind of object, but I make no novelty judgement.

The argument is classical throughout, as the packet declares. I produced this report before seeing any internal audit.
