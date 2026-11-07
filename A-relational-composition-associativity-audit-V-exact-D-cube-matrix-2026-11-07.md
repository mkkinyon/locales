# Project A — Associativity audit V: exact high/low relation-matrix calculus and D³ reduction to the Arrieta base

**7 November 2026. WORKING theorem package, not independently externally audited.** This note CORRECTS a false caution in [audit IV](A-relational-composition-associativity-audit-IV-D-cube-high-low-2026-11-07.md): although locale-surjections can fail arbitrary base change, they remain surjective after pullback along OPEN OR CLOSED sublocale embeddings, hence along LOCALLY CLOSED layer blocks. Consequently the full two-layer image/relational matrix calculus is valid for BINARY compositions. The all-locale associativity issue remains; we never suppress parentheses in triple products. This is an important improvement, not a counterexample to Loc's general nonassociativity.

## 1. Source and setup

Take Y strongly Hausdorff and X=X_u=O(u∨σ)↪Y×S, with u∈O(Y), σ the Sierpiński generator. Let U=O(u)↪Y and j:U↪Y its OPEN inclusion. X has open high layer H=O(σ)≅Y and complementary closed low layer N=C(σ)≅U. Let

    F=D_X,     E=D_U,     G=D_Y.

As proved in [audit IV §2](A-relational-composition-associativity-audit-IV-D-cube-high-low-2026-11-07.md), the exact localic relation restrictions of F are

    F_NN=E,    F_NH=P,    F_HN=P^smile,    F_HH=G,

where P⊆U×Y is E embedded along id_U×j (so P relates x∈U to y∈Y precisely via E with y also in U), and P^smile⊆Y×U is its converse.

Also c=s∘r:X→X is the OPEN idempotent and x≤c x for all generalized points. A fitted relation F is stable under applying c to either coordinate; crucially, compositions of c-stable relations are c-stable AS SUBLOCALES via endpoint-map image factorization, without requiring intermediate image lifts along arbitrary maps (audit IV §3).

## 2. OPEN and CLOSED embeddings preserve locale-surjections

**Lemma (direct frame proof).** Let f:T→Z be SURJECTIVE as a locale map, meaning f*:O(Z)→O(T) injective. Let i:C(a)↪Z be a CLOSED sublocale, with frame O(C(a))=↑a, whose quotient map sends z↦a∨z. Its pullback along f is C(f*a)↪T, frame ↑f*a. The frame inverse image of

    T×_Z C(a) → C(a)

is precisely the RESTRICTION

    f*|_(↑a):↑a→↑f*a,

which is injective. Thus locale-surjections are pullback-stable along CLOSED sublocale embeddings. For OPEN sublocale O(b)↪Z, use ↓b and restriction f*|_(↓b) analogously. Any locally closed inclusion is a composite of these, so has the same stability.

**Image base change corollary.** For any map t:T→Z and any locally closed B↪Z,

    im(T×_Z B → B) = im(t) ∧ B,

where the right meet is the sublocale intersection inside Z and the left side is transported along B↪Z.

This corrects audit IV's claim that restricting an intermediate image to a CLOSED low layer was inherently unsafe. Nonassociativity in Loc arises from base changes along other maps, such as the discrete-refinement map g:Z_disc→Y in audit I, NOT from open/closed endpoint inclusions.

## 3. Exact TWO-LAYER matrix multiplication for binary localic composition

For ANY R,S⊆X², restrict them to the four blocks X_N×X_N, X_N×X_H, X_H×X_N, X_H×X_H. The sublocale lattice is a coframe, and the complementary open/closed pairs N∨H=X, N∧H=0 remain complementary under pullback to the composable-pair source. The source R12∧S23 is therefore the FINITE JOIN of its restrictions to the two middle layers and the four endpoint blocks. Direct image preserves arbitrary joins. By §2 images restrict faithfully to the locally closed ENDPOINT blocks. Therefore

    **(R∘S)_(ij) = (R_(iN)∘S_(Nj)) ∨ (R_(iH)∘S_(Hj)),  i,j∈{N,H}.**

Here each binary composition on the right occurs in Loc between the corresponding (possibly distinct) layer locales; no claim that this matrix multiplication is associative.

For F above, ordinary block multiplication first gives

    (F²)_NN = E² ∨ (P P^smile),
    (F²)_NH = (E P) ∨ (P G),
    (F²)_HN = (P^smile E) ∨ (G P^smile),
    (F²)_HH = (P^smile P) ∨ G².

The NN terms P P^smile and E² agree: the middle high coordinate of P P^smile is forced into the open sublocale j(U) of Y, and U×_Y U=U since j is mono, so their composable-pair locales identify with the E² source. The NH and HN lower-mediator terms are contained in their upper-mediator terms by upgrading the intermediate low y to c y (F fitted, genuine composable-pair sources). The HH lower-mediator term P^smile P is contained in G² for the same reason, or because the image of E under j×j lies in G.

Thus the EXACT SQUARE is

    **F² = [ E²      P G
             G P^smile   G² ].**

No associativity or purely pointwise reasoning used.

## 4. Exact two bracketings of F³ — a three-equation criterion

Apply the valid BINARY matrix multiplication to (F²)F and F(F²), KEEPING parentheses on every triple term. Each product formally yields two middle-layer summands. In EVERY endpoint block, the summand with low intermediary is contained in the high-intermediary summand: the generic low intermediary y is replaced by c y (high), using c-upward stability of F AND F² from audit IV §3. This source-level map gives a genuine inclusion of images, even though F² is not known fitted.

Therefore

    **(F²) F =
      [  (P G) P^smile      (P G) G
         (G²) P^smile      (G²) G    ]**

and

    **F (F²) =
      [  P (G P^smile)      P (G²)
         G (G P^smile)     G (G²)    ].**

Because F,G symmetric, the HN equality is the converse of the NH equality. Thus:

**EXACT CRITERION (working):** F³ associates if and only if ALL THREE hold:

    (A) (G²) G = G (G²)                       [Y×Y]
    (B) (P G) G = P (G²)                      [U×Y]
    (C) (P G) P^smile = P (G P^smile)        [U×U].

These are three explicit LOCALIC image association tests on the smaller base and open sublocale, with exact parentheses. Nontransitivity F²⊄F provides no answer to any of them.

## 5. Strong reduction when U=O(u) is F-separated

Assume U is F-separated, E=D_U=Δ_U. Then P is simply the GRAPH Γ_j of the OPEN embedding j:U↪Y, and P^smile is the converse graph.

For ANY relation R on Y, composition with Γ_j or Γ_j^smile is ordinary sublocale restriction along j in the respective coordinate. Since j is OPEN, these restrictions commute with taking localic images.

Consequently condition (B) is automatic:

    (P G)G=(G|_(U×Y))G = G²|_(U×Y) =P(G²).

And condition (C) is automatic:

    (P G)P^smile=G|_(U×U)=P(G P^smile).

Thus, in the Sierpiński extension over sH Y with U F-SEPARATED,

    **D_X³ associates  ⇔  D_Y³ associates.**

Both bracketings of D_X³ agree on every block involving a LOW endpoint; their common entries are

    NN:  G|_(U×U),
    NH:  G²|_(U×Y),
    HN:  G²|_(Y×U).

Their HH entries are (G²)G versus G(G²), respectively.

This strengthens audit IV's one-way HH implication: with a F-separated low open part, the equivalence is EXACT, not merely a sufficient condition in one direction.

## 6. Arrieta's actual example permits a REGULAR open witness u

The 2024 published construction (Construction 4.2 + Example 4.5 + Cor. 4.10) starts with the Cantor cube C, deletes a countable family of disjoint nonempty compact K_n, and makes a topological extension Y=R⊔N, where R=C\∪K_n is REGULAR as a subspace of Cantor cube, and is OPEN in the newly constructed Y (not necessarily open in the original Cantor cube), while N is CLOSED DISCRETE in Y. The resulting Y is SPATIAL, strongly Hausdorff, anti-Urysohn and non-F-separated. Source: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf , printed pp. 12–14.

**Lemma (working).** In such a Y, some witness u for D_Y>Δ_Y can be chosen with u≤R. In particular O(u) is regular, hence F-separated.

Proof: Let d_I=∨_{a∧b=0}a⊠b, Δ_Y=C(d_I), and W=D_Y∧O(d_I)≠0. Restrict W to N×N. This vanishes: N×N is a DISCRETE localic product and therefore spatial/point-determined; for ordinary distinct n,m∈N, the Y Hausdorff (indeed T1) two-element open cover {Y\{n},Y\{m}} excludes the pair from D_Y, so D_Y|_(N²)=Δ_N; Δ∧O(d_I)=0. The open/closed first/second R,N partitions decompose W into four blocks. Since the NN block is zero and W is symmetric, W|_(R×Y) is NONZERO. On V=D_Y∧(R×Y), the restricted OPEN d_I is nonzero. Its frame restriction preserves arbitrary joins; hence some disjoint rectangle a⊠b has nonzero restriction to V. Put u=a∧R and v=b. Then u≤R, u∧v=0 and D_Y∧O(u⊠v)≠0. As v≤u*, the canonical witness D_Y∧O(u⊠u*) is also nonzero. Since R regular and U=O(u) is an OPEN sublocale of R, U is regular, hence F-separated.

This u can therefore be used in the externally refereed negative mixed-V transfer construction X_u=O(u∨σ) with no loss of that result.

**Corollary (precise current status for the ARRIETA-based spatial counterexample):** One may choose the spatial negative-transfer X_u so that

    **D_(X_u)³ associates  ⇔  D_Y³ associates.**

The desired remaining yes/no question has now been transferred ENTIRELY to Arrieta's strongly Hausdorff anti-Urysohn base Y. There is NO additional low-layer associativity obstruction for this choice of u.

This is NOT a claim that D_Y³ associates or fails: its status remains OPEN. Moreover the equivalence does not hold for all possible u without the F-separatedness of O(u).

## 7. Categorical lessons and remaining research target

1. Open AND closed endpoint embeddings are image-stable. The earlier idea that the low CLOSED block itself generates an image-instability obstruction was mistaken, and is explicitly retracted here.
2. Three nested D_X relations reduce to three base/mixed association tests (A)–(C); for F-separated U only (A) remains.
3. The non-F-separatedness witness can be chosen REGULAR in the Arrieta 2024 space, so all mixed issues are cleanly removed while the independently refereed I D⊄V and D²⊄D conclusions remain.
4. The next actual question is whether **(D_Y²)D_Y=D_Y(D_Y²)** for the published spatial sH anti-Urysohn Y. It requires a genuine localic image calculation, not ordinary points or density alone. The dense relation D_Y and U_Y=W_Y=Y² (audit IV) do NOT settle it.
5. Recheck the binary matrix lemma under a categorical adversarial audit before using more elaborate 4-layer expressions. The claims here are internally argued, not externally refereed.
