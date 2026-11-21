# Candidate B — selected-image stability implies an associative map-graph algebra

**This is the central, separately reviewable dependency of Candidate A's universal target dichotomy.** Please audit it independently, including all uses of compactness and product spatiality.

## B.1. Notation and hypothesis

Let f:X→Y be a continuous **surjection** between compact Hausdorff spaces, with G=X⊔Y. We use typed subrelations of G². For ordinary A,B⊆G put

\[
p(A,B)=[A\times B]_{G^2},\qquad q(A,B)=[A]_G\times_{\mathrm{Loc}}[B]_G.
\]

The distinction is critical: p is the spatial **point-generated** rectangle; q is the **full localic product**, potentially nonspatial. The prerequisite rectangular rule (file 05) states that any r∈{p(A,B),q(A,B)}, s∈{p(C,D),q(C,D)} satisfy

\[
r\circ s=0\ \text{if }[B]\wedge[C]=0,
\quad r\circ s=q(A,D)\ \text{otherwise}.\tag{RC}
\]

Let \(g=\Gamma_f\subseteq X\times Y\), \(g^\smile\subseteq Y\times X\), and \(K_f=X\times_Y X\subseteq X\times X\), the kernel-pair relation. All three are **closed spatial** sublocales of the compact Hausdorff ordinary products.

**Hypothesis (HSIS):** for every ordinary subset E⊆X, the induced point-surjective map

\[
e_E:[E]_X\longrightarrow[f(E)]_Y
\]

is a **pullback-stable locale-surjection** (surjective under arbitrary locale base changes, not merely sublocale inclusions).

**Theorem B.1 (candidate).** Under HSIS, the finite-join/composition algebra generated on G by **all** p/q rectangles, g, g^smile and Δ_G is associative, converse-closed and unital. Its elements are finite joins of p/q rectangles and members of a finite typed pure-graph system consisting of 0, Δ_X, Δ_Y, g, g^smile and K_f.

## B.2. Exact inverse image of an induced spatial support

**Lemma B.2.** For any continuous map f:X→Y of compact Hausdorff spaces and ordinary B⊆Y,

\[
\boxed{f^{-1}([B]_Y)=[f^{-1}(B)]_X.}\tag{INV}
\]

**Proof.** The inverse image of [B] identifies with \([B]\times_Y X\), i.e. with the inverse image of the **closed graph** of f under \([B]\times_{\rm Loc} X\to Y\times X\). Since X is compact Hausdorff, it is locally compact and the localic product of this spatial X with the spatial locale [B] is **spatial**, even if [B] is not locally compact. A closed sublocale of a spatial locale is spatial. Its ordinary points are precisely the pairs (b,x), b∈B, f(x)=b, in bijection with f^{-1}(B), and its embedding into X has the expected image. Thus it is the point-generated sublocale [f^{-1}(B)]. ∎

**Referee warning:** This does *not* assert spatiality of \([B]\times_{\rm Loc}[E]\) for arbitrary spatial [B],[E]. The locally compact multiplier is the **whole compact Hausdorff X**.

## B.3. Exact actions on point-generated rectangles

For t=p or q, the desired formulas are

\[
\begin{array}{rlrl}
t(A,E)\circ g &=t(A,f(E)), & E\subseteq X,\\
g^\smile\circ t(E,D)&=t(f(E),D), & E\subseteq X,\\
t(A,B)\circ g^\smile&=t(A,f^{-1}(B)),&B\subseteq Y,\\
g\circ t(B,D)&=t(f^{-1}(B),D),&B\subseteq Y,\\
t(A,E)\circ K_f&=t(A,\operatorname{Sat}(E)),&E\subseteq X,\\
K_f\circ t(E,D)&=t(\operatorname{Sat}(E),D),&E\subseteq X,
\end{array}\tag{ACT}
\]

where \(\operatorname{Sat}(E)=f^{-1}(f(E))\). All are understood as typed sublocales of G².

**First, prove (ACT) for p without HSIS.** On an image-forming side, such as p(A,E)∘g, the composability locale is the spatial point-generated rectangle itself and the endpoint map is \(\mathrm{id}\times f\). Image of an arbitrary join of singleton point sublocales is the join of their images, giving exactly p(A,f(E)). The converse orientation is analogous.

On an inverse-image side, such as p(A,B)∘g^smile, the path locale identifies as the preimage of the **closed** graph g^smile within the product \(p(A,B)\times_{\rm Loc}X\). This product is spatial because the **whole X** is compact Hausdorff. The path locale is closed in a spatial locale and is therefore spatial. Its ordinary points are exactly the composable triples, with endpoint set A×f^{-1}(B). The image is thus **exactly** p(A,f^{-1}(B)), not merely a sublocale between that and q(A,f^{-1}(B)). The analogous construction for p(A,E)∘K_f is a closed sublocale of p(A,E)×X, with endpoint set A×f^{-1}(f(E)). Its image is exactly p(A,Sat(E)). The two left-endpoint actions follow by converse.

**Next, prove (ACT) for q under HSIS.** For q(A,E)∘g, the composability locale is [A]×[E], and its endpoint map is the product of id_[A] with the selected-image map e_E:[E]→[f(E)]. HSIS implies this product is surjective onto **the whole q(A,f(E))**. The symmetric image-forming case follows by converse. For q(A,B)∘g^smile, the genuine pullback is [A]×f^{-1}([B]); by (INV) it is the full q(A,f^{-1}(B)). For the q-action of K_f, the relevant path projection is the pullback of e_E along f^{-1}([f(E)])↪X; by HSIS and (INV) it is a stable surjection onto [Sat(E)], and multiplication by [A] preserves its surjectivity. Hence its endpoint image is q(A,Sat(E)). The remaining orientations follow symmetrically.

**No general assertion about products of arbitrary spatial locales is used.** For p we have the whole compact Hausdorff multiplier; for q we use actual stable selected-image maps.

## B.4. Finite multiplication table for pure graph relations

Localic graph calculus gives the following exact identities in diagrammatic order:

\[
\begin{split}
g\circ g^\smile&=K_f,&g^\smile\circ g&=\Delta_Y,\\
K_f\circ K_f&=K_f,&K_f\circ g&=g,\\
g^\smile\circ K_f&=g^\smile.
\end{split}\tag{G}
\]

The other typed composites are with identities or are zero for incompatible clopen source/target blocks. The equality g^smile∘g=Δ_Y uses the **surjectivity of f**. Each equality can be proved by identifying the actual graph pullbacks, with diagonal witnesses for the needed lower bounds; alternatively, all are compact **closed** relational compositions and the image maps in question are proper. The table is associative. Note that K_f is a relation, not generally the diagonal on X.

## B.5. Overlap reciprocity

For ordinary E⊆X and B⊆Y, HSIS implies

\[
\boxed{[f(E)]\wedge[B]\ne0\iff[E]\wedge f^{-1}([B])\ne0.}\tag{NR}
\]

Indeed, the right-to-left implication follows by taking images under f. For the left-to-right implication, pull the **stably surjective** e_E back along the nonzero sublocale [f(E)]∧[B] of [f(E)]. The resulting source is nonzero and is precisely the relevant pullback in [E]. By (INV), it is [E]∧[f^{-1}(B)].

For every pure graph relation L in the table (Δ_X, Δ_Y, g, g^smile, K_f), define the *ordinary* set-theoretic forward/backward image of a subset E as \(L_\#E\), \(L^{-1}_\#E\). These are respectively E, f(E), f^{-1}(E), or Sat(E), depending on L and typing. Applying (NR), sometimes twice for K_f, yields

\[
\boxed{[L_\#B]\wedge[C]\ne0\iff[B]\wedge[L^{-1}_\#C]\ne0.}\tag{REC}
\]

This is the essential *middle witness reciprocity*, and it is stronger than just pointwise path existence.

## B.6. Closure and associativity

By (RC), rectangle × rectangle is 0 or a full q-rectangle. By (ACT), rectangle × pure graph and pure graph × rectangle are p/q rectangles of the same p/q type. By (G), graph × graph stays in the finite pure-graph system. Thus finite joins of these generators are closed under composition and converse. Localic composition distributes over **finite** joins, so it suffices to check three-generator words.

Use R for a p/q rectangle and L for a pure graph element. There are eight patterns:

- **RRR:** the previously proved uniform rule (RC) is associative.
- **RRL and LRR:** applying a graph to the outer endpoint does not alter the one middle rectangle-overlap test; (RC) and (ACT) yield the identical full q-rectangle (including zero).
- **RLR:** the two bracketings test [L_#B]∧[C]≠0 and [B]∧[L^{-1}_#C]≠0. (REC) gives equivalence, and both successful products are the same full q-rectangle on the untouched outer endpoint supports.
- **RLL / LLR:** the set-image operators on selected endpoint subsets obey the typed multiplication laws in (G), so successive (ACT) actions agree with the composite graph action.
- **LRL:** a graph on the left changes only the first endpoint of the middle rectangle; a graph on the right changes only the second. These actions commute.
- **LLL:** the finite pure-graph table is associative.

This checks associative multiplication on all generators. Finite distributivity extends it to all finite joins; the diagonal Δ_G is a unit, and converse preserves the collection. ∎

## B.7. What this does NOT show

- It does **not** assert that HSIS is necessary. The singleton graph probes give only the weaker condition (NR) for all E,B. Full stability demands arbitrary locale base changes.
- It does not assert arbitrary localic image-surjections are pullback-stable, nor that arbitrary nonrectangular point-generated relations belong to this algebra.
- It does not assert that the power-associativity of the *closed symmetric graph* Δ_G∨g∨g^smile requires HSIS: compact **closed** relation composition already associates. The condition here concerns its interaction with **all nonclosed point-generated rectangles**.
- Compact Hausdorff assumptions enter in (INV) and in the closed/spatial p-path argument. A constructive or general-locale extension is unproved.