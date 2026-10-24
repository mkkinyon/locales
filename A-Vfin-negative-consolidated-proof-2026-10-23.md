# Project A — Consolidated proof: finite-rank bars do not generate the fitted inseparability relation

**23 October 2026 | Correctness status:** both the original cofinite-sheet proof and its finite-rank K-fan input have passed an internal audit and a genuinely blind external audit. The simpler two-generic-point version was suggested by that auditor and independently checked during reconciliation. This is a mathematical consolidation, **not** a novelty or publication-readiness assessment.

## 0. Statement and scope

For a locale X let L=O(X), Q=L⊕L=O(X×_loc X), and let
  d_I = ⋁{u⊠v : u∧v=0}.
The closed inseparability relation is I=C(d_I). An open w∈Q is called a **bar** when w∨d_I=1. Its (rectangular) separation-tree rank rk(w) is the least rank of a well-founded tree using disjointness or w-rectangle leaves and arbitrary horizontal/vertical exact join covers. Leaves have rank 0; internal nodes have rank sup_child(rk(child)+1).

Put V=fit(I)=⋂_{w bar}O(w), V_n=⋂_{w bar,rk(w)≤n}O(w), and V_fin=⋂_{n<ω}V_n (sublocale intersections). This last equality is the intersection over **all finite-rank bars**, not a union of V_n. Because increasing the set of bars decreases the corresponding sublocale, V⊆V_fin.

**Main theorem.** There exists a countable, first-countable, sober T0 topological space X0 for which
   **V(X0) ⊊ V_fin(X0).**
The strictness is witnessed by an ORDINARY POINT p=(ell,r) of the localic product: p belongs to every finite-rank bar but not to an explicit two-rectangle bar q of exact ordinal separation-tree rank ω.

**T1 upgrade.** There also exists a countable, first-countable T1 (non-Hausdorff) space X with V(X)⊊V_fin(X), witnessed by a graph-null bar of hereditary exact rank ω over every nonempty rational parameter interval. No spatiality of either localic square is assumed.

The theorem answers the project's Question A NEGATIVELY. It does not prove V_n⊋V_(n+1) for all n, identify V with a simpler intrinsic formula, establish any novelty priority, or establish that the actual diagonal Δ (rather than I=C(d_I)) is fitted.

## 1. Rectangle calculus and two elementary lemmas

Given any w∈Q define
  D={(u,v)∈L²:u∧v=0},
  B_w={(u,v)∈L²:u⊠v≤w},
  S_w=D∪B_w.
An S_w-separation tree has root (1,1), leaves from S_w, horizontal children (u_i,v) with ⋁_iu_i=u, and vertical children (u,v_j) with ⋁_jv_j=v. Its existence is equivalent to w∨d_I=1 by the standard rectangular C-ideal presentation of frame coproducts. In particular, the construction of such a tree is a LOCALIC proof, not merely a cover of ordinary points in X×X.

For finite depths define H(A) and V(A) by closing a down-set A of rectangle labels under a horizontal or vertical join respectively, and
  R_0^H=R_0^V=S_w,
  R_(n+1)^H=H(R_n^V),   R_(n+1)^V=V(R_n^H).
These are lower sets, and the stages are monotone in n. Two adjacent cover steps in the same coordinate flatten. Thus **any tree of depth≤n can be put into either prescribed first orientation with depth≤n+1** by at most one unary root and padding/flattening. This implication, not a claim of orientation symmetry at equal depths, is all the fan lower bounds need.

**Strip-leaf lemma.** Let Y be a topological space, with C,F disjoint nonempty closed subsets, a=Y\C and e=Y\F. For
  w=(a⊠1)∨(1⊠e)
we have, for opens u,v of Y,
  (u,v)∈B_w ⇔ u≤a OR v≤e.             (1.1)
In fact the family {(u,v):u≤a or v≤e} is already a rectangular C-ideal: it is lower and separately closed under arbitrary joins. It is exactly the C-ideal associated with this two-strip open. The special rectangles (a,1),(1,e) are w leaves.

**Restriction lemma.** If a frame homomorphism h:L→M maps D leaves to D leaves and B_w leaves to B_w' leaves, mapping every node's labels coordinatewise along h sends any well-founded w-tree to a w'-tree of no larger ordinal rank. We will use h as restriction of opens to a clopen or closed subspace. The map must preserve joins AND finite meets; the later extension map E will preserve joins only and will require a separate leaf-repair argument.

## 2. Finite-rank asymmetric K-fan strips

We construct countable first-countable Hausdorff spaces Z_m with disjoint nonempty closed subsets F_m,C_m such that, writing a_m=Z_m\C_m, e_m=Z_m\F_m,
  w_m=(a_m⊠1)∨(1⊠e_m),
we have
  **rk(w_m)=m+1**.                        (2.1)

### Base m=1

Let Z_1 be Q with the classical K-topology restricted to Q, K={1/j:j≥1}, and exceptional point p=0. Away from K use usual rational interval neighborhoods; at points outside K also allow intervals minus K. Set F_1={0}, C_1=K. Both are closed disjoint. The space is countable first-countable Hausdorff.

For every k∈K choose a small ordinary interval u_k about k with 0∉cl(u_k). Then the first-coordinate opens a_1 and the u_k cover Z_1. At (a_1,1) we have a w_1 leaf. At (u_k,1), split vertically into (u_k,e_1), a w_1 leaf, and (u_k,u_k^*), a D leaf. Because e_1∨u_k^*=1, this is an H-first depth-two proof of w_1 barhood.

To exclude V-first depth two on the rectangle (e_1,a_1), note that every neighborhood b of p has closure meeting K. A vertical root split covering a_1 needs a child b containing p. The horizontal one-step leaf fiber against b is
  h(b)=a_1∨b^*,
because b≰e_1. As K⊆e_1\a_1 and cl(b) meets K, e_1≰h(b), so (e_1,b) has no H-leaf cover. Therefore
  (e_1,a_1)∉R_2^V.                       (2.2)
There is no depth-one tree for any proper bar (a root one-axis cover into w leaves would force w=1), so rk(w_1)=2.

### Inductive fan step

Assume Z_m,F_m,C_m are constructed. Take countably many pairwise disjoint **clopen copies** Y_i≅Z_m, i≥1, and adjoin a point t.

If m+1 is even, t is of C colour:
  F_(m+1)=⋃_i F_m^(i), C_(m+1)={t}∪⋃_i C_m^(i),
  U_N={t}∪⋃_{i≥N}e_m^(i).
If m+1 is odd, t is of F colour:
  F_(m+1)={t}∪⋃_i F_m^(i), C_(m+1)=⋃_i C_m^(i),
  U_N={t}∪⋃_{i≥N}a_m^(i).
Declare each old-copy open to remain open, and {U_N} to be a local base at t. As U_N∩Y_i is open, and U_N∩U_M=U_max(N,M), this is a topology. Every Y_i is clopen (its complement contains U_(i+1)); thus Z_(m+1) is countable, first-countable, Hausdorff, and its displayed C,F are disjoint closed subsets.

Set θ_m=V for odd m, θ_m=H for even m, and let σ_m be its opposite. Prove simultaneously:
  (A_m) (1,1)∈R_(m+1)^(σ_m);
  (B_m) (e_m,a_m)∉R_(m+1)^(θ_m).
The base was just proved.

For (A_(m+1)), if t has colour C, then (1,e_(m+1)) is a strip leaf and the second-coordinate opens e_(m+1),Y_1,Y_2,... cover 1. Each (1,Y_i) has an H-first tree copied from A_m, extended without height increase by adding the disjointness child (Z_(m+1)\Y_i,Y_i) at the original H root. A V-root gives depth m+2 and correct σ_(m+1). When t has colour F the argument is transposed: use the first-coordinate cover a_(m+1),Y_i and the strip leaf (a_(m+1),1).

For (B_(m+1)), suppose first that t has colour C, so θ_(m+1)=H and t∈e_(m+1). An H-first putative depth m+2 proof for (e_(m+1),a_(m+1)) must have first-coordinate child u containing t. Then u⊇U_N for some N, so for every i≥N, u∩Y_i⊇e_m^(i), while a_(m+1)∩Y_i=a_m^(i). Restrict the child's V-first tree of depth m+1 to Y_i and then downward-restrict labels to (e_m,a_m); this contradicts B_m, because θ_m=V. If t has colour F use the transpose, finding a second-coordinate child b containing t with b∩Y_i⊇a_m^(i) and θ_m=H. Thus B_(m+1).

A_m gives a depth m+1 bar certificate. A hypothetical certificate of depth≤m can be converted to a θ_m-first alternating tree of depth≤m+1 (by the flatten/pad lemma). Its root label (1,1) would imply (e_m,a_m)∈R_(m+1)^(θ_m), contradicting B_m. Therefore rk(w_m)=m+1.

*Remark.* Some older notes emphasize the symmetric bar s_m=(a_m⊠a_m)∨(e_m⊠e_m). It is NOT the input needed here: we have proved the exact ranks of the ASYMMETRIC strip w_m.

## 3. One asymmetric strip of exact rank ω

Form the topological sum
  Y=⊔_{m≥1}Z_m,
and C=⊔_m C_m, F=⊔_m F_m. These are disjoint nonempty closed sets in the countable first-countable Hausdorff space Y. Define a=Y\C,e=Y\F and
  w=(a⊠1)∨(1⊠e).

Every finite-rank proof tree for w restricts (both coordinates) to Z_m×_loc Z_m, yielding a tree for w_m of the same bounded depth. Since rk(w_m)=m+1 is unbounded, **w admits no finite-rank certificate**.

Nevertheless w is a genuine bar. At a horizontal root cover the first coordinate by the clopen Z_m. Below (Z_m,1), split the second coordinate into Z_m and Y\Z_m. The latter is a D leaf; the diagonal (Z_m,Z_m) supports the old finite w_m tree, with old leaves supported in the clopen component. Thus every branch is finite, although branch lengths are unbounded with m. The root has ordinal rank ω under the convention sup_child(rank(child)+1). Therefore
  **rk(w)=ω.**                          (3.1)

The key point is that Y itself could have V(Y)=I(Y) generated at low fitted rank; we are transferring the **individual strip proof complexity** into a new ambient space where a specific point is preserved by every finite-rank bar.

## 4. Two-generic-point transfer: the central lemma

**TRANSFER THEOREM.** Let Y be ANY topological space with disjoint nonempty closed sets C,F. If the strip w=(a⊠1)∨(1⊠e) is a bar but has no finite-depth separation tree, the following construction produces a space X0 for which V(X0)⊊V_fin(X0).

Take the set X0=Y⊔{ell,r}. Declare W⊆X0 open precisely when W∩Y is open in Y and
  W∩C≠∅ ⇒ ell∈W,
  W∩F≠∅ ⇒ r∈W.                         (4.1)
This is a topology: unions preserve implications existentially, finite intersections preserve them at any common C/F point. The points ell,r are isolated (their singletons are open), and Y is a closed subspace with its original topology. We have
  cl{ell}=C∪{ell},   cl{r}=F∪{r}.         (4.2)

Every old open u⊆Y has a canonical extension
  E(u)=u∪({ell} if u∩C≠∅)∪({r} if u∩F≠∅).     (4.3)
It is an X0-open and
  E(0)=0, E(1_Y)=1_X0, E(⋁_i u_i)=⋁_i E(u_i). (4.4)
We explicitly **do not assert E preserves finite meets**.

Let p=(ell,r), an ordinary localic product point. Define
  a0=X0\cl{ell}=a∪{r},
  e0=X0\cl{r}=e∪{ell},
  q=(a0⊠1)∨(1⊠e0)∈O(X0)⊕O(X0).         (4.5)
Every rectangle missing p has first open missing ell or second open missing r, so q is the GREATEST product-open with p(q)=0. In particular q<1. Its canonical leaf condition is: (U,V)∈B_q iff ell∉U or r∉V.

### Restriction: infinite rank is inherited

Let h:O(X0)→O(Y) be restriction. A D leaf restricts to D. If (U,V) is a q leaf and both u=U∩Y meets C and v=V∩Y meets F, then ell∈U and r∈V by (4.1), contradicting q-nullness. Hence u≤a or v≤e, so the restricted leaf is a w leaf by (1.1). Arbitrary coordinate joins and finite meets are preserved by h. Thus **every** q-tree restricts to a w-tree without increasing rank:
  rk(q)≥rk(w), and no finite-rank bar v≤q exists.       (4.6)
For the last claim, v≤q means every v leaf is also a q leaf, so a finite tree for v is a finite tree for q, impossible by (4.6).

### Lifting: q is actually a localic bar

Transport every internal node (u,v) of a well-founded w-tree to (E(u),E(v)). Its exact H/V covers remain exact by (4.4).

If the old node is a w leaf, then either u≤a or v≤e. In the first case ell∉E(u), in the second r∉E(v). Thus its transported rectangle is a q leaf.

If the old leaf is D, so u∩v=∅, split u=u_a∨u_e with u_a=u∩a,u_e=u∩e; similarly v=v_a∨v_e. These joins are exact because a∨e=1_Y, and they remain exact after E. Replace (E(u),E(v)) by:
  H children (E(u_a),E(v)) [q leaf] and (E(u_e),E(v)).
  Under the latter, V children (E(u_e),E(v_e)) [q leaf] and
  (E(u_e),E(v_a)) [D leaf].
The last two extensions have old traces u_e,v_a, which are disjoint, and new points in disjoint singleton sets: E(u_e) can add ell but not r, and E(v_a) can add r but not ell. Thus their intersection is empty. Every replacement is frame-valid.

Consequently the transported and repaired tree is well-founded and proves
  q∨d_I(X0)=1.                           (4.7)
If the original tree has the finite-branch/unbounded-depth shape of §3, replacement adds at most two edges per branch and preserves ordinal rank ω; combined with (4.6), the displayed q has **exact rank ω**.

### Sublocale strictness at an ordinary point

Take ANY finite-rank bar v on X0. If p(v)=0, then v≤q by maximality of q as the open missing p. Its finite proof would be a finite proof for q, contradicting (4.6). Thus p(v)=1 for EVERY finite-rank bar.

Since the meet of sublocales is their intersection, p belongs to O(v) for all finite-rank v and therefore
  p∈pt(V_fin(X0)).
But q itself is a bar by (4.7) and p(q)=0, so p∉pt(V(X0)). Hence
  **V(X0) ⊊ V_fin(X0).**                  (4.8)
This is the promised counterexample. No assertion about spatiality of X0×_loc X0 was used.

### Separation and sobriety of X0

If Y is countable first-countable T0, so is X0: at y∈C a countable Y-neighborhood basis can be extended via E, with ell mandatory and r avoidable by choosing neighborhoods disjoint from F; similarly for F, and the singleton generic points have singleton basic opens. In particular the Y from §3 is countable, first-countable, Hausdorff and sober, giving countable first-countable T0 X0.

In fact X0 is sober if Y is sober. Let A be a nonempty irreducible closed subset of X0. If ell∈A but A contains a point outside cl{ell}, the disjoint opens {ell} and X0\cl{ell} both meet A, contradiction to irreducibility. So A=cl{ell}. The same holds with r. If A contains neither, then A⊆Y, a closed subspace; it is irreducible closed in sober Y, hence cl{y} for a unique y∈Y. T0 ensures uniqueness. Thus **X0 is sober T0.**

## 5. Cofinite-sheet T1 upgrade

Let L0={ell_t:t∈Q} and R0={r_t:t∈Q} be disjoint ordinary rational sheets, and let X=Y⊔L0⊔R0. A set W is open iff its Y-trace is Y-open, its rational traces W_L,W_R are usual rational opens, and
  W_Y∩C≠∅ ⇒ W_L cofinite in Q,
  W_Y∩F≠∅ ⇒ W_R cofinite in Q.          (5.1)
These conditions define a topology. Both rational sheets are open, Y is a closed subspace carrying its old topology, and when Y is countable first-countable T1, so is X (but X is not Hausdorff).

For old u define E(u)=u plus the WHOLE left sheet if u meets C, plus the WHOLE right sheet if u meets F. E preserves all joins, zero and top. Old w leaves map to graph-null leaves; each old D leaf is repaired by the SAME H-V split in §4, because E(u∩e) can add only the left sheet and E(v∩a) only the right sheet. Thus the largest null open q of the rational graph
   g:Q→X×_locX,  t↦(ell_t,r_t),
is a proper bar. On the explicit input ω tree, rk(q)≤ω.

For every nonempty open rational parameter J⊆Q define q_J as greatest open with J∩g*(q_J)=∅. A canonical q_J-null rectangle (U,V) obeys
   U_L∩V_R∩J=∅.                      (5.2)
If U∩Y meets C and V∩Y meets F, then U_L and V_R are cofinite, so they meet each other inside EVERY nonempty rational-open J. Contradiction. Thus each q_J leaf restricts to an old w leaf; D leaves and arbitrary covers also restrict. Hence rk(q_J)≥rk(w)=ω for ALL nonempty J. Since q≤q_J, ranks cannot increase, so rk(q_J)=ω.

Any finite-rank bar v with g*(v) nondense would vanish on some nonempty rational open J and satisfy v≤q_J, contradicting infinite rank. Therefore all finite-rank bars pull back densely. For any t with t∧v≤q, its pullback satisfies g*t∧g*v=0; density gives g*t=0, hence t≤q by maximality. Thus v→q=q for every finite-rank bar v, and their join nucleus j_fin fixes q. But q itself is a bar, so the full fitted-hull nucleus j_V sends q to q→q=1. Since q<1,
   **V(X) ⊊ V_fin(X)** on a COUNTABLE FIRST-COUNTABLE T1 space.

This is the genuine T1 strengthening. It does not assert T1+Hausdorff or sobriety of X, and does not infer the localic square is spatial.

## 6. Dependency audit and notes for a shorter write-up

The negative theorem requires only: (i) a bar w of the special strip form on Y with *some* well-founded proof and no finite-depth proof; (ii) the elementary restriction lemma; (iii) the join-preserving E lift and D-leaf repair; and (iv) the ordinary-point or graph-density witness. Exact rank ω is a pleasant corollary for the selected Y, not logically essential.

The cofinite-sheet example cannot be dismissed by the old clopen-disjoint-union theorem: each old Z_m is clopen IN Y, but is closed and NOT open in graphized X, because Z_m meets C but contains no rational left-sheet point.

No novelty priority is asserted. The project calls the closed inseparability sublocale I=C(d_I), and V=fit(I); it is not claiming that the actual diagonal Δ is fitted. The hierarchy concerns rank of rectangular C-ideal separation trees, not finite generation of a nucleus by finitely many open nuclei.

For the external blind check already completed, see A-V-fin-negative-independent-audit-reconciliation-and-generic-points-2026-10-23.md. Future independent manuscript review should use this consolidated note rather than the older lengthy exploratory packets.
