# Project A — A CONNECTED compact example W = H ∧ U < H,U, and a finite-Alexandrov W-product theorem

**9 November 2026. NEW WORKING RESULTS, internally checked, not independently externally audited or priority-checked.** This strengthens [the first product/scattered example](A-W-HmeetU-product-transfer-nondisjoint-example-2026-11-09.md): the new example is **topologically connected** and does not use scatteredness or point-determination of arbitrary sublocales. Q and Q′ remain deferred. The compact two-apex W=H input was proved internally in [the shrinking note](A-W-equals-H-compact-two-apex-telescope-2026-11-09.md), not yet externally refereed.

Notation \(Z=X\times Y\) for localic products, \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal H\) the least closed fitted diagonal hull, \(\mathcal U\) Urysohn, \(\mathcal F\) functional. For a finite poset P equipped with upper Alexandrov topology write
\[
C_P=\{(p,q)\in P^2:\exists t\le p,q\}=\operatorname{pt}\mathcal D(P).
\]
Finite coherent theory gives \(W(P)=U(P)=\overline{C_P}\).

## 1. Elementary section calculus for a finite Alexandrov factor

Let P be a **finite** upper-Alexandrov poset, Y an **arbitrary locale**, and let \(L=\mathcal O(Y)\). There is a canonical frame isomorphism
\[
\boxed{\mathcal O(P\times Y)\cong
\{(v_p)_{p\in P}\in L^P:p\le q\Rightarrow v_p\le v_q\}}
\tag{1.1}
\]
with pointwise finite meets and arbitrary joins. For each open v, \(v_p\in L\) is the pullback along the p-slice \(Y\to P\times Y\). The decomposition
\[
v=\bigvee_{p\in P}\bigl(\uparrow p\boxtimes v_p\bigr)
\tag{1.2}
\]
shows the sections determine v: at q the right side is \(\bigvee_{p\le q}v_p=v_q\). (For general rectangles use the finite basis of principal upsets \(\uparrow p\).)

Likewise opens of \((P\times Y)^2\cong P^2\times Y^2\) are monotone families \(w_s\in\mathcal O(Y^2)\), indexed by \(s=(p,q)\in P^2\) with coordinatewise specialization order.

For a sublocale \(S\le Y^2\), write \(e=d_{\operatorname{cl}S}\in\mathcal O(Y^2)\), the **largest open disjoint from S**. Fix \(s\in P^2\), and consider the locale map \(i_s:Y^2\to P^2\times Y^2\) at the fixed P² coordinate s. The closure of the image of S under this map satisfies
\[
\boxed{\operatorname{cl}\bigl(\operatorname{im}(i_s|_S)\bigr)
=C_{P^2}(\text{outside }\downarrow s)\ \times\operatorname{cl}(S)
=(\downarrow s)\times\operatorname{cl}(S).}
\tag{1.3}
\]
The displayed notation in the middle means the **closed sublocale** whose P² point set is \(\downarrow s\); it does not mean the outside region itself is closed. To verify (1.3) independently of spatiality of Y: an open w is disjoint from the image iff its s-section \(w_s\le e\). By monotonicity, the **largest** such open has
\[
w_t=
\begin{cases}
e,&t\le s,\\
1,&t\nleq s.
\end{cases}
\]
Its closed complement is exactly \((\downarrow s)\times\operatorname{cl}S\).

## 2. Universal product formula for W with a finite poset

**Theorem 2.1 (new working theorem).** For **every** finite upper-Alexandrov poset P and **every** locale Y,
\[
\boxed{\mathcal W(P\times Y)=\mathcal W(P)\times\mathcal W(Y).}
\tag{2.1}
\]
No coherence, compactness, spatiality or local compactness is assumed for Y. The product of relations is understood as a sublocale of \(P^2\times Y^2\) under canonical coordinate rearrangement.

*Proof: upper bound.* The established lax naturality of W under arbitrary locale maps gives, for the two projections \(P\times Y\to P\) and \(P\times Y\to Y\),
\[
W(P\times Y)\le
\bigl(W(P)\times Y^2\bigr)\wedge\bigl(P^2\times W(Y)\bigr)
=W(P)\times W(Y).
\tag{2.2}
\]

*Proof: lower bound.* Fix any common-lower-bound pair \(s=(p,q)\in C_P\), choosing \(t\in P\) with t≤p,q. For **every** open cover \(\mathcal C\) of \(P\times Y\), its family of t-slices \((c_t)_{c\in\mathcal C}\) covers \(Y\), and for each c, \(c_t\le c_p,c_q\). The diagonal-cover open \(w_{\mathcal C}^{P\times Y}=\bigvee_{c\in\mathcal C}c\boxtimes c\) pulls back along i_s to
\[
i_s^*w_{\mathcal C}^{P\times Y}
=\bigvee_{c\in\mathcal C}c_p\boxtimes c_q
\ \ge\ \bigvee_{c\in\mathcal C}c_t\boxtimes c_t
=w^{Y}_{(c_t)_{c\in\mathcal C}}.
\]
By definition \(D(Y)\le O(w^Y_{(c_t)})\). Hence the composite locale map
\[
D(Y)\hookrightarrow Y^2\xrightarrow{i_s}(P\times Y)^2
\]
factors through **every** open diagonal neighborhood of \(P\times Y\); therefore its image lies in \(D(P\times Y)\).

Taking closures and invoking the frame-level calculation (1.3) with \(S=D(Y)\) gives
\[
(\downarrow s)\times W(Y)\le W(P\times Y)
\qquad(s\in C_P).
\tag{2.3}
\]
There are finitely many s. Their **finite sublocale join is closed**, and its defining complementary open sections show it equals
\[
\left(\bigcup_{s\in C_P}\downarrow s\right)\times W(Y)
=\overline{C_P}\times W(Y)
=W(P)\times W(Y).
\tag{2.4}
\]
Together with (2.2), this proves (2.1). □

**Caution:** The finite P assumption enters twice: opens admit the monotone-section presentation, and the common-lower family has a **finite** closed join. Do not extrapolate to arbitrary locale products or arbitrary infinite Alexandrov spaces without new proof.

## 3. A finite fence with up-cofinal Urysohn relation

Take
\[
P=\{m,a,k,b,n\},\qquad a<m,\ a<k,\ b<k,\ b<n,
\]
with no further nontrivial comparisons. This is a finite compact connected coherent sober locale. Direct finite enumeration verifies
\[
\boxed{U(P)=W(P)=P^2\setminus\{(m,n),(n,m)\},\quad H(P)=F(P)=P^2.}
\tag{3.1}
\]
Moreover, **upward saturation of U(P) is the entire P²**:
\[
\boxed{\uparrow_{P^2}U(P)=P^2,}
\tag{3.2}
\]
because the only missing pairs \((m,n),(n,m)\) lie respectively above \((a,b),(b,a)\), which belong to \(I(P)\le U(P)\). This was independently checked by enumerating all 25 P² pairs (U(P) has 23 and the up-saturation has 25).

## 4. The connected compact two-apex factor

Let \(Y=\mathbb R\cup\{p_+,p_-\}\), with the usual topology on ℝ, and basic neighborhoods
\[
N_+(F)=\{p_+\}\cup((0,\infty)\setminus F),\quad
N_-(G)=\{p_-\}\cup((-\infty,0)\setminus G),
\]
for finite F,G in their respective half-lines. **These are cofinite half-lines, not tails.**

Previous internally checked calculations (two-apex shrinking note) establish
\[
\boxed{W(Y)=H(Y)=K=A_+^2\cup A_-^2<U(Y)<F(Y)=Y^2,}
\tag{4.1}
\]
where \(A_+=[0,\infty)\cup\{p_+\}\), \(A_-=(-\infty,0]\cup\{p_-\}\), both closed. In particular K is an ACTUAL closed **fitted** sublocale of Y², though the two-apex localic square can have pointless sublocales.

Y is compact, locally compact, sober, \(T_1\), **noncoherent**, and **connected**: the ordinary real line ℝ is dense and connected, so its closure Y is connected. It has no nonempty compact-open subset contained in a bounded real interval J: an open subset of J compact in Y would be nonempty compact open in the ordinary real line, impossible.

Let
\[
\boxed{Z=P\times Y.}
\tag{4.2}
\]
P is connected because its comparability graph is connected, so Z is **connected**. It is compact, locally compact, sober, T₀ and noncoherent: if it had a basis of compact opens, any point of \(P\times J\) for bounded nonempty interval J would have a compact-open neighborhood L⊆P×J; its projection to Y is nonempty **compact and open** inside J (continuous image of compact and projection of product-open), contradiction. Its localic square is spatial because Z is locally compact sober. We will NOT assume every sublocale of this square is spatial.

Theorem 2.1 and (3.1),(4.1) give the exact localic relation
\[
\boxed{W(Z)=U(P)\times K.}
\tag{4.3}
\]

## 5. Compute H without using spatiality of arbitrary sublocales

**Lemma 5.1 (fitted propagation through a finite poset).** Let P be finite and let K be a **closed fitted** sublocale of Y². Let B⊆P² be an upset whose up-saturation is all of P² (for the application take B=U(P)). Then
\[
\boxed{\operatorname{fit}_{P^2\times Y^2}(B\times K)=P^2\times K.}
\tag{5.1}
\]
Here \(B\times K\) means the (possibly nonclosed) product sublocale of the spatial finite P² sublocale B with K. It suffices for the main application that \(B=U(P)\) is closed.

*Proof for closed B (the needed case).* The right side is fitted since it is the pullback of fitted K along the projection \(P^2\times Y^2\to Y^2\), and contains B×K. Conversely, if O(w) contains B×K, each section \(w_s\) with s∈B contains K as an open sublocale, and monotonicity \(w_s\le w_t\) for s≤t shows every w_t contains K, because \(\uparrow B=P²\). Hence O(w) contains all of P²×K. Taking the meet over **all** such O(w) yields (5.1). □

Use B=U(P) and K=W(Y)=H(Y) in (5.1). Since \(W(Z)=U(P)\times K\),
\[
\operatorname{fit}(W(Z))=P^2\times K.
\tag{5.2}
\]
The right side is **closed as well as fitted** (pullback of closed K), and contains the diagonal. Since H is the least closed fitted diagonal hull and contains W,
\[
\boxed{H(Z)=P^2\times K.}
\tag{5.3}
\]
This is a *point-free computation*: unlike the earlier scattered construction, (5.2)–(5.3) are proved using the sections of open sublocales, with no blanket claim of spatiality of sublocales.

## 6. Compute U and the full strict diamond

Because P and Y are locally compact sober, \((P\times Y)^2\) is the ordinary **spatial** product, and U is a closed sublocale determined by its ordinary point set. Basic product neighborhoods have product closures, so the Urysohn point relation factors:
\[
\boxed{U(Z)=U(P)\times U(Y).}
\tag{6.1}
\]
Combining (4.3),(5.3),(6.1) with \(K\le U(Y)\) gives
\[
\boxed{W(Z)=H(Z)\wedge U(Z).}\tag{6.2}
\]
Strictness witnesses, all ordinary:
\[
\begin{aligned}
((m,0),(n,0))&\in H(Z)\setminus U(Z),\\
((k,p_+),(k,p_-))&\in U(Z)\setminus H(Z).
\end{aligned}
\tag{6.3}
\]
Thus W<H, W<U and H,U incomparable in one **connected** compact noncoherent locale.

Every continuous real-valued function on P is constant (the comparability graph is connected). Every continuous real-valued function on Y is constant (by the cofinite-half-line/continuity-at-zero argument of the preceding two-apex note). For any continuous \(g:P\times Y\to\mathbb R\), restrictions to slices show
\(g(p,y)=g(q,y)=g(q,z)\) for all p,q,y,z. Therefore
\[
\boxed{F(Z)=Z^2.}
\tag{6.4}
\]
Both H(Z) and U(Z) are closed, so their **finite join is their closed union**. The pair
\[
((m,p_+),(n,p_-))
\]
is in F(Z) but in neither H(Z) nor U(Z); hence it is outside H(Z)∨U(Z). This yields the full strict diagram
\[
\boxed{
W=H\wedge U\quad<\quad H,U\quad<\quad H\vee U\quad<\quad F,
}
\tag{6.5}
\]
with H and U incomparable. As usual, the notation \(H,U<H\vee U\) means that **each** of H and U is a strict sublocale of their join; strictness follows from (6.3).

## 7. The fitted supplement in explicit frame terms

Set \(Q=\mathcal O(Z^2)\), \(d=d_{W(Z)}\), \(u=d_{U(Z)}\), \(r=d_{H(Z)}\). The finite-poset section description shows:
\[
d_s=
\begin{cases}
d_K,&s\in U(P),\\
1,&s\notin U(P),
\end{cases}
\quad
u_s=
\begin{cases}
d_{U(Y)},&s\in U(P),\\
1,&s\notin U(P),
\end{cases}
\quad
r_s=d_K\quad(\forall s\in P^2).
\tag{7.1}
\]
Since \(K\le U(Y)\), we have \(d_{U(Y)}\le d_K\), so sectionwise
\[
\boxed{d=u\vee r,\qquad C(r)=H(Z)\text{ fitted}.}
\tag{7.2}
\]
This is a direct **nontrivial certificate** for the fitted-supplement criterion from [the preceding H∧U study](A-W-H-meet-U-fitted-supplements-and-higher-stage-obstruction-2026-11-09.md). Neither r=0 nor r=d suffices here: both H and U strictly exceed W.

## 8. Scope and lessons

1. The original goal — obtain W=H∧U strictly below both H and U without a disjoint-sum construction — is fully achieved, **including topological connectedness**.
2. The new finite-Alexandrov factor theorem \(\mathcal W(P\times Y)=\mathcal W(P)\times\mathcal W(Y)\) is an independent structural result **for arbitrary Y**, supported by a cover and closure-image calculation; it is stronger than the earlier scattered-only transfer formula.
3. The connected example uses the previous internally checked \(W(Y)=H(Y)\) two-apex theorem, so the final result remains **working pending external audit** of this chain of lemmas.
4. We have not asserted analogous product formulas for arbitrary infinite P or general pairs of locales. The P-finite monotone-section calculus is essential to the proof.
5. The successful construction illustrates that the *fitted-supplement* condition can be realized through a factorwise barrier in a connected noncoherent space; no transfinite H iteration or Q/Q′ search is needed.

**Suggested next action:** conduct a targeted adversarial internal audit of the finite-P product lemma and the H propagation step before using the new construction in broader structural claims. Do not promote to the externally vetted theorem register yet.
