# Project A — Sphere plateaux and unit differentials in clean cover-insertion filtrations

**Independent blind audit packet, 16 November 2026.** These assertions concern ordinary order complexes filtered by marked covers. They do **not** concern a crosscut Čech spectral sequence. This note does not assert novelty, optimal sizes, or a result for arbitrary sets of marked covers.

## 1. Setup and precise claims

Let `Q` be a finite poset and `E` a set of its covers. Remove the strict inequalities in `E` to form `P=Q\E`. Because a cover has no intermediate point, removing any subset of these inequalities preserves transitivity: the marked covers are a *clean Boolean insertion family*.

For a chain simplex `sigma` of `Delta Q`, let `w(sigma)` count marked covers whose two endpoints belong to `sigma`, and let

\[
 F_p(Q)=\{\sigma\in\Delta Q:w(\sigma)\le p\},\quad p\ge0.
\]

This is a simplicial filtration with `F_0(Q)=Delta P`. Chains are oriented by their poset order when signs matter, and homological spectral-sequence differentials have bidegree
\[
 d_s:E^s_{p,q}\longrightarrow E^s_{p-s,q+s-1}.
\]
All homology groups below have coefficients in `Z`.

We construct recursively a **capped** finite poset `X_r`, with `r>=3` marked covers forming a path from a minimal element `b_r` to a maximal element. Define
\[
 A_{r,p}=F_p(X_r),\qquad B_{r,p}=F_p(X_r-\{b_r\}),
\]
using the inherited marks for the deletion. Write `searrow` for a sequence of elementary simplicial collapses.

**Theorem A (absolute plateau and deletion collapse).** For every `r>=3`:

1. `Delta X_r` is contractible; `A_{r,0} searrow B_{r,0}`.
2. `B_{r,p} searrow B_{r,p-1}` for every `1<=p<=r-1` (hence the inclusion `B_{r,0} -> B_{r,p}` is a simple homotopy equivalence).
3. `B_{r,p}` has homotopy type `S^{r-1}` for every `p>=0`.
4. Every inclusion `A_{r,p-1} -> A_{r,p}` is a homotopy equivalence for `1<=p<=r-1`. Consequently `A_{r,p} ~= S^{r-1}` for `0<=p<=r-1`, whereas `A_{r,r}=Delta X_r` is contractible.

The *uncapped* intermediate extensions have the same filtration-level homotopy types and inclusion equivalences as the corresponding capped extension, via a collapse removing the cap at every level.

**Theorem B (relative plateau).** Starting from `X_r`, form the uncapped extension `U` with `r+1` marks, then add two new incomparable minima `s,t` below `U`, marking `s<u`. Let `Q` be the resulting poset, with `m=r+2` marks. Then `F_0(Q)` and `F_m(Q)` are contractible, and
\[
 F_p(Q)\simeq S^{m-1}\quad(1\le p\le m-1),
\]
with every inclusion `F_p(Q) -> F_{p+1}(Q)` for `1<=p<=m-2` a homotopy equivalence.

**Corollary (unit long differentials).** In the *reduced absolute* homological spectral sequence for `X_r`, the only nonzero `E^1` terms are `Z` in bidegrees `(0,r-1)` and `(r,0)`. The unique nonzero differential is
\[
 d_r:E^r_{r,0}\xrightarrow{\ \cong\ }E^r_{0,r-1},
\]
and is multiplication by `+1` or `-1` after choosing generators. In the *relative* spectral sequence of `(Delta Q,F_0(Q))`, the only nonzero `E^1` terms are `Z` at `(1,m-2)` and `(m,0)`, joined by an isomorphism
\[
 d_{m-1}:E^{m-1}_{m,0}\xrightarrow{\ \cong\ }E^{m-1}_{1,m-2}.
\]
For the ordinary unreduced absolute sequence there is additionally the permanent `H_0=Z` term at `(0,0)`.

Thus arbitrary differential lengths occur with *one isolated integral persistence interval*: `[0,r)` in reduced homological degree `r-1` (absolute), and `[1,m)` in degree `m-1` (relative). The capped absolute `X_r` has `3r` vertices; the uncapped absolute extension of length `r` has `3r-1` vertices; the relative example with `m` marks has `3m-2` vertices.

## 2. The nine-vertex seed and finite collapse certificates

The vertices of `X_3` are `a,b,c,d,e,f,h,i,x` with Hasse covers
\[
 a\prec d,x;\quad b\prec c,d;\quad x\prec c,e;\quad
 c\prec f;\quad d\prec e,f;\quad e,f\prec h,i,
\]
where the last clause denotes all four comparisons. Mark
\[
 E_3=\{a\prec d,\ d\prec f,\ f\prec i\},\qquad b_3=a.
\]
These are covers. The marked path starts at minimal `a` and ends at maximal `i`.

**Contractibility.** Put `M={a,b,c,d,e,f,x}`. We have `X_3=M \oplus {h,i}` (the last two form an antichain). In `M`, the lower link of `e` is the order complex of the path `x-a-d-b`, a contractible tree; `e` has no upper points in `M`. Deleting `e` therefore preserves homotopy type. The remainder of `M` has greatest element `f`. Hence `Delta M` is contractible, as is `Delta X_3=(Delta M)*S^0`.

**Collapse notation.** For compactness, `acfix`, for example, denotes the *set* `{a,c,f,i,x}` spanning a chain, not an asserted linear ordering of those letters. Each ordered pair `(beta,alpha)` means: remove simplex `beta` and its codimension-one free face `alpha`. In each displayed sequence the pairs are applied **in the order printed**.

Here are complete certificates for the two absolute preterminal stages:

| Collapse | Pairs `(beta,alpha)` in order |
|---|---|
| `A_{3,2} searrow A_{3,1}` | `(adfh,adf)`, `(bdfi,dfi)` |
| `A_{3,1} searrow A_{3,0}` | `(acfix,acfi)`, `(adeh,adh)`, `(adei,ade)`, `(adi,ad)`, `(afix,afi)`, `(bdfh,dfh)`, `(bcfi,bfi)`, `(cfix,cfi)`, `(bdf,df)`, `(fix,fi)` |
| `B_{3,2} searrow B_{3,1}` | `(bdfi,dfi)` |
| `B_{3,1} searrow B_{3,0}` | `(bdfh,dfh)`, `(bcfi,bfi)`, `(cfix,cfi)`, `(bdf,df)`, `(fix,fi)` |

For reference, `(number of nonempty simplices)` is
\[
 \begin{array}{c|rrr}
 &p=0&p=1&p=2\\\hline
 A_{3,p}&76&96&100\\ B_{3,p}&50&60&62
 \end{array}.
\]

The filtration-zero deletion `B_{3,0}` has f-vector `(8,20,18,4)`. The following **additional** elementary collapses exhibit it as an octahedral sphere:

```
(bdeh,deh)   (bcfh,bfh)   (bdei,dei)   (cfhx,fhx)
(bde,de)     (bcf,bf)     (bdh,dh)     (cfh,fh)
(bdi,di)     (cfx,fx)     (bd,d)       (cf,f)
```

The remaining complex has the six vertices `b,x,c,e,h,i`, all twelve edges between distinct groups, and the eight facets
```
bch  beh  bci  bei  chx  ehx  cix  eix
```
This is precisely the boundary of the octahedron
\[
 S^0_{\{b,x\}}*S^0_{\{c,e\}}*S^0_{\{h,i\}}\cong S^2.
\]
Finally, the link of vertex `a` in `A_{3,0}` is a cone with apex `x`; hence `A_{3,0} searrow B_{3,0}`. The optional Python program verifies all these finite certificates from the Hasse relation and marked endpoints, but the argument should be checked independently.

## 3. Recursive capped extension

Assume `X=X_r`, with initial marked vertex `b=b_r` minimal in `X`. Add two incomparable new minima `u,v`, both below **every** vertex of `X`, and mark the new cover `u\prec b`. This gives the *uncapped* extension
\[
 U=\{u,v\}\oplus X.
\]
Then add a cap vertex `y` satisfying
\[
 u\prec y,\quad y\prec q\ \ (q\in X\setminus\{b\}),
 \quad y\parallel b,\quad y\parallel v.
\tag{3.1}
\]
Keep all old comparisons and marks; write `X_{r+1}=U\cup{y}`, `b_{r+1}=u`. The axioms define a poset: because `b` was minimal, there is no transitivity forcing `y<b`. New marks and old marks remain covers: `u<b` has no intermediate point (`y\parallel b`), and `y` cannot lie between endpoints of any old cover. The marked path length increases to `r+1`.

Since `Delta X` is contractible, `Delta U=S^0*Delta X` is contractible. The full link of the cap `y` in `Delta X_{r+1}` is the cone
\[
 u*\Delta(X\setminus\{b\}),
\]
so `Delta X_{r+1}` remains contractible.

**Filtered cap-collapse lemma.** For *every* `p`,
\[
 F_p(X_{r+1})\searrow F_p(U).
\tag{3.2}
\]
Every simplex involving `y` is of the form `y*sigma` or `u*y*sigma`, where `sigma` is a simplex of `Delta(X-b)`. The paired simplices have **equal weight**: they contain no `b`, hence never realize the new mark `u<b`. Pair `y*sigma` with `u*y*sigma`, processing the `sigma` in decreasing dimension. The absence of comparisons between `y` and `v,b` ensures these are free pairs. The collapse works simultaneously at every filtration level and commutes with filtration inclusions.

## 4. Collapse of all deletion-filtration steps

Deleting `u=b_{r+1}` leaves `v,y` and `X`. As the new mark `u<b` disappears, the inherited filtration is
\[
 \boxed{B_{r+1,p}=(v*A_{r,p})\cup(y*B_{r,p}),\qquad
 (v*A_{r,p})\cap(y*B_{r,p})=B_{r,p}.}
\tag{4.1}
\]

Assume by induction that `B_{r,p} searrow B_{r,p-1}`. Lift its elementary pairs `(beta,alpha)` to `(y*beta,y*alpha)` inside (4.1). They remain free in the union because a simplex containing `y` cannot contain `v` or `b`; its cofaces containing `y` correspond exactly to cofaces in `B_{r,p}`. After these removals the complex is
\[
 (v*A_{r,p})\cup(y*B_{r,p-1}).
\]
Now collapse the entire `v`-cone from `v*A_{r,p}` to `v*A_{r,p-1}`: for each old simplex `sigma` of weight exactly `p`, pair `(v*sigma,sigma)` in decreasing dimension. A removed simplex `sigma` cannot have a `y`-coface in `y*B_{r,p-1}`, whose simplices have weight at most `p-1`. This gives
\[
 \boxed{B_{r+1,p}\searrow B_{r+1,p-1}.}
\tag{4.2}
\]
At the old terminal step (`p=r`) the first part is vacuous because `B_{r,r}=B_{r,r-1}`, while the `v`-cone collapse still works. Thus (4.2) covers **all** nontrivial steps for `B_{r+1}`.

For `p=0`, formula (4.1) expresses `B_{r+1,0}` as the union of two cones along `B_{r,0}`. Because this union is a simplicial homotopy pushout,
\[
 B_{r+1,0}\simeq \Sigma B_{r,0}.
\tag{4.3}
\]
Together with the octahedral seed, this yields `B_{r,p} ~= S^{r-1}` at every stage.

The link of the new initial marked vertex `u` in `A_{r+1,0}` is `y*B_{r,0}`: a filtration-zero simplex containing `u` must avoid `b`. As this link is a cone, deletion is a simplicial collapse,
\[
 A_{r+1,0}\searrow B_{r+1,0}.
\tag{4.4}
\]
This settles the filtration-zero assertion.

## 5. Homotopy equivalences at every preterminal absolute stage

It remains essential to prove that the **actual inclusions** of stages are homotopy equivalences, not merely that all the spaces happen to have the same homotopy type.

For the uncapped extension `U`, define `D_0=B_{r,0}` and, for `p>=1`,
\[
 D_p=A_{r,p-1}\cup B_{r,p}.
\tag{5.1}
\]
The only new mark is `u<b`. A simplex containing `v` has no added marked edge, whereas one containing `u` gains one mark precisely when it contains `b`. Hence, *exactly*,
\[
 \boxed{F_p(U)=(v*A_{r,p})\cup(u*D_p),\qquad
 (v*A_{r,p})\cap(u*D_p)=D_p.}
\tag{5.2}
\]

For `p>=1`,
\[
 A_{r,p-1}\cap B_{r,p}=B_{r,p-1}.
\tag{5.3}
\]
By the deletion collapses (4.2), gluing `A_{r,p-1}` onto `B_{r,p}` along `B_{r,p-1}` leaves a collapse
\[
 D_p\searrow A_{r,p-1}.
\tag{5.4}
\]
These are inclusions of subcomplexes, so their induced homotopy equivalences are compatible with the inclusions as `p` changes.

At `p=1`, `D_0=B_{r,0} -> A_{r,0} -> D_1` is a composite of homotopy equivalences: the first is (4.4) (or its seed version), and the second is (5.4). Consequently `D_0 -> D_1` is a homotopy equivalence.

For `2<=p<=r`, the commuting square
\[
 \begin{array}{ccc}
 A_{r,p-2}&\longrightarrow&A_{r,p-1}\\
 \downarrow&&\downarrow\\
 D_{p-1}&\longrightarrow&D_p
 \end{array}
\]
has both vertical arrows homotopy equivalences by (5.4), and its top arrow is a homotopy equivalence by the induction hypothesis on the **old** absolute filtration. Therefore `D_{p-1} -> D_p` is a homotopy equivalence.

Each complex in (5.2) is the union of two simplicial cones meeting along `D_p`. Both cone inclusions between successive levels are homotopy equivalences (both source and target are contractible). The gluing lemma for these homotopy pushouts now implies
\[
 F_{p-1}(U)\hookrightarrow F_p(U)
 \quad\text{is a homotopy equivalence for }1\le p\le r.
\tag{5.5}
\]
The filtered cap collapses (3.2) transport (5.5) to the capped extension `X_{r+1}`. This proves the main absolute induction. The case `p=r+1` is **not** claimed: the final stage is the contractible full order complex.

## 6. Relative construction and complete plateau

From the capped `X_r`, first form its **uncapped** extension `U` as in Section 3. It has `r+1` marks and, by the preceding argument, `F_p(U) ~= S^r` and `F_{p-1}(U) -> F_p(U)` is a homotopy equivalence for all `0<=p<=r` and `1<=p<=r`, respectively. The full `Delta U` is contractible.

Add two incomparable minima `s,t` below all elements of `U`, marking the additional cover `s<u`, while preserving old marks. Set
\[
 Q=\{s,t\}\oplus U,\qquad m=r+2.
\]
All `m` marks lie on a path from the minimal `s` to the old maximal endpoint. As with the other steps, the new marked relation is a cover and does not change the old covers.

For `p>=1`, put
\[
 D'_p=F_{p-1}(U)\cup F_p(U-\{u\}).
\tag{6.1}
\]
Splitting chains according to which new minimum they contain gives
\[
 \boxed{F_p(Q)=(t*F_p(U))\cup(s*D'_p),\quad
 (t*F_p(U))\cap(s*D'_p)=D'_p.}
\tag{6.2}
\]
But `U-u=v*X_r`, with the original marks; therefore
\[
 F_p(U-u)=v*A_{r,p},\quad
 F_{p-1}(U)\cap(v*A_{r,p})=v*A_{r,p-1}.
\]
By pairing `(v*sigma,sigma)` for all old simplices `sigma` of weight `p` in descending dimension, we obtain
\[
 D'_p\searrow F_{p-1}(U).
\tag{6.3}
\]
The two summands of (6.2) are cones along `D'_p`, hence
\[
 F_p(Q)\simeq\Sigma D'_p\simeq\Sigma F_{p-1}(U).
\tag{6.4}
\]
Moreover, comparing the inclusions using the homotopy-pushout gluing lemma and (6.3) shows that `F_p(Q) -> F_{p+1}(Q)` is a homotopy equivalence for `1<=p<=r`.

At filtration zero,
\[
 F_0(Q)=(t*F_0(U))\cup(s*(v*A_{r,0})).
\]
The link of `s` is the cone `v*A_{r,0}`; delete `s` by a collapse. What remains is the cone `t*F_0(U)`. Thus `F_0(Q)` is **collapsible**, in particular contractible. The full `Delta Q=S^0*Delta U` is also contractible.

Since `F_{p-1}(U) ~= S^r` for `1<=p<=r+1=m-1`, (6.4) proves the relative plateau `S^{r+1}=S^{m-1}` and completes Theorem B.

## 7. Consequences for integral spectral sequences

For the absolute example, every successive relative group `H_*(A_{r,p},A_{r,p-1};Z)` with `1<=p<=r-1` vanishes because its inclusion is a homotopy equivalence. The initial `A_{r,0}` is `S^{r-1}` up to homotopy. Since `A_{r,r}=Delta X_r` is contractible, the pair long exact sequence gives
\[
 H_j(A_{r,r},A_{r,r-1};\mathbb Z)=
 \begin{cases}\mathbb Z&j=r,\\0&j\ne r.\end{cases}
\]
Thus the reduced absolute `E^1`-page has exactly the two groups specified in the corollary. The only possible differential is `d_r`. The abutment is zero in positive degrees, so this map must be an isomorphism `Z -> Z`, not multiplication by another nonzero integer.

For the relative example `(Delta Q,F_0(Q))`, the stage-one relative homology is the reduced homology of `F_1(Q)~=S^{m-1}`, because `F_0(Q)` is contractible. All intermediate successive relative groups vanish by the homotopy equivalences. The last pair `(F_m(Q),F_{m-1}(Q))` contributes a single `Z` in degree `m`; its lower-degree groups vanish. Since both `Delta Q` and `F_0(Q)` are contractible, the abutment is zero. Hence the sole possible `d_{m-1}:Z -> Z` is again an isomorphism.

As finite checks, `r=4` gives the capped absolute `12`-vertex family with `d_4=±1`; its uncapped variant has `11` vertices. The relative example from `r=3` has `13` vertices, `m=5` marks, and a `d_4=±1` from homological degree `5` to degree `4`; its persistent sphere occurs in **degree 4**, not degree 3.

## 8. Questions and limitations for the referee

The general theorem concerns this recursively defined family, **not** arbitrary clean Boolean insertion cubes. Statements about simplicity of intermediate stages are only homotopy-equivalence statements for `A_{r,p}` and `F_p(Q)`, while the `B`-filtration and cap removal have explicit elementary collapses. No minimality, classification, or novelty claim is made.

Please check in particular whether the apparently natural homotopy-pushout equivalences in Sections 5–6 really establish homotopy equivalences of the **actual inclusions**, as asserted, and whether any finite seed collapse pair fails to be free at its stated time. The optional verifier is independent executable evidence for the finite step, not for the general induction.
