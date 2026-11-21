# Project A — balanced-witness and scattered-matrix post-referee reconciliation
## 21 November 2026 · Session 10 · external audit reconciled

**Source documents (verbatim):**
- [Independent blind referee report](project-a/audits/2026-11-21/BALANCED_WITNESS_SCATTERED_MATRIX/INDEPENDENT_REFEREE_REPORT.md)
- [Independent referee addendum](project-a/audits/2026-11-21/BALANCED_WITNESS_SCATTERED_MATRIX/REFEREE_ADDENDUM.md)

**Submitted candidate notes:**
- [Balanced witness transport and scattered-index algebra](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md)
- [Exact localic matrix multiplication and locally finite lift](ProjectA_SCATTERED_INDEX_LOCALLY_FINITE_LOCALIC_RELATION_MATRICES_2026-11-21.md)

**Audit protocol:** Blind external review; the referee did not see internal adversarial reports. The previously independently reviewed compact-Hausdorff rectangle rule (RC) was imported as a premise, not re-proved.

## 1. Adjudication

| Claim | Post-referee disposition |
|---|---|
| SPLIT: fibre observation/reconstruction | Accepted |
| MAT: compact-Hausdorff scattered-index characterization | Accepted |
| MATn: finite scattered powers | Accepted |
| Balanced-witness algebra criterion (G,T,O) | Accepted **conditional on RC** |
| GRP: point-generated monomial graph multiplication | Accepted |
| Abstract wreath-product group identification | Correct **when the fibre P is nonempty**; otherwise not faithful |
| ACT: both p and full nonspatial q rectangle transport | Accepted |
| BAL: balanced nonzero sublocale-meet overlap | Accepted |
| TWIST: discrete-to-scattered complete sublocale-lattice transport | Accepted |
| Broad TWIST partial-graph associativity extrapolation | **Not established** by the stated hypotheses; separate proof needed |
| MUL: arbitrary binary localic relation matrix formula | Accepted, **does not** imply global associativity |
| FINMAT: row-and-column-finite associative converse-closed lift | Accepted |
| PATH: finite index-walk expansion | Accepted for n≥1; add n=0 unit convention if desired |

The two genuine issues are (i) the empty-fibre faithfulness exception for the abstract wreath product, and (ii) the lack of sufficient diagrammatic hypotheses in the ancillary TWIST-to-graph extrapolation. No objection to MAT/MUL/FINMAT or the discontinuous compact scattered monomial graph construction remains.

## 2. Corrections and proof clarifications

### 2.1 Closed-sector restriction lemma

For a compact Hausdorff space X, any ordinary A⊆X, and any **closed** F⊆X,
\[
[A]_X=[A\cap F]_X\vee[A\setminus F]_X,
\qquad [A]_X\wedge F=[A\cap F]_X.
\]
Indeed the second summand lies in the complementary **open** X\F; apply finite distributivity of the sublocale coframe. This does not authorize pointwise intersection of induced sublocales with arbitrary sublocales. It establishes that the closed (i,j) block of a point-generated monomial graph is precisely the corresponding fibre homeomorphism graph, with no extra pointless sector component.

### 2.2 Exact pullback/image order in MUL

Form the **actual** composability sublocale Q in G³ first, then reconstruct Q from its closed (i,j,k) sectors via MATn. Restriction/base change identifies each sector with the genuine P³ composability pullback. Next apply arbitrary-join preservation of the *image* under projection π13. Finally reconstruct the result from output sectors using SPLIT, not by assuming a closed-sector meet distributes over an infinite join. This proves
\[
(R\circ S)_{ik}=\bigvee_{j\in K}R_{ij}\circ_P S_{jk}
\]
for arbitrary binary relations R,S, regardless of associativity of the base P calculus.

### 2.3 Faithfulness and zero cases

The graph multiplication (GRP) is valid also for P=∅, but then G=∅ and every displayed graph is the unique zero relation (also the unit). The identification with \(\operatorname{Homeo}(P)^{|K|}\rtimes\operatorname{Sym}(|K|)\) is faithful only if P≠∅. Also replace a casual “perfect K” Booleanization example by **nonempty perfect K**. The empty perfect space has zero Booleanization.

### 2.4 TWIST: separate lattice and graph assertions

The discrete-to-scattered map g:P×D→P×K, with index bijection b and fibrewise homeomorphisms, gives a complete-lattice bijection on every parameterized sublocale lattice by scattered/discrete fibre relabeling. That fact **alone** does not establish graph composition G, rectangular transport T, or overlap O for graph relations regarded as sublocales of an unspecified common compact ambient square.

A precise safe replacement: work inside a **single** X=P×K_* with P nonempty compact Hausdorff and K_* compact scattered Hausdorff. Use arbitrary **partial monomial maps** on subsets of the index set, with at most one entry per row and column and homeomorphism-graph entries. Genuine sectorwise pullback/image proves G,T,O for this inverse semigroup of partial monomial graphs, so its finite-join extension with all global p/q rectangles is associative conditional on RC. General locally closed-sector TWIST extrapolations remain an open proof obligation. Do not silently infer this generality from lattice isomorphisms.

### 2.5 Smaller editorial points

- Clarify finite-join, not arbitrary-join, distributivity of **relational composition**.
- Include \(\Delta_P\) in diagonal sectors as the matrix unit.
- The PATH formula displays n≥1; n=0 is the identity matrix, with the empty-walk convention.
- The ideal conclusion is within the finite-join rectangular/graph algebra, not an arbitrary-join ideal for all localic relations.

## 3. Additional mathematical results from the report

### 3.1 Exact RHR obstruction

Assume nonempty G, RC, G, T, and closure of graph generators. **Within this regime** associativity of all rectangle–graph–rectangle triples forces O. Test
\[
q(G,B),\quad \Gamma_h,\quad q(C,G).
\]
The respective bracketings return \(q(G,G)\ne0\) or zero according to the two tests in O. Conversely O supplies the missing RHR compatibility in the balanced-witness theorem. This does **not** make G,T,O necessary for every possible associative relation subalgebra.

### 3.2 Completely discrete fibre P=1

For P a one-point locale and K compact scattered Hausdorff, MAT over K² and MUL identify **all** localic relations on K with ordinary set-theoretic binary relations on |K|, with Boolean matrix multiplication. In this case unrestricted relation composition is associative. This observation helps locate nonassociativity in the richer, possibly nonspatial P-coordinate.

## 4. New addendum results (not part of the submitted candidate)

### 4.1 Discrete-index comparison

Let P be compact Hausdorff, K compact scattered Hausdorff, and D the underlying set |K| with its discrete topology. The fibre-coordinate isomorphisms yield
\[
\mathsf T_n:\operatorname{Sub}((P\times K)^n)\cong
\operatorname{Sub}((P\times D)^n),\qquad n=1,2,3,
\]
preserving arbitrary sublocale meets and joins. On n=2 they also preserve converse, diagonal, and **genuine binary relational composition**, since MUL is identical on the scattered and discrete sides. They preserve global p/q rectangles fibrewise, and identify monomial point-generated graphs with graphs of genuine homeomorphisms of P×D.

Thus the **full** relation-composition magma with its sublocale-lattice structure cannot detect the topology of a scattered index (up to chosen bijection). No unrestricted associativity is inferred. The comparison does **not** preserve open/closed status, closure, or give a locale isomorphism; P×D may be noncompact. If using RC on the discrete side, transport the previously established identity instead of re-invoking the compact-Hausdorff theorem.

This is the preferred conceptual explanation for safe **discontinuous** index permutations, and a natural bridge to ordinary graph matrices.

### 4.2 One-sided finite lifts and finite-flank associativity

If A(P) contains 0, Δ, and is associative and finite-join-distributive with appropriate closure, then A(P)-valued **row-finite** matrices form a unital associative finite-join algebra, as do **column-finite** matrices. Converse exchanges these two algebras; their intersection is the row-and-column-finite converse-closed algebra.

Further, for **arbitrary** A(P)-valued R,S,T, if R is row-finite and T column-finite, then
\[
(R\circ S)\circ T=R\circ(S\circ T)
\]
even when S has infinite support. For fixed (i,ℓ), the outer supports
\[
J_i=\{j:R_{ij}\ne0\},\qquad L_\ell=\{k:T_{k\ell}\ne0\}
\]
are finite, and both bracketings expand over the same finite set \(J_i\times L_\ell\). There is no claim that all A(P)-valued matrices form an associative algebra.

### 4.3 Locally compact scattered-index MAT

The referee proposes and sketches an extension: if K and Z are **locally compact Hausdorff** and K is scattered, then every sublocale of Z×K is recovered from its closed point-index fibres. Conversely failure of scatteredness gives a nonzero pointless Booleanization ghost over a closed nonempty perfect subspace. The positive proof uses fitness/regularity of the ambient product and **isolates a point in the nonempty subset** pr_K(L) of a nonempty closed support L; that projection need not be closed. Thus compactness of the parameter and index is not needed for this strategy.

**Status:** New referee-origin deduction from the addendum, persuasive with a proof sketch, but outside the independently submitted compact-Hausdorff packet. Record without silently changing the scope of the independently audited theorem. Extensions of MUL and one-sided matrix algebras to locally compact K are natural corollaries to verify separately.

## 5. Project implications and next work

- **Accepted boundary endpoint:** scattered-index matrices provide an exact and robust positive mechanism for genuinely localic graph composition with nonspatial fibre entries, including safe discontinuous monomial graphs and locally finite index graphs.
- **Key structural insight:** the scattered-index topology is invisible to the full binary sublocale-relation calculus after passing to discrete-index coordinates, although it remains visible to topological predicates.
- **Boundary obligation retained:** do not promote the general TWIST partial-graph assertion without a common ambient-space pullback/image proof.
- **Recommended sequence:** add corrections to the two candidate notes; preserve the referee documents and addendum; then conduct the planned Project A **big-picture review** (original Cameron–Kumar motivation, hierarchy, graph algebras, and failures). Subsequently revisit intrinsic specialization graphs and the Dowker/common-witness picture. The locally compact extension and general ambient-sector lemma are good follow-up problems, but need not delay the overview.

No literature priority is claimed for any result in these notes.
