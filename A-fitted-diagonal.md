# A — Fitting the diagonal: a fourth separation relation

**19 October 2026. Status: short working note; equalities deferred.** Motivated by I. Arrieta, J. Picado, A. Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, *Applied Categorical Structures* **30** (2022), 247–263, and their notion (Fsep) of a **fitted diagonal**. Picado–Pultr, *Separation in Point-Free Topology* (2021), X.4 explicitly calls fitting "Another Closure". This note records comparisons with the three relations I, U, F; it does **not** assert novelty over the literature.

## 1. Definition

For a locale X let δ:X→X×X be its diagonal and Δ_X its image sublocale. Let O(w) denote the open sublocale corresponding to an element w∈O(X×X). Define

    D(X) = fit(Δ_X)
         = ⋂ { O(w) : Δ_X ⊆ O(w) }.

Thus D is a **fitted sublocale**, not necessarily a *closed* sublocale. In the terminology of Arrieta–Picado–Pultr, (Fsep) means exactly D(X)=Δ_X.

Our previous three relations are *closed* sublocales with complements

    d_I = ⋁_{a∧b=0} a⊠b,
    d_U = ⋁_{a*∨b*=1} a⊠b,
    d_F = ⋁_{a≺≺b*} a⊠b.

Their hierarchy is Δ⊆I⊆U⊆F.

## 2. Universal comparison: D⊆U

**Proposition (working point-free proof).** For every locale X,

    Δ_X ⊆ D(X) ⊆ U(X).

**Proof.** Let L=O(X), Q=L⊗L. Given a,b∈L with a*∨b*=1, set r=a⊠b. The standard frame-coproduct identity gives

    r*=(a*⊠1)∨(1⊠b*).

Consequently

    δ*(r*)=a*∨b*=1.

The open sublocale O(r*) therefore contains Δ_X. By the defining intersection, D(X)⊆O(r*). Since r*∧r=0, the open sublocale O(r*) lies in the closed complement C(r) of the open sublocale O(r). Thus

    D(X) ⊆ C(a⊠b)

for each far pair a,b. Taking the intersection over all such pairs yields D(X)⊆U(X). □

Hence the universal inclusion diagram is

                F
                |
                U
               / \
              I   D
               \ /
                Δ

No inclusion between I and D holds in general (proved below).

## 3. Ordinary points: an open-cover characterization

**Proposition (working; no product-spatiality assumption required).** For any ordinary topological space X and points x,y,

    (x,y)∈D(X)   ⇔   every open cover of X has some member containing both x and y.

Here on the left X denotes the locale associated to the topology of the given space, and membership means the point induced by the **specified original pair** (x,y) factors through the fitted sublocale. **If X is not sober, its locale has the points of the sobrification, which may include additional points not originating in X.** The points of the localic product are pairs of *locale points*, not necessarily pairs of original points; no product-spatiality assumption is needed to test original pairs. For a full point-set identification assume X sober.

**Proof.** An open sublocale O(w) of the product contains Δ iff δ*(w)=1. Every w∈L⊗L is a join of basic rectangles,

    w=⋁_i a_i⊠b_i;  δ*(w)=⋁_i (a_i∧b_i).

If δ*(w)=1, the opens c_i=a_i∧b_i cover X. Their **squares** c_i⊠c_i satisfy

    ⋁_i c_i⊠c_i ≤ w.

If every open cover has a member containing x,y, then for some i we have x,y∈c_i; the point (x,y) therefore lies in w. Hence it factors through the intersection of all diagonal-containing open sublocales, namely D.

Conversely for any cover {c_i}, the element w=⋁_i c_i⊠c_i satisfies δ*(w)=1; if no c_i contains both x,y, then (x,y) is not in O(w), hence not in D. □

**Corollary (exact pointwise T1 test).**

    [D relates no distinct **original** points of X] ⇔ [X is T1].

For **sober** X this equivalently says the **entire point set** of D is the diagonal. For a non-sober T1 space, sobrification may introduce additional points and the unrestricted assertion about *all locale points* is false.

Indeed, if X is T1, then for distinct x,y the two-member open cover {X\{x},X\{y}} has no member containing both. If X is not T1, some distinct x,y have x∈cl{y}; therefore **every open neighborhood of x contains y**, and any open cover has a member containing both. So D has a nontrivial off-diagonal point.

**Critical distinction:** The property (Fsep), D(X)=Δ_X *as sublocales*, is stronger than the assertion that D relates no distinct **original points**; the latter is equivalent to T1. For all locale points one must additionally control sobrification (e.g., assume X sober). Do not infer (Fsep) from T1 without a separate spatiality/other argument. In particular D is in general not a closed sublocale.

The pointwise D relation is reflexive and symmetric, and supplies a graph on the points with loops. Its off-diagonal edges detect **failure of T1 exactly**; by §3a it is precisely the closure-meeting graph of Cameron–Kumar. It can also connect specialization-incomparable pairs.

## 3a. Exact identification with Cameron–Kumar's closure-meeting graph

**Theorem (new identification of our construction, NOT new graph).** For any ordinary topological space X and points x,y,

    (x,y)∈D(X)   ⇔   cl_X{x} ∩ cl_X{y} ≠ ∅.

**Proof.** By §3, (x,y)∈D iff every open cover has a member containing x,y. If z lies in the two singleton closures, every open neighborhood of z contains x and y, so every open cover has such a member. Conversely if the two closures are disjoint, then {X\cl{x}, X\cl{y}} is a two-element open cover, and neither member contains both x,y. □

The right-hand side is **exactly the closure-meeting graph Cm(X)** of P. J. Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783 (2026), Definition 3.1. Their Theorem 3.2 gives precisely the graph-theoretic diamond

    Sp ⊆ Ins∩Cm,     Ins∪Cm ⊆ Ury ⊆ Fun,

with Ins and Cm incomparable in general. **Our fitted-diagonal construction recovers their Cm as the points of a distinguished sublocale of the localic product.** This is a better interpretation of the D–I incomparability and D⊆U than merely a new fourth relation. The relation D remains a generally **nonclosed** fitted sublocale, so even when its point set is Cm, its full point-free structure can carry more information. In particular pointwise Cm trivial ⇔ T1, whereas D=Δ as sublocales is the stronger F-separated condition (cf. Arrieta–Picado–Pultr 2022).

The corresponding specialized graph comparison is already in Cameron–Kumar; we should NOT claim priority for it. Any possible new content lies in the **localic realization, not the pointwise graph**.

## 4. Incomparability with I

For a finite T0 Alexandrov space P, regard P as a poset with **upper-set** topology.

- A pair x,y belongs to I(P) iff x,y have a **common upper bound**: the least neighborhoods ↑x,↑y intersect.
- A pair x,y belongs to D(P) iff x,y have a **common lower bound**. If z≤x,y, every open cover has a member containing z, therefore both x,y. Conversely, the cover {↑z:z∈P} shows that a D-related pair must have a common lower bound.

Finite locales and their finite products are spatial. Thus these pointwise calculations detect the localic relations in the present examples.

Example A (D not included in I): the three-element poset {0,a,b} with 0<a, 0<b and incomparable maximal a,b. The points a,b share lower bound 0 so (a,b)∈D, but ↑a={a} and ↑b={b} are disjoint, so (a,b)∉I.

Example B (I not included in D): the order dual {a,b,1} with a<1, b<1 and incomparable minimal a,b. The points a,b have upper bound 1 so (a,b)∈I, but no common lower bound, so (a,b)∉D.

**Conclusion:** neither I⊆D nor D⊆I holds universally. The inclusion picture is genuinely non-linear.

## 5. Scope and deferred questions

This is a **record of structural observations**, not a fourth central research program yet.

Deferred: investigate when D=I, D=U, D=Δ, I=U, and the various combinations; interpret them intrinsically in frames and relative to the literature on (Fsep), fitted diagonals, weak and almost homomorphisms, and Dowker–Strauss relations.

Priority/literature caution: the fitting of the diagonal, (Fsep), and the distinction between pointwise T1 and fitted-diagonal separation belong to established point-free separation theory; no new terminology/priority claim is made. Our use of the symbol **D** is provisional. The short proof D⊆U and the poset incomparability should be checked against the existing literature for earlier formulations before being called original.

## References

- I. Arrieta, J. Picado, A. Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, *Applied Categorical Structures* **30** (2022), 247–263; preprint https://www.mat.uc.pt/preprints/ps/p2117.pdf .
- J. Picado and A. Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021, §X.4, “Fitting, ‘Another Closure’”.
- - P. J. Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783 (2026), Definition 3.1 and Theorem 3.2. https://arxiv.org/pdf/2610.14783 .
- Our [A-localic-separation.md](A-localic-separation.md), [A-hierarchy-first-results.md](A-hierarchy-first-results.md), and [A-consolidated-theorems.md](A-consolidated-theorems.md).
