# Project A — Cross-cutting inventory audit: formal hull, functional reflection, and preservation

**8 November 2026.** Working consolidation, not a blanket new external audit or a novelty judgment. This report cross-checks the repository's 18–24 October foundational, hierarchy, post-\(\mathcal V\), and operation notes against the 21 October and 24 October external referee reconciliations. It adds an elementary **internal deduction** (universal naturality for all named relations), clearly separated below from source-audited results. The source documents and preserved external reports remain authoritative.

## Scope and notation

For \(X\), put \(L=\mathcal O(X)\), \(Q=L\oplus L\). Work in sublocale-inclusion order. Write
\(\mathcal I=\operatorname{cl}\Delta\), \(\mathcal D=\operatorname{fit}\Delta\),
\(\mathcal U=C(d_{\mathcal U})\), \(\mathcal F=\bigwedge_f\ker(f)\),
\(\mathcal V=\operatorname{fit}\mathcal I\), \(\mathcal W=\operatorname{cl}\mathcal D\),
\(\mathcal M=\mathcal I\wedge\mathcal D\), \(\mathcal J=\mathcal I\vee\mathcal D\), and
\(\mathcal H\) the least closed fitted sublocale containing \(\Delta\).
Set \(T(S)=\operatorname{cl}(S)\wedge\operatorname{fit}(S)\).

Verification classes: **E** independently examined with source repairs; **I** complete internally checked proof; **W** proof requiring a focused missing check; **O** open. Results introduced for the first time in *this* report are no more than I, even when their prerequisites are E.

## A. Formal hull and the two diamonds: the supported canonical package

**A1 (E, every locale):**
\[
T(\mathcal J)=\mathcal W\wedge\mathcal V\le\mathcal U\wedge\mathcal V,
\qquad \mathcal W\vee\mathcal V\le\mathcal H\le\mathcal F.
\]
Moreover \(\operatorname{cl}(\mathcal W\vee\mathcal V)=\operatorname{cl}\mathcal V\), and
\(\operatorname{fit}(\mathcal W\vee\mathcal V)=\operatorname{fit}\mathcal W\).
The identity for \(T(\mathcal J)\) uses **finite join preservation** of closure and fitting and the lattice inclusions \(\mathcal I\le\mathcal W\), \(\mathcal D\le\mathcal V\). The 24 October independent referee explicitly checked the coframe argument needed for finite joins of fitted sublocales.

**A2 (E, coherent locales):** In the Priestley patch picture, \(\mathcal H\) is the least patch-closed relation containing the diagonal and saturated under comparability in either coordinate. The ordinary points of \(\mathcal F\) form the least patch-closed equivalence containing the comparability-connected relation. These statements identify *actual* closed spatial spectral sublocales, not merely point sets; the compact-open-filter lemma is essential.
\[
\mathcal H\text{ internally transitive}\iff\mathcal H=\mathcal F
\quad\text{(coherent locales)}.
\]
The two patch-convergent zigzag rays give \(\mathcal U\vee\mathcal V\subsetneq\mathcal H\subsetneq\mathcal F\) and a nontransitive \(\mathcal H\).

**A3 (E, all locales and coherent specializations):** The operator
\[
\kappa(a)=\bigwedge\{x\in Q: w\to x=x\text{ for all }w\text{ with }a\vee w=1\}
\]
is monotone and deflationary and satisfies \(\operatorname{cl}(\operatorname{fit}(C(a)))=C(\kappa(a))\). Its transfinite iteration from \(d_{\mathcal I}\) computes \(\mathcal H\). At limit stages \(a_\lambda=\bigwedge_{\beta<\lambda}a_\beta\) and the stage \(C(a_\lambda)\) is the **closure of the join** of preceding closed stages, not necessarily their bare join. Under coherence, the finite spectral stages are \(\mathcal I_{\mathrm{pt}}^{2n+1}\) (ordinary order-relation powers), and exact first stabilization at \(\omega+m\) occurs for every finite \(m\ge1\). The external 24 October report checked the construction and its off-by-one convention. Do not use unparenthesized **localic** powers outside the separately audited coherent setting.

**A4 (E, negative universal comparisons):** The compact scattered \(T_1\) three-boundary-point space has \(\mathcal D=\Delta\), \(\mathcal I=\mathcal W=\mathcal V=\mathcal H\subsetneq\mathcal U=\mathcal F\), refuting universal \(\mathcal U\vee\mathcal V\le\mathcal H\). In the other direction, the coherent two-ray example refutes \(\mathcal H\le\mathcal U\vee\mathcal V\). The compact scattered \(T_0\) three-boundary-point example has
\[
\Delta\subsetneq\mathcal D=\mathcal M
\subsetneq\mathcal I=\mathcal J=\mathcal W=T(\mathcal J)
\subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F.
\]
In particular **this example has \(\mathcal J=T(\mathcal J)\)**; it only makes \(T(\mathcal J)<\mathcal U\wedge\mathcal V\). This is a previously repaired inventory misstatement that must not recur.

**A5 (I, counterexample beyond coherent scope):** The locally compact sober scattered \(T_1\) double cofinite-cloud/deleted-plank space satisfies \(\mathcal I=\mathcal U<\mathcal F\). Its localic square is fit, hence \(\mathcal H=\mathcal I\) and is internally transitive by the universal \(\mathcal I^2\le\mathcal U\). Thus the converse \(\mathcal H\text{ transitive}\Rightarrow \mathcal H=\mathcal F\) is false in arbitrary locales. This application was recorded **after** the 24 October external audit; the ingredients were reviewed, the assembled statement itself was not.

## B. The functional relation and its categorical meaning

**B1 (standard background plus I proof):** Let \(C(L)\) be the subframe generated by inverse images of all localic maps \(X\to\mathbb R\), and let \(r_X:X\to X_{\mathrm{cr}}=\operatorname{Loc}(C(L))\) be the induced map. Citing Picado–Pultr VI.2.2 for complete regularity and generation, \(r_X\) is the completely regular reflection and
\[
\boxed{\mathcal F_X=X\times_{X_{\mathrm{cr}}}X=\kerpair(r_X).}
\]
Proof: evaluation \(e:X\to\mathbb R^{\operatorname{Loc}(X,\mathbb R)}\) has frame-image \(C(L)\), so factors through \(r_X\) followed by a sublocale monomorphism. Kernel pairs of \(e\) and \(r_X\) are identical. This also gives the internal equivalence property of \(\mathcal F\). It is a categorical identification, not a novelty claim.

**B2 (I, a necessary warning):** \(\mathcal F=\Delta\) iff \(r_X\) is monic, equivalently the inclusion \(C(L)\hookrightarrow L\) is a **frame epimorphism**. Such epimorphisms need not be surjective. Thus \(\mathcal F=\Delta\) does not imply \(L\) completely regular. The source note derives this from the Picado–Pultr strongly Hausdorff but nonregular example; include its primary citation before publication.

**B3 (already in the repository; I/background):** \(d_{\mathcal F}\) has a frame-only generator description by the *completely-below* relation \(a\prec\!\prec b^*\), using Picado–Pultr VI.1.5.2. It belongs in a foundational theorem chapter, but no new proof or literature check is claimed here.

## C. A complete naturality principle (new short internal deduction)

**Proposition C1 (I; every locale map).** For any \(h:X\to Y\) and each
\[
R\in\{\mathcal I,\mathcal D,\mathcal U,\mathcal F,\mathcal V,\mathcal W,
\mathcal M,\mathcal J,\mathcal H\},
\qquad R_X\le (h\times h)^{-1}[R_Y].
\]
In fact the same holds for \(T(\mathcal J)\).

*Proof:* The \(\mathcal I,\mathcal U,\mathcal F\) instances appear explicitly in the foundational note. For \(\mathcal D\), the inverse image of \(\mathcal D_Y\) is fitted (inverse images preserve arbitrary intersections and take open sublocales to opens) and contains \(\Delta_X\), so it contains its fitted hull \(\mathcal D_X\). More generally, inverse image preserves fitting and closedness **as properties**, though not the corresponding hulls as equalities. The \(\mathcal V\) instance follows by applying the fitted-hull universal property to \(\mathcal I_X\le(h\times h)^{-1}\mathcal I_Y\); the \(\mathcal W\) instance by applying the closed-hull universal property to \(\mathcal D_X\). Both \(\mathcal M\) and \(\mathcal J\) are monotone combinations of the already natural \(\mathcal I,\mathcal D\): to show naturality of \(\mathcal J\), one only needs that its inverse image is an **upper bound** for the two relations, not that inverse image preserve joins. Finally \((h\times h)^{-1}\mathcal H_Y\) is simultaneously closed and fitted and contains \(\Delta_X\), so it contains \(\mathcal H_X\). The same hull argument yields naturality of \(T(\mathcal J)\). \(\square\)

**Corollary C2 (I; every binary locale product):** For every such relation
\[
\boxed{R_{X\times Y}\le R_X\times R_Y}
\]
under the coordinate permutation \((X\times Y)^2\cong X^2\times Y^2\). This is obtained from the two product projections. **Only inclusion is universal.** Neither C1 nor C2 should be described as equality/preservation under products.

This extension of the recorded naturality theorem is elementary but has **not** been separately externally reviewed; put it in the inventory as an internally supported proposition rather than assigning E on the strength of older audits covering only \(\mathcal I,\mathcal U,\mathcal F\).

## D. Disjoint unions and products: what is actually preserved

**D1 (I, arbitrary locale disjoint unions):** For \(X=\coprod_i X_i\), each of the nine named relations is supported on the diagonal component blocks \(X_i^2\subset X^2\), vanishes on \(X_i\times X_j\) for \(i\ne j\), and restricts to the corresponding \(R_{X_i}\) on each diagonal block. The proof uses the clopen block decomposition \(X^2=\coprod_{i,j}X_i\times X_j\), componentwise sublocale closure/fitting, and for \(\mathcal F\) component-separating real-valued functions. It is consistent with the October 21 independent audit of the special \(\mathcal I=\mathcal U\) class and the October 21 hierarchy preservation note, but the **all-relations package was not commissioned as a separate audit**. Thus equality of a relation with its own hull is stable under disjoint union whenever the equality is checked componentwise.

**D2 (I; coherent/spectral binary products):** The records support genuine localic product equality for \(\mathcal I,\mathcal D,\mathcal U,\mathcal V\), and the same argument supplies \(\mathcal F\):
\[
R_{X\times Y}=R_X\times R_Y\qquad
(R\in\{\mathcal I,\mathcal D,\mathcal U,\mathcal V,\mathcal F\},\ X,Y\text{ coherent}).
\]
For \(\mathcal I,\mathcal D\), common-upper/common-lower-bound tests factor coordinatewise; for \(\mathcal U,\mathcal V\), their length-four order-zigzags factor coordinatewise. For \(\mathcal F\), if \((x,x')\in\mathcal F_X\) and \((y,y')\in\mathcal F_Y\), then any continuous real \(f:X\times Y\to\mathbb R\) has \(f(x,y)=f(x',y)=f(x',y')\), using the two coordinate slices, and conversely use projection-pulled-back real maps. These point relations correspond to the actual named spectral/spatial sublocales via the previously checked compact-open-filter lemma. This is an internally consolidated extension of the 21 October product note; do **not** cite the 21 October coherent audit as independently verifying every product comparison.

In the coherent class \(\mathcal W=\mathcal U\), so \(\mathcal W\) also commutes with binary products. The same applies to \(\mathcal M=\mathcal I\wedge\mathcal D\) by meet/product compatibility. We make **no** product-equality claim for \(\mathcal H\) or \(T(\mathcal J)\) here.

**D3 (I; finite counterexample: \(\mathcal J\) is not product-preserving):** Let \(P=\{a,b,t\}\) with \(a<t,b<t\), and \(Q=\{o,r,s\}\) with \(o<r,o<s\), both with upper-set topology. In \(P\), \(\mathcal I_P=P^2\) but \(\mathcal D_P\) omits \((a,b)\); in \(Q\), \(\mathcal D_Q=Q^2\) but \(\mathcal I_Q\) omits \((r,s)\). Hence \(\mathcal J_P=P^2\) and \(\mathcal J_Q=Q^2\), but the pair \(((a,r),(b,s))\) in \((P\times Q)^2\) belongs to neither \(\mathcal I_{P\times Q}\) nor \(\mathcal D_{P\times Q}\). Thus
\[
\boxed{\mathcal J_{P\times Q}\subsetneq\mathcal J_P\times\mathcal J_Q=(P\times Q)^2.}
\]
In fact the earlier 21 October note checks that \(T(\mathcal J_{P\times Q})=(P\times Q)^2\): both \(\mathcal I^2\) and \(\mathcal D^2\) are full in that product. Consequently the class \(\mathcal J=T(\mathcal J)\) is **not** closed under binary frame coproducts, even among finite coherent frames. This exposes the flaw in applying positive product preservation of \(\mathcal I\) and \(\mathcal D\) to their **join**.

**D4 (open/closed sublocales and frame maps):** Previously audited classifications remain in force: \(\mathcal I=\mathcal U\) is open-hereditary but not closed-hereditary; \(\mathcal D=\mathcal U\) is closed-hereditary but not open-hereditary. The \(\mathcal I=\mathcal U\) class is closed under arbitrary frame products and frame coproducts but not under arbitrary subframes or surjective frame quotients. The unrestricted frame-coproduct stability of \(\mathcal D=\mathcal U\) is **open**, though coherent and some continuous cases are covered. These are class-preservation results, separate from equality of the named relations under a locale product.

## E. Critical boundaries and outstanding verification

1. **Source of \(\mathcal F\).** The complete-regularization kernel-pair description is grounded in Picado–Pultr VI.2.2 plus an internally given categorical proof; verify exact hypotheses against the monograph before a standalone manuscript.
2. **Categorical naturality.** The new C1 proof is short and uses standard inverse-image properties, but has not been in a referee packet. Retain I status.
3. **Products.** Keep separate **natural comparison** C2, **coherent spectral equality** D2, and **finite failure for \(\mathcal J\)** D3. Do not generalize D2 to arbitrary noncoherent locale products without a proof of the required localic image and hull behavior.
4. **\(\mathcal H\) transitivity.** Coherent \(\mathcal H\) transitive iff \(\mathcal H=\mathcal F\) is independently supported; the scattered noncoherent counterexample A5 was derived afterward and merits a short targeted review.
5. **Limit ordinals.** Keep the closure at limit stages in the \(\kappa\)-iteration; do not automatically replace it by a join of sublocales.
6. **No new \(\mathcal V_2\) research.** Its potential conceptual role is recorded only as a deferred consideration.
7. **Next inventory segment:** Properness/effectiveness of closed equivalence relations, the Scott-continuity converse, and separation of spatial versus genuinely localic quotient statements. Those notes include a known record-level status contradiction; reconcile it against the actual proof rather than relabeling from memory.

## Source map

- [Foundational relations and original functoriality of I,U,F](https://github.com/mkkinyon/locales/blob/main/A-hierarchy-first-results.md)
- [Functional relation and completely regular reflection](https://github.com/mkkinyon/locales/blob/main/A-equality-characterizations.md)
- [V-hierarchy and preservation overview](https://github.com/mkkinyon/locales/blob/main/A-V-relation-hierarchy-duality-preservation-2026-10-21.md)
- [Finite J fixed-point and product counterexample](https://github.com/mkkinyon/locales/blob/main/A-J-fixedpoint-compositions-coproduct-2026-10-21.md)
- [Post-V formal hierarchy and transfinite hull](https://github.com/mkkinyon/locales/blob/main/A-postV-consolidation-2026-10-24.md)
- [Independent post-V reconciliation, authoritative repairs](https://github.com/mkkinyon/locales/blob/main/A-postV-external-audit-reconciliation-2026-10-24.md)
- [Noncoherent H-transitivity counterexample (post-audit deduction)](https://github.com/mkkinyon/locales/blob/main/A-H-transitivity-noncoherent-counterexample-2026-10-24.md)
- [Arbitrary frame products/coproducts for I=U](https://github.com/mkkinyon/locales/blob/main/A-closure-properties-I-U.md)
- [Independent October 21 audit](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md)

**Repository status:** No edits committed. Preserve earlier blind reports verbatim.