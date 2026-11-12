# Project A — Point-free products: universal Urysohn and inseparability formulas, compact-fiber closed-hull transfer

**12 November 2026. New internally derived results, not independently audited or checked for priority in the literature.** Continuation of [spatial-base fiberwise transfer](ProjectA_Q_SEPARATED_SPATIAL_FACTOR_FIBERWISE_CLOSED_HULL_TRANSFER_2026-11-12.md). The user asked to **remove the spatiality assumption on the separated base**. The answer splits sharply:

- **Complete success for \(\mathcal U\)**: \(\boxed{\mathcal U(Z\times Y)=\mathcal U(Z)\times\mathcal U(Y)}\) for ALL locales Z,Y in classical Set, POINTLESS included. Similarly \(\mathcal I\) commutes with all binary products.
- **Positive point-free transfer for both closed fitted-diagonal hulls when the fiber Y is COMPACT:** a cover of \(Z\times Y\) is locally on Z refinable by a FINITE family of rectangles whose Y-components cover Y, using the proper-projection/tube lemma, with NO base point required.
- **Stronger gluing:** the compact assumption extends to a fiber with an open cover by COMPACT CLOPEN sublocales. If \(\mathcal W_2(Z)=\mathcal I(Z)\), then
\[
\boxed{\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)=\mathcal I(Z)\times\mathcal W(Y)}
\]
for every such Y, with Z allowed to be entirely POINTLESS. In particular the Q′ equality holds on these products.
- **Precise remaining gap:** for a noncompact fiber whose closed hull \(\mathcal W(Y)\) has genuine nonspatial/pointless density and has no compact clopen local decomposition, the tube step can fail; no universal pointfree formula for \(\mathcal W,\mathcal W_2\) is claimed here. Universal Q and Q′ remain OPEN.

Throughout, products of sublocales are actual localic products embedded in the appropriate product locale, not point-set products. The assertions use ordinary classical set theory, under which any product of two NONZERO locales is nonzero. This positivity also follows from the sup-lattice tensor presentation of frame coproducts.

## 0. Elementary positivity and product closure lemmas

**Lemma 0.1 (nonzero product rectangles).** For any locales Z,Y and opens \(a\in O(Z),b\in O(Y)\),
\[
a\boxtimes b=0\iff a=0\text{ or }b=0.
\tag{0.1}
\]
*Proof.* The underlying sup-lattice of the frame coproduct is the sup-lattice tensor product; the Boolean-valued positivity maps \(a\mapsto[a\ne0]\) from the respective underlying sup-lattices to 2 preserve arbitrary joins (in classical Set). Their tensor takes \(a\boxtimes b\) to 1 whenever both factors are nonzero. The other direction is trivial. Equivalent topological-language formulation: a product of two nonzero locales is nonzero. □

**Lemma 0.2 (pseudocomplement of a product rectangle).**
\[
\boxed{(a\boxtimes b)^*=(a^*\boxtimes1)\vee(1\boxtimes b^*).}
\tag{0.2}
\]
*Proof.* The right side is disjoint from \(a\boxtimes b\). Conversely any rectangle \(u\boxtimes v\) disjoint from \(a\boxtimes b\) has \((u\wedge a)\boxtimes(v\wedge b)=0\), so by Lemma 0.1 either \(u\le a^*\) or \(v\le b^*\). Thus every rectangle below the pseudocomplement lies below the displayed right side; rectangles join-generate the product frame. □

**Lemma 0.3 (a union of two coordinate strips covers only if one does).** For \(s\in O(Z),t\in O(Y)\),
\[
\boxed{(s\boxtimes1)\vee(1\boxtimes t)=1\ \Longrightarrow\ s=1\text{ or }t=1.}
\tag{0.3}
\]
*Proof.* If both are proper, the closed sublocales \(\mathfrak c_Z(s)\), \(\mathfrak c_Y(t)\) are nonzero. Their nonzero localic product lies in the closed complement of the union, contradiction. □

**Lemma 0.4 (closure commutes with products in classical Loc).** For ANY sublocales A⊆Z and B⊆Y,
\[
\boxed{\operatorname{cl}_{Z\times Y}(A\times B)=\operatorname{cl}_Z(A)\times\operatorname{cl}_Y(B).}
\tag{0.4}
\]
*Proof.* The right side is a CLOSED product sublocale containing A×B, giving ≤. Conversely A is dense in cl A and B dense in cl B. Every nonzero elementary relatively open rectangle of cl A×cl B has nonzero intersections with A and B, whose localic product is nonzero by Lemma 0.1. Thus A×B is dense in cl A×cl B, proving ≥. □

## 1. Universal Urysohn and inseparability product formulas — no spatiality, no compactness

For a locale T write
\[
d_{\mathcal U(T)}
=\bigvee\{a\boxtimes b:a^*\vee b^*=1_T\},\qquad
\mathcal U(T)=\mathfrak c_{T^2}(d_{\mathcal U(T)}).
\tag{1.1}
\]

**Theorem 1.1 (UNIVERSAL localic Urysohn product formula).**
For ANY locales Z,Y:
\[
\boxed{\mathcal U(Z\times Y)=\mathcal U(Z)\times\mathcal U(Y).}
\tag{1.2}
\]

*Proof.* By naturality of U under product projections,
\[
\mathcal U(Z\times Y)\le\mathcal U(Z)\times\mathcal U(Y).
\]
For the reverse, let \(A,B\in O(Z\times Y)\) be any FAR pair, \(A^*\vee B^*=1\). Expand A and B as joins of elementary rectangles,
\[
A=\bigvee_i(u_i\boxtimes a_i),\qquad
B=\bigvee_j(v_j\boxtimes b_j).
\]
For each i,j, since \(u_i\boxtimes a_i\le A\) and \(v_j\boxtimes b_j\le B\),
\[
1=A^*\vee B^*\le
(u_i\boxtimes a_i)^*\vee(v_j\boxtimes b_j)^*.
\]
By (0.2), the right side is
\[
\bigl((u_i^*\vee v_j^*)\boxtimes1_Y\bigr)
\vee\bigl(1_Z\boxtimes(a_i^*\vee b_j^*)\bigr).
\]
Lemma 0.3 implies EITHER \(u_i^*\vee v_j^*=1_Z\) OR \(a_i^*\vee b_j^*=1_Y\). Thus the X²-rectangle
\[
(u_i\boxtimes a_i)\boxtimes(v_j\boxtimes b_j)
\]
lies in the complement-defining open \(d_{\mathcal U(Z)}\boxtimes1_{Y^2}\vee1_{Z^2}\boxtimes d_{\mathcal U(Y)}\) of the CLOSED product \(\mathcal U(Z)\times\mathcal U(Y)\). Joining over all i,j shows the whole FAR rectangle \(A\boxtimes B\) lies in that open. Joining over all X-far A,B gives
\[
d_{\mathcal U(Z\times Y)}\le
d_{\mathcal U(Z)}\boxtimes1\vee1\boxtimes d_{\mathcal U(Y)},
\]
and therefore \(\mathcal U(Z)\times\mathcal U(Y)\le\mathcal U(Z\times Y)\). □

**Corollary 1.2 (UNIVERSAL inseparability product formula).** Since the diagonal of a product is the product of the diagonals, Lemma 0.4 gives
\[
\boxed{\mathcal I(Z\times Y)=\mathcal I(Z)\times\mathcal I(Y).}
\tag{1.3}
\]
No spatiality or compactness assumptions are needed.

**Consequence:** The earlier spatial-base product formula for U was unnecessarily restrictive. If \(\mathcal U(Z)=\Delta_Z\), then \(\mathcal U(Z\times Y)=\Delta_Z\times\mathcal U(Y)\) for every potentially POINTLESS fiber Y, and likewise if \(\mathcal I(Z)=\mathcal U(Z)\), the U relation is \(\mathcal I(Z)\times\mathcal U(Y)\).

## 2. The localic compact-fiber tube-cover identity

Let Y be COMPACT (not assumed spatial), Z arbitrary, and take any rectangle cover of \(Z\times Y\):
\[
\bigvee_{i\in I}u_i\boxtimes v_i=1_{O(Z\times Y)}.
\]
Then
\[
\boxed{
1_Z=
\bigvee_{\substack{F\subseteq I\text{ finite}\\\bigvee_{i\in F}v_i=1_Y}}
\bigwedge_{i\in F}u_i.
}
\tag{2.1}
\]

**Proof of the tube identity, with the pointfree compactness input exposed.** Write \(\pi:Z\times Y\to Z\). Compactness of Y makes this projection a PROPER locale map: the right adjoint \(\pi_*:O(Z\times Y)\to O(Z)\) preserves DIRECTED joins and satisfies base change along arbitrary maps (Beck–Chevalley for proper maps). For a FINITE set \(F\subseteq I\), the finite-rectangle calculation reads
\[
\boxed{
\pi_*\Bigl(\bigvee_{i\in F}u_i\boxtimes v_i\Bigr)
=
\bigvee_{\substack{J\subseteq F\\\bigvee_{j\in J}v_j=1_Y}}
\bigwedge_{j\in J}u_j.
}
\tag{2.2}
\]
To verify this without points of Z, take the FINITE DISTRIBUTIVE SUBFRAME of O(Z) generated by the finitely many \(u_i\)'s. It corresponds to a finite sober Alexandrov locale P with a locale map \(Z\to P\). In \(P\times Y\), a finite monotone section family has \(\pi_*\)-value the P-open set of p whose Y-section is top. Here that section is \(\bigvee_{i:p\in u_i}v_i\); the finite formula on the right is the same P-open, tested at each p. Proper base change pulls this finite equality back along \(Z\to P\).

Now the finite partial rectangle sums form a DIRECTED family with join 1_{Z×Y}. Apply the directed-join preservation of \(\pi_*\) and (2.2):
\[
1_Z=\pi_*(1)=\bigvee_{F\text{ finite}}\pi_*\left(\bigvee_{i\in F}u_i\boxtimes v_i\right)
=\bigvee_{\substack{J\subseteq I\text{ finite}\\\bigvee_{j\in J}v_j=1_Y}}
\bigwedge_{j\in J}u_j.
\]
This proves (2.1). No ordinary point of either locale is chosen. □

**Why compactness matters for this route.** If Y is noncompact and \(\{v_i\}\) is a Y-cover without a finite subcover, then \(\{1_Z\boxtimes v_i\}\) covers \(Z\times Y\) but the right side of (2.1) is 0_Z. Thus the tube identity itself cannot extend to arbitrary noncompact Y; this does NOT establish failure of the desired W transfer in any particular noncompact case.

## 3. Full fitted-diagonal inclusion over an ARBITRARY base with compact fiber

Let \(X=Z\times Y\) with Y compact. Identify the fiber-diagonal locale \(Z\times Y^2\) with \(\Delta_Z\times Y^2\subseteq X^2\).

**Theorem 3.1 (pointfree fiber-diagonal fitting).**
\[
\boxed{\Delta_Z\times\mathcal D(Y)\le\mathcal D(Z\times Y).}
\tag{3.1}
\]

*Proof.* Let C be ANY open cover of X. Refine it by ALL elementary rectangles \(u_i\boxtimes v_i\le c_i\in C\), a rectangle cover of X. For any finite F appearing in the tube cover (2.1), \(\{v_i:i\in F\}\) is a FINITE cover of Y, and \(\mathcal D(Y)\le O(w_{\{v_i:i\in F\}}^Y)\). Therefore over the base open \(b_F=\bigwedge_{i\in F}u_i\), the pair of coordinates \((z,y_1),(z,y_2)\) with \((y_1,y_2)\in\mathcal D(Y)\) satisfies one of the diagonal square rectangles from the refined C:
\[
b_F\times\mathcal D(Y)
\le
\bigvee_{i\in F} O_{Z\times\mathcal D(Y)}
\bigl(u_i\boxtimes(v_i\boxtimes v_i)\bigr).
\]
By (2.1), the \(b_F\)'s cover Z. Hence the restriction of the FULL X diagonal square \(w_C^X\) to \(Z\times\mathcal D(Y)\) is top. Since C was arbitrary, (3.1) follows. The proof is at the level of ACTUAL sublocales and their frame maps, and makes no assumption that \(\mathcal D(Y)\) has enough points. □

**Corollary 3.2 (unconditional compact-fiber sandwich).** For arbitrary Z, compact Y, by (0.4) and \(\mathcal D(Y)=\mathcal D_2(Y)\),
\[
\boxed{
\mathcal I(Z)\times\mathcal W(Y)
\le\mathcal W(Z\times Y)
\le\mathcal W_2(Z\times Y)
\le\mathcal W_2(Z)\times\mathcal W(Y).
}
\tag{3.2}
\]
For W separately the stronger upper bound \(\mathcal W(Z)\times\mathcal W(Y)\) is also available.

**Theorem 3.3 (EXACT closed-hull transfer over pointfree W₂=I bases).** If Z satisfies
\[
\boxed{\mathcal W_2(Z)=\mathcal I(Z)}
\tag{3.3}
\]
and Y is compact, then
\[
\boxed{
\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\mathcal I(Z)\times\mathcal W(Y).
}
\tag{3.4}
\]
There is NO spatiality requirement on Z or Y.

In particular:
- If \(\mathcal U(Z)=\Delta_Z\), then \(\mathcal I(Z)=\Delta_Z\) and the product closed hulls are \(\Delta_Z\times\mathcal W(Y)\).
- If \(\mathcal I(Z)=\mathcal U(Z)\), then \(\mathcal W_2(Z)=\mathcal I(Z)\), so (3.4) holds with the potentially NONDIAGONAL relation \(\mathcal I(Z)\).
- For nonzero separated Z, the gap \(\mathcal W(Y)<\mathcal U(Y)\) transfers STRICTLY to \(\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)<\mathcal U(Z\times Y)\), even if Z has NO points.

This is a substantive removal of the base spatiality hypothesis from the preceding product theorem, but it uses compactness of Y.

## 4. Beyond compactness: compact CLOPEN fiber covers

Assume the fiber Y has an open cover \(\{e_i:i\in I\}\) by COMPLEMENTED opens, with each clopen sublocale \(Y_i=O_Y(e_i)\) compact. No assumption of finitely many charts or an actual disjoint partition is made.

**Lemma 4.1 (clopen squares cover the Urysohn relation).**
\[
\boxed{\mathcal U(Y)\le O_{Y^2}\left(\bigvee_i e_i\boxtimes e_i\right).}
\tag{4.1}
\]
*Proof.* On the coordinate frame maps \(h,k:O(Y)\to O(\mathcal U(Y))\), any complemented e obeys h(e)=k(e): the off-diagonal mixed rectangles \(e\boxtimes e^*,e^*\boxtimes e\) are FAR, hence disjoint from U. Since \(h(e_i)=k(e_i)\) and \(\bigvee_ie_i=1_Y\),
\[
\bigvee_i h(e_i)\wedge k(e_i)=\bigvee_i h(e_i)=1.
\]
This is exactly (4.1). It does NOT assume that U itself is a finite-cover-compatible pair. □

**Theorem 4.2 (clopen-compact-fiber transfer).** If \(\mathcal W_2(Z)=\mathcal I(Z)\) and Y has a compact clopen open cover, then
\[
\boxed{
\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\mathcal I(Z)\times\mathcal W(Y),
\qquad
\mathcal U(Z\times Y)=\mathcal U(Z)\times\mathcal U(Y).
}
\tag{4.2}
\]

*Proof.* Let \(X=Z\times Y\) and \(J_i=Z\times Y_i\), a CLOPEN sublocale of X. The externally reviewed **closed heredity** for Dε and the elementary fact that closure commutes with OPEN restriction give
\[
\mathcal W_\epsilon(X)\wedge J_i^2=\mathcal W_\epsilon(J_i),\qquad
\mathcal W(Y)\wedge Y_i^2=\mathcal W(Y_i).
\]
By Theorem 3.3 on each COMPACT Y_i,
\[
\mathcal W_\epsilon(J_i)=\mathcal I(Z)\times\mathcal W(Y_i)
=(\mathcal I(Z)\times\mathcal W(Y))\wedge J_i^2.
\]
Thus the desired equality holds on every clopen chart square \(J_i^2\).

All of \(\mathcal W(X),\mathcal W_2(X)\) and the candidate \(\mathcal I(Z)\times\mathcal W(Y)\) lie below the CLOSED sublocale \(\mathcal U(X)=\mathcal U(Z)\times\mathcal U(Y)\). By Lemma 4.1, the open chart squares \(J_i^2\) COVER that Urysohn relation. A CLOSED sublocale supported inside a union of OPEN chart squares is uniquely determined by its restrictions to those charts (this is just the frame distributivity argument for its complementary open). Therefore the local equalities glue and prove (4.2). □

**Additional stronger fact for Y alone.** The same finite-cover patching argument using compact clopen pieces yields \(\boxed{\mathcal D(Y)=\mathcal D_2(Y)}\), even when Y is NONCOMPACT. Given any cover C, compactness of each Y_i gives a finite F_i⊂C with \(e_i\le\bigvee F_i\). Finite compatibility with \(\{e_i^*\}\cup F_i\), multiplied by the common h(e_i)=k(e_i), forces full C compatibility after joining e_i over all i. This is the older clopen patching theorem in concrete form.

**Rank-one consequence when \(\mathcal I(Z)=\mathcal U(Z)\).** With Z nonzero and I(Z)=U(Z), we obtain
\[
\boxed{
\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)=\mathcal I(Z)\times\mathcal W(Y),
\quad
\mathcal U(Z\times Y)=\mathcal I(Z)\times\mathcal U(Y).
}
\tag{4.3}
\]
Hence W=U on the product iff W(Y)=U(Y), and Q,Q′ hold automatically for the product (the two W hulls agree). The class I=U need not be spatial, separated or regular.

## 5. A SECOND route for NONCOMPACT fibers: dense common-predecessor point-pairs

Compactness is not the only possible substitute for spatiality of the BASE. In fact, if the **fiber's closed hull** is densely generated by ordinary common-specialization-predecessor pairs, we may use whole-Z constant-pair maps instead of z-point slices, even when Z has NO points.

Let \(\mathrm{Cm}(Y)\subseteq\operatorname{pt}(Y)^2\) denote the ordinary point-pairs \((y_1,y_2)\) possessing an ordinary common specialization predecessor \(p\le y_1,y_2\). Write “\(\mathrm{Cm}(Y)\) is dense in \(\mathcal W_2(Y)\)” in the STRONG/SPATIAL sense that **every nonzero relatively open sublocale of \(\mathcal W_2(Y)\) contains some ordinary pair in \(\mathrm{Cm}(Y)\)**. This is not just a statement about its point-set shadow.

**Lemma 5.1 (common-predecessor constant pairs preserve ALL diagonal covers over an arbitrary base).** For any locale Z and any such ordinary pair \(y_1,y_2\in Y\), the locale map
\[
f_{y_1,y_2}: Z\longrightarrow(Z\times Y)^2,\quad z\longmapsto((z,y_1),(z,y_2))
\]
factors through \(\mathcal D(Z\times Y)\).

*Proof.* Let C be ANY cover of Z×Y. For an ordinary point p≤y_1,y_2, the p-slices \(\{c_p:c\in C\}\) cover Z and satisfy \(c_p\le c_{y_1},c_{y_2}\) for every c by specialization monotonicity of opens. Thus
\[
\bigvee_{c\in C} c_{y_1}\wedge c_{y_2}
\ \ge\ \bigvee_{c\in C}c_p=1_Z.
\]
This is the pullback of \(w_C\) along f, so f factors through every full diagonal-square open; no base point was chosen. □

**Theorem 5.2 (noncompact point-dense fiber transfer over arbitrary pointfree base).** Suppose \(\mathcal W_2(Z)=\mathcal I(Z)\) and \(\mathrm{Cm}(Y)\) is dense in \(\mathcal W_2(Y)\) in the just-defined strong sense. Then
\[
\boxed{\mathcal W(Y)=\mathcal W_2(Y),\qquad
\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\mathcal I(Z)\times\mathcal W_2(Y).}
\tag{5.1}
\]
This conclusion has NO compactness, local compactness, or spatiality assumption on Z and NO compactness assumption on Y.

*Proof.* Each common-predecessor point pair belongs to D(Y), so its density in W₂(Y) forces W(Y)=W₂(Y). By Lemma 5.1, the image of \(f_{y_1,y_2}\) lies in D(Z×Y) for every such pair. Their union of images is DENSE in \(\Delta_Z\times\mathcal W_2(Y)\): any nonzero relatively open rectangle in the latter is \(a\times b\) with \(a\ne0_Z,b\ne0_{\mathcal W_2(Y)}\); choose a common-predecessor pair in b and restrict the constant-pair image of Z to a. Since \(\mathcal W(Z\times Y)\) is CLOSED and contains all these maps, it contains the closure
\[
\operatorname{cl}(\Delta_Z\times\mathcal W_2(Y))
=\mathcal I(Z)\times\mathcal W_2(Y)
\]
by Lemma 0.4. Naturality gives
\[
\mathcal W_2(Z\times Y)\le\mathcal W_2(Z)\times\mathcal W_2(Y)
=\mathcal I(Z)\times\mathcal W_2(Y).
\]
Everything sandwiches to equality. □

**Controls:** The completed nonempty-powerset Scott locale Y is NONCOMPACT and hyperconnected; the ordinary diagonal pair \((\omega,\omega)\) at its greatest specialization point \(\omega\) meets every nonzero basic product open, so \(\mathrm{Cm}(Y)\) is dense in \(Y^2=\mathcal W_2(Y)\). Theorem 5.2 computes both W hulls over a potentially POINTLESS base Z without compactness of Y. Similarly, finite coherent Alexandrov fibers and product-domain fibers with genuinely dense common-predecessor pairs fit the hypothesis. This theorem makes no claim for a fiber whose W₂ density is essentially POINTLESS rather than point-generated.

## 6. A genuinely POINTLESS control, and what remains open

Let \(B=\operatorname{RO}(2^\omega)\) be the COMPLETE atomless Boolean algebra of regular opens of Cantor space, regarded as a FRAME, and let Z be its locale. A completely prime filter in a complete Boolean algebra is principal at an atom; hence Z has **NO ordinary points**. Because its frame is Boolean, \(D(Z)=D_2(Z)=U(Z)=I(Z)=\Delta_Z\) (finite matching of complementary pairs already forces equal coordinates).

Take Y to be the previously checked **compact T₁ two-apex** locale, for which \(\mathcal W(Y)=\mathcal W_2(Y)<\mathcal U(Y)\). By Theorems 1.1 and 3.3,
\[
\boxed{
\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\Delta_Z\times\mathcal W(Y)
\ <\
\Delta_Z\times\mathcal U(Y)=\mathcal U(Z\times Y).
}
\tag{5.1}
\]
The product \(Z\times Y\) has **NO ordinary points** (a point would project to a point of Z), yet exhibits a nontrivial W= W₂ < U hierarchy. Strictness is reflected by multiplication with the nonzero locale Z: a nonzero relatively open U(Y)\W(Y) has nonzero product with Z. This is a real point-free stress test not covered by the earlier theorem whose BASE was spatial.

Likewise if Y is a NONCOMPACT clopen coproduct of compact two-apex locales, Theorem 4.2 gives the same strict U/W gap over the pointless Boolean base, with the additional fiber now noncompact.

**Limit of current argument.** The tube identity (2.1) fails for an arbitrary noncompact fiber: the rectangle cover \(\{1_Z\boxtimes v_i\}\) built from any Y-cover without finite subcover is a counterexample to the identity. This is only a failure of the present *compact-fiber proof mechanism*, NOT a counterexample to an unrestricted W transfer formula. In fact, the earlier spatial-base theorem works with every Y, compact or not, and Theorem 5.2 above covers certain genuinely NONCOMPACT fibers even over POINTLESS bases. The difficult residual case is a POINTLESS separated base and a NONCOMPACT fiber whose W₂ density cannot be recovered from compact clopen pieces or ordinary common-specialization-predecessor pairs.

**Decision for Question Q.** We have now removed spatiality completely for U and I, and for the W/W₂ closed hulls with compact/clopen-compact fibers. This produces genuinely pointless positive and strict-gap examples and a useful new product-transfer theorem. However it gives NO general implication \(\Phi_2(d_{\mathcal U})=d_{\mathcal U}\Rightarrow\Phi(d_{\mathcal U})=d_{\mathcal U}\) for an arbitrary locale. Neither Q nor Q′ is settled universally.

**Status: internally proved, not independently externally audited or literature-priority checked.**
