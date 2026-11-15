# Project A — Post-(LC-A) questions and the interval below M

**Research questions and lower-hierarchy cross-reference · 15 November 2026; provenance corrected.** This document records the user's distinct deferred question about a conceptual **dual** to \(\mathcal A\). Its lower-hierarchy placement restates established work on \(\mathcal S=\mathcal A\vee\mathcal A^{op}\) from [the 10 November Cameron–Kumar revisit](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md) and the [independently refereed SC+ theorem](ProjectA_SCplus_CANONICAL_2026-11-15.md), rather than introducing a new join. The additional meet identity \(\mathcal A\wedge\mathcal A^{op}=\Delta\) is internally checked here.

## 1. The location of oriented specialization

For any locale X, set \(\mathcal I=\operatorname{cl}(\Delta)\), \(\mathcal D=\operatorname{fit}(\Delta)\), \(\mathcal M=\mathcal I\wedge\mathcal D\), and let \(\mathcal A\) be universally presented by \(u_1\le u_2\). **The pre-existing symmetric relation** is \(\mathcal S:=\mathcal A\vee\mathcal A^{op}\); earlier notes also write \(\mathcal B:=\mathcal A^{op}\). Thus \(\Delta\le\mathcal A,\mathcal A^{op}\le\mathcal S\le\mathcal M\).

**Proposition (all locales).**
\[
\Delta\subseteq\mathcal A,\mathcal A^{op}\subseteq\mathcal M,\qquad
\mathcal A\wedge\mathcal A^{op}=\Delta,
\]
and
\[
\operatorname{cl}(\mathcal A)=\operatorname{cl}(\mathcal A^{op})=\mathcal I,
\qquad
\operatorname{fit}(\mathcal A)=\operatorname{fit}(\mathcal A^{op})=\mathcal D.
\]

*Proof.* Reflexivity gives \(\Delta\le\mathcal A\). For the closure inclusion, write \(d_{\mathcal I}=\bigvee_{u\wedge v=0}(u_1\wedge v_2)\), the largest product open missing \(\Delta\), so \(\mathcal I=C(d_{\mathcal I})\). On \(\mathcal A\), \(u_1\wedge v_2\le u_2\wedge v_2=0\) for each disjoint u,v. Thus \(\mathcal A\le\mathcal I\).

For the fitted inclusion, take any open \(W\in\mathcal O(X^2)\) such that \(\Delta\le O(W)\), write \(W=\bigvee_i u_{i,1}\wedge v_{i,2}\), and note \(\bigvee_i(u_i\wedge v_i)=1\). In \(\mathcal O(\mathcal A)\), because \(v_{i,1}\le v_{i,2}\),
\[
1=\bigvee_i(u_{i,1}\wedge v_{i,1})
 \le \bigvee_i(u_{i,1}\wedge v_{i,2})=W|_{\mathcal A}.
\]
Hence \(\mathcal A\le O(W)\) for every open neighborhood of \(\Delta\), i.e. \(\mathcal A\le\mathcal D\). Coordinate transposition fixes \(\Delta,\mathcal I,\mathcal D\) and yields the same inclusions for \(\mathcal A^{op}\).

A generalized pair in both oriented relations has frame maps \(f^*\le g^*\) and \(g^*\le f^*\), hence \(f^*=g^*\) and factors through \(\Delta\). This proves the meet identity. Finally, monotonicity and idempotence of closure/fitting, together with \(\Delta\le\mathcal A,\mathcal A^{op}\le\mathcal I\wedge\mathcal D\), force the displayed hull equalities. \(\square\)

These inclusions can be strict: on the two-point Sierpiński locale, \(\mathcal A\) is the three-point specialization-order graph while \(\mathcal I=\mathcal D=\mathcal M=X^2\).

## 2. Open question A-DUAL — a conceptual dual below I

**User's original question:** Is there a *corresponding natural “dual” relation* between \(\Delta\) and \(\mathcal I\), in analogy with the construction of \(\mathcal A\) between \(\Delta\) and \(\mathcal D\)?

The inclusion \(\mathcal A\le\mathcal I\) shows that the **same** \(\mathcal A\) already lies in both intervals; \(\mathcal A^{op}\) is another natural oriented relation in both. Nevertheless, transposition is not, by itself, a *duality between the closure and fitted-hull mechanisms*. The intended conceptual question therefore remains **OPEN / deferred**.

Possible future tests (no assertions): look for a universal construction emphasizing closure rather than fitting; use the two projections' asymmetric fibers (fitted point hull versus point closure); examine Hochster/co-Hochster duality, specialization versus co-specialization, and the interaction with symmetric reflexive relations in the original graph project. Any proposed candidate must be defined as an actual sublocale, tested on nonspatial examples, and compared with \(\mathcal A\) and \(\mathcal A^{op}\), not only on ordinary points.

## 3. Established SC+ obstruction, rechecked (not a new question)

The identity \(\mathcal S(X)=\mathcal M(X)\) **fails**, already for the finite four-point Alexandrov diamond \(P=\{0,a,b,1\}\) with \(0<a,b<1\) and \(a,b\) incomparable.

Because \((0,0)\in\Delta_P\) is the least and \((1,1)\in\Delta_P\) the greatest point of \(P^2\), the fitted hull and closure of the diagonal are both \(P^2\). Hence \(\mathcal M(P)=P^2\). But the points of \(\mathcal A(P)\vee\mathcal A(P)^{op}\) are just comparable pairs, so \((a,b)\) is missing. Thus the containment from §1 is strict.

[Short independent recalculation](ProjectA_A_JOIN_DIAMOND_COUNTEREXAMPLE_2026-11-15.md). This obstruction was **already recorded on 10 November and incorporated in the externally audited SC+ theorem**. The label '(A-JOIN)' had mistakenly suggested a newly posed and solved question; it is retained only as a historical cross-reference.

## 4. Open question LC-PT — the next substantive frontier

For a locally compact sober T1 space X, does
\[
(pt\text{-}fit)\quad\Longrightarrow\quad(T_U),
\]
where \((pt\text{-}fit)\) means all point sublocales are fitted and \((T_U)\) means \(\mathcal A(X)=\Delta_X\)?

The converse \((T_U)\Rightarrow(pt\text{-}fit)\) is Arrieta's Proposition 3.10. The cofinite-point example fails both, so does not separate these conditions. A useful local obstruction is the first-projection fiber \(\operatorname{fit}([p])\); whether its being [p] for all p is sufficient in the locally compact sober T1 class is unknown.

A further question, suggested by the external referee: can a **first-countable or second-countable** locally compact sober T1 example fail \((T_U)\)? The cofinite-point model cannot be first-countable when its Hausdorff base K is non-scattered (conditional on the referee's unreviewed scatteredness extension).

## 5. Order of work and status

1. Archive/consolidate the blindly verified (LC-A) counterexample, with the short proof and the \((T_U)\) identification.
2. Check the literature (Johnstone, Arrieta, Isbell, Banaschewski, Picado–Pultr), especially priority and existing implications \((pt\text{-}fit)\leftrightarrow(T_U)\). A [preliminary primary-source checkpoint](ProjectA_TU_PTFIT_LITERATURE_CHECK_2026-11-15.md) is now recorded, without a priority claim.
3. Return to (LC-PT), now with an [internally checked scattered closed-remainder reduction](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md); leave A-DUAL open/deferred. The diamond obstruction \(\mathcal S\ne\mathcal M\) is established SC+ background.

The hull inclusions for \(\mathcal S\) are **established, previously recorded** and the SC+ statement is independently audited; the additional meet identity in §1 is internally checked. The open questions are not covert theorem claims.
