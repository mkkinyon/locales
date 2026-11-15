# Project A — (LC-PT): a canonical zero-fiber generalized-comparability witness

**15 November 2026 · Internal deduction / proposed obstruction template, not externally audited.** The purpose is to make the remaining failure mode of (LC-PT) more algebraic and experimentally testable. Read together with the [maximal open TU locus](ProjectA_LCPT_MAXIMAL_TU_OPEN_CORE_2026-11-15.md) and [scattered closed-remainder theorem](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md).

## 1. The normalized difference pieces

Let \(X\) be any locale, \(\mathcal A(X)\subseteq X\times X\) its oriented specialization relation, and \(a_i=\pi_i^*a\) for \(a\in\mathcal O(X)\). Define the **unnamed normalized difference sublocale**
\[
E_a(X):=\mathcal A(X)\wedge O_{X^2}(a_2)\wedge C_{X^2}(a_1)
\ \hookrightarrow X^2.
\tag{1}
\]
No new calligraphic relation symbol is proposed.

**Lemma.**
\[
X\text{ is TU}\quad\Longleftrightarrow\quad E_a(X)=0
\quad\text{for every }a\in\mathcal O(X).
\tag{2}
\]

*Proof.* If \(\mathcal A=\Delta\), then \(a_1=a_2\) on \(\mathcal A\), so the open part \(a_2\) and closed complement of \(a_1\) cannot intersect. Conversely, if \(\mathcal A\ne\Delta\), its two projections give distinct comparable maps \(f\le g:\mathcal A\to X\). Some a satisfies \(f^*a<g^*a\). Since \(f^*a\le g^*a\), the locally closed part \(O(g^*a)\wedge C(f^*a)\) is nonzero and is exactly \(E_a\). \(\square\)

The key is that (1) imposes the **strong normal form** \(a_1=0\), \(a_2=1\) on E_a. Every nonzero restriction still witnesses inequality of the two projections.

## 2. All normalized obstructions are sourced from the non-TU core

Let \(U_{\mathrm{TU}}\) be the largest open TU sublocale of X, and \(F_{\mathrm{TU}}\) its closed complement, from [the maximal-core note](ProjectA_LCPT_MAXIMAL_TU_OPEN_CORE_2026-11-15.md).

**Proposition.** For each a, the first projection \(f_a:E_a\to X\) **factors through** \(F_{\mathrm{TU}}\).

*Proof.* On the open part of E_a where \(f_a\) lands in \(U_{\mathrm{TU}}\), comparability forces the second projection \(g_a\) to land there too. TU of \(U_{\mathrm{TU}}\) then gives \(f_a=g_a\) on that open part, contrary to \(a_1=0\), \(a_2=1\) unless the part is zero. Hence the pullback of the open \(U_{\mathrm{TU}}\) along f_a is 0, which is exactly factorization through the complementary closed sublocale. \(\square\)

If each point \(p\in F_{\mathrm{TU}}\) is fitted **in X**, then each ordinary fiber is actually zero:
\[
\boxed{E_a\times_{F_{\mathrm{TU}}}[p]=0
\qquad(p\in F_{\mathrm{TU}}).}\tag{3}
\]
Indeed, the first-projection fiber of \(\mathcal A(X)\) over p is \(\operatorname{fit}_X([p])=[p]\), so the two projections agree on that fiber. Their normalized difference has empty pullback.

Thus **a negative answer to (LC-PT)** would provide:

- a nonzero \(E_a\) for some a;
- a map \(E_a\to F_{\mathrm{TU}}\), where \(F_{\mathrm{TU}}\) is a nonempty closed subspace with **no isolated points**;
- **zero pullback fiber over every ordinary point** of \(F_{\mathrm{TU}}\);
- two distinct comparable maps \(E_a\to X\), forced apart by \(a\), despite all first-coordinate ordinary point fibers being trivial.

This is a concrete two-projection **zero-fiber witness** to test. It is stronger than saying merely that \(E_a\) has no ordinary points.

## 3. Why zero fibers alone cannot yield a positive theorem

A warning: there are **nonzero zero-fiber maps to perfectly regular locally compact spaces**. For example, let K be a nonempty compact Hausdorff space without isolated points (the Cantor space suffices). Its Booleanization \(B(K)\) has the complete Boolean frame of regular opens. This frame is atomless, hence has no points; nevertheless \(B(K)\) is a nonzero locale. The canonical sublocale inclusion \(B(K)\to K\) therefore has zero pullback over every point \(p\in K\): such a fiber is a sublocale of the one-point locale \([p]\), so if nonzero would provide a point of \(B(K)\).

Consequently neither spatiality nor local compactness of **the target alone** rules out (3). A proof of (LC-PT) must use the specific **oriented-specialization structure** of \(E_a\), not just the existence of a fiberwise-empty map.

This example is a formal calibration, not a candidate counterexample to (LC-PT): K itself is Hausdorff and TU.

## 4. Current status and possible tests

The open problem is still
\[
\text{locally compact + sober + }T_1+\text{all points fitted}
\stackrel?{\Longrightarrow}\mathcal A(X)=\Delta_X.
\]
The non-TU core and (1)–(3) reduce construction to a relatively controlled shape without settling existence. Possible next experiments:

1. Examine whether local compactness constrains \(E_a\) more strongly than it constrains arbitrary sublocales such as \(B(K)\), through compact saturated neighborhoods or way-below opens.
2. If constructing a counterexample, force the whole obstruction into a **closed crowded** locus; any model with scattered remainder is excluded.
3. Try a finite-/countable-base restriction where a zero-fiber witness from \(\mathcal A\) might be impossible, keeping separate any independent countability assertion.

**Provenance:** \(\mathcal A\) is the existing oriented specialization relation, while \(\mathcal S=\mathcal A\vee\mathcal A^{op}\) is an established *different*, symmetric relation; see [notation guide](ProjectA_LOWER_HIERARCHY_NOTATION_2026-11-15.md). No new relation in the global hierarchy is introduced here.
