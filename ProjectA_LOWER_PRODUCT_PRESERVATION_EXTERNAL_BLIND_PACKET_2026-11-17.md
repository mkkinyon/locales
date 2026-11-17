# Project A — Blind mathematical packet: products in the lower localic separation hierarchy

**17 November 2026. Independent examination requested.** This packet is presented as a set of proposed theorems, proofs, and counterexamples, not as a statement that they have been externally verified. Work classically, using the usual spatial/patch representation of stably locally compact locales and choice where necessary. No claim of literature priority is intended.

## 1. Conventions and statement of the problem

For a locale \(X\), write \(X^2=X\times_{\mathrm{Loc}}X\) and let \(\Delta_X\hookrightarrow X^2\) be its diagonal. In the coframe of sublocales of \(X^2\) put
\[
\begin{aligned}
\mathcal I_X&=\operatorname{cl}_{X^2}\Delta_X,
&\mathcal D_X&=\operatorname{fit}_{X^2}\Delta_X,\\
\mathcal V_X&=\operatorname{fit}_{X^2}\mathcal I_X,
&\mathcal W_X&=\operatorname{cl}_{X^2}\mathcal D_X,\\
\mathcal M_X&=\mathcal I_X\wedge\mathcal D_X.
\end{aligned}\tag{1.1}
\]
Here \(\operatorname{fit}\) means the intersection of all open sublocales containing the given sublocale. If \(P\) is a subset of a sober space \(Z\), then \([P]\) means the **least sublocale of \(Z\) containing all points of \(P\)**, equivalently the locale induced by the subspace topology on \(P\). It is not legitimate to infer \(\operatorname{pt}[P]=P\) for an arbitrary \(P\).

The order convention is
\[
x\le y\quad\Longleftrightarrow\quad x\in\overline{\{y\}},
\]
so opens are upper sets. Sublocale inclusion is \(\le\). All products of displayed relations refer to products of their embeddings as **locales**, followed by the canonical square identification \((X\times Y)^2\cong X^2\times Y^2\).

Two categorical constructions must be distinguished:

* A **locale product** \(X\times_{\mathrm{Loc}}Y\) corresponds to a **frame coproduct** \(\mathcal O(X)\oplus_{\mathrm{Frm}}\mathcal O(Y)\).
* A **frame direct product** \(\prod_i\mathcal O(X_i)\) corresponds to a **locale coproduct** \(\coprod_iX_i\). This is **not** an infinitary locale product.

The proposed inventory, subject to independent audit, is:

| Relation | Binary locale product for stably locally compact factors | Arbitrary frame direct product |
|---|---|---|
| \(\mathcal I\) | Exact | Exact for all locales |
| \(\mathcal D\) | Lax inclusion; can be strict | Exact for all locales |
| \(\mathcal V\) | Lax inclusion; can be strict; exact if one factor stably compact | Exact for all locales |
| \(\mathcal W\) | Exact | Exact for all locales |
| \(\mathcal M\) | Lax inclusion; proposed strict example | Exact for all locales |

We make **no claim** about completely unrestricted locale-product preservation or arbitrary infinite locale products.

## 2. Previously established input: stably locally compact point formulas

A stably locally compact (SLC) space here means a sober locally compact coherent space; stable compactness means SLC plus compactness. Its patch space is locally compact Hausdorff with closed specialization order. A localic finite product of SLC spaces is spatial and has the ordinary product topology, and it is SLC.

For SLC \(X\), define subsets of the *spatial* square \(X^2\) by
\[
\begin{aligned}
P_X^-&=\{(x,y):\exists r\in X\quad r\le x\text{ and }r\le y\},\\
P_X^+&=\{(x,y):\exists s\in X\quad x\le s\text{ and }y\le s\},\\
T_X&=\uparrow_{X^2}P_X^+.
\end{aligned}\tag{2.1}
\]
We use the following **SC+ point-induced and saturation theorem as a prerequisite**, not as a new result to be established from the product arguments:
\[
\boxed{\begin{aligned}
\mathcal I_X&=[P_X^+],&\quad \mathcal D_X&=[P_X^-],\\
\mathcal V_X&=[T_X],&\quad \mathcal W_X&=[\overline{P_X^-}].
\end{aligned}}\tag{2.2}
\]
The closure is ordinary topological closure in \(X^2\). More generally, for SLC sober \(Z\) and any subset \(B\subseteq Z\),
\[
\operatorname{fit}_Z([B])=[\uparrow_ZB].\tag{2.3}
\]
The reasoning behind these prerequisites is: \(\mathcal I\) is closed and its points are precisely inseparable pairs, equivalently pairs with a common upper bound (compact-saturated-neighborhood intersection argument); \(\mathcal D\) is the fitted hull of the diagonal, so (2.3) identifies it with the upward closure of diagonal points, i.e. \(P^-\); the same lemma applied to \(\mathcal I\) gives \(\mathcal V\); finally closure of a point-induced sublocale agrees with closure of its generating points. The SC+ proof of (2.3) uses compact saturated neighborhoods, the patch-closed specialization order and a nucleus calculation. These prerequisites were developed separately; the referee should check their **use** but need not reproduce their earlier proof.

Under coordinatewise specialization in a product, the point sets satisfy
\[
\boxed{P_{X\times Y}^-=P_X^-\times P_Y^-,\quad
P_{X\times Y}^+=P_X^+\times P_Y^+,\quad
T_{X\times Y}=T_X\times T_Y.}\tag{2.4}
\]
For the last equality, coordinatewise upper saturation of a Cartesian product is the product of the upper saturations. These are equalities of **subsets**; the point-induced notation in (2.2) is what upgrades the subsequent statements to sublocales.

## 3. Exact and lax binary locale-product formulas

**Proposition 3.1 (\(\mathcal I\)).** For SLC \(X,Y\),
\[
\mathcal I_{X\times Y}=\mathcal I_X\times\mathcal I_Y.\tag{3.1}
\]
**Proof proposed.** The diagonal of the product is the product of diagonals. Ordinary closure satisfies \(\overline{A\times B}=\overline A\times\overline B\) in a topological product. Closed embeddings of locales are stable under product. Thus both sides induce the same closed sublocale of \(X^2\times Y^2\). \(\square\)

**Theorem 3.2 (\(\mathcal W\)).** For SLC \(X,Y\),
\[
\boxed{\mathcal W_{X\times Y}=\mathcal W_X\times\mathcal W_Y.}\tag{3.2}
\]
**Proof proposed.** By (2.2), (2.4), the left side is the closed sublocale corresponding to
\[
\overline{P_X^-\times P_Y^-}=\overline{P_X^-}\times\overline{P_Y^-}.
\]
Both factors on the right in (3.2) are closed sublocales, and their product is the same closed sublocale. Hence this is an actual sublocale identity, independently of whether \(\mathcal D\) preserves the product. \(\square\)

**Proposition 3.3 (lax relations).** For SLC \(X,Y\),
\[
\boxed{\begin{aligned}
\mathcal D_{X\times Y}&\le\mathcal D_X\times\mathcal D_Y,\\
\mathcal V_{X\times Y}&\le\mathcal V_X\times\mathcal V_Y,\\
\mathcal M_{X\times Y}&\le\mathcal M_X\times\mathcal M_Y.
\end{aligned}}\tag{3.3}
\]
**Proof proposed.** The left sides for \(\mathcal D,\mathcal V\) are the least sublocales generated respectively by \(P_X^-\times P_Y^-\) and \(T_X\times T_Y\), while the proposed right sides contain these generating points. The \(\mathcal M\)-inequality follows by meeting the \(\mathcal D\)-inequality with (3.1) and using preservation of finite intersections by products of sublocale embeddings. \(\square\)

We ask the referee to check especially the use of minimality in the first two comparisons and the last step for \(\mathcal M\); pointwise inclusion alone is not sufficient in general.

## 4. An algebraic SLC space with rational cross-sheet slices

Let \(C\) be Cantor space and choose a countable dense subset \(E\subset C\); in particular \(E\) has no isolated points and is homeomorphic to \(\mathbb Q\). Take the *patch* space
\[
K=A\sqcup B\sqcup R,
\quad A=\{a_t:t\in C\}\cong C,
\quad B=\{b_t:t\in C\}\cong C,
\quad R=\{r_t:t\in E\}\text{ discrete}.
\tag{4.1}
\]
Give \(K\) the partial order generated by the strict comparisons
\[
r_t<a_t,\qquad r_t<b_t\quad(t\in E),\tag{4.2}
\]
and no others. Let \(X\) have as opens precisely the **patch-open upper subsets** of \(K\).

### 4.1 Claimed separation and compactness properties

Form the one-point compactification \(K^+=K\sqcup\{\bot\}\) and extend the order by \(\bot\le z\) for every \(z\in K^+\). Claim: its order graph is closed in the compact Hausdorff patch square. Indeed, any nonconstant family of witnesses \(r_t\) leaving every finite subset of \(R\) can accumulate only at \(\bot\), while the target coordinates of the order edges may tend to points on \(A\) or \(B\), and the limiting pairs \((\bot,z)\) are included. The remaining edges are diagonal or have an eventually fixed witness, so are closed. The compact-pospace correspondence then makes the upper topology on \(K^+\) **stably compact**. Since \(K\) is patch-open and upward closed, its upper topology \(X\) is **stably locally compact**.

Claim further: \(\mathcal O(X)\) is an **algebraic frame**. Clopen sets in the maximal Cantor sheets \(A,B\) provide a compact-open basis there. For \(r_t\), the basic opens are
\[
U_{t,V,W}=\{r_t\}\cup V_A\cup W_B,\tag{4.3}
\]
with \(V\subseteq C,W\subseteq C\) clopen neighborhoods of \(t\). Each is compact and open in the upper topology. Together these form a basis stable under finite intersections. The space is **not compact**: \(A,B\) and the witness-neighborhood family give a cover without a finite subcover.

The reader is invited to verify both the order-graph claim and the assertion that the listed neighborhoods are compact as **upper-topology** opens, not merely patch-compact sets.

### 4.2 Exact rational slices

Both \(A\) and \(B\) are upper-open subsets of \(X\), so \(U=A\times B\) is open in \(X^2\).

For a pair \((a_s,b_t)\), \(s,t\in C\), a common **lower** bound can only be a witness \(r_q\) with \(s=t=q\in E\). Thus
\[
P_X^-\cap U=\{(a_t,b_t):t\in E\}\cong\mathbb Q.\tag{4.4}
\]
There are no common **upper** bounds of \(a_s,b_t\), hence \(P_X^+\cap U=\varnothing\). But the *upward saturation* \(T_X=\uparrow P_X^+\) does intersect \(U\):
\[
\boxed{T_X\cap U=\{(a_t,b_t):t\in E\}\cong\mathbb Q.}\tag{4.5}
\]
To prove the nontrivial inclusion, suppose \((a_s,b_t)\ge(u,v)\in P_X^+\). Thus \(u\le a_s\), \(v\le b_t\), and \(u,v\) share an upper bound. Any path connecting an \(A\)-predecessor and a \(B\)-predecessor must use the **same** witness \(r_q\), whence \(s=t=q\in E\). Conversely, \((r_t,r_t)\in P_X^+\) lies below \((a_t,b_t)\).

### 4.3 An exact open sublocale, not just a rational point set

We use the following general fact for a sober space \(Z\): if \(P\subseteq Z\), \(U\hookrightarrow Z\) is an **open sublocale**, and \(C=Z\setminus U\) its complementary **closed sublocale**, then
\[
\boxed{[P]\wedge U=[P\cap U].}\tag{4.6}
\]
One proposed proof is to decompose \(P\) into its points inside \(U\) and \(C\), so that \([P]=[P\cap U]\vee[P\cap C]\); use finite distributivity of the sublocale coframe, \([P\cap U]\le U\), and \(U\wedge C=0\). Alternatively, this is the familiar compatibility of a point-induced sublocale with restriction to an **open** subspace. Equation (4.6) must not be extended to arbitrary closed intersections without proof.

By (2.2), (4.4)–(4.6), the sublocales \(\mathcal D_X\) and \(\mathcal V_X\) each have an **open sublocale isomorphic to the rational locale** \(\mathbb Q_{\mathrm{loc}}=\mathcal O(\mathbb Q)\). We have not asserted that all points of \(\mathcal V_X\) coincide with \(T_X\).

### 4.4 Proposed failure of \(\mathcal D\) and \(\mathcal V\) to preserve products

The classical theorem of Johnstone (*Stone Spaces*, Proposition II.2.14) says
\[
\mathbb Q_{\mathrm{loc}}\times_{\mathrm{Loc}}\mathbb Q_{\mathrm{loc}}\quad\text{is nonspatial}.\tag{4.7}
\]
Products of open localic embeddings are open. Therefore \(\mathcal V_X\times\mathcal V_X\) (and similarly \(\mathcal D_X\times\mathcal D_X\)) has an open **nonspatial** sublocale. Since every open sublocale of a spatial locale is spatial, the whole localic product is nonspatial.

On the other hand, (2.2) and (2.4) give
\[
\mathcal V_{X\times X}=[T_X\times T_X],\qquad
\mathcal D_{X\times X}=[P_X^-\times P_X^-].\tag{4.8}
\]
Both are spatial, because they are induced by (possibly nonsober) topological subspaces. The lax inclusions of Proposition 3.3 are consequently strict:
\[
\boxed{\mathcal V_{X\times X}\subsetneq\mathcal V_X\times\mathcal V_X,\qquad
\mathcal D_{X\times X}\subsetneq\mathcal D_X\times\mathcal D_X.}\tag{4.9}
\]
These are strict inequalities of **sublocales**; no claim is made that the two sides have identical point sets. An independent analysis of possible extra sobrification points is welcome but not needed for (4.9).

## 5. A proposed strict product example for \(\mathcal M\)

Extend the patch space \(K\) by an isolated point \(\omega\), ordered as a **greatest specialization element**, \(z\le\omega\) for every \(z\). Denote the resulting upper-topology space by \(Y\). It is claimed that adjoining a compactification bottom as in §4 again gives a compact Hausdorff patch with closed order, so \(Y\) remains SLC. The original \(X\) embeds as a **closed** subspace of \(Y\), with complement the open set \(\{\omega\}\).

Every nonempty open of \(Y\) contains \(\omega\). Hence every pair of points is inseparable, so
\[
\mathcal I_Y=Y^2,\qquad \mathcal M_Y=\mathcal D_Y.\tag{5.1}
\]
The proposed remaining argument is: no new common lower bound was added for pairs of old points, giving \(P_Y^-\cap X^2=P_X^-\). We claim the restriction of \(\mathcal D_Y=[P_Y^-]\) to the **closed** sublocale \(X^2\hookrightarrow Y^2\) is \(\mathcal D_X=[P_X^-]\), and therefore \(\mathcal D_X\) is a closed sublocale of \(\mathcal D_Y\). Its localic square \(\mathcal D_X\times\mathcal D_X\) is then a **closed sublocale** of \(\mathcal D_Y\times\mathcal D_Y\), and is nonspatial by (4.9). Closed sublocales of spatial locales are spatial, so \(\mathcal D_Y\times\mathcal D_Y\) is nonspatial. But \(\mathcal M_{Y\times Y}\), being a closed sublocale of the spatial \(\mathcal D_{Y\times Y}\), is spatial. Together with (3.3) and (5.1), this yields the proposed strictness
\[
\boxed{\mathcal M_{Y\times Y}\subsetneq\mathcal M_Y\times\mathcal M_Y.}\tag{5.2}
\]

**Particular referee request:** Please scrutinize the claimed closed-subspace restriction \([P_Y^-]\wedge X^2=[P_X^-]\). Identity (4.6) was established only for **open** intersections and does not by itself establish this closed restriction. If this step fails, we would prefer a clear negative verdict or a repair to a conditional endorsement.

## 6. Proposed positive theorem for \(\mathcal V\) with one stably compact factor

**Theorem 6.1.** If \(X\) is **stably compact** and \(Y\) is **stably locally compact**, then
\[
\boxed{\mathcal V_{X\times Y}=\mathcal V_X\times\mathcal V_Y.}\tag{6.1}
\]

**Proof proposed.** Since \(\mathcal I_X=\operatorname{cl}\Delta_X\) is closed, its point set \(P_X^+\) is closed in the original topology of \(X^2\), hence also closed in the finer Hausdorff patch topology. The patch of \(X^2\) is compact Hausdorff, with closed specialization order. Therefore the upward closure
\[
T_X=\{z\in X^2:\exists p\in P_X^+\text{ with }p\le z\}
\]
is the continuous projection of a patch-closed subset of the compact product \(P_X^+\times X^2\), so is patch-closed in \(X^2\). The standard patch-subspace theorem says that a patch-closed subspace of a stably compact space, equipped with the induced original topology, is stably compact. Consequently \(T_X\) is locally compact and sober; its induced locale \(\mathcal V_X=[T_X]\) is the locale of \(T_X\).

The subset \(T_Y\) may **not** be sober. Nevertheless, when \(T_X\) is locally compact sober, the comparison between the localic product and the ordinary product of topological spaces provides
\[
\mathcal O(T_X)\oplus\mathcal O(T_Y)\cong\mathcal O(T_X\times T_Y).\tag{6.2}
\]
Naturality for the point-induced embeddings into \(X^2,Y^2\) identifies the product embedding with \([T_X\times T_Y]\). Equation (2.4) now finishes:
\[
\mathcal V_X\times\mathcal V_Y
=[T_X\times T_Y]
=\mathcal V_{X\times Y}.
\]
\(\square\)

Please check not only that (6.2) is true, but that it is used with the **correct topology on \(T_X\)** and that the asserted naturality actually gives an equality of embedded sublocales. The hypothesis is one **stably compact** factor, not merely one SLC factor; §4 is intended to show why that distinction matters.

## 7. Unrestricted frame direct products: a different phenomenon

Let \(\{X_i:i\in I\}\) be **any** family of locales, with no spatiality, compactness, or coherence assumptions, and put
\[
Z=\coprod_{i\in I}X_i,\qquad
\mathcal O(Z)=\prod_{i\in I}\mathcal O(X_i).
\]
The product frame has the complementary coordinate idempotents \(e_i\), whose joins cover \(1\), expressing \(Z\) as a disjoint coproduct of clopen summands. Since localic products distribute over disjoint locale coproducts, the localic square has the clopen decomposition
\[
Z^2\cong\coprod_{(i,j)\in I^2}(X_i\times_{\mathrm{Loc}}X_j).\tag{7.1}
\]
The diagonal \(\Delta_Z\) restricts to \(\Delta_{X_i}\) in the \((i,i)\)-block and to the zero sublocale in every off-diagonal block.

**Theorem 7.1 (proposed).** For each relation \(\mathcal R\in\{\mathcal I,\mathcal D,\mathcal V,\mathcal W,\mathcal M\}\),
\[
\boxed{\mathcal R\!\left(\coprod_{i\in I}X_i\right)
\cong \coprod_{i\in I}\mathcal R(X_i),}\tag{7.2}
\]
as sublocales of (7.1), with the right side supported on the diagonal blocks. This includes **infinite** \(I\) and all locales. For \(I=\varnothing\), both sides are the empty locale.

**Proof proposed.** Sublocales of a disjoint clopen coproduct are determined componentwise, with componentwise order, meets, and joins. Open and closed sublocales likewise decompose componentwise. Hence taking closure and fitting of a diagonal-supported sublocale can be done block by block; an off-diagonal zero component remains zero. This gives the formulas successively for \(\mathcal I,\mathcal D\), then \(\mathcal V,\mathcal W\), and finally \(\mathcal M\). \(\square\)

This is preservation of **frame products** in dual language. In particular, it does **not** assert preservation of arbitrary infinite locale products. Please test whether infinite coproducts introduce any subtlety not covered by the block argument.

## 8. Scope, references and explicit uncertainty

We ask for a verdict on every row of the inventory in §1. In particular, the \(\mathcal M\) counterexample in §5 depends on a closed-restriction assertion whose justification should be tested independently. The primary structural dependencies are (2.2)–(2.3), the nonspatial rational localic square, and classical compact-pospace/localic-product comparison facts. No proof of point-set equality \(\operatorname{pt}[T_X]=T_X\) is assumed. There is no claim yet about preservation for \(\mathcal U,\mathcal J,\mathcal H\), or converses to Theorem 6.1.

External references for independent verification:

1. P. T. Johnstone, *Stone Spaces*, Cambridge Studies in Advanced Mathematics 3 (1982), II.2.13–14 and III.1.4; especially II.2.14 on the nonspatial localic square of \(\mathbb Q\).
2. A. Jung, M. Kegelmann, M. A. Moshier, [*Stably compact spaces and closed relations*](https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf), Theorem 2.5, for the compact-pospace and upper-topology equivalence.
3. A. Jung, [*Stably compact spaces and the probabilistic powerspace construction*](https://achimjungbham.github.io/pub/papers/scs.pdf), for patch constructions and stably compact subspaces.
4. Earlier Project A SC+ canonical theorem (15 November 2026): the input consists precisely of formulas (2.2)–(2.3), which have been restated above so that this packet can be read without consulting the repository. The packet's review should be independent of Project A's internal product-preservation audit.

**End of blind packet.**
