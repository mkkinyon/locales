# A — Verification of lower-point plank supplement (21 October 2026)

**Status:** second-pass independent check of Claude's supplement *Plank with lower points: sobriety and compact opens* (provided by user 21 Oct), extending the external-audit §3.4 construction. This note is an assessment, not a claim of novelty.

Let T be the deleted Tychonoff plank, with disjoint closed A,B and compact-open basis. Index finite nonempty S⊆A or S⊆B, never mixed; adjoin z_S. Define O⊆X open iff V=O∩T is open, z_S∈O⇒S⊆V and z_R∈O for all nonempty R⊆S. Basic neighborhoods N(S,V)=V∪{z_R:∅≠R⊆S}, V T-open containing S.

## Checked proofs

**Specialization:** cl_X{t}={t}∪{z_S:t∈S}; cl_X{z_R}={z_S:R⊆S}. Computed directly from the neighborhood bases.

**Sobriety: VERIFIED.** For an irreducible closed C, disjoint T-open neighborhoods exclude two distinct T-points. If C contains t∈T, every z_R∈C must have t∈R (otherwise t,z_R can be separated), hence C=cl{t}. If C⊆Z, it lies in one of Z_A,Z_B (disjoint-index neighborhoods). For z_R,z_R'∈C irreducibility yields z_S∈C with ∅≠S⊆R∩R'. Choose R with smallest finite cardinality among C's indices; then R⊆R' for all z_R'∈C, whence C=cl{z_R}. T0 gives unique generic points.

**Compact opens: VERIFIED.** For an OPEN O, compact iff O∩Z finite and O∩T compact in T. Compactness forces finite Z using cover by T and N(S,T), each covering finitely many Z-points. Given cover of O∩T by T-opens, build from finite subcovers of each finite S⊆O∩T a basic neighborhood of z_S∈O; compactness of O yields finite original T-open subcover. Conversely compact trace and finitely many Z-points give compact O. This equivalence need not hold for arbitrary *nonopen* compact sets.

**Arithmetic and algebraic: VERIFIED.** Compact-open traces are compact subsets of Hausdorff T, hence closed and closed under finite intersections; finiteness of added points is preserved. Every t∈T has a compact-open local basis. Every z_S has compact-open neighborhoods N(S,W) where W is a finite union of compact-open T-neighborhoods of points in S. Thus O(X) is algebraic, arithmetic, continuous, locally compact sober and not compact (infinitely many added points).

## Remaining Ury=Cm check (independent derivation)

For any open O⊆X, write V=O∩T. Its closure has T-trace cl_T(V), and z_R belongs to cl_X(O) iff R∩cl_T(V)≠∅. The converse direction of the iff uses finite R and regularity of T to choose a T-open W⊇R disjoint from V if R misses cl_T(V). If an added z_S belonged to O∩N(R,W), then S⊆R and S⊆V, contradicting R∩V=∅. This reproduces the closure formula quoted in external audit §3.4.

Consequently the ordinary closure-meeting (Cm) classes are A∪Z_A, B∪Z_B, and singleton t outside A∪B. Within each A/B class common lower witnesses are z_{S∪R}; for mixed A/B classes closures cannot meet.

To far-separate distinct Cm classes, use finite supports S and R, regularity of T, and closedness/disjointness of A,B. Choose the T-parts V,W of neighborhoods so cl_T(V)∩cl_T(W)=∅, with an additional buffer: (i) A-vs-B classes: cl_T(V)∩B=∅ and cl_T(W)∩A=∅; (ii) any singleton outside A∪B: its neighborhood closure misses A∪B. Then no index lying wholly in A or B meets *both* closures, so cl_X neighborhoods are disjoint. Thus Ury=Cm for original pairs. Since X is locally compact sober and its localic square is spatial, closed U is point-determined and the original-point criterion yields **D=U as localic sublocales**.

For any continuous f:X→ℝ, z_{ {a,a'} } below a,a' forces f(a)=f(a'), and similarly on B. The deleted-plank lemma forces the constants on A and B to coincide. A and B are different Cm classes and U-distinguishable; therefore U⊊F, hence **D=U=fit(U)⊊F**.

**Assessment:** Main sobriety and compact-open supplement is independently verified; the additional Ury=Cm and functional steps have now been checked at a direct argument level. Full publication-ready exposition should explicitly prove the displayed closure formula and the buffered-neighborhood separation, not merely assert 'regularity separates the classes'. The original Claude audit's machine-verification and novelty are not independently verified in this note.
