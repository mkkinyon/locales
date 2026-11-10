# Point-Free Topology — Nerve-contractibility, finite closed-cover resolutions, and universal coherent realizations

**10 November 2026. Internally checked working mathematics, NOT independently audited.** Continuation of [edgewise-bridge and zigzag-certificate study](PointFree_edgewise_chain_hull_audit_zigzag_criterion_2026-11-10.md) and [finite closed-sublocale relative crosscut](PointFree_coherent_finite_closed_cover_relative_crosscut_2026-11-10.md). This note distinguishes standard combinatorial topology from the current patched-localic deductions. No publication-priority claim.

## 0. Conventions

Classical coherent locales X have compact-open bounded distributive lattice K(X), with spectral specialization x≤y meaning every open containing x contains y. Let A↪X² be the canonical oriented specialization sublocale, and Ch_n(X)↪X^(n+1) the locale of chains x_0≤...≤x_n. For coherent X, all Ch_n are proconstructible spectral. Fix the suitably large Stone site with **finite jointly surjective covering families** and sheaf ∞-topos H_St; h is the sheafified representable and Patch turns coherent locales into Stone locales. Define
  C(X)=|h(Patch Ch_•(X))|,
  I(X)=|h(Patch I^(•+1)(X))|,
  D(X)=|h(Patch D^(•+1)(X))|.
The earlier *still unaudited* edgewise-Dowker theorem identifies the two canonical arrows C→I and C→D in the undercategory C/H_St; the subsequent conclusions about D depend on that result. The C-only conclusions below are independently supported by finite Čech descent.

**Definition.** A nonempty coherent locale Z is *specialization-nerve contractible* (SNC) if C(Z)≃1 in H_St. This is an intrinsic property of the coherent frame in this specified ambient homotopy theory; it is not a claim about an intrinsic shape functor on Loc.

For finite Alexandrov posets P, Patch(P) is discrete; because finite disjoint-union families cover the Stone site, C(P) is exactly the constant object on the homotopy type of Ord(P). Consequently SNC is equivalent to weak homotopy contractibility of the finite order complex (and thus to its contractibility, as a finite CW complex).

## 1. A finite closed-cover nerve theorem for the chain realization

Choose c_1,...,c_r∈K(Z) with ⋀_i c_i=0, and closed proconstructible spectral sublocales Z_i=C(c_i). For nonempty S⊆[r] let
  v_S=∨_{i∈S}c_i,  Z_S=C(v_S),  K(Z_S)≅[v_S,1]_{K(Z)}.
Let N(c) denote the finite abstract simplicial complex of nonempty S with v_S≠1 (the nonzero intersections of the cover).

**Theorem 1 (finite chain good-cover formula).** If every nonzero Z_S is SNC, then
  C(Z) ≃ underline(|N(c)|)
in H_St, where underline is the constant-object functor Spaces→H_St. In particular, contractibility of N(c) implies SNC of Z.

**Proof:** Each Z_i is specialization-downward-closed and the family covers Z. Every chain's last point lies in a Z_i, hence the entire chain does. Thus Patch Ch_n(Z) has a finite jointly surjective Stone cover by the Patch Ch_n(Z_i), whose iterated fiber products are precisely the Patch Ch_n(Z_S) (all true as genuine proconstructible coherent sublocales). The degreewise augmented Čech nerve is a colimit after applying h. Commute its realization with the chain-degree realization. For each S with Z_S≠0 the latter is terminal by hypothesis, and it is initial for empty intersections. The resulting simplicial object is the nerve N(c), as a finite coproduct of 1's in each degree, so the resulting realization is underline(|N(c)|). All comparisons are natural through the maps to the terminal object, with no arbitrary choices of contractions needed.

**Compact-open certificate.** At every nonempty S, if the bottom of [v_S,1] is meet-prime or the top is join-prime, then Z_S has a greatest or least spectral point, hence SNC by an extra degeneracy. More generally SNC of each intersection may be certified by another finite closed cover; this supplies *recursive good-cover certificates*. The conditions are genuinely frame-theoretic because the nerve is determined by the finite join equalities v_S=1 and endpoint tests in bounded lattice intervals.

## 2. Why this is strictly weaker than comparable-endomorphism zigzags

A *spectral specialization-zigzag contraction* of Z is a finite chain of bounded lattice endomorphisms
  φ_0=id, φ_1,...,φ_m=constant-point homomorphism
with adjacent maps pointwise comparable. Equivalently there is a finite chain of spectral order-preserving endomorphisms id=f_0 ⋚ f_1 ⋚...⋚ f_m=const_z. Such a zigzag contracts the internal chain nerve, so SNC follows.

**The converse is false already for finite coherent locales.** For a finite T0 poset P, finite comparable-map zigzags id→const are exactly ordinary homotopies of finite Alexandrov spaces (Stong's strong homotopy), whereas C(P)≃1 asks only that |Ord(P)| be contractible. Cianci–Ottina, *Smallest weakly contractible non-contractible topological spaces*, Proc. Edinb. Math. Soc. 63 (2020), 263–274, prove that there are exactly two minimal examples on nine points and no such example below nine points; arXiv:1608.05307. Thus no universal finite-zigzag characterization of SNC is possible.

**Concrete family using a dunce-hat triangulation.** Let T be any finite triangulation of the dunce hat with no free edges (standard eight-vertex triangulations exist), and P=F(T) its poset of nonempty simplices ordered by inclusion. The order complex Ord(P)=sd(T) is contractible, so C(P)≃1. But P has no beat points:
- a vertex has multiple incident edges, so no minimal strict upper face;
- an edge has two incomparable vertex subfaces and at least two triangular cofaces, so no beat direction;
- a triangle has multiple incomparable proper faces and no upper faces.
Stong's core theorem implies P is not contractible as a finite topological space, hence it has **no** finite comparable-endomorphism zigzag id→const. On the other hand, P admits a finite frame-theoretic good-cover certificate: for each maximal triangle F, the principal downset ↓F is a closed proconstructible sublocale; any nonempty finite intersection is the principal downset ↓(intersection of facets), with a greatest element. The facet-cover nerve is homotopy equivalent to T by the classical simplicial nerve theorem; it is therefore contractible. Theorem 1 certifies SNC without zigzags.

Reference for existence and no free edges: Benedetti–Lutz triangulations of dunce hat as surveyed in *Random simple-homotopy theory* (2023); for beat-point criterion see Stong / Barmak's finite-space theory. The nine-point examples give even smaller instances of the conceptual gap, without a specified facet-cover presentation.

## 3. Universality: every finite simplicial homotopy type from a genuinely infinite coherent locale

**Theorem 2 (coherent convergent-maximal-point inflation).** Let T be any nonempty finite abstract simplicial complex and choose a vertex v. There is an infinite coherent locale X_T with infinitely many maximal specialization points and a nonisolated patch point, such that
  C(X_T) ≃ I(X_T) ≃ D(X_T) ≃ underline(|T|),
the equivalences C→I,D being induced by the canonical simplicial inclusions.

**Construction:** Let P=F(T), the finite face poset of nonempty simplices. Adjoin a convergent sequence A={a_1,a_2,...,a_∞}, topologized as a Stone convergent sequence, with all points of P isolated. Define the partial order by the original face inclusions in P and
  v<a_n (all n),   v<a_∞,
and no other new nonreflexive comparisons. The new A points are maximal and pairwise incomparable. The order relation is patch closed: the only accumulating new comparisons v<a_n converge to the included pair v<a_∞. It is Priestley: for an original face σ, ↑σ is a clopen upset (if σ=v it contains all of A; otherwise it is finite original faces); for a_n, singleton {a_n} is clopen upset; for a_∞, clopen cofinite tails of A separate it from every point to which it is not ≤. Thus the spectral topology of patch-clopen upsets yields a genuine infinite coherent locale X_T.

**Finite closed cover:** For each maximal facet F of T, let Z_F=↓F (the finite set of nonempty faces contained in F), and let Z_A={v}∪A. These are patch-clopen downsets, hence closed proconstructible sublocales whose complements are compact spectral opens, and they cover X_T. For a nonempty subfamily of facets F_i,
  ⋂_i Z_{F_i}= ↓(⋂_i F_i) if the intersection face is nonempty, else ∅.
Such a nonempty intersection has greatest element ⋂_i F_i. Also Z_A has least element v, and
  Z_A∩ ⋂_i Z_{F_i}={v} if v belongs to all F_i, else ∅.
Thus EVERY nonempty intersection has a greatest or least specialization point. The frame-theoretic certificate in Theorem 1 applies to compute C(X_T); the previous finite closed-cover *relative* chain-to-I theorem applies to the SAME cover, and the edgewise bridge gives the D comparison.

Let N_F be the nerve of the facet cover {↓F} of P. The classical nerve theorem gives |N_F|≃|T| because facet intersections are principal downsets (and Ord(P)=sd T). The additional index A attaches a cone on the simplex spanned by those facets containing v. This simplex is already contained in N_F (all of them intersect at v), so attaching its cone does not change the homotopy type. Therefore the fourfold (or generally m+1-fold) cover nerve N' satisfies |N'|≃|T|. All three patched realizations are the constant object on this finite homotopy type.

**Important limitations:** This is NOT a theorem asserting the intrinsic localic shape of X_T equals |T|, and NOT a claim that every coherent locale meets a good-cover criterion. It shows that the patched chain/higher-hull homotopy theory is rich enough to realize every finite simplicial homotopy type, even under canonical chain-to-hull comparison equivalences.

## 4. An infinite coherent SNC example with NO finite specialization zigzag

Choose T to be a finite no-free-edge triangulation of the contractible dunce hat. Theorem 2 gives
  C(X_T)≃I(X_T)≃D(X_T)≃1.
Yet X_T has **no** finite spectral specialization-zigzag contraction. Indeed P=F(T) is a spectral retract of X_T: inclusion j:P→X_T is the proconstructible spectral sublocale on the original finite face set, and r:X_T→P fixes P and sends all a_n,a_∞ to the chosen vertex v. This r is patch-continuous (each original singleton is clopen, and r^{-1}({v})={v}∪A is patch-clopen), and order-preserving, hence spectral in Priestley duality. Then rj=id_P. If X_T admitted a finite zigzag id=f_0 ⋚ ... ⋚ f_m=constant, the composites r f_i j would give such a zigzag id_P ⋚ ... ⋚ constant on P, contradicting Stong's beat-point criterion. Thus SNC is *strictly weaker* than the previous compact-open zigzag certificate even for infinite coherent frames with a nonisolated patch point.

## 5. Stronger relative finite closed-cover criterion without zigzags

Let X be coherent and (Z_i=C(u_i)) a finite closed cover with relative common-upper simplicial locales H^X_•(Z_S)=I_•(X)∧Z_S^(•+1). Suppose for each nonempty intersection Z_S, either:
  (i) Z_S has a **least** spectral point, so the relative H is conical at this point and its chain nerve contractible; or
  (ii) its ambient compact-open centeredness UB_v holds (every finite family of compact opens meeting Z_S has nonzero meet in K(X)), **and Z_S is SNC** (perhaps by Theorem 1).
Then the canonical patched arrows C(X)→I(X) and C(X)→D(X) are equivalences. Proof: in (ii), UB_v ensures H_n^X(Z_S)=Z_S^(n+1) as actual proconstructible spectral sublocales, whose realization is terminal; C(Z_S) is terminal by SNC. In (i), the least point contracts both. Apply finite Čech descent and the edgewise comparison. This **strictly weakens the local zigzag certificate**, since there exist SNC locales with no such zigzag.

**Optional nontrivial global example:** Take the finite face poset P=F(T) of the dunce hat and a vertex v of T. Adjoin new maximal p,q above all P; add e,f,r with e<q,r and f<r,p; and add the convergent maximal sequence A above v, no other comparabilities. The resulting Priestley locale X has a finite patch-clopen downward cover
  Z_p=P∪{f,p},   Z_q=P∪{e,q},   Z_r={e,f,r},   Z_A={v}∪A.
Each main piece has a greatest or least point; pairwise intersections are P (for p,q), {f}, {e}, {v}, or empty, and the only nonempty triple intersection is {v} (p,q,A). The intersection P has UB via p or q and is SNC by the facet-cover good-nerve certificate, but has no SZC. The cover nerve is the triangle boundary p-q-r-p, with a filled triangle p-q-A glued along pq: homotopy equivalent to S¹. The *new* relative criterion proves
  C(X)≃I(X)≃D(X)≃underline(S¹)
via canonical maps. This is a strict extension at the level of local proof certificates; it is not proved that no alternative cover might satisfy an earlier condition.

## 6. Research status / boundaries

- The finite chain good-cover formula and all-locale lattice presentation are direct Čech and compact-open computations, internally checked in this segment.
- The gap between simplicial weak contractibility and finite zigzags is well-established finite-space topology (Stong, Barmak, Cianci–Ottina); the dunce-hat facet-cover certificate is a standard good-cover application.
- The infinite coherent universal construction is a new **working synthesis within this project**, not a claimed new theorem in the literature. Its D-side depends on the previously internally audited but not independently referee-reviewed edgewise-Dowker compatibility.
- The relative criterion allows SNC, not just explicit finite zigzags, as a local hypothesis. It should be externally audited with the infinite examples before promotion to the stable theorem ledger.
- Future useful research direction: find localic, intrinsically meaningful situations in which C(X) can be computed from *covers not necessarily of closed/downset type*, or whether the finite-lattice pro-approximation can compare its patched \infty-topos realization to a pro-homotopy object. Avoid conflating it with shape(X) or the unpatched s_q descent problem.

**Literature:** Cianci–Ottina, *Smallest homotopically trivial non-contractible spaces* (arXiv:1608.05307, published Proc. Edinburgh Math. Soc. 63 (2020)); Stong's finite-space core theorem; Barmak, *Algebraic topology of finite topological spaces and applications*; Benedetti–Lutz dunce-hat triangulations; Rota/Björner crosscut and classical simplicial nerve theorem.