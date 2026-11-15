# Project A — Specialization as the Sierpiński exponential

**Canonical categorical note · 15 November 2026.** Referee-origin insight from the independent blind (A-SC) audit, rederived and checked internally. The statement \(\mathcal A(X)\cong X^{\mathbb S}\) and the finite-poset extension were **not** part of the original blind packet. They are not claimed as novel in the literature.

## 1. The localic exponential

Let \(\mathbb S\) be the Sierpiński locale, with open frame \(0<s<1\) and specialization order \(0\le1\) on its two ordinary points. For **every** locale \(Z\), there is a natural frame isomorphism

\[
\boxed{\mathcal O(Z\times\mathbb S)
\cong \{(u,v)\in\mathcal O(Z)^2:u\le v\},}
\tag{1.1}
\]

where order and operations on the right are componentwise. To check this in the full category of locales, rather than only for products of topological spaces, note that the right-hand frame is the coproduct of \(\mathcal O(Z)\) and the three-element frame. The first canonical frame map takes \(u\mapsto(u,u)\), and the Sierpiński generator takes \(s\mapsto(0,1)\). Given any target frame \(M\), frame map \(f:\mathcal O(Z)\to M\), and element \(b\in M\) (the image of \(s\)), the unique frame map extending both is

\[
(u,v)\longmapsto f(u)\vee(b\wedge f(v)).
\tag{1.2}
\]

The finite-meet law follows from \(u\le v\); arbitrary joins follow componentwise.

For a locale \(X\), a map \(h:Z\times\mathbb S\to X\) is therefore a frame homomorphism

\[
h^*:\mathcal O(X)\to
\{(u,v)\in\mathcal O(Z)^2:u\le v\}.
\]

Writing \(h^*(a)=(f^*a,g^*a)\), it is precisely a pair of locale maps \(f,g:Z\to X\) such that \(f^*a\le g^*a\) for every \(a\in\mathcal O(X)\). By the universal presentation of the specialization sublocale, such a pair is the same as a map \(Z\to\mathcal A(X)\). Naturality in \(Z\) yields

\[
\boxed{\mathcal A(X)\ \cong\ X^{\mathbb S}.}
\tag{1.3}
\]

This explicitly constructs the Sierpiński exponential for every locale \(X\), with no spatiality assumption on either \(X\) or \(Z\).

## 2. Immediate formal consequences

Because \((-)^{\mathbb S}\) is right adjoint to \((-)\times\mathbb S\), the functor \(\mathcal A\) preserves **all limits that exist in \(\mathbf{Loc}\)**. This recovers and strengthens previously established identities without arguments about images or localic relation composition:

\[
\mathcal A(X\times Y)\cong\mathcal A(X)\times\mathcal A(Y)
\tag{2.1}
\]

for arbitrary locales, and similarly for arbitrary products, pullbacks and equalizers.

On ordinary points, the specialization order on \(\operatorname{pt}(\mathcal A(X))\) is the restriction of the coordinatewise order on \(\operatorname{pt}(X)^2\), since \(\mathcal A(X)\) is a sublocale of \(X^2\) and its point topology is the induced topology. Thus ordinary points of \(\mathcal A(\mathcal A(X))\) are **commuting monotone squares** in the specialization preorder. This is an interpretation of points, not an assertion that arbitrary localic relation composition associates.

The proof of the [A-SC theorem](ProjectA_ASC_CANONICAL_2026-11-15.md) shows moreover that when \(X\) is stably locally compact, this exponential locale is itself **stably locally compact and spatial**, with ordinary point set \(G_{\le_X}\).

## 3. Finite-poset diagram locales

Let \(P\) be a finite poset, regarded as its finite Alexandrov \(T_0\) locale: opens are upsets. A finite version of (1.1) identifies

\[
\mathcal O(Z\times P)
\cong\{(u_p)_{p\in P}:p\le q\Rightarrow u_p\le u_q\}.
\tag{3.1}
\]

This follows from the finite localic coproduct presentation, not merely from spatial products. Consequently \(X^P\) is the sublocale of \(X^P_{\mathrm{cart}}=\prod_{p\in P}X\) presented by the inequalities

\[
a_p\le a_q\qquad(a\in\mathcal O(X),\ p\le q\text{ in }P).
\tag{3.2}
\]

Here \(X^P\) on the left means the **locale exponential**, while \(X^P_{\mathrm{cart}}\) denotes the finite cartesian product; the notation separates the two constructions.

**Proposition (internally checked extension).** If \(P\) is a finite poset and \(X\) is stably locally compact, then the localic exponential \(X^P\) is spatial and stably locally compact. Its points are precisely monotone maps of posets \(P\to\operatorname{pt}(X)\).

*Proof.* For coherent \(Y\), its finite product \(Y^P_{\mathrm{cart}}\) is coherent. Because the inequalities (3.2) can be imposed on its bounded distributive compact-open lattice, the resulting exponential \(Y^P\) is again coherent. The construction \(X\mapsto X^P\) is functorial and preserves retractions, being a right adjoint.

If \(U\hookrightarrow Y\) is any sublocale, the quotient on opens shows that the defining inequalities for \(U^P\) are precisely the restrictions of those for \(Y^P\). Hence

\[
U^P \cong
U_{\mathrm{cart}}^P\times_{Y_{\mathrm{cart}}^P}Y^P.
\tag{3.3}
\]

When \(U\) is **open**, the right-hand side is an open sublocale of \(Y^P\). Now take the direct open-spectral retraction of a stably locally compact \(X\) from \(U\), where \(U\) is open in coherent \(Y\), as proved in the A-SC canonical note. Applying \((-)^P\), the locale \(X^P\) retracts from the open sublocale \(U^P\) of coherent \(Y^P\). It is spatial by the retract argument, and stably locally compact because that class is closed under open sublocales and retractions. \(\square\)

The finite-poset result is a useful **new corollary within the project**; its relation to established work on function-space locales, domain theory and exponentiability has not been investigated for priority.

## 4. Boundaries and next questions

1. Nothing here says that the exponential of a *spatial* locale by an arbitrary locale is spatial. The proved spatiality class is stably locally compact inputs \(X\), with finite poset exponent \(P\).
2. For general locally compact \(X\) without stable continuity, the ideal-completion map \(a\mapsto\{v:v\ll a\}\) need not preserve binary meets. The retraction proof then fails; no all-locally-compact spatiality theorem follows.
3. This categorical description does **not** repair the known nonassociativity of arbitrary image-defined localic relation composition: a right adjoint on objects and maps is different from exactness of relational images.
4. It may be fruitful to study finite diagram locales alongside Project A's coherent graph-power and bisimplicial constructions, keeping the distinction between point-level directed diagrams and genuine localic compositions.

**Provenance:** The Sierpiński-exponential observation and finite-poset suggestion originated in the independent blind referee's *additions* to their (A-SC) report. They were checked in this follow-up but did not receive a second external audit. No originality or bibliographic priority claim.
