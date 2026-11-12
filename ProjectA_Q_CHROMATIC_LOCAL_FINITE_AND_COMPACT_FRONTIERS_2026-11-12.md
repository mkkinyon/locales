# Project A — Q rank one: chromatically local finiteization and compact/regular chromatic frontiers

**12 November 2026 — NEW INTERNAL WORKING THEOREMS, not externally audited or literature-priority checked.** Bounded continuation of [the locally finite cover pre-nucleus theorem](ProjectA_Q_LOCAL_FINITE_COVERS_PRENUCLEUS_EXACT_INTERCHANGE_2026-11-12.md) and [the chromatic remainder theorem](ProjectA_Q_RANK_ONE_SHARP_CHROMATIC_GADGET_AND_REMAINDER_FILTER_2026-11-12.md). User specifically requested interaction of those two constraints on the SAME cover and SAME potential rank-one hole. Main results:

1. **Local chromatic finiteization:** If an arbitrary cover C kills a closed relation on a rectangle r, and an auxiliary cover V sees only FINITELY CHROMATIC induced cross-link graphs, then r≤Φ₂(d), even without finite stabilization or a uniform bound on colors.
2. The old local-finiteness locus \(\ell_C\) is EXACTLY the union of pseudocomplements of all cofinite cover tails. Thus \(H_C=C(\ell_C)\) is the *closed accumulation remainder*, and \(H_C=0\iff C\) is locally finite.
3. **Compact/regular remainder theorem:** The NONZERO CLOSED-TARGET QUOTIENT of a finite-compatible generalized pair on which C has matching value zero has BOTH endpoints supported on \(H_C\); the original unrestricted pair need not factor through it. If \(H_C\) is COMPACT or REGULAR closed, C is harmless even for weak \(\mathcal D_2>\mathcal D\) defects. For every finite-fixed d, \(w_C\to d=d\); for compact H_C the stronger universal **two-step** estimate \(w_C\to q\le\Phi_2^2(q)\) holds at every q.
4. **Exact chromatic frontier:** The cross-link graph of r yields a larger open locus \(\eta_{C,r}\supseteq\ell_C\), whose closed complement is the intersection of the closed closures of the tails after deleting ANY finitely colourable subfamily. If its closed chromatic frontier is compact or regular, r cannot witness a finite-fixed-point failure. This strengthens the plain locally finite remainder by using the relation itself.
5. **Hereditary support:** On the normalized Boolean-support core of a genuine Q′/Q hole, the bad cover is nowhere *locally finite chromatic* relative to the canonical open hole: every nonzero open intersects an induced subgraph of INFINITE chromatic number. This is the precise interaction of the previously separate invariants.
6. **Anti-drift:** The completed nonempty-powerset Scott locale supports analogous K_ω chromatic behaviour for a weak D₂>D Boolean witness but has W=W₂=U. Therefore NONE of these necessary conditions resolves Q. **Q and Q′ remain open.**

No new space is constructed. The already independently audited one-sided closed compact/regular fitting-rigidity theorem is used as an explicit prerequisite in §3.

## 0. Notation

Let \(L=\mathcal O(X)\), \(Q=L\oplus L\), \(w_C=\bigvee_{c\in C}c\boxtimes c\) for a cover \(C\subseteq L\), and
\[
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]
For closed localic relation \(T=\mathfrak c(d)\), a rectangle \(r=a\boxtimes b\), and cover C satisfying
\[
\boxed{r\wedge w_C\le d,}
\tag{0.1}
\]
define a cross-link graph \(\Gamma_r(C)\) with vertex set C: distinct c,c′ are adjacent iff
\[
r\wedge((c\boxtimes c')\vee(c'\boxtimes c))\not\le d.
\tag{0.2}
\]
There are no self-loops because of (0.1). Its induced subgraph on A⊆C is denoted \(\Gamma_r[A]\), its chromatic number \(\chi\), and
\[
\mathscr J_r=\{A\subseteq C:\chi(\Gamma_r[A])<\infty\}.
\tag{0.3}
\]
This is an ideal of P(C), containing Fin(C); it may equal P(C) if the graph is finitely colorable. For v∈L set \(I_C(v)=\{c\in C:c\wedge v\ne0\}\), and for A⊆C set \(u_A=\bigvee A\), \(v_A=\bigvee(C\setminus A)\).

## 1. The local chromatic finiteization theorem, without finite stabilization

**Theorem 1.1.** If \(\mathcal V\) is an open COVER of X such that \(\Gamma_r[I_C(v)]\) is finitely colorable for every \(v\in\mathcal V\), then
\[
\boxed{r\le\Phi_2(d).}
\tag{1.1}
\]
The number of colors can vary arbitrarily with v; there is NO uniform global bound.

*Proof.* Fix v and partition I_C(v) into finite k_v independent classes \(A_1,\dots,A_{k_v}\). Let \(t_v=v_{I_C(v)}=\bigvee(C\setminus I_C(v))\), so \(v\wedge t_v=0\). The finite family
\[
F_v=\{u_{A_1},\ldots,u_{A_{k_v}},t_v\}
\]
covers X. For any independent A_i,
\[
r\wedge(u_{A_i}\boxtimes u_{A_i})
=\bigvee_{c,c'\in A_i}r\wedge(c\boxtimes c')\le d,
\]
since the diagonal terms lie below d by (0.1), and each cross term lies below d by independence. Also \(r\wedge(v\boxtimes1)\wedge(t_v\boxtimes t_v)=0\), so
\[
r\wedge(v\boxtimes1)\wedge w_{F_v}\le d
\quad\Longrightarrow\quad
r\wedge(v\boxtimes1)\le w_{F_v}\to d\le\Phi_2(d).
\]
Join over v∈V, using \(\bigvee_{v\in V}v\boxtimes1=1_Q\). QED.

**Local chromatic support, without requiring V a cover.** Define
\[
\boxed{\eta_{C,r}
=\bigvee\{v\in L:I_C(v)\in\mathscr J_r\}.}
\tag{1.2}
\]
The same proof gives BOTH coordinate-strip inequalities:
\[
\boxed{
r\wedge(\eta_{C,r}\boxtimes1)\le\Phi_2(d),\qquad
r\wedge(1\boxtimes\eta_{C,r})\le\Phi_2(d).
}
\tag{1.3}
\]
Thus \(\eta=1\) suffices for the whole-rectangle simulation. The earlier finite-box-color theorem is a different sufficient mechanism for finite chromaticity; the present theorem needs only LOCAL finite chromaticity, not finite product-box rank.

## 2. The closed cofinite-tail accumulation remainder: exact characterization

For ANY cover C put
\[
t_F=\bigvee(C\setminus F)\quad(F\subseteq C\text{ finite}),\qquad
\ell_C=\bigvee\{v:I_C(v)\text{ finite}\}.
\]
Then
\[
\boxed{\ell_C=\bigvee_{F\subseteq_{\rm fin}C}t_F^*.}
\tag{2.1}
\]
Proof: if I_C(v)⊆F then v∧t_F=0 so v≤t_F*, and conversely t_F* meets only the members in F.

Define
\[
\boxed{
H_C=\mathfrak c_X(\ell_C)
=\bigwedge_{F\subseteq_{\rm fin}C}\operatorname{cl}_X\mathfrak o(t_F).
}
\tag{2.2}
\]
The family \(\{t_F^*:F\text{ finite}\}\) is a **canonical finitizer** whenever it covers X. Consequently
\[
\boxed{C\text{ locally finite}\iff\ell_C=1\iff H_C=0.}
\tag{2.3}
\]
This sharpens the terminology “local-finiteness locus”: H_C is literally the closed common accumulation remainder of ALL cofinite tails.

For a countably enumerated C=(c_n), writing \(t_n=\bigvee_{k\ge n}c_k\), one gets
\[
\ell_C=\bigvee_n t_n^*,\qquad H_C=\bigwedge_n\operatorname{cl}_X\mathfrak o(t_n).
\tag{2.4}
\]

## 3. A compact or regular H_C makes C harmless

**Lemma 3.1 (C-bad pair has both endpoints in H_C).** Let h,k:L→M be finite-cover-compatible, M nonzero, and suppose
\[
\bigvee_{c\in C}h(c)\wedge k(c)=0_M.
\tag{3.1}
\]
Then
\[
\boxed{h(\ell_C)=k(\ell_C)=0_M.}
\tag{3.2}
\]
Hence both generalized endpoints factor through the CLOSED sublocale H_C.

*Proof.* For EVERY finite F⊂C, the family \(F\cup\{t_F\}\) is a finite cover. All F-terms have zero matching value, so \(h(t_F)\wedge k(t_F)=1_M\), hence h(t_F)=k(t_F)=1. Because \(t_F\wedge t_F^*=0\), both maps send \(t_F^*\) to zero. Join over finite F and use (2.1). QED.

A pair whose C-matching value is merely \(u<1_M\) may be restricted to the NONZERO CLOSED target sublocale C_M(u), replacing M by \(\uparrow u\), to make its matching value bottom and leave all finite-cover compatibilities unchanged. Thus the lemma applies to ANY genuine finite-compatible C-defect.

**Theorem 3.2 (compact/regular accumulation remainder).** If H_C is compact OR regular as a CLOSED sublocale of X, then \(\mathcal D_2(X)\le\mathfrak o(w_C)\). Equivalently every finite-cover-compatible generalized pair is C-compatible. Moreover, for ANY q with \(\Phi_2(q)=q\),
\[
\boxed{w_C\to q=q.}
\tag{3.3}
\]

*Proof of D₂ containment.* Otherwise restrict a failing pair to a nonzero closed target component with C-value zero. Lemma 3.1 makes the first endpoint factor through H_C. The independently externally reviewed **one-sided closed compact/regular rigidity theorem** says D₂ and D agree on H_C×X; hence the pair is compatible with ALL covers, contradicting C-value zero.

*Proof for general finite-fixed q.* Suppose \(x=w_C\to q>q\), and let \(E=\mathfrak c(q)\wedge\mathfrak o(x)\), a nonzero relatively open sublocale of T=C(q). For every finite cover F, \(\Phi_2(q)=q\) implies \(w_F\to q=q\); hence the F-square is dense in T and its restriction to E is dense in E. Therefore its Booleanization B(E) lies in \(\mathcal D_2(X)\) (in fact in every F-square). It is disjoint from \(w_C\) because \(x\wedge w_C\le q\), so B(E) is a finite-compatible, C-incompatible pair. Lemma 3.1 and one-sided rigidity rule this out. Thus x=q. QED.

**Corollary 3.3 (nuclei equality under coverwise compact/regular remainders).** If EVERY open cover C of X has compact or regular H_C, then **every \(\Phi_2\)-fixed element is \(\Phi\)-fixed**, and the corresponding transfinite closure nuclei agree on ALL inputs:
\[
\boxed{\Phi^\infty=\Phi_2^\infty,\quad\mathcal D=\mathcal D_2,\quad\mathcal W=\mathcal W_2.}
\tag{3.4}
\]
Unlike the stronger locally finite refinement condition, this does **not** assert \(\Phi=\Phi_2\) after one step.

### 3.1 Quantitative TWO-step estimate when H_C is compact

**Theorem 3.4 (compact accumulation gives two finite steps).** If H_C is compact, then for EVERY q∈Q,
\[
\boxed{w_C\to q\le\Phi_2(\Phi_2(q)).}
\tag{3.5}
\]
*Proof.* Put x=w_C→q and y=Φ₂(q). The strip-localization theorem from the preceding note gives
\(x\wedge(\ell_C\boxtimes1)\le y\). Compactness of H_C means that the restricted cover C|H_C has a FINITE subcover; hence choose finite F₀⊂C such that \(\ell_C\vee\bigvee F_0=1\). Then \(\{\ell_C\}\cup F₀\) is a finite cover. On its square term \(\ell_C\boxtimes\ell_C\), x≤y by the strip inequality. On every term c⊠c for c∈F₀, x∧(c⊠c)≤q≤y. Thus \(x\wedge w_{\{\ell_C\}\cup F_0}\le y\), giving \(x\le\Phi_2(y)\). QED.

For a finite-fixed q, (3.5) reduces immediately to \(w_C\to q\le q\), recovering (3.3) without the one-sided rigidity theorem. This two-stage estimate may be useful for the rank hierarchy even when Q itself remains open.

## 4. The EXACT chromatic frontier, smaller than H_C

For the graph \(\Gamma_r(C)\) and its finite-chromatic ideal \(\mathscr J_r\) define the open **chromatically locally finite locus**
\[
\eta=\eta_{C,r}
=\bigvee\{v:\chi(\Gamma_r[I_C(v)])<\infty\}.
\]
Then the precise analog of (2.1) is
\[
\boxed{
\eta_{C,r}
=\bigvee_{A\in\mathscr J_r}v_A^*,
\qquad v_A=\bigvee(C\setminus A).
}
\tag{4.1}
\]
*Proof.* If A∈J, the open v_A* meets no member outside A, so I_C(v_A*)⊆A and is finitely chromatic, yielding one inclusion. Conversely if I_C(v)∈J, then \(v\wedge v_{I_C(v)}=0\), hence \(v\le v_{I_C(v)}^*\), giving the other inclusion.

Let
\[
\boxed{
H^\chi_{C,r}
=\mathfrak c_X(\eta_{C,r})
=\bigwedge_{A\in\mathscr J_r}\operatorname{cl}_X\mathfrak o(v_A).
}
\tag{4.2}
\]
Since Fin(C)⊆J,
\[
\boxed{\ell_C\le\eta_{C,r},\qquad H^\chi_{C,r}\le H_C.}
\tag{4.3}
\]
The right side is a **computable closed frontier from the actual cross-link graph**, not from a chosen Boolean probe.

**Theorem 4.1 (compact chromatic frontier gives two finite steps).** Under (0.1), if \(H^\chi_{C,r}\) is COMPACT, then
\[
\boxed{r\le\Phi_2^2(d).}
\tag{4.4}
\]
*Proof.* By (1.3), \(r\wedge(\eta\boxtimes1)\le y=\Phi_2(d)\). Compactness of Hχ gives finite F₀⊂C with \(\eta\vee\bigvee F_0=1\). Then \(\{\eta\}\cup F₀\) is finite; on its η-square r is ≤y and on each F₀-square r∧w_C≤d≤y. So \(r\wedge w_{\{\eta\}\cup F_0}\le y\), whence \(r\le\Phi_2(y)\). QED.

**Theorem 4.2 (regular chromatic frontier eliminates finite-fixed holes).** Suppose additionally \(\Phi_2(d)=d\). If \(H^\chi_{C,r}\) is COMPACT OR REGULAR closed, then
\[
\boxed{r\le d.}
\tag{4.5}
\]
*Proof.* Compact case follows (4.4). For regular case, suppose r not≤d and let \(E=\mathfrak c(d)\wedge\mathfrak o(r)\ne0\). E is a nonzero relatively OPEN part of T=C(d) and is contained in O(w_C→d) by (0.1). Its Booleanization B(E) is finite-compatible as in Theorem 3.2 and C-matching zero. For every v with finite-chromatic \(\Gamma_r[I_C(v)]\), the local inequalities (1.3) and Φ₂(d)=d imply \(E\wedge O(v\boxtimes1)=E\wedge O(1\boxtimes v)=0\). Hence both coordinate maps on B(E) kill η, so factor through Hχ. One-sided closed REGULAR rigidity implies full compatibility, contradiction. QED.

**Rank-one consequence:** With \(d=z_1=d_{\mathcal U}\), and \(\Phi_2(z_1)=z_1\), a genuine Q bad cover and linked rectangle r MUST have a nonzero closed chromatic frontier \(H^\chi_{C,r}\) which is **neither compact nor regular**. This is sharper than the plain condition on H_C because \(H^\chi_{C,r}\le H_C\).

### 4.3 Explicit test: chromatic finiteness can be much weaker than local finiteness

Let \(S=\mathcal P(\omega)\setminus\{\varnothing\}\) with its Scott topology. Let \(X=S_L\sqcup S_R\) be a DISJOINT sum of two copies, with clopen summands \(a=S_L,b=S_R\). For each n, let \(c^L_n\) be the nth singleton-basic Scott open in S_L and \(c^R_n\) its counterpart in S_R. The family \(C=\{c^L_n,c^R_n:n\in\omega\}\) covers X.

**Claim:** \(\ell_C=0\), hence \(H_C=X\), but for the nonzero CLOSED product relation \(T=a\times b\) and \(r=a\boxtimes b\), the link graph \(\Gamma_r(C)\) is the complete **bipartite** graph \(K_{\omega,\omega}\), so \(\eta_{C,r}=1\) and \(H^\chi_{C,r}=0\).

*Proof.* Every nonzero Scott-open in either copy meets ALL singleton-basic opens in that copy: given a finite nonempty condition F and any n, its extension F∪{n} lies in both. Thus no nonzero X-open meets only finitely many members of C, and ℓ_C=0. As r is mixed, every same-member square c⊠c lies entirely in one clopen summand's square, so r∧w_C=0. A left c and right c′ have a nonzero product in T[r], while two same-side c,c′ do not. Therefore the link graph is \(K_{\omega,\omega}\), globally 2-colorable, and \(\eta=1\).

This test proves the **chromatic** finiteization genuinely goes beyond local finiteness: the original cover is nowhere locally finite, yet its mixed relation is finitized by the two-color coarsening \(\{a,b\}\). Of course \(\Phi_2(d)>d\) for d the complement of T (the two-element finite cover already kills T). This is a control of the general theorem, **NOT** a Q counterexample or an assertion that Urysohn relations can link clopen-separated components.

## 5. The chromatic core is nowhere locally finitely chromatic

Let d=Φ₂(d), C a bad cover, and E=C(d)∧O(w_C→d) a NONZERO relatively open hole. Define \(\Gamma_E(C)\) by actual nonzero restrictions of E to c⊠c′ (loops vanish). Set
\[
\eta_{E,C}=\bigvee\{v\in L:\chi(\Gamma_E[I_C(v)])<\infty\}.
\]
The same finite local colouring argument, now applied directly to E and using density of every finite-cover square on E, proves
\[
\boxed{
E\wedge O((\eta_{E,C}\boxtimes1)\vee(1\boxtimes\eta_{E,C}))=0.
}
\tag{5.1}
\]
Thus \(\eta_{E,C}\) belongs to the joint coordinate zero ideal defining the least closed support K_E of E:
\[
\boxed{\ell_C\le\eta_{E,C}\le e_E.}
\tag{5.2}
\]

On the **independently audited** normalized core K=K_E, the original marked E survives and the coordinate maps are jointly zero-reflecting; therefore
\[
\boxed{\eta^{\,K}_{E,C|K}=0_K.}
\tag{5.3}
\]
Equivalently:
\[
\boxed{
\text{for every nonzero open }v\in O(K),
\quad
\chi\!\left(\Gamma_E(C|K)[\,\{c:c\wedge v\ne0\}\,]\right)=\infty.
}
\tag{5.4}
\]
This strictly sharpens the previous statement that each nonzero open meets INFINITELY MANY cover members: it meets a family with INFINITE CHROMATIC graph complexity.

**Co-chromatic tail density on K.** For each A∈\(\mathscr J_E\), the previous chromatic remainder theorem gives \(h(v_A)=k(v_A)=1\) on M=O(B(E)). If v is any nonzero K-open disjoint from v_A, then h(v)=k(v)=0, contradicting joint zero-reflection. Hence
\[
\boxed{v_A^*=0_K,\qquad
\overline{\mathfrak o_K(v_A)}=K.}
\tag{5.5}
\]
That is, **deleting any finitely chromatic family of cover members leaves a dense open in the WHOLE normalized support locale**, not merely a square open dense on the marked hole. For countable C, every ordinary cofinite tail is dense in K; the original K lies in the intersection of the tail closures. This is a precise, stable version of the “accumulation self-similarity” intuition, without claiming a literal recursive copy of K.

**Caution about rank-one inheritance:** Even when the ORIGINAL X is a Q-counterexample with \(\Phi_2(z_1^X)=z_1^X\), the closed support K need NOT be known to satisfy \(\Phi_{2,K}(z_1^K)=z_1^K\). The independently audited support theorem preserves the marked **Q′ hole**, not necessarily the rank-one condition of Q. All assertions of (5.1)–(5.5) on K use the universally finite-fixed \(d_{\mathcal W_2(K)}\), so this possible noninheritance causes NO error. Avoid silently claiming Q is hereditary under arbitrary closed sublocales.

## 6. Why these conditions do not yet settle Q: an actual negative control

The completed nonempty-powerset Scott domain \(S=\mathcal P(\omega)\setminus\{\varnothing\}\) with its singleton Scott cover \(C=\{\uparrow\{n\}\}\) has \(H_C=S\): every tail is dense, and \(\ell_C=0\). The standard pair into \(\operatorname{RO}(2^\omega)\), with positive and negative cylinder orientations, is finite-compatible and C-matching zero, and its BOOLEAN cross-link graph is Kω. Every nonzero Scott-open of S intersects every C-member, so the incidence graph on every nonzero open has INFINITE chromatic number. Yet
\[
\boxed{\mathcal W(S)=\mathcal W_2(S)=\mathcal U(S)=S^2.}
\]
Its Boolean pair is a WEAK fitted defect, not the Booleanization of a nonzero OPEN hole in W₂. This example falsifies any inference that chromatic saturation or a noncompact nonregular accumulation frontier alone contradicts Q.

### 6.1 A sharp literature-guided boundary: point-finite does NOT replace locally finite

Ferreira–Picado, *On Point-Finiteness in Pointfree Topology* (2006), §4, record the older **Dowker–Strauss point-finite** condition for a cover C:
\[
\boxed{
x=\bigwedge_{F\subseteq_{\mathrm{fin}}C}(x\vee t_F)
\quad\text{for every }x\in L,\qquad t_F=\bigvee(C\setminus F).
}
\tag{6.1}
\]
See https://www.mat.uc.pt/preprints/ps/p0630.pdf (printed p. 8, equation (4.1)). They emphasize that this old condition is not the optimal pointfree counterpart of classical point-finiteness and introduce a corrected notion. Our claim concerns ONLY (6.1).

**Proposition 6.1 (the Scott singleton cover is DS point-finite).** For S=P(ω)\{∅} with Scott topology and \(C=\{c_n=\uparrow\{n\}:n\in\omega\}\), condition (6.1) HOLDS, although \(\ell_C=0\) and the standard Boolean pair proves \(\mathcal D_2(S)>\mathcal D(S)\).

*Proof.* An arbitrary Scott-open x is an upper set, and \(t_F=\{A\ne\varnothing:A\setminus F\ne\varnothing\}\), with finite F now identified with a finite index set. As ordinary subsets of S,
\[
\bigcap_{F\mathrm{\ finite}}(x\cup t_F)
=x\cup\{A\subseteq\omega:A\text{ infinite}\}.
\]
The frame meet on the left is the **Scott interior** of this set. Every infinite A not in x has no Scott-basic neighborhood ↑G (G finite nonempty) contained in that set: any G⊆A lies outside x because x is upward, and G itself is FINITE, so G is outside the union. Therefore the Scott interior equals x. This proves (6.1). The cover is nowhere locally finite (every nonzero Scott open meets every c_n), and the Cantor Boolean pair yields a weak full-versus-finite fitting defect. □

Thus the exact locally finite pre-nucleus result **does not extend to DS point-finite covers**, even for algebraic sober Scott locales. This is an actual falsification test, not merely a missing proof. It does NOT establish anything negative about Q itself, because S has \(\mathcal U=\mathcal W=\mathcal W_2=S^2\). The newer **modified** point-finite condition of Ferreira–Picado has not been tested here.

**Conclusion / bounded next target:** We now have a precise choice-free closed frontier \(H_C\) and a smaller **graph-refined** closed frontier \(H^\chi_{C,r}\) on an actual proposed bad rectangle. Compact or regular frontiers eliminate the obstruction, and compact frontiers yield exact TWO-stage finite simulation. A hypothetical Q counterexample must have a genuinely noncompact, nonregular chromatic accumulation frontier throughout its hole. The remaining mathematical question is whether the **far-rectangle-generated nature of \(d_{\mathcal U}\)** and finite stabilization can exclude such a frontier, rather than whether one can add further pathologies to an example. No contradiction is presently established.

**STATUS: NEW INTERNAL WORKING RESULTS; Q and Q′ remain OPEN.**
