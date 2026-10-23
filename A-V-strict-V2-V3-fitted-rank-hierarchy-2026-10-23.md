# Strict fitted rank hierarchy: V2 is properly above V3
23 October 2026.

Let X be the countable Hausdorff rational-bridge space of A-V-rational-bridge-strict-depth-two-2026-10-22.md. Its two rational sheets are L,R; each rational basis interval J contains the two attaching sequences of some bridge z_n. Let g:Q_rat→X×loc X, g(t)=(ell_t,r_t), and let q be the greatest open annihilated by g*. Earlier proofs establish d∨q=1 and rank(q)=3.

Define Phi_n={v:d∨v=1, rank(v)≤n}, and nucleus j_n=join_Nuc{o_v:v∈Phi_n}, with o_v(t)=v→t. The fitted sublocale with nucleus j_n is V_n.

THEOREM: j_2(q)=q<1 but j_3(q)=1; hence V_2 strictly contains V_3.

PROOF. Every rank≤2 bar v has g*(v) dense in Q_rat. Otherwise a nonempty rational interval J misses g*v. For an H-then-V certificate of v, take a horizontal root child a containing a rational left-sheet interval J'⊂J. Choose a bridge z_n with both attaching sequences inside J'. The left sequence makes z_n∈closure(a), so no disjointness second-coordinate leaf at a contains z_n. Any v-rectangle leaf (u,b) with a≤u has b_R disjoint from J', or else g*v would meet J. The right attaching sequence forces every neighborhood of z_n to meet R over J', so b cannot contain z_n either. Thus no vertical leaf cover of 1 exists. The transpose argument using the right sheet excludes V-then-H proofs. Hence g*v is dense.

If t∧v≤q, pulling back by g gives g*t∧g*v=0, so density implies g*t=0. By maximality of q, t≤q. Therefore v→q=q for every rank≤2 bar v. Their nucleus join fixes q, giving j_2(q)=q. But q itself has rank3; thus o_q≤j_3 and j_3(q)=q→q=1.

The nonzero closed sublocale C(q) is disjoint from I, meets every rank-two bar densely, but is eliminated by rank-three bar q. This is STRICTNESS OF FITTED SUBLOCALES, not simply a difference in individual certificate ranks. It does not decide whether V_fin=V: q is already finite rank.

The key is hereditary depth-two obstruction on every rational interval, not simply rank(q)>2. Iterating such hereditary relative obstructions may lead to strict V_n at larger n or even to a negative answer to the general finite-rank Question A.
