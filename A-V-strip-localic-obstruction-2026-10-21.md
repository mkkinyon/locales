# Universal closed-sublocale obstruction to the dual-far strip equality (21 Oct 2026)

Working exact reduction, not a resolution. The original problem is W=V where V=fit(I), I=C(d), d=d_I in Q=O(X²)=L⊕L, W=meet of open strips s=(k⊠1)∨(1⊠h) with d∨s=1.

Let Σ be these strip elements, Σ^∧ their finite meets, and P(q)=∨_{s∈Σ^∧}(s→q). The nucleus j_W is the transfinite stabilization P^∞; W=V iff every q with d∨q=1 has P^∞(q)=1.

**Localic closure lemma.** For any q,s∈Q,

    cl(C(q)∧O(s))=C(s→q).

Indeed an open a is disjoint from C(q)∧O(s) iff a∧s≤q; the largest such a is s→q.

For a closed sublocale R=C(q) set

    D_loc(R)=meet_{s∈Σ^∧}cl(R∧O(s)) = C(P(q)).

The operator D_loc is monotone and deflationary on closed sublocales. Its transfinite iteration (meets at limits) stabilizes to the greatest fixed closed sublocale R_∞ below R. The fixed points are exactly closed R for which cl(R∧O(s))=R for every individual dual-far strip s: if each O(s) is dense in R, their finite intersections are dense in R, since the dense open subsets of any locale are closed under finite intersection.

**Exact arbitrary-locale theorem:** W=V iff there is NO nonzero closed sublocale R such that R∧I=0 and cl(R∧O(s))=R for every dual-far strip s. Proof: R∧I=0 iff R=C(q) with d∨q=1. A nonzero fixed R forces P^∞(q)≠1. Conversely if such q survives saturation, the greatest fixed sublocale obtained by descending iteration of D_loc from C(q) is nonzero, disjoint I, and has the stated density property.

**Spatial shadow and scope correction:** In an ordinary Hausdorff topological product, the fixed-point condition is equivalent to existence of a nonempty closed off-diagonal relation F such that each disjoint closed rectangle A×B is nowhere dense in F. This is only automatically a theorem about localic X×X when the locale product is represented faithfully by the ordinary spatial product. For general non-locally-compact Hausdorff spaces, the localic product can differ from the ordinary topological product: point-set calculations alone do NOT certify the unrestricted localic conclusion. The intrinsic criterion above has no such gap.

Next test: find a nonzero closed sublocale satisfying the 'every dual-far strip dense' condition, or prove none can exist using the special diagonal-generated structure of d_I. Nonzero fixed sublocales can be pointless. Avoid claiming one-stage failure necessarily implies full failure.
