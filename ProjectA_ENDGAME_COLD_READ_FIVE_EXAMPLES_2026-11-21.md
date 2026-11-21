# Cold read: five examples that explain the point-free topology project
## Endgame first-reading mathematical walkthrough · 21 November 2026

**Audience:** a mathematically experienced reader who was **not** present during the project. This is a **worked guide**, not a new independent proof or a claim of publication novelty. Source statements below have been reopened in their dated repository canonical proofs. For current theorem IDs and precise audit scopes use [ledger v3.1](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md), [proof dependencies](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md), and [21 Nov consolidation audit](ProjectA_ENDGAME_CONSOLIDATION_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md). The main project grew from Cameron–Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783.

## Five-minute common vocabulary

For a locale X, write \(X^2=X\times_{\mathrm{Loc}}X\), not an ordinary frame direct product, and \(\Delta\hookrightarrow X^2\) for its diagonal. The separation relations are
\[
\mathcal I=\operatorname{cl}\Delta,\quad
\mathcal D=\operatorname{fit}\Delta,\quad
\mathcal V=\operatorname{fit}\mathcal I,\quad
\mathcal W=\operatorname{cl}\mathcal D,\quad
\mathcal U=\text{Urysohn relation},\quad
\mathcal F=\text{functional equivalence}.
\]
\(\mathcal H\) is the **least relation containing Δ both closed and fitted**; \(\mathcal A\) is oriented specialization and \(\mathcal S=\mathcal A\vee\mathcal A^\smile\). All \(\le\) and \(\vee,\wedge\) refer to inclusion/lattice operations of **sublocales**, not just sets of ordinary points. The project order convention is \(x\le y\) iff \(x\in\overline{\{y\}}\); **opens are upsets** (opposite to Cameron–Kumar's displayed order convention). Composition of localic relations is image of their **genuine localic composability pullback**. It need not associate in general.

## Example 1 — a five-point fence: graph intuition and an explicit finite calculation

Let P={m,a,k,b,n} with only strict order relations
\[
a<m,\quad a<k,\quad b<k,\quad b<n.
\]
For upper Alexandrov opens, the comparability graph is the path \(m-a-k-b-n\) and hence connected. The ordinary inseparability relation I consists of pairs with a **common upper bound**; the fitted diagonal D consists of pairs with a **common lower bound**. These are different:
- \((a,b)\in\mathcal I\), with witness \(k\); \((a,b)\notin\mathcal D\).
- \((m,k)\in\mathcal D\), with witness \(a\); \((m,k)\notin\mathcal I\).

Because this finite locale's relations are point-determined, coherent composition gives \(\mathcal U=\mathcal I^2\), and direct enumeration yields
\[
\boxed{\mathcal U(P)=\mathcal W(P)=P^2\setminus\{(m,n),(n,m)\},
\qquad \mathcal H(P)=\mathcal F(P)=P^2.}
\]
For instance \(m\) and \(n\) have no two-hop I path; all other pairs do. A continuous real-valued function is constant along each specialization comparison, hence constant on this connected comparability graph, explaining F=P².

**Lesson:** the hierarchy already separates relations on finite spaces, with a simple order-graph description. Coherent powers can be literal localic powers because of the **separate coherent composition theorem**.

**Source and status:** [finite fence §§3–6](A-W-HmeetU-connected-example-finite-poset-product-2026-11-09.md), [W-phase independent audit reconciliation](ProjectA_Wphase_EXTERNAL_referee_reconciliation_2026-11-09.md). For the original Cameron–Kumar graph convention and dictionary see [revisit §1–2](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md).

## Example 2 — two convergent Priestley zigzag rays: \(\mathcal H\) fails transitivity

Let P={t}∪A∪B, where \(A=\{a_i:i\ge0\}\) and \(B=\{b_i:i\ge0\}\) are alternating order-zigzag rays, with no comparisons across A and B or to t. Give P the **patch** topology of the one-point compactification of the discrete A∪B: both rays converge to t. This is a Priestley space, defining a coherent spectral locale X.

Write \(S_A=A\cup\{t\},\ S_B=B\cup\{t\}\). The canonical proof identifies the **actual closed-and-fitted** diagonal hull as
\[
\boxed{\mathcal H=(S_A^2)\vee(S_B^2)}
\]
(the union is a finite union of closed sublocales, and the calculated point set is the corresponding patch-closed set). Its pairs include \((a_0,t)\) and \((t,b_0)\) but not \((a_0,b_0)\). The localic composability pullback contains the **ordinary generalized witness** \((a_0,t,b_0)\); hence
\[
\boxed{\mathcal H\circ\mathcal H\nleq\mathcal H.}
\]
The same audited example has \(\mathcal U\vee\mathcal V<\mathcal H<\mathcal F\). A separate coherent theorem says \(\mathcal H\) is internally transitive **iff** \(\mathcal H=\mathcal F\).

**Lesson:** closure under both **closedness** and **fittedness** is not closure under relational transitivity. Taking the least closed-and-fitted relation is not the same as taking an equivalence closure. The paired zigzag limits make the difference visible. In related coherent examples the explicit **closed-stage alternation** first stabilizes at \(\omega+m\), each m≥1; this is an ordinal *hull-iteration* invariant, not the V separation-tree rank.

**Source/status:** [two-ray proof §§1–8 and 11](A-H-two-convergent-zigzag-rays-nontransitive-coherent-counterexample-2026-10-24.md), [ordinal stages](A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md), **externally accepted** [post-V audit](A-postV-external-audit-reconciliation-2026-10-24.md).

## Example 3 — the rational bridge: finite versus all covers retain nonspatial information

Start with two **open** real-line sheets \(S=\{s_x\}\), \(T=\{t_x\}\). At each rational \(q\) add a bridge point \(b_q\) with basic neighborhood
\[
N(q,\epsilon)=\{b_q\}\cup\{s_x:q-\epsilon<x<q\}\cup\{t_x:q<x<q+\epsilon\}.
\]
The map \(p:X\to\mathbb R\) sending every point to its coordinate is an **étale local homeomorphism**. X is second countable, sober, locally compact and T1, but not Hausdorff. By de Brecht's established theorem (a later, post-audit observation), X is also quasi-Polish.

The *infinite* cover by the two sheets and all their bridge section charts provides enough local agreement to force
\[
\mathcal D(X)=\Delta_X,\qquad \mathcal W(X)=\mathcal I(X).
\]
For **every finite** open cover, however, its diagonal-cover square has a **dense** matching locus on the cross-sheet fibre sector
\[
J=S\times_{\mathbb R}T\cong\mathbb R.
\]
This finite-cover density is a Baire/category argument exploiting the dense rational bridge coordinates. The nonzero Isbell Booleanization \(B(J)\), **pointless**, lies in the finite-cover diagonal relation \(\mathcal D_2\wedge J\), but the full-cover relation \(\mathcal D\) misses J. Closing that nonzero dense Boolean witness fills J. The full computation gives
\[
\boxed{\mathcal D=\Delta,\quad \mathcal W=\mathcal I<\mathcal W_2=\mathcal U=X\times_{\mathbb R}X.}
\]
Even though the finite and full diagonal-cover relations have the **same ordinary point pairs**, their closed localic hulls differ. This refutes both Q and Q′.

**Lesson:** no ordinary graph on the original point pairs can capture the whole finite-versus-infinite-cover obstruction. The strictness is a nonspatial nucleus/Booleanization effect.

**Source/status:** [Q/Q′ canonical §§0–7](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md), [audit reconciliation](ProjectA_Q_DENSE_RATIONAL_BRIDGE_REFEREE_RECONCILIATION_2026-11-14.md). Quasi-Polish consequence belongs to the later [literature review](ProjectA_ENDGAME_COUNTEREXAMPLE_RANK_LITERATURE_FOCUSED_REVIEW_2026-11-21.md) and was not a separate blind-audited construction.

## Example 4 — rational/irrational middle overlap: why point-relation composition fails

Let G=[0,1] and for ordinary A,B⊆G define
\[
p(A,B)=[A\times B]_{G^2},\qquad
q(A,B)=[A]_G\times_{\mathrm{Loc}}[B]_G.
\]
By **Johnstone–Sun 1988**, p is the weak product of the two induced spatial locales, q their full localic product; \(p\le q\) with p dense in q, and they need not coincide. The independently audited **mixed rectangular rule** says, for r,s chosen independently from p or q:
\[
r(A,B)\circ s(C,D)=
\begin{cases}
q(A,D),&[B]_G\wedge[C]_G\ne0,\\
0,&[B]_G\wedge[C]_G=0.
\end{cases}
\]
The q output itself may be zero if outer supports are empty. Its **finite-join rectangular algebra** is associative, converse-closed, zero-containing and finite-join-distributive, **not asserted unital**. Adjoining locally closed partial-homeomorphism graphs produces a larger unital algebra under specified conditions.

Take B=Q∩G and C=G\Q, A=D=G. Then B∩C=∅ as **ordinary point sets**, so the ordinary point-relational composite is empty. But the two induced sublocales \([B]\), \([C]\) are both dense and contain the least dense (Booleanization) sublocale of G, so
\[
[B]\wedge[C]\ne0,\qquad
\boxed{p(G,B)\circ p(C,G)=q(G,G)=G^2.}
\]
**Lesson:** the localic witness in the middle can be nonzero with **no ordinary point**; composition sees more than set-theoretic witnesses. The historical weak/full-product distinction is classical; the mixed composition rule is a separate localic calculation.

**Source/status:** [rectangle proof §§1–6](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), [Johnstone–Sun primary comparison](ProjectA_ENDGAME_JOHNSTONE_SUN_WEAK_PRODUCTS_PRIMARY_SOURCE_2026-11-21.md). The rule was independently reviewed with repaired zero-case wording.

## Example 5 — a six-point poset illustrates the boundary of binary homotopy reconstruction

Let \(P=A_2\oplus A_2\oplus A_2\): three ordered layers of two incomparable points each. The order complex is the join of three 0-spheres, hence
\[
|\operatorname{Ch}_\bullet(P)|\simeq S^0*S^0*S^0\simeq S^2.
\]
For a coherent locale X, let \(I_n,D_n\) be the **patched simultaneous common-upper/common-lower witness** simplicial spaces and \(M_n=I_n\cap D_n\); the *higher* M_n is stronger than imposing a common witness pairwise. Write \(\mathbf C\) and \(\mathbf M\) for the corresponding realizations in a **chosen sufficiently large Stone-sheaf \(\infty\)-topos**.

The post-verdict cross-refereed theorem proves generally
\[
\boxed{\mathbf C(X)\longrightarrow\mathbf M(X)\ \text{is 2-connective},}
\]
i.e. π0 and π1 are isomorphisms and π2 is an epimorphism, **not necessarily an isomorphism**. For this six-point P, the canonical source calculates
\[
\boxed{\mathbf C(P)\simeq S^2,\qquad\mathbf M(P)\simeq1,}
\]
so the bound is sharp: π2 of the chain object is destroyed. It is a direct finite witness to the difference between *binary graph/chain 1-type reconstruction* and the genuinely higher data lost from binary descriptions. The binary I,D graphs **plus the patch topology** nevertheless recover all higher patched I_n and D_n as simplicial subsets; the functorial reconstruction requires a binary **isomorphism**, not arbitrary graph-preserving maps unless they preserve M₂.

**Lesson:** classification of binary relations, relational composition, and higher common-witness homotopy are connected but different. The Dowker strand is not simply a corollary of a binary graph hierarchy.

**Source/status:** [higher meet-hull canonical §§0–3](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md), [fourth-audit final reconciliation](PointFree_audit4_FINAL_RECONCILIATION_2026-11-11.md). The groupoid and sharp 2-connectivity results were **post-verdict proposals independently cross-checked by the opposite referee**, not claims included in the original blind packet. The proofs use preexisting **P1–P6** premises that the fourth referee **did not reprove**; see [cold-read dependency trace](PointFree_ENDGAME_FOURTH_AUDIT_PREMISE_TRACE_2026-11-21.md). No intrinsic localic shape theorem or site-independence is claimed.

---

## Lessons from the cold read

1. **Logical flow succeeds**, once the operations and scopes are stated before the examples. Finite posets explain the graph layer; nontransitive H and the rational bridge explain why hulls remain subtle; rectangles show why composition is genuinely pointfree; six points explain the higher-witness limit.
2. The existing [big-picture spine](ProjectA_ENDGAME_BIG_PICTURE_SPINE_2026-11-21.md) is a **survey of conclusions** rather than a worked introduction. A newcomer needs *this* example-first route before reading the 46-row theorem ledger.
3. **Source-status distinction is essential:** independently blind-reviewed theorem, separately crosschecked referee addendum, and after-verdict internally verified corollary are three different evidential levels. Avoid elevating them by sharing an umbrella document.
4. **Terminology requiring a glossary:** localic square and product, spatial/point-generated vs full sublocale, closure vs fitting, patch/spectral topology, lower/upper orientation, localic image, Booleanization, exact witness/finite-rank, P1–P6 imported site facts, n-connectivity.
5. **No new fatal mathematical defect was established in this five-example read.** It is a selective source-grounded cold read, not a second independent proof of each theorem.

**Recommended first-reading order:** this document → [start here](ProjectA_ENDGAME_START_HERE_2026-11-21.md) → [current ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md) → only the five linked canonical proofs that interest the reader → [dependency atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md). The original independently reviewed source mathematics, rather than this guide, retains evidential authority.
