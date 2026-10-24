# Project A — Regular bar filters: rank-two regular generation when the localic square is spatial

24 October 2026. **NARROW EXTRA SEGMENT AFTER THE BOUNDED THREE-SEGMENT FILTER TRIAL.** The universal conjecture B_fin^{##}=B is NOT proved or refuted. This segment establishes a strong sufficient criterion: closed-point detection of locally closed apartness residuals forces B_2^{##}=B. A particularly natural case is sober T1 X with SPATIAL localic square. It also identifies the necessary nature of any counterexample: for sober T1 X, failure of finite-bar regular generation must involve a NONZERO POINTLESS locally closed sublocale of the localic square, invisible to ordinary product points. New theorem is internally checked, not externally audited. It is not a full intrinsic characterization of V in O(X).

## 1. Setup

Let X be a topological space, L=O(X), Q=L⊕L=O(X×locX), and
  d=∨_{u∧v=0}u⊠v.
A bar is w with d∨w=1. Let B_n be the filter of bars admitting rectangular separation trees of rank≤n, and B the filter of all bars. For a filter F⊆Q, set
  F^#={z∈Q:∀w∈F, z∨w=1}.
Then B# contains ↑d and in fact B=(↑d)^#.

The **closed residual** of z is the closed sublocale C(z) of Q. For any z,
  d≤z iff C(z)∩O(d)=0.
Proof: the meet is the locally closed sublocale with open-closed support C(z)∩O(d), whose nucleus/top collapse is equivalent to d≤z. An ordinary point of C(z)∩O(d) is a locale point p of Q with p(z)=0, p(d)=1.

## 2. Universal point-avoidance lemma at rank TWO

**LEMMA.** Let x,y be CLOSED points of X (i.e. X\{x} and X\{y} are open) admitting disjoint open neighborhoods U∋x,V∋y. Then
   w_(x,y)=((X\{x})⊠1)∨(1⊠(X\{y}))
is a bar with a rectangular H-V certificate of depth≤2, and the ordinary product point p=(x,y) does not belong to O(w_(x,y)).

Proof. At a horizontal root cover the first coordinate by X\{x} and U. The first branch is a w-leaf. Beneath U, split vertically into X\{y} and V. The first is a w-leaf, and (U,V) is a disjointness leaf because U∩V=∅. Thus w∨d=1 in the FULL FRAME COPRODUCT. Since both complements omit their respective closed points, p(w)=0.

No claim about spatiality of the localic product is used.

## 3. Main point-detection criterion

Assume the following property, **closed-point detection of apartness residuals**:

  (CPD) For every z∈Q with d≰z, the nonzero locally closed sublocale C(z)∩O(d) contains an ordinary product point (x,y) such that both x,y are closed points of X.

Then
   **B_2^#=↑d, and B_2^{##}=B.**

Proof. Let z∈B_2^#. If d≰z, CPD supplies p=(x,y) with p(z)=0,p(d)=1. The second condition yields disjoint open neighborhoods U∋x,V∋y because d is the join of their disjointness rectangles. The rank-two bar w_(x,y) from §2 has p(w)=0, hence z∨w≠1, contradiction. Therefore z≥d, proving B_2^#⊆↑d. Conversely z≥d implies z∨w=1 for every bar w, so ↑d⊆B_2^#. Double supplementation yields B_2^{##}=(↑d)^#=B.

As a geometric equivalent, CPD says that the region O(d) is *closed-point detecting relative to closed sublocales* of the localic square. It is weaker than requiring the entire square spatial and every point closed, but stronger than ordinary pointwise density of O(d).

**COROLLARY.** If X is SOBER and T1, and X×locX is SPATIAL, then CPD holds (every locale point of X is an ordinary T1 point, and spatiality gives a point whenever d≰z). Therefore
  **B_2^{##}=B**
on every such X.

There is no claim that V_2=V or V_2=I under these hypotheses. Regular completion may collapse a strict fitted hierarchy: it is stronger than strongly exact completion.

## 4. Exactly what can go wrong in a nonspatial localic square

Let X be sober and T1 but DO NOT assume X×locX spatial. If z∈B_2^#, then NO ORDINARY product point can belong to C(z)∩O(d): such a point would have two closed coordinate points and the rank-two avoidance lemma would contradict z∨w=1. Therefore:

  **If B_2^#≠↑d, there is z with d≰z such that**
  **R_z=C(z)∩O(d) is a NONZERO POINTLESS sublocale.**

This is a NECESSARY condition, not sufficient to defeat regular completion. To falsify B_fin^{##}=B requires still more: a nonzero closed sublocale R⊆V_fin disjoint from I=C(d), or equivalently an open z supplementing every finite bar but failing to supplement SOME genuine bar. These are different obstructions. In particular failure of B_2^{##}=B does not imply failure of B_fin^{##}=B.

The result does NOT say "any nonspatial square yields a counterexample." A nonspatial square may have no relevant locally closed pointfree residual, and the two-generic-point space already has B_fin^{##}=B by a separate theorem.

## 5. Connection with the regular-filter trial

The previous three-segment analysis proved on the generic-point K-fan counterexample X0 that
  SEcl(B_fin)⊊B_fin^{##}=B.
That space is sober T0 but NOT T1, so §3 does not subsume that proof. Its rank-omega excluded product point p=(ell,r) is OPEN but not CLOSED, and finite bars eliminate the closed component rectangles in its specialization closure. This exemplifies how regular completion can erase a residual that strongly exact completion retains.

For sober T1 locales with spatial squares we have an even stronger, simpler conclusion B_2^{##}=B. The remaining unresolved universal problem is therefore inherently POINTFREE: any T1 counterexample would require the failure of closed-point detection, not merely a high finite separation-tree rank on ordinary point pairs.

## 6. Assessment and allocation

The universal conjecture
   B_fin^{##}=?B  for arbitrary locales
remains OPEN. The exact closed-sublocale criterion from segment 1, the complete generic-point example from segment 3, and the spatial-square theorem above provide enough structural guidance to record this as a distinct future problem.

This extra segment does NOT produce a characterization of V intrinsic solely to L avoiding the frame coproduct/bar calculus. It justifies **pausing the strongly-exact/regular-filter route now** and returning to the wider I,U,D,V,F hierarchy, unless a genuinely new method for constructing/detecting pointless closed residuals appears.
