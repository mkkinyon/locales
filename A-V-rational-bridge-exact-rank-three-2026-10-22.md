# Exact depth three for the rational-bridge graph bar

Let X be the previously defined countable Hausdorff rational-bridge space, with open copies L,R of Q, closed discrete bridge set Z, and at z_n left and right sequence limits alpha_n and beta_n, chosen all distinct, with alpha_n != beta_m for all n,m. The graph map g(t)=(ell_t,r_t) has largest null open q in O(X) coproduct O(X). Put B_q={(u,v):g*(u box v)=0}. Then the minimum separation-tree edge depth for B_q is exactly 3.

For each second-coordinate open b let h(b)=join{u:(u,b) is below either a disjointness rectangle or a graph-null rectangle}. We establish that for each fixed n and each y in X there is b_y containing y such that h(b_y) contains every ordinary point of L union R union {z_n}.

If y in L, choose b_y within L: the entire (1,b_y) rectangle is graph-null.

If y=r_t in R, choose a small rational interval J around t avoiding at least one of alpha_n,beta_n and b_y=r[J]. All first points in L admit disjointness leaves, all first points in R admit graph-null leaves. For z_n, if J avoids alpha_n choose first neighborhood of z_n with left trace avoiding J, giving graph-null rectangle; if J avoids beta_n choose first neighborhood with right trace avoiding J, giving disjointness rectangle.

If y=z_m choose b_y a neighborhood of z_m with left trace in rational interval I_m near alpha_m and right trace in J_m near beta_m. Choose intervals with disjoint real closures and alpha_n outside closure J_m, possible since alpha_m!=beta_m and alpha_n!=beta_m. For each ell_t in L, either t outside closure I_m or outside closure J_m: choose a small first open around ell_t disjoint from b_y (a disjointness leaf) or with left indices disjoint from b_y right indices (graph-null). Every first point in R has a graph-null neighborhood since the graph's first coordinate lies in L. At z_n choose a neighborhood with left trace avoiding J_m, giving graph-null rectangle.

Thus h(b_y) contains L,R,z_n. For any neighborhood N_n of z_n meeting Z only in z_n, this implies L<=h(b_y) and N_n<=h(b_y). The b_y for y in X cover 1. Hence (L,1) and (N_n,1) admit V-then-H trees of depth 2: split vertically among b_y and then horizontally among the leaf first opens covering L or N_n. Meanwhile (R,1) itself is a graph-null leaf.

At the root (1,1) split horizontally into (L,1),(R,1), and (N_n,1) for all n. These cover 1. Grafting the foregoing trees yields a well-founded H-V-H tree of maximal depth 3.

The previous independent lower-bound proof in A-V-rational-bridge-strict-depth-two-2026-10-22.md excludes either H-V or V-H depth 2. Hence exact minimal depth is three.

Point-free caveat: every graph-null rectangle is verified by g* vanishing; ordinary points are used only to show coverage in the spatial frame O(X), never to assert that localic product is spatial.
