# Unified Point-Free Topology — notation, ambient categories, and proof imports
## Compact one-page reader's reference · 21 November 2026 · after independent structural audit

**Start here** before using [theorem ledger v3.2](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md), [proof atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md), or [five worked examples](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md). The [independent structural referee reconciliation](ProjectA_ENDGAME_STRUCTURAL_EXTERNAL_REFEREE_RECONCILIATION_2026-11-21.md) explains which of the interfaces below received a fresh targeted mathematical review, which remain conditional, and which were *not* rechecked.

## 1. Basic operations on a locale X

Let \(L=\mathcal O(X)\), \(Q=\mathcal O(X\times_{\mathbf{Loc}}X)\). Write \(C(d)\) for the closed sublocale complementary to an **open element** \(d\in Q\); \(\operatorname{cl}\) and \(\operatorname{fit}\) are **closure** and **fitting** of sublocales, not point-set closure and an arbitrary filter closure.

| Symbol | Definition / exact meaning |
|---|---|
| \(\Delta\) | Localic diagonal \(X\hookrightarrow X^2\), \(X^2=X\times_{\mathbf{Loc}}X\) |
| \(d_{\mathcal I}\) and \(\mathcal I\) | \(d_{\mathcal I}=\bigvee_{a\wedge b=0}a\boxtimes b\), \(\mathcal I=C(d_{\mathcal I})=\operatorname{cl}\Delta\) |
| \(\mathcal D,\mathcal V,\mathcal W\) | \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal V=\operatorname{fit}\mathcal I\), \(\mathcal W=\operatorname{cl}\mathcal D\) |
| \(\mathcal M,\mathcal J,\mathcal T\) | \(\mathcal M=\mathcal I\wedge\mathcal D,\ \mathcal J=\mathcal I\vee\mathcal D,\ \mathcal T=\mathcal V\wedge\mathcal W\) (meet/join **of sublocales**, not point pairs) |
| \(\mathcal H\) | Least **simultaneously closed and fitted** super-sublocale of \(\Delta\). Need not be transitive, **even coherently**. |
| \(\mathcal U\) | Urysohn closed relation \(\mathcal U=C(d_{\mathcal U})\), \(d_{\mathcal U}=\bigvee_{a^*\vee b^*=1}a\boxtimes b\), where \(a^*\) is the frame pseudocomplement |
| \(\mathcal F\) | Functional closed relation \(C(d_{\mathcal F})\): \(d_{\mathcal F}=\bigvee_{f:X\to\mathbb R}(f\times f)^*(\mathbb R^2\setminus\Delta_{\mathbb R})\). Kernel pair of completely regular reflection. |
| \(\mathcal A,\mathcal B,\mathcal S\) | \(\mathcal A\): oriented localic specialization with generalized-pair condition \(u_1\le u_2\) for all \(u\in L\); \(\mathcal B=\mathcal A^\smile\); \(\mathcal S=\mathcal A\vee\mathcal B\). In coherent spectral points, \(x\le y\) means every open containing x contains y; opens are **upsets**. |

**Composition convention:** \(R\circ S=\mathrm{im}_{\mathbf{Loc}}(R\times_Y S\to X\times Z)\) means *first R, then S*; it is not ordinary point composition in general. Outside a **separately proven associative class**, do not omit parentheses.

**Cover distinction:** \(\mathcal D=\bigwedge_{\mathscr C\ {\rm all\ covers}}O(w_{\mathscr C})\), \(\mathcal D_2=\bigwedge_{\mathscr F\ {\rm finite\ covers}}O(w_{\mathscr F})\), \(w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c\); \(\mathcal W_2=\operatorname{cl}\mathcal D_2\). The finite/all distinction can be **pointless** and survive closed hulls.

## 2. Theorem scope table — what may be used where

| Principal theorem/interface | Exact ambient and assumptions | Special import / forbidden extrapolation |
|---|---|---|
| **Coherent composition/hulls** | **Coherent** locales and **proconstructible spectral** sublocales of finite localic products; finite words/joins; classical prime-filter duality | Actual Loc pullback/image checked; compact-open-filter fitting lemma needed. Prove \(\mathcal W=\mathcal I^2\) here, then import the **separate coherent** \(\mathcal W=\mathcal U\) before writing \(\mathcal U=\mathcal I^2\) or \(\mathcal S^4=\mathcal U\vee\mathcal V\). Not all sublocales compose associatively. |
| **Rectangular RC and finite sums** | One compact Hausdorff G; \(p(A,B)=[A\times B]_{G^2}\) (Johnstone–Sun **weak** product), \(q(A,B)=[A]\times_{\rm Loc}[B]\) (**full** product) | Binary RC uses **nonzero localic middle overlap**, even with no ordinary points. Finite joins associate. **New referee-addendum theorem:** unital iff G finite. No arbitrary-join interchange. |
| **Graph extensions** | Restrict to the exact [locally closed partial-homeomorphism graph algebra](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md) and stated overlaps, importing RC | The larger graph algebra is **unital**, but does not license arbitrary open/proper graphs, all infinite chart families, or general TWIST. This graph theorem was **not** retested in the 21 Nov structural packet. |
| **Scattered MAT / MUL** | \(P\) compact Hausdorff, \(K\) compact **scattered Hausdorff**; closed singleton index sectors; arbitrary binary sublocales of \((P\times K)^2\) | MATn splits **all** sectors as sublocales; MUL uses image only **after** forming the genuine composability meet and decomposing it. No locale isomorphism with a discrete K; **MUL alone does not imply associativity**. |
| **Finite-support matrix algebra** | Fibre **unital associative** relation algebra with finite joins, converse; K-index matrices with **row and column** finite support | FINMAT/PATH associate by **finite** sums. One-sided finite variants and locally compact K generalization have separate, later verification statuses. |
| **Diagonal/H counterexamples** | Finite Priestley/coherent two-ray model or locally compact sober T1 étale bridge as specified in each source | Coherent \(\mathcal H^2\nleq\mathcal H\) relies on *actual closed+fitted sublocale reconstruction*; \(W<W_2\) relies on **Booleanization**, all-cover descent, and closed spatial ambient \(F=X\times_{\mathbb R}X\). |
| **Higher I/D/M, chain groupoids** | **Coherent** locale, its **patch Stone** space, and chosen sufficiently large \(\mathscr H_\kappa=\mathrm{Shv}_\infty(\operatorname{Stone}_\kappa,\text{finite surjective families})\) | \(I_n,D_n\) require **one simultaneous** bound, not pairwise bounds. Binary graph **isomorphisms** reconstruct higher patched hulls; arbitrary binary-preserving maps may fail \(M_2\). Under-\(\mathbf C\) \(\mathbf C\to\mathbf I,\mathbf C\to\mathbf D\) arrow comparison is a **separate input**. |
| **Chain→meet 2-connectivity** | Same chosen Stone-sheaf site; degreewise **effective Čech** lower-witness covers and standard realization-connectivity lemma | \(\mathbf C\to\mathbf M\) is 2-connective (π₀,π₁ iso, π₂ epi), **not** a 2-type equivalence. Six-point example tests sharpness, not the general theorem. Site-size independence and intrinsic localic shape are not established. |

## 3. Two operations you must NOT exchange

1. **Point sets vs actual Loc images:** \(\operatorname{pt}(R\circ S)\) may not be ordinary relational composite. Coherent proconstructible and p/q RC are *separate* classes where equality has been **proved** by localic pullback/image mechanisms.
2. **Infinite meet vs infinite join:** writing \((\bigvee R_i)\wedge(\bigvee S_j)=\bigvee(R_i\wedge S_j)\) for general sublocales is **not valid**. The scattered MUL theorem first forms \(Q=R_{12}\wedge S_{23}\), **then** splits Q, and only then applies the arbitrary-join-preserving image map.

## 4. Certification and publication

The 21 Nov structural referee reviewed **seven selected interfaces**, not all 46 theorem groups. **Independent structural “valid after repairs” ≠ re-proof of imported results** (e.g. coherent W=U, under-C comparison, rank-ω V, \(\omega+m\) H). Referee-origin unitality iff finite is a **post-report theorem internally checked**; it was not included in the original blind packet. Literature priority remains unresolved for individual candidate contributions. See [current ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) for each exact evidence label.
