# Closed hereditarily projection-inseparable relation in a countable Hausdorff space

Date: 21 October 2026. Constructive result in the ORDINARY topological product, with the localic-product question explicitly open.

## Construction

Let (J_n) be a countable basis of nonempty open intervals in Q. Choose mutually disjoint countably infinite sets A_n,B_n⊂J_n, each a closed discrete subset of Q obtained as rational sequences converging to **distinct irrational** numbers in J_n. To arrange countably many disjoint sequences rigorously, first partition Q into countably many pairwise disjoint dense subsets D_i; then choose the 2n and 2n+1 sequences within D_{2n}∩J_n and D_{2n+1}∩J_n, respectively, approaching distinct irrational limits.

Let L={ℓ_t:t∈Q}, R={r_t:t∈Q}, both open copies of Q. Adjoin z_n for every n. A neighborhood of z_n includes z_n and open subsets of L,R containing cofinitely many ℓ_t for t∈A_n and r_t for t∈B_n respectively. This topology is Hausdorff: z_n and any point of L or R separate using a tail disjoint from that rational and normality of Q; z_n and z_m separate using disjoint closed A_n,A_m in L and disjoint closed B_n,B_m in R.

Define F={(ℓ_t,r_t):t∈Q}⊂X×_top X. This is homeomorphic to Q, nonempty, and misses Δ. It is closed: in L×R it is a closed graph; outside the four copy-products, points (z_n,r_t) and (ℓ_t,z_n) separate from F because A_n or B_n tails are closed and omit t; points (z_n,z_m) separate because A_n and B_m are disjoint closed subsets of Q and admit disjoint open neighborhoods. All remaining regions are disjoint from F trivially.

Every nonempty relatively open G⊆F contains the subgraph over some basic interval J_n. Since A_n,B_n⊂J_n and ℓ_{a_{n,k}}→z_n and r_{b_{n,k}}→z_n, we have z_n∈cl_X π₁(G)∩cl_X π₂(G). Therefore **every nonempty relatively open G has intersecting projection closures**, despite F∩Δ=∅ and F closed.

Equivalent consequence: every disjoint-sided closed rectangle C×D intersects F nowhere densely. Thus the full strip-derived closed-set operator on the ORDINARY product has F as a nonempty fixed point. The topological version of 'all dual-far strips recover the fitted diagonal' fails for this countable Hausdorff non-Urysohn example.

## IMPORTANT SCOPE

This does not by itself prove localic W≠fit(I). Since X is not locally compact, the locale product O(X)⊕O(X) may differ from O(X×_top X), including potentially nonspatial sublocale closure and diagonal phenomena. Next task: lift F via the graph map g:Q→X×_loc X into a nonzero closed sublocale of the locale product, and verify its closure is disjoint from the localic I=C(d_I). Pullbacks of dual-far strips along g are dense in Q by the projection argument, but verifying localic disjointness of the **closed image hull** from I is a separate nontrivial step.

Do not report the arbitrary-locale theorem as disproved without this step.
