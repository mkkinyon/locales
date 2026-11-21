# Project A — internal adversarial audit: scattered targets and graph-extension stability
## 21 November 2026 · pre-external review

**Materials reviewed directly:** [Scattered targets](ProjectA_SCATTERED_TARGET_UNIVERSAL_POINT_COVERS_AND_GRAPH_ALGEBRA_2026-11-21.md); [HSIS necessity and Boolean probes](ProjectA_HSIS_NECESSITY_TWO_COLOR_BOOLEAN_PROBES_2026-11-21.md); [compact-boundary and graph-extension criterion](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md); [separately refereed rectangular baseline](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md).

**Verdict: PROVISIONAL INTERNAL PASS, EXTERNAL AUDIT ESSENTIAL.** No fatal defect found in the Cantor–Bendixson point-cover argument, the compact-Hausdorff non-scattered witness, or the abstract graph-extension criterion after checking the key categorical steps. The **scatteredness ↔ point-cover stability** theorem is internally supported. The **universal graph-algebra safety** dichotomy relies on the **new, not independently audited HSIS ⇒ associative graph-extension theorem**, and must not be promoted as externally verified. The Level-2 ⇒ Level-3 converse and global HSIS necessity remain open.

### 1. Foundational checks

1. **Regular ⇒ Fit and fit ⇒ every sublocale fitted: PASS.** The ambient open-separator proof does not equate density with closure. Igor Arrieta, *Topology and its Applications* 342 (2024), 108785, §2.3 explicitly states Regular ⇒ Fit and equivalence of fitness to every sublocale being fitted.
2. **Localic sublocale inverse-image preserves arbitrary meets and finite joins: PASS.** Arrieta–Suarez, *The coframe of D-sublocales of a locale and the T_D duality*, describes inverse-image on sublocales as a coframe homomorphism. This supports finite open/closed gluing and finite-sheet selected-image covers; it does not justify arbitrary-join distribution of relation composition.
3. **Images of point-generated sublocales: PASS.** Localic image preserves arbitrary joins of point sublocales. It need not be stable under arbitrary pullback.
4. **Compact-Hausdorff spatial multiplier and closed graph: STANDARD INPUT, CHECK EXPLICITLY IN BLIND REVIEW.** The closed graph of f, spatiality of a product with compact Hausdorff X, and spatiality of closed sublocales justify the claimed exact inverse-image and point-generated rectangular actions. This is the highest-risk structural step.
5. **Nonzero middle locale is overt classically: PASS WITH CLASSICAL LOGIC.** No ordinary point of a pointless nonzero middle is chosen.

### 2. Cantor–Bendixson universal point-cover proof

**PASS.** For a scattered sober Y, write Y^(α) for transfinite derivatives, U_α=Y\Y^(α) (open), and L_α=Y^(α)\Y^(α+1). The layer L_α is discrete and is *closed relative to U_(α+1)*. For arbitrary locale h:T→Y, the pulled-back closed layer splits as a coproduct of point fibers T_y; the open part U_α and this closed layer form a **finite complementary open/closed join** inside U_(α+1). Limit stages use only preservation of arbitrary joins of open sublocales. Thus all point fibers cover T at the terminal derivative stage, even when T is pointless. A point-surjective e:S→Y receives a factor from the canonical discrete point cover (classical choice), hence is pullback-stably surjective.

**Presentation repair:** State clearly that L_α is closed only *inside* U_(α+1), and the open/closed decomposition is performed after pulling back to that open sublocale. Do not call the singleton fibers an open cover of all Y.

### 3. Non-scattered Hausdorff converse

**PASS.** A non-scattered Hausdorff Y has a nonempty crowded closed K, by taking the closure of a nonempty subspace without isolated points. Its least dense sublocale B(K) is nonzero but has no ordinary points, because it is contained in each dense open K\{k}. Pulling the canonical discrete point cover back along B(K) gives 0→B(K), so the point cover is not pullback-stable.

**Literature and novelty caution:** This sits near Simmons' scatteredness/sublocale theorem. No priority claim should be made.

### 4. Compact-Hausdorff universal graph-safety dichotomy

**CONDITIONAL PASS.** Positive: if compact Hausdorff Y is scattered, every selected target D=f(E) is scattered Hausdorff; the selected-image map [E]→D hits every ordinary point and therefore has HSIS by §2. Apply the still-unrefereed graph-extension sufficient criterion.

Negative: if compact Hausdorff Y is non-scattered, choose a nonempty perfect closed K. Classical resolvability gives disjoint dense Q,I⊂K. Take Z=β(Q_discrete), X=Y×Z and f the open/proper projection to Y. The selected discrete set E={(q,q):q∈Q} maps onto Q; pulling [I] back to [E] gives zero while [Q]∧[I] contains B(K)≠0. The rectangle–converse-graph–rectangle probe consequently has distinct bracketings. This proves failure of universal projection safety (and thus graph safety).

**External reference requirement:** For nonmetrizable K, state and cite exactly the classical resolvability result needed (crowded compact Hausdorff spaces have two disjoint dense subsets). It is documented in the standard Hewitt/resolvability literature; a survey also states that crowded countably compact regular Hausdorff spaces are ω-resolvable. For compact metric K, the countable-dense/simultaneously co-dense construction is elementary.

### 5. Abstract graph-extension sufficient criterion

**CONDITIONAL PASS, TOP EXTERNAL AUDIT PRIORITY.** For surjective compact-Hausdorff f:X→Y with g=Γ_f, inverse graph, K_f=X×_YX, assume every selected-image e_E:[E]→[f(E)] is pullback-stably surjective.

- For p(A,B)=[A×B], the claimed action along inverse graph and K_f uses a path locale which is a **closed sublocale of p(A,B)×X**. This product is spatial because X is compact Hausdorff. A closed sublocale is spatial, and its image is generated by ordinary endpoint pairs. The p-action is therefore precisely p(A,f^-1 B) or p(A,f^-1 f(E)), not merely an unknown sublocale between p and q.
- For q(A,B)=[A]×[B], stable surjectivity of e_E and of its product/base changes ensures the image side is a **full q** rectangle. The inverse-image side uses the closed-graph/spatial-multiplier equality f^-1([B])=[f^-1(B)], which is automatic in this setting.
- The pure graph relations Δ_X, Δ_Y, g, g^smile, K_f form a finite typed multiplication table. Mixed three-factor associativity reduces to their exact p/q actions and overlap reciprocity [f(E)]∧[B]≠0 iff [E]∧f^-1([B])≠0. It follows from HSIS.
- Only **finite** join distribution is invoked. No blanket associativity of arbitrary localic relations is claimed.

**Precise referee challenges:** Check the *actual* closed-pullback description for the K_f p-action; check spatial multiplier theorem and image of closed sublocale; verify all p/q type cases with nonspatial endpoint products; check typed zero and identity cases. Failure here would affect the positive graph-algebra classification but **not** the standalone scatteredness ↔ canonical-point-cover theorem.

### 6. Inclusion probes, Boolean supports and amplification

**PASS AS A BOUNDED REDUCTION; OPEN PROBLEMS UNCHANGED.** In a compact Hausdorff target, every sublocale V is the join of Booleanizations B(K) for the nonempty compact closed supports K with B(K)≤V; the ambient fitness argument supplies any missing closed support. Nonzero pullback tests on these Booleanizations detect *inclusion-base-change surjectivity*. Ordinary selected-support overlap probes are strictly weaker for a **fixed selected subset E**, as seen using the discrete point map of Cantor space: the pointless B(Cantor) base change fails while ordinary B-point probes pass.

The exact categorical product-amplification identity remains valid: universal pullback stability of e is equivalent to inclusion-stability of e×id_T for **every** locale T, since an arbitrary map h:T→V is embedded by its graph into V×T. This does not prove Level 2 ⇒ Level 3 or global necessity of HSIS.

### 7. Recommendation and blindness protocol

**Internal verdict:** favorable but conditional on explicit graph-extension structural checks. Prepare a single adversarial **blind** external packet containing:
1. the precise hypotheses and self-contained scattered-point-cover induction;
2. the non-scattered Booleanization converse and the universal target dichotomy;
3. the full HSIS⇒associative rectangular+graph algebra proof, with the spatial closed-path lemma highlighted;
4. the nonmetric resolvability input and metric special case;
5. a foundational appendix giving the separately reviewed finite rectangular composition rule, as a mathematical statement with proof rather than an appeal to prior verdict;
6. explicit boundaries: no Level 2⇒Level 3, no global necessity of HSIS, no claim about all nonrectangular relations or constructive locales.

**Do not provide this internal audit or verdict to the referee.** After receiving an independent referee report and optional addendum, reconcile results and update the repository before the planned later big-picture session.
