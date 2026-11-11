# Crosscut connectivity ladders for coherent canonical chain–hull comparisons

**11 November 2026 · New internally checked research segment, NOT independently audited.** Develops C-referee suggestion 4 and A/B-referee suggestion 3 from the [post-fourth-audit priority register](ProjectA_post_fourth_audit_research_priorities_2026-11-11.md). It gives *actual canonical-arrow* one-sided and two-sided connectivity theorems, with compact crosscuts and internal relative connectivity hypotheses. The two-sided theorem gives a geometric alternative to the independently cross-checked universal 2-connectivity theorem \(\mathbf C\to\mathbf M\) in [the canonical meet-hull account](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md). Classical connectivity crosscut theorems are known (Anders Björner, *Nerves, fibers and homotopy groups*, JCTA 102 (2003), 88–93, https://doi.org/10.1016/S0097-3165(03)00015-3); Ebert–Randal-Williams, *Semi-simplicial spaces*, AGT 19 (2019), Lemma 2.4 supplies the shifted realization lemma for spaces. The fourth audit checked the corresponding proof via connective–truncated factorization systems in an infinity-topos. **No novelty claim for classical finite crosscuts.**

## 0. Ambient conventions and connectivity

Let X be coherent, V its compact Priestley patch space, \(x\le y\) specialization, \(\mathscr H_\kappa\) our fixed Stone-sheaf infinity-topos. Let \(\mathbf C(X)=|h(\operatorname{Ch}_\bullet X)|\), \(\mathbf I(X)=|h(I_\bullet X)|\), \(\mathbf D(X)=|h(D_\bullet X)|\), and \(\mathbf M(X)=|h(M_\bullet X)|\), \(M_n=I_n\cap D_n\). All finite-dimensional witness subspaces are **patch-closed Stone subspaces of finite powers of V** by closedness of ≤ and compactness of projection. A surjective map between such spaces is a cover in the Stone site, so it becomes an effective epimorphism after h. Statements of “fibrewise connectivity” for coherent X below always refer to the **internal relative map** after sheaf realization; connectivity of ordinary set fibres is sufficient in the *finite discrete case* but must not be substituted for the internal condition in general.

A map is **n-connective** for n≥0 if it is an effective epi on π_n and an isomorphism on π_i for i<n (at all local base points); map to 1 is n-connective iff its domain is (n−1)-connected. This is Lurie's convention, called “n-connected” in some homotopy literature. The **shifted realization lemma** (cross-checked in fourth audit): if \(f_\bullet:A_\bullet\to B_\bullet\) has f_j (n−j)-connective for 0≤j≤n, then |f| is n-connective. Equivalences can be substituted for connectivity in all degrees. For a bisimplicial map f_{r,s}, applying the lemma first in s then in r shows:
\[
\forall r,s\ge0,\ r+s\le n:\quad f_{r,s}\ (n-r-s)\text{-connective}
\quad\Longrightarrow\quad |f_{\bullet,\bullet}|\ n\text{-connective}.
\tag{0.1}
\]
For boundary cases where (n-r-s)≤0 and the map is already effective epi, no extra hypothesis is required. For r or s axis the maps below are equivalences.

## 1. Patch-closed upper cofinal crosscuts and exact upper resolution

Fix any patch-closed U⊆V **upper cofinal**, i.e. ∀x∈V∃u∈U with x≤u. (U=V always works; finite P can use U=Max(P).) Let
\[
F^U_q(\mathbf u)=\bigcap_{j=0}^q\downarrow u_j,
\qquad D^U_q=\{\mathbf u\in U^{q+1}:F^U_q(\mathbf u)\ne\varnothing\}.
\]
The set D^U_q is patch closed: it is the compact projection of \(\{(x,\mathbf u):x\le u_j\ \forall j\}\).

Define bisimplicial Stone spaces
\[
B^{ch}_{p,q}=\{(x_0\le\cdots\le x_p,\mathbf u):u_j\in U,\ x_p\le u_j\ \forall j\},
\]
\[
B^{up}_{p,q}=\{(x_0,\ldots,x_p,\mathbf u):u_j\in U,\ x_i\le u_j\ \forall i,j\}.
\tag{1.1}
\]
There is a levelwise inclusion \(B^{ch}\to B^{up}\). For fixed p and varying q, both are the Čech nerves of surjective Stone witness projections onto \(\operatorname{Ch}_p(X)\), respectively \(I_p(X)\): for a chain choose u above x_p; for an upper-bounded tuple choose an upper witness w, then a u∈U above w. Consequently their q-realizations are h(Ch_p) and h(I_p), and their total canonical map **is exactly** \(\mathbf C(X)\to\mathbf I(X)\).

For fixed q, the horizontal realization of B^{up}_{p,q} is h(D^U_q): it is the Čech nerve, as p varies, of the surjective common-lower-point projection \(\{(x,\mathbf u):x\in F_q^U(\mathbf u)\}\to D^U_q\). The horizontal realization of B^{ch} is the **relative chain realization**
\[
\mathcal F^U_q:=\left|\,p\longmapsto h(B^{ch}_{p,q})\,\right|.
\]
Write \(f_q:\mathcal F^U_q\to h(D^U_q)\). We obtain
\[
\boxed{\quad
\big|q\mapsto f_q\big|\ \cong\
\big(\mathbf C(X)\longrightarrow\mathbf I(X)\big)
\quad}
\tag{1.2}
\]
as arrows in the infinity-topos (canonical, not merely objects).

At q=0 every \(\downarrow u\) has greatest element u; appending u supplies an extra degeneracy over h(U) and \(f_0\) is an equivalence. All f_q are 0-connective because \(\mathcal F_q^U\to h(D_q^U)\) is the realization of a simplicial object with degree-zero surjection of Stone spaces. In particular \(\mathbf C\to\mathbf I\) is 1-connective, agreeing with the fourth-audit rectangle groupoid calculation.

**Theorem A (upper connectivity ladder).** For n≥1, if f_q is (n−q)-connective for 1≤q≤n−1, then
\[
\boxed{\quad \mathbf C(X)\to\mathbf I(X)\text{ is n-connective.}\quad}
\tag{1.3}
\]
It is equivalent, by the audited canonical edgewise-arrow theorem, to the same bound on \(\mathbf C\to\mathbf D\).

In *finite* P with U⊆P upper-cofinal, the parameter spaces D^U_q are discrete, so the hypothesis reduces to: for each tuple \(\mathbf u\in D_q^U\), the order complex of F_q^U(\mathbf u) is (n−q−1)-connected. In particular:
- n=1: no extra hypothesis;
- n=2: connected pairwise common downsets;
- n=3: simply connected pairwise, connected triple common downsets;
- n=4: 2-connected pairwise, simply connected triple, connected quadruple.
If every nonempty finite intersection of downsets of U has **contractible relative chain realization**, then every f_q is an equivalence and so is the canonical \(\mathbf C\to\mathbf I\) map. In the finite setting this is the classical maximal-crosscut sufficient condition, *not* a new abstract homotopy-equivalence criterion.

## 2. Compact two-sided crosscuts and exact trisimplicial resolution

Choose also a patch-closed downward coinitial L⊆V: ∀x∈V∃a∈L with a≤x (take L=V in general or Min(P) in finite P). For \(\mathbf a=(a_0,\ldots,a_r)\in L^{r+1}\) and \(\mathbf u=(u_0,\ldots,u_s)\in U^{s+1}\), define the **window**
\[
F_{r,s}(\mathbf a;\mathbf u)=
\bigcap_i\uparrow a_i\ \cap\ \bigcap_j\downarrow u_j.
\tag{2.1}
\]
Let \(R_{r,s}=\{(\mathbf a,\mathbf u):F_{r,s}(\mathbf a;\mathbf u)\ne\varnothing\}\), a patch-closed compact Stone subspace of L^{r+1}×U^{s+1}. **Important:** inequalities \(a_i\le u_j\) alone need not imply R_{r,s}-membership; there must actually exist one interpolating x.

Define trisimiplicial Stone spaces
\[
T^{ch}_{p,r,s}=
\{(x_0\le\cdots\le x_p;\mathbf a,\mathbf u):
a_i\le x_0\le x_p\le u_j\ \forall i,j\},
\]
\[
T^M_{p,r,s}=
\{(x_0,\ldots,x_p;\mathbf a,\mathbf u):
a_i\le x_k\le u_j\ \forall i,j,k\}.
\tag{2.2}
\]
Their inclusion is natural in all three simplicial directions. For each fixed p, the (r,s)-object is the **product of the Čech nerves** of the lower and upper surjective witness maps to Ch_p, respectively M_p, because witness choices are independent. Iterated Čech realizations thus recover h(Ch_p) and h(M_p). For fixed (r,s), the horizontal p-realization of T^M is h(R_{r,s}), the Čech realization of \(\{(x,\mathbf a,\mathbf u):x\in F_{r,s}\}\twoheadrightarrow R_{r,s}\). Let
\[
\mathcal G_{r,s}:=\left|p\longmapsto h(T^{ch}_{p,r,s})\right|,
\qquad
g_{r,s}:\mathcal G_{r,s}\longrightarrow h(R_{r,s}).
\]
Then
\[
\boxed{\quad
\big|(r,s)\mapsto g_{r,s}\big|\ \cong\
\big(\mathbf C(X)\longrightarrow\mathbf M(X)\big).
\quad}
\tag{2.3}
\]
It is an equality of *canonical arrows* after the displayed Čech identifications.

**Two axis contractions.** For r=0, the point a_0 is the least element of the nonempty window F_{0,s}; for s=0, u_0 is its greatest element. In each case insertion of this parameter as first/last chain vertex is continuous on the Stone witness space and gives an extra degeneracy. Thus
\[
g_{0,s}\simeq\mathrm{id}_{h(R_{0,s})},
\qquad
g_{r,0}\simeq\mathrm{id}_{h(R_{r,0})}
\]
in the sense that both maps are **equivalences over their bases**. All g_{r,s} are 0-connective because the defining window is locally inhabited over R_{r,s}.

**Theorem B (two-sided connectivity ladder).** For n≥2, if \(g_{r,s}\) is (n−r−s)-connective for each r,s≥1 with r+s≤n (when r+s=n this is automatic), then
\[
\boxed{\quad\mathbf C(X)\longrightarrow\mathbf M(X)\text{ is n-connective}.\quad}
\tag{2.4}
\]
Indeed apply the shifted realization lemma first in s then in r (0.1), using the axis equivalences and interior hypotheses.

The cases have especially simple meanings:
- n=2: **no hypothesis** beyond coherent X, recovering the externally checked universal 2-connectivity theorem;
- n=3: internally connected 2-lower/2-upper windows suffice;
- n=4: internally simply connected 2×2 windows and connected 2×3 and 3×2 windows suffice;
- all degrees: if every nonempty finite window has contractible **relative chain realization**, then the *canonical* C→M is an equivalence.

For a **finite poset** with L=Min(P),U=Max(P), internal relative k-connectivity reduces to ordinary (k−1)-connectivity of the order complex of every nonempty window. This is a sufficient connectivity criterion; it is not asserted necessary, and it does **not** imply C→I or C→D equivalence in general. For example the two-level ordinal sum A₂⊕A₂ has C≃M≃S¹ but I≃D≃1.

## 3. Finite tests, including sharpness at every degree

**Face posets.** For finite simplicial complex K, P=F(K) is ordered by inclusion, L the vertices, U the facets. A nonempty two-sided window consists of faces containing the union of the lower vertex parameters and contained in the intersection of the upper facet parameters. Since a witness exists, the union is itself a face and the intersection is a face, giving **least and greatest elements** in the window. Thus all windows contract; C→M is a canonical equivalence. Likewise for any nonempty intersection of ↓facets, the intersection facet is itself the greatest element if it is nonempty, so C→I,D are canonical equivalences. Direct finite test for P=F(∂Δ²): for tuple lengths 1–3 in each crosscut direction, all **198** nonempty parameter pairs had a unique minimum and maximum.

**Layered two-antichain families, sharp in all dimensions.** Let \(P_m=(A_2)^{\oplus m}\) for m≥2. Then \(\mathbf C(P_m)\simeq S^{m-1}\), \(\mathbf I(P_m)\simeq\mathbf D(P_m)\simeq1\). For m≥3, \(\mathbf M(P_m)\simeq1\): any chosen intermediate-layer vertex is a cone point of the **symmetric M simplicial object**, because appending it preserves every tuple's existence of upper and lower bounds. At m=2, the canonical C→M is an equivalence with both types ≃S¹, even though C→I is not an equivalence.

Take U=the two maximal points and L=the two minimal points. The only noncontractible nonempty upper-crosscut intersection is ↓u₀∩↓u₁ for the **two distinct** maxima; it is \((A_2)^{\oplus(m-1)}\simeq S^{m-2}\), so the upper ladder detects precisely (m−1)-connectivity of S^{m-1}→1 for m≥2. For the two-sided ladder, if both lower parameters occur and both upper parameters occur, the window is precisely the m−2 *interior layers* with chain realization \(S^{m-3}\), for m≥3. If only one distinct lower or one distinct upper occurs the window has a minimum or maximum and is contractible. Therefore (2.4) detects **exactly (m−1)-connectivity**, and fails at n=m in the (r,s)=(1,1) condition, again sharp. In particular m=3 has the disconnected 2×2 window A₂, explaining the failure of C(S²)→M(*) to be 3-connective; m=4 has a circle window and C(S³)→M(*) is 3-connective but not 4.

**Independent finite code controls (internally executed).** For m=2,3,4,5,6, the reduced F₂ Betti vectors of the full P_m chain complexes are respectively S¹,S²,S³,S⁴,S⁵. For m≥3 the crucial 2×2 window complexes are respectively S⁰,S¹,S²,S³. Exhaustively checking every tuple in M for m=3..6 confirmed that appending a designated intermediate vertex preserves M membership, i.e. its simplicial nerve is a cone. These checks corroborate but do not replace the join/contraction proofs.

## 4. Interpretation and provenance

- The one-sided and two-sided theorems are **new internally checked work** using a **previously cross-refereed** connectivity lemma. No independent audit of these specific double/triple Čech identifications and all-parameter naturality has occurred yet.
- The finite connectivity crosscut ladder has strong classical precursors: Björner 2003, *Nerves, fibers and homotopy groups*, and poset fibre/crosscut theory (Quillen, Björner–Wachs–Welker). The potentially additional content here is the **specific canonical Stone-sheaf realization, relative internal connectivity and two-sided meet-hull formulation**, not the existence of connectivity crosscut arguments.
- **No** attempt to infer intrinsic localic shape, actual noncoherent frame formulas, or internal connectivity from every point-fibre without descent. Patch-closed U,L are crosscuts of the *point poset*, not necessarily spectral sublocales themselves.
- The two-sided condition is generally **weaker and different** than requiring both one-sided comparisons to be equivalences. For P₂=A₂⊕A₂, C→M is an equivalence but C→I,D are not.
- The next mathematical direction should return to one sharply defined **noncoherent frame-theoretic separation question** per the [ranked research program](ProjectA_post_fourth_audit_research_priorities_2026-11-11.md), after a short internal adversarial read of the current new classifying-anima identification and ladder. The finite formulas here should not be advertised as entirely new without comprehensive literature comparison.
