# Exact depth three for the crowded Cantor multigraph bar
22 October 2026. Proof for the previously constructed DENSE-bridge Cantor-shift X.

Let K be the middle-thirds Cantor set, C=K∩Q, and choose bridge limits alpha_n,beta_n with pairs dense in R² and
alpha_n∉Q−K, beta_m∉Q+K, beta_m−alpha_n∉K for ALL n,m.
Let η=∐_{c∈C}(t↦(ell_t,r_{t+c})), q_C largest η*-null open in T=O(X)⊕O(X). Let B_C={(u,v):u⊠v≤q_C}; it is a bar because the audited frame boundary lemma gives q_C∨d_I=1.

THEOREM: Minimum separation tree edge depth for B_C is **exactly 3**.

LOWER BOUND. Use the exact depth-two criterion. If first-open a meets L, choose rational interval I with ell[I]⊆a and choose any fixed c∈C (e.g. c=0). Dense pairs (alpha_n,beta_n) give n with alpha_n∈I and beta_n∈I+c. Left A_n tail in I, so z_n∈cl(a) and z_n∉a*. If (u,v)∈B_C with a≤u, graph-nullness for shift c means v has no r[I+c]. Right B_n tail lies in I+c; hence z_n∉v. Therefore a*∨F_BC(a)≠1. All first opens that are H→V-good avoid L, so no H→V proof of depth ≤2. Symmetrically any second-open b meeting R contains r[J] for some interval J; choose n with beta_n∈J and alpha_n∈J−c. Then z_n∈cl(b) but every first coordinate u of a rectangle (u,v)∈B_C with b≤v omits ell[J−c]; hence z_n∉b*∨G_BC(b), ruling out V→H. Rank≥3.

UPPER BOUND. Let h(b)=∨{u:(u,b)≤(a',b') for some disjointness rectangle or B_C rectangle}. For each n and each y∈X construct an open b_y∋y such that the OPEN h(b_y) contains L∪R∪{z_n}:
(a) If y∈L, choose b_y⊆L; since η has second coordinate only R, (1,b_y) is graph-null, h(b_y)=1.
(b) If y=r_s∈R, by alpha_n∉Q−K we have s∉alpha_n+K; choose small interval J around s with closure(J) disjoint alpha_n+K; b_y=r[J]. Every first point L has disjointness first neighborhood (since b_y⊆R), every first point R has graph-null first neighborhood (η first coordinate in L), and z_n has an open neighborhood whose L trace lies near alpha_n with (left trace+K)∩J=∅, giving graph-null rectangle.
(c) If y=z_m, exploit beta_m−alpha_m∉K and beta_m−alpha_n∉K. Choose real open intervals I_small⊂I_big about alpha_m and J about beta_m with closure(I_small)⊂I_big, (I_big+K)∩J=∅, and (alpha_n+K)∩closure(J)=∅, and shrink J so a small neighborhood U_n of alpha_n also satisfies (U_n+K)∩J=∅. Choose b_y a bridge neighborhood of z_m whose L trace lies in I_small and R trace in J (possible by tail convergence). For first ell_s with s∈I_big, choose open first neighborhood ell[U]⊆L within I_big; its graph-pullback against b_y vanishes since U+C misses J. For s outside closure(I_small), choose an open first interval avoiding I_small; first neighborhood disjoint from b_y (and hence D-leaf). These cases cover every ell_s since closure(I_small)⊂I_big. First points in R have q-null neighborhoods. At z_n choose a bridge neighborhood with L trace in U_n; then its rectangle with b_y is η-null. Therefore h(b_y) contains all L,R,z_n.
Since b_y for y∈X cover X, they join to 1 (spatiality of X). Thus (L,1) and (N_n,1), for any neighborhood N_n with N_n∩Z={z_n}, have V→H trees of edge height ≤2: split vertically to (L,b_y) or (N_n,b_y); use the definition of h(b_y) to cover each first coordinate horizontally by leaf rectangles (take meets with the desired L or N_n). (R,1) is itself a graph-null leaf. Finally H-root cover of 1 by L∨R∨∨_nN_n gives an H→V→H tree of height ≤3.

FRAME CAUTION: all B_C leaves are verified by η*(u⊠v)=0 for every shift c; D leaves by u∧v=0. Point arguments used only to produce genuine open covers in spatial frame O(X), never to infer covers in nonspatial O(X)⊕O(X).

CONCLUSION. Even though the crowded multigraph beats all single-valued graph-far neighborhood primitives, its rectangular-bar rank is STILL 3. Thus allowing infinite multivalued branching does not by itself amplify tree rank. This does NOT establish any universal depth-three theorem.
