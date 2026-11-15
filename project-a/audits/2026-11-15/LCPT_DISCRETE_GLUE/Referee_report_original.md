# Independent blind referee report — Project A (LC-PT), discrete-defect gluing

**Date:** 15 November 2026  
**Materials:** `Blind_prompt.md` and `Blind_packet.md`, from `LCPT_discrete_glue_blind_audit_2026-11-15.zip`.  
**Scope:** Independent mathematical review of the supplied packet. I did not consult the internal audit, repository synthesis, or earlier reports.

## 1. Verdict

**The central counterexample is correct.** I find no broken step in the construction or its proof. The frame exists; its point space is compact, locally compact, sober, and \(T_1\); every point sublocale is fitted; and the two coordinate maps into the double-negation frame furnish *distinct, comparable locale maps*. Consequently \(\mathcal A(X)\ne\Delta_X\), and (LC-PT) has the proposed negative answer.

I also confirm the optional claims about the compact-open basis, failure of meet-stability, first countability, failure of second countability, ordinary non-Hausdorffness, the maximal TU open locus, and the zero-fiber witness. The claimed nonspatiality of \(\mathcal A(X)\) follows as stated. The independently established positive theorem (A-SC) was not part of this audit; the example's failure of stability is, however, explicit and sufficient to remove any apparent conflict.

**No mathematical repair is needed.** The most important editorial repair is to spell out the sublocale lemma used in §5. The assertion is true, but an argument based merely on a complementary pair's join and meet would be unreliable in a nondistributive sublocale lattice. I give the correct reason below.

## 2. The pair frame and the point space

Let \(D(c,v)=c\setminus v\). Because \(c\) and \(v\) are open, \(D(c,v)\) is closed in \(c\). Thus the condition is exactly that \(D(c,v)\) be *relatively discrete* in \(c\).

For a coordinatewise join \((c,v)=(\bigcup c_i,\bigcup v_i)\), take \(p\in D(c,v)\) and choose \(i\) with \(p\in c_i\). Necessarily \(p\notin v_i\), and
\[
D(c,v)\cap c_i\subseteq D(c_i,v_i).
\]
An open neighborhood of \(p\) in \(c_i\) isolating it in the right-hand set therefore isolates it in the left-hand set. The defect of the join is relatively discrete. For a binary meet, the displayed formula in §2 expresses its defect as a union of two subsets that are closed discrete in the common open domain. A finite union of closed discrete subsets is closed discrete: at a point belonging to just one component, exclude the other closed component; at a point belonging to both, intersect isolating neighborhoods. Thus arbitrary joins and finite meets are inherited from \(\mathcal O(K)^2\), and \(L\) is a frame.

The two projections are frame maps \(L\to\mathcal O(K)\). The open sublocale associated with \(e=(\varnothing,K)\) has frame \(\{(\varnothing,v):v\in\mathcal O(K)\}\), and its closed complement has frame \(\{(c,K):c\in\mathcal O(K)\}\). These identify with \(K_U\) and \(K_F\). Any point evaluates \(e\) at 0 or 1 and factors through the corresponding piece, so **there are exactly two copies of the points of \(K\)**. Their evaluations separate all pairs \((c,v)\). Hence the point space is spatial and sober.

The opens \((K\setminus\{p\},K)\) and \((K,K\setminus\{p\})\) have complements in the point space \(\{p_F\}\) and \(\{p_U\}\), respectively. Both belong to \(L\), so \(X\) is \(T_1\).

## 3. Compactness and local compactness

The compactness argument in §4 is valid. Given a cover of \((K,K)\), compactness of the first copy of \(K\) supplies finitely many first coordinates covering \(K\). For their finite union \((K,v_*)\), the residual defect \(K\setminus v_*\) is closed discrete **in compact \(K\)**, hence finite. A finite number of further opens from the original cover covers those residual second-coordinate points.

Likewise, if \(d\) is clopen and \(S=\varnothing\) or \(\{p\}\), a cover of \((d,d\setminus S)\) has a finite subfamily whose first coordinates cover \(d\). The part of \(d\) omitted by their combined second coordinate is finite, and only finitely many of these omitted points lie outside \(S\) and require supplementary opens. This proves compactness of the proposed second and third basic types. Compactness of \((\varnothing,d)\) is inherited from the open copy of \(K\).

The basis argument is also correct. For an \(F\)-point in the defect \(c\setminus v\), relative discreteness and zero-dimensionality yield a clopen \(d\ni p\) with \(d\subseteq c\) and \(d\cap(c\setminus v)=\{p\}\). Then \((d,d\setminus\{p\})\le(c,v)\). The other point cases are immediate. Every frame element is therefore a join of compact elements, so \(L\) is algebraic, in particular continuous and locally compact.

Indeed, the compactness assertion extends from \(S=\varnothing,\{p\}\) to **any finite \(S\subseteq d\)**: every \((d,d\setminus S)\) is compact.

Both \(e=(\varnothing,K)\) and \(b_p=(K,K\setminus\{p\})\) are compact, while their meet \((\varnothing,K\setminus\{p\})\) is noncompact: on the open sheet it is the noncompact open \(K\setminus\{p\}\). This demonstrates failure of meet-stability, including the stability condition for the way-below relation (which would make the meet of two compact elements compact).

## 4. Fittedness: the critical localic step

Here is the lemma that makes the sublocale argument safe.

**Open/closed-complement lemma.** Let \(S\hookrightarrow X\) be any sublocale and \(U=O_X(e)\), \(F=C_X(e)\). If \(S\wedge U=0\), then \(S\le F\).

**Proof.** Let \(q:\mathcal O(X)\twoheadrightarrow\mathcal O(S)\) denote the quotient frame map. The pullback of \(U\) to \(S\) is the open sublocale \(O_S(q(e))\). This is zero precisely when \(q(e)=0\) in \(\mathcal O(S)\). The latter equality is precisely the condition for \(S\to X\) to factor through the closed complement \(C_X(e)\). \(\square\)

This establishes the implication used in the packet without assuming distributivity of the sublocale lattice.

For a point \(p\in K\), let \(d\) run over its clopen neighborhoods. In the sublocale lattice of \(K\),
\[
\bigwedge_{d\ni p}O_K(d)
=\bigwedge_{d\ni p}C_K(K\setminus d)
=C_K\!\left(\bigcup_{d\ni p}(K\setminus d)\right)
=[p].
\]
Consequently,
\[
\bigwedge_{d\ni p}O_K(d\setminus\{p\})
=[p]\wedge O_K(K\setminus\{p\})=0.
\]
Both are **sublocale identities**, not merely set-theoretic intersections.

The opens \((\varnothing,d)\) show directly that \(p_U\) is fitted. For \(p_F\), put
\[
T_p=\bigwedge_{d\ni p}O_X(d,d\setminus\{p\}).
\]
Restricting to \(U\) and using the second identity yields \(T_p\wedge U=0\). The lemma gives \(T_p\le F\). Restricting instead to \(F\) and using the first identity then gives
\[
T_p=T_p\wedge F=\bigwedge_{d\ni p}O_F(d)=[p_F].
\]
Since the displayed opens are all neighborhoods of \(p_F\), and the meet of **all** neighborhoods is squeezed between \([p_F]\) and their meet \(T_p\), this proves fittedness in the stipulated sense. The generalized-map check in §5 expresses the same argument and is valid.

This is the decisive part of the audit: **the packet correctly handles the potentially nonspatial intersection.**

## 5. The generalized specialization comparison

The double-negation operator \(j(w)=\operatorname{int}\overline w\) is a nucleus on \(\mathcal O(K)\). As a map to its fixed-point frame \(B=\operatorname{RO}(K)\), it preserves finite meets and arbitrary joins; the latter are regularized unions in \(B\). Therefore both
\[
f^*(c,v)=j(c),\qquad g^*(c,v)=j(v)
\]
are frame homomorphisms.

A relatively closed discrete subset of a nonempty open subset of perfect \(K\) has empty interior there. Hence \(c\setminus v\) is nowhere dense in \(c\), so \(c\subseteq\overline v\) and \(j(c)\le j(v)\). Thus \(f\le g\). They are distinct because their values on \(e\) are 0 and 1. The frame \(B\) is nontrivial, so this is a genuine nonzero source locale, and it proves \(\mathcal A(X)\ne\Delta_X\).

The source is indeed pointless. \(B\) is a complete atomless Boolean algebra: a nonzero regular open contains two disjoint nonzero regular opens. A completely prime filter of a complete Boolean algebra is generated by an atom, so \(B\) has no frame maps to \(2\).

An especially transparent reformulation is to let \(\beta:E\hookrightarrow K\) be the Booleanization sublocale map associated with \(j\). Then \(f\) and \(g\) are simply the composites of \(\beta\) with the two sheet inclusions \(K_F\to X\) and \(K_U\to X\). The inequality says that these two copies of the *same pointless generalized point* are comparable, although no distinct ordinary points are.

## 6. Optional refinements

All survive the audit:

1. **First countability.** A countable clopen local basis \(d_n\) at \(p\) gives \((\varnothing,d_n)\) at \(p_U\) and \((d_n,d_n\setminus\{p\})\) at \(p_F\). The latter refines any neighborhood of \(p_F\), whether \(p\in v\) or \(p\in c\setminus v\).
2. **Not second-countable.** An open in a countable basis has at most countably many defect points, since a discrete subspace of second-countable \(K\) is countable. Yet each \(p_F\) needs a basis element lying below \((K,K\setminus\{p\})\), necessarily with \(p\) in its defect. A countable basis cannot account for uncountably many \(p\).
3. **Not Hausdorff.** Every neighborhood of \(p_F\) meets every neighborhood of \(p_U\): the second coordinate of the former is dense in its first coordinate, and the latter has a second-coordinate neighborhood of \(p\).
4. **Maximal TU open.** The open sheet \(U\cong K\) is TU (already clear from its clopen basis). If \(a=(c,v)\) meets \(F\), then \(c\ne\varnothing\) and \(j(c)\ne0\). Restrict \(E\) to \(O_E(j(c))\). Both \(f\) and \(g\) factor through \(O_X(a)\) but stay distinct, as witnessed by \(e\). Thus no such open is TU, and \(U_{\rm TU}=U\) with closed complement \(F_{\rm TU}=F\), under the packet's conventions.
5. **Zero ordinary fibers.** The claimed zero-fiber result can be checked directly without invoking the previous proposition. For the Booleanization map \(\beta:E\to K\), its pullback over any point \(p\in K\) is zero: \(K\setminus\{p\}\) has pullback 1 along \(\beta\), since \(j(K\setminus\{p\})=1\), but pullback 0 along the point \(p\). Their fiber product forces \(1=0\). The whole \(E\) witness also satisfies \(f^*(e)=0\), \(g^*(e)=1\), so lands in the designated \(E_e(X)\).
6. **Nonspatial \(\mathcal A(X)\).** Its ordinary points are exactly the diagonal pairs, because \(X\) is \(T_1\). A spatial sublocale of \(X^2\) is determined by its induced point subspace, so if \(\mathcal A(X)\) were spatial it would equal the spatial diagonal \(\Delta_X\), contradicting the nonzero generalized witness.

## 7. Further observations

### 7.1. The closed sheet is *not* fitted, though every one of its points is

This is a potentially useful strengthening of the conceptual picture. An open \((c,v)\) contains the **whole closed sublocale** \(F\) if and only if \(c=K\). Its defect \(K\setminus v\) is then a closed discrete subset of compact \(K\), hence a **finite** set \(S\). Thus the opens containing \(F\) are precisely
\[
(K,K\setminus S),\qquad S\subseteq K\text{ finite}.
\]
The Booleanization sublocale \(E\hookrightarrow U\hookrightarrow X\) lies in every such open, since \(j(K\setminus S)=1\) for every finite \(S\). It is nonzero and lies entirely in \(U\), so it cannot lie in \(F\), which is disjoint from \(U\). Therefore
\[
F\ <\ \operatorname{fit}(F).
\]
This does **not** conflict with §5: the fittedness of *each individual point* \([p_F]\) uses the much more restrictive clopen neighborhoods around that point. It also shows that the join of this family of fitted point sublocales, namely the spatial closed sheet \(F\), need not be fitted.

### 7.2. Further countability properties

The open sheet \(U\) is dense: if \((c,v)\wedge e=0\), then \(v=\varnothing\), and a nonempty open \(c\) in perfect \(K\) cannot be discrete in itself; hence \(c=\varnothing\). Therefore a countable dense subset of \(U\cong K\) is dense in all of \(X\), so **\(X\) is separable**.

Moreover, \(X\) is **hereditarily Lindelöf as a point space**. Any subset \(A\subseteq X\) is the union of its intersections with \(U\) and \(F\), each a subspace of second-countable \(K\) and hence Lindelöf. Every open cover of \(A\) has countable subcovers on each piece. Thus separability and even hereditary Lindelöfness, together with first countability, do not rescue (LC-PT). The suggested possible second-countability boundary remains meaningful.

### 7.3. Scope of the construction

Nothing in the central argument depends on the specific middle-thirds Cantor set. It works for any **nonempty perfect Stone space** \(K\) (compact, Hausdorff, zero-dimensional, with no isolated points). Metrizability/countable local bases are needed only for the first-countability refinement, not for the negative answer itself.

## 8. Presentation recommendations

1. Insert the open/closed-complement lemma from §4 above before (6)–(7). State explicitly that the proof is *not* an application of distributivity of the sublocale lattice.
2. In the compactness proof, emphasize that the residual defect is finite because it is **closed discrete inside a compact clopen set**; relative discreteness alone does not make arbitrary residual defects finite.
3. After the displayed comparison, explain explicitly that \(f\) factors through \(F\) and \(g\) through \(U\), and both come from Booleanization of the same \(K\). This makes the geometry of the generalized comparison much easier to see.
4. Consider giving the direct one-line zero-fiber computation in §6 above rather than relying exclusively on an external proposition.
5. If the point-fitted-versus-closed-sheet-fitted distinction is germane to the project, add §7.1 to the synthesis. Otherwise it can remain a separate observation; it is not required for the main counterexample.

**Final assessment:** I recommend accepting the central result and its stated optional refinements, subject only to these expository clarifications. This is an independent positive audit, not a claim of literature novelty or priority.
