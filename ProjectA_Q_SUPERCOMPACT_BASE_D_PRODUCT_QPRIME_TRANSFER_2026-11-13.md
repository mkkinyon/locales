# Project A / Q′ — supercompact-open bases and exact full-D product transfer

**13 November 2026. New working proof; internally checked, NOT independently audited.** Continuation after the externally reviewed Cohen × Arrieta product failure and [post-referee consolidation](ProjectA_Q_COHEN_ARRIETA_ONE_BIT_AND_SECTION_RIGIDITY_CANONICAL_2026-11-13.md). Q and Q′ remain universally open.

## 1. A supercompact-open cover

Let \(Z\) be a locale. Call a nonzero open \(p\in\mathcal O(Z)\) **completely join-prime** (supercompact as a frame element) when
\[
  p\le\bigvee_{i\in I}a_i\ \Longrightarrow\
  p\le a_i\text{ for some }i.
\]
Suppose a family \(\mathscr B\) of such opens **covers** \(Z\):
\(\bigvee_{p\in\mathscr B}p=1\). This includes all upper-Alexandrov locales (the principal opens \(\uparrow z\) do the job), the Sierpiński locale (indeed \(1\) is completely join-prime), and finite coproducts of such bases.

Every \(p\in\mathscr B\) determines a locale point \(e_p:1\to Z\) with
\[
  e_p^*(a)=1\ \Longleftrightarrow\ p\le a.
\]
The condition on \(p\) makes this a frame homomorphism.

For an open \(c\in\mathcal O(Z\times Y)\) define its \(p\)-slice
\(\beta_p(c)=(e_p\times1_Y)^*(c)\in\mathcal O(Y)\). **The key rectangle inequality is**
\[
  \boxed{p\boxtimes\beta_p(c)\le c.}\tag{1.1}
\]
Indeed write \(c=\bigvee_i a_i\boxtimes b_i\). Its slice is
\(\beta_p(c)=\bigvee_{i:p\le a_i}b_i\); for each such \(i\),
\(p\boxtimes b_i\le a_i\boxtimes b_i\le c\).

## 2. A least diagonal cover and W=W₂=U

For any \(Z\)-cover \(\mathscr C\), complete join-primality gives, for each \(p\in\mathscr B\), some \(c\in\mathscr C\) with \(p\le c\). Thus
\[
  w_{\mathscr B}=\bigvee_{p\in\mathscr B}p\boxtimes p
                  \ \le\
  w_{\mathscr C}.
\]
Since \(\mathscr B\) itself is a cover,
\[
  \boxed{D(Z)=O(w_{\mathscr B}).}\tag{2.1}
\]
The Urysohn complement is
\[
  z_Z=\Phi_Z(0)
      =\bigvee_{\mathscr C\text{ cover}}w_{\mathscr C}^*
      =w_{\mathscr B}^*.
\]
Since the closure of \(O(w)\) is \(C(w^*)\),
\[
  W(Z)=\operatorname{cl}D(Z)
      =C(w_{\mathscr B}^*)=C(z_Z)=U(Z).
\]
The universal chain \(W\le W_2\le U\) now yields
\[
  \boxed{W(Z)=W_2(Z)=U(Z).}\tag{2.2}
\]
This directly recovers the known upper-Alexandrov Q′-positive class and explains it using a canonical cofinal cover.

## 3. Exact full fitted-diagonal product preservation

**Theorem 3.1 (working).** If \(Z\) admits a cover \(\mathscr B\) by nonzero completely join-prime opens, then for **every** locale \(Y\),
\[
  \boxed{D(Z\times Y)=D(Z)\times D(Y).}\tag{3.1}
\]

**Proof.** The upper inclusion follows from projection naturality. For the lower inclusion, take any locale \(T\) and two maps
\[
 (\alpha_1,f_1),(\alpha_2,f_2):T\to Z\times Y
\]
whose \(Z\)-coordinates factor through \(D(Z)\) and whose \(Y\)-coordinates factor through \(D(Y)\). Let \(\mathscr C\) be an arbitrary open cover of \(Z\times Y\). For each \(p\in\mathscr B\), the slices
\(\{\beta_p(c):c\in\mathscr C\}\) cover \(Y\). Hence
\[
 \bigvee_{c\in\mathscr C}
   f_1^*(\beta_p(c))\wedge f_2^*(\beta_p(c))=1_T.
\]
By (1.1), both pulls of \(c\) dominate their corresponding
\(\alpha_j^*(p)\wedge f_j^*(\beta_p(c))\). Therefore the **product-cover matching value** is at least
\[
 \bigvee_{p\in\mathscr B}
 \alpha_1^*(p)\wedge\alpha_2^*(p)
 =1_T,
\]
where the last equality follows from (2.1) and the \(D(Z)\)-compatibility of \(\alpha_1,\alpha_2\). Thus every product cover is matched, and the pair factors through \(D(Z\times Y)\). □

**Finite-cover variant.** If in addition \(D_2(Z)=D(Z)\) (for example, the cover \(\mathscr B\) has a finite subcover), then applying the same proof only to finite product covers gives
\[
  D_2(Z\times Y)=D_2(Z)\times D_2(Y).
\]
Without this extra hypothesis **no such finite-\(D_2\) formula is claimed**.

## 4. Q′-positive product preservation

For arbitrary sublocales \(S\subseteq Z^2\), \(T\subseteq Y^2\), the closure of their product equals the product of their closures (a product of dense sublocales is dense, as can be checked on nonzero rectangles). Therefore (3.1) yields
\[
  \boxed{W(Z\times Y)=U(Z)\times W(Y).}\tag{4.1}
\]
Projection naturality similarly gives
\[
  W_2(Z\times Y)\le W_2(Z)\times W_2(Y)
                       =U(Z)\times W_2(Y).
\]
If \(Y\) is Q′-positive, \(W_2(Y)=W(Y)\), the right-hand side is exactly \(W(Z\times Y)\). Since \(W\le W_2\), it follows that
\[
  \boxed{W_2(Z\times Y)=W(Z\times Y).}\tag{4.2}
\]
Thus **multiplying a Q′-positive locale by any locale possessing a supercompact-open cover preserves Q′**.

This is an *asymmetric sufficient criterion*, not a claim of a product formula for arbitrary bases, nor an equivalence/reflection theorem. It includes Sierpiński and arbitrary upper-Alexandrov factors; no non-weakly-subfit Sierpiński-type base of this form can amplify a Q′-positive factor into a counterexample.

## 5. Next concrete test, and what this does not settle

The theorem excludes upper-Alexandrov bases as a route to Q′ failure **when the second factor is already Q′-positive**. It does not exclude atomless Boolean bases such as the Cohen locale: these have no nonzero completely join-prime opens.

A more informative product test than Cohen × Arrieta (where \(W(A)=U(A)=A^2\)) is therefore:
\[
  \boxed{Z_C\times X_{\mathrm{cof}},}
\]
where \(X_{\mathrm{cof}}\) is the previously constructed **noncompact, countably based, sober \(T_1\) rational-arm/two-apex control** satisfying
\[
  D_2(X_{\mathrm{cof}})=D(X_{\mathrm{cof}}),\qquad
  W_2(X_{\mathrm{cof}})=W(X_{\mathrm{cof}})<U(X_{\mathrm{cof}}).
\]
The compact-fiber theorem does **not** apply because this factor is noncompact, and the Boolean N3 splitting theorem only gives the U-product formula without settling W or W₂. An actual Q′ counterexample would still require a **nonzero relatively open defect inside \(D_2(Z_C\times X_{\mathrm{cof}})\)**, not merely a nonclosed D-product failure.

**Next step:** Test a marked cover and residual \(w_{\mathscr C}\to d_{W_2}\) for this specific product, or prove a Boolean-base transfer theorem preventing such a hole. Do not extrapolate from the already settled Cohen × Arrieta case.
