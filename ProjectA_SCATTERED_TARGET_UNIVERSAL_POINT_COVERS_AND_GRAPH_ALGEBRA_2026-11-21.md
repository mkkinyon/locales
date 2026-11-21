# Project A — scattered targets, universally stable point covers, and graph-extension dichotomy
## 21 November 2026 · New INTERNAL theorem segment, not independently audited

**Project status.** This note continues the internally developed HSIS necessity/probe hierarchy in [the two-colour/Boolean support note](ProjectA_HSIS_NECESSITY_TWO_COLOR_BOOLEAN_PROBES_2026-11-21.md) and the [selected-image graph-extension criterion](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md). The finite point-generated/full rectangular algebra on compact Hausdorff spaces **is** independently blind-refereed in the [post-referee canonical note](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md); the later graph-extension criterion and all current results remain **internal**. No originality/priority claim. Classical Loc and classical choice throughout.

## 1. Pointwise-surjective locale maps are stably surjective under spatial base change

**Lemma 1.1.** Let e:S→V be a map of locales with spatial V, and assume e is surjective on ordinary points. For every **spatial** locale T and map h:T→V, the projection
\[
S\times_VT\longrightarrow T
\]
is surjective in Loc.

**Proof.** Every ordinary t∈T maps to v=h(t)∈V. Choose s∈S with e(s)=v. By the universal property of the localic pullback, (s,t) gives an ordinary point of S×_VT mapping to t. Thus the pullback projection is point-surjective; because T is spatial, its image must be all of T. No compactness, regularity, or product-spatiality assumption is needed.

**Consequence.** Each selected map \(e_E:[E]\to[f(E)]\) in our compact Hausdorff graph problem is automatically stable under all **spatial** base changes, including compact metrizable Hausdorff test spaces. A witness to failure of full HSIS must have a **nonspatial base-change target**. This does not say the source of the corresponding pullback is spatial.

## 2. Universal stability of the canonical point cover of a scattered space

For a space Y (sober, so it represents the intended spatial locale), put
\[
p_Y:\coprod_{y\in Y}1_y\longrightarrow Y,\qquad
y\mapsto y.
\tag{PC}
\]
The domain is the discrete locale on the underlying point set, possibly very large.

**Theorem 2.1 (new internal Cantor–Bendixson induction).** If Y is **scattered** (every nonempty subspace has an isolated point), then \(p_Y\) is a pullback-stable locale-surjection. Hence **every pointwise-surjective locale map e:S→Y is pullback-stably surjective**.

**Proof.** Fix an arbitrary locale map h:T→Y, with T possibly nonspatial. Let
\(
T_y=T\times_Y\{y\}\le T
\)
and J=∨_{y∈Y} T_y, the image of the pullback of (PC).

Define the transfinite Cantor–Bendixson derivatives Y^(α): Y^(0)=Y; Y^(α+1) is the set of points not isolated in Y^(α); Y^(λ)=∩_{α<λ}Y^(α) at a limit. Every Y^(α) is closed in Y. Put \(U_\alpha=Y\setminus Y^{(\alpha)}\), an **open** subspace of Y, and \(L_\alpha=Y^{(\alpha)}\setminus Y^{(\alpha+1)}\), a discrete subspace of Y^(α).

Claim: the pulled-back open sublocale h^-1(U_α) lies in J for all α.

- α=0: U_0=∅.
- Successor: inside U_(α+1), the open U_α and the relatively closed complement L_α cover by a **finite open/closed sublocale join**. By induction h^-1(U_α)≤J. The map from h^-1(L_α) to the **discrete** space L_α splits as the coproduct of its fibers T_y for y∈L_α, so h^-1(L_α)≤J. Hence h^-1(U_(α+1))≤J.
- Limit λ: U_λ=∪_{α<λ}U_α, an increasing union of ordinary opens. Locale inverse image **preserves arbitrary joins of opens**, so h^-1(U_λ)=∨_{α<λ}h^-1(U_α)≤J. This is *not* an unrestricted infinitary distributivity claim about sublocale pullback or relation composition.

Because Y is scattered, some derivative Y^(γ) is empty. Thus U_γ=Y and J=T. As h was arbitrary, p_Y is pullback-stably surjective.

If e:S→Y hits every ordinary y, choose for each y an ordinary point s_y∈S over y. These points determine a map p_Y→S over Y. Under any base change, p_Y factors through the pullback of e; since the former is surjective, so is the latter. □

**Examples.** A convergent-sequence compactum Y=ω+1 is scattered, so the identity-on-points map \(Y_{\rm disc}\to Y\) is stably surjective although it is neither open (the isolated point ∞ of the **domain** has non-open singleton image) nor proper (the inverse image of compact Y is infinite discrete noncompact). Thus open/proper maps are *sufficient*, but far from exhaustive, sources of stable surjections.

## 3. Converse and exact characterization of the canonical point cover

**Theorem 3.1 (internal).** For a **Hausdorff** space Y, these conditions are equivalent:
\[
\boxed{
\begin{gathered}
Y\text{ is scattered};\\
p_Y:Y_{\rm disc}\to Y\text{ is pullback-stably surjective};\\
\text{every map of locales }S\to Y\text{ that is point-surjective is pullback-stably surjective}.
\end{gathered}}\tag{SCAT}
\]

**Proof.** The forward implication is Theorem 2.1; the third implies the second. If Y is not scattered, choose a nonempty subspace with no isolated points and let K be its closure. In Hausdorff Y the closed space K is nonempty and perfect (no isolated points): if k were isolated in K, its singleton relatively open would intersect the dense no-isolated subset, making an isolated point there.

The least dense Booleanization \(\mathcal B(K)\) is a **nonzero pointless** sublocale of K: for each k∈K, K\{k} is open dense and contains \(\mathcal B(K)\), so no point sublocale of \(\mathcal B(K)\) exists.

Pulling p_Y back along the sublocale inclusion \(\mathcal B(K)\hookrightarrow K\hookrightarrow Y\) gives the coproduct of its ordinary point fibers; each is zero because \(\mathcal B(K)\) is pointless. Hence the pulled-back map is 0→\(\mathcal B(K)\ne0\), contradicting pullback stability. □

**Fixed-selection consequence.** The Stone–Čech example from the preceding HSIS note is a special instance: for non-scattered compact Y, the canonical point-cover map passes *every spatial* base change and every **ordinary point-generated overlap test with target [Y]**, but fails the Booleanized closed-support test at \(\mathcal B(K)\). The gap between Levels 1 and 2 for a fixed selection is therefore widespread rather than particular to Cantor space.

**Related literature, not an identical claim.** Simmons' scattered-space/sublocale correspondence is treated in Anna Laura Suarez, *Revisiting the relation between subspaces and sublocales* (arXiv:2010.05284). The theorem above focuses on *universal stability of the canonical point cover* and follows directly from Cantor–Bendixson open/closed gluing; no literature priority is asserted.

## 4. Hereditary selected-image stability is automatic over scattered targets

**Corollary 4.1 (internal).** Let Y be **scattered Hausdorff** and f:X→Y any continuous map from a Hausdorff space X. Then for every ordinary E⊆X, the selected map
\[
e_E:[E]\to[f(E)]
\]
is pullback-stably surjective. In particular, **HSIS(f) holds**.

**Proof.** D=f(E) is a Hausdorff scattered subspace of Y, hence sober and spatial. The selected map is point-surjective onto D by construction. Apply Theorem 2.1 to the scattered target D. There is no requirement that E be closed, locally compact, or compact; no bound on f's fiber cardinalities is used. □

**Corollary 4.2 (conditional only on the prior internal graph-extension theorem).** Let Y be compact scattered Hausdorff and X compact Hausdorff. For every continuous **surjection** f:X→Y, the finite-join/composition algebra on X⊔Y generated by all point-generated/full rectangles, \(\Gamma_f,\Gamma_f^\smile\), and \(\Delta\) is associative.

**Reason.** Corollary 4.1 supplies HSIS(f); the earlier [one-condition graph-extension criterion](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md) then applies. The independent referee established the base rectangular algebra, but the graph-extension criterion itself has not undergone external audit.

This subsumes all locally stratified singleton-boundary examples when their target is compact scattered, and gives positive graph-algebra examples with arbitrary compact source fibers and maps that are neither open nor locally finite-to-one.

## 5. A universal compact-Hausdorff target-space dichotomy

Call compact Hausdorff Y **universally projection-safe** when for **every compact Hausdorff** Z, the projection f:Y×Z→Y has an associative finite rectangular algebra enlarged by its graph and converse. Call it **universally graph-safe** if the same holds for *every* continuous surjection f:X→Y from compact Hausdorff X.

**Theorem 5.1 (internal, with a classical topological input).** For compact Hausdorff Y, the following are equivalent:
1. Y is scattered.
2. Y is universally graph-safe.
3. Y is universally projection-safe.

**Proof.** (1)⇒(2) is Corollary 4.2; (2)⇒(3) is immediate. For (3)⇒(1), suppose Y non-scattered. Choose a nonempty **perfect closed** subset K⊆Y (the closure of any nonempty crowded subspace). The classical Hewitt **resolvability theorem** for crowded locally compact Hausdorff spaces supplies disjoint ordinary subsets Q,I⊂K **both dense in K**. A reference stating this classical input explicitly is Dontchev–Ganster–Rose, *Ideal Resolvability*, §1, quoting Hewitt (1943).

Let Z=β(Q_discrete), the Stone–Čech compactification of the **discrete set Q** (its topology as a subset of K is not used in this construction). Each q∈Q is an isolated point of Z. Put X=Y×Z and f=projection to Y. This map is continuous, **open proper surjective**, with compact Hausdorff source.

Define the selected subset \(E=\{(q,q):q\in Q\}\subseteq X\), using the canonical discrete copy of Q in Z. The second coordinate isolates every point, so [E] is a **discrete** locale. Its image under f is Q. Since Q,I are separately dense in the nonempty compact closed K, their induced sublocales satisfy
\[
[Q]_Y\wedge[I]_Y\ge\mathcal B(K)\ne0.
\]
But the pullback \([E]\times_Y[I]\) is zero: each ordinary q∈Q misses I and the discrete source [E] is the coproduct of its singleton points. Therefore for a singleton-legged rectangle R=p({u},I) and T=p(E,{v}), with u∈Y and v∈X arbitrary, and the converse graph \(F=\Gamma_f^\smile\),
\[
(R\circ F)\circ T=0,\qquad R\circ(F\circ T)=\{(u,v)\}\ne0.
\]
Thus the enlarged algebra of the **open proper projection** f is nonassociative, contradicting (3).

If Y is compact **metrizable**, one may replace β(Q_discrete) by ordinary Cantor space, using Q={q_n} countable dense and a discrete sequence {z_n} in the auxiliary Cantor factor. No resolvability theorem beyond separable perfect metrizability is needed. □

**Important status boundaries:** This characterizes universal **safety of all maps/projections with the *entire finite rectangular algebra***, not the power-associativity of their individual closed symmetric graph relations (which holds for closed maps on compact locales). The positive half uses the *internally derived* graph-extension sufficiency theorem; it is not yet an independent blind referee verdict. The negative half is an explicit three-factor nonassociativity computation.

## 6. Exact reduction of Level 3 to product-amplified Level 2

This construction is **categorical** and applies in Loc without Hausdorff hypotheses.

Call a locale map e:S→V **inclusion-stably surjective** if its pullback along every sublocale inclusion W↪V is surjective (the Level 2 property of the previous note). Then
\[
\boxed{
e\text{ is pullback-stably surjective }
\iff
\forall\text{ locales }T,\quad
e\times\mathrm{id}_T:S\times T\to V\times T
\text{ is inclusion-stably surjective}.
}\tag{AMP}
\]

**Proof.** Universal stability is preserved by products and arbitrary pullbacks, so the forward implication is automatic. Conversely, given any h:T→V, the graph \(\Gamma_h:T\hookrightarrow V\times T\) is a sublocale embedding (it is an equalizer/regular mono). Pulling e×id_T back along \(\Gamma_h\) gives precisely \(S\times_VT\to T\). The right side of (AMP) asserts this pullback is surjective. □

Thus the open **Level 2⇒Level 3** problem can be restated as:

> Does inclusion-stable surjectivity of the particular spatial selected-image maps e_E imply that inclusion-stable surjectivity persists after tensoring with **all locale parameters T**?

Theorem 1.1 shows that base changes with **spatial** T pose no obstruction for pointwise-surjective e_E; any remaining counterexample must use genuinely nonspatial parameters. The AMP reduction makes the source of the gap precise without claiming it resolved.

## 7. Project significance and audit priorities

This result brings the investigation back to the original Cameron–Kumar motivation in a new way:
- The positive finite-rectangle and partial-map algebra calculus explains safe localic path multiplication for many ordinary graph relations.
- The scatteredness dichotomy identifies precisely when **the topology of the target alone** guarantees universal stability of every ordinary point-witness cover.
- Non-scattered compact Hausdorff spaces admit perfect closed supports with nonzero **pointless Booleanized overlap**; an open/proper projection can convert that hidden overlap into an ordinary ghost edge after one image collapse.
- Scatteredness therefore marks a **topological universal safe zone** for the graph-extension calculus, not a bound on fiber cardinality or on the number of inverse-branch pieces.

**Suggested independent adversarial audit tasks:** (a) verify the Cantor–Bendixson induction over arbitrary locale base changes, including infinite limit stages and the closed-relative discrete layer; (b) check graph \(\Gamma_h\hookrightarrow V\times T\) in the amplification lemma; (c) inspect the use of Hewitt's compact-Hausdorff resolvability theorem in the nonmetric converse; (d) check point-generated supports on β(Q_discrete) and all relational image claims; (e) separately test the previously unrefereed graph-extension sufficiency criterion used in the positive algebraic corollary.

**Next research question:** Level 2 versus Level 3 cannot be separated by targets that are scattered, because every selected image into a scattered target is Level 3 automatically. A counterexample to Level 2⇒Level 3, or to global HSIS necessity, must involve a **non-scattered** target and a failure that survives ordinary selected-subset thinning. One possible direction is to seek the first nonspatial parameter T for which the amplified map e_E×T fails a Booleanized graph-sublocale probe, despite all inclusion tests for e_E passing.
