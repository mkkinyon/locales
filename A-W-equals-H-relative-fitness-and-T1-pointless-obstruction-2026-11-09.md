# Project A — W=H beyond coherence: relative fitness, the regularity trap, and T1 pointless obstructions

**9 November 2026. New internally checked working segment, not externally audited or novelty-checked.** Q and Q′ remain deferred. This note concerns \(\mathcal W=\mathcal H\) as an independent hierarchy question. Standard antecedents are sourced where indicated; in particular the fit criterion for a frame element is an established result and not claimed as new.

Write \(L=\mathcal O(X)\), \(Q=L\oplus L\), \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal W=\operatorname{cl}\mathcal D=C(d)\) with \(d=d_{\mathcal W}\), \(\mathcal U=C(d_{\mathcal U})\), and \(\mathcal H\) the least simultaneously closed and fitted hull of Δ. Universally
\[
\mathcal I\le\mathcal W\le\mathcal U\le\mathcal F,\qquad
\mathcal W\le\mathcal H\le\mathcal F,\qquad
\mathcal W=\mathcal H\iff C(d)\text{ fitted}.
\]
The last equality is formal, but the results below provide concrete frame and point-space tests.

## 1. Relative fitness test: exactly one closed element

**Proposition 1 (standard specialized criterion).** For any frame Q and any d∈Q,
\[
\boxed{
C(d)\text{ fitted}\iff
\forall x\in Q,\quad d\not\le x
\Longrightarrow\exists w\in Q:
d\vee w=1,\ \ w\to x\ne x.
}
\tag{1.1}
\]
Equivalently the *fixed-point set* of the family of nuclei \(x\mapsto w\to x\), for all w satisfying d∨w=1, is precisely ↑d.

**Proof.** The fitted hull is \(S_d=\bigcap_{w\vee d=1}O(w)\). Its underlying sublocale frame consists of those x∈Q fixed by every open nucleus \(w\to-\) in this family. If d≤x and d∨w=1, any y with y∧w≤x satisfies
\(y=(y\wedge w)\vee(y\wedge d)\le x\); hence w→x=x. Conversely, x belongs to the closed C(d) precisely when d≤x. Thus equality of S_d and C(d) is equivalent to the displayed condition. □

This is the **single-closed-sublocale instance** of the established (Fit) axiom (e.g. Picado–Pultr and the subfit-biframe literature), not a newly named axiom. Applied to d=d_W it is an exact, entirely point-free test for W=H. It makes no reference to W₂ or transfinite fitting ranks.

## 2. A strong sufficient condition, and why it misses W=H<U

Define the *rather-below regular part* of d by
\[
r(d)=\bigvee\{v\in Q:v\prec d\},\qquad
v\prec d\iff v^*\vee d=1.
\tag{2.1}
\]
Equivalently
\[
\boxed{r(d)=\bigvee_{w\vee d=1}w^*.}
\tag{2.2}
\]
For one inequality, w*≺d whenever w∨d=1, since w**≥w; for the other, v≺d permits w=v* and v≤v**=w*.

**Proposition 2 (one-step sufficient condition).** If r(d)=d then C(d) is fitted.

*Proof.* If x is fixed by every nucleus \(w\to-\) with w∨d=1, then \(w^*\le w\to x=x\). Consequently
\(d=r(d)=\bigvee_{w\vee d=1}w^*\le x\), and Proposition 1 gives C(d) fitted. □

The condition r(d)=d is weaker than regularity of the **whole frame Q**; only the one element d must be a join of elements rather below it.

**Proposition 3 (regularity trap specific to W).** For any locale X, if \(d=d_{\mathcal W}\) then
\[
\boxed{r(d)\le d_{\mathcal U}\le d.}
\tag{2.3}
\]
Hence
\[
\boxed{r(d_{\mathcal W})=d_{\mathcal W}
\ \Longrightarrow\
\mathcal W=\mathcal U\text{ and }\mathcal W=\mathcal H.}
\tag{2.4}
\]
In particular, whenever W<U the sufficient condition r(d_W)=d_W **necessarily fails**.

*Proof.* Since Δ≤W=C(d), the diagonal pullback δ*:Q→L satisfies δ*(d)=0. Given v≺d, the equality v*∨d=1 gives δ*(v*)=1: v* is an open neighborhood of the diagonal. Our externally checked all-frame identity
\[
d_{\mathcal U}=\bigvee_{\delta^*(w)=1}w^*
\]
implies \(v\le v^{**}\le d_{\mathcal U}\). Joining over v yields r(d)≤d_U. The other inequality follows from W≤U and the reversed defining-open order. If r(d)=d, equality holds and Proposition 2 makes W fitted. □

**Interpretation:** regular approximation of the complement of W sees only the Urysohn-far region. It cannot capture genuinely nonregular fitted W with W<U. Thus the frame-theoretic problem must be sought in the **higher-order rather than one-step regular** behavior of the neighborhood filter. This observation is a structural limitation, not a new attempt at Q′.

## 3. Spatial T1 spaces: any failure is necessarily pointless

**Theorem 4 (working, all closed sublocales).** Let Z be a **sober spatial T1 locale** (the locale of opens of a sober T1 space). For every closed sublocale S=C(d),
\[
\operatorname{pt}(\operatorname{fit}S)=\operatorname{pt}(S).
\tag{3.1}
\]
Furthermore,
\[
\boxed{S\text{ fitted}\iff\operatorname{fit}(S)\text{ is spatial}.}
\tag{3.2}
\]
If S is not fitted, then
\[
R_S:=\operatorname{fit}(S)\wedge O(d)
\tag{3.3}
\]
is a **nonzero pointless** sublocale. Its least dense Boolean sublocale is a nonzero **atomless complete Boolean locale**.

**Proof.** A point z∉S lies in the open complement O(d), so d(z)=1. In a T1 space the set Z\\{z} is open, represented by w∈O(Z). The union w∨d=1 pointwise, and hence in the spatial frame; therefore O(w) is an open neighborhood of S excluding z. It follows that fit(S) contains no additional points. The reverse point inclusion S≤fit(S) is automatic, proving (3.1).

The closed S is spatial because it is the ordinary closed subspace of a spatial locale. If fit(S) is spatial, equality of embedded point sets and S≤fit(S) implies fit(S)=S (a spatial sublocale is the join of its point sublocales). Conversely if S fitted, fit(S)=S is spatial, proving (3.2).

Since O(d) and C(d) are complementary sublocales and the sublocale lattice is distributive, fit(S)≠S implies R_S≠0. A point of R_S would be a point of fit(S) outside S, contradicting (3.1). Thus R_S is nonzero and pointless. Its least dense Boolean sublocale B(R_S) is nonzero; it has no points, hence no atoms, because an atom of a complete Boolean frame defines a frame map to the two-element frame. □

**Corollary 5 (precise W=H test for T1 spatial squares).** If \(X\times_{\mathrm{Loc}}X\) is the locale of a sober T1 ordinary square (e.g. X is a locally compact sober T1 topological space), then
\[
\boxed{\mathcal W_X=\mathcal H_X
\iff \operatorname{fit}(\mathcal W_X)\text{ is spatial}.}
\tag{3.4}
\]
If W<H, there is a nonzero **pointless**, indeed atomless-Boolean, residual in
\(\operatorname{fit}(\mathcal W)\wedge O(d_{\mathcal W})\).

This is a *different obstruction* from the finite coherent five-point fence, where W<H is already witnessed by an ordinary point (m,n). In a spatial T1 square **ordinary point relations cannot detect failure of fittedness of a closed W**: all point differences vanish, and only pointless parts of the fitted hull can carry the defect.

This criterion is weaker than assuming the whole square is fit: it concerns the spatiality of just one fitted hull. It can prove W=H even when other closed sublocales of the square are nonfitted.

## 4. A nonfit square nevertheless having W=H<U

There are noncoherent examples where W=H<U (see the independently refereed Oct 24 compact T1 scattered α–β–γ example Y with
\[
\mathcal W_Y=\mathcal H_Y=\mathcal I_Y
\ <\ \mathcal U_Y\ <\ \mathcal F_Y).
\]
Its square is fit, which already explains fittedness of W but is stronger than necessary.

To eliminate even that global hypothesis, let S be the two-point Sierpiński locale (upper Alexandrov poset 0<1), and form the **clopen disjoint sum**
\[
X=Y\sqcup S.
\]
The known exact componentwise behavior gives W_X=H_X: on Y² the relation W_Y is fitted, on S², \(W_S=S²\) because S is hyperconnected, and on mixed component squares W_X is empty. Thus the global relation W_X is a clopen-block assembly of fitted closed relations. It is **properly below U_X** because W_Y<U_Y.

Yet \(X^2\) is **not a fit locale**. Its clopen block S² has a closed point (0,0) that is not fitted: any open in the upper Alexandrov square containing the minimum (0,0) is the whole S², so its fitted hull is S². Fitness is hereditary to clopen sublocales, therefore X² cannot be fit. (Equivalently extend this closed point in S² to the clopen block of X² and calculate its global fitted hull directly.)

This is a concrete, simple **noncoherent W=H<U example with nonfit ambient square**. Its role is to refute the temptation to regard global fitness of L⊕L as a necessary assumption for W=H.

A T1 version can be obtained (working, conditional on the sourced Arrieta input): replace S by Arrieta's spatial strongly Hausdorff anti-Urysohn non-F-separated Y₀, for which W(Y₀)=Y₀² but Δ(Y₀) is not fitted. Disjoint summing with the compact scattered Y again gives W=H<U, now with a T1 nonfit square. No local-compactness/spatial-square inference is used in this variant.

## 5. A useful structural dichotomy and a bounded next test

The results divide two kinds of possible failure of W=H:

- **Coherent non-T1 / specialization-based:** e.g. the five-point fence. W is a proper downward relation and its fitted hull adds **ordinary** upward-specialization pairs. The coherent maximal-point criterion completely describes this phenomenon.
- **Spatial T1:** no new ordinary pairs can enter \(\operatorname{fit}(W)\). A failure must be a **genuinely pointless atomless Boolean residue**, potentially visible only via complete Boolean-valued probes.

The regular part r(d_W) cannot handle W<U, by (2.3). So to understand the noncoherent W=H<U class we should analyze the local frame fitness test (1.1), not merely d_W≈regular d_U.

**Suggested next bounded test:** determine fittedness of the closed \(W=K=A_+^2\cup A_-^2<U\) for the compact non-scattered T1 *two-apex* space from the Q′ control example. This is likely a better discriminating test for the T1 pointless-obstruction mechanism than another abstract sufficient-condition search. The question is *not* Q′ and can be stopped after a precise localic computation. No external audit requested yet.

## Sources and provenance

- Established frame (Fit) condition: Picado–Pultr, *(Sub)fit biframes and non-symmetric nearness* (earlier preprint), and Ball–Picado–Pultr, *On an aspect of scatteredness in the point-free setting*, Port. Math. 73 (2016), 139–152.
- Universal d_U identity and Q′ separation: [9 Nov Q′ audit reconciliation](ProjectA_Qprime_referee_reconciliation_and_bounded_checks_2026-11-09.md).
- Coherent maximal-point criterion and five-point fence: [W=H coherent classification](A-W-equals-H-coherent-maximal-point-criterion-2026-11-09.md).
- Compact scattered T1 noncoherent counterexample: [Oct 24 post-V independent reconciliation](A-postV-external-audit-reconciliation-2026-10-24.md).
- Arrieta non-F-separated anti-Urysohn source: Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024), 108785; [our Nov 7 working analysis](A-relational-composition-associativity-audit-IV-D-cube-high-low-2026-11-07.md).
