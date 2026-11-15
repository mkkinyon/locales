# Project A — (LC-PT): closed-point excision and scattered-remainder reduction

**Research segment · 15 November 2026. Internally checked, NOT independently audited.** This begins the post-(LC-A) question: for locally compact sober T1 spaces, does **point-fitted** imply **totally unordered**? The results below hold without local compactness. They do not settle the unrestricted question.

## 1. Conventions

For any locale X let \(\mathcal A(X)\hookrightarrow X^2\) be universally presented by \(u_1\le u_2\) for all \(u\in\mathcal O(X)\). Then X is totally unordered (TU) iff \(\mathcal A(X)=\Delta_X\). A point \(p:1\to X\) is **fitted** if its one-point sublocale \([p]\) equals \(\operatorname{fit}_X([p])\).

For every p, the first-projection fiber of \(\mathcal A(X)\) at p is \(\operatorname{fit}_X([p])\), as a sublocale of X via the second projection. In particular,
\[
X\text{ TU}\quad\Rightarrow\quad
[p]=\operatorname{fit}_X([p])\quad\text{for every p}.
\]
This is the fiber version of Arrieta's published TU ⇒ (pt-fit).

TU is inherited by open sublocales: composing any two comparable maps into an open U with U↪X preserves their comparison, and the inclusion is monic.

## 2. Open/closed decomposition of the oriented relation

Let \(F=C_X(u)\) be an arbitrary closed sublocale and \(U=O_X(u)\) its complementary open. On \(\mathcal A(X)\) the inequality \(u_1\le u_2\) implies the open part cut out by \(u_1\) is the same as the part cut out by \(u_1\wedge u_2\). Restricting the universal presentation to \(U^2\) yields \(\mathcal A(U)\).

The open and closed complements of any locale jointly generate it. Applied to the first projection \(\rho_1:\mathcal A(X)\to X\), this gives the exact decomposition **in the lattice of sublocales of X²**:
\[
\boxed{
\mathcal A(X)=
i_{U^2!}\mathcal A(U)\ \vee\
\bigl(\mathcal A(X)\times_{X,\rho_1}F\bigr).
}\tag{2.1}
\]
Here \(i_{U^2!}\) denotes the inclusion of the sublocale from \(U^2\) into \(X^2\); no direct image along a general map is intended.

For a **closed point** \(p\), \(F=[p]\) and the fiber lemma specializes (2.1) to
\[
\boxed{
\mathcal A(X)=
\mathcal A(X\setminus\{p\})
\ \vee\ ([p]\times\operatorname{fit}_X([p])).
}\tag{2.2}
\]
The diagonal has the corresponding decomposition
\[
\Delta_X=\Delta_{X\setminus\{p\}}\vee([p]\times[p]).\tag{2.3}
\]

**One-point excision theorem.** If p is a closed point, then
\[
\boxed{X\text{ TU}\iff X\setminus\{p\}\text{ TU and }[p]\text{ fitted in }X.}\tag{2.4}
\]
The forward implication follows from inheritance and the fiber lemma; conversely, (2.2)–(2.3) show equality with \(\Delta_X\).

**Local fitting observation.** If V⊆X is open and contains p, then \(\operatorname{fit}_X([p])\le O_X(V)\), and its restriction to V is \(\operatorname{fit}_V([p])\). Thus a point fitted in one open neighborhood is fitted in X. In particular, a regular/Hausdorff locale neighborhood gives fittedness at p.

## 3. Maps into scattered spaces have constant open pieces

A topological space F is **scattered** if every nonempty subspace has an isolated point. Write \(F^{(0)}=F\), \(F^{(\alpha+1)}=F^{(\alpha)}\setminus\operatorname{Iso}(F^{(\alpha)})\), and \(F^{(\lambda)}=\bigcap_{\alpha<\lambda}F^{(\alpha)}\) for limit ordinals. Each derivative is closed in F; for scattered F, some derivative is empty.

**Lemma (constant-open-piece lemma).** Let F be a scattered sober space and \(f:Z\to F\) a locale map with \(Z\ne0\). Then some nonzero **open sublocale** \(V\hookrightarrow Z\) has constant composite \(f|_V=p!\) for an ordinary point \(p\in F\).

*Proof.* Suppose no such V exists. The set \(I_\alpha=\operatorname{Iso}(F^{(\alpha)})\) is open and discrete in \(F^{(\alpha)}\), a union of relatively open singletons. If f factors through \(F^{(\alpha)}\), then each inverse image of a singleton \(\{p\}\subseteq I_\alpha\) must be zero: otherwise it is a nonzero open V where f is p-constant. Their join (the inverse image of \(I_\alpha\)) is zero, so f factors through the closed complement \(F^{(\alpha+1)}\). At a limit stage, factoring through all earlier closed derivatives implies factoring through their closed intersection \(F^{(\lambda)}\). Transfinite induction would force f to factor through the empty derivative, contradicting \(Z\ne0\). \(\square\)

No ordinary point of Z is required; the argument works for nonspatial Z.

## 4. Scattered closed-remainder theorem

**Theorem (LC-PT partial positive result).** Let X be a locale with an open sublocale U whose closed complement F is **spatial and scattered**. Suppose U is TU and every ordinary point \(p\in F\) is fitted **as a point of X**. Then X is TU.

*Proof.* Suppose not. Choose comparable distinct maps \(f\le g:Z\to X\). Some open a satisfies \(f^*a<g^*a\). Restrict Z to the locally closed sublocale
\[
Z'=O_Z(g^*a)\wedge C_Z(f^*a).
\]
It is nonzero, because \(g^*a\not\le f^*a\); on it \(f^*a=0\), \(g^*a=1\), and the comparison persists. In particular, **no nonzero further restriction can make f and g equal**.

Let \(u\) represent U. On the open part \(O_{Z'}(f^*u)\), the inequality \(f^*u\le g^*u\) forces both f and g to take values in U, where TU(U) makes them equal. Thus this open part must be zero, and f factors through the closed complement F.

Apply the constant-open-piece lemma to \(f:Z'\to F\). There is a nonzero open \(V\subseteq Z'\) on which \(f=p!\) for a point p of F. Then \(f\le g\) on V, and fittedness of p in X (the first-projection fiber lemma) forces \(g=p!\) on V. This contradicts the normalization \(f^*a=0\), \(g^*a=1\) on every nonzero sublocale of Z'. Therefore X is TU. \(\square\)

**Corollary.** The same conclusion holds for a **closed discrete** remainder F (finite or infinite), with a shorter proof: the first-projection fiber over each p is [p], and the open singleton fibers cover the closed part of \(\mathcal A(X)\). The one-point theorem is the case F=[p].

**Scope warning:** the general closed F need not be scattered. Ordinary point fibers may then fail to detect a nonzero pointless piece of the closed part. This is the remaining obstruction to the full LC-PT question.

## 5. Concrete calibration

- **Cofinite-point extension** \(X=K\sqcup\{p\}\) of the negative (LC-A) theorem: U=K is Hausdorff/TU, F=[p] is closed discrete. Theorem (2.4) says X TU iff [p] fitted; for K=[0,1] the fitted hull has a nonzero pointless component, so neither property holds. This exactly localizes the failure.
- **Dense-rational-bridge space** from the separately audited Q/Q′ counterexample: U=S∪T consists of two open regular real-line charts, hence TU; F=H=\(\{b_q:q\in\mathbb Q\}\) is a closed discrete subspace, and each b_q has an open regular real-line chart, hence is fitted in X. The closed-discrete corollary therefore gives TU(X), consistently with its previously established stronger identity \(\mathcal D(X)=\Delta_X\). This is a new alternate explanation, not a re-audit of Q/Q′.
- **Line with two origins** (where formulated as a sober T1 space): it is locally Hausdorff, so an open TU cover already yields TU; non-Hausdorffness alone is not a negative LC-PT mechanism.

## 6. Next tests and audit boundary

The **full (LC-PT)** remains open:
\[
\text{locally compact + sober + T1 + all point sublocales fitted}
\stackrel?{\Longrightarrow}
\text{TU}.
\]

The scattered-closed-remainder reduction says that a counterexample possessing a TU open part must have a **non-scattered closed remainder**; a finite/countable *discrete* singular locus is insufficient. Candidate strategies:

1. Examine a non-scattered perfect closed singular locus supporting generalized comparable pairs with neither coordinate constant on any nonzero open sublocale.
2. Test whether local compactness plus pt-fit forces a TU open cover on suitable strata, or provides a descent theorem beyond scattered remainders.
3. Separate a genuine **Boolean-locale** witness from ordinary points: if \(f^*a<g^*a\), the locally closed normalization above gives a nonzero domain with \(f^*a=0\), \(g^*a=1\), and its Booleanization is nonzero. This is a finite-variable counterexample target.

**References/provenance:** Arrieta, *Localic separation and the duality between closedness and fittedness*, Definition 3.8 and Proposition 3.10 ([arXiv:2310.18522](https://arxiv.org/abs/2310.18522)); Suarez, *Revisiting the relation between subspaces and sublocales* ([arXiv:2010.05284](https://arxiv.org/abs/2010.05284)) for scattered/total-spatial background (not required for the elementary transfinite lemma); [LC-A canonical](ProjectA_LCA_COUNTEREXAMPLE_CANONICAL_2026-11-15.md); [Q/Q′ bridge](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md).

**Status:** all new results are **internal research**, not independent external audit, and no novelty claim.
