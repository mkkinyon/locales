# Referee report — Project A, Q program, Session 8 blind packet

12 November 2026

> **Status note, 13 November 2026.** The text below is the blind report as recorded on 12 November,
> before any repository note was opened. It is unchanged except that N4–N7 now sit with N1–N3.
> Three verdicts were later revisited against the repository: the two "unable to check" items and
> G.4 are all correct. See `REFEREE_SOURCE_CHECK_ADDENDUM_2026-11-13.md`, which also records that N1
> reproduces an existing repository theorem and that N3 answers the repository's stated next test.

## Bottom line

No displayed theorem in the packet is false. Every boxed result from (A.1) to (F.3) and every control in G checks out, some subject to a named import. Q and Q′ stay open; nothing in the packet or in this audit closes or refutes either.

Five findings change what the packet should say.

1. **The rigidity import is a three-line lemma.** One-sided regular rigidity holds for every target frame, using binary covers only. The regular-remainder case of (B.2) then holds for every q, with no Booleanization (N1, N2 below).
2. **(D.1) is correct but its hypothesis is not tight in one direction and is sharp in the other.** The D₂ half needs only (κ,2)-distributivity. Distributivity cannot be dropped: for the Cohen base B and the Scott space S, `D₂(B×S)` is strictly smaller than `Δ_B×D₂(S)` (N4, N5).
3. **The "deliberately open" Cohen test is settled at the closed level.** For every Boolean Z and every anti-Urysohn Y, `W(Z×Y)=W₂(Z×Y)=U(Z×Y)=Δ_Z×Y²`, with no distributivity and no basis hypothesis (N3). Only the non-closed question about `D(B×A)` remains open.
4. **The Arrieta citation overstates the source.** The paper proves strong Hausdorffness and the anti-Urysohn property. It does not state a countable basis and says nothing about fitted diagonals. Both facts are true and each has a two-line proof, which the packet should give instead of citing.
5. **Three statements cannot be checked as written.** They are the support-reduction sentence closing B.2, the two clopen-gluing variants in C.2 and C.3, and the undefined "two-apex space" in G.4. For G.4 an explicit space is supplied (N6).

## Scope, method and independence

This assessment rests on the blind packet alone, re-derived from first principles in the order D, E, F, C, B, G, A. Classical logic with choice is assumed throughout, as the packet states.

- **Repository notes: not consulted.** The linked source notes could not be opened from this session. No internal audit, earlier report or reconciliation memo was seen. Nothing below depends on them, except the three items marked "unable to check".
- **Published control: opened after the independent pass.** Arrieta's Section 4 was read in the arXiv version (2310.18522v1). Numbering there matches the packet's citation of Example 4.5; the journal version was not compared line by line.
- **Standard theorems: cited from memory.** Gleason projectivity, properness of compact-fibre projections, the Baire property of locally compact sober spaces, forcing distributivity and the adjunction between image and preimage of sublocales were not re-opened. Each is listed under Imported inputs with the exact form used.
- **Machine check.** The six-point fence of G.1 was brute-forced: `W=U`, `U>I`, `(0,4)∈U`, `(0,4)∉I`, contact core `{1}`. Identity (A.1) and `W=U` were confirmed on 400 random posets with at most six points.

Verdict vocabulary follows the referee prompt: correct, correct subject to a named import, gap, false, unable to check. Labels N1 to N7 refer to the section "New results from the audit".

## Verdicts at a glance

Twenty-four of twenty-six claim groups are correct, five of them subject to a named import or existence input. Two cannot be checked as stated.

| Ref | Claim | Verdict | Note |
| --- | --- | --- | --- |
| (A.1) | Rank-zero identity Φ(0)=Φ₂(0)=z | Correct | Classical rectangle positivity only |
| (A.2)–(A.3) | W₂=U iff Φ₂(z)=z; Q′ implies Q | Correct | |
| (A.4)–(A.5) | Hole `E_C` and its formula as relative interior of `cl T_C` | Correct | Both inclusions verified |
| (B.1) | Locally finite covers; locus `ℓ_C` | Correct | |
| (B.2) | Compact remainder gives a two-step bound | Correct | |
| B.1 end | Regular remainder version | Correct | Import proved in N1; stronger direct form in N2 |
| (B.3) | Chromatic bound on η strips | Correct | r need not be a rectangle |
| B.2 end | Hole forces Hχ neither compact nor regular | Correct | Same repair as above |
| B.2 last sentence | "Nowhere locally finitely chromatic" on the support reduction | Unable to check | Reduction not defined in the packet |
| B.3 | Baire lemma; point-finite covers on hereditarily Baire spaces | Correct | Locally compact sober class subject to a standard import |
| B.3 | Cantor–Bendixson removal to the perfect kernel | Correct | T₁ hypothesis unnecessary (N7) |
| (C.1)–(C.2) | Rectangle lemmas; U and I products | Correct | |
| (C.3) | Point-free tube-cover identity | Correct subject to import | Needs only directed-join preservation of `π_*` |
| (C.4)–(C.5) | Compact fibre lower bound and W, W₂ transfer | Correct subject to (C.3) | |
| C.2, C.3 | Clopen chart gluing variants | Unable to check | No statement given |
| (C.6) | Span-density transfer | Correct | Two auxiliary facts made explicit below |
| (C.7) | Spatial separated base; lax fibre restriction | Correct | |
| C.3 end, G.3 | Σ(A)=Δ while W=W₂=U=A² | Correct subject to import | Arrieta Cor. 4.3, Prop. 4.4, Table 1 |
| (D.1) | D and D₂ multiply over an SDκ Boolean base | Correct | Sharpened in N5; hypothesis shown necessary in N4 |
| D application | σ-closed base times Arrieta's space | Correct subject to imports | Countable basis verified here, not in the source |
| E.1 | Bounded-lattice lower selection | Correct | Uses choice twice; h, k need only be lattice maps |
| E.2 | Coherent frame upgrade | Correct | |
| (F.1) | D₂(X)=D(X̂)∧X² | Correct | The cautioned exchange is in fact legitimate |
| (F.2)–(F.3) | Ghost-contact equivalence; localized simulation for every q | Correct | |
| G.1–G.3 | Fence, Scott and Arrieta controls | Correct | G.1 machine-checked |
| G.4 | Rank-one fixedness is not closed-hereditary | Correct subject to existence of Y | Explicit Y supplied in N6 |

## A. Definitions and the hole formulation

Section A is correct as written, including the first-step hole formulation and the separation of the weak defect `T_C` from the hole `E_C`.

- **Pre-nuclei.** `w_{C∧C'} ≤ w_C ∧ w_{C'}` for the meet-refinement, so the family of `w_C` is down-directed. Monotone, inflationary and finite-meet preserving follow. D and D₂ are the fixed-point sublocales, so `W=C(Φ^∞(0))` and `W₂=C(d)`.
- **(A.1).** `a⊠b ≤ w_C*` iff every c in C misses a or misses b, which splits C into two parts under `a*` and `b*`. The converse uses the binary cover `{a*,b*}`. Correct.
- **Density reading.** `O(w)∧C(d)` is dense in `C(d)` iff `w→d=d`. Hence Q′ fails iff some `E_C` is nonzero. Correct.
- **(A.5).** `cl T_C ≤ C(d∨w_C)`, whose relative interior in `↑d` is `O(w_C→d)`. Conversely `E_C∧O(w_C)=0`, so `D₂∧E_C ≤ T_C`, and `D₂∧E_C` is dense in `E_C`. The last step needs: a dense sublocale meets every open sublocale densely. That holds because `v*` lies in both `O(v)` and the Booleanization.

Two reformulations follow at once and are worth recording.

- Since B(D₂)=B(W₂) is the least dense sublocale of W₂, **Q′ holds for X iff `B(D₂(X)) ≤ D(X)`**. The generic finite-compatible pair is the only one that needs testing.
- `W ≤ W₂ ≤ U` always. So **`W=U` forces Q′**, and any Q′ counterexample has Φ-rank at least two: `Φ(z)>z`.

## B. Finiteization and frontiers

All displayed bounds in B are correct, and the only import, one-sided rigidity, is provable in a few lines. One closing sentence cannot be checked.

**B.1, local finiteness and compact remainder.** With `x=w_C→q`: `(v⊠1)∧(t_v⊠t_v)=0` because `v∧t_v=0`, and `x∧(c⊠c)≤q` for c in `F_v`. So (B.1) holds for every q. The formula for `ℓ_C` and the description of `H_C` are right. For (B.2), `x∧(ℓ_C⊠ℓ_C) ≤ Φ₂(q)` and `x∧(c⊠c)≤q`, giving `x ≤ Φ₂²(q)`. Correct.

**The rigidity import.** The compact case is immediate: a finite `F₀` with `e∨⋁F₀=1` gives a finite cover on which `h(e)=0` kills one term. The regular case is N1 and is true for every target frame. The deduction through the Booleanization of `E_C` is also sound: that Booleanization equals `E_C∧B(W₂)`, so it lies in D₂, and its first coordinate kills `ℓ_C`.

**Repair offered.** The Booleanization detour is unnecessary. N2 gives `w_C→q ≤ Φ₂²(q)` for every q when `H_C` is regular, by the same two-step computation as the compact case. Compact and regular are both instances of one condition, stated there.

**B.2, chromatic frontier.** If the classes `A_i` are independent then `r∧(⋁A_i⊠⋁A_i)≤d`, using the hypothesis `r∧w_C≤d` on the diagonal terms. The strip version with the co-tail `t_v` and the identification `v ≤ (⋁(C\A))*` iff `I_C(v)⊆A` are right, so (B.3) holds. Nothing uses that r is a rectangle. The compact and regular conclusions for Hχ follow as for `H_C`.

**Unable to check.** "On the canonical least-closed-coordinate-support reduction it must be nowhere locally finitely chromatic" has no definition behind it in the packet. Two points need fixing before it can be a statement. First, a pair lives on `K²` only if both endpoints factor through K, so the reduction must use `C(e_h∧e_k)`, on which h no longer reflects zero. Second, the graph Γ depends on r and d, and neither restricts canonically.

**B.3, Baire.** The sets `F_n` are closed, and the maximal-count argument yields an open set meeting finitely many members. The contradiction on `K_h` is valid: `h(t_F)=1`, `a∧t_F≤e_h`, so `h(a)=0`. Only the single closed set `K_h` needs to be Baire. Closed subspaces of locally compact sober spaces are again locally compact sober, so the hereditary claim reduces to the standard theorem that such spaces are Baire.

**B.3, Cantor–Bendixson.** The induction is correct at successors and limits. T₁ is not needed. On the piece where h is an ordinary point, the pair matches every cover with no closedness or compactness assumption (N7). So the result holds for every closed spatial support.

**What the frontier results say together.** For a finite-compatible pair with zero C-value and first support `K_h`: for every finite `F⊆C` and every t with `t∨⋁F=1`, `h(t)=1`. So every neighbourhood of the closed set `K_h \ ⋁F` is dense in `K_h`. Non-compactness, non-regularity and the absence of locally finite patches are all special cases of this one line.

## C. Products and closed-hull transfer

Every displayed identity in C is correct. (C.3) needs one import, and (C.6) silently uses two classical facts that should be stated.

**C.1.** (C.1) holds because a rectangle `u⊠v` is zero iff u or v is zero, and pseudocomplements are joins of disjoint rectangles. The lemma "`(s⊠1)∨(1⊠t)=1` forces s=1 or t=1" is correct. For U, the inclusion `z_X ≤ (z_Z⊠1)∨(1⊠z_Y)` follows as written. The reverse holds because `u⊠1` and `v⊠1` are far whenever u and v are. For I, the diagonal of a product is the product of diagonals because diagonal maps are embeddings. The closure formula `cl(A×B)=cl A×cl B` holds because a product of dense maps is dense.

**C.2, tube identity.** The finite reduction is correct and needs no compactness: for finite F and any Y,

\[
\pi_*\Big(\bigvee_{i\in F}u_i\boxtimes v_i\Big)=\bigvee_{J\subseteq F,\ \bigvee_J v_j=1}\ \bigwedge_{j\in J}u_j .
\]

Proof of the non-trivial inclusion: on a nonzero locally closed piece where the right side vanishes, pick J maximal with `m=⋀_J u_j ≠ 0`. Then `m⊠1 ≤ m⊠⋁_J v_j` with `⋁_J v_j ≠ 1`, which is impossible. Compactness of Y enters only through preservation of directed joins by `π_*`. Beck–Chevalley is not needed.

**(C.4)–(C.5).** Pulling `w_R` back to `Z×D(Y)` gives at least `(⋀_F u_i)⊠1` on each good F, since D(Y) matches the finite cover `{v_i : i∈F}`. Joining over F gives 1 by (C.3). The upper bound uses `D_ε(Z×Y) ≤ D_ε(Z)×D_ε(Y)`, which is legitimate: preimage of sublocales is a right adjoint and preserves all meets. (C.5) follows.

**(C.6).** Correct. Two facts carry the density step and should be cited explicitly. First, `Z×T → Z×Im(f,g)` is dense, although it need not be a surjection. Second, `1⊠(−)` preserves arbitrary meets because projections are open classically. Together they give `cl(⋁ lifted images)=I(Z)×cl Σ(Y)`.

**(C.7).** Correct. Spatiality of Z makes the discrete cover `Z_disc → Z` an epimorphism, so `Z_disc×S → Z×S` is dense and the slices have dense join. "Nonempty" is needed only for reflection, not for the formula. The lax fibre statement is right: a rectangle `(u⊠u)⊠r` inside the hole pulls back along every slice at `z∈u` to the common Y-hole r.

**Unable to check.** The clopen-chart gluing in C.2 and the clopen-cover variant in C.3 are named but not stated.

**No-go.** `Σ(A)=Δ_A` follows from strong Hausdorffness via total unorderedness. The three equalities `U(A)=W(A)=W₂(A)=A²` need only `z_A=0`, by (A.1). No relation computation is required.

**Redundancy.** E.2 shows `cl Σ(Y)=W₂(Y)` for coherent Y, so (C.6) applies there. Coherent locales are compact, so (C.5) already covers that case.

## D. Strongly distributive Boolean base

(D.1) is correct for arbitrary covers of unbounded cardinality, and it is a statement about the non-closed sublocales D and D₂. The proof was checked step by step.

1. **Coefficient expansion.** `c=⋁_i u_{c,i}⊠b_i` holds: any rectangle `m⊠b≤c` splits over basic `b_i≤b`, and `u_{c,i}⊠b_i≤c` because `⊠` preserves joins in each variable.
2. **Partition `P_i`.** The elements lying under `¬u_i` or under some `u_{c,i}` are dense in M and down-closed. A maximal antichain among them is a partition of 1. This uses Zorn and a choice of labels.
3. **Common refinement.** SDκ is applied to the family `(P_i)`, which has at most κ members of arbitrary width. Each cell m lies under one cell of each `P_i`.
4. **Fibre cover.** For i outside `J_m`, `m∧u_{c,i}=0` for all c. So `(m⊠1)∧c ≤ m⊠⋁_{J_m} b_i`, and covering forces `⋁_{J_m} b_i=1`. Then `{v_{c,m}}` covers Y with `m⊠v_{c,m}≤c`.
5. **Finite covers.** The family `{v_{c,m}}` is indexed by C. It is finite when C is, whatever the size of the basis.
6. **Lower inclusion.** The pullback of `w_C` to `Z×D_ε(Y)` dominates `⋁_m m⊠1=1`.
7. **Upper inclusion.** Naturality gives `D_ε(Z×Y)≤D_ε(Z)×D_ε(Y)`. For Boolean Z the binary covers `{m,¬m}` already force the two projections to agree, so `D₂(Z)=D(Z)=Δ_Z`.

**Consequences.** Boolean locales have closed diagonal and `z_Z=d_Z`, so `I(Z)=U(Z)=Δ_Z`. Hence W, W₂ and U multiply as claimed.

**Hypotheses that are not necessary.**

- For the D₂ half, each `P_i` can be taken finite with no choice. Then (κ,2)-distributivity suffices (N5).
- For the D half with an Alexandrov fibre, no hypothesis on Z is needed (N5).
- For the closed-level conclusion with an anti-Urysohn fibre, no distributivity and no basis bound is needed (N3).

**The hypothesis is not removable.** For the Cohen base, `D₂(B×S)` is strictly below `Δ_B×D₂(S)` with S second countable (N4). This is consistent with (D.1) and shows that the packet's caution about the Cohen base is warranted at the D₂ level.

**Application.** The σ-closed forcing `Fn(ω₁,2,ω₁)` is separative and atomless, and its completion is (ω,∞)-distributive. That matches SDω as defined. Arrieta's space has a countable basis (shown under G.3 below). So `Z×A` has `W=W₂=U=Δ_Z×A²`, has no points, and has `Σ=Δ` because a product of strongly Hausdorff locales is strongly Hausdorff. The example stands. By N3 the same conclusion holds for every Boolean Z, so the example does not in fact need (D.1).

**Cohen test.** `W(B×A)=W₂(B×A)=U(B×A)=Δ_B×A²` by N3. Whether `D(B×A)=Δ_B×D(A)` remains open.

## E. Boolean finite selection and the coherent upgrade

Both claims are correct. Finite-cover compatibility does force a continuous Stonean selection of prime filters for an arbitrary frame L, and (E.2) is a legitimate frame extension.

**E.1, step by step.**

- `H(s)=h⁻¹(s)` is a prime filter of the lattice L for each ultrafilter s, and H is patch-continuous because preimages of the subbasic clopens `{P : a∈P}` are the clopens of `h(a)`.
- `G_s=H(s)∩K(s)` is a filter meeting every finite cover: the join in (E.1) lies in s, and s is prime.
- The ideal generated by `L \ G_s` is proper exactly because no finite join of non-members is 1. A prime ideal containing it has complement a prime filter `P_s ⊆ G_s`.
- R is closed: failure of `P ⊆ H(s)∩K(s)` is witnessed by one a, an open condition in the patch topology. R maps onto S by the previous step.
- S is extremally disconnected because M is complete. Gleason projectivity gives a continuous section, and `p_fin(a)={s : a∈P_s}` is clopen. Primeness of each `P_s` makes `p_fin` a bounded lattice homomorphism below h and k.

**Where each hypothesis enters.** Completeness of M is used only for extremal disconnectedness. Choice is used twice, in the prime ideal theorem and in Gleason's theorem. Nothing uses that L is a frame or that h and k preserve infinite joins. The claim holds for bounded distributive lattices and lattice maps.

**Infinite joins.** The stated obstruction is correct and unavoidable: zero matching value on C forces `p_fin(c)=0` for all c while `p_fin(1)=1`.

**E.2.** The restriction to K(L) satisfies the hypothesis because finite covers by compact elements are finite covers. `L≅Idl(K(L))` is the free frame on the lattice K(L), so (E.2) is the unique frame extension, and `p(a) ≤ ⋁_{c≤a} h(c)=h(a)`. Coherence is used only here.

**Remark.** For coherent L, matching of all covers is already automatic by compactness. The content of E.2 is the frame-map predecessor itself, that is, `B(D(X)) ≤ Σ(X)`.

## F. Coherent envelope and contact cores

F.1 to F.3 are correct, and (F.3) holds for every q, not only at rank one.

**F.1.** ε preserves arbitrary joins because the join of ideals is generated by their union. It preserves binary meets because `x∧y` lies in `J∩J'` for x in J and y in J'. The adjunction `ε(J)≤a iff J⊆↓a` is right, and j is a lattice map only. Finite covers pass in both directions as stated.

**(F.1).** Correct as an equality of sublocales. The packet's caution here is stricter than necessary. Preimage along a localic map is right adjoint to image, so it preserves arbitrary meets of sublocales. Directly:

\[
(i\times i)^{-1}\big[D(\widehat X)\big]=\bigwedge_{\widehat F\ \mathrm{finite}}O\big(w_{\varepsilon\widehat F}\big)=D_2(X).
\]

What genuinely fails is the exchange of closure with restriction, as the packet says for W₂.

**Ghost remainder.** `R_C` is nonzero iff C has no finite subcover, and `R_C∧X=0` because `ε(û_C)=1`. The extension `p̂` is a frame map and lands in `R_C` when `p_fin` kills C.

**(F.2).** `(j(a))*=j(a*)` is correct, so `G_C(a,b)` is the closed sublocale of the ideal generated by `a*`, `b*` and C. It is nonzero iff that ideal is proper. Correct.

**(F.3).** With `H={a*,b*}∪F`: the two starred squares meet `a⊠b` in zero, and each F-square meets x inside q. So `x ≤ w_H→q`. No property of q is used.

**Scope of the obstruction.** "Noncompact contact core and `G_C>0`" is necessary for a rectangle inside a Q-hole and is far from sufficient. In G.1 the cover C is a partition, hence locally finite, so (B.1) alone removes any hole while `G_C>0` persists.

**Terminology.** "U-linked" is used but never defined. From G.1 it must mean `a⊠b ≰ z`. This is weaker than "a and b are not far", because a rectangle can lie under z without being a far rectangle.

## G. Countercontrols

All four controls compute as claimed. Two of them are simpler than the packet suggests, and G.3 needs its sourcing corrected.

**G.1, fence.** Recomputed by hand and by machine. `↑0={0,5}`, `↑4={4}`, closures `{0,1,5}` and `{1,2,4}`, core `{1}`. In an Alexandrov space, `(x,y)∈U` iff some `x'≥x` and `y'≥y` have a common lower bound. Here 5 and 4 share the lower bound 1, so `(0,4)∈U`; 0 and 4 have no common upper bound, so `(0,4)∉I`. For `X=B×P`, (C.5) applies since `W₂(B)=I(B)=Δ_B`, and (C.2) gives U. `K(a,b)=B×{1}`, and `(1⊠(P\{1}))∨(⋁_F v_i⊠1)=1` only if `⋁_F v_i=1`, which fails for finite F. So `G_C(a,b)>0` with no hole. Correct.

**G.2, Scott space.** `O(S)` is the frame of upper sets of nonempty finite subsets of ω. Equivalently it is presented by generators `c_n` with the single relation `⋁c_n=1`. So frame maps out of `O(S)` are exactly sequences with join 1, and h and k exist because `⋁_n[x_n=0]` and `⋁_n[x_n=1]` are dense open. Every finite cover induces a finite partition of ω by which member contains each `c_n`. An infinite block N gives `h(⋁_N c_n)=k(⋁_N c_n)=1`. So the pair is finite-compatible with zero C-value. S is hyperconnected, so `z=0` and `W=W₂=U=S²` by (A.1). Correct.

One structural fact is worth adding. As a locale S is Alexandrov, with minimal cover C. So `D(S)=O(w_C)` is open, and the defect is exactly `D₂(S)∧C(w_C)`. More generally every Alexandrov locale has `W=U` (N7), so no Alexandrov locale can test Q or Q′.

**G.3, Arrieta.** The space is Example 4.5: Construction 4.2 applied to the Cantor cube with `K_n = {a : a_n=1, a_m=0 for m>n}`.

| Property used in the packet | Status in the paper |
| --- | --- |
| Strongly Hausdorff | Proved: Corollary 4.3 |
| Anti-Urysohn, i.e. `z_A=0` | Proved: Proposition 4.4, with Definition 4.6 |
| `Σ(A)=Δ_A` | Follows: strong Hausdorff implies totally unordered (Table 1) |
| `W=W₂=U=A²` | Not in the paper. Follows from `z_A=0` and (A.1) |
| Countable basis | Not stated in the paper. True, by the argument below |
| Noncompact | Not stated. True: compact Hausdorff locales are regular, hence Urysohn |

Countable basis: let 𝔅 be a countable base of the Cantor cube closed under finite unions. Each `K_n` is compact, so every open `U⊇K_n` contains some `B∈𝔅` with `K_n⊆B`. Hence `{B∩Y}` together with `{(B∩Y)∪{n} : K_n⊆B}` is a countable base of the topology (1) of Construction 4.2.

**G.4.** The construction is correct. Adjoining a generic point to a sober Y gives a sober hyperconnected X with `z_X=0`, so `Φ₂(z_X)=z_X`, while Y is closed in X. The packet does not define the "compact sober two-apex space" with `W₂(Y)<U(Y)`. Such a space exists; N6 gives one that is also T₁. Finite spaces cannot serve, since they always have `W=U`.

## New results from the audit

Seven statements arose while checking the packet. Each has a complete proof here and was re-derived a second time before this report was closed. They have had no independent review and no novelty is claimed.

### N1. One-sided regular rigidity

**Statement.** Let L be a frame and `e∈L` with `↑e` regular. Let M be any frame and `h,k:L→M` frame maps with `h(e)=0`. Suppose `h(y)∧k(y) ∨ h(c)∧k(c) = 1` for every binary cover `{y,c}` of L. Then `h ≤ k` pointwise. Consequently `⋁_{c∈C} h(c)∧k(c)=1` for every cover C.

**Proof.** Fix c. By regularity, `c∨e` is the join of those `s≥e` for which some `t≥e` has `s∧t=e` and `t∨c∨e=1`. Since `t≥e`, already `t∨c=1`. Meet the cover identity for `{t,c}` with `h(s)`:

\[
h(s)\ \le\ h(s\wedge t)\ \vee\ k(c)\ =\ h(e)\vee k(c)\ =\ k(c).
\]

Joining over s gives `h(c)=h(c∨e) ≤ k(c)`. Then `⋁ h(c)∧k(c)=⋁ h(c)=1`. ∎

Only binary covers are used, and M need not be Boolean.

### N2. One remainder criterion covering compact and regular

**Statement.** Let C be a cover, `q∈P`, `x=w_C→q`, and `ℓ∈L` with `x∧(ℓ⊠1) ≤ Φ₂(q)`. Call s *tame* if there are `t∈L` and a finite `F⊆C` with `s∧t ≤ ℓ` and `t∨⋁F=1`. If the tame elements join to 1, then `x ≤ Φ₂²(q)`.

**Proof.** For tame s put `G={t}∪F`, a finite cover. Then `x∧(s⊠1)∧(t⊠t) ≤ x∧(ℓ⊠1) ≤ Φ₂(q)` and `x∧(c⊠c) ≤ q` for c in F. So `x∧(s⊠1) ≤ w_G→Φ₂(q) ≤ Φ₂²(q)`. Join over s. ∎

**Instances.** Take `ℓ=ℓ_C`. If `C(ℓ)` is compact, `s=1` and `t=ℓ` are tame: this is (B.2). If `C(ℓ)` is regular, each `c∨ℓ` is a join of tame s with `F={c}`. If `C(ℓ)` is covered by opens with compact closure, `t=s→ℓ` works. The same proof with r for x, d for q and `ℓ=η_{C,r}` gives the chromatic versions. For Φ₂-fixed d the conclusion is `w_C→d=d`.

### N3. Boolean-base splitting lemma

**Statement.** Let Z be a Boolean locale with frame M, Y any locale, `X=Z×Y`, and `d_M=⋁{p⊠p' : p∧p'=0}`. Then

\[
\Phi_X(d_M\boxtimes 1)\;=\;z_X\;=\;(d_M\boxtimes 1)\vee(1\boxtimes z_Y).
\]

**Corollary.** If Y is anti-Urysohn (`z_Y=0`), then `z_X` is Φ-fixed and `W(X)=W₂(X)=U(X)=Δ_Z×Y²`. No distributivity of M and no basis of Y is assumed. In particular this holds for `B×A` with B the Cohen locale.

**Proof.** The second equality is (C.2) with `z_Z=d_M`. Since `d_M⊠1 ≤ z_X=Φ(0)`, only `w_C→(d_M⊠1) ≤ z_X` needs proof, for a cover C of X. Take a rectangle `(m₁⊠a)⊠(m₂⊠b)` under the left side. Splitting `m₁` and `m₂` along `m=m₁∧m₂` writes it as a join of four rectangles. Three have disjoint Z-coordinates and lie under `d_M⊠1`. The fourth is `a'⊠b'` with `a'=m⊠a`, `b'=m⊠b`; assume m, a, b nonzero.

Let `π_!` be the left adjoint of `u ↦ u⊠1`, so `π_!(w)=⋁{p : p⊠y ≤ w for some y≠0}`. Put `α_c=π_!(c∧a')` and `β_c=π_!(c∧b')` for c in C. If `p⊠y ≤ c∧a'` and `p'⊠y' ≤ c∧b'` with y, y' nonzero, then `(p⊠p')⊠(y⊠y') ≤ (a'⊠b')∧(c⊠c) ≤ d_M⊠1`. Restricting to the diagonal of Z gives `p∧p'=0`. Hence `α_c∧β_c=0`.

Now refine C to `C'={c∧(α_c⊠1), c∧(¬α_c⊠1) : c∈C}`, a cover because M is Boolean. By Frobenius, `π_!(c∧(α_c⊠1)∧b')=α_c∧β_c=0` and `π_!(c∧(¬α_c⊠1)∧a')=¬α_c∧α_c=0`. So every member of C' misses `a'` or misses `b'`. Therefore `a'*∨b'*=1`, the rectangle is far, and it lies under `z_X`. ∎

### N4. Cohen base times Scott fibre: D₂ does not multiply

**Statement.** Let B be the Cohen locale with frame `RO(2^ω)` and S the Scott space of G.2. Then `D₂(B×S)` is strictly smaller than `Δ_B×D₂(S)`. S has a countable basis, so the distributivity hypothesis of (D.1) cannot be dropped for D₂.

**Construction.** Take the binary cover `C={c⁰,c¹}` of `B×S` with `c^e=⋁_n [x_n=e]⊠c_n`. It covers because `[x_n=0]∨[x_n=1]=1` and `⋁c_n=1`. Let T be the locale with frame `RO(2^ω×2^ω)`, coordinates (x,y), and `b:T→B` the first projection. For n in ω write `i(n,x)` for the number of `j<n` with `x_j=1`, and `i'(n,x)` for the number with `x_j=0`. Define clopen sets

\[
H_n=\{x_n=1,\ y_{2i(n,x)}=1\},\qquad K_n=\{x_n=0,\ y_{2i'(n,x)+1}=1\}.
\]

Set `h(c_n)=H_n` and `k(c_n)=K_n`. For every infinite `N⊆ω` the unions `⋃_{n∈N}H_n` and `⋃_{n∈N}K_n` are dense. Given finite prefixes of x and y, extend x by enough ones (or zeros) up to some n in N, then set the one free y-coordinate. So h and k are frame maps on `O(S)`.

**Proof.** Every finite cover of S has a member containing `c_n` for all n in some infinite N, so h and k are finite-compatible and `(h,k)` lands in `D₂(S)`. Hence `(b,h,k)` maps T into `Δ_B×D₂(S)`. Its two components into `B×S` are `f=(b,h)` and `g=(b,k)`. Since `H_n≤[x_n=1]` and `K_n≤[x_n=0]`, we get `f*(c⁰)=0` and `g*(c¹)=0`. The matching value of C is `f*(c⁰)∧g*(c⁰) ∨ f*(c¹)∧g*(c¹)=0`, and T is nontrivial. So `Δ_B×D₂(S)` is not below `O(w_C)`, while `D₂(B×S)` is. ∎

**Reading.** Fibrewise, C is the two-colouring of `{c_n}` by a generic real. No ground-model finite partition refines it. By N3 the closed hulls still agree: `W₂(B×S)=Δ_B×S²`. By N5(b) the full fittings also agree: `D(B×S)=Δ_B×D(S)`. The failure is confined to the non-closed finite fitting.

### N5. Two sharpenings of (D.1)

**(a) The D₂ half needs only (κ,2)-distributivity.** For a finite cover `C={c₁,…,c_r}` and fixed i, take the cells `¬u_i`, `u_{c₁,i}`, `u_{c₂,i}∧¬u_{c₁,i}`, and so on. This is a finite labelled partition, chosen without Zorn. A common refinement of κ finite partitions exists under (κ,2)-distributivity, since each finite partition is the common refinement of finitely many binary ones. The rest of the packet's proof is unchanged.

**(b) With an Alexandrov fibre the D half needs nothing.** Let `O(Y)` be the upper sets of a poset Q and Z any locale. For t in Q the slice `s_t:Z→Z×Y` gives `s_t*(c)=u_{c,t}:=⋁{m : m⊠↑t ≤ c}`. So `⋁_c u_{c,t}=1` for every cover C. The pullback of `w_C` to `Z×D(Y)` is at least `⋁_t 1⊠ι*(↑t⊠↑t)=1`, because `D(Y)=O(w₀)` for the minimal cover. Hence `Δ_Z×D(Y) ≤ D(Z×Y)` for every Z, with equality when `D(Z)=Δ_Z`.

### N6. An explicit two-apex space for G.4

**Space.** Y has points a, b, t and isolated points `x_n`, `y_n`. Basic neighbourhoods are `A_N={a}∪{x_n : n≥N}`, `B_N={b}∪{y_n : n≥N}` and `T_N={t}∪{x_n,y_n : n≥N}`.

**Properties.** Y is compact, T₁, sober and locally compact, so `Y²` is spatial. The closures of `A_N` and `B_M` both contain t, so `(a,b)∈U`. Every other point of `A₀×B₀` has coordinates admitting neighbourhoods with disjoint closures, so `(A₀×B₀) \ z={(a,b)}`. No member of the finite cover C, namely `{A₀,B₀,T₀}`, contains both a and b. Hence `A₀×B₀ ≤ w_C→z` and `(a,b)∈Φ₂(z) \ z`. So `W(Y)=W₂(Y)<U(Y)`.

### N7. Two small rigidity facts

**(a) Ordinary points are rigid.** Let `(h,k)` be finite-compatible and let h be the ordinary point x on a piece m of M. For a cover C put `A=⋁{c : x∈c}` and `B=⋁{c : x∉c}`. Then `h(B)=0` on m, so the binary cover `{A,B}` gives `k(A)≥m`. Since `h(c)≥m` for each c containing x, the pair matches C on m. No closedness, compactness or T₁ is used. In particular D and D₂ have the same points.

**(b) Alexandrov locales have W=U.** If `O(X)` is the frame of upper sets of a poset, the cover `C₀={↑t}` refines every cover. So `Φ(q)=w_{C₀}→q` is a nucleus and `Φ(z)=Φ(Φ(0))=z`. This covers all finite spaces and the Scott space S.

## Imported inputs

Seven outside facts are used beyond the standing classical assumption; one-sided rigidity is no longer among them. The exact form needed is given so that each can be checked against its source.

| Used in | Input, in the form needed | Status |
| --- | --- | --- |
| (A.1), (C.1), D, N3 | In a frame coproduct, `u⊠v=0` iff u=0 or v=0 | Classical; fails constructively |
| (C.3) | For compact Y, `π_*:O(Z×Y)→O(Z)` preserves directed joins | Standard (proper maps are pullback-stable); from memory |
| (C.5), (F.1), D | Preimage of sublocales is right adjoint to image, so it preserves all meets | Standard; from memory |
| (C.6) | Product projections are open, so `1⊠(−)` preserves all meets | Classical |
| E.1 | Prime ideal theorem; Gleason: extremally disconnected compact Hausdorff spaces are projective | Standard; both need choice |
| B.3 class | Locally compact sober spaces are Baire | Standard (continuous-lattice literature); from memory |
| D application | A σ-closed forcing has (ω,∞)-distributive completion | Standard forcing theory; from memory |
| G.3, C.3 no-go | Arrieta, Cor. 4.3, Prop. 4.4, Def. 4.6, Table 1 | Opened and checked in the arXiv version |

The first row is counted with the packet's standing classical assumption, not as a separate import.

## Closing lists

### (a) Defects and proof obligations, in priority order

None of these is an error in a displayed theorem. They are statement gaps, sourcing errors and avoidable imports.

1. **Define or delete the support-reduction sentence** at the end of B.2, and the matching last sentence of G.4. State which closed sublocale is meant, for which endpoint, and how Γ restricts.
2. **State the two clopen-gluing variants** in C.2 and C.3, or remove them.
3. **Correct the Arrieta sourcing.** Cite Cor. 4.3 and Prop. 4.4 for what the paper proves. Prove the countable basis in the text. Derive `W=W₂=U=A²` from (A.1), not from a "relation computation".
4. **Define the two-apex space** of G.4, or adopt N6.
5. **Replace the rigidity import** by N1 and N2, and drop the Booleanization from the regular case.
6. **Restate (D.1)** with the weaker D₂ hypothesis, add N4 as the sharpness control, and update the Cohen test to "closed level settled, D level open".
7. **Name the real import in (C.3)** as directed-join preservation, drop Beck–Chevalley, and state the two density facts behind (C.6).
8. **Minor.** Remove T₁ from the Cantor–Bendixson claim. Define "U-linked". Relax the caution in F.1 about meets and preimages.
9. **Obligation on this report.** N1 to N7 have had no second reader. N3 and N4 carry the most weight and should be checked first.

### (b) Usability

| Class | Results |
| --- | --- |
| Usable now | (A.1)–(A.5); (B.1)–(B.3) with their compact and regular corollaries; Baire and Cantor–Bendixson claims for the stated supports; (C.1), (C.2), (C.6), (C.7); (D.1); E.1, E.2; (F.1)–(F.3); G.1, G.2 |
| Conditionally usable | (C.3)–(C.5), on the properness theorem; the locally compact sober metacompact class, on the Baire theorem; G.3 and the D application, on Arrieta's paper as read in its arXiv version; G.4, on N6 or the packet's own Y; N1–N7, pending a second check |
| Not yet usable | The support-reduction sentence of B.2; both clopen-gluing variants; any D-level statement over the Cohen base |

### (c) What to attack next

**First choice: test Q′ at Φ-rank two on non-compact relatives of N6.** This is a judgment, not a deduction. Three observations from the audit support it.

- Every control in the packet has `W=U` for a trivial reason: `z=0`, an Alexandrov frame, or a product with such a factor. Q′ is automatic whenever `W=U`. So Q′ has not yet been tested on any locale where it has content.
- N6 is a small space with `Φ(z)>z`, but it is compact. The cheapest informative experiment replaces its three neighbourhood filters by infinitely many, so that the separating cover becomes infinite with dense tails.
- The support-density line in section B says exactly what such a space must achieve: every neighbourhood of `K \ ⋁F` dense in the support K, for every finite `F⊆C`. That is a design target for a counterexample, and a checklist for a proof.

Either a hole appears, or the reason it cannot will be the missing lemma. One caution: outside the locally compact case the localic square need not be spatial, so point-set computations of W₂ must be justified separately.

**Second choice: decide whether `D(B×A)=Δ_B×D(A)`.** N3 and N4 leave this as the only open part of the Cohen test. It is a well-posed question about one cover-refinement property and does not depend on Q.

**Formulation to carry forward.** Q′ for X is equivalent to `B(D₂(X)) ≤ D(X)`. Arrieta's space shows that frame-map predecessor selection cannot prove this in general, since there `Σ=Δ` while `B(D₂)` is dense in `A²`. Any proof must therefore work with matching values directly, as N1 to N3 do.

## Sources

- I. Arrieta, [Localic separation and the duality between closedness and fittedness](https://arxiv.org/pdf/2310.18522), arXiv:2310.18522v1. Section 4 read: Construction 4.2, Corollary 4.3, Proposition 4.4, Example 4.5, Definition 4.6, Table 1.
- Publication record for the same paper: [Topology and its Applications 342 (2024), article 108785](https://research.birmingham.ac.uk/en/publications/localic-separation-and-the-duality-between-closedness-and-fittedn).
- Blind bundle `ProjectA_Q_Session8_EXTERNAL_BLIND_2026-11-12.zip`: `BLIND_REFEREE_PROMPT.md` and `BLIND_MATHEMATICAL_PACKET.md`.

The repository notes listed in section H of the packet were not opened. Textbook theorems in the Imported inputs table are cited from memory without a page reference.
