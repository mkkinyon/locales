# Point-Free Topology — Finite-poset crosscut criterion and canonical inclusions into higher witness nerves

**10 November 2026.** Working internally checked mathematical segment; not externally audited. The principal homotopy criterion is **classical crosscut/nerve theory**, notably Rota–Björner, and is NOT presented as a new theorem. A useful additional formulation is that the **canonical inclusions** from the order complex into BOTH witness complexes are homotopy equivalences under the good-intersection hypothesis; the argument below explicitly verifies those maps. This returns to Cameron–Kumar, *Graphs on Topological Spaces* (arXiv:2610.14783), and the [Project A/C Dowker reconciliation](PointFree_Dowker_EXTERNAL_referee_reconciliation_2026-11-10.md).

## 1. Notation and the three simplicial complexes

Let P be a nonempty finite poset, and M=Max(P). Write Ord(P) for the simplicial order complex (vertices P, faces the nonempty chains), and define
  K_up(P)={nonempty σ⊆P: σ has a common upper bound};
  K_low(P)={nonempty σ⊆P: σ has a common lower bound}.
There are **canonical simplicial inclusions**
  Ord(P) ↪ K_up(P),    Ord(P) ↪ K_low(P),
since a chain has both endpoints as witnesses. In a finite coherent locale P (upper Alexandrov convention), these are the simplicial sets of points of higher diagonal hulls I^(n)=cl Δ_n and D^(n)=fit Δ_n, respectively, with repetitions allowed (the ordinary complexes are their nondegenerate finite faces).

Let N_M(P) be the simplicial complex on M with a face S iff the set of common lower bounds
  B_S = ⋂_{m∈S}↓m = {x∈P: x≤m for all m∈S}
is nonempty. Thus N_M=K_low(P)|_M.

## 2. Unconditional strong collapse

**Lemma.** For every finite P, K_low(P) strongly collapses onto N_M(P) (hence has its simple-homotopy type). Proof: for each nonmaximal x choose m(x)∈M above x, with m(m)=m for maximal m. Map each vertex x to m(x). For any face σ of K_low with witness z≤all x∈σ, z≤m(x) for all x, and σ∪m(σ) is a simplex. Hence the resulting simplicial retraction r:K_low→N_M is contiguous to the identity (after including N_M). Even more concretely, each nonmaximal x is dominated by m(x); delete nonmaximal vertices one by one by elementary strong collapses. This proof requires no meet/contractibility assumptions.

Also **unconditionally**, K_up(P) has the homotopy type of N_M(P): cover it by full simplices on ↓m for m∈M. Each nonempty intersection is a full simplex on B_S, and the nerve is N_M. This is classical Dowker duality, now in the maximal-element reduction.

## 3. Good-intersection criterion: BOTH canonical inclusions are homotopy equivalences

**Theorem (classical crosscut criterion, with map-level strengthening).** Assume
  (*) For every nonempty S⊆M with B_S≠∅, Ord(B_S) is contractible.
Then both **canonical inclusions**
  Ord(P) ↪ K_up(P),    Ord(P) ↪ K_low(P)
are homotopy equivalences. Consequently, when P is the finite upper-Alexandrov T0 space, both common-witness complexes recover its weak homotopy type, via McCord's theorem. The hypothesis is weaker than requiring every nonempty B_S to have a greatest element (the meet of S).

**Proof of K_up inclusion.** The complexes F_m=Ord(↓m) cover Ord(P), while H_m=(full simplex on ↓m) cover K_up(P). For any S⊆M the intersections are
  ⋂_{m∈S}F_m=Ord(B_S);
  ⋂_{m∈S}H_m=full simplex on B_S.
They are simultaneously empty or contractible by (*), and their inclusion is a homotopy equivalence. The finite homotopy-gluing/nerve theorem for a map of good covers (equivalently induction via homotopy pushouts of simplicial subcomplexes) therefore shows that the *inclusion itself* Ord(P)↪K_up(P) is a homotopy equivalence.

**Proof of K_low inclusion.** Choose a retraction r:K_low→N_M as in §2. Put g = r∘i_low:Ord(P)→N_M, induced by the vertex map x↦m(x). To show g is a homotopy equivalence, let F(C) denote the face poset of a simplicial complex C and define
  Φ:F(Ord(P)) → F(N_M)^op,
  Φ(σ) = {m∈M: max(σ)≤m}.
The image is a nonempty face of N_M, and Φ is order-preserving into the opposite poset: extending a chain increases its maximum and shrinks the set of eligible maxima. For a nonempty face S of N_M, the lower Quillen fiber is
  Φ^{-1}(F(N_M)^op_{≤S}) = F(Ord(B_S)).
By (*) its order complex is contractible. Quillen's Theorem A for finite posets therefore shows that |Φ|:|sd Ord(P)|→|sd N_M| is a homotopy equivalence (the reversal of face order does not affect geometric realization).

Compare this map with g after standard subdivision projections. Choose the last/maximum vertex of each chain face σ for the source subdivision projection p:sd Ord(P)→Ord(P); choose an arbitrary vertex of each face S for the target subdivision projection t:sd N_M→N_M. For nested chains of faces σ_0⊂...⊂σ_k, each vertex of g∘p and t∘Φ lies in Φ(σ_0), since g(maxσ_i)=m(maxσ_i)∈Φ(σ_i)⊆Φ(σ_0) and t(Φ(σ_i))∈Φ(σ_i)⊆Φ(σ_0). This set is a simplex of N_M, so g∘p and t∘Φ are **contiguous**. The two subdivision projections are homotopy equivalences, as is Φ; hence g is a homotopy equivalence. Since r is a homotopy equivalence, so is i_low by two-out-of-three. QED.

**Naturality:** The inclusions Ord(P)→K_up(P), Ord(P)→K_low(P) are strictly natural for monotone maps of finite posets. The proof uses choices of maxima and a nerve comparison, but the resulting homotopy equivalences are canonical as maps.

## 4. Examples and strict weakening

1. **Face posets.** If P is the poset of nonempty faces of any finite simplicial complex, for maximal facets S with nonempty intersection, B_S is the principal downset of the intersection face. Thus (*) holds and both canonical inclusions are homotopy equivalences. This is classical crosscut theory.
2. **The K_{2,2} four-point obstruction.** P has two minima a,b, two maxima c,d with all lower-to-upper comparisons. B_{c,d}={a,b} has disconnected order complex. Ord(P) is a circle; the two witness complexes are contractible. This shows (*) has genuine content.
3. **Contractibility strictly weaker than existence of meets, even for a circle.** Begin with the face poset of a 3-edge cycle: minimal vertices v_1,v_2,v_3 and maximal edges e_12,e_23,e_31, each vertex below its incident edges. Add w<e_12,e_23 incomparable with v_2, and a point z with z<w and z<v_2, with no additional comparisons except those forced transitively. Then B_{e_12,e_23}={z,v_2,w} has a minimum z, hence contractible, but has no greatest element (v_2 and w are incomparable). Other pairwise maximal intersections are singleton sets {v_1} and {v_3}; the triple is empty. Thus (*) holds but meet existence fails, and Ord(P), K_up(P), K_low(P) all have homotopy type S^1.

## 5. All-locale chain-nerve bridge

For arbitrary locale X with oriented specialization sublocale A⊆X×X (a generalized pair f,g:Z→X factors through A iff f≤g), define
  Ch_n(X)={ (x_0,...,x_n): x_0≤x_1≤...≤x_n }
as the finite intersection of pulled-back A-relations. Because A represents an internally transitive preorder, deleting or repeating coordinates gives a simplicial locale Ch_•(X). The last coordinate x_n is an upper witness for all x_i; the first x_0 is a lower witness for all x_i. Consequently there are natural monomorphisms of simplicial locales
  Ch_•(X) ↪ K_•(A),   Ch_•(X) ↪ L_•(A).
By the referee's all-locale inequalities,
  K_n(A) ≤ I^(n+1),  L_n(A) ≤ D^(n+1).
Thus for every locale,
  Ch_n(X) ≤ I^(n+1) ∧ D^(n+1)
as actual sublocales. For coherent locales K_n(A)=I^(n+1), L_n(A)=D^(n+1); for finite Alexandrov P, their point simplicial sets are exactly K_up(P),K_low(P). The theorem in §3 therefore identifies a class on which the canonical **chain-to-higher-hull maps** become homotopy equivalences *of the associated finite simplicial sets*. It makes no unpatched localic homotopy claim.

## 6. Bibliography and status

The **homotopy-type criterion** is an instance of classical crosscut and simplicial nerve theory, not a new mathematical theorem. Explicit literature: Rota's crosscut theorem, as generalized by Björner; *Posets, clique graphs and their homotopy type*, European Journal of Combinatorics 29 (2008) 334–342; Margolis–Saliola–Steinberg, *Poset topology and homological invariants of algebras arising in algebraic combinatorics* (2013), Theorem 5.7 explicitly states the meet version. The map-level comparison (the inclusions themselves, rather than abstract homotopy equivalence) follows from the relative nerve lemma and Quillen A; check priority separately. Cameron–Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783, connects specialization, the two witness complexes, and finite-space homotopy under an acyclicity assumption. Do NOT presume their precise assumption is identical without comparing the original theorem text. McCord's finite-space weak homotopy theorem is used only in the finite T0 interpretation.

**Boundary:** Contractibility of the B_S, not merely vanishing reduced homology, is what the argument proving homotopy equivalence needs. This proof does not claim a general equivalence of simplicial locales in Loc or sheaf ∞-topos beyond finite-spatial simplicial sets.

**Next bounded questions:** (i) compare exactly against Cameron–Kumar §8 and their acyclicity formulation; (ii) test localic/combinatorial analogues of the good-intersection criterion for coherent spectral posets without collapsing back to patch point-set theory; (iii) ask whether the canonical inclusions are *simple* homotopy equivalences under weaker hypotheses, using the simple Quillen Theorem A and nerve theorem.