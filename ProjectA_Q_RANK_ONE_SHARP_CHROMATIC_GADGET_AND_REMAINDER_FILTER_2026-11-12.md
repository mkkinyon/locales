# Project A — Rank-one Q: sharp Urysohn chromatic gadgets and a canonical chromatic remainder filter

**12 November 2026 — NEW INTERNAL bounded result, no independent audit or literature-priority judgment.** Requested continuation of the rank-one finite-box colouring theorem after the blind referee's linking-graph and rank-one suggestions. **Question Q is NOT solved.** This segment has two complementary conclusions:

1. The special far-rectangle formula \(z_1=d_{\mathcal U}=\bigvee_{p^*\vee q^*=1}p\boxtimes q\) **does NOT alone bound the chromatic number** of the cross-link graph: for every \(m\ge1\) an explicit **compact, sober, locally compact \(T_1\)** space realizes \(K_{2^m}\) as a cross-link graph, with EXACTLY m product boxes in the relevant Urysohn restriction. Thus the \(2^m\) bound of [the previous theorem](ProjectA_Q_rank_one_BOX_COLORING_and_LOCAL_PRODUCT_RIGIDITY_2026-11-12.md) is **sharp even for actual Urysohn relations**, not just abstract unions of bicliques. Necessarily finite stabilization **fails** in these gadgets, since the bad cover is already finite.
2. When finite stabilization **does hold**, every genuine hole has a canonical **chromatic ideal** on its bad-cover index set: deleting **ANY finitely colourable subfamily** leaves the complementary diagonal square **dense on the ENTIRE hole**, not merely nonzero. This is a new exact localic/Boolean strengthening of the referee's infinite-chromatic obstruction. The quotient Boolean algebra by the chromatic ideal is nonzero and atomless (under ordinary classical graph compactness), and the construction is hereditarily repeated in every nonzero relatively open part of the hole.

The first result prevents a naive universal finite-colouring argument from the far-rectangle presentation. The second says precisely what additional structure any successful proof of Q must exploit, and does not create a new geometrical counterexample family.

## 0. Framework and notation

Let L=O(X), \(Q_X=L\oplus L\). For an open cover C of X let \(w_C=\bigvee_{c\in C}c\boxtimes c\). The full/finite pre-nuclei are \(\Phi,\Phi_2\) as usual, and
\[
z_1=\Phi(0)=\Phi_2(0)=d_{\mathcal U},
\qquad
\mathcal U=\mathfrak c(z_1).
\]
Question Q is the universal implication \(\Phi_2(z_1)=z_1\Rightarrow\Phi(z_1)=z_1\).

For a general closed relation \(T=\mathfrak c(d)\le X^2\) and a **relatively open** sublocale \(E\le T\), define a graph \(G_E(C)\) with vertex set the members of a given open cover C, putting an edge between distinct c,c' when
\[
E\wedge\mathfrak o(c\boxtimes c')\ne0
\quad\text{or}\quad
E\wedge\mathfrak o(c'\boxtimes c)\ne0.
\tag{0.1}
\]
This graph is not assumed to be given by ordinary points; it uses actual localic nonzero restrictions. For \(A\subseteq C\), write \(u_A=\bigvee_{c\in A}c\), \(u_\varnothing=0\).

## 1. Sharpness of the finite-box chromatic bound for actual Urysohn relations

**Theorem 1.1 (sharp \(2^m\) Urysohn gadgets).** For every integer \(m\ge1\) there is a compact, locally compact, sober \(T_1\) space \(X_m\), disjoint opens a,b, and a FINITE open cover
\[
C=\{c_v:v\in 2^{\{1,\ldots,m\}}\},\qquad |C|=2^m,
\tag{1.1}
\]
such that:
- \(r=a\boxtimes b\) meets \(\mathcal U(X_m)\) nontrivially;
- \(r\wedge w_C\le d_{\mathcal U(X_m)}\), i.e. every same-member local Urysohn restriction vanishes;
- the Urysohn restriction \(\mathcal U(X_m)[r]\) is a join of **exactly m** nonzero localic product sublocales, and cannot be a join of fewer;
- the corresponding cross-link graph \(G_C(a,b;\mathcal U)\) is the **complete graph \(K_{2^m}\)**. Thus
\[
\boxed{\chi(G_C)=2^m}
\tag{1.2}
\]
and the numerical bound in the previous finite-box colouring theorem is sharp even for actual far-generated Urysohn relations.

**Construction.** Let \(V=2^{\{1,\ldots,m\}}\). For each k=1,…,m define a separate compact three-level multi-apex component Y_k. Its nonisolated points are
\[
L_k=\{\alpha_{k,v}:v\in V,\ v_k=0\},\quad
R_k=\{\gamma_{k,v}:v\in V,\ v_k=1\},
\quad \beta_k.
\]
To EACH alpha attach an infinite private set of isolated points \(N^L_{k,v}\), and to EACH gamma attach a disjoint infinite private set \(N^R_{k,v}\). Neighborhood bases:
- alpha: \(\{\alpha_{k,v}\}\cup(N^L_{k,v}\setminus F)\) for finite F;
- gamma: \(\{\gamma_{k,v}\}\cup(N^R_{k,v}\setminus F)\) for finite F;
- beta: \(\{\beta_k\}\cup(N_k\setminus F)\), where \(N_k\) is the union of ALL private rays of component k, F finite;
- the ray points themselves are isolated.
Put \(X_m=\coprod_{k=1}^mY_k\). All distinguished singletons are closed (T1). Any open cover of Y_k has a beta-neighborhood covering all but finitely many isolated ray points, and finitely many alpha/gamma apices and exceptional ray points remain; so Y_k and X_m are compact. Every nonempty irreducible closed subset with an isolated ray point splits using its clopen singleton; any irreducible closed subset without ray points is finite and T1 and hence a singleton. Thus X_m is sober. The same compact neighborhoods show it is locally compact, so its **localic square is represented by the ordinary product**.

Let
\[
a=\bigcup_k\bigcup_{v_k=0}
\bigl(\{\alpha_{k,v}\}\cup N^L_{k,v}\bigr),\quad
b=\bigcup_k\bigcup_{v_k=1}
\bigl(\{\gamma_{k,v}\}\cup N^R_{k,v}\bigr).
\tag{1.3}
\]
They are disjoint opens. For every alpha in L_k and gamma in R_k, the closures of ANY two neighborhoods intersect at beta_k: every beta-neighborhood meets every cofinite private ray. Hence the pair lies in the ordinary point set of U. No pair involving an isolated ray point from a×b lies in U because its singleton is clopen; no cross-component pair lies in U because the components are clopen. Therefore
\[
\boxed{
\mathcal U(X_m)\wedge\mathfrak o(a\boxtimes b)
=\bigvee_{k=1}^m(L_k\times R_k).
}
\tag{1.4}
\]
The product factors L_k,R_k are finite closed discrete sublocales (the restriction to the open a or b is legitimate); this is an equality of sublocales because the square is spatial and U is CLOSED. No single nonzero product sublocale contained in (1.4) can meet two different k-components: the cross product would contain pairs in distinct clopen components, outside U. Thus the product-box rank is EXACTLY m.

For each v∈V define a global open c_v by its trace on each Y_k:
\[
c_v\cap Y_k=
\begin{cases}
Y_k\setminus R_k,&v_k=0,\\
Y_k\setminus L_k,&v_k=1.
\end{cases}
\tag{1.5}
\]
These traces are open since apex singletons are closed. The c_v cover X_m: in each component there are v of both kth bits and the corresponding two opens cover all Y_k. Each c_v omits one entire alpha/gamma side in each component, hence
\[
\mathcal U[r]\wedge\mathfrak o(c_v\boxtimes c_v)=0
\quad\forall v\in V.
\tag{1.6}
\]
But for v≠w choose k with v_k≠w_k: the c_v/c_w cross rectangles contain a left/right apex pair, and thus meet U. Every pair of distinct vertices is adjacent; G is K_{2^m}.

**Consistency with Q.** C is FINITE. Therefore (1.6) directly proves \(\Phi_2(z_1)>z_1\) on X_m. The theorem gives **NO Q counterexample**. It decisively shows, however, that the special definition of \(z_1\) as the join of far rectangles imposes NO universal numerical chromatic bound in the absence of finite stabilization: the previous \(2^m\) bound is realized sharply even by compact sober T₁ spaces.

**Optional general graph variant.** For any finite simple graph H, take one three-apex component (one left alpha, one right gamma, one intermediate beta with two private rays) for each edge ij, and let c_i contain its component minus gamma and c_j contain its component minus alpha. The same construction gives cross-link graph isomorphic to H, after omitting isolated vertices. Thus **arbitrary finite graphs** can occur. The K_{2^m} construction above is stronger because it has only m product boxes and makes the 2^m bound sharp.

## 2. The exact independent-set/diagonal-square equivalence

**Lemma 2.1.** Let \(E\le X^2\) be any sublocale satisfying \(E\wedge\mathfrak o(c\boxtimes c)=0\) for every \(c\in C\), and define G_E(C) by (0.1). Then for every A⊆C,
\[
\boxed{
G_E[A]\text{ has NO edges}
\iff
E\wedge\mathfrak o(u_A\boxtimes u_A)=0.
}
\tag{2.1}
\]
*Proof.* The frame identity
\[
u_A\boxtimes u_A
=\bigvee_{c,c'\in A}c\boxtimes c'
\]
and the fact that *restriction of opens to E preserves arbitrary joins* show that the relative open represented by u_A⊠u_A is zero exactly when all its cross-square summands are zero. The diagonal c=c' terms already vanish by hypothesis; the remaining terms are exactly the edges of G_E[A]. This is an identity of relative OPEN SUBLOCALES of E, not an illegitimate arbitrary meet/join distribution in the full lattice of all sublocales. □

Consequently, for a finite partition \(C=A_1\cup\cdots\cup A_k\), its coarsened finite cover \(\{u_{A_i}\}\) annihilates E iff the partition is a proper k-colouring of G_E. The **minimal cardinality of a finite union-coarsening** of the original C whose diagonal square misses E is exactly χ(G_E), when this is finite.

## 3. Finite stabilization gives a MUCH stronger chromatic tail property

**Theorem 3.1 (dense chromatic remainder; arbitrary locales).** Let X be a locale, T=C(d) any CLOSED relation on X², and assume
\[
\boxed{\Phi_2(d)=d.}
\tag{3.1}
\]
Let C be an arbitrary X-cover with a nonzero relative OPEN hole
\[
E=T\wedge\mathfrak o(w_C\to d)\ne0.
\tag{3.2}
\]
Let \(G=G_E(C)\), and let
\[
\mathscr J_G=
\{A\subseteq C:G[A]\text{ has finite chromatic number}\}.
\tag{3.3}
\]
Then:

**(i)** G has INFINITE chromatic number, and \(\mathscr J_G\) is a **proper ideal** in P(C), containing all finite subsets.

**(ii) Strong tail-density.** For EVERY \(A\in\mathscr J_G\), let \(v_A=u_{C\setminus A}=\bigvee_{c\in C\setminus A}c\). Then
\[
\boxed{E\wedge\mathfrak o(v_A\boxtimes v_A)
\text{ is DENSE in }E.}
\tag{3.4}
\]
Equivalently, writing \(B(E)\) for its least dense Boolean sublocale, and \(h,k:L\to M=O(B(E))\) for the coordinate maps,
\[
\boxed{h(v_A)=k(v_A)=1_M.}
\tag{3.5}
\]
These assertions strengthen the referee's “infinite-chromatic” necessary condition: even after deleting an arbitrary **infinite but finitely colourable** portion of C, the complementary diagonal square remains dense on the ENTIRE hole, not just nonzero somewhere.

**(iii) Hereditarily infinite chromatic.** The same cover C induces an infinite-chromatic graph \(G_V(C)\) on every nonzero relatively OPEN sublocale \(V\le E\). Every finitely colourable subset of this graph likewise has a complementary tail square dense in V.

**(iv) Chromatic quotient.** Under classical graph compactness (de Bruijn–Erdős and ordinary choice),
\[
\boxed{\mathcal P(C)/\mathscr J_G\text{ is a nonzero ATOMLESS Boolean algebra.}}
\tag{3.6}
\]
Consequently a free ultrafilter of C can be chosen which contains NO subset inducing a finite-chromatic graph. Such a choice is **optional**; the ideal and the density statement are canonical and choice-free once C,E are fixed.

*Proof of (i)–(iii).* The graph has no loops because \(E\wedge O(w_C)=0\), and since d is finite-cover fixed, every finite cover F satisfies \(w_F\to d=d\). Thus \(T\wedge O(w_F)\) is DENSE in T, and restricting this open to E leaves a DENSE open of E.

Let \(A\in\mathscr J_G\) have a proper k-colouring \(A=A_1\cup\cdots\cup A_k\). By Lemma 2.1, all the coarsened opens \(u_{A_i}\) have squares missing E. The finite family
\[
F_A=\{u_{A_1},\ldots,u_{A_k},v_A\}
\tag{3.7}
\]
covers X because C does. Its square restricted to E equals the relative open square of \(v_A\), since all k other terms vanish. It is dense by finite-fixedness. This proves (3.4). Isbell's least dense Boolean sublocale B(E) lies in that square, giving (3.5): the full Boolean matching value \(h(v_A)\wedge k(v_A)\) is 1, hence both values are 1.

If C itself had finite chromatic number, use A=C in the preceding argument; then \(v_A=0\), contrary to density of its zero square in nonzero E. Thus χ(G)=∞ and \(\mathscr J_G\) is proper. It is an ideal: induced-subgraph finite-colourability is downward closed, and unions of two finitely colourable sets can be coloured with DISJOINT palettes, so the union is finitely colourable. Every finite subset belongs to the ideal.

For any nonzero relatively open V⊆E, it is also relatively open in T. The same finite-cover density proof works with V in place of E (all c-squares still miss V). Thus the local graph G_V has infinite chromatic number, and its own chromatic remainder ideal satisfies the same density conclusion.

*Proof of (iv).* Let A⊆C be any set with infinite χ(G[A]). Deleting a finite subset preserves infinite chromaticity: otherwise a finite coloring of what remains can be extended by finitely many fresh colors. By the classical de Bruijn–Erdős graph compactness theorem, every such graph has finite induced subgraphs of arbitrarily high finite chromatic number. Inductively choose pairwise vertex-disjoint finite induced subgraphs \(H_n\subseteq A\) with \(\chi(H_n)>n\). Let \(A_0\) be the union of H_n for even n, and \(A_1\) that for odd n. Both A_0,A_1 are disjoint and have infinite chromatic number. Consequently every nonzero class [A]∈P(C)/J contains two disjoint nonzero classes (e.g. [A_0] and [A\A_0]), so the quotient Boolean algebra has no atoms. Properness gives nonzero quotient; J contains singletons, so ultrafilters disjoint from J are nonprincipal. □

### 3.1 Rank-one specialization and the previously identified exceptional sector

In Question Q set T=U, d=z₁=d_U and suppose \(\Phi_2(z_1)=z_1\) but \(\Phi(z_1)>z_1\). For any bad cover C, the canonical open hole E from (3.2) lies in
\[
G_\perp=\mathcal U\wedge\mathfrak o(d_{\mathcal U}^{**}\wedge d_{\mathcal I}),
\]
by the universal regular-core and inseparability inclusions. Theorem 3.1 applies **without requiring E to decompose into any product boxes**. Thus its chromatic ideal \(\mathscr J_G\) and its strong tail-density are canonical properties of the exact nonregular off-inseparability part of a putative Q counterexample.

This is a **stronger and more intrinsically self-reproducing condition** than the original statement “χ(G)=∞”: for every finitely colourable family of members removed, the rest must be dense on the SAME hole, and this persists in EVERY nonzero open part.

**It is not a contradiction by itself.** For example the complete graph on a countably infinite set has J=Fin and perfectly legitimate free ultrafilters. The proof does NOT show the far-rectangle generation \(z₁=\bigvee_{\mathrm{far}}r\) rules out the resulting chromatic filters. Achieving that would be genuine further progress on Q.

## 4. Critical weak-defect control: K_ω and the same tail filter already occur when Q HOLDS

The chromatic ideal and tail-density theorem MUST NOT be confused with a solution of Q. A direct adversarial control uses the older completed powerset Scott example.

Let \(S=\mathcal P(\omega)\setminus\{\varnothing\}\) with the Scott topology, and \(c_n=\{A\in S:n\in A\}\). Let \(M=\operatorname{RO}(2^\omega)\) and use the two frame maps \(h,k:O(S)\to M\) with
\[
h(c_n)=[x_n=0],\qquad k(c_n)=[x_n=1].
\tag{4.1}
\]
They match every finite cover to 1 but the countable cover \(\{c_n\}\) to 0. For n≠m,
\[
h(c_n)\wedge k(c_m)=[x_n=0,x_m=1]\ne0,
\]
while \(h(c_n)\wedge k(c_n)=0\). Thus the **BOOLEAN-PROBE** cross-link graph on \(\{c_n\}\) is exactly \(K_\omega\), with
\[
\mathscr J_G=\mathrm{Fin}(\omega),\qquad
\bigvee_{n\ge N}h(c_n)=\bigvee_{n\ge N}k(c_n)=1_M
\quad\forall N.
\tag{4.2}
\]
The finite chromatic ideal is proper and its quotient \(P(\omega)/\mathrm{Fin}\) is atomless; the same dense-tail behaviour is present on this Boolean *fitting* witness. But S is hyperconnected, so \(d_{\mathcal U(S)}=0\) and
\[
\Phi_2(0)=\Phi(0)=0,\qquad
\mathcal W(S)=\mathcal W_2(S)=\mathcal U(S)=S^2.
\tag{4.3}
\]
The Boolean probe is a **closed-relative weak defect**, not the Booleanization of a nonzero **open U-hole**. Its image lies in the closed complement of the dense full-cover square and is nowhere dense in U.

Hence **infinite chromaticity, even complete-graph chromaticity, atomless chromatic quotient, nowhere distributivity, and dense tails all coexist with a POSITIVE Q instance**. They are necessary conditions of a hypothetical strong hole but not sufficient. In any future Q argument, the **relatively OPEN position of the hole in G_perp**, and the specific far-generation of U, must be used in a way that the completed powerset Scott control excludes. This is the anti-drift falsification test for this line.

## 5. Research decision and remaining precise test

- **Ruled out:** An a priori universal finite chromatic bound from the far-rectangle presentation ALONE. Explicit actual-Urysohn K_{2^m} gadgets disprove it in the absence of finite stabilization, and attain the finite-box bound sharply.
- **Established under finite stabilization:** The canonical chromatic ideal J and its **strong tail-density** on every open part of a bad hole, for ANY finite-fixed closed relation (including rank-one U).
- **Remaining key task for Q:** Use the **specific** far-rectangle structure of z₁, together with finite stabilization, to contradict the dense chromatic remainder filter on the off-inseparability boundary G_perp—or construct an actual rank-one hole meeting all these constraints. High chromaticity alone, or the existence of a free ultrafilter, is not enough.

This is a bounded algebraic result; it is not another construction search for a Q counterexample. It does NOT claim Q or Q′ solved.

**Status: NEW INTERNAL WORKING PROOFS, not independently audited; Q/Q′ OPEN.**
