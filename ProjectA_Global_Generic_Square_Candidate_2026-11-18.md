# Project A — global generic-square generation and colour-sensitive bounds

**18 November 2026. Consolidated following independent blind audit and referee addendum.** The full proof of (62*) and (64*) has passed independent scrutiny **conditional on the explicitly stated finite-fence geometric assumptions**. The abstract localic implication is supported; a separate coordinate-level realization and proof of the strong forcing/traversal hypotheses have **not** been audited. The same-colour two-step refinement from the referee addendum is recorded below. A subsequent **not-yet-externally-audited, extra-hypothesis** negative solution to the mixed-colour question is in `ProjectA_MixedColour_TwoStep_Obstruction_2026-11-18.md`.

\[
\boxed{G\times G\le T\circ T,\qquad G=q^{-1}([p_\infty]),\quad T=H_G\circ H_G.}\tag{64*}
\]

The old argument for (64) in the finite-fence equivalence-hull note was invalid because it invoked proper descent for the non-proper patch counit. The replacement uses Theorem A / Corollary A.1 of `ProjectA_PatchFibre_CrossGap_Theorem_Note_2026-11-18.md`, an independently audited *special-fibre* isomorphism. No assertion about the whole kernel pair follows from (64*).

## 1. Global compact cutoffs and coordinate richness

Use the original finite-fence compact pospace `P=[0,1]` with closed height-one order, pairwise disjoint finite comparability components `P_n,Q_n`, countable vertex set `E=E_P∪E_Q`, and the generic quotient point `p_∞`. The two colour families have the fixed upper-open mediator sets `U_P,U_Q` visited by every sufficiently late corresponding component and dense endpoint sets `A,B⊂M`.

Write `p:P_patch→X`, `G=q^{-1}([p_∞])`, and

\[
F_\infty=(p\times p)^{-1}(G\times G)=\Lambda_E\times\Lambda_E
\quad\le P_{\rm patch}^2.\tag{1}
\]

The global patch generic fibre `Λ_E` is pointless. In fact, for **any** compact patch-closed `C⊂P` with `C∩E` finite, its comparability saturation `C^sat` is `C` together with finitely many entire finite fence components, hence is compact, patch-closed and saturated. Its upper-open complement descends to a quotient-open neighborhood of `p_∞` disjoint from `C`.

**Lemma 1 (global support richness).** Let `0≠S≤F_∞` be dense in its least ambient patch-closed support `C_0⊂P²` (automatically compact). In each nonempty relatively open `W⊂C_0`, both sets

\[
\pi_1(W)\cap E,\qquad\pi_2(W)\cap E
\]

are infinite. No finite union of vertical/horizontal point-coordinate sections contains a nonempty relatively open subset of `C_0`.

**Proof.** If `π_1(W)∩E` were finite, choose nonempty relative open `W'` with `cl_{C_0}(W')⊂W`. The first projection of that compact closure meets `E` finitely. The global compact cutoff supplies a generic quotient neighborhood whose patch pullback avoids the whole projection, so `S∧W'=0`, contradicting density in `C_0`. Symmetrically for the second projection. Each point-coordinate section meets `S` in zero, because `Λ_E` is pointless; a finite union of such sections cannot contain a nonempty relative open of its least closed support. ∎

## 2. Fixed-colour localization and global antichain fusion

**Lemma 2 (two-colour Baire localization).** Under Lemma 1's hypotheses, there is a nonempty relatively open portion `W⊂C_0`, with relatively compact ambient rectangular neighborhood, and fixed colours `α,β∈{P,Q}` such that every nonempty relatively open subset of `W` meets

\[
(E_\alpha\times P)\cap C_0
\quad\text{and}\quad
(P\times E_\beta)\cap C_0
\]

in infinitely many distinct coordinate values. The same property holds after passing to the least ambient closed support `C_1` of the restriction of `S` to a sufficiently small open rectangle in `W`.

**Proof.** Put `A_α=C_0∩π_1^{-1}(E_α)` and `B_β=C_0∩π_2^{-1}(E_β)`. By Lemma 1,

\[
C_0=\overline{A_P}\cup\overline{A_Q}
=\overline{B_P}\cup\overline{B_Q}.
\]

Thus the four closed intersections `\overline{A_α}∩\overline{B_β}` cover the compact Baire space `C_0`; at least one has nonempty relative interior `W`. Both designated selected traces are dense in `W`: if `O⊂W` is relatively open and nonempty, then `O` meets each of `A_α` and `B_β` because `W` lies inside their respective closures. A **finite** set of coordinate values cannot exhaust either trace in such an `O`: remove the corresponding finitely many nowhere-dense point sections (Lemma 1) to obtain another nonempty relative open subset of `O` still meeting the selected trace. Since every fence component is finite, the selected component indices are therefore unbounded in every relative open of `W`.

Choose a patch-open rectangle `V` with `C_0∩V≠∅` and `cl_{C_0}(C_0∩V)⊂W`. Because `S` is dense in `C_0`, its restriction to `V` is dense in `C_0∩V`. Consequently its least ambient closed support is exactly `C_1=cl_{C_0}(C_0∩V)`: any smaller closed candidate would omit an open part of `C_0∩V` on which `S` is nonzero. Every nonempty relative open of `C_1` meets the dense relatively open portion `C_0∩V`, so the same selected-colour richness and finite-section avoidance pass to `C_1`. This argument uses **ordinary points of the compact closed support**, never points of the pointless sublocale `S`. ∎

**Lemma 3 (global coloured Cantor graphs).** Every `0≠S≤F_∞` with compact least closed support `C_0` admits a compact Cantor graph `Γ⊂C_0` whose projections `D_1,D_2` are compact Cantor antichains and such that, for fixed colours `α,β`,

\[
D_1\cap E_\alpha\text{ is dense in }D_1,
\qquad D_2\cap E_\beta\text{ is dense in }D_2.\tag{2}
\]

**Proof.** Apply Lemma 2 to obtain a compact selected-colour-rich support `C_1⊂C_0`. Repeat the **global two-phase ternary fusion** of Lemma 5 in the corrected cross-gap note, replacing selected colours `P,Q` by `α,β`. First choose an anchor outside the countable union of fence-vertex sections by Baire. At each finite tree depth, choose all first-colour and second-colour new anchors globally, one of each at every node, reserving finite comparability components separately in both coordinates after each choice. Only after every anchor at that depth is chosen shrink all child rectangles simultaneously to avoid all other vertices of every registered component, plus all vertices in the first `n` still-unregistered components. Every exclusion is finite, and Lemma 2 supplies arbitrarily late fresh selected-colour anchors. Shrinking diameters, disjoint sibling coordinate intervals, and persistent child-0 anchors produce a Cantor graph. Its two selected traces are dense. The global component-exclusion invariant ensures at most one vertex of each component appears in either projected Cantor set; height one makes each projection an antichain. ∎

## 3. Global graph generation

Let `𝒞_∞` comprise **all** nonempty compact Cantor graphs in `P²` having antichain projections and fixed (possibly equal) selected colours `α,β` with dense traces as in (2).

**Theorem 4 (global graph generation; conditionally verified).**

\[
\boxed{F_\infty=\bigvee_{\Gamma\in\mathscr C_\infty}\mathcal B(\Gamma)}
\qquad\text{in }P_{\rm patch}^2.\tag{62*}
\]

**Proof.** For any `Γ∈𝒞_∞`, the two generic point tests from Lemma 6 of the cross-gap note apply verbatim: a generic-neighborhood complement meets `E` finitely and hence is nowhere dense in each perfect selected-colour projection; a non-generic quotient open misses `E` entirely and, being patch-open, misses both projections because their selected traces are dense. Thus `0≠B(Γ)≤F_∞`. Let `J` be the join of all these Booleanizations. If `F_∞≰J`, fittedness of the regular patch square gives a patch-closed annihilator `C` with `F_∞∧C≠0` and `J∧C=0`. Take the least compact closed support `C_0⊂C` of `F_∞∧C`. Lemmas 1–3 produce `Γ∈𝒞_∞` contained in `C_0⊂C`. Hence `0≠B(Γ)≤J∧C`, contradiction. ∎

## 4. The perfected strips are global in the selected endpoint

**Lemma 5 (global coloured strips; conditionally verified).** Let `D⊂P` be any perfect compact **antichain** with `D∩E_α` dense, for `α∈{P,Q}`. Then, in the patch square,

\[
\mathcal B(D\times M),\quad \mathcal B(M\times D)
\ \le\ (p\times p)^{-1}(T).\tag{3}
\]

**Proof.** The proof of the corrected dense-strip lemma needs only: (i) every nonempty relative open of `D` contains selected vertices from arbitrarily late `α`-fences; (ii) all sufficiently late `α`-fences meet every nonempty open in the fixed mediator `U_α`; (iii) their endpoints are dense in `M`. It does **not** use `D⊂U_α`. Thus the same dense component-pair traces in `D×U_α` and `U_α×M`, open pullbacks to `D×U_α×M`, and open image to `D×M` prove (3). ∎

**Lemma 6 (global graph composition; conditionally verified).** Every `Γ∈𝒞_∞` satisfies

\[
\mathcal B(\Gamma)\le(p\times p)^{-1}(T\circ T).\tag{4}
\]

**Proof.** Apply Lemma 5 with colours `α,β` to its two projected Cantor antichains. On the locale `Γ×M`, the two projections to `D_1×M` and `M×D_2` are homeomorphisms, so the pullbacks of both dense strips contain `B(Γ×M)`. This is a composable witness in the upper triple. The open-surjective outer projection to `Γ` has dense image, which contains `B(Γ)` and maps through `T∘T`. As before, the restriction to the graph precedes the composition. ∎

## 5. Special-fibre descent, and the remaining global problem

**Theorem 7 (global generic-square inclusion; conditionally verified (64*)).** Under the stated finite-fence hypotheses, `G×G≤T∘T`.

**Proof.** By (62*) and (4), `F_∞≤(p×p)^{-1}(T∘T)`. Every ordinary point `m∈M_min` lies in a single finite comparability component `C_m`; the saturated upper-open complement of `C_m` descends to a quotient neighborhood of `p_∞` but omits `m`. Thus `G∧[m]=0` for every minimal fence vertex `m`. Corollary A.1 (minimal-vertex avoidance) of the audited cross-gap theorem note gives the **specific isomorphism** `p^{-1}(G)≅G`, hence `(p×p)|_{F_∞}:F_∞≅G×G`. In fact the original Theorem A also applies: the upper topology of a compact closed pospace is sober, and the same finite-component complement excludes **every** ordinary point of `X` from `G`, so `G` is pointless. Transport the displayed patch-pullback inclusion through this isomorphism to obtain `G×G≤T∘T` in `X×X`. No assertion that the full patch counit is proper is used. ∎

The independent referee found the global colour-localization, strip extension, and special-fibre reflection correct relative to the geometric assumptions. This repairs the earlier route to (64) while leaving `K_q=T∘T` **unproved**. The remaining obstacle is a valid localic decomposition or detection theorem for the non-generic component and boundary pieces of `K_q`.

## 6. Audit and geometric-realization checklist

1. Does compact saturation of an arbitrary patch-closed set meeting `E` finitely give a **quotient-open generic neighborhood** without hidden properness?
2. Does Baire's finite colour localization on a *nonspatial* least closed support really preserve both selected-coordinate richness properties on its compact refinement?
3. Does the global two-phase reservation induction still work when the same colour is chosen in both coordinates and when projections meet `K,M,L` or gap boundaries?
4. Does the perfected dense-strip lemma extend to `D⊂P`, with no assumption that `D` is contained in its colour's mediator?
5. Is the use of `p^{-1}G≅G` justified by Corollary A.1, even if one avoids assuming independent pointlessness of `G`?
6. Are all Booleanization inclusions typed in the patch square, and is the transfer to `X²` performed only via the special-fibre isomorphism?

No blanket proper-descent or infinitary interchange law is assumed.

## 7. Internal adversarial check (18 November 2026)

**Outcome:** No invalid inference found in (64*) under the stated geometric hypotheses; retain **candidate** status pending independent review. The following checks distinguish the old, actually invalid proper-descent argument from the present restricted method.

* **Global cutoff:** The saturation of `C` adds only finitely many complete finite comparability components, because every non-singleton component point is in `E`. A compact union with finitely many finite sets is patch-closed. The saturated complement is both upper-open and quotient-open, and meets `E`; it is therefore a valid generic neighborhood. No closedness of `p` is invoked.
* **Colour localization:** The equalities `C_0=cl(A_P)∪cl(A_Q)=cl(B_P)∪cl(B_Q)` follow from *coordinate* `E`-richness on every nonempty support open, not from any supposed point-density of `S`. Finite Baire selects an open subset of one of four closed intersections; density of selected anchors on that region survives arbitrary finite coordinate exclusions. Passing to the closure of a smaller relative open portion preserves this property.
* **Global fusion:** At any finite stage, all earlier and newly chosen anchors have distinct coordinates where required. Each new anchor excludes the finitely many previously registered fence-component vertices in **both** coordinates. Reserve any component hit by either coordinate, even when unselected. Shrink all rectangles **only after** selecting all anchors at that depth; then every potential conflict is a finite forbidden coordinate value not itself an anchor. The reasoning is independent of the ambient location and allows `α=β`.
* **Strip extension:** The corrected dense-strip proof factors through `D×U_α×M` and uses no placement restriction on `D`; one needs only the local unbounded-index condition, ensured by perfection and dense selected-colour traces. The ambient relation claims are always in the *patch pullback* `(p×p)^{-1}T`.
* **Graph and transfer:** The generic point tests for `B(Γ)` use nowhere-dense **closed** intersections with a generic-neighborhood complement and empty **open** traces for non-generic quotient opens. Composition is performed on `Γ×M` before imaging. The final reflection uses the isomorphism on `G×G`, not surjectivity or properness of `p×p` on the entire square.

**External audit verdict (18 November 2026).** The independent referee verified (62*) and (64*) relative to the stated compact-pospace and finite-fence hypotheses. No fatal localic inference or missing hypothesis was found for those *conditional* implications. In particular, the referee independently checked global compact cutoffs, fixed-colour Baire localization on nonspatial supports, the two-phase fusion with coinciding colours, the extension of perfected strips beyond a mediator, graph-before-composition, and the isomorphic transfer through `p^{-1}(G)≅G`.

**Outstanding geometric verification.** The archive supplied no complete coordinate construction. The strongest premise—every closed saturated set meeting infinitely many finite-fence components contains all of `E`—must be independently verified together with late-fence traversal, dense distinct endpoints, closedness of the order, and compactness of the stated patch model before applying the theorems unconditionally to a concrete example.

## 8. Referee addendum: same-colour graphs need only two steps

Define the upper-to-patch pullbacks

\[
\widehat H=(p\times p)^{-1}H_G,\qquad
\widehat T=(p\times p)^{-1}T,\qquad
\widehat{T^{[2]}}=(p\times p)^{-1}(T\circ T).
\]

**Proposition 8 (same-colour graph, two steps).** Fix `α∈{P,Q}`. Suppose `Γ⊂P²` is a compact Cantor graph whose coordinate projections `D_1,D_2` are perfect compact sets and the maps `Γ→D_i` are homeomorphisms. If `D_1∩E_α` and `D_2∩E_α` are both dense, then

\[
\boxed{\mathcal B(\Gamma)\le\widehat T.}\tag{A1}
\]

The antichain assumption on `D_i` is **not needed** for this particular composition statement, although it was needed for the global graph-generation proof.

**Proof.** The dense component-pair argument already gives the *one-step* patch-typed inclusions

\[
\mathcal B(D_1\times U_\alpha)\le\widehat H,
\qquad\mathcal B(U_\alpha\times D_2)\le\widehat H.\tag{A2}
\]

Indeed every nonempty relatively open part of either perfect projection contains selected vertices from arbitrarily high-index `α`-fences, each of which visits any prescribed nonempty patch-open part of `U_α`. Pull both sublocales back to the **same** locale `Γ×U_α`. The projections to `D_1×U_α` and `U_α×D_2` are homeomorphisms, so their pullbacks contain `B(Γ×U_α)`. This supplies a composable upper-localic witness for `H_G∘H_G=T`. The outer-coordinate projection `Γ×U_α→Γ` is open surjective; the patch image of `B(Γ×U_α)` is dense in `Γ` and therefore contains `B(Γ)`. Thus `B(Γ)≤\widehat T`. ∎

**Corollary 9 (same-mediator generic products).** With `G_α^*=G∧U_α`,

\[
\boxed{G_\alpha^*\times G_\alpha^*\le T
\qquad(\alpha=P,Q).}\tag{A3}
\]

**Proof.** Pull the generic product to the patch mediator square `U_α×U_α`. For any nonzero closed restriction, pass to a compact ambient closed support inside a relatively compact open rectangle. A compact subset of this mediator meeting `E_α` finitely also meets `E` finitely, since the opposite-colour components do not enter the mediator. Global compact saturation therefore gives selected-coordinate richness of the *same* colour in both projections. The two-phase Cantor fusion constructs, inside the support, a graph with perfect Cantor antichain projections and both selected `E_α` traces dense. Its nonzero Booleanization lies in the patch generic product by both quotient-point tests, and Proposition 8 places it inside `\widehat T`. The fitted closed-annihilator argument yields the entire patch generic-product inclusion. The special-fibre isomorphisms `p^{-1}(G_α^*)≅G_α^*` transfer it to `X²`. ∎

This is **only** an inclusion for the generic product. It is **not** an asserted formula for `K_q∧(U_α×U_α)`, since ordinary pairs in the same finite fence also belong to that kernel-pair restriction.

## 9. Four colour classes and the mixed-colour two-step question

Let `J_{αβ}` be the join of `B(Γ)` over all global generating Cantor graphs `Γ` whose designated selected colours are `(α,β)`. Since the two colours need not be uniquely determined, these classes may overlap; nevertheless Theorem 4 gives

\[
F_\infty=J_{PP}\vee J_{PQ}\vee J_{QP}\vee J_{QQ}.\tag{A4a}
\]

Proposition 8 and Lemma 6 sharpen their respective relation bounds to

\[
\boxed{J_{PP}\vee J_{QQ}\le\widehat T,\qquad
J_{PQ}\vee J_{QP}\le\widehat{T^{[2]}}.}\tag{A4b}
\]

The two-step bound for *same-colour* pieces follows from a **common** upper-open mediator visited by all late fences of that colour. For mixed colours the original four-step proof goes through two potentially different mediators and the middle Cantor set `M`. This does **not** prove that four steps are minimal for any mixed-colour graph.

The concrete question posed at the time of the external audit was

\[
\boxed{G_P^*\times G_Q^*\stackrel{?}{\le}T.}\tag{MC2}
\]

Since the restricted cross-gap equalizer is already identified with this generic product and is contained in `T∘T`, a negative solution to (MC2) would separate two-step from four-step containment **on a precisely controlled open block**. The follow-on note `ProjectA_MixedColour_TwoStep_Obstruction_2026-11-18.md` develops just such a negative result, **conditional on segment-confined fences**: compact *closed lower* Cantor source/target sets choose late components whose middle endpoints lie in separated regions. The corresponding two one-step mediator supports intersect only in finitely many early vertices and those give no composable pair. This forces `T` to vanish on a closed rectangle while a nonzero Booleanization of its patch Cantor square belongs to the generic cross-gap product. The proof is internally checked but **has not received independent adversarial review**, and the segment-confinement condition is additional to the earlier abstract audit assumptions.

**Provenance and scope.** Proposition 8 and Corollary 9 were proposed with proofs in the referee's separately authored follow-up addendum of 18 November 2026. Their arguments have been checked internally here; they are consequences conditional on the same geometric hypotheses, not claims of an additional separate blind audit. The global kernel-pair equality remains open.
