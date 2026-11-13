# Project A / Q′ — Boolean-base transfer across anti-Urysohn persistent kernels

**13 November 2026. New internally checked working theorem; NOT externally audited.** This extends the filtered anti-Urysohn-arm core reduction to products with **arbitrary nonzero Boolean locales**, including the pointless Cohen locale. It relies on the referee-origin Boolean-base N3 theorem and on previously established marked-hole persistence. Universal Q and Q′ remain OPEN.

## 0. Definitions and imports

For a locale Y and cover C, put \(w_C=\bigvee_{c\in C}c\boxtimes c\). Write \(D(Y)\) and \(D_2(Y)\) for the full and finite fitted diagonals and \(W(Y)=\operatorname{cl}D(Y)\), \(W_2(Y)=\operatorname{cl}D_2(Y)\), \(U(Y)=C(z_Y)\). Q′-positive means W=W₂.

Let \(Z\) be a **nonzero Boolean locale**. Then \(W(Z)=W_2(Z)=U(Z)=\Delta_Z\), with closed diagonal. We import the referee's **N3 Boolean-base splitting theorem** ([reconciliation](ProjectA_Q_POSTREFEREE_RECONCILIATION_2026-11-13.md)): for any anti-Urysohn locale T (\(z_T=0\)),
\[
\boxed{W(Z\times T)=W_2(Z\times T)=U(Z\times T)=\Delta_Z\times T^2.}\tag{N3}
\]
This theorem is only used at the **closed** level; it says nothing about the nonclosed fitted diagonal multiplying.

We also import: (a) universal \(U(Z\times Y)=U(Z)\times U(Y)\); (b) exact closed heredity \(D_\epsilon(K)=D_\epsilon(Y)\wedge K^2\) for a closed K; (c) for a genuine Q′ gap a nonzero relatively open marked hole E⊆W₂(Y) exists with its dense Booleanization B(E)≤D₂(Y), and the same hole persists inside any closed K² containing E. These had separate audits/provenance.

## 1. Filtered two-arm space and persistent remainder

Let T be a nonempty sober T₁ spatial **anti-Urysohn** space, and let \(G_0\supseteq G_1\supseteq\cdots\) be nonempty T-opens with \(\bigcap_nG_n=\varnothing\). Form
\[
X=X(T,G)=T_+\amalg T_-\amalg\{a,b,t\},
\]
with basic apex neighborhoods
\[
A_n=\{a\}\cup(G_n)_+,\quad
B_n=\{b\}\cup(G_n)_-,\quad
T_n=\{t\}\cup(G_n)_+\cup(G_n)_-.
\]
Let \(P=\bigcap_n\operatorname{cl}_T(G_n)\), a closed persistent tail kernel, and \(F=P_+\cup P_-\cup\{a,b,t\}\subseteq X\), a **globally closed** residual sublocale. Write \(J_+=\operatorname{cl}_X T_+=T_+\cup\{a,t\}\), \(J_-=\operatorname{cl}_X T_-=T_-\cup\{b,t\}\), and \(R_\pm=(T\setminus P)_\pm\), opens in X.

The original filtered-core theorem ([source](ProjectA_Q_ANTIURYSOHN_TWOAPEX_PERSISTENT_CORE_ARRIETA_TEST_2026-11-13.md)) supplies the far-strip containment
\[
U(X)\wedge O(R_+\boxtimes1)\le J_+^2,
\quad
U(X)\wedge O(R_-\boxtimes1)\le J_-^2,
\tag{1.1}
\]
and symmetric second-coordinate statements. Here these are **localic** inclusions, not pointwise approximations.

## 2. Boolean-base persistent-core theorem

**Theorem 2.1 (new, working).** For any nonzero Boolean locale Z,
\[
\boxed{
W(Z\times F)=W_2(Z\times F)
\quad\Longrightarrow\quad
W(Z\times X)=W_2(Z\times X).
}\tag{2.1}
\]

*Proof.* Identify \((Z\times X)^2\cong Z^2\times X^2\). Set \(Y=Z\times X\), and consider the open chart \(V_+=Z\times T_+\subseteq Y\). Any Y-cover restricts to a V₊-cover, so, on the **actual** localic square,
\[
D(V_+)\le D(Y)\wedge V_+^2.
\tag{2.2}
\]
Since T is anti-Urysohn, N3 gives \(W(V_+)=\Delta_Z\times T_+^2\). Take closure inside Y². The product-closure formula and \(\operatorname{cl}_X T_+=J_+\) imply
\[
\boxed{\Delta_Z\times J_+^2\le W(Y).}\tag{2.3}
\]
Likewise \(\Delta_Z\times J_-^2\le W(Y)\).

Suppose instead W(Y)<W₂(Y) and take a nonzero relatively open canonical marked hole \(E\subseteq W_2(Y)\), disjoint from W(Y). Naturalness and the universal U-product formula imply
\[
E\le W_2(Y)\le U(Y)
=\Delta_Z\times U(X).
\]
By (1.1), the portion of E on a first-coordinate \(R_+\)-strip lies in \(\Delta_Z\times J_+^2\le W(Y)\), hence is zero. Repeat for R₋ and the symmetric second-coordinate strips. Thus E avoids all the opens supported on R₊∪R₋ in either X-coordinate, and
\[
\boxed{E\le (Z\times F)^2.}\tag{2.4}
\]
The sublocale Z×F is closed in Y. By marked-hole persistence under **closed** support, the same E is nonzero and relatively open in W₂(Z×F), but disjoint from W(Z×F). This contradicts the hypothesis. □

**Corollary 2.2 (compact persistent kernel).** If the persistent kernel P is compact, then F is compact (a finite union of compact subspaces). Since \(W_2(Z)=I(Z)=\Delta_Z\), the independently reconstructed **compact-fiber theorem** gives
\[
W(Z\times F)=W_2(Z\times F).
\]
Theorem 2.1 therefore yields
\[
\boxed{W(Z\times X(T,G))=W_2(Z\times X(T,G)).}\tag{2.5}
\]

No claim is made that \(D_2(Z\times X)=D(Z\times X)\), or that \(W(Z\times X)=\Delta_Z\times W(X)\).

## 3. Concrete Cohen × Arrieta-arm test

In [the one-point Arrieta-arm construction](ProjectA_Q_ANTIURYSOHN_TWOAPEX_PERSISTENT_CORE_ARRIETA_TEST_2026-11-13.md), choose T=A (Arrieta's strongly Hausdorff, nonregular, noncompact anti-Urysohn space) and tails \(G_n=V_n\cap Y\) shrinking through a deleted Cantor point \(x_*\in K_m\). The persistent kernel is exactly \(P=\{m\}\), and F is a finite **five-point discrete** closed subspace. The original X is noncompact, countably based, sober T₁ and has the explicitly proved finite-cover rank gap \(W(X)=W_2(X)<U(X)\).

Choose \(Z=Z_C=\mathrm{Loc}(RO(2^\omega))\), the atomless, pointless Cohen Boolean locale. Corollary 2.2 proves \(W(Z_C\times X)=W_2(Z_C\times X)\). The strict inequality to U survives: by W projection naturality and universal U-product preservation,
\[
W(Z_C\times X)
\le\Delta_{Z_C}\times W(X)
<\Delta_{Z_C}\times U(X)
=U(Z_C\times X).
\]
Hence
\[
\boxed{
W(Z_C\times X)=W_2(Z_C\times X)<U(Z_C\times X).
}\tag{3.1}
\]
This product has no ordinary points, and its fiber is **nonregular** as well as noncompact. Unlike Cohen×X_cof, it is not disposed of by the globally closed regular-patch argument; its Q′ positivity comes from **Boolean N3 plus persistent-kernel localization**.

## 4. Possible tower extension and limitations

Theorem 2.1 can be iterated through a descending chain of **closed** filtered-arm cores provided EVERY stage's arm is anti-Urysohn and the marked-hole persistence is retained at limit stages. A terminal compact F gives a positive Cohen product by compact-fiber transfer. A transfinite blanket statement additionally requires checking the topology of the stage restrictions, nonempty tail traces, and stabilization at limits; we do NOT present a new blanket theorem here. The [existing tower note](ProjectA_Q_TWO_APEX_ITERATED_KERNEL_EXHAUSTION_2026-11-13.md) supplies these checks for its particular construction.

**Research interpretation:** Boolean pointless multiplication does not resurrect Q′ holes removed by either (i) regular patchable supports or (ii) anti-Urysohn same-arm saturation plus compact persistent remainder. Further tests need genuinely new mixed-support geometry or an explicit relative-open cover defect. Do not mistake a nonclosed D₂ failure over the Cohen base for an open Q′ counterexample.

**Audit status:** New Theorem 2.1 and its corollary internally checked, NOT independently externally reviewed. Dependencies: referee-origin N3, prior compact-fiber transfer, original anti-Urysohn core geometry, and audited marked-hole persistence. Universal Q and Q′ remain open.


## 5. A second concrete control: Cohen × the ω-deep Arrieta tower

The [iterated-kernel note](ProjectA_Q_TWO_APEX_ITERATED_KERNEL_EXHAUSTION_2026-11-13.md), §4, constructs decreasing closed arms \(P_0=A\supset P_1\supset\cdots\), each \(P_i\cong A\) and hence **anti-Urysohn**, and closed filtered spaces \(X_i=X(P_i,G|P_i)\). The persistent kernel of stage i is \(P_{i+1}\), so its residual is \(X_{i+1}\). At the first infinite stage,
\[
P_\omega=\bigcap_{i<\omega}P_i=\{0^\omega\},\qquad
X_\omega=\{a,b,t,(0^\omega)_+,(0^\omega)_-\},
\]
a finite compact closed space. The note checks the topology, nonempty tail traces at each finite stage, and closed limit intersection.

**Corollary 5.1 (working).** For any nonzero Boolean locale Z, in particular pointless Cohen \(Z_C\),
\[
\boxed{W(Z\times X_0)=W_2(Z\times X_0).}\tag{5.1}
\]

*Proof without unjustified backward induction at an infinite ordinal.* Suppose there is a single nonzero marked relative-open Q′ hole E in \(W_2(Z\times X_0)\). Apply the **proof** of Theorem 2.1 at stage 0: it shows E is supported on \((Z\times X_1)^2\), is relatively open in \(W_2(Z\times X_1)\), and retains the same full-cover defect after closed restriction. Repeating at each finite stage yields E≤(Z×X_i)² for every i. Since these are CLOSED sublocales and
\[
\bigwedge_{i<\omega}(Z\times X_i)^2
=(Z\times X_\omega)^2,
\]
E lies in the terminal closed product square and persists as a nonzero relatively open hole there. But X_ω is compact and \(W_2(Z)=I(Z)\), so compact-fiber transfer gives Q′ positivity on Z×X_ω. Contradiction. □

**Caution.** The preceding tower note did **not** prove \(W_2(X_0)<U(X_0)\); consequently no strict W/U gap is claimed for its Cohen product. This is a Q′-positive control only. The argument extends to other ordinal towers only after verifying anti-Urysohnity at EVERY stage used, actual closed stage embeddings, nonempty tail traces, and the terminal Q′ theorem. No blanket claim about all possible filtered towers is made.

The combination of (3.1) and (5.1) removes both the single-point and ω-deep self-similar Arrieta cores as potential Q′ counterexamples generated by Cohen multiplication.


## 6. Componentwise Boolean-base transfer, and the split-Arrieta control

The [componentwise filtered-core note](ProjectA_Q_TWO_APEX_COMPONENTWISE_CORE_SPLIT_ARRIETA_2026-11-13.md) treats arms which are **not themselves anti-Urysohn**, but split into clopen anti-Urysohn channels. Its proof also admits Boolean-base multiplication.

**Theorem 6.1 (new working componentwise version).** Let \(T=\coprod_{i\in I}T_i\) be a topological sum of nonempty sober T₁ **anti-Urysohn** clopen components, with filtered tails G_n as in §1 (some G_n∩T_i may be empty). Put
\[
P_i=\bigcap_n\operatorname{cl}_{T_i}(G_n\cap T_i),\quad
P=\coprod_iP_i,\quad F=P_+\cup P_-\cup\{a,b,t\}.
\]
For every nonzero Boolean locale Z,
\[
\boxed{W(Z\times F)=W_2(Z\times F)
\ \Longrightarrow\ W(Z\times X(T,G))=W_2(Z\times X(T,G)).}\tag{6.1}
\]

*Proof.* For each channel i and sign σ, let \(J_{i,\sigma}=\operatorname{cl}_X((T_i)_\sigma)\). Restrict every cover of Z×X to the open chart Z×(T_i)_σ. N3 says its full fitted diagonal is dense in \(\Delta_Z\times(T_i)_\sigma^2\); taking ambient closure gives
\[
\Delta_Z\times J_{i,\sigma}^2\le W(Z\times X).
\]
For \(R_{i,\sigma}=(T_i\setminus P_i)_\sigma\), the precise far-strip computation of the earlier componentwise theorem gives
\[
U(X)\wedge O(R_{i,\sigma}\boxtimes1)\le J_{i,\sigma}^2
\]
(and the symmetric second-coordinate formula). The argument uses clopenness of T_i **within the open arm**, not of its closure in all X. The universal identity U(Z×X)=Δ_Z×U(X) therefore forces any nonzero marked Q′ hole E of Z×X to vanish on both coordinate strips over each \(R_{i,\sigma}\). The R_i,σ cover the arm region removed from F. Hence E≤(Z×F)². The same closed-heredity / dense Booleanization argument of Theorem 2.1 turns E into a hole of Z×F, contradiction. □

**Concrete split-Arrieta application.** In the cited split-Cantor construction, the first residual arm \(P=P_L\amalg P_R\) has two **clopen anti-Urysohn** noncompact nonregular channels; their componentwise persistent kernel is one attached point in each channel, and the second residual is a **seven-point compact** closed space F₂.

For Cohen Z_C, compact-fiber transfer makes Z_C×F₂ Q′-positive. Theorem 6.1 applied to the intermediate filtered space X(P,G|P) makes Z_C times that space Q′-positive. Theorem 2.1 applied to the **original** Arrieta anti-Urysohn arm A then gives
\[
\boxed{W(Z_C\times X(A,G))=W_2(Z_C\times X(A,G)).}\tag{6.2}
\]
No strict inequality to U is asserted in this split construction, because the original split-kernel note did not establish one.

**Updated product-test inventory.** Cohen multiplication now leaves Q′ positive in all the explicit filtered two-apex controls tested here: rational regular arms (§§1–3 of the regular-patch product note), one-point Arrieta kernel (§3), ω-deep self-similar Arrieta tower (§5), and the first non-anti-Urysohn *split* Arrieta kernel (§6). These are **internal working deductions**, not a claim about arbitrary filtered cores or arbitrary Boolean-base Q′ transfer. The next research effort should address the **relative-open density problem inside D₂/W₂ itself**, not another relabeling of these controlled tails.
