# Disjoint-gluing bounds for rectangular separation rank

Let X be a disjoint sum of locales X_i, with e_i the corresponding pairwise disjoint complemented frame opens, and L=O(X)=product_i O(X_i). Let B⊆L×L be any rectangular bar. Write B_ii={(a|X_i,b|X_i):(a,b)∈B}, a family in O(X_i)×O(X_i). Let rank(B) be the least natural-number maximum edge depth of separation trees, with infinity if no finite such tree.

**Theorem:** If each B_ii has a tree of depth ≤n_i, then
  sup_i rank(B_ii) ≤ rank(B) ≤ 2+sup_i rank(B_ii)
provided the supremum is finite; more generally a uniform upper bound n gives rank(B)≤n+2.

The lower bound follows by applying the frame restriction homomorphism O(X)→O(X_i) to BOTH coordinates of every proof-tree label; D-leaves remain D and B-leaves remain below B_ii, giving the same height. In particular each B_ii is a bar.

For the upper bound take a horizontal root split (1,1)→(e_i,1) for all i. For each i, split vertically (e_i,1)→(e_i,e_j), j∈I, since ∨_j e_j=1. If i≠j these are D-leaves because e_i∧e_j=0. For i=j, use the depth n_i proof for B_ii, lifting all its local-coordinate labels to global opens supported in e_i. The leaves from B_ii lift: if local rectangle (u,v) is below restriction of global (a,b)∈B, then the supported rectangle (u,v)≤(a,b) as global opens; local D-leaves lift to global D. Root (e_i,e_i) instead of (1_i,1_i) is the lifted local root. Height ≤2+sup n_i.

This estimate is NOT an amplification operation: it gives no strict lower bound beyond the maximum component rank, and the bound +2 might be improvable. In particular the original graph bar glued across copies has rank exactly 3 by an explicit optimized proof, although this estimate only gives upper bound 5.

Further observation: all genuinely new interactions in a disjoint union are cross-component rectangles, already D-leaves. Any meaningful substitution lemma forcing n→n+1 must involve non-clopen overlap or new intrinsic frame-coordinate dependencies; merely grouping components does not suffice.

**Status:** No rank-four example produced. Need tightness study for +2 bound and a nontrivial gluing operation with provable residual rank-sensitive invariant.
