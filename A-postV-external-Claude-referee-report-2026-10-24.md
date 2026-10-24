# Referee report — Project A post-V hierarchy packet (24 Oct 2026)

Oct 24, 2026 · @Someone

## Overall verdict

No fatal gap was found. Every headline claim checks out: C1–C3, R1–R5, the κ-recursion with Sₙ = 𝓘^(2n+1) and first stabilization at exactly ω+m, both diamond examples, and the thickening's boundary transfer. Three findings: (i) in three places the packet invokes the scattered-sublocale theorem R2 where a short elementary argument suffices, so the examples are more robust than stated; (ii) the term "almost normal" is used in a nonstandard sense and should be defined; (iii) several arguments admit one-line simplifications.

| Cluster | Verdict | Note |
| --- | --- | --- |
| A. Definitions, point formulas, universal hull identities, lower-diamond criteria | Correct | Frame theory only |
| B. Priestley/fittedness representation; C1, C2, C3 | Correct | R4 re-proved directly; standard inputs: Priestley/Hochster duality, Urysohn on compact Hausdorff quotients |
| C. Two-ray example R1–R5 | Correct | R5's separation argument replaceable by a point argument |
| D. κ-recursion, Sₙ = 𝓘^(2n+1), ω+m examples | Correct | Exact ordinal confirmed; no off-by-one |
| E. Compact T₁ upper diamond | Correct | R2 not needed: T₁ + scattered ⟹ fit |
| F. Compact three-boundary-point lower diamond | Correct | R2 not needed; "not almost normal" verified in the packet's sense |
| G. Noncompact thickening, 𝒲-boundary transfer | Correct conditional on a named lemma | Locally compact ⊕ spatial is spatial; no supplementary source needed |

Conventions: sublocales are subsets S ⊆ Q closed under meets and Heyting implication; C(a) = ↑a, O(w) = {w → x}; points of a sublocale are the prime elements it contains; ordinary points of L ⊕ L for spatial L are pairs (x,y). "Internally transitive" is read as π₁₂⁻¹𝓗 ∧ π₂₃⁻¹𝓗 ⊆ π₁₃⁻¹𝓗 in L^⊕3, equivalently the image of the composable-pair pullback under π₁₃ lies in 𝓗.

## A. Definitions, point formulas, and general lattice-hull lemmas — correct

**A1. Standing containments.** The non-immediate ones re-derived:

- 𝓘 ⊆ 𝒰: if a\* ∨ b\* = 1 then a ∧ b = (a ∧ b) ∧ (a\* ∨ b\*) = 0, so d\_𝒰 ≤ d\_𝓘.
- 𝒟 ⊆ 𝒰 (hence 𝒲 ⊆ 𝒰, as 𝒰 is closed): for a\* ∨ b\* = 1 put w = (a\* ⊠ 1) ∨ (1 ⊠ b\*). Then ∇(w) = a\* ∨ b\* = 1, so Δ ⊆ O(w) and 𝒟 ⊆ O(w); and w ∧ (a ⊠ b) = 0, so O(w) ⊆ C(a ⊠ b). Intersect over all such rectangles. No spatiality used.
- 𝓕 is closed **and fitted** (this makes 𝓗 ⊆ 𝓕 universal; the packet leaves it implicit): ker f is the pullback of Δ\_ℝ along f ⊕ f; 𝒪(ℝ) ⊕ 𝒪(ℝ) ≅ 𝒪(ℝ²) is regular, hence fit, so every sublocale of it (Δ\_ℝ included) is closed and an intersection of opens; preimage of sublocales is a right adjoint, so it preserves intersections and sends O(u) to O(f\*u).
- 𝒰 ⊆ 𝓕: in the regular frame 𝒪(ℝ), a ∧ b = 0 implies a ⊠ b = ⋁ aᵢ ⊠ b with aᵢ\* ∨ b\* = 1, and f(a)\* ∨ f(b)\* ≥ f(a\* ∨ b\*) = 1; so ker f = C((f ⊕ f)(d\_ℝ)) ⊇ C(d\_𝒰).

**A2. Point formulas.** All four verified for spatial L and ordinary points (x,y). The 𝒟 formula needs exactly what the packet says (the cover ⋁ U\_z ⊠ U\_z has codiagonal 1) and is correctly flagged as a statement about points only.

**A3. Hull identities (§2).** cl preserves finite joins since cl(S) = C(⋀S) and ⋀(S ∨ T) = ⋀S ∧ ⋀T. The step left implicit is that fit also preserves finite joins; it follows from the coframe law for sublocales:

```latex
\bigcap_i O(u_i) \vee \bigcap_j O(v_j) = \bigcap_{i,j} O(u_i \vee v_j)
```

With that, T(𝒥) = (𝓘 ∨ 𝒲) ∧ (𝒱 ∨ 𝒟) = 𝒲 ∧ 𝒱, and the absorption identities cl(𝒲 ∨ 𝒱) = cl 𝒱, fit(𝒲 ∨ 𝒱) = fit 𝒲 follow as stated. 𝓗 is well defined (intersections of closed-and-fitted sublocales are closed and fitted), and 𝒲 ∨ 𝒱 ⊆ 𝓗 ⊆ 𝓕 is correct.

**A4. Lower-diamond criteria (§7, first display).** Both biconditionals and the remark "𝓘 fitted ⟹ both sides equal 𝓘" are correct; the ingredients are 𝒲 ⊆ cl 𝒱, 𝓘 ⊆ 𝒲, and closedness of 𝒲.

**A5. Two tools used repeatedly below** (elementary; not stated in the packet):

- *Points of a binary join.* A prime p ∈ S ∨ T is s ∧ t with s ∈ S, t ∈ T, and primality forces p = s or p = t. So pt(S ∨ T) = pt S ∪ pt T for any two sublocales.
- *Spatial sublocales are joins of their points.* For S spatial and T arbitrary, pt S ⊆ pt T already gives S ⊆ T. Closed sublocales of spatial frames are spatial.

## B. Priestley/fittedness representation and the coherent 𝓗/𝓕 theorems — correct

Accepted from literature: coherent frames are spatial; Priestley/Hochster duality (R3), including that L ⊕ L is coherent with Priestley space P × P; Priestley separation of a closed upset from a closed downset; closed equivalence relations on compact Hausdorff spaces have compact Hausdorff quotients; Urysohn's lemma.

**B1. R4, re-proved directly.** Let G ⊆ K be a filter of compact opens, S = ⋂G (a patch-closed upset), N = ⋂\_{u∈G} O(u) with frame {x : u → x = x for all u ∈ G}. Points of N are the points lying in every u ∈ G, i.e. S. *Spatiality:* let x ≰ y in N; pick compact k ≤ x with k ≰ y. If every point of S ∩ k lay in y, the compact sets k ∖ y and S = ⋂G would be disjoint, so by patch-compactness some u ∈ G has u ∩ k ⊆ y, i.e. u ∧ k ≤ y, whence k ≤ u → y = y — contradiction. So some s ∈ S ∩ k ∖ y is a point of N separating x from y. Only compactness of the patch topology is used; coherence of N (as Idl(K/θ\_G)) is true but not needed anywhere in the packet. The caution not to extend R4 to arbitrary fitted sublocales is right: the Booleanization of a Stone space is a fitted, pointless, nonzero sublocale of a coherent frame.

**B2. Corollary (the workhorse).** *A closed sublocale C of a coherent frame is fitted iff its point set is an upset.* (⟸) S = pt C is patch-closed and an upset, so fit\_K(S) := ⋂{O(u) : u ∈ K, S ⊆ u} is spatial with points S by B1; C is spatial with the same points; two spatial sublocales with equal point sets coincide. (⟹) fitted sublocales have upward-closed point sets. The packet's phrase "has the same embedded points, hence is fitted" is valid only because *both* sublocales are spatial; this should be said.

For closed spatial C with points S: fit(C) = fit\_K(↑S) (any w with C ⊆ O(w) contains the compact S, hence some compact u ⊇ ↑S with u ≤ w), so pt fit(C) = ↑S and cl fit(C) has points ↓↑S. In particular pt 𝒱 = ↑𝓘\_pt, pt 𝒟 = ↑Δ\_pt, and pt 𝒲 = ↓↑Δ\_pt = 𝓘\_pt² = pt 𝒰 (the last by a directed-compactness argument), confirming 𝒰 = 𝒲 in the coherent case.

**B3. C1.** 𝓗 is closed, hence spatial, with point set S₀ patch-closed, a downset (closed) and an upset (fitted), containing Δ\_pt; coordinatewise comparability-saturation is exactly "upset and downset in the product order". Every candidate S gives, by B2, a closed fitted C\_S ⊇ Δ, so 𝓗 ⊆ C\_S and S₀ ⊆ S; S₀ is itself a candidate. Correct. Compactness of the patch space enters in B1 and nowhere else.

**B4. C2.** Points of ker f are the pairs with f(x) = f(y). Continuous f is patch-continuous and constant along ≤, so pt 𝓕 ⊇ E₀. Conversely, for a patch-closed equivalence E ⊇ ∼\_c, P\_patch/E is compact Hausdorff; a separating Urysohn function pulls back to a patch-continuous f constant on ≤-classes, so each f⁻¹(V) is a patch-open upset, i.e. spectral-open. Correct.

**B5. C3.** For closed sublocales of L^⊕3 (coherent, spatial), π₁₂⁻¹𝓗 ∧ π₂₃⁻¹𝓗 ⊆ π₁₃⁻¹𝓗 holds iff it holds on points, so internal transitivity equals pointwise transitivity of pt 𝓗 in the coherent case. 𝓗 is symmetric (the twist automorphism preserves Δ, closedness and fittedness, so fixes the least such sublocale). If pt 𝓗 is transitive it is a patch-closed equivalence containing ≤, so pt 𝓕 ⊆ pt 𝓗 and 𝓕 ⊆ 𝓗 by point-determination of closed sublocales. Converse: pt 𝓕 is an equivalence relation. Correct.

## C. Two-ray example and localic nontransitivity — correct

- **Priestley check.** The order is patch-closed (every nonconstant convergent sequence of comparable pairs tends to (t,t)). Total order-disconnectedness is not automatic from compactness plus a closed order, so it was checked: for x ≠ t, ↑x is a finite set of isolated points, hence a clopen upset; for x = t, ↓y is finite and isolated, so P ∖ ↓y is a clopen upset containing t.
- **R1.** R is an upset and a downset (comparabilities never cross components) and patch-closed (its complement consists of isolated points). By B2, C\_R is closed and fitted.
- **R2.** Any candidate S for C1 contains {a₀} × A (saturate the second coordinate along the zigzag), then A², B², (t,t); patch closure adds A × {t} and its transpose. So pt 𝓗 = R.
- **R3.** (a₀,t), (t,b₀) ∈ R and (a₀,b₀) ∉ R. The point (a₀,t,b₀) lies in the pullback and its image point lies outside 𝓗, so π₁₃\[pullback\] ⊄ 𝓗 whatever the precise definition of composition.
- **R4.** ∼\_c has classes A, B, {t}; the least patch-closed equivalence containing it is P².
- **R5.** pt 𝒰 = 𝓘\_pt² and pt 𝒱 = ↑𝓘\_pt (B2) both lie in K = A² ∪ B² ∪ {(t,t)}. By A5, pt(𝒰 ∨ 𝒱) = pt 𝒰 ∪ pt 𝒱 ⊆ K, which omits (a₀,t) ∈ 𝓗. Together with 𝒰 = 𝒲 ⊆ 𝓗 and 𝒱 ⊆ 𝓗, this is a sublocale-level strict inclusion witnessed by a point. The packet's clopen-upset separation argument is correct but unnecessary.

Since 𝒰 = 𝒲 here, the example also shows 𝒲 ∨ 𝒱 ⊊ 𝓗 **strictly, even in the coherent case**: 𝓗 is a transfinite closure, not a one-step join.

## D. κ-recursion, coherent odd powers, exact ω+m — correct

**D1. Frame facts.** F\_a is the set of w with C(a) ⊆ O(w); the frame of fit C(a) is Fix\_a, closed under meets, so κ(a) = ⋀Fix\_a ∈ Fix\_a and cl fit C(a) = C(κa). a ∈ Fix\_a (for w ∈ F\_a, w → a ≤ (w → a) ∧ (w ∨ a) ≤ a), so κ(a) ≤ a; monotonicity and "κ(a) = a ⟺ C(a) fitted" hold as stated. The chain stabilizes; C(a\_∞) is closed and fitted and contains Δ; any closed fitted C(b) ⊇ Δ has b ≤ d and κ(b) = b, so b ≤ a\_α by induction. **𝓗 = C(a\_∞) holds.** The limit-stage remark is correct: C(⋀a\_β) is the closed hull of ⋁C(a\_β).

**D2. Coherent recurrence.** By B2, S\_{α+1} = ↓↑S\_α. At limits, ⋀\_β a\_β in the frame is the interior of the set-intersection, so pt C(a\_λ) = cl\_spec ⋃S\_β = ↓cl\_patch ⋃S\_β (the ↓ is redundant, since patch closures of downsets are downsets, but harmless). 𝓘\_pt = cl\_spec Δ\_pt = ↓Δ\_pt is the common-upper relation; ↓↑R = 𝓘 ∘ R ∘ 𝓘 coordinatewise; S₀ = 𝓘; hence

```latex
S_n = \mathcal I_{\mathrm{pt}}^{\,2n+1},\qquad \bigcup_n S_n = {\sim_c},\qquad S_\omega = {\downarrow}\operatorname{cl}_{\mathrm{patch}}(\sim_c).
```

Two-ray: S\_n never contains (a₀,t), and S\_ω = R = S\_{ω+1}.

**D3. ω+m handles.** Priestley: the order is patch-closed (same argument as C); for x ≠ t₀, ↑x is a finite clopen upset; for x = t₀ and y ∉ {t₀,t₁}, ↓y is finite and avoids t₀, so P ∖ ↓y is a clopen upset. This holds for every m. Finite stages stay in A² ∪ T². At S\_ω the closure adds exactly A × {t₀} ∪ {t₀} × A (no other limits), and ↓ adds nothing since t₀ is minimal. Successor step: ↑T\_k = T\_k ∪ {t\_{2k+1}} (t\_{2k} < t\_{2k+1} is the only new upper bound) and ↓ of that adds exactly t\_{2k+2}; no common upper bounds exist beyond adjacent odd vertices, so one step moves the handle frontier by exactly two edges. S\_{ω+m} = P² ≠ S\_{ω+m−1} (the latter misses (a₀,t\_{2m})).

Both natural conventions — "first α with S\_α = 𝓗" and "first α with S\_{α+1} = S\_α" — coincide in general: S\_{α+1} = S\_α means C(a\_α) is fitted, hence equals 𝓗 by minimality. **Exactly ω+m; no off-by-one.**

## E. Compact noncoherent upper diamond — correct (R2 not needed)

**E1. Topology.** Open sets are exactly those whose boundary points impose the stated cofinite conditions; basic neighborhoods are open. T₁, not Hausdorff, compact, locally compact (basic neighborhoods are compact), sober (every closed set with two points splits off a clopen sheet singleton or a T₁ boundary point), scattered, noncoherent via N₁. By R1 (Hofmann–Lawson/Isbell: locally compact sober factors), L ⊕ L = 𝒪(X × X); X × X is T₁ and scattered.

**E2. The general lemma, with an elementary proof replacing R2.**

*Lemma.* If Y is a T₁ scattered space, then 𝒪(Y) is **fit**: every closed sublocale is fitted; consequently every sublocale of 𝒪(Y) is fitted.

*Proof.* Let F = Y ∖ d be closed. An open v lies in Fix\_d iff w → v = v for every open w ⊇ F, i.e., writing G = Y ∖ v, iff G = cl(G ∩ w) for every such w. Suppose G ⊄ F. Then G ∖ F is nonempty and open in G; scatteredness gives z ∈ G ∖ F isolated in G ∖ F, hence isolated in G. Then w = Y ∖ {z} is open (T₁), contains F, and cl(G ∩ w) = G ∖ {z} ≠ G. So Fix\_d ⊆ ↑d, κ(d) = d, and C(d) is fitted. Every sublocale is an intersection of sublocales C(a) ∨ O(b), and C(a) ∨ O(b) = ⋂ᵢ O(cᵢ ∨ b) by the coframe law, so all sublocales are fitted. ∎

Applied to Y = X × X: 𝒟 = fit Δ = Δ, 𝒱 = fit 𝓘 = 𝓘, hence 𝓗 = 𝓘 (𝓘 is closed, fitted, contains Δ), 𝒲 = cl 𝒟 = 𝓘, 𝒥 = 𝓘, 𝓜 = Δ. The packet's "rank-two bar" is simply the open complement of the point (x,y) in the T₁ space Y, and its "total spatiality" step is exactly what the lemma supplies without appeal to Niefield–Rosenthal, Simmons, or BPP Prop. 5.3.

**E3. Boundary relations.** pt 𝓘 = Δ ∪ {αβ, βα, βγ, γβ}; (α,γ) ∈ pt 𝒰 since β lies in the closure of every α- and every γ-neighborhood; sheet points are clopen, so no off-diagonal pair involving one lies in 𝒰 or 𝓕; f(α) = f(β) = f(γ) for continuous f. So pt 𝒰 = pt 𝓕 = Δ ∪ {α,β,γ}² and 𝒰 = 𝓕 by point-determination of closed sublocales (only spatiality of the square is needed). The chain

```latex
\Delta=\mathcal D=\mathcal M\subsetneq\mathcal I=\mathcal J=\mathcal W=\mathcal V=\mathcal H\subsetneq\mathcal U=\mathcal F
```

holds, and 𝒰 ∨ 𝒱 = 𝒰 ⊄ 𝓗. Combined with §4, both universal comparisons between 𝒰 ∨ 𝒱 and 𝓗 are refuted. This example is also a compact T₁ witness that 𝒲 ⊊ 𝒰 outside coherence.

## F. Compact three-boundary-point lower diamond — correct (R2 not needed)

**F1. Topology (L1–L2).** Basic sets are open (N\_x ⊆ N\_p). Open sets are characterized by: p ∈ U ⟹ x ∈ U and cofinite traces on S₁, S₂; x ∈ U ⟹ cofinite S₁; y ∈ U ⟹ cofinite S₂. Specialization: p < x only (all pairs checked; sheet points are clopen). Closed subsets of {p,x,y}: {p}, {y}, {p,x}, {p,y}, {p,x,y}; the irreducible ones are the point closures of p, y, and x (= {p,x}), so X is sober. Compact, locally compact, first-countable, scattered, noncoherent via S₂. R1 gives L ⊕ L = 𝒪(X × X).

*Non-interpolation of ≺.* cl A = {p,x} ∪ S₁ ⊆ B₀; any open C ⊇ cl A contains p, hence a cofinite part of S₂, hence y ∈ cl C ∖ B₀.

**Terminology flag.** The packet uses "almost normal" to mean "the rather-below relation ≺ interpolates" (explicit in §8). That is not a standard frame-theoretic name I can match, and it clashes with Singal–Arya's topological "almost normal". The mathematics is verified relative to the packet's definition; the term should be defined once in the standing definitions. The "almost-normal frame theorem ⟹ 𝒰 = 𝓕" cited in §8 is the usual Urysohn-scale argument from an interpolating ≺ and is plausible, but it is not needed (see G7).

**F2. Relations (L3–L4).** pt 𝒟 = Δ ∪ {(p,x),(x,p)}; pt 𝓘 adds (p,y),(y,p) and not (x,y) (N\_x(∅) ∩ N\_y(∅) = ∅); (x,y) ∈ pt 𝒰 since p ∈ cl N\_x(E₁) ∩ cl N\_y(E₂) always; sheet pairs are excluded by clopen singletons. pt 𝒱 = ⋂{w ⊇ pt 𝓘} = ↑pt 𝓘 (saturation), which contains (x,y) ≥ (p,y). So pt 𝒰 = pt 𝒱 = pt 𝓕 = Δ ∪ {p,x,y}².

*Sublocale equalities without R2:* 𝒰 = 𝓕 (both closed, same points). 𝒱 ⊆ 𝓕 universally; 𝓕 is closed hence spatial, hence the join of its points, all of which lie in 𝒱; so 𝓕 ⊆ 𝒱 (A5). Then 𝒱 ⊆ 𝓗 ⊆ 𝓕 = 𝒱 gives 𝓗 = 𝒱. No spatiality of 𝒱 is needed.

**F3. 𝒲 = 𝓘 (L5), proved without R2.** Let ρ = N\_x(∅) ⊠ N\_y(∅). Since 𝒟 ∧ O(ρ) = ⋂\_{∇w=1} O(w ∧ ρ) and every w ⊇ Δ contains N\_p(E) × N\_p(E) for some finite E = (E₁,E₂), the intersection equals ⋂\_E O(u\_E) with

```latex
u_E=(\{x\}\cup S_1\setminus E_1)\times(S_2\setminus E_2).
```

An open v = Y ∖ G lies in this intersection iff G = cl(G ∩ u\_E) for all E. If (a,b) ∈ G ∩ u\_∅ with b ∈ S₂, take E₂ = {b}: u\_E avoids second coordinate b while X × {b} is open, so (a,b) ∉ cl(G ∩ u\_E). Hence G ∩ u\_∅ = ∅ and G = ∅. So 𝒟 ∧ O(ρ) = 0, 𝒟 ⊆ C(ρ), 𝒲 ⊆ C(ρ), and (x,y) ∉ pt 𝒲; symmetrically for (y,x). With 𝓘 ⊆ 𝒲 and both closed, 𝒲 = 𝓘. Then 𝒟 ⊆ 𝒲 = 𝓘 gives 𝒥 = 𝓘, 𝓜 = 𝒟, and T(𝒥) = 𝒲 ∧ 𝒱 = 𝓘.

**F4. Chain (L6).**

```latex
\Delta\subsetneq\mathcal D=\mathcal M\subsetneq\mathcal I=\mathcal J=\mathcal W=T(\mathcal J)\subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F
```

Strictness is witnessed by (p,x), (p,y), (x,y) respectively. **Correct, assuming only R1.** The universal lower-diamond equality fails for a compact (non-fit, T₀) locale.

## G. Noncompact thickening and 𝒲-boundary transfer — correct conditional on one named lemma

The supplied material is sufficient; the referenced 23 Oct file was not needed.

**G1. Seed poset.** 𝓘(P) = Δ ∪ {(p,q),(q,p)} ∪ ≤ ∪ ≥; ↑(p,q) ∪ ↑(q,p) ∪ ↑Δ = P², so 𝒱(P) = P²; ↓↑x = {p,x} and ↓↑y = {q,y} are disjoint, so (x,y) ∉ 𝓘², and every other pair is in 𝓘². Correct.

**G2. Topology.** The declared opens form a topology (unions: a boundary point of the union lies in some H\_{Aᵢ} and filters are upward closed; finite intersections: finite unions of nowhere dense sets are nowhere dense). Sheet singletons are clopen ({r} is nowhere dense). The subspace topology on the closed set B is Alexandrov. B has finite principal upsets, so it is locally compact and sober (a directed set meets some finite ↑d₀ in a finite directed set whose maximum dominates it). X is sober (irreducible closed sets are clopen sheet singletons or principal downsets of B), scattered, countable, noncompact.

**G3. Filter-meeting lemma.** (⟸, contrapositive) If α ∉ Σ(T), choose an open interval J ∋ α with J ∩ int cl T = ∅; then T ∩ J is nowhere dense (any interval inside cl(T ∩ J) would lie in J ∩ int cl T), and (J ∩ ℚ) ∖ (T ∩ J) ∈ G\_α avoids T. (⟹) If α ∈ Σ(T), every J ∋ α contains an open I on which T is dense; I ∖ cl N ≠ ∅ for nowhere dense N, so the generator meets T. The nowhere-dense deletion step is sound.

**G4. Closure formula and interpolation.** Basic neighborhoods of b ∈ B are ↑b ∪ {s\_r : r ∈ T} with T lying in every filter G(α\_c) for c ∈ ↑b — a finite intersection of filters, so the union of finitely many avoiding members is an admissible trace. Both directions of the closure formula follow. Interpolation: if Σ(T\_A) = ∅ then H\_A = ∅ (for b ∈ H\_A, T\_A ∈ G(α\_b) forces α\_b ∈ Σ(T\_A)), so A ⊆ S is clopen; if Σ(T\_A) ≠ ∅, pick J ⊆ int cl T\_A; fiberwise density of the α\_(s,n), n ≥ N, puts (s,n) ∈ cl A for arbitrarily large n, so any open C ⊇ cl A has H\_C = B and C is clopen. Either endpoint interpolates. So ≺ interpolates in 𝒪(X).

**G5. Spatiality of the square.** Q = O(S ⊠ S) ∨ C(S ⊠ 1) ∨ C(1 ⊠ S), since C(S ⊠ 1) ∨ C(1 ⊠ S) = C(S ⊠ S). O(S ⊠ S) ≅ 𝒪(S) ⊕ 𝒪(S) is discrete; C(S ⊠ 1) = π₁⁻¹\[C(S)\] ≅ 𝒪(B) ⊕ 𝒪(X). **Named lemma:** *the coproduct of a locally compact frame with a spatial frame is spatial* (Isbell; Johnstone, Stone Spaces II.2.13; Picado–Pultr, product notes). With B locally compact and X sober this gives 𝒪(B × X). A join of spatial sublocales is spatial, the point set is X × X, and rectangles generate, so Q = 𝒪(X × X).

**G6. Boundary transfer.** (⟸) For (s,t) ∈ 𝒰(P) with r ≤ u ≥ s, r ≤ v ≥ t: ((u,0),(v,0)) ∈ pt 𝒟 via (r,0), and ((s,n),(t,m)) ≤ ((u,0),(v,0)) in product specialization — the lifts must sit at index 0, not at a large index; pt 𝒲 is a downset. (⟹) If (s,t) ∉ 𝒰(P) then ↑b ∩ ↑c = ∅ (a common upper bound would put (s,t) ∈ 𝓘(P)), so the finitely many attachment irrationals split into two disjoint finite sets; disjoint rational interval unions give an open rectangle U × V ∋ (b,c) with no 𝒟-point. To conclude (b,c) ∉ 𝒲 one needs 𝒟 ∧ O(U ⊠ V) = 0; the packet gets this from R2, but the fixpoint computation of F3 works: for any w ⊇ Δ, w ∩ (U × V) has no boundary–boundary points, and deleting a single rational r from every sheet trace of w (still admissible) shows no fixpoint G meets {s\_r} × X or X × {s\_r}; so G ⊆ B × B and G = cl(G ∩ w ∩ ρ) = ∅.

**G7. The strict chain.** pt 𝒱 ⊇ B² via ((p,N),(q,N)) ∈ 𝓘\_pt for large N and saturation; pt 𝓕 = Δ ∪ B² (B is one comparability component); 𝓕 ⊆ 𝒱 by A5, with no total spatiality needed. pt 𝒰 ⊇ B² directly: for a neighborhood U = ↑(x,0) ∪ {s\_r : r ∈ T\_U} of (x,0), T\_U ∈ G\_{α\_(x,0)} forces Σ(T\_U) ⊇ cl J for some nondegenerate interval J ∋ α\_(x,0), and cl J contains α\_(y,n) for infinitely many n by fiberwise density, so (y,n) ∈ cl U for those n; and (y,n) ∈ cl V for every neighborhood V of (y,0) because (y,n) ≤ (y,0). Hence ((x,0),(y,0)) ∈ pt 𝒰, and likewise all boundary pairs. So pt 𝒰 = pt 𝓕 = Δ ∪ B² and 𝒰 = 𝓕 by point-determination of closed sublocales, without invoking the "almost-normal frame theorem". By G6, ((x,0),(y,0)) ∉ pt 𝒲. Therefore

```latex
T(\mathcal J)=\mathcal W\wedge\mathcal V=\mathcal W\subsetneq\mathcal U\wedge\mathcal V=\mathcal F
```

for a countable, noncompact, noncoherent locale in which ≺ interpolates. **Correct**, conditional only on the lemma in G5.

## H. Surviving theorems, dependency graph, gaps, repairs, next questions

**H1. Surviving theorem list — all audited claims survive.**

1. Universal: Δ ⊆ 𝓘, 𝒟 ⊆ 𝒥 ⊆ 𝒰, 𝒱 ⊆ 𝓕; 𝒲 ⊆ 𝒰; 𝓕 closed and fitted; 𝒲 ∨ 𝒱 ⊆ 𝓗 ⊆ 𝓕; T(𝒥) = 𝒲 ∧ 𝒱; the two absorption identities; both comparable-side criteria; 𝓗 = C(a\_∞) with κ monotone, deflationary, fixed exactly on fitted closed sublocales.
2. Coherent: closed sublocale fitted ⟺ point set is an upset (B2); C1, C2, C3; S\_{α+1} = ↓↑S\_α, S\_λ = ↓cl ⋃S\_β, Sₙ = 𝓘^(2n+1), S\_ω = ↓cl(∼\_c); also (verified en route) 𝒰 = 𝒲, pt 𝒰 = 𝓘\_pt², pt 𝒱 = ↑𝓘\_pt, 𝒱 spatial.
3. Examples: two-ray (𝒰 ∨ 𝒱 = 𝒲 ∨ 𝒱 ⊊ 𝓗 ⊊ 𝓕, 𝓗 not transitive, stabilization at ω); handles (first stabilization exactly ω+m); compact T₁ upper diamond (𝒰 ∨ 𝒱 ⊄ 𝓗, 𝒲 ⊊ 𝒰); compact T₀ lower diamond (T(𝒥) ⊊ 𝒰 ∧ 𝒱); interpolating-≺ noncompact thickening (same strictness, with boundary transfer pt 𝒲 ∩ B² ↔ 𝒰(P)).

**H2. Dependency graph — what each cluster actually needs.**

| Cluster | Needs | Independent of |
| --- | --- | --- |
| A | Frame theory only (coframe law; closure/fit formulas) | — |
| B | A + Priestley/Hochster duality (R3) + patch compactness; R4 re-proved | — |
| C | B | — |
| D | A (frame recursion) + B (point recurrence) | — |
| E | R1 (spatial square) + lemma "T₁ scattered ⟹ fit" (E2) | R2 |
| F | R1 only | R2, any almost-normality result |
| G | Isbell–Johnstone product lemma (G5) + direct computations | R2, the almost-normal ⟹ 𝒰 = 𝓕 theorem |

Accepted from literature: Priestley/Hochster duality and its product compatibility; Priestley separation of disjoint closed up/down-sets; closed equivalences on compact Hausdorff spaces have compact Hausdorff quotients; Urysohn; R1 and its one-sided strengthening (locally compact ⊕ spatial = spatial); regular ⟹ fit; every sublocale is an intersection of sublocales C(a) ∨ O(b); preimage of sublocales is a right adjoint. Verified independently: everything else, including R4's spatiality, B2, the fit lemma, both zero-meet computations, every topological property claimed for the three spaces, and every point-relation enumeration.

**H3. Gaps.** No fatal or repairable gaps in the sense of invalid inferences. Items to fix in the write-up:

1. *Terminology.* Define "almost normal" explicitly as "≺ interpolates" (F1); as written, §7 asserts non-almost-normality under a name a reader may attach to a different property.
2. *Hidden spatiality steps.* In B2/C1 state that "same points ⟹ same sublocale" is applied to two spatial sublocales (closed in a spatial frame; the R4 sublocale). In R5 the inclusion 𝒰 ∨ 𝒱 ⊆ 𝓗 uses 𝒰 = 𝒲 (coherent), which is fine but should be said, since the packet elsewhere warns against relying on it.
3. *Over-reliance on R2.* §§6–8 all route through total spatiality of the scattered square. That theorem (Niefield–Rosenthal; Simmons; BPP Prop. 5.3) appears correctly stated, but the examples do not need it: E2, F2–F3, G6–G7 give elementary replacements. Rewriting on those lines shortens the dependency chain and matches the project's stance of avoiding unexamined point-to-sublocale transfers.
4. *Direction of lifts in G6.* "Lift to suitable points in B" must lift to index 0 (upward in B's order), not to a large index; the current wording is ambiguous.

**H4. Stronger or simpler replacements (distinct from repairs).**

- **Fit locales collapse the lower hierarchy.** If L ⊕ L is fit — in particular whenever L = 𝒪(X) with X × X a T₁ scattered space, by E2 — then 𝒟 = Δ and 𝒱 = 𝒲 = 𝓗 = 𝓘, so the picture reduces to Δ ⊆ 𝓘 ⊆ 𝒰 ⊆ 𝓕. This is the conceptual content of §6 and isolates the separation axiom responsible.
- **Join-of-points criterion (A5).** For closed (hence spatial) S and any T: pt S ⊆ pt T ⟹ S ⊆ T. This disposes of 𝓕 ⊆ 𝒱 in F and G, and of p ∉ 𝒰 ∨ 𝒱 in C, replacing the compact separation argument.
- **Zero-meet fixpoint test.** 𝒟 ∧ O(ρ) = 0 iff no nonempty closed G satisfies G = cl(G ∩ w ∩ ρ) for all w ⊇ Δ; in spaces with clopen singletons this is checkable by deleting one isolated coordinate. It is the right tool for 𝒲-exclusions when total spatiality is unavailable.
- The two-ray example shows 𝒲 ∨ 𝒱 ⊊ 𝓗 even coherently (C), a sharper negative statement than §2 records.

**H5. Suggested next mathematical questions.**

1. *Which ordinals occur as first stabilization?* ω+m is realized; stacking handles whose attachment points are themselves limits (ω²-type configurations) should realize ω·k+m and beyond. Is every countable ordinal realized by a countable Priestley space? Is there a bound in terms of the Cantor–Bendixson rank of the patch space?
2. *C3 beyond coherence.* "𝓗 = 𝓕 ⟹ transitive" is universal (kernel-pair argument). Does "𝓗 transitive ⟹ 𝓗 = 𝓕" survive for spatial squares of noncoherent locales, e.g. the fit case, where it asks whether a transitive 𝓘 forces 𝓘 = 𝓕?
3. *𝒰 versus 𝒲.* E gives a compact T₁ example with 𝒲 ⊊ 𝒰. Is there an intrinsic nucleus-level characterization of 𝒰 as a hull — the least closed sublocale containing Δ that is closed under meeting closures of rectangles, say — making 𝒰 = 𝒲 exactly a coherence-type condition?
4. *Fitness of L ⊕ L.* Is fit preserved by binary coproducts? If so, the collapse in H4 holds for every fit L and the upper diamond is the only diamond that can be nontrivial in fit locales.
5. *Interpolating ≺ and 𝒰 = 𝓕.* G7 verified 𝒰 = 𝓕 directly; the general implication "≺ interpolates ⟹ 𝒰 = 𝓕" (Urysohn scale) should be recorded as a theorem with proof, since G's strictness is interesting precisely because that class is where 𝒰 and 𝓕 agree.

**Summary.** The hierarchy stands as stated and needs no update, only the clarifications in H3. The main independent contribution of this audit is that the three noncoherent examples can be freed from the scattered-sublocale theorem, and that the §6 phenomenon is a theorem about fit locales rather than about scattered ones.