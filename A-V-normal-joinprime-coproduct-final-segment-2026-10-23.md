# Project A: final bounded segment on join-prime top under frame coproducts

23 October 2026. **Status: unresolved in arbitrary frames.** User explicitly requested one final segment on (JP×), then move on. This closes the line for now, rather than proposing an indefinite continuation.

## Setup

Let L be a nontrivial frame with finitely join-prime top: a∨b=1 ⇒ a=1 or b=1. Let Q=L⊕L. Recall that Q is represented by rectangular C-ideals A⊆L×L (downward closed and separately closed under arbitrary joins), with (a,b)∈A iff a⊠b lies below the represented open. A,B denote two PROPER C-ideals (corresponding to u,v<1). Their join in Q is the C-ideal closure of A∪B.

## Theorem: rank-two two-color elimination

**THEOREM.** No alternating proof tree of depth ≤2, with all leaves in A∪B, can establish the root (1,1).

Proof for H→V: Root horizontal cover 1=∨_i a_i. At each (a_i,1), vertical cover 1=∨_j b_ij and leaf (a_i,b_ij)∈A∪B. Partition the j's by their color. Since 1_L is finitely join-prime, one of the two color-subfamilies covers 1. Vertical join closure yields (a_i,1)∈A or B. Partition the root children by that color; join-primality again shows one color covers 1, and horizontal join closure gives (1,1)∈A or (1,1)∈B, contradiction. The V→H case is symmetric. Depth 0/1 cases may be padded.

**Consequently**, any witness to u∨v=1 for two proper u,v in Q requires a separation-tree derivation from A∪B of depth ≥3 (possibly transfinite). This strengthens the previously recorded necessity of an infinite rectangular cover. It is a genuine alternating-depth obstruction, but not a resolution of whether such a witness exists.

In saturation notation:
 (1,1)∉H(V(A∪B)) and (1,1)∉V(H(A∪B)).
Here H/V denote single-coordinate arbitrary-join closures and include downward closure. The restriction to two proper C-ideals is essential; no claim for arbitrary starting lower S.

## Exact first open case: H→V→H rank three

For u,v∈Q define the horizontal residual
 r_u(b)=∨{a∈L:a⊠b≤u},  r_v(b)=∨{a∈L:a⊠b≤v}.
These satisfy r_u(b)⊠b≤u and analogously for v.

There is a depth≤3 H→V→H proof of (1,1) from A∪B **iff** there exist opens a_i with ∨_i a_i=1 and, for each i, a cover b_ij of 1 such that
   a_i≤r_u(b_ij)∨r_v(b_ij)  for every j.
The ⇒ direction groups the final horizontal leaves by their colors and uses closure of each C ideal. The ⇐ direction splits a_i into
   a_i∧r_u(b_ij), a_i∧r_v(b_ij)
under each (a_i,b_ij), and uses those as A/B leaves. The V→H→V case is symmetric.

If u,v are proper and top L is join-prime, this rank-three condition cannot be satisfied with a SINGLE root open a_i=1: for each j,
 r_u(b_ij)∨r_v(b_ij)=1
forces one residual to be 1; coloring middle b_ij by that choice and using joinprimality of their cover implies r_u(1)=1 or r_v(1)=1, hence u=1 or v=1. Thus any possible rank-three witness must use an ESSENTIALLY INFINITE proper root cover, together with genuinely variable colored splittings of those proper root opens at the last horizontal stage.

This identifies the precise mechanism at which the rank-two proof fails: finite join-primality applies at the top 1, not to a cover of an arbitrary proper a_i by two colors. No available normality law upgrades it to relative join-primality. The failure is not in the algebra of the residuals, but in synchronizing their final horizontal splits across an infinite middle cover.

## Additional positive classes and caveat

Previous results give (JP×) for:
- one completely join-prime factor and one finitely join-prime factor;
- any downward-directed Alexandrov factor Up(P) with the other factor finitely join-prime, via Mon(P,B);
- frames whose localic square is spatial (notably continuous/algebraic frames), by the point-closure argument.

An additional weaker spatiality observation: if Q is **weakly spatial** in the sense that every nonzero closed sublocale C(w), w<1_Q, contains an ordinary point, then (JP×) follows for L with join-prime top. Indeed every nonzero closed C(a)⊆X also has a point: C(a)×X nonzero closed in Q. If u,v<1_Q cover Q, choose ordinary product points outside u,v; the localic point closures in X of each coordinate meet because top L is join-prime, and each such nonzero closed intersection has an ordinary point by the same weak spatiality property. The resulting coordinatewise common specialization predecessor lies outside both u,v, contradiction. Thus a counterexample must violate even this weak spatiality condition of Q.

IMPORTANT: if (JP×) fails, then D=fitΔ is proper (apply the diagonal map δ*:Q→L to a proper binary cover). This still need not give V=fit(I) proper: a proper diagonal neighborhood need not be an I-bar. No universal implication about V is deduced.

## Closure of the investigation

No general preservation theorem and no explicit counterexample was obtained. A direct targeted web literature search did not identify a source that settles (JP×) for arbitrary nonspatial frames. The new verified contribution is the two-color depth-two exclusion and the exact rank-three obstruction criterion; they should not be inflated into a solution.

Leave (JP×) **DEFERRED** and return to the main point-free separation programme, as requested by the user.
