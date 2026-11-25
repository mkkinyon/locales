# From graphs to localic evidence: two studies, five proof-guided examples
## A mathematical account of the Point-Free Topology project · adopted reader-facing synthesis · 21 November 2026

**Internal adversarial audit (21 Nov):** [claim-by-claim source and finite-case audit](ProjectA_ENDGAME_TWO_STUDIES_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) found no fatal mathematical error in the checked interfaces, but required sharpening the provenance and generation proof of (G′), an overloaded symbol, and certain finite/example scopes. Those editorial/proof-interface repairs are integrated below. This is **internal** checking, not a new external or formal proof certificate.

**Audience.** Mathematicians with basic algebra/topology who want to understand what the project actually established, rather than read a chronological research log or a list of 47 theorem groups. This is a **proof-guided synthesis and learning document**, not a finished publication, a new external audit, or a claim of novelty. The three historical A/B/C branches remain in the [authoritative research ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md); **this two-study organization is the adopted *reader-facing* account**. Detailed proofs, assumptions, and evidence statuses stay in their linked canonical sources.

**Starting source:** Peter J. Cameron and Vinod Kumar P. B., [*Graphs on Topological Spaces*](https://arxiv.org/abs/2610.14783) (2026). The five ordinary graph relations in that paper prompted our translation into genuine localic relations; its pointwise graph facts are not claimed as discoveries of this project.

**Central question.** What does an ordinary graph on the points of a locale retain about a genuine sublocale relation? When does the graph suffice to compute a relation or its composition, and when must one remember pointless witnesses, closed supports, or higher simultaneous witnesses?

**Two studies.** I: **genuine binary localic relations**, starting from specialization and its **two diagonal hulls**, then developing three effective calculi (coherent Priestley/patch, Booleanization/closed support, scattered-sector matrices) and sharp failures of naïve pointwise reconstruction; II: **higher simultaneous witnesses**, their Stone-sheaf comparison objects and precise homotopical limitations. They share the coherent patch-language, but II is *not* derived from the binary associative calculi.

**Five anchors** (in their pedagogical order): a five-point fence; two convergent Priestley zigzag rays; a rational bridge étale locale; disjoint rational/irrational middle sets; a pair of six-point order complexes. A small additional example on \(P\times(\omega+1)\) combines the second and third binary calculi. For all exact computations in an example see [five-example cold read](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md).

---

# Study I. Genuine binary localic relations

## 1. From Cameron–Kumar graphs to relations in a localic square

For a locale \(X\), the frame \(\mathcal O(X)\) of opens has arbitrary joins and finite meets distributing over joins; locale maps are dual to frame homomorphisms. A sublocale corresponds to an appropriate quotient of this frame (equivalently, a nucleus). Write \(X^2=X\times_{\mathbf{Loc}}X\) for the **localic product**, not a direct product of frames, and let a **genuine binary relation** be a sublocale \(R\hookrightarrow X^2\). Its point pairs, the point-generated sublocale of those pairs, and \(R\) itself need not be identical. In particular, the join of all points of \(R\) may miss a nonzero pointless sublocale. Neither sublocale joins nor images should be silently replaced by point-set unions or point images.

Write \(\Delta\hookrightarrow X^2\) for the diagonal. Our basic separation and hull relations are
\[
\begin{gathered}
\mathcal I=\operatorname{cl}\Delta,\qquad
\mathcal D=\operatorname{fit}\Delta,\qquad
\mathcal V=\operatorname{fit}(\mathcal I),\qquad
\mathcal W=\operatorname{cl}(\mathcal D),\\
\mathcal M=\mathcal I\wedge\mathcal D,\qquad
\mathcal J=\mathcal I\vee\mathcal D,\qquad
\mathcal T=\mathcal V\wedge\mathcal W,
\end{gathered}
\]
Here \(\operatorname{cl}(R)\) is the least **closed sublocale** containing \(R\), and \(\operatorname{fit}(R)\) the least **fitted sublocale**, namely the intersection of all open sublocales containing \(R\). The Urysohn relation \(\mathcal U\) is the closed complement of \(\bigvee_{a^*\vee b^*=1} a\boxtimes b\) (\(a^*\) denotes pseudocomplement in \(\mathcal O(X)\)); the functional relation \(\mathcal F\) is the kernel-pair relation of all real-valued locale maps, or of the completely regular reflection. The relation \(\mathcal H\) is the **least simultaneously closed and fitted** diagonal super-relation. See the [precise definition and assumption table](ProjectA_ENDGAME_NOTATION_AND_ASSUMPTIONS_2026-11-21.md) for the full cover and frame formulas.

### Specialization: one relation, two diagonal hulls

For **any** locale \(X\), let \(\mathcal A\hookrightarrow X^2\) be its **oriented localic specialization relation**: the largest sublocale on which
\[
(\pi_1^*a)|_{\mathcal A}\le(\pi_2^*a)|_{\mathcal A}
\qquad\text{for every }a\in\mathcal O(X).
\]
Write \(\mathcal A^\smile\) for its converse and set
\[
\boxed{\mathcal S=\mathcal A\vee\mathcal A^\smile.}
\]
Thus \(\mathcal S\) is the **symmetric, reflexive specialization relation**. On points of a coherent spectral locale, \(\mathcal S\) is the comparability relation of the specialization order, but the definition above is **localic** and makes sense without any points. We reserve \(\mathcal B(K)\) below for the *unrelated* Booleanization operation. Our spectral-point convention is \(x\le y\) when every open containing \(x\) also contains \(y\), so **opens are upsets**; this reverses the order convention of some graph papers.

Here is a useful fact **requiring no coherence or spatiality assumption**:
\[
\boxed{\Delta\le\mathcal S\le\mathcal I\wedge\mathcal D,
\qquad
\operatorname{cl}(\mathcal S)=\mathcal I,
\qquad
\operatorname{fit}(\mathcal S)=\mathcal D.}
\]
**Why?** Reflexivity gives \(\Delta\le\mathcal S\). On \(\mathcal A\), the pullbacks \(a_1\le a_2\) for each open \(a\). If \(a\wedge b=0\), then \(a_1\wedge b_2\le a_2\wedge b_2=0\), which places \(\mathcal A\) in the inseparability relation \(\mathcal I=\operatorname{cl}\Delta\). For an open cover \(\mathcal C\), the diagonal-cover open \(\bigvee_{c\in\mathcal C}(c_1\wedge c_2)\) restricts on \(\mathcal A\) to \(\bigvee_{c\in\mathcal C}c_1=1\); hence \(\mathcal A\le\mathcal D=\operatorname{fit}\Delta\). Both arguments work with coordinates reversed, so \(\mathcal A^\smile\le\mathcal I\wedge\mathcal D\) as well. The closure and fitting identities follow by applying these monotone hull operators to \(\Delta\le\mathcal S\le\mathcal I,\mathcal D\), respectively. [All-locale specialization-hull proof](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md).

**Interpretation.** The two lower branches of the separation hierarchy arise by **closing** and by **fitting the same specialization relation**. Neither \(\mathcal I\) nor \(\mathcal D\) is just an unrelated construction from \(\Delta\), and \(\mathcal S\) need not equal their meet. This perspective is already meaningful before any theory of relation composition.

Nor should \(\mathcal A\) be mistaken for the sublocale generated by its ordinary specialization pairs. A [compact, locally compact, sober \(T_1\) example](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md) has *trivial point specialization*, yet \(\mathcal A>\Delta\): even the oriented starting relation can retain **pointless information**. Under stronger stability hypotheses it is spatial, so the distinction is sensitive to the ambient class.

For composable localic relations \(R\le X\times Y\) and \(S\le Y\times Z\), composition means **first \(R\), then \(S\)**:
\[
R\circ S=\operatorname{im}_{\mathbf{Loc}}
\left((\pi_{12})^{-1}R\wedge(\pi_{23})^{-1}S
\;\longrightarrow\; X\times Z\right).
\tag{1}
\]
This is the smallest-sublocale image of the **actual localic composability pullback**, and it is **not globally associative**. The purpose of our positive results is to identify *specified subcalculi* for which actual composition can be computed and associated.

## 2. First calculus: patch-closed order in the coherent case

**The indispensable theorem.** Let the participating locales be coherent and the relations **proconstructible spectral sublocales** of their finite products. Under classical Priestley duality these sublocales correspond to **patch-closed relations** on the spectral point spaces. Their **actual Loc** composability pullback and image coincide with the appropriate patch-closed ordinary relation composite; the class is closed under **finite** joins, converse and composition, and its composition is associative.

**Proof gate, not optional rhetoric.** One must first identify a proconstructible sublocale via a compact-element-preserving quotient of the coherent frame, then verify that the actual pullback and image of restricted spectral maps remain in that class and have the stated point sets. Merely observing that the pointwise composites agree would not prove equality of arbitrary sublocales. Once this bridge is established, the subsequent calculations become honest order theory. [Full coherent proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md), [independent review scope](ProjectA_ENDGAME_STRUCTURAL_EXTERNAL_REFEREE_RECONCILIATION_2026-11-21.md).

This is the **coherent upgrade of the all-locale specialization-hull picture**: whereas the preceding identities \(\operatorname{cl}\mathcal S=\mathcal I\) and \(\operatorname{fit}\mathcal S=\mathcal D\) hold for every locale, the following *finite composition-word* identities use the restricted, genuine proconstructible spectral calculus:
\[
\boxed{\mathcal I=\mathcal A\mathcal A^\smile,\quad
\mathcal D=\mathcal A^\smile\mathcal A,\quad
\mathcal V=\mathcal D^2,\quad
\mathcal W=\mathcal I^2,\quad
\mathcal S^2=\mathcal J.}\tag{2}
\]
Importing the **separate coherent theorem** \(\mathcal W=\mathcal U\), not confusing it with (2) itself, gives
\[
\mathcal U=\mathcal I^2,\qquad
\mathcal S^4=\mathcal U\vee\mathcal V.
\tag{3}
\]
Thus the original undirected specialization graph has an exact localic **square** \(\mathcal S^2=\mathcal I\vee\mathcal D\), and—with the separate \(\mathcal W=\mathcal U\) input—an exact **fourth power** \(\mathcal S^4=\mathcal U\vee\mathcal V\). This recovers a graph-power thread of the Cameron–Kumar motivation *inside* our coherent theory, rather than replacing the more general compact-support and scattered-index calculi of the following sections. [Coherent graph-power discussion](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md).

The normal/conormal dualities of the compact-open lattice sharpen the corresponding equality classes; those directions are part of the hierarchy, not blanket claims of normality for every frame.

### Example 1. The five-point fence makes the hierarchy visible

Let \(P=\{m,a,k,b,n\}\) with strict relations
\[
a<m,\qquad a<k,\qquad b<k,\qquad b<n,
\]
and no further strict comparisons. The comparability graph is the path \(m-a-k-b-n\). The **common-upper** relation \(\mathcal I\) contains \((a,b)\), witnessed by \(k\), but \(\mathcal D\), the **common-lower** relation, does not. Conversely, \((m,k)\in\mathcal D\), witnessed by \(a\), but \((m,k)\notin\mathcal I\).

In this finite coherent/Alexandrov setting, the actual localic composition is computed by (2)–(3). An independent enumeration gives \(|\mathcal I|=15\), \(|\mathcal D|=17\), and \(|\mathcal I^2|=23\). A two-step common-upper path exists between every pair **except** the two ordered pairs with endpoints \(m,n\). Therefore
\[
\boxed{\mathcal U=\mathcal W=P^2\setminus\{(m,n),(n,m)\}.}
\tag{4}
\]
Every continuous real-valued function is constant along each specialization edge, hence along the connected comparability graph, so \(\mathcal F=P^2\). The **separate** finite closed/fitted hull computation in the canonical source gives \(\mathcal H=P^2\) as well; graph connectedness by itself would not justify that genuine sublocale equality without the coherent representation theorem.

**Lesson.** Some distinctions in the hierarchy are entirely readable from a small order. The coherent theorem is what licenses the promotion from those point-order computations to **genuine sublocale relations**. [Finite fence computation](A-W-HmeetU-connected-example-finite-poset-product-2026-11-09.md) and [W-phase referee reconciliation](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md).

### Example 2. Closed-and-fitted does not mean transitive

Form two disjoint alternating Priestley order-zigzag rays \(A=\{a_i:i\ge0\}\), \(B=\{b_i:i\ge0\}\), with exactly \(a_{2n}<a_{2n+1}>a_{2n+2}\) and \(b_{2n}<b_{2n+1}>b_{2n+2}\) as strict comparabilities. Add a single point \(t\), incomparable with either ray, and give \(A\cup B\cup\{t\}\) the patch topology of the one-point compactification of the discrete union: both rays converge to \(t\). Let \(S_A=A\cup\{t\}\) and \(S_B=B\cup\{t\}\). In the associated coherent spectral locale, the **computed least closed-and-fitted diagonal hull** is
\[
\mathcal H=(S_A\times_{\mathrm{Loc}}S_A)\vee(S_B\times_{\mathrm{Loc}}S_B).
\tag{5}
\]
It contains \((a_0,t)\) and \((t,b_0)\), while \((a_0,b_0)\notin\mathcal H\). The triple \((a_0,t,b_0)\) is a genuine composability witness, so
\[
\boxed{\mathcal H\circ\mathcal H\nleq\mathcal H,\qquad
\mathcal U\vee\mathcal V<\mathcal H<\mathcal F.}
\tag{6}
\]
Here the formula (5) is **the result of a closed/fitted localic hull calculation**; its visible pair-graph cannot substitute for that proof. A separate result characterizes coherent transitivity of \(\mathcal H\) by \(\mathcal H=\mathcal F\).

**Lesson.** Closure, fitting, and transitive closure are three genuinely different operations, even in a coherent setting with an excellent point-order dictionary. The related \(\omega+m\) stabilization stages measure **hull iteration**, not graph distance and not the \(\mathcal V\)-tree rank. [Coherent two-ray counterexample](A-H-two-convergent-zigzag-rays-nontransitive-coherent-counterexample-2026-10-24.md).

## 3. Second calculus: pointless Booleanization and compact closed supports

The classical inputs are Isbell's **least dense sublocale** \(\mathcal B(K)\), the weak/full-product distinction of Johnstone–Sun (1988), and the product-spatiality techniques of Isbell/Plewe. Plewe, *Localic Products of Spaces* (1996), **Thm. 3.2, pp.654–655**, already extracts a compact **closed support** of a nonzero pointless product sublocale and shows that its coordinate traces are dense; the Cantor witness comes afterward. The **method** is not newly invented by the project. [Full-text Plewe comparison](ProjectA_PLEWE_1996_FULL_PRIMARY_SOURCE_COMPARISON_2026-11-21.md).

### Example 3. The rational bridge shows how finite covers leave a pointless trace

Take two open real-line sheets \(S,T\), with at each rational \(q\) a bridge point \(b_q\) admitting neighborhoods
\[
N(q,\varepsilon)=\{b_q\}
\cup\{s_x:q-\varepsilon<x<q\}
\cup\{t_x:q<x<q+\varepsilon\}.
\tag{7}
\]
The coordinate map \(p:X\to\mathbb R\) is an **étale local homeomorphism**. The resulting \(X\) is second countable, locally compact, sober and \(T_1\), but not Hausdorff. In the cross-sheet fibre sector
\[
J=S\times_{\mathbb R}T\cong\mathbb R
\]
every *finite* diagonal-cover witness leaves a dense matching locus, hence contains the nonzero pointless Booleanization \(\mathcal B(J)\). The **full** (infinite) open section atlas \(\mathscr A=\{S,T\}\cup\{N_q:q\in\mathbb Q\}\), with \(N_q=\bigcup_{\varepsilon>0}N(q,\varepsilon)\), separates the sector. Thus the finite- and all-cover relations \(\mathcal D_2,\mathcal D\) have the **same ordinary point pairs**, but the sublocale/hull calculation is
\[
\boxed{\mathcal D=\Delta,\qquad
\mathcal W=\mathcal I<\mathcal W_2=\mathcal U=X\times_{\mathbb R}X.}
\tag{8}
\]
This settles the historical Q/Q′ finite-versus-all-cover questions **negatively**. The usual finite union of nowhere-dense boundary sets cannot account for every rational matching point; the actual *pointless* intersection is carried by \(\mathcal B(J)\). [Repaired canonical proof](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) and [Q/Q′ referee reconciliation](ProjectA_Q_DENSE_RATIONAL_BRIDGE_REFEREE_RECONCILIATION_2026-11-14.md).

**Lesson.** The finite-cover relation \(\mathcal D_2\) is obtained by taking the meet of the open diagonal-cover sublocales over **finite** covers; \(\mathcal D\) uses **all** covers. They agree on ordinary pairs in this \(T_1\) example but differ as sublocales. The obstruction is not another long order path; it is the intersection of all cover constraints in the sublocale lattice. The paper of Plewe makes the **older** closed-support technique historically visible, but this specific étale/hull calculation has its own detailed project proof and separate evidence status.

### Compact rectangular composition

Let \(G\) be compact Hausdorff, and \(A,B\subseteq G\) arbitrary ordinary subsets. Define
\[
p(A,B)=[A\times B]_{G^2},\qquad
q(A,B)=[A]_G\times_{\rm Loc}[B]_G.
\]
The \(p\)-rectangle is a **point-generated weak product**, and \(q\) is the **full** localic product. The distinction \(p\le q\), possibly strict, is **classical**. Our separately checked result concerns their **genuine localic composition**:
\[
\boxed{
r(A,B)\circ s(C,D)
=\begin{cases}
q(A,D),&[B]_G\wedge[C]_G\ne0,\\
0,&[B]_G\wedge[C]_G=0,
\end{cases}\quad r,s\in\{p,q\}.
}
\tag{9}
\]
The full outer \(q(A,D)\) can itself be zero if \(A\) or \(D\) is empty. With that qualification, the finite-join \(p/q\) rectangular algebra is associative, converse-closed, and contains zero. Its **multiplicative unit exists inside that finite-join algebra iff \(G\) is finite** (counting the one-element zero algebra when \(G=\varnothing\); otherwise assume \(G\ne\varnothing\)). This theorem **originated in the structural referee's post-verdict addendum** and was then internally checked; it has **now also passed a separate focused independent blind audit** ([final adjudication](ProjectA_FINAL_FOCUSED_CLIQUE_UNITALITY_REFEREE_RECONCILIATION_2026-11-21.md)). It was **not** included in the earlier original rectangular candidate.

**Proof mechanism.** A nonzero sublocale \(W\le [A]\times[D]\) has a least compact closed ambient support \(K\), with both \(A\)- and \(D\)-coordinate traces dense in \(K\). More strongly, the **full-sublocale generation theorem (G′)**, **proposed in a referee's post-verdict mathematical addendum, internally reconciled and now separately independently audited** ([focused report](ProjectA_FINAL_FOCUSED_CLIQUE_UNITALITY_REFEREE_RECONCILIATION_2026-11-21.md)), reconstructs
\[
\boxed{
[A]_G\times_{\rm Loc}[D]_G=
\bigvee_{\substack{\varnothing\ne K\subseteq G^2\text{ closed}\\
K\cap(A\times G),\,K\cap(G\times D)\text{ dense in }K}}
\mathcal B(K).
}
\tag{G′}
\]
**Why the join is the whole product.** Every indicated \(\mathcal B(K)\) lies in the product because the two coordinate-trace sublocales are dense in \(K\), and their meet contains the least dense sublocale. Let \(J\) denote their join. If \(J<[A]\times_{\rm Loc}[D]\), **fitness of the compact Hausdorff ambient locale** supplies an ambient open sublocale \(O\ge J\) that does not contain the full product. Its complementary closed sublocale \(F\) meets that product in some \(0\ne W\). The least closed support \(K'\) of \(W\) is a qualifying compact closed support lying in \(F\), so \(0\ne\mathcal B(K')\le J\wedge F=0\), a contradiction. This proves the **generation direction**; density alone would not suffice. The **mixed RC formula (9)** was subjected to a separate later independent structural review, which must not be conflated with an original blind audit of the referee-origin (G′).

Nonzero middle overlap has a nonempty compact closed support; over that support, the two composability pullbacks are dense, and their meet contains its least dense sublocale. Localic image of that meet saturates each outer \(\mathcal B(K)\), giving the full outer rectangle. This proves (9) without an ordinary middle point. The generating formula (G′) is a **whole-sublocale representation**, not merely the spatiality test from Plewe; *its precise historical priority has not been determined*. [Rectangular canonical proof](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md).

### Example 4. Disjoint rational/irrational middle sets produce a full composite

Let \(G=[0,1]\), \(B=G\cap\mathbb Q\), \(C=G\setminus\mathbb Q\), and \(A=D=G\). The ordinary relational composite of \(G\times B\) and \(C\times G\) is empty: \(B\cap C=\varnothing\). Yet both induced sublocales \([B]_G\) and \([C]_G\) are dense, so
\[
\mathcal B(G)\le[B]_G\wedge[C]_G,\qquad
[B]_G\wedge[C]_G\ne0.
\]
The actual localic formula (9) gives
\[
\boxed{p(G,B)\circ p(C,G)=q(G,G)=G^2.}
\tag{10}
\]
**Lesson.** A genuine composite can be maximal even when there is **not a single ordinary middle witness**. This is a different failure from Example 3: the bridge is about a finite/all-cover *hull*, whereas (10) is about actual **composition**.

The three-factor nonrectangular Stone counterexample in the rectangular canonical note shows why (9) must **not** be extended by arbitrarily decomposing every point-generated graph into infinitely many singleton rectangles. Finite-join composition is generally distributive, because inverse images of sublocales preserve **finite** joins, but unrestricted **infinite** distributivity fails (Plewe, §6, p.665).

## 4. Third calculus: scattered indices preserve all coefficients

Let \(P\) be an **arbitrary locale** and \(K\) a **locally compact scattered Hausdorff space**. The independently blind-audited arbitrary-parameter theorem asserts the **complete-lattice** decomposition
\[
\boxed{\operatorname{Sub}(P\times K)\cong
\prod_{k\in K}\operatorname{Sub}(P).}
\tag{MAT*}
\]
The \(k\)-coordinate is the genuine sublocale restriction to the closed fibre \(P\times\{k\}\); it need not be an open coordinate when \(k\) is a limit point. One **must not** infer a locale isomorphism \(P\times K\cong\coprod_{k\in K}P\).

**Proof mechanism of MAT*.** The localic open-cover localization \(W=\bigvee_\alpha(W\wedge O_\alpha)\) reduces to compact clopen index charts. Compact scattered Hausdorff spaces have a finite last Cantor–Bendixson derivative. Split into finitely many clopen charts each with a unique final-derivative point; split that singleton closed sector off by a **finite** open/closed decomposition, and use transfinite induction on smaller compact clopen pieces in the open complement. A locally compact scattered index is covered by compact clopen sets, so the compact proof localizes. Reconstruction and uniqueness use the complemented **singleton sector**, not arbitrary infinitary distributivity.

For **arbitrary genuine binary localic relations** \(R,S\le(P\times K)^2\), the exact formula is
\[
\boxed{(R\circ S)_{ik}=\bigvee_{j\in K}
(R_{ij}\circ_P S_{jk}).}
\tag{MUL*}
\]
Its proof first forms the **actual triple composability sublocale** and decomposes *that object* into \(i,j,k\)-sectors, then uses the fact that localic **images** preserve joins. This is not an illegitimate distribution of an infinite sublocale meet over joins. The formula is binary and does not yield unrestricted associativity.

If \(\mathcal A(P)\subseteq\operatorname{Sub}(P^2)\) contains \(0,\Delta_P\), is closed under finite joins, converse and genuine composition, and composes **associatively on that coefficient class**, then the **row-and-column-finite** \(K\times K\) \(\mathcal A(P)\)-matrices form an associative, unital, converse-closed algebra of actual localic relations. For any fixed entry, both triple bracketings reduce to the same **finite** double sum. This is **FINMAT***. No separate finite-join-distributivity hypothesis is needed; it holds for all genuine localic relation triples. [Canonical MAT*/MUL*/FINMAT* proof and focused independent referee reconciliation](ProjectA_MATSTAR_MULSTAR_POSTREFEREE_CANONICAL_2026-11-21.md).

### Combining the first two calculi with the third

There are two useful formal corollaries of the previously audited inputs. Use as \(\mathcal A(P)\):
1. for coherent \(P\), **proconstructible spectral relations**, giving associative localic matrices on possibly noncoherent/noncompact \(P\times K\);
2. for compact Hausdorff \(P\), the unitalized finite rectangular algebra
\[
\mathscr R_\vee^\sharp(P)=
\{R,\ R\vee\Delta_P:\ R\in\mathscr R_\vee(P)\},
\]
which is associative by finite distributivity and the strict identity property of \(\Delta_P\).

These coefficient choices and the following sector example are **new internal combinations** (not separate original blind packets); neither permits arbitrary TWIST adjunction or arbitrary infinite support.

### A nonisolated closed sector containing a pointless composability witness

Put \(P=[0,1]\), \(K=\omega+1\), \(B=P\cap\mathbb Q\), \(C=P\setminus\mathbb Q\). Set
\[
R_{\omega,\omega}=p(P,B),\qquad
S_{\omega,\omega}=p(C,P),
\]
with every other coefficient zero. Their ordinary point composite is empty; their genuine composite by (10) and MUL* has precisely one nonzero index coefficient:
\[
\boxed{(R\circ S)_{\omega,\omega}=q(P,P)=P^2,\qquad
(R\circ S)_{ik}=0 \quad ((i,k)\ne(\omega,\omega)).}
\tag{11}
\]
The nonzero coefficient lies in the **closed, nonopen \((\omega,\omega)\) index sector**. This combines the **pointless Booleanization witness** from (10) with a genuinely nondiscrete scattered-coordinate decomposition. The example belongs to the unital associative matrix algebra constructed above.

**What it does *not* say.** The index topology has not disappeared from the locale; the support decomposition is in the **sublocale lattice**, and being **open** remains a topological constraint. The product need not be a discrete coproduct, and unrestricted relation composition outside the coefficient algebra remains potentially nonassociative.

## 5. What the binary study does not reduce to these three mechanisms

Three additional types of obstruction from the research archive remain mathematically distinct:

- **Bar/proof-tree rank** in the \(\mathcal V\)-program: finite separation trees can have arbitrarily large ranks, and an explicit **countable first-countable \(T_1\) example** with an exact rank-\(\omega\) bar gives \(\mathcal V\subsetneq\mathcal V_{\mathrm{fin}}\) **for that locale** (not a universal strictness statement). A derivation of a new exact rank is **not** a pointfree Booleanization witness or a localic matrix-composition rank. [Consolidated strictness proof](A-Vfin-negative-consolidated-proof-2026-10-23.md).
- **Hull iteration**: the closed/fitted \(\mathcal H\) process can have specified first stabilization ordinals \(\omega+m\), \(m\ge1\), with **closure** at limit stages. This is neither the \(\mathcal V\)-bar rank nor graph diameter. [Ordinal calculation](A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md).
- **Relational composition depth**: locally finite/rectangular Stone examples have graph components of ordinary diameter \(\le1\) yet arbitrarily growing localic composition rank; the sharp clique rank \(\operatorname{diam}(\Lambda)+1\), arbitrary finite connected overlap-graph realization and pointwise filtration **originated after an earlier referee verdict but have now received a separate focused independent audit** ([final adjudication](ProjectA_FINAL_FOCUSED_CLIQUE_UNITALITY_REFEREE_RECONCILIATION_2026-11-21.md)). [Stone rank canonical](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md).

The safe graph-extension results for **locally closed partial homeomorphisms**, the properness/Scott-continuity theorem \(L^*\), and fixed-bracketing quotient/effectivity work are significant **technical follow-ups** to Study I, not proof of a universal associative algebra. Their exact assumptions and distinct referee stages are in [the theorem ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) and [dependency atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md).

---

# Study II. Higher simultaneous witnesses and their limits

## 6. Higher witness data are not just powers of binary relation words

Let \(V\) be the Priestley patch Stone space of a **coherent** locale with its spectral specialization order. Define patched simplicial spaces
\[
\begin{aligned}
\mathrm{Ch}_n&=\{(x_0,\ldots,x_n):x_0\le\cdots\le x_n\},\\
I_n&=\{(x_i):\exists u\ \forall i,\ x_i\le u\},\\
D_n&=\{(x_i):\exists a\ \forall i,\ a\le x_i\},\\
M_n&=I_n\cap D_n.
\end{aligned}\tag{12}
\]
For \(I_n,D_n\), a **single simultaneous witness** bounds the **whole tuple**. Pairwise witnesses are not sufficient by definition. This is not a presentation of higher simplicial objects as arbitrarily bracketed binary relation products.

Their realizations \(\mathbf C,\mathbf I,\mathbf D,\mathbf M\) are in a **chosen sufficiently large Stone-sheaf \(\infty\)-topos**
\[
\mathscr H_\kappa=
\operatorname{Shv}_\infty
(\operatorname{Stone}_\kappa,\text{finite jointly-surjective covers}),
\]
not automatically in an intrinsic homotopy/shape theory of the locale. The fixed site and its effective Čech-cover inputs are substantive hypotheses.

A positive *reconstruction* theorem says that the **binary** common-upper graph \(I_1\), together with the **patch topology**, determines all higher patched \(I_n\), and dually \(D_1\) determines all \(D_n\), for **binary graph isomorphisms** with the required patch structure. One reconstructs principal lower/upper cones through maximal-element clique neighborhoods. This does **not** assert that an arbitrary graph-preserving map preserves all \(M_n\). [Coherent chain/hull canonical](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md), [binary meet canonical](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md).

## 7. The positive 1-type result has a sharp higher obstruction

A separate chain/meet-witness comparison constructs, via *local Stone-surjective witness covers* and **effective descent**, a common fundamental groupoid. On a meet edge \((x,y)\), the proposed arrow has the representative
\[
\gamma(x,y)=[x,u][y,u]^{-1}=[a,x]^{-1}[a,y],
\qquad a\le x,y\le u.
\tag{13}
\]
The proof must show independence of the upper/lower witnesses by local covers, not globally choose \(a,u\) as continuous sections. A separately imported **under-\(\mathbf C\)** comparison is required.

In the stated Stone-sheaf \(\infty\)-topos, after the effective degreewise Čech-descent and standard realization-connectivity lemma, one obtains the **post-verdict crosschecked** conclusion
\[
\boxed{\mathbf C\to\mathbf M\text{ is 2-connective: }
\pi_0,\pi_1\text{ are isomorphisms; }\pi_2\text{ is an epimorphism}.}
\tag{14}
\]
It is **not** a 2-type equivalence; injectivity on \(\pi_2\) is not asserted. Original external fourth-audit verdicts apply to their own supplied premises **P1–P6**, and the later groupoid/2-connectivity enhancements were *crosschecked after the original verdict*, not included in it. [Exact fourth-audit premise trace](PointFree_ENDGAME_FOURTH_AUDIT_PREMISE_TRACE_2026-11-21.md).

### Example 5. Six points distinguish all common-witness hulls from the chain 2-type

Let \(A_2,C_2\) be two-element antichains and define
\[
P=A_2\oplus B_{\rm anti}\oplus C_2,\qquad
Q=A_2\oplus B_{\rm chain}\oplus C_2,
\tag{15}
\]
where \(B_{\rm anti}\) is a two-element antichain and \(B_{\rm chain}\) a two-element chain. Both patch spaces are the **same discrete six-point space**, but their spectral orders differ only on the two middle points.

For *either* poset, a tuple has a common upper bound iff it does not contain **both different top points**, and a common lower bound iff it does not contain **both different bottom points**. These conditions do not depend on the middle order. Thus the entire patched simplicial objects \(I_\bullet,D_\bullet,M_\bullet\) **agree on the same labels**, including face and degeneracy maps.

However, chains do detect the middle order. Their order complexes satisfy
\[
|\mathrm{Ch}(P)|\simeq S^0*S^0*S^0\simeq S^2,\qquad
|\mathrm{Ch}(Q)|\simeq S^0*|\Delta^1|*S^0\simeq *.
\tag{16}
\]
The direct finite enumeration gives chain-complex face counts \((6,12,8)\) for \(P\) and \((6,13,12,4)\) for \(Q\), while the two meet-witness complexes each have face counts \((6,13,12,4)\). Moreover, \(M_\bullet(P)\) and \(M_\bullet(Q)\) are cones: adjoining either specified middle vertex does not introduce a prohibited extreme pair. Therefore
\[
\boxed{\mathbf M(P)\simeq\mathbf M(Q)\simeq *;\qquad
\mathbf C(P)\simeq S^2,\quad\mathbf C(Q)\simeq *.}\tag{17}
\]

**Proof boundary.** The *finite* chain-complex computation independently shows that any general comparison **cannot** be \(\pi_2\)-injective. It does **not** on its own establish the *general* 2-connectivity theorem (14), which rests on the specific Stone-sheaf descent and realization imports. Conversely, matching **all** patched \(I_n,D_n\) between P and Q does not identify their chain 2-types. [Six-point computation and source-status review](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md), [local connectivity stress test](PointFree_ENDGAME_BINARY_MEET_CONNECTIVITY_COLD_READ_2026-11-21.md).

This is the mathematically decisive reason to develop Study II as a **companion** to Study I rather than an afterthought derived from binary relational composition.

### Further higher-witness developments and stopping boundary

Stone-indexed nonconstant Čech gluing, classifying anima, relative cohomology and crosscut-connectivity ladders have significant audited, conditional, crosschecked, and internal components. Their precise status remains in the **C** section of the ledger. The seven-point poset \(A_2\oplus A_2\oplus A_2\oplus1\) disproves the naïve converse “one disconnected \(2\times2\) window forces failure of 3-connectivity”; a local bad window can coexist with globally contractible complexes. Do **not** promote the accompanying random-poset homology scripts to proofs of general homotopy statements. [Opus addendum reconciliation](ProjectA_OPUS_ADDENDUM_SPATIALITY_WINDOW_RECONCILIATION_2026-11-21.md).

---

# Synthesis and reference guide

## 8. A dependency map, not an omnibus novelty claim

| Mathematical interface | What is proved/available | What must not be inferred |
|---|---|---|
| Coherent/proconstructible gate | Patch-closed order computes **actual** Loc finite relation words; (2)–(3) | All arbitrary Loc relations associate; \(\mathcal W=\mathcal U\) follows from the composition theorem alone |
| Isbell/J–S/Plewe → rectangular RC | Closed support and Booleanization support (G′, **referee-origin, now separately blind-checked**); mixed p/q actual formula (9) and finite-join algebra separately reviewed; [focused referee reconciliation](ProjectA_FINAL_FOCUSED_CLIQUE_UNITALITY_REFEREE_RECONCILIATION_2026-11-21.md) | Weak/full or C-scattered criteria are historically new; infinite singleton expansion of arbitrary graphs |
| MAT* → MUL* → FINMAT* | Arbitrary locale \(P\), locally compact scattered \(K\), binary matrices; finite-support associative lift | A discrete-coproduct locale decomposition; arbitrary matrices associate merely from binary MUL* |
| Patched coherent premise → Stone Čech descent | Higher I/D reconstruction and conditional C→M 2-connectivity | All higher chain homotopy from binary graphs; independence of chosen Stone site or intrinsic locale shape |
| Hull and rank counterexamples | Nontransitive H, strict \(\mathcal V<\mathcal V_{\rm fin}\), finite/all cover bridge, unbounded composition rank | Equality of these *different* ranks; all points of a sublocale generate that sublocale |

**Evidence labels.** **L**: predecessor theorem in published literature; **E**: submitted claim checked in an independent model-referee packet with stated scope; **X**: post-verdict result separately crosschecked, often conditional on imported premises; **I**: internal or referee-addendum deduction not separately blind checked; **C**: explicit conditional hypotheses or standard imported result; **F**: disproved assertion. These are *not* substitutes for formal verification or human peer review, and they do not certify historical originality. The current [47-group theorem ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) is authoritative for individual labels. The [first editorial/source review](ProjectA_ENDGAME_EDITORIAL_SOURCE_CONSISTENCY_REVIEW_2026-11-21.md) records navigation and bibliographic repairs; the [second-pass 47-group evidence audit](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md) traces each claim's original report versus addendum/import status and records the A18/B15 label corrections. Neither is a mathematical reproof of 47 claims.

### Selected historical sources

The following are **antecedents and reference points**, not a bibliography establishing novelty for the project:

- P. J. Cameron and Vinod Kumar P. B., [*Graphs on Topological Spaces*](https://arxiv.org/abs/2610.14783) (2026): the pointwise graph motivation.
- J. R. Isbell, [*Product Spaces in Locales*](https://doi.org/10.1090/S0002-9939-1981-0589150-5), *Proc. Amer. Math. Soc.* **81** (1981), 116–118: universal product/spatial multiplier antecedents, as also reproduced in Plewe's Theorem 1.6.
- P. T. Johnstone and Shuhao Sun, [*Weak Products and Hausdorff Locales*](https://doi.org/10.1007/BFb0081358), in *Categorical Algebra and its Applications*, Lecture Notes in Mathematics **1348** (Springer, 1988), 173–193: weak/full product distinction.
- Till Plewe, [*Localic Products of Spaces*](https://doi.org/10.1112/plms/s3-73.3.642), *Proc. London Math. Soc.* (3) **73** (1996), 642–678: product-spatiality classifications and the closed-support/dense-trace method.

The exact source-versus-project-claim comparison is in the [current literature crosswalk](ProjectA_ENDGAME_LITERATURE_CROSSWALK_2026-11-21.md) and [full-text Plewe analysis](ProjectA_PLEWE_1996_FULL_PRIMARY_SOURCE_COMPARISON_2026-11-21.md). The full original Plewe journal PDF was supplied privately for the research reading but is **not** redistributed in this repository.

The full source history is deliberately **not** reorganized into this two-study order. Its temporal ordering matters for tracking repaired proofs, failed conjectures and independent reports; the [proof dependency atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md) and [open-frontier register](ProjectA_ENDGAME_OPEN_FRONTIERS_2026-11-21.md) retain that information.

## 9. The mathematical conclusion

**Ordinary graph pairs are useful but incomplete shadows of point-free structure.** We have identified rigorous domains in which (i) their patch-closed order reconstructs localic relations, (ii) compact closed supports explain additional pointless relational witnesses, and (iii) scattered-coordinate matrices retain every sublocale coefficient while restricting associativity to safe finite-support algebras. Higher simultaneous witnesses form a distinct, related theory whose first homotopy type is surprisingly accessible but whose higher homotopy is not determined even by all patched common-witness objects.

This answers the educational question that motivated the project more faithfully than either a universal “localic graph algebra” or a claim that all results share a single proof device. **The right output is a family of well-scoped calculi and their exact boundaries.**

**Recommended reader route:** this account → [five-example detailed calculations](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md) → [compact notation/assumptions](ProjectA_ENDGAME_NOTATION_AND_ASSUMPTIONS_2026-11-21.md) → [47-group ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) → chosen canonical proofs and original referee packets. Future publication, if desired, should be selected by **separate theorem-level priority checks**; the project itself may conclude without a paper.
