# External blind referee report — Project A: localic relational associativity and Arrieta's fitted diagonal

Report on `ProjectA_associativity_EXTERNAL_BLIND_packet_2026-11-07.md`. Written 7 November 2026, without consulting any internal audit, GitHub notes or prior comparison. Source checked: I. Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024) 108785, read in the arXiv/ar5iv version (2310.18522); section numbers below refer to that version and agree with the packet's citations.

Notation follows the packet, except: I write $o(u)$, $c(u)$ for open and closed sublocales, $\mathfrak B(L)$ for the Booleanization (smallest dense sublocale), $Q_n=\mathcal O(V)^{\oplus n}$, $w_n^{(m)}=W_n^{(m)}\cap V$ where $W_n^{(m)}=\{x\in C: x_n=1,\ x_j=0\ (n<j\le m)\}$ is the $m$-th basic clopen neighbourhood of $K_n$ ($m\ge n$), and I fix the packet's convention $\operatorname{supp}\widehat\pi x=\pi(\operatorname{supp}x)$, i.e. $(\widehat\pi x)_j=x_{\pi^{-1}(j)}$.

---

## Summary of verdicts

| # | Statement (packet §) | Verdict |
|---|---|---|
| 1 | Cover presentation $\mathcal D_Z=\bigwedge_{\mathcal C} o(\gamma_{\mathcal C})$ (§3) | **verified** |
| 2 | Frame normal form of $\mathcal O(Y)$, $\Theta$, admissible covers = traces of $Y$-covers (§2) | **verified** |
| 3 | Formula (A) for $A=\mathcal D_Y\wedge(V\times V)$ (§3) | **verified** |
| 4 | Vanishing mixed blocks $P_n=0$ (§3) | **verified**; justification should be rewritten (see B.4) |
| 5 | $\mathcal D_Y\wedge(N\times N)=\Delta_N$ (§3) | **verified** |
| 6 | Block formula (B), read as $\mathcal D_Y=A\vee\Delta_N$ with $A\subseteq V^2$, $\Delta_N\subseteq N^2$ (§3) | **verified** |
| 7 | (Cube-Y): $\mathcal D_Y^3$ associates iff $(A^2)A=A(A^2)$ (§3) | **verified** (given 6) |
| 8 | Sierpiński-transfer theorem $X_u$ (§3) | **not checked** — no statement/proof supplied |
| 9 | Boolean test (Pair) (§4) | **verified** |
| 10 | $\sigma,\tau$ bijections; $hAk$; $kA\ell$; $h\not A\ell$ via $\mathcal C_*$ (§5) | **verified** (all four) |
| 11 | **$A\circ A\not\subseteq A$** (§5) | **verified** |
| 12 | **$\mathcal D_Y\circ\mathcal D_Y\not\subseteq\mathcal D_Y$** (§5) | **verified**, and in fact independent of (B) — see A |
| 13 | (Perm) permutation-pair criterion incl. compactness step (§6) | **verified** |
| 14 | Diameter-two / Baire observation (§6) | **verified** (Baire is overkill) |
| 15 | Point fibres $A\vert_{\{p\}\times V}=\{(p,p)\}$ and for every parenthesized power (§7) | **verified** |
| 16 | $A\times_V V_d\cong V_d$; $A\to V$ does not stably preserve surjections (§7) | **verified** |
| 17 | "Projections neither open nor proper" (§7, optional) | **not checked**; the needed stability theorem is not cited |
| 18 | "Higher powers dense, nonspatial" (§7, optional) | **verified** by a new argument (A is dense in $V^2$, see D.1) |
| 19 | (CubeCong) (§8) | **verified** as an exact reformulation; it is not an advance |
| 20 | §0 background claims ($\mathcal I\mathcal D\subseteq\mathcal U$, seven-of-eight words, general $(RR)R\ne R(RR)$ example) | **not checked** — not in packet |
| 21 | Cube $(A^2)A\overset?=A(A^2)$ | **open**; I could not settle it; see D |

No checked proposition is incorrect. I found no gap that threatens the central theorem. The main value I can add beyond confirmation is in sections A (a simpler transfer), D.1–D.3 (structure of $A$: density, decomposition $A=\Delta_V\vee G$, Boolean-graph reformulation, a Boolean-valued sequence model) and E–F.

---

## (A) Precise verdict on the central nontransitivity theorem

**Verdict: correct.** $A\circ A\not\subseteq A$, hence $\mathcal D_Y\circ\mathcal D_Y\not\subseteq\mathcal D_Y$ for Arrieta's spatial, strongly Hausdorff locale $Y$ of Example 4.5. The proof in §5 is complete once the following four pieces are checked, all of which I did independently (details in B):

1. **The topology is Arrieta's.** Construction 4.2 (which Arrieta attributes to Juhász–Soukup–Szentmiklóssy, Lemma 2.1) takes a Hausdorff $X$, pairwise disjoint nonempty compact $K_n$, $Y_{Arr}=X\setminus\bigcup K_n$, and $Z_{Arr}=Y_{Arr}\sqcup\mathbb N$ with basis $\{U\cap Y_{Arr}\}\cup\{(U\cap Y_{Arr})\cup\{n\}: U\supseteq K_n\}$. Example 4.5 takes $X=\{0,1\}^{\mathbb N}$ and $K_n=\{a: a_n=1,\ a_m=0\ \forall m>n\}$. This is exactly the packet's §2 with the letter change (packet $V$, $Y$) $=$ (Arrieta $Y$, $Z$). Strong Hausdorffness is Corollary 4.3 (via Prop. 4.1, using that $\mathbb N$ is discrete, hence a spatial multiplier, and $Y_{Arr}$ regular); non-F-separatedness is Prop. 4.9/Cor. 4.10, proved through the *anti-Urysohn* property (Prop. 4.4, Def. 4.6, Lemma 4.7, Prop. 4.8). Arrieta nowhere discusses transitivity or composition; the nontransitivity theorem is new relative to the source.

2. **Formula (A) and test (Pair).** Correct (B.1–B.3, B.9).

3. **The triple.** $hAk$ and $kA\ell$ hold for *every* admissible cover; $\mathcal C_*$ is a cover, admissible, and separates $h$ from $\ell$ (B.10). The frame-homomorphism/pointless-locale bookkeeping is right: $T=\mathrm{Loc}(\mathrm{RO}(V))$ is nonzero, a map into a meet of opens factors iff each $f^*(\gamma)=1$, a map factoring through a pullback $A_{12}\wedge A_{23}$ is one whose two projections factor, and the composite with $\pi_{13}$ factors through the image. So $(h,\ell)$ factors through $A\circ A$ and not through $A$; hence $A\circ A\not\subseteq A$.

4. **Transfer to $Y$ — simpler than in the packet.** The packet transfers via block formula (B). That is valid, but **(B) is not needed** for the inequality. Only two trivialities are: $A\subseteq\mathcal D_Y$ (as sublocales of $Y^2$, via the open embedding $\iota^2:V^2\hookrightarrow Y^2$) and $A=\mathcal D_Y\wedge(V\times V)$ (definition). Then, with $\iota^3:V^3\hookrightarrow Y^3$ an open embedding (so images along it preserve meets) and $\pi^Y_{13}\circ\iota^3=\iota^2\circ\pi^V_{13}$,
   $$\iota^2[A\circ_V A]=\operatorname{im}\big(\iota^3[A_{12}\wedge A_{23}]\to Y^2\big)\subseteq\operatorname{im}\big((\mathcal D_Y)_{12}\wedge(\mathcal D_Y)_{23}\to Y^2\big)=\mathcal D_Y\circ\mathcal D_Y .$$
   If $\mathcal D_Y\circ\mathcal D_Y\subseteq\mathcal D_Y$ then $\iota^2[A\circ A]\subseteq\mathcal D_Y\wedge o(V\oplus V)=\iota^2[A]$, i.e. $A\circ A\subseteq A$, contradiction. So **$\mathcal D_Y^2\not\subseteq\mathcal D_Y$ is unconditional** given §5; the mixed-block lemma is only needed for the *equivalence* (Cube-Y) and for the converse $\mathcal D_Y>\Delta_Y\Rightarrow A>\Delta_V$.

Also note: (Triple) alone shows $A>\Delta_V$ (hence $\mathcal D_Y\neq\Delta_Y$): $(h,k)$ factors through $A$ but not through $\Delta_V$ because $h\ne k$ (take $a=[x_2=1,x_4=0]\cap V$; then $\widehat\sigma^{-1}a=[x_4=1,x_2=0]\cap V$ and $q(a)\ne q(\widehat\sigma^{-1}a)$). So the packet does contain an independent proof of Arrieta's non-F-separatedness for this $Y$; see D.1 for an even shorter one.

**Cleaner statement of the theorem (recommended).** For a $D$-preserving homeomorphism $f$ of $C$, put $\Gamma_f=\{(x,f x)\}\subseteq V^2$ (closed, $\cong V$) and $\mathfrak B(\Gamma_f)$ its Booleanization. The pair $(h_\pi,h_\kappa)=(\widehat\pi\times\widehat\kappa)\circ\delta\circ b$ (with $b:\mathfrak B(V)\hookrightarrow V$, $\delta$ the diagonal) has image exactly $\mathfrak B(\Gamma_{\widehat\kappa\widehat\pi^{-1}})$. So "$h_\pi A h_\kappa$" means $\mathfrak B(\Gamma_f)\subseteq A$ with $f=\widehat\kappa\widehat\pi^{-1}$, (Perm) reads

> $\mathfrak B(\Gamma_f)\subseteq A \iff P_f:=\{x\in D: x, f(x)\text{ lie in a common }K_n\}\text{ is dense in }C,$

and since $(x,fx,gfx)$ exhibits $\mathfrak B(\Gamma_{gf})\subseteq\mathfrak B(\Gamma_f)\circ\mathfrak B(\Gamma_g)$, the theorem is:

> **Theorem.** If $f,g$ are $D$-preserving homeomorphisms with $P_f,P_g$ dense and $P_{gf}$ not dense, then $\mathfrak B(\Gamma_{gf})\subseteq A^2\setminus A$. With $f=\widehat\sigma$, $g=\widehat\tau\widehat\sigma^{-1}$ (so $gf=\widehat\tau$): $P_{\widehat\sigma}\supseteq\{x: \max\operatorname{supp}x\text{ odd}\}$, $P_{\widehat\tau\widehat\sigma^{-1}}\supseteq\widehat\sigma\{x:\max\operatorname{supp}x\equiv2\ (4)\}$ are dense, and $P_{\widehat\tau}=\varnothing$ because $\max\tau(S)\ne\max S$ for every finite nonempty $S$.

This removes the locale $T$ and the maps $h,k,\ell$ from the statement entirely, and makes clear what the witness is: the Booleanization of the graph of $\widehat\tau$.

---

## (B) Proof-by-proof issues

Severity scale: **none** (correct as written), **minor** (correct, wording/justification should change), **moderate** (correct conclusion but the written argument has a real gap), **major** (incorrect or unprovable as stated). No item below is major or moderate.

**B.1 Cover presentation of $\mathcal D_Z$ (§3). Verified, severity none.** $\Delta\subseteq o(u)$ iff $\nabla(u)=1$ where $\nabla(a\oplus b)=a\wedge b$. Writing $u=\bigvee a_i\oplus b_i$, the family $\{a_i\wedge b_i\}$ covers and $\bigvee(a_i\wedge b_i)\oplus(a_i\wedge b_i)\le u$. So cover-opens are cofinal downward among open neighbourhoods of $\Delta$, and the meet is the fitted hull.

**B.2 Frame normal form (§2). Verified, none.** An open $U\subseteq Y$ is determined by $a=U\cap V$ and $S=U\cap N$, with $n\in S\iff n\in\Theta(a)$. Meets: $\Theta(a\wedge a')=\Theta(a)\wedge\Theta(a')$ (intersect the two neighbourhoods of $K_n$). Joins are componentwise. A useful reformulation the packet could add: the largest Cantor-open whose trace lies in $a=W\cap V$ is $\operatorname{int}_C(W\cup D)$, so $n\in\Theta(a)\iff K_n\subseteq\operatorname{int}_C(a\cup D)$. Admissible covers $=$ traces of $Y$-covers: both directions as stated.

*Minor:* "$V$ is open in $Y$, not necessarily open in $C$" — $V$ is **never** open in $C$ (its complement $D$ is dense).

**B.3 Formula (A) (§3). Verified, none.** $V\times V=o(V\oplus1)\wedge o(1\oplus V)=o(V\oplus V)$ (open embeddings are pullback-stable); $\downarrow\!(V\oplus V)\cong\mathcal O(V)\oplus\mathcal O(V)$; under this, $(a,S)\oplus(a,S)\wedge(V\oplus V)\mapsto a\oplus a$; meets of sublocales distribute over intersection with a fixed sublocale; the trace of a $Y$-cover is admissible and every admissible cover lifts. Also, for later use: refining an admissible cover inside the class of admissible covers (e.g. to clopen traces) does not change the meet, since finer covers give smaller $\gamma$.

**B.4 Vanishing mixed blocks (§3). Verified, severity minor.** The restriction of $\gamma_{\mathcal C}$ to $\{n\}\times V\cong V$ is $\beta_n(\mathcal C)=\bigvee\{a:(a,S)\in\mathcal C,\ n\in S\}$; the two-element covers give $\le$, and every cover has a member containing a basic neighbourhood of $n$ giving $\ge$, so $\mathcal D_Y\wedge(\{n\}\times V)\cong P_n=\bigwedge_{W\supseteq K_n}o_V(W\cap V)$. Then $P_n=j^{-1}[\bigwedge_W o_C(W)]=j^{-1}[\mathrm{fit}(K_n)]=j^{-1}[c(C\setminus K_n)]$ using that preimage of sublocales is a right adjoint (preserves meets) and $C$ is regular. **The correct final step is the closed-sublocale pullback formula** $j^{-1}[c(u)]=c(j^*u)$ with $j^*(C\setminus K_n)=V=1_V$, so $c(1)=\mathsf 0$. The packet's wording "a sublocale of that finite discrete locale, disjoint from $V$ at the level of points, so $P_n=0$" is not a valid general principle (a pullback of a sublocale can be nonzero and pointless); here it happens to be harmless only because the sublocale is closed. Rewrite the sentence.

**B.5 $N\times N$ block (§3). Verified, none.** $N\times N$ is closed in $Y^2$ with frame $\mathcal P(N)\oplus\mathcal P(N)\cong\mathcal P(N\times N)$ (discrete locales are locally compact); every sublocale of a Boolean frame is closed, i.e. a subset; points $(n,m)$, $n\ne m$, are excluded by a three-element cover; $(n,n)\in\Delta$.

**B.6 Block formula (B) (§3). Verified, none, but state it precisely.** The meaningful statement is $\mathcal D_Y=A\vee\Delta_N$ as sublocales of $Y^2$, where $A\subseteq V\times V$ and $\Delta_N\subseteq N\times N$. Proof: $Y^2=(V\times V)\vee(V\times N)\vee(N\times V)\vee(N\times N)$ because $o(u)\vee c(u)=1$ and $\mathcal S(Y^2)$ is a distributive lattice; intersect with $\mathcal D_Y$ and use B.4, B.5. The sentence "closed and open endpoint block embeddings preserve locale-surjections under pullback" is true (B.15) but is not what (B) needs; (B) needs only finite distributivity.

**B.7 (Cube-Y) (§3). Verified, none.** $A\circ\Delta_N=0$ since $A_{12}\wedge(\Delta_N)_{23}\subseteq V\times(V\wedge N)\times N=0$; images preserve finite joins; so $\mathcal D_Y^2=A^2\vee\Delta_N$, $(\mathcal D_Y^2)\mathcal D_Y=(A^2)A\vee\Delta_N$, $\mathcal D_Y(\mathcal D_Y^2)=A(A^2)\vee\Delta_N$, and intersecting with the open $V\times V$ recovers the $A$-terms. (Also $A\circ_YA=\iota^2[A\circ_VA]$ as in A.4.)

**B.8 Sierpiński transfer (§3). Not checked.** No statement of the "open retraction" or of the hypotheses on $u$ is given. I note only that any such transfer has to control an *image* under a non-open, non-proper map, so it cannot be a pure formality; it should be refereed from a written proof.

**B.9 (Pair) (§4). Verified, none.** $q$ is a frame homomorphism; $(h_\pi,h_\kappa)^*(\gamma_{\mathcal C})=\bigvee_a q(\widehat\pi_V^{-1}a\cap\widehat\kappa_V^{-1}a)=q(H_{\pi,\kappa}(\mathcal C))$, and $q(H)=1$ iff $H$ dense. $B$ is atomless because $V$ is crowded Hausdorff. (Convention check: $\widehat\pi$ preserves $V$, so $\widehat\pi^{-1}(W)\cap V=\widehat\pi_V^{-1}(W\cap V)$, which the proofs use silently.)

**B.10 The triple (§5). Verified, none; two minor presentation points.**
- $\sigma$, $\tau$ are bijections; $\tau$ has the single orbit $\cdots7\to5\to3\to1\to2\to4\to6\cdots$.
- $hAk$: with $n$ odd, $n>m$ and $n>\sigma(i)$ for $i\le m$, $x=$ prefix $+e_n$ has $\operatorname{supp}\widehat\sigma x=\sigma(\text{prefix})\cup\{n\}$, so $x,\widehat\sigma x\in K_n$; the rest is as written. Correct.
- $kA\ell$: $\sigma(n)=\tau(n)=n+2$ exactly when $n\equiv2\pmod 4$; correct.
- $h\not A\ell$: $\max\tau(S)\neq\max S$: for $n$ even $\tau(n)=n+2$; for $n$ odd $\tau^{-1}(n)=n+2\notin S$. Correct. The clopen $W_n$ exists: take disjoint clopens $W\supseteq K_n$, $W'\supseteq\widehat\tau K_n$ and $W_n=W\cap\widehat\tau^{-1}W'$ — **spell this out**, the packet just says "choose". $(\widehat\tau x)_1=x_3$ relies on the support convention; **state the convention as a displayed formula**, since with the other convention $(\widehat\tau x)_1=x_2$ and the $B_0$ argument breaks. The role of $B_0$ is only to dodge $\mathrm{Fix}(\widehat\tau)\cap V$ (which contains $0$ and $\mathbf 1$); any clopen on which $\widehat\tau$ has no fixed point works, and the whole third proof is literally the necessity half of (Perm) with $P=\varnothing$. I recommend proving (Perm) first and deriving the triple from it (see the Theorem in A).
- Localic conclusion: correct, see A.3.

**B.11–12. $A^2\not\subseteq A$, $\mathcal D_Y^2\not\subseteq\mathcal D_Y$. Verified**; the second without (B), see A.4.

**B.13 (Perm) (§6). Verified, none.** Sufficiency as written. Necessity: if $\operatorname{int}(\{\rho=\lambda\}\cap B)\ne\varnothing$ it meets $D$, and for $x\in D$ with $\rho x=\lambda x\in D$ both lie in the same $K_n$, so $x\in P$ — this uses that $\rho,\lambda$ preserve $D$, which is the standing hypothesis. $F(B)$ compact, disjoint from $\Delta$ and from each $K_n\times K_n$; clopen $W_n\supseteq K_n$ with $(W_n\times W_n)\cap F(B)=\varnothing$ exists since $K_n\times K_n$ is compact in the open complement of $F(B)$; finitely many $U_i$ by compactness of $C$ and $F(B)\cap\Delta=\varnothing$. The resulting cover is admissible and kills $B\cap V$. Note the nice by-product: **failure of the $A$-test is always witnessed by a single admissible cover**, consistent with §5.

**B.14 Diameter two (§6). Verified, none.** Agreement at infinitely many coordinates suffices (choose an agreement index whose common image exceeds all images of the prefix). The Baire argument is right (each $\{\sigma:\sigma(n)=\pi(n)\}$ is clopen in the Polish group $\mathrm{Sym}(\mathbb N)$, and $\bigcup_{n\ge N}$ is dense open) but a two-line back-and-forth construction of a permutation agreeing infinitely often with both $\pi$ and $\kappa$ is simpler. In graph language: $\mathfrak B(\Gamma_f)\subseteq A^2$ for every coordinate-permutation homeomorphism $f$.

**B.15 Point fibres (§7). Verified, none.** The cover $\{V\setminus\{p\},b\}$ is admissible since $p\notin K_n$. On $\{p\}\times V\cong V$ the restriction of $\gamma$ is $b$, so $A\wedge(\{p\}\times V)\subseteq\bigwedge_{b\ni p}o(b)=\mathrm{fit}(\{p\})=\{p\}$ by regularity. Induction: **surjections are stable under pullback along every open and every closed embedding** — because the pulled-back frame map is the restriction of the injective $f^*$ to $\downarrow u$ resp. $\uparrow u$ — so $(R\circ S)\wedge(\{p\}\times V)=\operatorname{im}(E\wedge(\{p\}\times V\times V))$, and $E\wedge(\{p\}\times V\times V)=\{p\}\times(S\wedge(\{p\}\times V))=\{(p,p,p)\}$ via pullbacks along projections (which preserve meets). This is exactly what the packet asserts; I recommend stating the one-line stability lemma explicitly, because it is the *only* kind of base change the whole packet is entitled to use, and its failure for fitted sublocales is the whole problem.

**B.16 Discrete refinement (§7). Verified, none.** $A\times_VV_d$ (fibre product over the **first** projection — say so) is $(d\times\mathrm{id})^{-1}[A]\subseteq V_d\times V=\coprod_pV$; sublocales of a coproduct are coproducts of sublocales (a frame congruence on a product of frames is determined by its restrictions to the complemented summands); each component is $A\wedge(\{p\}\times V)=\{(p,p)\}$; so the pullback is $V_d$ mapping onto $\Delta_V\neq A$.

**B.17 Open/proper (§7, optional). Not checked.** "If $\pi_1|_A$ were open (proper) then the pullback of the surjection $d$ along it would be surjective" needs a citation (Joyal–Tierney for open, Vermeulen for proper); I am not certain the open case is a theorem in the generality needed, so please cite precisely or drop the remark.

**B.18 Density/nonspatiality (§7, optional). Verified**, via D.1 below: $A$ itself (hence every power and both cube bracketings) is a dense sublocale of $V^2$; nonspatial since $\mathrm{pt}(A)=\Delta$ but $A>\Delta_V$.

**B.19 (CubeCong) (§8). Verified, none.** $\pi_{12}^{-1}[A^2]=(A^2)\times V$ has frame $(Q_2/K_2)\oplus L=Q_3/\widetilde K_{12}$, meets of sublocales are joins of congruences, images are quotients by kernels, sublocales of $V^2$ correspond to congruences on $Q_2$. It is an exact restatement of the definitions, so it is "correct" in the weakest sense: it contains no idea for comparing the two kernels. The honest wording "criterion, not solution" is appropriate.

---

## (C) Status of the reduction and supplementary propositions

- **Reduction $\mathcal D_Y\mapsto A$:** correct; (B) and (Cube-Y) verified. The *inequality* $\mathcal D_Y^2\not\subseteq\mathcal D_Y$ needs none of it (A.4).
- **Point fibres, discrete refinement:** verified. They prove that *some* surjection onto $A$ (and onto each power) is not stable along $\pi_1$. They do **not** say anything about the specific surjection $E\to A^2$ along the specific sublocale $(A^2)_{12}\wedge A_{23}$, as the packet correctly stresses.
- **(Perm), diameter two:** verified; genuine statements about generalized points over the single Boolean locale $T$, equivalently (A) about Booleanized graphs $\mathfrak B(\Gamma_f)$.
- **(CubeCong):** verified as reformulation.
- **New structural facts** that sharpen the reduction are in D.1–D.3.

---

## (D) What remains unresolved about associativity, and the best next experiment

I could not settle $(A^2)A\overset?=A(A^2)$. I record (D.1–D.3) what I could prove about $A$, which I believe changes the shape of the problem, then (D.4) the precise obstruction and (D.5) the experiments I would run.

### D.1 $A$ is dense in $V\times V$; $\mathcal D_Y\supseteq\mathfrak B(Y\times Y)$

**Lemma.** For every admissible cover $\mathcal C$, $\gamma_{\mathcal C}$ is a dense element of $Q_2$.

*Proof.* A nonzero element of $Q_2$ lies above some $a\oplus b$ with $a,b\neq0$; shrink to cylinder traces $[s]\cap V$, $[t]\cap V$. Pick $n>|s|,|t|$. Then $s0\cdots01$ and $t0\cdots01$ (the $1$ in position $n$) lie in $K_n$. Admissibility gives $c\in\mathcal C$ and open $W\supseteq K_n$ with $W\cap V\subseteq c$. $W\cap[s]$ and $W\cap[t]$ are nonempty opens of $C$, so they meet the dense $V$; hence $c\wedge a\ne0\ne c\wedge b$ and $(a\oplus b)\wedge(c\oplus c)\neq0$. $\square$

By Isbell's density theorem ($\mathfrak B(L)$ is the least dense sublocale), $A=\bigwedge o(\gamma_{\mathcal C})\supseteq\mathfrak B(V^2)$. The same argument for arbitrary $Y$-covers (members containing a neighbourhood of $K_n$ meet every pair of nonempty opens) gives $\mathcal D_Y\supseteq\mathfrak B(Y\times Y)$; since $\Delta_Y$ is closed with empty interior, $\Delta_Y\wedge\mathfrak B(Y^2)=0$, so **$\mathcal D_Y\neq\Delta_Y$ in one line.** This is really Arrieta's anti-Urysohn property (Prop. 4.4) in relational clothing. In general:

> **Lemma.** A locale $L$ is anti-Urysohn (Arrieta Def. 4.6: $a^*\vee b^*\ne1$ for all $a,b\ne0$) iff $\gamma_{\mathcal C}$ is dense in $L\oplus L$ for every cover $\mathcal C$. Hence for anti-Urysohn $L$, $\mathrm{fit}(\Delta_L)\supseteq\mathfrak B(L\oplus L)$, and $L$ is F-separated only if $L$ has no two disjoint nonzero elements.

($\Leftarrow$: if $a^*\vee b^*=1$ then $\{a^*,b^*\}$ is a cover whose $\gamma$ is disjoint from $a\oplus b$. $\Rightarrow$: a member $c$ with $c\not\le a^*$, $c\not\le b^*$ exists, else $1=\bigvee\mathcal C\le a^*\vee b^*$.) This is a mild strengthening of Arrieta's Lemma 4.7 + Prop. 4.8 and explains *why* the fitted diagonal is huge here: it contains the entire Booleanization of the square. Everything in the cube problem — $A$, $A^2$, both bracketings — is a dense sublocale of $V^2$ sandwiched between $\Delta_V\vee\mathfrak B(V^2)$ and $V^2$, with point set exactly $\Delta$. (Also: $A\ne\Delta_V\vee\mathfrak B(V^2)$; the witness $\mathfrak B(\Gamma_{\widehat\sigma})\subseteq A$ lies in $o(\delta)$ but not in $o(d_\sigma)$, $d_\sigma:=\bigvee\{a\oplus b: a\wedge b=0=a\wedge\widehat\sigma^{-1}b\}$, which is dense.)

### D.2 Decomposition $A=\Delta_V\vee G$ with $G$ pointless

Every admissible cover has the same $\gamma$ as a cover of the form $\{w_n\}_{n}\cup\mathcal U$ with $w_n=W_n\cap V$, $W_n\supseteq K_n$ open and $\mathcal U$ an arbitrary $V$-cover (adjoin the $w_n$ witnessing admissibility; this does not raise $\gamma$). Since $o(x\vee y)=o(x)\vee o(y)$ and finite joins distribute over arbitrary meets in the coframe $\mathcal S(V^2)$,
$$A=\bigwedge_{(W_n),\mathcal U}\big(o(g_{(W_n)})\vee o(\gamma_{\mathcal U})\big)=\underbrace{\bigwedge_{(W_n)}o\Big(\bigvee_n w_n\oplus w_n\Big)}_{=:G}\ \vee\ \underbrace{\bigwedge_{\mathcal U}o(\gamma_{\mathcal U})}_{=\mathcal D_V=\Delta_V}.$$
$G$ is symmetric, dense (D.1 applies to $g_{(W_n)}$), nonzero, **pointless** (for an ordinary $(p,p')$ choose every $W_n\not\ni p$), and contains $\mathfrak B(V^2)$ and $\mathfrak B(\Gamma_{\widehat\sigma})$. Because $R\circ\Delta=R=\Delta\circ R$ and images preserve finite joins,
$$A^2=A\vee G^2,\qquad (A^2)A=A\vee G^2\vee(G^2)G,\qquad A(A^2)=A\vee G^2\vee G(G^2),$$
and since $G$ is symmetric, $((G^2)G)^{\smile}=G(G^2)$. **Hence: the cube associates iff $(A^2)A$ is a symmetric relation.** The entire difficulty is concentrated in the pointless, Boolean-flavoured relation $G$, which is a meet over the *Baire space* $\mathbb N^{\mathbb N}$ (choices $m\mapsto W_n^{(m(n))}$ form a cofinal family): $G=\bigwedge_{m\in\mathbb N^{\mathbb N}}o\big(\bigvee_n w_n^{(m(n))}\oplus w_n^{(m(n))}\big)$. (By contrast $\Delta_V=\bigwedge_k o(\gamma_k)$ over the countably many cylinder covers of length $k$, by the Boolean-point argument in D.3.) The meet is **not** reducible to a countable one: ordinary points $(x,x)$ with gaps growing like $i\mapsto i$ satisfy all "$m(n)=n+k$" conditions but are excluded by $m(n)=2n+2$. So $G$ is governed by eventual-domination combinatorics on gap sequences, not by a metric.

### D.3 A Boolean-valued sequence model (complete for sublocales, but not for images)

Two facts make Boolean-valued points the right language, and one fact limits them.

(i) *Sublocales are determined by their Boolean sublocales:* $S=\bigvee_{a\in S}\mathfrak b(a)$ with $\mathfrak b(a)=\{x\to a\}=\mathfrak B(c(a))$ (Picado–Pultr). So $S\subseteq S'$ iff every map from a Boolean locale that factors through $S$ factors through $S'$.

(ii) *Boolean points of $V$ are sequences.* Since $C$ is Polish and $D$ countable, the induced sublocale $V\subseteq C$ equals $\bigwedge_{k\in D}o(C\setminus\{k\})$ (if $U\subseteq\operatorname{int}(U\cup D)$ were strict, $\operatorname{int}(U\cup D)\setminus U$ would be a nonempty countable relatively closed, hence Polish, set, with an isolated point $k$ — Cantor–Bendixson — making $U\cup\{k\}$ open). Frame maps $\mathcal O(C)\to B$ are Boolean maps $\mathrm{Clop}(C)\to B$, i.e. sequences $(b_i)\in B^{\mathbb N}$. Hence
$$\mathrm{Loc}(B)\to V\quad\longleftrightarrow\quad (b_i)\in B^{\mathbb N}\ \text{ with }\ \textstyle\bigwedge_i(b_i\leftrightarrow k_i)=0\ \ \forall k\in D,$$
"$x$ is forced not to be any ground-model finitely supported nonzero sequence". For two such points $x=(b_i)$, $y=(c_i)$ write $[x=y]=\bigwedge_i(b_i\leftrightarrow c_i)$ and $g_m(x,y)=\bigvee_n\big(b_n\wedge c_n\wedge\bigwedge_{n<j\le m(n)}\neg b_j\wedge\neg c_j\big)$. Then (using the cofinal covers of D.2 and $\bigwedge_{\mathcal U}\bigvee_{u\in\mathcal U}x^*(u)\wedge y^*(u)=[x=y]$, together with complete distributivity in $B$):
$$(x,y)\in G\iff\forall m:\ g_m(x,y)=1,\qquad (x,y)\in A\iff\forall m:\ g_m(x,y)\ge[x\ne y].$$
This recovers all of §5–§7 by computation (e.g. $h_\pi$ is $b_i=([x_{\pi(i)}=1]\cap V)$ in $\mathrm{RO}(V)$) and turns the cube into a question about $B$-names for elements of $2^{\mathbb N}$ and ground-model functions $m$ — a forcing-flavoured combinatorics problem.

(iii) *Limit — do not confuse (i) with liftability.* A Boolean point of an image $\operatorname{im}(E\to S)$ need **not** lift to $E$, even after a Boolean cover: pullback of a surjection along a Boolean sublocale can be empty (discrete refinement $d:\mathbb R_d\to\mathbb R$ has $d^{-1}[\mathfrak B(\mathbb R)]=\bigcap\{\text{dense opens}\}=\varnothing$). Surjections *are* stable along open and closed embeddings, and along arbitrary joins of sublocales along which they are stable; not along fitted or Boolean sublocales. I flag this because it is exactly the trap one falls into when trying to upgrade (i) to a pointwise computation of $A^2$.

### D.4 The precise obstruction

With $E=A_{12}\wedge A_{23}\twoheadrightarrow A^2$ and $F_L=(A^2)_{12}\wedge A_{23}$, the triple source $E_3=A_{12}\wedge A_{23}\wedge A_{34}$ is the pullback of $E\to A^2$ along $F_L\to A^2$, and $(A^2)A\supseteq A^{[3]}:=\operatorname{im}(E_3\to V^2_{14})\subseteq A(A^2)$. Associativity holds if the pullback $E_3\to F_L$ is surjective, i.e. if the surjection $E\times V\twoheadrightarrow A^2\times V$ is stable along the fitted sublocale $(A^2\times V)\wedge(V\times A)$. By D.2 the $\Delta$-part of $A$ contributes a stable (isomorphic) piece; **the whole question is the stability of $G_{12}\wedge G_{23}\twoheadrightarrow G^2$ (and its iterate) along $V\times G$**, a meet of countable joins of open squares indexed by $\mathbb N^{\mathbb N}$. Nontransitivity is irrelevant to this, as the packet says. Both bracketings contain $A^{[3]}$ and are contained in the manifestly symmetric naive bound $N_3=\bigwedge_{\mathcal C,\mathcal C',\mathcal C''}o\big(\bigvee\{a\oplus c:\exists b\in\mathcal C',\ a\wedge b\ne0\ne b\wedge c\}\big)$.

### D.5 Best next experiments, in order

1. **Is $G^2$ equal to its naive bound?** $N(G,G)=\bigwedge_{m,m'}o\big(\bigvee\{w_n^{(m(n))}\oplus w_{n'}^{(m'(n'))}: W_n^{(m(n))}\cap W_{n'}^{(m'(n'))}\ne\varnothing\}\big)$, where the compatibility is: $n=n'$, or $n<n'$ and $n'>m(n)$, or symmetrically. If naive bounds are exact at every stage, both bracketings equal $N_3$ and the cube associates. If $G^2\subsetneq N(G,G)$, that gap is a concrete instance of image instability and the natural place to look for cube failure. In the model of D.3: given $(x,z)$ with $\bigvee_{(n,n')\text{ compatible}}[x\in W_n^{(m(n))}]\wedge[z\in W_{n'}^{(m'(n'))}]=1$ for all $m,m'$, either construct a **single** $B$-valued $y$ (over some Boolean extension of $B$, which is allowed) with $g_m(x,y)=g_m(y,z)=1$ for all $m$, or prove none exists. The obvious candidate $y=x\wedge z$ (coordinatewise) handles only the diagonal terms $n=n'$ and may be forced finitely supported nonzero, so it is not in $V$; the issue is a uniformization over all ground-model $m,m'$ at once. I expect this to be decidable with forcing-style arguments (the relevant invariant is whether the gap function of the common support is dominated by a ground-model function).

2. **Closed-graph probes.** For a $D$-preserving homeomorphism $f$, stability along the closed $\Gamma_f$ gives computable restrictions:
$$(A^2)A\wedge\Gamma_f\ \cong\ \pi_1\big[A^2\wedge(f\times\mathrm{id})^{-1}A\big],\qquad A(A^2)\wedge\Gamma_f\ \cong\ \pi_1\big[A\wedge(f\times\mathrm{id})^{-1}A^2\big]$$
as sublocales of $V$ (using $A^{\smile}=A$, $(A^2)^{\smile}=A^2$). A nonassociativity witness would be an $f$ for which these two sublocales of $V$ differ; by the symmetry reformulation of D.2 it suffices to find $f$ with $(A^2)A\wedge\Gamma_f\ne(A^2)A\wedge\Gamma_{f^{-1}}$ transported by $f$. Coordinate permutations will *not* work (all their Booleanized graphs already lie in $A^2$ by diameter two); one needs $D$-preserving homeomorphisms that are not coordinate permutations, or non-graph Boolean points.

3. **Replace (CubeCong) by a tractable countable presentation.** $Q_3$ is countably presented ($\mathcal O(V)=\mathcal O(C)/\langle C\setminus\{k\}=1:k\in D\rangle$), and $\Delta_V$ needs only countably many relations, but $G$ needs the $\mathbb N^{\mathbb N}$-indexed family. Any attempt to "compute the kernels" should first decide whether a $\le^*$-dominating subfamily of $\mathbb N^{\mathbb N}$ suffices (it does for the *eventual* part of the conditions; the finitely many initial terms are what break naive cofinality).

4. **Only after 1–3:** the Sierpiński transfer and the "seven of eight words" claims, from written proofs.

---

## (E) First-reading and presentation comments

1. **Letters.** Arrieta's $Y$ is the packet's $V$ and Arrieta's $Z$ is the packet's $Y$; say so once. The set $D$ (finite supports) collides with the hull $\mathcal D$ and with Arrieta's $D_L$ for the diagonal. $K_2=\ker\phi_{13}$ collides with $K_n$. $B=\mathrm{RO}(V)$ collides with the cylinders $B_0$, $B$. Rename at least $D$ and $K_2$.
2. **Convention.** Display $(\widehat\pi x)_j=x_{\pi^{-1}(j)}$ once; two proofs silently depend on it.
3. **§0** refers to $\mathcal U$, to a "one-generator Sierpiński-transfer counterexample", to "seven of eight words" and to a general $(RR)R\neq R(RR)$ example, none of which is in the packet. Either include statements or mark them as outside the audit.
4. **Hausdorff vs strongly Hausdorff.** The packet correctly cites Cor. 4.3; add a footnote that a Hausdorff *space* need not be strongly Hausdorff as a locale (Arrieta needs the spatial-multiplier hypothesis of Prop. 4.1), so the citation is not decorative.
5. **§3 block lemma**: replace the "disjoint at the level of points" sentence by the closed-pullback formula (B.4). State the one-line stability lemma for open/closed embeddings (B.15) once and refer to it.
6. **§5**: spell out the choice of $W_n$ (B.10); either derive the third proof from (Perm) or say it is a special case; consider the graph-Booleanization statement (A) which eliminates $T,h,k,\ell$.
7. **§6**: the clause "Scope: this is only a statement about this family" is good; add that it shows $\mathfrak B(\Gamma_f)\subseteq A^2$ for every coordinate permutation $f$, so coordinate permutations cannot separate $A^2$ from anything above it.
8. **§7**: specify "fibre product over the first projection".
9. **§8**: say explicitly that (CubeCong) is definitional and that its content is nil without a method for the kernels.
10. **Simplifications**: (a) transfer without (B) (A.4); (b) one-line non-F-separatedness via density (D.1); (c) $A=\Delta_V\vee G$ and "cube $\iff$ $(A^2)A$ symmetric" (D.2); (d) direct back-and-forth instead of Baire (B.14).

---

## (F) Bibliographical and originality cautions

1. **Construction.** Arrieta attributes Construction 4.2 to Juhász–Soukup–Szentmiklóssy (Lemma 2.1 of their work on anti-Urysohn spaces); the packet should credit them and should say that Arrieta's route to non-F-separatedness is anti-Urysohn $\Rightarrow\neg(\mathrm F)$ (Lemma 4.7, Prop. 4.8), since D.1 is the relational version of precisely that argument. Arrieta's paper contains no statement about transitivity or composition of the fitted diagonal; the nontransitivity theorem is not in the source.
2. **Nonassociativity of localic relational composition** is, to my knowledge, folklore (the pullback of a surjection need not be a surjection, so sublocales of products do not form an allegory). I cannot point to a published counterexample for a reflexive symmetric endorelation; before claiming novelty for §0's example, check the literature on localic/quantale-valued relations (Vickers, Townsend, Resende; Picado–Pultr, *Separation in Point-Free Topology*, 2021, for the fitted-diagonal viewpoint). I could not verify any antecedent for "fitted diagonal not transitive"; treat as plausibly new but unsearched.
3. **Standard facts used** (cite rather than reprove): Isbell density theorem; $\mathfrak B(L)=\bigwedge\{o(d): d\text{ dense}\}$; sublocales as joins of Boolean sublocales $\mathfrak b(a)$ (Picado–Pultr, *Frames and Locales*); image/preimage adjunction and $f^{-1}[c(u)]=c(f^*u)$, $f^{-1}[o(u)]=o(f^*u)$; pullback-stability of open and closed embeddings; Joyal–Tierney for open surjections, Vermeulen for proper maps (only if B.17 is kept).
4. **Spatiality of products.** Nothing in the verified parts needs $V\times V$ or $Y\times Y$ to be spatial; I recommend the packet state this explicitly, since readers will wonder, and since the whole phenomenon lives in the pointless part $G$.
5. **No provenance problem detected.** All numerical/combinatorial claims (orbit of $\tau$, $\sigma(n)=\tau(n)$ iff $n\equiv2\pmod 4$, $\max\tau(S)\ne\max S$, $|K_n|=2^{n-1}$) check.

---

*End of report. I did not consult the internal audit, the GitHub notes or any prior comparison.*