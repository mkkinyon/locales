# Project A — graph extension boundary: locally closed partial homeomorphisms versus open proper projections
## Research continuation · 20 November 2026 · INTERNAL deductions, not yet externally audited

**Scope.** This note builds on the independently blind-reviewed compact-Hausdorff **finite rectangular calculus** [canonical note](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and on the internally derived [graph-probe criterion](ProjectA_GRAPH_EXTENSIONS_BICLIQUE_AND_IMAGE_STABILITY_2026-11-20.md). It strengthens the previous [clopen partial-homeomorphism note](ProjectA_CLOPEN_PARTIAL_HOMEOMORPHISM_RECTANGULAR_ALGEBRA_2026-11-20.md) to **locally closed** domains/ranges and constructs an explicit graph of a **globally open, proper, surjective projection** that cannot be safely adjoined to the rectangular algebra. Neither new assertion is in the referee's report; no priority or novelty claim.

All compositions use the actual localic pullback and image, in classical Loc. We distinguish p(A,B)=[A×B] (point-generated spatial rectangle) from q(A,B)=[A]×_Loc[B] (full localic rectangle) for ordinary subsets of a compact Hausdorff space G.

### 1. Restricting induced spatial supports to locally closed subspaces

**Lemma 1.1.** Let U⊂G be a locally closed subspace, regarded as the corresponding locally closed sublocale. For any ordinary B⊆G,
\[
\boxed{[B]_G\wedge U=[B\cap U]_G.}\tag{L}
\]
Likewise, restricting p(A,B) to G×U gives p(A,B∩U), and restricting q(A,B) gives q(A,B∩U).

**Proof.** Write U=O∩F for O⊂G open, F⊂G closed. The pullback of O to the induced **spatial** sublocale [B] is the open spatial subspace B∩O, and its further pullback along F is the closed spatial subspace B∩O∩F. Embedding this pullback into G gives precisely [B∩U]. For p, apply the same argument to the spatial subspace A×B of G², restricting by G×U. For q, use the pullback-stability of the product with [A] to compute ([A]×[B])∧(G×U)=[A]×([B]∧U). This is localic product preservation under restriction and does not assume the full product is spatial.

Both open and closed subspaces are particular locally closed cases; **arbitrary induced spatial sublocales are not**: Q∧I may be nonzero even if Q∩I is empty.

### 2. Graph actions and algebra of partial homeomorphisms

Let h:U_h→V_h be a homeomorphism between locally closed subspaces of G. Let Γ_h≤G² be its graph. This graph is spatial and point-generated (homeomorphic to U_h), but need not be closed/open in G².

**Lemma 2.1.** For ordinary A,B⊆G and t∈{p,q},
\[
\boxed{
t(A,B)\circ\Gamma_h=t(A,h(B\cap U_h)),\qquad
\Gamma_h\circ t(A,B)=t(h^{-1}(A\cap V_h),B).
}\tag{PH}
\]
**Proof.** For the first composite, the composability pullback is the restriction of t(A,B) to the second-coordinate sublocale U_h, and its endpoint map is the isomorphism id×h onto G×V_h, followed by an inclusion. Lemma 1.1 computes the restricted relation, and the isomorphism transports both point-generated and full rectangles. The second formula is dual. This avoids any assertion that the image of a nonisomorphic map is pullback-stable.

If h and k are locally closed partial homeomorphisms, their composite is the partial homeomorphism k∘h on U_h∩h^-1(U_k), again between locally closed subsets of G. The inverse graph is Γ_{h^-1}. Hence such graphs form an inverse semigroup under relational composition.

**Theorem 2.2 (INTERNAL).** Let \(\mathscr A_{\mathrm{lc}}(G)\) consist of finite joins of p(A,B), q(A,B), and Γ_h for **all locally closed partial homeomorphisms h** of G. Then \(\mathscr A_{\mathrm{lc}}(G)\) is an associative, converse-closed, finite-join-distributive algebra under localic relation composition. It contains 0 and the identity Δ_G=Γ_id.

**Proof.** The independently reviewed uniform rectangular rule (RC) handles any rectangle–rectangle product. (PH) handles a rectangle and a graph; composition of partial homeomorphisms handles graph–graph. Thus the generator types are closed under composition.

For associativity, check three-factor generators:
- RRR: (RC) supplies the full outer rectangle if both adjacent middle support overlaps are nonzero, zero otherwise.
- RRH, HRR: the same single middle-overlap test controls both bracketings; coordinate restriction occurs on the outer side and gives identical t/q rectangles (including the zero empty-set cases).
- RHR: one bracketing tests [h(B∩U_h)]∧[C]≠0, the other [B]∧[h^-1(C∩V_h)]≠0. These tests are equivalent: both can be restricted to the locally closed range V_h and pulled back under the isomorphism h; by (L) the induced spatial support restrictions are correct. Both results are q(A,D) when nonzero, zero otherwise.
- RHH/HHR: the composition of partial homeomorphisms has exactly the domain/range restrictions obtained by acting successively on a rectangle, so the two outcomes agree.
- HRH: restrictions of different *outer* coordinates commute, giving identical t(h^-1(A∩V_h),k(B∩U_k)).
- HHH: composition of partial maps is associative.

Here R denotes either p or q, and H denotes a partial graph. By distributivity of composition over **finite** joins, the triple-generator identities yield associativity for the finite-join algebra; converse swaps p(A,B) with p(B,A), q(A,B) with q(B,A), and Γ_h with Γ_{h^-1}. The total identity graph is Δ_G. No infinitary distribution is used.

### 3. Corollary: graphs of compact-Hausdorff local homeomorphisms

Let f:X→Y be a **local homeomorphism** with X,Y compact Hausdorff. For each x∈X choose an open neighborhood U_x on which f restricts to a homeomorphism onto an open subset of Y. Compactness of X provides **finitely many** such neighborhoods U_1,…,U_m covering X. Each graph Γ_{f|U_i} is a graph of an **open partial homeomorphism** between subspaces of G=X⊔Y (a compact Hausdorff disjoint union). As the full graph Γ_f is spatial and point-generated,
\[
\boxed{\Gamma_f=\bigvee_{i=1}^m\Gamma_{f|U_i}.}\tag{LH}
\]
Thus Γ_f and its converse belong to \(\mathscr A_{\mathrm{lc}}(G)\), and can be mixed arbitrarily with finite p/q rectangular joins **without losing associativity**.

This includes finite-sheeted nontrivial coverings of connected compact spaces, for which no nontrivial globally clopen domain trivialization need exist. The reason is finite **open** chart coverage, not global clopen splitting.

### 4. A genuinely open-and-proper map graph that destroys associativity

**Theorem 4.1 (INTERNAL counterexample).** There exist compact metrizable **Stone** spaces X,Y and a continuous **open proper surjection** f:X→Y such that the graph-converse Γ_f^smile, together with two point-generated (singleton-leg) rectangles, forms a nonassociative triple. Thus *global* openness and properness of f do **not** suffice to adjoin its graph to \(\mathscr A_{\rm rect}(X\amalg Y)\).

**Construction.** Let Y=2^ℕ be Cantor space. Choose a countable dense ordinary subset Q={q_n:n≥1} with distinct points and with dense complement I=Y\Q (e.g. eventually-zero sequences). By Isbell density, [Q]∧[I]≠0. Let Z=2^ℕ and choose
\[
z_n=0^n1\,0^\infty\in Z,\quad n\ge1.
\]
The clopen cylinders [0^n1] are pairwise disjoint, and each isolates z_n from all other z_m. Put
\[
X=Y\times Z,\qquad f=\operatorname{pr}_Y:X\to Y,\qquad
E=\{(q_n,z_n):n\ge1\}\subseteq X.
\]
X and Y are compact metrizable Stone spaces; the projection f is **open, proper and surjective**. The ordinary subspace E is **discrete**, since the z_n coordinate cylinders isolate each point. Therefore its induced spatial sublocale [E] is a discrete locale. The restriction f|[E] is the ordinary map n↦q_n.

Since all f(E) points lie in Q and Q∩I=∅, the localic pullback
\[
\boxed{[E]\wedge f^{-1}([I])=0.}\tag{4.2}
\]
Precisely: when pulled back to the discrete locale [E], [I] has zero restriction to each singleton; any sublocale of a discrete locale is spatial/point-determined, hence the entire pullback is zero. By point-generated image preservation,
\[
\boxed{\operatorname{im}(f|[E])=[Q].}\tag{4.3}
\]

Let G={u}⊔Y⊔X⊔{v}, with the displayed four summands clopen; G is still compact metrizable Stone. Define endorelations on G:
\[
R=\{u\}\times[I],\quad F=\Gamma_f^\smile\subseteq Y\times X,\quad T=[E]\times\{v\}.
\]
All three are point-generated; the middle graph is **closed** in G² since X is compact and Y Hausdorff, and both outer factors are complete bipartite singleton-leg rectangles.

First associate left:
\[
R\circ F=\{u\}\times f^{-1}([I]),
\qquad
(R\circ F)\circ T=0
\]
by (4.2) and the rectangular rule. Associate right:
\[
F\circ T=[Q]\times\{v\},\qquad
R\circ(F\circ T)=\{(u,v)\}\ne0
\]
because [I]∧[Q]≠0.

Therefore
\[
\boxed{(R\circ F)\circ T=0\quad\ne\quad R\circ(F\circ T)=\{(u,v)\}.}\tag{OP}
\]

**Interpretation.** Even though f:X→Y is globally **open and proper** (hence its own map-image surjection is pullback-stable), the induced map **on the selected spatial support** f|[E]:[E]→[Q] loses nonzero reflection after pullback along the pointless overlap [I]∧[Q]. Thus failure is a *hereditary image-stability defect*, not global improperness.

The middle relation Γ_f^smile cannot be a finite join of complete bipartite point-generated rectangles: any nonempty ordinary rectangle contained in the graph of f has its Y-coordinate contained in a single value, while f(X)=Y is infinite. The example has no conflict with the positive finite-rectangular algebra or with local-homeomorphism graph extensions: the projection f has infinite Cantor fibers and is not a local homeomorphism.

### 4.1. An exact finite-versus-infinite fiber dichotomy for product projections

**Theorem 4.2 (INTERNAL, complete dichotomy).** Fix Cantor space \(Y=2^{\mathbb N}\) and a **nonempty compact metrizable** space \(K\). Let \(X=Y\times K\), \(f=\mathrm{pr}_Y:X\to Y\), and \(G=\{u\}\amalg Y\amalg X\amalg\{v\}\). Consider the finite-join/composition algebra generated by the **full compact-Hausdorff rectangular algebra** on G together with \(\Gamma_f\) and its converse. Then
\[
\boxed{\text{the resulting algebra is associative }\Longleftrightarrow K\text{ is finite}.}\tag{FIN}
\]

**Proof.** If K is finite, compact Hausdorff forces K discrete. The finitely many sheets Y×{k} are clopen, and each projection restriction Y×{k}→Y is a homeomorphism. Thus Γ_f is a finite join of clopen partial homeomorphism graphs, and Theorem 2.2 supplies associativity of the containing algebra.

If K is infinite compact metric, choose a sequence (z_n) of **distinct** points converging to an accumulation point z_∞ with z_∞ not among the z_n. Such a sequence exists by compact metric sequential compactness; its point set {z_n} is discrete as a *subspace* of K, since each fixed z_n is separated from the limit and all but finitely many other z_m. Choose a countable dense Q={q_n} in Cantor space with dense complement I. Put E={(q_n,z_n):n≥1}⊆Y×K. The projection E→Y is a bijective enumeration of Q, and E is discrete as a subspace of X because the second-coordinate sequence is discrete.

The pullback of [I] along [E]→Y is zero because every singleton source point maps to q_n∉I and **all sublocales of a discrete locale are point-determined**. Meanwhile the localic image of [E] in Y is [Q], with [Q]∧[I]≠0. Thus the same three relations
\(
\{u\}\times[I],\ \Gamma_f^\smile,\ [E]\times\{v\}
\)
have distinct bracketings exactly as in Theorem 4.1. The generated algebra is not associative.

The metric assumption on K is used only to extract a **countably infinite discrete subspace**; the negative proof extends verbatim to any compact Hausdorff K containing such a subset. The sufficiency for finite K needs no metrizability. □

**Significance.** This is a controlled threshold for maps whose global properties are uniformly excellent: every projection f in the family is **open, proper and surjective**, regardless of K. The issue is precisely the ability to select arbitrarily many different witness points in an infinite fiber direction, making the selected source support discrete while its image remains dense.

### 4.3. A single reflexive symmetric ordinary graph with a ghost edge across distinct components

The preceding counterexample is not merely about three heterogeneous, asymmetric relations. On the same compact metric Stone ambient space \(G=\{u\}\amalg Y\amalg X\amalg\{v\}\), put
\[
\boxed{H=\Delta_G\vee R\vee R^\smile\vee F\vee F^\smile\vee T\vee T^\smile.}\tag{SYM}
\]
This is a **point-generated reflexive symmetric** localic relation, and its ordinary adjacency graph is a genuine undirected graph with loops.

Assign clopen levels 0,1,2,3 to {u},Y,X,{v}. Every non-diagonal edge of H changes level by exactly 1, and only edges joining consecutive levels occur. Consequently any **three-factor** composite from level 0 to level 3 must traverse the unique forward level sequence 0→1→2→3. Finite distributivity and clopen restriction therefore give exact identities
\[
\begin{aligned}
((H\circ H)\circ H)\wedge(\{u\}\times\{v\})
 &=((R\circ F)\circ T)=0,\\
(H\circ(H\circ H))\wedge(\{u\}\times\{v\})
 &=R\circ(F\circ T)=\{(u,v)\}.
\end{aligned}\tag{SYM3}
\]
Thus **a single reflexive symmetric point-generated relation on a compact metrizable Stone locale fails threefold power-associativity**, even though its only nonlinear graph constituent is the converse of a **globally open proper projection**.

The ordinary graph has **no path of any finite length** from u to v. Indeed each x∈X is joined only to its projection f(x)∈Y, the vertex u joins precisely the Y-vertices in I, and the vertex v joins precisely the selected x∈E, all projecting into Q. Any ordinary path from u remains in the I-labeled side; any path from v remains in the Q-labeled side. Yet the right-associated localic third power contains the ordinary pair (u,v), arising entirely from the pointless nonzero overlap [I]∧[Q] **after** the F∘T image collapse.

This is a sharp graph-theoretic contrast with the positive clique and finite-rectangular theorems: the ordinary connected-component partition itself is not preserved by arbitrary *parenthesized localic powers*. The equality (SYM3) is a new **internal** deduction from Theorem 4.1 and the clopen level support, not a separately audited external theorem.

### 5. Exact necessary probe condition for adding a graph

For any continuous f:X→Y between compact Hausdorff spaces, and any ordinary subsets E⊆X, A⊆Y, the same singleton-marker test gives
\[
\bigl(\{u\}\times[A]\bigr)\circ\Gamma_f^\smile\circ
\bigl([E]\times\{v\}\bigr)
\]
with parentheses carefully retained. The left-associated triple is nonzero iff
\(
[E]\wedge f^{-1}([A])\ne0,
\)
whereas the right-associated triple is nonzero iff
\(
[f(E)]\wedge[A]\ne0.
\)
A necessary condition for Γ_f^\smile to adjoin associatively to the **entire** finite rectangular algebra is therefore
\[
\boxed{
[E]\wedge f^{-1}([A])\ne0
\quad\Longleftrightarrow\quad
[f(E)]\wedge[A]\ne0
\quad\text{for all ordinary }E,A.
}\tag{NR}
\]
Only the implication from left to right is automatic. The reverse fails in Theorem 4.1, despite f being open and proper. Condition (NR) is a **necessary diagnostic**, not claimed sufficient; other mixed triple tests may still fail even when every singleton marker probe agrees.

### 6. Big picture and recommended next test

The new contrast is:

| Map graph | Positive / negative evidence |
|---|---|
| Homeomorphism | Positive, invertible coordinate change |
| Locally closed partial homeomorphism | Positive, exact induced-support restriction (L) |
| Compact-Hausdorff local homeomorphism | Positive, **finite open chart** graph decomposition |
| Open proper projection with infinite compact fibers | **Negative**, via discrete support E |
| General finite-to-one proper/open map with branch points | Unknown; not implied by either result |

The **number of local invertible pieces** and stability under restriction to arbitrary induced spatial supports now appear more informative than global open/proper properties alone. The next bounded test is a **finite-to-one continuous map that is not a local homeomorphism**, such as a branched covering, asking whether it has a finite **locally closed piecewise-homeomorphism** presentation (positive) or admits the nonzero-reflection probe (NR) (negative). The graph algebra is not claimed to encompass arbitrary infinite decompositions of graphs.

### 7. Research origin / qualification

This revisits the Cameron–Kumar graph motivation from the localic side: an ordinary graph records paths, but a localic composite can acquire a new **ordinary pair** by an intermediate *pointless* overlap after an image collapse. The positive graph algebras are those for which witness presentations can be composed stably using finitely many rectangles and invertible locally closed graph charts. The directed overlap calculus remains the corresponding finite witness combinatorics. None of the new results here asserts that the imposed Stone graph relations are canonical Urysohn or inseparability graphs of these Stone spaces; their intrinsic compact-Hausdorff separation graphs are equality.

**Audit status:** Internal proof only. Previous referee results are imported with attribution. The locally closed partial-homeomorphism extension and the globally-open-proper projection counterexample should be included in the next independent adversarial audit cycle, not presented as externally certified.
