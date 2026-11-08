# Referee report — Project A: Scott-continuity converse for closed relations

**External blind review 1 of 2 · 8 November 2026**
**Documents examined:** the referee prompt and the technical packet `ProjectA_Scott_converse_EXTERNAL_BLIND_packet_2026-11-08.md` only, plus published background literature chosen by the referee (listed in §9). No Project A internal material was consulted.

---

## 0. Summary of verdicts

| Claim | Verdict | Comment |
|---|---|---|
| **Theorem T** (topological, T1 ⟺ T2) | **Valid as stated.** | Proof is correct in every step I checked. In addition, the hypothesis *weakly locally compact* is **superfluous** for T1 ⟺ T2: the equivalence holds for **arbitrary** spaces `X`, `Y` and closed `E ⊆ X×Y` (proof in §6.1). |
| **T3 equivalence** (§2.3 of packet) | **Valid as stated**, under weak local compactness. | This is the *only* place where weak local compactness is genuinely needed; without it T3 is strictly stronger than T1/T2 (counterexample in §6.2). |
| **Theorem L** (localic) | **Valid as stated**, under classical logic + choice, with the background facts B1–B3, which I confirmed to be correct and correctly scoped. | Forward direction is the packet's argument; I re-verified the Frobenius computation (3.1). Reverse direction is immediate. |
| §4 corollary (supplementary) | Not refereed in depth; **one point should be pinned down** (exact hypotheses of the effectiveness/quotient theorems invoked), see §5. | Outside primary scope by the packet's own instruction. |

**No fatal issues were found.** All items in §4 below are editorial/clarificatory. The packet is self-contained enough to referee.

The hardest steps I checked independently were: (i) the tube-lemma closedness of `K_F × W_F → W_F` without any separation axiom and with `K_F` not closed; (ii) the inclusion (2.1) and the equality `p_Y(H) ∩ W_F = π_Y(H ∩ (K_F × W_F))`; (iii) the Frobenius identity (3.1), including the set identity `f(A ∩ f^{-1}B) = f(A) ∩ B`; (iv) the exact scope of B2 (localic vs. topological product) and B3 (closed sublocale ↔ closed subspace, including `↑a ≅ O(Z∖a)`).

---

## 1. Conventions — one ambiguity to fix

**Directed means non-empty.** The packet says "preserves every directed join". For both T and L this must mean *non-empty* directed joins (the usual convention), and the packet should say so explicitly, because the statements are **false** if the empty family is admitted:

> If `p_Y` is not onto, `(p_Y)_*(∅) = Y ∖ p_Y(E) ≠ ∅`, while the empty join is `∅`. E.g. `E = ∅`, `Y ≠ ∅`: `p_Y` is trivially closed with (empty, hence compact) fibres, so T2 holds, but `r_E(∅) = Y ≠ ∅`.

Since §5(3) of the packet explicitly wants to allow non-surjective `p_Y`, this is a necessary clarification, not a pedantic one. Vermeulen's definition of proper also uses non-empty directed joins, so L is unaffected once the convention is stated. **Severity: editorial, but must be stated.**

Everything else in §1 of the packet (definitions of `f_*`, weak local compactness, closed with compact fibres, proper) is unambiguous and matches the literature. The formula `r_E(U) = int_Y(Y ∖ E[X∖U])` is correct: `W ⊆ r_E(U)` iff `E ∩ (X×W) ⊆ U×Y` iff `W ∩ E[X∖U] = ∅`.

---

## 2. Theorem T — step-by-step audit

### 2.1 T1 ⇒ T2 (packet §2.1)

* **Cover and directed family.** Correct. `(U_F)_{F finite}` is non-empty (take `F = ∅`), directed, with union `X`; `r_E(X) = (p_Y)_*(E) = Y` because right adjoints preserve top. Scott continuity then gives `Y = ⋃_F r_E(U_F)`. ✔
  *Minor:* choosing one pair `(V_x, K_x)` per point uses the axiom of choice. This is avoidable: index the family by *all* pairs `(V,K)` with `V` open, `K` compact, `V ⊆ K`; finite unions of the `V`'s still form a directed cover. T is then choice-free (classical logic only). Worth a footnote since the prompt asks about choice principles.

* **Uniform compact support (2.1).** Correct. `W_F ⊆ (p_Y)_*(p_X^{-1}U_F)` means `p_Y^{-1}(W_F) ⊆ p_X^{-1}(U_F)`, i.e. `E ∩ (X×W_F) ⊆ (U_F × Y) ∩ (X × W_F) = U_F × W_F ⊆ K_F × W_F`. ✔

* **Closed projection.** Correct.
  - `H` closed in `E`, `E` closed in `X×Y` ⇒ `H` closed in `X×Y`. ✔
  - `p_Y(H) ∩ W_F = π_Y(H ∩ (K_F × W_F))`: if `y ∈ W_F` and `(x,y) ∈ H ⊆ E` then by (2.1) `x ∈ K_F`. ✔
  - `H ∩ (K_F × W_F)` is closed in the subspace `K_F × W_F`, whose topology is the product of the subspace topologies. ✔
  - **Tube lemma without separation:** for `K` compact (finite-subcover sense, no `T_0`/Hausdorff) and any `W`, `π: K×W → W` is closed. Proof: if `y ∉ π(C)` with `C` closed, cover `K×{y}` by boxes `A_k × B_k` missing `C`, take a finite subcover, intersect the `B_k`. No point of this uses that `K` is closed in `X`, Hausdorff, or anything else. ✔ (This is the easy half of Kuratowski's characterisation of compactness.)
  - Local-to-global: `A ⊆ Y` is closed iff `A ∩ W` is closed in `W` for every member `W` of an open cover. ✔

* **Compact fibres.** Correct. `E_y` is closed in `X` (preimage of `E` under `x ↦ (x,y)`), lies in `K_F`, hence is closed in the compact space `K_F`, hence compact. Closed subsets of compact spaces are compact without separation axioms. ✔ `K_F` need not be closed in `X`; nothing in the argument requires it.

**Conclusion:** T1 ⇒ T2 is correct as written, and uses *only* weak local compactness; no Hausdorffness or closedness of compacta is used tacitly.

### 2.2 T2 ⇒ T1 (packet §2.2)

* (2.2) `f_*(V) = Y ∖ f(Z∖V)` for closed `f`: the right-hand side is open (closedness), `f^{-1}` of it lies in `V`, and any open `W` with `f^{-1}W ⊆ V` misses `f(Z∖V)`. ✔ (In general, `f_*(V) = int(Y ∖ f(Z∖V))`; closedness removes the interior.)
* Directed-join step: `y ∈ f_*(⋃V_j)` ⇒ `f^{-1}(y) ⊆ ⋃V_j` ⇒ (compactness + directedness) `f^{-1}(y) ⊆ V_j` for one `j` ⇒ `y ∉ f(Z∖V_j)` ⇒ `y ∈ f_*(V_j)`. ✔
  - **Empty fibres:** if `f^{-1}(y) = ∅`, any `j` works, which requires `J ≠ ∅` — this is exactly where the "directed = non-empty" convention of §1 is needed. With it, non-surjective `p_Y` and arbitrary non-Hausdorff `X, Y` are handled correctly.
* `r_E = (p_Y)_* ∘ p_X^*`: `p_X^*` preserves all joins and is monotone, so it sends directed families to directed families; the composite preserves directed joins. ✔ Note that this direction uses **neither** closedness of `E` **nor** local compactness of `X`.

### 2.3 Condition T3 (packet §2.3)

* T1 ⇒ T3: the proof of §2.1 produces `(W_F, K_F)`. ✔
* T3 ⇒ T2: identical tube-lemma argument with the cover by the `W`'s; closedness of `E` is used (for `H` closed in `X×Y` and for `E_y` closed), closedness of `K` is not. ✔
* T2 ⇒ T1 ⇒ T3 closes the cycle. ✔

So **T1 ⟺ T2 ⟺ T3 under the packet's hypotheses is correct.** But see §6.2: T3 is the one condition that really *needs* weak local compactness; T1 ⟺ T2 does not.

### 2.4 Role of the hypothesis "E closed"

Needed for T1 ⇒ T2 and cannot be dropped: take `X = {∗}`, `E = {∗} × A` for a non-closed `A ⊆ Y`. `O(X)` has two elements, so `r_E` is trivially Scott-continuous, but `p_Y(E) = A` is not closed. (Suggested as an added sanity check for packet §5.)

---

## 3. Theorem L — audit

### 3.1 Background B1–B3

* **B1 (Hofmann–Lawson).** Correct: continuous frames are exactly the frames `O(X)` with `X` locally compact sober; the point space `pt(L)` is locally compact sober with `O(pt L) ≅ L`. "Locally compact" here is the strong sense (neighbourhood base of compact sets), which implies the packet's weak sense. **Choice:** spatiality of continuous frames is a classical theorem — the proof (Hofmann–Mislove / Hofmann–Lawson; Johnstone *Stone Spaces* VII.4; Picado–Pultr VII.6) uses a choice principle and the theorem fails constructively. The packet's "classical logic and choice" is therefore accurate; one could sharpen it to "the axiom of choice in the form used for the Hofmann–Mislove theorem", but this is optional.

* **B2 (localic = topological product).** Correct, and in fact stronger than stated: by Isbell (*Product spaces in locales*, PAMS 81 (1981)) the embedding of sober spaces into locales preserves `X × Y` whenever `X` is core-compact (= `O(X)` continuous), for **any** space `Y`. The packet only needs the case `Y = X_pt`. Note that the statement genuinely needs a hypothesis: for two spatial locales the localic product need not be spatial (Isbell's example of two disjoint dense subsets of a `T_2` space; e.g. `ℚ ×_loc (ℝ∖ℚ)`, and also `ℚ ×_loc ℚ`, differ from the topological products).

* **B3 (closed sublocale ↔ closed subspace).** Correct. For a space `Z` and open `a`, the closed sublocale `c(a)` has frame `↑a`, and `U ↦ U ∩ (Z∖a)` is a frame isomorphism `↑a → O(Z∖a)` (inverse: `V ↦ V ∪ a` for `V` relatively open). Hence closed sublocales of spatial locales are spatial and correspond to closed subspaces; the projections `E → X` are the restricted frame maps, so their right adjoints are literally the same maps. ✔

### 3.2 Forward direction (packet §3.1)

* Transfer to spaces via B1–B3, then Theorem T (with `X = Y = X_pt`, both weakly locally compact; T only needs it for `X`). ✔
* Scott continuity of `(p_2)_*` on **all** of `O(E)` via (2.2). ✔
* **Frobenius (3.1):** I re-derived it. For closed `f`: `f_*(V ∪ f^{-1}W) = Y ∖ f((Z∖V) ∩ f^{-1}(Y∖W)) = Y ∖ (f(Z∖V) ∩ (Y∖W)) = (Y∖f(Z∖V)) ∪ W = f_*(V) ∪ W`. The identity `f(A ∩ f^{-1}B) = f(A) ∩ B` holds for every function, with no surjectivity. ✔
* The packet's definition of *proper* (Scott-continuous `f_*` + closed Frobenius) agrees with Vermeulen 1994 (and with Johnstone's *Elephant* C3.2); the Frobenius law is exactly the statement that `f` is a closed locale map. The packet's terminology warning (semi-proper/lax proper/perfect ≠ proper) is appropriate.

### 3.3 Reverse direction and symmetry (packet §3.2)

* Reverse: immediate from the definition and the fact that `p_1^*` preserves all joins; indeed no spatial transfer is needed, and this direction is constructive and holds for **arbitrary** locales. ✔
* Symmetry: the twist automorphism of `X ×_loc X` restricts to `E` precisely when `E` is symmetric and exchanges `p_1`, `p_2`. ✔

### 3.4 Scope remarks for L

* **L is valid as stated.** With §6.1 below, the hypothesis "`O(X)` continuous" is used *only* to make the localic product spatial (B2) — not in the topological argument itself. See §7 for the generalisations this suggests.
* The theorem is stated for `E ↪ X ×_loc X`. Since T allows different spaces and Isbell's theorem allows any spatial `Y`, L holds verbatim for closed `E ↪ X ×_loc Y` with `O(X)` continuous and `Y` any spatial locale (no local compactness on `Y`).

---

## 4. Issues list (all editorial; none fatal)

1. **(Must state)** "Directed" = non-empty directed; see §1. Otherwise T2 ⇒ T1 and the reverse direction of L fail for non-surjective projections.
2. **(Should state)** Theorem T's hypothesis "X weakly locally compact" is not needed for T1 ⟺ T2 (§6.1). Keeping it is harmless but the paper's sanity-check §5(1) ("closedness of E and weak local compactness play different roles") then needs rewording: weak local compactness plays a role only for T3.
3. **(Optional)** Point out that the proof of T1 ⇒ T2 uses Scott continuity of `r_E` only at directed families whose union is `X` (see §6.3); this is a genuinely weaker hypothesis and makes the theorem sharper.
4. **(Optional)** Avoid the choice function in §2.1 by indexing over all pairs `(V,K)` (§2.1 above).
5. **(Optional)** In §2.2, remark that (2.2) is the "closed" case of the general `f_*(V) = int(Y∖f(Z∖V))`; this makes it obvious why closedness of `f` is the extra ingredient.
6. **(Optional)** Mention that "closed with compact fibres" is Bourbaki's *proper* (universally closed) map, *Topologie Générale* I §10 Thm 1, valid with no separation axioms. Then T reads: "`r_E` Scott-continuous ⟺ `p_Y` proper", mirroring L exactly.
7. **(Optional)** Add the example of §2.4 to packet §5 to show closedness of `E` cannot be dropped, and the example of §6.4 to show that for *general* maps Scott continuity of `f_*` does **not** imply closedness — so the theorem is specifically about projections of closed relations.
8. **(Optional, B2)** Cite Isbell 1981 for the product comparison; it gives the sharper "for all `Y`" form that is needed for the generalisation in §3.4.

No incorrect uses of external literature were found. The references in packet §6 are appropriate for their stated roles.

---

## 5. Remarks on the §4 corollary (supplementary target only)

I did not referee this in depth, as instructed. Two points to pin down before relying on it:

* **Exact hypotheses of the effectiveness/quotient theorem.** Vermeulen's descent results concern proper maps/surjections; the statement "closed proper internal equivalence relation ⇒ effective, with proper quotient map" should be quoted with its precise hypotheses (both projections proper? closedness of `E` in `X×X`? existence/behaviour of the coequaliser in **Loc**?). The packet correctly flags this as background, but the chain "proper ⇒ effective ⇒ quotient continuous ⇒ strongly Hausdorff ⇒ completely regular" has four links each needing a citation with matching hypotheses.
* **"Quotient is continuous (locally compact)."** For spaces this is the fact that a perfect surjective image of a locally compact space is locally compact; for locales a precise reference is needed (the packet already notes "proper-quotient continuity" as an input). Strong Hausdorffness of the quotient from closedness of `E` plus properness of `q×q` is fine.

Nothing here affects T or L.

---

## 6. Stronger conclusions that genuinely follow (separated from the verdict)

### 6.1 Theorem T′: the local compactness hypothesis can be dropped

**Theorem T′.** Let `X`, `Y` be arbitrary topological spaces and `E ⊆ X×Y` closed. Then `r_E = (p_Y)_* p_X^*` preserves (non-empty) directed joins iff `p_Y : E → Y` is closed with compact fibres.

*Proof of ⇐:* packet §2.2 (uses neither closedness of `E` nor local compactness).

*Proof of ⇒.* Throughout, `W ⊆ r_E(U)` for open `W` iff `E ∩ (X×W) ⊆ U × Y`; in particular `y ∈ r_E(U)` implies `E_y ⊆ U`; and `r_E(X) = Y`.

*Compact fibres.* Fix `y` and a directed open family `(U_j)` with `E_y ⊆ ⋃U_j`. Since `E` is closed, `E_y` is closed in `X`, so `V_j := U_j ∪ (X∖E_y)` is open; `(V_j)` is directed with union `X`. By Scott continuity `Y = r_E(X) = ⋃_j r_E(V_j)`, so `y ∈ r_E(V_j)` for some `j`, whence `E_y ⊆ V_j`, whence `E_y ⊆ U_j`. So `E_y` is compact.

*Closed map.* Let `H ⊆ E` be closed in `E`, hence closed in `X×Y`, and let `y ∉ p_Y(H)`. For every `x ∈ X` we have `(x,y) ∉ H`, so there are opens `A_x ∋ x`, `B_x ∋ y` with `(A_x × B_x) ∩ H = ∅`. The finite unions `U_F = ⋃_{x∈F} A_x` (`F ⊆ X` finite) form a directed open cover of `X`. By Scott continuity there is a finite `F` and an open `W ∋ y` with `W ⊆ r_E(U_F)`, i.e. `E ∩ (X×W) ⊆ U_F × Y`. Put `B := W ∩ ⋂_{x∈F} B_x`, an open neighbourhood of `y`. If `y′ ∈ B` and `(x′,y′) ∈ H ⊆ E`, then `x′ ∈ U_F`, so `x′ ∈ A_x` for some `x ∈ F`, and `y′ ∈ B_x`; thus `(x′,y′) ∈ (A_x×B_x) ∩ H = ∅`, a contradiction. Hence `B ∩ p_Y(H) = ∅`, and `p_Y(H)` is closed. ∎

*Remarks.* (a) Choice-free; classical logic only. (b) The argument is a "tube lemma in which Scott continuity replaces compactness": local compactness manufactured a compact tube in the packet, but the directed cover `(U_F)` built from *the closedness of H itself* already suffices. (c) The packet's proof remains correct; it is just not the sharpest.

### 6.2 Where weak local compactness really lives: condition T3

T3 is **not** equivalent to T1/T2 in general. Example: `X = Y = ℚ`, `E = Δ`. Then `r_E = id` is Scott-continuous and `p_Y` is a homeomorphism (T1, T2 hold), but T3 requires an open `W ∋ y` and compact `K` with `W ⊆ K`, impossible in `ℚ`. In general, for closed `E`:

> T3 ⟺ T2 **and** every `y ∈ Y` has a neighbourhood `W` with `p_X(p_Y^{-1}W)` contained in a compact subset of `X`.

Under weak local compactness of `X` the second clause follows from T2 (cover the compact fibre `E_y` by finitely many relatively compact opens with union `U`; then `y ∈ r_E(U)` by (2.2) gives the `W`), which is a slightly more direct proof of T2 ⇒ T3 than going through T1. So the packet's §2.3 is correct as stated, and the hypothesis is exactly right for T3.

### 6.3 Scott continuity "at the top" suffices

Both halves of the ⇒ proof in §6.1 (and the packet's own proof) use Scott continuity of `r_E` only for directed families whose union is `X`. Hence T′ can be stated with the a priori weaker hypothesis

> (T1⁻) for every directed open cover `(U_j)` of `X`, `⋃_j r_E(U_j) = Y`,

and T1⁻ ⟺ T1 ⟺ T2. This is a useful checkable criterion in applications.

### 6.4 Semi-proper = proper for projections of closed relations

Since Scott continuity of `(p_2)_*` on all of `O(E)` trivially implies that of `r_E`, T′/L give: *for the projection of a closed relation, Scott continuity of `(p_2)_*` (semi-properness) already implies the closed Frobenius law (properness).* This fails for general maps: `f : {∗} → S` into Sierpiński space hitting the open point has `f_*` trivially Scott-continuous but `f_*(∅ ∪ f^{-1}{a}) = Y ≠ ∅ ∪ {a}`. Consistently, the corresponding relation `{(∗,a)} ⊆ {∗} × S` is not closed.

### 6.5 Bourbaki-properness

By Bourbaki (TG I §10 Thm 1, no separation axioms), "closed with compact fibres" is equivalent to "universally closed" (`p_Y × id_T` closed for all `T`). So T′ says: `r_E` Scott-continuous ⟺ `p_Y` is Bourbaki-proper — the exact spatial shadow of L's conclusion, which makes the packet's two theorems a single statement in two categories.

### 6.6 Consequences for L

Using T′ in place of T, the forward direction of L needs only: `X`, `Y` spatial and `X ×_loc Y` spatial (then closed sublocales are closed subspaces by B3). Hence:

> **L′.** Let `X`, `Y` be spatial locales with `X ×_loc Y` spatial (e.g. `O(X)` continuous and `Y` arbitrary spatial, by Isbell 1981), and `E ↪ X ×_loc Y` closed. Then `(p_2)_* p_1^*` is Scott-continuous iff `p_2 : E → Y` is proper.

The continuity hypothesis on `O(X)` is now visibly a *product-spatiality* hypothesis and nothing more.

---

## 7. Suggestions for pushing further (clearly conjectural where marked)

### 7.1 A point-free reformulation: Scott continuity of `r_E` = a map `Y → P_U X`

`r_E` always preserves finite meets (`p_1^*` is a frame map; `(p_2)_*` preserves all meets). So **`r_E` is Scott-continuous iff it is a preframe homomorphism `O(X) → O(Y)`**, i.e. (by the universal property of the upper powerlocale, Johnstone *Elephant* C4.1 / Vickers) iff there is a locale map `φ : Y → P_U X` with `φ^*(□u) = r_E(u)`. Topologically: iff `y ↦ ↑E_y` (saturation of the fibre) is a continuous map into the Smyth hyperspace of compact saturated sets — an upper-semicontinuous compact-valued multifunction. Theorem T′ is then the relational form of the classical equivalence "perfect map ⟺ usc compact-valued fibre map", which I would regard as folklore-adjacent. This reformulation is worth stating in the paper because it explains *why* the theorem is true.

### 7.2 Conjecture: L holds for arbitrary locales, constructively

The reverse direction already holds for arbitrary locales. For the forward direction the following point-free route looks viable; items (a)–(e) I have checked, item (f) is the one external fact to verify.

Let `X`, `Y` be locales, `a ∈ O(X) ⊕ O(Y)`, `E = c(a)`, `r(u) = π_{2*}((u⊕1) ∨ a)` Scott-continuous.

(a) `r` is a preframe homomorphism (above), giving `φ : Y → P_U X`.
(b) Let `K ⊆ X × P_U X` be the sublocale "where `1⊕□u ≤ u⊕1` for all `u`" (the largest sublocale `S` with `S ∩ o(1⊕□u) ∩ c(u⊕1) = ∅` for all `u`; this exists because meeting with a complemented sublocale preserves all joins in the coframe of sublocales). Its pullback along a point `F` of `P_U X` (a Scott-open filter) is `⋂_{u∈F} o(u)`, the corresponding compact fitted sublocale — so `K` is the *generic compact fitted sublocale*.
(c) A map `h : E → Z` factors through "where `s ≤ t`" iff `h^*s ≤ h^*t` (via `h[h^{-1}o(s)] = h[E] ∩ o(s)`). Hence, with `g = 1_X × φ`, `E ⊆ g^{-1}(K)` iff `(1 ⊕ r(u)) ∨ a ≤ (u ⊕ 1) ∨ a` for all `u`, which holds **by definition of `r`** (`1⊕r(u) ≤ (u⊕1) ∨ a`). ✔
(d) `g^{-1}(K) → Y` is the pullback of `K → P_U X` along `φ`.
(e) `E ↪ g^{-1}(K)` is a closed sublocale inclusion (as `E` is closed in `X×Y`), hence proper; proper maps are pullback-stable and closed under composition (Vermeulen 1994).
(f) **To verify:** `K → P_U X` is proper. This should be the relative form of Vickers' description of generalized points of `P_U X` (*Constructive points of powerlocales*, Math. Proc. Camb. Phil. Soc. 122 (1997)) combined with "proper = fibrewise compact" (Johnstone–Vermeulen, *Elephant* C3.2); I have **not** checked the literature statement in the form needed.

If (f) holds, then `p_2 = (g^{-1}K → Y) ∘ (E ↪ g^{-1}K)` is proper, and one obtains:

> **Conjectural Theorem L\*.** For arbitrary locales `X`, `Y` and any closed sublocale `E ↪ X × Y`: `(p_2)_* p_1^*` preserves directed joins ⟺ `p_2` is proper. Constructively valid; no continuity, spatiality, or choice.

This would subsume T′, L, L′, and eliminate B1–B3 entirely. Note that `g^{-1}(K)` is the "fibrewise saturation" of `E` over `Y`; `E` itself need not be fitted, which is why the closed-inclusion step (e) is needed.

### 7.3 Smaller items

* With T1⁻ (§6.3), Project A's practical test for properness of the inseparability projections reduces to checking `⋃_j r_𝓘(U_j) = X` for directed covers `(U_j)` of `X` — i.e. "every point has a neighbourhood over which all inseparable points are already caught by a single `U_j`".
* For reflexive `E`, `r_E(U) ⊆ U`; for `E = cl(Δ)` one has `r_𝓘(U) = int{y : cl(Δ)_y ⊆ U}`, and Scott continuity of `r_𝓘` is a form of "uniform local separation". It may be worth recording in §4 what T1⁻ says concretely for `𝓘`.
* The packet's remark §5(4) (idempotence) could be sharpened: for a closed *equivalence* relation with proper projections one has `r_E r_E = r_E` (because `E∘E = E` and the box of a composite of relations with proper projections is the composite of boxes); without properness the interior operators interfere.

---

## 8. Answers to the seven specific verification requests

1. Weak local compactness suffices for the forward argument; no Hausdorffness or closedness of compacta is used. (And it can be dropped altogether, §6.1.)
2. Directed cover, uniform compact support (2.1), closed-subset-of-`E` handling, and the compact-factor projection are all correct; the tube lemma is correctly invoked without separation axioms.
3. Reverse direction is correct for empty fibres and arbitrary `X, Y`, **provided** directed families are non-empty (§1).
4. T3 is equivalent to T1/T2 under the stated hypotheses, and is the one condition that needs them (§6.2).
5. B1 is classical and needs choice; B2 holds (and more generally for any spatial `Y`, Isbell 1981); B3 holds with the explicit isomorphism `↑a ≅ O(Z∖a)`.
6. Scott continuity of `(p_2)_*` vs. properness: the Frobenius computation (3.1) is correct; for projections of closed relations the two notions coincide (§6.4), for general maps they do not.
7. Symmetry claim correct; transitivity is used only in §4; the quotient chain in §4 needs its citations pinned to exact hypotheses (§5); terminology is handled carefully.

---

## 9. Literature consulted (independently chosen)

* N. Bourbaki, *Topologie Générale*, Ch. I §10 (proper maps = closed with quasi-compact fibres; no separation axioms).
* J. R. Isbell, *Product spaces in locales*, Proc. AMS 81 (1981) 116–118 (sober-space embedding preserves `X×Y` when `X` is quasi-locally compact).
* P. T. Johnstone, *Stone Spaces* (1982), II.2 (products), VII.4 (continuous frames are spatial); *Sketches of an Elephant* (2002), C3.2 (proper maps), C4.1 (powerlocales).
* J. Picado, A. Pultr, *Frames and Locales* (2012), Ch. VII; *Notes on the product of locales*, Math. Slovaca 65 (2015).
* J. J. C. Vermeulen, *Proper maps of locales*, JPAA 92 (1994) 79–107 (definition: Scott-continuous `f_*` + Frobenius; pullback stability; composition).
* S. Vickers, *Constructive points of powerlocales*, Math. Proc. Camb. Phil. Soc. 122 (1997) 207–222 (global and generalized points of `P_U`).
* J. Goubault-Larrecq, blog posts on Plewe's game and localic vs topological products (for the `ℚ` examples; secondary source).

---

*End of report. The referee is willing to answer follow-up questions on any step, and in particular to attempt the verification of item 7.2(f) if the researcher wishes to pursue L\*.*