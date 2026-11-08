# Project A — Properness, effectiveness, quotient locales, and Scott continuity

**Source and dependency audit | 8 November 2026 | Inventory segment 7**

This document is a theorem- and proof-oriented consolidation of the historical Project A notes. **It is not a fresh blind external refereeing and makes no originality claims.** It distinguishes (P) published mathematical input, (E) previously externally checked with qualifications, (I) internally checked working proofs, and (O) unresolved. The main source set is linked at the end.

## 1. Executive verdict

1. **Effectiveness is settled in the literature:** Vermeulen, *Proper Maps of Locales* (1994), Corollary 5.17: *closed proper internal equivalence relations of locales are effective*, **with no compactness assumption on the ambient locale**. Vermeulen's Corollary 5.14 is a different weakly-fitted condition. Manuell, *Presenting Quotient Locales* (2023), Remark 3.8, describes the proper coequalizer and its fixed-point frame. The formerly proposed effectiveness problem is closed as a research direction.
2. **Our point-free relation lemma is independent of properness:** `I∘I≤U` for every locale. Thus `I=U` implies `I` is an internal equivalence relation, regardless of spatiality or associativity of general composition.
3. **A proper quotient need not be completely regular.** Under the additional hypothesis that `O(X)` is continuous (classical ZFC), a proper quotient of `I` is continuous and strongly Hausdorff, hence completely regular. Under compactness of `X`, the quotient is compact and strongly Hausdorff, hence regular and completely regular even if `X` is nonspatial. Without these hypotheses, effectivity does **not** entail `I=F`.
4. **The Scott-continuity status contradiction is resolved:** `A-scott-continuity-converse.md` gives a proof, and the top banner of the later `A-scott-continuity-converse-status-2026-10-21.md` explicitly corrects its obsolete “unresolved” body. For a **closed topological** relation `E⊆X×Y`, with `X` *weakly locally compact*, `r_E=(p_Y)_*p_X^*` is Scott-continuous iff `p_Y:E→Y` is topologically perfect (closed with compact fibers). For a closed **localic** relation on a classical continuous locale `X`, this gives `r_E` Scott-continuous iff `p_2` proper as a locale map. This is an **I** theorem, internally audited after the original external reports, not a new blind-external certificate.
5. **Transitivity alone does not make the operator idempotent:** even with `I=U=F`, the closed-relation operator `r_I` may fail idempotence and Scott continuity. The finite-fiber nonclosed-quotient example is externally reviewed. Under **proper projections**, `r_E=q^*q_*` and is idempotent/Scott-continuous.
6. The **arbitrary-frame/localic** converse `r_I` Scott-continuous ⇒ `p_i` proper remains **O**, without continuity/spatial-product assumptions; no point-set argument is silently extended to pointless locales.

## 2. Definitions and precise terminology

Fix a locale `X`, let `L=O(X)` and `Q=L⊕L`. For a closed reflexive symmetric relation `E=C(d_E)↪X×X`, write

- `α=p_1^*:L→O(E)`, `β=p_2^*:L→O(E)`, and
- `r_E=β_*α:L→L`, where `β_*` is right adjoint to `β`.

The frame-only formula is

`r_E(u)=⋁{v∈L : 1⊠v ≤ (u⊠1)∨d_E}`.

A locale map `p:E→X` is **proper** when its right adjoint `p_*` (i) preserves directed joins and (ii) satisfies **closed Frobenius**

`p_*(v∨p^*(u))=p_*(v)∨u`.

This is stronger than Scott continuity of a composite `β_*α`. For ordinary topological maps, *perfect* here means **closed with compact point fibers**, not the potentially different “inverse images of compact sets are compact” convention used in other contexts.

## 3. Effectiveness and the proper quotient (published input)

**P-E1 (Vermeulen 1994, Cor. 5.17).** A closed internal equivalence sublocale `E↪X×X` with proper coordinate projections is effective, i.e. `E=kerpair(q)` for its coequalizer `q:X→Q_E`. No ambient compactness is needed. This is the genuine theorem; our earlier attempt to prove effectiveness under special `E=clΔ` assumptions added no generality.

**P-E2 (Vermeulen and Manuell).** The coequalizer of such a proper equivalence relation is a proper quotient; its inverse-image frame can be represented by fixed points of an interior operator. For a proper **reflexive symmetric** equivalence relation the operator below is `q^*q_*`. Manuell 2023, Remark 3.8 provides the more general symmetric-pair formulation.

**I-E3 (our universal lemma).** `I∘I≤U`, proved in the frame of the localic threefold product: on the composable-pair sublocale `I_12∧I_23`, for a far pair `a*∨b*=1`, the disjointness relations give `a_1∧(a*)_2=0` and `(b*)_2∧b_3=0`, whence `a_1∧b_3=0`. No associativity of composition is used.

**Consequence.** `I=U` makes `I` internally transitive since `I∘I≤U=I`. Reflexivity and symmetry are unconditional. If the projections are proper, the effective quotient exists and is proper. But `I=U` alone neither forces properness nor implies `I=F` for noncompact continuous locales.

## 4. The relational interior operator and false idempotence claim

**P/I-O1.** `r_E` is monotone, deflationary (reflexivity), preserves finite meets, and has fixed-point frame

`Fix(r_E)={u : p_1^*(u)=p_2^*(u)}`

for reflexive symmetric `E`. These are the `E`-invariant opens. In general, **`r_E(u)` need not itself be invariant**. For the coequalizer `q`, the operator `s=q^*q_*` selects the greatest invariant open below `u`; universally `s≤r_E`, and under the stated reflexive symmetric hypotheses `r_E` is idempotent iff `r_E=s`. Properness of the equivalence-relation projections ensures equality.

**E-O2 (externally reviewed counterexample).** In the countable, compact-open-based, sober space `X={a,b}∪{c_n,d_n:n≥1}`, with opens subject to `a∈O⇒b∈O`, `c_n∈O⇒d_n∈O`, and `a∈O⇒d_n∈O` for all but finitely many `n`, the localic relations satisfy `I=U=F`. The equivalence classes are `{a,b}` and `{c_n,d_n}` and the quotient is a compact convergent sequence. Nevertheless for `u={a,b}∪{d_n:n≥1}`,

`r_I(u)={b}`,  `r_I²(u)=∅`.

Every fiber is finite, but the quotient is **not closed**. An increasing open cover also witnesses failure of Scott continuity. Reference: `A-saturation-operator-nonidempotence.md` and the October 20 two-referee reconciliation.

**I-O3 (exact spatial test).** For an ordinary equivalence relation `E` represented by a topologically closed relation, with the appropriate spatial/localic comparison,

`r_E(u)=X\overline{E[X\u]}`.

Thus `r_E²=r_E` iff the closure of `E[C]` is `E`-saturated for every closed `C`. A **closed quotient** suffices; it is not necessary. Idempotence does not follow just from E being an equivalence relation.

## 5. Scott continuity versus properness: the recovered theorem

**I-S1 (topological, internally audited).** Let `X` have a cover by opens `V_i` each contained in some compact `K_i` (weak local compactness). Let `Y` be arbitrary and `E⊆X×Y` closed. Then

`r_E:O(X)→O(Y)` preserves directed joins  **iff**  `p_Y:E→Y` is closed with compact fibers.

**Forward proof, explicitly identifying the topological hypothesis.** For finite `F`, put `U_F=⋃_{i∈F}V_i`, `K_F=⋃_{i∈F}K_i`, and `W_F=r_E(U_F)`. The directed joins `⋃_FU_F=X` and `r_E(X)=Y`, together with Scott continuity, yield `Y=⋃_FW_F`. Adjunction says

`E∩(X×W_F)⊆U_F×W_F⊆K_F×W_F`.

On each `W_F`, `E` is closed in the product of a **compact** first factor with `W_F`. The tube lemma implies the projection of any closed subset of `E` is closed locally on `W_F`, hence globally. Each fiber is closed inside some compact `K_F`. No Hausdorffness of `X` or `Y` is required. **Closedness of E in X×Y is essential.**

**Reverse proof.** For a closed map with compact fibers, the right adjoint to inverse image preserves directed joins: a directed cover of the compact fiber can be reduced to one member; closedness makes the right-adjoint values open. Composing with `p_X^*` preserves directed joins.

**I-S2 (continuous locales, classical ZFC).** If `O(X)` is continuous, the Hofmann–Lawson representation identifies `X` with a strongly locally compact sober space, its localic square with the ordinary product, and closed sublocales with closed topological subspaces of that product. Then for every closed localic `E↪X²`,

`r_E Scott-continuous ⇔ p_2:E→X proper as a locale map`.

For symmetric `E`, the coordinate flip gives properness of both projections. This does **not** need transitivity. One direction is immediate from Scott continuity of the right adjoint of a proper map; the converse applies I-S1 then uses the topological closed/Frobenius formula for a perfect map. Outside the continuous/spatial comparison, the inference remains **unproved**.

**Historical status correction.** `A-scott-continuity-converse-status-2026-10-21.md` has an **explicit correction banner** saying its “unresolved” assertion is obsolete in the continuous case; its body still lists the formerly open special cases. `A-external-audit-reconciliation-2026-10-21.md` (§3) independently rechecked the October 20 proof after the earlier reports. Canonical status: **I** for I-S1/I-S2; **O** for arbitrary noncontinuous locales. This is not a blanket “externally verified” classification.

## 6. Completely regular quotients and two positive collapse theorems

**I-C1 (continuous source).** Assume `O(X)` continuous, `I=clΔ` internally transitive, and both projections `I⇉X` proper. Then `q:X→Q_I` is effective and proper by Vermeulen; `Q_I` is **strongly Hausdorff** because the image of closed `I` under proper `q×q` is precisely its diagonal; its frame is **continuous**, since `q_*` Scott-continuous and `q_*q^*=id` transfer way-below approximants from `O(X)` to `O(Q_I)`. Under classical spatiality, `Q_I` is therefore locally compact Hausdorff and completely regular.

Every real map `f:X→ℝ` coequalizes `I` (indeed `I≤F`) and factors through `q`. Since `Q_I` is completely regular, `q` is the completely regular reflection. Hence `F=kerpair(q)=I`, and `I≤U≤F` implies

**`I=U=F`.**

In particular `I=U` and Scott continuity of `r_I` are sufficient for the collapse in a continuous locale. **They are not necessary:** there are examples `I=U=F` in which `r_I` is not Scott-continuous.

**I-C2 (compact source, including pointless locales).** If `X` is compact and `I` internally transitive, then `I` is a **closed proper** equivalence relation automatically: closed inclusions are proper, and projection `X²→X` is proper because the other factor `X` is compact. The quotient `Q_I` is proper effective and compact. The same closed-image argument makes `Q_I` strongly Hausdorff.

**The previously outstanding primary input is now located:** Picado–Pultr–Tozzi, *Locales* (chapter II, §6.4), explicitly proves that **each compact Hausdorff locale is regular** (Hausdorff there means closed diagonal), and §4.8 deduces complete regularity. Accordingly `Q_I` is completely regular even when `X` is not spatial or continuous. Thus

**For compact locales, `I` internally transitive ⇔ `I=U` ⇔ `I=U=F`.**

The direction `I=U⇒I` transitive follows from I-E3; the converse is this proper-quotient argument. This is a derived corollary of published machinery and our point-free composition lemma, not a novelty claim. The source dependency cited as “bibliography pending” in the October 20 ledger can now be closed at the level of finding the theorem (a manuscript proof still needs an exact edition/page reference).

## 7. Why proper effectiveness does **not** imply functional collapse without a source hypothesis

Do not replace “strongly Hausdorff” by “completely regular” outside the compact/continuous categories. The precise obstruction is not effectivity but lack of real-valued separation on `Q_I`.

There is in fact a **simple negative general pattern** (source-supported deduction): take any nontrivial **regular Hausdorff space on which every continuous real-valued function is constant**; classical examples are given by Gantner (1971), with predecessors due to Hewitt and Novák. The locale is regular, hence strongly Hausdorff: `I=U=Δ`. Thus its `I`-projections are isomorphisms (automatically proper), the quotient is `q=id_X`, and effectivity is trivial. Yet `F=X²>Δ`. Therefore properness of `I⇉X` **alone** does not imply `I=F` for arbitrary locales. This conclusion is distinct from the still-open Scott-continuity **converse** for arbitrary locales.

Primary historical example: T. E. Gantner, “A Regular Space on Which Every Continuous Real-Valued Function Is Constant,” *American Mathematical Monthly* (1971). The repository's `A-equality-characterizations.md` and October 21 referee report already use the general phenomenon; the above application sharpens its placement in the properness ledger. The existence of the example was independently checked bibliographically during this consolidation; this *new application* is **I**, not independently refereed as part of an original packet.

## 8. Properness failure mechanisms (do not merge these examples)

| Example | `I=U=F`? | Fibers of quotient | Quotient closed? | Scott continuity `r_I`? | What it shows |
|---|---|---|---|---|---|
| Deleted-plank cofinite-cloud | **No** (`I=U<F`) | Some noncompact | Yes | No | Closed quotient alone does not give properness or functional collapse |
| Countable paired `a,b,c_n,d_n` | Yes | Finite | No | No; `r_I²≠r_I` | Compact fibers alone do not give properness or idempotence |
| Duplicated real-line points `1/n` | Yes | Finite | No | No (by I-S2, since properness fails) | `I=F` does not imply closed saturation/closed quotient |
| Regular non-functionally-Hausdorff space | **No** (`I=U=Δ<F`) | Singletons | Yes (`q=id`) | Yes (`r_I=id`) | Even properness plus effectivity cannot replace complete regularity of the quotient |

The distinct lessons are **compact fibers**, **closed image/saturation**, **idempotence**, **Scott continuity**, and **functional separation**. None may be used as a synonym for another.

For an ordinary topologically closed relation `E⊆X²`, images `E[K]` of compact subsets `K` are closed by the tube lemma. Failure of closed saturation of a closed `C` therefore forces representatives to **escape every compact subset** while partners converge. This mechanism is illustrated concretely by the duplicated-real-point example in `A-closed-saturation.md`. The escape statement is an **ordinary topological** theorem, not asserted as a point-free arbitrary-locale characterization.

## 9. Dependency diagram (textual)

`rectangular coproduct & closed diagonal` → `I∘I≤U` → `[I=U ⇒ I an internal equivalence relation]`

`proper projections of closed E` + `E an equivalence relation` → **Vermeulen 5.17** → `effective proper q`, `kerpair(q)=E`, `Δ_Q closed`.

Then either:

- `O(X)` **continuous** + `q` proper → `O(Q)` continuous (classically spatial) + closed diagonal → `Q` locally compact Hausdorff → `Q` completely regular → `E=I=F`;
- `X` **compact** → `Q` compact + closed diagonal → **Picado–Pultr–Tozzi compact Hausdorff ⇒ regular ⇒ completely regular** → `E=I=F`.

Separately:

`X` weakly locally compact **topological** + `E⊆X×Y` **closed** → `r_E` Scott ⇔ `p_Y` perfect → for continuous locale `X`, `p_Y` proper.

There is **no asserted arrow** from Scott continuity of `r_E` to properness of `p_Y` on arbitrary noncontinuous locales; and **no asserted arrow** from properness/effectivity to complete regularity of arbitrary quotients.

## 10. Open issues and editorial actions

**Open or not independently certified:**
- **O:** Arbitrary-locale implication `r_I` Scott-continuous ⇒ `p_2:I→X` proper, absent continuous-frame/spatial comparison.
- **O:** Whether some stronger, intrinsic **frame-only** hypothesis on the effective quotient guarantees complete regularity without assuming compactness or continuity. The naive unconditional implication is *false* by regular nonfunctionally-Hausdorff examples.
- **I:** The weakly-locally-compact topological Scott converse is a complete internal proof, but it was checked retrospectively, not blindly refereed as a standalone theorem.
- **I:** Compact `I`-transitivity collapse derives from published Vermeulen + Picado–Pultr–Tozzi inputs; manuscript-level reference precision/independent review remains useful.

**Recommended repository edits (not made here):**
1. Replace the body status “unresolved” in `A-scott-continuity-converse-status-2026-10-21.md` by a historical note and put a one-line proof citation to the October 20 note; retain the top correction banner.
2. Make `A-vermeulen-effectiveness-correction.md` and `A-proper-inseparability-relations.md` the authoritative references for effectivity and proper continuous quotients. Distinguish the published Corollary 5.17 from our deductions explicitly.
3. Add the compact-Hausdorff-locale regularity citation (Picado–Pultr–Tozzi §6.4), resolving an October 20 outstanding bibliography item.
4. Retain `A-saturation-operator-nonidempotence.md` as the canonical correction to the false “equivalence ⇒ idempotent r” inference.
5. Clarify that noncontinuous proper **collapse** is false, while the noncontinuous **Scott-continuity converse** remains open.
6. Keep exact distinctions topological/spatial/localic and weak/strong local compactness in theorem statements.

## 11. Primary literature and project source index

**Published and external:**
- J. J. C. Vermeulen, [*Proper Maps of Locales*](https://core.ac.uk/download/pdf/82053693.pdf), *J. Pure Appl. Algebra* **92** (1994), 79–107, especially Corollary 5.17 (printed p. 107), Proposition 5.5.
- G. Manuell, [*Presenting Quotient Locales*](https://link.springer.com/article/10.1007/s10485-023-09736-x), *Applied Categorical Structures* **31** (2023), article 28, Remark 3.8 (corrected published version).
- J. Picado, A. Pultr, A. Tozzi, [*Locales*](https://www.mat.uc.pt/~picado/publicat/Chapter2.pdf), chapter II §6.4, “Each compact Hausdorff locale is regular”; §4.8, regular compact ⇒ completely regular.
- T. E. Gantner, [*A Regular Space on Which Every Continuous Real-Valued Function Is Constant*](https://www.math.wustl.edu/~freiwald/4181RegnotCReg.pdf), 1971.

**Project source notes:**
- [A-proper-inseparability-relations.md](https://github.com/mkkinyon/locales/blob/main/A-proper-inseparability-relations.md)
- [A-vermeulen-effectiveness-correction.md](https://github.com/mkkinyon/locales/blob/main/A-vermeulen-effectiveness-correction.md)
- [A-scott-continuity-converse.md](https://github.com/mkkinyon/locales/blob/main/A-scott-continuity-converse.md)
- [A-scott-continuity-converse-status-2026-10-21.md](https://github.com/mkkinyon/locales/blob/main/A-scott-continuity-converse-status-2026-10-21.md)
- [A-external-audit-reconciliation-2026-10-21.md](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md)
- [A-external-audits-reconciliation-2026-10-20.md](https://github.com/mkkinyon/locales/blob/main/A-external-audits-reconciliation-2026-10-20.md)
- [A-saturation-operator-nonidempotence.md](https://github.com/mkkinyon/locales/blob/main/A-saturation-operator-nonidempotence.md)
- [A-closed-saturation.md](https://github.com/mkkinyon/locales/blob/main/A-closed-saturation.md)
- [A-equality-characterizations.md](https://github.com/mkkinyon/locales/blob/main/A-equality-characterizations.md)

**End of standalone report.**