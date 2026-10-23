# Rank three for full-interval rational bridges with ARBITRARY boundary topology

22 October 2026. Main result: the locally compact boundary hypothesis can be entirely removed from the rank-three calculation and even from barhood for the FULL-INTERVAL attachment class. Proof is a direct H→V→H separation-tree construction, valid without assuming the localic square spatial.

## The bridge space

Let Z be ANY topological space, and let α,β:Z→R\Q be continuous functions satisfying α(z)≠β(z) for every z. Define X as two disjoint open copies L_0,R_0 of Q, together with Z. At every z∈Z basic neighborhoods are
 N(z;I,J,V)=ℓ[I∩Q] ∪ r[J∩Q] ∪ {z'∈V:α(z')∈I and β(z')∈J},
where I,J⊂R are open intervals with α(z)∈I, β(z)∈J, and V is a Z-open neighborhood of z. Continuity ensures these sets define a topology whose induced topology on Z is the original one, with open rational sheets and Z closed. If α,β are each injective, X is Hausdorff (separate distinct bridge points by disjoint left and right intervals; bridges from rational points by irrationality).

Let γ(t)=(ℓ_t,r_t):Q→X×locX. Let q be the largest γ*-null tensor open, τ flip factors, and s=q∧τ(q). For u,v∈O(X), the canonical B_s leaf condition is EXACTLY
  u_L∩v_R=∅ and u_R∩v_L=∅
for rational-index traces, with no conditions on the boundary traces directly. Let D={(u,v):u∧v=0} and S=D∪B_s.

## THEOREM: universal H-V-H rank bound for this construction

For EVERY topology of Z and every continuous α,β as above with pointwise α(z)≠β(z), the relation S admits a well-founded H→V→H separation tree rooted at (1,1) with maximum edge depth THREE. In particular, s∨d_I=1 automatically: B_s is a genuine bar WITHOUT invoking any localic boundary spatiality lemma or compactness of Z.

**First-coordinate root cover:** Put e=L_0∨R_0. Fix z∈Z. Choose CLOSED bounded real intervals A_z,B_z with α(z)∈int A_z, β(z)∈int B_z, and A_z∩B_z=∅. Define
 V_z={x∈Z:α(x)∈int A_z and β(x)∈int B_z}
(open by continuity, contains z) and a_z=e∪V_z∈O(X). The opens a_z (and e if Z empty) cover 1. Claim: each a_z is V→H-good, i.e. Φ_s(a_z)=1.

**For each second point y pick b_y∋y so that a_z≤h_s(b_y)=∨{u:(u,b_y)∈S}.**

1. y=ℓ_t. Since A_z,B_z disjoint compact intervals, choose a small real rational interval H about t whose closure avoids at least one of A_z,B_z. Put b_y=ℓ[H]. For first rational points ℓ_t' use same-sheet symmetric graph-null leaves; first rational r_t' use D leaves. For any first bridge x∈V_z, if H avoids A_z choose u_x near x with LEFT rational trace avoiding H (D leaf, because b_y⊆L); if H avoids B_z choose u_x near x with RIGHT rational trace avoiding H (B_s leaf). Thus a_z≤h_s(b_y).

2. y=r_t. Symmetric: choose H about t avoiding A_z or B_z. For first rational r_t' use same-sheet graph-null leaves, first rational ℓ_t' use D leaves; for first bridge x∈V_z choose either D or B_s via avoidance on the appropriate trace.

3. y∈Z. Choose small closed-disjoint real intervals I about α(y), J about β(y), such that NEITHER closure(I) NOR closure(J) meets BOTH A_z and B_z. This is possible because A_z,B_z are disjoint compact intervals and α(y)≠β(y). Choose b_y=N(y;int I,int J,W) for some Z-open W∋y (the traces lie inside I,J).

  For any first rational ℓ_t: if t∉closure(I), choose first L-open disjoint b_y (a D leaf). Otherwise t∉closure(J), since I,J have disjoint closures; choose first L-open avoiding b_y right trace J (a B_s leaf). First rational r_t handled with I,J reversed.

  Fix first bridge x∈V_z, with A=α(x)∈int A_z and B=β(x)∈int B_z. We claim at least one of:
    (D) A∉closure(I) AND B∉closure(J);
    (N) A∉closure(J) AND B∉closure(I).
  Combinatorial proof: if both fail, (A∈cl I or B∈cl J) and (A∈cl J or B∈cl I). Expanding gives 4 alternatives: A in both cl I and cl J (impossible since disjoint closures), B in both (same), A and B both in cl I (impossible because cl I does not meet both A_z and B_z), or A and B both in cl J (same). Therefore D or N holds. If D, shrink bridge first neighborhood u_x so its left/right rational traces avoid I/J respectively, and its Z trace (controlled by α,β) is disjoint from b_y's Z trace: u_x∧b_y=0. If N, shrink u_x so its LEFT trace avoids J and RIGHT trace avoids I: u_x⊠b_y≤s by both forward/reverse graph-null tests. Hence every first x∈V_z lies in h_s(b_y).

In every case b_y∋y and a_z≤h_s(b_y). Since as y varies b_y cover all of X, 1=∨_y b_y≤Φ_s(a_z), giving Φ_s(a_z)=1. Therefore each (a_z,1) admits a V→H subtree of depth≤2. Root horizontally splits into a_z, covering 1, and these subtrees yield a valid H→V→H tree of height3. This proves localic barhood as a consequence of actual coordinatewise leaf-cover derivation.

NOTE for Z empty: X=L⊔R, which is Hausdorff regular, and the root easily has depth≤2; alternatively take e=1 and repeat easy-fiber argument.

## EXACT RANK THREE under diagonal-density of attaching pairs

Assume in addition:
  for every nonempty real interval J there exists z∈Z with α(z)∈J and β(z)∈J.

Then no depth≤2 tree exists. For every first-open a meeting L_0 choose rational interval J with ℓ[J]⊆a and bridge z with α(z),β(z)∈J. Then z∈cl_X(a) and z∉a*. Any B_s leaf (u,v) with a≤u forces v_R∩J=∅ by forward graph-nullness. But any v containing z has right rational trace intersecting J, because β(z)∈J. Thus z∉∨_{(u,v)∈B_s,a≤u} v, so a fails the depth-two H→V criterion. Symmetric argument for second-open b meeting R_0 rules out V→H. Hence rank≥3 and the upper bound makes rank exactly3.

## EXPLICIT NONLOCALLY COMPACT BOUNDARY

Enumerate a rational interval basis (J_n), infinitely many J_n⊂every nonempty rational interval. Let Z=⊔_n Q_n, where Q_n=Q∩(-ε_n,ε_n) in its usual topology, and choose distinct irrational constants α_n,β_n∈J_n so close to interior that α_n+Q_n and β_n+Q_n are subsets of J_n. Arrange all α_n,β_n in different cosets modulo Q (possible inductively). Define on Q_n:
  α(n,t)=α_n+t, β(n,t)=β_n+t.
Both α,β are continuous injections into irrationals, their images are disjoint, and α(n,t)≠β(n,t). X as above is Hausdorff; its boundary Z is a NONLOCALLY COMPACT topological sum of rational intervals, so the previous locally compact boundary lemma does not apply. Yet the direct tree proves s∨d=1 and rank≤3. Because for each J_n, the point (n,0) has α_n,β_n∈J_n, the diagonal-density hypothesis holds and rank=3 EXACTLY.

Therefore genuine NONLOCALLY COMPACT boundary structures and arbitrarily many bridge clusters do not raise this full-interval graph-null separation bar above rank3. Neither universal (*) for all frames nor existence of rank4 is established. Any higher-rank bridge construction must alter the attachment geometry, not merely the topology or compactness of Z.

## Sharp barhood criterion (added after first proof)

The pointwise condition α(z)≠β(z) is also NECESSARY for forward graph-null barhood, and hence for symmetric barhood. If α(z)=β(z)=t (an irrational) at some bridge point z, then every pair of open neighborhoods u,v of z has first-left rational interval around t in u and second-right rational interval around t in v. Their rational index traces intersect, so u⊠v cannot lie below q (and a fortiori cannot lie below s). Because all opens in O(X)⊕O(X) are joins of rectangles, the ordinary product point (z,z) is not contained in q. Also it is not in d_I: every disjointness rectangle a⊠b avoids all ordinary diagonal pairs. Thus q∨d_I≠1, and s∨d_I≠1. The sufficiency of pairwise α(z)≠β(z) for s∨d_I=1 is proved by the H-V-H tree above. Therefore for full-interval rational-bridge attachments:
  q∨d_I=1 iff s∨d_I=1 iff α(z)≠β(z) for EVERY z∈Z.
This equivalence is independent of compactness, local compactness, soberness, or spatiality of the localic square (although X is an ordinary topological space in the setup).
