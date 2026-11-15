# Project A — (A-SC) external blind referee reconciliation

**15 November 2026.** Independent blind report received for [the prompt](ProjectA_ASC_EXTERNAL_BLIND_PROMPT_2026-11-15.md) and [original packet](ProjectA_ASC_EXTERNAL_BLIND_PACKET_2026-11-15.md). The referee did **not** see the internal adversarial audit or the repository. [Original report](project-a/audits/2026-11-15/ASC/Referee_report_original.md) is preserved without editorial alteration. No claim of novelty or historical priority is made.

## 1. Independent verdict

**Correct, with no mathematical repairs required.** The referee checked the actual localic universal property and functoriality of \(\mathcal A\), the coherent base case, both frame maps in the ideal-completion retraction, the direction of that retraction, the bottom compactification, the sublocale pullback, and spatiality of the final point-generated sublocale.

The referee specifically tested whether the argument secretly used point-set equality to infer localic equality, whether localic products were being confused with products of spaces, and whether surjectivity of a perfect map was assumed pullback-stable. None of these errors occurs.

The canonical proof is now [ProjectA_ASC_CANONICAL_2026-11-15.md](ProjectA_ASC_CANONICAL_2026-11-15.md).

## 2. Referee improvements incorporated

1. **Direct open retract:** For an arbitrary stably continuous frame \(L\), put \(K=\operatorname{Idl}(L)\), \(\iota(u)=\{v:v\ll u\}\), \(\sigma(I)=\bigvee I\), and \(W=\iota(1)\). The adjunction \(\iota\dashv\sigma\dashv\downarrow\) and the restriction \(L\to\downarrow W\to L\) exhibit \(X\) as a retract of an open sublocale of coherent \(Y=\operatorname{Loc}(K)\). This *eliminates* the need for the bottom compactification in the canonical proof.
2. **Arbitrary sublocale restriction:** \(\mathcal A(U)=U^2\times_{Y^2}\mathcal A(Y)\) holds for every sublocale \(U\), not merely open ones. Openness is needed only when transferring spatiality from \(\mathcal A(Y)\).
3. **Sierpiński exponential:** \(\mathcal A(X)\cong X^{\mathbb S}\) as locales. This is established carefully in [the separate note](ProjectA_SIERPINSKI_EXPONENTIAL_2026-11-15.md), including the localic product-frame calculation and the consequence that \(\mathcal A\) preserves all limits.
4. **Stronger structural corollary:** \(\mathcal A\) preserves stable local compactness, not merely spatiality in that class. The canonical theorem note now proves closure of stably continuous frames under frame retracts rather than taking it on faith.
5. **Finite-poset extension:** For finite Alexandrov posets \(P\), the localic diagram exponential \(X^P\) is spatial and stably locally compact when \(X\) is. A proof is included in the Sierpiński note. This is a referee-origin suggestion, internally rechecked after the blind review, not part of the original independently audited packet.

## 3. Minor presentation fixes

The canonical text addresses the referee's comments:

- An explicit adjunction verifies arbitrary joins of \(\iota\) and \(\sigma\).
- The ideal-completion directions under frame–locale duality are stated.
- The join/meet arguments cite the correct facts about ideals and frame distributivity.
- The noncompact terminology is explicit: Vickers's “stably locally compact” includes compactness, unlike our usage.
- The base coherent case is established by an actual frame quotient.
- The point-generated conclusion is proved by comparing quotient congruences, not inferred from agreement on point sets.
- The description of old illustrative test spaces is removed from the proof, while their historical status is preserved.

## 4. Status and boundaries

| Statement | Status |
|---|---|
| Coherent \(\mathcal A(Y)\) is coherent | Previously established and included in blind packet; independently accepted |
| Stably locally compact \(\mathcal A(X)=[G_{\le_X}]\) | **Independently blind-refereed, correct** |
| Direct open spectral retraction of any stably locally compact \(X\) | Referee improvement; subsequently checked internally and used canonically |
| \(\mathcal A(X)\cong X^{\mathbb S}\), all-limit preservation | Referee-origin; independently rederived internally; not separately blind-refereed |
| Preservation of stable local compactness by \(\mathcal A\) | Referee-origin, internally checked with frame-retract lemma |
| Finite-poset exponential spatiality | Referee-origin, internally checked; not separately blind-refereed |
| \(\mathcal A(X)\) spatial for all locally compact \(X\) | **Open**, a separate frontier; stability is used in the direct retraction |
| Novelty/prior-art claims | Not investigated; do not assert |

The previous SC+ theorem (characterizing \(\mathcal S=\mathcal M\) by chain intervals) remains independent and unaffected. The positive A-SC result concerns the **oriented** relation \(\mathcal A\), not spatiality or equality of every relation in the wider hierarchy.

## 5. Research program after (A-SC)

The natural next bounded question is spatiality of \(\mathcal A(X)\) for general locally compact sober \(X\) **without** stable continuity. The obstruction to transporting the proof is exact: although \(\iota\dashv\sigma\) persists for continuous frames, \(\iota\) need not preserve binary meets. Regular locally compact spaces are a positive control because \(\mathcal A(X)=\Delta_X\); nonregular, nonstable examples must be tested.

The [local-compactness frontier note](ProjectA_ASC_LOCALLY_COMPACT_FRONTIER_2026-11-15.md) records initial tests separately from the audited theorem.
