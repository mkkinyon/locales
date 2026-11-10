# Project A / Project C interface — Point-free Dowker comparison for frame-cover nerves

**10 November 2026 — working internally checked proposition and applications, not externally audited; no novelty/prior-art claim.** This note bridges [C-frame-nerves.md](C-frame-nerves.md) and [Project A's bisimplicial Dowker investigation](ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md). The bisimplicial rectangle mechanism has antecedents, especially Brun–Fosse–Salbu (arXiv:2303.16032), and effective descent of open surjections is due to Joyal–Tierney. Distinguish the chosen-cover invariant from homotopy or shape of the locale.

## 1. Open-cover relation for an arbitrary frame

Let X be any locale, L=O(X), and (u_i)_{i∈I} any indexed family of opens. It need not cover for most assertions below. Regard I as the discrete locale I_d and define the **open relation**
  R_U = \coprod_{i∈I} O(u_i) ↪ I_d × X.
For p,q≥0 the internal rectangle locale is
  E_{p,q}(R_U) ≅ \coprod_{\mathbf i=(i_0,...,i_p)∈I^{p+1}} O(\bigwedge_{k=0}^p u_{i_k})^{q+1}
as a sublocale of I_d^{p+1}×X^{q+1}. Products are localic products, and empty intersections give the initial locale.

Set K_p=im(E_{p,0}→I_d^{p+1}) and L_q=im(E_{0,q}→X^{q+1}). Then
  K_p ≅ { (i_0,...,i_p): \bigwedge_{k=0}^p u_{i_k}≠0 }_d,
  L_q = O(w_q),  w_q= \bigvee_{i∈I} \bigwedge_{j=0}^q \pi_j^*(u_i)∈ O(X^{q+1}).
Hence K_• is exactly the ordered-tuple simplicial set of the **frame-cover nerve**, regarded degreewise as discrete locales. Repeated indices are allowed. L_0=O(\bigvee_i u_i), hence L_0=X if (u_i) covers 1.

## 2. Both witness maps are open surjections

**Theorem (working).** For any locale X and any family of opens (u_i), every
 r_p:E_{p,0}→K_p and s_q:E_{0,q}→L_q
is an **open surjection** in Loc. No spatiality, coherence, compactness, or point-existence assumptions.

Proof for r_p: Over each element \mathbf i of the discrete set K_p, the fiber is O(u_{\mathbf i})→1 with u_{\mathbf i}=\bigwedge_k u_{i_k}≠0. Every locale map Z→1 is open, with left adjoint O(Z)→2 taking 0↦0 and nonzero opens to 1; it is surjective iff Z≠0. These maps assemble along the discrete coproduct as an open surjection.

Proof for s_q: E_{0,q}=\coprod_i O(u_i)^{q+1}. Each component is an open sublocale of X^{q+1}, and their union is exactly L_q=O(w_q). The canonical map from the disjoint coproduct to the union of the open sublocales is an open surjection. QED.

For any localic relation R↪X×Y, the rectangle locale E_{p,q} is both (q+1)-fold fiber power of E_{p,0} over K_p and (p+1)-fold fiber power of E_{0,q} over L_q. Thus E_{p,•} and E_{•,q} are the respective Čech nerves. For our open-cover relation, both are Čech nerves of open surjections, hence of Joyal–Tierney effective-descent maps in Loc. This is an **unpatched** two-sided localic result.

## 3. Homotopical formulation (requires specifying ambient category)

Choose a small universe/site of locales with enough finite limits, discrete index locales and open-surjection covers, then let H_op be the \infty-topos of space-valued sheaves for the open-surjection topology; denote representable sheaves by h(Z). The topology is subcanonical because open surjections are stable effective-descent morphisms in Loc. Alternatively take the \infty-topos associated with a suitable canonical open coverage; record the choice of site before publication.

Each h(r_p) and h(s_q) is an effective epimorphism in H_op. The representable h preserves finite limits, so h(E_{p,•}) and h(E_{•,q}) are their Čech nerves. By Čech descent and commuting homotopy colimits,
  |h(K_•)| ≃ |h(E_{•,•})| ≃ |h(L_•)|.
The two equivalences are functorial for morphisms of indexed open-cover relations.

**Interpretation:** K_• is a discrete simplicial locale encoding the ordinary meet-nerve of an indexed family, even if X is pointless. L_• is a simplicial locale of tuples that lie simultaneously in some one cover member. No claim that their realization is the intrinsic homotopy type of X. For the single-member cover {1}, K_• is a point and L_q=X^{q+1}, whose realization becomes terminal under open-surjection descent regardless of X. Thus a fixed-cover Dowker equivalence cannot by itself establish a nerve lemma for X.

## 4. Refinements: canonical comparison up to homotopy

Let \mathcal V=(v_j)_{j∈J} refine \mathcal U=(u_i)_{i∈I} by an assignment \alpha:J→I with v_j≤u_{\alpha(j)}. This gives a map of open relations R_V→R_U, hence simplicial locale maps K_•(V)→K_•(U), L_•(V)→L_•(U). The L-map is the canonical degreewise open-sublocale inclusion O(w_q(V))↪O(w_q(U)), independent of which refinement assignment is chosen.

If \alpha,\beta are two refinement assignments, the corresponding maps on the discrete simplicial K_• are **contiguous**: for every nondegenerate simplex (j_0,...,j_p), \bigwedge_k v_{j_k}≠0, and this same nonzero meet lies beneath all u_{\alpha(j_k)} and all u_{\beta(j_k)}. Thus the union of their image vertices forms a simplex in N(U). Hence the two induced maps on geometric realizations are homotopic. This is ordinary simplicial contiguity, so the assignment-independent morphism is established at least in the homotopy category; coherent higher choices needed for an \infty-categorical pro-object must be treated separately.

## 5. Purely pointless illustration and Boolean disjoint refinements

Take the complete atomless Boolean frame L=RO(S¹), which has no points (a completely prime filter of a complete Boolean algebra is principal at an atom). Choose three regular-open arcs centered 120° apart with half-width 75°. Their join is 1, they have pairwise nonzero meets and zero triple meet. The nerve is the boundary of a triangle, homotopy equivalent to S¹. The theorem above applies literally to the resulting *pointless* open-cover relation R_U in Loc and produces two open effective-descent Čech resolutions. This realizes the chosen-cover combinatorics without ordinary points; it does NOT identify shape(L) with S¹.

In fact **every cover of a complete Boolean frame refines to a pairwise disjoint cover**. Well-order the indices and set v_i=u_i∧¬(∨_{j<i}u_j); complete Boolean distributivity gives \bigvee_i v_i=\bigvee_i u_i, the nonzero v_i are disjoint, and v_i≤u_i. Such a refinement has a discrete nerve (only vertices, no nondegenerate edges). The disjoint refinements are cofinal among all indexed covers; common refinements of two Boolean partitions can be taken by pairwise meets. Therefore a pro-homotopy construction using *all* cover nerves is pro-discrete on complete Boolean frames. In particular, the one-cover S¹ from the arcs is not an intrinsic S¹-type for RO(S¹). Do not identify this pro-nerve construction with an independently defined localic shape invariant without proving a comparison.

## 6. Significance and next bounded questions

This gives an unconditional unpatched localic Dowker comparison for frame-cover relations, where the index side is discrete and the witness side is a locale. The failure of unpatched triquotiency in Project A for coherent specialization relations does not contradict this: those relations are generally not open relations between a discrete locale and a locale.

Potential next steps: (1) formulate the refinement pro-homotopy object with proper coherence bookkeeping; (2) compare it with established point-free shape/Čech shape for frames; (3) identify when a single cover nerve is justified by an actual localic nerve lemma. Investigate source priority; the result is a direct formal application of standard internal Dowker/Čech descent, not yet a novelty claim.

**Sources/background:** Joyal–Tierney, *An Extension of the Galois Theory of Grothendieck* (1984), open surjections effective descent in Loc; Brun–Fosse–Salbu, *Dowker Duality for Relations of Categories* (2023), bisimplicial rectangle nerves; Project C backlog; the earlier Project A coherent specializations and patch-Čech result.