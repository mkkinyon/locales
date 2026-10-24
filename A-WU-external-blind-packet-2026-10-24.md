# Project A — External blind mathematical audit packet

**Subject:** The equality \(\mathcal W=\mathcal U\) in localic separation theory, with special attention to whether \(\mathcal W_2=\mathcal U\) forces \(\mathcal W=\mathcal U\).  
**Date:** 24 October 2026.  
**Status:** Working arguments and examples submitted for **independent adversarial audit**, not a finished paper. Every theorem, proof and example below is open to challenge. No novelty claim is made.

## 0. Motivation and two levels of the problem

We are translating separation relations inspired by Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces* (2026), into localic relations (sublocales of \(X\times X\)). The main relations include the closed inseparability relation \(\mathcal I\), the closed Urysohn relation \(\mathcal U\), and the fitted diagonal \(\mathcal D=\operatorname{fit}(\Delta)\). In coherent frames an audited project theorem says \(\operatorname{cl}(\mathcal D)=\mathcal U\). This identity **can fail** for compact noncoherent frames. Explaining the equality or its failure for arbitrary frames is the **general research goal**.

Put \(\mathcal W=\operatorname{cl}(\mathcal D)\). The investigation found that neighborhoods defined by *binary* covers generate \(\mathcal U\) after taking closures. This suggests defining \(\mathcal D_2\) using only binary covers, and \(\mathcal W_2=\operatorname{cl}(\mathcal D_2)\). We have \(\mathcal W\le\mathcal W_2\le\mathcal U\). The **specific focal problem** is

\[
\boxed{\mathcal W_2=\mathcal U\stackrel{?}{\Longrightarrow}\mathcal W=\mathcal U\quad\text{for arbitrary frames}.}
\tag{Q}
\]

(Q) is proved below for several families, including compact frames, but remains **undecided** in this packet. We also exhibit \(\mathcal D_2\ne\mathcal D\) with \(\mathcal W_2=\mathcal W=\mathcal U\); this explicitly does **not** disprove (Q). All inclusions between sublocales are **actual localic inclusions**, never merely point-set inclusions.

## 1. Definitions and conventions

Let \(L\) be an arbitrary frame, \(X\) its locale, and \(Q=L\oplus L=\mathcal O(X\times X)\) the frame coproduct. For \(a,b\in L\), write \(a\boxtimes b=(a\boxtimes1)\wedge(1\boxtimes b)\) for a pure rectangle, where the coordinate frame injections are understood. The diagonal inverse image is \(\delta^*:Q\to L\), \(\delta^*(a\boxtimes b)=a\wedge b\). All implications and pseudocomplements \(q\to r\), \(q^*=q\to0\) appearing without a subscript are computed in \(Q\).

For \(q\in Q\), let \(O(q)\) be the **open sublocale** (nucleus \(x\mapsto q\to x\)), and \(C(q)\) the **closed sublocale** (nucleus \(x\mapsto q\vee x\)). Thus

\[
\operatorname{cl}(O(q))=C(q^*),\quad
\operatorname{int}(C(q))=O(q^*),\quad
C(q)\subseteq O(w)\iff q\vee w=1.
\]

Closed sublocales satisfy \(\bigcap_iC(q_i)=C(\bigvee_iq_i)\); if \(C(q)\subseteq C(r)\), then \(r\le q\). The closure of the diagonal is \(\mathcal I=C(d_I)\), where

\[
d_I=\bigvee_{a\wedge b=0}a\boxtimes b.
\]

The Urysohn relation is \(\mathcal U=C(d_U)\), where

\[
d_U=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
\]

with \(a^*,b^*\) taken in \(L\). Its standard interpretation for spatial products: two points are \(\mathcal U\)-related precisely when they have no open neighborhoods with disjoint closures. We use the previously established universal comparison \(\mathcal I\subseteq\mathcal U\).

Define the **diagonal-neighborhood filter**

\[
\mathscr B_\Delta=\{w\in Q:\delta^*(w)=1\},
\quad\mathcal D=\operatorname{fit}(\Delta)
=\bigcap_{w\in\mathscr B_\Delta}O(w),
\quad\mathcal W=\operatorname{cl}(\mathcal D)=C(d_W).
\]

For any cover \(\mathscr C\subseteq L\) (\(\bigvee\mathscr C=1\)), put

\[
w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c.
\]

For \(a\vee b=1\), write \(v(a,b)=a\boxtimes a\vee b\boxtimes b\). Finally define

\[
\mathcal D_2=\bigcap_{a\vee b=1}O(v(a,b)),
\qquad\mathcal W_2=\operatorname{cl}(\mathcal D_2)=C(d_{W_2}).
\]

**Standard coproduct facts used in this packet and explicitly offered for audit:** rectangles join-generate \(Q\); \(a\boxtimes b=0\) iff \(a=0\) or \(b=0\); and

\[
(a\boxtimes b)^*=(a^*\boxtimes1)\vee(1\boxtimes b^*).
\tag{R}
\]

For topological interpretations, assume \(X\) is sober and the localic square is spatial **and equals the ordinary topological product**; this holds in the locally compact sober examples below. Spatiality of the ambient square does **not** imply arbitrary sublocales are spatial.

## 2. Diagonal-neighborhood theorem and full fixed-point condition

**Claim A1 (arbitrary frame).**

\[
\boxed{d_U=\bigvee_{w\in\mathscr B_\Delta}w^*,\qquad
\mathcal U=\bigcap_{w\in\mathscr B_\Delta}\operatorname{cl}(O(w)).}
\tag{A1}
\]

*Proposed proof.* Take \(w\in\mathscr B_\Delta\), write \(w=\bigvee_i p_i\boxtimes q_i\), and put \(c_i=p_i\wedge q_i\). Then \(\bigvee_i c_i=1\) and \(\bigvee_i c_i\boxtimes c_i\le w\). If \(a\boxtimes b\le w^*\), then for each \(i\), \((a\wedge c_i)\boxtimes(b\wedge c_i)=0\); by the rectangle-zero property, \(c_i\le a^*\) or \(c_i\le b^*\). Hence \(a^*\vee b^*=1\), so every rectangle below \(w^*\) is below \(d_U\). Thus \(w^*\le d_U\). Conversely, given \(a^*\vee b^*=1\), set \(r=a\boxtimes b\); by (R), \(\delta^*(r^*)=a^*\vee b^*=1\), hence \(r\le r^{**}\le\bigvee_{w\in\mathscr B_\Delta}w^*\). Join all far rectangles. Closed-sublocale calculus yields the second equality.

**Claim A2 (full diagonal pre-nucleus).** Define

\[
\Phi(q)=\bigvee_{w\in\mathscr B_\Delta}(w\to q).
\]

This is exactly \(\kappa_L\) in Arrieta–Picado–Pultr (2022), **Lemma 5.4**, and is already known to be a pre-nucleus. Its fixed-point frame is the intersection of the open nuclei for \(w\in\mathscr B_\Delta\), i.e. \(\mathcal D\). Iteration to the least fixed point above zero produces \(d_W\). From A1,

\[
\boxed{\Phi(0)=d_U,\qquad
\mathcal W=\mathcal U\iff\Phi(d_U)=d_U.}
\tag{A2}
\]

Equivalently, for every cover \(\mathscr C\) and \(a,b\in L\):

\[
\left[\forall c\in\mathscr C,
(a\wedge c)\boxtimes(b\wedge c)\le d_U\right]
\Longrightarrow a\boxtimes b\le d_U.
\tag{A3}
\]

The basis argument: every \(w\in\mathscr B_\Delta\) majorizes some square-cover \(w_{\mathscr C}\), and implications reverse order in the antecedent. Condition (A3) is called **arbitrary-cover rectangle descent** here, as descriptive shorthand only.

## 3. Binary neighborhoods: universal identities and finite-cut lemma

**Claim B1 (arbitrary frame).** For \(a\vee b=1\),

\[
v(a,b)^*=a^*\boxtimes b^*\vee b^*\boxtimes a^*,
\]

and consequently

\[
\boxed{d_U=\bigvee_{a\vee b=1}v(a,b)^*
=\bigvee_{a\vee b=1}a^*\boxtimes b^*.}
\tag{B1}
\]

*Sketch.* Expand the pseudocomplement of the join of the two square rectangles via (R). Terms involving \(a^*\wedge b^*\) vanish. Each binary \(v(a,b)\) belongs to \(\mathscr B_\Delta\), so its pseudocomplement is \(\le d_U\). Conversely, if \(u^*\vee v^*=1\), take binary cover \(a=u^*,b=v^*\); then \(u\boxtimes v\le u^{**}\boxtimes v^{**}\le v(a,b)^*\). This proves (B1), and also

\[
\mathcal U=\bigcap_{a\vee b=1}\operatorname{cl}(O(v(a,b)))
\quad\text{for every frame.}
\]

**Claim B2 (finite-cut identity).** If \(c_1\vee\cdots\vee c_n=1\), let \(a_S=\bigvee_{i\in S}c_i\) and \(b_S=\bigvee_{i\notin S}c_i\). Then

\[
\boxed{\bigvee_{i=1}^n c_i\boxtimes c_i
=\bigwedge_{S\subseteq[n]}v(a_S,b_S).}
\tag{B2}
\]

*Proposed proof.* Both expressions lie in the finite bounded distributive lattice coproduct generated by the \(c_i\)'s in two coordinates. The left side is at most each right-hand factor. For a pair of prime filters \((P,R)\) of the finite lattice, the left side is true iff some \(c_i\) belongs to both filters. If none does, choose \(S=\{i:c_i\in P\}\); the cover assumption ensures \(S\) and its complement are nonempty, and neither \(a_S\) nor \(b_S\) belongs to both filters. The corresponding right-hand factor fails. Therefore equality holds in the finite distributive coproduct and hence in \(Q\). We specifically ask the referee to verify that the transport into the *frame* coproduct is legitimate.

**Claim B3 (compact binary-basis theorem).** If the frame top \(1\) is compact, every diagonal neighborhood majorizes a **finite meet** of binary neighborhoods \(v(a,b)\), by extracting a finite subcover and applying B2. Hence

\[
\boxed{\mathcal D_2=\mathcal D,
\quad\mathcal W=\mathcal U
\iff\forall a\vee b=1,\quad v(a,b)\to d_U=d_U.}
\tag{B3}
\]

For general \(L\), this binary condition is not yet known to imply \(\mathcal W=\mathcal U\).

## 4. The binary operator and relative density

Define

\[
\Psi(q)=\bigvee_{a\vee b=1}(v(a,b)\to q).
\]

**Caution:** No assertion is made that \(\Psi\) preserves finite meets or is a pre-nucleus. The binary family is not known to be closed under finite meets. The claims needed here are: \(\Psi\) is monotone and inflationary, its fixed points are exactly the joint fixed points of all the binary open nuclei, and its least fixed point above \(0\) is \(d_{W_2}\). From B1,

\[
\boxed{\Psi(0)=d_U,\qquad
\mathcal W_2=\mathcal U\iff\Psi(d_U)=d_U.}
\tag{C1}
\]

The order is always \(\mathcal D\subseteq\mathcal D_2\subseteq\mathcal U\) and \(\mathcal W\subseteq\mathcal W_2\subseteq\mathcal U\). The fixed-point condition means each binary neighborhood restricts to a **dense** open of \(\mathcal U\), as opposed to covering \(\mathcal U\) entirely (which is the stronger equality \(\mathcal D=\mathcal U\)).

## 5. Compatible pairs of homomorphisms and broader positive cases

Given frame homomorphisms \(h,k:L\to M\), call them **finite-cover compatible** if

\[
\bigvee_{c\in\mathscr C}(h(c)\wedge k(c))=1_M
\]

for every finite cover \(\mathscr C\) of \(1_L\). Call them **cover compatible** if the same holds for arbitrary covers. These are frame homomorphisms, not almost homomorphisms; the arbitrary-cover notion is established in Arrieta–Picado–Pultr (2022), Lemma 4.4.

**Claim C2 (functorial test).** The unique frame map \(f:Q\to M\) induced by \(h,k\) factors through \(\mathcal D_2\) iff the pair is finite-cover compatible, and through \(\mathcal D\) iff it is cover compatible. Thus

\[
\boxed{\mathcal D_2=\mathcal D\iff
\substack{\text{finite-cover compatibility implies all-cover compatibility}\\\text{for all frame targets }M}}
\tag{C2}
\]

For finite covers, use B2; for arbitrary covers, use the square-cover presentation of \(\mathcal D\). The reverse direction of C2 is tested using the coordinate maps into \(\mathcal O(\mathcal D_2)\).

**Claim C3 (spatial targets).** If \(M\) is spatial, finite-cover compatibility automatically implies all-cover compatibility. Proof: compose \(h,k\) with each point of \(M\). For a hypothetical cover with no common member at one point, split the cover into elements accepted by the first point and their complement; joining each part gives a binary cover contradicting compatibility. Spatiality detects the equation in \(M\). Hence \(\mathcal D\) and \(\mathcal D_2\) have the same maps from all spatial test locales, and their ordinary point sets agree.

**Claim C4 (compact complemented cover).** If \(1=\bigvee_i e_i\), with each \(e_i\) both compact and complemented in \(L\), then \(\mathcal D_2=\mathcal D\) even when \(1\) is noncompact. Proof: binary compatibility for \(e_i\vee e_i^c=1\) forces \(h(e_i)=k(e_i)=m_i\). For any cover \(\mathscr C\) select finitely many \(c_j\in\mathscr C\) covering \(e_i\). Apply finite compatibility to the cover \(e_i^c,c_1\wedge e_i,\ldots,c_n\wedge e_i\), then meet with \(m_i\):

\[
m_i\le\bigvee_{j=1}^n h(c_j)\wedge k(c_j)
\le\bigvee_{c\in\mathscr C} h(c)\wedge k(c).
\]

Join over \(i\), using \(\bigvee_i m_i=1\). Then invoke C2. This includes arbitrary sums of compact locales and other compact-clopen-covered locales. **This criterion does not itself imply \(\mathcal W=\mathcal U\); it makes the binary test exact.**

## 6. Canonical Boolean target and countable distributivity

Let \(N=\mathcal O(\mathcal U)=\uparrow d_U\), and let \(\beta:N\to B(N)\) be the double-negation (Booleanization) quotient. Define

\[
h(a)=\beta(d_U\vee(a\boxtimes1)),\qquad
k(a)=\beta(d_U\vee(1\boxtimes a)).
\]

These are two **canonical frame homomorphisms** \(L\to B(N)\).

**Claim D1 (canonical Boolean reduction).** For any cover \(\mathscr C\),

\[
\bigvee_{c\in\mathscr C}h(c)\wedge k(c)
=\beta(d_U\vee w_{\mathscr C})
=1\iff w_{\mathscr C}\to_Qd_U=d_U.
\]

The last equivalence is density inside the interval frame \(\uparrow d_U\). Therefore

\[
\boxed{\mathcal W_2=\mathcal U\iff(h,k)\text{ finite-cover compatible},\quad
\mathcal W=\mathcal U\iff(h,k)\text{ cover compatible}.}
\tag{D1}
\]

This replaces a search over arbitrary targets by this canonical Boolean target. In particular, if \(B(N)\) is **atomic** (and hence spatial), C3 implies the focal implication (Q).

**Claim D2 (countable-distributivity extension).** Let \(B\) be a complete Boolean algebra satisfying \((\omega,2)\)-distributivity:

\[
\bigvee_{\varepsilon\in2^{\mathbb N}}
\bigwedge_{n\in\mathbb N} b_n^{\varepsilon(n)}=1
\]

for every sequence \((b_n)\), where \(b_n^1=b_n\), \(b_n^0=\neg b_n\). Then every finite-cover-compatible pair \(h,k:L\to B\) respects countable covers. Proof: if a countable cover \(\{c_n\}\) failed, below the nonzero Boolean complement of \(\bigvee_n(h(c_n)\wedge k(c_n))\) select a nonzero Boolean piece deciding all the values of \(h(c_n)\), \(k(c_n)\) simultaneously. Partition indices according to acceptance by \(h\); the two joins of \(c_n\) form a binary cover whose compatibility equation vanishes on that nonzero piece. Contradiction.

Thus if **every cover of \(1_L\) has a countable subcover** and \(B(N)\) is countably distributive, (Q) holds. This is a distinct sufficient hypothesis, not a claim that every complete Boolean algebra is countably distributive.

## 7. Arbitrary-family regular core and boundary localization

**Claim E1 (general closure–intersection statement).** Let \(Y\) be any locale and \(w_i\in\mathcal O(Y)\). Set

\[
S=\bigcap_i O(w_i),\quad
T=\bigcap_i\operatorname{cl}(O(w_i))=C(d),\quad
 d=\bigvee_iw_i^*,\quad \operatorname{cl}(S)=C(e).
\]

Then

\[
\boxed{d\le e\le d^{**},\quad
\operatorname{int}(\operatorname{cl}S)=\operatorname{int}(T),\quad
\operatorname{cl}(\operatorname{int}T)\subseteq\operatorname{cl}(S)\subseteq T.}
\tag{E1}
\]

*Proposed proof.* \(S\subseteq T\) gives \(d\le e\). Put \(r=d^{**}\). For each \(i\), \(w_i^*\le d\le r\). If \(z=w_i\to r\), then \(z\wedge w_i\le r\), whence \(z\wedge r^*\le w_i^*\le r\), so \(z\wedge r^*=0\). Thus \(z\le r^{**}=r\), and in fact \(w_i\to r=r\). Therefore \(r\) is in the fixed-point frame of \(S\), so its least element \(e\) is \(\le r\). Pseudocomplementation gives \(d^*=e^*\); then use \(\operatorname{int}C(x)=O(x^*)\). The general lemma's place in the literature is **unchecked**.

For our diagonal family, (E1) yields

\[
\boxed{d_U\le d_W\le d_U^{**},\qquad
\operatorname{cl}(\operatorname{int}\mathcal U)
\subseteq\mathcal W\subseteq\mathcal U.}
\tag{E2}
\]

In particular \(\mathcal W\) and \(\mathcal U\) have equal interiors, and **regular-closedness of \(\mathcal U\)** suffices for \(\mathcal W=\mathcal U\). This is not necessary, e.g. the usual real-line diagonal has empty interior but \(\mathcal W=\mathcal U=\Delta\).

**Claim E3 (nonregular boundary sector).** With \(d=d_U\), put

\[
K=C(d^{**})=\operatorname{cl}(\operatorname{int}\mathcal U),\quad
G=\mathcal U\wedge O(d^{**}).
\]

Then \(\mathcal U=K\vee G\), \(K\le\mathcal W\le\mathcal W_2\le\mathcal U\), and

\[
\boxed{\mathcal W=\mathcal U\iff \mathcal D\wedge G\text{ dense in }G,
\quad\mathcal W_2=\mathcal U\iff \mathcal D_2\wedge G\text{ dense in }G.}
\tag{E3}
\]

The proposed justification uses closure commuting with restriction to an open sublocale. Only the sector \(G\), not the regular-closed core \(K\), can support failure of (Q).

**Claim E4 (boundary-local Boolean sufficiency).** If \(B(\mathcal O(G))\) is atomic/spatial, (Q) holds, via the canonical coordinate pair restricted to \(G\) and spatial-target compatibility C3. If \(L\) is Lindelöf and \(B(\mathcal O(G))\) is countably distributive, (Q) also holds by D2. The referee should check the relative frame and Booleanization conventions carefully.

## 8. Explicit infinitary counterexample at the fitted-sublocale level

Set

\[
S=\mathcal P(\mathbb N)\setminus\{\varnothing\}
\]

with the Scott topology inherited from the powerset dcpo. Write \(c_n=\{A\in S:n\in A\}\). The \(c_n\) are compact opens covering \(1\) without a finite subcover; finite intersections \(c_F\) form a compact-open basis. The frame \(L=\mathcal O(S)\) is algebraic, locally compact, sober, and noncompact. It has a presentation with generators \(c_n\) subject to the additional cover \(\bigvee_n c_n=1\).

Let \(K=2^{\mathbb N}\) be the ordinary Cantor space and \(B=\operatorname{RO}(K)\), its complete regular-open Boolean algebra. Let \(A_n=\{z:z_n=0\}\), \(B_n=\{z:z_n=1\}\), complementary clopen cylinders. Each assignment \(c_n\mapsto A_n\) and \(c_n\mapsto B_n\) respects the generator relations because \(\bigvee_n A_n=\bigvee_n B_n=1_B\); thus each extends to a frame homomorphism \(h,k:L\to B\). For **every infinite** \(J\subseteq\mathbb N\), \(\bigvee_{n\in J}A_n=\bigvee_{n\in J}B_n=1_B\) because each corresponding ordinary union is dense in Cantor space.

**Claim F1 (strict finite-versus-full compatibility).** \(h,k\) respect all finite covers of \(L\), but not \(\{c_n:n\in\mathbb N\}\). For a finite cover \(u_1,\ldots,u_m\) of \(S\), every singleton point \(\{n\}\) belongs to some \(u_j\); any Scott-open containing \(\{n\}\) contains the whole \(c_n\). By infinite pigeonhole, one \(u_j\) contains infinitely many \(c_n\), so \(h(u_j)=k(u_j)=1_B\). But \(h(c_n)\wedge k(c_n)=A_n\wedge B_n=0\), so the countable cover fails.

It follows by C2 that

\[
\boxed{\mathcal D_2(S)\ne\mathcal D(S).}
\tag{F1}
\]

**Crucial limitation:** every nonempty Scott open contains the top point \(\mathbb N\). Therefore \(d_I=d_U=0\) and \(\mathcal I=\mathcal U=S^2\). The universal chain gives

\[
\boxed{\mathcal W(S)=\mathcal W_2(S)=\mathcal U(S)=S^2.}
\tag{F2}
\]

The example does **not** refute (Q). It demonstrates that a nonzero pointless difference \(\mathcal D_2\setminus\mathcal D\) need not change closed hulls. \(\operatorname{RO}(2^{\mathbb N})\) is not countably distributive: the full coordinate partitions have no nonzero regular-open simultaneous assignment, consistent with D2.

## 9. Nontrivial U without a counterexample to (Q)

Let \(P\) be the finite upper-Alexandrov zigzag \(0<5>1<4>2<3\), and put \(X=S\times P\), with \(S\) as in §8.

**Claim F3 (product stabilization).** \(X\) is locally compact, sober, algebraic and noncompact. Its localic square agrees with the ordinary product. Pointwise relations factor by coordinates:

\[
\operatorname{pt}\mathcal I(X)=S^2\times\operatorname{pt}\mathcal I(P),
\quad\operatorname{pt}\mathcal U(X)=S^2\times\operatorname{pt}\mathcal U(P),
\]

up to permutation of coordinates. In \(P\), \((0,4)\in\mathcal U\setminus\mathcal I\) while \((0,3)\notin\mathcal U\). The closure-meeting relation \(\operatorname{Cm}(S)\) is dense in \(S^2\) because \((\mathbb N,\mathbb N)\) meets every nonempty basic product open. The finite coherent result gives \(\overline{\operatorname{Cm}(P)}=\operatorname{pt}\mathcal U(P)\). Hence the ordinary closure-meeting relation in \(X\) is dense in \(\mathcal U(X)\); the closed hull \(\mathcal W\), containing these points, equals \(\mathcal U\). Composing the maps from §8 with the inverse image of a point-slice \(S\to S\times P\) transfers the strict finite/infinite-cover defect. Thus

\[
\boxed{\mathcal I(X)\subsetneq\mathcal W(X)=\mathcal U(X)
\subsetneq X^2,\qquad \mathcal D(X)\subsetneq\mathcal D_2(X).}
\tag{F3}
\]

Again this is a **nontrivial control example, not a counterexample to (Q)**.

## 10. A nonspatial fitted diagonal in a compact sober T₁ space

Take \(Y=\mathbb R\) with its usual topology, an infinite discrete set \(Z\), and adjoin \(p\). Set \(X=Y\sqcup Z\sqcup\{p\}\). Old-part opens are as in the topological sum; a basic neighborhood of \(p\) is \(\{p\}\cup((Y\sqcup Z)\setminus F)\) for \(F\) finite.

**Claim F4 (cofinite-apex control).** \(X\) is compact, locally compact, sober and \(T_1\). Every \(z\in Z\) is clopen, while all nonempty opens of \(Y\) have \(p\) in their closure. Its ordinary Urysohn point relation is

\[
R_U=(Y\cup\{p\})^2\cup\Delta_Z,
\]

and \(\mathcal I\subsetneq\mathcal U\subsetneq X^2\). The closed \(\mathcal U\) is **regular closed**: \(Y\times Y\) and the isolated diagonal points \((z,z)\) are ambient open portions of \(R_U\) whose union is dense in \(R_U\). Thus E2 gives \(\mathcal W=\mathcal U\).

However \(X\) is \(T_1\), so the only ordinary points of \(\mathcal D\) are diagonal pairs. If \(\mathcal D\) were spatial, \(\mathcal W=\operatorname{cl}(\Delta)=\mathcal I\), contradicting \(\mathcal I<\mathcal U\). Therefore \(\mathcal D\) is genuinely **nonspatial**. For disjoint nonempty real intervals \(A,B\), \(\mathcal D\wedge O(A\boxtimes B)\) is nonzero and pointless. Because \(X\) is compact, \(\mathcal D_2=\mathcal D\) by B3. This example shows the role of pointless density in \(\mathcal W=\mathcal U\) but cannot witness failure of (Q) because its nonregular boundary \(G\) is zero.

The referee is explicitly asked to check the topology, sobriety and regular-closed calculation independently.

## 11. Spatial geometric tests and necessary obstruction certificates

For a sober \(X\) whose localic square is the ordinary topological square, denote by \(R_U\) the closed ordinary point relation of \(\mathcal U\). The ordinary point pairs of \(\mathcal D\) are exactly the closure-meeting pairs

\[
\operatorname{Cm}(X)=\{(x,y):\overline{\{x\}}\cap\overline{\{y\}}\ne\varnothing\}.
\]

**Claim G1.** \(\operatorname{pt}\mathcal D_2=\operatorname{pt}\mathcal D=\operatorname{Cm}(X)\). A common lower specialization point forces both points into any member of a binary cover that contains it. If their singleton closures are disjoint, the binary cover \(X\setminus\overline{\{x\}},X\setminus\overline{\{y\}}\) excludes the pair. Thus any difference \(\mathcal D_2>\mathcal D\) is invisible to ordinary points; and if \(\mathcal D_2\) is spatial, necessarily \(\mathcal D_2=\mathcal D\).

**Claim G2 (geometric binary-density test).** Under the spatial-square hypothesis,

\[
\boxed{\mathcal W_2=\mathcal U\iff
\operatorname{int}_{R_U}(R_U\cap(A\times B))=\varnothing
\text{ for every disjoint closed }A,B\subseteq X.}
\tag{G2}
\]

For \(a\vee b=1\), let \(A=X\setminus a\), \(B=X\setminus b\). The complement of \(v(a,b)\) in the square is \((A\times B)\cup(B\times A)\); relative density of \(v\) in \(R_U\) is equivalent to the relative complement's having empty interior. Use symmetry and finite-union stability of relatively closed nowhere-dense sets.

**Claim G3 (a necessary disjoint-open witness).** If \(\mathcal W<\mathcal U\), since \(\mathcal I\le\mathcal W\), we have \(d_U\le d_W\le d_I\), with \(d_W\not\le d_U\). Rectangular generation and \(d_I=\bigvee_{a\wedge b=0}a\boxtimes b\) yield **disjoint opens** \(a,b\in L\) with

\[
\boxed{a\boxtimes b\not\le d_U,\qquad
\mathcal D\wedge O(a\boxtimes b)=0.}
\tag{G3}
\]

In a spatial square this means \(a\times b\) contains U-related point pairs but no closure-meeting point pairs. This does not contradict G2: G2 quantifies over **disjoint closed** coordinate sets, whereas G3 produces disjoint **open** coordinate sets.

**Claim G4 (infinitary certificate).** If \(\mathcal W_2=\mathcal U\) but \(\mathcal W<\mathcal U\), there is a cover \(\mathscr C\) with no finite subcover and a rectangle \(r=a\boxtimes b\) satisfying

\[
\boxed{r\not\le d_U,
\quad (a\wedge c)\boxtimes(b\wedge c)\le d_U
\text{ for all }c\in\mathscr C.}
\tag{G4}
\]

Reason: failure of \(\Phi(d_U)=d_U\) gives a diagonal neighborhood \(w\) with \(w\to d_U\not\le d_U\); refine it to \(w_{\mathscr C}\le w\); pick a rectangle below \(w_{\mathscr C}\to d_U\) but outside \(d_U\). A finite subcover would contradict B2 and binary density. The sublocale \(\mathcal D_2\wedge O(r)\) is then nonzero and **dense in** \(\mathcal U\wedge O(r)\), but has **no ordinary points**, as \(\mathcal D\wedge O(r)=0\) and \(\operatorname{pt}\mathcal D_2=\operatorname{pt}\mathcal D\).

If in addition the nonregular sector \(G\) of §7 has atomic Booleanization, G4 is impossible by E4. If \(L\) is Lindelöf and the relevant Booleanization is countably distributive, G4 is likewise impossible. Neither sufficient condition is universal.

## 12. What is established, what is not, and the referee's research task

**Claims submitted for independent validation:** A1–A3 (universal neighborhood identity and full fixed-point condition); B1–B3 (binary and finite-cut formulas, compact theorem); C1–C4 (binary operator, categorical finite-cover interpretation, spatial targets, compact complemented cover); D1–D2 (canonical Boolean and countable-distributivity criteria); E1–E4 (regular core and boundary sector); F1–F4 (concrete test examples); G1–G4 (geometric and obstruction lemmas). These have *working* proofs but have **not** received this external referee's independent audit.

**Not claimed:** a proof or disproof of (Q); a novelty theorem about \(\Phi=\kappa_L\); equality of sublocales inferred solely from equal point sets; that nonspatial \(\mathcal D_2\) automatically forces unequal closed hulls; that \(\Psi\) is a pre-nucleus.

**Referee's main tasks:** determine which of A–G are correct; provide explicit corrections or counterexamples to any that fail; assess whether there is an overlooked general theorem settling (Q); and identify a useful alternative formulation of **the general equality \(\mathcal W=\mathcal U\)** and of **the specific focal implication (Q)**.

## References (for the cold read)

- I. Arrieta, J. Picado, A. Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, **Applied Categorical Structures** 30 (2022), 247–263, DOI: 10.1007/s10485-021-09655-9. Authors' preprint: https://www.mat.uc.pt/preprints/ps/p2117.pdf . See particularly §§3–5, Lemmas 4.4 and 5.4. These cover the **already established** arbitrary-cover compatibility and full pre-nucleus.
- J. Picado and A. Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021, particularly the discussion of fitting as another closure.
- P. J. Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783 (2026). Motivation for closure-meeting and Urysohn graphs: https://arxiv.org/abs/2610.14783 .
- For standard Booleanization / countable distributivity background, consult ordinary references on complete Boolean algebras and locales; no source-priority claim about D2 or the countable theorem is made.

**Blind-review instruction:** This packet contains all the context required for the mathematical review. Please do not consult the project's historical audits or notes before writing your independent referee report.