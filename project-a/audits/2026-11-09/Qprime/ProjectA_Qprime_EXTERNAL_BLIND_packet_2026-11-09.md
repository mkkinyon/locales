# Project A — Blind mathematical audit packet for Q′ and W₂

**Prepared 9 November 2026. This packet is for an independent cold read.** It contains **working claims**, not an assertion that those claims are already verified. The accompanying referee prompt explains scope and priorities. Internal audits and earlier referee reports are deliberately excluded.

## Executive orientation

This work is part of a study of binary **localic** separation relations, not simply relations on underlying sets of points. Our next project phase will examine the relation \(\mathcal W\) on its own terms. Before doing so, we wish to audit the substantial body of work on its finite-cover approximation \(\mathcal W_2\).

**Neither open question is claimed to be solved:**
\[
(Q'):\qquad \mathcal W_2=\mathcal W\ \text{for all locales?}
\]
\[
(Q):\qquad \mathcal W_2=\mathcal U\Longrightarrow \mathcal W=\mathcal U\ \text{for all locales?}
\]
The first would imply the second. The packet consists of algebraic reductions and positive theorems, followed by explicit examples showing why natural approaches to a counterexample have failed. Please distinguish **global equalities** from equalities **only on specified open rectangles**.

The sections marked **CORE** should receive priority. The source-note index at the end supplies the unabridged research record; it is supplementary, not a substitute for checking the proofs below.

---

# Part A. Algebraic setting and the exact obstruction — CORE

## A1. Definitions and conventions

Let \(L\) be a frame and \(Q=L\oplus L\), the coproduct of frames (the frame of the localic product). A pure rectangle is written \(a\boxtimes b\); rectangles join-generate \(Q\), with
\[
(a\boxtimes b)\wedge(c\boxtimes d)
  =(a\wedge c)\boxtimes(b\wedge d).
\]
Let \(\delta^*:Q\to L\) be the frame map of the diagonal, \(\delta^*(a\boxtimes b)=a\wedge b\). The diagonal sublocale is \(\Delta\), its fitted hull is \(\mathcal D=\operatorname{fit}(\Delta)\), and \(\mathcal I=\operatorname{cl}(\Delta)\). The Urysohn-style closed relation is \(\mathcal U=C(d_{\mathcal U})\), where
\[
 d_{\mathcal U}=\bigvee\{a\boxtimes b:a^*\vee b^*=1\}.
\]
An individual rectangle with \(a^*\vee b^*=1\) is *far*. For \(q\in Q\), write \(O(q)\) and \(C(q)\) for the open and closed sublocales respectively; \(q^*\) is the frame pseudocomplement. For any cover \(\mathcal C\subseteq L\) with \(\bigvee\mathcal C=1\), put
\[
 w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c.
\]
The diagonal-neighborhood presentation used throughout is
\[
 \mathcal D=\bigcap_{\mathcal C\text{ arbitrary cover}} O(w_{\mathcal C}),
 \qquad
 \mathcal D_2=\bigcap_{F\text{ finite cover}}O(w_F).
\]
Define
\[
 \mathcal W=\operatorname{cl}(\mathcal D)=C(d_{\mathcal W}),\qquad
 \mathcal W_2=\operatorname{cl}(\mathcal D_2)=C(d_0),\quad d_0=d_{\mathcal W_2}.
\]
Universally,
\[
\mathcal D\subseteq\mathcal D_2\subseteq\mathcal U,
\qquad
\mathcal I\subseteq\mathcal W\subseteq\mathcal W_2\subseteq\mathcal U,
\qquad d_{\mathcal U}\le d_0\le d_{\mathcal W}\le d_{\mathcal I}.
\]
These inclusions are prerequisites; please examine any use of them carefully.

For \(a,b\in L\), \(a\prec b\) means \(a^*\vee b=1\) ("rather below"). Frame regularity means \(b=\bigvee\{a:a\prec b\}\) for every \(b\).

The filter of all diagonal square neighborhoods gives a pre-nucleus
\[
 \Phi(x)=\bigvee_{\mathcal C\text{ arbitrary cover}}(w_{\mathcal C}\to x),
\]
and finite-cover neighborhoods give
\[
 \Phi_2(x)=\bigvee_{F\text{ finite cover}}(w_F\to x).
\]
For two covers, their common refinement by pairwise meets has square neighborhood equal to the meet of the original square neighborhoods. Hence the indexing families give actual pre-nuclei (not merely inflationary monotone maps). Their transfinite fixed-point closures have
\[
 \Phi(0)=\Phi_2(0)=d_{\mathcal U},\qquad
 \Phi^\infty(0)=d_{\mathcal W},\qquad
 \Phi_2^\infty(0)=d_0,
\]
so \(\Phi_2(d_0)=d_0\). The full-cover operator is the previously known \(\kappa_L\) operator of Arrieta–Picado–Pultr; no novelty is claimed for it.

A pair of frame homomorphisms \(h,k:L\to M\) (any frame \(M\)) induces \(Q\to M\). It factors through \(\mathcal D_2\) iff
\[
 \bigvee_{c\in F}h(c)\wedge k(c)=1_M\qquad
 (F\text{ any finite cover}), \tag{A.1}
\]
and factors through \(\mathcal D\) iff (A.1) holds for **all** covers. These tests are the main method for the examples.

**Foundational checks requested:** Confirm the diagonal-cover presentation, the pre-nucleus identities including \(\Phi_2(0)=d_{\mathcal U}\), and the equivalence between a pair factoring through a sublocale and the displayed cover equations. If taking some as previously known lemmas, say which ones.

## A2. Exact pure-rectangle certificate for failure of Q′

**Claim A2 (CORE).** \(\mathcal W\subsetneq\mathcal W_2\) iff there exist an infinite cover \(\mathcal C\) of \(1\), with no finite subcover, and nonzero \(a,b\in L\) with
\[
 a\wedge b=0,\qquad
 r=a\boxtimes b\not\le d_0,\qquad
 r\wedge w_{\mathcal C}\le d_0. \tag{A.2}
\]

*Proposed proof.* Since \(d_0\) is \(\Phi_2\)-fixed, the strict inequality \(d_{\mathcal W}>d_0\) forces \(\Phi(d_0)>d_0\): otherwise \(d_0\) would be full-\(\Phi\)-fixed and the least full fixed point above \(0\) could not exceed it. Some cover \(\mathcal C\) therefore has \((w_{\mathcal C}\to d_0)\not\le d_0\). Because rectangles join-generate \(Q\), there is \(r=a\boxtimes b\le(w_{\mathcal C}\to d_0)\) with \(r\not\le d_0\). The adjunction for \(\to\) gives the last inequality of (A.2).

Further \(r\le\Phi(d_0)\le d_{\mathcal W}\le d_{\mathcal I}\); the diagonal inverse image satisfies \(\delta^*(d_{\mathcal I})=0\), hence \(a\wedge b=\delta^*(r)=0\). A finite subcover \(F\subseteq\mathcal C\) would yield \(r\wedge w_F\le d_0\), so \(r\le(w_F\to d_0)\le\Phi_2(d_0)=d_0\), contradiction. Conversely (A.2) gives \(\Phi(d_0)>d_0\), hence \(d_{\mathcal W}>d_0\).

If (A.2) holds, \(\mathcal D\wedge O(r)=0\) but \(\mathcal D_2\wedge O(r)\) is a **nonzero dense** sublocale of \(\mathcal W_2\wedge O(r)\). The point sets of \(\mathcal D,\mathcal D_2\) agree: at a 2-valued point, finite binary cover compatibility forces compatibility with an arbitrary cover by partitioning its members according to which of the two coordinate evaluations accepts them. Thus the nonzero remnant of \(\mathcal D_2\) on \(r\) is **pointless**.

## A3. Further necessary tests: chromatic, rather-below and compact complement

**Claim A3.1 (chromatic obstruction).** Fix a proposed witness \((\mathcal C,r=a\boxtimes b)\) satisfying (A.2). Make a graph on the members of \(\mathcal C\), connecting distinct \(c,d\) if either of
\[
(a\wedge c)\boxtimes(b\wedge d),\qquad
(a\wedge d)\boxtimes(b\wedge c)
\]
is not below \(d_0\). Then this graph has **infinite chromatic number**. For if there were a finite coloring, each color-class union \(u_j\) would satisfy \((a\wedge u_j)\boxtimes(b\wedge u_j)\le d_0\), and the \(u_j\)'s would give a finite-cover contradiction to \(\Phi_2(d_0)=d_0\). Similarly, any infinite cover that is a finite union of upward-directed subfamilies has the same square neighborhood as a finite cover, and cannot yield (A.2).

**Claim A3.2 (cover-dependent rather-below localization).** Define
\[
 t_{\mathcal C}=
 \bigvee_{F\subseteq\mathcal C,\;F\text{ finite}}
 \bigvee\{v:v\prec\bigvee F\}.
\]
Whenever \(r\wedge w_{\mathcal C}\le d_0\), we have
\[
 r\wedge(t_{\mathcal C}\boxtimes1)\le d_0,
 \qquad
 r\wedge(1\boxtimes t_{\mathcal C})\le d_0.\tag{A.3}
\]
*Proposed proof:* if \(v\prec\bigvee F\), then \(\{v^*\}\cup F\) is a finite cover. On \(v\boxtimes1\) its square neighborhood agrees with the squares from \(F\), so \(r\wedge(v\boxtimes1)\le(w_{\{v^*\}\cup F}\to d_0)\le d_0\). Join and repeat symmetrically. Thus a witness requires \(t_{\mathcal C}<1\).

**Claim A3.3 (compact closed complement).** If \(a\wedge b=0\) and the closed sublocale \(C(a\vee b)\) is compact, then
\[
\mathcal D\wedge O(a\boxtimes b)
 =\mathcal D_2\wedge O(a\boxtimes b),
\quad
\mathcal W\wedge O(a\boxtimes b)
 =\mathcal W_2\wedge O(a\boxtimes b).
\tag{A.4}
\]
*Proposed proof:* For any cover \(\mathcal C\), compactness of \(C(a\vee b)\) supplies a finite \(F\subseteq\mathcal C\) with \(a\vee b\vee\bigvee F=1\). The finite cover \(\{a,b\}\cup F\) has square neighborhood which, when met with \(r=a\boxtimes b\), becomes exactly \(r\wedge w_F\) (the two diagonal squares vanish by \(a\wedge b=0\)). Hence \(\mathcal D_2\wedge O(r)\le O(w_{\mathcal C})\) for every \(\mathcal C\). Closure commutes with restriction to an open sublocale. A witness (A.2) therefore requires \(C(a\vee b)\) **noncompact**.

---

# Part B. Positive structure and interface no-go results — CORE

## B1. Finite-cover locality and proper-over-regular theorem

**Claim B1 (CORE).** Let \(f:X\to Y\) be a locale map such that \(\mathcal O(Y)\) is regular and its inverse-image right adjoint \(f_*:\mathcal O(X)\to\mathcal O(Y)\) preserves directed joins. Then
\[
\boxed{\mathcal D_2(X)=\mathcal D(X).} \tag{B.1}
\]
In particular this holds for a proper locale map over a regular codomain, and for the projection \(Y\times K\to Y\) when \(K\) is compact.

*Proposed proof:* First let \(\mathcal C\) cover \(X\). If elements \(e_i\) cover \(1\) and for each \(i\) there is a finite \(F_i\subseteq\mathcal C\) with \(e_i^*\vee\bigvee F_i=1\), then any finite-cover-compatible pair \(h,k\) respects \(\mathcal C\). Indeed \(\{e_i^*\}\cup F_i\) is a finite cover, and meeting its compatibility equation with \(h(e_i)\) yields \(h(e_i)\le\bigvee_{c\in\mathcal C}h(c)\wedge k(c)\). Join over \(i\).

For the map \(f\), put \(u_F=f_*(\bigvee F)\) for finite \(F\subseteq\mathcal C\). By directed-join preservation, \(\bigvee_F u_F=f_*(1)=1\). Regularity of \(Y\) says that elements \(v\prec u_F\), over all \(F\), cover \(Y\). Their inverse images \(e_{F,v}=f^*(v)\) cover \(X\). Since frame maps preserve rather-below and \(f^*f_*(\bigvee F)\le\bigvee F\) (adjunction counit), we have \(e_{F,v}^*\vee\bigvee F=1\). Apply the first argument. For compact \(K\), the localic projection \(Y\times K\to Y\) is proper.

**High-priority audit question:** Is there a hidden properness/direct-join or adjunction hypothesis? This claim deliberately strengthens a prior zero-dimensional-base compact-fiber result.

## B2. Completely join-prime boundary no-go theorem

Call \(n\in L\) **completely join-prime** when \(n\le\bigvee_i c_i\) implies \(n\le c_i\) for some \(i\). Such \(n\) satisfies \(O(n\boxtimes n)\subseteq\mathcal D\), since every cover contains a member above \(n\).

**Claim B2 (CORE).** If \(a\wedge b=0\) and there is a family of completely join-prime elements \(n_i\) with \(a\vee b\vee\bigvee_i n_i=1\), then
\[
\boxed{\mathcal W\wedge O(a\boxtimes b)
       =\mathcal W_2\wedge O(a\boxtimes b).}\tag{B.2}
\]
*Proposed proof:* Take a rectangle \(s=u\boxtimes v\le a\boxtimes b\) with \(\mathcal D_2\wedge O(s)\ne0\). If there is no \(i\) with both \(u\wedge n_i\ne0\) and \(v\wedge n_i\ne0\), partition the \(i\)'s according to which meet vanishes, write their respective joins \(n_1,n_2\). Then \(\{a,b,n_1,n_2\}\) is a finite cover whose square neighborhood is disjoint from \(s\), contradicting \(\mathcal D_2\wedge O(s)\ne0\). Hence such \(i\) exists, and the nonzero rectangle \((u\wedge n_i)\boxtimes(v\wedge n_i)\le s\) lies below the open sublocale \(\mathcal D\), since it is below \(n_i\boxtimes n_i\). Thus \(\mathcal D\) is dense in \(\mathcal D_2\) inside \(O(a\boxtimes b)\). Taking closures proves (B.2).

## B3. Earlier compact-remainder, hyperconnected and Booleanization criteria

The October working notes established further sufficient conditions. Please examine their proofs in the linked source notes if needed, or report that you did not check them:

- Let \(h_{hc}\) be the join of nonzero hyperconnected opens of \(L\), and \(h_{cc}\) the join of \(k^*\) over compact closed sublocales \(C(k)\). With \(e=h_{hc}\vee h_{cc}\), the working statement is that \(\mathcal W\) and \(\mathcal W_2\) agree on the open strips \(O(e\boxtimes1\vee1\boxtimes e)\), and if \(C(e)\) is compact then \(\mathcal W=\mathcal W_2\).
- If \(C(h_{cc})\) is compact, the stronger \(\mathcal D=\mathcal D_2\) is proposed.
- Let \(G=\mathcal U\wedge O(d_{\mathcal U}^{**})\) be the nonregular Urysohn sector and \(H_2=\mathcal W_2\wedge G\). The working Isbell Boolean criterion is
  \[
  \mathcal W=\mathcal W_2 \quad\Longleftrightarrow\quad
  B(H_2)\subseteq\mathcal D,
  \qquad B(H_2)\subseteq\mathcal D_2\ \text{always},
  \]
  where \(B(-)\) denotes the least dense Boolean sublocale. If this Booleanization is spatial/atomic, equality follows because \(\operatorname{pt}\mathcal D_2=\operatorname{pt}\mathcal D\).
- If \(\mathcal U\) is regular closed, then \(\mathcal W=\mathcal W_2=\mathcal U\). In particular this was proved for arbitrary Alexandrov locales.

**Scope note:** These are prior **working** deductions. Please do not call them independently verified merely because the foundational October W/U packet previously received a separate audit. The bibliography and source-note index below contain their detailed original proofs.

---

# Part C. Counterexample controls and failed Q′ attempts

The examples are deliberately included because several satisfy \(\mathcal D\subsetneq\mathcal D_2\), sometimes in the atomless nonregular boundary, **without** giving \(\mathcal W\subsetneq\mathcal W_2\). One major audit goal is to verify that both inequalities and claimed density are actually established.

## C1. Scott/Cantor baseline — CORE

Let \(S=\mathcal P(\mathbb N)\setminus\{\varnothing\}\) with the Scott topology, and \(c_n=\{E\in S:n\in E\}\). These compact opens cover \(S\) with no finite subcover. Let \(K=2^{\mathbb N}\), \(M=\operatorname{RO}(K)\), and let \(A_n=\{z:z_n=0\}\), \(B_n=\{z:z_n=1\}\) be complementary cylinders. Define
\[
 h(c_F)=\bigwedge_{n\in F}A_n,
 \qquad k(c_F)=\bigwedge_{n\in F}B_n,
 \quad c_F=\bigcap_{n\in F}c_n,
\]
extending by frame joins (the original note gives the sectionwise formula).

Every finite cover of \(S\) has a member containing infinitely many \(c_n\), since every singleton point \(\{n\}\) must be covered. The images of that member under both maps are \(1_M\): for infinite \(J\subseteq\mathbb N\), \(\bigvee_{n\in J}A_n=\bigvee_{n\in J}B_n=1_M\). But
\[
 \bigvee_n h(c_n)\wedge k(c_n)=0.
\]
Thus \(\mathcal D(S)\subsetneq\mathcal D_2(S)\). On the other hand \(S\) has a greatest point and is hyperconnected; no two nonzero opens are far, \(\mathcal I=\mathcal U=S^2\), and hence \(\mathcal W=\mathcal W_2=S^2\). This example proves the necessity of paying attention to **closure**, not only to finite-cover factorization.

## C2. Compact two-apex nonregular boundary control

Let \(Y=\mathbb R\sqcup\{p,q\}\), with ordinary real opens and with neighborhoods at \(p\) containing a cofinite positive tail, and neighborhoods at \(q\) containing a cofinite negative tail. The correctly checked topological fact is that **Y is compact** (not noncompact). Put
\[
 A_+=[0,\infty)\cup\{p\},\quad
 A_-=(-\infty,0]\cup\{q\},\quad
 K_Y=A_+^2\cup A_-^2.
\]
The asserted ordinary point relation is
\[
 \operatorname{pt}(\mathcal U(Y))
   =K_Y\cup\{(p,q),(q,p)\}.
\]
The open core \(K_Y=\operatorname{cl}(\operatorname{int}\mathcal U)\) is regular closed. The cross pairs are relatively isolated in \(\mathcal U\) and killed by a binary diagonal cover \(\{Y\setminus\{p\},Y\setminus\{q\}\}\), so in this compact spatial-square model
\[
 \mathcal I<\mathcal W=\mathcal W_2=K_Y<\mathcal U.
\]
A product with a branching factor can make the Urysohn residual atomless, but the same binary cover then eliminates the **entire** residual from \(\mathcal W_2\): the product of independent defects does not work. Please verify the point/localic-square inference, and do not inherit the historical mistaken claim of noncompactness.

## C3. Join-prime infinite boundary gluing

Take two copies \(A,B\) of the Scott space \(S\) in C1, and boundary \(T=\{t_n:n\ge1\}\). A basis comprises the sheet opens and
\[
 N_n=\{t_n\}\cup c_n^A\cup c_n^B.
\]
The closed complement \(T\) is infinite discrete. Restriction to the two sheets and the Scott/Cantor maps of C1 gives \(h(N_n)=A_n\), \(k(N_n)=B_n\), finite-cover compatibility and an infinite-cover defect on \(A\boxtimes B\). Yet \(N_n\) is **completely join-prime**: it is the least neighborhood of \(t_n\). Thus B2 applies and forces local \(\mathcal W=\mathcal W_2\). More explicitly, the two greatest Scott points in the sheets yield four full-cover-compatible point pairs, dense in the localic square.

## C4. Nonprincipal-filter gluing with a dense pointless full-cover core

Let \(R=\mathbb Q\) with its usual topology, enumerated \((q_j)\), and \(E_m=R\setminus\{q_1,\ldots,q_m\}\), decreasing dense opens with empty intersection. Let \(P=\operatorname{Fin}_+(\mathbb N)\) with upper Alexandrov topology; its basic opens are \(c_F=\{G\supseteq F\}\) and it is hyperconnected. Take sheets \(A,B\cong R\times P\), boundary \(t_n\), and basis
\[
 N_{n,m}=\{t_n\}\cup(E_m\times c_n)^A\cup(E_m\times c_n)^B.
\]
No boundary point has a least neighborhood; its traces on both sheets have empty intersection. The Cantor maps on \(\operatorname{RO}(R\times2^{\mathbb N})\) again produce \(\mathcal D_2\ne\mathcal D\), with the cover \(\{A,B\}\cup\{N_{n,1}\}\). For this cover \(t_{\mathcal C}=0\).

Nevertheless the maps
\[
 \theta_\sigma(U)=\operatorname{int}\overline{\pi_R(U\cap\sigma)}
 \quad(\sigma=A,B)
\]
are frame homomorphisms to \(\operatorname{RO}(R)\). The projection preserves finite meets because every two nonempty opens of \(P\) intersect. Each boundary neighborhood has dense parameter projection, so \(\theta_A,\theta_B\) send it to \(1\). Any pair of rational-translation variants of these maps respects **every** open cover: some cover member contains a given boundary point and hence an entire basic neighborhood. By translating two nonempty parameter projections until they overlap, one makes the image of any two nonzero opens meet in \(\operatorname{RO}(R)\). Thus \(\mathcal D\) is dense in the entire localic square and \(\mathcal W=\mathcal W_2=\mathcal U=X^2\), **despite there being no ordinary full-cover-compatible cross-sheet pairs**. The density is pointless.

## C5. Coupled rational boundary: D₂>D **inside** the nonregular H₂ sector — CORE

This is an important stress test because it no longer locates the infinite-cover defect away from the relevant Urysohn boundary.

Let \(R=\mathbb Q\) and \(P=\operatorname{Fin}_+(\mathbb N)\) as in C4. Take sheets \(A,B\cong R\times P\), but now attach boundary points \(t_{q,n}\) for each \(q\in R,n\ge1\), with neighborhoods
\[
 N_{q,n,I}=\{t_{q,n}\}\cup(I\times c_n)^A\cup(I\times c_n)^B,
 \quad q\in I\subseteq R\text{ open interval}.
 \tag{C.5}
\]
There is a well-defined countable topology; the closed complement \(T\) is countably infinite discrete. Let \(K=2^{\mathbb N}\), \(M=\operatorname{RO}(R\times K)\), and write \(A_F=\bigcap_{n\in F}[n=0]\), \(B_F=\bigcap_{n\in F}[n=1]\). For any open \(U\subseteq R\times P\) let \(U_F=\{q:(q,F)\in U\}\) and define
\[
 H_+(U)=j\Bigl(\bigcup_{F\in P}U_F\times A_F\Bigr),
 \quad
 H_-(U)=j\Bigl(\bigcup_{F\in P}U_F\times B_F\Bigr),
\]
where \(j(V)=\operatorname{int}\overline V\). Taking \(h(U)=H_+(U\cap A)\), \(k(U)=H_-(U\cap B)\) gives
\[
 h(N_{q,n,I})=j(I\times A_n),\quad k(N_{q,n,I})=j(I\times B_n),
 \quad h(A)=k(B)=1.
\]
The proposed proof that \(h,k\) respect **every finite cover**: fix a nonempty rational-parameter interval \(O\) and a Cantor cylinder \([s]\). At any \(q\in O\), the finitely many cover members containing the different \(t_{q,n}\) have a member appearing for infinitely many \(n\). Choose distinct \(n,n'\) outside the finite support of \([s]\). The corresponding intervals around \(q\) overlap, and \([s]\cap A_n\cap B_{n'}\ne0\). This shows the join of their image intersections is dense in \(R\times K\). The infinite cover \(\{A,B\}\cup\{N_{q,n,R}:q\in R,n\ge1\}\) fails compatibility term by term. Thus \(\mathcal D_2\ne\mathcal D\) on \(\rho=A\boxtimes B\).

For any sheet-open \(u\), with rational projection \(\pi(u)\), the boundary-closure test is
\[
 t_{q,n}\in\overline u \iff q\in\overline{\pi(u)}.
\]
Every nonzero mixed rectangle has a nonzero subrectangle with disjoint-closure parameter intervals, hence far: \(d_{\mathcal U}\wedge\rho\) is dense in \(\rho\), or \(\rho\le d_{\mathcal U}^{**}\). Thus the witness to \(\mathcal D_2\ne\mathcal D\) lives in the nonregular residual \(H_2=\mathcal W_2\wedge\mathcal U\wedge O(d_{\mathcal U}^{**})\), and the residual restricted to \(\rho\) is atomless (two disjoint rational localizations inside every nonzero relatively open).

Yet whenever two nonempty sheet opens have a shared parameter \(q\), choose finite conditions \(F,G\) in their sections and a larger condition \(H=F\cup G\cup\{n\}\). The pair \(((q,H)^A,(q,H)^B)\) is a **point of the full** \(\mathcal D\): every cover has a member containing \(t_{q,n}\) and hence both points. If sheet projections are disjoint, coordinatewise expansion into parameter intervals with disjoint closures shows the entire rectangle lies under \(d_{\mathcal U}\). Hence the full fitted diagonal is dense in the mixed Urysohn relation:
\[
 \mathcal W\wedge O(\rho)=\mathcal W_2\wedge O(\rho)=\mathcal U\wedge O(\rho).
 \tag{C.6}
\]
This proves **local**, not global, equality. The proposed ordinary cross-sheet point descriptions are: \(\operatorname{pt}\mathcal U\) consists of equal-parameter pairs, whereas \(\operatorname{pt}\mathcal D\) additionally requires the two finite conditions to share a label. Verify both point claims and the nonpointwise coproduct argument for (C.6).

## C6. Missing-center finite-condition forcing: finite-flip rescue — CORE

To eliminate the preceding common-upper-bound points, let \(R=\mathbb R\setminus\mathbb Q\) and enumerate rational centers \(q_n\). Replace \(P\) with \(\operatorname{Fn}(\mathbb N,2)\setminus\{\varnothing\}\), finite nonempty partial binary conditions ordered by extension (upper Alexandrov topology). Conditions with opposite assignments at the same coordinate are incompatible. Take sheets \(A,B\cong R\times P\) and boundary points \(t_n\) with
\[
 N_{n,I}=\{t_n\}\cup((I\cap R)\times\uparrow\ell_n)^A
                 \cup((I\cap R)\times\uparrow\ell_n)^B,
 \quad\ell_n=\{n\mapsto0\},\quad q_n\in I.
\]
The center \(q_n\) is missing from both sheets; no original cross-sheet pair is a point of \(\mathcal D\). Let \(M=\operatorname{RO}(R\times2^{\mathbb N})\) and for a sheet-open \(U\) define
\[
 H_+(U)=j\Bigl(\bigcup_{s\in P}U_s\times[s]\Bigr),\quad
 H_-(U)=j\Bigl(\bigcup_{s\in P}U_s\times[\overline s]\Bigr),
\]
where \([s]\) is a Cantor cylinder and \(\overline s\) flips all bits in the finite domain. Restrict these to A and B to get \(h,k\). Then \(h(N_{n,I})=j((I\cap R)\times[n=0])\), \(k(N_{n,I})=j((I\cap R)\times[n=1])\). The infinite cover \(\{A,B\}\cup\{N_{n,R}\}\) fails compatibility.

**Proposed finite-cover proof:** Given finitely many cover members, color each rational center \(q_n\) according to a member containing \(t_n\). The finitely many color-class closures cover the real line; by the Baire property of \(\mathbb R\), one class is dense in a nonempty interval. For every target open \(O\times[s]\) in \(R\times2^{\mathbb N}\), use two distinct same-color centers with overlapping boundary intervals, whose indices avoid \(\operatorname{dom}(s)\). The corresponding contradictory bit orientations concern *different* coordinates, so the two target cylinder images intersect. This establishes finite-cover compatibility, hence \(\mathcal D_2\ne\mathcal D\).

For each finite \(E\subseteq\mathbb N\), let \(\gamma_E\) flip only the coordinates of \(E\) on the Boolean target. Consider the two **same-orientation** sheet maps
\[
 \theta_A=H_+(-\cap A),\quad
 \theta_B^E=\gamma_E\circ H_+(-\cap B).
\]
These are **fully** cover compatible, because every cover member containing \(t_n\) with \(n\notin E\) sends at least the same open cylinder \(j((I_n\cap R)\times[n=0])\) under both maps; their join as \(n\notin E\) is \(1_M\). Every pair of finite conditions \(s,t\) can be made cylinder-compatible by flipping the finitely many coordinates on which they conflict. Thus \(\mathcal D\) meets every mixed rectangle having overlapping parameter projections; disjoint parameter projections produce rectangles beneath \(d_{\mathcal U}\) by a two-stage join decomposition. One obtains the **local** equality (C.6) again, now with **no ordinary cross-sheet \(\mathcal D\)-points**. This is a genuinely Boolean-valued rescue, not the earlier common-upper-bound argument.

## C7. Focused rigidity tests: two opposite failures

**C7(a): Repeated-coordinate labels.** In C6 replace the label \(n\) at rational center \(q_n\) by \(f(n)=\operatorname{den}(q_n)\), its denominator in lowest terms. Every Boolean coordinate now occurs infinitely often. But centers with denominator in a *finite* set form a locally finite, nowhere-dense set. Thus the finite-cover color-class proof survives, **and** after any finite-coordinate flip enough untouched boundary centers remain dense to give fully cover-compatible maps. The local equality of W/W₂ on the mixed Urysohn rectangle remains.

**C7(b): Perfect-tree forcing.** Replace C6's finite partial functions by a poset of perfect binary trees and the target by its complete regular-open forcing Boolean algebra \(B\). The bit conditions \(b_n^0,b_n^1\) are complementary. A perfect tree may force infinitely many bits to zero: for \(S=\{n:q_n\in J\}\), with \(J\) a bounded real interval and both \(S\), \(\mathbb N\setminus S\) infinite, there is a nonzero perfect-tree value \(b_{T_S}\) with \(b_{T_S}\le b_n^0\) for all \(n\in S\). Choose a smaller \(J_0\) with \(\overline{J_0}\subset J\). For every \(n\notin S\) choose \(I_n\ni q_n\) disjoint from \(J_0\); choose arbitrary such intervals for \(n\in S\). Let \(N=\bigvee_n N_{n,I_n}\). The two-element cover \(\{A\vee N,B_{\mathrm{sheet}}\}\) forces \(k(N)=1\) for the **mirrored** pair, but the nonzero rectangle \((J_0\cap R)\boxtimes b_{T_S}\) has zero meet with \(k(N)\). Hence the *proposed natural pair* is **not even finite-cover compatible**. This is **not** a theorem excluding all perfect-tree or nonhomogeneous forcing approaches.

**C7(c): Nested finite strings.** If all boundary labels prescribe a first bit, and the mirrored images of a label \(s_i\) lie respectively below \([s_i]\), \([\overline{s_i}]\), partition the labels by the first bit. For the resulting two-element cover \(\{A\vee N_0,B\vee N_1\}\), finite-cover compatibility would imply \(k(N_0)\vee h(N_1)=1\). Both terms lie below the proper clopen cylinder \([1]\), a contradiction. Again this defeats only this natural family of maps.

**Research-status conclusion:** No counterexample to Q′ has been produced. The examples show different reasons that an infinitary defect might disappear upon closure: hyperconnectedness, an atomic binary-excluded boundary, completely join-prime interface squares, full-cover-compatible pointless projections, ordinary common extensions, and tail-preserving finite-coordinate automorphisms. These mechanisms are not known to combine into a general proof of Q′.

---

# Part D. Dependency map, priority questions, and complete source-note index

## D1. Suggested order of adversarial checking

The **minimal proof chain** is: A1 (correct frame/sublocale interpretations) → A2 (exact obstruction) → A3/B1/B2 (positive no-go theorems) → C1 (first strict D₂>D control) → C5 and C6 (the claimed stronger coupled examples) → C7 (bounded rigidity failures). The alternative October sufficient conditions B3 may be checked before or after the concrete models.

Particularly important potential error types:

1. Does \(\Phi_2(d_0)=d_0\) follow with **all** finite-cover neighborhoods, not merely individual binary square neighborhoods?
2. Is the right adjoint direction in B1 correct, and does properness of localic product projection hold as used?
3. Does B2 really show **sublocale** density, or only pointwise density?
4. Are the H+/H− assignments in C5/C6 genuinely **frame maps**? Do their finite-color arguments handle *every* finite open cover?
5. Does each claimed point-set description of \(\mathcal U\) imply the stated **localic** relation, or is a rectangle decomposition missing?
6. Is the infinitary defect in C5/C6 genuinely inside \(H_2\), and is the boundary actually atomless?
7. Is the perfect-tree condition \(b_{T_S}>0\), and is the binary-cover contradiction correctly computed?
8. Have any additional assumptions (sobriety, product spatiality, compactness, coherent versus noncoherent) slipped into a proof without being stated?

## D2. Optional research input

We welcome *at most two* concrete suggestions with a discriminating first step, including a serious route to proof of Q′ or the weaker Q, a non-forcing counterexample, or a meaningful simplification. Do not manufacture suggestions. A conclusion that it is time to stop searching and instead study W as a relation is an acceptable outcome.

## D3. Original sources and exact links

All of the following are Markdown research notes in the **mkkinyon/locales** GitHub repository. Prior referee assessments and reconciliations are intentionally omitted from the link list. The packet above is the minimum self-contained basis; links below allow checking expanded proofs, chronology, and qualifications. Neither earlier referee reports nor the internal audit are included.

**Foundations and October consolidated Q′ work:**

- [Q′ unified synthesis, 24 Oct](https://github.com/mkkinyon/locales/blob/main/A-WU-Qprime-unified-synthesis-2026-10-24.md)
- [Full diagonal-neighborhood nucleus criterion](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-nucleus-criterion-2026-10-24.md)
- [Finite-cover-compatible morphisms](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-finite-cover-morphisms-2026-10-24.md)
- [Infinite-cover Boolean/Cantor example](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-infinite-cover-Boolean-witness-2026-10-24.md)
- [Compact remainder / compact-closed strips](https://github.com/mkkinyon/locales/blob/main/A-WU-Qprime-compact-remainder-and-compact-closed-strips-2026-10-24.md)
- [Clopen finite patching / compact-fiber theorem](https://github.com/mkkinyon/locales/blob/main/A-WU-Qprime-clopen-finite-patching-2026-10-24.md)
- [Alexandrov / branching / atomless boundary controls](https://github.com/mkkinyon/locales/blob/main/A-WU-Qprime-Alexandrov-branching-atomless-boundary-2026-10-24.md)

**November targeted Q′ construction records:**

- [Proper-over-regular theorem and cover-localization obstruction, 8 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-proper-regular-base-and-localized-witness-2026-11-08.md)
- [Infinite join-prime boundary gluing and no-go, 8 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-noncompact-interface-gluing-test-2026-11-08.md)
- [Nonprincipal-filter gluing with dense pointless full-fitting core, 8 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-nonprincipal-filter-gluing-test-2026-11-08.md)
- [Rational coupled nonregular boundary, 8 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-coupled-rational-boundary-test-2026-11-08.md)
- [Missing-center forcing and finite-coordinate flips, 9 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-missing-center-forcing-finite-flips-2026-11-09.md)
- [Focused nonhomogeneous forcing tests, 9 Nov](https://github.com/mkkinyon/locales/blob/main/A-W2-nonhomogeneous-forcing-focused-tests-2026-11-09.md)

**Foundational literature pointer only:** Arrieta–Picado–Pultr, *On the fitting of the diagonal* (2022), see the University of Coimbra preprint linked in the source notes. No novelty or priority is claimed for the diagonal pre-nucleus or standard Isbell Booleanization facts.

**Please produce your independent report before consulting any earlier referee assessments or internal audit.**