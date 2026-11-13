# Project A — fixed-point localization outside compact/regular coordinate patches

**13 November 2026 — NEW INTERNAL proof, not externally audited.** This is an intrinsic bounded continuation of the Q/Q′ programme. It upgrades the previously proved *one-sided full-vs-finite fitted-diagonal rigidity* to an inequality valid at **every** fixed point of the finite-cover pre-nucleus. It gives a universal closed-core support restriction for a possible rank-one Q or Q′ hole, but does **NOT** prove either universal conjecture.

## 0. Definitions and scope

Let \(L=\mathcal O(X)\), \(Q=\mathcal O(X\times X)=L\oplus L\), and for a cover \(C\) of \(1_L\) set
\[
 w_C=\bigvee_{c\in C}c\boxtimes c,\qquad
 \Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
 \Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]
Let \(d\in Q\) be **any** \(\Phi_2\)-fixed open, \(\Phi_2(d)=d\). Hence for **each** finite cover \(F\),
\[
 (w_F\to d)\le d,
 \quad\text{i.e.}\quad
 [r\wedge w_F\le d]\Longrightarrow r\le d
 \quad(r\in Q).                                      \tag{0.1}
\]
Let \(K=\mathfrak c_X(e)\) be a **globally closed** sublocale of \(X\); then \(\mathcal O(K)=\uparrow e\), with restriction \(a\mapsto e\vee a\). An ambient open \(u\in L\) is *supported in K* here if \(u\wedge e=0\). This is stronger than merely having nonzero restriction to K.

## 1. The fixed-point one-sided localization theorem

**Theorem 1.1 (all finite-fixed opens).** Suppose \(K=\mathfrak c(e)\) is **compact or regular** as a locale. For every \(u\in L\) with \(u\wedge e=0\), every \(\Phi_2\)-fixed \(d\in Q\), and every arbitrary cover \(C\),
\[
 \boxed{(u\boxtimes1)\wedge(w_C\to d)\le d,\qquad
 (1\boxtimes u)\wedge(w_C\to d)\le d.}                 \tag{1.1}
\]
Consequently
\[
 \boxed{(u\boxtimes1)\wedge\Phi(d)\le d,\qquad
 (1\boxtimes u)\wedge\Phi(d)\le d.}                   \tag{1.2}
\]
This is a **pointwise fixed-point-sector** inequality; it does not assert \(\Phi=\Phi_2\) at arbitrary arguments.

*Proof, compact case.* By compactness of K, the cover C has a finite subfamily \(F\subseteq C\) with
\[
 e\vee\bigvee_{c\in F}c=1.
\]
Thus \(G=F\cup\{e\}\) is a finite cover of X. Put \(\rho=w_C\to d\) and \(r=\rho\wedge(u\boxtimes1)\). Since \(u\wedge e=0\),
\[
 r\wedge(e\boxtimes e)=0.
\]
For every \(c\in F\), \(r\wedge(c\boxtimes c)\le\rho\wedge w_C\le d\). Hence \(r\wedge w_G\le d\), and (0.1) implies \(r\le d\). The other-coordinate inequality is symmetric.

*Proof, regular case.* Work in the regular frame \(\mathcal O(K)=\uparrow e\). For every \(c\in C\) and every \(v\prec(e\vee c)\) in K, write \(b=v_K^*\) for the pseudocomplement of v in this frame. Since \(v\prec(e\vee c)\),
\[
 b\vee(e\vee c)=1,\qquad v\wedge b=e.
\]
Both \(v,b\) are elements of \(\uparrow e\), so \(b\ge e\) and hence \(b\vee c=1\) **in X**. Therefore \(\{b,c\}\) is a finite X-cover.

Put \(\rho=w_C\to d\) and \(r_{v,c}=\rho\wedge((u\wedge v)\boxtimes1)\). We have
\[
 r_{v,c}\wedge(b\boxtimes b)=0
 \quad\text{since }u\wedge v\wedge b=u\wedge e=0,
\]
while \(r_{v,c}\wedge(c\boxtimes c)\le\rho\wedge w_C\le d\). Thus \(r_{v,c}\wedge w_{\{b,c\}}\le d\); (0.1) gives \(r_{v,c}\le d\).

By regularity,
\[
 \bigvee_{\substack{c\in C\\v\prec(e\vee c)}}v
 =\bigvee_{c\in C}(e\vee c)=1
\]
(the last equality uses that C covers X). Meet with u, then distribute \(\boxtimes\) and meets to obtain
\[
 \rho\wedge(u\boxtimes1)
 =\bigvee_{\substack{c\in C\\v\prec(e\vee c)}}
       \rho\wedge((u\wedge v)\boxtimes1)
 \le d.
\]
Again swap factors for the second inequality. This proves (1.1); distributing over the defining join of \(\Phi(d)\) proves (1.2). □

**Adversarial check.** The regular case uses that \(b=v_K^*\) belongs to \(\uparrow e\), so \(b\vee c=1_X\), and \(v\wedge b=e\); it does **not** assume a pseudocomplement in K equals the ambient pseudocomplement in X. The finite-cover condition is invoked only because \(\Phi_2(d)=d\). No compactness of X, spatiality of X², Booleanization, or external Baire theorem is used.

## 2. A universal closed residual core for all rank-one and Q′ holes

Define the **compact/regular closed-support open** of X by
\[
 p_X=\bigvee\{u\in L:\ \exists e\in L,\ u\wedge e=0,\
       \mathfrak c(e)\text{ is compact or regular}\},
 \qquad R_X=\mathfrak c_X(p_X).                       \tag{2.1}
\]
This is a definition from the underlying locale, **independent of the chosen cover C and fixed point d**. Put \(s_X=(p_X\boxtimes1)\vee(1\boxtimes p_X)\). Joining (1.2) yields, for every finite-fixed d,
\[
 \boxed{s_X\wedge\Phi(d)=s_X\wedge d.}                \tag{2.2}
\]
In particular, for each cover C the relative open
\[
 E_{C,d}=\mathfrak c_{X^2}(d)\wedge
          \mathfrak o_{X^2}(w_C\to d)
\]
is a sublocale of
\[
 \boxed{E_{C,d}\le R_X\times R_X.}                   \tag{2.3}
\]
Indeed (1.1) says the defining open of E meets the sector \(s_X\) only inside the complementary open d. Equivalently E has zero intersection with the open sublocale \(\mathfrak o(s_X)\), and thus factors through its closed complement \(R_X\times R_X\). This is a **support restriction**, not automatic transfer of the hole to \(R_X\) or proof that this closed square is nowhere dense in \(\mathcal W_2\).

**Corollary 2.1 (global local-patch sufficient condition).** If \(p_X=1\), then **every** fixed point of \(\Phi_2\) is a fixed point of \(\Phi\). In fact the transfinite least-fixed-point closure operators \(\Phi_2^\infty\) and \(\Phi^\infty\) agree at **all arguments**: the \(\Phi_2\)-closure is already \(\Phi\)-fixed, and \(\Phi_2\le\Phi\). In particular both Q and Q′ hold on X, and \(\mathcal D_2(X)=\mathcal D(X)\). The last fitted-diagonal equality also follows by localizing the older one-sided theorem over the cover of X by such opens.

The corollary includes compact X and regular X (take e=0, K=X, u=1); it also includes locales covered by opens each lying inside some globally closed compact/regular sublocale. This is a **sufficient condition**, not claimed necessary.

**Corollary 2.2 (obligatory support of a putative counterexample).** For the rank-one Q premise \(\Phi_2(z_1)=z_1\), \(z_1=\Phi(0)=\Phi_2(0)\), any counterexample witness \(E_{C,z_1}\) is supported in \(R_X^2\). For Q′, take \(d=d_{\mathcal W_2}=\Phi_2^\infty(0)\): every canonical marked Q′ hole \(E_{C,d}\) is supported in **the same** \(R_X^2\). This does **not** imply a hole must exist there; it rules out local compact/regular patches as its location.

If a hypothetical Q′ counterexample is replaced by its independently audited **least closed coordinate support** K of the *same* marked hole, then \(p_K=0\): otherwise (2.3) would put E in the proper closed sublocale \(\mathfrak c_K(p_K)^2\), contradicting that K is its least closed common coordinate support. Thus every closed compact/regular sublocale of this normalized K has **empty ambient interior** in K. This reproduces an aspect of prior support normalization in intrinsic local terms.

## 3. Relation to earlier examples and limits

- **Arrieta compact controls:** compactness gives \(p_X=1\), as required; their \(W=W_2<U\) is no contradiction, because this theorem compares \(\Phi\) with \(\Phi_2\), not their common fixed points with U.
- **Noncompact partial-function Scott controls:** these do have \(\mathcal D_2>\mathcal D\), so Corollary 2.1 forces \(p_S\ne1\). For the normalized weak Boolean defect with individually zero-reflecting coordinate support, the old one-sided lemma in fact rules out **every nonzero** compact/regular-supported open, yielding \(p_S=0\). Recall that S consists of **nonempty** partial functions, so it has no global bottom point and is noncompact; do not accidentally substitute a Scott dcpo with a least element.
- **Cohen × Arrieta controls:** their Q′ positivity rests on N3 closed-hull and persistent-core arguments, **not** on assuming \(p_X=1\). No computation of p_X for those products is asserted here.
- **Important logical boundary:** \(R_X\) may be large, even all of X; and a closed square \(R_X^2\) can have relatively open interior in \(\mathcal W_2\), even if R_X is nowhere dense in X. Consequently (2.3) does not settle Q/Q′. The statement is rank-independent at finite **fixed** points only; it is not a theorem about arbitrary \(\Phi\)-iterates after they cease to be \(\Phi_2\)-fixed.

## 4. Decision

This sector theorem is a short, direct strengthening of the internally checked one-sided compact/regular sublocale lemma. Its value is that **one universal closed residual core** \(R_X\) catches any one-step full-cover obstruction at either the Q rank-one stage or the Q′ terminal finite stage. It gives a precise concrete property to check on future candidates. However the normalized supports we already construct are expected to have \(p=0\), so simply iterating the same support reduction is **not** a credible proof strategy.

Continue seeking a condition on relative open charts *inside* \(\mathcal W_2\) that forces full-cover density despite absence of globally closed compact/regular coordinate patches. **Q and Q′ remain OPEN.**

**Verification status: internally checked direct frame calculation; not externally refereed.**