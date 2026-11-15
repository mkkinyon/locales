# Addendum to the independent blind referee report: the full cross-sheet specialization relation

**Date:** 15 November 2026  
**Companion report:** `LCPT_discrete_glue_blind_referee_report_2026-11-15.md`  
**Status:** Mathematical observations made *after* completing the independent blind audit. They strengthen the analysis of the example, but were not part of the original packet or its blind verification.

## 1. Summary

The Booleanization \(B=\operatorname{RO}(K)\) used in the packet is only a **proper sublocale of the complete cross-sheet specialization witness**. That witness is the sublocale
\[
P=\bigwedge_{p\in K}O_K(K\setminus\{p\}),
\tag{A1}
\]
whose nucleus is determined by the *Cantor–Bendixson perfect kernel*. Moreover, \(P\) is exactly the open-sheet trace of the fitted hull of the closed sheet. This yields a conceptual link between oriented specialization and fitted hulls.

We use the notation of the packet: \(X\) has frame
\[
L=\{(c,v)\in\mathcal O(K)^2:c\setminus v\text{ is relatively closed discrete in }c\},
\]
with closed sheet \(F=C_X(e)\cong K\), open sheet \(U=O_X(e)\cong K\), and \(e=(\varnothing,K)\). We write \(\mathcal A(X)\) for the oriented specialization sublocale.

## 2. Exact identification of the cross-sheet component

**Proposition A.** The pullback of \(\mathcal A(X)\) to \(F\times U\) is the diagonal copy of \(P\) in the two copies of \(K\):
\[
\boxed{\mathcal A(X)\wedge(F\times U)\cong P.}
\tag{A2}
\]

**Proof.** Let \(E\) be any locale, and let \(f:E\to F\), \(g:E\to U\) be comparable when regarded as maps into \(X\). Every \((c,c)\) with \(c\in\mathcal O(K)\) belongs to \(L\), so the underlying maps \(E\to K\) are comparable. Since Stone spaces are TU (clopen complements reverse the inequality, and clopens generate the frame), these maps are equal; denote the common map by \(h:E\to K\).

For every \(p\in K\), the pair \(b_p=(K,K\setminus\{p\})\) belongs to \(L\). Comparability therefore yields
\[
1=f^*(b_p)\le g^*(b_p)=h^*(K\setminus\{p\}),
\]
so \(h^*(K\setminus\{p\})=1\) for every \(p\). Equivalently, \(h\) factors through each \(O_K(K\setminus\{p\})\), hence through their meet \(P\).

Conversely, suppose \(h:E\to K\) factors through \(P\). Given \((c,v)\in L\), put \(D=c\setminus v\). For each \(p\in D\), choose an open neighborhood \(d_p\subseteq c\) such that \(d_p\cap D=\{p\}\). Then \(d_p\setminus\{p\}\subseteq v\), and
\[
h^*(d_p)=h^*(d_p)\wedge h^*(K\setminus\{p\})
=h^*(d_p\setminus\{p\})\le h^*(v).
\]
As \(c=(c\cap v)\cup\bigcup_{p\in D}d_p\), preservation of arbitrary joins gives \(h^*(c)\le h^*(v)\). The two composites \(E\xrightarrow h K\cong F\hookrightarrow X\) and \(E\xrightarrow h K\cong U\hookrightarrow X\) are therefore comparable. The two implications characterize the pullback by its universal property. \(\square\)

The other sheetwise restrictions are straightforward:

| First sheet | Second sheet | Restriction of \(\mathcal A(X)\) |
|---|---|---|
| \(F\) | \(F\) | The diagonal \(\Delta_K\) |
| \(U\) | \(U\) | The diagonal \(\Delta_K\) |
| \(U\) | \(F\) | Zero, because \(e_1\le e_2\) forbids \(1\le0\) |
| \(F\) | \(U\) | The diagonal copy of \(P\) |

These are *pullback restrictions*. No assertion is made here that their join reconstructs \(\mathcal A(X)\) globally.

Notice that \(P\) has no ordinary points: a point \(p\in K\) cannot factor through the open complement of itself. But \(P\ne0\), because the double-negation sublocale \(B\) factors through every punctured open \(K\setminus\{p\}\).

## 3. The Cantor–Bendixson nucleus

Let \(n_p\) be the nucleus of the open sublocale \(O_K(K\setminus\{p\})\). On \(\mathcal O(K)\),
\[
n_p(w)=(K\setminus\{p\})\to w
=\operatorname{int}(w\cup\{p\}).
\tag{A3}
\]
An open \(w\) is fixed by \(n_p\) precisely if \(p\) is not an isolated point of \(K\setminus w\). Since the nucleus \(j_P\) is the join of all \(n_p\), its fixed elements are exactly the opens whose closed complements have no isolated points.

For a closed set \(C\subseteq K\), let \(\operatorname{Perf}(C)\) denote its Cantor–Bendixson perfect kernel: the largest closed subset of \(C\) with no isolated points (possibly empty). The smallest fixed open above \(w\) is the complement of the largest perfect closed set contained in \(K\setminus w\). Therefore
\[
\boxed{j_P(w)=K\setminus\operatorname{Perf}(K\setminus w).}
\tag{A4}
\]
The complement/perfect-kernel description applies more generally whenever the relevant closed-set Cantor–Bendixson process stabilizes; in particular it applies to the compact metrizable Cantor space used here.

**Proposition B.** The original Booleanization witness is *properly* contained in \(P\):
\[
\boxed{B=\operatorname{RO}(K)\subsetneq P.}
\tag{A5}
\]

**Proof.** Containment follows from \(j_B(K\setminus\{p\})=1\) for every \(p\), since \(K\) has no isolated points. To prove strictness, choose a nonempty closed nowhere-dense perfect subset \(C\subsetneq K\) (for example, in \(2^{\mathbb N}\), fix every even-indexed coordinate at zero) and set \(w=K\setminus C\). The complement of \(w\) is already perfect, so (A4) gives \(j_P(w)=w\). However \(w\) is dense, hence its double-negation regularization is \(j_B(w)=\operatorname{int}\overline w=K\). Thus the two nuclei differ. \(\square\)

In particular, the Boolean source from the audit packet witnesses the nonzero cross-sheet relation but does **not** exhaust it. The full carrier \(P\) is non-Boolean and pointless.

## 4. Exact connection with the fitted hull of \(F\)

An open \((c,v)\in L\) contains the entire closed sublocale \(F\) exactly when \(c=K\). In that case \(K\setminus v\) is closed discrete in compact \(K\), hence finite. Thus all open neighborhoods of \(F\) are exactly
\[
(K,K\setminus S),\qquad S\subseteq K\text{ finite}.
\]
Taking their meet and restricting to the open sheet gives
\[
\begin{aligned}
\operatorname{fit}_X(F)\wedge U
&=\bigwedge_{S\subseteq K\text{ finite}}O_U(K\setminus S)\\
&=\bigwedge_{p\in K}O_U(K\setminus\{p\})\\
&=P.
\end{aligned}
\tag{A6}
\]
Combining (A2) and (A6), we obtain
\[
\boxed{\mathcal A(X)\wedge(F\times U)
\cong\operatorname{fit}_X(F)\wedge U.}
\tag{A7}
\]

This gives a precise explanation of the observation in the referee report that \(F\) is not fitted although all its individual points are fitted: the fitted hull of \(F\) has an entire nonzero pointless trace in \(U\), and that trace is exactly the carrier of cross-sheet specialization.

## 5. A general obstruction

**Proposition C.** Let \(X\) be any locale, \(U=O_X(e)\) an open sublocale and \(F=C_X(e)\) its closed complement. If \(f:E\to F\) and \(g:E\to U\) satisfy \(f\le g\) when regarded as maps into \(X\), then \(g\) factors through
\[
\operatorname{fit}_X(F)\wedge U.
\]
In particular,
\[
\boxed{F\text{ fitted}\quad\Longrightarrow\quad
\mathcal A(X)\wedge(F\times U)=0.}
\tag{A8}
\]

**Proof.** If an open sublocale \(O_X(a)\) contains \(F\), then \(f^*(a)=1\). Comparability implies \(1=f^*(a)\le g^*(a)\), so \(g\) factors through every open neighborhood of \(F\), and therefore through their sublocale meet \(\operatorname{fit}_X(F)\). Since \(g\) also factors through \(U\), it factors through the displayed intersection. If \(F\) is fitted, that intersection is \(F\wedge U=0\), forcing \(E=0\). \(\square\)

Thus nonfittedness of a closed stratum is **necessary** for a nonzero comparison from that stratum into its open complement. In the present example, (A7) is an exact identification of the resulting off-diagonal relation, not merely an obstruction.

## 6. Suggested next questions

1. Identify hypotheses on a more general open/closed gluing \(X=U\cup F\) under which the inclusion supplied by Proposition C becomes an equality, as it does in (A7).
2. Study the Cantor–Bendixson nucleus \(j_P\) as an object in its own right, including how its fixed-point frame compares with the double-negation quotient and whether analogous nuclei arise naturally for other defect classes.
3. Keep the second-countability boundary on the problem list, but treat it separately: the present construction is first-countable, separable, and hereditarily Lindelöf yet not second-countable. Nothing here proves either direction of the second-countable version of (LC-PT).

**Assessment.** These deductions do not change the positive audit verdict. They provide a sharper description of the counterexample and a new structural relation between oriented specialization and fittedness. As post-audit observations, they are suitable candidates for a separate adversarial check before being promoted to consolidated theorem status.
