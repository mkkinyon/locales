# Endgame separation literature crosswalk — established axioms versus intermediate localic relations
## 21 November 2026 · Segment 4

**Purpose.** Primary-source theorem-level attribution and exact project comparisons for the initial separation-hierarchy literature pass. **No priority or novelty claim.** Explicitly distinguish established equality **properties of X** from new/intermediate **sublocales of X×Loc X**. The localic product is the frame coproduct, not a frame direct product.

### Source access and provenance
1. **Igor Arrieta**, *Localic Separation and the Duality Between Closedness and Fittedness*, *Topology and its Applications* **342** (2024), 108785, DOI 10.1016/j.topol.2023.108785, open original publisher PDF https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf. **Directly inspected** §§2–5, Table 1 (p.7), Fig. 1 (p.11), Fig. 2 (p.14), Theorem 3.1, Example 4.5 and Corollary 4.10.
2. **Igor Arrieta, Jorge Picado, Aleš Pultr**, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, *Applied Categorical Structures* **30** (2022), 247–263, DOI 10.1007/s10485-021-09655-9; original author preprint https://www.mat.uc.pt/preprints/ps/p2117.pdf . **Original first page checked; exact historical theorems attributed using Arrieta (2024) Table 1 and earlier repository source reading.** The 2022 original has not been fully reread in this particular segment because the publisher/host intermittently timed out; do not state otherwise.
3. **P. T. Johnstone and Sun Shu-Hao**, *Weak Products and Hausdorff Locales*, in *Categorical Algebra and Its Applications*, LNM **1348** (1988), 173–193, DOI 10.1007/BFb0081358. **Complete original 21-page chapter supplied by project owner and read** in preceding segment; see [dedicated note](ProjectA_ENDGAME_JOHNSTONE_SUN_WEAK_PRODUCTS_PRIMARY_SOURCE_2026-11-21.md). Its §2 and Prop. 2.14 establish the conservative (H) condition and identify it with the contemporaneous Paseka–Šmarda T₂ condition.
4. **Jan Paseka and Bohumil Šmarda**, *T₂-Frames and Almost Compact Frames*, *Czechoslovak Mathematical Journal* **42** (1992), 385–402, received 3 March 1987, full original https://www.dml.cz/bitstream/handle/10338.dmlcz/128349/CzechMathJ_42-1992-3_1.pdf . **Directly checked** introduction and §1, especially definition p.387 and Proposition 1.3. They explicitly say their T₂ condition equals the Johnstone–Sun Hausdorff property; historical contemporaneous original work, not an invention of either project.
5. **Prior work requiring further exact-source comparison:** J. R. Isbell, *Atomless Parts of Spaces*, *Math. Scand.* **31** (1972), 5–32; C. H. Dowker and D. Strauss, *Separation Axioms for Frames* (1972); Banaschewski, *Singly Generated Frame Extensions* (1992); Clementino–Picado–Pultr, *The Other Closure and Complete Sublocales* (2018) **and its 2018 correction**; Picado–Pultr, *Separation in Point-Free Topology* (2021); Juhász–Soukup–Szentmiklóssy, *Anti-Urysohn Spaces* (2016); Cornish *Normal Lattices* (1972) and coherent conormality/minimal-prime antecedents. Do not make theorem-level claims beyond the separately verified prior project ledgers without rechecking.

## I. Exact standard dictionary and axiom relationships

For any locale X, let \(\Delta\hookrightarrow X^2\), \( \mathcal I=\operatorname{cl}\Delta\), \(\mathcal D=\operatorname{fit}\Delta\), and \(\mathcal A\) the oriented specialization sublocale presented by \(u_1\le u_2\) for **all** opens u. Thus:
\[
\boxed{\text{strong Hausdorff (sH)}\iff\mathcal I=\Delta,\qquad
\text{F-separated (Fsep)}\iff\mathcal D=\Delta,\qquad
\text{totally unordered (TU)}\iff\mathcal A=\Delta.}
\]
The first two are **definitions/prior** from Isbell and Arrieta–Picado–Pultr. The last is the **immediate project translation** of Arrieta's definition of TU (\(h\le k:L\to M\Rightarrow h=k\) for all frame maps), using the universal property of \(\mathcal A\) on generalized points; this is **not a novel separation axiom**. For spatial T₁, only \(\operatorname{pt}(\mathcal A)=\operatorname{pt}(\Delta)\) follows, not \(\mathcal A=\Delta\).

Arrieta (2024) Table 1, p.7, states the established **duality**:
- sH means no distinct frame maps respect **disjoint pairs**; Fsep means no distinct maps respect **covers**.
- Relaxed morphism tests: **weak** homomorphisms (Sup, preserve top and disjoint pairs) on sH side; **almost** homomorphisms (PreFrm, preserve bottom and covers) on Fsep side.
- sH iff TU plus source's **property (W)**; Fsep iff TU plus source's **property (A)**. **NOTATION COLLISION:** these are author-defined first-order/morphism properties, **not** our relation \(\mathcal W=\operatorname{cl}\mathcal D\) or our oriented specialization \(\mathcal A\). Likewise their (H), (F) below are **not** \(\mathcal H\) and \(\mathcal F\) relations.
- Strong Hausdorff ⇒ TU, F-separated ⇒ TU (the second explicitly Theorem 2.4).
- sH and Fsep **incomparable** (see Fig. 1, Fig. 2, especially Cor.4.10 for sH not Fsep); regularity implies both. The paper §5 **explicitly claims** all shown implications are strict and no further implications among its listed separation *properties*. Therefore do not rebuild or claim originality for the axiom implication diagram.

Johnstone–Sun/Paseka–Šmarda's conservative **property (H)** is (Arrieta 2024 §2.6):
\[
1\ne a\not\le b\ \Longrightarrow\ 
\exists u\not\le a,\ v\not\le b\text{ with }u\wedge v=0.
\]
It is weaker than strong Hausdorff and agrees with Hausdorff for T₀ spatial locales. **Property (F)** in Arrieta §3 (Theorem 3.1, condition iv) is its fitted-side dual:
\[
1\ne a\not\le b\ \Longrightarrow\
\exists u,v:\ u\to a\ne a,\ v\to b\ne b,\ u\vee v=1.
\]
Fsep ⇒ (F); converse false (Remark 3.3). (F) is hereditary, product-stable and epireflective; it implies the prime-based T₁ condition, but is incomparable with other relaxations of fitness (§3.2). Arrieta's Fig. 2 (p.14) gives the exact established implication hierarchy. **Do not identify source (F) with the project functional equivalence subrelation \(\mathcal F\)**.

Arrieta §2.5 records the closed-diagonal formula \( \mathcal I=c(d_L)\) with \(d_L=\bigvee_{a\wedge b=0}a_1\wedge b_2\), which matches our frame definition. This is **prior apparatus**, not new.

## II. An exceptionally strong known strictness example

Arrieta (2024), **Construction 4.2, Example 4.5, Cor. 4.3, Def. 4.6, Cor. 4.10** (pp.12–14), starts with Cantor space \(X=2^{\mathbb N}\), chooses pairwise disjoint compact subsets \(K_n\), forms \(Z=Y\sqcup\mathbb N\) with \(Y=X\setminus\bigcup K_n\), and a specified quotientlike topology. The **anti-Urysohn** part goes back to Juhász–Soukup–Szentmiklóssy (2016), and Arrieta additionally proves it is **strongly Hausdorff**; it is **not F-separated**.

A nontrivial locale L is anti-Urysohn exactly if for any nonzero opens a,b,
\[
a^*\vee b^*\ne1.
\]
Project \(\mathcal U=c(d_U)\), \(d_U=\bigvee_{a^*\vee b^*=1} a_1\wedge b_2\). Only zero rectangles can appear in d_U, hence \(d_U=0\) and \(\mathcal U=X^2\). As always \(\mathcal U\le\mathcal F\), so \(\mathcal F=X^2\). Strong Hausdorff gives \(\mathcal I=\Delta\); Fsep fails so \(\mathcal D>\Delta\). TU follows from sH, hence \(\mathcal A=\Delta\), and \(\mathcal S=\Delta\). Thus in **our exact notation**:
\[
\boxed{\mathcal S=\mathcal I=\Delta
\quad<\quad\mathcal U=\mathcal F=X^2,\qquad
\mathcal D>\Delta.}
\]
This is an **elementary project translation of a published example**, not a new counterexample. It is a prime candidate for a **canonical literature example** in the final overview: strong Hausdorffness can coexist with universally nonseparable Urysohn/functional relation. Do not invent new priority claims about this phenomenon.

## III. The project's distinct localic phenomena

**Genuinely *intermediate* relation questions not answered by Arrieta's property diagram:** (a) \(\mathcal I=\mathcal U\), \(\mathcal D=\mathcal U\), \(\mathcal W=\operatorname{cl}\mathcal D\) and finite-cover approximations \(\mathcal W_2\); (b) \(\mathcal V=\operatorname{fit}\mathcal I\), alternated hull \(\mathcal H\), meet/join \(\mathcal M,\mathcal J,\mathcal T\); (c) localic relational **composition** \(\mathcal A\mathcal A^\smile,\mathcal S^n,\mathcal I^2,\mathcal D^2\); (d) locally compact/sober/T₁ and nonspatial examples; (e) higher-rank witness/graph problems. These require their own source comparisons, not just arrieta 2024.

**Complementary externally reviewed Project A example:** [negative LC-A canonical](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md) constructs compact, sober, T₁, non-stably-locally-compact X with
\[
\operatorname{pt}(\mathcal A)=\operatorname{pt}(\Delta),\qquad
\mathcal A>\Delta.
\]
This distinguishes pointwise T₁ from the genuine TU/A=Δ condition *even in a compact sober T₁ setting*. Arrieta 2024 Remark 3.3 gives a non-TU space with Property (F) of a different type; the project's stronger compact example is separately audited, but **priority still requires a dedicated search**. Avoid claiming all such examples are new.

The [Q/Q′ dense rational bridge](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) gives \(\mathcal D=\Delta,\ \mathcal W=\mathcal I<\mathcal W_2=\mathcal U\) for a locally compact sober T₁ étale space. This is a **higher-hull/finite-cover distinction**, beyond the static axiom diagram. Separately externally reviewed. Literature priority not yet settled.

**Known coherent characterizations and their ancestors:** [coherent conormality](A-coherent-conormality.md) identifies \(\mathcal I=\mathcal U\) with conormality of compact opens; underlying Cornish minimal-prime and mp-ring characterizations are **known**, do not claim algebraic novelty. [equality characterization note](A-equality-characterizations.md) expresses \(\mathcal F\) through completely below and as kernel pair of completely regular reflection, based on standard Picado–Pultr frame/function theory. A normal locale implies \(\mathcal U=\mathcal F\) via classical normality interpolation/Urysohn lemma (Dowker–Papert, Picado–Pultr). Exact project equality formulations require further checking.

## IV. Next endgame priority

1. Continue tracing \(\mathcal I=\mathcal U,\mathcal D=\mathcal U,\mathcal U=\mathcal F\) against normal/conormal and complete regularity references **without** re-proving classical separation.
2. For possible hierarchy paper, foreground **full intermediate sublocale relations** and their coherent/noncoherent compositions and examples, not the **already settled** T₁/T₂ property implication diagram.
3. Compare preservation under limits/sublocales: Arrieta's Prop.2.1 already proves **sH and Fsep** are closed under arbitrary limits and monomorphisms, so simple closure statements at the equality-class level are known.
4. Test whether older hull/operator literature has exact analogues of \(\mathcal W_2\) and alternating hull, rather than assuming a construction not named in 2024 is new.
5. If preparing a survey, cite the Juhász–Soukup–Szentmiklóssy/Arrieta anti-Urysohn example and the compact T₁ LC-A example side-by-side; their point-free lessons are genuinely different.

**No novelty verdict** from this note. The 1988 user-supplied original and 2024 published article were available; no new user-provided source is requested immediately. The older Isbell/Dowker–Strauss originals may be retrieved if the endgame demands precise historical theorem phrasing.


## V. Additional directly checked normality and conormality predecessors

**W. H. Cornish, *Normal Lattices*, J. Austral. Math. Soc. 14 (1972), 200–215, Theorem 2.4**, full original article https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B71E90ADA1C98165B2EDD8C7B40BB289/S1446788700010041a.pdf/div-class-title-normal-lattices-div.pdf . **Source read:** pp.200–202, abstract and Theorem 2.4. For a distributive lattice with 0, every prime ideal contains a unique minimal prime iff the annihilator ideals of disjoint x,y are comaximal. When a top 1 exists, his condition (h) is the *witness form*:
\[
x\wedge y=0 \Longrightarrow \exists x_1,y_1:
x\wedge x_1=y\wedge y_1=0,\quad x_1\vee y_1=1.
\]
This is **known classical lattice theory**. For coherent frame L, project's independently audited equivalence \(\mathcal I=\mathcal U\iff K(L)\text{ conormal}\) connects it to Cornish's normal-lattice/unique-minimal-prime condition. The converse/equality for arbitrary frames **does not follow** from applying Cornish to the full underlying frame: the relevant bounded distributive lattice is **K(L)**. This distinction was already made in [A-literature-separation-status](A-literature-separation-status-2026-10-21.md). Terminology "normal" in Cornish means modern **conormal** in this spectral convention; don't confuse with frame normality.

**J. Gutiérrez García and J. Picado**, *On the Parallel Between Normality and Extremal Disconnectedness* (2013), original author preprint https://www.mat.uc.pt/preprints/ps/p1304.pdf. **Original source text checked** (abstract and Remark 2.2 via source extraction). Remark 2.2 explicitly states that in a **normal frame** the rather-below relation \(a\prec b\iff a^*\vee b=1\) is interpolative, hence (classically) agrees with the completely-below relation \(a\prec\prec b\). Applied to the generating far rectangles of the project \(\mathcal U\) and completely separated rectangles of the functional relation \(\mathcal F\), this gives the **known-background implication**
\[
L\text{ normal}\Longrightarrow \mathcal U=\mathcal F.
\]
The *general* relation equality \(\mathcal U=\mathcal F\) need not imply normality and is not claimed equivalent by that source. The project formulation is an immediate relation translation of known interpolation, rather than a new normality theorem.

**Bibliographic correction:** Dowker–Strauss, *Separation Axioms for Frames*, belongs to the 1972 symposium proceedings **published in 1974**, as verified in Paseka–Šmarda (1992) reference [5], pp.223–240. Distinguish this from their 1985 *T₁- and T₂-Axioms for Frames* and Dowker–Papert's 1967 *On Urysohn's Lemma*.

**Current status:** the core background classification is now anchored to original sources. Remaining priority work concerns the genuinely **intermediate sublocale relations** and the strict noncoherent hull/rank examples, not the general normality or minimal-prime characterizations.
