# Project A — Q′: focused rigidity tests and a binary boundary-cover obstruction

**9 November 2026 — Internal working note only; not independently audited, no originality or priority claim.**

The open question is (Q′): is \(\mathcal W=\mathcal W_2\) for all frames? Equivalently, is \(d_{\mathcal W_2}\) fixed by the full diagonal-cover pre-nucleus? We test whether a forcing variant can retain a disjointly supported, finite-cover-compatible Boolean witness while removing the **finite-coordinate flips** that made \(\mathcal D\) dense in the previous missing-center model. Both tests below fail, for opposite reasons. No result about universal Q′ is asserted.

Conventions: \(L=\mathcal O(X)\), \(Q=L\oplus L\), \(w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c\), \(\mathcal D=\bigcap_{\mathcal C}O(w_{\mathcal C})\), \(\mathcal D_2\) uses only finite covers, and \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal W_2=\operatorname{cl}\mathcal D_2\). For frame maps \(h,k:L\to M\), finite-cover compatibility is \(\bigvee_{c\in F}h(c)\wedge k(c)=1_M\) for all finite covers \(F\).

## 1. A necessary binary boundary-color condition

Suppose \(A,B\in L\) are disjoint opens, \(A\vee B\vee\bigvee_i N_i=1\), and \(h,k:L\to M\) have
\[
h(A)=k(B)=1,\quad h(B)=k(A)=0. \tag{1.1}
\]
For any partition \(I=I_0\sqcup I_1\), let \(N_j=\bigvee_{i\in I_j}N_i\). Since \(\{A\vee N_0,B\vee N_1\}\) is a **finite cover**, its compatibility condition reads
\[
\boxed{k(N_0)\vee h(N_1)=1_M.} \tag{1.2}
\]
Using the reversed two-element cover \(\{B\vee N_0,A\vee N_1\}\) gives
\[
\boxed{h(N_0)\vee k(N_1)=1_M.} \tag{1.3}
\]
Both are necessary for every partition and every simultaneous choice of boundary neighborhoods.

**Immediate obstruction to nested-string labeling.** Suppose the Boolean target is \(\operatorname{RO}(2^\omega)\) (or another Boolean frame with a proper complemented first-bit element), and \(h(N_i)\le[s_i]\), \(k(N_i)\le[\overline{s_i}]\) where each finite word \(s_i\) specifies its first bit. Color \(i\) by \(s_i(0)\). For \(I_0\) consisting of words beginning in 0 and \(I_1\) those beginning in 1,
\[
k(N_0)\le[1],\qquad h(N_1)\le[1],
\]
contradicting (1.2), as \([1]<1\). Thus a naive longer-prefix or nested-prefix rigidity modification destroys finite-cover compatibility *already for two opens*. It is not a Q′ example.

## 2. Infinite repetition of labels: the finite flips survive

Use the missing-center two-sheet construction of [the previous forcing gluing test](A-W2-missing-center-forcing-finite-flips-2026-11-09.md), but allow the boundary label at \(q_n\) to refer to a base coordinate \(f(n)\), not necessarily to \(n\). More precisely:

Let \(R=\mathbb R\setminus\mathbb Q\), let \((q_n)_{n\ge1}\) enumerate all rationals without repetition, and \(P=\operatorname{Fn}(\mathbb N,2)\setminus\{\varnothing\}\), with the extension Alexandrov topology. Take open sheets \(A,B\cong R\times P\), attach boundary points \(t_n\), and give \(t_n\) neighborhoods
\[
N_{n,I}=\{t_n\}\cup((I\cap R)\times\uparrow\ell_{f(n)})^A
                     \cup((I\cap R)\times\uparrow\ell_{f(n)})^B,
\quad \ell_j=\{j\mapsto0\},\ q_n\in I.
\tag{2.1}
\]

Choose **the denominator labeling**
\[
f(n)=\operatorname{den}(q_n),
\tag{2.2}
\]
where a rational is in lowest terms and its denominator is positive. Every base coordinate \(j\) now occurs at **infinitely many** boundary points, so flipping a single base coordinate modifies infinitely many boundary neighborhoods. But the corresponding rational centers are the discrete set \(\{p/j:\gcd(p,j)=1\}\). For every finite \(E\subseteq\mathbb N\), the union of the rational centers with \(f(n)\in E\) is locally finite and nowhere dense in \(\mathbb R\); its complement among the rationals is dense in every interval.

Put \(K=2^{\mathbb N}\), \(M=\operatorname{RO}(R\times K)\). With the standard frame maps from the finite-condition poset to M, define a pair \(h,k\) by restricting to the two sheets and using opposite bit orientations. Thus
\[
h(N_{n,I})=j((I\cap R)\times[f(n)=0]),\qquad
k(N_{n,I})=j((I\cap R)\times[f(n)=1]).
\tag{2.3}
\]
The original construction of these frame maps is by taking joins of sections against Cantor cylinders; finite meets hold because any two compatible conditions have a common extension. Here \(j\) is double-negation regularization.

**Claim 2.4 (finite-cover compatibility).** Every finite open cover \(U_1,\ldots,U_m\) of X is compatible with h,k.

*Proof.* Assign each \(t_n\) a color \(i(n)\in\{1,\ldots,m\}\) such that \(U_{i(n)}\supseteq N_{n,I_n}\) for some interval \(I_n\ni q_n\). Let \(O\times[s]\subseteq R\times K\) be a nonempty target basic open, where \(O\) is the irrational part of a real interval and \(s\) is a finite binary condition.

The color classes \(C_i=\{q_n:i(n)=i\}\) cover the rationals, hence their closures cover the real line. By Baire category (or the elementary finite-union nowhere-dense argument), some class \(C_i\) is dense in a nonempty real interval \(J\) contained in the interval underlying \(O\). Because the points with any prescribed finite set of denominators are nowhere dense, choose \(n\) of color \(i\) in \(J\) with \(f(n)\notin\operatorname{dom}(s)\). Next choose \(n'\) of the same color in the nonempty interval \(J\cap I_n\), with
\(f(n')\notin\operatorname{dom}(s)\cup\{f(n)\}\). The intersection \(I_n\cap I_{n'}\cap J\) is nonempty, as is
\[
[s]\cap[f(n)=0]\cap[f(n')=1].
\]
Thus the target basic open meets \(h(U_i)\wedge k(U_i)\). As the target basic open was arbitrary, \(\bigvee_i h(U_i)\wedge k(U_i)=1_M\). \(\square\)

The infinite cover
\[
\mathcal C=\{A,B\}\cup\{N_{n,\mathbb R}:n\ge1\}
\tag{2.5}
\]
has \(h(c)\wedge k(c)=0\) for every member, so D2>D is witnessed by the disjoint rectangle \(\rho=A\boxtimes B\).

**Claim 2.6 (finite-flip rescue survives).** For every finite set E of **base** coordinates, define \(\theta_A=H_+\circ(-\wedge A)\), and \(\theta_B^E=\gamma_E\circ H_+\circ(-\wedge B)\), where \(\gamma_E\) flips the Cantor coordinates in E. Then \((\theta_A,\theta_B^E)\) is compatible with **every cover**, not merely finite covers.

*Proof.* For any cover V, each t_n lies in some \(V_n\in V\) containing \(N_{n,I_n}\). Whenever \(f(n)\notin E\),
\[
\theta_A(V_n)\wedge\theta_B^E(V_n)
 \ge j((I_n\cap R)\times[f(n)=0]).
\]
The join of the right-hand opens over such n is \(1_M\). Indeed, to meet any nonempty target basic \(O\times[s]\), choose \(q_n\) in its underlying real interval with \(f(n)\notin E\cup\operatorname{dom}(s)\). Its interval \(I_n\) meets O, and its bit cylinder meets \([s]\). Thus the join is dense and regularizes to top. \(\square\)

Given basic sheet conditions s,t with overlapping parameter intervals, flip the **finite** set where s,t prescribe conflicting bits. Their images under \((\theta_A,\theta_B^E)\) then have nonzero meet, so D meets the associated mixed rectangle. For disjoint parameter projections, a two-stage rectangle expansion into subopens with disjoint parameter closures proves that the mixed rectangle lies under \(d_{\mathcal U}\). Hence, exactly as in the previous forcing note,
\[
\boxed{\mathcal W\wedge O(\rho)
=\mathcal W_2\wedge O(\rho)
=\mathcal U\wedge O(\rho).}
\tag{2.7}
\]

**Significance.** Repeating each bit infinitely often is **not** enough to destroy the full-cover-compatible finite modifications. The modified labels form a locally finite subset of parameter centers; regular-open completion ignores their loss as long as the untouched centers remain dense.

## 3. Perfect-tree forcing: the desired Boolean witness fails already at two covers

A more substantive rigidity mechanism is to allow a nonzero forcing condition that fixes **infinitely many** binary coordinates. Consider the poset \(\mathbb S\) of perfect binary trees ordered by extension (stronger = smaller tree), with the upper Alexandrov topology defined by its stronger conditions. Let \(B\) be its complete regular-open forcing Boolean algebra and \(b_T>0\) the Boolean value of a perfect-tree condition T. Let \(\ell_n^0\) be the perfect tree of sequences having bit n=0, and \(b_n^0=b_{\ell_n^0}\); its complement is \(b_n^1\), corresponding to bit n=1.

As in the missing-center construction, take two sheets \(A,B_{\mathrm{sh}}\cong R\times\mathbb S\), with rational boundary centers q_n and neighborhoods
\[
N_{n,I}=\{t_n\}\cup((I\cap R)\times\uparrow\ell_n^0)^A
                 \cup((I\cap R)\times\uparrow\ell_n^0)^{B_{\mathrm{sh}}}.
\]
The standard regular-open completion \(\alpha:\mathcal O(\mathbb S)\to B\) sends \(\uparrow T\) to \(b_T\), and its composition with global bitwise complement sends \(\uparrow\ell_n^0\) to \(b_n^1\). Via the frame coproduct target \(M=\mathcal O(R)\oplus B\), these give sheet maps \(h,k:\mathcal O(X)\to M\) with
\[
h(A)=1,\quad h(B_{\mathrm{sh}})=0,\quad k(A)=0,\quad k(B_{\mathrm{sh}})=1,
\]
\[
h(N_{n,I})=(I\cap R)\boxtimes b_n^0,\qquad
k(N_{n,I})=(I\cap R)\boxtimes b_n^1.
\tag{3.1}
\]
(These maps may alternatively be defined by sectionwise rectangular joins, avoiding any topological-product spatiality assumption.)

**Claim 3.2.** This proposed pair \((h,k)\) is **not finite-cover compatible**.

*Proof.* Choose bounded real intervals \(J_0,J\) with
\(\overline{J_0}\subset J\) and \(J_0\cap R\ne\varnothing\). Set
\[
S=\{n:q_n\in J\}.
\]
Both S and its complement are infinite. There is a perfect-tree condition \(T_S\) whose branches have bit 0 at **every n∈S**, while all coordinates outside S remain free. This condition is perfect because \(\mathbb N\setminus S\) is infinite. Its Boolean value \(b_{T_S}>0\) satisfies \(b_{T_S}\wedge b_n^1=0\) for every n∈S.

For every n∉S choose a rational interval \(I_n\ni q_n\) disjoint from J_0, possible because \(q_n\notin J\supseteq\overline{J_0}\). Choose arbitrary \(I_n\ni q_n\) for n∈S. Set \(N=\bigvee_nN_{n,I_n}\). Then
\[
\{A\vee N,\ B_{\mathrm{sh}}\}
\tag{3.2}
\]
is a two-element open cover of X. The nonzero target rectangle
\[
(J_0\cap R)\boxtimes b_{T_S}
\]
has zero meet with \(k(N)\): each n∈S contributes a Boolean value disjoint from \(b_{T_S}\), and each n∉S contributes a parameter open disjoint from \(J_0\). Thus \(k(N)\ne1_M\). But since h(A)=1 and h(B_sh)=0, compatibility with (3.2) would force
\[
1_M=h(A\vee N)\wedge k(A\vee N)\vee h(B_{\mathrm{sh}})\wedge k(B_{\mathrm{sh}})
=k(N),
\]
a contradiction. \(\square\)

This failure is particularly sharp: the candidate does not even define a point of \(\mathcal D_2\), so no closed-hull comparison can be inferred.

The underlying contrast is the following. In the Cohen Boolean algebra \(\operatorname{RO}(2^\omega)\), the meet of all fixed-bit cylinders over any infinite S is zero (the corresponding set is nowhere dense). In the Sacks forcing completion, the **same infinite bit prescription** can be a nonzero perfect-tree condition when \(\mathbb N\setminus S\) is infinite. A boundary cover local to the rational centers indexed by S then exposes it at the binary-cover level.

## 4. Outcome and scope

The two targeted rigidity mechanisms fail for **opposite reasons**:

1. **Infinite duplication of independent labels (denominator assignment):** finite-cover compatibility persists, but finite-support transformations still produce enough fully compatible Boolean maps to make D dense in the mixed Urysohn boundary.
2. **Allow nonzero infinite-coordinate restrictions (perfect-tree forcing):** the hoped-for nonhomogeneity is real, but a simple **two-element cover** already defeats the mirrored Boolean pair.
3. **Nested-prefix labels:** even ordinary Cohen completion fails the necessary binary boundary-coloring condition (1.2), because the prefix supplies a finite-visible invariant.

This is not a theorem excluding all nonhomogeneous forcing constructions: other label incidence patterns, targets, and genuinely coupled geometries remain possible. But the obvious variations have been tested on their exact failure modes. We have no new counterexample, no new proof of Q′, and no justification for an indefinitely expanding catalog of such examples.

The most precise remaining design requirement is **simultaneously** (i) sufficient local mixing under every finite coloring of boundary labels to pass (1.2)–(1.3) and the full finite-cover test, and (ii) a nontrivial Boolean residual in which no tail-preserving compatible maps are dense. Neither test supplies such a structure.

**Status: working mathematics only.** Do not modify the externally checked theorem ledger or open-problem register based on this note.
