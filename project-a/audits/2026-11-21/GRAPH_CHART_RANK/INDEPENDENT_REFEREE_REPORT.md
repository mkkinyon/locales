# Independent blind referee report
## Project A — graph extensions of the rectangular calculus and finite chart rank
**21 November 2026**

### 1. Executive verdict

**Verdict: CORRECT WITH MINOR REPAIRS, CONDITIONAL ON THE IMPORTED RECTANGULAR COMPOSITION THEOREM (RC).**

I read the seven substantive documents in the supplied blind packet in the specified order, without consulting the project repository or earlier internal/referee assessments. I checked the two quoted publications on Michael's zero-dimensional selection theorem independently. The essential positive theorem, the two negative graph examples, the nonassociative symmetric graph, and the exact chart-rank theorem survive the checks below. I found **no counterexample to a principal new theorem**. There are a few statements whose wording or proof should be tightened; particularly, the “exactly when” assertion about zero in the `RRR` case is literally false when an *outer* support is empty. This is a harmless bookkeeping error, not an associativity failure.

My certification has an important stated dependency: I have **not re-refereed (RC)**, the previously reviewed assertion that every nonzero middle overlap of point-generated/full localic rectangles produces the *full* endpoint rectangle. All associativity and rectangular-ideal conclusions below are conditional on that input. In contrast, the graph probes, both topological counterexamples, and the Michael-selection decomposition have independent proofs not relying on (RC).

The most informative feature of the packet is the distinction between:

* **finite locally closed partial-homeomorphism chart rank**, sufficient for safe algebraic adjunction of a graph;
* **uniform fiber multiplicity**, insufficient without some additional hypothesis; and
* **openness plus bounded finite multiplicity over a zero-dimensional metrizable target**, sufficient for *optimal* chart rank by selection theory.

No necessity theorem for finite chart rank has been established, and none should be inferred.

### 2. Claim ledger

| Claim | Verdict | Qualification |
|---|---|---|
| **LC / LCR** | **PASS** | Pullbacks against open and closed inclusions, composed, give the asserted spatial restrictions; the `q` product is treated genuinely locally. |
| **PH** | **PASS** | Both `p` and `q` formulas follow from the actual graph pullback, not from pointwise paths. |
| **H** | **PASS** | Locally closed embeddings are transitive; partial-homeomorphism composition and converse remain in the class. |
| **ALG** | **PASS, conditional on RC** | All eight three-letter types agree; finite-join distributivity is valid. Repair the `RRR` zero-case prose. |
| **LH** | **PASS** | Compactness gives finitely many open source charts. |
| **IDEAL / NF** | **PASS, conditional on RC** | Rectangles form a two-sided finite-join ideal; the three word forms are correct, with zero understood separately. |
| **GP / NR** | **PASS** | The two bracketings test pullback nonzeroness versus image/intersection nonzeroness; orientation is correct. |
| **OP** | **PASS** | The projection is globally open and proper, but its restriction to the discrete selector is not pullback-stably surjective. |
| **FIN** | **PASS, conditional on ALG** | The finite case has finitely many clopen sheets; the infinite compact metric case has a graph-probe associator. |
| **C2** | **PASS** | The source is Cantor, the map is proper/surjective/nonopen and its fibers have size 1 or 2. |
| **RANK-NEG** | **PASS** | Stronger assertion (no finite cover even by arbitrary partial-homeomorphism charts) is proved. |
| **SYM / SYM3** | **PASS** | Clopen level sectors isolate the three forward edges; the asymmetric threefold outputs give a genuine ordinary ghost edge. |
| **SEL** | **PASS** | Michael's theorem applies at every residual stage; all required spaces, values, and maps retain the necessary properties. |
| **G-SEL** | **PASS, conditional on ALG** | The point-generated graph is the finite join of the selected charts. |

### 3. The locally closed restriction lemma and graph actions

Let `i_B:B→G` denote the ordinary subspace inclusion and its localic embedding. By definition its image is `[B]`. For an open sector `O⊆G`, the localic pullback of `i_B` and the open embedding `O→G` is the open subspace `B∩O` of `B`. For a closed sector `F⊆G`, it is the closed subspace `B∩F` of `B`. Hence, for `U=O∩F`, forming the pullback successively gives

\[
[B]\wedge U=[B\cap O\cap F]=[B\cap U].
\]

This is an equality **of sublocales**, not an assertion that arbitrary intersections of induced sublocales are represented by set intersection. The corresponding pullback with `G×U` proves the `p` formula. For `q`, use the localic product pullback identity

\[
([A]\times_{\mathrm{Loc}}[B])\wedge(G\times U)
\cong[A]\times_{\mathrm{Loc}}([B]\wedge U).
\]

No spatiality assumption on the full product is needed. Thus **LC and LCR pass**.

Now regard `Γ_h` as the graph of the *localic isomorphism* `h:U_h≅V_h`, with `U_h,V_h` locally closed in `G`. The pullback of a relation `t(A,B)` with this graph is precisely the second-coordinate restriction to `U_h`; its endpoint map is the induced isomorphism `id×h`. Consequently

\[
 t(A,B)\circ\Gamma_h=t(A,h(B\cap U_h)),\qquad
 \Gamma_h\circ t(A,B)=t(h^{-1}(A\cap V_h),B)
\]

for both `t=p` and `t=q`. The fact that `q` may be nonspatial causes no difficulty: its restriction is computed in `Loc` before the isomorphism is applied.

For graph–graph products, put `W=V_h∩U_k`, which is locally closed in `G`. It is locally closed as a subspace of `V_h`, and `h^{-1}(W)` is locally closed in `U_h`. A subset locally closed in a locally closed subspace is locally closed in the ambient space: write each locally closed inclusion as an open restriction followed by a closed inclusion. The range `k(W)` is likewise locally closed in `G`. Thus the composite is an allowed partial homeomorphism and the graph formula **H passes**.

### 4. Full associativity audit: the eight generator patterns

Write `R` for either type of rectangle and `H` for a locally closed partial-homeomorphism graph. The binary multiplication table has the types

\[
 RR\to q\text{ or }0,\quad RH\to R\text{ or }0,\quad
 HR\to R\text{ or }0,\quad HH\to H\text{ or }0.
\]

The important cases are as follows.

* **RRR:** If the two successive overlaps of middle induced sublocales are nonzero, each bracketing produces the same outer `q` rectangle. Otherwise both are zero. **Correction:** even with both overlaps nonzero, the outer `q(A,F)` can itself be zero when `A=∅` or `F=∅`. Therefore the packet's phrase “zero exactly when either ... overlap is zero” is too strong. State the conditional output formula, not an iff zero criterion.
* **RRH / HRR:** The only *interior overlap* test is between the two adjoining rectangles. The graph merely transports/restricts one outer endpoint. If that endpoint becomes empty, the answer is zero on **both** sides. No additional overlap condition is missing.
* **RHR:** This is the decisive compatibility test. Put `b=[B]`, `c=[C]`, `U=U_h`, `V=V_h`. The two nonzero conditions are

  \[
  [h(B\cap U)]\wedge c\ne0
  \quad\text{and}\quad
  b\wedge[h^{-1}(C\cap V)]\ne0.
  \]

  Since the first factor on the left is supported inside `V`, intersecting with `c` may first be restricted to `V`, giving `[C∩V]` by LC. Transport along the isomorphism `h` then turns the left intersection into

  \[
  [B\cap U]\wedge[h^{-1}(C\cap V)],
  \]

  exactly the right-hand intersection after restricting `b` to `U`. Thus the tests are equivalent *as nonzero localic intersections*, not just at the level of ordinary points. Both nonzero bracketings yield `q(A,D)`; otherwise both give zero.
* **RHH / HHR:** Pulling back a support successively through `h` and `k` is the same as pulling it back through the partial composite. The locally closed domain calculation above validates the composite chart.
* **HRH:** Restrictions on independent outer coordinates commute. In either bracketing the answer is

  \[
  t(h^{-1}(A\cap V_h),\,k(B\cap U_k)).
  \]
* **HHH:** Both sides are the graph of the same restricted threefold composite of partial homeomorphisms.

These are all eight cases. The extension from individual letters to finite joins is justified. The lattice of sublocales is distributive, and localic inverse image on sublocales preserves **finite joins**; localic image is left adjoint to inverse image and preserves joins. Thus each side of composition distributes over *finite* joins. One may expand a triple of finite joins into finitely many generator triples. **No infinitary distribution is used.**

The resulting `A_lc(G)` is unital (the full identity is an allowed locally closed graph), closed under converse, and associative, **assuming RC**.

### 5. Ideal and normal-form assertions

Every product containing one rectangle letter is a rectangle or zero, by RC/PH. Hence finite rectangular sums form a two-sided finite-join ideal of `A_lc(G)`; converse preserves it. For a word of individual generators, the number of rectangle letters gives the stated trichotomy:

1. zero rectangles: a single partial-homeomorphism graph (allow the empty graph);
2. one rectangle: a rectangle of the same `p`/`q` type, or zero;
3. two or more rectangles: a full `q` rectangle, or zero.

The second rectangle is where RC forces `q`; subsequent graph words preserve the type and subsequent rectangle words again yield `q` or zero. A zero product cannot later become nonzero. This is valid for every bracketing by ALG. The normal forms **do not** say that an arbitrary *finite join* reduces to one generator; arbitrary elements retain the stated `rectangle-sum ∨ graph-sum` form.

### 6. Graph-probe identity: independent localic derivation

Use the packet's typing `R:{u}→Y`, `F=Γ_f^\smile:Y→S`, `T:S→{v}`, with `R={u}×B` and `T=S×{v}`. For the first bracketing, the exact composability object is `B×_Y S`. Its image under the endpoint map into `{u}×S` is `{u}×f^{-1}(B)`. Composing with `T` projects a nonzero locale onto the singleton, giving

\[
 (R\circ F)\circ T=1_{\{(u,v)\}}
 \quad\Longleftrightarrow\quad f^{-1}(B)\ne0.
\]

For the other bracketing, `F∘T=im(f)×{v}`. Its subsequent pullback with `R` is the intersection `B∧im(f)`, so

\[
 R\circ(F\circ T)=1_{\{(u,v)\}}
 \quad\Longleftrightarrow\quad B\wedge im(f)\ne0.
\]

A nonzero pullback always has a nonzero image sublocale contained in `B∧im(f)`; therefore only the **right-associated nonzero / left-associated zero** defect can occur in this test. Both orientation and strength of GP are correct.

For `T=[E]×{v}`, one needs the specialized criterion `(NR)` involving
`[E]∧f^{-1}([I])` and `[f(E)]∧[I]`. The assertion `im(f|[E])=[f(E)]` is valid: two opens of `Y` become equal on the image exactly when their traces on the ordinary set `f(E)` agree. Equivalently, the induced spatial sublocale is the image of the ordinary inclusion of `f(E)`.

### 7. Adversarial model A: failure outside the locally closed hypothesis

Take Cantor space `Y`, a countable dense `Q⊂Y`, and its dense complement `I`. Neither `Q` nor `I` is locally closed (a dense locally closed subset is open, while a countable dense subset of Cantor space is not open). Let `h=id_Q:Q→Q`, viewed as a partial homeomorphism on a **non-locally-closed** domain. Consider `R={u}×[I]`.

The genuine localic calculation is

\[
 R\circ\Gamma_h
 =\{u\}\times\bigl([I]\wedge[Q]\bigr)
 \ne0,
\]

because both `[I]` and `[Q]` are dense sublocales and their meet contains the nonzero least dense (double-negation) sublocale `Y_{\neg\neg}`. But the *set-theoretic* extension of PH would predict

\[
 \{u\}\times[h(I\cap Q)]=0.
\]

Thus the locally closed restriction assumption is doing actual mathematical work; one cannot silently allow all spatial graph domains. This is also a useful quick stress test of every proof that replaces pullback by ordinary intersection.

### 8. Adversarial model B: open and proper, but nonassociative

Let `Y=2^ℕ`, `K` an infinite compact metric space, and `f:Y×K→Y` the projection. Pick distinct `z_n→z_∞` in `K` and a countable dense set `Q={q_n}` in `Y` with dense complement `I`. Put

\[
 E=\{(q_n,z_n):n\ge1\}.
\]

Because the `z_n` are distinct and isolated *within the selected sequence*, `E` is an ordinary discrete subspace. As a locale, `[E]` is a coproduct of singleton locales, and `f|_E` sends every one of them to a point of `Q`, outside `I`.

For each `e∈E` the pullback of `[I]` to `{e}` is zero: `{f(e)}` is a closed sublocale of Hausdorff `Y`, disjoint from `I`, and LC for closed sectors applies. Pullback to the discrete coproduct is consequently zero:

\[
 [E]\wedge f^{-1}([I])
 \cong\coprod_{e\in E}\left(\{f(e)\}\wedge[I]\right)=0.
\]

In contrast `im(f|[E])=[Q]` and

\[
 [Q]\wedge[I]\ \ge\ Y_{\neg\neg}\ \ne0.
\]

With `R={u}×[I]`, `F=Γ_f^\smile`, and `T=[E]×{v}`, the complete three-factor calculation is

\[
 (R\circ F)\circ T=0,
 \qquad R\circ(F\circ T)=\{(u,v)\}.
\]

This explicitly exhibits the required localic failure for a **globally open proper** map; the failure occurs only after the source has been restricted to `[E]`. Every infinite compact metric `K` contains a sequence as used above. If `K` is finite, its points are clopen and the graph is a finite union of homeomorphic sheets. This proves the sharp FIN assertion, conditional on ALG in the finite direction.

### 9. Adversarial model C: two-to-one Cantor map and infinite rank

The construction of the closed nowhere-dense Cantor supports `K_n` is legitimate: at stage `n`, the finite union of earlier supports is nowhere dense, so `W_n` contains a nonempty clopen cylinder disjoint from it; inside that cylinder one can put a nowhere-dense Cantor copy. The selected `q_n∈K_n∩W_n` are distinct and form a dense countable set `Q`.

Let

\[
 X=(Y\times\{0\})\cup\bigcup_{n\ge1}(K_n\times\{1/n\}).
\]

This is closed in the compact metrizable zero-dimensional `Y×({0}∪{1/n})`: a limit of upper-sheet points either stays at an isolated positive height (and belongs to its closed `K_n`) or falls to height zero, where the full base is present. Each positive-height sheet is a perfect Cantor space, while every base point lies in the perfect height-zero copy of `Y`. Therefore `X` has no isolated points; being nonempty, compact metrizable and zero-dimensional, it is a Cantor space.

The projection `f:X→Y` is continuous, proper and onto. The pairwise disjoint `K_n` ensure each fiber contains the base point and at most one upper point; `f` is not open because the clopen upper sheet `K_n×{1/n}` has nowhere-dense image `K_n`. With

\[
 E=\{(q_n,1/n):n\ge1\},
\]

`E` is discrete (positive height levels are clopen) and maps bijectively to the dense `Q`. **Exactly the full localic calculation in §8** gives a nonassociative graph probe, despite fiber multiplicity at most two.

The chart-rank argument is also sound, including its stronger formulation. If finitely many arbitrary homeomorphic charts `U_i→f(U_i)` covered `X`, the sets `D_i=f(E∩U_i)` would each be discrete *in the subspace topology inherited from `Y`*, since `E∩U_i` is discrete and the chart map is a homeomorphism. A discrete subset `D` of a perfect Hausdorff space has nowhere-dense closure: if some nonempty open `O` lay in `cl(D)`, a point `d∈D∩O` would have a neighborhood `N` with `N∩D={d}`; yet the nonempty open set `(N∩O)\{d}` must meet `D` by density, contradiction. The finite union of the closed nowhere-dense `cl(D_i)` cannot contain the dense `Q`. Thus no finite cover by even unrestricted partial-homeomorphism charts exists, and in particular

\[
 \rho_{lc}(f)=\infty,\qquad  \max_y|f^{-1}(y)|=2.
\]

The proof does **not** rely on an erroneous assertion that discrete sets are closed or on a misplaced Baire-category argument.

### 10. A single symmetric reflexive graph and its ghost edge

Put the four blocks `{u},Y,X,{v}` at clopen levels `0,1,2,3`, and form

\[
 H=\Delta\vee R\vee R^\smile\vee F\vee F^\smile\vee T\vee T^\smile.
\]

Each term is an induced spatial sublocale of its ordinary set of pairs. A finite join of such point-generated sublocales is point-generated by the union of their pairs, so `H` really is one reflexive symmetric point-generated relation.

To arrive from level 0 at level 3 in precisely three factors, every factor must increase level by one. Diagonal loops and backwards edges cannot contribute; by finite-join distributivity and the clopen sector projections, the `(0,3)` component of the two bracketings is **exactly** the corresponding component of `((R∘F)∘T)` and `R∘(F∘T)`. Their values are respectively `0` and the full singleton edge by §§6–9. Hence SYM3 passes.

Ordinary undirected paths cannot connect `u` to `v`, even with additional steps or reverses: the `Y` neighbors of `u` lie in `I`, and the only `X` points adjacent to those have image in `I`; the points of `E` adjacent to `v` all have image in `Q=Y\setminus I`. The bipartite graph between `Y` and `X` is the graph of a function and cannot change the projected `Y` coordinate. This verifies both the “ghost edge” and “no ordinary path” statements.

### 11. Michael selection and the exact positive boundary

I verified that the **zero-dimensional Michael theorem does not require convex values**. It applies to any lower-semicontinuous multifunction with nonempty *closed* values, from a zero-dimensional paracompact domain into a *complete metric* range. Two publicly accessible confirmations are Stasyuk–Tymchatyn, *Topology Proceedings* 39 (2012), p. 41, and Bressan–Colombo, *Studia Mathematica* 102 (1992), p. 1; both explicitly state the nonconvex zero-dimensional version.

Here is a full audit of the induction. Initially `X_1=X` and `Y_1=Y`. Assuming `X_i` is open in compact metric `X`, it is **completely metrizable** with some compatible complete metric, even though its metric inherited from `X` may not be complete. Its image `Y_i=f(X_i)` is open because `f` is open; `Y_i` is metrizable, hence paracompact, and remains zero-dimensional. The restricted map `f_i:X_i→Y_i` is an open surjection. Its inverse-fiber multifunction

\[
 \Phi_i(y)=f_i^{-1}(y)
\]

has nonempty **closed values in `X_i`** because `Y_i` is Hausdorff, and is lower semicontinuous because the inverse-image hit set of each open `O⊆X_i` is exactly the open set `f_i(O)`. Michael therefore gives a continuous section `s_i:Y_i→X_i`.

The image `U_i=s_i(Y_i)` is closed *in `X_i`*, without requiring compactness: it is the equalizer of `id_{X_i}` and `s_i∘f_i` into Hausdorff `X_i`. Hence `U_i` is locally closed in `X`. Its image `f(U_i)=Y_i` is open in the original `Y`. Remove the section. The residual `X_{i+1}=X_i\setminus U_i` is open in `X`; its image under the original open map is open in `Y`, and its restricted map remains open. Thus the same hypotheses recur at every stage. At each stage precisely one point is removed from every nonempty residual fiber. After `N` stages no points remain; since a fiber of size `N` exists, each of the `N` stages is nonempty. The resulting charts are pairwise disjoint.

No chart meets any single fiber twice; hence `N` is also a lower bound on the number of charts. Therefore

\[
 \rho_{lc}(f)=\max_{y\in Y}|f^{-1}(y)|=N,
\]

as submitted. Each chart graph is induced spatial, and the finite union of its pairs is the graph of `f`. Accordingly G-SEL follows **conditionally on ALG**.

**A useful sharpening:** the same section-removal proof works without compactness if `X` is *completely metrizable*, `Y` is *zero-dimensional metrizable*, and `f:X→Y` is an open surjection with a uniform finite fiber bound. The open residual subsets of `X` remain completely metrizable, and the open residual subsets of metric `Y` remain paracompact and zero-dimensional. If the integer bound `N` is attained, its chart rank is exactly `N`. The compact metric form in the packet is therefore a clean special case of a somewhat more general topological theorem. The **localic algebra application**, however, still requires the appropriate compact-Hausdorff ambient setting in which RC was imported.

### 12. Repairs, exposition improvements, and remaining questions

**Required minor repairs.** Replace the `RRR` “zero exactly when” sentence by a formula that allows zero outer endpoint supports. Explicitly prove or cite the finite-join preservation of sublocale pullbacks and localic images in the step from generator triples to sums. Include the one-line argument that locally closed inclusions compose, to make graph–graph closure unambiguous. In the selection proof, emphasize the distinction between **complete metrizability** and completeness of the inherited metric, as the current packet fortunately already does.

**Useful proof simplifications.** The entire positive theory can be organized around two identities: (i) `[B]∧U=[B∩U]` for locally closed `U`, and (ii) the `RHR` overlap-transport equivalence in §4. Once these are presented as lemmas, six of the other generator patterns become formal, and one need not repeatedly reason about localic points. On the negative side, formulate “dense discrete selector” as a standalone obstruction lemma and then treat the open projection and the two-to-one Cantor map as two geometric realizations. The section-removal argument for SEL is also best presented independently of RC.

**Language that should remain conditional.** “Safe graph adjunction” means associativity *in the algebra generated by the stated finite p/q rectangles and admitted chart graphs*, assuming RC. It is not an assertion that image-defined composition of **all** spatial relations is associative. Likewise, `ρ_lc(f)<∞` has been proved sufficient, not necessary, for associativity with this whole rectangular algebra. Finally, the symmetric counterexample is an **imposed graph** on compact Hausdorff components; it is not an intrinsic nontrivial Cameron–Kumar separation graph, which would collapse to the diagonal in the indicated Hausdorff instances.

**Mathematical follow-up.** The most interesting new question remains necessity: does associative adjunction of `Γ_f` and `Γ_f^\smile` to the full rectangular algebra enforce a finite chart condition under reasonable compact metric assumptions, or merely a weaker stable-image/pullback-reflection property? The exact probe (NR) is a good first necessary condition, but its sufficiency is not established. A further tractable direction is chart-rank bounds for finite-to-one *open* maps over positive-dimensional bases; the zero-dimensional selection proof gives the precise location where the argument presently uses dimension zero. Neither question affects this audit's correctness verdict.

### 13. Source and provenance separation

* **Previously reviewed, taken as an explicit hypothesis:** `02_REVIEWED_RECTANGULAR_BASELINE.md`, especially the uniform composition rule (RC). I have not independently certified it here.
* **Existing published theorem, checked externally:** Michael's zero-dimensional continuous-selection theorem, as restated by I. Stasyuk and E. D. Tymchatyn, “A Note on Uniformly Continuous Selections for Multi-Valued Maps,” *Topology Proceedings* **39** (2012), 41–44, <https://topology.nipissingu.ca/tp/reprints/v39/tp39004.pdf>; and A. Bressan and G. Colombo, “Selections and representations of multifunctions in paracompact spaces,” *Studia Mathematica* **102** (1992), <https://matwbn.icm.edu.pl/ksiazki/sm/sm102/sm10232.pdf>.
* **New packet assertions independently audited here:** LC, PH, H, LH, GP, NR, OP, C2, RANK-NEG, SYM, SEL and their topological details. ALG, IDEAL, NF, FIN (finite direction), and G-SEL follow as claimed **provided RC holds**.

**Overall recommendation:** accept this collection as a coherent new extension of the rectangular program after the small `RRR` wording correction and the suggested explicit pullback/finite-join justification. No mathematical retraction of a substantive new result is called for on the evidence of this audit.