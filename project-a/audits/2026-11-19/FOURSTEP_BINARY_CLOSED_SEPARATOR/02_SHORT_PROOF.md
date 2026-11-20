# Project A — four-step effectiveness by a binary Cantor graph and a closed separator

**19 November 2026. Candidate proof for independent blind review.**

## Purpose and verification boundary

This candidate uses a direct closed-separator contradiction to establish its global square inclusion. It needs neither (a) a join-of-Booleanized-Cantor-graphs theorem nor (b) antichain requirements or global component registries in Cantor fusion. Its prerequisites are the explicit finite-fence coordinate geometry, exact point fibre, finite-cutoff rigidity, and special pointless patch-fibre comparison. **The final four-step theorem is offered for independent checking.**

Let $P=[0,1]$ carry the compact closed height-one fence order in the accompanying coordinate appendix; $X$ is its upper locale, $p:P_{\mathrm{patch}}\to X$ the Euclidean-patch map, $q:X\to Q$ the component quotient, $E=E_P\cup E_Q$ the countable fence-vertex set, and $p_\infty:1\to Q$ the completely prime point whose opens are exactly the quotient opens meeting $E$. The middle Cantor set $M$ contains two disjoint dense families of fence endpoints. Each sufficiently late fence of colour $\alpha\in\{P,Q\}$ traverses every prescribed nonempty open subset of a fixed open mediator $U_\alpha$ in its own gap. All comparability components other than singletons are finite fences.

Write

$$
H=[\{(x,y):x,y\text{ ordinary points in the same component}\}],\quad
K=X\times_QX,\quad T=H\circ_XH,\quad R=T\circ_XT,
$$

with **the balanced bracketing fixed**, and define

$$
G=X\times_Q1,\quad B=G\times G,\quad
\Lambda=p^{-1}G,\quad F_\infty=\Lambda\times\Lambda,
\quad \widehat L=(p\times p)^{-1}L
$$

for a sublocale $L\le X^2$. Every composite is the **image of the actual localic composability pullback**, not a pointwise relation product. The question is whether $R=K$ (equivalently, by the audited localization theorem, $(D^2)\circ_G(D^2)=B$ with $D=H\wedge B$).

## I. Geometric and localic inputs

The following inputs have proofs in the appended mathematical foundations, and are not assumed to follow from ordinary point-set equality:

1. **Finite-vertex separation:** any patch-compact $C\subseteq P$ meeting $E$ finitely has compact component-saturated closure $C^{\rm sat}$ meeting $E$ finitely. Its complement is a quotient-open neighborhood of $p_\infty$ disjoint from $C$.
2. **Actual fibre and pointlessness:** the point pullback $G$ is the meet of the complementary opens of the finite-vertex cutoffs (positive **and negative** tests); $\Lambda$ has no ordinary patch points.
3. **Special patch comparison:** $\Lambda\to G$ is an isomorphism, hence $F_\infty\to B$ is an isomorphism over $X^2$. No general properness or arbitrary image/base-change theorem for $p$ is used.
4. **Cutoff rigidity:** $K\wedge(C\times C)\le H$ for each saturated finite-vertex cutoff $C$. The coframe lemma gives $K=H\vee B$.
5. **Ordinary fence geometry:** every late $\alpha$-fence meets $U_\alpha$, and the corresponding endpoints in $M$ are dense with unbounded indices in every nonempty relatively open part of $M$.

The compact regular patch square is fit: every one of its sublocales is an intersection of patch-open sublocales. The standard open-map density lemma is recorded in §IV.

## II. Closed supports and fixed colours

**Lemma 1 (support richness).** If $0\ne S\le F_\infty$ and $C_0$ is its least patch-closed support, then each nonempty relatively open $W\subseteq C_0$ has infinitely many first-coordinate values in $E$ and infinitely many second-coordinate values in $E$. Every vertical or horizontal section at an ordinary coordinate value is nowhere dense in $C_0$.

**Proof.** $C_0$ is a nonempty compact metric space, and $S$ is dense in it. If, for example, $\pi_1(W)\cap E$ is finite, choose a nonempty relatively open $W'\subseteq C_0$ whose compact closure is contained in $W$. Its first-coordinate projection is compact and meets $E$ finitely; input 1 supplies a positive quotient open whose patch pullback misses that projection. Since the first projection of $S$ factors through $\Lambda$, this forces $S\wedge W'=0$, contrary to density. The other coordinate is symmetric. Since $\Lambda$ has no ordinary points, $S$ meets every point-coordinate section in zero. Such a section is relatively closed, so nonempty relative interior would again contradict density of $S$. $\square$

**Lemma 2 (fixed-colour localization).** For some nonempty compact closed support $C_1\subseteq C_0$ and fixed $\alpha,\beta\in\{P,Q\}$, every nonempty relatively open part of $C_1$ has infinitely many first-coordinate values in $E_\alpha$ and second-coordinate values in $E_\beta$. Its coordinate sections remain nowhere dense.

**Proof.** In $C_0$ set $A_\alpha=C_0\cap\pi_1^{-1}(E_\alpha)$, $B_\beta=C_0\cap\pi_2^{-1}(E_\beta)$. Lemma 1 yields

$$
C_0=\overline{A_P}\cup\overline{A_Q}
=\overline{B_P}\cup\overline{B_Q}.
$$

The four closed intersections $\overline{A_\alpha}\cap\overline{B_\beta}$ cover the compact Baire space $C_0$, so one has nonempty relative interior $W$. Both designated traces are dense on $W$. Choose an ambient patch-open rectangle $V$ with $C_0\cap V\ne\varnothing$ and $\overline{C_0\cap V}\subseteq W$. The nonzero sublocale $S\wedge V$ is dense in $C_1=\overline{C_0\cap V}$. Every nonempty relative open of $C_1$ meets $C_0\cap V$ in a nonempty relative open of $W$, hence meets both selected traces. Since individual coordinate sections are nowhere dense (by the same argument applied to $S\wedge V$), deleting any finite collection of coordinate values still leaves selected values in each nonempty open. Thus each selected trace is locally infinite. $\square$

## III. Ordinary binary Cantor fusion — no antichains

**Lemma 3 (binary graph).** Under Lemma 2, there is a compact $\Gamma\subseteq C_1$ homeomorphic to Cantor space such that both coordinate projections are homeomorphisms onto compact perfect $D_1,D_2\subseteq P$ and

$$
D_1\cap E_\alpha\text{ dense in }D_1,
\qquad D_2\cap E_\beta\text{ dense in }D_2.
$$

No antichain condition is asserted or needed.

**Proof.** Build a binary tree of closed product rectangles $R_s=I_s\times J_s$ of diameters tending to zero, with anchors $z_s\in C_1\cap\operatorname{int}R_s$. At depth $n$, child $s0$ inherits $z_s$. Choose the new anchor for child $s1$ in $C_1\cap\operatorname{int}R_s$, avoiding the two coordinate values of $z_s$, with its first coordinate in $E_\alpha$ if $n$ is even and its second coordinate in $E_\beta$ if $n$ is odd. Lemma 2 supplies this point after removing two nowhere-dense coordinate sections. Choose small child rectangles within the parent, around the anchors, whose first-coordinate intervals are disjoint and whose second-coordinate intervals are disjoint. Different parents already have disjoint coordinate intervals, so no cross-parent coordination is necessary.

Every infinite branch gives a unique point of $C_1$ by compactness and shrinking diameters; the resulting $\Gamma$ is homeomorphic to $2^\omega$. Disjointness of coordinate intervals at the first branch divergence makes both projections injective; compactness and Hausdorffness make them homeomorphisms onto the Cantor sets $D_i$. Any cylinder has descendants at arbitrarily late even and odd levels. The selected anchor of a child $s1$ persists on its all-zero tail. Thus both designated selected traces meet every cylinder and are dense. $\square$

## IV. Dense strips and the actual image composition

**Open-map density fact.** If $f:Y\to Z$ is an open surjection, inverse images of dense sublocales are dense; images of dense sublocales are dense. For the first assertion, given nonzero open $W\le Y$, its open image $f[W]$ meets the dense sublocale of $Z$, and the restricted open surjection $W\to f[W]$ remains surjective after base change. For the second, every nonzero open of $Z$ has nonzero open inverse image meeting the dense sublocale of $Y$, whose image then meets the original open. In any locale $Z$, its double-negation sublocale $\mathcal B(Z)$ lies in every dense sublocale. Nonempty spatial factors here make the relevant product projections open surjections.

**Lemma 4 (strips without antichains).** Suppose $D\subseteq P$ is compact perfect and $D\cap E_\alpha$ is dense. Then

$$
\mathcal B(D\times M)\le(D\times M)\wedge\widehat T,
\quad
\mathcal B(M\times D)\le(M\times D)\wedge\widehat T.
$$

**Proof.** In every nonempty basic patch-open $A\times V\subseteq D\times U_\alpha$, the relatively open $A$ contains selected vertices from arbitrarily late $\alpha$-fences (perfectness plus density), and each sufficiently late such fence meets $V$. Thus ordinary component-related pairs are dense in $D\times U_\alpha$, and the point-generated relation $H$ contains their patch images. Therefore

$$
\mathcal B(D\times U_\alpha)\le\widehat H.
$$

Similarly, the $\alpha$-fence endpoints are dense in $M$, with arbitrarily late indices in every open, giving $\mathcal B(U_\alpha\times M)\le\widehat H$. In $Y=D\times U_\alpha\times M$, pull back these dense sublocales along the two open-surjective patch product projections. Both inverse images contain $\mathcal B(Y)$, so the map $\mathcal B(Y)\to X^3$ factors through the **actual** localic pullback $H\times_XH$. Its outer-coordinate map factors through $T$. The open-surjective projection $Y\to D\times M$ has dense image on $\mathcal B(Y)$; that image contains $\mathcal B(D\times M)$ and is contained in the pullback of $T$. This proves the first assertion. The second is symmetric, since $H$ is symmetric. At no point is $D$ assumed an antichain. $\square$

**Lemma 5 (graph-restricted witness).** If $\Gamma\subseteq P^2$ is a compact Cantor graph whose projections are homeomorphisms onto $D_1,D_2$ satisfying Lemma 3, then

$$
0\ne\mathcal B(\Gamma)\le\Gamma\wedge\widehat R.
$$

**Proof.** Lemma 4 gives $\mathcal B(D_1\times M)\le\widehat T$ and $\mathcal B(M\times D_2)\le\widehat T$. On $\Gamma\times M$, the two maps to these two products are homeomorphisms. Thus both pulled-back strips contain $\mathcal B(\Gamma\times M)$, and its upper triple map factors through $T\times_XT$. The outer map therefore factors through $R$. The patch projection $\Gamma\times M\to\Gamma$ is open surjective, so its image of $\mathcal B(\Gamma\times M)$ is dense and contains $\mathcal B(\Gamma)$. The latter is nonzero because $\Gamma$ is a nonempty Cantor locale. **No claim $\mathcal B(\Gamma)\le F_\infty$ is made or needed.** $\square$

## V. Direct closed-separator proof of the generic-square inclusion

**Theorem 6 (global generic square).** Under inputs I.1–I.5,

$$
\boxed{G\times G\le (H\circ_XH)\circ_X(H\circ_XH).}
$$

**Proof.** Suppose $F_\infty\not\le\widehat R$. Since the regular patch square is fit, there is a patch-open $O\ge\widehat R$ with $F_\infty\not\le O$. Let $C$ be its complementary patch-closed sublocale. Finite distributivity yields

$$
\widehat R\wedge C=0,\qquad S:=F_\infty\wedge C\ne0.
$$

Let $C_0$ be the least closed support of $S$. Lemmas 1–3, applied to $S$, produce a graph $\Gamma\subseteq C_0\subseteq C$ with the properties of Lemma 5. Hence

$$
0\ne\mathcal B(\Gamma)\le C\wedge\widehat R=0,
$$

a contradiction. We conclude $F_\infty\le\widehat R$. The **special** isomorphism $F_\infty\cong G\times G$ over $X^2$ transports this factorization to the desired inclusion. No arbitrary surjective-image base-change law, no associativity assumption, and no join-of-Cantor-graphs statement is used. $\square$

## VI. Nonzeroness and the four-step theorem

**Lemma 7 (middle Cantor witness).** $G\ne0$, and in fact $0\ne\mathcal B(M)\le\Lambda$ as patch sublocales.

**Proof.** The endpoint sets $\{a_n\}$ and $\{b_n\}$ lie in $E\cap M$, and each is dense in the perfect Cantor set $M$. Every positive quotient open has a saturated closed complement meeting $E$ finitely, so its trace on $M$ is dense open and contains $\mathcal B(M)$. Every negative quotient open misses $E$, so its patch-open trace on $M$ is empty. Thus the map $\mathcal B(M)\to Q$ sends each open to top or bottom according as it belongs to the completely prime filter of $p_\infty$. It factors through the point $p_\infty$ and hence through $\Lambda$. Since $M\ne0$, its least dense sublocale is nonzero. The patch comparison yields $G\ne0$. $\square$

**Theorem 8 (four-step kernel-pair effectiveness).** For the explicit finite-fence pospace,

$$
\boxed{(H\circ_XH)\circ_X(H\circ_XH)=K=\operatorname{EqHull}_X(H).}
$$

**Proof.** The cutoffs give $K=H\vee(G\times G)$ by the coframe decomposition (background lemma). Theorem 6 gives $G\times G\le R$. The point-generated component relation $H$ contains the diagonal: $X$ is spatial, its diagonal locale is spatial, and every ordinary diagonal pair is among the generators of $H$. Thus $H$ is reflexive, so $H\le T\le R$. Also $R\le K$ because $H\le K$ and kernel pairs are transitive. Therefore $K=H\vee(G\times G)\le R\le K$. As $K$ is an equivalence relation containing $H$, while every equivalence relation containing $H$ contains both $T$ and $R$, its least equivalence hull is $K$. $\square$

With $D=H\wedge(G\times G)$, the separately established generic-fibre composition-localization isomorphism $[H,K]\cong[D,G\times G]$ now yields the equivalent **balanced** equality $(D^2)\circ_G(D^2)=G\times G$.

## VII. Scope

No strict inequality between intermediate powers is claimed, and no associativity statement is claimed. The proof does not depend on a global join of Booleanized graphs or on a factorization of any individual graph through the generic fibre. Appendix 03 gives the separate exact-fibre, cutoff, and patch-comparison arguments; Appendix 04 gives the explicit coordinates.
