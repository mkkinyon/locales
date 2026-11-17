# Project A — Lower-hierarchy products: post-referee canonical account

**17 November 2026. Status:** the underlying SC+ point/saturation results were previously blind-refereed; the lower-product packet received a positive independent *blind* report and a mathematical addendum on 16 November. Corrections and extensions from those reports are integrated below. The final Plewe-derived strengthening in §8 is **new post-review work**, not part of the blind verdict. No originality or literature-priority claim is made.

**Historical sources:** [pre-referee consolidation](ProjectA_LOWER_PRODUCT_PRESERVATION_CONSOLIDATION_2026-11-17.md), [historical internal adversarial audit](ProjectA_LOWER_PRODUCT_PRESERVATION_INTERNAL_ADVERSARIAL_AUDIT_2026-11-17.md), [referee reconciliation](ProjectA_LOWER_PRODUCTS_EXTERNAL_REFEREE_RECONCILIATION_2026-11-17.md), and [SC+ canonical note](ProjectA_SCplus_CANONICAL_2026-11-15.md). The two reports received as attachments are not silently substituted for the historical internal audit.

## 1. Conventions and the two different products

Work classically. Sublocale order is inclusion. For a locale \(X\), write \(X^2=X\times_{\mathrm{Loc}}X\), \(\Delta_X\hookrightarrow X^2\), and

\[
\begin{split}
\mathcal I_X&=\operatorname{cl}(\Delta_X),&
\mathcal D_X&=\operatorname{fit}(\Delta_X),\\
\mathcal V_X&=\operatorname{fit}(\mathcal I_X),&
\mathcal W_X&=\operatorname{cl}(\mathcal D_X),\\
\mathcal M_X&=\mathcal I_X\wedge\mathcal D_X.
\end{split} \tag{1.1}
\]

**Locale product** means \(X\times_{\mathrm{Loc}}Y\); on frames it is the **frame coproduct** \(\mathcal O(X)\oplus\mathcal O(Y)\). Conversely **frame direct product** \(\prod_i\mathcal O(X_i)\) corresponds to locale **coproduct** \(\coprod_iX_i\). The two must not be interchanged.

For any set of points \(P\) of a sober space \(Z\), \([P]\) is the smallest sublocale of \(Z\) containing those points. In general \(\operatorname{pt}[P]\) is the sobrification of \(P\), not necessarily literally \(P\). Set \(\operatorname{sp}(S)=[\operatorname{pt}(S)]\), its largest spatial sublocale.

## 2. Exact SLC point formulas

A stably locally compact (SLC) space is understood as locally compact, sober, coherent (finite intersections of compact saturated sets are compact), and well-filtered. Here \(x\le y\) means every open containing \(x\) contains \(y\). For SLC \(X\), set

\[
\begin{split}
P_X^-&=\{(x,y):\exists r,\ r\le x,\ r\le y\},\\
P_X^+&=\{(x,y):\exists s,\ x\le s,\ y\le s\},\\
T_X&=\uparrow_{X^2}P_X^+,\qquad
E_X=P_X^-\cap P_X^+.
\end{split} \tag{2.1}
\]

The independently checked SC+ theorem, combined with the referee's \(\mathcal M\)-restriction observation, gives the **equalities of sublocales**

\[
\boxed{\mathcal I_X=[P_X^+],\quad \mathcal D_X=[P_X^-],\quad
\mathcal V_X=[T_X],\quad \mathcal W_X=[\overline{P_X^-}],\quad
\mathcal M_X=[E_X].} \tag{2.2}
\]

The bar is ordinary closure in the spatial \(X^2\). All five are spatial. Moreover their *exact point spaces* are, respectively, \(P_X^+,P_X^-,T_X,\overline{P_X^-},E_X\). The key correction to our earlier internal audit is that \(P_X^-\) and \(T_X\) are specialization-upper (saturated) subspaces of the sober \(X^2\), hence sober. A saturated subspace of a sober space is sober: close an irreducible closed subset in the ambient sober space and use upper saturation to retain its generic point. Also \(P_X^+\) is closed and \(E_X\) is closed in \(P_X^-\).

Under the canonical identification \((X\times Y)^2\cong X^2\times Y^2\) for SLC factors, specialization and all witnesses split coordinatewise:

\[
P_{X\times Y}^{\pm}=P_X^{\pm}\times P_Y^{\pm},\qquad
T_{X\times Y}=T_X\times T_Y,\qquad
E_{X\times Y}=E_X\times E_Y. \tag{2.3}
\]

All topological products in (2.3) carry their subspace product topology; the *localic product* of the corresponding induced sublocales can have extra, pointless structure.

## 3. The product inventory

| Relation | Binary locale products, arbitrary locales | Binary locale products, SLC factors | One stably compact SLC factor | Arbitrary frame direct products |
|---|---|---|---|---|
| \(\mathcal I\) | **Exact** | Exact | Exact | **Exact** |
| \(\mathcal D\) | **Lax** | Lax, sometimes **strict** | **Exact** | **Exact** |
| \(\mathcal V\) | **Lax** | Lax, sometimes **strict** | **Exact** | **Exact** |
| \(\mathcal W\) | **Lax**; general exactness **open** | **Exact** | Exact | **Exact** |
| \(\mathcal M\) | **Lax** | Lax, sometimes **strict** | **Exact** | **Exact** |

The orientation in every “lax” entry is

\[
\boxed{\mathcal R_{X\times Y}\ \le\ \mathcal R_X\times\mathcal R_Y.} \tag{3.1}
\]

These are claims about *actual sublocales*. Exactness for finite locale products has not been extrapolated to infinite locale products. Frame direct products of any cardinality are a separate, proved case (§7).

### 3.1 Results valid for arbitrary locales

**Closure/product lemma.** For arbitrary sublocales \(S\hookrightarrow X,T\hookrightarrow Y\),

\[
\operatorname{cl}(S\times T)=\operatorname{cl}S\times\operatorname{cl}T. \tag{3.2}
\]

Indeed a product of dense sublocales is dense: a frame coproduct is generated by open rectangles, a pure rectangle \(a\otimes b\) vanishes exactly when one factor vanishes, and the zero-reflecting quotient maps for dense sublocales induce a zero-reflecting coproduct map. The right side of (3.2) is closed and \(S\times T\) is dense in it. Consequently \(\mathcal I_{X\times Y}=\mathcal I_X\times\mathcal I_Y\) without SLC assumptions.

Products of fitted sublocales are fitted: \(S\times T=\pi_X^{-1}S\wedge\pi_Y^{-1}T\), and inverse image preserves the relevant meets and opens. Applying the minimality of fitting to products of diagonals (and of \(\mathcal I\)) yields the lax \(\mathcal D,\mathcal V\) inequalities. The \(\mathcal W\)-inequality follows from (3.2), and the \(\mathcal M\)-inequality from exactness of \(\mathcal I\) and the product-of-meets formula.

### 3.2 The stronger SLC spatial-part theorem

**Theorem (referee E5, extended to the closed branches).** For SLC \(X,Y\) and *each* \(\mathcal R\in\{\mathcal I,\mathcal D,\mathcal V,\mathcal W,\mathcal M\}\),

\[
\boxed{\mathcal R_{X\times Y}=\operatorname{sp}(\mathcal R_X\times\mathcal R_Y).} \tag{3.3}
\]

For \(\mathcal D,\mathcal V,\mathcal M\), (2.2)–(2.3) identify the left side as the least sublocale containing precisely the points of the right side. For \(\mathcal I,\mathcal W\), their proven exactness and spatiality give (3.3). **Thus exactness for SLC factors is equivalent to spatiality of the localic product \(\mathcal R_X\times\mathcal R_Y\).** In particular, whenever (3.1) is strict in the SLC setting, the two sides have *the same points*: strictness is entirely point-free.

Using (3.2), \(\mathcal W\) is exact for SLC products since \(\mathcal W_X\) is the closed subspace \(\overline{P_X^-}\), and \(\overline{P_X^-\times P_Y^-}=\overline{P_X^-}\times\overline{P_Y^-}\). Also \(\mathcal D_{X\times Y}\) is **dense** in \(\mathcal D_X\times\mathcal D_Y\): both have the same closure \(\mathcal W_X\times\mathcal W_Y\).

## 4. An indispensable restriction lemma

**Complemented restriction (referee G1).** If \(Z\) is sober, \(P\subseteq Z\), and \(F\) is either an *open* or a *closed* subspace of \(Z\), then inside \(Z\)

\[
\boxed{[P]\wedge[F]_{\mathrm{open/closed}}=[P\cap F].} \tag{4.1}
\]

The notation on the left means the corresponding open or closed sublocale, not an arbitrary point-generated sublocale. To prove (4.1), split \([P]=[P\cap F]\vee[P\setminus F]\). The two terms lie in complementary open/closed sublocales; finite distributivity of the coframe of sublocales gives the formula. **Do not extend (4.1) to arbitrary noncomplemented sublocales.** For example, disjoint dense subspaces of \(\mathbb R\) may induce sublocales with nonzero meet.

## 5. Counterexamples: nonspatial rational slices

Let \(C\) be Cantor space, and \(H\subset C\) countable dense without isolated points (thus \(H\cong\mathbb Q\)). Form the locally compact Hausdorff *patch* space

\[
K=A\sqcup B\sqcup R,qquad A=\{a_t:t\in C\},\quad B=\{b_t:t\in C\},\quad R=\{r_t:t\in H\},
\]

where \(A,B\cong C\), \(R\) discrete, and the strict order consists exactly of \(r_t<a_t,r_t<b_t\). In the one-point compactification \(K^+=K\cup\{\bot\}\), put \(\bot\le z\) for all \(z\). The order is closed: sequential limits of non-diagonal comparisons either stabilize at one witness or send the first coordinate to \(\bot\); all resulting limits belong to the order. Since \(K^+\) is compact metric, sequential closedness suffices. Its upper topology is stably compact. The open upper subspace \(X_0=K\) is SLC and noncompact.

Its frame is **algebraic**. A corrected compact-open basis contains both (i) sheet-only \(V_A\sqcup W_B\) for Cantor clopen \(V,W\) and (ii) \(\{r_t\}\sqcup V_A\sqcup W_B\) where \(t\in H\), \(t\in V\cap W\). The earlier claim that type (ii) alone is meet-stable was false: intersections at distinct witnesses can be sheet-only.

The rectangle \(U=A\times B\) is open in \(X_0^2\). Direct order checking gives

\[
P^-_{X_0}\cap U=T_{X_0}\cap U
=\{(a_t,b_t):t\in H\}\cong\mathbb Q,qquad P^+_{X_0}\cap U=\varnothing. \tag{5.1}
\]

By (4.1) this rational slice is an **open sublocale** of both \(\mathcal D_{X_0}\) and \(\mathcal V_{X_0}\). The localic square \(\mathbb Q_{\mathrm{loc}}\times\mathbb Q_{\mathrm{loc}}\) is not spatial (Johnstone, *Stone Spaces*, II.2.14; independently see Plewe, §1, and the referee addendum's Isbell-density proof). Its open embedding in \(\mathcal D_{X_0}\times\mathcal D_{X_0}\), and likewise \(\mathcal V_{X_0}\times\mathcal V_{X_0}\), makes these products nonspatial; the corresponding relations of \(X_0\times X_0\) are spatial by (3.3). Hence

\[
\mathcal D_{X_0\times X_0}\subsetneq\mathcal D_{X_0}\times\mathcal D_{X_0},\qquad
\mathcal V_{X_0\times X_0}\subsetneq\mathcal V_{X_0}\times\mathcal V_{X_0}. \tag{5.2}
\]

For \(\mathcal M\), adjoin a patch-isolated **greatest** specialization point \(\omega\) to obtain the SLC space \(Y_0\), with opens \(\varnothing\) and \(\{\omega\}\cup O\) (\(O\) open in \(X_0\)). The old \(X_0\) is a closed subspace of \(Y_0\), and \(P^+_{Y_0}=Y_0^2\). Thus \(\mathcal I_{Y_0}=\mathcal V_{Y_0}=Y_0^2\) and \(\mathcal M_{Y_0}=\mathcal D_{Y_0}\). By **closed** restriction (4.1), \(\mathcal D_{X_0}=\mathcal D_{Y_0}\wedge c(X_0^2)\). Therefore the nonspatial \(\mathcal D_{X_0}^2\) is a closed sublocale of \(\mathcal M_{Y_0}^2\), and

\[
\mathcal M_{Y_0\times Y_0}\subsetneq\mathcal M_{Y_0}\times\mathcal M_{Y_0}. \tag{5.3}
\]

The \(Y_0\) construction separates the \(\mathcal V\)- and \(\mathcal D\)-behaviors: \(\mathcal V\) is trivially exact on \(Y_0^2\), but \(\mathcal D\) is strict there. All inequalities in (5.2)–(5.3) have identical point sets on both sides by (3.3).

## 6. Compact and patch-closed factors

**Theorem (referee E6, strengthening the old \(\mathcal V\)-only theorem).** Suppose \(X\) is stably compact and \(Y\) is SLC. Then \(\mathcal R_{X\times Y}=\mathcal R_X\times\mathcal R_Y\) for all five \(\mathcal R\).

Only \(\mathcal D,\mathcal V,\mathcal M\) need proof. In the compact Hausdorff patch of \(X^2\), the specialization order is closed; each of \(P_X^-,P_X^+,T_X\) is a projection of a closed relation on a compact product and is therefore patch-closed, and so is \(E_X\). By the patch-closed-subspace theorem (Jung 2004, Proposition 16), these three relevant point spaces are stably compact, hence locally compact. For any locally compact sober space \(A\) and sober space \(B\), the comparison

\[
\eta_{A,B}:\operatorname{Loc}(A\times_{\mathrm{Top}}B)longrightarrow
\operatorname{Loc}(A)\times_{\mathrm{Loc}}\operatorname{Loc}(B) \tag{6.1}
\]

is an isomorphism. On frames it is the **surjection** \(\mathcal O(A)\oplus\mathcal O(B)\twoheadrightarrow\mathcal O(A\times_{\mathrm{Top}}B)\). Naturality with respect to the embeddings of \(A=E_{\mathcal R}(X)\), \(B=E_{\mathcal R}(Y)\) into their ambient squares identifies the localic product with the point-induced sublocale \([A\times B]\). Formula (3.3) then gives exactness.

**Qualified generalization:** the same argument works for any SLC \(X\) and \(\mathcal R\in\{\mathcal D,\mathcal V,\mathcal M\}\) whenever its point space \(E_{\mathcal R}(X)\) is locally compact; in particular the referee notes a sufficient patch-closedness condition. This does not imply that *all* SLC factors have locally compact point relations, by §5.

## 7. Arbitrary frame direct products, fully unrestricted

For locales \(X_i\), \(Z=\coprod_{i\in I}X_i\) has \(\mathcal O(Z)=\prod_i\mathcal O(X_i)\). Its square is the disjoint clopen coproduct of blocks \(X_i\times X_j\). The diagonal vanishes on off-diagonal blocks and restricts to \(\Delta_{X_i}\) on each diagonal block. Every nucleus on an arbitrary frame direct product \(L=\prod_iL_i\) is componentwise: for \(e_i\) the central idempotent selecting coordinate \(i\),

\[
j(a)\wedge e_i=j(a\wedge e_i)\wedge e_i.
\]

Thus sublocales, closure, fitting, finite meets, and joins of the clopen blocks are computed coordinatewise **even for infinite \(I\)**. It follows for each of the five relations that, under the canonical block identification,

\[
\boxed{\mathcal R_{\coprod_i X_i}=\coprod_i\mathcal R_{X_i}
\quad\text{(diagonal blocks only).}} \tag{7.1}
\]

Here the right side is embedded into \(Z^2\) as the coproduct of diagonal-block relations, with zero on every \(i\ne j\) block. Empty families are included. **This is not** an assertion about arbitrary infinite *locale* products.

## 8. Plewe's spatiality results and a fixed test factor

**Primary source now read:** T. Plewe, *Localic Products of Spaces*, *Proc. London Math. Soc.* (3) **73** (1996), 642–678, DOI [10.1112/plms/s3-73.3.642](https://doi.org/10.1112/plms/s3-73.3.642). Exact results: Theorem **1.1** (game criterion for products of sober spaces); Theorem **1.6** (Isbell's spatial-multiplier characterization for completely regular spaces); Theorem **2.2** (metrizable multiplier iff every nonempty closed subspace has a relatively locally compact point; equivalently complete with no closed copy of the irrationals); Theorem **2.4** (Hurewicz: metrizable strongly Baire iff no closed copy of \(\mathbb Q\)); and Theorem **2.6** (if metrizable \(A\) is not strongly Baire, \(A\times_{\mathrm{Loc}}B\) is spatial iff metrizable \(B\) is a spatial multiplier). The referee's original rational/irrational slice test is a special case.

**Corollary (new deduction from Plewe, pending its own external audit).** Let \(X\) be SLC and \(\mathcal R\in\{\mathcal D,\mathcal V\}\). If \(E_{\mathcal R}(X)\) contains a **closed metrizable subspace \(F\)** that is **not a spatial multiplier**, then

\[
\mathcal R_{X\times X_0}\subsetneq\mathcal R_X\times\mathcal R_{X_0}. \tag{8.1}
\]

For \(\mathcal M\), use \(E_{\mathcal M}(X)=E_X\) and replace \(X_0\) by \(Y_0\). In particular, the hypothesis holds if \(F\) is incomplete, or if it has a closed subspace homeomorphic to the irrationals; it includes the addendum's closed \(\mathbb Q\) and irrational cases. Proof: \(F\) gives a closed sublocale of \(\mathcal R_X\) by (4.1); the test factor contains the rational open slice of §5 (for \(\mathcal M\), inside the closed \(\mathcal D_{X_0}\) part of \(\mathcal M_{Y_0}\)). Plewe 2.6 makes \(\mathbb Q_{\mathrm{loc}}\times\operatorname{Loc}(F)\) nonspatial, hence the product of the relations is nonspatial. Apply (3.3). A space need not itself be a copy of \(\mathbb Q\) or of the irrationals for this conclusion to apply.

**Important scope warning:** if SLC \(X\) has *metrizable whole* \(T_X\), or whole \(P_X^-\), or whole \(E_X\), its embedded diagonal \(\Delta_X\cong X\) is metrizable, hence \(X\) is \(T_1\). An SLC \(T_1\) space is locally compact Hausdorff (its specialization order is equality in the patch-pospace representation); therefore \(P_X^-=P_X^+=T_X=E_X=\Delta_X\). Thus Plewe's metrizable-factor classification applies to **proper metrizable slices** of the nontrivial relations, not to their complete point spaces. For whole (generally nonmetrizable) sober relations, Plewe's **Theorem 1.1 game** remains applicable.

## 9. Open problems and scope boundaries

1. **Unrestricted \(\mathcal W\).** For arbitrary locales, is \(\mathcal W_{X\times Y}=\mathcal W_X\times\mathcal W_Y\)? By (3.2) this is equivalent to density of \(\mathcal D_{X\times Y}\) in \(\mathcal D_X\times\mathcal D_Y\). We know it for SLC factors, not in general.
2. **Converse to the compact-factor theorem.** If SLC \(X\) has exact \(\mathcal V\)-product with every SLC \(Y\), must \(T_X\) be locally compact? Plewe-based test (8.1) excludes any closed metrizable slice that is not a spatial multiplier, but does not settle the general nonmetrizable problem.
3. **Infinite locale products.** No arbitrary-infinite assertion is included. In particular do not use (7.1) (frame products) to infer it.
4. **Reverse \(\mathcal D/\mathcal V\) separation.** Can \(\mathcal D_X\) have spatial product with every SLC test factor while \(\mathcal V_X\) fails for some factor?
5. **Beyond the lower five:** analogous product questions for \(\mathcal U,\mathcal J,\mathcal H\) have not been audited here.

### References and provenance

- The original independent report, *Referee report — Project A products in the lower localic hierarchy* (16 Nov 2026), results G1–G5 and E1–E8; and *ProjectA_referee_report_addendum_2026-11-16*, A1–A3. Received as user attachments; its questions Q1–Q4 remain proposals rather than established statements.
- Plewe (1996), DOI above, personally checked against the user-supplied published paper in this session. In particular the original addendum had **not** consulted Plewe directly, whereas this consolidation has.
- P. T. Johnstone, *Stone Spaces* (1982), II.2.14 (nonspatial rational square). Plewe, p. 646, independently cites this proof.
- A. Jung, A. Kegelmann, M. A. Moshier, *Stably compact spaces and closed relations* (2001), Theorem 2.5 (compact pospaces).
- A. Jung, *Stably compact spaces and the probabilistic powerspace construction* (2004), Proposition 16 (patch-closed subspaces).

**Editorial note:** Corrections to the earlier note are catalogued, not erased, in the separate reconciliation. Any further extension (especially §8) should receive its own independent adversarial read before reuse in a paper.
