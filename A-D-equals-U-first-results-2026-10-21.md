# A — First results on D = U (21 October 2026)

**Status: new working proofs; not independently audited.** Start from [A-fitted-diagonal.md](A-fitted-diagonal.md) (definition D=fit(Δ), general inclusions Δ⊆D⊆U and I⊆U).

## 1. Intrinsic arbitrary-frame open-cover criterion

Let L be a frame, Q=L⊕L its frame coproduct, δ*:Q→L the diagonal inverse-image, and

    d_U = ⋁ {a⊠b : a*∨b*=1}.

For an open cover C⊆L with ⋁C=1, put w_C=⋁_{c∈C} c⊠c.

**Proposition (working).** The following are equivalent:

1. D(L)=U(L).
2. For every open cover C of L, d_U∨w_C=1 in Q.
3. For every w∈Q with δ*(w)=1, d_U∨w=1.

**Proof.** The defining fitting D=⋂_{δ*w=1}O(w) and D⊆U show equality iff U⊆O(w) for each such w. For a closed sublocale C(d)⊆O(w), the standard closed/open inclusion criterion is d∨w=1. This yields (3). Every w is a join of rectangles a_i⊠b_i, and δ*w=1 entails that {a_i∧b_i} covers 1, with w_{C}≤w. Conversely δ*(w_C)=1 for every cover. Hence (2)⇔(3).

**Interpretation:** For any open cover, the squares of its members together with *all far rectangles* cover X×X *as a locale*. Ordinary pointwise coverage is not an adequate substitute.

This is a direct reformulation of the fitting definition, **not** claimed to be a new separation axiom.

## 2. Finite Alexandrov classification

Use upper-set topology for a finite poset P. By [A-fitted-diagonal.md](A-fitted-diagonal.md), x D y iff x,y have a common lower bound; x I y iff they have a common upper bound. U lies above both.

**Theorem (working).** For a finite poset P, D(P)=U(P) iff every connected component of its comparability graph has a least element, equivalently every component is downward directed.

**Proof.** Suppose D=U, so I⊆D. If x D y and y D z, choose u≤x,y and v≤y,z. Since u,v share upper bound y, u I v, whence u D v. So some t≤u,v satisfies t≤x,z, proving transitivity of D. Comparable points are D-related, and hence D relates every pair in a comparability component. Therefore that component is downward directed; a finite directed-downward poset has a least element.

Conversely, if each component has a least point, any pair in the component is D-related. For points in different components, the closures of their least open neighborhoods stay in their respective components, hence the points are not U-related. Equality follows on all points; the finite locale and its product have enough points to detect these particular sublocales (indeed all sublocales of finite frames are spatial).

**Caution:** Do not extend the 'least element' criterion to infinite posets without proof; downward directedness does not imply a least element. Also avoid inferring analogous global equivalence for arbitrary frames from a finite spatial calculation.

## 3. Next questions (deferred separately)

- Find an intrinsic non-tautological characterization of D=U using nuclei, fitting, or standard point-free separation notions.
- Test stability under frame products/coproducts; unlike I=U, fitting need not commute formally with those operations.
- Examine continuous/coherent specializations of the cover criterion.
- **Separate later question:** Does D=U imply D=U=F? Do not assume this from finite evidence.

## Literature

Arrieta, Picado, Pultr (2022), *A New Diagonal Separation and Its Relations With the Hausdorff Property*; Arrieta (2024), *Localic Separation and the Duality Between Closedness and Fittedness*. Literature priority and any exact identification remain unchecked.

## 4. Fitted U need not equal D (decisive finite example)

**Theorem (direct point-free proof).** There is a finite coherent frame L with U(L) fitted but D(L)≠U(L).

Let P={a,b,t}, ordered a<t and b<t, with upper-set topology. Its frame L has five elements: ∅, {t}, {a,t}, {b,t}, P. Every nonempty open contains t. Therefore each nonzero u has u*=0. A pair u,v is far only if one is zero; every far rectangle vanishes, so d_U=0 and U=C(0)=P×P, which is fitted (O(1)).

The two opens A={a,t} and B={b,t} cover P. Their square-open w=A⊠A∨B⊠B satisfies δ*(w)=A∨B=1 but does not contain the ordinary product point (a,b). Hence D⊆O(w)≠P×P=U. This is Example B already present in A-fitted-diagonal.md, now repurposed as a strictly weaker fittedness witness.

**Optional nontrivial proper U:** Take the disjoint union of this P and a singleton. Then U is the union of the two component squares (mixed-component pairs are far), hence is a proper clopen/fitted sublocale of the product, while D≠U still holds on the P component.

**Finite-locale observation:** In a finite frame, only finitely many distinct open sublocales occur; intersections of open sublocales are open. Hence every fitted sublocale is open. Therefore every *closed* fitted sublocale of a finite locale is clopen. For our U this can simplify classification, but one must still check that the relevant clopen blocks are precisely the comparability-component squares before promoting a full finite classification.

**Consequence:** U fitted ⇒ D=U is **false**, already for finite coherent frames. In this example U=F is also total (all real-valued continuous maps are constant), so it does not settle the separate question D=U ⇒ U=F.

## 5. Fitting hull and functional relation (21 October, working proof)

For every locale, D⊆U⊆fit(U)⊆F. The final inclusion follows from **F fitted**: F=⋂_{f:X→R}Eq(fπ₁,fπ₂); the real locale has fitted diagonal, pullbacks preserve fitted sublocales, and intersections of fitted sublocales are fitted. As U⊆F, monotonicity of fitting implies fit(U)⊆fit(F)=F. Record as a **working categorical proof**, with verification of arbitrary sublocale pullback/intersection conventions before publication.

This supplies an intermediate (generally nonclosed) relation fit(U). Further equality fit(U)=F or strictness requires investigation.

## 6. Coherent compact-lattice formulation (21 October, working proof)

For coherent L=Id(D), D=K(L), define u⊥_f v (u,v∈D) iff some c,d∈D satisfy c∨d=1, u∧c=0, v∧d=0. This agrees with u*∨v*=1 in L, by compact generation and compactness of 1.

Then D_reln(L)=U(L) (here D_reln denotes fitting-of-diagonal, *not* the compact lattice D) iff for every finite compact cover k₁∨...∨kₙ=1 and every pair P,Q of prime filters of D, either some k_i∈P∩Q or there exist u∈P,v∈Q with u⊥_f v.

Equivalent purely finitary identity: for every such cover there exist finitely many u_j⊥_f v_j such that 1=∨_i(k_i⊠k_i)∨∨_j(u_j⊠v_j) in the bounded-distributive-lattice coproduct D ⨿ D. The equivalence uses K(L⊕L)≅D⨿D and the compactness of 1. Both forms are **working proofs**, not recognized named axioms or novelty claims.

**Separate future problem:** D_reln=U ⇒ U=F? Not assumed. Also examine whether fit(U)=F, and if not find a strict intermediate example.

## 7. fit(U) is in general strictly smaller than F (21 October 2026)

**Theorem (working proof).** There exist spatial locales X for which fit(U_X) ⊊ F_X.

**General closed-point lemma.** If S=C(d) is a closed sublocale of a locale Y and p:1→Y is a *closed point* outside S, then p is outside fit(S). Indeed, the closed singleton sublocale {p} has open complement O(e); p∉C(d) entails d∨e=1 (equivalently C(d)⊆O(e)), and thus fit(S)⊆O(e), which excludes p. Hence fitting a closed sublocale does not add closed points.

Take any **Urysohn but non-functionally Hausdorff T1 space** X (the standard distinction T_{2½} versus functionally Hausdorff; corrected Arens-square-type examples are available). Choose x≠y that no real continuous function separates. Then (x,y) belongs to F but not U, because a,b neighborhoods with disjoint closures exist. The product point (x,y) is a closed point of the *localic* product because x,y are closed points of X and products of closed sublocale embeddings are closed. By the lemma (x,y) is outside fit(U). Consequently fit(U)⊊F, even as localic sublocales; **no product-spatiality assumption** is needed. For every T1 space, the point pairs of fit(U) and U coincide.

**Source caution:** Older versions of the Arens square in Steen–Seebach were reported to have a gap in the Urysohn verification; use an explicitly corrected construction, e.g. the 2023 paper *Enumeration Degrees and Non-Metrizable Topology*, section 3.6.1 (found at https://personal.ntu.edu.sg/kmng/Files/Papers/nonmetriz.pdf), before citing a specific example formally. The mathematical implication requires only the well-established existence of a Urysohn non-functionally-Hausdorff space.

Open: whether fit(U)=U or fit(U)=F under useful coherent/continuous hypotheses. The counterexample above is not asserted to be coherent or continuous.
