# Project A — Foundational Audit II: the Scott-continuity converse

**Date:** 8 November 2026.  
**Disposition:** **PASS (internal adversarial reconstruction)** for the topological theorem and its classical continuous-locale corollary. **Not an external blind referee report** and not a claim of originality. The general arbitrary-locale converse remains open.

## 1. Canonical sources and exact scope

Primary project proof: [`A-scott-continuity-converse.md`](https://github.com/mkkinyon/locales/blob/main/A-scott-continuity-converse.md) (20 October), §§1–5. Cross-check: [`A-external-audit-reconciliation-2026-10-21.md`](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md), §3. Historical/open-status note [`A-scott-continuity-converse-status-2026-10-21.md`](https://github.com/mkkinyon/locales/blob/main/A-scott-continuity-converse-status-2026-10-21.md) begins with a correction and its old unresolved entries are **obsolete** for continuous locales only.

The present result is **not** Vermeulen's effectiveness theorem: it supplies a criterion for properness of a projection of a closed relation on a *continuous locale*, where Vermeulen's quotient theorems may then be applied if the relation is an equivalence relation.

Throughout, Scott-continuity means preservation of directed joins of open subsets. A topological projection called *perfect* in the original note means **continuous, closed, with compact fibers**; this does **not** assert Hausdorff or separated fibers. Terminology varies in the literature, so the descriptive phrase is safer. A *proper locale map* means Scott-continuity of its right adjoint together with the **closed Frobenius** law.

## 2. The topological theorem — reconstructed and checked

**Theorem T.** Let `X` be a topological space in which **every point has a compact neighborhood** (weak local compactness), let `Y` be any topological space, and let `E ⊆ X × Y` be **closed**. Give `E` the subspace topology; denote its projections `p_X:E→X`, `p_Y:E→Y`. For any open `U ⊆ X`, set

\[
 r_E(U)=(p_Y)_*p_X^{-1}(U)
       =\operatorname{int}_Y\bigl(Y\setminus E[X\setminus U]\bigr).
\]

Then

\[
 \boxed{r_E\text{ preserves directed joins }\iff p_Y\text{ is closed with compact fibers}.}
\]

**No** `T₀`, sobriety, Hausdorff, symmetry, reflexivity or transitivity hypothesis is used.

### 2.1. Forward implication: local compact support

Pick open sets `V_i` covering `X` and compact subsets `K_i` with `V_i ⊆ K_i`; the compact sets need not be closed. For each finite index set `F` let `U_F = ⋃_{i∈F}V_i` and `K_F = ⋃_{i∈F}K_i`. The `U_F` form a directed family with union `X`; `K_F` is compact by finite union.

Scott-continuity and the fact that a right adjoint sends the whole domain to the whole codomain imply

\[
 Y=r_E(X)=\bigcup_{F\text{ finite}}r_E(U_F).
\]

Put `W_F = r_E(U_F)`. By the definition of right adjoint,

\[
 p_Y^{-1}(W_F)\subseteq p_X^{-1}(U_F),
 \qquad E\cap(X\times W_F)\subseteq K_F\times W_F. \tag{1}
\]

For every target point `y` choose `F` with `y∈W_F`; then (1) gives a **single compact source subset** controlling all relation-fibers over an open neighborhood of `y`. This is substantially stronger than pointwise compactness.

### 2.2. Forward implication: closedness of the projection

Take any `H ⊆ E` closed in the subspace topology. Because **E is closed in `X×Y`**, `H` is also closed in `X×Y`. On a chosen `W_F`, inclusion (1) ensures

\[
 p_Y(H)\cap W_F
 =\pi_Y\bigl(H\cap (K_F\times W_F)\bigr).
\]

The set on the right is the projection of a closed subset of `K_F×W_F`: it is closed *in that product*, even though `K_F` itself need not be closed in `X`. The projection `K_F×W_F →W_F` is closed by the compact-factor tube lemma; no Hausdorffness is needed. Thus `p_Y(H)∩W_F` is closed in `W_F`. Because the `W_F` form an open cover of `Y`, `p_Y(H)` is closed in `Y`.

### 2.3. Forward implication: compactness of every fiber

For `y∈W_F`, the fiber `E_y={x:(x,y)∈E}` lies inside `K_F`. It is closed in `K_F` because `E` is closed in `X×Y`, and is therefore compact. This includes empty fibers.

### 2.4. Reverse implication: Scott-continuity of the full right adjoint

For **any** continuous closed map `f:Z→Y`, its inverse-image right adjoint is

\[
 f_*(V)=Y\setminus f(Z\setminus V),\qquad V\in\mathcal O(Z), \tag{2}
\]

because the image of the closed set `Z\V` is closed. If in addition every fiber `f^{-1}{y}` is compact and `(V_i)` is a directed collection of open subsets of `Z`, any fiber lying in `⋃V_i` lies in some **single** `V_i`: compactness gives a finite subcover, and directedness dominates those finitely many indices. Formula (2) therefore shows

\[
 f_*\left(\bigcup_iV_i\right)=\bigcup_i f_*(V_i).
\]

Apply this to `f=p_Y`, and compose with the all-join-preserving `p_X^*`. This proves the reverse implication. In fact, it proves the stronger conclusion that **`(p_Y)_*` itself** is Scott-continuous, whereas the hypothesis concerned only `(p_Y)_*p_X^*`.

### 2.5. A convenient equivalent formulation

Under the hypotheses of Theorem T, these three conditions are equivalent:

1. `r_E` preserves directed joins.
2. For every `y∈Y` there exist an open neighborhood `W` of `y` and a compact `K ⊆ X` such that `E ∩ (X×W) ⊆ K×W` (**local uniform compact support**).
3. `p_Y` is closed with compact fibers.

The implications 1→2→3→1 are exactly the preceding proof. The weak-local-compactness hypothesis is used specifically in 1→2. The closedness hypothesis on `E` is used specifically in 2→3. We do **not** claim this characterization without those assumptions.

## 3. The localic transfer — reconstructed and checked

**Theorem L (classical logic and choice).** Let `X` be any locale with **continuous frame** `L=O(X)`, and `E ↪ X×_loc X` any **closed** sublocale. Let `p₁,p₂:E⇉X` be its projections. Then

\[
 \boxed{(p_2)_*p_1^*\text{ Scott-continuous }\iff p_2\text{ proper as a locale map}.}
\]

If `E` is symmetric, the swap of coordinates gives properness of **both** projections.

**Bridge 1: space representation.** Classical Hofmann–Lawson duality represents the continuous frame `L` as the frame of opens of a locally compact sober topological space `X_pt`. This is stronger than weak local compactness. The finite localic product of these spaces agrees with the ordinary topological product, so `O(X×_loc X)=O(X_pt×_top X_pt)`. The closed localic `E` therefore corresponds to an ordinary closed subset of the topological product (it is sober as a closed subspace of a sober space). Coordinate projections agree under this identification.

**Bridge 2: topological closed + compact-fibered implies localic proper.** Let `f:Z→Y` be a continuous closed map with compact fibers. Section 2.4 proves `f_*` Scott-continuous. Moreover for opens `V⊆Z`, `W⊆Y`, formula (2) and the set-theoretic identity `f(A∩f^{-1}B)=f(A)∩B` give

\[
\begin{aligned}
 f_*\bigl(V\cup f^{-1}W\bigr)
 &=Y\setminus f\bigl((Z\setminus V)\cap f^{-1}(Y\setminus W)\bigr)\\
 &=(Y\setminus f(Z\setminus V))\cup W\\
 &=f_*(V)\cup W.
\end{aligned}
\]

This is the closed Frobenius law `f_*(v∨f^*w)=f_*(v)∨w`, **not** a general law for arbitrary localic maps. Thus `f` is proper as a locale map (Vermeulen/Manuell convention).

**Bridge 3: converse.** If `p₂` is proper as a locale map, then by definition `(p₂)_*` preserves directed joins. Its composite with `p₁^*`, which preserves arbitrary joins, does too. No representation is needed for this easier direction.

**Audit verdict:** Both bridges are legitimate under the stated **classical continuous-frame** hypothesis. Neither can be silently applied to a noncontinuous/possibly pointless locale.

## 4. Consequences for the inseparability relation

Set `E=I_X=cl(Δ_X)`, a closed symmetric relation. For continuous `X`, Theorem L yields

\[
 \boxed{r_I\text{ Scott-continuous}\iff p_1,p_2:I\rightrightarrows X\text{ proper}.}
\]

If `I` is *also internally transitive*, it is a closed proper internal equivalence relation. Vermeulen (1994, Cor. 5.17) gives its effective proper quotient; proper quotients preserve continuity of frames, and its quotient has a closed diagonal. Classical local compactness + closed diagonal makes the quotient locally compact Hausdorff and hence completely regular. The quotient is therefore the completely regular reflection, and

\[
 \boxed{I=U=F.}
\]

It is enough to assume `I=U` instead of independent transitivity, using the separately established universally valid `I∘I ⊆ U`. Conversely, functional collapse `I=U=F` does **not** imply Scott continuity or properness.

**Dependencies not re-refereed here:** Vermeulen's effectiveness theorem, the proper-quotient machinery, and identification `F=kerpair(X→X_cr)` have their own prior source/audit records. The Scott-continuity audit has not independently reproved the entirety of that quotient theory.

## 5. Adversarial stress tests and scope cautions

**(a) Compact fibers alone are insufficient.** The externally supplied countable algebraic sober example `X={a,b}∪{c_n,d_n:n≥1}` with inseparability classes `{a,b}`, `{c_n,d_n}` has finite classes and `I=U=F`, but the quotient is not closed. There exist directed opens `u_N↑1` with `r_I(u_N)` excluding `a` for all `N`; hence `r_I` is not Scott-continuous. Canonical source: [`A-saturation-operator-nonidempotence.md`](https://github.com/mkkinyon/locales/blob/main/A-saturation-operator-nonidempotence.md).

**(b) Closedness alone is insufficient.** The cofinite-cloud deleted-plank example has a closed quotient but noncompact classes and `r_I` fails Scott-continuity. Canonical source: [`A-proper-inseparability-relations.md`](https://github.com/mkkinyon/locales/blob/main/A-proper-inseparability-relations.md).

**(c) Idempotence is NOT an unstated step.** None of §§2–3 uses `r_E^2=r_E`. In general, even an internal equivalence relation can have a nonidempotent `r_E`; properness supplies idempotence **after** it is proved, not beforehand.

**(d) Terminology.** Some topological authors call a closed compact-fibered map `proper`, and reserve `perfect` for a `proper` map whose relative diagonal is closed (separatedness). Others call a closed compact-fibered map `perfect`. State the property instead of relying solely on the name. In localic literature, `semi-proper`/`perfect` may refer just to Scott-continuity of `f_*`; this is strictly weaker than properness unless closed Frobenius is also established.

**(e) No stronger claims.** The theorem assumes `E` is CLOSED, the source `X` has a COVER by open sets lying in compact subsets, and the localic transfer assumes classical continuity of `O(X)`. We did not prove `r_E` Scott ⇒ properness for arbitrary locales, nor any quotient effectiveness statement for nontransitive tolerances.

## 6. Status disposition and referee targets

- **Master ledger Q04:** retain `I` (internally checked), now with a line-by-line adversarial reconstruction and compact-support proof.
- **Master ledger Q05:** retain `I` (internally checked), with the localic properness bridge explicitly proved and named classical representation inputs.
- **Master ledger Q06:** no status change to the published-effectiveness-dependent synthesis; the implication from Q05 is confirmed, but full independent primary-source audit of all quotient ingredients belongs elsewhere.
- **Open-problem register:** do not reinstate the continuous-locale Scott converse as open. Keep the **arbitrary-locale** converse open and separate from the deferred tolerance-effectiveness question.
- **Next external review, if chosen:** ask for adversarial verification of (i) the precise weak-local-compactness assumption; (ii) topological tube-lemma step without `T₂`; (iii) compatibility of `O(X×_loc X)` with `O(X_pt×_top X_pt)` for locally compact sober spaces; (iv) full closed Frobenius; and (v) whether any of the argument accidentally needs symmetry or transitivity. Do **not** give an auditor the internal PASS before their independent derivation.

## 7. Reference pointers

- J. Picado and A. Pultr, *Frames and Locales: Topology without points* (2012), Hofmann–Lawson duality and locale-product comparison.
- J. J. C. Vermeulen, *Proper Maps of Locales*, *Journal of Pure and Applied Algebra* **92** (1994), 79–107, Corollary 5.17 (proper effectiveness).
- G. Manuell, *Presenting Quotient Locales* (2023), properness definition as Scott-continuity plus closed Frobenius: https://link.springer.com/article/10.1007/s10485-023-09736-x .
- For the locally compact sober product comparison, see J. Picado and A. Pultr, *Notes on the product of locales*, *Mathematica Slovaca* **65** (2015), 247–264; cited as Proposition 4.4.1 in the discussion https://mathoverflow.net/questions/341528/product-of-topological-spaces-and-product-of-corresponding-locales/342413 .
- Source theorem and historical reconciliation documents linked in §1.