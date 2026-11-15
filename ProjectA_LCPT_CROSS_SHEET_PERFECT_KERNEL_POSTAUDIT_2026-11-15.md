# Project A — post-audit cross-sheet carrier and Cantor–Bendixson nucleus

**15 November 2026 · Referee's follow-up, internally rechecked at the level described below; NOT part of the independent blind audit.** Original [referee addendum](project-a/audits/2026-11-15/LCPT_DISCRETE_GLUE/Referee_addendum_original.md). Main [LC-PT canonical counterexample](ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md). No literature-priority claim.

## 1. Setup

Let \(K\) be Cantor space and
\[
L=\{(c,v)\in\mathcal O(K)^2:
c\setminus v\text{ closed discrete in }c\}.
\]
Write \(X\) for its locale, \(F=C_X(e)\cong K\) and \(U=O_X(e)\cong K\), where \(e=(\varnothing,K)\).

For the open complements of all ordinary points in K, define the sublocale
\[
P=\bigwedge_{p\in K}O_K(K\setminus\{p\}).
\tag{1}
\]
This meet is in the sublocale lattice. It has **no points**, but it is **nonzero** because the Booleanization \(B=\operatorname{RO}(K)\) lies in each punctured open, hence in P.

## 2. Exact cross-sheet comparison (internally checked)

**Proposition.**
\[
\boxed{\mathcal A(X)\wedge(F\times U)\cong P,}
\tag{2}
\]
where the embedding of P in \(F\times U\cong K\times K\) is the diagonal of its inclusion into K.

**Proof.** Consider generalized comparable maps \(f:E\to F\), \(g:E\to U\). Every \((c,c)\) is an X-open, hence the underlying two maps to K satisfy \(f_K\le g_K\). A Stone locale K is TU: on each clopen d, the inequality reverses on its clopen complement; clopens generate all opens. Therefore \(f_K=g_K=:h\).

For every p, the open \(b_p=(K,K\setminus\{p\})\) forces \(1=h^*(K)\le h^*(K\setminus\{p\})\), so h factors through P. Conversely, if h factors through P, fix an open (c,v) of X with relative discrete defect \(D=c\setminus v\). For each p∈D, choose an open \(d_p\subseteq c\) with \(d_p\cap D=\{p\}\). Then
\[
h^*(d_p)=h^*(d_p\setminus\{p\})\le h^*(v),
\]
because h factors through the punctured open \(K\setminus\{p\}\). Since
\(c=(c\cap v)\cup\bigcup_{p\in D}d_p\), it follows that \(h^*(c)\le h^*(v)\). By the universal property of \(\mathcal A\), this is exactly the cross-sheet condition. \(\square\)

The restrictions to \(F\times F\) and \(U\times U\) are diagonals; the restriction to \(U\times F\) is zero because \(e_1\le e_2\). Equation (2) is the *cross-sheet* statement and does not need a global decomposition claim.

## 3. Nucleus and the perfect kernel (internally checked for Cantor K)

The nucleus of the punctured open \(O_K(K\setminus\{p\})\) is
\[
n_p(w)=(K\setminus\{p\})\to w=\operatorname{int}(w\cup\{p\}).
\tag{3}
\]
An open w is fixed iff its closed complement \(K\setminus w\) has no isolated point at p. The join of these nuclei therefore has fixed opens exactly the complements of **perfect closed** subsets of K.

For a closed \(C\subseteq K\), let \(\operatorname{Perf}(C)\) denote its Cantor–Bendixson perfect kernel, the largest closed perfect subset of C (possibly empty). Then
\[
\boxed{j_P(w)=K\setminus\operatorname{Perf}(K\setminus w).}
\tag{4}
\]
To see that this is the least fixed open above w, equivalently seek the largest perfect closed subset of its closed complement. Cantor–Bendixson derivation stabilizes for compact metrizable K.

The inclusion \(B\subseteq P\) is **strict**: take a nonempty nowhere-dense closed perfect \(C\subsetneq K\), e.g. sequences with every even coordinate zero, and let \(w=K\setminus C\). Then \(j_P(w)=w\) but \(\neg\neg w=K\). Thus the Boolean generalized witness in the original packet is a proper part of the full cross relation. The locale P is non-Boolean as well: w is a nonzero proper fixed open whose only open disjoint from it is 0, hence has no Boolean complement.

## 4. The fitted hull of the closed sheet

An X-open \((c,v)\) contains all of F iff \(c=K\), in which case \(K\setminus v\) is finite. Thus the opens containing F are exactly \((K,K\setminus S)\) for finite S, and
\[
\operatorname{fit}_X(F)\wedge U
=\bigwedge_{\substack{S\subseteq K\\S\text{ finite}}}O_U(K\setminus S)
=\bigwedge_{p\in K}O_U(K\setminus\{p\})=P.
\tag{5}
\]
Combining (2) and (5):
\[
\boxed{\mathcal A(X)\wedge(F\times U)
\cong\operatorname{fit}_X(F)\wedge U.}
\tag{6}
\]
In particular \(F<\operatorname{fit}_X(F)\) although **every** point sublocale \([p_F]\) is fitted. This separates pointwise fittedness from fittedness of their join.

## 5. General obstruction (independently rechecked from the universal property)

**Proposition.** For any locale X, open U=O_X(e), closed complement F=C_X(e), and generalized comparable maps \(f:E\to F\), \(g:E\to U\) (as maps into X), the map g factors through \(\operatorname{fit}_X(F)\wedge U\). Thus
\[
\boxed{F\text{ fitted}\ \Longrightarrow\
\mathcal A(X)\wedge(F\times U)=0.}
\tag{7}
\]

**Proof.** If O_X(a) contains F, then \(f^*a=1\). Comparability forces \(g^*a=1\), so g lies in every open neighborhood of F, hence its fitted hull. It also lies in U. If F itself is fitted, that intersection is \(F\wedge U=0\). \(\square\)

This establishes a **necessary** condition for nonzero oriented cross-sheet comparison. Equality between the cross-sheet carrier and fitted-hull trace, as in (6), is *special* and is not asserted for arbitrary gluing.

## 6. Follow-up directions

1. Characterize open/closed gluing interfaces for which the general inclusion of §5 becomes an equality (after specifying a diagonal identification of both sides).
2. Investigate whether the Cantor–Bendixson nucleus admits a useful abstract description for other defect classes, without assuming metrizability where it is needed for simpler proofs.
3. Ask the **second-countable** version of (LC-PT). The counterexample already shows first countability, separability, and hereditary Lindelöfness do not suffice; no direction is established for second countability.
4. Keep (A-DUAL) in the unranked deferred pool.

**Provenance:** Sections 2–5 originated in the referee's *post-blind-review addendum* and were independently rechecked here, not sent back for a second blind audit. Treat as a separate mathematical stratum from the verified core counterexample.
