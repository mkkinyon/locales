# Project A — BLIND independent audit packet: W as a relation, W=H, and H∧U

**9 November 2026. All new conclusions are WORKING CLAIMS submitted for independent adversarial checking.** Please read the accompanying blind prompt first. This packet does **not** contain prior internal-audit conclusions, earlier referee opinions, or hints about which claims we expect to fail.

## 0. Purpose, notation, and standard inputs to verify

Let \(X\) be a locale, \(L=\mathcal O(X)\), and \(Q=L\oplus L=\mathcal O(X\times_{\mathrm{loc}}X)\). Denote coproduct generators by \(a\boxtimes b\). If \(u\in Q\), \(O(u)\) and \(C(u)\) denote respectively the open sublocale (nucleus \(u\to -\)) and its complementary closed sublocale (nucleus \(u\vee -\)). The sublocale lattice is a **coframe**; arbitrary meets of open sublocales are called **fitted**. Let \(\operatorname{fit}S\) be the least fitted sublocale containing S, and \(\operatorname{cl}S\) the least closed sublocale containing S.

Put \(\Delta\) for the localic diagonal. For an open cover \(\mathcal C\) of the unit of L, set
\[
 w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c.
\]
Use the relations
\[
\begin{aligned}
\mathcal I&=\operatorname{cl}\Delta,
&\mathcal D&=\operatorname{fit}\Delta
   =\bigcap_{\mathcal C\text{ cover}}O(w_{\mathcal C}),\\
\mathcal V&=\operatorname{fit}\mathcal I,
&\mathcal W&=\operatorname{cl}\mathcal D,\\
\mathcal U&=C(d_{\mathcal U}),
&d_{\mathcal U}&=\bigvee\{a\boxtimes b:a^*\vee b^*=1\},\\
\mathcal F&=\bigwedge_{f:X\to\mathbb R}\ker(f),
&\mathcal H&=\text{least closed and fitted sublocale of }X^2\text{ containing }\Delta.
\end{aligned}
\]
Established general inclusions (the referee should challenge their use if necessary):
\[
\mathcal I\le\mathcal W\le\mathcal U\le\mathcal F,
\qquad \mathcal W,\mathcal V\le\mathcal H\le\mathcal F.
\]
\(\mathcal F\) is closed and fitted. Our new central question is whether
\[
\boxed{\mathcal W=\mathcal H\wedge\mathcal U}
\]
can hold strictly below BOTH \(\mathcal H\) and \(\mathcal U\) in a connected compact locale. We also study sufficient conditions for \(\mathcal W=\mathcal H\).

**Standard/literature inputs, not claimed as new:** (S1) a localic product of locally compact sober spatial factors agrees with the ordinary topological product; (S2) all sublocales of a spatial scattered locale are spatial/point-determined; (S3) coherent locales have spectral point spaces with compact Priestley patch topology, and a closed sublocale is fitted iff its patch-closed point set is upward-specialization-saturated; (S4) coherent locales satisfy \(\mathcal W=\mathcal U=\mathcal I\circ\mathcal I\), where the point relation of \(\mathcal I\) consists of pairs with a common specialization upper bound; (S5) \(\mathcal F\) is the least patch-closed equivalence containing comparability connectivity in the coherent case; (S6) finite joins of closed sublocales remain closed. Please identify any inaccurate statement or missing hypothesis here; the claims below depend on them.

**Important:** a spatial locale need not have all its sublocales spatial. In the connected example we use point-determination ONLY for **closed** sublocales of a spatial square, not for its fitted diagonal or fitted hull.

## 1. Boolean-valued cover compatibility and lax naturality

**Claim B1 (all locales).** For \(a,b\in L\), the following are equivalent:

(a) \(\mathcal W\wedge O(a\boxtimes b)\ne0\);

(b) \(\mathcal D\wedge O(a\boxtimes b)\ne0\);

(c) there are a nontrivial complete Boolean frame B and frame maps \(h,k:L\to B\) such that for every cover \(\mathcal C\),
\[
\bigvee_{c\in\mathcal C}h(c)\wedge k(c)=1_B,
\qquad h(a)\wedge k(b)\ne0.
\tag{B1}
\]
One can require \(h(a)=k(b)=1_B\). Proof sketch: (a) iff (b) by density of \(\mathcal D\) in its closure and restriction to opens. For (b)⇒(c), quotient \(Q\) by the nonzero sublocale \(\mathcal D\wedge O(a\boxtimes b)\), Booleanize it, and restrict to the two coproduct injections. Conversely a compatible pair factors through \(\mathcal D\), and a nonzero Boolean meet can be localized to a nontrivial Boolean target.

Hence \(\mathcal W=\operatorname{cl}_{X^2}B(\mathcal D)\), where \(B(\mathcal D)\) denotes the least dense Boolean sublocale of \(\mathcal D\). These are **Boolean-valued** compatible pairs, not merely ordinary points.

**Claim B2 (lax naturality).** Every locale map \(f:Y\to X\) satisfies
\[
\mathcal D_Y\le(f\times f)^{-1}\mathcal D_X,
\qquad \mathcal W_Y\le(f\times f)^{-1}\mathcal W_X.
\tag{B2}
\]
Proof sketch: pull back any cover of X, then take the closed hull. Equality on restriction can fail for open or closed embeddings, already on the two dual three-point upper-Alexandrov forks \(0<p,0<q\) and \(p<1,q<1\), respectively. Nevertheless W decomposes exactly over clopen disjoint sums.

## 2. Coherent W=H and a finite fence

**Claim C1 (coherent case).** The following conditions are equivalent:
\[
\mathcal W=\mathcal H;
\quad\mathcal W\text{ fitted};
\quad\mathcal U\text{ fitted};
\quad\mathcal U=\mathcal F;
\quad\mathcal U\circ\mathcal U\le\mathcal U.
\tag{C1}
\]
The equivalence of the first three follows from coherent \(W=U\) and minimality of H. If U is fitted, it is both downward and upward saturated on spectral points, and its diagonal forces comparability connectivity; the minimality of F yields U=F. Conversely F is fitted/transitive. If U is internally transitive, its point relation is a patch-closed equivalence containing comparability, so U=F. (Please check the coherence and point-to-sublocale steps.)

**Claim C2 (maximal-specialization criterion).** For P the spectral point space of a coherent locale,
\[
\boxed{\mathcal W=\mathcal H\iff
\text{every pair of maximal points in every comparability-connected component of P has a common lower bound}.}
\tag{C2}
\]
The needed point formula is
\[
(x,y)\in\mathcal U\iff\exists u\ge x,\ v\ge y,\ z\le u,v.
\tag{C2a}
\]
Every spectral point has a maximal specialization above it, by a Zorn argument using compactness of the patch topology: a chain of specializations has an upper bound in the intersection of all compact-open neighborhoods of all its members. The condition on maxima then makes every comparable-zigzag-connected pair U-related. Conversely, U=F forces U-related maxima to share a lower bound via (C2a).

**Finite test P (the “five-point fence”).** Let \(P=\{m,a,k,b,n\}\) with covering relations
\[
a<m,\ a<k,\ b<k,\ b<n,
\]
and no other nontrivial comparisons. Its comparability graph is connected, and direct finite computation gives
\[
\begin{aligned}
\mathcal D(P)&=\{(p,q):\exists t\le p,q\},\\
\mathcal U(P)=\mathcal W(P)&=P^2\setminus\{(m,n),(n,m)\},\\
\mathcal V(P)=\mathcal H(P)=\mathcal F(P)&=P^2.
\end{aligned}
\tag{C3}
\]
In particular, \(\uparrow_{P^2}\mathcal U(P)=P^2\); the missing (m,n) and (n,m) lie above (a,b) and (b,a). The order-dual fence exchanges the behavior of W and V at H. These concrete calculations are relevant to §§7–8.

## 3. Fitted envelopes, pointlessness, and finite-branch shrinking

For arbitrary Q and d∈Q, \(C(d)\) is fitted iff
\[
\forall b\in Q,\quad d\not\le b\implies
\exists w\in Q:\ d\vee w=1,\ w\to b\ne b.
\tag{F1}
\]
This is the standard frame fitness axiom localized at one element; please check the fixed-point proof.

If \(S\le T\le Z\) and T is fitted in Z, then
\[
\operatorname{fit}_T(S)=\operatorname{fit}_Z(S)
\tag{F2}
\]
when the former is regarded as a sublocale of Z. Thus
\(W=H\iff W\text{ fitted intrinsically inside }F\).

A sufficient condition is that the open complement \(d_W\) be regularly generated inside the frame \(\mathcal O(F)=\uparrow d_F\). A still stronger, simple condition is that W be clopen **inside F**. Absolute rather-below generation of \(d_W\), however, would force \(W=U\), and is too strong for our noncoherent examples.

**Pointless-residual observation.** If \(Z=X^2\) is spatial and T₁, the fitted hull of any closed sublocale C has exactly the same ordinary points as C: a point outside C is excluded by the open complement of its singleton, which contains C. Therefore \(W<H\) implies that \(\operatorname{fit}(W)\wedge O(d_W)\) is a **nonzero pointless sublocale**, lying within \(F\wedge O(d_W)\).

**Claim F3 (finite-branch coframe lemma).** For finitely many decreasing towers of sublocales \(S_{j,n}\),
\[
\bigwedge_n\left(\bigvee_{j=1}^mS_{j,n}\right)
=\bigvee_{j=1}^m\bigwedge_nS_{j,n}.
\tag{F3}
\]
For m=2, fix k, use \(S_{1,n}\le S_{1,k}\) for n≥k, distribute finite joins over arbitrary meets, then meet over k. The result is false for infinitely many branches, even in the two-element Boolean algebra (eventually zero towers indexed by j).

**Claim F4 (explicit null-tower test).** If \(r_1\ge r_2\ge\cdots\) in frame Q and
\[
r_1\le\bigvee_n r_n^*,
\tag{F4}
\]
then \(\bigwedge_n O(r_n)=0\). A Boolean-valued proof uses \(t=\bigwedge_n g(r_n)\): it satisfies \(t\le\neg t\). A direct sublocale proof is also possible.

**Claim F5 (arbitrary-frame finite-branch fittedness).** Let \(T=C(d)\), and suppose \(d=\bigvee_{i\in I}t_i\). For each i assume there are open neighborhoods \(w_{i,n}\) of T (\(w_{i,n}\vee d=1\)), a finite number \(m_i\) of decreasing open towers \(r_{i,j,n}\), and
\[
t_i\wedge w_{i,n}\le\bigvee_{j=1}^{m_i}r_{i,j,n},\qquad
\bigwedge_n O(r_{i,j,n})=0
\quad(1\le j\le m_i).
\tag{F5}
\]
Then T is fitted. Proof sketch: put \(S=\operatorname{fit}T\); restrict S to each open sector \(O(t_i)\). Its intersection with the chosen neighborhoods is bounded above by the finite join of zero-meet towers; (F3) gives zero. The general open-locality identity
\[
S\wedge O(\bigvee_i t_i)=\bigvee_i(S\wedge O(t_i))
\tag{F5a}
\]
then eliminates the entire open complement of T. The number of sectors may be infinite; **branch width in each sector must be finite**. One may use (F4) instead of directly proving each tower Boolean-null. This is a general fittedness theorem, not restricted to relation W.

## 4. The compact cofinite-half-line TWO-APEX space

Let \(Y=\mathbb R\cup\{p_+,p_-\}\), usual topology on the ordinary \(\mathbb R\), with apex neighborhoods
\[
N_+(F)=\{p_+\}\cup((0,\infty)\setminus F),\quad
N_-(G)=\{p_-\}\cup(( -\infty,0)\setminus G),
\tag{A1}
\]
where F,G are finite subsets of the indicated entire half-lines. **These are cofinite half-lines, not tails \((N,\infty)\).** Let
\[
 u_+=(0,\infty)\cup\{p_+\},\quad
 u_-=(-\infty,0)\cup\{p_-\},
\]
\[
 A_+=[0,\infty)\cup\{p_+\},\quad
 A_-=(-\infty,0]\cup\{p_-\},\quad
 K=A_+^2\cup A_-^2.
\]
The space is claimed compact, locally compact, sober, connected, T₁ and noncoherent. Its localic square is the spatial ordinary square.

**Claim A2 (relations).** The ordinary Urysohn relation, as a closed sublocale, is
\[
\mathcal U(Y)=K\cup\{(p_+,p_-),(p_-,p_+)\}.
\tag{A2}
\]
The claim \(\mathcal W(Y)=K\) can be proved as follows. Every pair of points in the same \(u_+\) (respectively \(u_-\)) is Urysohn-related: every small real-open neighborhood on the positive (respectively negative) side has p+ (respectively p−) in its closure. Thus \(\bigcup_\pm u_\pm\boxtimes u_\pm\le U\). Use the established regular-core inequality
\(\operatorname{cl}(\operatorname{int}U)\le W\)
(which the referee should check if concerned) to infer \(K\le W\).

Conversely, \(W\le U\); all U-pairs outside K are the two cross-apex pairs. The two-element cover \(\{Y\setminus\{p_+\},Y\setminus\{p_-\}\}\) has diagonal-square neighborhood excluding both cross-apex pairs. On a mixed open rectangle \(u_+\boxtimes u_-\), the restriction of U is precisely the single ordinary point \((p_+,p_-)\), so D is zero there and W, its closure, is also zero there. Symmetrically for the transposed rectangle. Therefore W≤K. This proof uses the fact that the open restriction of a one-point spatial U-sublocale has no nonzero pointless part.

**Claim A3 (two-sided shrinking proves W=H).** Write
\[
d_W=(u_+\boxtimes u_-)\vee(u_-\boxtimes u_+).
\]
For n≥1 take \(a_n=(0,1/n)\), \(b_n=(-1/n,0)\), and closed sets
\[
 C_n^+=[1/n,\infty)\cup\{p_+\},\quad
 C_n^-=(-\infty,-1/n]\cup\{p_-\}.
\]
Define open W-neighborhoods
\[
 w_{+,n}=Y^2\setminus(C_n^+\times C_n^-),\qquad
 w_{-,n}=Y^2\setminus(C_n^-\times C_n^+).
\]
They satisfy
\[
(u_+\boxtimes u_-)\wedge w_{+,n}
 =(a_n\boxtimes u_-)\vee(u_+\boxtimes b_n),
\tag{A3}
\]
with the transposed equation on the other sector. Since
\(\bigcap_n\overline{a_n}=\{0,p_+\}\) and
\(\bigcap_n\overline{b_n}=\{0,p_-\}\), their open sublocale towers have zero meet (these are **sublocale**, not just point-set, equalities). The corresponding rectangle branches have zero meet. Claim F5 forces W fitted. In fact a stronger explicit equality is claimed:
\[
\boxed{W(Y)=\bigwedge_{n\ge1}O(w_{+,n})\wedge\bigwedge_{n\ge1}O(w_{-,n}).}
\tag{A4}
\]
Every continuous real-valued function Y→ℝ is constant, giving \(F(Y)=Y^2\). The strict chain is \(W(Y)=H(Y)=K<U(Y)<F(Y)\). Relative clopenness and absolute regular generation both fail; W=H is obtained by shrinking rather than clopen separation.

## 5. Other noncoherent examples and a finite multi-apex family

**Scattered three-point boundary control.** Let A consist of infinite discrete sets \(N_1,N_2\) and T₁ limit points \(\alpha,\beta,\gamma\), with cofinite neighborhoods along N₁ for α, along both N₁∪N₂ for β, and along N₂ for γ. The previously claimed hierarchy is
\[
W(A)=V(A)=H(A)=I(A)<U(A)=F(A),
\tag{M1}
\]
with I(A) containing α–β and β–γ but not α–γ. Inside F the extra pairs \((\alpha,\gamma),(\gamma,\alpha)\) are relatively clopen. Claim F5 applies **degenerately** inside F with one constant-zero branch.

**Negative control.** A previously constructed compact noncoherent T₀ example with boundary points p<x and y, and two infinite discrete sheets, has \(W=I<H=U=V=F\); an ordinary \((x,y)\in H\setminus W\) prevents the finite-branch criterion from holding on a sector containing it. This is a consistency check, not a new theorem of this packet.

**Claim M2 (finite m-apex star family).** For finite m≥2, let \(R_i=(0,\infty)\times\{i\}\) be m rays joined at a common origin o, and adjoin m apexes \(p_i\), with neighborhoods \(\{p_i\}\cup(R_i\setminus F)\), F finite. Write \(u_i=R_i\cup\{p_i\}\), \(A_i=R_i\cup\{o,p_i\}\), and \(K_m=\bigcup_i A_i^2\). Claim X_m compact, locally compact, sober, noncoherent, T₁, with a spatial square. Then
\[
\boxed{W(X_m)=H(X_m)=K_m
   <U(X_m)=K_m\cup\{(p_i,p_j):i\ne j\}<F(X_m)=X_m^2.}
\tag{M2}
\]
For i≠j, the open mixed sector \(u_i\boxtimes u_j\) meets U in just the cross-apex point, excluded from D by the binary cover \(\{X_m\setminus\{p_i\},X_m\setminus\{p_j\}\}\). The universal regular core gives K_m≤W; mixed-sector exclusion gives W≤K_m.

For each i,n define \(a_{i,n}=(0,1/n)\times\{i\}\), \(C_{i,n}=\{p_i\}\cup([1/n,\infty)\times\{i\})\). These C are closed, and \(\bigcap_n\overline{a_{i,n}}=\{o,p_i\}\). For each ordered i≠j define \(w_{ij,n}=X_m^2\setminus(C_{i,n}\times C_{j,n})\); in the sector \(t_{ij}=u_i\boxtimes u_j\),
\[
t_{ij}\wedge w_{ij,n}=(a_{i,n}\boxtimes u_j)\vee(u_i\boxtimes a_{j,n}).
\tag{M3}
\]
The two branches vanish and F5 yields W=H. Moreover \(W=\bigwedge_{i\ne j,n}O(w_{ij,n})\), with m(m−1) mixed sectors and two shrinking branches each. Please check all topological and localic steps, including nonspatial residuals.

## 6. The intermediate relation H∧U and fitted supplements

Put \(d=d_W\), \(u=d_U\), \(h=d_H\) in Q, so \(h,u\le d\), \(H\wedge U=C(h\vee u)\).

**Claim S1 (all frames).** The following are equivalent:
\[
\boxed{W=H\wedge U}
\quad\Longleftrightarrow\quad
\exists r\le d:\ d=u\vee r\ \text{ and }C(r)\text{ fitted}.
\tag{S1}
\]
Proof: if r exists, W≤C(r) implies H≤C(r) by H's minimality; intersect with U. Conversely take r=h. Equivalently, one can give a family r_i≤d of fitted barriers with d=u∨∨r_i, since arbitrary meets of closed fitted sublocales are closed fitted. A relative variant may certify C(r) fitted **inside F** by relative regular generation or F5.

**Claim S2 (Boolean failure witness).** Write \(\mathscr R_d=\{r\le d:C(r)\text{ fitted}\}\), so \(h=\bigvee\mathscr R_d\). Strict W<H∧U iff some nontrivial complete Boolean frame B admits a frame map g:Q→B with
\[
g(d)=1_B,\quad g(u)=0_B,\quad g(r)=0_B\quad(r\in\mathscr R_d).
\tag{S2}
\]
This is obtained by Booleanizing \(H\wedge U\wedge O(d)\) and conversely.

**A warning about one-step criteria.** For the five-point upper-Alexandrov poset \(a<s,\ b<s,\ b<t,\ c<t\), let closed sublocales \(S=\{a\}\), \(U_0=\{a,c\}\). Iterating \(S_{n+1}=\operatorname{cl}(\operatorname{fit}S_n)\) yields \(S_0=\{a\}\), \(S_1=\{a,s,b\}\), \(S_2=P\). The restriction \(S_0\cap U_0=S_1\cap U_0=\{a\}\) but \(S_2\cap U_0=U_0\). This is a general hull-calculus control, NOT a direct diagonal example. It warns that fitting and subsequent closure can leave and later reenter a given closed relation.

**Disjoint-sum control:** The coherent fence with W=U<H and the scattered αβγ space with W=H<U give W=H∧U strictly below both factors on their disjoint sum. Adding the compact T₀ negative control yields a genuinely strict intermediate meet, but with defects in separate clopen summands. The main goal below is to achieve a stronger, connected example.

## 7. A finite-Alexandrov factor product theorem for **arbitrary** locales

This is a **principal claim** of the packet, independent of the connected example. Let P be a finite upper-Alexandrov poset, Y any locale whatsoever (possibly pointless/noncompact), and M=O(Y). The localic product frame is claimed to have the canonical presentation
\[
\boxed{\mathcal O(P\times Y)\cong
\operatorname{Up}(P,M)=\{(v_p)_{p\in P}:p\le q\Rightarrow v_p\le v_q\}.}
\tag{P1}
\]
The join/meet are pointwise. Every open has the decomposition
\(v=\bigvee_{p\in P}(\uparrow p\boxtimes v_p)\); check both directions of this frame isomorphism, not just surjectivity.

The square frame \(\mathcal O((P\times Y)^2)\) is correspondingly \(\operatorname{Up}(P^2,\mathcal O(Y^2))\), using coordinatewise order on P².

**Claim P2 (new product theorem).** For every such P and arbitrary Y,
\[
\boxed{W(P\times Y)=W(P)\times W(Y).}
\tag{P2}
\]
*Upper inclusion:* apply lax naturality B2 to the two product projections.

*Lower inclusion:* Let \(s=(p,q)\in P²\) have a common lower bound t≤p,q. For every cover \(\mathcal C\) of P×Y, the family of t-slices \((c_t)_{c\in\mathcal C}\) covers Y and
\[
(i_s)^*(w_{\mathcal C}^{P\times Y})
=\bigvee_{c\in\mathcal C}c_p\boxtimes c_q
\ge\bigvee_{c\in\mathcal C}c_t\boxtimes c_t.
\tag{P3}
\]
Therefore the fixed-P²-coordinate slice map \(i_s:Y²\to(P\times Y)^2\), restricted to D(Y), factors through D(P×Y). The claimed *closed image* of D(Y) under this slice is
\[
\boxed{(\downarrow s)\times W(Y).}
\tag{P4}
\]
To verify (P4) pointfreely, an open w of the square is a monotone family \(w_v\) of Y²-opens. It misses the image of D(Y) iff its s-section lies below \(e=d_{W(Y)}\), the largest open disjoint from D(Y). The largest monotone open with \(w_s\le e\) is
\[
w_v=\begin{cases}e,&v\le s,\\1,&v\not\le s.\end{cases}
\]
Its closed complement is precisely \((\downarrow s)\times W(Y)\). This checks (P4) as a statement about genuine closed sublocales, not points.

Taking these closed images for all common-lower pairs s and their **finite closed join** yields \(\overline{\mathrm{Cm}(P)}\times W(Y)\). The established finite-coherent identity \(\overline{\mathrm{Cm}(P)}=W(P)=U(P)\) finishes P2. The referee should independently check the frame tensor/monotone-section isomorphism, cover factorization, closed-image computation, and finite closed join.

## 8. The CONNECTED compact strict diamond

Take P to be the five-point fence from (C3). Take Y to be the **connected compact two-apex** locale from §4, with \(K=W(Y)=H(Y)\). Set
\[
Z=P\times Y.
\]
The factors are connected (P because its comparability graph is connected, Y because ℝ is a dense connected subspace); hence Z is **connected**. It is compact, locally compact, sober, T₀, and noncoherent. For noncoherence: a hypothetical compact-open basis would give a nonempty compact-open subset of \(P\times J\) for a bounded real interval J; projecting to Y gives a nonempty compact-open subset inside J, impossible because the real line has no nonempty compact-open subsets.

By P2 and C3,
\[
\boxed{W(Z)=U(P)\times K.}
\tag{Z1}
\]
**Claim Z2 (fitted hull propagation).** In the finite-poset section frame, if \(K\le Y²\) is fitted and a **closed** relation B⊆P² has up-saturation all of P², then
\[
\boxed{\operatorname{fit}_{P²\times Y²}(B\times K)=P²\times K.}
\tag{Z2}
\]
In the application B=U(P), a **closed DOWNSET, not an upset**. Proof: an open w containing B×K has w_s containing K for all s∈B; since sections are monotone and every index lies above some s∈B, all sections contain K. Hence every such w contains P²×K. Conversely P²×K is fitted because K is fitted: if \(K=\bigcap_iO_M(v_i)\), the constant-section open \(\widehat v_i\) in \(\operatorname{Up}(P²,M)\) acts via
\[
(\widehat v_i\to x)_s=v_i\to_M x_s.
\tag{Z3}
\]
Therefore \(P²\times K=\bigcap_i O(\widehat v_i)\). This sectionwise calculation must be verified; do **not** assume arbitrary sublocale meets pull back without proof.

Because U(P) has full up-saturation, \(\operatorname{fit}W(Z)=P²\times K\). The latter is closed as well as fitted, so
\[
\boxed{H(Z)=P²\times K.}
\tag{Z4}
\]
The localic square of Z is spatial (Z locally compact sober), and basic neighborhoods factor. The closed Urysohn relation is thus
\[
\boxed{U(Z)=U(P)\times U(Y).}
\tag{Z5}
\]
Combining Z1, Z4, Z5 gives
\[
\boxed{W(Z)=H(Z)\wedge U(Z).}
\tag{Z6}
\]
There are explicit ordinary-point witnesses:
\[
\begin{aligned}
((m,0),(n,0))&\in H(Z)\setminus U(Z),\\
((k,p_+),(k,p_-))&\in U(Z)\setminus H(Z).
\end{aligned}
\tag{Z7}
\]
Every continuous real-valued map on P and on Y is constant; restricting a continuous map \(Z\to\mathbb R\) to coordinate slices shows \(F(Z)=Z²\). The point \(((m,p_+),(n,p_-))\) is outside both H(Z) and U(Z), hence outside their **finite closed** join. Thus the full working assertion is
\[
\boxed{W(Z)=H(Z)\wedge U(Z)
   <H(Z),U(Z)<H(Z)\vee U(Z)<F(Z)=Z²,}
\tag{Z8}
\]
with H and U incomparable, **on a single connected compact noncoherent locale**.

**Explicit fitted supplement.** Set d=d_W(Z), u=d_U(Z), r=d_H(Z). In the P²-indexed frame of Y²-sections,
\[
 d_s=\begin{cases}d_K,&s\in U(P),\\1,&s\notin U(P),\end{cases}
\qquad
 u_s=\begin{cases}d_{U(Y)},&s\in U(P),\\1,&s\notin U(P),\end{cases}
\qquad r_s=d_K\ (\forall s).
\]
These satisfy \(r\le d\), \(d=u\vee r\), and C(r)=H(Z) fitted, so S1 receives a concrete nontrivial certificate.

## 9. Alternative scattered-factor product (less strong)

If P is finite Alexandrov and A is locally compact sober scattered T₁, one can instead use spatial/scatteredness of \((P\times A)^2\) to get the point-determined formulas
\[
D(P\times A)=\mathrm{Cm}(P)\times\Delta_A,\quad
W(P\times A)=U(P)\times I(A),\quad
U(P\times A)=U(P)\times U(A),\quad
H(P\times A)=H(P)\times I(A).
\tag{R1}
\]
Taking A=the αβγ space produces \(W=H\wedge U\) strictly below H and U in a **product not a disjoint sum**, but that example is disconnected. Claim P2 generalizes the W part of (R1) to **arbitrary** Y; the connected example in §8 is stronger. Please audit (R1) insofar as its reasoning illuminates or challenges P2 or Z2, but prioritize §8.

## 10. Requested independent mathematical focus

Please decide separately:

- Does the two-apex **W=K** and **W=H** proof genuinely handle pointless sublocales?
- Is the finite-branch criterion correct for arbitrary frames with *finite local branch width* and arbitrarily many sectors? Is the coframe identity being used in the right direction?
- Is P2 true for **arbitrary** second-factor locales, and is (P4) the genuine closure of a localic image rather than a point-set argument?
- Does fittedness of P²×K follow from the explicit implication formula (Z3), with no hidden assumption that arbitrary sublocales of Z² are spatial?
- Are compactness, sobriety, connectedness, and noncoherence of Z established rigorously?
- Are C1/C2, the m-apex family M2, fitted-supplement theorem S1, Boolean witness S2, and the stage-reentry warning correct under their stated hypotheses?
- Are any conclusions falsely described as novel or stronger than the existing literature warrants?

**Q and Q′ concerning finite-cover approximations remain OPEN and DEFERRED. Do not treat their resolution as part of this packet.**