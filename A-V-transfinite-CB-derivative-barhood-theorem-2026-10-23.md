# Project A — Transfinite boundary-derivative theorem for graph-null bars

23 October 2026. **New working theorem with transfinite well-founded proof trees.** Correctly distinguishes pointwise leaf cover from the localic BAR equation; the former can be used to PROVE the latter via the constructed tree. Extends the finite derivative notes. This theorem does not by itself settle Question A.

## Assumptions

Let X be a topological space, L=O(X), and let S⊆L×L be a downset of permissible leaves containing all disjointness rectangles. Assume **pointwise leaf cover (P)**: for every ordinary pair (x,y)∈X×X there exist opens u∋x,v∋y with (u,v)∈S. We do NOT assume (1,1) belongs to the rectangular C-ideal closure of S.

For u∈L put
 K(u)=X\⋃{v:(u,v)∈S}.
It is a monotone closed-set-valued function. Under (P), for every x∈X and compact C⊆X, there is a neighborhood u of x (refinable inside any prescribed neighborhood) with K(u)∩C=∅: take finite second-coordinate subcover from pointwise S leaves and intersect the corresponding first neighborhoods.

Suppose opens a,b and a closed F⊆X satisfy K(u)⊆F for EVERY open u⊆a.

Define transfinite **nonlocal-compactness derivatives**:
 D^0(F)=F;
 D^(α+1)(F)=D(D^α(F)), where D(A) is the closed set of points of closed A that lack any compact neighborhood in the subspace A;
 D^λ(F)=⋂_{β<λ}D^β(F) for limit ordinals λ.
All derivatives are closed. If A⊆F closed then D^α(A)⊆A∩D^α(F) for all α, by transfinite induction and local compactness heredity to closed subspaces.

Define ordinal rank bounds d(α):
 d(0)=1;
 d(α+1)=d(α)+2 (ordinal addition on the RIGHT);
 d(λ)=sup_{β<λ}(d(β)+1), λ a nonzero limit.
Thus d(n)=2n+1 for finite n, d(ω)=ω, and d(ω+1)=ω+2.
Tree node rank always means sup_(child)(rank(child)+1); this is NOT in general equal to 1+sup(child ranks) for limit ordinals.

## Uniform relative transfinite theorem

For EVERY ordinal α, simultaneously:

(B_α) If D^α(F)∩b=∅ then the rectangle (a,b) has a V-FIRST well-founded S-proof tree of rank≤d(α).

(A_α) If D^α(F)∩b is contained in some compact C⊆X then (a,b) has an H-FIRST well-founded S-proof tree of rank≤d(α)+1.

**Proof:** B_0 follows because b∩K(a)=∅, so (a,b)∈V(S), rank≤1.

For ANY α, assuming B_α, prove A_α: cover a by opens u_x⊆a with K(u_x)∩C=∅ (compact avoidance). Put F_x=K(u_x). Closed heredity yields D^α(F_x)∩b=∅. Because every v⊆u_x has K(v)⊆F_x, apply B_α to (u_x,b) with controlling closed set F_x. One H-root cover yields rank≤d(α)+1.

For successor α+1 prove B_(α+1) from A_α. Set G=D^α(F). Since D(G)∩b=∅, each y∈b∩G has a compact neighborhood IN G. Choose an ambient open b_y⊆b such that G∩b_y lies in a compact subset C_y of G; for y∈b\G choose b_y disjoint from G. By A_α each (a,b_y) has an H-first tree of rank≤d(α)+1. The b_y cover b, so one V-root gives rank≤d(α)+2=d(α+1).

For limit λ prove B_λ from all B_β, β<λ: since D^λ(F)∩b=∅, for each y∈b choose β_y<λ with y∉D^β_y(F), then an open b_y⊆b disjoint from that closed derivative. Apply B_β_y to (a,b_y). A V-root with these children has rank≤sup_{β<λ}(d(β)+1)=d(λ). This is WELL FOUNDED even if the child ranks are unbounded finite or transfinite, because each branch enters a strictly smaller ordinal stage.

This proves the theorem. Every node uses horizontal/vertical joins in L; no spatiality assumption on L⊕L.

## Graph-null and scattered-boundary consequence

Assume X contains disjoint OPEN copies L0,R0 of Q, with closed boundary B=X\(L0∪R0). Let g(t)=(ell_t,r_t), q its greatest null open, and let S=D∪B_q. Assume:
(1) X is HAUSDORFF (or explicitly S satisfies pointwise leaf cover P);
(2) every x∈X has an open a_x containing x with (a_x)_L∩(a_x)_R=∅ AND with real closures of these rational traces having NO COMMON RATIONAL POINT;
(3) the boundary B has scattered Cantor–Bendixson height ≤α, i.e. B^(α)=∅ for some ordinal α.

The self-null neighborhoods in (2), together with Hausdorff separation, imply P: diagonal pairs lie in graph-null self-rectangles, and off-diagonal pairs lie in D rectangles.

For each u⊆a_x, K(u)=cl_X(u)∩cl_X(r[u_L]) is contained in B: no left sheet rational point lies in the closure of the right-sheet-only set r[u_L]; a right sheet rational point in K(u) would index a rational belonging to both real trace closures of a_x, forbidden by (2).

For a closed subspace A, D(A)⊆A' (isolated points have singleton compact neighborhoods). Transfinite induction shows D^α(B)⊆B^(α)=∅. Therefore B_α applies to (a_x,1), giving V-first trees of rank≤d(α). These a_x cover X, so one H-root gives the GLOBAL TREE BOUND
   **rk(q)≤d(α)+1.**
In particular, q is automatically a BAR in the localic product; this follows from the explicit tree and does NOT invoke barhood circularly.

For α=n finite the bound is 2n+2; for α=ω it is ω+1. More generally it supplies an ordinal upper bound for any scattered boundary with ordinal CB height. If q is already a bar, Hausdorffness may be dropped: use the bar equation to obtain P.

## Why the limit ordinal ω matters

If B is a TOPOLOGICAL DISJOINT SUM of components B_i, each of FINITE Cantor–Bendixson height h_i but with h_i unbounded, then B^(ω)=∅ although no uniform finite height bound exists. If X is Hausdorff and satisfies the separated-trace self-neighborhood hypothesis, the global graph-null candidate q has an explicit WELL-FOUNDED tree of rank≤ω+1. No new 'super-anchor' point of CB rank ω is necessary.

This removes a major obstacle in approaching Question A: barhood of an ω-stage graph-null construction can be established from a uniform topological boundary criterion, rather than by hand-building infinitely many rank-dependent upper trees. The remaining challenge is to force every parameter restriction q_J to have unbounded finite rank. See the separate dense-gadget assembly reduction.

**Scope:** We do NOT assert that arbitrarily high boundary CB rank forces high bar rank, or that the separate ω-rank K-fan bar is graph-null/fitted-stage strict.
