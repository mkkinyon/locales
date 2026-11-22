# Project A — Plewe, *Localic Products of Spaces* (1996): full primary-source comparison
## Session 11 · 21 November 2026 · revised after user supplied the complete journal PDF

**PRIMARY SOURCE READ DIRECTLY:** Till Plewe, “Localic Products of Spaces,” *Proceedings of the London Mathematical Society* (3) **73** (1996), 642–678, DOI https://doi.org/10.1112/plms/s3-73.3.642, full 37-page journal PDF supplied by the project owner in Session 11. The paper's publisher footer records download on **16 November 2026**, consistent with the owner's recollection that it had been uploaded in an earlier session. **The copyrighted journal PDF is not committed to the public repository.** Page numbers below are the *printed* journal pages, not PDF page indices; e.g., printed p.654 is PDF page 13.

This source-based note **supersedes the earlier, abstract-only** [Plewe/Isbell preliminary comparison](ProjectA_PLEWE_ISBELL_CSCATTERED_CLOSED_SUPPORT_LITERATURE_COMPARISON_2026-11-21.md). That earlier note accurately identifies major statements but no longer accurately describes source availability. Related original project files: [full closed-support \(G'\) / mixed RC proof](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), [Opus product-spatiality addendum reconciliation](ProjectA_OPUS_ADDENDUM_SPATIALITY_WINDOW_RECONCILIATION_2026-11-21.md), [weak/full overlap observations](ProjectA_OPUS_RECTANGLE_OVERLAP_REES_ETALE_OBSERVATIONS_2026-11-21.md).

## 1. The exact classical antecedents are now directly confirmed

### Isbell's universal spatial-multiplier criterion — Plewe Theorem 1.6, p.649 (PDF p.8)

Plewe explicitly restates Isbell's theorem for completely regular \(X\), making equivalent:
1. \(X\times_{\rm Loc}Y\) spatial for every sober \(Y\);
2. **every nonempty closed subspace of \(X\) contains a point with a locally compact neighborhood**;
3. \(X\) complemented in its Stone–Čech compactification.

The second property is the **\(C\)-scattered / hereditary-somewhere-locally-compact** criterion independently rediscovered by Claude Opus in our project. Its sufficiency was **not discovered here**. Plewe's introduction p.642 already credits Isbell before proving the theorem again by the game method. Its proof also invokes the diagonal pullback and nonzero pointless sublocale of a product of disjoint sublocales (p.649), strikingly close to Project A's broader technique.

### Metric classification — Plewe Theorem 2.2, pp.650–651 (PDF pp.9–10)

For any metrizable \(X\), Plewe gives **seven equivalent conditions** (not just the two in the abstract). Among them:
- spatial multiplier for arbitrary sober factors;
- every nonempty closed subspace has a locally compact point;
- spatial multiplier for all **metrizable** factors;
- complete metrizability and **no closed copy of the irrationals \(\mathbb R\setminus\mathbb Q\)**.

The proofs use Lemma 2.1, a closed Baire-space construction inside a completely metrizable nowhere-locally-compact subspace. This is far stronger and more precise than the initial abstract-based inference.

### The \(\mathbb Q\)-test and non-strongly-Baire factors — Plewe Theorem 2.6, p.652 (PDF p.11)

Plewe proves: for metrizable \(X,Y\), when \(X\) is **not strongly Baire**, \(X\times_{\rm Loc}Y\) is spatial **iff** \(Y\) is a spatial multiplier. Since \(\mathbb Q\) is not strongly Baire, taking \(X=\mathbb Q\) gives, for **any metrizable \(A\)**, even **nonseparable**:
\[
\boxed{A\times_{\rm Loc}\mathbb Q\ \text{spatial}
\iff A\ \text{is a spatial multiplier}
\iff A\ \text{is \(C\)-scattered}.}\tag{P-Q}
\]
The last equivalence is from Theorem 2.2. Thus the project Opus “one-factor rational test,” earlier stated for *separable* metrizable \(A\), is a **special case** of an explicit 1996 theorem (combined with Theorem 2.2); the full classical result does not require separability.

For **separable** metrizable \(A\), the above is equivalent to **\(\sigma\)-compact Polish**, via the Hurewicz characterization of completely metrizable spaces without closed Baire-space copies. **Do not extend the \(\sigma\)-compact characterization to all metrizable \(A\)**: an uncountable discrete metric space is a spatial multiplier but not \(\sigma\)-compact.

Related direct corollaries: Plewe Corollary 2.8, p.653, says complete \(\times\) strongly Baire is spatial and strongly Baire; Corollary 2.9, p.653, says \((\mathbb R\setminus\mathbb Q)\times_{\rm Loc}A\) spatial iff \(A\) strongly Baire. The former recovers the project observation about two Čech-complete metric factors, with broader known antecedent noted in the paper.

## 2. The crucial exact link to our \(G'\): Plewe Theorem 3.2, pp.654–655

Plewe's Theorem 3.2 concerns **finite products of metrizable spaces** and says they are nonspatial **iff** their factors contain closed subspaces \(F_i\) with dense embeddings \(F_i\hookrightarrow C\), the Cantor set, such that the embedded images have **empty common intersection**. For two factors the images are disjoint and dense. (This is Theorem 3.2's exact finite-factor formulation, beyond the abstract's binary version.)

The **necessity proof is directly methodologically ancestral** to the compact closed-support techniques of Project A. Plewe:
1. Reduces to separable closed subspaces via Corollary 1.5, and embeds factors into **compact metrizable completions** \(X_i\).
2. Chooses a **nonzero closed pointless sublocale** \(P\) inside the nonspatial full product; sets \(K=\operatorname{cl}_{\prod X_i}(P)\). This \(K\) is **perfect** and compact, and carries no points of the ordinary factorwise product.
3. Defines the coordinate traces
   \[
   D_i=K\cap (X_1\times\cdots\times A_i\times\cdots\times X_n)
   \]
   and proves **each \(D_i\) is dense in \(K\)** via the inclusion of the least dense sublocale \(D(K)\) in the restricted full localic product.
4. Applies Lemma 3.1 to find a **diagonally placed Cantor subset** of \(K\) with dense coordinate traces and injective projections. This yields the required closed factor subspaces and dense embeddings in Cantor space.

The **form of step (3)** is strikingly similar to the key hypothesis in our closed-support family \(\mathscr K(A,D)\). In particular, **Plewe already uses an arbitrary compact closed support with dense coordinate traces to detect nonspatiality; this is an explicit published antecedent**, not merely a guess inferred from the abstract.

The companion Theorem 3.3 (p.655) gives the analogous criterion for failure of strong Baireness, with the intersection homeomorphic to \(\mathbb Q\); Theorem 3.7 (p.656) constructs strongly Baire factors whose **ordinary** product is strongly Baire but whose **localic** product is nonspatial. These are genuine further refinements beyond our Opus observations.

## 3. What \(G'\) does (and does not) add

For compact Hausdorff **ambient** spaces \(X,Z\), with arbitrary subsets \(A\subseteq X\), \(D\subseteq Z\), Project A's independently checked theorem is the **whole-sublocale decomposition**
\[
\boxed{
[A]_X\times_{\rm Loc}[D]_Z
=\bigvee_{\substack{\varnothing\ne K\subseteq X\times Z\text{ closed}\\
K\cap(A\times Z),\,K\cap(X\times D)\text{ dense in }K}}
\mathcal B(K).
}\tag{G'}
\]
\(\mathcal B(K)\) denotes the **least dense/Booleanization sublocale** of \(K\). This includes arbitrary *possibly nonmetrizable* compact Hausdorff ambients and is an equality of actual **sublocales**, not a predicate saying whether the product is spatial.

**Stronger as a formulated statement** than Plewe's particular \(\Leftrightarrow\) spatiality test: it reconstructs \(q(A,D)\) itself, and it has a central *additional use in Project A*—the proof of the mixed p/q **actual relational-composition rule**. Plewe's Theorem 3.2 does not state (G') as a join over all qualifying supports or give that mixed relational-composition rule.

**Weaker as evidence of independent novelty** than previously suggested: Plewe's proof contains essentially the support/density extraction itself and invokes the smallest dense sublocale. We should not claim that “closed-support methods,” “Cantor graph bad supports,” “diagonal pullback of pointless intersections,” or C-scattered/product-spatiality criteria originate in Project A. Nor does the present reading prove (G') has no exact predecessor elsewhere; a negative historical claim about all prior literature would require a separate systematic check.

The later [Opus weak=full criterion](ProjectA_OPUS_RECTANGLE_OVERLAP_REES_ETALE_OBSERVATIONS_2026-11-21.md) follows from (G') and is best viewed as an explicit localic-support reformulation of **classical product-spatiality theory**, not advertised as a new classification:
\[
[A]\times_{\rm Loc}[D]=[A\times D]\iff
\text{each qualifying }K\text{ has }K\cap(A\times D)\text{ dense}.
\]
This formalism may still be pedagogically useful and makes the passage to relation composition particularly transparent.

## 4. Further interesting direct connections

**Plewe's Theorems 1.1–1.2, pp.645–646.** A topological **strictly determined game** characterizes spatiality of arbitrary binary/family products of sober spaces. His §3 compact closed-support obstruction can be reached either through the proof using Lemma 3.1 or via the alternate **winning-strategy/tree** proof in the Appendix, pp.672–677. This makes a direct bridge between point-free product obstructions, finite/infinite rectangle covers and combinatorial trees—but these are game/strategy trees, **not** Project A's depth-n separation trees \(\mathcal V_n\).

**Countable products.** Section 8 (pp.671–672) explicitly distinguishes finite-product characterizations from open questions, *as of 1996*, about countable powers of noncomplete spaces; do not report them as currently open without a contemporary literature check.

**Finite vs infinite join distributivity.** Lemma 6.3, p.665, warns explicitly that for arbitrary locales,
\[
(\bigvee_i L_i)\times_{\rm Loc}M
\quad\text{can strictly contain}\quad
\bigvee_i(L_i\times_{\rm Loc}M).
\]
This is about **arbitrary infinite** joins. It is entirely consistent with Project A's recently settled **finite** identity
\[
(S\vee T)\times Z=(S\times Z)\vee(T\times Z),
\]
because pullback of sublocales preserves finite joins, but need not preserve infinite joins. Plewe's explicit warning supplies an excellent historical citation for why our matrix-composition proofs avoid an *infinite* interchange.

**Different ranks.** Corollary 5.6 (p.662–663) constructs Bernstein sets whose *localic spatiality power rank* is prescribed at any finite integer and \(\omega\). This is a distinct invariant from our \(\mathcal V\) proof-tree rank and from the composition rank of graph powers; do not conflate them.

**Broader published agenda.** The extensive §4–§5 Galois-closed class and Bernstein-space constructions, §6 approximate \(G_\delta\) locales, and §7 absolutely Borel locales are already a rich classical body of work. We need not reproduce them to consolidate Project A, but they signal how much deeper Plewe went than a short metrizable-product spatiality criterion.

## 5. Disposition for project endgame

1. **Classical antecedents definitively confirmed from full source.** Isbell theorem as reproduced in Plewe 1.6, full metric classification 2.2, exact \(\mathbb Q\)-test 2.6, and closed-support-to-Cantor construction 3.2.
2. **Correct a scope restriction:** the \(\mathbb Q\)-test and \(C\)-scattered equivalence hold for **every metrizable factor**, not just separable ones; only the \(\sigma\)-compact Polish corollary needs separability.
3. **Distinguish contribution:** our \((G')\) is a **full Booleanization-supported sublocale generation formula** and serves actual mixed relation composition; its closed-support method itself is classical in Plewe. Exact originality of the stronger full-join representation remains **undetermined**, not affirmed or denied.
4. **Update historical preliminary note** with a clear supersession banner rather than deleting its previous source-access limitations. The primary journal PDF is held in the conversation attachment, **not** committed to public GitHub.
5. **Next best step:** final conceptual synthesis; no new blind audit necessary merely to rediscover Plewe's established spatiality classifications.
