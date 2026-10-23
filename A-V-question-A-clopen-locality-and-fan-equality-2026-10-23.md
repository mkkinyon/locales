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
