# Project A — Noncontinuous Scott dcpo with nonregular Urysohn boundary and strict W<U

**11 November 2026 · NEW INTERNALLY CHECKED construction, not externally refereed or literature-priority checked.** This is a bounded test of the hypothesis in [the continuous-Scott-dcpo theorem](ProjectA_Qprime_continuous_dcpo_OPEN_Cm_regular_U_closed_heredity_2026-11-11.md). We exhibit a **countable noncontinuous dcpo** whose Scott topology is **compact, locally compact, sober, algebraic as a frame, but not coherent**, and whose actual localic relations satisfy
\[
\boxed{\mathcal D=\mathcal D_2,\quad \mathcal W=\mathcal W_2<\mathcal U,\quad
\operatorname{cl}(\operatorname{int}\mathcal U)<\mathcal U.}
\]
Thus the continuous-dcpo conclusion \(W=U\) genuinely fails in a noncontinuous Scott dcpo even when its Scott frame is algebraic; the nonregular Urysohn boundary becomes real. **It is not a Q′ counterexample**: the whole space is compact, so all covers have finite subcovers. The stronger universal Q, Q′ remain OPEN.

## 0. The order

Let \(P\) consist of:
- three incomparable limit elements \(x,y,z\);
- four disjoint increasing countable chains \(x_0<x_1<\cdots\), \(y_0<y_1<\cdots\), \(u_0<u_1<\cdots\), \(v_0<v_1<\cdots\);
- two countable families of incomparable maximal **bridges** \(a_n,b_n\), \(n\in\omega\).

Add order relations
\[
x_n<x,\quad y_n<y,\quad u_n<z,\quad v_n<z,\quad
x_i,u_i\le a_n\ (i\le n),\quad y_i,v_i\le b_n\ (i\le n),
\tag{0.1}
\]
and their transitive consequences; NO other comparisons. The infima of the chains of course are their n=0 elements. In particular there is **no** common lower bound of any element of the \(x,a\)-wing and any element of the \(y,b\)-wing.

Every directed set either has a greatest element or is cofinal in exactly one of the four chains, whose supremum is respectively \(x,y,z,z\). So P is a dcpo. It is NOT continuous at z: both \((u_n)\) and \((v_n)\) are directed with supremum z, and no element is below a member of **both** chains. If p≪z it must be below an element of each chain, impossible. Hence
\[
\boxed{\{p:p\ll z\}=\varnothing.}
\tag{0.2}
\]

## 1. Exact Scott-open basis, compactness, local compactness and sobriety

Put
\[
\begin{aligned}
X_N&=\{x\}\cup\{x_i,a_i:i\ge N\},\\
Y_M&=\{y\}\cup\{y_i,b_i:i\ge M\},\\
Z_{N,M}&=\{z\}\cup\{u_i,a_i:i\ge N\}\cup\{v_i,b_i:i\ge M\}.
\end{aligned}
\tag{1.1}
\]
Together with singleton opens \(\{a_n\},\{b_n\}\), these form a **basis of the Scott topology**. They are upper sets; Scott-inaccessibility follows because the only nontrivial directed suprema are the four chain limits. Conversely any open containing a limit contains sufficiently long tails of its relevant chain(s), forcing the indicated bridge tails by upward closure. A Scott-open containing an intermediate chain point automatically contains its limit and can be refined by the corresponding \(X_N,Y_M,Z_{N,M}\).

**All these basic opens are compact.** For example, an open cover of X_N contains a member covering x, which covers all x_i,a_i for sufficiently large i; finitely many members cover the finitely many remaining points. For Z_N,M choose a member covering z: it contains sufficiently late u- and v-chain points and both bridge tails; again a finite remainder. Singletons are compact. The whole P is compact: choose a cover member at each of x,y,z and then cover finitely many early points.

Therefore \(O_\sigma(P)\) is an **algebraic frame** (compact opens join-generate), and the space is locally compact.

**P is sober (self-contained check).** Both bridge families are unions of open singletons. Let F be nonempty irreducible Scott-closed. If F contains a bridge a_n or b_n, the corresponding singleton is a nonempty open subset of irreducible F and hence dense there; F is exactly its singleton closure. Otherwise F is contained in the closed complement \(B=P\setminus\{a_n,b_n:n\in\omega\}\). The relative topology on B is a **disjoint sum of three clopen components**
\[
B_x=\{x,x_0,x_1,\dots\},\quad
B_y=\{y,y_0,y_1,\dots\},\quad
B_z=\{z,u_0,u_1,\dots,v_0,v_1,\dots\},
\]
as obtained by restricting X_0,Y_0,Z_{0,0}. Irreducibility forces F into one component. The first two are sober Scott chains \(\omega+1\). In B_z, a closed set containing z is all of B_z and is closure of z; a nonempty closed set not containing z consists of finite initial segments of the u/v chains (Scott-closedness prevents unbounded directed chains without their supremum). If both chains occur, basic opens \(Z_{r,s+1}\), \(Z_{r+1,s}\) for their largest retained indices r,s yield disjoint nonempty relatively open subsets of F, contradicting irreducibility. So F is the principal closure of the maximum of exactly one finite initial segment. Every nonempty irreducible closed set thus has a unique generic point. QED.

**Not coherent.** \(X_0,Z_{0,0}\) are compact open, but
\[
X_0\cap Z_{0,0}=\{a_n:n\in\omega\}
\]
is infinite discrete open and **not compact**. So the meet of two compact elements of O(P) is not compact; the algebraic frame is noncoherent.

**Product legitimacy.** P is locally compact and sober, so its **localic square** \(\operatorname{Loc}(P)\times\operatorname{Loc}(P)\) is represented by the ordinary topological square \(P\times P\); rectangles join-generate the product frame. The ensuing open and closed relation comparisons are therefore genuine **localic** assertions, not unsafe identifications for an arbitrary spatial locale.

## 2. A Urysohn-related pair with no common lower-bound approximation

The opens \(X_0,Y_0\) are disjoint, and every pair of points in \(X_0\times Y_0\) has **no common lower bound**. Nevertheless
\[
\boxed{(x,y)\in\operatorname{pt}\mathcal U(P).}
\tag{2.1}
\]
Indeed, for every Scott-open O containing x, some X_N⊆O. For EVERY Scott neighborhood \(Z_{K,L}\) of z, choose i≥max(N,K); the bridge a_i lies in \(X_N\cap Z_{K,L}\). Hence z∈cl(O). Symmetrically z∈cl(O') for every O' containing y, using b_i. Therefore every pair of Scott neighborhoods of x,y has intersecting closures at z, which is precisely the condition of belonging to the **closed Urysohn relation**.

By contrast, the open sets
\[
A=\{a_n:n\in\omega\}\subseteq X_0,\qquad
B=\{b_n:n\in\omega\}\subseteq Y_0
\]
are each dense in their respective wings. Every \(\{a_i\},\{b_j\}\) pair is **far**, because
\[
\overline{\{a_i\}}=\downarrow a_i
=\{a_i\}\cup\{x_k,u_k:k\le i\},\quad
\overline{\{b_j\}}=\downarrow b_j
=\{b_j\}\cup\{y_k,v_k:k\le j\},
\]
which are disjoint. Hence
\[
A\boxtimes B\le d_\mathcal U.
\tag{2.2}
\]
Since A×B is a dense OPEN subset of X_0×Y_0, the far-rectangle open \(d_\mathcal U\) is **dense on the mixed wing square**. Thus \(\operatorname{int}\mathcal U\) is disjoint from \(\mathfrak o(X_0\boxtimes Y_0)\), and its closure remains disjoint from that open. But (x,y) lies in U and in X_0×Y_0. Therefore
\[
\boxed{\operatorname{cl}(\operatorname{int}\mathcal U)<\mathcal U.}
\tag{2.3}
\]
This is the precise failure of the continuity-dcpo argument: at z there is no Scott-open cone controlled by one lower predecessor; independent Scott-convergent u- and v-chains force simultaneous accumulation of the two isolated bridge wings, despite the total absence of cross-wing common lower bounds.

## 3. Stronger: D vanishes on the entire mixed wing square

For n∈ω, consider the **finite Scott-open cover**
\[
\boxed{
\mathcal F_n=\{X_0,\ Y_0,\ Z_{0,n},\ Z_{n,0}\}.
}
\tag{3.1}
\]
It covers every point: X_0 covers the x-chain and all a-bridges, Y_0 covers the y-chain and all b-bridges, Z_{0,n} covers **all u-chain points**, and Z_{n,0} covers **all v-chain points**; both contain z.

Let \(A_{\ge n}=\{a_i:i\ge n\}\), \(B_{\ge n}=\{b_i:i\ge n\}\). Restrict the corresponding finite diagonal-cover open \(w_{\mathcal F_n}\) to the mixed rectangle \(X_0\boxtimes Y_0\). The X_0- and Y_0-squares contribute nothing there; the remaining squares give exactly
\[
\boxed{
w_{\mathcal F_n}\wedge(X_0\boxtimes Y_0)
=(A\boxtimes B_{\ge n})\vee(A_{\ge n}\boxtimes B).
}
\tag{3.2}
\]
Every term lies in the **open discrete** product sublocale A×B. Since A×B is discrete, \(\mathcal O(A\times B)=\mathcal P(\omega\times\omega)\), and open sublocales on it are just ordinary subsets. The trace of (3.2) on A×B is
\[
E_n=\{(i,j)\in\omega^2:i\ge n\text{ or }j\ge n\},
\quad \bigcap_{n\in\omega}E_n=\varnothing.
\tag{3.3}
\]
Thus the **sublocale meet** of the \(\mathfrak o(w_{\mathcal F_n})\), restricted to \(X_0\times Y_0\), is ZERO: already the n=0 open restricts the meet to the discrete A×B, and there the descending family of E_n has empty intersection. Since the full D is contained in every finite-cover square open,
\[
\boxed{\mathcal D(P)\wedge\mathfrak o(X_0\boxtimes Y_0)=0.}
\tag{3.4}
\]
In fact the **finite-cover fitted diagonal** D₂ is already zero on this mixed rectangle, by exactly the same finite covers.

Closure cannot meet a nonempty OPEN sublocale where the original sublocale is zero. Hence
\[
\boxed{\mathcal W(P)\wedge\mathfrak o(X_0\boxtimes Y_0)=0.}
\tag{3.5}
\]
In particular (x,y), which lies in U by §2, does not lie in W. Therefore
\[
\boxed{\mathcal W(P)<\mathcal U(P).}
\tag{3.6}
\]

Because P is compact, EVERY open cover has a finite subcover. Consequently the full and finite diagonal-cover meets coincide:
\[
\boxed{\mathcal D(P)=\mathcal D_2(P),\qquad
\mathcal W(P)=\mathcal W_2(P)<\mathcal U(P).}
\tag{3.7}
\]
So this is not a Q′ counterexample. It is a decisive **boundary control**: a noncontinuous Scott dcpo with an actual nonregular, non-fitted Urysohn boundary that stays outside W, in sharp contrast to the continuous-dcpo collapse W=U.

## 4. Finite truncation checks

For N=2,4,8 we independently enumerated the finite order truncations (respectively 21,33,57 elements) and checked:
- there is no common lower bound between any X_0-element and any Y_0-element;
- each \(\mathcal F_n\) covers the truncated poset for n≤N;
- the mixed-square trace of \(w_{\mathcal F_n}\) is exactly \(E_n\) in (3.3), with respective cardinality \((N+1)^2-n^2\).

These are combinatorial checks of (3.2), **not** numerical verifications of the infinite Scott-localic sublocale conclusion. The latter follows from the exact infinite discrete meet calculation in §3. The finite truncations are Alexandrov/continuous, so each has W=U by the older general Alexandrov theorem; the limit topology loses cone neighborhoods at z and produces the strict W<U defect. Do not infer this is a domain-theoretic inverse limit preservation counterexample without verifying bonding maps.

## 5. Research implications

1. **Continuity is substantively used.** The preceding theorem that continuous Scott dcpos have U=cl(common-lower open)=W=W₂ does NOT extend to arbitrary Scott dcpos, even if their Scott-open **frame** is algebraic and their Scott space compact, sober and locally compact.
2. **A truly nonregular U boundary now exists inside a Scott locale.** It is the mixed wing square X_0×Y_0: U contains the ordinary pair (x,y), but this entire open square has no fitted-diagonal sublocale D or finite approximation D₂.
3. **No Q′ failure:** compactness eliminates infinitary cover gaps. The next sensible problem is whether one can replace the compactness mechanism by a noncompact tail or couple this nonregular U boundary to an independent infinitary \(\mathcal D_2>\mathcal D\) defect in the **same** mixed rectangle, without rescue by regular/hyperconnected strips. The earlier closed-remainder self-reduction warns that merely adjoining an unrelated pathology will not work.
4. **Related literature:** Johnstone's 1981 non-sober Scott dcpo and later noncontinuous-domain examples show that discontinuous Scott spaces can be subtle. This particular countable compact sober construction has a separately supplied sobriety proof and should not be called an instance of Johnstone's nonsober example. See Dongsheng Zhao (2025), “Johnstone's Non-Sober Dcpo and Extensions,” International Journal of Topology 2(1), article 3 (DOI 10.3390/ijt2010003). No literature priority checked for the present construction.

**Status: NEW INTERNAL working proof, not externally audited.** Especially audit the Scott-open compact basis, sobriety classification, the localic product=ordinary product justification, and the discrete-sublocale infinite meet in §3 before promotion. Q and Q′ remain OPEN.
