# Independent blind referee prompt — Project A, Q′ pre-nucleus and Boolean-support normal form

**To the referee: Please read this prompt FIRST, then the attached companion file**
\`ProjectA_Qprime_PRENUCLEUS_EXTERNAL_BLIND_packet_2026-11-12.md\`.
**Do not read internal audits, previous referee reports, comparisons, or reconciliation notes before completing your own independent report.** The packet is self-contained for the claimed results; repo source links are optional context, not prerequisites.

## Why we are asking

We study localic separation relations associated with a frame \(L\), particularly the fitted diagonal \(\mathcal D\), its finite-cover approximation \(\mathcal D_2\), and their closed hulls \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal W_2=\operatorname{cl}\mathcal D_2\). The unresolved question
\[
(Q'):\qquad \mathcal W_2(X)=\mathcal W(X)\quad\text{for every locale X?}
\]
implies a weaker open question about the Urysohn relation \(\mathcal U\):
\[
(Q):\quad \mathcal W_2=\mathcal U\ \Longrightarrow\ \mathcal W=\mathcal U.
\]
**Neither question is claimed solved.**

After a lengthy series of geometric example constructions, we have returned to the **pre-nucleus** \(\Phi(q)=\bigvee_{\mathcal C}(w_{\mathcal C}\to q)\). The new proposal makes the metaphorical “self-similarity of counterexamples” precise: any failure of \(Q'\) yields a canonical nonzero regular-open **hole** \(E\) inside \(\mathcal W_2\), a complete Boolean-valued finite-cover-compatible pair matching one full cover to zero, and the **least closed common coordinate support** \(K\). It claims that the *same hole E*, not merely another failure, survives inside \(\mathcal W_2(K)\), while \(\mathcal W(K)\) misses it. The pair is jointly zero-reflecting on K, forcing the bad cover's rather-below patch to vanish, and the marked support construction becomes idempotent.

We want an adversarial check of whether this is correct, whether “the same E” is a legitimate localic statement, and whether the claimed reduction has mathematically useful content beyond simply restating \(Q'\).

## Tasks and priority

1. **Independently verify or refute each CORE item**, using the proofs actually in the packet. Give each a verdict: **correct**, **correct with a precise repair**, **not established**, or **false**. A small explicit counterexample is preferred to a vague objection.
2. Check **point-free validity**, not just ordinary points. In particular examine sublocale joins/meets, relative pseudocomplementation, the least dense Boolean sublocale, whether E remains the same after closed restriction, and where closure does or does not commute with restriction.
3. Check the formula
   \[
   e_C=p_{1*}((w_C\to d_0)\to d_0)
         \wedge p_{2*}((w_C\to d_0)\to d_0)
   \]
   (the inner implication is \(w_C\to d_0\)); verify it really yields the **least closed common coordinate support**, and check whether repeating the construction on the *marked E* is idempotent.
4. Distinguish **weak fitting defects** \(\mathcal D_2>\mathcal D\) from **strong open-hull defects** \(\mathcal W_2>\mathcal W\). Does a weak fitting defect really give a nonzero **relative closed** \(T_C=\mathcal D_2\wedge C(w_C)\)? Does the strong hole require E to be relatively **open** in W₂? Does the branching-domain control invalidate any claimed converse?
5. Check the consequences \(t_{C|K}=0\), disappearance of nonzero open two-coordinate hull-sound strips, and absorption of earlier safe patches. Distinguish unconditional proofs from assertions depending on earlier unrefereed strip theorems.
6. Check the **one-sided closed compact/regular rigidity theorem** provided in the packet. Assess the two hereditary criteria which, surprisingly, purport to force the **stronger equality \(\mathcal D_2=\mathcal D\)**.
7. Check that the statements about \(Q,Q'\), idempotence, support minimality, and lax naturality have the precise logical scope claimed. No full transfinite descent, minimal-counterexample existence, or equality of arbitrary closed-restriction pre-nuclei is asserted.
8. **Presentation critique:** Record confusion encountered on first reading, hidden dependencies, notation clashes, missing hypotheses, and possible shorter proofs. Please consider remarks and qualifications as fully in scope, not only numbered theorems.

## Optional mathematical suggestions

If a specific, bounded next check or an independent proof strategy occurs to you, describe it and state its first falsification test. We would especially appreciate a way to decide whether a jointly zero-reflecting Boolean pair arising from a NONZERO **OPEN** hole is impossible, without constructing new ad hoc spaces.

A reasoned answer **“no further suggestion”** is entirely welcome. We are not asking you to solve \(Q'\) during the review.

## Ground rules

- **Blind independence matters.** Please do not request or look at our internal audit or previous reports until your report has been completed. The packet flags old prerequisites but does **not** tell you our internal verdict on the new results.
- Do **not** treat standard named facts as permission to overlook misuse: Isbell's Booleanization, pullback of open/closed sublocales, and closed heredity need the precise hypotheses.
- Do **not** silently repair a false statement. Explain the precise failure and the smallest repair.
- No originality/priority/publication claim is made. Audit **correctness and exposition** first.
- If you cannot complete all the packet, tell us exactly which sections were checked independently.

Thank you. An adversarial negative report would be just as valuable as a positive one.
