# Independent BLIND referee prompt — Project A: dense rational bridges as proposed counterexample to Q and Q′

**14 November 2026.** Please read this prompt first and then the accompanying self-contained packet, `ProjectA_DENSE_BRIDGE_EXTERNAL_BLIND_PACKET_2026-11-14.md`.

We ask for a **strictly independent, adversarial mathematical audit** of a newly proposed construction in point-free topology. Do not read any internal audit or comparison notes before delivering your first report. A separate internal examination exists but is intentionally **not** included. You are not being asked to endorse the argument or to find a repair at all costs.

## Why this matters

For each locale X, let D(X) and D₂(X) denote respectively the full-cover and finite-cover fitted diagonals in the localic square; put W(X)=cl D(X), W₂(X)=cl D₂(X), and let U(X) be the closed Urysohn-style relation. Precise frame definitions are in the packet.

The universal questions under investigation are:

- **Q′:** Is W(X)=W₂(X) for every locale X?
- **Q:** Does W₂(X)=U(X) imply W(X)=U(X) for every locale X?

Q′ would imply Q. Prior work found many finite-versus-full diagonal discrepancies that **did not** survive closure. We have therefore insisted on a nonzero *closed-hull* gap and, for Q, a separate proof of W₂=U.

The packet proposes a second-countable sober T₁ topological space X, étale over ℝ, formed from two disjoint global sections plus bridge points indexed by ℚ. The proposed precise conclusion is

\[
\boxed{W(X)=I(X)<W_2(X)=U(X)=X\times_{\mathbb R}X.}
\]

If valid, this would answer **both** universal questions negatively. It is a **claim under review**, not an accepted theorem.

## Audit instructions

1. **Start from the actual topology.** Verify that the stated neighborhoods really define a space and the projection p is an open local homeomorphism. Check the claimed fibers, T₁, sobriety, second countability, and openness of the section charts. Report any issue with the infinite gluing.
2. **Recheck the density lemma independently.** For *every arbitrary finite open cover* F of X, the common-member base open m_F for the two distinguished sections is claimed dense in ℝ. Is the finite-union-of-boundaries argument sound in every case? Try to design a finite countercover.
3. **Check the POINT-FREE step.** Verify that the double-negation Booleanization B(ℝ), with its frame map β*, converts dense m_F into 1 and hence defines a NONZERO map into D₂(X). Check the distinction between joins in O(ℝ) and joins in RO(ℝ). Investigate whether the purported generalized pair could collapse to zero.
4. **Verify the full diagonal and Q′ failure.** Does the infinite atlas of open sections imply D(X)=Δ_X in Loc under the stated naturality? Is the open rectangle S×T genuinely disjoint from W(X)=cl Δ_X? Is there a valid *closed-hull* gap, rather than merely D₂≠D?
5. **Audit the upgrade to Q.** Verify F=X×_ℝX is a closed SPATIAL sublocale of X². Does containment of the dense Boolean-support sublocale force the entire open chart J=S×_ℝT into the closed hull W₂? Are all remaining ordinary fiber-square pairs indeed in I(X)? Does this suffice to establish W₂(X)=F=U(X)?
6. **Try to falsify the chain** in any other way: spatial-versus-localic product confusion, incorrect use of density, improper sublocale restriction, unsupported heredity, incorrect inclusion orientation, or an unnoticed finite cover.

Please classify each central claim as **correct / incorrect / incomplete**, identify the first fatal failure if any, and give a corrected theorem if possible. Rank concerns by severity, including possible nonfatal presentation defects. If the argument survives, please provide your own shorter derivation where one is available.

The packet includes its definitions and complete working proof, so inaccessible repository links should not be a blocker. You may consult primary mathematical literature if needed, but distinguish imported facts from your independent derivation. No literature-novelty or priority judgment is required; if you have a clear source bearing on the construction, please mention it.

**Important:** Report your independent findings *before* seeking any internal audit. We will compare audits only afterward.
