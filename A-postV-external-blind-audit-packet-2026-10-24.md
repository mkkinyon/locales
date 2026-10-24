# Project A — Blind audit packet: the formal upper hull, the two diamonds, and graph connectivity

**Prepared 24 October 2026.**  
**For an independent mathematical referee.** All statements described as “claimed” or “proposed” below are **working claims to test**. It is intended to be readable without access to earlier project conversations.

## 0. Why these questions arose

The motivating source is Cameron–Kumar, *Graphs on topological spaces* (arXiv:2610.14783). A project initiated from a universal-algebra/locale perspective now studies a family of localic binary relations on \(X\). Earlier coherent-locale work produced
\[
\mathcal U=\operatorname{cl}(\mathcal D)=\mathcal I\circ\mathcal I,
\qquad
\mathcal V=\operatorname{fit}(\mathcal I)=\mathcal D\circ\mathcal D.
\]
The first equality does **not** hold in arbitrary noncoherent locales. This is why the formal cross-hull \(\mathcal W=\operatorname{cl}(\mathcal D)\) must be distinguished from the original Urysohn relation \(\mathcal U\), and why the formal fitted companion \(\mathcal V\) may not capture every aspect of a genuinely intrinsic dual to \(\mathcal U\).

The present packet focuses on the **formal hull \(\mathcal H\)** and the upper/lower diamonds, not on the earlier substantial \(\mathcal V\)-rank investigation. The organizing question is how much of undirected graph connectivity survives when graph vertices and relational closure are interpreted pointfreely, and what changes when specialization comparisons, fitted hulls, closed hulls, and topological limits interact.

The requests for verification are integrated into the statements. Please issue **independent verdicts for individual claims**, rather than a single global score.

## 1. Standing definitions and background

Let \(L=\mathcal O(X)\) be a frame and \(Q=L\oplus L\) its coproduct, the frame of the localic square \(X\times_{\mathrm{loc}}X\). Its generators are rectangles \(a\boxtimes b\). Let \(\Delta\) be the diagonal sublocale. Write \(C(d)\) for the closed sublocale whose nucleus is \(x\mapsto d\vee x\), and \(O(w)\) for the open sublocale with nucleus \(x\mapsto w\to x\). Sublocale inclusion is the **opposite** of nucleus order.

Define
\[
\begin{aligned}
d_{\mathcal I}&=\bigvee_{a\wedge b=0}a\boxtimes b,
&\mathcal I&=\operatorname{cl}\Delta=C(d_{\mathcal I}),\\
d_{\mathcal U}&=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
&\mathcal U&=C(d_{\mathcal U}),\\
\mathcal D&=\operatorname{fit}\Delta,
&\mathcal V&=\operatorname{fit}(\mathcal I),\\
\mathcal W&=\operatorname{cl}(\mathcal D),
&\mathcal F&=\bigwedge_{f:X\to\mathbb R}\ker(f),\\
\mathcal M&=\mathcal I\wedge\mathcal D,
&\mathcal J&=\mathcal I\vee\mathcal D.
\end{aligned}
\]
Here \(a^*\) is the Heyting pseudocomplement of \(a\) in \(L\). The fitted hull of a sublocale \(S\) is the intersection of **all open sublocales containing \(S\)**. Define
\[
T(S)=\operatorname{cl}(S)\wedge\operatorname{fit}(S),
\]
and let \(\mathcal H\) be the *least* sublocale containing \(\Delta\) that is both closed and fitted.

Previously established universal containments being used include
\[
\Delta\subseteq\mathcal I,\mathcal D\subseteq\mathcal J
\subseteq\mathcal U,\mathcal V\subseteq\mathcal F,
\qquad \mathcal W\subseteq\mathcal U.
\]
The equality \(\mathcal U=\mathcal W\) is available in the coherent case only. If the referee sees a hidden reliance on that equality outside coherence, it is a serious defect.

### Elementary point formulas: please verify

For a topological space with specialization order \(\le\), the proposed point interpretations in its ordinary/localic product are:

* \((x,y)\in\operatorname{pt}(\mathcal I)\) iff every pair of neighborhoods of \(x,y\) intersects.
* \((x,y)\in\operatorname{pt}(\mathcal D)\) iff there exists a **common specialization predecessor** \(z\le x,y\).
* \((x,y)\in\operatorname{pt}(\mathcal U)\) iff the closures of every neighborhood of \(x\) and every neighborhood of \(y\) intersect.
* \(\mathcal V\) is fitted, hence its ordinary points are upward closed under specialization; \(\mathcal I\subseteq\mathcal V\).

For the \(\mathcal D\) formula: a common predecessor \(z\) forces any diagonal neighborhood containing \((z,z)\) to contain \((x,y)\). If none exists, for each \(z\in X\) choose an open \(U_z\ni z\) excluding at least one of \(x,y\). Then \(\bigvee_z U_z\boxtimes U_z\) is a genuine open neighborhood of \(\Delta\) omitting \((x,y)\). This is a point formula, not an unqualified sublocale equality.

### Standard representation results used as inputs

**R1 (localic products).** If the factors are locally compact sober topological spaces, the localic product is spatial and identifies with their ordinary product.

**R2 (scattered sublocales).** For a sober scattered space, all sublocales of its open frame are spatial and uniquely represented by appropriate subspaces; in particular, sublocales of a scattered spatial locale are determined by their ordinary points. A finite product of scattered spaces is scattered.

**R3 (Priestley/coherent).** A coherent frame has a spectral point space \(P\) with compact zero-dimensional Hausdorff patch topology and patch-closed specialization order; spectral opens are patch-open upsets. Products remain coherent, and the patch topology of the spectral product agrees with the product patch topology. Spectral closed subsets correspond to patch-closed downsets.

**R4 (compact-open filtered fitted sublocales).** If \(K\) is the distributive lattice of compact opens of a spectral space, then a filter \(G\subseteq K\) defines a fitted intersection \(\bigcap_{u\in G}O(u)\), represented by an appropriate quotient/congruence of \(K\). In this specific compact-open-filter setting the resulting sublocale is claimed coherent and spatial, with points the prime filters containing \(G\). Do not silently extend this claim to arbitrary fitted sublocales.

Classical references for R1–R4 include Picado–Pultr (frame coproducts and sublocales), standard Priestley/Hochster duality, Ball–Picado–Pultr (2016) Proposition 5.3, Suarez (2022) on scattered spaces and sublocales, and Jakl–Suarez (2025) on fitted sublocales. The exact hypotheses and applicability of these results should be independently checked.

## 2. Universal hull identities and the upper-diamond correction

The following are proposed **for all locales**:
\[
\boxed{\mathcal W\vee\mathcal V\subseteq\mathcal H\subseteq\mathcal F,}
\qquad
\boxed{T(\mathcal J)=\mathcal W\wedge\mathcal V\subseteq\mathcal U\wedge\mathcal V,}
\]
\[
\boxed{\operatorname{cl}(\mathcal W\vee\mathcal V)=\operatorname{cl}(\mathcal V),\quad
\operatorname{fit}(\mathcal W\vee\mathcal V)=\operatorname{fit}(\mathcal W).}
\]
For example, a closed fitted superrelation of \(\Delta\) contains \(\mathcal D\) and its closure \(\mathcal W\), and contains \(\mathcal I\) and its fitting \(\mathcal V\). The mutual cross-hull absorption follows from \(\mathcal D\subseteq\mathcal V\) and \(\mathcal I\subseteq\mathcal W\).

The project explicitly **does not** claim \(\mathcal U\vee\mathcal V\subseteq\mathcal H\) universally; the examples below propose to disprove both possible comparisons between those expressions.

## 3. Coherent \(\mathcal H\) and \(\mathcal F\) as graph completions

Let \(X\) be coherent and \(P\) its spectral point space. Write \(x\sim_c y\) if there is a **finite** undirected path joining them in the comparability graph of the specialization order. A relation \(S\subseteq P^2\) is *coordinatewise comparability-saturated* if whenever \((x,y)\in S\), replacing either coordinate by a comparable point preserves membership; finite iterations then saturate entire components.

**Claim C1.** The ordinary point relation of \(\mathcal H\) is
\[
\boxed{
\operatorname{pt}(\mathcal H)=
\bigcap\{S\subseteq P^2:S\text{ patch-closed, coordinatewise comparability-saturated, and }\Delta_{\rm pt}\subseteq S\}.}
\]
Each such relation is asserted to represent a genuine closed-and-fitted sublocale.

**Sketch of the key point-to-sublocale lemma:** If \(S\) is patch-closed and an upset, then for each \(p\notin S\), \(s\not\le p\) for every \(s\in S\). Priestley separation gives, for each \(s\), a patch-clopen upset \(U_s\ni s\) with \(p\notin U_s\). Compactness of \(S\) yields finitely many \(U_s\) covering \(S\), producing one compact-open upset containing \(S\) but excluding \(p\). The intersection of the corresponding open sublocales is fitted; R4 is used to make it spatial/coherent and identify its point set with \(S\). If \(S\) is also spectral-closed, its closed sublocale has the same embedded points, hence is fitted.

**Claim C2.** The ordinary point relation of \(\mathcal F\) is the *least patch-closed equivalence relation containing* \(\sim_c\):
\[
\boxed{
\operatorname{pt}(\mathcal F)=
\bigcap\{E\subseteq P^2:E\text{ patch-closed equivalence},\ \sim_c\subseteq E\}.}
\]
One direction follows because continuous real-valued maps are patch-continuous and constant on comparable points. Conversely, any patch-closed equivalence \(E\) has compact Hausdorff quotient \(P_{\rm patch}/E\). A continuous real-valued function separating two distinct quotient classes pulls back to a patch-continuous function constant on comparison classes. Its inverse images of real opens are patch-open upsets and therefore spectral-open, giving a genuine continuous map \(X\to\mathbb R\).

**Claim C3.** For every coherent locale,
\[
\boxed{\mathcal H\text{ is internally transitive}\iff \mathcal H=\mathcal F.}
\]
If internal transitivity holds, the point relation of the closed \(\mathcal H\) is itself a patch-closed equivalence relation containing \(\sim_c\), so C2 gives \(\mathcal F\subseteq\mathcal H\) by point-determination of closed sublocales; the reverse universal inclusion is \(\mathcal H\subseteq\mathcal F\). The reverse implication uses the kernel-pair nature of \(\mathcal F\).

**Audit requests:** Are C1–C3 correct as actual locale claims? Does R4 apply as stated? Where exactly is compactness of the patch space used? Does every passage from point relations to localic inclusions have sufficient support?

## 4. Coherent counterexample: two zigzag rays accumulating at one point

Set \(P=A\sqcup B\sqcup\{t\}\), with \(A=\{a_n:n\ge0\}\) and \(B=\{b_n:n\ge0\}\). Put the *patch topology* of the one-point compactification of the discrete set \(A\cup B\): every ray vertex is isolated and every neighborhood of \(t\) contains all but finitely many ray vertices.

Order each ray by
\[
a_{2n}<a_{2n+1},\qquad a_{2n+2}<a_{2n+1},
\]
and likewise \(b_{2n}<b_{2n+1}\), \(b_{2n+2}<b_{2n+1}\). There are no other strict comparisons, and \(t\) is comparable only to itself. This is claimed a Priestley space: strict order pairs involving unbounded indices converge only to \((t,t)\), and the usual clopen-upset separation holds. Give it the associated spectral topology.

Define
\[
R=(A\cup\{t\})^2\cup(B\cup\{t\})^2.
\]
**Claim R1:** As a genuine sublocale of the coherent square, \(R\) is **closed and fitted**. It is spectral closed because its complement \((A\times B)\cup(B\times A)\) is spectral open; its patch point set is a closed union of two closed rectangles, and it is upward saturated because comparisons never cross the three graph components.

**Claim R2:** \(\mathcal H=R\). Minimality gives \(\mathcal H\subseteq R\). Every closed fitted relation containing \(\Delta\) is saturated under moving along comparisons in either coordinate, so it contains \(A^2\), \(B^2\), and \((t,t)\). Since it is closed, patch limits force \(A\times\{t\}\), \(\{t\}\times A\), \(B\times\{t\}\), and \(\{t\}\times B\). Hence \(R\subseteq\mathcal H\).

**Claim R3:** \(\mathcal H\) is *not internally transitive*: \((a_0,t),(t,b_0)\in\mathcal H\), but \((a_0,b_0)\notin\mathcal H\). The ordinary triple \((a_0,t,b_0)\) is a point of the composable-pair pullback, whose relational image has an endpoint outside \(\mathcal H\).

**Claim R4:** \(\mathcal F\) is the whole localic square. A real-valued continuous function is constant along each zigzag by specialization and has equal constants on the two rays by convergence to \(t\) in the patch topology.

**Claim R5:** \(\mathcal U\vee\mathcal V\subsetneq\mathcal H\). In coherent locales \(\mathcal U=\mathcal I^2\), \(\mathcal V=\mathcal D^2\). Their point relations remain inside \(K=A^2\cup B^2\cup\{(t,t)\}\). Both are patch-closed (\(\mathcal U\) because closed, \(\mathcal V\) by compact projection of the closed order/common-lower relation). Fix \(p=(a_0,t)\in\mathcal H\). No \(k\in\operatorname{pt}(\mathcal U)\cup\operatorname{pt}(\mathcal V)\) satisfies \(k\le p\) in the product order. Compact Priestley separation therefore supplies a patch-clopen product-upset \(W\) containing those two compact point sets but excluding \(p\). Since the two sublocales are respectively closed/spatial and fitted/coherent/spatial, this is claimed to give genuine \(\mathcal U,\mathcal V\subseteq O(W)\) and hence \(p\notin\mathcal U\vee\mathcal V\).

The proposed exact chain is
\[
\boxed{\mathcal U\vee\mathcal V\subsetneq\mathcal H\subsetneq\mathcal F,\qquad
\mathcal H\circ\mathcal H\not\subseteq\mathcal H.}
\]

**Audit:** Every part R1–R5, especially fittedness of \(R\), localic strictness of the join, and the internal rather than merely pointwise transitivity failure.

## 5. Formal closed-and-fitted hull: arbitrary frame recursion

For any frame \(Q\), define
\[
F_a=\{w\in Q:a\vee w=1\},\quad
\operatorname{Fix}_a=\{x\in Q:\forall w\in F_a,\ w\to x=x\},\quad
\kappa(a)=\bigwedge\operatorname{Fix}_a.
\]
The fitted hull \(\operatorname{fit}(C(a))=\bigcap_{w\in F_a}O(w)\) has frame \(\operatorname{Fix}_a\). Its bottom is \(\kappa(a)\), so its closed hull is \(C(\kappa(a))\). Therefore the claims are
\[
\kappa(a)\le a,\quad a\le b\Rightarrow\kappa(a)\le\kappa(b),\quad
\kappa(a)=a\iff C(a)\text{ is fitted}.
\]

Start from \(d=d_{\mathcal I}\) in the localic square and define
\[
a_0=d,\quad a_{\alpha+1}=\kappa(a_\alpha),\quad
 a_\lambda=\bigwedge_{\beta<\lambda}a_\beta\quad(\lambda\text{ limit}).
\]
The descending chain eventually stabilizes, and the working theorem asserts
\[
\boxed{\mathcal H=C(a_\infty).}
\]
Any closed fitted \(C(b)\) containing \(\Delta\) has \(b\le d\) and is a fixed point of \(\kappa\). Induction yields \(b\le a_\alpha\) for all ordinals \(\alpha\), so the stable closed sublocale is minimal.

**Important limit-stage distinction:** \(C(a_\lambda)\) is the **closed hull** of the sublocale join \(\bigvee_{\beta<\lambda} C(a_\beta)\); the bare join of infinitely many closed sublocales may not be closed.

### Coherent graph recurrence

For coherent \(X\), let \(S_\alpha\subseteq P^2\) be the point relation of \(C(a_\alpha)\). The proposed exact formulas are
\[
\boxed{
S_0=\mathcal I_{\rm pt},\quad
S_{\alpha+1}=\downarrow\uparrow S_\alpha,\quad
S_\lambda=\downarrow\operatorname{cl}_{\rm patch}\left(\bigcup_{\beta<\lambda}S_\beta\right).}
\]
On a Priestley space, \(\mathcal I_{\rm pt}\) is the common-upper relation. For any \(R\subseteq P^2\), \(\downarrow\uparrow R=\mathcal I_{\rm pt}\circ R\circ\mathcal I_{\rm pt}\). It follows that
\[
\boxed{S_n=\mathcal I_{\rm pt}^{\,2n+1}\quad(n<\omega).}
\]
The increasing union of these odd powers is the equivalence relation \(\sim_c\) of finite comparability paths, and so
\[
\boxed{S_\omega=\downarrow\operatorname{cl}_{\rm patch}(\sim_c).}
\]
The two-ray example is asserted to stabilize first at \(\omega\).

### Proposed \(\omega+m\) constructions

For every integer \(m\ge1\), let \(A=\{a_n:n\ge0\}\) be a single infinite alternating zigzag as above, and let \(T=\{t_0,t_1,\ldots,t_{2m}\}\) be the finite alternating zigzag
\[
t_0<t_1>t_2<t_3>\cdots<t_{2m-1}>t_{2m}.
\]
Make **no order comparisons between \(A\) and \(T\)**. Topologize \(P=A\cup T\) in the *patch topology* such that all points other than \(t_0\) are isolated, and cofinite tails of \(A\) converge to \(t_0\). The order is claimed patch-closed and Priestley; \(t_0\) is a minimal point of the finite handle.

Finite comparability components are \(A,T\); \(\sim_c=A^2\cup T^2\). Patch closure at \(\omega\) adds cross pairs involving \(t_0\), but no others. Set
\[
T_k=\{t_0,t_1,\dots,t_{2k}\},\qquad k=0,\dots,m.
\]
The proposed **exact formula** is
\[
\boxed{
S_{\omega+k}=A^2\cup T^2\cup (A\times T_k)\cup(T_k\times A),
\qquad 0\le k\le m.}
\]
One application of \(\downarrow\uparrow\) extends the relevant finite-handle endpoint set by one common-upper step, i.e. two adjacent edges, \(T_k\to T_{k+1}\). Consequently \(S_{\omega+m}=P^2\), and no earlier stage equals \(P^2\). The first stabilization stage is therefore asserted **exactly \(\omega+m\)**.

**Audit:** Check the topology is really Priestley for *every* \(m\), check patch closure and down-saturation at \(\omega\), check whether a single successor step can propagate *farther* than two handle edges through unexpected common upper bounds, and check the first-stabilization convention.

## 6. Noncoherent upper-diamond example: a compact \(T_1\) space

Let \(N_1,N_2\) be disjoint countably infinite discrete sets. Adjoin \(\alpha,\beta,\gamma\), all pairwise incomparable in specialization (the space is \(T_1\)). The new neighborhood bases are
\[
\begin{aligned}
\alpha &: \{\alpha\}\cup(N_1\setminus E_1),\\
\beta &: \{\beta\}\cup((N_1\cup N_2)\setminus E),\\
\gamma &: \{\gamma\}\cup(N_2\setminus E_2),
\end{aligned}
\]
with the indicated finite excluded sets; all sheet points are isolated.

The claimed properties: compact, locally compact, sober, scattered, noncoherent, \(T_1\), with spatial scattered localic square. For instance the two compact opens \(\{\alpha\}\cup N_1\) and \(\{\beta\}\cup N_1\cup N_2\) meet in infinite noncompact discrete \(N_1\).

**General lemma to check:** If a \(T_1\) space has a spatial scattered localic square, then \(\mathcal D=\Delta\), \(\mathcal V=\mathcal I\), and \(\mathcal H=\mathcal I\). For any separable distinct pair \((x,y)\), construct the rank-two bar
\[
w_{xy}=((X\setminus\{x\})\boxtimes1)\vee (1\boxtimes(X\setminus\{y\})),
\]
with a horizontal split by \(X\setminus\{x\}\) and a separating neighborhood \(U\ni x\), followed by a vertical split by \(X\setminus\{y\}\) and a disjoint \(V\ni y\). It misses \((x,y)\). Total spatiality of the square's sublocales is then used to prove \(\mathcal V=\mathcal I\). The common-predecessor point formula gives \(\mathcal D=\Delta\).

On the three-point boundary, \(\operatorname{pt}(\mathcal I)\) has edges \(\alpha-\beta\), \(\beta-\gamma\), but not \(\alpha-\gamma\). Yet every \(\alpha\)- and \(\gamma\)-neighborhood has closures intersecting at \(\beta\), so \(\alpha\,\mathcal U\,\gamma\). The continuous reals identify all three limit points; the clopen singletons distinguish the others. The claimed **actual sublocale** relations are
\[
\boxed{\Delta=\mathcal D=\mathcal M
\subsetneq\mathcal I=\mathcal J=\mathcal W=\mathcal V=\mathcal H
\subsetneq\mathcal U=\mathcal F.}
\]
Hence \(\mathcal U\vee\mathcal V\nsubseteq\mathcal H\), even compactly and \(T_1\). Together with §4 this refutes **both possible universal directions** between \(\mathcal U\vee\mathcal V\) and \(\mathcal H\).

## 7. The lower diamond: universal reductions and a compact counterexample

Since \(\mathcal W\le\mathcal U\),
\[
T(\mathcal J)=\mathcal W\wedge\mathcal V\le\mathcal U\wedge\mathcal V.
\]
The following criteria are proposed for arbitrary locales:
\[
\boxed{
\begin{aligned}
\mathcal V\le\mathcal U&\implies
[T(\mathcal J)=\mathcal U\wedge\mathcal V\iff\operatorname{cl}(\mathcal V)=\mathcal W],\\
\mathcal U\le\mathcal V&\implies
[T(\mathcal J)=\mathcal U\wedge\mathcal V\iff\mathcal U=\mathcal W].
\end{aligned}}
\]
If \(\mathcal I\) is fitted then \(\mathcal V=\mathcal I\) and both sides of the lower-diamond equality equal \(\mathcal I\).

### Compact example with only three nonisolated points

Let \(S_1,S_2\) be disjoint countably infinite discrete sets; adjoin \(p,x,y\). All sheet points are isolated. At the three new points take the bases
\[
\begin{aligned}
N_p(E_1,E_2)&=\{p,x\}\cup(S_1\setminus E_1)\cup(S_2\setminus E_2),\\
N_x(E_1)&=\{x\}\cup(S_1\setminus E_1),\\
N_y(E_2)&=\{y\}\cup(S_2\setminus E_2),
\end{aligned}
\]
with finite \(E_i\subseteq S_i\).

**Claims L1–L2 (topology).** This is a countable first-countable compact locally compact sober scattered \(T_0\) space, noncoherent. Its only nontrivial boundary specialization is \(p<x\). The sheet singletons are clopen. The compact opens \(\{p,x\}\cup S_1\cup S_2\) and \(\{y\}\cup S_2\) have infinite discrete noncompact intersection \(S_2\). It is NOT almost normal: put \(A=\{x\}\cup S_1\) and \(B_0=\{p,x\}\cup S_1\cup S_2\). Then \(\overline A=A\cup\{p\}\subseteq B_0\), while every open \(C\) containing \(\overline A\) includes \(p\), has cofinite \(S_2\)-trace, and satisfies \(y\in\overline C\not\subseteq B_0\). Therefore the rather-below relation fails interpolation.

By R1–R2, its localic square is the scattered ordinary product, and every sublocale is spatial/point-determined.

**Claims L3–L4 (three relation levels).** The only offdiagonal \(\mathcal D\)-pairs on the boundary are \((p,x),(x,p)\), arising from common specialization predecessor \(p\). The relation \(\mathcal I\) adds precisely \((p,y),(y,p)\), via cofinite \(S_2\)-tail intersections. The boundary pair \((x,y)\) is *not* \(\mathcal I\)-related: \(\{x\}\cup S_1\) and \(\{y\}\cup S_2\) are disjoint neighborhoods. However, all their neighborhood closures meet at \(p\), so \((x,y),(y,x)\in\mathcal U\). Likewise \((p,y)\in\mathcal I\) and \((p,y)\le(x,y)\) in the specialization order; fitting therefore forces \((x,y)\in\mathcal V\). Clopen sheet singletons exclude all distinct offdiagonal pairs involving sheet points. Every real-valued continuous function identifies \(p,x,y\) (comparison \(p<x\) and inseparability \(p\mathcal I y\)); clopen sheet characteristic functions separate the remaining pairs. Hence the proposed localic equality \(\mathcal U=\mathcal V=\mathcal F\) follows from point-determination.

**Claim L5 (cross-hull).** Universally \(\mathcal I\le\mathcal W\). The product rectangle
\[
(\{x\}\cup S_1)\boxtimes(\{y\}\cup S_2)
\]
contains **no** \(\mathcal D\)-point, as no pair in it has a common specialization predecessor (and its sheet-pair points are offdiagonal). Its transpose likewise excludes \((y,x)\). If R2 applies, these rectangles meet \(\mathcal D\) in the zero sublocale, so both pairs are outside \(\mathcal W=\operatorname{cl}\mathcal D\). They are the only boundary pairs outside \(\mathcal I\), hence \(\mathcal W=\mathcal I\) as closed sublocales.

**Claim L6 (full chain).** Combining the above gives
\[
\boxed{
\Delta\subsetneq\mathcal D=\mathcal M
\subsetneq\mathcal I=\mathcal J=\mathcal W=T(\mathcal J)
\subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F.}
\]
This would refute the universal lower-diamond equality **even for compact locales**, independently of the more elaborate construction below.

**Audit:** Check every topological claim, especially the absence of additional specialization relations, the product-spatiality and scattered representation hypotheses, the point formula for \(\mathcal D\), the complete pair relation enumeration, the \(\mathcal W=\mathcal I\) inference, and the non-almost-normality witness. If this construction fails, please identify the precise earliest failure and whether a close repair exists.

## 8. Optional second lower-diamond construction: noncompact almost-normal thickening

This construction yields a potentially stronger class restriction (almost-normality), at the cost of more technical topology. It is **not needed** if the compact example in §7 is correct, but is included to audit the post-\(\mathcal V\) claims accurately.

### Seed poset and its finite relations

Let \(P=\{p,q,t,x,y\}\) with exactly the comparisons
\[
p<t,\quad p<x,\quad q<t,\quad q<y.
\]
The two minimal points are \(p,q\), and the three maximal points are \(x,t,y\). Common-upper and common-lower calculations on this **finite** Alexandrov poset give
\[
\mathcal V(P)=P^2,
\quad \mathcal U(P)=P^2\setminus\{(x,y),(y,x)\}.
\]
The finite combinatorics can be checked independently.

### Topological thickening

Put \(B=P\times\omega^{\mathrm{op}}\), with
\[
(s,n)\le(t,m)\iff s\le_P t\ \text{and}\ n\ge m.
\]
Each principal upset \(\uparrow b\subseteq B\) is finite. Adjoin a rational sheet \(S=\{s_r:r\in\mathbb Q\}\), all whose points are clopen. Choose distinct irrational \(\alpha_b\) for every \(b\in B\), with \(\{\alpha_{(s,n)}:n\ge N\}\) dense in \(\mathbb R\) for every fixed \(s\in P\) and \(N\).

For irrational \(\alpha\), define \(G_\alpha\) to be the filter on \(\mathbb Q\) generated by
\[
(J\cap\mathbb Q)\setminus N,
\]
where \(J\) is an ordinary real interval containing \(\alpha\), and \(N\subseteq\mathbb Q\) is nowhere dense in \(\mathbb R\). A set \(A\subseteq X=B\sqcup S\) is declared open iff its boundary trace \(H_A=A\cap B\) is an upset of \(B\), and the rational trace \(T_A=\{r:s_r\in A\}\) belongs to \(G_{\alpha_b}\) for every \(b\in H_A\). This is claimed to define a topology, induce the Alexandrov topology on the closed \(B\), and make every sheet singleton clopen.

The almost-normality proof is built on
\[
\Sigma(T)=\operatorname{cl}_{\mathbb R}\operatorname{int}_{\mathbb R}\operatorname{cl}_{\mathbb R}(T).
\]
**Proposed filter-meeting lemma:** every member of \(G_\alpha\) meets \(T\subseteq\mathbb Q\) iff \(\alpha\in\Sigma(T)\). For the forward contrapositive, if \(\alpha\notin\Sigma(T)\), find an interval \(J\) about \(\alpha\) lying in the complement of \(\operatorname{cl}\operatorname{int}\operatorname{cl}T\); after shrinking inside \(J\), the set \(T\cap J\) is nowhere dense, and the filter generator \((J\cap\mathbb Q)\setminus(T\cap J)\) avoids \(T\). Conversely, if \(\alpha\in\Sigma(T)\), every neighborhood interval of \(\alpha\) contains a smaller interval on which \(T\) is dense, and deleting a nowhere-dense subset cannot avoid \(T\).

**Proposed closure formula:** for open \(A\subseteq X\) with boundary upset \(H_A\) and rational trace \(T_A\),
\[
b\in\overline A\iff
\bigl(\uparrow b\cap H_A\ne\varnothing\bigr)
\quad\text{or}\quad
\bigl(\exists c\in\uparrow b:\alpha_c\in\Sigma(T_A)\bigr).
\]
For the converse direction, if every relevant \(\alpha_c\) avoids \(\Sigma(T_A)\), pick for each of the **finitely many** \(c\in\uparrow b\) a filter trace avoiding \(T_A\), and take their union to obtain a common admissible rational trace still avoiding \(T_A\). A boundary neighborhood of \(b\) with that trace misses \(A\).

**Proposed almost-normality argument:** if \(\Sigma(T_A)=\varnothing\), no boundary point belongs to \(A\), and the closure formula says the open \(A\subseteq S\) is also closed. If \(\Sigma(T_A)\ne\varnothing\), choose a nonempty real interval \(J\subseteq\operatorname{int}\operatorname{cl}T_A\). Each \(s\)-fiber has arbitrarily large indices \(n\) with \(\alpha_{(s,n)}\in J\), so \((s,n)\in\overline A\) for arbitrarily large \(n\). Thus any open \(C\supseteq\overline A\) must contain the entire boundary \(B\), because it is an upset. Its complement is contained in the open discrete sheet \(S\), making \(C\) clopen. Consequently, if \(A\prec C\) (i.e. \(\overline A\subseteq C\)), either \(A\) or \(C\) is clopen, and the corresponding endpoint is a valid interpolant \(A\prec D\prec C\). This would show the frame is almost normal.

Please verify the filter-meeting lemma carefully, particularly the nowhere-dense deletion step and the handling of finite but potentially different attachment coordinates. The source construction and a longer proof are also recorded at `A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md`; those references are **not needed** to reconstruct the displayed reasoning, but may help pinpoint any omitted step.

### New boundary-transfer claim

The localic square is claimed spatial and scattered: its open \(S\times S\) part is discrete; the closed complementary summands involve \(B\times_{\mathrm{loc}}X\) and \(X\times_{\mathrm{loc}}B\), spatial because \(B\) is locally compact and sober. Their finite join makes the square spatial, while the ordinary square is scattered. Thus all its sublocales should be point-determined.

For boundary points \(b=(s,n),c=(t,m)\), the new claim is
\[
\boxed{(b,c)\in\operatorname{pt}(\mathcal W_X)\iff(s,t)\in\mathcal U(P).}
\]
If \((s,t)\in\mathcal U(P)\), find \(u\ge s,v\ge t\) with common predecessor \(r\le u,v\), lift to suitable points in \(B\), and use the downwards closure of the closed \(\mathcal W\). If \((s,t)\notin\mathcal U(P)\), the finite upsets \(\uparrow b,\uparrow c\) cannot contain a pair with common lower predecessor; they have disjoint finite sets of irrational attachment coordinates. Choose disjoint rational interval traces around those sets. The product of the resulting basic neighborhoods contains no \(\mathcal D\)-point, excluding \((b,c)\) from \(\mathcal W\) if the claimed spatiality holds.

On the chosen seed \(P\), each boundary point lies above a \(p\)- or \(q\)-point, and \(p,q\) have common upper bound \(t\), so \(\mathcal V_X\) contains every boundary pair. Clopen sheet points show its remaining points equal those of \(\mathcal F\), giving \(\mathcal V=\mathcal F\) under total spatiality. The almost-normal frame theorem then supplies \(\mathcal U=\mathcal F\). Yet \(\mathcal W\) excludes \(((x,0),(y,0))\).

The claimed strictness is
\[
\boxed{T(\mathcal J)=\mathcal W\subsetneq\mathcal U\wedge\mathcal V=\mathcal F}
\]
for a **countable, noncompact, almost-normal, noncoherent** topological locale. This is a separate theorem from the compact example in §7.

## 9. Dependencies, requested comparison, and limits

Please distinguish the following propositions if some fail:

- **Universal frame facts** (§§1–2 and the \(\kappa\)-operator in §5), independent of any topological examples.
- **Coherent Priestley representation** (§3), which underpins the coherent graph interpretation and part of the two-ray calculation.
- **Two-ray concrete example** (§4), which can be examined separately for its closed and fitted relation \(R\).
- **Exact \(\omega+m\) examples** (§5), which are finer ordinal claims and need not stand or fall with nontransitivity.
- **Compact \(T_1\) upper-diamond example** (§6), relying on scattered/spatial sublocales rather than Priestley spectral duality.
- **Compact \(T_0\) lower-diamond example** (§7), independently checkable and not relying on the almost-normal thickening.
- **Almost-normal noncompact thickening** (§8), which has a more extensive prior technical dependency chain.

The broader project also has separate questions about relational composition, arbitrary-frame normality, preservation under products, and a genuinely intrinsic dual definition of \(\mathcal U\); **none are being claimed solved here**. No claim of novelty or publication readiness is intended. Precise identification of which theorems survive independent review will decide which directions to pursue next.

### Background references (not audit reports)

- P. J. Cameron and Vinod Kumar P. B., *Graphs on topological spaces*, arXiv:2610.14783.
- J. Picado and A. Pultr, *Frames and Locales: Topology Without Points*, Springer, 2012; *Separation in Point-Free Topology*, 2021.
- A. Pultr and J. Picado, *Notes on the product of locales*, especially the locally compact sober product theorem.
- R. N. Ball, J. Picado and A. Pultr, *On an aspect of scatteredness in the point-free setting*, Portugaliae Mathematica 73 (2016), 139–152, Proposition 5.3.
- A. L. Suarez, *On the relation between subspaces and sublocales*, Journal of Pure and Applied Algebra 226 (2022), 106851.
- T. Jakl and A. L. Suarez, *Canonical extensions via fitted sublocales*, Applied Categorical Structures 33 (2025), article 10.
- Standard Priestley and Hochster duality sources for coherent frames and spectral spaces.