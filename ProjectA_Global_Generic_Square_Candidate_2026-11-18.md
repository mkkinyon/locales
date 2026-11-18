# Project A — recovering the global generic-square inclusion

**18 November 2026. Internally stress-tested research candidate; NOT yet externally audited.** This note extends the independently audited patch-fibre/Cantor-graph method beyond the open `P`–`Q` cross-gap rectangle. Its proposed conclusion is the **global generic-square inclusion**

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

**Proposition 4 (global graph generation; candidate).**

\[
\boxed{F_\infty=\bigvee_{\Gamma\in\mathscr C_\infty}\mathcal B(\Gamma)}
\qquad\text{in }P_{\rm patch}^2.\tag{62*}
\]

**Proof.** For any `Γ∈𝒞_∞`, the two generic point tests from Lemma 6 of the cross-gap note apply verbatim: a generic-neighborhood complement meets `E` finitely and hence is nowhere dense in each perfect selected-colour projection; a non-generic quotient open misses `E` entirely and, being patch-open, misses both projections because their selected traces are dense. Thus `0≠B(Γ)≤F_∞`. Let `J` be the join of all these Booleanizations. If `F_∞≰J`, fittedness of the regular patch square gives a patch-closed annihilator `C` with `F_∞∧C≠0` and `J∧C=0`. Take the least compact closed support `C_0⊂C` of `F_∞∧C`. Lemmas 1–3 produce `Γ∈𝒞_∞` contained in `C_0⊂C`. Hence `0≠B(Γ)≤J∧C`, contradiction. ∎

## 4. The perfected strips are global in the selected endpoint

**Lemma 5 (global coloured strips; candidate extension).** Let `D⊂P` be any perfect compact **antichain** with `D∩E_α` dense, for `α∈{P,Q}`. Then, in the patch square,

\[
\mathcal B(D\times M),\quad \mathcal B(M\times D)
\ \le\ (p\times p)^{-1}(T).\tag{3}
\]

**Proof.** The proof of the corrected dense-strip lemma needs only: (i) every nonempty relative open of `D` contains selected vertices from arbitrarily late `α`-fences; (ii) all sufficiently late `α`-fences meet every nonempty open in the fixed mediator `U_α`; (iii) their endpoints are dense in `M`. It does **not** use `D⊂U_α`. Thus the same dense component-pair traces in `D×U_α` and `U_α×M`, open pullbacks to `D×U_α×M`, and open image to `D×M` prove (3). ∎

**Lemma 6 (global graph composition; candidate).** Every `Γ∈𝒞_∞` satisfies

\[
\mathcal B(\Gamma)\le(p\times p)^{-1}(T\circ T).\tag{4}
\]

**Proof.** Apply Lemma 5 with colours `α,β` to its two projected Cantor antichains. On the locale `Γ×M`, the two projections to `D_1×M` and `M×D_2` are homeomorphisms, so the pullbacks of both dense strips contain `B(Γ×M)`. This is a composable witness in the upper triple. The open-surjective outer projection to `Γ` has dense image, which contains `B(Γ)` and maps through `T∘T`. As before, the restriction to the graph precedes the composition. ∎

## 5. Special-fibre descent, and the remaining global problem

**Proposition 7 (candidate (64*)).** Under the stated finite-fence hypotheses, `G×G≤T∘T`.

**Proof.** By (62*) and (4), `F_∞≤(p×p)^{-1}(T∘T)`. Every ordinary point `m∈M_min` lies in a single finite comparability component `C_m`; the saturated upper-open complement of `C_m` descends to a quotient neighborhood of `p_∞` but omits `m`. Thus `G∧[m]=0` for every minimal fence vertex `m`. Corollary A.1 (minimal-vertex avoidance) of the audited cross-gap theorem note gives the **specific isomorphism** `p^{-1}(G)≅G`, hence `(p×p)|_{F_∞}:F_∞≅G×G`. In fact the original Theorem A also applies: the upper topology of a compact closed pospace is sober, and the same finite-component complement excludes **every** ordinary point of `X` from `G`, so `G` is pointless. Transport the displayed patch-pullback inclusion through this isomorphism to obtain `G×G≤T∘T` in `X×X`. No assertion that the full patch counit is proper is used. ∎

This result, **if its global colour-localization and strip extensions survive adversarial audit**, repairs the earlier route to (64) while leaving the global kernel-pair equality `K_q=T∘T` unresolved. The remaining obstacle is a valid localic decomposition or detection theorem for the non-generic component and boundary pieces of `K_q`; (64*) by itself does not settle that problem.

## 6. Adversarial checklist before promotion

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

**Residual risk / audit request:** An independent referee should try to break the fixed-colour support localization and the global strip extension using a compact support concentrated near `K`, `M`, `L`, or a singleton-component accumulation point. The old global result was rejected for a real reason; the present argument avoids that reason but is not yet externally checked.
