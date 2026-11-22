# From pointwise shadows to localic evidence: revised mathematical architecture
## Point-free topology endgame · Session 11 · 21 November 2026

**Purpose.** An alternative **mathematical/expository synthesis**, not a new theorem ledger, and not a claim that the entire research archive should be reorganized. Informed by (i) the project's [integrated three-branch synthesis](ProjectA_ENDGAME_MATHEMATICAL_SYNTHESIS_2026-11-21.md), (ii) [Claude Opus's independent structural critique](ProjectA_OPUS_ENDGAME_INDEPENDENT_REVIEW_RECONCILIATION_2026-11-21.md), (iii) the [fresh blind technical acceptance of arbitrary-parameter MAT*/MUL*/FINMAT*](ProjectA_MATSTAR_MULSTAR_REFEREE_RECONCILIATION_2026-11-21.md), and (iv) a [full-text comparison with Plewe 1996](ProjectA_PLEWE_1996_FULL_PRIMARY_SOURCE_COMPARISON_2026-11-21.md).

**Scope/provenance:** The new combination/amplification corollaries in §3 are algebraic consequences worked out **internally this session**, relying on separately independently checked input theorems; **not themselves a new blind audit**. The classical techniques and product-spatiality results are credited to their antecedents; originality is not asserted.

## 1. Central mathematical question and the first separation

The starting point from Cameron–Kumar was a graph built from point-pair separation or common-witness relations. In a locale \(X\), there are three distinct things:

- a subset \(T\subseteq\operatorname{pt}(X)^2\);
- the point-generated sublocale \([T]\le X^2\);
- a genuine sublocale relation \(R\le X^2\), possibly with nonzero **pointless** parts, with composition \(R\circ S\) obtained from the actual composability pullback \(R\times_X S\) and its smallest-sublocale image in \(X^2\).

The naïve move from the pointwise shadow of \(R\) to genuine composition is not reliable without a theorem. Localic relation composition is not globally associative. This motivates a **modular question**:

> Under what hypotheses can the localic information be (a) reconstructed from a pointwise order description, (b) encoded by compact closed supports and least dense sublocales, (c) decomposed into exact index sectors, or (d) retained in higher simultaneous-witness spaces?

This organizes the results by **evidence mechanism**, not by the historical labels A/B/C.

## 2. Three successful calculi of genuinely binary localic relations

### 2.1. Priestley/patch order (the coherent regime)

For coherent locales \(P\), the proconstructible spectral sublocales of \(P^2\) correspond to **patch-closed** binary point relations. The one indispensable technical gate is that **actual localic composability pullback and image** agree with the patch-closed order-theoretic computation in this restricted class. The [8 Nov coherent theorem](ProjectA_coherent_composition_canonical_proof_2026-11-08.md) then gives a unital, associative, converse-closed, finite-join algebra of actual relations.

Typical diagonal-hull identities:
\[
\mathcal I=\mathcal A\mathcal A^\smile,\quad
\mathcal D=\mathcal A^\smile\mathcal A,\quad
\mathcal V=\mathcal D^2,\quad
\mathcal W=\mathcal I^2,\quad
\mathcal S^2=\mathcal J.
\]
The additional equality \(\mathcal W=\mathcal U\) is a **separately imported coherent theorem**, not part of the order-composition calculation alone. This regime encompasses many intrinsic normal/conormal and stably compact descriptions, while the **nontransitive coherent \(\mathcal H\)** counterexample shows what it does *not* imply.

**Not all diagonal phenomena reduce to Isbell Booleanization.** The rank-\(\omega\) \(\mathcal V\subsetneq\mathcal V_{\mathrm{fin}}\) construction has its own **proof-tree/bar** obstruction; in the rational bridge the finite/all cover discrepancy is made visible by a nonzero pointless witness. Treat these as different mechanisms and keep their source hypotheses.

### 2.2. Isbell Booleanization and compact closed supports (the rich pointless regime)

For compact Hausdorff \(P\) and subsets \(A,B\subseteq P\), distinguish
\[
p(A,B)=[A\times B]_{P^2},\qquad
q(A,B)=[A]_P\times_{\rm Loc}[B]_P.
\]
The weak/full distinction is **Johnstone–Sun 1988** and classical, as is Isbell's least dense sublocale. In the separately checked rectangular calculus, for \(r,s\in\{p,q\}\),
\[
r(A,B)\circ s(C,D)
=\begin{cases}q(A,D), &[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0.\end{cases}
\]
This yields an associative finite-join rectangle algebra \(\mathscr R_\vee(P)\) with zero, converse, but **not necessarily a unit**; its unit lies inside it iff \(P\) is finite (post-report internally checked referee theorem).

The project-specific full-sublocale formula
\[
[A]\times_{\rm Loc}[D]
=\bigvee_{K} \mathcal B(K)
\tag{G'}
\]
joins the least dense sublocales of all nonempty compact closed \(K\subseteq P^2\) whose two prescribed coordinate traces are dense in \(K\). This **reconstructs the whole sublocale**, not merely a yes/no spatiality predicate; it is a crucial ingredient in proving the actual mixed rectangular composition rule.

**Historical calibration:** Plewe, *Localic Products of Spaces* (1996), **Theorem 3.2, pp.654–655**, already chooses a compact closed support of a nonzero pointless sublocale, proves both coordinate traces dense, and extracts a Cantor witness. Plewe **Theorems 1.6, 2.2, 2.6** and Isbell already provide the \(C\)-scattered spatial multiplier and metrizable \(\mathbb Q\)-test, including **all** metrizable factors. Thus neither the support/density technique nor product-spatiality classification can be sold as new. The **exact full Booleanization join representation (G')** is not identified in Plewe's statement, but no comprehensive negative priority claim is made.

### 2.3. Scattered-sector coordinates (the general arbitrary-parameter regime)

For any locale \(P\) whatsoever and locally compact scattered Hausdorff \(K\), the new independently blind-accepted theorem supplies
\[
\operatorname{Sub}(P\times K)\cong
\prod_{k\in K}\operatorname{Sub}(P)
\tag{MAT*}
\]
and for arbitrary genuine *binary* localic relations on \(G=P\times K\),
\[
(R\circ S)_{ik}=\bigvee_{j\in K}(R_{ij}\circ_P S_{jk}).
\tag{MUL*}
\]
This is a **sublocale-lattice isomorphism**, not a locale isomorphism with a discrete coproduct. A nonisolated \(k\) contributes a **closed sector**, and all coefficients, even pointless ones, are retained. The proof first forms the composability pullback and only afterward decomposes it and takes image. It does *not* distribute an arbitrary meet across infinite coefficient joins.

For an associative finite-join-closed unital coefficient class \(\mathcal A(P)\), row-and-column-finite matrices yield a **genuine unital associative converse-closed** algebra. The row/column finiteness controls the paths, not the topological accumulation of the index.

## 3. NEW INTERNAL SYNTHESIS: two scattered amplification corollaries

### General amplification

**Proposition (formal corollary of independently checked source theorems).** Suppose \(\mathcal A(P)\subseteq\operatorname{Sub}(P^2)\) contains \(0,\Delta_P\), is closed under finite joins, converse and actual localic relation composition, and composition associates within \(\mathcal A(P)\). Let \(K\) be locally compact scattered Hausdorff. Then the class of row-and-column-finite \(K\times K\) matrices of members of \(\mathcal A(P)\), interpreted via MAT*, is an **associative unital involutive idempotent semiring** of genuine relations on \(P\times K\).

This is exactly [FINMAT*](ProjectA_MATSTAR_MULSTAR_POSTREFEREE_CANONICAL_2026-11-21.md); no further topology on \(P\) is required. (A “semiring” here has additive operation finite join, multiplicative operation genuine composition, zero and unit, and involution converse; it is **not** claimed to be complete under infinite joins.)

**Corollary A — coherent-fibre amplification.** Take \(P\) coherent and \(\mathcal A(P)\) its **proconstructible spectral relations**. By the independently reviewed coherent composition theorem, the coefficient assumptions hold, so for **every** locally compact scattered Hausdorff \(K\) the resulting matrix relations on \(P\times K\) form such an actual Loc associative algebra. In particular \(K\) may be noncompact (e.g. \([0,\omega_1)\)); even if the ambient \(P\times K\) is noncoherent, its specified matrix algebra still associates. This is a **derived extension of a positive coherent calculus to a broader ambient**, not a theorem that all ambient relations become coherent or associative.

**Corollary B — rectangular-fibre amplification.** Take \(P\) compact Hausdorff and let \(\mathscr R_\vee(P)\) denote the independently checked finite-join algebra generated by weak/full rectangles. When \(P\) is infinite this algebra has no unit, so explicitly form the *formal unitalization inside the actual localic relation lattice*
\[
\mathscr R_\vee^\sharp(P)
=\{R\vee\varepsilon\Delta_P: R\in\mathscr R_\vee(P),\ \varepsilon\in\{0,1\}\}.
\]
This class contains \(0,\Delta_P\), is converse- and finite-join-closed, and is associative under actual composition. Indeed the general **finite** distributivity law and the genuine identity \(\Delta_P\) give
\[
(R\vee\varepsilon\Delta_P)\circ(S\vee\delta\Delta_P)
=(R\circ S)\vee \delta R\vee\varepsilon S
\vee(\varepsilon\delta)\Delta_P,
\]
where a zero scalar indicates omission of a term. Both triple bracketings reduce by finite distributivity to triple products whose factors lie either in \(\mathscr R_\vee(P)\) (associative) or are \(\Delta_P\) (a strict unit); hence \(\mathscr R_\vee^\sharp(P)\) is associative. Its row-and-column-finite matrices give a genuine associative unital localic relation algebra on \(P\times K\) for every admissible index \(K\).

This is a **simple algebraic unitalization**, not the separately studied *safe graph-adjunction theorem*: no unqualified nonrectangular graph generators or TWIST claim is being made.

### A concrete joint Booleanization/matrix calculation

Take \(P=[0,1]\), \(B=\mathbb Q\cap P\), \(C=P\setminus\mathbb Q\), \(K=\omega+1\) (order topology), and choose the **nonisolated** index \(k_\infty=\omega\). Under MAT*, form two relations \(R,S\le(P\times K)^2\), with precisely one potentially nonzero matrix entry each:
\[
R_{\omega,\omega}=p(P,B),\quad S_{\omega,\omega}=p(C,P),\qquad
R_{ij}=S_{ij}=0\text{ otherwise}.
\]
Every ordinary middle point would have to belong to both \(B\) and \(C\), so the **ordinary point-graph composite is empty**. Yet \([B]\wedge[C]\supseteq\mathcal B(P)\ne0\), so the genuine RC formula and then MUL* give
\[
\boxed{
(R\circ S)_{\omega,\omega}=q(P,P)=P^2,\quad
(R\circ S)_{ij}=0\ (i,j)\ne(\omega,\omega).
}
\]
This provides a fully explicit **actual localic composite with no ordinary composable point pair** supported on a closed **nonopen** index sector, inside a provably associative matrix algebra (after the coefficient unitalization). The calculation combines the **Booleanization** mechanism and the **scattered matrix** mechanism; it is not an independent proof of either input theorem, nor a new blind-audited example.

## 4. The higher simultaneous-witness study has a different proof theory

For a coherent locale with ordered Priestley patch space \(V\), higher witness spaces are built from
\[
I_n=\{(x_i):\exists u\ \forall i\ x_i\le u\},\quad
D_n=\{(x_i):\exists a\ \forall i\ a\le x_i\},\quad
M_n=I_n\cap D_n,
\]
and the chain simplicial object \(\mathrm{Ch}_n\). Their patched Stone-sheaf realizations \(\mathbf I,\mathbf D,\mathbf M,\mathbf C\) are interpreted in a **specified sufficiently large Stone-site sheaf \(\infty\)-topos**; no unproved intrinsic locale-shape/site-independence interpretation is silently substituted.

The binary \(I,D\) relations **plus patch topology** reconstruct all higher patched \(I_n,D_n\) for binary graph isomorphisms. Via stated effective Stone Čech-descent/realization inputs, the \(\mathbf C\to\mathbf M\) comparison is **2-connective** (isomorphisms on \(\pi_0,\pi_1\), epimorphism on \(\pi_2\)), but does **not** recover the chain 2-type. The exact pair of six-point ordinal sums \(A_2\oplus B_{\mathrm{anti}}\oplus C_2\) and \(A_2\oplus B_{\mathrm{chain}}\oplus C_2\) has the **same** patched higher \(I,D\), yet \(\mathbf C\) has \(S^2\) vs contractible homotopy type.

This study shares the coherent patch/graph dictionary with the binary-relation study, but its Čech descent and higher-witness content are **not consequences of FINMAT*** or the rectangular algebra. The new seven-point disconnected-window counterexample also rules out a tempting converse for the crosscut ladder. Keep it a **companion study with explicit dependencies**, not a derived chapter of matrix algebra.

## 5. Editorial choice: two studies, not three research-history bins

**Recommended exposition (without implying papers already exist):**

**Study I — Genuine localic graph relations: recoverability, composition, failure.**
- Opening finite graph/fence; distinction point-shadow / generated sublocale / genuine image composite.
- Coherent Priestley calculus and diagonal hierarchy; the normal/conormal duality, and failure of universal H-transitivity.
- Proof-tree/bar-rank and rational bridge as different failure mechanisms; ranks in the *main narrative* at least briefly, with detailed ordinal calculations in an appendix.
- Isbell Booleanization, Johnstone–Sun weak/full products, Plewe classical support antecedents, and the actual mixed rectangular RC.
- MAT*/MUL*, coherent and rectangle coefficient amplifications, closed-sector example above. The unsafe broad TWIST and nonassociative boundary.
- Optional technical chapters on properness \(L^*\), quotients, generic fibres and four-step effectivity.

**Study II — From binary witnesses to simplicial/Stone-sheaf comparison.**
- Patched ordered setting and exact \(I_n,D_n,M_n,\mathrm{Ch}_n\) definitions.
- Binary graph isomorphism reconstruction and its failure for arbitrary preserving maps.
- Čech witness descent, groupoid, sharp 2-connectivity and the six-point obstruction to 2-type recovery.
- Nonconstant gluing, classifying anima and the crosscut ladder as further developments, with site and imported-theorem qualifiers.

A **single opening mathematical thesis** can introduce both studies:
> Ordinary graphs are not faithful witnesses of localic constructions. The right replacement is not a universal associative graph algebra, but a collection of *certified reconstruction and composition regimes*—and, beyond binary composition, an explicit theory of simultaneous witnesses.

**Advantages over existing three-branch order:** makes the coherent theorem appear **once** instead of duplicating A/B; gives Booleanization and Plewe their correct central-but-not-universal role; incorporates the new arbitrary-\(P\) scattered extension; and displays the substantial independence of Stone-sheaf homotopy. The archive's 47-group A/B/C ledger should remain intact as a **research-provenance index** rather than be rewritten to follow this new reader-facing architecture.

## 6. Source status and remaining boundaries

- **Independently checked in original or later blind packets:** coherent proconstructible composition, compact-Hausdorff mixed p/q RC (with distinct post-report addendum status), arbitrary-\(P\) MAT*/MUL*/FINMAT*.
- **Derived internally in this note:** the two coefficient-algebra amplifications, rectangular unitalization, and the nonisolated-index rational/irrational example.
- **Higher witness:** originally conditional external checks plus separately crosschecked post-report theorems, tied to an explicit Stone-sheaf \(\infty\)-topos. Not a full intrinsic localic shape theorem.
- **Historical:** Isbell, Johnstone–Sun, Plewe and Priestley/Stone duality provide foundational concepts and many product-spatiality theorems.
- **Not proved:** arbitrary relations associate, all TWIST cases are safe, arbitrary infinite joins commute with pullback/composition, high homotopy follows from binary graphs, or all project claims have been published previously or are historically novel.

**Current recommendation:** preserve this alternative outline as a candidate **reader-facing mathematical architecture**; compare it with the integrated synthesis before finalizing a November 25 educational research wrap-up. No need to settle broad conjectures or seek another large blind audit to choose an exposition.
