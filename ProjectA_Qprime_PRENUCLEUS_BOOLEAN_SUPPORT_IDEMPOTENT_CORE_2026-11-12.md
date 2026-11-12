# Project A — Q′ and the pre-nucleus: idempotent Boolean-support core of a counterexample

**12 November 2026 — NEW INTERNAL theorem and research consolidation; NOT independently audited, no literature-priority claim.** This responds to the question whether the *pre-nucleus itself sees the apparent self-similarity* of a hypothetical Q′ counterexample, after the [frontier stop rule](ProjectA_Qprime_FRONTIER_ONE_SIDED_RIGIDITY_EXIT_TREE_STOP_2026-11-12.md). **Yes, in a sharply limited and testable sense.** A bad cover yields a **canonical nonzero relative regular-open hole E inside W₂**, and its least CLOSED common coordinate support K is itself a Q′ counterexample. The *same E and its canonical Boolean witness* survive unchanged on K. The restricted bad cover has **zero rather-below patch**, and K has **no nonzero open two-coordinate hull-sound strip**. The support reduction is **idempotent for the marked E**; it is not a claimed recursive self-similarity of the entire frame or an existence theorem for Q′ counterexamples.

Notation, scope and provenance are critical. The two pre-nuclei/fixed-point criterion, closed-subspace fitting heredity, universal regular-core bound, and Isbell minimal dense Boolean sublocale are from the previous project framework (the first group externally corroborated on 9 November). The new theorem is the **joint support normalization and exact persistence** (§§2–5), not the older observation that a closed remainder can also be a counterexample. Neither Q nor Q′ is solved.

## 0. The full-cover pre-nucleus *inside* the finite closed hull

Let \(L=\mathcal O(X)\), \(Q=L\oplus L=\mathcal O(X^2)\), and for every open cover \(\mathcal C\) of \(1_L\) put
\[
w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c,\qquad
\Phi(q)=\bigvee_{\mathcal C}(w_{\mathcal C}\to q),\qquad
\Phi_2(q)=\bigvee_{\mathcal F\text{ finite cover}}(w_{\mathcal F}\to q).
\]
The families are diagonal-neighborhood filters, so \(\Phi,\Phi_2\) are inflationary meet-preserving pre-nuclei. Let
\[
d_0=d_{\mathcal W_2}=\Phi_2^\infty(0),\qquad
\mathcal W_2=C_Q(d_0),\qquad
\Phi_2(d_0)=d_0.
\]
The frame of opens of \(\mathcal W_2\) is the upset \(\uparrow d_0\subseteq Q\) (bottom \(d_0\)). Both pre-nuclei restrict to pre-nuclei on this frame. For q≥d₀, a cover square restricts to \(w_{\mathcal C}\vee d_0\), whose implication inside \(\uparrow d_0\) is
\[
(w_{\mathcal C}\vee d_0)\to_{\uparrow d_0}q
=(w_{\mathcal C}\to_Qq)\wedge(d_0\to_Qq)
=w_{\mathcal C}\to_Qq.
\tag{0.1}
\]
Thus the **relative full pre-nucleus** is literally the restriction \(\Phi|_{\uparrow d_0}\). The previously established fixed-point criterion is
\[
\boxed{\mathcal W=\mathcal W_2\iff\Phi(d_0)=d_0.}
\tag{0.2}
\]

For a cover C set
\[
\rho_C=w_C\to d_0,\qquad
E_C=\mathcal W_2\wedge\mathfrak o_Q(\rho_C).
\tag{0.3}
\]
Inside \(\mathcal W_2\), \(\rho_C\) is the **relative pseudocomplement** of \(w_C\vee d_0\), hence a *regular open* of \(\mathcal W_2\). It is nonzero iff \(\rho_C\not\le d_0\). Consequently
\[
\boxed{Q'\text{ fails on X}\iff E_C\ne0
\text{ for SOME cover C}.}
\tag{0.4}
\]
Equivalently Q′ holds iff **every arbitrary-cover square open is dense in W₂**. (This does NOT mean set-theoretic intersection of those dense opens is dense; we use the locale-theoretic sublocale meet and the minimal Boolean dense sublocale.)

For finite covers F, the relative pseudocomplement is always zero, because \(\Phi_2(d_0)=d_0\).

## 1. First-step hole and canonical Boolean obstruction

Assume one cover C has E=E_C≠0 and put \(\rho=\rho_C\).

Because \(\mathcal D_2\) is dense in its closed hull W₂, \(\mathcal D_2\wedge E\) is dense in the relatively open E. Let \(B(E)\) denote Isbell's least dense Boolean sublocale of E. Therefore
\[
B(E)\le\mathcal D_2(X)\wedge E
\quad\text{and}\quad
B(E)\ne0.
\tag{1.1}
\]
The canonical projections \(B(E)\to X\) induce frame homomorphisms
\[
h,k:L\longrightarrow M=\mathcal O(B(E)),
\tag{1.2}
\]
where M is a NONZERO complete Boolean algebra. For EVERY finite X-cover F,
\[
\boxed{\bigvee_{c\in F}h(c)\wedge k(c)=1_M.}
\tag{1.3}
\]
But by definition \(\rho\wedge w_C\le d_0\), so \(E\wedge\mathfrak o(w_C)=0\). Consequently
\[
\boxed{\bigvee_{c\in C}h(c)\wedge k(c)=0_M.}
\tag{1.4}
\]
This is a canonical **zero-valued full-cover defect on an OPEN part of W₂**, not an arbitrary D₂>D witness. In particular the complete Boolean M must be atomless: an atom yields a point of B(E), hence an ordinary D₂ pair which is also a D pair by the old all-locale equality of point sets, contradicting (1.4).

These observations use only the existence of the ONE-step hole E; no long Φ transfinite iteration is involved.

## 2. The closed common coordinate support: a pre-nucleus formula

Let \(p_1,p_2:X^2\to X\) be projections, with \(p_i^*:L\to Q\) and their right adjoints \(p_{i*}:Q\to L\). Define
\[
\boxed{
e_C=p_{1*}(\rho\to d_0)\wedge p_{2*}(\rho\to d_0),
\qquad
K_C=\mathfrak c_X(e_C).
}
\tag{2.1}
\]
The formula is computed entirely from the **finite pre-nucleus fixed point d₀, the chosen full cover w_C and the coordinate adjunctions**; no choice of a disjoint rectangle is required. An equivalent characterization is
\[
\boxed{
e_C=\bigvee\{a\in L:h(a)=k(a)=0_M\}.
}
\tag{2.2}
\]

*Proof of equivalence.* Density of B(E) in E means
\[
h(a)=0_M
\iff E\wedge\mathfrak o(p_1^*a)=0
\iff \rho\wedge p_1^*a\le d_0
\iff a\le p_{1*}(\rho\to d_0),
\]
and symmetrically for k. Their common zero ideal is the principal downset ↓e_C. Because h,k preserve arbitrary joins, h(e_C)=k(e_C)=0. QED.

**Proposition 2.1 (minimal support).** \(K_C\) is the **least closed sublocale of X** through which BOTH coordinate maps \(B(E)\to X\) factor. Moreover
\[
\boxed{E\le K_C\times K_C}
\tag{2.3}
\]
as actual sublocales of X², and after factoring h,k through \(\mathcal O(K_C)=\uparrow e_C\) we have
\[
\boxed{
\forall\,0_{K_C}\ne v\in\mathcal O(K_C):
\quad h_K(v)\vee k_K(v)\ne0_M.
}
\tag{2.4}
\]
That is, the pair is **jointly zero-reflecting** on K_C, or E has joint dense coordinate support.

*Proof.* h,k factor through C(e_C) because h(e_C)=k(e_C)=0. If another closed C(a) supports them, then h(a)=k(a)=0, hence a≤e_C, so C(e_C)≤C(a). The pair B(E)→K_C² exists; K_C² is CLOSED in X². Since B(E) is dense in E, the closed K_C² containing B(E) contains E, proving (2.3). Finally v∈↑e_C with both h_K(v)=k_K(v)=0 implies v≤e_C by (2.2); thus v=e_C=0_K. QED.

**Caution:** "jointly zero-reflecting" does **not** mean each h_K and k_K separately reflects zero. Nor does it mean that K_C is a minimal Q′ counterexample among ALL closed sublocales of X. It is only minimal among closed **supports for this marked E**.

## 3. Exact persistence: the SAME hole in the smaller locale

**Theorem 3.1 (marked-hole self-reduction).** For K=K_C as above, let \(i:K\hookrightarrow X\), \(C_K=\{i^*(c):c\in C\}\), and \(\rho_K=i^{(2)*}(\rho)\), where \(i^{(2)}=i\times i\). Then
\[
\boxed{\mathcal W_2(K)\wedge\mathfrak o_{K^2}(\rho_K)=E}
\tag{3.1}
\]
under the inclusion \(K^2\hookrightarrow X^2\), and
\[
\boxed{\mathcal W(K)\wedge E=0,\quad
B(E)\le\mathcal D_2(K)\wedge E,\quad
\mathcal D(K)\wedge E=0.}
\tag{3.2}
\]
In particular W(K)<W₂(K), and \(C_K\) is a **genuine full-cover pre-nucleus witness** on K:
\[
\boxed{
\rho_K\wedge w_{C_K}\le d_{\mathcal W_2(K)},\qquad
\rho_K\not\le d_{\mathcal W_2(K)},\qquad
\Phi_K(d_{\mathcal W_2(K)})>d_{\mathcal W_2(K)}.
}
\tag{3.3}
\]
The pair \(h_K,k_K:\mathcal O(K)\to M\) is **the exact same Boolean probe** from §1, with every finite cover matched to 1 and the restricted C-cover matched to 0.

*Proof.* First recall exact **closed heredity** for both fitted diagonals:
\[
\mathcal D_\varepsilon(K)=
\mathcal D_\varepsilon(X)\wedge K^2,\qquad
\varepsilon\in\{\text{full},2\}.
\tag{3.4}
\]
This can be shown WITHOUT presuming that arbitrary locale pullbacks preserve all sublocale meets: generalized endpoint maps into K² are finite/full cover-compatible in K iff their composites into X² are compatible in X. Indeed every X-cover restricts to a K-cover, and conversely every K-cover lifts to an X-cover by adding the open complement e_C, which is zero on both K endpoints.

By (1.1) and Proposition 2.1,
\[
B(E)\le\mathcal D_2(X)\wedge K^2=\mathcal D_2(K).
\]
Since B(E) is dense in E and W₂(K) is CLOSED in K² containing B(E), we obtain \(E\le W₂(K)\).

Conversely W₂(X)∧K² is a closed sublocale of K² containing D₂(K), so
\[
W₂(K)\le W₂(X)\wedge K^2.
\]
Intersect with the open \(\mathfrak o_{K^2}(\rho_K)\). Because E≤K², both inclusions give EXACTLY (3.1).

From \(E\wedge O_X(w_C)=0\) and D(X)≤O_X(w_C), closed heredity gives D(K)∧E=0. Since \(E=W₂(K)\wedge O_{K^2}(\rho_K)\), D(K) is disjoint from the **open** \(O_{K^2}(\rho_K)\) (indeed D(K)≤W₂(K)), so its closure W(K) is also disjoint from that open, giving W(K)∧E=0. This proves (3.2).

Pull back \(\rho\wedge w_C\le d_0\) along i²:
\[
\rho_K\wedge w_{C_K}\le i^{(2)*}d_0\le d_{\mathcal W_2(K)}.
\]
The last inequality is equivalent to W₂(K)≤W₂(X)∧K², already proved. The equality E=W₂(K)∧O(\rho_K) shows \(\rho_K\not\le d_{\mathcal W_2(K)}\). Therefore \(\Phi_K(d_{\mathcal W_2(K)})>d_{\mathcal W_2(K)}\), establishing (3.3). QED.

**Important:** We do NOT claim that \(\rho_K=(w_{C_K}\to d_{\mathcal W_2(K)})\); only the indicated inequality and the exact persistence of the marked *open E*. The entire new cover-hole might be larger than E. The reduction is idempotent **for the fixed E**, not necessarily if one replaces E at each stage by the new entire hole.

## 4. The intrinsically saturated CORE: t_C vanishes in ONE step

**Theorem 4.1 (cover-patch saturation and sound-strip elimination).** On the reduced locale K=K_C,
\[
\boxed{t_{C_K}^{\,K}=0_K.}
\tag{4.1}
\]
Indeed K has **no nonzero open \(v\)** on whose **two-coordinate strip**
\[
(p_1^*v)\vee(p_2^*v)
\]
the two closed hulls W(K) and W₂(K) agree. Therefore all previously identified open hull-sound loci in K vanish (in particular \(h_{\rm hc}(K)=0\) by the earlier working hyperconnected-strip theorem; similarly compact-closed-neighborhood strips by the prior, stronger fitted-diagonal result).

*Proof of (4.1) without any residual-lemma dependency.* Fix a finite subfamily F⊂C_K, write c_F=∨F in O(K), and choose v≺_K c_F. Then \(\{v^*\}\cup F\) is a **finite cover of K**. Finite compatibility of h_K,k_K implies
\[
1_M=h_K(v^*)\wedge k_K(v^*)
\vee\bigvee_{c\in F}h_K(c)\wedge k_K(c).
\]
The last join is zero because the SAME pair matches the entire bad cover C_K to zero. Meeting with h_K(v) gives h_K(v)=0; symmetry gives k_K(v)=0. Joint zero-reflection (2.4) implies v=0_K. Thus every rather-below patch in the definition of t_{C_K} is zero, proving (4.1).

For the sound-strip assertion, suppose v∈O(K) is such that W(K)=W₂(K) when restricted to the union of the two coordinate strips of v. Since E≤W₂(K) and E∧W(K)=0, E has zero intersection with **both** strips. Density of B(E) in E implies h_K(v)=k_K(v)=0, hence v=0_K by (2.4). QED.

**Idempotence for the marked hole.** Repeat the support construction §2 on K, using the same E embedded in K² and its SAME B(E) coordinate pair. Joint zero-reflection means the largest common killed open in O(K) is bottom. Hence the newly calculated *closed support for E* is **K itself**, not a proper closed sublocale. This is a literal idempotent normal form: one reduction produces an E-supported core that cannot be further reduced by killing opens invisible to both endpoints.

This **strengthens** the earlier conditional observation "if a minimal closed counterexample exists, then t_C and safe strips vanish." The normalized core ALWAYS exists given a Q′ counterexample, with NO minimal-counterexample hypothesis and NO transfinite-limit continuity assumption. It is not necessarily a minimal *locale* counterexample—only an irredundant support for the fixed E.

## 5. A formal lax naturality statement for the prenucleus

For any closed inclusion \(i:K\to X\), let \(q=i^{(2)*}:Q_X\to Q_K\) be its frame map. For every z∈Q_X, frame maps preserve implications only in the **lax** direction
\[
q(w_C\to z)\le(qw_C\to qz).
\]
Thus
\[
\boxed{q(\Phi_X(z))\le\Phi_K(qz),\qquad
q(\Phi_{2,X}(z))\le\Phi_{2,K}(qz).}
\tag{5.1}
\]
The second inequality uses the restriction of finite X-covers, and the first of all X-covers. **Equality is not claimed.** The finite fixed-point d₀ also need not commute with closed restriction: all we generally have is
\[
q(d_{\mathcal W_2(X)})\le d_{\mathcal W_2(K)},
\]
since W₂(K) lies in the closed pullback of W₂(X).

The support theorem is strictly more powerful than lax naturality: it carries the **same nonzero localic open E**, with its **same Boolean witness**, across a closed restriction, even though none of these naive equalities of pre-nuclei or fixed points has been assumed.

## 6. Important negative control and anti-drift conclusion

The completed branching algebraic Scott dcpo S from [continuous-dcpo note](ProjectA_Qprime_continuous_dcpo_OPEN_Cm_regular_U_closed_heredity_2026-11-11.md) has an explicit Boolean pair finite-cover-compatible and with a ZERO-valued infinite cover, so \(\mathcal D_2(S)>\mathcal D(S)\). Yet \(\mathcal W_2(S)=\mathcal W(S)=S^2\). Therefore for **every** cover C on S,
\[
E_C=W₂(S)\wedge O(w_C\to d_0)=0.
\]
The Boolean pair on S is **not** the Booleanization of a nonzero relatively OPEN defect of W₂. This is the precise distinction: an infinitary fitted-diagonal defect may be present only in a nowhere-dense **sublocale**, and no first-step Φ-hole exists.

Thus the theorem does NOT prove Q′, nor does it reduce the problem to the bare existence of any jointly zero-reflecting Boolean pair with a zero-valued bad cover. One additionally needs its support to be **dense in a nonzero relatively open part of W₂**, as in §1. The condition is essential and already falsified by S.

**Anti-drift research decision.** Rather than invent another geometric counterexample, use the present normalized core as the **canonical internal normal form** for any failure of Q′:
- one full cover C whose square is NOT dense in W₂;
- its nonzero regular-open complement E in W₂;
- the same Boolean algebra M=O(B(E)) and a finite-compatible, C-incompatible pair with matching value zero;
- joint zero-reflection in the reduced frame O(K);
- no nonzero rather-below patch for the SAME cover C and no open two-coordinate W/W₂ agreement strips;
- \(\Phi_K(d_{\mathcal W_2(K)})>d_{\mathcal W_2(K)}\), with exactly the original marked E still visible.

These conditions DO NOT produce a contradiction: the completed branching Scott example shows several of them can coexist without an OPEN hull defect. They do replace the earlier metaphorical "self-similarity" by a rigorous **idempotent support-reduction theorem** and make further investigation of Q′ an algebraic, auditable question about the relative pre-nucleus and its canonical Boolean hole, not an endless catalogue of frontier geometries.

**STATUS: New internal proof only; Q/Q′ still OPEN.**
