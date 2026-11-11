# Binary feedback II — Complete triangle-wedge hierarchy and unbounded finite formal-hull ranks at fixed homotopy type

**10 November 2026. New internally checked working mathematics, not externally audited.** Continues [rectangle groupoids and relative skeleta](PointFree_binary_rectangle_pi1_relative_skeleton_2026-11-10.md) and the [binary feedback roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md). Uses the [canonical coherent composition calculus](ProjectA_coherent_composition_canonical_proof_2026-11-08.md), the separately audited coherent identity U=cl D=I², and the [audited pointed face-poset gluing theorem](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md). The closed-stage iteration convention comes from [the earlier formal hull paper](A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md). No novelty or intrinsic-shape claim.

## 0. Coherent calculus and notation

Let P be the six-element face poset of a triangle boundary with vertices v,a,b and edges p={v,a}, q={v,b}, r={a,b}. Let S be a nonempty Stone space with at least two points, and X=W_S(P,v), with one shared minimal vertex v. Nonshared points have labels a_s,b_s,p_s,q_s,r_s. Put E_s={p_s,q_s}, B_s={a_s,b_s,p_s,q_s}. Thus ↑v={v}∪⋃E_s and ↓↑v={v}∪⋃B_s. The order has spectral opens as upsets.

For coherent X, I=cl Δ (common upper), D=fit Δ (common lower), U=W=cl D=I², V=fit I=D². Closure and fitting of any proconstructible spectral relation are respectively down/up saturation in the product order. Finite composition, finite joins and meets stay proconstructible and are determined by patch-closed point sets. Write H for least simultaneously closed and fitted sublocale containing Δ, F for functional equivalence, M=I∧D, J=I∨D and T(R)=cl(R)∧fit(R). All formulas below concern these actual localic sublocales, not arbitrary point-set differences.

## 1. Complete cross-fibre formulas

For distinct s,t and nonshared x_s,y_t:
- I: no pair. Any upper witness of a nonshared point lies in its own fibre.
- D: iff x_s∈E_s and y_t∈E_t. Only possible common lower witness is v.
- U=W: iff x_s∈B_s and y_t∈B_t. Apply downward saturation to D; upper extensions of nonshared coordinates stay in their fibres.
- V: iff x_s∈E_s OR y_t∈E_t. For the necessity, a lower pair in I must have at least one coordinate v (otherwise they are in distinct fibres). For sufficiency, if e.g. v≤x_s then every y_t has a lower extension z_t I-related to v: use itself for a,b,p,q and a_t for r_t. Thus (v,z_t)∈I lies below (x_s,y_t).

Within a single fibre the restrictions of I,D,U,V agree with the finite P relations. Indeed the order-preserving folding map X→P is a retraction of each fibre; existential positive witness formulas are preserved by each map. I on P is comparability plus ordered pairs of distinct vertices; D is comparability plus ordered pairs of distinct maximal edges; U(P)=V(P)=P² since any two maximal edges share a vertex and any two minimal vertices have a common upper edge. In particular v is U- and V-related to every point.

These formulas specify all label blocks as empty, S×S, or Δ_S (for nonshared labels), and the v-blocks as empty or S. More precisely, if a cross-fibre label block is allowed, its same-fibre entries are allowed as well, so the full block is S×S. Otherwise it is Δ_S or empty according to the finite relation. This proves patch-closedness directly and agrees with the coherent calculus. Do NOT identify S²∖Δ_S with a compact Stone object. Its complement in a full label block is patch-open and may not be compact.

## 2. Lower and upper diamonds and the formal hull

M=I∧D is exactly symmetric comparability (including Δ). J restricts in each fibre to comparable pairs, vertex/vertex pairs and edge/edge pairs, omitting the six ordered nonincident vertex-edge pairs. Across fibres J=D, i.e. E_s×E_t.

Since cl J=U and fit J=V, T(J)=U∧V. It is strictly larger than J: inside a fibre any nonincident vertex-edge pair is in U∧V but not J. Also cross-fibre (a_s,p_t) is in U∧V but not J. The cross-fibre block of U∧V consists of B_s×B_t with at least one incident-edge coordinate, hence 12 entries. U and V incomparable: (a_s,b_t)∈U∖V and (p_s,r_t)∈V∖U. Their union has 20 cross-fibre entries.

Compute cl V=I³: within fibres full; across distinct fibres iff x_s∈B_s OR y_t∈B_t. Indeed upper extensions of the coordinates stay in their respective fibres, and at least one must have an incident-edge upper extension. Only excluded cross pair is (r_s,r_t). Thus U∨V<cl V, since (a_s,r_t) lies in cl V but neither U nor V. Also fit U=D³=X², since every nonshared point has a lower extension in its fibre B_s, and all pairs involving v already lie in U. In particular all points are connected by finite comparability paths through v. H=X² (every up/down saturated relation containing Δ must contain all pairs along these coordinate paths), and F=X² (any real-valued map is constant on comparable points and hence on all points; alternatively H⊆F). All localic equalities are justified by proconstructibility; for H the finite iteration below reaches X².

The exact closed-stage iteration starting at I is
\[
C_0=I,\qquad C_1=\operatorname{cl}(\operatorname{fit}I)=I^3,\qquad C_2=I^5=X^2.
\]
Indeed I graph distance from v is one for B_s, two for r_s. Across fibres an I-path must pass through v, so distance between r_s and r_t is four. Every distance is at most four. Thus I³<X²=I⁴, and the first fixed closed stage is exactly 2. This is the previously defined cf iteration; do not confuse it with W₂ from the separate compact noncoherent question.

Strict Hasse pattern among displayed relations:
Δ < M < I,D < J < T(J)=U∧V < U,V < U∨V < cl V < H=F=fit U,
with I∥D and U∥V. W=U. Each branch strict for |S|≥2, and no additional comparabilities between the two pairs of incomparable branches. This example witnesses strictness of the lower-diamond J<T(J) and upper-diamond W∨V<H while the canonical C→I,D are both equivalences.

Finite checks for |S|=m: |X|=1+5m, |I|=1+23m, |D|=1+23m+4m(m−1), |U|=|V|=1+35m+16m(m−1), |cl V|=1+35m+24m(m−1), |H|=(1+5m)². Direct exhaustive finite enumeration in JS confirmed these block formulas and I⁴=D³=X² for m=1,2,3,4. For m=2, sizes 47,55,103,103,119,121 respectively; m=3 sizes 70,94,202,202,250,256; m=4 sizes 93,141,333,333,429,441. Equality of finite U,V cardinalities does not assert an unmarked sheaf isomorphism. Their cross-block geometric decompositions differ.

## 3. General pointed-fibre observation and arbitrarily large finite H rank

For a finite connected poset P (connected comparability graph) and minimal v, W_S(P,v) has no I edges between distinct nonshared fibres. By the fold and the fibre inclusions, graph distances for I within a fibre agree with those in I(P). For s≠t and nonshared points x_s,y_t, every I path passes through v, hence
\[
d_{I(W)}(x_s,y_t)=d_{I(P)}(x,v)+d_{I(P)}(v,y).
\]
Let d=max_{x∈P}d_{I(P)}(x,v). For |S|≥2, the I graph diameter is exactly 2d (when d≥1; choose a farthest x in two fibres), since distances within one fibre are at most 2d by routing via v. All points are connected, H=F=X², and I^k=X² iff k≥2d for d≥1 (reflexivity permits padding). By the established odd-power formula for closed stages C_n=I^{2n+1}, the first fixed closed stage is exactly d. Proof: C_d=full, C_{d−1}≠full; any earlier fixed stage would remain fixed forever. For singleton P, d=0 and X is a point, rank zero.

**Fixed nonconstant common homotopy, arbitrary finite rank.** For each integer ℓ≥2, let T_ℓ be the simplicial graph consisting of a triangle boundary with a path of ℓ edges attached at v, with all other path vertices new. Take P_ℓ=F(T_ℓ) and W_ℓ=W_S(P_ℓ,v). The I graph on P_ℓ has vertex adjacency along T_ℓ, edges adjacent only to their endpoints (and themselves); therefore the terminal path vertex has I-distance ℓ from v, the last path edge also has distance ℓ, and all triangle face points have distance ≤2. Thus d=ℓ. The canonical comparisons are equivalences by the audited finite face-poset criterion and pointed Stone gluing. Since the path retracts to v by a pointed homotopy,
\[
\mathbf C(W_\ell)\simeq\mathbf I(W_\ell)\simeq\mathbf D(W_\ell)
\simeq h(S)_+\wedge\underline{S^1},
\qquad \text{first fixed closed H stage}=\ell.
\]
The equivalences of common homotopy types respect the indicated common basepoint and may be obtained via the inclusions of the original triangle into the whiskered graph; naturality of chain and hull inclusions gives equivalences of the canonical arrow diagrams (each leg is an equivalence). For infinite S the shared object has nonconstant H_1=Z[h(S)], as previously audited. Hence even the common **nonconstant** homotopy object and canonical comparison diagram do not bound the number of finite formal-hull stages. For S Cantor, all compact-open lattices are countable. A path alone provides a terminal common object of arbitrary rank, but the circle plus whisker is stronger.

The construction has no implication for transfinite ranks beyond those already studied, nor for the noncoherent W₂ question. It is a negative answer to a particular feedback question: unfiltered C/I/D homotopy cannot determine or even bound formal hull rank. A useful positive future test is the relation-distance filtration or higher rectangle constructions retaining distance, rather than total realization. Another is to ask for homotopical comparison obstructions within a fixed exact hierarchy pattern. These new deductions are working, not externally audited.
