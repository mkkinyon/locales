# Mathematical packet — Coherent localic chain nerves and nonconstant sheaf homotopy

**10 November 2026 · Self-contained independent audit packet · New working Claims A1–E3.**

This packet follows a previously independently checked coherent chain/higher-diagonal phase. It contains **new after-audit mathematics** rather than claiming the present developments were part of the earlier review. Standard ∞-topos, Priestley and condensed mathematics inputs are identified precisely. Publication priority is not claimed. **Please examine every claim, proof, example, aside, and hypothesis adversarially.**

## 0. Ground conventions and previously verified prerequisites

**Locales and order.** All work uses classical choice, at least the prime ideal/filter theorem, so coherent locales are represented as spectral spaces and their compact-open lattices. For coherent locale X, write K(X) for the bounded distributive lattice of compact opens, with O(X)=Idl K(X). Its compact Hausdorff *patch* is a Stone space P, ordered by spectral specialization
\[
x\le y\iff \forall k\in K(X),\quad (x\in k\Longrightarrow y\in k).
\]
Thus spectral opens are **upsets**, closed sublocales are **downsets**. For coherent X, proconstructible sublocales correspond to closed subspaces of its patch; for these (and not arbitrary sublocales), pointwise equality is actual localic equality. Spectral maps between coherent locales are continuous maps of Priestley spaces preserving order, with the converse established by Priestley duality.

**Simplicial locales.** The canonical *oriented* localic specialization subrelation \(A_X\hookrightarrow X^2\) is imposed frame-theoretically by \(\pi_0^*k\le\pi_1^*k\) for each compact open k. Its nerve \(\operatorname{Ch}_n(X)\subseteq X^{n+1}\) imposes \(x_0\le\cdots\le x_n\) for all n≥0. Let
\[
I_n(X)=\operatorname{cl}(\Delta_{n+1}),\qquad
D_n(X)=\operatorname{fit}(\Delta_{n+1}),
\]
where the index n means **arity n+1**. For coherent X these are actual proconstructible spectral sublocales whose spectral point tuples are precisely those with a **common upper**, respectively **common lower**, specialization witness in X. There are canonical simplicial inclusions Ch_•→I_• and Ch_•→D_•.

**Stone sheaf ∞-topos.** Fix a suitably large essentially small site Stone_κ, closed under necessary finite products and coproducts, with **finite jointly surjective families** (including the empty cover of the empty Stone locale) as covers. Work in \(\mathscr H=\mathrm{Shv}_\infty(\mathrm{Stone}_\kappa)\). The sheafified Yoneda embedding h preserves finite limits, finite coproducts and the initial object; finite jointly surjective Stone families are effective epimorphisms, so their augmented Čech nerves realize to their targets. Presheaf-space realizations can be sheafified because sheafification preserves colimits; **evaluation at an arbitrary Stone T need not commute with realization**, while evaluation at the one-point object does in this particular site. The constant-object functor from spaces is written \(\underline{(-)}\); for discrete group G, sections of \(\underline G\) on compact Stone T are **locally constant**, hence finite-image, functions T→G. Nonempty S→1 is a finite Stone cover (and thus effective epi). The choice of κ is large enough for all spaces used, and independence of κ is not asserted.

The three **patched sheaf-homotopy** objects are
\[
\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet(X))|,\quad
\mathbf I(X)=|h(\operatorname{Patch}I_\bullet(X))|,\quad
\mathbf D(X)=|h(\operatorname{Patch}D_\bullet(X))|.
\]
They are **not asserted to be intrinsic localic shapes**. We use the following *previously independently checked* result as a prerequisite:

> **Canonical edgewise arrow theorem (prerequisite).** For every coherent X, the two canonical arrows \((\mathbf C(X)\to\mathbf I(X))\) and \((\mathbf C(X)\to\mathbf D(X))\) are equivalent **in the undercategory \(\mathbf C(X)/\mathscr H\)**. It is obtained from the rectangle bisimplicial object E_{p,q} of all comparisons x_i≤y_j, patched effective Čech descent in its two directions, and the strict simplicial map splitting a chain of length 2n+2 into two blocks. The two block projections from twofold edgewise subdivision realize to equivalences (cofinality of ordinal sum), compatibly with the rectangle projections. This does **not** assert unpatched effective descent for the lower-witness projection. For finite P, the canonical inclusion Ord(P)→K_up(P) is a homotopy equivalence whenever the intersections of principal downsets at maximal points have contractible order complexes; for a finite simplex-boundary face poset all such intersections have a greatest element. The corresponding canonical D-side equivalence follows by the arrow theorem.

Other prerequisites: a finite cover by coherent **closed downsets** induces levelwise jointly surjective patch Stone covers of Ch_n and of the **relative ambient upper hull** \(I_n(X)\cap Z^{n+1}\), with Čech intersection formulas. Applying h and realizing yields *closed-side Čech codescent of the canonical C→I arrow*. This has been independently checked for covers with compact-open complements. It is critical to use **ambient** hulls, not I_n(Z), since a witness can lie outside Z. We will prove the open-side analogue here.

## A. The two-apex suspension and nonconstant homology

Let S be any nonempty Stone space. Define an ordered Stone space
\[
P(S)=S\sqcup\{p,q\},\qquad s<p,\ s<q\quad(s\in S),
\]
with no other strict comparabilities. p,q are isolated and incomparable; points of S retain their Stone topology and are pairwise incomparable.

**A1 (Priestley and compact-open lattice).** P(S) is Priestley. Its order graph is closed: the diagonal, S×{p}, S×{q} are closed, and clopen upsets distinguish incomparable pairs. In particular clopen upsets are exactly ∅, {p}, {q} and U∪{p,q} with U⊆S clopen. Thus the associated coherent X(S) has a completely explicit compact-open bounded distributive lattice, obtained by placing Clop(S) above the four-element Boolean diamond and identifying their adjacent extrema.

**A2 (realizations and canonical arrows).** Put Z_p=S∪{p}=X\{q}, Z_q=S∪{q}=X\{p}. These are patch-clopen closed downsets covering X, with common intersection S and terminal chain-nerve realizations (greatest elements p,q). Since Ch_n(S)=S (diagonal equality order), closed-side Čech descent gives
\[
\boxed{\mathbf C(X(S))\simeq1\amalg_{h(S)}1=:\Sigma h(S).}
\]
A tuple has a common upper witness iff it lies in Z_p^{n+1} or Z_q^{n+1}. Each simplicial piece is the Čech nerve of a nonempty Stone space mapping to 1; their overlap is S^{n+1}, also a Čech nerve of S→1. Thus \(\mathbf I(X(S))\simeq1\). By the prerequisite canonical edgewise theorem, \(\mathbf D(X(S))\simeq1\), and both canonical arrows are the unique arrow \(\Sigma h(S)\to1\). Their common cofiber is \(\Sigma^2h(S)\).

**A3 (homology and nonconstancy).** Denote by \(\mathbb Z[h(S)]\) the free abelian sheaf, obtained by sheafification of T↦\(\mathbb Z[\operatorname{Cont}(T,S)]\). Let \(\varepsilon:\mathbb Z[h(S)]\to\underline{\mathbb Z}\) be augmentation. The reduced homology sheaves of the unreduced suspension satisfy
\[
\widetilde{\mathcal H}_1(\Sigma h(S);\mathbb Z)\cong\ker\varepsilon,\qquad
\widetilde{\mathcal H}_j=0\quad(j\ne1).
\]
Because S→1 is effective epi, augmentation is epi; apply Mayer–Vietoris or the free simplicial abelian chain functor to the pushout 1←h(S)→1. If S is finite, h(S) is a finite coproduct of copies of 1 and \(\Sigma h(S)\) is a constant wedge of |S|−1 circles. If S is infinite, the section
\[
\sigma=[\operatorname{id}_S]-[\operatorname{const}_{s_0}]\in(\ker\varepsilon)(S)
\]
has pairwise distinct point-values [s]−[s_0] for s∈S; a section of a constant discrete abelian sheaf on compact Stone S has finite image. Thus ker ε is **nonconstant** and \(\Sigma h(S)\) is nonconstant. In fact Σh(S) is constant iff S is finite.

## B. Open-cover gluing of the fitted hull, for all locales

For **arbitrary locale** X, not assumed coherent/spatial, let \(\{u_i\}_{i\in I}\subseteq\mathcal O(X)\) be any (possibly infinite) open cover, \(\bigvee_i u_i=1\). Put \(w_i=\bigwedge_{j=0}^n\pi_j^*(u_i)\in\mathcal O(X^{n+1})\).

**B1 (all-locale cover identity).** In the actual frames
\[
\boxed{\bigvee_i w_i|_{\operatorname{Ch}_n(X)}=1,
\qquad\bigvee_i w_i|_{D_n(X)}=1}\quad(n\ge0).
\]
Proof: In Ch_n, specialization implies \(\pi_0^*u_i\le\pi_j^*u_i\), hence w_i=\pi_0^*u_i and their join is 1. For D_n, the open O(w) with w=∨_i w_i contains the diagonal because \(\Delta_{n+1}^*(w)=\bigvee_i u_i=1\). Since the fitted hull is the intersection of **all** open sublocales containing the diagonal, D_n≤O(w), equivalent to w|_{D_n}=1. Each pair of families of opens
\[
\operatorname{Ch}_n(U_i)=\operatorname{Ch}_n(X)\cap U_i^{n+1},\qquad
H_n^{X,\downarrow}(U_i)=D_n(X)\cap U_i^{n+1}
\]
therefore covers its target; multiple intersections are the same constructions on U_{i_0}∩⋯∩U_{i_k}. The localization of Ch is intrinsic; the relative fitted hull is **ambient**, not generally D_n(U_i). Because the coproduct of each open-chart family is an open surjection of locales, standard Joyal–Tierney effective descent gives **degreewise localic open-cover descent**. This statement is not about descent of the lower-witness projection E→D, which can fail without patching.

**B2 (coherent patched D-side codescent).** If X is coherent and u_1,…,u_r are **compact opens** with ∨_i u_i=1, their open charts U_i and their finite intersections are coherent and patch-clopen Stone, so after Patch the degreewise open-cover families above are jointly surjective Stone covers. Defining
\[
\mathbf R_X^\downarrow(U_S)=|h(\operatorname{Patch}(D_\bullet(X)\cap U_S^{\bullet+1}))|,
\quad U_S=O(\bigwedge_{i\in S}u_i),
\]
we obtain the canonical arrow \(\mathbf C(X)\to\mathbf D(X)\) as the homotopy-colimit of the local canonical maps \(\mathbf C(U_S)\to\mathbf R_X^\downarrow(U_S)\) over the **full indexed Čech diagram**, retaining repeated indices and multiplicities. Therefore equivalences on each nonempty intersection imply equivalence of the global canonical arrow. By the prerequisite edgewise theorem this also gives C→I.

**B3 (dual ambient-LB test, exactness).** Let U=O(u) be a nonempty compact open of coherent X and K=K(X). Define
\[
(\mathrm{LB})_u:\quad
u\nleq k_1,\ldots,u\nleq k_m\Longrightarrow\bigvee_{i=1}^m k_i\ne1
\]
for every finite nonempty family of k_i∈K. This is equivalent to the existence of a spectral point z∈X **below every point of U**, which need not lie in U; and equivalent to \(H_n^{X,\downarrow}(U)=U^{n+1}\) as actual coherent proconstructible sublocales for every n. Proof: the set \(\{k:u\nleq k\}\) generates a proper ideal; extend to a prime ideal J, and take z from its complementary prime filter. If z∈k while x∈U\setminus k then k∈J, contradiction. Conversely if every finite tuple in U has a lower witness, choose x_i∈U\setminus k_i, and any lower witness lies in none of k_i (opens are upsets). Since K(U)≅[0,u]_K, either a greatest point of U, or (LB)_u plus SNC (\(\mathbf C(U)\simeq1\)), is sufficient to make its local relative comparison an equivalence. Applied to every compact-open chart intersection, this supplies a dual finite-cover criterion.

## C. Mixed Čech descent, ordinal sums, and nonconstant higher obstructions

**C1 (mixed closed/open chain cover).** Suppose coherent X has finite patch-closed specialization downset cover {Z_i} with compact-open complements and finite patch-clopen upset cover {U_j}. Every chain x_0≤⋯≤x_n lies in some intersection W_{ij}=Z_i∩U_j: choose Z_i containing its last vertex, U_j its first. Therefore the mixed two-indexed Čech diagram, in bidegree (p,q) built from \(\mathbf C(Z_{i_0}\cap\cdots\cap Z_{i_p}\cap U_{j_0}\cap\cdots\cap U_{j_q})\), realizes to \(\mathbf C(X)\). **Warning:** those same mixed cells need not cover either I_n or D_n; use closed covers for I and open covers for D separately.

**C2 (ordinal-sum theorem).** For nonempty coherent locales P,Q, form the Priestley ordinal sum P⊕Q: disjoint-union patch topology, original orders, and every p∈P below every q∈Q. It is again Priestley. Every length-(n+1) chain has a unique cut between its P-block and its Q-block, so its patched simplicial chain nerve is exactly the *simplicial join* of the nerves of P and Q, with the empty-chain convention. Hence
\[
\boxed{\mathbf C(P\oplus Q)\simeq\mathbf C(P)*\mathbf C(Q),\qquad
A*B=\operatorname{hocolim}(A\leftarrow A\times B\to B).}
\]
Moreover \(\mathbf I(P\oplus Q)\simeq\mathbf D(P\oplus Q)\simeq1\): choose spectral p_0∈P and q_0∈Q. Inserting p_0 into a common-upper-witness tuple preserves the upper-witness condition (if the witness lies in Q, p_0 is below it; if every tuple coordinate lies in P, any Q-point witnesses the enlarged tuple). Dually inserting q_0 into a common-lower-witness tuple preserves its lower witness (if any tuple point is in P, its old lower witness is also below q_0; if all coordinates are in Q, choose any P-point as new lower witness). These pointwise factorizations induce strict actual spectral/localic extra degeneracies because the domains and hulls are coherent proconstructible, and thus contract both simplicial realizations.

**C3 (higher sheaf-homotopy obstructions).** For a two-point antichain A, \(\mathbf C(A)=\underline{S^0}\), and \(\mathbf C(A\oplus Z)\simeq\Sigma\mathbf C(Z)\simeq\mathbf C(Z\oplus A)\). For any nonempty Stone S and r,s≥1, the layered locale \(X_{r,s}(S)=A^{\oplus r}\oplus S\oplus A^{\oplus s}\) has
\[
\boxed{\mathbf C(X_{r,s}(S))\simeq\Sigma^{m}h(S),\quad
\mathbf I=\mathbf D=1,\quad m=r+s\ge2.}
\]
This is (m−1)-connected in \(\mathscr H\), with first nontrivial homotopy sheaf
\[
\pi_m\mathbf C(X_{r,s}(S))\cong
\mathcal K_S:=\ker(\mathbb Z[h(S)]\xrightarrow{\varepsilon}\mathbb Z)
\]
by internal Hurewicz; its other reduced homology sheaves vanish. For infinite S, \(\mathcal K_S\) is nonconstant by A3. The common relative cofiber of canonical C→I,D is \(\Sigma^{m+1}h(S)\).

## D. A genuinely nonconstant common C=I=D realization

Choose a finite poset P with a **minimal** element v (not necessarily least), and nonempty Stone space S. Form
\[
W_S(P,v)=\{v\}\sqcup (S\times(P\setminus\{v\})),
\]
with disjoint-union Stone topology. Comparisons within one s-fiber are inherited from P, v≤(s,x) iff v≤_P x, and there are **no comparisons across distinct nonbasepoint fibers**.

**D1 (Priestley and compact-open lattice).** This is Priestley. Closed order and separation follow from closed diagonals in S×S and clopen upset slices. The compact-open lattice is the bounded distributive lattice of locally constant maps f:S→Ups(P) with the indicator of membership of v **independent of s**. Formally, it is the fiber product of LC(S,Ups(P))→LC(S,2), f↦[v∈f(s)], with 2→LC(S,2) as constant functions.

**D2 (actual gluing, canonical comparison).** Put \(v_n=(v,\ldots,v)\) in Ch_n(P) and I_n(P). For every n, there are actual Stone isomorphisms
\[
\operatorname{Patch}\operatorname{Ch}_n(W)
\cong1\sqcup (S\times(\operatorname{Ch}_n(P)\setminus\{v_n\})),
\]
\[
\operatorname{Patch}I_n(W)
\cong1\sqcup (S\times(I_n(P)\setminus\{v_n\})).
\]
A non-v coordinate in a chain forces all other non-v coordinates to have the **same s**, and a tuple with a common upper witness likewise must be in one fiber, with v allowed: if the witness lies in s-fiber, every coordinate below it does too; if the witness is v, all coordinates are v. These descriptions are closed/sub-constructible actual coherent spectral sublocales, not arbitrary point sets. Simplicial operators either preserve the parameter s or send the tuple to the unique v_n; compatibility is strict. In degree n, the following are pushouts **along a clopen coproduct summand**, not arbitrary Stone quotient pushouts:
\[
\begin{array}{ccc}
S\times\{v_n\}&\to&S\times\operatorname{Ch}_n(P)\\
\downarrow&&\downarrow\\
1&\to&\operatorname{Patch}\operatorname{Ch}_n(W)
\end{array}
\qquad
\text{and similarly for }I_n.
\]
After h and realization this gives, compatibly with the *canonical inclusion*,
\[
\boxed{\mathbf C(W)\simeq h(S)_+\wedge\mathbf C(P),\qquad
\mathbf I(W)\simeq h(S)_+\wedge\mathbf I(P).}
\]
If the *finite* canonical \(\mathbf C(P)\to\mathbf I(P)\) is an equivalence, so is the *actual* \(\mathbf C(W)\to\mathbf I(W)\); the prerequisite edgewise theorem then gives a canonical equivalence C(W)→D(W). **Do not assert that D_n(W) has the same fiberwise gluing**: points in different fibers can share a lower witness v.

**D3 (nonconstant common homotopy groups in every positive degree).** Let P_m=F(∂Δ^{m+1}) be the nonempty face poset of a triangulated m-sphere, v one of its minimal vertices. Its order complex is the barycentric subdivision of S^m and the finite canonical C(P_m)→I(P_m) is a homotopy equivalence by the crosscut criterion. Put X_m(S)=W_S(P_m,v). Then
\[
\boxed{\mathbf C(X_m(S))\xrightarrow{\sim}\mathbf I(X_m(S)),\quad
\mathbf C(X_m(S))\xrightarrow{\sim}\mathbf D(X_m(S)),\quad
\mathbf C(X_m(S))\simeq h(S)_+\wedge\underline{S^m}.}
\]
Its reduced homology sheaf is \(\widetilde{\mathcal H}_m\cong\mathbb Z[h(S)]\), other reduced homology zero. This is the **full free** abelian sheaf, unlike the augmentation kernel in C3: the common basepoint is identified. For m≥2 this object is (m−1)-connected, and internal Hurewicz gives \(\pi_m\cong\mathbb Z[h(S)]\). For m=1 the connected π₁-sheaf has abelianization \(\mathbb Z[h(S)]\). If S is infinite, \([\mathrm{id}_S]\in\mathbb Z[h(S)](S)\) has distinct values [s] on points and proves nonconstancy. Thus **both canonical comparisons are equivalences, yet their common realization has essential nonconstant sheaf homotopy in every prescribed m≥1**. Finite k-fiber controls give wedges of k circles for m=1; for general m wedges of k m-spheres.

## E. Reconstruction: what the homology sheaf remembers

Write M_S=\(\mathbb Z[h(S)]\), the degree-m homology sheaf in D3.

**E1 (published negative result, not independently proved here).** Clausen–Scholze, *Condensed Mathematics and Complex Geometry*, Lecture III (2022), printed p. 26, discussion following Question 3.6, state that if S=βN and T is the quotient by identifying two distinct points in the remainder βN\N, then \(\mathbb Z[h(S)]\cong\mathbb Z[h(T)]\) as **unmarked condensed abelian groups**. The quotient T is Stone but not homeomorphic to S: S is extremally disconnected, whereas T is not. For the latter, choose clopen V⊂S containing one identified nonisolated point a and not the other b. The image of the saturated open V\{a} has closure containing the glued point but not an open neighborhood there (every neighborhood meets points near b outside V). Zero-dimensionality of T follows from saturated unions of clopen neighborhoods around a,b and clopen neighborhoods elsewhere. Thus **unmarked** M_S is not a complete invariant of the topology of S, even though it detects finite versus infinite Stone spaces by nonconstancy. Source: https://people.mpim-bonn.mpg.de/scholze/Complex.pdf ; do not infer that the *full unmarked homotopy objects* h(S)_+∧S^m and h(T)_+∧S^m are equivalent.

**E2 (diagonal coalgebra and group-like reconstruction).** The free abelian sheaf functor satisfies \(\mathbb Z[A\times B]\cong\mathbb Z[A]\otimes\mathbb Z[B]\). Linearizing the diagonal and terminal maps of h(S) equips M_S with a canonical *cocommutative counital coalgebra*
\[
\delta:M_S\to M_S\otimes M_S,\qquad
\varepsilon:M_S\to\underline{\mathbb Z},\quad
\delta([s])=[s]\otimes[s],\quad\varepsilon([s])=1.
\]
Define the group-like **subsheaf** G_S of sections x satisfying \(\delta(x)=x\otimes x\) and \(\varepsilon(x)=1\). **Claim:** \(G_S\cong h(S)\) naturally. For finite E, a group-like element ∑n_e[e] of Z[E] satisfies \(n_e=n_e^2\), \(n_en_f=0\) for e≠f, and ∑n_e=1, hence equals exactly one [e]. For general S=lim_i S_i finite, a group-like section over test Stone R yields compatible locally constant R→S_i, hence a continuous f:R→S. Clausen–Scholze Proposition 3.3, printed p. 25, embeds \(M_S\) as a subsheaf of \(\varprojlim_i\mathbb Z[S_i]\): it is the union of inverse limits of finite ℓ¹-bounded subsets. Thus the original section equals [f]. Conversely [f] is group-like, showing G_S=h(S) functorially.

**E3 (full faithfulness but only WITH coalgebra).** Every coalgebra morphism \(M_S\to M_T\) restricts to a morphism of group-like subsheaves h(S)→h(T), i.e. a unique continuous map S→T, and is its unique free-abelian linear extension. Conversely that extension preserves diagonal and counit. Therefore
\[
\boxed{\operatorname{Hom}_{\mathrm{cocomm\ coalg}}(M_S,M_T)
\cong\operatorname{Cont}(S,T),}
\]
so the functor S↦(M_S,δ,ε) is fully faithful. **Critical caveat:** the diagonal coalgebra structure is *extra data coming from the free presentation*; it has not been shown to be an intrinsic structure on the *unmarked* sheaf-homotopy object of D3. The Clausen–Scholze unmarked isomorphism in E1 must not be assumed to preserve the chosen coalgebras. Full homotopy-object reconstruction remains unproved.

## Sources / exact literature boundary

- **Clausen–Scholze**, *Condensed Mathematics and Complex Geometry*, 2022, Lecture III, Propositions 3.3 and 3.5 with the example after Question 3.6: https://people.mpim-bonn.mpg.de/scholze/Complex.pdf . Their free-ab-group inverse-limit embedding is used in E2; their unmarked-isomorphism example is *quoted, not proved* in E1.
- **Commelin–Scholze**, *Lectures on Condensed Mathematics*, Proposition 2.5, for the sheafification-based free abelian group adjunction: https://math.commelin.net/files/LTE.pdf .
- **Cameron–Kumar**, *Graphs on topological spaces*, arXiv:2610.14783v1 §9 for the finite-poset homotopy-type criterion, with the canonical inclusion as an additional previously independently checked deduction.
- **Standard category/homotopy machinery:** Joyal–Tierney effective descent for open localic surjections; ∞-topos Čech descent and universal colimits, internal Mayer–Vietoris and Hurewicz; simplicial join of category nerves and homotopy join; Stone–Priestley duality. None is presented as new.

## Explicit scope and unresolved points

All main statements concern the patched Stone-sheaf \(\infty\)-topos, **not** a weak-equivalence model on unpatched locales or intrinsic localic shape. The original independently checked edgewise theorem is accepted as a precisely stated premise; this packet tests its **new applications**, not its original proof. The fixed site must be chosen large enough to include every Stone test space appearing (notably βN in E1). The current segment does not prove that the full sheaf-homotopy object h(S)_+∧S^m recovers S; it proves only that its free homology sheaf does not, while the **enriched coalgebra** does. This entire A–E packet is **new working mathematics**; no claim of prior independent review or publication priority is made.