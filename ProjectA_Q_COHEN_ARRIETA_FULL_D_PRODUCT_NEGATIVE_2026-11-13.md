# Project A — Cohen × Arrieta: FULL fitted-diagonal product failure

**13 November 2026. Major new internally derived result; NOT independently refereed.** This note answers the formerly open nonclosed product question **negatively**. It builds on the explicit finite-level Arrieta Boolean maps in [the preceding working note](ProjectA_Q_COHEN_ARRIETA_D2_BINARY_FAILURE_AND_FULL_D_FRONTIER_2026-11-13.md), but **uses a different, all-cover-compatible pair**. No Q or Q′ counterexample follows: the closed Cohen × Arrieta formula W=W₂=U=Δ_Z×A² remains true by the referee's N3 theorem.

## 1. A general closed-graph obstruction

**Theorem 1.1 (Boolean product failure for strongly Hausdorff non-F-separated locales).**
Let Y be **strongly Hausdorff**, so its diagonal Δ_Y is a closed sublocale of Y². The following are equivalent:

1. Y is F-separated: D(Y)=Δ_Y.
2. For every Boolean locale Z, D(Z×Y)=Δ_Z×D(Y).

More pointedly, if D(Y)≠Δ_Y, then there is a **nonzero Boolean locale Z** and a **binary cover** of Z×Y such that

\[
\boxed{D(Z\times Y)\ \subsetneq\ \Delta_Z\times D(Y).}\tag{1.1}
\]

**Proof, positive direction.** If D(Y)=Δ_Y and Z is Boolean, D(Z)=Δ_Z. Projection naturality gives D(Z×Y)≤D(Z)×D(Y)=Δ_{Z×Y}; the diagonal is always fitted-contained, giving equality.

**Proof, negative direction.** Because Δ_Y is closed and D(Y) properly contains it, the relatively open off-diagonal part

\[
E=D(Y)\wedge O(Y^2\setminus\Delta_Y)
\]

is nonzero. Take its Booleanization T=B(E), a nonzero Boolean locale. Its coordinate maps f,g:T→Y form a **full-cover-compatible pair**, because T→Y² factors through D(Y), and have **empty equalizer**, because T maps into the open complement of the diagonal.

Put Z=T and consider the two graph sections

\[
s_f=(1_Z,f),\qquad s_g=(1_Z,g):Z\longrightarrow Z\times Y.
\]

Since Y is strongly Hausdorff, each graph Γ_f,Γ_g is a **closed** sublocale of Z×Y (pullback of Δ_Y). The graphs have zero intersection: their pullback is the equalizer of f,g, which is zero. Thus their **open complements** u_f=(Z×Y)\setminus Γ_f and u_g=(Z×Y)\setminus Γ_g form a binary open cover of Z×Y.

The section s_f kills u_f, while s_g kills u_g. Consequently the pair (s_f,s_g) evaluates the cover square to

\[
s_f^*(u_f)\wedge s_g^*(u_f)
\ \vee\
s_f^*(u_g)\wedge s_g^*(u_g)=0.
\]

It does **not** factor through D(Z×Y). But its common Z-coordinate is the identity and (f,g) factors through D(Y), so it **does** factor through Δ_Z×D(Y). This witnesses strictness. □

**Scope:** The existence of *some* Boolean witnessing base follows for every strongly Hausdorff non-F-separated Y. The theorem alone does **not** identify that base as Cohen. The next section supplies an explicit Cohen witness for Arrieta's A.

## 2. Independent Cantor coordinates give full-cover-compatible Cohen maps

Let C=2^ω and let A=Y⊔ω be Arrieta's [Construction 4.2 / Example 4.5](https://arxiv.org/pdf/2310.18522), with the finite K_n⊆C and dense Y=C\setminus⋃K_n. Arrieta proves that A is **strongly Hausdorff** and anti-Urysohn. Every infinite subfamily of the K_n has dense union in C.

Put P=C×C, M=RO(P), and Z=Loc(M). Since P is homeomorphic to Cantor space, Z is the **Cohen Boolean locale Z_C**. The regular-open quotient of O(P) gives two frame maps from O(A) to M:

\[
h(u)=\operatorname{ro}_P(V_u\times C),\qquad
k(u)=\operatorname{ro}_P(C\times V_u),
\]

where V_u is any Cantor-open set with V_u∩Y=u∩Y and ro_P denotes the regular-open hull. These are well-defined frame maps: the restriction of O(A) to O(Y), followed by regularization of a Cantor-open representative of the Y-trace, is a frame map into M (with regular-open joins). Let f,g:Z→A be the corresponding locale maps.

**Lemma 2.1 (full-cover compatibility).** For **every** A-cover \(\mathcal C\),

\[
\boxed{\bigvee_{u\in\mathcal C}h(u)\wedge k(u)=1_M.}\tag{2.1}
\]

Proof. Test density in P on a nonempty basic Cantor rectangle R×S. Choose n sufficiently large that K_n meets both R and S; this is possible because for all large n, K_n meets each fixed basic cylinder. Some u∈\mathcal C contains the attached point n. Hence u∩Y contains a Y-neighbourhood of the **whole** K_n, arising from a Cantor-open V_u. This V_u meets R and S in nonempty Cantor-open subsets, so the regular-open rectangle h(u)∧k(u) has a nonzero part inside R×S. Therefore the union of the matching rectangles is dense in P, and its join in RO(P) is 1. □

Thus (f,g):Z→A² factors through the **full fitted diagonal D(A)**, not merely through D₂(A). This is substantially stronger than the complementary-coordinate pair in the previous note, which deliberately failed a countable ground A-cover.

**Lemma 2.2 (empty equalizer).** The equalizer of f,g is zero. For each n define the A-open

\[
a_n=(Y\cap\{x:x_n=1\})\cup\{n\}.
\]

Then h(a_n) is the clopen P-open “first-coordinate bit n equals 1,” while k(a_n) is the corresponding “second-coordinate bit n equals 1.” If f and g agree on a sublocale, that sublocale lies in the clopen equality locus e_n={ (x,y):x_n=y_n}. In the complete Boolean algebra RO(P),

\[
\bigwedge_{n\in\omega}e_n
=\operatorname{int}_P\{(x,y):x=y\}=0,
\]

because the Cantor diagonal is nowhere dense. Hence their equalizer is zero. □

## 3. The binary cover resolving the Cohen product question

Let Γ_f,Γ_g be the graphs of f,g inside Z_C×A. They are **closed** because A is strongly Hausdorff (the diagonal is localically closed). By Lemma 2.2, they are disjoint. Hence

\[
\mathcal C_{\rm graph}=
\{(Z_C\times A)\setminus\Gamma_f,\quad
  (Z_C\times A)\setminus\Gamma_g\}
\]

is a **two-member open cover**.

The two sections s_f=(1,f), s_g=(1,g) share their Cohen base coordinate and their A-components factor through D(A), by Lemma 2.1. Hence the pair factors through Δ_{Z_C}×D(A). But the first cover member is killed by s_f and the second by s_g; their matching value is 0. Thus it fails even this binary cover of Z_C×A:

\[
\boxed{
D(Z_C\times A)\ \subsetneq\
\Delta_{Z_C}\times D(A).
}\tag{3.1}
\]

This **settles the 13 November Priority 2 full-D product question NEGATIVELY**. The obstruction is inherently Boolean-valued/nonspatial: the two generic Cantor coordinates are **jointly generic enough to match every ground A-cover**, but their individual values are available as maps from the Cohen base, so their **graphs can be separated by a new product cover**.

The graph-cover argument bypasses the difficult attempt to uniformly refine product covers by ground A-covers. That uniformization is genuinely unnecessary for a **negative** result.

## 4. Compatibility with the positive closed-level results

The external referee's N3 Boolean-base splitting theorem remains intact:

\[
W(Z_C\times A)=W_2(Z_C\times A)=U(Z_C\times A)
=\Delta_{Z_C}\times A^2.
\]

Thus (3.1) is a **nonclosed** failure: no relatively open Q′-hole is produced, and both Q and Q′ remain OPEN universally. The previous explicit D₂ counterexample also remains true, but the new full-D failure is strictly more informative; it uses **all-cover** compatibility in the A-factor and only a **binary** cover in the product.

The general Theorem 1.1 explains why strongly Hausdorff **non-F-separated** Y are natural sources of Boolean-base nonclosed product defects. It is fully consistent with the earlier SDκ-positive product theorem: a highly distributive Boolean base need not admit the all-cover-compatible, everywhere-distinct generalized maps f,g that Cohen supplies.

## 5. Proof dependencies and verification points

- Arrieta, [localic separation and the closed/fitted diagonal duality](https://arxiv.org/pdf/2310.18522): Construction 4.2, Corollary 4.3, Proposition 4.4, Example 4.5; importantly, strong Hausdorff means the **locale diagonal is closed**, so graphs of maps into A are closed.
- The map O(Y)→RO(C) requires **regular-open joins**, not ordinary unions, and is well-defined because Y is dense in C. Verify the factorization through Y and both coordinate projections.
- Lemma 2.1 is an **all-cover** computation, not merely finite-cover matching. It uses the full K_n neighbourhood of each attached point and arbitrarily large n meeting every two basic cylinders.
- Lemma 2.2 uses the **complete Boolean meet** of the clopen equality loci, not their ordinary infinite intersection as a potentially nonopen set. This meet is 0.
- The two graphs are **actual closed sublocales** and their intersection is the pullback equalizer, not merely an ordinary-point intersection.
- All equalities and inequalities concern actual fitted sublocales of localic squares. No density-to-closed-restriction inference is used.

**Audit status:** The category-theoretic graph obstruction and Cohen-Arrieta specialization were derived and adversarially reconstructed internally on 13 November 2026, after the previous blind report. They should receive an independent external audit before being promoted to the certified theorem ledger. The project questions Q/Q′ are unaffected and remain open.


## 6. Distinguish this product defect from an internal Q′ weak defect

The pair (s_f,s_g) of §3 lies in **Δ_{Z_C}×D(A)** but **not** in D₂(Z_C×A), since the *binary* product cover already separates it. Thus it does **not** define a weak defect T_C=D₂(Z_C×A)∧C(w_C) of the type relevant to Q′. It is a **failure of nonclosed product preservation**, not a failure of full-cover compatibility *inside the product's D₂*. This distinction is stronger than merely saying that its defect has empty relative interior.

The right intrinsic Q′ criterion remains: for every full X-cover C, the relatively closed T_C=D₂(X)∧C(w_C) must be nowhere dense *in D₂(X)*, equivalently B(D₂(X))∧T_C=0, or B(D₂(X))≤D(X). The Boolean target Z_C used in §3 is **not** thereby being identified with a sublocale of B(D₂(Z_C×A)).

**Next conceptual work:** Study conditions guaranteeing that a Boolean-valued *weak* pair in D₂(X)∧C(w_C) cannot extend to a relatively open D₂ patch. The newly resolved product inequality supplies a valuable nonclosed control, but does not by itself bridge the support-versus-relative-density gap.


## 7. Audit handoff (13 November)

The [internal adversarial audit](ProjectA_Q_FULL_D_COHEN_ARRIETA_INTERNAL_AUDIT_2026-11-13.md) provisionally **passes** the general theorem and explicit Cohen specialization after checking the frame homomorphisms, all-cover argument, Boolean equalizer, graph cover, and the distinction from Q/Q′. Arrieta’s primary-source statements were rechecked directly. The separate [external blind prompt](ProjectA_Q_FULL_D_COHEN_ARRIETA_EXTERNAL_BLIND_PROMPT_2026-11-13.md) and [proof packet](ProjectA_Q_FULL_D_COHEN_ARRIETA_EXTERNAL_BLIND_PACKET_2026-11-13.md) contain no internal verdict. **External review pending; do not promote to independently certified status.**
