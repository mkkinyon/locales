# Counterexample to unrestricted dual-far strip description of V

Date: 21 October 2026. Complete argument, pending external proof audit.

## The proposed identity
For arbitrary locale X, let Q=O(X)⊕O(X), d_I=∨_{a∧b=0}a⊠b, I=C(d_I), V=fit(I). Define Σ the open strips s=(k⊠1)∨(1⊠h) with d_I∨s=1. Let W=meet_{s∈Σ}O(s). General V⊆W. We construct countable Hausdorff spatial X with V≠W.

## Construction
Let L,R be disjoint open copies of Q_rationals, indexed ℓ_t,r_t. Enumerate base intervals J_n of Q. Choose pairwise disjoint closed discrete infinite rational sets A_n,B_n⊂J_n (rational sequences converging to pairwise distinct irrationals). Add z_n and give it neighborhoods whose L-parts contain a tail of ℓ_{A_n} and R-parts contain a tail of r_{B_n}. The ℓ/r copies retain usual open subspace topologies. X=L⊔R⊔Z is countable Hausdorff; Z={z_n} closed and discrete, since L∨R open and z_n admit row-specific separating neighborhoods. X is not locally compact; its localic square may be nonspatial (indeed L×loc R≅Q×loc Q is nonspatial).

Let Y=Q_rationals and g:Y→X×loc X, t↦(ℓ_t,r_t). Write g*:Q→O(Y). Define q=∨{u⊠v:u_L∩v_R=∅}; it is the largest open annihilated by g*. Let S=C(q) be closure of image, nonzero.

## Dual-far strips dense in S
For each dual-far strip s=(k⊠1)∨(1⊠h), closed C(k),C(h) are disjoint as ordinary subsets (as their localic product avoids I, and every diagonal point belongs I). If g*(s) missed a nonempty rational interval J, then ℓ_J⊆C(k) and r_J⊆C(h). Pick basis interval J_n⊆J: z_n is a common closure point of these two projections, contradicting disjoint C(k),C(h). Thus g*(s) dense in Y. If t∧s≤q, then g*(t)∧g*(s)=0, giving g*(t)=0 and hence t≤q. Consequently s→q=q, i.e. c(S∧O(s))=S for all s∈Σ. This makes S a fixed nonzero closed sublocale for the transfinite strip saturation.

## THE DECISIVE LOCALIC COVER: q∨d_I=1
Put e=L∨R in O(X), let Z=C(e), a closed discrete sublocale. The open square e⊠e decomposes into L⊠L, L⊠R, R⊠L, R⊠R. The three rectangles except L⊠R lie in q because v=L has empty right trace or u=R has empty left trace. The remaining L⊠R lies in d_I because L∧R=0. Therefore e⊠e≤q∨d_I.

Let E=C(q∨d_I). Then E≤C(e⊠e). In the sublocale lattice,
 C(e⊠e)=C(e⊠1)∨C(1⊠e)
       =(Z×loc X)∨(X×loc Z).
Since Z is discrete, Z×loc X and X×loc Z are coproducts of copies of X and spatial. The finite join of spatial sublocales is spatial: its frame embeds subdirectly into the product of their spatial frames. Hence C(e⊠e) is spatial, and its closed sublocale E is spatial.

Every ordinary pair (x,y) lies in open q∨d_I. If (x,y) is outside the closed topological graph F={(ℓ_t,r_t):t∈Q}, it has an open rectangle disjoint from F, hence that rectangle's g* inverse image is empty, and it lies in q. If (x,y)∈F, its coordinates are distinct, so Hausdorffness supplies disjoint neighborhoods and (x,y) lies in d_I. Thus E contains no point. Since E is spatial, E=0. Consequently q∨d_I=1, and S∧I=0.

## Conclusion
S=C(q) is nonzero, disjoint from I, and every dual-far strip is dense in S. By the exact fixed-closed-sublocale criterion, the strip meet W strictly exceeds V=fit(I). Thus the unrestricted intrinsic dual-Urysohn formula proposed for V is FALSE, already for a countable Hausdorff locale. Compact/coherent theorem remains valid; no contradiction because this X is noncompact and noncoherent.

## Audit checklist
1. Explicit definition/topology of z_n; verify A_n,B_m all closed disjoint sets in Q, and neighborhoods for z_n,z_m separate.
2. F is closed in ordinary X×top X: all (z_n,z_m) separated from rational graph using disjoint neighborhoods of A_n and B_m, likewise mixed points.
3. q is largest g*-annihilated open (rectangles generate coproduct).
4. s→q=q for all dual-far strips via rational interval density.
5. Z closed discrete, products Z×loc X spatial; finite join spatial (subdirect product argument).
6. C(e⊠e)=Z×loc X∨X×loc Z, E spatial and point-free, hence zero.

Novel argument should be independently audited before publishing the project as final.
