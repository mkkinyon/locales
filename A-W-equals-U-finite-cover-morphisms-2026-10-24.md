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

## Compact complemented cover theorem

**Theorem (working).** If L admits a cover 1=⋁_i e_i by compact complemented elements, then D2=D. Hence the binary density criterion for W=U is exact in this class even without compactness of 1 or coherence.

Proof. Let h,k:L→M be finite-cover compatible. The binary cover {e_i,e_i^c} forces h(e_i)=k(e_i)=m_i: the images are complemented, and (h(e_i)∧k(e_i))∨(h(e_i^c)∧k(e_i^c))=1 forces agreement.

For any cover C of 1, compactness of e_i yields a finite list c_1,...,c_n∈C covering e_i. Hence {e_i^c,c_1∧e_i,...,c_n∧e_i} is a finite cover of 1. Finite-cover compatibility and meeting with m_i give

    m_i ≤ ⋁_{j=1}^n (h(c_j)∧k(c_j))
        ≤ ⋁_{c∈C} (h(c)∧k(c)).

Join over i: ⋁m_i=h(⋁e_i)=1. Thus h,k respect C. By the categorical test, D2=D.

Corollaries include arbitrary locale coproducts of compact locales and covers by compact clopen sublocales without disjointness. This does not itself imply W=U: it says the binary test detects whether W=U.

## Sharp form of any remaining counterexample

If W2=U but W<U, there is necessarily an infinite open cover C of 1 with no finite subcover and a pure rectangle r=a⊠b such that

    r not≤d_U,   and   r∧w_C≤d_U,

where w_C=⋁_{c∈C}c⊠c. Indeed Phi(d_U)>d_U supplies a diagonal neighborhood with nontrivial implication beyond d_U; refine to a square cover, then choose a rectangle below that implication but not d_U. Finite-cut decomposition would forbid a finite subcover under binary density.

In addition, D2∧O(r) is nonzero and dense in U∧O(r), but has no ordinary points: cl(D2)=U, whereas D∧O(r)=0 and pt(D2)=pt(D). Thus any such example must exhibit a dense pointless residual localized to an open part of U.

## Operator correction

The earlier note's claim that Psi(q)=⋁_{a∨b=1}(v(a,b)→q) is a finite-meet-preserving pre-nucleus was unsupported: binary neighborhoods are not closed under finite meets. Psi is monotone and inflationary, with Fix(Psi)=D2, so its transfinite least-fixed-point construction and the equality W2=U iff Psi(d_U)=d_U remain valid. The earlier repository note has been corrected.

**Status:** All new deductions here are working proofs pending adversarial audit and priority check. The general implication W2=U ⇒ W=U is still open.
