# Project A — returning to ordinary graphs: biclique covers, map graphs, and image stability
## First graph-extension segment, 20 November 2026 — NEW INTERNAL deductions

**Scope / provenance.** This note continues the [independently blind-refereed compact-Hausdorff rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and [Cameron–Kumar revisitation](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md). New items in §§2–5 are **internal deductions**, not part of either independent referee report. We work in classical Loc; products and composition are genuine locale pullbacks followed by images. Literature priority is unchecked.

**Big-picture distinction.** The Stone examples below put arbitrary point-generated graph relations on Stone locales; they are NOT claimed to arise as one of Cameron–Kumar's canonical Ins, Cm, Ury, or Fun graphs (which are just equality in compact Hausdorff topology). The intrinsic separation hierarchy remains a separate but interacting program. The aim here is to understand which *graph operations and witness presentations* survive localic image-defined composition.

### 1. The audited positive algebra

For compact Hausdorff G and ordinary A,B⊆G put
\[
p(A,B)=[A\times B]_{G^2},\qquad q(A,B)=[A]_G\times_{\rm Loc}[B]_G.
\]
The referee's theorem gives
\[
r(A,B)\circ s(C,D)=
\begin{cases}q(A,D),&[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0,\end{cases}
\tag{RC}
\]
for any independent choices r,s∈{p,q}. Hence all finite joins of such p/q rectangles form an associative, converse-closed algebra under localic composition, despite possible pointless middle intersections. Arbitrary point-generated relations [T] are not automatically in this algebra because composition is not known to preserve infinitary joins.

### 2. Exact graph-probe criterion for an image-map defect

Let f:S→Y be **any** locale map with image J=im(f)≤Y, and let B≤Y be any sublocale. Realize the typed relations below as relations between clopen summands of a larger locale G, with two singleton marker summands {u},{v}:
\[
R=\{u\}\times B,\quad F=\Gamma_f^\smile\subseteq Y\times S,\quad
T=S\times\{v\}.
\]
The source/target S may be a nonclosed sublocale of a compact ambient G. The graph-converse F is the image of S under (f,id_S):S→Y×S, an embedding.

**Proposition 2.1 (graph-probe associator).**
\[
\boxed{
(R\circ F)\circ T=
 \begin{cases}\{(u,v)\},& B\times_Y S\ne0,\\0,&B\times_Y S=0,\end{cases}
}
\]
and
\[
\boxed{
R\circ(F\circ T)=
 \begin{cases}\{(u,v)\},&B\wedge J\ne0,\\0,&B\wedge J=0.\end{cases}
}
\tag{GP}
\]

**Proof.** The genuine path pullback R×_Y F is canonically B×_Y S, whose image in {u}×S is the same sublocale, so R∘F={u}×f^{-1}(B). The rectangular lemma applied to the full rectangle S×{v} gives the first formula. Conversely F∘T is the image of f:S→Y with a fixed singleton target, hence J×{v}; composing the full rectangles {u}×B and J×{v} gives the second formula. A nonzero B×_Y S always has nonzero image contained in B∧J, so only the right-associated product can be strictly larger in this probe.

Thus the precise obstruction is
\[
\boxed{B\wedge\mathrm{im}(f)\ne0\quad\text{while}\quad f^{-1}(B)=0.}\tag{*}
\]
For a fixed f, absence of ALL such graph-probe associators is exactly the condition that every nonzero sublocale of J=im(f) have nonzero inverse image under its image-factor surjection e:S→J. Call this **nonzero-sublocale reflection** as descriptive terminology; do not claim it is established nomenclature or equivalent to full pullback-stable surjectivity.

If e:S→J is a **pullback-stable surjection**, then (*) is impossible. In particular open or proper surjections provide this sufficient condition, by their classical pullback stability (Picado–Pultr–Tozzi, *Locales*, Chapter II). **This only certifies the singleton graph probes (GP), not arbitrary associativity after adjoining Γ_f to the whole rectangular algebra.**

**Concrete failure.** Let Y be Cantor, Q⊂Y a countable dense set, I=Y\Q dense; X=ℕ∪{*} the one-point compactification and S=ℕ the open discrete sublocale of X. Choose an enumeration f:S→Q⊂Y. Its localic image in Y is the **induced spatial sublocale** [Q]. Pulling [I] back along f gives 0: S is the coproduct of its singleton points, all mapped into Q, and no singleton lies in I. Yet [I]∧[Q]≠0 by Isbell density. Thus (GP) gives
\[
(R\circ F)\circ T=0,\qquad R\circ(F\circ T)=\{(u,v)\}.
\]
All three factors are point-generated; the outer two are full rectangles (singleton-leg). The middle relation Γ_f^\smile is a point-generated *infinite injective matching graph*, not a finite join of complete bipartite relations. All ordinary three-step paths from u to v are absent: the right-associated localic edge is created after taking an image, through a **pointless** middle meet.

### 3. Graph-theoretic positive class: finite biclique covers plus loops

For an ordinary directed adjacency set E⊆G_pts×G_pts, suppose
\[
E=\Delta_{\rm pts}\ \cup\
\bigcup_{i=1}^m(A_i\times B_i)
\tag{BC}
\]
with a **finite** number of complete bipartite edge sets, all contained in E. (For undirected adjacency add each B_i×A_i as well.) Let [E]≤G² be the point-generated localic relation. Since the ambient diagonal Δ_G is spatial for compact Hausdorff G,
\[
[E]=\Delta_G\vee\bigvee_{i=1}^m p(A_i,B_i).
\tag{BC'}
\]

**Proposition 3.1 (unital finite-biclique algebra).** Adjoin Δ_G to the referee's associative finite-join rectangular algebra, as a two-sided unit, and close under finite joins. The result is still closed under composition and associative: expand products by finite distributivity and contract the Δ factors. Thus every [E] of the form (BC') belongs to an **associative algebra**, and arbitrary heterogeneous compositions of finitely many such relations associate.

This gives a genuinely *graph-theoretic sufficient condition*, expressed by finite biclique-cover number (Boolean rectangle rank), for reflexive graph relations on an **infinite** compact Hausdorff space to compose associatively.

**Not necessary:** Δ_G itself generally has infinite biclique-cover number as an ordinary infinite matching of loops, yet is the unit. Similarly, a graph of a homeomorphism may have infinite biclique-cover number but still lie in another safe algebra (§4). The condition is sufficiency, not characterization.

### 4. A second positive class: add graphs of homeomorphisms

Let Homeo(G) be the group of homeomorphisms of compact Hausdorff G. For each h∈Homeo(G) let Γ_h≤G² be its spatial closed graph, x↦h(x).

**Proposition 4.1 (homeomorphism-graph extension; internal).** The finite-join algebra generated by all p(A,B), q(A,B), and Γ_h (h∈Homeo(G)) is closed under composition, converse, and associative.

**Generator formulas.** For either t=p or q and h,k∈Homeo(G),
\[
\begin{aligned}
t(A,B)\circ\Gamma_h&=t(A,h(B)),\\
\Gamma_h\circ t(A,B)&=t(h^{-1}(A),B),\\
\Gamma_h\circ\Gamma_k&=\Gamma_{k\circ h}.
\end{aligned}\tag{HG}
\]
Each equality follows from the localic graph pullback and the fact that homeomorphisms induce **isomorphisms** on the affected coordinate. In particular, they preserve point-generation and full localic products.

For any triple of generators: (i) if all three are rectangles use (RC); (ii) if graphs occur only at the beginning/end, use the isomorphism action and (RC); (iii) for a rectangle–graph–rectangle triple the two overlap tests are equivalent under h,
\(
[h(B)]\wedge[C]\ne0\iff[B]\wedge[h^{-1}(C)]\ne0;
\)
(iv) for two/three graphs use group composition and action laws. Thus the two triple bracketings coincide in every case. Finite distributivity promotes this to finite joins. The relation Γ_id=Δ_G is already the identity.

For infinite G, a homeomorphism graph is ordinarily an infinite matching and generally has no finite biclique cover. This positive example demonstrates that **failure of finite biclique cover alone does not imply nonassociativity**: the relevant alternative mechanism is invertible, image-stable graph composition.

**Boundary:** No corresponding closure theorem is asserted for arbitrary proper or open (noninvertible) maps. Even if f is proper on compact G, its restrictions to the induced spatial sublocales [B] need not inherit the exact properties required for composing with nonspatial q(A,B); the singleton probe (GP) is too weak to decide this.

### 5. Witnesses, the original motivation, and next problem

The finite biclique presentation (BC) is a finite **witness-indexed decomposition** of adjacency. The referee's directed overlap graph on witness labels has an arrow i→j when the target support [B_i] meets the next source support [A_j] *localically*, which is weaker than requiring a shared **ordinary vertex**. Its exact-length walks recover every composition power k≥2, retaining the localic pointless-intersection information in a finite combinatorial shadow.

This directly echoes the original Cameron–Kumar emphasis on graph paths, common witnesses, and §8 Dowker complexes. A biclique index is a binary common-witness label; higher nerves should remember *simultaneous* overlaps and not just pairwise ones. But no new Dowker or simplicial theorem is claimed here.

**Three current positive mechanisms:**
1. Coherent/spectral or closed/proper intrinsic relation families retain witness images under pullback.
2. Finite complete-bipartite decompositions yield an associative rectangular calculus, even for nonclosed and nonspatial endpoint supports.
3. Graphs of homeomorphisms yield invertible reindexing, and can be added to that algebra.

**Negative mechanism:** A noninvertible graph whose image-surjection loses nonzero support under pullback can produce a ghost edge after earlier image collapse.

**Next bounded questions:** (A) Can one enlarge the algebra with graphs of **open or proper noninvertible** maps under a checkable condition on all induced-support restrictions, rather than just the singleton probes? (B) Which canonical Cameron–Kumar graph sublocales admit useful finite biclique/witness presentations? (C) Is there a higher localic witness/nerve invariant that retains exactly the distinctions erased by image-defined binary composition?

No unrestricted associativity, infinite-join interchange, or novelty claim follows.
