# Project A — Q′ independent-referee reconciliation and bounded follow-ups

**9 November 2026.** This is our post-referee reconciliation, not part of the independent report. The original referee report, blind packet, prompt, and separate internal audit are archived in [the audit directory](project-a/audits/2026-11-09/Qprime/README.md). The referee independently reported no false structural theorems or example conclusions in the packet, but several exposition gaps and three unchecked older items. We independently examined the proposed global upgrades and performed one bounded test of each optional research suggestion. **Q and Q′ remain OPEN.**

## 1. Status and provenance

Notation \(Q=L\oplus L\), \(\mathcal D=\operatorname{fit}(\Delta)\), \(\mathcal D_2\) finite-cover fitting, \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal W_2=\operatorname{cl}\mathcal D_2\), \(\mathcal U=C(d_{\mathcal U})\). Questions:
\[
(Q):\quad \mathcal W_2=\mathcal U\Longrightarrow\mathcal W=\mathcal U,
\qquad
(Q'):\quad \mathcal W_2=\mathcal W\quad\text{for every frame}.
\]
Q′ implies Q, but neither has been proved or disproved.

**Externally corroborated by the 9 November blind report:** diagonal cover and pre-nucleus presentation; \(\Phi(0)=\Phi_2(0)=d_{\mathcal U}\); exact disjoint-rectangle certificate for W<W₂; infinite chromatic obstruction and finite-directed-family reduction; cover-dependent rather-below strip localization; compact closed complement rectangle theorem; proper-over-regular locale map theorem with directed-join-preserving right adjoint; completely join-prime boundary theorem; compact-closed strip and Boolean residual criteria (within packet); C1–C7 examples as **carefully scoped** in packet, including identified repairable exposition gaps.

**Not newly checked by this referee:** hyperconnected-strip localization theorem; regular-closedness of U for *all* Alexandrov locales; the branching-factor variant of the two-apex control. Preserve their earlier working/provenance statuses.

**Editorial corrections required:** (i) cofinite-positive/cofinite-negative, not ordinary tail, definition of the compact two-apex space; (ii) the word “no finite subfamily covers”; (iii) explicit generic-pair justification of sublocale equality; (iv) closure restriction and density/rectangle tests; (v) \(\mathcal D_2\)-to-\(\mathcal D\) frame-homomorphism proof for Boolean completions; (vi) correct finite-cover Baire argument *inside each target interval* (especially C6); (vii) display the actual localic \(w\to d_{\mathcal U}\) computation for two-apex; (viii) spell out the correct boundary-closure condition in C6, which differs from C5.

The referee re-proved the **already recorded** universal regular-core inequality
\[
d_{\mathcal W}\le d_{\mathcal U}^{**},\qquad
\operatorname{cl}(\operatorname{int}\mathcal U)
\le\mathcal W\le\mathcal W_2\le\mathcal U.
\]
This is a useful independent short proof, **not** a newly discovered inclusion: it already appears in the October unified synthesis. The proof inducts on \(\Phi^\alpha(0)\wedge d_{\mathcal U}^*=0\). For a successor, any generating rectangle \(r=u\boxtimes v\le (w_{\mathcal C}\to x)\wedge d_{\mathcal U}^*\) has \(r\wedge w_{\mathcal C}=0\); partitioning \(\mathcal C\) shows \(u^*\vee v^*=1\), hence \(r\le d_{\mathcal U}\wedge d_{\mathcal U}^*=0\). The result localizes every potential W/W₂ gap to the nonregular Urysohn residual.

## 2. Independent check of the referee's C5/C6 *global* upgrade

The original packet only claimed
\[
\mathcal W\wedge O(\rho)=\mathcal W_2\wedge O(\rho)=
\mathcal U\wedge O(\rho),\quad \rho=A\boxtimes B,
\]
for the two-sheet constructions C5 (rational parameter and directed finite-set conditions) and C6 (irrational parameter and finite binary forcing conditions). The referee proposed the **global** equality W=W₂=U in both. We have checked the upgrade via a single parameter-footprint argument, independent of the referee's case-splitting.

Let \(R\) be the sheet parameter space: \(R=\mathbb Q\) in C5 and \(R=\mathbb R\setminus\mathbb Q\) in C6. Let \(Y=\mathbb Q\) in C5 and \(Y=\mathbb R\) in C6. The continuous parameter map \(\pi:X\to Y\) assigns each sheet point its parameter and each boundary point its rational center. (For C6 its codomain is \(\mathbb R\), not the irrational sheet parameter subspace.)

For \(u\in\mathcal O(X)\) let
\[
p(u)=\pi_R(u\cap A)\cup\pi_R(u\cap B)\in\mathcal O(R),
\]
where \(\pi_R\) denotes ordinary projection of sheet opens. Every nonzero u has \(p(u)\ne0\), and every boundary point included in u has a basic neighborhood whose sheet footprints contain a relative-open neighborhood of its rational center.

**Claim 2.1 — disjoint footprints are U-separated.** If \(p(u)\cap p(v)=\varnothing\), then \(u\boxtimes v\le d_{\mathcal U}\).

For C5, view \(p(u),p(v)\) as disjoint opens in regular \(Y=\mathbb Q\). For C6 define a real-open lift
\[
V_u=\bigcup\{J\in\mathcal O(\mathbb R):J\cap R\subseteq p(u)\}.
\]
Then \(V_u\cap R=p(u)\), and every sheet or boundary point in u maps into \(V_u\); hence \(u\le\pi^*(V_u)\). Likewise for v. The lifts \(V_u,V_v\) are disjoint: if they met in a nonempty real-open set, density of the irrationals would yield a point of \(p(u)\cap p(v)\). C5 has the same properties with \(V_u=p(u)\).

Since Y is regular, \(V_u=\bigvee\{J:\overline J\subseteq V_u\}\), and similarly for \(V_v\). Thus
\[
u\boxtimes v
=\bigvee_{J,K}\bigl(u\wedge\pi^*J\bigr)
               \boxtimes\bigl(v\wedge\pi^*K\bigr).
\]
For these J,K the closures of J,K in Y are disjoint. Continuity of \(\pi\) gives
\(\overline{\pi^{-1}J}\subseteq\pi^{-1}\overline J\), hence the two coordinate opens in each summand have disjoint closures in X and are far. Each summand is one of the generators of \(d_{\mathcal U}\); Claim 2.1 follows by **coproduct distributivity**, with no assumption that the localic square is spatial.

**Claim 2.2 — overlapping footprints force D-density.** Suppose \(p(u)\cap p(v)\ne\varnothing\). Pick sheet labels \(\sigma,\tau\in\{A,B\}\), a common sheet parameter and basic sheet opens over that parameter, with conditions s,t.

- C5: the condition poset Fin₊(N) is directed. Extend s,t to \(H=s\cup t\cup\{n\}\). If \(\sigma=\tau\), the shared sheet point \((q,H)\) is a diagonal point; if \(\sigma\ne\tau\), the two sheet points at q are fully cover-compatible because any cover element containing the boundary \(t_{q,n}\) contains both. Thus a **D point** is inside \(O(u\boxtimes v)\).
- C6: pick the finite conflict set E of the two binary conditions. The fully cover-compatible pair of maps \((\theta_\sigma,\gamma_E\theta_\tau)\) into \(\operatorname{RO}(R\times2^\mathbb N)\) sends \(u\boxtimes v\) to a nonzero value (the two condition cylinders overlap after the finite flip, and their parameter intervals overlap). This works for **any ordered pair of sheets**, including \(\sigma=\tau\). Factorization through D implies \(D\wedge O(u\boxtimes v)\ne0\).

Now every rectangle \(u\boxtimes v\) meeting U nontrivially has \(p(u)\cap p(v)\ne\varnothing\), by Claim 2.1; hence it meets D by Claim 2.2. Rectangles join-generate Q, so D is dense in U; therefore
\[
\boxed{\mathcal W(X)=\mathcal W_2(X)=\mathcal U(X)}
\quad\text{globally for both C5 and C6}.
\]
These are **newly upgraded working conclusions**, supported independently by the referee and by the footprint proof here. They do not imply global Q′.

## 3. Bounded test of suggestion 1: random/measure algebra

Let \(\mathbb B\) be the complete Boolean *measure algebra* of the fair-coin product probability space \(2^\mathbb N\), and \(\gamma_E\) the automorphism flipping the finite coordinate set E.

**Lemma 3.1 (finite-flip mixing).** For any \(b,c>0\) in \(\mathbb B\), some finite E satisfies
\[
b\wedge\gamma_E(c)>0.
\]
**Proof.** Represent b,c by positive-measure measurable sets. By the dyadic cylinder Lebesgue density theorem (equivalently martingale convergence), choose finite strings s,t of the SAME length N, with conditional densities of b on [s] and c on [t] both greater than \(3/4\). Let E be the indices where s and t differ. The flip maps [t] to [s] and preserves measure. Inside [s], the relative densities of b and \(\gamma_E(c)\) each exceed \(3/4\), so their intersection has positive relative measure. □

**Lemma 3.2 (no finite-color obstruction for independent labels).** For any infinite S⊆N and b>0, there exist distinct n,m∈S such that
\[
b\wedge[n=0]\wedge[m=1]>0.
\]
Indeed, if every such meet vanished, b would be supported (mod null) on the set of sequences whose bits on S are all equal; this set has product measure zero.

**Application to the C6 sheet template.** Let \(N=\mathcal O(R)\oplus\mathbb B\), \(R=\mathbb R\setminus\mathbb Q\), and \(M\) be its double-negation/Booleanization quotient. Define sheet maps
\[
H_\pm(U)=j\Bigl(\bigvee_{s\in P} U_s\boxtimes[\pm s]\Bigr),
\]
where \([s]\in\mathbb B\) is the equivalence class of the finite bit cylinder, \([{-}s]\) its bitwise complement, and j is the double-negation nucleus. The same condition-compatibility argument as for Cohen/Cantor shows H± preserve arbitrary joins and binary meets.

The mirrored pair retains finite-cover compatibility: for a finite cover and a nonzero target rectangle \(O\boxtimes b\), choose a finite cylinder [s] in which b has relative measure >\(7/8\). Apply Baire within the target interval O to get two distinct same-color boundary labels n,m outside dom(s), with overlapping local intervals. The intersection with \([s]\wedge[n=0]\wedge[m=1]\) has positive measure even after meeting b, since it occupies \(1/4\) of [s] and b excludes <\(1/8\). Their rational interval traces overlap O, so some same-color finite-cover term meets the target rectangle. Its join is dense, and j sends it to 1. The all-label mirrored cover still has disjoint bit images, so D₂>D.

For every finite E, the same-orientation pair with \(\gamma_E\) is **fully cover-compatible**: outside E, the cover members containing the boundary labels produce opens with Boolean factor [n=0]. Given any nonzero \(O\boxtimes b\), select a high-density cylinder [s] and a rational center in O with n outside dom(s)∪E; meeting b with [s]∧[n=0] remains positive. The resulting join is dense and j sends it to 1. For two basic conditions, an appropriate finite E makes their cylinders overlap; Lemma 3.1 even provides this for arbitrary positive Boolean values.

Therefore the random/measure-algebra version is **rescued by finite flips just like the Cohen construction**. The referee's first bounded test does not offer a candidate. It may suggest an abstract no-go theorem but we do **not** open that program now. No assertion that every forcing completion behaves this way.

## 4. Bounded test of suggestion 2: the U-separation predicate

Define
\[
a\perp_{\mathcal U}b\quad\Longleftrightarrow\quad a\boxtimes b\le d_{\mathcal U}.
\]
The adjunction for \(w_F\to d_{\mathcal U}\), using rectangle generators, proves
\[
\boxed{\mathcal W_2=\mathcal U}
\ \Longleftrightarrow\
\left[
\text{for every finite cover F and }a,b\in L:
\bigl(\forall c\in F,\ a\wedge c\perp_{\mathcal U}b\wedge c\bigr)
\Rightarrow a\perp_{\mathcal U}b
\right].
\]
Similarly \(\mathcal W=\mathcal U\) iff the same locality holds for **arbitrary** covers. Thus Q asks whether finitary cover-locality of a binary predicate implies arbitrary cover-locality. This is an exact reformulation, **not** yet a new proof method.

In C5, for sheet opens u≤A and v≤B, let \(\pi(u),\pi(v)\) be their rational-parameter projections. The global footprint argument yields an explicit description:
\[
\boxed{u\perp_{\mathcal U}v\iff
\pi(u)\cap\pi(v)=\varnothing.}
\]
For the nontrivial reverse direction, if the projections meet at q, choose conditions F,G and common extension H containing any label n; the pair of sheet points \(((q,H)^A,(q,H)^B)\) is in D≤U and lies in the rectangle.

This gives a nucleus-free check of full-cover locality for these cross-sheet pairs. If \(\pi(u)\cap\pi(v)\ne\varnothing\), fix such a common q and H with n∈H. Every cover has a member containing boundary \(t_{q,n}\); that member includes both corresponding sheet points, and so the restricted opens \(u\wedge c,v\wedge c\) still have intersecting projections and fail \(\perp_{\mathcal U}\). Contraposition gives arbitrary-cover locality. The compact two-apex control instead displays **failure of finite** \(\perp_{\mathcal U}\)-locality, as expected from W₂<U.

This predicate is a useful conceptual entry point for the proposed next study of \(\mathcal W\). We see **no universal finitary-to-infinitary descent** in this check, so Q remains OPEN.

## 5. Decision and handoff

- **Accepted:** all externally checked structural claims and examples, with the listed repairs; independent footprint proofs upgrade C5/C6 global W=W₂=U.
- **Remain working with previous provenance:** hyperconnected strips, arbitrary Alexandrov regular-closed U, branching-factor variant.
- **Do not promote to headline theorems:** failed candidate constructions as classifications; optional N1⇔finite-cover characterization or template-wide rigidity conjecture, which were *suggestions*, not proved assertions.
- **Close the bounded follow-ups:** measure-algebra check gives the same finite-flip rescue; \(\perp_{\mathcal U}\) gives a correct and potentially conceptually useful reformulation but no solution.
- **Research status:** Q and Q′ both open, deferred. Next active subject: \(\mathcal W=\operatorname{cl}\mathcal D\) **as an independent relation in the separation hierarchy**, not principally as a step toward Q′.

No further external audit required for this phase. External mathematical corroboration is not a literature originality or priority check.
