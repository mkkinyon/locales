# Blind audit packet — two-sheet zero-dimensional specialization and fitting

**15 November 2026. Claims for independent review, not assumed correct.** This packet is self-contained; it does not include the authors' internal audit.

## A. Definitions and elementary facts

For any locale \(X\), let \(\mathcal A(X)\hookrightarrow X\times X\) denote the canonical oriented specialization relation specified by:
\[
(f,g):E\to X\times X\text{ factors through }\mathcal A(X)
\iff f^*(a)\le g^*(a)\text{ for every }a\in\mathcal O(X),
\tag{A1}
\]
for **every locale** \(E\). Let \(\Delta_X\) be the diagonal. For \(S\hookrightarrow X\), define
\[
\operatorname{Sat}_{\mathcal A,X}(S)
=\operatorname{im}\bigl(\mathcal A(X)\wedge(S\times X)\xrightarrow{\pi_2}X\bigr).
\tag{A2}
\]

The fitting \(\operatorname{fit}_X(S)\) is the intersection, **in the lattice of sublocales**, of all open sublocales containing \(S\). We assume the standard facts that the sublocale lattice is a **coframe**; corresponding open and closed complements \(U=O_X(e)\), \(F=C_X(e)\) satisfy \(F\wedge U=0\), \(F\vee U=X\); and \(\mathcal A\) is reflexive. Thus
\[
S\le\operatorname{Sat}_{\mathcal A}(S)\le\operatorname{fit}(S).
\tag{A3}
\]

Every zero-dimensional locale is regular, hence **fit**, meaning **every** sublocale is an intersection of open sublocales. Zero-dimensional means the complemented opens generate \(\mathcal O(K)\) under arbitrary joins; no assumption of spatiality is intended.

## B. Two-sheet construction

Let \(K\) be zero-dimensional. Suppose \(L=\mathcal O(Z)\) is a subframe of \(\mathcal O(K)\times\mathcal O(K)\), with joins and finite meets coordinatewise, and satisfies:

- \(e=(0,1)\in L\), with open sheet \(U=O_Z(e)\cong K\) (the second coordinate) and complementary closed sheet \(F=C_Z(e)\cong K\) (the first coordinate);
- \((d,d)\in L\) whenever \(d\in\mathcal O(K)\) is complemented.

As clopens generate the frame and \(L\) is closed under arbitrary joins, \((c,c)\in L\) for every \(c\in\mathcal O(K)\). Define the fitted sublocale
\[
P:=\bigwedge_{\,(1,v)\in L}O_K(v)\hookrightarrow K.
\tag{B1}
\]
For \(H\hookrightarrow K\), write \(H_F\hookrightarrow Z\) or \(H_U\hookrightarrow Z\) for its embedding in the indicated sheet.

### Claim 1 (exact cross-sheet relation)

\[
\boxed{\mathcal A(Z)\wedge(F\times U)=\Delta_K(P)}
\quad\text{inside }K\times K.
\tag{B2}
\]
The restrictions of \(\mathcal A(Z)\) to \(F\times F\) and \(U\times U\) are the diagonals, while \(\mathcal A(Z)\wedge(U\times F)=0\).

**Proposed proof.** A generalized comparable pair \((f,g):E\to F\times U\) yields \(f_0,g_0:E\to K\). For every complemented \(d\), comparability for \((d,d)\) and \((d^c,d^c)\) gives inequalities in both directions, hence \(f_0^*d=g_0^*d\). Since clopens generate \(\mathcal O(K)\), \(f_0=g_0=h\). Comparison for every global \((1,v)\in L\) gives \(h^*v=1\), so \(h\) factors through \(P\).

Conversely, for \(h:E\to P\), let \((c,v)\in L\) and \(d\le c\) be complemented. The coordinatewise identity
\[
(c,v)\wedge(d,d)\vee(d^c,d^c)
=(1,v\vee d^c)\in L
\tag{B3}
\]
shows \(h^*(v\vee d^c)=1\). Thus \(h^*d\le h^*v\). Taking the join over all complemented \(d\le c\) gives \(h^*c\le h^*v\). So \((h_F,h_U)\) factors through \(\mathcal A(Z)\). For a same-sheet pair, clopens and their complements force equality; the reverse block is empty by comparison on \(e=(0,1)\). \(\square\)

### Claim 2 (arbitrary first-sheet sublocale)

For every sublocale \(H\hookrightarrow K\), without closedness or compactness,
\[
\boxed{\operatorname{Sat}_{\mathcal A,Z}(H_F)
=\operatorname{fit}_Z(H_F)
=H_F\vee(P\wedge H)_U.}
\tag{B4}
\]

**Proposed proof.** Reflexivity and (B2) yield
\[
H_F\vee(P\wedge H)_U
\le\operatorname{Sat}(H_F)\le\operatorname{fit}(H_F).
\tag{B5}
\]
Write \(T=\operatorname{fit}_Z(H_F)\). Every global open \((1,v)\) contains \(H_F\), so \(T\wedge U\le P_U\). Every diagonal open \((c,c)\) with \(H\le O_K(c)\) also contains \(H_F\). Because \(K\) is fit, meeting their traces in U gives \(T\wedge U\le H_U\). The corresponding diagonal traces in F give \(T\wedge F=H_F\). Thus
\[
T=(T\wedge F)\vee(T\wedge U)
\le H_F\vee(P\wedge H)_U.
\tag{B6}
\]
Together with (B5), this proves (B4). \(\square\)

### Claim 3 (finite joins of exact-saturation sources)

If \(\operatorname{Sat}(S)=\operatorname{fit}(S)\) and \(\operatorname{Sat}(T)=\operatorname{fit}(T)\), then
\[
\operatorname{Sat}(S\vee T)=\operatorname{fit}(S\vee T).
\tag{B7}
\]
**Proposed proof.** Finite joins of fitted sublocales are fitted: the sublocale coframe law gives
\[
\Bigl(\bigwedge_i O_i\Bigr)\vee\Bigl(\bigwedge_j V_j\Bigr)
=\bigwedge_{i,j}(O_i\vee V_j),
\]
where all \(O_i,V_j\) are open, and a join of two open sublocales is open. Hence fitting preserves finite joins. Using **monotonicity** of saturation, rather than assuming it preserves joins,
\[
\operatorname{fit}(S\vee T)
=\operatorname{Sat}(S)\vee\operatorname{Sat}(T)
\le\operatorname{Sat}(S\vee T)
\le\operatorname{fit}(S\vee T).
\quad\square
\]

### Claim 4 (main theorem: every source in one step)

For every sublocale \(G\hookrightarrow Z\), with \(H_F=G\wedge F\),
\[
\boxed{
\operatorname{Sat}_{\mathcal A,Z}(G)
=\operatorname{fit}_Z(G)
=G\vee(P\wedge H)_U.}
\tag{B8}
\]
In particular, the saturation operation is idempotent on **all** sublocales of \(Z\).

**Proposed proof.** As \(F\vee U=Z\) and \(\mathcal S(Z)\) is distributive,
\[
G=(G\wedge F)\vee(G\wedge U)=H_F\vee C_U.
\tag{B9}
\]
Every sublocale \(C\hookrightarrow U\cong K\) is fitted in U, because K is zero-dimensional and fit. Since U is open in Z, its open sublocales are open in Z, so \(C_U\) is fitted in Z. Then \(\operatorname{Sat}(C_U)=C_U\) by (A3). Apply Claims 2 and 3 to (B9), obtaining
\[
\operatorname{Sat}(G)=\operatorname{fit}(G)
=\operatorname{fit}(H_F)\vee C_U
=G\vee(P\wedge H)_U.
\quad\square
\]

## C. Infinite-join warning: the Cantor test

Take \(K\) to be Cantor space, and let
\[
L=\{(c,v)\in\mathcal O(K)^2:c\setminus v\text{ is relatively closed discrete in }c\}.
\tag{C1}
\]
The earlier independently reviewed construction shows that L is a frame, \(Z\) is compact and locally compact, sober \(T_1\), and every point sublocale in either sheet is fitted. A subsequent calculation (not part of that earlier blind review) identifies the cross remnant as
\[
P=\bigwedge_{p\in K}O_K(K\setminus\{p\})\ne0,
\tag{C2}
\]
which has no points. In particular, the whole closed sheet F is not fitted.

Let \([p_F]\) denote the closed-sheet point at \(p\). Since it is fitted, \(\operatorname{Sat}([p_F])=[p_F]\). Because K is spatial, \(\bigvee_{p\in K}[p_F]=F\). If Claim 4 holds, it gives
\[
\boxed{
\operatorname{Sat}\Bigl(\bigvee_{p\in K}[p_F]\Bigr)
=F\vee P_U
\ne F
=\bigvee_{p\in K}\operatorname{Sat}([p_F]).}
\tag{C3}
\]
This is offered as an additional test. In particular **Claim 3 is only finite**, and its proof must not be extrapolated to arbitrary joins.

## D. Control cases and questions for the referee

1. If \(L=\mathcal O(K)^2\), then \(P=0\), and Claim 4 predicts saturation=fitting=identity on a disjoint sum of zero-dimensional locales.
2. If \(L=\{(c,v):c\le v\}\), then \(P=K\), and Claim 4 predicts that the upper sheet acquires precisely the copy of the source's first-sheet part.
3. For the Cantor example in §C, \(P\) is nonzero but pointless. Can any unnoticed point-set reasoning invalidate Claims 1–4?
4. Does the main result survive noncompact zero-dimensional K? Are any assumptions omitted about source sublocales, categorical images, or the diagonal \(\Delta(P)\)?
5. Is any claimed finite distributivity being misused in an infinitary context?

Please give a correctness verdict separately for (B2), (B4), (B7), (B8), and (C3); if one fails, locate the first invalid inference. Presentation and simplification comments are welcome.

**References for standard background, not required to read the proof:**

- J. Picado, A. Pultr, A. Tozzi, *Joins of Closed Sublocales*, §1.7, https://www.mat.uc.pt/preprints/ps/p1639.pdf (regular implies fit; sublocale coframe facts).
- R. N. Ball, J. Picado, A. Pultr, *When Are Sublocales Joins of Closed Sublocales?*, https://ems.press/content/serial-article-files/44773?nt=1 (fit iff every sublocale is a meet of opens).
