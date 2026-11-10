# Project A — Brun–Fosse–Salbu (2023) and the Dowker rectangle nerve: exact crosswalk

**10 November 2026. Source-reading note, with newly derived localic comparison explicitly separated from source results. Not an external audit or novelty claim.**

Primary source: M. Brun, M. Gårdsmann Fosse, L. M. Salbu, *Dowker Duality for Relations of Categories*, arXiv:2303.16032v1 (2023), https://arxiv.org/pdf/2303.16032 (16 pages). Read Sections 1–6, in particular Definition 3.1; Definition 4.1–4.3; Theorems 4.5–4.6; Proposition 5.4; Corollary 6.1; Lemma 6.3 and Corollary 6.4; Corollary 6.7.

## I. What the authors prove (SOURCE)

A relation of categories is any functor \(R:\mathscr R\to\mathscr C\times\mathscr D\), not necessarily an inclusion. The bisimplicial rectangle nerve \(ER\) in bidegree \((m,n)\) consists of functors \(r:[m]\times[n]\to\mathscr R\) such that \(Rr=a\times b\) for uniquely determined functors \(a:[m]\to\mathscr C\), \(b:[n]\to\mathscr D\). The Dowker nerve \(DR\subseteq N\mathscr C\) is the image of \(ER_{m,0}\to N\mathscr C_m\), degreewise.

For each \(a\in N\mathscr C_m\), the fiber simplicial set \(\pi_R^a\) consists of all compatible rectangles over \(a\), allowing variable \(n\). \(R\) is a *Dowker relation* if every \(\pi_R^a\) is contractible or empty (Definition 4.2). Theorem 4.5: \(d(ER)\to DR\) is a weak equivalence if \(R\) is a Dowker relation; proof applies the standard rowwise-to-diagonal theorem for bisimplicial sets. Transposition yields a natural isomorphism of the diagonal rectangle nerves; if \(R\) and \(R^T\) both satisfy the condition, \(DR\simeq DR^T\) through that common diagonal (Theorem 4.6), naturally for morphisms of relations. Section 5 gives compatible homotopies. Application §6.1: for the comma relation \(F\downarrow G\to\mathscr C\times\mathscr D\), the two relevant fibers are nerves of \(F(a(m))\downarrow G\) and \(F\downarrow G(b(0))\), yielding Quillen's Theorem A. Application §6.2: uses the *translation/chaotic category* on a vertex set, as well as a chosen total order, and face-poset witness categories to show naturally \(|\mathrm{Sing}(K)|\simeq|K|\), where \(\mathrm{Sing}(K)_m\) is the set of all (possibly repeated) \(m+1\)-tuples spanning a simplex. This is not the usual topological singular complex \(\mathrm{Sing}(|K|)\).

## II. Our localic rectangle nerve exactly internalizes their construction (PROJECT DEDUCTION)

For any locale \(Z\), let \(\mathsf{Pair}(Z)\) be the *pair/indiscrete internal category* with object locale \(Z\), arrow locale \(Z\times Z\), and exactly one internal arrow between each generalized pair. A localic subrelation \(R\hookrightarrow X\times Y\) induces a functor of internal categories
\[
  \mathsf{Pair}(R)\to\mathsf{Pair}(X)\times\mathsf{Pair}(Y).
\]
The internal rectangle object at \((m,n)\) is represented by the locale
\[
 E_{m,n}(R)=\bigwedge_{0\le i\le m,\ 0\le j\le n}\pi_{ij}^{-1}(R)
 \hookrightarrow X^{m+1}\times Y^{n+1}.
\]
Reason: a functor into a pair category is determined by its vertex objects; factorization through \(a\times b\) says that the object at \((i,j)\) has coordinates \((x_i,y_j)\); its membership in \(R\) imposes precisely the displayed meet. This requires only finite limits, so it holds in Loc for arbitrary relations, *not just coherent* ones. Coordinate deletion and repetition reproduce both simplicial structures.

Consequently our earlier remark that the paper's nerve is only superficially analogous was too weak: our \(E_{\bullet,\bullet}\) is precisely the **internal-category rectangle nerve** obtained from the pair categories of locales. But the SOURCE theorem concerns simplicial sets and their weak equivalences; the above internalization does not import its homotopy theorem into Loc.

In coherent spectral locales with proconstructible \(R\), patches make every \(E_{m,n}\) proconstructible and point-determined. Forgetting topology gives exactly the bisimplicial set of rectangles for the **chaotic categories of the spectral point sets**. Taking \(R=\mathcal A\) (oriented specialization) gives
\[
 \operatorname{pt}K_m(\mathcal A)=\{(x_0,\dots,x_m):\exists y,\ \forall i\ x_i\le y\},
\quad
 \operatorname{pt}L_n(\mathcal A)=\{(y_0,\dots,y_n):\exists x,\ \forall j\ x\le y_j\}.
\]
These are the common-upper and common-lower simplicial sets, respectively (tuples with repetition), so the source Theorems 4.5–4.6 recover the ordinary pointwise Dowker equivalence. Each fiber over a tuple is the nerve of an indiscrete category on its witness set, automatically contractible when nonempty.

## III. A consequential choice: order categories versus chaotic categories (PROJECT DEDUCTION)

If instead one regards the poset \(P\) as a category in its natural way and takes the full subcategory \(\mathscr R\subseteq P\times P\) on \((x,y)\) with \(x\le y\), then its rectangle simplices are two monotone chains
\(x_0\le\cdots\le x_m\), \(y_0\le\cdots\le y_n\) such that \(x_m\le y_0\). Both Dowker nerves are just \(NP\), the *order complex*, since a chain always admits a terminal upper (or initial lower) witness from itself. Fiber categories have initial or terminal objects, so the paper's theorem is true but gives \(NP\simeq NP\), not Cameron–Kumar's common-witness complexes.

This is not merely a presentational distinction. Let \(P\) be the four-point poset with minima \(a,b\), maxima \(c,d\), and all four strict comparisons \(a,b<c,d\). The order complex \(NP\) is the four-cycle and has homotopy type \(S^1\). The common-upper complex has facets \(\{a,b,c\}\) and \(\{a,b,d\}\), glued along \(\{a,b\}\), so is contractible. The common-lower complex is likewise contractible. Thus the categorical order relation and the chaotic-categorified underlying *set* relation produce genuinely different invariants. Natural inclusion \(P\to\mathsf{Pair}(P)\) does not induce a homotopy equivalence of their Dowker nerves in general.

## IV. Precisely where a point-free Dowker theorem needs more (PROJECT ANALYSIS)

For a fixed tuple of generalized points, the witness object may have no global point. An *internal pair groupoid* on a witness locale is a Čech-type object; its geometric realization becomes locally terminal only in an ambient homotopy theory where the relevant witness projection is an **effective epimorphism** (effective-descent cover). The categorical proof's “nonempty witness set has contractible chaotic-category nerve” does not itself give that property for arbitrary maps of locales. It holds after patching coherent proconstructible relations: the patch of each \(E_{m,0}\to K_m\) and \(E_{0,n}\to L_n\) is a surjection of Stone locales, hence a proper effective-descent cover. Thus our earlier patched sheaf-theoretic Dowker equivalence is the exact **internal Čech realization** of the logic behind Brun–Fosse–Salbu, not a competing argument.

A general formal version: in any \(\infty\)-topos, for a (-1)-truncated relation \(R\hookrightarrow X\times Y\), define \(E_{m,n}\) as above and \(K_m,L_n\) by (-1)-truncated images. The effective-epi/mono factorization and universal Čech descent show
\[
  |\;K_\bullet\;|\simeq|\;E_{\bullet,\bullet}\;|\simeq|\;L_\bullet\;|.
\]
Proof: \(E_{m,\bullet}\) is the Čech nerve of effective epi \(E_{m,0}\to K_m\), and \(E_{\bullet,n}\) of \(E_{0,n}\to L_n\); commute the two geometric realizations. This is a general internal category/\(\infty\)-topos deduction, **not asserted by the 2023 paper**. It does not assert the same with image sublocales in unpatched Loc, whose surjective maps need not satisfy effective descent or stable base change. When representing our localic images in a sheaf \(\infty\)-topos, their effective image can differ from the representable localic image. This is the key missing compatibility condition.

## V. Disposition

- **Very relevant antecedent:** the bisimplicial rectangle viewpoint and functoriality; cite Brun–Fosse–Salbu whenever presenting this approach. The basic bisimplicial schema must not be advertised as an unexplored innovation.
- **More exact than anticipated:** the localic \(E_{\bullet,\bullet}\) is the internal rectangle nerve of pair categories, not merely an analogy.
- **Not resolved by the paper:** the effective descent/triquotient behavior of unpatched common-lower-witness maps, and the meaning of weak equivalence of simplicial locales. Previous coherent counterexample to triquotiency does not contradict any theorem of the paper.
- **Promising framing:** work with a specified internal homotopy theory of localic objects and require that localic image subobjects be the correct effective images. The patched coherent setting satisfies this condition; an unpatched theorem needs additional hypotheses or new methods.
- No user-supplied TeX is needed: arXiv PDF suffices for definitions, proofs, and comparisons.

**Working status:** source-derived assertions verified from 16-page arXiv version; localic internalization, the K_{2,2} comparison, and the \(\infty\)-topos formulation are project deductions, pending independent audit. No priority claim.