# One-stage dual-far strip saturation fails: countable Hausdorff non-Urysohn example

21 October 2026. Working proof; targeted independent audit recommended.

## Construction
Let X={x,y} ∪ {z_n:n∈N} ∪ {a_{n,m}, b_{n,m}:n,m∈N}. All a,b isolated. Bases:
U_N(x)={x}∪{a_{n,m}:n≥N,m arbitrary};
V_N(y)={y}∪{b_{n,m}:n≥N,m arbitrary};
T_M(z_n)={z_n}∪{a_{n,m},b_{n,m}:m≥M}.
This is a countable Hausdorff scattered space, not Urysohn: all neighborhoods of x and y have closure containing z_n for sufficiently large n. Every nonempty subspace has an isolated point: if it contains any a/b use that; otherwise within {x,y,z_n}, z_n is relatively isolated; if only x,y remains, both relatively isolated. Finite products of scattered spaces are scattered (isolate an element in first coordinate projection, then in corresponding fiber).

## Closed off-diagonal relation
For each n set A_n={z_n}∪{a_{n,m}:m∈N} and B_n={z_n}∪{b_{n,m}:m∈N}. Define F=closure in X² of ∪_{n≠k}A_n×B_k, and W=X²\F. Each (z_n,z_n) has a row-n-only basic rectangle missing the generating union. All other diagonal points admit neighborhoods missing the union because first factor is left type (a,z) and second is right type (b,z), and x,y lie outside the incompatible types. Thus F∩Δ=∅, so W is open diagonal neighborhood (I=Δ because X Hausdorff). However (x,y)∈F because neighborhoods U_N(x)×V_M(y) contain a_{n,m}×b_{k,t} with n≠k large.

## Refutation of one-stage (9)
Let Σ be dual-far strips s=(k×X)∪(X×h) with closed complementary rectangle C×D, C∩D=∅. Let P(w)=∨_{s∈Σ^∧}(s→w). Claim (x,y)∉P(W). If it were, for a finite strip meet s, some basic neighborhood U_N(x)×V_N(y) would satisfy F∩(U_N×V_N) ⊆ X²\s=∪_{i=1}^r C_i×D_i, with C_i,D_i closed and disjoint. For every distinct n,k≥N, the entire array {a_{n,m}}×{b_{k,t}} lies inside this union. As union closed, (z_n,z_k) is inside as well. Put L_i={n≥N:z_n∈C_i}, R_i={n≥N:z_n∈D_i}; then L_i∩R_i=∅ and all ordered pairs n≠k lie in some L_i×R_i. With finitely many membership-patterns across the 2r sets, choose distinct n,k with identical patterns. Cover (n,k) yields n∈L_i,k∈R_i; same pattern forces n∈R_i, contradiction. Hence P(W)≠X² though W contains Δ, disproving (9).

## Crucial distinction
The **full** strip-generated nucleus still equals V=fit(Δ) for this X: X² is scattered, and the previously proved Cantor–Bendixson iteration removes any closed off-diagonal F transfinally using singleton-complement dual-far strips. Thus this example refutes ONE-STAGE saturation, not the unrestricted identity Wstrip=V. Indeed (x,y) survives the first stage but need not survive subsequent steps.

## Status
Arbitrary-frame (9): FALSE, already countable Hausdorff non-Urysohn.
Arbitrary-frame full strip equality fit(I)=meet dual-far open strips: OPEN.
This is a novel constructed test and should be independently checked before publication.
