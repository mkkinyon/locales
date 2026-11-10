# Point-Free Topology — Finite closed-sublocale descent criterion for chain/higher-hull comparison

**10 November 2026 · NEW working segment, internally checked, NOT externally audited. No literature-priority claim.** Follow-up to [coherent chain/higher hull edgewise and crosscut note](PointFree_coherent_chain_higher_hulls_edgewise_crosscut_2026-11-10.md) and [10 Nov external audit reconciliation](PointFree_Dowker_EXTERNAL_referee_reconciliation_2026-11-10.md). Classical mathematics and prime-filter arguments are used. The new criterion is a Čech-local statement in the explicitly chosen **patched Stone sheaf ∞-topos**, not an unpatched equivalence of simplicial locales or a theorem about intrinsic shape.

## 0. Conventions and setup

Let X be a coherent locale, L=O(X), K=K(X), with patch Priestley space P. Specialization is x≤y iff every spectral open containing x contains y. Let Ch_n(X)⊆X^(n+1) be chains and I_n(X)=cl Δ_(n+1)⊆X^(n+1) the n-th closed higher diagonal hull. In coherent X the points of I_n(X) are all tuples with a common upper bound. The canonical Ch_•→I_• and Ch_•→D_• are simplicial monomorphisms. Write
  H_n^X(Z) := I_n(X) ∧ Z^(n+1) ⊆ X^(n+1),
for any proconstructible spectral sublocale Z↪X. The relative H distinguishes an upper witness **in X** from an upper witness **inside Z**; H_n^X(Z) need not be I_n(Z).

Choose finitely many compact opens u_1,...,u_r∈K satisfying ∧_i u_i=0. Put Z_i=C(u_i)↪X. These are closed, proconstructible, specialization-downward-closed spectral sublocales, and cover X. For each nonempty index set S⊆[r], put
  v_S=∨_{i∈S}u_i∈K,  Z_S=∧_{i∈S}Z_i=C(v_S).
Intersections may be the empty locale. Let H_•^X(Z) be the corresponding simplicial sublocale of I_•, and Ch_•(Z)↪H_•^X(Z) the canonical simplicial inclusion.

Work in \mathscr H_St=Shv_∞(Stone_κ, J_fin jointly surj), the sufficiently large subcanonical Stone site with finite jointly surjective covering families, as repaired in the 10 November blind audit. Write h for sheafified Yoneda and \mathbf C(X)=|h(Patch Ch_•(X))|, \mathbf I(X)=|h(Patch I_•(X))|, \mathbf D(X)=|h(Patch D_•(X))|. The edgewise rectangle theorem in the immediately preceding **unaudited working note** supplies equivalence of statuses of canonical \mathbf C→\mathbf I and \mathbf C→\mathbf D. The current theorem independently proves the closed-side statement, but the D-side uses that edgewise lemma; maintain explicit provenance.

## 1. Main finite closed-sublocale descent theorem

**Theorem (relative finite descent).** Suppose for every nonempty S⊆[r] the inclusion
  |h(Patch Ch_•(Z_S))| → |h(Patch H_•^X(Z_S))|
is an equivalence in \mathscr H_St (empty Z_S: both sides are initial). Then \mathbf C(X)→\mathbf I(X) is an equivalence, and consequently \mathbf C(X)→\mathbf D(X) is an equivalence by the edgewise rectangle comparison.

**Proof:** The n-th chain object is covered in Stone by Ch_n(Z_i): any chain (x_0≤...≤x_n) ends at x_n∈some Z_i, and downward closure forces every x_j∈Z_i. Likewise I_n(X) is covered by H_n^X(Z_i): any tuple with a common upper witness y∈P has y∈some Z_i, hence all coordinates belong to Z_i. Because all terms and inclusions are proconstructible spectral and point-determined in the coherent class, these are genuine finite jointly surjective Stone cover families after patching; no claim about general arbitrary sublocales determined by points is used.

Their k-fold Čech intersections are exactly Ch_n(Z_S) and H_n^X(Z_S). Apply h and form the augmented Čech nerves in cover-index degree k, varying simplicially in n. Every row in n realizes to \mathbf C(X) or \mathbf I(X) by levelwise effective epimorphic descent. On k-fold intersections, the assumed comparison realizes to an equivalence; coproducts and colimits preserve it. Interchange the two geometric realizations to obtain \mathbf C(X)≃\mathbf I(X) under the **canonical** chain inclusion. The edgewise rectangle compatibility identifies its D-side counterpart. QED.

**Warning:** The statement with a one-element cover Z_1=X is formally tautological. The force comes from choosing proper manageable Z_i and verifying the intersection hypotheses algebraically as in §2 below.

## 2. A fully compact-open-lattice criterion

For every nonempty S let K_S=K(Z_S). Since Z_S=C(v_S) with v_S compact, the compact opens are
  K_S ≅ [v_S,1]_K
as a bounded distributive lattice, whose 0 element is v_S and whose 1 is 1_K. The locale Z_S is nonzero iff v_S≠1.

**Prime-endpoint criterion.** Suppose that for each S with v_S≠1, **at least one** of the following holds in K_S:

(A) *Meet-prime bottom*: \(a\wedge b=0_{K_S}\Rightarrow a=0_{K_S}\text{ or }b=0_{K_S}\).

(B) *Join-prime top*: \(a\vee b=1_{K_S}\Rightarrow a=1_{K_S}\text{ or }b=1_{K_S}\).

Then both canonical maps \mathbf C(X)→\mathbf I(X) and \mathbf C(X)→\mathbf D(X) are equivalences.

**Proof of algebraic point identification.**
(A) The set of nonzero elements of K_S is a prime filter: it is upward-closed, finite-meet-closed by (A), and prime for joins because a∨b≠0 implies a≠0 or b≠0. It contains every other prime filter, so the corresponding spectral point \(g_S\) is **greatest** in the specialization order.
(B) The singleton {1} is a prime filter: primeness is precisely (B). It lies inside every other prime filter, so its point \(\ell_S\) is **least** in the specialization order.

Conversely, for a nonzero coherent locale a greatest spectral point forces (A), and a least spectral point forces (B), so these are exactly the finite lattice tests for existence of specialization endpoints.

**Why (A) suffices for each relative comparison.** If Z_S has greatest point g_S, every tuple in Z_S has common upper witness g_S∈X, so H_n^X(Z_S)=Z_S^(n+1) as actual proconstructible spectral sublocales. This is the Čech nerve of the Stone-surjection Patch Z_S→1 and realizes to 1. Meanwhile the internal chain category on Z_S has terminal point g_S; its nerve has an extra degeneracy and realizes to 1. The map between them is an equivalence.

**Why (B) suffices.** If Z_S has least point ℓ_S, the chain category has an initial point and its patched nerve realizes to 1. Furthermore H_•^X(Z_S) is simplicially conical at ℓ_S: for any tuple in Z_S having common upper bound y∈X, adding ℓ_S preserves this witness because ℓ_S≤x_i≤y. The continuous constant-point insertion maps define an extra degeneracy of the **actual** Stone simplicial object, and its realization is 1. Thus the relative comparison is an equivalence.

This criterion is stated entirely in terms of finitely many **compact-open elements** of the bounded distributive lattice K, their finite joins, and primality of endpoints in the intervals [v_S,1]_K. It needs neither a designated set of maximal points nor a chosen ordinary point as input.

**Scope:** The above is a sufficient, not necessary, test. Both (A) and (B) are used as convenient finite algebraic certificates of contractibility, not a classification of all coherent locales for which the canonical maps are equivalences.

## 3. Strictly beyond the finite-maximal hypothesis: an infinite-maximal S¹ example

Let P_0 be the 6-point face poset of a three-edge circle: minima v_1,v_2,v_3; maxima e_12,e_23,e_31; incidence v_i<e_ij when vertex i belongs to edge ij. Adjoin a convergent sequence A={a_1,a_2,...,a_∞} of **new maximal points**, with sole additional strict comparabilities
  v_1<a_n (n≥1),  v_1<a_∞.
The a_n are pairwise incomparable, incomparable with a_∞, and incomparable with every e_ij. In the patch topology a_n→a_∞ and the original 6 points are isolated. The order is closed: its only nonconstant limiting comparisons v_1<a_n converge to v_1<a_∞. Priestley separation holds: ↑v_i are patch-clopen; the isolated maximal e_ij,a_n have clopen upset singletons; the a_∞-tail sets {a_∞}∪{a_n:n≥N} are clopen upsets. The spectral topology generated by patch-clopen upsets defines an infinite coherent X.

Its set of maximal points
  M={e_12,e_23,e_31} ∪ A
is infinite. Consequently the preceding finite-maximal crosscut criterion **cannot** be applied.

Define four proper closed proconstructible spectral downsets:
  Z_1=↓e_12={v_1,v_2,e_12};
  Z_2=↓e_23={v_2,v_3,e_23};
  Z_3=↓e_31={v_3,v_1,e_31};
  Z_4={v_1}∪A.
Each Z_i is **patch-clopen** and downward-closed. Therefore its complement u_i=P\Z_i is a patch-clopen upset, hence compact spectral open; Z_i=C(u_i). They cover P, hence ∧_i u_i=0 in K(X).

The nonempty intersections are
  Z_1∩Z_2={v_2}; Z_2∩Z_3={v_3}; Z_3∩Z_1={v_1};
  Z_1∩Z_4={v_1}; Z_3∩Z_4={v_1}; Z_2∩Z_4=∅;
  Z_1∩Z_3∩Z_4={v_1},
and other triple intersections and the quadruple intersection are empty.
Each Z_1,Z_2,Z_3 has a greatest point e_ij (case A). Z_4 has a least point v_1 (case B). Every nonempty proper intersection is a singleton (both A and B). Therefore the intrinsic criterion of §2 holds.

The finite cover nerve has four vertices 1,2,3,4, edges 12,23,31,14,34, and a single 2-simplex 134; its realization is a circle (the triangle 134 is attached along edge 13 to the triangle boundary 123). Hence the Čech proof gives
  \mathbf C(X) ≃ \mathbf I(X) ≃ \mathbf D(X) ≃ \underline{S¹}
in the repaired Stone sheaf ∞-topos, **via the canonical chain inclusions**.

A finite truncation of the sequence (three isolated a_i plus a_∞) was checked combinatorially: intersections, five edges plus one 2-simplex, Euler characteristic 0, and maximal points as claimed. The proof is the infinite compact Priestley construction; the truncation is a sanity check only.

This example demonstrates strict extension beyond the finite-maximal theorem while retaining noncontractible homotopy, and illustrates why allowing a lower cone with a **least** rather than greatest point is useful.

## 4. Next questions and cautions

- The **finite closed-cover criterion** is an immediate but useful descent mechanism. The fully algebraic prime-endpoint test is a strong sufficient condition for it. Its formulation as a finite interval-lattice test is intrinsic to K(X).
- The closed-sublocale cover necessarily uses compact opens u_i with meet zero; arbitrary patch-proconstructible downsets would also work if their complements are genuine spectral opens, but the compact condition makes the interval formula and tests transparent.
- The **D-side** of the theorem relies on the preceding still-unaudited edgewise rectangle comparison. The C→I implication and the finite lattice test for it have independent Čech proofs.
- Nothing here identifies localic intrinsic shape, nor claims that every coherent locale admits such a good cover. For Stone locales with an infinite underlying Stone space, the criterion is far from necessary: Ch=I=D degreewise even if no finite cover satisfies the endpoint tests.
- Verify separately the edgewise projection equivalence in the chosen ∞-topos before incorporating the D-side into a canonical audited theorem. Do not pursue broad shape consequences based solely on this segment.
- Literature context: classical crosscut and nerve methods; standard sheaf \infty-topos Čech descent. Novelty, if any, is in this specific frame formulation and the explicit localic examples; not established.
