# Project A — targeted internal adversarial audit: balanced witness transport and scattered matrix group
## 21 November 2026 · INTERNAL audit, not independent

**Reviewed candidate:** [Balanced witness transport and scattered-index matrix algebras](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md). **Imported separately:** the independently reviewed compact-Hausdorff rectangle composition rule (RC), the independently reviewed locally closed graph actions, and the previously internally audited scattered-coordinate fibre lemma. **Published background:** Picado–Pultr, *Axiom T_D and the Simmons sublocale theorem* (2019), and the standard implications regular⇒fit, sublocale lattice is a coframe. Novelty is not asserted.

### 1. Verdict and status

**Provisional favorable internal verdict** after checking the potentially dangerous steps against the requirements of genuine localic pullback/image. The balanced-witness semigroup criterion is a *conditional* sufficient statement, so it does not by itself prove an arbitrary graph safe. The geometric scattered-index theorem **independently verifies** (G),(T),(O) for a large new class, including ordinary discontinuous permutations. Neither result is externally certified. **External audit strongly recommended**, focused on full sublocale-matrix reconstruction and middle-index pullback/image handling in (G)/(ACT).

### 2. Check: is the scattered-fibre reconstruction really independent of illicit infinite distributivity?

For any compact Hausdorff Z,K and family A_k≤Z, put W=∨_k(A_k×{k}). Fix k. Let J=∨_{j≠k}(A_j×{j}), which lies below Z×[K\{k}] **as a whole** because each summand does. This open support is disjoint from closed Z×{k}. Therefore \(J\wedge(Z\times\{k\})=0\), and
\(
W\wedge(Z\times\{k\})
=(A_k\times\{k\})\vee0
\)
uses **finite distributivity only**. This yields ΦΣ=id even for nonscattered K. This is a useful correction to any proof that attempts to pass the k-fiber through an arbitrary localic join without justification.

For injectivity when K scattered: if W is not the join of its point fibers, use regular⇒fit to separate by ambient open O, take closed complement and nonzero residue W', least closed support L, compact projection P⊂K, isolated point k∈P and a K-open neighborhood V with V∩P={k}. Density of W' in L ensures a nonzero part over k, contradiction. All uses are valid in compact Hausdorff Z×K; no ordinary point of W' is selected. If K not scattered, choose nonempty closed perfect F⊂K and the nonzero least dense sublocale B(F). Since no point lies in all dense open sublocales of F (remove that singleton), B(F) is pointless, so fibre generation fails already with Z=1. Thus MAT⇔scatteredness is credible and sharp.

**Residual risk:** the fit-open-separation for arbitrary J≤W and nonzero W' and the closed-support density lemma should be independently reviewed from definitions. The proof does not claim arbitrary locale/noncompact parametrization.

### 3. Check: is the discontinuous graph a legitimate sublocale, and are its indexed fibers correct?

For arbitrary ordinary function Θ:P×K→P×K, possibly discontinuous, its graph is an ordinary subset T⊆(P×K)² and the **induced spatial sublocale [T]** exists; we do not pretend Θ is a locale morphism. Since K² is compact scattered, (P×K)²≅P²×K² has a full sublocale matrix decomposition. The fibre at (i,j) is the ordinary subspace graph of h_i when j=σ(i), otherwise empty. This uses **closed** restriction by the singleton index pair and the standard induced-sublocale restriction identity, not ordinary point guessing.

### 4. Check: actual graph–graph composition is the claimed group multiplication

Use the full sublocale matrix decomposition over K³, which is scattered because finite products of scattered spaces are scattered. For each fixed triple (i,j,k), the composability sublocale is the pullback in P³ of two homeomorphism graphs if j=σ(i), k=τ(j), and 0 otherwise. Its image in P² is Γ_{g_j∘h_i}. The total composability sublocale is the **arbitrary join** of these indexed fibres. Image along π13 is a left adjoint on sublocales, hence preserves arbitrary joins. The resulting image is therefore the join of all indexed graph images. For each (i,k), **at most one** j survives, and Theorem MAT over K² determines the output exactly. Thus no unsanctioned arbitrary distributivity of *composition* over joins is invoked; only join preservation by **image**, which is valid. The result is point-generated Γ_{Θ2∘Θ1}. Converse is the inverse of the underlying set bijection and belongs to the same class.

Potential external check: image being a left adjoint on sublocales, and the identification of the closed triple sectors under the localic projection, should be made explicit.

### 5. Check: full q rectangular action

For ordinary A,B⊆P×K, let A_i,B_j⊆P be index slices. In G², the k-pair sector of p(A,B) is p_P(A_i,B_j), while for q(A,B) it is **q_P(A_i,B_j)**, generally nonspatial. These are calculated by actual closed-sector pullbacks. In G³, composition with H_{σ,h} has only the j→σ(j) graph sector for each j. Within P³, composing q_P(A_i,B_j) with Γ_{h_j} yields q_P(A_i,h_j(B_j)) by a *genuine homeomorphism* on P's second coordinate. The same localic image/join reconstruction as step 4 gives exactly q_G(A,Θ(B)); no replacement by a spatial p rectangle. The first-coordinate action is dual.

### 6. Check: overlap balancedness with pointless P components

Inside Sub(G)≅∏_j Sub(P), the meet [Θ(B)]∧[C] is nonzero iff one of the indexed meets
\(
[h_j(B_j)]\wedge[C_{\sigma(j)}]
\)
is nonzero. Because h_j is an actual homeomorphism of P, this is equivalent to
\(
[B_j]\wedge[h_j^{-1}(C_{\sigma(j)})]\ne0
\),
the corresponding component of [B]∧[Θ^{-1}(C)]. This proof does **not** assume that [B_j]∧[C_k] has ordinary points; it respects ghost intersections in perfect P. This establishes the exact RHR test.

### 7. Check: balanced semigroup theorem is not circular

Theorem 1.1 requires (G), (T), (O) to be *established independently* of associativity. The proof then checks **eight** individual generator triples. (G) is a condition about graph-only products; (T) about graph-rectangle binary products; (O) about sublocale overlaps. Their verification uses matrix decomposition and homeomorphism composition for the specific geometric class, not a blanket reassociation of arbitrary relations.

In RRR when both internal overlaps are nonzero, the formal output q(A,D) can be zero for empty outer supports. In RHR the overlap equivalence gives **the same output**, not an iff statement about nonzero outer endpoints. For one rectangle, word type p/q is preserved; after two rectangles it becomes full q, unless zero. Only **finite** join expansion is used in transferring associativity to finite sums. The rectangular family remains a two-sided ideal.

### 8. A concrete strictness example

K={0}∪{1/n:n≥1} with one nonisolated 0. P=Cantor. Let σ swap 0 and 1 (the isolated point 1), fix every other index; h_k=id_P. The underlying set bijection Θ(p,k)=(p,σ(k)) is **discontinuous**: choose an ordinary sequence (p,1/n)→(p,0); its images converge to (p,0), but Θ(p,0)=(p,1). Yet its point-generated graph H under genuine localic composition satisfies H²=Δ_G because σ²=id and graph matrix multiplication holds. It is a legitimate non-map localic relation and acts by complete sublocale lattice permutation on all rectangles. This shows the new class is strictly broader than graphs of continuous locale maps, without claiming H is an isomorphism in Loc.

### 9. Strategic conclusion and audit priority

The mathematical abstraction that survives the internal challenges is **finite witness semigroups acting by exact p/q rectangular support transport and balanced middle overlap**. The new source of such semigroups is *atomic scattered indexing*, permitting arbitrary permutations of scattered index points and arbitrary homeomorphisms of nonspatial perfect fibers, not just the earlier 15-arrow corridor.

Proposed independent audit order: (i) MAT⇔scatteredness proof, specifically arbitrary sublocale W of Z×K; (ii) graph matrix sectors of discontinuous Θ, graph–graph image/projection; (iii) q rectangle transport; (iv) balanced RHR; (v) normal forms/ideal corollaries.

If independently accepted, the larger Project A program can use this as a clean *positive* endpoint for the graph-witness boundary investigation before undertaking the planned big-picture review and revisiting intrinsic specialization/Dowker complexes.
