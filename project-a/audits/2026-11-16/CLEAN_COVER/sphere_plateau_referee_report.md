# Independent blind referee report

**Project A — Sphere plateaux and unit differentials in clean cover-insertion filtrations**  
**Date:** 16 November 2026  
**Materials examined:** `BLIND_REFEREE_PROMPT.md`, `BLIND_MATHEMATICAL_PACKET.md`, and `verify_seed_collapses.py` from the supplied archive. No earlier referee reports or project discussion were consulted in preparing this audit.

## Overall verdict

**I find the two theorems and the integral spectral-sequence corollary correct as stated, subject only to minor presentational clarifications.** In particular, the proposed proof establishes homotopy equivalences of the *actual successive inclusions*, not just agreement of the homotopy types of their source and target. The cap-removal and deletion collapses have the requisite free-face and filtration compatibility. The long differential is an **integral unit**, with no appeal to the unwarranted inference that nonvanishing modulo two implies a unit over the integers.

No false assertion or unfilled mathematical gap was identified. The most useful new observation from this audit is a **stronger collapse theorem**: every individual preterminal sphere-stage in both constructions actually *simplicially collapses onto a standard crosspolytope boundary*. This does **not** say that the inclusions between successive stages are elementary collapses. A short lemma establishing the strengthening appears in §9.

## 1. Foundation and seed

**Status: established.**

1. Removing marked cover inequalities from a partial order preserves transitivity. If `x<y<z`, then `x<z` is not a cover and therefore cannot be among the deleted comparisons. The filtration by the number of marked covers with both endpoints in a chain is indeed simplicial, and its zeroth stage is `Delta(Q\E)`.
2. All three seed marks `a<d`, `d<f`, `f<i` are genuine covers. They form a chain from minimal `a` to maximal `i`.
3. The proposed seed contractibility argument is valid. In `M={a,b,c,d,e,f,x}`, the lower link of `e` is the four-vertex tree `x—a—d—b`; removing `e` preserves homotopy type, and `M-e` has greatest element `f`. The two maximal vertices `h,i` are incomparable and above all of `M`, so `Delta X_3=Delta M*S^0` is contractible.
4. The supplied verifier successfully checks, in their printed order, **all** elementary-collapse pairs in the four seed-filtration certificates and the twelve further pairs leading to the octahedron. In particular, it checks the stronger requirement that the indicated facet has exactly one remaining strict coface, not merely that the two simplices differ by one vertex. I also inspected the algorithm and its representation of the Hasse order, weight and simplex sets; I found no encoding error.
5. All reported seed counts agree: `|A_{3,p}|=(76,96,100)` and `|B_{3,p}|=(50,60,62)` for `p=0,1,2`, and the f-vector of `B_{3,0}` is `(8,20,18,4)`. After the twelve further collapses, the remaining facets form `S^0_{b,x}*S^0_{c,e}*S^0_{h,i}`, the octahedral `S^2`.
6. The link of `a` in `A_{3,0}` is conical with apex `x` (every possible vertex above `a` at weight zero is above `x`). Thus deleting `a` is an elementary simplicial collapse sequence, not only a homotopy equivalence.

The verification program is correctly limited in scope: it proves none of the general inductive steps. In particular it does not itself certify the cap collapse, filtration naturality or integral spectral-sequence assertion.

## 2. Recursive order and filtered cap collapse

**Status: established.**

The added `u,v,y` comparisons are consistent and transitive. The only potential obstruction to `y` being incomparable with `b` would be a chain from `y` through an old vertex to `b`; minimality of `b` excludes it. The new mark `u<b` is a cover because `v` is incomparable with `u` and `y` is incomparable with `b`. No old marked cover acquires an intervening new vertex.

The filtered cap matching is legitimate. Each simplex containing `y` has exactly one of the forms `y*sigma` and `u*y*sigma`, with `sigma` a chain in `X-b`. The two simplices have exactly the same marked weight: the only new mark is `u<b`, and `b` cannot occur in either. Process `sigma` in decreasing dimension and remove `(u*y*sigma, y*sigma)`. At the moment a pair is removed, the second member has no remaining coface other than the first. In particular, no coface involving `v` or `b` is possible. The empty `sigma` gives the final pair `(uy,y)`.

The matching restricts to each filtration level. Hence the natural inclusions `F_p(U) -> F_p(X_{r+1})` are homotopy equivalences for all `p`, and the resulting squares with the filtration inclusions commute **strictly as inclusions**. No unproved naturality of chosen collapse retractions is needed.

The full order complex is contractible because `U=S^0\oplus X` has contractible order complex and the link of `y` is `u*Delta(X-b)`, a cone.

## 3. Deletion filtration, including the old terminal step

**Status: established.**

Formula (4.1) is exact:

`B_{r+1,p}=(v*A_{r,p}) ∪ (y*B_{r,p})`, with intersection `B_{r,p}`.

Here `u` has been deleted, so the new mark is absent; `y` is incomparable with the old initial vertex `b` and with `v`. All simplices are accounted for, with the inherited old weights.

To lift a collapse `(beta,alpha)` of `B_{r,p}` onto `B_{r,p-1}`, take `(y*beta,y*alpha)`. Cofaces containing `y` cannot involve `v` or `b`, so the lifted face is free exactly when the old face is free. The base copies of `alpha` are left untouched. The lifted pairs leave `(v*A_{r,p}) ∪ (y*B_{r,p-1})`.

For the second matching, take all old simplices `sigma` of weight **exactly** `p` and remove `(v*sigma,sigma)` in decreasing dimension. Such a `sigma` has no `y`-coface in `y*B_{r,p-1}`, because that complex has weight at most `p-1`. Any other coface is associated with an old weight-`p` coface and has already been removed. This proves the actual collapse `B_{r+1,p} searrow B_{r+1,p-1}`.

**The delicate case `p=r` works.** Removing the initial vertex of `X_r` removes its unique incident marked edge. Consequently `B_{r,r}=B_{r,r-1}`, so the lifted `y`-matching is empty, but the `v`-matching still eliminates the old weight-`r` simplices from `A_{r,r}`. The purported top step is not being assumed from the induction hypothesis.

At level zero the two cones have common base `B_{r,0}`; because the inclusions of simplicial subcomplexes are cofibrations, their ordinary union models the homotopy pushout. Hence `B_{r+1,0} ≃ Sigma B_{r,0}`. Finally, the link of `u` in `A_{r+1,0}` is `y*B_{r,0}`, a cone, giving `A_{r+1,0} searrow B_{r+1,0}`.

## 4. Absolute preterminal inclusions

**Status: established.**

Formula (5.2) follows by separating `u`-chains from `v`-chains. A chain with `u` and `b` incurs the new mark, while one with `u` but without `b` does not. Accordingly, `D_0=B_{r,0}` and `D_p=A_{r,p-1}∪B_{r,p}` for `p>=1`; the cone intersection is precisely `D_p`.

For `p>=1`, the intersection `A_{r,p-1}∩B_{r,p}` equals `B_{r,p-1}`. Each collapse pair in `B_{r,p} searrow B_{r,p-1}` lies entirely at old weight `p`; therefore no new coface appears upon adjoining `A_{r,p-1}`. Thus the stronger relation `D_p searrow A_{r,p-1}` is valid.

The first transition needs a separate argument, and the packet gives it: `D_0=B_{r,0} -> A_{r,0} -> D_1` is a composite of homotopy equivalences. For `2<=p<=r`, the commuting square with top row `A_{r,p-2} -> A_{r,p-1}` and vertical rows into `D_{p-1}` and `D_p` proves `D_{p-1} -> D_p` is a homotopy equivalence by two-out-of-three.

Now both summands of (5.2) are cones and the intersection is `D_p`. The maps between corresponding cones are homotopy equivalences (indeed, all four cones are contractible); the intersection map is the homotopy equivalence just proved. The homotopy-pushout gluing lemma for cofibrations gives a homotopy equivalence of the **actual** maps `F_{p-1}(U) -> F_p(U)`. The filtrationwise cap inclusions then transfer this to the actual inclusions for `X_{r+1}`. The range is exactly `1<=p<=r`, excluding the new terminal step `p=r+1`.

This is the central argument of the packet. I see no substitution of an abstract sphere-type comparison for the required natural comparison of filtration inclusions.

## 5. Relative construction

**Status: established.**

The new mark `s<u` is a cover and the full marked chain runs from minimal `s` to the old maximal endpoint. Formula (6.2) holds at every `p>=1`, with intersection `D'_p`: the mark is incurred precisely in `s`-chains containing `u`. In particular, `U-u=v*X_r` and `F_p(U-u)=v*A_{r,p}` exactly.

In (6.3), the pairs `(v*sigma,sigma)` for old weight-`p` simplices remove `F_p(U-u)\F_{p-1}(U-u)` without touching `F_{p-1}(U)`. They are free for the same reason as in the deletion induction. The collapse is vacuous where the weight-`p` layer is empty, including the final preterminal relative stage. This yields `D'_p searrow F_{p-1}(U)`.

For `1<=p<=r`, the square comparing `F_{p-1}(U) -> F_p(U)` with `D'_p -> D'_{p+1}` proves the latter is a homotopy equivalence. The two-cone homotopy-pushout argument proves the actual inclusions `F_p(Q) -> F_{p+1}(Q)` are homotopy equivalences.

At zero, the link of `s` is `v*A_{r,0}`, a cone; deletion collapses `F_0(Q)` to the cone `t*F_0(U)`. Thus the zero stage is **collapsible**, not just contractible. The full complex is `S^0*Delta U` and is contractible. The relative sphere dimension `r+1=m-1`, the index range `1<=p<=m-1` and the differential page `m-1` are consistent.

## 6. Integral spectral sequences

**Status: established.**

The absolute reduced `E^1`-page has precisely

- `E^1_{0,r-1}=Z`, from `\widetilde H_{r-1}(A_{r,0};Z)`;
- `E^1_{r,0}=Z`, from `H_r(A_{r,r},A_{r,r-1};Z)`;
- zero everywhere else.

Intermediate relative groups vanish because the successive inclusions are homotopy equivalences, and the final relative group follows from the long exact sequence of a contractible space and its preterminal sphere. With differential bidegree `(-s,s-1)`, the only possible map between surviving terms is `d_r:E^r_{r,0} -> E^r_{0,r-1}`. Since the reduced abutment is zero, this map **must** be an isomorphism of free rank-one abelian groups, hence multiplication by `+1` or `-1`.

For `(Delta Q,F_0(Q))`, the relative `E^1` groups are exactly `E^1_{1,m-2}=Z` and `E^1_{m,0}=Z`; the same argument forces `d_{m-1}` to be a unit. The degree shift is correct: the relative persistence sphere lies in degree `m-1`, while the final attaching group is in degree `m`. The permanent `(0,0)` term occurs only in the *unreduced absolute* sequence and has been properly distinguished.

**Useful simplification:** At the terminal stage of either construction there is exactly **one** simplex of maximal marked weight: the simplex on the full marked path. Every marked edge is a cover, so no extra vertex can be inserted between successive path vertices; the path begins at a minimum and ends at a maximum, so there is no room outside it either. Thus `F_r(X_r)\F_{r-1}(X_r)` is one `r`-simplex and `F_m(Q)\F_{m-1}(Q)` is one `m`-simplex. This makes the rank-one final relative chain group immediate, and the contractibility argument identifies the attaching degree as `±1`. It would be a pleasant short addition to §7.

## 7. Independent finite checks beyond the supplied seed verifier

I independently enumerated chain simplices from the recursively generated posets and computed ordinary and successive-pair homology over `F_2`, using a separate boundary-matrix rank computation. These checks are corroborative, not substitutes for the integral proof.

| Example | Numbers of nonempty simplices at successive filtration levels | Betti and relative-pair result |
|---|---|---|
| Absolute `r=3` | `76,96,100,101` | `S^2` Betti numbers at `p=0,1,2`, contractible at `p=3`; only final pair has `H_3=F_2` |
| Absolute `r=4` | `306,402,426,430,431` | `S^3` Betti numbers at `p=0,1,2,3`, contractible at `p=4`; only final pair has `H_4=F_2` |
| Absolute `r=5` | `1228,1672,1796,1824,1828,1829` | `S^4` Betti numbers at `p=0,...,4`, contractible at `p=5`; only final pair has `H_5=F_2` |
| Relative `m=5` | `563,806,890,912,916,917` | `F_0` contractible; `S^4` Betti numbers at `p=1,...,4`; pairs have `H_4=F_2` only at `p=1`, and `H_5=F_2` only at `p=5` |
| Relative `m=6` | `2251,3336,3744,3856,3882,3886,3887` | `F_0` contractible; `S^5` Betti numbers at `p=1,...,5`; pairs have `H_5=F_2` only at `p=1`, and `H_6=F_2` only at `p=6` |

I also checked directly, at `r=3` and for every relevant preterminal index, the free-face matching in the additional cone-collapse lemma below for both the uncapped absolute and the relative constructions. All matches passed. No numerical discrepancy was found. These computations do not determine integral torsion or integral attaching degree; those conclusions rest on the mathematical proofs already audited.

## 8. Presentation suggestions and minor cautions

None is a correctness objection.

1. **Make the cofibration hypothesis explicit.** The homotopy-pushout gluing lemma in §§4–6 is being applied to *simplicial subcomplex inclusions*. One sentence emphasizing that these are cofibrations would eliminate the most likely first-reading doubt.
2. **Flag the exceptional first transition.** The treatment of `D_0 -> D_1` in §5 is correct and essential. Present it as a deliberate separate base case, since the square for `p>=2` does not cover it.
3. **Spell out the old terminal step.** In §4, mention explicitly that deletion of `b` removes exactly one of the `r` marked covers, so `B_{r,r}=B_{r,r-1}`. This makes the exceptional `p=r` move instantly transparent.
4. **Distinguish a natural inclusion from a chosen collapse map.** The matching in §3 restricts at every filtration level, but the proof of naturality needs only the strictly commuting *inclusion* squares. Phrasing the argument that way avoids implying that arbitrary elementary-collapse retractions themselves commute strictly with filtration maps.
5. **State the simplex convention.** The cone formulas implicitly include the empty base simplex, so the apex alone is a simplex. This is standard, but the final cap pair `(uy,y)` is easier to see if it is said once.
6. **Give the actual homology index in §7.** The displayed rank-one final relative group is in *homological degree `r`* (respectively `m`), while the plateau sphere is one dimension lower. The packet gets this right; a short top-simplex observation can make it more intuitive.
7. **Do not overstate what is a collapse.** The packet is careful to claim homotopy equivalence, not a collapse `A_{r,p} searrow A_{r,p-1}`. Keep this distinction even if the strengthening below is incorporated: it gives individual collapses to sphere models, not filtration-step collapses.
8. **Clarify the optional script's role.** Its checks are well implemented, but the important inductive proof is fully mathematical. The present division of labor is appropriate.

## 9. Additional mathematical result: all sphere stages collapse onto crosspolytope boundaries

This strengthening appears to follow from the very cone decompositions in the packet. It is not needed for the two theorems, but it may be worth incorporating as a proposition or remark.

**Cone-reduction lemma.** Let `D⊆A` be finite simplicial complexes and let `u,v` be distinct new vertices, with no simplex containing both. Then

\[
K=(v*A)\cup(u*D)\quad\searrow\quad(v*D)\cup(u*D)=S^0*D.
\]

**Proof.** For every nonempty simplex `sigma∈A\D`, in decreasing order of dimension, remove the pair `(v*sigma,sigma)`. A coface of `sigma` in `u*D` is impossible: it would imply `sigma∈D`. Every other coface besides `v*sigma` has a strictly larger base simplex in `A\D` and has already been removed. Thus `sigma` is free when paired with `v*sigma`. At the end precisely the two cones on `D` remain. (In the present applications `D` is nonempty, so no empty-face exception arises.) `□`

It is also standard, and follows by lifting each elementary pair into the joins, that `K searrow L` implies `S^0*K searrow S^0*L`.

**Applications.**

1. From (4.1), immediately `B_{r+1,p} searrow S^0*B_{r,p}` for every `p` in range. In particular `B_{r+1,0} searrow S^0*B_{r,0}`. Since `B_{3,0}` collapses onto the octahedral boundary and suspension preserves collapses, **every `B_{r,p}` collapses onto the boundary of the `r`-dimensional crosspolytope**.
2. From (5.2), `F_p(U) searrow S^0*D_p`. For `p>=1`, combine with (5.4) to get `F_p(U) searrow S^0*A_{r,p-1}`. At `p=0`, get `F_0(U) searrow S^0*B_{r,0}`. The filtered cap collapse (3.2), the seed collapses at `p=0,1,2`, and induction therefore show that **every `A_{r,p}` with `0<=p<r` collapses onto an `(r-1)`-sphere realized as the boundary of the `r`-dimensional crosspolytope**.
3. From (6.2), `F_p(Q) searrow S^0*D'_p`; by (6.3), this continues to `S^0*F_{p-1}(U)` for `1<=p<=m-1`. The uncapped sphere stages already collapse onto crosspolytope boundaries, so **every relative preterminal stage `F_p(Q)` likewise collapses onto the boundary of the `m`-dimensional crosspolytope**.

Here “collapses onto” refers to an explicit elementary simplicial-collapse sequence **within the individual stage**. It does not establish elementary collapses from one filtration stage to the preceding stage. The inclusion-equivalence proof from §5 of the packet remains indispensable.

## Final classification

| Classification | Findings |
|---|---|
| **Established** | Seed certificates and numerical data; contractibility; filtered cap collapse; all deletion filtration collapses including the top old step; actual absolute and relative preterminal inclusion equivalences; integral unit differentials and page indices. |
| **Repairable presentation points** | Minor clarifications listed in §8; no change of hypotheses or theorem statements required. |
| **Unproved claims** | None identified among the claims made by the packet. The added crosspolytope-collapse strengthening is supported by the proof in §9 but is a new observation rather than an assertion previously audited in the packet. |
| **False claims** | None identified. |

**Recommendation:** Accept the mathematical conclusions of this audit packet. Incorporate the modest clarifications above and consider adding the cone-reduction lemma as a stronger and rather concrete description of the preterminal plateau complexes.
