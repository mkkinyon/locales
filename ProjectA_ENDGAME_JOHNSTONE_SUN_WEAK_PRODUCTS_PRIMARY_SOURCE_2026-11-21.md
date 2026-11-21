# Endgame source reconciliation — Johnstone–Sun (1988): weak products, p/q, scatteredness
## 21 November 2026 · uploaded primary paper, pages 173–193

**Primary source directly read:** P. T. Johnstone and Sun Shu-Hao, *Weak Products and Hausdorff Locales*, in *Categorical Algebra and Its Applications*, Lecture Notes in Mathematics 1348 (1988), pp. 173–193, DOI 10.1007/BFb0081358. Source supplied by project owner as a 21-page PDF extract of the volume. **Do not copy the copyrighted supplied PDF into the public repository**; this note gives exact statements, page numbers and project corollaries. This supersedes the earlier “not accessible, request from user” status in [prior exact comparison](ProjectA_ENDGAME_EXACT_COMPARISON_PATCH_AND_PQ_2026-11-21.md).

**Major verdict:** This is an **exact, substantial antecedent** for the *weak product versus full product* distinction underlying our p(A,B) and q(A,B), and for the *special role of scattered coordinates*. It does **not** state the mixed rectangular localic **composition rule** (RC), the full parameterized arbitrary-sublocale reconstruction (MAT), or its actual localic-image matrix law (MUL); do **not** infer these from the source without proofs.

## I. What Johnstone and Sun actually prove

Notation: they write \(A\mathbin{@}B\) for the **weak product** and \(A\times_{\rm Loc}B\) for the categorical localic product. Weak products are defined via the double Galois closure \(S^{+-}\) on locale product C-ideals (§1, Definition 1.1 and Lemmas 1.2–1.4, pp.175–176).

1. **Cor. 1.5 (p.176):** \(A@B\) is always a **dense sublocale** of \(A\times_{\rm Loc}B\).
2. **Prop. 1.7 / Thm. 1.8 (p.177):** weak product is functorial and defines a **symmetric monoidal structure** on all locales. These are not arbitrary retract/coreflection tricks.
3. **Prop. 1.9 / Cor. 1.10 (pp.177–178):** every point of a full localic product factors through the weak product, and every map from a **spatial** locale into the product factors through it.
4. **Prop. 1.11 / Cor. 1.12 (p.178):** weak product of spatial locales is spatial and \(\Omega(X)@\Omega(Y)\cong\Omega(X\times Y)\), exactly the spatial part of the full localic product. This is the decisive predecessor for our p/q.
5. **Lemma 1.16 (pp.181–182):** for **locally closed inclusions** \(A'\hookrightarrow A\), \(B'\hookrightarrow B\), the natural square comparing weak products with full locale products is a **pullback**. This is relevant to chart restriction, not by itself a localic relation-composition theorem.
6. **§1 preceding Prop. 1.17 (p.182):** if A is locally compact and spatial and B spatial, then \(A@B=A\times_{\rm Loc}B\). This is cited to Johnstone, *Stone Spaces*, II.2.13, and Cor. 1.12.
7. **Def. distributed (p.182):** \(A\) is *distributed* if \(A@B=A\times_{\rm Loc}B\) **for every locale** \(B\), including nonspatial B.
8. **Prop. 1.17 (pp.182–183):** distributedness is inherited by locally closed sublocales and retracts, finite products, distributed open covers and complemented open/closed gluing; injective locales are distributed, with a locally compact Boolean test (f).
9. **Lemma 1.18 (p.183):** nonempty Hausdorff spaces without isolated points have **non-distributed** locale of opens, using the regular-open atomless Boolean frame as a test factor.
10. **Prop. 1.19 (pp.183–184):** for **any Hausdorff space X**, \(\Omega(X)\) distributed **iff X scattered**. Proof uses a nonempty perfect closed subspace for the negative direction and Cantor–Bendixson induction, plus open/closed gluing and local opens, for the positive.
11. **Prop. 1.20 (p.184):** weak exponentiability of A iff ordinary local compactness **and** distributedness. An adjacent but separate classical result.
12. **§2, especially Def.2.1, Cor.2.3, Prop.2.4 and Prop.2.14 (pp.185–192):** introduces a *conservative Hausdorff locale* axiom, coinciding with ordinary Hausdorffness on spatial locales and **equivalent to the (T₂) axiom independently developed by Paseka and Šmarda**. Distinct from our **strong** Hausdorff/closed-diagonal axiom \(\mathcal I=\Delta\). Provides important older separation-axiom background for the next literature stage; do not conflate.

## II. Exact embedding of p and q into the weak-product formalism

For compact Hausdorff G and ordinary A,B⊆G, let \(V_A=[A]_G\), \(V_B=[B]_G\) be the induced sublocales. Since A,B are Hausdorff, \(\mathcal O(A)\cong V_A,\ \mathcal O(B)\cong V_B\) as spatial locales. The inclusions \(V_A\hookrightarrow G,\ V_B\hookrightarrow G\) induce
\[
q(A,B)=V_A\times_{\rm Loc}V_B\hookrightarrow G\times_{\rm Loc}G.
\]
Johnstone–Sun Cor. 1.12 identifies \(V_A@V_B\) with \(\mathcal O(A\times B)\), and the composite of its canonical inclusion \(V_A@V_B\hookrightarrow q(A,B)\) with \(q(A,B)\hookrightarrow G^2\) is exactly the locale embedding of the ordinary topological subspace \(A\times B\subseteq G\times G\). Hence
\[
\boxed{p(A,B)=V_A@V_B,\qquad q(A,B)=V_A\times_{\rm Loc}V_B}
\]
**as specified sublocales of G²**. This is a straightforward **project corollary/identification of Johnstone–Sun**, not a theorem stated in their rectangle notation.

Further exact consequences:
- **p is dense in q** (Cor.1.5), even if q is genuinely nonspatial; the weak product is the **spatial part** of q for spatial A,B. This is stronger than merely having equal least ambient closed support.
- If **either A or B is scattered**, then Prop.1.19 gives \(p(A,B)=q(A,B)\), including when the other factor is arbitrary Hausdorff and not locally compact.
- If **either A or B is locally compact as a subspace**, the spatial product of locally compact with spatial equals the localic product, so \(p=q\). In particular, if one is a **locally closed subspace** of compact Hausdorff G, it is locally compact, so \(p=q\).
- Therefore a **strict** p/q gap requires **both** subspace factors to be neither scattered **nor** locally compact. This is a useful necessary condition, not a sufficient characterization; other spatial multipliers can also force equality.
- The weak product is a **functorial monoidal** operation. Our finite p/q rectangular calculus mixes its arrows with **full categorical products**, an interaction not studied in the paper's §1 as relational composition.

**Important caution:** neither the density \(p\le q\) nor the equality of their ambient closures justifies \(p\circ p=q\) without the separate **referee-origin saturated middle-overlap theorem (RC)**. Source's Theorem 1.8 is associativity of a *monoidal product of locales*, categorically distinct from associativity of *relational image/pullback composition*. Never conflate the two associativities.

## III. Relevance to scattered-index matrix theorem MAT/MUL

Let compact Hausdorff K be scattered. Prop.1.19 gives a **much earlier structural explanation** for the exceptional behavior of the K-coordinate: \(K@Z=K\times_{\rm Loc}Z\) for **every locale Z**, possibly pointless. The project MAT states, for compact Hausdorff Z and K,
\[
\operatorname{Sub}(Z\times K)\cong\prod_{k\in K}\operatorname{Sub}(Z),
\]
with the explicit fiberwise reconstruction and its extension to finite K-powers. Project MUL states that the **actual** localic image/pullback relation composition satisfies
\[
(R\circ S)_{ik}=\bigvee_{j\in K}(R_{ij}\circ_Z S_{jk})
\]
even though arbitrary relation associativity over Z does not follow.

**Scope of overlap:** distributedness of K is an assertion about the equality of **two product functors with K as a factor**; MAT is an assertion about **all subobjects of one product**, and MUL additionally about the **composability pullback and actual image**. The former neither states nor immediately proves the latter. However, the close correspondence deserves a search for a categorical reduction, perhaps through universal point-cover descent; the project recently produced a separate internal HSIS/point-cover argument. Do not advertise MAT as having no classical scattered-product antecedent.

**Local chart connection:** Lemma 1.16 provides exact pullback behavior of weak versus full product under **locally closed maps**. In our chart algebra, local product constraints can therefore be compared directly with their full localic pullbacks. This may provide an explanatory lemma for some chart arguments, but it does **not** automatically prove balanced-witness triple associativity.

## IV. Separation side: important extra reference

The article explicitly distinguishes **strong Hausdorffness** (closed diagonal in the full locale square) from its new conservative Hausdorffness (Def.2.1, p.185). Cor.2.3 identifies the latter with ordinary Hausdorffness for T₀ spaces; Prop.2.4 gives the first-order condition; Prop.2.14 identifies it with Paseka–Šmarda \((T_2)\) (pp.186, 192). This belongs in the Arrieta/Isbell/Dowker–Strauss portion of the endgame literature review because our \(\mathcal I=\operatorname{cl}\Delta\) precisely measures **strong** Hausdorffness, which is not conservative. Johnstone–Sun does not identify the full \(\mathcal I,\mathcal D,\mathcal U\) hierarchy.

## V. Priority and repository disposition

**Established prior facts:** weak products, their dense inclusion, spatial product identification, functorial/symmetric-monoidal law, locally closed compatibility, distributedness criterion, conservative Hausdorff axiom.

**Newly sharpened project synthesis:** our \(p/q\) are precisely the weak/full product pair **inside a common compact-Hausdorff square**; p is dense in q; strict gap needs both factors non-scattered and non-locally compact. These are formal easy consequences of the 1988 source, **not novel mathematical claims**.

**Still separate audited project theorems:** RC's exact four mixed p/q composition cases, balanced-witness/graph extension under RC, parameterized MAT and actual localic MUL. A fuller categorical reduction or older predecessor to them is **unresolved**, not certified new.

**Editorial action:** revise any earlier prose implying weak/full product distinction was discovered here; cite Johnstone–Sun explicitly for p/q at the beginning of the rectangular canonical proof. No need to alter the audited mathematical statements. Final priority picture must give this 1988 source prominent placement, alongside Townsend (1996), Plewe (1996), and Picado–Pultr's later scatteredness theorem.
