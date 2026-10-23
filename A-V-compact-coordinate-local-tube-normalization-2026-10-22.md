# Compact-first tube lemma and two-step local normalization
Date 22 October 2026.

This strengthens the prior compact-top theorem by allowing an arbitrary second-factor frame and by treating relative rectangles inside arbitrary noncompact products.

Let A,B be arbitrary frames, and let S⊆A×B be a lower set. Use the rectangle product A⊕B and write W=∨_{(u,v)∈S}u⊠v. Fix compact a∈A (i.e. every open cover of a has a finite subcover), and arbitrary b∈B.

THEOREM (one compact coordinate). If a⊠b≤W, then (a,b)∈V(H(S)); equivalently, (a,b) has a V→H tree of maximum edge depth TWO, with leaves from S. No spatiality, algebraicity or continuity of either ambient frame required. The symmetric assertion holds if b is compact, with H→V.

Proof sketch with finite tube formula and proper projection.

1. Restrict to open sublocales A_a=↓a and B_b=↓b. First factor A_a is a compact locale (its top a is compact in A). The restricted rectangles (a∧u,b∧v) cover top in A_a⊕B_b.

2. Let X be an arbitrary compact locale, Y an arbitrary locale. For a finite family of rectangles (u_i,v_i) in O(X)×O(Y), with w_F=∨_{i∈F}u_i⊠v_i, the projection right adjoint Π_*:O(X×Y)→O(Y) has the finite-tube formula
  Π_*(w_F) = ∨_{J⊆F, ∨_{j∈J}u_j=1_X} ∧_{j∈J}v_j.
This actually holds for ALL X,Y, independent of compactness of X.

Proof of finite formula: one inequality is clear: if ∨_J u_j=1, then 1⊠(∧_J v_j)≤w_F. Conversely, generate the finite distributive subframe K⊆O(X) by the first-coordinate u_i. Every point t of the finite T0 space for K has a nonzero locally closed fiber F_t inside X, on which each u_i is either top or bottom according as t∈u_i. If 1⊠v≤w_F, restrict to F_t×Y; nonzero F_t implies projection pullback O(Y)→O(F_t×Y) is injective (by the suplattice retraction: nonzero-open predicate O(F_t)→2 preserves all joins). Thus v≤∨_{i:t∈u_i}v_i for every t. Finite distributivity in O(Y) expands ∧_t ∨_{i:t∈u_i}v_i into joins of finite meets ∧_{i∈J}v_i, where J hits every t, equivalent to ∨_{i∈J}u_i=1_X in K. This establishes the formula.

3. Compactness of X implies the projection X×Y→Y is proper. In frame terms Π_* preserves directed joins. (Standard localic compact-base-change/tube lemma; see literature on proper projections of compact locales.) Express W=∨_{F finite}w_F as directed join of finite rectangle subcovers. Since W=1, we have
  1=Π_*(W)=∨_{F finite}Π_*(w_F)
   =∨_{J finite,∨_{j∈J}u_j=1_X}∧_{j∈J}v_j.
For each such J, the second open v_J=∧_{j∈J}v_j has a horizontal cover of first-coordinate top by u_j (j∈J), with leaf rectangles (u_j,v_J)≤(u_j,v_j)∈S. Thus one vertical cover of second-coordinate top by v_J followed by horizontal covers proves (1,1)∈V(H(S)).

4. Lift the resulting relative tree in A_a×B_b back to A×B. Original leaves are valid since relative first/second coordinates were cut by a,b. This proves the main statement.

Corollaries:
- Any bar on compact locale (a=1 compact, b=1) has V→H depth≤2, even when the second factor is not compact if generalizing to A⊕B.
- For any canonical bar B_w on arbitrary frame L, EVERY compact element a∈L belongs to the H-V-H good-open ideal G_w: since (a,1) is covered by S=D∪B_w in tensor, the theorem gives a V→H certificate for (a,1); hence Φ_w(a)=1. Thus the residual p=∨G_w is at least the join of all compact elements, without an algebraicity assumption.
- For algebraic L, root can be covered horizontally by compact opens a, each having V→H proof. This recovers the bar-root version of the algebraic depth-three theorem with a geometric tube-lemma interpretation.
- This does NOT settle universal depth three on arbitrary frames: L might not have compact opens covering 1. Nor does it assert the continuous-frame three-stage normal form for arbitrary lower relations.

Audit note: The finite-tube formula uses finite spatial K only; F_t is a sublocale of potentially pointless X, and nonzero-factor projection injectivity follows from suplattice tensor properties. The step Π_* Scott-continuous for compact X is an external standard fact; do not conflate it with preservation of arbitrary joins (false).
