# Attempted amplification of rational-bridge separation-tree rank

Date 2026-10-22.

Question: can one modify the rank-three graph-null rectangular bar B_q on the rational-bridge space to obtain bars of arbitrarily large finite minimum depth?

**No such amplification is proved here.** Two natural operations fail or present a serious obstacle.

1. Disjoint duplication does NOT raise rank. Let X_i be copies of the rank-three rational-bridge space X, let Y be their topological disjoint union, and let gamma_i:Q->X_i x_loc X_i be the original graph maps. Let gamma be their coproduct map into Y x_loc Y, and q_gamma its largest graph-null open. The bar B_qgamma has minimum depth exactly 3:
upper bound: use initial horizontal cover of Y by all local first-side regions L_i, R_i, and individual bridge neighborhoods N_i,n, copying the H-V-H proof inside each component. For the second-coordinate points in other components, any rectangle with first side in component i and second side in component j != i is disjointness leaf. Thus every first-root child has V-H descendant height<=2.
lower bound: restricting any proposed global height<=2 tree to one component X_i in BOTH coordinates preserves exact covers and converts D/global-null leaves into D/local-null leaves. It would yield a height<=2 tree for B_q on X_i, contradicting the audited lower bound. So depth exactly 3 for any nonempty disjoint sum.
2. Iterating bridges (bridge points of a new level accumulating on existing bridge points) might raise rank, but makes Z=X\(L_0 union R_0) non-discrete. The crucial boundary lemma used to establish q join d_I=1 assumes closed-discrete Z. Thus ordinary closedness of the lifted graph away from the diagonal does NOT suffice to prove localic disjointness of graph closure and I. Any claimed higher-rank example must replace this step, not implicitly reuse it.

**Needed rank amplification lemma:** For a candidate next-level space X^{(n+1)} and graph-null bar B^{(n+1)}, produce (A) a frame-level cover q_new join d_I=1; (B) an upper tree of controlled finite height; and (C) a rank-sensitive restriction or quotient showing any tree of height<=n induces a forbidden tree of height<=n-1 for the previous stage. Pointwise inseparability alone, which only rules out depth two, does not provide (C).

No general finite bound is disproved by present results; exact rank three remains the highest established.
