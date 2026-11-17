# Project A — Internal adversarial audit of lower-hierarchy product preservation

**17 November 2026.** Independent external review has **not** occurred for this package. This is an internal, adversarial check of [the consolidation](ProjectA_LOWER_PRODUCT_PRESERVATION_CONSOLIDATION_2026-11-17.md), taking the previously blind-refereed SC+ saturation and point-induced formulas as established input. The referee-style checks below distinguish actual sublocales from mere point sets. Literature priority is outside scope.

## Verdict

**Core product conclusions survive the audit**, subject to the external SC+ dependency and the traditional classical locale/topology comparison theorems:
\[
\begin{gathered}
\mathcal W(X\times Y)=\mathcal W(X)\times\mathcal W(Y)\quad\text{for stably locally compact }X,Y,\\
\mathcal V(X\times Y)\le\mathcal V(X)\times\mathcal V(Y),\quad\text{strict for an algebraic stably locally compact }X,\\
\mathcal V(X\times Y)=\mathcal V(X)\times\mathcal V(Y)
\quad\text{if }X\text{ is stably compact and }Y\text{ stably locally compact},\\
\mathcal V(\coprod_iX_i)\cong\coprod_i\mathcal V(X_i),\qquad
\mathcal W(\coprod_iX_i)\cong\coprod_i\mathcal W(X_i)
\quad\text{for arbitrary locale families.}
\end{gathered}
\]

**One material overstatement was detected and corrected in the consolidation:** the strict \(\mathcal V\)-product inclusion was described as invisible to ordinary points. That conclusion is **not established**. The proof establishes a spatial-versus-nonspatial difference and needs no equality of point sets. Because \([\uparrow P^+]\) may have points beyond its generating subset, no unconditional assertion of point equality is permissible.

## A. Adversarial checks

### A1. Does the SLC saturation formula apply to V, and is V spatial?

**Pass, with explicit dependency.** The previously independently audited saturation lemma states \(\operatorname{fit}_Z([P])=[\uparrow P]\) for stably locally compact sober \(Z\). Here \(Z=X^2\) is stably locally compact, and \(\mathcal I_X=[P_X^+]\) because it is closed in spatial \(X^2\). Thus \(\mathcal V_X=[T_X]\). This is spatial since the locale of the subspace \(T_X\) has enough points, even when \(T_X\) itself is not sober. It does **not** follow that \(\operatorname{pt}(\mathcal V_X)=T_X\).

### A2. Is the witness-sheet construction actually stably locally compact?

**Pass.** The patch \(K=A\sqcup B\sqcup R\) is locally compact Hausdorff; \(A,B\) are compact Cantor components and \(R\) is countably infinite discrete. In the one-point compactification \(K^+=K\cup\{\bot\}\), extend the order with global bottom \(\bot\). Every potentially new limit of an edge \((r_t,a_t)\) or \((r_t,b_t)\) has first coordinate \(\bot\), because distinct witnesses can only escape to \(\bot\). The limiting edges are already included. The order graph is closed; the upper topology on \(K^+\) is stably compact by the compact-pospace correspondence, and \(K\) is an open upper subspace. Its frame is algebraic: compact Cantor clopen upper neighborhoods on each maximal sheet, and compact patch-open upper neighborhoods \(\{r_t\}\cup V_A\cup V_B\) at the witnesses, form a meet-stable basis. The frame is noncompact because infinitely many isolated witnesses require infinitely many basis members to cover.

**No shortcut:** ordinary Hausdorff local compactness of the patch alone would not suffice without the closed-order verification.

### A3. Could the rational slice be larger because fitting adds non-spatial 'ghosts'?

**Pass at the sublocale level, without presuming point-set equality.** Set \(T_X=\uparrow P_X^+\). For \(a_s\in A,b_t\in B\), if \((a_s,b_t)\in T_X\), there exist \(u\le a_s,\ v\le b_t\) and a common upper \(w\ge u,v\). The only order links from sheet \(A\) to sheet \(B\) are via a *single* witness \(r_q\), so this forces \(s=t=q\in T\). Conversely \((r_t,r_t)\in P_X^+\) lies below \((a_t,b_t)\). Thus the set-theoretic slice is exactly the countable dense diagonal \(T\cong\mathbb Q\).

To verify that this is an **open sublocale**, use the following general identity. If \(P\) is a subset of the points of a sober locale \(Z\), and \(U\subseteq Z\) is an **open** sublocale with complementary closed sublocale \(C\), then
\[
[P]=[P\cap U]\vee[P\cap C],\qquad [P]\wedge U=[P\cap U].
\]
Indeed, the two summands lie under \(U,C\), respectively, and distributivity of the sublocale lattice removes the second summand upon intersection with \(U\). This identity is stronger and safer than a mere claim about points of \([P]\). Taking \(P=T_X\), \(U=A\times B\), gives the exact open sublocale \(\mathbb Q_{\mathrm{loc}}\hookrightarrow\mathcal V_X\).

### A4. Does the nonspatial product obstruction really prove strict inclusion?

**Pass.** Products of open localic embeddings are open, so \(\mathbb Q_{\mathrm{loc}}\times_{\mathrm{Loc}}\mathbb Q_{\mathrm{loc}}\) embeds openly into \(\mathcal V_X\times\mathcal V_X\). Johnstone, *Stone Spaces*, II.2.14, proves this rational localic square nonspatial. Open sublocales of spatial locales are spatial; therefore \(\mathcal V_X\times\mathcal V_X\) is nonspatial.

By coordinatewise specialization, \(T_{X\times X}=T_X\times T_X\), so \(\mathcal V_{X\times X}=[T_X\times T_X]\) is spatial. The lax inclusion is valid because \(\mathcal V_X\times\mathcal V_X\) contains every point in \(T_X\times T_X\), hence contains their *least* generated sublocale. Spatiality versus nonspatiality now makes the inclusion strict. **No point-set equality is asserted or required.**

### A5. Is W-product exactness merely an equality of point sets?

**Pass as an equality of closed sublocales.** SC+ yields \(\mathcal D_X=[P_X^-]\). The closure of a point-induced sublocale in spatial \(X^2\) is the ordinary closed subspace \([\overline{P_X^-}]\). For stably locally compact \(X,Y\), \(X^2\times Y^2\) is spatial and has the ordinary product topology, and
\[
\overline{P_X^-\times P_Y^-}
=\overline{P_X^-}\times\overline{P_Y^-}.
\]
Products of closed localic embeddings are closed; both proposed sides of W-exactness are literally the same closed sublocale of the spatial product. This proof does **not** require \(\mathcal D\) itself to commute with locale products, which it demonstrably need not.

### A6. Does 'frame products' accidentally mean localic products?

**Pass.** The frame direct product corresponds to the **locale coproduct**. For \(Z=\coprod_i X_i\) the frame \(\mathcal O(Z)=\prod_i\mathcal O(X_i)\) contains central complementary idempotents \(e_i\) forming a disjoint covering partition of \(1\). They split the square into clopen \(X_i\times X_j\) blocks. All diagonal data lie in the \(i=j\) blocks. The closure and fitting operations are componentwise over this disjoint decomposition, including arbitrary index sets because arbitrary joins of the \(e_i\) exist in frames. This establishes the frame-product claims for **all locales**, without invoking preservation of infinite **locale** products (a different and generally hazardous question).

### A7. Is the compact-factor V theorem valid in the presence of extra sobrification points?

**Pass, provided the classical patch-subspace and locally compact product theorems are invoked explicitly.** If \(X\) is stably compact, \(P_X^+=\operatorname{pt}\mathcal I_X\) is closed in the original topology on \(X^2\), hence compact and closed in the Hausdorff patch. Its upward closure \(T_X\) is a projection of a closed subset of a compact pospace product, hence patch-closed. The standard theorem that patch-closed subspaces of stably compact spaces remain stably compact in the induced topology makes \(T_X\) sober and locally compact. In particular, \(\mathcal V_X=[T_X]\) is the locale of that stably compact subspace.

For arbitrary stably locally compact \(Y\), we keep \(T_Y\) as a *topological subspace*, possibly nonsober. The standard comparison for a locally compact sober first factor gives
\[
\mathcal O(T_X)\oplus\mathcal O(T_Y)\cong\mathcal O(T_X\times T_Y).
\]
Since both factor embeddings are point-induced, their localic product embedding is exactly \([T_X\times T_Y]\), which agrees with \(\mathcal V(X\times Y)\). The argument does not depend on a speculative identity \(\operatorname{pt}[T_Y]=T_Y\). The compact-factor theorem is classical and substantially stronger than a compact–compact special case, but is still internally checked rather than blind-refereed.

## B. Corrections, limitations and recommendations

1. **Corrected (material):** Remove the assertion that \(\mathcal V(X\times X)<\mathcal V_X\times\mathcal V_X\) is invisible on ordinary points. We have a nonspatial obstruction, not a proof that the two sides have the same points. The consolidation has been updated.
2. **Scope:** Locale-product theorems rely on stable local compactness. They should not be promoted to arbitrary frames without separate proof. Frame **direct-product** statements, in contrast, are unrestricted.
3. **Hypotheses:** 'Stably compact' in the compact-factor proposition includes compactness. A mere stably locally compact factor does not suffice, as the Cantor-witness counterexample shows.
4. **Sourcing:** Cite Johnstone II.2.14 for \(\mathbb Q_{\mathrm{loc}}^2\) nonspatiality, Jung–Kegelmann–Moshier for the compact-pospace correspondence, and the patch-closed-subspace result for compact-factor preservation. The latter is not a consequence of point-set calculations alone.
5. **External review targets:** An independent referee should attack (i) the closedness of the one-point compactified order graph; (ii) the exact rational open sublocale identification; (iii) the compact-factor patch-closedness argument; and (iv) the assertion of arbitrary frame-product preservation.
6. **No novelty claim:** The structural locale-product and frame-product results may overlap classical literature; literature priority is unreviewed.

## C. Final internal status

| Claim | Verdict |
|---|---|
| \(\mathcal W\) exact on stably locally compact locale products | **PASS** (SC+ dependent) |
| \(\mathcal V\) lax inequality on stably locally compact locale products | **PASS** (SC+ dependent) |
| Strict \(\mathcal V\)-product failure for algebraic stably locally compact \(X\) | **PASS** (Johnstone rational-square input) |
| \(\mathcal V\) exact with one stably compact factor | **PASS** (standard patch and local-compactness theorems) |
| \(\mathcal V,\mathcal W\) exact under arbitrary frame products | **PASS** (componentwise coproduct decomposition) |
| Same ordinary point sets for the strict \(\mathcal V\) inclusion | **NOT ESTABLISHED; REMOVED** |
| Fully general locale-product results for all frames | **NOT CLAIMED** |
| Literature novelty / independent external audit | **NOT DONE** |

**Overall:** The mathematical core of the consolidation withstands the internal adversarial pass after one necessary qualification. Given the nonspatial-product result, a *blind independent referee* would be appropriate before canonical promotion.
