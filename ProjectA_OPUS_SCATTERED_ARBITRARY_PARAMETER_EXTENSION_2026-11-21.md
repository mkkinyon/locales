# Scattered-index sublocale matrices with arbitrary parameter locales
## Claude Opus 5.5 High proposal of 21 November 2026 · internal proof reconstruction

**Status:** *post-report external-reader deduction, internally reconstructed*, **not** part of the previous blind MAT/MUL/FINMAT packets and not subjected to a second independently blind audit. The proof below is classical and uses clopen Cantor–Bendixson decomposition. **No literature novelty is asserted**: it may follow from Simmons' scattered sublocale theorem / locale-product theory. The original [compact-parameter MAT/MUL theorem](ProjectA_BALANCED_WITNESS_TRANSPORT_AND_SCATTERED_MATRIX_ALGEBRA_2026-11-21.md) remains fully valid with its existing external audit; this is an extension, not a correction to it.

### Theorem (Opus extension E1)

Let \(P\) be an **arbitrary locale** and \(K\) a **locally compact, scattered Hausdorff space**, in classical locale theory. For each \(k\in K\), let \(i_k:P\times\{k\}\hookrightarrow P\times K\) be the **closed** singleton-index sector, and denote \(\mathsf{Sub}(X)\) the complete lattice of sublocales of X. Then
\[
\boxed{
\Phi(W)=(W\wedge(P\times\{k\}))_{k\in K}:
\mathsf{Sub}(P\times K)\ \simeq\
\prod_{k\in K}\mathsf{Sub}(P)
}
\tag{MAT*}
\]
is a complete-lattice order isomorphism, whose inverse sends a family \((W_k)\) to the **sublocale join** \(\bigvee_k i_{k*}(W_k)\).

For finite \(n\) the same applies to parameter \(P^n\) and index \(K^n\), since finite products of locally compact scattered Hausdorff spaces remain locally compact, scattered and Hausdorff.

**Consequently** for **arbitrary locale** P and K as above, for any genuine localic binary relations \(R,S\hookrightarrow(P\times K)^2\),
\[
\boxed{(R\circ S)_{ik}=\bigvee_{j\in K} (R_{ij}\circ_P S_{jk}).}\tag{MUL*}
\]
This is an equality of actual localic **binary composites**. It does **not** claim the composite is associative for unrestricted matrices.

If \(\mathcal A(P)\subseteq\mathsf{Sub}(P^2)\) contains \(0,\Delta_P\), is closed under genuine composition, converse and finite joins, and is associative with finite-join-distributive composition, the row-**and**-column-finite \(\mathcal A(P)\)-valued K-index matrices form an associative **unital** finite-join algebra with exact finite-path expansions. The only assumptions on P are those required for \(\mathcal A(P)\); **compact Hausdorff P is needed only when the chosen fibre algebra is the p/q rectangle algebra**.

### Proof check: sublocales localize across open covers

For **any locale** X, sublocale \(W\hookrightarrow X\), and open cover \((U_i)\) of X, the open sublocales \(W\wedge O(U_i)\) cover W, because inverse images of those opens cover W and open-sublocale joins reflect joins of opens:
\[
W=\bigvee_i (W\wedge O(U_i)).
\tag{OpenLoc}
\]
This is *not* the false identity \(W\wedge\bigvee_j S_j=\bigvee_j(W\wedge S_j)\) for **arbitrary sublocales** \(S_j\): the \(O(U_i)\) here must all be **open**.

Likewise, for a **clopen decomposition** \(X=C\sqcup D\), its two corresponding sublocales are complements in the distributive **finite** sublocale lattice, so
\[
W=(W\wedge C)\vee(W\wedge D).
\tag{Clop}
\]
For a **closed** \(c\hookrightarrow X\) with **open complementary** sublocale \(o\), the same finite decomposition holds:
\[
W=(W\wedge c)\vee(W\wedge o).
\tag{Closed/Open}
\]
These two localizations depend only on the distributivity of the finite sublocale lattice. They do not use regularity, spatiality, compactness or Hausdorffness of P.

### Step 1. Compact scattered index

Let K be **compact scattered Hausdorff**. Such K is a **zero-dimensional Stone space** of successor Cantor–Bendixson height \(\alpha+1\), with a nonempty **finite** last derivative \(K^{(\alpha)}=\{k_1,\ldots,k_m\}\). We prove (MAT*) by transfinite induction on its Cantor–Bendixson height.

Choose a **finite clopen partition** \(K=\bigsqcup_{i=1}^m N_i\) with \(N_i\cap K^{(\alpha)}=\{k_i\}\). Use (Clop) to decompose any \(W\hookrightarrow P\times K\) across these **clopen** N_i.

Fix i. Inside \(P\times N_i\), split the **closed** singleton sector \(c_i=P\times\{k_i\}\) from its **open** complement \(o_i=P\times(N_i\setminus\{k_i\})\), using (Closed/Open). The open subspace \(N_i\setminus\{k_i\}\) is covered by **compact clopen** subspaces C of strictly smaller Cantor–Bendixson height, because every point admits compact clopen neighborhoods disjoint from the finite last derivative. By (OpenLoc), the restriction \(W\wedge o_i\) is the **join** of its restrictions to P×C. Each such restriction splits into singleton-index fibres by the induction hypothesis. Adding the sector at k_i and summing over i proves
\[
W=\bigvee_{k\in K} \bigl(W\wedge(P\times\{k\})\bigr).
\tag{Exhaust}
\]

No separation of an ambient **P×K** closed support was necessary. The proof depends only on the scattered **index** and the standard open/closed sublocale decompositions.

### Step 2. Locally compact scattered index

Every **locally compact scattered Hausdorff K** admits a cover by **compact clopen subspaces** (zero-dimensionality follows from local compactness, Hausdorffness and scatteredness). Restrict W to P×C over each such clopen C. These are **open** sublocales whose join covers P×K. Use (OpenLoc) and Step 1 inside each compact clopen chart. This proves (Exhaust) for locally compact K.

### Step 3. Fibres determine a join uniquely

For any Hausdorff K and any family \((W_k)\) of sublocales of P, write \(\Sigma(W_k)=\bigvee_{k} i_{k*}(W_k)\). Fix k. Every other sector j≠k lies **below the open sublocale** \(P\times(K\setminus\{k\})\), disjoint from the closed k-sector. Its arbitrary join also lies below this open complement. Finite distributivity therefore gives
\[
\bigl(\Sigma(W_k)\bigr)\wedge(P\times\{k\})=W_k.
\]
Thus \(\Phi\Sigma=\mathrm{id}\), while (Exhaust) gives \(\Sigma\Phi=\mathrm{id}\). These are inverse order-isomorphisms and hence automatically preserve **all** lattice joins/meets.

### Step 4. Actual matrix multiplication

Apply (MAT*) to the **already-formed** localic composability sublocale
\[
Q=\pi_{12}^{-1}(R)\wedge\pi_{23}^{-1}(S)\hookrightarrow(P\times K)^3.
\]
The triple sector (i,j,k) is exactly the genuine composability object of the corresponding P-fibre relations, since restricting a relation to a closed singleton-index sector is a categorical pullback. Reconstruct Q as a **join of its sectors**. The localic image along \(\pi_{13}\) is a **left adjoint** on sublocale lattices and therefore preserves **arbitrary joins**. Taking its image *after* the decomposition yields (MUL*), entry by entry. No distribution of an arbitrary sublocale **meet** over infinite joins is used.

For row-and-column finite matrices the standard finite-expansion argument from [the previously audited FINMAT proof](ProjectA_SCATTERED_INDEX_LOCALLY_FINITE_LOCALIC_RELATION_MATRICES_2026-11-21.md) now applies unchanged.

### Remaining checks and caveats

- The proof of MAT* has been independently reconstructed from the reader's suggested **Cantor–Bendixson decomposition**, without using regularity of P.
- A potential *nonconstructive/classical* ingredient is the zero-dimensionality/compact-clopen decomposition of locally compact scattered Hausdorff spaces; do not claim a constructive locale-theoretic version.
- A literature comparison against Simmons/Picado–Pultr, Johnstone–Sun and work on products of scattered locales is needed before any originality statement.
- This theorem **does not imply** that \(P\times K\) is the **coproduct of discrete K many copies of P** as a locale. It gives a complete **sublocale-lattice** decomposition only; openness, closedness and topology of K remain relevant.
- The theorem generalizes B07/B08 hypotheses, but the **previous E audit** only checked the compact Hausdorff parameter setting. **Record MAT*/MUL* as new Opus-external proposal plus internal proof reconstruction (I), not E**, until a separate independent audit or other proof comparison.
