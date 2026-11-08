# Independent referee report — unrestricted localic Scott‑continuity converse (L\*)

**Packet examined:** `ProjectA_Lstar_EXTERNAL_INDEPENDENT_packet_2026-11-08.md` (read after `..._prompt_2026-11-08.md`, as instructed).
**Date of report:** 8 November 2026.
**Independence statement:** No prior Project A audits, internal reconciliations, comparative verdicts, ledgers or referee reports were consulted. The only outside material consulted was the published literature (bibliographic checks on Vermeulen 1994, Vickers 1995/1997, Townsend 2005, Moerdijk–Vermeulen 2000, Johnstone's *Elephant*); none of it was used to shortcut the verification of the candidate proof, which was reconstructed step by step from the packet alone.

---

## 0. Verdict

**Overall: VALID.** The candidate proof of L\* is correct. I found no fatal error, no illicit distributivity of `□` over non‑directed joins, and no unproved passage from "pointwise compact family" to "proper map". Every nontrivial step (the C‑ideal model, the nucleus of `K`, both nested inductions in Lemma 2, the directedness and distributivity claims in (S) and (F), the classifying map, the pullback/pasting argument, and the closedness of `E ↪ Ẹ`) was independently reconstructed and checked, with details in §§2–6 below.

Scope of the verdict:

* **Classically:** L\* holds for arbitrary locales `X, Y` and arbitrary closed `E ↪ X×Y`, with no continuity, spatiality or compactness hypotheses. Unconditional, given the published theorem that proper maps are pullback‑stable (B4(c), Vermeulen 1994).
* **Constructively (topos‑valid, choice‑free):** the candidate proof itself is fully constructive and uses no choice; it is impredicative (least sets closed under rules; frames of C‑ideals), i.e. valid in the internal logic of any elementary topos, not in a predicative setting such as CZF/formal topology without further work. The **only** external input that is not elementary is B4(c). I did not re‑derive B4(c); the literature states it constructively (Vermeulen 1994 via preframes; Vickers 1995 "Locales are not pointless" gives an explicitly topos‑valid account of properness; Johnstone's *Elephant* C3.2 develops proper maps over an arbitrary base). So the constructive claim stands **exactly as conditional on B4(c) as the packet says it is**, and no more.

**Nonfatal issues found (all exposition, none propagate):** one genuinely false sentence in (C) ("principal downsets `↓(s,u)` are C‑ideals"), which contaminates one formula in Lemma 1 Step 3 and two "is" identifications; a precise repair is given in §2.3 and §3.3. A few spatial asides are loosely stated. Nothing else.

**Antecedents:** Theorem K is, in content, the "generic‑point" form of the constructive Hofmann–Mislove / upper‑powerlocale correspondence (Johnstone 1985 classically; Vickers 1997 constructively for generalized points; Townsend 2005 categorically), combined with the standard "proper = fibrewise compact" reading of properness. The packet's proof of Theorem K is a different, direct, self‑contained argument and does not depend on those results. For L\* **as stated** I found no published antecedent; it appears to be an easy corollary of the generalized‑point form of the P_U‑characterization *if* that is stated in the fibrewise‑proper form (I could not confirm the exact wording of Vickers 1997 from the full text; see §7). Originality of the *statement* should therefore be claimed only cautiously; originality of the *technique* of Lemma 2 seems plausible but I have not searched exhaustively.

---

## 1. Independent plausibility checks performed before reading the proof

To avoid being led by the packet, I first tested the *statement*.

**(a) Spatial argument for (⇒).** For sober spaces with `E ⊆ X×Y` closed, write `E_y` for the fibre and `r(u) = int{y : E_y ⊆ u}`. Suppose `r` preserves directed unions. *Compact fibres:* if `E_y ⊆ ⋁↑u_k` then `y ∈ r(⋁u_k) = ⋃ r(u_k)`, so `E_y ⊆ u_k` for some `k`. *Closedness (tube property):* given `E_y ⊆ U` open, for each `x ∉ U` closedness of `E` gives an open rectangle `s_x × w_x ∋ (x,y)` missing `E`. The family `U_F := U ∪ ⋃_{x∈F} s_x`, `F` finite, is directed with union `X`, and `r(X) = Y`, so `y ∈ r(U_F)` for some `F`; intersecting that neighbourhood with `⋂_{x∈F} w_x` gives a neighbourhood `V` of `y` with `E_{y'} ⊆ U` for `y' ∈ V`. Hence `{y : E_y ⊆ U}` is open, i.e. `p₂` is closed. So spatially L\* is true, and the point‑free proof must replace "pick `x ∉ U`" by something — the packet replaces it by the universal family `K`.

**(b) Necessity of closedness.** `X=Y=ℝ`, `E = {xy=1}` (closed, compact fibres, `p₂` not closed): `r((−n,n)) = {|y|>1/n}`, whose union misses `0 ∈ r(ℝ)`. Consistent with L\*. For a non‑closed `E` (graph of the identity over `ℝ∖{0}`) `r` again fails Scott‑continuity, so no counterexample arises from dropping closedness either; but closedness *is* used essentially in Steps 1, 3 and 5.

**(c) Degenerate cases.** `Y = 1`: L\* reduces to "a closed sublocale `F = c(a)` is compact iff `F → 1` is proper", with Frobenius for the terminal map following from Scott‑continuity by the directed set `{v} ∪ {1 | p}` — the same truth‑value‑indexed directed join the packet uses in (F). `E = ∅`: both sides true. `E = X×Y`: both sides ⟺ `X` compact.

**(d) Theorem K spatially.** For `X` sober and locally compact (so `P_U X` is spatial with points the compact saturated `Q`), `K = {(x,Q) : x ∈ Q}`; fibres are compact and the standard finite‑subcover argument shows `π_K(H)` is closed for `H` closed in `K` (one exhibits `□(⋂u_i ∩ ⋃s_i)` as a neighbourhood of `Q` missing `π_K(H)`). Note `K` need **not** be closed in `X × P_U X` (Sierpiński `X` already fails), so any argument must address properness of `π_K` directly, which the packet does.

These checks make the statement credible; they play no role in the verification below.

---

## 2. Foundations: B1, B2, (C), the `σ_e` repackaging (prompt item 1; check 1)

### 2.1 Presentations and the coverage (correct)

* `O(W)`: generators `□u` qua ∧‑semilattice (so `□1 = 1`, `□(u∧u') = □u∧□u'` are the semilattice structure), relations `□(⋁↑u_k) = ⋁□u_k`. The coverage `u ◁ {u_k}` (directed, join `u`) is meet‑stable in the strict sense required by *Stone Spaces* II.2.11: for `b ≤ u`, `{b∧u_k}` is directed with join `b`. ✓
* `O(X)` presented by itself qua ∧‑semilattice with all join relations (including the empty join). ✓
* Coproduct of presented frames = presentation on the product semilattice with relations in each coordinate (II.2.13 and its evident generalization; one recovers the two frame maps as `g₁ ↦ (g₁,1)`, `g₂ ↦ (1,g₂)`). ✓
* Meet‑stability of the mixed coverage on `O(X)×O(X)`: meeting `(⋁s_j,u) ◁ {(s_j,u)}` with `(b₁,b₂) ≤ (⋁s_j,u)` gives `{(s_j∧b₁, b₂)}` covering `(b₁,b₂)`; meeting `(s,⋁↑u_k) ◁ {(s,u_k)}` with `(b₁,b₂)` gives the directed `{(b₁, u_k∧b₂)}` with join `(b₁,b₂)`. ✓

So **(C) is the correct frame‑coproduct presentation**, and the C‑ideal description (downsets closed under (i) all first‑coordinate joins *including the empty one*, and (ii) directed second‑coordinate joins) is right.

### 2.2 The `σ_e` repackaging (correct)

`e_v = {s : (s,v) ∈ e}` is a downset closed under all joins (by (i)), hence `↓σ_e(v)` with `σ_e(v) = ⋁e_v ∈ e_v`. Antitone by the downset property; (ii) ⟺ `⋀_k σ_e(v_k) ≤ σ_e(⋁↑v_k)` and the reverse inequality is antitonicity. Conversely any antitone `σ` with `σ(⋁↑v_k) = ⋀σ(v_k)` gives a C‑ideal. Order = pointwise order. ✓ Sanity check `X = 1`: antitone Scott‑continuous `σ: Ω → Ω^op` are determined by `(σ(⊤) ≤ σ(⊥))`, recovering `O(P_U 1) = O(Sierpiński) ≅ Ω^{→}`. ✓

**So `O(X × P_U X) ≅ {Scott‑continuous O(X) → O(X)^op}` is correct** and is the cleanest way to read the whole proof.

### 2.3 One false sentence and its repair (nonfatal)

> "Principal downsets `↓(s,u)` are C‑ideals … `1 ⊕ □d` is `↓(1,d)`; `u ⊕ □u` is `↓(u,u)`."

**False.** Rule (i) with the empty family forces `(0,v) ∈ e` for **every** `v`, but `(0,v) ∈ ↓(s,u)` only when `v ≤ u`. So `↓(s,u)` is never a C‑ideal unless `u = 1`. (By contrast `↓(u,1) = {(s,v) : s ≤ u}` *is* a C‑ideal — this is used correctly in Lemma 1 Step 3.) The frame element `s ⊕ □u` is the C‑ideal **generated** by `(s,u)`, `cl↓(s,u) ⊋ ↓(s,u)` in general.

**What survives (everything that is used):** by B1, `s ⊕ □u ≤ e ⟺ cl↓(s,u) ⊆ e ⟺ (s,u) ∈ e` for every C‑ideal `e`. This is the only consequence the proof needs, and it is correct. Likewise `(d,d) ∈ ↓(1,d) ⊆ 1⊕□d`, used for `D ≤ Ψ(1⊕D)`, is fine.

**Where the false sentence is actually applied:** Lemma 1 Step 3 computes `k(↓(1,u))`, i.e. applies the nucleus to a non‑element. Repair (one line): since `k` is a nucleus, `k(1⊕□u) ≤ k(u⊕1) ⟺ 1⊕□u ≤ k(u⊕1) ⟺ (1,u) ∈ k(↓(u,1)) = {(s,v): s∧v ≤ u} ⟺ u ≤ u`. ✓ Theorem K (F) uses only the set `G` (the first‑coordinate‑join closure of `e ∪ ↓(1,d)`), never the C‑ideal `1⊕□d` itself, so it is unaffected; and `cl(G) = e ∨ (1⊕□d)` holds because `cl(e ∪ ↓(1,d)) = cl(e) ∨ cl↓(1,d)`.

*Side remark (constructive, not needed for the proof).* Even the natural constructive candidate `{(s,v) : s ≤ ⋁{1 | v ≤ d}}` for the C‑ideal `1⊕□d` is only a C‑ideal when `v ↦ χ(v≤d)`, `χ := ⋁{1 | −}: Ω → O(X)`, turns directed joins into meets, i.e. when `⋀_k χ(p_k) ≤ χ(∀k p_k)`. That is automatic classically (`χ` takes values in `{0,1}`), but it is a constant‑domain‑type principle that fails in general: in `Sh(ℝ)` take `O(X) = Idl(D)` where `D(U)` is the lattice of maps `U → {⊥,⊤}` with closed `⊤`‑locus; with `d = 0`, `v_k = ↓y_k`, `y_k` the section with `⊤`‑locus `ℝ∖(−1/k,1/k)`, and `x₀` the section with `⊤`‑locus `{0}`, one finds `x₀ ∈ ⋀_k χ(v_k ≤ 0)` but `x₀ ∉ χ(⋁v_k ≤ 0)`. So authors should not describe `1⊕□d` by that formula in a constructive text. The packet's proof never does.

---

## 3. Lemma 1 — nucleus of `K` and the formula for `(π_K)_*` (prompt item 2; check 2)

### 3.1 Sublocale calculus B3a–B3c (correct, constructive)

* **B3a.** I re‑proved it via nuclei: `S ⊆ c(s) ∨ o(t)` iff `(x∨s) ∧ (t→x) ≤ j_S(x)` for all `x`. (⇒) put `x = t`. (⇐) `(x∨s)∧(t→x) ≤ x ∨ (s ∧ (t→x))` and `s ∧ (t→x) ≤ j_S(t) ∧ j_S(t→x) ≤ j_S(x)`. The packet's coframe‑distributivity proof is also fine (`c(s) ∨ o(s) = Z` holds constructively: `(x∨s)∧(s→x) ≤ x`). ✓
* **B3b, B3c.** Image = `Fix(h_*h^*)`; `h_*h^*s ≤ h_*h^*t ⟺ h^*s ≤ h^*t` (apply `h^*`, resp. `h_*`); preimage characterized by factorization; two sublocales with the same factoring maps coincide. ✓ Preimages preserve intersections (a map factors through `⋂S_i` iff through each). ✓ No points used anywhere.

### 3.2 Step 1 (`e^K` is a C‑ideal) — correct

Downset ✓; (i) including empty join ✓ (`(0∧v,v) = (0,v) ∈ e`); (ii): the two‑index trick (`(s∧u_j, u_k) ≤ (s∧u_l,u_l)` for `l ≥ j,k`, then (ii) in `k`, then (i) in `j`) is correct and uses only existence of upper bounds inside the proof — no choice.

### 3.3 Steps 2–4 — correct (Step 3 after the repair in §2.3)

`k` inflationary/idempotent/meet‑preserving ✓. `j_K ≤ k` via B3a for `S_k` ✓ (with the repaired computation). `k ≤ j_K`: for `(s,v)` with `(s∧v,v) ∈ e`, `i_K^*(s⊕□v) = i_K^*(s⊕1) ∧ i_K^*(1⊕□v) ≤ i_K^*(s⊕1) ∧ i_K^*(v⊕1) ∧ i_K^*(1⊕□v) = i_K^*((s∧v)⊕□v) ≤ i_K^*(e)` ✓, then join over `e^K` ✓.

### 3.4 Displayed equivalences and `Ψ` — correct

`i_K^*(1⊕□u) ≤ i_K^*(e) ⟺ 1⊕□u ≤ j_K(e) ⟺ (1,u) ∈ e^K ⟺ (u,u) ∈ e ⟺ u ≤ σ_e(u)` ✓ (each step via B1 or the formula). `(π_K)_*(i_K^*e) = ⋁{C : i_K^*(1⊕C) ≤ i_K^*e}` and, since `C` is a join of generators and both `1⊕(−)` and `i_K^*` preserve joins, this equals `⋁{□u : (u,u) ∈ e} = Ψ(e)` ✓.

**Lemma 1 is correct and point‑free.** The spatial aside is harmless but imprecise: for a general sober `X` the points of `P_U X` are the Scott‑open filters (classically ↔ compact saturated sets by Hofmann–Mislove), but `P_U X` need not be spatial, so "`(x,Q) ∈ K ⟺ x ∈ Q`" describes global points only. The alternative description of `K` as the equalizer of `π₂` and `m` is correct (`[a ≤ b∧a] = [a ≤ b]`).

---

## 4. Lemma 2 — the closure lemma (prompt item 3; check 3). **Correct.**

This is the step the prompt flags most heavily, so I reconstructed it twice: once following the packet, once by a slightly different double induction.

### 4.1 (a) `P` holds on `C^∞` — correct

The set `{(s,v) : □(s∧v) ≤ V}` contains `G` and is closed under (down), (ii) (`□(s∧⋁↑v_k) = □(⋁↑(s∧v_k)) = ⋁□(s∧v_k)`, the family `(s∧v_k)` being directed), and (i‑dir) (`□((⋁↑s_j)∧v) = ⋁□(s_j∧v)`). Both uses of `□(⋁↑) = ⋁□` are on **directed** families; **there is no use of `□` over a non‑directed join anywhere in the proof.** By the induction principle for the least set, `C^∞ ⊆ {P}`. ✓

### 4.2 (b) `C^∞` is closed under binary first‑coordinate joins — correct

I checked every clause of both inductions.

*First induction, `B'' = {(s',v) ∈ C^∞ : ∀v' ≤ v, ∀(s,v') ∈ G, (s∨s',v') ∈ C^∞}`.*
`G ⊆ B''`: for `(s',v) ∈ G`, `v' ≤ v`, `(s,v') ∈ G`: `(s',v') ∈ G` (downset) so `(s∨s',v') ∈ G ⊆ C^∞` (first‑coordinate joins). ✓
(down): `(s'',v'') ≤ (s',v)`, `v' ≤ v''`, `(s,v') ∈ G` ⇒ `v' ≤ v` ⇒ `(s∨s',v') ∈ C^∞` ⇒ `(s∨s'',v') ∈ C^∞` by (down). ✓
(ii): `(s',v_k) ∈ B''` directed, `v' ≤ ⋁v_k`, `(s,v') ∈ G`: `(s, v'∧v_k) ∈ G` (downset) and `v'∧v_k ≤ v_k`, so `(s∨s', v'∧v_k) ∈ C^∞` for all `k`; `(v'∧v_k)_k` is directed with join `v' ∧ ⋁v_k = v'`; apply (ii) in `C^∞`. ✓ *This is the step the prompt singles out ("use of `v'∧v_k`"); it is correct — the quantification over all `v' ≤ v` in the definition of `B''` is exactly what makes it go through.*
(i‑dir): `(s∨s'_j, v')` is directed in `j` with join `(s∨⋁s'_j, v')`. ✓
Hence `B'' = C^∞`.

*Second induction, `B = {(s,v) ∈ C^∞ : ∀v' ≤ v, ∀(s',v') ∈ C^∞, (s∨s',v') ∈ C^∞}`.*
`G ⊆ B`: for `(s,v) ∈ G`, `v' ≤ v`, `(s',v') ∈ C^∞`: `(s,v') ∈ G`; apply `B'' = C^∞` to `(s',v')` with `v'' := v'` and `(s,v') ∈ G`. ✓ Closure under the three rules is verbatim the `B''` argument with `G` replaced by `C^∞` (I wrote it out; it uses only that `C^∞` is a downset closed under (ii) and (i‑dir)). ✓ Hence `B = C^∞`, and taking `v' = v` gives binary joins.

*Cross‑check by a different route.* Fix `(s₀,v₀) ∈ C^∞` and let `A := {(s,v) : (s∨s₀, v∧v₀) ∈ C^∞}`. `A` is closed under the three rules trivially; `G ⊆ A` follows from a prior induction showing `A' := {(s₀,v₀) : ∀(s,v)∈G, (s∨s₀, v∧v₀) ∈ C^∞}` equals `C^∞`. This is the same double induction in different clothing and confirms (b).

### 4.3 (c) `cl(G) = C^∞` — correct

Arbitrary first‑coordinate joins: finite subjoins exist by (b) and `(0,v) ∈ G`; the family of finite subjoins (indexed by Kuratowski‑finite subsets) is directed with the full join as supremum; apply (i‑dir). Then `C^∞` is a C‑ideal containing `G`, so `cl(G) ⊆ C^∞`; conversely `cl(G)` is closed under the three rules, so `C^∞ ⊆ cl(G)`. ✓ The final sentence `(u,u) ∈ cl G ⇒ □u = □(u∧u) ≤ V` ✓.

### 4.4 Spatial sanity check of the conclusion

For `X = ℕ` discrete, `cl(G)` corresponds to `σ(v) = ⋂_{F ⊆_fin v} τ(F)`; a finite `F ⊆ σ(v)∧v` satisfies `F ⊆ τ(F)∧F`, hence `F ∈ V` by the hypothesis on `G`. Consistent with Lemma 2 (and it shows why the lemma needs no closure of `V` under unions — the finite set `F` is caught by a *single* `(τ(F),F) ∈ G`).

**Lemma 2 is correct, constructive and choice‑free.** The "why the detour is needed" remark is accurate: the predicate `P` is not stable under binary first‑coordinate joins, and (b) is precisely the statement that the C‑ideal closure of an already first‑coordinate‑join‑closed downset never needs to re‑apply them.

---

## 5. Theorem K — `π_K` is proper (prompt item 4; checks 4–5). **Correct.**

### 5.1 Reduction via B5 — correct

B5 as stated is right and choice‑free (the largest preimage `j(x)` is canonical; directedness of the `e_k` follows from `q(e_k ∨ e_l) = x_l`). With `L = O(X×W)`, `q = i_K^*`, `Φ = (π_K)_*`, `Φ∘q = Ψ` (Lemma 1), (S) gives Scott‑continuity of `(π_K)_*`. For Frobenius: every `x ∈ O(K)` is `i_K^*(e)` (take `e := x ∈ Fix(j_K)`), and `x ∨ π_K^*D = i_K^*(e ∨ 1⊕D)`, so (F) gives `(π_K)_*(x ∨ π_K^*D) = (π_K)_*x ∨ D`. ✓ The trivial inequalities `≥` are correctly justified (`(d,d) ∈ ↓(1,d) ⊆ 1⊕□d`).

### 5.2 (S) — correct

`G = {(s,v) : s ≤ ⋁_j σ_{e_j}(v)}` is the first‑coordinate‑join closure of `⋃e_j`, a downset, and `cl(G) = ⋁↑e_j` (since `⋃e_j ⊆ G ⊆ cl(⋃e_j)`). For `(s,v) ∈ G`: `(σ_{e_j}(v))_j` is directed because `(e_j)` is (inhabited and directed), so `s∧v = ⋁↑_j t_j`, `t_j := s∧v∧σ_{e_j}(v)` (frame distributivity). `t_j ≤ v` ⇒ `σ_{e_j}(v) ≤ σ_{e_j}(t_j)` ⇒ `t_j ≤ σ_{e_j}(t_j)` ⇒ `(t_j,t_j) ∈ e_j` ⇒ `□t_j ≤ Ψ(e_j)`. `□(s∧v) = ⋁□t_j` (directed) `≤ V`. Lemma 2 applies (its hypotheses on `G` hold) and gives `Ψ(⋁↑e_j) ≤ ⋁Ψ(e_j)`. ✓

### 5.3 (F) — correct

*Basic case `D = □d`.* `G = {(s,v) : s ≤ σ_e(v) ∨ ⋁{1 | v≤d}}` is indeed the first‑coordinate‑join closure of `e ∪ ↓(1,d)` (⊇: closure; ⊆: `s = (s∧σ_e(v)) ∨ ⋁{s | v≤d}`), is a downset (`v ≤ d ⇒ v' ≤ d` for `v' ≤ v`), and `cl(G) = e ∨ (1⊕□d)`. The set `S = {t} ∪ {s∧v | v ≤ d}`, `t = s∧v∧σ_e(v)`, is **directed constructively**: it is inhabited by `t`, and for two members one performs disjunction‑elimination on their membership (not a case split on `v ≤ d`): both equal `t`, or one is `s∧v` (so `v ≤ d` is known and `s∧v ∈ S` bounds both). Its join is `s∧v`. Then `□(s∧v) = □t ∨ ⋁{□(s∧v) | v≤d} ≤ Ψ(e) ∨ □d` since `t ≤ σ_e(t)` as before and `s∧v ≤ d` when `v ≤ d`. Lemma 2 ⇒ `Ψ(e ∨ 1⊕□d) ≤ Ψ(e) ∨ □d`. ✓ The truth‑value‑indexed join is exactly the device that makes this constructive; I confirm it is used correctly.

*Finite joins of generators.* `1⊕(D₁∨D₂) = (1⊕D₁) ∨ (1⊕D₂)`, and the basic case holds for every `e`, so induction on the (Kuratowski‑)finite set of generators works; the empty join (`D = 0`, `1⊕0 = 0`) is trivially fine. ✓

*General `D`.* `D` is the directed join of its finite subjoins of generators `D_k`; `e ∨ 1⊕D = ⋁↑_k (e ∨ 1⊕D_k)` is a directed join of C‑ideals; apply (S). ✓

**Theorem K is proved, constructively and without choice.** The spatial sanity check for `X = ℕ` is correct (`W` = finite subsets with the Alexandrov topology of `⊇`; `π_K(H)` of an `⊆`‑up‑closed‑sectioned closed set is `⊆`‑up‑closed).

---

## 6. Theorem L\* (prompt item 5; check 6). **Correct.**

* **(⇐)** trivial, as stated. ✓
* **Step 1.** `r` preserves finite meets including the empty one (`r(1) = (p₂)_*(1) = 1`), hence is a preframe homomorphism under the hypothesis; the universal property of the presentation gives the unique `φ: Y → W` with `φ^*(□u) = r(u)`. The explicit formula `r(u) = ⋁{w : 1⊕w ≤ (u⊕1) ∨ a}` is right (`O(E) = ↑a`, `p₂^*w = (1⊕w)∨a`, and `(1⊕w)∨a ≤ (u⊕1)∨a ⟺ 1⊕w ≤ (u⊕1)∨a`). ✓
* **Step 2.** `(1×φ)^*(s⊕C) = s⊕φ^*C`; B3c and preservation of intersections give `Ẹ = ⋂_u [1⊕r(u) ≤ u⊕1]`. ✓
* **Step 3.** `E ⊆ Ẹ ⟺ ∀u: (1⊕r(u))∨a ≤ (u⊕1)∨a`, and `1⊕r(u) = ⋁{1⊕w : 1⊕w ≤ (u⊕1)∨a} ≤ (u⊕1)∨a`. ✓ (Correct observation that this is the only place `E` enters, through `r`.)
* **Step 4.** `(X×W) ×_W Y ≅ X × (W ×_W Y) ≅ X×Y` is a pullback in any finitely complete category; `Ẹ` is by definition the pullback of `K ↪ X×W` along `1×φ`; the pasting lemma makes the outer rectangle `Ẹ → K` over `Y → W` a pullback, with `Ẹ → Y` the composite `Ẹ ↪ X×Y → Y`. Hence `Ẹ → Y` is a pullback of `π_K` along `φ`, proper by Theorem K and B4(c). ✓
* **Step 5.** `E = c(a) ∩ Ẹ = i_Ẹ^{-1}(c(a)) = c(i_Ẹ^*a)`; preimage of a closed sublocale under any map `h` is `c(h^*a)` (a map `g` factors through it iff `g^*h^*a = 0`). Closed inclusions are proper: `i_*` is the inclusion `↑a ⊆ O(Z)`, which preserves all **inhabited** joins (directed joins are inhabited, so the empty‑join subtlety does not arise), and Frobenius is `(x∨a)∨w = x∨w` for `x ≥ a`. ✓ (Matches *Elephant* C3.2.9.)
* **Step 6.** Composite of proper maps proper: `(gf)_* = g_*f_*`, and `(gf)_*(x ∨ f^*g^*w) = g_*(f_*x ∨ g^*w) = g_*f_*x ∨ w`. ✓

**Conceptual reading (consistent with the spatial check in §1):** `Ẹ` is the fibrewise saturation of `E` with respect to the compact family classified by `r`; L\* says the closed `E` sits inside its proper saturation as a closed, hence proper, sublocale.

### 6.1 The one external theorem: B4(c)

Everything above except B4(c) is elementary and verified here. B4(c) — "pullbacks of proper maps are proper", for proper = `f_*` Scott‑continuous + Frobenius — is Vermeulen's theorem (J.J.C. Vermeulen, *Proper maps of locales*, JPAA 92 (1994) 79–107; the paper establishes that the "sensible" definitions of properness agree and that proper maps are precisely the pullback‑stable closed maps). Independent expositions confirm both the statement and that the proof is the preframe analogue of the suplattice proof for open maps (Manuell, *Pointfree topology and constructive mathematics*, arXiv:2304.06000, Thm 3.43 and Rem. 3.44); Johnstone's *Elephant* C3.2 develops proper maps over an arbitrary base topos; Vickers, *Locales are not pointless* (1995) gives an explicitly topos‑valid characterization of properness; Moerdijk–Vermeulen, *Proper maps of toposes* (Mem. AMS 705, 2000) prove pullback stability at topos level. The hypotheses match the packet's definition exactly (Vermeulen's "closed" is the Frobenius identity). I did **not** re‑derive B4(c). Consequently:

* classically, L\* is unconditionally established;
* constructively, L\* is established modulo the (published, and to the best of my reading constructive) pullback stability of proper maps — which is precisely the dependency the packet declares. I found no *additional* hidden classical step.

---

## 7. Scope and antecedents (prompt item 6; checks 7–8)

**Classical validity:** yes, for arbitrary locales, as proved.
**Constructive, choice‑free validity:** yes relative to B4(c); the packet's own arguments use no excluded middle (the two places where a case split would be tempting — `v ≤ d` in (F), and "some `s_j ≠ 0`" in describing generated C‑ideals — are handled or avoided correctly) and no choice (all existentials are used inside proofs or replaced by canonical largest preimages). The metatheory is impredicative (powersets; least sets closed under rules), i.e. topos logic/IZF, not CZF; the packet does not claim predicativity.
**Defect in the claim vs. defect in this proof:** neither. The claim is true and this proof establishes it.
**Narrower surviving theorem:** not needed; the unrestricted statement survives.

**Published antecedents.**

1. *Theorem K.* Its content is: the sublocale `K ↪ X × P_U X` cut out by `π₂^*□u ≤ π₁^*u` is the externalization of the internal fitted sublocale `⋂_{u∈F} o(u)` for the generic Scott‑open filter `F` of `Sh(P_U X)` (truth value of `u ∈ F` being `□u`; the internal "`o(u)` if `u∈F`" externalizes to `c(1⊕□u) ∨ o(u⊕1)`), and `π_K` proper is the statement that this internal sublocale is compact. The global version (Scott‑open filters ↔ compact fitted sublocales) is Johnstone, *Vietoris locales and localic semilattices* (1985) classically and Vickers, *Constructive points of powerlocales*, Math. Proc. Camb. Phil. Soc. 122 (1997) 207–222 constructively — whose abstract states that it extends the Bunge–Funk/Johnstone descriptions **to generalized points**; Townsend, *A categorical account of the Hofmann–Mislove theorem*, Math. Proc. Camb. Phil. Soc. 139 (2005) 441–456 gives an axiomatic version. Interpreting the constructive theorem in `Sh(P_U X)` at the generic point and using "proper = internally compact" (*Elephant* C3.2 / Vermeulen) yields Theorem K. **So Theorem K is known in content**; the packet's direct `Ψ`/Lemma‑2 proof is an independent, self‑contained route that avoids internal‑logic machinery and is, as far as I can tell, new in method. The packet's own "relative Hofmann–Mislove" remark after Lemma 1 shows awareness of this.
2. *L\* as stated.* I found no published statement of the equivalence "`(p₂)_*p₁^*` Scott‑continuous ⟺ `p₂` proper" for closed `E ↪ X×Y`. If Vickers 1997's generalized‑point theorem is stated in the form "maps `Y → P_U X` ↔ sublocales of `X×Y` proper over `Y` and fibrewise fitted" (I could not verify the exact wording from the full text), then Steps 2 and 4 of L\* are an instance of it and L\* is a short corollary (Steps 1, 3, 5, 6 remaining). Either way, the *statement* L\* appears not to be in the literature in this form, but its proof is close to known material; a claim of originality should be limited to the formulation and to the direct proof of Theorem K via Lemma 2, pending a fuller literature search I did not perform.
3. *The frame identity* `O(X×P_U X) ≅ ScottCont(O(X), O(X)^op)` is an immediate consequence of the coverage theorem and of Johnstone–Vickers' preframe view of coproducts; I would not claim it as new.

---

## 8. Findings list (by location)

**Fatal:** none.

**Nonfatal — must fix in a final text:**

* **§2 (C), sentence "Principal downsets `↓(s,u)` are C‑ideals … `1⊕□d` is `↓(1,d)`; `u⊕□u` is `↓(u,u)`."** False (empty‑join clause of (i)). Replace by: "the element `s⊕□u` is the C‑ideal generated by `(s,u)`; by B1, `s⊕□u ≤ e ⟺ (s,u) ∈ e`." Note that `↓(u,1)` *is* a C‑ideal.
* **Lemma 1, Step 3, "`k(↓(1,u)) = … = ↓(1,u)`".** Applies `k` to a non‑element. Replace by: "`k(1⊕□u) ≤ k(u⊕1) ⟺ 1⊕□u ≤ k(u⊕1) ⟺ (1,u) ∈ k(↓(u,1)) ⟺ u∧1 ≤ u`."
* **Theorem K, "`(d,d) ∈ ↓(1,d)`"** — fine, but say `↓(1,d) ⊆ 1⊕□d`.

**Nonfatal — exposition:**

* §3 spatial aside: "points of `W` being compact saturated sets" presupposes Hofmann–Mislove and does not make `P_U X` spatial; label it as a heuristic for global points.
* §1: say explicitly that "directed family" in (ii) and in the preframe relation ranges over inhabited directed *subsets* (or indexed families — both are used) and that finiteness in Theorem K/Lemma 2(c) is Kuratowski‑finiteness; the proofs are correct under either reading.
* Lemma 2: the `B''`/`B` induction could be stated once as a "translation" lemma (fix `(s₀,v₀)`, show `(s,v) ↦ (s∨s₀, v∧v₀)` preserves `C^∞`), which is the same argument but easier to audit.
* State the metatheory precisely: "constructive" = valid in the internal logic of an elementary topos (impredicative), not CZF.
* B4(c): give the precise locus in Vermeulen 1994 (and/or *Elephant* C3.2) in the final text, since it is the one non‑elementary input; the present pointer "Vermeulen 1994; Elephant C3.2" is adequate but not line‑specific.

---

## 9. Delicate steps I independently reconstructed (summary for the record)

1. Meet‑stability of the mixed coverage and the forced membership `(0,v) ∈ e` (which exposed the false "principal downsets" sentence).
2. `O(X×P_U X)` as antitone Scott‑continuous maps, with the `X = 1` sanity check.
3. B3a by a nucleus computation independent of the packet's.
4. Lemma 1 Step 1(ii) two‑index argument; Step 4 inequality chain; the repaired Step 3.
5. Both inductions of Lemma 2(b), clause by clause, plus an alternative "translation" induction giving the same conclusion; Lemma 2(c) via Kuratowski‑finite subjoins.
6. Directedness of `(σ_{e_j}(v))_j`, of `(t_j)`, and of the truth‑value‑indexed set in (F) (by disjunction elimination, not by case split on `v ≤ d`).
7. The absence of any non‑directed use of `□(⋁) = ⋁□`.
8. The pullback/pasting diagram and the identification of `Ẹ → Y` with the pullback of `π_K`; closedness of `E` in `Ẹ`; constructive properness of closed inclusions (inhabited joins).
9. Spatial corroboration of L\* (tube argument) and of Theorem K, plus the `xy = 1` example, performed *before* reading the proof.

---

*End of report. Prepared as a bounded foundational audit; no other Project A questions were pursued.*