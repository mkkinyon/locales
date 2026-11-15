# Project A — zero-dimensional two-sheet interfaces and one-step specialization fitting

**15 November 2026. Post-referee canonical consolidation.** The full cross-sheet computation, arbitrary-source one-step theorem, finite-join propagation, and Cantor infinitary obstruction **passed an independent blind external audit with no mathematical repairs**. The additional realization, fitted-classification, join-continuity, and ordinary-point corollaries in §§8–11 were developed **after** that audit and have been checked internally only. [Audit reconciliation](ProjectA_OPEN_CLOSED_TWO_SHEET_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md). No literature-priority claim is made.

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
\(P\) may be nonzero and pointless. In (5), \(\Delta_K(P)\) means the image of the composite \(P\hookrightarrow K\xrightarrow{\Delta_K}K\times K\), **not** the diagonal of the set of ordinary points of \(P\). For a sublocale \(H\hookrightarrow K\), write \(H_F\hookrightarrow F\hookrightarrow Z\) and \(H_U\hookrightarrow U\hookrightarrow Z\). The notation \((P\wedge H)_U\) means the corresponding sublocale of the open sheet.

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

**Proof.** Reflexivity supplies \(H_F\le\operatorname{Sat}(H_F)\). More precisely, restricting the cross block \(\Delta_K(P)\) of Lemma 1 to \(H_F\times U\) produces \(\Delta_K(P\wedge H)\), whose second-projection image is exactly \((P\wedge H)_U\). Thus
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
and is pointless. The remnant is nonzero because every punctured open \(K\setminus\{p\}\) is dense and contains the nonzero Booleanization sublocale \(B_K\): if \(j\) is a dense nucleus, then \(j(a)\wedge a^*=0\) forces \(j(a)\le a^{**}\), whence \(B_K\le O_K(K\setminus\{p\})\). Its being pointless follows because no ordinary point lies in all punctured opens. Every closed first-sheet point \([p_F]\) is fitted (the externally audited point-fittedness result), so \(\operatorname{Sat}([p_F])=[p_F]\). But \(K\) is spatial, hence \(\bigvee_{p\in K}[p_F]=F\), and (11) gives \(\operatorname{Sat}(F)=F\vee P_U>F\). Thus
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

**Audit status:** Equations (5), (7), (10), (11), and (13) have passed a genuinely blind independent review, **without mathematical repairs**. The reviewer also checked the arbitrary-locale generalized points, source generality, and the Cantor remnant. The structural corollaries in §§8–11, based on a later referee follow-up, are **internally checked only**; see the [reconciliation](ProjectA_OPEN_CLOSED_TWO_SHEET_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md) for the precise boundary.

**Sources:**

- J. Picado, A. Pultr, A. Tozzi, *Joins of Closed Sublocales*, §1.7 (regular \(\Rightarrow\) fit): https://www.mat.uc.pt/preprints/ps/p1639.pdf
- R. N. Ball, J. Picado, A. Pultr, *When Are Sublocales Joins of Closed Sublocales?*, introductory characterizations of fitness: https://ems.press/content/serial-article-files/44773?nt=1
- Existing repository: `ProjectA_LCPT_OPEN_CLOSED_INTERFACE_2026-11-15.md`, `ProjectA_LCPT_CROSS_SHEET_PERFECT_KERNEL_POSTAUDIT_2026-11-15.md`, `ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md`.

**Research positioning:** The general interface calculation is complete enough for this stage. After consolidation, compare *only* second-countable (LC-PT) and the graph/homotopy connection as next projects, per the agreed agenda.

## 8. Coordinates and a complete description of fitted sublocales (post-referee)

The complementary open and closed sublocales (F,U) give an isomorphism of **complete lattices**
\[
\mathcal S(Z)\xrightarrow{\cong}\mathcal S(K)\times\mathcal S(K),
\qquad G\longmapsto(G\wedge F,G\wedge U).
\tag{14}
\]
Its inverse sends ((H,C)) to (H_F\vee C_U). Indeed, (F\vee U=Z), (F\wedge U=0), and the sublocale lattice is distributive; hence (G=(G\wedge F)\vee(G\wedge U)). The restrictions identify the intervals below (F,U) with (mathcal S(K)). In particular, joins and meets in these coordinates are coordinatewise (although **infinite distributivity of finite meets over arbitrary joins is not valid**).

The audited one-step theorem (11) is therefore exactly
\[
\boxed{\operatorname{Sat}_{\mathcal A}(H,C)
=\operatorname{fit}_Z(H,C)=(H,C\vee(P\wedge H)).}
\tag{15}
\]

**Corollary 4 (fitted sublocales).** A sublocale (G=H_F\vee C_U) is fitted in (Z) if and only if
\[
\boxed{P\wedge H\le C.}\tag{16}
\]
Thus (H_F) is fitted precisely when (P\wedge H=0). This is an equality **of sublocales**, not a statement about ordinary points.

## 9. Exact obstruction to preserving arbitrary joins (post-referee)

**Corollary 5.** Under the hypotheses of §2, (operatorname{Sat}_{\mathcal A,Z}) preserves arbitrary joins if and only if
\[
\boxed{P\wedge\bigvee_iH_i=\bigvee_i(P\wedge H_i)
\qquad\text{for all families }(H_i)\subseteq\mathcal S(K).}
\tag{17}
\]

**Proof.** Apply (15) to (\bigvee_i(H_i,C_i)) and to the separate summands, using the complete-lattice product (14). Equation (17) gives equality of upper coordinates and hence suffices. For necessity set every (C_i=0); the remaining upper coordinates are exactly the two sides of (17). \(\square\)

If (P) is **complemented** in (mathcal S(K)), (17) holds: a complemented element of a complete distributive lattice determines a direct-product decomposition, and meeting with it preserves all joins. Conversely, if (K) is **spatial** and (P\ne0) is **pointless**, (17) fails. Indeed,
\[
K=\bigvee_{p\in\operatorname{pt}(K)}[p],\quad
P\wedge[p]=0\ (\forall p),
\]
so the left side of (17) is (P) and the right side is zero. This generalizes the Cantor failure in §6: **every nonzero pointless interface over a spatial base obstructs arbitrary-join preservation**.

## 10. Realization and maximality of prescribed interfaces (post-referee)

Let (P\hookrightarrow K) be an arbitrary **fitted** sublocale, with inclusion (i) and quotient frame homomorphism (i^*:\mathcal O(K)\to\mathcal O(P)). Define
\[
\boxed{L_P=\{(c,v)\in\mathcal O(K)^2:i^*(c)\le i^*(v)\}.}
\tag{18}
\]

**Theorem 6 (realization and largest gluing).** If (K) is zero-dimensional, then (L_P) is an admissible two-sheet subframe, its interface is exactly (P), and every other admissible two-sheet frame (L) with interface (P) satisfies (L\subseteq L_P). Hence the possible interfaces are **exactly the fitted sublocales of (K)**, and each has a canonical largest admissible gluing.

**Proof.** The defining inequality is stable under coordinatewise arbitrary joins and finite meets since (i^*) is a frame homomorphism. Every ((c,c)) and (e=(0,1)) lies in (L_P). Moreover,
\[
(1,v)\in L_P\iff i^*(v)=1\iff P\le O_K(v).
\]
Thus the interface calculated from (4) is (igwedge_{P\le O(v)}O(v)=\operatorname{fit}_K(P)=P).

For maximality, let ((c,v)\in L) and let (d\le c) be complemented. The globalizing identity (6) gives ((1,v\vee d^c)\in L), so (P\le O_K(v\vee d^c)); equivalently (i^*(v)\vee i^*(d^c)=1). Since (i^*(d)) and (i^*(d^c)) are complementary, (i^*(d)\le i^*(v)). Joining over all complemented (d\le c) gives (i^*(c)\le i^*(v)). Therefore ((c,v)\in L_P). \(\square\)

For clarity about the exact extent of this classification, write (P_L) for the interface of (L). The preceding argument yields an **order-reversing Galois correspondence**
\[
\boxed{L\subseteq L_P\iff P\le P_L.}\tag{19}
\]
Here (L) ranges over admissible subframes, ordered by inclusion, and (P) over fitted sublocales, also ordered by inclusion. The implication from right to left uses (L\subseteq L_{P_L}\subseteq L_P); the converse follows by examining the pairs ((1,v)). In particular,
\[
P_{L_P}=P,\qquad L\subseteq L_{P_L},
\]
and (L\mapsto L_{P_L}) is an extensive idempotent enlargement. The full gluing frame need not be determined by its interface; its **saturation and fitting operators are**, under the canonical identification (14).

The endpoint checks are (L_0=\mathcal O(K)^2) and (L_K=\{(c,v):c\le v\}). No assertion is made here about smallest admissible presentations of a prescribed nontrivial (P).

## 11. Ordinary specialization, (T_1), and point-fittedness (post-referee)

Assume that (K) is **spatial** and zero-dimensional. For any admissible (L), the two coordinate-evaluation families separate the elements of (L), so (Z) is spatial and its point space is sober. Each point sends (e) to (0) or (1) and hence belongs to exactly one of the two sheets; there are no extra points.

The within-sheet specialization relations are equality; there is no (U\to F) specialization; and the cross-sheet block (5) gives
\[
p_F\preceq q_U\iff p=q\text{ and }p\text{ factors through }P.
\tag{20}
\]
The coordinate criterion (16) also says that the ordinary point sublocale ([p_F]) is fitted exactly when (p) does **not** factor through (P), whereas every upper-sheet point is fitted. Consequently,
\[
\boxed{Z\text{ is }T_1\iff\text{every ordinary point sublocale is fitted}
\iff\operatorname{pt}(P)=\varnothing.}
\tag{21}
\]
In this family, localic specialization is nontrivial but invisible to the ordinary specialization graph **exactly when** (P\ne0) is pointless.

If (K) is compact, (Z) is compact for every admissible (L): a cover of ((1,1)) covers each compact coordinate, and finitely many cover each coordinate. **Local compactness is not automatic.** In particular, the maximal construction for the Booleanization (P=B_K) of Cantor space is the already studied [Boolean lax double](ProjectA_LCPT_BOOLEAN_LAX_DOUBLE_NONLC_CONTROL_2026-11-15.md), whose failure of continuity is proved internally there, including a broader pointless-quotient version. That note is **not independently blind-refereed** and should not be confused with the independently audited *locally compact* discrete-defect gluing.

## 12. Status, provenance, and boundary of this consolidation

**Independently blind-refereed, positive:** equations (5), (7), (10), (11), and the Cantor arbitrary-join counterexample (13), including the generalized-point proof and the zero-dimensionality/fitness hypotheses. See the [external-versus-internal reconciliation](ProjectA_OPEN_CLOSED_TWO_SHEET_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md) and [original blind report](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Referee_report_original.md). The original internal audit and blind prompt/packet remain separate, unmodified historical records.

**Post-referee and separately checked internally, not part of that blind verdict:** equations (14)–(21), the fitted classification, arbitrary-join criterion, realization/maximality, Galois correspondence, and (T_1) equivalences. The referee proposed the first four structural directions in a subsequent [follow-up](project-a/audits/2026-11-15/OPEN_CLOSED_TWO_SHEET/Referee_followup_original.txt); the Galois formulation and the spatial-point obstruction are subsequent internal deductions. All are recorded with proofs above, not silently attributed to the blind audit.

**Deferred:** minimal gluing frames, systematic compactness/coherence/local-compactness-preserving realizations, and further join-continuity classification. At this stopping point, the agreed next decision concerns **only** second-countable (LC-PT) versus the graph/homotopy connection. No literature novelty or priority assertion is made.
