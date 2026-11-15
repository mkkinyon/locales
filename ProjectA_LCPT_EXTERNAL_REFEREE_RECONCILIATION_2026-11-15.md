# Project A — (LC-PT) independent referee reconciliation (15 November 2026)

**Status:** The discrete-defect counterexample to (LC-PT) has passed both the [formal internal adversarial audit](ProjectA_LCPT_DISCRETE_GLUE_INTERNAL_ADVERSARIAL_AUDIT_2026-11-15.md) and a **genuinely blind independent external audit**, with a positive correctness verdict and **no mathematical repairs required**. This is a correctness claim, **not** a literature-novelty or priority claim.

Primary canonical construction: [discrete-defect gluing counterexample](ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md).
Original materials: [blind prompt](project-a/audits/2026-11-15/LCPT_DISCRETE_GLUE/Blind_prompt.md), [blind packet](project-a/audits/2026-11-15/LCPT_DISCRETE_GLUE/Blind_packet.md), [original referee report](project-a/audits/2026-11-15/LCPT_DISCRETE_GLUE/Referee_report_original.md), [post-audit follow-up addendum](project-a/audits/2026-11-15/LCPT_DISCRETE_GLUE/Referee_addendum_original.md).

## 1. Verified theorem

Let \(K\) be the Cantor space and let
\[
L=\{(c,v)\in\mathcal O(K)^2:c\setminus v
\text{ is closed discrete relative to }c\}.
\]
For its locale \(X\), the independent referee confirms:
- \(L\) is a frame; \(X\) is **compact, locally compact, spatial/sober, and \(T_1\)**.
- Every ordinary point sublocale is **fitted**.
- \(L\) has a compact-open basis but its compact opens are **not meet-stable**, so \(X\) is not stably locally compact.
- The distinct generalized points \(f,g:E\to X\), with \(\mathcal O(E)=\operatorname{RO}(K)\), have
  \(f^*(c,v)=\neg\neg c\le\neg\neg v=g^*(c,v)\), and hence \(\mathcal A(X)\ne\Delta_X\).
- \(X\) is **first-countable but not second-countable**, non-Hausdorff; \(\mathcal A(X)\) is nonspatial; its maximal open TU part is exactly its open Cantor sheet.

Thus the question (LC-PT) has the **negative** answer
\[
\boxed{
\text{compact + locally compact + sober + }T_1
+\text{ all points fitted}\ \not\!\!\Longrightarrow\
\mathcal A(X)=\Delta_X.}
\]

This is stronger than the separately blind-refereed negative (LC-A), whose previous locally compact example failed point-fittedness. It does not conflict with the separately blind-refereed *positive* (A-SC): stable local compactness implies spatiality of \(\mathcal A\).

## 2. The single expository repair

The referee recommends inserting this short lemma in the fitted-point calculation:

**Open/closed-complement lemma.** If \(S\hookrightarrow X\) is any sublocale, \(U=O_X(e)\), and \(F=C_X(e)\), then
\[
S\wedge U=0\quad\Rightarrow\quad S\le F.
\]
Indeed, for the quotient \(q:\mathcal O(X)\twoheadrightarrow\mathcal O(S)\), the intersection \(S\wedge U\) is the open sublocale \(O_S(q(e))\). It vanishes iff \(q(e)=0\), which is precisely factorization of \(S\) through \(C_X(e)\).

This proof directly uses the quotient, avoiding any dependence on how one presents the sublocale lattice. Our earlier argument using the complement law was sound under the standard coframe distributivity of sublocales, but the referee's lemma is a safer and clearer presentation. No theorem statement changes.

The referee also encourages explaining that the two comparable maps are the **same Booleanization generalized point** of \(K\), inserted into the closed and open sheets respectively.

## 3. Additional consequences of the original blind report

These were not claims from the original blind packet, and have been checked separately against the given construction:

1. **The closed sheet \(F\) is not fitted**, although every point \([p_F]\) is fitted. An open containing all of F is exactly \((K,K\setminus S)\) with S finite. The nonzero Booleanization sublocale of the open sheet lies in every such open, yet is disjoint from F. In particular, the join of these fitted point sublocales need not be fitted.
2. **U is dense**, because a nonzero open \((c,\varnothing)\) would require a nonempty open discrete subspace \(c\) of perfect K. Hence X is separable.
3. X is **hereditarily Lindelöf** as a topological space: each of its two sheets is second-countable, and each subset is the union of its intersections with the sheets.
4. The construction and main negative answer work over any nonempty **perfect Stone space** K; metrizability is used only for the first-countability assertion.

## 4. Post-audit addendum: separate verification status

After completing its independent blind review, the referee derived a stronger description of the entire cross-sheet relation, identifying its carrier with a Cantor–Bendixson quotient P and the open-sheet trace of \(\operatorname{fit}_X(F)\); and gave a general necessary condition from fitted closed strata. These are **post-audit suggestions, not part of the original independent blind verdict**.

Our separate internal check found the core universal-property calculation convincing; it is recorded with full hypotheses and caveats in [the post-audit cross-sheet note](ProjectA_LCPT_CROSS_SHEET_PERFECT_KERNEL_POSTAUDIT_2026-11-15.md). Do not silently upgrade its stronger assertions to blind-refereed status.

## 5. Reprioritization

**Settled (subject to literature check):** (LC-PT) negative by the above counterexample. The earlier maximal-TU/open-core and zero-fiber reductions remain valid and are *realized* by this example.

**Promising next problems:** (i) second-countable (LC-PT), now that first countability, separability, and hereditary Lindelöfness are insufficient; (ii) characterize when a cross-sheet specialization relation is exactly the trace of the fitted hull of the closed sheet, as in the example; (iii) study the Cantor–Bendixson nucleus if it proves to be a useful reusable localic construction.

**Deferred:** the previously recorded (A-DUAL), whose priority should be ranked against these and older Project A questions rather than assumed high.

No complete literature-priority assessment has been performed.
