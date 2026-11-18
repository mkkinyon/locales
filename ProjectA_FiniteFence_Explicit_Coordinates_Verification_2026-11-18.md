# Project A — explicit coordinates for the two-colour finite-fence compact pospace

**18 November 2026. Direct geometric verification.** This note fills the coordinate-level gap identified in the independent finite-fence audit reports. It supplies an explicit recursive choice of vertices and checks the geometric assumptions used in the subsequently audited patch-fibre, restricted cross-gap, and global generic-square theorems. It also verifies the segment-confinement hypothesis needed for the new, internally audited mixed-colour two-step obstruction. The *localic proofs* from those separate notes are not silently reproved here; this note verifies their input data.

## 1. Three explicit Cantor sets and two disjoint dense endpoint sequences

Let

\[
\mathfrak C=\left\{\sum_{j=1}^{\infty}\frac{2\varepsilon_j}{3^j}:\varepsilon_j\in\{0,1\}\right\}\subset[0,1]
\]

be the standard ternary Cantor set. Define

\[
K=\tfrac1{10}+\tfrac1{10}\mathfrak C\subset[.1,.2],\qquad
M=\tfrac4{10}+\tfrac1{10}\mathfrak C\subset[.4,.5],\qquad
L=\tfrac7{10}+\tfrac1{10}\mathfrak C\subset[.7,.8].\tag{C1}
\]

These are pairwise disjoint compact perfect Cantor sets with `K<M<L`. The fixed geometric gaps are

\[
I_P=(.2,.4),\qquad I_Q=(.5,.7).\tag{C2}
\]

Write `C_0` for the points of `𝔠` represented by binary sequences which are eventually **zero**, and `C_1` for those represented by sequences eventually **one**. Both are countable and dense in `𝔠`, and they are disjoint: ternary expansions using only digits `0,2` are unique (if the first differing digit is in position `k`, the leading difference `2/3^k` exceeds the maximum opposing tail `1/3^k`). Put

\[
A=\tfrac4{10}+\tfrac1{10}C_0,\qquad
B=\tfrac4{10}+\tfrac1{10}C_1,\tag{C3}
\]

and fix **any** repetitions-free enumerations `A={a_n:n≥1}` and `B={b_n:n≥1}`. Since every nonempty relatively open subset of a perfect Cantor set contains infinitely many members of either dense set, the indices lying in any prescribed nonempty relative open part of `M` are unbounded for both sequences. Use the affine homeomorphisms

\[
f:M\to K,\quad f(t)=t-.3,\qquad
g:M\to L,\quad g(t)=t+.3.\tag{C4}
\]

The four endpoint families `f(a_n),a_n,b_n,g(b_n)` have no collisions, either within or across colours.

## 2. An explicit recursive construction of the vertices

Fix once and for all an enumeration of the rationals in `(0,1)`. Construct `P_1,Q_1,P_2,Q_2,…` in that order. A general fence has distinct endpoints `u<v` of one of the forms

\[
(u,v)=(f(a_n),a_n)\quad\text{or}\quad(u,v)=(b_n,g(b_n)).
\]

Let `n` be its index, and let `V_{old}` be the **finite** set of vertices already chosen in earlier construction stages. Choose an even integer `N=2m≥2` large enough that

\[
\Delta=(v-u)/N<\frac1{1000n}.\tag{C5}
\]

Set `x_0=u`, `x_N=v`. For each `1≤j<N`, let `x_j` be the first rational in the fixed enumeration belonging to

\[
\left(u+(j-\tfrac1{10})\Delta,\ u+(j+\tfrac1{10})\Delta\right)
\setminus(K\cup M\cup L\cup V_{old}).\tag{C6}
\]

These nonempty choices exist: the union `K∪M∪L` is closed nowhere dense, and the additional forbidden set is finite. The small intervals in (C6) are disjoint and lie strictly between the endpoints, so

\[
u=x_0<x_1<\cdots<x_N=v,
\qquad |x_{j+1}-x_j|<1.2\Delta<\frac1{800n}<\frac1n.\tag{C7}
\]

All interiors avoid the three Cantor sets and every earlier vertex. Future endpoints lie in `K∪M∪L`; future interiors avoid the vertices already chosen. Therefore **every vertex of every fence is distinct**, except for the intentional repeated use of an endpoint within its own fence. In particular the `P_n,Q_n` components are pairwise disjoint. The recursion is an explicit specification: the fixed rational enumeration resolves every remaining choice.

For the fence `x_0,…,x_N` declare each **even** vertex minimal, each **odd** vertex maximal, and put the strict comparisons

\[
x_{2i}<_{\!P} x_{2i+1},\qquad
x_{2i+2}<_{\!P} x_{2i+1}\quad(0\le i<m).\tag{C8}
\]

Include equality on all of `[0,1]` and no other comparisons. The direction of the *order* zigzags, while the vertex coordinates increase monotonically along the real interval. Hence every nontrivial comparability component is exactly one finite connected fence, all strict comparisons are edges, and there are no strict chains of length two. Antisymmetry and transitivity are immediate.

**Segment confinement is automatic:** every vertex of `P_n` lies in `[f(a_n),a_n]` and every vertex of `Q_n` in `[b_n,g(b_n)]`. Thus this realization satisfies (SC) from `ProjectA_MixedColour_TwoStep_Obstruction_2026-11-18.md`.

## 3. Closedness of the partial order and patch identification

The relation `≤_P` is closed in the Euclidean compact square `[0,1]²`. Indeed, the diagonal is closed; each individual finite fence contributes finitely many strict pairs; and by (C7), pairs from fences with indices tending to infinity have Euclidean distance between their coordinates tending to zero. Hence a limit `(x,y)` with `x≠y` of strict pairs must come from one of finitely many early fences, so it is itself one of their edges. There are no new off-diagonal limit comparisons.

Thus `([0,1],≤_P)` is a **compact Hausdorff pospace**. Its open upper sets form a stably compact topology `X` with specialization order `≤_P`; the patch topology of `X` is exactly the original Euclidean topology. This is the standard compact-pospace/stably-compact correspondence, for example Jung–Kegelmann–Moshier, *Stably compact spaces and closed relations*, Theorem 2.5 (https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf). Consequently the map `p:P_patch→X` used in the prior arguments is the canonical patch map and has the claimed type. It is **not** asserted to be a Vermeulen-proper map.

All three Cantor sets are antichains: their only fence vertices are designated **minimal endpoints**, and every other point of them is a singleton comparability component; no two distinct points of `K∪M∪L` are comparable.

The **upper-open mediator sets** required in the earlier theorems can also be specified. For a Euclidean-open `O⊂P` let `r(O)=P\setminus\downarrow(P\setminus O)={x:↑x⊂O}`. By compactness and closedness of the order, `r(O)` is Euclidean-open and upper. Take, for instance,

\[
U_P=r((.25,.35)),\qquad U_Q=r((.55,.65)).\tag{C8a}
\]

Both are nonempty: each displayed Euclidean interval contains points outside the countable fence-vertex set, and such singleton-comparability points belong to its upper core. Their Euclidean closures lie in the disjoint fixed gaps `I_P,I_Q`. The mesh argument below applies to **every** nonempty open part of these mediators, so in particular every sufficiently late fence of the appropriate colour visits them.

## 4. Gap traversal and the strong finite-fence forcing lemma

Every `P_n` spans the entire closed interval between some point of `[.1,.2]` and some point of `[.4,.5]`. Its increasing vertex mesh has maximum step `<1/(800n)`. Consequently for each `t∈I_P` there is a vertex of `P_n` at Euclidean distance `<1/(800n)` from `t`. Every sufficiently late `P_n` therefore meets every fixed nonempty open subinterval `J⊂I_P`, and the even (minimal) vertices alone have the same property, at distance at most twice the mesh. The identical argument applies to all `Q_n` across `I_Q`.

The chosen mesh is **uniformly** below `1/800`, smaller than either gap's width `1/5`. Thus **every** `P_n` has at least one vertex in `I_P`, and **every** `Q_n` has at least one vertex in `I_Q`; this is useful when saturating a closed set. Each colour's vertex set is dense in its fixed gap, and its minimal-vertex set is also dense there.

**Theorem C (strong closed-saturation forcing).** If `S⊂[0,1]` is Euclidean closed, is a union of comparability components, and meets infinitely many distinct nontrivial fence components, then `E=⋃_n(V(P_n)∪V(Q_n))⊂S`.

**Proof.** One of the two colours occurs infinitely often. Suppose `S` contains infinitely many `P_{n_j}`; necessarily `n_j→∞`. For each fixed `t∈I_P`, select `x_j∈V(P_{n_j})` with `|x_j-t|<1/(800n_j)`. Closedness of `S` gives `t∈S`. Therefore `I_P⊂S`. Every `P_m` has a vertex in `I_P`; saturation puts **all** `P_m` in `S`. In particular all `a_m` lie in `S`. Their density in `M` gives `M⊂S`, and the endpoint `b_m∈M` of each `Q_m` now forces all `Q_m⊂S`. Thus `E⊂S`. Starting from infinitely many `Q_n` uses `I_Q`, the dense set `B`, and then the `P_n` endpoints `a_n∈M` in the same way. ∎

This is exactly the strong geometric hypothesis that was previously left conditional. Note that the theorem explicitly concerns infinitely many **fence** components, not infinitely many arbitrary singleton components.

## 5. The component quotient and its generic fence-tail point

Let `E_G` be the set of all ordinary ordered pairs of points lying in one comparability component and `H_G=[E_G]≤X×X` the point-generated sublocale. Define the quotient locale `Q` by the subframe of **component-saturated upper opens** in `O(X)`, with `q^*:O(Q)↪O(X)` its inclusion. The subframe is closed under arbitrary unions and finite intersections. Because `H_G` is generated by the component pairs, the two projections `H_G⇉X` have the same `q`-composite. Conversely, an upper open equalized by these two projections must have constant membership on each component, so this is precisely their coequalizer frame.

Define

\[
\mathfrak p_\infty=\{U\in O(Q):q^{-1}(U)\cap E\ne\varnothing\}.\tag{C9}
\]

For any saturated upper open `V` meeting `E`, the closed saturated complement cannot contain infinitely many fence components by Theorem C; therefore it meets only finitely many of those components, and `V` contains all but finitely many entire fences. It follows that the intersection of any two opens in `\mathfrak p_\infty` still meets `E`. Arbitrary primality follows directly from unions meeting `E` exactly when one summand does. Thus `\mathfrak p_\infty` is a completely prime filter and defines the asserted point `p_∞∈pt(Q)`.

For any ordinary `x∈P`, its comparability component `C_x` is finite (a fence) or a singleton, hence Euclidean closed and saturated. Its complement is a saturated upper open which belongs to `\mathfrak p_\infty` but omits `x`. Accordingly `p_∞` is different from every ordinary quotient point `q(x)`.

Moreover, `q(x)=q(y)` for **ordinary** points precisely when `x,y` lie in the same component. The forward direction follows by separating any distinct components with the saturated upper open `P\setminus C_x`, which contains `y` but not `x`; the reverse direction is the defining saturation property. In particular, the ordinary point fibre of `q(x)` is exactly `C_x`. This statement does not assert that the entire **localic** kernel pair has only ordinary component pairs.

Theorem C also yields the two generic-neighborhood tests used throughout the earlier proofs: the complement of a quotient-open **containing** `p_∞` meets `E` in finitely many vertices; a quotient-open **not containing** `p_∞` misses `E` entirely. Compact patch-closed cutoffs meeting `E` finitely can be saturated by adjoining only finitely many complete fence components, preserving compact closedness. These assertions require no properness of `p`.

## 6. The separated mixed-colour subsequences are realized

The first-level ternary division of `M` yields nonempty relatively clopen Cantor pieces

\[
M^-\subset[.4,.433\overline3],\qquad M^+\subset[.466\overline6,.5].
\]

Choose, for instance, `r=.44` and `s=.46`. There are arbitrarily high indices with `a_n∈M^-`, and arbitrarily high indices with `b_m∈M^+`, because `A` and `B` are each dense in `M`. Segment confinement implies

\[
V(P_n)\subset[0,r]\quad(a_n\in M^-),\qquad
V(Q_m)\subset[s,1]\quad(b_m\in M^+).\tag{C10}
\]

Every one of these selected fences still spans the **whole corresponding fixed gap**, so its high-index minimal vertices visit every prescribed nonempty open subinterval of that gap. Therefore the exact separated-cofinal-subsequence hypothesis used in the internally audited mixed-colour obstruction is satisfied, not merely postulated.

**A further simplification specific to these coordinates:** the *global* strict-edge mesh `<1/(800n)≤1/800` is much smaller than `(s-r)/2=.01`. The proof of the finite mediator-overlap lemma shows that any point of `\downarrow[0,r]∩\downarrow[s,1]` would require an edge of Euclidean length at least `.01`. There is no such edge. Therefore in the present concrete model

\[
\boxed{\downarrow[0,.44]\ \cap\ \downarrow[.46,1]=\varnothing}.\tag{C11}
\]

The two selected colours admit **disjoint closed lower mediator bounds**, not merely bounds with finite early overlap. The general mixed-colour obstruction proof remains valid, but for this particular realization its finite-overlap elimination step is unnecessary.

## 7. Verification ledger and consequences

| Geometric input | Verified by |
| --- | --- |
| Distinct `K<M<L`, disjoint dense `A,B⊂M`, affine endpoint maps | (C1)–(C4) |
| Even finite height-one zigzags with pairwise distinct vertices | (C5)–(C8) |
| Mesh `<1/n` and no nontrivial strict chains of length two | (C7)–(C8) |
| Closed order, compact pospace, Euclidean patch topology | §3 |
| Nonempty separated upper-open mediators compactly contained in the gaps | (C8a), §3 |
| Late traversal of both fixed gaps; dense minimal vertices | §4 |
| Any closed saturated set meeting infinitely many fence components contains `E` | Theorem C, §4 |
| Component quotient with completely prime special point `p_∞` | §5 |
| Finite-component saturation of compact cutoffs | §5 |
| Segment confinement and separated cofinal subsequences | §§2, 6 |

**Consequence.** The previously independently audited *conditional* theorems about the patch special fibre, restricted cross-gap equalizer, and global generic-square inclusion now have an explicit compact-pospace model satisfying their stated geometric premises. The internally audited negative mixed-colour two-step result also has its additional (SC) premise satisfied in this model. In particular, **subject to the correctness of the earlier localic proofs and of the mixed-colour obstruction proof**, this is a concrete example in which

\[
G_P^*\times G_Q^*\le T\circ T,
\qquad G_P^*\times G_Q^*\not\le T,
\qquad T=H_G\circ H_G.
\]

This does **not** prove the unresolved full kernel-pair equality `K_q=T∘T`; nor does it fix the old invalid argument invoking proper descent along the patch counit. It replaces the previously unverified *geometric realization* premise with a direct construction.

**Audit scope:** The current coordinate proof has received a direct self-check but no independent external audit. For any eventual external package, include this file alongside the mixed-colour obstruction and the earlier conditional theorems; ask the referee specifically to test the recursive no-collision construction, the strong forcing lemma, and the coequalizer-frame identification.

## 8. Second internal adversarial audit (18 November 2026)

**Verdict:** No fatal gap found in the explicit coordinate and order construction. All numbered geometric hypotheses in §7 are accounted for. This is a second internal check, **not** a fresh external referee report and **not** a blanket verification of every dependent localic proof.

1. **Endpoint data.** Eventual-zero and eventual-one Cantor codes are individually countable dense sets and have no common points because ternary `0,2` coding is injective. Every nonempty relative Cantor open meets each in infinitely many points, hence the required index subsequences are unbounded for *arbitrary* repetitions-free enumerations.
2. **Recursive avoidance.** For each fixed `n`, earlier fences contribute only finitely many forbidden vertices. The finitely many current grid bands are disjoint, and each meets the rational complement of the finite union of nowhere-dense Cantor sets and previously used vertices. No future endpoint can collide with an interior vertex, because every endpoint is in `K∪M∪L`. The numeric bound `1.2Δ<1/(800n)` includes both endpoint edges.
3. **Order axioms and closure.** Even vertices have no strict incoming arrows, odd vertices no outgoing arrows; disjoint fences prevent cross-component chains. Thus the displayed relation is already reflexive, antisymmetric and transitive. Off-diagonal edge limits can only arise among finitely many bounded indices; any sequence of edges with indices tending to infinity approaches the diagonal. This proves closedness of the **entire** relation, not merely of each finite fence.
4. **Patch identification.** The compact-pospace correspondence applies after verifying the closed graph. The upper core formula produces actual nonempty upper opens compactly contained in each gap; using arbitrary Euclidean intervals as mediators without taking their upper cores would have been an unjustified shortcut.
5. **Forcing quantifiers.** An infinite collection of distinct fences of one colour has indices tending to infinity. *Every one* spans the corresponding fixed gap, with uniformly vanishing vertex mesh, so the closed set contains **every point** of that gap. The extra uniform mesh bound ensures even the earliest fences meet the gap, making saturation to all components immediate. Endpoint density then transfers forcing from one colour to the other.
6. **Quotient point and coequalizer.** Saturated upper opens form a subframe. Equality of the two projection pullbacks on the point-generated spatial locale `H_G` is equivalent to pointwise constancy along each finite component. For `p_∞`, finite meets are nonempty on `E` because each positive open contains all but finitely many fence components; complete primality is direct from set-theoretic unions. Complements of individual finite components separate `p_∞` from every `q(x)` and also distinguish distinct ordinary components.
7. **Sharp mediator separation.** With `r=.44`, `s=.46`, membership in both downward closures would force at least one strict comparison spanning `(s-r)/2=.01`. Since *every* strict edge has length `<1/800`, no such comparison exists: the intersection is empty, not merely finite. This requires height one; it should not be silently generalized to relations with longer strict chains.

**Remaining boundary of the result:** This note verifies the *geometric* premises, including the compact-pospace/patch typing and the quotient's generic point. The assertions concerning the nonspatial fibre `G`, Booleanizations of Cantor supports, the restricted equalizer, and the localic image calculations still rely on their **separately recorded proofs** and audit statuses. The invalid global proper-descent argument is not revived. No additional geometric assumption was found to be missing from the conditional statements used in the mixed-colour two-step calculation.
