# Independent referee prompt — CO-01: does Arrieta's fitted diagonal stabilize at its square?

Please read [the self-contained theorem/proof packet](ProjectA_CO01_Arrieta_square_saturates_remote_equivalence_PROOF_2026-11-11.md) **independently and adversarially**. This is newly proposed mathematics, **not independently checked outside the authors' own working sessions**. The theorem purports to prove a strong positive answer to the remaining associativity question for the specific Arrieta 2024 strongly Hausdorff noncoherent locale, namely
\[
A^2=\Delta_V\vee(Z\times Z),
\quad A^2\circ A=A\circ A^2=A^2,
\]
where A is the nontrivial V² block of its fitted diagonal and Z is the intersection of open complements of all compact subspaces of V.

**Read in this order:**
1. The published Arrieta 2024 construction, specifically Construction 4.2 and Example 4.5, to verify that the precise K_n and the Θ-admissible open-cover presentation are correct (original primary PDF: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf).
2. [Localic explicit Θ-cover and block computation](A-relational-composition-associativity-audit-VI-Arrieta-explicit-covers-2026-11-07.md), particularly §§2–7. Treat it as **an unproved assertion requiring audit**, not as a premise to accept blindly.
3. [Compact-local diagonal calculation](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md), independently checking its use of closed-base-change.
4. [General remote maximal relation proof](ProjectA_closed_family_remote_equivalence_general_theorem_2026-11-11.md), focusing on Boolean-probe conservativity, decomposition, the join of Δ and Z², and associativity-free transitivity.
5. [New saturation proof](ProjectA_CO01_Arrieta_square_saturates_remote_equivalence_PROOF_2026-11-11.md) without granting its conclusions.

**The critical proof tests are:**
- Is the full pullback of the intersection of *all* Θ-admissible-cover open sublocales exactly the intersection of their pulled-back opens? Give the relevant direct image/pullback adjunction rather than assuming it.
- For an arbitrary **complete** Boolean frame B and map \(f:\operatorname{Loc}(B)\to Z\), does the associated \(\operatorname{Ult}(B)\to C\) actually meet \(K_n\) for unbounded n on **every nonempty clopen component**? Check both the density-of-D and absence-of-interior-in-singleton-D-fibres arguments.
- Does every Θ-admissible cover force its pullback square-open \(w_\mathcal C=\bigvee_a f^*a\boxtimes a\) to be dense in the **localic** product \(\operatorname{Loc}(B)\times V\)? Check use of ordinary V-points only for nonzero rectangles, and the K_n-prefix property.
- Does Booleanization \(N=(\operatorname{Loc}(B)\times V)_{\neg\neg}\) lie in the two separate pullbacks of A? Is the composite \(N\to\operatorname{Loc}(B)\) a genuine locale-surjection, **not merely a dense map**? Verify injectivity of the inverse-image frame map.
- Does the surjective **new generic-middle cover** \(N\to T\) prove the endpoint map \(T\to V²\) factors through the image sublocale \(A²\), without assuming all surjections are pullback-stable?
- Do complete Boolean locales jointly detect arbitrary sublocale inclusion? Check the closed-quotient followed by double-negation construction, including which element is separated.
- Is the compact-local diagonal theorem strong enough to prove \(A²\le\Delta\vee Z²\), and does its proof use genuine (rather than false) surjection stability under **closed** inclusions?
- Does the reduction from the V×V block to the full fitted diagonal \(\mathcal D_Y\) survive nonclopen V/N decomposition? Verify this separately.
- Does the final stabilization of **all parenthesizations** use only reflexivity, monotonicity and an independently proved \(R_\infty²=R_\infty\), without illicit reassociation?

**Important historical correction:** Two earlier examples of *general* nonassociative locale relations incorrectly asserted that a topologically dense inclusion \(D_{\rm discrete}\to C\) was a locale-surjection. It is not. These examples were explicitly withdrawn in [the correction note](ProjectA_CO01_historical_dense_inclusion_locale_surjection_CORRECTION_2026-11-11.md). This must **not** be transferred into the present proof, which uses a different surjection and gives a literal frame-injectivity argument. Conversely, do not reject the new proof solely because the older example was wrong; decide it on its own merit.

**Deliverables:** A clear verdict (correct, repairable, invalid, or undecided), first fatal gap if any, line-by-line justification of all nonstandard categorical steps, potential counterexamples (especially to the general closed-family theorem), minimal fixes and notation ambiguities, and whether the full \(\mathcal D_Y\) cube conclusion truly follows from the A-block result. Treat incidental remarks and claims of generality as in scope. You may state that a proposed new result is classical or uncertain priority. Do not infer that the theorem is published or certified.
