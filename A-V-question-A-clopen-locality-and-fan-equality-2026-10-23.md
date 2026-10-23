# Question A: clopen locality and all fan locales

23 October 2026. Working theorems.

Let Q=O(X)⊕O(X), d the disjointness open, Phi={w:d∨w=1}, and Phi_fin its finite separation-tree rank part. Set j_fin=join of open nuclei o_v(q)=v→q for v∈Phi_fin. Equality V_fin=V is equivalent to j_fin(w)=1 for every w∈Phi.

THEOREM 1. Let X be the disjoint union of clopen locales X_i. If a bar w restricts to a finite-rank bar on every diagonal block X_i×X_i, then j_fin(w)=1, in fact join_{v∈Phi_fin}(v→w)=1.

Proof. For finite E of indices let t_E be the clopen union of blocks X_i×X_j (i,j∈E). Then join_E t_E=1. Define v_E=(w∧t_E)∨complement(t_E). Thus v_E≥w and t_E∧v_E≤w, hence t_E≤v_E→w. The bar v_E has finite rank: split first coordinate into finitely many X_i and their complement, then second coordinate similarly. Off-diagonal blocks (i≠j) are disjointness leaves, diagonal blocks i=j have the inherited finite tree for w|X_i², and all blocks outside t_E are B_vE leaves. Therefore v_E belongs to Phi_fin. Joining the implication inequalities gives 1≤join_E(v_E→w)≤j_fin(w), proving claim.

THEOREM 2. Suppose a spatial T1 space X consists of a point t and disjoint clopen subspaces Y_i covering X\{t}. If every bar on every Y_i has rank≤N for some common finite N, then EVERY bar on X has rank≤N+3, regardless of t's neighborhood topology.

Proof. For a bar w use diagonal pullback to select a B_w leaf (u,v) containing (t,t). First-root H covers X by u and all Y_i. For child (Y_i,1), V split second into Y_i and its clopen complement: complementary rectangle D, diagonal rectangle receives finite tree for restriction w_ii (rank≤N). For child (u,1), V split second into v and all Y_i. (u,v) is B_w leaf. For (u,Y_i), H split first into u∩Y_i (its rectangle inherits restricted finite tree w_ii) and u∩(X\Y_i) (D leaf). Thus height ≤N+3.

COROLLARY. The original one-stage rational K-topology X_1 has a compact exceptional nonregular locus {0}, so all bars have rank≤3 by the previous compact-exception theorem. Each iterated fan X_(m+1) is a new point plus countably many clopen copies of X_m. Theorem2 gives universal finite bound N_m≤3m for every bar on X_m. Therefore on X_infty=disjoint union of all X_m, EVERY bar has finite-rank diagonal restrictions. By Theorem1 j_fin(w)=1 for EVERY bar w, hence j_fin=j_V and
   V_fin(X_infty)=V(X_infty).
This strengthens the previous special calculation for the symmetric exact omega-rank bar s_infty: full fitted-hull equality holds on that space despite the noncofinality of finite-rank neighborhoods.

More generally, any disjoint union of locales whose bars each have some finite universal rank bound has V_fin=V, even if the bounds across components are unbounded.

Open: Question A for arbitrary frames remains unresolved. This proof relies essentially on complemented clopen blocks, and does not imply cofinality in neighborhood order or any bound for all frames.

## Exact all-frame criterion for FAILURE of Question A

Let Φ_fin be the finite-rank bar filter and j_fin the least nucleus dominating open nuclei o_v(q)=v→q for v∈Φ_fin. Then

  V_fin≠V  iff  there exists a proper bar r∈Q, r<1, such that
                         v→r=r for EVERY v∈Φ_fin.

Proof (⇐): If every generating nucleus o_v fixes r, their join j_fin fixes r, hence j_fin(r)=r<1, while r is a bar and j_V(r)=1. Thus V_fin>V. Proof (⇒): If some bar w has j_fin(w)<1, put r=j_fin(w). Because r≥w, r is also a bar; r<1. For every v∈Φ_fin, o_v≤j_fin so v→r=o_v(r)≤j_fin(r)=r; converse inflationary, so equality. Thus proper fixed-point bar r exists.

Under the closed sublocale correspondence R=C(r), condition v→r=r means the open sublocale O(v) meets R densely in R, equivalently c(R∧O(v))=R. The bar r means R∧I=0. So Question A fails iff there is a nonzero closed sublocale R disjoint from I such that EVERY finite-rank bar v is dense on R. This is much stronger than the existence of infinite-rank individual bars. The rational graph R from the earlier strip counterexample is NOT such a witness, because its annihilator q is itself a rank-three bar; similarly no closed witness can survive all finite block truncations on X_infty.

For any Hausdorff spatial X, finite rank-2 bars exclude each ordinary off-diagonal pair: given x≠y choose disjoint neighborhoods U∋x,T∋y, put v=((X\{x})⊠1)∨(1⊠(X\{y})); a horizontal first split into X\{x},U and vertical second split into X\{y},T provides an H→V depth-two bar certificate. Consequently both V and V_fin have precisely diagonal ordinary point sets. If strict inequality occurs on Hausdorff X, it is a genuine nonspatial-sublocale distinction, invisible as an ordinary binary relation on points.

A potential counterexample must therefore build a closed off-I ghost R that is HEREDITARILY resistant to ALL finite-rank bars; merely accumulating arbitrarily high finite-rank components at a clopen-accessible limit is insufficient. The general arbitrary-frame Question A remains OPEN.
