# CO-01 coordinate-injection Boolean maps: full two-step connectivity, explicit lifts

**11 November 2026. New internally checked Baire-category extension of audit VIII's coordinate-permutation theorem, NOT a cube associativity verdict.** Complements [noninvertible doubling probe](ProjectA_CO01_continuous_endomorphism_Boolean_test_2026-11-11.md) and [graph-density obstruction](ProjectA_CO01_graph_probes_strict_and_doubling_jump_2026-11-11.md).

For any injection \(\lambda:\mathbb N\hookrightarrow\mathbb N\), define its Cantor coordinate-embedding
\[
(F_\lambda x)_{\lambda(n)}=x_n,\qquad
(F_\lambda x)_j=0\ \ (j\notin\lambda(\mathbb N)).
\]
It is continuous and maps D→D, V→V (finite nonzero support remains finite nonzero, infinite remains infinite, zero remains zero). Let \(h_\lambda=q\circ F_\lambda^*:\mathcal O(V)\to B=\mathrm{RO}(V)\).

**Lemma.** If injections \(\lambda,\kappa\) agree on an infinite set \(J\subseteq\mathbb N\), then \(h_\lambda A h_\kappa\).

**Proof.** In every prescribed finite input cylinder with prefix length m, choose n∈J larger than m and such that \(\lambda(n)=\kappa(n)\) exceeds the finitely many values of \(\lambda,\kappa\) on \(\{1,\ldots,m\}\); this is possible because the injections take arbitrarily large values on any infinite J. Choose a finite support realizing the prefix, add a 1 at n and leave the remaining coordinates zero. Then the two images have the same maximal 1-coordinate \(\lambda(n)=\kappa(n)\), hence the same K_{\lambda(n)}. Such points occur in every cylinder, so the exact continuous-map criterion \(P_{\lambda,\kappa}\) dense applies.

**Theorem.** For arbitrary two injections \(\lambda,\kappa:\mathbb N\hookrightarrow\mathbb N\), there is a **permutation** \(\sigma\in\mathrm{Sym}(\mathbb N)\) agreeing with each on infinitely many indices. Consequently
\[
\boxed{\quad h_\lambda\ A\ h_\sigma\ A\ h_\kappa
\quad\text{for every pair of coordinate injections }\lambda,\kappa.\quad}
\tag{1}
\]

**Proof.** In the Polish Baire space \(\mathrm{Sym}(\mathbb N)\), for fixed injection λ and each m put
\[
U_m(\lambda)=\bigcup_{n\ge m}\{\sigma:\sigma(n)=\lambda(n)\}.
\]
It is open and dense: any finite partial bijection p admits extension by n↦λ(n) with n≥m outside dom(p) and λ(n) outside ran(p), because λ is injective and unbounded on every cofinite set. Thus \(\bigcap_m U_m(\lambda)\) is dense Gδ. Intersect with the corresponding dense Gδ for κ and use Baire. The lemma supplies the two A-edges. QED.

**Consequences for CO-01.** Any Boolean-valued triple \((h_\lambda,h_\kappa,h_\eta)\) of coordinate-injection maps that factors through \(S_L=(A²)_{12}\cap A_{23}\) lifts along the honest four-path comparison \(\ell:E_4\to S_L\): use hσ from (1) to fill the first A² segment and preserve the given last A-edge hκ A hη. Thus **the entire coordinate-injection family is also incapable of witnessing failure of the special source comparison \(\ell\)**, strengthening the earlier permutation-only no-go statement. This still does not address *all* continuous Cantor maps (which may collapse coordinates or be nonlinear), or arbitrary nonspatial generalized points of A².

Status: internally checked Baire argument; no external audit and no conclusion on cube associativity.
