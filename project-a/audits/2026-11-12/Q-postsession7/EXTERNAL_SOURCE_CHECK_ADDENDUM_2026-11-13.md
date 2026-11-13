# Referee report — source-check addendum, 13 November 2026

Addendum to the blind referee report of 12 November on `ProjectA_Q_Session8_EXTERNAL_BLIND_2026-11-12`.
The blind verdicts were recorded before any repository note was opened. This addendum records what
changed once `mkkinyon/locales` was readable (commit `17a679f`, 12 Nov 2026).

**Result.** All three items the blind report marked "unable to check" or "undefined" are correct as
stated in the repository notes. No blind verdict is reversed. The packet now stands at 26 of 26 claim
groups correct, four of them subject to a named import. One audit result (N3) answers a question the
repository lists as open.

## 1. Items resolved against the notes

| Item | Note and place | Outcome |
| --- | --- | --- |
| B.2 last sentence: support reduction, "nowhere locally finitely chromatic" | Q′ pre-nucleus note §2–§3; chromatic note §5 | **Correct.** |
| G.4 last sentence: marked hole persists on the support | Q′ pre-nucleus note, Theorem 3.1 | **Correct.** |
| C.2 variant: compact clopen fibre charts | Point-free products note, Lemma 4.1, Theorem 4.2 | **Correct.** |
| C.3 variant: clopen-trivial bundles | Separated-factor note, Lemmas 6.1–6.2, Theorem 6.3, Corollary 6.4 | **Correct.** |
| G.4: the "two-apex space" | Two-apex note §2; marked-Urysohn note §3 | **Defined and verified.** |
| B.1/B.2: one-sided compact/regular rigidity | Frontier note, Theorem 1.1 | **Correct.** Same argument as N1. |
| D application: countable basis of Arrieta's space | Boolean-base note §3 | **Present**, same compactness argument as in the report. |

### 1.1 Support reduction (B.2, G.4)

The two objections in the blind report are both answered by the notes.

- *Which support.* The notes use `K_E = C(e_E)` with `e_E = ⋁{a : h(a)=k(a)=0}`, the largest open killed by
  **both** coordinates of `B(E)`. Equivalently `e_E = p₁*(ρ→d₀) ∧ p₂*(ρ→d₀)`; the equivalence uses only
  density of `B(E)` in `E`. Then `E ≤ K_E²` because `K_E²` is closed and contains the dense `B(E)`.
- *Zero reflection.* Joint reflection (`h(v)∨k(v)≠0` for `v≠0_K`) is immediate. Separate reflection also
  holds: `d₀` and `w_C` are swap-symmetric, so `E` is, so `k = α∘h` for an automorphism α of `O(B(E))`, and
  the two zero ideals coincide.
- *Which graph.* §5 of the chromatic note defines `Γ_E` from `E` itself (`c ~ c'` iff `E` meets
  `(c⊠c')∨(c'⊠c)`), not from a chosen `r` and `d`. That restricts to `K_E` with no ambiguity. For
  `r = w_C→d` it agrees with the packet's `Γ_r`.

Checked: Proposition 2.1; closed heredity `D_ε(K) = D_ε(X) ∧ K²`; Theorem 3.1, i.e. `W₂(K) ∧ O(ρ_K) = E`,
`W(K) ∧ E = 0`, `Φ_K(d_{W₂(K)}) > d_{W₂(K)}`; and (5.1)–(5.5) of the chromatic note. In (5.3) the local
colouring argument is run inside `K` against the Φ₂-fixed `d_{W₂(K)}`, so no inheritance of the rank-one
hypothesis is needed. The notes say so explicitly and that caution is right.

**What the packet should add:** the definition of `K_E`, the symmetry remark, and the definition of `Γ_E`.
Without them the sentence cannot be refereed.

### 1.2 Clopen variants (C.2, C.3)

- **Theorem 4.2, products note.** Lemma 4.1 is right: for complemented `e`, the rectangles `e⊠e*` and
  `e*⊠e` are far, so the two coordinates agree on `e` over `U(Y)`, and the squares `e_i⊠e_i` cover `U(Y)`.
  The chart identities use closed heredity of `D_ε` plus "closure commutes with open restriction", both
  valid. The gluing step is valid: if `R=C(r)` and `S=C(s)` lie under `C(u)`, opens `o_i` satisfy
  `u∨⋁o_i=1`, and `o_i→r = o_i→s` for all i, then `r = ⋀_i(o_i→r) = ⋀_i(o_i→s) = s`.
- **The side remark `D(Y)=D₂(Y)`** for a compact-clopen cover is correct. It is the instance `s=e_i`,
  `t=e_i*`, `F=F_i` of the audit's criterion N2.
- **Theorem 6.3 and Corollary 6.4, separated-factor note.** Lemma 6.1 is right for all four relations,
  including `U`: far pairs in a clopen `J=O(e)` extend to far pairs in `X` because `a*∨b* ≥ e∨e* = 1`.
  Lemma 6.2 is the same gluing argument on `F=(p×p)⁻¹Δ_Z`. The chartwise formula uses (C.7), whose
  hypotheses hold on each clopen `O(e_i)`. The zero-dimensional refinement in Corollary 6.4 is valid. The
  warning about vacuous Q on bundles with varying fibres is apt.

### 1.3 Two-apex space

The notes define `Y = ℝ ∪ {p,q}`: ℝ with its usual topology; neighbourhoods of `p` contain `p` and all but
finitely many positive reals; `q` likewise on the negative side. It is compact, T₁, sober and locally
compact, so `Y²` is spatial.

Direct check of `W₂(Y) < U(Y)`. Put `u₊=(0,∞)∪{p}`, `u₋=(−∞,0)∪{q}`. Every nonempty open set of positive
reals has `p` in its closure, and likewise `q` on the negative side. So every point of `u₊×u₋` other than
`(p,q)` has neighbourhoods with disjoint closures, while closures of neighbourhoods of `p` and `q` meet at
0. The finite cover `{u₊, u₋, (−1,1)}` has no member containing both `p` and `q`. Hence
`(p,q) ∈ Φ₂(z) \ z`. G.4 is therefore correct without qualification. The audit's N6 remains a valid,
smaller alternative.

## 2. Overlap between the audit's own results and the repository

| Audit result | Status against the notes |
| --- | --- |
| N1, one-sided regular rigidity | **Not new.** Reproduces the frontier note's Theorem 1.1, including `h ≤ k`. Independent confirmation only. |
| N2, tame-element criterion | **Partly new.** Overlaps with the rather-below patch `t_C` (Q′ pre-nucleus note, Theorem 4.1 and (4.2)). Adds the bound `w_C→q ≤ Φ₂²(q)` for every q when `H_C` is regular; the notes prove that bound only for compact `H_C` and use Booleanization for the regular case. |
| N3, Boolean-base splitting lemma | **Answers an open item.** See §3. |
| N4, Cohen × Scott, `D₂` not multiplicative | No counterpart found in the notes read. |
| N5, (κ,2)-distributivity for the `D₂` half; Alexandrov fibre | No counterpart found. The Boolean-base note deliberately states SDω and declines (ω,2); N5(a) shows (ω,2) is enough for `D₂` only. |
| N6, countable two-apex space | Alternative to the notes' example. |
| N7(a), ordinary points are rigid | **Not new.** The Q′ pre-nucleus note §1 already uses equality of the point sets of `D` and `D₂`. The audit only adds its use to drop T₁ from the Cantor–Bendixson claim. |
| N7(b), Alexandrov locales have `W=U` | No counterpart found in the notes read. |

## 3. N3 against the repository's "next concrete test"

The Boolean-base note ends by asking whether `Φ₂(d_U) = d_U` on `Z_C × A`, with `Z_C` the Cohen locale,
`A` Arrieta's space and `d_U = d_{Δ}⊠1`. The two-apex note (4.4) poses the same target and says neither
`W=W₂` nor `W₂=U` is known there.

N3 states that for **every** Boolean `Z` and every locale `Y`,

    Φ_{Z×Y}(d_Z ⊠ 1) = z_{Z×Y} = (d_Z ⊠ 1) ∨ (1 ⊠ z_Y).

With `z_A = 0` this gives `Φ(d_U) = d_U`, hence also `Φ₂(d_U) = d_U`, and

    W(Z_C × A) = W₂(Z_C × A) = U(Z_C × A) = Δ × A².

So, if N3 stands, `Z_C × A` is Q-positive and Q′-positive. It is neither a Q counterexample nor a new
`W₂<U` control. The mechanism is neither tube covers nor spans: it is that a Boolean base lets any cover
be split along a complemented base open, combined with the universal `U` product formula (C.2).

The proof was re-derived a second time in coefficient form after reading the notes:

1. Reduce to a rectangle `(m⊠a)⊠(m⊠b)` with `m, a, b ≠ 0` whose meet with `w_C` lies under `d_Z⊠1`.
2. For `c ∈ C` let `α_c` be the join of `m∧m_j` over rectangles `m_j⊠a_j ≤ c` with `a_j∧a ≠ 0`, and `β_c`
   the same with `b`. The hypothesis gives `α_c ∧ β_c = 0`.
3. `C' = {c∧(α_c⊠1), c∧(¬α_c⊠1)}` is a cover. The first kind of member misses `m⊠b`; the second misses
   `m⊠a`.
4. So `(m⊠a)* ∨ (m⊠b)* = 1`. By (C.1) this reads `(¬m⊠1) ∨ (1⊠(a*∨b*)) = 1`, forcing `a*∨b*=1`, which
   contradicts `z_A=0`.

The one place a "new generic open" could cause trouble is step 4, and it does not: farness is tested on
the two ground rectangles, where (C.1) applies. That is exactly why `U` multiplies over the Cohen base
while `D₂` does not (N4).

**This is the item I would most like a second reader on.** It contradicts the notes' expectation that the
Cohen product is a hard discriminating case.

## 4. Revised closing lists

### (a) Defects and proof obligations, in priority order

1. **Have N3 checked.** It closes the repository's stated next test.
2. **Carry the missing definitions into the packet:** `K_E` with the symmetry remark, `Γ_E`, the two clopen
   theorems, and the two-apex space. All are in the notes and all are correct.
3. **Tighten the Arrieta wording.** Attribute strong Hausdorffness and the anti-Urysohn property to the
   paper (Cor. 4.3, Prop. 4.4). Attribute the countable basis and `W=W₂=U=A²` to the project's own short
   arguments. `W=W₂=U` needs only `z_A=0` and (A.1), not the regular-closed-core theorem.
4. **Restate (D.1).** The `D₂` half holds under (κ,2)-distributivity. Add N4 as the sharpness control.
   Change the Cohen test to "closed level settled by N3; `D(Z_C×A)` open".
5. **Shorten the regular-remainder case** with N2: no Booleanization, and a two-step bound for every q.
6. **Name the real import in (C.3)** as directed-join preservation by `π_*`; drop Beck–Chevalley. State the
   two density facts behind (C.6).
7. **Minor.** Remove T₁ from the Cantor–Bendixson claim. Define "U-linked". Relax the caution in F.1:
   preimage of sublocales preserves all meets.
8. **Obligation on the report.** N3, N4 and N5 have had no second reader.

### (b) Usability

| Class | Results |
| --- | --- |
| Usable now | (A.1)–(A.5); (B.1)–(B.3) with compact and regular corollaries; one-sided rigidity; support reduction and marked-hole persistence; Baire and Cantor–Bendixson claims; (C.1), (C.2), (C.6), (C.7); the clopen-bundle theorem 6.3 and Corollary 6.4; (D.1); E.1, E.2; (F.1)–(F.3); G.1, G.2, G.4 |
| Conditionally usable | (C.3)–(C.5) and the compact-clopen-chart theorem 4.2, on the properness theorem; the locally compact sober metacompact class, on the Baire theorem; G.3 and the D application, on Arrieta's paper; N2–N7, pending a second check |
| Not yet usable | Any `D`-level statement over the Cohen base beyond N4 and N5(b) |

### (c) What to attack next

Unchanged in substance, with one consequence of §3: the Cohen × Arrieta product should come off the list
of discriminating tests. The remaining well-posed Cohen question is whether `D(Z_C×A) = Δ×D(A)`. The first
choice remains testing Q′ at Φ-rank two on non-compact relatives of the two-apex space, since every control
examined so far has `W=U` for a trivial reason or is compact.

## 5. What was and was not opened

Read, in the sections cited above: the chromatic, Q′ pre-nucleus, point-free products, separated-factor,
two-apex, frontier one-sided rigidity, Boolean-base and marked-Urysohn notes of 12 November.

Not opened, by design: the Session 8 consolidation, the referee-addendum audit, and all earlier
reconciliation and ledger files. The other notes listed in section H of the packet were not re-read,
because the blind verdicts on their content did not depend on them.
