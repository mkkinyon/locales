# Genuine nested rational bridges, still exact rank three

Date 22 October 2026. **Proved:** A countable Hausdorff bridge space with genuinely accumulating bridge points, NOT a product thickening, has a symmetric rational-graph-null canonical bar of exact minimum separation-tree depth 3.

## 1. Choice of attaching limits

Enumerate a rational interval basis (J_n)_{n≥1}, with infinitely many J_n contained in every nonempty rational interval J. Let K_n={z_n}∪{z_{n,k}:k≥1} be a convergent-sequence compact Hausdorff space with z_{n,k}→z_n. Put Z=disjoint union of K_n.

Choose continuous maps alpha,beta:Z→R\Q satisfying:
(a) alpha and beta are EACH injective;
(b) alpha(Z)∩beta(Z)=∅ (all left and right attaching limits distinct);
(c) for each n, alpha(K_n)∪beta(K_n)⊂J_n (even positive margin inside J_n);
(d) alpha(z_{n,k})→alpha(z_n) and beta(z_{n,k})→beta(z_n), the maps are continuous.
These can be selected inductively from distinct irrationals in J_n. Each A_n=alpha(K_n), B_n=beta(K_n) is compact and consists only of irrationals, and A_n∩B_m may be empty for all n,m (by (b)). NOTE: alpha(Z) and beta(Z) are dense in R because each J_n carries a cluster, but each individual A_n, B_n is compact and disjoint from opposite-coordinate limit values.

## 2. Construction of topological X

Underlying set X=L_0⊔R_0⊔Z, where L_0 and R_0 are disjoint open copies of the rationals with their usual topologies. In addition to all opens of L_0,R_0, declare basic bridge neighborhoods

  N(z;I,J,V)=ell[I] ∪ r[J] ∪ {z'∈V: alpha(z')∈I and beta(z')∈J},

where I,J are ordinary real open intervals containing alpha(z), beta(z), respectively, and V is a Z-open neighborhood of z. (The final expression is interpreted on rational indices for ell[I],r[J].) Continuity of alpha,beta makes these a compatible local base at each z; intersections contain smaller neighborhoods of this form. The induced topology on the closed subspace Z is its original topological sum topology.

X is Hausdorff: two distinct bridge points have distinct alpha-values and beta-values, so choose left and right rational intervals disjoint in pairs. Bridge vs rational point can be separated by avoiding its rational index in the appropriate interval; rational points on separate sheets are separated automatically. Hence X is sober. Z=X\(L_0∨R_0) is closed, locally compact and NONDISCRETE, each K_n compact and open in Z. In particular, z_{n,k} genuinely converges to z_n in X.

This is not of the Cartesian graph-thickening form X_old×K, since the rational sheets remain single copies of Q rather than products and the new bridge coordinates carry varying attachment values.

## 3. Graph null open and barhood

Let gamma:Q→X×locX, t↦(ell_t,r_t), and let q be the largest gamma*-null open in the locale product; equivalently the join of all rectangles u⊠v with u_L∩v_R=∅. Let tau exchange tensor factors, s=q∧tau(q), and B_s={(u,v):u⊠v≤s}. Then the leaf condition for B_s is exactly
  u_L∩v_R=∅ and u_R∩v_L=∅.

The ordinary graph F={(ell_t,r_t):t∈Q} is closed in the ordinary product X×topX: for mixed bridge/rational pairs use irrationality of alpha, beta; for a pair (z,z') use alpha(z)≠beta(z'); for rational pair off F use distinct rational indices; all other first/second sheet pairs have trivial neighborhoods avoiding F. Hence each ordinary pair outside F has a graph-null open rectangle, and points on F have disjoint neighborhoods in X, hence lie in d_I. So q∨d_I covers every ordinary point.

Let e=L_0∨R_0. The four blocks of e⊠e are covered by q or d_I: L⊠R is in d_I, and the other three are q-null. Thus e⊠e≤q∨d_I.

Since Z is locally compact, the previously proved locally compact boundary reflection theorem implies q∨d_I=1 in the LOCALIC tensor product (not merely ordinary points). Transposing gives tau(q)∨d_I=1. By finite distributivity s∨d_I=(q∨d_I)∧(tau(q)∨d_I)=1. Thus B_s is a genuine bar.

## 4. Strict failure of depth 2

Let a∈O(X) meet the left rational sheet. Choose nonempty rational interval J with ell[J]⊆a; choose n with J_n⊂J. Then z_n∈closure_X(a), because all neighborhoods of z_n have left rational traces near alpha(z_n)∈J. Thus z_n∉a*.

If (u,v)∈B_s with a≤u, graph nullness u_L∩v_R=∅ forces v to omit all r[J]. But beta(z_n)∈J, and any neighborhood of z_n has right rational trace intersecting r[J]. Hence z_n∉v. Thus z_n∉a*∨F_Bs(a), so a cannot be H→V good. Every H→V-good a therefore misses the entire left rational sheet, and these cannot join to top. Thus no H→V depth-two root.

Likewise any second-coordinate open b meeting R_0 contains r[J] for some J, and some z_n with J_n⊂J belongs to closure b but cannot occur in any first coordinate of a B_s leaf with b≤v. Therefore no V→H depth-two root. Rank≥3.

## 5. Constructing the H→V→H depth-three tree

For b∈L set h(b)=b*∨r_s(b), the horizontal leaf saturation at second coordinate b. Fix one COMPACT bridge component K_n, and put A_n=alpha(K_n), B_n=beta(K_n). Both compact subsets of the irrational reals, disjoint from each other and from the ENTIRE opposite-coordinate range: A_n∩beta(Z)=∅, B_n∩alpha(Z)=∅.

Claim: for every second-coordinate point y∈X there exists an open b_y containing y such that
  L_0∪R_0∪K_n ⊆ h(b_y)
as ordinary sets.

Case y=ell_t∈L_0: Choose rational interval J about t whose closure misses compact B_n (possible t rational, B_n all irrational). Set b_y=ell[J]. All first ell_s have B_s leaves u⊆L_0 since both first and second opens lie on left sheet; all first r_s have D leaves u⊆R_0. For any z∈K_n choose bridge neighborhood u of z with right rational trace avoiding J; then u⊠b_y≤s by both graph-null conditions. Thus h(b_y) contains L_0,R_0,K_n.

Case y=r_t∈R_0: Symmetric; choose J disjoint compact A_n and b_y=r[J]. Then first r_s have B_s leaves, first ell_s have D leaves, and all bridge points z∈K_n have symmetric graph-null neighborhoods with left trace disjoint J.

Case y=z'∈Z: Because alpha(z')∉B_n, beta(z')∉A_n and alpha(z')≠beta(z'), choose small real intervals I around alpha(z') and J around beta(z') whose CLOSED intervals satisfy
  cl I ∩ cl J=∅,
  cl I ∩ B_n=∅,
  cl J ∩ A_n=∅.
Choose bridge neighborhood b_y=N(z';I,J,V), so b_y has left trace in I and right trace in J.
For any first ell_t: if t∉cl I, choose u⊆L_0 with rational indices avoiding I, giving D; if t∈cl I, use cl I∩cl J=∅ to choose u⊆L_0 with rational indices avoiding J, giving symmetric graph-null B_s leaf.
For any first r_t: if t∉cl J, choose u⊆R_0 avoiding J, giving D; otherwise choose u⊆R_0 avoiding I, giving B_s.
For each first z∈K_n, alpha(z)∉cl J and beta(z)∉cl I. Choose neighborhood u at z whose left and right traces avoid J and I respectively; then u⊠b_y≤s. Thus again h(b_y) contains L_0,R_0,K_n.

This establishes the claim. Since h(b_y) is an actual open of X and all L_0∪R_0∪K_n lie within it, we have a_n≤h(b_y) where a_n:=L_0∪R_0∪K_n. The set a_n is OPEN in X because K_n is an open component of the boundary Z; every bridge point z∈K_n has a basic neighborhood whose Z-trace stays in K_n, while the rational sheets are contained in a_n.

As y varies over X, the opens b_y cover 1, so
  Phi_s(a_n)=∨{b:a_n≤h(b)}=1.
Thus every (a_n,1) has V→H separation subtree of edge depth ≤2, and the a_n cover X because Z=∪_nK_n. A horizontal root cover 1=∨_n a_n and grafting the V→H subtrees gives H→V→H height 3.

Combining with depth-two lower bound, rank(B_s)=3, and by symmetry both orientation-specific ranks are 3.

## 6. Significance and limitation

This is an HONEST nested-bridge example with z_{n,k}→z_n and changing attaching limits; unlike a product thickening, the rational sheets remain single. Each compact cluster K_n supports uniform choice of second-coordinate neighborhoods through disjointness of its compact sets A_n,B_n from opposite-coordinate bridge limits. This explains rank-three persistence under a genuine second layer.

It gives NO rank-four bar and NO universal arbitrary-frame (*) theorem. A potential higher-rank construction must defeat uniformization on every suitable open neighborhood of accumulating boundary clusters; in particular cross-limit accumulation or noncompact bridge families might be essential, while maintaining ordinary graph closedness and localic barhood.

Reference for spatiality of localic products with a locally compact sober factor: Encyclopedia of Mathematics, 'Locale' (https://encyclopediaofmath.org/wiki/Locale); J. R. Isbell, 'Product spaces in locales', Proc. AMS 81 (1981), 116–118.
