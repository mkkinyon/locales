# Project A — A coupled nonregular Urysohn-boundary stress test for Q′

**8 November 2026 — Internally checked working example, not independently audited; no novelty or priority claim.** This note addresses Q′: is \(\mathcal W_2=\mathcal W\) for every locale? It **does not** settle Q′. It constructs an example in which \(\mathcal D_2\ne\mathcal D\) **inside the nonregular Urysohn boundary \(\mathcal H_2\)**, yet \(\mathcal W=\mathcal W_2=\mathcal U\) locally on the offending rectangle.

This is a more tightly coupled example than the earlier independent product of a Scott-cover defect and a two-apex boundary. Its failure is explained by densely available **fully cover-compatible ordinary pairs** carrying the same rational parameter.

## 1. Definitions and topological construction

Let \(P=\operatorname{Fin}_+(\mathbb N)\), the nonempty finite subsets of \(\mathbb N\) ordered by inclusion, with upper Alexandrov topology, and let \(c_F=\{G\in P:F\subseteq G\}\), \(c_n=c_{\{n\}}\). This space is hyperconnected: any two nonempty upper sets intersect, because they contain a common finite union.

Let \(R=\mathbb Q\) with its usual topology. Take two disjoint open copies \(A,B\) of \(R\times P\). Let \(T=\{t_{q,n}:q\in R,\ n\in\mathbb N\}\), and put \(X=A\sqcup B\sqcup T\). A basis for X consists of the ordinary product bases on A,B, and
\[
N_{q,n,I}=\{t_{q,n}\}\cup(I\times c_n)^A\cup(I\times c_n)^B,
\quad q\in I,\ I\subseteq R\text{ open rational interval}.
\]
The basis axioms hold: intersections of two N-neighborhoods at the same boundary point shrink I, at distinct boundary points they are unions of opens in A,B, and intersections with sheet basics are sheet-open. Thus X is countable and second-countable. The closed subspace T=X\(A∪B) is infinite discrete, so the closed sublocale \(C(A\vee B)\) is noncompact.

For a sheet open \(U\), let \(\pi(U)\subseteq R\) denote its parameter projection. Every nonempty open section \(U_q\subseteq P\) intersects every c_n because P is hyperconnected. Therefore
\[
t_{q,n}\in\overline U
\quad\Longleftrightarrow\quad q\in\overline{\pi(U)}^{\,R}.
\tag{1.1}
\]
This holds for every n. Closures of opens on opposite sheets can intersect only in T.

## 2. Finite-cover-compatible Cantor maps with an infinite-cover failure

Let \(K=2^{\mathbb N}\) and \(M=\operatorname{RO}(R\times K)\). Write
\[
A_n=\{z:z_n=0\},\quad B_n=\{z:z_n=1\},\quad
A_F=\bigcap_{n\in F}A_n,\quad B_F=\bigcap_{n\in F}B_n.
\]
Let \(j:\mathcal O(R\times K)\to M\) be regularization \(j(V)=\operatorname{int}\overline V\). For \(U\in\mathcal O(R\times P)\) and \(F\in P\), define the open section \(U_F=\{q\in R:(q,F)\in U\}\), and set
\[
H_+(U)=j\left(\bigcup_{F\in P} U_F\times A_F\right),\qquad
H_-(U)=j\left(\bigcup_{F\in P} U_F\times B_F\right).
\tag{2.1}
\]
These are frame homomorphisms. The raw unions preserve arbitrary joins. They preserve binary meets because for opens U,V upward in the P-coordinate, any pair \(F\in U_q,G\in V_q\) has \(F\cup G\in(U\cap V)_q\), and \(A_F\cap A_G=A_{F\cup G}\) (likewise B). Finally \(H_\pm(1)=1\), since \(\bigcup_{n\ge1}A_n\) and \(\bigcup_{n\ge1}B_n\) are dense open in K; the complete Boolean quotient j preserves arbitrary joins and finite meets.

Set \(h(U)=H_+(U\cap A)\), \(k(U)=H_-(U\cap B)\), for \(U\in\mathcal O(X)\). Then
\[
h(A)=k(B)=1_M,\quad h(B)=k(A)=0,\qquad
h(N_{q,n,I})=j(I\times A_n),\quad k(N_{q,n,I})=j(I\times B_n).
\tag{2.2}
\]

**Finite-cover compatibility.** Fix a finite cover \(\{U_1,\ldots,U_m\}\) of X. We prove that
\(\bigvee_jh(U_j)\wedge k(U_j)=1_M\). Let \(O\times C\) be any nonempty target basic rectangle, with \(O\) a rational interval and C a clopen Cantor cylinder specifying finitely many coordinates. Fix \(q\in O\). For every \(n\), one U_j contains \(t_{q,n}\), hence contains some \(N_{q,n,I_n}\) with \(q\in I_n\). By infinite pigeonhole, one j occurs for infinitely many n. Choose distinct \(n,n'\) among them outside the finite support of C. Then
\[
(O\cap I_n\cap I_{n'})\times(C\cap A_n\cap B_{n'})
\]
is a **nonempty open** subset of
\(h(U_j)\wedge k(U_j)\). Thus the union of the intersections is dense in \(R\times K\), and its join in M equals 1. The pair (h,k) factors through \(\mathcal D_2(X)\).

**Infinite-cover failure.** Let
\[
\mathcal C=\{A,B\}\cup\{N_{q,n,R}:q\in R,n\ge1\},
\tag{2.3}
\]
where \(N_{q,n,R}\) denotes the open \(\{t_{q,n}\}\cup(R\times c_n)^A\cup(R\times c_n)^B\). This covers X. For c=A or B, \(h(c)\wedge k(c)=0\); for \(c=N_{q,n,R}\), \(h(c)=R\times A_n\), \(k(c)=R\times B_n\), so the meet is again zero. Thus (h,k) does *not* factor through \(\mathcal D\). Since h(A)∧k(B)=1, the difference \(\mathcal D_2\ne\mathcal D\) is genuinely supported in the **disjoint rectangle**
\[
\rho=A\boxtimes B\in\mathcal O(X)\oplus\mathcal O(X).
\tag{2.4}
\]

For this cover (2.3) the earlier rather-below localization element \(t_{\mathcal C}\) is 0. Indeed any nonzero open V⊆X intersects a sheet over a nonempty open subset of R, so for any rational q in that parameter projection and **all** n, (1.1) puts t_{q,n} in cl V. But any finite subunion of (2.3) contains at most finitely many boundary points. Therefore no nonzero V is rather below any such finite subunion.

## 3. The nonregular Urysohn boundary is actually reached

Let \(Q=\mathcal O(X)\oplus\mathcal O(X)\), and let \(d_{\mathcal U}\) denote the open defining the Urysohn closed relation \(\mathcal U=C(d_{\mathcal U})\).

**Claim 3.1.** \(d_{\mathcal U}\wedge\rho\) is dense in \(\rho\), so
\[
\rho\le d_{\mathcal U}^{**}.
\tag{3.1}
\]
**Proof.** Every nonzero open under the rectangle \(\rho\) contains a nonzero rectangle \(u\boxtimes v\) with u≤A, v≤B. Pick two **different** rational parameters in the nonempty open projections \(\pi(u),\pi(v)\), and disjoint open rational intervals I,J around them with disjoint closures in R. Then \(u'=u\cap(I\times P)^A\) and \(v'=v\cap(J\times P)^B\) are nonzero. Formula (1.1) implies cl_X(u')∩cl_X(v')=∅, so \(u'\boxtimes v'\le d_{\mathcal U}\) is a nonzero subrectangle. This proves density and hence (3.1). □

Set
\[
G=\mathcal U\wedge O(d_{\mathcal U}^{**}),\qquad
H_2=\mathcal W_2\wedge G.
\]
By (3.1), on O(ρ) one has \(G=\mathcal U\) and \(H_2=\mathcal W_2\). The map (h,k) factors through \(\mathcal D_2\wedge O(\rho)\), hence this sublocale is nonzero and lies in \(H_2\). Moreover it does **not** lie in \(\mathcal D\): otherwise h,k would factor through D, contradicting (2.3).

Thus the strict difference between D2 and D occurs **inside the nonregular Urysohn boundary H2 itself**, unlike the earlier product control \(P\times Y\) where \(H_2=0\).

## 4. Nevertheless the full fitted diagonal is dense in U on the same rectangle

**Claim 4.1.** For any sheet opens \(u\le A,v\le B\), if
\[
\pi(u)\cap\pi(v)=\varnothing,
\]
then \(u\boxtimes v\le d_{\mathcal U}\). Indeed, regularity of R permits covers of π(u),π(v) by rational opens whose **individual closures lie inside the respective projections**. Refine u,v by these intervals. Each resulting crossed pair has disjoint parameter closures, hence disjoint closures in X by (1.1); therefore each resulting rectangle is one of the far generators of d_U. Taking joins proves the claim.

Conversely, if \(\pi(u)\cap\pi(v)\ne\varnothing\), choose \(q\) in that intersection and finite sets \(F\in u_q\), \(G\in v_q\). Choose any n and put \(H=F\cup G\cup\{n\}\). Because u,v are upward open, \((q,H)^A\in u\) and \((q,H)^B\in v\). Every open cover of X contains a member holding \(t_{q,n}\); that member includes an N_{q,n,I}, hence **both** these sheet points. Therefore
\[
((q,H)^A,(q,H)^B)
\]
is an **ordinary full-cover-compatible point**, so lies in the point set of \(\mathcal D\), and belongs to \(O(u\boxtimes v)\).

It follows that every nonzero relative open of \(\mathcal U\wedge O(\rho)\) meets \(\mathcal D\). Any such relative open is generated by restrictions of rectangles u⊠v. If the parameter projections of such a rectangle are disjoint, Claim 4.1 shows its U restriction is zero. Otherwise the preceding construction provides a point of D. Thus
\[
\boxed{\mathcal W\wedge O(\rho)
=\mathcal W_2\wedge O(\rho)
=\mathcal U\wedge O(\rho).}
\tag{4.1}
\]
This does not assert any global equality for X.

**Atomlessness of the reached boundary.** Every nonzero relative open of \(\mathcal U\wedge O(\rho)\) contains a **nonzero relatively open restriction** of some rectangle u⊠v whose parameter projections overlap. Choose two disjoint nonempty rational intervals I,J contained in their intersection. The two subrectangles obtained by restricting *both* coordinates to I and to J have nonzero U restrictions by the compatible-point argument and are disjoint. Thus no nonzero relative open is hyperconnected; the Booleanization of \(\mathcal U\wedge O(\rho)=H_2\wedge O(\rho)\) is atomless.

## 5. Interpretation and precise limitation

This is the first test in this line of work in which:

- the closed complement of the disjoint sheets is noncompact;
- the cover-dependent rather-below locus vanishes;
- D2>D is witnessed by genuinely infinitary, disjointly supported Cantor/Boolean maps;
- the open Urysohn region on that **same** rectangle is nonregular and has a nonzero atomless H2 part;
- the difference D2>D survives **inside** H2.

Yet Q′ is not refuted, because D has its own dense, full-cover-compatible **ordinary** pairs on the same boundary, supplied by shared rational parameters and common finite-set extensions. These ordinary pairs are enough to yield (4.1) independently of the Cantor maps.

A further counterexample construction must eliminate this shared-extension mechanism **while keeping the Boolean finite-cover witness nonzero on the residual boundary**. Merely twisting a two-apex product, adding a noncompact interface, or localizing the same hyperconnected sheet filters over a crowded regular base is insufficient.

**No claim that Q′ is true or false; no second audit requested.** Preserve the distinction between local equality (4.1) and any unproved global statement.
