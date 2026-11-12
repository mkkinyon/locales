# Project A — Q′ noncompactification of bridge dcpo: exact W/W₂/U transfer and coexisting uncoupled defects

**11 November 2026 · NEW INTERNAL working theorem + adversarial test; NOT externally audited, no literature priority claim.** This is the bounded continuation requested after the [compact noncontinuous three-limit/two-bridge Scott example](ProjectA_Qprime_noncontinuous_Scott_THREE_LIMIT_BRIDGES_strict_WU_2026-11-11.md). It shows why the most natural noncompactification fails to turn that \(\mathcal W<\mathcal U\) boundary into a strict \(\mathcal W<\mathcal W_2\) gap: product with a Scott space having a dense common-predecessor relation **transfers both closed diagonal hulls exactly**, without changing their difference. A completed-branching factor introduces an actual \(\mathcal D<\mathcal D_2\) defect while preserving \(\mathcal W=\mathcal W_2<\mathcal U\). The resulting **connected noncompact noncontinuous Scott dcpo** has \(h_{\rm hc}=h_{\rm cc}=0\) and a cover with \(t_{\mathcal C}=0\). Thus many necessary Q′ diagnostics coexist, but the defect still cannot reach the mixed bridge rectangle. Q and Q′ are **OPEN in general**.

## 0. Conventions, inputs, topological domain

For a locale X, and a cover C of O(X), let \(w_C=\bigvee_{c\in C} c\boxtimes c\). The full fitted diagonal and its finite-cover approximation are
\[
\mathcal D(X)=\bigwedge_{C\text{ cover}}\mathfrak o(w_C),\qquad
\mathcal D_2(X)=\bigwedge_{F\text{ finite cover}}\mathfrak o(w_F),
\]
and \(\mathcal W(X)=\operatorname{cl}\mathcal D(X)\), \(\mathcal W_2(X)=\operatorname{cl}\mathcal D_2(X)\).

For any topological \(S\), in its specialization order (opens are upsets), define
\[
C_S=\{(s,t)\in S^2:\exists p\in S,\ p\le s,t\}.
\tag{0.1}
\]
Call \(S\) **common-predecessor dense** when \(C_S\) is dense in the ordinary product \(S^2\). This means every pair of nonempty S-opens contains a pair with a common lower specialization point, but does NOT require S to be hyperconnected or directed.

All theorem factors below are **locally compact sober spaces**. Their ordinary topological products compute localic products, so the closed localic relations and frame-coproduct calculations are legitimate. This is the classical locally compact sober product fact; the argument does NOT assume that arbitrary spatial locales have spatial localic products.

## 1. Naturality upper bounds: old finite covers persist under projection

**Lemma 1.1 (lax covariant containment).** For any locale map \(f:X\to B\) and \(\varepsilon\in\{\mathrm{full},2\}\),
\[
\mathcal D_\varepsilon(X)\le(f\times f)^{-1}\mathcal D_\varepsilon(B),
\qquad
\mathcal W_\varepsilon(X)\le(f\times f)^{-1}\mathcal W_\varepsilon(B).
\tag{1.1}
\]
*Proof.* Every (finite, respectively arbitrary) B-cover C pulls back to a cover \(f^*C\) of X with \(w_{f^*C}=(f\times f)^*w_C\). Thus \(\mathcal D_\varepsilon(X)\) is below the inverse image of every B square-cover open. Pullback preserves arbitrary meets of sublocales, giving the first inclusion. The inverse image of the **closed** sublocale \(\mathcal W_\varepsilon(B)\) is closed and contains the first sublocale, so its containment of the closure gives the second. QED.

For \(X=B\times S\), \(f=\pi_B\), this gives
\[
\boxed{\mathcal W(B\times S)\le\mathcal W(B)\times S^2,\quad
\mathcal W_2(B\times S)\le\mathcal W_2(B)\times S^2.}
\tag{1.2}
\]
**No-go meaning.** If \(\mathcal W_2(B)\wedge\mathfrak o(a\boxtimes b)=0\), then the inverse-image strip \((a\times S)\boxtimes(b\times S)\) is already disjoint from \(\mathcal W_2(B\times S)\). Hence **any fibered gluing with a continuous projection back to B retaining this mixed wing rectangle** inherits the finite-cover exclusion. Enlarging fibers alone cannot produce a \(Q'\) witness on that rectangle.

## 2. Main exact transfer theorem

**Theorem 2.1 (dense-common-predecessor stabilization).** Let \(B,S\) be locally compact sober spaces, with \(S\ne\varnothing\) and \(C_S\) dense in \(S^2\). With the canonical permutation \((B\times S)^2\cong B^2\times S^2\), there are equalities of **closed localic subrelations**:
\[
\boxed{
\mathcal W(B\times S)=\mathcal W(B)\times S^2,\quad
\mathcal W_2(B\times S)=\mathcal W_2(B)\times S^2,\quad
\mathcal U(B\times S)=\mathcal U(B)\times S^2.
}
\tag{2.1}
\]
Consequently, since S has a point and a B²-slice,
\[
\boxed{\mathcal W(B\times S)=\mathcal W_2(B\times S)
\iff \mathcal W(B)=\mathcal W_2(B).}
\tag{2.2}
\]
Thus product with S **reflects as well as preserves** the existence of a Q′ gap. There is no assertion of equality at the level of \(\mathcal D\) or \(\mathcal D_2\).

### Proof for W and W₂: generalized probes and a common lower witness

Fix \(\varepsilon=\mathrm{full}\) or \(2\). Put \(D_\varepsilon=\mathcal D\) or \(\mathcal D_2\), and \(H_\varepsilon=\operatorname{cl}D_\varepsilon\).

The upper containment is (1.2). For the reverse it suffices to prove \(D_\varepsilon(B\times S)\) is dense in the closed product \(H_\varepsilon(B)\times S^2\).

Take any nonzero relative open of this product. Its frame is generated by elementary rectangles; choosing one nonzero rectangle and refining B's coordinate opens yields B-opens a,b and S-opens u,v such that
\[
H_\varepsilon(B)\wedge\mathfrak o(a\boxtimes b)\ne0,
\quad u,v\ne0,
\]
and the elementary open \((a\times u)\boxtimes(b\times v)\) lies in the chosen relative open.

Density of \(D_\varepsilon(B)\) in \(H_\varepsilon(B)\) gives the nonzero locale
\[
T=D_\varepsilon(B)\wedge\mathfrak o(a\boxtimes b)
\]
and canonical generalized endpoint maps \(f,g:T\to B\) such that \(f^*a\wedge g^*b=1_T\). Density of \(C_S\) gives ordinary points s∈u, t∈v with a common predecessor p≤s,t.

Define
\[
\tilde f=(f,\underline s),\qquad \tilde g=(g,\underline t):
T\to B\times S.
\tag{2.3}
\]
We claim the pair factors through \(D_\varepsilon(B\times S)\). Let \(\mathcal C\) be ANY cover of B×S, or a finite cover in the ε=2 case. For each c∈C let \(c_p\in O(B)\) be its restriction to the slice \(B\times\{p\}\). The (finite) family \(\{c_p:c∈C\}\) covers B. Since f,g factor through D_ε(B),
\[
1_T=\bigvee_{c\in C}f^*(c_p)\wedge g^*(c_p).
\tag{2.4}
\]
Because p≤s,t and open subsets of B×S are upward-closed in the S coordinate,
\[
f^*(c_p)\le\tilde f^*(c),\qquad
g^*(c_p)\le\tilde g^*(c).
\]
Thus the ε-appropriate cover equation for \(\tilde f,\tilde g\) follows from (2.4), **for arbitrary probe locale T**, without selecting a point of D_ε(B).

Moreover \(\tilde f^*(a\times u)\wedge\tilde g^*(b\times v)=1_T\), so the chosen relative open meets D_ε(B×S) nontrivially. This proves the required density and equality of closures.

### Proof for U

For every pair of nonempty S-opens u,v, density of C_S produces s∈u,t∈v and p≤s,t; hence their closures intersect at p. Therefore \(\mathcal U(S)=S^2\).

For two points of B×S, testing the Urysohn relation can be done using product-basic neighborhoods, whose closures are the products of the factor closures. Thus the U point relation on B×S is the product of the U point relations on B and S. Since the localic square is spatial, the corresponding **closed sublocales** agree. With U(S)=S² this is the last equality in (2.1). QED.

### Adversarial boundary

The proof does **not** equate D_ε(B×S) with a product of the fitted diagonals. In fact the example below shows these fitted diagonals can behave differently while the closed hulls transfer exactly. It also does **not** assume that common-lower pairs in S are all of S², just that they are dense.

## 3. Specific noncompactification: three-limit bridge B times completed branching S

Let B be the countable compact sober noncontinuous Scott dcpo from [the preceding bridge note](ProjectA_Qprime_noncontinuous_Scott_THREE_LIMIT_BRIDGES_strict_WU_2026-11-11.md), with two wings X₀,Y₀ and finite bridge covers. As previously internally proved,
\[
\mathcal D(B)=\mathcal D_2(B),\quad
\mathcal W(B)=\mathcal W_2(B)<\mathcal U(B),
\quad
\operatorname{cl}(\operatorname{int}\mathcal U(B))<\mathcal U(B),
\tag{3.1}
\]
and \(\mathcal W_2(B)\wedge\mathfrak o(X_0\boxtimes Y_0)=0\) whereas \((x,y)\in\mathcal U(B)\cap(X_0\times Y_0)\).

Take S to be the algebraic dcpo of **all nonempty finite or infinite partial binary functions on N**, ordered by extension. Its Scott opens have basis ↑s for nonempty finite partial s. It is locally compact sober and NONCOMPACT: the singleton-literal cover
\[
\mathcal L=\{\uparrow\{n\mapsto b\}:n\in\omega,b\in2\}
\tag{3.2}
\]
has no finite subcover.

**Common predecessors dense.** If u,v are nonempty Scott opens, pick finite conditions s,t with ↑s⊆u,↑t⊆v. Choose a coordinate n outside dom(s)∪dom(t), and let p={n↦0}. Then extensions \(s\cup p\in u\) and \(t\cup p\in v\) share the lower bound p. Hence \(C_S\) is dense, though S has many incompatible pairs and is NOT hyperconnected.

Put
\[
X=B\times S.
\tag{3.3}
\]

### 3.1 This is a genuine Scott dcpo product, not just a topological space

**Lemma 3.1.** If P is any dcpo and S a **continuous dcpo**, then the Scott topology of P×S equals the product of the Scott topologies.

*Proof.* Coordinate projections preserve directed suprema, so product opens are Scott-open. Conversely, let O be Scott-open in P×S, with (p,s)∈O. The directed set \(\{(p,q):q\ll_S s\}\) has supremum (p,s), so some q≪s has (p,q)∈O. Put \(V=\{p':(p',q)\in O\}\), a Scott-open in P because the constant-q embedding preserves directed suprema. Put \(W=\Uparrow_S q=\{s':q\ll s'\}\), Scott-open containing s. Since W⊆↑q and O is an upper set, \(V\times W\subseteq O\). Thus every Scott-open is a product-topology open. QED.

The completed branching S is algebraic, hence continuous, so X with the ordinary product topology **is the Scott space of the product dcpo B×S**. It is still noncontinuous: a way-below approximant \((b,s)\ll(z,t)\) would project to b≪z in B (test directed sets \(\{(d,t)\}\) with sup (z,t)), but B has no such b.

Both factors are connected: the comparability graph of B is connected along its x/a/u/z/v/b/y bridges. For S, every nonempty partial function lies above some singleton literal. Two singleton literals on different coordinates have a common finite extension; two conflicting literals on the **same** coordinate are joined by a zigzag through a singleton at a different coordinate and two compatible finite extensions. Hence the entire comparability graph of S is connected, even for infinite or total partial functions (one must NOT assume there is a fresh coordinate outside the domain of a total function). A clopen of a Scott space is simultaneously an upper and lower set in the specialization order, hence constant on comparability components. Therefore X is **connected**, as well as noncompact, locally compact sober, noncontinuous and noncoherent.

**Noncoherence:** X₀×↑s and Z_{0,0}×↑s are compact opens for a finite condition s, but their intersection \(\{a_n:n\in\omega\}\times\uparrow s\) projects onto an infinite discrete space and is noncompact.

### 3.2 A genuine infinitary fitted-diagonal defect

The earlier completed branching example gives frame maps
\[
h_\pm:O(S)\to\operatorname{RO}(2^\omega)
\]
which are compatible with every finite cover, but fail the singleton-literal infinite cover (3.2): on each basic literal open \(\uparrow\{n\mapsto b\}\), their images are the opposite clopen cylinders [n=b] and [n=1−b], whose meet is zero.

Choose any bridge point \(b_0\in B\). Slice insertion \(i:S\to B\times S,\ s\mapsto(b_0,s)\) is continuous. The composites \(H_\pm=h_\pm\circ i^*:O(X)\to\operatorname{RO}(2^\omega)\) are finite-cover compatible (every finite X-cover restricts to an S-cover), but fail the X-cover \(\{B\times c:c\in\mathcal L\}\). Thus
\[
\boxed{\mathcal D(X)<\mathcal D_2(X).}
\tag{3.4}
\]

### 3.3 The two hulls still agree and both remain strictly below U

The transfer theorem immediately gives
\[
\boxed{
\mathcal W(X)=\mathcal W_2(X)
=\mathcal W(B)\times S^2
<\mathcal U(B)\times S^2=\mathcal U(X).
}
\tag{3.5}
\]
Since the nonregular Urysohn defect in B survives ×S², \(\mathcal U(X)\) remains **not regular closed**. More concretely, the entire mixed open strip
\[
(X_0\times S)\boxtimes(Y_0\times S)
\]
misses \(\mathcal W_2(X)\), even though its Urysohn restriction is nonzero. This follows already by the projection upper bound (1.1): the old finite bridge covers pull back to X, eliminating any alleged D₂ defect on this strip.

Thus the **two defects coexist in one connected noncompact noncontinuous Scott dcpo but do not couple**. There is NO Q′ counterexample.

## 4. Stronger stress test: all old easy patches can vanish

For S the completed branching domain, the prior note [continuous-Scott-dcpo programme](ProjectA_Qprime_continuous_dcpo_OPEN_Cm_regular_U_closed_heredity_2026-11-11.md) established:
\[
h_{\rm hc}(S)=h_{\rm cc}(S)=0,\qquad t_{\mathcal L}(S)=0.
\tag{4.1}
\]

**Claim 4.1: \(h_{\rm hc}(X)=0\).** Every nonzero X-open contains a nonzero product-basic U_B×U_S. Since every nonzero S-open contains two disjoint nonzero opens, the product open splits into two disjoint nonzero opens. Thus no nonzero X-open is hyperconnected.

**Claim 4.2: \(h_{\rm cc}(X)=0\).** Suppose a compact CLOSED sublocale F⊆X contains a nonzero open, hence U_B×U_S. Projection \(\pi_S:B\times S\to S\) is a proper/closed map because B is compact: the tube-lemma proof shows projection of every closed subset is closed, without a Hausdorff assumption on B. Thus \(\pi_S(F)\) is compact and closed in S, and contains nonzero U_S, contradicting \(h_{\rm cc}(S)=0\). This is a topological proof for the spatial closed sublocale F, which is represented by a closed subspace because X is sober; its compactness as a locale agrees with ordinary compactness.

**Claim 4.3: a cover has \(t_{\mathcal C}(X)=0\).** Take the pullback cover \(\mathcal C=\{B\times c:c\in\mathcal L\}\). If \(0\ne e\prec\bigvee F\) for finite F⊂C, choose a bridge point b and a nonempty S-open section \(e_b=\{s:(b,s)\in e\}\ne0\). Restrict \(e^*\vee\bigvee F=1_X\) to the B-slice at b. Because the frame homomorphism \(i_b^*\) preserves meet, it satisfies \(i_b^*(e^*)\le e_b^*\); therefore
\[
e_b^*\vee\bigvee(c:c\in F|_S)=1_S,
\]
contradicting \(t_{\mathcal L}(S)=0\). Thus no nonzero rather-below e exists and
\[
\boxed{t_{\mathcal C}(X)=0.}
\tag{4.2}
\]

We have therefore constructed a **noncompact**, nonregular, noncontinuous, noncoherent Scott locale with
\[
\boxed{
h_{\rm hc}=h_{\rm cc}=0,\quad t_{\mathcal C}=0
\text{ for a genuinely infinite cover},\quad
\mathcal D<\mathcal D_2,\quad
\mathcal W=\mathcal W_2<\mathcal U,\quad
\mathcal U\text{ not regular closed}.
}
\tag{4.3}
\]
Every apparently encouraging **global** necessary diagnostic survives, yet no Q′ gap exists. The missing condition is precisely a finite-cover defect **on the Urysohn residual rectangle where \(\mathcal W_2\) is nonzero**, rather than a product of two independent pathologies.

## 5. A non-product extension test: persistence versus pointwise rescue

The projection criterion is not the only obstruction to a non-product coupling. The original bridge-cover proof admits a useful formulation that can be applied when no projection to B remains.

**Lemma 5.1 (finite-tail cover persistence).** Let X be any locale with opens a,b and an **open discrete** sublocale \(D\le\mathfrak o(a\boxtimes b)\) indexed by a set I. Suppose there are finite covers \(F_n\) of X such that
\[
\mathfrak o(a\boxtimes b)\wedge\mathfrak o(w_{F_0})\le D,
\]
and \(\mathfrak o(w_{F_n})\wedge D\) corresponds to a subset \(E_n\subseteq I\) with \(\bigcap_nE_n=\varnothing\). Then
\[
\boxed{\mathcal D_2(X)\wedge\mathfrak o(a\boxtimes b)=0,\quad
\mathcal W_2(X)\wedge\mathfrak o(a\boxtimes b)=0.}
\tag{5.1}
\]
*Proof.* The first finite-cover square forces the D₂ restriction into the discrete D. There, sublocales of an ordinary discrete locale are ordinary subsets and their arbitrary meets are intersections, so simultaneous restriction by all the square covers is zero. The closure of D₂ is disjoint from any open on which D₂ is zero. QED.

For the original bridge B take a=X₀,b=Y₀, \(D=A\times B_{\rm bridges}\) and \(E_n=\{(i,j):i\ge n\text{ or }j\ge n\}\). The lemma survives **any non-product modification** whose finite bridge covers still exist with the same vanishing discrete tail traces, even when the modification has no projection to the original B. In particular, adding finite-cover members which never touch **both** wings contributes no mixed square and does not break this obstruction.

There is an opposite elementary danger.

**Lemma 5.2 (pointwise predecessor rescue).** Suppose X has a spatial localic square, and \(x,y\in X\) are such that **every pair of their open neighborhoods** a∋x,b∋y contains points s∈a,t∈b with a common specialization predecessor p≤s,t. Then
\[
\boxed{(x,y)\in\operatorname{pt}\mathcal W(X).}
\tag{5.2}
\]
*Proof.* Every common-predecessor pair (s,t) belongs to the full fitted diagonal D: a cover member containing p contains both s and t because opens are specialization-upward. Thus the common-predecessor relation is pointwise contained in D. Its closure contains (x,y) by the hypothesis, and the closure of D is W. QED.

So a proposed non-product identification of x/y bridge tails cannot create a cofinal family of **actual common-predecessor pairs** in every mixed neighborhood: that would cause full D, not only D₂, to become dense at the intended boundary point. Together Lemmas 5.1 and 5.2 articulate the narrow remaining design window: **finite bridge cuts must cease to eliminate the candidate mixed residual, but the new cross-wing compatibility must remain genuinely pointless, rather than becoming dense through ordinary lower-bound witnesses**. This is a research constraint, not a classification or universal disjunction.

## 6. Implications, boundaries and next experiment

1. The general transfer theorem (2.1) gives a new **no-go principle**: a noncompactification of the bridge example that preserves a locale map back to B cannot populate its forbidden mixed wing rectangle with \(\mathcal W_2\). Tensoring the bridge with a Scott forcing domain cannot defeat those old finite covers.
2. Conversely if some B were a Q′ counterexample, then B×S would be one as well, by (2.2). Thus this class of product operations does not simplify the universal question.
3. A genuine counterexample construction must **destroy the continuous projection back to the compact bridge** on the relevant mixed region, or change the Urysohn boundary so that the finite bridge covers cannot simply be pulled back.
4. The next *bounded* step should attempt a **non-product order coupling**: make bridge elements carry nonuniform forcing labels or identify a boundary cone in a way that breaks the projection. Its first audit test is whether the four finite bridge covers still extend to honest finite X-covers. If they do, the mixed rectangle remains excluded by W₂.
5. No claim of universal Q′ or Q: both **OPEN**. Neither local compactness alone nor algebraicity of the open frame controls the infinitary defect, and the current product example achieves all the obvious necessary global features while remaining positive for Q′.

**Audit status:** NEW INTERNAL proof. The exact transfer theorem's generalized-probe step, Scott product-topology lemma, and zero-patch stress tests require independent scrutiny before headline use. Background on locally compact sober products and continuous domains is classical; no originality claim.
