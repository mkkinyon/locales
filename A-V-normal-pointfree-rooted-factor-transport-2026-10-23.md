# Project A: normality without product spatiality; rooted-factor transport theorem

23 October 2026. **Working new theorem; frame-coproduct proof given. Independently audit before publication.** This note does NOT assert that every normal frame satisfies V=U.

## 0. Definitions and universal reduction

Let X be a locale, L=O(X), Q=L⊕L. Write I=cl(Δ)=C(d_I), D=fit(Δ), U=C(d_U), V=fit(I), and F functional equivalence.

For EVERY locale, D⊆V because Δ⊆I and fitting is monotone. Also D⊆U and I⊆U. Therefore
    D=U ⇒ V=U
even without normality: D=U makes U fitted; I⊆U then V=fit(I)⊆fit(U)=U; conversely D⊆V.

For normal L, U=F by the pointfree Urysohn lemma, and AN1 yields V⊆V2=U. Thus:
    D ⊆ V ⊆ U=F;
    D=U ⇒ V=U=F.

The unrestricted problem normal L ⇒ V=U remains OPEN and is potentially weaker than the older open normal L ⇒ D=U. Known positive cases compact normal frames, continuous normal frames, normal/subfit frames, normal frames with spatial square. Do not infer product spatiality from normality.

## 1. An arbitrary-cover shrink criterion

Let C={c_i} cover 1 in L. Suppose a family r_j,s_j satisfies
    ⋁_j r_j=1,   r_j≺s_j≺c_{i(j)},
where ≺ is rather-below (a*∨b=1). Then:
    1 = d_U ∨ ⋁_i (c_i⊠c_i)
in L⊕L.

Proof: s_j≺c_i implies s_j*∨c_i=1. Also r_j≺s_j implies r_j*∨(s_j*)*=r_j*∨s_j**=1, so r_j⊠s_j*≤d_U. Thus
    r_j⊠1=(r_j⊠c_i)∨(r_j⊠s_j*)≤(c_i⊠c_i)∨d_U.
Join in j.

Hence if every cover of L admits this two-step rather-below refinement, D=U. A normal finite open cover has the required shrinking; a regular frame has it for any cover, by iterating regular-below decompositions. Normality alone need not furnish such refinements: the normal noncompact upper-set frame of P=omega^op has a cover by its finite initial segments, but no nonzero r≺s≺c_i for these proper initial segments (every nonzero open is dense, so r≺s iff s=1 or r=0). Yet D=U=whole for the chain. Thus this criterion is sufficient, not necessary.

## 2. Rooted-factor transport theorem (arbitrary possibly pointless Y)

Let P be a NONEMPTY FINITE poset with least element 0. Let Y be any locale, B=O(Y), X=P×_locY, and π:X→Y the projection.

The frame coproduct presentation is
    O(X) ≅ Mon(P,B),
    O(X×_locX) ≅ Mon(P²,B⊕B),
with monotonicity in both P coordinates. Write A_p∈B for each open A∈O(X) and w_{p,q}∈B⊕B for each open w of the square. Let R_π=(π×π)^{-1}(R_Y) for any sublocale R_Y⊆Y².

**THEOREM.** With NO assumption on the points or compactness of Y, the following equalities hold *as sublocales*:
    D(X) = π^{-1}D(Y),
    U(X) = π^{-1}U(Y),
    V(X) = π^{-1}V(Y),
    F(X) = π^{-1}F(Y).
Here π^{-1} is shorthand for inverse image along π×π. Generally I(X) is strictly smaller than π^{-1}I(Y).

### 2.1 Fitted diagonal D

Let w∈O(X²) be a diagonal neighborhood, δ_X^*w=1_X. At root 0:
    δ_Y^*(w_{0,0})=1_Y.
Thus D(Y)⊆O(w_{0,0}). Since (0,0)≤(p,q), monotonicity gives w_{0,0}≤w_{p,q}; hence D(Y)⊆O(w_{p,q}) for EVERY (p,q). Consequently π^{-1}D(Y)⊆O(w). Intersect all such w:
    π^{-1}D(Y)⊆D(X).
Conversely Δ_X⊆π^{-1}Δ_Y. Since pullback preserves intersections of sublocales and open sublocales, π^{-1}D(Y) is fitted; therefore D(X)=fit(Δ_X)⊆π^{-1}D(Y).

### 2.2 Urysohn relation U, direct separation-open identity

For A∈Mon(P,B) put T_A=⋁_{p∈P}A_p. Because P has a least element, its pseudocomplement satisfies
    (A*)_0 = (T_A)*_B.
Proof: an open C disjoint from A has C_0≤C_p≤(A_p)* for all p, so C_0≤(T_A)*; conversely the constant open (T_A)* is disjoint from A and witnesses the reverse inequality.

Thus if A*,C* cover 1 in Mon(P,B), evaluation at 0 gives
    (T_A)*∨(T_C)*=1 in B.
For each p,q, A_p⊠C_q≤T_A⊠T_C≤d_U(Y). Every generator A⊠C of d_U(X) lies under (π×π)^*d_U(Y), yielding one inequality.

Conversely, if a*∨b*=1 in B, the CONSTANT monotone opens A_p=a,C_p=b satisfy A*=constant(a*), C*=constant(b*). Hence their rectangle (π×π)^*(a⊠b) is a d_U(X) generator. Joining gives the reverse inequality:
    d_U(X)=(π×π)^*(d_U(Y)).
Taking closed complements proves U(X)=π^{-1}U(Y).

### 2.3 Inseparability relation at the root, hence V

Similarly, evaluation of d_I(X) at root/root gives
    (d_I(X))_{0,0}=d_I(Y).
The ≤ direction follows because disjoint A,C in Mon(P,B) have disjoint root values A_0,C_0. The ≥ direction follows from constant disjoint pairs in B.

If w is any BAR for I(X), then w∨d_I(X)=1. Evaluating at root/root yields
    w_{0,0}∨d_I(Y)=1,
so w_{0,0} is a bar for I(Y). Thus V(Y)⊆O(w_{0,0}) and, by monotonicity, V(Y)⊆O(w_{p,q}) for all p,q. Therefore π^{-1}V(Y)⊆O(w) for every bar w, whence
    π^{-1}V(Y)⊆V(X).

Conversely I(X)⊆π^{-1}I(Y) by functoriality of I. Since π^{-1}V(Y) is fitted and contains π^{-1}I(Y), it contains fit(I(X))=V(X). Thus equality.

### 2.4 Functional relation F

For every f:X→R, write f_p^*:O(R)→B for the coordinate frame homomorphisms. These obey f_0^*(u)≤f_p^*(u) for all real opens u because 0≤p.

**Lemma.** If A is a REGULAR frame and h,k:A→B are frame maps satisfying h≤k pointwise, then h=k. Proof: for a≺b in A, h(a*)∨h(b)=1; k(a)∧h(a*)≤k(a)∧k(a*)=0 (since h(a*)≤k(a*)); hence k(a)≤h(b). Express b as join of elements a≺b by regularity and conclude k(b)≤h(b). Thus equality.

Applying the lemma to A=O(R) shows f_p^*=f_0^* for every p. Therefore f^*:O(R)→Mon(P,B) is constant, i.e. every real-valued locale map on X factors uniquely through π. Thus the real-function evaluation kernel pair F(X) is precisely π^{-1}F(Y).

### 2.5 Normality transfers from Y

If B is NORMAL, then O(X)=Mon(P,B) is normal: for A∨C=1_X, evaluate at 0 to get A_0∨C_0=1_B. Choose u,v in B with A_0∨u=1=C_0∨v and u∧v=0. Their constant functions are disjoint opens satisfying A∨u=1=C∨v. No spatiality needed.

As normal B entails U(Y)=F(Y), the transport theorem gives U(X)=F(X). If in addition U(Y)=Δ_Y (e.g. B is regular), then
    D(X)=U(X)=V(X)=F(X)=K_π
because D(Y)⊆U(Y)=Δ_Y and contains Δ_Y, so D(Y)=Δ_Y; and V(Y)=Δ_Y because it lies between I(Y)⊆U(Y)=Δ_Y and U(Y) fitted under normality.

## 3. Explicit pointless, noncompact, normal example

Choose P={0<a, 0<b}, the finite bottom fork. Let B=RO(R), the atomless complete Boolean algebra of real regular-open sets.

B is normal and completely regular. Its locale Y has NO points (a completely prime filter of a complete Boolean algebra produces an atom); Y is NONCOMPACT since (-n,n) have join top and no finite subjoin top. Therefore X=P×Y is pointless, noncompact, normal, and not covered by spatial-product arguments.

As B is regular, D(Y)=U(Y)=V(Y)=F(Y)=Δ_Y. By transport,
    D(X)=V(X)=U(X)=F(X)=K_π.
But I(X)⊊K_π: the two generalized sections s_a,s_b:Y→X satisfy πs_a=πs_b=id_Y, so t=(s_a,s_b):Y→X² factors through K_π. The disjoint opens ({a}×Y), ({b}×Y) show t^*d_I(X)=1_B, whence t^*I(X)=empty, proving strictness.

This gives a genuinely pointfree NONCOMPACT NORMAL example with
    I(X)⊊D(X)=V(X)=U(X)=F(X),
where Δ_X⊊I(X) may be evaluated separately; the displayed strictness is sufficient.

## 4. What remains genuinely open

The general statement
    L normal ⇒ V(L)=U(L)=F(L)
has not been proved or refuted here. It follows from the (older, still open) normal⇒D=U implication but could be strictly weaker. The project note A-noncompact-normality-D-U-2026-10-21.md already identified the infinite-cover/nonspatial obstacle; do not mistake positive rooted-factor examples for a general argument.

A plausible next approach is to characterize how the normal frame's completely regular reflection handles arbitrary bar neighborhoods, or seek a normal frame with a genuinely infinite tensor-cover obstruction. Any counterexample must be noncompact, noncontinuous, nonsubfit, and cannot be constructed solely by taking a rooted finite Alexandrov product with a normal base that already has V=U.

Relevant existing project references:
- A-noncompact-normality-D-U-2026-10-21.md
- A-external-audit-reconciliation-2026-10-21.md (compact normal iff D=U)
- A-V-almost-normal-rank-two-equals-F-2026-10-23.md
- A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md
- A-hierarchy-first-results.md
