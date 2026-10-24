# Project A — Targeted literature ledger after the negative answer to Question A

**Search date: 23 October 2026.** Subject: the pointfree relation V=fit(I) where I=C(d_I) is closed inseparability in X×_loc X, and the counterexample to V_fin=V obtained from rank-omega rectangle separation trees. This is **focused due diligence, not an exhaustive literature review or a novelty finding**. Verified public article pages and accessible full HTML/abstracts are distinguished from unexamined book chapters or inaccessible full texts. The mathematical proof itself is in [A-Vfin-negative-consolidated-proof-2026-10-23.md](A-Vfin-negative-consolidated-proof-2026-10-23.md).

## 0. Terminology and direct new-to-old connection

The project calls
  d_I=⋁{u⊠v:u∧v=0} in Q=O(X×_locX),
  I=C(d_I),
  V=fit(I).
The set of bars
  B(I)={w∈Q:w∨d_I=1}
is precisely the **open-neighborhood filter fi(I)** of the CLOSED sublocale I, because
  C(d)⊆O(w) iff d∨w=1.
This is a STANDARD filter-theoretic description, not an invented intrinsic characterization of V. Fitting I is simply
  V=su(B(I))=⋂_{w∈B(I)}O(w).
The distinction from the **actual diagonal** Δ (and its fitted hull D=fit(Δ)) is essential; most F-separatedness papers study fitted Δ, not fitted closed inseparability I.

Let B_fin(I) be all bar opens having at least one finite-height rectangular C-ideal proof tree. This is an UPPER SET. It is also a FILTER: if u,v have finite trees of depths m,n, graft the v tree (restricted to each u-leaf rectangle) onto every u-bar leaf; since all descendant labels remain under u, the resulting bar leaves lie under u∧v and D leaves remain D; finite depth≤m+n. Thus u∧v has a finite certificate. Therefore
  V_fin=su(B_fin(I)).
Our counterexample says the strongly-exact-filter closure of B_fin(I) is STILL strictly smaller than B(I); this is stronger than just B_fin(I) being a proper subset of B(I). The exact/strongly exact filter theory below is therefore the most promising algebraic language for the eventual intrinsic V characterization.

**Caution:** The term "semiclosed" appears with varying conventions in the localic literature. Until checking the precise primary-source definition, describe V as the "fitting of a closed sublocale" rather than asserting a potentially ambiguous equivalence of terminology. "Finite rank" here means the HEIGHT of a rectangular well-founded C-ideal cover certificate; it does not mean a finite set of generators, finite meets of open nuclei, compactness, or finite rank in a filter lattice.

## 1. Core literature, confirmed at source pages

### [L1] Picado & Pultr, Frames and Locales: Topology Without Points (2012)

Springer Frontiers in Mathematics, DOI 10.1007/978-3-0348-0154-6.
URL https://link.springer.com/book/10.1007/978-3-0348-0154-6

**Confirmed:** standard references for frame coproducts (Chapter IV), sublocales (Chapter III), pointfree separation axioms (Chapter V). The contents list the appropriate sections. The entire proprietary book was NOT searched here in full. Our rectangular-C-ideal framework is standard; its use to measure finite alternating certificate height is our project-specific refinement. Avoid novelty claims from absence of a match in snippets.

### [L2] Picado & Pultr, Separation in Point-Free Topology (2021)

Birkhäuser, DOI 10.1007/978-3-030-53479-0.
URL https://link.springer.com/book/10.1007/978-3-030-53479-0

**Confirmed:** comprehensive monograph on localic separation axioms, including Hausdorff-type and fitting/fitness discussions. Published 2021, 281 pages. **Not verified here:** whether its full text contains a particular analogue of our ranks or the I→fit(I) finite-exhaustion question. Earlier project chapter checks did not find a match; that observation is research history, not a certified systematic negative literature search.

### [L3] Arrieta, Picado & Pultr, A New Diagonal Separation and its Relations With the Hausdorff Property (2022)

Applied Categorical Structures 30 (2022), 247–263 (project bibliographic record; verify page information at final reference stage).
Open institutional page: https://research.birmingham.ac.uk/en/publications/a-new-diagonal-separation-and-its-relations-with-the-hausdorff-pr/

**Confirmed from author/institution abstract:** introduces F-separated locales, characterized by fittedness of the actual diagonal Δ, weaker than fitness and in a duality with strong Hausdorff separation. **Distinction:** Our V=fit(C(d_I)) is not fit(Δ). The negative finite-rank theorem does not directly disprove F-separatedness or settle the relations among D,U,F.

### [L4] Arrieta, Localic separation and the duality between closedness and fittedness (2024)

Topology and its Applications 342 (1 Feb 2024), article 108785, DOI 10.1016/j.topol.2023.108785.
Open abstract: https://arxiv.org/abs/2310.18522
Publisher: https://www.sciencedirect.com/science/article/pii/S0166864123003784

**Confirmed:** explicit comparison of closedness and fittedness in T1-like localic separation, with a new first-order property and implication chart. This is immediately pertinent to the hierarchy, especially D and V, but the ABSTRACT does not state a finite-rank rectangle-tree exhaustion theorem. The publisher full text returned an access error in this search; investigate the arXiv full text before definitive priority assertions.

### [L5] Moshier, Picado & Pultr, Some General Aspects of Exactness and Strong Exactness of Meets (2022)

Topology and its Applications 309 (2022), article 107906, DOI 10.1016/j.topol.2021.107906.
Publisher abstract: https://www.sciencedirect.com/science/article/abs/pii/S0166864121003217
Institutional author copy metadata: https://digitalcommons.chapman.edu/scs_articles/806/

**Confirmed from the article abstract:** strongly exact filters connect with the order dual of the coframe of fitted sublocales; exact filters connect with joins of closed sublocales; a more general coframe/filter construction is developed. **Important:** their word "exact" refers to preservation properties of meets, NOT finite certificate height.

### [L6] Jakl & Suarez, Canonical Extensions via Fitted Sublocales (2025)

Applied Categorical Structures 33, article 10 (published online 28 Feb 2025), DOI 10.1007/s10485-025-09802-6.
**Public full HTML:** https://link.springer.com/article/10.1007/s10485-025-09802-6
Preprint: https://arxiv.org/abs/2404.18325

**Directly verified in full HTML**:
- §2.4 defines su(G)=⋂_{a∈G}o(a) and defines strongly exact filters (closed under meets satisfying ⋂o(a_i)=o(⋀a_i)).
- §6.0–6.1 uses fi(S)={a:S⊆o(a)}.
- Theorem 6.2: the adjunction fi ⊣ su restricts to an isomorphism between strongly exact filters SE(L) and fitted sublocales S_o(L).
- Eq. (6.3.1): fi(C(d))={w:w∨d=1}, EXACTLY our bar filter formula.
- §§6–7 connect fitted hulls of smooth/closed/compact sublocales with exact/regular/Scott-open/completely prime filters via polarities and canonical extension methods.

**Priority and future research relevance: HIGHEST.** Our B_fin is a genuinely combinatorially specified FILTER whose strongly exact closure differs from the full closed-neighborhood filter B(I). This is a sensible bridge from separation trees into existing filter algebra. It may give an intrinsic expression for V in terms of strongly exact closure of disjointness-derived filters, but such a characterization has NOT been proved or found as a ready-made published theorem.

### [L7] Picado, Pultr & Tozzi, Joins of Closed Sublocales (2019)

Houston Journal of Mathematics 45 (2019), 21–38.
Institutional listing: https://nomos.is.cuni.cz/publication/572486?lang=en
Public source-level discussion also in [L6] references.

**Confirmed:** the system of joins of closed sublocales S_c(L), its Booleanization relationship with subfitness, and sublocale representations; helpful when placing fitting of closed I within the larger sublocale coframe. **Not a direct claim** about our finite rectangle-rank filtration.

### [L8] Arrieta, Joins of Closed Sublocales Are Not Always a Coframe (2026)

Order 43, article 15 (published 23 Feb 2026), DOI 10.1007/s11083-025-09725-w.
Open full HTML https://arxiv.org/html/2510.00987v1
Publisher https://link.springer.com/article/10.1007/s11083-025-09725-w

**Confirmed:** resolves a question of Picado–Pultr–Tozzi on whether S_c(L) is always a coframe, in the negative. It underscores that filtered/closed-sublocale generation can have genuinely infinitary failures, but **does not establish or refute our particular V_fin theorem**. It supplies valuable current context for any novelty paragraph about failures of lattice completion or finite exhaustion.

### [L9] Ball, Picado & Pultr, On an Aspect of Scatteredness in the Point-Free Setting (2016)

Portugaliae Mathematica 73(2), 139–152, DOI 10.4171/PM/1980.
Open publisher https://ems.press/journals/pm/articles/13748

**Confirmed:** characterizes locales with every sublocale a join of closed ones, using subfitness and scatteredness. Related to earlier project discussion of scattered fan constructions and point-detectability, but does not imply high-rank bars produce fitted-stage differences. The Y fan sum can have V(Y)=I(Y) at very low fitted rank, yet a HIGH-RANK INDIVIDUAL bar on Y can be transferred into strict fitted rank on X0.

### [L10] Suarez, Revisiting the Relation Between Subspaces and Sublocales (2020 preprint, subsequent publication to verify)

Preprint https://arxiv.org/abs/2010.05284
**Confirmed from abstract:** study of spatial sublocales and pointwise subsets; recovers Simmons' theorem on scattered spaces and representation of all sublocales by sober subspaces. Relevant because our T0 witness is an ordinary product point, whereas the T1 witness uses a graph pullback and need not be point-detectable.

### [L11] Goubault-Larrecq, Exponentiable Locales I: Every Exponentiable Locale Is Continuous (online exposition)

URL https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=6714

**Confirmed from the exposition:** standard rectangular C-ideal construction of localic products, including arbitrary joins in one coordinate at a time. Useful for accessible proof background; this is a technical exposition, not a priority citation for new mathematics.

## 2. What the searches did NOT establish

A targeted public web search using expressions such as "fitted sublocale", "finite rank", "semiclosed", "rectangle C-ideals", "alternating covers", "strongly exact filters", "localic diagonal", "separation hierarchy", and names Picado/Pultr/Arrieta/Jakl/Suarez yielded **no clearly identified paper that states the specific theorem**
  "there exists X with fit(C(d_I)) strictly smaller than its intersection over all finite-height rectangular-bar neighborhoods,"
or the particular two-generic-point graphization/strip-transfer mechanism.

This is a **qualified negative search result, not a novelty assertion**. The precise problem formulation/notation is likely nonstandard. The proof could be equivalent to a published statement framed in filter-language, frame coproduct closure ordinals, normality, cover-dimension, or localic relations. Monographs and some publisher full texts were not searched comprehensively. Search indexes do not guarantee exhaustive coverage. No MathSciNet/Zentralblatt systematic citation-chain review was performed.

## 3. Proof/literature interface: promising specific propositions

**(P1) Finite bar filter.** As shown in §0, B_fin(I) is a filter. Prove carefully in any final write-up via finite tree grafting. It is not necessarily a strongly exact filter.

**(P2) Exact distinction.** The full bar filter B(I)=fi(I) is strongly exact (because fi(I)=fi(fit(I)) and the latter corresponds to a fitted sublocale). The generic-point example shows the strongly exact saturation of B_fin(I) does NOT reach B(I). In literature notation:
   su(B_fin(I))=V_fin ≠ V=su(B(I)).
The equality of strongly exact closures would FORCE equal su's, so they are distinct. This algebraizes the result directly in the filter duality of [L5]–[L6].

**(P3) Scope of positive classifications.** Existing project theorems give finite-rank collapse under regularity, compactness, and suitable clopen/localization hypotheses. Determine which are already special cases of Scott-open, compact, or exact filters in [L6], and whether the converse can be phrased as filter closure. This may be more fruitful than searching for yet higher fitted-rank strictness.

**(P4) Connection to V's intrinsic formula.** A priori V=su(fi(I)) is tautological. What would count as non-tautological is a frame-internal expression for fi(I) avoiding all open neighborhoods in the coproduct—e.g. a generator/filter class built from L, its disjointness relation, and a recognizable closure operation. Strongly exactness supplies an EXISTING closure notion, but the counterexample proves it cannot be replaced by naive bounded-height rectangular proofs.

**(P5) Distinguish diagonal relations.** A genuine dual of U may require treating the closed inseparability I and fitted actual diagonal D separately. F-separatedness is about Δ; Question A was about I. Do not conflate the standard F-separated literature with our new V property.

## 4. Recommended targeted follow-up checks (NOT performed)

1. Read all relevant sections of the 2021 Picado–Pultr monograph at hand, including the separation chapter(s), with explicit search for finite/ordinal rectangular C-ideal derivations and sublocale fitting of closed inseparability; compare terminology in the 2012 volume.
2. Read 2024 Arrieta arXiv full text, especially duality diagrams and generators of fitted diagonals.
3. Work through Theorem 6.2, eq. (6.3.1), and the strongly exact filter examples of Jakl–Suarez 2025; explicitly translate our B_fin and B(I) into their language.
4. Citation-chase from Moshier–Picado–Pultr 2022 to earlier strongly exact filters, and search generalized cover ranks/C-ideal closure ordinals in Johnstone, Vickers and Raney-extension literature.
5. Only after that, consider contacting relevant authors with a **two-page theorem statement and one-page mechanism**, without claiming novelty; the author-facing version should mention that proof correctness and publication priority are separate questions.

## 5. Interim position

The mathematical proof is currently well supported by independent audit. The literature check establishes standard framing in localic sublocales and strongly exact filters, and identifies a very promising path for later intrinsic V research. It does **not** establish that the theorem is known or novel. The current project agenda should be **consolidation, targeted filter-language translation, and cautious novelty checks** before returning to the full I,U,D,V,F hierarchy.


## 6. Additional close structural antecedent: simple extensions (checked after the first ledger pass)

The source [L3] has a freely accessible Coimbra preprint:
https://www.mat.uc.pt/preprints/ps/p2117.pdf

Its **§2.3 (printed page 9)** recalls a "simple extension" of a space by refining the topology relative to a subspace, used to produce separation/property counterexamples. This was checked directly, including the displayed definition. It is an important precedent for **topological extension mechanisms in localic separation**, but it is NOT visibly the same as our two-point extension X0 (which adjoins new isolated/generic points along specified closed C and F rather than simply refining a topology on a fixed set). This reference should be considered in any novelty review of the graphization trick.

The same preprint **§2.2.2** confirms that its fittedness condition applies to the ACTUAL diagonal; our V fits the closed inseparability relation instead. The reference list cites Banaschewski, "Singly generated frame extensions" (J. Pure Appl. Algebra 83 (1992), 1–21) as a further potential source for general extension machinery, but that article has NOT been examined here.

**Search consequence:** the literature gives genuine precedents for both sides of the proof — rectangular coproduct presentations and topology/frame extensions — so any eventual originality claim should be narrowly formulated around the *specific finite-bar exhaustion failure*, not around generic points, simple extensions, or C-ideals considered separately.
