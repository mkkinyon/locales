# Referee report — Project A/C Dowker and higher diagonal phase (blind audit)

Nov 10, 2026 · @Someone

Independent blind audit of `ProjectAC_Dowker_EXTERNAL_BLIND_PACKET_2026-11-10.md`. No internal review or reconciliation of this phase was read.

## Executive verdict

**Correct after stated repairs. No numbered claim is refuted.** Every proposition, equality and example in §§1–9 survived an independent re-derivation. The repairs concern proof steps, the specification of the two sites, and two scope statements.

Three findings matter most.

1. **Claim 5.1 is true and can be strengthened.** For every q ≥ 1 the map s\_q is not even a descent morphism in Loc: it is not a pullback-stable regular epimorphism. The packet's scope note leaves effective descent open; it is settled negatively (Issue 1).
2. **Claims 6.2 and 7.2 are correct only once the sites are pinned down, and they are formal.** Both are instances of a Dowker lemma valid in any ∞-topos. Their whole content is that r\_p and s\_q are covers (Issue 2 and the section on meaning).
3. **The closed cover tests are not simplicial for a fixed cover.** C(b\_U^(n)) is stable under coordinate deletion but not under repetition. I^(•+1) is a limit of simplicial closed tests only over meet-closed covers (Issue 3).

Notation: I write f^∗ for the frame map of f, f\_∗ for its right adjoint, and keep the packet's symbols otherwise. Composition of relations is diagrammatic throughout.

| Packet item | Verdict |
| --- | --- |
| §1 universal chain Δ ≤ S ≤ I∧D, cl S = I, fit S = D | Verified for every locale |
| §1 coherent graph powers S² = J, S⁴ = U∨V, S^(2n) = I^n ∨ D^n | Verified; conditional on the prerequisite's Theorem B |
| §2 simplicial locales I^(•+1), D^(•+1) | Verified for every locale |
| §2 coherent point description; n = 3 example | Verified; conditional on the prerequisite's Lemmas 5.1, 6.1, 6.2 |
| Claim 3.1 (Čech identities) | Verified for every locale |
| §3 categorical crosswalk and four-point example | Verified against the source definitions |
| Claim 4.1 (proper rows) | Verified as a statement in Loc, after two added lines (Issue 5) |
| Claim 4.2 and both §4 examples | Verified; the non-open example needs one added line (Issue 4) |
| Claim 5.1 (triquotient failure, every q ≥ 1) | Verified; strengthened to failure of descent; a smaller example exists |
| Claim 6.1 (patch Čech preservation) | Verified |
| Claim 6.2 (patched comparison) | Correct after the site repair of Issue 2 |
| §7 identifications and Claim 7.1 | Verified for arbitrary frames and infinite covers |
| Claim 7.2 (unpatched frame-cover comparison) | Correct after the site repair; the classical reading of the K-side is conditional |
| Claims 8.1–8.4 | Verified degreewise; simplicial caveat in Issue 3 |
| Claim 9.1 and its limitation | Verified |

## Issue ledger

No issue is fatal. Two are major, four minor, seven presentational.

| # | Severity | Packet location | Objection | Repair |
| --- | --- | --- | --- | --- |
| 1 | Major (scope; strengthens the claim) | §5 “Scope of the proposed conclusion”; §6 “What is NOT claimed” | The note leaves open that s\_q is still effective descent. It is not. Pulling s\_q back along the sublocale {y} ∪ {y\_n} of D^(q+1) gives a map that is monic and epic but not invertible. | Replace the note by the theorem in the next section. Add that no subcanonical topology on a pullback-closed site of locales makes h(s\_q) an effective epimorphism. |
| 2 | Major (specification; affects meaning, not truth) | Claims 6.2 and 7.2; §6 finite-poset remark; §7 “underlying simplicial set” | The sites are underspecified. (a) With single surjections as the only covers, h of a discrete locale is not a coproduct of points, so neither the finite-poset remark nor the reading of K\_• as a simplicial set holds. (b) The size bound must exceed the index set and be closed under finite limits of locales; frame coproducts can raise cardinality. (c) The theorems of Vermeulen and Joyal–Tierney are not what makes the arrows effective epimorphisms. | Use κ-small Stone spaces with finite jointly surjective families (6.2), and κ-small locales with families whose copairing is an open surjection (7.2), κ a strong limit cardinal above card(I) and card(O(X)). State that effective epimorphisms come from the covers, and that the descent theorems supply subcanonicity. |
| 3 | Minor (gap in any simplicial reading) | Claim 8.4, last sentence; §8 | For fixed U, n ↦ C(b\_U^(n)) is stable under coordinate deletion (using that U covers) but not under repetition. Example: X discrete on {1,2,3}, U = ({1,2},{2,3},{1,3}). Then b\_U^(2) = 0, yet (x,y) ↦ (x,y,y) sends (1,3) into b\_U^(3). | Restrict to covers closed under finite meets and containing 1. For these, every coordinate map c satisfies c^∗(b\_U^(m)) ≤ b\_U^(n), and they are cofinal under concatenation. The fitted tests O(w\_U^(•+1)) = L\_•(R\_U) are simplicial for every U. |
| 4 | Minor (proof step) | §4 “Coherent nonopen example” | “The image of O is not open” is a statement about point sets. In a non-T\_D space a localic open map need not have open point-image. | Add: if ∃ were a left adjoint of s\_1^∗ with Frobenius, then (b\_∞,c\_∞) ∈ ∃(O), so ∃(O) ⊇ V\_n = {(b\_n,c\_n)} for large n. But ∃(O) ∧ V\_n = ∃(O ∧ s\_1^∗V\_n) = ∃(0) = 0. |
| 5 | Minor (proof step) | Claim 4.1, proof | Two steps are compressed. A closed subset of E\_{p,0} is down-closed only relative to E\_{p,0}. And “closed” must mean the localic identity r\_∗(u ∨ r^∗v) = r\_∗(u) ∨ v. | Both hold. The move from ((x\_i),y) to ((x\_i'),y) stays inside E\_{p,0}. For sober spaces a closed continuous map f satisfies the identity, because f(C) minus an open set is closed when f(C) is. |
| 6 | Minor (scope) | §4, first display | K\_p(A) = I^(p+1) and L\_q(A) = D^(q+1) are coherent statements. The packet does not record what survives in general. | In every locale Δ ≤ K\_p(A) ≤ I^(p+1) and Δ ≤ L\_q(A) ≤ D^(q+1). Hence cl K\_p(A) = I^(p+1) and fit L\_q(A) = D^(q+1). Proof below. |
| 7 | Presentation | §0, §1 | The order of composition is never stated. AB = I, BA = D, cl(S) = A∘S∘B and fit(S) = B∘S∘A hold for diagrammatic composition only; the functional convention swaps all four. | State the convention, as the prerequisite does in its (0.1). |
| 8 | Presentation | §2 “Coherent point-description claim” | The n-ary description is attributed to the hull calculus, whose displayed formula is binary. | Cite the prerequisite's Lemmas 5.1, 6.1 and 6.2 with Z = X^n. They are stated for an arbitrary coherent Z. |
| 9 | Presentation | §5, list of separating sets | The listed clopen up-sets do not separate b\_∞ from c. Every other pair is separated. | Add the tails {b\_∞} ∪ {b\_n : n ≥ N}. With them the space is Priestley. |
| 10 | Presentation | §5, definition and proof | The equality form of the assignment forces f\_# f^∗ = id. Other sources use two inequalities plus f\_# f^∗ = id. Directed-join preservation is never used in the refutation. | Say that the refutation covers both forms, and excludes every map satisfying the two identities, Scott-continuous or not. |
| 11 | Presentation | Claims 8.1 and 8.3 | The meet runs over a proper class of indexed families. Also, covers with n+1 members already suffice for the closed formula in every locale. | Restrict to covers with at most n+1 members (closed) and to subfamilies of O(X) (fitted). In 8.3 the content of the closed half is “compact opens”, not “finite”. |
| 12 | Presentation | §7, K\_p; §3, pointwise remark | The ordered-tuple simplicial set is identified with the usual nerve complex without a source. | Cite Brun–Fosse–Salbu, Corollary 6.7. |
| 13 | Presentation | §3 “Categorical crosswalk” | The source works over Set only. The “internal-locale version” is a definition by analogy, and the source's theorem is used nowhere in the packet. | Say so. Add that chaotic relations are Dowker relations in the source's sense, which is what recovers the pointwise theorem. |

**Proof for Issue 6.** In O(E\_{p,0}(A)) one has π\_i^∗(a) ≤ π\_y^∗(a) for every open a and every i. A rectangle a\_0⊠⋯⊠a\_p with zero meet therefore pulls back below π\_y^∗(a\_0∧⋯∧a\_p) = 0. So E\_{p,0}(A) → X^(p+1) factors through C(d\_(p+1)) = I^(p+1), and the diagonal X → E\_{p,0}(A) gives Δ ≤ K\_p(A).

Dually, an open w containing the diagonal of X^(q+1) contains a join of powers c⊠⋯⊠c (q+1 factors), taken over a family of opens c that covers 1. This is the packet's proof of Claim 8.1. In the frame of E\_{0,q}(A) each such power pulls back above π\_x^∗(c), so w pulls back to 1.

Equality can fail outside the coherent class. If X is totally unordered then A = Δ and K\_p(A) = Δ\_(p+1), which is closed for p = 1 only when X is strongly Hausdorff.

## Claim 5.1 strengthened: s\_q is not a descent morphism

**Theorem.** Let X be the coherent locale of packet §5 and let q ≥ 1. Then s\_q : E\_{0,q}(A) → D^(q+1) is not a pullback-stable regular epimorphism in Loc. Hence it is not a descent morphism, not an effective descent morphism, and not triquotient.

This argument is the referee's and is new to the packet, so the authors should check it. It uses only the two identities the packet already proves.

Write E = E\_{0,q}(A), B = D^(q+1), s = s\_q, and keep y, y\_n, z, O, W, V\_n from §5. Let V be the open set {y\_n : n ≥ 1}, the join of the V\_n. Let T be the set of points (a; y\_n), n ≥ 1, together with (d; y).

1. **The test sublocale.** Let N be the sublocale of B induced by the subset {y} ∪ {y\_n : n ≥ 1}. Each {y\_n} is open in N. The point y is not isolated in N, because an open of B containing y contains z, hence y\_n for large n.
2. **The pullback.** The pullback P of s along N is the sublocale of E whose congruence θ is generated by the pairs (s^∗u, s^∗v) with u ∩ N = v ∩ N. Its points are T, and restriction of opens to T is a frame map ρ from O(P) to the power set of T.
3. **A complemented pair.** W ∩ N = V ∩ N, so s^∗W θ s^∗V. The packet proves O ∧ s^∗V = 0 and O ∨ s^∗W = 1. Hence the class o of O and the class c of s^∗V are complements in O(P).
4. **Below c.** Each point (a; y\_n) is open in E. So ρ maps the part of O(P) below c isomorphically onto the power set of {(a; y\_n) : n ≥ 1}.
5. **Below o.** Let G ≤ O be open. If (d; y) ∉ G then G ≤ s^∗W, so G = G ∧ s^∗W θ G ∧ s^∗V = 0. If (d; y) ∈ G then G ∨ s^∗W = 1, so G ∨ s^∗V θ 1; meeting with O gives G θ O. The part below o is {0, o}, and o ≠ 0 because ρ(o) = {(d; y)}.
6. **P is discrete.** By 3–5, ρ is an isomorphism. So P is the discrete locale on T, and the pulled-back map g : P → N is the identity on points.
7. **g is epic and monic but not invertible.** g^∗ is injective, so g is epic. A map h : Z → P is a partition of 1 in O(Z) into complemented opens h\_t, t ∈ T. Since each {y\_n} is open in N, the composite g∘h determines every h\_t over a y\_n, and the remaining piece is their complement. So g is monic. It is not invertible because {y} is not open in N.
8. **End.** A regular epimorphism that is monic is invertible. So g is not a regular epimorphism, and s is not a pullback-stable one.

### Consequences

- **Claim 5.1 follows.** Triquotient maps are pullback-stable regular epimorphisms (Plewe), so s\_q is not triquotient. Open and proper are excluded the same way.
- **No Čech descent on the D-side.** Let C be a full subcategory of Loc closed under pullbacks and containing E, B and N, with a subcanonical topology. Then h(s\_q) is not an effective epimorphism: otherwise h(g) would be monic and effective epic, hence invertible, and h is fully faithful. The Čech nerve of s\_q therefore realizes to a proper subobject of h(D^(q+1)).
- **What does hold unpatched.** Take proper surjections as covers. The internal Dowker lemma (section on meaning, below) gives an equivalence between the realization of h(I^(•+1)) and that of the image sheaves of h(s\_•). For q ≥ 1 those image sheaves are proper subsheaves of h(D^(q+1)). Whether h(I^(•+1)) and h(D^(•+1)) have equivalent realizations by another route is open.
- **The §4 example too.** The same proof applies to the packet's “coherent nonopen example”, with y = (d,d), y\_n = (b\_n,c\_n) and O the condition “witness in U”. That s\_1 is not a descent morphism either.

### The packet's refutation as one frame identity

**Lemma.** Let f\_# satisfy f\_#(u ∧ f^∗v) = f\_#(u) ∧ v and f\_#(u ∨ f^∗v) = f\_#(u) ∨ v. If O ∨ f^∗W = 1 and O ∧ f^∗V = 0, then ¬V ∨ W = 1, where ¬V is the pseudocomplement of V.

Proof: G = f\_#(O) satisfies G ∨ W = f\_#(1) = 1 and G ∧ V = f\_#(0) = 0, so G ≤ ¬V.

In §5 neither W nor ¬V contains y, where V = {y\_n : n ≥ 1}. This is the packet's argument with the points removed, and it answers the “fully localic” question. The only point-level input is the computation of the opens of E and B, which is legitimate because both are spatial by the prerequisite.

### A smaller counterexample

The element c can be deleted. Take the patch space {a, d, b\_∞} ∪ {b\_n : n ≥ 1} with b\_n → b\_∞, and strict relations a < b\_n, a < b\_∞, d < b\_∞ only. It is Priestley: the complement of {d}, the complement of {a}, the singletons {b\_n}, and the tails {b\_n : n ≥ N} ∪ {b\_∞} with or without d separate every pair.

For q ≥ 1 put y = (d,…,d), z = (b\_∞,…,b\_∞) and y\_n = (b\_n, b\_(n+1), …, b\_(n+1)). The witness fibres are {d}, {a, d, b\_∞} and {a}. With O the condition “witness ≠ a”, and W, V\_n as before, every step above goes through.

In the packet, c only stops b\_n from being its own witness; two consecutive terms do the same. No finite poset can work, by Claim 4.2, and q = 0 is excluded because s\_0 has a section.

## Cluster-by-cluster table

All seven clusters hold; clusters 3 to 6 carry the repairs.

| Cluster | Packet items | Finding | Rests on |
| --- | --- | --- | --- |
| 1. Arbitrary-locale algebra | §1 universal chain; §2 simplicial hulls; bisimplicial E and simplicial K, L; Claim 3.1; Claim 4.2 for s\_0 | Verified as sublocale statements. The proofs use only finite limits, preimages (which preserve all meets of sublocales) and the universal property of the image. I found no use of associativity of composition or of images commuting with pullback. | Basic structure of Loc only |
| 2. Coherent spectral specialization | §1 graph powers; §2 point description; K\_p(A) = I^(p+1), L\_q(A) = D^(q+1); Claim 4.1; finite cases of Claim 4.2; finite non-proper example | Verified. Proper rows hold in Loc: r\_p is spectral, so its right adjoint preserves directed joins, and r\_p is closed. For finite posets s\_q is open; already for the 3-point poset s\_0 is not closed. | Prerequisite Theorems A, B and Lemmas 5.1, 6.1, 6.2. Vermeulen for the effective-descent corollary. |
| 3. Triquotient obstruction | Claim 5.1; §4 non-open example | Verified for every q ≥ 1: Priestley property (after adding tails), the three fibres, both Frobenius identities, closedness of {y}, openness of {y\_n}. Strengthened: s\_q is not a descent morphism. Simplified: a poset without c. | Prerequisite, for spatiality of E and B. Plewe only for the implication to triquotient. |
| 4. Patched homotopy comparison | Claims 6.1, 6.2 | 6.1 verified; the shortest proof is that Patch is right adjoint to the inclusion of Stone spaces in spectral spaces. 6.2 is correct once the coherent topology is fixed. Evaluating at the point recovers the classical Dowker equivalence of the point relation. | Site repair (Issue 2). Standard facts: covers give effective epimorphisms; sheafified Yoneda is left exact. |
| 5. Frame-cover unpatched comparison | §7 identifications; Claims 7.1, 7.2; refinement and contiguity; pointless example | Identifications and 7.1 verified for arbitrary frames and infinite covers. Only the decidable predicate “v ≠ 0” is used, never points; K\_p is discrete because every sublocale of a discrete locale is a subset. 7.2 is correct once the site is fixed. Contiguity and the RO(S¹) example verified. | Classical logic. Site repair (Issue 2). Joyal–Tierney for subcanonicity. |
| 6. Higher diagonal reconstruction | Claims 8.1 to 8.4 | Both universal formulas verified for arbitrary frames. The coherent reduction and its prime-filter point description verified. Both test systems are directed. Caveat: the closed tests are not degeneracy-stable for a fixed cover (Issue 3). | Frame algebra only; the prime ideal theorem for points in 8.3 |
| 7. Refinement and simplicial span | §7 refinement maps; Claim 9.1; §9 limitation | Verified. Q\_• is the base change of a map of Čech nerves along I^(•+1), so the span is simplicial and natural in the pair (U, α). The stated limitation is right: the span alone carries no homotopical information. | Classical logic; pullback-stability of open surjections |

## Status of results

Nothing is refuted; the conditional and unverified items are listed so they are not mistaken for certified ones.

### Verified (re-derived in full for this report)

- §1: Δ ≤ S ≤ I∧D, cl S = I and fit S = D in every locale.
- §2: I^(•+1) and D^(•+1) are simplicial; they are in fact stable under every coordinate map X^n → X^m.
- §3: E is bisimplicial, K\_• and L\_• are simplicial sublocales, and Claim 3.1.
- Claim 4.2, the 3-point non-proper example, the n = 3 example and the four-point example.
- Claim 5.1, once the tails are added to the list of separating sets.
- Claim 6.1.
- §7: the formulas for E, K, L; Claim 7.1; refinement and contiguity; the pointless example.
- Claims 8.1, 8.2, 8.3 and 8.4, read degreewise.
- Claim 9.1 and its limitation.
- New in this report: the bounds of Issue 6, the non-descent theorem, the smaller counterexample, and the meet-closed repair of Issue 3.

### Conditional on named prerequisites

- §1 graph powers, the §2 point description, K\_p(A) = I^(p+1), L\_q(A) = D^(q+1), and spatiality of every E\_{p,q}(A): on the prerequisite's Theorems A and B and Lemmas 5.1, 6.1, 6.2. I read those proofs, found no gap, and re-derived the image lemma independently.
- Claim 4.1 itself is verified; its corollary “effective descent” rests on Vermeulen's theorem.
- “Triquotient implies pullback-stable regular epimorphism and effective descent”: Plewe.
- Claims 6.2 and 7.2: on the site repairs of Issue 2, and on two standard facts recalled from Lurie's Higher Topos Theory, §6.2: covering families give effective epimorphisms, and sheafified Yoneda preserves finite limits.
- Subcanonicity of the open-surjection topology: Joyal–Tierney.
- The crosswalk: on Definitions 3.1 and 4.1 to 4.3 and Theorem 4.6 of Brun–Fosse–Salbu.

### Unverified

- Whether the constant-object functor from spaces to H\_op is fully faithful, or H\_op has a point that is the identity on discrete locales. Without one of these, the realization of h(K\_•(R\_U)) is known only as the constant object on the classical nerve.
- Whether h(I^(•+1)) and h(D^(•+1)) have equivalent realizations in some unpatched topos by a route other than Čech descent.
- The §0 assertion that composition fails to associate outside the coherent class. It rests on a project file I did not open.
- Any identification of U with an independently defined Urysohn relation. Read as U := cl(D), the packet's I² = U is verified.
- The original texts of Plewe, Vermeulen and Joyal–Tierney, and all questions of priority.

### Refuted

- No numbered claim and no example.
- Two readings should be withdrawn: that s\_q might still be effective descent (Issue 1), and that Claim 8.4 exhibits I^(•+1) as a limit of simplicial closed tests over arbitrary covers (Issue 3).

## What “point-free Dowker equivalence” means here

It is an equivalence between the colimits, in a chosen sheaf ∞-topos, of the simplicial representables h(K\_•) and h(L\_•). It is not an equivalence of simplicial locales and not a statement about shape.

| Reading | Patched, Claim 6.2 | Frame-cover, Claim 7.2 |
| --- | --- | --- |
| Realizations of representable sheaves | Yes. This is the statement. | Yes. This is the statement. |
| The original simplicial locales | No. The packet gives no map between K\_• and L\_•, only the zigzag through E, and only the patches enter. | No. Again only a zigzag through E. |
| Classical point-set nerves | Yes, by evaluating at the point. Every covering family of the point has a section, so global sections preserve colimits, and one gets the classical equivalence for the relation on points. | K-side: the constant object on the ordered nerve, provided coproduct families are covers. L-side: no point-set meaning. Evaluation at 1 is not a point of H\_op, because a nonzero pointless locale covers 1 without a section. |
| Shape of the locale X | No. | No. The cover U = (1) gives the terminal object for every X ≠ 0, as the packet says. |

### What carries the content

Both claims are instances of one lemma.

**Internal Dowker lemma.** In any ∞-topos, let R → X×Y be a monomorphism. Define E\_{p,q} by the packet's finite limits, and let K\_p, L\_q be the images of E\_{p,0} → X^(p+1) and E\_{0,q} → Y^(q+1). Then the realizations of K\_•, E\_{•,•} and L\_• are equivalent.

Proof: Claim 3.1 holds in any finitely complete category, an effective epimorphism is the colimit of its Čech nerve, and colimits commute.

Given the lemma, Claims 6.2 and 7.2 say one thing: h sends the localic images K\_p, L\_q to the sheaf images. That holds because r\_p and s\_q are covers. So the mathematical content of §6 is “surjections of Stone spaces are covers”, and the content of §7 is Claim 7.1. Everything after that is standard descent.

The new information lies in the identification of the terms: patched I^(•+1) and D^(•+1) for R = A, the discrete ordered nerve and O(w\_U^(•+1)) for R\_U. For R = A unpatched, the hypothesis fails on the L-side in every subcanonical topology, by the theorem above.

### Three remarks on interpretation

- **The patched statement sees only Patch(R).** It is Dowker duality for a closed relation between Stone spaces. For R = A it concerns the closed partial order of a Priestley space; the spectral topology enters only through the order.
- **The cover's Čech nerve is already inside E.** For a cover U, the column p ↦ E\_{p,0}(R\_U) is the Čech nerve of the open surjection T\_U → X, so it realizes to h(X) in H\_op. The maps r\_• then give the canonical comparison from h(X) to the realization of h(K\_•(R\_U)). A nerve lemma would say this comparison is a shape equivalence; the packet rightly claims nothing of the kind. The other direction of E replaces each open O(v) by its Čech nerve over a point, which remembers only whether v ≠ 0.
- **D^(•+1) is the limit of the L-sides.** By Claim 8.1 and L\_q(R\_U) = O(w\_U^(q+1)), D^(•+1) is the meet over all covers U of the simplicial sublocales L\_•(R\_U). Realization does not commute with this limit, so no shape statement follows.

## Verdicts on the seven questions of packet §10

1. **All-locale equations and coordinate repetitions.** Yes to both. The equations are identities of sublocales. Repetitions act on both hulls; the D case works because preimage preserves arbitrary meets of sublocales. Repetition does fail for the fixed-cover closed tests (Issue 3).
2. **Properness in Loc.** Yes. The argument proves the localic identity r\_∗(u ∨ r^∗v) = r\_∗(u) ∨ v and Scott-continuity of r\_∗, once the two lines of Issue 5 are added.
3. **Priestley, and fully localic.** Yes, after adding the tails (Issue 9). The refutation is the frame statement ¬V ∨ W ≠ 1; points are used only to compute opens of two spatial locales.
4. **Patched identities and the two equivalences.** The Čech identities are correct. The sites need Issue 2. Standard descent: everything after “r\_p and s\_q are covers”. New information: which locales K\_• and L\_• are.
5. **Pointless locales and infinite covers.** Handled correctly. The index nerve is discrete because sublocales of a discrete locale are subsets, and only “v ≠ 0” is decided.
6. **Simplicial span.** Yes. It is a base change of a map of Čech nerves, and it is natural for specified refinements.
7. **Silent assumptions.** None found on associativity, on points of nonzero locales, or on identifying sublocales by points. Point reasoning needed a bridge in two places, Issues 4 and 5, and both bridges exist.

## Source crosswalk, antecedents and simpler routes

The crosswalk to [Brun–Fosse–Salbu](https://arxiv.org/pdf/2303.16032) is accurate at the level of definitions, and none of the packet's equivalences uses their theorem.

| Packet statement | Kind | Check |
| --- | --- | --- |
| Bisimplicial rectangle object; proof of Dowker duality for sets by rows and columns | Prior published method | The [rectangle complex of Brun–Salbu](https://ar5iv.labs.arxiv.org/html/2207.02018); Definition 3.1 and Theorems 4.5, 4.6 of Brun–Fosse–Salbu |
| E\_{p,q}(R) is the rectangle nerve of Pair(R) → Pair(X)×Pair(Y), and K\_p its Dowker nerve | Formal deduction for sets; definition by analogy for locales | Matches Definitions 3.1 and 4.3, because R → X×Y is monic. The source works over Set and has no internal or sheaf-valued version. |
| Nonempty witness sets have contractible chaotic nerves, which recovers the pointwise theorem | Formal deduction | These nerves are the source's Dowker fibres (Definition 4.1). So chaotic relations are Dowker relations (Definition 4.2) and Theorem 4.6 applies. |
| Order-category relation: both Dowker nerves are NP; four-point example | Formal deduction | Follows from Definition 4.3: a chain has its top as upper witness and its bottom as lower witness. Homology of the example checked by machine. |
| Claim 3.1 | Formal deduction | Finite limits only |
| Claims 6.2 and 7.2 | Formal deduction, given the covers | Internal Dowker lemma. I know of no published statement in this generality and did not search systematically. |
| Claims 4.1, 5.1, 7.1, 8.1 to 8.4, 9.1; coherent point descriptions | Need proofs specific to locales | The proofs are present and correct after the repairs. I did not find them in the sources accessed. Priority not assessed. |

### Antecedents the packet does not cite

- [Arrieta–Picado–Pultr (2022)](https://research.birmingham.ac.uk/en/publications/a-new-diagonal-separation-and-its-relations-with-the-hausdorff-pr/) study locales whose diagonal is fitted. [Arrieta (2023)](https://arxiv.org/abs/2310.18522v1) treats closedness and fittedness as dual and shows that strong Hausdorff does not imply a fitted diagonal. These are direct antecedents of D = fit Δ and of the I/D duality. The prerequisite cites the first; the packet cites neither. Abstracts only.
- [Janelidze–Sobral](https://baes.uc.pt/bitstream/10316/11557/1/Finite%20preorders%20and%20topological%20descent.pdf) and [Clementino–Hofmann](https://estudogeral.sib.uc.pt/bitstream/10316/11336/1/On%20some%20special%20classes%20of%20continuous%20maps.pdf) characterize descent, effective descent and triquotient maps of finite spaces by lifting chains. That bears on the finite case of Claim 4.2, and it explains §5: the convergence y\_n → y has no lift. Excerpts only.
- Corollary 6.7 of Brun–Fosse–Salbu: the simplicial set Sing(K) of ordered tuples has the homotopy type of K. This is the source needed in Issue 12.
- With the coherent topology, the site of Claim 6.2 is the site of condensed sets, up to the size convention. Naming it would help readers. From memory; no source opened.
- Yoon, *Dowker duality, profunctors, and spectral sequences* (arXiv:2408.13136) may bear on the categorical crosswalk. I saw only its citation.

### Simpler routes

- **A represents the order.** A map Z → A is a pair of maps f ≤ g from Z to X; this is immediate from the defining relations. So E\_{p,q}(A) represents families f\_i ≤ g\_j, and r\_p, s\_q are restriction maps. This gives §3 and §4 for R = A without coordinates.
- **Patch is a right adjoint.** A spectral map from a Stone space S to X is the same as a continuous map from S to Patch X. So Patch preserves the limits in Claim 6.1.
- **Order duality explains the asymmetry.** Reverse the order and keep the patch topology; this is the de Groot dual. On points, s\_q for X is r\_q for the dual, and D^(q+1) of X is I^(q+1) of the dual. So s\_q is a proper surjection for the dual topologies. The failure in §5 is a mismatch between the fitted side and the chosen topology, and patching is the symmetric repair.

## Access record

I read the prompt, the packet and one prerequisite file in full; no internal audit or reconciliation of this phase was opened or requested.

| Document | Access | Used for |
| --- | --- | --- |
| Blind prompt and blind packet (10 November 2026) | Read in full | The audit |
| [Coherent composition canonical proof (8 November 2026)](https://github.com/mkkinyon/locales/blob/main/ProjectA_coherent_composition_canonical_proof_2026-11-08.md) | Read in full; this file only | Conventions; Theorems A to C; Lemmas 5.1, 6.1, 6.2; identity (7.9) |
| [Brun–Fosse–Salbu, arXiv:2303.16032](https://arxiv.org/pdf/2303.16032) | Fetched; definitions and theorem statements extracted | Crosswalk |
| [de Silva et al., arXiv:2506.10909](https://arxiv.org/abs/2506.10909v1) | Abstract and journal listing | Existence; Journal of Applied and Computational Topology 10(2), 2026 |
| Cameron–Kumar, arXiv:2610.14783 | Not read. Existence confirmed from an arXiv listing and [the first author's blog](https://cameroncounts.wordpress.com/) | Provenance only |
| Plewe (1997), Vermeulen (1994), Joyal–Tierney (1984) | Originals not accessed. Definitions of proper and triquotient checked against excerpts of [arXiv:1509.08229](https://arxiv.org/pdf/1509.08229) and [arXiv:2207.05116](https://arxiv.org/pdf/2207.05116) | Named dependencies |
| Arrieta–Picado–Pultr (2022), Arrieta (2023), Janelidze–Sobral, Clementino–Hofmann | Abstracts or excerpts | Antecedents |
| Chowdhury–Mémoli; other repository files | Not opened | None |

Two disclosures. The prerequisite's header says it consolidates a referee report and reconciliation from the earlier coherent-composition phase; that is the permitted prerequisite, not a review of this packet. A web search for the Cameron–Kumar paper also returned the repository's front-page description; I did not open the repository.

### Machine checks

A script checked the examples; every check passed. It is a sanity check, not a proof.

- Exact, finite: the n = 3 example; homology of the four-point order complex and of both witness complexes; the 3-point non-proper example including failure of the co-Frobenius identity; the arc cover; the degeneracy counterexample of Issue 3.
- Exact, on 60 random finite posets: the §1 relation identities up to S⁶, the hull formulas, r\_p closed and s\_q open for p, q ≤ 2, and Claim 8.1 for n = 2, 3.
- Truncated to sequence indices 1 to 9 plus the limit: Priestley separation for the §4 and §5 posets and for the smaller poset, the gap in the packet's list of separating sets, and for q = 1, 2 the fibres and both identities O ∨ s^∗W = 1 and O ∧ s^∗V\_n = 0.

The non-descent theorem, the internal Dowker lemma, Claim 4.1 in the infinite case and all arbitrary-frame claims were checked by hand only.