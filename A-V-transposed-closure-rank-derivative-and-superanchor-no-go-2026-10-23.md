# Project A — Transposed-closure rank calculus and the super-anchor no-go

Date: 23 October 2026. **New working theorem package, proofs given here.** The proper graph-null bar q in the audited two-index noncofinite bridge construction has hereditary exact rank 4 and yields V3 strictly above V4. This note develops the requested topological closure calculus to test rank 5 and proves a no-go for the naive third-level super-anchor. **It does not construct V4>V5.** The claims here are separate from Claude's audited theorem and deserve independent verification before promotion.

## 1. Graph-null leaf calculus

Let X be a topological space with disjoint OPEN rational-sheet copies L0={ell_t:t∈Q}, R0={r_t:t∈Q}, and let g:Q→X×loc X send t↦(ell_t,r_t). For nonempty open J⊆Q, q_J is the largest open in O(X)⊕O(X) null under the graph g restricted to J, and S_J=D∪B_(q_J), the lower family of disjointness and q_J rectangle leaves.

For u∈O(X), set
   u^L_J = {r_t:t∈J and ell_t∈u} ⊆R0,
and for v set
   v^R_J = {ell_t:t∈J and r_t∈v} ⊆L0.
These are OPEN in X. The leaf condition is
   (u,v)∈S_J  iff  u∩v=∅ OR v∩u^L_J=∅.
The second condition exactly means u_L∩v_R∩J=∅, i.e., (u,v) is graph-null.

Define closed, monotone maps O(X)→Closed(X):
   K^L_J(u)=cl_X(u)∩cl_X(u^L_J),
   K^R_J(v)=cl_X(v)∩cl_X(v^R_J).

**FIBER LEMMA:**
   (u,v)∈V(S_J)  iff v∩K^L_J(u)=∅;
   (u,v)∈H(S_J)  iff u∩K^R_J(v)=∅.
Proof: for fixed u, a permitted second open v is disjoint from u or from u^L_J; the union of all such v is u*∨(u^L_J)* = X\(cl u∩cl u^L_J). The vertical join condition is precisely v≤that union. Symmetrically for H. No spatiality of the localic square.

## 2. A single closed-set recursion for every finite rank

For ANY monotone map K:O(X)→Closed(X), define
   (T K)(b) = X \ ⋃{a∈O(X): b∩K(a)=∅}.
Here b is an open, and T K(b) is CLOSED. Equivalently:
   x∈(T K)(b) iff every neighborhood a of x meets the condition b∩K(a)≠∅.
(The second expression means: for all a∋x, b∩K(a)≠∅; it does not require x∈K(a).)

The operator T preserves pointwise inclusions and monotonicity in the open argument:
   K≤K' ⇒ T K≤T K';
   b≤b' ⇒ T K(b)⊆T K(b').

By induction on the number of alternating H/V closures,
   (a,b)∈V(S_J) iff b∩K^L_J(a)=∅;
   (a,b)∈H(V(S_J)) iff a∩(T K^L_J)(b)=∅;
   (a,b)∈V(H(V(S_J))) iff b∩(T² K^L_J)(a)=∅;
   (a,b)∈H(V(H(V(S_J)))) iff a∩(T³ K^L_J)(b)=∅.
The opposite orientation begins with K^R_J, with H and V exchanged.

For every integer n≥1,
   **rk(q_J)≤n iff (T^(n-1) K^L_J)(1)=∅ OR (T^(n-1) K^R_J)(1)=∅**.
Here 1 denotes the open X. This uses the alternating normalization of arbitrary mixed trees: if R0=S and R_(n+1)=H(R_n)∪V(R_n), then R_n is contained in (and in fact equal to) the union of the two n-stage alternating closures. One can prove this inductively since H and V are extensive, monotone, idempotent and each (n−1)-stage alternating closure lies in BOTH n-stage closures, allowing outer closure to absorb arbitrary mixtures. All statements are about covers in O(X), not point sets of X×loc X.

Hence **rank>4 is equivalent to both closed sets**
   (T³ K^L_J)(1), (T³ K^R_J)(1)
being NONEMPTY. Rank>5 requires both T⁴ bad sets nonempty. These tests are exact even if q_J has no well-founded bar certificate; finite rank is the tested property.

**TWO-PARITY DESCENT:** T²K≤K for every monotone closed-valued K. Indeed if b⊆X\K(a) is open, then a⊆X\(T K)(b), since a itself is eligible in T K(b). Such b cover X\K(a), so X\K(a)⊆X\(T²K)(a). By monotonicity of T,
   K≥T²K≥T⁴K≥⋯,
   T K≥T³K≥T⁵K≥⋯.
These descending closed-set chains provide an intrinsic analogue of an alternating proof-search derivative.

**COUNTABLE BASIS:** If B is a topological basis of X, then
   (T K)(b)=X\⋃{a∈B:b∩K(a)=∅}.
To see this, whenever an arbitrary open a is eligible, every basic subopen a'⊆a is also eligible because K is monotone. Thus no non-basic opens are needed in the union. When X is countable first countable, it is second countable: union countable local bases. All finite tree ranks are consequently encoded by repeated countable basis tests on the K-functions; this holds WITHOUT assuming the localic square spatial.

**HEREDITARY TEST IN THIS LANGUAGE:** A graph-null bar q yields j_n(q)=q provided for every nonempty basic parameter interval J BOTH sets
   (T^(n-1)K^L_J)(1), (T^(n-1)K^R_J)(1)
are nonempty. If q has rank≤n+1, this gives strict V_n⊋V_(n+1). If both stay nonempty for every finite n and every J and q remains a bar, this gives V_fin≠V. The existence of such a q is OPEN.

## 3. A pointwise necessary condition for graph-null barhood

**PAIRWISE LEAF NECESSITY.** If q is a genuine bar (q∨d_I=1 in the localic square), then for every pair of ORDINARY points x,y∈X there are open neighborhoods U∋x,V∋y such that EITHER
    U∩V=∅
OR U_L∩V_R=∅.
Proof: evaluate the localic equation at the product point (x,y), and use that both d_I and q are joins of their canonical disjointness / graph-null rectangles. This is necessary, not sufficient for localic barhood.

This simple constraint is particularly important when trying to add accumulation points: a proposed rank-raising topology can make the graph-null open cease to be a bar, even if its lower-rank tests fail spectacularly.

## 4. Super-anchor no-go, independent of Hausdorffness

Work in one fixed tower k of the independently audited two-index rank-four construction. Write t=t_k; the lower z_(m,l) have left and right attachment coordinates alpha_(m,l), beta_(m,l)→gamma_m as l→∞ for fixed row m, and every t-neighborhood contains some T_N with ALL z_(m,l) and rational traces A_(m,l),B_(m,l) for m,l≥N.

Its RIGHT anchors y_m have right attachment coordinate beta(y_m)=gamma_m.

**NO-GO THEOREM.** Suppose one enlarges the space, retaining the original neighborhoods of t and the right-anchor rational traces, by a new ordinary point s such that every neighborhood W of s contains y_m for arbitrarily large m. Then the largest null open q for the unchanged rational graph g CANNOT be a bar.

Proof. Fix ANY neighborhoods U∋t and W∋s. Take N with T_N⊆U and choose m≥N with y_m∈W. Since W is open at y_m and beta(y_m)=gamma_m, its right-sheet trace W_R contains a rational interval J around gamma_m. For l sufficiently large, alpha_(m,l),beta_(m,l) lie in J and l≥N. The t-open U contains rational left/right traces around alpha_(m,l),beta_(m,l), hence U_L∩W_R ≠∅ and U_R∩W_R ≠∅.

The first intersection prevents U⊠W from being graph-null. The second gives U∩W≠∅, preventing a disjointness leaf. Since U,W were arbitrary, the ordinary pair (t,s) lies in neither q nor d_I. Evaluating at (t,s) yields q∨d_I<1. QED.

The symmetric claim holds if one adds a new point whose every neighborhood contains arbitrarily far-out LEFT anchors x_m with alpha(x_m)=gamma_m: the problematic point pair is then (s,t), with the graph orientation transposed.

**SIGNIFICANCE:** Dropping Hausdorffness does NOT rescue the naive rank-five plan of adding a point converging to cofinal tails of the existing anchors. It destroys the very bar required for the fitted-stage argument. This is stronger than the earlier proof that such a super-anchor would spoil Hausdorff separation between s and t. It does NOT rule out a more intricate noncofinite construction with moving witnesses across multiple towers, or a different graph/polarity.

## 5. Compact-escape / variable-witness lemma

Fix ANY topological X and ANY bar q (not necessarily graph-null), and set S=D∪B_q. Since q∨d_I=1, the canonical leaves pointwise cover X×X.

For any compact subset K⊆X and ordinary y∈X, for each x∈K choose a leaf (u_x,v_x)∈S with x∈u_x,y∈v_x. Finitely many u_x cover K; intersect the corresponding finitely many v_x to obtain a neighborhood b of y. Then each of the finitely many u_x remains an S-leaf against b, so
   K⊆⋃{u:(u,b)∈S}⊆⋃{u:(u,b)∈V(S)}.
Thus for every compact K and y, some neighborhood b_y satisfies K⊆G(b_y), where G(b)=⋃{u:(u,b)∈V(S)}.

Consequently, if a first-root open a and a point y provide a BAD witness to an H-first rank-four certificate, namely
   for every b∋y, a is NOT contained in G(b),
then the offending points x_b∈a\G(b) cannot be confined to any fixed compact subset of a: for every compact K⊆a some b∋y satisfies K⊆G(b). In particular no FIXED ordinary point x can witness failure for every b∋y. This is the exact quantifier reason the naive attempt to take x=t as the third-level obstruction must fail if q is a bar.

The analogous statement with H/V transposed holds for V-first rank-four failure. It sharpens the instruction for rank-five construction: it must involve genuinely moving noncompact witness clouds as b shrinks, not a fixed upper point or compact collection of anchors.

## 6. What remains

For a genuine V4⊋V5 graph construction the two orientation bad sets
   (T³ K^L_J)(1), (T³ K^R_J)(1)
must remain nonempty for every nonempty rational interval J; a proper q needs an actual finite-height≤5 (or otherwise well-founded) C-ideal bar certificate. A hereditarily exact rank-five example requires both T⁴ bad sets to be empty in some orientation, while T³ remain nonempty in both, for EVERY interval J.

The direct super-anchor variant is impossible even for non-Hausdorff spaces (no-go theorem above). The next viable possibility must distribute the rank-four obstructions across DIFFERENT towers so that no fixed pair of ordinary points violates the pairwise barhood condition. Another possibility is to abandon the single-valued rational graph in favor of a non-graph relation, while preserving a concrete hereditary rank witness.

No claim of V4>V5 or negative answer to Question A is made.
