# Project A / C — Internal adversarial audit of the Dowker phase

**Date:** 10 November 2026  
**Status:** Internal mathematical review only; no external referee has assessed the new statements.  
**Source period:** Session 5 (specialization graph powers), Session 6 (higher diagonal hulls, localic rectangle nerves, descent, frame-cover nerves).  
**Scope:** Actual localic sublocales, spectral representation, point-free Čech complexes, proper/triquotient/open surjections, homotopy realizations, functoriality, and illustrative examples.  
**Literature priority:** Not evaluated. The bisimplicial rectangle method is known from Brun–Salbu and Brun–Fosse–Salbu; effective descent of open/proper surjections is classical.

## Executive verdict

No fatal error was found in the central **unrestricted frame-theoretic formulas** or in the **finite-limit Čech-nerve identities**. The elementary open-cover construction produces open surjections in both directions in the usual classical metatheory. The coherent specialization constructions and the one-sequence nontriquotient example passed this internal line-by-line examination, though they rely on deeper spectral-localic identifications that should be independently checked. The patched and unpatched sheaf-homotopy comparisons are **conditional on an explicitly chosen site and its effective-epimorphism topology**. They must not be presented as statements about intrinsic localic shape, classical geometric realization of spectral spaces, or weak equivalence in an unspecified model structure on simplicial locales.

**Priority for external audit:** (1) the spectral-to-actual-localic properness argument; (2) the Priestley nontriquotient counterexample and the two Frobenius calculations; (3) the exact ∞-topos/sheafification setup, including recovery of classical homotopy; (4) unbounded frame-cover/pointless details and exact claim of all-locale constructive generality.

## 1. Foundation: higher diagonals and their simplicial maps — PASS internally

For arbitrary locale X and n≥1 let Δ_n↪X^n be its n-fold diagonal and I^(n)=cl Δ_n, D^(n)=fit Δ_n. Use the order convention for sublocales: ≤ means containment. Any coordinate deletion or duplication map c:X^n→X^m carries Δ_n into Δ_m. For each *closed* sublocale C⊇Δ_m, the inverse-image c⁻¹(C) is closed and contains Δ_n, hence I^(n)≤c⁻¹(C); therefore c(I^(n))≤cl Δ_m. Likewise for every open O⊇Δ_m, its inverse-image is open containing Δ_n; D^(n)≤c⁻¹(O), hence c(D^(n))≤fit Δ_m. This proves the simplicial structures without relying on false general preservation of hulls by direct images.

For coherent X, the spectral points of these sublocales are the tuples with a common upper, respectively common lower, specialization bound. The exact sublocale conclusion uses the already externally checked coherent proconstructible hull representation (C08/C10/C11; see canonical composition proof). **Dependency**: do not infer actual sublocale equalities merely because the ordinary point sets agree.

## 2. Universal cover-nerve formulas — PASS internally

With L=O(X), write a_1⊠···⊠a_n for the rectangle in O(X^n). For each indexed cover U=(u_i), define

- b_U^(n)=∨_{i_1,...,i_n: ∧_j u_{i_j}=0}(u_{i_1}⊠···⊠u_{i_n}), the missing-simplex open;
- w_U^(n)=∨_i(u_i⊠···⊠u_i), the common-cover-member open.

Then

    I^(n)= ⋀_{U cover} C(b_U^(n)),
    D^(n)= ⋀_{U cover} O(w_U^(n)).

Closed formula: the largest open d_n annihilated by Δ_n^* is the join of all rectangles having zero meet in L; such rectangles appear in some b_(a_1,...,a_n,1). Taking C(d_n) produces cl Δ_n. Fitted formula: every rectangle decomposition of an open w with Δ_n^*(w)=1 yields a cover c_t=∧_j a_(t,j) with w_(c_t)^(n)≤w; all open neighborhoods of Δ_n therefore contain a special common-member neighborhood. Both are genuinely localic equalities, no points required.

Moreover, a labelled ordered tuple (i_1,...,i_n) is a simplex of N(U) iff I^(n)∧O(u_{i_1}⊠···⊠u_{i_n})≠0. This uses the fact that Δ_n is dense in its closure. **Keep labels:** abstract simplicial isomorphism types alone cannot reconstruct the actual sublocale.

## 3. Coherent finite compact-open reduction — PASS internally, citation scope explicit

If X is coherent, 1 and finite meets of compact opens are compact. Every zero-meet open rectangle is a join of zero-meet compact rectangles, and each such tuple is included in a finite compact-open cover by adjoining 1. Likewise, every open cover admits a finite cover by compact opens refining it. This proves both arbitrary-cover formulas using only finite compact-open covers. The patch-closed spectral descriptions follow using standard Priestley/coherent representation. The check should explicitly separate compactness of X from local compactness (which is not enough for a *finite* cover in this form).

## 4. General bisimplicial rectangle and Čech identities — PASS internally

For a localic relation R↪X×Y define E_{p,q}=⋀_{i≤p,j≤q}π_{ij}^{-1}(R) in X^{p+1}×Y^{q+1}; let K_p and L_q be the images under the two witness-forgetting projections. Then

    E_{p,q} ≅ (E_{p,0})^{×_{K_p}(q+1)},
    E_{p,q} ≅ (E_{0,q})^{×_{L_q}(p+1)}.

Reason: K_p↪X^{p+1}, L_q↪Y^{q+1} are monos, and the corresponding fiber powers impose exactly the displayed finite intersections. No associativity of arbitrary localic relation composition is used. Surjectivity of the image-factor maps is by definition, **but arbitrary surjections need not be descent covers**, so none of the later homotopy results follows from these identities alone.

The comparison with Brun–Fosse–Salbu is exact at the *object of internal rectangles* after replacing sets by the internal pair/chaotic categories Pair(X), Pair(Y), Pair(R); it does not import the paper's weak equivalence theorem into Loc. Verified distinction: using posets themselves as categories instead produces ordinary order-complex nerves and can yield different homotopy types (four-point K_(2,2) poset test).

## 5. Coherent specialization witness maps — PASS relative to spectral-image inputs; priority E

For R=A oriented specialization (x≤y), K_p=I^(p+1) and L_q=D^(q+1) in coherent locales. The maps r_p:E_{p,0}→K_p are claimed proper surjections. Source is spectral and map spectral; inverse image preserves compact opens, hence the right adjoint preserves directed joins (semiproper/perfect). To show the map *closed in Loc*, take any closed sublocale C of E_{p,0}; its points form patch-closed downset. Projection yields patch-closed points by compactness. If x'≤x coordinatewise, a witness y above x remains above x', and (x',y)≤(x,y) lies in C. Hence the image is downward closed and spectral closed. The canonical coherent image theorem identifies the **actual image sublocale** with that closed spectral subspace. A closed + semiproper spectral map is proper, so Vermeulen applies.

**Independent audit obligation:** check the passage 'image of any closed sublocale is identified by its patch point set', including whether the closed sublocale of E_{p,0} is spectral and whether the image theorem applies as asserted. Mere topological closedness does not suffice unless the localic image is known to match the spectral image.

Opposite maps s_q:E_{0,q}→L_q: q=0 always has the diagonal section and is triquotient. For finite Alexandrov spaces each s_q is open, hence triquotient. Not all coherent s_q are open or proper. The elementary three-point fork gives s_0 nonproper.

## 6. Countable coherent nontriquotient example — PASS internally; priority E

Patch space P={a,d,c,b_∞}∪{b_n:n≥1}, with b_n→b_∞ and a,d,c isolated. Strict order:

    a<b_n (all n),  a<b_∞,  a<c,
    d<b_∞,  d<c.

This is a Priestley space. Its order is patch closed. Clopen upsets separating points include P\{d}=↑a, P\{a}, singleton b_n and c, tails of maximal b's, and {d,c,b_∞} plus any sufficiently long b-tail. All excluded comparison pairs can be separated.

For q≥1 in B_q=D^(q+1), set y=(d,...,d), z=(b_∞,c,...,c), y_n=(b_n,c,...,c). They lie in B_q; y≤z and y_n→z in patch, so y_n→y in spectral topology. Fibers: W(y)={d}, W(y_n)={a}, W(z) contains {a,d}. Set U=P\{a}, a clopen upset, and O⊆E_{0,q} the open requiring witness x∈U. O contains the whole y-fiber and misses all y_n-fibers. Since y is minimal and patch-isolated, {y} is spectral closed; W=B_q\{y} is open, and O∨s_q^*(W)=1. Each y_n is patch-isolated maximal in B_q, so V_n={y_n} is compact spectral open, and O∧s_q^*V_n=0.

Any Plewe assignment s_# satisfies both Frobenius identities, s_#0=0, s_#1=1. The second identity gives 1=s_#(O)∨W, hence y∈s_#O. The first gives s_#O∧V_n=s_#0=0, hence y_n∉s_#O. Contradicts y_n→y. This is genuinely localic, provided the equality of opens O∨s_q^*W=1 (and emptiness over V_n) is justified by spatiality of the proconstructible spectral source. That is the key independent check.

This is a counterexample to triquotiency only; **do not infer failure of effective descent**.

## 7. Patch-localic homotopy comparison — CONDITIONAL PASS; category must be precise

For coherent proconstructible R, E_{p,q}, K_p,L_q are spectral proconstructible locales; after patching they are Stone. Finite fiber products correspond to the obvious patch-closed subsets of finite Stone powers. Patched r_p,s_q are surjective compact-Hausdorff maps, hence proper effective-descent maps of locales. Define a small Grothendieck site of Stone locales with the topology generated by surjective maps (or a suitable universe-bounded site containing the diagrams and their pullbacks), and let H be its ∞-topos of space-valued sheaves. Denote representable sheaves by h. Then

    |h(Patch K_•)| ≃ |h(Patch E_{•,•})| ≃ |h(Patch L_•)|

because each patched Čech nerve becomes the effective-epi Čech nerve in H and geometric realizations commute. This is an **equivalence of objects of H**, not a weak equivalence of original spectral simplicial locales, and certainly not automatically an equivalence of their intrinsic localic shapes.

**Critical clarification:** 'recovers ordinary Dowker equivalence' for finite discrete point sets requires identifying finite discrete representables with finite coproducts of the terminal object in the chosen ∞-topos, and explaining how to evaluate or compare the resulting constant simplicial spaces. Formal bicomplex descent alone does not imply an intrinsic shape theorem. This must be spelled out in the audit packet or downgraded to a contextual remark.

## 8. Open-cover relations and unpatched two-sided descent — PASS (classical metatheory)

For an indexed family (u_i) in O(X), let I_d be the discrete locale and R_U=∐_i O(u_i)↪I_d×X. Then

    E_{p,q}=∐_{(i_0,...,i_p)} O(∧_{k=0}^p u_{i_k})^{q+1},
    K_p={ (i_0,...,i_p):∧_k u_{i_k}≠0 }_d,
    L_q=O(∨_i ∧_{j=0}^q π_j^*u_i)⊆X^{q+1}.

The map s_q:E_{0,q}→L_q is an open-cover coproduct map and hence open surjective. The map r_p has discrete target K_p and components O(∧u_{i_k})→1. Over ordinary classical Set, any nonzero locale→1 is an open surjection (its left adjoint is the positivity/nonzero predicate). **Constructive qualification:** nonzero alone need not imply overtness; do not silently advertise this argument as constructive. For the stated ordinary classical point-free project it is valid. Both directions are open effective descent, without coherence or passage to patches. The sheaf-theoretic homotopy equivalence is conditional on the same specified ∞-topos construction as in §7.

A single cover nerve cannot recover shape(X). For the one-member cover (1) of any nonzero X, K_• is terminal, L_q=X^{q+1}, and L_• is the Čech nerve of X→1. Thus its realization in the *open-surjection sheaf ∞-topos* is terminal regardless of intrinsic homotopy of X. This distinction is a central substantive interpretation warning, not a minor editorial footnote.

## 9. Refinement, pointless example, and simplicial span — PASS with stated limitations

For a specified refinement V≼U, K_•(V)→K_•(U) is induced by the index assignment and L_•(V)⊆L_•(U) by cover refinement. Distinct index choices yield *contiguous* maps on discrete simplicial nerves, hence agree in the homotopy category, but no homotopy-coherent functor on an ∞-category of unchosen refinements has been constructed.

For complete atomless Boolean L=RO(S¹), the 3-arc cover has nerve ∂Δ² while all covers admit disjoint refinements via v_i=u_i∧¬(∨_{j<i}u_j). This gives a cofinal system of discrete nerves. Therefore its **chosen-cover** S¹ nerve is not an invariant of the locale's shape. Over a classical metatheory, the nonzero pointfree components of the cover relation still give open surjections.

For each cover U and n≥1, define Q_(n−1)(U)=I^(n)×_{X^n}(T_U)^n, T_U=∐O(u_i)→X. The right map to I^(n) is an open surjection by pullback/product of the open cover; its components map to the discrete K_(n−1)(U) nontrivially iff the corresponding tuple is a nerve simplex, giving the left open surjection. Coordinate deletion/repetition gives a genuine simplicial span K_•(U)←Q_•(U)→I^(•+1). **But degreewise open surjections do not imply realization equivalences**. A two-point discrete X and cover (1) refute that shortcut.

## 10. Process-level and editorial corrections requested

1. Use `n≥1` consistently for higher diagonals (binary hierarchy starts at n=2); clarify indexing q=n−1.
2. State all 'all-locale' positive assertions in classical mathematics. If aiming for constructive/geometric validity, the map nonzero locale→1 requires an overtness/positivity hypothesis; some proof steps use classical prime-filter extensions.
3. State explicitly where a spectral description determines the *actual* sublocale, especially proper-row proofs and the nontriquotient example.
4. Define the site, size/universe, representable h, and the category where geometric realizations exist. Do not abbreviate a site equivalence to 'point-free homotopy type of X'.
5. The formal ∞-topos theorem should be labeled as a deduction in a fixed setting; it is not a published theorem of Brun–Fosse–Salbu and is not a property of all surjective localic maps.
6. Give the one-element cover as a standing limitation on proposed localic nerve lemmas.
7. Do not claim the b_U nonface tests are monotone under arbitrary refinement; concatenation enlarges b_U, while intersection refinements decrease w_U.
8. Treat relation-induced simplicial objects as the *full ordered-tuple simplicial sets/locales* (repetitions allowed); the nondegenerate abstract nerve is the corresponding simplicial complex.
9. Clearly identify the 2023 categorical rectangle nerve and the earlier Brun–Salbu construction as provenance; de Silva et al. (2025/2026) treat multiway relations; Chowdhury–Mémoli (2018) treat naturality.
10. Keep 'passed internal audit' distinct from 'externally certified' and from any literature-priority claim.

## External referee audit architecture

Recommended independent clusters, in order:

**A. Frame and simplicial algebra:** higher diagonal hulls, nonfaces and cover witnesses, finite compact-open reduction, simplicial structure, natural span and counterexamples.

**B. Localic Čech, descent and homotopy:** internal rectangle identities; coherence/properness; patching; open-cover two-sided descent; ∞-topos definition and actual meaning of the equivalence.

**C. Obstructions and literature:** nonopen/nonproper witnesses, coherent nontriquotient example, missing shape inference, Brun–Fosse–Salbu internalization and priority limits.

Prepare a **blind self-contained packet** with statements and proposed proofs, but *omit this internal audit and its verdicts*. Ask for correctness grading by claim and explicit identification of counterexamples, missing hypotheses, transfer-to-actual-locales failures, and source-versus-new distinctions. Invite an independent simpler proof of an individual claim or falsification of any remark.

## Source paths

- [Specialization and graph powers](https://github.com/mkkinyon/locales/blob/main/ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md)
- [Coherent composition canonical proof](https://github.com/mkkinyon/locales/blob/main/ProjectA_coherent_composition_canonical_proof_2026-11-08.md)
- [Bisimplicial Čech and patch descent](https://github.com/mkkinyon/locales/blob/main/ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md)
- [Triquotient counterexample](https://github.com/mkkinyon/locales/blob/main/ProjectA_Dowker_witness_triquotient_counterexample_2026-11-10.md)
- [Brun–Fosse–Salbu crosswalk](https://github.com/mkkinyon/locales/blob/main/ProjectA_Brun_Fosse_Salbu_Dowker_crosswalk_2026-11-10.md)
- [Frame-cover open descent](https://github.com/mkkinyon/locales/blob/main/ProjectAC_frame_cover_Dowker_open_descent_2026-11-10.md)
- [Higher diagonal reconstruction](https://github.com/mkkinyon/locales/blob/main/ProjectAC_higher_diagonal_cover_nerve_reconstruction_2026-11-10.md)
- [Original Project C plan](https://github.com/mkkinyon/locales/blob/main/C-frame-nerves.md)

**Final internal disposition:** No broad retraction recommended at this stage. Maintain all major claims as *working*, and submit the categorical/descent/pointfree-to-spectral interfaces for an independent blind review before incorporating into the externally verified ledger.