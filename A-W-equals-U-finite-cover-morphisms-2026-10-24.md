# Project A — Finite-cover compatibility and W = U

24 October 2026. Working results, pending audit and literature-priority check.

## The categorical test

Let L be a frame and Q=L⊕L. Write D=fit(Delta) and D2 for the intersection of the open sublocales corresponding to binary cover squares v(a,b)=a⊠a∨b⊠b, a∨b=1.

For frame homomorphisms h,k:L→M, call the pair *finite-cover compatible* when

    ⋁_{c∈C} (h(c)∧k(c))=1

for every finite cover C of 1. Use *cover compatible* when the condition holds for arbitrary covers.

**Proposition.** The induced frame homomorphism Q→M factors through D2 iff the pair is finite-cover compatible, and factors through D iff it is cover compatible. The first equivalence uses the finite-cut identity (binary compatibility implies compatibility with every finite cover); the second uses the diagonal square-cover presentation of D.

Therefore D2=D iff for EVERY frame M, every finite-cover-compatible pair of frame maps L→M is cover compatible. For the reverse implication test the two projections on D2 itself.

**Literature bridge.** The arbitrary-cover notion and its fitted-diagonal interpretation are in Arrieta–Picado–Pultr (2022), Lemma 4.4 and Theorem 4.5 (https://www.mat.uc.pt/preprints/ps/p2117.pdf). The finitary variation is recorded here as a working extension, not as a novelty claim.

## Spatial targets cannot witness a difference

**Lemma.** Finite-cover-compatible h,k:L→M are cover compatible whenever M is spatial.

Proof. Evaluate at any point p:M→2. Let C cover 1. If no c∈C is accepted by both 2-valued composites, take S={c∈C:(p∘h)(c)=1}. Then a=⋁S and b=⋁(C\S) cover 1, while neither is accepted by both composites, contradicting binary compatibility. Thus the required arbitrary-cover equation holds at every point of M and hence in M by spatiality.

Consequently D and D2 agree on maps from all spatial test locales; any difference requires nonspatial tests.
