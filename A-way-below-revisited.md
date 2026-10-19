> **DECISIVE UPDATE (18 October 2026):** The **unrestricted** continuous-frame implication is **false**. See [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md): adjoining two nonclosed isolated tags to disjoint nonnormally separable closed subsets of a locally compact Hausdorff space (explicitly the deleted Tychonoff plank) gives a locally compact sober space with **I=U⊊F**, even for a far pair of *compact opens*. This supersedes any unresolved-status or conjectural statement below. Positive conclusions under compactness, sigma-compactness/kω, paracompactness, or quotient hypotheses remain valid.

> **Subsequent progress (18 October 2026):** [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md) proves that for every kω-space, a transitive inseparability relation is already functional equivalence, since the quotient is normal Hausdorff. Hence the unrestricted continuous-frame implication is now established for **σ-compact locally compact sober spaces**, without a closed- or open-quotient assumption. This does not settle the general non-σ-compact case. See [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md) for the noncompact closed-buffer lemma and a counterexample to arbitrary one-step interpolation. For C*-algebra spectra, apply only after independently verifying the requisite σ-compactness/local-compactness hypotheses.

# A — Returning to way-below: the missing interpolation step

**18 October 2026 — Status: partial progress, general implication unresolved.** This note follows [A-continuous-frames.md](A-continuous-frames.md), [A-continuous-compactness-question.md](A-continuous-compactness-question.md), and [A-closed-saturation.md](A-closed-saturation.md). It is a research record, not a novelty claim.

## 1. Precise formulation

Let L be a continuous frame, let \(\prec\) denote the rather-below relation, \(x\prec y\iff x^*\vee y=1\), and let \(x\ll y\) denote way-below. Let \(\prec\!\prec\) be Picado–Pultr's *completely below* relation (VI.1.1), equivalently existence of a dyadic interpolation scale in \(\prec\), or a suitable continuous real function (VI.1.5.2).

The results of [A-continuous-frames.md](A-continuous-frames.md) provide the exact criteria:

    I=U  ⇔  [a∧b=0 and u≪a and v≪b] ⇒ u≺v*;

    U=F  ⇔  [a*∨b*=1 and u≪a and v≪b] ⇒ u≺≺v*.

The first condition provides a **single** rather-below relation. The second demands **all stages** of a rational-scale interpolation, potentially infinitely many. The implication I=U⇒U=F is exactly the problem of deriving this interpolation. No such derivation has been found here.

For an arbitrary fixed pair of opens u,v, the relation u≺≺v* can be tested by a dyadic family \(c_t\) (t dyadic in [0,1]) with

    c_0=u,   c_1=v*,   and c_s*∨c_t=1 for s<t.

Picado–Pultr 2021, VI.1.1.1, makes clear that under countable dependent choice \(\prec\!\prec\) is the largest interpolative subrelation of \(\prec\). Therefore a *genuinely new* sufficient approach would be to construct an interpolative subrelation containing the pairs furnished by the first equality. Merely proving one-step farness is not enough.

## 2. Openness heredity of the lower equality

**Proposition 2.1 (proved).** If T is a topological space with I(T)=U(T) as point relations, then I(O)=U(O) for every open subspace O⊆T.

**Proof.** For x,y∈O, their ordinary inseparability in O is equivalent to inseparability in T, because every neighborhood in O is also open in T and any neighborhood in T can be intersected with O. Thus I(O)=I(T)∩(O×O). A pair Urysohn-separated by neighborhoods in T remains Urysohn-separated after restriction to O (closures in O are intersections with the closures in T), so U(O)⊆U(T)∩(O×O). Combined with I(O)⊆U(O), equality I(T)=U(T) forces equality in O. □

For locally compact sober spaces, the analogous statement holds for equality of the **closed localic relations**, using localic product comparison and the fact that restricting the closure of the diagonal to an open subspace yields the closure of the restricted diagonal. This shows the hypothesis is robust under localization.

But it does **not** supply global continuous functions: functions on O need not extend to T. A proof based on a compact neighborhood K and functions on K must justify such an extension, or give a different method of gluing real functions.

## 3. No localized bump-function theorem—even when I=U=F

Use the locally compact sober split-real-line space from [A-closed-saturation.md](A-closed-saturation.md):

    X = R ⊔ {e_n:n≥1},  with p(e_n)=1/n, p(t)=t.

Ordinary R is open. A basic neighborhood of e_n consists of e_n and a punctured interval around 1/n. We proved that I=U=F=ker(p).

Choose n=2, and ordinary real opens

    u=(0.49,0.51),     a=(0.4,0.6),

both viewed as subsets of the ordinary R part (so e_2∉a). Then **u≪a**: the ordinary compact interval K=[0.48,0.52] sits between u and a and remains compact as a subset of X.

**Proposition 3.1 (proved).** There is no continuous f:X→[0,1] with f=1 on u and f=0 on X\a.

**Proof.** Such f would give f(1/2)=1 and f(e_2)=0. But 1/2 and e_2 are inseparable, so every continuous map to Hausdorff [0,1] agrees on them. Contradiction. □

This proves that **relative compactness u≪a, even combined with I=U=F, does not produce the usual compactly supported bump functions**. The obstacle is the need to respect whole inseparability classes, including representatives outside a.

This counterexample does **not** defeat the desired implication: separators of *far pairs* exist globally in X (they factor through p). It only rules out the naive localization proof.

## 4. Double pseudocomplementation does not supply the interpolant

Use the compact T1 sober example from [A-continuous-compactness-question.md](A-continuous-compactness-question.md), §3. Its points are x,y and isolated s_n,t_n (n≥1); a neighborhood basis at x is

    A_N={x}∪{s_n:n≥N},

while a neighborhood basis at y is

    B_{N,M}={y}∪{s_n:n≥N}∪{t_n:n≥M}.

The only nonsingleton E-class is {x,y}; moreover I=U=F by compactness.

Fix N and put u=A_N. This is a **compact open**, so u≪u. We calculate:

- y∈cl(u), since every neighborhood of y meets the tail {s_n:n≥N};
- y∉int(cl(u)), since every neighborhood of y includes isolated t_n not in cl(u).

But in O(X),

    u* = X\cl(u),        u**=int(cl(u)).

Thus y is in neither u* nor u**, and therefore

    u*∨u** ≠1, i.e. u ⊀ u**.

**Proposition 4.1 (proved).** Even in a compact continuous frame with I=U=F, the implication

    u≪a  ⇒  u≺a**

is **false** (choose u=a=A_N). In particular the tempting interpolant c=a** need not solve a proposed bisection argument.

This explains why double-negation/regular-open approximation is too crude; the desired real function can exist even where this local regularization fails.

## 5. What can and cannot be obtained from finite rectangles

The argument that makes the way-below tests possible is robust:

    u≪a, v≪b ⇒ u⊠v≪a⊠b

for locally compact sober X, since u and v can be trapped in compact saturated subsets K⊆a, H⊆b.

Consequently, an inclusion a⊠b≤d_U can be reduced to a **finite** covering of u⊠v by far rectangles. Finitely many far rectangles covering one rectangle yield farness of the smaller pair by taking closures and restricting to the diagonal.

There is an analogous **finite gluing theorem** for complete separation: finitely many *already existing real separators* on rectangles can be combined into one real separator using the map into [0,1]^n and distance functions. See [A-continuous-frames.md](A-continuous-frames.md), §2.

However, **the missing implication is exactly the creation of real separators out of merely far pairs**. Finite gluing does not accomplish that: it takes real separators as input. Any proof of I=U⇒U=F that invokes the finite gluing lemma at this step without first constructing its input functions is circular.


## 5a. A genuine positive localization theorem: open subspaces of compact good spaces

**Proposition (proved).** If T is a compact topological space with I(T)=U(T), and O⊆T is open, then

    I(O)=U(O)=F(O).

**Proof.** The compact theorem gives I(T)=F(T). For x,y∈O, I(O)=I(T)∩(O×O), since open neighborhoods in O are exactly open neighborhoods in T contained in O. Every continuous real function on T restricts to one on O, so F(O)⊆F(T)∩(O×O). Thus

    I(O) ⊆ U(O) ⊆ F(O) ⊆ F(T)∩O² = I(T)∩O² = I(O).

This also proves the corresponding closed-localic relation equality for open sublocales of compact locally compact sober spaces under the usual product comparison. □

**Implication for the research problem.** Any counterexample among locally compact sober spaces **cannot** be an open subspace of a compact space in which I=U. This suggests an alternative strategy: construct a compactification preserving I=U. But **the existence of such a compactification is exactly what remains to prove**, and it must not be taken for granted. A generic one-point compactification of a non-Hausdorff locally compact space need not preserve the required separation property.

## 6. A precise interpolation program (unproved)

Given a*∨b*=1 and u≪a, v≪b, find a dyadic family (c_t) with

    c_0=u,     c_1=v*,     c_s≺c_t for s<t.

A possible strategy would be a **simultaneous bisection lemma**:

> Under I=U, can one assign to every such (a,b;u,v) an intermediate c and appropriately smaller way-below witnesses so that the same hypothesis can be iterated independently on both sides?

A statement merely asserting an intermediate c with u≺c≺v* is **not** yet enough: repeated bisection requires a hypothesis stable under passing to c. The two examples above rule out the two simplest choices of intermediate open based only on compact supports and double pseudocomplements.

One alternative is to work through the quotient X/E. Because E is a closed equivalence relation under I=U, the question becomes whether locally compact sobriety plus the restricted relation forces X/E to be *functionally Hausdorff*. The quotient need not be open or closed (proved in the previous notes), so the argument must avoid assuming either property. A separator may need to be assembled simultaneously over whole E-classes.

## 7. Provisional conclusion

**No general proof or counterexample** has yet been obtained for

    L continuous, I(L)=U(L)  ⇒?  U(L)=F(L).

The way-below formulation gives an exact target but does **not automatically convert far neighborhoods into a completely-below interpolation**. Compactness gives this by a global quotient argument; local compactness only supplies finite local covers, insufficient without a new gluing/interpolation lemma.

Next directions: try a class of *finite-stage bisection lemmas* with hypotheses stable under iteration; or search for a locally compact sober counterexample in which every pair of separated points has far neighborhoods but the quotient by E is not functionally Hausdorff.

**Literature:** Picado–Pultr (2021), VI.1.1, VI.1.5.2, for scales and completely-below; Hofmann–Lawson for continuous frames and locally compact sober spectra. Classical non-functionally Hausdorff Urysohn spaces exist, but their non-local compactness prevents using them directly as counterexamples.
