# A — Equality characterizations for the localic separation hierarchy

**Working research note — 18 October 2026.** Proofs given here are intended for mathematical scrutiny, not a claim of priority. The first two papers to compare with are Picado–Pultr, *Separation in Point-Free Topology* (2021), especially VI.1.5.2, VI.2.2 and V.2.4, and Arrieta–Picado–Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property* (2022), especially the Dowker–Strauss approach to parallel frame maps. Our notation **F(X)** means the functional-equivalence **relation**, not their distinct property **(Fsep)** of a fitted diagonal.

Start with [A-hierarchy-first-results.md](A-hierarchy-first-results.md), where the three closed relations and proofs of Δ⊆I⊆U⊆F are recorded.

## 1. A frame-only generating formula for the functional relation

For L=O(X) and Q=L⊗L, define the three opens

    d_I = ⋁_{a∧b=0} a⊠b,
    d_U = ⋁_{a*∨b*=1} a⊠b,
    d_F = ⋁_{f:X→R} (f×f)^*((R×R)\Δ_R).

The relations are I=C(d_I), U=C(d_U), F=C(d_F).

Write a≺b iff a*∨b=1 (“rather below”), and a≺≺b for the standard **completely below** relation witnessed by a rational scale. See Picado–Pultr VI.1.1–1.5.2, pp. 108–111. Their Proposition VI.1.5.2 states:

    u≺≺v  ⇔  there exists h:O(R)→L such that
                   h(R\{0})≤u* and h(R\{1})≤v.

**Proposition 1 (proved, working).**
    
    d_F = ⋁_{a≺≺ b*} a⊠b.

In particular, the apparently external quantification over all real-valued localic maps is reducible to an **intrinsic relation on elements of the frame**.

**Proof.** Suppose a≺≺b*. By VI.1.5.2 find h with h(R\{0})≤a* and h(R\{1})≤b*. Since

    R = (R\{0}) ∪ (-∞,1/3),     R = (R\{1}) ∪ (2/3,∞),

we have a≤h((-∞,1/3)) and b≤h((2/3,∞)). The rectangle formed by these last two opens is in d_F, so a⊠b≤d_F.

Conversely, for any f and rational r<s, set c=f^*((-∞,r)) and d=f^*((s,∞)). Choose a continuous cutoff θ:R→[0,1] which is 0 on (-∞,r] and 1 on [s,∞). The map θ∘f gives a homomorphism h= (θ∘f)^* with h(R\{0})≤c* and h(R\{1})≤d*. VI.1.5.2 yields c≺≺d*. Since such opposite rectangles generate d_F and both orientations are accounted for, d_F≤⋁_{a≺≺b*}a⊠b. □

**Corollary.** a≺≺b* is symmetric in a,b. Equivalently, a and b are *completely separated* by a localic real-valued function taking value 0 on the open sublocale a and 1 on the open sublocale b. Note that this refers to the *open sublocales*, not just points.

## 2. Exact tensor-ideal criteria

Put

    Z = {(a,b): a∧b=0},
    R = {(a,b): a*∨b*=1},
    C = {(a,b): a≺≺b*}.

Then C⊆R⊆Z, and

    d_F = ⋁_{(a,b)∈C}a⊠b, d_U = ⋁_{(a,b)∈R}a⊠b,
    d_I = ⋁_{(a,b)∈Z}a⊠b.

For any set of pairs S⊆L×L put its **rectangular saturation**

    Sat(S) = {(a,b): a⊠b ≤ ⋁_{(u,v)∈S}u⊠v}.

This is intrinsic to the frame coproduct; it is *not* a claim about points of X.

**Proposition 2 (proved, working).**

    I(X)=U(X) iff Sat(R)=Z,
    U(X)=F(X) iff Sat(C)=Sat(R).

The first formula uses Sat(Z)=Z: if a⊠b≤d_I, applying the diagonal inverse-image map gives a∧b=0. Both equivalences are immediate from the three displayed join formulas.

These tests are exact, but not yet satisfactory stand-alone *structural* classifications. Their advantage is that they isolate the problem as a precise rectangular-covering property of frame coproducts.

### Sufficient 'grid refinement' criteria (not asserted necessary)

If each a∧b=0 admits join decompositions a=⋁_i a_i and b=⋁_j b_j such that a_i*∨b_j*=1 for all i,j, then I=U.

If each a*∨b*=1 admits such join decompositions a=⋁_i a_i, b=⋁_j b_j with a_i≺≺b_j*, then U=F.

The argument is simply distribution of ⊠ over joins in each variable. It is unknown here whether either sufficient condition is equivalent to the corresponding equality for arbitrary frames.

## 3. A categorical characterization without coproduct notation

Let h,k:L→M be frame homomorphisms, with M an **arbitrary** frame (including the trivial frame if desired). Use the predicates

    Disj(h,k):   for all a∧b=0, h(a)∧k(b)=0,
    Far(h,k):    for all a*∨b*=1, h(a)∧k(b)=0,
    Real(h,k):   h∘f^*=k∘f^* for every f:X→R.

**Theorem 3 (proved, working).**

(a) I(X)=U(X) if and only if for every frame M and h,k:L→M,

    Far(h,k) ⇒ Disj(h,k).

(b) U(X)=F(X) if and only if for every frame M and h,k:L→M,

    Real(h,k) ⇒ Far(h,k).

**Proof (a).** The pair (h,k) corresponds to a unique homomorphism [h,k]:L⊗L→M sending a⊠b to h(a)∧k(b). Thus Far is [h,k](d_U)=0 and Disj is [h,k](d_I)=0. If d_I=d_U the implication follows.

Conversely choose M=O(U(X)), and let q_U:L⊗L→M be the quotient onto the closed sublocale U(X), i.e. q_U(z)=z∨d_U (with M the upper interval ↑d_U, bottom element d_U). Put h=q_U∘ι_1 and k=q_U∘ι_2. Far(h,k) holds, so Disj(h,k) yields q_U(d_I)=0_M, equivalently d_I≤d_U. The other inequality always holds. □

**Proof (b).** If Real(h,k) holds, [h,k] annihilates d_F, because each pair of disjoint real-line intervals has zero intersection after substituting the common map h∘f^*=k∘f^*. If d_U=d_F, Far follows.

Conversely take M=O(F(X)) with its closed-sublocale quotient q_F:L⊗L→M, and h=q_F∘ι_1, k=q_F∘ι_2. By definition F is a kernel pair of every f, so Real(h,k) holds. By hypothesis Far(h,k) follows and q_F(d_U)=0_M. Thus d_U≤d_F and equality follows. □

**Literature warning:** This homomorphism-pair form resembles the Dowker–Strauss criteria for strong Hausdorff and fitted diagonals in Picado–Pultr and Arrieta–Picado–Pultr. Whether the above particular implications are known needs checking; at present this is a direct reformulation of the equality of our specific relations, not evidence of novelty.

## 4. F is the kernel pair of the completely regular reflection

Let C(L)⊆L denote the **subframe generated by all images of frame homomorphisms O(R)→L**. This is a frame-subobject: arbitrary joins and finite meets are computed as in L.

Picado–Pultr VI.2.2, p. 112, shows C(L) is completely regular (because it is generated by such images), and every completely regular subframe of L is contained in C(L). Let

    j:C(L)→L

be the inclusion, corresponding to the localic map

    r_X:X→X_cr := Loc(C(L)).

**Proposition 4 (proved, working).** r_X is the universal map from X to a completely regular locale. Moreover,

    F(X) = X×_{X_cr} X = kerpair(r_X).

**Proof.** If g:X→T with T completely regular, O(T) is generated by images of its own maps O(R)→O(T) (Picado–Pultr VI.2.2). Composing with g^* lands in C(L), so g factors uniquely through j:C(L)→L in Frm, or through r_X in Loc. This proves the adjoint universal property.

Let S be the set of all maps f:X→R and let e:X→R^S be the product evaluation. By definition of C(L), the image of the inverse-image frame homomorphism e^*:O(R^S)→L is exactly C(L). Hence e factors as X --r_X--> X_cr --i--> R^S, where i corresponds to the **surjective** frame homomorphism e^*:O(R^S)→C(L). Such an i is a sublocale embedding, in particular a monomorphism. Therefore the kernel pairs of e and r_X coincide. The kernel pair of e is the intersection of kernel pairs of all its components f, which is F(X). □

**Corollary 5 (proved, working).**

    F(X)=Δ_X  ⇔  r_X is monic in Loc
              ⇔  j:C(L)→L is an epimorphism in Frm.

**Important:** a frame epimorphism is not necessarily surjective. Therefore F=Δ need **not** imply L is completely regular. Note also that F=Δ forces I=U=Δ by the general hierarchy, so all three diagonal-collapse conditions agree with F=Δ only if one also assumes F=Δ; the conditions I=Δ, U=Δ by themselves are weaker.

### Concrete nonregular example with all three relations equal to Δ

Picado–Pultr V.2.4.1–2.4.4, pp. 91–92, give a strongly Hausdorff but nonregular topology T_OF on [0,1], together with a **frame epimorphism**

    e:O([0,1],usual) → O([0,1],T_OF)

given by the inclusion of the usual opens. The usual opens form a completely regular subframe, so they lie in C(L) for L=O([0,1],T_OF). Since e factors through C(L)→L and e is epi, the inclusion C(L)→L is epi. Thus F=Δ. Since this topology is also strongly Hausdorff by their construction, I=Δ. Consequently

    Δ=I=U=F

**even though L is not regular, hence not completely regular**. This rules out an equivalence between diagonal collapse and complete regularity.

Source: Picado–Pultr, V.2.4.1, V.2.4.2, V.2.4.4, pp. 91–92. The example is their construction, while the deduction about F is ours.

## 5. Other sufficient conditions and non-necessity examples

### Extremal disconnectedness yields complete relation collapse

**Proposition 6 (proved, working).** If L is extremally disconnected, in the frame-theoretic form a*∨a**=1 for every a∈L, then

    I(X)=U(X)=F(X).

**Proof.** If a∧b=0 then a≤b*, so a**≤b* and a*∨b*=1. Thus d_I≤d_U and hence d_I=d_U. Moreover b* is **complemented** with complement b** in an extremally disconnected frame. The clopen partition (b*,b**) defines a continuous characteristic function to the discrete two-point sublocale {0,1}⊆R; since a≤b* and b≤b**, it separates a from b. Therefore a⊠b≤d_F whenever a∧b=0. This gives d_I=d_U=d_F. □

This does *not* assert that the common relation is Δ: a finite chain, such as the Sierpiński locale, is extremally disconnected and has I=U=F=X×X.

### Neither main equality implies regularity or normality

Take the three-point **particular-point** topology on {p,x,y}:

    O(X)={∅,{p},{p,x},{p,y},X}.

Every two nonempty opens intersect at p. Thus d_I=d_U=0. Every localic real-valued map is constant (as seen from the finite poset p<x, p<y; comparable points must have equal real values). Hence d_F=0. So

    I=U=F=X×X.

However the frame is **not normal**: the two disjoint closed sets {x} and {y} have no disjoint open neighborhoods. Nor is it regular (it is a nondiscrete finite T0 locale). This gives a small example ruling out converses to the regularity and normality sufficient conditions in the previous note.

### Finite Alexandrov-space classification

For a finite T0 Alexandrov locale, let G be its diagonal-inclusive *inseparability graph* (xGy iff smallest neighborhoods meet). Directly from the upper-set poset description,

    U=G^2   (paths of length ≤2),
    F=the equivalence relation generated by G
      (same connected component).

Consequently:

    I=U iff every component of G is a clique;
    U=F iff every component of G has diameter ≤2.

The first criterion implies the second, so **I=U forces I=U=F in finite Alexandrov locales**, though it need not for general locales (the regular non-functionally-Hausdorff examples from the previous note yield I=U≠F). This is a comparison of the frame-theoretic relations via finite spatial locales, not an arbitrary-localic composition theorem.

Proof of U=G²: If cl(↑x)∩cl(↑y) contains t, choose common uppers u≥x,t and v≥y,t. Then x G t G y. Conversely such a two-edge path gives t∈cl(↑x)∩cl(↑y). F follows because continuous maps into Hausdorff R are constant along comparable pairs, hence each connected component, while distinct components may be assigned distinct real values.

## 6. Next open problems

1. Seek a **recognizable, purely internal frame axiom** equivalent to I=U, stronger in interpretive value than Sat(R)=Z or the h,k test.
2. Likewise, seek a structural characterization of U=F using the completely-below relation, beyond Sat(C)=Sat(R).
3. Determine whether reasonable hypotheses (e.g. subfitness, sobriety, coherent/compact generation) turn the sufficient grid-refinement conditions in §2 into equivalences.
4. Study **relative** reflection/kernel-pair conditions giving U=F, and categorize their stability under locale constructions.
5. Compare systematic known work on functional separation, zero/cozero sublocales, nearness, frame F-spaces and separation axioms before claiming priority.
6. Investigate products and localic relation composition only after the above equalities are better understood.

## References

- J. Picado and A. Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021; III.5–6, V.2.4, VI.1.5.2 and VI.2.2, VIII.4.4.
- I. Arrieta, J. Picado, A. Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, *Applied Categorical Structures* **30** (2022), 247–263, [author preprint](https://www.mat.uc.pt/preprints/ps/p2117.pdf).
- P. J. Cameron and V. Kumar, *Graphs on topological spaces*, arXiv:2610.14783 (2026).
- J. Gutiérrez García, J. Picado and A. Pultr, point-free completely separated sublocales and the completely-below relation; [Coimbra preprint 1427](https://www.mat.uc.pt/preprints/ps/p1427.pdf), §5.4 (bibliographic details to verify).
