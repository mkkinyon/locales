# Project A / Q′ — regular-patch elimination, closed-remainder transfer, and Cohen × rational two-apex control

**13 November 2026. Working theorem and concrete test, internally checked; NOT externally audited.** Uses the earlier one-sided regular rigidity theorem and the externally checked marked-hole support/closed-heredity framework. Universal Q and Q′ remain OPEN.

## 0. Conventions and imported results

For a locale P and a cover \(\mathscr C\) of \(\mathcal O(P)\), put \(w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c\) in \(\mathcal O(P^2)\). The full and finite fitted diagonals are
\[
D(P)=\bigwedge_{\mathscr C\text{ cover}}O(w_{\mathscr C}),\qquad
D_2(P)=\bigwedge_{\mathscr F\text{ finite cover}}O(w_{\mathscr F}),
\]
and \(W(P)=\operatorname{cl}D(P)\), \(W_2(P)=\operatorname{cl}D_2(P)\). Q′ for P is \(W=W_2\).

**One-sided regular rigidity** ([source](ProjectA_Qprime_FRONTIER_ONE_SIDED_RIGIDITY_EXIT_TREE_STOP_2026-11-12.md), Theorem 1.1): for a **globally closed regular** sublocale \(J\hookrightarrow P\),
\[
D_2(P)\wedge(J\times P)=D(P)\wedge(J\times P).
\tag{R}
\]
In generalized-pair form, any finite-compatible pair \(f,g:T\to P\) with its first coordinate factoring through J matches **every** P-cover. The symmetric version holds in the second coordinate.

We also use the independently checked facts: (i) \(D_\epsilon(K)=D_\epsilon(P)\wedge K^2\) for every closed K⊆P; (ii) a genuine Q′ hole has a nonzero relative open \(E\subseteq W_2(P)\), with its Booleanization \(B(E)\subseteq D_2(P)\) dense in E and a full cover \(\mathscr C\) whose matching value on B(E) is 0. These imports have different provenance from the results below.

## 1. Regular-patch exhaustion with a closed remainder

Say that \(P\) has a **closed-regular-patch exhaustion relative to e** if an open \(e\in\mathcal O(P)\) can be written \(e=\bigvee_{i\in I}u_i\) such that each open sublocale \(O(u_i)\) is contained in a **globally closed regular** sublocale \(J_i\subseteq P\). Let \(K=C_P(e)\), the closed remainder; K need not itself be regular.

**Lemma 1.1 (Boolean defect concentrates in the remainder).** Let \(h,k:\mathcal O(P)\to B\), B a nontrivial complete Boolean algebra, be finite-cover-compatible. If some full P-cover \(\mathscr C\) has **zero** matching value
\[
\bigvee_{c\in\mathscr C}h(c)\wedge k(c)=0_B,
\tag{1.1}
\]
then \(h(e)=k(e)=0\). Hence both coordinates factor through K.

*Proof.* Fix i and put \(m=h(u_i)\in B\). On the open Boolean component m, the first coordinate lies in J_i because O(u_i)⊆J_i. By (R), the restricted pair matches \(\mathscr C\), contradicting (1.1) unless \(m=0\). Thus \(h(u_i)=0\) for every i, so \(h(e)=0\). Apply the symmetric version of (R) to k to get k(e)=0. □

**Theorem 1.2 (nonclosed fitting equality from a regular remainder).** If \(P\) admits such an exhaustion and \(D_2(K)=D(K)\), then
\[
\boxed{D_2(P)=D(P).}\tag{1.2}
\]
In particular it suffices for K to be regular or compact.

*Proof.* If D₂(P)>D(P), choose a P-cover C whose matching open in O(D₂(P)) is proper. Its nonzero closed complement has nonzero Booleanization, yielding a nontrivial complete Boolean target B and a finite-compatible pair with zero C-matching value. Lemma 1.1 makes both endpoints factor through K. The closed-heredity identity D₂(P)∧K²=D₂(K), together with D₂(K)=D(K), now forces the restricted pair to match C|K, contradicting zero matching. □

**Theorem 1.3 (closed-remainder Q′ transfer).** If \(P\) admits such an exhaustion and **K is Q′-positive**, then **P is Q′-positive**:
\[
\boxed{W_2(K)=W(K)\quad\Longrightarrow\quad W_2(P)=W(P).}\tag{1.3}
\]
No assumption D₂(K)=D(K) is needed.

*Proof.* Suppose P has a genuine marked relative-open Q′ hole E in W₂(P), from some cover C. Its dense Booleanization B(E)≤D₂(P) has C-matching value zero. By Lemma 1.1, both coordinate maps on B(E) factor through K; therefore B(E)≤K². Since K² is closed and B(E) is dense in E, also E≤K².

By closed heredity, D₂(P)∧K²=D₂(K). The sublocale D₂(P)∧E is dense in E (since E is relatively open in W₂(P)), and it lies in D₂(K); consequently E≤W₂(K). As W₂(K)≤W₂(P)∧K², the original E remains a **nonzero relatively open** sublocale of W₂(K). It meets D(K)=D(P)∧K² trivially (C-matching is zero), so it is disjoint from W(K) as well, because closure commutes with restriction to an open sublocale. This contradicts W₂(K)=W(K). □

**Important:** Theorem 1.3 is a one-way preservation statement, NOT closed-heredity of Q′. Ordinary arbitrary-closed restriction of a dense sublocale is still invalid. The marked-open step is what makes the argument work.

## 2. Product stability under a regular base

If Z is regular, products of Z with regular locales are regular. If J_i↪P and K↪P are closed, then Z×J_i and Z×K are globally closed in Z×P. Moreover the opens \(Z\times O(u_i)\) cover \(Z\times O(e)\). Therefore:

**Corollary 2.1.** Let P admit the exhaustion of §1 and let Z be any regular locale.
1. If \(D_2(Z\times K)=D(Z\times K)\), then \(D_2(Z\times P)=D(Z\times P)\).
2. If \(W_2(Z\times K)=W(Z\times K)\), then \(W_2(Z\times P)=W(Z\times P)\).

The hypotheses on Z×K cannot simply be replaced by corresponding hypotheses on K alone: Q′ preservation under arbitrary regular/Boolean bases is NOT proved in general. In the special case when K itself is regular, Z×K is regular, and part 1 applies.

## 3. The Cohen × noncompact rational two-apex test

Recall the sober T₁ noncompact space \(X_{\mathrm{cof}}=\mathbb Q_+\amalg\mathbb Q_-\amalg\{a,b,t\}\), whose apex neighborhoods use \(G_n=(n,\infty)\cap\mathbb Q\): \(A_n=\{a\}\cup(G_n)_+\), \(B_n=\{b\}\cup(G_n)_-\), \(T_n=\{t\}\cup(G_n)_+\cup(G_n)_-\). Its established finite-cover witness gives \(W(X_{\mathrm{cof}})=W_2(X_{\mathrm{cof}})<U(X_{\mathrm{cof}})\).

Let e be the union of the two rational arms. Cover e by bounded rational intervals \(I\) in either arm. Their closures in X_cof are entirely contained in the same rational arm (late cofinal tails miss each bounded interval); hence each \(\overline I\) is a **globally closed regular sublocale**. The closed remainder \(K=\{a,b,t\}\) is discrete, finite, hence regular. Consequently for **every regular locale Z**, the product Z×X_cof has the exhaustion of §1 with regular remainder Z×K, and
\[
\boxed{D_2(Z\times X_{\mathrm{cof}})=D(Z\times X_{\mathrm{cof}}).}\tag{3.1}
\]
In particular choose the **pointless** Cohen Boolean locale \(Z_C=\mathrm{Loc}(RO(2^\omega))\), which is regular. Then
\[
\boxed{W_2(Z_C\times X_{\mathrm{cof}})=W(Z_C\times X_{\mathrm{cof}}).}\tag{3.2}
\]
This is a **negative control for Q′**, not a universal Q′ proof.

The product retains a strict rank gap. For nonzero regular Z, \(W(Z)=U(Z)=\Delta_Z\); naturality of W and the *universal* U-product formula yield
\[
W(Z\times X_{\mathrm{cof}})
\le\Delta_Z\times W(X_{\mathrm{cof}})
<\Delta_Z\times U(X_{\mathrm{cof}})
=U(Z\times X_{\mathrm{cof}}).
\]
Thus, in particular,
\[
\boxed{W(Z_C\times X_{\mathrm{cof}})=W_2(Z_C\times X_{\mathrm{cof}})<U(Z_C\times X_{\mathrm{cof}}).}\tag{3.3}
\]
**Not claimed:** exact formula \(W(Z_C\times X_{\mathrm{cof}})=\Delta_{Z_C}\times W(X_{\mathrm{cof}})\), or a formula for the nonclosed product D. The displayed inequality suffices to preserve the strict gap.

## 4. Candidate-selection consequences

The new regular-patch theorem eliminates Cohen×X_cof by an intrinsically **nonclosed** argument: even an infinitary weak D₂>D defect is impossible. It also eliminates any further product test built by attaching regular patches to a **Q′-positive product remainder**, even if the total space is nonregular and the regular pieces are NOT clopen. This extends, but does not supersede, the earlier **clopen-remainder gluing** theorem (which needs Q′-positive clopen charts but allows arbitrary nonregular charts).

An informative next candidate requires a remainder Z×K whose Q′ status is genuinely unknown (not regular, compact, anti-Urysohn-Boolean-stabilized or already controlled by previous kernel-exhaustion theorems). More importantly, it needs an **explicit full-cover square giving a nonzero relatively open hole in W₂**; a Cohen-valued finite/full weak defect alone is not enough.

**Audit status:** New §§1–3 internally reconstructed, not independently blind-reviewed. The key potential proof-checks are Booleanization of the closed complement in Theorem 1.2, preservation of E through K² in Theorem 1.3, regularity of localic products, and the strictness of (3.3). Neither universal Q nor universal Q′ is resolved.
