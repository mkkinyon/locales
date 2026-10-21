# Preservation of I = U under arbitrary frame coproducts

**20 October 2026.** Working note; proof in arbitrary frames, including pointless and noncontinuous frames. This strengthens the coherent coproduct result proved first.

## Definitions

For a frame `L`, write `L ⊕ L` for the coproduct in `Frm`, and `a ⊠ b` for pure rectangles. Set

```
d_I(L) = ∨ {a ⊠ b : a ∧ b = 0}
d_U(L) = ∨ {a ⊠ b : a* ∨ b* = 1}.
```

The closed relations agree iff `d_I(L)=d_U(L)`. We call `a,b` **far** when `a*∨b*=1`.

## Lemma 1 (farness is preserved by frame maps)

If `h:A→B` is a frame homomorphism and `a*∨b*=1` in `A`, then `h(a)*∨h(b)*=1` in `B`.

Indeed `h(a*)≤h(a)*`, `h(b*)≤h(b)*`, and `h(a*)∨h(b*)=1`.

Consequently, the induced homomorphism `h⊕h:A⊕A→B⊕B` sends `d_U(A)` below `d_U(B)`. In particular, if `a∧b=0` and `d_I(A)=d_U(A)`, then
```
h(a) ⊠ h(b) = (h⊕h)(a⊠b) ≤ (h⊕h)(d_U(A)) ≤ d_U(B).
```
Note: `h(a),h(b)` need not be far themselves; they merely have a far-rectangle cover in `B⊕B`.

## Lemma 2 (nonvanishing of finite basic coproduct meets)

Let `B=⊕_{i∈J}L_i` with structure homomorphisms `ι_i`. For any finite set `F⊆J` and `a_i∈L_i`,
```
∧_{i∈F} ι_i(a_i) = 0  iff  some a_i=0.
```
For `F=∅` the meet is 1 (provided the coproduct is nondegenerate). This is the standard pure-tensor nonvanishing property of frame coproducts: for two frames, the cp-ideal presentation gives `a⊠b=0` precisely if `a=0` or `b=0`; finite products follow inductively. If one factor is the degenerate one-element frame, the full coproduct is degenerate and the main theorem below is trivial, so assume nondegenerate factors when using the criterion.

## Theorem (arbitrary coproduct closure)

**For any set-indexed family `(L_i)` of frames such that `I(L_i)=U(L_i)` for all `i`, their coproduct `L=⊕_i L_i` satisfies `I(L)=U(L)`.** No algebraicity, coherence, continuity, spatiality or compactness is required.

**Proof.** An arbitrary element of `L` is a join of basic finite-support meets
```
R=∧_{i∈F}ι_i(a_i).
```
This is because these elements contain the structure maps' images and are closed under finite meets, and their joins form a subframe, hence the entire coproduct.

Take `a,b∈L` with `a∧b=0` and write
```
a=∨_s R_s,    b=∨_t S_t
```
as joins of basic finite-support meets below `a` and `b`. For every `s,t`, `R_s∧S_t=0`.

After combining the finite supports and filling omitted coordinates with `1`, Lemma 2 provides an index `j` with `a_j∧b_j=0`, where `R_s≤ι_j(a_j)` and `S_t≤ι_j(b_j)`.

Apply Lemma 1 to `h=ι_j:L_j→L`: since `I(L_j)=U(L_j)`,
```
R_s ⊠ S_t ≤ ι_j(a_j) ⊠ ι_j(b_j) ≤ d_U(L).
```
Finally coproduct rectangles preserve arbitrary joins in each coordinate, so
```
a ⊠ b = ∨_{s,t}(R_s ⊠ S_t) ≤ d_U(L).
```
Therefore `d_I(L)≤d_U(L)`; the opposite inequality always holds. QED.

The argument also covers the empty family: the empty coproduct in `Frm` is the two-element frame, for which equality holds.

## Coherent corollary (the earlier result)

If all `L_i` are coherent and satisfy `I=U`, then the coproduct is coherent and satisfies `I=U`. Coherence of the coproduct follows from the finite-support lattice of compact opens (equivalently, ideal completion of the bounded-distributive-lattice coproduct). Using the coherent characterization `I=U iff K(L) is conormal`, one gets that coproducts of conormal bounded distributive lattices are conormal.

This coherent statement is subsumed by the arbitrary-frame theorem above, but its conormality formulation may be independently useful.

## What is special about the proof?

The finite-support **zero-detection lemma** does the essential work. For each pair of basic disjoint opens, a single coordinate witnesses disjointness. Equality `I=U` in that coordinate supplies an *infinite* far-rectangle cover when needed, and the frame homomorphism `ι_j` transports this cover to the big coproduct. There is no need to make the cover finite, and hence no compactness hypothesis.

This should be audited independently before publication, especially the finite-support nonvanishing lemma and the passage through the induced map `ι_j⊕ι_j`.
