# Project A: all-stage local-compactness derivative bounds for rectangular bars

23 October 2026. **New working structural theorem, complete proof below.** The central purpose is to study the WHOLE hierarchy V_(n+1)⊆V_n, not merely the isolated V4>V5 case. No new strict fitted stage is claimed. This note assumes X is an ordinary topological space and uses its spatial frame L=O(X), but does NOT assume the localic product X×loc X is spatial, or that X is Hausdorff/regular/coherent.

## 1. Definitions and a compact-avoidance principle

Let Q=O(X)⊕O(X), d_I be the join of disjointness rectangles. Fix any bar q∈Q, so q∨d_I=1. Put
  S={(u,v)∈O(X)²: u∩v=∅ or u⊠v≤q}.
This is a down-set and its well-founded horizontal/vertical proof trees compute the bar condition.

For u∈O(X), define the closed bad fiber
  K(u)=X\bigcup{v∈O(X):(u,v)∈S}.
Then K is monotone: u≤u' ⇒ K(u)⊆K(u'); and
  (u,b)∈V(S) iff b∩K(u)=∅.

**Compact avoidance lemma.** For any ordinary x∈X and compact C⊆X, there exists u∋x with K(u)∩C=∅. If a is any given open neighborhood of x, u can be chosen with u⊆a.

Proof. For each y∈C, evaluating q∨d_I=1 at the ordinary product point (x,y) supplies a rectangle (u_y,v_y)∈S containing (x,y). The v_y cover compact C. Select finitely many and put u=a∩⋂u_y. It is a neighborhood of x, and the corresponding v_y remain S leaves against u, so the union of those v_y covers C; hence K(u)∩C=∅. No product spatiality or separation assumption.

If a⊠a≤q and u⊆a, then K(u)⊆∂a=cl_X(a)\a. Indeed (u,a) is a q leaf, so K(u) avoids a; (u,X\cl_X u) is a D leaf, so K(u)⊆cl_X u⊆cl_X a. This is the **frontier support lemma**.

## 2. Iterated non-local-compactness derivatives

For a CLOSED F⊆X, define D(F)={y∈F: F has no compact neighborhood of y in the subspace F}. Then D(F) is closed in F and X; compact-neighborhood points form an open subset. Define D^0(F)=F and D^(m+1)(F)=D(D^m(F)).

Closed heredity: if A⊆F is closed in F, then D(A)⊆A∩D(F), because a compact neighborhood in F restricts to a compact neighborhood in A. Inductively, D^m(A)⊆A∩D^m(F).

Define C_m^H(S)=H(V(H(V(...S)))) with 2m+2 alternating operations, outermost H; and C_m^V(S)=V(H(V(...S))) with 2m+1 operations, outermost V. They are rooted tree families of those maximum depths.

**UNIFORM RELATIVE RANK THEOREM.** Let a,b be opens and F⊆X closed. Assume K(u)⊆F for EVERY open u⊆a.

(A_m) If D^m(F)∩b is contained in some compact set C⊆X, then
    (a,b)∈C_m^H(S), a tree of depth≤2m+2.

(B_m) If D^m(F)∩b=∅, then
    (a,b)∈C_m^V(S), a tree of depth≤2m+1.

Proof, simultaneous induction on m.

Base A_0: F∩b⊆C compact. For each x∈a choose u_x⊆a with K(u_x)∩C=∅ by compact avoidance. Since K(u_x)⊆F, its intersection with b is empty; hence (u_x,b)∈V(S). These u_x cover a, giving H(V(S)), depth2.

Base B_0: F∩b=∅ gives b∩K(a)=∅, so (a,b)∈V(S), depth1.

Inductive A_m, m≥1: Choose compact C containing D^m(F)∩b. For each x∈a choose u_x⊆a, x∈u_x, with K(u_x)∩C=∅. Put F_x=K(u_x), a closed subspace of F, and note K(v)⊆F_x for every v⊆u_x. Closed heredity gives
 D^m(F_x)∩b ⊆ F_x∩D^m(F)∩b ⊆F_x∩C=∅.
Thus G_x=D^(m−1)(F_x) is locally compact at EVERY point y∈b∩G_x. Because G_x is closed in X, for each y∈b there is open b_xy⊆b containing y for which G_x∩b_xy lies in a compact subset of G_x (if y∉G_x, take b_xy disjoint from G_x; otherwise use local compactness at y). Apply A_(m−1) to (u_x,b_xy), with closed controlling set F_x, obtaining an H-first tree of depth≤2m. The b_xy cover b, so (u_x,b) has a V-first tree of depth≤2m+1. The u_x cover a, so (a,b) has an H-first tree of depth≤2m+2.

Inductive B_m, m≥1: If D^m(F)∩b=∅, every y∈b∩D^(m−1)(F) is a locally compact point of G=D^(m−1)(F). Choose open b_y⊆b containing y with G∩b_y contained in a compact set; for y∈b\G use an open b_y disjoint from G, possible because G is closed. Apply A_(m−1) to (a,b_y), obtaining H-first trees of depth≤2m, and join them in the vertical coordinate to obtain a V-first tree for (a,b), depth≤2m+1.

All joins are the coordinate joins of O(X) in the rectangular C-ideal calculus. No compactness of X or spatiality of Q is assumed.

## 3. Null-square frontier theorem and global consequence

If a⊠a≤q, the frontier support lemma allows F=∂a, and b=X. Hence:

  D^m(∂a) compact ⇒ (a,1) has rank≤2m+2;
  D^m(∂a)=∅ ⇒ (a,1) has rank≤2m+1.

Examples: compact ∂a gives depth2; locally compact ∂a (D∂a=∅) gives depth3; compact D(∂a) gives depth4; compact D²(∂a) gives depth6. These are universal sufficient bounds and are NOT asserted sharp.

**GLOBAL UNIFORM COROLLARY.** If every x∈X belongs to some open a_x with a_x⊠a_x≤q and D^m(∂a_x) compact, then q has a global separation tree of depth≤2m+3 (a horizontal first cover by the a_x, followed by the local trees). If D^m(∂a_x)=∅ for all x, the bound improves to ≤2m+2.

**Necessary higher-rank obstruction.** If rk(q)>2m+3, there is a point x such that EVERY graph-null self-neighborhood a of x has NONCOMPACT D^m(∂a). If rk(q)>2m+2, there is a point x such that EVERY such neighborhood has NONEMPTY D^m(∂a). (In the latter statement, if rank>2m+2, each x might have good a with D^m empty giving a global tree≤2m+2; contrapositive is valid.) This statement is only meaningful when self-null opens exist near every x; if not, the obstruction point may have no such neighborhood, and the quantified condition is vacuous. For a graph-null bar, barhood gives self-null neighborhoods at every ORDINARY diagonal point: from a q rectangle around (x,x), take its coordinate intersection.

Thus, in the case of rational graph-null bars on ordinary X, prospective arbitrary finite fitted-rank jumps require successive **noncompact non-locally-compact frontier kernels** at an ordinary point in every parameter restriction J.

## 4. Null-square opens cannot enclose a dense family of bridge-center points

For canonical rational graph g(t)=(ell_t,r_t), if a⊠a≤q then the rational index opens a_L,a_R⊆Q are DISJOINT. Consequently the closed set
    cl_R(a_L)∩cl_R(a_R)
has empty interior in R: otherwise a_L,a_R would be disjoint relatively OPEN DENSE subsets of some nonempty rational interval, impossible.

Suppose T is a set of boundary points t_lambda each having the property that every neighborhood of t_lambda has BOTH rational sheet traces accumulating at a specified irrational lambda. If a contains t_lambda, then lambda∈cl_R(a_L)∩cl_R(a_R). Therefore no q-null-square open a can contain points t_lambda with lambda dense in a real interval.

In the independently audited rank-four bridge example the upper bridge centers lambda_k are dense in R, with exactly this two-sided trace property. Thus a new single q-null top neighborhood CANNOT contain the entire dense old obstruction family. The naive 'put the old X4 module inside one new top' amplifier fails for a uniform, all-rank reason. An iterated construction would have to localize the old modules into nowhere-dense nested clusters and re-densify at the next global level, rather than stack the whole hereditary family at one point.

## 5. Inductive mechanism under investigation, not established

A possible reusable n→n+1 mechanism would use a tree of nested, pairwise disjoint irrational-centered support intervals; over each parent, child centers converge to its center and occupy disjoint intervals, so the parent admits a null-square neighborhood. A second family of auxiliary *filter points* would carry the opposite polarity; each filter must be able to discard any FIXED child branch. Otherwise barhood fails at an ordinary pair (the already proved super-anchor no-go). At global scale take densely many root centers to ensure every rational parameter interval J encounters an obstruction.

An actual theorem would have to verify three assertions UNIFORMLY in n: (i) the graph-null open is a localic bar, by an explicit height-controlled C-ideal tree; (ii) both orientation lower bounds persist for every parameter interval J, preferably using the bad-kernel recursion; (iii) no rank≤n generator moves the closed graph residual, by hereditary graph density. The derivative theorem in §2 provides a universal screening condition on (i)/(ii), but does not supply this induction by itself.

**STATUS:** no new V4>V5 example, no all-n strictness theorem, and no decision on V_fin=V. The genuine advances in this segment are the all-stage FRONTIER DERIVATIVE UPPER BOUNDS, the global hereditary obstruction, and the no-dense-enclosure lemma. The user explicitly requested a general-n perspective rather than continuing isolated finite stages.
