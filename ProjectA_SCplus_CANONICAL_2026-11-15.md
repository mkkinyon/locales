# Project A — The stably locally compact specialization-meet theorem (SC+)

**Canonical post-referee statement and proof, 15 November 2026.** Classical locale theory, with ordinary spatial/patch representation and choice where required. This note incorporates the corrections of the independent blind referee; it supersedes the proof presentation in the [blind packet](ProjectA_SCplus_EXTERNAL_BLIND_PACKET_2026-11-15.md), which remains an immutable audit snapshot. The [referee reconciliation](ProjectA_SCplus_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md) records what changed. No novelty or priority claim is made.

## 1. Definitions and order convention

Let \(X\) be a locale, \(Y=X\times X\) its **localic** square, \(L=\mathcal O(X)\), and \(a_i=\pi_i^*a\). We write \(a\boxtimes b=a_1\wedge b_2\). Denote the diagonal sublocale by \(\Delta\), and put
\[
\mathcal I=\operatorname{cl}_Y(\Delta),\qquad
\mathcal D=\operatorname{fit}_Y(\Delta),\qquad
\mathcal M=\mathcal I\wedge\mathcal D.
\]
Let \(\mathcal A\) be the largest sublocale of \(Y\) on which \(a_1\le a_2\) for every \(a\in L\); define
\[
\mathcal S=\mathcal A\vee\mathcal A^\smile.
\]
For spatial \(X\), the specialization order is \(x\le y\) iff \(x\in\overline{\{y\}}\), so ordinary opens are **upper**. The points of \(\mathcal A\) are precisely \((x,y)\) with \(x\le y\). We use \([B]\) for the **sublocale induced** by a subspace \(B\) of a sober space; it is the least sublocale containing the points \(B\). Do **not** infer \(\operatorname{pt}[B]=B\) for an arbitrary subset \(B\).

**All-locale comparison.**
\[
\boxed{\Delta\le\mathcal S\le\mathcal M.}\tag{1.1}
\]
Indeed, on \(\mathcal A\) we have \(a_1\le a_2\), hence \(a_1\wedge b_2=0\) whenever \(a\wedge b=0\); thus \(\mathcal A\le\mathcal I\). To prove \(\mathcal A\le\mathcal D\), check **all** diagonal-neighborhood opens, not just square covers. If \(w=\bigvee_i(a_i\boxtimes b_i)\in\mathcal O(Y)\) with \(\delta^*w=\bigvee_i(a_i\wedge b_i)=1\), the family \(c_i=a_i\wedge b_i\) covers \(X\), and
\[
w_{\mathscr C}=\bigvee_i(c_i\boxtimes c_i)\le w.
\]
On \(\mathcal A\), \(w_{\mathscr C}\) restricts to top because \(c_1\le c_2\) there, so \(w\) also restricts to top. Since this works for every such \(w\), \(\mathcal A\le\mathcal D\). The converse relation is symmetric, proving (1.1).

## 2. Saturation and the fitted hull

**Saturation lemma.** Let \(Z\) be a stably locally compact sober space, not necessarily compact. If \(C\subseteq Z\) is specialization-saturated (upper), then \([C]\) is fitted; moreover for every \(B\subseteq Z\),
\[
\boxed{\operatorname{fit}_Z([B])=[\uparrow B].}\tag{2.1}
\]

**Proof.** The quotient nucleus of \([C]\) is
\[
j_C(w)=\operatorname{int}\bigl(w\cup(Z\setminus C)\bigr).
\]
We establish the **pointwise identity**
\[
\boxed{j_C(w)=\bigvee_{C\subseteq u\in\mathcal O(Z)}(u\to w).}\tag{2.2}
\]
The \(\ge\) direction follows because \(Z\setminus u\subseteq Z\setminus C\). Conversely take \(z\in j_C(w)\). Choose an open \(V\ni z\) with \(V\cap C\subseteq w\), and a compact saturated \(K\) with
\(z\in\operatorname{int}K\subseteq K\subseteq V\).
Put \(F=K\setminus w\). The patch of \(Z\) is locally compact Hausdorff; the order graph is patch-closed; compact saturated sets are patch-compact; and patch-open upper sets are exactly the original opens. Thus \(F\) is patch-compact, \(\downarrow F\) patch-closed, and \(u=Z\setminus\downarrow F\) is an original open. Since \(C\) is upper and \(C\cap F=\varnothing\), one has \(C\subseteq u\). Also \(K\cap u\subseteq w\), so
\[
z\in\operatorname{int}K\subseteq(u\to w).
\]
This gives (2.2).

Each \(j_u(w)=u\to w\) is the nucleus of the open sublocale \(O(u)\). Let \(k=\bigvee_{u\supseteq C}j_u\) be the **join in the lattice of nuclei**, not an assumed pointwise join. Every \(j_u\le j_C\), hence \(k\le j_C\); by (2.2), \(k(w)\ge\bigvee_u j_u(w)=j_C(w)\). Therefore \(k=j_C\), and \([C]\) is a meet of open supersublocales, i.e. fitted. Finally, ordinary opens containing \(B\) are exactly those containing \(\uparrow B\); their associated open sublocales have the same meet. This proves (2.1). \(\square\)

**Noncompact patch scope.** The patch facts just used require stable local compactness, not compactness. One way to reduce them to the stably compact case is to adjoin a new specialization bottom \(\bot\) whose only open neighborhood is all of \(Z_\bot\). Then \(Z_\bot\) is stably compact, \(Z\) is an open upper subspace and an open patch subspace, and patch-open upper = original open restricts to \(Z\). In particular, products of stably locally compact spaces remain stably locally compact, with product patch and coordinatewise order. This is the noncompact justification missing from the blind packet. The proof is classical; none of these patch facts is asserted here constructively.

## 3. The two spatial relations and their point formulas

Let \(X\) now be stably locally compact, hence (classically) sober and spatial. Since \(X\) is locally compact, its localic square \(Y\) is the spatial product; it is also stably locally compact. The diagonal sublocale equals the sublocale induced by the diagonal point set. Applying (2.1) in \(Y\) yields
\[
\boxed{\mathcal D=[\uparrow_Y\Delta].}\tag{3.1}
\]
The order of \(Y\) is coordinatewise, hence
\[
(x,y)\in\operatorname{pt}(\mathcal D)
\quad\Longleftrightarrow\quad \exists r\ (r\le x\text{ and }r\le y).
\tag{3.2}
\]

Since \(\mathcal I=\operatorname{cl}_Y\Delta\) is a **closed** sublocale of \(Y\), \(\mathcal M=\mathcal I\wedge\mathcal D\) is a **closed sublocale of the spatial locale \(\mathcal D\)**. Consequently \(\mathcal M\) is spatial, and its points are exactly the points of \(\mathcal I\) lying in \(\mathcal D\). This shorter argument avoids a second use of (2.1) and avoids needing the claim that arbitrary closed subspaces remain stably locally compact. The additional exact all-locale identity
\[
\operatorname{fit}_{\mathcal I}(\Delta)=\mathcal I\wedge\operatorname{fit}_Y(\Delta)=\mathcal M
\tag{3.3}
\]
remains useful but is not needed for the main proof.

**Inseparability witness lemma.** In a stably locally compact sober space, points \(x,y\) cannot be separated by disjoint opens iff \(\uparrow x\cap\uparrow y\ne\varnothing\).

**Proof.** A common upper bound belongs to every neighborhood of both points, so one implication is immediate. Conversely, suppose \(x,y\) inseparable. Take compact saturated neighborhoods \(K\) of \(x\) and \(H\) of \(y\), with \(x\in\operatorname{int}K\), \(y\in\operatorname{int}H\). Inseparability makes every \(K\cap H\) nonempty. Coherence makes finite intersections of such compact saturated neighborhoods compact saturated, and they are patch-compact/patch-closed. Fix one intersection \(K_0\cap H_0\); the other intersections cut out a family of patch-closed subsets with the finite-intersection property inside this compact ambient set. Therefore the total intersection is nonempty. Compact saturated neighborhoods of a point intersect to its upward closure; hence the intersection is \(\uparrow x\cap\uparrow y\). \(\square\)

Because \(\mathcal I\) is the closed sublocale induced by the set of inseparable pairs, its point formula is
\[
(x,y)\in\operatorname{pt}(\mathcal I)
\quad\Longleftrightarrow\quad\exists s\ (x\le s\text{ and }y\le s).
\tag{3.4}
\]
Combining (3.2) and (3.4) with spatiality of \(\mathcal M\), put
\[
P_X=\{(x,y):\exists r,s\in X,\ r\le x,y\le s\}.
\]
Then the **localic** equality is
\[
\boxed{\mathcal M=[P_X],\qquad \operatorname{pt}(\mathcal M)=P_X.}\tag{3.5}
\]
The equality of point sets here is established through the closed-in-\(\mathcal D\) argument, **not** a general principle that \(\operatorname{pt}[B]=B\).

## 4. SC+ and the unrestricted necessary condition

**Theorem (SC+, independently blind-refereed).** For every stably locally compact locale \(X\), whether compact or not,
\[
\boxed{\mathcal S(X)=\mathcal M(X)
\quad\Longleftrightarrow\quad
\text{every specialization-order interval }[r,s]
\text{ is a chain}.}\tag{4.1}
\]

**Proof of sufficiency.** Suppose each interval is a chain. Every pair in \(P_X\) lies in some common interval \([r,s]\), so is comparable. A comparable pair is a point of \(\mathcal A\) or \(\mathcal A^\smile\), hence of \(\mathcal S\). Since \(\mathcal M=[P_X]\) is the *least* sublocale containing all those points, \(\mathcal M\le\mathcal S\). Reverse inclusion is (1.1). This proof does **not** require \(\mathcal S\) to be spatial. \(\square\)

**Unrestricted necessity.** For **any** locale \(X\), if \(\mathcal S=\mathcal M\) then every interval among points is a chain. Indeed, if \(r\le x,y\le s\), then \((x,y)\) lies in \(\mathcal I\), as \(s\) witnesses inseparability, and in \(\mathcal D\), since every open neighborhood of the diagonal contains \((r,r)\) and (being upward in the spatial specialization order) contains \((x,y)\). Thus \((x,y)\in\operatorname{pt}(\mathcal M)\). Points of the binary join \(\mathcal A\vee\mathcal A^\smile\) are points of one of its two factors (point sublocales are join-prime for finite joins), hence are comparable. Equality forces \(x,y\) comparable. \(\square\)

## 5. Controls, sharpness and corollary

| Space | Interval chains? | \(\mathcal I\) points | \(\mathcal D\) points | Conclusion |
|---|---|---|---|---|
| Four-element diamond \(r<x,y<s\) | No | All pairs | All pairs | \(\mathcal S\ne\mathcal M\) |
| Finite wedge \(x,y<s\) | Yes | All pairs | Comparable pairs | \(\mathcal S=\mathcal M=\mathcal D\) |
| Finite vee \(r<x,y\) | Yes | Comparable pairs | All pairs | \(\mathcal S=\mathcal M=\mathcal I\) |
| \(\operatorname{Spec}\mathbb Z\) | Yes | All pairs | Comparable pairs | Equality; \(\mathcal M\ne\mathcal I\) |
| Two-arm tent \([-1,1]\), order toward apex \(0\) | Yes | All pairs | Same-arm pairs | Equality, \(\mathcal I=Y\), \(\mathcal M=\mathcal D\) |
| Open tent \((-1,1)\), same order | Yes | All pairs | Same-arm pairs | Noncompact equality, genuinely using (2.1) |

The tent topology is the **upper topology** of the Euclidean compact (respectively locally compact) two-arm ordered patch. The comparability set is \(R=\{(s,t):st\ge0\}\). The original noncompact escaping-witness sequence control from the blind packet is valid, but since there \(\mathcal M=\mathcal I\) it does not actually test the saturation lemma; the tents do.

**Sharp boundary (referee's \(X_1\) control).** Let \(X_1=\{\bot,a,p\}\cup\{g_n:n\in\mathbb N\}\). An open is either all of \(X_1\), or a set missing \(\bot\) such that \(a\in U\) forces every \(g_n\in U\), and \(p\in U\) forces all but finitely many \(g_n\in U\). This space is compact, locally compact, sober but **not coherent**: \(\uparrow a\) and \(\{p\}\cup\{g_n:n>0\}\) are compact saturated, with noncompact intersection. Every interval is a chain (strict comparisons are \(\bot< a<g_n\) and \(\bot<p\)), yet \(a,p\) are inseparable and have common lower bound \(\bot\), while incomparable. Consequently \((a,p)\in\operatorname{pt}\mathcal M\setminus\operatorname{pt}\mathcal S\). **SC+ fails without stability, even for compact locally compact sober spaces.**

The referee also supplied a locally compact sober noncoherent sequence-tree space \(T\) in which a saturated set \(C\) induces a **nonfitted** \([C]\). Its details and an unreviewed exact general criterion appear in the reconciliation and original referee report; neither is elevated here into a separately audited project theorem.

**Corollary.** In a stably locally compact locale,
\[
\boxed{\mathcal D=\Delta\quad\Longleftrightarrow\quad X\text{ is }T_1
\quad\Longleftrightarrow\quad X\text{ is Hausdorff}.}\tag{5.1}
\]
Indeed, (3.2) says \(\mathcal D=\Delta\) forces specialization equality, i.e. \(T_1\). Conversely, in the \(T_1\) case the patch order is equality, so the original topology equals the locally compact Hausdorff patch topology. A Hausdorff space also has equality specialization, and (3.1) gives \(\mathcal D=[\Delta]=\Delta\).

## 6. Audit status and next question

The internal adversarial review and the independent **blind** external referee accepted the SC+ theorem, saturation lemma, and inseparability lemma, subject to the presentation corrections incorporated above. The external referee did not see the internal audit. No computational or constructive verification is claimed, and the literature-priority review remains open.

**Next frontier (A-SC), deliberately not worked on in this segment:** for stably locally compact \(X\), with \(G_\le=\{(x,y):x\le y\}\), determine whether
\[
\boxed{\mathcal A(X)\stackrel{?}{=}[G_\le].}
\]
Unlike \(\uparrow\Delta\), the oriented order graph is generally **not saturated** in the coordinatewise order on \(X^2\); (2.1) does not directly decide its spatiality. Do not infer \(\mathcal S\) spatial merely from the theorem's proof that \(\mathcal M\) is spatial.

## References / provenance

- [Original blind packet](ProjectA_SCplus_EXTERNAL_BLIND_PACKET_2026-11-15.md), [referee reconciliation](ProjectA_SCplus_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md), [audit archive](project-a/audits/2026-11-15/SCplus/README.md).
- [Cameron–Kumar project revisit and finite criterion](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md).
- Bice–Starling, *Hausdorff tight groupoids generalised*, Proposition 2.32 (patch compactness); Escardó, *The regular-locally-compact coreflection of a stably locally compact locale* (patch locales); see the original report for exact links and bibliographical caveats.
- Compare Arrieta–Picado–Pultr on the fitted diagonal and Arrieta's follow-up on separation; a proper novelty comparison for (2.1) should include Jakl, Jakl–Suarez and Moshier–Pultr–Suarez.
