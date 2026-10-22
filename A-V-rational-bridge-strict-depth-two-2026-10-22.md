# A strict depth-two separation-tree counterexample from the rational-bridge graph
22 October 2026. **New theorem**: the original rational-bridge graph-null rectangular bar has no depth-two separation tree. Does NOT assert it has a depth-three tree.

## Input from earlier audited construction
X is countable Hausdorff with disjoint open rational copies L_0,R_0 and a closed-discrete set Z of bridge points z_n. For each basic rational interval J_n there is a bridge z_n with sequences A_n,B_n ⊂ J_n of rational indices accumulating in X at z_n through L_0 and R_0 respectively; the sequences converge in R to distinct irrational α_n,β_n. Let γ:Q→X×_loc X be γ(t)=(ℓ_t,r_t), and q largest γ*-null open in T=O(X)⊕O(X). The already audited localic boundary-lemma proof yields q∨d_I=1 (also q≠1).

Define B_q={(u,v)∈L×L:u⊠v≤q}. Since rectangles join-generate T, b_Bq=q. Thus B_q is a rectangular bar and admits some well-founded separation tree by C-ideal completeness.

## Exact depth-two criterion
For arbitrary B, F_B(a)=∨{v:(u,v)∈B,a≤u}, so a one-step vertical leaf cover of (a,1) exists precisely when a*∨F_B(a)=1. A H→V depth-two tree exists iff ∨{a:a*∨F_B(a)=1}=1. Swap coordinates for V→H. Same-orientation adjacent levels flatten, so these cover ALL depth≤2 trees.

## H→V fails for B_q
Let a∈L meet L_0. There is a nonempty rational interval J with ℓ[J]⊆a. Choose n with J_n⊆J, so both A_n and B_n are contained in J (or eventually so). Then z_n∈cl_X(a) by L sequence A_n, hence z_n∉a*=X\cl(a).

If (u,v)∈B_q has a≤u, then u⊠v≤q implies graph γ pullback zero: for every rational t with ℓ_t∈u, r_t∉v. In particular v contains none of r[J], since ℓ[J]⊆a≤u. Because right sequence B_n⊂J converges to z_n, this implies z_n∉v (any open v containing z_n contains a tail of r[B_n]⊆r[J]). Thus z_n∉F_Bq(a), and a*∨F_Bq(a)≠1. Therefore every horizontal-good a misses L_0, so ∨{a:good(a)}≤X\L_0 (an open? union certainly misses L_0) <1. No H→V depth-2 tree.

## V→H fails
Symmetrically if b meets R_0, choose rational J with r[J]⊆b and n with A_n,B_n⊂J. Then z_n∈cl b by right B_n and hence z_n∉b*. For every (u,v)∈B_q with b≤v, the graph-null condition forces u to omit all ℓ[J]. As left sequence A_n⊂J converges to z_n, z_n∉u. Thus z_n∉G_Bq(b)=∨{u:(u,v)∈B_q,b≤v}; b*∨G_Bq(b)≠1. Every vertical-good b misses R_0, so no V→H depth-2 tree.

## Conclusion and scope
B_q is a rectangular bar with **minimum tree depth >2**. This is a STRICT counterexample to universal depth-two collapse, within a countable Hausdorff spatial locale. It does not establish that minimum depth is exactly 3, nor disprove a universal finite bound N>2, nor demonstrate a bar requiring transfinite rank. It is fitting that the original strict-strip counterexample also exhibits a strict proof-tree alternation obstruction.

Potential check: ensure the previously constructed X has for each basis interval J a bridge n with both entire rational sequences (or tails) inside J. This was explicit in the original rational-graph construction; no use of dense limit pairs in R² is necessary.
