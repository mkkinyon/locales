# Project A — Rank-one Q: finite-box colouring and local product rigidity

**12 November 2026. New INTERNAL bounded theorem; not externally audited, no originality claim.** This begins the user-approved return from Q′ to **Question Q**, following the referee's rank-one observation and subsequent addendum. The problem \(Q\) is **NOT solved**, but the first bounded test yields a new sufficient class directly using **finite stabilization** and the referee's infinite-chromatic linking graph, rather than a further geometric counterexample. The theorem concerns **arbitrary locales**, including pointless ones, and all rectangles are interpreted in the localic product.

## 0. The exact rank-one problem

Let L=O(X), \(Q=L\oplus L\) (here Q denotes the product frame, not the open problem label), and \(w_C=\bigvee_{c\in C}c\boxtimes c\). Define full and finite diagonal-neighborhood pre-nuclei:
\[
\Phi(q)=\bigvee_{\mathcal C\text{ cover}}(w_\mathcal C\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]
Put
\[
z_1=\Phi(0)=\Phi_2(0)=d_{\mathcal U},
\qquad \mathcal U=\mathfrak c_{X^2}(z_1).
\]
Question Q is exactly
\[
\boxed{\Phi_2(z_1)=z_1\Longrightarrow\Phi(z_1)=z_1.}
\tag{0.1}
\]
The hypothesis says \(\mathcal W_2=\mathcal U\), and the desired conclusion says \(\mathcal W=\mathcal U\).

We know by the rectangle basis of \(L\oplus L\) that \(\Phi(z_1)>z_1\) iff there is a cover C and pure rectangle \(r=a\boxtimes b\not\le z_1\) with \(r\wedge w_C\le z_1\), equivalently
\[
\boxed{(a\wedge c)\boxtimes(b\wedge c)\le z_1\qquad(\forall c\in C).}
\tag{0.2}
\]
Since \(\delta^*(z_1)=0\) and C covers, the local inequalities force \(a\wedge b=0\). Thus *disjoint* coordinate rectangles suffice throughout.

The initial referee's independent cross-link graph construction shows that any counterexample with finite stabilization must produce an **infinite-chromatic** graph on C, with edges between c,c′ when \(\mathcal U\) meets the cross rectangle \((a\wedge c)\boxtimes(b\wedge c')\) or its reversal.

## 1. Finite-box decomposition of a localic relation

Let \(T=\mathfrak c(d)\hookrightarrow X^2\) be ANY closed localic relation. For a rectangle \(r=a\boxtimes b\), put
\[
T[r]=T\wedge\mathfrak o(r).
\]
We say **\(T[r]\) has product-box rank ≤m** if it is the **join as a sublocale** of m product sublocales:
\[
\boxed{T[r]=\bigvee_{i=1}^{m}(S_i\times T_i),\quad
S_i\le\mathfrak o_X(a),\ T_i\le\mathfrak o_X(b),\quad
S_i\times T_i\le T[r].}
\tag{1.1}
\]
The factor sublocales need not be spatial, compact, regular or open. Product means their *localic* product, embedded into X² by the two inclusions. The empty sublocale has rank 0. We use the elementary facts:
(a) the sublocale lattice is distributive for **finite** joins and meets;
(b) pullback of a product sublocale by an open rectangle gives the product of the corresponding open restrictions; and
(c) over classical Set, the localic product of two nonzero locales is nonzero. **Point-free verification of (c):** The frame coproduct (L\oplus M) is the tensor product of the underlying sup-lattices. Define the SUP-lattice maps (\pi_L:L\to2), (\pi_M:M\to2) by (\pi_L(a)=1\) iff (a\ne0\), and similarly for M. They preserve arbitrary joins (but need NOT be frame maps). Their tensor gives a join-homomorphism (L\otimes M\to2\) sending the pure rectangle (a\boxtimes b\) to 1 exactly when both (a,b\ne0\). Hence nonzero coordinate opens yield a nonzero product, with **no ordinary points assumed**. This avoids invoking arbitrary pullback stability of locale surjections, which was not established here. The standard sup-lattice-tensor representation of frame coproducts is the only structural input to this verification.

## 2. Main finite-box colouring lemma

**Theorem 2.1 (finite-box rank bounds cross-link chromatic number).** Suppose \(T[r]\) has rank ≤m as in (1.1), and a cover C of X satisfies
\[
\boxed{T\wedge\mathfrak o((a\wedge c)\boxtimes(b\wedge c))=0\quad
\text{for each }c\in C.}
\tag{2.1}
\]
Then there exists a FINITE coarsening \(F=\{u_\tau:\tau\in\{0,1\}^m\}\) of C, with **at most \(2^m\) nonempty members**, satisfying
\[
\boxed{T\wedge\mathfrak o(r\wedge w_F)=0,\qquad
r\wedge w_F\le d.}
\tag{2.2}
\]
Equivalently the cross-link graph \(G_C(a,b;T)\) has a proper vertex colouring with at most \(2^m\) colours.

*Proof.* For each i and each c∈C, define a bit
\[
\epsilon_i(c)=
\begin{cases}
1 & S_i\wedge\mathfrak o(c)\ne0,\\
0 & S_i\wedge\mathfrak o(c)=0.
\end{cases}
\tag{2.3}
\]
If \(\epsilon_i(c)=1\), then \(T_i\wedge\mathfrak o(c)=0\): otherwise their product is nonzero and lies inside the prohibited same-member restriction (2.1). Thus for every c and i, at least one of the two coordinate restrictions vanishes.

Partition C according to \(\epsilon(c)\in2^m\); define \(u_\tau=\bigvee_{\epsilon(c)=\tau}c\). Empty colour classes may be dropped. These u form a FINITE cover because C covers. For each i and each τ:
- if τ_i=0, \(S_i\wedge\mathfrak o(u_\tau)=0\), because every member of the class misses S_i;
- if τ_i=1, \(T_i\wedge\mathfrak o(u_\tau)=0\), because every member misses T_i.

Therefore
\[
(S_i\times T_i)\wedge\mathfrak o(u_\tau\boxtimes u_\tau)=0
\]
for every i,τ. By finite distributivity and (1.1),
\(T[r]\wedge\mathfrak o(w_F)=0\), proving (2.2). The same partition is a proper colouring: if a cross-link c–c′ occurs, finite decomposition (1.1) shows an i with S_i meeting c and T_i meeting c′ (or reversed), so their ith colour bits differ. □

**Graph-theoretic sharpness.** Each product box contributes a (possibly empty) complete bipartite subgraph between cover members meeting its left and right factors; the no-loop hypothesis makes those vertex classes disjoint. Therefore the cross-link graph is a union of at most m bicliques and admits the above m-bit colouring. The numerical bound \(2^m\) cannot be improved **solely from this abstract biclique-union hypothesis**: on the vertices \(2^m\), take the m bipartite cut graphs separating bit 0 from bit 1 in each coordinate. Their union is the complete graph \(K_{2^m}\), whose chromatic number is \(2^m\). This does NOT assert that every such abstract graph is realizable as a Urysohn cross-link graph of a locale.

**Remark (scope of product positivity).** This is a proof in the sublocale lattice rather than an argument from ordinary pairs. In particular "not locally linked" is tested by the *actual nonzero localic product*, not only by spatial points.

**Corollary 2.2A (ONE-step finite simulation; no stabilization assumed).** For ANY closed T=C(d), ANY locale X, ANY rectangle r with finite product-box rank T[r], and ANY arbitrary cover C,
\[
\boxed{r\wedge w_C\le d\quad\Longrightarrow\quad
r\le\Phi_2(d).}
\tag{2.4a}
\]
Indeed the finite coarsening F from Theorem 2.1 gives \(r\le w_F\to d\le\Phi_2(d)\). **This is an exact partial positive answer to the referee's UNRESTRICTED rank-one test**, with d=z₁: \(r\le\Phi_2(z_1)\le d_0\). No hypothesis \(\Phi_2(z_1)=z_1\) is required.

**Corollary 2.2 (finite-fixed closed relations cannot have holes on finite-box patches).** If \(d\) is **finite-cover fixed**, i.e. \(\Phi_2(d)=d\), and a rectangle r is such that T[r] has finite box rank, then for EVERY arbitrary X-cover C,
\[
\boxed{r\wedge w_C\le d\quad\Longrightarrow\quad r\le d.}
\tag{2.4}
\]
*Proof.* By Theorem 2.1 coarsen C to a finite F with \(r\wedge w_F\le d\). Hence \(r\le w_F\to d\le\Phi_2(d)=d\). □

This is a strictly local condition: it makes no claim about \(T\) outside the chosen rectangle.

## 3. A new positive class for Q localized to the nonregular Urysohn boundary

Let
\[
G=\mathcal U\wedge\mathfrak o(z_1^{**}),
\qquad
K_{\rm reg}=\operatorname{cl}(\operatorname{int}\mathcal U)=\mathfrak c(z_1^{**}).
\tag{3.1}
\]
The previously established universal regular-core theorem says
\(K_{\rm reg}\le\mathcal W\le\mathcal W_2\le\mathcal U\).

Call \(r=a\boxtimes b\le z_1^{**}\) a **finite-box patch in G** if \(\mathcal U[r]\ne0\) and \(\mathcal U[r]\) admits a finite product-box decomposition as (1.1). (It is already a relatively open sublocale of G.)

**Theorem 3.1 (locally finite-box residual criterion, NEW INTERNAL).** Suppose the join of all finite-box patches in G is **dense in G** (equivalently every nonzero relatively open sublocale of G contains a nonzero finite-box rectangular patch). Then
\[
\boxed{\mathcal W_2=\mathcal U\quad\Longrightarrow\quad\mathcal W=\mathcal U.}
\tag{3.2}
\]
In other words, **Question Q holds for every locale with such a locally finite-product decomposable nonregular Urysohn boundary.**

*Proof.* Assume \(\Phi_2(z_1)=z_1\), but \(\Phi(z_1)>z_1\). Choose C with nonzero regular-open hole
\[
E=\mathcal U\wedge\mathfrak o(\rho_C),\qquad\rho_C=w_C\to z_1.
\]
The inclusion \(K_{\rm reg}\le\mathcal W\) and the fact that E is disjoint from \(\mathcal W\) imply \(0\ne E\le G\). By density of finite-box patches in G, E meets a finite-box patch \(\mathcal U[r_0]\) nontrivially. Because their intersection is relatively open in U and rectangles join-generate Q, there is a pure rectangle \(r'=a'\boxtimes b'\le r_0\wedge\rho_C\) with \(\mathcal U[r']\ne0\). Restrict the finite product decomposition of \(\mathcal U[r_0]\) to this rectangle: each box remains a product of open restrictions, so \(\mathcal U[r']\) has finite box rank. We have \(r'\wedge w_C\le z_1\) and \(r'\not\le z_1\). Corollary 2.2 contradicts finite stabilization at z₁. □

**What this covers and what it does NOT.** When G=0 (U regular closed), it recovers the old regular-core positive mechanism. When G contains a dense family of *genuine finite product regions*—even products of nonspatial or atomless sublocales—the new finite-box argument supplies a different positive mechanism. This hypothesis is NOT claimed necessary, nor is it shown to subsume the earlier atomic-Boolean criterion. A Hausdorff perfect space has \(G=\Delta\) and need not possess finite-box diagonal patches although W=U; thus the criterion should be regarded as a useful **new sufficient class** rather than an approximate characterization of Q.

### 3.2 Unrestricted one-stage implication under a STRONGER rectangular hypothesis

The **unconditional stage-one simulation** in Corollary 2.2A gives a separate sufficient condition for
\[
\Phi(z_1)=\Phi_2(z_1).
\]
It suffices that **EVERY nonzero rectangular restriction** \(\mathcal U[r]\), \(r=a\boxtimes b\), have finite product-box rank. Indeed, for any cover C and rectangle \(r\le w_C\to z_1\), the finite simulation directly gives \(r\le\Phi_2(z_1)\). Rectangles join-generate \(Q\), so \(\Phi(z_1)\le\Phi_2(z_1)\); the reverse inclusion is automatic.

**IMPORTANT ADVERSARIAL CORRECTION:** A previous version of this section claimed that DENSITY of finite-box open patches in the whole U sufficed for \(\Phi(z_1)=\Phi_2(z_1)\). That proof was WRONG: for a strict difference, the nonzero sublocale
\[
\mathfrak c(\Phi_2(z_1))\wedge\mathfrak o(r)
\]
is relatively open in the CLOSED locale \(\mathfrak c(\Phi_2(z_1))\), **not** necessarily relatively open in U. It may be nowhere dense in U, so dense finite-box patches of U can MISS it. We withdraw the density-based general one-stage claim. Theorem 3.1 on **Question Q** is UNAFFECTED because under \(\Phi_2(z_1)=z_1\), its canonical hole E is indeed a nonzero relatively OPEN sublocale of U. Corollary 2.2A and the stronger **all-rectangle** statement above remain valid.

### 3.3 Rank-zero local far-separation is not the hard part

A small comparison helps locate the exact new difficulty. Suppose a,b∈L and C is an arbitrary cover such that **each** pair \((a\wedge c,b\wedge c)\) is itself far, i.e.
\[
(a\wedge c)^*\vee(b\wedge c)^*=1\qquad(c\in C).
\]
**One must NOT use the false Heyting identity** \((a\wedge c)^*=a^*\vee c^*\) (it fails for ordinary topological opens). Instead, relative pseudocomplementation in the principal ideal \(\downarrow c\) gives the VALID identities \(c\wedge(a\wedge c)^*=c\wedge a^*\) and \(c\wedge(b\wedge c)^*=c\wedge b^*\). Meeting the assumed local far equality with c gives \(c=c\wedge(a^*\vee b^*)\), so \(c\le a^*\vee b^*\). Since C covers 1, \(a^*\vee b^*=1\), and (a,b) is itself far. This *local-to-global gluing for individual far pairs* needs no finite-stabilization hypothesis. Rank one is hard precisely because the LOCAL rectangles need only lie below the **JOIN** \(z_1\) of far rectangles; they need not themselves be far.

For a topological picture of this distinction, on the ordinary real line the product of the disjoint opens (0,1) and (1,2) lies in the far-relation open \(z_1\) (U=diagonal), although the closures of the two entire opens meet at 1. This is an illustration, not a Q counterexample.

## 4. Rank-one obstruction sharpened

**Corollary 4.1 (infinite rectangular complexity in every genuine Q-hole).** Under \(\Phi_2(z_1)=z_1\), if \(\Phi(z_1)>z_1\) and \(E_C=\mathcal U\wedge\mathfrak o(w_C\to z_1)\ne0\), then
\[
\boxed{\text{NO nonzero relatively open sublocale of }E_C
\text{ is a finite product-box join.}}
\tag{4.1}
\]
More precisely, for every rectangle \(r\le w_C\to z_1\) with \(\mathcal U[r]\ne0\), the product-box rank of \(\mathcal U[r]\) is infinite (cannot equal any finite m). Otherwise apply Corollary 2.2 to r.

This constraint complements, rather than replaces, the referee's **infinite-chromatic cross-link graph** and nowhere-distributivity constraints. In a bad cover, finite rank m gives an explicit 2^m-colouring; a genuine Q-hole cannot have finite product-box rank at any of its nonzero rectangular open patches.

**Proposition 4.2 (locally hereditary infinite chromaticity of a rank-one hole).** Under the assumptions of Corollary 4.1, keep the SAME bad cover C and canonical open hole E_C. For **every** nonzero relatively open sublocale V⊆E_C, one can choose a pure rectangle \(r_V=a_V\boxtimes b_V\le w_C\to z_1\) with
\[
0\ne\mathcal U[r_V]\le V,\qquad a_V\wedge b_V=0,
\]
such that the associated cross-link graph on the members of the **same C** has infinite chromatic number, and this remains true for every refinement of C.

*Proof.* Because E_C is a relatively open U-sublocale, V=U∧O(q) for an ambient open q≤w_C→z₁ (taking q to represent the relative open). Choose a rectangle \(r_V\le q\) with U[r_V]≠0. The cover condition \(r_V\wedge w_C\le z_1\) implies disjoint coordinate opens, by applying the diagonal frame map and joining over C. If the cross-link graph admitted a finite coloring, joining colour classes would give a finite cover F with \(r_V\wedge w_F\le z_1\), hence \(r_V\le\Phi_2(z_1)=z_1\), contradicting the nonzero U restriction. The same cover condition persists under every refinement of C. □

Thus a hypothetical **rank-one hole must carry unbounded finite chromatic complexity in EVERY nonzero relatively open part**, for the SAME fixed cover, not only for the original rectangle as a whole. This is a precise local/combinatorial analogue of the referee's closed-support “self-similarity,” and is still only a necessary condition.

**Generalization:** Theorem 2.1 and Corollary 2.2 are true with \(\mathcal U\) replaced by ANY closed T=C(d) with \(\Phi_2(d)=d\). Thus the same finite-box exclusion applies to Q′ holes in W₂. What is specifically rank-one is the localization to the **nonregular Urysohn boundary** G and the equivalence with Question Q.

### 4.2 Atomless finite-box control (no false equivalence with atomicity)

Let Y denote the **compact two-apex** control from our October W/U phase, whose nonregular U boundary contains the two opposite apex pairs and for which \(W_2(Y)=W(Y)<U(Y)\). Let S be the **completed branching algebraic Scott dcpo** of nonempty finite/infinite binary partial functions. Then \(\mathcal U(S)=S^2\) via dense common-predecessor pairs, but the Booleanization of \(S^2\) is **atomless**: every nonzero basic Scott rectangle contains disjoint nonzero subrectangles obtained by splitting a fresh binary coordinate in one factor.

For the locally compact sober product \(X=Y\times S\), the previously internally proved dense-common-predecessor transfer says \(U(X)=U(Y)\times S^2\) and \(W_2(X)=W_2(Y)\times S^2<U(X)\). The nonregular off-diagonal apex boundary pieces in U(X) are of the form
\[
(\{p\}\times S)\times(\{q\}\times S)
\quad\text{and their transposes},
\]
**single product sublocales**, despite having atomless Booleanizations. This shows that “finite product-box rank” is NOT equivalent to atomic Booleanization. It is compatible with substantial pointless Boolean complexity. Finite stabilization fails in this control, so there is no contradiction with Theorem 3.1.

**Status of control:** Relies on the earlier working compact two-apex boundary computation and the internal product-transfer lemma; those example computations were not re-audited as part of this rank-one proof. The rank-one box-colouring theorem itself is independent of the control.

## 5. Why this is not an answer to Q

1. The proof requires the existence of finite product-box *sublocales* inside the Urysohn relation. No argument shows that their relatively open pieces are dense in G for arbitrary L. In particular, \(G=\Delta\) in many Hausdorff non-discrete locales, where such a density assertion may fail.
2. Infinite chromatic number is a NECESSARY property of a bad cover, but high chromatic number by itself does not construct a cover, a linked rectangle, or a point-free density defect.
3. The new criterion is independent of the earlier **Boolean distributivity** sufficient condition in form; whether it yields strictly new concrete examples needs testing.
4. The predecessor *rank-zero* statement \(\Phi(0)=\Phi_2(0)\) is NOT being used as a hidden blanket compactness principle. Only the **finite fixedness of d=z₁** and the explicitly described finite product-box regions enter.
5. The only new claim here is the **finite-box colouring theorem and its rank-one local application**, which require external scrutiny especially concerning nonzero products of arbitrary sublocales and the sublocale join/restriction step. No universal conclusion about Q is asserted.

## 6. Follow-up discipline

This bounded rank-one segment has a definite outcome (with the explicit §3.2 withdrawn-claim warning): the referee's infinite-chromatic obstruction can be turned into an explicit finite-cover construction whenever the linked relation has locally finite product-box rank. It removes an entire class of prospective rank-one holes and gives a positive theorem for G with a dense finite-box patch family. The next step should be a **deliberate counter-control**: test whether a truly nonregular Urysohn boundary can have atomless finite-box patches while \(\mathcal W_2<\mathcal U\), and distinguish local rank from atomicity; alternatively attack a rank-one hole with provably **infinite** box rank, rather than another generic forcing gadget.

**STATUS: INTERNAL WORKING PROOF, NOT INDEPENDENTLY AUDITED. UNIVERSAL Q/Q′ OPEN.**
