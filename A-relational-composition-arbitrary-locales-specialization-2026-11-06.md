# Project A — Arbitrary-locale mixed composition and the canonical specialization relation

6 November 2026. **Working investigation** (proofs in §§1–5 are direct frame/generalized-point arguments; coherent comparison uses the earlier audited coherent results). Literature/priority warning: specialization order on locale maps and its Sierpinski-exponential classifying locale are STANDARD; explicitly Vickers, *Locales and Toposes as Spaces*, Definition 1.10(5) and Fauser–Raynaud–Vickers, *The Born rule as structure of spectral bundles* (2012), §1.3. No novelty claim for their constructions.

The original questions are whether the coherent results I=AB, D=BA, I∘D=ABA, D∘I=BAB have an all-locale counterpart, and whether either mixed composition stays in U∧V outside coherence.

Conventions: L=O(X), Q=L⊕L, Delta diagonal, I=cl Delta=C(d_I), D=fit Delta, U=C(d_U), V=fit I, M=I∧D, J=I∨D; a_i denotes i-th coordinate inverse image in X^n. Compositions are localic images of pullbacks of relations. We adopt x≤y iff every open containing x contains y (f≤g iff f*a≤g*a for every a). This is the convention of the project's spectral order.

## 1. PREVIOUSLY KNOWN: specialization on generalized locale points

For ANY locales T,X, define f⊑g for maps T→X iff f*a≤g*a in O(T) for all a∈L. This is a partial order on Loc(T,X); postcomposition preserves it. This is standard (Vickers, Definition 1.10(5), see https://www.cs.bham.ac.uk/~sjv/LocTopSpaces.pdf).

Fauser, Raynaud and Vickers (2012), §1.3, https://doi.org/10.4204/EPTCS.95.8 , explicitly say that related pairs C⊑D:W→B are classified by the exponential locale B^S, S the Sierpinski locale. Evaluation at ⊥ and ⊤ yields the generic specialization pair. This is precisely the canonical relation we need. The ordered-locale literature of van der Schaaf (2024, arxiv:2406.15406) studies EXTRA order structures on locales; distinguish that from the universal specialization order already present on hom-sets.

## 2. Frame presentation of the graph A=Sp_X

Let A⊆X×X be the quotient imposing, for every a∈L,

    a_1≤a_2.

Then a map (f,g):T→X² factors through A iff f⊑g. Thus A is the image/representing sublocale of the evaluation pair X^S→X×X, not a new object.

A convenient explicit description is

    A = ⋂_{a∈L} [C(a_1)∨O(a_2)].

For an individual frame inequality u≤v in Q, its sublocale is C(u)∨O(v), with nucleus j(q)=(u∨q)∧(v→q). A frame homomorphism h:Q→M factors through this quotient iff h(u)≤h(v): if h(u)≤h(v), then h(j(q))=h(q) for all q, since h(v→q)≤h(v)→h(q); conversely j(v)=u∨v and h(j(v))=h(v) implies h(u)≤h(v).

A is reflexive, transitive and internally antisymmetric: if f⊑g and g⊑f, their inverse image homomorphisms agree on every a, hence f=g. Writing B=A^smile, we have

    A∘A=A, B∘B=B, A∧B=Delta.

These are identities of genuine LOCALIC relations because they are tested by their classifying universal property on arbitrary generalized points T→- and images of their composable-pair locales. A is lax functorial: for h:X→Y, A_X⊆(h×h)^-1(A_Y).

## 3. Universal containment A,B⊆M, and exact hulls

For f⊑g:T→X and any disjoint a,b∈L:

    f*a∧g*b≤g*a∧g*b=0.

Thus A⊆I. For any open cover C of 1, the square-neighborhood pullback obeys

    ⋁_{c∈C} f*c∧g*c = ⋁_{c∈C} f*c=1.

Thus A⊆D. By symmetry B⊆I∧D. Therefore

    Delta≤A,B≤M=I∧D.

Since I=cl Delta and D=fit Delta, and both hulls are monotone,

    **cl(A)=cl(B)=I**,  **fit(A)=fit(B)=D**.

The two opposite specialization orders are canonical common seeds for the two diagonal hulls; they satisfy A∧B=Delta but their closure and fitting hulls are both I and D.

Composition of the order with its converse recovers the COHERENT identities as INCLUSIONS for arbitrary locales:

    A∘B⊆I,     B∘A⊆D.

Proof: x≤z≥y gives f*a∧h*b≤g*a∧g*b=0 for a∧b=0. For x≥z≤y, the common lower generalized point g satisfies ⋁ f*c∧h*c≥⋁g*c=1 for any cover C, so the pair factors through D. Both composites contain Delta (reflexivity). Therefore cl(A B)=I and fit(B A)=D as well.

**Genuine loss outside coherence:** In the compact locally compact sober scattered T1 alpha–beta–gamma example, the localic square is spatial and its sublocales are point-determined; ordinary specialization is equality, so A=B=Delta, while I>Delta. Consequently A B<I. Thus at least I=A B FAILS for arbitrary locales, even compact T1 locales. Do not claim a noncoherent counterexample to D=B A without checking it separately.

## 4. Closed versus fitted relations as modules for specialization

This is an ALL-LOCALE formal lemma:

**Lemma.** For any closed relation C⊆X² and any fitted relation F⊆X²,

    A∘C=C=C∘B,
    B∘F=F=F∘A.

Proof. If C=C(d) for some d∈Q and f⊑g, then for any h:T→X and open d on X² one has d(f,h)≤d(g,h), since d is a join of rectangles. Thus if (g,h) factors through C (i.e. d(g,h)=0), so does (f,h). Similarly C is stable under specialization downward in the second coordinate. The inclusions A C≤C, C B≤C follow by applying these arguments to the generalized points of their composable-pair locales; reverse inclusion follows from reflexivity of A,B.

For fitted F=⋂_{w∈W}O(w), every open w is monotone in both generalized coordinates: if f⊑g, then w(f,h)≤w(g,h). Hence if (f,h) lies in F, so does (g,h); similarly in the second coordinate. This gives B F=F=F A.

**Applications.** I is closed and D fitted, so

    A I=I=I B,     B D=D=D A.

Define R=I∘D, R'=D∘I. Then

    A R=R=R A,    B R'=R'=R' B.

Thus **R is an order distributor** (downward closed in first and upward in second coordinate) for EVERY locale, and R' is the oppositely oriented distributor. This universal conclusion does not require I=A B or D=B A.

As a further universal hull bound, for ANY relation S in X²,

    A∘S∘B ⊆ cl(S),
    B∘S∘A ⊆ fit(S).

Proof: use the module lemma for the closed/fitted hulls and monotonicity of relation composition. For coherent spectral S whose localic representation is patch-closed/coherent, these become equalities by the Priestley point-space up/down saturation machinery; arbitrary equality is not claimed.

## 5. NEW UNIVERSAL mixed-composition inclusion R,R'⊆U

**Proposition (point-free, arbitrary locale).**

    **I∘D⊆U and D∘I⊆U.**

Proof: it suffices to prove the first, since U is symmetric. Let E=I_12∧D_23⊆X³, the localic composable-pair source. Take a far pair a,b in L, a*∨b*=1. The binary cover C={a*,b*} gives D23⊆O(w) where

    w=(a*)_2∧(a*)_3 ∨ (b*)_2∧(b*)_3.

On I12, the open a_1∧(a*)_2 vanishes, since a∧a*=0. Also b_3∧(b*)_3=0 identically. Consequently on E,

    (a_1∧b_3) = (a_1∧b_3∧w)=0.

This holds for every far pair, so E⊆U_13. The image of E under π13 is I∘D, hence I∘D⊆U. Converse follows by swapping coordinates.

This is a universal substantive extension of the coherent comparison. No compactness/coherence/product-spatiality used. Combine with reflexivity (Delta≤I,D) to obtain

    **J=I∨D ≤ R∧R' ≤ R,R' ≤ R∨R' ≤ U.**

We do NOT currently have the analogous arbitrary-locale inclusion R⊆V or R'⊆V. This is the next precise research target.

## 6. Least distributor hull and the coherent comparison

Because A is reflexive/transitive, the **least order distributor** containing J in the left-A/right-A sense exists explicitly:

    Dist_A(J)=A∘J∘A.

Indeed A J A contains J and is stable under A on both sides by A²=A; any other left/right A-saturated relation containing J contains A J A. The opposite distributor hull is B J B.

Since R,R' contain J and are respectively A- and B-saturated by §4, all locales satisfy

    A J A ⊆ R=I D,
    B J B ⊆ R'=D I.

For coherent locales all become equalities: I=A B, D=B A, so R=A B A, R'=B A B. This recovers the previously obtained coherent characterization that R and R' are the least patch-closed order distributors containing J. For general locales the possible strictness of A J A≤I D is now an interesting focused alternative to directly testing R≤V.

Also, A,B≤M but A∨B may be strictly smaller than M already in finite posets: an incomparable pair in the diamond has both common upper and lower bounds and thus lies in M but not A∨B.

## 7. Open targets and research judgment

1. **Main:** Is I∘D⊆V=fit(I) (and hence D∘I⊆V) for arbitrary locales? It holds coherently, follows trivially if D=Delta or I=Delta, and is not settled by the universal proof of R⊆U. Need a proof via all diagonal-neighborhood opens or a pointless counterexample.
2. **Distributor-exactness:** Is A J A=I D universally? Likewise B J B=D I. If not, a counterexample would isolate a genuinely nonspatial compositional excess beyond order saturation.
3. **Other factorization:** When does D=B A hold outside coherence? The identity I=A B is already false for compact T1 non-Hausdorff locales.
4. **Mixed closure:** Compare cl(I D) with W=cl D and U; universal W≤cl(I D)≤U, coherent equality U, and compact scattered T1 alpha–beta–gamma example has cl(I D)=I=W<U. Full arbitrary classification open.

No claimed resolution of the stronger all-locale inclusion I D≤V, no claim to novelty for the specialization relation or its exponential classifying space. This is the recommended research continuation.
