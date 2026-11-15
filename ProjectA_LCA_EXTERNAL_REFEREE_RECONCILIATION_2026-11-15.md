# Project A — External blind referee reconciliation for negative (LC-A)

**15 November 2026.** The referee received the [blind packet](project-a/audits/2026-11-15/LCA/Blind_packet.md) and prompt, without the internal audit or access to the project history.

## Verdict and audit boundary

**Referee verdict: CORRECT, with no mathematical repairs.** The explicit X from K=[0,1] is compact, locally compact in the locale-theoretic sense, sober, T1 and non-stably locally compact; its \(\mathcal A(X)\) strictly contains the point-generated diagonal and is nonspatial. The referee checked lemmas 3.1–3.3, 4.1, 5.1–5.2, the alternate §6 witness, and §7's generalization to locally compact Hausdorff K **without isolated points**.

The positive (A-SC) theorem and other earlier examples were **not** in this packet, so this report gives no new verification of them. Priority was **not** investigated.

[Original blind referee report](project-a/audits/2026-11-15/LCA/Referee_report_original.md) · [original mathematical addendum](project-a/audits/2026-11-15/LCA/Referee_addendum_original.md) · [canonical theorem and short proof](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md).

## Referee's constructive improvements

1. **Short generalized-point proof.** Use the nonzero \(\beta_K\) and the pair \((p!,z):\beta_K\to X^2\). The cofinite opens ensure the pair satisfies all \(\mathcal A\)-inequalities; \(z^*K=1\ne0=(p!)^*K\) proves it does not factor through the diagonal. No fiber calculation is necessary for the theorem.
2. **Exact pointless fiber frame.** For \(E=\operatorname{fit}([p])\wedge O(K)\), the referee obtained \(\mathcal O(E)=\{V\subseteq K\text{ open}:K\setminus V\text{ has no isolated points}\}\), isomorphic to perfect subsets of K in opposite order. This separately verifies nonzero and pointless. The statement is in the original referee report; its use as a general scatteredness criterion is only a later sketch.
3. **Frame-level failure of stability.** \(a=K\setminus\{x\}\ll K,U_{\{x\}}\) but \(a\not\ll a\), giving failure of multiplicativity of \(\ll\) without relying on stable-compact convention.
4. **Editorial precision.** The two Booleanization routes use the same dense-open Boolean core; §6 is “independent of the fitted-fiber lemma,” not entirely independent. The diagonal need not be closed in X². The argument uses open/closed sublocales of spatial locales, never the false assertion that all sublocales of a spatial locale are spatial.

## Later addendum: relevant, but not part of the blind verdict

The referee identified \(\mathcal A(X)=\Delta_X\) with Isbell's **totally unordered** axiom \((T_U)\), noted Arrieta's \((T_U)\Rightarrow(pt\text{-}fit)\), recalled Johnstone's Hausdorff non-\((T_U)\) space (not locally compact), and explained that the first and second point fibers of \(\mathcal A\) are respectively the fitted point hull and point closure. This general fiber calculation is internally checked.

**Qualification to addendum §2:** “second-projection fibers are always spatial” must be read with the hypothesis that X is spatial. A closed sublocale of an *arbitrary* locale need not be spatial. It is safe for the topological spaces used here.

The referee also sketched (not blind-audited) a **scattered-K criterion** and a no-first-countability observation for the cofinite-point construction. We preserve these as potential follow-ups, not as parts of the externally established theorem.

## New questions and literature control

- (LC-PT): in locally compact sober T1, is \((pt\text{-}fit)\Rightarrow(T_U)\)?
- (A-DUAL): find a natural closure-side “dual” to \(\mathcal A\) in \([\Delta,\mathcal I]\) (not trivially resolved by transposition).
- (A-JOIN): **CLOSED (false)** after this audit, by an internally checked [four-point diamond counterexample](ProjectA_A_JOIN_DIAMOND_COUNTEREXAMPLE_2026-11-15.md).
- (COUNT-A): can a first- or second-countable locally compact sober T1 space fail \((T_U)\)?

See [follow-up and dual question ledger](ProjectA_LCA_FOLLOWUP_AND_A_DUAL_QUESTIONS_2026-11-15.md). No claim that the LC-A example is first in the literature; inspect Johnstone, Arrieta and further sources before asserting novelty.
