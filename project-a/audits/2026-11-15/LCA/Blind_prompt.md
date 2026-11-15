# Independent blind referee prompt — Project A, Question (LC-A)

**15 November 2026**

Please read the accompanying mathematical packet **without first consulting** our internal audit, earlier discussion, or the Project A repository. The packet is meant to stand alone. We are asking for an independent, adversarial examination of a proposed **negative** solution to Question (LC-A).

## The claim under review

For a locale \(X\), let \(\mathcal A(X)\hookrightarrow X\times X\) be the actual sublocale universally imposing \(u_1\leq u_2\) for every \(u\in\mathcal O(X)\), where \(u_i=\pi_i^*u\). The question was whether \(\mathcal A(X)\) must be spatial whenever \(X\) is locally compact and sober.

The packet proposes a counterexample: attach a point \(p\) to \(K=[0,1]\), giving \(p\) the cofinite neighborhood basis \(U_F=\{p\}\cup(K\setminus F)\) for finite \(F\subseteq K\), while retaining the usual opens of \(K\). It claims that the resulting \(X\) is **compact, locally compact, sober, \(T_1\)**, but \(\mathcal A(X)\) is **not spatial**. In particular, its ordinary specialization graph is only the diagonal, while the localic relation is strictly larger.

This claim would separate mere local compactness from the previously established positive result for **stably** locally compact locales. Please do not take that background result or the proposed proof's apparent simplicity as evidence for the new claim.

## Priority checks

1. **Topology and separation.** Is the specified family really a topology? Is the space compact, locally compact in the sense corresponding to a continuous frame (not just weakly locally compact), \(T_1\), and sober? Check the irreducible-closed-set proof carefully.
2. **Failure of stability.** Are the exhibited compact saturated subsets genuinely compact and saturated in this non-Hausdorff space? Is their intersection noncompact? Does this prove failure of stable local compactness under the intended conventions?
3. **Fitted fiber.** Is the fiber of the first projection \(\mathcal A(X)\to X\) over \(p\) canonically the fitted hull \(\operatorname{fit}_X([p])=\bigwedge_{p\in U}O_X(U)\)? Verify the universal property at the level of arbitrary test locales, not only ordinary points.
4. **Booleanization.** Does the nonzero double-negation (Booleanization) sublocale \(\beta_X\) lie inside *every* dense open sublocale? Check the nucleus-order direction, the claim that \(K\) and all \(U_F\) are dense, and the assertion that \(\beta_X\) is nonzero.
5. **From the fiber to nonspatiality.** Is the fiber over \(p\) a **closed** sublocale of \(\mathcal A(X)\), and is its intersection with the open second-coordinate copy of \(K\) a **nonzero, pointless, locally closed** sublocale? Are closed and open sublocales of a spatial locale necessarily spatial? Distinguish these facts from the *false* assertion that every sublocale of a spatial locale is spatial.
6. **Independent witness.** Check the alternative construction using \(\beta_K\to\{p\}\times K\). Does it land in \(\mathcal A(X)\), and does it establish nonzeroness of the specific locally closed piece rather than merely producing an arbitrary nonspatial sublocale?
7. **Scope of the conclusion.** If the proof is correct, does \(\mathcal A(X)\neq\Delta_X=[G_{\le_X}]\) follow as an equality/inequality of *sublocales*, not merely from point-set considerations? Check the proposed generalization to locally compact Hausdorff \(K\) without isolated points separately.

Please look actively for a counterexample to a lemma, a reversed order convention, a silently invalid pullback or sublocale inference, or a distinction between topological and localic local compactness. **Every mathematical assertion is in scope**, including explanatory remarks and optional generalizations.

## Requested report

- Verdict: **correct / correct after repair / incomplete / false**.
- Major issues first, with exact section and equation references; minor issues and presentation surprises separately.
- If a step fails, provide the smallest decisive counterexample or a rigorous explanation of the gap.
- If correct, suggest any simplification, stronger statement, or useful next question, clearly distinguished from the audited theorem.
- No need to invent improvements or a headline result; a clean confirmation is useful.

**Blind-review protocol:** The enclosed zip contains only this prompt and the mathematical packet. It does **not** contain our internal adversarial audit or earlier referee reports. Please finish the independent report before requesting those materials.
