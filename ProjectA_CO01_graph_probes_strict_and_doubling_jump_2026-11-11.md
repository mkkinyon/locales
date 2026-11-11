# CO-01: homeomorphism-graph probes are strictly incomplete; doubling graph has A=point and A² dense

**11 November 2026. New internally checked research segment, NOT a cube-associativity verdict or external audit.** Directly pursues the [countable top-class endpoint criterion (6)](ProjectA_CO01_regular_fit_topclass_countable_endpoint_tests_2026-11-11.md) and the [continuous Boolean probe theorem](ProjectA_CO01_continuous_endomorphism_Boolean_test_2026-11-11.md). Main output: an explicit **single asymmetric endpoint open** that passes every Cantor-homeomorphism-graph density test but is not an open neighborhood of A², plus an exact **localic graph restriction** on which A collapses to a point while A² becomes dense. This rules out a natural proposed completeness strategy for the cubic top-class problem; it does **not** decide the cubes.

## 0. Conventions

Write \(C=2^{\mathbb N}\), \(D=\bigcup K_n\), \(V=C\setminus D\), \(B=\operatorname{RO}(V)\), \(q:\mathcal O(V)\twoheadrightarrow B\) the double-negation frame map, and \(A\subseteq V^2\) the exotic symmetric fitted relation. V is completely regular, so its locale is **strongly Hausdorff** (standard theorem regular locale⇒closed diagonal; Johnstone *Stone Spaces*, III.1; see Picado–Pultr). Consequently the graph \(\Gamma_f\subseteq V^2\) of every continuous f:V→V is a **closed localic sublocale**, by pulling back Δ_V. The **localic** square V² need not be spatial, but graph pullbacks and complements are valid in Loc.

For a continuous Cantor map f preserving D and V, let \(h_f=q\circ f_V^*\). The pair \((h_{\rm id},h_f)\) factors through \(\Gamma_f\), and its localic image in \(\Gamma_f\cong V\) is the **double-negation/Booleanization sublocale** \(V_{\neg\neg}\); this sublocale is dense in V.

## 1. Necessary homeomorphism-graph density condition for all endpoint top classes

Let H be the group of all Cantor homeomorphisms \(\rho:C\to C\) preserving D and V. Prior audit VIII's Baire-permutation argument says for every \(\rho\) in the **coordinate-permutation subgroup** \(\operatorname{Sym}(\mathbb N)\) one can find σ with \(h_{\rm id}\ A\ h_\sigma\ A\ h_\rho\); for arbitrary H this has **not** been established. Accordingly define G using only coordinate permutations, where the statement is proved:
\[
G=\bigvee_{\pi\in\operatorname{Sym}(\mathbb N)}
\operatorname{im}\big((h_{\rm id},h_\pi):\operatorname{Loc}(B)\to V^2\big).
\tag{1.1}
\]
Each image lies in \(Q=A^2\), so G⊆Q⊆L,R, where L=(A²)A and R=A(A²). Thus every endpoint open w with L⊆o(w) or R⊆o(w) satisfies
\[
q((\mathrm{id},\widehat\pi)^*w)=1
\ \Longleftrightarrow\
(\mathrm{id},\widehat\pi)^{-1}w\text{ is dense open in V}
\quad\forall\pi\in\operatorname{Sym}(\mathbb N).
\tag{1.2}
\]
This condition is invariant under endpoint swap because inversion of a coordinate permutation sends its graph to the reverse graph up to homeomorphism. Do not expand “coordinate permutations” to **all D-preserving Cantor homeomorphisms** without a separate two-hop theorem; the earlier Baire proof covered permutations, not arbitrary homeomorphisms.

## 2. An explicit proper asymmetric endpoint open passing all homeomorphism tests

Define coordinate doubling \(\delta:C\to C\) by \((\delta x)_{2n}=x_n\), \((\delta x)_{2n-1}=0\). It maps D into D, V into V and has **closed nowhere-dense range**
\[
T=\{y\in C:y_{2n-1}=0\ \forall n\}.
\]
Its only fixed point in C (and V) is 0, since a fixed x must satisfy \(x_{2n-1}=0\) and \(x_{2n}=x_n\), hence by recursively removing factors 2, x=0.

Let \(w=V^2\setminus\Gamma_\delta\) be the open **complement of the closed localic graph**. For any Cantor homeomorphism \(\rho\) preserving V, the coincidence locus \(Z_\rho=\{x\in V:\rho(x)=\delta(x)\}\) is closed **nowhere dense**. Indeed, if it contained a nonempty relatively open V∩O, then \(\rho(V\cap O)\), dense in the nonempty Cantor open \(\rho(O)\) because \(\rho(V)=V\) and V is dense, would lie in T, contradicting T nowhere dense. Hence
\[
q((\mathrm{id},\rho)^*w)=q(V\setminus Z_\rho)=1
\quad\text{for **every** such homeomorphism }\rho.
\tag{2.1}
\]
Thus even the full group H's graph-density **test** passes, irrespective of whether all H-graphs are contained in Q.

But the explicit noninvertible path proved in the companion note gives
\[
h_{\rm id}\ A\ h_\sigma\ A\ h_\delta,
\]
so the pair \(h_{\rm id},h_\delta\) factors through Q. Its pullback of w is 0, since its image lies in Γδ. Therefore
\[
\boxed{\quad G\subseteq o(w),\qquad Q\not\subseteq o(w),
\quad\text{hence } G\subsetneq Q. \quad}
\tag{2.2}
\]
Since Q⊆L,R, this w is NOT in the top class of either cube. It is not an associativity separator; it shows **permutation/homeomorphism graph testing is not complete even for A²**. The point is strict generation, not a new proof of nontransitivity.

## 3. Pullback of A along the doubling graph is exactly the single fixed point

Let \(j_\delta:V\to V^2\) be its graph inclusion; put \(A_\delta=j_\delta^{-1}A\), a sublocale of V.

**Theorem.**
\[
\boxed{ A_\delta=\{0\}\quad\text{as a localic sublocale of }V. }\tag{3.1}
\]

**Proof.** Reflexivity Δ≤A implies the fixed-point locale \(\mathrm{Eq}(\mathrm{id},\delta)=\{0\}\) lies in Aδ. Conversely choose any x∈V\{0}. Because δ(x)≠x, there is a Cantor-clopen neighborhood U of x disjoint from the equality locus. The continuous-map Boolean all-cover proof in [the companion note](ProjectA_CO01_continuous_endomorphism_Boolean_test_2026-11-11.md) gives more than failure of a dense Boolean test: since the same-\(K_n\) coincidence set \(P_{\mathrm{id},\delta}\) is EMPTY globally (heights n and 2n differ for every d∈D), for a sufficiently small Cantor-clopen \(U'\ni x\) one can construct an explicit Θ-admissible cover \(\mathcal C_{U'}\) with
\[
U'\cap V\cap\bigcup_{a\in\mathcal C_{U'}}(a\cap\delta^{-1}a)=\varnothing.
\tag{3.2}
\]
Namely, the compact image of \(U'\) under \((\mathrm{id},\delta)\) avoids Δ_C and every K_n×K_n. As in the earlier necessity proof choose Cantor-clopen W_n⊇K_n avoiding that compact image in \(W_n^2\), and finitely many additional Cantor-clopens U_i covering C and also avoiding it in \(U_i^2\). The Θ-admissible cover \(\{W_n\cap V\}\cup\{U_i\cap V\}\) gives (3.2).

Therefore \(A_\delta\) meets no nonempty Cantor-clopen \(U'\subseteq V\setminus\{0\}\). These clopens cover V\{0}, hence \(A_\delta\) is disjoint from the open sublocale V\{0} and is therefore contained in its closed complement {0}. With the first inclusion, equality follows. QED.

**Theorem (dense jump).** The pullback \(Q_\delta=j_\delta^{-1}(A²)\) contains \(V_{\neg\neg}\), since the path \(h_{\rm id}\ A\ h_\sigma\ A\ h_\delta\) is a map from Loc(B) into Q over jδ, with image precisely \(V_{\neg\neg}\subseteq V\). Hence
\[
\boxed{\quad A_\delta=\{0\}\ \subsetneq\
V_{\neg\neg}\ \subseteq Q_\delta,\qquad
\operatorname{cl}(Q_\delta)=V.\quad}
\tag{3.3}
\]
Strictness: Booleanization V¬¬ is nonzero and dense in the nontrivial V; it cannot lie in singleton {0}, as {0} is a proper closed sublocale. This is a **genuine jump from a single ordinary fixed point to a dense nonspatial sublocale of a graph after one relational composition**. It isolates where the new exotic paths live.

## 4. General equalizer-collapse criterion and universal A² density (new strengthening)

**Proposition.** Let \(f,g\in\mathscr T\), the full monoid of continuous C→C preserving D and V. Put \(p=(f_V,g_V):V\to V²\), let \(E=\mathrm{Eq}(f_V,g_V)\) (a closed sublocale, since V regular/strongly Hausdorff), and define
\[
P_{f,g}=\{d\in D:\mathrm{ht}(f(d))=\mathrm{ht}(g(d))\}.
\]
If **every** d∈P_{f,g} already satisfies \(f(d)=g(d)\), then
\[
\boxed{\quad p^{-1}A=E\quad\text{as sublocales of }V.\quad}\tag{4.1}
\]

**Proof.** Always \(E\subseteq p^{-1}A\) by reflexivity. For x∈V\setminus E choose a Cantor clopen neighborhood U of x such that f(y)≠g(y) for every y∈U, using continuity on C and Hausdorffness. Since P⊆Eq, U∩P=∅. The compact set \(F(U)=\{(f(y),g(y)):y\in U\}\) avoids Δ_C and every K_n²: any y∈U mapping into K_n² must lie in D (partition-preservation) and then in P, contradiction. Choose Cantor clopens \(W_n\supseteq K_n\) and a finite clopen cover \(U_i\) of C such that \(F(U)\) misses every \(W_n²\) and every \(U_i²\) (as in the exact all-cover necessity proof). The Θ-admissible cover \(\{W_n\cap V\}\cup\{U_i\cap V\}\) has pulled-back common-member open disjoint from U∩V. Thus \(p^{-1}A\) meets no clopen neighborhood of any x∈V\E. These clopens cover V\E, so \(p^{-1}A\) lies in the closed complement E. Equality follows.

**Independent strengthening (Baire theorem).** The separate [fusion/Baire theorem](ProjectA_CO01_All_Cantor_Endomorphisms_Boolean_DiameterTwo_2026-11-11.md) proves for **every** pair f,g∈\(\mathscr T\) that \(h_f A h_\sigma A h_g\) for some permutation σ. Therefore
\[
\boxed{\quad V_{\neg\neg}\subseteq p^{-1}(A²),\quad
\operatorname{cl}_V(p^{-1}A²)=V
\quad\text{for every }f,g\in\mathscr T.\quad}\tag{4.2}
\]
When P⊆Eq and E is a **proper closed** sublocale, A collapses to the exact equalizer but A² is dense. This generalizes the coordinate-doubling example and demonstrates that localic composition creates dense nonspatial graph structure even when the original relation is confined to an ordinary equalizer.

**Important:** the previous §1 limitation to coordinate permutations as the established A²-total family is superseded by the proven fusion/Baire theorem. The full monoid \(\mathscr T\), including arbitrary D/V-preserving homeomorphisms, is A²-total in Boolean-valued points; this remains far short of proving that such points generate the whole image locale A² or its cubic pullbacks.

## 4. Limits for CO-01

- Equation (6) is now bounded by a strictly incomplete graph-density condition: no proof of its symmetry can rely solely on coordinate-permutation/homeomorphism generic graphs.
- The graph \(\Gamma_\delta\) is a concrete **closed noncompact** carrier where A and A² differ dramatically. A candidate cubic separator might be supported on a different noncompact graph, but merely choosing \(\Gamma_\delta\) fails because A²⊆both cubes.
- These results do NOT show that \((A²)A=A(A²)\), nor that the endpoint-path forcing condition holds. The needed new datum is a **nonliftable generalized point of the image \(A²\)** after the relevant base change, or an asymmetric infinite clopen endpoint top equation.
- New results internally checked; no independent external audit. The tested homeomorphism group in §1 is **specifically the coordinate-permutation group**; statements about all D-preserving homeomorphism **tests** in §2 do not assume factorization of their graphs through A².
