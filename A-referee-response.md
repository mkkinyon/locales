# Project A — Response to independent cold referee

**18 October 2026.** The user obtained an independent mathematical referee report from another high-effort LLM. The report itself is retained by the user; this document records **our disposition of its mathematical findings**, not a reproduction of the report. The report independently checked the major claims and agreed that the deleted-Tychonoff-plank two-tag example is correct as a **strongly locally compact sober** continuous-frame counterexample. This review is substantial additional evidence, not a substitute for a human referee.

## Corrections accepted

**1. Weak versus strong local compactness (substantive).** A compact neighborhood at each point is *weak* local compactness. To identify a sober space with a continuous frame and to compare the localic product with the ordinary spatial product, require **strong local compactness**: every open neighborhood contains a compact neighborhood, equivalently (in this sober context) core-compactness. The kω and paracompact **point-set theorems remain valid under the weak definition**; only their application to closed localic relations is now stated with the strong hypothesis. This correction does **not** affect the deleted-plank space; its proof provides compact neighborhoods inside arbitrary neighborhoods.

An explicit witness to the distinction: put a generic point ⊥ under the rational line Q, taking as opens all ordinary opens of Q and the whole X=Q∪{⊥}. The space is compact, sober, hence weakly locally compact, but its frame is not continuous: its nonempty proper opens inherit the absence of compact containment from Q.

**2. Product points versus product spatiality (substantive correction).** Hom(1,X×Y) ≅ Hom(1,X)×Hom(1,Y) always. There are no *additional points* of a localic product. What can fail is that the product locale be spatial. Consequently, a **pointwise strict inclusion** gives a strict localic inclusion without a spatial-product hypothesis; a **pointwise equality** needs the spatiality comparison to be lifted to an equality of closed sublocales.

**3. Correct scope and novelty of the negative implication.** Arbitrary regular locales already satisfy I=U=Δ. Classical regular T1 spaces with non-separating continuous real functions provide I=U=Δ⊊F, so failure of the implication for *arbitrary* locales was known. The two-tag construction is distinctive because it yields a **continuous frame**, where regularity would instead imply complete regularity. Published background example: *Embedding topological spaces into Hausdorff ω-bounded spaces*, *Topology and its Applications* (2020), Example 4.1, https://www.sciencedirect.com/science/article/pii/S0166864120302200 . No priority claim is made for the two-tag mechanism without a deeper search.

**4. Closed quotient is not a sufficient hypothesis on its own.** The deleted-plank two-tag X has a **closed** inseparability quotient map q:X→X/E: for any closed C, E[C] is C together with zero, one or both of the **closed classes** A∪{p_A}, B∪{p_B}. Nevertheless q has a non-Hausdorff quotient and I=U⊊F. The earlier closed-saturation theorem requires global additional conditions (such as the kω/σ-compact assumptions); closedness by itself is insufficient.

**5. Superseded status and labels.** Old research notes contained obsolete declarations that the unrestricted continuous-frame question was open and conflicting statements about the coherent case. Active notes should state the negative result, while earlier chronological explorations can be retained with an explicit historical notice. The symbol C, F, U and the star on f* versus open pseudocomplement should be disambiguated in any manuscript.

## Independently supported results (reported by the external reviewer)

- Basic hierarchy, frame expression d_F=∨_{a≺≺b*}a⊠b, reflection/kernel pair, and frame map criteria.
- Seven-point and pointless strictness examples (the reviewer reports independent hand checks and finite computations).
- **Finite-rectangle lemma in arbitrary locales**: identity (a⊠b)*=a*⊠1∨1⊠b*, plus finite-join interaction with the diagonal; the reviewer agrees with the internal addendum and finds it choice-free.
- Coherent conormality/mp-ring characterization and compact/continuous pairwise tests (with the usual choice/spatiality assumptions).
- Compact/kω quotient normality and paracompact decomposition, preserving the distinction between point-set and closed-localic conclusions.
- The two-tag deleted-plank example's topology, strong local compactness, sobriety, pointwise I=U, and U⊊F, together with the localic lift.

## Further work

- Verify the exact external theorem statements, page numbers, and relevant choice principles systematically.
- The Picado–Pultr V.2.4.1–2.4.4 T_OF example was marked unverified by the external report; the book itself explicitly gives the relevant frame epimorphism, strong Hausdorffness and nonregularity in the previously consulted pp. 91–92. Cross-check citations in final manuscript rather than leaving unsupported assertions.
- Check novelty beyond a single literature search, particularly generic-point extensions of closed sets and the possible established terminology for the U-relation.
- Prepare a short *clean* theorem manuscript without contradictory historical progress notes, and seek a second independent human/topologist review before claiming readiness.

**Decision:** the central counterexample remains a strong working result, now independently corroborated; the weak/strong compactness error requires surgical corrections to the localic corollaries but does not overturn the main research outcome. The independent report's novelty assessment is fairly cautious and should guide how a paper is framed.
