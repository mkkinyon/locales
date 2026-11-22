# Project A — MAT*/MUL* arbitrary-parameter blind referee reconciliation
## Session 11 · 21 November 2026

### Submitted material and original reports

- [Original independent blind report — unchanged](project-a/audits/2026-11-21/MATSTAR_MULSTAR/INDEPENDENT_REFEREE_REPORT.md)
- [Original additional mathematical addendum — unchanged](project-a/audits/2026-11-21/MATSTAR_MULSTAR/REFEREE_ADDENDUM.md)
- [Original audit README](project-a/audits/2026-11-21/MATSTAR_MULSTAR/README.md)
- [Candidate proof (historical proposal)](ProjectA_OPUS_SCATTERED_ARBITRARY_PARAMETER_EXTENSION_2026-11-21.md)
- [Post-referee canonical proof and corollaries](ProjectA_MATSTAR_MULSTAR_POSTREFEREE_CANONICAL_2026-11-21.md)

The user sent the packet to a **fresh ChatGPT session outside the project**, distinct from Claude Opus 5.5, which first proposed the extension. The new referee examined only the six neutral blind-packet files, explicitly excluding previous referee assessments. This is an independent **model-generated mathematical referee check**, not a formal proof certificate or human peer review.

### Exact adjudication

| Item | Result | Scope |
|---|---|---|
| MAT* | **E — accepted**, modest exposition repairs | Arbitrary locale \(P\), locally compact scattered Hausdorff \(K\), complete lattice of **all** sublocales of \(P\times K\). Includes nonspatial/nonregular/empty \(P\). |
| MUL* | **E — accepted** | All genuine binary localic relations on \(P\times K\), image of already-formed composability locale; does **not** imply global associativity. |
| FINMAT* | **E — accepted** | Associative unital converse-closed algebra of row-and-column-finite matrices over a coefficient algebra with associative actual localic composition, finite-join and converse closure. |
| Finite-join distributivity of genuine localic relation composition | **General categorical fact**, not a new conjecture | Follows from pullback preserving finite joins, finite lattice distributivity, and image preserving joins. Can be dropped as a separate algebra hypothesis. |
| General finite-join product with \(Z\) | **Settled positive by same general categorical fact** | \((S\vee T)\times Z=(S\times Z)\vee(T\times Z)\) for all locales \(Y,Z\) and sublocales \(S,T\le Y\). **Not** arbitrary infinite joins. |

No fatal gap, hidden topological requirement on \(P\), or counterexample was reported.

**Proof clarifications integrated in canonical note:** (a) the precise open-cover localization argument in the interval \(\operatorname{Sub}(W)\); (b) finite closed/open decomposition, including infinite joins only against a complemented sector; (c) successor Cantor–Bendixson height and finite last derivative in compact scattered \(K\); (d) the compact clopen neighborhoods from one-point compactification of locally compact \(K\); (e) the image–pullback adjunction and the commuting sector projection identity \(\pi_{13}e_{ijk}=d_{ik}\pi_{13}^P\); (f) support-finiteness proof and \(n=0\) path convention. None alters the main statement.

### Post-report addendum (distinguish status from the candidate)

**New referee-origin, internally checked corollaries; not part of blind submitted MAT*/MUL* proof packet:**

1. **Subspace heredity.** All subspaces \(B\subseteq K\) of an admissible locally compact scattered Hausdorff index inherit the same sublocale-lattice product formula, even if \(B\) is not locally compact. Use the sublocale embedding \(B\hookrightarrow K\), its pullback along the parameter projection, and the order interval in MAT* coordinates; check finite localic powers before extending MUL*.
2. **Indexed functorial formulas.** For product maps \(F=f\times h\), pullback is coefficientwise \((F^{-1}W)_{k'}=f^{-1}(W_{h(k')})\); image groups fibres \((F_!V)_k=\bigvee_{h(k')=k}f_!(V_{k'})\). The latter is an adjunction consequence, not Beck–Chevalley for arbitrary images.
3. **Finite-sector joint truncation.** For any two relations \(R,S\), \(R\circ S=\bigvee_{F\Subset K}((R|_F)\circ(S|_F))\). This is specific to coordinated finite sector cutdowns and does not prove arbitrary directed-join continuity of composition.
4. **Row-/column-finite separate lifts.** Each is associative and unital under the coefficient hypotheses; converse interchanges them, while row **and** column finiteness ensures converse closure.

The referee additionally notes a separate sufficient index class of scattered Hausdorff spaces of **finite Cantor–Bendixson height** without local compactness, using isolated-stratum / derivative induction. This was not part of the original candidate, and is not here asserted for every scattered Hausdorff space.

### One previously open question is now closed: finite joins and products

The earlier Opus addendum and the then-current [Start Here](ProjectA_ENDGAME_START_HERE_2026-11-21.md) incorrectly left unrestricted
\[
(S\vee T)\times Z\stackrel{?}{=}(S\times Z)\vee(T\times Z)
\]
undecided. This identity is **generally true**, because \(S\times Z=\pi_Y^{-1}(S)\) in Loc and \(f^{-1}\) is a coframe homomorphism. For a published statement of that standard fact see Arrieta–Suárez, *The coframe of D-sublocales of a locale and the \(T_D\) duality*, §2, https://www.mat.uc.pt/preprints/ps/p2034.pdf . Preserve the old historical uncertainty as chronology but add an explicit superseding notice; any previous *restricted* proofs remain valid, only the declared limit was overly cautious.

### Mathematical significance and remaining limits

- Relative scattered-index atomicity is a **sublocale-lattice phenomenon**, not a locale coproduct isomorphism or a claim that the index topology is irrelevant to open/closed conditions.
- These are genuinely localic relations: nonspatial sector coefficients and nonspatial ambient sublocales are included.
- Unlimited index joins in MUL* do not grant associativity of arbitrary matrices; finite matrix-support remains a convenient **sufficient** safeguard.
- The generic TWIST extrapolation is still not certified, and the product-spatiality/Telgársky–Plewe comparison remains a separate research/literature task.
- Historical originality of the arbitrary-parameter theorem is not determined. Picado–Pultr's Simmons \(T_D\) theorem supplies the \(P=1\) antecedent, and a full published-product literature check has not yet been done.

### Archive housekeeping

This document supersedes statements describing MAT*/MUL* as merely "I pending external audit" in the Start Here guide, current ledger, and open-frontier notes. The original Claude proposal and both independent referee originals are retained unchanged; the new canonical theorem note incorporates exposition repairs and labels the post-report additions separately.
