# Independent blind mathematical audit request

**Project:** Point-free topology, Project A (localic fitted diagonal and products)

**Subject:** Claimed negative answer to the nonclosed Cohen × Arrieta fitted-diagonal product question, and a general closed-graph theorem

**Review order:** Read **this prompt first**, then `EXTERNAL_BLIND_PACKET.md`. The packet gives definitions, source facts, proposed proofs, and explicit questions. The primary source is Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, arXiv:2310.18522, especially §§2.5 and 4: <https://arxiv.org/pdf/2310.18522>.

Please act as a genuinely skeptical **independent referee**. The author has done an internal audit, but you are **not** being shown its report; do not request or read it before completing your own judgment. Do not take the packet's claims of correctness or provenance as evidence.

Your main tasks:

1. Decide whether the claimed general theorem is correct: for strongly Hausdorff `Y`, `D(Y)=Δ_Y` iff `D(Z×Y)=Δ_Z×D(Y)` for every Boolean locale `Z`; in the negative case a *binary* product cover suffices over some Boolean base.
2. Independently verify the **specific** Cohen-base specialization for Arrieta's space, which is stronger than the general theorem's existential choice of Boolean base:
   
   \[
   D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A),
   \qquad Z_C=\operatorname{Loc}(RO(2^\omega)).
   \]
3. Check every use of localic (not merely point-set) closure, sublocale meet, graph, equalizer, Booleanization, complete Boolean meet, frame map, and arbitrary-join preservation.
4. Check the Arrieta source facts independently, especially whether **strong Hausdorff** really makes the localic diagonal closed and whether the attached finite sets `K_n` have the claimed cofinal-density property.
5. Identify counterexamples, missing hypotheses, unjustified implications, or mistaken distinctions. In particular, challenge the jump from density of ordinary Cantor rectangles to **full-cover compatibility in a complete Boolean frame**.
6. Audit the smaller `D₂` precursor as a consistency check, but do **not** confuse a `D₂`-compatible pair with the new **all-cover-compatible** one.
7. Assess what the result does **not** imply about closed hulls `W,W₂`, the universal questions Q and Q′, or relative openness inside `D₂`.

Please report:

- A clear **verdict on each main claim** (correct / correct with repair / unproved / false), with concrete reasons.
- The **first point of confusion on reading**, if any, even if ultimately resolved.
- Every gap and any explicit repair, with exact formulas when possible.
- Any useful simplification or generalization that occurred to you; “none” is fine.
- A compact list of proof obligations that would still need independent verification.

**Blindness and files:** The external packet deliberately omits the internal audit and its conclusions. Please write your own report first. If a linked source is inaccessible, state that limitation explicitly and distinguish source-dependent from self-contained checks.

**Research status before this claim:** The independent 12–13 November review established that the *closed* Cohen × Arrieta relation satisfies `W=W₂=U=Δ_Z×A²`; it did **not** settle the actual nonclosed `D` equality. Neither universal Q nor Q′ is known. The new negative product claim, if correct, does not by itself settle either universal question.
