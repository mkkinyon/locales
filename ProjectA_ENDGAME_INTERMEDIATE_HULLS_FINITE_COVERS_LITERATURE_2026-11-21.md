# Unified Point-Free Topology — intermediate diagonal hulls and finite-cover literature
## Endgame primary-source comparison, Segment 5 · 21 November 2026

**Purpose.** Source-grounded comparison of Project A's \(\mathcal V=\operatorname{fit}(\mathcal I)\), \(\mathcal W=\operatorname{cl}(\mathcal D)\), alternating closed-and-fitted hull \(\mathcal H\), and finite-cover approximants \(\mathcal D_2,\mathcal W_2\). **NOT a priority verdict.** All project claims below are sourced to linked canonical notes and are distinct from cited published source theorems. Use the full **localic square** throughout.

**Canonical project inputs:** [fitted diagonal](A-fitted-diagonal.md); [coherent composition and hull identities](ProjectA_coherent_composition_canonical_proof_2026-11-08.md); [alternating hull](A-alternating-hull-diagonal-2026-10-21.md); [W-phase audit](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md); [Q/Q′ counterexample](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md); [J/T comparability theorem](ProjectA_J_T_COMPARABILITY_GRAPH_STABLY_COMPACT_CANONICAL_2026-11-17.md); [separation source crosswalk](ProjectA_ENDGAME_SEPARATION_PRIMARY_SOURCE_CROSSWALK_2026-11-21.md).

## 1. Direct sources examined in this tranche

**S1 — Jakl–Suarez (2025).** Tomáš Jakl and Anna Laura Suarez, *Canonical Extensions via Fitted Sublocales*, *Applied Categorical Structures* **33** (2025), article 10, DOI 10.1007/s10485-025-09802-6. Full open HTML primary source https://link.springer.com/article/10.1007/s10485-025-09802-6 . Directly checked §§2–3, 6.1–6.6, especially Theorem 6.2, Lemma 6.5, Theorem 6.6, equation (6.3.1), Proposition 6.7, Theorems 6.8, 6.11, 6.13. Treats \(\operatorname{fit}\) as the established closure operator whose fixed points are fitted sublocales; links fitted sublocales to strongly exact filters, fittings of closed and locally closed sublocales to classes of closed/regular/exact filters, and fittings of compact sublocales to Scott-open filters. **Not** a theorem about Project A's particular diagonal hulls or ranks.

**S2 — Arrieta (2022).** Igor Arrieta, *On Joins of Complemented Sublocales*, *Algebra Universalis* **83** (2022), article 1, DOI 10.1007/s00012-021-00757-y. Primary preprint https://www.mat.uc.pt/preprints/ps/p2023.pdf; abstract and source excerpts checked. Constructs/studies \(\mathcal S_b(L)\), joins of locally closed/complemented sublocales, and their relation with induced spatial sublocales and \(T_D\). Established background to our handling of sublocale lattice operations; does not state our diagonal relation hierarchy.

**S3 — Arrieta (2026).** Igor Arrieta, *Joins of Closed Sublocales are not Always a Coframe*, *Order* **43** (2026), article 15, DOI 10.1007/s11083-025-09725-w, published 23 February 2026; full open article metadata, abstract and reference list directly checked https://link.springer.com/article/10.1007/s11083-025-09725-w ; arXiv:2510.00987. Proves the Picado–Pultr–Tozzi 2019 open question has negative answer: the frame \(\mathcal S_c(L)\) of arbitrary joins of closed sublocales need not be a coframe. This **does not** directly assert an inequality among \(\operatorname{cl}\) and \(\operatorname{fit}\) on our diagonal; it is a strong warning against importing invalid infinitary distributive laws.

**S4 — Exact-filter predecessors.** Ball–Moshier–Picado–Pultr et al., *Exact Filters and Joins of Closed Sublocales* (2020), source abstract https://digitalcommons.chapman.edu/scs_articles/664/ ; Moshier–Pultr–Suarez, *Exact and Strongly Exact Filters* (2020), https://digitalcommons.chapman.edu/scs_articles/682/ ; Picado–Pultr–Tozzi, *Joins of Closed Sublocales* (2019). Source abstracts checked; their precise statements are built into S1's citations. Need not claim direct full reading here. Important **existing** sublocale/filter technology for \(\operatorname{fit}(\mathcal I)\), especially S1 §6.3.

**S5 — Picado–Pultr (2012).** *Frames and Locales: Topology without Points*, chapter VIII on uniformity and nearness, §§2–5 and chapter IX §1, full original electronic edition https://pages.jh.edu/rrynasi1/NewFoundations4Math/Literature/Frames%2BLocales/Picado%2BPultr2012Frames%2BLocales.pdf . Relevant verified items: Ch.VIII §2 treats entourage-versus-cover definitions and the rather-below relation; §2.3.3 states that in any system of covers containing all finite covers the induced rather-below relation equals the ordinary rather-below relation. Ch.VIII §5.1 states compact regular frames have a unique nearness, the all-cover system, which is a uniformity; Ch.IX §1.2 shows in normal frames finite covers can be refined by rather-below covers. **These are known nearby cover techniques**, *not* source statements about \(\mathcal D_2\), \(\mathcal W_2\), or \(\Phi_2^\infty(0)\).

**S6 — Arrieta–Picado–Pultr (2022).** *A New Diagonal Separation and Its Relations With the Hausdorff Property*, *Applied Categorical Structures* 30 (2022), 247–263; original author PDF https://www.mat.uc.pt/preprints/ps/p2117.pdf . Primary source explicitly treats fitting \(\operatorname{fit}(\Delta)\) as the established notion of fitted diagonal, but does not in the inspected sections define our finite-cover closed hull \(\mathcal W_2\). Previous source note contains full equality-axiom crosswalk.

**S7 — Arrieta–Suarez (2026).** *The Lattice of Smooth Sublocales as a Bruns–Lakser Completion*, *Applied Categorical Structures* (2026), DOI 10.1007/s10485-026-09873-z, https://link.springer.com/article/10.1007/s10485-026-09873-z. Abstract/metadata found after S1–S3. Another very recent, closely related **algebraic representation** of joins of locally closed sublocales; fuller theorem comparison **not yet performed**. Do not misidentify its "smooth" sublocales with our \(\mathcal W\), or assume it proves our rank constructions.

## 2. Formal hull operations: known versus project-specific

For \(X\) any locale and \(Y=X\times_{\rm Loc}X\), put:
\[
\Delta=\Delta_X,\ I=\operatorname{cl}\Delta,\ D=\operatorname{fit}\Delta,\
V=\operatorname{fit}I,\ W=\operatorname{cl}D,\
J=I\vee D,\ M=I\wedge D.
\]
**Established tools:** closure \(c\) and fitting \(f\) are both extensive, monotone, idempotent **closure-type operators on the sublocale poset**. The least **simultaneously closed-and-fitted** hull \(H_Y(S)\) is the meet of all common fixed-point sublocales containing S; transfinite alternating iteration of \(cf\) or \(fc\), with joins at limits, stabilizes at this least common fixed point (standard complete-poset closure-operator argument). For S=Δ call it \(\mathcal H\). Existence/closure-operator formalism is **not by itself a new theorem**.

**Project-specific positional identities:** \(I\le W\), \(D\le V\); \(J=I\vee D\) satisfies
\[
\boxed{\operatorname{cl}(J)=W,\qquad \operatorname{fit}(J)=V}
\]
by monotonicity/idempotence and the inequalities. Thus
\[
T(J)=\operatorname{cl}(J)\wedge\operatorname{fit}(J)=W\wedge V.
\]
**WARNING:** \(W\wedge V\) need not already be *both* closed and fitted, and need not equal the least common-fixed-point hull \(\mathcal H\). Our named \(\mathcal H\) is constructed by transfinite iteration, not by one meet of partial hulls.

For \(d_I=\bigvee_{a\wedge b=0}a_1\wedge b_2\) and \(I=C(d_I)\), we have the **exact direct source connection** (S1 eq.(6.3.1)):
\[
C(d_I)\subseteq O(u)\iff d_I\vee u=1,\qquad
\boxed{V=\bigwedge_{u\vee d_I=1}O(u)}.
\]
The indexing \(F_I=\{u:d_I\vee u=1\}\) is the **closed filter associated with I** in Jakl–Suarez; its fitting is in their closed/regular-filter framework. This representation is an *immediate translation* of known S1, not a separate new proof. The *special geometry* of this filter for the inseparability diagonal and its graph-rank consequences are not asserted in S1.

**Coherent input:** for coherent locales the project proves \(W=U\) and \(I=A A^\smile,\ D=A^\smile A,\ V=D^2,\ U=I^2\), where A is oriented specialization and composition is **genuine localic** (external audit subject to imported coherent inputs). The 2025 fitted-sublocale paper does **not** contain these specific relational composition identities; exact older antecedents remain to be searched.

## 3. New short pointwise fact: D and D2 have identical ordinary points

Let \(X\) be any topological space represented as a spatial locale. For any open cover \(\mathscr C\) put
\[
w_{\mathscr C}=\bigvee_{c\in\mathscr C}(c\boxtimes c)\in \mathcal O(X^2).
\]
Define \(D=\bigwedge_{\mathscr C}O(w_{\mathscr C})\) and \(D_2=\bigwedge_{\mathscr F\text{ finite}}O(w_{\mathscr F})\). On an **ordinary point pair** \((x,y)\), factoring through O(w) means a member of the cover contains both points. Then
\[
\boxed{\operatorname{pt}(D)=\operatorname{pt}(D_2)
=\{(x,y):\overline{\{x\}}\cap\overline{\{y\}}\ne\varnothing\},}
\]
where the pair-notation identifies the points of the localic square with pairs of points, even if the entire square is nonspatial.

*Proof.* If \(z\) is in both singleton closures, any open containing z also contains x,y, so all covers have a common member. Conversely, if the closures are disjoint, their two complements \(\{X\setminus\overline{\{x\}},X\setminus\overline{\{y\}}\}\) form a **finite two-element open cover** without any member containing both x,y. Thus the finite and all-cover conditions give the same point pairs, already Cameron–Kumar's Cm graph. □

This is an **elementary project corollary**, newly emphasized at the endgame, not independently externally audited (but requires no new deep ingredient). It is consistent with, and strengthens the interpretation of, the original [D-Cm note](A-fitted-diagonal.md). It shows that the distinction \(D_2>D\), and a fortiori \(W_2>W\), can be **entirely pointless**, even for the source being a topological space.

## 4. Exact finite-cover pre-nuclei and the Q/Q′ example

Canonical source: [externally reviewed Q/Q′ counterexample](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md), §1–7. With \(\Phi(q)=\bigvee_{\mathscr C}(w_{\mathscr C}\to q)\) and \(\Phi_2(q)=\bigvee_{\mathscr F\text{ finite}}(w_{\mathscr F}\to q)\), the stable nuclei give D and D2, and
\[
W=C(\Phi^\infty(0)),\quad W_2=C(\Phi_2^\infty(0)).
\]
At the **first stage** both operators agree:
\[
\boxed{\Phi(0)=\Phi_2(0)=d_U
=\bigvee_{a^*\vee b^*=1}a\boxtimes b.}
\]
Thus no all-versus-finite disparity appears at rank one. The distinction comes from **later stabilization of these cover operators**. In the second-countable sober locally compact T1 étale bridge X the reviewed proof gives
\[
\boxed{D(X)=\Delta,\qquad W=I<W_2=U=X\times_{\mathbb R}X.}
\]
The countable atlas forces full-cover fitting of Δ back to Δ; **every finite cover** has a dense matching locus on the separated source sheets, leaving the nonzero pointless Booleanization \(B(J)\le D_2\wedge J\) for an open bridge sector J; its ambient closure fills J. The finite/all difference is thus genuinely **nonspatial** rather than a difference in ordinary point pairs. The referee independently checked the main construction, with one presentation correction in independent U proof; the exact Φ/Q equivalence was checked separately after the blind audit. Historical ledger entries labeling Q/Q′ open are **superseded**.

**Compactness:** if X is compact, every X-cover has finite subcover, so \(D=D_2\) and \(W=W_2\) (formal, no priority). Ordinary T1, sobriety, local compactness, second countability—even together—do not force equality, as X shows.

## 5. Precise relation to uniformities and nearness

There is a close **methodological** analogy: an open cover \(\mathscr C\) yields a **diagonal-square open** \(w_{\mathscr C}\), like a cover entourage, and our \(D_2\) retains only finite-cover squares. Chapter VIII in Picado–Pultr 2012 already develops entourages, covers, nearness, and the special significance of finite covers; §2.3.3 notes that containing all finite covers determines the standard rather-below relation; Ch.VIII §5 handles compact uniform/near frames. Ch.IX connects normal finite covers with rather-below refinements.

**But no exact theorem was located** in those searched source passages identifying the **sublocale**
\[
\operatorname{cl}\!\left(\bigwedge_{\mathscr F\mathrm{ finite}}O(w_{\mathscr F})\right)
\]
with a named uniformity, a nearness, or a previously studied diagonal relation. Classical fine uniformities normally involve **normal** or **uniform** covers, not every arbitrary open cover. Do not claim W2 is *the* fine-uniform entourage or *the* total bounded uniformity from an analogy. More careful nearness theory may still reveal an exact link; classify **priority unresolved**.

## 6. Project publication/overview implications

**Classical/known:** closure and fitting of sublocales; their general closure-system formalism; the filter correspondence for fitting a closed sublocale; exact/strongly-exact filter work; finite-cover uniformity/nearness methods; and general problems with arbitrary joins of closed sublocales.

**Project contributions requiring fresh precise comparison, not asserted new:** names \(\mathcal V,\mathcal W,\mathcal H\) **as diagonal-derived relations**; the coherent relation-power identities; the inequalities and strictness examples of the noncoherent hull diamond; the finite-cover **post-stabilization** distinction \(W<W_2\) (and associated Q,Q′ negative answers) under strong countability/local compactness/sobriety/T1 hypotheses; and the localic graph-rank and transitivity issues.

**Recommended canonical exposition:** place S1's filter formula (our Eq. for V) directly after definition of the hierarchy; use the explicit ordinary-point identity ptD=ptD2 before presenting the bridge example; distinguish *generic abstract hull theory* from *special diagonal geometry*. Avoid claiming that the sophisticated literature on exact filters already proves our composition or rank theorems; and avoid claiming no earlier exact formulation without comprehensive search.

**Remaining close source request (optional):** Arrieta's 2022 doctoral thesis *A Study of Localic Subspaces, Separation, and Variants of Normality and Their Duals* (full 2022 thesis at https://addi.ehu.es/bitstream/handle/10810/57201/TESIS_IGOR_ARRIETA_TORRES.pdf?isAllowed=y&sequence=1), and Clementino–Picado–Pultr 2018 with its correction. The thesis is a plausible place for further unpublished/hard-to-find variants of intermediate hull comparison. URLs located; **not yet read closely**. No urgent user upload needed until these links fail or a precise critical assertion requires it.
