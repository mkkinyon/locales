# Project A — Lower hierarchy notation and provenance (15 November 2026)

**Navigation note, not a new theorem.** This resolves a notational collision that emerged while discussing (LC-A) and (LC-PT). The notation and principal relations below were introduced **before** the LC-A follow-up, principally in the [10 November Cameron–Kumar graph revisit](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md) and established further in the [independently audited SC+ theorem](ProjectA_SCplus_CANONICAL_2026-11-15.md).

For every locale \(X\), all relations are sublocales of \(X\times X\). Write \(a_i=\pi_i^*(a)\).

| Symbol | Meaning | Status / warning |
|---|---|---|
| \(\Delta\) | diagonal | universal minimum of the reflexive relations |
| \(\mathcal A\) | **oriented specialization**: largest sublocale satisfying \(a_1\le a_2\) for all \(a\in\mathcal O(X)\) | generally **not symmetric**; \(X\) totally unordered (TU) iff \(\mathcal A=\Delta\) |
| \(\mathcal A^{op}=\mathcal A^\smile\) | coordinate transpose, satisfying \(a_2\le a_1\) | older notes also call this \(\mathcal B\); use \(\mathcal A^{op}\) in LC-PT discussion |
| **\(\mathcal S\)** | **\(\mathcal A\vee\mathcal A^{op}\)**, the symmetric specialization relation | **existing symbol**, not a new \(\mathcal A\)-join construction; point graph is the Cameron–Kumar specialization-comparability graph |
| \(\mathcal I\) | \(\operatorname{cl}(\Delta)\) | also \(\operatorname{cl}(\mathcal S)\) |
| \(\mathcal D\) | \(\operatorname{fit}(\Delta)\) | also \(\operatorname{fit}(\mathcal S)\) |
| \(\mathcal M\) | \(\mathcal I\wedge\mathcal D\) | **upper bound** for \(\mathcal S\), not generally equal to it |
| \(\mathcal J\) | \(\mathcal I\vee\mathcal D\) | distinct from \(\mathcal M\); coherent-composition calculus gives \(\mathcal S^2=\mathcal J\) |

The guaranteed lower-hierarchy inclusions and meet are
\[
\boxed{\Delta\le\mathcal A,\mathcal A^{op}
\le\mathcal S=\mathcal A\vee\mathcal A^{op}
\le\mathcal M=\mathcal I\wedge\mathcal D,}
\qquad
\boxed{\mathcal A\wedge\mathcal A^{op}=\Delta.}
\]
The relation \(\mathcal S\) is symmetric, unlike the two oriented components. The meet identity was explicitly rechecked in the [post-LC-A follow-up](ProjectA_LCA_FOLLOWUP_AND_A_DUAL_QUESTIONS_2026-11-15.md).

**Strictness and equality.** On the four-element Alexandrov diamond \(0<a,b<1\), \(\mathcal S\subsetneq\mathcal M=X^2\). This was recorded in the 10 November note, **not** newly discovered as "(A-JOIN)" on 15 November. In the **stably locally compact** class, the externally audited SC+ theorem says \(\mathcal S=\mathcal M\) precisely when each specialization interval is a chain. The converse generally fails for compact locally compact sober **nonstable** examples, as the same SC+ canonical note explains.

**Coherent composition only.** In the coherent category, with the precisely specified composition from the canonical calculus,
\[
\mathcal S^2=\mathcal J,\qquad
\mathcal S^4=\mathcal U\vee\mathcal V.
\]
Do not extend these identities or assume associativity/distributivity for arbitrary localic relations without checking the respective hypotheses.

**Separate questions.**

- **(LC-PT), active:** Does point-fittedness of all ordinary points imply TU in locally compact sober \(T_1\) spaces? The [closed-point/scattered-remainder reduction](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md) is internally checked but not externally audited.
- **(A-DUAL), deferred:** Find a *conceptually closure-side* natural relation between \(\Delta\) and \(\mathcal I\), if there is one. Neither transposing \(\mathcal A\) nor renaming \(\mathcal S\) resolves the intended question.

For provenance and full proofs, consult [10 November graph revisit](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md), [SC+ canonical](ProjectA_SCplus_CANONICAL_2026-11-15.md), [LC-A follow-up](ProjectA_LCA_FOLLOWUP_AND_A_DUAL_QUESTIONS_2026-11-15.md), and [LC-PT excision](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md).
