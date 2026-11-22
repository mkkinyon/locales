> **21 NOV — PLEWE/ISBELL PRIMARY-ABSTRACT COMPARISON:** [focused first literature reconciliation](ProjectA_PLEWE_ISBELL_CSCATTERED_CLOSED_SUPPORT_LITERATURE_COMPARISON_2026-11-21.md). Plewe 1996 already states the metrizable **disjoint-dense Cantor** characterization and classifies **spatial multipliers**; his non-strongly-Baire factor result makes **Q a classical test factor**. Isbell 1981 supplies the earlier hereditary-local-compactness antecedent. For separable metrizable A the test amounts to **sigma-compact Polish**, equivalently C-scattered. Our closed-support theorem (G') still gives a full **Booleanization sublocale decomposition**, not merely a yes/no test; exact priority of that formula remains undetermined. **Full Plewe/Isbell PDFs were inaccessible**, so this is an initial evidence-limited comparison, not a proof-level full-paper audit.

> **21 NOV — LATER FINITE-JOIN CORRECTION:** The §4 unrestricted **finite**-join product identity is **true for all locales**, not still open: \\(S\\vee T)\\times Z=(S\\times Z)\\vee(T\\times Z)\\ follows because sublocale inverse image along the product projection preserves finite joins. See [MAT*/MUL* post-referee reconciliation](ProjectA_MATSTAR_MULSTAR_REFEREE_RECONCILIATION_2026-11-21.md). §4 is preserved as a historical report of what was known at that earlier point.

# Opus independent review: spatiality and window-ladder addendum
## 21 November 2026 · original addendum and four accompanying scripts reviewed

**Original uploaded source:** \`INDEPENDENT_OPUS_ENDGAME_REVIEW_ADDENDUM.md\` by Claude Opus 5.5 High; additional \`check3.py\`, \`check4.py\`, \`check5.py\`, \`check6.py\`; original earlier \`poset_conn.py\`. They remain conversation attachments. This document is an **independent internal examination and literary comparison**. The proposed product-spatiality proofs are **post-report reviewer-origin and internally inspected**, **not** submitted in a new blind proof audit. The 7-point poset counterexample **is fully checked**. Do not treat numerical homology tests as proof of sheaf \(\infty\)-topos connectivity.

## 1. Spatiality of localic products: main claims

Let A⊆X, D⊆Z, with X,Z compact Hausdorff and induced spatial sublocales [A],[D]. The already checked [closed-support theorem (G′)](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and [weak/full criterion](ProjectA_OPUS_RECTANGLE_OVERLAP_REES_ETALE_OBSERVATIONS_2026-11-21.md) show
\[
[A]\times_{\rm Loc}[D]=[A\times D]_{X\times Z}
\]
iff every nonempty closed K⊆X×Z with both **coordinate traces** K∩(A×Z) and K∩(X×D) dense in K also has K∩(A×D) dense. Call a failure a **bad closed support**.

### Theorem A: a \(C\)-scattered factor guarantees a spatial product

Opus introduces the label **hereditarily somewhere locally compact** (HSLC): every nonempty closed subspace has a point with a compact neighborhood in that subspace. **IMPORTANT PRIOR LITERATURE DISCOVERY:** this is precisely the known notion of a **\(C\)-scattered space** (Telgársky), and that name should be used instead of coining HSLC in a mathematical manuscript. An accessible definition appears in *Topology Proceedings* 27 and in the literature on paracompact C-scattered spaces (Friedler–Martin–Williams 1987); see https://topology.nipissingu.ca/tp/reprints/v27/tp27125.pdf and https://doi.org/10.2140/pjm.1987.129.277 .

**Opus Theorem 1, internally checked:** If A is C-scattered, then for every D, its localic product with [D] is spatial.

*Exact key argument.* If the product were nonspatial, choose bad K and a nonempty relatively open N⊆K disjoint from A×D. Both A-coordinate and D-coordinate traces are dense in N; the latter lies in the complement of the former. Set L=π_X(cl_K N), a nonempty compact Hausdorff subspace of X. Continuity of the projection shows **both A∩L and L∖A are dense in L**. Then A′=A∩L is nonempty **closed in A**. If A′ had a relatively compact neighborhood W of a point a (compact W⊆A′), then compactness makes W closed in Hausdorff L; choose a relatively open L-neighborhood U of a with U∩A′⊆W. Density forces U⊆cl_L(U∩A′)⊆W⊆A, contradicting density of L∖A. Thus A′ is nowhere locally compact. That contradicts C-scatteredness.

This is a **topological sufficient condition** and may be a direct corollary of published product-spatiality theory. It is **not** claimed to characterize spatiality for a fixed arbitrary D: two non-C-scattered Polish factors may still have a spatial product.

### Theorem B: nowhere-locally-compact closed core vs closed rational copy

**Opus Theorem 2, internally checked with a fusion detail identified for audit:** If X,Z are compact **metrizable**, A contains a nonempty closed nowhere-locally-compact subspace A′, and D contains a closed copy E′ of \(\mathbb Q\), then [A]×[D] is nonspatial.

Write L=cl_X A′ and Y=cl_Z E′. Since A′ is closed **in A**, A∩L=A′; likewise D∩Y=E′. The dense subset A′⊂L is **codense** (else a nonempty relatively open part of L would be locally compact in A′), and L has no isolated points. Similarly E′ is countable dense-in-itself inside perfect compact Y. A standard **center-preserving Cantor fusion** constructs compact Cantor subspaces C⊆L and C′⊆Y with A∩C and C∖A both dense in C, and E′∩C′=D∩C′ countable dense in C′. Choose a countable dense G⊆C∖A. **Countable dense homogeneity of Cantor space** gives a homeomorphism h:C→C′ mapping G onto D∩C′. The graph K=Γ_h⊆X×Z has both coordinate traces dense but *no* A×D points. Thus K is bad. The fusion and CDH theorems are classical nontrivial topological inputs; name them in any stand-alone proof.

**One-factor rational test, conditional on (G′):**
\[
\boxed{\text{For separable metrizable A, }\ [A]\times_{\rm Loc}[\mathbb Q]\text{ is spatial}\iff A\text{ is C-scattered}.}
\]
Use a compact metrizable embedding of A. The forward direction is contrapositive of Theorem B with D=Q; the backward direction is Theorem A. This is a clean reformulation, **not a verified novelty claim**.

**Čech-complete factors:** when A,D are both Čech-complete (Polish in separable metric case), they are Gδ in their compactifications/closures; both admissible closed-support traces are dense Gδ in compact K, so their intersection is dense by the Baire theorem, making the product spatial. In particular \(\mathbb P\times_{\rm Loc}\mathbb P\) (irrationals) is spatial, while \(\mathbb P\times_{\rm Loc}\mathbb Q\) is not.

**Coanalytic classification:** Hurewicz (Kechris *Classical Descriptive Set Theory*, Thm 21.18) gives that a **coanalytic separable metrizable** non-Polish space contains a **closed copy of Q**. Accordingly both Polish factors give a spatial localic product; both non-Polish coanalytic factors give a nonspatial one; in the mixed case (Polish A, non-Polish D), spatiality is equivalent to A being C-scattered. **This implication is conditional on the two product-spatiality lemmas and the classical Hurewicz theorem**, not a new Hurewicz theorem.

### Priority and historical context (important)

**Till Plewe, "Localic Products of Spaces", *Proc. London Math. Soc.* 73(3) (1996), 642–678, DOI https://doi.org/10.1112/plms/s3-73.3.642** already states in its public abstract a **metrizable nonspatial-product iff closed subspaces can be embedded as disjoint dense subsets of Cantor space**, as well as a theorem on **spatial multipliers**, and explicitly invokes Hurewicz's rational-space criterion. That prior work is **very close to**, and may encompass, much of Opus's addendum. The matched Cantor fusion in Theorem B is especially Plewe-adjacent. Before treating any consequence here as new, read the full Plewe paper and compare its proof and exact hypotheses; an abstract does **not** license declaring literal theorem duplication. A separate accessible discussion is https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=6400 .

**Editorial use:** emphasize the exact **G′** closed-support mechanism and the classical **C-scattered** term. This is a valuable *application/rediscovery and clarification*, not demonstrated priority.

## 2. Window connectivity: an exact failed converse (mathematically checked)

Opus asks whether a disconnected 2-lower × 2-upper window must obstruct **3-connectivity** of the canonical \(\mathbf C\to\mathbf M\) map. **No**, already for a finite 7-point poset:
\[
P=A_2\oplus A_2\oplus A_2\oplus1.
\]
Let bottom layer {a₁,a₂}, middle {b₁,b₂}, next {c₁,c₂}, and global top t. The **two-sided window**
\[
F(a_1,a_2;c_1,c_2)=\uparrow a_1\cap\uparrow a_2\cap\downarrow c_1\cap\downarrow c_2
=\{b_1,b_2\}
\]
is a **disconnected antichain**. Nevertheless:
- The chain order complex \(\mathrm{Ch}(P)\) is a **cone** on the global greatest element t, hence contractible.
- Every subset has upper bound t. Thus \(M(P)=D(P)\), the **common-lower** complex. It is the union of the two simplices on ↑a₁ and ↑a₂; their intersection contains the middle layers, top layers, and t and is a simplex, hence the union is contractible.
- The canonical inclusion \(\mathbf C(P)\to\mathbf M(P)\) is therefore an **equivalence** (of ordinary realizations, and in the chosen representable Stone-sheaf setting for this finite discrete case). A disconnected interior window therefore does **not** force 3-connectivity failure.

This is a clean negative answer to the proposed *naive converse* of [two-sided crosscut ladder Theorem B](PointFree_crosscut_connectivity_ladder_2026-11-11.md). It does **not** contradict the published sufficient theorem. It suggests (speculatively) a **global spectral-sequence/total-complex obstruction** rather than an obstruction from *one* bad window; no general spectral-sequence converse is proved.

**Finite check from uploaded scripts:** \`check6.py\` gives homology-map ranks in degrees 0..4:
\`[(1,1,1),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]\` over F₂. Independent simplex enumeration: f(Ch)=(7,18,20,8), f(M)=(7,20,30,25,11,2), both contractible by the explicit cone/union argument. The script corroborates but does not prove equivalence.

## 3. Four scripts — precise inspection and reproducibility

All scripts are small Python/NumPy programs. \`poset_conn.py\` from the original Opus review is required and available alongside the four new scripts. Dependencies:
- \`check3.py\` uses \`poset_conn.random_poset\`, \`complexes\`, \`homology_map_ranks\`. Its \`connected_poset\` tests connectivity in the comparability graph of a finite window, which is exactly connectedness of its order complex.
- \`check4.py\` generates layered posets and imports \`double_intervals_connected\` from \`check3.py\`.
- \`check5.py\` imports both helpers and generates random layered posets with at least one **disconnected** 2×2 window, checking **homology-only** 3-connectivity; seed is supplied on command line.
- \`check6.py\` constructs the explicit 7-point ordinal sum, then tests homology maps.

**Actual session reruns:**
- \`python check6.py\`: expected list of F₂ homology maps \`[(1,1,1),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]\`.
- \`python check3.py\`: **2,971** randomly generated posets with **all** tested double intervals connected; **zero** H₂/H₃-nontrivial chain examples and zero homological 3-connectivity failures. This is a **weak test** of the 3-connectivity criterion because its tested instances were homologically trivial above H₁.
- \`python check5.py 3\`: **330** layered posets with a disconnected window; **72** nonetheless had H₂ isomorphism and H₃ epimorphism. Other seeds produce different counts: seed 0→326/80, seed 11→282/76. These are **not numerical contradictions** of Opus's reported 310/73: its seed was not specified in the addendum.
- \`check4.py\` default **4,000 iterations** was started but did not finish within the execution budget; this is **not** treated as verification of its original full reported statistics. A separate smaller reproduction using its imported \`layered\` and \`double_intervals_connected\` helpers, **316** successfully generated layered posets on ≤9 vertices (seed 3, layer sizes 1–3), found **no H₂ epimorphism failure**, **312 connected-window instances**, **no H₃ epimorphism failure**, and **zero connected-window nontrivial H₂/H₃ instances**. Again weak numerical support, not a proof.

**Limits:** Computing \(H_k\) is weaker than a **π₁** or internal \(\infty\)-topos connectivity assertion. The seven-point hand proof is decisive; the random experiments merely illustrate. \`check5.py\` is meant to run as a script, and attempts to import it as a module without a command-line seed trigger its top-level \`sys.argv[1]\` access. No code-integrity concern: this is a usability limitation, not a mathematical bug.

## 4. Unresolved finite-join distributivity question

Opus could not settle, **for arbitrary locales Y,Z** and arbitrary sublocales S,T⊆Y, whether
\[
(S\vee T)\times Z\stackrel{?}{=}(S\times Z)\vee(T\times Z).
\]
It notes positive cases when Z is exponentiable/locally compact, when S,T are both closed and their finite quotient map is proper, or when they are complemented. **Do not infer general validity or failure** without a categorical proof/counterexample. Existing [compact Hausdorff rectangular RC](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and [Stone clique](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) statements have already had their **ambient scope narrowed**, without affecting their accepted algebra results.

## 5. Disposition

1. **Window-ladder converse decisively false**, now a finite counterexample to avoid reopening as a conjecture.
2. **Product spatiality theory mathematically plausible/strongly supported by internal proof checks**, but **classical C-scattered terminology and Plewe 1996 priority antecedents matter greatly**. Before any scholarly priority claim, compare the complete original paper; Claude explicitly did not search the literature.
3. **Leave the proposed universal finite-join distributivity identity OPEN**; the verified specialized uses suffice for current applications.
4. **Archive the scripts and methodology but do not equate homology checks with internal homotopy theorems.** The user uploads remain available in the conversation and were not copied into this public repository.
5. **Technical audit order changes:** any remaining independent proof audit should select either the broad arbitrary-parameter MAT/MUL generalization or the new product-spatiality derivation as its single major target. Combining every recent Opus deduction and the two big theorems into one packet risks losing the benefit of the genuinely independent reading.
