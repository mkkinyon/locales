# CO-01 Boolean probe extension: arbitrary Cantor endomorphisms preserving D and V

**11 November 2026. Internally checked new exact generalized-point test and explicit noninvertible witness. Does NOT settle Arrieta's cube.** Builds on the [all-cover homeomorphism criterion in associativity audit VIII §11](A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md) and the [countable clopen normal form](ProjectA_CO01_Arrieta_countable_clopen_generators_finite_cover_gap_2026-11-11.md).

## 1. Exact criterion without invertibility

Let \(C=2^\mathbb N\), \(K_n\) the nonzero finite-support points with final 1 at n, \(D=\bigcup_nK_n\), \(V=C\setminus D\), \(B=\operatorname{RO}(V)\), and q:O(V)→B the double-negation frame quotient. Let \(\rho,\lambda:C\to C\) be **continuous, not necessarily homeomorphisms**, satisfying
\[
\rho(D)\subseteq D,\ \rho(V)\subseteq V,\qquad
\lambda(D)\subseteq D,\ \lambda(V)\subseteq V.
\tag{1.1}
\]
The restrictions to V are continuous, hence define frame maps \(h_\rho=q\circ\rho_V^*, h_\lambda=q\circ\lambda_V^*:O(V)\to B\).

Define
\[
P_{\rho,\lambda}=
\{x\in D:\exists n\ge1,\ \rho(x),\lambda(x)\in K_n\}.
\tag{1.2}
\]

**Theorem.**
\[
\boxed{\quad (h_\rho,h_\lambda):\operatorname{Loc}(B)\to V^2
\text{ factors through }A
\iff P_{\rho,\lambda}\text{ is dense in }C.\quad}
\tag{1.3}
\]

**Sufficiency:** For any Θ-admissible cover \(\mathcal C\) and nonempty basic cylinder O⊂C, pick x∈O∩P and n with rho(x),lambda(x)∈K_n. Choose a∈C and Cantor-open W⊇K_n with W∩V⊆a. The Cantor-open O∩rho^{-1}(W)∩lambda^{-1}(W) is nonempty at x; its V-trace is nonempty and belongs to \(\bigcup_{a\in\mathcal C}(\rho_V^{-1}a\cap\lambda_V^{-1}a)\). Thus the latter union is dense in V, so q maps it to 1 and the pair factors through A. This uses continuity and density of V, not invertibility.

**Necessity:** If P is not dense choose nonempty clopen O⊆C disjoint P. Let E={x:rho(x)=lambda(x)} closed. It has no interior in O: any nonempty open O'⊆O∩E contains d∈D (D dense), and rho(d)=lambda(d)∈D by (1.1), contradicting O∩P=∅. Shrink to nonempty Cantor clopen O'⊆O\E and let F=(rho,lambda)(O') compact. Then F avoids Δ_C, and it avoids K_n×K_n for every n: if an x∈O' had both images in K_n⊆D, then x∉V by preservation of V, hence x∈D, contradicting P-free O. For each n choose Cantor-clopen W_n⊇K_n with F∩(W_n×W_n)=∅ (compact separation from K_n²). For each z∈C choose a Cantor-clopen U_z∋z with F∩U_z²=∅, and by compactness choose finitely many U_i covering C. The cover
\[
\mathcal C^*=\{W_n\cap V:n\ge1\}\cup\{U_i\cap V:1\le i\le m\}
\]
is Θ-admissible, but no member a contains both rho(x),lambda(x) for any x∈O'∩V. Hence the common-cover union is not dense and q of γ_C* is not 1. Thus the pair does not lie in A. QED.

**This extends the previous exact Boolean test from the homeomorphism group to a noninvertible transformation monoid.** It makes no claim about arbitrary frame maps into B that do not arise this way.

## 2. Explicit noninvertible two-hop witness

Define the coordinate-doubling map \(\delta:C\to C\) by
\[
(\delta x)_{2i}=x_i,\qquad(\delta x)_{2i-1}=0.
\]
It preserves D and V forward: finite nonzero supports map to finite nonzero supports, zero maps to zero and infinite supports to infinite supports. For any d∈D with highest 1 at n,
\[
\max\operatorname{supp}(\delta d)=2n\ne n
=\max\operatorname{supp}(d),
\]
so \(P_{\mathrm{id},\delta}=\varnothing\), and the theorem gives
\[
h_{\mathrm{id}}\not\mathrel A h_\delta.
\tag{2.1}
\]

Let σ be the coordinate permutation swapping (4,8),(16,32),(64,128),... (all pairs \((4^k,2\cdot4^k)\) for k≥1), and fixing all other indices, in particular all odds. Given any prescribed finite prefix pattern of length m, add a final 1 at an odd n larger than m and every value σ(1),...,σ(m). Both x and σ(x) have highest 1 at n; thus \(P_{\mathrm{id},\sigma}\) is dense and \(h_{\mathrm{id}}\mathrel A h_\sigma\).

For the same prefix, instead add the last 1 at n=4^k large enough that σ(n)=2n exceeds all σ(1),...,σ(m) and 2m. Then σ(x) and δ(x) both have final 1 at 2n, so \(P_{\sigma,\delta}\) is dense and \(h_\sigma\mathrel A h_\delta\).

Therefore
\[
\boxed{\quad h_{\mathrm{id}}\ A\ h_\sigma\ A\ h_\delta,
\qquad h_{\mathrm{id}}\not A h_\delta.\quad}
\tag{2.2}
\]
This is a genuine Boolean-valued two-step generalized point with one **non-homeomorphism** endpoint. It is not an endpoint-cube separator because it has an honest intermediate witness in the same Boolean locale; this limitation is explicit.

## 3. Relevance to CO-01

All admissible-cover equations for such maps reduce to density of finite-support points whose *image maxima* coincide. This extends the combinatorial search beyond permutations to noninvertible coordinate encodings and finite-to-one block maps, potentially allowing new generalized-point behavior. However, as long as an alleged A² pair is exhibited by an actual A–A path over the same Boolean locale, adjoining a third A-edge automatically gives a four-step lift and **cannot witness failure of** \(\ell:E_4\to S_L\). A future counterexample to associativity needs an intrinsically nonliftable image-factorization generalized point or a directly separating Q₂ endpoint congruence.

**Status:** exact generalized point criterion and explicit noninvertible example internally checked only; cube associativity unresolved.
