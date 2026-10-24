# Project A — When does W = U? Diagonal-neighborhood and nucleus criteria

24 October 2026. **Working results:** algebraic calculations newly derived in this segment; not independently audited, no priority claim. Throughout Q=L⊕L and δ*:Q→L is the codiagonal, Δ its image, D=fit(Δ), W=cl(D), U=C(d_U), and B={w∈Q:δ*(w)=1}. Write a⊠b for a rectangle.

## 1. Universal intersection-of-closures theorem

**Theorem (working).** For every frame L,

    d_U = ⋁_{w∈B} w*
    U = ⋂_{w∈B} cl(O(w)).

Proof. Express any w∈B as a join of rectangles a_i⊠b_i. The elements c_i=a_i∧b_i cover 1 and ⋁ c_i⊠c_i≤w. If a⊠b≤w*, then for each i the rectangle (a∧c_i)⊠(b∧c_i)=0, whence a∧c_i=0 or b∧c_i=0. Thus c_i≤a*∨b*, so a*∨b*=1. Since rectangles generate Q, w*≤d_U.

Conversely, for a far rectangle r=a⊠b (a*∨b*=1), the standard rectangle pseudocomplement identity gives δ*(r*)=a*∨b*=1. Hence r*∈B and r≤r**≤⋁_{w∈B}w*. Join over all far r. Finally cl(O(w))=C(w*) and intersection of C(q_i) equals C(⋁q_i).

Thus the problem W=U is exactly the commutation

    cl(⋂_{w∈B}O(w)) = ⋂_{w∈B}cl(O(w)).

This is a highly specialized closure/meet-interchange property at the diagonal-neighborhood filter; do not infer unrestricted closure preservation.

## 2. The diagonal-cover pre-nucleus

Define, for x∈Q,

    Φ(x) = ⋁_{w∈B}(w→x).

Because B is a filter (upward closed under finite meets), Φ is monotone, inflationary and preserves finite meets: for w,v∈B, (w→x)∧(v→y)≤(w∧v)→(x∧y). Hence Φ is a pre-nucleus.

The sublocale D=⋂_{w∈B}O(w) has frame Fix(Φ): x is fixed iff w→x=x for all w∈B. Transfinite inflationary iteration of Φ from any x, taking joins at limits, gives the least fixed element above x, i.e. its nucleus j_D(x). In particular,

    Φ(0)=⋁_{w∈B}w*=d_U,
    j_D(0)=d_W.

Therefore the equality in question is a *single fixed-point test*:

    W=U   ⇔   Φ(d_U)=d_U
          ⇔   ∀w∈B, (w→d_U)=d_U.

This avoids iterating the full nucleus when checking equality: since the first iterate of 0 is exactly d_U, either it is already fixed or the second iterate witnesses strict W<U.

## 3. Relative density and cover descent

Let U=C(d_U), whose open frame is ↑d_U with bottom element d_U. The relative pseudocomplement of d_U∨w in ↑d_U is w→d_U. Therefore

    W=U ⇔ every diagonal neighborhood O(w) restricts to a dense open sublocale of U.

Compare D=U ⇔ each such restriction equals the whole of U, i.e. d_U∨w=1; density is strictly weaker.

For any open cover C⊆L, let w_C=⋁_{c∈C}c⊠c. The family of w_C is cofinal below B. Consequently it suffices to check

    ∀ open covers C of 1,  (w_C→d_U)=d_U.

Equivalently, for every cover C and every a,b∈L:

    [∀c∈C, (a∧c)⊠(b∧c)≤d_U] ⇒ a⊠b≤d_U.

This is a gluing/descent property for rectangles already contained in the Urysohn separation open, rather than just those globally far.

If 1∈L is compact, it suffices to test finite open covers. More generally, any cardinal bound on subcovers restricts tests to that size.

## 4. Relationship with previous results

Coherent frames satisfy W=U, and hence Φ(d_U)=d_U. In locales with FIT localic square, D=Δ and W=I, so W=U iff I=U. The compact T1 three-boundary-point example has W=I<U, while the T1 locally compact sober scattered deleted-plank discrete-cofinite-cloud example has W=I=U<F.

This criterion is not claimed to be recognized in the published literature; possible connections to neighborhood-filter closure and theta-type separation should be checked before naming it.



## 5. Explicit two-element-cover failure in the compact T1 example

Let X be the alpha–beta–gamma space with disjoint infinite clopen discrete sheets N1,N2 from [the upper-diamond note](A-H-upper-diamond-unrestricted-failure-compact-T1-2026-10-24.md). Set a={alpha}∪N1 and b={gamma}∪N2. Its U relation contains (alpha,gamma), so r=a⊠b is NOT ≤d_U.

Take the two-element open cover C={X\{alpha}, X\{gamma}}. Its square-cover w_C omits the point (alpha,gamma). More directly, the two localized rectangles are

    (a∧(X\{alpha}))⊠(b∧(X\{alpha})) = N1⊠b,
    (a∧(X\{gamma}))⊠(b∧(X\{gamma})) = a⊠N2.

Each lies below d_U: for every n∈N1 or N2 the singleton {n} is clopen, and the opposite open b or a avoids n, so each relevant pure subrectangle is far. But a⊠b is NOT ≤d_U, witnessed by (alpha,gamma)∈U. Thus condition (11) fails already for a cover of cardinality two, which explicitly witnesses Φ(d_U)>d_U and W<U without any transfinite computation.

This distinguishes a finite-cover (indeed binary-cover) failure from possible infinitary failures. It does NOT establish that testing only binary covers suffices in general.

## 6. Literature terminology caution

The identity U=⋂ cl(O(w)) resembles neighborhood-filter closure constructions. Do not identify it without proof with standard theta-closure: the usual theta-closure of a subset A tests closures of *neighborhoods of the testing point*, whereas this identity takes closures of *neighborhoods of the diagonal as a whole*. The distinction can matter in nonregular spaces.

## 7. Next work

Can cover descent be recognized intrinsically in L without explicitly computing d_U in Q? Test behavior under frame constructions and search for a standard separation axiom or categorical class whose defining condition is Φ(d_U)=d_U. Distinguish finite-cover failures (compact noncoherent example) from infinitary failures.
