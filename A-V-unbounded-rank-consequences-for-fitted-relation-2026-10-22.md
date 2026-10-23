# Consequences of unbounded separation-tree rank for V=fit(I): neighborhood filtration and non-cofinality
Date: 22 October 2026
Status: point-free implications established, no unsupported claim about a strict fitted-sublocale gap.

Let L be a frame, Q=L⊕L, d=∨_{u∧v=0}u⊠v, I=C(d), V=fit(I). Let
  Φ={w∈Q:d∨w=1}.
Then Φ is EXACTLY the filter of OPEN NEIGHBORHOODS of I, and equally of V:
  w∈Φ ⇔ I≤O(w) ⇔ V≤O(w).
The first iff is the standard closed/open sublocale disjointness criterion; the second follows since V is meet of all open sublocales containing I, so I≤V≤O(w) simultaneously for all w∈Φ.

Define for n finite
  Φ_n={w∈Φ: canonical D∪B_w has a rooted separation tree of edge depth≤n},
  Φ_fin=⋃_{n<ω}Φ_n.
Then each Φ_n is upward closed in Q, Φ_fin is an UPWARD-CLOSED FILTER closed under finite meets. The finite-meet +1 theorem shows for finite-rank bars w,v, rank(w∧v)≤max(rank w,rank v)+1<ω; ordinary lattice upward closure obvious. Individual bounded Φ_n generally fail finite-meet closure: two orientation-rigid rank-2 dual-far strip bars w,τw have rank2 but meet symmetric s rank3; more generally rank-n rigid bars yield rank n+1 under symmetrization. The ordinary Φ is a filter closed under finite meets by finite frame distributivity of d∨−.

Using X∞ and rank-ω symmetric two-rectangle bar s∞ from A-V-unbounded-finite-rank-and-omega-two-rectangle-fan-2026-10-22.md:
  s∞∈Φ\Φ_fin.
Furthermore Φ_fin is NOT COFINAL in Φ under the open-neighborhood order: there is no v∈Φ_fin with v≤s∞, because rank monotonicity w≤v ⇒ rank(v)≤rank(w), and hence finite-ranked v≤s∞ would force s∞ to have finite rank.

Even dual-far STRIPS have unbounded finite rank. The inductive construction uses w_m=(a_m⊠1)∨(1⊠e_m), with a_m∨e_m=1, and d∨w_m=1, so each w_m is an allowable dual-far strip in the previous strip description of V. Each has exact rank m+1. Their symmetric meets s_m=w_m∧τw_m=(a_m⊠a_m)∨(e_m⊠e_m) have rank m+2. Thus the infinitary height arises INSIDE the strip test family, not only in arbitrary complex Q-opens. It does NOT imply strip-generated W differs from V in these fan locales (earlier W≠V is established by separate rational graph-null example).

NUCLEUS CAVEAT, WITH A POSITIVE CALCULATION. Let j_fin=∨^{Nuc(Q)}_{v∈Φ_fin}o_v, where o_v(q)=v→q. Let V_fin denote corresponding fitted sublocale, so V≤V_fin. Noncofinality of Φ_fin does NOT force strict V<V_fin, because join of nuclei is a transfinite saturation rather than a union of open neighborhood inequalities.

For the specific rank-ω bar s∞ on X∞=⊔_{m≥1}X_m, we can PROVE j_fin(s∞)=1 despite s∞∉Φ_fin. Indeed Q=O(X∞×locX∞) decomposes into clopen blocks (X_i×locX_j). For each N define v_N∈Q blockwise:
   v_N | (X_i×X_j) = s∞ | (X_i×X_j) if i,j≤N,
   v_N | (X_i×X_j) = 1 otherwise.
Then v_N≥s∞, v_{N+1}≤v_N, and ∧_{N<ω}v_N=s∞ in Q. Every v_N has finite rank: split first coordinate into the X_i, split second by X_j, handle off-diagonal i≠j by D (even on finite blocks), each diagonal i=j≤N by the known finite s_i-tree, each diagonal i=j>N by a v_N B-leaf (entire X_i×X_i). Thus v_N∈Φ_fin.

Let t_N=∨_{i,j≤N}(X_i⊠X_j) be the clopen union of the N×N initial blocks, increasing to 1. By construction t_N∧v_N≤s∞ (indeed equality on t_N), so t_N≤v_N→s∞=o_vN(s∞). Therefore
   1=∨_Nt_N≤∨_N(v_N→s∞)≤j_fin(s∞).
Hence j_fin(s∞)=1, equivalently V_fin≤O(s∞)! So this very rank-ω neighborhood, while not admitting any finite-rank neighborhood refinement, IS ALREADY A CONSEQUENCE OF FINITE-RANK OPEN NEIGHBORHOODS VIA ONE NUCLEUS-SATURATION COVER. This underscores the real distinction between **cofinality of open filters** and **equality of fitted hulls**.

OTHER NON-IMPLICATIONS: These examples do not imply V≠I or V≠D∘D on their locales, or strictness of finite-rank-generated fitted hull, or any particular transfinite stabilization ordinal for j_V. They concern the proof-theoretic complexity of individual open-neighborhood inequalities d∨w=1. For every Hausdorff X, ordinary point pairs of V can be shown exactly diagonal: for x≠y choose disjoint open U∋x,V∋y and the dual-far strip w=(X\{x})⊠1∨1⊠(X\{y}); w is a bar because 1=(X\{x}∨U)⊠(X\{y}∨V)≤w∨(U⊠V), and U⊠V≤d. This w excludes ordinary (x,y), while I and V contain all ordinary diagonal points. Thus any nontrivial geometry of V beyond the point diagonal is invisible on ordinary points.

ACTIONABLE RESEARCH: To show V_fin>V on a single frame, one needs w∈Φ with j_fin(w)≠1; merely exhibiting rank(w)≥ω does NOT suffice, and the present X∞ example fails this stronger witness test. For the strip formula W=meet of dual-far strips, analogously use nucleus membership and fixed-point tests, not raw cover ranks.
