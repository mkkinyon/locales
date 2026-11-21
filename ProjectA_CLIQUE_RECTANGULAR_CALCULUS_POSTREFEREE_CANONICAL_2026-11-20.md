# Project A — compact-Hausdorff point-generated rectangular composition calculus
## Post-referee canonical consolidation · 20 November 2026

**Audit provenance and scope.** The [submitted repaired candidate](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_REPAIRED_CANDIDATE_2026-11-20.md) proved compact-*metric* clique power associativity via a two-colour Cantor-graph generation lemma. The independent blind referee [accepted the submitted claims](project-a/audits/2026-11-20/CLIQUE_POWER_ASSOCIATIVITY/INDEPENDENT_REFEREE_REPORT.md) and supplied **after reviewing them** a new closed-support proof valid for all compact Hausdorff spaces. The separate [referee addendum](project-a/audits/2026-11-20/CLIQUE_POWER_ASSOCIATIVITY/REFEREE_ADDENDUM.md) extends the result from cliques to **finite joins of arbitrary point-generated or full bipartite rectangles**, and establishes an associative algebra. The metric Cantor-graph lemma survives, but is **not needed** to prove the compact-Hausdorff calculus below. All results here are in classical locale theory; no literature originality/priority claim. The submitted and referee-origin versions are kept distinct in the [reconciliation](ProjectA_CLIQUE_POWER_ASSOCIATIVITY_REFEREE_RECONCILIATION_2026-11-20.md).

### 1. Definitions, products, and the indispensable distinction

For an ordinary subset A of a compact Hausdorff space G, let \(V_A=[A]_G\) be its **induced spatial sublocale** (not its closure). For A,B⊆G set
\[
 p(A,B)=[A\times B]_{G^2},
 \qquad q(A,B)=V_A\times_{\rm Loc}V_B.
 \tag{1}
\]
Here \(p(A,B)\) is the **point-generated** spatial bipartite relation; \(q(A,B)\) is the **full localic rectangle**. In general \(p(A,B)\le q(A,B)\), with strict inequality possible because a product of spatial sublocales can be nonspatial. If A or B is empty, both are 0.

Relational composition uses the genuine localic pullback followed by image, with the first factor traversed first. For full localic rectangles,
\[
(X_1\times Y_1)\circ(X_2\times Y_2)=
\begin{cases}X_1\times Y_2,&Y_1\wedge X_2\ne0,\\0,&Y_1\wedge X_2=0.\end{cases}
\tag{R}
\]
For nonzero middle W, projection from the composability locale is a pullback of W→1, an **open surjection in classical Loc**. This proves (R) without assuming that W has points. Composition distributes over **finite** joins of sublocales; no arbitrary-join exchange is asserted.

### 2. Compact closed-support richness

**Lemma 2.1 (referee's support lemma).** Suppose X,Z are compact Hausdorff spaces, U=[A]≤X and V=[D]≤Z, and 0≠W≤U×V. Let K be the **least ambient closed support** of W in X×Z. Then K is nonempty compact Hausdorff and
\[
K\cap(A\times Z),\qquad K\cap(X\times D)
\]
are both dense as ordinary subsets of K.

**Proof.** W is dense in K by definition of its closed support. Suppose a nonempty relatively open N⊂K contains no point with first coordinate in A. Choose nonempty N'⊂K with compact closure L⊂N, by regularity. The image T=pr_X(L) is compact closed in X and disjoint from A. The induced point-generated sublocale U satisfies U≤X\T, since every generating point lies in that open. Therefore W≤U×V does not meet N' (whose first coordinates lie in T), contradicting density in K. The second-coordinate proof is symmetric. No ordinary point of W is chosen.

The same argument applies to a **single** point-generated sublocale U=[A]≤G and a nonzero W≤U, using K=cl_G(W): A∩K is dense in K.

### 3. Closed-support generation without Cantor graphs

Let \(\mathscr K(A,D)\) consist of all **nonempty closed** K⊆X×Z with the two selected coordinate traces in Lemma 2.1 both ordinarily dense. Write \(\mathcal B(K)\) for the least dense sublocale (Booleanization) of K, embedded in X×Z.

**Theorem 3.1 (G', referee-origin).**
\[
\boxed{
[A]_X\times_{\rm Loc}[D]_Z
=\bigvee_{K\in\mathscr K(A,D)}\mathcal B(K).
}
\tag{G'}
\]

**Proof.** On each allowed K, the inverse images of [A] and [D] along the coordinate projections each contain their prescribed dense ordinary trace. Thus both inverse-image sublocales are dense in K, and their meet contains \(\mathcal B(K)\). Hence every term on the right lies in U×V.

Let J denote that join. If U×V≰J, **fitness of the regular compact Hausdorff ambient locale X×Z** supplies an ambient open sublocale O with J≤O but U×V≰O. Let F be the complementary closed sublocale. Because O,F are complementary in the sublocale lattice, W=F∧(U×V) is nonzero. Its least closed support K is contained in F and, by Lemma 2.1, belongs to \(\mathscr K(A,D)\). Hence 0≠\(\mathcal B(K)\)≤J∧F=0, contradiction.

Every singleton pair (a,d) is among the permitted K, so no separate join of ordinary point sublocales is required. **Compact metrizability is not used.** The submitted stronger geometric theorem generating products by *Cantor graphs* remains a valid, separately metric result according to the independent referee, but is not a dependency of (G').

### 4. Dense-middle bipartite saturation

**Theorem 4.1 (B*, referee-origin).** Let X,Y,Z be compact Hausdorff and A⊆X,D⊆Z nonempty; let B,C⊆Y be ordinarily dense. Form
\[
R=[A\times B]_{X\times Y},\qquad
S=[C\times D]_{Y\times Z}.
\]
Then
\[
\boxed{R\circ S=[A]_X\times_{\rm Loc}[D]_Z.}\tag{B*}
\]

**Proof.** Write T=R∘S. Source/target support gives T≤U×V with U=[A], V=[D]. Take any K∈\(\mathscr K(A,D)\). Inside the ordinary compact Hausdorff **spatial** product K×Y, pull R and S back along (k,y)↦(k_X,y,k_Z), and let M be the meet of these two inverse-image sublocales. The first contains the ordinary dense set \((K\cap(A\times Z))\times B\); the second contains \((K\cap(X\times D))\times C\). Therefore both are **dense sublocales** of K×Y, and their meet contains \(\mathcal B(K\times Y)\). In particular M is dense.

Projection K×Y→K is an **open surjection** (Y is nonempty overt). The image of M under this projection is dense in K; hence it contains \(\mathcal B(K)\). Its image in X×Z factors through the actual composability pullback R×_Y S, so \(\mathcal B(K)\le T\). Join over all K and apply (G') to deduce U×V≤T, completing the proof.

The two ordinary dense middle sets B and C need **not intersect**; their induced sublocales share a nonzero pointless overlap. No assumption that U×V is spatial is made.

### 5. Uniform formula for point-generated and full rectangles

**Theorem 5.1 (referee addendum).** Let A,B,C,D⊆G be ordinary subsets of one compact Hausdorff space. Independently choose
\[
r\in\{p(A,B),q(A,B)\},\qquad
s\in\{p(C,D),q(C,D)\}.
\]
Then
\[
\boxed{
r\circ s=
\begin{cases}
q(A,D),&V_B\wedge V_C\ne0,\\
0,&V_B\wedge V_C=0.
\end{cases}}
\tag{RC}
\]

**Proof.** If the middle intersection is zero the genuine composability locale vanishes; the nonzero case has endpoint upper bound q(A,D). If V_B∧V_C≠0, take its least compact closed support K in G. Lemma 2.1 in its single-factor form gives B∩K and C∩K **ordinarily dense in K**. Restrict p(A,B) and p(C,D) to the point-generated bipartite subrelations with middle B∩K and C∩K. Theorem 4.1 over middle K makes their composite the full q(A,D), so p(A,B)∘p(C,D)=q(A,D). Enlarging either p to q preserves this lower bound, while the endpoint upper bound gives equality. Empty-factor cases are 0.

Thus each multiplication of two nonzero rectangular generators is **the full outer rectangle**, regardless of whether its inputs were point-generated or already full.

### 6. Associative finite-join rectangular algebra

Define
\[
\mathscr R(G)=\{0\}\cup\{p(A,B),q(A,B):A,B\subseteq G\},\qquad
\mathscr R_\vee(G)=\{\text{finite joins of elements of }\mathscr R(G)\}.
\tag{2}
\]

**Theorem 6.1 (referee addendum).** The collection \(\mathscr R(G)\) is closed under composition, with associative multiplication; so is its finite-join closure \(\mathscr R_\vee(G)\). Converse preserves both and is an involution. The latter is a finite-join-distributive associative algebra with zero. Neither a multiplicative identity inside \(\mathscr R_\vee(G)\) nor arbitrary-join closure is asserted.

**Proof.** For r with support labels (A,B), s with (C,D), and t with (E,F), formula (RC) makes either bracketed triple zero iff at least one of V_B∧V_C or V_D∧V_E is zero; otherwise both are q(A,F). This proves associativity of generators. Composition preserves **finite** joins; expanding (R∨R')∘S and its converse distributes associativity to all finite joins. Converse interchanges p(A,B)↔p(B,A), q(A,B)↔q(B,A).

**Scope caution:** An arbitrary point-generated localic relation [T] for T⊆G² need not be a finite join of bipartite rectangles. Infinite decomposition into singleton rectangles cannot be substituted, because infinitary distribution of localic composition is not available in general.

### 7. Directed index-walk formula; clique specialization

Let t_i∈{p(A_i,B_i),q(A_i,B_i)} be a finite family and H=∨_{i=1}^m t_i. Define a **directed** overlap graph on the indices by
\[
i\to j\iff V_{B_i}\wedge V_{A_j}\ne0.
\]
Then for every k≥2 and every full binary bracketing W_k,
\[
\boxed{
W_k(H)=\bigvee_{i_1\to\cdots\to i_k}q(A_{i_1},B_{i_k}).
}
\tag{DW}
\]
The indexing is over directed walks of **exactly k−1 arrows**; this is a bracketing-independent consequence of (RC), finite distribution and associativity. There are no automatic loops, so **do not replace exact length by graph distance ≤k−1** in this general directed setting.

For **cliques**, A_i=B_i=E_i and t_i=p(E_i,E_i). The overlap graph is undirected with a loop at each index (each E_i is nonempty), so every shortest path can be padded by stationary steps. Consequently
\[
\boxed{W_k(H)=\bigvee_{\operatorname{dist}_\Lambda(i,j)\le k-1}U_i\times U_j\qquad(k\ge2).}\tag{PA}
\]
The original finite point-clique power formula is recovered, now for **all compact Hausdorff** ambient spaces, not only metrizable ones. The k=1 word is the original join of point-generated cliques, possibly smaller than the corresponding full products.

For finite directed index graphs, the possible walks of length k−1 are governed by powers of a finite Boolean adjacency matrix; the resulting powers W_k(H) are **eventually periodic**, though not necessarily constant. Example: on a two-point discrete G={a,b}, H=p({a},{b})∨p({b},{a}) alternates H,H²=Δ,H³=H,….

### 8. Five-vertex test and earlier exact-rank theory

For four Cantor blocks, the three bipartite relations
\[
R=p(I_0,Q_1),\quad S=p(I_1,Q_2),\quad T=p(I_2,Q_3)
\]
have intermediate overlaps Q_1∧I_1≠0, Q_2∧I_2≠0. The universal rectangular formula gives
\[
\boxed{(R\circ S)\circ T=I_0\times Q_3=R\circ(S\circ T).}
\]
The entire nonspatial outer product is attained. The earlier four-vertex positive calculation and the [independently reviewed unbounded exact Stone completion ranks](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) remain consistent and correct.

The metric Cantor-graph generator lemma (G) was accepted in the independent referee's review as a **valid stronger geometric refinement** for arbitrary point-generated endpoints of compact metrizable spaces. It should be preserved separately rather than deleted as redundant.

### 9. Further questions, not theorems

1. **Beyond finite rectangular joins:** identify conditions on a nonrectangular point-generated ordinary graph T⊆G² that place [T] in an associative subcalculus; unrestricted infinite joins are a genuine obstruction.
2. **Beyond compact Hausdorff:** seek abstract hypotheses replacing compact closed projections, e.g. proper/closed-coordinate image properties, or test locally compact Hausdorff examples.
3. **Presentations:** describe the finite-join algebra and its identifications using the directed incidence matrix, remembering that distinct index-pair rectangles can coincide locally.
4. **Graph refinements:** understand whether Cantor graphs can be replaced by other explicit compact perfect supports in nonmetrizable settings.

**Provenance:** Theorem 3.1 and the compact-Hausdorff extension are **new independent-referee contributions** in the main referee report. The uniform p/q calculus and directed walk formula are from the **separate addendum**. They were not in the originally submitted compact-metric candidate; this canonical note treats them as postsubmission referee-origin results, checked against the earlier proof dependencies, not silently as an accepted original submission.
