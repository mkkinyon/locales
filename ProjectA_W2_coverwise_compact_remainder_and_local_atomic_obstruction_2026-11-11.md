# Project A — Coverwise compact remainders and localized atomic obstruction to Q′

**11 November 2026 — NEW INTERNAL working separation-hierarchy segment, not externally audited.** Return to the original noncoherent localic hierarchy after the coherent crosscut/homotopy programme and the CO-01 fitted-pinching work. This note deliberately addresses the finite-cover questions, not an unsupported general homotopy-to-separation implication. No literature novelty claim.

## 0. Definitions, established starting facts, open questions

Let \(L=\mathcal O(X)\), \(Q=L\oplus L=\mathcal O(X^2)\). Write
\[
w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c
\]
for a cover \(\mathcal C\) of \(1_L\). Define
\[
\mathcal D=\bigwedge_{\mathcal C\ \text{cover}}\mathfrak o(w_{\mathcal C}),
\quad
\mathcal D_2=\bigwedge_{F\ \text{finite cover}}\mathfrak o(w_F),
\quad
\mathcal W=\operatorname{cl}\mathcal D,\quad
\mathcal W_2=\operatorname{cl}\mathcal D_2.
\]
Then
\[
\mathcal I\le\mathcal W\le\mathcal W_2\le\mathcal U
\]
and the implications under investigation are
\[
(Q'):\quad \mathcal W_2=\mathcal W\ \text{always?}\qquad
(Q):\quad \mathcal W_2=\mathcal U\implies\mathcal W=\mathcal U\ ?
\]
**Both are open.** It is possible that \(\mathcal D<\mathcal D_2\) but \(\mathcal W=\mathcal W_2\); known branching and Scott controls show this.

Use \(e\prec a\) to mean \(e^*\vee a=1\) (rather-below). For each cover \(\mathcal C\), define
\[
t_{\mathcal C}=
\bigvee_{\substack{F\subseteq\mathcal C\\ F\ \text{finite}}}
\bigvee\{e\in L:e\prec\bigvee F\}.
\tag{0.1}
\]
The previously established **localized residue lemma** is that if \(d_0=d_{\mathcal W_2}\) and a rectangle \(r=a\boxtimes b\) satisfies
\[
r\wedge w_{\mathcal C}\le d_0,
\tag{0.2}
\]
then
\[
r\wedge(t_{\mathcal C}\boxtimes1)\le d_0,\qquad
r\wedge(1\boxtimes t_{\mathcal C})\le d_0.
\tag{0.3}
\]
See [proper-over-regular localization](A-W2-proper-regular-base-and-localized-witness-2026-11-08.md). This statement was subsequently part of the externally corroborated Q′ packet.

Recall also the independently corroborated universal regular-core bound
\[
K=\operatorname{cl}(\operatorname{int}\mathcal U)
=C(d_{\mathcal U}^{**})
\le\mathcal W\le\mathcal W_2\le\mathcal U,
\qquad
d_{\mathcal W}\le d_{\mathcal U}^{**}.
\tag{0.4}
\]
Set \(G=\mathcal U\wedge\mathfrak o(d_{\mathcal U}^{**})\), the relative nonregular Urysohn boundary, and \(H_2=\mathcal W_2\wedge G\).

## 1. New positive theorem: coverwise compact remainder

**Lemma 1.1 (finite compatibility on rather-below patches).** Let \(h,k:L\to B\) be frame maps, where B is ANY frame, compatible with **every finite open cover** in the sense that
\[
\bigvee_{a\in F}h(a)\wedge k(a)=1_B
\tag{1.1}
\]
for every finite cover F. Fix an arbitrary cover \(\mathcal C\), and put
\[
z_{\mathcal C}=\bigvee_{a\in\mathcal C}h(a)\wedge k(a).
\]
Then
\[
\boxed{h(t_{\mathcal C})\le z_{\mathcal C},\qquad k(t_{\mathcal C})\le z_{\mathcal C}.}
\tag{1.2}
\]

*Proof.* If \(e\prec c_F=\bigvee F\) for a finite \(F\subseteq\mathcal C\), then \(\{e^*\}\cup F\) is a finite cover. Apply (1.1) and meet its right side with h(e). The first term \(h(e^*)\wedge k(e^*)\) dies because \(e\wedge e^*=0\), while all remaining terms are ≤ \(z_{\mathcal C}\). Thus \(h(e)\le z_{\mathcal C}\). Join over all F,e; symmetry gives the other inequality. □

**Theorem 1.2 (coverwise compact remainder).** If the **closed sublocale** \(\mathfrak c(t_{\mathcal C})\hookrightarrow X\) is compact, every finite-cover-compatible frame-map pair h,k is compatible with \(\mathcal C\):
\[
\boxed{\bigvee_{a\in\mathcal C}h(a)\wedge k(a)=1_B.}
\tag{1.3}
\]
In particular, if the stated compactness condition holds for **every** cover \(\mathcal C\), then
\[
\boxed{\mathcal D_2=\mathcal D,\qquad \mathcal W_2=\mathcal W.}
\tag{1.4}
\]

*Proof.* Restrict the cover \(\mathcal C\) to the compact closed locale \(\mathfrak c(t_{\mathcal C})\). Some **finite** \(F_0\subseteq\mathcal C\) covers this locale. Equivalently,
\[
\mathfrak c(t_{\mathcal C})\le \mathfrak o(c_{F_0})
\quad\Longleftrightarrow\quad
t_{\mathcal C}\vee c_{F_0}=1_L
\tag{1.5}
\]
where \(c_{F_0}=\bigvee F_0\). Hence \(\{t_{\mathcal C}\}\cup F_0\) is a finite cover. Compatibility gives
\[
1_B=h(t_{\mathcal C})\wedge k(t_{\mathcal C})
 \ \vee\ \bigvee_{a\in F_0}h(a)\wedge k(a)
\le z_{\mathcal C}
\]
by Lemma 1.1. Thus \(z_{\mathcal C}=1_B\), with no restriction on B. The factorization characterization of \(\mathcal D,\mathcal D_2\) for all frame targets gives (1.4). □

**Sharper cover-relative formulation.** The same proof requires only *some finite* \(F_0\subseteq\mathcal C\) with \(t_{\mathcal C}\vee c_{F_0}=1_L\). Compactness of \(\mathfrak c(t_{\mathcal C})\) is a sufficient condition, not necessary for a given cover. This is distinct from requiring a fixed compact remainder independent of \(\mathcal C\); the exceptional closed sublocale can vary with the cover.

**Immediate controls.**
- On a compact locale, every \(\mathcal C\) has a finite subcover, hence (1.5) holds trivially and \(\mathcal D_2=\mathcal D\), even if \(t_{\mathcal C}=0\).
- On a regular locale, rather-below approximations of finite unions cover \(X\), so \(t_{\mathcal C}=1\), its closed complement is zero, and again \(\mathcal D_2=\mathcal D\).
- The established **proper-over-regular base** theorem also has \(t_{\mathcal C}=1\) in its proof, by pulling back regular rather-below approximations.
- For the forcing/branching examples of [the synthesis](A-WU-Qprime-unified-synthesis-2026-10-24.md) and [missing-center model](A-W2-missing-center-forcing-finite-flips-2026-11-09.md), the obstructing infinite cover can have \(t_{\mathcal C}=0\) and noncompact X; these are expected failures of this sufficient criterion and do not refute Q′.

## 2. A localized *two-coordinate* necessary obstruction to Q′

For each open cover \(\mathcal C\), write
\[
J_{\mathcal C}
=
H_2\
\wedge\mathfrak c(p_1^*t_{\mathcal C})\
\wedge\mathfrak c(p_2^*t_{\mathcal C})
\quad\le X^2,
\tag{2.1}
\]
where \(p_i:X^2\to X\). This is the portion of the **actual finite-cover residual boundary** \(H_2=\mathcal W_2\wedge G\) that survives the closed remainders in *both* coordinates. It is generally **smaller than \(H_2\)** and is cover-dependent. Do not claim that it is an open sublocale of \(H_2\); it is the meet with two *closed* sublocales.

**Proposition 2.1 (two-coordinate localization).** If \(\mathcal W<\mathcal W_2\), then there exist a cover \(\mathcal C\) without a finite subcover and a nonzero **relatively open** sublocale
\[
E=\mathcal W_2\wedge\mathfrak o(r)
\tag{2.2}
\]
for some disjoint rectangle \(r=a\boxtimes b\) with \(a\wedge b=0\), such that
\[
\boxed{0<E\le J_{\mathcal C},\quad
\mathcal D\wedge E=0,\quad
\mathcal D_2\wedge E\text{ is dense in }E.}
\tag{2.3}
\]
In particular \(E=J_{\mathcal C}\wedge\mathfrak o(r)\) is **open in \(J_{\mathcal C}\)**.

*Proof.* The externally corroborated disjoint-rectangle Q′ certificate gives a cover \(\mathcal C\) without finite subcover and a rectangle \(r\le(w_{\mathcal C}\to d_0)\wedge d_{\mathcal U}^{**}\) with \(r\not\le d_0\), \(a\wedge b=0\), and \(r\wedge w_{\mathcal C}\le d_0\). Then \(E=\mathcal W_2\wedge\mathfrak o(r)\ne0\), and since \(r\le d_{\mathcal U}^{**}\) and \(\mathcal W_2\le\mathcal U\), \(E\le H_2\). By (0.3),
\[
E\wedge\mathfrak o(p_i^*t_{\mathcal C})=0
\quad(i=1,2),
\]
so \(E\le\mathfrak c(p_i^*t_{\mathcal C})\). Thus \(E\le J_{\mathcal C}\). Because \(E=\mathcal W_2\wedge\mathfrak o(r)\), this is precisely the relative open \(J_{\mathcal C}\wedge\mathfrak o(r)\).

Since \(\mathcal D\le\mathfrak o(w_{\mathcal C})\wedge\mathcal W_2\) and \(r\wedge w_{\mathcal C}\le d_0\), \(\mathcal D\wedge E=0\). Since \(\mathcal D_2\) is dense in its closure \(\mathcal W_2\), restriction to the nonzero open E is dense. □

**Corollary 2.2 (cover-local atomic test).** If, for *every* cover \(\mathcal C\), the Booleanization \(B(J_{\mathcal C})\) is an **atomic complete Boolean locale** (allow \(J_{\mathcal C}=0\)), then
\[
\boxed{\mathcal W=\mathcal W_2.}
\tag{2.4}
\]

*Proof.* If not, let E be as in Proposition 2.1. Since E is nonzero and **open in \(J_{\mathcal C}\)**, atomicity of \(B(J_{\mathcal C})\) implies \(B(E)\) has an atom and hence an ordinary locale point. Density of \(\mathcal D_2\wedge E\) in E implies \(B(E)\le \mathcal D_2\wedge E\). Thus E contains a point of \(\mathcal D_2\). But the previously established all-locale point identity
\[
\operatorname{pt}(\mathcal D_2)=\operatorname{pt}(\mathcal D)
\]
implies this point belongs to \(\mathcal D\), contradiction to \(\mathcal D\wedge E=0\). □

**Warning on comparison with older atomic tests.** The earlier theorem assumes atomic \(B(H_2)\), whereas this criterion assumes atomic \(B(J_{\mathcal C})\) for every cover. Neither hypothesis is asserted to imply the other: \(J_{\mathcal C}\) need not be open in \(H_2\), and a closed nowhere-dense sublocale of a space with dense isolated points can have atomless Booleanization. What is new and unambiguous is the stronger *necessary localization* of an actual counterexample to the cover-dependent two-coordinate remainder.

**Sharper failure criterion.** A Q′ counterexample supplies a cover \(\mathcal C\) with:
1. \(\mathfrak c(t_{\mathcal C})\) noncompact by Theorem 1.2 (or at least the absence of finite \(F\) with \(t_{\mathcal C}\vee c_F=1\));
2. \(J_{\mathcal C}\ne0\) and an open \(E\subseteq J_{\mathcal C}\) with **atomless Booleanization**;
3. \(\mathcal D_2\) dense but \(\mathcal D\) zero on E, so a genuinely pointless discrepancy; and
4. a disjoint coordinate rectangle detecting the defect.

These conditions are necessary, not sufficient. They separate **compactness obstruction**, **nonregular Urysohn boundary**, and **pointless finite-cover defect** within *one and the same* cover.

## 3. Research disposition

The coverwise compact-remainder result is an elementary positive theorem for \(\mathcal D_2=\mathcal D\). The cover-local atomic test refines the exact obstruction to the weaker \(\mathcal W_2=\mathcal W\) without pretending to solve it. In this form it also clarifies why constructing independent pathologies in separate factors has consistently failed: a single cover must create a noncompact two-coordinate remainder **inside** the finite-cover nonregular Urysohn boundary.

The next test should be narrowly chosen: determine whether, for a broad *intrinsic* class of locales (e.g. one locally countably based but not proper over a regular locale), \(J_{\mathcal C}\) is automatically zero or has atomic Booleanization for all \(\mathcal C\). Do **not** assume second countability alone enforces this—the missing-center forcing models already furnish second-countable noncompact boundaries with a finite-cover defect and an atomless Boolean residual yet \(\mathcal W=\mathcal W_2\).

**Status:** Internal working proof, not independently audited. No resolution of Q/Q′ and no claim of literature novelty.
