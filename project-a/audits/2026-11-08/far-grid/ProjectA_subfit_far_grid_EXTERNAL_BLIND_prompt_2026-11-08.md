# Independent blind referee prompt — Project A subfit far-grid converse

**8 November 2026.** Read this prompt **first**, then the accompanying technical packet only. Please complete your independent examination **before** seeing any author-side internal audit, earlier referee reports, reconciliation notes, GitHub research history, or outside discussion of this specific candidate. If something essential is missing, note the limitation explicitly.

## Mathematical purpose

We are investigating the separation relations \(\mathcal I=\operatorname{cl}\Delta\) and \(\mathcal U\) on the localic square of a frame, defined exactly in §1 of the packet. The **far-grid property** requires that for each disjoint pair \(u,v\), there be two simultaneous join decompositions into pieces whose cross pairs satisfy \(u_\alpha^*\vee v_\beta^*=1\). It always implies \(\mathcal I=\mathcal U\).

A previous independently refereed example showed the converse fails for arbitrary frames, but that frame was **not subfit**. The narrow new question is:

> Does \(L\) subfit together with \(\mathcal I(L)=\mathcal U(L)\) imply that \(L\) has the far-grid property?

The packet claims **no**, with \(L=\mathcal O(X)\) for a countable second-countable \(T_1\) space built from infinite cofinite clouds \(P_i\), discrete tails \(S_i\), points \(r_i\), and a point \(q\). The argument includes a localic, not merely pointwise, proof of \(\mathcal I=\mathcal U\). The presenting \(T_1\) space is claimed to be nonsober; the **frame**, not the original space's sobriety, is the relevant object. Please treat every claim as unverified.

## Requested adversarial checks

1. **Topology and separation.** Does the displayed family satisfy the basis axioms, including cross-type intersections? Is \(X\) really \(T_1\) and second-countable? Check the inference that \(\mathcal O(X)\) is subfit using precisely the stated subfitness definition. Look for subtle failures caused by infinite cofinite clouds.
2. **All closure formulas.** Independently derive the arbitrary-set closure criterion (3.1) and the four basic-open closure formulas (3.2). In particular, check accumulation from infinite \(P_i\), the tail-filter behavior at \(r_i\), and any possibility of unwanted accumulation at \(q\).
3. **Complete farness table.** Verify every one of the ten unordered basic-open type pairs, including all boundary cases \(i=n\), the finite exclusion sets \(F,G\), and pairs sharing an index. Are the \((A_{i,F},N_n)\), \(i\ge n\), genuinely the only disjoint non-far basis pairs? If not, give an explicit offending pair.
4. **Genuinely localic equality.** Independently check (4.1)–(4.3) using the frame coproduct \(L\oplus L\), its rectangular join laws, or the C-ideal presentation. Does the basis-to-arbitrary-opens passage prove \(d_{\mathcal I}=d_{\mathcal U}\) as **elements of the coproduct**, without assuming the square is spatial or using an invalid pointwise inference?
5. **Far-grid nonexistence.** For \(a=\bigcup_iP_i\), \(b=N_1\), verify the obstruction for **arbitrary** cover families, even overlapping, infinite, or nonbasic pieces. Can a cleverly chosen piece containing \(q\), or a sparse open piece meeting \(P_i\), evade the common closure point \(r_i\)? Check all quantifiers.
6. **Boundary claims.** Check non-sobriety of the original \(T_1\) presentation, the classification of irreducible closed sets needed to claim the soberification is countable, second-countability of the soberification, noncompactness, and noncontinuity of the frame. Distinguish any mistake in auxiliary claims from an error in the central theorem.
7. **Stress tests.** Try to construct a far grid or a disjoint basic pair defeating the claimed coproduct calculation. Check that the argument does not inadvertently rely on stronger hypotheses than subfitness or conflate topological product opens with localic product opens.
8. **Presentation and originality.** Report anything confusing on first reading, including asides and boundary claims; propose precise repairs. You need not conduct a literature-priority audit, but do not infer novelty solely from correctness.

Please give a clear final verdict, distinguishing **fatal**, **major**, **minor**, and **editorial** issues. State which calculations you reconstructed independently and which standard results you accepted. If the main result is valid, say exactly what it settles and which stronger questions (such as a simultaneously sober \(T_1\) representation) it does **not** settle. Research ideas are welcome but label them separately from verified conclusions.

**Independence instruction:** Do not request or read our internal audit until you have finished and signed your report. No author-side verdict is included in the packet.