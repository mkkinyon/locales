# Project A — The symmetric Q/Q′ hole: individually dense endpoints, clopen self-locality, and an exact Boolean-doubling no-go

**12 November 2026 — NEW INTERNAL strengthening of the externally reviewed canonical support theorem, with an adversarial negative control. Neither Q nor Q′ is solved.** This continuation explicitly tests the previous target: whether *full joint coordinate support*, combined with *local rank-one stabilization* and the far-rectangle formula, forces something beyond finite-cover compatibility. The answer is **yes for the canonical symmetric hole's geometric support**, but **no for bare Boolean-valued pair algebra**. Its symmetry upgrades joint zero-reflection to **SEPARATE zero-reflection** and proves recurrence in the square of **EVERY nonzero clopen sublocale** of the support. On the other hand, every arbitrary weak fitting defect can be doubled to satisfy all these symmetry-level algebraic properties, so one cannot deduce Q merely from them. The precise nonformal ingredient is still the Boolean witness's density in a **nonzero relatively OPEN Urysohn/finite-closed-hull hole**.

## 0. The setup and the unnoticed symmetry

For \(L=O(X)\), \(Q=L\oplus L=O(X^2)\), let
\[
w_C=\bigvee_{c\in C}c\boxtimes c,\quad
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\quad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]
Put \(d_0=d_{W_2(X)}=\Phi_2^\infty(0)\) and \(W_2=C_{X^2}(d_0)\). The closed hull \(W_2\) is symmetric under the coordinate-swap \(\tau:X^2\to X^2\), since the finite diagonal-cover squares are symmetric. Fix any bad C with
\[
\rho_C=w_C\to d_0>d_0,\qquad E_C=W_2\wedge O_{X^2}(\rho_C)\ne0.
\tag{0.1}
\]
Both \(w_C\) and \(d_0\) are swap-invariant, hence \(\rho_C\) and **E_C are swap-invariant**. (Heyting implication is invariant under frame isomorphisms.)

Let \(B(E)\) be the Isbell least dense Boolean sublocale of E, \(M=O(B(E))\), and \(h,k:L\to M\) the two coordinate maps. Isbell Booleanization is canonical under locale isomorphisms, so swap restricts to \(B(E)\), inducing a COMPLETE Boolean automorphism \(\alpha:M\to M\), \(\alpha^2=\mathrm{id}\). It satisfies
\[
\boxed{k=\alpha\circ h,\qquad h=\alpha\circ k.}
\tag{0.2}
\]
The pair matches all finite covers to \(1_M\), and C to 0.

## 1. Separate coordinate-support theorem: the conjunction in the original formula is redundant

**Theorem 1.1 (individually dense canonical endpoints).** Let \(K=C_X(e)\) be the previously defined least CLOSED joint coordinate support of E, where
\[
e=p_{1*}(\rho_C\to d_0)\wedge p_{2*}(\rho_C\to d_0)
=\bigvee\{a:h(a)=k(a)=0\}.
\tag{1.1}
\]
Then the two coordinate zero ideals are actually IDENTICAL, and
\[
\boxed{
p_{1*}(\rho_C\to d_0)=p_{2*}(\rho_C\to d_0)=e
=\bigvee\{a:h(a)=0\}
=\bigvee\{a:k(a)=0\}.
}
\tag{1.2}
\]
Consequently the induced maps \(h_K,k_K:O(K)=\uparrow e\to M\) BOTH separately reflect zero:
\[
\boxed{h_K(v)=0\iff v=0_K\iff k_K(v)=0.}
\tag{1.3}
\]
Equivalently, **each projection \(B(E)\to K\) is individually dense**; the same holds for the coordinate projections \(E\to K\) in the sense that every nonzero K-open has nonzero inverse image.

*Proof.* From (0.2), \(\alpha\) preserves zero, so \(h(a)=0\iff k(a)=0\) for every a∈L. The formerly joint zero ideal is therefore EACH coordinate zero ideal. The adjoint characterization in the independently reviewed theorem identifies their generators as the two p_{i*} values, proving (1.2). If \(v\ge e\) in \(O(K)\) and \(h_K(v)=0\), then v≤e by (1.2), hence v=e, the bottom of O(K). Ditto k. Density of the projections is precisely zero-reflection by their inverse-image frame maps. □

**Important editorial correction.** The earlier normal-form paper and referee packet emphasized only “jointly zero-reflecting” and cautioned that this does not *in general* imply separate zero reflection. That logical warning is correct for arbitrary frame-map pairs. But **for the canonical symmetric E, the stronger separate property DOES hold**. No previously established theorem fails; the previous statement was unnecessarily weak. The *weak fitting-defect* normalization from an unsymmetrized chosen T_C need NOT have this property until it is symmetrized as in §3.

## 2. Every nonzero clopen region contains a genuine square of the SAME marked hole

**Lemma 2.1 (clopen equality for finite-compatible pairs).** If \(u\) is complemented in any frame L, then for finite-compatible h,k:L→M,
\[
\boxed{h(u)=k(u).}
\tag{2.1}
\]
Indeed the finite cover \(\{u,\neg u\}\) has matching value 1; writing p=h(u),q=k(u), the equation \(1=p\wedge q\vee\neg p\wedge\neg q\) forces p=q, even if the target M is not Boolean (h,k preserve the chosen complements). This was already recorded in our October synthesis.

**Theorem 2.2 (clopen-square recurrence).** On the normalized K from Theorem 1.1, for EVERY nonzero complemented \(0_K\ne u\in O(K)\),
\[
\boxed{
E\wedge O_{K^2}(u\boxtimes u)\ne0.
}
\tag{2.2}
\]
*Proof.* By Lemma 2.1, \(h_K(u)=k_K(u)\). By separate zero-reflection, this common element is NONZERO. Hence its meet with itself, the inverse image of \(u\boxtimes u\) along the map \(B(E)\to K^2\), is nonzero. Thus E∧O(u⊠u)≠0. □

**Corollary 2.3 (clopen hereditary Q′ self-locality).** Every nonzero CLOPEN SUBLOCALE \(K_u=O_K(u)\subseteq K\) is itself a Q′ counterexample for the SAME restricted bad cover:
\[
\boxed{W_2(K_u)>W(K_u).}
\tag{2.3}
\]
The subhole \(E_u=E\wedge O(u\boxtimes u)\) is a nonzero relatively open part of W₂(K_u), disjoint from W(K_u); its least closed support in \(K_u\) is all of \(K_u\), and each coordinate of its Booleanization zero-reflects.

*Proof.* A clopen locale inclusion is simultaneously OPEN and CLOSED, so the closed-heredity theorem gives \(D_\varepsilon(K_u)=D_\varepsilon(K)\wedge K_u^2\) for ε=finite/full, and the OPEN restriction commutes with ambient closure:
\(W_\varepsilon(K_u)=W_\varepsilon(K)\wedge K_u^2\). Apply (2.2) and the existing marked-hole persistence \(E\le W₂(K)\), \(E\wedge W(K)=0\). Since every nonzero K_u-open v is also a K-open ≤u, separate zero-reflection of the restricted coordinate maps (or the relative density of B(E_u)) makes the least closed support of E_u equal to K_u. □

**Corollary 2.4 (clopen hereditary Q in the ORIGINAL locale).** Suppose X hypothetically violates Q, so W₂(X)=U(X)>W(X), and K is the least closed support of a canonical Q-hole E. For every clopen \(u\in O(X)\) with \(K\wedge O_X(u)\ne0\), the clopen sublocale \(X_u=O_X(u)\) itself violates Q:
\[
\boxed{W_2(X_u)=U(X_u)>W(X_u).}
\tag{2.4}
\]
Indeed the trace u|K is nonzero, so E∧O(u⊠u)≠0 by (2.2). Both W and W₂ restrict exactly to a clopen square; U likewise restricts exactly along clopen inclusions, because far opens in the clopen summand extend to far opens in X by adjoining the complemented exterior. Thus the global finite rank-one equality IS inherited by COPEN (not arbitrary closed) sublocales, and the genuine hole persists.

**Clopen finite-partition form.** If \(1_K=\bigvee_{i=1}^n u_i\) is a finite disjoint clopen partition, then \(E\le U(K)\) cannot meet \(u_i\boxtimes u_j\) for i≠j, since their factors are separated by a complemented cut and hence form a FAR rectangle. Thus
\[
\boxed{
E=\coprod_{i=1}^n(E\wedge O(u_i\boxtimes u_i)),
\quad\text{each summand nonzero if }u_i\ne0_K.
}
\tag{2.5}
\]
This is stronger than just nonzero intersections with separate one-coordinate strips, although it does NOT force a bounded chromatic graph on any summand.

## 3. No-go: every weak Boolean witness can be made equally symmetric and individually supported

**Theorem 3.1 (Boolean doubling).** Let \(u,v:L\to N\) be ANY frame homomorphisms to a nonzero complete Boolean algebra N, matching EVERY finite cover to 1 and SOME full cover C to zero. Define
\[
M=N\times N,\qquad h(a)=(u(a),v(a)),\quad k(a)=(v(a),u(a)).
\tag{3.1}
\]
Let \(\alpha:M\to M\) exchange the two factors. Then
\[
k=\alpha h,\quad h=\alpha k,\qquad
\bigvee_{c\in F}h(c)\wedge k(c)=1_M\text{ for every finite cover }F,
\quad
\bigvee_{c\in C}h(c)\wedge k(c)=0_M.
\tag{3.2}
\]
Moreover, if u,v are **jointly zero-reflecting** on L, then h,k are EACH separately zero-reflecting. If they are jointly zero-reflecting only after reducing to a least closed support K, the same doubling there yields **all the algebraic properties** of Theorems 1.1 and 2.2 on K (including clopen-square nonvanishing).

*Proof.* All equations are coordinatewise. For any a, h(a)=0_M iff u(a)=v(a)=0_N; k(a)=0_M has the same criterion. Finite/full matching equations evaluate in M as two copies of the corresponding N equation. For any nonzero complemented a, finite compatibility forces u(a)=v(a), so h(a)=k(a) is a nonzero diagonal pair after support normalization, verifying clopen-square recurrence. □

**Concrete negative control:** Take the nonempty finite/infinite partial-function completed branching Scott locale S, and the earlier maps \(u=h_+,v=h_-:O(S)\to\operatorname{RO}(2^\mathbb N)\), finite-cover-compatible but matching the singleton-literal cover to zero. Every nonzero Scott-open contains a nonempty finite basic condition; both u and v assign that condition a nonzero Cantor cylinder, so each is already zero-reflecting on S. The doubled h,k are symmetric, each zero-reflecting, with C matching zero. Yet
\[
\boxed{W(S)=W_2(S)=U(S)=S^2.}
\tag{3.3}
\]
Therefore **symmetry plus separate zero-reflection plus finite compatibility plus maximal cover failure are insufficient to imply Q′ or Q failure**: the strong hole must additionally be relatively OPEN in W₂/U. This is a decisive falsification test against a purely pair-algebra solution.

## 4. Boolean orientation of the canonical involution: free, but not a new constraint

For the canonical symmetric E, define \(a_c=h(c)\in M\). Since the full C matching value is zero,
\[
a_c\wedge\alpha(a_c)=h(c)\wedge k(c)=0\quad(\forall c\in C),
\qquad \bigvee_{c\in C}a_c=1_M.
\tag{4.1}
\]

**Lemma 4.1 (Boolean fundamental half; classical choice).** There exists \(b\in M\) such that
\[
\boxed{b\wedge\alpha(b)=0,\qquad b\vee\alpha(b)=1.}
\tag{4.2}
\]

*Proof.* Let S={b∈M:b∧αb=0} with the usual order. Every chain has a join in S (for any two chain members one is ≤the other, so all cross meets with α vanish). By Zorn choose maximal b. If \(r=\neg(b\vee\alpha b)>0\), then αr=r. Since \(\bigvee a_c=1\), some \(d=r\wedge a_c>0\). It obeys \(d\wedge\alpha d=0\) by (4.1), and lies under r disjoint from b∨αb. Thus b∨d is a strictly larger S-element, contradiction. Hence r=0. □

**Proposition 4.2 (the symmetric witness is two oriented copies of an arbitrary witness).** Put \(N=M\downarrow b\), the complete Boolean interval with top b. The frame isomorphism
\[
\Theta:M\overset{\cong}{\longrightarrow}N\times N,\qquad
\Theta(m)=(b\wedge m,\ b\wedge\alpha(m))
\tag{4.3}
\]
conjugates α to coordinate-swap. With
\[
u(a)=b\wedge h(a),\qquad v(a)=b\wedge k(a)\in N,
\]
one has
\[
\Theta(h(a))=(u(a),v(a)),\qquad
\Theta(k(a))=(v(a),u(a)).
\tag{4.4}
\]
Both u,v are frame maps, compatible with finite covers and incompatible with the chosen C. They are jointly zero-reflecting on K exactly when h,k separately zero-reflect on K.

**Interpretation:** The Boolean orientation (4.2) is canonical only up to a noncanonical maximal choice and belongs to B(E), not necessarily to the ambient open E or a coordinate clopen of K. In fact every coordinate clopen t∈O(K) has h(t)=k(t)=αh(t), while an orientation b satisfies αb=¬b. Thus **no nontrivial Boolean orientation can be the image of a coordinate clopen**. There is NO general method here to lift the chosen Boolean half to a FINITE cover of K, and the Scott doubled-pair control proves that orientation itself is not the missing argument for Q.

## 5. Summary and stop rule

**Genuine strengthening:** The least closed support of a canonical symmetric pre-nucleus hole is the least closed support of EACH coordinate. Both projections from B(E) and E into K are individually dense. The same marked strong hole persists nontrivially in the square of every nonzero clopen part of K (Q′), and in every clopen part of the ORIGINAL Q-counterexample meeting K (Q).

**Algebraic no-go:** Any weak Boolean fitting defect can be symmetrized and doubled so as to have symmetry, separate zero-reflection, atomlessness, zero C matching, and clopen-square recurrence. The involution also admits a Boolean fundamental half, which is just the orientation of the two copies. **No universal Q or Q′ proof can follow from this algebraic package alone.** The missing ingredient must remain the **NONZERO RELATIVELY OPEN density** of the canonical witness in W₂/U, plus cover geometry at that open level.

**Next bounded test:** Determine whether relatively open density can promote the Boolean orientation (4.2) to an actual finite *ambient-open* separation in some nontrivial class (e.g. complemented/zero-dimensional local bases or fiberwise factors), not whether the orientation exists abstractly. Be prepared to stop if that lifting reduces to the previously proved zero-dimensional patching theorem.

**Status: new internal proof, not independently refereed; Q/Q′ OPEN.**
