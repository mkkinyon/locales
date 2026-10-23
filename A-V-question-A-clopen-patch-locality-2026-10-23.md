# Question A: point-free clopen-patch locality
23 October 2026. New stronger theorem and streamlined proof.

Let L be an arbitrary frame, Q=L⊕L, d=join of rectangles u⊠v with u∧v=0. Let Phi={w:d∨w=1}, Phi_fin its finite-stage canonical bar subset, and j_fin the join in Nuc(Q) of open nuclei o_v(q)=v→q for v∈Phi_fin. Define r=j_fin(w), so r≥w and v→r=r for each v∈Phi_fin.

THEOREM (one complemented patch). Fix a complemented element c∈L, with complement c', and let w∈Phi. Suppose the restriction of w to the open square c⊠c (corresponding to the frame ↓c⊕↓c) has a finite separation-tree certificate. Then
    (c⊠1)∨(1⊠c) ≤ j_fin(w).
Proof.
(1) Let t=c⊠c, complemented in Q. Its complement is t'=(c'⊠1)∨(1⊠c'). Define v=(w∧t)∨t'. Then v≥w and v∧t≤w. The bar v has finite rank: H root split 1=c∨c'; child (c',1) is a B_v leaf, and child (c,1) splits V into c and c'. The (c,c') child is a B_v leaf; the (c,c) child uses the inherited finite tree for w restricted to ↓c. Therefore v∈Phi_fin. Hence t≤v→w≤j_fin(w)=r.
(2) Consider the two rank≤2 *partition strips*
   p=(c⊠1)∨(1⊠c'),   q=(c'⊠1)∨(1⊠c).
They are bars because c,c' are complementary (explicit H-V tree: root split c∨c', then second split c∨c'; only D on opposite partition blocks). The rectangle c'⊠c is disjoint from p, and c⊠c' disjoint from q. Since p→r=q→r=r, Heyting adjunction yields c'⊠c≤r and c⊠c'≤r.
(3) With c⊠c≤r, these imply c⊠1=(c⊠c)∨(c⊠c')≤r and 1⊠c=(c⊠c)∨(c'⊠c)≤r. QED.

COROLLARY (clopen-local universal equality). If for EVERY bar w∈Phi there is a family (c_i) of complemented elements of L whose join is 1 and for which w restricted to c_i² has finite rank, then j_fin(w)=1 for all w; equivalently V_fin=V. In particular, sufficient that the locale admits a clopen cover (c_i) such that each open sublocale ↓c_i has a finite UNIVERSAL separation-tree bound N_i (no common bound needed). This does NOT require a disjoint clopen partition or any spatiality; applies to arbitrary frames.

PER-BAR RESIDUAL. For an arbitrary bar w, let e_w=join of all complemented c such that the restricted bar on c² has finite rank. The above theorem yields
  (e_w⊠1)∨(1⊠e_w)≤j_fin(w).
Consequently any residual closed sublocale R=C(j_fin(w)) is supported on the closed-boundary localic square C(e_w)×locC(e_w). This works even if e_w itself is not complemented; no pseudocomplement substitution is needed.

APPLICATIONS: On a topological disjoint union of finite-universal-rank spaces, the component opens are complemented and cover top, so V_fin=V by one-patch argument. On one-point fans over such components, e_w contains their union, so C(j_fin(w)) lies on singleton square {t}² and vanishes since w contains diagonal (t,t). If closed remainder Z=C(e_w) is locally compact Hausdorff and the ambient X Hausdorff, use rank-two strips formed from disjoint compact relative neighborhoods of distinct z,z' to remove any offdiagonal ordinary point from the spatial square Z×locZ, while diagonal points already lie in w; hence j_fin(w)=1. This recovers and simplifies the earlier locally compact boundary theorem.

CRITICAL CAVEAT: A rank-two singleton-complement strip excludes an ordinary offdiagonal POINT, but need not vanish on a relatively OPEN neighborhood of that point. To contradict density v→r=r on a closed residual one needs the latter stronger property, obtained from separated compact neighborhoods in the locally compact boundary. It is incorrect to conclude j_fin(w)=1 from mere pointwise exclusions in an arbitrary spatial product. Point-set agreement of V_fin and V is weaker than fitted sublocale equality.

OPEN: arbitrary-locale V_fin=V. A negative witness must have a proper bar r fixed by all finite-rank open nuclei, hence a nonzero closed R disjoint from I that cannot be eliminated on any complemented patch with finite local rank. This rules out many clopen-local constructions, not all possible intertwined infinite-rank obstructions.
