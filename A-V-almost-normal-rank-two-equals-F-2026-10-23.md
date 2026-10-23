# Project A: almost-normality identifies the rank-two fitted hull with F
23 October 2026. **Working theorem; independent audit requested before treating as final.**

## Conventions

Let L be a frame, Q=L⊕L, and write a⊠b for a rectangle. The rather-below relation is a≺b iff a*∨b=1; a≺≺b means rationally interpolated completely-below. Let

- d_I = ⋁{a⊠b : a∧b=0};
- d_U = ⋁{a⊠b : a*∨b*=1};
- d_F = ⋁{a⊠b : a≺≺b*};
- d_2 = ⋁{c⊠f : c≺a, f≺b, a∧b=0 for some a,b}.

Write I=C(d_I), U=C(d_U), F=C(d_F), V=fit(I). A bar is an open w∈Q with d_I∨w=1; its canonical rectangle family is B_w={(u,v):u⊠v≤w}. Define j_2 to be the supremum in Nuc(Q) of open nuclei o_v(x)=v→x over all bars v with rectangular separation-tree rank ≤2; V_2 is the corresponding sublocale.

## Theorem (arbitrary frames, almost-normal hypothesis)

If ≺ interpolates on L (equivalently, L is almost normal, with usual dependent choice for rational scales), then

    d_U=d_2=d_F
    and
    V_2=U=F.

In particular F is fitted. This statement makes NO continuity, spatiality, compactness, regularity or T1 assumption. It does *not* claim that V=V_2 or that I=F.

### Proof, part 1: collapse of apartness opens

Interpolation of ≺ implies a≺b iff a≺≺b, by recursively inserting interpolants on the dyadic rationals; monotonicity permits filling a rational interpolation scale. Thus d_U=d_F, since a*∨b*=1 iff a≺b*. The always-valid sandwich d_F≤d_2≤d_U yields d_U=d_2=d_F.

### Proof, part 2: every rank≤2 bar covers the F-remainder

Let v be a bar with an H-then-V tree of depth ≤2. Its first-coordinate root cover has 1=⋁_i a_i. Below each (a_i,1), its vertical leaves lie below either D={(u,b):u∧b=0} or B_v. Set

    h_i = ⋁{b : ∃u≥a_i, u⊠b≤v}.

The leaf cover yields a_i*∨h_i=1, i.e. a_i≺h_i. Interpolate to choose c_i with a_i≺c_i≺h_i. In particular c_i*∨h_i=1. Since ≺=≺≺, a_i≺≺c_i≤c_i**, and hence a_i≺≺(c_i*)*. Therefore a_i⊠c_i*≤d_F. Also a_i⊠h_i≤v by separate join preservation in Q. Hence

    a_i⊠1 = (a_i⊠c_i*)∨(a_i⊠h_i) ≤ d_F∨v.

Joining the root cover gives 1=d_F∨v. The V-then-H case is symmetric; rank≤1 cases may be padded. Therefore every rank≤2 bar v satisfies v∨d_F=1.

In nucleus order this means o_v≤j_{C(d_F)}, since if v∨d_F=1 then
v→x = (v→x)∧(v∨d_F) ≤ x∨d_F.
Taking the join over rank-two v yields j_2≤j_{C(d_F)}.

### Proof, part 3: converse nucleus inequality from rank-two strips

For c≺a, f≺b, a∧b=0, the strip

    v_cf=(c*⊠1)∨(1⊠f*)

is a bar with explicit H→V depth≤2 tree: root first opens c*,a cover 1; under (a,1), second opens f*,b cover 1, and the (a,b) leaf is D. Since v_cf∧(c⊠f)=0, the open nucleus o_vcf(0)=v_cf* contains c⊠f. Thus j_2(0)≥d_2=d_F. By monotonicity and inflationarity j_2(x)≥x∨d_F=j_{C(d_F)}(x). Combining with the previous inequality proves j_2=j_{C(d_F)}. Hence V_2=F=U.

## What remains open

**Question:** Does interpolating ≺ imply V=V_2=F? Equivalently, for every bar w does d_F∨w=1 hold? The equivalence uses this theorem and the bar-neighborhood formula for fit(I).

A negative example needs a proper bar w with w∨d_F<1; the stronger fixed-point witness can be taken from C(w), and rank-two nuclei already have the exact form x↦x∨d_F. On a continuous frame all bars have depth ≤3 by the prior H-V-H normalization theorem, so any negative continuous-frame example has V_2 ⊋ V_3=V.

For **spatial T1** almost-normal X with *spatial localic square*, all disjoint open-neighborhood pairs of points can be separated by completely-below neighborhoods; then d_I=d_F and V=V_2=I=F. The non-T1 continuous Scott-space case requires separate analysis. Do NOT infer localic equality from pointwise equality on a nonspatial square.

## Audit checklist

1. Exact use of a_i*∨h_i=1 from H-V leaves, including downward closure of canonical leaves.
2. The inference a_i≺c_i⇒a_i≺≺c_i** via interpolation and rational scales.
3. o_v≤j_C(d_F) from v∨d_F=1, and order reversal for sublocales.
4. Proof that the rank-two strips v_cf are bars and annihilate c⊠f; empty/zero cases.
5. The equivalence between almost-normal frame and interpolation; set-theoretic choice needed for dyadic scales.
6. Do not confuse this theorem with the distinct relation D=fit(Delta).

## Relationship to existing notes

Builds on A-V-two-step-apartness-I-U-F-hierarchy-2026-10-23.md and A-V-rather-below-separated-apartness-rank-two-2026-10-23.md. This improves the former note's weaker statement d_2=d_F under interpolation to the full equality d_U=d_2=d_F, and adds the genuinely new nucleus equality V_2=F. Neither the general Question A V_fin=V nor the new almost-normal Question V=F is resolved here.
