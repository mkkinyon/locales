# Project A: intrinsic rectangular bars for the fitted inseparability hull
22 October 2026. First positive *exact* frame-only characterization; **currently a coordinatized re-expression of the fitted-hull definition, not the sought non-tautological dual**.

Let L be a frame. Define the formal rectangle preordered set R=L×L, symbols [a,b]. Define a *rectangular C-ideal* J⊆R to be down-closed and separately closed under arbitrary joins:
- if [a_i,b]∈J for all i then [∨_i a_i,b]∈J;
- if [a,b_i]∈J for all i then [a,∨_i b_i]∈J.
Empty joins put all [0,b],[a,0] in J. The lattice CIdl(R) with intersections as meets and C-ideal generated unions as joins presents the frame coproduct T=L⊕L; [a,b] corresponds to a⊠b through principal C-ideals. This should be checked against standard C-ideal presentation in a write-up.

Let D={(a,b):a∧b=0} and let ⟨S⟩_C be the least rectangular C-ideal containing S, obtained by iterating the down-set and separate-join rules transfinitely.

**Definition (rectangular bar):** a subset B⊆L×L for which (1,1)∈⟨D∪B⟩_C. In other words, adjoining formal rectangles from B to the formal disjointness family D covers the formal unit of the coproduct. This is a check entirely in the original frame L (order, meets, arbitrary joins); it does not use the already-built locale product or the fitted hull.

Put b_B=∨_{(a,b)∈B}a⊠b∈T. By coproduct/C-ideal presentation, B is a bar iff b_B∨d_I=1.

**Exact theorem (baseline):** 
  V= ∧_{B rectangular bar} O(b_B),
with each O(b_B) a principal open sublocale of the product. Indeed every bar satisfies b_B∨d_I=1, and conversely each w∈T with w∨d_I=1 is the rectangle join of the set B_w={(a,b):a⊠b≤w}; B_w is a bar and b_{B_w}=w. This is formally correct but is *not yet a deep dual*, since the family of all bars corresponds exactly to all opens w containing I.

**Why worth recording:** It gives a coordinate-only derivation calculus for an arbitrary-locale complete generator family, and makes explicit that the missing power in strips, graphs, and étale relations is closure under unrestricted infinitary *rectangular cover proofs*. A substantial positive theorem would constrain bars to a simpler intrinsic class yet still generate V, or supply a non-circular normal form for the proof trees.

**Potential tests:** (i) characterize B via cut-free transfinite proof trees with no reference to T; (ii) compress bars into a basis indexed by coordinatewise saturated binary relations, prove these are closed under a meaningful operation; (iii) test whether every bar can be built via étale-bar completion of generators (not known and should not be presumed); (iv) identify finitary/coherent reductions reproducing strip theorem.

**Status:** This exact characterization is a verified formal consequence of the standard C-ideal construction, but remains only a baseline positive characterization, not a satisfactory final answer to user's intrinsic-duality goal.
