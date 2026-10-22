# Separation-tree rank is subadditive under finite meets of bar opens
Date 2026-10-22.

Let T=L⊕L and d=∨{a⊠b:a∧b=0}. For an open w∈T define canonical rectangle bar B_w={(a,b):a⊠b≤w}. Suppose d∨w=1. Define rho(w) as minimum finite edge-depth of a well-founded separation tree for D∪B_w, or infinity when none finite exists.

THEOREM. If w,v are bar neighborhoods with finite ranks n,m, then w∧v is also a bar neighborhood, and
   max{rho(w),rho(v)} ≤ rho(w∧v) ≤ rho(w)+rho(v).
Also rho(w∨v)≤min{rho(w),rho(v)}.

Proof: d∨(w∧v)=(d∨w)∧(d∨v)=1. Since B_{w∧v}⊆B_w∩B_v, any tree for w∧v is a tree for either w or v, giving lower bounds. For upper bound take a tree Tw for w of height≤n. At each D leaf keep it unchanged. At each B_w leaf (a,b), graft a copy of a tree Tv for v, restricting all first labels by meet a and all second labels by meet b. This maps an exact horizontal or vertical cover to an exact cover in the corresponding restricted coordinates, by distributivity in L; restricts a D-leaf (u,t) to (a∧u,b∧t) still disjoint; restricts a B_v leaf to (a∧u,b∧t) whose rectangle lies under w (as ≤a⊠b) and v (as ≤u⊠t), hence w∧v. Terminal graft leaf is valid. The grafted tree is well founded (a well-founded outer tree with well-founded graft at each leaf) and has maximum edge-depth n+m. For B_w leaf of actual smaller rectangle below an advertised (u,v), the argument uses the actual rectangle containment; fine. This is valid for arbitrarily many children and nonspatial tensor frames. For union, each B_w leaf is also B_{w∨v} leaf.

Corollaries: For arbitrary finite bar family w_1,...,w_k, max rho(w_i)≤rho(meet_i w_i)≤sum rho(w_i). For w_sym=w∧tau(w), tau preserves the tree rank by swapping orientations, giving rho(w)≤rho(w_sym)≤2rho(w). Earlier symmetric rational-bar calculation improved generic bound 6 to exact 3.

This is a nontrivial quantitative operation on bars but NOT a rank amplifier: no strict lower bound over max follows. In particular finite intersections of rank-three graph obstructions have an a priori finite bound 3k, even without a more clever proof. Universal finite bound for arbitrary bars and existence of rank-four witness remain open.
