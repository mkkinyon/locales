# Project A — Literature checkpoint: TU, fitted points, and locally compact T1

**Preliminary source check · 15 November 2026.** This note is a **limited primary-source reading**, not a systematic priority search. It follows the independent blind verification of the [negative LC-A example](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md).

## 1. Exact definitions and implications verified

Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, *Topology and its Applications* **342** (2024), article 108785 ([author/publisher PDF](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf); [arXiv:2310.18522](https://arxiv.org/abs/2310.18522)):

- §2.3 uses **totally unordered** (TU): frame homomorphisms \(h,k:L\to M\) with \(h\le k\) must be equal. This is equivalent, by the universal defining property, to \(\mathcal A(X)=\Delta_X\). The equivalence is our immediate translation, not a claim that Arrieta named the sublocale \(\mathcal A\).
- Definition 3.8 defines **fitted points** (pt-fit): every point sublocale is fitted.
- Proposition 3.10 gives \((TU)\Rightarrow(pt\text{-}fit)\), as well as implications from its properties (H), (F).
- Remark 3.3 invokes Johnstone's *Stone Spaces* III.1.5 for a refined topology on \(\mathbb R\) with opens \(U\cup(V\cap\mathbb Q)\), a Hausdorff space which is **not** TU. This historical example is not locally compact because locally compact Hausdorff implies regular, and regular implies TU.
- The implications diagram in §5 separates TU and pt-fit in the **general frame** setting; it does not settle the restricted class of *locally compact sober T1 spaces*.
- Arrieta uses a separate first-order **property (A)** in §3 and its thesis (an “almost homomorphism” property in the closed/fitted duality). It must not be confused with our *relation* \(\mathcal A(X)\) of oriented specialization.

Nathaniel Bannister, *Locales as Spaces in Outer Models*, [arXiv:2411.05967](https://arxiv.org/abs/2411.05967), Definition 1.2 and Proposition 6.2, also uses TU and characterizes it through preservation of T1 under forcing/Boolean-valued interpretations. This gives an alternative perspective on non-TU, but does not currently provide a priority determination for our explicit compact LC sober T1 example.

Igor Arrieta, *A study of localic subspaces, separation, and variants of normality and their duals* (2022 thesis, [University of the Basque Country PDF](https://addi.ehu.es/bitstream/handle/10810/57201/TESIS_IGOR_ARRIETA_TORRES.pdf?sequence=1)), §2.3, recalls Johnstone's definition and discusses TU and bounded-above/bounded-below pairs. The located text does **not** give the desired \((pt\text{-}fit)\Rightarrow(TU)\) under local compactness.

## 2. Priority is unresolved

The limited search and source reading found the older Hausdorff non-TU example and general T1-related theories, **not** an earlier result with the precise extra hypothesis of compactness/local compactness of the sober T1 space. Absence from this short search is not evidence of novelty.

Before a priority claim, inspect directly:
- Johnstone, *Stone Spaces*, III.1.5 (original, not just secondary citation);
- Arrieta's thesis and published articles beyond the located passages;
- Banaschewski, work on singly generated frame extensions and Isbell-type separation;
- the Picado–Pultr monograph and its separation hierarchy;
- literature on non-Hausdorff locally compact T1 sober spaces and on fitted point sublocales.

Record any known space with the same obstruction or a stronger general theorem; compare exact localic versus ordinary T1 notions.

## 3. Mathematical next step (LC-PT)

The question left by the referee is:
\[
\text{locally compact + sober + T1 + (pt-fit)}
\quad\stackrel{?}{\Longrightarrow}\quad(TU).
\]
The blind-refereed counterexample is **not** a counterexample to this implication: it fails both pt-fit and TU.

Potential testing approach: analyze the first-projection map \(\rho_1:\mathcal A(X)\to X\). Its fiber over p is \(\operatorname{fit}([p])\), so pt-fit makes *every ordinary first fiber* precisely [p]. The second fiber is \(\operatorname{cl}([p])=[p]\) under T1. The remaining difficulty is whether a nonzero **pointless** sublocale of \(\mathcal A(X)\) can escape detection by all ordinary point fibers while X is locally compact and sober. Pointwise-fiber information alone does not justify excluding such a sublocale.

The closure/fitted placement of \(\mathcal A\) and its transpose, and the postponed dual construction, are recorded separately in [the A-DUAL/LC-PT register](ProjectA_LCA_FOLLOWUP_AND_A_DUAL_QUESTIONS_2026-11-15.md).
