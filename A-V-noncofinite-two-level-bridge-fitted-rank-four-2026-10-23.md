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
