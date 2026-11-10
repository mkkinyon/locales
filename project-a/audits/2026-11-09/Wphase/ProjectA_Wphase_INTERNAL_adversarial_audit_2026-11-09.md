# Project A — Internal adversarial audit of the 9 November W programme

**Date:** 9 November 2026  
**Audience:** internal only. **Do not send this document to the blind external referee.**  
**Verdict:** **qualified internal PASS on the main chain**, conditional on the independently established earlier project inputs identified below. No fatal flaw found in the connected product example, finite-Alexandrov product theorem, compact two-apex shrinking calculation, finite-branch theorem, or fitted-supplement criterion. This is not an external verification or a novelty assessment.

## 1. Scope and dependency hierarchy

The work audited spans the 9 November notes on (a) Boolean-valued interpretations of W, (b) coherent W=H/maximal-specialization geometry, (c) relative fitness in F, (d) the two-apex shrinking construction, (e) the all-frame finite-branch theorem and its multiray tests, (f) H∧U and fitted supplements, (g) the scattered-factor product, and (h) the stronger **connected** example with finite-Alexandrov product formula. Exact canonical source links are in §7.

The proof chain with greatest risk is:

**Previously reviewed two-apex W/U calculation → newly derived two-apex W=H by shrinking → arbitrary-Y finite-poset W-product theorem → fitted propagation for W(P×Y) → pointwise U-product formula for locally compact sober factors → connected strict diamond.**

This is where the blind external referee should spend the most effort. Auditing only the finite fence and treating sublocale products as sets of ordinary points would miss the central risks.

## 2. Adversarial findings on the main chain

### A. Two-apex space and the shrinking proof — PASS (working)

Use the *cofinite entire half-line* neighborhoods, **not** eventual tails:

\[
N_+(F)=\{p_+\}\cup((0,\infty)\setminus F),\qquad
N_-(G)=\{p_-\}\cup(( -\infty,0)\setminus G),\quad F,G\text{ finite}.
\]

These are genuine opens. The space is compact, T₁, locally compact and sober. The previous audited computation gives
\[
W(Y)=K=A_+^2\cup A_-^2,\qquad
A_+=[0,\infty)\cup\{p_+\},\quad A_-=(-\infty,0]\cup\{p_-\},
\]
with complementary open \(d_W=(u_+\boxtimes u_-)\vee(u_-\boxtimes u_+)\), and \(W<U<F=Y^2\).

I checked the following vulnerable points independently:

1. For \(a_n=(0,1/n)\), \(\overline{a_n}=[0,1/n]\cup\{p_+\}\), hence \(\bigcap_n\overline{a_n}=\{0,p_+\}\), disjoint from \(a_1\). Consequently \(\bigcap_n O(a_n)=0\) *as sublocales*: a hypothetical sublocale lies in every closed \(\overline{a_n}\) but also inside \(O(a_1)\), which is disjoint from their intersection. Similarly for the negative intervals. The proof does not require point-determination of arbitrary sublocales.
2. \(C^+_n=[1/n,\infty)\cup\{p_+\}\) and \(C^-_n=(-\infty,-1/n]\cup\{p_-\}\) are **closed**; their complements contain appropriate apex neighborhoods. Thus \(w_{+,n}=Y^2\setminus(C^+_n\times C^-_n)\) is an open neighborhood of K.
3. The restriction identity
   \[
   (u_+\boxtimes u_-)\wedge w_{+,n}
    =(a_n\boxtimes u_-)\vee(u_+\boxtimes b_n)
   \]
   is an equality **of frame opens**, not merely point sets.
4. If the fitted residual on this sector is nonzero, Booleanizing it produces two decreasing Boolean sequences of meet zero whose pairwise joins are all top, an impossibility. The other sector is symmetric. No reliance on ordinary-point density is hidden here.
5. Each continuous real-valued function is constant: continuity at \(p_+\) forces constancy on the positive ray, at \(p_-\) on the negative ray, and at 0 equates constants.

Thus the new conclusion \(W(Y)=H(Y)=K<U(Y)<F(Y)\) survives this internal audit. The **actual computation W(Y)=K** is an inherited previously reviewed input, not silently re-proved by the shrinking test.

### B. Finite-branch shrinking — PASS; simplify proof

The lattice of sublocales is a **coframe**. For finitely many decreasing towers \(S_{j,n}\),
\[
\bigwedge_n\bigvee_{j=1}^m S_{j,n}
=\bigvee_{j=1}^m\bigwedge_n S_{j,n}.
\]
The right-hand side vanishes if all branches vanish. The direct two-branch proof fixes \(k\), distributes \(A_k\vee\bigwedge_{n\ge k}B_n\), then takes the meet over k. This is shorter and conceptually more honest than the Boolean-valued proof. Finite branch width is essential; the countably infinite eventually-zero branches in the two-element Boolean algebra give a counterexample to infinite-width interchange.

The star-exhaustion condition \(r_1\le\bigvee_n r_n^*\) indeed implies \(\bigwedge_n O(r_n)=0\); restricting the condition to a hypothetical nonzero intersection gives a contradiction. The arbitrary sector cover is legitimate via the **special open restriction identity**
\[
S\wedge O(\bigvee_i t_i)=\bigvee_i(S\wedge O(t_i)),
\]
which holds because open sublocales inside S preserve joins. **Do not invoke coframe distributivity alone** to justify this arbitrary join formula.

### C. Finite-Alexandrov product theorem — PASS, with a nonoptional section argument

For P finite upper-Alexandrov and arbitrary frame L, \(\mathcal O(P\times Y)\) is the frame of monotone sections \((v_p)_{p\in P}\in L^P\). The decomposition \(v=\bigvee_p(\uparrow p\boxtimes v_p)\) and the coproduct relations establish the isomorphism without assuming Y spatial.

**Upper bound:** lax naturality of W under the projections gives
\[
W(P\times Y)\le W(P)\times W(Y).
\]
This lax naturality follows directly by pulling back every diagonal cover, then taking a closed hull.

**Lower bound:** if p,q share t≤p,q, then for every cover \(\mathcal C\) of P×Y, its t-sections cover Y and
\[
\bigvee_{c\in\mathcal C}c_p\boxtimes c_q\ \ge\
\bigvee_{c\in\mathcal C}c_t\boxtimes c_t.
\]
Therefore the slice image of D(Y) at (p,q) factors through D(P×Y). Its closed image is \((\downarrow p\times\downarrow q)\times W(Y)\). This latter identity is **not a pointwise inference**: the largest monotone open disjoint from the slice has section \(d_{W(Y)}\) on positions below (p,q), and top elsewhere. Taking all common-lower pairs and their finite closed union yields \(W(P)\times W(Y)\). Thus
\[
\boxed{W(P\times Y)=W(P)\times W(Y)}
\]
for every locale Y. The finite hypothesis on P must remain explicit.

As a finite shadow check, I enumerated 219 labeled four-point partial orders and 19 labeled three-point partial orders and compared the relation formula on **all 4,161 products**. There were zero disagreements. This is corroborative only; the arbitrary-locale proof is the frame-level argument above.

### D. Fitted-hull propagation and connected diamond — PASS after a wording correction

The original first draft wrongly called \(B=U(P)\) an **upset**. It is a **closed downset whose upward saturation is all P²**; that correction has already been committed to the source. Calling it an upset would make the lemma nonsensical, since \(U(P)\ne P²\).

With \(J=P²\), \(M=\mathcal O(Y²)\), and fitted \(K=\bigcap_iO_M(v_i)\), the constant-section open \(\widehat v_i\) acts on the monotone-section frame by
\[
(\widehat v_i\to x)_t=v_i\to_M x_t.
\]
Hence \(J\times K=\bigcap_i O_{\operatorname{Up}(J,M)}(\widehat v_i)\) is fitted. This **explicit sectionwise argument**, now inserted in the source, avoids an unproved blanket assertion about pulling back arbitrary meets of sublocales.

If an open neighborhood w contains \(U(P)\times K\), every section indexed by s∈U(P) contains K. Monotonicity and \(\uparrow U(P)=P²\) force **every** section to contain K. Therefore
\[
\operatorname{fit}(U(P)\times K)=P²\times K,
\quad H(P\times Y)=P²\times K
\]
when K=W(Y)=H(Y) is closed and fitted. The argument does **not** assume arbitrary sublocales of Y² are spatial.

For P the five-point fence, direct enumeration gives \(|\mathrm{Cm}(P)|=17\), \(|I(P)|=15\), \(|U(P)|=23\) out of 25, missing just (m,n),(n,m); \(V(P)=H(P)=P²\), and \(\uparrow U(P)=P²\). For the two-apex Y, basic-product neighborhood closure gives \(U(P\times Y)=U(P)\times U(Y)\), as a **closed sublocale of the spatial square** (P×Y is locally compact sober). Thus
\[
W(Z)=U(P)\times K=H(Z)\wedge U(Z),\quad
H(Z)=P²\times K,\quad U(Z)=U(P)\times U(Y).
\]
H and U are incomparable by the explicit ordinary-point witnesses, and both strictly contain W. Real-valued functions on Z are constant, so F(Z)=Z²; a witness outside both H and U proves their **finite closed join** strictly below F.

**Topology:** P is connected (comparison graph connected). Y is connected (the ordinary real line is dense); so Z=P×Y is connected. Compactness, local compactness, sobriety and noncoherence are checked directly; the compact-open nonbasis argument uses projection of a hypothetical compact-open subset of P×J to a nonempty compact-open subset of an ordinary bounded real interval J, which is impossible.

## 3. Other W-programme results — scoped checks

- **Boolean full-cover witness interpretation:** the construction using nonzero \(D\wedge O(a\boxtimes b)\) and double-negation Booleanization is correct. This characterizes rectangles meeting W without replacing W by its ordinary point set.
- **Coherent W=H criterion:** coherent W=U plus spectral closed-sublocale fittedness and the patch-closed comparability-connectivity description of F give \(W=H\iff U=F\). The maximal-specialization/common-lower criterion follows using patch compactness and the coherent identity \(U=I\circ I\). The critical latter identity is an **inherited** antecedent and should be independently checked in the external packet if the referee is willing.
- **Relative fitness:** if T is fitted and S⊆T, fitting S intrinsically in T coincides with its ambient fitting, as both use restrictions of the same ambient open sublocales. Relative rather-below generation in F is sufficient; absolute rather-below generation is too strong and would force W=U. Distinguish these statements carefully.
- **Finite m-ray, m-apex family:** the topology, closed sectors, U point relation, D exclusion on mixed sectors and width-two shrinking identities are consistent. The sobriety proof should be written fully for publication; it is not enough to claim the entire square's sublocales spatial, only its **closed** sublocales are point-determined and the shrinking proof deals with the rest.
- **Fitted supplements:** the equivalence \(W=H\wedge U\iff\exists r\le d_W\ (d_W=d_U\vee r\ \&\ C(r)\text{ fitted})\) follows directly from minimality of H. Arbitrary families of barriers may be joined on the complementary-open side, because their closed fitted sublocales meet. The exact Boolean obstruction is a reformulation, not a solved classification.
- **Stage re-entry:** the five-point upper-Alexandrov calculation is correct for *arbitrary closed S,U₀*, not a specific diagonal counterexample. The source correctly distinguishes this limitation.

## 4. Risks and repairs before treating these as reviewed theorems

1. **Do not generalize the finite-Alexandrov product formula to arbitrary locale products.** Finiteness is used in the section calculus and closed finite union. In the source, make the sectionwise fittedness argument explicit (done) and maintain the corrected 'closed downset B' wording (done).
2. **Blind-referee dependencies:** Give the complete two-apex K/W/U computation rather than quoting its conclusion; likewise require a genuine locale-map proof of the fixed-slice image closure and of the fitted propagation. The referee must be free to challenge the October antecedents.
3. **Do not conflate spatiality of the square with spatiality of all its sublocales.** This is essential in the connected example. The separate scattered-factor argument may use the latter only because of the scattered-sublocale theorem.
4. **The m-apex family is independently new working work:** its pointwise U description and frame-level use of the regular core deserve a closer external check; no universal all-m theorem should be added to the externally certified ledger yet.
5. **Priority is unverified.** The all-frame finite-branch identity is standard coframe distributivity; the original Boolean derivation is valid but not the conceptual novelty. No claim of originality for the algebraic criterion before literature review.
6. **No Q/Q′ work:** neither finite-cover approximation question was tested or resolved by this segment. Their statuses remain **OPEN, DEFERRED**.

## 5. Audit verdict and action

**The central connected strict-diamond theorem provisionally survives internal adversarial review.** The two highest-risk uses of localic structure have genuine frame-level proofs. One incorrect lemma hypothesis was repaired in the source during this audit; the finite-product fittedness step now has a detailed sectionwise argument. No other definite error was found in the core chain.

**Recommendation:** Send a **blind external audit** now, with a self-contained prompt and mathematical packet covering the whole recent W investigation. Do **not** send this internal report, the earlier Q′ referee report, or the previous external audit reconciliations. Instruct the referee to check all statements including side remarks, and to separately label any attempted research suggestions. Consolidate to the theorem ledger *after* the external verdict; no new construction programme before then.

## 6. Published facts used but not claimed as new

- Sublocale lattices are coframes, and finite closed joins remain closed: standard treatments by Picado–Pultr and later work.
- Sublocales of a spatial scattered locale are spatial: established scattered-sublocale results attributed in the earlier Project A audits to Simmons, with discussions in Suarez.
- The coherent spectral/Priestley representation and localization of localic products for locally compact sober factors.

The external referee may use standard references independently; it should not assume our summaries of them are correct.

## 7. Canonical repository note index

All links have prefix `https://github.com/mkkinyon/locales/blob/main/`:

1. `A-W-as-Boolean-cover-relation-and-lax-naturality-2026-11-09.md`
2. `A-W-equals-H-coherent-maximal-point-criterion-2026-11-09.md`
3. `A-W-equals-H-relative-fitness-functional-envelope-2026-11-09.md`
4. `A-W-equals-H-compact-two-apex-telescope-2026-11-09.md`
5. `A-W-equals-H-abstract-finite-branch-shrinking-2026-11-09.md`
6. `A-W-equals-H-finite-star-testing-shrinking-2026-11-09.md`
7. `A-W-H-meet-U-fitted-supplements-and-higher-stage-obstruction-2026-11-09.md`
8. `A-W-HmeetU-product-transfer-nondisjoint-example-2026-11-09.md`
9. `A-W-HmeetU-connected-example-finite-poset-product-2026-11-09.md`