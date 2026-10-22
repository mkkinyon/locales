# Dense-bridge Cantor multigraph refutes symmetric bi-graph formula (working proof)
22 October 2026. New result; **requires independent adversarial audit**. This modifies the prior crowded Cantor-shift rational-bridge construction by making the bridge limit pairs dense in R².

## Construction
Fix standard Cantor K⊂R and C=K∩Q (countable, crowded, closed relative Q). Enumerate basic rational open rectangles I_n×J_n of R². Recursively choose irrational α_n∈I_n and β_n∈J_n such that:
(i) all α_n are different, and all β_n are different;
(ii) α_n∉Q−K and β_n∉Q+K;
(iii) β_m−α_n∉K for ALL n,m.
At stage n, choose α_n avoiding Q−K, {α_i:i<n}, and ⋃_{i<n}(β_i−K); then β_n avoiding Q+K, {β_i:i<n}, ⋃_{i≤n}(α_i+K). Countable unions of closed nowhere dense sets allow choices by Baire. In particular all α_n,β_n irrational and { (α_n,β_n) } dense R². Choose pairwise disjoint rational sequences A_n→α_n,B_n→β_n; each has only an irrational real accumulation point, so closed discrete in Q. Let X be two open Q copies L_0={ℓ_t},R_0={r_t}, with added z_n approached along A_n on L_0 and B_n on R_0 (basic z_n neighborhoods include open sets containing cofinitely many points of each sequence). X countable Hausdorff; Z={z_n} closed discrete.

Let Y=⊔_{c∈C}Q and η:Y→X×_loc X, η|_{c}(t)=(ℓ_t,r_{t+c}). Let T=O(X)⊕O(X), q_C=largest element killed by η*, equivalently q_C=∧_{c∈C}q_c where each q_c is the corresponding graph-null open.

## Closed off-diagonal ordinary relation and localic disjointness
F_C={(ℓ_t,r_s):t,s∈Q,s−t∈C} is closed in X×_top X: in L_0×R_0, C closed in Q and difference continuous; boundary (z_n,r_s) excluded since s−α_n∉K; (ℓ_t,z_m) excluded since β_m−t∉K; (z_n,z_m) excluded since β_m−α_n∉K. Compactness of K lets choose uniform rectangular neighborhoods avoiding F_C. Other quadrants trivially excluded. In particular F_C∩Δ=∅.

Set e=L_0∨R_0. Three quadrants of e⊠e are killed by η* and hence ≤q_C, while L_0⊠R_0≤d_I since L_0∩R_0=0. Thus e⊠e≤q_C∨d_I. For each point with a coordinate in closed discrete Z, F_C closed supplies an open rectangle missing F_C, hence below q_C. By Claude's elementary localic boundary lemma, q_C∨d_I=1. The closed sublocale S_C=C(q_C) is nonzero (η*(1)=1 and η*(q_C)=0), disjoint from I.

## Hereditary projection inseparability
Every nonempty relatively open G⊆F_C has cl_X π1(G)∩cl_X π2(G)≠∅. Choose (ℓ_t,r_{t+c})∈G; take rational intervals I,J with F_C∩(ℓ[I]×r[J])⊆G and t∈I,t+c∈J. Shrink I so I+c⊆J. Choose n with α_n∈I and β_n∈I+c (density of bridge limit pairs in R²). For sufficiently large m, a_{n,m}∈I and a_{n,m}+c∈J, showing ℓ[a_{n,m}]⊆π1G and z_n∈cl π1G. Similarly b_{n,m}∈I+c and b_{n,m}−c∈I, so r[b_{n,m}]⊆π2G and z_n∈cl π2G.

## All dual-far strips fix q_C, LOCALLY
Let s=(k⊠1)∨(1⊠h) satisfy d_I∨s=1. Suppose t∧s≤q_C but t≰q_C. Rectangle generation gives a⊠b≤t with η*(a⊠b)≠0; so F_C∩(a×b) is nonempty relatively open. Since t∧s≤q_C, **all points of this relative open subset lie outside the ordinary strip s**, so π1G⊆X\k, π2G⊆X\h. Their closures have common bridge z_n by the preceding lemma, hence z_n∉k,h. The diagonal point (z_n,z_n) evaluates both s and d_I to zero (every disjoint-side generator of d_I vanishes there), contradicting d_I∨s=1. Therefore t≤q_C; s→q_C=q_C for every dual-far strip.

## All individual partial-graph primitives fix q_C
Let φ:U→X have open U⊆X, and γ=(incl,φ), or transpose. Any relatively open nonempty G⊆F_C contains some nonempty rectangle slice. Its projection to the graph-domain coordinate has a nonempty open rational interval I' such that for EVERY t∈I' its corresponding fiber within G has at least two distinct points (because C is crowded and the shift condition is open around a selected c∈C). If I'∩U=∅, the closure of γ(U) misses I'×X, so cannot contain G. Otherwise choose t∈I'∩U; the graph closure over a point of U has at most one value since X Hausdorff, while G has ≥2. Thus no relatively open G⊆F_C lies in the ordinary closure of a single partial graph (either orientation).

Now if t∧q_φ≤q_C but t≰q_C, take rectangle a⊠b≤t meeting some translation branch c. The relative open G=F_C∩(a×b) is not contained in closure of graph φ. Choose p∈G outside closure, then a smaller open rectangle a'×b'⊆a×b around p misses the ordinary graph; hence a'⊠b'≤q_φ. As p belongs to some translation branch c', a'⊠b'≰q_C, contradiction. Thus q_φ→q_C=q_C, and similarly for transposed graph.

## Consequence
Every generator of the symmetric bi-graph nucleus fixes q_C. Their nucleus join therefore fixes q_C; but q_C∨d_I=1 and q_C≠1, so j_V(q_C)=1. Thus
   V ⊊ W_bgr
for THIS strengthened countable Hausdorff spatial locale. The collectively graph-far étale primitive O(q_C) witnesses the failure; therefore the étale scheme STRICTLY enlarges the bi-graph scheme.

**Audit priority:** Carefully check the 'graph closure over open domain stays single-valued' argument in any nonregular Hausdorff X, the boundary closedness of F_C, and the recursive pair-density-with-K-avoidance. Do not promote as independently audited yet.
