# Referee report — Project A coherent proconstructible composition calculus

Nov 8, 2026 · @Someone · Blind external audit; packet and prompt dated 8 November 2026

## Summary verdict

**Principal claim T is correct, and Application C is correct, including the two delicate sublocale identifications (the presented `A` and the fitted diagonal `D = fit Δ`).** I found no counterexample inside the proconstructible class and no false statement in the packet. What I did find is a small number of places where the written argument stops one step short of the conclusion, most importantly in §5 (identification of `A`, where the text as written comes close to the forbidden "same points, same sublocale" inference, and identification of `D`, where the packet offers two alternative justifications without committing to either). In each case the gap closes with an argument I give in full in Section 3 below; none requires new hypotheses.

The strongest single observation of this audit is an **intrinsic characterization** that the packet does not state but which makes most of §§2–5 shorter: a sublocale `S ↪ Z` of a coherent locale is proconstructible spectral **if and only if the frame quotient `O(Z) → O(S)` preserves compact elements** (equivalently, `S` is coherent and its embedding is a spectral map; equivalently, `O(S) = Idl(K(Z)/θ)` for a lattice congruence `θ`). With this in hand, Lemma C, the identification of `A`, the identification of `D`, and the closure of the class under `cl` and `fit` all become two-line consequences of Stone duality for bounded distributive lattices plus the fact that `Idl : DLat → Frm` is a left adjoint preserving injections and surjections. Section 6 lays this out as a recommended rewrite.

A second structural observation: on the proconstructible class the hull operators act as `cl(R) = A∘R∘B` and `fit(R) = B∘R∘A`. This yields `I = AB`, `D = BA` and `V = fit(I) = BABA = D²` as **theorems inside the packet's own framework**, so `V = D²` need not be imported as an external input (and `U = I²` becomes a theorem too whenever Project A's `U` is `cl(D)`; I could not check that from the packet because `U` is not defined there).

**How the audit was conducted.** Every lemma and every displayed identity was re-derived by hand from the stated definitions; the two literature URLs in §7 of the packet were not reachable from this session, so no numbering of cited results was verified and no step below depends on a cited theorem (Section 4 lists exactly which background facts are used and in what form). Nothing from any prior internal audit or referee comparison was consulted. Classical logic (the prime ideal theorem) is used wherever the packet uses it; Section 6 notes which statements survive constructively.

## 1. Verdict table by claim

Every claim the packet makes is either correct as stated or correct with a gap in the written proof that I close in Section 3. No claim is false and no claim needs an added hypothesis.

| # | Claim (packet §) | Verdict | Status of the written proof | Where closed |
| --- | --- | --- | --- | --- |
| A1 | `Frm(Idl K, L) ≅ DLat(K, UL)`; `Idl` preserves colimits (§1) | Correct | Complete | — |
| A2 | Compact-preserving maps of coherent frames are `Idl(h)` (§1) | Correct | Complete (one line missing: `f` preserves joins and ideals are joins of principal ideals) | §3.1 |
| A3 | `Loc` pullback of coherent locales along spectral maps `= Idl` of the `DLat` pushout, universal in **all** of `Loc` (§1) | Correct | Complete; the universality in all of `Loc` is exactly colimit preservation by a left adjoint | §3.1 |
| A4 | That pullback is the spectral fiber product with the subspace topology (§1) | Correct (classical) | Complete modulo spatiality of coherent locales (prime ideal theorem) | §3.1 |
| B1 | Patch-closed `S` with subspace topology is spectral; `K(Z) → K(S)` is a surjective lattice map (§2) | Correct | Spectrality asserted as standard; a self-contained proof is short | §3.2 |
| B2 | `O(Z) → O(S)` is a frame surjection; `S` has exactly the points of `S` (§2) | Correct | Complete | — |
| B3 | Pullback of a proconstructible inclusion along a spectral map is the proconstructible inclusion of the preimage (§2) | Correct | Complete given A3 | — |
| B4 | Finite sublocale join = union of point sets (§2) | Correct | One step unstated: image of a coproduct map is the join of the images | §3.2 |
| C1 | Localic image of a spectral map is the proconstructible sublocale on the set-theoretic image (§3) | Correct | Complete; relies only on spatiality of the **target** `C`, not of `T` | §3.3 |
| C2 | The argument avoids the "spatial source + closed image" fallacy (§3) | Correct | The reason should be stated explicitly: uniqueness of (surjection, embedding) factorizations | §3.3 |
| T0 | `R ×_Y S = π_12^{-1}R ∧ π_23^{-1}S` as sublocales of `X×Y×Z` (§0, §4) | Correct, in all of `Loc` | Asserted without proof | §3.4 |
| T1 | Binary composite of proconstructible relations is proconstructible on the pointwise composite (§4) | **Correct** | Complete given A–C; the identification of the pullback with `E` is compressed | §3.4 |
| T2 | Associativity, identity, converse, finite distributivity in the class (§4) | **Correct** | Complete | §3.4 |
| P1 | Presented `A = ⋂_u [π_1^*u ≤ π_2^*u]` equals the proconstructible sublocale on the graph of `≤` (§5) | **Correct** | Gap: the text concludes from equality of point sets; the missing link is that `A ↪ X²` is a *spectral* embedding | §3.5 |
| P2 | `[u_1 ≤ u_2] = c(u_1) ∨ o(u_2)` (§5) | Correct | Asserted; verified by a nucleus computation | §3.5 |
| P3 | `I = cl Δ` is proconstructible with `I_pt = {∃z: x ≤ z ≥ y}` (§5) | Correct | Complete | §3.6 |
| P4 | `D = fit Δ` is proconstructible with `D_pt = {∃z: x ≥ z ≤ y}` (§5) | **Correct** | Packet does not commit to a proof; the compact-open-filter congruence argument works and Hofmann–Mislove is not needed | §3.6 |
| P5 | `I = A∘B`, `D = B∘A`, `I∘D = ABA`, `D∘I = BAB`, `I² = ABAB`, `D² = BABA` as sublocale equalities (§5) | **Correct** | Follows from T + P1 + P3 + P4 | §3.7 |
| W1 | `C² = J`, `C³ = ABA ∨ BAB`, `C⁴ = U ∨ V`, `J² = U ∨ V`, general `C^n` (§5) | Correct, conditional on `U = I²`, `V = D²` | Complete; uses only reflexivity, idempotence, finite distributivity, associativity in the class | §3.7 |
| W2 | `V = fit(I) = D²` | Correct **unconditionally** (supplementary) | Not claimed in packet; follows from `fit(R) = BRA` | §3.6, §6 |
| S1 | Non-claims and limitations (§6) | Accurate | The "spectral map" hypothesis is in fact automatic for every map used in T | Section 5 |

## 2. Correctness issues, by severity

None of the issues below is a false statement; all are gaps or compressions in the written argument. I rank them by how much a careful reader must supply to close them. Issues 1–3 are the ones I would insist on for a manuscript; 4–8 are presentational.

**1. (§5, identification of `A`) The final step as written is the inference the prompt warns against.** The packet proves that the presented `A` is `Idl(M')` for a lattice quotient `M'` of `K(X)⊗K(X)`, hence coherent and spatial, and then says that equality of its point set with the order graph "identifies the localic sublocale". That sentence is true only because `A ↪ X²` is a *spectral* embedding (its frame map is `Idl` of a lattice surjection), after which Lemma C, or the intrinsic characterization of Section 6, applies. Without that remark the argument reads as "same points, therefore same sublocale". Fix: one sentence. See §3.5.

**2. (§5, identification of `D = fit Δ`) No proof is actually given.** The packet proposes two routes (Hofmann–Mislove / Jakl–Suárez, or a compact-open-filter congruence computation) and asks the referee to verify. The congruence computation is correct and complete; I give it in §3.6. Two sub-points the packet asks about: (a) `fit Δ` is indeed the intersection of the *compact-open* sublocales `o(k)` with `Δ ⊆ o(k)`, by compactness of `Δ ≅ X`; (b) the delicate step is that the frame congruence generated by the directed union of the open congruences `θ_k` coincides with the frame congruence generated by the lattice congruence `a ≡ b ⇔ ∃f∈Φ, a∧f = b∧f`; both inclusions need an argument (one uses compactness of `a∧k`). Hofmann–Mislove is not needed for any step; the reference to Jakl–Suárez Prop. 6.9 can be dropped.

**3. (§0 and §4) `R ×_Y S = π_12^{-1}(R) ∧ π_23^{-1}(S)` is asserted, not proved.** It is true in all of `Loc` by a direct universal-property argument (§3.4), and the packet needs it because T is stated with the pullback and the proof is run with the triple sublocale `E`. The proof of T also compresses "Lemmas A and B show the actual localic pullback is represented by `E`"; the cleanest justification is that the lattice map `K_X ⊗ K_Y ⊗ K_Z → K_R ⊔_{K_Y} K_S` is surjective (its target is generated by the images of the three factors), so the canonical map `R ×_Y S → X×Y×Z` is a spectral embedding whose point set is `E`.

**4. (§2) Spectrality of a patch-closed subspace is cited as standard.** It is (Hochster; Dickmann–Schwartz–Tressl), but a six-line self-contained proof via Stone duality exists and keeps the packet closed under its own tools (§3.2). The same remark applies to "patch topology of a product is the product of patch topologies", used silently in §4 to see that `E` is patch closed.

**5. (§2, finite joins) One step unstated.** The argument shows `S_1 ⊔ S_2 → S_1 ∪ S_2` is a locale surjection. To conclude that `S_1 ∪ S_2` *is* the sublocale join one also needs: the image of `[f_1, f_2] : S_1 ⊔ S_2 → Z` is `im f_1 ∨ im f_2` (a sublocale contains both images iff both maps factor through it iff the copairing does). One sentence.

**6. (§1, audit task A) The role of the spectral-map hypothesis should be stated once and for all.** The hypothesis is on the two legs of the cospan only; the universal property holds against arbitrary locales and arbitrary (non-spectral) mediating maps. In T every map that appears (projections, the diagonal, the swap, inclusions of proconstructible sublocales, and their composites) is automatically spectral, so T has no spectral-map hypothesis beyond "`X, Y, Z` coherent, `R, S` proconstructible". The packet's §6 could say this.

**7. (§1, §4) Classical logic.** Spatiality of coherent locales, the identification `pt(X×Y) = pt X × pt Y`, and every pointwise formula use the prime ideal theorem. The packet says "classically" once. Section 6 notes that T itself has a point-free formulation that does not.

**8. Minor remarks and asides.**

- §0: "with its compact elements closed under finite meets" should include the top element explicitly (it is compact by compactness of `O(X)`, so nothing is lost, but readers check this).
- §1, proof that `ĥ` preserves finite meets: the displayed computation also needs `ĥ(K) = 1`, i.e. `h(1) = 1`; this is in "bounded" but worth a word.
- §2: "The patch topology on `S` is compact Hausdorff" is used only to get `k ∩ S` quasi-compact; the argument would read more cleanly as "`k ∩ S` is patch-closed in the compact `S_patch`".
- §5: the convention `x ≤ y ⇔ x ∈ cl{y}` makes `A` the graph of specialization in the order where *opens are up-sets*; with it, `I_pt` is the set of pairs with a common *generization* and `D_pt` the set of pairs with a common *specialization*. The packet's phrases "common-upper" and "common-lower" are correct in this convention; a manuscript should say "generization/specialization" to avoid the reader re-deriving the direction.
- §5, `I_pt`: the quoted justification ("compact-open neighborhoods and patch compactness") is fine; the one-line version is the prime filter theorem applied to the filter generated by `F_x ∪ F_y`.
- §5, `D_pt`: the packet's "open-cover criterion" can be replaced by the general fact that the intersection of all open neighbourhoods of a set `F` is its saturation `↑F` (no compactness needed), applied to `F = Δ_set`.
- §6, test 2: "nonclosed specialization fibers" presumably means a point whose generization set `↑x` is not closed; `cl{x}` is always closed.
- §7: I could not reach the two URLs from this session; the statements attributed to DST Cor. 1.3.23 and Finocchiaro et al. Prop. 2.1 are consistent with what I know of those sources but the numbering is unverified here. No step of the audit depends on them.

## 3. Independent verification

Throughout, `K = K(Z)` is the lattice of compact opens of a coherent locale `Z`, `O(Z) = Idl K`, and a *lattice map* is a bounded distributive lattice homomorphism. Points are prime filters of `K`; `x ≤ y` means `F_x ⊆ F_y`, i.e. every open containing `x` contains `y`.

### 3.0 An intrinsic characterization (not in the packet; used below)

**Proposition.** For a sublocale `S ↪ Z` of a coherent locale, with frame quotient `q : O(Z) → O(S)`, the following are equivalent: (i) `S` is proconstructible spectral in the packet's sense; (ii) `q` preserves compact elements; (iii) `q = Idl(h)` for a surjective lattice map `h : K → K'`.

*Proof.* (i)⇒(ii) is Lemma B (traces of compact opens are compact). (ii)⇒(iii): the images `q(k)` are compact, closed under finite meets and joins, and every element of `O(S)` is a join of them; a compact element of `O(S)` is below a finite join of them, hence equals one; so `O(S)` is coherent with `K(O(S)) = q[K]`, and `q = Idl(q|_K)`. (iii)⇒(i): `S = Idl K'` is coherent, hence spatial with spectral point space `Spec K'`; its embedding is a spectral map; by Lemma C (§3.3) the image of that embedding, which is `S` itself, is the proconstructible sublocale on its patch-closed point set. ∎

Consequently the class is in bijection with lattice congruences on `K` (anti-isomorphic to the lattice of patch-closed subsets), and a sublocale with the "right" points lies in the class **iff its frame quotient is `Idl` of a lattice map**. This is the test to apply to `A` and to `D`.

### 3.1 Lemma A

`ĥ(J) = ⋁ h[J]` preserves joins (an element of the ideal generated by `⋃J_α` lies below a finite join of members), finite meets (distributivity, and `i∧j ∈ I∩J`), and top (`h(1)=1`). Uniqueness: a frame map agreeing with `h` on principal ideals is determined, since every ideal is the join of its principal ideals. So `Idl ⊣ U` and `Idl` preserves all colimits of `DLat` in **all of `Frm`**: the universal property of `Idl(K_A ⊔_{K_Z} K_B)` is tested against arbitrary frames, so the dual pullback is a pullback in all of `Loc`. The only hypothesis is that the two legs are `Idl` of lattice maps, i.e. spectral.

If `f : Idl K → Idl K'` preserves compact elements, `h := f|_K` is a lattice map and `f = Idl(h)` because `f` preserves joins. Points of `Idl(K_A ⊔_{K_Z} K_B)` are lattice maps to `2`, i.e. pairs of prime filters agreeing on `K_Z`; basic compact opens are finite joins of `a∧b`, whose point sets are `(D(a)×D(b)) ∩ (\text{fiber product})`, so the induced topology is the subspace topology of the product. Spatiality of the pullback locale is spatiality of coherent locales (prime ideal theorem). The same applies to binary products (`K_X ⊗ K_Y` the `DLat` coproduct) and to meets of proconstructible sublocales, whose inclusions are spectral by §3.0.

**Verified:** every identification in §1. The pullback is a `Loc` pullback; only the legs need to be spectral.

### 3.2 Lemma B

*Spectrality of a patch-closed `S`, self-contained.* Let `K_S := {k ∩ S : k ∈ K}`, a lattice, and `h : K → K_S` the surjective lattice map `k ↦ k∩S`. Points of `Idl K_S` are prime filters of `K` that are saturated for `ker h`. For `p ∈ S`, `F_p` is saturated. For `p ∉ S`: since `S` is patch closed, `Z ∖ S` is a union of constructible sets `c ∖ d` with `c, d ∈ K`; pick one containing `p`. Then `c ∩ S ⊆ d`, so `h(c) = h(c∧d)`, while `c ∈ F_p` and `c∧d ∉ F_p`: `F_p` is not saturated. So `Spec K_S = S` as sets, and the topology generated by `K_S` is the subspace topology. Hence `S` is spectral, `O(S) = Idl K_S`, and `O(Z) → O(S)` is `Idl(h)`, a frame surjection. (The packet's route through quasi-compactness of `k∩S` is equally valid.)

*Pullbacks.* Spectral maps are patch-continuous, so `f^{-1}(S)` is patch closed; by §3.1 the `Loc` pullback is the fiber product `f^{-1}(S)` with subspace topology. Both legs are spectral. ✓

*Finite joins.* `O(S_1 ∪ S_2) → O(S_1) × O(S_2)` is injective (a point separating two opens lies in `S_1` or `S_2`), so `S_1 ⊔ S_2 → S_1∪S_2` is a surjection; and `im[f_1,f_2] = im f_1 ∨ im f_2` because a sublocale `W` contains both images iff both `f_i` factor through `W` iff `[f_1,f_2]` does. Hence `S_1 ∨ S_2 = S_1 ∪ S_2`. ✓ (Arbitrary joins fail: in the Stone space `ω+1`, the join of the point sublocales `{n}` is the open sublocale `o(ℕ)`, not in the class; see Section 5.)

### 3.3 Lemma C and the "spatial source" fallacy

`f : T → Z` spectral; `C := f(T)` is patch closed (patch-continuous image of a compact space in a Hausdorff one). `T → C` is spectral: every compact open of `C` is a trace `k∩C`, with preimage `f^{-1}(k)`. Injectivity of `O(C) → O(T)`: if `U ≠ V` in `O(C)` pick `p ∈ U △ V` (spatiality of `C`), write `p = f(t)`; then `t ∈ f^{-1}U △ f^{-1}V`. So `T → C` is a surjection. The image of `f` is the sublocale whose congruence is `ker f^*`; if `f = m ∘ e` with `e^*` injective and `m^*` surjective then `ker m^* = ker(e^* m^*) = ker f^*`, so `im f = C`. ✓

*Why the fallacy is avoided.* The invalid inference is "`im f` has points `f(pt T)`; the sublocale with those points is `C`; so `im f = C`" — invalid because many sublocales share a point set. The packet instead *constructs* a specific spatial sublocale `C` and *proves* `T → C` is a surjection, then uses uniqueness of (surjection, embedding) factorizations. The only spatiality used is that of the **target** `C`; nothing about `T` beyond its having enough points to cover `C`. Point-surjectivity onto a non-spatial target would prove nothing.

*Point-free form (for Section 6).* With `h : K_Z → K_T` the lattice map and `K_C := h[K_Z]` its image sublattice, `Idl(K_Z) → Idl(K_C) → Idl(K_T)` is (surjection, injection) because `Idl` preserves surjective and injective lattice maps. So `im f = Idl(K_C)` with no points at all; classically `Spec K_C = f(T)` by the prime filter theorem.

### 3.4 Theorem T

*The pullback equals the triple sublocale (in all of `Loc`).* A map `g : W → X×Y×Z` factors through `π_12^{-1}R ∧ π_23^{-1}S` iff `π_12 g` factors through `R` and `π_23 g` through `S`. Given such `g`, `(r, s) := (π_12 g, π_23 g)` satisfies `π_Y r = π_2 g = π_Y s`; given `(r,s)` with `π_Y r = π_Y s`, `g := (π_X r, π_Y r, π_Z s)` recovers them. The bijection is natural, so the meet is the pullback `R ×_Y S`.

*The pullback is the proconstructible sublocale on `E`.* The lattice map `K_X ⊗ K_Y ⊗ K_Z → K_R ⊔_{K_Y} K_S` is surjective (the pushout is generated by the images of `K_R` and `K_S`, which are generated by the images of `K_X⊗K_Y` and `K_Y⊗K_Z`). So `R ×_Y S → X×Y×Z` is a spectral embedding, hence in the class by §3.0, with point set `E = {(x,y,z) : (x,y)∈R, (y,z)∈S}` by §3.1.

*Image.* `E → X×Z` is spectral; Lemma C gives `R∘S =` the proconstructible sublocale on `{(x,z) : ∃y …}`. ✓

*Associativity.* Both bracketings of `R∘S∘T` are, by two applications of the binary result, proconstructible sublocales on the same point set; the class is in bijection with point sets (§3.0), so they are equal. Identity: the localic diagonal is the image of the spectral map `X → X×X`, so by Lemma C it is the proconstructible sublocale on `{(x,x)}` (it is also an embedding since `π_1Δ = id`). Converse: the swap is a spectral isomorphism. Finite distributivity: `R∘(S_1∨S_2) = R∘(S_1∪S_2)` by §3.2, and pointwise composition distributes over union. ✓

*Counterexample search.* Within the class none can exist: the composite is a function of point sets. I checked the boundary cases the packet lists (finite Alexandrov posets; `ω+1` with a non-compact open; the generic point of a non-trivial spectrum, where `↑x` is patch closed but not closed) and each behaves as predicted: the calculus is exact on patch-closed sets and the only failures are for sublocales outside the class (Section 5).

### 3.5 The specialization sublocale `A`

*`[a ≤ b] = c(a) ∨ o(b)`.* The nucleus of `c(a)∨o(b)` is `ν(x) = (a∨x) ∧ (b→x)`; one checks `νν = ν`, that `ν(a) = a∧(b→a) ≤ a∨b = ν(b)`, and that any nucleus `ν'` with `ν'(a) ≤ ν'(b)` fixes every `ν`-fixed element (using `ν'(b→x) = b→x` for `x` fixed, and `ν'(ν'(a)∨x) ≤ ν'(b∨x)`). So it is the largest sublocale on which `a ≤ b`, i.e. the quotient by the congruence generated by `(a, a∧b)`. ✓

*Reduction to compact generators.* `π_1^*u ≤ π_2^*u` for all `u` follows from the same for compact `k`, since `u = ⋁ k_i`. So `A` is the quotient of `Idl(K⊗K)` by the frame congruence generated by the pairs `(k⊗1, k⊗1 ∧ 1⊗k)`. Let `M'` be the lattice quotient of `K⊗K` by the same pairs. By the adjunction, `Frm(Idl M', L) ≅ {h ∈ DLat(K⊗K, L) : h(k⊗1) ≤ h(1⊗k)} ≅ {f ∈ Frm(Idl(K⊗K), L) : f(k⊗1) ≤ f(1⊗k)}`, so `O(A) ≅ Idl M'` and `O(X²) → O(A)` is `Idl` of the surjection `K⊗K → M'`. **This is the step the packet omits: it shows the embedding is spectral.** By §3.0, `A` is the proconstructible sublocale on its point set, which is `{(F,G) : F ⊆ G} =` the graph of `≤`. ✓ Patch-closedness of that graph as stated in the packet is correct.

### 3.6 The hulls `I = cl Δ` and `D = fit Δ`

*Closed sublocales are in the class.* For `c(a) = ↑a`, the quotient `u ↦ u∨a` sends compact `k` to `k∨a`, which is compact in `↑a` (directed joins in `↑a` are computed in `O(Z)`). By §3.0, `c(a)` is proconstructible, on the closed set `Z∖a`. For `I`: since `X²` is spatial and `Δ` is spatial, the largest open missing `Δ` is the complement of the topological closure of `Δ_set`, so `I` is the proconstructible sublocale on `cl(Δ_set) = {(x,y) : ∃z, x≤z≥y}` (the prime filter theorem applied to the filter generated by `F_x ∪ F_y`, proper because compact-open neighbourhoods of `x` and `y` meet). ✓

*Fitted hulls of compact sublocales are in the class.* Let `S` be any **compact** sublocale of `Z` and `Φ_S := {k ∈ K : S ⊆ o(k)}`. (1) `Φ_S` is a filter: `o(k)∧o(k') = o(k∧k')`. (2) `fit S = ⋂_{k∈Φ_S} o(k)`: if `S ⊆ o(W)`, write `W = ⋁ k_i`; the image of `W` in `O(S)` is top, `S` is compact, so a finite subjoin `k ≤ W` already has `S ⊆ o(k)`. (3) Let `≡` be the lattice congruence `a ≡ b ⇔ ∃f∈Φ_S, a∧f = b∧f`, let `Θ'` be the frame congruence generated by `≡` (so `Idl K/Θ' = Idl(K/≡)` by the adjunction argument of §3.5), and let `Θ := ⋁_k θ_k` be the frame congruence of `⋂ o(k)`, where `u θ_k v ⇔ u∧k = v∧k`. **Claim: `Θ = Θ'`.** `Θ' ⊆ Θ`: each generator `(a,b)` of `Θ'` lies in `θ_f ⊆ Θ`. `Θ ⊆ Θ'`: fix `k ∈ Φ_S` and `u θ_k v`. For compact `a ≤ u`: `a∧k ≤ v∧k = ⋁↑{b∧k : b ≤ v \text{ compact}}`, and `a∧k` is compact, so `a∧k ≤ b∧k` for some compact `b ≤ v`; then `a∧k = (a∧b)∧k`, so `(a, a∧b) ∈ Θ'`. Joining over all compact `a ≤ u` gives `u Θ' w` for some `w ≤ u∧v`, hence `u Θ' u∧v` by convexity of congruence classes; symmetrically `v Θ' u∧v`. So `θ_k ⊆ Θ'` for every `k`, and `Θ ⊆ Θ'`. ∎

Therefore `fit S = Idl(K/≡)`, whose quotient map preserves compact elements: by §3.0 **`fit S` is proconstructible spectral**, and its points are the prime filters containing `Φ_S`, i.e. `⋂ Φ_S`. In particular `fit S` is compact (coherent), which answers the packet's question about compact fittedness without Hofmann–Mislove.

*Applied to `D`.* `Δ ≅ X` is compact. `⋂ Φ_Δ = ⋂{\text{opens} ⊇ Δ_set} = ↑Δ_set = {(x,y) : ∃z, z≤x, z≤y}` (the intersection of all open neighbourhoods of any set `F` is its saturation `↑F`: for `p ∉ ↑F` choose for each `f ∈ F` an open containing `f` but not `p`, and take the union). So `D` is the proconstructible sublocale on `D_pt = (BA)_pt`. ✓

*The same computation for `V = fit I`.* `I` is compact (closed in a compact locale), so `V` is in the class with points `↑I_pt = {(x,y) : ∃x'≤x, y'≤y, x'≤z≥y'} = (BABA)_pt = (D²)_pt`. Hence **`V = D²` holds as a sublocale equality with no external input.**

### 3.7 The word identities

In the class, `⊆` of sublocales is `⊆` of point sets, composition is monotone, `Δ ⊆ A, B` (reflexivity), `A² = A`, `B² = B` (transitivity). With `I = AB`, `D = BA` from §3.5–3.6 and T: `I∘D = ABBA = ABA`, `D∘I = BAB`, `I² = ABAB`, `D² = BABA`. For `C = A∨B`, finite distributivity gives `C² = A ∨ AB ∨ BA ∨ B = AB ∨ BA = J` (since `A ⊆ AB` via `z = y`, `B ⊆ AB` via `z = x`). Inductively any word of length `m` is contained in an alternating word of length `m+1` extending it (`w ⊆ w∘A`, `w ⊆ w∘B`), and any word reduces by idempotence to an alternating word; so `C^n` is the join of the two alternating words of length `n`: `C³ = ABA ∨ BAB`, `C⁴ = ABAB ∨ BABA`, `C^{2n} = (AB)^n ∨ (BA)^n`. `J² = C⁴ = I² ∨ D²`, which equals `U ∨ V` given `U = I²` (external input) and `V = D²` (now a theorem). ✓ No unrestricted associativity is used; every factor is in the class.

## 4. Background vs. verified vs. supplementary

No conclusion above rests on a cited theorem that I could not re-derive; the published facts used are listed so that a manuscript can cite them or prove them inline.

| Category | Statement | Role |
| --- | --- | --- |
| Published background (standard, used as stated) | Stone duality `DLat^op ≃ Spec`; prime filter theorem; coherent locales are spatial (classically) | Spatiality in Lemmas A–C and all pointwise formulas |
| Published background | Spectral maps are patch-continuous; patch topology is compact Hausdorff; constructible sets are finite unions of `c ∖ d` with `c, d` compact open | Lemma B (self-contained proof in §3.2 uses only the last fact), Lemma C |
| Published background | Patch topology of a finite product of spectral spaces is the product of patch topologies | Patch-closedness of `E` in §4 |
| Published background (standard, re-proved here) | Patch-closed subsets with the subspace topology are spectral; `Idl ⊣ U`; `c(a)∨o(b)` is the largest sublocale on which `a ≤ b`; the image of a locale map is the sublocale with congruence `ker f^*` | §3.1, §3.2, §3.3, §3.5 |
| Verified directly from the packet | Lemmas A, B, C; Theorem T (binary formula, associativity, identity, converse, finite distributivity); patch-closedness of the graph of `≤`; `I_pt`, `D_pt`; `I = cl Δ` proconstructible; all displayed word identities | Sections 1–3 |
| Verified with an argument the packet omits | `R ×_Y S = π_12^{-1}R ∧ π_23^{-1}S` in all of `Loc`; the pullback is the sublocale on `E`; the embedding `A ↪ X²` is spectral; `fit Δ = Idl(K/≡)` (the `Θ = Θ'` claim) | §3.4, §3.5, §3.6 |
| Supplementary deductions (new, not needed for T or C but recommended) | Intrinsic characterization §3.0; `fit S` proconstructible for every compact sublocale `S`; `cl(R) = ARB`, `fit(R) = BRA` on the class; `V = fit I = D²` unconditionally; the class is closed under arbitrary meets and finite joins and is anti-isomorphic to `Con(K)`; point-free form of T | §3.0, §3.6, Section 6 |
| Not verified | Numbering of DST Cor. 1.3.23, Finocchiaro et al. Prop. 2.1, Jakl–Suárez Prop. 6.9 (URLs unreachable from this session); the external inputs `U = I²` and the definition of `U` | None of the verdicts depend on these |

## 5. Exact scope for use elsewhere in Project A

**Safe to use without further proof.** For coherent locales `X, Y, Z` and sublocales whose frame quotients preserve compact elements (equivalently: proconstructible spectral sublocales; this includes every closed sublocale, every compact-open sublocale `o(k)`, the diagonal, `A`, `B`, `I`, `D`, `V = fit I`, and `fit S` for every compact sublocale `S`):

1. `R ∘ S` (image of the `Loc` pullback) is in the class and has the pointwise composite as point set.
2. Composition is associative, `Δ` is a two-sided identity, converse reverses composites, and composition distributes over **finite** joins; order of sublocales is inclusion of point sets.
3. `I = AB`, `D = BA`, `V = BABA = D²`, `I∘D = ABA`, `D∘I = BAB`, `I² = ABAB`, `C^n` = join of the two alternating words of length `n`, `J² = I² ∨ D²`.
4. `cl(R) = ARB` and `fit(R) = BRA` for `R` in the class (Section 6); so iterated alternating hulls of `Δ` are alternating words.
5. Arbitrary meets of class members are class members (point intersection); finite joins are class members (point union).

**Conditional.** `U = ABAB` and `J² = U ∨ V` hold exactly when Project A's `U` equals `I²` as a sublocale (an input this packet does not prove). If `U` is defined as `cl(D)`, item 4 proves `U = A(BA)B = ABAB = I²` outright.

**What breaks when a hypothesis is dropped.**

| Hypothesis dropped | What fails | Witness |
| --- | --- | --- |
| Patch-closedness of a relation (keeping `X` coherent) | The relation may leave the class, its image under projection may fail to be spatial-by-points, and infinite joins already fail inside the class | In the Stone space `ω+1`: `o(ℕ)` is an open sublocale, spatial, not patch closed; the sublocale join of the points `{n}` is `o(ℕ)`, while the patch-closed union would be the whole space. `fit S` for non-compact `S` (e.g. `S = o(ℕ)`) is not in the class |
| Coherence of `X` (keeping relations closed) | Products of spatial locales need not be spatial; images of closed relations under projection need not be closed or point-determined; `A`, `B` collapse to `Δ` on points while `I` can be non-trivial | The packet's test 4 (compact `T_1` non-Hausdorff, e.g. cofinite topology: `Δ` is dense, `I = X×X`, `AB = Δ` on points) |
| Compactness of `O(X)` only (algebraic, compact elements closed under meets, but `1` not compact) | Patch space not compact; images of patch-closed sets under spectral maps not patch closed; Lemma C fails | Take `X = ℕ` discrete (compact opens = finite sets, no compact top) and `Y = ω+1` the Stone space. The closed, patch-closed relation `{(n,n)} ⊆ X×Y` has localic image `o(ℕ) ⊆ Y` under the projection: spatial, but neither closed nor patch closed, so the class of closed relations is not preserved by composition. |
| Spectrality of a map one pulls back along | Lemma A: the `Loc` pullback need not be coherent or spatial | Not an issue for T, where every map is automatically spectral; relevant only if one composes with relations given by non-spectral embeddings |
| Finite joins replaced by arbitrary joins | Distributivity and membership fail | The `ω+1` example above |
| Classical logic | Pointwise formulas and "spatial" vanish; the lattice-congruence formulation of T survives | Section 6 |

**Two cautions for other Project A branches.** (a) The equality `I = AB` is an equality of *sublocales* only because both sides are in the class; the same point identity on a non-coherent locale is not evidence of a sublocale identity. (b) Transfinite hull iterations stay in the class at successor stages (by items 1–5) but a limit stage is an infinite join, which must be shown patch closed separately before the calculus applies again; the `ω+1` example shows this is a real obstruction, not a formality.

## 6. Recommendations for a manuscript-ready presentation

The packet proves T by going through points three times (Lemmas A, B, C each pass from a lattice statement to a point statement and back). A manuscript can prove T once, point-free, and use points only to *compute*. The six recommendations below are ordered by how much they shorten the text.

**6.1 Lead with the intrinsic characterization and rename the class.** State §3.0 as the definition: a *coherent sublocale* (or *spectral sublocale*) of a coherent locale `Z` is one whose frame quotient `O(Z) → O(S)` preserves compact elements; equivalently `O(S) = Idl(K/θ)` for a lattice congruence `θ`. Then record as a proposition that these are exactly the sublocales induced by patch-closed subspaces. This removes the need for the disclaimer "not intended to include arbitrary sublocales with the same points": membership is now a property of the frame quotient, and the point description is a theorem. It also gives, for free, the complete lattice structure: coherent sublocales of `Z` form a lattice anti-isomorphic to `Con(K)`, closed under arbitrary meets in `Sl(Z)` and under finite joins.

**6.2 Prove T point-free, then compute with points.** The proof reduces to three sentences once the following are on record: (a) `Idl : DLat → Frm` is a left adjoint, so `Coh → Loc` (coherent locales with spectral maps) preserves all limits, in particular pullbacks and finite products; (b) `Idl` preserves injective and surjective lattice maps, so `Coh → Loc` preserves surjections and embeddings, hence image factorizations (`im f = Idl` of the image sublattice); (c) `DLat^op` is a regular category (amalgamation property of distributive lattices = pullback-stability of surjections), so relations in `Coh` compose associatively by the general theory of relations in regular categories. Then T reads: *the relational calculus of `Coh` is preserved by the embedding into `Loc`*. This is the conceptual content of the "repair": `Loc` is not regular, but it contains a regular subcategory whose images it respects. Points enter only in the corollary "and in `Coh` composition is pointwise", which is Stone duality plus the prime filter theorem. A side benefit: (a) and (b) are constructively valid and (c) is expected to be (see 7.2), so T would hold in any topos with the class defined via lattice congruences; only the pointwise formulas need classical logic.

**6.3 Treat the hull operators uniformly.** Prove once that for `R` in the class, `cl(R)` is in the class (closed sublocales of coherent locales are coherent, §3.6) and `fit(R)` is in the class (every member is compact, and `fit` of a compact sublocale is coherent, §3.6), with point sets `↓R` and `↑R` respectively (closure of a proconstructible set is its specialization-closure, by patch compactness; intersection of open neighbourhoods of any set is its saturation). Since `↓R = ARB` and `↑R = BRA` pointwise, one gets

```latex
\mathrm{cl}(R) = A \circ R \circ B, \qquad \mathrm{fit}(R) = B \circ R \circ A
```

for every `R` in the class. Then `I = cl Δ = AB`, `D = fit Δ = BA`, `V = fit I = BABA = D²` are one-line corollaries, the alternating-word structure of iterated hulls is explained rather than observed, and idempotence `cl² = cl`, `fit² = fit` is a consistency check (`AARBB = ARB`). If Project A's `U` is `cl(D)`, then `U = ABAB = I²` joins this list and the "external inputs" disappear.

**6.4 State the `fit` result at its natural generality.** The argument in §3.6 shows: *for any compact sublocale `S` of a coherent locale, `fit S` is coherent, with `K(fit S) = K/≡_{Φ_S}`.* This covers `Δ`, `I`, and any future compact relation, and it does not require `S` to be spatial. Hofmann–Mislove and Jakl–Suárez become remarks ("in particular `fit S` is compact fitted, consistent with HM") rather than steps. I recommend removing the Jakl–Suárez pointer unless the manuscript wants to connect to canonical extensions.

**6.5 Add the two one-line lemmas the packet uses silently.** (i) `R ×_Y S = π_12^{-1}R ∧ π_23^{-1}S` in any category with finite limits (§3.4). (ii) The image of a copairing `[f_1, f_2]` is the join of the images (§3.2). Both are standard but their absence is what makes §4 and the finite-join paragraph of §2 feel compressed.

**6.6 Make the "known dangers" paragraph a lemma with a counterexample.** The manuscript should exhibit one locale where image composition is not associative or where a point-surjection onto a non-spatial target is not a surjection, so the reader sees what the coherent hypothesis buys. The packet asserts non-associativity in `Loc` without a witness; the `ω+1` / non-compact examples of Section 5 illustrate the failure of the class to be closed under infinite joins and under `fit` of non-compact sublocales, but a genuine non-associativity witness in `Loc` would make the "why this question arose" section self-contained. (This referee did not construct one; it is a known phenomenon in the literature on localic relations and should be cited or reproduced.)

**Smaller editorial points.** Replace "common-upper/common-lower" by "common generization/common specialization" and fix the specialization convention in one display; write `K(X)` consistently for compact opens and `Idl` for the ideal frame; in §1 write the pushout as `K_A ⊔_{K_Z} K_B` once and then use it; in §6 add the sentence that all maps in T are automatically spectral; move the bibliographic pointers to where they are used, and verify the result numbers (I could not).

## 7. Extensions and generalizations

These go beyond the audit brief; each is marked by how much of it this referee has checked.

**7.1 Stably compact locales and perfect maps (plausible; not verified).** Everything in T used about coherent locales is: a duality with a category of "spaces" whose patch topology is compact Hausdorff, in which images of the relevant maps are patch closed, and whose inclusion into `Loc` preserves finite limits and image factorizations. Stably compact locales with perfect (proper) maps are the natural wider setting: by Nachbin duality they are compact ordered spaces, patch-closed relations are closed subsets of a compact Hausdorff product, and closed-relation composition is associative there for elementary reasons. The two steps to check are (i) that finite limits of stably compact locales along perfect maps, computed in `Loc`, are stably compact with the expected points (I believe this is in Johnstone's *Stone Spaces* VII or in Escardó's work on stably compact locales, but did not verify), and (ii) a Lemma C analogue: the localic image of a perfect map between stably compact locales is the sublocale induced by its patch-closed set image. If both hold, `A`, `B`, `I`, `D` and the word identities hold verbatim for stably compact `X`, which would cover every compact Hausdorff and every spectral case at once.

**7.2 Constructive version (checked at the level of statements).** With the class defined as `Idl` of lattice congruences (6.1) and T proved as in 6.2, the whole calculus is a statement about `DLat`: a relation `R ↪ X×Y` is a lattice congruence on `K_X ⊗ K_Y`, the composite is the congruence obtained by pushing out along `K_Y` and restricting to the sublattice generated by `K_X` and `K_Z`. Associativity is then regularity of `DLat^op` (pushout-stability of injective lattice maps). I verified this classically via Stone duality; I expect a constructive proof through the normal form for lattice coproducts but did not carry it out, so the constructive claim is conditional on that one lemma. The pointwise descriptions become classical corollaries. This would let Project A state its coherent results in any topos, which may matter if the Scott-continuity branch uses internal locales.

**7.3 A relational structure, not just an associative composition (checked).** The class of coherent relations between coherent locales, with localic composition, converse, finite joins and arbitrary meets, is isomorphic (via points, classically; via congruences, constructively) to the allegory of patch-closed relations between spectral spaces. In particular it is a *distributive allegory* in Freyd–Scedrov's sense (modular law included), so any identity valid in all allegories is available to Project A for free, e.g. `R ∩ S∘T ⊆ (R∘Tˇ ∩ S)∘T`. This is a cheap way to generate and certify further mixed-word inequalities.

**7.4 Hull calculus as a monoid action (checked for cl and fit).** By 6.3 the hull operators act on the class by two-sided multiplication: `cl = A(−)B`, `fit = B(−)A`. Any composite of hulls applied to `Δ` is therefore a single alternating word, and two composites agree iff the words agree after cancellation by `A² = A`, `B² = B`. This gives a decision procedure for all "hull-word" identities on coherent locales, and it predicts exactly which ones fail to collapse (e.g. `fit cl Δ = BABA` and `cl fit Δ = ABAB` are generally distinct and incomparable). It also makes the growth of iterated hulls transparent: the length-`n` alternating words are strictly increasing in general, which is presumably the Project A phenomenon that the separation theorems measure.

**7.5 Transfinite iterations (partially checked).** Successor stages of any hull iteration stay in the class by Sections 3 and 6; limit stages are infinite joins and may leave it (the `ω+1` example). A positive result is available when the limit union of patch-closed relations is *closed in the patch topology*: this holds, for example, when the iteration is eventually constant, or when the relations form a chain whose union is a finite union, or when the ambient spectral space is finite (patch topology discrete). Note that Noetherian is not enough: the patch topology of Spec ℤ is the one-point compactification of the discrete primes, so an infinite set of closed points is not patch closed. This referee has no general sufficient condition to offer beyond these; the limit-stage obstruction is real and should be stated as an open hypothesis in Project A's hull iterations.

**7.6 A worked check for the manuscript.** A small non-Alexandrov test case that exercises the patch-closed-but-not-closed phenomenon: `X = Spec ℤ` (coherent; points = primes and the generic point `(0)`). `A` = pairs `(x, (0))` and `(x,x)`; `I = AB` = all pairs (every two points have the common generization `(0)`), so `cl Δ = X×X`; `D = BA` = `Δ ∪ {((0),p), (p,(0))}`, which is patch closed, not closed, and not open; `V = BABA = X×X`. This verifies the formulas against intuition about `Spec ℤ` and shows `D` as a genuinely proconstructible, non-closed relation.