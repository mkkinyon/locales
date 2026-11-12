# Project A — Testing Boolean common-predecessor selection: generic anchors, two apices, and nonregular pointless rank-one stabilization

**12 November 2026 — NEW INTERNAL bounded tests, new generic-anchor selection lemma, no external audit or novelty check.** Follows [the generalized specialization-span criterion](ProjectA_Q_GENERALIZED_SPECIALIZATION_SPANS_POINTFREE_FIBER_TRANSFER_2026-11-12.md). User approved testing the canonical Boolean predecessor criterion on **known nonregular Q-positive locales**, rather than adding more untested sufficient conditions. Outcome: the canonical predecessor exists on the essential POINTLESS fitted-diagonal density of the compact cofinite-apex control, and on the W₂ of the compact two-apex control; it FAILS on U of the latter, exactly where W₂<U. Moreover it persists under a POINTLESS NONCOMPACT separated base producing a genuinely NONREGULAR Urysohn relation with W₂=U=W. These examples **support the usefulness** of the span criterion, but DO NOT establish that it is necessary for Q or Q′. Universal Q,Q′ remain OPEN.

Notation: for a closed sublocale R≤Y² write B(R) for the Isbell least dense Boolean sublocale, M=O(B(R)), h,k:O(Y)→M for the canonical coordinate frame maps. For a relatively open sublocale V≤R, \(B(V)=B(R)\wedge V\); it is an open Boolean sublocale of B(R). A relatively open V⊂R is dense iff B(R)≤V.

## 1. A general **generic-anchor** criterion on Booleanization

**Theorem 1.1 (generic-anchor selection; NEW INTERNAL).** Let Y be any locale, R⊆Y² a CLOSED sublocale, and suppose there exists a family of relatively OPEN sublocales \(V_i≤R\) with **dense open join** \(V=\bigvee_i V_i\) in R. For each i, suppose there is an ORDINARY point \(t_i:1→Y\) such that for EVERY Y-open a with \(t_i∈a\), both coordinate relative opens
\[
V_i\wedge O_{R}(a\boxtimes1),\qquad
V_i\wedge O_{R}(1\boxtimes a)
\]
are DENSE in V_i. Then there is a SINGLE frame homomorphism
\[
\boxed{p^*:O(Y)\to M=O(B(R)),\quad p^*(a)\le h(a)\wedge k(a)\ \forall a.}
\tag{1.1}
\]
Hence the image of the Boolean locale B(R) in Y² is the image of a generalized common-predecessor span and lies in the full fitted diagonal D(Y). If R=W₂(Y), this gives \(\boxed{W(Y)=W₂(Y)}\), and if R=U(Y)=W₂(Y), it gives Q on Y.

*Proof.* For each i let m_i∈M be the Boolean open restricting B(R) to V_i. Since V is dense in R, B(R)⊆V, so \(\bigvee_i m_i=1_M\). By the dense-coordinate assumption and open localization of Booleanization, whenever t_i∈a one has
\[
m_i≤h(a)\wedge k(a).
\tag{1.2}
\]
Disjointify the Boolean cover in ordinary classical Set: well-order I and set \(n_i=m_i\wedge\neg\bigvee_{j<i}m_j\). These are pairwise disjoint, n_i≤m_i, \(\bigvee_i n_i=1\). Define
\[
\boxed{p^*(a)=\bigvee_{\{i:t_i\in a\}}n_i.}
\tag{1.3}
\]
This is the Boolean coproduct of the ordinary point maps t_i: it preserves arbitrary joins, finite meets and top, and is thus a frame map. For any i with t_i∈a, n_i≤m_i≤h(a)∧k(a), so p^*(a)≤h(a)∧k(a). □

**Conceptual point:** The anchor point t_i need NOT be an ordinary specialization predecessor of any two distinct ordinary point-pairs in V_i. It only needs its neighborhoods to be DENSE in both coordinates of V_i, so those neighborhoods become top in the **pointless Booleanized** piece B(V_i). In a T₁ space, this permits a genuinely nontrivial 2-cell between generalized locale points even though the specialization order on ORDINARY points is discrete.

**Regularity limitation:** When Y is regular as a locale, specialization between ANY locale maps into Y is discrete: if p≤f and a=∨_{b≺a}b with b^*∨a=1 (rather-below), then \(f(b)\wedge p(b^*)=0\), \(p(b^*)\vee p(a)=1\), hence f(b)≤p(a), so f(a)≤p(a); thus p=f. Consequently nontrivial Boolean anchored pairs for T₁ spaces necessarily exploit nonregularity of Y, not the mere absence of ordinary points in the source.

## 2. Test 1: compact cofinite-apex X, W=W₂=U with essential pointless D density

Let \(X=R\sqcup Z\sqcup\{p\}\), where R is the usual crowded real line, Z is infinite discrete, and the neighborhoods of p contain p and all but finitely many points of the old part R⊔Z. Earlier [cofinite-apex proof](A-W-equals-U-boundary-sector-apex-control-2026-10-24.md) establishes: X compact, sober, locally compact T₁; U is the CLOSED relation
\[
\boxed{\mathcal U(X)=((R\cup\{p\})\times(R\cup\{p\}))\cup\bigcup_{z\in Z}\{(z,z)\}.}
\tag{2.1}
\]
The open U-patches \(V_R=R\times R\) and \(V_z=\{(z,z)\}\) have dense union V in U: R is dense in the closed R∪{p} part and each z singleton is clopen in X. This is a spatial calculation of the CLOSED relation only; no claim D spatial is made.

**Anchor verification.** On V_R, choose the point t_R=p. Any open a∋p contains all but finitely many reals, hence a∩R is DENSE in R. Thus each coordinate-cylinder O(a) is dense in R². On V_z, choose t_z=z; both cylinders are the entire singleton whenever a∋z. Theorem 1.1 applies.

Let \(M=O(B(U(X)))\), and e_R,e_z be the mutually disjoint Boolean opens of the canonical Booleanization associated to V_R and V_z. They join to 1. The predecessor is the explicit frame map
\[
\boxed{
p^*(a)=
\bigl(\mathbf 1_{p\in a}\cdot e_R\bigr)
\vee\bigvee_{\{z\in Z:z\in a\}}e_z,
\quad p^*(a)\le h(a)\wedge k(a).
}
\tag{2.2}
\]
The scalar notation means e_R when the condition holds and bottom otherwise.

**Pointfree significance:** On EVERY pair of disjoint nonempty real intervals A,B, D(X)∧O(A⊠B) is NONZERO but has NO ORDINARY POINTS (because X is T₁). Formula (2.2) proves the global B(U) predecessor nonetheless exists. It captures essential POINTLESS fitting density using a CONSTANT ordinary apex as a generalized predecessor in the **Boolean-valued** world, despite that apex being unable to precede distinct ordinary points in X.

## 3. Test 2: compact two-apex X, selection succeeds on W₂ but fails on U

Take \(X=\mathbb R\cup\{p_+,p_-\}\) with cofinite-neighborhoods at p_+ along the positive and p_- along the negative reals, as in [the compact two-apex exact computation](A-W-equals-H-compact-two-apex-telescope-2026-11-09.md). Define
\[
A_+=[0,\infty)\cup\{p_+\},\qquad A_-=(-\infty,0]\cup\{p_-\}.
\]
We know (from the earlier computed compact example)
\[
\boxed{\mathcal W_2(X)=\mathcal W(X)=A_+²\cup A_-²
\ <\ \mathcal U(X)=\mathcal W(X)\cup\{(p_+,p_-),(p_-,p_+)\}.}
\tag{3.1}
\]

Put \(V_+=(0,\infty)^2\), \(V_-=(-\infty,0)^2\); these are DISJOINT relatively open U pieces and their union is DENSE in W=W₂ because each real half-line is dense in its closed A_±. Let e_+,e_-∈O(B(W₂)) be the Boolean opens induced by V_±. They are disjoint and e_+∨e_-=1. Choose anchors t_+=p_+, t_-=p_-. Any p_+ neighborhood has cofinite positive trace, and analogously for p_-. Thus
\[
\boxed{p^*(a)=
(\mathbf 1_{p_+\in a}\cdot e_+)\vee
(\mathbf 1_{p_-\in a}\cdot e_-)
\le h(a)\wedge k(a).}
\tag{3.2}
\]
So the strong canonical predecessor selection property holds on B(W₂), even though W₂ contains off-diagonal U-related ordinary pairs with NO ordinary common predecessor (e.g. two distinct positive reals).

**Exact failure on B(U).** The mixed pair (p_+,p_-) is a RELATIVELY ISOLATED point of the CLOSED Urysohn sublocale U(X), detected by the open mixed rectangle \(u_+\boxtimes u_-\), where \(u_+=(0,\infty)\cup\{p_+\}\), \(u_-=(-\infty,0)\cup\{p_-\}\). Hence it gives a NONZERO Boolean atom of B(U). On that atom, the coordinate maps evaluate at the two DISTINCT ordinary points p_+,p_-. If a global predecessor existed on B(U), restricting to this atomic Boolean component would supply an ORDINARY point t∈X satisfying t≤p_+ and t≤p_- in specialization order. But X is T₁, so no such t exists. Therefore:
\[
\boxed{\text{A predecessor exists on }B(W₂(X))\text{ but NOT on }B(U(X)).}
\tag{3.3}
\]
This matches precisely the known strict W₂<U in this example, where finite rank-one stabilization \(\Phi_2(z_1)=z_1\) FAILS. It does NOT prove the criterion is necessary when rank-one stabilization holds.

## 4. A fully POINTLESS NONCOMPACT, NONREGULAR U, genuine W₂=U=W test

Let B be the Boolean locale with frame \(O(B)=RO(2^\omega)\), complete atomless Boolean, with NO ordinary points and NO nonzero compact open. Let X be the compact cofinite-apex example §2 and put
\[
\boxed{Y=B\times X.}
\tag{4.1}
\]
The previous [unrestricted U product formula and compact-fiber W transfer](ProjectA_Q_POINTFREE_PRODUCTS_URYSOHN_AND_COMPACT_FIBER_TRANSFER_2026-11-12.md) give
\[
\boxed{\mathcal W(Y)=\mathcal W_2(Y)=\mathcal U(Y)=\Delta_B\times\mathcal U(X).}
\tag{4.2}
\]
Y is POINTLESS (any point would project to B), NONCOMPACT (B is a RETRACT using one X-point), and has NO nonzero compact open sublocales (a compact open in Y would project to one in B under the open projection with compact X fiber). It is not locally compact spatial, and its U is NONREGULAR CLOSED:

**Lemma 4.1 (atomless Boolean diagonal has empty interior).** For a complete atomless Boolean frame M, the diagonal sublocale Δ_B⊂B² has EMPTY ambient interior. *Proof:* every nonzero elementary open rectangle a⊠b in B² contains nonzero pairwise-disjoint subrectangles a'⊠b' with a'∧b'=0: if a∧b=0 take a'=a,b'=b; otherwise split the nonzero a∧b into two disjoint nonzero Boolean pieces. Their product rectangle is nonzero and disjoint from Δ_B. Since elementary rectangles generate O(B²), Δ_B cannot contain a nonzero ambient open. □

From Δ_B interior empty and \(U(Y)=\Delta_B\times U(X)\), int U(Y)=0 (a nonzero ambient rectangle in U(Y) would give a nonzero B²-rectangle inside Δ_B). Thus U(Y) is nonzero CLOSED with EMPTY interior, so is not regular closed; \(\boxed{d_{U(Y)}^{**}\ne d_{U(Y)}}\).

**Canonical predecessor on B(U(Y)) without any point of Y.** Under the identification \(U(Y)\cong B\times U(X)\), let \(T=B(U(Y))\). Both canonical coordinate maps \(h_Y,k_Y:T\to B\times X\) have the SAME B-coordinate map \(g:T\to B\), because U(Y) lies in the B-diagonal. The dense open cover from §2 becomes the dense open family
\[
B\times(R\times R),\qquad B\times\{(z,z)\}\quad(z\in Z)
\]
of \(B\times U(X)\). Its pullback to the Boolean locale T supplies disjoint Boolean pieces e_R,e_z covering T. As before, on the e_R piece, the two X-coordinate maps send every p-neighborhood to top (the cofinite-positive/full-real traces stay DENSE after product with B); on e_z they both evaluate at z. Thus the Boolean pasting formula (2.2) defines a frame map
\[
p_X:T\to X,\qquad p_X^*(a)\le h_X^*(a)\wedge k_X^*(a).
\]
Pair it with g:
\[
\boxed{
p=(g,p_X):T\longrightarrow B\times X=Y,
\quad
p^*(q)\le h_Y^*(q)\wedge k_Y^*(q)\quad(\forall q\in O(Y)).
}
\tag{4.3}
\]
The inequality holds on elementary product opens q=u⊠a because g is shared and p_X≤h_X,k_X; it then holds on arbitrary joins of rectangles. This is a **genuinely POINTLESS predecessor map**, since its target Y has NO ordinary points, and gives a full span whose image contains B(U(Y)) densely. Thus the generalized predecessor criterion succeeds on a NONCOMPACT, POINTLESS, NONREGULAR, RANK-ONE-STABILIZED locale.

**Provenance control:** Y was built from previously understood factors, and equality (4.2) also follows by our earlier compact-fiber theorem; this is NOT an irreducible example or an independent proof of universal Q. It IS a decisive test that (6) is meaningful in a noncompact, entirely pointless, nonregular U setting.

## 5. Synthesis, tests passed and next question

- The canonical Boolean predecessor criterion SUCCEEDS on the compact cofinite-apex W=U example, whose D density is essentially pointless; this directly tests the proposed notion where ordinary common-predecessor point pairs fail.
- It SUCCEEDS on B(W₂) of the compact two-apex W₂<U example, but fails on the two isolated offdiag Boolean atoms of B(U); this distinguishes a real finite-stage U gap in that example.
- It SUCCEEDS on B(U) of a fully pointless, noncompact, nonregular U locale with genuine rank-one W₂=U=W, formed by taking the product of the cofinite-apex example with an atomless Boolean base.
- The **generic-anchor criterion** is a new reusable sufficient class, not a known characterization. All presently tested positive cases with essential pointless closed-hull density DO have a generalized predecessor. But these are highly structured examples with obvious cofinite anchors or product factors. The test does NOT show such a predecessor is always available whenever W= W₂, or whenever W₂=U.
- The crucial barrier is now explicit: a future non-product rank-one-stabilized U whose canonical Boolean pair has NO common predecessor could exist yet still satisfy Q; such an example would falsify NECESSITY of our criterion. Conversely forcing existence of a predecessor from finite rank-one stabilization alone would solve Q. No evidence currently suffices for either direction.

**Status: new internal lemma + explicit tests, not externally audited or priority checked; universal Q,Q′ OPEN.**
