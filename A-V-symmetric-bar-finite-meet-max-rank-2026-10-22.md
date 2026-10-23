# EXACT max-rank law for finite intersections of symmetric rectangular bars
22 October 2026. NEW WORKING THEOREM, with fully elementary coordinatewise tree proof.

Let L be an arbitrary frame, Q=L⊕L and d=∨_{a∧b=0}a⊠b. For each open bar neighborhood w∈Q with d∨w=1, let B_w={(a,b):a⊠b≤w}, S_w=D∪B_w. Let ρ(w) be the least finite height of a separation tree rooted at (1,1), if finite. Let τ be flip on Q.

ORIENTED RANK. Define stage R_0^H(w)=R_0^V(w)=S_w. Inductively
  R_{n+1}^H(w)=H(R_n^V(w)), R_{n+1}^V(w)=V(R_n^H(w)).
By flattening adjacent same-orientation splits, any finite-height n tree with root H can be rearranged into alternating H,V,... shape without increasing height; the analogous V statement holds. With S_w symmetric if w symmetric, flip interchanges R_n^H and R_n^V. Hence for a symmetric bar whose rank≤n, BOTH alternating orientation certificates of height≤n exist at the root (pad shorter trees with unary splitting when needed).

PARALLEL-INTERSECTION LEMMA. For arbitrary opens w,v∈Q (barhood not needed) and all n, if (a,b)∈R_n^H(w) and (c,d)∈R_n^H(v) then
 (a∧c,b∧d)∈R_n^H(w∧v).
Ditto V.
Proof induct on n. Base n=0:
 if either original pair is D, their coordinatewise meet is D, since (a∧c)∧(b∧d)≤a∧b or c∧d=0. If both in B, then (a∧c)⊠(b∧d)=(a⊠b)∧(c⊠d)≤w∧v, hence in B_{w∧v}.
 For n+1 H, write (a,b)∈H(R_n^V(w)) with a=∨_i a_i and (a_i,b)∈R_n^V(w), and similarly c=∨_j c_j with (c_j,d)∈R_n^V(v). Frame distributivity gives a∧c=∨_{i,j}(a_i∧c_j); inductively (a_i∧c_j,b∧d)∈R_n^V(w∧v), so H covers yield claim. V identical.
If original trees have height less than n, use inclusions R_m^H⊆R_n^H etc via unary splits, and/or transposition for symmetric bars.

THEOREM (finite symmetric meet max law). Suppose w_1,...,w_m are symmetric BAR opens (τ w_i=w_i), each ρ(w_i)<∞. Their intersection w=∧_{i=1}^m w_i is automatically a bar:
 d∨∧_i w_i = ∧_i(d∨w_i)=1 (finite frame distributivity).
Then
  ρ(w)=max_i ρ(w_i).
Upper: set n=max_iρ(w_i). Choose for each w_i an oriented alternating H-first tree (symmetry assures availability), pad to height n, and repeatedly invoke parallel-intersection lemma to produce a height≤n H-first tree for (1,1) in S_w.
Lower: w≤w_i so B_w⊆B_{w_i}; any w-certificate is a w_i-certificate, thus ρ(w)≥ρ(w_i). Equality.

MORE GENERAL ALIGNED-ORIENTATION MEET THEOREM. Symmetry is not necessary if all input bars have H-FIRST alternating certificates (or all V-FIRST) of a common bounded height n. Their intersection has a certificate of height≤n by the same induction. It need not preserve individual EXACT minimum ranks under opposite orientations; determining whether an orientation-asymmetric bar exists is a separate open question.

SIGNIFICANCE. The previous general inequality max(ρ(w),ρ(v))≤ρ(w∧v)≤ρ(w)+ρ(v) is sharpened to equality for finite meets of symmetric bars. In particular finite intersections of any number of symmetric EXACT rank-three rational bridge or Cantor graph bars remain rank3, even if the component graphs strongly overlap. Thus **finite multigraph intersections cannot create rank4** from symmetric rank3 constituents. Possible rank amplification must use infinitely many barriers, differing orientation for nonsymmetric bars, or genuinely higher-rank primitive data.

NO CLAIM about INFINITE meets: a frame does not distribute d over infinite meets; ∧_i w_i may cease being a bar, even when every w_i is. Moreover parallel tree choices only distribute FINITE meets across arbitrary coordinate joins.

PROJECT LINKS: A-V-separation-tree-rank-meet-subadditivity-2026-10-22.md (older general bound); A-V-symmetric-rational-bar-exact-rank-three-2026-10-22.md (exact rank3); A-V-Cantor-multigraph-exact-rank-three-2026-10-22.md.

## NEW: finite meet of arbitrary finite-rank bars raises rank by at most ONE

Let w_1,...,w_m be ANY finite family of bar opens of finite rank and n=max_iρ(w_i). Then
  n ≤ ρ(∧_i w_i) ≤ n+1.
Proof: Every height≤n tree may be converted to alternating orientation at each depth, beginning either H or V, by collapsing successive same-coordinate joins and padding shorter branches by unary joins. For an H-first tree, pad to height n+1 with the alternating H,V,H,... signature. For a V-first tree, prepend a unary H split at the root and then pad to height n+1; it too has the signature H,V,H,... . Thus all bars have common-orientation certificate of height n+1. Repeatedly apply the parallel-intersection lemma, producing height≤n+1 certificate for ∧_i w_i. The lower bound follows from B_(∧w_i)⊆B_wi. Crucially, the +1 bound is INDEPENDENT of number m. If all max-rank component certificates can be chosen in a common orientation, n suffices and rank=max exactly.

## Exact symmetrization dichotomy and orientation rigidity

For any bar w of finite rank n, put s=w∧τw (automatically symmetric bar). The transposition τ carries an H-first certificate for w to a V-first certificate of the same height for τw, and vice versa, so ρ(τw)=ρ(w)=n. Consequently n≤ρ(s)≤n+1.

CLAIM: ρ(s)=n iff w admits BOTH an H-first and a V-first alternating certificate of height≤n. Thus ρ(s)=n+1 iff w is 'orientation-rigid' at its minimum finite height n (exactly one starting orientation available).

Proof (⇒): s symmetric, so any height-n root proof for s can be transposed to get a height-n proof with opposite root orientation, ALSO for s (because τs=s). Since S_s⊆S_w, both oriented proofs work for w. Proof (⇐): if w admits height-n certificates in BOTH orientations, τw admits both as well. Choose aligned H-first proofs for w,τw, and the parallel-intersection lemma yields an H-first certificate for s of height n. As already n≤ρ(s), equality follows. This is a precise IFF, not merely an implication.

RESEARCH REDUCTION: A nonsymmetric bar of rank exactly 3 with just ONE height-three root orientation would IMMEDIATELY produce a symmetric bar of exact rank FOUR by symmetrization. Conversely, the universal depth-three conjecture (*) implies that every finite-rank-3 bar necessarily has certificates of BOTH orientations: otherwise its symmetric meet would have rank4, contradict (*). This indicates a concrete finite-rank orientation asymmetry test as a route to an informative counterexample. We have NOT found such a rigid bar and have NOT proved (*) globally.

CAVEAT: For rank n=0 root itself is B_w leaf and w=1, both orientations can be regarded as vacuous or unary-padded; dichotomy holds with ρ(s)=0. For n≥2 the orientation claim has its intended nontrivial content. Canonical bars of rank exactly1 do not exist: a one-step root H or V cover by S=D∪B_w forces w=1 (D cannot contain (a,1) or (1,b) for nonzero a,b), so rank would be0.
