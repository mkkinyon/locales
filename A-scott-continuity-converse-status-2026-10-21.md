# A — Scott-continuity converse: research status (21 October 2026)

**Status: unresolved.** A ledger of the October 20–21 discussion, **not** a paper-ready proof. Consult [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md), [A-continuous-frames.md](A-continuous-frames.md), and [A-external-audits-reconciliation-2026-10-20.md](A-external-audits-reconciliation-2026-10-20.md) for foundational and audit context.

## Notation and question

For an internal closed equivalence relation E ⇉ X, put L=O(X), M=O(E), α=p₁*, β=p₂*, r_E=β_*α. Special relation I=cl(Δ_X). The primary open question: under what hypotheses does Scott continuity of r_I force localic properness of p₂:I→X? Separate (i) Scott continuity of β_* on all O(E), (ii) co-Frobenius/stable closedness, and (iii) idempotence of r_I.

## Established elementary statements

- For reflexive symmetric E, r_E is monotone, deflationary, finite-meet-preserving; its fixed points are exactly saturated opens, equalizer B={u:αu=βu}.
- For coequalizer q:X→Q and s=q*q_*, s(u) is the largest saturated open below u, s≤r, s∘r=s=r∘s. Idempotence of r is equivalent to r=s. Scott continuity of s iff Scott continuity of q_* (q* order embedding).
- In a continuous frame, monotone r is Scott-continuous iff r(a)=∨_{b≪a}r(b). For f:Y→X with O(X) continuous, f_* is Scott-continuous iff f*(u)≪f*(v) whenever u≪v. These are generic domain-theoretic lemmas, not new discoveries.
- For reflexive E, β_*(α(a)∧β(b))=r_E(a)∧b. Scott continuity of r_E implies preservation of directed joins of **coordinatewise directed rectangles** α(a_i)∧β(b_i), but not from this alone preservation on finite unions of rectangles.
- The right adjoint β_* is Scott-continuous iff it preserves directed joins on directed families of finite rectangular unions (using join-generation). This is a reduction, **not** a proof of the converse.
- The known properness ⇒ Scott continuity and idempotence results require genuine localic properness and Beck–Chevalley; do not reverse these implications without proof.

## Failed or incomplete approaches

1. Way-below interpolation to force r_I²=r_I: circular; finding b≪a with u≤r(b) does not yield b≤r(a).
2. Rectangular generators: β_* need not preserve binary joins; controlling single rectangles does not control finite unions.
3. Quotient fixed-point operator: Scott continuity of r need not imply that of s by abstract order theory. On P(N), r(A)={n∈A:n+1∈A} is monotone, deflationary, finite-meet-preserving and Scott-continuous, but its largest-fixed-point operator s(A)={n:[n,∞)⊆A} is not Scott-continuous. **This operator example does not arise from an equivalence relation.**
4. Geometric confinement for I=clΔ: if a∧b=0 then p₁*a∧p₂*b=0. **Do not** infer p₁*a≤p₂*(a**) from this: inverse images need not preserve pseudocomplements. The valid statement is p₁*a≤(p₂*(a*))*. Closed relational images E[K] of compact sublocales K can be useful, but closed does not mean compact.
5. Arbitrary closed equivalence relations need not have idempotent r_E; explicit counterexamples and caveats appear in the foundational audits. They do **not** settle special I=clΔ.

## Specialized positive calculation — Alexandrov locales

For the upper-set Alexandrov space of a poset P, ordinary points satisfy x I y iff ↑x∩↑y≠∅. If I is transitive, its classes are clopen upward-directed components, with I total on each component. The saturation operator selects complete components contained in an open, so is idempotent; its Scott continuity is equivalent to compactness of every component. Componentwise finite-product properness yields proper relation projections. This is a **spatial Alexandrov special case**, not an arbitrary algebraic-frame theorem. Audit independently before publication.

## Open questions

- Continuous frame, I transitive, r_I Scott-continuous ⇒ r_I idempotent?
- Same hypotheses ⇒ β_* Scott-continuous / p₂ proper?
- Does equality I=U assist either implication?
- Is there a counterexample that is not a disguised arbitrary-closed-relation construction?

**Discipline:** Do not regard any of these implications as established. In classical mathematics continuous frames are spatial by Hofmann–Lawson (already corrected in A-continuous-frames.md), so do not refer casually to 'pointless continuous frames' in classical/ZFC arguments.
