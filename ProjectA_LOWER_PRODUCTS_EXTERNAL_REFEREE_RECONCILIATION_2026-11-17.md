# Project A — Blind referee report, addendum, and Plewe: reconciliation of lower products

**17 November 2026.** This is a claim-by-claim reconciliation of the independently supplied blind report (*Referee report — Project A products in the lower localic hierarchy*, 16 Nov), its subsequent addendum (*ProjectA_referee_report_addendum_2026-11-16*), the [pre-referee consolidation](ProjectA_LOWER_PRODUCT_PRESERVATION_CONSOLIDATION_2026-11-17.md), and its [internal adversarial audit](ProjectA_LOWER_PRODUCT_PRESERVATION_INTERNAL_ADVERSARIAL_AUDIT_2026-11-17.md). It records explicit mathematical corrections, provenance, and open questions. The resulting [canonical account](ProjectA_LOWER_PRODUCTS_POSTREFEREE_CANONICAL_2026-11-17.md) incorporates them. Plewe (1996) was supplied by the user and *read directly*, unlike the referee addendum, which flagged it as not yet consulted.

## A. Verdict and changes of status

The referee found **no invalidating error in the theorem statements or counterexamples** in the blind packet. Specific proof gaps G1–G5 were repaired. The strict product failures \(\mathcal D,\mathcal V,\mathcal M\) are now independently reviewed, not solely internally checked. The SC+ formulas used as inputs were checked again independently. The pre-referee note and internal audit should be retained as historical records, **not rewritten to conceal their obsolete qualifications**.

The single significant internal-audit correction is this:

> Earlier internal audit: we cannot assert that the point sets of the two sides of a strict \(\mathcal V\)-product inclusion coincide, because \([T_X]\) may gain sobrification points.
>
> Reconciled result (referee E4–E5): in SLC spaces \(T_X\) is **saturated in sober** \(X^2\), hence sober, and \(\operatorname{pt}[T_X]=T_X\). Similar arguments handle \(P_X^-\) and \(P_X^+\cap P_X^-\). The strict \(\mathcal D,\mathcal V,\mathcal M\) inequalities **do have identical points on both sides**. Their difference is pure point-free nonspatiality.

The original internal audit's warning remains sound for *general* point-induced \([P]\) with arbitrary nonsober \(P\), but not for the special point spaces used here.

## B. Disposition of all reported gaps G1–G5

| Item | Referee's finding | Resolution |
|---|---|---|
| **G1** | Closed restriction \([P]\wedge c(F)=[P\cap F]\) is valid as well as open restriction. | Accepted and proved by splitting \([P]\) into its pieces in complementary open/closed sublocales. Repairs \(\mathcal D_{Y_0}\wedge c(X_0^2)=\mathcal D_{X_0}\), needed for strict \(\mathcal M\). Caution now applies to *noncomplemented* restriction, not to every closed restriction. |
| **G2** | Compactified witness order needed a real closedness argument. | Accepted sequential proof on compact metrizable \(K^+\). Escaping distinct witness labels converge only toward the new bottom; stable witnesses have fixed upper endpoints; all limit pairs remain ordered. |
| **G3** | Compact-factor naturality had an imprecise comparison map. | Corrected to \(\eta_{A,B}:\mathrm{Loc}(A\times_{Top}B)\to\mathrm{Loc}(A)\times_{Loc}\mathrm{Loc}(B)\) and its *frame* comparison \(\mathcal O(A)\oplus\mathcal O(B)\twoheadrightarrow\mathcal O(A\times_{Top}B)\). Naturality is applied to subspace embeddings. Do **not** call a frame coproduct a frame direct product. |
| **G4** | Infinite componentwise decomposition of sublocales cannot rely on an infinite coframe distributivity assumption. | Replaced with the nucleus identity \(j(a)\wedge e_i=j(a\wedge e_i)\wedge e_i\) on \(\prod_i L_i\), showing all nuclei split into components. Hence arbitrary frame direct products preserve all five relations. |
| **G5** | Witness-neighborhood family alone is not meet-stable. | Include sheet-only compact opens \(V_A\sqcup W_B\) besides witness opens \(\{r_t\}\sqcup V_A\sqcup W_B\). The algebraicity conclusion survives. |

Two other source/presentation corrections: the point relation \(T_Y\) is **always sober** in our SLC setting (saturated subspace of a sober space), though it need not be locally compact; and the meanings of “coherent” and “patch” (noncompact patch \(K\) versus compactified \(K^+\)) are stated explicitly.

## C. Disposition of the referee's E1–E8

| Item | Mathematical conclusion | Status in canonical account |
|---|---|---|
| **E1** | \(\mathcal I\) exactly preserves binary locale products for **arbitrary locales**; more generally closure commutes with binary products of sublocales. | Incorporated with density/rectangle proof, §3.1. |
| **E2** | Lax \(\mathcal D,\mathcal V,\mathcal W,\mathcal M\) inclusions hold for arbitrary locales. | Incorporated §3.1; \(\mathcal W\) exactness outside SLC is **not** inferred. |
| **E3** | \(\mathcal M_X=[P_X^+\cap P_X^-]\) for SLC \(X\). | Added to the five point formulas §2; recovers strict \(\mathcal M\) proof. |
| **E4** | Exact point sets for \(\mathcal D,\mathcal V,\mathcal M\). | Incorporated §2; supersedes historical internal hedging. |
| **E5** | For SLC factors and \(\mathcal R\in\{\mathcal D,\mathcal V,\mathcal M\}\), the relation on the product is the spatial part of the product relation. | Promoted to main theorem §3.2; extended *formally* to \(\mathcal I,\mathcal W\), already exact and spatial. Hence equality iff product spatial. |
| **E6** | \(\mathcal D,\mathcal M\) also exact when one factor stably compact; point relations are patch-closed. | Incorporated with \(\mathcal V\) §6, Jung's Proposition 16 and correct naturality. Local compactness of the point relation is the operative sufficient condition. |
| **E7** | \(\mathcal D_{X\times Y}\) dense in \(\mathcal D_X\times\mathcal D_Y\) for SLC factors. | Incorporated §3.2 using exactness of \(\mathcal W\). |
| **E8** | \(Y_0\) has \(\mathcal V_{Y_0}=Y_0^2\) although \(\mathcal D\) fails product preservation; all five collapse to \(\Delta\) for LCH spaces. | Incorporated §5 and §8 scope caveat. |

The referee's Q1–Q4 are **open research questions**, not consequences of E1–E8. The one substantive new conjectural extension under Q3 (infinite locale products of compact factors) has not been promoted. The referee did *not* certify literature priority.

## D. Addendum A1–A3, independently reconciled

**A1: independent rational-square proof.** The addendum gives the Isbell-density route: embed disjoint dense metrizable copies of \(\mathbb Q\) in a locally compact Hausdorff host (e.g. \(\mathbb Q\) and \(\mathbb Q+\sqrt2\) in \(\mathbb R\)). Their point-induced sublocales meet nontrivially (Isbell's density theorem), although the two underlying sets are disjoint. Pullback of the *closed diagonal* along the localic product of these embeddings supplies a nonempty pointless closed sublocale. Hence \(\mathbb Q_{loc}\times\mathbb Q_{loc}\) is nonspatial, independently of the exact Johnstone proposition number. We accept the argument with Isbell's theorem as a named premise; it is not a claim that disjoint dense point subspaces must meet as *sets*.

**A2: spatiality comparison.** For SLC factors and \(\mathcal R\in\{\mathcal D,\mathcal V,\mathcal M\}\), exactness is equivalent to spatiality of the localic product of their *sober point spaces*. The canonical frame map is from the **frame coproduct** of their opens onto the opens of the ordinary product; it is an isomorphism exactly when the localic product is spatial. The addendum's heuristic “Plewe's game” can now be cited precisely from the user's primary-source paper, Plewe **Theorem 1.1**.

**A3: closed rational/irrational slices.** Accepted: a closed \(\mathbb Q\) or irrational subspace of \(E_{\mathcal R}(X)\) gives a **closed sublocale**, whose product with the rational open test slice is nonspatial. \(X_0\) tests \(\mathcal D,\mathcal V\); \(Y_0\) tests \(\mathcal M\). The closed-into-open order of embedding for \(\mathcal M\) is legitimate: a nonspatial closed sublocale of an open sublocale rules out spatiality of the ambient relation product.

**A3(b) was only a suggestion.** Claims about all Borel or Polish cases were not proved by the addendum; the note correctly warns that \(T_{X_0}\) itself is not metrizable. We replace vague descriptive-set claims with exact cited theorems below, without claiming they settle the general converse.

## E. Direct check of Plewe (1996): exact scope

**Source supplied and read:** T. Plewe, *Localic Products of Spaces*, *Proceedings of the London Mathematical Society* (3) **73** (1996), 642–678, [DOI 10.1112/plms/s3-73.3.642](https://doi.org/10.1112/plms/s3-73.3.642). Relevant numbered statements:

1. **1.1:** a strictly determined two-player game characterizes spatiality/nonspatiality of localic products of two *sober* spaces. This is the correct general-purpose tool for entire nonmetrizable \(T_X\).
2. **1.6 (Isbell):** for completely regular \(S\), the universal spatial-multiplier property is equivalent to every nonempty closed subspace of \(S\) containing a point with a locally compact neighborhood (relative to that closed subspace).
3. **2.2:** for *metrizable* \(S\), being a multiplier for all sober spaces is equivalent to being a multiplier for all metrizable spaces; also equivalent to completeness plus **no closed copy of the irrationals**. The closed-subspace locally compact-point criterion is equivalent as well. Do not confuse a spatial multiplier with a locally compact space.
4. **2.4 (Hurewicz):** a metrizable space is *strongly Baire* precisely when it has **no closed copy of \(\mathbb Q\)**.
5. **2.6:** if metrizable \(A\) is *not strongly Baire* and \(B\) metrizable, \(A\times_{Loc}B\) is spatial **iff** \(B\) is a spatial multiplier. In particular with \(A=\mathbb Q\), *any metrizable non-multiplier* \(B\) gives a nonspatial \(\mathbb Q\)-product.
6. **3.2:** for any finite family of metrizable spaces, nonspatiality is equivalent to closed subspaces with dense embeddings into one Cantor set with empty intersection of their images. This may provide future concrete obstruction certificates.

**Derived strengthening (not blind-audited):** in A3 replace “closed copy of \(\mathbb Q\) or the irrationals” with “closed *metrizable* subspace \(F\) that is *not a spatial multiplier*.” Plewe 2.6 then proves nonspatiality of \(\mathbb Q_{loc}\times \mathrm{Loc}(F)\), so the same \(X_0/Y_0\) strictness follows. By Plewe 2.2 the hypothesis is equivalent to incompleteness of \(F\) **or** existence of a closed irrational copy in \(F\); this is strictly more flexible than the original A3 statement. Mark as **new corollary requiring independent audit** if used in a publication.

**Scope check new in this reconciliation:** since \(\Delta_X\cong X\) sits in each of \(P_X^-,T_X,E_X\), metrizability of a *whole* one of these point spaces implies metrizability (hence \(T_1\)) of SLC \(X\). But SLC \(T_1\) implies locally compact Hausdorff, so all lower relations collapse to \(\Delta_X\). Thus Plewe's metrizable classification is informative on **proper slices** of nontrivial relations, not on the entire nontrivial relation. His game remains available for the full sober spaces. This also corrects the addendum's tentative hedgehog line of thought.

## F. Remaining boundaries and suggested next work

- **Open Q1:** exactness of \(\mathcal W\) for arbitrary locales; equivalent to universal density of \(\mathcal D\) in the product of its factors.
- **Open Q2:** does universal exactness of \(\mathcal V\) over SLC test factors force \(T_X\) locally compact? The Plewe test excludes closed metrizable non-multiplier *slices* but does not decide the nonmetrizable case.
- **Open Q3:** arbitrary infinite locale products, particularly of stably compact factors. Do not confuse them with arbitrary frame products, already settled.
- **Open Q4:** can \(\mathcal D\) have universal SLC exactness but \(\mathcal V\) fail?
- Precise literature citations for the locally compact product theorem, Isbell density theorem, and patch restriction should be maintained before manuscript submission; novelty checking remains entirely separate.

**Outcome:** no headline counterexample was lost; the referee repairs the proofs, expands the all-locales lax/equality range, upgrades strictness to identical-point (pointless) failure, and supplies patch-closed compact-factor exactness for the missing \(\mathcal D,\mathcal M\) branches. Plewe supplies the next concrete test without pretending to resolve the broad converses.
