# Symmetric rational-graph bar has exact rank three

22 October 2026.

Let X be the original countable Hausdorff rational-bridge space. Its open rational copies are L_0 and R_0, and bridge points z_n have left/right real irrational limit coordinates alpha_n,beta_n. Assume (as in the original construction) ALL limits are pairwise distinct. Define q as largest null open of gamma(t)=(ell_t,r_t). Let tau flip the localic factors, q_sym=q meet tau(q), and let B_sym={(u,v):u box v<=q_sym}. The graph-null condition for a rectangle is exactly u_L∩v_R=empty AND u_R∩v_L=empty.

Theorem: B_sym has minimum separation-tree edge depth exactly THREE.

Lower bound: B_sym subset B_q, hence rank(B_sym)>=rank(B_q)=3. B_sym is a bar: d_I join q_sym=(d_I join q) meet (d_I join tau(q))=1.

Upper bound: for second-coordinate open b define h(b)=join{u:(u,b) is below a D rectangle or B_sym rectangle}. Fix n. For every y∈X choose b_y containing y so that h(b_y) contains all of L_0, R_0, and z_n.

Case y=ell_t in L_0: b_y=ell[J] for a sufficiently small interval J around t avoiding at least one of alpha_n,beta_n. Every first ell_s admits a q_sym-null open neighborhood u⊆L_0, because b_R=0,u_R=0. Every first r_s admits D neighborhood u⊆R_0. For z_n, if J avoids beta_n, choose first z_n neighborhood with right trace avoiding J: both null conditions hold. If J avoids alpha_n, choose first z_n neighborhood with left trace avoiding J: it is disjoint from b_y.

Case y=r_t in R_0: symmetrical: first r_s get q_sym-null neighborhoods, first ell_s get D neighborhoods; for z_n avoid alpha_n to get q_sym, or beta_n to get D.

Case y=z_m: choose real intervals I_m around alpha_m, J_m around beta_m with DISJOINT closures; also beta_n outside closure(I_m), alpha_n outside closure(J_m), possible by pairwise distinct irrational limits. Let b_y be a bridge neighborhood of z_m with left rational trace inside I_m and right trace inside J_m. Each first ell_s is either outside closure(I_m), then locally disjointness, or inside closure(I_m), then outside closure(J_m), so a sufficiently small u⊆L_0 has u_L∩b_R=empty and u_R=empty, giving q_sym-null. Each r_s is handled similarly, swapping I_m,J_m. At z_n choose first neighborhood u with left trace disjoint from J_m and right trace disjoint from I_m, giving both null conditions for q_sym.

In all cases h(b_y) contains L_0,R_0,z_n. Hence for fixed n and any open N_n with N_n∩Z={z_n}, we have N_n<=h(b_y); also L_0<=h(b_y), R_0<=h(b_y). As y varies, b_y join to 1 because X is spatial. Therefore each of (L_0,1), (R_0,1), (N_n,1) has a V→H two-level subtree: vertical cover by b_y, then horizontal leaf cover using definition of h(b_y), restricting each leaf to required first coordinate.

Root (1,1) horizontally covers with L_0,R_0,N_n for n∈N, since Z closed discrete and N_n covers z_n. Thus H→V→H tree of max edge depth 3. Combining with lower bound proves rank(B_sym)=3. Since B_sym symmetric, transposing gives V→H→V depth 3 as well.

Note correction to prior asymmetric rank-three proof: (R_0,1) is NOT a B_sym leaf (its reverse graph pullback is nonzero); here it is handled by the same two-stage V→H subtree. Every leaf is checked locally via graph inverse-images, not spatiality of the localic product.

This rules out rank increase by finite meet q∧tau(q) in this example, but establishes no universal rank-three bound.
