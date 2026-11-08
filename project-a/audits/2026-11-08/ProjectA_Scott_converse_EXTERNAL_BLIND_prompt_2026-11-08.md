# Independent referee request — Project A: Scott-continuity converse

**8 November 2026 · External review 1 of 2 (conducted sequentially)**

Please **read this prompt first**, then the accompanying file `ProjectA_Scott_converse_EXTERNAL_BLIND_packet_2026-11-08.md`.

## The assignment

Independently referee the two assertions in the packet:

- **T (topological):** for a closed relation `E ⊆ X × Y` with `X` weakly locally compact (every point has a compact neighborhood), the relational open operator `r_E=(p_Y)_*p_X^*` is Scott-continuous **if and only if** the projection `p_Y:E→Y` is a closed map with compact fibers. `Y` has no separation or local-compactness assumptions.
- **L (localic):** if `O(X)` is a continuous frame, then for any closed sublocale `E ↪ X ×_loc X`, Scott-continuity of `r_E=(p_2)_*p_1^*` is **equivalent** to `p_2:E→X` being a proper locale map, using the convention of Scott-continuous right adjoint **plus** closed Frobenius.

We request a genuine adversarial correctness check. Treat every assertion and explanatory aside as in scope; do not assume the statements are correct because a proof is supplied.

Please, in particular, verify:

1. That **weak** local compactness (an open neighborhood inside some compact subset) suffices for the forward topological argument; no Hausdorffness or closedness of compact subsets may be tacitly used.
2. The directed-cover argument, the uniform compact support over `W_F`, the treatment of a **closed subset of E**, and the compact-factor projection/tube lemma.
3. The reverse direction for possibly empty fibers and arbitrary non-Hausdorff `X,Y`.
4. Whether the intermediate **local uniform compact support** condition really is equivalent to the other two assertions under the stated hypotheses.
5. The exact classical prerequisites for representing a continuous frame by a locally compact sober space; compatibility of the *localic* product with the ordinary product; and identification of a **closed localic sublocale** with an ordinary closed subspace.
6. The difference between Scott continuity of `p_{2*}` and **full localic properness**, especially the closed Frobenius calculation.
7. The assertions about symmetry, transitivity, quotient consequences, and any scope or terminology problems.

## Desired report

Please give:

- An **overall verdict for T**, and separately an **overall verdict for L**: valid as stated, valid with corrections/hypotheses, invalid with counterexample, or unresolved on the supplied argument.
- For every gap or incorrect statement, its **precise location**, a rigorous explanation, and, where feasible, a repair or counterexample. Distinguish a fatal issue from an editorial clarification.
- Any overlooked assumptions (including choice principles), incorrect uses of external literature, and first-reading ambiguities.
- Optional simplifications, stronger conclusions that genuinely follow, or literature antecedents, **clearly separated** from the referee verdict. Publication priority is *not* the principal task.

If the proof is sound, please say so explicitly and identify the hardest step(s) you checked independently. Do not fill a gap by silently adopting an unstated assumption.

## Independence protocol

For this review, please examine **only this prompt, the accompanying technical packet, and published background sources you independently choose to consult**. Do **not** read the Project A internal foundational audits, past referee reports, reconciliation notes, master theorem ledger, repository status index, or the second review's packet/report. The technical packet is intended to be self-contained; let us know if it is not.

The researcher's second review (on *coherent localic composition*) is separate and will be conducted after this one; no conclusions from it are needed here.

Please return your report as Markdown or plain text. No edits to the technical packet are requested.