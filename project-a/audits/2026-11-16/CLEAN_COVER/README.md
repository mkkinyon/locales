# Clean Boolean cover insertion: 16 November 2026 audit archive

This archive preserves the provenance of the [current canonical consolidation](../../../../ProjectA_clean_cover_sphere_plateaux_and_shifts_CANONICAL_2026-11-16.md). It concerns filtered **ordinary order complexes** of finite posets, not the project's crosscut Čech spectral sequence.

## Chronological records

1. [Original proof](original_proof.md), [external blind packet](first_blind_packet.md), and [blind prompt](first_blind_prompt.md). The [internal adversarial audit](first_internal_audit.md) was **not** supplied to the external referee.
2. [First independent blind report](first_referee_report.md) and [first referee addendum](first_referee_addendum.md). The report accepted the unbounded integral differentials but corrected the 13-vertex relative `d_4` barcode to **degree 4** and observed that an earlier ten-vertex relative `d_3` example was not supported in that packet.
3. [Sphere-plateau blind packet](sphere_plateau_blind_packet.md), [second blind prompt](sphere_plateau_blind_prompt.md), and [seed verifier](verify_seed_collapses.py). The self-contained packet presented the exact free-face certificates, all-stage sphere theorem, actual inclusion equivalences, and integral `±1` differentials.
4. [Second independent blind report](sphere_plateau_referee_report.md). It accepted the plateau and unit theorems, performed further independent finite checks, and supplied the cone-reduction lemma showing that **individual sphere stages collapse onto crosspolytope boundaries**.
5. [Second referee addendum](sphere_plateau_referee_addendum.md). Written **after** the blind report, this proposes a repeatable filtration shift and independent control of interval birth and length. It was *not separately blind-audited*. The canonical consolidation develops an additional whole-spectral-sequence shift, also internally checked only.

The original working proof and first packet predate the corrections and plateau strengthening. Read the canonical consolidation for **current** assertions and the source files here for the audit chronology. No minimality, novelty, or literature-priority claim is made.

## Reproducibility

Run `python3 verify_seed_collapses.py`. The program checks the Hasse relations and covers, all seed filtration cardinalities, every displayed elementary collapse pair in its prescribed order, the octahedral boundary, and its f-vector. It does **not** replace the abstract induction or the integral spectral-sequence argument.
