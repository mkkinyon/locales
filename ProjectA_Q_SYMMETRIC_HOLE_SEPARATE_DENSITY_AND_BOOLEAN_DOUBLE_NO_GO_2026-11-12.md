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

**Important editorial correction.** The earlier normal-form paper and referee packet emphasized only “jointly zero-reflecting” and cautioned that this does not *in general* imply separate zero reflection. That logical warning is correct for arbitrary frame-map pairs. But **for the canonical symmetric E, the stronger separate property DOES hold**. No previously established theorem fails; the previous statement was unnecessarily weak. The *canonical weak fitting-defect sublocale* T_C is ALSO symmetric; see §2.5. Separate reflection therefore holds for its Booleanization after support reduction as well.

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

### 2.5 Canonical WEAK defects are symmetric too — the decisive adversarial observation

The same argument applies directly to the **canonical weak fitting-defect sublocale**
\[
T_C=\mathcal D_2(X)\wedge\mathfrak c_{X^2}(w_C)\ne0
\]
whenever \(\mathcal D_2(X)>\mathcal D(X)\). Both D₂ and \(\mathfrak c(w_C)\) are swap-invariant, so **T_C itself is symmetric**, and its Booleanization B(T_C) is invariant. Thus the two coordinate frame maps on \(O(B(T_C))\) have equal zero ideals. After passing to their least closed coordinate support K, **each** separately reflects zero and **every** nonzero K-clopen u has
\[
T_C\wedge O(u\boxtimes u)\ne0.
\]
All of the symmetry, separate support and clopen-square recurrence assertions therefore hold for canonical WEAK defects too. They are **not signs that the defect is relatively open in W₂**.

**Corrected scope:** The earlier sentence that an “unsymmetrized chosen T_C” may require the doubling trick was too weak/misleading. **For the canonical T_C of (2.5), no doubling is necessary.** The separate Boolean-doubling theorem below serves to show the stronger fact that **arbitrary noncanonical** Boolean-valued fitting witnesses can be symmetrized. The completed branching Scott control supplies canonical symmetric weak T_C while W=W₂=U. This is the cleanest anti-drift falsification check.

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

## 5. Genuine Urysohn control: infinite product-box complexity can coexist with POSITIVE rank-one stabilization even off inseparability

The preceding Boolean doubling is a WEAK fitting control. There is also a useful **genuine rank-one Urysohn** control against over-interpreting infinite product-box rank.

Let \(H=2^\omega\) be Cantor space, a compact perfect zero-dimensional Hausdorff space. Let \(P\) be the finite six-point upper-Alexandrov poset
\[
0<5>1<4>2<3
\]
(with its transitive closure and no other comparabilities). It is finite coherent and sober, and its relations satisfy
\[
W(P)=U(P)>I(P).
\]
Specifically the pair (0,4) has NO common upper bound, so is outside \(I(P)=\operatorname{cl}\Delta_P\), but the closures of the basic opens ↑0={0,5} and ↑4={4} meet at 1, so (0,4) belongs to U(P).

Set \(X=H\times P\), a **compact**, locally compact sober locale with spatial square. Ordinary product-neighborhood closure gives
\[
\boxed{U(X)=\Delta_H\times U(P),\qquad I(X)=\Delta_H\times I(P)}
\tag{5.1}
\]
with coordinates permuted to \(H^2\times P^2\).

**Claim 5.1 (a genuine positive Q instance).**
\[
\boxed{D_2(X)=D(X),\quad W(X)=W_2(X)=U(X).}
\tag{5.2}
\]
The first equality is trivial from COMPACTNESS of X: any cover has a finite subcover. For the W equality there is an independent dense-point argument: the common-specialization-predecessor pairs \(C_P=\{(p,q):\exists t\le p,q\}\) are dense in U(P) because the finite coherent P satisfies \(W(P)=U(P)\). The **actual point pairs** \(((h,p),(h,q))\), with h∈H and (p,q)∈C_P, belong to D(X), by the common predecessor (h,t). They are dense in U(X)=Δ_H×U(P): any nonempty relative basic open chooses a nonempty H-open neighborhood around h and a nonempty U(P) neighborhood, each of which contains such a point. Hence closure of D(X) is all U(X). No blanket product-preservation theorem for D is needed.

**Claim 5.2 (nontrivial off-inseparability boundary, nowhere finite-box).** Because H has NO isolated points,
\[
\operatorname{int}_{X^2}U(X)=0,\qquad
G_\perp=U(X)\wedge O(d_{I(X)})\ne0
\tag{5.3}
\]
(the pair ((h,0),(h,4)) lies in G_perp for every h). Yet for EVERY rectangle r with nonzero \(U(X)\wedge O(r)\), that relatively open restriction has **INFINITE product-box rank**: it cannot be a finite join of genuine product sublocales \(S_i\times T_i\le U(X)\wedge O(r)\).

*Proof.* A nonzero product sublocale \(S\times T\le U(X)\) is forced into a single Cantor fiber \(\{h\}\times P\) on BOTH coordinate factors. To see this without relying on ordinary points of S or T, take their nonzero H-coordinate projections and their nonempty CLOSED image supports A,B⊂H. If x∈A and y∈B are distinct, choose disjoint clopen H-neighborhoods u∋x and v∋y. The respective restrictions of S and T to u×P and v×P are both nonzero (since x,y lie in their closed image supports), and the product of two nonzero locales is nonzero. But \(U(X)\) has no point, indeed no sublocale, on the mixed clopen rectangle \((u\times P)\boxtimes(v\times P)\): this is a far rectangle. Contradiction. Thus A×B lies on the diagonal of H² and, with A,B nonempty, A=B={h}. Each S_i×T_i is therefore supported over one Cantor fiber h_i.

On the other hand any nonzero relatively open \(U(X)\wedge O(r)\) contains ordinary pairs for ALL h in a nonempty H-open set (the H-coordinate intersection of the sides of r). Cantor's no-isolated-point property makes that set infinite. It cannot be covered as a localic sublocale by finitely many fiber-supported product boxes. □

This control is **stronger than the trivial perfect-Hausdorff diagonal example**: \(G_\perp\) is genuinely NONZERO because U(P)>I(P), and U is globally nonregular closed because its ambient interior is zero, even while Q holds. Thus the earlier locally finite-box sufficient theorem is not close to a characterization of Q. **Genuine Urysohn geometry supports infinite product-box complexity in every nonzero open part of its exceptional sector WITHOUT any rank-one defect.** A proof of Q must allow **fibered-diagonal pieces** \(\Delta_H\times R\), not merely finite sums of ordinary products \(S\times T\).

**Provenance:** The finite coherent \(W(P)=U(P)\) and the finite-fence pair (0,4) occur in earlier Project A records; the product-density argument above is supplied independently. This is a deliberate *control* of our strategy, not a new counterexample or an originality claim. A direct enumeration of the finite P relation checks \(|C_P|=20\), \(|I(P)|=20\), and \(|U(P)|=|\operatorname{cl}C_P|=32\) of the 36 pairs, including \((0,4)\in U(P)\setminus I(P)\).

## 6. Summary and stop rule

**Genuine strengthening:** The least closed support of a canonical symmetric pre-nucleus hole is the least closed support of EACH coordinate. Both projections from B(E) and E into K are individually dense. The same marked strong hole persists nontrivially in the square of every nonzero clopen part of K (Q′), and in every clopen part of the ORIGINAL Q-counterexample meeting K (Q).

**Algebraic no-go:** Any weak Boolean fitting defect can be symmetrized and doubled so as to have symmetry, separate zero-reflection, atomlessness, zero C matching, and clopen-square recurrence. The involution also admits a Boolean fundamental half, which is just the orientation of the two copies. **No universal Q or Q′ proof can follow from this algebraic package alone.** The missing ingredient must remain the **NONZERO RELATIVELY OPEN density** of the canonical witness in W₂/U, plus cover geometry at that open level.

**Next bounded test:** Determine whether relatively open density can promote the Boolean orientation (4.2) to an actual finite *ambient-open* separation in some nontrivial class (e.g. complemented/zero-dimensional local bases or fiberwise factors), not whether the orientation exists abstractly. Be prepared to stop if that lifting reduces to the previously proved zero-dimensional patching theorem.

**Status: new internal proof, not independently refereed; Q/Q′ OPEN.**
