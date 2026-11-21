> **21 NOV 2026 — EXTERNAL-AUDIT RECONCILIATION.** The independent blind referee accepts SPLIT, MAT, GRP, ACT, BAL, and the balanced-witness extension conditional on previously reviewed RC. The wreath-product *faithful identification* requires **nonempty fibre P**. The Section 4 discrete-to-scattered complete-lattice transport is accepted, but its broad partial-graph extrapolation is **not proved** without explicit common-ambient pullback/image hypotheses. See [reconciliation](ProjectA_BALANCED_WITNESS_SCATTERED_MATRIX_POSTREFEREE_RECONCILIATION_2026-11-21.md), [referee report](project-a/audits/2026-11-21/BALANCED_WITNESS_SCATTERED_MATRIX/INDEPENDENT_REFEREE_REPORT.md), and [addendum](project-a/audits/2026-11-21/BALANCED_WITNESS_SCATTERED_MATRIX/REFEREE_ADDENDUM.md).

# Project A — balanced witness transport and scattered-index matrix algebras
## Research continuation, 21 November 2026 · NEW INTERNAL generalization, independent audit pending

**Motivation.** The previous internally argued [scattered-coordinate pseudo-bijection](ProjectA_PERFECT_TARGET_SCATTERED_CORRIDOR_SAFE_INFINITE_CHART_RANK_2026-11-21.md) and [tensorized Cantor-to-Cantor version](ProjectA_PERFECT_SOURCE_TARGET_TENSORED_SCATTERED_PSEUDO_ISOMORPHISM_2026-11-21.md) suggested that *sublocale transport*, rather than topological invertibility or finite chart rank, is the relevant mechanism. This note derives (1) an exact criterion for finite-join graph-extension associativity, and (2) a substantially larger **concrete** class of point-generated relations, including discontinuous permutations of a scattered index, which satisfies that criterion. The earlier compact-Hausdorff rectangular rule **(RC)** is independently reviewed; everything new here is **INTERNAL** and not literature-priority claimed.

We work in classical Loc. For a compact Hausdorff spatial locale G and ordinary subsets A,B⊆G write
\[
p(A,B)=[A\times B]_{G^2},\quad q(A,B)=[A]_G\times_{\rm Loc}[B]_G.
\]
The previously independently refereed input **(RC)** says for independent r,s∈{p,q},
\[
r(A,B)\circ s(C,D)=
\begin{cases}q(A,D),&[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0,\end{cases}
\]
where q(A,D) may be 0 for empty outer supports. Composition is genuine localic pullback/image in diagrammatic left-to-right order; it distributes over **finite**, not asserted arbitrary, joins.

### 1. Balanced witness semigroups: the exact algebraic criterion

Let \(\mathscr H\) be a family of **point-generated graph relations** \(\Gamma_h\le G^2\) indexed by partial bijections \(h:D_h\to E_h\) of ordinary subsets of G (the functions need not be continuous), containing the identity graph \(\Delta_G\) and 0 and closed under converse. Make the following three explicit **assumptions**, which must be checked by genuinely localic computations:

**(G)** The localic composite \(\Gamma_h\circ\Gamma_k\) is exactly the point-generated graph of the ordinary partial composition \(k\circ h\), which again belongs to \(\mathscr H\). Thus the graph factors form an associative partial-bijection semigroup under the **actual** image/pullback composition. This is *not* assumed for arbitrary point-generated graphs.

**(T)** For every ordinary A,B⊆G and t independently equal to p or q,
\[
\boxed{
t(A,B)\circ\Gamma_h=t(A,h(B\cap D_h)),\qquad
\Gamma_h\circ t(A,B)=t(h^{-1}(A\cap E_h),B).
}\tag{T}
\]
In particular, q stays the **full nonspatial localic rectangle** after action, not merely its point-generated part.

**(O)** For all ordinary B,C⊆G,
\[
\boxed{
[h(B\cap D_h)]\wedge[C]\ne0
\Longleftrightarrow
[B]\wedge[h^{-1}(C\cap E_h)]\ne0.
}\tag{O}
\]
All meets are genuine meets of **induced sublocales**, not ordinary point intersections.

**Theorem 1.1 (Balanced Witness Extension Criterion, INTERNAL; conditional on RC).** Finite joins of the graph generators \(\mathscr H\) and all p/q rectangular generators form an associative, unital, converse-closed, finite-join-distributive algebra under actual localic relational composition. The finite-join rectangular algebra is a converse-closed two-sided ideal. For individual-generator words, no rectangle letters gives a graph generator, one rectangle gives the same p/q type (or 0), and ≥2 rectangle letters gives q (or 0).

**Proof.** Binary products stay generators by (RC),(G),(T). Check triple patterns RRR, RRH, RHR, RHH, HRR, HRH, HHR, HHH (R=p/q rectangle, H=graph). RRR uses (RC); allow the outer q to vanish from empty endpoints. RRH/HRR retain the same internal overlap test before/after endpoint restriction. RHH/HHR follow from the partial bijection action and (G). HRH restricts independent outer coordinates and so commutes. HHH follows from (G). Only RHR is delicate: the two bracketings test respectively [h(B∩D_h)]∧[C]≠0 and [B]∧[h^-1(C∩E_h)]≠0, equivalent by (O). They consequently return the same full outer q rectangle (or 0). **Finite** distributivity expands arbitrary finite joins into generator triples, proving associativity. The ideal/normal-form assertions follow by the same multiplication table. □

**Not a classification:** Conditions (G),(T),(O) are a convenient sufficient structural test, not claimed necessary for safe graph adjunction. Its value depends on finding *geometric hypotheses* that imply all three rather than verifying associativity directly.

### 2. Atomic index characterization (scatteredness is exactly what is needed)

For compact Hausdorff Z and K let \(\mathrm{Sub}(Z\times K)\) denote the full coframe of sublocales. For W≤Z×K let \(W_k=W\wedge(Z\times\{k\})\), identified with a sublocale of Z, and define
\[
\Phi_Z(W)=(W_k)_{k\in K},\qquad
\Sigma_Z((A_k)_{k\in K})=\bigvee_{k\in K}(A_k\times\{k\}).
\tag{FIB}
\]

**Lemma 2.1 (Fibre observation/reconstruction).** For every compact Hausdorff K,Z,
\[
\boxed{\Phi_Z\Sigma_Z=\mathrm{id},\qquad\Sigma_Z\Phi_Z\le\mathrm{id}.}\tag{SPLIT}
\]
**Proof.** Clearly ΣΦ(W)≤W. Fix k and let \(J=\bigvee_{j\ne k}(A_j\times\{j\})\). Every j≠k summand lies below \(Z\times[K\setminus\{k\}]\), so their **arbitrary join** J also lies below that sublocale. As K is Hausdorff, K\{k} is open and is disjoint (as a sublocale) from closed {k}; hence J∧(Z×{k})=0. By just **finite** distributivity, the k-fiber of Σ(A) is exactly A_k. No forbidden infinite meet/join interchange occurs. □

Thus ΣΦ is an **interior operator** extracting the part of W generated by its ordinary K-point fibers. In general it may miss a *pointless* vertical component.

**Theorem 2.2 (Atomic-index characterization, INTERNAL).** For a compact Hausdorff K the following are equivalent:

(i) K is **scattered**.

(ii) Every sublocale W≤K is the join of its ordinary singleton fibers.

(iii) For **every** compact Hausdorff parameter Z,
\[
\boxed{
\Phi_Z:\operatorname{Sub}(Z\times K)\overset{\cong}{\longrightarrow}
\prod_{k\in K}\operatorname{Sub}(Z)}
\tag{MAT}
\]
is a complete-lattice isomorphism, inverse to Σ_Z.

**Proof.** (iii)→(ii) by Z=1. (ii)→(i): if K is not scattered, it has a nonempty closed perfect subspace F. Its nonzero least dense Booleanization \(\mathcal B(F)\) has **no ordinary points**, because for each x∈F the open \(F\setminus\{x\}\) is dense, contains \(\mathcal B(F)\), but excludes x. The embedded \(\mathcal B(F)\le K\) is therefore a nonzero sublocale with every point fiber 0, contradicting (ii).

(i)→(iii): fix compact Hausdorff Z and any W≤Z×K. Let J=ΣΦ(W). If W≰J, **regularity (hence fitness)** of Z×K yields an open sublocale O with J≤O, W≰O. Let F be its closed complement. Then W'=W∧F≠0. Its least closed support L⊆Z×K is nonempty compact Hausdorff; W' is dense in L. Its projection P=pr_K(L) is nonempty compact closed in K, hence scattered. Choose k∈P isolated in P and K-open V with V∩P={k}. The relatively open part L∩(Z×V) is nonzero and meets W' nontrivially by density. It lies in Z×{k}, hence gives \(0\ne W'\wedge(Z\times\{k\})\le J\wedge F=0\), contradiction. Thus W=J. With Lemma 2.1, Φ and Σ are inverse order isomorphisms, necessarily preserving all meets/joins. □

**Scope note.** The compact/regular context is used for the closed support projection and open separator. This is not a claim of a parametrized equivalence for arbitrary locale Z/K. When K is perfect, \(\mathcal B(K)\) is a simple explicit **vertical ghost** invisible to all singleton fibers: the atomic-index condition is sharp.

**Published antecedent:** Picado–Pultr, *Axiom T_D and the Simmons sublocale theorem* (2019), https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1904/picpul.pdf, characterizes total point determination for scattered \(T_D\) spaces. The **parameterized full-sublocale-lattice theorem** (MAT) above is a new deduction, with no priority claim.

### 3. A concrete enlargement: discontinuous permutations with independently varying fiber homeomorphisms

Let P be **any** compact Hausdorff space and K compact scattered Hausdorff, and put G=P×K. For **any set-theoretic permutation** \(\sigma:|K|\to|K|\) and **any family of homeomorphisms** \(h_k:P\to P\), define a set function
\[
\Theta_{\sigma,h}(p,k)=(h_k(p),\sigma(k)).
\tag{TH}
\]
There is **no continuity assumption on σ or on the variation k↦h_k**. Define its **point-generated graph relation**
\[
H_{\sigma,h}:=[\,\{((p,k),(h_k(p),\sigma(k))):p\in P,k\in K\}\,]_{G^2}.
\tag{HG}
\]
This is a genuine sublocale relation even if Θ is not a locale map.

**Theorem 3.1 (scattered-index wreath-product algebra; NEW INTERNAL, conditional on RC).** The family \(\mathscr H_{P,K}=\{H_{\sigma,h}\}\) is a group under **localic** relational composition and converse, with multiplication
\[
\boxed{
H_{\sigma,h}\circ H_{\tau,g}
=
H_{\tau\circ\sigma,\,(g_{\sigma(k)}\circ h_k)_{k\in K}}.
}\tag{GRP}
\]
When \(P\ne\varnothing\), it is faithfully isomorphic, as an abstract group, to \(\operatorname{Homeo}(P)^{|K|}\rtimes\operatorname{Sym}(|K|)\) with the evident reindexing action. It contains identity Δ_G.

Moreover, for t∈{p,q} and ordinary A,B⊆G,
\[
\boxed{
t(A,B)\circ H_{\sigma,h}
=t(A,\Theta_{\sigma,h}(B)),\qquad
H_{\sigma,h}\circ t(A,B)
=t(\Theta_{\sigma,h}^{-1}(A),B).
}\tag{ACT}
\]
The induced-sublocale overlap test is balanced:
\[
[\Theta_{\sigma,h}(B)]\wedge[C]\ne0
\iff[B]\wedge[\Theta_{\sigma,h}^{-1}(C)]\ne0.
\tag{BAL}
\]
Consequently, finite joins of **all** p/q rectangles and all such graph relations form an **associative unital converse-closed algebra**, with the rectangular algebra a two-sided ideal.

**Proof — full localic matrix calculation.** By Theorem 2.2 applied to K,K²,K³, sublocales of G,G²,G³ are respectively arrays of arbitrary sublocales of P,P²,P³ indexed by K,K²,K³. The (i,j)-fiber of H_{σ,h} is \(\Gamma_{h_i}\le P^2\) for j=σ(i), and 0 otherwise, because restriction of the induced spatial graph to the closed (i,j) sector is the corresponding graph of the homeomorphism h_i.

For two such graph relations, the actual composability pullback, in the closed (i,j,k) sector of G³, vanishes unless j=σ(i) and k=τ(j). In that one case, it is the ordinary localic graph of the paired homeomorphisms \(p\mapsto(p,h_i(p),g_j(h_i(p)))\). Its image to the (i,k) sector is \(\Gamma_{g_j\circ h_i}\). There is **exactly one** permitted intermediate j for each input i and endpoint k; no infinitely indexed distributivity of composition is used. Theorem 2.2 applied to K² now reconstructs the entire composite and gives (GRP). Converse clearly reverses the ordinary partial graph and is H of the inverse set permutation and inverse h's.

For **rectangular actions**, write \(A_i=\{p:(p,i)\in A\}\), \(B_j=\{p:(p,j)\in B\}\). The (i,j)-fibers of p(A,B) and q(A,B) are respectively p_P(A_i,B_j) and q_P(A_i,B_j), where the latter may be nonspatial. Composing with H along the unique permissible intermediate j transports that fiber by the **homeomorphism** h_j, giving respectively p_P(A_i,h_j(B_j)) or the **full** q_P(A_i,h_j(B_j)). These are precisely the (i,k)-fibers of t(A,Θ(B)) for k=σ(j), proving the first ACT identity; the second is symmetric. The same point-fiber decomposition of Sub(G), and the fact each h_j induces a sublocale lattice isomorphism, proves (BAL) *without* replacing meets of nonspatial supports by ordinary set intersection. Apply Theorem 1.1. □

**Example 3.2 (genuinely discontinuous safe graph).** Take \(K=\{0\}\cup\{1/n:n\ge1\}\), P=Cantor. Let σ swap the unique nonisolated point 0 with the isolated point 1, fixing all other points, and take h_k=id_P. The ordinary bijection Θ(p,k)=(p,σ(k)) is **not continuous**, but its point-generated graph H is an involution under actual localic relation composition:
\[
H\circ H=\Delta_G.
\]
Both actions with **full nonspatial** rectangles remain exact, and the finite-join algebra generated by H and all p/q rectangles is associative. Thus the class of safe point-generated graph relations is strictly larger than graphs of continuous maps—even though the ambient G is compact Hausdorff and contains a perfect Cantor coordinate.

This should **not** be called a map in Loc: the discontinuous Θ is used only to label ordinary points of the legitimate point-generated sublocale H.

### 4. The earlier discrete-to-scattered corridor as a second realization

Let D be discrete, K compact scattered and b:D→K an ordinary bijection. For any compact Hausdorff P,Z, the discrete coproduct decomposition of \(\operatorname{Sub}(Z\times P\times D)\) and Theorem 2.2 for \(\operatorname{Sub}(Z\times P\times K)\) identify their sublocale lattices by relabeling k=b(d), even after a homeomorphism h_d:P→P is applied on each fiber. Explicitly,
\[
g:P\times D\to P\times K,\qquad (p,d)\mapsto(h_d(p),b(d))
\tag{TWIST}
\]
is continuous (D is discrete), ordinarily bijective and generally not a homeomorphism. Its map \(id_Z\times g\) induces **inverse complete-lattice isomorphisms** on all sublocales, obtained by relabeling plus the homeomorphic action \(id_Z\times h_d\).

The **complete-lattice transport** just proved is valid, but it does *not by itself* imply (G),(T),(O) for partially defined graph relations embedded in an arbitrary common compact Hausdorff ambient. Those conclusions require explicit ambient-sector, pullback and image compatibility, which was not specified here and remains a separate proof obligation. A fully justified sufficient replacement uses **partial monomial maps on one common compact scattered index K_*** with homeomorphism graphs on each matched fibre; see the post-referee reconciliation. The fibrewise lattice construction still extends the original untwisted tensor construction, with no continuity requirement on the family h_d.

Theorem 3.1 is a more dramatic unconditional realization **within** G=P×K, because its graph family is automatically closed under composition, even for discontinuous index permutations.

### 5. Why the abstraction is useful and its limitations

The scattered-coordinate case is no longer an isolated trick:

- It arises from the **sharp, parameterized atomic-index criterion** (MAT), not merely from ordinary pointwise bijectivity.
- It produces an explicit **large group** of genuinely localic-safe graph relations of wreath-product form, not just the earlier 15-arrow example.
- It transports *all* sublocales of the P-coordinate, including pointless ones, so the method genuinely handles **q** and the RHR overlap.
- The algebraic Balanced Witness Criterion can be applied to other graph families once their transport and overlap behavior is checked, without requiring scatteredness as part of its statement.

**Do not infer:** arbitrary graph relations on G=P×K associate when P is perfect; arbitrary maps with stable image surjections are safe; every safely adjoining graph satisfies (G),(T),(O); or the index-matrix construction works for nonscattered K. Over a perfect K the nonzero pointless Booleanization of K defeats the atomic-index decomposition.

**Research next:** (a) independently audit MAT and the wreath-product localic composition (including discontinuous permutations); (b) test a *non-atomic* but stably image-exact partial correspondence to see whether (G),(T),(O) can hold outside the scattered/indexed and homeomorphism mechanisms; (c) return to the intrinsic specialization relation and common-witness complexes after the planned big-picture review. This is a *candidate* general mechanism, not yet an externally certified new branch.
