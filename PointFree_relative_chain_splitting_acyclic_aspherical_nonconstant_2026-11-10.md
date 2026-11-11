# Point-Free Topology — Relative chain splitting and homologically invisible nonconstant common hulls

**10 November 2026 · New internally checked research segment; NOT externally audited or literature-priority reviewed.** Continues the [relative full-subcomplex Stone gluing theorem](PointFree_Stone_indexed_relative_full_subcomplex_nonsuspension_2026-11-10.md), which is likewise **working** and remains unrefereed. Our earlier **audited** foundations are in [the nonconstant sheaf/Čech canonical account](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md), especially the pointed Stone-indexed face-poset theorem and the separately established canonical edgewise arrow theorem. This segment derives an **exact derived-module formula for relative gluing** and uses a finite *acyclic but aspherical and noncontractible* Higman presentation complex to construct a connected, nonconstant, **aspherical** common hull realization whose **ordinary homology sheaves equal those of a point**.

No assertion about intrinsic localic shape, κ-independence, full literature priority, or results blind-audited after 10 November.

## 0. The finite-pair construction and linearized chain functor

Fix a finite simplicial pair \(K\subseteq T\) with \(K\ne\varnothing\), a nonempty Stone space S, and replace the pair by \(\operatorname{sd}K\subseteq\operatorname{sd}T\), making K **full** in T. The preceding working theorem gives a coherent locale \(X(S;T,K)\) by identifying face-poset copies along \(F(K)\). Its **canonical** maps
\[
\mathbf C(X)\xrightarrow{\sim}\mathbf I(X),\qquad
\mathbf C(X)\xrightarrow{\sim}\mathbf D(X)
\]
are equivalences in a sufficiently large Stone-sheaf ∞-topos \(\mathscr H_\kappa\), and their common realization is
\[
\mathcal E_{T,K}(S)=
\underline{|K|}\mathop{\amalg}_{h(S)\times\underline{|K|}}
\bigl(h(S)\times\underline{|T|}\bigr).
\tag{0}
\]
**Scope:** This finite-pair extension beyond singleton K is still working, not externally audited. The **pointed case \(K=\{v\}\)** is already independently blind-refereed and will suffice for both concrete acyclic examples in §2. Thus the core example remains valid even if later audits demand repairs to the general pair extension.

Let R be a commutative ring and \(C_R(Y)=R[Y]\in\operatorname{Mod}_{HR}(\mathscr H_\kappa)\) the derived free R-linearization (equivalently the singular HR-chain object). It preserves all ∞-categorical colimits and is symmetric monoidal for cartesian products:
\[
C_R(Y\times Z)\simeq C_R(Y)\otimes_R^{\mathbb L}C_R(Z).
\]
For constant finite CW realizations this agrees with the ordinary cellular/simplicial chain complex, regarded as a constant derived R-module.

Choose a point \(s_0\in S\). Put \(M_{S,R}=R[h(S)]\) and \(J_{S,R}=\ker(M_{S,R}\overset{\epsilon}\to\underline R)\), the **reduced free R-module sheaf**. The generator \(s_0\) splits the augmentation,
\[
M_{S,R}\cong\underline R\oplus J_{S,R},
\]
as ordinary sheaves of R-modules and as derived HR-modules. For infinite S, the section \([{\rm id}_S]-[{\rm const}_{s_0}]\in J_{S,R}(S)\) has pairwise distinct point values for any nonzero **field** R.

## 1. A relative chain splitting valid before homology calculations

**THEOREM 1 (derived linearization of the finite-pair glued object).** With K,T,S as above and a choice of \(s_0\),
\[
\boxed{
C_R(\mathcal E_{T,K}(S))
\simeq
\underline{C_*(T;R)}
\oplus
\left[
J_{S,R}\otimes_R^{\mathbb L}
\underline{C_*(T,K;R)}
\right]
}
\tag{1}
\]
in the stable ∞-category of sheaves of HR-modules. The decomposition depends on the choice \(s_0\); the underlying chain object \(\mathcal E\) is not asserted to be a *space-level wedge*.

**Proof.** Apply \(C_R(-)\) to the defining pushout (0). Because free R-linearization preserves colimits/products, it becomes the homotopy pushout of the stable module diagram
\[
C_R(K)
\longleftarrow
M_{S,R}\otimes_R^{\mathbb L}C_R(K)
\longrightarrow
M_{S,R}\otimes_R^{\mathbb L}C_R(T).
\]
The left map is augmentation \(\epsilon\otimes 1\) and the right is \(1\otimes C_R(K\hookrightarrow T)\). Split \(M_{S,R}=R\oplus J\). The R-summands give C_R(T), while the J-summands give the cofiber of
\(J\otimes C_R(K)\to J\otimes C_R(T)\). Tensoring is exact in the stable module category, so this is
\(J\otimes^{\mathbb L}\operatorname{cofib}(C_R(K)\to C_R(T))
=J\otimes^{\mathbb L}C_R(T,K)\). QED.

**Corollary 2 (finite-field detection).** For a field k and finite simplicial T,K, the finite-dimensional relative chain complex over k splits into its homology (noncanonically). Consequently
\[
\boxed{
\mathcal H_n(\mathcal E_{T,K}(S);k)
\cong
\underline{H_n(T;k)}
\oplus
\left(J_{S,k}\otimes_k
\underline{H_n(T,K;k)}\right).
}
\tag{2}
\]
This formula is noncanonical in general, beyond the splitting determined by s0, because choosing chain contractions for T,K over k is noncanonical. It does **not** assume that arbitrary condensed abelian sheaves are flat; the finite relative complex is explicitly split over a field.

For infinite S and \(H_n(T,K;k)\ne0\), \(\mathcal H_n(\mathcal E;k)\) is **nonconstant**: tensor a nonzero relative class with the section \([{\rm id}_S]-[{\rm const}_{s_0}]\) and evaluate at points \(s\in S\), obtaining infinitely many distinct values in the J-summand of (2). Sections of a constant discrete abelian sheaf over compact S have finite point-image. Thus **every nonzero relative homology group of the finite pair is detected by nonconstancy with some field coefficients**: a nonzero finitely generated integral relative homology group survives modulo some prime p (or over Q).

**Corollary 3 (homologically invisible gluing).** If \(K\hookrightarrow T\) is an **integral homology equivalence**, then \(C_*(T,K;\mathbb Z)\) is a bounded acyclic complex of finitely generated free abelian groups and hence is chain-contractible. Therefore, for **every coefficient ring R**,
\[
C_R(\mathcal E_{T,K}(S))\simeq\underline{C_*(T;R)}.
\]
So **all ordinary homology sheaves** of the common chain/hull realization are the constant homology sheaves of T. This does **not** imply that the homotopy object \(\mathcal E\) is constant. It gives a clean criterion for where nonconstant structure can be *completely invisible to untwisted homology*, in every coefficient ring.

**Warning:** Do NOT replace (1) by a space-level splitting
\(\mathcal E\simeq T\vee (J\wedge(T/K))\) in general. It is generally false; the torus-along-essential-circle example has \(\pi_1\cong\mathbb Z\times F(S)\), not the corresponding free-product group. The derived-module splitting forgets essential attaching and multiplicative data.

## 2. A finite acyclic, noncontractible poset source from a balanced presentation

The classic binary icosahedral group \(G\cong \mathrm{SL}_2(5)\) (order 120) admits the **two-generator, two-relator** symmetric presentation
\[
G=
\langle a,b\mid ab^2a=bab,\quad ba^2b=aba\rangle.
\tag{3}
\]
This is recorded by Tomoda–Zvengrowski, *Remarks on the cohomology of finite fundamental groups of 3-manifolds*, Geometry & Topology Monographs 14 (2008), §4.3 (https://msp.org/gtm/2008/14/gtm-2008-14-023p.pdf), and ultimately Coxeter–Moser.

Let Q be the connected presentation CW 2-complex: one 0-cell, two 1-cells (a,b), two 2-cells attached by the two relators. On the cellular integral chain complex, its boundary map
\[
\partial_2:\mathbb Z^2\to\mathbb Z^2
\]
is the identity matrix (up to relator orientation): for \(ab^2a(bab)^{-1}\), the exponent-sum vector is (1,0); for \(ba^2b(aba)^{-1}\), it is (0,1). Hence \(H_1(Q;\mathbb Z)=H_2(Q;\mathbb Z)=0\). Higher homology vanishes by dimension, while \(H_0(Q)=\mathbb Z\): **Q is integral-acyclic**. But \(\pi_1(Q)\cong G\) is nontrivial/perfect (indeed finite of order 120), so Q is not contractible. Any finite simplicial model T of the homotopy type of Q, with a chosen vertex v, can be used in the already independently audited **singleton-point** Stone-indexed face-poset gluing construction.

This example is particularly small at the CW-presentation level, but **Q is not aspherical**: a nontrivial finite group cannot have a finite-dimensional K(G,1) of this kind. It nevertheless proves all the homological-invisibility and sheaf-nonconstancy conclusions below; using G also yields a *torsion obstruction* to the result being a suspension.

For a stronger **aspherical** example, use Higman's group \(H\), whose standard balanced presentation can be written
\[
\tag{4}
H=\langle a,b,c,d\mid
aba^{-1}=b^2,\quad
bcb^{-1}=c^2,\quad
cdc^{-1}=d^2,\quad
dad^{-1}=a^2
\rangle.
\]
Its presentation 2-complex has one vertex, four edges, four 2-cells. The four exponent-sum boundary vectors form a signed permutation matrix: the cellular chain differential \(C_2\to C_1\) is an isomorphism of free rank-4 abelian groups. It is therefore **integral-acyclic**. More importantly, the presentation is **aspherical**, and H is an **infinite nontrivial group with no finite quotients** (Bridson–Grunewald, *Annals of Mathematics* 160 (2004), §4.1, Prop. 4.1 and the Higman construction in pp. 364–365: https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n1-p08.pdf). Thus the presentation CW 2-complex is a **finite \(K(H,1)\)**. Choose a finite simplicial complex T with this homotopy type and a vertex v. Finite simplicial replacement is standard and does not alter homotopy type or integral acyclicity.

## 3. A genuinely nonconstant sheaf object whose ALL ordinary homology sheaves are constant

**THEOREM 4 (homologically invisible nonconstant canonical-equivalence examples).** Let T be a finite connected, integral-acyclic simplicial complex with a chosen vertex v and nontrivial fundamental group G. Let S be an **infinite Stone space**. Form the coherent locale \(X=W_S(F(T),v)\) using the **previously blind-refereed pointed Stone-indexed face-poset theorem**, so
\[
\boxed{
\mathbf C(X)\xrightarrow{\sim}\mathbf I(X),\quad
\mathbf C(X)\xrightarrow{\sim}\mathbf D(X),\quad
\mathbf C(X)\simeq h(S)_+\wedge\underline{|T|}.
}
\]
Then the common object E has all the properties:
1. E is connected and its **ordinary reduced homology sheaves with any coefficient ring R vanish in every degree**; its H₀ is the constant R sheaf. In particular its integral homology sheaves are exactly those of 1.
2. E is nevertheless **not a constant sheaf-homotopy object**. Its \(\pi_1\) sheaf is nonconstant, even though its abelianization and all ordinary homology sheaves are trivial.
3. If T is aspherical (use Higman's presentation), E is also **aspherical/1-truncated**. It is the classifying object of the sheaf of groups obtained by sheafifying the presheaf
\[
\boxed{
R_0\longmapsto\mathop{*}_{f\in\operatorname{Cont}(R_0,S)}G,
}
\tag{5}
\]
where \(R_0\) denotes any test Stone space, not a coefficient ring. This \(\pi_1\) sheaf is nonconstant and perfect. At the terminal Stone point, \(\pi_1(E(*))\cong *_{s\in S_{\rm set}}G\).
4. For Higman's G=H, \(\pi_1(E(*))\) is an infinite perfect group **with no finite quotients**. Thus the common sheaf-homotopy is nonconstant and aspherical while being invisible to untwisted homology, and even its point-evaluated group has trivial profinite completion.

**Proof.** First, E is the pointed S-indexed wedge of copies of T. Derived R-linearization gives
\(\widetilde C_R(E)\simeq R[h(S)]\otimes^{\mathbb L}_R\widetilde C_R(T)\). The finite integral reduced cellular chain complex \(\widetilde C_*(T;\mathbb Z)\) is bounded finite free and acyclic, hence contractible. Tensoring with any R sheaf preserves its chain homotopy, giving vanishing reduced homology *with every constant coefficient ring*. Because T is connected, E is connected.

For nonconstancy, choose \(1\ne g\in G=\pi_1(T,v)\), represented by a based loop \(\gamma:S^1\to|T|\). The universal map
\[
h(S)\times\underline{|T|}\to E
\]
sends \(h(S)\times\gamma\) to a morphism \(h(S)\to\pi_1(E)\) after forming the internal based loop object and applying \(\pi_0\). Evaluate this morphism on the *identity section* \(\mathrm{id}_S\in h(S)(S)\). For each point s:*\to S its restriction is the element \(g_s\) in the s-th free-product factor of
\[
\pi_1(E(*))\cong\mathop{*}_{s\in S_{\mathrm{set}}}G.
\]
The elements \(g_s\) are pairwise distinct. Thus the section over compact S has **infinite point-value image**. No section of a constant discrete group sheaf on compact S has infinite image, so \(\pi_1(E)\), and therefore E, is nonconstant. Note this argument uses the **nonabelian** π₁ sheaf; ordinary homology cannot see these classes since G is perfect.

If T=K(G,1), the objectwise pointed wedge is \(K(*_{f\in\operatorname{Cont}(R_0,S)}G,1)\) for each Stone test object \(R_0\), by topological van Kampen and the Bass–Serre description of the universal cover of a wedge of aspherical CW spaces. Sheafification is left exact and commutes with truncation, hence E remains 1-truncated; its π₁ is the sheafification of (5). This works without hypercompleteness assumptions.

The Higman group H is perfect (abelianization zero) and has no nontrivial finite quotient. Free products of perfect groups are perfect, and any homomorphism of \(*_sH\) to a finite group vanishes on every factor, so is trivial; thus the point-evaluated group has no finite quotients. QED.

**Non-suspension bonus:** At the terminal point the group \(*_{s}G\) is nontrivial perfect. Any CW suspension has either trivial or free fundamental group, while the only perfect free group is trivial. Hence E(*) is not a suspension; evaluation at * preserves homotopy pushouts, so E cannot be a suspension in the sheaf ∞-topos. Similarly it is not a wedge of spheres. For the binary-icosahedral option (3), torsion in the free product is another direct obstruction to a suspension.

## 4. What is established, what is deferred

**The conceptual hierarchy of the last two segments:**
- Torus-along-circle pair: nonconstant **H₁ and H₂** sheaves, nonzero cup products, nonfree π₁, and canonical C=I=D.
- **General relative homology theorem:** the relative finite chain complex \(C_*(T,K)\) controls all extra homology via the reduced free condensed coefficient sheaf \(J_{S,R}\).
- **Acyclic pointed finite complex:** canonical C=I=D, genuinely nonconstant **nonabelian** homotopy but **all ordinary homology sheaves constant**. Higman's example makes the common realization also 1-truncated/aspherical with perfect nonconstant π₁ sheaf and no finite quotients at its terminal point.

**No new independent audit has occurred.** The general relative full-subcomplex gluing theorem and this relative derived chain splitting are **internally checked working**. The **acyclic example's canonical C=I=D equivalences** use only the previously independently checked **pointed gluing theorem**, so that part rests on stronger prior evidence. The Higman and binary-icosahedral presentation properties are **established literature facts**, not claims of novelty; the specific coherent sheaf-homotopy synthesis has not been priority searched.

**Suggested next bounded inquiry (not attempted here):** What nonconstant homotopy can remain **invisible even to finite-group local systems** and to truncated/profinite approximations, and how does that reflect the original localic binary separation relations? For Higman, the point-evaluated π₁ already has no finite quotients, making it a clean test. Another direction is analyzing twisted homology/local coefficient sheaves, which can detect \(\pi_1\)-behavior hidden by all constant coefficients.
