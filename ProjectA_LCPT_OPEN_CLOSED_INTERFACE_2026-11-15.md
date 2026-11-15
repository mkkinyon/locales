# Project A — exact open/closed interface calculus for oriented comparability

**15 November 2026. Internal derivation, not independently refereed.** This is a structural note for (LC-PT), with no claim of literature priority. It uses ordinary frame/sublocale conventions and keeps \(\mathcal A\) distinct from the symmetric \(\mathcal S\).

## 1. An open/closed locale extension as a filter-valued interface

Let \(U=O_X(e)\hookrightarrow X\) be open and \(F=C_X(e)\hookrightarrow X\) its closed complement. Put \(H=\mathcal O(F)\), \(G=\mathcal O(U)\). The frame \(\mathcal O(X)\) embeds into \(H\times G\) by
\[
a\longmapsto (a\vee e,\ a\wedge e).
\tag{1}
\]
Coordinates are understood through the identifications \(H=\uparrow e\) and \(G=\downarrow e\) (with respective bottom/top conventions). Injectivity follows from distributivity: if \(a\vee e=b\vee e\) and \(a\wedge e=b\wedge e\), then \(a=b\); (1) preserves arbitrary joins and finite meets.

Every \(c\in H\) appears paired with \(1_G\), and every \(v\in G\) appears paired with \(0_H\). Set
\[
N(c)=\{v\in G:(c,v)\text{ is an open of }X\}.
\tag{2}
\]
Each \(N(c)\) is a nonempty upper filter (closed under binary meets), and
\[
N(0_H)=G,\qquad
N\!\left(\bigvee_i c_i\right)=\bigcap_i N(c_i).
\tag{3}
\]
The empty-family case of (3) is included. Conversely, any assignment of nonempty upper filters satisfying (3) defines a frame
\[
L_N=\{(c,v)\in H\times G:v\in N(c)\}
\tag{4}
\]
under coordinatewise joins and finite meets, with the indicated open \(U\) and closed \(F\). In checking finite meets, use the antitonicity \(c\le d\Rightarrow N(c)\supseteq N(d)\), a consequence of (3).

This is an exact parameterization of open/closed gluing by *filter-valued* interfaces. No principal-filter or Scott-openness hypothesis is tacitly imposed.

## 2. Exact cross-comparability locus

Let
\[
C_N=\mathcal A(X)\wedge (F\times U)
\quad\hookrightarrow F\times U
\tag{5}
\]
be an **unnamed** cross-comparability sublocale. For a test locale \(E\), a map \(E\to F\times U\) is a pair of frame maps \(\alpha:H\to\mathcal O(E)\), \(\beta:G\to\mathcal O(E)\). It factors through \(C_N\) precisely when
\[
\boxed{\alpha(c)\le\beta(v)\quad\text{for all }c\in H,\ v\in N(c).}
\tag{6}
\]
Indeed, the two composites into X pull the open \((c,v)\) back to \(\alpha(c)\) and \(\beta(v)\).

Because \(e_1\le e_2\) on \(\mathcal A(X)\), the part in \(U\times F\) is zero. Decomposing \(X^2\) with the complementary open/closed sublocales in each factor, and using sublocale distributivity, gives
\[
\boxed{\mathcal A(X)=\mathcal A(U)\vee C_N\vee\mathcal A(F).}
\tag{7}
\]
Here the terms are viewed through their canonical embeddings in \(X^2\). The same partition gives \(\Delta_X=\Delta_U\vee\Delta_F\). Consequently
\[
\boxed{X\text{ is TU}\iff U,F\text{ are TU and }C_N=0.}
\tag{8}
\]
This isolates the cross term as the unique obstruction when both layers are TU. In particular, pointwise disappearance of \(C_N\) need not imply \(C_N=0\).

## 3. Caveats and use in (LC-PT)

- Equation (6) tests genuine maps from arbitrary locales; ordinary pairs of points do not suffice.
- The parameterization is exact even if \(N(c)\) has no least member. Reducing to a single quotient or a principal relation would discard important nonspatial interfaces.
- This note by itself imposes no compactness or local compactness. A concrete compact locally compact, sober \(T_1\), all-points-fitted construction with \(C_N\ne0\) is examined separately in [discrete-defect gluing](ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md).
