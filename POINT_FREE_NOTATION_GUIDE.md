# Point-Free Topology — compact notation and convention guide

**10 November 2026 · editorial reference, not a mathematical proof.** The main research program unifies historical A and C. Older filenames preserve their origin.

## Locale/frame conventions

- \(L=\mathcal O(X)\) is a frame; \(K(X)\) its bounded distributive lattice of compact opens for coherent X, so \(\mathcal O(X)\cong\operatorname{Idl}K(X)\). \(\operatorname{Patch}(X)\) is the associated Stone locale when X is coherent.
- **Order orientation:** for points, \(x\le y\) means **specialization**, equivalently every spectral open containing x contains y. Spectral opens are upsets; closed sublocales are downsets. An **upper witness** y satisfies \(x_i\le y\) for all i; a **lower witness** z satisfies \(z\le x_i\) for all i. Cameron–Kumar's specialization convention is the opposite of this one.
- \(C(u)\) is the **closed sublocale complementary to the open u**, not the chain realization \(\mathbf C(X)\). \(a\boxtimes b\) is a basic open rectangle. \(a^*=a\to0\) is pseudocomplement.
- \(\mathcal A_X\) or \(A_X\) is the canonical **oriented specialization localic relation**; avoid confusing it with historical “Track A”.
- Frames of powers: \(\mathcal O(X\times Y)\) is the frame **coproduct** of \(\mathcal O(X),\mathcal O(Y)\). Relation compositions based on localic images need not be associative in arbitrary locales; do not use ordinary set-relational composition silently.

## Historic binary localic separation relations

- \(\Delta\) is the diagonal, \(\mathcal I=\operatorname{cl}(\Delta)\) inseparability, \(\mathcal D=\operatorname{fit}(\Delta)\) fitted diagonal, and \(\mathcal U,\mathcal F\) are the established Urysohn and formal relations.
- \(\mathcal V=\operatorname{fit}(\mathcal I)\), \(\mathcal W=\operatorname{cl}(\mathcal D)\), \(\mathcal M=\mathcal I\wedge\mathcal D\), \(\mathcal J=\mathcal I\vee\mathcal D\), \(\mathcal H\) the alternating formal hull. Subscripts such as \(\mathcal V_n\), \(\mathcal W_2\) are iterated hierarchy operations; **not** the higher simplicial arity index below.
- For exact containment theorems, see [master ledger v2.0](PointFree_master_theorem_ledger_v2_0_2026-11-10.md); not every intuitively plausible inclusion is valid.

**For arbitrary noncoherent locales:** Present the localic specialization relation using frame inequalities for **all** frame opens, or a join-generating base, not just compact opens. The compact-open presentation is sufficient only for coherent X. This repairs the third blind referee's B1 definition gap.

## Higher diagonals and simplicial objects

- \(\Delta_{n+1}\hookrightarrow X^{n+1}\); \(I_n(X)=\operatorname{cl}(\Delta_{n+1})\), \(D_n(X)=\operatorname{fit}(\Delta_{n+1})\). The index \(n\) here denotes **arity \(n+1\)**. In coherent X, \(I_n\) has tuples with a common upper witness, \(D_n\) tuples with a common lower witness.
- \(\operatorname{Ch}_n(X)=\{x_0\le\cdots\le x_n\}\) is the specialization chain locale, an actual simplicial locale.
- \(E_{p,q}(A_X)\) is the bisimplicial rectangle object of all x_i≤y_j comparisons. It is defined by intersections; **not** by a potentially nonassociative localic relation composition.
- \(\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet X)|,\ \mathbf I(X)=|h(\operatorname{Patch}I_\bullet X)|,\ \mathbf D(X)=|h(\operatorname{Patch}D_\bullet X)|\) are sheaf-homotopy objects. **Boldface matters:** \(\mathbf C\) is not \(C(u)\).
- For a closed proconstructible Z⊂X, \(H_n^{X,\uparrow}(Z)=I_n(X)\cap Z^{n+1}\) is the **relative AMBIENT upper hull**; generally not equal to \(I_n(Z)\). The ambient lower analog \(H_n^{X,\downarrow}(U)\) is only a suggested future notation.
- **UB**: ambient upper-bound compact-open centeredness. **SZC**: spectral specialization-zigzag contraction. **SNC**: specialization-nerve contractibility \(\mathbf C(Z)\simeq1\) in the chosen sheaf \(\infty\)-topos.
- “Canonical arrows equivalent” refers to equivalence in the **undercategory** \(\mathbf C(X)/\mathscr H_\kappa\), not merely equivalence of the targets \(\mathbf I,\mathbf D\).

## Scope/provenance

- \(\mathscr H_\kappa\): a sufficiently large Stone sheaf \(\infty\)-topos with **finite jointly surjective covers including the empty cover of \(\emptyset\)**. Comparisons occur **after Patch**, not necessarily before.
- A result marked **externally blind-checked after repairs** differs from **referee-origin working**, **internally checked**, **open**, and **historical attempt**. Original external referee reports remain unchanged and separated from our later reconciliations.
- [Unified start](POINT_FREE_TOPOLOGY_START_HERE.md) · [phase index](PointFree_coherent_homotopy_PHASE_INDEX_2026-11-10.md) · [master theorem ledger](PointFree_master_theorem_ledger_v2_1_2026-11-10.md).
