# Project A — Point-free generalized specialization spans: stable fitted-diagonal density, noncompact pointless fiber transfer, and the compactness no-go

**12 November 2026 — new internal bounded theorem and independent checks; not externally audited or priority checked.** Continuation of [universal point-free U/I products and compact-fiber W/W₂ transfer](ProjectA_Q_POINTFREE_PRODUCTS_URYSOHN_AND_COMPACT_FIBER_TRANSFER_2026-11-12.md), prompted by the question whether compactness of the fiber can be replaced by a condition on the D₂-dense relation. **Yes** if the density is witnessed by generalized *common-specialization-predecessor spans*. The new method handles NONCOMPACT, entirely POINTLESS fibers and bases without invoking ordinary points or compact tube lemmas. It remains a sufficient condition, not a characterization, and universal Q/Q′ remain OPEN.

The specialization ordering of locale maps is standard 2-categorical structure: for \(p,f:T\to Y\), write \(p\preceq f\) iff \(p^*(a)\le f^*(a)\) for every \(a\in O(Y)\). See e.g. Johnstone, *Stone Spaces* / Vickers, *Locales and Toposes as Spaces*, Ch. 1, and the nLab page “locale”. The following consequences for the fitted diagonal are derived here, not ascribed to those sources.

## 0. Definitions and order stability

Let \(L=O(Y)\). A **generalized common-predecessor span** consists of an arbitrary locale T (possibly POINTLESS) and three locale maps \(p,f,g:T\to Y\) with
\[
\boxed{p^*(a)\le f^*(a)\wedge g^*(a)\qquad\forall a\in O(Y).}
\tag{0.1}
\]
It determines a generalized pair \((f,g):T\to Y^2\).

The 2-order is preserved by taking products with an arbitrary locale Z: for any x∈O(Z×Y), using rectangle generators,
\[
(\operatorname{id}_Z\times p)^*(x)
\le(\operatorname{id}_Z\times f)^*(x),
\quad
(\operatorname{id}_Z\times p)^*(x)
\le(\operatorname{id}_Z\times g)^*(x).
\tag{0.2}
\]

Let \(\Sigma(Y)\) denote the JOIN AS SUBLOCALES of the images of ALL generalized common-predecessor spans, viewed as a sublocale of Y². This is a SET-defined sublocale: even though there may be a proper class of source locales/maps, the resulting image sublocales belong to the SET of sublocales of Y². Every image is below the full fitted diagonal by Theorem 1.1, so
\[
\boxed{\Sigma(Y)\le\mathcal D(Y)\le\mathcal D_2(Y)\le\mathcal W_2(Y).}
\tag{0.3}
\]
Calling Σ the **specialization-span core** is project terminology, not an asserted standard construction. No claim that Σ=D is made.

## 1. Universal base-change of individual spans

**Theorem 1.1 (point-free stable full fitting).** For ANY locales Z,Y,T and any span (0.1), the induced locale map
\[
F:Z\times T\longrightarrow (Z\times Y)^2,\quad
F(z,t)=((z,f(t)),(z,g(t)))
\tag{1.1}
\]
factors through the FULL fitted diagonal \(\mathcal D(Z\times Y)\).

*Proof.* Let C be an arbitrary cover of X=Z×Y (no finiteness assumption), and let \(a_i:Z\times T\to Z\times Y\) be the maps id×f,id×g, and \(a_0=\mathrm{id}\times p\). By (0.2), \(a_0^*(c)\le a_1^*(c)\wedge a_2^*(c)\) for EVERY c∈C. Therefore
\[
1_{Z\times T}=\bigvee_{c\in C}a_0^*(c)
\le\bigvee_{c\in C}a_1^*(c)\wedge a_2^*(c)
=F^*(w_C).
\]
Since C is arbitrary, F factors through \(\bigwedge_C O(w_C)=D(X)\). □

**This genuinely removes all ordinary points:** the source T and both factors Z,Y may be pointless, and the cover may be infinite. It is the pointfree replacement for the older “ordinary point pair with a common specialization predecessor” lifting argument.

## 2. Density of generalized spans implies exact closed-hull transfer

Call Y **span-dense at W₂** if
\[
\boxed{\operatorname{cl}_{Y^2}\Sigma(Y)=\mathcal W_2(Y).}
\tag{2.1}
\]
Equivalently, EVERY nonzero relatively OPEN sublocale of W₂(Y) meets the image of some generalized predecessor span. The equivalence uses that any open sublocale disjoint from EVERY span image is disjoint from their join, since their sublocale join is contained in its CLOSED complement.

**Lemma 2.1 (span density forces Q′ equality on the fiber).** If (2.1) holds then
\[
\boxed{\mathcal W(Y)=\mathcal W_2(Y).}
\tag{2.2}
\]
Proof: Σ(Y)≤D(Y), so \(\mathcal W_2(Y)=\operatorname{cl}\Sigma(Y)\le\operatorname{cl}\mathcal D(Y)=\mathcal W(Y)\le\mathcal W_2(Y)\). □

**Theorem 2.2 (stable span-dense transfer, NEW INTERNAL).** Let Z be ANY locale (possibly POINTLESS) with
\[
\boxed{\mathcal W_2(Z)=\mathcal I(Z).}
\tag{2.3}
\]
Let Y be ANY, possibly NONCOMPACT and POINTLESS, locale satisfying (2.1). Then
\[
\boxed{\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\mathcal I(Z)\times\mathcal W_2(Y).}
\tag{2.4}
\]
No local-compactness or coherence assumptions are made.

*Proof.* Naturality under projection (previously established for W₂) gives the UPPER inclusion
\[
\mathcal W_2(Z\times Y)\le\mathcal W_2(Z)\times\mathcal W_2(Y)
=\mathcal I(Z)\times\mathcal W_2(Y).
\tag{2.5}
\]
For the REVERSE, consider the images in \((Z\times Y)^2\) of ALL maps (1.1) supplied by spans. By Theorem 1.1 they lie in D(Z×Y). Their join is DENSE in the possibly NONCLOSED product \(\Delta_Z\times\mathcal W_2(Y)\): for any nonzero relative open rectangle \(a\boxtimes b\), with a∈O(Z), b∈O(W₂(Y)), pick a predecessor span whose image meets b. Restrict its source T to the nonzero preimage \(t=(f,g)^*b>0\); the pullback of the rectangle along F is the NONZERO localic product \(O_Z(a)\times O_T(t)\). Therefore \(\operatorname{cl}\mathcal D(Z\times Y)\) contains
\[
\operatorname{cl}_{(Z\times Y)^2}\bigl(\Delta_Z\times\mathcal W_2(Y)\bigr)
=\mathcal I(Z)\times\mathcal W_2(Y),
\]
using the general product-of-closures lemma from the preceding note. This supplies the reverse containment and proves (2.4). □

**Corollary 2.3 (pointless separated base).** If \(\mathcal U(Z)=\Delta_Z\), then \(\mathcal W_2(Z)=\mathcal I(Z)=\Delta_Z\), and
\[
\boxed{\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)=\Delta_Z\times\mathcal W_2(Y).}
\tag{2.6}
\]
Combining with the unrestricted pointfree product formula for U,
\[
\boxed{\mathcal U(Z\times Y)=\Delta_Z\times\mathcal U(Y).}
\tag{2.7}
\]
For nonzero Z, W=U on the product iff W₂(Y)=U(Y); but this latter equality is already W(Y)=U(Y) by Lemma 2.1. Thus the constructed class never yields a Q/Q′ counterexample—correctly, because we have proved their positive equality.

**Important scope:** The method requires DENSITY of actual predecessor spans in W₂(Y). It does not assert that mere equality W=W₂ implies span density; nor does it prove that every finite-cover-compatible generalized pair has a common predecessor. Replacing that density assumption by arbitrary D₂-density is EXACTLY the unresolved pointfree base-change difficulty.

### 2.4 Independent easy product corollaries: the W=I and W₂=I classes

These follow from the PREVIOUS universal \(\mathcal I\)-product formula and from naturality, **without** the generalized span theorem. They belong in the general theorem ledger rather than being counted as evidence that span density is automatic.

**Corollary 2.4.** For arbitrary locales Z,Y,
\[
\boxed{
\begin{aligned}
\mathcal W(Z)=\mathcal I(Z),\ \mathcal W(Y)=\mathcal I(Y)
&\Longrightarrow \mathcal W(Z\times Y)=\mathcal I(Z\times Y),\\
\mathcal W_2(Z)=\mathcal I(Z),\ \mathcal W_2(Y)=\mathcal I(Y)
&\Longrightarrow \mathcal W_2(Z\times Y)=\mathcal I(Z\times Y).
\end{aligned}}
\tag{2.8}
\]
*Proof.* For either \(R=\mathcal W\) or \(R=\mathcal W_2\), naturality gives
\[
\mathcal I(Z\times Y)\le R(Z\times Y)\le R(Z)\times R(Y)
=\mathcal I(Z)\times\mathcal I(Y)=\mathcal I(Z\times Y).
\]
All inclusions are equalities. □

Thus both classes are closed under ARBITRARY BINARY PRODUCTS; by induction under all FINITE products. No reflection statement for arbitrary POINTLESS factors is asserted.

If W₂(Y)=I(Y), span density (2.1) is AUTOMATIC because Δ_Y⊆Σ(Y) and its closure is I(Y)=W₂(Y). This recovers the second product case using the more elaborate span proof, but the direct naturality argument is preferable.

## 3. A directly checkable condition on the CANONICAL Boolean witness

Let \(B=B(\mathcal W_2(Y))\) denote Isbell's least dense Boolean sublocale of W₂(Y), with canonical coordinate maps \(h,k:B\to Y\). Suppose that B has an OPEN COVER by sublocales \(B_i\) such that on each \(B_i\) there exists a generalized predecessor
\[
\boxed{p_i:B_i\to Y,\qquad p_i\preceq h|_{B_i},\quad p_i\preceq k|_{B_i}.}
\tag{3.1}
\]

**Corollary 3.1 (Boolean-predecessor local coverage criterion).** Under (3.1), Y is span-dense at W₂, so the full conclusions of Theorem 2.2 apply for any Z satisfying (2.3).

*Proof.* Each \((p_i,h_i,k_i)\) is a span, so the image in Y² of B_i lies in Σ(Y). The \(B_i\)'s COVER B; hence the sublocale join of their images contains B. Since B is DENSE in W₂(Y), Σ(Y) is dense there. □

This formulation is genuinely *on a dense sublocale of W₂(Y)*, not on finite subcovers of Y itself. It is a strong, testable SUFFICIENT condition. **In a complete Boolean source, local predecessors can always be disjointified and pasted into a SINGLE global predecessor, as proved in §3.3**; the apparently weaker local option introduces no extra generality in classical Set.

**Corollary 3.2 (direct positive Q test).** If Y happens to satisfy \(\mathcal W_2(Y)=\mathcal U(Y)\) and (3.1), then \(\mathcal W(Y)=\mathcal U(Y)\). This is a positive class of the original rank-one Q question. No claim that (3.1) is automatic from rank-one stabilization is made.

### 3.3 Boolean disjointification: the local predecessor condition is equivalent to ONE GLOBAL predecessor

The criterion in Corollary 3.1 can be simplified substantially **in classical set theory** because \(B=B(W₂(Y))\) is a COMPLETE BOOLEAN locale.

**Proposition 3.3 (Boolean-valued predecessor selection).** Let h,k:Y-valued locale maps from a Boolean locale B (i.e. frame maps O(Y)→M=O(B), with M complete Boolean). The following are equivalent:
1. An OPEN COVER \(\{B_i=O_B(m_i)\}_{i\in I}\) of B exists with local maps \(p_i:B_i\to Y\) satisfying \(p_i\preceq h|_{B_i},k|_{B_i}\).
2. ONE GLOBAL map \(p:B\to Y\) exists satisfying \(p\preceq h,k\).

*Proof.* (2)⇒(1) is immediate. For (1)⇒(2), well-order I and disjointify the Boolean cover:
\[
n_i=m_i\wedge\neg\bigvee_{j<i}m_j.
\]
The \(n_i\) are pairwise disjoint, \(n_i\le m_i\), and \(\bigvee_i n_i=1_M\). Restrict the map p_i to O_B(n_i) (a clopen summand), obtaining a frame map \(q_i^*:O(Y)\to\downarrow n_i\). Because the n_i form a disjoint cover, define
\[
\boxed{p^*(a)=\bigvee_{i\in I}q_i^*(a)\in M.}
\]
This preserves arbitrary joins, finite meets (cross terms for distinct i vanish), and 1. It is a frame homomorphism and hence a locale map. For each a, \(q_i^*(a)\le n_i\wedge h(a)\wedge k(a)\), so joining yields \(p^*(a)\le h(a)\wedge k(a)\) as required. □

Thus the open-local predecessor criterion on the canonical BOOLEAN witness is simply the existence of a **single frame map**
\[
\boxed{p^*:O(Y)\to O(B(W₂(Y)))\quad\text{with}\quad
p^*(a)\le h(a)\wedge k(a)\ (\forall a).}
\tag{3.2}
\]
There is no genuine additional flexibility in requiring it merely locally on a cover of this particular BOOLEAN locale. This uses classical choice to well-order an arbitrary cover; it does NOT say arbitrary locale-valued maps on arbitrary nonBoolean source locales can be pasted without compatibility.

A subtle but important point: the equivalence of (1) and (2) does **NOT** mean that the existence of p is necessary for \(W(Y)=W₂(Y)\) or for Q. It is a strong pointfree selection property of the two CANONICAL Boolean coordinate maps, and a useful sufficient criterion. It may fail for Q-positive locales whose closed fitted-diagonal density is essentially non-spanned.

## 4. Fully pointless NONCOMPACT fiber with nontrivial Urysohn boundary — explicit control

Let \(B=\mathrm{RO}(2^\omega)\), the complete ATOMLESS Boolean algebra of regular opens of Cantor space, viewed as a locale. It has NO ordinary completely prime points. It is NONCOMPACT: a nonzero element of a complete atomless Boolean algebra is never compact as a frame element (successively split it into infinitely many pairwise disjoint nonzero pieces and include their remainder). In particular B has NO NONZERO compact open sublocales.

Let P be the finite SIX-POINT upper-Alexandrov fence \(0<5>1<4>2<3\), as in the earlier Project A note, with \(W(P)=W₂(P)=U(P)>I(P)\) and the ordinary common-predecessor point pairs \(\mathrm{Cm}(P)\) dense in U(P). Define
\[
\boxed{Y=B\times P.}
\tag{4.1}
\]
Then Y is POINTLESS (every point would project to one of B), NONCOMPACT (B is a RETRACT of Y by a fixed P-point slice), and
\[
\boxed{\mathcal W_2(Y)=\Delta_B\times\mathcal U(P)>\Delta_B\times\mathcal I(P)=\mathcal I(Y).}
\tag{4.2}
\]
These identities follow from the previously derived compact-fiber theorem with base B and compact P, and the unrestricted U/I product formulas.

Despite Y having NO ordinary points, its W₂ relation is generated DENSELY by genuine POINTLESS generalized predecessor spans. For each \((p,q)\in\mathrm{Cm}(P)\), choose \(t\le p,q\) and take source T=B with
\[
p_0(b)=(b,t),\quad f(b)=(b,p),\quad g(b)=(b,q).
\tag{4.3}
\]
All maps are locale maps B→B×P, and \(p_0\preceq f,g\). Their pair images are the whole B-diagonal fiber at \((p,q)\), i.e. \(\Delta_B\times\{(p,q)\}\). As Cm(P) is dense in U(P), these images are dense in \(\Delta_B\times U(P)=W₂(Y)\). Therefore Σ(Y) is W₂-dense.

This Y has NO cover by COMPACT CLOPEN opens: any nonzero compact open of B×P would project (along the finite P factor) to a nonzero COMPACT OPEN sublocale of B, impossible because B is atomless complete Boolean. Hence the *direct fiber hypothesis* of the previous compact-clopen theorem does not cover this Y; the generalized-span criterion does.

Let Z be any further pointless Boolean locale with \(\mathcal W_2(Z)=\mathcal I(Z)=\Delta_Z\). Then Theorem 2.2 gives
\[
\boxed{\mathcal W(Z\times Y)=\mathcal W_2(Z\times Y)
=\Delta_Z\times\Delta_B\times U(P)=\mathcal U(Z\times Y).}
\tag{4.4}
\]
This supplies an actual **noncompact, entirely pointless FIBER** with nontrivial nonregular Urysohn geometry, stabilized over a further pointless base, with no compact clopen fiber-localization.

**Honest alternative proof:** Here Y itself FACTORS as B×P, and one can also re-associate \(Z\times(B\times P)=(Z\times B)\times P\) to reapply the previous COMPACT-P theorem. The example validates the new span proof and illustrates a genuinely pointfree dense witness, but does NOT establish a logically independent class of explicit locales beyond every possible product re-association. An irreducibly non-product span-dense pointless Y remains to be found.

## 5. A compactness no-go: the entire W₂ relation cannot be the weaker compact object

The suggested weakening “assume \(\mathcal W_2(Y)\) is compact instead of Y” is NOT a genuine weakening:

**Proposition 5.1.** For every locale Y,
\[
\boxed{\mathcal W_2(Y)\text{ is COMPACT}\quad\iff\quad Y\text{ is COMPACT}.}
\tag{5.1}
\]
*Proof.* If W₂(Y) is compact, its first-coordinate projection \(p_1:W₂(Y)\to Y\) is split surjective, because the diagonal map Y→W₂(Y) is a section. A continuous surjective image of a compact locale is compact, hence Y compact. Conversely, if Y is compact then Y² is compact (finite localic Tychonoff), and its CLOSED sublocale W₂(Y) is compact. □

Likewise, compactness of the nonclosed D₂(Y) would force compactness of Y by the same projection-section argument, though compactness of Y need not imply compactness of D₂(Y).

**Moral:** The right compactness replacement is NOT compactness of W₂ or D₂ itself. It is a **locally generated dense family of stable generalized predecessor witnesses**, as in (2.1) or (3.1), which may live over noncompact POINTLESS source locales.

## 6. Relation to Q and the remaining sharp question

The new span mechanism explains a class of *stable full fitting witnesses* whose density survives arbitrary pointfree base change. It is a genuine extension of the older ordinary-point common-predecessor transfer theorem. It also identifies exactly what is MISSING when attempting to replace compactness by arbitrary D₂-density: finite-cover-compatible generalized pairs need NOT admit a predecessor map, and neither their local predecessor factorization nor density of the resulting span images has been shown under \(\mathcal W_2=\mathcal U\).

For a hypothetical Q or Q′ counterexample, a nonzero open hole E is disjoint from D(Y), so it cannot meet ANY generalized predecessor span image. Thus if \(\Sigma(Y)\) were dense in W₂(Y), that hole would be impossible. This is a necessary obstruction reformulation, not yet a direct rank-one solution.

### 6.1 Exact absence of LOCAL generalized predecessors in a canonical Q/Q′ Boolean hole

**Proposition 6.1 (local predecessor exclusion by the SAME bad cover).** Let \(E=\mathcal W_2(Y)\wedge\mathfrak o(w_C\to d_{\mathcal W_2(Y)})>0\) be any canonical full-versus-finite OPEN hole, and let \(M=O(B(E))\) with coordinate maps \(h,k:O(Y)\to M\). For EVERY nonzero \(m\in M\), there is NO frame homomorphism
\[
p_m^*:O(Y)\longrightarrow\downarrow m
\]
satisfying
\[
p_m^*(a)\le(m\wedge h(a))\wedge(m\wedge k(a))
\qquad\text{for all }a\in O(Y).
\tag{6.1}
\]
*Proof.* The marked bad cover C has \(\bigvee_{c\in C}h(c)\wedge k(c)=0_M\). If p_m existed, all its C-values would be zero; but because C is a cover and p_m preserves arbitrary joins and top,
\[
m=p_m^*(1)=\bigvee_{c\in C}p_m^*(c)=0_{\downarrow m},
\]
contradicting m≠0. □

This is a genuinely **pointfree local no-predecessor condition on the CANONICAL BOOLEAN HOLE**, not merely an absence of ordinary common-predecessor point pairs. It holds for Q′ holes and hence for Q holes. It is nevertheless an IMMEDIATE consequence of the fixed bad-cover equation and **ALSO holds on the Boolean probe of a WEAK fitting defect**; the additional condition that B(E) be dense in a NONZERO RELATIVELY OPEN W₂- or U-piece remains indispensable.

**Useful targeted question:** Let \(B=B(\mathcal U(Y))\) be the canonical Boolean witness on a rank-one-stabilized locale \(\mathcal W_2(Y)=\mathcal U(Y)\). Does every nonzero relatively open part of B support some generalized predecessor \(p:T\to Y\), over some NONZERO open T⊆B, below the two restricted coordinate maps? A YES would solve Q for that locale, but a NO might already be visible in previously known Q-positive nonregular T₁ examples. Do NOT automatically assume this local-predecessor property is equivalent to Q; the available proof establishes only sufficiency.

**Status: NEW INTERNAL PROOFS, not externally audited or priority checked. Both Q and Q′ universally OPEN.**
