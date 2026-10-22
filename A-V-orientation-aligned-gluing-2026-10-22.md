# Orientation-aligned disjoint gluing preserves separation rank

Date: 22 Oct 2026.

Let X=disjoint union of X_i, L=O(X)=product of L_i; e_i opens are pairwise disjoint and join to 1. Let B subset L×L be any rectangular bar and B_ii={(a|X_i,b|X_i):(a,b)∈B}. Suppose every B_ii admits a well-founded separation tree with maximum edge depth ≤n, n≥2, such that its root is a H-cover and all its root children are either leaves or V nodes (i.e. alternating H-first normal form). Then B admits a H-first separation tree of depth ≤n, NOT merely n+2.

Proof: For each local root H-child (a_iα,1_i), make a global H-child (supported a_iα,1) in X. All such children for all i join 1 in first coordinate. For any local V-root child with vertical cover (a_iα,b_iβ), lift all its b_iβ into supported e_i and add all cross-component opens e_j for j≠i; together these cover 1 globally, and the cross children (a_iα,e_j) are D-leaves. For local b_iβ children lift their entire lower H/V tree to global supported rectangles; D leaves remain D, while B_ii leaves below a restricted (u|X_i,v|X_i) lift to leaves below the original B rectangle (u,v). All tree heights remain ≤n. If a local root H-child is already a D/B leaf (a_iα,1_i), globally its (a_iα,1) is handled by a vertical cover consisting of (a_iα,e_i) (lift of original leaf) and cross disjoint leaves (a_iα,e_j), height ≤2≤n. Empty components ignored.

Symmetric statement for V-first trees. Lower bound rank(B)≥sup_i rank(B_ii) follows by frame restriction maps. In particular if all component B_ii have **exact rank 3 with H-V-H trees** then global B also has exact rank 3. Thus arbitrary rectangular bars on disjoint unions cannot gain rank when the component witness trees have aligned orientation and n≥2.

This strengthens the earlier rough bound rank≤sup rank(component)+2, but does not prove equality when different components have incompatible optimal orientations. Incompatible orientation of component proofs is the only possible reason for a strict increase under disjoint sums, but no such example is asserted.

Rank 4 still NOT constructed; no universal rank-three collapse established.
