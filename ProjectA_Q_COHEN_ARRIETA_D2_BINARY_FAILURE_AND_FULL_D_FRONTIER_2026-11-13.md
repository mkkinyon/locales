# Project A — Cohen × Arrieta: an explicit D₂ failure and the surviving full-D question

> **Historical frontier status superseded later 13 Nov:** The [full fitted-diagonal Cohen×Arrieta product question](ProjectA_Q_COHEN_ARRIETA_FULL_D_PRODUCT_NEGATIVE_2026-11-13.md) has now been **answered negatively by a separate graph-complement argument** with a genuinely all-cover-compatible pair. This note's D₂ witness, slab-splitting lemma, countable-cover reduction, frame shadow calculus and category formulation remain valid, but claims here that full D is still open are historical. **Q and Q′ remain open.** The new full-D result has only internal verification so far.


**13 November 2026. Newly reconstructed internal calculations, not externally audited.** Continuation of [post-referee priorities](ProjectA_Q_POSTREFEREE_PRIORITIES_2026-11-13.md). **The remaining full-D equation D(Z_C×A)=Δ_{Z_C}×D(A) is STILL OPEN.** The present note proves a sharp **finite-D₂ failure**, reduces arbitrary product covers to countable ones, identifies a fixed-ground-cover splitting obstruction, and describes Arrieta's compact Cantor shadow. It does not infer a Q′ hole from these weak defects.

## 1. An exact localic Baire-category reformulation of Q′

For an arbitrary locale X, put W₂=cl D₂=C(d), with d the least Φ₂-fixed open, and for a full X-cover C let

\[
T_C=D_2(X)\wedge C_{X^2}(w_C),
\quad
E_C=W_2(X)\wedge O(w_C\to d).
\]

Here T_C is **relatively closed in D₂** and E_C is the corresponding relatively open hole in W₂. Since D₂ is dense in W₂, the following useful strengthening of the audited formula holds:

\[
\boxed{\operatorname{int}_{D_2}(T_C)=D_2\wedge E_C.}\tag{1.1}
\]

Indeed, for any dense sublocale D≤W and ambient closed K, an ambient open patch U satisfies D∧O(U)≤K iff W∧O(U)≤K. The forward implication uses density of D∧O(U) inside W∧O(U), and closedness of K; the reverse is immediate. Hence relative interiors commute with passage from W to the dense D in this special **closed-ambient** situation. Formula (1.1) follows from E_C=int_{W₂}(W₂∧C(w_C)).

Consequently

\[
\boxed{Q'(X)\iff
  T_C\text{ is nowhere dense as a closed sublocale of }D_2(X)
  \text{ for every full cover }C.}\tag{1.2}
\]

This is a **point-free** category assertion. Ordinary points of D₂ always lie in D, so a nonzero T_C may have **no points at all**; a usual Baire theorem applied only to the point set of X² cannot discharge (1.2). The project already knew E_C=int_{W₂}cl(T_C); (1.1)–(1.2) isolate the *relative D₂-open* interpretation requested in Session 8.

## 2. Arrieta's Cantor attachment and a Boolean-valued pair

Use Arrieta's [Construction 4.2 / Example 4.5](https://arxiv.org/pdf/2310.18522). Let C=2^ω, K_n={x∈C:x_n=1 and x_j=0 for j>n}, Y=C\setminus⋃_nK_n, and A=Y⊔ω. A basic n-neighbourhood is (V∩Y)∪{n} for Cantor-open V⊇K_n. Y is a dense Gδ; every infinite subfamily {K_n:n∈I} has dense union in C. A is countably based, Hausdorff, strongly Hausdorff, anti-Urysohn, and noncompact.

Let M=RO(C), the complete Cohen Boolean algebra; write b_n∈M for the clopen cylinder {x:x_n=1}, with complement \bar b_n. The dense trace Y⊆C gives a frame map

\[
r:O(Y)\longrightarrow M,\qquad
r(V\cap Y)=\operatorname{int}_C\overline V^{\,C}
\quad(V\text{ Cantor-open}).
\]

This is well-defined: equal traces have equal C-closures since Y is dense. It preserves finite meets and arbitrary joins with the **regular-open frame operations**. Compose with restriction O(A)→O(Y), and let σ:C→C flip every binary coordinate. Define frame maps h,k:O(A)→M by

\[
h(u)=r(u\cap Y),\qquad k(u)=\sigma^{-1}(h(u)).
\]

**Lemma 2.1.** The pair (h,k) matches **every finite cover** of A. In fact if an A-open u contains infinitely many attached points n, its trace u∩Y is dense in C: the union of the corresponding K_n is dense, and u contains a Y-neighbourhood of every such K_n. Therefore h(u)=k(u)=1. Any finite A-cover has a member containing infinitely many n, hence has matching value 1.

Now define A-opens

\[
a_n=(Y\cap\{x:x_n=1\})\cup\{n\}\quad(n\in\omega),
\qquad a_* =Y\cap\{x:x_0=0\}.
\]

They cover A (the a_n cover all attached n and every Y-point with a 1; a_* covers the all-zero Y-point). The a_n are open because K_n is contained in the nth 1-cylinder. Their Boolean values are

\[
h(a_n)=b_n,\quad k(a_n)=\bar b_n;\qquad
h(a_*)=\bar b_0,\quad k(a_*)=b_0.
\]

Thus every single member of this **countable** A-cover has h(a)∧k(a)=0, so the whole cover has matching value zero. The pair (h,k) belongs to D₂(A), but not D(A):

\[
\boxed{D(A)\subsetneq D_2(A).}\tag{2.2}
\]

This is a **weak nonclosed defect** compatible with W(A)=W₂(A)=U(A)=A². It cannot be upgraded to an open Q′-hole.

## 3. A binary Cohen × Arrieta product counterexample for D₂

Let Z_C=Loc(M), the Cohen Boolean locale. The coproduct universal property gives frame maps H,K:O(Z_C×A)→M having common Boolean-base component id_M, and fiber components h,k. Thus their pair lies in Δ_{Z_C}×D₂(A).

Form the following **binary** open cover of Z_C×A:

\[
\begin{aligned}
c_0&=\bigvee_{n\in\omega}(\bar b_n\boxtimes a_n)
                   \ \vee\ (b_0\boxtimes a_*),\\
c_1&=\bigvee_{n\in\omega}(b_n\boxtimes a_n)
                   \ \vee\ (\bar b_0\boxtimes a_*).
\end{aligned}
\]

Because b_n∨\bar b_n=1 for every n, c₀∨c₁=1. But

\[
H(c_0)=
\bigvee_n(\bar b_n\wedge h(a_n))
  \vee(b_0\wedge h(a_*))=0,
\]
\[
K(c_1)=
\bigvee_n(b_n\wedge k(a_n))
  \vee(\bar b_0\wedge k(a_*))=0.
\]

Therefore H(c₀)∧K(c₀)∨H(c₁)∧K(c₁)=0. This pair does **not** factor through D₂(Z_C×A), even though it factors through Δ_{Z_C}×D₂(A). Projection naturality supplies the opposite inclusion, so

\[
\boxed{D_2(Z_C\times A)\ \subsetneq\
       \Delta_{Z_C}\times D_2(A).}\tag{3.1}
\]

Exactly the same construction works over the **ordinary spatial Cantor base** C by using the regularization map O(C)→M as the common base component; clopen base coordinates still map to b_n. As C is compact regular, D₂(C)=Δ_C, giving

\[
\boxed{D_2(C\times A)\ \subsetneq\
       \Delta_C\times D_2(A).}\tag{3.2}
\]

This is an Arrieta analogue of the referee's Scott N4 construction. Its decisive limitation is explicit: **h,k fail an actual countable A-cover**. They are finite-compatible but not full-compatible, so (3.1)–(3.2) say **nothing negative** about the still-open D(Z_C×A)=Δ_{Z_C}×D(A).

## 4. Why coloring a fixed *full* A-cover cannot settle full D

**Lemma 4.1 (ground-cover slab splitting; arbitrary base).** Let Z,Y be any locales, C an open cover of Z×Y. Suppose there exists a Y-cover {a_i}_{i∈I} and, for each i, Z-opens z_{i,c} indexed by c∈C such that

\[
\bigvee_{c\in C}z_{i,c}=1_Z,\qquad
z_{i,c}\boxtimes a_i\le c
\quad(\forall i,c).
\]

Then

\[
\boxed{\Delta_Z\times D(Y)\le O(w_C).}\tag{4.1}
\]

Proof: test generalized endpoint maps H,K into any frame target, with common Z-component q and Y-components h,k matching all Y-covers. Then

\[
\begin{aligned}
\bigvee_{c\in C}H(c)\wedge K(c)
&\ge \bigvee_{i,c}
   q(z_{i,c})\wedge h(a_i)\wedge k(a_i)\\
&=\bigvee_i h(a_i)\wedge k(a_i)=1.
\end{aligned}
\]

In particular, **an arbitrary Boolean coloring or partition of each member of one fixed ground Y-cover is harmless at the full-D level**. The construction in §3 fails at full D for exactly this reason: its fixed ground family {a_n,a_*} already separates h,k.

For Boolean Z one may weaken the hypothesis locally: a Boolean partition of 1_Z may carry **different ground Y-covers on different cells**, provided each such cover has slabs dominated by members of C. The same calculation proves (4.1), cell by cell. Thus any full-D counterexample must evade *every such Boolean-local ground-cover uniformization*. This is a necessary obstruction, **not** a claim that its failure suffices for a counterexample.

## 5. Countable covers suffice over Cohen × Arrieta

**Lemma 5.1.** If Z has the **countable subjoin property** (every join of opens has a countable subfamily with the same join) and Y has a countable frame basis (b_i), then Z×Y has the countable subjoin property.

For any family of product opens {c_\alpha}, write each in the canonical rectangle-basis form

\[
c_\alpha=\bigvee_{i\in\omega}(u_{\alpha i}\boxtimes b_i),
\quad
u_{\alpha i}=\bigvee\{z\in O(Z):z\boxtimes b_i\le c_\alpha\}.
\]

For each fixed i choose countably many α with the same join of the u_{\alpha i}; taking their countable union over i preserves the overall product join. □

M=RO(C) has the countable subjoin property because its antichains are countable (nonzero disjoint regular opens contain distinct members of a fixed countable Cantor base). A is second-countable. Hence **every** cover of Z_C×A has a **countable** subcover, and the full-D product equation needs checking only for countable product covers. This is an exact reduction, not a finite reduction: the witness in §2 is countable and not reducible to finite compatibility.

An arbitrary product cover can therefore be encoded by a **countable Boolean coefficient matrix** (u_{ni})_{n,i∈ω} relative to a countable A-basis. The original SDω argument would choose one Boolean partition simultaneously deciding the labels across all basis columns. Cohen's algebra does not supply that countable common refinement. Arrieta-specific geometry must replace that unavailable step.

## 6. Arrieta's compact Cantor shadow: precise reach and failure

Each A-open u is determined by its Y-trace v=u∩Y and its attached-point set I=u∩ω. Define its maximal Cantor-open **shadow**

\[
s(v)=C\setminus\overline{Y\setminus v}^{\,C},
\qquad N(v)=\{n:K_n\subseteq s(v)\}.
\]

One has s(v)∩Y=v; the A-openness condition is exactly I⊆N(v). Therefore, as a frame presented by pairs,

\[
\boxed{
O(A)=\{(v,I):v\in O(Y),\ I\subseteq N(v)\},
}\tag{6.1}
\]

with finite meets and arbitrary joins computed componentwise. (The set N(v) is monotone in v and preserves finite meets; it need not preserve arbitrary joins.)

If {(v_j,I_j)} is an A-cover, then the Cantor opens {s(v_j)} cover C: they cover Y by ∨v_j=Y, and each x∈K_n belongs to some shadow because n∈I_j for at least one cover member j. Since C is compact, **finitely many shadows cover C**.

But this is emphatically **not** a finite subcover of A. For the standard countable A-cover {Y}∪{N_n:n∈ω}, the single open Y has shadow s(Y)=C yet misses every attached n. Thus naive compact-fiber transfer through Cantor shadows would be invalid. The missing mathematical step is control of the **attached-index remainder** after selecting finite shadows, and doing so uniformly over the Cohen base.

## 7. Where this leaves the full-D problem and the Q′ category idea

1. The binary D₂ failure over Cohen × Arrieta is now explicit, but it cannot answer the all-cover D-product question; a full-compatible h,k would already match the countable ground cover used in §3.
2. There are only **countably many** cover members to consider after reduction, and a fixed ground A-cover with any Cohen-dependent color assignment is harmless. A negative D example must use a genuinely Cohen-dependent **new fiber cover** that cannot be Boolean-locally reduced to a ground-cover slab splitting.
3. The Cantor shadow furnishes finite compact control on the **Y geometry**, but leaves infinitely many attached n uncontrolled. That remainder is a concrete place to test both a positive transfer lemma and a negative Cohen-coded cover.
4. The category reformulation (1.2) reminds us not to confuse any such nonclosed D or D₂ failure with Q′. An actual Q′ counterexample requires a **nonzero open piece** of the finite fitted relation killed by a full cover. The Arrieta and Scott controls show this distinction is essential.

**Recommended next bounded question:** Given a *countable* cover C of Z_C×A, after selecting finite Cantor shadows on a nonzero Boolean patch, can one prove that the remaining attached-index cover contributions are matched by **every** full-A-compatible pair h,k? An answer must work with the actual product cover and its Boolean coefficient matrix, not only with the set-theoretic Cantor shadow. No claim of such a lemma is made yet.

**Provenance:** Original Arrieta topology and anti-Urysohn proof are from Arrieta's published construction. The explicit h,k witness, binary D₂ products, fixed-cover slab lemma, countable reduction, frame shadow presentation, and relative category identity are internally derived in this note. They have not undergone an independent referee audit.
