# Project A — Compact three-boundary-point lower-diamond counterexample

**Date:** 24 October 2026  
**Status:** New working theorem, internally checked; not independently audited.

## Statement

For the standing project notation,
\(\mathcal W=\operatorname{cl}(\mathcal D)\),
\(\mathcal V=\operatorname{fit}(\mathcal I)\),
\(\mathcal J=\mathcal I\vee\mathcal D\),
\(\mathcal M=\mathcal I\wedge\mathcal D\), and
\(T(\mathcal J)=\mathcal W\wedge\mathcal V\).

There is a **countable, first-countable, compact, locally compact, sober, scattered, noncoherent** \(T_0\) space \(X\) such that, as localic sublocales,

\[
\boxed{\Delta\subsetneq\mathcal D=\mathcal M\subsetneq
\mathcal I=\mathcal J=\mathcal W=T(\mathcal J)
\subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F.}
\]

In particular, \(T(\mathcal J)\subsetneq \mathcal U\wedge\mathcal V\) is possible **even compactly** and when \(\mathcal U=\mathcal V=\mathcal F\).

## Construction

Let \(S_1,S_2\) be disjoint countably infinite discrete sets and adjoin \(p,x,y\). The basic neighborhoods at these three points are

\[
\begin{aligned}
N_p(E_1,E_2)&=\{p,x\}\cup(S_1\setminus E_1)\cup(S_2\setminus E_2),\\
N_x(E_1)&=\{x\}\cup(S_1\setminus E_1),\\
N_y(E_2)&=\{y\}\cup(S_2\setminus E_2),
\end{aligned}
\]
for finite sets \(E_i\subseteq S_i\). All points of the sheets are isolated. These neighborhoods generate a topology. The specialization order on the closed boundary \(B=\{p,x,y\}\) has just \(p<x\), with \(y\) incomparable with both.

Every isolated sheet singleton is clopen. The space is compact because a member of an open cover containing \(p\) covers \(x\) and all but finitely many sheet points; only \(y\) and finitely many isolated points remain. Each displayed basic neighborhood is compact by the same cofinite argument, so \(X\) is locally compact. It is first-countable and scattered. It is sober: an irreducible closed set meeting an isolated clopen singleton must equal that singleton; otherwise it lies in the finite sober Alexandrov boundary. It is noncoherent: two compact opens \(\{p,x\}\cup S_1\cup S_2\) and \(\{y\}\cup S_2\) intersect in infinite discrete, noncompact \(S_2\).

Because \(X\) is locally compact and sober, its **localic square is the ordinary topological product**. The finite product is scattered; by the Simmons scattered-sublocale theorem, every sublocale of the square is spatial and point-determined. This is why the point calculations below establish genuine localic equalities.

## The three relational levels

Distinct sheet points and all off-diagonal mixed sheet/boundary pairs are excluded from inseparability by a clopen singleton.

1. **Fitted diagonal.** For any topological space, the ordinary points of \(\mathcal D\) are the pairs with a common specialization predecessor. Here this gives the diagonal and precisely \((p,x),(x,p)\) off the diagonal.

2. **Closed inseparability.** \(p\) and \(x\) are inseparable by specialization; \(p\) and \(y\) are inseparable because every pair of their neighborhoods overlaps cofinitely in \(S_2\). But \(x,y\) have disjoint neighborhoods \(N_x(\varnothing)=\{x\}\cup S_1\) and \(N_y(\varnothing)=\{y\}\cup S_2\). Thus \(\mathcal I\) adds precisely \((p,y),(y,p)\) to \(\mathcal D\)'s point relation.

3. **Urysohn/fitted/functional relation.** Every neighborhood of \(x\) and every neighborhood of \(y\) has \(p\) in its closure, because every \(p\)-neighborhood has cofinite traces in both sheets. Therefore \((x,y),(y,x)\in\mathcal U\). They also belong to \(\mathcal V\), because \((p,y)\in\mathcal I\), \((p,y)\le(x,y)\) in the product specialization order, and fitted sublocales are upward saturated on ordinary points. Every continuous real-valued function satisfies \(f(p)=f(x)\) by specialization and \(f(p)=f(y)\) by inseparability. Clopen sheet singletons distinguish every other pair, so \(\mathcal F\)'s point relation has exactly one three-point block \(B^2\), plus diagonal sheet pairs. All sublocales of the square are spatial, hence \(\mathcal U=\mathcal V=\mathcal F\).

To show **\(\mathcal W=\mathcal I\)**, note universally \(\mathcal I\subseteq\mathcal W\). The rectangle \((\{x\}\cup S_1)\times(\{y\}\cup S_2)\) contains no point of \(\mathcal D\): no boundary pair inside has a common predecessor, no mixed pair does, and \(S_1\times S_2\) has no diagonal points. Since \(\mathcal D\) is spatial, this rectangle meets it in the zero sublocale. Hence it excludes \((x,y)\) from \(\operatorname{cl}(\mathcal D)\); its transpose excludes \((y,x)\). These are the only ordinary pairs outside \(\mathcal I\), so the closed sublocales \(\mathcal W\) and \(\mathcal I\) agree. Thus \(\mathcal D\subseteq\mathcal I\), \(\mathcal M=\mathcal D\), and \(\mathcal J=\mathcal I\). Finally, \(\mathcal H=\mathcal F\) since \(\mathcal V=\mathcal F\subseteq\mathcal H\subseteq\mathcal F\).

The inequalities \(\Delta\subsetneq\mathcal D\subsetneq\mathcal I\subsetneq\mathcal U\) are witnessed by \((p,x)\), \((p,y)\), and \((x,y)\), respectively.

The example is **not almost normal**: put \(A=\{x\}\cup S_1\), \(B_0=\{p,x\}\cup S_1\cup S_2\). Then \(\operatorname{cl}(A)=A\cup\{p\}\subseteq B_0\), so \(A\prec B_0\). Any open intermediate \(C\) containing \(\operatorname{cl}(A)\) must contain \(p\) and cofinally many \(S_2\) points, whence \(y\in\operatorname{cl}(C)\not\subseteq B_0\). Interpolation fails.

## Positive equality criteria beyond coherence

For arbitrary locales, \(\mathcal W\le\mathcal U\) and \(\mathcal D\le\mathcal V\) imply \(T(\mathcal J)=\mathcal W\wedge\mathcal V\le\mathcal U\wedge\mathcal V\).

- If \(\mathcal V\le\mathcal U\), equality holds iff \(\operatorname{cl}(\mathcal V)=\mathcal W\).
- If \(\mathcal U\le\mathcal V\), equality holds iff \(\mathcal U=\mathcal W\).
- If \(\mathcal I\) is fitted, then \(\mathcal V=\mathcal I\), and both sides equal \(\mathcal I\), independently of coherence.
- If \(X\) is sober and \(T_1\), the localic square is spatial, and \(\mathcal V\) is itself spatial, then \(\operatorname{pt}(\mathcal V)=\operatorname{pt}(\mathcal I)\) (exclude each external product point using the open complement of its singleton). Hence \(\mathcal V=\mathcal I\) and equality holds. In particular, this covers locally compact sober scattered \(T_1\) spaces. The hypothesis that \(\mathcal V\) is spatial is essential to the proof, not automatic from spatiality of the square.

**Unresolved refinements:** compact almost-normal locales; compact \(T_1\) locales with potentially nonspatial fitted residuals; more intrinsic criteria without comparability assumptions.

## Standard literature used

- Picado–Pultr, *Notes on the product of locales* (2015), Proposition 4.4.1: localic products of sober locally compact spaces agree with topological products.
- Ball–Picado–Pultr, *On an aspect of scatteredness in the point-free setting* (2016), Proposition 5.3; Suarez, *On the relation between subspaces and sublocales* (2022): scattered-space sublocale correspondence.

No novelty or publication-readiness claim. Independently audit the spatiality application and the common-predecessor formula before treating this as a refereed theorem.