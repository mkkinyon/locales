# Project A — pointless patch fibres and the open cross-gap equalizer

**18 November 2026.** Consolidated research theorem note for independent audit. **Status:** The patch-fibre comparison (Theorem A) has passed an internal adversarial check. The cross-gap assertion (Theorem B) has an internally supported proof, conditional on the explicit Cantor-fusion induction in Lemma 5; an independent audit is requested. Neither statement establishes the global assertion `K_q = T∘T`.

## 1. Construction and conventions

Let `P=[0,1]` with its Euclidean patch topology and the closed height-one partial order of the finite-fence construction. Its nontrivial comparability components are two disjoint sequences of finite connected zigzag fences `P_n` and `Q_n`; all other components are singletons. Every strict order pair lies along one edge of one fence. Each edge in the `n`th fence has Euclidean length `<1/n`, and no strict chain has length two. All fence vertices are distinct. Set

\[
 E_P=\bigcup_n V(P_n),\qquad E_Q=\bigcup_nV(Q_n),\qquad E=E_P\cup E_Q.
\]

The `P_n` travel through the geometric gap between two disjoint compact Cantor antichains `K<M`; the `Q_n` travel through the gap between `M<L`. Their endpoints in `M` enumerate disjoint dense countable sets `A={a_n}` and `B={b_n}`. Every sufficiently late `P_n` visits every prescribed nonempty upper-open subset compactly contained in the first gap, and likewise `Q_n` in the second. In fact the mesh estimate gives this for every fixed nonempty open subinterval of its gap.

Let `X` be the locale of Euclidean-open **upper** sets of `P`; write `p:P_patch→X` for the canonical patch map. The quotient `q:X→Q` has as opens the component-saturated upper opens. The quotient has a generic point `p_∞`, characterized by those saturated opens that meet `E`. A saturated patch-closed set meeting infinitely many fence components contains all of `E` (finite-fence forcing); thus the complement of any `p_∞`-neighborhood meets `E` only finitely, and every other quotient open misses `E`.

Write

\[
 H_G=[E_G],\quad T=H_G\circ H_G,\quad
 \mathcal K_q=X\times_Q X,
\]

where `E_G` consists of all ordinary pairs in a common comparability component, square brackets denote the point-generated spatial sublocale, and `∘` is image-based localic relational composition. `T∘T` always has this exact bracketing. Since `H_G≤K_q` and kernel pairs are transitive, `T∘T≤K_q`.

Choose nonempty **upper-open** `U_P,U_Q` whose Euclidean closures lie strictly inside the corresponding two gaps. They are fixed mediators visited by all sufficiently late fences of their respective colors. Define

\[
 G_P^*=G\wedge U_P,\qquad G_Q^*=G\wedge U_Q,
 \quad G=q^{-1}([p_\infty]).
\]

Their inverse images in the *ambient* patch space are `\widetilde G_P` and `\widetilde G_Q`. The exact cross-gap equalizer formula established by direct saturated cutoffs in the preceding restricted calculation is

\[
 \boxed{\mathcal K_q\wedge(U_P\times U_Q)=G_P^*\times G_Q^*.} \tag{E}
\]

For reference, its reverse inclusion holds because both factors map constantly to `p_∞`. For the upper inclusion, a quotient open missing `p_∞` restricts to zero on both gaps; a neighborhood of `p_∞` has closed saturated complement meeting `E` finitely. Compact cutoffs inside the disjoint gaps, followed by saturation of the finitely many touched components, produce separate quotient-open tests that agree with the original test on one gap and equal top on the other. The equalizer therefore satisfies the two generic-neighborhood conditions independently. This argument is *specific to these disjoint open gaps* and does not use global patch descent.

## 2. Theorem A: pointless sublocales do not see shrinking fence edges

**Theorem A (pointless patch comparison).** For **every pointless sublocale** `S≤X`, the canonical pullback comparison

\[
 \boxed{p_S:p^{-1}(S)\longrightarrow S\text{ is an isomorphism}.} \tag{A}
\]

In particular,

\[
 \boxed{\widetilde G_P\cong G_P^*,\quad
        \widetilde G_Q\cong G_Q^*.} \tag{40}
\]

**Proof.** Let `i:O(X)↪O(P_patch)` be inclusion. For Euclidean-open `O⊂P` define its largest upper-open core

\[
 r(O)=\{x:\uparrow x\subseteq O\}
     =P\setminus\downarrow(P\setminus O). \tag{A1}
\]

The order is closed and `P\O` compact, so its downward closure is closed. Hence `r(O)` is upper-open, `r(O)⊂O`, and `r` is right adjoint to `i`. In particular `r` preserves finite meets and `r(U)=U` for upper opens `U`.

Put `D_O=O\r(O)`. Every member of `D_O` is a minimal fence vertex having some upper neighbor outside `O`. If `C⊂O` is Euclidean compact, let `δ=dist(C,P\O)>0` (the trivial case `O=P` is omitted). Any edge from `D_O∩C` to `P\O` has length at least `δ`, so only finitely many early fences contribute. Therefore `D_O∩C` is finite. Because `r(O)` is open, `D_O` is closed and locally finite in the Euclidean-open space `O`.

For an **arbitrary** family of Euclidean opens `(O_i)`, let

\[
 W=r(\bigcup_iO_i),\qquad R=\bigcup_i r(O_i),\qquad D=W\setminus R. \tag{A2}
\]

`D` is upper-closed relative to the upper-open `W`. Moreover every `x∈W` lies in some `O_i`, and `D∩O_i⊂D_{O_i}`, so `D` is Euclidean locally finite in `W`. All its points are minimal fence vertices. For `d∈D` the upper cone `↑d` is finite, is contained in `W`, and meets `D` exactly in `{d}`. The Euclidean closed-discreteness of `D` in `W` permits a Euclidean-open neighborhood `N⊂W` of `↑d` avoiding `D\{d}`. Then `r(N)` is an upper-open neighborhood of `d` meeting `D` only at `d`. Thus `D` is a **closed discrete subspace in the upper topology of `W`**.

For a pointless `S≤X`, `S∧D=0`: any sublocale of the closed discrete locale `D` is spatial, because every frame quotient of `\mathcal P(D)` is complete atomic Boolean. Let `λ:O(X)↠O(S)` be restriction. Within `W`, the open `R` and its closed complement `D` have join `W`; finite distributivity of the sublocale lattice and `S∧D=0` imply `λ(W)=λ(R)`. Hence

\[
 λr(\bigcup_iO_i)=\bigvee_iλr(O_i). \tag{A3}
\]

Combined with preservation of finite meets, `ρ=λr:O(P_patch)→O(S)` is a **frame homomorphism**, despite the fact that `r` itself need not preserve joins. Since `ρi=λ`, its locale map `s:S→P_patch` satisfies `p∘s` equal to the inclusion `S→X`; the pullback universal property gives a section `\bar s:S→p^{-1}(S)` of `p_S`.

Conversely, `p^{-1}(S)` is pointless. For every patch-open `O`, the difference `D_O` is closed discrete relative to `O` and so meets `p^{-1}(S)` in zero. Therefore `O` and `r(O)` have **identical** restrictions to `p^{-1}(S)`. Every open of the latter is consequently the restriction of an upper-open; i.e. `p_S^*:O(S)→O(p^{-1}S)` is surjective. The section makes it injective. This proves (A). ∎

**Scope warning.** The patch counit `p` is not a closed map in this example (a maximal fence singleton is patch-closed but not upper-closed). Theorem A neither asserts that `p` is Vermeulen-proper nor invokes any general proper-descent theorem. It works for the *specific pointless pullbacks*.

## 3. Compact cutoff and richness of generic supports

We work inside the Euclidean patch rectangle `U_P×U_Q`. Set

\[
 F=\widetilde G_P\times\widetilde G_Q. \tag{F}
\]

Both factors and all their ordinary one-point coordinate fibres are zero. The following cutoff is useful.

**Lemma 1 (finite-vertex cutoff).** If `C⊂U_P` is compact and `C∩E_P` finite, its saturation by comparability components is a compact closed saturated subset of `P` meeting `E` finitely. Its complement descends to a quotient-open neighborhood of `p_∞` disjoint from `C`. The same holds in `U_Q` with `E_Q`.

**Proof.** Every component meeting `C` is either a singleton already in `C` or one of the finitely many finite fences containing a vertex of `C∩E_P`. Add those finite vertex sets. The union is compact closed and saturated; its complement is saturated upper-open and misses only finitely many fence vertices. ∎

**Lemma 2 (selected-coordinate richness).** Let `0≠S≤F` have compact closed support `C_0` in the patch rectangle, and assume `S` is dense in `C_0` (for example take its least closed support). For every nonempty relatively open `W⊂C_0`, both sets

\[
 \pi_1(W)\cap E_P,\qquad \pi_2(W)\cap E_Q
\]

are infinite. Furthermore no finite union of vertical and horizontal coordinate sections contains a nonempty relatively open subset of `C_0`.

**Proof.** If the first selected-coordinate set were finite, choose nonempty relatively open `W'` in `C_0` with `\overline{W'}⊂W`. The first-coordinate projection of this closure is compact and meets `E_P` finitely. Lemma 1 provides a `p_∞`-neighborhood whose first-coordinate pullback misses `\overline{W'}`; since `S≤F`, this would give `S∧W'=0`, contradicting density of `S` in `C_0`. The other coordinate is symmetric. For the final assertion, each one-point vertical or horizontal section has zero intersection with `S` because the factors of `F` are pointless. If a nonempty relatively open part of `C_0` lay in finitely many such sections, density of `S` would be contradicted. ∎

In applying this lemma to a nonzero closed restriction of `F`, first restrict to a relatively compact patch-open rectangle where the restriction stays nonzero, then take its least closed support. Such a rectangle exists because these rectangles form an open cover of `U_P×U_Q`.

## 4. Cantor graph with two selected projections

**Lemma 3 (finite exclusions).** Given a nonempty relatively open `W⊂C_0`, finite sets `A_0` of forbidden first-coordinate values, `B_0` of forbidden second-coordinate values, and a bound `N`, there exists a point of `W` whose first coordinate belongs to `E_P` in a fence of index `>N` and whose second coordinate avoids `B_0`, with both coordinates avoiding the prescribed finitely many complete fence components. There is a symmetric choice with second coordinate in `E_Q` of index `>N`.

**Proof.** Every specified vertical or horizontal section is relatively closed and has empty interior in `C_0` by Lemma 2. Removing their finite union leaves a nonempty relatively open piece of `W`. The corresponding selected-coordinate projection remains infinite by Lemma 2. Each fence is finite, so there are selected coordinates from arbitrarily high, unreserved component indices. ∎

**Lemma 4 (no selected coordinate required for the first anchor).** There exists a point of `C_0` whose two coordinates lie outside `E`. In fact the complement of the countable union of vertical and horizontal sections at `E` is dense in `C_0`.

**Proof.** Each such section is closed nowhere dense by Lemma 2, and `C_0` is a nonempty compact metric Baire space. ∎

**Lemma 5 (antichain Cantor-graph fusion — audit target).** Under Lemma 2's hypotheses, there exists a nonempty compact Cantor graph `Γ⊂C_0` such that both coordinate maps are homeomorphisms onto compact Cantor **antichains** `D_P⊂U_P`, `D_Q⊂U_Q`, and the traces `D_P∩E_P` and `D_Q∩E_Q` are dense in the respective projections.

**Induction.** Construct a ternary tree of closed Euclidean rectangles `R_s=I_s×J_s`, `s∈{0,1,2}^{<ω}`, with distinguished anchors `z_s∈C_0∩int R_s`. Begin with a rectangle around a point from Lemma 4. At every depth impose these invariants:

1. Each child rectangle lies in the parent interior; sibling first-coordinate intervals are pairwise disjoint, as are sibling second-coordinate intervals; all diameters at depth `n` are `<2^{-n}`; each anchor is interior to its rectangle.
2. Child `s0` keeps `z_s` as its anchor. Child `s1` gets an anchor with first coordinate in `E_P`, and child `s2` gets an anchor with second coordinate in `E_Q`. The latter anchors have pairwise distinct coordinates in both factors and belong to previously unused fence components in their selected coordinates.
3. Maintain *two separate finite component registries*, one for each coordinate. When a newly chosen anchor coordinate happens to be any fence vertex (even in its unselected coordinate), reserve its whole finite component for that coordinate. No future new anchor coordinate may use a different vertex of a reserved component. Parent anchors may persist but are not new reservations.
4. At depth `n`, all current coordinate intervals avoid **every unreserved vertex** of the first `n` fence components; for a component with a reserved anchor coordinate, only its single reserved vertex is permitted in the union of current intervals for that coordinate. Enforce the same finite exclusions for every previously reserved component, regardless of index.

At a node `s`, first retain `z_s` for child 0. Use Lemma 3, excluding all already reserved component vertices and the finite coordinate values of the anchors just chosen, to select the color-`P` anchor for child 1 and color-`Q` anchor for child 2. All choices lie in `C_0∩int R_s` and can be made in fresh components above the current stage. The finite-exclusion lemma guarantees this after each added restriction. Register all fence components hit by *either* coordinate of either new anchor. Shrink disjoint closed intervals about the three anchors inside `R_s`; the finiteness of each reserved component permits removal of all its other vertices, and the first-`n` restriction is finite. Continue simultaneously at the finitely many nodes at each depth.

Define

\[
 \Gamma=C_0\cap\bigcap_n\bigcup_{|s|=n}R_s. \tag{CG}
\]

Nested compactness and shrinking diameters give exactly one limit point on each infinite branch. The three disjoint children guarantee a Cantor space with no isolated points; disjoint sibling intervals in **each** coordinate make both projections injective. Every selected anchor persists on the branch obtained by continually taking child 0, so each cylinder meets a first-selected anchor from its child 1 and a second-selected anchor from its child 2. These anchors are dense in the two projections.

Finally, suppose two distinct first-coordinate limit points were vertices in one fence component of index `j`. At any depth beyond `j`, the component-exclusion invariant permits at most the one registered vertex of that component in the union of all intervals. This is impossible. The same argument applies to the second projection. Since all strict comparabilities are within finite fence components, both projections are antichains. ∎

**Comment for the referee.** The induction is the principal constructive claim requiring independent scrutiny. In particular, check simultaneous feasibility of the child-anchor choices and exclusion invariants, rather than accepting a generic assertion that “some Cantor subset” exists.

## 5. Booleanization of the graph and the two-step strips

Write `B(Z)` for the least dense sublocale (double-negation Booleanization) of `Z`.

**Lemma 6 (generic inclusion, with both point tests).** The graph from Lemma 5 satisfies

\[
 0\ne\mathcal B(\Gamma)\le F. \tag{B1}
\]

**Proof.** If `V` is a quotient-open neighborhood of `p_∞`, its closed saturated complement meets `E` finitely. Since the selected traces are dense in the perfect projections `D_P,D_Q`, the intersections of those projections with the complement are nowhere dense. The two pullbacks of `V` to `Γ` are therefore dense opens containing `B(Γ)`. If `V` does *not* belong to `p_∞`, its saturated pullback misses `E`; being patch-open, it cannot meet either `D_P` or `D_Q` at all, because the selected vertices are dense there. Thus the positive and negative tests of the point sublocale `[p_∞]` both hold. Equivalently, use the known exact patch-fibre formula `p^{-1}G=\Lambda_E`, the meet of complements of patch-closed sets meeting `E` finitely. Both routes give (B1). ∎

**Lemma 7 (corrected dense strips).** For a **perfect compact antichain** `D⊂U_P` with dense `D∩E_P` (or analogously `D⊂U_Q` with dense `D∩E_Q`),

\[
 \mathcal B(D\times M)\le T,
 \qquad\mathcal B(M\times D)\le T. \tag{DS'}
\]

**Proof.** In `D×U_P`, component-equivalent ordinary pairs are dense: every nonempty relative open in `D` contains selected vertices from arbitrarily late fences, and each late fence visits every prescribed nonempty open in `U_P`. Thus `B(D×U_P)≤H_G`. Likewise ordinary component pairs are dense in `U_P×M`, using the dense sequence `a_n`, so `B(U_P×M)≤H_G`. Their pullbacks to `D×U_P×M` along the open product projections are dense sublocales, and their meet contains the least dense sublocale of that triple. Projecting to `D×M` along the open surjection gives a dense image inside `H_G∘H_G=T`, hence an image containing `B(D×M)`. Reverse coordinates or exchange colors to obtain the remaining cases. **Perfection (or the explicit unbounded-index condition) is essential**: the claim is false for a singleton fence vertex. ∎

**Lemma 8 (graph-restricted composition).** For the graph in Lemma 5,

\[
 \boxed{\mathcal B(\Gamma)\le T\circ T.} \tag{B2}
\]

**Proof.** By Lemma 7, `B(D_P×M)≤T` and `B(M×D_Q)≤T`. On the *same* locale `Γ×M`, both projections onto the strip domains are homeomorphisms, because `Γ→D_P` and `Γ→D_Q` are homeomorphisms. Hence `B(Γ×M)` factors through the pullbacks of both copies of `T`, giving an actual composable sublocale. Its outer-coordinate image lies in `T∘T`. Projection `Γ×M→Γ` is open surjective, and the image of `B(Γ×M)` is dense in `Γ`, so that image contains `B(Γ)`. **Restrict to the graph before composing**; density on the full `D_P×M×D_Q` is not enough to survive a nowhere-dense graph restriction. ∎

## 6. Theorem B: equality on the open cross-gap rectangle

**Theorem B (cross-gap restricted effectivity, audit candidate).** Under the finite-fence hypotheses,

\[
 \boxed{\mathcal K_q\wedge(U_P\times U_Q)
       =(T\circ T)\wedge(U_P\times U_Q)
       =G_P^*\times G_Q^*.} \tag{53}
\]

**Proof.** The exact equalizer identification is (E). By Theorem A, the pullback of `G_P^*×G_Q^*` along `p×p` is the patch generic product `F`, and the restriction of `p×p` to `F` is an isomorphism onto `G_P^*×G_Q^*`.

Put `R=(p×p)^{-1}(T∘T)`, a sublocale of the regular Hausdorff patch square. Suppose `F≰R`. Regular locales are fit, hence all their sublocales are fitted. There is therefore a patch-open sublocale containing `R` but not `F`; its patch-closed complement `C` satisfies `R∧C=0` and `F∧C≠0`.

Restrict `F∧C` to some patch-open rectangle compactly contained in `U_P×U_Q` on which it remains nonzero, and take the least closed support `C_0` of that restriction. Lemmas 1–5 produce a compact Cantor graph `Γ⊂C_0⊂C` with selected perfect antichain projections. Lemma 6 gives nonzero `B(Γ)≤F`; Lemma 8 places the same sublocale in the patch pullback `R` (indeed its map to `X²` factors through `T∘T`). Thus `0≠B(Γ)≤R∧C=0`, contradiction. Hence `F≤R`.

The isomorphism `(p×p)|_F:F≅G_P^*×G_Q^*` transports this factorization to the **upper** square, proving `G_P^*×G_Q^*≤T∘T`. Conversely `T≤K_q`, so `T∘T≤K_q` by transitivity, with no general associativity claim. Together with (E), this yields (53). ∎

## 7. Audit priorities and limits

This note does **not** assert global `(H_G∘H_G)∘(H_G∘H_G)=K_q`. The central remaining difficulty is combining restricted equalizer calculations over the entire upper square without an illicit infinitary join/interchange or proper-descent argument.

Independent referee priorities:

1. Test Theorem A's local-finiteness and **arbitrary-family** join calculation, and the inference from pointless to zero intersection with closed discrete sublocales.
2. Attack the finite-component cutoff and the richness lemma for arbitrary **nonspatial** closed support.
3. Examine every step of Lemma 5's ternary fusion, especially the simultaneous selected-color anchors, reserved-component condition, antichain projections, and persistence of anchors.
4. Test the two-sided generic point conditions in Lemma 6.
5. Verify the perfected dense-strip lemma and graph-specific `Γ×M` image, with all localic product/projection hypotheses.
6. Verify use of fittedness and **restricted** descent via Theorem A; do not invoke general proper descent of `p`.
7. Look for a small model or explicit counterexample if any claim fails, and distinguish repairs from genuinely false conclusions.

**Background sources:** J. Picado and A. Pultr, *Frames and Locales: Topology without Points* (regular/fit locales and sublocale nuclei); A. Jung, A. Kegelmann and M. A. Moshier, *Stably Compact Spaces and Closed Relations* (compact pospaces); M. H. Escardó, *The regular-locally-compact coreflection of a stably locally compact locale* (patch). The present arguments are intended to be self-contained apart from standard locale facts just named.
