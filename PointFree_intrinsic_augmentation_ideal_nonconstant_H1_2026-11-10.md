# Point-Free Topology — The intrinsic augmentation ideal detects nonconstant twisted cohomology

**10 November 2026 · One bounded research segment after [the folded-coefficient threshold calculation](PointFree_Higman_twisted_cohomology_continuity_threshold_2026-11-10.md). INTERNALLY CHECKED ONLY; not externally audited, and no literature-priority claim.** This is the requested end of the bounded twisted-coefficient branch; [the binary-relation feedback roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md) is explicitly retained as the next branch. Standard background: crossed derivations and inner derivations represent first group cohomology, the universal property of internal free products, and group rings in condensed abelian sheaves.

## 0. Coherent-locale motivation and exact sheaf definitions

Take an **infinite Stone space** S and a discrete group G with an element \(1\ne g\in G\) of **infinite order**. Write \(A=h(S)\) for its representable sheaf on the sufficiently large Stone finite-surjection site, and
\[
\Pi=\mathop{*}_{A}\underline G
\]
for the internal free product of copies of the **constant** group G indexed by A. Let
\[
R_\Pi=\mathbb Z[\Pi],\qquad
J_\Pi=\ker(R_\Pi\xrightarrow{\varepsilon}\underline{\mathbb Z})
\]
be the **intrinsic** group-ring sheaf and augmentation ideal, both with left regular action by Π. For any internal Π-module M, write
\[
\mathscr H^1(\Pi;M)=
\underline{\operatorname{Der}}(\Pi,M)/
\underline{\operatorname{PDer}}(\Pi,M)
\]
for the **sheaf quotient** of internal crossed derivations \(d(xy)=d(x)+x\cdot d(y)\) by principal derivations \(x\mapsto x\cdot a-a\). This is the sheaf of internal first cohomology classes; it is not assumed equal to ordinary group cohomology of the point-evaluated group. Its restrictions to \(*\) nevertheless map naturally to ordinary \(H^1(\Pi(*);M(*))\), and **equality internally implies equality of the ordinary classes**.

For Higman's infinite torsion-free group H, the previously independently blind-checked pointed Stone-indexed face-poset construction gives a coherent locale \(X_H(S)\) such that both canonical chain-to-higher-hull arrows are equivalences and the common realization is \(E_S\simeq B\Pi\). Its ordinary integral homology sheaves all equal those of a point (proved in [the acyclic construction note](PointFree_relative_chain_splitting_acyclic_aspherical_nonconstant_2026-11-10.md)). The prior folded-coefficient local system (pullback of the constant H-augmentation ideal along Π→H) yielded a **constant** internal degree-one cohomology sheaf. The present note tests the truly **intrinsic** augmentation ideal \(J_\Pi\).

## 1. General theorem: nonconstant internal first twisted cohomology

**THEOREM (internally proved).** For any infinite Stone S and any discrete group G with an element g of infinite order,
\[
\boxed{\mathscr H^1(\Pi;J_\Pi)\text{ is NONCONSTANT},\qquad
\mathscr H^1(\Pi;R_\Pi)\text{ is NONCONSTANT}.}
\]
Indeed there is an explicit morphism \(h(S)\to\mathscr H^1(\Pi;J_\Pi)\) whose values at **distinct** points of S are distinct, and the same holds for \(R_\Pi\).

**Proof, Step 1: build a continuous family of intrinsic coefficients.** For every index s∈S denote by \(g_s\in\Pi(*)=\mathop{*}_{s\in S_{\mathrm{set}}}G\) the copy of g in the s-th factor. More intrinsically, the indexed free product supplies a sheaf morphism \(\gamma:A\to\Pi\) sending s to \(g_s\). Let \([\gamma]\) denote its image in the free group-ring sheaf. Using the two projections \(A_t\times A_s\rightrightarrows A\), define a **morphism of sheaves**
\[
\boxed{
m:A_t\times A_s\longrightarrow J_\Pi,\qquad
m(t,s)=([g_t]-1)([g_s]-1).
}
\]
Here juxtaposition is group-ring multiplication. The right side has augmentation zero and indeed belongs to \(J_\Pi^2\), so it defines the claimed map without choosing pointwise discontinuous sections.

**Step 2: build an internally continuous family of crossed derivations.** For each parameter t and index s, define a **principal G_s-derivation**, with values in the Π-module \(J_\Pi\), by
\[
\boxed{d_t(x_s)=(x_s-1)m(t,s),\qquad x\in G.}
\]
Each is a crossed derivation on its indexed copy of G. The **internal universal property of the indexed free product** assembles these into a crossed derivation \(d_t:\Pi\to J_\Pi\). As t varies, this construction is natural in Stone test spaces and yields a sheaf morphism \(A\to\underline{\operatorname{Der}}(\Pi,J_\Pi)\), hence an element
\[
\sigma\in\mathscr H^1(\Pi;J_\Pi)(S).
\]

**Step 3: show its point-values are pairwise distinct.** Choose distinct \(t,u\in S\). Suppose their restrictions \(d_t,d_u\) become cohomologous even in the **ordinary** group cohomology \(H^1(\Pi(*);J_\Pi(*))\). Then there exists \(a\in J_\Pi(*)\subseteq\mathbb Z[\Pi(*)]\) such that for **every** index s, evaluating the two derivations on \(g_s\) gives
\[
(g_s-1)\bigl(m(t,s)-m(u,s)-a\bigr)=0.
\tag{1}
\]
Since g_s has infinite order, **left multiplication by \(g_s-1\) on the ordinary group ring \(\mathbb Z[\Pi(*)]\) is injective**: a finitely supported group-ring element fixed by an infinite-order left translation must vanish. Hence
\[
a=m(t,s)-m(u,s)=([g_t]-[g_u])([g_s]-1)
\quad\text{for every }s\in S.
\tag{2}
\]
Choose distinct \(s_1,s_2\notin\{t,u\}\), possible because S is infinite. Subtract (2) at s_1 and s_2 to obtain
\[
0=([g_t]-[g_u])([g_{s_1}]-[g_{s_2}])
=[g_tg_{s_1}]-[g_tg_{s_2}]-[g_ug_{s_1}]+[g_ug_{s_2}].
\tag{3}
\]
But \(g_tg_{s_1},g_tg_{s_2},g_ug_{s_1},g_ug_{s_2}\) are **four distinct reduced words** in the free product of the four distinct indexed G-factors. Their basis elements in the ordinary integral group ring are linearly independent; the right side of (3) cannot vanish. Contradiction.

Thus \(t\mapsto[d_t]\) is injective into ordinary group cohomology at point evaluation. In particular the point-restrictions of the **internal** sheaf class σ are pairwise distinct: equality in the sheaf would imply equality after passing to ordinary group cohomology. σ therefore has infinitely many distinct point-values.

**Step 4: conclude nonconstancy.** A section of a **constant discrete abelian group sheaf** over compact Stone S is a locally constant function S→M_disc, and its point-value image is finite. If \(\mathscr H^1(\Pi;J_\Pi)\) were a constant group sheaf, the section σ would have finite image, contradiction. Thus it is nonconstant.

**Regular group-ring coefficients:** Each \(d_t\) also takes values in \(R_\Pi\) via \(J_\Pi\hookrightarrow R_\Pi\). The same argument permits a principal comparison element \(a\in R_\Pi(*)\) instead of a∈J and still obtains (1)–(3); therefore its classes in \(\mathscr H^1(\Pi;R_\Pi)\) are pairwise distinct. This proves the second assertion. QED.

**Group-level sanity check:** The key contradiction uses only the universal normal form of the free product and the finite-support property of the ordinary group ring. No invocation of Higman's duality, perfectness or acyclicity is needed in this **nonconstancy** proof—only an element of infinite order. The Higman group is special because the underlying coherent common-hull object is aspherical **and ordinary-homology-acyclic**, making this a sharp twisted-coefficient detection theorem.

## 2. Comparison with the previous folded calculation

The two coefficient systems are **different**, even though both are called augmentation ideals:

| Coefficient sheaf on \(B\Pi\) | Action and origin | Result for internal \(\mathscr H^1\) |
|---|---|---|
| \(\rho^*\underline{I_H}\), where \(\rho:\Pi\to\underline H\) folds all factors | **Constant underlying abelian sheaf**, Π-action factors through H | **Constant sheaf** \(\underline{(\mathrm{LC}(S,I_H)/I_H)\oplus\mathrm{LC}(S,\mathbb Z)}\) (previous internally checked calculation) |
| \(J_\Pi=\ker(\mathbb Z[\Pi]\to\mathbb Z)\) | **Intrinsic, nonconstant underlying sheaf** with full indexed Π-action | **NONCONSTANT** internal \(\mathscr H^1\), theorem above |
| \(R_\Pi=\mathbb Z[\Pi]\) | Full regular Π-module sheaf | **NONCONSTANT** internal \(\mathscr H^1\), same explicit family |

The intrinsic \(J_\Pi\) result does **not** contradict the constant folded calculation: the coefficient objects and their Π-actions are different. The source of variation is not merely the existence of nontrivial cohomology of H: it is the impossibility of making an indexed family of principal derivations into one **globally principal derivation** in the full group-ring module.

Our construction shows **nonconstancy**, not a complete description of \(\mathscr H^1\) as an extension or presentation. A possible larger calculation using H's one-ended duality and \(H^1(H,\mathbb Z[H])=0\) is intentionally **not attempted** in this bounded segment.

## 3. Consequences for the locale program and explicit stopping point

For the Higman coherent locale \(X_H(S)\) with infinite Stone S, the previously audited pointed gluing gives
\[
\mathbf C(X_H(S))\xrightarrow{\sim}\mathbf I(X_H(S)),
\qquad
\mathbf C(X_H(S))\xrightarrow{\sim}\mathbf D(X_H(S)),
\]
and the common object \(E_S=B\Pi\) has **ordinary homology sheaves of a point** but a nonconstant π₁. The new theorem proves more:
\[
\boxed{\mathscr H^1(E_S;J_\Pi)\text{ is nonconstant,}}
\]
where the coefficient sheaf itself is the intrinsic augmentation ideal of \(\pi_1(E_S)\); the same holds for \(\mathbb Z[\Pi]\). This is a **positive bounded answer** to the question left open in [the previous note](PointFree_Higman_twisted_cohomology_continuity_threshold_2026-11-10.md).

**Important boundaries:** Nothing has been proved about reconstruction of S from the **unmarked** twisted-cohomology sheaf, higher twisted cohomology in arbitrary degrees, finite-rank parametrized bundles, localic intrinsic shape, or equality among original binary separation relations. No independent audit or priority search has occurred. Standard derivation background: crossed derivations and principal derivations represent H¹; e.g. [Gerig, *Group Cohomology* exercise solutions](https://scholar.harvard.edu/files/gerig/files/group_cohomology.pdf), Chapter IV §2. Group rings of condensed groups and free abelian sheaves are standard, e.g. [Schütz, *Lectures notes on topoi and condensed math* §5.6](https://janschuetz.perso.math.cnrs.fr/lehre/lecture_notes_topcond.pdf).

**Next chosen branch after the user-authorized single bounded segment:** Return to the **original binary localic separation hierarchy**, following the already saved [concrete roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md). The first example there is the audited pointed triangle-face-poset wedge: binary \(\mathcal I(X)\) and \(\mathcal D(X)\) remain **incomparable** even though **both canonical higher chain-to-hull realizations are equivalences**. This is a clear warning that unfiltered total realization forgets binary relation distinctions. The next research target is to find useful *filtered or relative* invariants that retain some of that information, not to falsely infer binary equality from homotopy equivalence.
