# Project A — bounded ordinary graph diameter and unbounded localic composition rank
## Audit archive · 20 November 2026

This folder preserves **separate** internal and independent external evaluations of the Stone-locale rank theorems. The independent referee **did not have the internal audit** while reviewing the candidate packet.

### Primary documents

- [Independent blind referee report](INDEPENDENT_REFEREE_REPORT.md), 20 November 2026. Favorable verdict for the finite-rectangular calculus, diameter-three and diameter-two exact ranks, ordinary clique unboundedness, and repaired connected nonassociative gadget/attachment. Its initial clique bound was n+2≤r(H_n)≤2n+2.
- [Independent referee's later addendum](REFEREE_ADDENDUM.md), 20 November 2026. Strengthens the clique result to the **exact all-bracketing rank n+2** and proves a general point-clique overlap-graph lemma. These additions are **referee-origin**, subsequent to the blind report.
- [Internal adversarial audit](INTERNAL_ADVERSARIAL_AUDIT.md), 20 November 2026. Prepared **before** the independent review; warns against the unsupported whole-product image in the earlier unmodified gadget and validates the repaired version. Kept separate from the blind materials.

### Source packet

The originally issued blind ZIP was named **ProjectA_Bounded_Diameter_Unbounded_Rank_BLIND_AUDIT_2026-11-20.zip** and contained, in sequence:

- 00_READ_ME_FIRST.md
- 01_BLIND_REFEREE_PROMPT.md
- 02_STONE_CHAIN_CANDIDATE.md
- 03_NONASSOCIATIVE_ATTACHMENT_CANDIDATE.md
- 04_DEFINITIONS_DEPENDENCIES_AND_TESTS.md
- 05_support_rank_check.py (optional finite symbolic consistency test)

The source ZIP was provided as a conversation attachment; it is not reproduced as a binary file in this GitHub text archive. The two **original reports** and the internal audit above are preserved as independent markdown documents; they have not been rewritten into the canonical theorem note.

### Current corrected mathematical entry points

- [Canonical post-referee theorem and proof note](../../../../ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md).
- [External/internal reconciliation and claim ledger](../../../../ProjectA_BOUNDED_DIAMETER_RANK_EXTERNAL_AUDIT_RECONCILIATION_2026-11-20.md).

The current verified ranks are:
\[
r(D_n)=3n+4,\qquad r(\widetilde D_n)=2n+4,\qquad
r(H_n)=n+2,
\]
each for **all** bracketings, with ordinary graph diameters ≤3, ≤2 and ≤1. The attached **nonassociative** variant has uniformly bounded ordinary graph diameter **8** and verified unbounded rank, but no exact rank formula.

**Post-referee only (not blind-audited):** realization of any finite connected overlap graph on a Stone locale with rank diameter+1, and the pointwise-filtration formula for every bracketing. Both appear with proofs and qualifications in the canonical note.

**Not established:** exact six-step rank for the *old unmodified* nonassociative gadget; exact rank of the repaired attached family; equality/associativity of the **full localic intermediate clique powers**. The last is the next intended research question.

No novelty or literature-priority assessment is implied by this audit archive.
