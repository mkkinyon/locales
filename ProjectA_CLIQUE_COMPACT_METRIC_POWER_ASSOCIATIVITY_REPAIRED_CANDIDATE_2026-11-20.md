# Project A: compact-metric point-clique power associativity
## Repaired theorem and complete candidate proof — 20 November 2026

**Review status:** CANDIDATE SUBMITTED FOR INDEPENDENT BLIND REVIEW. No prior internal verdict is provided here. All locales are considered in classical mathematics. These arguments concern genuine localic pullbacks/images, not pointwise relational composition.

## 1. Definitions and scope

For sublocales $R,S\le G\times G$, $R\circ S$ means the localic image in $G\times G$ of the actual composability pullback $R\times_G S$, traversing $R$ first. A $k$-factor word means a **fully parenthesized** product of $k$ relation factors. Pullback of sublocales preserves finite joins, image preserves joins, and the sublocale lattice is a coframe. In particular, localic composition distributes over **finite** joins in either variable. No general associativity or infinitary distributivity is presumed.

For an ordinary subset $A$ of a sober space $X$, write $[A]_X$ for the spatial sublocale induced by the subspace $A$. For ordinary subsets $A\subseteq X$ and $D\subseteq Z$, put
$$
P_{A,D}=[A\times D]_{X\times Z},
$$
the point-generated spatial sublocale in the *ordinary topological product*, which is not automatically the entire localic product $[A]_X\times_{\rm Loc}[D]_Z$. We write $\mathcal B(K)$ for the least dense/double-negation sublocale of $K$, considered as a sublocale of an ambient space when $K$ is closed.

The main theorem assumes $G$ compact metrizable Hausdorff and a **finite** family of nonempty subsets $E_1,\ldots,E_m\subseteq G$, which need not be disjoint. Put
$$
U_i=[E_i]_G,\qquad P_i=[E_i\times E_i]_{G^2},\qquad H=\bigvee_{i=1}^{m}P_i.
$$
Define the finite overlap graph $\Lambda$ on indices $1,\ldots,m$ by $i\sim j$ for distinct indices if $U_i\wedge U_j\ne0$; repeated indices may always be used as steps because $U_i\ne0$. Distances between different connected components are $\infty$.

**Theorem (candidate).** For every integer $k\ge2$ and every full binary bracketing $W_k(H)$ of $k$ copies of $H$,
$$
\boxed{ W_k(H)=\bigvee_{\operatorname{dist}_{\Lambda}(i,j)\le k-1} U_i\times U_j. }\tag{PA}
$$
Thus all powers of $H$ are independent of parenthesization. The case $k=1$ is deliberately excluded: generally $P_i\ne U_i\times U_i$.

The proof has three major ingredients, stated independently to make the audit modular.

## 2. Elementary rectangular and density facts

**Lemma 2.1 (rectangles).** For $A,B,C,D\le G$,
$$
(A\times B)\circ(C\times D)=
\begin{cases}A\times D,&B\wedge C\ne0,\\0,&B\wedge C=0.\end{cases}\tag{R}
$$
The composability locale is exactly $A\times(B\wedge C)\times D$. In classical Loc a nonzero locale is overt; its map to $1$ is an **open surjection**, as is every pullback. Hence projection onto $A\times D$ is surjective when the middle is nonzero. This is NOT a claim that arbitrary locale-surjections are pullback-stable.

**Lemma 2.2 (spatial point support).** If $A\subseteq X$ is an ordinary subset and $K\subseteq X$ is closed with $K\cap A=\varnothing$, then $[A]_X\le X\setminus K$ as sublocales. Conversely, if $T\le[A]_X$ is nonzero and $C=\overline T\subseteq X$ is its least closed support, then $A\cap C$ is dense in $C$ whenever $X$ is compact Hausdorff.

*Proof.* The first statement follows because $[A]_X$ is the join of the point sublocales at $a\in A$, all lying in the open complement of $K$. For density, suppose a nonempty relatively open $V\subseteq C$ misses $A$. Choose nonempty relatively open $V'$ with $\overline{V'}^{\,C}\subseteq V$. Its closure is compact closed in $X$, misses $A$, and contains $V'$. Thus $[A]_X\le X\setminus\overline{V'}^{\,C}$, so $T\wedge V'=0$. This contradicts density of $T$ in its least closed support $C$. The statement remains true for a nonzero meet $T\le[A]_X$ with other sublocales, and for compact-metric $X$ as a special case. $\square$

**Lemma 2.3 (density/image facts).** The meet of two dense sublocales of the same locale is dense, since both contain its least dense sublocale $\mathcal B$. If $f:V\to W$ is an open surjection and $S\le V$ dense, then the image $f[S]\le W$ is dense: every nonzero open of $W$ has nonzero open inverse image, and that inverse image meets $S$ nontrivially. Consequently $\mathcal B(W)\le f[S]$. This implication is used only for the explicitly open-surjective maps below.

## 3. The two-colour compact Cantor-graph lemma

**Lemma 3.1 (two-colour graph fusion).** Let $X,Z$ be compact metrizable spaces and $K\subseteq X\times Z$ a nonempty closed subset. Assume **every vertical section** $K\cap(\{x\}\times Z)$ and **every horizontal section** $K\cap(X\times\{z\})$ is nowhere dense relative to $K$. Let $P,Q\subseteq K$ be two (not necessarily disjoint) dense ordinary subsets. Then there exists a nonempty compact subset $\Gamma\subseteq K$, homeomorphic to the Cantor space, such that:

1. Both coordinate projections $\Gamma\to X$ and $\Gamma\to Z$ are injective (hence homeomorphisms to their compact images).
2. The subsets $\Gamma\cap P$ and $\Gamma\cap Q$ are **both dense in $\Gamma$**.

*Proof (full induction).* Fix compatible metrics. We construct a finitely-branching tree indexed by $\{0,1,2\}^{<\omega}$. For every node $s$ at depth $n$, choose a closed ambient product rectangle $R_s=F_s\times L_s$ with $K\cap\operatorname{int}(R_s)\ne\varnothing$, and an **inherited anchor** $c_s\in K\cap\operatorname{int}(R_s)$. At each depth, insist that the first-coordinate projections of rectangles at that depth are pairwise disjoint, and likewise the second-coordinate projections; the closed child rectangles lie in the respective **interiors** of their parents and have product diameter at most $2^{-n}$ (for $n\ge1$).

At the root take $R_\varnothing=X\times Z$ (if necessary use the whole compact space as the ambient rectangle), and choose any point $c_\varnothing\in K$. Assume all depth-$n$ parent rectangles and anchors are fixed. Process **all** finitely many nodes at that depth, keeping a global finite registry of the first and second coordinates of every already chosen anchor at the new stage (including all inherited anchors). Within the nonempty relatively open set $K\cap\operatorname{int}(R_s)$, select a new $p_s\in P$ and then a new $q_s\in Q$ whose **two coordinates** avoid every registered coordinate, including those of $c_s$ and of $p_s$. This is possible: for any finite list of forbidden coordinate values, the union of their vertical and horizontal sections is relatively closed nowhere dense in $K$; its complement intersects the nonempty relative open of $K$, and the dense sets $P$ and $Q$ meet that complement. Register both coordinates of $p_s,q_s$ after each selection. The three anchors $c_s,p_s,q_s$ now have distinct first coordinates and distinct second coordinates, globally across all nodes of this depth.

**Only after every node has had its two new anchors selected**, shrink simultaneous child rectangles around each of the three anchors. Choose $R_{s0},R_{s1},R_{s2}\subseteq\operatorname{int}(R_s)$ closed, with their anchor respectively $c_s,p_s,q_s$ in their interiors, each of diameter at most $2^{-n-1}$, and with all first-coordinate projections and all second-coordinate projections pairwise disjoint over **all** children at the new depth. This is feasible because there are finitely many chosen anchors, their first coordinates are pairwise distinct, their second coordinates are pairwise distinct, and the parent interior neighborhoods are open. Assign $c_{s0}=c_s$, $c_{s1}=p_s$, $c_{s2}=q_s$. An anchor carried into child 0 will also be carried into its child 0 at every subsequent depth.

For each infinite branch $b\in\{0,1,2\}^{\omega}$, the nested nonempty compact sets $K\cap R_{b|n}$ have diameters tending to zero, so they have a **unique** common point $\gamma_b\in K$. Distinct branches first split into children with disjoint first-coordinate rectangles and disjoint second-coordinate rectangles, hence their two limit points differ in **both** coordinates. The map $b\mapsto\gamma_b$ is a continuous injection from compact Cantor space into Hausdorff $K$; its image $\Gamma$ is a compact Cantor graph with both projections injective.

Each anchor $p_s$ lies in $\Gamma$, since it persists down the branch $s1 0^\omega$; likewise $q_s$ lies in $\Gamma$ down $s2 0^\omega$. Every basic cylinder determined by $s$ contains both such selected anchors, and cylinders form a base for $\Gamma$. Thus $P\cap\Gamma$ and $Q\cap\Gamma$ are dense. $\square$

*Boundary warnings:* The fusion works in the **ordinary closed support $K$**, not by selecting points of an arbitrary pointless sublocale. Only finitely many coordinate sections are excluded at each stage. Select all anchors before shrinking children globally; separate both first and second coordinates. The section hypothesis is stronger than the assertion that $K$ is perfect and is proved separately below.

## 4. Closed-annihilator generation of a localic product

**Lemma 4.1 (graph generation, G).** Let $X,Z$ be compact metrizable Hausdorff spaces, $A\subseteq X$ and $D\subseteq Z$ nonempty ordinary subsets, and $U=[A]_X$, $V=[D]_Z$. Let $P_{A,D}=[A\times D]_{X\times Z}$. Let $\mathscr G(A,D)$ be the compact Cantor graphs $\Gamma\subseteq X\times Z$ with injective coordinate projections and with the traces
$$
\{\gamma\in\Gamma:\pi_X\gamma\in A\},\qquad
\{\gamma\in\Gamma:\pi_Z\gamma\in D\}
$$
separately dense in $\Gamma$. Then
$$
\boxed{U\times V=P_{A,D}\ \vee\bigvee_{\Gamma\in\mathscr G(A,D)}\mathcal B(\Gamma).}\tag{G}
$$
The localic product $U\times V$ need not be spatial.

*Proof.* For $\Gamma\in\mathscr G$, the inverse images of $U$ and $V$ along the coordinate maps from $\Gamma$ contain the two respective **dense ordinary point traces**. Hence they are dense sublocales of $\Gamma$ and both contain $\mathcal B(\Gamma)$. Thus $\mathcal B(\Gamma)\le U\times V$ as a sublocale of $X\times Z$; likewise $P_{A,D}\le U\times V$. Denote the RHS of (G) by $J$.

Suppose $J\not\ge U\times V$. Since the ambient compact Hausdorff locale $X\times Z$ is regular and all its sublocales are fitted, there is an **ambient open sublocale** $O$ with $J\le O$ but $U\times V\not\le O$. Let $F$ be the complementary closed sublocale. The nonzero meet
$$S=F\wedge(U\times V)\ne0$$
exists by finite distributivity over the open/closed complement. Let $K$ be the least **ambient closed support** of $S$. It is a nonempty compact metrizable closed **ordinary subset** of $X\times Z$, lies inside $F$, and $S$ is dense in $K$. Since $P_{A,D}\le J$ and $J\wedge F=0$, the closed set $F$ has no ordinary point $(a,d)$ with $a\in A,d\in D$.

We show that the two ordinary subsets
$$
P=\{(x,z)\in K:x\in A\},\qquad
Q=\{(x,z)\in K:z\in D\}
$$
are separately dense in $K$. If a nonempty relatively open $W\subseteq K$ misses $P$, choose nonempty relatively open $W'$ with compact closure $L=\overline {W'}^K\subseteq W$. The projection $T=\pi_X(L)$ is compact and therefore closed in $X$, and is disjoint from $A$. Consequently $U\le X\setminus T$ by Lemma 2.2. But $S\le U\times V$ and $W'$ lies over $T$, so $S\wedge W'=0$, contradicting density of $S$ in $K$. The proof for $Q$ is the same with the other coordinate.

Next, **every vertical or horizontal section of $K$ is relatively nowhere dense**. Suppose a vertical section at $x\in X$ contained a nonempty relatively open $W\subseteq K$, and choose nonempty $W'$ with compact closure $L=\overline{W'}^K\subseteq W$. If $x\notin A$, the closed singleton $\{x\}$ misses $A$, giving $U\le X\setminus\{x\}$, and again $S\wedge W'=0$. If $x\in A$, set $T=\pi_Z(L)$, compact closed in $Z$. Now $L\subseteq F\cap(\{x\}\times Z)$ and $F$ contains **no selected point pair** $(x,d)$, $d\in D$. Thus $T\cap D=\varnothing$, giving $V\le Z\setminus T$ and $S\wedge W'=0$. Both contradict density. The horizontal sections are treated symmetrically. **We do not infer that nonzero sublocales of spatial point slices must have ordinary points**; that inference is false and is not used.

Apply Lemma 3.1 to compact closed $K$ with dense subsets $P,Q$. It yields $\Gamma\in\mathscr G(A,D)$ inside $K\subseteq F$. The nonzero Booleanization $\mathcal B(\Gamma)$ lies in $J$ by definition and in $F$ because $\Gamma\subseteq F$. This contradicts $J\wedge F=0$. Therefore (G) holds. $\square$

## 5. Dense bipartite saturation

**Lemma 5.1 (bipartite saturation, B).** Let $X,Y,Z$ be compact metrizable Hausdorff spaces and $A\subseteq X$, $B,C\subseteq Y$, $D\subseteq Z$ nonempty ordinary subsets, with **both $B,C$ dense in the same $Y$**. Then for the point-generated spatial relations
$$R=[A\times B]_{X\times Y},\qquad S=[C\times D]_{Y\times Z}$$
we have
$$\boxed{R\circ S=[A]_X\times[D]_Z.}\tag{B}$$
The composition is the genuine localic image of the genuine pullback.

*Proof.* Source/target support gives $R\circ S\le U\times V$, where $U=[A],V=[D]$. For any ordinary $a\in A,d\in D$, the one-point-legged **spatial** rectangles $\{a\}\times[B]_Y\le R$ and $[C]_Y\times\{d\}\le S$ are present because the corresponding ordinary point pairs generate them. Both $[B]_Y$ and $[C]_Y$ are dense, hence their meet is nonzero. The rectangular lemma gives the point edge $\{(a,d)\}\le R\circ S$. Joining yields $P_{A,D}\le R\circ S$.

Now let $\Gamma\in\mathscr G(A,D)$ be a graph appearing in (G). Consider the **compact spatial product** $\Gamma\times Y$ (compact metrizable), with map
$$\Phi:\Gamma\times Y\longrightarrow X\times Y\times Z,\quad(\gamma,y)\longmapsto(\pi_X\gamma,y,\pi_Z\gamma).$$
The pullback under $\Phi$ of the first relation condition contains all ordinary points with $\pi_X\gamma\in A$ and $y\in B$, a subset dense in $\Gamma\times Y$ because the first selected trace is dense in $\Gamma$ and $B$ is dense in $Y$. The pullback of the second relation condition analogously contains the dense ordinary set with $\pi_Z\gamma\in D$ and $y\in C$. Hence **both actual localic pullback sublocales** are dense in $\Gamma\times Y$, and their meet contains the nonzero least dense sublocale $\mathcal B(\Gamma\times Y)$. This meet maps into the actual composability pullback $R\times_Y S$.

The product projection $\Gamma\times Y\twoheadrightarrow\Gamma$ is an **open surjection** (nonempty overt middle factor $Y$), and the image of the dense meet is dense in $\Gamma$ by Lemma 2.3. Its outer-coordinate image lies in $R\circ S$, so $\mathcal B(\Gamma)\le R\circ S$. Applying (G) and joining all the graph Booleanizations proves $U\times V\le R\circ S$. $\square$

**Monotonicity variant.** If $R\le R'\le [A]\times[B]$ and $S\le S'\le[C]\times[D]$ with $R,S$ as above, then $R'\circ S'=[A]\times[D]$ by monotonicity and endpoint support. We use this variant for subtrees already equal to full rectangles.

## 6. Compact overlap supports

**Lemma 6.1.** Let $G$ be compact metrizable Hausdorff, let $U_i=[E_i]_G,U_j=[E_j]_G$, and assume $W=U_i\wedge U_j\ne0$. Let $K=\overline W$ be the least ambient closed support in $G$. Then $K$ is a nonempty compact metrizable closed subspace and **both $E_i\cap K$ and $E_j\cap K$ are dense ordinary subsets of $K$**.

*Proof.* The meet $W$ is dense in its least closed support $K$. Apply Lemma 2.2 to $W\le U_i$ and $W\le U_j$ separately. This does not assert that $W$ has a point; indeed it can be pointless. $\square$

The point-generated bipartite subrelations $[E_i\times(E_i\cap K)]$ and $[(E_j\cap K)\times E_j]$ lie in $P_i$ and $P_j$, respectively (in their appropriately typed ambient products). Since the two middle subsets are dense in the same compact $K$, (B) gives
$$
\boxed{P_i\circ P_j=U_i\times U_j\quad\text{whenever }U_i\wedge U_j\ne0.}\tag{C2}
$$
The opposite inequality comes from source/target supports. If the overlap is zero, the actual composability object vanishes, so $P_i\circ P_j=0$. This includes $i=j$, with $K$ the least closed support of $U_i$, or directly by choosing one ordinary point of $E_i$ and using two point-legged rectangles.

## 7. All-bracketing induction (all four split types)

**Lemma 7.1 (indexed words).** Fix $k\ge2$ and indices $j_1,\ldots,j_k$. For **every** full binary bracketing $T$ of $P_{j_1}\circ\cdots\circ P_{j_k}$,
$$
\boxed{T=U_{j_1}\times U_{j_k}\quad\text{if }U_{j_t}\wedge U_{j_{t+1}}\ne0\text{ for every }t<k,}
$$
and $T=0$ if any of these adjacent overlaps is zero.

*Proof of the nonzero case.* Induct on the number of leaves. For $k=2$ this is (C2). Suppose the root splits after the $t$-th leaf, with left child $L$ and right child $R$.

- **Both children have at least two leaves:** Induction gives $L=U_{j_1}\times U_{j_t}$ and $R=U_{j_{t+1}}\times U_{j_k}$. Their middle supports have nonzero meet, so Lemma 2.1 gives the full outer rectangle.
- **Left child a single leaf and right child composite:** Write the first index $i=j_1$ and the next index $j=j_2$, and let the right subtree end in index $\ell=j_k$. By induction $R=U_j\times U_\ell$. Let $K$ be the compact closed support of $U_i\wedge U_j\ne0$ from Lemma 6.1. The left leaf $P_i$ contains $[E_i\times(E_i\cap K)]$, while the right full rectangle contains $[(E_j\cap K)\times E_\ell]$. By (B) their composition is the **entire** $U_i\times U_\ell$. Endpoint support supplies the reverse bound.
- **Right child a single leaf and left child composite:** Reverse the preceding argument, using the compact support of $U_{j_{k-1}}\wedge U_{j_k}$ and point-generated subrelations inside the left full rectangle and the right leaf.
- **Both children single leaves:** This is the base case (C2).

At no stage do we assume that $U_i\times U_j$ is spatial; its fullness follows from the proved saturation lemma. This completes the nonzero case.

*Proof of the zero case.* If an adjacent pair $U_{j_t}\wedge U_{j_{t+1}}=0$, find the lowest common ancestor of consecutive leaves $t$ and $t+1$. Its two children end/start with those indices. Independently of whether these children are zero or nonzero, their endpoint support lies inside the two respective supports, whose meet is zero. Their actual composability pullback vanishes. Hence that ancestor, and the full word containing it, is zero. $\square$

## 8. Proof of the main theorem

Expand any fully parenthesized $k$-word in $H=\bigvee_{i=1}^{m}P_i$ using only **finite** distributivity of composition. This gives a finite join of individually bracketed indexed words. By Lemma 7.1, a summand is nonzero exactly when its index sequence is a walk in the overlap graph, allowing repetitions, and then the summand is the entire rectangle between its initial and final support indices.

For $k\ge2$, there exists such a length-$k$ index sequence from $i$ to $j$ precisely when $\operatorname{dist}_\Lambda(i,j)\le k-1$: use a shortest path and pad by repetitions at any vertex, including when $i=j$. Therefore the finite join is exactly
$$W_k(H)=\bigvee_{\operatorname{dist}_\Lambda(i,j)\le k-1}U_i\times U_j,$$
independently of parenthesization. $\square$

**Interpretation:** The theorem says the *powers of one relation* $H$ are associative/power-associative. It does NOT say composition is associative on the subalgebra generated by heterogeneous relations $P_i$, nor for arbitrary localic relations, nor for infinite families or nonmetrizable settings. It also does NOT claim that $H=\bigvee_i U_i^2$ at length one.

## 9. Concrete five-vertex sector

For four clopen Cantor blocks $C_0,C_1,C_2,C_3$ with dense induced irrational and rational sublocales $I_t,Q_t$, set
$$
R=[I_0\times Q_1],\quad S=[I_1\times Q_2],\quad T=[I_2\times Q_3].
$$
The bipartite lemma gives
$$
R\circ S=I_0\times Q_2,\qquad S\circ T=I_1\times Q_3.
$$
Use (B) and the monotonicity variant for the next step. Then
$$
\boxed{(R\circ S)\circ T=I_0\times Q_3=R\circ(S\circ T).}\tag{5V}
$$
These are equal **localic products**, potentially nonspatial, not merely equal sets of ordinary point pairs. This is the exact distance-two sector left by the four-vertex clique calculation.

## 10. Explicit verification boundaries

The referee should challenge the following rather than relying on analogies with ordinary graphs:

- Fittedness of sublocales in regular locale $X\times Z$ and extraction of a separating **ambient open**, not merely a set of missing ordinary points.
- The least closed support $K$ of a nonzero potentially pointless sublocale $S$: why its selected-coordinate traces are dense; why point sections have **empty relative interior** using compact projected closures.
- The **global two-phase** Cantor fusion, injectivity of *both* coordinate projections, and persistence/density of both sets of selected anchors.
- The pullbacks to $\Gamma\times Y$ in Lemma 5.1, and the precise **open-surjection** used to transport density to $\Gamma$.
- The compact closed support $K$ in Lemma 6.1 and the leaf-versus-full-rectangle steps of Lemma 7.1.
- Spatial point-generated relations $[A\times B]$ versus nonspatial products $[A]\times[B]$, and the prohibition on deducing localic equality from equality of ordinary point pairs.

All claimed results in this document are submitted as proofs to check, not as an instruction to return a positive verdict. A counterexample to any statement, a necessary additional hypothesis, or a shorter proof is welcome.