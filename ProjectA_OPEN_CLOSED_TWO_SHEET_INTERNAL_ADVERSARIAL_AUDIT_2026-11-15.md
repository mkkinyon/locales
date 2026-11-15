# Project A — internal adversarial audit: zero-dimensional two-sheet one-step theorem

**15 November 2026. INTERNAL. Not to be included in the blind referee packet.**

**Object:** `ProjectA_OPEN_CLOSED_TWO_SHEET_ONE_STEP_CONSOLIDATION_2026-11-15.md`, especially its cross-sheet Lemma 1 and arbitrary-source theorem. This review was carried out after the previous blind audit of the *distinct* discrete-defect (LC-PT) counterexample.

## 1. Verdict, with scope

**No fatal gap found after the attacks below.** I recommend blind external review before upgrading the strengthened theorem to verified status. The proof is self-contained modulo standard facts on sublocales and regularity. This report checks reasoning, not literature novelty; no exhaustive automated model search was run.

The original argument established saturation=fitting for **closed** sources. The present theorem removes closedness entirely because **zero-dimensional \(\Rightarrow\) regular \(\Rightarrow\) fit**, meaning *all* sublocales of the sheets are fitted relative to their own sheet. This step is explicitly grounded in Picado–Pultr–Tozzi and Ball–Picado–Pultr, rather than inferred from the classical behavior of point sets.

## 2. Attack ledger

### A. Does the gluing really contain all diagonal opens?

**Threat.** Only diagonal clopen pairs are assumed; the fitting proof needs \((c,c)\) for arbitrary \(c\in\mathcal O(K)\).

**Check.** Zero-dimensionality expresses every \(c\) as a join of clopens \(d\le c\). Coordinatewise arbitrary joins in the subframe \(L\) give \((c,c)=\bigvee_{d\le c}(d,d)\in L\). **Pass.** Important to state closure under *arbitrary* joins, not merely finite joins.

### B. Is the cross-sheet locus really \(\Delta(P)\), including pointless test locales?

**Threat.** A computation on ordinary comparable pairs could miss nonspatial specialization, the central phenomenon of the project.

**Check.** Work with arbitrary locale \(E\) and frame homomorphisms \(f^*,g^*\). Comparability on clopens \(d,d^c\) forces equality, since their pullbacks are complemented elements; then global opens force factorization through \(P\). In the converse, for \((c,v)\in L\) and clopen \(d\le c\), the identity
\[
(c,v)\wedge(d,d)\vee(d^c,d^c)=(1,v\vee d^c)\in L
\]
is valid coordinatewise. A map factoring through \(P\) pulls back the right-hand open to 1, giving \(h^*d\le h^*v\). Taking joins in the **frame \(\mathcal O(E)\)** yields \(h^*c\le h^*v\). This identifies the cross block by its complete functor of points, not its ordinary points. **Pass.**

**Discarded unsafe shortcut:** One must **not** interchange \(P\wedge\bigvee_{d\le c}O(d)\) with \(\bigvee_{d\le c}(P\wedge O(d))\) in the coframe of sublocales; coframe distributivity does not supply that infinitary meet-over-join law. The generalized-map proof avoids it.

### C. Are the same-sheet and reverse blocks correct?

For maps into one zero-dimensional sheet, the specialization inequalities for both clopen complements force the coordinate maps equal, hence \(\mathcal A(K)=\Delta_K\). Reverse \(U\to F\) comparisons violate the inequality for \(e=(0,1)\) unless the test locale is zero. **Pass.** No Hausdorffness-by-points argument is used.

### D. Does restriction to a general sublocale \(H\hookrightarrow F\) produce \(P\wedge H\)?

The pullback of the diagonal embedding \(\Delta(P)\hookrightarrow K\times K\) along \(H\times K\) is canonically \(\Delta(P\wedge H)\). Its second projection is isomorphic onto \(P\wedge H\). Thus \(\operatorname{Sat}(H_F)\) contains \((P\wedge H)_U\). **Pass.** No image/base-change interchange is needed beyond this explicit pullback of a diagonal.

### E. Is the fitting formula using only valid sublocale distributivity?

**Threat.** One might mistakenly distribute finite meets across infinite joins in a coframe.

**Check.** The proof takes intersections of *all open neighborhoods*, then separately restricts to F and U. On U, global opens bound the trace by P; diagonal opens bound it by H, using \(\operatorname{fit}_K(H)=H\). On F, the same diagonal opens give exact trace H. The recombination
\[
T=(T\wedge F)\vee(T\wedge U)
\]
uses only **finite distributivity** and \(F\vee U=Z\). No infinite distributivity is invoked. **Pass.**

### F. Is every sublocale of the open zero-dimensional sheet fitted in the ambient locale?

**Threat.** Fitting is an ambient notion; relative fitting need not persist along arbitrary embeddings.

**Check.** Any open sublocale of \(U=O_Z(e)\) is an open sublocale of \(Z\), because open embeddings compose. Intersections of relative opens in U remain intersections of ambient opens. Zero-dimensional U is regular and therefore fit, so an arbitrary \(C\hookrightarrow U\) is fitted in Z. **Pass.** The openness of U is essential.

### G. Does saturation preserve the finite join needed in the proof?

**Threat.** It was never established that \(\operatorname{Sat}\) preserves joins as a relational direct image, and it actually fails to preserve certain infinite joins.

**Check.** No join-preservation of \(\operatorname{Sat}\) is assumed. The inequality
\[
\operatorname{Sat}(S)\vee\operatorname{Sat}(T)
\le\operatorname{Sat}(S\vee T)
\]
comes from monotonicity; the reverse bound comes from \(\operatorname{Sat}\le\operatorname{fit}\). Finite joins of fitted sublocales are fitted by coframe distributivity. **Pass.**

### H. Does every sublocale split between F and U?

**Threat.** Point-set decomposition would not suffice and might lose a pointless mixed sublocale.

**Check.** Open and corresponding closed sublocales satisfy \(F\vee U=Z\) in \(\mathcal S(Z)\). Since \(\mathcal S(Z)\) is a coframe and therefore distributive, any \(G\) satisfies \(G=(G\wedge F)\vee(G\wedge U)\). This is a sublocale identity. **Pass.** Verify directly by nuclei if a referee doubts the complement convention.

### I. Does the Cantor infinite-join witness really work?

**Threat.** \(P\) is pointless, and ordinary point computations alone can be misleading.

**Check.** The earlier externally refereed Cantor construction proves \(P\ne0\), all point sublocales \([p_F]\) fitted, and F nonfitted. As K is spatial, the join of its point sublocales is the entire closed sheet F. The theorem yields \(\operatorname{Sat}(F)=F\vee P_U>F\), whereas the join of the individual saturations is F. **Pass**, conditional on the cross-sheet computation already audited above.

### J. Boundary controls

- Disjoint sheets \(L=\mathcal O(K)^2\): global \((1,0)\) makes \(P=0\), and the theorem specializes to \(\operatorname{Sat}=\operatorname{fit}=\mathrm{id}\).
- Sierpiński-style sheets \(L=\{(c,v):c\le v\}\): \(P=K\), giving the expected directional first-to-second saturation.
- Cantor discrete-defect sheets: P is a nonzero pointless remnant; the same formula applies without collapsing the relation to ordinary specialization.

These test opposite ends of the remnant parameter. They are sanity checks, **not** exhaustive computation or an independent substitute for proof.

## 3. Logical dependencies and remaining risks

1. **A-SC canonical relation:** The generalized-point characterization of \(\mathcal A\) was independently audited earlier in the project and is assumed here. If conventions differ in the referee's framework, every cross-sheet assertion must be translated explicitly.
2. **Fitness theorem:** Regular \(\Rightarrow\) fit and fit \(\Leftrightarrow\) all sublocales are meets of open sublocales are sourced to primary frame-theory papers. The proof does not presume every sublocale is spatial.
3. **Sublocale coframe:** Finite distributivity and open/closed complementation are standard. Infinite join-preservation is emphatically *not* used.
4. **Generality:** The theorem requires a literal subframe \(L\subseteq\mathcal O(K)^2\), coordinatewise operations, the open second sheet, and the complete diagonal clopen family. No claim for arbitrary gluing interfaces without these hypotheses.
5. **Novelty:** Not researched exhaustively. Even a correct theorem may have a standard reformulation or precedent.

## 4. Internal conclusion and referee targets

The strengthened theorem is **internally provisionally accepted**. I found no circular step or unjustified topological-to-localic upgrade. The two most important blind-audit requests are:

(i) reconstruct the generalized-point cross-sheet calculation, including globalization of an arbitrary \((c,v)\); and

(ii) scrutinize the relative-to-ambient fitting and sublocale coframe splitting, with a genuine counterexample attempt if either seems suspect.

Only after external evaluation should the result be marked verified and the agreed narrow comparison of the next two research priorities begin.
