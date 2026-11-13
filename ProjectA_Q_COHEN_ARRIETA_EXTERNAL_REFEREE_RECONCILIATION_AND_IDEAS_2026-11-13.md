# Project A — Cohen × Arrieta external referee reconciliation and further-ideas triage

**13 November 2026.** This is a **post-report analysis**. It does not change or overwrite the [original independent report](project-a/audits/2026-11-13/cohen-arrieta-fullD/EXTERNAL_REFEREE_REPORT_ORIGINAL.md) or the [original further suggestions](project-a/audits/2026-11-13/cohen-arrieta-fullD/EXTERNAL_REFEREE_FURTHER_SUGGESTIONS_ORIGINAL.txt). The prior [internal audit](ProjectA_Q_FULL_D_COHEN_ARRIETA_INTERNAL_AUDIT_2026-11-13.md) remained blind to the external referee. The [historical proof packet](ProjectA_Q_FULL_D_COHEN_ARRIETA_EXTERNAL_BLIND_PACKET_2026-11-13.md) is also preserved.

## 1. Disposition of the independent blind report

**External verdict:** The general strongly-Hausdorff closed-graph theorem, explicit Cohen × Arrieta frame maps, empty equalizer, and strict full-\(D\) product inequality were accepted. The sole proof-level repair is the following one line in the all-cover argument:

If \(u\) contains the attached point \(n\), choose Cantor-open \(V\supseteq K_n\) with \(V\cap Y\subseteq u\cap Y=V_u\cap Y\). Density of \(Y\subseteq C\) gives
\[
  V\subseteq\operatorname{cl}_C(V\cap Y)
   \subseteq\operatorname{cl}_C(V_u)
   \quad\Longrightarrow\quad
  V\subseteq\operatorname{ro}_C(V_u).
\]
Therefore \(K_n\subseteq\operatorname{ro}_C(V_u)\), which is exactly what the rectangle-density proof needs. The stronger, unjustified statement \(K_n\subseteq V_u\) is **not** required.

The referee's additional **direct binary product cover** avoids importing strong Hausdorffness. We independently checked the construction: for \(P=C^2\), \(M=RO(P)\), \(f,g:\operatorname{Loc}(M)\to A\), let
\[
 U_f=\bigvee\{b\boxtimes v:b\wedge f^*(v)=0\},\qquad
 U_g=\bigvee\{b\boxtimes v:b\wedge g^*(v)=0\}.
\]
For each attached \(n\), write \(v_n=Y\cup\{n\}\). Given disjoint clopen Cantor cylinders \(R,S\) with \(R\cap K_n=\varnothing\), put \(b=R\times S\in M\) and split
\[
 v_n=\bigl(((C\setminus R)\cap Y)\cup\{n\}\bigr)
       \ \vee\ (R\cap Y)=v'\vee v''.
\]
Then \(b\wedge f^*(v')=0\) and \(b\wedge g^*(v'')=0\), so \(b\boxtimes v_n\le U_f\vee U_g\). Such \(R\times S\) have **regular-open join 1** because their union is dense in \(P\), excluding only a subset of the nowhere-dense diagonal and finite \(K_n\times C\). Join first over these rectangles, then over \(n\), to obtain \(U_f\vee U_g=1\). The sections annihilate \(U_f\), respectively \(U_g\). Thus the original strict full-\(D\) conclusion stands with this independent, elementary alternate cover.

**Presentation correction:** The blind packet mentioned \(W,W_2,U,Q,Q′\) in its negative-scope discussion but omitted their definitions. This explains the referee's appropriate uncertainty. The new [copy-and-trim external-audit preamble](ProjectA_EXTERNAL_AUDIT_PACKET_DEFINITIONS_BOILERPLATE_2026-11-13.md) prevents recurrence. No historical packet has been retroactively altered.

**The referee's internal-defect question:** The all-bit-flip pair does give
\(D_2(A)\wedge C(w_{\mathscr C})\ne0\), hence \(D_2(A)\ne D(A)\). This is consistent with Q′, which concerns **closed hulls**. Indeed the independent-coordinate quotient identifies \(B(A^2)\le D(A)\); its density gives \(W(A)=W_2(A)=A^2\). The defect is nonzero but nowhere dense relative to \(D_2(A)\). Both **universal** Q and Q′ remain OPEN.

## 2. Further suggestion 1: one Cohen real and one flipped bit — **ADOPT**

Let \(C=2^\omega\), \(M_0=RO(C)\), \(Z_C=\operatorname{Loc}(M_0)\). Let \(r:O(A)\to M_0\) be Cantor-trace regularization, and let \(\tau:C\to C\) flip **only bit 0**. Set
\[
 h_1(u)=r(u),\qquad k_1(u)=\tau^{-1}r(u).
\]
Both are frame maps. For every \(n\ge1\), \(\tau(K_n)=K_n\). Fix an arbitrary \(A\)-cover \(\mathscr C\) and a nonempty Cantor cylinder \(R\). Choose \(n\ge1\) large with \(K_n\cap R\ne\varnothing\), and choose \(u\in\mathscr C\) containing the attached point \(n\). As in §1, an open \(V\supseteq K_n\) lies in \(r(u)\). If \(p\in K_n\cap R\), then both \(p,\tau p\in K_n\subseteq V\), hence
\[
 R\cap r(u)\cap\tau^{-1}r(u)\ne\varnothing
\]
and this intersection is open. Consequently
\[
 \bigvee_{u\in\mathscr C}h_1(u)\wedge k_1(u)=1_{M_0}
\]
for **every** cover. This is full-\(D(A)\), not just finite-cover, compatibility.

For \(a_0=(Y\cap[x_0=1])\cup\{0\}\), the images \(h_1(a_0)=[x_0=1]\) and \(k_1(a_0)=[x_0=0]\) are complementary clopens. Thus the equalizer is zero as a **sublocale** of \(Z_C\). The previous closed-graph theorem (or direct cover) yields the same strict Cohen product inequality with a **single generic Cantor coordinate**. The old all-bit-flip pair is still only finite-cover compatible; no contradiction.

**Additional consequence (internally checked, not externally audited):**
\[
  \boxed{\Delta_A\vee B(A^2)\ <\ D(A).}
\]
Indeed the two-coordinate map from \(RO(C^2)\) identifies \(B(A^2)\le D(A)\). Let \(t:Z_C\to A^2\) be the one-bit-flip pair and let \(S\) denote its nonzero image sublocale. We know \(S\le D(A)\) and \(S\wedge\Delta_A=0\). Define an \(A^2\)-open
\[
 w=\bigvee_{R\times S'\,\cap\,\Gamma_\tau=\varnothing}
       (R\cap Y)\boxtimes(S'\cap Y),
\]
where \(R,S'\) range over clopen cylinders and \(\Gamma_\tau\subset C^2\) is the graph of \(\tau\). Its image under the Booleanization map \(O(A^2)\to RO(C^2)\) is 1 because \(C^2\setminus\Gamma_\tau\) is dense; hence \(B(A^2)\le O(w)\). Its pullback along \(t\) is 0, so \(S\le C(w)\). Thus \(S\wedge B(A^2)=0\). Finite distributivity of the sublocale lattice gives \(S\wedge(\Delta_A\vee B(A^2))=0\), proving strictness.

This is a useful conceptual improvement: \(D(A)\) contains genuinely nonspatial off-diagonal pieces **beyond** the Booleanization of the entire square.

## 3. Further suggestion 2: section rigidity — **ADOPT, WITH A STRENGTHENING**

**Proposition (internally checked):** Let \(Y\) be strongly Hausdorff and \(Z\) a **weakly subfit** locale (in particular any Boolean or subfit locale). For \(f,g:Z\to Y\), consider sections \(s_f=(1_Z,f)\), \(s_g=(1_Z,g)\) into \(Z\times Y\). Then
\[
 (s_f,s_g)\text{ factors through }D_2(Z\times Y)
 \quad\Longleftrightarrow\quad f=g.
\]
If \(f\ne g\), a **two-member cover** witnesses failure.

**Proof.** The equalizer \(E=\operatorname{eq}(f,g)\) is closed in \(Z\), say \(E=C_Z(v)\). If \(f\ne g\), then \(v\ne0\). Weak subfitness yields \(a<1_Z\) with \(a\vee v=1_Z\), so \(E\le O_Z(a)\). The graphs \(\Gamma_f,\Gamma_g\subseteq Z\times Y\) are closed, with open complements \(u_f,u_g\); their intersection is the graph of \(E\), which lies over the open \(a\). Therefore
\[
  \left\{\,u_f\vee(a\boxtimes1_Y),\quad u_g\,\right\}
\]
covers \(Z\times Y\). Its matching value under \((s_f,s_g)\) is **exactly \(a<1\)**: the first term is \(a\wedge s_g^*(u_f\vee(a\boxtimes1))=a\), and the second is zero. Conversely, \(f=g\) gives the product diagonal, which lies in \(D_2\). □

For **Boolean** \(Z\), one can take \(a=s\), the clopen support of the equalizer. This recovers the referee's exact-value formula. The referee suggested three cover members for a *subfit* base; the argument above requires only **weak** subfitness and still uses two members. The improvement is new internal mathematics and deserves later independent scrutiny before promotion.

**Important scope:** This is rigidity for two **sections over the identity on \(Z\)**. It does not assert that the entire sublocale \(D_2(Z\times Y)\wedge(\Delta_Z\times Y^2)\) equals the diagonal.

## 4. Suggestions 3–6: assessment

| Referee idea | Decision | Reason / next useful test |
| --- | --- | --- |
| **3. Base-change failure of fitting; proposed Boolean-section axiom** | **Partly adopt, defer axiom.** | The precise base-change failure follows from the existing product witness: in \(Z_C\times A^2\), \(\operatorname{fit}(Z_C\times\Delta_A)\ <\ Z_C\times D(A)\). Pull the product cover back along the common-base diagonal to obtain an open neighbourhood of \(Z_C\times\Delta_A\) killing the witness. Claims about a new axiom's equivalence to total unorderedness \(TU\) need an exact definition and proof. “Closure commutes” must be scoped to the relevant map, not asserted for arbitrary pullbacks. |
| **4. Atomic / Cohen-adding / measure bases** | **Adopt the first two, investigate measure separately.** | A complete atomic Boolean base is a discrete coproduct of copies of \(A\), so the full fitted-diagonal formula holds componentwise. Any nonzero Boolean base \(Z\) admitting a locale map \(Z\to Z_C\) inherits the strictness witness by composing \(f,g\); equalizer zero and all-cover matching are preserved. The sweeping assertion that *no* measure algebra witnesses strictness is currently unproved. |
| **5. Lindelöf and countable covers** | **Adopt as a reduction, with a wording correction.** | A ccc complete Boolean algebra has the property that every join is the join of a countable subfamily. Combined with a countable base of \(A\), every open cover of \(Z_C\times A\) has a countable subcover: decompose its members into rectangles, group by the countably many \(A\)-basic opens, and countably reduce the Boolean coefficients. Consequently **all-cover \(D\) on this product can be tested using countable covers**. This does *not* by itself establish a strict inequality \(D_2(Z_C\times A)\ne D(Z_C\times A)\). |
| **6. Criterion for closed \(N\subseteq C^2\)** | **Defer pending definition; do not record as conjecture yet.** | “\(B(N)\) lies in \(D(A)\)” has no canonical meaning for arbitrary closed \(N\): the coordinate maps \(B(N)\to A\) need not exist. The proposed condition is phrased “off the diagonal” but uses \(N=C^2\) as a supporting case. Even a singleton \(N=\{(p,q)\}\subseteq K_n\times K_n\) with \(p\ne q\) satisfies the proposed density condition without giving a canonical off-diagonal point of \(A^2\). First specify the allowed \(N\), the trace/regularization maps, and what inclusion is meant. |

### Concrete measure-algebra negative control, not a general no-go

Let \(\mu\) be fair-coin product measure on \(C\) and replace \(RO(C)\) by the measure algebra. The **one-bit-flip** pair of §2 then fails all-cover compatibility: cover \(Y\) by the two bit-0 cylinder traces, whose matching squares are zero, and cover each attached \(n\) by \((V_n\cap Y)\cup\{n\}\) with \(V_n\supseteq K_n\) and \(\sum_n\mu(V_n)<1/4\). The matching join has measure at most \(1/4\), not 1.

Likewise the **independent-coordinate** measure pair fails: cover \(Y\) by the \(2^m\) length-\(m\) cylinder traces (their independent matching squares have total product measure \(2^{-m}\)); cover the attached points by tiny \(V_n\) with \(\sum_n\mu(V_n)^2<1/4\). Choosing \(m\ge2\) makes the whole matching join have measure below 1. These tests support the referee's measure/category heuristic **for the canonical pairs only**; they do not exclude other measure-algebra-valued maps.

## 5. Priorities after reconciliation

1. **Retain the externally accepted main theorem** \(D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A)\) with the one-line D.2 repair. Its independent audit is now complete, distinct from the fresh addendum results.
2. **Consolidate the one-bit witness and section rigidity** as internally checked corollaries; the strict \(\Delta_A\vee B(A^2)<D(A)\) is especially informative about the shape of the fitted diagonal. Submit for separate audit if used centrally later.
3. **Use the countable-cover reduction** to simplify any future concrete analysis of \(D(Z_C\times A)\), but keep \(D_2\) versus \(D\) on the product itself unresolved.
4. **Return to the actual Q′ density problem**: for each full cover \(\mathscr C\), can \(T_{\mathscr C}=D_2(X)\wedge C(w_{\mathscr C})\) contain a nonzero **relative-open patch of \(D_2(X)\)**? Neither the new product failure nor the nonzero weak defect on \(A\) supplies one.
5. **Treat measure-algebra obstruction and the closed-\(N\) classification as secondary.** A measure theorem would require ruling out *all* Boolean-valued pairs, not merely the two canonical examples. The \(N\)-criterion requires a valid construction before becoming a conjecture.

**Status and provenance:** Main product theorem **independently blind-reviewed, with minor presentation repair**; one-bit witness, strengthened section rigidity, Lindelöf reduction, base-change interpretation, and the extra structural inequality are **newly internally checked only**. Q and Q′ remain **OPEN**.
