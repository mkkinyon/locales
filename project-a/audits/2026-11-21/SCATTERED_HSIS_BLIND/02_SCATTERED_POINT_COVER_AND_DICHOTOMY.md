# Candidate A — scattered point covers and a compact-Hausdorff target dichotomy

## A.1. Setup and the discrete point cover

Work in classical locales. If Y is a sober spatial locale, its *canonical discrete point cover* is

\[
p_Y:\coprod_{y\in Y}1_y\longrightarrow Y,
\]

sending the copy 1_y to the ordinary point y. It is point-surjective by construction, and hence surjective because Y is spatial. The question is whether it is **pullback-stably** surjective: for every locale map h:T→Y, including when T has no points, is \(\coprod_y(T\times_Y\{y\})\to T\) a surjection?

### Lemma A.1: spatial base changes of a point-surjective map

Let e:S→V be point-surjective with V spatial. If h:T→V has spatial T, then S×_V T→T is point-surjective, and therefore a locale-surjection. For every t∈T, choose a point s∈S mapping to h(t); the pair (s,t) supplies a point in the localic pullback over t. Thus **any failure of universal stability must use a nonspatial base-change target**.

## A.2. Scattered targets

A topological space Y is *scattered* when every nonempty subspace has an isolated point. Assume Y is sober and scattered. Define the Cantor–Bendixson sequence:

\[
Y^{(0)}=Y,\quad
Y^{(\alpha+1)}=\bigl(Y^{(\alpha)}\bigr)',\quad
Y^{(\lambda)}=\bigcap_{\alpha<\lambda}Y^{(\alpha)}.
\]

Here prime denotes removing points isolated in the current subspace. The Y^(α) are closed, U_α=Y\Y^(α) are open, and each successor layer L_α=Y^(α)\Y^(α+1) is a **discrete subspace**, closed **relative to U_(α+1)**. At some ordinal γ, Y^(γ)=∅.

**Theorem A.2 (scattered-point-cover stability).** For scattered sober Y, p_Y is pullback-stably surjective. Hence any locale map e:S→Y surjective on ordinary points is pullback-stably surjective.

**Proof.** Fix arbitrary h:T→Y with T not assumed spatial. Let T_y=T×_Y{y}≤T and J=∨_{y∈Y}T_y. We prove h^{-1}(U_α)≤J by transfinite induction. At α=0, U_0=∅. At a successor stage, inside the pulled-back open sublocale h^{-1}(U_(α+1)), the open part h^{-1}(U_α) and its complementary closed part h^{-1}(L_α) form a finite open/closed cover. The first is ≤J by induction. Since L_α is spatial discrete, its pullback h^{-1}(L_α) decomposes, by extensivity of Loc over a coproduct, as \(\coprod_{y\in L_\alpha}T_y\), whose image is ≤J. Hence all of h^{-1}(U_(α+1)) is ≤J. At a limit λ, the increasing opens satisfy U_λ=∪_{α<λ}U_α; inverse-image on **opens** preserves the arbitrary join, giving h^{-1}(U_λ)≤J. As U_γ=Y, we obtain J=T. This proves stability of p_Y for arbitrary T.

If e:S→Y is point-surjective, choose a point s_y∈S above each y (classical choice). The family (s_y) determines a map p_Y→S over Y. It remains a factor under any base change, and p_Y is stably surjective, so e is stably surjective too. ∎

**Question for the referee:** Are the relative closed-layer and limit steps correct for arbitrary locales T, including nonspatial ones? Is soberness or another separation hypothesis needed beyond the stated one?

## A.3. Converse in Hausdorff spaces

For a locale K, denote by \(\mathcal B(K)\) its least dense / double-negation sublocale. If K is a nonempty Hausdorff space without isolated points, \(\mathcal B(K)\ne0\) and it has **no ordinary points**: each K\{k} is open dense, so it contains \(\mathcal B(K)\), excluding the point k.

**Theorem A.3 (point-cover characterization).** For a Hausdorff topological space Y the following are equivalent:

1. Y is scattered;
2. p_Y:Y_discrete→Y is pullback-stably surjective;
3. every point-surjective locale map S→Y is pullback-stably surjective.

**Proof.** (1)⇒(3) is A.2; (3)⇒(2) is immediate. If Y is non-scattered, choose a nonempty subspace A without isolated points and let K=cl_Y A. K is nonempty, closed and has no isolated points: if k∈K were isolated in K, its singleton relative open would meet the dense A in an isolated A-point. Hence \(\mathcal B(K)\ne0\) is pointless. Pull p_Y back along the sublocale embedding \(\mathcal B(K)\hookrightarrow K\hookrightarrow Y\). Since the discrete source is a coproduct of singleton points and \(\mathcal B(K)\) has none, every point fiber is zero; the pulled-back source is 0, not a surjection onto \(\mathcal B(K)\). Thus (2) fails. ∎

**Literature caution:** This is closely related to Simmons' theorem identifying scatteredness with a correspondence between topological subspaces and localic sublocales. The present formulation is about the stability of a canonical point cover, not an asserted new priority result.

## A.4. Selected-image consequence

For any continuous f:X→Y and ordinary E⊆X write D=f(E), with [E]_X and [D]_Y the point-generated induced spatial sublocales. The induced map e_E:[E]→[D] hits every ordinary point of [D]. If Y is scattered Hausdorff then so is D, and A.2 yields

\[
\boxed{\forall E\subseteq X,\quad e_E:[E]\to[f(E)]\text{ is pullback-stably surjective}.}\tag{HSIS}
\]

This selected-image property is the hypothesis of **Candidate B** in file 03. Its implication for the generated rectangular algebra must be evaluated independently of the point-cover proof.

## A.5. Universal compact-Hausdorff graph-safety

Let G=X⊔Y, with X,Y compact Hausdorff. Let \(p(A,B)=[A\times B]\) and \(q(A,B)=[A]\times_{\mathrm{Loc}}[B]\) for ordinary subsets A,B⊆G. Denote by \(\mathscr A_f(G)\) the smallest family of sublocales of G² containing every p/q rectangle, Γ_f and its converse, and Δ_G, and closed under **finite** joins and relation composition.

Define Y *universally graph-safe* when \(\mathscr A_f(G)\) is associative for **every continuous surjection f:X→Y from compact Hausdorff X**. Define Y *universally projection-safe* when this holds for every compact Hausdorff auxiliary Z and f=pr_Y:Y×Z→Y.

**Theorem A.5 (compact-Hausdorff target dichotomy, DEPENDENT ON B).** For compact Hausdorff Y:

\[
\boxed{Y\text{ scattered}\iff Y\text{ universally graph-safe}\iff Y\text{ universally projection-safe}.}\tag{UT}
\]

**Proof of positive implication.** If Y scattered, the selected-image maps e_E for every f:X→Y are pullback-stably surjective by A.4. Candidate B says that this implies associativity of the enlarged rectangular algebra. This is the ONLY place in the target dichotomy using the new graph-extension theorem.

**Proof of negative implication.** Suppose Y is non-scattered. Choose nonempty compact **perfect closed** K⊂Y. Use the classical resolvability theorem (crowded compact Hausdorff K admits disjoint ordinary dense Q,I⊂K). Set Z=β(Q_discrete), the Stone–Čech compactification of the underlying discrete set Q. Put X=Y×Z, f=pr_Y:X→Y. The map is continuous, **open, proper and surjective**.

For each q∈Q, regard the same symbol q as an isolated point of Z. Define E={(q,q):q∈Q}⊂X. The second coordinate isolates each element, so [E] is a **discrete locale**, and its localic image under f is [Q]. By density of Q,I in K,

\[
0\ne\mathcal B(K)\le [Q]_Y\wedge[I]_Y.
\]

By contrast, [E]×_Y[I]=0: the source is a coproduct of points indexed by E, and each such point maps to q∉I; since Y is Hausdorff, [I]≤Y\{q}, so each pullback point fiber is zero.

Choose ordinary marker points u∈Y and v∈X, so **the ambient remains exactly G=X⊔Y as stipulated in the definition of universal safety**. (Fresh disjoint markers may be added for visual clarity, but are unnecessary.) Put

\[
R=\{u\}\times[I],\quad F=\Gamma_f^{\smile}:Y\to X,\quad T=[E]\times\{v\}.
\]

The actual composability pullback gives

\[
(R\circ F)\circ T=0,\qquad R\circ(F\circ T)=\{(u,v)\}\ne0.
\]

The second identity uses F∘T=[Q]×{v} and the (point-generated/full) rectangle rule with pointless nonzero middle [I]∧[Q]. Hence the graph algebra for this **open proper projection** is nonassociative. The independent factor types R⊂Y×Y, F⊂Y×X and T⊂X×X ensure that these calculations involve no other sectors. No enlargement of G is used in the universal-safety contradiction.

For metric compact Y, choose a countable dense/co-dense split of perfect K and take Z=Cantor with a discrete sequence of Z-points, avoiding Stone–Čech and the nonmetric resolvability theorem. ∎

**Referee dependency warning:** If Candidate B is incorrect, A.2 and A.3 may still be valid; the proof of the positive implication of A.5 then needs repair. The negative implication does not rely on Candidate B beyond the baseline rectangular rule.