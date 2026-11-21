# Project A — unbounded finite degree, but associative graph calculus
## A positive boundary theorem for a countably stratified Stone projection
**20 November 2026 · NEW INTERNAL RESEARCH, NOT EXTERNALLY AUDITED**

**Previous question.** The [finite-to-one map note](ProjectA_FINITE_TO_ONE_GRAPH_BRANCHING_STRATA_AND_SPIKES_2026-11-20.md) constructed an open proper surjection f whose finite fiber cardinalities are unbounded, so its graph has no finite locally closed inverse-branch cover. It asked whether adjoining that graph and its converse to the independently reviewed compact-Hausdorff [rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) destroys associativity. **Answer for this specific example: no.** Its full generated finite-join algebra is associative, even though \(\lambda_{\rm lc}(f)=\infty\).

This is an INTERNAL proof, relying on exact sublocale pullbacks/images. Its novel stability and algebra claims should be subjected to adversarial and blind audits before entering the externally certified theorem ledger. No originality/priority claim.

### 1. The stratified compact Stone map

Choose copies C_n of Cantor space, n≥1, and put
\[
Y=\left(\coprod_{n\ge1}C_n\right)^*,\qquad
X=\left(\coprod_{n\ge1}C_n\times\{1,\ldots,n\}\right)^*.
\tag{1}
\]
These are one-point compactifications of locally compact countable disjoint unions of compact metric Stone blocks. The compactification points are \(\infty_Y,\infty_X\). The spaces are compact metrizable Stone. Define f:X→Y by f(y,j)=y over C_n, and f(\infty_X)=\infty_Y.

Each C_n is clopen in Y; each sheet X_nj=C_n×{j} is clopen in X. Their complements \(Y^\circ=Y\setminus\{\infty_Y\}\), \(X^\circ=X\setminus\{\infty_X\}\) are open disjoint unions of these clopen pieces.

The map f is continuous, open, proper, and surjective. It is **not** a local homeomorphism at infinity; every neighborhood of \(\infty_X\) contains all n sheets for sufficiently large n. Its fibers have cardinality n over C_n and 1 over infinity. Therefore no finite family of injective partial maps can cover X, i.e. the locally closed inverse-branch cover number \(\lambda_{\rm lc}(f)=\infty\).

Let G=X⊔Y (optional finitely many clopen singleton markers do not affect any arguments).

### 2. Preliminary localic gluing facts

**(a) Open/closed two-piece detection.** In any locale Z with an open sublocale O and complementary closed F, O∨F=Z and O∧F=0. The coframe of sublocales is finite-distributive, so every sublocale S≤Z satisfies
\[
S=(S\wedge O)\vee(S\wedge F).\tag{2}
\]
Consequently equality of sublocales can be tested by restriction to O and F. This remains true after arbitrary base change, because pullback on sublocales preserves finite joins and meets.

**(b) Disjoint open coproduct detection.** Sublocales of an ordinary open topological disjoint union \(\coprod_n Z_n\) can be restricted/tested componentwise. Locales form an extensive category on disjoint coproducts; arbitrary base changes over such a coproduct split componentwise.

**(c) A finite sublocale cover is stably surjective.** If S_1∨…∨S_m=Z as sublocales, the canonical coproduct map \(\coprod_iS_i\to Z\) is a pullback-stable locale-surjection. Indeed pullback preserves finite joins and the image of a coproduct of sublocale embeddings is their join. This applies even when the S_i have no ordinary pointwise overlap and their meet contains pointless material.

**(d) Induced spatial support under clopen and open/closed restriction.** For any ordinary E⊂Z and open or closed subspace W⊂Z, \([E]\wedge W=[E\cap W]\). For closed W, split the generating point set into E∩W and E\W, use a finite join, and observe the second piece lies in the complementary open; for open W use its complementary closed subspace similarly. This extends to locally closed W. A one-point-legged product \(\{z\}\times[A]\) is spatial.

These facts use *finite* coframe joins. They do not assume arbitrary distribution of relation composition over infinite joins.

### 3. Point-generated inverse images are exact

**Lemma 3.1.** For every ordinary B⊆Y,
\[
\boxed{f^{-1}([B]_Y)=[f^{-1}(B)]_X.}\tag{3}
\]

On every clopen sheet X_nj, f is an isomorphism onto C_n, so the claimed inverse-image identity holds after restriction to X_nj. Thus it holds on the whole open X° by disjoint-coproduct detection. On the closed singleton \(\{\infty_X\}\), both sides are the singleton exactly when \(\infty_Y\in B\), and otherwise zero. Apply (2) to finish.

The lemma asserts spatiality of this **particular** pullback. It does not assert that inverse images of arbitrary induced spatial sublocales under all continuous maps are spatial.

### 4. Every selected-image map is universally surjective

For arbitrary ordinary E⊆X, set D=f(E)⊆Y, and let
\[
e_E:[E]_X\longrightarrow[D]_Y
\tag{4}
\]
be the induced map (it has target the point-generated **image**, not the topological closure of D).

**Lemma 4.1 (hereditary stable image).** Each e_E is a **pullback-stable locale-surjection**, for arbitrary E.

**Proof.** Restrict over C_n. The source is the **finite** disjoint union of the selected sheet subspaces \([E\cap X_{nj}]\), j=1,…,n; each maps by a homeomorphism onto an induced spatial sublocale \(D_{nj}=[f(E\cap X_{nj})]\le C_n\). The finite join \(D_{n1}\vee\cdots\vee D_{nn}=[D\cap C_n]\) is the entire selected target on C_n. Thus the induced map on C_n is pullback-stably surjective by §2(c). These blockwise surjections assemble over the open target Y° by §2(b), retaining pullback stability under *arbitrary* base changes.

On the complementary closed point \(\{\infty_Y\}\), the selected map is either an isomorphism of singleton locales (if infinity is in E) or a map of zero locales (if infinity is absent from E and hence from D). Its base changes are surjective as well.

For any base change T→[D], the preimages of Y° and {\(\infty_Y\)} form a complementary open/closed pair on T, jointly covering T by a **finite** join. The image of the pulled-back selected map contains each of those two target pieces, because its restrictions to them are surjective. Hence its image is all T. This is exactly pullback-stable surjectivity. □

**Corollary 4.2 (all localic singleton probes vanish).** For every ordinary E⊆X and arbitrary sublocale B≤Y,
\[
\boxed{
[f(E)]\wedge B\ne0
\iff
[E]\wedge f^{-1}(B)\ne0.
}\tag{5}
\]
The reverse-to-right direction follows by pulling back the nonzero overlap along e_E and using its stable surjectivity; the converse follows by taking its image. This is stronger than the earlier necessary test in which B was itself point-generated. **It does not by itself establish associativity**; the kernel-pair and mixed-word calculations below are also needed.

### 5. A finite pure-graph calculus

Let \(g=\Gamma_f\le X\times Y\) and \(g^\smile\le Y\times X\), and write
\[
K=X\times_Y X\hookrightarrow X\times X
\tag{6}
\]
for the kernel-pair relation. K is a **closed spatial** relation since Y is Hausdorff and X compact. On every clopen X_n block, K is the finite union of graphs of the homeomorphisms between its n sheets; over infinity it is the identity singleton.

In diagrammatic composition order (first left, then right),
\[
\begin{gathered}
g\circ g^\smile=K,\qquad g^\smile\circ g=\Delta_Y,\\
K\circ K=K,\quad K\circ g=g,\quad
g^\smile\circ K=g^\smile.
\tag{7}
\end{gathered}
\]
Each follows from the actual graph pullbacks, with the reverse-inclusion supplied by explicit diagonal/identity sections and the upper inclusion by equality of f-images; g^\smile g uses surjectivity of f. Type-incompatible products are 0. Along with \(\Delta_X,\Delta_Y\), these are all possible nonzero pure graph words. Their composition is associative (direct finite multiplication table, or proper/closed-relational composition on compact locales).

For any ordinary E⊆X define its fiber saturation
\[
\operatorname{Sat}(E)=f^{-1}(f(E)).
\tag{8}
\]
Combining (3) and the stable image lemma gives \([{\rm Sat}(E)]=f^{-1}([f(E)])\).

### 6. Exact actions on point-generated AND full rectangles

For any typed source/target clopen components of G, write
\[
p(A,B)=[A\times B],\qquad q(A,B)=[A]\times_{\mathrm{Loc}}[B],
\]
and let t denote independently p or q. The following expressions are typed by the domain/range of f (and include the empty-set zero cases):
\[
\boxed{
\begin{aligned}
t(A,E)\circ g &=t(A,f(E)), & E\subseteq X,\\
g^\smile\circ t(E,D)&=t(f(E),D), & E\subseteq X,\\
t(A,B)\circ g^\smile&=t(A,f^{-1}(B)),&B\subseteq Y,\\
g\circ t(B,D)&=t(f^{-1}(B),D), & B\subseteq Y,\\
t(A,E)\circ K&=t(A,\operatorname{Sat}(E)),&E\subseteq X,\\
K\circ t(E,D)&=t(\operatorname{Sat}(E),D),&E\subseteq X .
\end{aligned}}
\tag{ACT}
\]

**Proof for g, g^\smile.** Composing a p-rectangle with a functional graph on its **image-forming** side is the image under id×f (or f×id) of the spatial point-generated rectangle. Localic image preserves arbitrary joins of point sublocales, so the result is precisely the corresponding p(A,f(E)) or p(f(E),D). For a q-rectangle, the same image map is the product of id with e_E; by Lemma 4.1 it is a surjection after product with any locale, so the image is the **full** q-rectangle on f(E).

On the **inverse-image** side (p(A,B)∘g^\smile or g∘p(B,D)), the path locale is the actual pullback of the rectangle along id×f or f×id, with an embedding as endpoint map. Over each clopen sheet X_nj the map is an isomorphism, so the pullback is exactly the point-generated p-rectangle on the preimage of B. Over the closed point infinity, both sides are either the corresponding spatial one-point-legged rectangle or 0; glue using the complementary open/closed decomposition (2). The q-case follows immediately from the product pullback and Lemma 3.1.

**Proof for K and q.** The path through K ending in X computes the fiber product \([E]\times_Y X\to X\). This map is the pullback of e_E:[E]→[f(E)] along \(f^{-1}([f(E)])\hookrightarrow X\); it is a pullback-stable surjection onto \([\mathrm{Sat}(E)]\) by Lemmas 3.1 and 4.1. Taking its product with [A] and imaging yields q(A,Sat(E)). The dual action on the first endpoint is symmetric.

**Proof for K and p (the critical possible nonspatial remainder).** Ordinary composable triples imply the lower bound
\[
p(A,\operatorname{Sat}(E))\ \le\ p(A,E)\circ K.
\]
Endpoint support and Lemma 3.1 imply the upper bound q(A,Sat(E)). We must exclude a larger, pointless remainder. Restrict the **target** coordinate to any clopen sheet X_nj: the corresponding piece of K is a **finite** join of graphs of homeomorphisms from the other n sheets over C_n, so the p-action follows from the isomorphism formula and **finite** distributivity. Thus the result equals p(A,Sat(E)) on all of the open target X°.

On the closed target singleton infinity, the upper bound q(A,Sat(E)) restricts to 0 when \(\infty_X\notin E\), or to the **spatial** point-legged rectangle [A]×{\(\infty_X\)} when \(\infty_X\in E\). In the latter case this entire rectangle already belongs to the lower point-generated bound. Hence equality also holds on infinity. The open/closed detection (2) finishes the p-action. The first-endpoint action is the converse argument.

The proof never assumes \(p=q\) or treats an arbitrary infinite join of graph pieces as composition-distributive.

### 7. Overlap reciprocity for the graph generators

Let L be any of the five pure-graph types \(\Delta_X,\Delta_Y,g,g^\smile,K\), with ordinary set-valued forward and backward relational image operators \(L_{\#}\), \(L^{-1}_{\#}\). E.g. for g these are f(E) and f^{-1}(C); for g^\smile they are f^{-1}(B) and f(C); for K both are Sat.

**Lemma 7.1 (localic overlap reciprocity).** For all ordinary subsets B,C in the appropriate typed spaces,
\[
\boxed{
[L_{\#}B]\wedge[C]\ne0
\iff
[B]\wedge[L^{-1}_{\#}C]\ne0.
}
\tag{REC}
\]

For g, this is Corollary 4.2 with B as the chosen source subset and C as the target sublocale (and Lemma 3.1). For g^\smile it is the same equivalence with source/target reversed. For K, both sides are equivalent to \([f(B)]\wedge[f(C)]\ne0\) by applying the g/g^\smile cases successively. Partial identity cases are immediate.

This equivalence is the **nonzero-mediator Frobenius test** required for associativity of rectangle–graph–rectangle words. It is substantially more precise than the claim that f is globally open or proper.

### 8. Closure and associativity of the generated finite-join algebra

Let \(\mathscr A_f(G)\) be the smallest family of localic endorelations on G containing **all** compact-Hausdorff p/q rectangles, both g and g^\smile, and the diagonal \(\Delta_G\), closed under finite joins and composition. (The graph g and its converse are already typed subrelations of G².)

**Theorem 8.1 (INTERNAL POSITIVE RESULT).** For the stratified projection (1),
\[
\boxed{\mathscr A_f(G)\text{ is an associative, converse-closed, unital, finite-join-distributive relation algebra.}}\tag{SAFE}
\]
Moreover, every element is a finite join of p/q rectangles and members of the **five-element typed pure-graph system** of §5 (and 0, with type-incompatible products zero). In particular its graph can be safely adjoined although \(\lambda_{\rm lc}(f)=\infty\).

**Proof.** Decompose any p/q rectangle across the **finite** clopen components X,Y of G into its typed p/q pieces. By the independently audited uniform rectangular formula (RC), two rectangular generators compose to 0 or a full q-rectangle. By (ACT), any rectangular generator composed with any pure graph generator remains a p/q-rectangle. By (7), pure graph generators compose to another member of the finite graph system (or 0). Thus the class of finite joins of these generators is closed under composition and converse, by **finite** distributivity; it contains the original generators and hence is precisely \(\mathscr A_f(G)\).

For associativity it suffices to compare all triple-generator patterns, coding a rectangle by R and a pure-graph generator by L.

- **RRR:** independently audited (RC).
- **RR L** and **L RR:** the single rectangle overlap test is unaffected by applying L only to the outer endpoint; (ACT) and (RC) give the same full q-result.
- **R L R:** the left bracketing tests \([L_\#B]\wedge[C]\ne0\), while the right bracketing tests \([B]\wedge[L^{-1}_\#C]\ne0\). By (REC) these agree; when nonzero both yield the full q-rectangle on the unchanged outer supports.
- **R L L** and **L L R:** the two ordinary set-image operators compose functorially along the pure-graph multiplication table (7), and (ACT) gives the same rectangle regardless of bracketing.
- **L R L:** the left and right graph actions operate independently on the two *outer* support coordinates of a rectangular generator, hence commute.
- **L L L:** associative by the finite pure-graph multiplication table.

The check includes all p/q choices, empty subsets and typed zero products. Finite distributivity promotes triple associativity to all finite joins. Converse preserves p/q and exchanges g↔g^\smile, while K=K^\smile; the unit is Δ_G. □

**Crucial limitation:** This proof is special to the *clopen finite-sheet blocks plus unique closed point at infinity*. It is not a theorem that every proper, open, finite-to-one map preserves rectangular associativity. The earlier open-proper infinite-compact-fiber counterexample and nonopen two-to-one spike example remain unaffected.

### 9. Significance and next questions

The conjectured necessity of a **finite** locally closed inverse-branch cover fails in this example:
\[
\lambda_{\rm lc}(f)=\infty,\qquad \mathscr A_f(G)\ \text{associative}.
\]
Thus infinite witness multiplicity is compatible with associative localic graph composition when it is **locally finite over a clopen stratification and the boundary fiber is a singleton**.

The more relevant invariant appears to be **hereditary stability of the image maps**
\(
[E]\to[f(E)]
\)
together with spatiality of inverse-image supports and controlled kernel-pair actions. This may suggest a sufficient general map criterion abstracted from Lemmas 3.1–7.1.

**Natural follow-up:** Replace the unique infinity fiber by a finite, nontrivial or nonspatial boundary fiber; or replace the clopen-sheet stratification by a nontrivial finite-sheeted covering varying at infinity. Determine whether selected-image stable surjectivity and the exact p/q actions persist. A separate higher-level question is whether the finite graph system in §5 admits a simple involutive semigroup or allegory presentation, clarifying the connection to ordinary graph witness calculus.

**Audit priority:** Check every claim concerning pullback-stable selected-image surjections, the p-action of the kernel pair at infinity, and preservation of the induced spatial sublocale by inverse image. In particular do not infer (SAFE) merely from absence of graph-probe defects; the explicit generator actions and (REC) are essential.
