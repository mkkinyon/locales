# Project A — Countable distributivity and binary diagonal descent

24 October 2026. Working proofs pending external audit and literature-priority check.

## Canonical Boolean pair

Write Q=L⊕L and U=C(d_U), with N=O(U)=↑d_U. Let beta:N→B(N) be the double-negation nucleus quotient to its Booleanization and define frame homomorphisms

    h(a)=beta(d_U∨(a⊠1)),
    k(a)=beta(d_U∨(1⊠a)).

For each cover C of L, w_C=⋁_{c∈C} c⊠c, and

    ⋁_{c∈C}h(c)∧k(c)=beta(d_U∨w_C).

This equals 1 iff w_C→_Q d_U=d_U (the restricted open is dense in U). Therefore

    W2=U iff h,k respect finite covers;
    W=U iff h,k respect arbitrary covers.

This is an EXACT reduction for every L, to one canonical complete Boolean target. It is stronger than saying a generic nonspatial target might be necessary.

## Countable distributivity lemma

Call a complete Boolean algebra B countably (binary-)distributive when for every sequence b_0,b_1,...∈B,

    ⋁_{epsilon∈2^N} ⋀_{j∈N} b_j^{epsilon(j)} = 1,

where b_j^1=b_j and b_j^0 is its Boolean complement. This is the usual (omega,2)-distributivity law.

**Lemma (working).** Suppose B is countably distributive, and h,k:L→B are frame homomorphisms respecting finite covers. Then h,k respect EVERY countable cover.

Proof. Suppose C={c_n:n∈N} covers 1 but t=⋁_n h(c_n)∧k(c_n)<1. Put e=¬t>0. Apply the displayed distributivity identity to the interleaved sequence h(c_0),k(c_0),h(c_1),k(c_1),... . There is a nonzero q≤e deciding each h(c_n) and k(c_n): for each n, q≤h(c_n) or q≤¬h(c_n), and similarly for k(c_n).

Since e∧h(c_n)∧k(c_n)=0, no n has q≤both. Since h,k preserve covers, ⋁_n h(c_n)=⋁_n k(c_n)=1, so some n is accepted by h on q and some by k.

Let S={n:q≤h(c_n)}, a=⋁_{n∈S} c_n, b=⋁_{n∉S}c_n. This is a binary cover of 1. Every c_n with n∈S satisfies q≤¬k(c_n), so q∧k(a)=0. Every c_n outside S satisfies q≤¬h(c_n), so q∧h(b)=0. Therefore

    q∧[(h(a)∧k(a))∨(h(b)∧k(b))]=0,

contradicting compatibility with the binary cover {a,b}. QED.

## Lindelof sufficient condition for W=U

**Theorem (working).** Suppose every cover of 1∈L has a countable subcover (L is Lindelof in the frame-theoretic sense), and the Booleanization B(O(U)) is countably distributive. Then

    W2=U ⇒ W=U.

Proof: by the canonical-pair criterion, W2=U makes h,k finite-cover compatible. The lemma implies compatibility for every countable cover. For an arbitrary cover select a countable subcover. The same equality follows for the original cover, hence W=U.

If B(O(U)) is atomic, it is spatial and in particular countably distributive, recovering a stronger unrestricted positive theorem (no Lindelof assumption needed) by the spatial-target lemma. Atomlessness alone therefore does not entail an obstruction; countable distributivity is a separate, potentially useful hypothesis.

## Stress test and limitation

In the Scott-space counterexample X=P(N)\{empty}, the Boolean target RO(2^N) FAILS countable distributivity. The clopen coordinate partitions {A_n,B_n} have no nonzero simultaneous Boolean condition deciding all infinitely many bits; indeed every complete assignment defines at most a singleton of Cantor space, whose regular-open interior is 0. Thus the lemma appropriately excludes that concrete finite-versus-countable cover failure.

The countable distributivity theorem does NOT decide the unrestricted implication W2=U⇒W=U. Its assumptions may fail even for ordinary Lindelof spaces, and the known witness only separates D2,D, not their closed hulls.

## Literature

Arrieta–Picado–Pultr (2022), Lemma 4.4 establishes the arbitrary cover-respecting homomorphism characterization; Lemma 5.4 already defines the full diagonal-neighborhood prenucleus kappa_L. Our Phi agrees with kappa_L, so its definition is not new; the observation Phi(0)=d_U and the derived binary descent identities require their own priority check. Reference: https://www.mat.uc.pt/preprints/ps/p2117.pdf .
