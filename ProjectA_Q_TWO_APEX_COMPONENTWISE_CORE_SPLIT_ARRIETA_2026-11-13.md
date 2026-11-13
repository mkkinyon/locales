# Project A — componentwise persistent-core transfer and a split Arrieta test

**13 November 2026. Internally checked working mathematics; no independent referee yet.** Follow-up to the [one-arm core theorem](ProjectA_Q_ANTIURYSOHN_TWOAPEX_PERSISTENT_CORE_ARRIETA_TEST_2026-11-13.md) and the [transfinite exhaustion note](ProjectA_Q_TWO_APEX_ITERATED_KERNEL_EXHAUSTION_2026-11-13.md). The split test is designed expressly to **break** the hypothesis that the first derived kernel is anti-Urysohn. Both universal Q and Q′ remain open.

## 1. Transfer along clopen anti-Urysohn *arm channels*

Let T be a topological sum of any family of nonempty T₁ sober **anti-Urysohn clopen components** T_i (disjoint, covering T). Let G_n be decreasing nonempty T-opens with empty intersection and form the filtered two-arm, three-apex X=X(T,G). Individual G_n∩T_i are allowed to be empty. Define componentwise persistent kernels

\[
P_i=\bigcap_n\operatorname{cl}_{T_i}(G_n\cap T_i),
\quad P=\coprod_i P_i\ \text{(a closed subspace of T)},
\quad F=P_+\cup P_-\cup\{a,b,t\}\subseteq X.
\]

**Theorem 1.1 (componentwise core reduction).**
\[
\boxed{W(F)=W_2(F)\quad\Longrightarrow\quad W(X)=W_2(X).}
\]
In particular, if P is compact, then X is Q′-positive. This extends the preceding single anti-Urysohn-arm theorem to a T that may itself be **non-anti-Urysohn**.

**Proof.** Suppose E⊆W₂(X)≤U(X) is a nonzero relatively open marked Q′ hole, disjoint from W(X). For each sign σ∈{+,-} and channel i, the open arm component T_{i,σ} has anti-Urysohn rank zero. Its fitted diagonal is dense in its own square, and restricting any X-cover to this open component shows

\[
\operatorname{cl}_{X^2}(T_{i,\sigma}^2)
=J_{i,\sigma}^2\le W(X),
\qquad J_{i,\sigma}=\operatorname{cl}_X(T_{i,\sigma}).
\]

No assumption that J_{i,\sigma} is open or clopen is made.

Let R_{i,\sigma}=(T_i\setminus P_i)_\sigma. For each x∈R_{i,\sigma}, there is n and a T_i-open V_x about x disjoint from G_n∩T_i. Since T_i is clopen within the arm, the X-closure of V_x stays in T_{i,\sigma}: the relevant a- and t-neighbourhoods miss it, and all other arm components and the opposite arm are separated from it. Put H_{i,\sigma}=X\setminus J_{i,\sigma}, an open sublocale. Its closure is disjoint from the **open** T_{i,\sigma}. Therefore

\[
V_x\boxtimes H_{i,\sigma}\le z_X,
\quad\text{and hence}\quad
R_{i,\sigma}\boxtimes H_{i,\sigma}\le z_X.
\]

Within the first-coordinate R_{i,\sigma} strip, U(X)=C(z_X) has its second coordinate inside J_{i,\sigma}; hence that portion of E lies in J_{i,\sigma}²≤W(X) and must vanish. By symmetry the same holds in second-coordinate strips. Joining over i and both signs gives

\[
E\le F^2.
\]

Finally B(E), its dense Booleanization, lies in D₂(X)∧F²=D₂(F) by exact closed heredity. Hence E≤W₂(F); it is relatively open there, and is disjoint from W(F) by exact full-D heredity. Thus F has a Q′ hole, contradiction. □

**What this does not prove.** If P is a noncompact Q′-unknown subspace with mixed channel interactions, the theorem transfers the problem to F but does not settle it. Clopen components of the *arms* are not automatically clopen subspaces of X once the apices adhere, so the earlier clopen-remainder gluing theorem alone would not imply this result.

## 2. The first non-anti-Urysohn Arrieta kernel

Use Arrieta's Cantor source C=2^ω, the finite sets K_n of eventually-zero sequences with last 1 at n, Y=C\setminus⋃K_n, and the anti-Urysohn attached space A=Y⊔ω. Define two disjoint, closed, nowhere-dense Cantor subspaces

\[
S_L=\{x:x_0=0,\ x_j=0\ (j\ge1\text{ odd})\},
\]
\[
S_R=\{x:x_0=1,\ x_j=0\ (j\ge2\text{ even})\},
\qquad S=S_L\cup S_R.
\]

All K_n meet S, but each attaches to **exactly one** channel:

- For even n≥2, K_n∩S_L≠∅ and K_n∩S_R=∅.
- For odd n≥1, K_n∩S_R≠∅ and K_n∩S_L=∅.
- K_0∩S_R≠∅ and K_0∩S_L=∅.

Thus the closed subspace

\[
P=(Y\cap S)\cup\omega\subseteq A
\]

splits into two **clopen** noncompact nonregular subspaces P_L and P_R, each anti-Urysohn. For P_L this is literally an Arrieta copy on the free even positions. For P_R the odd positions are free and the extra 0-attached point replaces the all-zero free sequence; the same anti-Urysohn verification holds: every nonempty relative Cantor-open patch meets K_n∩S_R for all sufficiently large odd n, so the closure of each nonempty P_R-open contains cofinitely many of these attached odd n. (Both channels are T₁ Hausdorff, hence sober.)

Choose x_L∈K_2∩S_L and x_R∈K_1∩S_R. Take a descending sequence V_n of Cantor-clopen neighbourhoods of S with ∩V_n=S. For c=L,R choose descending Cantor-clopen O_n^c around x_c such that O_n^c⊆V_n, O_n^c lies in the corresponding first-coordinate cylinder, and ∩O_n^c={x_c}. Set

\[
G_n=\bigl((V_n\setminus S)\cup O_n^L\cup O_n^R\bigr)\cap Y.
\]

The G_n are nonempty decreasing A-opens with empty intersection. Since S is nowhere dense, V_n\setminus S is dense in V_n, so

\[
\bigcap_n\operatorname{cl}_C G_n=S.
\]

As in the first Arrieta kernel calculation, an attached point k belongs to every cl_A G_n exactly when K_k∩S≠∅. Therefore the **first persistent arm kernel is exactly P**, which is noncompact, nonregular and **not anti-Urysohn** (its two channels are disjoint clopen nonempty subspaces). The single-arm Theorem 2.1 from the preceding note cannot be re-applied to X(P,G_n∩P).

But in the induced closed two-apex space X(P,G|P), the traces are

\[
G_n\cap P_c=O_n^c\cap Y\cap S_c
\quad(c=L,R),
\]

and each channel P_c is anti-Urysohn. The componentwise kernel is **one attached point in each channel**, by the nested finite-K compactness calculation:

\[
\bigcap_n\operatorname{cl}_{P_L}(G_n\cap P_L)=\{2\},
\qquad
\bigcap_n\operatorname{cl}_{P_R}(G_n\cap P_R)=\{1\}.
\]

Its closed remainder consists of the three apices and the two surviving attached points in each of the two arms, hence **seven points**, compact. Apply Theorem 1.1 to the first residual X(P,G|P), then the original anti-Urysohn-arm reduction to X(A,G):

\[
\boxed{W(X(A,G))=W_2(X(A,G)).}
\]

This test deliberately introduces the first **non-anti-Urysohn** persistent kernel while retaining noncompactness, nonregularity and nontrivial traces. A finite clopen split into positive anti-Urysohn channels still cannot create a Q′ hole when the next componentwise residual is compact.

## 3. A side check: Arrieta's arms are not metacompact

The non-metacompactness filter from the post-referee priority ledger is **necessary for a Q′ counterexample in the relevant Baire/quasi-Polish setting, not sufficient**. Indeed Arrieta's A is not metacompact.

Let \(\mathcal C=\{Y\}\cup\{N_n:n\in\omega\}\), where N_n=(V_n∩Y)∪{n} is any chosen basic n-neighbourhood (here V_n is a Cantor-open neighbourhood of K_n). Suppose there were a point-finite open refinement. For each n choose a refining R_n containing n; it can only refine N_n. Every R_n contains a basic neighbourhood of n, hence its trace R_n∩Y contains U_n∩Y for some Cantor-open U_n⊇K_n. Every nonempty basic Cantor cylinder meets K_n for **all sufficiently large n** (choose the prescribed finite prefix and put the last 1 at n). Hence for each N the Y-open union ⋃_{n≥N}(R_n∩Y) is **dense** in the Polish Baire space Y. Their intersection is dense and nonempty, so some y∈Y belongs to infinitely many distinct R_n, contradiction.

The same obstruction applies to every filtered X(A,G) with G_n⊆Y: the added-point set ω_+ in one arm is closed in X; use its open complement together with basic arm-open n-neighbourhoods as a cover. Any point-finite refinement again supplies one n-neighbourhood per n whose Y_+-traces overlap infinitely at a Y-point. So these Q′-positive controls genuinely pass the **non-metacompactness** necessary filter; that filter alone does not decide Q′.

## 4. Scope and remaining design issue

Three independent suppressors of open Q′ defects have now been proved within filtered two-apex geometry:

1. Regular Hausdorff arm patches: a normalized bad support is either regularly patchable or collapses to anti-Urysohn rank zero.
2. Clopen Q′-positive *whole-space* patches: an open hole localizes to a Q′-positive closed remainder.
3. Anti-Urysohn arm **channels**, even when they cease to be clopen in the apex extension: an open hole localizes to the common componentwise persistent kernel. Iterated and limit-stage versions may reach a compact terminal support.

The split Arrieta example rules out the most direct escape from the all-anti-Urysohn-core condition of the ω-tower note. An untested two-apex candidate would need a residual nonregular, non-anti-Urysohn kernel **not decomposable into positive anti-Urysohn clopen channels with a positive common residual**, and must pass the marked relatively-open-hole test. Constructing such a kernel with explicit cover-square control is a genuinely new mechanism rather than a further adjustment to the present tails.

**Audit status:** All componentwise localization, split-Cantor and metacompactness calculations above are fresh internal arguments. The imported exact closed heredity, Boolean-hole localization, rank-zero identity, and Arrieta source facts were previously checked separately. No independent external audit is claimed for this synthesis.
