# Independent blind referee assignment — Project A, post-\(\mathcal V\) hierarchy

**IMPORTANT — READ THIS PROMPT FIRST, THEN THE ACCOMPANYING PACKET.**

You are asked to serve as an **independent, adversarial mathematical referee** for a cluster of working results on the localic separation relations \(\Delta,\mathcal I,\mathcal D,\mathcal U,\mathcal V,\mathcal W,\mathcal F\), their lattice combinations, and the simultaneously closed-and-fitted diagonal hull \(\mathcal H\). The authors have been exploring these notions from a universal-algebra and graph-theoretic viewpoint, partly inspired by Cameron–Kumar's *Graphs on topological spaces* (arXiv:2610.14783). Their larger project does **not** assume that spatial/topological arguments automatically hold in localic products.

This is a **blind correctness audit**, not a request for encouragement, exposition polishing, or literature priority assessment. The packet presents *claims to be checked*, not previously verified theorems. You are not given earlier internal audits or external referee reports. **Please do not search for or read any other project audit/reconciliation documents until your independent check is complete.** If you must consult the project repository for a technical definition, record exactly what you read. Classical literature may be consulted as appropriate, with precise theorem/hypothesis citations.

## Your assignment

1. **Audit every central theorem independently**, proving it afresh where feasible; explicitly try to disprove it. A theorem should not be marked correct merely because its proof uses familiar words such as “Priestley”, “spatial”, “scattered”, “fitted”, or “product”.
2. **Check all topologies and frame constructions**: topology basis axioms, Hausdorff/patch/Priestley/spectral claims, sobriety, local compactness, compactness, scatteredness, noncoherence, specialization order, and product-spatiality hypotheses.
3. **Separate ordinary point relations from genuine localic sublocales.** Whenever a pointwise argument is used for a sublocale identity or strictness, identify the exact point-determination or compact-open quotient theorem that licenses the inference. Audit the spatiality of *fitted* sublocales particularly carefully.
4. **Check the general coherent Priestley argument** that patch-closed specialization-upsets determine fitted coherent sublocales, including the compact-open-filter quotient, and that closed-and-fitted relations correspond exactly to patch-closed comparability-saturated subsets. Check the claimed characterization of \(\mathcal F\) by patch-closed equivalence relations and the corollary \(\mathcal H\) transitive iff \(\mathcal H=\mathcal F\) for coherent locales.
5. **Check the two-ray counterexample** as an actual coherent localic example: order is closed and Priestley, \(\mathcal H=R\) is fitted and closed, its nontransitivity is **internal**, \(\mathcal F\) is full, and \(\mathcal U\vee\mathcal V\subsetneq\mathcal H\) is a *sublocale* inequality rather than point-set arithmetic.
6. **Check the arbitrary-frame \(\kappa\)-recursion**, including monotonicity, fixed points, limit stages, the distinction between joins and closed hulls, and minimality of its eventual stage \(\mathcal H\). Check the coherent formula \(S_n=\mathcal I^{2n+1}\) and especially the exact first stabilization ordinal \(\omega+m\) for the handle examples. Search for an off-by-one error or an earlier stage containing unexpected cross pairs.
7. **Check the upper-diamond noncoherent example** from the three-limit-point \(T_1\) space. Does the scattered-sublocale theorem really justify \(\mathcal D=\Delta\), \(\mathcal V=\mathcal I\), and \(\mathcal H=\mathcal I\)? Is \(\mathcal U=\mathcal F\), and does \(\mathcal U\vee\mathcal V\nsubseteq\mathcal H\) follow?
8. **Check both lower-diamond examples separately**, prioritizing the new compact three-boundary-point construction. Verify the complete chain
   \[
   \Delta\subsetneq\mathcal D=\mathcal M\subsetneq
   \mathcal I=\mathcal J=\mathcal W=T(\mathcal J)
   \subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F.
   \]
   Confirm that the space is *not* almost normal. Independently check the optional noncompact almost-normal thickening's \(\mathcal W\)-boundary-transfer claim if the supplied material permits a verdict; say explicitly if a supplementary source is necessary.
9. **Check all stated universal hull identities and comparable-side equality criteria**. Beware reversal of order when translating between nuclei and sublocales; beware treating frame-pseudocomplements as set complements.
10. **Audit secondary statements, remarks, and purported generalizations**, not only the headline results. Identify stronger or simpler replacements if you find them, and distinguish them from repairs necessary for correctness.

## Reporting format

Please organize your report into the following sections, with explicit independent verdicts (**correct / correct conditional on a named standard lemma / repairable gap / incorrect / cannot assess from supplied data**) for each cluster:

- **A. Definition/notation consistency and general lattice-hull lemmas.**
- **B. Priestley/fittedness representation and coherent \(\mathcal H/\mathcal F\) theorem.**
- **C. Two-ray example and localic nontransitivity.**
- **D. Scalar \(\kappa\)-recursion, coherent odd powers, and exact \(\omega+m\) examples.**
- **E. Compact noncoherent upper-diamond counterexample.**
- **F. Compact three-boundary-point lower-diamond counterexample.**
- **G. Optional noncompact almost-normal thickening and \(\mathcal W\)-boundary transfer.**
- **H. Surviving theorem list, dependency graph, fatal gaps, repairs, and suggested next mathematical questions.**

For any gap, give **the earliest invalid inference**, a concrete counterexample or precise unfulfilled hypothesis if possible, and whether the stated theorem can still be rescued. If the overall story is correct, say what you actually checked independently versus accepted from literature. If a strong claim fails, explain which **weaker claims survive** and how the main hierarchy should be updated.

## Mathematical context and boundaries

The project has already proved several coherent relation identities and explored finite-rank bars, but this packet's *new* claims should be audited without assuming that old proofs extend beyond their stated hypotheses. The motivation is to understand whether \(\mathcal H\) is a sensible pointfree graph-connectivity hull and how \(\mathcal U\) differs from the formal cross-hull \(\mathcal W=\operatorname{cl}(\mathcal D)\) outside coherence.

**Do not claim originality or publication readiness from a correctness verdict.** If browsing literature, clearly separate standard theory and your new verification. The packet is deliberately self-contained; please do not rely on links to other chats or presumed project history.