# Project A — A non-disjoint-sum example of W = H ∧ U < H,U via a product transfer theorem

**9 November 2026. NEW WORKING RESEARCH: internal mathematical check only; not independently refereed or priority-checked.** Both Q and Q′ remain deferred. This note is a bounded follow-up to [the fitted-supplement/strict-meet study](A-W-H-meet-U-fitted-supplements-and-higher-stage-obstruction-2026-11-09.md). The user requested an example where \(\mathcal W=\mathcal H\wedge\mathcal U\) but \(\mathcal W<\mathcal H\) and \(\mathcal W<\mathcal U\), without placing the two strictness mechanisms in separate clopen summands. A **Cartesian product** of two previously analyzed locales achieves this. The full product formula extends to a useful class; the resulting space is not connected, but the two defects cannot be isolated into different clopen summands.

## 1. The factors and hypotheses

Let \(P\) be a **finite poset** equipped with its upper-Alexandrov topology. Let \(A\) be a **locally compact sober, scattered, \(T_1\) topological space**. Write \(X=P\times A\).

The following background results are crucial and have appeared in the previously independently audited Project A work:
- finite poset locales are coherent, and \(\mathcal W(P)=\mathcal U(P)=\overline{\mathrm{Cm}(P)}\), where \(\mathrm{Cm}(P)=\{(p,q):\downarrow p\cap\downarrow q\ne\varnothing\}\);
- for a locally compact sober scattered \(T_1\) space A, its localic square is the ordinary **scattered** product, every sublocale is spatial/point-determined (scattered-sublocale theorem), and \(\mathcal D(A)=\Delta_A,\ \mathcal W(A)=\mathcal V(A)=\mathcal H(A)=\mathcal I(A)\);
- finite products of scattered spaces are scattered, including finite Alexandrov factors: for a nonempty subset of \(P^2\times A^2\), select a **maximal** element of its finite \(P^2\) projection, making that fiber relatively open, and isolate a point in the corresponding scattered \(A^2\) fiber;
- because P and A are locally compact sober, \(X^2\) is the ordinary topological product \(P^2\times A^2\) and is scattered; **all sublocale equalities below are therefore point-determined**.

Identify \(X^2=(P\times A)^2\) with \(P^2\times A^2\) by coordinate rearrangement. We write product notation \(R_P\times R_A\) for the genuine product sublocale under that identification, not for an unverified general law on all locale relations.

For P put
\[
C_P=\mathrm{Cm}(P)
=\{(p,q):\exists r\le p,q\},\quad
E_P=\{(p,q):p,q\text{ lie in one comparability component}\}.
\]
In the finite class, \(\mathcal H(P)=\mathcal F(P)=E_P\), and \(\mathcal V(P)\subseteq E_P\).

## 2. A general finite-poset × scattered-T₁ product theorem

**Theorem 2.1 (new working transfer theorem).** Under the stated hypotheses,
\[
\boxed{
\begin{aligned}
\mathcal D(X)&=C_P\times\Delta_A,\\
\mathcal I(X)&=\mathcal I(P)\times\mathcal I(A),\\
\mathcal W(X)&=\mathcal U(P)\times\mathcal I(A),\\
\mathcal U(X)&=\mathcal U(P)\times\mathcal U(A),\\
\mathcal V(X)&=\mathcal V(P)\times\mathcal I(A),\\
\mathcal H(X)&=\mathcal H(P)\times\mathcal I(A)=E_P\times\mathcal I(A),\\
\mathcal F(X)&=\mathcal F(P)\times\mathcal F(A)=E_P\times\mathcal F(A).
\end{aligned}}
\tag{2.1}
\]
In particular,
\[
\boxed{\mathcal W(X)=\mathcal H(X)\wedge\mathcal U(X).}
\tag{2.2}
\]

**Proof — D and W.** In a sober space, an ordinary pair belongs to the fitted diagonal iff its points have a common specialization predecessor (the closure-meeting relation Cm). For \(x=(p,a),y=(q,b)\in P\times A\), the specialization order is \((p,a)\le(q,b)\iff p\le q\text{ and }a=b\), since A is T₁. Thus
\[
(x,y)\in\operatorname{pt}(\mathcal D(X))
\iff (p,q)\in C_P,\ a=b.
\]
Since X² is scattered, D(X) is determined by those points, giving \(D(X)=C_P\times\Delta_A\). Topological closure of a product set is the product of the closures. Because \(W(P)=\overline{C_P}=U(P)\) for finite coherent P and \(\overline{\Delta_A}=I(A)\), the W formula follows.

**Proof — I and U.** In ordinary product topology, a pair has intersecting basic neighborhoods precisely when **both** factor-coordinate pairs are inseparable. It has intersecting closures of all basic product neighborhoods precisely when both factor pairs satisfy Urysohn relatedness; use
\[
\overline{V_P\times V_A}
=\overline{V_P}\times\overline{V_A}.
\]
Both I and U are closed sublocales, and X² is spatial, so their point descriptions give the displayed localic product formulas.

**Proof — V.** The fitted hull of a spatial sublocale in this scattered X² is determined by the specialization **up-saturation** of its point set: open neighborhoods have upward-saturated point sets; conversely every specialization upset is an intersection of ambient opens, and all sublocales of X² are spatial. Since A is T₁, up-saturation in X² acts only in the P² coordinate. Therefore
\[
V(X)=\uparrow_{P^2}I(P)\times I(A)=V(P)\times I(A).
\]

**Proof — H.** Let \(T=E_P\times I(A)\). This is topologically closed: E_P is a union of comparability-component squares, and every component of a finite Alexandrov poset is clopen; I(A) is closed. It is upward saturated in the product specialization order: the P² factor is a union of whole components, and A² has equality specialization. Since X² is scattered and every sublocale spatial, T is **fitted** (any specialization upset is the intersection of its open neighborhoods, and sublocale point-determination identifies the intersection). Thus T is a closed fitted relation containing the diagonal, so H(X)≤T.

Conversely H(X) contains I(X). For each \((a,b)\in I(A)\) and each p∈P, this includes the pair \(((p,a),(p,b))\). Because H(X) is closed **and** fitted, its ordinary point relation is both downward and upward saturated in specialization order. Move first and second P coordinates successively along arbitrary finite zigzags of comparabilities; membership in H(X) persists. Thus H(X) includes every \(((p,a),(q,b))\) with p,q in the same comparability component and (a,b)∈I(A), precisely the points of T. Point-determination gives T≤H(X), completing the equality.

**Proof — F.** For any spaces P,A, \(\mathcal F(P\times A)\) has the product **point relation** \(\mathcal F(P)\times\mathcal F(A)\): projection-composed real maps give the inclusion in one direction, and for any continuous real map \(g:P\times A\to\mathbb R\), if \(p\sim_{\mathcal F(P)}q\) and \(a\sim_{\mathcal F(A)}b\), then
\(g(p,a)=g(q,a)=g(q,b)\) by restricting g to fixed-coordinate slices. Point-determination of the closed sublocale F(X) gives equality. A real map P→ℝ is constant along comparabilities, so \(\mathcal F(P)=E_P\).

Finally U(P)≤H(P)=E_P (the coherent general inclusion W≤H). Since I(A)≤U(A),
\[
H(X)\wedge U(X)
=(E_P\times I(A))\cap(U(P)\times U(A))
=U(P)\times I(A)=W(X).
\]
All meets and products are actual closed-subspace operations in the spatial square. □

**Scope caution.** Formula (2.1) is **NOT claimed for arbitrary product locales**, especially where the square may have nonspatial sublocales. Scatteredness is doing essential work by turning the actual fitted diagonal into its full ordinary-point relation.

## 3. Choosing explicit factors for simultaneous strictness

Take the five-point fence \(P=\{m,a,k,b,n\}\) with \(a<m,a<k,b<k,b<n\), all other comparisons reflexive. Its comparability graph is connected. Direct finite calculation gives:
\[
C_P\text{ has 17 ordered pairs},\quad
I(P)\text{ has 15 ordered pairs},\quad
U(P)=P^2\setminus\{(m,n),(n,m)\},\quad
V(P)=H(P)=F(P)=P^2.
\]
Thus \(U(P)<H(P)\). These cardinalities and missing pairs were independently enumerated by a finite-poset calculation in this segment.

Take the **externally checked** compact, locally compact, sober scattered T₁ space \(A=N_1\sqcup N_2\sqcup\{\alpha,\beta,\gamma\}\) with \(N_1,N_2\) infinite discrete, neighborhoods
\[
\alpha:\ \{\alpha\}\cup(N_1\setminus F_1),\quad
\beta:\ \{\beta\}\cup((N_1\cup N_2)\setminus F),\quad
\gamma:\ \{\gamma\}\cup(N_2\setminus F_2).
\]
Here
\[
\begin{aligned}
I(A)&=\Delta_A\cup\{(\alpha,\beta),(\beta,\alpha),(\beta,\gamma),(\gamma,\beta)\},\\
U(A)&=F(A)=\Delta_A\cup\{\alpha,\beta,\gamma\}^2,
\end{aligned}
\tag{3.1}
\]
and \(\mathcal I(A)=\mathcal W(A)=\mathcal H(A)<\mathcal U(A)\).

Set \(X=P\times A\). Theorem 2.1 gives
\[
\boxed{
\begin{aligned}
W(X)&=U(P)\times I(A),\\
H(X)&=V(X)=P^2\times I(A),\\
U(X)&=U(P)\times U(A),\\
F(X)&=P^2\times U(A).
\end{aligned}}
\tag{3.2}
\]

Therefore
\[
\boxed{
W(X)=H(X)\wedge U(X),\quad
W(X)<H(X),\quad W(X)<U(X),\quad
H(X)\nleq U(X),\quad U(X)\nleq H(X).
}
\tag{3.3}
\]
Explicit witnesses:
- \(((m,\beta),(n,\beta))\in H(X)\setminus U(X)\);
- \(((k,\alpha),(k,\gamma))\in U(X)\setminus H(X)\).
Both lie outside W, proving its strictness below both.

There is also a **fourth strict level above the diamond**:
\[
\boxed{H(X)\vee U(X)<F(X).}
\tag{3.4}
\]
Indeed both H,U are closed and their **finite join is their closed union**. The pair
\(((m,\alpha),(n,\gamma))\) lies in F(X) but outside H(X) (since α not-I γ) and outside U(X) (since m not-U n); it is therefore not in their join. Thus the non-disjoint-sum example exhibits the full pattern
\[
W=H\wedge U<H,U<H\vee U<F.
\]

**Noncoherence of X.** A has compact opens \(V_\alpha=\{\alpha\}\cup N_1\) and \(V_\beta=\{\beta\}\cup N_1\cup N_2\) with noncompact intersection N₁. Their products \(P\times V_\alpha\) and \(P\times V_\beta\) are compact opens in X, while their intersection \(P\times N_1\) is noncompact (its continuous projection onto N₁ is an onto map to an infinite discrete noncompact space). Therefore X is compact, locally compact, sober and **noncoherent**.

## 4. Why this is not just a disguised disjoint sum

The new X is **not topologically connected**, because A has isolated clopen sheet points. Do not claim connectedness.

However the two strictness mechanisms cannot be segregated into distinct clopen summands. Every clopen subset E⊆P×A has the form P×C with C⊆A clopen:

For each a∈A, the section \(E_a=\{p:(p,a)\in E\}\) is clopen in P. The comparison graph of P is connected, so P has no proper nonempty clopen subspace; hence each E_a is either P or empty. Therefore E=P×C. Pulling E back along any fixed p-slice A→P×A shows C is clopen.

In A, α I β and β I γ, so no clopen partition can separate these three points; if a clopen C contains one, it contains all three. Consequently any clopen summand of X containing one boundary fiber P×{α,β,γ} contains **all three** fibers. The witness for H\U uses β and the witness for U\H uses α,γ, so **both strictness mechanisms occur within every clopen summand containing the boundary fibers**.

Thus the construction is a genuinely **multiplicative** interaction of the two relation defects, and not a recombination of separate clopen examples as in the previous disjoint-sum illustration.

**Remaining limitation:** We have not produced a *connected* example. This particular scattered-T₁ transfer technique cannot produce one: any nontrivial scattered T₁ space has an isolated point, whose singleton is clopen, and its nonempty product with P is therefore disconnected. To seek connected examples one must leave this scattered-T₁ class and confront the possibility of pointless fitted-diagonal structure; the formulas above cannot be reused without new proofs.

## 5. Research meaning, status, and follow-up

The transfer theorem says that finite specialization geometry and scattered T₁ non-Urysohn geometry can mix *within a product* while the two corresponding defects remain exactly orthogonal:
\[
\underbrace{U(P)<H(P)}_{\text{specialization defect}},
\qquad
\underbrace{I(A)<U(A)}_{\text{non-Urysohn T₁ defect}},
\]
produce \(W(X)=H(X)\wedge U(X)\), even though both W<H and W<U.

The closed fitted **barrier** from the preceding fitted-supplement note is explicit: \(H(X)=P^2\times I(A)\), and its closed complementary open \(r=d_{H(X)}\) satisfies \(d_{W(X)}=d_{U(X)}\vee r\). This witnesses the fitted-supplement theorem without transfinite iteration of H.

**Suggested next bounded direction:** examine whether the product formula remains valid when A is a *connected* non-Hausdorff T₁ space with I(A)<U(A), for example by replacing the discrete sheets with connected rays. Such an A is not scattered, so the fitted diagonal D(P×A) may carry extra pointless structure. This is a specific technical obstruction, not a reason to reopen the deferred Q′ search.

**Status:** new working proof and transfer theorem, internally checked but not independently refereed; the underlying component examples have previous external provenance. Do not promote to audited theorem ledger yet.
