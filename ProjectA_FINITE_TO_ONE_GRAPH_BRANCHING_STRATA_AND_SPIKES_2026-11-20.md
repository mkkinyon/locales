# Project A — finite-to-one graph maps: open stratified coverings versus proper spike obstructions
## New internal research segment · 20 November 2026

**Status:** NEW INTERNAL MATHEMATICS, not independently blind-refereed. This continues the independently reviewed [compact-Hausdorff rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and the internally argued [locally closed partial-homeomorphism and infinite-fiber projection boundary](ProjectA_GRAPH_LOCAL_HOMEOMORPHISM_POSITIVE_OPEN_PROPER_NEGATIVE_2026-11-20.md). Source results and newly derived statements are distinguished below. All locale theory is classical. Do not claim novelty/priority without literature search.

### 1. The organizing number: locally closed inverse-branch cover size

For a continuous map f:X→Y between compact Hausdorff spaces, define the **working invariant**
\[
\lambda_{\mathrm{lc}}(f)=\min\{m\in\mathbb N:X=P_1\cup\cdots\cup P_m,\quad
P_i\text{ locally closed in }X,\quad
f(P_i)\text{ locally closed in }Y,\quad
f|_{P_i}:P_i\to f(P_i)\text{ a homeomorphism}\},
\]
and set \(\lambda_{\mathrm{lc}}(f)=\infty\) when no finite decomposition exists. Pieces may overlap. This notation is introduced for the research program; it is **not asserted standard nomenclature**.

If \(\lambda_{\mathrm{lc}}(f)<\infty\), then on G=X⊔Y (compact Hausdorff), the graph \(\Gamma_f\) is the finite join of graphs of locally closed partial homeomorphisms. By the previously internally argued partial-homeomorphism algebra theorem, adjoining \(\Gamma_f\) and its converse to the **full finite-join point-generated/full rectangular algebra** preserves associativity. Necessarily \(\lambda_{\mathrm{lc}}(f)\ge\sup_y|f^{-1}(y)|\), since every piece is injective.

The converse "**no finite inverse-branch presentation implies nonassociativity**" is **not** claimed.

### 2. General structural fact: fiber-cardinality strata of open proper finite-fiber maps

**Proposition 2.1 (internal, elementary topological proof).** Let f:X→Y be a continuous **open** surjection between compact Hausdorff spaces, every fiber finite, with or without a uniform bound. Set
\[
Y_{\ge k}=\{y:|f^{-1}(y)|\ge k\},\qquad
Y_k=Y_{\ge k}\setminus Y_{\ge k+1}.
\]
Then each \(Y_{\ge k}\) is **open**; each \(Y_k\) is **locally closed**; and
\[
f_k:f^{-1}(Y_k)\longrightarrow Y_k
\]
is a **k-sheeted covering map** (if \(Y_k\) is nonempty).

**Proof.** For y with ≥k distinct preimages, choose k pairwise disjoint open neighborhoods U_i of those preimages. Each f(U_i) is open at y; every point of their intersection has a preimage in each U_i. Hence Y_{≥k} is open and Y_k is locally closed.

On Y_k every fiber has exactly k points. Restricted f_k is open: for O⊂X open, f(O∩f^-1 Y_k)=f(O)∩Y_k. It is also **closed** as a map to Y_k: a relatively closed C⊂f^-1(Y_k) is F∩f^-1(Y_k) for some closed F⊂X, and f_k(C)=f(F)∩Y_k; f(F) is compact closed because X is compact, Y Hausdorff. Fix y∈Y_k and write the fiber {x_1,…,x_k}. Choose disjoint relative open U_i around x_i in f^-1 Y_k. Then
\[
W=\bigcap_i f_k(U_i)\setminus f_k\bigl(f^{-1}(Y_k)\setminus\bigcup_iU_i\bigr)
\]
is a relative open neighborhood of y. Over every y'∈W, each U_i contributes ≥1 preimage and there are exactly k in all, hence exactly one in each U_i and none elsewhere. As f_k is open, each restricted sheet U_i∩f_k^-1 W→W is a homeomorphism. Therefore W is evenly covered.

**Important:** Y_k need not be compact. A finite trivializing chart cover of Y_k **does not** follow just from compactness of the original Y. The next lemma circumvents this using zero-dimensional **clopen partitions**.

### 3. Finite-sheet theorem for open uniformly bounded maps of Stone spaces

**Theorem 3.1 (internal).** Suppose X,Y are **compact metrizable zero-dimensional Hausdorff** spaces, f:X→Y is continuous open surjective, and
\(
1\le |f^{-1}(y)|\le N
\)
for all y. Then
\[
\boxed{\lambda_{\mathrm{lc}}(f)\le\sum_{k=1}^N k=\frac{N(N+1)}2.}\tag{OPEN-FIN}
\]
Consequently the graph of f can be adjoined to the associative finite rectangular algebra without destroying associativity, and the same is true after adjoining its converse.

**Proof.** The finite locally closed strata Y_k of §2 partition Y. Each Y_k is second-countable, metrizable, zero-dimensional. Proposition 2.1 makes f_k a finite k-sheeted covering of Y_k. Choose an evenly covered open neighborhood of every point of Y_k, refine each to a **clopen** neighborhood, and by second-countability select a countable clopen subcover C_1,C_2,…. Disjointize it:
\(
D_1=C_1,\quad D_n=C_n\setminus\bigcup_{j<n}C_j.
\)
Every D_n is clopen in Y_k, the D_n are disjoint, and their union is Y_k. Each D_n lies within one evenly covered neighborhood. Over D_n, arbitrarily label the k covering sheets 1,…,k. For each fixed label j, unite the j-th sheets over **all** D_n, obtaining P_{k,j}⊂f^-1 Y_k. This P_{k,j} is clopen in f^-1 Y_k, because it and its complement are unions of open sheets over disjoint clopen D_n. The restriction f|P_{k,j}:P_{k,j}→Y_k is a homeomorphism: its inverse is continuous on each of the pairwise disjoint clopen D_n, hence globally continuous.

The strata Y_k are locally closed in Y, and f^-1 Y_k are locally closed in X. Since P_{k,j} is clopen relative to f^-1 Y_k, it is locally closed in X. Thus each f|P_{k,j} is a **locally closed partial homeomorphism**, and the P_{k,j}, over k=1,…,N, cover X. There are at most N(N+1)/2 pieces; the prior algebra theorem applies.

**Point worth stressing:** The clopen refinement may require **infinitely many** chart domains. Nevertheless the sheets can be glued labelwise over the disjoint clopen partition into only k globally defined partial homeomorphisms per stratum. No mistaken finite-subcover appeal to a noncompact stratum occurs.

### 4. Proper surjection of degree ≤2 that fails the graph associativity test

**Theorem 4.1 (internal counterexample).** There is a continuous proper surjection f:X→Y of compact metrizable **Stone** spaces with all fibers of cardinality 1 or 2 such that the graph of f cannot be adjoined associatively to the finite-join rectangular algebra.

**Construction.** Take Cantor space Y, a countable dense ordinary subset Q={q_n:n≥1}, and dense complement I=Y\Q. Put
\[
X=(Y\times\{0\})\cup\{e_n=(q_n,1/n):n\ge1\}\subseteq Y\times[0,1],\quad
f(y,t)=y.
\tag{SPIKE}
\]
X is closed in compact Y×({0}∪{1/n}) and hence compact metric and zero-dimensional. The base copy maps bijectively to Y, and each q_n has one extra isolated point e_n. Thus every fiber has size ≤2. Each singleton {e_n} is open in X but its image {q_n} is not open in Y; f is **not open**. Being a continuous map of compact into Hausdorff, f is proper.

Let E={e_n:n≥1}, an **open discrete subspace** of X, and let [E] be its induced spatial sublocale. Its localic image under f is [Q] (the join of the image points). On the other hand,
\[
\boxed{[E]\wedge f^{-1}([I])=0,\qquad
f_*[E]=[Q],\qquad [Q]\wedge[I]\ne0.}\tag{S1}
\]
For the zero assertion, each e_n maps to q_n∉I; the pullback [I] to each singleton {e_n} is zero, since [I]≤Y\{q_n}. The discrete locale [E] is a coproduct of singleton points, so its entire pullback is zero. The nonzero overlap follows from the standard Isbell density property on Cantor space.

On G={u}⊔Y⊔X⊔{v}, put
\[
R=\{u\}\times[I],\quad F=\Gamma_f^\smile,\quad T=[E]\times\{v\}.
\]
These are **point-generated** localic relations; the two outer ones are full singleton-legged rectangles, and F is the converse of a **closed graph**, since f is a map between compact Hausdorff spaces. Yet
\[
\boxed{(R\circ F)\circ T=0\ne\{(u,v)\}=R\circ(F\circ T).}\tag{S2}
\]
Indeed, the left pullback meets [E]∧f^-1[I]=0, while the right inner composite is [Q]×{v}, which meets [I] pointlessly. Thus properness plus degree ≤2 does **not** suffice.

**Corollary:** \(\lambda_{\mathrm{lc}}(f)=\infty\), because a finite locally closed partial-homeomorphism decomposition would place Γ_f in the positive algebra, contrary to (S2). The following direct topological argument independently confirms this. If X were a finite union of locally closed homeomorphic pieces P_j, each f(P_j) locally closed in Y, then E∩P_j is relatively open in P_j (E is open in X); its image Q_j=f(E∩P_j) is relatively open in f(P_j), and hence **locally closed in Y**. The finitely many Q_j cover Q. But every locally closed subset L of Cantor space contained in Q has nowhere-dense closure: if cl(L) had nonempty interior, since L is open dense in its closure, L would contain a nonempty ordinary open subset of Cantor space, contradicting empty interior of Q. Thus finitely many such Q_j cannot cover the dense Q. Contradiction.

**Symmetric graph consequence:** Replace the three R,F,T by their union with converses and the diagonal. By the 4-level clopen support arrangement, the two threefold bracketings still differ on the singleton slice {u}×{v}. This gives a **single reflexive symmetric point-generated graph** on compact Stone space with ghost edge across distinct ordinary components. The computation is identical to the already noted infinite-fiber example, but now the middle graph is **two-to-one**.

### 5. Positive branched examples, even with a nontrivial branch set

**Example 5.1 (ordinary real fold).** The continuous open proper map
\(f:[-1,1]\to[0,1],\ f(t)=t^2\)
has fiber size 2 except at 0; it is not a local homeomorphism at 0. Its graph is the union of **two closed** partial-homeomorphism graphs: the restrictions to [-1,0] and [0,1], each homeomorphic onto [0,1]. Hence its graph belongs to the safe algebra on the compact Hausdorff disjoint union.

**Example 5.2 (complex branched square).** Let D be the closed unit disk, f(z)=z². Its domain is the union of four **locally closed** sets: the open upper half-disk Im(z)>0, the open lower half-disk Im(z)<0, and the two **closed real half-intervals** [-1,0], [0,1]. Each of the first two restrictions is a homeomorphism onto the slit disk D\[0,1] (the positive real ray removed), and each real half-interval restriction is a homeomorphism onto [0,1]. Thus \(\lambda_{\mathrm{lc}}(f)\le4\); this genuinely branched, open proper finite-to-one map is in the associative algebra.

**Example 5.3 (Stone branch gluing).** Take two copies of Cantor space Y, identify their corresponding points over an arbitrary closed F⊂Y, and let X be the resulting compact Hausdorff quotient. The natural map f:X→Y has fibers of size 1 over F and 2 outside; it is open and, when Y is Stone, X is Stone. Each original copy of Y maps to a **closed** subspace of X homeomorphic to Y, so Γ_f is the union of two closed partial-homeomorphism graphs. Choosing F neither empty nor clopen produces genuine branch points. This gives a positive 2-sheeted branched Stone example, directly contrasted with the nonopen spike map of Theorem 4.1.

These positive examples are already covered by the *locally closed partial-homeomorphism* theorem, but they show that **having branch points is not itself an obstruction**.

### 6. The still-open unbounded-multiplicity boundary

The uniform bound in Theorem 3.1 is **not automatic** from openness + properness + finite fibers. For an explicit compact metric Stone example, let Y be the one-point compactification of the topological disjoint union \(\coprod_{n\ge1}C_n\) of Cantor spaces, and let X be the one-point compactification of \(\coprod_{n\ge1}(C_n\times\{1,\ldots,n\})\). Define f blockwise by projection to C_n, and send infinity to infinity.

Then f is continuous, **open**, proper and surjective; its fiber size is n over C_n and 1 at infinity. All fibers are finite but their cardinalities are unbounded. Such a graph **cannot** admit a finite locally closed partial-homeomorphism decomposition, since any finite union of injective graph pieces imposes a uniform bound on fiber cardinality. However this observation by itself **does not prove a nonassociative triple**; a graph might belong to another safe class without a finite sheet decomposition.

**Open test:** determine whether this explicit open proper finite-fiber but unbounded-degree map preserves associativity when adjoined to the finite rectangular algebra. A positive result would prove finite locally closed inverse-branch rank is *not necessary* for associativity; a negative result would identify a genuinely infinitary **open** witness obstruction.

### 7. Project perspective and proposed follow-ups

We have separated three different issues that were conflated under "branched":
- **Global properness** controls the map on compact spaces but does *not* control images of arbitrary selected point-generated supports (spike counterexample).
- **Openness plus bounded degree on compact metric Stone spaces** forces a finite *locally closed inverse-branch presentation*, giving a positive associativity theorem.
- **Infinitely many witnesses** may occur either within a single compact fiber (negative Cantor×Cantor projection) or in an unbounded sequence of finite fibers (open question).

This suggests an interaction of two graph-theoretic ranks: the finite biclique-cover number and the newly introduced locally closed inverse-branch cover size \(\lambda_{\mathrm{lc}}\). Both yield finite witness presentations, whereas nonstable image formation can create an ordinary "ghost edge" after a parenthesized localic composite.

The project remains distinct from, but motivated by, Cameron–Kumar's **intrinsic** specialization/inseparability/Urysohn graphs: these are *imposed* graph relations on Stone locales, not claims that the compact Hausdorff topology itself has nontrivial inseparability edges.

**Audit status:** internal only. The positive open bounded-degree theorem, the 2-to-1 spike obstruction, and the branch-cover rank mechanism require adversarial review before promotion to the independently certified theorem ledger. No novelty or priority claim.
