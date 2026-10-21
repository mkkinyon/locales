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
