# Fourth audit — final reconciliation after blind reports, cross-review and internal-audit comparisons

**11 November 2026 · Consolidated audit verdict.** This document reconciles **two separately blind original reviews**, **two independent cross-checks of the other referee's post-verdict results**, **the pre-existing internal adversarial report**, and **two nonblind internal-audit comparisons**. Do not describe the whole exercise as a formal proof check, a fresh verification of pre-existing premises P1–P6, or a full priority review. The original reports, prompts, and supplements must remain unmodified. Companion corrected theorem accounts: [binary meet-hull canonical addendum](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md) and [relative-gluing/twisted canonical addendum](PointFree_relative_gluing_twisted_CANONICAL_2026-11-11.md).

## 1. Claim-by-claim disposition

**Original blinded A/B package:** A1–A4, B1–B4, R1–R3 all survived independent review **relative to the explicitly given earlier premises and named classical inputs**, with two minor proof additions and scope/bibliographic repairs. This includes relative Stone-indexed lower-ideal gluing (WR sufficient), torus non-suspension and nonconstant examples, derived relative-chain splitting, acyclic aspherical nonconstant examples, finite-rank monodromy blindness, folded H¹ and intrinsic coefficient nonconstancy, referee-origin free condensed group identifications and pointed fitted-side gluing. The internal report's historical false aside “all finite pairs yield nonconstant gluing for infinite S” had already been removed from the blind submission.

**Original blinded C package:** C1, C2a,b, C3, C4, C5a–d, C6, C7a,b, C8a,b and C9 all survived independent review relative to P1–P6. The C referee supplied explicit finite controls through seven-point posets for several binary/π₁ claims, complete checks of stated Hasse signatures and rank, and independent group-theoretic computations; none replaces the general proof. Five small proof omissions G1–G5 and seven scope issues S1–S7 were recorded and require text repairs.

**Opposite-referee cross-checks:** (i) C's new \(\mathrm{Ch}_\bullet\to M_\bullet=I_\bullet\cap D_\bullet\) groupoid theorem and 2-connectivity theorem were independently assessed and accepted by A/B, which supplied an \(\infty\)-topos realization-connectivity proof; (ii) A/B's new finite-pair gluing constancy iff acyclicity theorem was independently assessed and accepted by C with six small repairs. These post-verdict statements have **independent cross-checks**, unlike additions made in the final nonblind comparisons.

**Internal-audit comparisons:** Both referees report agreement on every original numbered claim. C correctly distinguishes its original C9 proof (invariance using two orders) from the stronger *new* meet-hull proof (intrinsic patched model). A/B corrects several overcautious scope statements and supplies a new strengthening of B4 for finite groups. Neither comparison uncovered a fatal error. Several open bibliography items remain open and should not be silently certified.

## 2. Main improvements to the mathematics

### 2.1 The sharp patched binary reconstruction statement

For coherent X put \(M_n(X)=I_n(X)\cap D_n(X)\). The local witness formula
\[
(x,y)\longmapsto[x,u][y,u]^{-1}=[a,x]^{-1}[a,y]\qquad(a\le x,y\le u)
\]
descends to an inverse of the chain-to-meet internal edge-path groupoid functor. The M₂ triangle \((x,y,u)\) verifies the inverse composite. This is over \(h(X_{\rm patch})\) and commutes strictly with both hull functors. It **supersedes the paired-extrema proof as the preferred presentation**, without making that earlier independently audited proof false. Since simplicial-vertex neighborhoods of binary I and D recover all patched I_n and D_n for coherent X (C6), isomorphisms of patched binary pairs determine the chain 1-type and its canonical comparisons on 1-types.

**Exact functoriality:** the intrinsic groupoid model is natural for patch-continuous maps preserving \(M_1\) and \(M_2\). It is **not** natural for arbitrary maps preserving only I₁ and D₁; a nine-point target with private upper and lower witnesses for each of three pairs gives a counterexample. The recovered object is *patched sheaf homotopy*, not intrinsic localic shape. Full chain nerves, spectral orders and 2-types need not be reconstructed.

### 2.2 A new sharp 2-connectivity theorem

\[
\mathbf C(X)\to\left|h(M_\bullet(X))\right|
\quad\text{is **2-connective** (}\pi_0,\pi_1\text{ iso; }\pi_2\text{ epi).}
\]
The proof uses the lower-witness double Čech resolution: at auxiliary degree j=0 the canonical Ch→I comparison is an equivalence by inserting the lower witness; at every j it is 1-connective. The shifted realization-connectivity lemma in an \(\infty\)-topos, proved by semisimplicial skeletal pushouts and iterated codiagonals, gives degree 2. This does not require hypercompleteness. The six-point ordinal sum of three two-antichains has C≈S² and M≈1, so the bound cannot improve to 3-connectivity. **Do not call this a 2-equivalence** or claim that the undetermined 2-type is classified just by the kernel of \(\pi_2\); the \(\pi_1\)-action and k-invariant remain.

### 2.3 Exact constancy criterion for relative gluing

Let \(\varnothing\ne K\subseteq T\) be a **finite** simplicial pair and \(S\ne\varnothing\) Stone. Set
\[
E_{T,K}(S)=\underline{|K|}\amalg_{h(S)\times\underline{|K|}}
 \big(h(S)\times\underline{|T|}\big).
\]
If \(f:|K|\to|T|\) is a homotopy epimorphism (equivalently every homotopy fibre is **nonempty and acyclic**), then the canonical fold \(E\to\underline{|T|}\) is an equivalence for **any** nonempty S. If S is **infinite**, the converse holds even if E is only assumed abstractly constant. Hence for infinite S, “constant,” “fold equivalence” and “f homotopy epimorphism/acyclic” are equivalent. Finite S always gives a constant gluing object. The forward implication does not require finite K,T; the converse proof uses their finiteness for internal relative mapping objects. The key is *homotopies under K*, not merely free homotopies. Acyclic **map** is much stronger than integral homology isomorphism. Background: Raptis, *Some characterizations of acyclic maps* (2019), Theorem 2.1(a), https://arxiv.org/abs/1711.08898. This sharpens the earlier historical warning that not every finite pair gives nonconstant E.

### 2.4 New final-round strengthening of twisted H¹: finite groups included

A/B's nonblind comparison extends original B4 to **every nontrivial discrete group G**, with an elementary new argument. This **extension was not a claim in the original blind packet and has not been independently cross-refereed**; it has been internally checked here and is recorded separately from the externally blind-checked original B4.

Let S infinite, Γ=∗_{s∈S_set}G, choose 1≠g∈G and t≠u∈S. For the original B4 derivation family, if d_t−d_u were principal with coefficient a∈Z[Γ], choose s outside {t,u} and outside all free factors occurring in the finite support of a. Put
\[
\Delta=(g_t-g_u)(g_s-1),\qquad y=\Delta-a.
\]
The relation on the s-factor says \((x_s-1)y=0\) for every \(x\in G\); it forces all coefficients of y to be constant along left G_s-orbits. But the coefficient of y at the reduced word \(g_tg_s\) is +1, whereas the coefficient at \(x_sg_tg_s\), for any \(x\ne1\), is 0: it begins with an s-letter and lies neither in the four-term support of Δ nor in supp(a). Contradiction. No infinite order is needed. Therefore both intrinsic \(\mathcal H^1(\Pi;J_\Pi)\) and \(\mathcal H^1(\Pi;\mathbb Z[\Pi])\) are nonconstant for infinite S and **any nontrivial G**. The original infinite-order statement remains externally blind-checked; this weakening of the hypothesis is **post-comparison internally checked only**.

## 3. Final issue ledger and necessary editorial fixes

1. **A1/WR:** the upper-witness-reflection hypothesis is *exactly* what ensures the particular degreewise I-hull identification over the shared lower ideal, but **only sufficient**, not necessary, for the final canonical comparison to be an equivalence. A/B provides a four-point diamond counterexample to necessity for equivalence. Without WR a corrected pushout remains available using \(I_n(P)\cap A^{n+1}\).
2. **Relative chains:** distinguish \(M_S=R[h(S)]\), \(J_S=\ker(M_S\to R)\), and the two different relative objects \(C(E,K)\) and \(C(E,T_{s_0})\); retain derived tensor notation. The fold projection to C(T) is canonical, complementary splitting depends on s₀.
3. **Nonconstant sheaves:** add the lemma that any constant homotopy/homology sheaf has finite-image sections over compact Stone bases, and state exactly how global basepoints are handled.
4. **Ordinary versus internal H¹:** define the internal cohomology sheaf as Der/PDer and justify by the section-object fibre sequence. Its value at * equals the **absolute H¹ of the sheaf-classifying object in this special topos**, because Γ=evaluation at * commutes with π₀; it does **not** generally equal ordinary group cohomology of Π(*) nor the naive presheaf value on arbitrary tests.
5. **Binary relation quotient:** define the normal subgroupoid quotient at presheaf level before sheafification; record surjective Stone witness covers, and use an interpolant rather than assuming a continuous least upper bound.
6. **C2/C3:** explicit injection of free modules under edge subobjects; justify nonconstancy of direct summands; prove no S²\Δ_S blocks by fibre-folding so all relation blocks are patch-closed.
7. **C4/C5/C8:** do not rely on naturality not listed among prior premises when avoidable. Specify diamond attachment **before** the S-wedge; preserve distinction between actual localic equalities within X and patched equality across different orders. Name binary words; compare precisely the *displayed* hierarchy pattern, not all possible relational identities. Do not infer sheaf homotopy conclusions from finite point evaluations alone.
8. **F2 proof wording:** auxiliary E_j orders are actually Priestley; local sections exist only after covering base change. Cite the realization lemma in the ∞-topos form with connectivity convention and proof; do not call M a fourth model canonically equivalent to C,I,D.
9. **B4:** finite-G improvement is **new post-comparison**, distinct provenance. Do not conflate the original packet proof (uses infinite-order cancellation) with this new support/orbit argument.
10. **Literature:** add classical upper/lower/double bound graph and bound-polysemy antecedents (C6 finite case is not new), Dowker duality, Okunev M-equivalence antecedent of R2, Dranishnikov–Rudyak for the Berstein–Schwarz square, Bieri–Eckmann for duality, Ebert–Randal-Williams/Kerodon for realization, and Raptis for acyclic/epi. Verify uncertain page and version-specific theorem numbers; avoid unsupported priority claims.
11. **Notation:** distinguish \(\mathcal M\) (binary meet) from \(M_n=I_n\cap D_n\) (higher meet hull), and use distinct symbols for the coefficient ring/module, Higman's group and the ambient Stone-sheaf \(\infty\)-topos. Keep the empty Stone test/empty cover convention and non-hypercomplete qualifications.

## 4. What is established, and what remains open

- **Externally blind-checked relative to earlier P-premises:** all original numbered A/B and C packet claims, after the documented repairs.
- **Externally cross-checked additions:** F1 (internal groupoid isomorphism), F2 (2-connectivity), and gluing constancy⇔acyclicity (finite pair, S infinite). The cross-reviewers had not seen each other's initial report.
- **New internally checked post-comparison result:** B4 without infinite-order assumption, for any nontrivial G. An additional referee read is appropriate if headline; not required for the original B4 certificate.
- **Still unsettled/not claimed:** arbitrary-locale unpatched versions, intrinsic localic shape, site-size independence, the full internal H¹ computation for intrinsic group-ring coefficients, general lower-ideal direct fitted-side descent (only sketch), nonfinite-pair converse to acyclic constancy, arbitrary binary-graph-map functoriality (indeed false), or determination of the chain 2-type (false). Priority review remains incomplete.
- **Workflow:** original reports and additions retain exact provenance. Publish corrected canonical theorem summaries, update the separate v2.2 addendum, preserve v2.1 unchanged for historical trace, and resume research only after that editorial consolidation.
