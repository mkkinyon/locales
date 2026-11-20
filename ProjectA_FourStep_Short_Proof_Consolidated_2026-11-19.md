# Project A — four-step effectiveness by a binary Cantor graph and a closed separator

**Consolidated 19 November 2026; repaired 20 November 2026 following independent blind review.** The referee judged the argument *valid with specific repairs*, principally the arbitrary-union defect lemma in the patch-fibre comparison. The repair and its localic consequences are written out below. The original blind packet remains an unchanged archival snapshot.

## Purpose and verification boundary

This note replaces the *global graph-generation* step in the earlier candidate proof with a direct closed-separator contradiction. It eliminates both (a) a join-of-Booleanized-Cantor-graphs theorem and (b) the antichain requirements and global component registries in Cantor fusion. It uses the finite-fence coordinate geometry, exact point fibre, finite-cutoff rigidity, and special pointless patch-fibre comparison. The short proof, including its stated inputs, has now received a positive **qualified** independent blind report, with the substantive repair incorporated in §I.A. The audit reconciliation records the individual checks and their remaining scope.

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

The following inputs have proofs in the [exact-fibre and cutoff companion](ProjectA_FourStep_Fibre_Cutoff_Foundations_CANONICAL_2026-11-20.md), the [explicit coordinate appendix](project-a/audits/2026-11-19/FOURSTEP_BINARY_CLOSED_SEPARATOR/04_EXPLICIT_COORDINATES.md), and §I.A below. They are not assumed to follow from ordinary point-set equality:

1. **Finite-vertex separation:** any patch-compact $C\subseteq P$ meeting $E$ finitely has compact component-saturated closure $C^{\rm sat}$ meeting $E$ finitely. Its complement is a quotient-open neighborhood of $p_\infty$ disjoint from $C$.
2. **Actual fibre and pointlessness:** the point pullback $G$ is the meet of the complementary opens of the finite-vertex cutoffs (positive **and negative** tests); $\Lambda$ has no ordinary patch points.
3. **Special patch comparison:** $\Lambda\to G$ is an isomorphism, hence $F_\infty\to B$ is an isomorphism over $X^2$. No general properness or arbitrary image/base-change theorem for $p$ is used.
4. **Cutoff rigidity:** $K\wedge(C\times C)\le H$ for each saturated finite-vertex cutoff $C$. The coframe lemma gives $K=H\vee B$.
5. **Ordinary fence geometry:** every late $\alpha$-fence meets $U_\alpha$, and the corresponding endpoints in $M$ are dense with unbounded indices in every nonempty relatively open part of $M$.

The compact regular patch square is fit: every one of its sublocales is an intersection of patch-open sublocales. The standard open-map density lemma is recorded in §IV.

### I.A. The repaired special patch-fibre comparison

We record the previously missing argument **for arbitrary unions**. This is the only patch/upper comparison used to transport the generic-square inclusion; it makes no assertion that the full patch map $p$ is proper.

For a Euclidean patch-open subset $O\subseteq P$, its largest upper-open core is

$$
r(O)=\{x\in P:\uparrow x\subseteq O\}
=P\setminus\downarrow(P\setminus O).
$$

It is patch-open as well as upper-open, by compactness of $P\setminus O$ and closedness of the order. Every point of $O\setminus r(O)$ is a **minimal fence vertex** with a strict successor outside $O$. Such a vertex is among the finitely many early fence vertices in any compact subset of $O$, since every corresponding edge must cross the positive distance to $P\setminus O$, whereas all sufficiently late strict edges are uniformly shorter. Thus $O\setminus r(O)$ is relatively patch-closed and locally finite in $O$; as a relatively closed sublocale of the patch-open $O$, it is spatial and discrete.

**Lemma A (arbitrary-union defect).** Let $(O_i)_{i\in I}$ be an arbitrary family of patch opens and set

$$
V=\bigcup_iO_i,\qquad
W=r(V),\qquad U=\bigcup_i r(O_i).
$$

The relative closed complement $F=W\setminus U$ is a spatial **discrete sublocale of the upper-open locale $W$**, supported on a locally finite collection of ordinary minimal fence vertices. In particular, if $S\le X$ is a sublocale through which no such vertex point $1\to X$ factors, then $S\wedge F=0$.

**Proof.** The inclusion $U\subseteq W$ is upper-open. If $v\in W\setminus U$ were nonminimal, then $\uparrow v=\{v\}$; since $v\in V$ it would lie in some $O_i$ and hence in $r(O_i)$, a contradiction. Thus every point of $F$ is minimal.

Fix $x\in W$ and choose patch-open neighborhoods $N',N$ of $x$ with

$$
\overline{N'}\subseteq N,\qquad \overline N\subseteq W,
$$

where the closures are compact. Since $\overline N\subseteq V=\bigcup_iO_i$, finitely many of the $O_i$ cover $\overline N$. Let $\delta>0$ be a Lebesgue number for this finite cover restricted to $\overline N$, and let $\varepsilon=\operatorname{dist}(\overline{N'},P\setminus N)>0$. By uniform edge shrinking, after discarding finitely many early fences, every strict edge has length less than $\min(\varepsilon,\delta/3)$. For a minimal vertex $v\in N'$ on such a late fence, its upper cone consists of $v$ and at most two maximal neighbors. This cone lies inside $N\subseteq\overline N$ and has diameter less than $\delta$. It therefore lies in one member $O_i$ of the finite cover, so $v\in r(O_i)\subseteq U$. Hence

$$
F\cap N'\subseteq\{\text{minimal vertices of finitely many early fences}\}.
$$

This proves local finiteness in the patch topology. It is also relatively patch-closed since $U$ is patch-open. To verify the **upper-locale** assertion, fix $v\in F$. The finite cone $\uparrow v\subseteq W$ admits a patch-open neighborhood $A\subseteq W$ with $A\cap F=\{v\}$: use local finiteness around each cone point, together with relative patch-closedness of $F$. Then $r(A)$ is upper-open, contains $v$, and meets $F$ exactly at $v$. Thus the topology on the closed sublocale $F$ induced from the upper-open locale $W$ is discrete. Because $W$ is spatial and $F$ is its closed sublocale, this is a spatial discrete locale, not merely a discrete set of its points.

Every sublocale of a discrete locale is spatial: for the powerset frame, each nucleus has the form $j(A)=A\cup j(\varnothing)$. A nonzero sublocale of $S\wedge F$, if one existed, would therefore contain a point mapping both into $S$ and to a forbidden minimal vertex. This contradicts the hypothesis. $\square$

**Proposition B (special comparison).** Under the hypothesis on $S$ in Lemma A, the canonical map

$$
p^{-1}S=P_{\mathrm{patch}}\times_XS\longrightarrow S
$$

is an isomorphism.

**Proof.** Let $\lambda:\mathcal O(X)\to\mathcal O(S)$ denote the restriction frame map. The operation $r$ preserves finite intersections and $r(O)=O$ on upper opens. For a family $(O_i)$, Lemma A annihilates the closed complement of $U=\bigcup_i r(O_i)$ in $W=r(\bigcup_iO_i)$ on $S$; the open/closed complement identities then give

$$
\lambda r\Bigl(\bigcup_iO_i\Bigr)
=\lambda\Bigl(\bigcup_i r(O_i)\Bigr)
=\bigvee_i\lambda r(O_i).
$$

Consequently $\lambda r:\mathcal O(P_{\mathrm{patch}})\to\mathcal O(S)$ is a frame homomorphism restricting to $\lambda$ on upper opens. It is a retraction of the canonical frame map $\mathcal O(S)\to\mathcal O(p^{-1}S)$, so the latter is injective.

For surjectivity, use the single-open defect $O\setminus r(O)$ described before Lemma A. Its patch-locale sublocale is spatial discrete, supported on forbidden minimal vertices; its pullback to $p^{-1}S$ is zero, since a point in any nonzero part of that discrete pullback would induce a forbidden point of $S$. Thus every patch-open generator has on $p^{-1}S$ the same restriction as its upper core $r(O)$. Patch opens generate $\mathcal O(p^{-1}S)$ over $\mathcal O(S)$, so the canonical frame map is surjective as well. $\square$

For $S=G$, the finite component containing any ordinary minimal vertex has a saturated upper-open complement belonging to the positive generic filter and omitting the vertex. Hence no such point factors through $G$, and Proposition B gives

$$
\boxed{\Lambda=p^{-1}G\simeq G,\qquad F_\infty=\Lambda^2\simeq G^2.}
$$

**Scope.** The uniform shrinking bound for all strict edges is essential to Lemma A. Neither Proposition B nor anything below asserts properness of the full patch map or general image/base-change preservation.

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

**Proof.** Build a binary tree of closed product rectangles $R_s=I_s\times J_s$ of diameters tending to zero, with anchors $z_s\in C_1\cap\operatorname{int}R_s$. At depth $n$, child $s0$ inherits $z_s$. Choose the new anchor for child $s1$ in $C_1\cap\operatorname{int}R_s$, avoiding the two coordinate values of $z_s$, with its first coordinate in $E_\alpha$ if $n$ is even and its second coordinate in $E_\beta$ if $n$ is odd. Lemma 2 supplies this point after removing two nowhere-dense coordinate sections. Choose small child rectangles **with both anchors in their interiors**, inside the parent, whose first-coordinate intervals are disjoint and whose second-coordinate intervals are disjoint. Repeat the interior condition at every step: an anchor inherited by any all-zero descendant lies in the interior of *every* rectangle on that descendant chain. Different parents already have disjoint coordinate intervals, so no cross-parent coordination is necessary.

Every infinite branch gives a unique point of $C_1$ by compactness and shrinking diameters; the resulting $\Gamma$ is homeomorphic to $2^\omega$. Disjointness of coordinate intervals at the first branch divergence makes both projections injective; compactness and Hausdorffness make them homeomorphisms onto the Cantor sets $D_i$. Any cylinder has descendants at arbitrarily late even and odd levels. The selected anchor of a child $s1$ persists on its all-zero tail. Thus both designated selected traces meet every cylinder and are dense. $\square$

## IV. Dense strips and the actual image composition

**Open-map density fact.** If $f:Y\to Z$ is an open surjection, inverse images of dense sublocales are dense; images of dense sublocales are dense. For the first assertion, given nonzero open $W\le Y$, its open image $f[W]$ meets the dense sublocale of $Z$, and the restricted open surjection $W\to f[W]$ remains surjective after base change. For the second, every nonzero open of $Z$ has nonzero open inverse image meeting the dense sublocale of $Y$, whose image then meets the original open. In any locale $Z$, its double-negation sublocale $\mathcal B(Z)$ lies in every dense sublocale. Nonempty spatial factors here make the relevant product projections open surjections.

**Lemma 4 (strips without antichains).** Suppose $D\subseteq P$ is compact perfect and $D\cap E_\alpha$ is dense. Then

$$
\mathcal B(D\times M)\le(D\times M)\wedge\widehat T,
\quad
\mathcal B(M\times D)\le(M\times D)\wedge\widehat T.
$$

**Proof.** All products and coordinate projections in this paragraph are **patch-localic**, followed by the maps to their corresponding upper locales via $p$. In every nonempty basic patch-open $A\times V\subseteq D\times U_\alpha$, the relatively open $A$ contains selected vertices from arbitrarily late $\alpha$-fences (perfectness plus density), and each sufficiently late such fence meets $V$. Thus ordinary component-related pairs are dense in $D\times U_\alpha$, and the point-generated relation $H$ contains their patch images. Therefore

$$
\mathcal B(D\times U_\alpha)\le\widehat H.
$$

Similarly, the $\alpha$-fence endpoints are dense in $M$, with arbitrarily late indices in every open, giving $\mathcal B(U_\alpha\times M)\le\widehat H$. In $Y=D\times U_\alpha\times M$, pull back these dense sublocales along the two open-surjective patch product projections. Both inverse images contain $\mathcal B(Y)$, so the map $\mathcal B(Y)\to X^3$ factors through the **actual** localic pullback $H\times_XH$. Its outer-coordinate map factors through $T$. The open-surjective projection $Y\to D\times M$ has dense image on $\mathcal B(Y)$; that image contains $\mathcal B(D\times M)$ and is contained in the pullback of $T$. This proves the first assertion. The second is symmetric, since $H$ is symmetric. At no point is $D$ assumed an antichain. $\square$

**Lemma 5 (graph-restricted witness).** If $\Gamma\subseteq P^2$ is a compact Cantor graph whose projections are homeomorphisms onto $D_1,D_2$ satisfying Lemma 3, then

$$
0\ne\mathcal B(\Gamma)\le\Gamma\wedge\widehat R.
$$

**Proof.** Lemma 4 gives $\mathcal B(D_1\times M)\le\widehat T$ and $\mathcal B(M\times D_2)\le\widehat T$. On $\Gamma\times M$, the two patch maps $(z,m)\mapsto(\pi_1z,m)$ and $(z,m)\mapsto(m,\pi_2z)$ to those products are homeomorphisms. Thus both pulled-back strips contain $\mathcal B(\Gamma\times M)$, and its upper triple map factors through $T\times_XT$. The outer map therefore factors through $R$. The patch projection $\Gamma\times M\to\Gamma$ is open surjective, so its image of $\mathcal B(\Gamma\times M)$ is dense and contains $\mathcal B(\Gamma)$. The latter is nonzero because $\Gamma$ is a nonempty Cantor locale; no ordinary point of its Booleanization is required. **No claim $\mathcal B(\Gamma)\le F_\infty$ is made or needed.** $\square$

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

## VII. Independent-audit disposition

| Claim | Status after 19 November blind review and 20 November repair |
| --- | --- |
| Explicit coordinates, strong forcing, quotient point, cutoffs | Independently checked, no substantive objection |
| Exact point-fibre and finite-cutoff rigidity | Independently checked, no substantive objection |
| Special pointless patch-fibre isomorphism | **Qualified:** arbitrary-union defect gap identified; independent compactness repair supplied and incorporated above |
| Fixed-colour Baire support lemma | Independently checked |
| Binary Cantor graph with no component registries | Independently checked |
| Antichain-free dense strips and graph-restricted image | Independently checked |
| Direct closed-separator contradiction | Independently checked |
| $\mathcal B(M)$ nonzero generic-fibre witness | Independently checked |
| Four-step equality and equivalence hull | Independent verdict: valid with specified repair and clarifications; now incorporated |

The earlier ternary antichain fusion, its registry invariant, the global join of Booleanized graphs, and individual graph factorization through the generic fibre are **not** dependencies of the present proof. No strict inequality between intermediate powers is claimed. The original independent referee report and an exact [reconciliation](ProjectA_FourStep_Binary_ClosedSeparator_External_Audit_Reconciliation_2026-11-20.md) are recorded in the [blind-audit archive](project-a/audits/2026-11-19/FOURSTEP_BINARY_CLOSED_SEPARATOR/README.md); the referee has **not** undertaken a second audit of this revised text.
