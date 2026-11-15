# Project A — zero-dimensional two-sheet interfaces and one-step specialization fitting

**15 November 2026. Consolidated internal theorem draft.** The foundational Cantor discrete-defect gluing and its negative (LC-PT) conclusion were independently blind-refereed. The full cross-sheet computation in the follow-up addendum and the general theorem in this document **have not** been independently refereed. No literature-priority claim is made.

## 1. Conventions

For a locale \(X\), write \(\mathcal A(X)\hookrightarrow X\times X\) for the canonical **oriented** localic specialization relation. A generalized point \((f,g):E\to X^2\) factors through \(\mathcal A(X)\) exactly when \(f^*(a)\le g^*(a)\) for every \(a\in\mathcal O(X)\). Define

\[
\operatorname{Sat}_{\mathcal A,X}(S)
=\operatorname{im}\bigl(\mathcal A(X)\wedge(S\times X)\xrightarrow{\pi_2}X\bigr).
\tag{1}
\]

The fitting \(\operatorname{fit}_X(S)\) is the meet of all open sublocales containing \(S\). Universally,
\[
S\le\operatorname{Sat}_{\mathcal A,X}(S)\le\operatorname{fit}_X(S).
\tag{2}
\]
Both operators are monotone. We use joins and meets in the **coframe of sublocales**, not set-theoretic unions and intersections of points.

## 2. Hypotheses of the interface theorem

Let \(K\) be a **zero-dimensional locale** (compactness is not required). Let \(Z\) be an open/closed two-sheet locale with a subframe presentation
\[
L=\mathcal O(Z)\subseteq\mathcal O(K)\times\mathcal O(K)
\tag{3}
\]
whose arbitrary joins and finite meets are coordinatewise. Require:

1. \(e=(0,1)\in L\), so \(U=O_Z(e)\cong K\) is the open second sheet and \(F=C_Z(e)\cong K\) is the closed first sheet.
2. \((d,d)\in L\) for every complemented (clopen) \(d\in\mathcal O(K)\).

Because the clopens generate \(\mathcal O(K)\) and \(L\) is closed under arbitrary joins, \((c,c)\in L\) for **every** open \(c\in\mathcal O(K)\). The two coordinate restrictions are therefore onto the open frames of the sheets.

Define the **global-open remnant** in the common sheet \(K\) by
\[
P=\bigwedge_{(1,v)\in L}O_K(v).
\tag{4}
\]
\(P\) may be nonzero and pointless. For a sublocale \(H\hookrightarrow K\), write \(H_F\hookrightarrow F\hookrightarrow Z\) and \(H_U\hookrightarrow U\hookrightarrow Z\). The notation \((P\wedge H)_U\) means the corresponding sublocale of the open sheet.

## 3. Exact cross-sheet specialization

**Lemma 1.** As a sublocale of \(F\times U\cong K\times K\),
\[
\boxed{\mathcal A(Z)\wedge(F\times U)=\Delta_K(P).}
\tag{5}
\]
The other three blocks are \(\Delta_F\), \(\Delta_U\), and \(0\) on \(U\times F\), respectively.

**Proof.** Let \((f,g):E\to F\times U\) be a generalized comparable pair. Write \(f_0,g_0:E\to K\) for its coordinates. Every diagonal open \((d,d)\) with \(d\) clopen gives \(f_0^*d\le g_0^*d\). Applying the same inequality to the clopen complement \(d^c\) reverses the inequality, so \(f_0^*d=g_0^*d\). Clopens generate the frame; hence \(f_0=g_0=h\). For every \((1,v)\in L\), comparability gives \(1\le h^*v\), so \(h\) factors through \(P\).

Conversely suppose \(h:E\to P\). Fix any \((c,v)\in L\) and clopen \(d\le c\). Closure of \(L\) under finite meets and joins yields the **globalized open**
\[
(c,v)\wedge(d,d)\vee(d^c,d^c)=(1,v\vee d^c)\in L.
\tag{6}
\]
Since \(h\) factors through \(P\), \(h^*(v\vee d^c)=1\). As \(h^*d\) is complemented, \(h^*d\le h^*v\). Taking the **frame join** over the clopens \(d\le c\) gives \(h^*c\le h^*v\). Thus the two sheet-copies of \(h\) form a comparable pair. This uses generalized points over arbitrary \(E\), and proves the equality of sublocales. On each same-sheet block, the two coordinate maps agree because \(K\) is zero-dimensional; the \(U\to F\) block vanishes by applying the inequality to \(e=(0,1)\). \(\square\)

**Audit-sensitive detail:** Equation (6) only requires the assumed subframe structure; it does not require the filter-valued interface to be principal. The infinite join at the end is taken in \(\mathcal O(E)\), so no invalid distributivity of an arbitrary sublocale meet over an infinite sublocale join is used.

## 4. Arbitrary first-sheet sources

**Lemma 2.** For **every** sublocale \(H\hookrightarrow K\) (closed or not, compact or not),
\[
\boxed{
\operatorname{Sat}_{\mathcal A,Z}(H_F)
=\operatorname{fit}_Z(H_F)
=H_F\vee(P\wedge H)_U.}
\tag{7}
\]

**Proof.** Reflexivity supplies \(H_F\le\operatorname{Sat}(H_F)\). Lemma 1, restricted to \(H_F\times U\), supplies the image \((P\wedge H)_U\). Thus
\[
H_F\vee(P\wedge H)_U
\le\operatorname{Sat}(H_F)
\le\operatorname{fit}(H_F).
\tag{8}
\]

Let \(T=\operatorname{fit}_Z(H_F)\). Its trace on \(U\) lies in \(P\): all global opens \((1,v)\) contain \(H_F\). Its trace on \(U\) also lies in \(H\): for each \(c\) with \(H\le O_K(c)\), the diagonal open \((c,c)\) contains \(H_F\). Because zero-dimensional locales are regular and therefore fit, \(H\) is the meet of these opens in the sublocale lattice of \(K\). The analogous argument on \(F\) gives \(T\wedge F=H_F\). Since \(F\vee U=Z\) and the sublocale lattice is distributive,
\[
T=(T\wedge F)\vee(T\wedge U)\le H_F\vee(P\wedge H)_U.
\tag{9}
\]
Combine with (8). \(\square\)

## 5. Every sublocale is fitted in one specialization step

**Lemma 3 (finite-join propagation).** If \(\operatorname{Sat}(S)=\operatorname{fit}(S)\) and \(\operatorname{Sat}(T)=\operatorname{fit}(T)\), then the same holds for \(S\vee T\). Indeed, fitted sublocales are closed under finite joins (by the coframe distributivity law); consequently
\[
\operatorname{fit}(S\vee T)
=\operatorname{fit}(S)\vee\operatorname{fit}(T)
\le\operatorname{Sat}(S\vee T)
\le\operatorname{fit}(S\vee T).
\tag{10}
\]
The first inequality uses **only monotonicity** of saturation, not any claimed join-preservation property.

**Theorem (zero-dimensional two-sheet one-step theorem).** Under §2 hypotheses, for an **arbitrary** sublocale \(G\hookrightarrow Z\), writing \(H_F=G\wedge F\),
\[
\boxed{
\operatorname{Sat}_{\mathcal A,Z}(G)
=\operatorname{fit}_Z(G)
=G\vee(P\wedge H)_U.
}
\tag{11}
\]
In particular, \(\operatorname{Sat}_{\mathcal A,Z}^2=\operatorname{Sat}_{\mathcal A,Z}\) on the entire sublocale lattice.

**Proof.** The complementary open/closed sublocales satisfy \(F\vee U=Z\), so the coframe identity gives
\[
G=(G\wedge F)\vee(G\wedge U)=H_F\vee C_U.
\tag{12}
\]
Zero-dimensionality makes \(U\) fit: **every** sublocale \(C\hookrightarrow U\) is fitted in \(U\). Since \(U\) is open in \(Z\), every relatively open sublocale of \(U\) is open in \(Z\), so \(C_U\) is fitted in \(Z\). By (2), \(\operatorname{Sat}(C_U)=C_U\). Apply Lemmas 2 and 3 to (12):
\[
\operatorname{Sat}(G)=\operatorname{fit}(G)
=\operatorname{fit}(H_F)\vee C_U
=G\vee(P\wedge H)_U.
\]
Fitting is idempotent, giving the final assertion. \(\square\)

**Corollary (closed-source formula).** If \(G\) is closed, (11) applies with no compactness assumption. Such \(G\) is fitted exactly when \((P\wedge(G\wedge F))_U\le G\wedge U\). The earlier closed \(B\subseteq K\) formula is a special case.

## 6. An infinitary obstruction: saturation does not preserve arbitrary joins

In the Cantor discrete-defect gluing, the remnant is
\[
P=\bigwedge_{p\in K}O_K(K\setminus\{p\})\ne0
\]
and is pointless. Every closed first-sheet point \([p_F]\) is fitted (the externally audited point-fittedness result), so \(\operatorname{Sat}([p_F])=[p_F]\). But \(K\) is spatial, hence \(\bigvee_{p\in K}[p_F]=F\), and (11) gives \(\operatorname{Sat}(F)=F\vee P_U>F\). Thus
\[
\boxed{
\operatorname{Sat}\left(\bigvee_{p\in K}[p_F]\right)
\ne\bigvee_{p\in K}\operatorname{Sat}([p_F]).}
\tag{13}
\]
The finite-join propagation lemma **must not** be extended to arbitrary joins. The failure is compatible with direct images preserving joins: the source-intersection/pullback stage defining saturation does not preserve this infinite join.

## 7. Sanity checks, scope, and status

- **Disjoint two sheets:** \(L=\mathcal O(K)^2\); then \((1,0)\in L\), so \(P=0\) and every sublocale is already fitted in the disjoint-sum locale.
- **Sierpiński-style double:** \(L=\{(c,v):c\le v\}\); then \(P=K\), and (11) adds the second-sheet copy of the first-sheet part.
- **Cantor discrete-defect gluing:** the intermediate case \(0<P<K\) with nonzero pointless P; the theorem is a genuinely localic calculation and not a pointwise specialization computation.

**Checked internally:** subframe globalization (6), arbitrary test locales in Lemma 1, regular-implies-fit, finite coframe distributivity, relative fitting in an open sheet, and the spatiality argument in (13). **Not checked externally:** the new general formulas (5), (7), (11), (13). All remain subject to independent adversarial review.

**Sources:**

- J. Picado, A. Pultr, A. Tozzi, *Joins of Closed Sublocales*, §1.7 (regular \(\Rightarrow\) fit): https://www.mat.uc.pt/preprints/ps/p1639.pdf
- R. N. Ball, J. Picado, A. Pultr, *When Are Sublocales Joins of Closed Sublocales?*, introductory characterizations of fitness: https://ems.press/content/serial-article-files/44773?nt=1
- Existing repository: `ProjectA_LCPT_OPEN_CLOSED_INTERFACE_2026-11-15.md`, `ProjectA_LCPT_CROSS_SHEET_PERFECT_KERNEL_POSTAUDIT_2026-11-15.md`, `ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md`.

**Research positioning:** This reaches a natural stopping point for the open/closed interface. After external review, compare *only* second-countable (LC-PT) and the graph/homotopy connection as next projects, per the agreed agenda.
