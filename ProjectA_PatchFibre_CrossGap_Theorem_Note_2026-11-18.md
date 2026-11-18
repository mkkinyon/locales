# Project A — pointless patch fibres and the open cross-gap equalizer

**18 November 2026.** Consolidated research theorem note, updated after the independent blind referee report and addendum of the same date. **Status:** Theorems A and B and Lemmas 1–8 passed independent review under the finite-fence geometric hypotheses below. The referee requested precise patch/upper typing, a global two-phase fusion induction, and a compact-support clarification; these repairs are included here. Theorem C and Corollary A.1 record the referee's subsequently checked addendum. Nothing here proves the global assertion `K_q = T∘T`.

## 1. Construction and conventions

Let `P=[0,1]` with its Euclidean patch topology and the closed height-one partial order of the finite-fence construction. Its nontrivial comparability components are two disjoint sequences of finite connected zigzag fences `P_n` and `Q_n`; all other components are singletons. Every strict order pair lies along one edge of one fence. Each edge in the `n`th fence has Euclidean length `<1/n`, and no strict chain has length two. All fence vertices are distinct. Set

\[
 E_P=\bigcup_n V(P_n),\qquad E_Q=\bigcup_nV(Q_n),\qquad E=E_P\cup E_Q.
\]

The `P_n` travel through the geometric gap between two disjoint compact Cantor antichains `K<M`; the `Q_n` travel through the gap between `M<L`. Their endpoints in `M` enumerate disjoint dense countable sets `A={a_n}` and `B={b_n}`. Every sufficiently late `P_n` visits every prescribed nonempty upper-open subset compactly contained in the first gap, and likewise `Q_n` in the second. In fact the mesh estimate gives this for every fixed nonempty open subinterval of its gap.

For clarity, the geometric facts used in the proofs are:

1. Each component is finite (apart from singleton components), there are finitely many components of index at most `n`, and strict edge lengths tend to zero.
2. No two vertices in distinct components are comparable; each nontrivial component has height one, so each strict order pair joins a minimal and a maximal vertex.
3. Every sufficiently late `P_n` (respectively `Q_n`) visits every fixed nonempty Euclidean open subinterval of its own gap.
4. The middle endpoints `a_n,b_n` are pairwise distinct, and each colour's endpoints are dense in the perfect compact set `M`.
5. A patch-closed component-saturated set meeting infinitely many fence components contains **all** of `E`; thus any generic-neighborhood complement meets `E` only finitely.
6. Compact cutoffs inside either chosen mediator meet no components of the other colour, and the mediators' closures lie strictly inside their disjoint gaps.

These are the **assumed finite-fence geometric properties**; the present note does not independently construct every vertex by coordinates. Theorem A needs only the closed order and the first two shrinking/finiteness properties. The cross-gap and graph-generation theorems also use the remaining density, forcing and gap-separation properties.

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

**Proof of (E), included for completeness.** The reverse inclusion follows because the two generic factors both map constantly to the point sublocale `[p_∞]`, so their product factors through the kernel pair.

For the upper inclusion put `Z=K_q∧(U_P×U_Q)`. If a quotient open `V` does not belong to the neighborhood filter of `p_∞`, its upper-open inverse image `q^{-1}V` misses `E`. As `E_P` is dense in the first gap and `E_Q` in the second, this inverse image restricts to zero on **both** `U_P` and `U_Q` (a nonempty patch-open trace would contain a fence vertex). Thus both projections of `Z` satisfy the required negative point tests.

Suppose next that `V∈p_∞` and let `S=P\setminus q^{-1}V`. This is patch-closed, component-saturated and meets `E` finitely. Choose a compact patch-closed cutoff `C_P` with `\overline{U_P}⊂\operatorname{int}C_P` and `C_P` wholly inside the first gap. Let `A_P=S∩C_P`; saturate `A_P` by adjoining the **finitely many entire** `P_n` components it meets. The result `S_P` is compact, closed, saturated and contained in `S`, with `S_P∩U_P=S∩U_P` and `S_P∩U_Q=∅`. Its complement descends to a quotient open `V_P∈p_∞`. The trace of `q^{-1}V_P` on `U_P` agrees with that of `q^{-1}V`; its trace on `U_Q` is top. Since the two quotient-coordinate maps agree on `Z`, testing them against `V_P` forces the first projection of `Z` to lie in `q^{-1}V`.

Perform the symmetric construction with a compact cutoff `C_Q` inside the second gap. The resulting quotient open `V_Q∈p_∞` has top trace on `U_P` and the same trace as `V` on `U_Q`; the equalizer test forces the second projection of `Z` into `q^{-1}V`.

Thus **both** projections of `Z` satisfy all positive and negative quotient-open tests for `[p_∞]`. Hence `Z≤G_P^*×G_Q^*`, proving (E). This uses only disjoint compact cutoffs and finite-component saturation, **not** any global patch-descent theorem. ∎

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

For a pointless `S≤X`, `S∧D=0`: every sublocale of the closed discrete locale `D` is spatial. Indeed, if `j` is a nucleus on the powerset frame `\mathcal P(D)`, then inflationarity and meet preservation imply

\[
j(A)=A\cup j(\varnothing).
\]

To see the nontrivial inclusion, `j(A)\cap(D\setminus A)\subseteq j(A)\cap j(D\setminus A)=j(\varnothing)`. The quotient is therefore the powerset of `D\setminus j(\varnothing)`. In particular, every nonzero sublocale has an ordinary point. Let `λ:O(X)↠O(S)` be restriction. Within `W`, the open `R` and its closed complement `D` have join `W`; finite distributivity of the sublocale lattice and `S∧D=0` imply `λ(W)=λ(R)`. Hence

\[
 λr(\bigcup_iO_i)=\bigvee_iλr(O_i). \tag{A3}
\]

Combined with preservation of finite meets, `ρ=λr:O(P_patch)→O(S)` is a **frame homomorphism**, despite the fact that `r` itself need not preserve joins. Since `ρi=λ`, its locale map `s:S→P_patch` satisfies `p∘s` equal to the inclusion `S→X`; the pullback universal property gives a section `\bar s:S→p^{-1}(S)` of `p_S`.

Conversely, `p^{-1}(S)` is pointless. For every patch-open `O`, the difference `D_O` is closed discrete relative to `O` and so meets `p^{-1}(S)` in zero. Therefore `O` and `r(O)` have **identical** restrictions to `p^{-1}(S)`. Every open of the latter is consequently the restriction of an upper-open; i.e. `p_S^*:O(S)→O(p^{-1}S)` is surjective. The section makes it injective. This proves (A). ∎

**Scope warning.** The patch counit `p` is not a closed map in this example (a maximal fence singleton is patch-closed but not upper-closed). Theorem A neither asserts that `p` is Vermeulen-proper nor invokes any general proper-descent theorem. It works for the *specific pointless pullbacks*.

**Corollary A.1 (minimal-vertex avoidance; referee addendum).** Let `M_min` be the set of minimal vertices in nontrivial fence components. The same comparison `p^{-1}(S)→S` is an isomorphism for **any** sublocale `S≤X` satisfying

\[
S\wedge[m]=0\qquad(m\in M_{\min}). \tag{M}
\]

**Proof.** Each discrepancy `D` from (A2) is a discrete sublocale of an upper-open and is supported on `M_min`. If `S∧D` were nonzero, the discrete-sublocale argument just given would produce an ordinary point `[m]≤S` for some `m∈M_min`, contrary to (M). Thus `λr` preserves arbitrary joins and the section exists just as before. Likewise `D_O=O\setminus r(O)` is patch-discrete and supported on `M_min`. Any point of a nonzero meet `p^{-1}(S)∧D_O` would map under `p` to an ordinary minimal vertex point of `S`, again contradicting (M). Hence upper opens still generate the opens of `p^{-1}(S)`, and the comparison is an isomorphism. This includes pointful examples (e.g. a maximal fence vertex or a singleton component). The hypothesis is sufficient, not asserted necessary. ∎

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

In applying this lemma to a nonzero closed restriction `F∧C`, choose a patch-open rectangle `V` with **compact closure contained in** `U_P×U_Q` and `F∧C∧V≠0`. Take `C_0` to be the *least ambient patch-closed support* of that restriction, not merely its closure relative to the open rectangle. Then `C_0⊂C∩\overline V`, so `C_0` is a compact Euclidean-closed subset of the patch square, and the restricted sublocale is dense in `C_0` by minimality. Such a rectangle exists because the relatively compact rectangles cover the mediator product.

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

**Global two-phase construction at depth `n`.** There are only finitely many nodes `s` of depth `n`. Keep every old anchor `z_s` as the proposed anchor of child `s0`.

**Phase I: choose all new anchors before shrinking any rectangles.** Process the finitely many nodes sequentially. At each node use Lemma 3 to choose a colour-`P` anchor for child `s1` and a colour-`Q` anchor for child `s2`, inside `C_0∩int R_s`, in respectively fresh selected components of index `>n+1`. At every choice forbid, in **each coordinate separately**, (i) every vertex of every already registered finite component, (ii) every coordinate value of old or newly chosen anchors that could conflict with a sibling, and (iii) all as-yet unreserved vertices in the first `n+1` components. The forbidden sets are finite unions of closed nowhere-dense coordinate sections in `C_0`, so selected anchors of arbitrarily large index remain available. Immediately after **each** new anchor is chosen, register the entire finite fence component containing either of its coordinates if that coordinate is a fence vertex, including its *unselected* coordinate. The two registries are global for the entire level, not local to individual parents.

**Phase II: shrink all children using the final registries.** Only after anchors at **every** depth-`n` node are fixed, choose disjoint small closed coordinate intervals around all three anchors within each parent rectangle. Require diameter `<2^{-(n+1)}`; forbid (i) every vertex other than its designated anchor coordinate in every registered component for that coordinate, and (ii) every vertex of each still-unreserved component of index at most `n+1`. These are finite exclusions, and no forbidden value is an anchor: previous anchors are registered when selected, and all new anchors avoided the previous registries. Hence sufficiently small intervals exist. They enforce the component-exclusion invariant **globally across all new children**, including components reserved at nodes processed late in Phase I. All anchors lie in the interiors of their child rectangles.

Define

\[
 \Gamma=C_0\cap\bigcap_n\bigcup_{|s|=n}R_s. \tag{CG}
\]

Nested compactness and shrinking diameters give exactly one limit point on each infinite branch. The three disjoint children guarantee a Cantor space with no isolated points; disjoint sibling intervals in **each** coordinate make both projections injective. Every selected anchor persists on the branch obtained by continually taking child 0, so each cylinder meets a first-selected anchor from its child 1 and a second-selected anchor from its child 2. These anchors are dense in the two projections.

Finally, suppose two distinct first-coordinate limit points were vertices in one fence component of index `j`. At any depth beyond `j`, the component-exclusion invariant permits at most the one registered vertex of that component in the union of all intervals. This is impossible. The same argument applies to the second projection. Since all strict comparabilities are within finite fence components, both projections are antichains. ∎

**Audit history.** The independent referee specifically checked the finite-component exclusions and supplied the global two-phase formulation above. The original per-node phrasing was insufficiently explicit about later reservations at other nodes of the same level.

## 5. Booleanization of the graph and the two-step strips

Write `B(Z)` for the least dense sublocale (double-negation Booleanization) of `Z`.

**Ambient typing convention.** `D`, `M`, and `Γ` in this section carry their **Euclidean patch** topologies, whereas `H_G` and `T` are sublocales of the **upper** square `X×X`. Define the sublocales of the patch square

\[
\widehat H=(p\times p)^{-1}(H_G),\qquad
\widehat T=(p\times p)^{-1}(T),\qquad
\widehat{T^{[2]}}=(p\times p)^{-1}(T\circ T). \tag{PT}
\]

Here `\widehat{T^{[2]}}` is a single pullback of the *already composed* upper relation; no equality with `\widehat T\circ\widehat T` is assumed. All Booleanization inclusions below are made in the patch square, equivalently as factorization statements for maps into `X×X`.

**Lemma 6 (generic inclusion, with both point tests).** The graph from Lemma 5 satisfies

\[
 0\ne\mathcal B(\Gamma)\le F. \tag{B1}
\]

**Proof.** If `V` is a quotient-open neighborhood of `p_∞`, its closed saturated complement meets `E` finitely. Since the selected traces are dense in the perfect projections `D_P,D_Q`, the intersections of those projections with the complement are nowhere dense. The two pullbacks of `V` to `Γ` are therefore dense opens containing `B(Γ)`. If `V` does *not* belong to `p_∞`, its saturated pullback misses `E`; being patch-open, it cannot meet either `D_P` or `D_Q` at all, because the selected vertices are dense there. Thus the positive and negative tests of the point sublocale `[p_∞]` both hold. Equivalently, use the known exact patch-fibre formula `p^{-1}G=\Lambda_E`, the meet of complements of patch-closed sets meeting `E` finitely. Both routes give (B1). ∎

**Lemma 7 (corrected dense strips).** For a **perfect compact antichain** `D⊂U_P` with dense `D∩E_P` (or analogously `D⊂U_Q` with dense `D∩E_Q`),

\[
 \mathcal B(D\times M)\le\widehat T,
 \qquad\mathcal B(M\times D)\le\widehat T. \tag{DS'}
\]

**Proof.** In `D×U_P`, component-equivalent ordinary pairs are dense: every nonempty relative open in `D` contains selected vertices from arbitrarily late fences, and each late fence visits every prescribed nonempty open in `U_P`. Thus `B(D×U_P)≤\widehat H`. Likewise ordinary component pairs are dense in `U_P×M`, using the dense sequence `a_n`, so `B(U_P×M)≤\widehat H`. Their pullbacks to `D×U_P×M` along the open product projections are dense sublocales, and their meet contains the least dense sublocale of that triple. Its image in the upper triple is a genuine composable witness for the two copies of `H_G`. Projecting to `D×M` along the open surjection gives a dense patch image whose map into the upper square factors through `H_G∘H_G=T`; hence that image contains `B(D×M)` and establishes the stated *patch-typed* inclusion. Reverse coordinates or exchange colors to obtain the remaining cases. **Perfection (or the explicit unbounded-index condition) is essential**: the claim is false for a singleton fence vertex. ∎

**Lemma 8 (graph-restricted composition).** For the graph in Lemma 5,

\[
 \boxed{\mathcal B(\Gamma)\le\widehat{T^{[2]}}.} \tag{B2}
\]

**Proof.** By Lemma 7, `B(D_P×M)≤\widehat T` and `B(M×D_Q)≤\widehat T`. On the *same* locale `Γ×M`, both projections onto the strip domains are homeomorphisms, because `Γ→D_P` and `Γ→D_Q` are homeomorphisms. Hence `B(Γ×M)` factors through the pullbacks of both copies of the upper relation `T`, giving an actual composable sublocale over the upper triple. Its outer-coordinate image in the upper square lies in `T∘T`. Projection `Γ×M→Γ` is open surjective, and the patch image of `B(Γ×M)` is dense in `Γ`, so that image contains `B(Γ)`. This proves the stated patch-pullback inclusion. **Restrict to the graph before composing**; density on the full `D_P×M×D_Q` is not enough to survive a nowhere-dense graph restriction. ∎

## 6. Theorem B: equality on the open cross-gap rectangle

**Theorem B (cross-gap restricted effectivity; externally audited).** Under the finite-fence hypotheses,

\[
 \boxed{\mathcal K_q\wedge(U_P\times U_Q)
       =(T\circ T)\wedge(U_P\times U_Q)
       =G_P^*\times G_Q^*.} \tag{53}
\]

**Proof.** The exact equalizer identification is (E). By Theorem A, the pullback of `G_P^*×G_Q^*` along `p×p` is the patch generic product `F`, and the restriction of `p×p` to `F` is an isomorphism onto `G_P^*×G_Q^*`.

Put `R=(p×p)^{-1}(T∘T)`, a sublocale of the regular Hausdorff patch square. Suppose `F≰R`. Regular locales are fit, hence all their sublocales are fitted. There is therefore a patch-open sublocale containing `R` but not `F`; its patch-closed complement `C` satisfies `R∧C=0` and `F∧C≠0`.

Choose a patch-open rectangle `V` with compact closure inside `U_P×U_Q` such that `F∧C∧V≠0`, and let `C_0` be the least **ambient patch-closed** support of this restriction. Then `C_0⊂C∩\overline V` is compact. Lemmas 1–5 produce a compact Cantor graph `Γ⊂C_0⊂C` with selected perfect antichain projections. Lemma 6 gives nonzero `B(Γ)≤F`; Lemma 8 places the same sublocale in the patch pullback `R` (indeed its map to `X²` factors through `T∘T`). Thus `0≠B(Γ)≤R∧C=0`, contradiction. Hence `F≤R`.

The isomorphism `(p×p)|_F:F≅G_P^*×G_Q^*` transports this factorization to the **upper** square, proving `G_P^*×G_Q^*≤T∘T`. Conversely `T≤K_q`, so `T∘T≤K_q` by transitivity, with no general associativity claim. Together with (E), this yields (53). ∎

## 7. Theorem C: Cantor graphs generate the generic product

Let `\mathscr C` denote the set of all nonempty compact Cantor graphs `Γ⊂U_P×U_Q` such that both coordinate projections are homeomorphisms onto compact Cantor antichains `D_P,D_Q`, with `D_P∩E_P` and `D_Q∩E_Q` dense in their respective projections.

**Theorem C (graph generation; referee addendum).** In the **patch** square,

\[
\boxed{F=\bigvee_{\Gamma\in\mathscr C}\mathcal B(\Gamma).}\tag{G}
\]

Consequently, for **every** patch-square sublocale `R`,

\[
\boxed{F\le R\quad\Longleftrightarrow\quad
\mathcal B(\Gamma)\le R\text{ for all }\Gamma\in\mathscr C.}\tag{G'}
\]

**Proof.** Lemma 6 uses only the perfect antichain projections and the two dense selected traces, so `B(Γ)≤F` for every `Γ∈\mathscr C`. Put `J=⋁_{Γ∈\mathscr C}B(Γ)`; then `J≤F`. Suppose `F≰J`. Fittedness of the regular patch square gives a patch-closed sublocale `C` such that `J∧C=0` but `F∧C≠0`. Restrict `F∧C` to a relatively compact patch-open rectangle `V⊂U_P×U_Q` where it remains nonzero, and take its least **ambient closed** support `C_0⊂C∩\overline V`. Lemmas 2–5 produce `Γ∈\mathscr C` contained in `C_0`. But Lemma 6 gives `0≠B(Γ)≤J∧C`, a contradiction. Thus `F=J`, and (G') is immediate. ∎

Theorem A identifies `F` isomorphically with the generic product `G_P^*×G_Q^*` in the upper square. Under that **specific isomorphism**, the sublocales `B(Γ)` transfer to a generating family for the upper generic product. There is no assertion that arbitrary relation composition commutes with the join in (G).

**Structural use.** Theorem B may be split into the graph-generation theorem (G), which mentions no relation `T`, and the separate relation-specific inclusion `B(Γ)≤(p×p)^{-1}(T∘T)` for each graph, furnished by Lemmas 7–8. This separation makes (G') available for testing other candidate relations.

## 8. Audit record and limits

This note does **not** assert global `(H_G∘H_G)∘(H_G∘H_G)=K_q`. The central remaining difficulty is combining restricted equalizer calculations over the entire upper square without an illicit infinitary join/interchange or proper-descent argument.

The independent blind referee of 18 November 2026 accepted Theorems A and B and their supporting lemmas relative to the stated geometry, requesting the following clarifications, all incorporated in this revision:

1. Type the patch Booleanization statements as pullbacks from upper-square relations.
2. Choose all new anchors at a given finite depth before shrinking the rectangles, with global per-coordinate component registries.
3. Use compact **ambient** closed supports of restrictions to relatively compact rectangles.
4. Spell out the nuclei calculation for arbitrary discrete locales.
5. Itemize the finite-fence geometric assumptions, which were not independently reconstructed from coordinates.

The subsequent referee addendum proposed Theorem C (G) and Corollary A.1 (M); their arguments have been independently checked internally and are recorded above. Neither result is a global kernel-pair decomposition.

**Background sources:** J. Picado and A. Pultr, *Frames and Locales: Topology without Points* (regular/fit locales and sublocale nuclei); A. Jung, A. Kegelmann and M. A. Moshier, *Stably Compact Spaces and Closed Relations* (compact pospaces); M. H. Escardó, *The regular-locally-compact coreflection of a stably locally compact locale* (patch). The present arguments are intended to be self-contained apart from standard locale facts just named.
