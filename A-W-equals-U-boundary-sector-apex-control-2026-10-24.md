# Project A — Regular-boundary localization and a cofinite-apex control example

24 October 2026. New working deductions; not independently audited or priority-checked.

## 1. Canonical nonregular-boundary sector

For every locale, put Q=L⊕L, U=C(d) with d=d_U, D=fit(Delta), W=cl(D), D2 and W2 as in the previous notes. Let

    K=C(d**)=cl(int U),
    G=U ∧ O(d**).

The universal regular-core theorem gives K≤W≤W2≤U. The closed K and its relative open complement G generate U:

    U=K∨G.

Because G is open in U, closure commutes with restricting a sublocale of U to G. Therefore

    W=U  ⇔ D∧G is dense in G,
    W2=U ⇔ D2∧G is dense in G.

Equivalently, W=U iff G≤W, and likewise for W2. A counterexample to binary sufficiency must therefore be located in the canonical nonregular boundary G; a construction with regular-closed U has G=0 and cannot work.

## 2. Boundary-local atomic Booleanization theorem

**Proposition (working).** If the Booleanization of the frame O(G) is spatial (equivalently, a complete atomic Boolean algebra), then

    W2=U ⇒ W=U,

without compactness, spatiality of the square, or atomicity of the Booleanization of O(U).

Proof. Assume W2=U. Every binary diagonal neighborhood is dense in U, hence remains dense when restricted to the open sublocale G. Let h_G,k_G:L→B(O(G)) be the two coordinate frame maps Q→O(G) followed by Booleanization. Then h_G,k_G respect all binary covers. Since their Boolean target is spatial, the spatial-target lemma from the finite-cover morphism note gives compatibility with ALL covers. Hence every diagonal-cover neighborhood is dense in G, so D∧G is dense in G and W=U by §1.

The same argument gives a localized Lindelof/countable-distributivity variant: if L is Lindelof and B(O(G)) is countably distributive, binary density implies full density on G.

This improves the earlier sufficient condition requiring atomicity of B(O(U)); only the nonregular sector matters.

## 3. Explicit compact sober T1 cofinite-apex example

Let Y=R with its usual crowded Hausdorff topology, let Z be an infinite discrete set, and set X=Y⊔Z⊔{p}. Old-part opens have their usual topological-sum traces; a neighborhood of p contains p and all but finitely many old points. This defines a topology. Every p-neighborhood is compact, and X is compact T1 locally compact. It is sober: an irreducible closed set with two distinct old points splits by disjoint old-part open neighborhoods; one with p and just one old point is a two-point finite closed T1 discrete subspace, also reducible. Hence irreducible closed sets are singletons.

Each z∈Z is clopen, while every nonempty Y-open subset is infinite and meets every p-neighborhood. Thus the ordinary Urysohn point relation is exactly

    pt U = (Y∪{p})² ∪ Δ_Z,

and I is properly smaller because distinct real points have disjoint neighborhoods (they are inseparable from p but not from each other). U is proper because each z has a clopen singleton. The localic square is the ordinary product (X locally compact sober); U and I are closed and determined by their point sets.

Importantly, U is REGULAR CLOSED: Y×Y and all diagonal singletons {z}×{z} are ambient open subsets contained in U, and their union is dense in its closed point set. Thus d_U=d_U** and the universal regular-core theorem gives

    I<W=U<X².

Since X is T1, all ordinary points of D are on Delta; if D were spatial, cl D would be I. Therefore D is NONSPATIAL and its nonspatial part is essential to W=U. In fact for disjoint nonempty real intervals A,B, D∧O(A⊠B) is nonzero yet has no ordinary points (by density of D in U and the T1 point formula).

As X is compact, the previous binary theorem also gives D2=D. This example illustrates that **even a compact sober T1 spatial square can have a nonspatial fitted diagonal**; this is not itself an infinitary binary-versus-full counterexample.

A direct density proof: every diagonal neighborhood w contains N_F×N_F for some cofinite p-neighborhood N_F; each nonempty Y-open set meets N_F. Thus w is dense on Y², and w contains all diagonal pairs (z,z). Therefore every diagonal neighborhood is dense in U, independently confirming W=U.

## 4. Construction lesson

A fixed apex p whose every neighborhood meets every nonempty open subset of a crowded core Y forces the core square into int(U), and usually makes U regular closed if no other bad boundary remains. Such a gluing cannot create W<U on that region. A successful noncompact construction must instead produce a Urysohn boundary region G not covered by its regular-closed core, and exhibit a genuinely infinite diagonal-cover obstruction supported there.

No counterexample W2=U but W<U is claimed.
