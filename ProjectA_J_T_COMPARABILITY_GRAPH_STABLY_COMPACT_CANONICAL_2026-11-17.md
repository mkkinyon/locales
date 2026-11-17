# Project A — The join \(\mathcal J\), the hull \(\mathcal T\), and comparability graphs

**Consolidation date:** 17 November 2026. **Status:** internally checked working theorem, extending the finite-Alexandrov and coherent arguments to **stably compact locales**. The coherent step has received an internal adversarial audit; the perfect-nucleus proof below removes its most delicate compact-open approximation step. **This particular consolidated extension has not undergone an independent blind audit.** No claim of priority or novelty is made.

## 1. Conventions and scope

Work classically, with sublocales ordered by inclusion. For a locale \(X\), put \(Y=X\times_{\mathrm{Loc}}X\), with diagonal \(\Delta\hookrightarrow Y\), and define

\[
\begin{aligned}
\mathcal I&=\operatorname{cl}\Delta,&
\mathcal D&=\operatorname{fit}\Delta,\\
\mathcal V&=\operatorname{fit}\mathcal I,&
\mathcal W&=\operatorname{cl}\mathcal D,\\
\mathcal J&=\mathcal I\vee\mathcal D,&
\mathcal T&=\mathcal V\wedge\mathcal W.
\end{aligned}\tag{1}
\]

Here \(\operatorname{cl}\) is the smallest **closed sublocale** containing an argument; \(\operatorname{fit}\) is the smallest **fitted sublocale** containing it. Recall that the universal hull operator on arbitrary sublocales is
\[
\mathbf T(S)=\operatorname{cl}(S)\wedge\operatorname{fit}(S).
\]
Thus the notation \(\mathcal T\) in (1) agrees with \(\mathbf T(\mathcal J)\), because universally
\[
\operatorname{cl}\mathcal J=\mathcal W,\qquad
\operatorname{fit}\mathcal J=\mathcal V.\tag{2}
\]
These are **sublocale** joins and meets, not set-theoretic unions or intersections by fiat.

An important product convention remains in force: \(\mathcal O(Y)=\mathcal O(X)\oplus\mathcal O(X)\) is a **frame coproduct**. A frame direct product instead corresponds to a locale coproduct. All statements here concern the localic square, not a frame direct product.

For the main theorem, \(X\) is **stably compact** (compact, locally compact, sober, and coherent in the topological sense). In particular, its localic square is spatial and its point space is the ordinary topological square. Write \(P=\operatorname{pt}(X)\) and use specialization order
\[
x\le y\quad\Longleftrightarrow\quad
\text{every open neighborhood of }x\text{ contains }y.
\tag{3}
\]
We use the product order on \(P^2\) and write \(\uparrow K,\downarrow K\) for its order up- and down-closures. Let \(\delta=\{(x,x):x\in P\}\).

## 2. Main localic theorem

**Theorem (stably compact graph theorem).** For every stably compact locale \(X\), all six sublocales in (1) are **perfect** (their nuclei preserve directed joins), hence spatial and stably compact. They are therefore determined by their point sets, which are

\[
\begin{aligned}
\operatorname{pt}(\mathcal I)&=\downarrow\delta
  =\{(x,y):\exists z\ (x\le z\ \&\ y\le z)\},\\
\operatorname{pt}(\mathcal D)&=\uparrow\delta
  =\{(x,y):\exists z\ (z\le x\ \&\ z\le y)\},\\
\operatorname{pt}(\mathcal V)&=\uparrow\downarrow\delta,\\
\operatorname{pt}(\mathcal W)&=\downarrow\uparrow\delta,\\
\operatorname{pt}(\mathcal J)&=\downarrow\delta\ \cup\ \uparrow\delta,\\
\operatorname{pt}(\mathcal T)&=\uparrow\downarrow\delta\ \cap\ \downarrow\uparrow\delta.
\end{aligned}\tag{4}
\]

If \(X\) is coherent/spectral, all six are again coherent/spectral. The theorem genuinely concerns the **sublocales**, not merely their ordinary points.

**Proof, with the previously audited delicate step isolated.**

1. A stably compact space \(P\) has compact Hausdorff **patch** topology and a patch-closed specialization order. Its localic product is represented by the ordinary topological product, which is again stably compact. The diagonal \(\delta\) is patch closed. If \(K\subseteq P^2\) is patch closed, then \(\downarrow K\) is the ordinary closure of \(K\): the lower set is ordinary closed (the order is patch closed and projecting along compact \(K\) preserves patch closedness), and every ordinary closed set is specialization-lower. This gives the first line of (4).

2. The diagonal sublocale is compact because it is isomorphic to \(X\); its closure \(\mathcal I\) is compact because it is closed in compact \(Y\). Fitting a compact sublocale gives a **compact fitted** sublocale (Jakl–Suarez, Theorem 6.11), so \(\mathcal D=\operatorname{fit}\Delta\) and \(\mathcal V=\operatorname{fit}\mathcal I\) are compact fitted.

3. By the pointfree Hofmann–Mislove correspondence, compact fitted sublocales correspond to Scott-open filters. For stably locally compact locales the resulting fitted nuclei are **perfect** (Escardó, *regular-locally-compact coreflection*, Lemma 5.1). Thus \(\mathcal D\) and \(\mathcal V\) are perfect. The nuclei of closed sublocales are perfect: the closed nucleus \(u\mapsto a\vee u\) even preserves all joins. Thus \(\mathcal I\) and \(\mathcal W\) are perfect. Perfect nuclei constitute a **subframe** of all nuclei (Escardó, *coreflection*, §2; *Properly injective spaces*, Lemma 3.1.8). Since sublocale order reverses nucleus order, finite joins and meets of these sublocales remain perfect, giving \(\mathcal J\) and \(\mathcal T\).

4. A perfect sublocale of a spatial locale is spatial **classically** (Escardó, *Properly injective spaces*, Theorem 3.1.4, whose proof uses Zorn's lemma). Perfect sublocales of stably locally compact and spectral locales retain those properties (ibid., Theorem 3.1.7); compactness is likewise retained. Thus all the sublocales above are spatial and stably compact, coherent when \(X\) is coherent.

5. For a **spatial** sublocale \(S\), the points of \(\operatorname{fit}S\) are the intersection of all open neighborhoods of its point set, namely its specialization-upward saturation. We apply this only to the spatial sublocales \(\Delta\) and \(\mathcal I\). The points of a sublocale meet are an intersection of point sets. For the join \(\mathcal J\), extra care is needed: in general one cannot assert that *every* join of spatial sublocales has precisely the union of their point sets. Here, however, \(\downarrow\delta\) and \(\uparrow\delta\) are **patch closed**; their finite union is patch closed and thus a stably compact (in particular sober) subspace. The spatial join therefore has exactly this union as its points. Applying these observations gives the remaining four lines of (4). All the displayed supports are patch closed, by the patch-closed order and compact projection.

The same perfect-nucleus argument avoids assuming that an arbitrary meet of spatial sublocales is spatial. That was a chief potential gap in informal coherent treatments. \(\square\)

**Duality.** Reversing the specialization order through the de Groot dual of a stably compact space (Hochster dual in the coherent case) exchanges the two point relations \(\mathcal I\leftrightarrow\mathcal D\), and \(\mathcal V\leftrightarrow\mathcal W\), while preserving the descriptions of \(\mathcal J\) and \(\mathcal T\). This compares relations on **different dual localic squares**; it is not a literal equality of sublocales in a single frame.

## 3. Graph-theoretic form

Let \(G=G(P)\) be the *undirected comparability graph*: distinct \(x,y\) are joined when \(x\le y\) or \(y\le x\). Write \(d(x,y)\) for its graph distance, \(\infty\) for disconnected vertices, and \(G^k=\{(x,y):d(x,y)\le k\}\), including the diagonal. We identify these graph relations with **spatial** sublocales only under the hypotheses of §2.

**Corollary.** On a stably compact locale,

\[
\boxed{\mathcal J=G^2,\qquad G^3\subseteq\mathcal T\subseteq G^4.}\tag{5}
\]

Indeed, a path of length two has a common upper or a common lower middle vertex, perhaps after collapsing consecutive order-comparable steps using transitivity. Conversely each common upper/lower witness gives a two-edge path. For \(\mathcal T\), the conditions in (4) furnish paths of length at most four. Every three-edge comparability path contributes to both \(\uparrow\downarrow\delta\) and \(\downarrow\uparrow\delta\); consecutive arrows in the same direction shorten by transitivity, while an alternating three-edge path admits the two needed order witnesses. The claim can also be checked directly against (4).

In particular,

\[
\boxed{\mathcal J=\mathcal T\quad\Longleftrightarrow\quad
\text{every connected component of }G\text{ has diameter at most }2.}\tag{6}
\]

The implication from right to left follows from (5), and if a component has diameter at least three it has a pair at distance exactly three, lying in \(\mathcal T\setminus\mathcal J\). Thus \(\mathcal J\) is a fixed point of the universal closed-and-fitted hull \(\mathbf T\) exactly when the graph has this diameter bound.

### The precise distance-four fringe

For \(d(x,y)=4\), any four-edge shortest path must alternate specialization directions. The conditions are:

- \((x,y)\in\mathcal V\) iff a geodesic starts **downward**: \(x>u<z>v<y\).
- \((x,y)\in\mathcal W\) iff a geodesic starts **upward**: \(x<u>z<v>y\).
- Consequently \((x,y)\in\mathcal T\) iff **both** starting orientations occur among geodesics.

This criterion is independent of which orientation we initially choose: reversing the poset exchanges the two requirements.

There is even a **graph-only** test. For \(d(x,y)=4\), set

\[
\begin{aligned}
A_{xy}&=\{u:d(x,u)=1,\ d(u,y)=3\},\\
B_{xy}&=\{z:d(x,z)=d(z,y)=2\},\\
M(u)&=N_G(u)\cap B_{xy}\quad(u\in A_{xy}).
\end{aligned}\tag{7}
\]

Then

\[
\boxed{(x,y)\in\mathcal T\iff
\exists u,r\in A_{xy}:\ u\sim r,\quad
M(u)\not\subseteq M(r),\quad M(r)\not\subseteq M(u).}\tag{8}
\]

For proof, a middle neighbor \(z\in M(u)\) extends \(x-u-z\) to a length-four geodesic. If \(u,r\) are comparable and lie on the **same** side of \(x\), transitivity makes the corresponding middle-neighbor sets nested; so nonnesting forces them to lie on opposite sides, giving the two orientations. Conversely, two opposite-start geodesics give \(u<x<r\), hence \(u\sim r\), and neither middle-neighbor set can contain the other: otherwise a shared or cross-attached middle vertex would make a directed two-step segment, shortcutting a four-edge geodesic. This establishes (8), with no finiteness assumption on \(G\).

**Examples.** The four-point fence \(0<1>2<3\) has \(d(0,3)=3\), so \((0,3)\in\mathcal T\setminus\mathcal J\). Distance-four membership can go either way: a simple length-four fence supplies a pair outside \(\mathcal T\), whereas the eight-point poset generated by
\[
u<x<r,\quad u<z,\quad v<z,\quad v<y<s,\quad t<r,\quad t<s
\]
has \(d(x,y)=4\) with both paths \(x>u<z>v<y\) and \(x<r>t<s>y\), so \((x,y)\in\mathcal T\).

**Finite sanity check (not a substitute for proof).** An exhaustive check of 5,231 naturally labelled posets on at most six vertices, covering 183,301 ordered vertex pairs, found no exception to (5), (6), or (8). This check only corroborates the combinatorial proofs.

## 4. Why the stably compact hypothesis matters

Take the **circle with doubled origin**: form \(X\) from two copies of \(S^1\) by identifying corresponding points except for one marked point, which is retained as \(o_0,o_1\). This \(X\) is compact, \(T_1\), locally Hausdorff (hence sober and locally compact), but not Hausdorff or stably compact. Its specialization order is equality, so its comparability graph consists of isolated vertices and \(G^2=\Delta\).

Nevertheless every neighborhood of \(o_0\) meets every neighborhood of \(o_1\), which places \((o_0,o_1)\) in the ordinary closure of the diagonal of \(X\times X\):
\[
(o_0,o_1)\in\operatorname{pt}(\mathcal I)\setminus G^2.
\]
Thus even the first equality in (5) can fail in compact, locally compact, sober \(T_1\) spaces. The compact-pospace/patch-closed-order mechanism is substantive, not cosmetic.

## 5. Internal audit and precise boundaries

1. **Sublocale versus support.** Point-set joins/intersections alone cannot prove sublocale identities. The crucial additional assertion is *perfectness*, then spatiality, of \(\mathcal I,\mathcal D,\mathcal V,\mathcal W,\mathcal J,\mathcal T\). Without it, (4) is only a support calculation.
2. **The coherent approximation gap.** An earlier coherent route described a fitting as a meet of compact-open sublocales and invoked limits. It requires checking all compactness, cofilteredness, and coherence assertions. The compact-fitting/Scott-continuous-nucleus argument in §2 is the preferred proof.
3. **The two product notions.** This theorem uses the **locale** square and spatiality of its product. It says nothing automatically about frame direct products or arbitrary infinite locale products, whose separate results are recorded elsewhere.
4. **Classical spatiality.** Escardó's theorem that a finitary/perfect sublocale of a spatial locale is spatial uses choice. Do not silently promote the claim to a constructive setting.
5. **Distance four is conditional.** \(\mathcal T\) is generally *not* all of \(G^4\); both initial geodesic orientations are required. Nor is it just \(G^3\) in all examples.
6. **No broad noncompact extension claimed.** Some point formulas for \(\mathcal I,\mathcal D,\mathcal V,\mathcal W\) extend to stably locally compact spaces, but compactness of the diagonal and its closure was used here to obtain perfect fittings. The exact sublocale graph theorem for arbitrary noncompact stably locally compact locales remains a separate question.

**Further work.** (a) Determine the weakest useful hypotheses under which \(\mathcal J\) and \(\mathcal T\) are perfect/spatial; (b) test whether the graph-only characterization survives on larger stably locally compact classes or only describes the spatial parts; (c) investigate whether the distance-four fringe defines a familiar undirected graph operation or a natural closure system.

## 6. Primary references and project connections

- M. H. Escardó, *Properly injective spaces and function spaces*, [author PDF](https://martinescardo.github.io/papers/injective.pdf), especially Theorems 3.1.4, 3.1.7 and Lemma 3.1.8 (the paper uses “finitary” for Scott-continuous/perfect nuclei).
- M. H. Escardó, *The regular-locally-compact coreflection of a stably locally compact locale*, [author PDF](https://www.cs.bham.ac.uk/~mhe/papers/patch-full.pdf), especially §2 and Lemma 5.1.
- T. Jakl and A. L. Suárez, *Canonical extensions via fitted sublocales*, [journal article](https://link.springer.com/article/10.1007/s10485-025-09802-6), especially Proposition 6.9 and Theorem 6.11.
- A. Jung, M. Kegelmann and M. A. Moshier, *Stably compact spaces and closed relations*, [PDF](https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf), for the compact-pospace/patch representation.
- [Earlier Project A meet/join foundation](A-I-D-meet-join-frame-theory-2026-10-21.md), [finite \(\mathcal J\) fixed-point result](A-J-fixedpoint-compositions-coproduct-2026-10-21.md), [Hochster duality](A-Hochster-duality-I-D-2026-10-21.md), and [post-referee product canonical note](ProjectA_LOWER_PRODUCTS_POSTREFEREE_CANONICAL_2026-11-17.md).

