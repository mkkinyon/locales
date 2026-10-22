# Dual farness and an intrinsic compact-strip presentation of V

21 October 2026. New working theorem in coherent locales; independent audit recommended.

Let L be coherent, Q=L⊕L, d_I=∨_{a∧b=0} a⊠b, I=C(d_I), and V=fit(I) (definition unchanged). Let K=K(L).

Define **dual far** compact opens k,h∈K by

    k ⟂^vee h  iff  d_I ∨ (k⊠1) ∨ (1⊠h) = 1_Q.

This says the closed rectangle C(k)×C(h)=C((k⊠1)∨(1⊠h)) is disjoint from I as a sublocale. Diagonal pullback shows dual far implies k∨h=1. On spectral points equivalent to ↑(X\K_k) ∩ ↑(X\K_h)=∅, i.e. no pair of points in the two closed basic subsets has a common generalization.

**Theorem (coherent):**

    V = ⋂_{k ⟂^vee h} O((k⊠1)∨(1⊠h)).

Proof: I_pt is patch-closed in spectral X², hence patch-compact. By Claude's verified compact-open-filter lemma, both sides are coherent, spatial sublocales, and V_pt=↑I_pt. Every dual-far strip includes ↑I_pt, because its closed rectangle is an order downset disjoint from I_pt. Conversely if (x,y)∉↑I_pt, then for each (u,v)∈I_pt, either u not≤x or v not≤y. By spectral compact-open separation find compact open K containing u excluding x, or H containing v excluding y. These vertical/horizontal strips cover I_pt; patch-compactness selects finitely many. Join the corresponding K's into k and H's into h. Then x∉K_k,y∉K_h, and I_pt is contained in (K_k×X)∪(X×K_h). Because that union is spectral open and contains every point of the closed spatial I sublocale, I⊆O((k⊠1)∨(1⊠h)); equivalently dual far. Thus every point outside ↑I_pt is excluded by a dual-far strip, and both sublocales have exactly the same point set. Spatiality proves equality.

Compare U=C(∨_{a*∨b*=1}a⊠b). Ordinary farness implies a∧b=0; dual farness implies k∨h=1. U excludes far OPEN rectangles; V is the intersection of complements of dual-far CLOSED rectangles. The formula does not use fit(I) or D² on its right side and is a genuine intrinsic frame-coproduct presentation in the coherent setting. It provides an internal form for the pointwise Urysohn relation of the Hochster dual.

**Do not generalize without proof:** cofar definition makes sense with arbitrary a,b∈L, but the strip-meet formula is presently proved only for coherent locales, using spectral patch compactness and coherent compact-open-filter spatiality. Investigate a choice-free proof and whether the formula persists for stably compact/other frames. Compare this cofar predicate with normal/conormal lattice separation axioms.

## NEW: Elimination of coproduct from dual farness (compact theorem)

**Theorem (compact frame L).** For any k,h∈L,

    d_I∨(k⊠1)∨(1⊠h)=1
iff ∃a,b∈L: a∧b=0, k∨a=1, h∨b=1.

If L is coherent and k,h compact, a,b can be chosen compact by approximation and compactness of 1.

Reverse direction is universal: (k∨a)⊠(h∨b)=1 and its expansion is bounded by the two strips plus a⊠b≤d_I.

Forward direction: compactness of X² selects finitely many generators a_i⊠b_i of d_I (a_i∧b_i=0), so 1=(k⊠1)∨(1⊠h)∨∨_i(a_i⊠b_i). Restrict to closed rectangle C(k)×C(h), whose frame is ↑k⊕↑h; finite rectangle lemma yields k∨u=1 for u=∨_{S:h∨∨_{i∈S}b_i=1} ∧_{i∈S}a_i. Put v=∧_S∨_{i∈S}b_i. Finiteness gives h∨v=1, and u∧v=0 by a_i∧b_i=0. The case of no eligible S is handled by empty join u=0 and empty meet v=1, forcing k=1. Thus disjoint supplements exist. (The finite rectangle lemma should be included in a publication proof.)

**Consequence (compact L):** L is normal iff for every k∨h=1 the pair k,h is dual far. For coherent frames, compact lattice K is normal iff every covering compact pair is dual far. This clarifies the connection between V dual separation and pm/normality.

**Scope:** The coproduct-free *predicate* extends to all compact frames; equality of V with the meet of dual-far strips has been proved only in coherent frames. No unrestricted fit(I) formula is asserted.
