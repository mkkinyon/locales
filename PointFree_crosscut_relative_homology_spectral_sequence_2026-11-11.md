# Project A — Crosscut connectivity ladders: relative homology and obstruction spectral sequences

**11 November 2026. New internally checked continuation of the crosscut-connectivity programme; not independently audited.** This supplements [the canonical-arrow connectivity ladders](PointFree_crosscut_connectivity_ladder_2026-11-11.md), whose definitions and site-specific qualifications are retained. The new finite-poset construction is a relative Čech–Mayer–Vietoris spectral sequence, so a close classical antecedent should be expected (Björner, *Nerves, fibers and homotopy groups*, JCTA 102 (2003), 88–93; standard Mayer–Vietoris spectral sequences). The new point for our project is the **specific relative canonical map** and its two-sided meet-hull version. No novelty assertion or homotopy-connectivity converse is made.

## 1. The one-sided relative crosscut spectral sequence

Let P be a nonempty **finite** poset and let U⊆P be upper cofinal. For an ordered tuple \(\mathbf u=(u_0,\ldots,u_q)\in U^{q+1}\), put
\[
F_q(\mathbf u)=\bigcap_{j=0}^q\downarrow u_j,
\quad D_q=\{\mathbf u:F_q(\mathbf u)\ne\varnothing\}.
\]
Write \(\mathbf C(P)=|\operatorname{Ch}_\bullet(P)|\) for the order-complex realization and \(\mathbf I(P)=|I_\bullet(P)|\) for the common-upper-witness complex. The canonical comparison is \(\iota:\mathbf C(P)\to\mathbf I(P)\). For any commutative ring \(R\), use relative homology \(H_*(\mathbf I(P),\mathbf C(P);R)\), meaning the homology of the **mapping cone of \(\iota\)** (no assertion that the map is a cofibration is needed).

**Theorem A (relative crosscut spectral sequence; working).** There is a natural homological first-quadrant spectral sequence
\[
\boxed{E^1_{q,t}=\bigoplus_{\mathbf u\in D_q}^{\mathrm{norm}}
\widetilde H_{t-1}\bigl(|\operatorname{Ord}(F_q(\mathbf u))|;R\bigr)
\quad\Longrightarrow\quad H_{q+t}(\mathbf I(P),\mathbf C(P);R).}
\tag{1.1}
\]
Here \(q,t\ge0\), and the direct sum is normalized in the simplicial-Čech **q direction**, so tuples with **adjacent repeated entries** are removed. Each \(F_q\) is nonempty by definition. Set \(\widetilde H_{-1}(F_q)=0\) in this nonempty setting. The differential \(d^1:E^1_{q,t}\to E^1_{q-1,t}\) is the alternating sum of the homology maps induced by deleting one parameter \(u_j\), using the inclusion \(F_q(\mathbf u)\subseteq F_{q-1}(\partial_j\mathbf u)\). This normalization is compatible with these maps, including the faces of degenerate tuples. \(q=0\) contributes zero, since \(F_0(u)=\downarrow u\) has a maximum.

*Proof.* Use the **exact upper resolution** of the earlier crosscut note: bisimplicial sets
\[
B^{ch}_{p,q}=\{(x_0\le\cdots\le x_p;\mathbf u):x_p\le u_j\},\quad
B^{up}_{p,q}=\{(x_0,\ldots,x_p;\mathbf u):x_i\le u_j\ \forall i,j\}.
\]
After realizing in q, their p-levels recover \(\operatorname{Ch}_p(P)\) and \(I_p(P)\) by the Čech nerves of the surjective upper-witness maps. Thus the realized bisimplicial map is the **canonical** inclusion \(\iota\). For fixed \(q\), the p-realization is, respectively,
\[
\coprod_{\mathbf u\in D_q}|\operatorname{Ord}(F_q(\mathbf u))|
\longrightarrow \coprod_{\mathbf u\in D_q}*.
\]
Apply normalized free \(R\)-chains, take the chain-level mapping cone, and filter the resulting bisimplicial total complex by the q-degree. The vertical homology in relative degree t at \(\mathbf u\) is
\[
H_t(*,|\operatorname{Ord}(F_q(\mathbf u))|;R)
\cong\widetilde H_{t-1}(|\operatorname{Ord}(F_q(\mathbf u))|;R).
\]
The horizontal differential is alternating deletion of parameters. The first-quadrant filtration is exhaustive and finite in each total degree; the resulting spectral sequence converges strongly to the homology of the mapping cone of \(\iota\). This proves (1.1). □

**Consequences.** Since \(q=0\) and \(t=0\) vanish, the relative groups \(H_0,H_1(\mathbf I,\mathbf C;R)\) vanish unconditionally. More generally, if every nonempty \((q+1)\)-fold upper crosscut \(F_q\) has \(\widetilde H_j(F_q;R)=0\) for \(0\le j\le n-q-1\), for \(1\le q\le n-1\), then \(H_k(\mathbf I,\mathbf C;R)=0\) for \(k\le n\). **This is a homological version** of the homotopy-connectivity ladder, not an if-and-only-if or a replacement for fundamental-group hypotheses.

## 2. Two-sided window spectral sequence

Choose also a downward coinitial L⊆P. For \(r,s\ge0\), let
\[
F_{r,s}(\mathbf a;\mathbf u)
=\bigcap_{i=0}^r\uparrow a_i\cap\bigcap_{j=0}^s\downarrow u_j,
\quad R_{r,s}=\{(\mathbf a,\mathbf u):F_{r,s}\ne\varnothing\}.
\]
Write \(\mathbf M(P)=|M_\bullet(P)|\), the two-sided common-witness simplicial complex, and let \(\iota_M:\mathbf C(P)\to\mathbf M(P)\) be the canonical inclusion.

**Theorem B (relative two-sided crosscut spectral sequence; working).** For each commutative ring R, there is a first-quadrant spectral sequence
\[
\boxed{E^1_{j,t}=
\bigoplus_{\substack{r+s=j\\r,s\ge0}}
\bigoplus_{(\mathbf a,\mathbf u)\in R_{r,s}}^{\mathrm{norm}}
\widetilde H_{t-1}\bigl(|\operatorname{Ord}(F_{r,s}(\mathbf a;\mathbf u))|;R\bigr)
\quad\Longrightarrow\quad H_{j+t}(\mathbf M(P),\mathbf C(P);R).}
\tag{2.1}
\]
Normalization independently deletes adjacent repeated lower or upper parameters. The \(d^1\) differential is the signed sum of all lower and upper face maps, with total-complex sign convention \(d=d_r+(-1)^r d_s\). **Both axes vanish:** if r=0 the window has least point \(a_0\), while if s=0 it has greatest point \(u_0\). Thus only r,s≥1 appear on E¹.

*Proof.* Start with the exact trisimplicial comparison in the preceding note:
\[
T^{ch}_{p,r,s}=\{(x_0\le\cdots\le x_p;\mathbf a,\mathbf u):a_i\le x_0\le x_p\le u_j\},
\]
\[
T^M_{p,r,s}=\{(x_0,\ldots,x_p;\mathbf a,\mathbf u):a_i\le x_k\le u_j\ \forall i,j,k\}.
\]
Realization in (r,s) recovers \(\operatorname{Ch}_p(P)\to M_p(P)\), via the product of two witness Čech resolutions. For fixed (r,s), p-realization is the disjoint union of maps \(|\operatorname{Ord}(F_{r,s})|\to*\). Filter the total mapping-cone complex by total parameter degree j=r+s. Its vertical homology is the direct sum in (2.1). There are two kinds of horizontal face maps; with the standard sign convention these give d¹. The filtration is first quadrant and converges as above. □

**Consequences.** Because both axes vanish and the relative t=0 row vanishes, we have **unconditional homological vanishing**
\[
H_k(\mathbf M(P),\mathbf C(P);R)=0\qquad(k\le2).
\tag{2.2}
\]
This is the homological shadow of the previously independently cross-reviewed **2-connectivity** of \(\mathbf C\to\mathbf M\). For n≥3, vanishing of \(\widetilde H_i(F_{r,s};R)\) for \(i\le n-r-s-1\) on all windows with \(r,s\ge1,\ r+s\le n-1\) yields \(H_k(\mathbf M,\mathbf C;R)=0\) for all k≤n. This does **not** by itself prove n-connectivity in homotopy.

## 3. First obstructions and sharp layered families

Let \(P_m=(A_2)^{\oplus m}\), an ordinal sum of m two-point antichains, m≥3; choose U=the two maxima and L=the two minima. Then \(\mathbf C(P_m)\simeq S^{m-1}\), while \(\mathbf I(P_m)\simeq\mathbf M(P_m)\simeq *\). Thus
\[
H_k(\mathbf I(P_m),\mathbf C(P_m);\mathbb Z)
\cong H_k(\mathbf M(P_m),\mathbf C(P_m);\mathbb Z)
\cong\begin{cases}\mathbb Z&k=m,\\0&k\ne m.\end{cases}
\tag{3.1}
\]

In Theorem A, the only noncontractible upper windows are those containing **both** distinct maxima; each is \(P_{m-1}\), with order realization \(S^{m-2}\). Its reduced homology lies at degree m−2, and so contributes to E¹ at \(t=m-1\). Alternating upper tuples remain after normalization. Their d¹ gives the normalized Čech chain complex with two symbols, modulo the two singleton cones: its homology has **one copy of Z in q=1**. Therefore the first and only surviving class lies in total degree \(q+t=1+(m-1)=m\).

In Theorem B, the only noncontractible windows contain **both** distinct minima and **both** distinct maxima. Their order complex is \(S^{m-3}\), so their relative contribution is at \(t=m-2\). The double normalized Čech parameter directions, each built from alternating two-symbol tuples and starting at degree 1, contribute a single copy of Z in bidegree \((r,s)=(1,1)\). The unique surviving class lies in total degree \(r+s+t=1+1+(m-2)=m\). In particular:
- m=3: disconnected 2×2 window \(A_2=S^0\), causing the relative \(H_3\cong\mathbb Z\) obstruction;
- m=4: circle window \(P_2\simeq S^1\), causing \(H_4\cong\mathbb Z\);
- m=5: sphere window \(P_3\simeq S^2\), causing \(H_5\cong\mathbb Z\).

**Finite direct checks, independent of spectral-sequence indexing.** A bit-matrix reduction of the actual relative simplicial inclusion complexes \(C_*(I(P_m),\operatorname{Ord}(P_m);\mathbb F_2)\) and \(C_*(M(P_m),\operatorname{Ord}(P_m);\mathbb F_2)\) for m=3,4,5 gives precisely one nonzero homology group, rank 1 in degree m, in each case. For m=2, the two-sided map is literally an equality of simplicial complexes, while the one-sided relative group is \(H_2\cong\mathbb F_2\). These computations corroborate the formulas but the join/cone proof establishes the integral claims without relying on computation.

## 4. Sufficient criteria are not necessary: a redundant-crosscut example

Begin with P₃, and **adjoin a new greatest element t** above both of the original maxima. Let L be its original two minimal points and let U consist of the original two maxima **together with t**; U remains upper cofinal (though not minimal). Then \(\operatorname{Ord}(P)\) is contractible (terminal object t). So is I(P) (all tuples have upper witness t). Moreover M(P) is contractible: appending t to any M-simplex preserves a common lower witness, while t supplies a common upper witness. Thus **both canonical maps C→I and C→M are homotopy equivalences** (maps between nonempty contractible spaces).

Nevertheless \(\downarrow u_0\cap\downarrow u_1\) for the two **original** maxima is \(P_2\simeq S^1\), and \(\uparrow a_0\cap\uparrow a_1\cap\downarrow u_0\cap\downarrow u_1\) for the two original minima and maxima is the two isolated middle points \(A_2\simeq S^0\). Consequently the n=3 homotopy ladder hypotheses **fail** for this choice of crosscuts, although the canonical comparisons are equivalences. At the E¹ page the apparent local obstructions are killed by other parameter faces involving t.

This is a concrete reminder that the ladder conditions are **sufficient**, not necessary, and the **crosscut choice affects E¹ but not its abutment**. Choosing U={t} instead makes the one-sided crosscut trivial, illustrating the redundancy responsible for this counterexample.

## 5. Coherent Stone-sheaf version: exact form and scope

The finite spectral sequences are a shadow of a general construction in the patched Stone-sheaf ∞-topos \(\mathscr H_\kappa\), using the exact resolutions \(f_q:\mathcal F_q\to h(D_q)\) and \(g_{r,s}:\mathcal G_{r,s}\to h(R_{r,s})\) from the earlier note. For any coefficient ring R, let \(R[-]\) denote free R-module linearization of objects of \(\mathscr H_\kappa\). Apply the stable mapping-cone construction to
\[
R[\mathcal F_q]\to R[h(D_q)],\qquad R[\mathcal G_{r,s}]\to R[h(R_{r,s})].
\]
Filter their simplicial/bisimplicial totalizations by q or by j=r+s. The associated spectral sequences have E¹ sheaves
\[
E^1_{q,t}=\mathcal H_t\!\left(\operatorname{cofib}(R[\mathcal F_q]\to R[h(D_q)])\right),
\tag{5.1}
\]
\[
E^1_{j,t}=\bigoplus_{r+s=j}\mathcal H_t\!\left(\operatorname{cofib}(R[\mathcal G_{r,s}]\to R[h(R_{r,s})])\right),
\tag{5.2}
\]
converging in the ordinary first-quadrant/connective range to the relative R-homology sheaves of the actual canonical comparison maps. The differential is induced by the Čech face maps. Axis-equivalence and degree-zero cover-surjectivity imply the same vanishing lines; sheaf-valued relative homology is not replaced by point-fibre homology.

**Important scope:** (5.1)–(5.2) are a *working derived-Čech formulation*; unlike the finite-poset formulas, their full model/site and convergence bookkeeping has not received a separate adversarial audit. In particular, for infinite Stone parameter spaces, one must NOT replace the displayed homology sheaves by direct sums of ordinary homology groups indexed by points. The previously checked infinity-topos **connectivity** ladder remains the stronger, established homotopical statement; these spectral sequences illuminate its homological obstruction groups but do not automatically yield higher homotopy connectivity.

## 6. Provenance and next step

**Known antecedents:** Standard Mayer–Vietoris/Čech spectral sequences for covers and relative homology, and Björner's classical connectivity nerve theorem (JCTA 102 (2003), 88–93, DOI https://doi.org/10.1016/S0097-3165(03)00015-3). The direct recovery of the relative *canonical inclusion maps* C→I and C→M uses the previous exact double/triple Čech resolutions; these remain internally checked, not blind refereed. No claim of novelty for classical homology spectral sequences is justified.

**Research outcome:** This segment provides a computable E¹-page, precise first obstruction degrees, and a concrete non-necessity example. It does not assert that the full relative homology determines the map up to homotopy. A bounded next step would be a **specific comparison with the relative π₁/π₂ defect modules** from the fourth-audit rectangle calculation, or else return to one noncoherent frame-theoretic problem as recommended in the priority register. Avoid indefinite elaboration of familiar spectral-sequence technology.

**Status: internal working mathematics, not independently audited.**