# Independent Blind Referee Report — Project A Subfit Far-Grid Converse

Nov 8, 2026 · @Someone

## Verdict

**The central theorem is correct.** The frame L = O(X) of the packet's space is subfit, satisfies d\_I = d\_U in the coproduct L ⊕ L, and the disjoint pair a = ⋃P\_i, b = N\_1 admits no far grid. I found **no fatal and no major issues**. Every §6 boundary claim I checked also holds. The issues below are minor or editorial.

This report was written blind: I read only the prompt and the packet, and I had no access to the internal audit, earlier referee reports, ledger or reconciliation notes.

| Severity | Count | Items |
| --- | --- | --- |
| Fatal | 0 | — |
| Major | 0 | — |
| Minor | 3 | M1 finite case omitted in the irreducible-closed-set classification (§6); M2 the (P\_i, N\_n) pairs *do* have far grids, so the choice a = ⋃P\_i is essential and should be motivated; M3 "coherent" used without a definition |
| Editorial | 6 | E1–E6 in Check 8 |

**What I reconstructed independently:** the basis axioms (all ten intersection types), T\_1, second countability, the subfitness inference, the closure criterion (3.1) from the neighbourhood bases, the four closure formulas (3.2), all ten rows of the farness table (by hand and by a mechanical cross-check over 36,145 disjoint basic pairs in a truncated model), identities (4.1)–(4.3), the far-grid obstruction with all quantifiers, non-sobriety, the classification of irreducible closed sets, countability and second countability of the soberification, noncompactness, and non-continuity.

**Standard results I accepted without reproof:** in a frame coproduct, u ⊕ v := ι₁(u) ∧ ι₂(v) preserves arbitrary joins in each coordinate (frame distributivity plus the injections being frame maps; equivalently the C-ideal condition); u\* ∨ v\* = 1 implies u ∧ v = 0; in O(X), u\* = X ∖ cl(u); T\_1 spaces have subfit open frames; a basis is a frame-theoretic notion, so frame-isomorphic spaces share second countability; algebraic ⇒ continuous.

## Check 1 — Topology and separation: correct

**Basis axioms.** The family covers X (q ∈ N\_1, r\_i ∈ R\_{i,∅,1}, p\_{i,k} ∈ A\_{i,∅}, s\_{i,t} ∈ T\_{i,t}). I checked every one of the ten intersection types, including the cross-type ones the packet only summarises:

| Intersection | Result | Basic or union of basics? |
| --- | --- | --- |
| A\_{i,F} ∩ A\_{i,G} | A\_{i,F∪G} (nonempty since P\_i infinite) | basic |
| A\_{i,F} ∩ R\_{i,G,m} | A\_{i,F∪G} | basic |
| A ∩ T, A ∩ N, A or R or T across blocks | ∅ | — |
| T\_{i,t} ∩ R\_{i,F,m} | {s\_{i,t}} if t ≥ m, else ∅ | basic |
| T\_{i,t} ∩ N\_n | {s\_{i,t}} if i ≥ n, else ∅ | basic |
| R\_{i,F,m} ∩ R\_{i,G,k} | R\_{i,F∪G,max(m,k)} | basic |
| R\_{i,F,m} ∩ N\_n | ∅ if i < n; ⋃*{t≥m} T*{i,t} if i ≥ n | union of basics |
| N\_n ∩ N\_k | N\_{max(n,k)} | basic |

All intersections are unions of basis members, so B is a basis. No subtlety arises from the infinite clouds here: cofinite sets are closed under finite intersection and remain nonempty.

**Countability and second countability.** Index sets: i ≥ 1, finite F ⊆ P\_i (countably many), m, n, t ≥ 1. The basis and X are countable; hence X is second-countable.

**T\_1.** I verified directly that X ∖ {x} is open for every x, by exhibiting for each other point y a basic neighbourhood avoiding x:

- x = q: r\_i ∈ R\_{i,∅,1}; p ∈ A\_{i,∅}; s ∈ T. None contains q.
- x = r\_i: q ∈ N\_1 (no N\_n contains any r); p\_{i,k} ∈ A\_{i,∅}; s\_{i,t} ∈ T\_{i,t}; other blocks via R\_j.
- x = p\_{i,k}: r\_i ∈ R\_{i,{p\_{i,k}},1}; other cloud points via A\_{i,{p\_{i,k}}}.
- x = s\_{i,t}: r\_i ∈ R\_{i,∅,t+1}; q ∈ N\_{i+1}; other s via T.

**Subfitness.** The packet uses: u ≰ v ⇒ ∃w with u ∨ w = 1 and v ∨ w ≠ 1. For opens u ⊄ v pick x ∈ u ∖ v and w = X ∖ {x}, open by T\_1. Then u ∪ w = X and v ∪ w = X ∖ {x} ≠ X. This matches the stated definition exactly and uses only T\_1. Correct.

No failure caused by the infinite cofinite clouds was found in this section; the clouds only matter from Check 2 onward.

## Check 2 — Closure formulas (3.1) and (3.2): correct

I rederived (3.1) from the neighbourhood bases, then (3.2) from (3.1).

**Neighbourhood bases.** p\_{i,k}: the sets A\_{i,F} with p\_{i,k} ∉ F (every R\_{i,F,m} containing p\_{i,k} contains such an A). s\_{i,t}: the singleton T\_{i,t}, so s-points are isolated. r\_i: the sets R\_{i,F,m}. q: the sets N\_n. These are the only basics containing the respective points.

**(3.1), point by point.**

- p\_{i,k} ∈ cl E iff every cofinite subset of P\_i avoiding p\_{i,k} meets E, iff p\_{i,k} ∈ E or E ∩ P\_i is infinite. (If E ∩ P\_i is finite and misses p\_{i,k}, take F = E ∩ P\_i.) Correct.
- s\_{i,t} ∈ cl E iff s\_{i,t} ∈ E, since s-points are isolated. Correct.
- r\_i ∈ cl E iff for all finite F and all m, E meets (P\_i ∖ F) ∪ {s\_{i,t} : t ≥ m}. If E ∩ P\_i is infinite, or E ∩ S\_i is infinite, every such set meets E. Conversely if both are finite and r\_i ∉ E, take F = E ∩ P\_i and m larger than every t with s\_{i,t} ∈ E; that R\_{i,F,m} misses E. Correct. The "tail filter" at r\_i is handled exactly: finitely many s-points can always be excluded, infinitely many cannot.
- q ∈ cl E iff every N\_n meets E, iff E meets S\_i for infinitely many i. Note that cloud points and the r\_i are invisible to q: no N\_n contains any p or r. So E ⊆ ⋃P\_i ∪ {r\_i} never accumulates at q. Correct, and this is what rules out unwanted accumulation at q in §4–§5.

**(3.2).**

| Basic | Closure | Reason |
| --- | --- | --- |
| A\_{i,F} | P\_i ∪ {r\_i} | A ∩ P\_i infinite; no s-points; meets no S\_j |
| T\_{i,t} | T\_{i,t} | clopen singleton |
| R\_{i,F,m} | P\_i ∪ {r\_i} ∪ {s\_{i,t} : t ≥ m} | as above; meets only one S\_i, so q is excluded |
| N\_n | N\_n ∪ {r\_i : i ≥ n} | N\_n ∩ S\_i = S\_i infinite for i ≥ n; N\_n ∩ P\_i = ∅ so no cloud points |

All four agree with the packet. The subspace topology on each P\_i is indeed the cofinite topology (the traces of basics on P\_i are exactly the cofinite sets), which is the one-line justification the packet gives.

## Check 3 — The complete farness table: correct, no offending pair

Write F\_i = P\_i ∪ {r\_i} and S\_i^{≥m} = {s\_{i,t} : t ≥ m}. Farness means disjoint closures, with closures from (3.2). I recomputed each row, with the boundary cases i = n, shared indices, and the finite exclusion sets F, G.

| Pair | Disjoint iff | Closures meet iff | Far iff | Packet row |
| --- | --- | --- | --- | --- |
| A\_{i,F}, A\_{j,G} | i ≠ j (same block: P\_i ∖ (F∪G) ≠ ∅) | F\_i ∩ F\_j ≠ ∅ iff i = j | i ≠ j | agrees |
| A\_{i,F}, T\_{j,t} | always | never | always | agrees |
| A\_{i,F}, R\_{j,G,m} | i ≠ j | i = j | i ≠ j | agrees |
| A\_{i,F}, N\_n | always | r\_i ∈ cl N\_n iff i ≥ n | i < n | agrees: **not far iff i ≥ n** |
| T\_{i,t}, T\_{j,u} | (i,t) ≠ (j,u) | equal | distinct | agrees |
| T\_{i,t}, R\_{j,F,m} | i ≠ j, or i = j and t < m | i = j and t ≥ m | i ≠ j or t < m | agrees (same condition) |
| T\_{i,t}, N\_n | i < n | i ≥ n | i < n | agrees |
| R\_{i,F,m}, R\_{j,G,k} | i ≠ j (r\_i shared otherwise) | i = j | i ≠ j | agrees |
| R\_{i,F,m}, N\_n | i < n | r\_i common iff i ≥ n; S\_i^{≥m} ∩ cl N\_n ≠ ∅ iff i ≥ n | i < n | agrees |
| N\_n, N\_k | never (q common) | — | vacuous | agrees |

In every row except (A, N), the disjointness condition and the farness condition coincide, so every disjoint pair is far. In the (A, N) row the two conditions differ precisely for i ≥ n, where cl A\_{i,F} ∩ cl N\_n = {r\_i}. The finite sets F, G never affect any row: they change neither the closure (3.2) nor disjointness, because cofinite subsets of an infinite set are nonempty and pairwise intersecting.

**Answer to the prompt's question 3:** yes, the (A\_{i,F}, N\_n) with i ≥ n are the only disjoint non-far basic pairs. I found no offending pair.

**Mechanical cross-check.** I also ran a script that encodes blocks i = 1..5 with P\_i and S\_i truncated to 8 points, F ranging over subsets of size ≤ 2, m, t ≤ 4, computes disjointness directly and farness from (3.2), and enumerates all unordered pairs. Of 36,145 disjoint basic pairs, exactly 165 are non-far, all of type (A\_{i,F}, N\_n) with i ≥ n meeting only at r\_i, and 165 is exactly the number of such pairs in the enumeration. This checks only the table against (3.2); (3.2) itself was verified by hand in Check 2, since truncation cannot model cofiniteness faithfully.

## Check 4 — Genuinely localic equality d\_I = d\_U: correct

The argument is a valid calculation in L ⊕ L. It uses nothing about points of the square and nowhere assumes L ⊕ L is spatial.

**Ingredients used, and their status.**

1. u ⊕ v = ι₁(u) ∧ ι₂(v), where ι₁, ι₂ are the coproduct injections (frame homomorphisms). Then (⋁u\_α) ⊕ v = (⋁ι₁(u\_α)) ∧ ι₂(v) = ⋁(ι₁(u\_α) ∧ ι₂(v)) by the frame distributive law. Likewise in the second coordinate. In the C-ideal presentation this is exactly the defining closure condition. Standard; accepted.
2. d\_U ≤ d\_I: if u\* ∨ v\* = 1 then u ∧ v = u ∧ v ∧ (u\* ∨ v\*) = 0. Standard; verified.
3. The farness-as-disjoint-closures translation u\* ∨ v\* = 1 ⇔ cl u ∩ cl v = ∅, valid because u\* = X ∖ cl u in O(X). Verified.
4. Every open is the join of the basis members below it. This is a statement in L = O(X), not in the square. Verified.

**(4.1).** N\_n = {q} ∪ ⋃(j ≥ n) S\_j = ({q} ∪ ⋃(j ≥ i+1) S\_j) ∪ ⋃(n ≤ j ≤ i) S\_j = N\_{i+1} ∪ ⋃(n ≤ j ≤ i) ⋃(t) T\_{j,t}. Correct for i ≥ n.

**(4.2).** Applying ingredient 1 in the second coordinate gives A\_{i,F} ⊕ N\_n = (A\_{i,F} ⊕ N\_{i+1}) ∨ ⋁(j,t) (A\_{i,F} ⊕ T\_{j,t}). Each summand is a far rectangle: (A\_{i,F}, N\_{i+1}) is far because i < i + 1 (table row 4), and (A\_{i,F}, T\_{j,t}) is far (row 2). So each summand is ≤ d\_U, hence the whole is. The transpose N\_n ⊕ A\_{i,F} follows identically (or from the symmetry of d\_U under the twist automorphism of L ⊕ L). Correct.

**Basis to arbitrary opens.** For disjoint u, v write u = ⋁(k) A\_k and v = ⋁(l) B\_l over basics below them. Each A\_k ∩ B\_l ⊆ u ∩ v = ∅. Applying ingredient 1 twice, u ⊕ v = ⋁(k,l) A\_k ⊕ B\_l, and each A\_k ⊕ B\_l ≤ d\_U by the table (far case) or (4.2) (the (A, N) case). So u ⊕ v ≤ d\_U, and joining over all disjoint pairs gives d\_I ≤ d\_U. Combined with ingredient 2, d\_I = d\_U as elements of L ⊕ L. Correct.

**Is any pointwise inference hidden?** No. The only place points appear is in computing closures in X to establish which basic pairs are far, and "far" is a property of pairs in L (u\* ∨ v\* = 1), not of the square. The passage from L to L ⊕ L is entirely via rectangles and ingredient 1.

**Remark worth adding to the packet.** The proof actually shows something sharper that illuminates why the far-grid converse fails: for every disjoint basic pair, u ⊕ v ≤ d\_U is witnessed by a *one-sided* decomposition (only the N-side is split). What the far-grid property demands, and what fails in Check 5, is a decomposition of a that works uniformly against every piece of b. The example is exactly a case where "u ⊕ v is a join of far rectangles" (true, by (4.2)) does not imply "u ⊕ v is a join of a product family of far rectangles".

## Check 5 — Far-grid nonexistence for a = ⋃P\_i, b = N\_1: correct, all quantifiers verified

a is open (a union of A\_{i,∅}) and b is a basic open; a ∩ b = ∅. Suppose a = ⋁ a\_α and b = ⋁ b\_β in L with every cross pair far. I checked each step against arbitrary families.

1. **Some b\_β₀ contains q.** Because q ∈ b = ⋃ b\_β (joins in O(X) are unions). No assumption on the family.
2. **b\_β₀ ⊇ N\_n for some n.** b\_β₀ is open and contains q; the N\_n are the only basics containing q, so they form a neighbourhood base there. A "cleverly chosen" sparse piece containing q cannot evade this: every open neighbourhood of q contains all of S\_i for all i from some n on. No piece can contain q without containing infinitely many whole discrete tails.
3. **Fix i ≥ n. Some a\_α₀ meets P\_i.** Because P\_i ⊆ a = ⋃ a\_α. This uses that *every* P\_i lies in a, which is why a must meet infinitely many clouds (see Minor M2).
4. **a\_α₀ contains a cofinite subset of P\_i.** Pick p ∈ a\_α₀ ∩ P\_i; some basic neighbourhood of p lies in a\_α₀, and the only basics containing p are A\_{i,F} and R\_{i,F,m} with p ∉ F, both ⊇ P\_i ∖ F. So a "sparse open piece meeting P\_i" does not exist: any open meeting P\_i is cofinite on P\_i.
5. **r\_i ∈ cl a\_α₀** by (3.1), since a\_α₀ ∩ P\_i is infinite.
6. **r\_i ∈ cl N\_n ⊆ cl b\_β₀** by (3.2), since i ≥ n.
7. Hence cl a\_α₀ ∩ cl b\_β₀ ∋ r\_i, so a\_α₀\* ∨ b\_β₀\* ≠ 1. Contradiction.

Nothing in steps 1–7 uses cardinality, disjointness, order, or basicness of the pieces; pieces may overlap, may be empty (irrelevant ones are never chosen), and may be nonbasic. The packet's quantifier structure is right.

**Why the pair must be chosen this way (Minor M2).** For a single cloud, a' = P\_i and b' = N\_n with i ≥ n, a far grid *does* exist: take a' undecomposed and decompose b' as in (4.1). Each cross pair (P\_i, N\_{i+1}) and (P\_i, T\_{j,t}) is far. So the disjoint non-far *basic* pairs are not themselves counterexamples to far grids. The obstruction needs a to contain P\_i for infinitely many i (so that whichever N\_n is swallowed by the q-piece, some i ≥ n is available) and b to contain q. I recommend saying this explicitly; it is the heart of why the example works, and a reader will naturally try the basic pair first and be puzzled.

I also confirmed that the obstruction does not need the full union: a = ⋃(i ∈ I) P\_i for any infinite I ⊆ ℕ works the same way, as does b = N\_k for any k. This is a robustness observation, not a correction.

## Check 6 — Boundary claims and soberification: all correct, one gap in exposition

None of these claims bears on the central theorem; an error here would be auxiliary. I found none, but one argument is incomplete as written.

**Non-sobriety.** F\_i = P\_i ∪ {r\_i} is closed (it is cl A\_{i,∅}). Every nonempty relatively open subset of F\_i contains a cofinite subset of P\_i: a relatively open set containing a cloud point does so by Check 5 step 4, and one containing r\_i contains R\_{i,F,m} ∩ F\_i ⊇ P\_i ∖ F. Two cofinite subsets of an infinite set meet, so F\_i is irreducible. In a T\_1 space point closures are singletons, so F\_i is not a point closure. X is not sober. Correct.

**Classification of irreducible closed sets.** B\_i = R\_{i,∅,1} is open; its complement {q} ∪ ⋃(j ≠ i) B\_j is open because q ∈ N\_{i+1} ⊆ complement and every B\_j is open. So B\_i is clopen. An irreducible closed C meeting a clopen K satisfies C = (C ∩ K) ∪ (C ∖ K) with both parts closed, so C ⊆ K. Hence an irreducible closed C is one of: {s\_{i,t}} (if it meets a clopen singleton); a subset of F\_i (if it meets B\_i but no s-point); or {q} (if it meets no block). Inside F\_i: if C ∩ P\_i is infinite then cl C ⊇ F\_i so C = F\_i. **If C ∩ P\_i is finite, C is a finite closed set, and a finite irreducible closed set in a T\_1 space is a singleton** (a set with ≥ 2 points is the union of two proper closed subsets). The packet's sentence "either a singleton or all of F\_i, since every infinite subset of P\_i has closure F\_i" justifies only the infinite case; the finite case is true but unstated. This is Minor M1. Conclusion unchanged: the non-point irreducible closed sets are exactly the F\_i, i ≥ 1.

**Soberification countable and second-countable.** X^sob = X ∪ {ρ\_i : i ≥ 1}, one new point per F\_i, so countable. O(X^sob) ≅ O(X) as frames, and "B is a basis" is a frame-theoretic property of a subset of O(X) (every element is a join of members of B), so the image of B is a countable basis of X^sob. Correct.

**Consequence worth stating explicitly.** In X^sob the new point ρ\_i has closure F\_i ∪ {ρ\_i} ⊇ P\_i, so X^sob is T\_0 but not T\_1. Since a spatial frame has a unique sober representation (its spectrum), **this frame L has no representation that is simultaneously sober and T\_1**. The packet says the example does not settle the sober-T\_1 version; it can say more strongly that this L cannot settle it.

**Noncompactness.** {N\_1} ∪ {B\_i : i ≥ 1} is an open cover (q ∈ N\_1, everything else in its block). Any finite subfamily omits some B\_j, and then P\_j ∪ {r\_j} is uncovered (N\_1 contains no cloud points or r-points). Correct.

**Non-continuity.** The sets D\_F = N\_{n+1} ∪ F, F a finite set of s-points from S\_1 ∪ … ∪ S\_n, are open (N\_{n+1} plus finitely many open singletons), directed, with union N\_1. No D\_F contains N\_n since D\_F ∩ S\_n = F ∩ S\_n is finite while S\_n ⊆ N\_n is infinite. So N\_n ≪ N\_1 fails for every n. If N\_1 were the join of elements way below it, q would lie in some w ≪ N\_1, w ⊇ N\_n for some n, and ≪ is down-closed in its first argument, so N\_n ≪ N\_1: contradiction. L is not continuous. Correct. Not algebraic follows (algebraic ⇒ continuous). "Not coherent" follows under the usual definition (coherent ⇒ algebraic), but the packet does not define coherent; see Minor M3.

**Historical aside (§7).** I cannot verify the earlier example, but the stated inference is sound in general: if a point p is isolated and not closed, then u = {p}, v = ∅ violate subfitness, since the only w with {p} ∪ w = X and p ∉ w would be X ∖ {p}, which is not open. So an isolated non-closed point does kill subfitness, as the aside says.

## Check 7 — Stress tests: no breach found

**Attempts to build a far grid for (a, b).** Every attempt I made runs into step 2 or step 4 of Check 5: a piece containing q contains infinitely many whole tails S\_i and therefore has r\_i in its closure for all large i; any piece meeting P\_i has r\_i in its closure. The two closure mechanisms (infinite cloud, infinite tail) both land on the same point r\_i and cannot be separated by any choice of opens. Decomposing a more finely does not help because every nonempty open piece of P\_i is cofinite in P\_i. Decomposing b more finely does not help because whichever piece gets q gets some full N\_n.

**Attempts to defeat the coproduct calculation.** Since Check 3 shows every disjoint basic pair other than (A, N) with i ≥ n is far, and (4.2) handles that case, there is no disjoint basic pair whose rectangle escapes d\_U. For nonbasic disjoint opens the reduction to basics in Check 4 is exhaustive. I tried the natural candidate u = ⋃P\_i, v = N\_1 (the very pair with no far grid): u ⊕ v = ⋁(i) A\_{i,∅} ⊕ N\_1 = ⋁(i) \[A\_{i,∅} ⊕ N\_{i+1} ∨ ⋁(j ≤ i, t) A\_{i,∅} ⊕ T\_{j,t}\], a join of far rectangles. So this pair lies below d\_U without having a far grid, exactly as the theorem requires. The decomposition of the N-side depends on which A-piece it is paired with; that dependence is what a grid forbids.

**Hidden hypotheses.** The argument uses: T\_1 (for subfitness and for the point-closure facts in §6), the explicit topology (for closures), and frame-coproduct algebra. Nothing stronger than subfitness is used in the statement. In fact T\_1 is strictly stronger than subfitness, so the example satisfies a stronger hypothesis than needed, which only makes the counterexample more informative: even T\_1 plus I = U does not yield far grids.

**Topological product vs localic product.** The packet never uses O(X × X). All square-side reasoning is in L ⊕ L through rectangles and the join laws. No conflation occurs. (For the record, L ⊕ L and O(X × X) might well differ here since X is not sober and not locally compact; the packet correctly avoids needing either way.)

**Is L accidentally regular or fit?** It is not regular: A\_{i,F} and N\_n with i ≥ n are disjoint opens with intersecting closures, so X is not even regular as a space, and the frame cannot be regular. This matters because regular frames have far grids trivially (see the research notes below), so a regular example would have been impossible.

## Check 8 — Presentation, repairs, originality

The packet is short, well organised and reads cleanly. Everything below is a suggested repair, with the location.

| ID | Severity | Location | Issue | Proposed repair |
| --- | --- | --- | --- | --- |
| M1 | Minor | §6, classification paragraph | Only the infinite case of "singleton or all of F\_i" is argued | Add: "if C ∩ P\_i is finite, C is a finite closed set, and a finite irreducible closed set in a T\_1 space is a singleton." |
| M2 | Minor | §5, choice of a, b | Not explained why a = ⋃P\_i rather than the offending basic pair (A\_{i,F}, N\_n) | Add one sentence: (P\_i, N\_n) does have a far grid via (4.1), so the obstruction needs a to meet infinitely many clouds. |
| M3 | Minor | §6, last sentence | "coherent" undefined; the inference depends on the definition | Either define (compact elements closed under finite meets and generating) or drop the word. |
| E1 | Editorial | §2, basis axioms | "every other intersection is empty or a union of indicated singleton basics" is vague for a referee | Replace with the explicit list of T ∩ R and T ∩ N (Check 1 table). |
| E2 | Editorial | §1 | Notation ⊠ for rectangles alongside ⊕ for the coproduct; the prompt uses ⊕ for both | Fix one symbol and say u ⊕ v := ι₁(u) ∧ ι₂(v) once. |
| E3 | Editorial | §5, first line of proof | "Some b\_β₀ contains q" | Add "since q ∈ b = ⋃ b\_β". |
| E4 | Editorial | §4, after (4.2) | The sharper phenomenon is not named | Add the remark: every disjoint basic rectangle is below d\_U via a one-sided split; a grid demands a uniform split, which (a, b) lacks. |
| E5 | Editorial | §6, soberification | The stronger negative fact is omitted | State that X^sob is not T\_1 (cl{ρ\_i} ⊇ P\_i), so L itself has no sober T\_1 representation. |
| E6 | Editorial | §3, line after (3.1) | "the tails in the R-neighbourhoods detect infinite subsets of S\_i" | Fine, but add the converse half: finitely many s-points are excluded by taking m large. |

**First-reading confusions.** (i) On first reading I expected the counterexample pair to be the offending basic pair and briefly thought §5 contradicted (4.2); M2 resolves this. (ii) The table's "When disjoint" column for (T, R) lists two conditions joined by "or" while other rows list one; a short note that disjointness and farness coincide in every row but (A, N) would make the table self-explanatory.

**Originality.** I did not conduct a priority search and the packet makes no novelty claim. Correctness here does not imply novelty: the construction (cofinite clouds attached to a limit point, with a separate point q accumulating along tails) is built from standard ingredients, and related separation-relation counterexamples may exist in the literature on subfit and T\_1 locales. Any eventual write-up should include a literature check before any claim beyond "this settles the question posed".

## What is settled, what is not

**Settled (verified).** There is a subfit frame L, namely O(X) for a countable second-countable T\_1 space, with I(L) = U(L) in the genuinely localic sense d\_I = d\_U in L ⊕ L, that does not have the far-grid property. So subfitness plus I = U does not imply far grids. Since X is T\_1, the same frame also shows that "L = O(X) with X T\_1, and I = U" does not imply far grids.

**Not settled by this packet.**

- The version requiring a representation that is **simultaneously sober and T\_1**. This L cannot serve (Check 6, consequence paragraph): its spectrum is not T\_1.
- Any version with hypotheses strictly between subfitness and regularity, such as **fit**, **Hausdorff** (for spatial L) or **prefit**. X is not Hausdorff: every neighbourhood of p\_{i,k} and every neighbourhood of r\_i contain cofinite subsets of P\_i, so they meet. Whether O(X) is fit I have **not** checked, and the packet makes no claim either way.
- Whether a **continuous** or **locally compact** example exists; this L is not continuous.
- Whether the far-grid property is equivalent to I = U under any natural additional hypothesis.

## Research notes (not verified conclusions)

1. **Regular frames have far grids trivially.** If L is regular, for disjoint a, b write a = ⋁{c : c ≺ a} and b = ⋁{d : d ≺ b}. Since d ≤ b ≤ a\*, we get d\* ≥ a\*\* ≥ a, so c\* ∨ d\* ≥ c\* ∨ a = 1. So the open range for the question is strictly between subfit and regular; **fit** is the natural next hypothesis to test. Is O(X) here fit? I would guess not (the pair A\_{i,F} ≰ N\_n-complement-type witnesses), but this needs checking.
2. **A Hausdorff candidate?** The same mechanism (two closure routes to one point) seems compatible with Hausdorffness if the clouds P\_i are replaced by convergent sequences in a Hausdorff setting while keeping q non-regular. A Hausdorff, non-regular, second-countable version would sharpen the result considerably.
3. **Sober T\_1 obstruction.** For a sober T\_1 space every irreducible closed set is a point, which rules out the "cloud with a phantom generic point" trick used here. The r\_i would have to be genuine limit points of P\_i in a T\_1 way, i.e., P\_i ∪ {r\_i} would need to be non-irreducible. Whether the obstruction survives is open and seems to be the real content of the stronger question.
4. **Characterisation.** The example suggests the right intermediate notion between I = U and far grids: "u ⊕ v is a join of far rectangles" (equivalent to I = U) versus "u ⊕ v is a join of a product family of far rectangles" (far grid). One could ask for the weakest frame property under which the first implies the second.

## Independence statement and signature

I examined only the prompt and the technical packet. I did not read, request, or have access to any author-side audit, prior referee report, theorem ledger, reconciliation note, or external discussion of this candidate. All closures, table rows, coproduct identities and boundary claims above were reconstructed independently; the mechanical cross-check script and its output are available on request.

Verdict: **accept the central theorem as correct**; minor repairs M1–M3 and editorial items E1–E6 recommended.

Signed: Claude (Fable 5.1), independent blind referee, 8 November 2026.