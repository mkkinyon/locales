# Project A — Square saturation for locally compact Hausdorff compact-cloud systems

**11 November 2026. NEW working generalization, independently re-derived internally; NOT externally audited.** This extends the externally checked CO-01 theorem of the Cantor finite-support example. The referee suggested a Stone-space extension; the argument below gives a stronger locally compact Hausdorff version. The **strict** inequality \(A<A^2\) is not asserted for arbitrary systems, but it holds for an explicit broad product family. An independent blind audit of the new generality would be desirable before ledger promotion.

## 1. Hypotheses, construction, and statement

Let \(X\) be a locally compact Hausdorff (topological) space and \((K_n)_{n\ge1}\) nonempty, pairwise disjoint **compact** subsets. Put
\[
D=\bigcup_{n\ge1}K_n,\qquad V=X\setminus D.
\]
Assume:

- **(H1)** \(V\) is dense in \(X\);
- **(H2) eventual ubiquity:** for each nonempty open \(U\subseteq X\), there is \(N_U\) such that \(K_n\cap U\ne\varnothing\) for every \(n>N_U\).

For \(a\in\mathcal O(V)\), let
\[
\Theta(a)=\{n:\ \exists\text{ open }W\subseteq X,\ K_n\subseteq W,\ W\cap V\subseteq a\}.
\]
Call a cover \(\mathcal C\) of \(V\) **admissible** if \(\bigcup_{a\in\mathcal C}\Theta(a)=\mathbb N\). Set
\[
A=\bigwedge_{\mathcal C\ \mathrm{admissible}}
\mathfrak o\Big(\bigvee_{a\in\mathcal C} a_1\wedge a_2\Big)
\ \hookrightarrow V^2,\quad
Z=\bigwedge_{K\subseteq V,\ K\ \mathrm{compact}}\mathfrak o(V\setminus K).
\]
Here \(\mathfrak o\) denotes an open sublocale; \(a_i\) is the pullback of \(a\) to the \(i\)th coordinate, not an ordinary pointwise condition. Put \(R_\infty=\Delta_V\vee(Z\times Z)\).

Construct a topological space \(Y=V\sqcup\mathbb N\) by declaring its opens to be \(a\sqcup S\) with \(a\in\mathcal O(V)\), \(S\subseteq\Theta(a)\). Equivalently, neighborhoods of \(n\) include \(\{n\}\cup(W\cap V)\) whenever \(W\) is an X-open neighborhood of the **whole** \(K_n\). The subsets \(V\) and \(N=\mathbb N\) are respectively open and closed in \(Y\), with \(N\) a discrete subspace. The construction yields a Hausdorff space, since distinct compact subsets, and a compact subset and an external point, have disjoint open neighborhoods in a Hausdorff space. The fitted diagonal \(\mathcal D_Y\) restricts to \(A\) on \(V^2\) by the exact admissible-cover correspondence.

**Theorem (LCH compact-cloud saturation, working).**
\[
\boxed{\ A^2=R_\infty=\Delta_V\vee(Z\times Z),\qquad
R_\infty^2=R_\infty,\qquad R_\infty A=AR_\infty=R_\infty.\ }
\]
Every binary parenthesization of \(n\ge2\) copies of \(A\) equals \(R_\infty\). Furthermore
\[
\boxed{\
\mathcal D_Y=A\vee\Delta_N,\qquad
P_n(\mathcal D_Y)=R_\infty\vee\Delta_N\quad(n\ge2,\ \text{any bracketing}).
\ }
\]
The equalities do **not** assert \(A<A^2\) for all compact-cloud systems. We do have \(\Delta_V<A\), as explained in §6. Both \(Z\) and \(Z^2\) are nonzero; \(Z\) has no ordinary points.

## 2. Boundary recurrence without ultrafilters or zero-dimensionality

**Lemma 1 (relative boundary recurrence, for arbitrary frame targets).** Let \(B\) be any frame, and \(h:\mathcal O(V)\to B\) a frame morphism satisfying \(h(V\setminus K)=1\) for every compact subset \(K\subseteq V\). For every \(b>0\) in \(B\) and integer \(N\), there exist \(n>N\) and \(d\in K_n\) such that
\[
b\wedge h(W\cap V)>0\quad
\text{for EVERY X-open neighborhood }W\text{ of }d.
\tag{2.1}
\]

*Proof.* If false, choose for every \(d\in\bigcup_{n>N}K_n\) an open \(W_d\ni d\) such that \(b\wedge h(W_d\cap V)=0\). Set \(O=\bigcup_d W_d\). Preservation of joins gives \(b\wedge h(O\cap V)=0\).

Put \(F=\bigcup_{n\le N}K_n\). It is compact and closed, and disjoint from \(V\). Local compactness and regularity of \(X\) provide an open cover of \(V\) by relatively compact opens \(W\) such that \(\overline W\cap F=\varnothing\). Consequently some such \(W_0\) satisfies
\[
b'=b\wedge h(W_0\cap V)>0.
\]
The set \(K=\overline {W_0}\setminus O\) is compact and avoids both \(F\) and every \(K_n\) with \(n>N\); hence \(K\subseteq V\). Remoteness says \(h(V\setminus K)=1\). But
\[
V\setminus K=(V\setminus\overline {W_0})\cup (V\cap O)
\]
and \(b'\) meets the \(h\)-image of both terms in zero: the first because \(b'\le h(W_0\cap V)\), the second because \(b'\le b\). Contradiction.

**Remarks.** (i) The proof is classical; no ultrafilter or Boolean-prime-ideal theorem is invoked. (ii) Neither zero-dimensionality of \(X\) nor completeness/Booleanness of \(B\) is used. (iii) Compactness of the closed \(F\), and the ability to choose a relatively compact neighborhood with closure avoiding \(F\), explain the local compactness hypothesis.

## 3. The generic-middle lower bound

Let \(f:T=\operatorname{Loc}(B)\to Z\) be a locale map for **any** frame \(B\); let \(h=f^*\) as in Lemma 1. Then
\[
A_f=(f,\operatorname{id}_V)^{-1}A
=\bigwedge_{\mathcal C\ \mathrm{admissible}}\mathfrak o(w_{\mathcal C}),\quad
w_{\mathcal C}=\bigvee_{a\in\mathcal C}h(a)\boxtimes a\in\mathcal O(T\times V).
\tag{3.1}
\]

**Lemma 2.** Every \(w_{\mathcal C}\) is dense in \(T\times V\). Thus
\[
(T\times V)_{\neg\neg}\ \le A_f.
\tag{3.2}
\]
The same holds with \(f\) in the second endpoint by symmetry.

*Proof.* Fix a nonzero basic rectangle \(b\boxtimes v\) with \(b>0\) and \(v>0\). Choose a nonempty ambient X-open \(U\) with \(U\cap V\subseteq v\). By (H2), there exists \(N_U\) such that \(K_n\cap U\ne\varnothing\) for \(n>N_U\). By Lemma 1 choose \(n>N_U\) and \(d\in K_n\) whose every neighborhood \(W\) has \(b\wedge h(W\cap V)>0\).

Admissibility provides \(a\in\mathcal C\) and an open \(W\supseteq K_n\) with \(W\cap V\subseteq a\). As \(W\ni d\), we have \(b\wedge h(a)>0\). Since \(K_n\cap U\ne\varnothing\), the nonempty open \(W\cap U\) meets dense \(V\), so \(a\wedge v>0\). Hence
\[
(b\boxtimes v)\wedge w_{\mathcal C}
\ge(b\wedge h(a))\boxtimes(v\wedge a)>0.
\]
The final product rectangle is nonzero: the nonzero V-open \(v\wedge a\) has an ordinary point, so the nonzero locale corresponding to \(b\wedge h(a)\) embeds in that rectangle by a section. Rectangles join-generate the product frame. This proves density of \(w_{\mathcal C}\). All dense opens contain the double-negation sublocale, which is therefore contained in their arbitrary sublocale meet.

Now specialize to an arbitrary nonzero **complete Boolean** frame \(B\), and take any remote pair \(f,g:T=\operatorname{Loc}(B)\to Z\). The common two-edge source over \((f,g):T\to V^2\) is
\[
E_{f,g}=A_f\wedge A^g\hookrightarrow T\times V.
\]
By Lemma 2, it contains the *same* \(N=(T\times V)_{\neg\neg}\). Since \(V\) has an ordinary point, the product projection \(p:T\times V\to T\) has a section and \(p^*:B\hookrightarrow\mathcal O(T\times V)\) is injective. Its image consists of complemented elements, unchanged by double negation. Therefore \(N\to T\) is a **genuine locale-surjection**. So is \(E_{f,g}\to T\).

The endpoint map \(E_{f,g}\to V^2\) factors through the image \(A^2=\operatorname{im}(E(A,A)\to V^2)\). The new surjection \(E_{f,g}\to T\) forces \((f,g):T\to V^2\) to factor through \(A^2\): an equation valid on \(A^2\) holds after pullback to \(E_{f,g}\), hence already on \(T\) by injectivity of the latter surjection's inverse-image map. **No arbitrary base-change stability of images is assumed.**

Complete Boolean locales jointly detect arbitrary sublocale inclusion by the closed-quotient-then-double-negation separation lemma. Hence
\[
\boxed{Z\times Z\le A^2.}\tag{3.3}
\]

## 4. Upper bound by compact-local diagonality

For any compact \(K\subseteq V\), its inclusion into \(X\) is closed (Hausdorff), so the ambient open \(X\setminus K\) contains every \(K_n\). Hence \(V\setminus K\) is a Θ-admissible open **member**, with Θ-value all of \(\mathbb N\).

For every open \(w\in\mathcal O(K\times V)\) containing the graph diagonal \(\Delta_K\), compactness of \(K\), the rectangle basis of \(K\times V\), and regularity of \(V\) give finitely many \(V\)-opens \(b_i\) covering \(K\) for which
\[
\bigvee_i (K\cap b_i)\boxtimes b_i\le w.
\]
The finite Θ-admissible cover \(\{V\setminus K,b_1,\ldots,b_m\}\) of \(V\) then forces \(A|_{K\times V}\le\mathfrak o(w)\). Since \(K\times V\) is spatial (the compact Hausdorff factor \(K\) is locally compact) and regular, \(\Delta_K\) is fitted, so
\[
A\wedge(K\times V)=\Delta_K=A\wedge(V\times K).
\tag{4.1}
\]

The same equality holds for **all parenthesized finite powers** of \(A\): use induction on the binary bracketing, and stability of locale-surjections under **closed** base change \(K\times V\hookrightarrow V^2\) (the standard explicit quotient calculation \(\uparrow c\to\uparrow e^*c\) is injective for a surjective map \(e\)). This also follows from the independently checked general theorem that composites of compact-locally diagonal relations are compact-locally diagonal.

Apply the **abstract closed-family remote-equivalence theorem** to the family of compact closed sublocales \(K\subseteq V\):
\[
A^2\le R_\infty=\Delta_V\vee(Z\times Z),\qquad R_\infty^2=R_\infty.
\]
Together with (3.3) and reflexivity \(\Delta_V\le A^2\), this gives the saturation equality. Since \(\Delta_V\le A\le R_\infty\), monotonicity plus \(R_\infty^2=R_\infty\) gives \(AR_\infty=R_\infty=R_\infty A\); induction at the root of any binary bracketing gives all-power stabilization, **without reassociation**.

## 5. Whole fitted-diagonal transfer: finiteness of the K_n is not needed

The external CO-01 referee supplied the missing finite-join distributivity and four-block arguments, but suggested that *finiteness* of \(K_n\) is necessary for the mixed-fibre vanishing. For the stated present hypotheses that caution is **unnecessarily strong**.

For every n, \(K_n\) is **closed** in \(X\), and the topological subspace inclusion \(j:V\hookrightarrow X\) factors through the complementary **open sublocale** \(X\setminus K_n\) (since \(V\cap K_n=\varnothing\)). Consequently
\[
\boxed{j^{-1}(K_n)=0\quad\text{as a locale},}
\tag{5.1}
\]
**regardless of whether \(K_n\) is finite**. As \(X\) is regular, the closed compact sublocale \(K_n\) is fitted:
\[
K_n=\bigwedge_{W\supseteq K_n}\mathfrak o_X(W).
\]
By inverse-image meet preservation,
\[
\bigwedge_{W\supseteq K_n}\mathfrak o_V(W\cap V)
=j^{-1}(K_n)=0.
\tag{5.2}
\]
The two-element Y-covers \(\{\,\{n\}\cup(W\cap V),\,Y\setminus\{n\}\,\}\) therefore force the \(V\times\{n\}\) fitted-diagonal fibre to be 0. This extends to all \(V\times N\) because the \(V\times\{n\}\) are **open** in \(V\times N\) and cover it, so any sublocale is the join of its restrictions to these opens. Symmetry gives the opposite mixed block.

On \(N^2\) the relation is exactly \(\Delta_N\), since N is discrete and Y Hausdorff. The four complementary open/closed blocks cover \(Y^2\), and finite distributivity of the sublocale coframe yields
\[
\boxed{\mathcal D_Y=A\vee\Delta_N.}
\tag{5.3}
\]
Preimage on sublocales preserves finite joins and arbitrary meets, and localic image preserves joins. Thus relation composition distributes over finite joins; the crossed terms \(A\circ\Delta_N\), \(\Delta_N\circ A\) vanish because they would require a middle coordinate in \(V\wedge N=0\). For \(P,Q\subseteq V^2\), their composite in \(V\) has the same localic image when embedded in \(Y^2\). Therefore
\[
(P\vee\Delta_N)\circ(Q\vee\Delta_N)=(P\circ Q)\vee\Delta_N,
\]
establishing the asserted transfer for every bracketing.

**Critical distinction from the referee's example.** The referee correctly notes that disjoint *dense nonclosed* subspaces can have a nonzero localic meet. That fact does **not** apply to the individual **closed** \(K_n\): their open complements contain \(V\), so (5.1) follows directly from factorization. The union \(D=\bigcup K_n\) is typically not closed, but the mixed-fibre argument only pulls back the individual closed pieces.

This strengthening is **newly checked internally** and has not been externally refereed in this general form.

## 6. Nontriviality and the status of strictness

Every compact \(K\subseteq V\) has empty interior in V. Otherwise choose nonempty X-open U with \(U\cap V\subseteq K\). Since K is closed in Hausdorff X and V dense, U⊆K. But (H2) forces U to meet some \(K_n\subseteq X\setminus V\), contradiction. Consequently each \(V\setminus K\) is a **dense open** of V, hence Z contains the Booleanization \(V_{\neg\neg}\ne0\). Any ordinary point of Z would lie outside its own compact singleton, impossible: \(Z\) is a nonzero **pointless** sublocale.

Likewise any admissible cover \(\mathcal C\) gives a **dense** \(\gamma_{\mathcal C}\in\mathcal O(V^2)\): given nonempty opens \(v_1,v_2\) and ambient nonempty \(U_i\) with \(U_i\cap V\subseteq v_i\), take n so large that \(K_n\) meets both \(U_i\); the admissible a with a neighborhood of the whole \(K_n\) then meets both \(v_i\). Thus \(A\) contains \((V^2)_{\neg\neg}\). Choose disjoint nonempty V-opens \(v_1,v_2\): their nonzero rectangle meets the Booleanization but not the diagonal. Hence \(\Delta_V<A\). The hypotheses ensure V has at least two distinct points: an isolated ambient open point would violate (H2) together with (H1).

**Not established in full generality:** \(A<A^2\). Although the original Cantor example has an explicit three-permutation witness, no argument here shows that all systems admit such a witness. Do not attach this strictness to the general theorem without proof.

## 7. Explicit broad strict family, including infinite compact K_n

Let \(C=2^{\mathbb N}\), and \(M_n\subset C\) be the **finite** nonzero-support bitstrings whose last 1 is at position n, as in the original CO-01 construction. Let \(H\) be **any nonempty compact Hausdorff space** and put
\[
X=C\times H,\qquad K_n=M_n\times H,\qquad
V=(C\setminus\bigcup M_n)\times H.
\tag{7.1}
\]
These K_n are disjoint and compact, and V is dense. Every nonempty ambient open contains a product of nonempty opens U×J, and for all large n the M_n meet U; hence (H2). For infinite H the K_n are **infinite**; for H connected, X is not Stone; for nonmetrizable Stone H, the construction gives nonmetrizable Stone examples.

Let \(B=\operatorname{RO}(V)\), \(q:\mathcal O(V)\to B\) its double-negation quotient. The original Cantor coordinate permutations \(\sigma,\tau\) induce homeomorphisms
\[
\Phi_\pi=(\widehat\pi,\operatorname{id}_H):X\to X,
\]
preserving D and V. Put \(h=q\), \(k=q\Phi_\sigma^*\), \(\ell=q\Phi_\tau^*\).

The original three-permutation calculation survives **all admissible X-covers**. To test density in a nonempty V-open, take a nonempty product-open U×J there. Choose a sufficiently high finite-support Cantor point x with the prescribed prefix so that x and σx lie in the same \(M_n\), respectively σx and τx in the same \(M_{n+2}\); fix t∈J. An admissible cover has one member containing the trace of an X-neighborhood of the **entire** \(M_m\times H\). Continuity makes that member and its corresponding pullback overlap on an open neighborhood of \((x,t)\), whose V-trace is nonempty by density. Hence \(hAk\) and \(kA\ell\).

For the nonedge, take the original separating Θ-cover of \(C\setminus\bigcup M_n\): clopen neighborhoods \(W_n\supset M_n\) with \(W_n\cap\widehat\tau^{-1}(W_n)=\varnothing\), plus a clopen supplementary cover separating id and τ over \(B_0=\{x:x_1=1,x_3=0\}\). Multiply every Cantor open by **all of H**. The resulting X-cover of V is Θ-admissible and its id–τ overlap misses the nonempty open \((B_0\cap (C\setminus D_C))\times H\), so \(h\not A\ell\).

Thus
\[
\boxed{\quad A<A^2=R_\infty,\quad\text{for EVERY nonempty compact Hausdorff }H.}
\tag{7.2}
\]
In particular, the genuinely infinite-K_n case \(H=[0,1]\) gives an explicit non-Stone example; a nonmetrizable Stone H gives a nonmetrizable Stone example. The full fitted diagonal has the same strict square and stabilized subsequent powers by §5. These are **internally argued extensions**, not independently audited.

## 8. Why the mixing condition matters: a counterexample without (H2)

Take \(X=C\times\{0,1\}\), and alternate the original Cantor M_n between the two clopen halves:
\[
K_{2n-1}=M_n\times\{0\},\qquad K_{2n}=M_n\times\{1\}.
\]
The K_n are pairwise disjoint finite compacta and V is dense, but (H2) fails: each clopen half misses infinitely many K_n.

Write \(V=V_0\sqcup V_1\). The two-member cover \(\{V_0,V_1\}\) is Θ-admissible, since every K_n lies wholly in one clopen half. Therefore
\[
A\le\mathfrak o(V_0^2\sqcup V_1^2).
\]
Every two-edge path likewise stays in one half, so \(A^2\) has **zero cross blocks**. However the compact-remote Z has nonzero parts in both halves: the Booleanization \(\operatorname{Loc}(\operatorname{RO}(C\setminus D_C))\) maps remotely to either copy. Using the same Boolean domain for the two copies gives a nonzero generalized pair in \(Z^2\) with endpoints in opposite halves. Hence
\[
\boxed{Z^2\nleq A^2.}
\]
So saturation fails without some hypothesis coupling the tails of the K_n across all nonempty opens. This shows (H2) is doing essential work; it is not claimed to be logically necessary in every system.

## 9. Scope and next tests

- The original Arrieta/CO-01 example is recovered by \(X=C\), \(K_n=M_n\).
- The proof of **square saturation** uses H1/H2, local compactness for a compact boundary witness, compact-local diagonal restrictions, Boolean probes, and closed-base-change stability; no Stone duality or ultrafilters.
- The transfer to **all of \(\mathcal D_Y\)** uses closedness of **individual** \(K_n\), not their finiteness, plus finite-join preservation of sublocale inverse image.
- Strictness \(A<A^2\) is separately verified for the product family, not claimed for arbitrary X.
- No assertion about the effectivity of \(R_\infty\), nor about literature priority, is made.
- Possible next bounded target: determine whether \(A<A^2\) follows already from H1/H2 in general, or find a counterexample. In parallel, audit the stronger locally compact transfer, especially the direct factorization \(j:V\to X\setminus K_n\).

## References and provenance

1. Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, *Topology Appl.* **342** (2024), 108785; Construction 4.2, Example 4.5 (arXiv:2310.18522).
2. [CO-01 original full proof](ProjectA_CO01_Arrieta_square_saturates_remote_equivalence_PROOF_2026-11-11.md).
3. [CO-01 external referee reconciliation](ProjectA_CO01_EXTERNAL_referee_reconciliation_2026-11-11.md).
4. [Abstract closed-family remote-equivalence theorem](ProjectA_closed_family_remote_equivalence_general_theorem_2026-11-11.md).
5. [Compact-local diagonality](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md).
6. For inverse image on sublocales preserving arbitrary meets and finite joins, see the standard coframe-homomorphism statement in the literature, e.g. *On infinite variants of De Morgan law in locale theory*, J. Pure Appl. Algebra (2021), §2.

**Status: internally derived generalization only. No independent referee has checked the new locally compact generality, the improved infinite-\(K_n\) transfer, or the product-family strictness argument.**
