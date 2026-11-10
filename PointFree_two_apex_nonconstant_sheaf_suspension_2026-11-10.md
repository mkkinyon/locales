# Point-Free Topology — A genuinely nonconstant coherent chain-nerve suspension

**10 November 2026 · New internally checked research segment; NOT externally audited.** Origin: the **second** independent referee's post-report suggestion #2 in [triage register](PointFree_referee2_mathematical_suggestions_triage_2026-11-10.md). The calculation below goes beyond the referee's suggestion by proving *sheaf-theoretic nonconstancy for every infinite Stone space* via an explicit first-homology sheaf section and characterizing exactly when the suspension is constant. The referee's idea did **not** form part of its independently blind-audited packet or report. Claims in this note are new *working deductions* within our project, not literature-priority claims. Start with [canonical coherent chain/hull account](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md).

## 0. Setup, convention and the coherent locale

Fix a sufficiently large Stone site \(\mathrm{Stone}_\kappa\) with the topology of finite jointly surjective covering families, including the empty cover of the empty Stone locale, and let \(\mathscr H=\operatorname{Shv}_\infty(\mathrm{Stone}_\kappa)\). Write \(h(T)\) for the representable sheaf of a Stone space T, and \(\underline Y\) for the constant-object functor from spaces. The latter is not the same as \(h(T)\) when \(T\) is infinite. We use the established, independently referee-checked facts: finite coproducts and appropriate intersections are carried by \(h\), finite Stone covers are effective epis, and evaluation at the one-point Stone object preserves colimits.

Let S be any **nonempty** Stone space (classical, with choice). Form the disjoint-union Stone space
\[
P(S)=S\;\sqcup\;\{p,q\}
\]
where the two apices are isolated, and order it by
\[
s<p,\quad s<q\qquad (\forall s\in S),
\]
with no comparisons between distinct s,t∈S and no comparison between p and q. Then \(P(S)\) is a Priestley space:
- the relation \(\le\) is patch-closed (the diagonal and the two compact sets S×{p}, S×{q});
- \(\{p\}\), \(\{q\}\) are clopen upsets;
- for s≠t in S, a clopen U⊆S containing s but not t gives the clopen upset U∪{p,q}.
Its clopen upsets, hence the compact opens of the associated coherent spectral locale \(X(S)\), form
\[
K(X(S))=\{\varnothing,\{p\},\{q\}\}\cup
\{U\cup\{p,q\}:U\in\mathrm{Clop}(S)\}.
\]
Equivalently \(K(X(S))\) is the ordinal sum of the four-element Boolean diamond \(\{0,p,q,c=p\vee q\}\) with \(B=\mathrm{Clop}(S)\), identifying c with 0_B. Thus this family has an **entirely bounded-distributive-lattice presentation**. S is the closed sublocale complementary to the compact open \(\{p,q\}\); its induced specialization order is equality and Patch S=S.

Put \(Z_p=S\sqcup\{p\}=C(\{q\})\) and \(Z_q=S\sqcup\{q\}=C(\{p\})\). These are closed, patch-clopen, specialization-downward-closed coherent sublocales, cover X, and intersect in S. The internal specialization category on Z_p (respectively Z_q) has a terminal point p (q).

## 1. Exact canonical-arrow calculation

Let
\[
\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet X)|,\quad
\mathbf I(X)=|h(\operatorname{Patch}I_\bullet X)|,\quad
\mathbf D(X)=|h(\operatorname{Patch}D_\bullet X)|
\]
be the established patched chain and higher closed/fitted diagonal realizations. These are **sheaf objects**, not ordinary homotopy types or locale shape.

**Theorem (referee-origin candidate, internally proved).**
\[
\boxed{\mathbf C(X(S))\simeq1\mathop{\amalg}\limits_{h(S)}1=:\Sigma_{\mathrm{unred}}h(S),
\qquad
\mathbf I(X(S))\simeq\mathbf D(X(S))\simeq1.}
\]
The two canonical arrows \(\mathbf C\to\mathbf I,\mathbf C\to\mathbf D\) correspond to the unique map from the internal unreduced suspension to the terminal object. Their common homotopy cofibre is
\[
\mathbf I\amalg_{\mathbf C}1\simeq
\mathbf D\amalg_{\mathbf C}1\simeq
\Sigma_{\mathrm{unred}}^2h(S).
\]

**Proof of C.** Every specialization chain in X lies in Z_p or Z_q (p and q cannot occur in one chain). The two simplicial subsheaves \(\operatorname{Ch}_\bullet Z_p,\operatorname{Ch}_\bullet Z_q\) have intersection \(\operatorname{Ch}_\bullet S\); this is the special case of the verified finite closed-cover Čech codescent theorem. Since p,q are terminal in the chain categories, their patched chain-nerve realizations are both 1; as the induced order on S is discrete, \(\operatorname{Ch}_n(S)=S\) and \(\mathbf C(S)=h(S)\). Therefore their homotopy pushout is \(\mathbf C(X)\simeq 1\amalg_{h(S)}1\), compatibly with the canonical maps.

**Proof of I.** In every degree n, tuples with a common upper witness in X are precisely
\[
I_n(X)=Z_p^{n+1}\cup Z_q^{n+1},
\]
because p and q are incomparable and each is an upper bound for every element of its own Z; intersection is \(S^{n+1}\). This is equality of actual coherent proconstructible sublocales, not just arbitrary sublocales determined by points. After Patch each component is a Čech nerve of a surjection to 1; for nonempty S these realize to 1, as does their intersection \(S^{\bullet+1}\). By finite Čech codescent and commuting realizations, \(\mathbf I(X)\simeq1\amalg_1 1\simeq1\).

**Proof of D.** The externally independently audited **canonical edgewise arrow equivalence** \((\mathbf C\to\mathbf I)\simeq(\mathbf C\to\mathbf D)\) in \(\mathbf C/\mathscr H\) implies \(\mathbf D(X)\simeq1\) and identifies the arrows. One must **not** assert unpatched descent of lower-witness maps. This is the only use of the earlier edgewise theorem.

**Relative cofiber:** Since the two targets are 1, their cofibres are \(1\amalg_{\mathbf C(X)}1=\Sigma_{\rm unred}\mathbf C(X)\simeq \Sigma_{\rm unred}^2 h(S)\). For |S|=2, C(X) has type S¹ and its relative cofibres type S², matching the refereed four-point computation.

## 2. The internal homology sheaf and nonconstancy

Write \(\mathbb Z[A]\) for the **free abelian sheaf** on a 0-truncated sheaf A (sheafification of T↦Z[A(T)]), and let \(\varepsilon:\mathbb Z[h(S)]\to\mathbb Z\) be augmentation. Because S→1 is a finite-cover effective epi, augmentation is epi. Define the reduced free condensed abelian group sheaf
\[
\mathcal K_S:=\ker\big(\mathbb Z[h(S)]\overset{\varepsilon}\longrightarrow\mathbb Z\big).
\]
The homological Mayer–Vietoris sequence of the homotopy pushout \(1\leftarrow h(S)\rightarrow1\), or reduced chain complexes of an unreduced suspension of a discrete sheaf, gives
\[
\boxed{\widetilde{\mathcal H}_1(\mathbf C(X(S));\mathbb Z)\cong\mathcal K_S,\qquad
\widetilde{\mathcal H}_j(\mathbf C(X(S));\mathbb Z)=0\;\;(j\ne1).}
\]
The suspension is connected (after h(S)→1 effective epi), and the *ordinary underlying point-evaluation* homotopy type is \(\Sigma_{\rm unred}(S_{\rm set})\), a wedge of \(|S|-1\) circles when S is finite and a free graph of rank |S| in the infinite case. Evaluation at the point preserves colimits and computes \(\mathcal K_S(*)=\ker(\mathbb Z[S_{\rm set}]\to\mathbb Z)\).

**Theorem (nonconstancy criterion).** For nonempty Stone S,
\[
\boxed{\mathbf C(X(S))\text{ is equivalent to a constant sheaf-homotopy object}\iff S\text{ is finite}.}
\]
**Proof, finite:** If S is finite, h(S)=coproduct of |S| copies of 1=\(\underline{S_{\rm set}}\), and \(\mathbf C(X(S))=\underline{\Sigma S_{\rm set}}\), as constant objects preserve homotopy colimits.

**Proof, infinite:** Fix \(s_0\in S\). The free abelian sheaf \(\mathbb Z[h(S)]\) has a canonical element \([\,\mathrm{id}_S\,]\) over the test Stone object S, since \(\mathrm{id}_S\in h(S)(S)\). The constant map \(c_{s_0}:S\to S\) gives another \([c_{s_0}]\). Their difference
\[
\sigma:=[\,\mathrm{id}_S\,]-[c_{s_0}]\in\mathcal K_S(S)
\]
has augmentation zero. For each point t:*=1→S, pullback gives
\[
t^*\sigma=[t]-[s_0]\in\mathcal K_S(*)=\ker(\mathbb Z[S_{\rm set}]\to\mathbb Z).
\]
These are **pairwise distinct** as t varies over any infinite S, hence the associated point-value function has infinite image.

A **constant abelian sheaf** \(\underline G\) on the Stone finite-surjection site evaluates at S as the group of locally constant maps \(S\to G_{\rm discrete}\); every such map has **finite image** because S is compact. Any isomorphism \(\mathcal K_S\simeq\underline G\) would identify the evaluations at all t by a fixed isomorphism \(G\simeq\mathcal K_S(*)\); then the section σ would have finite image, a contradiction. Thus \(\mathcal K_S\) is **not constant**. If \(\mathbf C(X(S))\) were a constant space object \(\underline Y\), its homology sheaves would be constant (constant-object functor is left exact and colimit-preserving, and hence commutes with the free abelian chain construction and associated homology). This contradicts the nonconstancy of \(\mathcal K_S\).

Therefore **every infinite Stone S**, in particular Cantor space or the convergent-sequence Stone space, yields a genuinely nonconstant sheaf-homotopy invariant. This answers the *existence* part of PF-Q01 positively, subject to an independent referee check before certified status.

**A stronger relative obstruction:** Since the canonical map \(\mathbf C\to\mathbf I,\mathbf D=1\), the relative cofibres are \(\Sigma_{\rm unred}^2h(S)\), whose nonconstant second reduced homology sheaf is the same \(\mathcal K_S\).

## 3. Literature/priorities and relation to the previous examples

The finite Stone-site sheaf setting and free abelian group construction are standard in **condensed mathematics**, not project inventions. For background: Commelin–Scholze, *Lectures on Condensed Mathematics / LTE*, where a profinite S defines a condensed set T↦Cont(T,S) and \(\mathbb Z[S]\) is the sheafification of T↦\(\mathbb Z[\mathrm{Cont}(T,S)]\). Discrete condensed groups give sheaves of continuous (= locally constant) maps T→G_disc. Sources: https://math.commelin.net/files/LTE.pdf and https://people.mpim-bonn.mpg.de/scholze/Condensed.pdf . Whether the precise two-apex construction and characterization have appeared elsewhere is **not checked**.

For S=2 the poset X(S) is the referee-audited four-point pseudo-circle, with \(\mathbf C\simeq\underline{S^1}\) and \(\mathbf I=\mathbf D=1\). For finite |S|=m≥1, C(X) is the constant homotopy type of a bouquet of m−1 circles; its canonical relative cofiber has type a bouquet of m−1 two-spheres. Infinite S is **different**, not merely an infinite supply of ordinary circles: the identity map of S supplies a **non-locally-constant family of homology classes** in the sheaf, whereas previous infinite X_T examples all had constant realizations. This uses the patch topology essentially.

The frame-theoretic compact-open lattice \(K(X(S))\) is the ordinal sum of a four-element Boolean diamond and the Boolean algebra \(B=\operatorname{Clop}(S)\). Thus we have an explicit algebraic criterion: **the homology sheaf is nonconstant iff \(B\) is infinite**. The stable zero/positive distinction is not visible from a single finite-quotient poset, although it is reflected in the full pro-system.

## 4. Guardrails and next bounded questions

- This is an **internal proof**, not yet an external audit. The high-priority audit checks are the simplicial Čech union comparison, homology Mayer–Vietoris inside \(\mathscr H\), and description of sections of constant discrete sheaves on the sufficiently large Stone site.
- Intrinsic **localic shape** remains unaddressed.
- The second referee's distinct suggestion #1, **finite compact-open-upset D-side relative Čech codescent**, is a promising next complementary lemma and does not contradict the independently established failure of **unpatched** lower-witness map descent.
- Optional: compute internal \(\pi_1\) as a **free group object on \(h(S)\) with the chosen generator \(s_0\) killed**, via sheaf-internal van Kampen; this should be proved, not assumed from the H1 calculation.
- Explore whether the suspension detects profinite topological distinctions between two infinite Stone spaces with the same cardinality of points, rather than merely differentiating finite from infinite; the sheaf \(\mathcal K_S\) is a natural candidate.
- Finite-stage inverse-limit comparison remains open: geometric realization must **not** be interchanged blindly with coherent finite-lattice inverse limits, as the first referee's compactified-fence W already demonstrated.
