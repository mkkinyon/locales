# Project A — (LC-PT) candidate counterexample by discrete-defect gluing

**15 November 2026. Complete internal proof candidate; NOT YET externally audited.** The claims below require an adversarial second reading before upgrading the problem register. No literature-priority claim is made. Compare the independently audited [stable-local-compactness theorem (A-SC)](ProjectA_ASC_CANONICAL_2026-11-15.md) and the [open/closed interface calculus](ProjectA_LCPT_OPEN_CLOSED_INTERFACE_2026-11-15.md).

## 1. Statement

**Proposed theorem.** There exists a **compact, locally compact, sober \(T_1\)** space \(X\) in which **every point sublocale is fitted**, but
\[
\boxed{\mathcal A(X)\ne\Delta_X.}
\tag{1}
\]
Thus (LC-PT), without *stable* local compactness, would have a negative answer. The space has a basis of compact opens, but that basis is not stable under finite meets; thus it does not contradict (A-SC).

## 2. The frame

Fix the Cantor space \(K\): nonempty, compact, zero-dimensional, Hausdorff, and without isolated points. For opens \(c,v\subseteq K\) put
\[
(c,v)\in L\quad\Longleftrightarrow\quad
c\setminus v\text{ is closed and discrete in the relative space }c.
\tag{2}
\]
Since \(v\) is open, \(c\setminus v\) is automatically closed in \(c\); the substantive condition is relative discreteness. Order \(L\subseteq\mathcal O(K)^2\) coordinatewise.

**Frame check.** Let \((c_i,v_i)\in L\), \(c=\bigcup_i c_i\), \(v=\bigcup_i v_i\). For any \(p\in c\setminus v\), choose i with \(p\in c_i\); then
\[
(c\setminus v)\cap c_i\subseteq c_i\setminus v_i.
\]
The right side is discrete in the open neighborhood \(c_i\) of p, so p is isolated in \(c\setminus v\). Thus \((c,v)\in L\). For two pairs, the defect of their meet satisfies
\[
(c_1\cap c_2)\setminus(v_1\cap v_2)
= ((c_1\setminus v_1)\cap c_2)\cup((c_2\setminus v_2)\cap c_1),
\]
a finite union of relatively closed discrete subsets in \(c_1\cap c_2\). Thus L is a subframe, with bottom \((\varnothing,\varnothing)\) and top \((K,K)\).

Set \(e=(\varnothing,K)\). The open locale \(U=O_X(e)\) and closed complement \(F=C_X(e)\) are both copies of \(K\), obtained from the second and first coordinates respectively.

## 3. Spatiality, sobriety, and \(T_1\)

Any point \(p:\mathcal O(X)=L\to2\) has \(p(e)=0\) or \(1\). In the first case it factors through \(F\cong K\), and in the second through \(U\cong K\). Hence the point set is two disjoint copies \(K_F\sqcup K_U\). The evaluation points separate elements of L (the coordinates really are open subsets of K), so \(X\) is spatial, and its point space is sober.

Each point is closed. The complement of \(p_F\) is the open \((K\setminus\{p\},K)\); the complement of \(p_U\) is the open \((K,K\setminus\{p\})\), valid because a singleton is relatively closed discrete. Thus \(X\) is \(T_1\).

## 4. Compactness and local compactness

X is compact: an arbitrary open cover of \((K,K)\) covers compact first-sheet K by its first coordinates, so finitely many first coordinates cover K. Their union pair \((c_*,v_*)\) has \(c_*=K\) and finite defect \(K\setminus v_*\) (closed discrete in compact K). Finitely many more members of the original cover cover those finitely many remaining second-sheet points.

More strongly, there is a **basis of compact opens**:
\[
(\varnothing,d),\qquad(d,d),\qquad(d,d\setminus\{p\}),
\tag{3}
\]
where d ranges over clopen subsets of K and p∈d in the third type.

To check compactness of \((d,d\setminus S)\) for S=∅ or \(\{p\}\), consider an arbitrary cover by pairs \((c_i,v_i)\). Compactness of d gives finitely many first coordinates whose union covers d; their combined second coordinate \(v_*\) misses only a finite set \(R=d\setminus v_*\), because R is a closed discrete subset of compact d. All of \(R\setminus S\) is covered by the full family of second coordinates, so finitely many supplementary pairs finish the cover. The compactness of \((\varnothing,d)\) follows directly from compactness of d in the open sheet.

To see (3) is a basis, consider \((c,v)\in L\). A U-sheet point of v has a neighborhood \((\varnothing,d)\le(c,v)\). An F-sheet point p in c∩v has \((d,d)\le(c,v)\) for clopen d⊂c∩v. If p∈c\setminus v, relative discreteness gives clopen d⊂c with d∩(c\setminus v)=\{p\}; then \((d,d\setminus\{p\})\le(c,v)\).

Thus L is continuous (indeed compact-open generated), and X is locally compact.

**Failure of stability.** Both \(e=(\varnothing,K)\) and \(b_p=(K,K\setminus\{p\})\) are compact opens, but
\[
e\wedge b_p=(\varnothing,K\setminus\{p\})
\tag{4}
\]
is **not** compact: within the open U-sheet it is \(K\setminus\{p\}\), a noncompact open subset of compact Hausdorff K because p is nonisolated. In particular the compact opens are not finite-meet stable. This is precisely why the independently audited (A-SC) theorem does not apply.

## 5. Every point is fitted — sublocale-level verification

For \(p_U\), the clopen neighborhoods \((\varnothing,d)\) inside U already have fitted meet \([p_U]\), as K is a Stone space. Thus \(p_U\) is fitted in X.

For \(p_F\), use the neighborhood family
\[
b_{p,d}=(d,d\setminus\{p\}),\qquad d\subseteq K\text{ clopen},\quad p\in d.
\]
Put
\[
T_p=\bigwedge_{d\ni p} O_X(b_{p,d})
\tag{5}
\]
in the lattice of sublocales, **not** merely in the lattice of point sets. We have \([p_F]\le T_p\). Restriction to U gives
\[
T_p\wedge U=\bigwedge_{d\ni p}O_U(d\setminus\{p\})=0.
\tag{6}
\]
For the last equality, \(O_U(d\setminus\{p\})=O_U(d)\wedge O_U(K\setminus\{p\})\), whereas the meet of the clopen neighborhoods O_U(d) of p is the closed point sublocale \([p]\), disjoint from \(O_U(K\setminus\{p\})\). The clopen-neighborhood assertion follows because each O_U(d) is also the closed sublocale of its clopen complement, and \(\bigcup_{d\ni p}(K\setminus d)=K\setminus\{p\}\).

Since an open sublocale U and its closed complement F have join X and meet zero, (6) forces \(T_p\le F\). Restricting (5) to F now yields
\[
T_p=T_p\wedge F
=\bigwedge_{d\ni p}O_F(d)=[p_F].
\tag{7}
\]
Hence every F-sheet point is fitted in X as well.

**Adversarial checkpoint:** Steps (6)–(7) deliberately use sublocale meets and the open/closed complement law. The mere topological intersection of the neighborhoods would have been insufficient.

## 6. A nonzero generalized specialization comparison

Let \(B=\operatorname{RO}(K)\), the complete Boolean frame of regular open subsets, and let
\[
j:\mathcal O(K)\twoheadrightarrow B,\qquad j(w)=\operatorname{int}\overline w
\tag{8}
\]
be the double-negation frame quotient. Compose the first and second coordinate projections \(L\to\mathcal O(K)\) with j, obtaining frame homomorphisms
\[
f^*,g^*:L\longrightarrow B,\qquad
f^*(c,v)=j(c),\quad g^*(c,v)=j(v).
\tag{9}
\]
For \((c,v)\in L\), the closed discrete defect \(c\setminus v\) has empty relative interior because K has no isolated points. Hence \(c\cap v\) is dense in c, giving \(c\subseteq\overline v\) and
\[
f^*(c,v)=j(c)\le j(v)=g^*(c,v).
\tag{10}
\]
These maps are **distinct**, since \(f^*(e)=0\) and \(g^*(e)=1\). Taking the nonzero locale with frame B as source, we have a genuine generalized comparable pair \(f<g:E\to X\). By the defining universal property of \(\mathcal A(X)\), it determines a map \(E\to\mathcal A(X)\) that cannot factor through the diagonal. Therefore \(\mathcal A(X)\ne\Delta_X\).

As B is atomless, its locale E is pointless; this explains how the generalized comparison escapes the ordinary \(T_1\) specialization order and how the zero-point-fiber obstruction arises.

## 7. Consequences / provisional status

The construction meets all four hypotheses of (LC-PT) in the ordinary sober-spatial \(T_1\) sense, while showing \(\mathcal A\ne\Delta\). Thus the proposed implication fails **if the checks above survive external audit**.

It also illustrates why the earlier Boolean lax double over a fixed quotient failed: the new filter-valued interface allows the exceptional defect to be *locally discrete* and hence produces compact-open neighborhoods, without making their intersections compact. Local compactness survives; stability does not.

**Suggested next actions:** (i) a truly independent adversarial read of §2 join closure, §4 compact opens, §5 fitted sublocales, and §6 quotient comparison; (ii) reconcile and update the (LC-PT) problem register only after passing that audit; (iii) ask whether weaker restrictions, such as a countable basis, restore a positive statement. The present compact-open basis is indexed by all points p∈K and need not be countable.

## 8. Further diagnostics: first countability, but not second countability

Because the Cantor space has a countable clopen local basis at each p, the \(b_{p,d}\) above form a **countable neighborhood basis at \(p_F\)**. Indeed, whether p lies in v or in the defect \(c\setminus v\), a sufficiently small clopen d makes \(b_{p,d}\le(c,v)\). The opens \((\varnothing,d)\) form a countable local basis at \(p_U\). Thus X is **first-countable**.

It cannot be second-countable. For each \(p\in K\), the open \(b_p=(K,K\setminus\{p\})\) contains \(p_F\) but not \(p_U\). Any global basis must contain some member \(B_p=(c_p,v_p)\) with \(p_F\in B_p\le b_p\), hence \(p\in c_p\setminus v_p\). But every relatively discrete subset of the second-countable Cantor space is countable, so the defect \(c\setminus v\) of **each** basic open is countable. A countable basis could account for only countably many such p, whereas K is uncountable.

The two copies \(p_F,p_U\) of any p cannot have disjoint open neighborhoods: for any \(p\in c\) and \(p\in v'\), the open set \(c\cap v'\) contains p and a nonempty neighborhood punctured at a relatively discrete defect \(c\setminus v\), so it meets v. Hence the space is non-Hausdorff in the ordinary sense too.

These extra diagnostics suggest a possible **second-countability** boundary for future study; they do not alter the (LC-PT) construction.

## 9. Exact maximal TU open locus and the zero-fiber witness

The open sheet \(U\cong K\) is TU, but **every nonempty open of X meeting the F-sheet is non-TU**. Indeed, let \(a=(c,v)\) be such an open; then c is nonempty. In the Boolean frame \(B=\operatorname{RO}(K)\), \(j(c)\ne0\). Restrict the generalized comparable pair \((f,g)\) of §6 to the nonzero open sublocale \(O_E(j(c))\). Because \(j(c)\le j(v)\), both f and g now factor through \(O_X(a)\); they remain distinct on the open e, whose pullbacks are 0 and 1. Thus \(O_X(a)\) is not TU.

Consequently, in the notation of the earlier [maximal-open-core reduction](ProjectA_LCPT_MAXIMAL_TU_OPEN_CORE_2026-11-15.md),
\[
U_{\rm TU}=U\cong K,\qquad F_{\rm TU}=F\cong K.
\tag{11}
\]
The closed non-TU core is therefore **entirely crowded** (Cantor), in exact agreement with the previous point-fitted perfect-core obstruction.

There is also a normalized zero-fiber witness for \(E_e(X)=\mathcal A(X)\wedge O(e_2)\wedge C(e_1)\), using the open e=(∅,K): on the source E, \(f^*(e)=0\), \(g^*(e)=1\), so the entire nonzero Boolean witness lands in \(E_e(X)\). Since every F-sheet point is fitted, the first-projection pullback of \(E_e\) over any ordinary point is zero by the [zero-fiber proposition](ProjectA_LCPT_ZERO_FIBER_OBSTRUCTION_2026-11-15.md). Thus this example realizes the earlier **nonzero generalized comparison with all ordinary fibers empty**.

Finally, since the ordinary specialization order of X is equality, \(\operatorname{pt}(\mathcal A(X))\) consists exactly of diagonal pairs; the nonzero off-diagonal Boolean witness forces \(\mathcal A(X)\) to be **nonspatial**.
