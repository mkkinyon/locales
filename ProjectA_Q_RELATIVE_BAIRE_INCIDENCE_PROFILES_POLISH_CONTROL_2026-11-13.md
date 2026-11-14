# Project A / Q′ — relative Baire incidence-profile obstruction and a Polish countercontrol

**13 November 2026 (America/Denver); NEW INTERNAL density segment, not externally audited. Universal Q/Q′ OPEN.** This builds on the [countable finite-test criterion](ProjectA_Q_SPATIAL_BAIRE_COUNTABLE_FINITE_TEST_DENSITY_2026-11-13.md), the [relative tail theorem](ProjectA_Q_COVERWISE_SHRINKABILITY_AND_RELATIVE_TAIL_BAIRE_2026-11-13.md), and the [closed-atomic weak-defect no-go](ProjectA_Q_CLOSED_ATOMIC_SCATTERED_WEAK_DEFECT_NO_GO_2026-11-13.md).

## 0. Setting and pointwise qualification

Let \(L=\mathcal O(X)\), \(P=L\oplus L\), \(d\in P\) with \(\Phi_2(d)=d\), and \(Y=\mathfrak c_{X^2}(d)\). Every finite-cover matching square \(w_F\) restricts to a dense open in \(Y\).

Fix an arbitrary indexed \(L\)-cover \(C=\{c_i:i\in I\}\). Let
\[
E=\mathfrak o_Y(w_C\to d)
\]
be the largest relatively open \(C\)-hole; thus \(w_C|_E=0\) and all finite-cover squares remain dense on \(E\). To apply **ordinary** Baire category below, assume \(E\) is **spatial and Baire as a topological space**. This follows if \(Y\) is spatial Baire and \(E\) is a nonzero open sublocale, but is not automatic for a general localic \(W_2\).

For a point \(z:1\to E\), write \((x_z,y_z)\) for its two endpoint points of \(X\). Define
\[
I_x=\{i\in I:x\in c_i\},\qquad I_y=\{i\in I:y\in c_i\}.
\]
Because \(C\) covers, each \(I_x,I_y\) is nonempty; because \(E\) is a \(C\)-hole, \(I_{x_z}\cap I_{y_z}=\varnothing\).

## 1. Individual profiles are nowhere dense, in each coordinate

For every \(S\subseteq I\) define
\[
a_S=\bigvee_{i\in S}c_i,\qquad b_S=\bigvee_{i\notin S}c_i,\qquad
F_S=\{a_S,b_S\}.
\]
This is a **binary \(X\)-cover**. Let \(U_S\) be its matching-square open in \(E\); it is dense open because \(d\) is finite-fixed. Consequently
\[
N_S=E\setminus U_S
\]
is a closed nowhere-dense subset of the spatial Baire space \(E\).

**Theorem 1.1 (category-small incidence-profile fibers).** For every \(S\subseteq I\), each of the sets
\[
\{z\in E:I_{x_z}=S\},\qquad \{z\in E:I_{y_z}=S\}
\]
is contained in \(N_S\), hence is nowhere dense in \(E\).

*Proof.* If \(I_x=S\), then \(x\in a_S\), \(x\notin b_S\). Since \(I_x\cap I_y=\varnothing\) and \(C\) covers, \(y\notin a_S\), \(y\in b_S\). Therefore \((x,y)\) matches neither member of the binary cover \(F_S\). The argument with the coordinates swapped is identical. □

**Corollary 1.2 (local uncountability).** For every nonempty open \(V\subseteq E\), the sets of first-coordinate and second-coordinate incidence profiles attained on \(V\) are **both uncountable**. More precisely, for every countable family \(\mathcal A\subseteq\mathcal P(I)\), the set
\[
\bigcap_{S\in\mathcal A}(U_S\cap V)
\]
is a dense \(G_\delta\) subset of \(V\), all of whose points have **neither coordinate profile in \(\mathcal A\)**.

*Proof.* Each \(U_S\cap V\) is dense open in \(V\), and nonempty open subspaces of Baire spaces are Baire. Any point with either profile \(S\) belongs to \(N_S\), so lies outside \(U_S\). Countable Baire intersection yields the conclusion. □

**Corollary 1.3 (bounded profile class).** Fix a cover \(C\) and suppose \(Y=W_2\) is spatial Baire. If the first endpoint incidence-profile map has countable range on every ordinary point of \(Y\) (or merely on some open neighborhood of each point of the putative \(C\)-hole), then \(C\) cannot witness failure of Q′. In particular, if the sober point space of \(X\) is **countable** and \(W_2(X)\) is spatial Baire, then Q′ holds for \(X\).

*Scope:* Countability of ordinary points of \(X\) alone does **not** imply that \(W_2\) is spatial Baire. No such automatic property is claimed.

## 2. Countable-cover generic two-sided infinite incidence

**Proposition 2.1.** Suppose \(C=\{c_n:n<\omega\}\), and \(E\ne0\) is spatial Baire as above. Then a dense \(G_\delta\) subset of \(E\) consists of point-pairs \((x,y)\) with
\[
I_x\cap I_y=\varnothing,\qquad |I_x|=|I_y|=\aleph_0.
\]

*Proof.* For each \(n\), put \(t_n=\bigvee_{i\ge n}c_i\). The finite family
\(\{c_0,\ldots,c_{n-1},t_n\}\) covers \(X\). Its matching square is dense open on \(E\), whereas each square \(c_i\boxtimes c_i\) vanishes on \(E\). Hence the **tail square** \(t_n\boxtimes t_n\) restricts to a dense open of \(E\). The countable intersection of these tail-square opens is dense \(G_\delta\). Every point pair therein meets a \(c_i\) with \(i\ge n\) in *both* coordinates for every \(n\); both profile sets are infinite. Disjointness holds throughout \(E\). □

This is a **two-sided** and **relative-to-the-open-hole** version of earlier infinite-incidence statements on closed coordinate supports. It remains conditional on spatial Baire \(E\).

## 3. Polish countercontrol: finite color density does not suffice

Take the Polish space \(X=[\omega]^\omega\) of all infinite subsets of \(\omega\), with the subspace topology from Cantor \(2^\omega\). Let
\[
c_i=\{A\in X:i\in A\}\qquad(i<\omega),\qquad C=\{c_i:i<\omega\}.
\]
Each \(c_i\) is clopen, and \(C\) covers \(X\). Let
\[
R=\{(A,B)\in X\times X:A\cap B=\varnothing\}.
\]
It is a **nonempty closed Polish**, hence Baire, subspace of \(X^2\). Its restriction of the same-index matching open \(w_C\) is zero.

For **every finite coloring** \(\kappa:\omega\to\{1,\dots,m\}\), form the corresponding finite cover
\[
b_\ell=\bigcup_{\kappa(i)=\ell}c_i,\qquad B_\kappa=\{b_1,\dots,b_m\}.
\]
Then \(w_{B_\kappa}|_R\) is dense open in \(R\). Indeed every basic nonempty open chart of \(R\) fixes only finitely many coordinates of \(A,B\). At least one color class is infinite; choose two fresh distinct indices \(i,j\) of that color, prescribe \(i\in A\) and \(j\in B\), and complete to disjoint infinite sets. The resulting pair lies in the chart and matches \(b_{\kappa(i)}\). This argument works in every smaller basic chart, establishing density.

Also every nonempty open chart of \(R\) has continuum many first- and second-coordinate incidence profiles; the incidence sets are simply \(A,B\), and the charts admit continuum many disjoint infinite completions. Thus **all** of the preceding Baire profile and monochromatic chromatic constraints are modeled.

**But \(R\) fails full finite-cover density.** For each \(n\), the clopen binary \(X\)-cover
\[
F_n=\{c_n,X\setminus c_n\}
\]
has matching open *not dense* in \(R\): the nonempty \(R\)-open chart \(n\in A,\ n\notin B\) misses both matching squares. In fact \(X\) is zero-dimensional Hausdorff and \(D_2(X)=\Delta_X\), so \(R\cap W_2(X)=\varnothing\). This is **not** a counterexample to Q′.

**Lesson:** Even a Polish Baire bad-\(C\) relation with maximal profile complexity and density of every finite **color coarsening of \(C\)** need not be compatible with all finite **ambient \(X\)-covers**. Future density arguments must exploit those ambient cover tests, or the special fact that a genuine defect is a **nonzero open chart inside \(W_2\)**.

## 4. Priority and audit scope

- **Positive conditional fact:** A genuine spatial Baire \(C\)-hole has no locally countable incidence-profile range in either coordinate. Countable bad covers have comeagre two-sided infinite incidence.
- **Negative control:** All finite-coloring density information, even strengthened by spatial Polish Baire geometry and continuum incidence complexity, is insufficient.
- **Next mathematical test:** Find a useful class of finite \(X\)-covers *not generated by coarsening \(C\)* that detects a hole from local incidence behavior, without automatically assuming regularity or clopen separation.
- **Closed-atomic gate:** Any **weak** defect already requires atomless least closed coordinate supports by the separately audited theorem.

**Status: internally checked direct topological and frame calculations; no external audit. Q/Q′ universally OPEN.**
