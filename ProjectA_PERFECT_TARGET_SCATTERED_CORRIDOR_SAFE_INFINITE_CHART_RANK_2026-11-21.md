# Project A — perfect target, infinite chart rank, yet associative graph adjunction
## 21 November 2026 · NEW INTERNAL theorem and proof; independent audit outstanding

**Provenance.** This note follows the [independently reviewed rectangular rule (RC)](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), the [independently reviewed finite-exception graph-membership addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md), and the [internally derived scattered relation-algebra example](ProjectA_SCATTERED_RELATION_ALGEBRA_FINITE_TO_ONE_NECESSITY_COUNTEREXAMPLE_2026-11-21.md). It **refutes even the perfect-target, uniformly two-to-one version** of finite chart rank necessity, by proving **full safe adjunction**, not only the earlier NR graph-probe condition. The new ingredient is a closed-scattered **fiber decomposition** and an explicit **15-element partial-relation semigroup**. All new statements here need an independent adversarial audit before canonical promotion; no priority claim.

**Convention.** For compact Hausdorff spatial G and ordinary A,B⊆G,
\[
p(A,B)=[A\times B]_{G^2},\quad q(A,B)=[A]_G\times_{\mathrm{Loc}}[B]_G.
\]
Localic composition is genuine pullback followed by localic image, read from left to right. The independently reviewed (RC) says a product of any two p/q rectangles equals the full q outer rectangle when the middle induced supports overlap nontrivially, and zero otherwise. The displayed outer q may itself be zero for empty outer support.

## 1. Atomic decomposition over a closed scattered coordinate

**Lemma 1.1 (SCATTERED-FIBER, NEW INTERNAL).** If Z is compact Hausdorff and K is compact **scattered Hausdorff**, then every sublocale \(W\le Z\times_{\mathrm{Loc}}K\) satisfies
\[
\boxed{
W=\bigvee_{k\in K} \bigl(W\wedge(Z\times\{k\})\bigr).
}\tag{SF}
\]
For each k, regard its fiber as a sublocale of Z×K through the closed embedding Z×{k}.

**Proof.** Let J denote the join of the right-hand fibers. Clearly J≤W. Suppose W≰J. Since the compact Hausdorff ambient locale Z×K is **regular, hence fit**, there is an ambient open sublocale O such that J≤O and W≰O. Let F be its closed complement. Finite distributivity of the sublocale lattice gives \(W'=W\wedge F\ne0\). Let L be the least ambient closed support of W'. Then L is nonempty compact Hausdorff, W' is dense in L, and the projection \(P=\pi_K(L)\) is a nonempty compact closed subset of K.

Scatteredness of K supplies a point k isolated in P. Choose a K-open neighborhood V of k with V∩P={k}. The open sublocale \((Z\times V)\cap L\) is nonzero (it contains an ordinary point) and therefore meets the dense W' nontrivially. Yet the resulting nonzero sublocale W'∧(Z×V) is supported in \(Z\times\{k\}\), because L projects into P. Thus
\[
0\ne W'\wedge(Z\times V)\le W\wedge(Z\times\{k\})\wedge F\le J\wedge F=0,
\]
contradiction. □

**Corollary 1.2.** For any ordinary B⊆K and any sublocale A≤Z,
\[
\boxed{A\times_{\rm Loc}[B]=\bigvee_{k\in B}(A\times\{k\}).}\tag{SFq}
\]
Indeed the k-fiber of the left side is A×{k} if k∈B and 0 otherwise; all sublocales of K are induced by ordinary subsets (Simmons/Picado–Pultr), so \([B]\wedge\{k\}\) is pointwise. In particular, a compact scattered coordinate is a **fiberwise atomic multiplier even for nonspatial A**.

**Caution:** This is a statement about **sublocales** of Z×K, not that the locale K is topologically discrete. The equality in (SF) is an *arbitrary localic join*, and its proof uses fit/closed-support separation rather than an invalid arbitrary-meet/join exchange.

## 2. A pseudo-bijection between discrete and scattered subspaces

Let G be compact Hausdorff. Suppose U⊆G is **open discrete**, K⊆G is **closed scattered**, U∩K=∅, and \(b:U\to K\) is an ordinary bijection, continuous since U is discrete. Write \(\beta\le G^2\) for the point-generated graph of b, and \(\beta^\smile\) for its converse. b need not be a homeomorphism: K may be a nondiscrete countable compact ordinal space.

**Lemma 2.1 (PSEUDO-ACTIONS).** For any ordinary A,B⊆G and t∈{p,q},
\[
\boxed{
\begin{aligned}
t(A,B)\circ\beta&=t(A,b(B\cap U)),\\
\beta\circ t(A,B)&=t(b^{-1}(A\cap K),B),\\
t(A,B)\circ\beta^\smile&=t(A,b^{-1}(B\cap K)),\\
\beta^\smile\circ t(A,B)&=t(b(A\cap U),B).
\end{aligned}}\tag{PB}
\]

**Proof.** For p, restriction to either U (open) or K (closed) is exactly the ordinary induced spatial restriction, and every relevant source with a discrete U coordinate is point-determined. Images of point-generated spatial sublocales are the induced sublocales of the ordinary images, giving the p formulas. For q, use \([B]\wedge U=[B\cap U]\) and \([B]\wedge K=[B\cap K]\), then compute the actual product pullbacks. The U coordinate is discrete, so the localic product with U splits into a coproduct of its point fibers. Its image under \(id\times b\) is the join \(\bigvee_{u\in B\cap U}[A]\times\{b(u)\}\), which is **the whole** q(A,b(B∩U)) by (SFq), not merely its point-generated sublocale. The other three formulas are the analogous first/second coordinate arguments, using that K is scattered (so preimages of sublocales from K to discrete U are point-determined). □

**Lemma 2.2 (PSEUDO-INVERSE and OVERLAP).**
\[
\boxed{\beta\circ\beta^\smile=\Delta_U,\qquad
\beta^\smile\circ\beta=\Delta_K.}\tag{PI}
\]
The first composability locale lies in U×U, which is discrete, and bijectivity forces the ordinary diagonal. The second composition passes through U discrete and is the point-generated image of the ordinary diagonal of K; since K is spatial scattered, this is the genuine closed diagonal \(\Delta_K\).

For all ordinary B,C⊆G,
\[
\boxed{
[b(B\cap U)]\wedge[C]\ne0
\iff
[B]\wedge[b^{-1}(C\cap K)]\ne0.
}\tag{OT}
\]
Indeed the left meet is supported in the closed scattered K and hence is point-determined; the right meet is supported in open discrete U and likewise point-determined. Both assert that there exists \(u\in B\cap U\) with \(b(u)\in C\). The converse orientation obeys the same criterion. This is the exact RHR test used in the referee's prior graph-algebra proof, without requiring b^-1 to be continuous.

## 3. A two-to-one compact metric map onto PERFECT Cantor space

Let \(C=2^{\mathbb N}\), and choose a **closed scattered** copy
\[
K\subset C,\quad K\cong[0,\omega^\omega]
\]
(countable compact metrizable zero-dimensional scattered; standard embedding into Cantor space). Enumerate K without repetition as \(K=\{k_n:n\ge1\}\). Let
\[
S=\{0\}\cup\{1/n:n\ge1\},\quad
X=(C\times\{0\})\cup\{(k_n,1/n):n\ge1\}\subseteq C\times S,
\quad f(x,t)=x.
\tag{X}
\]
Then X is **closed** in compact metric C×S: any infinite upper-sheet limit has height 0, where all base points are present. Thus X is compact metrizable Hausdorff. Its **base** \(B=C\times\{0\}\) is closed and homeomorphic to C; its **upper discrete part** \(U=X\setminus B=\{(k_n,1/n)\}\) is open discrete. The map f is surjective and proper, with
\[
|f^{-1}(y)|=2\quad(y\in K),\qquad
|f^{-1}(y)|=1\quad(y\notin K).
\tag{FIB}
\]
It is not open: the upper singleton \(\{(k_n,1/n)\}\) is open in X but has singleton image \(\{k_n\}\), not open in perfect C.

**Proposition 3.1 (infinite chart rank).** \(\rho_{\rm lc}(f)=\infty\), even if "locally closed" is dropped from the permitted chart domains. Indeed if finitely many homeomorphic partial charts covered X, their intersections with the upper discrete U would map homeomorphically onto finitely many **discrete ordinary subsets of K** whose union is K. A T1 space covered by m discrete subsets has empty m-th Cantor–Bendixson derivative (proved in the [earlier scattered note](ProjectA_SCATTERED_RELATION_ALGEBRA_FINITE_TO_ONE_NECESSITY_COUNTEREXAMPLE_2026-11-21.md)); but K≅[0,ω^ω] has a nonempty derivative at every finite stage. Contradiction.

**Proposition 3.2 (ALL NR PROBES PASS; selected-support Frobenius).** For every ordinary E⊆X and A⊆C,
\[
\boxed{\mathrm{im}\bigl([E]\wedge f^{-1}([A])\bigr)
=[f(E)]\wedge[A].}\tag{FF}
\]
Here f^-1 denotes genuine localic inverse image of sublocales, and im is image of the resulting sublocale into C.

**Proof.** Decompose E=E_0∪E_1 into base and upper points. The induced sublocale [E]=[E_0]∨[E_1]. Image, and meet with [A] against a **finite** join, preserve the respective finite joins. On E_0, f is a homeomorphism onto C, so the equality holds for arbitrary induced A (including a pointless intersection). On E_1, the source is discrete and f(E_1)⊂K; the pullback is precisely the discrete set of selected points mapping into A. Its image is [f(E_1)∩A]. On the target the meet [f(E_1)]∧[A] is supported in the closed scattered K, so equals exactly [f(E_1)∩A]. Join the two cases. □

Thus the necessary graph probe condition NR holds for **all** ordinary E,A, despite f having infinite chart rank over a perfect target. However (FF) alone is not used as a substitute for the associativity proof below.

## 4. Finite graph semigroup and FULL SAFE ADJUNCTION

Put \(G=X\amalg C_Y\), where \(C_Y\) is a separate copy of Cantor C. Denote its closed base copy of C in X by B, and the closed copies of K in B and C_Y by \(K_B,K_Y\). Let \(h:B\to C_Y\) be the canonical homeomorphism, and \(g:U\to K_Y\) the bijective enumeration projection. Put \(b=h^{-1}\circ g:U\to K_B\) and \(t=h|_{K_B}:K_B\to K_Y\).

The point-generated localic graph of f is the **finite join**
\[
\boxed{\Gamma_f=\Gamma_h\vee\Gamma_g,}\tag{GD}
\]
and its converse is \(\Gamma_h^\smile\vee\Gamma_g^\smile\).

**Lemma 4.1 (15-element graph semigroup).** Let \(\mathcal H\) be the following 15 individual sublocale relations on G:
- Zero and the full identity: \(0,\Delta_G\).
- Five partial identities: \(\Delta_B,\Delta_{C_Y},\Delta_U,\Delta_{K_B},\Delta_{K_Y}\).
- Eight oriented partial bijections: \(\Gamma_h,\Gamma_h^\smile,\Gamma_t,\Gamma_t^\smile,\Gamma_g,\Gamma_g^\smile,\Gamma_b,\Gamma_b^\smile\).

Then \(\mathcal H\) is closed under localic relational composition and converse. Each product of two elements equals the point-generated graph of their **ordinary partial-bijection composite**, or zero. Composition on \(\mathcal H\) is associative.

**Proof.** At the set level this is a finite inverse semigroup of partial bijections generated by h and g, with domains/ranges on three disjoint sectors B, C_Y, U and distinguished closed sectors K_B,K_Y. Restriction to K is the only possible new nontrivial domain condition; composing again only yields the listed maps/partial identities. The 15 displayed partial maps are closed under ordinary partial composition (a finite direct check).

For *localic* products: compositions involving only h,t and the listed partial identities are actual compositions of locally closed partial homeomorphism graphs, hence their point-generated graphs. Any remaining nonzero composite has a g or g^smile factor. If its composability object is pulled through h or t (an isomorphism), it reduces to U discrete or to a closed scattered K sector. If two pseudo arrows are composed, their composability locale lies in products of U and/or closed scattered K sectors; these are scattered Hausdorff, so the Simmons/Picado–Pultr point-determination theorem eliminates extra pointless composability. Thus the localic result is the point-generated ordinary partial composite, one of the listed 15. The multiplication agrees with the ordinary associative partial-bijection semigroup. □

**Theorem 4.2 (MAIN NEW INTERNAL POSITIVE RESULT).** The class \(\mathcal A^\ast(G)\) of **finite joins** of the 15 semigroup relations in \(\mathcal H\) and all point-generated/full rectangular generators p(A,B),q(A,B) is closed under genuine localic relation composition and converse, is **associative**, and contains the identity Δ_G. In particular **Γ_f and Γ_f^smile can be adjoined safely to the full compact-Hausdorff rectangular algebra**, despite f being (at most) two-to-one with infinite locally closed chart rank and perfect target.

**Proof.** The binary multiplication table is closed:
- Rectangular×rectangular products are 0 or q rectangles by the independently reviewed **(RC)**.
- \(\mathcal H\)×\(\mathcal H\) stays in \(\mathcal H\) by Lemma 4.1.
- Rectangular×\(\mathcal H\) and \(\mathcal H\)×rectangular products remain the **same p/q rectangle type** (possibly zero). For genuine locally closed partial homeomorphism arrows h,t, and partial identities, use the independently checked **(PH)** action. For the pseudo arrows g,b and their converses use (PB), relying crucially on (SF).

To verify associativity of individual generators, consider the eight R/H three-letter types:
- RRR: the same outer q(A,D) if both middle overlaps are nonzero, zero otherwise; allow q=0 for empty endpoints.
- HHH: multiplication in the finite partial-bijection semigroup is associative (Lemma 4.1).
- RRH, HRR: one middle rectangular overlap controls the outcome; graph action only restricts/reindexes an outer endpoint.
- RHH, HHR: successive graph actions on a rectangle equal the action of the ordinary composed partial bijection, since (PH)/(PB) transport endpoint subsets by the exact setwise maps (and Lemma 4.1 computes their graph composite).
- HRH: independent restrictions of first and second outer supports commute.
- **RHR:** The two overlap tests are transported by the middle partial bijection. For a genuine locally closed partial homeomorphism, this is the already audited localic overlap-transport identity. For a pseudo-bijection, this is (OT): the relevant meets live in open discrete U or closed scattered K and are therefore **point-determined**. Thus the tests agree, and both bracketings give the same outer q rectangle, possibly zero.

These exhaust all cases. Genuine localic composition distributes over **finite** joins in the two arguments (the same finite-join result used and independently checked in the rectangular and locally-closed chart audits), so triple-generator associativity extends to arbitrary finite joins. Converse preserves generators and exchanges their orientations. Δ_G is a two-sided unit. By (GD), Γ_f,Γ_f^smile lie in this associative algebra, proving safe adjunction. □

**Strong conclusion (NEW INTERNAL).**
\[
\boxed{
\begin{gathered}
Y=C\ \text{perfect compact metric},\\
1\le |f^{-1}(y)|\le2,\qquad \rho_{\rm lc}(f)=\infty,\\
\Gamma_f\notin\mathcal A_{\rm lc}(X\amalg Y)\quad\text{(referee's finite-to-one membership criterion)},\\
\Gamma_f,\Gamma_f^\smile\ \text{adjoin associatively to the ENTIRE rectangular calculus}.
\end{gathered}}\tag{PERF}
\]
This **refutes perfect-target finite-to-one necessity** for the known chart algebra, if the new internal Theorem 4.2 withstands independent review. It does **not** claim that all relations on G associate; G contains a perfect Cantor component, and arbitrary localic relations may still be nonassociative.

### 5. Mathematical implications and audit priorities

1. **New positive mechanism:** an open discrete sector can be paired by a set-bijection with a **closed scattered sector**. It acts on full localic rectangles via the scattered-fiber decomposition (SF), even when its inverse is not continuous. This extends beyond the earlier locally closed *homeomorphism* chart calculus.
2. **Safety is strictly broader than finite graph-chart membership**, even with **uniform fiber degree two and perfect target**. The true boundary involves which partial correlations are point-determined *where the relevant pullbacks occur*, not global fiber count, openness, or chart rank alone.
3. **NR remains weaker than safety as a theorem:** our example satisfies a strong Frobenius equality (FF) and is separately proven safe by the semigroup method. No universal sufficiency of NR is asserted.
4. **Audit the NEW dependencies** (SF, PB, PI, 15-element graph semigroup multiplication, RHR transport, and finite-join extension) adversarially. The earlier independently reviewed RC, PH and finite-to-one membership theorem are imported, not silently re-proved.
5. **Big-picture target after this boundary:** formulate a *stable witness calculus* that encompasses locally closed homeomorphic charts, closed-scattered pseudo-bijections, and constant rectangular fibers; then return to the intrinsic specialization graph and Cameron–Kumar/Dowker complexes, treating imposed Stone graph examples as algebraic test cases rather than intrinsically topological separation graphs.

**Audit status:** New internal theorem. It requires a careful independent audit before being promoted from candidate to canonically established result.
