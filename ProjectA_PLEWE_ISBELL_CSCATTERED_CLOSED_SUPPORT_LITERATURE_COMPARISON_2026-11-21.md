> **SUPERSEDED EVIDENCE STATUS, 21 NOV:** The complete 37-page journal PDF was subsequently supplied and read directly; [full primary-source report](ProjectA_PLEWE_1996_FULL_PRIMARY_SOURCE_COMPARISON_2026-11-21.md) now supersedes all “abstract only / complete paper inaccessible” limitations below. In particular, Plewe Theorem 3.2 *explicitly uses a compact closed support with dense coordinate traces*, and Theorems 2.2/2.6 give the **Q-test for all metrizable**, not just separable, factors. This document is retained as an earlier preliminary reading.

# Project A — Plewe 1996, Isbell 1981, and the closed-support (G′) product criterion
## Session 11 first literature comparison · 21 November 2026

**STATUS / EVIDENCE LIMIT:** Primary **published abstract** of Till Plewe, *Localic Products of Spaces*, *Proc. London Math. Soc.* (3) **73** (1996), 642–678, DOI https://doi.org/10.1112/plms/s3-73.3.642, has been directly inspected at https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/s3-73.3.642 . The publisher's downloadable full paper redirected to its abstract and the complete original 37-page article **could not be accessed** during this segment. An extensive explanatory secondary source is J. Goubault-Larrecq, *Localic products and Till Plewe's game*, https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=6400, which reproduces the game and gives detailed proofs for its relation to the tensor product of frames. Isbell (1981) was checked via its published abstract/metadata and a recent mathematics discussion citing Theorem 4, *not* via the original full 3-page text. **Do not claim an exhaustive theorem-by-theorem or proof-by-proof review of either inaccessible full primary article.**

## 1. Exact primary-abstract statements of Plewe relevant to Project A

For **metrizable** spaces \(A,B\), Plewe's abstract states:
\[
[A]\times_{\rm Loc}[B]\text{ nonspatial}
\iff
\begin{gathered}
\text{there exist closed subspaces }A'\subseteq A,\ B'\subseteq B\\
\text{which can be embedded in Cantor space as}\\
\text{two disjoint dense subspaces}.
\end{gathered}\tag{P-Cantor}
\]
The term "closed" here is **closed in the respective factors**, not necessarily closed in arbitrary ambient compactifications. The existence of the two embeddings is a substantial geometric assertion. This theorem is already in print (1996), so our related Cantor-graph witness cannot be presented as a new characterization of nonspatial metrizable products.

For a **metrizable** \(A\), the abstract also states that \(A\) is a **spatial multiplier**—\([A]\times_{\rm Loc}[Y]\) is spatial for every spatial factor \(Y\)—iff \(A\) is *complete* (topologically completely metrizable) and has **no closed subspace homeomorphic to the irrationals** \(\mathbb N^{\mathbb N}\):
\[
\operatorname{Multiplier}(A)\iff
A\text{ completely metrizable and contains no closed }\mathbb N^{\mathbb N}.
\tag{P-Mult}
\]
It cites Hurewicz's characterization of **strongly Baire** spaces (all nonempty closed subspaces Baire, or equivalently no closed copy of \(\mathbb Q\)) and records: any factor **not** strongly Baire has a spatial product only with spatial multipliers. Consequently, since \(\mathbb Q\) is not strongly Baire,
\[
[A]\times_{\rm Loc}[\mathbb Q]\text{ spatial}
\iff \operatorname{Multiplier}(A)
\quad\text{for every metrizable }A.
\tag{P-Q}
\]
Sufficiency is the definition of spatial multiplier; necessity is Plewe's published implication. **Thus \(\mathbb Q\) as a universal test factor is already a consequence of Plewe 1996**, independently of the project's derivation using (G′).

For a **separable metrizable** \(A\), Hurewicz's classical theorem says a Polish space is \(\sigma\)-compact iff it contains no closed \(\mathbb N^{\mathbb N}\). Hence:
\[
[A]\times_{\rm Loc}[\mathbb Q]\text{ spatial}
\iff A\text{ is }\sigma\text{-compact Polish}.
\tag{P-Q-sep}
\]
This is a consequence of *published* statements plus classical Hurewicz theory, not a claim that Plewe uses exactly this wording.

The abstract also announces: a game-theoretic criterion for arbitrary products; spatiality of a complete factor times a strongly Baire metrizable factor; a Galois connection between factor classes induced by pairwise product spatiality; and a theorem on metrizable locales Borel in every completion. These are outside the present narrow comparison.

## 2. Earlier Isbell 1981 antecedent

John R. Isbell, *Product spaces in locales*, *Proc. Amer. Math. Soc.* **81** (1981), 116–118, DOI https://doi.org/10.1090/S0002-9939-1981-0589150-5, predates Plewe. Its accessible published abstract states that localic products of sober spaces agree with ordinary products when a factor is quasi-locally compact, and gives a universal criterion for completely regular \(A\) in terms of being a **complemented sublocale of a compact space**. A recent discussion, https://mathoverflow.net/questions/516361/when-does-omegax-otimes-omegay-omegax-times-y-hold-for-every-y/516370, reports that Isbell Theorem 4 gives the sufficient condition that every nonempty closed subspace has a point with a quasi-locally-compact neighborhood, and the converse when completely regular; for Hausdorff spaces this is the ordinary hereditary-somewhere-locally-compact condition. The theorem-number attribution is **secondary evidence pending access to the original paper**.

This corresponds to **\(C\)-scatteredness**, due to Telgársky: every nonempty closed subspace contains a point with a compact neighborhood. For definitions see *Topology Proceedings* 27, https://topology.nipissingu.ca/tp/reprints/v27/tp27125.pdf . Consequently, the universal sufficiency result proposed in Claude Opus's addendum has significant classical antecedents, and its mathematical value is a **new derivation from Project A's (G′)** rather than a novel product-spatiality criterion.

## 3. Direct small topological consequence: C-scattered = sigma-compact Polish (separable metric)

**Proposition (classical consequences, independently elementary/descriptive-set-theoretically checked).**
For a **separable metrizable** space \(A\),
\[
A\text{ \(C\)-scattered}\iff A\text{ \(\sigma\)-compact and Polish}.
\tag{C=Ksigma-Polish}
\]

**Proof:** If \(A\) is \(\sigma\)-compact Polish, every nonempty closed \(F\subseteq A\) is again Polish and \(\sigma\)-compact, hence Baire. Write \(F\) as countably many compact closed sets; one has nonempty interior in \(F\), giving a compact neighborhood in \(F\).

Conversely suppose \(A\) is \(C\)-scattered. Perform its transfinite \(C\)-scattered derivative: start with \(F_0=A\), let \(F_{\alpha+1}\) be the closed residual after removing all points of \(F_\alpha\) with compact \(F_\alpha\)-neighborhoods, and intersect at limits. \(C\)-scatteredness makes the derivative empty. Because \(A\) is second-countable, there are only **countably many strict successor drops** (each drop consumes a previously unconsumed basic open set); hence the derivative stops at a countable ordinal. Each removed relatively open locally compact stratum is a union of **countably many compact subsets** (Lindelöfness), and all these compact sets are compact in \(A\). Thus \(A\) is \(\sigma\)-compact.

Moreover every nonempty open part of any nonempty closed \(F\subseteq A\) contains a nonempty **locally compact open patch**: apply \(C\)-scatteredness to the closure of that open part in \(F\), then intersect the compact-neighborhood patch with the original open part. Since such patches are Baire, each closed \(F\) is Baire. Thus \(A\) is **completely Baire**. Embed \(A\) in its separable complete metric completion \(M\). Because \(A\) is \(\sigma\)-compact, it is \(F_\sigma\) in \(M\), hence coanalytic. By Hurewicz's theorem, a coanalytic completely Baire metrizable subspace of a Polish space is Polish. \(\square\)

This is not offered as an original theorem; see Gruenhage–Tamano, *If X is \(\sigma\)-compact Polish, then \(C_k(X)\) has a \(\sigma\)-closure-preserving base*, https://webhome.auburn.edu/~gruengf/papers/cksig.pdf for the **forward** observation and \(C\)-scattered derivative terminology, and Hurewicz expositions such as https://arxiv.org/abs/1405.7899 for the coanalytic completely-Baire/Polish step.

Combining (P-Q-sep), the proposition, and the Opus addendum's separately internally checked argument recovers the latter's characterization:
\[
[A]\times_{\rm Loc}[\mathbb Q]\text{ spatial}\iff A\text{ \(C\)-scattered}
\quad\text{for separable metrizable }A,
\]
but it is now clearly **a classical consequence of Plewe**, with an alternative proof mechanism through (G′).

## 4. Exactly what (G′) contributes conceptually

The independently checked [compact Hausdorff rectangular/closed-support canonical theorem](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) establishes, for compact Hausdorff ambient spaces \(X,Z\) and *arbitrary* subsets \(A\subseteq X,\ D\subseteq Z\):
\[
[A]_X\times_{\rm Loc}[D]_Z
=\bigvee_{\substack{\varnothing\ne K\subseteq X\times Z\text{ closed}\\
K\cap(A\times Z),\,K\cap(X\times D)\text{ dense in }K}}
\mathcal B(K).
\tag{G′}
\]
Here \(\mathcal B(K)\) is the least dense (Booleanization) sublocale of the compact support \(K\). This is a formula for the **whole full localic product as a sublocale**, not merely a yes/no criterion for spatiality. The [weak/full criterion](ProjectA_OPUS_RECTANGLE_OVERLAP_REES_ETALE_OBSERVATIONS_2026-11-21.md) then gives
\[
[A]\times_{\rm Loc}[D]=[A\times D]
\iff
\text{every qualifying }K\text{ also has }K\cap(A\times D)\text{ dense}.
\tag{G′-spatiality}
\]
It does **not** require metrizability. The first formula is a mathematical part of our independently audited RC/closed-support package; the displayed weak=full corollary was proposed subsequently by Opus and internally checked conditional on (G′), not separately blind certified.

**Scope comparison:**
- Plewe's (P-Cantor) replaces arbitrary compact closed-support obstructions by the particularly vivid **Cantor-disjoint-dense embedding criterion**, under **metrizability**. His theorem is a definitive earlier characterization of **spatiality**.
- Our (G′) is a **full sublocale generation theorem**, for arbitrary compact Hausdorff ambients and arbitrary subsets, with potentially nonspatial Booleanizations as generators. It is useful not only for spatiality but as the central ingredient of actual localic p/q **rectangular composition** (RC).
- Neither the journal abstract nor the secondary game exposition settles whether **this exact representation (G′)** occurs, perhaps disguised, in Plewe's full article or in earlier Isbell/Johnstone–Sun work. Do **not** assert novelty of the formula without reading these primary texts.
- The **Cantor graph \(K=\Gamma_h\)** in the Opus addendum is a particular *bad closed support*; Plewe's criterion is an existence theorem for two *closed factor subspaces* admitting disjoint dense embeddings in Cantor space. It is **not** legitimate, without a proof, to treat the two constructions as word-for-word identical.
- Distinguish \(p(A,D)=[A\times D]\) (point-generated weak product) from \(q(A,D)=[A]\times_{\rm Loc}[D]\) (full localic product), as in Johnstone–Sun 1988. Our **mixed rectangular composition** theorems require additional localic image/pullback work and are not consequences of Plewe's spatiality criterion alone.

## 5. Plewe's game: an alternative frame-level perspective

The accessible Goubault-Larrecq exposition presents Plewe's strictly determined game for a cover \(\mathcal U\) of \(U_0\times V_0\) by open rectangles. I chooses points in shrinking coordinate opens; II replies with smaller open neighborhoods. II wins as soon as its product neighborhood lies inside one of the specified cover rectangles; otherwise I wins along an infinite play. Plewe's theorem characterizes preservation of the product by the embedding of spaces in locales in terms of winning strategies (the explanatory source also proves an explicit comparison via **C-ideals/Galois connections** between frames). See https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=6400 .

This is complementary to (G′): game/rectangle-cover failure witnesses a **frame coproduct** defect, while a bad closed support witnesses a **nonspatial full product sublocale** through Booleanization. The explicit equivalence between those *individual witness formats* has **not** been worked out in the present project. One might study it for pedagogical value, but it is not necessary for the November 25 consolidation.

## 6. Disposition

1. **Historical novelty disclaimed** for universal \(C\)-scattered sufficiency, the Cantor characterization, spatial multipliers, the \(\mathbb Q\)-factor test, and the associated Polish/\(\sigma\)-compact implications.
2. **Distinct project technique retained:** (G′) gives an explicit ambient Booleanization support decomposition useful for the mixed p/q rectangular image-composition calculus; we have not established whether its *exact statement* is present in earlier literature.
3. The product-spatiality lemmas from the Opus addendum should be presented as **rederivations/applications of classical theory**, not among the project's independent headline results.
4. **Uncompleted primary-literature obligation:** obtain Plewe's *full article* and Isbell's three-page 1981 article for exact section/theorem and proof comparisons. Publisher abstracts and the Goubault-Larrecq expository proof are sufficient for this initial evidence-based comparison but not for an exhaustive priority audit.
5. This is an appropriate stopping point for the immediate literature question. Unless full articles become available, move next to the **final conceptual synthesis** rather than spending several research segments reconstructing published theory from abstracts.
