# Independent blind referee prompt — Project A, Question (A-SC)

**15 November 2026**

Please read the accompanying packet **before** looking at other Project A notes, previous reports, or the repository. This is intended to be an independent, adversarial mathematical review. The packet includes all definitions and arguments needed to assess its principal claim.

## Assignment

The packet proposes a positive solution to Question **(A-SC)**:

> For every **stably locally compact locale** (X), the canonical specialization-order sublocale (mathcal A(X)\hookrightarrow X\times X) is spatial and equals the point-generated sublocale ([G_{\le_X}]).

The claimed proof reduces first to coherent locales via an **actual locale retraction** of a stably compact locale from an ideal completion, and then removes compactness by adjoining a new top element to the frame.

Your principal task is to determine whether the theorem and its proof are correct. Treat **every mathematical assertion in the packet as in scope**, including standard-sounding lemmas, parenthetical remarks, the coherent base case, and the description of the point-generated sublocale. Please do not take the author's confidence in the proof as evidence.

## Questions to prioritize

1. **Universal property and functoriality.** Does the sublocale presented by (u_1\le u_2) for every open (u) actually define a covariant functor (mathcal A:\mathbf{Loc}\to\mathbf{Loc}) on *arbitrary* locale maps? Is there any hidden problem in restricting (f\times f) or showing that identities and compositions are preserved?
2. **Ideal completion.** For a compact stably continuous frame (L), check from first principles that
   \[
   \sigma:\operatorname{Idl}(L)\to L,\quad I\mapsto\bigvee I,
   \qquad
   \iota:L\to\operatorname{Idl}(L),\quad u\mapsto\{v:v\ll u\}
   \]
   are *frame* homomorphisms and (\sigma\iota=1_L). Scrutinize arbitrary joins, the nullary meet (top), and the direction of the retraction under frame–locale duality.
3. **Coherent base case.** Does the bounded-distributive-lattice presentation of (mathcal A(Y)) imply that it is a coherent, hence classically spatial, locale? Verify that all inequalities on arbitrary opens follow from the compact-open inequalities.
4. **Noncompact extension.** Does (L^{\top}), obtained by adjoining a fresh top, really have a compact stably continuous frame structure for any stably continuous (L)? Is (X) an **open** sublocale of (X_\bot), and is
   \[
   \mathcal A(U)\cong U^2\times_{Y^2}\mathcal A(Y)
   \]
   correct for every open sublocale (U\hookrightarrow Y)?
5. **Spatial conclusion.** Is every locale retract of a spatial locale spatial? Does spatiality of the specialization sublocale actually imply equality with the point-generated sublocale ([G_{\le_X}]) *as a sublocale*, rather than merely coincidence of point sets?

Please look especially for a mistake that would invalidate the argument despite the correctness of the standard spectral-retraction theorem. If you find a failure, supply a counterexample or a precise diagnosis. If it is correct, say whether the proof admits a shorter or more transparent formulation.

## Report requested

- A clear verdict: **correct / correct with repair / incomplete / false**.
- Any major and minor issues, with precise references to the packet's numbered sections.
- Presentation problems and misleading phrases encountered on first reading.
- Suggested simplifications, conceptual generalizations, and worthwhile follow-up questions (if any).

**Independence protocol:** This is a blind packet. No internal audit accompanies it. Please finish your independent report before consulting earlier Project A reports or asking to see the internal analysis.

