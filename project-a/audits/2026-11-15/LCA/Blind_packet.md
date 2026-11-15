# Project A — A proposed compact sober counterexample to (LC-A)

**Independent blind mathematical packet · 15 November 2026**

**Status:** Proposed theorem and proof for independent adversarial review. No claim of publication priority or constructive validity is made. The packet is self-contained apart from elementary frame/locale theory and the usual correspondence between locally compact sober spaces and locally compact locales.

## 1. The question and the presented relation

Let \(X\) be a locale and write \(u_i=\pi_i^*u\in\mathcal O(X\times X)\), \(i=1,2\), for \(u\in\mathcal O(X)\). The **oriented specialization relation** is the sublocale

\[
\mathcal A(X)\hookrightarrow X\times X
\tag{1.1}
\]

universally presented by the frame inequalities

\[
u_1\le u_2\qquad (u\in\mathcal O(X)).
\tag{1.2}
\]

In particular, for any locale \(Z\) and map \(g=(g_1,g_2):Z\to X\times X\), the map \(g\) factors through \(\mathcal A(X)\) if and only if \(g_1^*u\le g_2^*u\) for all \(u\). On ordinary points its graph is

\[
G_{\le_X}=\{(x,y):x\le_X y\},\qquad
x\le_X y\iff(\forall u)(x\in u\Rightarrow y\in u).
\tag{1.3}
\]

Write \([G_{\le_X}]\) for the point-generated sublocale of \(X^2\), not merely the underlying set of pairs.

The positive theorem **(A-SC)**, established separately, says that \(\mathcal A(X)\) is spatial for every *stably locally compact* locale. The present question is its proposed extension:

> **Question (LC-A).** Must \(\mathcal A(X)\) be spatial for every locally compact sober space \(X\)? Equivalently, must it equal \([G_{\le_X}]\)?

Our proposed answer is **no**, even for compact sober \(T_1\) spaces. The proof does not use the positive theorem (A-SC).

## 2. Construction of the space

Let \(K=[0,1]\) with its Euclidean topology, and take a new point \(p\notin K\). Put \(X=K\sqcup\{p\}\). Declare its open sets to be:

1. the ordinary open subsets \(V\subseteq K\), with \(p\notin V\); and
2. the sets \(U_F=\{p\}\cup(K\setminus F)\), for each **finite** \(F\subseteq K\).

This is a topology. The decisive intersection formulas are

\[
U_F\cap U_G=U_{F\cup G},\qquad U_F\cap V=V\setminus F.
\tag{2.1}
\]

The latter is open in \(K\), as finite sets are closed. Arbitrary unions are also of one of the prescribed forms: a union that contains \(p\) is \(U_{\cap_i F_i}\) over the nonempty subfamily of members containing \(p\), possibly enlarged by ordinary opens of \(K\); equivalently its complement in \(K\) is a subset of a finite set, hence finite. The unions not containing \(p\) are ordinary open unions in \(K\).

The open subspace \(K\hookrightarrow X\) has precisely its original topology, and the neighborhoods of \(p\) are exactly the \(U_F\).

## 3. Compactness, local compactness, sobriety, and nonstability

**Lemma 3.1.** The space \(X\) is compact and \(T_1\).

*Proof.* Any open cover contains some \(U_F\) with \(p\in U_F\). This member covers all but the finitely many points of \(F\), so finitely many additional cover members finish the cover. Similarly every \(U_F\) is a compact open subspace: a cover of \(U_F\) contains an open member containing \(p\), which misses only finitely many points of \(U_F\). The complement of \(\{p\}\) is the open set \(K\), and the complement of \(\{x\}\), for \(x\in K\), is \(U_{\{x\}}\). Thus each singleton is closed. \(\square\)

**Lemma 3.2.** The space \(X\) is locally compact in the strong (core-compact/localic) sense, and is sober.

*Proof.* At \(p\), the \(U_F\) form a basis of compact open neighborhoods. At \(x\in K\), given a neighborhood \(W\) of \(x\) in \(X\), its trace \(W\cap K\) is an ordinary neighborhood in the locally compact Hausdorff space \(K\). Choose \(x\in V\subseteq C\subseteq W\cap K\), with \(V\) open in \(K\) and \(C\) compact in \(K\). Then \(V\) is open in \(X\) and \(C\) is compact in \(X\). Because \(X\) is \(T_1\), every subset is saturated; these compact saturated neighborhoods witness the standard localic local compactness criterion for sober spaces.

For sobriety, let \(C\neq\varnothing\) be irreducible closed in \(X\). If \(C\cap K\) contained distinct \(x,y\), disjoint Euclidean neighborhoods of \(x,y\), also open in \(X\), would give disjoint nonempty relatively open sets of \(C\), impossible for irreducibility. Thus \(|C\cap K|\le1\). If \(C\) contained both \(p\) and \(x\in K\), then necessarily \(C=\{p,x\}\); the opens \(U_{\{x\}}\cap C=\{p\}\) and \(K\cap C=\{x\}\) contradict irreducibility. Hence \(C\) is a singleton, which is the closure of its unique point because \(X\) is \(T_1\). \(\square\)

**Lemma 3.3.** The locale of \(X\) is **not** stably locally compact.

*Proof.* The two subsets \(K\) and \(U_{\{x\}}\) are compact saturated subsets of \(X\) for any \(x\in K\): \(K\) is compact as the unit interval, and \(U_{\{x\}}\) is compact by Lemma 3.1; saturation follows from \(T_1\). Their intersection is \(K\setminus\{x\}\), which is not compact if \(x\) is nonisolated: it is not closed in the compact Hausdorff subspace \(K\). In a stably locally compact sober space, finite intersections of compact saturated subsets are compact. \(\square\)

## 4. The closed-point fiber of the presented relation

For an open sublocale determined by \(u\in\mathcal O(X)\), write \(O_X(u)\). For a point sublocale \([p]\hookrightarrow X\), its **fitted hull** is

\[
\operatorname{fit}_X([p])=
\bigwedge_{p\in u}O_X(u)
=\bigwedge_{F\subseteq K\;\mathrm{finite}}O_X(U_F).
\tag{4.1}
\]

The meet is in the **sublocale lattice**, not a set-theoretic intersection of opens or the frame meet of all the \(U_F\).

**Lemma 4.1 (fiber identification).** Let \(\rho_1:\mathcal A(X)\to X\) be the first projection and \(F_p=\mathcal A(X)\times_X[p]\) its fiber. The second projection identifies \(F_p\) as a sublocale of \(X\), with

\[
F_p\cong\operatorname{fit}_X([p]).
\tag{4.2}
\]

*Proof.* A map \(z:Z\to X\) defines a map \((p!,z):Z\to\{p\}\times X\subseteq X^2\), where \(!:Z\to1\). It factors through \(\mathcal A(X)\) precisely when

\[
(p!)^*u\le z^*u\qquad\text{for all }u\in\mathcal O(X).
\tag{4.3}
\]

For \(p\notin u\), the left side is \(0\), so the condition is automatic. For \(p\in u\), the left side is \(1\), and the condition says \(z^*u=1\), exactly the condition that \(z\) factor through the open sublocale \(O_X(u)\). Imposing these conditions for all \(u\ni p\) is the universal property of (4.1). This works for arbitrary \(Z\), not just points. \(\square\)

Since \([p]\) is a **closed** sublocale of \(X\), its inverse image \(F_p\) along \(\rho_1\) is a **closed sublocale** of \(\mathcal A(X)\). We will use both the closedness and (4.2); neither assertion follows from point-set considerations alone.

## 5. The nonzero pointless piece

Let \(\beta_X\hookrightarrow X\) be the double-negation or **Booleanization** sublocale, whose frame nucleus is

\[
j_\beta(a)=\neg\neg a\qquad(a\in\mathcal O(X)).
\tag{5.1}
\]

It is nonzero: the fixed-point frame has distinct bottom and top, since \(X\neq0\) and \(\neg\neg0=0\neq1=\neg\neg1\).

**Lemma 5.1.** If \(u\) is a dense open of any locale \(Y\), then \(\beta_Y\le O_Y(u)\) in the **sublocale order**.

*Proof.* The open nucleus is \(j_u(a)=u\to a\). With \(\neg u=0\),

\[
(u\to a)\wedge\neg a\wedge u=0,
\qquad
(u\to a)\wedge\neg a\le\neg u=0;
\]

so \(u\to a\le\neg\neg a\). Since the nucleus order is opposite the sublocale-inclusion order, this gives \(\beta_Y\le O_Y(u)\). \(\square\)

**Lemma 5.2.** Both \(K\subseteq X\) and every \(U_F\subseteq X\) are dense open subspaces.

*Proof.* Every nonempty open of \(X\) intersects \(K\): an open containing \(p\) has cofinite nonempty \(K\)-part. Thus \(K\) is dense. The complement of \(U_F\) is finite, with empty interior because \(K=[0,1]\) has no isolated points. Thus each \(U_F\) is dense. \(\square\)

Combining (4.1), Lemmas 5.1 and 5.2 gives

\[
0\ne\beta_X
\ \le\ 
\operatorname{fit}_X([p])\wedge O_X(K).
\tag{5.2}
\]

On the other hand, **the right side has no points**. Any point of \(\operatorname{fit}_X([p])\) must lie in each ordinary neighborhood \(U_F\) of \(p\), and

\[
\bigcap_{F\text{ finite}}U_F=\{p\}.
\tag{5.3}
\]

No point of \(O_X(K)\) is \(p\). Consequently

\[
E:=\operatorname{fit}_X([p])\wedge O_X(K)
\tag{5.4}
\]

is a **nonzero locale with no points**, so is nonspatial.

**Proposed theorem (negative LC-A).** For the compact, locally compact, sober \(T_1\) space \(X\) of §2, the presented sublocale \(\mathcal A(X)\) is not spatial. In particular,

\[
\boxed{\mathcal A(X)\ne[G_{\le_X}]=\Delta_X.}
\tag{5.5}
\]

*Proof.* Via Lemma 4.1, \(E\) is an **open sublocale** of the **closed sublocale** \(F_p\subseteq\mathcal A(X)\). If \(\mathcal A(X)\) were spatial, its closed sublocale \(F_p\) would be spatial, and then its open sublocale \(E\) would be spatial. This contradicts (5.2)–(5.4). The argument uses the special **locally closed** position of \(E\); it does *not* assert that every sublocale of a spatial locale is spatial.

Finally \(X\) is \(T_1\), so \(x\le_Xy\) forces \(x=y\); therefore its point graph is the diagonal. The diagonal sublocale is the spatial image of \(X\) and is generated by its ordinary points, since \(X\) is spatial. Thus \([G_{\le_X}]=\Delta_X\), whereas \(\mathcal A(X)\) is nonspatial. \(\square\)

## 6. Independent nonzeroness witness from \(K\)

There is a second route to the nonzero locally closed sublocale which does not initially use \(\beta_X\).

Let \(\beta_K\) be the double-negation sublocale of the perfect Hausdorff space \(K\). Every \(K\setminus F\) is dense open in \(K\), so

\[
0\ne\beta_K\le O_K(K\setminus F)\qquad(F\subseteq K\text{ finite}).
\tag{6.1}
\]

Take \(z:\beta_K\hookrightarrow K\hookrightarrow X\). The map \((p!,z):\beta_K\to X^2\) satisfies \(u_1\le u_2\) for all opens \(u\in\mathcal O(X)\): if \(p\notin u\), the first pullback is zero, while if \(p\in u\), then \(u=U_F\) and \(z^*u=1\) by (6.1). Consequently \((p!,z)\) factors through \(\mathcal A(X)\). Its image lies in

\[
\mathcal A(X)\wedge(\{p\}\times K),
\tag{6.2}
\]

the locally closed sublocale identified with \(E\) in (5.4). As \(\beta_K\ne0\), the identity \(\beta_K\to\beta_K\) could not factor through the zero locale, so (6.2) is nonzero. It has no points by the same set-theoretic restriction as §5.

This is a useful separate check of the central nonzeroness assertion. As before, arbitrary **nonspatial** sublocales of spatial locales are possible; the contradiction comes specifically from **locally closedness**.

## 7. Scope, optional generalization, and context

The same construction is proposed for any nonempty locally compact Hausdorff \(K\) **without isolated points**, using the same cofinite neighborhoods at \(p\). The topology, compactness of \(X\), compact-open basis at \(p\), \(T_1\) property, and sobriety arguments remain valid; local compactness at points of \(K\) comes from that of \(K\). Dense open \(K\) and \(U_F\) again force the same Booleanization obstruction. To see nonstability even when \(K\) itself is not compact, choose a compact neighborhood \(C\subseteq K\) of some \(x\in K\) whose interior contains \(x\). Then \(C\) and \(U_{\{x\}}\) are compact saturated in \(X\), but \(C\cap U_{\{x\}}=C\setminus\{x\}\) is noncompact because \(x\) is nonisolated in compact Hausdorff \(C\). This extension is **optional** and should be reviewed independently of the explicit \([0,1]\) theorem.

For context: the established positive (A-SC) result covers stably locally compact locales, while open-cover, semilattice-retraction, Alexandrov, and Scott-domain tests produced nonstable locally compact spaces whose presented relation was nevertheless spatial. The proposed \(X\) therefore tests a genuinely different failure mode: the obstruction is a nonzero **pointless locally closed fiber piece** above a closed point.

The packet deliberately includes its own proof of each nonstandard step. A referee need not accept any earlier Project A claim to assess (5.5).

## 8. Audit questions in brief

- Is the precise topological space of §2 genuinely compact, sober, and locally compact in the locale-theoretic sense?
- Are the fitted-hull fiber and double-negation inclusions mathematically correct, with nucleus and sublocale orders handled consistently?
- Is \(E\) really nonzero **and** pointless, and is it locally closed in \(\mathcal A(X)\)?
- Is there an implicit assumption that a sublocale of a spatial locale is spatial? Does the proof avoid it by using an open sublocale of a closed sublocale?
- Can the main proof be shortened or generalized, and would any such changes require additional hypotheses?

Please adjudicate **every assertion** in the packet rather than only its boxed theorem.
