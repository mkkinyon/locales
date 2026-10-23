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

## Stronger result: no nucleus iteration is needed on clopen-local and locally compact-boundary spaces

For any frame Q and finite-rank bar filter Phi_fin define the single-step (generally non-idempotent) prenuclear value
    P_fin(w)=join_{v in Phi_fin}(v→w).
The one-complemented-patch theorem actually proves
    (c⊠1)∨(1⊠c)≤P_fin(w)
for any complemented c with finite-rank diagonal restriction w|c². This uses implication inequalities relative to w directly: on c² the finite-rank truncation v_c matches w, so c⊠c≤v_c→w; on c×c' and c'×c rank-two partition strips p,q are ZERO, so mixed blocks lie below p→w and q→w. It does not require r=j_fin(w) nor idempotence.

COROLLARY (one-stage equality). If the locally finite-rank clopen opens c cover 1, then P_fin(w)=1 for every bar w. Hence j_fin=j_V, with a stronger one-step implication cover for all bar neighborhoods.

LOCALLY COMPACT BOUNDARY. More generally suppose X Hausdorff, Z closed locally compact Hausdorff, and X\Z is covered by clopen opens c_i on whose diagonal squares w has finite rank. The patch lemma yields (e⊠1)∨(1⊠e)≤P_fin(w), where e=join_i c_i=X\Z. Restrict to Z×locZ, a spatial product. At any ordinary diagonal (z,z), the restriction of w is top at this point because w is a bar (diagonal pullback). At any offdiagonal (z,z'), choose disjoint compact closed neighborhoods A,B inside Z (with relative interiors containing z,z'), and disjoint ambient opens around them. The rank-two strip s=((X\A)⊠1)∨(1⊠(X\B)) is a bar and vanishes on the relatively OPEN rectangle int_Z A×int_Z B. Hence the restriction of s→w to Z² is top throughout that open rectangle. It follows pointwise on the spatial product Z×Z that P_fin(w)|Z²=1. Since its closed residual is already contained in Z² from the e-cover, the residual vanishes globally. Therefore P_fin(w)=1, not merely j_fin(w)=1. This recovers clopen disjoint unions and one-point fans (Z singleton) with a stronger quantified conclusion.

Careful logical distinction: a strip excluding just the ordinary singleton pair (z,z') need NOT provide an open neighborhood of it, and therefore does not suffice for this argument. Relative open exclusion follows here from compact closed neighborhoods in locally compact Hausdorff Z. The global Question A and the still stronger global one-stage assertion P_fin(w)=1 remain open.

## CORRECTION, 23 October 2026 — One-step claim on closed boundaries NOT established

The preceding locally compact-boundary paragraph asserts P_fin(w)|Z²=1 by restricting s→w to a relatively open Z²-rectangle on which s restricts to 0. THIS ARGUMENT IS INVALID: a frame homomorphism induced by a closed sublocale does not generally preserve Heyting implication; from (s|Z²)∧t=0 one cannot infer t≤(s→w)|Z². Relative open zero sets need not lift to AMBIENT opens where s vanishes.

The VALID statement is j_fin(w)=1 for this boundary class by the previously established fixed-point/nucleus-density argument (see A-V-question-A-locally-compact-boundary-equality-2026-10-23.md). Put r=j_fin(w), then r is fixed by each o_s, so the closed residual R=C(r) has R∩O(s) dense in R. After clopen patch localization, R lies in spatial Z×locZ. At each offdiagonal point of R, a rank-two s vanishes on a nonzero RELATIVELY open part of R (interiors of disjoint compact A,B), contradicting DENSITY. Diagonal points excluded by original w. Therefore R=0 and j_fin(w)=1. This proof does NOT show P_fin(w)=1.

The ONE-STEP theorem remains rigorously proved for complemented clopen patches and their covering families: its ambient inequalities c×c≤v_c→w and cross c×c'≤p→w are sound. One-point fan and arbitrary clopen cover follow at one step. For general closed locally compact boundaries, one-step saturation remains unproved (and may fail). This correction supersedes only the inappropriate one-step promotion, not fitted-hull equality.
