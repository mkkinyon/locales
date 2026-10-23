# Compact exceptional nonregular locus: universal depth-three bars on Hausdorff spaces

Date: 22 October 2026.

**THEOREM (compact nonregular locus).** Let X be a Hausdorff topological space and K⊆X a compact subset such that every point y∈X\K is a point of regularity: for every open neighborhood U of y there exists open b∋y with closure_X(b)⊆U. Then EVERY rectangular bar B on L=O(X) has an explicit H→V→H separation tree of maximum edge depth THREE.

Proof. Put S=D∪B, h(b)=∨{u:(u,b)∈S}, and Φ(a)=∨{b:a≤h(b)}.

(1) Diagonal leaves cover all ordinary points. Since d_I∨b_B=1 in L⊕L, pull back along localic diagonal Δ* and use Δ*(d_I)=0 to obtain
  1=∨_{(u,v)∈B}u∧v.
Thus for each x∈X choose (u_x,v_x)∈B with x∈u_x∩v_x.

(2) Each REGULAR second-coordinate point y∈X\K admits b_y∋y with h(b_y)=1. Indeed choose bar diagonal leaf (u_y,v_y) containing y, then by regularity shrink b_y with y∈b_y, closure b_y⊆u_y∩v_y. The B leaf (u_y,b_y) and D leaf (b_y*,b_y) horizontally cover 1 because u_y∨b_y*=1. Consequently (1,b_y)∈H(S), equivalently h(b_y)=1.

(3) Fix any first-coordinate point x∈X and diagonal B leaf (u_x,v_x) containing x. The subset F_x=K\v_x is compact and excludes x. In a Hausdorff space, a point and a disjoint compact subset admit disjoint OPEN neighborhoods. Choose U_x∋x and W_x⊇F_x with U_x∩W_x=∅. Set a_x=u_x∩U_x, an open neighborhood of x.

For second-coordinate points in K∩v_x: the single B leaf (a_x,v_x)∈B gives a_x≤h(v_x).
For second-coordinate points in K\v_x: the single D leaf (a_x,W_x)∈D gives a_x≤h(W_x).
For every y∉K: use b_y from (2), for which a_x≤h(b_y)=1.

The open family {v_x,W_x}∪{b_y:y∈X\K} covers X, and a_x≤h(each member). Hence Φ(a_x)=1, i.e. (a_x,1)∈V(H(S)).

(4) As x varies, a_x cover X. Hence
  (1,1)∈H(V(H(S))).
This is the desired rooted H→V→H tree. There is NO assumption on the spatiality of X×locX: the only localic input is the diagonal pullback of the bar equation, and every subsequent certificate is built using frame joins and genuine B/D rectangles.

**SHARPNESS for Hausdorff nonregular spaces.** If X also fails regularity at any point p (necessarily p∈K), the elementary two-rectangle bar
  s_(p,a)=(a⊠a)∨((X\{p})⊠(X\{p}))
has exact rank3 by A-V-Hausdorff-nonregular-orientation-rigid-rank-two-2026-10-22.md. Thus for this whole compact-exceptional class, the supremum of finite minimum bar ranks equals 2 if X regular and 3 otherwise. In particular every Hausdorff X with FINITELY many nonregular points has universal rank≤3 (finite K) and exact rank3 if nonregular.

**COUNTEREXAMPLE CONSEQUENCE.** Any Hausdorff space supporting a rank≥4 bar must have a set of nonregular points that is NOT contained in any compact subset of X. In particular a compactly supported isolated nonregularity defect, or an entire compact convergent cluster of such defects, cannot give rank4 regardless of the structure of the bar.

**DO NOT MISSTATE:** It is not necessary that the subspace K be locally compact as a complement of a fixed open e in a bridge construction; K is an arbitrary compact subset containing all failure points of ambient regularity. Conversely, the theorem does NOT apply just because the nonregular locus is σ-compact or closed discrete: separating x from the possibly noncompact K\v_x is the crucial global step.

**Scope:** This is a theorem for Hausdorff spatial topological X. Extension to compact sublocales in pointless frames may require a replacement of point/compact-set Hausdorff separation and is not asserted. Universal arbitrary-frame rank3 remains open, and no rank4 bar is constructed.

## STRONGER BAR-SPECIFIC THEOREM: compact one-step residual implies three stages

Let X be ANY Hausdorff space, B ANY rectangular bar, S=D∪B, and define the one-step horizontal-fiber cover
 t_H(B)=∨{b∈O(X):(1,b)∈H(S)}=∨{b:h_S(b)=1}.
Let F_H(B)=X\t_H(B), a closed subset of X.

THEOREM. If F_H(B) is compact, then (1,1)∈H(V(H(S))) (an H→V→H root tree of depth≤3). Dually, if
 t_V(B)=∨{a:(a,1)∈V(S)}, F_V(B)=X\t_V(B)
 is compact, then (1,1)∈V(H(V(S))) (V→H→V depth≤3).

Proof. For each x∈X choose B leaf (u_x,v_x) containing ordinary (x,x), by diagonal pullback of bar equation. Since F_H compact, K_x=F_H\v_x compact and x∉K_x. Hausdorff point/compact-set separation provides disjoint opens U_x∋x, W_x⊇K_x. Let a_x=u_x∩U_x. Then (a_x,v_x) is a B leaf and (a_x,W_x) is a D leaf, so a_x≤h(v_x),h(W_x). For every y∈t_H, by definition of t_H choose b_y∋y with h(b_y)=1, thus a_x≤h(b_y). These second-coordinate opens cover X, so Φ_S(a_x)=1 and (a_x,1)∈V(H(S)). Finally ∨_x a_x=1, establishing H(V(H(S))) root. Dual by transpose.

Thus the global compact-exception theorem follows since every regular second point y lies in t_H(B) (regular shrink proof). The residual F_H(B) is closed and lies entirely in the nonregular point set, so if the latter is contained in a compact subset K, the residual itself is compact.

IMPORTANT NECESSARY CONDITION for orientation-rigid rank3 on a Hausdorff space: if B admits H→V→H depth3 but NO V→H→V depth3, then F_V(B) must be NONCOMPACT; similarly, if V works and H fails, F_H(B) must be noncompact. For a rank≥4 bar, both F_H(B),F_V(B) must be noncompact. These are bar-specific closed residuals, not just global nonregularity. Noncompactness is only necessary, NOT sufficient, for orientation failure.

Concrete illustration: for the elementary H-rigid rank2 bar w=(a⊠1)∨(e⊠e), with e=X\{p} and regularity failing at p, its horizontal fiber t_H=e, so F_H={p} compact; this explains the existence of a V→H→V certificate at depth3 despite failure of V→H at depth2. The dual one-step residual F_V is empty because H→V already works at depth2.

This theorem is independent of localic product spatiality and works solely with frame-sound rectangular bar leaves and ordinary Hausdorff separation of a point from a compact set.

## Further extension: first-countable Hausdorff, countably compact residuals

LEMMA (countably compact set vs. first-countable point). Let X be Hausdorff, x∈X have a countable local base, and A⊆X be countably compact with x∉A. Then there are disjoint opens U∋x and W⊇A. Indeed choose decreasing neighborhood base (U_n)_n at x. Suppose cl_X(U_n)∩A≠∅ for every n. The closed subsets F_n=A∩cl_X(U_n) of A are nonempty and decreasing. Countable compactness supplies y∈∩_n F_n. By Hausdorffness, choose disjoint opens V_x∋x and V_y∋y. For some n, U_n⊆V_x, so y∈cl U_n⊆cl V_x; but V_y is disjoint from V_x and thus from cl V_x, contradiction. Hence some U_n has cl U_n∩A=∅. Take U=U_n, W=X\cl U.

THEOREM. Let X be first-countable Hausdorff, B a rectangular bar, and F_H(B)=X\t_H(B) its closed one-stage residual as above. If F_H(B) is COUNTABLY COMPACT, then B admits H→V→H rank≤3. Similarly countably compact F_V(B) implies V→H→V rank≤3.

Proof: the compact residual proof above needs only separation of each x from A_x=F_H\v_x by disjoint opens. Since A_x is closed in F_H, it is countably compact; x∉A_x since x∈v_x. Apply the new point-vs-countably-compact lemma. All remaining proof steps are unchanged.

COROLLARY. If X is first-countable Hausdorff and its set of nonregular points is contained in a CLOSED COUNTABLY COMPACT subset K, then every rectangular bar has rank≤3 (in both root orientations). Indeed F_H and F_V are closed subsets of K and hence countably compact; apply the theorem in each orientation.

CONCRETE STRICTLY STRONGER EXAMPLE. Let X_0=R equipped with the classical K-topology, K={1/n:n≥1}. Its unique nonregular point is 0. Let Y=[0,ω_1) with the order topology (the space of all COUNTABLE ordinals). This Y is Hausdorff, first-countable, countably compact, but NOT compact. The product X=X_0×Y is Hausdorff and first-countable. Its nonregular locus is F={0}×Y, homeomorphic to Y: if first coordinate ≠0 both factors regular at the point and so is the product; if first coordinate=0 use inverse image of a nonregular neighborhood of 0 to see nonregularity persists in product. F is closed and countably compact, not compact. The theorem gives UNIVERSAL depth≤3 for EVERY rectangular bar on O(X), a case NOT covered by the compact-exception theorem. X is nonregular, so there exists a symmetric two-rectangle bar of EXACT rank3 by the Hausdorff regularity characterization. Thus the optimal universal bound on this noncompact irregular-locus example is exactly3.

CARDINAL GENERALIZATION. Fix infinite κ. If X is Hausdorff and every x has character ≤κ, and if A⊆X is initially κ-compact (every open cover of A of cardinal≤κ has finite subcover), then point x∉A can be separated from A by disjoint opens. Proof: choose a local base (U_i)_{i∈I}, |I|≤κ, and suppose F_i=A∩cl U_i nonempty for all i. Every finite intersection of F_i contains F_j for a base element U_j contained in the finite intersection of U_i, so FIP. Initial κ-compactness gives ∩_iF_i nonempty. Hausdorffness yields contradiction as above. Consequently initially κ-compact F_H(B) implies H→V→H rank≤3 if χ(X)≤κ, with dual statement; global initially κ-compact exceptional nonregular set also suffices. Case κ=ℵ_0 is the main concrete theorem.

NOTE: One must assume that the exceptional countably compact set K is closed (or at least that each residual F_H,F_V is countably compact). A closed subset of a countably compact set is countably compact; an arbitrary subset need not be. No universal arbitrary-locale rank3 proof is claimed.
