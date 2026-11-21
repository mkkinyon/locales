# Project A — internal adversarial audit of exact scattered-index matrix multiplication
## 21 November 2026 · INTERNAL only, not an independent referee report

**Reviewed:** [exact matrix multiplication and locally finite matrix algebra](ProjectA_SCATTERED_INDEX_LOCALLY_FINITE_LOCALIC_RELATION_MATRICES_2026-11-21.md), based on [atomic index theorem and balanced witness group algebra](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md). **Imported independently reviewed:** the rectangular composition rule (RC) and positive locally closed graph calculus; the closed-relation/proper-image calculus is part of the previously investigated compact-locale branch. All present matrix results remain **candidate internal proofs**, requiring external review before canonical promotion.

### Verdict

**Provisional favorable internal audit** with the *precise scope* that row-and-column finite index support is essential to use only finite distributivity of the base relation algebra. The exact matrix product formula (MUL) itself is more general and does not presume associativity on the base. It must not be misread as asserting associative composition for every sublocale relation on P×K.

### Challenges and checks

1. **Full sublocale matrix decomposition:** Requires the preceding nontrivial atomic-index theorem, \(\operatorname{Sub}(P^n\times K^n)\cong\operatorname{Sub}(P^n)^{K^n}\). Finite powers K^n are scattered (isolate a point successively in projection/fiber). Thus the full P³ nonspatial structure is retained in each triple sector; nothing is pointified inside P.

2. **Source of composability Q:** In locale theory Q=π12^-1(R)∧π23^-1(S) in G³ is the **genuine pullback** of relations. For each closed index triple (i,j,k), its restriction is exactly the ordinary localic composability pullback of R_ij and S_jk in P³. This follows by finite-limit stability under the closed sector inclusions.

3. **Projection images under arbitrary fibre joins:** By matrix reconstruction, \(Q=\bigvee Q_{ijk}\). The localic **image** operation \((\pi_{13})_!\) on sublocales is a left adjoint, hence preserves arbitrary joins. This is categorically distinct from claiming that relational composition distributes over arbitrary joins. Therefore \(\mathrm{im}(Q)=\bigvee_{ijk}\mathrm{im}(Q_{ijk})\) is legitimate, and each image lies in its fixed closed (i,k) sector. Reindexing over j gives the exact formula \((R\circ S)_{ik}=\bigvee_j(R_{ij}\circ_P S_{jk})\).

4. **No forbidden arbitrary interchange:** The proof of MAT uses one infinite fibre join but separates a target fiber with the **single** open support \(K\setminus\{k\}\), avoiding an illicit infinite distributivity. The proof of MUL applies arbitrary-join preservation only to the image left adjoint; the pullback/meet is computed **before** decomposing the composability locale. The locally finite theorem expands only **finite** joins for each matrix entry.

5. **Support closure:** Row-finite R and S have row-finite product: each row i of R hits finitely many intermediate j, each with finitely many targets from S. Column-finite is dual. Finite joins preserve both finiteness conditions. Converse transposes the support matrix and dualizes entries, preserving the **intersection** of row and column finite classes.

6. **Associativity:** For a fixed (i,l), row-finite R and S yield a finite set of (j,k) paths from i of length two; expanding either triple bracketing requires only finite distributivity, and each summand agrees by associativity of \(\circ_P\) *inside the chosen base algebra*. No unbounded intermediate join appears. Equality of all matrix entries implies equality of the genuine sublocales by MAT.

7. **Unit and involution:** The full diagonal Δ_{P×K} has only k=k diagonal entries Δ_P, one per row/column; converse flips indices and converses component relation. Verified.

8. **Strictness over prior monomial group:** The balanced-witness group corresponds to *one* homeomorphism-graph entry per row and column. The new matrix theorem includes arbitrary finite-degree index graphs with closed relations / rectangles / locally closed graphs in its entries, not just permutations. Thus it is a substantive extension, not a renamed version of the earlier example.

9. **Global rectangle caution:** An arbitrary G-rectangle p/q(A,B) can occupy an infinite Cartesian set of index pairs. It is generally *not* row/column finite. The matrix theorem **does not** claim closure of its locally finite algebra after adjoining all such rectangles. The balanced-witness theorem handles full rectangular adjunction for deterministic monomial indices, but arbitrary locally finite matrices need different conditions to handle global rectangles.

10. **An adversarial edge case:** Let P be compact perfect (Cantor), and let K be a convergent sequence with limit 0. Choose nonzero P-relation entries along infinitely many (1/n,1/(n+1)) index edges, no edges at index 0. The resulting relation may be nonclosed in G² as index pairs approach (0,0). Nonetheless its matrix has rows/columns of degree ≤2, so it lies in the locally finite algebra if each entry belongs to an associative base algebra. Its powers associate by the finite path formula, even though **ambient** G is not scattered. This checks that the theorem's point is not disguised "all relations are point-determined".

### Scope and recommendation

The two new complementary criteria are: (a) a **balanced witness semigroup** preserving the entire global p/q rectangular algebra; (b) an **associative locally finite matrix algebra** over any compact scattered index and an associative finite-join base relation algebra.

An independent referee should first scrutinize the **atomic-index reconstruction** in a genuinely nonspatial P, then the localic compositor Q and image-to-matrix formula, and finally the finite path rebracketing. A combined packet would be preferable to premature theorem-by-theorem audit fragmentation, since MAT is their common dependency.

The larger investigation can now choose between testing the boundary of *finite-path* support (weaker than row/col finiteness) and moving to the promised project-wide big picture review. No new source has independently certified this internal audit.
