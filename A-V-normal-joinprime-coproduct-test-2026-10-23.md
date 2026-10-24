# Project A: testing join-prime top under frame coproducts

23 October 2026. **Partial positive theorems and exact obstruction; (6) still UNRESOLVED for arbitrary frames.** This is a bounded follow-up to A-V-normal-prime-top-directed-square-test-2026-10-23.md. All claims are ordinary frame-coproduct calculations; no pointwise spatiality argument is used.

## Question

If 1_L is FINITELY join-prime (a∨b=1 ⇒ a=1 or b=1), must 1_(L⊕L) also be finitely join-prime? Call this (JP×). This is strictly stronger in form than the desired normal-frame conclusion V(L)=U(L)=X²: failure of (JP×) yields a proper DIAGONAL neighborhood, but not necessarily a proper I-bar.

## 1. A useful necessary consequence of failure

Let δ*:L⊕L→L be diagonal pullback. If u,v<1_Q but u∨v=1_Q, then δ*u∨δ*v=1_L. Join-primality of 1_L gives δ*u=1 or δ*v=1. Hence there exists a PROPER open diagonal neighborhood in Q, and
   (JP× fails) ⇒ D(L)=fit(Δ) < X².

CAUTION: this does not prove V<X² because an arbitrary proper diagonal neighborhood need not contain I; the stronger V question cannot be settled merely by refuting (JP×).

## 2. The finitary rectangle sublattice cannot reveal failure

If 1_L is finitely join-prime and
   1_Q=⋁_{i=1}^n(a_i⊠b_i),
apply δ* to obtain 1_L=⋁_i(a_i∧b_i). Finite join primality gives one term a_i∧b_i=1, hence a_i=b_i=1, so the rectangle itself is top.

Therefore ANY failure of (JP×) must use two PROPER opens u,v whose RECTANGULAR PRESENTATIONS jointly cover 1_Q only via an ESSENTIALLY INFINITE family, no finite subcover. Thus (JP×) is automatic if Q is compact. (As expected, compactness of L implies compactness of Q.)

## 3. One factor with completely join-prime top

Let A,B be nontrivial frames, with top of A COMPLETELY join-prime and top of B FINITELY join-prime. The characteristic map ε:A→2, ε(a)=1 iff a=1, is a frame homomorphism. Its coproduct-with-identity extension
   e=ε⊕id_B:A⊕B→2⊕B≅B
satisfies:
   e(w)=1_B ⇒ w=1_(A⊕B).
Indeed write w=⋁_i a_i⊠b_i; e(w)=⋁_{i:a_i=1_A}b_i; all those 1_A⊠b_i are themselves below w, so 1_A⊠e(w)≤w. Hence e reflects the top.

If u∨v=1 in A⊕B, applying e and join-primality of top_B forces e(u)=1 or e(v)=1, and thus u=1 or v=1.

**THEOREM 1.** Completely join-prime top in one factor and finitely join-prime top in the other imply finitely join-prime top in their coproduct.

Compact + finitely join-prime top implies completely join-prime top (a cover has a finite subcover, then a top member), so compact join-prime A satisfies the hypothesis. This requires no spatiality, even for the second factor.

## 4. Exact arbitrary-Alexandrov-factor theorem

Let P be a NONEMPTY poset and B any nontrivial frame. There is an explicit frame isomorphism
  Up(P)⊕B ≅ Mon(P,B),
where Mon(P,B) is the frame of coordinatewise monotone functions P→B, join/meet pointwise. This follows from the decomposition W=⋁_{p∈P}(↑p⊠W_p) and the frame-coproduct universal presentation, as in A-V-normal-compact-envelope-fitted-base-change-2026-10-23.md.

**THEOREM 2.** 1_(Up(P)⊕B) is finitely join-prime if and only if
    (a) P is downward DIRECTED, and
    (b) 1_B is finitely join-prime.

Proof ⇐: If f∨g=1 in Mon(P,B), then f(p)∨g(p)=1_B for all p, so for every p either f(p)=1_B or g(p)=1_B. The sets
   U_f={p:f(p)=1_B}, U_g={p:g(p)=1_B}
are UPSETS covering P. Downward directedness says the top of Up(P) is finitely join-prime: if two proper upsets U,V covered P, choose x∉U,y∉V and common r≤x,y; then r lies in neither. Hence U_f=P or U_g=P, so f=1 or g=1.

Proof ⇒: constant B-valued functions embed B in Mon(P,B) (nonempty P), so its prime-top property forces B prime-top. Also 0/1-valued monotone functions embed Up(P), so Up(P) prime-top; this is equivalent to P being downward directed as above.

Consequently (JP×) holds for EVERY Alexandrov frame Up(P) with prime top, including arbitrary infinite downward-directed P with no least element, without assuming compactness/spatiality of the other factor. This extends Theorem 1 substantially: neither factor needs a completely join-prime top, and B may be pointless/noncompact.

## 4a. Continuous frames: square as ordinary localic product

For a classically continuous frame L, the corresponding sober space X is locally compact, and the localic square agrees with the usual topological square. If top L is finitely join-prime, then any two nonempty closed subsets of X meet. Given nonempty closed subsets C,D of X×X, choose (x,y)∈C and (u,v)∈D. The ordinary closed sets cl{x},cl{u} have a common point z, and cl{y},cl{v} have a common point t. Their product (z,t) belongs to C∩D by closedness under specialization. Thus X×X is ultraconnected, and top of Q join-prime. This is another positive case (already implicit in earlier spatial-square theorems), not an arbitrary pointfree proof.

## 5. No general answer yet

Search of localic-product and frame-coproduct literature did not produce an immediate general preservation theorem or an explicit failure for noncontinuous, nonspatial prime-top frames. The two elementary arguments above rely on a generic-bottom section or the explicit monotone-function presentation and do NOT generalize to an arbitrary frame L whose top is join-prime but not completely join-prime.

A negative example to (JP×), if one exists, must involve:
- essentially INFINITE rectangle cover in Q,
- at least one PROPER open diagonal neighborhood by §1,
- a noncompact, non-Alexandrov/noncontinuous phenomenon (the normal top-prime condition excludes compact and continuous spatial-product examples),
- but not necessarily a proper bar for I, so would not automatically refute normal⇒V=U.

The full problem remains OPEN at the end of this segment; do not mark (6) solved.
