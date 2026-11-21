# Project A — exact localic matrix multiplication over scattered indices
## 21 November 2026 · NEW INTERNAL theorem and locally finite associative lift

**Purpose.** This is a substantive abstraction of the previous [scattered-coordinate pseudo-bijection](ProjectA_PERFECT_TARGET_SCATTERED_CORRIDOR_SAFE_INFINITE_CHART_RANK_2026-11-21.md), [tensorization](ProjectA_PERFECT_SOURCE_TARGET_TENSORED_SCATTERED_PSEUDO_ISOMORPHISM_2026-11-21.md), and [balanced-witness / scattered-index permutation algebra](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md). It replaces monomial (one-entry-per-index) graph matrices by **general locally finite matrices of genuinely localic relations**, and proves their associativity by finite-index algebra rather than by assuming arbitrary infinitary distributivity. The results are **INTERNAL and not yet externally audited**; no literature priority claim.

### 1. Sublocale matrix coordinates

Let P be **any compact Hausdorff space**, and K a compact **scattered Hausdorff** space. Let G=P×K, and write \(\mathsf{S}(X)\) for the complete coframe of sublocales of a locale X.

By the separately internally proved [atomic-index theorem](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md),
\[
\boxed{
\mathsf{S}(P^n\times K^n)
\cong\prod_{(k_1,\ldots,k_n)\in K^n}\mathsf{S}(P^n)
}\qquad(n=1,2,3).
\tag{MATn}
\]
Finite products of scattered spaces are scattered (isolate a coordinate in the projection, then isolate a coordinate in the fiber).

Hence **every** localic relation R≤G² has an exact matrix \((R_{ij})_{i,j\in K}\), with each entry an arbitrary **possibly nonspatial sublocale** of P²:
\[
R_{ij}=R\wedge(P^2\times\{(i,j)\}),\qquad
R=\bigvee_{i,j\in K}R_{ij}.
\]
No assumption that R is a point-generated graph, closed, rectangular, or in any associative subalgebra is made.

### 2. Exact matrix-product formula

**Theorem 2.1 (INTERNAL).** For **any** localic relations R,S≤G², the genuine image/pullback composition is given by
\[
\boxed{
(R\circ S)_{ik}=\bigvee_{j\in K}
\left(R_{ij}\circ_P S_{jk}\right).
}
\tag{MUL}
\]
On the right the operation \(\circ_P\) is the genuine localic relation composition on P, and the join is the actual join of sublocales of P². This identity holds even if relation composition on P is nonassociative.

**Proof.** Let \(Q=R_{12}\wedge S_{23}\hookrightarrow G^3\) be the genuine composability locale. Matrix decomposition over K³ gives
\[
Q=\bigvee_{i,j,k\in K}Q_{ijk}
\]
and each closed-index triple component \(Q_{ijk}\hookrightarrow P^3\) is precisely the localic composability sublocale of \(R_{ij}\) and \(S_{jk}\). The map π13:G³→G² is a locale map, and its image operation on sublocales is a left adjoint to sublocale pullback, hence **preserves arbitrary joins**:
\[
\operatorname{im}(\pi_{13}|Q)
=\bigvee_{i,j,k}\operatorname{im}(\pi_{13}|Q_{ijk}).
\]
Each term is supported in its closed index-pair (i,k) sector and, inside that sector, is \(R_{ij}\circ_P S_{jk}\). Reconstructing via the matrix order isomorphism over K² gives (MUL). There is **no** claim that relational composition itself distributes over arbitrary joins: only the localic **image** preserves them, after the composability source has already been decomposed by MATn. □

**Warning:** For unrestricted matrices, the infinite join in (MUL) can break associativity even when the *binary* formula is valid. The formula by itself does **not** make all localic relations on G associative when P is perfect.

### 3. Locally finite matrices inherit finite-join associative relation algebras

Let \(\mathcal A(P)\subseteq\mathsf S(P^2)\) be any class of relations satisfying:
- 0 and Δ_P are included;
- closure under genuine localic binary composition, **finite** joins and converse;
- composition is **associative within** \(\mathcal A(P)\) and distributes over finite joins.

The compact-Hausdorff rectangular+locally-closed graph algebra is one such \(\mathcal A(P)\), **conditional on independently refereed RC**. Another, independently established example is the algebra of **closed relations** on any compact locale P, whose composites are closed and associate by proper image stability.

Define \(\operatorname{Mat}_{\rm rcf}(K,\mathcal A(P))\) to consist of all sublocales R≤G² such that:
\[
R_{ij}\in\mathcal A(P)\ \text{for all }i,j,\qquad
\#\{j:R_{ij}\ne0\}<\infty\ \forall i,\qquad
\#\{i:R_{ij}\ne0\}<\infty\ \forall j.
\tag{LCF}
\]
Thus every matrix row and column has **finite support**, though the entire index set K and the matrix itself may be infinite.

**Theorem 3.1 (locally finite matrix lift; INTERNAL).** The class \(\operatorname{Mat}_{\rm rcf}(K,\mathcal A(P))\) is an **associative unital**, converse-closed, finite-join-distributive subalgebra of the genuine localic relations on G. Its multiplication is the familiar **finite** matrix formula
\[
\boxed{
(R\circ S)_{ik}=\bigvee_{j\text{ in finite support of row }i}R_{ij}\circ_P S_{jk}.
}\tag{FINMAT}
\]

**Proof.** In (MUL) only finitely many j contribute for any fixed (i,k), and each entry of the composite belongs to A(P) by finite-join and composition closure. For any source index i, only finitely many j are in the i-row of R, and each of those j has finitely many nonzero targets under S, so the composite has finite i-row support. The dual column argument uses the finite k-column support of S and the finite column supports of R. Hence the product stays row-and-column finite. Converse transposes the index matrix and converses each entry, preserving the class and finiteness. Finite joins also preserve all conditions; the full diagonal Δ_G corresponds to diagonal entries Δ_P and zero off-diagonal, so is a unit.

For three matrices R,S,T, fixing row i leaves finitely many j in R and finitely many k for each such j in S. Hence both bracketings expand into the **same finite** join
\[
\bigvee_{j,k}(R_{ij}\circ_P S_{jk})\circ_P T_{k\ell}
=
\bigvee_{j,k}R_{ij}\circ_P(S_{jk}\circ_P T_{k\ell}),
\]
by associativity and finite distributivity in A(P). Equality holds for every index (i,ℓ), so MATn makes the two genuine localic bracketings equal. □

**Interpretation.** The scattered index K lets us treat a localic relation as a genuine matrix, *including pointless P-fiber components*. Local finiteness gives the exact algebraic safeguard against the uncontrolled infinite join interchange that caused trouble elsewhere in Project A.

### 3.1. Exact graph-path expansion for all finite powers

**Corollary 3.2 (INTERNAL).** For any \(R\in\operatorname{Mat}_{\rm rcf}(K,\mathcal A(P))\), every finite power \(R^n\) is unambiguously defined, lies in the same associative algebra, and has entries
\[
\boxed{
(R^n)_{i_0i_n}
=
\bigvee_{\substack{i_0\to i_1\to\cdots\to i_n\\
R_{i_{r-1}i_r}\ne0}}
R_{i_0i_1}\circ_P
R_{i_1i_2}\circ_P\cdots\circ_P R_{i_{n-1}i_n}.
}\tag{PATH}
\]
For fixed start \(i_0\) and finite n the index-walk set is **finite** by row-finiteness. The expression can therefore be evaluated using only the known **finite** associativity/distributivity of the base algebra; no unproved arbitrary-index exchange appears.

**Proof.** By Theorem 3.1 the power is independent of parentheses. Apply the finite-index multiplication formula (FINMAT) inductively; each extension of a finite path set by finitely many neighbors stays finite. □

This gives a fully **localic analogue of ordinary adjacency-matrix path counting**: the index walk combinatorics is ordinary finite branching, but each walk carries a composition of potentially nonspatial relations in the P-fiber. In particular it provides a natural algebraic bridge to the original Cameron–Kumar graph-path viewpoint, while still not claiming a Dowker nerve theorem.

### 4. New graph-theoretic families beyond permutations

**Closed-edge matrices.** Let \(\mathcal C(P)\) be the algebra of **closed relations** on compact Hausdorff P (including 0 and Δ). Theorem 3.1 gives an associative algebra of row-and-column-finite index matrices whose nonzero entries are arbitrary closed relations on P. The **total resulting sublocale relation on G need not be closed**, because its nonzero sectors may accumulate through K. Nevertheless, all its bracketings associate.

**Locally finite graph with perfect fibres.** Take P=Cantor and K={0}∪{1/n:n≥1}, with the index edges of a graph consisting of loops and \(1/n\leftrightarrow1/(n+1)\) for n≥1. Each row and column has at most 3 nonzero index pairs (the limit index 0 is isolated as an **index-graph** component although not topologically isolated in K). Place a closed relation C_{ij}≤P² in each allowed sector (for example Γ_id or all P²). The resulting localic relation on (P×K)² has associative finite powers, despite potentially being **nonclosed overall** and despite P being perfect. The graph of an index permutation is the special monomial case with exactly one nonzero entry per row/column, each entry a homeomorphism graph.

**Important algebraic boundary:** Theorem 3.1 does **not** automatically allow adjoining *all rectangular relations on G*: a full G-rectangle may have infinitely many nonzero entries in every row/column, hence lie outside \(\operatorname{Mat}_{\rm rcf}\), and multiplying a general locally finite matrix by such a rectangle need not yield another *finite global sum of G-rectangles*. The stronger **balanced-witness theorem** handles the monomial homeomorphism case specifically and proves compatibility with the full rectangular algebra. Do not conflate these two extensions.

### 5. Future use and limits

This gives two complementary abstract models:

- **Balanced witness semigroups:** finite joins of **all global** p/q rectangles plus graph symmetries that transport supports and middle overlaps exactly.
- **Locally finite sublocale matrices:** arbitrary locally finite K-index graphs with entries in an associative localic relation algebra on P, but not necessarily compatible with every **global** rectangle on G.

Both arise from one geometric theorem: compact scattered K is an **atomic index** for complete sublocale lattices after any compact Hausdorff parameter.

The matrix formula (MUL), its proof using the genuinely localic composability locale, and the finite-support associativity reduction should be independently audited before canonical promotion. If certified, they give an explicit bridge between ordinary graph adjacency matrices/path counts and point-free relational composition without pretending that the entire locale-relations category is regular.

**Research sequencing:** test if the finite-support assumption can be weakened to a *finitary overlap condition*; then perform the requested big-picture Project A review; afterward return to intrinsic specialization and Dowker common-witness complexes.
