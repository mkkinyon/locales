# Two-index noncofinite bridge filters: working strict fitted stage V3 > V4

Date: 23 October 2026. **WORKING MATHEMATICAL PROOF — targeted independent audit essential.** This note presents a countable first-countable Hausdorff locale X, a rational graph g:Q_rat→X×loc X, and a proper graph-null bar q of exact rank 4 whose restriction to every nonempty rational parameter interval still has rank 4. By the previously established graph-density lemma, j_3(q)=q<1=j_4(q), proving the working result V3(X) strictly contains V4(X). No priority claim.

## Construction

Take disjoint open copies L_0={ell_r:r∈Q_rat}, R_0={r_r:r∈Q_rat}. Pick a countable dense family of distinct irrational numbers lambda_k (k≥1).

For every k choose distinct irrational gamma_(k,m) tending lambda_k as m→∞, avoiding ALL lambda_j. Choose closed real intervals C_(k,m) around gamma_(k,m), disjoint for FIXED k, with diameters tending to 0 and C_(k,m)→lambda_k. Write C^- and C^+ for its halves to the left and right of gamma. For every (k,m,l), choose distinct irrational attachment coordinates alpha_(k,m,l)∈int C^- and beta_(k,m,l)∈int C^+ tending gamma_(k,m) as l→∞. Choose small open intervals A_(k,m,l) about alpha and B_(k,m,l) about beta with closures respectively inside int C^- and int C^+, diameters tending zero as l→∞. Thus, for fixed k, all A intervals are disjoint from all B intervals; their real trace closures intersect only at irrational points gamma_(k,m) and lambda_k. The sets of alpha centers and beta centers for each fixed k have compact irrational closures K_k^alpha,K_k^beta; choose all coordinates to avoid the lambda_j except the prescribed limits.

For each k,m add TWO anchor points x_(k,m),y_(k,m), with alpha(x)=gamma_(k,m), beta(y)=gamma_(k,m), and other irrational attachment coordinates chosen different from these and all lambda_j. Add lower bridge points z_(k,m,l) at the two indicated alpha/beta coordinates. Arrange that the alpha coordinates of ALL lower bridges are pairwise distinct and likewise their beta coordinates (the equality alpha(x)=beta(y) is across, and allowed). Ensure alpha≠beta at every lower point.

Each lower bridge h has basic neighborhoods {h}∪ell[I∩Q]∪r[J∩Q], I,J real open intervals about alpha(h),beta(h). Add an upper bridge t_k with neighborhood base
 T_(k,N)={t_k} ∪ ⋃_(m,l≥N) ({z_(k,m,l)}∪ell[A_(k,m,l)∩Q]∪r[B_(k,m,l)∩Q]).
Give rational-sheet points their usual open-interval bases. The displayed sets, lower bridge basics and rational intervals generate a topology; their intersections satisfy the basis axiom. Each t_k has noncofinite two-index tails of lower bridges (infinitely many rows and infinitely many points in each row). The shrinking supports near lambda_k make the space first countable and Hausdorff: any fixed lower bridge or rational point can be avoided by sufficiently small T_(k,N), and distinct upper t_k separate by their distinct lambda_k. Lower bridges separate by pairwise distinct alpha/beta coordinates.

Put g(s)=(ell_s,r_s). Let q be the greatest open of O(X)⊕O(X) whose inverse image under g is zero. Then a rectangle u⊠v is below q exactly when u_L∩v_R=∅; S is the union of these graph-null rectangle leaves with disjointness leaves u∧v=0.

Key facts: (a) T_(k,N)⊠T_(k,N)≤q because its left and right rational traces are disjoint. (b) The common REAL closure of those two rational traces contains no rational point, only possibly gamma_(k,m),lambda_k. (c) For fixed k, the lower z_(k,m,l) alpha and beta centers have compact closures containing no rational and no lambda_j for j≠k. The last facts drive the tree upper bound.


## Rank-four LOWER bound on every rational interval

For any nonempty rational open interval J choose k with lambda_k∈J. Let g_J be the rational graph restricted to J, and q_J its greatest null open. We prove neither orientation of a depth≤3 alternating tree for S_J=D∪B_(q_J) exists. (No barhood is needed for these lower bounds.)

H-V-H: any first root open a containing t_k contains T_(k,N) for some N. Select m≥N with gamma_(k,m)∈J. Let y=y_(k,m), whose RIGHT attachment coordinate is gamma_(k,m). For every open b∋y the right rational trace b_R contains an interval around gamma_(k,m). Choose l≥N so large that BOTH alpha_(k,m,l), beta_(k,m,l) lie in this interval and in J. The lower z=z_(k,m,l) belongs to a. No first u containing z is a disjointness leaf against b (u_R meets b_R near beta_z), nor a graph-null leaf against b (u_L meets b_R within J near alpha_z). Therefore z∉h_SJ(b), so a≰h_SJ(b) for EVERY b∋y. No vertical second-coordinate cover of 1 under this first root a can have final H leaves. No first root cover of X works since t_k must be covered. Thus H-V-H fails.

V-H-V: any second root b containing t_k contains some T_(k,N). Select m with gamma_(k,m)∈J. Let x=x_(k,m), whose LEFT attachment coordinate is gamma_(k,m). For every first open a∋x, its left rational trace contains an interval about gamma_(k,m). Choose l≥N with alpha_z,beta_z in this interval and in J, and z=z_(k,m,l)∈b. No second v containing z can be a disjointness leaf with a (v_L meets a_L near alpha_z), nor a graph-null leaf (v_R meets a_L within J near beta_z). Hence b is not below the vertical one-step fiber for ANY a containing x. The first horizontal covers needed below b therefore cannot cover x. Thus V-H-V fails.

Every depth≤3 tree can be flattened/padded to one of these orientations, so rk(q_J)>3 for EVERY nonempty rational interval J. The same is true of q itself.

## Rank-four UPPER bound: explicit H-V-H-V certificate

For b∈O(X), let h(b) denote the union of all first-coordinate opens u with (u,b) a disjointness or graph-null rectangle leaf; since S is a lower set, (a,b)∈H(S) iff a≤h(b). Write E=L_0∪R_0.

**Sheet observation:** If the real closures of the rational left and right traces of b have no RATIONAL point in common, then E≤h(b). For a first rational point ell_s, either s lies outside the closure of b_L (and a small first L-neighborhood is disjoint from b) or outside closure of b_R (and the first L-neighborhood is graph-null against b). Every first R-sheet rational point has a graph-null neighborhood. In particular this holds for b in a single rational sheet, for a sufficiently small lower-bridge neighborhood (its two trace closures disjoint), and for a top neighborhood T_(j,M) by the construction's irrational-only common-closure condition.

**Lower-bridge children.** Fix ANY lower bridge x (anchor or z). For each second point y choose an open neighborhood b_y with E≤h(b_y) and x∈h(b_y):
- second left-sheet rational: b_y entirely in L, hence (1,b_y) is graph-null;
- second right-sheet rational: choose b_y⊂R with rational index interval avoiding irrational alpha_x, giving a graph-null first neighborhood of x;
- second lower bridge y: if y≠x, use Hausdorff disjoint neighborhoods of x,y and shrink b_y to disjoint-closure left/right traces; if y=x, use distinct alpha_x,beta_x to obtain a graph-null rectangle around (x,x) and shrink b_y to separated traces;
- second upper t_j: choose T_(j,M) with right rational trace avoiding alpha_x (since alpha_x≠lambda_j), making x graph-null against it.
Every selected b_y satisfies the sheet observation. Thus h(b_y) contains E∪{x}. Any basic first neighborhood N_x⊂E∪{x} satisfies N_x≤h(b_y) for all y. These b_y cover X, hence (N_x,1)∈V(H(S)) with depth 2. Also (E,1)∈V(H(S)).

**Upper-bridge children.** Fix k and a=T_(k,N). Show (a,1)∈V(H(V(S))) (depth≤3), by choosing for each second point y a neighborhood b_y such that (a,b_y)∈H(V(S)).

Case y in the left rational sheet: choose b_y⊂L. The whole a⊠b_y is graph-null, so (a,b_y)∈S.

Case y in the right rational sheet: for this fixed k, the chosen alpha/beta centers of all z_(k,m,l) have compact irrational closures K_k^alpha,K_k^beta, so a rational s lies outside both. Choose b_y=r[J] with closure(J) avoiding these two compact sets and lambda_k. Every first selected z in a has a disjoint first neighborhood against b_y (its right trace can avoid J); t_k has a first neighborhood with right trace near lambda_k avoiding J. First L-sheet rational points are disjoint from b_y, first R-sheet points are graph-null. Therefore a≤h(b_y).

Case y=t_k: put b_y=a. The left and right rational traces of a are disjoint, so a⊠a≤q.

Case y=t_j with j≠k: choose b_y=T_(j,M) with right trace inside a real neighborhood of lambda_j disjoint from compact K_k^alpha and from lambda_k; possible since lambda_j does not belong to K_k^alpha and lambda_j≠lambda_k. Every first lower z in a has a graph-null neighborhood against b_y, and t_k itself has a graph-null neighborhood with left trace near lambda_k avoiding b_y's right trace. The sheet observation covers all first rational points. Hence a≤h(b_y).

Case y any LOWER bridge: choose a basic b_y containing only y among boundary points, with left/right trace closures disjoint, and with some top neighborhood u_t of t_k disjoint from b_y (Hausdorff). The sheet observation gives E≤h(b_y), while u_t∧b_y=0. For each lower first point x=z_(k,m,l) in a, choose a basic u_x⊂a about x with its two trace closures disjoint. We claim (u_x,b_y)∈V(S). If x≠y shrink u_x and choose a second v_y⊂b_y disjoint from u_x (Hausdorff); if x=y choose v_y⊂b_y with right trace avoiding the first u_x left trace, giving a graph-null rectangle. For each rational second ell_s in b_y use a small second L-neighborhood (graph-null, second R trace empty). For each rational second r_s in b_y choose a small R-neighborhood: its index lies outside at least one of the two disjoint closed trace intervals of u_x, hence is graph-null (if outside u_x left trace) or disjoint (if outside u_x right trace). These second opens plus v_y cover b_y, proving the claimed V(S) membership. Thus every first point of a lies in a first open u with (u,b_y)∈V(S): the rational points by E≤h(b_y), the top t_k by u_t, and each lower x by the previous claim. Consequently (a,b_y)∈H(V(S)).

The b_y from all five cases cover X, so (a,1)∈V(H(V(S))) of depth 3.

Finally, take a GLOBAL horizontal first-root cover consisting of E, all basic lower N_x, and a=T_(k,1) for every top t_k. The E and lower children have V-H subtrees of depth≤2; the upper t_k children have V-H-V subtrees of depth≤3. Consequently
    (1,1)∈H(V(H(V(S))))
is a genuine H-V-H-V certificate of rank≤4 in the FULL FRAME COPRODUCT; no assumption that the localic square is spatial.

Combined with the lower bound, rk(q)=4 and q is a proper bar. Since q_J≥q, all q_J have rk≤4 and the lower bound proves rk(q_J)=4 for every nonempty J.


## Fitted rank stage, not merely bar rank

Let Phi_n be all bars of rank≤n and j_n=join of their open nuclei o_v(u)=v→u. The graph inverse image g*:O(X²_loc)→O(Q_rat) is SURJECTIVE: ell[I]⊠1 pulls back to any rational open interval I, and such intervals generate O(Q_rat).

For every nonempty rational interval J the restricted graph-null q_J has rank exactly 4, as established above. Suppose a rank≤3 bar v had NONDENSE g*v. Some nonempty rational interval J would miss g*v; thus v≤q_J, implying rk(q_J)≤rk(v)≤3, contradiction. Hence g*v is dense for ALL rank≤3 bars v. If t∧v≤q, then g*t∧g*v=0; density forces g*t=0, hence t≤q. Therefore v→q=q for every rank≤3 v, and their join nucleus also fixes q:
    j_3(q)=q<1.
Since q is itself a bar of rank 4,
    j_4(q)≥q→(-),   j_4(q)=1.
Thus the working theorem is a genuine STRICT FITTED STAGE:
    **V3(X) strictly contains V4(X)**,
not simply a rank-four individual tree.

The reason this escapes the old K-fan no-go is HEREDITARY rank four. Every nonempty rational graph slice intersects the attachment of a suitable top t_k (lambda_k dense), and at that top the two independent anchor directions force BOTH orientations of rank3 to fail. The noncofinite tail filter lets an open t_k-neighborhood OMIT ANY FIXED row m while retaining an infinite new row m' beyond any threshold; that simultaneously preserves barhood and defeats all uniform rank3 root patches. The old cofinite-on-all-bridges construction could not do this.

## Focused audit list

1. Check that the intervals C_(k,m), A_(k,m,l),B_(k,m,l) can be chosen with common left/right real closure meeting only in irrational gamma_(k,m),lambda_k for fixed k and all N. In particular ensure the set of alpha centers for a fixed k has compact closure disjoint from every other lambda_j.
2. Check the basis axiom for the top T_(k,N), especially intersections with selected lower bridge neighborhoods, and verify Hausdorffness for t_k versus EVERY lower anchor.
3. Check the "sheet observation" E≤h(b) for top b=T_(j,M); disjoint rational traces alone would NOT suffice without the stronger no-RATIONAL-common-closure property.
4. Check the lower-bridge V-H certificates, including the fixed N_x≤E∪{x} trick.
5. Check that the top a=T_(k,N) lower-second-boundary case really yields H(V(S)), not merely pointwise cover; verify the vertical cover of an entire lower b_y from one fixed first u_x.
6. Check rank≤3 orientation exclusion for graph restrictions q_J. The lower proof must rule out D leaves and B_(q_J) leaves, not just graph leaves.
7. Check the graph-density-to-nucleus implication and order reversal between j_n and V_n.
8. This is a complex new construction and should NOT be promoted to 'independently audited' until a fresh blind referee reads the full note. No assertion of priority relative to literature.

The simpler first-order noncofinite experiment with ONE top t did not give a fitted-stage jump: after graph restriction to a parameter interval disjoint from its limiting irrational, the top obstruction disappears. Densely many distinct lambda_k (each with its own noncofinite fan) are essential for HEREDITARY rank-four.
