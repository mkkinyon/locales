# Project A — Consolidation of the post-\(\mathcal V\) relational-hierarchy work

**Date:** 24 October 2026  
**Scope:** Work after the extended \(\mathcal V\)-characterization/finite-rank/regular-filter investigation, chiefly the upper diamond, \(\mathcal H\), formal alternating hulls, and the lower diamond.  
**Status:** A research consolidation, **not** a blanket certification. Several claims below remain working results requiring external audit. The companion *internal adversarial audit* distinguishes established dependencies from newly asserted implications.

## 1. Notation and motivation

For a locale \(X\), write \(L=\mathcal O(X)\), \(Q=L\oplus L=\mathcal O(X\times_{\mathrm{loc}}X)\), and \(\Delta\) for its diagonal sublocale. The standing relations are

\[
\mathcal I=\operatorname{cl}(\Delta)=C(d_{\mathcal I}),\qquad
\mathcal D=\operatorname{fit}(\Delta),\qquad
\mathcal U=C(d_{\mathcal U}),\qquad
\mathcal V=\operatorname{fit}(\mathcal I),\qquad
\mathcal F=\bigwedge_{f:X\to\mathbb R}\ker(f),
\]
\[
\mathcal M=\mathcal I\wedge\mathcal D,\qquad
\mathcal J=\mathcal I\vee\mathcal D,\qquad
\boxed{\mathcal W=\operatorname{cl}(\mathcal D)},\qquad
T(S)=\operatorname{cl}(S)\wedge\operatorname{fit}(S).
\]

Here \(d_{\mathcal I}=\bigvee_{a\wedge b=0}a\boxtimes b\), and \(d_{\mathcal U}=\bigvee_{a^*\vee b^*=1}a\boxtimes b\). The latter expression uses pseudocomplements in \(L\). Let \(\mathcal H\) be the **least simultaneously closed and fitted sublocale** containing \(\Delta\). We compare sublocales by inclusion, not nuclei order.

**Recorded motivation (user's clarification).** The long exploration of \(\mathcal V\) was not merely aesthetic. Although \(\mathcal U=\operatorname{cl}(\mathcal D)\) and \(\mathcal V=\operatorname{fit}(\mathcal I)\) are formal counterparts in coherent locales, the first equality **fails in noncoherent locales**. Thus \(\operatorname{fit}(\mathcal I)\) may not be the intrinsically appropriate dual of the *actual* \(\mathcal U\) in arbitrary locales. The notation \(\mathcal V\) remains unchanged, and \(\mathcal W\) records the literal cross-hull.

## 2. Universal relations, and the two diamond questions

Independently of coherence,

\[
\mathcal I,\mathcal D\ \subseteq\ \mathcal J\ \subseteq\ \mathcal U,\mathcal V,
\qquad \mathcal W\subseteq\mathcal U,
\qquad T(\mathcal J)=\mathcal W\wedge\mathcal V\subseteq\mathcal U\wedge\mathcal V,
\]
\[
\boxed{\mathcal W\vee\mathcal V\subseteq\mathcal H\subseteq\mathcal F.}
\]

Also
\[
\operatorname{cl}(\mathcal W\vee\mathcal V)=\operatorname{cl}(\mathcal V),\qquad
\operatorname{fit}(\mathcal W\vee\mathcal V)=\operatorname{fit}(\mathcal W).
\]

The equality \(\mathcal J=\mathcal U\wedge\mathcal V\) was **already refuted** by finite Alexandrov examples. The more precise coherent identity is
\[
\mathcal U\wedge\mathcal V=T(\mathcal J),
\]
which motivated the unrestricted lower-diamond question. Likewise \(\mathcal U\vee\mathcal V=\mathcal F\) was already refuted by a finite six-point zigzag.

**New post-\(\mathcal V\) findings (working):**

* \(\mathcal U\vee\mathcal V\subseteq\mathcal H\) is **not** universal. There is no universal inclusion in the reverse direction either. The genuine universal formal diamond uses \(\mathcal W\vee\mathcal V\), not \(\mathcal U\vee\mathcal V\).
* \(T(\mathcal J)=\mathcal U\wedge\mathcal V\) also fails outside coherence; we have both a noncompact almost-normal construction and a far simpler **compact** counterexample.

## 3. A coherent graph interpretation of \(\mathcal H\) and \(\mathcal F\)

Let \(X\) be coherent, with spectral point space \(P\) and compact Hausdorff Priestley patch topology \(P_{\mathrm p}\). Let \(\sim_c\) be finite-path connectivity in the undirected comparability graph of the specialization order. A relation on \(P^2\) is *coordinatewise comparability-saturated* if it is invariant under moving either coordinate along finitely many comparisons.

**Working coherent theorem.** The ordinary points of \(\mathcal H\) form the **smallest patch-closed, coordinatewise comparability-saturated relation containing the diagonal**, and those of \(\mathcal F\) form the **smallest patch-closed equivalence relation containing \(\sim_c\)**. Each claimed point set determines an actual closed sublocale of the coherent localic square. The proof uses the Priestley compact-open presentation of fitted sublocales, as well as compact-Hausdorff quotients of closed equivalence relations.

One consequence is the proposed coherent equivalence
\[
\boxed{\mathcal H\text{ internally transitive}\iff\mathcal H=\mathcal F.}
\]

This should be distinguished from the false assertion that \(\mathcal H\) is always transitive.

### The two convergent alternating rays

Let \(P=A\sqcup B\sqcup\{t\}\), with \(A=\{a_n:n\ge0\}\) and \(B=\{b_n:n\ge0\}\). In each ray impose the alternating adjacent comparisons
\[
a_{2n}<a_{2n+1},\quad a_{2n+2}<a_{2n+1},
\]
and analogously on \(B\). There are no comparisons across rays or with \(t\). Give \(P\) the patch topology of the one-point compactification of the discrete rays, with both rays converging to \(t\).

This is a Priestley space. Define the relation
\[
R=(A\cup\{t\})^2\cup(B\cup\{t\})^2.
\]
It is the point set of a **closed and fitted** sublocale, and the working proof gives \(\mathcal H=R\). We have \((a_0,t),(t,b_0)\in R\), but \((a_0,b_0)\notin R\). This witnesses failure of localic transitivity. Every continuous real-valued function is constant, so \(\mathcal F=X^2\). Coherent separation and the common-upper/common-lower formulas yield
\[
\boxed{\mathcal U\vee\mathcal V\subsetneq\mathcal H\subsetneq\mathcal F.}
\]

**Main audit dependency:** patch-closed upsets must be shown to define *genuine fitted coherent sublocales*, and excluding a point from \(\mathcal U\vee\mathcal V\) must use an actual compact-open separator, not the set-theoretic union of point relations.

## 4. A frame iteration for the formal hull

For \(a\in Q\), define
\[
\mathcal F_a=\{w\in Q:a\vee w=1\},\quad
\operatorname{Fix}_a=\{x\in Q:\forall w\in\mathcal F_a,\ w\to x=x\},\quad
\kappa(a)=\bigwedge\operatorname{Fix}_a.
\]
The fitted sublocale \(\operatorname{fit}(C(a))\) has the common fixed-point frame \(\operatorname{Fix}_a\), hence
\[
\operatorname{cl}(\operatorname{fit}(C(a)))=C(\kappa(a)).
\]
The operator \(\kappa\) is monotone and deflationary; \(\kappa(a)=a\) iff \(C(a)\) is fitted. Iterate
\[
a_0=d_{\mathcal I},\qquad a_{\alpha+1}=\kappa(a_\alpha),\qquad
a_\lambda=\bigwedge_{\alpha<\lambda}a_\alpha.
\]
At its fixed point \(a_\infty\), the working argument proves
\[
\boxed{\mathcal H=C(a_\infty).}
\]
At limit ordinals, the closed stage is the **closure of the join** of earlier closed stages; the join itself need not be closed.

In a coherent spectral locale, if \(S_\alpha\) denotes the point set of \(C(a_\alpha)\), then the working Priestley recursion is
\[
S_0=\mathcal I_{\mathrm{pt}},\quad
S_{\alpha+1}=\downarrow\!\uparrow S_\alpha,\quad
S_\lambda=\downarrow\overline{\bigcup_{\alpha<\lambda}S_\alpha}^{\mathrm{patch}}.
\]
Since \(\downarrow\uparrow R=\mathcal I_{\mathrm{pt}}\circ R\circ\mathcal I_{\mathrm{pt}}\),
\[
S_n=\mathcal I_{\mathrm{pt}}^{\,2n+1},\qquad
S_\omega=\downarrow\overline{\sim_c}^{\mathrm{patch}}.
\]

The two-ray example first stabilizes at \(\omega\). A second family attaches a finite alternating zigzag \(t_0<t_1>t_2<\cdots>t_{2m}\) to the infinite zigzag **only by patch convergence to \(t_0\)**, not an order comparison. Its proposed exact stages are
\[
S_{\omega+k}=A^2\cup T^2\cup(A\times T_k)\cup(T_k\times A),\quad
T_k=\{t_0,\ldots,t_{2k}\},\quad0\le k\le m,
\]
and stabilization first occurs at \(\omega+m\). These are *stage-height* statements, not claims about all possible alternation schedules or publication novelty.

## 5. Unrestricted upper diamond: the compact \(T_1\) example

Revisit the previously investigated compact, locally compact, sober, scattered, noncoherent \(T_1\) space with two countably infinite isolated sheets \(N_1,N_2\) and three limit points \(\alpha,\beta,\gamma\). Neighborhoods at \(\alpha\) contain a cofinite \(N_1\)-tail, at \(\gamma\) a cofinite \(N_2\)-tail, and at \(\beta\) cofinite tails of **both** sheets. The earlier independent audit verified the strict failure \(\operatorname{cl}(\mathcal D)<\mathcal U\), not the entire new hierarchy calculation.

The new working calculation invokes the scattered-sublocale theorem for the spatial localic square, to obtain
\[
\boxed{\mathcal D=\Delta,\quad
\mathcal V=\mathcal I=\mathcal W=\mathcal H,\quad
\mathcal I\subsetneq\mathcal U=\mathcal F.}
\]
On the three-point boundary, \(\mathcal I\) has the path \(\alpha-\beta-\gamma\), while \(\mathcal U\) completes the endpoint edge \(\alpha-\gamma\). Thus
\[
\mathcal U\vee\mathcal V\not\subseteq\mathcal H.
\]
The opposite universal inclusion fails in the six-point coherent zigzag (and in the convergent-rays example). Hence **\(\mathcal U\vee\mathcal V\) and \(\mathcal H\) are incomparable as universal constructions**. The corrected formal upper diamond is \(\mathcal W\vee\mathcal V\le\mathcal H\).

A useful general lemma employed here: for a \(T_1\) space with spatial scattered localic square, every separated ordinary pair is excluded by a rank-two bar. Point-determination then yields \(\mathcal V=\mathcal I\), \(\mathcal D=\Delta\), and \(\mathcal H=\mathcal I\).

## 6. Lower diamond: counterexamples and positive criteria

### Noncompact almost-normal thickening

For the finite seed poset \(P=\{p,q,t,x,y\}\), with only \(p<t,p<x,q<t,q<y\), one has \(\mathcal V(P)=P^2\) but \(\mathcal U(P)=P^2\setminus\{(x,y),(y,x)\}\). Applying the earlier almost-normal rational-cloud thickening \(X(P)=(P\times\omega^{\mathrm{op}})\sqcup S\), the new working *boundary-transfer* calculation gives \(\mathcal W_{X(P)}\) the point relation \(\mathcal U(P)\) on the boundary while \(\mathcal U=\mathcal V=\mathcal F\) globally. Therefore
\[
\boxed{T(\mathcal J)=\mathcal W\subsetneq\mathcal U\wedge\mathcal V=\mathcal F.}
\]
This inherits technical dependencies from the original almost-normal construction and its focused internal audit.

### A simpler *compact* counterexample

Let \(X=S_1\sqcup S_2\sqcup\{p,x,y\}\), where \(S_1,S_2\) are countably infinite isolated sheets, with neighborhood bases
\[
\begin{aligned}
N_p(E_1,E_2)&=\{p,x\}\cup(S_1\setminus E_1)\cup(S_2\setminus E_2),\\
N_x(E_1)&=\{x\}\cup(S_1\setminus E_1),\\
N_y(E_2)&=\{y\}\cup(S_2\setminus E_2),
\end{aligned}
\]
for finite \(E_i\subseteq S_i\). Its only nontrivial specialization comparison on the boundary is \(p<x\); it is countable, compact, locally compact, sober, scattered, \(T_0\), and noncoherent.

The working *complete* hierarchy is
\[
\boxed{
\Delta\subsetneq\mathcal D=\mathcal M
\subsetneq\mathcal I=\mathcal J=\mathcal W=T(\mathcal J)
\subsetneq\mathcal U=\mathcal V=\mathcal H=\mathcal F.}
\]

The extra off-diagonal \(\mathcal D\)-pair is \((p,x)\), via the common specialization predecessor \(p\). Inseparability adds \((p,y)\) via common cofinite \(S_2\)-tails. The remaining pair \((x,y)\) is separable by \(\{x\}\cup S_1\) and \(\{y\}\cup S_2\), but belongs to \(\mathcal U\) because every pair of these neighborhoods has intersecting closures at \(p\), and belongs to \(\mathcal V\) by upward specialization from \((p,y)\in\mathcal I\). Every real function identifies \(p,x,y\), and clopen sheet singletons distinguish all other pairs.

Since \(X\) is locally compact sober and its ordinary square is scattered, the localic product is spatial and every sublocale is point-determined. The rectangle \((\{x\}\cup S_1)\boxtimes(\{y\}\cup S_2)\) contains no \(\mathcal D\)-point, so \((x,y)\notin\mathcal W\); this yields \(\mathcal W=\mathcal I\).

**Compactness alone does not force lower-diamond equality.** The example is neither \(T_1\) nor almost normal.

### Exact equality criteria

For all locales,
\[
\begin{aligned}
\mathcal V\subseteq\mathcal U&\implies
[T(\mathcal J)=\mathcal U\wedge\mathcal V\iff\operatorname{cl}(\mathcal V)=\mathcal W],\\
\mathcal U\subseteq\mathcal V&\implies
[T(\mathcal J)=\mathcal U\wedge\mathcal V\iff\mathcal W=\mathcal U].
\end{aligned}
\]
If \(\mathcal I\) is fitted, both sides of the lower-diamond equality equal \(\mathcal I\). For a sober \(T_1\) space with spatial localic square, if \(\mathcal V\) is spatial, it coincides with \(\mathcal I\), because each separated product point is omitted by a bar. In particular locally compact sober scattered \(T_1\) spaces satisfy lower-diamond equality.

## 7. Outstanding questions and audit targets

* Are the general coherent Priestley/compact-open spatiality arguments fully sound? Does \(\mathcal H\) transitivity iff \(\mathcal H=\mathcal F\) hold without a hidden passage from ordinary points to locale images?
* Do the exact \(\omega+m\) ordinal examples have the stated first stabilization stage with correct limit closure?
* Can all three noncoherent example calculations be proved at the **localic** level as claimed using the scattered-sublocale theorem, including \(\mathcal W=\mathcal I\) and \(\mathcal U=\mathcal V=\mathcal F\)?
* Does compact almost-normality force lower-diamond equality? What about compact \(T_1\) spaces without stronger point-determination?
* Could \(\mathcal H\), or a related mixed hull, admit a useful formulation without the explicit localic-square construction?

## 8. Source map (internal, for provenance)

Relevant repository files in `mkkinyon/locales`:

- `A-V-conceptual-motivation-noncoherent-asymmetry-2026-10-24.md`
- `A-H-two-convergent-zigzag-rays-nontransitive-coherent-counterexample-2026-10-24.md`
- `A-H-upper-diamond-unrestricted-failure-compact-T1-2026-10-24.md`
- `A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md`
- `A-lower-diamond-strict-almost-normal-2026-10-24.md`
- `A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md`
- `A-V-thickened-zigzag-focused-audit-2026-10-23.md`
- `A-Claude-three-claims-focused-verification-2026-10-21.md`
- `A-lower-diamond-compact-three-point-working-note.md` (local standalone note)

**Warning:** This document is a map of claims and dependencies, not a substitute for the independent proof assessment below.