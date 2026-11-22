# Arbitrary-parameter scattered-index sublocale matrices — post-referee canonical proof
## 21 November 2026 · Session 11 · MAT*, MUL*, FINMAT*

**Status:** Accepted in an independent blind mathematical model-referee report (21 November 2026), with only proof clarifications requested. See [original report](project-a/audits/2026-11-21/MATSTAR_MULSTAR/INDEPENDENT_REFEREE_REPORT.md), [subsequent addendum](project-a/audits/2026-11-21/MATSTAR_MULSTAR/REFEREE_ADDENDUM.md) and [audit reconciliation](ProjectA_MATSTAR_MULSTAR_REFEREE_RECONCILIATION_2026-11-21.md). The four addendum propositions below are **post-report additions**, internally reconciled, not part of the blind audited candidate. This is a mathematical verification by an independent model session, **not** human peer review, formal verification or a literature-priority judgment.

Write \(\operatorname{Sub}(X)\) for the complete coframe of genuine sublocales, ordered by inclusion. All products are in \(\mathbf{Loc}\), and all images are smallest-sublocale images, not ordinary point images. Work in classical locale theory.

## Main theorem MAT*

Let \(P\) be **any locale** and \(K\) a **locally compact scattered Hausdorff topological space**. For each \(k\in K\), write \(e_k:P\times\{k\}\hookrightarrow P\times K\). Then
\[
\boxed{
\Phi:\operatorname{Sub}(P\times K)\overset{\cong}{\longrightarrow}
\prod_{k\in K}\operatorname{Sub}(P),\quad
\Phi(W)_k=e_k^{-1}W
}
\tag{MAT*}
\]
is an order isomorphism of complete lattices with inverse
\[
(W_k)_{k\in K}\longmapsto \bigvee_{k\in K}(e_k)_!W_k .
\]
It preserves arbitrary meets and joins by virtue of being an order isomorphism. It does **not** assert \(P\times K\cong\coprod_{k\in |K|}P\) in Loc.

### Elementary sublocale facts

1. Sublocales of a sublocale \(W\hookrightarrow X\) correspond exactly to sublocales of \(X\) below \(W\), preserving their joins and meets (order interval).
2. **Open-cover localization.** For a locale \(X\), \(W\le X\), and opens \(u_a\in\mathcal O(X)\) with \(\bigvee_a u_a=1\),
   \[
   W=\bigvee_a(W\wedge O_X(u_a)).
   \tag{OpenLoc}
   \]
   Proof: the frame map \(\mathcal O(X)\to\mathcal O(W)\) sends \((u_a)\) to a cover of \(W\). Their open sublocales join to \(W\) *inside* \(\operatorname{Sub}(W)\), hence inside \(\operatorname{Sub}(X)\).
3. For complementary open/closed sublocales \(o,c\) of \(X\), the **finite** distributive law gives
   \[
   W=(W\wedge o)\vee(W\wedge c).
   \tag{OC}
   \]
   The same works for finite clopen partitions. More generally, if \(e\in\operatorname{Sub}(X)\) is complemented, then \(e\wedge-\) preserves **all** joins: on the interval below \(e\) it is left adjoint to \(b\mapsto e'\vee b\), where \(e'\) complements \(e\). This is a *special complemented-element law*, not arbitrary meet over arbitrary join distribution.
4. Every localic map \(f:X\to Y\) has a sublocale pullback \(f^{-1}\) preserving arbitrary meets and finite joins, with image left adjoint \(f_!\dashv f^{-1}\); hence \(f_!\) preserves **all joins**, and images are functorial. No arbitrary image/base-change stability is assumed.

### Proof of MAT*

**Compact scattered \(K\).** If \(K\ne\varnothing\) is compact scattered Hausdorff, it has a clopen basis and successor Cantor–Bendixson height \(\alpha+1\) with a **finite nonempty** last derivative \(F=K^{(\alpha)}\). Separate the points of \(F\) by a finite clopen partition \(K=\bigsqcup_r N_r\), each \(N_r\) containing a single \(k_r\in F\). For any \(W\le P\times K\), split it over the clopen \(P\times N_r\), then split each such piece into the **closed** index sector \(P\times\{k_r\}\) and its **open** complement. Every point of \(N_r\setminus\{k_r\}\) has a compact clopen neighborhood \(C\) avoiding \(F\). As \(C\) is clopen in \(K\), \(C^{(\beta)}=C\cap K^{(\beta)}\), so its height is strictly below \(\alpha+1\). OpenLoc localizes the remaining piece over these \(C\); transfinite induction supplies the singleton decomposition in each chart. This establishes
\[
W=\bigvee_{k\in K}\bigl(W\wedge(P\times\{k\})\bigr).
\tag{E}
\]
The proof makes no use of points or regularity of \(P\).

**Locally compact scattered \(K\).** Its one-point compactification \(K^+\) is compact, Hausdorff and scattered, hence zero-dimensional. Every point of \(K\) has a compact clopen neighborhood avoiding \(\infty\). These compact clopen sets cover \(K\), so their inverse images cover \(P\times K\). Apply OpenLoc and the compact case chartwise. This proves (E) for arbitrary locally compact scattered Hausdorff \(K\).

**Reconstruction.** Each singleton sector \(E_k=P\times\{k\}\) is a complemented closed sublocale; the other sectors lie inside its complementary open part. Consequently
\[
E_k\wedge\bigvee_j(e_j)_!W_j=(e_k)_!W_k.
\]
Use the complemented-element law, or simply group \(j=k\) against all \(j\ne k\) and apply finite distributivity. This proves that the reconstruction map is a left inverse of \(\Phi\); (E) makes it a right inverse. The empty-index and empty-parameter cases have the unique trivial-lattice interpretation.

## Actual binary localic matrix multiplication MUL*

Put \(G=P\times K\). Finite products \(K^n\) are again locally compact scattered Hausdorff; thus MAT* applies to \(P^n\times K^n\cong G^n\) for \(n=1,2,3\). For arbitrary genuine localic binary relations \(R,S\le G^2\), write \(R_{ij},S_{jk}\le P^2\) for their index sectors. Then
\[
\boxed{(R\circ S)_{ik}=\bigvee_{j\in K}(R_{ij}\circ_P S_{jk}).}
\tag{MUL*}
\]

**Proof.** Construct first the *actual localic composability sublocale*
\[
Q=(\pi_{12}^{G})^{-1}R\wedge(\pi_{23}^{G})^{-1}S\le G^3.
\]
Its \(ijk\)-sector is, by the pullback squares for singleton sectors,
\[
Q_{ijk}=(\pi_{12}^{P})^{-1}R_{ij}\wedge(\pi_{23}^{P})^{-1}S_{jk}\le P^3 .
\]
MAT* **decomposes Q itself** into the join of all these sectors. Now use the image adjunction, join-preservation of image, and the **equality of locale maps on each sector**
\[
\pi_{13}^G e_{ijk}=d_{ik}\pi_{13}^P
\]
with \(d_{ik}:P^2\hookrightarrow G^2\). Then
\[
(\pi_{13}^G)_!Q
=\bigvee_{i,j,k}(d_{ik})_!(\pi_{13}^P)_!Q_{ijk}
=\bigvee_{i,k}(d_{ik})_!\Big(\bigvee_j R_{ij}\circ_P S_{jk}\Big).
\]
Unique sector reconstruction gives MUL*. **No** unrestricted infinite meet/join interchange and **no** arbitrary Beck–Chevalley rule for images has been invoked.

MUL* is a formula for a **binary composite only**. It does not imply unrestricted associativity, which may fail in \(\operatorname{Sub}(P^2)\).

## FINMAT*: associative finite-support algebra

Let \(\mathcal A(P)\subseteq\operatorname{Sub}(P^2)\) contain \(0,\Delta_P\), be closed under converse, genuine localic composition, and finite joins, and have **associative composition on \(\mathcal A(P)\)**. (A separate finite-distributivity assumption is unnecessary: genuine localic composition preserves finite joins in each variable, since sublocale inverse image preserves finite joins, the coframe is finitely distributive, and image preserves joins.)

Let \(\operatorname{Mat}_{\rm rcf}(K,\mathcal A(P))\) consist of genuine relations on \(G\) having coefficients in \(\mathcal A(P)\), with finitely many nonzero coefficients in every row and every column. This is an associative, unital, converse-closed, finite-join relation algebra under genuine localic composition. Its unit is \(\Delta_G\), the diagonal matrix with entries \(\Delta_P\). In a fixed \((i,\ell)\) entry, both triple bracketings expand into a **finite** join indexed by \(j,k\), to which associativity and finite distributivity in \(\mathcal A(P)\) apply. Products remain row-/column-finite. Finite-length paths produce finite sums at each fixed starting index. Set \(R^0=\Delta_G\) for the length-zero path convention. This does not assert closure under arbitrary joins of matrices or compatibility with *all* global \(p/q\) rectangles.

## Post-report addendum: separately labeled corollaries

The referee subsequently proposed the following, **outside the submitted blind candidate**. We have inspected their short derivations but retain their distinct provenance.

**A1 — Heredity to subspaces.** If \(B\subseteq K\) is *any* topological subspace of a locally compact scattered Hausdorff \(K\), then
\[
\operatorname{Sub}(P\times B)\cong\prod_{b\in B}\operatorname{Sub}(P).
\]
The subspace inclusion \(B\hookrightarrow K\) is a sublocale embedding, preserved by product pullback along \(P\times K\to K\). In MAT* coordinates, \(P\times B\) has coefficient \(P\) exactly at indices in \(B\) and \(0\) otherwise. Sublocales below it are the corresponding order interval. For powers of \(B\), use that \(B^n\hookrightarrow K^n\) is a localic sublocale whose index support is the ordinary point set \(B^n\); MAT* for \(K^n\) ensures this even when the localic product of \(B\)'s need not be identified by a naive topological product rule. The full binary MUL* and FINMAT* deductions follow. This enlarges the permitted indices to some **non-locally-compact** scattered Hausdorff spaces; it does not prove the result for every scattered Hausdorff space.

**A2–A3 — Indexed pullback/image.** Given locales \(P',P\), admissible indices \(K',K\), a locale map \(f:P'\to P\), a continuous \(h:K'\to K\), and \(F=f\times h\),
\[
(F^{-1}W)_{k'}=f^{-1}(W_{h(k')}),\qquad
(F_!V)_k=\bigvee_{h(k')=k} f_!(V_{k'}).
\]
The first is pullback functoriality along singleton sectors. The second follows by the adjunction \(F_!\dashv F^{-1}\) and coefficientwise inequalities. MUL* is the special image-assembly instance \(h(i,j,k)=(i,k)\) **after** forming the composability sublocale.

**A4 — Coordinated finite-sector truncation.** For finite \(F\subseteq K\), let \(R|_F,S|_F\) restrict both indices to \(F\). Then
\[
R\circ S=\bigvee_{F\Subset K}\bigl((R|_F)\circ(S|_F)\bigr).
\]
Check the \((i,k)\) coefficient using MUL*: every triple \(i,j,k\) lies in one finite \(F\). This special directed approximation is **not** continuity of composition for arbitrary directed joins of relations.

**One-sided finite-support lifts.** Row-finite \(\mathcal A(P)\)-matrices alone form an associative unital finite-join algebra (not generally converse-closed); likewise column-finite matrices. Converse exchanges the two; their intersection is the rcf algebra.

## General finite-join product correction

For *any* locales \(Y,Z\) and \(S,T\le Y\),
\[
\boxed{(S\vee T)\times Z=(S\times Z)\vee(T\times Z).}
\tag{FJP}
\]
Indeed, product with \(Z\) of a sublocale \(S\hookrightarrow Y\) is its pullback along \(\pi_Y:Y\times Z\to Y\), and sublocale inverse image preserves finite joins. This completely resolves the former "arbitrary Loc finite-join" question from the Opus addendum; it **does not** extend to arbitrary infinite sublocale joins. For a published articulation of the coframe-morphism property, see Igor Arrieta and Anna Laura Suárez, *The coframe of D-sublocales of a locale and the \(T_D\) duality*, preprint §2 ("Images and preimages"), https://www.mat.uc.pt/preprints/ps/p2034.pdf .

## Literature and scope

Picado–Pultr, *Axiom \(T_D\) and the Simmons sublocale theorem*, CMUC 60 (2019), Theorem 3.3, already supplies important **\(P=1\)** scattered \(T_D\) antecedents; Proposition 1.5 concerns complemented-element distribution. Neither the referee nor this note claims MAT*/MUL* priority beyond known literature. A separate systematic antecedent check remains appropriate if publication becomes a goal.
