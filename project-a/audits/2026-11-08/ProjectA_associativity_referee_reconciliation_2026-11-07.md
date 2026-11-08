# Project A — Reconciliation of the external blind associativity referee report

**Date:** 7 November 2026. **Independent report:** `ProjectA_associativity_EXTERNAL_BLIND_report.md` (Claude Fable 5.1, High effort). This reconciliation is a *subsequent internal assessment*; it is not part of the blind audit and makes no literature-priority claim.

## 1. Accepted core verdict

The external referee independently checked Arrieta's construction (in the cited arXiv version), the open-cover formula for `D_Y`, the `V^2` restriction `A`, the Boolean test, the three coordinate permutations, all-cover positive assertions, and the explicit separating admissible cover. The referee found no major or moderate errors in the propositions checked and certified

\[
 A\circ A\not\subseteq A,\qquad \mathcal D_Y\circ\mathcal D_Y\not\subseteq\mathcal D_Y,
\]

for Arrieta's **spatial strongly Hausdorff** locale `Y` of Example 4.5. This is a strengthening in scope over the previously independently audited general transfer example `X_u`: the base `Y` itself has nontransitive fitted diagonal.

The referee independently verified the mixed-block vanishing and exact decomposition `D_Y = A ∨ Δ_N`, hence the reduction of cube associativity of `D_Y` to that of `A`. Both bracketings of the cube **remain open**.

The simpler proof that `D_Y²⊄D_Y` follows directly from the open embedding `V²→Y²` and `A≤D_Y`: no block decomposition is needed for this implication. Keep the block result for the *equivalence* of cube questions.

## 2. Scope of the external certification

**Verified:** cover presentation, Arrieta topology and admissible-cover normal form, `A` formula, mixed blocks and `N²` block, cube reduction, the `RO(V)`-valued permutation triple, permutation criterion, diameter-two Boolean permutation family, diagonal singleton fibers of all finite bracketed powers, failure of surjection stability along a discrete refinement, and the exact but tautological cube-congruence criterion.

**Not checked:** transfer along a Sierpiński extension `X_u`; the seven-of-eight three-letter `I,D` associativity claims; the example of general relational nonassociativity for one symmetric reflexive endorelation; the universal `I D≤U` background assertion (audited separately); and the optional assertion that the projections of `A` are neither open nor proper. The last assertion needs exact stability citations or should be omitted.

**Open:** `(A²)A = A(A²)` and equivalently the `D_Y` cube.

## 3. Presentation repairs accepted

1. Replace the invalidly general 'no ordinary points means zero sublocale' wording for the mixed fibers by the **closed-pullback calculation** `j^{-1}[c(C\setminus K_n)]=c(j^*(C\setminus K_n))=c(1_V)=0`. The proof of vanishing is correct with this repair.
2. Explicitly display the support convention `(\widehat\pi x)_j=x_{\pi^{-1}(j)}`; without it, the `τ`-witness cylinder can be misread.
3. Explain the construction of each separating Cantor-clopen neighborhood `W_n`; the referee supplies a compactness/separation argument.
4. Clarify that the discrete-refinement pullback is along the **first** projection, and that open/closed endpoint embeddings—not general fitted sublocales—allow the relevant base change.
5. Avoid overloading `D` (the countable deleted subset vs fitted diagonal), `K_n` vs endpoint congruence kernels, and `B` (regular-open Boolean frame vs cylinders). Credit the original Juhász–Soukup–Szentmiklóssy construction via Arrieta.
6. Make clear that the packet's motivation cites other project results which were **not** independently checked in this particular audit. No general product-spatiality assumption is used in the central proof.

## 4. New referee proposals: promising but separate from blind certification

**N1. Density and anti-Urysohn.** The referee argues each admissible-cover square `γ_C` is dense in `O(V²)`. Therefore `A` contains the least dense (Booleanization) sublocale `𝔅(V²)`. He proves a more general equivalence: `L` anti-Urysohn iff *every* diagonal cover-square is dense in `L⊕L`. The proof is short and plausible on direct recheck: if a nonzero rectangle misses a cover-square, every cover member is disjoint from one of its nonzero factors, forcing `a*∨b*=1`; conversely a far pair produces an obstructing two-member cover. This is a **new referee-derived lemma**, to preserve separately and compare with Arrieta's Lemma 4.7/Prop. 4.8.

**N2. Pointless remainder.** The proposed identity `A=Δ_V∨G`, with

\[
G=\bigwedge_{(W_n)}O\left(\bigvee_n (W_n\cap V)\boxtimes(W_n\cap V)\right),\quad W_n\supseteq K_n,
\]

looks valid: every admissible cover can be augmented by the `W_n` traces without changing its square-open, and the coframe distributive law yields the split. `G` is fitted, symmetric, dense and has no ordinary points. The consequent expansions

\[
 A²=A\vee G²,\quad (A²)A=A\vee G²\vee(G²)G,\quad A(A²)=A\vee G²\vee G(G²)
\]

are safe two-factor calculations using the diagonal as a unit and distributivity over **finite joins**, not arbitrary associativity. Since `A` is symmetric, the cube associates iff `(A²)A` is symmetric; this last equivalence actually holds for *any* symmetric endorelation, independently of the decomposition.

**N3. Boolean sequence model.** The referee suggests representing Boolean generalized points of `V=C\setminus D` by Boolean-valued bit sequences avoiding every ground-model nonzero finite-support sequence. The proposed test for `A` is `g_m(x,y)≥[x≠y]` for every `m:N→N` with `m(n)≥n`, and the test for `G` is `g_m(x,y)=1`. This is a useful conditional research model, **not** a proof of any composite-image formula: Boolean-valued points of the image need not lift along arbitrary surjections.

**Terminology/verification caution:** D.3 appeals to 'complete distributivity in B'. An atomless complete Boolean algebra such as `RO(V)` is **not** completely distributive in the standard lattice-theoretic sense (complete distributivity of a complete Boolean algebra implies atomicity). The individual formulas may be obtained without it, using only frame distributivity, Boolean De Morgan laws, and the universal nucleus of a closed-plus-open join. For a closed `C(d)` and an open `O(g)` in any locale, the nucleus of `C(d)∨O(g)` is

\[
  j(t)=(d\vee t)\wedge(g\to t).
\]

A frame map `h` factors through this join iff `h(d)≤h(g)`: necessity follows by evaluating `j(g)=d∨g`, and sufficiency follows from `h(g→t)≤h(g)→h(t)`. For Boolean bit pairs, `h(d_Δ)=[x≠y]` and `h(g_m)=g_m(x,y)`. This gives the intended `A` test with *no* complete-distributivity axiom. The representation of `V` itself as a meet of point-complement opens should remain explicitly justified (the referee gives a Polish/Cantor–Bendixson argument).

**N4. Uncountable filter genuinely necessary.** The referee shows the family `m(n)=n+k` is insufficient. A sharper argument establishes that **no countable subfamily** suffices: `V` is dense `G_δ` in Cantor space and hence Polish, so `V×V` is Baire. Every `g_m` is an open dense subset of the ordinary product (by the cylinder argument in N1), hence any countable intersection of the `g_m` contains an ordinary point. But `G` has *no* ordinary points (choose a neighborhood of each finite `K_n` avoiding a fixed `x∈V`). Thus `G` cannot equal any countable submeet of these opens. This independently strengthens the referee's particular gap-sequence illustration. It does not decide the cube.

**N5. Closed-graph and naive-bound strategies.** The suggested `G²` naive-bound test and restrictions along closed graphs are legitimate possible starting points *if the composition investigation is resumed*. One caution: knowing `𝔅(Γ_f)≤A²` for a coordinate permutation `f` by itself does **not** show the two cube bracketings have equal intersections with the **whole graph** `Γ_f`. Thus 'coordinate permutations will not work' should be read only as 'the current Booleanized-graph witnesses do not distinguish them', not as a proven no-go theorem.

## 5. Inventory updates

- Upgrade **R6** to **E (within the supplied packet's scope)**: externally verified nontransitivity of `D_Y` on spatial strongly Hausdorff `Y`.
- Add **R6a**: block decomposition and equivalence of the two cube questions — E.
- Add **R6b**: permutation-family criterion, singleton-point fibers and discrete-refinement base-change obstruction — E, with the exact verified qualifications.
- Keep **R8** O: cube associativity unresolved.
- Keep **R3, R4, R7** at their prior independent statuses: not part of this referee's checking.
- Keep **N1–N5** as referee-originated **working** structural contributions, not externally corroborated theorems merely because they occur in a referee report.

## 6. Disposition and research schedule

Accept the strong nontransitivity theorem and source repairs. Preserve the original external report unchanged. In a later focused investigation, study the `G` decomposition and `G²` compatibility bound before performing more cube-congruence expansions. For now return to the theorem/dependency inventory and its arbitrary-locale classification section; do not reopen the cube question solely because the referee supplied attractive new formulations.