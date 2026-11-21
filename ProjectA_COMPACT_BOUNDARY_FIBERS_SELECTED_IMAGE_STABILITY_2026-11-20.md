> **21 NOV 2026 — SCATTERED TARGET / HSIS INTERNAL AUDIT COMPLETED; BLIND EXTERNAL PACKET READY.** [Pre-referee consolidation](ProjectA_SCATTERED_HSIS_PRE_EXTERNAL_CONSOLIDATION_2026-11-21.md) · [internal adversarial audit](ProjectA_SCATTERED_TARGET_HSIS_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) · [blind referee archive](project-a/audits/2026-11-21/SCATTERED_HSIS_BLIND/README.md). The **scattered sober point-cover theorem** and Hausdorff converse pass internal review; the **compact-Hausdorff universal graph-safety iff scattered** dichotomy is *conditional on the new HSIS graph-extension sufficient criterion*, which the referee is asked to check independently at full p/q rectangle level. The blind ZIP has six stand-alone Markdown files, with **no internal verdict**. Level 2⇒Level 3 and global necessity of HSIS are still **OPEN**. Pending the external report/addendum and post-external repairs, **defer the planned big-picture research synthesis**. The earlier compact-Hausdorff rectangular algebra retains its distinct positive external referee status.

> **21 NOV 2026 — SCATTERED TARGETS: UNIVERSAL POINT-COVER STABILITY AND A GRAPH-ALGEBRA DICHOTOMY (NEW INTERNAL THEOREMS).** The [Cantor–Bendixson proof and graph-extension note](ProjectA_SCATTERED_TARGET_UNIVERSAL_POINT_COVERS_AND_GRAPH_ALGEBRA_2026-11-21.md) proves that for any **scattered sober** space Y, its canonical discrete point cover is **pullback-stably surjective**—indeed *every pointwise-surjective locale map* to Y is stable, including after pointless base changes. Conversely for **Hausdorff** Y, stability of the canonical point cover characterizes scatteredness, via a nonzero pointless Booleanization of a perfect closed subspace. Hence every selected spatial image into a scattered Hausdorff target is automatically HSIS. Combining this with the earlier INTERNAL graph-extension criterion gives a classification: a compact Hausdorff target Y is **universally safe for adjoining graphs of all compact-Hausdorff surjections to the finite rectangular algebra iff Y is scattered**; the negative direction uses a globally **open/proper** projection with a discrete selected support over two disjoint dense subsets of a perfect compact closed kernel (Hewitt resolvability; Cantor-space elementary version for metric Y). Also proved: every pointwise-surjective selected map is stable under all **spatial** base changes, and full stable surjectivity equals **inclusion stability after all Cartesian product amplifications**. These claims are internal/unrefereed and the positive graph-algebra half depends on our earlier unrefereed sufficiency criterion. The original Level-2 versus Level-3 question for non-scattered targets remains open.

> **21 NOV 2026 — NECESSITY FOLLOW-UP (NEW INTERNAL WORK):** The [two-colour/Boolean support-probe note](ProjectA_HSIS_NECESSITY_TWO_COLOR_BOOLEAN_PROBES_2026-11-21.md) translates the necessary graph-probe condition (NR) into ordinary two-colour compact closed-support lifting. It proves a strict gap **for one fixed selected subset E**: in β(Y_disc)→Cantor Y with E=Y_disc, every ordinary selected-support probe passes but the pullback along pointless Booleanization ᵍ(Y) is zero. Taking a *smaller* selected subset Q restores an ordinary probe failure, so the **global** necessity of HSIS remains open. A general fittedness lemma expresses every sublocale V≤compact Hausdorff Y as a join of Booleanizations of nonempty closed supports; these yield a complete test for stability under all **sublocale inclusion** base changes. The jump from inclusion-base-change stability to arbitrary-base-change stability is not established. These are not part of the earlier independent referee report.

> **POST-PROOF SIMPLIFICATION (20 NOV 2026, INTERNAL):** Condition (S1) below is actually **automatic for every continuous compact-Hausdorff map**, by the closed-graph/spatial-multiplier Lemma 1.3 added below. Therefore the substantive sufficient hypothesis in Theorem 1.1 is **(S2) alone**: hereditary pullback-stability of every selected spatial image [E]→[f(E)]. The older two-condition phrasing is retained as the proof dependency map, with (S1) now proved rather than separately assumed. This refinement is internal and not yet independently audited.

# Project A — compact boundary fibers: stable graph algebra versus boundary ghost edges
## Research continuation · 20 November 2026
**Status:** NEW INTERNAL proof and examples; NOT independently adversarially or blind-audited. Builds on the independently reviewed [compact-Hausdorff rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and the previous [stratified unbounded-degree map note](ProjectA_UNBOUNDED_FINITE_DEGREE_PROJECTION_ASSOCIATIVE_GRAPH_ALGEBRA_2026-11-20.md). The abstract criterion and both new boundary examples are post-referee mathematics, not in the independent reports. Classical Loc throughout. Literature priority not checked.

## 1. Abstract sufficient criterion for a map graph

Let f:X→Y be a continuous **surjection of compact Hausdorff spaces**. For ordinary point sets A⊆X, B⊆Y put [A],[B] for induced spatial sublocales. Work with the localic endorelations on G=X⊔Y, and let p(A,B)=[A×B] and q(A,B)=[A]×_Loc[B] denote the point-generated and full typed rectangles. Let
\[
g=\Gamma_f\subseteq X\times Y,\quad g^\smile\subseteq Y\times X,\quad K_f=X\times_YX\subseteq X\times X.
\]
The last is a **closed spatial** relation because f is continuous and Y Hausdorff.

Assume the following two conditions hold for every ordinary E⊆X and B⊆Y:

**(S1) Exact inverse image of point-generated supports**
\[
\boxed{f^{-1}([B])=[f^{-1}(B)].}\tag{S1}
\]

**(S2) Hereditary pullback-stable selected image**
\[
\boxed{e_E:[E]\to[f(E)]\quad\text{is a pullback-stable locale-surjection.}}\tag{S2}
\]
The target is the *point-generated localic image*, not the topological closure of f(E). These are sufficient **extra hypotheses**, not asserted automatic for all continuous proper or open f.

**Theorem 1.1 (internal sufficient criterion).** Under (S1) and (S2), the finite-join/composition algebra generated on G by **all p/q typed rectangles**, g, g^\smile, and the diagonal \(\Delta_G\) is associative, converse-closed, finite-join-distributive, and unital. It is exactly the family of finite joins of such rectangles and the finite typed pure-graph system
\[
0,\Delta_X,\Delta_Y,g,g^\smile,K_f.
\]

### 1.1. A useful automatic spatial path lemma

**Lemma 1.2.** For any continuous compact-Hausdorff f, *without* (S1),(S2), the point-generated rectangle actions are
\[
\begin{aligned}
p(A,E)\circ g &=p(A,f(E)),\\
p(A,B)\circ g^\smile&=p(A,f^{-1}(B)),\\
p(A,E)\circ K_f&=p(A,f^{-1}(f(E))),
\end{aligned}\tag{P}
\]
with symmetric left-endpoint counterparts.

**Proof.** For the image-forming side of the functional graph, the actual composability locale is p(A,E), spatial and generated by its ordinary pairs; taking its localic image under id×f preserves the arbitrary join of those point sublocales. For the inverse-image side g^\smile or the kernel pair K_f, the path locale is a **closed sublocale** of the product of the *spatial* rectangle p(A,B) or p(A,E) with the compact Hausdorff space X. Such a localic product is spatial because one factor is locally compact Hausdorff (standard spatial-product multiplier theorem, e.g. Johnstone, *Sketches of an Elephant*, C4.1.8). Its closed sublocale is spatial. Its ordinary points are precisely the composable triples, so the localic image is generated by their endpoints, yielding the displayed p-rectangle. This proof does not rely on the image factor being pullback-stable. Converse gives the other orientation.

**Why this matters:** In the preceding singleton-boundary proof, the kernel-pair p-action was shown by blockwise restrictions. The closed-spatial-path argument is **more general** and eliminates that delicate image-restriction argument entirely. It must not be confused with the false assertion that arbitrary products of spatial locales are spatial: **X is compact Hausdorff** here.

### 1.1.1. Exact induced inverse images are automatic for compact-Hausdorff maps

**Lemma 1.3 (NEW INTERNAL SIMPLIFICATION).** If f:X→Y is **any continuous map between compact Hausdorff spaces** and B⊆Y is any ordinary subset, then
\[
\boxed{f^{-1}([B]_Y)=[f^{-1}(B)]_X.}\tag{AUTO}
\]

**Proof.** Regard the converse graph \(\Gamma_f^\smile\subseteq Y\times X\) as a **closed** sublocale; closedness uses Hausdorffness of Y. The genuine localic pullback \([B]\times_Y X\), whose embedding into X is \(f^{-1}([B])\), identifies with the inverse image of this closed graph in the product \([B]\times_{\rm Loc}X\).

The product \([B]\times_{\rm Loc}X\) is **spatial**: [B] is spatial, and X is compact Hausdorff, hence locally compact; the standard localic-product theorem (Johnstone, *Sketches of an Elephant*, C4.1.8) gives spatiality when one spatial factor is locally compact. A closed sublocale of this spatial product is itself spatial. Its ordinary points are exactly those pairs (b,x) with b∈B and f(x)=b. Via its embedding into X, this spatial locale is therefore the **point-generated** sublocale of the ordinary set f^-1(B), as claimed. □

In fact the same proof works for X **locally compact Hausdorff** and Y Hausdorff, without assuming X compact. The earlier proof of (S1) by separate finite-sheet and boundary restrictions was valid for the constructed example, but unnecessary in the general compact-Hausdorff class.

**Corollary 1.4 (one-condition form of Theorem 1.1).** For a continuous **surjection** f of compact Hausdorff spaces, the assumption that every
\(
e_E:[E]\to[f(E)]
\)
is a pullback-stable locale-surjection, for every ordinary E⊆X, is **sufficient** to adjoin \(\Gamma_f,\Gamma_f^\smile\) associatively to the entire finite point-generated/full rectangular algebra. There is no separate (S1) hypothesis. The proof is Theorem 1.1, using Lemma 1.3 for its (S1) input.

**Important:** Lemma 1.3 does *not* imply that inverse images of arbitrary **nonspatial** sublocales are spatial. Nor does it say that the **selected image** e_E is pullback-stable; that remains the substantive hypothesis and fails in the infinite-compact-fiber projection and spike counterexamples.

### 1.2. Actions on full localic rectangles

For q(A,E), (S2) says e_E remains surjective after product with an arbitrary locale, so composing with g on the image-forming side gives q(A,f(E)). For inverse-image compositions with g^\smile, the localic pullback gives q(A,f^{-1}([B])), which is q(A,f^{-1}(B)) by (S1). The q-action of the kernel pair factors through the pulled-back selected surjection e_E, hence
\[
q(A,E)\circ K_f=q(A,f^{-1}(f(E))).
\]
Together with Lemma 1.2, all six actions in (P) hold for t∈{p,q}, and likewise on the first coordinate.

The pure graphs multiply by
\[
g\circ g^\smile=K_f,\quad
g^\smile\circ g=\Delta_Y,\quad
K_f^2=K_f,\quad K_f\circ g=g,\quad
g^\smile\circ K_f=g^\smile,
\tag{G}
\]
with typed identities and zero incompatible products. The two first formulas use graph pullbacks; f-surjectivity supplies the full diagonal in the second. The other formulas follow by diagonal sections and the equivalence f(x)=f(x'). This finite graph system is associative.

### 1.3. Overlap reciprocity and full associativity proof

Stable surjectivity in (S2) implies, for E⊆X and **every** sublocale D≤Y,
\[
[f(E)]\wedge D\ne0\quad\Longleftrightarrow\quad
[E]\wedge f^{-1}(D)\ne0.\tag{NR}
\]
The reverse-to-right implication uses a base change of e_E along a nonzero sublocale of [f(E)]; the other follows by taking images. By (S1), the right side becomes [E]∧[f^{-1}(B)] for D=[B]. The same symmetry applies to g^\smile. For K_f, applying the equivalence twice gives
\[
[\operatorname{Sat}(E)]\wedge[B]\ne0
\iff
[f(E)]\wedge[f(B)]\ne0
\iff
[E]\wedge[\operatorname{Sat}(B)]\ne0.
\]
Thus every pure graph relation L has **overlap reciprocity**
\[
\boxed{[L_\#E]\wedge[B]\ne0
\iff[E]\wedge[L^{-1}_\#B]\ne0.}\tag{REC}
\]

The new algebra is composition-closed because the independently refereed full-rectangle composition (RC) handles R∘R, Lemma 1.2 and (S1),(S2) handle R∘L and L∘R, and (G) handles L∘L. Products of generator types remain of these types. Associativity reduces, by **finite distributivity**, to checking three-generator words, where R denotes either p or q rectangle and L one of the five nonzero pure graphs:

* RRR: (RC), already independently reviewed.
* RRL and LRR: the same one middle overlap test and the same outside graph action.
* RLR: two adjacent overlap tests are (REC), hence equivalent, giving the same full outer q rectangle when nonzero.
* RLL and LLR: ordinary image/preimage/saturation operators respect the finite pure-graph multiplication table (G); their typed action laws agree.
* LRL: left and right graph factors act on different outer coordinates of the middle rectangle and hence commute.
* LLL: (G), directly.

This covers both p/q types, typed zeros, and arbitrary finite joins. Converse swaps p(A,B)↔p(B,A), q(A,B)↔q(B,A), g↔g^\smile, and fixes K_f; diagonal is the two-sided identity. This proves Theorem 1.1, **conditional only on the explicitly assumed (S1),(S2)**.

## 2. Constructing a nontrivial infinite boundary fiber with all properties

Let
\[
Y=\left(\coprod_{n\ge1}C_n\right)^*
\]
be the one-point compactification of countably many disjoint Cantor blocks; write ∞ for its closed boundary point. Let K be **Cantor space**, metrized by a compatible metric d. Choose finite nonempty sets F_n⊂K that form ε_n-nets with ε_n→0 and |F_n|→∞. Inside K×Y define
\[
\boxed{
X=(K\times\{\infty\})\ \cup\
\bigcup_{n\ge1}(F_n\times C_n).
}\tag{X}
\]
The second-coordinate projection f:X→Y is well defined. X is **closed** in K×Y: its complement is the open union \(\bigcup_n((K\setminus F_n)\times C_n)\). Hence X and Y are compact metrizable Stone spaces. Over C_n, f is a finite disjoint union of homeomorphic sheets F_n×C_n→C_n. Over ∞, its fiber is the entire infinite compact Cantor space K.

**Lemma 2.1.** The projection f is continuous, **open, proper and surjective**.

**Proof.** Continuity, properness and surjectivity are immediate. At a point in a finite clopen sheet the restriction is a local homeomorphism, hence open. For a point (k,∞) of the boundary, any product-basic relative neighborhood contains \((U\times V)\cap X\) with k∈U open in K and V a neighborhood of ∞ in Y. Every sufficiently large finite ε_n-net F_n meets U, so the image of this neighborhood contains ∞ and all C_n for sufficiently large n; that is an open neighborhood of ∞ in Y. Thus f is open.

**Lemma 2.2.** The map f satisfies (S1) and (S2) for **all** ordinary selected subsets.

**Proof of (S1).** The closed boundary in X is \(K\times\{\infty\}\), with open complement \(\coprod_n(F_n\times C_n)\). On each sheet f is an isomorphism onto C_n, so f^{-1}([B])=[f^{-1}B] there. On the closed boundary, the inverse image of [B] is the entire compact fiber K if ∞∈B and zero otherwise. This equals the restriction of [f^{-1}B] by the standard closed-sublocale restriction of induced spatial subspaces. The complementary open/closed pieces detect equality of sublocales, giving (S1).

**Proof of (S2).** Let E⊆X, D=f(E). On any clopen base C_n, selected E is the finite disjoint union of E's subsets of the finitely many sheets; each maps homeomorphically to an induced spatial sublocale of [D∩C_n], and these finitely many target sublocales have join [D∩C_n]. Hence the induced selected image map is **pullback-stably surjective** over C_n, by the finite-sublocale-cover principle. These base changes glue over the disjoint open union Y°.

Over the complementary closed boundary {∞}, E restricts to E∩(K×{∞}). If E has no boundary points then D excludes ∞ and the relative selected target boundary is zero. Otherwise the restriction is the nonzero induced spatial locale [E∩K]→{∞}, which is an **open surjection in classical Loc** (every nonzero locale is overt classically). It is pullback-stable under every base change. The target is covered by its open part and complementary closed boundary, which jointly detect surjectivity after every base change. Thus e_E:[E]→[D] is pullback-stably surjective.

Apply Theorem 1.1:

**Theorem 2.3 (INTERNAL POSITIVE BOUNDARY-FIBER EXAMPLE).** Adjoining Γ_f and Γ_f^\smile to the full compact-Hausdorff finite rectangular calculus on X⊔Y gives an **associative** finite-join relation algebra, even though the proper, open, surjective map f has (i) finite but unbounded fibers over the open Cantor blocks, and (ii) a **whole infinite compact Cantor fiber over its closed boundary point**.

This shows that even a nontrivial **infinite compact boundary fiber** need not destroy associativity. Its safety is explained by (S1),(S2), not by finite inverse-branch cover number. The abstract p-action in Lemma 1.2 avoids any assumption that the kernel pair's boundary restriction is only a singleton.

## 3. Negative companion: make the target boundary itself Cantor

Let B and K be copies of Cantor space, and let S={∞}∪{n:n≥1} be the convergent-sequence compact Stone space. Fix finite ε_n-nets F_n⊂K tending uniformly dense. Put
\[
Y_-=B\times S,\qquad
X_-=(B\times K\times\{\infty\})\cup
\bigcup_{n\ge1}(B\times F_n\times\{n\})\subseteq B\times K\times S,
\]
and let f_-:X_-→Y_- be the projection onto B×S.

The same compactness and net argument shows f_- is **continuous, open, proper, surjective**. Its fibers over each B×{n} are finite, of size |F_n|; over the closed boundary B×{∞} the fiber is K, with boundary restriction
\(
B\times K\to B
\)
the usual Cantor projection.

Choose Q={q_n:n≥1}⊂B dense with dense complement I=B\Q, and choose distinct points k_n∈K forming a **discrete sequence** (e.g. k_n=0^n1\,0^\infty). Let
\[
E=\{(q_n,k_n,\infty):n\ge1\}\subseteq X_-,\quad
A=I\times\{\infty\}\subseteq Y_-.
\]
The selected subspace E is discrete, even though it lies in the closed boundary, because the k_n are isolated from the other sequence points. Its ordinary image f_-(E)=Q×{∞}. By point-generated image preservation and localic Isbell density in the closed Cantor boundary,
\[
\boxed{f_{-*}[E]=[Q\times\{\infty\}],\qquad
[A]\wedge[f_-(E)]\ne0.}\tag{NEG1}
\]

Meanwhile, every selected point maps into Q×{∞}, disjoint from A. Each singleton point of E has zero pullback of [A]. Since [E] is a **discrete locale** (coproduct of its singleton points), the entire localic pullback is zero:
\[
\boxed{[E]\wedge f_-^{-1}([A])=0.}\tag{NEG2}
\]

On G_-={u}⊔Y_-⊔X_-⊔{v}, define
\[
R=\{u\}\times[A],\quad
F=\Gamma_{f_-}^\smile,\quad
T=[E]\times\{v\}.
\]
The graph-probe calculation then gives
\[
\boxed{(R\circ F)\circ T=0\quad\ne\quad R\circ(F\circ T)=\{(u,v)\}.}\tag{NEG3}
\]

**Theorem 3.1 (INTERNAL NEGATIVE BOUNDARY-BASE EXAMPLE).** A globally **open, proper** compact metrizable Stone projection whose open part consists of finite-sheeted blocks may become graph-nonassociative when its **closed target boundary has a nontrivial Cantor base** supporting pointlessly overlapping induced spatial subsets. Here the boundary restriction is Cantor×Cantor→Cantor, and all ordinary finite sheets outside are harmless. In contrast, Theorem 2.3 has the *same sort* of infinite compact domain fiber but a **single closed target point**, and is associative.

### 3.1. Consequence and qualification for ordinary undirected graphs

For either of the projection maps f (the positive f or the negative f_-), set G=X⊔Y and consider the **small** reflexive symmetric ordinary graph relation
\[
H_f=\Delta_G\vee\Gamma_f\vee\Gamma_f^\smile.
\]
Because f is a continuous map between compact Hausdorff spaces, this H_f is itself a **closed** relation on compact G. The general compact-closed relational calculus already gives associativity of its powers, **without** (S1),(S2)! Furthermore, since f is surjective, its twofold power equals the kernel pair of the natural retraction \(r:G\to Y\) (r|X=f, r|Y=id), and all longer powers agree with that kernel pair.

Therefore the negative boundary map f_- becomes nonassociative **only after adding the nonclosed selected-support rectangles** R and T. Do not mistake failure of the **enlarged algebra** for failure of the closed undirected graph H_f itself. To produce a *single non-power-associative reflexive symmetric graph* in the negative case, symmetrize the union \(\Delta_G\vee R\vee F\vee T\) with converses as in the prior four-level examples; the unique three-step route along the distinct clopen levels preserves the graph-probe discrepancy. This distinction is important for the original Cameron–Kumar graph motivation.

## 4. Open–closed gluing for selected-image stability

The positive/negative pair above admits an exact abstract local-to-global statement that removes the special role of a singleton target boundary.

For a continuous map h:Z→W of sober spatial locales, say **HSIS(h)** holds if for every ordinary point subset E⊆Z, the induced point-generated image map
\(
[E]_Z\to[h(E)]_W
\)
is a **pullback-stable locale-surjection**. This is a working abbreviation (hereditary selected-image stability), not established external nomenclature. The target is the induced spatial sublocale on h(E), not its topological closure.

**Lemma 4.1 (open–closed gluing; new internal deduction).** Let f:X→Y be a continuous map of Hausdorff spaces, U⊂Y open, and F=Y\U closed. Put X_U=f^-1(U), X_F=f^-1(F). Then
\[
\boxed{\mathrm{HSIS}(f)\iff \mathrm{HSIS}(f|_{X_U}:X_U\to U)\quad\text{and}\quad
\mathrm{HSIS}(f|_{X_F}:X_F\to F).}\tag{GL}
\]

**Proof.** Let E⊆X and D=f(E). The induced target [D] restricts along the complementary open and closed sublocales U,F to \([D\cap U]\) and \([D\cap F]\). The induced source [E] restricts along X_U,X_F to \([E\cap X_U]\) and \([E\cap X_F]\). These exact identities use restriction of point-generated spatial sublocales along **open and closed** subspaces, not false intersection rules for arbitrary point-generated subsets.

Given an arbitrary base change T→[D] of e_E:[E]→[D], its target T has a complementary open–closed cover T_U∨T_F=T. The pulled-back image map restricted over T_U is a base change of the selected-image map for E∩X_U under f|X_U; similarly for T_F. If the two stratum maps are HSIS, both restricted pullbacks are surjective. Their image jointly contains T_U∨T_F=T, proving e_E stably surjective.

Conversely, if f is HSIS, take an arbitrary E⊆X_U (respectively X_F). Then its image D lies in U (respectively F), and the induced map of its point-generated locale is the corresponding selected-image map for the restricted f, as a map over the subspace. Thus HSIS descends to both strata. □

**Lemma 4.2 (disjoint-open gluing).** If U is an ordinary topological coproduct of open-and-closed pieces U_i and each f|f^-1(U_i) is HSIS, then f over U is HSIS, regardless of the cardinality of the index set. This follows because induced spatial sublocales and base changes split along arbitrary disjoint open coproduct decompositions; no infinitary distribution of **relation composition** is invoked.

**Corollary 4.3 (stratified safe graph maps).** Suppose f:X→Y is a continuous **compact-Hausdorff surjection** and Y=U∪F is an open/closed complementary decomposition. Suppose:
1. \(U=\coprod_{i\in I}U_i\), each U_i open clopen in U, and f^-1(U_i) is a finite disjoint union of subspaces each homeomorphic to U_i under f (finite number allowed to depend on i);
2. the boundary restriction \(h:f^{-1}(F)\to F\) is HSIS.
Then **f is HSIS**, and by Corollary 1.4 adjoining \(\Gamma_f,\Gamma_f^\smile\) to the compact-Hausdorff finite rectangular algebra is associative.

**Proof.** For any E over one U_i the selected image map is a finite cover by the induced spatial images of the selected sheets, hence pullback-stably surjective by preservation of finite sublocale joins. Lemma 4.2 gives HSIS over U, and hypothesis (2) gives it over F. Lemma 4.1 glues the two and Corollary 1.4 supplies the algebra.

**Interpretation.** A **nontrivial Cantor target boundary is not itself unsafe**: its boundary map could be a homeomorphism or a finite covering (both HSIS), in which case gluing is positive. The negative example in §3 fails because the boundary Cantor projection admits a selected dense-discrete support with an image overlap invisible to the actual pullback. Therefore the correct local-to-global invariant is HSIS of the **map on the closed boundary**, not topological dimension/cardinality of the boundary.

**Specific future test:** Prove necessity, or find a counterexample to necessity, of HSIS for associativity of the entire compact-Hausdorff finite rectangular algebra enlarged by a graph. The graph-probe nonzero-reflection condition is necessary, but full pullback-stable surjectivity might be stronger than the generated algebra can detect.

## 5. Conceptual synthesis and audit agenda

The key distinction is **not** boundary-fiber cardinality: both examples have an infinite compact Cantor fiber and arbitrarily large finite-sheet blocks. Rather, it is whether the selected witness map admits an *unstable spatial image* on the closed target boundary. A singleton target boundary forces every nonzero selected boundary support to surject openly to that singleton, whereas a Cantor target boundary supports the classic pointless dense-meet Q∧I despite ordinary disjointness.

The reusable positive criterion is the conjunction:
- exact pullback of each induced spatial target support (S1);
- pullback-stability of every **selected** spatial image map (S2).

These supply exact p/q rectangle actions, reciprocity of localic overlap tests, and associativity of the enlarged finite algebra. Neither mere global openness/properness nor the number of inverse-branch pieces is a substitute.

**Connections to Project A's original graph motivation.** As before, these are **imposed** ordinary adjacency relations on compact Hausdorff/Stone spaces, not nontrivial intrinsic inseparability or Urysohn adjacency in those spaces. The symmetric relation \(\Delta_G\vee\Gamma_f\vee\Gamma_f^\smile\) is an ordinary bipartite graph of fibers. Its localic powers behave normally in the positive example and may acquire ghost edges under the negative selected-support probes. This localic witness-stability perspective supplies an algebraic analogue of tracking finite graph paths while accounting for pointless overlap.

**Audit targets:** (i) exact p-action lemma via closed spatial pullbacks for any compact-Hausdorff map; (ii) base-change stability of the selected-image map over the open–closed decomposition; (iii) (S1) at an infinite compact boundary fiber; (iv) all mixed three-generator cases for the abstract sufficiency criterion; (v) the discrete-support negative Cantor boundary construction.

**Next bounded study:** replace the collapsed boundary map K→{∞} by a map h:K→B whose selected spatial images are stable but whose induced inverse-image supports may fail to be spatial; or formulate a gluing/descent criterion for a finite open–closed stratification with safe maps on each stratum. Also test whether (S2) is close to necessary for the generated algebra by constructing a nontrivial graph-probe using a closed target support from its failure.

No external audit of these new results has yet occurred. The [previous singleton-boundary theorem](ProjectA_UNBOUNDED_FINITE_DEGREE_PROJECTION_ASSOCIATIVE_GRAPH_ALGEBRA_2026-11-20.md) remains a special case.
