# Project A / C — Technical packet for a blind Dowker-phase audit

**10 November 2026 — working claims, proposed proofs, and examples. Not externally audited.**  
**READ the accompanying blind referee prompt first.** This packet intentionally contains no internal-audit verdicts or reconciliation notes.

## 0. Motivation, notation, provenance

The project's original motivation is Cameron–Kumar, *Graphs on topological spaces*, arXiv:2610.14783. Project A examines genuinely localic separation relations (sublocales of a locale square); the originally reserved Project C examines frame-cover nerves, point-free Dowker duality, and homotopy. The recent work links them using higher diagonals and common-witness bisimplicial locales.

We work classically unless explicitly stated otherwise. `Loc` is the category of locales and locale maps; `O(X)` is the frame of opens. `S≤T` means sublocale inclusion. For a frame element a∈O(X), `O(a)` is the open sublocale and `C(a)` its complementary closed sublocale. `cl(S)` is the smallest closed sublocale containing S, and `fit(S)` the meet of all open sublocales containing S. Sublocale meets in formulas are actual sublocale intersections. `im(f)` is the localic image, not merely the image of ordinary points. For an n-fold power X^n, denote `a_1⊠···⊠a_n = ⋀_j π_j^*(a_j)`. These rectangles join-generate O(X^n).

A **coherent locale** is represented by a spectral space P with compact Hausdorff Priestley patch topology, a specialization order, and a basis of compact opens. Convention: x≤y iff x belongs to the closure of {y}; hence opens are upward closed. For coherent locales, the project's already externally audited **proconstructible composition calculus** says that certain patch-closed subspaces and their localic relations are genuine proconstructible sublocales; spectral image calculations for these objects are valid actual localic-image computations. The same calculus establishes that, for such a proconstructible S⊆X², `cl(S)=A∘S∘B`, `fit(S)=B∘S∘A`, where A is the oriented specialization relation and B=A^smile. Full prerequisite: [Coherent composition canonical proof](https://github.com/mkkinyon/locales/blob/main/ProjectA_coherent_composition_canonical_proof_2026-11-08.md). Outside this class, localic relation composition need not associate; never assume it does.

Published/background sources: Dowker duality; Cameron–Kumar; Brun–Salbu and Brun–Fosse–Salbu *Dowker Duality for Relations of Categories* (arXiv:2303.16032); Joyal–Tierney on effective descent of open surjections; Vermeulen on proper localic maps/effective descent; Plewe *Localic triquotient maps are effective descent maps* (1997); de Silva et al. *Dowker's theorem for higher-order relations* (arXiv:2506.10909; journal 2026); Chowdhury–Mémoli *A functorial Dowker theorem...* (arXiv:1608.05432). These are references, not claims of novelty for their techniques.

## 1. The specialization graph and finite powers (context)

Let `A↪X×X` be the greatest sublocale imposing `π_1^*(a)≤π_2^*(a)` for all a∈O(X), with `B=A^smile`. Define the reflexive symmetric specialization relation `S=A∨B`. Universal claims include

    Δ≤S≤I∧D,    cl(S)=I,    fit(S)=D,

where `I=cl Δ`, `D=fit Δ`; the last two follow by monotonicity and idempotence of hulls. In coherent locales, audited relation-composition inputs include

    A²=A, B²=B,  AB=I,  BA=D,  I²=U=cl(D), D²=V=fit(I).

All those compositions associate and distribute over finite joins in the particular proconstructible class. Thus

    S²=I∨D=:J,    S⁴=U∨V,
    S^{2n}=I^n∨D^n    for every finite n≥1.

This follows by expanding powers of A∨B and deleting adjacent equal A or B letters. The full general finite-alternating-word identity is equation (7.9) of the prerequisite coherent composition canonical proof. This graph-power material supplies context; the main subject of the current packet begins in §2.

## 2. Higher diagonal hulls and simplicial structures

Let Δ_n:X→X^n be the n-fold diagonal for n≥1. Define

    I^(n)(X)=cl(Δ_n),    D^(n)(X)=fit(Δ_n).

For n=2 these are I and D. Coordinate deletion and coordinate repetition maps of cartesian powers carry diagonals to diagonals. For a map c:X^n→X^m of either type, if a closed sublocale F⊆X^m contains Δ_m, then c^{-1}F is closed and contains Δ_n. Therefore I^(n) maps into F and hence I^(m). The analogous argument using open sublocales proves D^(n) maps into D^(m). These degreewise maps satisfy the simplicial identities, yielding simplicial locales `I^(•+1)` and `D^(•+1)` in any locale.

**Coherent point-description claim.** If X is coherent with spectral points P, the patch point sets of these genuinely proconstructible sublocales are

    pt(I^(n)) = { (x_1,...,x_n): ∃ z∈P, x_i≤z for every i },
    pt(D^(n)) = { (x_1,...,x_n): ∃ z∈P, z≤x_i for every i }.

Proof sketch: Δ_n is proconstructible; its downward product-order saturation gives the closure, and its upward saturation gives fitting, by the coherent hull calculus and compact patch representation. These are localic equalities only because the participating sublocales lie in the proconstructible class.

**Example distinguishing n=3 from n=2.** Let P consist of minima a,b,c and maxima t_ab,t_bc,t_ca with only a,b<t_ab; b,c<t_bc; c,a<t_ca. Each pair among a,b,c has a common upper bound, but all three do not. Thus pairs lie in I^(2) while (a,b,c)∉I^(3). Order duality gives the corresponding D^(3) example.

## 3. Localic rectangle nerve and strict Čech descriptions (arbitrary R)

For any localic relation `R↪X×Y`, define

    E_{p,q}(R) = ⋀_{0≤i≤p,0≤j≤q} (π_{ij})^{-1}(R)
                   ↪X^{p+1}×Y^{q+1},             (p,q≥0).

The coordinates are tuples (x_0,...,x_p ; y_0,...,y_q), with all x_i R y_j. Face and degeneracy maps delete/repeat X or Y coordinates, making E bisimplicial. Set

    K_p(R)=im(E_{p,0}→X^{p+1}),
    L_q(R)=im(E_{0,q}→Y^{q+1}).

These form simplicial sublocales. Let r_p and s_q denote the corresponding image-factorization maps, which are surjective by definition of image.

**Claim 3.1 (all-locale exact Čech identities).** For each p,q,

    E_{p,q} ≅ (E_{p,0})×_{K_p}⋯×_{K_p}(E_{p,0})      (q+1 factors),
    E_{p,q} ≅ (E_{0,q})×_{L_q}⋯×_{L_q}(E_{0,q})      (p+1 factors).

Proof: K_p↪X^{p+1} and L_q↪Y^{q+1} are monomorphisms. Fiber products over them equal the fiber products over their ambient powers, imposing exactly every R condition in the defining formula. Thus the rows/columns are the Čech nerves of r_p/s_q. This assertion is independent of coherence, image pullback stability, and associativity of arbitrary relation composition.

**Categorical crosswalk.** For a locale Z let Pair(Z) denote its internal pair/chaotic category with objects Z and arrows Z×Z. The functor Pair(R)→Pair(X)×Pair(Y) is an internal relation of categories. The objects of its (p,q)-rectangles are precisely E_{p,q}(R), because a functor [p]×[q] into a pair category is determined by its array of objects, and factorization of the base functor forces the (i,j)-object to be (x_i,y_j)∈R. This is the internal-locale version of the rectangle nerve of Brun–Fosse–Salbu; it does **not** by itself assert a homotopy equivalence of simplicial locales.

For a coherent proconstructible R, taking spectral points yields the usual rectangle bisimplicial set for chaotic categories on the sets of points. A nonempty common-witness set has contractible chaotic nerve; this recovers the ordinary pointwise Dowker equivalence. In contrast, if P is made into its **order category** and R is the full subcategory on x≤y, the two nerves are ordinary order-complex nerves NP rather than arbitrary-common-witness complexes. Example: for the four-point poset with two minima a,b, two maxima c,d, and a,b<c,d, NP is a circle (four edges), whereas the two common-witness complexes are each the union of two triangles along an edge, hence contractible.

## 4. Specialization witness projections: properness and its limits

In coherent X take R=A, the oriented specialization relation. Then the coherent point-description and the proconstructible image theorem identify

    K_p(A)=I^(p+1),   L_q(A)=D^(q+1).

Here r_p:E_{p,0}(A)→I^(p+1) forgets a *common upper* witness y with x_i≤y; s_q:E_{0,q}(A)→D^(q+1) forgets a *common lower* witness x with x≤y_j.

**Claim 4.1 (proper-row proposition).** For every p≥0 and coherent X, r_p is a proper surjection of locales.

Proposed proof: r_p is spectral between coherent locales, since all relevant relation sublocales and images are proconstructible. Spectral maps preserve compact opens under inverse image, hence their right adjoints preserve directed joins (perfect/semi-proper). For a closed sublocale C of E_{p,0}, its spectral point set is patch-closed and downward closed. The projected point set is patch-closed by compactness. It is downward closed: if ((x_i),y)∈C and x_i'≤x_i for all i, then ((x_i'),y)≤((x_i),y) and belongs to C, so ((x_i')) belongs to the image. A patch-closed downset is spectral-closed. By the coherent proconstructible image theorem this is equality of the **actual image sublocale**, so r_p is a closed localic map. Closedness plus perfection gives properness; surjectivity is definitional. Vermeulen's theorem makes these proper surjections effective-descent maps.

**Claim 4.2.** For *every* locale X, s_0:A→X has the diagonal section and is triquotient. For finite T0 Alexandrov X and all q, s_q is open surjective and thus triquotient. Indeed the witness x≤y_j remains a witness after coordinatewise generalizing y_j to y'_j≥y_j; in finite upper-Alexandrov topologies this going-up property gives openness.

**Finite nonproper example.** Let P={a,b,t}, with a<t,b<t and a,b incomparable. For s_0:A→P, the closed downset of (a,t) in A has image {a,t}, not a closed subset of P because b≤t. Thus s_0 is not generally proper.

**Coherent nonopen example.** Take patch space comprising three disjoint convergent sequences a_n→a_∞, b_n→b_∞, c_n→c_∞ plus isolated d. Let a_n<b_n,c_n; a_∞<b_∞,c_∞; d<b_∞,c_∞, with no other comparisons. Claim it is Priestley. The patch-clopen upset U={d}∪{b_n,b_∞}∪{c_n,c_∞} is a compact spectral open. In E_{0,1}, let O require the lower witness to lie in U. The image under s_1 contains (b_∞,c_∞), by d, but excludes (b_n,c_n), whose only lower witness is a_n. These pairs converge patchwise to (b_∞,c_∞), so the image of O is not open; s_1 is not generally open.

## 5. A countable coherent counterexample to triquotiency

Plewe's localic triquotient assignment for f:E→B is a directed-join-preserving map f_#:O(E)→O(B) satisfying for every u∈O(E), v∈O(B)

    f_#(u∧f^*v)=f_#(u)∧v,
    f_#(u∨f^*v)=f_#(u)∨v.

These imply f_#0=0, f_#1=1, f_#f^*=id. Triquotient maps are effective descent (Plewe), but the converse is not assumed.

**Claim 5.1 (same coherent X, every q≥1).** There is a countable coherent X for which every lower-witness map s_q:E_{0,q}(A)→D^(q+1) fails to be triquotient.

Construction: take compact Stone patch set P={a,d,c,b_∞}∪{b_n:n≥1}, with b_n→b_∞ and a,d,c isolated. The only strict comparisons are

    a<b_n (every n),  a<b_∞,  a<c,
    d<b_∞,  d<c.

The order is patch closed. Proposed clopen separating upsets include ↑a=P\{d}; P\{a}; singletons {b_n} and {c}; and {d,c,b_∞}∪{b_n:n≥N}, for sufficiently large N. Thus P is Priestley and yields coherent X.

Fix q≥1 and set B_q=D^(q+1). Define tuples of length q+1:

    y=(d,d,...,d),
    z=(b_∞,c,...,c),
    y_n=(b_n,c,...,c).

They belong to B_q. We have y≤z coordinatewise, and y_n→z in patch topology. Hence y_n→y in the spectral topology. The common-lower-witness fiber over y is {d}, over y_n is {a}, and over z contains both a,d.

Let U=P\{a}, a compact clopen upset. In E_{0,q}, let O be the open sublocale requiring witness x∈U. O contains the whole fiber over y and misses every fiber over y_n. Since y is a minimal, patch-isolated point of B_q, {y} is closed; put W=B_q\{y}, an open. Then, as actual opens of E_{0,q},

    O∨s_q^*(W)=1.

Every y_n is isolated and maximal in B_q, hence V_n={y_n} is compact spectral open; and

    O∧s_q^*(V_n)=0.

If a triquotient assignment s_{q#} existed, the second Frobenius equation would yield

    1=s_{q#}(1)=s_{q#}(O)∨W,

so y∈s_{q#}(O). The first would yield

    s_{q#}(O)∧V_n=s_{q#}(0)=0,

so no y_n∈s_{q#}(O). This contradicts y_n→y and openness of s_{q#}(O). Thus no triquotient assignment exists.

**Scope of the proposed conclusion:** not triquotient does **not** imply not effective descent. The example concerns coherent spectral locales and actual localic opens, rather than a merely pointwise condition.

## 6. A patched two-sided Dowker comparison

For coherent locales X,Y and a **proconstructible** relation R⊆X×Y, the locales E_{p,q}(R), K_p(R), L_q(R) are spectral/proconstructible. Their patches are Stone locales. The maps Patch(r_p),Patch(s_q) are surjections of Stone locales, hence proper surjections, and both are effective descent by Vermeulen.

**Claim 6.1 (patch Čech preservation).** The canonical maps

    Patch(E_{p,q}) → (Patch E_{p,0})×_{Patch K_p}⋯×_{Patch K_p}(Patch E_{p,0}),

and the transpose analog over Patch L_q, are isomorphisms. Proposed reason: each locale is represented by a patch-closed subspace of a finite product of compact Hausdorff patches; the underlying sets on both sides impose exactly the same coordinate constraints, and the corresponding topologies are the subspace patch topologies. Hence both patched directions are true Čech nerves.

**Claim 6.2 (sheaf-homotopy comparison).** Choose an appropriately universe-bounded site `Stone` with the Grothendieck topology generated by surjective maps of Stone locales; let H_Stone be the ∞-topos of space-valued sheaves and h the sheaf-representable embedding. Then

    |h(Patch K_•(R))| ≃ |h(Patch E_{•,•}(R))|
                         ≃ |h(Patch L_•(R))|     in H_Stone.

Sketch: representables preserve finite limits; proper-surjection covers are effective epimorphisms after sheafification. Each row/column of h(Patch E) is an effective-epi Čech nerve, so it realizes to the corresponding representable h(Patch K_p) or h(Patch L_q). The two iterated homotopy colimits commute. For R=A the K/L terms are the patched higher closed/fitted diagonals.

**What is NOT claimed:** an unpatched equivalence in Loc, ordinary geometric realization of spectral simplicial spaces, or intrinsic equivalence of X's locale shape. For finite posets the patches are finite discrete locales; comparison with the usual set-level Dowker equivalence requires the appropriate interpretation of finite discrete representables as constant finite objects in this sheaf ∞-topos.

## 7. Frame-cover relation and unpatched effective descent

Let X be any locale with frame L, and let U=(u_i)_{i∈I} be an indexed family of frame elements; assume ∨_i u_i=1 when calling it a cover. Write I_d for the discrete locale on I. Define the open relation

    R_U = ∐_{i∈I} O(u_i) ↪ I_d×X.

For p,q≥0, the following localic identifications are proposed:

    E_{p,q}(R_U)= ∐_{(i_0,...,i_p)∈I^{p+1}} O(∧_{k=0}^p u_{i_k})^{q+1},

    K_p(R_U)= { (i_0,...,i_p): ∧_{k=0}^p u_{i_k}≠0 }_d,

    L_q(R_U)=O(w_U^(q+1)),
      w_U^(n)= ∨_{i∈I} ⋀_{j=1}^n π_j^*(u_i) ∈O(X^n).

Here the K_p are **discrete locales** whose underlying simplicial set is the ordered-tuple nerve of the cover; repetitions are allowed. If U is a cover, L_0=X.

**Claim 7.1 (all-locale open-cover descent).** Every r_p:E_{p,0}→K_p and s_q:E_{0,q}→L_q is an *open surjection*, without coherence/spatiality assumptions (in a classical metatheory).

Proof: each r_p component over a nonzero index tuple is O(v)→1 with v=∧u_{i_k}≠0. In classical mathematics every nonzero locale→1 is open surjective, with existential left adjoint the nonzero-open predicate. Hence r_p is an open surjection over the discrete target. Each s_q is the canonical coproduct of open inclusions O(u_i)^{q+1} into X^{q+1}, followed by its open union L_q, so it is open surjective. Joyal–Tierney effective descent now applies to both directions.

**Claim 7.2 (unpatched frame-cover Dowker comparison).** In a suitable ∞-topos H_op of space-valued sheaves on a universe-bounded locale site for the open-surjection topology,

    |h(K_•(R_U))| ≃ |h(E_{•,•}(R_U))| ≃ |h(L_•(R_U))|.

The same Čech descent + Fubini colimit argument as §6 is proposed. This is a *selected-cover* result. Taking U=(1) gives K_•=1, L_q=X^{q+1}; the latter is the Čech nerve of the open-surjection X→1 for X≠0, hence realizes to terminal in H_op even when X itself has nontrivial independent homotopy/shape. No localic nerve lemma is inferred.

**Refinement/naturality claim.** A specified refinement V=(v_j)_{j∈J} of U, with v_j≤u_{α(j)}, yields K_•(V)→K_•(U) and canonical degreewise inclusions L_•(V)↪L_•(U). The latter depend only on V,U, not α. Two choices α,β induce *contiguous* maps of ordinary nerves: if (j_0,...,j_p) spans a simplex, the nonzero ∧_k v_{j_k} lies below all u_{α(j_k)} and u_{β(j_k)}, so the union of image vertex sets spans a simplex. Thus the induced maps on ordinary realizations are homotopic; no homotopy-coherent refinement ∞-functor is claimed.

**Pointless example.** L=RO(S¹), the complete atomless Boolean algebra of regular-open subsets of a circle, has no completely prime points. Choose three regular-open arcs centered 120 degrees apart with half-width 75 degrees. They join to 1, pairwise meets are nonzero, and the triple meet is zero; their nerve is ∂Δ² with H_1=Z. However, every cover of a complete Boolean frame has a disjoint refinement: well-order the indices and put v_i=u_i∧¬(∨_{j<i}u_j). Thus disjoint covers are cofinal, and all their nerves are discrete. A single circle-shaped cover nerve does not imply that the pointless locale has circle shape.

## 8. Exact higher diagonal reconstruction from cover nerves

Let n≥2 and keep the arbitrary locale X and indexed cover U=(u_i).

Define the **missing-simplex open**

    b_U^(n)=∨_{(i_1,...,i_n): ∧_j u_{i_j}=0} (u_{i_1}⊠···⊠u_{i_n}),

and the **common-member open** w_U^(n) from §7.

**Claim 8.1 (arbitrary-locale reconstruction).** As actual sublocales of X^n,

    I^(n)= ⋀_{U open cover of X} C(b_U^(n)),
    D^(n)= ⋀_{U open cover of X} O(w_U^(n)).

**Proof for I^(n).** The largest open in X^n that restricts to zero on Δ_n is

    d_n=∨_{a_1,...,a_n∈O(X), ∧_j a_j=0}(a_1⊠···⊠a_n).

Thus I^(n)=C(d_n). Each b_U≤d_n. Conversely, every rectangle contributing to d_n appears in the nonface list for the cover U=(a_1,...,a_n,1), so d_n=∨_U b_U. Since C(∨b_U)=⋀_U C(b_U), the formula follows.

**Proof for D^(n).** The special open O(w_U^(n)) contains Δ_n, as Δ_n^*(w_U^(n))=∨_i u_i=1. Conversely, write any open w containing Δ_n as ∨_t(a_{t,1}⊠···⊠a_{t,n}); the family c_t=∧_j a_{t,j} covers 1, and w_(c_t)^(n)=∨_t c_t^{⊠n}≤w. Thus the special open neighborhoods are cofinal among *all* open neighborhoods of Δ_n, whose meet is fit Δ_n.

**Claim 8.2 (mutual reconstruction with labels).** For any indexed family U, not necessarily a cover, and tuple (i_1,...,i_n),

    (i_1,...,i_n) is a simplex of the ordered nerve
      iff ∧_j u_{i_j}≠0
      iff I^(n)∧O(u_{i_1}⊠···⊠u_{i_n})≠0.

Proof: Δ_n is dense in its closure I^(n), so an open of X^n meets I^(n) nontrivially iff it meets Δ_n nontrivially. Pullback of the indicated rectangle along Δ_n is ∧_j u_{i_j}. Actual opens/labels matter; one abstract unlabelled nerve does not determine I^(n).

**Claim 8.3 (coherent finite reduction).** If X is coherent, both meets of Claim 8.1 can be restricted to **finite covers by compact opens**. For the closed formula, expand arbitrary zero-meet open rectangles into compact-open rectangles and append compact top 1 to make a finite cover. For the fitted formula, choose a finite compact-open refinement of any arbitrary cover; its witness open w_V≤w_U. For coherent spectral points this recovers the 'common upper/common lower bound' characterization of §2 using prime-filter extension.

**Claim 8.4 (two directed test systems).** For the closed tests, concatenation of indexed covers U⊔V gives b_{U⊔V}≥b_U,b_V and hence decreasing C(b). For the fitted tests, any refinement V≼U gives w_V≤w_U, and intersection refinement U⊗V gives a common lower test. Neither construction assumes b_U monotone under *all* cover refinements. At each degree n, the intersection of these sublocales is the categorical limit of the corresponding diagram of monos in the sublocale lattice.

## 9. A simplicial open-cover span between Project C and Project A

For any cover U write T_U=∐_i O(u_i)→X for the canonical open surjection. For n≥1 define

    Q_{n−1}(U)=I^(n)×_{X^n} T_U^{n}
      ≅∐_{(i_1,...,i_n)} [ I^(n)∧O(u_{i_1}⊠···⊠u_{i_n}) ].

By Claim 8.2, the component over a nonface is the zero locale, and over every nerve simplex it is nonzero. Thus the index map factors through the discrete K_{n−1}(U) and yields a span

    K_{n−1}(U) ← Q_{n−1}(U) → I^(n).

**Claim 9.1.** Both maps are open surjections in arbitrary classical locales. Right arrow: pullback of the n-fold product of the open-surjection T_U→X. Left arrow: over the discrete nerve K, each component is nonzero locale→1, open surjective classically. Coordinate deletion/repetition are compatible and give a *simplicial span* K_•(U)←Q_•(U)→I^(•+1); maps are natural for specified refinements.

**Explicit limitation:** this does **not** yield an equivalence of simplicial realizations merely because both arrows are degreewise open surjections. If X is the discrete two-point locale and U=(1), K_• is terminal while I^(n)=Δ_n≅X in every degree; Q_•≅I^(•+1), so the span would incorrectly identify a two-point constant simplicial object with a point if one made such an inference.

## 10. Requested independent questions and source ledger

The referee is invited to check every statement including examples and editorial side-claims, without looking at internal analysis. In addition, the following source/dependency boundaries need explicit verdicts:

- Are the all-locale equations actually sublocale identities, and do coordinate repetitions give the claimed maps for *both* hulls?
- Does the proper-row argument prove properness as a map in Loc, not merely closedness of a point map?
- Is the countable ordered patch example Priestley, and is the proof of failure of a Plewe triquotient assignment fully localic?
- Do the patched Čech identities and the two ∞-topos equivalences have a correct site/topology and precise interpretation? Which parts merely express standard descent and which convey new information?
- Are open relations and maps to discrete index nerves handled correctly for *pointless* locales and infinite covers?
- Does Claim 9.1 genuinely define a *simplicial* span, and does it interact naturally with refinement maps?
- Does any statement silently assume associativity of arbitrary localic relation composition, that nonzero locales have actual points, or that sublocales are identified by their ordinary points?

### Source links and document titles (for provenance; supplementary only)

Project working notes (not independent reviews):

1. [Cameron–Kumar revisited / specialization graph powers](https://github.com/mkkinyon/locales/blob/main/ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md)
2. [Bisimplicial Čech and patch descent](https://github.com/mkkinyon/locales/blob/main/ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md)
3. [Coherent triquotient counterexample](https://github.com/mkkinyon/locales/blob/main/ProjectA_Dowker_witness_triquotient_counterexample_2026-11-10.md)
4. [Brun–Fosse–Salbu categorical/localic crosswalk](https://github.com/mkkinyon/locales/blob/main/ProjectA_Brun_Fosse_Salbu_Dowker_crosswalk_2026-11-10.md)
5. [Frame-cover open descent](https://github.com/mkkinyon/locales/blob/main/ProjectAC_frame_cover_Dowker_open_descent_2026-11-10.md)
6. [Higher diagonal reconstruction and simplicial span](https://github.com/mkkinyon/locales/blob/main/ProjectAC_higher_diagonal_cover_nerve_reconstruction_2026-11-10.md)
7. [Original Project C ideas](https://github.com/mkkinyon/locales/blob/main/C-frame-nerves.md)

Published references:

- P. J. Cameron and Vinod Kumar P. B., *Graphs on topological spaces*, arXiv:2610.14783 (2026).
- M. Brun, M. Gårdsmann Fosse, L. M. Salbu, *Dowker Duality for Relations of Categories*, arXiv:2303.16032 (2023).
- T. Plewe, *Localic triquotient maps are effective descent maps*, Math. Proc. Cambridge Philos. Soc. **122** (1997), 17–43.
- J. Vermeulen, *Proper maps of locales*, J. Pure Appl. Algebra **92** (1994).
- A. Joyal and M. Tierney, *An Extension of the Galois Theory of Grothendieck* (1984); theorem that open surjections of locales are effective descent.
- V. de Silva et al., *Dowker's theorem for higher-order relations*, arXiv:2506.10909 (2025; journal 2026).
- S. Chowdhury and F. Mémoli, *A functorial Dowker theorem and persistent homology of asymmetric networks*, arXiv:1608.05432v3 (2018).

**End of blind packet. No internal audit or author reconciliation is included.**