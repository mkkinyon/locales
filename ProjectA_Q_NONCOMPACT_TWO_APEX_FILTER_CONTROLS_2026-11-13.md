# Project A — noncompact two-apex filter controls: two opposite no-go mechanisms

> **Later 13 Nov generalization:** The [filtered-apex/clopen-gluing theorems](ProjectA_Q_FILTERED_APEX_REGULAR_ARMS_AND_CLOPEN_GLUE_NO_GO_2026-11-13.md) show that **all** regular Hausdorff arms with arbitrary decreasing tails are Q′-positive; this supersedes the suggestion in §5 below that merely mixing dense and nondense rational tails may help. Disjoint clopen anti-Urysohn cloud replacements fail too. The explicit models here remain correct negative controls.

**13 November 2026. Bounded working research segment; internally checked, not independently audited.** This begins [Priority 1](ProjectA_Q_POSTREFEREE_PRIORITIES_2026-11-13.md) after the external referee's compact two-apex N6. It constructs explicit **noncompact, countably based, sober T₁** spaces and finds why the two easiest modifications fail to test Q′. It neither proves nor refutes universal Q or Q′.

## 1. A preliminary scattered-support stop rule

**Lemma 1.1 (existing Cantor–Bendixson machinery).** If X is sober, spatial, T₁ and scattered, then D₂(X)=D(X), hence W₂(X)=W(X).

Reason: a weak D₂>D witness gives a finite-compatible Boolean pair h,k and a full cover matched to zero. Normalize to the pair's least closed coordinate support K, and apply the already established transfinite isolated-point elimination: an endpoint component supported on an isolated singleton is excluded by one-sided compact rigidity. If K is scattered, its perfect derivative is empty, forcing h=k=0 contrary to a nonzero target. The argument is the **weak** (D₂>D) version of the Cantor–Bendixson obstruction, not a proof that every space is scattered.

**Corollary 1.2.** A **countable, T₁, completely Baire, sober** space has D₂=D. Indeed every nonempty closed subspace is countable T₁ Baire, hence must have an isolated point: otherwise it is a countable union of closed nowhere-dense singletons, contradicting the Baire property. So X is scattered. In particular, countable T₁ quasi-Polish spaces cannot furnish a Q′ counterexample (quasi-Polish closed subspaces are quasi-Polish and Baire; see de Brecht, [Quasi-Polish Spaces](https://arxiv.org/abs/1108.1445)). A countable T₁ candidate must either abandon complete Baireness or fail to be a meaningful counterexample.

Thus merely replacing isolated sequences by more complicated **scattered** tails is insufficient, even if compactness disappears.

## 2. A uniform filtered two-arm construction

Let T be a nonempty Hausdorff space and let G₀⊇G₁⊇⋯ be nonempty open subsets of T with ∩_n G_n=∅. Take disjoint copies T_+, T_- and three new points a,b,t. Define

\[
X(T,G)=T_+\amalg T_-\amalg\{a,b,t\},
\]

with ordinary opens on each arm and basic apex neighbourhoods

\[
A_n=\{a\}\cup (G_n)_+,\qquad
B_n=\{b\}\cup (G_n)_-,\qquad
T_n=\{t\}\cup (G_n)_+\cup(G_n)_-.
\]

Intersections of basis elements are open, e.g. A_n∩T_m=(G_{\max(n,m)})_+. Because ∩G_n=∅, each apex has a neighbourhood omitting any prescribed ordinary arm point. Thus X is T₁; it is countably based if T is countably based.

**Sobriety.** Let F be nonempty irreducible closed. If F meets an arm in two points, disjoint arm-open neighbourhoods contradict irreducibility (T is Hausdorff). If F meets an arm in exactly one point x and also contains some other point, take an arm-open neighbourhood of x, and a neighbourhood of the other point omitting x; their traces on F do not meet. Thus F is either a singleton or contained in the finite T₁ subspace {a,b,t}, where it is again a singleton. Hence X is sober. This argument does not assume its localic square is spatial.

The model retains a nontrivial **three-apex convergence geometry**, since every A_n and B_m has t in its closure whenever each G_n is nonempty: every t-neighbourhood meets both A_n and B_m on an arm tail.

## 3. Cofinal rational tails: genuinely noncompact and W₂<U, but D₂=D

Take T=ℚ with its usual topology, and G_n=(n,\infty)∩ℚ, n≥0. Write X_cof=X(ℚ,G).

**Noncompactness.** The open family consisting of A₀,B₀,T₀ and, in both rational arms, the bounded intervals (−n,n)∩ℚ for n≥1, covers X_cof. No finite subfamily covers the negative unbounded part of either arm.

**A strict rank-one calculation.** Put F={T_+,T_-,A₀,B₀,T₀}, a **finite** X-cover, and r=A₀⊠B₀. In the localic square,

\[
r\wedge w_F=(G_0)_+\boxtimes(G_0)_-
\le T_+\boxtimes T_-\le z_X.
\]

The last inclusion is not an appeal to square spatiality: every arm open is the union of bounded rational intervals, and the closures in X of bounded intervals in opposite arms are disjoint. Therefore every pure rectangle between such bounded opens is far, so the full cross-arm rectangle lies under the far open z_X.

On the other hand, the ordinary point-pair (a,b) belongs to r but not to z_X: every neighbourhood of a and of b has t in its closure, so their closures cannot be disjoint. Hence

\[
\boxed{r\le w_F\to z_X\le\Phi_{2,X}(z_X),\quad r\nleq z_X,}
\]

and consequently

\[
\boxed{\Phi_{2,X}(z_X)>z_X,\qquad W_2(X)<U(X).}
\]

This is a bona fide **noncompact rank-one nonstabilization control**.

**But full fitting already equals finite fitting.** Every nonzero closed subspace K of X_cof has a nonzero open patch V contained in a closed subspace J⊆K which is compact or regular:

- If K meets an ordinary arm, choose x∈K∩T_± and a bounded rational interval I around x. The nonzero open V=K∩I has closure J=cl_K V wholly within that arm, because sufficiently late G_n miss I. As a closed subspace of the regular Hausdorff space ℚ, J is regular.
- If K misses both arms, it is a nonempty subspace of {a,b,t}, hence finite T₁, discrete and compact.

The previously established **hereditary compact/regular patch criterion** (the weak D₂>D normalization plus one-sided rigidity; Q′ pre-nucleus note, Cor. 4.3) therefore gives

\[
\boxed{D_2(X_{\rm cof})=D(X_{\rm cof}),\quad
W_2(X_{\rm cof})=W(X_{\rm cof})<U(X_{\rm cof}).}
\]

**Moral:** lack of global compactness and nontrivial Φ₂-rank do **not** suffice. Regular patches on *every* nonzero closed coordinate support eliminate the infinitary fitting defect. The displayed strict W₂<U uses actual locale opens and one ordinary witness point; it does not rely on product-square spatiality.

## 4. Dense rational tails: noncompact, perfect arms, but z=0

Take a sequence D={d_m:m∈ω}⊆ℚ converging in ℝ to an irrational, with distinct d_m. This D is an infinite closed discrete nowhere-dense **noncompact** subset of ℚ. Enumerate ℚ\D={q_0,q_1,…}; put F_n=D∪{q_0,…,q_n} and G_n=ℚ\F_n.

Every G_n is dense open, nonempty and decreasing, and ∩G_n=∅. Let X_dense=X(ℚ,G). It is countably based, sober, T₁, and noncompact: a cover by A₀,B₀,T₀ and sufficiently small arm-open intervals around points of F₀ has no finite subcover, since F₀ includes the infinite closed discrete D.

But every nonempty X_dense-open has a nonempty rational arm-open part. Every t-neighbourhood T_n meets every such arm-open, because G_n is dense in each rational arm. Thus **t belongs to the closure of every nonempty open of X_dense**. No two nonempty opens have disjoint closures, i.e. z_X=0. The rank-zero identity Φ(0)=Φ₂(0)=z now gives

\[
\boxed{W(X_{\rm dense})=W_2(X_{\rm dense})
=U(X_{\rm dense})=X_{\rm dense}^2.}
\]

**Moral:** making the tails dense enough to destroy regular patches may instead make U universal, so the desired higher-rank obstruction disappears. This is a Q- and Q′-positive control for an entirely different reason than in §3.

## 5. Research consequence and next design constraint

The two simplest substitutions for the compact N6 tails fail in opposite ways:

| Tail choice | Noncompact? | Rank-one behavior | Why Q′ survives |
| --- | --- | --- | --- |
| Ordinary cofinal tails in ℚ | Yes | Φ₂(z)>z; W₂<U | Every closed support has a regular or compact nonzero patch, so D₂=D |
| Dense open tails in ℚ | Yes | z=0; W=W₂=U | Anti-Urysohn collapse from t lying in every nonempty open's closure |

The next candidate should have all of the following *on the prospective normalized closed support*, not merely globally:

1. **Non-scattered, noncompact, nowhere locally compact/regular-support geometry** that escapes the one-sided stop rule.
2. **Nonzero far opens** and genuine \(\Phi_2\)-rank structure; avoid a universal U relation caused by one point lying in all nonempty closures.
3. A cover C for which the weak D₂>D defect has **nonzero relatively open interior inside W₂**. Neither a graph obstruction nor a bad finite cover alone suffices.

One plausible next bounded construction is to replace the rational arms by **nonregular crowded attached cores** with tail filters that are dense on selected supports but not on every nonempty open. This is a research direction, not a theorem, and may fail for the same local-patch or anti-Urysohn reasons.

**Status:** these are two mathematically informative **negative controls**, not a Q or Q′ counterexample. A separate external audit would be prudent before using the strengthened general class claims as published results.
