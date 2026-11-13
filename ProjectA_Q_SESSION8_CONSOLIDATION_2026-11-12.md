# Project A — Session 7 to Session 8 Q-program consolidation

> **Historical status notice (13 November 2026):** The independent blind report and subsequent source check have completed. Read the [post-referee mathematical reconciliation](ProjectA_Q_POSTREFEREE_RECONCILIATION_2026-11-13.md) and [updated priorities](ProjectA_Q_POSTREFEREE_PRIORITIES_2026-11-13.md) first. In particular, the Cohen Boolean base × Arrieta **closed** W/W₂/U test described below as open was settled positively by referee-derived Boolean-base splitting N3. Only its nonclosed D product equation remains open. The 12 November proof inventory is retained below unchanged for provenance; **Q and Q′ remain OPEN**.

**12 November 2026.** This is a consolidated map of recent working mathematics, not a new external certification. Its source of truth is the theorem-by-theorem working documents in `mkkinyon/locales`. The old Project A ledgers and status index retain historical provenance. **Q and Q′ remain open.**

## 1. Fixed notation, questions, and logical dependencies

Let `L=O(X)`, `P=L⊕L=O(X²)`. For a cover `C⊆L`, put `w_C=∨_{c∈C}(c⊠c)`. Define the inflationary, meet-preserving pre-nuclei

`Φ(q)=∨_{C cover}(w_C→q)`, `Φ₂(q)=∨_{F finite cover}(w_F→q)`.

The rank-zero identity is `z=Φ(0)=Φ₂(0)=d_U=∨{a⊠b:a*∨b*=1}`. Write `d=Φ₂^∞(0)` for the least Φ₂-fixed element above 0, so `D₂` is the finite fitted diagonal, `W₂=cl D₂=C(d)`; similarly `D,W` use all covers. `I=cl Δ` and `U=C(z)`. The chains `D⊆D₂⊆W₂⊆U` and `W⊆W₂` are baseline.

**Q (rank one):** `Φ₂(z)=z ⇒ Φ(z)=z`, equivalently `W₂=U ⇒ W=U`. **Q′ (full closed-hull):** `W₂=W` for all locales. Q′ would imply Q, but proof of Q would not settle Q′. Neither is known universally.

For a chosen cover C and any Φ₂-fixed d, the *strong relatively open hole* is `E_C=C(d)∧O(w_C→d)`. At `d=d_{W₂}`, `E_C>0` is equivalent to Q′ failure. At `d=z` assuming Φ₂(z)=z, it tests Q. The *weak closed relative defect* `T_C=D₂∧C(w_C)` may be nonzero even if `E_C=0`. The externally reviewed formula `E_C=int_{W₂} cl_{X²}(T_C)` applies at `d=d_{W₂}`. Keep these notions distinct.

## 2. Group A: cover calculus and necessary obstructions

**Local finiteization.** Every locally finite cover C satisfies `(w_C→q)≤Φ₂(q)` for every q. For the locally finite locus `ℓ_C=∨_{F finite}(∨(C\F))*` and closed tail-accumulation remainder `H_C=C(ℓ_C)`, the same bound holds after intersecting either coordinate strip over ℓ_C. Compact H_C gives the two-step estimate `(w_C→q)≤Φ₂²(q)` for every q. The regular-H_C finite-fixed conclusion depends on separately established one-sided regular closed rigidity and must be audited with that dependency in view. Under locally finite refinements of all covers, `Φ=Φ₂` pointwise.

**Chromatic finiteization.** If a rectangle r is killed modulo a closed relation's defining open d by an arbitrary cover C, `r∧w_C≤d`, form its cross-link graph Γ on C by cross-rectangles still linked modulo d. A finite coloring of Γ gives `r≤Φ₂(d)`; a cover of the coordinate locale by opens seeing locally finite-chromatic induced graphs does likewise. With `η_{C,r}` the corresponding open locus, `Hχ=C(η)` is a smaller closed support than H_C. Compact Hχ yields `r≤Φ₂²(d)`; regular Hχ and finite-fixed d exclude r as a hole using one-sided rigidity. A genuine finite-fixed hole forces locally infinite chromaticity on its reduced coordinate support. No converse is claimed.

**Baire/scattered extensions.** For hereditarily Baire spatial X, ordinarily point-finite covers are compatible with all finite-compatible generalized pairs. A closed spatial T₁ support of a bad pair can be repeatedly stripped of isolated points; the defect must remain on its Cantor–Bendixson perfect kernel. The proofs use classical Baire, arbitrary target frames, and one-sided compact/regular rigidity for the final exclusion. The claimed locally compact sober metacompact positive class is conditional on the ambient hereditary-Baire assertion as used in the proof. These add positive classes, not universal solutions.

## 3. Group B: localic products and span methods

**Universal (classical Set) product formulas:** `U(Z×Y)=U(Z)×U(Y)` and `I(Z×Y)=I(Z)×I(Y)` for arbitrary locales, from rectangle pseudocomplements, nonzero product rectangles and the closure-of-products calculation. The same equality is **not** claimed universally for D, D₂, W or W₂.

**Closed-hull transfer.** If `W₂(Z)=I(Z)` and Y is compact, exact `W(Z×Y)=W₂(Z×Y)=I(Z)×W(Y)` follows from a point-free compact-fiber tube-cover identity. Compact clopen covers of Y suffice by gluing. A different route works for noncompact Y when generalized common-predecessor spans are dense in W₂(Y), with `Σ(Y)` the join of their images: `cl Σ(Y)=W₂(Y)` implies W=W₂ on Y, and exact product transfer over any such Z. If Z is a nonempty spatial factor with W₂(Z)=Δ_Z, closed-hull fiberwise product formulas hold for arbitrary Y by point slices; when U(Z)=Δ_Z this also gives exact U transfer and Q/Q′ preservation/reflection, with a marked cover-hole descending on an open set of fibers.

**Nonnecessity of span density.** Arrieta's spatial strongly Hausdorff anti-Urysohn locale A is a control with `I(A)=Σ(A)=Δ_A`, but `W(A)=W₂(A)=U(A)=A²`. This blocks an attempted universal predecessor criterion. The cited external construction/topological properties are dependencies, not independently reproved in the recent notes.

**New distributive Boolean base mechanism.** For a complete Boolean algebra M satisfying strong `SD_κ` (common partitions refining any family of at most κ partitions, even when individual partitions have arbitrary cardinalities), let Z=Loc(M), and let Y have a frame basis of cardinality at most κ. The internal argument proves the stronger nonclosed formulas `D_ε(Z×Y)=Δ_Z×D_ε(Y)` for ε full or finite, hence exact W, W₂, U products. The proof localizes arbitrary product covers by basis coefficients and a single common Boolean partition. A σ-closed atomless Boolean completion provides a pointless `SD_ω` base; with the asserted countable base of Arrieta A, this yields a Q-positive product not explained by predecessor spans. **This is a top-priority independent audit target.** In contrast, the Cohen/RO(Cantor) Boolean base is not SDω and its product with A remains an actual open test.

## 4. Group C: Boolean lower selections and coherent envelope

**Gleason/patch selection.** For frame maps h,k:L→M with M complete Boolean and all finite covers matched, an ordinary bounded distributive-lattice predecessor `p_fin:L_lat→M` exists below h,k: work over the Stonean space Stone(M), the compact patch spectrum of finite prime filters of L_lat, and a closed common-lower-point relation; use Gleason projectivity. This predecessor is *not generally a frame map*. If an infinite C-cover is matched to zero, every such p_fin sends each c∈C to zero but sends their join 1 to 1. For coherent L, use the **compact-element lattice K(L)** in place of L_lat and extend the selection from K(L) to L=Idl(K(L)); this gives a genuine frame predecessor. Choice, ordinary Boolean ultrafilters, finitely vs completely prime filters, and preservation of arbitrary joins are essential distinctions.

**Coherent envelope.** Let `Lhat=Idl(L_lat)`, `j(a)=↓a`, `ε(J)=∨J`; then ε is a surjective frame map with ε⊣j and εj=id. The induced sublocale X↪Xhat has `D₂(X)=D(Xhat)∧X²` (actual pullback); since Xhat is compact and coherent, this is full fitting there. For an X-cover C, `uhat_C=∨_{c∈C}↓c` is proper exactly when C has no finite subcover; its closed complement `R_C` is disjoint from X. Selected p_fin frame-extends on Lhat and lands in R_C when all C matching values vanish. Such a spectral ghost alone does not indicate a Q failure.

**Contact localization (last result of Session 7).** For a,b∈L let `K(a,b)=C_X(a*∨b*)=cl O(a)∧cl O(b)`. With `G_C(a,b)=R_C∧cl O(j(a))∧cl O(j(b))`, the principal-ideal equality `j(a)*=j(a*)` gives

`G_C(a,b)>0 ⇔ a*∨b*∨∨F ≠1` for **every finite** `F⊆C`.

If `G_C(a,b)=0`, then for **every q**,

`(a⊠b)∧(w_C→q)≤Φ₂(q)`.

Compact K(a,b) forces G=0. Thus a rank-one Q-hole under finite stabilization requires a disjoint U-linked rectangle whose contact core is noncompact and has persistent G>0. **Not sufficient:** for B=Loc(RO(Cantor)), P the six-point upper-Alexandrov fence `0<5>1<4>2<3`, the product B×P is Q-positive (`W=W₂=U`) but has a U-linked disjoint rectangle a=1_B×↑0, b=1_B×↑4 with noncompact K=B×{1}; an infinite Boolean antichain cover even gives `G_C(a,b)>0` while the actual rank-one hole remains zero.

## 5. What failed, what remains to audit, and next bounded target

- **Do not infer an open U-hole** from a nonzero weak defect, spectral ghost, atomless/nowhere-distributive Boolean target, infinitely chromatic linking, noncompact frontier, or a selected finitely prime lower point. All have known Q-positive negative controls.
- **Do not assume closed heredity of the rank-one hypothesis.** The marked Q-hole survives its least closed support reduction with local rank-one stabilization, but global `Φ₂,K(z_K)=z_K` need not follow; a generic-point extension shows global rank-one finite stabilization is not closed hereditary.
- **Do not infer Q from the envelope identity.** It is a trace statement; closure and restriction to X² do not commute in general.
- **Proof priorities for the blind referee:** strong-SDκ arbitrary-cover product localization; localic tube-cover and closed-hull transfers; universal Boolean predecessor and coherent frame upgrade; coherent-envelope pullback and contact theorem; chromatic/compact frontier and Baire assumptions; and whether the nonregular pointless controls genuinely satisfy every claimed relation.
- **After the audit:** the concrete Cohen-Boolean-base × Arrieta A rank-one calculation, or a direct algebraic argument extracting *relative openness* from rank-one finite stabilization, is preferable to another list of necessary spectral hypotheses.

## 6. Provenance and scope

The **12 November Q′ first-step hole/support-reduction theorem** has undergone an independent blind review with a corrected intermediate inequality and explicit reconciliation; that previous report does **not** certify the newer November 12 product, Gleason, chromatic, Baire or spectral claims. This consolidation is not a literature-priority assessment. Its proof sources are the `ProjectA_Q_*_2026-11-12.md` notes and `project-a/audits/2026-11-12/Qprime-prenucleus-internal/` in the repository. The separately prepared internal audit grades those dependencies one by one; its verdict must not be shown to a blind referee before the referee finishes.