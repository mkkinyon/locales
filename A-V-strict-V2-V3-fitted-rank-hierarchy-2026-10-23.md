# Strict fitted rank hierarchy: V2 is properly above V3
23 October 2026.

Let X be the countable Hausdorff rational-bridge space of A-V-rational-bridge-strict-depth-two-2026-10-22.md. Its two rational sheets are L,R; each rational basis interval J contains the two attaching sequences of some bridge z_n. Let g:Q_rat→X×loc X, g(t)=(ell_t,r_t), and let q be the greatest open annihilated by g*. Earlier proofs establish d∨q=1 and rank(q)=3.

Define Phi_n={v:d∨v=1, rank(v)≤n}, and nucleus j_n=join_Nuc{o_v:v∈Phi_n}, with o_v(t)=v→t. The fitted sublocale with nucleus j_n is V_n.

THEOREM: j_2(q)=q<1 but j_3(q)=1; hence V_2 strictly contains V_3.

PROOF. Every rank≤2 bar v has g*(v) dense in Q_rat. Otherwise a nonempty rational interval J misses g*v. For an H-then-V certificate of v, take a horizontal root child a containing a rational left-sheet interval J'⊂J. Choose a bridge z_n with both attaching sequences inside J'. The left sequence makes z_n∈closure(a), so no disjointness second-coordinate leaf at a contains z_n. Any v-rectangle leaf (u,b) with a≤u has b_R disjoint from J', or else g*v would meet J. The right attaching sequence forces every neighborhood of z_n to meet R over J', so b cannot contain z_n either. Thus no vertical leaf cover of 1 exists. The transpose argument using the right sheet excludes V-then-H proofs. Hence g*v is dense.

If t∧v≤q, pulling back by g gives g*t∧g*v=0, so density implies g*t=0. By maximality of q, t≤q. Therefore v→q=q for every rank≤2 bar v. Their nucleus join fixes q, giving j_2(q)=q. But q itself has rank3; thus o_q≤j_3 and j_3(q)=q→q=1.

The nonzero closed sublocale C(q) is disjoint from I, meets every rank-two bar densely, but is eliminated by rank-three bar q. This is STRICTNESS OF FITTED SUBLOCALES, not simply a difference in individual certificate ranks. It does not decide whether V_fin=V: q is already finite rank.

The key is hereditary depth-two obstruction on every rational interval, not simply rank(q)>2. Iterating such hereditary relative obstructions may lead to strict V_n at larger n or even to a negative answer to the general finite-rank Question A.

## General graph-density witness lemma

Let g:Y→X×locX be any locale map, q its maximal g-null open, and suppose q is a bar. Let n≥0. If for every rank≤n bar v the inverse image g*v is dense in O(Y) (that is, its pseudocomplement vanishes), then j_n(q)=q. The proof is uniform: t∧v≤q implies g*t∧g*v=0, hence g*t=0, hence t≤q. Thus v→q=q, for all n-stage generators, and their nucleus join fixes q. If q<1 then the n-stage fitted hull is strictly above V. If also q has rank n+1, then V_n strictly exceeds V_(n+1). This lemma gives a concrete target for higher-rank graph constructions: hereditary graph-density of every lower-stage bar.

## Ordinary point invisibility

On any Hausdorff spatial X, rank-two bars already exclude every ordinary offdiagonal pair (x,y): choose disjoint opens U∋x,V∋y and set p=((X\{x})⊠1)∨(1⊠(X\{y})). It has an H→V tree: root first opens X\{x} and U; first child is a B_p leaf; second child splits the second coordinate by X\{y} and V, using B_p and D. But p excludes (x,y). Thus V_2 and V_3 both have ordinary point set equal to the diagonal, even in our strict example. The strict inclusion arises entirely at the localic sublocale/nucleus level.

## The initial hierarchy on the rational bridge space

No nontrivial bar has separation rank 1: a one-step H-root covers 1 by pairs (u_i,1) in D∪B_w, and any nonzero such pair cannot lie in D. Thus 1=join_i(u_i box1)≤w, giving w=1 (rank0). Likewise for V. So Phi_0=Phi_1={1} and V_0=V_1=the entire localic square.

There are nontrivial rank2 bars on every Hausdorff X with at least two points: for x≠y choose disjoint neighborhoods U_x,U_y; the strip p=((X\{x}) box1)∨(1box(X\{y})) has an H-V tree using the leaf (X\{x},1), the B leaf (U_x,X\{y}) and D leaf (U_x,U_y), so p is a rank2 bar excluding ordinary (x,y). Thus V_2 is proper in the entire localic square, and its ordinary points are exactly the diagonal. Yet on the rational graph bridge X, V_2 strictly contains V_3 by the q witness above, while V_3 also has only diagonal ordinary points. The first two strictness steps therefore measure different things: top→V2 removes ordinary offdiagonal points, whereas V2→V3 removes a purely localic/nonspatial closed graph obstruction.

## Why iterated fan symmetrizations do not automatically separate fitted rank stages

GENERAL FINITE-MEET NUCLEUS LEMMA: If a bar w is a finite meet w=∧_{i=1}^k v_i of bars with rank(v_i)≤n, then j_n(w)=1, even when rank(w)>n. Indeed open nuclei compose by the Heyting identity o_v(o_u(t))=(v∧u)→t, so j_n(w)≥o_v1∘...∘o_vk(w)=w→w=1. No pointwise one-step claim is needed.

In particular for every iterated K-fan, s_m=w_m∧tau(w_m) has rank m+2 while its two constituents have rank m+1. Therefore j_(m+1)(s_m)=1. The rank increase under symmetrization is real proof-tree complexity but is NOT a strict step in the fitted-hull approximation at that same stage. For the original rational graph q, by contrast, j_2(q)=q and there is no rank-two finite-meet explanation of q at the fitted level. This makes the hereditary graph-density obstruction a stronger phenomenon than orientation rigidity or high rank by themselves.
