# Project A — adding clopen partial homeomorphism graphs to the rectangular algebra
## New internal positive extension · 20 November 2026

**Status:** INTERNAL theorem/proof, not independently audited. This extends the independently reviewed [compact-Hausdorff rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and the [graph-probe/biclique note](ProjectA_GRAPH_EXTENSIONS_BICLIQUE_AND_IMAGE_STABILITY_2026-11-20.md). It does **not** assert associativity when adjoining arbitrary noninvertible map graphs.

Let G be a compact Hausdorff spatial locale. For ordinary A,B⊆G, set
\[
p(A,B)=[A\times B]\le G^2,\qquad q(A,B)=[A]\times_{\rm Loc}[B].
\]
These are the point-generated and full rectangles. The independent referee established
\[
r(A,B)\circ s(C,D)=
\begin{cases}q(A,D),&[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0,\end{cases}
\tag{RC}
\]
for r,s independently chosen as p or q.

### 1. Partial homeomorphism graphs and their exact actions

A **clopen partial homeomorphism** is a homeomorphism \(h:U_h\to V_h\) between clopen subspaces of G. Its graph \(\Gamma_h\le G^2\) is closed, spatial and point-generated (the domain is compact Hausdorff). The empty map is allowed, with graph 0. For ordinary A,B and t∈{p,q},
\[
\boxed{
\begin{aligned}
t(A,B)\circ\Gamma_h&=t(A,h(B\cap U_h)),\\
\Gamma_h\circ t(A,B)&=t(h^{-1}(A\cap V_h),B).
\end{aligned}}
\tag{PH}
\]

**Proof.** When restricting any point-generated p(A,B) to the clopen sector G×U_h, we obtain exactly p(A,B∩U_h); when restricting q(A,B), we obtain q(A,B∩U_h). Indeed the clopen decomposition G=U_h⊔U_h^c splits the sublocale lattice and restrictions preserve joins of point generators, while product meets split accordingly. The composability pullback with Γ_h is this restriction, and the image map is the *isomorphism* id×h onto the corresponding G×V_h sector. This proves the first identity, with no image instability. The second is the same calculation for V_h×G, transported by h^{-1} on the first coordinate.

For two such maps \(h:U_h\to V_h\) and \(k:U_k\to V_k\),
\[
\Gamma_h\circ\Gamma_k=\Gamma_{k\circ h|_{U_h\cap h^{-1}(U_k)}},
\tag{PHH}
\]
and the restricted domain and range are again clopen. Thus the class of clopen partial homeomorphism graphs is composition-closed and converse-closed.

### 2. Associative finite-join closure

**Theorem 2.1 (internal).** Let \(\mathscr A_{\rm cl}(G)\) be the collection of **finite joins** of generators of the forms p(A,B), q(A,B), and Γ_h for clopen partial homeomorphisms h. Then \(\mathscr A_{\rm cl}(G)\) is closed under localic relational composition and converse; composition is **associative** and distributes over finite joins. Its identity is Γ_id=Δ_G.

**Proof.** Formula (RC) handles any two rectangular generators, (PH) handles one rectangle and one graph, and (PHH) handles two graphs. All outcomes remain in the generator class, so finite-join closure follows.

To verify associativity, consider a triple of generators, coding rectangles by R and graph factors by H.

- **RRR:** formula (RC) gives zero iff an adjacent middle support intersection is zero; otherwise the full outer q-rectangle, independent of bracketing.
- **RRH:** the two bracketings produce q(A,h(D∩U_h)) when the middle intersection [B]∧[C] is nonzero (zero otherwise), by (RC) and (PH).
- **HRR:** similarly both produce q(h^{-1}(A∩V_h),D) under the same middle intersection test.
- **RHR:** one bracketing tests [h(B∩U_h)]∧[C]≠0, the other [B]∧[h^{-1}(C∩V_h)]≠0. The tests are equivalent under the sublocale isomorphism h:U_h≅V_h, using the clopen restriction property. Both yield the same full outer q(A,D) if nonzero.
- **RHH / HHR:** both use the same restricted composite partial homeomorphism and the associative restriction of subsets under the maps.
- **HRH:** restrictions of the first and last coordinate commute, giving the same rectangle t(h^{-1}(A∩V_h),k(B∩U_k)).
- **HHH:** composition of partial homeomorphisms is associative.

The zero cases are included in each formula. Thus all possible triples of generators associate. Since localic relational composition distributes over **finite** joins, associativity extends to their finite-join closure. Converse interchanges p(A,B)↔p(B,A), q(A,B)↔q(B,A) and Γ_h↔Γ_{h^{-1}}. The graph of the total identity is the diagonal and is a two-sided identity. □

**Scope:** The theorem uses **clopen** domain and range for arbitrary supports A,B. Their induced sublocales split along clopens, a property not automatically available for arbitrary open domains. Do not replace "clopen" by "open", or "partial homeomorphism" by "proper/open noninvertible map", without a separate analysis.

### 3. A genuinely noninvertible infinite example

Take G=2^ℕ, Cantor space, and the left-shift map \(\sigma:G\to G\), \(\sigma(x_0x_1x_2\ldots)=x_1x_2\ldots\). It is **two-to-one**, continuous, open and proper. Let
\[
U_0=\{x:x_0=0\},\qquad U_1=\{x:x_0=1\}
\]
be the two clopen cylinders. Each restriction \(\sigma|_{U_i}:U_i\to G\) is a homeomorphism, so
\[
\boxed{\Gamma_\sigma=\Gamma_{\sigma|_{U_0}}\vee\Gamma_{\sigma|_{U_1}}\in\mathscr A_{\rm cl}(G).}
\tag{SHIFT}
\]
Its graph has infinitely many ordinary pairs and cannot be covered by finitely many complete bipartite graphs (each nonempty rectangle inside the graph of a function has only one target value, whereas σ has infinite image). The **reflexive symmetric graph relation**
\[
H=\Delta_G\vee\Gamma_\sigma\vee\Gamma_\sigma^\smile
\]
belongs to the associative algebra and therefore has bracketing-independent powers. This gives a nontrivial noninvertible **positive** example beyond finite biclique covers and globally invertible homeomorphisms.

Contrast with the earlier dense enumeration graph ℕ_discrete→Q⊂Cantor: its source is an **open but nonclopen** sublocale of the compactification, its image-surjection is not pullback-stable, and the singleton probes produce a nonassociative triple.

### 4. Mathematical position and next boundary

We now have three concrete safe graph families inside compact Hausdorff locales: (1) finite biclique covers plus the diagonal, (2) graphs of total homeomorphisms, and (3) finite joins of graphs of **clopen partial homeomorphisms**, all together in one associative algebra with p/q rectangles.

The natural next boundary is a noninvertible continuous map not expressible as a **finite** union of clopen partial homeomorphisms, or a partial homeomorphism with an **open, nonclosed** domain. The exact graph-probe criterion in the companion note detects failure of *nonzero-sublocale reflection* of its localic image, but it is only a necessary diagnostic for the much stronger question of adjoining the graph to the whole rectangular algebra.

**Open:** characterize graphs \(\Gamma_f\) that can be adjoined to \(\mathscr R_\vee(G)\) without loss of associativity. Special candidate classes: finite-sheeted local homeomorphisms without globally clopen trivializations; proper maps with nonspatial restrictions to induced point-generated supports; and clopen versus merely open partial homeomorphisms. This should be adversarially audited before being promoted into an externally certified theorem ledger.
