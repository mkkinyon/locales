# Project A — Independent checks of the W-phase referee's three additions

**9 November 2026 · POST-referee technical analysis, NOT part of the blind referee report.** This note checks claims A3–A5 of the [archived independent report](project-a/audits/2026-11-09/Wphase/Independent_Blind_Referee_Report_2026-11-09.md). It separates independently corroborated mathematics from the packet's already reviewed results and from the referee's own new conjectural research proposals. The finite-cover approximation questions Q and Q′ are **still OPEN, DEFERRED**.

The verdict of our submitted packet was favorable, with one coherent-proof repair and one unverified old negative control. These additions are **new** relative to the packet, so the external referee did *not* certify them. The checks below are internal and should not be labeled E/external audit evidence.

## 1. Addition A3: compact factors imply D and W multiplicativity — independently checked

**Theorem 1 (working independent check).** For any pair of compact locales X,Y (classical foundational assumptions),
\[
\boxed{\mathcal D(X\times Y)=\mathcal D(X)\times\mathcal D(Y),\qquad
\mathcal W(X\times Y)=\mathcal W(X)\times\mathcal W(Y).}
\tag{1.1}
\]
The W identity for a *finite Alexandrov* first factor and arbitrary second factor was already proved in our packet; the compact/compact statement is a referee addition.

**Finite rectangular-grid lemma.** Suppose \(\bigvee_{i=1}^n a_i\boxtimes b_i=1\) in \(\mathcal O(X\times Y)\). Let \(\mathcal J=\{J\subseteq[n]:\bigvee_{i\in J}b_i=1_Y\}\). For each \(J\notin\mathcal J\), one has
\[
\bigvee_{i\notin J}a_i=1_X. \tag{1.2}
\]
For otherwise the product of the two nonzero closed sublocales
\(C_X(\bigvee_{i\notin J}a_i)\) and
\(C_Y(\bigvee_{i\in J}b_i)\)
would be nonzero and would annihilate every selected rectangle, contradicting that they cover. This is a locale argument; ordinary points of X,Y are not assumed.

Define the finite cover \(\mathcal A\) of X by all \(a_J=\bigwedge_{i\in J}a_i\), \(J\in\mathcal J\). To show \(\bigvee\mathcal A=1\), distribute the finite family of joins in (1.2). For any choice of \(i_J\notin J\) across all \(J\notin\mathcal J\), the set \(T=\{i_J:J\notin\mathcal J\}\) must be **good**, \(T\in\mathcal J\), since otherwise the choice at the bad set J=T would satisfy \(i_T\in T\) and \(i_T\notin T\). Thus every distributive summand \(\bigwedge_{J\notin\mathcal J}a_{i_J}\) lies below some \(a_T\) with \(T\in\mathcal J\).

Define the finite cover \(\mathcal B\) of Y by all
\(b_\phi=\bigwedge_{J\in\mathcal J}b_{\phi(J)}\), indexed by choice functions \(\phi(J)\in J\).
The equality
\[
1_Y=\bigwedge_{J\in\mathcal J}\bigvee_{i\in J}b_i
=\bigvee_\phi b_\phi
\]
is finite distributivity. For every grid cell,
\[
a_J\boxtimes b_\phi\le a_{\phi(J)}\boxtimes b_{\phi(J)}.
\tag{1.3}
\]
Hence the grid \(\{a_J\boxtimes b_\phi\}_{J,\phi}\) refines the original rectangular cover.

**Use of compactness.** Every cover of the compact product X×Y can be refined by finitely many rectangles: refine each open by rectangles, then extract a finite subcover. The finite grid lemma refines those rectangles by a product cover \(\mathcal A\times\mathcal B\). Since \(\mathcal D(X)\le O(w_{\mathcal A})\) and \(\mathcal D(Y)\le O(w_{\mathcal B})\), their product lies in the diagonal-square neighborhood of the grid, hence in that of the original cover. Thus \(\mathcal D(X)\times\mathcal D(Y)\le\mathcal D(X\times Y)\). The other inclusion is lax naturality under projections. Finally the product of two dense inclusions is dense: a nonzero basic open rectangle in the product of their closures meets both dense factors. Therefore
\(\operatorname{cl}(S\times T)=\operatorname{cl}S\times\operatorname{cl}T\), giving the W identity.

**Foundational caution:** the finite-grid proof uses no points of X,Y. It invokes the standard nontriviality of a product of two nonzero locales and the usual compactness of finite locale products. Do not claim the compact hypothesis can be dropped. Do not identify this with the still deferred Q′ assertion.

## 2. Addition A4: U and H multiply across a finite Alexandrov factor — independently checked

Let P be a finite upper-Alexandrov poset and Y an arbitrary locale. Write \(M=\mathcal O(Y^2)\), \(J=P^2\), so \(\mathcal O((P\times Y)^2)\cong \operatorname{Up}(J,M)\) with pointwise joins and meets. Sublocales of each slice are evaluated by frame quotient along the corresponding point \(s\in J\).

**Theorem 2 (working independent check).**
\[
\boxed{\mathcal U(P\times Y)=\mathcal U(P)\times\mathcal U(Y),\qquad
\mathcal H(P\times Y)=\mathcal H(P)\times\mathcal H(Y).}
\tag{2.1}
\]

**U formula.** For a section family \(v=(v_p)\in \operatorname{Up}(P,\mathcal O(Y))\),
\[
(v^*)_t=\bigwedge_{r\ge t}v_r^*
=\left(\bigvee_{r\ge t}v_r\right)^*.
\tag{2.2}
\]
Take far opens v,w satisfying \(v^*\vee w^*=1\). If \((p,q)\in U(P)\), choose \(p\le a\ge z\le b\ge q\), using the finite-poset common-upper/common-lower formula. Evaluate far-ness at z. Since \(v_p\le v_a\le\bigvee_{r\ge z}v_r\), and analogously \(w_q\le w_b\le\bigvee_{r\ge z}w_r\), we obtain \(v_p^*\vee w_q^*=1\). Thus the (p,q)-slice of the U-complement is ≤\(d_{U(Y)}\). Constant-in-P far sections achieve every Y far rectangle, proving equality on U(P). For \((p,q)\notin U(P)\), the principal opens ↑p and ↑q are far in P; their pullbacks give a far pair with section rectangle top at (p,q), so the complementary open section equals 1. This is the precise open-element formula for the product U relation, valid for arbitrary Y.

**H formula.** The product \(\mathcal H(P)\times\mathcal H(Y)\) is a closed fitted sublocale containing Δ, so
\(\mathcal H(P\times Y)\le\mathcal H(P)\times\mathcal H(Y)\). Closedness follows from the product of closed sublocales; fittedness from preservation of arbitrary meets/open sublocales by preimage along the two projections.

Conversely put \(S=\mathcal H(P\times Y)\). For each s∈P² let \(S_s\le Y²\) be its pullback to the constant-P² slice. Each \(S_s\) is **closed and fitted** because S is both, and preimages preserve those properties. Since S is closed, the slice sublocales decrease along specialization: s≤t implies \(S_t\le S_s\). Since S is fitted, they increase along specialization (each open neighborhood has increasing sections, and meets preserve inclusion): \(S_s\le S_t\). Thus slices are equal on comparable indices and hence on whole comparability components of P². Every diagonal slice \(S_{(p,p)}\) contains Δ_Y, so contains H(Y). The union of comparability components of P² meeting the diagonal is exactly H(P), by finite Alexandrov order theory. Hence \(S_s\ge H(Y)\) whenever s∈H(P), and the sectionwise closed-subspace criterion yields \(S\ge H(P)\times H(Y)\). Thus equality holds.

**Corollary (qualify P nonempty).** Since \(W(P)=U(P)\le H(P)\),
\[
\boxed{
\begin{aligned}
W(P\times Y)&=U(P)\times W(Y),\\
(H\wedge U)(P\times Y)&=U(P)\times(H(Y)\wedge U(Y)).
\end{aligned}}
\tag{2.3}
\]
For any **nonempty** finite P, equality \(W=H\wedge U\) on \(P\times Y\) holds *iff* it holds on Y. Reflection uses any diagonal slice \((p,p)\in U(P)\). With P empty the product is empty and this iff is false. This small qualification is missing from the referee's prose.

**Interpretation.** The connected strict diamond built from the finite fence and two-apex Y is valid, but the two strictness mechanisms are **factorwise** rather than an intrinsically new coupling. The product transfer is structurally more important than claims of a new interaction.

## 3. Addition A5: a connected compact T₁ locale with W<H — independent direct audit

Define \(T=(0,\infty)\cup(-\infty,0)\cup\{p_+,p_-,q\}\). On the two rays use the usual topology; \(p_+\) has cofinite-positive neighborhoods \(N_+(F)=\{p_+\}\cup((0,\infty)\setminus F)\), and \(p_-\) cofinite-negative neighborhoods \(N_-(G)=\{p_-\}\cup((-\infty,0)\setminus G)\). A basic q-neighborhood is
\[
\boxed{N_q(\varepsilon,G)=\{q\}\cup(0,\varepsilon)\cup((-\infty,0)\setminus G)}
\quad(\varepsilon>0,\ G\subset(-\infty,0)\text{ finite}).
\tag{3.1}
\]
This fully specifies the topology; it is not an ordinary wedge-point topology.

Put
\[
u_+=(0,\infty)\cup\{p_+\},\quad u_-=(-\infty,0)\cup\{p_-\},
\]
\[
A_+=u_+\cup\{q\},\quad A_-=u_-\cup\{q\},\quad
K=A_+^2\cup A_-^2.
\tag{3.2}
\]

**Topological checks.** T is T₁: every point has open singleton complement. It is compact: choose any open covering p₊ and p₋; those two sets cover both rays except finitely many points, after which q and finitely many remaining ray points can be covered with finitely many more opens. It is connected: any clopen U meeting the connected positive ray contains the whole positive ray; because q and p₊ lie in its closure, they belong to U. An open neighborhood of q meets the connected negative ray, forcing the entire negative ray into U, and then p₋; similarly starting with the negative ray. It is locally compact: q has compact neighborhoods
\(\{q\}\cup(0,\delta]\cup((-\infty,0)\setminus G)\)
contained in any prescribed \(N_q(\varepsilon,G)\) by taking δ<ε; a cover of such a compact set is reduced to a q-neighborhood, finitely many negative leftovers and the ordinary compact interval [η,δ]. Apex neighborhoods are compact opens and ray points have ordinary compact intervals. T is sober: an irreducible closed subset cannot contain two distinct ray points, since distinct reals admit disjoint ordinary open neighborhoods; hence it is finite (at most one ray point plus the three distinguished points), and a finite T₁ irreducible closed set must be a singleton.

**Compute U.** The closure of every positive ray neighborhood includes p₊, and the closure of every negative ray neighborhood includes p₋ and q. The closure of every p₊-neighborhood includes q, while q-neighborhoods contain cofinally the entire negative ray and a small initial positive interval. From these observations, for the closed Urysohn relation:
\[
\boxed{U(T)=K\cup(\{p_+\}\times u_-)\cup(u_-\times\{p_+\}).}
\tag{3.3}
\]
All other cross-ray pairs admit far neighborhoods: take a bounded interval around a positive ray point separated from q and a bounded negative interval or p₋-neighborhood. The square is spatial (locally compact sober factors), and U is closed, so the ordinary-pair calculation determines the genuine U sublocale. Strict U>K is witnessed e.g. by (p₊,p₋).

**Compute W from below.** \(u_+^2\cup u_-^2\subseteq U(T)\), and the closure of this open union is K. The previously established universal regular-core inequality \(\operatorname{cl}(\operatorname{int}U)\le W\) yields \(K\le W\).

**Compute W from above.** The complement of K is exactly \(t_{+-}\vee t_{-+}\), where \(t_{+-}=u_+\boxtimes u_-\) and \(t_{-+}=u_-\boxtimes u_+\). The binary cover
\[
\mathcal C=\{T\setminus\{p_+\},u_+\}
\]
has diagonal square-cover open \(w_{\mathcal C}=(T\setminus\{p_+\})^2\cup u_+^2\), which excludes \(\{p_+\}\times u_-\) and its transpose. Since U restricted to either mixed sector has points only in those strips, and restriction of closed spatial U to an open is spatial, \(D\wedge O(t_{+-}\vee t_{-+})=0\). Taking closure along opens shows \(W\le K\). Therefore
\[
\boxed{W(T)=K<U(T).}
\tag{3.4}
\]

**W is NOT fitted.** Let \(t_0=(0,\infty)\boxtimes(-\infty,0)\), a nonzero ordinary open quadrant inside \(d_W\). Let O(w) be *any* open neighborhood of the closed W=K. Every point \((x,q)\), x>0, belongs to K, hence to w. Choose a basic product neighborhood \(I_x\times N_q(\varepsilon,G)\subseteq w\) at (x,q). Its intersection with the negative ray contains all but finitely many negative points. Therefore every nonempty basic open rectangle \(I\times J\subseteq t_0\) meets w. Thus \(w\wedge t_0\) is **dense in t₀**.

Let B(t₀) be the least dense Boolean sublocale (double-negation sublocale) of the nonzero locale O(t₀). Every such dense open w|t₀ contains B(t₀), so
\[
0\ne B(t_0)\le\operatorname{fit}(W)\wedge O(t_0).
\tag{3.5}
\]
This is nonzero yet pointless: T² is spatial and T₁, and fittedness of the closed W cannot add ordinary points outside W; alternatively B(t₀) has no points because t₀ is an ordinary, crowded Hausdorff quadrant. Hence W<fit(W) and W<H.

Since B(t₀) is dense in t₀, its closure is \(\operatorname{cl}(t_0)=A_+\times A_-\). By symmetry H also contains \(A_-\times A_+\). Together with \(W= A_+^2\cup A_-^2\), these four closed rectangles cover all of T², since \(A_+\cup A_-=T\). Therefore
\[
\boxed{H(T)=T^2.}
\tag{3.6}
\]

**F=T².** Any continuous f:T→ℝ is constant on each ray by continuity at the corresponding cofinite apex; continuity at q equates the two ray constants and f(q), hence f(p₊),f(p₋). Thus
\[
\boxed{W(T)=K<U(T)<H(T)=F(T)=T^2.}
\tag{3.7}
\]
The second strictness follows, for example, from \((x,y)\) with x>0 and y<0, which lies outside U.

**Verdict on A5:** The original referee's T₁ construction survives an independent topology, U/W computation, and genuinely pointfree fitted-hull test. This is **new working mathematics, not externally certified** by the blind report (the referee presented it as their own unchecked addition). Its first-stage fitted residual is nonzero and has no ordinary points, but closure makes that residual dense enough to force H to be the full square.

## 4. Conclusions, status and boundaries

- Core original submitted packet: **externally corroborated**, with the coherent C1 repair and the missing inherited inputs documented separately in the reconciliation.
- Compact X,Y **D/W product formulas** (A3): **independently checked after the report**, not part of the referee's certificate.
- Finite-P **U/H product formulas** (A4): **independently checked after the report**, not part of the referee's certificate. The equality-class reflection needs **P nonempty**.
- Compact connected T₁ W<H example (A5): **independently checked after the report**, not part of the original independent referee's certificate. No inference about the proposed general conjecture W=U⇒W fitted.
- The connected finite-fence/two-apex strict diamond remains correct, but the referee's factorwise interpretation is more precise than our earlier suggestion of intrinsically coupled defects.
- No general arbitrary-product multiplicativity, no new general T₁ separation theorem, and no resolution of Q/Q′ are asserted.
