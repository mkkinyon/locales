# Fixed rank-n fitted hull locality: K-fans collapse already at rank 2

23 October 2026. Major improvement on Question A. In all statements n is an integer >=2.

Notation. For locale/frame L, Q=L⊕L, d the disjointness open, Phi_n the canonical bars d∨w=1 admitting separation trees of height<=n, j_n the nucleus join of {o_v:v in Phi_n}, with o_v(t)=v→t. Let V_n be fitted sublocale represented by j_n. Equality V_n=V means j_n(w)=1 for every bar w.

LEMMA 1 (clopen finite-rank extension with ZERO overhead for n>=2).
Let c be complemented in L, t=c⊠c in Q, and u an open in the localic square of the open sublocale ↓c. Extend u to the global open
    Ext_c(u)=(u∧t)∨t',
where t'=(c'⊠1)∨(1⊠c') is the complement of t in Q. If u is a canonical bar of separation-tree rank <=n, then Ext_c(u) is a global canonical bar of rank <=n. It agrees with u on t.

Proof. A local tree rooted (c,c) with height<=n can be normalized to an alternating H-first or V-first tree, padded by trivial splits. Suppose it begins H. At the global H-root, replace the local first-coordinate cover c=∨_i a_i by 1=c'∨∨_i a_i. The new (c',1) is an Ext-leaf. For each old child (a_i,c), we need (a_i,1): at the next V-root, enlarge the old second-coordinate cover of c by adding c' as an extra branch, with (a_i,c') an Ext-leaf. If the old child was already a leaf, create a V split into c and c'; this costs at most height2, permitted since n>=2. All other old branches lift unchanged, because Ext agrees with u on c². Thus the resulting global tree has height<=n. Dual argument if original root V. If u top (rank0), Ext=top and there is nothing to prove. Also if local tree starts H but height1, extension has height2. This exhausts n>=2.

LEMMA 2 (restriction of fixed points to clopen square).
For any global bar w and r=j_n^L(w), let c complemented and t=c⊠c. Then the local open r_c=r∧t (viewed in ↓t) is a bar and is fixed by EVERY rank<=n local bar open nucleus: for local v rank<=n, extend to global Ext_c(v) rank<=n by Lemma1. Then o_Ext(v)(r)=r since j_n(r)=r, and projecting to the complemented factor t preserves Heyting implication, giving v→_t r_c=r_c.

Consequently if V_n(↓c)=V(↓c), then r_c=t: because r_c is a local bar and is fixed by all local rank<=n open nuclei, so j_n^local(r_c)=r_c, while equality V_n=V means every local bar is sent to top by j_n. Therefore
    c⊠c<=j_n^L(w)
for EVERY global bar w.

THEOREM A (arbitrary clopen-cover locality for rank-n fitted equality).
Suppose L has a family of complemented elements c_i with join_i c_i=1, and each open locale ↓c_i satisfies V_n=V. Then L satisfies V_n=V.

Proof. Let w any bar, r=j_n(w). Lemma2 gives c_i⊠c_i<=r for all i. For each c=c_i with complement c', the partition strips
    p_c=(c⊠1)∨(1⊠c'), q_c=(c'⊠1)∨(1⊠c)
are canonical bars of rank<=2<=n, so p_c→r=q_c→r=r. Since p_c∧(c'⊠c)=0 and q_c∧(c⊠c')=0, we have c'⊠c<=r, c⊠c'<=r (Heyting adjunction). Together with c⊠c<=r, this gives (c⊠1)∨(1⊠c)<=r. Join_i c_i=1 implies r=1. Since w arbitrary, j_n=j_V.

THEOREM B (one-point fan stability of rank-n fitted equality).
Let X be a T1 spatial space and t∈X such that X\{t} is the union of pairwise disjoint CLOPEN subspaces Y_i. Suppose V_n(Y_i)=V(Y_i) for every i. Then V_n(X)=V(X), WITHOUT any uniform bound on individual separation-tree ranks.

Proof. Fix bar w and r=j_n(w). Lemma2 yields Y_i⊠Y_i<=r for each i. The same rank2 partition-strip argument gives Y_i⊠1 and 1⊠Y_i <=r. Writing e=X\{t}=union_iY_i, obtain (e⊠1)∨(1⊠e)<=r. Thus closed complement C(r) is a sublocale of the singleton square {t}×loc{t}. The bar equation implies the diagonal pullback Δ*w=1, so its ordinary point (t,t) is contained in w, hence r. A closed sublocale of this one-point locale that avoids its unique point is zero. Thus r=1.

BASE THEOREM (rank TWO is fitted-complete on rational K-topology).
Let X1=Q_K (rational K-topology, K={1/m}) and p=0. Each point x≠p has a clopen ordinary-rational-interval neighborhood c_x bounded away from p; the induced topology on c_x is the usual rational topology because K is finite locally away from p. Thus O(c_x) is regular and EVERY local canonical bar has rank<=2 by the point-free regular-frame theorem. The clopen patch inequality (older A-V-question-A-clopen-patch-locality-2026-10-23.md) gives
    c_x⊠1 ∨ 1⊠c_x <= P_2(w)
for any bar w on X1, where P_2(w)=∨_{rank(v)<=2}(v→w). Since the c_x cover X1\{p}, the closed complement of P_2(w) lies on singleton (p,p), but w contains (p,p) by diagonal pullback. Hence P_2(w)=1 for EVERY bar w; in particular V_2(X1)=V(X1).

FAN INDUCTION. Each X_(m+1) of A-V-unbounded-finite-rank-and-omega-two-rectangle-fan-2026-10-22.md is obtained by adjoining one point to disjoint clopen copies Y_i of X_m. By Theorem B, V_2(X_m)=V(X_m) for ALL m. The countable disjoint union X_infty=⨿_m X_m is covered by clopen components X_m, so Theorem A gives
    V_2(X_infty)=V(X_infty).
This holds despite symmetric exact-rank-m+2 bars on X_m for all m and a symmetric exact-rank-omega bar on X_infty. In particular, for the rank-omega bar s_infty, j_2(s_infty)=1. That is MUCH stronger than the previously proved j_fin(s_infty)=1.

ADDITIONAL OBSERVATION (stage2 absorbs high ranks on fans). For m>=2, the special asymmetric bar w_m of rank exactly m+1 satisfies even P_m(w_m)=1, because its restriction to each clopen X_(m-1) copy has rank m. By old one-step clopen patch localization at level m, P_m(w_m) contains the coordinate strips from all old copies; the only residual is the new point diagonal, already in w_m. Consequently j_m(w_m)=1 although rank(w_m)=m+1. Symmetric s_m=w_m∧τw_m has rank m+2, but j_m(s_m)=1, since j_m sends each factor w_m,τw_m to top and is meet-preserving. The new Theorem B sharpens this further: j_2(s_m)=1 for ALL m.

Significance. Fixed separation rank of fitted generators is radically different from certificate ranks: on a single countable first-countable Hausdorff locale the rank-2 fitted hull can equal full V while bars require arbitrarily high finite ranks; on X_infty a rank-omega bar is already eliminated by rank-2 nuclei. Contrasts with rational bridge graph X where V_2 strictly contains V_3. A failure of global Question A must be resistant to this stronger fixed-stage clopen descent, not only to finite-rank descent.

Cautions. n>=2 is essential for no-overhead clopen extension; with n=0,1 there are no nontrivial rank1 bars. Restriction to a clopen factor preserves Heyting implication, unlike restriction to a general CLOSED sublocale (explicit correction in earlier documents). X1 has clopen neighborhoods at every point except 0, not a clopen cover of all X1 by regular pieces. The one-point remainder is handled by its diagonal, not by treating {0} as open.
