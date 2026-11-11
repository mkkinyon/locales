# CO-01 compact-local triviality theorem — Arrieta A and all finite localic powers

**11 November 2026. New internally checked frame/sublocale theorem, NOT a cube-associativity verdict or external audit.** Complements the [countable clopen Θ-cover normal form](ProjectA_CO01_Arrieta_countable_clopen_generators_finite_cover_gap_2026-11-11.md) and [regular-fit top-class reduction](ProjectA_CO01_regular_fit_topclass_countable_endpoint_tests_2026-11-11.md). It strengthens the previous theorem that every finite power has exactly diagonal **ordinary point fibres**: restriction along **any compact subspace** of V is exactly diagonal as a **locale**.

Let C=2^N, D=∪K_n, V=C\D with its regular subspace topology. Let A⊆V² be the exotic fitted nontransitive V×V block of Arrieta's \(\mathcal D_Y\). For every \(\Theta\)-admissible open cover \(\mathcal C\), A⊆O(\gamma_C), with \(\gamma_C=\bigvee_{a\in\mathcal C}a_1\wedge a_2\). All compact K⊂V are compact in the Hausdorff Cantor C and hence **closed in C**, so disjoint from D.

## Theorem 1 (compact first-coordinate restriction)

For any compact subspace \(K\subseteq V\) (possibly empty), with localic inclusion \(K\hookrightarrow V\),
\[
\boxed{\quad
A\cap(K\times V)=\Delta_K\subseteq K\times V,\quad
A\cap(V\times K)=\Delta_K.
\quad}\tag{1.1}
\]
The left-hand formula identifies Δ_K with the graph of the inclusion K→V, so this is a statement about **sublocales**, not just their ordinary point sets.

**Proof.** Since K is compact Hausdorff and V is regular, the localic product K×V has its usual rectangle basis and the graph Δ_K is a closed, hence fitted, sublocale of the regular K×V. Let \(w\in\mathcal O(K\times V)\) be any open containing Δ_K. By a rectangle basis and compactness of K, choose finitely many V-opens \(b_1,\ldots,b_m\) such that K⊆∪ b_i and
\[
\bigvee_i (K\cap b_i)\boxtimes b_i\le w
\quad\text{in }\mathcal O(K\times V).
\tag{1.2}
\]
For clarity: for each x∈K choose a rectangle U_x⊠V_x≤w containing (x,x), choose a V-open b_x around x with K∩b_x⊆U_x and b_x⊆V_x, then take finitely many b_x covering K. This can also be proved frame-theoretically using δ_K^*(w)=1, compactness of K and the rectangle tensor basis, without relying on global spatiality of V².

The family
\[
\mathcal C_K=\{V\setminus K,b_1,\ldots,b_m\}
\]
is an **open cover of V**. It is Θ-admissible: the Cantor-open C\K contains **every** K_n (since K⊂V and K_n⊂D), and its V-trace is V\K. Thus Θ(V\K)=N. By definition A⊆O(γ_{C_K}). After restriction to K×V, the \((V\setminus K)\boxtimes(V\setminus K)\) rectangle vanishes (the first coordinate lies in K), while the remaining squares lie below w by (1.2). Hence \(A|_{K\times V}\subseteq O(w)\) for every open w containing Δ_K. Since Δ_K is fitted, \(A|_{K\times V}\subseteq\Delta_K\). The reverse inclusion follows from reflexivity of A. Symmetry proves the second formula. QED.

**No finite-cover collapse is claimed:** the compact restriction was proved using a *particular* finite admissible cover depending on w and K; globally A⊊A_fin, as shown earlier.

## Theorem 2 (all parenthesized finite powers)

Let P(A) be any nonempty finite binary parenthesized product of copies of A under image-defined localic composition, with Δ as the two-sided unit. Then for every compact K⊂V:
\[
\boxed{\quad
P(A)\cap(K\times V)=\Delta_K
=P(A)\cap(V\times K).
\quad}\tag{2.1}
\]
**Proof.** Induct on the number of factors. For P=R∘S, the composable source \(R_{12}\cap S_{23}\to V²\) factors through its localic image P via a **locale-surjection**. Base change of a locale-surjection along a **closed sublocale inclusion** remains a locale-surjection. Here K×V↪V² and V×K↪V² are closed, since K is closed in V. On the first-coordinate restricted composable source, the induction hypothesis R|_{K×V}=Δ_K forces the middle coordinate equal to the first x∈K; then S|_{K×V}=Δ_K forces the last coordinate equal to x. Consequently the restricted source is exactly Δ_K, and its image after the pullback-stable surjection is Δ_K. The second-coordinate version follows dually. Every parenthesized product contains Δ because A is reflexive, so no loss of diagonal occurs. QED.

**Proof of the needed closed-base-change fact:** If e:T→S is locale-surjective (e^*:O(S)→O(T) injective) and K=C(c)↪S is a closed sublocale, the frame for the base change T×_S K is the closed quotient ↑e^*(c), and the induced ↑c→↑e^*(c) sends x∨c to e^*(x∨c). It is injective by injectivity of e^*. Thus the pulled-back locale map is surjective. This is the same fact independently used in [associativity audit VIII §7](A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md).

## Consequences and scope

1. For any generalized point \(T\to A\) or \(T\to P(A)\), **if either endpoint coordinate factors through a compact subspace K of V, the endpoints must coincide**. This is stronger than singleton ordinary point fibres; T itself may be nonspatial.
2. A possible nonassociativity separator between the cubic relations **cannot** be obtained by confining either endpoint to a compact subset of V. The two bracketings both restrict there to Δ_K.
3. The effect is genuinely noncompact: V has **no nonempty relatively compact open neighborhood**. Otherwise a nonempty V-open inside a compact K⊂V would contain a nonempty Cantor cylinder trace, whose closure in C meets dense D, contradicting K∩D=∅. Hence compact-local triviality does **not** imply A=Δ on all of V².
4. A remains a nontransitive fitted relation: the nonspatial Boolean generalized points \(h_{\rm id},h_\sigma,h_\tau\) from audit VIII cannot have an endpoint factor through any compact K⊂V unless both endpoints coincide. Their path obstruction occurs genuinely at the nonlocally-compact boundary.
5. The theorem does **not** show associativity of the cube; it rules out a broad class of generalized endpoint tests and provides a concrete finite-cover localization tool to investigate the remaining infinite-depth endpoint equations.

**Status:** new internally checked theorem on all finite powers, built on an independently used closed-base-change lemma; no new CO-01 association verdict.
