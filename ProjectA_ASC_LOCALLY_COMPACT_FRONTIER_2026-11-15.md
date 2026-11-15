> **RESOLVED 15 NOVEMBER 2026 — HISTORICAL FRONTIER NOTE.** Question (LC-A) below is **answered negatively**, contrary to its old unresolved label. The independent blind referee confirmed the compact, locally compact, sober T1 counterexample. See [canonical negative theorem](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md), [reconciliation](ProjectA_LCA_EXTERNAL_REFEREE_RECONCILIATION_2026-11-15.md), and [follow-up register](ProjectA_LCA_FOLLOWUP_AND_A_DUAL_QUESTIONS_2026-11-15.md). The open LC-PT point-fitting converse and A-DUAL question replace LC-A as next research tasks; the historical exploration below is preserved, not current.

# Project A — Beyond stable local compactness: first oriented-specialization tests

**Research frontier note · 15 November 2026.** This note begins the post-(A-SC) investigation. Its new observations are **internally checked only**, not independently blind-refereed. The [independently audited theorem](ProjectA_ASC_CANONICAL_2026-11-15.md) proves \(\mathcal A(X)\) spatial for every *stably* locally compact \(X\). The question here is whether stable continuity is necessary when \(X\) is merely locally compact and sober.

## 1. The unresolved general question

Let \(\mathcal A(X)\hookrightarrow X^2\) be the actual sublocale presented by \(u_1\le u_2\) for all \(u\in\mathcal O(X)\), with point graph \(G_{\le_X}\).

**Question (LC-A).** Is \(\mathcal A(X)\) spatial for every locally compact locale \(X\) (equivalently, classically, every locally compact sober space)?

The stable-compact proof does not settle this: for a general continuous frame \(L\), the approximation map \(\iota(u)=\{v:v\ll u\}\) preserves arbitrary joins but need not preserve **binary meets**. Hence it need not be the inverse-image map of a locale retraction from an open spectral locale.

There is not yet a positive theorem or counterexample in this full class.

## 2. Spatiality is local under an open cover of the source

**Lemma 2.1 (open-cover local test; all locales).** Suppose \(X\) has an open cover by sublocales \(U_i\hookrightarrow X\) such that every \(\mathcal A(U_i)\) is spatial. Then \(\mathcal A(X)\) is spatial.

*Proof.* Let \(u_i\in\mathcal O(X)\) represent the cover, so \(\bigvee_i u_i=1\). On \(\mathcal A(X)\), the defining inequality \(u_{i,1}\le u_{i,2}\) gives

\[
u_{i,1}\wedge u_{i,2}=u_{i,1}.
\tag{2.1}
\]

The sublocale restriction formula

\[
\mathcal A(U_i)
=U_i^2\times_{X^2}\mathcal A(X)
\tag{2.2}
\]

shows that \(\mathcal A(U_i)\) is precisely the open sublocale of \(\mathcal A(X)\) determined by \(u_{i,1}\wedge u_{i,2}\), hence by \(u_{i,1}\). These opens cover \(\mathcal A(X)\), since \(\bigvee_i u_{i,1}=1\).

A locale covered by spatial open sublocales is spatial: if two opens \(a,b\) differ, distributivity yields an \(i\) with \(a\wedge u_{i,1}\ne b\wedge u_{i,1}\); a point of the corresponding spatial open sublocale separates their restrictions, hence distinguishes \(a,b\) in the whole locale. \(\square\)

**Corollary 2.2.** Every locale admitting an open cover by stably locally compact open sublocales has spatial \(\mathcal A(X)\), even if \(X\) itself is not stably locally compact.

The stronger corollary with all cover pieces merely satisfying spatial \(\mathcal A\) is already Lemma 2.1.

## 3. Adjoining a specialization bottom preserves the answer

For any locale \(X\) with frame \(L\), form the **bottom lift** \(Y=X_\bot\) with frame \(L^\top=L\cup\{1'\}\), where the old top \(d=1_L\) lies strictly below the new top \(1'\). The open sublocale of \(Y\) determined by \(d\) is \(X\), while the complementary closed sublocale is the singleton \(\{\bot\}\).

**Lemma 3.1 (open/closed spatiality test).** If \(S\) has an open sublocale \(O(a)\) and complementary closed sublocale \(C(a)\), and both are spatial, then \(S\) is spatial.

*Proof.* The respective quotient maps on frames send \(w\mapsto w\wedge a\) and \(w\mapsto w\vee a\). They are jointly injective in any distributive lattice. Indeed, if \(w\wedge a=z\wedge a\) and \(w\vee a=z\vee a\), then

\[
w=w\wedge(z\vee a)=(w\wedge z)\vee(w\wedge a)
=(w\wedge z)\vee(z\wedge a)=z.
\]

If \(w\ne z\), at least one restriction differs and a point of the corresponding spatial sublocale distinguishes them in \(S\). \(\square\)

**Proposition 3.2 (bottom-lift invariance).** For a spatial locale \(X\),

\[
\boxed{\mathcal A(X)\text{ spatial}\iff\mathcal A(X_\bot)\text{ spatial}.}
\tag{3.1}
\]

*Proof.* The forward implication is the substantive one. Let \(Y=X_\bot\). In \(\mathcal A(Y)\), write \(a=d_1\) for the open “first coordinate lies in \(X\)”. Since \(d_1\le d_2\) on \(\mathcal A(Y)\), the open sublocale \(O(a)\) is the pullback of \(\mathcal A(Y)\) along \(X^2\hookrightarrow Y^2\), hence is **\(\mathcal A(X)\)**.

The complementary closed sublocale \(C(a)\) imposes \(d_1=0\). Every old open \(u\in L\) satisfies \(u_1\le d_1\), so it vanishes on \(C(a)\). Thus the first coordinate factors through the closed singleton \(\{\bot\}\hookrightarrow Y\), and all inequalities \(u_1\le u_2\) become automatic. The second coordinate is unrestricted. By the universal properties, this identifies

\[
C(a)\ \cong\ \{\bot\}\times Y\ \cong\ Y.
\tag{3.2}
\]

If \(X\) is spatial, its lift \(Y\) is spatial as well: ordinary points of \(X\) distinguish old opens, and the new bottom distinguishes the added top \(1'\) from every old open. Hence both \(O(a)\cong\mathcal A(X)\) and \(C(a)\cong Y\) are spatial. Lemma 3.1 gives spatiality of \(\mathcal A(Y)\).

Conversely \(\mathcal A(X)\) is open in \(\mathcal A(Y)\), so spatiality of \(\mathcal A(Y)\) implies that of \(\mathcal A(X)\). \(\square\)

This proposition is **not** a consequence of stable local compactness of the lift: if \(X\) is nonstable, its bottom lift can be nonstable too. It follows from the special open/closed decomposition of the oriented order relation.

## 4. A sharp nonstable sequence-space control

Recall the referee's compact locally compact sober **noncoherent** space \(X_1\) from the [SC+ canonical note](ProjectA_SCplus_CANONICAL_2026-11-15.md), §5:

\[
X_1=\{\bot,a,p\}\sqcup\{g_n:n\in\mathbb N\}.
\]

Its opens are the whole space and those sets missing \(\bot\) such that:

- if \(a\) belongs to an open, all \(g_n\) belong to it;
- if \(p\) belongs to an open, all but finitely many \(g_n\) belong to it.

In the previous project phase this gave a counterexample to extending the **SC+** equivalence beyond stable local compactness. It is therefore an especially natural control for the *different* question (LC-A).

Put \(X_0=X_1\setminus\{\bot\}\), an open subspace. There are two open subspaces

\[
A=\{a\}\cup\{g_n:n\in\mathbb N\},
\qquad
P=\{p\}\cup\{g_n:n\in\mathbb N\},
\qquad X_0=A\cup P.
\]

Both are coherent:

- \(A\) is the one-bottom-point Alexandrov cone over countably many isolated maximal points. Its compact opens are finite subsets of \(\{g_n\}\) and all of \(A\), a bounded distributive basis.
- \(P\) is the one-point compactification of a countable discrete space, a compact zero-dimensional Hausdorff space.

Yet \(X_0\) is **not** stably locally compact. The sets \(A,P\) are compact saturated open subsets of \(X_0\), but \(A\cap P=\{g_n:n\in\mathbb N\}\) is infinite discrete and noncompact. The space \(X_0\) is compact, locally compact and sober (open in the known sober \(X_1\)).

By coherent (A-SC) on \(A\) and \(P\), and Lemma 2.1,

\[
\boxed{\mathcal A(X_0)\text{ is spatial, although }X_0\text{ is not stably locally compact}.}
\tag{4.1}
\]

Finally \(X_1\cong(X_0)_\bot\), so Proposition 3.2 yields

\[
\boxed{\mathcal A(X_1)\text{ is spatial as well}.}
\tag{4.2}
\]

This gives a **positive** LC-A test at the very example which refutes the broader SC+ equivalence. The two questions have different sharpness boundaries.

## 5. Other controls and next tasks

**Regular locales.** For every regular locale \(X\), \(\mathcal A(X)=\Delta_X\). Indeed, if \(v\prec u\) is well inside \(u\), choose an open \(v^*\) with \(v\wedge v^*=0\), \(v^*\vee u=1\). On \(\mathcal A(X)\), \(v^*_1\le v^*_2\), so \(v_2\wedge v^*_1=0\), and

\[
v_2=v_2\wedge(v^*_1\vee u_1)\le u_1.
\]

Taking the join over \(v\prec u\) gives \(u_2\le u_1\). Thus the projections agree, so the relation is the diagonal. In particular, all locally compact regular locales are LC-A-positive.

**Remaining question.** We do **not** know whether every locally compact sober \(X\) has spatial \(\mathcal A(X)\). The open-cover lemma and the bottom-lift proposition exclude two natural classes of false counterexamples. In a genuine negative example, failure of spatiality cannot be explained merely by a noncoherent intersection of coherent open subspaces followed by adjoining a bottom point.

Natural next tasks:

1. Find a locally compact sober space whose nonstable behavior cannot be removed by coherent/stable open localization and bottom lifting.
2. Or prove a more general spatiality criterion for \(X^{\mathbb S}\) from mere continuity of \(\mathcal O(X)\), without needing meet-stability of the approximation map.
3. Keep careful track of point-generated versus presented sublocales: a locally compact nonstable **SC+** counterexample does not automatically refute (LC-A).

**Status:** Sections 2–4 are newly derived, internally checked working results. They have not received an independent blind audit and should not be promoted to the same evidential tier as the stably locally compact (A-SC) theorem.


## 6. Subsequent internal tests (15 November 2026)

A further internally checked note, [Semilattice retractions and nonstable LC-A tests](ProjectA_ASC_MEET_RETRACTION_2026-11-15.md), develops:

1. A pointfree **meet/join retraction principle**: a compatible continuous idempotent semilattice operation makes \(\mathcal A(X)\) a locale retract of \(X^2\); if the square is spatial, so is \(\mathcal A(X)\).
2. An explicit **nonstable sober Alexandrov meet-semilattice** \(P=\{c,a,p,g_0,g_1,\ldots\}\) with \(c<a,p<g_n\) and \(g_{n+1}<g_n\), where \(\uparrow a\cap\uparrow p=\{g_n\}\) is noncompact. The only open containing \(c\) is \(P\), so **no** stable/coherent open cover exists; nonetheless \(\mathcal A(P)\) is spatial by retraction.
3. The referee's noncoherent sequence-tree \(T\) is covered by coherent open cones and tail neighborhoods; therefore \(\mathcal A(T)\) is spatial.
4. A **closed-point obstruction**: the fiber of \(\mathcal A(X)\to X\) over \(p\) is \(\operatorname{fit}_X([p])\); if \(p\) is closed, its nonspatiality would imply that \(\mathcal A(X)\) is nonspatial.
5. The specialization graph \(G_{\le_X}\) is a **sober topological subspace** of \(X^2\) whenever \(X\) is sober. This alone does not establish spatiality of the presented relation.

These deductions await external audit. **(LC-A) remains open.**


## 7. Ideal completion and continuous-dcpo Scott spaces

The internally checked note [Ideal completion and continuous-domain spatiality](ProjectA_ASC_IDEAL_COMPLETION_2026-11-15.md) proves a full frame isomorphism
\[
\mathcal A(\operatorname{Idl}(P))\cong\operatorname{Idl}(P^\to),
\qquad P^\to=\{(p,q):p\le q\}
\]
for every poset \(P\), and hence spatiality for all algebraic-dcpo Scott locales. The standard Scott-continuous retraction \(D\to\operatorname{Idl}(D)\to D\), \(x\mapsto\{a:a\ll x\}\mapsto\sup I\), extends this to **every continuous-dcpo Scott locale**. The earlier sober Alexandrov theorem follows as a special case.

These results are internally checked, not independently refereed. They do not answer (LC-A) for arbitrary locally compact sober spaces, which need not be Scott spaces of continuous dcpos.


## 8. A sharpened \(T_1\) test (internal observation)

If \(X\) is locally compact, sober and \(T_1\), its point specialization graph is the diagonal. Hence
\[
\mathcal A(X)\text{ spatial}\quad\Longleftrightarrow\quad
\mathcal A(X)=\Delta_X.
\]
Indeed, a spatial sublocale is generated by its points, and \(\Delta_X\) is spatial.

If \(X\) is **locally Hausdorff**, it has an open cover by locally compact Hausdorff (hence regular) open subspaces \(U_i\). The regular-locale calculation gives \(\mathcal A(U_i)=\Delta_{U_i}\); the open-cover lemma then makes \(\mathcal A(X)\) spatial and therefore equal to its diagonal.

Thus a negative \(T_1\) test would have to be a locally compact sober \(T_1\) space that is **not locally Hausdorff**, with pointfree oriented relation strictly larger than the diagonal. Its closed-point fibers \(\operatorname{fit}([p])\) offer one necessary-condition test. No such example has yet been produced here.
