> **STRONGER PRENUCLEUS NORMAL FORM (12 Nov 2026):** The closed-remainder self-reduction below is now superseded in strength by the [canonical Boolean-support core theorem](ProjectA_Qprime_PRENUCLEUS_BOOLEAN_SUPPORT_IDEMPOTENT_CORE_2026-11-12.md). Every Q′ failure provides a nonzero *regular-open* first-step \(\Phi(d_{\mathcal W_2})\) hole E attached to one cover C; its canonical Booleanization supplies the SAME finite-compatible, C-incompatible witness before and after restricting to its **least closed common coordinate support** K, and even the SAME localic open E survives. The reduced K has \(t_{C|K}=0\) and no nonzero hull-sound two-coordinate strips; this normal form is **idempotent for the marked E**. Unlike the conditional minimal-counterexample discussion in §4 below, no minimal-counterexample existence or transfinite limit assumption is needed. Q/Q′ remain OPEN; the new theorem is internal, not externally audited.

# Project A — Q′ hereditary closed-remainder reduction and regular-core rigidity

**11 November 2026 · NEW INTERNAL theorem and adversarial proof check, NOT externally audited.** Successor to [zero-dimensional residual proof and Baire boundary control](ProjectA_Qprime_closed_zero_dimensional_residual_rigidity_BAIRE_2026-11-11.md). It strengthens that zero-dimensional lemma to **arbitrary regular closed sublocales**, gives exact **closed heredity of the full and finite fitted diagonals**, and proves a **self-reduction theorem**: an alleged Q′ counterexample yields an *actual counterexample* inside its cover-dependent closed remainder. This is stronger than merely placing a pointless sublocale there. Neither Q′ nor Q is solved universally. No novelty or priority claim; regularity→fitted-diagonal follows classical frame principles, and the relative closure argument is a new project-level deduction.

## 0. Definitions and imported localization

For a locale X, L=O(X), write
\[
w_\mathcal C=\bigvee_{c\in\mathcal C}c\boxtimes c\in L\oplus L,\quad
\mathcal D(X)=\bigwedge_{\mathcal C\text{ cover}}\mathfrak o(w_\mathcal C),
\quad \mathcal D_2(X)=\bigwedge_{\mathcal F\text{ finite cover}}\mathfrak o(w_\mathcal F),
\]
and \(\mathcal W(X)=\mathrm{cl}_{X^2}\mathcal D(X)\), \(\mathcal W_2(X)=\mathrm{cl}_{X^2}\mathcal D_2(X)\). Q′ asserts W=W₂ for all locales (OPEN).

For a cover \(\mathcal C\) set
\[
t_\mathcal C=\bigvee_{\substack{F\subseteq\mathcal C\\F\ \mathrm{finite}}}
\bigvee\{v:v^*\vee\bigvee F=1\}.
\]
Let e be an open **hull-sound on coordinate strips**, i.e. W₂ and W restrict equally on \(\mathfrak o(e\boxtimes1\vee1\boxtimes e)\). The previous mixed theorem supplies \(e=h_{\rm hc}\), join of hyperconnected opens, and allows the further addition of the previously established compact-closed-neighborhood strip open \(h_{\rm cc}\). The e=h_hc input has an earlier working-proof provenance, rather than independent audit.

**Previously established exact defect:** if W<W₂, there is a cover C and a disjoint rectangle r=a⊠b with \(r\not\le d_0=d_{W₂}\), \(r\wedge w_C\le d_0\), \(r\le d_W\). The rather-below and sound-strip localization imply, with \(\ell=t_C\vee e\),
\[
E=W_2(X)\wedge\mathfrak o(r)\ne0,\qquad
E\le K^2,\quad K=\mathfrak c(\ell),
\]
and
\[
\mathcal D(X)\wedge E=0,\qquad
\mathcal D_2(X)\wedge E\text{ dense in }E.
\tag{0.1}
\]
All support claims are in the localic product (actual sublocales). These are imported established structural results, not re-proved from pointwise spatiality.

## 1. Exact closed-heredity theorem for fitted diagonals

**Theorem 1.1.** For **every closed sublocale** \(i:K\hookrightarrow X\),
\[
\boxed{
\mathcal D_2(X)\wedge(K\times K)=\mathcal D_2(K),\qquad
\mathcal D(X)\wedge(K\times K)=\mathcal D(K)
}
\tag{1.1}
\]
as sublocales of X² under the canonical embedding K²↪X².

*Proof (frame/sublocale).* The product inclusion \(i\times i\) pulls back each open square to its restricted square:
\[
(i\times i)^{-1}\mathfrak o(w_F^X)
=\mathfrak o\!\left(\bigvee_{c\in F}(i^*c)\boxtimes(i^*c)\right).
\]
Sublocale inverse image preserves arbitrary meets. Hence the pullback of D₂(X) is the meet of restrictions of all finite **X-covers**; similarly for D(X) and all covers.

Every X-cover restricts to a K-cover. Conversely, given ANY finite K-cover \(G=\{g_1,\ldots,g_n\}\), lift its opens to \(c_i\in O(X)\) using surjectivity of \(i^*:O(X)\twoheadrightarrow O(K)\). If \(K=\mathfrak c(a)\), the finite family \(\{a,c_1,\ldots,c_n\}\) is an X-cover, and its restriction is \(G\cup\{0_K\}\), inducing exactly the same square in \(O(K^2)\). This establishes equality of the two families' generated filter of square opens and thus their meets. The **same proof** works for arbitrary (possibly infinite) covers G by adding just one open a. □

**Corollary 1.2 (closed heredity of finite/full equality).** If \(\mathcal D_2(X)=\mathcal D(X)\), then \(\mathcal D_2(K)=\mathcal D(K)\) for every closed K⊂X. Do NOT infer that W₂=W is hereditary to closed sublocales merely from (1.1): closure need not commute with restriction to a closed sublocale.

## 2. Regular locales have diagonal finite-cover fitting

**Theorem 2.1.** For every regular locale K,
\[
\boxed{\mathcal D_2(K)=\mathcal D(K)=\Delta_K.}
\tag{2.1}
\]

*Proof.* Let h,k:O(K)→B be arbitrary frame maps with the finite-cover compatibility property. Fix u∈O(K) and v≺u, so \(\{v^*,u\}\) is a finite cover. Its compatibility says
\[
1_B=h(v^*)\wedge k(v^*)\ \vee\ h(u)\wedge k(u).
\]
Meet with h(v). The first term disappears, giving \(h(v)\le k(u)\). By symmetry \(k(v)\le h(u)\). Since regularity says \(u=\bigvee_{v\prec u}v\), join gives h(u)≤k(u) and k(u)≤h(u). Hence h=k as frame maps, for ANY target frame B. The generalized pair factors through the diagonal; converse inclusion is tautological. Because Δ≤D≤D₂, all are equal. □

**Corollary 2.2.** If K is a closed **regular** sublocale of arbitrary X, then
\[
\boxed{\mathcal D_2(X)\wedge K^2=\Delta_K.}
\tag{2.2}
\]
In particular this extends the preceding **closed zero-dimensional** result (zero-dimensional frames are regular). The simple clopen-cover proof of the preceding note is retained as an independent low-tech argument; the regular proof uses rather-below approximation.

**Remark.** This is consistent with known locale theory: regular locales are fit and the diagonal is fitted, but (2.1) gives an explicit short **finite-cover** compatibility proof with no appeal to general separatedness theorems.

## 3. The main hereditary residual theorem

**Theorem 3.1 (coverwise diagonally-finitary residuals).** Let e be an open hull-sound on coordinate strips. For every open cover C of X define its **closed remainder**
\[
K_C=\mathfrak c(t_C\vee e).
\]
If
\[
\boxed{\mathcal D_2(K_C)=\mathcal D(K_C)
\quad\text{for every cover C},}
\tag{3.1}
\]
then
\[
\boxed{\mathcal W(X)=\mathcal W_2(X).}
\tag{3.2}
\]

*Proof.* Otherwise take C and nonzero E from §0. By (1.1),
\[
0\ne\mathcal D_2(X)\wedge E
\le\mathcal D_2(X)\wedge K_C^2
=\mathcal D_2(K_C)=\mathcal D(K_C)
\le\mathcal D(X).
\]
This contradicts \(\mathcal D(X)\wedge E=0\). □

**New positive instance:** if K_C is **regular for every C**, (3.1) holds by (2.1). This permits any noncompact, non-zero-dimensional, connected or nonspatial regular remainder. Earlier positive classes (compact K_C; zero-dimensional K_C; K_C with totally spatial square, such as locally compact Hausdorff scattered K_C) all satisfy (3.1):
- compact K_C: arbitrary covers have finite subcovers;
- zero-dimensional K_C: regular;
- totally spatial K_C²: D₂(K_C) and D(K_C) have the same ordinary points (old all-locale theorem) and, being sublocales of a totally spatial locale, must coincide.
Thus (3.1) **unifies** the previous compact, zero-dimensional and scattered remnants without claiming equivalence of their underlying hypotheses.

**Fixed-boundary criterion 3.2.** If some closed K⊂X has D₂(K)=D(K) and K_C≤K for every C, then (3.2) follows: closed heredity (Corollary 1.2) applies to each K_C, which is closed in K. This avoids checking every cover's K_C separately.

## 4. Stronger still: the closed remainder is ITSELF a Q′ counterexample

**Theorem 4.1 (self-reduction of a Q′ counterexample).** Let e be hull-sound. If
\[
\mathcal W(X)<\mathcal W_2(X),
\]
there is a cover C and a rectangle r as in §0 such that the closed sublocale
\[
K=\mathfrak c(t_C\vee e)
\]
satisfies
\[
\boxed{\mathcal W(K)<\mathcal W_2(K).}
\tag{4.1}
\]
Moreover the restricted cover \(C|_K\) and rectangle \(r_K=(i\times i)^*(r)\) give an explicit disjoint-rectangle **Q′ witness on K**.

*Proof.* Let E be as in (0.1). The nonzero \(\mathcal D_2(X)\wedge E\) lies in K² and in \(\mathfrak o(r_K)\); (1.1) gives
\[
\mathcal D_2(K)\wedge\mathfrak o_K(r_K)\ne0.
\tag{4.2}
\]
On the other hand, since \(\mathcal D(X)\le\mathcal W_2(X)\),
\[
\begin{aligned}
\mathcal D(K)\wedge\mathfrak o_K(r_K)
&=\mathcal D(X)\wedge K^2\wedge\mathfrak o(r)\\
&\le\mathcal D(X)\wedge\mathcal W_2(X)\wedge\mathfrak o(r)\\
&=\mathcal D(X)\wedge E=0.
\end{aligned}
\tag{4.3}
\]
**Careful scope:** the inequality in line 2 uses **\(\mathcal D(X)\le\mathcal W_2(X)\)**, not an unjustified general claim that closure commutes with restriction to K. Thus the open \(\mathfrak o_K(r_K)\) meets D₂(K) but is disjoint from D(K). Consequently it meets \(\mathcal W_2(K)\) but not \(\mathcal W(K)\), proving (4.1).

For the advertised explicit witness, pulling \(r\wedge w_C\le d_0\) back to K² gives \(r_K\wedge w_{C|K}\le(i\times i)^*(d_0)\). The closed sublocale \(\mathcal W_2(X)\wedge K^2\) contains D₂(K) by (1.1), so it contains \(\mathcal W_2(K)\). Therefore the defining open satisfies
\[
(i\times i)^*(d_0)\le d_{\mathcal W_2(K)}.
\]
Hence \(r_K\wedge w_{C|K}\le d_{\mathcal W_2(K)}\). Equation (4.2) ensures \(r_K\not\le d_{\mathcal W_2(K)}\). Also \(r_K\) is a disjoint rectangle because \(a\wedge b=0_X\) implies \(i^*a\wedge i^*b=0_K\). Thus the exact disjoint-rectangle certificate holds INSIDE K for the restricted cover, which therefore has no finite subcover. □

**Proper-reduction consequence.** If \(t_C\vee e\ne0_X\), then K is a **proper closed** Q′ counterexample. In particular a counterexample having any nonzero globally hull-sound strip e admits a proper closed counterexample. A hypothetical counterexample minimal among its nonzero closed sublocales would therefore have h_hc=0, h_cc=0 (using their established soundness), and \(t_C=0\) for every cover that witnesses its Q′ failure. This is a **conditional minimality** consequence; existence of minimal counterexamples is NOT claimed, since descending chains of closed counterexamples need not have a counterexample at their intersection.

## 5. Geometric control with NONCOMPACT, NON-ZERO-DIMENSIONAL regular remainder

The construction from the [Baire boundary note](ProjectA_Qprime_closed_zero_dimensional_residual_rigidity_BAIRE_2026-11-11.md) works with **any nonempty second-countable regular Hausdorff noncompact boundary T** in place of Baire space. Take:
- \(Y=\ell^2\), connected infinite-dimensional separable Hilbert;
- \(S=\mathcal P(\mathbb N)\setminus\{\varnothing\}\), upper Scott topology, hyperconnected and noncompact;
- \(T=\ell^2\) as a **second, distinct copy** of infinite-dimensional Hilbert, closed in the resulting X.

As a set \(X=Y\sqcup S\sqcup T\). Let Y,S be disjoint open subspaces with their native topologies. At each t∈T, give neighborhoods
\[
N(U,n,F)=U\cup\{y\in Y:\|y\|>n\}\cup\uparrow F,
\tag{5.1}
\]
with U an ordinary open T-neighborhood of t, n∈N, F finite nonempty. Intersections give N(U∩U',max(n,n'),F∪F').

As in the Baire control:
- X is second countable, T₀, **sober**, connected, noncompact and nonregular (S is a nonregular open subspace). Sobriety: a nonempty irreducible closed A meeting Y or S is the closure of the unique generic point of A∩that open sober subspace; otherwise A⊂T and is singleton, since T is Hausdorff. Connectedness: closures of connected Y and S are Y∪T and S∪T, meet along T, and cover X.
- \(h_{\rm hc}=S\). Every open meeting Y or T contains disjoint nonempty Y-opens (T neighborhoods contain Hilbert tails); every nonempty open of S is hyperconnected.
- For EVERY cover C, \(Y\subseteq t_C\), by sufficiently small bounded Y-balls with closures inside C-members and still closed in X. Thus \(K_C=C(t_C\vee S)\) is a **closed sublocale of T**, hence regular: a closed subspace of a metric space is metric regular. Theorem 3.1 gives
\[
\boxed{\mathcal W(X)=\mathcal W_2(X).}
\tag{5.2}
\]

The same Cantor-regular-open frame maps \(h_+,h_-:\mathcal O(S)\to\operatorname{RO}(2^\omega)\) used in the preceding Baire note yield a **strict \(\mathcal D_2(X)>\mathcal D(X)\)**. Specifically, take a countable open cover \(\{U_m\}\) of T and
\[
\mathcal C^\star=\{Y\}\cup
\{N(U_m,1,\{0\}):m\in\omega\}\cup
\{\uparrow\{n\}\subseteq S:n\in\omega\}.
\tag{5.3}
\]
All C* members restrict to S as zero or a singleton principal Scott upset. The pair is finite-cover compatible but its meet-compatibility over C* equals zero; this is a **pointless**, truly infinitary discrepancy.

For this C*, one checks \(t_{C^\star}=Y\), because a relatively nonzero S-open has pseudocomplement zero on S while finite restrictions of C* never cover S, and every T-neighborhood meets S. Consequently
\[
\boxed{K_{C^\star}=T\cong\ell^2,}
\tag{5.4}
\]
which is **noncompact, connected, not zero-dimensional, not scattered**, and nowhere locally compact. The earlier compact-remainder criterion and the zero-dimensional/scattered remainder criteria all fail to apply, but the new **regular** remainder criterion works.

The space also satisfies \(h_{\rm cc}=0\): a compact closed sublocale with nonempty interior meeting Y contains a closed noncompact Hilbert ball; one meeting S or T contains closure of a nonempty S-open, hence all of the noncompact closed T. The fixed hyperconnected remainder \(X\setminus S=Y\cup T\) is noncompact.

**Nonregular Urysohn control (localic rectangle argument, not just point pairs):** Restrict to the **open locale square** Y². If a,b∈O(Y) are disjoint, write a and b as joins of **bounded metric balls whose closures lie respectively within a and b**. Every such ball's closure in X equals its ordinary closed Hilbert ball (all boundary T-neighborhoods can exclude a bounded set), hence each cross rectangle is far *in X*. Coproduct distributivity shows that the whole \(a\boxtimes b\) lies in the restriction of \(d_{\mathcal U(X)}\). Since Y is Hausdorff in the strong localic sense, these rectangles join-generate the complement of \(\Delta_Y\). Conversely U(X) contains Δ_X. Thus, as **localic subobjects** (even without assuming spatiality of the entire square),
\[
\boxed{\mathcal U(X)\wedge\mathfrak o(Y^2)=\Delta_Y.}
\]
Because Y has no isolated points, Δ_Y has empty interior: no nonzero rectangular open can lie inside Δ_Y. Any open in X² meeting Y² would restrict to a nonzero open in Y², so \(\operatorname{int}\mathcal U(X)\) misses Y². Its closure also misses this *open* square, while U(X) contains Δ_Y. Hence \(\mathcal U(X)\) is **not regular closed**. Equality W=W₂ here is therefore NOT a mere consequence of the universal regular-core inclusion.

These topological controls have not been externally checked; the frame-theoretic main theorems §§1–4 stand independently of the example.

## 6. Relationship to the original Q/Q′ programme

This gives an exact **self-similar obstruction**. To defeat Q′, a single cover C must yield a remainder K_C which:
1. is noncompact (compact ⇒D₂=D);
2. has \(\mathcal D_2(K_C)>\mathcal D(K_C)\) (Theorem 3.1), hence is NOT regular or zero-dimensional;
3. is itself an actual Q′ **counterexample** (Theorem 4.1);
4. admits a nonzero pointless witness in a disjoint coordinate rectangle, which survives relative closure and cannot be removed by any available hull-sound strip;
5. has a nonregular global Urysohn boundary on the relevant piece, by the prior regular-core theorem.

The previous branching and Scott examples have D₂>D without Q′ failure, and the Hilbert-boundary example here shows noncompact, non-zero-dimensional, perfect residuals PLUS a full infinitary fitting defect elsewhere still do not force Q′ failure. The same cover must localize the defect and reproduce Q′ failure on its own closed remainder. No inductive termination theorem or universal answer is asserted.

**Literature notes:** Regularity→rather-below approximation and the classical fitted-diagonal theory are background (e.g. Picado–Pultr, *Frames and Locales*, Ch. V; Arrieta–Picado–Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, Applied Categorical Structures 30 (2022), 247–263). The scattered total-spatial result is classical (Suarez, *On the relation between subspaces and sublocales*, JPAA 226 (2022), 106851); here it only explains one sufficient class subsumed by Theorem 3.1. No originality claim.

**Audit status:** New internal mathematical results. The key closed-heredity lemma and regularity proof are independent of any earlier hyperconnected-strip statement; the generalized remainder theorem uses that older working strip lemma and the earlier externally corroborated rectangular obstruction/localization. A focused adversarial audit should revisit (i) inverse image of arbitrary fitted-sublocale meets, (ii) lifting finite and infinite covers from K, (iii) the frame inequality in Theorem 4.1, and (iv) the Hilbert/Scott/boundary topology, before promotion.
