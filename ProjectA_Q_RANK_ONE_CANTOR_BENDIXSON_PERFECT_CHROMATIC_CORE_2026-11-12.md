# Project A — Q chromatic frontier: one-sided Cantor–Bendixson rigidity

**12 November 2026 — NEW INTERNAL theorem, not externally audited and without novelty/priority check.** This is a bounded next segment on the SAME rank-one Q obstruction and the SAME chromatic frontier after [the chromatically local finiteization and compact/regular frontier theorem](ProjectA_Q_CHROMATIC_LOCAL_FINITE_AND_COMPACT_FRONTIERS_2026-11-12.md). The specific extra result is that, whenever the closed chromatic frontier admits a **spatial T₁ presentation**, *all weak fitting defects and all strong Urysohn-hole defects are forced onto its ordinary Cantor–Bendixson PERFECT kernel*. Scattered T₁ frontiers are impossible even if neither compact nor regular. More generally, a compact or regular perfect kernel is enough to exclude the defect.

This is NOT a proof of universal Q or Q′, nor a claim that every chromatic frontier is spatial T₁. The argument works for arbitrary ambient locales X but requires that the stated CLOSED coordinate sublocale H be spatial T₁ (hence all its closed sublocales are represented by actual closed T₁ subspaces).

## 0. Background

Let L=O(X), Q=L⊕L, \(\mathcal D=\bigwedge_{\mathcal C}\mathfrak o(w_\mathcal C)\), and \(\mathcal D_2\) the meet over finite covers. A generalized pair is a pair of frame maps \(h,k:L\to M\), viewed as a map into X². The pair belongs to D₂ iff it matches all finite covers, and belongs to D iff it matches ALL covers. An arbitrary C matches to \(u_C=\bigvee_{c\in C}h(c)\wedge k(c)\). Restricting the target to the **closed** quotient \(\mathfrak c_M(u_C)\) produces a nonzero pair with **C-matching zero** whenever \(u_C<1_M\), while preserving all finite compatibility.

Previously proved and independently audited (through the 12 November pre-nucleus blind packet and frontier addendum): if J↪X is a **closed compact** sublocale, any finite-compatible pair whose ONE endpoint factors through J is compatible with ALL covers. The same holds for closed regular J. The proof here imports only these one-sided theorems, not the previous geometric counterexamples.

For a spatial T₁ space H, put \(H^{(0)}=H\), \(H^{(\alpha+1)}=H^{(\alpha)}\setminus\operatorname{Iso}(H^{(\alpha)})\), and at limits \(H^{(\lambda)}=\bigcap_{\alpha<\lambda}H^{(\alpha)}\). These are decreasing CLOSED subsets. Eventually the sequence stabilizes at a CLOSED **perfect kernel** \(P(H)\), which has no isolated points. H is **scattered** iff \(P(H)=\varnothing\). This classical Cantor–Bendixson construction is not new.

## 1. One-sided zero-cover support reaches the perfect kernel

**Theorem 1.1 (Cantor–Bendixson zero-cover localization, NEW INTERNAL).**
Let \(i:H\hookrightarrow X\) be a closed sublocale, where H is represented by a spatial T₁ space. Let \(h,k:O(X)\to M\) be an arbitrary generalized pair into a NONZERO frame M such that:
\[
\bigvee_{c\in F}h(c)\wedge k(c)=1_M \quad\text{for every FINITE X-cover }F,
\tag{1.1}
\]
and for ONE arbitrary X-cover C
\[
\bigvee_{c\in C}h(c)\wedge k(c)=0_M,
\tag{1.2}
\]
with h factoring through H. Then h in fact factors through the CLOSED perfect kernel \(P(H)\hookrightarrow X\). No assumption that k factors through H is necessary.

*Proof (transfinite elimination).* Start with \(H^{(0)}=H\) and assume h factors through the closed \(H^{(\alpha)}\). Every isolated point p of \(H^{(\alpha)}\) determines an open singleton \(u_p=\{p\}\) in the spatial T₁ locale \(H^{(\alpha)}\). **Claim:** \(h_\alpha(u_p)=0_M\). Otherwise put \(m=h_\alpha(u_p)>0\) and restrict the target locale to the NONZERO open \(\mathfrak o_M(m)\). The restricted map sends \(u_p\) to the top m, so its first coordinate factors through the open sublocale \(\{p\}\hookrightarrow H^{(\alpha)}\). Since \(H^{(\alpha)}\) is T₁, this singleton is CLOSED in \(H^{(\alpha)}\), and since H and all derivatives are closed in X, the singleton is a CLOSED COMPACT sublocale of X. Finite compatibility and matching value zero for C survive target restriction (all cover equations are met with m). The previously proved one-sided compact rigidity theorem now contradicts (1.2). Thus the claim holds.

The open complement of \(H^{(\alpha+1)}\) in \(H^{(\alpha)}\) is the join of the opens \(u_p\), all killed by h; consequently h factors through \(H^{(\alpha+1)}\).

At a limit ordinal \(\lambda\), the earlier closed derivatives correspond to an increasing family of ambient defining opens \(e_\alpha\) (closed \(H^{(\alpha)}=\mathfrak c_X(e_\alpha)\)), all killed by h. Since h preserves arbitrary joins, \(h(\bigvee_{\alpha<\lambda}e_\alpha)=0\), so h factors through their closed intersection \(H^{(\lambda)}\).

At the stage where the derivatives stabilize, the factorization is through \(P(H)\). QED.

**Stronger formulation (no target Booleanization).** The proof uses only arbitrary frame target M and finite-cover compatibility. It never assumes spatiality of X, X², or M. Spatiality and T₁ apply ONLY to the closed coordinate sublocale H.

**Corollary 1.2 (one-sided scattered rigidity).** If H is a closed **scattered T₁ spatial** sublocale of X, then
\[
\boxed{\mathcal D_2(X)\wedge(H\times X)=\mathcal D(X)\wedge(H\times X),}
\tag{1.3}
\]
and symmetrically for X×H.

*Proof.* If the inclusion failed, choose a cover C for which the finite-compatible sublocale \(T=\mathcal D_2(X)\wedge(H\times X)\wedge\mathfrak c_{X^2}(w_C)\) is nonzero. The induced coordinate maps into O(T) satisfy (1.1)–(1.2), with first coordinate factoring through H. Theorem 1.1 forces the first coordinate through \(P(H)=0\), contradiction with target nonzero. The existence of nonzero T uses the elementary fact that the CLOSED complement of a restricted OPEN equals zero exactly if the restricted open is top; there is NO illegitimate distributivity over arbitrary sublocales. QED.

**Corollary 1.3 (compact/regular perfect kernel).** If H is closed spatial T₁ and its perfect kernel \(P(H)\) is **compact or regular as a closed locale**, then the same one-sided equality (1.3) holds. For any zero-C defect, Theorem 1.1 localizes the first coordinate to \(P(H)\), and the independently audited one-sided compact/regular rigidity theorem then forces C compatibility, contradiction.

This is not a disguised claim that H itself is compact/regular: H can be noncompact, nonregular and still have a compact or regular perfect kernel.

## 2. Exact localic weak-defect containment

**Theorem 2.1 (point-free sublocale containment).** Under Theorem 1.1's assumptions on the closed sublocale H, for every arbitrary X-cover C,
\[
\boxed{
\mathcal D_2(X)\wedge(H\times X)\wedge\mathfrak c_{X^2}(w_C)
\ \le\ P(H)\times X.
}
\tag{2.1}
\]
*Proof.* Take the generalized locale
\(T=\mathcal D_2\wedge(H\times X)\wedge\mathfrak c(w_C)\) itself as target of its two projections. Its matching value for finite covers is top, its C matching is bottom, and its first coordinate factors through H. Theorem 1.1 factors that same projection through P(H). Consequently the inclusion of T in X² factors through the closed P(H)×X, proving the sublocale inclusion. □

If H is compact or regular itself, the older one-sided theorem makes the left side zero. The new theorem replaces H by P(H), which can be strictly smaller even when H is neither compact nor regular. All computations are point-free *after* the spatial T₁ closed coordinate kernel is supplied.

## 3. Application to the rank-one chromatic frontier

Keep the prior construction:
\[
z_1=d_{\mathcal U}=\Phi(0)=\Phi_2(0),\qquad
\mathcal U=\mathfrak c(z_1).
\]
For a cover C and rectangle \(r=a\boxtimes b\) with
\[
r\wedge w_C\le z_1,
\tag{3.1}
\]
let \(\Gamma_r(C)\) be its actual **localic U-linked graph**, let \(\mathscr J_r\) be the ideal of its finite-chromatic induced vertex subsets, and put
\[
\eta_{C,r}=\bigvee_{A\in\mathscr J_r}
\left(\bigvee(C\setminus A)\right)^*,\qquad
H^\chi_{C,r}=\mathfrak c_X(\eta_{C,r}).
\tag{3.2}
\]
The earlier local finite-colouring theorem states, WITHOUT finite fixedness,
\[
r\wedge(\eta_{C,r}\boxtimes1)\le\Phi_2(z_1),\qquad
r\wedge(1\boxtimes\eta_{C,r})\le\Phi_2(z_1).
\tag{3.3}
\]

**Theorem 3.1 (perfect-kernel obstruction for Q, NEW INTERNAL).** Assume \(\Phi_2(z_1)=z_1\) and suppose \(r\not\le z_1\) while (3.1) holds. Then
\[
E_r=\mathcal U\wedge\mathfrak o(r)\ne0
\]
is a nonzero relatively OPEN Urysohn sublocale, disjoint from \(\mathfrak o(w_C)\). By (3.3) it is supported inside BOTH closed coordinate remainders:
\[
\boxed{E_r\le H^\chi_{C,r}\times H^\chi_{C,r}.}
\tag{3.4}
\]
If \(H^\chi_{C,r}\) is a **spatial T₁ closed sublocale**, then
\[
\boxed{E_r\le P(H^\chi_{C,r})\times P(H^\chi_{C,r}).}
\tag{3.5}
\]
In particular, if \(P(H^\chi_{C,r})\) is compact or regular (including the case that it is empty, i.e. Hχ scattered), then (3.1) forces \(r\le z_1\). So such a rectangle CANNOT witness Q failure.

*Proof.* Set H=Hχ. The finite-fixedness and (3.1) make E_r disjoint from the two \(\eta\)-coordinate strips; hence (3.4). As in the first-step relative pre-nucleus theorem, B(E_r) is a nonzero dense Boolean sublocale of E_r, contained in D₂ because **every finite diagonal square is dense in U** under finite fixedness. Also \(E_r\wedge O(w_C)=0\), so it lies in \(\mathfrak c(w_C)\), in the sublocale sense. Hence
\[
B(E_r)\le\mathcal D_2\wedge(H\times X)\wedge\mathfrak c(w_C).
\]
Theorem 2.1 gives \(B(E_r)\le P(H)\times X\). Since P(H)×X is CLOSED and B(E_r) is DENSE in E_r, \(E_r\le P(H)\times X\). By symmetry apply the second-coordinate version and obtain (3.5). If P(H) compact/regular, one-sided rigidity contradicts \(B(E_r)\ne0\) and its C zero value, hence E_r=0; thus \(r\le z_1\). □

**Strong scope warning.** This does NOT claim Q is inherited by the closed P(H): the argument localizes the marked hole and its Boolean witness inside X². We do not apply the rank-one fixed-point hypothesis to the smaller locale. No equality \(\Phi_{2,P(H)}(z_1^{P(H)})=z_1^{P(H)}\) is asserted.

**Corollary 3.2 (spatial T₁ condition on the frontier).** For a locally compact sober T₁ space X (or any X for which the specific closed Hχ is spatial T₁), a hypothetical Q counterexample must have a **nonempty perfect closed chromatic kernel** \(P(H^\chi_{C,r})\) which is **neither compact nor regular** and supports the ENTIRE marked open Urysohn hole in both coordinates.

This is more precise than saying "Hχ is neither compact nor regular." A chromatic remainder with a scattered, compact, or regular perfect core is harmless even when its full closed remainder has those bad global properties.

## 4. What is and is not gained

The constructive content is a general ONE-SIDED rigidity theorem on scattered T₁ closed sublocales, and the exact containment (2.1) onto a classical perfect kernel. No far-generation is needed for these theorems; their specialization to Q uses the **already established** rank-one open-hole localization and finite-chromatic frontier.

This is an honest additional POSITIVE class:
\[
\boxed{P(H^\chi_{C,r})\text{ compact OR regular}
\ \Rightarrow\text{no rank-one hole on }r,}
\]
under the stated spatial T₁ condition. It excludes noncompact nonregular frontiers whose only obstruction comes from removable scattered strata, instead of introducing more ad hoc cover obstructions.

A simple strictness control: let Y be the compact T₁ scattered nonregular two-limit space with isolated points n∈ω and two distinct limit points p,q, both having cofinite neighborhoods on the isolated points. Then
\[
H=[0,1]\sqcup\bigsqcup_{n\in\omega}Y_n
\]
is T₁, noncompact, nonregular, and its perfect kernel is the compact regular interval [0,1]. The new perfect-kernel criterion applies to this H whereas the earlier global “H is compact or regular” criterion does not. **This is a control of the abstract one-sided theorem, not a claim that this particular H arises as a Q chromatic frontier.**

**Negative control:** The completed branching Scott locales that realize \(\mathcal D_2>\mathcal D\) without Q/Q′ failure are NOT T₁; they do not refute the theorem. No hypothetical perfect T₁ noncompact nonregular chromatic frontier is constructed here.

**Classical terminology:** The Cantor–Bendixson derivative and its stable perfect kernel are standard. A concise reference is the scattered-space entry at https://topology.pi-base.org/properties/P000051 and an explicit transfinite definition at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2476CB7A112975F78C2CB2355600D2C0/S2050509422000238a.pdf/invariant_ideal_axiom.pdf . No claim of novelty for this general topology is made.

**STATUS: NEW INTERNAL PROOF ONLY; NOT EXTERNALLY AUDITED. UNIVERSAL Q, Q′ OPEN.**
