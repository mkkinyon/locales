# Point-Free Topology — Edgewise chain/Dowker bridge verified; ambient-upper and zigzag crosscut criterion

**10 November 2026. NEW working mathematics: internal adversarial check, not external referee-audited; no literature-priority claim.** Builds on the [coherent edgewise/crosscut working note](PointFree_coherent_chain_higher_hulls_edgewise_crosscut_2026-11-10.md), the [finite closed-cover local-to-global result](PointFree_coherent_finite_closed_cover_relative_crosscut_2026-11-10.md), and the [10 November external Dowker reconciliation](PointFree_Dowker_EXTERNAL_referee_reconciliation_2026-11-10.md).

## 0. Ambient conventions and status

Let X be coherent; K=K(X) compact-open bounded distributive lattice; specialization x≤y iff every spectral open containing x contains y; A⊆X² canonical oriented specialization. Set
  Ch_n(X)={x_0≤...≤x_n},
  I_n(X)=cl Δ_(n+1)=K_n(A),
  D_n(X)=fit Δ_(n+1)=L_n(A),
  E_{p,q}(A)={(x_0,...,x_p;y_0,...,y_q):x_i≤y_j for all i,j},
as **actual proconstructible spectral sublocales** of the respective coherent powers, using the previously audited coherent image theorem. Use the patched Stone-site ∞-topos \mathscr H=Shv∞(Stone_κ,finite jointly surjective covers) and sheafified Yoneda h. Write
  C=|h(Patch Ch_•)|, I=|h(Patch I_•)|, D=|h(Patch D_•)|,
  T=|h(Patch diag E_••(A))|.
The patched bisimplicial Čech comparison T→I, T→D is an equivalence on each side **only after patching**. No intrinsic localic shape claim and no assertion about unpatched D-projection effective descent (which fails for the known coherent example).

## 1. Edgewise comparison audited at the simplicial-map level

Define ε([n])=[n]*[n]=[2n+1], ε(α)=α*α. Then (esd₂ Ch)_n=Ch_(2n+1). Define F_n:Ch_(2n+1)→E_{n,n} by splitting
  x_0≤...≤x_n≤x_(n+1)≤...≤x_(2n+1)
  ↦ (x_0,...,x_n ; x_(n+1),...,x_(2n+1)).
It factors as a genuine localic map because x_i≤y_j holds for all i,j by internal transitivity. Compatibility with ε(α) for all α∈Δ makes it simplicial.

Let a,b:esd₂ Ch→Ch be the two block projections. We can **construct a simplicial homotopy already in Loc**, rather than assuming Brown–Chan–Galatius–Payne's realized homotopy. Given θ∈Δ[1]_n = Hom_Δ([n],[1]) define
  H_n(x_0≤...≤x_(2n+1), θ)
    = (x_{i+(n+1)θ(i)})_{i=0}^n.
Since θ is monotone, the indices increase, so H_n is a localic map into Ch_n. For α:[m]→[n], ε(α) carries i+(m+1)θ(α(i)) to α(i)+(n+1)θ(α(i)), verifying full simplicial naturality. Endpoints θ≡0, θ≡1 recover a,b. Thus a~b as simplicial localic maps; the comparison is **point-free before patching**.

Both realized maps |h(Patch a)|, |h(Patch b)| from |h(Patch esd₂ Ch)| to C are equivalences by the classical edgewise theorem. To avoid assuming an unsupported internal generalization, verify objectwise in presheaves of spaces on Stone_κ (the ordinary edgewise subdivision/realization theorem for simplicial spaces), then apply colimit-preserving sheafification. The standard diagonal-vs-iterated-realization theorem for bisimplicial spaces extends by the same objectwise/sheafification argument. For a relevant explicit reference, F. Brown, M. Chan, S. Galatius, S. Payne, *Hopf Algebras in the Cohomology of A_g, GL_n(Z), and SL_n(Z)*, §3.1, Definition 3.5 and Corollary 3.9 (web PDF published version); it shows realization of the two projections is homotopic to diagonal. The objectwise presheaf proof is our additional verification.

The composites esd₂ Ch --F→diag E→K and →L are exactly i_I∘a and i_D∘b. Since a,b are equivalent after realization and homotopic, and T→I,T→D are equivalences, the arrows C→I and C→D are equivalent **in the undercategory C/ \mathscr H**. In particular:
  (C→I)≃(C→D),   I ⨿_C 1 ≃ D ⨿_C 1.
Thus they have equivalent *relative obstruction objects*, stronger than the mere iff for whether either arrow is an equivalence. This does not give an unpatched comparison, nor a general equivalence of the original simplicial locales.

## 2. An ambient-upper condition entirely in the compact-open lattice

Let Z=C(v)↪X be a nonzero **closed** sublocale with v∈K. Its compact-open lattice is K_Z=[v,1]_K, and an open O(k) meets Z iff k\nleq v. Define
  T_v={k∈K:k\nleq v}.
Consider the **centeredness test**
  (UB)_v: for every finite nonempty k_1,...,k_m∈T_v, ⋀_j k_j≠0 in K.
This condition is weaker than meet-primality of the zero in K_Z: it requires the meet to remain nonzero **in K(X)**, not necessarily nonzero in the quotient interval [v,1].

**Lemma (classical Priestley/prime-filter derivation).** For coherent X, (UB)_v iff there is a spectral point g∈X such that every spectral point z∈Z satisfies z≤g. If UB holds, T_v generates a proper filter in K, extendible by the prime-filter theorem to F_g. Every compact open containing z∈Z belongs to T_v⊆F_g, giving z≤g. Conversely, every compact open k meeting Z must contain g, so finite such k have nonzero meet. Note that g may be **outside Z**.

Under UB, every tuple from Z has a common upper bound in X, hence actual proconstructible equality
  H_n^X(Z):=I_n(X)∧Z^(n+1) = Z^(n+1)
for all n≥0, by the coherent point-determination theorem. In the patched Stone sheaf ∞-topos, |h(Patch H_•^X(Z))| ≃ 1, since Z^(•+1) is the Čech nerve of nonempty Stone Z→1.

## 3. A specialization-zigzag contraction entirely in the compact-open lattice

Let B=K_Z=[v,1]_K. Suppose there are bounded distributive lattice endomorphisms
  φ_0,...,φ_m:B→B
with φ_0=id, φ_m factoring through 2 (evaluation at a prime filter and subsequent inclusion 2→B), and for every i either φ_i(k)≤φ_(i+1)(k) for all k∈B, or the reverse holds for all k∈B.

The corresponding spectral endomorphisms f_i:Z→Z satisfy f_0=id, f_m constant, and each adjacent pair is **comparable as generalized specialization maps**. Indeed f≤g iff f^*(k)≤g^*(k) for all compact k. Such a comparison is an internal natural transformation between order-endofunctors. Applying the simplicial nerve gives a homotopy; composing the zigzag gives id homotopic to a constant map on |h(Patch Ch_•(Z))|. Since a constant map factors through a point 1→|Ch|, this realizes to the terminal object. This is a constructive *finite certificate* in the lattice, modulo the classical prime-filter interpretation of the last evaluation.

We call this a **specialization-zigzag contraction (SZC)**. It requires no top or bottom element in the specialization order of Z.

## 4. Improved intrinsic finite closed-cover criterion

**Theorem (new working sufficient criterion).** Let u_1,...,u_r∈K with ⋀_i u_i=0. For nonempty S⊆[r] put v_S=∨_{i∈S}u_i, Z_S=C(v_S), and B_S=[v_S,1]_K. Suppose for every nonzero Z_S *either*
  (B) the top of B_S is join-prime (Z_S has a least specialization point), *or*
  (UB+SZC) the ambient centeredness (UB)_{v_S} holds and B_S admits a specialization-zigzag contraction.
Then the **canonical** chain-to-hull maps
  C(X)→I(X), C(X)→D(X)
are equivalences in the patched Stone-sheaf ∞-topos.

**Proof:** Alternative B provides a least point ℓ in Z_S: the local chain nerve has an initial object, and the relative upper-witness simplicial object H_•^X(Z_S) has an extra degeneracy adding ℓ, since ℓ≤x_j≤y for each ambient upper witness y. Thus both realize to 1. In UB+SZC, the preceding two sections show both realize to 1. Hence every local comparison Ch_•(Z_S)→H_•^X(Z_S) is a realization equivalence. Apply the finite Čech descent theorem from the previous note to the closed cover Z_i, yielding C→I, then the edgewise arrow comparison yields C→D.

**Strictness:** Meet-prime bottom (the previous “greatest point” condition) implies UB+SZC: a greatest g∈Z provides ambient upper witness and the one-step id≤const_g. Join-prime top is retained as a separate alternative since it can contract relative H without UB. New UB+SZC also works when neither endpoint exists.

## 5. Explicit finite four-point relative certificate without endpoints

Let Z={a,b,c,d}, ordered a<c, b<c, b<d, with no other nontrivial comparisons (a four-vertex path as an order complex). Z has **no least or greatest point**:
  ↑c={c}, ↑d={d} are disjoint nonempty opens, defeating meet-prime bottom;
  ↑a={a,c}, ↑b={b,c,d} are proper opens covering Z, defeating join-prime top.

Define the monotone endomorphism f:Z→Z by
  f(a)=c, f(b)=b, f(c)=c, f(d)=d.
Then id≤f≥const_b, an SZC witnessed by a zigzag of **two** comparisons. If Z occurs as a downset in a coherent X with an ambient upper bound t (not necessarily inside Z), UB holds and the local chain-to-relative-upper comparison is an equivalence even though neither old prime-endpoint alternative holds.

## 6. Infinite coherent example with circle homotopy and a genuinely non-prime intersection

Start with the finite poset of §5 and add isolated elements e,f and maximal p,q,r, with:
- every x∈Z below p and q;
- e<q,r and f<r,p;
- no other comparisons besides those in Z and transitive consequences.

Now add a convergent sequence A={a_1,a_2,...,a_∞} of **new maximal points** with a<a_n, a<a_∞ and no other comparisons. Give P=Z∪{e,f,p,q,r}∪A the compact Stone topology a_n→a_∞, all other points isolated. The order is patch closed; upsets ↑x for all isolated x are patch clopen (↑a contains the entire convergent sequence), while tails {a_∞}∪{a_n:n≥N} separate the nonisolated a_∞ from the isolated a_n and other points. Thus it is a Priestley space, defining an infinite coherent locale X with infinitely many maximal points.

Define four patch-clopen downward-closed subspaces, hence closed proconstructible spectral sublocales with compact-open complements:
  Z_p=↓p=Z∪{f,p};
  Z_q=↓q=Z∪{e,q};
  Z_r=↓r={e,f,r};
  Z_A={a}∪A.
They jointly cover X. Each of Z_p,Z_q,Z_r has a greatest point; Z_A has least point a. Their nonempty intersections are:
  Z_p∩Z_q=Z (the four-point path with **no** endpoints);
  Z_q∩Z_r={e},  Z_r∩Z_p={f};
  Z_p∩Z_A={a}, Z_q∩Z_A={a};
  Z_p∩Z_q∩Z_A={a};
other nontrivial intersections empty.
For Z_p∩Z_q=Z, UB holds via ambient common upper p (or q), and SZC is the id≤f≥const_b contraction. This intersection violates both previous prime-endpoint alternatives.

The nerve of this four-piece closed cover has the cycle p-q-r-p, together with edges p-A,q-A and the filled triangle p-q-A. The latter triangle collapses along a free edge, leaving a circle. The finite Čech argument identifies the realizations of the patched chain and both higher-hull nerves with the constant S¹:
  C(X) ≃ I(X) ≃ D(X) ≃ underline(S¹)
via the canonical maps.
This example simultaneously goes beyond **finite maximal points** and beyond the **prime-endpoint condition on all nonempty intersections**. Its infinity and topology are genuine: A is a convergent sequence of maximal points with nonisolated a_∞.

## 7. Disposition and boundaries

**Internally checked in this turn:** the actual simplicial homotopy of block projections, the passage to sheaf realizations by objectwise presheaves and sheafification, the undercategory/relative-cofiber strengthening, UB equivalence via compact-open filters, SZC internal-category contraction, the four-point core, the explicit infinite Priestley model and intersection/nerve computation.

**External audit:** still needed before promotion into the certified theorem ledger. The relative finite-descent theorem and initial edgewise lemma on which this builds were not included in the previous 10 November blind packet. A targeted future referee request should focus on (i) the sheaf-internal homotopy in §1, (ii) frame-level equivalence of UB and the pointwise upper witness, and (iii) the infinite example's Priestley and proconstructible localic comparisons. Standard external results: edgewise subdivision of simplicial spaces (Brown–Chan–Galatius–Payne, §3.1, especially Corollary 3.9); nerve of natural transformations; compact Priestley duality; localic Čech descent for Stone covers.

**Important scope:** The theorem concerns sheaf-theoretic homotopy of **patched coherent simplicial locales**, not intrinsic localic shape or weak homotopy equivalences of unpatched simplicial locales. The unpatched D witness maps may fail *descent*, as shown by the independently refereed counterexample. A finite zigzag of lattice maps is sufficient but not necessary for internal chain contractibility, and the ambient UB condition is also sufficient rather than a classification.
