# Localic product analysis of the rational graph counterexample

22 October 2026 (continuation of 21 October work). Explicitly preserve unresolved cover condition.

Let X=L⊔R⊔{z_n} with two open Q copies and sequence-bridge points z_n as in A-hereditarily-inseparable-closed-relation-2026-10-21.md. Qloc=O(X)⊕O(X), Y=Q (rational numbers as topological locale), and g:Y→X×_loc X map t↦(ℓ_t,r_t), given by its two continuous coordinates. Let g*:Qloc→O(Y) be the copairing frame homomorphism. On rectangles,
g*(u⊠v)=u_L∩v_R,
where u_L={t:ℓ_t∈u} and v_R={t:r_t∈v}.

Put q=∨{w∈Qloc:g*(w)=0}; since every w is a join of rectangles, q can explicitly be expressed as
 q=∨{u⊠v:u_L∩v_R=∅}.
Then g*(q)=0, the closure of its localic image is R=C(q), and R≠0 (since g*(1)=Y, g*(q)=0). The quotient frame of R is ↑q.

**All dual-far strips are dense in R (proved):** For a dual-far strip s=(k⊠1)∨(1⊠h) with d_I∨s=1, its complementary closed rectangle is C(k)×C(h), and that rectangle misses I, so in particular it misses the *pointwise* diagonal. Hence C(k),C(h) are disjoint closed topological subsets of X (no assumptions about the locale product needed for this implication). Then g*(s) is dense in Y: if a nonempty open rational interval J were disjoint from g*(s), then ℓ_J⊆C(k) and r_J⊆C(h), so their X-closures are contained in disjoint C(k),C(h); however for some n, J_n⊆J, both projections accumulate at z_n, contradiction. Thus (g*(s))*=0 in O(Y). For any t∈Qloc with t∧s≤q, g*(t)∧g*(s)=0, hence g*(t)=0 (density), hence t≤q. Therefore s→q=q, i.e. cl(R∧O(s))=R. (This actually holds for every strip arising from disjoint closed C(k),C(h), whether or not its stronger *localic* dual-far criterion holds.)

**The remaining decisive question is one frame equation.** Let d=d_I=∨_{a∧b=0}a⊠b. g*(d)=Y: each (ℓ_t,r_t) has disjoint coordinate neighborhoods because X Hausdorff. Thus q∨d has g*-image Y, but this does NOT prove q∨d=1 in Qloc; g* does not reflect top. R∧I=C(q∨d), so R is disjoint from I iff q∨d=1. Since ordinary topological graph F is closed and misses Δ, the *spatialization* of q∨d is top; but it may be a proper dense open in the nonspatial locale product. Do not infer localic disjointness from ordinary product closedness.

Explicit cover:
  1_Qloc ?= ∨_{a∩b=∅ in O(X)}a⊠b  ∨ ∨_{u_L∩v_R=∅}u⊠v.
A proof of this equality would yield a full unrestricted dual-far strip counterexample (nonzero R, disjoint I, all strips dense). Its failure would reveal an extra purely localic overlap of the diagonal and graph closure, defeating this *particular* lift.

**Important structural caution:** the canonical map from localic product to ordinary space product does not automatically preserve a closed embedding. Whether the product locale is spatial cannot be decided merely by checking pointwise covers. No general claim yet.

Next work: compute coproduct cover using the presentation of O(X), or construct a quotient/frame-valued point of Qloc annihilating both d and q to witness failure.
