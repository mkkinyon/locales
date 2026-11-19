# Independent blind referee prompt

You are asked to referee a mathematical claim in pointfree topology. Treat all material as **unverified**, including introductory descriptions that refer to earlier results. Your objective is to determine whether each asserted theorem follows from the stated hypotheses.

## The problem

Let (q:X\to Q) be a locale map with kernel pair (K=X\times_QX), and let (H\le K) be a reflexive localic relation. Fix a point (p:1\to Q), its localic fibre (G=X\times_Q1), the generic square (B=G\times G\le X^2), and the generic trace (D=H\wedge B). Under special compact-cutoff conditions, the packet claims that generic restriction of relations **commutes with image-defined relational composition** throughout the interval ([H,K]):

\[
(R\circ_XS)\wedge B=(R\wedge B)\circ_G(S\wedge B)
\quad(H\le R,S\le K).
\]

The principal application sets (R=S=H) and asserts that the canonical base change

\[
e_\infty:D\times_GD\longrightarrow (H\circ_XH)\wedge B
\]

of the surjective localic image-factor map (H\times_XH\twoheadrightarrow H\circ_XH) is **surjective**. General localic surjections do *not* remain surjective under arbitrary pullback. The packet purports to establish this particular instance directly from finite-cutoff rigidity.

## Instructions

1. **Audit the abstract theorem independently.** Verify every use of coframe distributivity, inverse images of sublocales, localic images, kernel-pair pullbacks and reflexive unit laws. Especially check the genuine pullback identity for the generic-middle summand and the claimed image of the finite-cutoff summands.
2. **Audit the application to the base-changed surjection.** Check that the fibre of the composability locale is exactly (D\times_GD), that the fibre of the image locale is exactly (A=(H\circ_XH)\wedge B), and that equality of localic images establishes a surjection of locales. Do not substitute set-theoretic point arguments for localic arguments.
3. **Audit the interval correspondence and its consequences.** Check the isomorphism ([H,K]\cong[D,B]), preservation of composition and converse, fixed-bracket iterates, and the formula for equivalence hulls. Do not assume associativity of localic composition.
4. **Check the hypotheses supplied by the finite-fence model** using the included foundations appendix. If an input is correct only under a stronger condition than stated, identify the missing condition precisely. A fully independent re-derivation of the long coordinate construction is not required; check how its listed properties are used.
5. **Try to break the argument.** A counterexample, a type mismatch, or an unjustified distributive step would be particularly informative. For an invalid statement, identify the earliest failure and, if possible, the strongest valid replacement.
6. **Evaluate presentation.** Record any notation ambiguity, unspoken hypothesis, unclear universal property, or point at which the proof is difficult to follow on first reading. Suggestions for shorter or more conceptual proofs are welcome.

## Reporting format

Please provide:

- A one-paragraph verdict: **correct**, **correct conditional on specified repairs**, **incomplete**, or **false**.
- Numbered findings separating fatal defects, repairable gaps, and minor expository issues.
- A dependency table stating exactly which inputs you checked and which you treated as hypotheses.
- Any useful generalization or counterexample you encountered, clearly marked as additional rather than part of the verification.

Please assess *all* displayed formulas, including the aside about equivalence hulls. Do not consult an internal audit or earlier referee findings until your independent report is complete.
