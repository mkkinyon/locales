# External referee prompt — Project A: when is W = U?

**Please read this prompt FIRST, then read the attached packet `ProjectA_WU_external_blind_packet_2026-10-24.md`.**

You are being asked to act as an **independent, adversarial mathematical referee** for ongoing exploratory research in point-free topology. The author is an algebraist developing a localic analogue of separation relations appearing in Cameron–Kumar, *Graphs on Topological Spaces* (2026). Your task is to verify, correct, simplify, or refute the claims; **it is not to endorse them**.

## Research objectives

**General goal:** Understand and characterize exactly when

\[
\mathcal W(X)=\mathcal U(X),\qquad
\mathcal W=\operatorname{cl}(\operatorname{fit}(\Delta_X)),
\]

where \(\mathcal U\) is the closed localic Urysohn relation. This identity is known in coherent locales but fails for some compact noncoherent locales. We seek structural frame-theoretic and localic explanations beyond coherence.

**Specific focal goal:** Determine whether the binary-cover condition is sufficient in arbitrary frames:

\[
\boxed{\mathcal W_2=\mathcal U\ \Longrightarrow\ \mathcal W=\mathcal U,}
\]

where \(\mathcal D_2\) is the intersection of all two-element-cover diagonal-square open sublocales and \(\mathcal W_2=\operatorname{cl}(\mathcal D_2)\). The implication is proved for compact frames and under several weaker/special hypotheses, but **is not resolved in the packet**. A genuine proof or counterexample would be valuable, but a careful identification of why the present techniques do or do not settle it is equally valuable. Do not invent an answer if the problem resists resolution.

## Required independent-review protocol

1. **Cold read:** Base the first review on the attached packet, your own mathematics, and the explicitly identified published literature. Do **not** search or read earlier internal audits, reconciliation notes, prior referee reports, or the live GitHub repository until you have finished your independent mathematical judgment. This matters because prior independent-audit work was inadvertently included in an earlier external-audit context.
2. **Check the entire packet:** All definitions, lemmas, proofs, examples, inequalities, remarks, and footnotes are in scope. A correct headline theorem with an incorrect aside still deserves correction.
3. **Do not infer localic equality from point-set equality.** Pay particular attention to nonspatial sublocales, frame coproducts, arbitrary joins, pseudocomplements, nuclei, and the distinctions \(\mathcal D\ne\mathcal D_2\) versus \(\mathcal W\ne\mathcal W_2\).
4. **Independently check sources and priority.** The paper of Arrieta–Picado–Pultr (2022) already contains the full diagonal-neighborhood pre-nucleus \(\kappa_L\) (Lemma 5.4) and a cover-respecting homomorphism criterion (Lemma 4.4). Do not treat these underlying ingredients as new. Examine whether any other packet identities are also established literature, without making unsupported claims either way.
5. **No artificial progress:** If the central implication stays open, say so. A useful referee report may consist chiefly of rigorous verification, counterexamples to intermediate claims, or sharpening of hypotheses.

## Questions on which to concentrate

**Highest priority**

- Is \(d_{\mathcal U}=\bigvee_{\delta^*w=1}w^*\) correct for arbitrary frames? Are any coproduct-rectangle facts used without justification?
- Is the finite-cut decomposition of a finite square cover into a finite meet of binary diagonal neighborhoods valid in an arbitrary frame coproduct?
- Does \(\mathcal D_2=\mathcal D\) hold for compact frames and for frames covered by compact complemented elements?
- Are the binary and unrestricted fixed-point criteria, including the canonical Booleanization reduction, correct? **The binary operator \(\Psi\) is not assumed to be a pre-nucleus.**
- Does the regular-closed core and nonregular-boundary localization behave as claimed inside the sublocale lattice?
- Is the Scott/Cantor example a valid finite-cover-versus-infinite-cover witness, and is it correctly stated *not* to settle \(\mathcal W_2=\mathcal U\Rightarrow\mathcal W=\mathcal U\)?
- Can you prove or disprove the focal implication, or find a class of locales substantially broader than those already listed for which it holds?

**Secondary priority**

- Verify the geometric binary criterion and disjoint-open rectangle certificate under their stated spatiality hypotheses.
- Verify the product-stabilization and cofinite-apex examples, especially their sobriety, product spatiality, claims of nonspatial fitted diagonals, and exact hierarchies.
- Inspect the countable-distributivity/Boolean-target lemma and its Lindelöf consequence.
- Identify shorter proofs, stronger statements, false generalizations, and useful related work.

## Requested report format

Give an executive verdict followed by findings sorted as **fatal / major / minor / verified**. For each contested statement quote its label from the packet, explain precisely where the proof fails or why it works, and provide a repair or explicit counterexample wherever possible. End with:

- a compact corrected theorem ledger, separating **proved**, **proved under an additional hypothesis**, **false**, and **open**;
- an answer/status for the **specific focal implication**;
- a short assessment of the **general W = U program** (what structural insights survive);
- bibliographic/priority cautions, including what is already due to Arrieta–Picado–Pultr.

Please complete the independent portion before consulting any prior audit or live repository notes. The packet is intentionally self-contained and does not embed our own audit conclusions.