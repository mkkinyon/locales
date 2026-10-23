# UNBOUNDED FINITE SEPARATION-TREE RANK AND AN EXACT OMEGA-RANK TWO-RECTANGLE BAR
Date: 22 October 2026
Status: complete inductive proof, using only countable first-countable Hausdorff topological spaces and canonical localic bars. Supersedes open 'can rank4 be iterated?' query.

## 1. Core definitions
Let X be a T1 space with disjoint closed subsets F,C. Put e=X\F and a=X\C; since F∩C=∅, a∨e=1. In Q=O(X)⊕O(X), set
    w_X=(a⊠1)∨(e⊠e)=(a⊠1)∨(1⊠e).
The equality is because a∨e=1. Put
    s_X=w_X∧τ(w_X)=(a⊠a)∨(e⊠e).
Canonical leaves: S_X=D_X∪B_{w_X}, D_X={(u,v):u∧v=0}, B_{w_X}={(u,v):u⊠v≤w_X}. The leaf condition admits the exact form:
    (u,v)∈B_{w_X} ⇔ u≤a OR v≤e.
The reverse implication follows from either strip, and the forward implication follows by evaluation at ordinary points (x,y) with x∈C∩u and y∈F∩v, which would be excluded by w_X. In particular (a,1),(1,e) are ALWAYS B_w leaves.

Define alternating finite stages:
    R_0^H(S)=R_0^V(S)=S,
    R_{r+1}^H(S)=H(R_r^V(S)),   R_{r+1}^V(S)=V(R_r^H(S)).
Adjacent same-coordinate splits flatten, and trivial unary splits permit padding, so R_r^H and R_r^V describe the prescribed first-orientation trees of edge depth≤r.

## 2. Clopen component restriction and extension
If Y⊆X is CLOPEN and F_Y=F∩Y, C_Y=C∩Y, then the restriction of w_X to Y×locY is w_Y. Thus restricting BOTH coordinates of any global proof tree to Y preserves every leaf (D or B_w), cover, orientation and edge depth. Formally (u,v)∈R_r^θ(X) ⇒ (u∩Y,v∩Y)∈R_r^θ(Y) for θ∈{H,V}, all r.

If (1_Y,1_Y) admits an H-first certificate of height r≥1 for w_Y, then (1_X,Y) admits an H-first certificate of the SAME height: merge a disjointness leaf (X\Y,Y) at the horizontal root with the first-coordinate root cover of the old Y proof. Analogously, a V-first certificate for w_Y extends to (Y,1_X) with the SAME height, by adding (Y,X\Y) D at the vertical root. This is the crucial no-extra-level clopen extension lemma. All Y_i below are clopen.

## 3. Inductive construction of X_m, F_m,C_m
BASE m=1. Let X_1=Q_K, the rationals with K-topology K={1/j:j≥1}, p=0, F_1={p}, C_1=K. Both are closed disjoint subsets. X_1 is countable first-countable Hausdorff. Every neighborhood b of p has cl(b)∩K≠∅. Thus e_1=X_1\{p} is NOT V→H certifiable over second a_1=X_1\K:
    (e_1,a_1)∉R_2^V(X_1).
Indeed any second b∋p has H(S)-fiber h(b)=a_1∨b*, which does not contain e_1 due K∩cl b. Yet (1,1)∈R_2^H(X_1): first split a_1 and suitably small u_x around each x∈K with p∉cl u_x; below a_1 use (a_1,1) B leaf, and below u_x vertical split by e_1 and u_x*, with (u_x,e_1) B and (u_x,u_x*) D. This yields rank(w_1)=2, H-rigid.

INDUCTIVE STEP. Assume X_m is a countable first-countable Hausdorff space with disjoint closed F_m,C_m. Make countably many clopen copies Y_i≅X_m, i≥1, and add new point t.

If m+1 EVEN (new point has color C):
  F_{m+1}=⋃_i F_m^{(i)},   C_{m+1}={t}∪⋃_i C_m^{(i)}.
  Basic neighborhoods of t: U_N={t}∪⋃_{i≥N}e_m^{(i)}.
If m+1 ODD (new point has color F):
  F_{m+1}={t}∪⋃_i F_m^{(i)},   C_{m+1}=⋃_i C_m^{(i)}.
  Basic neighborhoods of t: U_N={t}∪⋃_{i≥N}a_m^{(i)}.
All old copy opens remain open. Each U_N∩Y_i is open and U_N∩U_M=U_max(N,M), so this is a topology with (U_N) a countable local base at t. Each Y_i is clopen (complement has U_{i+1} neighborhood at t). Hausdorffness: separate t from any point in Y_i via U_{i+1} and Y_i; copies are Hausdorff. Thus X_{m+1} countable, first-countable, Hausdorff. Both F_{m+1},C_{m+1} are closed disjoint: at new C point t, the neighborhood base avoids all F (e_m), while a_new is open as union of old a_m; dual at new F point.

Let θ_m=V if m odd, θ_m=H if m even, and opposite orientation σ_m=H if m odd, σ_m=V if m even.

INDUCTIVE CLAIM, simultaneously for all m≥1:
  (A_m) (1,1)∈R_{m+1}^{σ_m}(X_m): a successful alternating rooted tree of depth m+1.
  (B_m) (e_m,a_m)∉R_{m+1}^{θ_m}(X_m): critical rectangle obstruction in opposite orientation.

Proof of (A_{m+1}). If new point t has color C (m+1 even), then t∈e_new, so second-coordinate opens e_new and clopen copies Y_i cover 1. The pair (1,e_new) is a B_w LEAF. Since m odd, old X_m has H-first tree of depth m+1, which by clopen extension yields (1,Y_i)∈R_{m+1}^H(X_new). One final vertical root split gives (1,1)∈R_{m+2}^V(X_new), as desired. If new t has color F (m+1 odd), then t∈a_new, and first opens a_new and Y_i cover 1. The pair (a_new,1) is a B_w leaf. Since m even, old X_m has V-first tree of depth m+1, which by clopen extension gives (Y_i,1)∈R_{m+1}^V(X_new). One final horizontal root gives (1,1)∈R_{m+2}^H(X_new).

Proof of (B_{m+1}). If new t has color C (m+1 even), t∈e_new. Suppose (e_new,a_new)∈R_{m+2}^H(X_new)=H(R_{m+1}^V). Its H-root first-coordinate cover of e_new includes at least one open u containing t; choose N with U_N⊆u, then for any i≥N, e_m^{(i)}⊆u∩Y_i, while a_new∩Y_i=a_m^{(i)}. Restrict the child rectangle (u,a_new)∈R_{m+1}^V to Y_i; by downward closure obtain (e_m,a_m)∈R_{m+1}^V(X_m), contradicting (B_m) because m odd. Therefore (B_new) holds.
If new t has color F (m+1 odd), t∈a_new. Suppose (e_new,a_new)∈R_{m+2}^V=V(R_{m+1}^H). Its V-root second-coordinate cover of a_new includes some b containing t; U_N⊆b. For any i≥N, a_m^{(i)}⊆b∩Y_i, while e_new∩Y_i=e_m^{(i)}. Restrict (e_new,b)∈R_{m+1}^H and use downward closure to obtain (e_m,a_m)∈R_{m+1}^H(X_m), contradiction because m even. Thus (B_new).

Now (B_m) implies (1,1)∉R_{m+1}^{θ_m} by downward closure. If there were ANY root tree of height≤m, then converting it to alternating normal form and prepending (if necessary) a trivial unary θ_m-root, or padding, would give (1,1)∈R_{m+1}^{θ_m}, contradiction. With (A_m), it follows:
    ρ(w_m)=m+1 EXACTLY,
and w_m is orientation-rigid: its unique starting direction at minimum height is σ_m, alternating H,V,H,V,... with m.

Because w_m is a genuine bar by (A_m), the symmetric s_m=w_m∧τw_m=(a_m⊠a_m)∨(e_m⊠e_m) is also a bar. The previously proved sharp symmetrization theorem then gives:
    ρ(s_m)=m+2 EXACTLY.
Thus for every integer n≥3, choosing m=n−2 yields a countable first-countable Hausdorff X_m and a symmetric TWO-RECTANGLE canonical bar of exact rank n.

## 4. A SINGLE space and TWO-RECTANGLE bar of exact ordinal rank OMEGA

Take the countable topological sum
   X_∞=⊔_{m≥1}X_m,
with each X_m clopen, Hausdorff and first-countable. Let F=⊔_m F_m and C=⊔_m C_m; these are closed disjoint subsets. Put e=X_∞\F and a=X_∞\C, and define
   s_∞=(a⊠a)∨(e⊠e).
This is ONE symmetric bar candidate generated by just TWO tensor rectangles, and its restriction to the clopen diagonal square X_m×locX_m is exactly s_m.

BARHOOD and an OMEGA-height tree: For first-root H split 1=∨_m X_m. Below each first open X_m, split second coordinate vertically by X_m and its clopen complement X_∞\X_m. The off-diagonal (X_m,X_∞\X_m) is D. The diagonal (X_m,X_m) has a finite separation tree of exact depth m+2 from s_m; lift its leaves to X_∞ (the diagonal square inclusion is an open sublocale). Each branch has finite length ≤m+4 (including the H root and V split), so the overall tree is WELL-FOUNDED with ordinal rank/height at most ω (standard well-founded node rank sup_{children}(rank(child)+1)). Hence d_I∨s_∞=1 in the full localic product. Any finite-height global tree would restrict, for every m, to a tree for s_m of the same bounded height, which is impossible because ρ(s_m)=m+2 is unbounded. Thus its MINIMUM WELL-FOUNDED TREE ORDINAL RANK is EXACTLY ω. Note: this is not a claim of a finite-depth certificate; indeed no finite bound exists.

This exact ω result strengthens 'arbitrarily high finite ranks': a SINGLE symmetric TWO-RECTANGLE bar on a SINGLE countable, first-countable, Hausdorff space has no finite-depth separation tree.

## 5. Research implications
- No finite universal separation-tree rank bound exists, even for symmetric 2-rectangle canonical bars on countable first-countable Hausdorff spatial locales.
- Orientation rigidity occurs at every finite rank n≥2 for two-rectangle asymmetric strip bars w=(a⊠1)∨(1⊠e), and the unique optimal root orientation alternates.
- The n-stage construction depends on F,C closed disjoint and the special strip form; general topology or graph-null complexity is unnecessary.
- A countable disjoint union produces a symmetric two-rectangle bar of ordinal rank ω.
- Open: whether a SINGLE connected/irreducible space can realize unbounded ranks; whether all countable ordinals or arbitrarily large ordinals arise from iterated fan constructions; whether more general point-free ordinal-rank upper bounds follow from spatial cardinality.
- Distinguish original finite-depth recurrence R_r^θ from transfinite well-founded tree rank: we have a genuine well-founded tree of rank ω, not necessarily a transfinite alternation normal-form identity.
