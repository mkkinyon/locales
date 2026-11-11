# CO-01: a canonical compact-remote equivalence relation bounding ALL localic powers of Arrieta A

**11 November 2026. New internally checked structural theorem, not a verdict on the associativity of \(A^3\) and not independently externally audited.** This uses [compact-local diagonal restriction](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md) and [regular-fit endpoint top classes](ProjectA_CO01_regular_fit_topclass_countable_endpoint_tests_2026-11-11.md). It gives an exact **diagonal + entirely noncompact residual** decomposition of every parenthesized power of A, plus a *maximal localic equivalence relation* containing them. Unlike earlier formal kernel rephrasings, the bound is intrinsic to the underlying regular Hausdorff locale V and requires no admissible-cover presentation.

## 0. The compact-remote sublocale

Let V be Arrieta's regular spatial (Tychonoff) \(C\setminus D\), where \(C=2^\mathbb N\), D is countable dense nonzero finite-support sequences. Every compact subset \(K\subseteq V\) is closed in C and in V. Define the fitted sublocale
\[
Z=\bigcap_{K\subseteq V\text{ compact}}\mathfrak o(V\setminus K)\ \subseteq V.
\tag{0.1}
\]
(Intersection means meet in the **sublocale lattice**, not a set-theoretic intersection of open subsets. The corresponding quotient of O(V) forces every open V\K to be top.) Its ordinary point set is empty, since each p∈V lies in the compact singleton {p}. It is **nonzero**: every compact K is nowhere dense in V, because V has no nonempty relatively compact open; consequently the dense double-negation sublocale \(V_{\neg\neg}\) factors through every \(\mathfrak o(V\setminus K)\) and thus through Z. The ordinary points are absent but Z contains a nonzero dense Boolean sublocale.

Write
\[
\mathscr R_\infty=\Delta_V\vee (Z\times Z)
\ \subseteq V^2.
\tag{0.2}
\]
The join is **the localic image of the coproduct map** \(\Delta_V\sqcup (Z\times Z)\to V^2\); it is not claimed to be an ordinary point-set union. Because the square V² is regular and hence fit, its sublocales are fitted and determined by top classes.

## 1. Complete Boolean locales detect inclusion of sublocales in a fit ambient locale

**Lemma 1 (Boolean probes).** Let X be a fit locale and S,T⊆X sublocales. Then
\[
S\le T\quad\Longleftrightarrow\quad
\text{every map }\operatorname{Loc}(B)\to S
\text{ from a nonzero complete Boolean frame B}
\text{ factors through }T.
\tag{1.1}
\]
**Proof.** The forward implication is automatic. If S⊄T, fittedness of T gives an open w∈O(X) with T⊆o(w) but S⊄o(w). Put a=w|_S∈O(S), so a<1. The **closed quotient** O(S)→↑a sending x↦x∨a is nontrivial, and its double-negation/Booleanization \(\nu:\uparrow a\to(\uparrow a)_{\neg\neg}=B\) is a frame map to a nontrivial complete Boolean frame, with a↦0 and 1↦1. The resulting map \(\operatorname{Loc}(B)\to S\) has pullback of w equal to 0, so cannot factor through o(w) and hence cannot factor through T. QED.

This is the formal reason the following decomposition may be proved by testing **all** Boolean locales B, not just the single B=RO(V) used in the earlier permutation work.

## 2. Exact noncompact/diagonal decomposition

Call a sublocale \(S\subseteq V^2\) **compact-locally diagonal** if \(\Delta_V\subseteq S\) and for every compact K⊂V,
\[
S\cap(K\times V)=\Delta_K=S\cap(V\times K)
\tag{2.1}
\]
as sublocales (where Δ_K is the graph K↪V).

**Theorem 2 (remote decomposition).** Every compact-locally diagonal S has
\[
\boxed{\qquad S=\Delta_V\vee(S\cap(Z\times Z)).\qquad}
\tag{2.2}
\]
In particular,
\[
\boxed{\qquad S\le\mathscr R_\infty=\Delta_V\vee(Z\times Z).\qquad}\tag{2.3}
\]

**Proof.** The \(\supseteq\) inclusion is immediate because Δ⊆S and \(S\cap Z²\subseteq S\).

For the converse, by Lemma 1 it suffices to show every Boolean-valued map \(t:T=\operatorname{Loc}(B)\to S\) factors through the join on the right. Let \(f,g:T\to V\) be its two endpoint maps. For each compact K⊂V define Boolean elements
\[
b^f_K=\neg f^*(V\setminus K),\quad b^g_K=\neg g^*(V\setminus K)\quad\in B.
\]
The pullback of the **closed** sublocale K along f (respectively g) is the clopen sublocale represented by \(b^f_K\) (respectively \(b^g_K\)); indeed a closed sublocale in a Boolean locale is clopen. Set
\[
c=\bigvee_{K\text{ compact}}(b^f_K\vee b^g_K)\in B.
\]

On each T_{b^f_K} the map t factors through S∩(K×V)=Δ_K, so f=g; similarly on each T_{b^g_K}. By distributivity in B, on the clopen piece T_c the two endpoint frame maps agree, hence t factors through Δ_V.

On the complementary clopen piece T_{¬c}, for every K both pullback opens f^*(V\K) and g^*(V\K) become top, hence f|_{T_{¬c}},g|_{T_{¬c}} factor through **every** open sublocale o(V\K), and therefore through their meet Z. The map t on that piece consequently factors through \(S\cap Z²\).

Because \(T\simeq T_c\sqcup T_{\neg c}\) (complementary clopen pieces), t factors through the coproduct \(\Delta_V\sqcup(S\cap Z²)\), hence through its image \(\Delta_V\vee(S\cap Z²)\). Lemma 1 completes the proof. QED.

**Warning:** Boolean probe conservativity does *not* mean that the **fixed** Boolean locale \(\operatorname{Loc}(\mathrm{RO}(V))\), or just its maps induced by Cantor selfmaps, suffices to detect all sublocale inclusions. The proof ranges over all nonzero complete Boolean frames and all maps.

## 3. Greatest compact-locally diagonal relation, and transitivity

**Lemma 3 (closed-base-change stability).** If e:T→S is locale-surjective and K↪X is a **closed sublocale**, pullbacks of e along K×X↪X² (where applicable) remain surjective. Consequently compact-local diagonal property (2.1) is preserved under:
- **binary localic composition** \(S\circ T\), where the image of the composable-pair locale is used; and
- **finite joins** of relations, because the join is the image of their disjoint coproduct, and this image remains surjective after the indicated closed base changes.

The composition proof is direct: on K×V the first relation forces the intermediate endpoint equal to the first and in K, and the second forces the final endpoint equal to it; this holds at the level of pulled-back localic sources and their image-surjections. For joins, each summand restricts to Δ_K and the pullback of the coproduct-to-join image-surjection is surjective by the same closed-base-change fact. No regularity or global image-stability is assumed.

Since Δ is compact-locally diagonal and Z∩K=0 for every compact K, both Δ and Z² are compact-locally diagonal **after taking their reflexive join**: the restriction of Δ∨Z² to K×V is Δ_K. Thus \(\mathscr R_\infty\) has property (2.1). Theorem 2 makes it the **greatest** compact-locally diagonal relation.

It follows that \(\mathscr R_\infty\circ\mathscr R_\infty\) is compact-locally diagonal, hence lies in \(\mathscr R_\infty\). Conversely, because Δ⊆\(\mathscr R_\infty\), unit and monotonicity give the reverse inclusion. Therefore
\[
\boxed{\quad
\mathscr R_\infty^2=\mathscr R_\infty,\qquad
\mathscr R_\infty^\smile=\mathscr R_\infty,\qquad
\Delta_V\subseteq\mathscr R_\infty.
\quad}\tag{3.1}
\]
So \(\mathscr R_\infty\) is an actual **internal localic equivalence relation** in the image-defined sense, despite the fact that Loc is not a regular category. Its construction is intrinsic to V (compact sets and the diagonal), not to Arrieta's extra sequence of K_n attachment data.

**Caution:** This proves that \(\mathscr R_\infty\) is transitive, *not* that A² or either cube is already \(\mathscr R_\infty\). In a nonregular category a transitive relation containing A need not make intermediate image composites associative by formal reassociation. All containment statements below use only monotonicity and the compact-local theorem.

## 4. Application to Arrieta A and CO-01

From the separately internally checked [compact restriction theorem](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md), **every nonempty parenthesized finite localic power** P(A) is compact-locally diagonal. Thus
\[
\boxed{\quad
P(A)=\Delta_V\vee(P(A)\cap(Z\times Z))
\ \le\ \mathscr R_\infty
\qquad\text{for every parenthesized finite word }P.
\quad}\tag{4.1}
\]
In particular,
\[
A\subsetneq A²\le (A²)A,\ A(A²)\le\mathscr R_\infty.
\]
The strict \(A\subsetneq A²\) follows from the prior Boolean triple nontransitivity witness. The two cubic relations agree on every compact endpoint and have the **same diagonal contribution**; any failure of associativity must occur **entirely in their Z² restrictions**:
\[
\boxed{\quad
(A²)A=A(A²)\iff
((A²)A)\cap Z²=(A(A²))\cap Z².
\quad}\tag{4.2}
\]
Thus CO-01 is reduced to a comparison **inside the compact-remote residual locale Z×Z**, rather than testing open neighborhoods of all V². This is a genuine *structural decomposition*, not merely the previous congruence test restated: it removes all compactly supported contributions categorically.

The new residual upper bound \(\mathscr R_\infty\) is a proper but dense localic equivalence relation with exactly diagonal ordinary point pairs. It is proper because any compact singleton first-coordinate restriction is diagonal, and it is dense because it contains the already dense A. Z has no ordinary points but contains the nonzero dense Booleanization of V (any compact K is nowhere dense). The open questions now naturally include:
- Is \(A²=\mathscr R_\infty\)? A positive answer would imply both cubic composites equal A², since A⊆R and R²=R; but **no equality is asserted**.
- More modestly, do the two cubic residual restrictions in (4.2) coincide? A separator must live in a *noncompact, nonspatial* sublocale of Z².
- Is the compact-remote relation \(\mathscr R_\infty\) effective as a kernel pair in Loc? (No implication from its transitivity alone; properness is not known.) This is a separate deferred question, not necessary for CO-01.

## 5. Generality and caveats

Theorem 2 and maximality/transitivity apply to any **regular spatial Hausdorff locale** V for which compact subspaces are closed; the residual Z may vanish if V is locally compact. The proof uses the fit ambient square (regular localic products) and Boolean-probe conservativity (Lemma 1). Its application to A uses the special compact restriction theorem derived from Θ-admissibility. Notation \(\mathscr R_\infty\) is **temporary research notation**, not a new entry in the earlier separation Hasse diagram.

**Status:** new structural theorem and exact CO-01 residual reduction, internally checked here. Independent adversarial audit is strongly recommended before using the Boolean-probe decomposition as a major theorem.
