# Referee report — far-grid converse counterexample

**Project A · Blind external mathematical audit · independent adversarial report**

Nov 8, 2026 · @Someone

## 1. Verdict: VALID

The candidate counterexample is correct. The space X of §2 is a countable, second-countable, T0, sober space; its frame L = O(X) satisfies d\_I = d\_U in L ⊕ L (so I = U as closed sublocales of the localic square), and the disjoint pair a = ⋃\_i P\_i, b = N\_1 admits no simultaneous far grid. I reconstructed every step from the definitions in §0 without relying on any assertion of the packet, and found no fatal gap and no false statement in §§2–5.

Headline findings:

- Topology (§2): the displayed family is a basis; all four closure formulas (1) are correct; (2) holds in every topological space.
- Farness table (§3): all ten rows are correct, including the disjointness conditions and the single exceptional type (P\_i, N\_n) with i ≥ n. No omitted cases, no wrong index bound. Confirmed by hand and by an exhaustive check on a finite truncation.
- Localic equality (§3): the argument is a correct computation in the frame coproduct. Re-derived in the C-ideal presentation of L ⊕ L; the pair (a, b) enters d\_U after three alternating join closures (coordinate 2, then 2, then 1), which is exactly what a simultaneous grid cannot deliver.
- Grid obstruction (§4): sound for arbitrary (transfinite, overlapping, repeated) index families; it only uses that joins in O(X) are unions.
- Auxiliary claims (§5): all true (countable, second countable, T0, sober, noncompact, q has no compact neighbourhood). The clopen-block sobriety argument is correct.
- Boundaries (§6): O(X) is not compact (hence not coherent), not continuous and not algebraic — I supply proofs the packet omits. Unstated limitation: O(X) is not subfit (so not T1, fit or regular), and the obstruction mechanism depends on this.

All issues found are expository (severity Minor or Note); none affects the verdict. A collapsed variant of the construction (one point s\_i per block) fails, which shows the infinite tails S\_i are essential and not an artefact.

The verdict is relative to the definitions of I, U and the far-grid property exactly as stated in §0 of the packet; see §12 for the limits of this check.

## 2. Scope, method and provenance of each check

I audited only the two blind documents (prompt and packet, both dated 2026-11-08). I did not read any internal audit, ledger, reconciliation or earlier referee report, and I did not consult the web. The report below was written before seeing any author response.

**Reconstructed independently (no reliance on the packet's assertions):** the basis axiom; the characterisation of open sets and of closures in X; the four closure formulas (1); the identity (2); all ten rows of the farness table; identity (3); the coproduct computation of §3 (re-done in the C-ideal presentation); the grid obstruction of §4 with explicit quantifier bookkeeping; T0, T\_D, sobriety, noncompactness, non-existence of compact neighbourhoods of q; non-coherence, non-continuity, non-algebraicity and non-subfitness of O(X); the collapsed variant X' and why it fails.

**Relied on as standard (not re-proved from axioms):**

- L ⊕ L is the frame of C-ideals of L × L; a ⊠ b = ι₁(a) ∧ ι₂(b); the rectangular join identities of §0 hold because ι₁, ι₂ are frame homomorphisms and L ⊕ L is a frame.
- For a frame homomorphism h: M → N with right adjoint h∗, the closure of the induced sublocale is C(h∗(0)), where h∗(0) = ⋁{w : h(w) = 0}; applied to the codiagonal ∇(a ⊠ b) = a ∧ b this gives cl Δ = C(d\_I). (Checked in one line in §5 below.)
- u\* = X \\ cl u in O(X).
- Points of L ⊕ L are pairs of points of L, and the spatialisation of O(X) ⊕ O(X) is O(X × X) (used only for a sanity check, not for the verdict).

**Mechanical cross-check.** A short script (indices truncated to i, n ≤ 7 and m, t ≤ 7, basic opens tested with indices ≤ 5 so that tails and eventually-disjoint neighbourhoods exist inside the window) verified: the basis axiom for all pairwise intersections; the four closure formulas from the neighbourhood-base criterion; the disjointness condition in each of the ten rows; that the disjoint-but-not-far pairs are exactly (P\_i, N\_n) with i ≥ n; identity (3); and the failure of the collapsed variant. The script checks combinatorics of indices given the neighbourhood bases; the tail conditions themselves were verified by hand (§3 below).

**Definitions used.** Exactly those of §0 of the packet: d\_I = ⋁{a ⊠ b : a ∧ b = 0}, d\_U = ⋁{a ⊠ b : a\* ∨ b\* = 1}, I = C(d\_I), U = C(d\_U); far-grid property as displayed. I did not check whether the "Urysohn separation relation" is defined this way in the surrounding literature; if it is defined differently there, the verdict does not automatically transfer (§12).

## 3. Task 1 — Topology: basis, open sets, closures

The displayed family is a basis and all four closure formulas (1) are correct.

**Basis axiom.** The family covers X (p\_i ∈ P\_i, s\_{i,m} ∈ T\_{i,m}, r\_i ∈ R\_{i,m}, q ∈ N\_n). Every pairwise intersection is a union of members of the family:

| Pair | Intersection | Union of basics? |
| --- | --- | --- |
| P\_i with anything | ∅ or P\_i (P\_i ⊆ R\_{i,m}; P\_i ∩ N\_n = ∅) | yes |
| T\_{i,m} with anything | ∅ or T\_{i,m} | yes |
| R\_{i,m} ∩ R\_{j,t} | ∅ if i ≠ j; R\_{i,max(m,t)} if i = j | yes |
| R\_{i,m} ∩ N\_n | ∅ if i < n; ⋃*{t ≥ m} T*{i,t} if i ≥ n | yes (not itself basic) |
| N\_n ∩ N\_{n'} | N\_{max(n,n')} | yes |

The packet states the intersections but never says why they suffice; the point is that R\_{i,m} ∩ N\_n (i ≥ n) is not a basic open but is a union of basic opens, which is all the basis criterion needs. Expository only.

**Open sets.** From the basis, U ⊆ X is open iff

- r\_i ∈ U implies p\_i ∈ U and s\_{i,t} ∈ U for all but finitely many t (some R\_{i,m} ⊆ U), and
- q ∈ U implies S\_i ⊆ U for all i ≥ some n (some N\_n ⊆ U).

Points p\_i and s\_{i,m} are isolated. The neighbourhood bases of §2 are therefore correct: at p\_i the single set P\_i, at s\_{i,m} the single set T\_{i,m}, at r\_i the decreasing chain R\_{i,1} ⊇ R\_{i,2} ⊇ …, at q the decreasing chain N\_1 ⊇ N\_2 ⊇ …. The only basic opens containing q are the N\_n, and the only ones containing r\_i are the R\_{i,m}.

**Closure criterion.** For any A ⊆ X, x ∈ cl A iff every basic neighbourhood of x meets A. Hence:

- p\_i ∈ cl A iff p\_i ∈ A; s\_{i,m} ∈ cl A iff s\_{i,m} ∈ A.
- r\_i ∈ cl A iff r\_i ∈ A, or p\_i ∈ A, or A ∩ S\_i is infinite.
- q ∈ cl A iff q ∈ A, or A meets S\_i for infinitely many i.

**The four formulas (1).**

| Set | r\_j ∈ closure? | q ∈ closure? | Closure |
| --- | --- | --- | --- |
| P\_i | j = i only (p\_i ∈ P\_i) | no (meets no S\_j) | P\_i ∪ {r\_i} ✓ |
| T\_{i,m} | no (p\_i ∉, meets S\_i in one point) | no (meets one S\_j) | T\_{i,m} ✓ (closed, hence clopen) |
| R\_{i,m} | j = i only (already in the set) | no (meets only S\_i) | R\_{i,m} ✓ (clopen) |
| N\_n | j ≥ n (N\_n ⊇ S\_j infinite); j < n no | yes (in the set) | N\_n ∪ {r\_j : j ≥ n} ✓ |

The one formula that carries the whole construction is cl T\_{i,m} = T\_{i,m}: it holds because R\_{i,m+1} misses s\_{i,m}, i.e. because the neighbourhood filter of r\_i is the tail filter on S\_i. See §9 for what happens when this is destroyed.

**Identity (2).** In any space, the pseudocomplement of an open u in O(X) is the largest open disjoint from u, which is X \\ cl u. Then u\* ∨ v\* = X iff cl u ∩ cl v = ∅. Correct, and not specific to X.

## 4. Task 2 — Farness and the ten-row table

All ten rows are correct: the disjointness condition, and the verdict that disjoint implies far, with the single exception (P\_i, N\_n), i ≥ n. There are exactly ten unordered type pairs (four types, with repetition), so the table is exhaustive.

Using (1), each row was recomputed as: disjoint iff the two sets have no common point; far iff the two closures from (1) have no common point.

| Row | Disjoint iff | Closures meet iff | Verdict |
| --- | --- | --- | --- |
| P\_i, P\_j | i ≠ j | i = j | far when disjoint ✓ |
| P\_i, T\_{j,t} | always | never | far ✓ |
| P\_i, R\_{j,m} | i ≠ j (p\_i ∈ R\_{i,m}) | i = j | far when disjoint ✓ |
| P\_i, N\_n | always | i ≥ n (common point r\_i) | far iff i < n; exceptional for i ≥ n ✓ |
| T\_{i,t}, T\_{j,u} | (i,t) ≠ (j,u) | (i,t) = (j,u) | far when disjoint ✓ |
| T\_{i,t}, R\_{j,m} | i ≠ j, or i = j and t < m | i = j and t ≥ m | far when disjoint ✓ |
| T\_{i,t}, N\_n | i < n | i ≥ n (s\_{i,t} ∈ N\_n) | far when disjoint ✓ |
| R\_{i,m}, R\_{j,t} | i ≠ j | i = j | far when disjoint ✓ |
| R\_{i,m}, N\_n | i < n (else share s\_{i,t}, t ≥ m) | i ≥ n (r\_i, and the s\_{i,t}) | far when disjoint ✓ |
| N\_n, N\_{n'} | never (both contain q) | — | vacuous ✓ |

**Points specifically hunted for and not found.**

- Boundary cases i = n: (P\_n, N\_n) is disjoint and not far (r\_n ∈ both closures) — correctly included in the exceptional range i ≥ n. (T\_{n,t}, N\_n) and (R\_{n,m}, N\_n) are not disjoint — correctly excluded by i < n.
- The row T\_{i,t}, R\_{i,m} with t < m: disjoint, and far because cl T\_{i,t} = T\_{i,t} (the tail-filter point above). Correct.
- Transposes: the table suppresses order; both orders of (P\_i, N\_n) are exceptional and §3 handles the transpose by symmetry of ⊠ under the coordinate swap. Fine.
- Repeated indices in rows 1, 5, 8 (i = j) are covered: the pairs are then not disjoint.

**Mechanical confirmation.** On the truncated model, every disjoint pair of tested basic opens is far except exactly the 15 pairs (P\_i, N\_n) with 1 ≤ n ≤ i ≤ 5; every row's disjointness predicate matched the table; identity (3) held for all tested n ≤ i.

## 5. Task 3 — Localic equality d\_I = d\_U in L ⊕ L

The packet's argument is a correct computation in the frame coproduct and establishes d\_I = d\_U, hence I = U as closed sublocales. I re-derived it in the C-ideal presentation, where every step is a concrete closure operation and nothing is inferred from points.

**Setting.** L ⊕ L is the frame of C-ideals of L × L: down-sets J ⊆ L × L containing all (0, b) and (a, 0), closed under (a\_k, b) ∈ J for all k ⇒ (⋁\_k a\_k, b) ∈ J, and symmetrically in the second coordinate. The rectangle a ⊠ b is the C-ideal generated by (a, b); joins of C-ideals are generated C-ideals; and a ⊠ b ≤ J iff (a, b) ∈ J. The two rectangular identities of §0 are exactly the two closure rules. So:

- d\_I = the C-ideal generated by G = {(a, b) : a ∧ b = 0};
- d\_U = the C-ideal generated by F = {(a, b) : a\* ∨ b\* = 1}.

**Step 0: cl Δ = C(d\_I).** The diagonal sublocale is induced by the codiagonal ∇: L ⊕ L → L, ∇(a ⊠ b) = a ∧ b. The closure of the sublocale induced by a frame map h is C(h∗(0)), where h∗ is the right adjoint and h∗(0) = ⋁{w : h(w) = 0}. Since every w is a join of rectangles and ∇ preserves joins, ∇(w) = 0 iff every rectangle in w has a ∧ b = 0, so ∇∗(0) = ⋁{a ⊠ b : a ∧ b = 0} = d\_I. Correct as asserted in §0. Also C is injective (d = ⋀ ↑d), so C(d\_I) = C(d\_U) iff d\_I = d\_U.

**Step 1: d\_U ≤ d\_I.** G is itself a C-ideal: down-closed, contains the zero pairs, and closed under coordinate joins by frame distributivity ((⋁a\_k) ∧ b = ⋁(a\_k ∧ b) = 0). F ⊆ G because a\* ∨ b\* = 1 gives a ∧ b = (a ∧ b) ∧ (a\* ∨ b\*) = 0. So d\_U ⊆ G = d\_I.

**Step 2: every disjoint basic pair lies in d\_U.** By §4 all disjoint basic pairs except (P\_i, N\_n), i ≥ n, are in F. For the exception, (3) is a set identity (N\_n = N\_{i+1} ∪ S\_n ∪ … ∪ S\_i, and each S\_j is the union of the singletons T\_{j,t} over t); (P\_i, N\_{i+1}) ∈ F since i < i+1, and (P\_i, T\_{j,t}) ∈ F for all j, t. One closure in coordinate 2 gives (P\_i, N\_n) ∈ d\_U. The transpose follows by the symmetric rule. This is exactly (4) of the packet; the use of the second rectangular identity is legitimate.

**Step 3: every disjoint pair (u, v) lies in d\_U.** Let u ∧ v = 0. For a basis, u = ⋁{B basic : B ⊆ u} and likewise v. Fix B ⊆ u. Every basic C ⊆ v is disjoint from B, so (B, C) ∈ d\_U for all such C; a closure in coordinate 2 gives (B, v) ∈ d\_U. Then a closure in coordinate 1 over all B ⊆ u gives (u, v) ∈ d\_U. Hence G ⊆ d\_U, i.e. d\_I ≤ d\_U.

With Step 1, d\_I = d\_U. ∎

**What the computation shows about alternation.** For a = P\_1 ∪ P\_2 ∪ … and b = N\_1, the pair (a, b) is reached from F by: (i) for each i, a join in coordinate 2 using a decomposition of b that depends on i, namely b = N\_{i+1} ∪ S\_1 ∪ … ∪ S\_i; (ii) a join in coordinate 1 over i. The decomposition of b in (i) varies with the piece of a. A simultaneous grid would require one decomposition of b serving all pieces of a at once; §6 shows none exists. This is the precise sense in which the motivation's phrase "alternating refinements, not a single simultaneous grid" is realised.

**Pointwise sanity check (not used for the verdict).** Under the spatialisation σ: L ⊕ L → O(X × X), σ(a ⊠ b) = a × b, σ(d\_I) = (X × X) \\ cl Δ and σ(d\_U) = ⋃{a × b : cl a ∩ cl b = ∅}. Since σ preserves joins, d\_I = d\_U forces these two subsets of X × X to coincide, and they do: a pair (x, y) with disjoint neighbourhoods has far neighbourhoods by the table, the only delicate case being (p\_i, q), which is covered by P\_i × N\_{i+1}. (An initial attempt to exhibit (p\_i, q) as a pointwise counterexample failed precisely for this reason — it was a slip on my side, not an issue in the packet; I record it because it is the natural trap.)

**Checks of the prompt's warnings.** The packet does not infer equality of sublocales from points; it works in L ⊕ L throughout. The rectangular identities are used exactly in Steps 2 and 3 and nowhere else. No use is made of X × X being the localic product (it need not be, and I did not assume it).

## 6. Task 4 — The far-grid obstruction

The argument of §4 is correct for arbitrary index families: any cardinality, overlapping pieces, repeated pieces, empty pieces, pieces not themselves basic. Nothing in it depends on the shape of the decompositions beyond the fact that in O(X) a join is a union.

**Quantifier bookkeeping.** Let a = ⋃ of all P\_i and b = N\_1 (disjoint: b contains no p\_i). Suppose families (a\_α) and (b\_β) of opens are given with ⋃ a\_α = a, ⋃ b\_β = b, and cl(a\_α) ∩ cl(b\_β) = ∅ for all α, β.

1. q ∈ b = ⋃ b\_β, so there exists β₀ with q ∈ b\_β₀. (Existential over the family; uses only that the join is a union.)
2. b\_β₀ is open and contains q, so it contains a basic open containing q; the only such are the N\_n. Fix one n with N\_n ⊆ b\_β₀.
3. By (1), r\_i ∈ cl(N\_n) ⊆ cl(b\_β₀) for every i ≥ n. (Monotonicity of closure.)
4. Fix any single i ≥ n (i = n suffices). p\_i ∈ a = ⋃ a\_α, so there is α\_i with p\_i ∈ a\_α\_i; then P\_i ⊆ a\_α\_i and r\_i ∈ cl(P\_i) ⊆ cl(a\_α\_i).
5. r\_i ∈ cl(a\_α\_i) ∩ cl(b\_β₀), so by (2) a\_α\_i and b\_β₀ are not far. Contradiction.

The order of quantifiers is ∀ families ∃ β₀ ∃ n ∀ i ≥ n ∃ α\_i: one bad pair (α\_i, β₀) is enough. The proof never needs the b\_β to be basic, nor the a\_α to be the P\_i, nor the families to be disjoint, well-ordered or countable.

**Can a large family evade it?** No. Any evasion would have to deny one of: (i) some b\_β contains q — impossible since q ∈ b and the join is a union; (ii) every open containing q contains some N\_n — this is the definition of the topology; (iii) every open containing p\_i contains P\_i — trivial; (iv) closure is monotone. None depends on the index set.

**Transfinite or non-simultaneous refinements.** The far-grid property as defined in §0 is a one-step condition: one decomposition of a and one of b, all cross pairs far. It is not the condition "(a, b) lies in the C-ideal generated by far pairs", which allows the decomposition of b to depend on the piece of a (§5, Step 2) and iterates. The packet is clear about this, and the gap between the two conditions is exactly what the example exhibits.

**One more pair, for completeness.** The same obstruction applies to (a, N\_n) for every n, and to (P\_i ∪ P\_{i+1} ∪ …, N\_n) for every i, n; a single failing pair is all the statement needs.

**Direction already known.** I also checked the easy direction stated in §0: if a = ⋁ a\_α, b = ⋁ b\_β with all cross pairs far, then a ⊠ b = ⋁ over α, β of a\_α ⊠ b\_β ≤ d\_U by the two rectangular identities; so the far-grid property implies d\_I ≤ d\_U, i.e. I = U.

## 7. Task 5 — Auxiliary topological claims

All auxiliary claims of §§1 and 5 are true. Status by claim:

| Claim | Status | Independent check |
| --- | --- | --- |
| X countable | true | countable union of countable sets |
| second countable | true | basis indexed by N ⊏ N² ⊏ N² ⊏ N |
| T0 | true | see below |
| T\_D (not claimed) | true | R\_{i,m} minus r\_i and N\_n minus q are open |
| sober | true | clopen-block argument verified |
| noncompact | true | cover {N\_1} ∪ {B\_i} |
| q has no compact neighbourhood | true | both cases of §5 verified |
| not T1, not regular | true (not claimed) | r\_i ∈ cl{p\_i} |

**T0.** For r\_i vs r\_j (i ≠ j): R\_{i,1} omits r\_j. For r\_i vs q: R\_{i,1} omits q. For r\_i vs p\_j: P\_j omits r\_i. All other points are isolated. Correct.

**Closed sets.** F is closed iff: p\_i ∈ F ⇒ r\_i ∈ F; F ∩ S\_i infinite ⇒ r\_i ∈ F; F meets infinitely many S\_i ⇒ q ∈ F. In particular {q}, {r\_i}, {r\_i, p\_i} = cl{p\_i}, {s\_{i,m}} and each B\_i = R\_{i,1} are closed. B\_i is open as a basic set, so clopen — as the packet claims.

**Sobriety (the clopen-block argument).** Let F be nonempty, closed, irreducible.

- If F meets B\_i: F = (F ∩ B\_i) ∪ (F \\ B\_i) with both parts closed (B\_i clopen); irreducibility and F ∩ B\_i ≠ ∅ force F ⊆ B\_i. Correct.
- Inside B\_i: if F contains some s\_{i,m}, then {s\_{i,m}} is clopen in X, and the same splitting gives F = {s\_{i,m}} = cl{s\_{i,m}}. Otherwise F ⊆ {r\_i, p\_i}, whose nonempty closed subsets are {r\_i} = cl{r\_i} and {r\_i, p\_i} = cl{p\_i} ({p\_i} is not closed). Correct.
- If F meets no B\_i: F ⊆ X \\ ⋃ B\_i = {q}, so F = {q} = cl{q}. Correct.

Every irreducible closed set is the closure of a point, and the generic point is unique because X is T0. Hence X is sober. The packet's argument is complete; it could add the half-sentence that T0 gives uniqueness, and that {q} and {r\_i} are closed.

Since X is sober and O(X) is spatial, Loc(O(X)) is X itself; the "localic" and "spatial" readings of the square's points agree, though the packet correctly does not use this.

**Noncompact.** N\_1 ∪ ⋃ B\_i = X; any finite subfamily omits some B\_i and so misses p\_i and r\_i. Correct.

**q has no compact neighbourhood.** Any neighbourhood K of q contains some N\_n, hence all S\_i with i ≥ n. Suppose K is compact.

- Case A: K contains r\_i for infinitely many i. The sets N\_1 ∩ K and B\_i ∩ K form an open cover of K; each r\_i ∈ K lies in B\_i only, so no finite subcover. Correct.
- Case B: K contains only finitely many r\_i. Choose i ≥ n with r\_i ∉ K. The sets N\_{i+1}, B\_j (j ≠ i), P\_i and all T\_{i,m} cover X \\ {r\_i} ⊇ K. The points of S\_i ⊆ K lie only in the T\_{i,m}, so no finite subcover. Correct.

So no compact set is a neighbourhood of q: X is not locally compact at q in the strongest sense. (A direct frame-theoretic confirmation — no V ≪ N\_1 contains q — is in §8.)

**Relation between the two.** Noncompactness alone would not matter for the main theorem; non-local-compactness does, because it places O(X) outside the continuous frames (§8).

## 8. Task 6 — Boundaries and unstated limitations

O(X) lies outside all three positive classes named in the prompt. The packet only disclaims these classes (§6); it does not prove the example is outside them. The proofs below are mine. I have not verified the positive results themselves (that I = U implies far grids for coherent, continuous or algebraic frames); that is outside the packet.

| Class | O(X) in it? | Reason |
| --- | --- | --- |
| compact / coherent | no | X is not compact (§7) |
| continuous (= X core-compact, = locally compact since X is sober) | no | no V with q ∈ V ≪ N\_1; see below |
| algebraic | no | no compact open contains q; see below |
| spatial | yes | it is a topology |
| subfit (hence fit, regular, T1) | no | see below |
| T\_D | yes | §7 |

**Not continuous.** It suffices to show N\_n is not way below N\_1 for any n, since any V containing q contains some N\_n and the way-below relation is down-closed in its first argument. Let D be the family of opens N\_m ∪ E with m > n and E a finite subset of S\_1 ∪ … ∪ S\_n. D is directed and its union is N\_1. No member contains N\_n, because N\_n ⊇ S\_n is infinite while (N\_m ∪ E) ∩ S\_n = E ∩ S\_n is finite. So N\_n is not way below N\_1, and O(X) is not a continuous frame.

**Not algebraic.** Claim: no compact open V contains q. Let V be open with q ∈ V, so V ⊇ N\_m for some m.

- If r\_j ∈ V for all j ≥ some j₀, then B\_j ⊆ V for all j ≥ max(m, j₀) (r\_j ∈ V forces p\_j ∈ V, and S\_j ⊆ N\_m ⊆ V). Cover V by N\_j, the B\_k for k ≥ j, and V ∩ (B\_1 ∪ … ∪ B\_{j-1}), the last being open since finite unions of clopens are clopen. Any finite subfamily omits some B\_k with k ≥ j, and then p\_k ∈ V is uncovered. So V is not compact.
- Otherwise r\_j ∉ V for infinitely many j; pick such a j ≥ m. Then V \\ S\_j is open (q has N\_{j+1} ⊆ V \\ S\_j; each r\_k ∈ V with k ≠ j keeps a neighbourhood R\_{k,t} ⊆ V disjoint from S\_j; other points are isolated). The cover {V \\ S\_j} ∪ {T\_{j,t} : t ∈ N} of V has no finite subcover since S\_j ⊆ V is infinite. So V is not compact.

Hence N\_1 is not a join of compact opens, and O(X) is not algebraic. For the record, the compact opens are exactly the finite unions of sets P\_i, T\_{i,m}, R\_{i,m} (each R\_{i,m} is compact: a neighbourhood of r\_i swallows a tail of S\_i, leaving finitely many points).

**Not subfit (unstated limitation).** Subfitness of O(X) requires: whenever U ⊄ V there is an open W with U ∪ W = X but V ∪ W ≠ X. Take U = P\_i, V = ∅. Any W with P\_i ∪ W = X contains r\_i, hence contains some R\_{i,m} ∋ p\_i, so W = X = V ∪ W. Subfitness fails. Consequently O(X) is not fit, not regular, and X is not T1 (also directly: r\_i ∈ cl{p\_i}).

This matters because the obstruction mechanism of §6 lives entirely on non-T1 behaviour: the point p\_i has a least neighbourhood whose closure contains the extra point r\_i. The packet does not say so. The example therefore leaves open whether the converse holds for subfit, fit, T1 or Hausdorff frames (§11).

**Other limitations worth stating in the packet.**

- The frame is spatial and sober, so this is also a counterexample at the level of sober spaces; the packet could claim this explicitly (it is a strength).
- The failure is witnessed by a single disjoint pair (a, b); the packet does not say how many disjoint pairs lack far grids. (Not needed; (a, b) is enough.)
- The term "Urysohn separation relation" and the far relation are used as defined in §0. If the external literature defines U differently (for instance through a stronger separation than a\* ∨ b\* = 1), the verdict applies to the packet's definition only.

## 9. Task 7 — Independent stress tests

Four tests were run: a collapsed variant of the space (which fails, instructively), a general method for proving that a pair is *not* in d\_U (which confirms the failure and would have detected an error in the packet), an alternative route to the equality (which shows where alternation is forced), and a hunt for counterexamples to each displayed identity. None found an error.

**Test 1: collapse each S\_i to one point.** Let X' = {q} ∪ {p\_i, r\_i, s\_i : i ∈ N} with basis {p\_i}, {s\_i}, R\_i = {r\_i, p\_i, s\_i}, N\_n = {q} ∪ {s\_i : i ≥ n}. This is a basis, X' is T0 and sober, (P\_i, N\_n) is still disjoint-not-far for i ≥ n with the same refinement (3), and the grid obstruction of §6 goes through verbatim. One might hope it is a smaller counterexample. It is not: cl{s\_i} = {s\_i, r\_i}, because the only neighbourhood of r\_i is R\_i ∋ s\_i. So (P\_i, T\_i) is a disjoint pair of atoms of O(X') whose closures meet at r\_i, and atoms cannot be refined. Indeed (P\_i, T\_i) ∉ d\_U, by Test 2. So d\_I ≠ d\_U in O(X'): the collapsed space is not a counterexample.

Moreover O(X') is algebraic (every open is a union of the compact opens {p\_i}, {s\_i}, R\_i, N\_n; here N\_n is compact since any open containing q contains N\_m and leaves finitely many s\_i uncovered). So X' is a sober space, outside the coherent class only because it is noncompact, where I ≠ U. This is consistent with the positive results the prompt alludes to, and it shows the design of the packet's X is tight: the infinite S\_i with the tail filter at r\_i are needed exactly to make each T\_{i,m} closed (so that every T–R and T–N disjoint pair is far) while keeping r\_i in cl N\_n. The same feature destroys algebraicity (§8). The verified closure cl T\_{i,m} = T\_{i,m} is the load-bearing line of the whole packet.

**Test 2: a certificate that a pair is not in d\_U.** To show (a, b) ∉ d\_U it suffices to exhibit a C-ideal J ⊇ F with (a, b) ∉ J. Useful choice: for points x, y, let J(x, y) = {(u, v) : x ∉ u or y ∉ v}. This is always a C-ideal (down-closed; if x ∈ ⋁u\_k then x ∈ some u\_k; same in the other coordinate). It contains F whenever every neighbourhood of x and every neighbourhood of y have meeting closures. In X', J(p\_i, s\_i) ⊇ F and (P\_i, T\_i) ∉ J(p\_i, s\_i), which proves d\_I ≠ d\_U there. In the packet's X I tried to build such a certificate for (a, b) = (⋃P\_i, N\_1) and for (P\_i, N\_n): J(p\_i, q) does not contain F, because (P\_i, N\_{i+1}) ∈ F while p\_i ∈ P\_i and q ∈ N\_{i+1}. No pointwise certificate exists for X — consistent with §5, which shows (a, b) ∈ d\_U constructively. (A general certificate need not be pointwise, but the constructive membership proof in §5 settles the matter.)

**Test 3: alternative route via a pointwise far-grid lemma.** Say a space has the *local far-grid property* if for all disjoint opens u, v and every x ∈ u there are an open u\_x with x ∈ u\_x ⊆ u and a decomposition v = ⋃ v\_k into opens each far from u\_x. This implies d\_I = d\_U (one closure in coordinate 2 per x, then one in coordinate 1), and it is weaker than the far-grid property. I checked it on X point type by point type, for arbitrary disjoint u, v:

- x = s\_{i,m}: u\_x = T\_{i,m} is clopen and v is already far from it.
- x = r\_i: u\_x = R\_{i,m} ⊆ u is clopen; v misses p\_i, r\_i and a tail of S\_i, so r\_i ∉ cl v, and v is already far from u\_x.
- x = p\_i: u\_x = P\_i. Since p\_i ∉ v, also r\_i ∉ v, and v \\ S\_i is open. Then v = (v \\ S\_i) ∪ ⋃{T\_{i,t} ⊆ v}, each piece far from P\_i. One decomposition of v suffices.
- x = q: u\_x ⊇ N\_n for some n, and v ∩ B\_j ⊆ {p\_j} for all j ≥ n. If p\_j ∈ v for infinitely many j, then no u\_x and no decomposition of v works: every piece containing p\_j has closure through r\_j ∈ cl N\_n. This is the transposed obstruction of §6.

So the local property fails at q for (N\_1, ⋃P\_j), and the equality cannot be proved by refining v alone, nor (by symmetry) by refining u alone. The basis route of §5 refines coordinate 2 for the pairs (P\_i, N\_n) and coordinate 1 for their transposes, and this two-sided alternation is unavoidable. The test confirms rather than replaces the packet's proof, and it localises exactly where alternation is forced.

**Test 4: look for a counterexample to each displayed identity.** (1), (2), (3) were checked by hand (§3) and mechanically (§4). (4) is (3) plus the second rectangular identity. The intersection formula R\_{i,m} ∩ N\_n and the two monotone chains were checked. No counterexample was found.

## 10. Issues, severity-ranked, with repairs

No issue is Fatal or Major. Everything below is Minor (an omitted justification a careful reader must supply) or Note (a suggestion). The counterexample stands as written.

| # | Severity | Location | Issue | Repair |
| --- | --- | --- | --- | --- |
| 1 | Minor | §2, basis | The basis axiom is never stated or checked; R\_{i,m} ∩ N\_n (i ≥ n) is not a basic open. | Add one sentence: each pairwise intersection is a union of listed sets, which is what the basis criterion requires. |
| 2 | Minor | §2, (1) | The closure formulas are stated without the closure criterion that justifies them. | Add the three-line criterion (§3 of this report) and remark that cl T\_{i,m} = T\_{i,m} uses R\_{i,m+1} ∩ T\_{i,m} = ∅. |
| 3 | Minor | §0 | "I = cl Δ = C(d\_I)" is asserted without proof. | Cite or give the one-line computation ∇∗(0) = ⋁{a ⊠ b : a ∧ b = 0}. |
| 4 | Minor | §5, sobriety | Uniqueness of generic points, and closedness of {q}, {r\_i}, are not mentioned. | Add "X is T0, so generic points are unique" and list the closed sets used. |
| 5 | Minor | §5, local compactness | "Not locally compact at q" is not defined; the proof actually shows no compact set is a neighbourhood of q. | State that stronger form explicitly. |
| 6 | Minor | §6 | The packet disclaims the coherent/continuous/algebraic classes but does not show O(X) lies outside them. | Add the two short arguments of §8 of this report (not continuous; no compact open contains q). |
| 7 | Note | §6 | O(X) is not subfit, hence the example says nothing about T1, fit or regular frames. | State this as a limitation. |
| 8 | Note | §3, table | The table conflates "when disjoint" with the disjointness condition on indices; fine, but the two i = n boundary cases deserve one sentence. | Add: (P\_n, N\_n) is exceptional; (T\_{n,t}, N\_n) and (R\_{n,m}, N\_n) are not disjoint. |
| 9 | Note | §1 | "first-countability observation" refers to an earlier draft not in the packet. | Delete the reference or make the packet self-contained. |
| 10 | Note | §5 | A reader may want to know why the S\_i must be infinite. | Add the collapsed variant X' as a remark (§9, Test 1 of this report). |

**Distinguishing fatal gaps from omissions.** None of items 1–6 can fail: each omitted justification was supplied and verified here. A fatal gap would have been, for example, a disjoint basic pair not in d\_U with no refinement, or a false closure formula; the one place where this could plausibly happen (cl T\_{i,m}) was verified by hand and mechanically, and the collapsed variant shows what the failure would have looked like.

## 11. Supplementary: research ideas (labelled by what was checked)

These are suggestions, not findings. Each is tagged with what I actually verified.

1. **Alternation depth as an invariant.** *Checked:* in X the pair (⋃P\_i, N\_1) enters d\_U after one coordinate-2 closure (per piece) and one coordinate-1 closure, and §9 Test 3 shows one-sided refinement cannot do it. *Not checked:* whether a space exists needing k alternations for each k, or transfinitely many. The construction suggests a template: stack the "p\_i / r\_i / tail" gadget so that each refinement creates a new exceptional pair.
2. **Local far-grid property.** *Checked:* the property defined in §9 Test 3 implies I = U, is implied by the far-grid property, and fails in X. *Not checked:* whether it is equivalent to I = U in any natural class (it is a candidate for an intermediate, pointwise-checkable condition, and the obvious conjecture is that it already characterises I = U for spatial frames in which some coordinate can always be chosen first).
3. **Subfit / T1 / Hausdorff versions.** *Checked:* O(X) is not subfit and the obstruction uses r\_i ∈ cl{p\_i}. *Not checked:* whether I = U implies far grids for subfit or T1 frames. In a T1 space points have no least neighbourhood, so pieces of a around p can shrink; the obstruction would have to come from a point p ∉ cl W such that every neighbourhood of p has closure meeting cl W, which Hausdorff non-regular spaces can provide. A Hausdorff counterexample seems plausible but was not attempted.
4. **Converse for coherent/continuous/algebraic frames.** *Checked:* the collapsed X' is algebraic, noncompact and has I ≠ U, which is consistent with but not evidence for the positive results. *Not checked:* the positive results themselves. If they are proved via compactness of the top, the noncompact algebraic case (like X') is worth a separate statement.
5. **Certificates of non-membership.** *Checked:* the C-ideal J(x, y) of §9 Test 2 is always a C-ideal and witnesses d\_I ≠ d\_U in X'. *Suggestion:* for spatial frames, d\_I ≠ d\_U might always be witnessed by a pointwise J(x, y) or by a J built from a filter of neighbourhoods; if true, this would give a usable test. In X the pointwise certificates all fail, as they must.
6. **Minimality.** *Checked:* S\_i cannot be made finite (X' fails). *Not checked:* whether the r\_i can be removed by letting p\_i's closure reach into another gadget, or whether a countable space with fewer point types exists. The packet's phrase "particularly small" is not quantified and I did not attempt a minimality proof.

## 12. Limits of this check and independence statement

- **Independence.** This report was written from the prompt and packet alone. No internal audit, ledger, draft reconciliation, earlier referee report or author response was read, and no literature was consulted. The report is preserved as written before any reconciliation.
- **Standard results relied on.** The C-ideal presentation of L ⊕ L; cl of a sublocale induced by h is C(h∗(0)); u\* = X \\ cl u. Each is textbook point-free topology and I checked the one-line derivations where they are used, but did not re-prove them from the axioms.
- **Definitions.** The verdict is for I, U and the far-grid property exactly as defined in §0 of the packet. If the "Urysohn separation relation" in the project's source literature is defined otherwise, that definition must be compared with §0 before the verdict is transferred.
- **Positive results not verified.** I did not check that I = U implies far grids for coherent, continuous or algebraic frames, nor the "known" status of anything; I only showed O(X) is outside those classes.
- **Mechanical check scope.** The script verifies index combinatorics on a truncation with i, n ≤ 7 and m, t ≤ 7; it is a cross-check of the table and (1), not a proof. The infinite-tail facts (cl T\_{i,m} = T\_{i,m}; r\_i ∈ cl N\_n for i ≥ n; non-compactness; way-below) were proved by hand.
- **Test 3 and the research items** are supplementary; Test 3 was carried through for all four point types, the research items were not.
- **Scope of "valid".** Valid means: the central counterexample is correct, every technical claim in §§2–5 is true, and the omissions listed in §10 are expository. It does not assert novelty or priority (none is claimed).