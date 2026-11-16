# Addendum to the independent blind referee report

**Project A — Sphere plateaux and unit differentials in clean cover-insertion filtrations**  
**Date:** 16 November 2026  
**Subject:** Iterating the relative construction to prescribe the birth time of a sphere plateau

These remarks arose after completion of the independent blind referee report. They are additional mathematical suggestions, not corrections to that report. In particular, the filtration-shift formulation below has **not** undergone a separate adversarial audit.

## 1. A repeatable filtration-shift operation

The relative construction in §6 of the original packet appears to be an instance of a more general operation.

Let `Y` be a finite poset with marked covers, one of which begins at a minimal vertex `b`. Assume that deleting `b` leaves a poset with an **unmarked cone minimum** `c`: thus `Y-b={c}⊕W`, and no inherited marked edge has endpoint `c`. At every filtration level,

\[
F_p(Y-b)=c*F_p(W).
\]

Construct `T(Y)` by adjoining two incomparable minima `s,t` below every element of `Y` and marking the new cover `s<b`, leaving all old marks unchanged. The new initial marked vertex is `s`.

**Filtration-shift claim.** For every `p>=1`,

\[
\boxed{F_p(T(Y))\searrow\Sigma F_{p-1}(Y).}
\tag{1}
\]

In addition, `F_0(T(Y))` is collapsible. Whenever the old inclusion `F_{p-1}(Y) -> F_p(Y)` is a homotopy equivalence, the new inclusion `F_p(T(Y)) -> F_{p+1}(T(Y))` is a homotopy equivalence.

Here `Sigma` denotes the simplicial suspension `S^0* -`. The collapse in (1) is a collapse **of one filtration stage to a suspension model**, not a collapse between consecutive filtration stages.

### Proof sketch

Set

\[
D_p=F_{p-1}(Y)\cup F_p(Y-b),\qquad p\ge1.
\]

Separating chains according to the new minima gives

\[
F_p(T(Y))=(t*F_p(Y))\cup(s*D_p),
\qquad (t*F_p(Y))\cap(s*D_p)=D_p.
\tag{2}
\]

Also,

\[
F_{p-1}(Y)\cap F_p(Y-b)=F_{p-1}(Y-b).
\]

Since `Y-b` is a filtered cone with unmarked apex `c`, pair `(c*sigma,sigma)` for every simplex `sigma` of `W` having marked weight exactly `p`, in decreasing order of dimension. These pairs collapse `F_p(Y-b)` onto `F_{p-1}(Y-b)`. They remain free after adjoining `F_{p-1}(Y)`, because a weight-`p` simplex has no coface of weight at most `p-1`. Hence

\[
D_p\searrow F_{p-1}(Y).
\tag{3}
\]

Apply the cone-reduction lemma from §9 of the referee report to (2):

\[
F_p(T(Y))\searrow (t*D_p)\cup(s*D_p)
=\Sigma D_p\searrow\Sigma F_{p-1}(Y),
\]

proving (1). The last collapse uses the fact that simplicial suspension preserves elementary collapses.

At filtration zero, the link of `s` in `F_0(T(Y))` is `F_0(Y-b)`, a cone. Deleting `s` collapses the complex onto `t*F_0(Y)`, also a cone. Thus `F_0(T(Y))` is collapsible.

Finally, the inclusions `F_{p-1}(Y)->D_p` and `F_p(Y)->D_{p+1}` are homotopy equivalences by (3). Their squares with `D_p -> D_{p+1}` commute, so the old inclusion equivalence implies that `D_p -> D_{p+1}` is an equivalence. Applying the homotopy-pushout gluing lemma to (2) at the two levels gives the asserted equivalence of the *actual* new inclusions.

Crucially, the operation is repeatable:

\[
T(Y)-s=\{t\}\oplus Y,
\]

and `t` is again an unmarked cone minimum. Thus `T(Y)` satisfies the same deletion hypothesis as `Y`.

## 2. Iteration and arbitrary birth times

Begin with the **uncapped** extension `U` of the capped example `X_r`, where `r>=3`. It has `r+1` marks and `3r+2` vertices. Its deletion of the initial marked vertex `u` is `U-u={v}⊕X_r`, with unmarked cone minimum `v`. The audited theorem shows that its filtration has the homotopy type `S^r` at levels `0,...,r`, with all intermediate inclusions homotopy equivalences; its terminal stage `r+1` is contractible.

For an arbitrary integer `k>=0`, iterate the new operation:

\[
Y_k=T^k(U).
\]

It has

\[
m=r+1+k\quad\text{marked covers},\qquad
3r+2+2k\quad\text{vertices}.
\]

Repeated application of (1), together with the base-case assertions for `U`, yields

\[
\boxed{
\begin{aligned}
F_p(Y_k)&\simeq * &&(0\le p<k),\\
F_p(Y_k)&\simeq S^{r+k} &&(k\le p<m),\\
F_m(Y_k)&\simeq *.
\end{aligned}}
\tag{4}
\]

The pre-birth stages are actually collapsible by induction; their inclusions are homotopy equivalences. The inclusions along the sphere plateau are homotopy equivalences by the shift lemma. Consequently the only nonzero reduced persistent-homology interval is

\[
\boxed{[k,r+1+k)}
\]

in homological degree `r+k`.

## 3. The integral spectral-sequence consequence

Write `m=r+1+k`. The reduced absolute homological spectral sequence has precisely two nonzero `E^1` terms:

\[
E^1_{k,r}\cong\mathbb Z,
\qquad
E^1_{m,0}\cong\mathbb Z.
\]

Their only possible connecting differential is

\[
\boxed{
d_{r+1}:E^{r+1}_{r+1+k,0}
\longrightarrow E^{r+1}_{k,r}.
}
\tag{5}
\]

The final order complex is contractible, since each operation adjoins two incomparable minima and hence suspends the preceding full order complex. As in the original unit-differential proof, the reduced abutment vanishes; therefore (5) is an isomorphism of two infinite cyclic groups, necessarily multiplication by `+1` or `-1`.

Equivalently, put `d=r+1`. For **every `d>=4` and `k>=0`**, the method gives a clean cover-insertion filtration with

- a unique nonzero reduced persistence interval `[k,k+d)`;
- a unique nonzero differential `d_d: Z -> Z`, of coefficient `±1`;
- `d+k` marked covers and `3d+2k-1` vertices.

When `k=0`, this recovers the uncapped absolute family. When `k=1`, it recovers the relative family in the audited packet. Higher values give genuinely later birth times without increasing the page of the nonzero differential.

## 4. Significance and suggested presentation

The construction separates two parameters:

1. **Differential length**, controlled by the original capped examples.
2. **Birth time**, controlled by iterating the two-minimum extension.

It therefore gives a more systematic picture of which individual finite persistence intervals can be realized by these clean Boolean cover-insertion filtrations. A natural way to incorporate the observation is to formulate the filtration-shift claim as a lemma independently of the special family `X_r`, then state its iteration as a corollary.

This is an additional mathematical direction, **not** a newly discovered problem in the originally audited arguments. Apart from it, I have no further mathematical reservations or suggestions beyond those already recorded in the referee report.
