# Canonical addendum — relative Stone gluing, acyclic constancy, twisted coefficients

**11 November 2026. Fourth-audit corrected consolidation, preserving original proofs and reports.** Original claims A1–A4, B1–B4 and R1–R3 were accepted in an independently blind external review **relative to earlier stated premises P1–P5** and their classical inputs, subject to the repairs recorded in the [final reconciliation](PointFree_audit4_FINAL_RECONCILIATION_2026-11-11.md). The **acyclic-map constancy criterion** was proposed by the A/B referee after the verdict and independently cross-checked by the C referee. The **extension of intrinsic H¹ nonconstancy from infinite-order groups to all nontrivial groups** was proposed *in the final nonblind internal-audit comparison* and separately rechecked internally, **NOT external cross-refereed**. No novelty, intrinsic-localic-shape or site-size-independence claim.

## 0. Ambient theory

Work in a sufficiently large patched Stone-sheaf \(\infty\)-topos \(\mathscr H_\kappa\), with surjective finite Stone covers, including the empty-cover convention. The constant-object functor is \(c:\mathcal S\to\mathscr H_\kappa\), \(h(S)\) denotes the representable sheaf of a Stone space, and \(\Gamma=\mathrm{ev}_*\) denotes evaluation at the one-point Stone space. Important: \(\Gamma\) preserves colimits and finite limits in this particular topos because covers of the one-point space split; **evaluation at arbitrary Stone tests does not preserve sheaf colimits**. All descriptions as objectwise wedges, free products or joins are at the presheaf stage *before sheafification*. No hypercompleteness assumption.

**Constant-object nonconstancy lemma.** If Y is a constant homotopy object (with a global base point if required), its homotopy and ordinary homology sheaves are constant; a section of a constant discrete sheaf over compact Stone S is locally constant and has finite point-image. Thus a section of a homotopy/homology sheaf with infinitely many distinct point-values is an obstruction to Y being constant. This lemma is needed explicitly in the original A2b, A3, A4 and B4 arguments; it was missing from their packet text, and is supplied by the independent referee.

## 1. Lower-ideal gluing and canonical comparison

Let P be a finite poset, \(\varnothing\ne A\subseteq P\) a lower ideal, and S a nonempty Stone space. Write
\[
W_S(P,A)=A\amalg (S\times(P\setminus A)),
\]
with shared A and each s-fibre carrying P's order, and no nonshared comparisons across distinct fibres. The order is closed and Priestley. Its clopen upset lattice is
\[
K(W)=\{f\in\mathrm{LC}(S,\mathrm{Ups}(P)): f(s)\cap A
\text{ independent of }s\}.
\]
Let (WR) be **upper-witness reflection**: for every tuple in A, having a common upper witness in P is equivalent to having one in A. This is exactly the degreewise equality \(I_n(P)\cap A^{n+1}=I_n(A)\) for all n (finite tuples).

**Original A1 theorem, corrected wording.** Under (WR), the patched **chain** and **upper-hull** simplicial objects satisfy the compatible homotopy-pushout formulas
\[
\mathbf C(W)\simeq
\mathbf C(A)\amalg_{h(S)\times\mathbf C(A)}\bigl(h(S)\times\mathbf C(P)\bigr),
\]
\[
\mathbf I(W)\simeq
\mathbf I(A)\amalg_{h(S)\times\mathbf I(A)}\bigl(h(S)\times\mathbf I(P)\bigr).
\tag{1.1}
\]
The canonical \(\mathbf C(W)\to\mathbf I(W)\) is induced by the morphism of these two displayed spans; it is an equivalence when both finite comparisons are. The fitted comparison \(\mathbf C(W)\to\mathbf D(W)\) is equivalent **as a canonical arrow under C** by the previously audited edgewise theorem. **No fibrewise degreewise D_n identity is asserted.**

**WR is sufficient, not necessary, for the final equivalence.** A/B's comparison supplies \(P=\{z<a,z<b,a<c,b<c\}\), \(A=\{z,a,b\}\): WR fails for (a,b), but the glued C and I objects are both contractible and their comparison is an equivalence. Even without WR a corrected I-pushout exists after replacing the shared \(I_\bullet(A)\) by the relative ambient simplicial space \(I'_n=I_n(P)\cap A^{n+1}\). WR is precisely what makes \(I'=I(A)\); do not call WR a necessary condition for homotopy equivalence.

**A2a:** For any nonempty finite simplicial pair \(K\subseteq T\), subdivision makes the inclusion of face posets a lower ideal satisfying WR. The **strictly commuting square of canonical simplicial inclusions** produces a coherent locale whose canonical C→I,D comparisons are equivalences, with common realized object
\[
E_{T,K}(S)=c|K|\amalg_{h(S)\times c|K|}(h(S)\times c|T|).
\tag{1.2}
\]
No appeal to unquoted naturality of a previous *criterion* is required.

**A2b:** The unsubdivided full row-circle inclusion \(K=S^1\times\{*\}\subseteq T=S^1\times S^1\), using the explicit nine-vertex torus triangulation in the original packet, yields
\[
E_{T,K}(S)\simeq cS^1\times\bigl(h(S)_+\wedge cS^1\bigr)
\simeq B\bigl(c\mathbb Z\times\mathrm{Fr}(h(S))\bigr).
\tag{1.3}
\]
Its homology sheaves in degrees 0,1,2 are \(\mathbb Z,\ \mathbb Z\oplus\mathbb Z[h(S)],\ \mathbb Z[h(S)]\), respectively, and zero above 2. They are nonconstant for infinite S. At point evaluation the cup product of two degree-one classes is nonzero (torus retract), hence this object is not a suspension. Equivalently π₁ at * is \(\mathbb Z\times F(S_{\rm set})\), which contains \(\mathbb Z^2\) and is not free, whereas the fundamental group of any connected suspension is free. For S infinite the object is not any internally indexed wedge whose point evaluation is a wedge of finite connected complexes: such a free product either has trivial centre or is finitely generated, unlike \(\mathbb Z\times F(S_{\rm set})\). The count “six shared faces and 48 fibre faces” refers to the **unsubdivided already-full pair**.

**A3 (relative derived-chain splitting).** Put \(M_S=R[h(S)]\), \(J_S=\ker(M_S\to R)\), choosing \(s_0\in S\) for \(M_S\cong R\oplus J_S\). For finite K⊆T there is a canonical fold projection \(C_R(E)\to C_R(T)\) and a choice-dependent complementary splitting, in sheaves of HR modules:
\[
C_R(E)\simeq C_R(T)\oplus
 \bigl(J_S\otimes_R^{\mathbb L}C_R(T,K)\bigr).
\tag{1.4}
\]
The *other* relative object is \(C_R(E,K)\simeq M_S\otimes_R^{\mathbb L} C_R(T,K)\); do not conflate it with the complementary summand \(C_R(E,T_{s_0})\simeq J_S\otimes_R^{\mathbb L}C_R(T,K)\). All finite simplicial pair chain complexes here are bounded free so the derived tensor can be calculated termwise. Over a field, nonzero finite relative homology gives a corresponding nonconstant J_S summand for infinite S. Vanishing integral relative homology implies all ordinary untwisted homology sheaves agree with those of cT, **not** that E itself is constant.

**A4:** For a connected noncontractible finite acyclic complex T (the binary icosahedral group presentation or the finite aspherical Higman presentation) and K={v}, the common object \(E=h(S)_+\wedge c|T|\) has constant untwisted homology in every degree, but a nonconstant fundamental-group sheaf when S is infinite. In the Higman case it is 1-truncated:
\[
\pi_1(E)=\text{sheafification of }\Bigl[U\mapsto *_{{\rm Cont}(U,S)}H\Bigr].
\]
There is no \(\infty\)-topos Whitehead inference from vanishing homology. The ordinary **space-level** suspension of a connected acyclic CW complex is contractible by van Kampen, Hurewicz and Whitehead; transporting that result through c establishes the stable/untwisted invisibility. The non-suspension conclusion holds for both finite acyclic group presentations because their point-evaluated π₁ is nontrivial perfect, hence not free.

## 2. Exact constancy criterion (new, independently cross-checked)

**Theorem (A/B referee, independently assessed by C).** For any nonempty Stone S and nonempty finite simplicial pair K⊆T:
1. If \(f:|K|\to|T|\) is a **homotopy epimorphism** (equivalently, every homotopy fibre is nonempty and acyclic), then the canonical fold
\[
\rho:E_{T,K}(S)\longrightarrow c|T|
\]
is an equivalence. This direction in fact does not require finite K,T.
2. If **S is infinite** and \(E_{T,K}(S)\) is equivalent to any constant object, then f is a homotopy epimorphism.
3. Thus for S infinite the following are equivalent: E constant, ρ an equivalence, f a homotopy epimorphism, f fibrewise acyclic. If S finite, E is constant for every pair.

**Proof of 1.** The constant-object functor preserves pushouts, hence preserves the epi equation \(T\amalg_KT\simeq T\). Product with h(S) preserves pushouts, so the corresponding map \(h(S)\times cK\to h(S)\times cT\) is epi as well. The map \(cK\to E\) is a cobase change of this epi and therefore epi. Choose \(s_0\in S\), which supplies a section \(\sigma:cT\to E\) of the fold. The two maps \(\sigma\rho\) and \(\mathrm{id}_E\) agree after restriction along the epi \(cK\to E\), and precomposition with an epi is monic on mapping spaces. Hence \(\sigma\rho\simeq\mathrm{id}_E\) and \(\rho\simeq\mathrm{id}\). This uses only S nonempty.

**Proof of 2.** Suppose \(E\simeq cZ\). The canonical map \(cK\to cZ\) comes from a map \(g:K\to Z\), since \(\Gamma c\simeq\mathrm{id}\). For finite simplicial T,K the relative internal mapping-space object
\[
\operatorname{fib}_{g}\!\bigl([cT,cZ]\to[cK,cZ]\bigr)
\simeq c\,\mathrm{Map}_{K/}(T,Z)
\]
is constant: finite complexes are finite homotopy colimits of points, internal hom turns these into finite limits and c is left exact. The attached family of T-copies defines an S-section of this constant mapping object; after \(\pi_0\), it is a locally constant function S→\(\pi_0\mathrm{Map}_{K/}(T,Z)\) and therefore has finite image. As S is infinite, two distinct copies \(j_s,j_t:T\to E(*)\) are homotopic **under K**. Retract the point-evaluated gluing onto \(T\amalg_KT\) by sending one copy to the first and another to the second; this makes their canonical inclusions \(i_1,i_2\) homotopic **under K**. As endomorphisms of \(T\amalg_KT\) under K, \(i_1\nabla=(i_1,i_1)\simeq(i_1,i_2)=\mathrm{id}\), while \(\nabla i_1=\mathrm{id}\). Thus the fold \(\nabla:T\amalg_KT\to T\) is an equivalence and f is epi. QED.

**Acyclicity equivalence** is classical (Raptis, *Some characterizations of acyclic maps*, Theorem 2.1(a), https://arxiv.org/abs/1711.08898): the homotopy fibre of \(T\amalg_KT\to T\) at t is the unreduced suspension of the fibre of f. It is contractible exactly when the latter is nonempty and acyclic. This does not require a connectedness assumption on K,T. A finite acyclic noncontractible K with T=cone(K) illustrates that the fold can be an equivalence even when K→T is not; with K a *point* and T the same acyclic noncontractible complex, the gluing remains nonconstant for infinite S despite all untwisted reduced homology vanishing. The converse for arbitrary **infinite complexes** has not been established.

## 3. Twisted coefficients: what was blind-audited

Let H be Higman's acyclic group, S nonempty Stone and \(\Pi=\ast_{h(S)}H\) the free-product group sheaf arising in A4. Its fold \(\rho:\Pi\to\underline H\) acts on suitable coefficients.

**B1:** Every map \(H\to GL_n(k)\) is trivial: a finitely generated linear image is residually finite (Mal'cev), whereas H has no nontrivial finite quotients. The same holds for \(\mathrm{Aut}(M)\) for finitely generated abelian M, by analyzing torsion and free quotients. All such finite-dimensional/finitely generated monodromy is trivial; with the acyclic finite presentation, the corresponding reduced cohomology vanishes. Only **finite generation** of H is needed here and in the B3 derivation parametrization.

**B2:** Let \(I_H=\ker(\mathbb Z[H]\to\mathbb Z)\) be the augmentation ideal. The Berstein–Schwarz derivation \(\beta_H(g)=[g]-1\) defines an infinite-order H¹ class and its degree-two square is nonzero by standard cohomological-dimension results. For the degree-two claim cite Dranishnikov–Rudyak, *On the Berstein–Svarc theorem in dimension 2*, arXiv:0712.2087, Theorem 3.4 and Corollary 3.5; for Higman duality cite appropriate Bieri–Eckmann background. The pullback nontriviality can be detected at \(*\) and restricted to a chosen H-factor; distinguish this from asserting an unproved internal H² sheaf formula.

**B3:** With \(D_H=\mathrm{Der}(H,I_H)\), \(D_H\cong I_H\oplus\mathbb Z\beta_H\), the **internal** degree-one cohomology sheaf for the folded coefficient module is
\[
\mathcal H^1(\Pi;\rho^*\underline{I_H})
\simeq \underline{\mathrm{LC}(S,D_H)/I_H}
\simeq\underline{\mathrm{LC}(S,I_H)/I_H\oplus\mathrm{LC}(S,\mathbb Z)}.
\tag{3.1}
\]
Here \(\mathcal H^1=\pi_0\mathrm{Sec}(K(M,1)\text{-bundle}/B\Pi)\) is \(\mathrm{Der}/\mathrm{PDer}\) as a sheaf, justified by the internal section-object fibre sequence \(\mathrm{Der}\to(BM)^{h\Pi}\to BM\). At the terminal Stone object, \(\Gamma\) commutes with \(\pi_0\) in this site, hence \(\mathcal H^1(*)\) **does equal absolute sheaf-classifying-space H¹**. It does *not* equal \(H^1(\Pi(*);I_H)\), which is \(\mathrm{Der}(H,I_H)^{S_{\rm set}}/I_H\) and is generally much larger. Nor should values at arbitrary Stone tests be naively identified with cohomology of the pointwise evaluated group without considering sections over that test.

**B4 as originally submitted (blind-checked):** For S infinite and any discrete G containing an infinite-order element, the intrinsic augmentation ideal \(J_\Pi=\ker(\mathbb Z[\Pi]\to\mathbb Z)\) and the regular ring \(\mathbb Z[\Pi]\) have **nonconstant internal first-cohomology sheaves**. The original proof uses injectivity of left multiplication by \(g_s-1\) for infinite-order g and distinguishes classes indexed by t∈S via four reduced words.

### Stronger B4 with arbitrary nontrivial G (NEW, internal only)

**Proposition (A/B referee in its final nonblind comparison; independent internal verification here).** The B4 conclusion holds for **every nontrivial discrete group G**, whether finite or infinite. It was **not** part of the original blind verdict and has not received another independent referee report.

**Proof.** Choose \(1\ne g\in G\). In the point-valued free product \(\Gamma=*_{s\in S_{\mathrm{set}}}G\) the original derivation classes \(d_t\) satisfy, on each G_s, \(d_t(x_s)=(x_s-1)m(t,s)\) with \(m(t,s)=(g_t-1)(g_s-1)\). Suppose \(d_t-d_u\) is principal with witness \(a\in\mathbb Z[\Gamma]\). Since supp(a) is finite and S infinite, choose s≠t,u whose factor does not occur in any word of supp(a). Put
\[
\Delta=(g_t-g_u)(g_s-1),\qquad y=\Delta-a.
\]
Principality yields \((x_s-1)y=0\) for **every** \(x\in G\). Thus the coefficient of y at w equals its coefficient at x_sw, since x_sy=y. At the reduced word \(w=g_tg_s\) the coefficient is +1: this term occurs in Δ but not supp(a). At \(x_sw=x_sg_tg_s\) for any x≠1, the coefficient is 0: the word begins with a nontrivial s-letter, whereas all four Δ terms begin in the t or u factor and no word in supp(a) contains an s-letter. Contradiction. Hence the point-evaluated classes for t≠u are distinct, and so are their internal classes, yielding a section of \(\mathcal H^1\) with infinite point-image over S. Both coefficient sheaves give nonconstancy by the lemma in §0. No element of infinite order is required. QED.

## 4. Three referee-origin addenda (blind checked in A/B)

**R1:** \(h(S)_+\wedge cS^1\simeq B\mathrm{Fr}(h(S))\), with full free **group** sheaf \(\pi_1=\mathrm{Fr}(h(S))\), and the unreduced suspension quotient after choosing a global point.

**R2:** For Stone S and distinct a,b, the two-point quotient \(T=S/(a\sim b)\) has \(\mathrm{Fr}(h(S))\cong\mathrm{Fr}(h(T)\sqcup1)\) by the explicit corrected generator maps recorded in the prior canonical account. For S=βN one absorbs an isolated point to obtain \(\mathrm{Fr}(h(S))\cong\mathrm{Fr}(h(T))\) with S,T not homeomorphic; hence unmarked full pointed homotopy types do not recover the Stone parameter even **up to isomorphism**, whereas a separately marked diagonal coalgebra on \(\mathbb Z[h(S)]\) does. The classical \(M\)-equivalence antecedent is Okunev's retract method; the *condensed sheaf group* statement has a direct proof here. Do not confuse the extra marked generator coalgebra with the ordinary spherical reduced-homology diagonal, which is primitive.

**R3:** For pointed gluing along a minimal v, the fitted simplicial object is a **union**, not a degreewise fibre wedge: \(D_n(W)=F_n\cup (\uparrow_Wv)^{n+1}\). The nerve of the latter and the intersection have terminal realizations; the degreewise union is an \(\infty\)-pushout of subobjects. Thus \(\mathbf D(W)\simeq h(S)_+\wedge\mathbf D(P)\) **compatibly with the canonical C→D map**. This direct calculation corroborates rather than replaces the previously audited general edgewise comparison. No analogous *degreewise* formula for D_n is asserted.

## 5. What remains open and provenance discipline

- The A/B original claims and R1–R3 are **externally blind-checked relative to P1–P5** after repairs. The new acyclic-map criterion has an **independent C-referee cross-check**. The arbitrary-nontrivial-G strengthening of B4 is a **new post-comparison internally rechecked** argument only.
- A proposed extension of direct fitted-side gluing to **every lower ideal** is still a sketch, not included as a theorem.
- Full computation of intrinsic \(\mathcal H^1(\Pi;J_\Pi)\), \(\mathcal H^1(\Pi;\mathbb Z[\Pi])\), and internal H² remains open. The role of arbitrary test spaces and sheaf cohomology must be preserved.
- Do not assert the converse of the acyclic-constancy theorem for arbitrary infinite K,T; the finite mapping-object hypothesis is essential to the current proof.
- Do not confuse abstract patched sheaf-homotopy conclusions with intrinsic localic shape, or identify sheaf realizations by naive unsheafified point evaluations.
- **Bibliography audit:** Okunev's original article, Bieri scan pages and version-specific Dranishnikov/Scholze theorem numbering remain worth checking before publication; use the already verified primary arXiv sources where possible. The torus, finite group, Higman and all other original computations remain in the independently reviewed technical packet and scripts.
