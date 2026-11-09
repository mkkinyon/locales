# Project A — Nonprincipal-filter gluing: a dense pointless full-cover core

**8 November 2026. Internal working stress test, not externally audited; no novelty or priority claim.**

**Question Q′:** Is \(\mathcal W_2=\mathcal W\) for all frames? We continue the rectangular obstruction search. This test deliberately removes completely join-prime boundary neighborhoods, replaces them by nonprincipal filters with *empty intersection of their traces on both sheets*, and retains a disjointly supported Cantor Boolean witness to \(\mathcal D_2\ne\mathcal D\). Nevertheless \(\mathcal D\) remains dense, this time due to *pointless* complete Boolean targets rather than ordinary compatible pairs.

The conclusion is a negative result about this construction strategy, not a counterexample to Q′.

## 1. Construction

Let \(R=\mathbb Q\) with its usual topology, enumerated \(R=\{q_1,q_2,\dots\}\), and let
\[
E_m=R\setminus\{q_1,\ldots,q_m\}.
\]
Each \(E_m\) is open dense in \(R\), \(E_{m+1}\subsetneq E_m\), and \(\bigcap_m E_m=\varnothing\).

Let \(P=\operatorname{Fin}_+(\mathbb N)\), ordered by inclusion, with the upper Alexandrov topology. Its basic opens are \(c_F=\{G\in P:F\subseteq G\}\), \(F\in P\). Write \(c_n=c_{\{n\}}\). Every two nonempty opens of \(P\) meet (if \(F\in U,G\in V\), then \(F\cup G\in U\cap V\)); the frame \(\mathcal O(P)\) is hyperconnected.

Take two disjoint copies \(A,B\) of \(R\times P\), and a countably infinite boundary \(T=\{t_n:n\ge1\}\). Put \(X=A\sqcup B\sqcup T\). Keep the ordinary product opens in the sheets, and give \(t_n\) the decreasing neighborhood base
\[
N_{n,m}=\{t_n\}\cup(E_m\times c_n)^A\cup(E_m\times c_n)^B,
\qquad m\ge1.
\]
Together with sheet product basics these form a basis for \(X\): the intersections of two \(N\)-sets at different boundary points consist of sheet opens, those for the same point reduce to \(N_{n,\max(m,k)}\), and intersections with sheet opens are open in that sheet.

The space is countable and second-countable. Its closed remainder \(T=X\setminus(A\cup B)\) is an infinite discrete subspace, hence the closed sublocale \(C(A\vee B)\) is noncompact. No \(N_{n,m}\) is completely join-prime: all contain \(t_n\), but their strictly descending chain has no least neighborhood.

For either sheet \(\sigma\in\{A,B\}\),
\[
\bigcap_{m\ge1}(N_{n,m}\cap\sigma)=\varnothing
\]
because \(\bigcap_m E_m=\varnothing\). Thus no original sheet point remains in all neighborhoods of any fixed \(t_n\).

## 2. A disjointly supported finite-cover defect

Let \(K=2^{\mathbb N}\) be Cantor space. For \(n\ge1\) let \(A_n=\{z:z_n=0\}\), \(B_n=\{z:z_n=1\}\), and for finite nonempty \(F\subseteq\mathbb N\) set \(A_F=\bigcap_{n\in F}A_n\), \(B_F=\bigcap_{n\in F}B_n\). These are clopen. In \(\operatorname{RO}(K)\), for every infinite \(J\subseteq\mathbb N\),
\[
\bigvee_{n\in J}A_n=\bigvee_{n\in J}B_n=1,
\qquad A_n\wedge B_n=0.
\]

Let \(M=\operatorname{RO}(R\times K)\). There are frame maps \(H_0,K_0:\mathcal O(R\times P)\to M\) with
\[
H_0(O\times c_F)=j(O\times A_F),\qquad
K_0(O\times c_F)=j(O\times B_F),
\]
where \(O\subseteq R\) is open and \(j(U)=\operatorname{int}\overline U\) denotes regularization into \(M\).

For completeness, an explicit definition for arbitrary open \(U\subseteq R\times P\) is
\[
H_0(U)=\bigvee_{F\in P}j(U_F\times A_F),
\quad U_F=\{q\in R:(q,F)\in U\},
\]
and similarly for \(K_0\) using \(B_F\). The sections \(U_F\) are open; joins are preserved sectionwise, and finite meets are preserved because \(F\cup G\) refines both \(F,G\), while \(A_F\cap A_G=A_{F\cup G}\) (and similarly for \(B\)). Each map sends \(1\) to \(1\).

Define \(h,k:\mathcal O(X)\to M\) by restricting to the two sheets and applying these maps:
\[
h(U)=H_0(U\cap A),\qquad k(U)=K_0(U\cap B).
\]
Then
\[
h(A)=1,\quad k(B)=1,\quad h(B)=k(A)=0,\qquad
h(N_{n,m})=R\times A_n,\quad k(N_{n,m})=R\times B_n.
\]

**Finite-cover compatibility.** If \(\{U_1,\ldots,U_\ell\}\) covers \(X\), then for every \(n\), some member contains \(t_n\) and hence some \(N_{n,m_n}\). One member \(U_j\) receives infinitely many distinct \(n\)'s. Therefore \(h(U_j)=k(U_j)=1\), using the infinite-join identities for cylinders. So \((h,k)\) factors through \(\mathcal D_2\).

**Failure of full compatibility.** The family
\[
\mathcal C=\{A,B\}\cup\{N_{n,1}:n\ge1\}
\]
covers \(X\), but every term \(h(c)\wedge k(c)\) vanishes. So \((h,k)\) does not factor through \(\mathcal D\). Since \(h(A)\wedge k(B)=1\), this is witnessed on the disjoint rectangle \(A\boxtimes B\):
\[
\mathcal D\ne\mathcal D_2,\qquad A\wedge B=0.
\]

Moreover \(t_{\mathcal C}=0\) for the cover-dependent rather-below locus of the preceding working note. Indeed, the trace of every \(N_{n,m}\) is dense in either sheet: \(E_m\) is dense in \(R\) and \(c_n\) meets every nonempty open of the hyperconnected \(P\). Hence **every nonempty open of \(X\) has every \(t_n\) in its closure**. Yet any finite union of elements of \(\mathcal C\) contains only finitely many \(t_n\); therefore no nonzero \(v\) is rather below that finite union.

This passes the previous three diagnostic tests: a noncompact closed interface, no completely join-prime \(N_{n,m}\), and maximal failure \(t_{\mathcal C}=0\).

## 3. There are no ordinary full-cover-compatible cross-sheet pairs

For any original points \(x=(q_j,F)\in A\), \(y\in B\), consider the open cover
\[
\{A,B\}\cup\{N_{n,j}:n\ge1\}.
\]
Every \(N_{n,j}\) avoids \(x\) because \(q_j\notin E_j\); the member \(A\) misses \(y\), and \(B\) misses \(x\). Thus no member of the cover contains both \(x,y\). The pair \((x,y)\) cannot be a point of \(\mathcal D\).

The same conclusion holds for all points over the two sheet open sublocales in their soberifications: the \(R\)-coordinate of any such point is an actual rational \(q_j\) because \(R\) is sober; the displayed cover excludes that rational coordinate from every boundary neighborhood.

## 4. Nevertheless D is dense: a genuinely pointless mechanism

Let \(j_R:\mathcal O(R)\to\operatorname{RO}(R)\) be regularization. For \(\sigma=A\) or \(B\), define a frame map
\[
\theta_\sigma(U)=j_R\bigl(\pi_R(U\cap\sigma)\bigr).
\]
The projection of an open \(U\subseteq R\times P\) onto \(R\) preserves arbitrary joins; it also preserves finite meets **because \(P\) is hyperconnected**: nonempty open sections over a common rational have nonempty intersection. Therefore \(\theta_\sigma\) is a frame map. Every \(N_{n,m}\) has projected sheet trace \(E_m\), dense in \(R\), so
\[
\theta_A(N_{n,m})=\theta_B(N_{n,m})=1.
\]
Composing either map with any rational translation of \(R\) still sends every \(N_{n,m}\) to \(1\).

Given *any* open cover of \(X\), a member containing \(t_1\) contains some \(N_{1,m}\); hence any pair of these translated \(\theta\)-maps sends that member to \(1\) in both coordinates. Such a pair is therefore **full-cover compatible** and factors through \(\mathcal D\).

Now take any nonzero opens \(u,v\in\mathcal O(X)\). Each intersects at least one sheet in a nonzero open; choose \(\sigma,\tau\in\{A,B\}\) accordingly. The projected nonempty rational opens
\[
U=\pi_R(u\cap\sigma),\qquad V=\pi_R(v\cap\tau)
\]
can be made to intersect by rational translation: choose \(p\in U,q\in V\), and translate \(V\) by \(p-q\). The corresponding full-cover-compatible pair \(\theta_\sigma,\theta_{\tau,p-q}\) satisfies
\[
\theta_\sigma(u)\wedge\theta_{\tau,p-q}(v)\ne0
\]
in \(\operatorname{RO}(R)\). Therefore \(\mathcal D\wedge O(u\boxtimes v)\ne0\). Since nonzero rectangles form a base for the frame coproduct, \(\mathcal D\) is **dense in the entire localic square**.

Thus
\[
\boxed{\mathcal W=\mathcal W_2=X^2.}
\]
In fact, since every nonzero open of \(X\) accumulates at all the \(t_n\), no two nonzero opens are far; \(d_{\mathcal U}=0\) and
\[
\boxed{\mathcal W=\mathcal W_2=\mathcal U=X^2.}
\]

This is not a pointwise argument: there are **no ordinary full-cover-compatible cross-sheet point pairs**, as shown in §3. The density comes from nonspatial Boolean-valued generalized points in \(\operatorname{RO}(\mathbb Q)\), the least dense Boolean sublocale of the crowded rational space.

## 5. Disposition

Replacing join-prime boundary neighborhoods by truly **nonprincipal** neighborhood filters, even ones with empty sheet intersection, does not in itself move a finite-cover defect into the closed-hull boundary. The dense-open regularization of the non-Baire rational factor regenerates full-cover-compatible **pointless** generalized pairs throughout the square.

The recurring failure is a regular-closed Urysohn relation: in this model \(\mathcal U=X^2\), so the known inclusion \(\operatorname{cl}(\operatorname{int}\mathcal U)\le\mathcal W\) already enforces \(\mathcal W=\mathcal U\). A useful next design must build a nonregular Urysohn boundary *intrinsically* into the gluing, not append an independently pathological factor.

No claim about universal Q′ is made, and these calculations are internal working results only.
