# A — Continuous frames and way-below criteria

**Research note, 18 October 2026.** Working proofs; no claim of novelty. These results extend the coherent/algebraic criteria in [A-coherent-conormality.md](A-coherent-conormality.md). Here **continuous frame** means continuous as a complete lattice, i.e., each a is the join of the elements u **way below** it. All the spatial arguments invoke ordinary classical mathematics, including the Hofmann–Lawson representation theorem; they are **not** proofs valid in choice-free locale theory.

## 0. Important scope correction: continuous frames are spatial in classical mathematics

The Hofmann–Lawson theorem identifies continuous frames with frames of opens of locally compact sober spaces. In particular, **there are no nontrivial pointless continuous frames over ZFC**. The previous idea that continuous frames might naturally provide genuinely nonspatial examples is incorrect in ordinary classical mathematics. See:

- K. H. Hofmann and J. D. Lawson, *The spectral theory of distributive continuous lattices*, Trans. Amer. Math. Soc. **246** (1978), 285–310; DOI [10.1090/S0002-9947-1978-0515540-7](https://doi.org/10.1090/S0002-9947-1978-0515540-7).
- J. Goubault-Larrecq, [*Exponentiable locales II: the exponentiable locales are the continuous frames*](https://topology.lmf.cnrs.fr/exponentiable-locales-ii-the-exponentiable-locales-are-the-continuous-frames/) (2023); classical reduction using spatiality and locally compact sobriety, with the constructive/choice-free caveat spelled out.

A localic product of locally compact sober spaces agrees with the ordinary topological product (core-compact/exponentiable space result). The pointwise pairs consequently detect **closed sublocales** of X×X: distinct closed subsets correspond to distinct closed sublocales, and vice versa. We are not making that inference for arbitrary spatial locales without a product comparison.

## 1. Compact-containment lemma for way-below elements

For a frame L, u≪a means: whenever a≤⋁_i a_i for a directed family, there exists i with u≤a_i. Equivalent formulation: for an arbitrary open cover of a, some **finite** subfamily covers u.

In a locally compact sober space X,

    u ≪ a  iff  there exists a compact saturated K⊆X
                         with u⊆K⊆a.

Explanation: for ⇒, choose at each p∈a a small open V_p with p∈V_p⊆K_p⊆a and K_p compact saturated, then extract finitely many V_p covering u; the finite union of K_p works. For ⇐, any open cover of a has a finite subcover of K.

Consequently, if u≪a and v≪b, there exist compact K,H with

    u×v ⊆ K×H ⊆ a×b.

Since finite products of compact spaces are compact (no separation hypotheses), **every open covering of a×b has a finite subfamily covering u×v**. In frame terms:

    u⊠v ≪ a⊠b in O(X×X).

(We only use this relative compactness conclusion, not any stronger assertion that u⊠v is a compact open.)

## 2. Two elementary finite-rectangle lemmas

These lemmas hold in arbitrary ordinary topological spaces X and are used only after translating continuous frames to their locally compact sober spectra.

**Lemma 2.1 (finite farness).** Suppose

    A×B ⊆ ⋃_{i=1}^n (U_i×V_i)

and cl(U_i)∩cl(V_i)=∅ for each i. Then cl(A)∩cl(B)=∅.

**Proof.** Taking closure in X×X and using finite union,

    cl(A)×cl(B) ⊆ ⋃_i [cl(U_i)×cl(V_i)].

Each rectangle on the right misses the diagonal. If cl(A)∩cl(B) contained z, the left would contain (z,z), contradiction. □

**Lemma 2.2 (finite complete separation).** Under the same rectangle coverage, suppose instead that for each i a continuous f_i:X→[0,1] equals 0 on U_i and equals 1 on V_i. Then a single continuous f:X→[0,1] equals 0 on A and 1 on B.

**Proof.** Let F=(f_1,…,f_n):X→[0,1]^n. For every x∈A, y∈B, one coordinate differs by 1, so ||F(x)-F(y)||≥1. Hence the closures C=cl(F(A)) and D=cl(F(B)) in Euclidean space are separated by distance ≥1. Writing dist(z,C), dist(z,D) for distance functions, set

    g(z)=dist(z,C)/(dist(z,C)+dist(z,D)).

The denominator is bounded below by 1, and g is continuous, 0 on C and 1 on D. The composite g∘F works. (If A or B is empty choose a constant map.) □

Unlike Lemma 2.1, Lemma 2.2 uses the real-valued separator descriptions from Picado–Pultr 2021, VI.1.5.2, to establish the existence of the f_i when u_i≺≺v_i*.

## 3. Exact tests for continuous frames

Let L be a continuous frame, X its locally compact sober spectrum. Recall

    d_I = ⋁_{a∧b=0} a⊠b,
    d_U = ⋁_{a*∨b*=1} a⊠b,
    d_F = ⋁_{a≺≺b*} a⊠b,

and I=C(d_I), U=C(d_U), F=C(d_F).

**Theorem 3.1 (working proof).** For a continuous frame L,

    I(X)=U(X)

if and only if for every a,b∈L with a∧b=0 and every u≪a, v≪b,

    u*∨v*=1.

**Proof, ⇒.** By equality, a⊠b≤d_U. Since u⊠v≪a⊠b, some finite collection of the generating far rectangles covers u⊠v. Lemma 2.1 gives u*∨v*=1.

**Proof, ⇐.** Fix a∧b=0. Continuity supplies a=⋁_{u≪a}u and b=⋁_{v≪b}v. The assumed condition gives u⊠v≤d_U for every pair, hence a⊠b≤d_U. Thus d_I≤d_U and equality follows. □

**Theorem 3.2 (working proof).** For a continuous frame L,

    U(X)=F(X)

if and only if for every a,b∈L with a*∨b*=1 and every u≪a, v≪b,

    u≺≺v*.

**Proof, ⇒.** The far a,b generate a⊠b≤d_U=d_F. Relative compactness of u⊠v gives a finite covering by generators of d_F, corresponding to pairs of opens completely separated by real-valued functions. Lemma 2.2 combines these into a single real-valued separator for u and v. By Picado–Pultr VI.1.5.2, u≺≺v*.

**Proof, ⇐.** As above, write a,b as joins of way-below elements and use complete separation of each pair u,v; then a⊠b≤d_F and d_U≤d_F. □

### A one-line statement of the results

For continuous frames, the arbitrary frame-coproduct saturations may be replaced by **local pairwise tests**:

    I=U  ⇔  disjoint opens have way-below subopens with disjoint closures;
    U=F  ⇔  far opens have way-below subopens completely separable by real functions.

Here “have way-below subopens” means **every** way-below pair, not merely the existence of one pair.

This is a genuine extension of the coherent compact-element criterion. In a coherent frame, every u≪a lies below some compact k≤a, and compact k≤a satisfies k≪a. Thus the tests reduce to the previous compact-open tests.

## 4. Compact continuous frames: extension of the coherent implication

**Corollary 4.1 (working proof).** If L is both compact and continuous, then

    I=U  ⇒  I=U=F.

Indeed, by Hofmann–Lawson L=O(X) for a **compact**, locally compact sober X. The abstract compact-space argument in [A-coherent-implication.md](A-coherent-implication.md) applies to the ordinary point relations: I=U makes inseparability a closed equivalence relation, whose quotient is compact Hausdorff; therefore real functions separate the inequivalent classes. For locally compact sober X, O(X×X)=L⊗L, and these point-relation equalities imply equality of closed sublocales.

This extends the coherent result to noncoherent compact continuous frames. For example, O([0,1]) is compact and continuous but **not algebraic**: its only compact elements are ∅ and [0,1] (a nonempty proper compact open of connected compact Hausdorff [0,1] would be clopen). Thus this is a genuine extension of the *scope* of the implication, although the particular space [0,1] already has all three relations diagonal.

We do **not** deduce the implication for compact nonspatial locales: those need not have continuous frames and the compact-space proof uses ordinary points.

## 5. A continuous, nonalgebraic strictness example

Let P be the seven-element finite upper-set Alexandrov space from [A-hierarchy-first-results.md](A-hierarchy-first-results.md):

    a1 < b1 > a2 < b2 > a3 < b3 > a4.

Set X=P×R (ordinary Euclidean R). It is a **locally compact sober** space, so L=O(X) is continuous. Its frame is **not algebraic**, indeed it has **no nonzero compact open elements**: the projection of any nonempty compact open subset of P×R to R would be a nonempty compact open subset of R, which is impossible (projection is open because P is a topological space).

For the pairs x=((a1,0),(a3,0)) and y=((a1,0),(a4,0)), the same arguments as for the finite space show

    x ∈ U\I,     y ∈ F\U.

The frame/product agreement guarantees

    I(X) ⊊ U(X) ⊊ F(X).

Thus the continuous way-below tests are informative on frames where the compact-element tests are vacuous.

## 6. Next questions

1. Does I=U imply U=F for **all** continuous frames, not necessarily compact? The compact quotient proof no longer directly applies. No assertion made.
2. Are Theorems 3.1–3.2 expressible as familiar separation principles from classical *core-compact* topology? Compare with neighborhood refinements and completely separated compact-saturated sets.
3. Can these results be proved **internally** without the classical spatial representation, to recover a constructive locale theorem? The finite rectangular separation and gluing lemmas need localic analogues.
4. Seek a nontrivial characterization of these equalities valid for *noncontinuous and nonspatial* frames, which is still necessary if “point-free” is to add more than a reformulation of locally compact sober point-set topology.
5. Consider **stably continuous** frames and stably locally compact locales: does multiplicativity of the way-below relation add stronger implications?
6. After these checks, compare with appropriate compactifications/quotient objects rather than relying solely on local tests.

## References

- K. H. Hofmann and J. D. Lawson, *The spectral theory of distributive continuous lattices*, Trans. Amer. Math. Soc. **246** (1978), 285–310, DOI 10.1090/S0002-9947-1978-0515540-7.
- J. Picado and A. Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021, VI.1.5.2 and VI.2.2.
- P. Collins, *Computable analysis with applications to dynamic systems*, Math. Structures Comput. Sci. **30** (2020), 191–233, Theorem 4.26 (locally compact sober spaces, way-below and compact neighborhoods); check bibliographic details against publisher.
- P. Taylor, *Computably Based Locally Compact Spaces*, Logical Methods in Computer Science **2**(1:1), 2006, [open access](https://lmcs.episciences.org/2255).
