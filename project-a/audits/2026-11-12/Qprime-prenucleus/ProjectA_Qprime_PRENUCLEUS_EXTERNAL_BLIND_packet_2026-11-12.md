# Project A — Blind audit packet: the Q′ pre-nucleus and a canonical Boolean-support core

**Prepared 12 November 2026. INDEPENDENT REVIEW DRAFT, NOT A CERTIFICATION.**
Read the companion referee prompt FIRST. This file presents the proposed mathematics without results or verdicts of any internal audit. The proofs are offered **for independent verification**, not as proven theorems. No solution of \(Q\) or \(Q'\) is claimed.

## Orientation and order of review

**CORE:** Parts A–E (relative pre-nucleus, Boolean hole, support formula, exact persistence, and its idempotent reduced form). They are the central new claims. **SECONDARY BUT IN SCOPE:** Parts F–H (the weak/strong distinction, two hereditary sufficient criteria, and an explicit control example). **INTERFACE:** Part I (old rather-below and strip patches, lax naturality). The most serious potential failure would be a subtle mistake about *subspace closure*, the least dense Boolean sublocale, or pulling back a localic relation through a **closed** embedding.

This is a study of LOCALIC relations on \(X^2\), not merely their ordinary point sets.

---

# A. Definitions and exact fixed-point obstruction — CORE

Let \(L\) be an arbitrary frame and
\[
Q=L\oplus L=\mathcal O(X\times X),\qquad X=\operatorname{Loc}(L).
\]
Write \(a\boxtimes b\in Q\) for a pure rectangle. The rectangles join-generate \(Q\); \((a\boxtimes b)\wedge(c\boxtimes d)=(a\wedge c)\boxtimes(b\wedge d)\). For \(q\in Q\), \(\mathfrak o(q)\) and \(\mathfrak c(q)\) are respectively the open and closed sublocales; the latter is the complement of \(\mathfrak o(q)\) in the open/closed sense. The order on sublocales is inclusion.

For an open cover \(\mathcal C\subseteq L\) (\(\bigvee\mathcal C=1_L\)), set
\[
w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c.
\]
The fitted diagonal and its finite-cover approximation are
\[
\mathcal D=\bigwedge_{\mathcal C\text{ cover}}\mathfrak o(w_{\mathcal C}),\qquad
\mathcal D_2=\bigwedge_{F\text{ finite cover}}\mathfrak o(w_F).
\tag{A.1}
\]
Let \(\mathcal W=\operatorname{cl}_{X^2}\mathcal D=\mathfrak c(d_{\mathcal W})\) and
\[
\mathcal W_2=\operatorname{cl}_{X^2}\mathcal D_2
=\mathfrak c(d_0),\qquad d_0=d_{\mathcal W_2}\in Q.
\tag{A.2}
\]
Thus \(\mathcal D\le\mathcal D_2\), \(\mathcal W\le\mathcal W_2\). Question \(Q'\) asks whether \(\mathcal W=\mathcal W_2\) ALWAYS. A weaker open question \(Q\) asks whether \(\mathcal W_2=\mathcal U\) forces \(\mathcal W=\mathcal U\), with \(\mathcal U\) the Urysohn closed relation.

The two cover pre-nuclei are
\[
\Phi(q)=\bigvee_{\mathcal C\text{ arbitrary}}(w_{\mathcal C}\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite}}(w_F\to q),
\tag{A.3}
\]
where \(\to\) is the Heyting implication in Q. A common refinement of covers has \(w_{\mathcal C\wedge\mathcal C'}=w_{\mathcal C}\wedge w_{\mathcal C'}\), implying these maps are inflationary, monotone and meet-preserving pre-nuclei. Their transfinite fixed-point closures starting from \(0_Q\) satisfy
\[
\Phi^\infty(0_Q)=d_{\mathcal W},\qquad
\Phi_2^\infty(0_Q)=d_0,\qquad
\Phi_2(d_0)=d_0.
\tag{A.4}
\]
These are **imported foundation results** from the earlier Q′ packet, independently reviewed on 9 November. Please check their usage; if you wish, independently reconstruct (A.4) rather than accepting it.

**Foundational generalized-pair criterion.** A pair of frame homomorphisms \(h,k:L\to M\), for any frame M, jointly factors through \(\mathcal D_2\) precisely when
\[
\bigvee_{c\in F} h(c)\wedge k(c)=1_M
\quad\text{for EVERY finite cover }F;
\tag{A.5}
\]
joint factorization through \(\mathcal D\) uses (A.5) for **EVERY arbitrary cover**. In this packet all finite-cover compatibility statements quantify over all finite covers, not merely particular displayed ones.

**Claim A1 (first-step criterion).**
\[
\boxed{\mathcal W=\mathcal W_2
\iff \Phi(d_0)=d_0.}
\tag{A.6}
\]
Because \(d_0\) is already \(\Phi_2\)-fixed, equality with the full closure is equivalent to its being fixed by \(\Phi\).

For each arbitrary cover \(\mathcal C\) put
\[
\rho_{\mathcal C}=w_{\mathcal C}\to d_0,\qquad
E_{\mathcal C}=\mathcal W_2\wedge\mathfrak o_Q(\rho_{\mathcal C}).
\tag{A.7}
\]
Then
\[
\boxed{
\mathcal W<\mathcal W_2\iff
E_{\mathcal C}\ne0\quad\text{for some cover }\mathcal C.
}
\tag{A.8}
\]

**Proposed proof of relative regular-open property.** The frame \(O(\mathcal W_2)\) is \(\uparrow d_0\subseteq Q\), with bottom \(d_0\). For \(q\ge d_0\), the relative implication of the open restriction \(w_{\mathcal C}\vee d_0\) into q is
\[
(w_{\mathcal C}\vee d_0)\to_{\uparrow d_0}q
=w_{\mathcal C}\to_Q q.
\tag{A.9}
\]
Thus \(\rho_{\mathcal C}\) is the **relative pseudocomplement** of \(w_{\mathcal C}|_{\mathcal W_2}\), and is automatically double-negation fixed in \(O(\mathcal W_2)\). The sublocale \(E_{\mathcal C}\) is a **regular open of \(\mathcal W_2\)**; this does not claim its defining element is necessarily regular open in all of Q.

When \(F\) is finite, \(\rho_F=d_0\) by \(\Phi_2(d_0)=d_0\); a genuine hole therefore requires an infinite cover without a finite subcover.

---

# B. The canonical Boolean-valued witness — CORE

Assume \(\mathcal W<\mathcal W_2\), and choose ONE cover \(\mathcal C\) with \(E=E_{\mathcal C}\ne0\). Write \(\rho=\rho_{\mathcal C}\).

**Standard fact for the audit:** Every locale \(T\) has a least dense **Boolean** sublocale \(B(T)\), the Isbell/double-negation sublocale. Equivalently, if \(\mathcal S\le T\) is dense, then \(B(T)\le\mathcal S\). A proof uses that a dense nucleus j satisfies \(j(a)\wedge a^*\le j(0)=0\), hence \(j(a)\le a^{**}\). For nonzero T, B(T) is nonzero and its open frame is a complete Boolean algebra.

Since \(\mathcal D_2\) is dense in its closure \(\mathcal W_2\), the sublocale \(\mathcal D_2\wedge E\) is dense in the relatively open E. Therefore
\[
\boxed{B(E)\le\mathcal D_2\wedge E.}
\tag{B.1}
\]
Write \(M=\mathcal O(B(E))\). The two coordinate projections \(B(E)\to X\) give frame homomorphisms
\[
h,k:L\to M.
\tag{B.2}
\]

**Claim B1 (maximal cover discrepancy).** For every finite cover F,
\[
\bigvee_{c\in F}h(c)\wedge k(c)=1_M,
\tag{B.3}
\]
whereas for the chosen arbitrary cover C,
\[
\boxed{\bigvee_{c\in\mathcal C}h(c)\wedge k(c)=0_M.}
\tag{B.4}
\]
Indeed, B(E) lies in D₂, while \(\rho\wedge w_C\le d_0\) makes E disjoint from \(\mathfrak o(w_C)\).

Optional additional consequence to inspect: M is **atomless**, because an atom would yield an ordinary point of D₂ in E, whereas ordinary points of D₂ and D coincide for all locales, and D misses E.

**Critical qualification:** (B.3)–(B.4) alone do NOT prove \(\mathcal W<\mathcal W_2\). The essential additional input is that B(E) is dense in a NONZERO **open** sublocale of W₂. Part H supplies a control where B-valued cover discrepancy exists but this open-hull condition fails.

---

# C. Least closed common coordinate support — CORE

Let \(p_i:X^2\to X\) be the two coordinate projections. Their inverse-image frame homomorphisms \(p_i^*:L\to Q\) have right adjoints \(p_{i*}:Q\to L\).

Define
\[
e_{\mathcal C}=
\bigvee\{a\in L:h(a)=k(a)=0_M\}
\tag{C.1}
\]
and the **closed sublocale**
\[
K=\mathfrak c_X(e_{\mathcal C})\hookrightarrow X.
\tag{C.2}
\]

**Claim C1 (intrinsic pre-nucleus support formula).**
\[
\boxed{
e_{\mathcal C}
=p_{1*}(\rho\to d_0)\wedge p_{2*}(\rho\to d_0).
}
\tag{C.3}
\]

**Proposed proof.** Since B(E) is dense in E, for \(a\in L\),
\[
\begin{split}
h(a)=0_M
&\iff E\wedge\mathfrak o_Q(p_1^*a)=0\\
&\iff \rho\wedge p_1^*a\le d_0\\
&\iff a\le p_{1*}(\rho\to d_0).
\end{split}
\tag{C.4}
\]
The symmetric formula applies to k. Their joint zero ideal is ↓e_C, and h,k kill their join e_C.

**Claim C2 (minimality and density of joint support).** K is the LEAST CLOSED sublocale of X through which **both** coordinate maps \(B(E)\to X\) factor. Moreover,
\[
\boxed{E\le K\times K}
\tag{C.5}
\]
as sublocales of X², and after factoring h,k through K, the resulting maps \(h_K,k_K:\mathcal O(K)\to M\) satisfy
\[
\boxed{
h_K(v)=k_K(v)=0_M\quad\Longrightarrow\quad v=0_K.
}
\tag{C.6}
\]

**Proposed proof.** \(h(e_C)=k(e_C)=0\), so the maps factor through K. Any other closed C(a) through which both factor has a in the joint zero ideal, hence a≤e_C and K≤C(a). The image of \(B(E)\to X^2\) lies in K². Since K² is CLOSED in X² and B(E) is DENSE in E, it also contains E, proving (C.5). A v in O(K)=↑e_C killed by both coordinate maps must satisfy v≤e_C and hence v=e_C=0_K.

**Requested check:** The step from a CLOSED sublocale containing a DENSE sublocale of E to containing E must hold without point-set spatiality. Also clarify that (C.6) is **joint** zero-reflection, not separate zero-reflection of either coordinate map.

---

# D. Exact persistence inside the support core — CORE / highest priority

Write \(i:K\hookrightarrow X\) for the closed inclusion and \(q=(i\times i)^*:Q_X\to Q_K\). Put
\[
\mathcal C_K=\{i^*(c):c\in\mathcal C\},\qquad \rho_K=q(\rho).
\tag{D.1}
\]
\(\mathcal C_K\) is an open cover of K.

**Auxiliary lemma D0: exact closed heredity of the fitted diagonals.** For ANY closed sublocale \(K\hookrightarrow X\),
\[
\boxed{
\mathcal D_2(K)=\mathcal D_2(X)\wedge K^2,\qquad
\mathcal D(K)=\mathcal D(X)\wedge K^2.
}
\tag{D.2}
\]
**Proof offered.** An X-cover restricts to a K-cover. Conversely, given ANY (finite or arbitrary) K-cover \(\{v_j\}\), choose lifts \(c_j\in O(X)\) and add \(a\), the open complement of K. Then \(\{a\}\cup\{c_j\}\) is a (finite, respectively arbitrary) X-cover, inducing the same K-square cover since \(a|_K=0\). Thus a generalized pair into K² is cover-compatible in K iff its composite is cover-compatible in X. In particular (D.2) is proved **without asserting that closure commutes with closed restriction**.

**Main proposed Theorem D1 (same marked hole).** As sublocales of \(K^2\), with E included using (C.5),
\[
\boxed{
\mathcal W_2(K)\wedge\mathfrak o_{K^2}(\rho_K)=E.
}
\tag{D.3}
\]
Moreover,
\[
\boxed{
\mathcal W(K)\wedge E=0,\quad
B(E)\le\mathcal D_2(K),\quad
\mathcal D(K)\wedge E=0.
}
\tag{D.4}
\]

**Proposed proof.** (B.1), (C.5), (D.2) give \(B(E)\le\mathcal D_2(K)\). Since B(E) is dense in E, the closed hull W₂(K) contains E. Conversely the pullback of the CLOSED \(\mathcal W_2(X)\) is closed in K² and contains D₂(K), so
\[
\mathcal W_2(K)\le\mathcal W_2(X)\wedge K^2.
\tag{D.5}
\]
Intersect both containments with \(\mathfrak o_{K^2}(\rho_K)\); using \(E=\mathcal W_2(X)\wedge\mathfrak o_Q(\rho)\le K^2\), obtain (D.3).

For the full fitted relation, since \(\rho\wedge w_C\le d_0\), and \(\mathcal D(K)\le\mathfrak o_{K^2}(w_{C_K})\le\mathcal W_2(K)\), it misses the **ambient open** \(\mathfrak o_{K^2}(\rho_K)\). Consequently its CLOSED hull W(K) misses that same open. Hence (D.4).

**Corollary D2 (still a genuine pre-nucleus failure).** The restricted cover and restricted \(\rho\) satisfy
\[
\boxed{
\rho_K\wedge w_{\mathcal C_K}
\le d_{\mathcal W_2(K)},\qquad
\rho_K\not\le d_{\mathcal W_2(K)}.
}
\tag{D.6}
\]
Indeed \(q(\rho\wedge w_C)\le q(d_0)\le d_{\mathcal W_2(K)}\) by (D.5), while (D.3) is nonzero. Thus
\[
\boxed{\Phi_K(d_{\mathcal W_2(K)})>d_{\mathcal W_2(K)},}
\tag{D.7}
\]
and Q′ fails on K.

**Critical scope:** We do NOT assert that \(\rho_K=w_{\mathcal C_K}\to d_{\mathcal W_2(K)}\); frame homomorphisms preserve implication only in one direction. We assert persistence of **the same marked nonzero sublocale E**, not equality of two entire new canonical holes.

**Highest-priority stress test:** Is the reasoning from B(E) dense in E to E≤W₂(K) legitimate for nonspatial locales? Does (D.3) remain correct even though *closure does not generally commute with restriction to a closed sublocale*? Is \(\mathcal D(K)\) really disjoint from the AMBIENT open defined by \(\rho_K\), not merely from E?

---

# E. Vanishing cover patches, sound strips, and marked idempotence — CORE

Use \(\prec\) for the frame rather-below relation, \(v\prec u\iff v^*\vee u=1\). For any locale Y and an arbitrary cover \(\mathcal V\), define
\[
t_{\mathcal V}^{Y}=
\bigvee_{\substack{F\subseteq\mathcal V\\ F\text{ finite}}}
\bigvee\{v\in O(Y):v\prec_Y\bigvee F\}.
\tag{E.1}
\]

**Claim E1 (intrinsic reduced core).** For K and \(\mathcal C_K\) as above,
\[
\boxed{t_{\mathcal C_K}^{K}=0_K.}
\tag{E.2}
\]

**Proof offered.** Fix finite \(F\subseteq\mathcal C_K\), \(v\prec\bigvee F\). Then \(\{v^*\}\cup F\) is a FINITE K-cover. The reduced maps h_K,k_K give matching value 1 for it, while every member of F has matching value 0 because the entire bad \(\mathcal C_K\) has matching value zero. Meeting with h_K(v) kills the v* contribution and yields h_K(v)=0. Symmetry gives k_K(v)=0. Joint zero-reflection (C.6) forces v=0. Join over all such v,F.

**Claim E2 (no local two-coordinate equality strip).** If \(v\in O(K)\) is such that \(\mathcal W(K)\) and \(\mathcal W_2(K)\) agree on the open union of the two coordinate strips
\[
\mathfrak o_{K^2}\bigl((v\boxtimes1)\vee(1\boxtimes v)\bigr),
\]
then v=0. **Proof offered:** E lies inside W₂(K) but is disjoint from W(K); agreement on the strips forces E to miss them. The coordinate Boolean values h_K(v),k_K(v) are therefore zero; invoke (C.6).

**Claim E3 (idempotence for the MARKED E).** Repeat the least-closed-common-coordinate-support construction on K, but using the SAME sublocale E and the SAME Booleanization \(B(E)\). Its common coordinate zero ideal in O(K) is bottom by (C.6). Thus the resulting closed support is K itself. This is an **idempotent support reduction**. It is not idempotence of \(\Phi\) or a claim that a newly computed maximal hole on K has exactly the same support.

---

# F. Weak D₂>D defects versus strong W₂>W defects — SECONDARY

The preceding CORE construction begins with a **nonzero relatively OPEN sublocale of W₂**. A weaker version appears to apply whenever D₂>D.

**Claim F1 (weak support normalization).** If \(\mathcal D_2(X)\not\le\mathcal D(X)\), some cover C has \(\mathcal D_2\not\le\mathfrak o(w_C)\). The sublocale
\[
T_C=\mathcal D_2(X)\wedge\mathfrak c_{X^2}(w_C)
\tag{F.1}
\]
is then NONZERO. **Check carefully:** this uses that the pullback of an ambient CLOSED sublocale \(\mathfrak c(w_C)\) to D₂ is the closed complement of the restricted open \(w_C|_{D_2}\), which is zero iff that open is top. It does NOT assume arbitrary lattice distributivity of sublocales.

The Booleanization \(B(T_C)\) gives a nonzero Boolean-valued pair finite-cover-compatible but C-matching zero. Form its least closed common coordinate support as in C, obtaining K and jointly zero-reflecting maps into the SAME Boolean target. Then:
\[
\mathcal D_2(K)>\mathcal D(K),\qquad
t_{\mathcal C_K}^{K}=0.
\tag{F.2}
\]
There is NO claim that \(\mathcal W_2(K)>\mathcal W(K)\); the weak witness need not be dense in any NONZERO relatively open part of W₂.

**Audit task:** Is (F.1) genuinely nonzero under the stated assumption for arbitrary locales? Is the weak normalization valid, and is it correctly distinguished from the *strong* exact persistence theorem D1?

---

# G. One-sided rigidity and two hereditary sufficient criteria — SECONDARY

**Auxiliary proposed Theorem G1 (one-sided closed-sublocale rigidity).** If \(J\hookrightarrow Y\) is closed and J is either COMPACT or REGULAR, then
\[
\boxed{
\mathcal D_2(Y)\wedge(J\times Y)=
\mathcal D(Y)\wedge(J\times Y),
}
\tag{G.1}
\]
and symmetrically for Y×J.

**Compact-case proof offered.** For a finite-cover-compatible generalized pair \(f,g:T\to Y\) with f factoring through J, restrict any Y-cover C to compact J and choose finite F⊂C covering J. If a defines the open complement of J, \(\{a\}\cup F\) is a finite Y-cover. Since \(f^*a=0\), its matching value comes solely from F; hence C is fully compatible.

**Regular-case proof offered.** For c∈O(Y), \(v\prec_J i^*c\), lift \(v^*\) to w∈O(Y), and add the complement a to obtain the finite cover \(\{a,w,c\}\). Finite matching and meeting with \(f_J^*v\) give \(f_J^*v\le g^*c\). As J is regular, \(i^*c=\bigvee_{v\prec i^*c}v\), so
\[
f^*c\le g^*c\quad\text{for every ambient open }c.
\tag{G.2}
\]
Thus every arbitrary cover matches to 1. No regularity of Y or of the second endpoint is assumed.

**Two additional claims to audit:**
- **G2 (hereditarily nonzero cover patches).** If for every NONZERO CLOSED sublocale \(Y\hookrightarrow X\) and EVERY open cover \(\mathcal V\) of Y we have \(t_{\mathcal V}^Y\ne0_Y\), then \(\boxed{\mathcal D_2(X)=\mathcal D(X)}\). Proof proposed: otherwise the WEAK support normalization F1 produces a nonzero closed K and an inherited cover with zero t.
- **G3 (hereditarily compact/regular patches).** If every nonzero closed \(Y\hookrightarrow X\) contains a nonzero OPEN \(V\subseteq Y\) which lies inside some closed compact or regular \(J\hookrightarrow Y\), then \(\boxed{\mathcal D_2(X)=\mathcal D(X)}\). Proof proposed: otherwise weak normalization gives a jointly zero-reflecting C-incompatible Boolean pair on K. Applying (G.1) on J×K and K×J forces both coordinate images of V to vanish, contradiction.

**Audit task:** These are sufficient, not necessary conditions. Does the inference to the STRONGER equality \(\mathcal D_2=\mathcal D\) survive all localic subtleties?

---

# H. Explicit negative control: zero-valued fitting defects need not produce an open hole

Let
\[
S=\{s:\mathbb N\rightharpoonup\{0,1\}:\operatorname{dom}(s)\ne\varnothing\}
\]
with **finite and infinite** partial functions and order by extension. S is an algebraic dcpo, with Scott-open basis \(\uparrow s\) for finite nonempty s. Its Scott locale is locally compact sober and is NOT compact.

Let \(B_0=\operatorname{RO}(2^{\mathbb N})\), the complete Boolean algebra of regular opens of Cantor space. For a finite nonempty binary partial function s, write [s] for its Cantor cylinder, and \(\overline s\) for the bitwise opposite assignment on \(\operatorname{dom}s\). Define frame maps
\[
h_+(U)=j\left(
\bigcup_{\substack{s\text{ finite nonempty}\\\uparrow s\subseteq U}}[s]\right),\qquad
h_-(U)=j\left(
\bigcup_{\substack{s\text{ finite nonempty}\\\uparrow s\subseteq U}}[\overline s]\right),
\tag{H.1}
\]
with j the double-negation map \(\mathcal O(2^\mathbb N)\to B_0\). Arbitrary joins are preserved because membership of a finite condition in a Scott-open union is witnessed by one member; finite meets because compatible partial conditions combine by union, and incompatible conditions give disjoint cylinders.

For ANY finite cover \(U_1,\ldots,U_m\) of S, one member contains infinitely many singleton partial functions on DISTINCT coordinates; its h₊ and h₋ values are both 1 in \(B_0\) because the corresponding unions of positive and negative coordinate cylinders are dense. Hence the pair is compatible with every finite cover.

For the infinite singleton-literal cover
\[
\mathcal L=\{\uparrow\{n\mapsto b\}:n\in\mathbb N,\ b\in\{0,1\}\},
\tag{H.2}
\]
each term matches to
\[
h_+(\uparrow\{n\mapsto b\})\wedge
h_-(\uparrow\{n\mapsto b\})
=[n=b]\wedge[n=1-b]=0.
\]
Thus \(\mathcal D_2(S)>\mathcal D(S)\), with a nonzero Boolean pair and zero-valued infinite cover.

But common-specialization-predecessor pairs are dense in \(S^2\): any two basic Scott opens contain finite conditions s,t, which can be extended by a SHARED singleton condition on a fresh coordinate. Every pair of completed extensions shares that lower point and hence belongs to the FULL fitted diagonal. As the localic square is spatial, \(\mathcal D(S)\) is dense in \(S^2\), and
\[
\boxed{\mathcal W(S)=\mathcal W_2(S)=S^2.}
\tag{H.3}
\]
Therefore ALL relative first-step regular-open holes \(E_C\) in W₂ are ZERO, despite the existence of a zero-valued finite-compatible Boolean pair. This is the test case against conflating Part F and Part D.

**Audit task:** The control's detailed combinatorics are secondary to the main theorem. Check at least that it plausibly supports the claimed logical distinction. If inspecting full frame-map preservation, flag any unproven quantifier.

---

# I. Comparison with older localizations; lax naturality — INTERFACE

Two working prerequisites, with separate review histories:

- **Rather-below localization.** For a cover C, define \(t_C\) by (E.1). Earlier work proves that a rectangular full-cover defect satisfying \(r\wedge w_C\le d_0\) is supported in the closed remainder \(\mathfrak c(t_C)^2\).
- **Hull-sound coordinate strips.** An open a is *hull-sound* when W and W₂ agree on the union of its two coordinate strips. Previously proposed examples include the union \(h_{\rm hc}\) of hyperconnected opens and \(h_{\rm cc}\) of compact-closed-neighborhood opens. The **hyperconnected-strip theorem remains an imported working result**; you need not certify it to check the algebra below.

**Claim I1 (old patches are included in the intrinsic support open).** For the original chosen strong-hole cover C,
\[
\boxed{t_C\le e_C.}
\tag{I.1}
\]
Indeed for any finite F⊂C and v≺∨F, the finite cover \(\{v^*\}\cup F\), together with the Boolean pair's zero C value, forces h(v)=k(v)=0. The same conclusion holds for ANY hull-sound open a because E, disjoint from W but inside W₂, must miss the sound strips. Hence a≤e_C. Conditional on the old strip results, \(h_{\rm hc}\vee h_{\rm cc}\le e_C\); therefore the new minimal closed support is contained in the earlier coverwise closed remainder \(\mathfrak c(t_C\vee h_{\rm hc}\vee h_{\rm cc})\).

**Claim I2 (lax naturality, not exact naturality).** For a closed inclusion i:K→X, set \(q=(i\times i)^*:Q_X\to Q_K\). Then
\[
\boxed{
q(\Phi_X(z))\le\Phi_K(qz),\qquad
q(\Phi_{2,X}(z))\le\Phi_{2,K}(qz),
}
\tag{I.2}
\]
since frame homomorphisms satisfy \(q(w\to z)\le(qw\to qz)\), and X-covers restrict to K-covers. Also \(q(d_{\mathcal W_2(X)})\le d_{\mathcal W_2(K)}\). Equality is NOT generally asserted.

**Audit task:** Are these inequalities in the correct directions? Are the imported hull-sound cases clearly separated from the new unconditional algebraic statement?

---

# J. Questions we particularly want answered

1. Does a first-step nonzero *relative pseudocomplement* \(\rho_C\) provide the claimed regular-open E in W₂? Is this exactly equivalent to Q′ failure?
2. Is the Isbell/double-negation inclusion \(B(E)\le D_2\wedge E\) legitimate for **all** locales and all (possibly pointless) E?
3. Is formula (C.3) correct? Is the joint support really **least among closed supports**, and does its construction require any tacit choice?
4. Is (D.3) — **the identical marked open E surviving in W₂(K)** — correct? Check each closure and sublocale comparison. The argument must **not** assume that closure commutes with closed restriction.
5. Do we really get both a strict pre-nucleus failure on K and \(t_{C_K}=0\), with no nonzero hull-sound two-coordinate strip? Is the fixed-point/idempotence statement precisely scoped?
6. Are the weak fitting-defect normalization (F1), one-sided rigidity (G1), and hereditary positive classes (G2,G3) valid? Look for counterexamples.
7. Which claims are mere restatements of \(Q'\), and which produce genuinely new structural restrictions? Any bounded, concrete next algebraic experiment?

The packet intentionally contains no internal verdict, no internal referee-comparison material, and no claims of external verification for the new theorem. Please complete your own report before consulting the source notes.
