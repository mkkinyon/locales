# Compact-boundary tube uniformization for rank-three bars

Date: 22 October 2026.

**General H-V-H theorem.** Let X be a Hausdorff space, e∈O(X) an open subset, and Z=X\e a locally compact Hausdorff closed subspace. Let S⊆O(X)×O(X) be a lower family of allowed terminal rectangles (e.g. D∪B_w). Let h_S(b)=∨{u:(u,b)∈S}. Assume:

(I) **Pointwise terminal cover:** every pair (x,y)∈X×topX lies in some ordinary rectangle u×v with (u,v)∈S.
(II) **Easy open-part uniformization:** for every y∈X there is an open neighborhood c_y of y with e≤h_S(c_y).

Then the root (1,1) admits a separation-tree certificate of edge depth ≤3 and shape H→V→H, using only S-leaves.

Proof. For any z∈Z choose relatively compact Z-open V_z∋z, with compact closure K_z=cl_Z V_z. The open a_z=e∪V_z belongs to O(X) because e is open, Z is closed, and V_z is open in Z. We prove a_z is V→H-good. Fix y∈X. Choose c_y∋y with e≤h_S(c_y) by (II). By (I), for every x∈K_z choose a terminal leaf rectangle u_x×v_x containing (x,y). Its first opens u_x cover compact K_z, so finitely many u_1,...,u_m suffice. Put b_y=c_y∧v_1∧...∧v_m. Then b_y contains y; since b_y≤c_y and h_S is antitone, e≤h_S(b_y). Since b_y≤v_i and S is lower, (u_i,b_y)∈S, hence u_i≤h_S(b_y). Therefore h_S(b_y) contains e∪K_z as a SET, so a_z=e∪V_z≤h_S(b_y). The b_y cover X as y varies, hence Φ_S(a_z)=∨{b:a_z≤h_S(b)}=1. Thus (a_z,1) admits a V→H tree of depth≤2. Finally ∨_{z∈Z} a_z=1 (if Z empty then e=1, and the same easy-fiber hypothesis directly gives (1,1)∈V H S). Horizontal root cover by a_z proves H→V→H depth≤3.

This theorem does not assume the localic product X×locX spatial. The argument works with pointwise rectangles solely to build genuine frame-open coordinate covers in O(X). The stronger localic barhood w∨d=1 may be established separately, e.g. by the locally compact boundary lemma.

**Application: full-interval rational bridge attachments.** Let Z be ANY locally compact Hausdorff space and alpha,beta:Z→R\Q continuous with alpha(z)≠beta(z) for every z. Form X from two disjoint OPEN rational copies L,R plus Z, with bridge basic neighborhoods
 N(z;I,J,V)=ell[I] ∪ r[J] ∪ {z'∈V:alpha(z')∈I, beta(z')∈J},
for real intervals I∋alpha(z), J∋beta(z) and Z-open V∋z. Assume the resulting X is Hausdorff (e.g., alpha and beta separately injective, so rational traces of neighborhoods of distinct bridge points can be made disjoint in both sheets). Let gamma(t)=(ell_t,r_t), q largest gamma*-null open, and s=q∧tau(q).

1. For x≠y in X, Hausdorffness gives a D leaf around (x,y). At x=y∈L or R, same-sheet rectangles are s-null. At x=y=z∈Z, choose bridge U around z with disjoint left and right rational trace intervals I,J (possible alpha(z)≠beta(z)); then U⊠U≤s. Hence D∪B_s covers every ordinary pair. 
2. Let e=L∨R. For each y∈X we can choose c_y∋y with e≤h_s(c_y).
 - y∈L: choose c_y⊆L, then first L has s-null leaves and first R has D leaves; likewise y∈R with roles swapped.
 - y=z: choose c_y bridge neighborhood with left/right rational trace intervals I,J having disjoint closures. For any first ell_t, if t∉cl I choose a disjointness neighborhood in L avoiding I; if t∈cl I choose a symmetric graph-null neighborhood in L avoiding J. For any first r_t argue symmetrically. Therefore every first rational point belongs to h_s(c_y), so e≤h_s(c_y).

The general theorem gives H→V→H depth≤3 for B_s.

BARHOOD: e⊠e≤d∨s (same-sheet blocks s-null, opposite-sheet blocks D). Since Z is locally compact, use the boundary reflection lemma with pointwise cover in (1) to obtain d∨s=1 in localic square. Thus B_s really is a bar. The bar may have extra off-diagonal graph closure at (z,z') when alpha(z)=beta(z') for DISTINCT bridge points; this is harmless, since those pairs are separated by D. Consequently it is NOT necessary to demand alpha(Z)∩beta(Z)=∅, only pointwise alpha(z)≠beta(z).

STRICTNESS: If for every nonempty rational interval J there is z with alpha(z),beta(z)∈J, the usual depth-two obstruction survives: for any a meeting L choose rational J with ell[J]⊆a, and z with both attaching limits in J; z∈cl a\(a*∨F_Bs(a)); similarly the V→H case. Thus rank(B_s)=3 exactly.

**Importance:** This is an actual H-V-H normalization theorem for an entire class of NONCONTINUOUS frames, with no bound on size/character of the locally compact boundary Z. It subsumes the nested compact-cluster example A-V-genuine-nested-rational-bridge-exact-rank-three-2026-10-22.md and allows cross-limit collisions at distinct bridge points, which can enlarge the ordinary graph closure but do not interfere with barhood.

Any rank-four bridge construction must defeat one of the structural hypotheses, especially the compact tube plus 'easy open part' property, or use a boundary too non-locally-compact for the boundary reflection lemma. No universal arbitrary-frame (*) theorem and no rank-four witness are asserted.
