# Independent Referee Report — Project A, Q′ / W₂ packet (2026-11-09)

Nov 9, 2026 · @Someone

## Summary verdict

No structural theorem in the packet is false. Every labeled claim in Parts A and B that is stated with a proof (A1 identities, A2, A3.1–A3.3, B1, B2) is correct as written; the example ledger (Part C) is correct in substance, with four write-up gaps that are repairable from the packet's own material and none that reverses a conclusion. No counterexample to Q′ is produced, and no claim pretends otherwise.

The one place where the packet says less than it could: a five-line induction shows d\_W ∧ d\_U\* = 0, i.e. W ⊇ cl(int U) for every frame (Section 4). It proves two B3 bullets outright, shows that any A2 witness lies in the nonregular residual O(d\_U\*\*), and reclassifies C1, C3 and C4 as instances of the trivial case d\_U = 0. It also lets the local equalities (C.6) in C5 and C6 be upgraded to global W = W₂ = U in those spaces.

What I checked and how: every proof in A1–A3, B1, B2 line by line; C1–C7 at the level of the topologies, the frame-homomorphism property of H±, every-finite-cover compatibility, the closure tests and the density arguments. What I did not check: the hyperconnected half of B3 bullet 1, the claim that U is regular closed for all Alexandrov locales, the "branching factor" variant mentioned in C2, and anything in the linked source notes (I did not open them, per the prompt). Lemmas I took as known are listed in Section 1.

I did not consult any internal audit or prior referee report.

## 1. Foundations (A1): all three requested checks pass

Notation: I write a ⊕ b for the pure rectangle a ⊠ b, Q = L ⊕ L, and o\_w(x) = w → x for the open nucleus.

**Diagonal-cover presentation — correct.** Δ ⊆ O(q) iff δ\*(q) = 1. Writing q = ⋁ a\_i ⊕ b\_i gives a cover c\_i = a\_i ∧ b\_i with w\_C ≤ q and δ\*(w\_C) = 1, so the opens O(w\_C) are cofinal among opens containing Δ, and fit(Δ) = ⋂\_C O(w\_C). The finite-cover variant D₂ is a definition.

**Pre-nucleus identities — correct.** For covers C, C′ with pairwise-meet refinement C″, frame distributivity gives w(C) ∧ w(C′) = ⋁ (c ∧ c′) ⊕ (c ∧ c′) = w(C″); so the w(C) form a filter base, the join defining Φ is directed, and (w(C) → x) ∧ (w(C′) → y) ≤ w(C″) → (x ∧ y). Hence Φ and Φ₂ preserve binary meets and are pre-nuclei (a finite refinement of finite covers is finite). The sublocale ⋂ O(w(C)) has as nucleus the join in N(Q) of the open nuclei o(w(C)), which is the transfinite closure of the pointwise join Φ; its bottom is Φ^∞(0), and cl(S) = C(⋀S) for any sublocale S. So d\_W = Φ^∞(0), d\_0 = Φ₂^∞(0), and Φ₂(d\_0) = d\_0 holds with respect to all finite covers, answering D1 question 1.

**Φ(0) = Φ₂(0) = d\_U — correct, with the following proof (the packet asserts it).** Using (a ⊕ b)\* = (a\* ⊕ 1) ∨ (1 ⊕ b\*) and the fact that a rectangle is 0 iff a factor is 0: if a\* ∨ b\* = 1 then {a\*, b\*} is a (binary) cover with (a ⊕ b) ∧ w\_{{a\*,b\*}} = 0, so a ⊕ b ≤ w\* ≤ Φ₂(0). Conversely a rectangle u ⊕ v ≤ w\_C\* has (u ∧ c) ⊕ (v ∧ c) = 0 for all c ∈ C; partitioning C by which factor vanishes gives ⋁C₁ ≤ u\*, ⋁C₂ ≤ v\*, so u\* ∨ v\* = 1. Since every element is the join of the rectangles below it, w\_C\* ≤ d\_U.

**Factorization test (A.1) — correct, standard.** A frame map g : Q → M factors through O(w) iff g(w) = 1, and through an intersection of sublocales iff through each. The packet should state once that the test gives *sublocale equality* when applied to the generic pair of D₂ itself (the two coproduct injections composed with Q → D₂); this is what makes B1 a theorem rather than a statement about particular pairs.

**Lemmas taken as known.** (i) a ⊕ b = 0 iff a = 0 or b = 0; u ⊕ v ≤ a ⊕ b with u, v ≠ 0 iff u ≤ a and v ≤ b; rectangles join-generate Q. (ii) Sublocale–nucleus correspondence; joins of nuclei via iteration of a pre-nucleus. (iii) Proper locale maps are pullback-stable and K → 1 is proper iff K is compact (Vermeulen), used only in B1's "in particular". (iv) Ω(X × Y) ≅ ΩX ⊕ ΩY when X is locally compact (Johnstone / Picado–Pultr), used only in C2.

**One further foundational fact the packet uses silently (A2, A3.3, B2): closure commutes with restriction to an open sublocale.** Proof: for a sublocale S and u ∈ Q, u → ⋀S lies in S (sublocales are closed under x → (−) from S) and in O(u), so ⋀(S ∩ O(u)) ≤ u → ⋀S; hence cl(S) ∩ O(u) = cl\_{O(u)}(S ∩ O(u)). A companion fact used repeatedly below: O(q) ∩ S = 0 iff q ≤ ⋀S, so S ⊆ T is dense in T iff every rectangle s with O(s) ∩ T ≠ 0 has O(s) ∩ S ≠ 0.

## 2. Part A: all four claims correct

**Claim A2 (exact certificate) — correct.** Both directions check. (⇒) d(W) > d₀ forces Φ(d₀) > d₀, since Φ^∞(0) is the least Φ-fixed point and d₀ ≤ d(W). Some cover C has (w(C) → d₀) ≰ d₀; a rectangle r below it with r ≰ d₀ exists because rectangles generate; r ∧ w(C) ≤ d₀ is the adjunction. r ≤ Φ(d₀) ≤ Φ(d(W)) = d(W) ≤ d(I) and δ\*(d(I)) = 0 give a ∧ b = 0. If a finite F ⊆ C covered, r ∧ w(F) ≤ d₀ would give r ≤ Φ₂(d₀) = d₀. (⇐) r ≤ Φ(d₀), r ≰ d₀, so d₀ is not Φ-fixed while d(W) is. The phrase "no finite subcover" should read "no finite subfamily of C covers", which is what the proof gives.

Second paragraph of A2 — correct. D ∩ O(r) ⊆ O(w(C) ∧ r) ⊆ O(d(W)) and D ⊆ C(d(W)), so D ∩ O(r) = 0. D₂ ∩ O(r) is dense in W₂ ∩ O(r) by the closure–restriction fact (Section 1) and is nonzero because r ≰ d₀. The point argument (partition a cover by which coordinate evaluation accepts a member, then use the binary cover) is right, so pt D = pt D₂ and the remnant is pointless.

**Localized form of A2 (used below; not stated in the packet).** For any q ∈ Q: W ∩ O(q) ≠ W₂ ∩ O(q) iff there is a witness (A.2) with r ≤ q. Proof: the two closed sublocales of O(q) have bottoms q → d(W) and q → d₀, so inequality means q ∧ d(W) ≰ d₀; take the least α with q ∧ Φ^α(0) ≰ d₀ (a successor β+1), pick C and a rectangle r ≤ q ∧ (w(C) → Φ^β(0)) with r ≰ d₀; then r ∧ w(C) ≤ q ∧ Φ^β(0) ≤ d₀. This is what justifies deducing *local* W = W₂ statements from *local* D/D₂ statements in A3.3, B2 and B3.

**Claim A3.1 (chromatic) — correct.** Expanding (a ∧ u\_j) ⊕ (b ∧ u\_j) over pairs c, d in a colour class: diagonal terms are r ∧ (c ⊕ c) ≤ r ∧ w(C) ≤ d₀; off-diagonal terms are ≤ d₀ by non-adjacency. So r ∧ w({u\_j}) ≤ d₀ and r ≤ Φ₂(d₀) = d₀. The directed-union remark is also right: for directed Cᵢ with join uᵢ, w(Cᵢ) = uᵢ ⊕ uᵢ, so w(C) = w({uᵢ}).

**Claim A3.2 (rather-below localization) — correct.** (v ⊕ 1) ∧ (v\* ⊕ v\*) = 0, so r ∧ (v ⊕ 1) ∧ w({v\*} ∪ F) = r ∧ (v ⊕ 1) ∧ w(F) ≤ d₀, and {v\*} ∪ F is a finite cover. The proof uses nothing about r being a rectangle. Unstated corollary worth recording: in a regular frame t(C) = ⋁ over finite F of ⋁F = 1 for every cover, so regular frames satisfy W = W₂ directly from A2 (consistent with B1 at f = id).

**Claim A3.3 (compact closed complement) — correct.** Compactness of ↑(a ∨ b) gives finite F with a ∨ b ∨ ⋁F = 1; with a ∧ b = 0 the squares a ⊕ a and b ⊕ b meet r in 0, so r ∧ w({a,b} ∪ F) = r ∧ w(F) and D₂ ∩ O(r) ⊆ O(w(C)) for every C. The W-statement follows by closure–restriction. The conclusion "a witness needs C(a ∨ b) noncompact" follows since D ∩ O(r) = 0 ≠ D₂ ∩ O(r) for a witness. Note the immediate corollary (via the localized A2): every compact frame has W = W₂; in fact B1 with f : X → 1 gives D = D₂ for compact X. This matters for reading C2 (Section 5).

## 3. Part B: B1 and B2 correct; B3 partly verified from the packet alone

**Claim B1 (proper-over-regular) — correct; no hidden hypothesis.** First paragraph: from the finite cover {eᵢ∗} ∪ Fᵢ, meeting the compatibility equation with h(eᵢ) kills h(eᵢ) ∧ h(eᵢ∗) ∧ k(eᵢ∗) and leaves h(eᵢ) ≤ ⋁ over c ∈ Fᵢ of h(c) ∧ k(c); joining over i gives compatibility with C. Second paragraph: u(F) = f∗(⋁F) is directed in F with join f∗(1) = 1 (directed-join preservation; f∗(1) = 1 always); regularity of Y makes the v ≺ u(F) cover Y; the inverse image f⁻ preserves ≺ because f⁻(v∗) ∧ f⁻(v) = 0; and f⁻f∗(⋁F) ≤ ⋁F is the counit. All hypotheses are used, none is missing. Only directed-join preservation of f∗ is used, not closedness/Frobenius, so "proper" is more than needed. For Y × K → Y with K compact, properness is pullback stability of K → 1 (Vermeulen), fine. The step from "every compatible pair respects C" to the boxed D₂ = D requires applying the test to the generic pair of D₂; see Section 1.

**Claim B2 (completely join-prime boundary) — correct, and the density is genuine sublocale density (D1 question 3).** For s = u ⊕ v ≤ a ⊕ b nonzero we have u ≤ a, v ≤ b, so v ∧ a = u ∧ b = 0; the finite cover {a, b, n¹, n²} then has s ∧ w = 0 exactly as claimed, so some nᵢ meets both u and v and (u ∧ nᵢ) ⊕ (v ∧ nᵢ) is a nonzero rectangle below s with O(·) ⊆ O(nᵢ ⊕ nᵢ) ⊆ D. By the companion fact in Section 1 (density is tested on rectangles because O(q) ∩ S = 0 iff q ≤ ⋀S and q is a join of rectangles), ⋀(D ∩ O(r)) = ⋀(D₂ ∩ O(r)), so closures in Q agree and (B.2) follows by closure–restriction. The packet should spell out this last step; as written "D is dense in D₂ inside O(a ⊕ b)" could be misread as a point-set statement.

**B3 ledger.** I did not open the source notes. From the packet alone, using the lemma of Section 4:

| B3 bullet | Status | Reason |
| --- | --- | --- |
| Strips over compact closed C(k) (the h(cc) half of bullet 1) | Verified | A witness r = a ⊕ b ≤ k\* ⊕ 1 has a ≤ k\*, so the finite cover {k, b} ∪ F (F from compactness of C(k)) gives r ∧ w = r ∧ w(F); then D₂ ∩ O(r) = D ∩ O(r), contradicting the witness via localized A2; join over k. "C(e) compact ⇒ W = W₂" then follows by the finite cover {e} ∪ F. |
| Hyperconnected strips (the h(hc) half of bullet 1) | Not verified | A witness a ⊕ b ≤ h ⊕ 1 forces b ∧ h = 0, hence a\* ∨ b\* ≥ h ∨ h\*, which need not be 1; I did not find a short proof and did not look for a counterexample. |
| C(h(cc)) compact ⇒ D = D₂ (bullet 2) | Verified | For each compact C(kᵢ) a finite Fᵢ gives h(kᵢ\*) ≤ ⋁ over C of h(c) ∧ k(c); join to h(h(cc)); then the finite cover {h(cc)} ∪ F closes the argument. |
| Isbell Boolean criterion (bullet 3) | Verified | B(H₂) ⊆ D₂ always since D₂ ∩ O(d(U)**) is dense in H₂. (⇐) D ∩ O(d(U)**) ⊇ B(H₂) is dense in H₂, so W ⊇ W₂ ∩ O(d(U)**); and W ⊇ C(d(U)**) by Section 4; closed ∨ open covers W₂. (⇒) immediate. The spatial/atomic remark is right since pt D₂ = pt D. |
| U regular closed ⇒ W = W₂ = U (bullet 4) | Verified | Immediate from W ⊇ cl(int U) = C(d(U)\*\*) (Section 4). |
| U regular closed for every Alexandrov locale | Not verified | Not provable from the packet's content; needs the source note. |

## 4. A free lemma: W always contains cl(int U)

**Lemma.** For every frame L, d(W) ∧ d(U)∗ = 0; equivalently d(W) ≤ d(U)∗∗, i.e. C(d(U)∗∗) = cl(int U) ⊆ W. Hence

```latex
\operatorname{cl}(\operatorname{int}\,\mathcal U)\ \subseteq\ \mathcal W\ \subseteq\ \mathcal W_2\ \subseteq\ \mathcal U
```

*Proof.* Show Φ^α(0) ∧ d(U)∗ = 0 by induction on α. Limits are joins and ∧ distributes. For a successor, let x = Φ^α(0) with x ∧ d(U)∗ = 0, fix a cover C, and take a rectangle s = u ⊕ v ≤ (w(C) → x) ∧ d(U)∗. Then s ∧ w(C) ≤ x ∧ d(U)∗ = 0, so (u ∧ c) ⊕ (v ∧ c) = 0 for every c ∈ C, so each c is below u∗ or below v∗, so u∗ ∨ v∗ = 1 and s ≤ d(U). Together with s ≤ d(U)∗ this gives s = 0. Since (w(C) → x) ∧ d(U)∗ is the join of the rectangles below it, it is 0. ∎

The same induction with finite covers gives the same for Φ₂, and the computation inside the proof is exactly the one that gives Φ(0) = d(U).

**Consequences for the packet.**

1. Any A2 witness rectangle r satisfies r ≤ d(W) ≤ d(U)∗∗, so every witness lives in the nonregular residual O(d(U)∗∗). Q′ is therefore equivalent to W ∩ O(d(U)∗∗) = W₂ ∩ O(d(U)∗∗). This is the content of B3 bullet 3 and confirms that the design choice in C5–C7 (defect inside H₂) is the only one that can matter.
2. B3 bullet 4 (U regular closed ⇒ W = W₂ = U) is immediate. In particular, whenever d(U) = 0 (no far rectangles), W = W₂ = U = L ⊕ L.
3. C1, C3 and C4 all have d(U) = 0 (checked in Section 5), so their W = W₂ conclusions are instances of item 2; B2 is not needed for C3. They remain valid as D₂ ≠ D controls but say nothing about closure beyond item 2.
4. In C2, the lower bound K(Y) ⊆ W, which the packet asserts without argument, is item 2's inclusion cl(int U) ⊆ W.
5. Combined with the localized A2 (Section 2), the local equalities (C.6) in C5 and C6 upgrade to global W = W₂ = U (Section 5).

## 5. Part C: every example stands; four write-up gaps, none fatal

**Frame-homomorphism status of H₊ (C4–C7; D1 question 4) — correct, proof missing from the packet.** For a sheet R × P with P an Alexandrov poset of conditions and a target RO(R × K): joins are preserved because j(⋃ j(Vᵢ)) = j(⋃ Vᵢ). Finite meets: opens of R × P are up-closed in the P coordinate, so U(s) ⊆ U(t) for s ≤ t, and \[s\] ∩ \[t\] is \[s ∪ t\] or ∅; hence (U(s) × \[s\]) ∩ (V(t) × \[t\]) ⊆ (U ∩ V)(s ∪ t) × \[s ∪ t\], giving H₊(U) ∧ H₊(V) ≤ H₊(U ∩ V), and j(X) ∩ j(Y) = j(X ∩ Y) for opens. H₊(1) = 1 because ⋃ of the cylinders is dense. The mirrored H₋ is the same argument with the flipped cylinders. In C1 the extension from the basis c(F) is legitimate because every c(F) is compact, so the only covering relations are c(F) ⊆ c(G) for G ⊆ F, which the assignment respects.

**C1 (Scott/Cantor) — correct.** Scott opens of P(N) minus the empty set are the up-sets generated by their finite members, so the c(F) form a basis of compact opens. Every finite cover has a member containing infinitely many c(n) (each singleton {n} lies in some member, which is an up-set), and ⋁ of A(n) over an infinite set is 1 in RO(2^N). The infinite cover {c(n)} fails term by term. d(U) = 0 since every nonempty Scott open contains the top point N. So W = W₂ = U by Section 4, item 2.

**C2 (compact two-apex) — correct under the reading below; three gaps.** (i) "Neighbourhoods at p containing a cofinite positive tail" must mean: {p} ∪ V with V open in R and V ⊇ (0,∞) minus a finite set. Under the other natural reading ({p} ∪ (t,∞)) the space is the two-point compactification, Hausdorff, and the stated pt(U) is wrong; the packet should fix the definition. Under the cofinite reading I verified: Y is T₁ and compact; Y is locally compact (compact neighbourhood bases at p, q and at reals), so Ω(Y) ⊕ Ω(Y) ≅ Ω(Y × Y) and the "spatial-square model" is justified — this hypothesis should be stated (D1 question 8); pt(U) = A₊² ∪ A₋² ∪ {(p,q),(q,p)} exactly as claimed, because every open containing a point of \[0,∞) has p in its closure and every neighbourhood of p or q has 0 in its closure; int U = ((0,∞) ∪ {p})² ∪ ((−∞,0) ∪ {q})² and its closure is K(Y). (ii) The upper bound W₂ ⊆ K(Y): the binary cover w = (Y∖{p})² ∪ (Y∖{q})² is dense in Y², so cl(O(w)) alone kills nothing; the correct computation is W₂ ⊆ cl(O(w) ∩ C(d(U))) = C(w → d(U)), and w → d(U) = int(d(U) ∪ {(p,q),(q,p)}) = d(U) ∪ {(p,q),(q,p)} precisely because the cross pairs are relatively isolated in U. This is the step the packet compresses into "killed by a binary cover"; it is right, but it is a localic computation, not a point-set one (D1 question 5). (iii) The lower bound K(Y) ⊆ W is asserted without proof; it is Section 4. Also note: Y is compact, so D = D₂ (B1 with f : Y → 1) and W = W₂ is automatic; C2 tests the I < W < U pattern, not the finite-cover mechanism. The "branching factor" variant: not verified.

**C3 (join-prime gluing) — correct.** N(n) is the least neighbourhood of t(n), hence completely join-prime; finite-cover compatibility by pigeonhole on the t(n); infinite cover fails. B2 applies with a = A, b = B. But d(U) = 0 here too (every nonempty open contains a top point of a sheet, whose closure contains the sheet and all of T), so W = W₂ = U = X ⊕ X globally; the "four dense point pairs" remark is the same fact. C3 is therefore not a test of B2's mechanism beyond the trivial case.

**C4 (nonprincipal filter gluing) — correct.** Basis and topology check; ⋂ of the traces is empty. h(N(n,m)) = R × A(n) because E(m) is dense; finite-cover compatibility by pigeonhole; t(C) = 0 for the displayed cover because the closure of any nonempty open contains all of T. The θ maps are frame homomorphisms (projection preserves finite meets because any two nonempty opens of P meet). Every pair (θσ, τ∘θσ′) with σ, σ′ ∈ {A, B} and τ a rational translation is fully cover compatible, and the density inference is the right localic one: if a D-factoring pair g has g(u ⊕ v) = m ≠ 0, then O(m) → Q lands in D ∩ O(u ⊕ v), which is therefore nonzero. Again d(U) = 0, so the conclusion also follows from Section 4.

**C5 (coupled rational boundary) — correct; the strongest example.** Basis and countability check; T closed discrete. h, k are frame maps (above). Every finite cover: fix O × \[s\]; at q ∈ O some member U contains t(q,n) for infinitely many n; pick n ≠ n′ outside dom(s); then h(U) ∧ k(U) ≥ j((Iₙ ∩ Iₙ′) × A(n) ∩ B(n′)), which meets O × \[s\]. The argument handles every finite cover. The infinite cover fails term by term. Boundary-closure test t(q,n) ∈ cl(u) iff q ∈ cl(π(u)) is right (the meet (I ∩ Iᵢ) × ↑(Fᵢ ∪ {n}) is nonempty iff I meets Iᵢ). Every nonzero mixed rectangle has a far subrectangle (shrink to intervals with disjoint closures; then a∗ ∪ b∗ contains both sheets and every t(q,n)), so ρ ≤ d(U)∗∗ and the defect is inside H₂ (D1 question 6). Atomlessness on ρ holds (two disjoint parameter intervals inside any relatively open piece). Both point claims verified: pt(U) on A × B is the equal-parameter pairs; pt(D) additionally needs F ∩ G ≠ ∅, and ((q,H),(q,H)) with n ∈ H is a D-point because every cover member containing t(q,n) contains N(q,n,I) ∋ both. The far decomposition for disjoint projections (refine each interval into subintervals with closure inside it) is right. So D ∩ O(ρ) is dense in U ∩ O(ρ) and (C.6) holds.

*Upgrade to global (my observation, not a claim of the packet).* Any rectangle a ⊕ b with a ∧ b = 0 decomposes into pieces of the forms sheet⊕sheet, sheet⊕N, N⊕N. In C5 two pieces on the same sheet or involving boundary neighbourhoods are disjoint only if their parameter projections are disjoint (all finite conditions are compatible), and then the piece is ≤ d(U) by the far decomposition; the remaining pieces lie under ρ or its mirror. A witness r would then have a witness piece under ρ, contradicting (C.6) via the localized A2. Hence W = W₂ = U in C5.

**C6 (missing centre, finite flips) — correct after one repair.** Topology fine (ℓ(n), ℓ(m) are compatible for n ≠ m). No cross-sheet D-point: shrink I(n) to miss a given irrational. h, k frame maps; infinite cover fails. *Repair in the finite-cover proof:* as written, Baire is applied once to R and yields a colour class dense in *some* interval J, but the target O × \[s\] is arbitrary and O may miss J. Apply Baire inside O′ (the real open set with O = O′ ∩ R): the finitely many closures cl(Qᵢ) cover O′, so one contains an interval J ⊆ O′. Then "two same-colour centres with overlapping boundary intervals" is obtained by density, not assumed: take qₙ ∈ J of that colour with n ∉ dom(s), and qₙ′ ∈ Iₙ ∩ J of the same colour with n′ ∉ dom(s) ∪ {n}; then Iₙ ∩ Iₙ′ ∩ J is a nonempty open set around qₙ′ and h(Uᵢ) ∧ k(Uᵢ) ≥ j((Iₙ ∩ Iₙ′ ∩ R) × \[n=0, n′=1\]) meets O × \[s\]. With this the argument handles every finite cover. Same-orientation maps (θA, θB^E): fully cover compatible because every t(n) with n ∉ E contributes j((Iₙ ∩ R) × \[n=0\]) under both, and the join over such n is dense (rational centres outside E ∪ dom(s) are dense). Density on overlapping projections: choose E = the conflict set of the two conditions. *Second small gap:* the boundary-closure test differs from C5 — t(n) ∈ cl((I ∩ R) × ↑s) iff qₙ ∈ cl(I) and s(n) ≠ 1 — and the packet reuses C5's test implicitly. The far decomposition survives because cl(a) ∩ T ⊆ {t(n) : qₙ ∈ cl(I)} still holds. So (C.6) holds in C6 with no cross-sheet D-points, as claimed. The same decomposition as in C5 upgrades it to global W = W₂ = U: here same-sheet disjoint pieces with overlapping projections exist (incompatible conditions), but (θσ, θσ′^E) with E the conflict set shows D meets them.

**C7(a) — correct.** Centres with denominator in a finite set are discrete, so the dense colour class minus them is still dense; flips fixing cofinitely many labels still give full compatibility. **C7(b) — correct.** T(S) = {x : x(n) = 0 for n ∈ S} is perfect because N ∖ S is infinite, so b(T(S)) > 0 and b(T(S)) ≤ bₙ⁰ for n ∈ S (D1 question 7). The two-element cover {A ∨ N, B} forces k(N) = 1 since h(B) = 0 and h(A) = 1; (J₀ ∩ R) ⊠ b(T(S)) meets k(N) in 0 (n ∉ S by interval choice, n ∈ S by b(T(S)) ≤ bₙ⁰). Correctly scoped as a failure of one pair. **C7(c) — correct.** k(N₀) ∨ h(N₁) ≤ R × \[first bit = 1\] < 1.

**Logical direction (prompt item 4).** Q′ ⇒ Q is trivially right, and nowhere does the packet assert a global equality that was only proved on a rectangle; if anything it under-claims (C5, C6 are global).

## 6. Classification of every labeled claim

Statuses: **Correct**; **Correct after repair** (the fix is stated and uses only the packet's material); **Unresolved** (not checkable from the packet); **False** (none found). "Structural" = a theorem about all frames; "example" = a computation in one model.

| Location | Claim | Kind | Status | Note |
| --- | --- | --- | --- | --- |
| A1 | Diagonal-cover presentation of D | structural | Correct | §1 |
| A1 | Φ, Φ₂ are pre-nuclei; Φ^∞(0) = d(W), Φ₂^∞(0) = d₀ | structural | Correct | §1 |
| A1 | Φ(0) = Φ₂(0) = d(U) | structural | Correct | proof supplied in §1; packet asserts it |
| A1 | Universal inclusions | structural | Correct |  |
| A1 | Factorization test (A.1) | structural | Correct | standard; add the generic-pair remark |
| A2 | Exact certificate (A.2) iff W < W₂ | structural | Correct | "no finite subcover" → "no finite subfamily covers" |
| A2 | D ∩ O(r) = 0, D₂ ∩ O(r) nonzero dense pointless | structural | Correct | uses closure–restriction, §1 |
| A3.1 | Infinite chromatic number; directed-union remark | structural | Correct |  |
| A3.2 | (A.3); witness needs t(C) < 1 | structural | Correct | unstated corollary: regular ⇒ W = W₂ |
| A3.3 | (A.4); witness needs C(a ∨ b) noncompact | structural | Correct | corollary: compact ⇒ W = W₂ |
| B1 | D₂ = D for directed-join-preserving f∗ over regular Y; proper; Y × K | structural | Correct | only directed joins used |
| B2 | (B.2) under completely join-prime boundary | structural | Correct | density step should be spelled out |
| B3.1 | Strips over compact closed sublocales | structural | Correct | verified from §4 + localized A2 |
| B3.1 | Strips over hyperconnected opens | structural | Unresolved | not checked |
| B3.2 | C(h(cc)) compact ⇒ D = D₂ | structural | Correct | verified |
| B3.3 | Isbell Boolean criterion | structural | Correct | verified via §4 |
| B3.4 | U regular closed ⇒ W = W₂ = U | structural | Correct | immediate from §4 |
| B3.4 | U regular closed for Alexandrov locales | structural | Unresolved | not checked |
| C1 | D ⊂ D₂; W = W₂ = U = S ⊕ S | example | Correct | d(U) = 0 |
| C2 | Y compact; pt(U); K(Y) regular closed; I < W = W₂ = K(Y) < U | example | Correct after repair | fix topology wording; state local compactness; supply w → d(U) computation and the lower bound (§4) |
| C2 | Branching-factor variant | example | Unresolved | not checked |
| C3 | D ⊂ D₂ on A ⊕ B; N(n) completely join-prime; local W = W₂ | example | Correct | d(U) = 0, so global and trivial |
| C4 | D₂ ≠ D; t(C) = 0; θ frame maps; D dense pointless; W = W₂ = U | example | Correct | d(U) = 0 |
| C5 | Topology; h, k frame maps; every finite cover; infinite cover fails | example | Correct | frame-map proof supplied in §5 |
| C5 | Closure test; ρ ≤ d(U)∗∗; atomless residual | example | Correct |  |
| C5 | Point descriptions of U and D; (C.6) | example | Correct | upgrades to global, §5 |
| C6 | Topology; no cross-sheet D-points; frame maps; infinite cover fails | example | Correct |  |
| C6 | Finite-cover compatibility via Baire | example | Correct after repair | apply Baire inside the target interval; overlap by density |
| C6 | Same-orientation maps fully compatible; (C.6) with no D-points | example | Correct | closure test differs from C5; decomposition still works |
| C7(a) | Repeated labels: both conclusions survive | example | Correct |  |
| C7(b) | b(T(S)) > 0; mirrored pair not finite-cover compatible | example | Correct |  |
| C7(c) | Nested strings: binary-cover contradiction | example | Correct |  |
| D1/Exec | Q′ ⇒ Q; local vs global scoping | logic | Correct |  |

## 7. Exposition

**Ambiguities and missing definitions.**

- C2: the neighbourhood system at p and q is ambiguous (§5); write it out. State that the square is spatial because Y is locally compact, and name the theorem.
- A2: "infinite cover with no finite subcover" should be "no finite subfamily covers".
- C1: S² should be written S ⊕ S (the localic square); S does have a basis of compact opens, so its square happens to be spatial, but the argument never uses this and the notation should not suggest it does.
- C7(b): say explicitly what the target is (RO(R × P) with P the tree poset, or RO(R) ⊗ B) and that the order on trees is reverse inclusion; the computation is the same either way.
- "Atomless" (C2, C5): say which frame is meant (the frame of the sublocale W₂ ∩ O(ρ)) and what is being shown (every nonzero relatively open part splits into two disjoint nonzero parts).

**Unsupported shortcuts that should be written out once.**

- Closure commutes with restriction to an open sublocale (used in A2, A3.3, B2, B3) — three lines, §1.
- Density tested on rectangles: O(q) ∩ S = 0 iff q ≤ ⋀S (used in B2, C4–C6) — §1.
- The pair test proves sublocale equality when applied to the generic pair of D₂ (B1) — §1.
- The density inference from a D-factoring pair g with g(u ⊕ v) ≠ 0 (C4–C6): restrict g to the open sublocale O(g(u ⊕ v)) of the target.
- H₊, H₋ are frame homomorphisms (C4–C7) — §5.
- The localized A2 (§2), which is what turns local D/D₂ statements into local W/W₂ statements.
- C2's "killed by a binary cover" is the computation w → d(U) = d(U) ∨ {cross pairs}.

**Simplifications.**

- Put the lemma of §4 in Part A. It makes B3 bullets 3–4 one-liners, shows every witness is in the residual, and lets C1, C3, C4 be stated in one sentence each ("d(U) = 0, so W = W₂ = U; the example only shows D ⊂ D₂").
- Record the two corollaries of A3.2/A3.3: regular ⇒ W = W₂ and compact ⇒ W = W₂ (the latter already D = D₂ by B1). C2 is then flagged as a compact control.
- In B1, replace "proper" by "f∗ preserves directed joins" in the statement and keep "proper" only in the "in particular".
- C5 and C6 can be stated as global equalities W = W₂ = U once the decomposition remark (§5) is added; the mixed rectangle ρ is then just where the D₂ ≠ D defect sits.
- The C6 Baire paragraph should be rewritten with the target interval fixed first (§5).

## 8. Optional research input: two bounded suggestions, and a view

My view first: nothing in the packet points to a counterexample, and the lemma of §4 plus A3.1–A3.3 narrows any witness to a noncompact, non-rather-below, infinitely chromatic configuration inside the nonregular residual. Stopping the search and studying W as a relation is a defensible outcome. The two items below are the only bounded checks I see; neither is a research programme.

**Suggestion 1 — a no-go theorem for the sheet template (closes C5–C7 as a family, or finds the candidate).** C5, C6, C7 are instances of one template: sheets R × P over a condition poset P, boundary labels ℓₙ ∈ P at dense centres qₙ, target B = RO(P)-type Boolean algebra, mirrored pair (H₊, H₋). The packet's own arguments isolate two conditions. (N1) Finite-cover compatibility of the mirrored pair holds iff there is no nonzero b ∈ B and no set S of centres dense in an interval such that b ∧ \[ℓₙ\] ∧ \[ℓ̄ₘ\] = 0 for all distinct n, m ∈ S (Cohen forcing satisfies it, Sacks forcing violates it — that is exactly C7(b)). (N2) D is *not* dense in U ∩ O(ρ); the finite-flip rescue violates (N2) whenever any two conditions can be made compatible by an automorphism of B fixing cofinitely many labels. Conjecture: (N1) implies the rescue, so the template can never give W ≠ W₂. *First check (about a page):* take B = the measure algebra of 2^N and ℓₙ = "bit n = 0". (N1) holds since a positive-measure set decides only finitely many bits. Then test whether, for positive-measure s, t, some finite flip γ gives γ(t) ∧ s ≠ 0; by Lebesgue density (pick density points of s and t, flip the finitely many coordinates on which their initial segments differ) I expect yes. If so, both a Cohen-like and a random-like B are rescued and the conjecture is worth proving abstractly; if not, the measure algebra is the candidate to run through the full C6 argument.

**Suggestion 2 — exploit the weaker premise through the U-separation relation.** Define a ⊥ b iff a ⊕ b ≤ d(U) (a and b are "U-separated"; d(U) is the C-ideal generated by the far pairs). Since Φ₂(d(U)) = d(U) iff d₀ = d(U), one has

```latex
\mathcal W_2=\mathcal U\iff\Bigl[\forall F\text{ finite cover}:\ (\forall c\in F\ \ a\wedge c\perp b\wedge c)\Rightarrow a\perp b\Bigr]
```

and W = U is the same with arbitrary covers. So (Q) asks whether finite cover-locality of ⊥ implies full cover-locality, a statement about one binary relation on L with no sublocales in sight. *First check:* (a) verify the displayed equivalence (one line from Φ₂(d(U)) = d(U) and the adjunction); (b) sanity-test it on C2, where W₂ ≠ U: a = a neighbourhood of p, b = a neighbourhood of q, F = {Y∖{p}, Y∖{q}} should violate finite locality, and in the spatial square ⊥ is just a × b ⊆ d(U); (c) compute ⊥ explicitly in C5 (I expect: the parameter projections have disjoint closures, with boundary neighbourhoods counted through their sheet traces) and prove full cover-locality directly. If (c) goes through cleanly it is a second, nucleus-free proof of W = U there and a template for an abstract argument; if ⊥ in C5 turns out not to be describable by projections, the relation is less tractable than it looks and the idea should be dropped.