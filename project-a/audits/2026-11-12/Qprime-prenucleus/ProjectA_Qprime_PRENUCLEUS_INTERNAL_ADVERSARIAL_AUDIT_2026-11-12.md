# Project A — Internal adversarial audit: Q′ pre-nucleus holes and Boolean support cores

**12 November 2026 — INTERNAL REVIEW ONLY. DO NOT SEND TO THE EXTERNAL BLIND REFEREE.**

## Scope, source, and verdict

**Target:** [ProjectA_Qprime_PRENUCLEUS_BOOLEAN_SUPPORT_IDEMPOTENT_CORE_2026-11-12.md](../../../ProjectA_Qprime_PRENUCLEUS_BOOLEAN_SUPPORT_IDEMPOTENT_CORE_2026-11-12.md), as amended through the distinction between **weak fitting** defects and **strong open-hull** defects, and the earlier prerequisites:
- diagonal cover presentation, \(\Phi,\Phi_2\), fixed-point theorem, and rectangle criterion — independently reviewed on 9 November;
- [closed heredity of \(\mathcal D,\mathcal D_2\)](../../../ProjectA_Qprime_closed_remainder_HEREDITARY_REDUCTION_REGULAR_2026-11-11.md) — internal working result;
- [one-sided closed compact/regular rigidity](../../../ProjectA_Qprime_FRONTIER_ONE_SIDED_RIGIDITY_EXIT_TREE_STOP_2026-11-12.md) — internal working result;
- Isbell least dense Boolean sublocale — standard locale-theoretic fact, but explicitly rechecked below.

**Overall verdict:** No counterexample or fatal logical flaw found in the **first-step open-hole criterion**, **canonical Boolean probe**, **least closed common-coordinate support**, **exact persistence of the same marked hole**, or **one-step idempotent support normalization**. Their short proofs can be reconstructed without presuming that pullback preserves closure. The **weak/strong distinction is indispensable** and the weak defect lemma has to be proved via closed-complement pullback, not by making a false inference that a proper sublocale difference is relatively open. The two newest hereditary sufficient criteria are valid *conditional on* the internally proved one-sided rigidity lemma, but are **not independently certified**. This is a mathematical review of this target, NOT a retrospective certification of the entire November geometric example corpus; especially the separately sourced hyperconnected-strip theorem remains at its earlier status.

**No resolution of \(Q'\) or \(Q\), no originality or priority judgment.** Recommend an independent, blind, adversarial review before upgrading statuses.

## A. Independent reconstruction and verdicts

### A1. First-step \(\Phi\)-hole — PASS

Let \(Q=L\oplus L\), \(w_C=\bigvee_{c\in C}c\boxtimes c\), \(\Phi(z)=\bigvee_C(w_C\to z)\), \(\Phi_2(z)=\bigvee_{F\text{ finite}}(w_F\to z)\), \(d_0=\Phi_2^\infty(0)=d_{\mathcal W_2}\). We use the previously externally corroborated \(\Phi_2(d_0)=d_0\) and \(\Phi^\infty(0)=d_{\mathcal W}\).

For \(q\ge d_0\), the frame \(O(C(d_0))=\uparrow d_0\) has bottom \(d_0\), and
\[
(w_C\vee d_0)\to_{\uparrow d_0}q=w_C\to_Q q.
\]
This follows from the adjunction against test elements \(z\ge d_0\), not from an assumption that every locale pullback preserves arbitrary implications. In particular \(\rho_C=w_C\to d_0\ge d_0\) is the **relative pseudocomplement** of the restricted cover-square, hence \(\rho_C^{**}=\rho_C\) in \(O(\mathcal W_2)\). Thus \(E_C=\mathcal W_2\wedge O_Q(\rho_C)\) is relatively **regular open**.

\(\Phi(d_0)>d_0\) iff some \(\rho_C>d_0\) iff some \(E_C\ne0\) iff \(d_{\mathcal W}>d_0\). Finite covers alone give \(\rho_F=d_0\). **PASS.**

**Exposition repair:** distinguish \(O_Q(\rho_C)\), an ambient open, from its restriction \(E_C\), which is regular open **in W₂**, not necessarily an ambient regular-open element of Q.

### A2. Isbell Boolean probe and zero-valued cover — PASS, with explicit dependency

\(\mathcal D_2\) is dense in its closure \(\mathcal W_2\), so \(\mathcal D_2\wedge E\) is dense in **the open sublocale** E. In any locale T, the double-negation nucleus is the maximum dense nucleus: for any dense nucleus j, \(j(a)\wedge a^*\le j(0)=0\), so \(j(a)\le a^{**}\). Thus \(B(T)\), its least dense Boolean sublocale, lies in every dense sublocale. Hence \(B(E)\le\mathcal D_2\wedge E\).

The endpoint maps from \(B(E)\to X^2\) are frame homomorphisms to the NONZERO complete Boolean algebra \(M=O(B(E))\). Since \(B(E)\le\mathcal D_2\), every finite cover has matching value 1; since \(\rho_C\wedge w_C\le d_0\), \(B(E)\wedge O_Q(w_C)=0\), so the chosen full cover has matching value **zero**. **PASS.**

**Exposition repair:** density of D₂ on E is needed; bare D₂>D does not produce such an E. Atomlessness of M follows from the previous theorem that \(\operatorname{pt}\mathcal D_2=\operatorname{pt}\mathcal D\) and the fact that B(E) misses D; this is an *ancillary*, not a proof-critical, observation.

### A3. Common coordinate zero ideal and support formula — PASS

Let \(h,k:L\to M\). For any \(a\in L\), density of B(E) in E gives
\[
h(a)=0\iff E\wedge O_Q(p_1^*a)=0
\iff \rho_C\wedge p_1^*a\le d_0
\iff a\le p_{1*}(\rho_C\to d_0),
\]
and analogously for k. Thus the **joint** kernel is the downset of
\[
e_C=p_{1*}(\rho_C\to d_0)\wedge p_{2*}(\rho_C\to d_0).
\]
As h,k preserve arbitrary joins, \(h(e_C)=k(e_C)=0\). K=C_X(e_C) is the **least closed** common support (note the contravariant order of C(e)). With \(B(E)\le K^2\) and K² closed in X², its density in E forces \(E\le K^2\). The induced pair on \(O(K)\) is **jointly zero-reflecting**, but NEITHER separate map need reflect zero. **PASS.**

**Exposition repair:** prove explicitly the step “closed K² containing dense B(E) contains E” by intersecting K² with E, a relatively closed sublocale of E; density then forces all of E. Do not invoke automatic spatiality.

### A4. Exact persistence of THE SAME E — PASS, highest-priority external check

For any closed inclusion \(i:K\hookrightarrow X\), a family of K-opens lifts to a family of X-opens by adding the open complement of K. Hence an arbitrary generalized pair into K² is finite/full cover compatible **in K iff** its composite is compatible in X; this gives
\[
D_\varepsilon(K)=D_\varepsilon(X)\wedge K^2,\quad\varepsilon=2,\text{full}.
\]
This proof avoids a questionable unqualified claim that a particular **closure operator** commutes with closed restriction.

Because \(B(E)\le D_2(X)\wedge K^2=D_2(K)\) and B(E) is dense in E, \(E\le W_2(K)\). On the other hand \(W_2(X)\wedge K^2\) is closed in K² and contains \(D_2(K)\), so \(W_2(K)\le W_2(X)\wedge K^2\). Intersecting with the **ambient open restricted to K²** \(O(\rho|K²)\) yields **exactly**
\[
W_2(K)\wedge O_{K²}(\rho_K)=E
\]
as sublocales of K². Full cover C|K matches zero and \(D(K)\le W_2(K)\), so \(D(K)\) misses the entire open \(O_{K²}(\rho_K)\); hence its **closure** \(W(K)\) misses that open, proving \(W(K)\wedge E=0\). This is stronger than the insufficient inference “D(K)∧E=0 ⇒ W(K)∧E=0”; the **ambient open** is essential. **PASS.**

**High-priority external requests:** Can a referee find a localic subtlety in (i) B(E) dense relative to E, (ii) exact closed heredity, (iii) passing from relative dense containment to E≤W₂(K), or (iv) the open-restriction closure argument?

**Scope warning:** \(\rho_K\) need NOT equal \(w_{C_K}\to d_{W_2(K)}\); the proof supplies \(\rho_K\wedge w_{C_K}\le d_{W_2(K)}\), \(\rho_K\not\le d_{W_2(K)}\) and hence \(\Phi_K(d_{W_2(K)})>d_{W_2(K)}\), without identifying the two opens.

### A5. Saturation \(t_{C_K}=0\) and idempotence — PASS

The reduced Boolean pair is finite compatible, matches C_K to 0 and jointly reflects 0. If \(v\prec_K\bigvee F\) for finite F⊂C_K, the finite cover \(\{v^*\}\cup F\) has compatibility value 1; meeting with either coordinate's value of v kills the v* square, while every F-square term is ≤the zero-valued full cover. Hence h(v)=k(v)=0, so v=0_K. All summands in \(t_{C_K}\) vanish.

Also E≤W₂(K) and E is disjoint from W(K). If v is two-coordinate hull-sound on K, E misses both strips, so the Boolean coordinate values h(v),k(v) vanish; joint zero-reflection gives v=0. Repeating the **least common closed support of the SAME marked E** in K gives K itself. **PASS.**

**Scope warning:** This is idempotence of **marked support reduction**, NOT \(\Phi^2=\Phi\), NOT idempotence when replacing E by a new maximal hole in K, and NOT existence of a minimal counterexample among all closed sublocales.

### A6. Absorption of old patches — PASS, conditional on strip premises

For the ORIGINAL Boolean pair, finite-cover compatibility + C-matching zero imply \(h(v)=k(v)=0\) whenever \(v\prec\bigvee F\) with F⊂C finite. Hence \(t_C\le e_C\).

For any hull-sound open a, W and W₂ agree on the two coordinate strips. Since \(D\le O(w_C)\) and \(\rho\wedge w_C\le d_0\), one has \(W\wedge O(\rho)=0\). Thus E misses the a-strips, h(a)=k(a)=0, and a≤e_C. In particular \(h_{\rm hc},h_{\rm cc}\le e_C\) **provided** the earlier working strip theorems hold. **PASS conditional on those independently identified imports.**

### A7. Lax naturality — PASS

For the restriction frame map \(q:Q_X\to Q_K\), frame homomorphisms satisfy \(q(x\to y)\le(qx\to qy)\), not generally equality. Every restricted X-cover is a K-cover, hence
\[
q\Phi_X(z)\le\Phi_K(qz),\quad q\Phi_{2,X}(z)\le\Phi_{2,K}(qz).
\]
Likewise \(q(d_{W_2(X)})\le d_{W_2(K)}\). No commuting-fixed-points or commuting-implications claim is made. **PASS.**

### A8. Weak \(\mathcal D_2>\mathcal D\) normalization — PASS after spelling out closed-complement pullback

If \(D_2\not\le D=\bigwedge_C O(w_C)\), then for some C, \(D_2\not\le O(w_C)\). In the locale \(D_2\), the pullback of \(C_{X²}(w_C)\) is the **relative closed complement** of its restricted open \(w_C|D_2\). A closed complement is zero iff the restricted open is top. Therefore
\[
T_C=D_2\wedge C_{X²}(w_C)\ne0.
\]
This is NOT to be confused with a **nonzero open part of W₂**. \(B(T_C)\to X²\) supplies a finite-cover-compatible Boolean pair with C-matching zero, and passing to the least common closed coordinate support yields a jointly zero-reflecting pair with \(t_{C_K}=0\) and \(\mathcal D_2(K)>\mathcal D(K)\). **PASS.**

**Exposition repair (important):** State the relative closed-complement argument explicitly. The inference “a sublocale not contained in O(w) must meet C(w)” is a theorem about pullback of this *particular closed complement*, not about arbitrary complementary sublocales or arbitrary lattice distributivity.

**Negative control:** The completed branching Scott dcpo has such a normalized Boolean pair and t_C=0 but W=W₂. Therefore these properties alone are NOT evidence of Q′ failure. The strong theorem additionally has a nonzero relatively OPEN E⊆W₂, whose identity survives support reduction.

### A9. Two hereditary positive criteria — CONDITIONAL PASS, externally request an independent proof

(i) If every nonzero closed Y⊆X has \(t_V^Y\ne0\) for every cover V of Y, then the WEAK normalization contradicts this, giving \(D_2(X)=D(X)\). This is stronger than just Q′ and follows directly from A8.

(ii) If every nonzero closed Y⊆X contains a nonzero open V≤J for a compact OR regular closed J⊆Y, then the earlier one-sided theorem
\[
D_2(Y)\wedge(J\times Y)=D(Y)\wedge(J\times Y)
\]
(and symmetric) forces any zero-valued C Boolean witness on Y to kill V on both coordinates. Joint zero-reflection contradicts V≠0, so \(D_2(X)=D(X)\). **The new consequence is sound IF the one-sided rigidity theorem is sound.** That one-sided theorem has a short frame-map proof; include it independently in the blind packet rather than expect the referee to trust a repository link.

## B. Deliberate false inferences and countercontrols

1. **False:** Every Boolean-valued finite-compatible pair with a zero-valued infinite cover forces Q′. **Countercontrol:** completed branching Scott dcpo S, with D₂>D but W₂=W=S².
2. **False:** E_C is an arbitrary ambient regular open. It is **regular in O(W₂)**; \(\rho_C\in Q\) can have different absolute regularity.
3. **False:** D(K)∩E=0 alone implies its closure misses E. The proof must use the ambient open \(\rho_K\) and D(K)≤W₂(K).
4. **False:** The canonical reduction finds a minimal closed counterexample. It finds the least closed support of the **MARKED hole**. A different hole could have different support.
5. **False:** Taking the closed support commutes with the global \(\Phi\)-closure. Only the exhibited **lax** inequalities are available.
6. **Unproved:** That the existence of a jointly zero-reflecting M-valued pair and t_C=0 implies a contradiction, or that its associated Boolean sublocale must contain a nonzero relatively open part of W₂. S shows the latter fails.
7. **Unproved:** Atomic/compact/regular/hyperconnected patch assertions involving unrefereed material may be promoted without a separate dependency audit.

## C. Requested external stress tests

Ask the external referee to:
- Prove or disprove the principal normal form **independently**, using only the blind packet.
- Pay particular attention to **relative** versus **ambient** sublocale operations; Isbell least dense Booleanization; inverse images of arbitrary meets; and closure in a closed sublocale.
- Test both the **strong** marked open E construction and the **weak** T_C construction: are the two normalization hypotheses really different, and is exact persistence true only for the strong one?
- Audit the **one-sided closed compact/regular** fitting-rigidity lemma, used in one hereditary sufficient condition.
- Check the nonzero support K and the proof that \(\rho_K\) is still a full-pre-nucleus witness WITHOUT claiming \(q(\rho)=w_{C_K}\to d_{W_2(K)}\).
- Check the claimed **absorption** \(t_C\vee h_{\rm hc}\vee h_{\rm cc}\le e_C\), taking h_hc/h_cc as *conditional imports* if unwilling to re-prove them.
- Provide corrections or counterexamples if any logical step is invalid. A negative audit is useful.

## D. Audit classification and publication readiness

| Item | Internal verdict | External dependency |
|---|---|---|
| A1 relative pre-nucleus hole / regular-open E | Pass | Previously corroborated fixed-point framework |
| A2 B(E) Boolean witness and zero match | Pass | Standard Isbell fact; pointfree density |
| A3 e_C projection-right-adjoint support formula | Pass | Standard frame adjunction |
| A4 exact same marked E after closed reduction | Pass, highest scrutiny priority | Closed heredity of D/D₂ |
| A5 t_{C_K}=0 and idempotent marked support | Pass | A2–A4 |
| A6 safe patch absorption | Pass conditional | Earlier strip theorems |
| A7 lax naturality | Pass | Standard Heyting inequality |
| A8 weak D₂>D normalization | Pass after explicit complement argument | Closed complement pullback |
| A9 hereditary stronger D₂=D classes | Conditional pass | One-sided closed compact/regular rigidity |

**Internal conclusion:** Mathematical content appears correct on targeted adversarial review, with several precision repairs now incorporated in the working note. No universal answer to Q′ is claimed. **Do not send this internal audit to a blind referee before they finish their own review.**
