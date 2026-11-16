# Independent blind referee instructions — Project A clean-cover differential theorem

**16 November 2026**

Please read the accompanying packet **independently and adversarially**, treating it as an unrefereed mathematical manuscript. It proposes a nonzero integral \(d_k\) for arbitrarily large \(k\) in the spectral sequence of a finite-poset order-complex filtration by inserted cover comparisons. We have not supplied the internal audit, and we ask that you **not seek it out before finishing your own report**.

## Requested review

1. **Correctness, with all details in scope.** Check every statement in the packet, including explanatory remarks and the low-dimensional sanity checks. In particular, verify that the indicated pairs are covers, the deletion family is genuinely Boolean, all specified extensions define partial orders, and the given filtration is simplicial.
2. **Base case.** Expand the oriented boundary of the eight-term \(3\)-chain \(T\); verify the \(1\)-cycle \(t\), the corrective chain \(a*x*t\), and the claim that \(\partial(T+a*x*t)\) lies in \(F_0\) while avoiding \(a\). Recheck contractibility of the nine-vertex poset.
3. **Inductive step.** Try to break the construction of the cap vertex \(y\), including transitivity, unintended new comparabilities, surviving cover relations, the filtration level of the correction \(u*y*z\), the oriented chain identity, and contractibility of the full order complex.
4. **Spectral-sequence justification.** Scrutinize the two maximal-simplex certificates. Is the inference from nontriviality of the boundary in \(H(F_{m-1})\) or \(H(F_{m-1},F_0)\) to a nonzero \(d_m\) or \(d_{m-1}\) valid at the stated page? Verify that earlier differentials cannot kill the source or target, and check all bidegrees and coefficient claims.
5. **Relative case.** Check the two-cone description of \(F_0\), its contractibility, the vanishing of \(H_m(Q,F_0;\mathbb Z)\), and the contradiction using the unique maximal top-weight simplex.
6. **Results and status.** Confirm or refute the assertions of nonzero integral absolute \(d_k\) for every \(k\ge3\), and nonzero integral relative \(d_k\) for every \(k\ge4\), together with the example vertex/mark counts. Do not assume the result is novel. Please report any mathematical antecedents you know, and distinguish established facts from conjectural extensions.
7. **Presentation.** Record anything confusing upon first reading, suggest simplifications or better conceptual organization, and note any unnecessary hypotheses.

Please distinguish, in your report:

- **fatal errors** (with a counterexample or explicit failed step);
- **gaps requiring a proof**;
- **correct but poorly explained passages**;
- **verified statements and useful improvements**.

If you find an error, please investigate whether a weaker repaired theorem survives. You are welcome to supply independent calculations, but an explicit integral argument is needed to validate the integral claim. An honest negative assessment is as valuable as a positive one.

## Context

This is one thread of a long-running point-free topology project. Here the construction is purely finite-poset topology and persistent/filtered simplicial homology; it must not be conflated with the distinct crosscut Čech spectral sequences in other project notes. The current goal is mathematical validity and understanding, not publication priority.

**Files supplied:** this prompt and the self-contained blind packet. **Files withheld:** our internal audit and working calculations.
