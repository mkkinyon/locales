# Project A — Product preservation for the lower hierarchy: I, D, V, W and M

**Consolidation, 17 November 2026.** Internal mathematical status only; no independent external audit of the nonspatial-product counterexamples in this note. Work classically and use the specialization convention \(x\le y\) iff every open containing \(x\) contains \(y\). Novelty and literature priority are not assessed.

## 1. Distinguish the two products

* **Locale product:** \(X\times_{\mathrm{Loc}}Y\), dual to the **frame coproduct** \(\mathcal O(X)\oplus_{\mathrm{Frm}}\mathcal O(Y)\).
* **Frame product:** \(\mathcal O(X)\times_{\mathrm{Frm}}\mathcal O(Y)=\mathcal O(X\sqcup Y)\), dual to the **locale coproduct** \(X\sqcup Y\).

The results below concern the relations as actual sublocales of the relevant localic square, not merely their ordinary-point relations.

Write
\[
\mathcal I_X=\operatorname{cl}_{X^2}(\Delta_X),\quad
\mathcal D_X=\operatorname{fit}_{X^2}(\Delta_X),\quad
\mathcal V_X=\operatorname{fit}_{X^2}(\mathcal I_X),\quad
\mathcal W_X=\operatorname{cl}_{X^2}(\mathcal D_X),\quad
\mathcal M_X=\mathcal I_X\wedge\mathcal D_X.
\]
For any set of points \(P\) of a sober space, \([P]\) denotes the *least sublocale containing* \(P\); one must not silently infer \(\operatorname{pt}[P]=P\).

## 2. Point-induced formulas in the stably locally compact class

For stably locally compact \(X\) put
\[
P_X^-=\{(x,y):\exists r\in X,\ r\le x,\ r\le y\},\quad
P_X^+=\{(x,y):\exists s\in X,\ x\le s,\ y\le s\},\quad
T_X=\uparrow_{X^2}P_X^+.
\]
The independently refereed SC+ theorem and its saturation lemma, in [ProjectA_SCplus_CANONICAL_2026-11-15.md](ProjectA_SCplus_CANONICAL_2026-11-15.md), give
\[
\boxed{\mathcal I_X=[P_X^+],\quad
\mathcal D_X=[P_X^-],\quad
\mathcal V_X=[T_X],\quad
\mathcal W_X=[\overline{P_X^-}].}\tag{2.1}
\]
Here the closure is ordinary closure in the *spatial* \(X^2\). Each displayed relation is spatial, but only the stronger SC+ results identify exact point sets of \(\mathcal I,\mathcal D\); no point-set equality for arbitrary \([T_X]\) is presumed.

The specialization order of a product is coordinatewise. Therefore, for stably locally compact \(X,Y\),
\[
P_{X\times Y}^{\pm}=P_X^\pm\times P_Y^\pm,\qquad
T_{X\times Y}=T_X\times T_Y.\tag{2.2}
\]
Products of stably locally compact locales are stably locally compact and their localic products are spatial.

## 3. Exact positive locale-product results

**Proposition I.** For stably locally compact \(X,Y\),
\[
\mathcal I_{X\times Y}=\mathcal I_X\times\mathcal I_Y.
\]
Indeed \(\Delta_{X\times Y}=\Delta_X\times\Delta_Y\) under the square identification, and ordinary closure commutes with finite spatial products. The product of closed localic embeddings is closed, so this is an equality of closed sublocales.

**Theorem W.** For stably locally compact \(X,Y\),
\[
\boxed{\mathcal W_{X\times Y}=\mathcal W_X\times\mathcal W_Y.}\tag{3.1}
\]
Using (2.1)–(2.2), the left side is the closed sublocale induced by
\[
\overline{P_X^-\times P_Y^-}
=\overline{P_X^-}\times\overline{P_Y^-}.
\]
The right side is the same closed sublocale, since products of closed embeddings are closed. This does **not** imply that \(\mathcal D\) preserves locale products.

**Lax comparisons.** For stably locally compact \(X,Y\),
\[
\boxed{\mathcal D_{X\times Y}\le\mathcal D_X\times\mathcal D_Y,\qquad
\mathcal V_{X\times Y}\le\mathcal V_X\times\mathcal V_Y,\qquad
\mathcal M_{X\times Y}\le\mathcal M_X\times\mathcal M_Y.}\tag{3.2}
\]
For \(\mathcal D,\mathcal V\), the left side is the least sublocale containing respectively \(P_X^-\times P_Y^-\) or \(T_X\times T_Y\), and the right side contains these points. The \(\mathcal M\)-inequality follows from that of \(\mathcal D\), exactness for \(\mathcal I\), and finite-intersection stability of products of embeddings. Do not infer the reverse inequality from equality of ordinary points.

## 4. Nonspatial-product counterexample for V

Let \(C\) be Cantor space and let \(T\subset C\) be countable and dense. It has no isolated points and is homeomorphic to \(\mathbb Q\). Take disjoint patch components
\[
A=\{a_t:t\in C\}\cong C,\quad
B=\{b_t:t\in C\}\cong C,\quad
R=\{r_t:t\in T\}\text{ discrete}.
\]
Define the strict specialization comparisons to be precisely
\[
r_t<a_t,\qquad r_t<b_t\qquad(t\in T),
\]
besides their reflexive/transitive consequences. Let \(X\) carry the upper topology from this patch/order data.

**Stable local compactness.** The patch space \(K=A\sqcup B\sqcup R\) is locally compact Hausdorff. Adjoin the one-point compactification point \(\bot\) and declare \(\bot\) below every element. The order graph is closed: a net of distinct witness points escaping \(R\) can only converge to \(\bot\), and all resulting comparisons with \(\bot\) are present. The resulting compact ordered space has a stably compact upper topology, and \(X=K\) is an open upper subspace, hence stably locally compact.

**Algebraic frame.** Cantor clopens form compact open upper neighborhoods on \(A,B\). For \(r_t\) use
\[
\{r_t\}\cup V_A\cup V_B
\]
where the Cantor-clopen neighborhoods \(V_A,V_B\) contain \(a_t,b_t\), respectively. These are compact patch-open upper sets; their finite intersections again are compact open. They form a basis, so \(\mathcal O(X)\) is algebraic and stably continuous (not compact).

**Rational open slice.** The sheets \(A,B\) are open upper subsets of \(X\). Within \(A\times B\), the set \(P_X^+\) of common-upper pairs is empty. Nevertheless, the upward saturation \(T_X=\uparrow P_X^+\) meets this rectangle in exactly
\[
T_X\cap(A\times B)=\{(a_t,b_t):t\in T\}\cong\mathbb Q.
\]
Indeed, to have \((a_s,b_t)\in T_X\) one needs \(u\le a_s,v\le b_t\) with a common upper bound. The only possible cross-sheet bridge is the *same* witness \(r_t\), so \(s=t\in T\); the converse follows from \((r_t,r_t)\in P_X^+\). The induced sublocale identity for intersection with an open component shows that \(\mathcal V_X=[T_X]\) has an *open sublocale* \(\mathbb Q_{\mathrm{loc}}\), not just a rational set of points.

Therefore \(\mathcal V_X\times\mathcal V_X\) contains the open localic sublocale \(\mathbb Q_{\mathrm{loc}}\times\mathbb Q_{\mathrm{loc}}\). By Johnstone, *Stone Spaces*, Proposition II.2.14, this locale is nonspatial; hence \(\mathcal V_X\times\mathcal V_X\) is nonspatial. But by (2.1)–(2.2),
\[
\mathcal V_{X\times X}=[T_X\times T_X]
\]
is spatial. Combined with the lax inclusion (3.2), this proves
\[
\boxed{\mathcal V_{X\times X}\subsetneq\mathcal V_X\times\mathcal V_X.}\tag{4.1}
\]
This strictness follows from the difference in spatiality. No assertion that the two sublocales have identical ordinary point sets is needed or currently established: for a general subset (T_X), the point set of ([T_X]) may exceed (T_X).

**Earlier D and M witnesses.** The same \(X\) gives an open rational slice of \(\mathcal D_X\), so \(\mathcal D_{X\times X}<\mathcal D_X\times\mathcal D_X\). Adjoin a patch-isolated greatest specialization point \(\omega\) to obtain \(Y\), with the old \(X\) closed in \(Y\). Then \(\mathcal I_Y=Y^2\), so \(\mathcal M_Y=\mathcal D_Y\); restriction of point-induced sublocales along the closed inclusion gives \(\mathcal D_X=\mathcal D_Y\wedge X^2\). Thus \(\mathcal M_{Y\times Y}<\mathcal M_Y\times\mathcal M_Y\). These D/M claims are part of the same still-internally-audited product program, not an independent external finding.

## 5. A positive compact-factor theorem for V

**Theorem (compact factor, internally checked).** If \(X\) is stably compact and \(Y\) stably locally compact, then
\[
\boxed{\mathcal V_{X\times Y}=\mathcal V_X\times\mathcal V_Y.}\tag{5.1}
\]

Here \(P_X^+=\operatorname{pt}\mathcal I_X\) is closed in the original \(X^2\), hence closed and compact in its Hausdorff patch topology. The patch order graph is closed, so \(T_X=\uparrow P_X^+\), the image under projection of a closed subset of a compact product, is patch-closed. By the compact-pospace/patch-closed-subspace theorem, \(T_X\) with its induced topology is stably compact. Therefore \(\mathcal V_X=[T_X]\) is stably compact, in particular locally compact and sober.

For an arbitrary topological space \(T_Y\), the localic product of the locally compact sober space \(T_X\) with the locale of \(T_Y\) is the locale induced by the ordinary topological product \(T_X\times T_Y\). Consequently
\[
\mathcal V_X\times\mathcal V_Y=[T_X\times T_Y]=\mathcal V_{X\times Y}.
\]
This compact-factor extension relies on standard compact-pospace and localic-product theorems, not just the trivial spatiality of each factor.

## 6. Frame products (locale coproducts), unrestricted

For an arbitrary family of locales \(X_i\), let \(Z=\coprod_iX_i\), so \(\mathcal O(Z)=\prod_i\mathcal O(X_i)\) is the **frame product**. The localic square decomposes into clopen blocks \(X_i\times X_j\); the diagonal lies only in blocks with \(i=j\). Closure and fitting of a sublocale supported on diagonal blocks are computed componentwise. Thus for **all locales**, without stable local compactness,
\[
\boxed{\mathcal V\!\left(\coprod_iX_i\right)\cong\coprod_i\mathcal V(X_i),\qquad
\mathcal W\!\left(\coprod_iX_i\right)\cong\coprod_i\mathcal W(X_i).}\tag{6.1}
\]
Both resulting sublocales vanish on off-diagonal blocks. The same applies to \(\mathcal I,\mathcal D,\mathcal M\). This is *frame-product* preservation, not locale-product preservation. It does not claim that infinite locale products distribute over arbitrary coproducts.

## 7. Inventory and audit boundaries

| Relation | Locale products (stably locally compact) | Frame products (all locales) |
|---|---|---|
| \(\mathcal I\) | Exact | Exact |
| \(\mathcal D\) | Lax, sometimes strict | Exact |
| \(\mathcal V\) | Lax, sometimes strict; exact if one input stably compact | Exact |
| \(\mathcal W\) | Exact | Exact |
| \(\mathcal M\) | Lax, sometimes strict | Exact |

**Dependence and status.** The SC+ point-induced and saturation theorems were independently blind-refereed earlier. The present product arguments and Cantor rational-slice obstruction have undergone internal checking only, pending a separate adversarial report. Do not promote them to externally audited status or claim literature priority. The possible converse to the compact-factor theorem and analogous product questions for \(\mathcal U,\mathcal J,\mathcal H\) remain open in this note.

## References

- [SC+ canonical theorem](ProjectA_SCplus_CANONICAL_2026-11-15.md), particularly the saturation lemma and point formulas.
- Peter T. Johnstone, *Stone Spaces* (Cambridge, 1982), II.2.13–14 and III.1.4, for spatial localic products and the nonspatial rational square.
- Jung–Kegelmann–Moshier, *Stably compact spaces and closed relations*, Theorem 2.5, for compact pospaces and upper topologies.
- Jung, *Stably compact spaces and the probabilistic powerspace construction*, for patch-closed subspaces.
- Project A earlier D/M product-segment calculations in the research conversation; these are awaiting independent audit.
