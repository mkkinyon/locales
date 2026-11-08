# Project A — The unrestricted Scott-continuity converse: canonical corrected proof

**8 November 2026 · Canonical theorem note · Status E (independent external verification, with incorporated correction).**

**Purpose.** This is the consolidated reference proof of Theorem \(L^*\) and its universal-family lemma, replacing the *working proof* for mathematical use while preserving both historical referee reports and the blind-audit packet unaltered. The proof was proposed by the first Scott-continuity referee; a different independent blind referee reconstructed it and found one false assertion concerning principal downsets in the coverage presentation. **That assertion and its dependent nucleus calculation have been replaced below, not merely annotated.** The two nested inductions in the closure lemma are retained in full. No novelty or priority claim is made.

## The theorem and conventions

All locales and frames are arbitrary. For a locale map \(f:Z\to Y\), write \(f^*:\mathcal O(Y)\to\mathcal O(Z)\) and \(f_*\) for its right adjoint. **Directed** always means **nonempty (inhabited) and upward directed**.

A map \(f\) is **proper** in Vermeulen's sense if

1. \(f_*\) preserves nonempty directed joins; and
2. \(f_*(v\vee f^*w)=f_*(v)\vee w\) for all \(v\in\mathcal O(Z), w\in\mathcal O(Y)\) (**closed Frobenius**).

For \(a\in\mathcal O(Z)\), \(\mathfrak c(a)\) and \(\mathfrak o(a)\) denote the closed and open complementary sublocales. The frame of \(\mathfrak c(a)\) is \(\uparrow a\), and its quotient map is \(z\mapsto z\vee a\). Closed sublocale inclusions are proper, composites of proper maps are proper, and proper maps are stable under arbitrary pullback. The last property is the one non-elementary *published* proper-map input; see the references.

**Theorem \(L^*\) (unrestricted Scott-continuity converse).** Let \(X,Y\) be locales and let \(E\hookrightarrow X\times Y\) be a **closed** sublocale, with projections \(p_1:E\to X\), \(p_2:E\to Y\). Put

\[
 r_E=(p_2)_*p_1^*:\mathcal O(X)\longrightarrow\mathcal O(Y).
\]

Then

\[
\boxed{\quad r_E\text{ preserves nonempty directed joins}\quad\Longleftrightarrow\quad p_2\text{ is proper.}\quad}
\]

There are **no** continuity, coherence, spatiality, compactness, sobriety, separation, symmetry, or transitivity assumptions.

The proof uses a self-contained construction of a proper universal family over the **upper powerlocale**.

## 1. Preliminary frame and sublocale facts

### 1.1. The upper powerlocale

Fix \(L=\mathcal O(X)\) and let \(W=P_UX\). Its frame is presented by elements \(\Box u\), \(u\in L\), subject to

\[
 \Box1=1,\qquad \Box(u\wedge v)=\Box u\wedge\Box v,\qquad
 \Box\Bigl(\bigvee_i^{\uparrow}u_i\Bigr)=\bigvee_i^{\uparrow}\Box u_i.
 \tag{1.1}
\]

Thus frame homomorphisms \(\mathcal O(W)\to M\) correspond to **preframe homomorphisms** \(L\to M\): maps preserving finite meets, including top, and nonempty directed joins. Every element of \(\mathcal O(W)\) is a join of generators \(\Box u\), because finite meets of generators are again generators. **We do not assume that \(\Box\) preserves arbitrary or binary joins.**

Use the rectangle notation

\[
 s\boxtimes C=\pi_1^*s\wedge\pi_2^*C
 \in\mathcal O(X\times W),\qquad s\in L,\ C\in\mathcal O(W).
\]

The product frame is the frame coproduct \(\mathcal O(X)\oplus\mathcal O(W)\).

### 1.2. A closed-form sublocale for an inequality

For \(s,t\in\mathcal O(Z)\), set

\[
 [s\le t]\;:=\;\mathfrak c(s)\vee\mathfrak o(t)\quad\text{(a sublocale of \(Z\)).}
 \tag{1.2}
\]

It is the **largest** sublocale \(S\hookrightarrow Z\) on which \(i_S^*s\le i_S^*t\). Indeed, using the complementarity of \(\mathfrak c(s)\), \(\mathfrak o(s)\) and distributivity of the sublocale coframe, the inequality is equivalent to
\(S\cap\mathfrak o(s)\subseteq\mathfrak o(t)\), which is equivalent to \(S\subseteq\mathfrak c(s)\vee\mathfrak o(t)\).
Consequently, for any locale map \(g:T\to Z\),

\[
 g\text{ factors through }[s\le t]
 \iff g^*s\le g^*t,\qquad
 g^{-1}[s\le t]=[g^*s\le g^*t].
 \tag{1.3}
\]

Arbitrary intersections of sublocales have the expected factorization property; their inverse images are the intersections of the inverse images.

### 1.3. Descending Scott continuity through a quotient

Let \(q:H\twoheadrightarrow M\) be a surjective frame homomorphism, with right adjoint \(q_*\) and nucleus \(j=q_*q\). If \(\Phi:M\to N\) is monotone and \(\Phi q\) preserves nonempty directed joins, then \(\Phi\) does too.

To see this, for each member \(x_i\) of a directed family in \(M\), take its **canonical largest lift** \(e_i=q_*x_i\in H\). The family \((e_i)\) is directed (\(q_*\) is monotone), \(q(e_i)=x_i\), and
\(q(\bigvee_i e_i)=\bigvee_i x_i\). Hence

\[
\Phi\bigl(\bigvee_i x_i\bigr)
 =\Phi q\bigl(\bigvee_i e_i\bigr)
 =\bigvee_i\Phi q(e_i)=\bigvee_i\Phi(x_i).
\tag{1.4}
\]

This uses no choice. It will let us prove Scott continuity on the ambient product frame and pass to the universal sublocale.

### 1.4. Two elementary proper-map stability facts

For the closed inclusion \(i:\mathfrak c(a)\hookrightarrow Z\), the frame of its domain is \(\uparrow a\). The right adjoint \(i_*\) is the inclusion \(\uparrow a\hookrightarrow\mathcal O(Z)\): it preserves **nonempty** directed joins, since these are computed as in \(\mathcal O(Z)\). The empty join is deliberately excluded: the bottom of \(\uparrow a\) is \(a\), not necessarily \(0\). For \(x\ge a\),

\[
 i_*(x\vee i^*w)=i_*(x\vee(a\vee w))=x\vee w=i_*x\vee w.
\]

Hence closed inclusions are proper. For composable proper maps \(Z\xrightarrow{f}Y\xrightarrow{g}T\), the right adjoint of \(gf\) is \(g_*f_*\), which preserves nonempty directed joins, and

\[
 (gf)_*(v\vee f^*g^*w)
 =g_*\bigl(f_*v\vee g^*w\bigr)
 =g_*f_*v\vee w.
\]

Thus proper maps compose. **We invoke, rather than reprove, the published theorem that proper maps are stable under pullback.**

## 2. The mixed coverage-ideal presentation — with the referee's correction

Johnstone's coverage theorem and the frame-coproduct presentation give \(\mathcal O(X\times W)\) as the frame of subsets \(e\subseteq L\times L\) satisfying these three rules:

- **(D)** downward closure for the componentwise order;
- **(C1)** if \((s_i,v)\in e\) for every \(i\) in **any** index set (including the empty set), then \((\bigvee_i s_i,v)\in e\);
- **(C2)** if \((v_i)\) is nonempty directed and \((s,v_i)\in e\) for all \(i\), then \((s,\bigvee_i v_i)\in e\).

Call these subsets **coverage ideals**, or **\(\mathsf C\)-ideals**. They form a frame ordered by inclusion; meets are intersections and joins are obtained by taking the \(\mathsf C\)-ideal generated by the union.

The underlying coverage is meet-stable: meeting an arbitrary first-coordinate join cover with \((b_1,b_2)\) distributes \(b_1\) over the join; meeting a directed second-coordinate cover distributes \(b_2\) over that directed join. Thus the coverage theorem applies.

Write \(\langle s,v\rangle_{\mathsf C}\) for the **\(\mathsf C\)-ideal generated by** the pair \((s,v)\), or equivalently by the ordinary downset \(\downarrow(s,v)\). The rectangle \(s\boxtimes\Box v\) represents \(\langle s,v\rangle_{\mathsf C}\). The fundamental membership criterion is

\[
 \boxed{\quad s\boxtimes\Box v\le e\quad\Longleftrightarrow\quad(s,v)\in e.\quad}
 \tag{2.1}
\]

**Essential correction.** One must **not** identify \(\langle s,v\rangle_{\mathsf C}\) with the ordinary principal downset \(\downarrow(s,v)\). Rule (C1) for the empty family forces \((0,w)\in e\) for **every** \(w\in L\), whereas \(\downarrow(s,v)\) omits \((0,w)\) when \(w\nleq v\). Thus \(\downarrow(s,v)\) is generally not a \(\mathsf C\)-ideal. The special downset

\[
 \downarrow(s,1)=\{(a,v):a\le s\}
 \tag{2.2}
\]

*is* a \(\mathsf C\)-ideal and represents \(s\boxtimes1\). Ordinary downsets like \(\downarrow(1,d)\) may safely be used as **generating subsets**, not as frame elements. This correction is incorporated in every calculation below.

For a \(\mathsf C\)-ideal \(e\), set

\[
 e_v=\{s:(s,v)\in e\},\qquad \sigma_e(v)=\bigvee e_v.
\]

By (C1), \(e_v=\downarrow\sigma_e(v)\). By (D) and (C2), \(\sigma_e:L\to L\) is antitone and satisfies

\[
 \sigma_e\bigl(\bigvee_i^\uparrow v_i\bigr)
 =\bigwedge_i\sigma_e(v_i).
 \tag{2.3}
\]

Conversely any such \(\sigma\) determines a \(\mathsf C\)-ideal
\(e=\{(s,v):s\le\sigma(v)\}\). Hence

\[
 \mathcal O(X\times P_UX)
 \cong \{\sigma:L\to L^{\mathrm{op}}:\sigma\text{ preserves nonempty directed joins}\}
 \tag{2.4}
\]

as ordered sets, with order on \(\sigma\)'s pointwise in \(L\). Crucially, \((u,u)\in e\iff u\le\sigma_e(u)\).

## 3. The universal family and its nucleus

Define \(K\hookrightarrow X\times W\) by

\[
 K=\bigcap_{u\in L}[\;1\boxtimes\Box u\ \le\ u\boxtimes1\;].
 \tag{3.1}
\]

Thus \(K\) is the largest sublocale satisfying
\(i_K^*(1\boxtimes\Box u)\le i_K^*(u\boxtimes1)\) for all \(u\). Let \(j_K\) be its nucleus and let
\(\pi_K=\pi_2i_K:K\to W\).

**Lemma 3.1 (nucleus formula).** For every \(\mathsf C\)-ideal \(e\),

\[
 \boxed{\quad j_K(e)=e^K
 :=\{(s,v):(s\wedge v,v)\in e\}.\quad}
 \tag{3.2}
\]

Equivalently, \(\sigma_{j_K(e)}(v)=v\to\sigma_e(v)\), where \(\to\) is Heyting implication in \(L\).

*Proof.* Put \(k(e)=e^K\).

**(i) \(k(e)\) is a \(\mathsf C\)-ideal.** Downward closure is immediate. For (C1), if \((s_i\wedge v,v)\in e\) for all \(i\), then
\(((\bigvee_i s_i)\wedge v,v)=(\bigvee_i(s_i\wedge v),v)\in e\).
For (C2), suppose \((s,v_i)\in k(e)\) for all members of a nonempty directed family, and set \(v=\bigvee_i v_i\). Given \(i,j\), choose \(k\ge i,j\). Since
\((s\wedge v_i,v_j)\le(s\wedge v_k,v_k)\in e\), we have
\((s\wedge v_i,v_j)\in e\) for all \(i,j\). Applying (C2) in \(j\) yields \((s\wedge v_i,v)\in e\), and then (C1) in \(i\) yields \((s\wedge v,v)\in e\). Thus \((s,v)\in k(e)\).

**(ii) \(k\) is a nucleus.** It is monotone, inflationary by downward closure, idempotent because \(v\wedge v=v\), and preserves binary meets because those of \(\mathsf C\)-ideals are intersections.

**(iii) The sublocale \(S_k\) of \(k\) satisfies the inequalities defining \(K\).** This is the step repaired after the blind audit. Since \(\downarrow(u,1)\) really is a \(\mathsf C\)-ideal, (3.2) gives

\[
 k(u\boxtimes1)=k(\downarrow(u,1))
  =\{(s,v):s\wedge v\le u\}.
\]

As \(k\) is a nucleus, and by the **generator-membership criterion (2.1)**,

\[
\begin{aligned}
 k(1\boxtimes\Box u)\le k(u\boxtimes1)
 &\iff 1\boxtimes\Box u\le k(u\boxtimes1)\\
 &\iff (1,u)\in k(u\boxtimes1)\\
 &\iff 1\wedge u\le u,
\end{aligned}
\]

which holds. **No expression \(k(\downarrow(1,u))\) is used:** that would apply \(k\) to a set that need not be a frame element. Hence \(S_k\subseteq K\), and \(j_K\le k\) in the nucleus order.

**(iv) Conversely \(k\le j_K\).** Suppose \((s,v)\in k(e)\); then \((s\wedge v,v)\in e\). On \(K\), by (3.1),

\[
\begin{aligned}
 i_K^*(s\boxtimes\Box v)
 &=i_K^*(s\boxtimes1)\wedge i_K^*(1\boxtimes\Box v)\\
 &\le i_K^*(s\boxtimes1)\wedge i_K^*(v\boxtimes1)
             \wedge i_K^*(1\boxtimes\Box v)\\
 &=i_K^*((s\wedge v)\boxtimes\Box v)
 \le i_K^*e.
\end{aligned}
\]

Every \(\mathsf C\)-ideal is the join of the generators corresponding to its elements, so \(i_K^*k(e)\le i_K^*e\). By adjunction \(k(e)\le i_{K*}i_K^*e=j_K(e)\). Combining (iii)–(iv) proves (3.2). The implication formula follows from
\(s\wedge v\le\sigma_e(v)\iff s\le v\to\sigma_e(v)\). \(\square\)

**Corollary 3.2 (right-adjoint formula).** For \(e\in\mathcal O(X\times W)\),

\[
 \boxed{\quad
 (\pi_K)_*(i_K^*e)=\Psi(e)
 :=\bigvee\{\Box u:(u,u)\in e\}
 =\bigvee\{\Box u:u\le\sigma_e(u)\}.
 \quad}\tag{3.3}
\]

*Proof.* By adjunction and the nucleus formula,

\[
\begin{aligned}
 i_K^*(1\boxtimes\Box u)\le i_K^*e
 &\iff 1\boxtimes\Box u\le j_K(e)\\
 &\iff (1,u)\in e^K\\
 &\iff (u,u)\in e.
\end{aligned}
\]

Every open of \(W\) is a join of generators \(\Box u\). The right adjoint is therefore the join of exactly those generators satisfying this inequality. \(\square\)

## 4. Closure lemma: why directed joins suffice

For a subset \(G\subseteq L\times L\), write \(\langle G\rangle_{\mathsf C}\) for the least \(\mathsf C\)-ideal containing it. **Do not confuse this with topological closure or the closed-sublocale operator.**

**Lemma 4.1 (closure lemma).** Let \(G\subseteq L\times L\) be a downset closed under **arbitrary joins in its first coordinate** (so \((0,v)\in G\) for every \(v\)). Let \(V\in\mathcal O(W)\), and suppose

\[
 (s,v)\in G\quad\Longrightarrow\quad\Box(s\wedge v)\le V.
 \tag{4.1}
\]

Then (4.1) holds for all \((s,v)\in\langle G\rangle_{\mathsf C}\). In particular,

\[
 \Psi(\langle G\rangle_{\mathsf C})\le V.
 \tag{4.2}
\]

*Proof.* Let \(C^\infty\) be the least subset containing \(G\) and closed under:

- **(down)** componentwise downward closure;
- **(2-dir)** inhabited directed joins in the second coordinate;
- **(1-dir)** inhabited directed joins in the first coordinate.

The property \(P(s,v):\Box(s\wedge v)\le V\) holds on \(G\) and is preserved under all three rules. For (2-dir), this uses
\(\Box(s\wedge\bigvee_i^\uparrow v_i)=\bigvee_i^\uparrow\Box(s\wedge v_i)\); for (1-dir) it uses
\(\Box((\bigvee_i^\uparrow s_i)\wedge v)=\bigvee_i^\uparrow\Box(s_i\wedge v)\). **Every use of the \(\Box\)-join law is on a directed family.** Therefore \(P\) holds throughout \(C^\infty\).

It remains to show that \(C^\infty\) is already closed under **all**, not only directed, first-coordinate joins. The important step is closure under binary joins; we include both required inductions.

**First induction.** Let \(B''\) consist of those \((s',v)\in C^\infty\) for which

\[
 \forall v'\le v\;\forall(s,v')\in G:
       (s\vee s',v')\in C^\infty.
 \tag{4.3}
\]

Then \(B''\) contains \(G\), since \(G\) is a downset and is closed under first-coordinate joins. It is closed under (down): if \((s'',v'')\le(s',v)\in B''\) and \(v'\le v''\), then \((s\vee s',v')\in C^\infty\), so \((s\vee s'',v')\in C^\infty\). It is closed under (2-dir): if \((s',v_i)\in B''\), \(v'\le\bigvee_i v_i\), and \((s,v')\in G\), then
\((s,v'\wedge v_i)\in G\) and \(v'\wedge v_i\le v_i\). Hence
\((s\vee s',v'\wedge v_i)\in C^\infty\) for all \(i\); the directed family \((v'\wedge v_i)\) joins to \(v'\), yielding \((s\vee s',v')\in C^\infty\). It is closed under (1-dir): the joins of the directed family \((s\vee s'_i,v')\) give \((s\vee\bigvee_i s'_i,v')\). Thus \(B''\) is closed under all generating rules, so

\[
 B''=C^\infty.
 \tag{4.4}
\]

**Second induction.** Let \(B\) consist of those \((s,v)\in C^\infty\) for which

\[
 \forall v'\le v\;\forall(s',v')\in C^\infty:
       (s\vee s',v')\in C^\infty.
 \tag{4.5}
\]

For \((s,v)\in G\), the required pair \((s,v')\) belongs to \(G\); using (4.4) for \((s',v')\in C^\infty\) proves \((s\vee s',v')\in C^\infty\). So \(G\subseteq B\). The same verification as above, with \(G\) replaced by \(C^\infty\), proves closure of \(B\) under (down), (2-dir), and (1-dir): in the second-coordinate step replace \(v'\) by \(v'\wedge v_i\) and use downclosure of \(C^\infty\); in the first-coordinate step take directed joins of the \((s_i\vee s',v')\). Therefore

\[
 B=C^\infty.
 \tag{4.6}
\]

Taking \(v'=v\) in (4.5) gives
\((s,v),(s',v)\in C^\infty\Rightarrow(s\vee s',v)\in C^\infty\): **binary first-coordinate joins hold**. Since \((0,v)\in G\), empty and finite joins hold too. Any arbitrary join is the inhabited directed join of its finite subjoins (including the empty finite subjoin), so (1-dir) now gives closure under arbitrary first-coordinate joins.

Thus \(C^\infty\) satisfies (D), (C1), (C2), i.e. it is a \(\mathsf C\)-ideal containing \(G\); conversely every such ideal is closed under the three generating rules. Hence
\(C^\infty=\langle G\rangle_{\mathsf C}\), and \(P\) holds there. If \((u,u)\in\langle G\rangle_{\mathsf C}\), we obtain \(\Box u\le V\), proving (4.2) using (3.3). \(\square\)

**Why this lemma is indispensable.** It would be invalid simply to close \(G\) under arbitrary first-coordinate joins while tracking \(\Box(s\wedge v)\le V\): \(\Box\) does **not** preserve such joins. The two inductions establish that first-coordinate binary joins do not have to be reapplied after directed closure, so the predicate can be propagated using only the permitted directed-join law.

## 5. Properness of the universal family

**Theorem K.** For every locale \(X\), the projection

\[
 \boxed{\quad\pi_K:K\longrightarrow P_UX\quad\text{is proper.}\quad}
 \tag{5.1}
\]

*Proof.* By Corollary 3.2 and the quotient descent fact (1.4), it suffices to prove for \(\Psi:\mathcal O(X\times W)\to\mathcal O(W)\):

\[
\begin{aligned}
 \Psi\Bigl(\bigvee_j^\uparrow e_j\Bigr)
    &=\bigvee_j^\uparrow\Psi(e_j), &&\text{(S)}\\
 \Psi(e\vee (1\boxtimes D))
    &=\Psi(e)\vee D, &&\text{(F)}
\end{aligned}
 \tag{5.2}
\]

for nonempty directed families \((e_j)\) of \(\mathsf C\)-ideals and all \(D\in\mathcal O(W)\). Indeed, (S) descends to Scott continuity of \((\pi_K)_*\), and (F) is precisely its closed Frobenius law after pulling any open of \(K\) back to \(X\times W\). In both equations, the \(\ge\) inequality follows from monotonicity and the adjunction unit \(D\le(\pi_K)_*\pi_K^*D\); we prove the other inequality.

**(S) Scott continuity.** For a directed family \((e_j)\), put

\[
 G=\{(s,v):s\le\bigvee_j\sigma_{e_j}(v)\},
 \qquad V=\bigvee_j\Psi(e_j).
\]

Then \(G\) is a downset closed under arbitrary joins in the first coordinate, and
\(\langle G\rangle_{\mathsf C}=\bigvee_j e_j\). For \((s,v)\in G\), set
\(t_j=s\wedge v\wedge\sigma_{e_j}(v)\). Since the \(e_j\)'s are directed, so are \(\sigma_{e_j}(v)\) and \(t_j\), with \(s\wedge v=\bigvee_j t_j\). Now \(t_j\le v\) and \(\sigma_{e_j}\) is antitone, so

\[
 t_j\le\sigma_{e_j}(v)\le\sigma_{e_j}(t_j).
\]

Therefore \((t_j,t_j)\in e_j\) and \(\Box t_j\le\Psi(e_j)\le V\). By (1.1),
\(\Box(s\wedge v)=\bigvee_j^\uparrow\Box t_j\le V\). Apply Lemma 4.1 to conclude
\(\Psi(\bigvee_j e_j)\le V\). This proves (S).

**(F) Frobenius, first for a generator.** Fix \(d\in L\), put \(D=\Box d\), and let

\[
 G=\{(s,v):s\le\sigma_e(v)\vee\bigvee\{1\mid v\le d\}\},
 \qquad V=\Psi(e)\vee\Box d.
 \tag{5.3}
\]

The join indexed by the proposition \(v\le d\) is a **truth-value-indexed join**: no decision of that proposition is made. The set \(G\) is the downward, first-coordinate-join closure of the generating subset \(e\cup\downarrow(1,d)\). Hence
\(\langle G\rangle_{\mathsf C}=e\vee(1\boxtimes\Box d)\). (We do not assert that \(\downarrow(1,d)\) itself is a \(\mathsf C\)-ideal.)

For \((s,v)\in G\), put \(t=s\wedge v\wedge\sigma_e(v)\). Distributing \(s\wedge v\) over (5.3) gives

\[
 s\wedge v=t\vee\bigvee\{s\wedge v\mid v\le d\}.
 \tag{5.4}
\]

The family \(\{t\}\cup\{s\wedge v\mid v\le d\}\) is **inhabited and directed constructively**: \(t\) belongs to it, and any member of the second set bounds \(t\) and all other members of that second set (the latter are equal when present). Thus (5.4) is a **directed** join. Also \(t\le\sigma_e(v)\le\sigma_e(t)\), so \(\Box t\le\Psi(e)\); whenever \(v\le d\) holds, \(\Box(s\wedge v)\le\Box d\). Applying the directed-join law of \(\Box\) to (5.4) yields
\(\Box(s\wedge v)\le V\). Lemma 4.1 gives

\[
 \Psi(e\vee1\boxtimes\Box d)\le\Psi(e)\vee\Box d.
\]

This proves (F) for a single generator. The same identity for any **finite join** of generators follows by iteration (including the empty join, which is trivial). Finally, every \(D\in\mathcal O(W)\) is a **directed join of finite joins of generators**. Apply (S) to
\(e\vee1\boxtimes D=\bigvee_k^\uparrow(e\vee1\boxtimes D_k)\)
to obtain (F) for arbitrary \(D\).

Both (S) and (F) are proved. By quotient descent (1.4), \((\pi_K)_*\) is Scott-continuous. Because \(i_K^*\) is surjective, every \(v\in\mathcal O(K)\) is \(i_K^*e\) for some \(e\); (F) gives

\[
\begin{aligned}
 (\pi_K)_*(v\vee\pi_K^*D)
  &=(\pi_K)_*i_K^*(e\vee1\boxtimes D)\\
  &=\Psi(e\vee1\boxtimes D)\\
  &=\Psi(e)\vee D=(\pi_K)_*v\vee D.
\end{aligned}
\]

This is closed Frobenius. Thus \(\pi_K\) is proper. \(\square\)

## 6. Proof of Theorem \(L^*\)

*Proof.* Write \(E=\mathfrak c(a)\hookrightarrow X\times Y\) for some \(a\in\mathcal O(X\times Y)\).

**Properness implies Scott continuity.** If \(p_2\) is proper, \((p_2)_*\) preserves nonempty directed joins; \(p_1^*\) preserves all joins and maps directed families to directed families. Hence \(r_E=(p_2)_*p_1^*\) is Scott-continuous.

**Conversely, suppose \(r_E\) preserves nonempty directed joins.** Since \(p_1^*\) preserves finite meets and \((p_2)_*\) preserves all meets (including top), \(r_E\) is a preframe homomorphism. By the universal property (1.1), it classifies a locale map

\[
 \varphi:Y\longrightarrow P_UX=W,\qquad
 \varphi^*(\Box u)=r_E(u).
 \tag{6.1}
\]

Let \(\widetilde E\hookrightarrow X\times Y\) be the pullback of the universal family \(K\hookrightarrow X\times W\) along \(1_X\times\varphi\). By (1.3),

\[
 \widetilde E=\bigcap_{u\in L}
      [\;1\boxtimes r_E(u)\ \le\ u\boxtimes1\;]
 \quad\text{(now in \(X\times Y\)).}
 \tag{6.2}
\]

**Claim: \(E\subseteq\widetilde E\).** The adjunction formula for \(r_E\) and the description \(\mathcal O(E)=\uparrow a\) give

\[
 r_E(u)
 =\bigvee\{w\in\mathcal O(Y):1\boxtimes w\le(u\boxtimes1)\vee a\}.
 \tag{6.3}
\]

Since inverse image along the second projection preserves joins,
\(1\boxtimes r_E(u)\le(u\boxtimes1)\vee a\). Hence in \(\mathcal O(E)\),
\(i_E^*(1\boxtimes r_E(u))\le i_E^*(u\boxtimes1)\), for each \(u\). By (1.2)–(1.3), \(E\) lies in every sublocale in (6.2), and therefore in \(\widetilde E\).

**The projection \(\widetilde E\to Y\) is proper.** The ordinary product square

\[
\begin{array}{ccc}
 X\times Y&\xrightarrow{\ 1_X\times\varphi\ }&X\times W\\
 \downarrow&&\downarrow\\
 Y&\xrightarrow{\ \varphi\ }&W
\end{array}
\]

is a pullback. Pulling back \(K\hookrightarrow X\times W\) and pasting the two pullback squares yields

\[
 \widetilde E\cong Y\times_WK,
 \tag{6.4}
\]

with \(\widetilde E\to Y\) the base change of \(\pi_K:K\to W\) along \(\varphi\). It is therefore proper by Theorem K and the standard pullback-stability theorem.

**The inclusion \(E\hookrightarrow\widetilde E\) is closed and proper.** Because \(E=\mathfrak c(a)\) is closed in the product and \(E\subseteq\widetilde E\), we have

\[
 E=\widetilde E\cap\mathfrak c(a)
     =\mathfrak c(i_{\widetilde E}^*a)
       \quad\text{as a sublocale of \(\widetilde E\).}
 \tag{6.5}
\]

Closed sublocale inclusions are proper. The composite

\[
 E\hookrightarrow\widetilde E\longrightarrow Y
\]

is exactly \(p_2\), and composites of proper maps are proper. This proves the converse and hence Theorem \(L^*\). \(\square\)

## 7. Consequences and exact boundaries

**7.1. Symmetric closed relations.** If \(E\hookrightarrow X\times X\) is symmetric, coordinate interchange identifies its two projections. Therefore

\[
 r_E\text{ Scott-continuous}
 \iff p_1,p_2:E\to X\text{ are proper}.
\]

In particular this applies to \(\mathcal I_X=\operatorname{cl}(\Delta_X)\) for **every locale \(X\)**. No transitivity is assumed or deduced.

**7.2. Properness versus semi-properness for these projections.** For a projection \(p_2\) of a **closed** localic relation, Scott continuity of \((p_2)_*\) already implies that of \(r_E=(p_2)_*p_1^*\); Theorem \(L^*\) therefore supplies closed Frobenius and full properness. This inference does **not** hold for arbitrary locale maps.

**7.3. Dependence on closedness.** The proof uses closedness precisely in (6.5) to make \(E\hookrightarrow\widetilde E\) proper. The conclusion is not asserted for general sublocales of \(X\times Y\).

**7.4. Not consequences.** The theorem does not assert that \(r_E\) is idempotent, that \(E\) is transitive or effective, or that an arbitrary quotient is completely regular. Such deductions require additional hypotheses and their own results.

## 8. Proof status, metatheory, and provenance

1. **Corrected proof.** The initial referee-origin proof incorrectly said that all principal downsets \(\downarrow(s,v)\) are \(\mathsf C\)-ideals. The independent blind referee identified the error and supplied the corrected argument, incorporated in §§2–3. The original packet and both reports remain intact as archival documents.
2. **Independent verification.** The second referee reconstructed the mixed coverage, both nested inductions of Lemma 4.1, the Scott and Frobenius checks, and the final categorical pullback. The full theorem is recorded as externally verified (**E**) in the Project A master theorem ledger, with explicit attribution of the referee-origin proof.
3. **Constructivity.** The internal calculations use no choice or excluded middle. They use impredicative frames/coverage-ideal constructions (ordinary elementary-topos-style constructive mathematics), and the final argument invokes the published pullback-stability theorem for proper maps. A predicative/CZF proof is **not** claimed; the constructive verification of the published pullback-stability proof is not reproduced here.
4. **Literature/priority.** The universal-family statement is closely related in content to the constructive Hofmann–Mislove theorem and generalized points of the upper powerlocale. This note makes **no novelty claim** for either the statement or method; priority has not been exhaustively investigated.
5. **Other Project A questions** (including arbitrary-relation associativity, quotient-complete-regularity questions, and deferred tolerance/effectiveness considerations) are neither reopened nor resolved by this consolidation.

### Background references

- J. J. C. Vermeulen, *Proper Maps of Locales*, **Journal of Pure and Applied Algebra** 92 (1994), 79–107: definition, composition, and pullback stability of proper maps.
- P. T. Johnstone, *Stone Spaces* (1982), II.2.11 and II.2.13: coverage theorem and frame coproduct presentations.
- P. T. Johnstone, *Sketches of an Elephant* (2002), C1.2, C3.2, C4.1: sublocales, proper maps, and powerlocales.
- P. T. Johnstone and S. Vickers, *Preframe Presentations Present* (1991): preframe presentation methods.
- S. Vickers, *Constructive Points of Powerlocales*, **Mathematical Proceedings of the Cambridge Philosophical Society** 122 (1997), 207–222: upper-powerlocale generalized-point background.
- C. Townsend, *A Categorical Account of the Hofmann–Mislove Theorem*, **Mathematical Proceedings of the Cambridge Philosophical Society** 139 (2005), 441–456: related categorical viewpoint.

### Project A archival sources (unaltered)

- `ProjectA_Scott_converse_EXTERNAL_report2_universal_family_2026-11-08.md`: original referee-origin Theorem K/\(L^*\) proof (contains the principal-downset error).
- `ProjectA_Lstar_EXTERNAL_INDEPENDENT_referee_report_2026-11-08.md`: second independent referee's complete audit and essential repair.
- `ProjectA_Lstar_second_blind_referee_reconciliation_2026-11-08.md`: recorded comparison and disposition, including a warning about a separate preliminary spatial aside in the second referee report.
- `ProjectA_master_theorem_ledger_v1_4_2026-11-08.md`: theorem IDs Q05b/\(L^*\), Q05c/Theorem K, both E after correction.

**Archival rule:** Cite this canonical note for the corrected proof; cite the two referee reports for provenance. No repository commit is implied by creation of this file.