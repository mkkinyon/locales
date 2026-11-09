# Project A — Proper-over-regular finite-cover fitting and localized Q′ obstructions

**8 November 2026 — New internally checked working theorems, not externally refereed.** No novelty or priority claim. This arose from testing twisted/glued compact fibers as potential counterexamples to Q′: \(\mathcal W_2=\mathcal W\) for every locale? This note is **not** a resolution of Q′.

Throughout \(L=\mathcal O(X)\), \(Q=L\oplus L\), \(a\boxtimes b\) is a pure rectangle, \(w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c\) for a cover \(\mathcal C\) of \(1\), and
\[
\mathcal D=\bigcap_{\mathcal C\text{ any cover}}O(w_{\mathcal C}),\qquad
\mathcal D_2=\bigcap_{F\text{ finite cover}}O(w_F).
\]
Write \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal W_2=\operatorname{cl}\mathcal D_2=C(d_0)\). As in the earlier audited framework, \(\Phi_2(d_0)=d_0\), where \(\Phi_2(z)=\bigvee_{F\text{ finite cover}}(w_F\to z)\). A pair of frame homomorphisms \(h,k:L\to M\) factors jointly through \(\mathcal D_2\) iff
\[
\bigvee_{c\in F}\bigl(h(c)\wedge k(c)\bigr)=1_M
\]
for every finite cover \(F\). The analogous condition for all covers corresponds to factoring through \(\mathcal D\).

## 1. Elementary finite-localization lemma

**Lemma 1.** Fix a cover \(\mathcal C\) of \(1_L\). Suppose there is a cover \(1_L=\bigvee_{i\in I}e_i\) and, for each \(i\), a finite \(F_i\subseteq\mathcal C\) such that
\[
 e_i^*\vee\bigvee F_i=1_L. \tag{1}
\]
Then every finite-cover-compatible pair \(h,k:L\to M\), for an arbitrary frame \(M\), is compatible with the possibly infinite cover \(\mathcal C\).

**Proof.** The family \(\{e_i^*\}\cup F_i\) is a finite cover, hence
\[
1_M=h(e_i^*)\wedge k(e_i^*)\ \vee\
  \bigvee_{c\in F_i}h(c)\wedge k(c).
\]
Meeting with \(h(e_i)\) annihilates the first summand and yields
\[
h(e_i)\le \bigvee_{c\in\mathcal C}h(c)\wedge k(c).
\]
Joining over \(i\), the left side is \(h(1_L)=1_M\), proving the claim. \(\square\)

In particular, if (1) is available for *every* cover \(\mathcal C\), then \(\mathcal D_2=\mathcal D\). The lemma does **not** assume the \(e_i\) are complemented. Notice \(e_i^*\vee\bigvee F_i=1\) is a rather-below condition \(e_i\prec \bigvee F_i\), not the weaker assertion \(e_i\le\bigvee F_i\).

## 2. Proper regular-base theorem

**Theorem 2 (working).** Let \(f:X\to Y\) be a locale map. Assume \(M=\mathcal O(Y)\) is regular and the right adjoint \(f_*:\mathcal O(X)\to M\) of the inverse-image frame homomorphism \(f^*:M\to L\) preserves directed joins. Then
\[
\boxed{\mathcal D_2(X)=\mathcal D(X).}
\]
In particular this holds for a proper locale map \(f\) with regular codomain.

**Proof.** Fix an arbitrary cover \(\mathcal C\) of \(L\). For finite \(F\subseteq\mathcal C\) let \(c_F=\bigvee F\) and \(u_F=f_*(c_F)\). The \(c_F\) form a directed family with join \(1_L\), so
\[
\bigvee_Fu_F=f_*(\bigvee_Fc_F)=f_*(1_L)=1_M.
\]
By regularity, \(u_F=\bigvee\{v:v\prec u_F\}\). Thus all \(v\prec u_F\), for all finite \(F\), cover \(1_M\). Applying \(f^*\) shows that the elements \(e_{F,v}=f^*(v)\) cover \(1_L\).

Frame homomorphisms preserve the rather-below relation: \(v^*\vee u_F=1\) implies \(f^*(v)^*\vee f^*(u_F)=1\). By the adjunction counit,
\[
f^*(u_F)=f^*f_*(c_F)\le c_F,
\]
so \(e_{F,v}^*\vee c_F=1_L\). Apply Lemma 1. Every finite-cover-compatible pair is compatible with \(\mathcal C\), and \(\mathcal C\) was arbitrary. By the standard frame-map presentation of \(\mathcal D,\mathcal D_2\), they are equal. \(\square\)

**Corollary 3.** If \(Y\) is a regular locale and \(K\) a compact locale, then
\[
\mathcal D_2(Y\times K)=\mathcal D(Y\times K);
\quad\text{therefore }\mathcal W_2(Y\times K)=\mathcal W(Y\times K).
\]
Indeed, the localic projection \(Y\times K\to Y\) is proper. No zero-dimensionality, local compactness or spatiality assumption on the regular base is needed; \(K\) need not be Hausdorff. This strengthens the previously recorded zero-dimensional-base/compact-fiber sufficient condition and includes compact-fiber bundles whenever the projection is proper.

For instance take a nonlocally compact connected regular space such as infinite-dimensional separable Hilbert space as \(Y\), and the compact nonregular two-apex locale from the October control examples as \(K\). The conclusion still holds. It does not require a clopen patching basis on \(Y\).

## 3. A localized necessary condition on a rectangular Q′ witness

Let \(d_0=d_{\mathcal W_2}\) and fix an arbitrary cover \(\mathcal C\). Define
\[
t_{\mathcal C}=
\bigvee_{\substack{F\subseteq\mathcal C\\F\text{ finite}}}
\bigvee\{v\in L:v\prec\bigvee F\}. \tag{2}
\]

**Proposition 4 (working).** Suppose \(r=a\boxtimes b\) satisfies
\[
r\wedge w_{\mathcal C}\le d_0.
\tag{3}
\]
Then
\[
r\wedge(t_{\mathcal C}\boxtimes1)\le d_0,
\qquad
r\wedge(1\boxtimes t_{\mathcal C})\le d_0. \tag{4}
\]
Consequently, if \(r\not\le d_0\), then necessarily \(t_{\mathcal C}\ne1\). Relative to \(\mathcal W_2\), any open defect witnessed by \(r\) is confined to the product of the closed remainder \(C(t_{\mathcal C})\) with itself.

**Proof.** Fix finite \(F\subseteq\mathcal C\) and \(v\prec c_F=\bigvee F\). Then \(\{v^*\}\cup F\) is a finite cover. Put \(r_v=r\wedge(v\boxtimes1)\). We have
\[
r_v\wedge w_{\{v^*\}\cup F}
=r_v\wedge\bigvee_{c\in F}c\boxtimes c
\le r\wedge w_{\mathcal C}\le d_0.
\]
Since \(d_0\) is fixed by the finite-cover pre-nucleus, the finite-cover residual inequality gives \(r_v\le d_0\). Join over all \(F,v\) to obtain the first inequality in (4). The second follows by swapping the rectangle coordinates. If \(t_{\mathcal C}=1\), the first inequality says \(r\le d_0\), contrary to the hypothesized defect. \(\square\)

This necessary condition is distinct from the previous compact-closed and hyperconnected strip criteria: it is a *cover-dependent* rather-below localization. It makes precise why a proposed counterexample relying on a regular base with proper fibers cannot work: the regular-base theorem forces the localization to cover all of \(X\).

## 4. Research disposition

The gluing strategy of placing a compact nonregular two-apex fiber over a regular but highly noncompact base fails *regardless of twisting* whenever the projection is proper: in fact \(\mathcal D_2=\mathcal D\), not only \(\mathcal W_2=\mathcal W\). To continue a counterexample search via gluing, it is necessary to drop properness of this projection or regularity of its base (or change the strategy entirely). Merely having infinite chromatic or topological twisting is not enough.

**Q′ and Q remain open.** This is a self-contained internally checked working advance, not a resolution or a priority claim. It should not be entered in the theorem ledger as externally refereed without a separate audit.
