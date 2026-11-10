# Project A / C — Higher diagonal hulls reconstructed from frame-cover nerves

**10 November 2026. Working internal proof, not externally audited and no novelty claim.** This note develops the original Project C frame-cover nerve idea [C-frame-nerves.md](C-frame-nerves.md) and Project A's higher diagonal hulls / bisimplicial common witnesses [ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md](ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md), [ProjectAC_frame_cover_Dowker_open_descent_2026-11-10.md](ProjectAC_frame_cover_Dowker_open_descent_2026-11-10.md).

Fix an arbitrary locale X, L=O(X), n≥2, and its diagonal sublocale Δ_n↪X^n. Put
  I^(n)=cl(Δ_n),  D^(n)=fit(Δ_n).
Write O(a) for the open sublocale associated with a∈O(X^n), C(a) for its complementary closed sublocale, and
  a_1⊠···⊠a_n := ⋀_{j=1}^n π_j^*(a_j)∈O(X^n).

For an indexed cover U=(u_i)_{i∈I}, ⋁_i u_i=1, define two opens
  w_U^(n)=⋁_{i∈I}(u_i⊠···⊠u_i),
  b_U^(n)=⋁_{(i_1,...,i_n)∈I^n, ⋀_j u_{i_j}=0}(u_{i_1}⊠···⊠u_{i_n}).
The tuples in b_U are precisely the absent (n−1)-simplices in the *ordered tuple* cover nerve N(U); repetitions are allowed.

## 1. Exact unrestricted reconstruction theorem

**Theorem 1.** For every locale X and n≥2, as genuine sublocales of X^n,
  I^(n)= ⋀_{U an indexed open cover} C(b_U^(n)),
  D^(n)= ⋀_{U an indexed open cover} O(w_U^(n)).
The second factor O(w_U^(n)) is exactly the degree-(n−1) common-member locale L_{n−1}(R_U) of our frame-cover bipartite relation R_U↪I_d×X.

**Closed proof.** In any frame coproduct O(X^n), rectangles join-generate. For a rectangle r=a_1⊠···⊠a_n its restriction to Δ_n is Δ_n^*(r)=⋀_j a_j. Thus the largest open of X^n annihilated by Δ_n^* is
  d_n=⋁_{a_1,...,a_n∈L, ⋀_j a_j=0}a_1⊠···⊠a_n.
Consequently cl Δ_n=C(d_n). Every b_U^(n)≤d_n. Conversely, each rectangle with zero diagonal restriction appears as a summand in b_U^(n) for the cover U=(a_1,...,a_n,1). Therefore d_n=⋁_U b_U^(n), so C(d_n)=⋀_U C(b_U^(n)).

**Fitted proof.** Δ_n^*(w_U^(n))=⋁_i u_i=1, so O(w_U^(n)) contains Δ_n. Conversely, for any open O(w) containing Δ_n, write w=⋁_t(a_{t,1}⊠···⊠a_{t,n}). Put c_t=⋀_j a_{t,j}. Then ⋁_t c_t=Δ_n^*w=1 and c_t⊠···⊠c_t≤a_{t,1}⊠···⊠a_{t,n}≤w. Hence w_{(c_t)}^(n)≤w. The displayed family is cofinal among all open sublocales containing Δ_n; their meet equals fit Δ_n.

No coherence, spatiality, compactness, or point assumptions enter either argument.

## 2. Cover nerves can themselves be read from the closed higher diagonal hull

**Theorem 2 (mutual reconstruction with labelled opens).** For any indexed family U=(u_i) (cover not required) and any tuple \mathbf i=(i_1,...,i_n),
  \mathbf i∈N_{n−1}(U)
  ⇔ ⋀_j u_{i_j}≠0
  ⇔ I^(n) ∧ O(u_{i_1}⊠···⊠u_{i_n})≠0.
Indeed Δ_n is dense in its closure I^(n). For any open w of X^n, O(w)∧I^(n)=0 iff O(w)∧Δ_n=0. The latter for a rectangle is equivalent to ⋀_j u_{i_j}=0.

Thus the entire family of *labelled* cover nerves is read off from the higher closed diagonal sublocales; conversely Theorem 1 reconstructs I^(n) using the forbidden localic rectangles from the labelled nonfaces. Merely knowing the abstract simplicial complex of one cover, without its actual opens in L, is not sufficient to determine the sublocale.


## 2a. A natural simplicial span of two open covers (new structural strengthening)

Let U=(u_i) be an open cover, and write T_U=∐_i O(u_i)→X for the standard open-cover surjection. For n≥1 pull back its n-fold product along I^(n)↪X^n:
  Q_{n−1}(U) := I^(n) ×_{X^n} (T_U)^n
    ≅ ∐_{(i_1,...,i_n)∈I^n} [I^(n)∧O(u_{i_1}⊠···⊠u_{i_n})].
By Theorem 2, the components indexed by nonfaces of N(U) are ZERO, so the index projection factors uniquely through the discrete locale K_{n−1}(U) of nerve tuples. We obtain a canonical span
  K_{n−1}(U) ← Q_{n−1}(U) → I^(n).
**Both maps are open surjections**, for arbitrary locales: the right map is a pullback of the n-fold product of an open-cover map, and the left map is assembled over the discrete K_{n−1}(U) from nonzero locale maps to 1. Deleting/repeating coordinate maps yield a simplicial span
  K_•(U) ← Q_•(U) → I^(•+1)
natural for specified refinements of indexed covers.

**Important:** Degreewise open surjections are NOT sufficient for a weak equivalence of simplicial realizations. For example, with the one-element cover {1} of a discrete two-point locale, K_• is terminal and I^(•+1) is constant at the two-point locale, with the comparison simply a two-point surjection onto a point. This is a genuine simplicial open-cover comparison, not a localic nerve lemma.

## 3. Coherent reduction to finite compact-open covers

Suppose X coherent (compact spectral) and K(X) the bounded distributive lattice of compact opens. Then **both** meets in Theorem 1 may be restricted to *finite indexed covers by compact opens*.

For I^(n), every arbitrary rectangle from the zero-meet formula expands as a join of compact-open rectangles with zero total meet. Each n-tuple of compact opens can be extended to a finite compact-open cover simply by adjoining 1 (compact in the coherent case). Therefore the finite-cover b_U are join-cofinal in d_n.

For D^(n), take any open cover U. Expand its entries as joins of compact opens; because 1 is compact, a finite selection of those compact opens covers 1. The resulting finite compact-open cover V refines U, so w_V^(n)≤w_U^(n). Thus the finite-compact cover tests are meet-cofinal.

Each b_U^(n) and w_U^(n) for such a finite compact-open cover is compact open in X^n. Its associated closed/open sublocale is patch-clopen in the spectral point space. The arbitrary meets have patch-closed point sets, independently corroborating the proconstructible nature of these particular higher hulls (given the standard proconstructible locale correspondence).

On spectral points, the theorem reads:
  (x_1,...,x_n)∈pt(I^(n))
    iff for every compact open k_j containing x_j, ⋀_j k_j≠0
    iff the x_j have a common generization (upper bound);
  (x_1,...,x_n)∈pt(D^(n))
    iff for every finite compact-open cover U some u_i contains all x_j
    iff the x_j have a common specialization (lower bound).
The first final equivalence follows from prime-filter extension of the proper filter generated by the union of prime filters F_{x_j}. For the second, put F=⋂_j F_{x_j} in K(X); the cover condition is equivalent to the ideal generated by K(X)\F being proper. Extend it to a prime ideal; its complementary prime filter G⊆F represents the common lower point.

**Caution on monotonicity.** Under arbitrary cover refinement, w_V≤w_U holds, but b_V≥b_U need NOT hold. Example: discrete two-point X, U=({a},{b},1) and V=(1); V refines U, b_U^(2)≠0 while b_V^(2)=0. For *canonical intersection refinement* U⊗V=(u_i∧v_j)_{i,j}, b_{U⊗V}≥b_U,b_V and w_{U⊗V}≤w_U,w_V. Do not claim the nonface operators form a monotone inverse system under arbitrary refinement assignments.

### Directed approximation systems (distinct for the two hulls)

The test families can each be arranged into a genuine decreasing diagram of sublocales, but **not using the same refinement order**.

- For I^(n), if U⊔V denotes *concatenation* of two indexed covers, then b_{U⊔V}^(n)≥b_U^(n),b_V^(n). Consequently C(b_{U⊔V})≤C(b_U),C(b_V). Inclusion/concatenation of indexing families makes the closed tests a filtered decreasing family, whose intersection (limit of subobjects of X^n) is I^(n). This works already without coherence.
- For D^(n), ordinary refinement V≼U gives w_V^(n)≤w_U^(n). A common intersection refinement U⊗V=(u_i∧v_j) refines both, so the open witness locales L_{n−1}(V) form a cofiltered decreasing family with limit D^(n). In a coherent locale, finite compact-open covers suffice for this strict inverse-limit description, in every simplicial degree, giving D^(•+1) as a degreewise inverse limit of the L_•(U).

This does **not** imply that geometric realizations or homotopy groups commute with these inverse limits. Avoid interpreting the degreewise inverse-limit identity itself as a nerve lemma or shape theorem.

## 4. Genuine higher-dimensional information

Take the six-point finite poset P with three minimal elements a,b,c and three maximal elements t_ab,t_bc,t_ca, where a,b≤t_ab, b,c≤t_bc, c,a≤t_ca, and no other strict comparisons. In the upper-Alexandrov topology its principal opens U_a,U_b,U_c cover P, have pairwise nonzero intersection, but U_a∧U_b∧U_c=0. Thus their cover nerve is the triangle boundary. Each pair among a,b,c belongs to I^(2), but (a,b,c) does not belong to I^(3), detected by the missing 2-simplex. Order-dualizing gives an analogous distinction for D^(3) versus its binary coordinate projections. Thus higher hulls are not generally determined by their 2-dimensional skeleta, already for finite coherent locales.

## 5. Relationship with Dowker literature

The new theorem is a direct lattice/sublocale computation, not a claim of a new general Dowker homotopy theorem. The project frame-cover rectangle nerve leads to a point-free Dowker comparison via open effective descent, as recorded in the preceding note. Two additional works flagged by the owner:
- de Silva, Giusti, Itskov, Robinson, Sazdanovic, Schonsheck, Vaupel, Yoon, *Dowker's theorem for higher-order relations*, arXiv:2506.10909 (2025; journal version 2026): develops *multiway relations among several sets*, prod-complexes and functorial homotopy equivalences. Conceptually relevant to future higher-arity Dowker constructions, not needed for Theorems 1–2.
- Chowdhury–Mémoli, *A functorial Dowker theorem and persistent homology of asymmetric networks*, arXiv:1608.05432v3 (2018), Theorem 3: functoriality for inclusions of relations. Useful precedent for refinement naturality, does not address localic sublocale hull reconstruction.

## 6. Interpretation and bounded next steps

The two hull operations have exact cover-combinatorial descriptions:
  I^(n): prohibit coordinatewise open rectangles indexed by missing simplices of the cover nerve;
  D^(n): require the tuple to lie in a single member of *every* open cover (interpreted as a meet of open sublocales, not naive points).
They capture different levels of information but come from the **same** indexed frame-cover data. The cover nerve of *one* cover does not determine localic homotopy/shape; even the entire family of nerves must retain frame labels if it is to reconstruct the actual sublocales.

Bounded follow-ups: independently audit the frame identities; explore whether a natural morphism or comparison between the simplicial locale degrees K(U), L(U) and the higher diagonal-hull simplicial locales exists beyond the proven sublocale approximation; examine whether higher-order relational-product techniques help *only* for a specified shape invariant. Avoid inferring a localic nerve lemma from the present reconstruction theorem.