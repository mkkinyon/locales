# Project A — endgame literature deep dive: localic associative composition
## 21 November 2026, segment 2 · primary-source comparison and priority cautions

**Companion:** [first literature crosswalk](ProjectA_ENDGAME_LITERATURE_CROSSWALK_2026-11-21.md), [unified spine](ProjectA_ENDGAME_BIG_PICTURE_SPINE_2026-11-21.md), [coherent composition canonical](ProjectA_coherent_composition_canonical_proof_2026-11-08.md), [rectangular canonical](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), [matrix reconciliation](ProjectA_BALANCED_WITNESS_SCATTERED_MATRIX_POSTREFEREE_RECONCILIATION_2026-11-21.md).

**Reading policy:** "DIRECTLY CHECKED" means inspected the original article/preprint (at least the sections specified) in this segment. "EARLIER PROJECT" indicates repository background rather than fresh reading. "NOT LOCATED" means absence in this targeted search, **never** a novelty/priority finding. Distinguish **sublocale relations in Loc**, **closed relations in CHLoc**, **spectral distributors** and **relations between frame elements**; they are not interchangeable.

## 1. General categorical relation calculus and its failure in Loc

- A. Klein, *Relations in Categories*, *Illinois J. Math.* 14 (1970), 536–550. Reflected explicitly in Nesta van der Schaaf, *Localic Relations with Open Cones*, arXiv:2605.04038v2 (2 Sept 2026), §12.2, https://arxiv.org/abs/2605.04038. The general failure of associative pullback/image composition in Loc, associated with pullback non-stability of epis/images, is **known**. Do not claim discovery.
- Standard **regular-category/allegory** apparatus gives associative composition for internal relations whenever images are pullback stable. Our issue is that the ambient category of *all locales and all sublocale inclusions* lacks that exactness.
- An individual source and target locale being compact Hausdorff does *not* mean arbitrary sublocales R↪X×Y are subobjects of the **category CHLoc**; the latter are exactly its **closed** sublocales. Thus the CHLoc regularity theorem does not make every relation in Sub_Loc(X×Y) associative.

## 2. Townsend, 1996: an essential close predecessor

**Christopher Townsend**, *Preframe Techniques in Constructive Locale Theory*, PhD thesis, Imperial College London (1996), original accessible on Steven Vickers's page: https://sjvickers.github.io/townsend.pdf; https://sjvickers.github.io/cftpage.html. **DIRECTLY CHECKED:** Chapter 4, especially §4.2, Theorem **4.2.1**, plus thesis abstract.

The thesis explicitly constructs \(\mathrm{REL}(\mathrm{KHausLoc})\) via the **genuine pullback/image operation for closed sublocale relations** between compact regular/Hausdorff locales; proves a **preframe formula** for such relation composites by complementing an open calculated using a preframe trihomomorphism; and connects closed relations with preframe homomorphisms. The follow-up brief text *Hausdorff Systems* (https://www.christophertownsend.org/Documents/HausdorffSystems.pdf), Lemma **1.3**, says closed sublocales of X×Y for compact Hausdorff X,Y correspond to preframe homomorphisms, composition corresponding to function composition. **Known, constructive, before this project.**

**Exact project comparison:** the **closed-entry base algebra** used in our locally finite matrix theorem is an application of this known calculus. Our more complex \(p(A,B)=[A\times B]\) and \(q(A,B)=[A]\times_{\rm Loc}[B]\) may be nonclosed and q may be nonspatial; the rectangle-saturation rule RC is not a statement about arbitrary *closed* CHLoc subobjects. The distinction is essential. This source may also allow a simpler conceptual proof of compact Hausdorff **closed** relation examples; investigate whether the p/q algebra has a preframe operator model, but **no such reduction is established**.

## 3. Modern regularity and exactness sources

**Panagis Karazeris and Konstantinos Tsamis**, *Regular and Effective Regular Categories of Locales*, arXiv:2004.04404 (2020), https://arxiv.org/abs/2004.04404, published *Cahiers de topologie et géométrie différentielle catégoriques* LXII-3 (2021), https://cahierstgdc.com/wp-content/uploads/2021/07/Karazeris-Tsamis_LXII-3.pdf. Checked title/abstract and reference information; **compact regular locales form a Barr-exact category**. This provides a direct earlier categorical foundation for Townsend's compact Hausdorff closed-relation associativity.

**Célia Borlido, Panagis Karazeris, Luca Reggio, Konstantinos Tsamis**, *Filtral Pretoposes and Compact Hausdorff Locales*, *Theory and Applications of Categories* 41 (2024), no. 41, 1439–1475 (10 Oct 2024), https://www.tac.mta.ca/tac/volumes/41/41/41-41abs.html and author preprint https://www.mat.uc.pt/preprints/ps/p2330.pdf. **DIRECTLY CHECKED** §§2.1–2.2: CHLoc is a pretopos, regular epis are localic surjections (Lemma 2.3), and categorical subobjects of a compact Hausdorff locale identify with its **closed** sublocales (Example 2.7). This makes the boundary between CHLoc closed relations and arbitrary Loc sublocales categorical rather than merely pointwise.

## 4. Classical/topological relational categories on spectral and stably compact spaces

**Achim Jung, Mathias Kegelmann, M. Andrew Moshier**, *Stably Compact Spaces and Closed Relations*, *Electronic Notes in Theoretical Computer Science* 45 (2001), 209–231; original https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf. **DIRECTLY CHECKED** §2.2 and Propositions 2.9–2.10. Defines closed relation \(R\subseteq X\times Y_\kappa\) and **ordinary set-relational composition**, categorically equivalent to a compact-set/Vietoris Kleisli construction. For compact Hausdorff X,Y this becomes the familiar closed subsets of X×Y, composition associative. On general stably compact spaces, the **identity relation is specialization**, not necessarily Δ as a set; converse reverses the cocompact order, not necessarily an endofunctor. This makes important distinctions from our reflexive symmetric localic subrelations.

**Dirk Hofmann and Pedro Nora**, *Dualities for Modal Algebras from the Point of View of Triples* (2014 manuscript), https://sweet.ua.pt/dirk/artigos/2015/dualmodalg_revised.pdf. **DIRECTLY CHECKED** introduction and §3–4 around formula \(\mathrm{SpecRel}\simeq\mathrm{DLat}^{op}_{\bot,\vee}\). An associative spectral-relations category appears as a Vietoris **Kleisli** category, with StoneRel a subcategory. These relations satisfy a specific Vietoris/spectral structure; they are not automatically arbitrary patch-closed *localic subobjects*. Do not conflate use of the word "spectral" with the theorem from our repo.

**Hofmann–Nora**, *Esakia Spaces via Idempotent Split Completion*, manuscript July 2015, https://sweet.ua.pt/dirk/artigos/2014/esakia_revised2.pdf. **DIRECTLY CHECKED** introduction and §2 (p. 5 onward). Further identifies **StCompDist** of stably compact spaces and spectral distributors, where identity is the underlying order, and composition arises from lower Vietoris/Kleisli. In the compact Hausdorff case the underlying order is equality, and the full subcategory is CompHausRel. Again a known, structured associative relation category.

**Max Dickmann, Niels Schwartz, Marcus Tressl**, *Spectral Spaces*, Cambridge UP 2019, notably §6.3 *Spectral Orders and Spectral Relations*, Corollary **6.3.9** and §6.3.12; publisher TOC https://assets.cambridge.org/97811071/46723/frontmatter/9781107146723_frontmatter.pdf and book citation DOI 10.1017/9781316543870. **SOURCE-EXTRACT CHECKED** of §6.3 via available excerpts, not complete publisher chapter rereading. A proconstructible subset \(R\subseteq X\times Y\) of spectral spaces supplies a *spectral order* on a topological disjoint union; iterative spectral-relation constructions are explicitly studied. This is a **very close topological/graph antecedent** to the use of patch-closed binary relations and comparative spectral orders, but does not itself assert equality between actual \(\mathbf{Loc}\) pullback/image of arbitrary proconstructible spectral sublocales and pointwise relation products.

**Additional source for follow-up**: *Topological Duality for Distributive Lattices: Theory and Applications* (Cambridge University Press, 2023), §6.4, "Duality for Spaces of Relations and Functions"; source extract https://doi.org/10.1017/9781009349680.007 . It describes free modal layers and binary relation spaces; could clarify the graph-algebra connection, but has not been fully read or priority-matched.

**Additional contemporary closed-relation dualities:** Marco Abbadini, Guram Bezhanishvili, Luca Carai, *Vietoris Endofunctor for Closed Relations and Its de Vries Dual*, *Topology Proceedings* 64 (2024), 213–250, preprint arXiv:2308.16823; and *MacNeille Completions of Subordination Algebras*, arXiv:2211.02974. These extend closed-relation calculus on compact Hausdorff spaces to subordination/de Vries representations. The abstracts have been checked; full priority comparison is pending.

## 5. Exact comparison with the project coherent-proconstructible theorem

Project authority: [coherent composition canonical §0–4](ProjectA_coherent_composition_canonical_proof_2026-11-08.md). Our **Theorem A** characterizes sublocales induced by patch-closed spectral subspaces via compact-preserving surjective frame maps / quotient of the compact-open lattice. Our **Theorem B** says **within that class** the actual **Loc** composite agrees with *ordinary* point-relation composition, is again proconstructible spectral, and associates. Proof forms actual pullback, shows resulting sublocale remains proconstructible spectral, then proves localic image via spectral surjection onto its patch-closed point image. Our hull theorem uses the actual \(\mathcal A\) presentation to obtain compositions describing closure/fitting.

This is mathematically close to known image preservation of patch-closed sets by spectral maps, to Priestley duality, and to structured spectral-relations categories. **However**:
- Not every proconstructible relation is necessarily a Hofmann–Nora spectral distributor; check order-saturation hypotheses.
- Our category has **all** proconstructible spectral sublocales as morphisms in the permitted product, rather than only closed *patch* relations equipped with a spectral-distributor property.
- Equality of point sets does **not** identify arbitrary sublocales; Theorem B relies on the compact preserving frame quotient and full localic pullback/image.
- **Priority of the exact localic Theorem B remains unresolved.** It may well be an easy categorical reformulation of existing spectral compactness/regularity; explicitly test this before asserting novelty.

In any publication: cite Townsend 1996, Karazeris–Tsamis 2021, Borlido et al. 2024, Jung–Kegelmann–Moshier 2001, Hofmann–Nora, Dickmann–Schwartz–Tressl before making any comparison claims.

## 6. Exact comparison with the rectangular and scattered-index papers

Project RC on compact Hausdorff G: for independently chosen \(r,s\in\{p,q\}\), the genuine image/pullback composite of \(r(A,B)\) and \(s(C,D)\) is \(q(A,D)\) iff \([B]\wedge[C]\ne0\), otherwise zero; all sublocale overlaps genuine. This is a **nonclosed, possibly nonspatial** relation computation and hence *not* subsumed merely by known CHLoc closed relation associativity. **No exact predecessor located in this targeted search.** Could be formal consequence of known dense/spatial-sublocale machinery; priority still open.

Project MAT and MUL: for compact scattered Hausdorff K and compact Hausdorff P, all sublocales of \(P^n\times K^n\) are exactly indexed families of **arbitrary** sublocales of \(P^n\), yielding the **full genuine binary** matrix formula \((R\circ S)_{ik}=\bigvee_j(R_{ij}\circ_P S_{jk})\). Classical scatteredness/point-determination itself is already Simmons/Picado–Pultr, but the parameterized reconstruction and its localic-image compatibility are separately externally audited. **No exact predecessor found** in the current search; do not treat this as a finding of novelty. The locally finite matrix algebra is an algebraic **consequence** of MAT/MUL plus known associative base properties, and the referee's discrete-index comparison is another such consequence. In presentation, emphasize mathematical *mechanism* over unsupported originality.

## 7. Suggested endgame publication triage, revised

1. **Best likely standalone spine:** how to go beyond established closed/spectral relation categories and still recover associativity for genuinely nonclosed (sometimes nonspatial) sublocales: p/q rectangular saturation, balanced witness actions, scattered-index matrices. This is a candidate paper *conditional on sources and author proof checks*.
2. **Coherent hierarchy paper:** the conceptual graph-to-diagonal identification, genuine localic hulls, equality/counterexamples, with coherent relational calculations; keep clear that most building blocks are established separation and Priestley/spectral theory. Possible research or research-expository paper, exact priority pending.
3. **Higher Dowker branch:** independent potential paper, but deserves distinct source scan and a more focused statement before manuscript planning.

Do not issue an originality verdict for any of these during the endgame without exhaustive mathematical-literature comparison.

## 8. Next source checks

- Read Hofmann–Nora's exact conditions for spectral distributors and test the project \(\mathcal A,\mathcal I,\mathcal D\) examples to distinguish classes formally.
- Search specialized sublocale/relations papers for a \(p/q\)-type rectangular formula or a parameterized scattered-index statement; do not rely on absence of keyword hits.
- Check whether the project's coherent Theorem B is a corollary of a *regular category of coherent locales* versus only a restricted associative subalgebra inside Loc.
- Compare modern subordination/de Vries literature on closed relations; it could suggest a short conceptual proof for the closed-entry base case.
- Refine exact bibliography (journal status/DOIs) and later split inherited source theorems from project deductions in the final theorem ledger.

No priority claim is made here.
