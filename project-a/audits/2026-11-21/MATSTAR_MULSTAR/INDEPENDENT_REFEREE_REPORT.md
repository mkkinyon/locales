# Independent blind referee report: MAT*, MUL*, and FINMAT*

**Submission:** `ProjectA_MATstar_MULstar_BLIND_AUDIT_2026-11-21.zip`  
**Date of review:** 21 November 2026  
**Material examined:** `00_README_FIRST.md` through `05_SOURCE_AND_PROVENANCE_FOR_REFEREE.md`, in the prescribed order. No earlier project referee reports or internal adjudications were consulted.  
**Scope:** Mathematical correctness of the arbitrary-locale, locally compact scattered-index assertions; not novelty of the broader research program.

## 1. Executive verdict

| Claim | Verdict | Qualification |
|---|---|---|
| **MAT*** | **Valid as stated.** | The transfinite exhaustion argument works for **every locale** \(P\), including pointless and nonregular locales. Several topological and sublocale lemmas should be stated explicitly, but they are valid. |
| **MUL*** | **Valid as stated.** | This is a formula for the **actual binary localic composite**. The proof correctly avoids any assertion that image commutes with arbitrary base change, or that meets distribute over infinite sublocale joins. |
| **FINMAT*** | **Valid as stated.** | The finite-support and restricted associativity arguments work. The requirement of finite-join distributivity on the base algebra can in fact be dropped: for sublocale relations, binary composition already preserves finite joins in each variable. |

**Overall recommendation:** Accept the mathematical conclusions after a modest proof-level revision making the key localization and image facts explicit. I found **no counterexample, hidden hypothesis on \(P\), or fatal gap**. This is a positive verdict on the statements and arguments submitted, *not* a certification of any other results in the project.

The central reason the extension works is that the proof uses an **open cover of the ambient locale**, which remains a cover after pullback to *any* sublocale, and a **finite closed/open decomposition**; it never attempts a generally invalid interchange of an arbitrary sublocale meet with an arbitrary sublocale join.

## 2. Definitions and categorical preliminaries independently checked

Throughout, \(\operatorname{Sub}(X)\) means the coframe of *sublocales*, not the poset of subsets of \(\operatorname{pt}(X)\). If \(a:A\hookrightarrow X\) is a sublocale inclusion, there is an order isomorphism
\[
\operatorname{Sub}(A)\simeq\{W\in\operatorname{Sub}(X):W\le A\}.
\tag{2.1}
\]
Consequently, joins of sublocales of \(A\) are the same joins when regarded as sublocales of \(X\).

The coframe law says that **finite joins distribute over arbitrary meets**. In particular its underlying lattice is distributive for *finite* operations. It does **not** follow that
\(W\wedge\bigvee_\lambda A_\lambda=\bigvee_\lambda(W\wedge A_\lambda)\)
for arbitrary sublocales \(A_\lambda\). The candidate does not use that invalid rule.

### 2.1. Open-cover localization (A1; candidate lines 46–52)

**Verdict: correct for an arbitrary locale and an arbitrary sublocale.** Here is a proof with the necessary embeddings made explicit.

Let \(i:W\hookrightarrow X\) be the sublocale embedding and let \(\bigvee_a u_a=1\) in \(\mathcal O(X)\). Since \(i^*:\mathcal O(X)\to\mathcal O(W)\) is a frame homomorphism,
\[
\bigvee_a i^*(u_a)=1_W.
\]
The open sublocales \(O_W(i^*u_a)\) therefore join to all of \(W\) **in** \(\operatorname{Sub}(W)\). Their images under (2.1) are precisely
\(W\wedge O_X(u_a)\). Since (2.1) respects their joins,
\[
W=\bigvee_a\bigl(W\wedge O_X(u_a)\bigr).
\tag{2.2}
\]
No spatiality, compactness, regularity, overtness, or points of \(W\) are involved. Importantly, this is a *special open-cover identity*, not a general coframe distributivity assertion.

### 2.2. Closed/open decomposition (A2; lines 54–60)

**Verdict: correct.** For \(u\in\mathcal O(X)\), the open sublocale \(o(u)\) and its closed complement \(c(u)\) are complementary **elements of** \(\operatorname{Sub}(X)\):
\[
o(u)\vee c(u)=X,\qquad o(u)\wedge c(u)=0.
\]
In nucleus notation their defining operations are \(x\mapsto (u\Rightarrow x)\) and \(x\mapsto(u\vee x)\), respectively. Since \(\operatorname{Sub}(X)\) is finitely distributive,
\[
W=W\wedge(o(u)\vee c(u))=(W\wedge o(u))\vee(W\wedge c(u)).
\tag{2.3}
\]
The analogous finite clopen partition identity follows by iteration. The two pieces need **not** amount to a coproduct decomposition of the underlying locale, and none is asserted. Equation (2.3) is legitimate even though arbitrary meets over arbitrary joins are problematic.

A useful stronger fact: **meet with a complemented element in any distributive complete lattice preserves all joins**. For a complement \(e'\) of \(e\),
\(e\wedge x\le b\iff x\le e'\vee b\) when \(b\le e\); equivalently, \(x\mapsto e\wedge x\) has a right adjoint, and so preserves joins. In particular,
\[
e\wedge\bigvee_\lambda W_\lambda
 =\bigvee_\lambda(e\wedge W_\lambda)
\tag{2.4}
\]
for **complemented** \(e\). This offers a shorter alternative verification of the fixed-sector calculation in §4. Compare Picado–Pultr (2019), Proposition 1.5 (reference in §8 below).

### 2.3. Localic image and pullback (B2–B4; lines 123–136)

For a locale morphism \(f:X\to Y\), let \(f^{-1}:\operatorname{Sub}(Y)\to\operatorname{Sub}(X)\) denote **pullback of sublocales**. The smallest-sublocale image \(f_!:\operatorname{Sub}(X)\to\operatorname{Sub}(Y)\) exists and satisfies
\[
 f_!(A)\le B\quad\Longleftrightarrow\quad A\le f^{-1}(B).
\tag{2.5}
\]
This is the sublocale-image/pullback adjunction. Thus \(f_!\) preserves arbitrary joins, even for nonproper or nonopen \(f\). The inverse-image operation is functorial, preserves arbitrary meets and finite joins, and its image adjoints compose:
\[
(gf)_!=g_!f_!.
\tag{2.6}
\]
For a sublocale embedding \(i:A\hookrightarrow Y\), \(i_!\) simply regards a sublocale of \(A\) as a sublocale of \(Y\).

One can see existence independently from the frame homomorphism of a map \(h:V\to Y\): its kernel frame congruence determines the quotient frame of the smallest image sublocale through which \(h\) factors. This image is *not* the set-theoretic image of ordinary points, and (2.5) is not an assertion of pullback stability of images.

## 3. Proof of MAT*: detailed audit

### 3.1. Compact scattered Hausdorff index (A3, A4; lines 64–83)

The topological facts used here are sound, but deserve a few explanatory sentences:

1. A compact scattered Hausdorff space is **zero-dimensional**. Indeed, a nontrivial connected subspace cannot be scattered; the compact space is totally disconnected; compact Hausdorff total disconnectedness gives a clopen basis.
2. If \(K\ne\varnothing\) is compact and scattered, its Cantor–Bendixson height is a **successor** ordinal \(\alpha+1\). Its final nonempty derivative \(F=K^{(\alpha)}\) is compact and discrete, hence **finite**. The derivative process must terminate (otherwise one obtains a nonempty closed subset without an isolated point); compactness rules out termination at a limit ordinal by the finite-intersection property.
3. Finite clopen separation produces a clopen partition \(K=\bigsqcup_{r=1}^m N_r\) with \(N_r\cap F=\{k_r\}\). Since the clopen \(N_r\) is compact, this remains a finite decomposition.
4. For \(x\in N_r\setminus\{k_r\}\), choose a clopen \(C\subseteq N_r\setminus\{k_r\}\) containing \(x\). It is compact and avoids \(F\). For any clopen \(C\subseteq K\), derivatives satisfy \(C^{(\beta)}=C\cap K^{(\beta)}\) by transfinite induction, so \(C^{(\alpha)}=\varnothing\). The Cantor–Bendixson height of nonempty \(C\) is strictly below that of \(K\).

Now apply transfinite induction to the assertion
\[
E(K;P,W):\qquad
W=\bigvee_{k\in K}\bigl(W\wedge(P\times\{k\})\bigr)
\quad\text{for every }W\le P\times K.
\tag{3.1}
\]
Each \(P\times N_r\) is a clopen sublocale of \(P\times K\). In it, (2.3) splits \(W\) between the **closed** sector \(P\times\{k_r\}\) and the **open** complement \(P\times(N_r\setminus\{k_r\})\). The latter is covered by open sets \(P\times C\), with \(C\) as in point 4. Equation (2.2) localizes its sublocale to these charts, each of which satisfies the induction hypothesis. Their singleton-sector restrictions are the restrictions of the original \(W\), because intersections and sector inclusions are compatible. Rejoin the charts, their apices, and the finitely many \(N_r\). This proves (3.1).

**Crucial generality check:** the entire induction is performed in \(\operatorname{Sub}(P\times K)\); the only properties of \(P\) used are the existence of products and of sublocale pullbacks. In particular, \(P\) need not possess points, and no compact-Hausdorff or spatial argument about \(P\) has slipped in.

### 3.2. Locally compact (possibly noncompact) index (A5; lines 85–95)

The needed compact clopen chart fact follows particularly cleanly from one-point compactification. If \(K\) is locally compact Hausdorff, its one-point compactification \(K^+\) is compact Hausdorff. If \(K\) is scattered, so is \(K^+\): every nonempty subset meeting \(K\) has a relatively isolated point **inside the open part** \(K\), while \(\{\infty\}\) is a singleton. Thus \(K^+\) is zero-dimensional. For each \(k\in K\), choose a clopen neighborhood in \(K^+\) containing \(k\) but avoiding \(\infty\). It is compact clopen in \(K\). (If \(K\) is already compact, the conclusion follows directly.)

These compact clopen sets form an **open cover** of \(K\). Their inverse-image opens in \(P\times K\) cover the product for every locale \(P\). Apply (2.2) and then (3.1) within each \(P\times C\). This proves (3.1) for all locally compact scattered Hausdorff \(K\), without a compactness assumption on \(P\) or \(K\).

This also handles topological sums of compact scattered spaces and the locally compact noncompact ordinal \([0,\omega_1)\). The proof is genuinely local in the **index**, not in the parameter.

### 3.3. Reconstruction/injectivity (A6, A7; lines 97–107)

Let \(E_k=P\times\{k\}\). Since \(K\) is Hausdorff, \(E_k\) is a **closed** sublocale of \(P\times K\), complemented by the open sublocale \(P\times(K\setminus\{k\})\). Distinct \(E_j,E_k\) have zero meet.

For arbitrary entries \(V_j\le E_j\), the complemented-sector distributivity (2.4) gives
\[
 E_k\wedge\bigvee_j V_j
 =\bigvee_j(E_k\wedge V_j)=V_k.
\tag{3.2}
\]
This uses no generally invalid infinite coframe distributivity: the factor \(E_k\) is **complemented**. Alternatively, the candidate's explicit argument puts \(\bigvee_{j\ne k}V_j\) below the complementary open sector and applies only a finite distributivity step; that argument is likewise sound.

Consequently \(\Phi\Sigma=\mathrm{id}\), and (3.1) gives \(\Sigma\Phi=\mathrm{id}\). Both maps are order preserving, so they are inverse **complete-lattice** order isomorphisms. This proves MAT* exactly as stated. The result neither identifies open sublocales coordinatewise nor identifies \(P\times K\) as a localic coproduct of isolated copies of \(P\).

**Degenerate cases:** if \(K=\varnothing\), both sides of MAT* are one-element lattices (\(P\times\varnothing\) is the empty locale). If \(K\) is one point, MAT* is the tautological identification with \(\operatorname{Sub}(P)\). If \(P\) is the empty locale, every matrix entry and every sublocale of the product is empty and the result again holds. These cases require no extra hypothesis.

## 4. Proof of MUL*: actual localic relation composition

### 4.1. Finite powers of the index (B1; candidate lines 23, 111)

Finite products of scattered spaces are scattered: given nonempty \(A\subseteq K_1\times K_2\), choose an isolated point in its projection to \(K_1\), then an isolated point in the corresponding fiber in \(K_2\); the pair is isolated in \(A\). The argument iterates. Finite products of locally compact Hausdorff spaces are locally compact Hausdorff. Moreover the product locales of these spatial locally compact Hausdorff spaces agree with their ordinary topological products. Thus MAT* applies to \(P^n\times K^n\) for \(n=2,3\), and \((P\times K)^n\cong P^n\times K^n\) categorically for any \(P\).

### 4.2. Exact triple-sector calculation (B2; lines 111–127)

Put \(G=P\times K\), let \(R,S\le G^2\), and let
\[
Q=\pi_{12}^{-1}R\wedge\pi_{23}^{-1}S\le G^3.
\]
Write \(e_{ijk}:P^3\hookrightarrow G^3\) for the closed triple sector and \(e_{ij}:P^2\hookrightarrow G^2\) for a double sector. The squares relating \(e_{ijk}\), \(\pi_{12}\), \(e_{ij}\) and \(\pi_{12}^P\) (and analogously \(\pi_{23}\)) commute and are pullback squares of product sectors. Functoriality of sublocale pullback and preservation of finite meets give
\[
\begin{aligned}
Q_{ijk}
&=e_{ijk}^{-1}Q\\
&=(\pi_{12}^P)^{-1}(e_{ij}^{-1}R)
 \wedge(\pi_{23}^P)^{-1}(e_{jk}^{-1}S)\\
&=(\pi_{12}^P)^{-1}(R_{ij})
 \wedge(\pi_{23}^P)^{-1}(S_{jk}).
\end{aligned}
\tag{4.1}
\]
This is an equality of actual **sublocales of \(P^3\)**, not of point sets. The triple-sector decomposition from MAT* then says
\(Q=\bigvee_{i,j,k}(e_{ijk})_!Q_{ijk}\).

### 4.3. Image computation without Beck–Chevalley (B3–B5; lines 129–142)

Let \(d_{ik}:P^2\hookrightarrow G^2\) be the output-sector inclusion and \(p=\pi_{13}^P:P^3\to P^2\). The relevant composite **of maps**, restricted to the \((i,j,k)\) sector, is
\[
\pi_{13}\,e_{ijk}=d_{ik}\,p.
\tag{4.2}
\]
Using join preservation and functoriality of **image** ((2.5)–(2.6)), and the fact that image along \(d_{ik}\) is just sublocale inclusion,
\[
\begin{aligned}
\operatorname{im}_{\pi_{13}}Q
&=\bigvee_{i,j,k}
  (\pi_{13}e_{ijk})_!Q_{ijk}\\
&=\bigvee_{i,j,k}
  (d_{ik})_!\bigl(p_!Q_{ijk}\bigr)\\
&=\bigvee_{i,k}(d_{ik})_!
  \left(\bigvee_j (R_{ij}\circ_P S_{jk})\right).
\end{aligned}
\tag{4.3}
\]
Finally apply the reconstruction/injectivity statement (3.2) for the double sectors. This yields precisely
\[
\boxed{(R\circ S)_{ik}=\bigvee_{j\in K}(R_{ij}\circ_P S_{jk}).}
\tag{4.4}
\]

**This is the decisive categorical point.** There is *no* invocation of the generally false rule that localic images are stable under arbitrary pullback. The candidate first constructs the genuine composability pullback \(Q\); only *then* does it decompose \(Q\) and use image-preservation of joins. Also, it never needs to distribute the composability **meet** over either infinite matrix join. Thus MUL* is valid for arbitrary, potentially pointless entry sublocales.

The formula is **binary**. It does *not* imply associative multiplication of unrestricted matrices, because rebracketing triple composites would still require associativity of the base \(\circ_P\).

## 5. FINMAT*: closure and path expansion

Let \(A\subseteq\operatorname{Sub}(P^2)\) contain \(0,\Delta_P\), be closed under converse, genuine composition and finite joins, and suppose composition is associative on \(A\). For matrices \(R,S\) with finite support in every row and column, equation (4.4) gives each entry as a **finite** join. Explicitly, for fixed \((i,k)\), only the finite set \(\{j:R_{ij}\ne0\}\) can contribute, and zeros compose to zero. Hence each entry is in \(A\).

Row support is finite because
\[
\operatorname{supp}(R\circ S)_{i,*}
\subseteq\bigcup_{j\in\operatorname{supp}R_{i,*}}
\operatorname{supp}S_{j,*},
\]
a finite union of finite sets. The analogous proof using finite columns establishes column support. Finite joins and transpose preserve both kinds of finiteness (C1).

The **actual localic diagonal** of \(G\) has entries \(\Delta_P\) on \((i,i)\) and \(0\) off the index diagonal, by pulling back the diagonal along each double sector. It is row-and-column finite, and \(\Delta_P\) is a two-sided unit under genuine \(\circ_P\), by the usual diagonal pullback identifications. MUL* now makes \(\Delta_G\) a genuine two-sided unit on the matrix class (C2).

For \(R,S,T\) in the class, fixing \(i,\ell\) leaves only finitely many contributing pairs \((j,k)\). Associativity on \(A\) and finite join distributivity permit rebracketing, yielding equality in every \((i,\ell)\) sector. By MAT* this is equality of **genuine sublocales** of \(G^2\), not merely coefficientwise formal equality (C3).

Induction gives the claimed length-\(n\) path formula for \(n\ge1\): row finiteness ensures finitely many paths from each fixed start vertex after any fixed finite number of steps. For \(n=0\), use \(R^0=\Delta_G\) with the empty path contributing \(\Delta_P\) when the endpoint equals the start and \(0\) otherwise (C4).

### A useful simplification of FINMAT*'s hypotheses

**Finite-join distributivity need not be assumed separately.** For arbitrary localic sublocale relations, pullback of sublocales preserves **finite joins** (it is a coframe morphism), finite meets distribute over finite joins in \(\operatorname{Sub}(P^3)\), and sublocale image preserves **all** joins. Therefore
\[
R\circ_P(S\vee T)=(R\circ_P S)\vee(R\circ_P T),\qquad
(R\vee S)\circ_P T=(R\circ_P T)\vee(S\circ_P T),
\tag{5.1}
\]
and composition with \(0\) gives \(0\). This does **not** assert any *infinite*-join distributivity and does **not** confer associativity. Thus closure of \(A\) under finite joins and composition, together with associativity on \(A\), already supplies the distributivity property used in the matrix proof.

## 6. Adversarial boundary checks and proposed refinements

| Packet item | Finding |
|---|---|
| **Nonspatial \(P\); \(K=\omega+1\)** | The compact-height induction applies unchanged to every sublocale of \(P\times(\omega+1)\). A nonzero sublocale with all singleton fibers zero would contradict (3.1), even if it has no ordinary points. |
| **Noncompact \(K\)** | Open localization over compact clopen charts proves the theorem for topological sums and for \([0,\omega_1)\); global compactness is unnecessary. |
| **Perfect compact \(K\)** | Scatteredness is substantive. For example, the Booleanization of \([0,1]\), obtained from the double-negation nucleus, is nonzero and has no points: its frame of regular opens is atomless as a complete Boolean algebra. Its intersection with each singleton point-sector is therefore zero. MAT* fails already for \(P=1\) if \(K=[0,1]\). |
| **Implicit compact/spatial \(P\)** | None found. No step uses support-theoretic arguments, regularity of \(P\), openness/properness of the projection from \(P\times K\), or the existence of points of \(P\). |
| **Associativity trap** | The submitted proof establishes **binary** MUL* and restricted FINMAT* only. It never derives unrestricted associativity. No independent explicit nonassociativity example is needed to verify these two statements, and I have not claimed one here. |
| **Degenerate locales/indexes** | Empty index, singleton index, and empty parameter all satisfy MAT*, MUL*, and the corresponding trivial matrix statements with conventional empty-join interpretation. |

**Additional defensible weakening:** The compact-clopen-chart argument can be replaced by a finite Cantor–Bendixson-height induction for **any scattered Hausdorff \(K\) of finite derivative height**, without local compactness. Indeed, split the first isolated stratum (an open discrete subspace) from its closed derivative, apply open-cover localization to the isolated stratum and induct on the derivative. This is a separate sufficient hypothesis; it does not establish the arbitrary-locale theorem for *all* scattered Hausdorff spaces of unbounded or limit height without local compactness. I do not recommend enlarging the submitted main statement without a distinct proof.

## 7. Precise editorial recommendations, by source location

These are **clarifications, not mathematical corrections**:

1. **§1, lines 46–52:** Insert the one-paragraph proof of OpenLoc in §2.1 above. It is the principal justification that arbitrary sublocales of an arbitrary parameter are covered correctly.
2. **§1, lines 54–60:** Explicitly note that open and closed complementary sublocales are complementary *in the sublocale lattice*, and cite finite (not infinite) distributivity.
3. **§2, lines 66–76:** Justify successor Cantor–Bendixson height, finite final derivative, the clopen finite partition, and the derivative-height reduction for clopen charts. These are nontrivial, although classical, topological facts.
4. **§3, line 87:** Prove the compact clopen neighborhood fact by one-point compactification (as in §3.2). This makes the noncompact extension transparent.
5. **§4, lines 99–103:** Either retain the candidate's valid open-complement argument, or shorten it using (2.4). Specify the zero meet of distinct sectors as a **localic** statement.
6. **§5, lines 123–140:** Add diagram (4.2) and equation (4.3). These remove any possible suspicion of an unproved base-change theorem for image. State the adjunction (2.5) explicitly.
7. **§6, lines 146–167:** Give the finite-support set inclusion and the \(n=0\) convention explicitly. Optionally remove the redundant finite-distributivity hypothesis by referring to (5.1).
8. **§7, lines 169–176:** Retain the stated limitations. In particular, do not extrapolate to infinite-index path expansions without further hypotheses and do not identify the lattice decomposition with a coproduct decomposition of locales.

**First critical gap:** None. The first point needing *more exposition* is **OpenLoc** (candidate lines 46–52), but its asserted justification is correct and the proof in §2.1 fills it. The first point at which an *incorrect replacement argument* would be especially dangerous is the image calculation (candidate lines 129–140): an arbitrary image/base-change commutation would be unjustified, whereas the actual argument (4.3) is valid.

## 8. Sources, antecedents, and originality caveat

The closest **verified antecedent** I located is:

- **J. Picado and A. Pultr**, *Axiom \(T_D\) and the Simmons sublocale theorem*, *Commentationes Mathematicae Universitatis Carolinae* **60** (2019), 541–551, DOI [10.14712/1213-7243.2019.030](https://doi.org/10.14712/1213-7243.2019.030). Its **Theorem 3.3** proves, for a \(T_D\)-space \(X\), that \(X\) is scattered precisely when all sublocales of \(\Omega(X)\) are induced by and precisely represent subspaces; in particular \(\operatorname{Sub}(X)\cong\mathcal P(X)\). Its **Proposition 1.5** gives the complemented-element infinite-distributivity identity used in (2.4). [Open article](https://www.dml.cz/manakin/handle/10338.dmlcz/147971).

This directly confirms the **\(P=1\) phenomenon**, in even greater topological generality, and confirms the complemented-element calculation. It does **not**, by itself, state or prove the relative formula \(\operatorname{Sub}(P\times K)\cong\prod_k\operatorname{Sub}(P)\) for *arbitrary possibly pointless* \(P\), nor the formula for genuine localic relation composition. The present report verifies those by the independent proof above, but expresses **no historical priority claim**.

As general background on sublocale image/pullback and open/closed complements, see the definitions and standard adjunction discussion in [*Interior and \(\mathfrak h\) operators of the category of locales*](https://pisrt.org/psr-press/journals/oms/01-vol-7-2023-issue-1/interor-and-mathfrak-h-operators-of-the-category-of-locales/), particularly its preliminaries; the primary arguments in this report are given directly so they do not depend on that source's subsequent claims.

---

**Final assessment:** MAT*, MUL*, and FINMAT* are mathematically supported as stated. The proofs extend to the arbitrary locale parameter, including pointless sublocales, because all localization steps use genuinely open covers or complemented closed/open pieces and all image steps use the correct sublocale adjunction. The revisions recommended above would make this conclusion much easier for a reader to audit independently.