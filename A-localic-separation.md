# A — Localic separation relations (active)

**Update:** Detailed working proofs and explicit finite/pointless examples are now in [A-hierarchy-first-results.md](A-hierarchy-first-results.md). See also [the Picado–Pultr 2021 reading notes](A-reading-Picado-Pultr-2021.md).

**Working notes, 2026-10-18.** The definitions and elementary deductions below are starting points, not claims of novelty. In particular, diagonal-closure separation has an existing locale-theoretic literature. All claims involving arbitrary locales merit checking against standard conventions for sublocales, products, and real-valued locale maps.

## 1. Motivation and notation

Cameron–Kumar, *Graphs on topological spaces*, arXiv:2610.14783, define relations on pairs of points: inseparable, Urysohn-inseparable, and indistinguishable by continuous real-valued functions. To treat pointless locales, use **sublocales of X × X** rather than a graph whose vertex set is the points.

Let `L=O(X)`, `O(X×X)=L⊗L`. For `a,b∈L` write `a⊠b` for the open rectangle. The diagonal map `δ:X→X×X` satisfies `δ*(a⊠b)=a∧b`. The closure of a sublocale `S` is the complement of the largest open sublocale disjoint from `S`.

## 2. Inseparability relation

Define
```text
d_I = ⋁ {a ⊠ b : a,b ∈ L, a ∧ b = 0}.
I(X) = (X×X) \ d_I,  as a CLOSED sublocale.
```
Equivalently `I(X)=cl(δ(X))` (the closure of the diagonal *image* as a sublocale).

**Proof (working).** A rectangle `a⊠b` pulls back along the diagonal to `a∧b`. Every open of `L⊗L` is a join of rectangles. Hence the join of all opens whose diagonal pullback is zero is precisely `d_I`.

For a spatial space `T`, the ordinary points `(x,y)` in this closed sublocale are exactly pairs admitting no disjoint open neighborhoods. **Caution:** the localic product of spatial locales may have additional points; pointwise equality should not be mistaken for equality of the complete localic relations.

**Research:** relate `I(X)=δ(X)` to strong Hausdorffness and variants, carefully specifying whether equality is with the diagonal image or its closure and whether the diagonal is a closed embedding.

## 3. Urysohn-inseparability relation

Set `a*=a→0` (pseudocomplement). Define
```text
d_U = ⋁ {a ⊠ b : a*, b* ∈ L and a* ∨ b* = 1}.
U(X) = (X×X) \ d_U  (closed sublocale).
```
For a spatial topological space, `a* = T \ cl(a)`; therefore `a*∨b*=1` iff the ordinary closures of opens `a,b` are disjoint. Thus the ordinary point pairs in `U(X)` satisfy the Cameron–Kumar Urysohn-inseparability condition.

Since `a*∨b*=1 ⇒ a∧b=0`, one gets `d_U≤d_I` and so **`I(X)⊆U(X)`**.

**To verify:** What is the recognized point-free Urysohn separation axiom? Is it exactly `U(X)=δ(X)`, or a related localic/diagonal condition? In general pointwise and localic versions can differ.

## 4. Functional equivalence

For every localic map `f:X→ℝ`, let
```text
K_f = (f×f)^−1(Δ_ℝ)   (kernel-pair sublocale)
F(X) = ⋂_{f:X→ℝ} K_f.
```
There is a set of such maps (frame homomorphisms `O(ℝ)→L`), so the intersection exists. `F(X)` is an equivalence relation in locales (kernel pair of the canonical evaluation morphism to a product of copies of ℝ). On spatial points, it is equality under every continuous real-valued function.

**Working inclusion:** `U(X)⊆F(X)`. For each `f`, the inverse image of an off-diagonal rectangle of ℝ can be covered by rectangles with disjoint-closure rational intervals; their preimages `a,b` satisfy `a*∨b*=1` (check closure behavior via continuity). Thus the complementary open of `K_f` is below `d_U`. Equivalently `U(X)⊆K_f` for every `f`. **Action:** expand this into an entirely internal locale proof, avoiding implicit arguments about ordinary points.

We consequently expect `I(X)⊆U(X)⊆F(X)`.

## 5. What needs checking before writing a paper

1. Compare with separation of locales by diagonal closure, strong Hausdorffness, Urysohn locales, regularity, complete regularity, and the completely regular reflection. Cite the *exact* known theorem before claiming novelty.
2. Distinguish sublocale inclusion from inclusion of underlying sets of points, and distinguish product locale from an ordinary topological product.
3. Check whether `F(X)` is indeed the kernel pair of the evaluation map in the required category; prove equivalence relation and set-size details.
4. Seek examples with strict `I⊊U⊊F` **as sublocales**, not merely distinct spatial-point relations.
5. Study products and inverse-image behavior: preimage of `I(Y)` need not equal `I(X)`; specify hypotheses for exact formulas.
6. Investigate whether specialization and closure-meeting admit intrinsic, useful **relations** or require a deliberately different construction. Do not force an unjustified five-relation hierarchy.
7. Check coincidence criteria and comparison with Cameron–Kumar's finite Alexandrov results.

## 6. First concrete tasks

- [ ] Formal proof of `U(X)⊆F(X)` in frame language.
- [ ] Literature table of competing Hausdorff/Urysohn definitions for locales and precise implications.
- [ ] Find strictness examples, preferably both spatial and pointless.
- [ ] Explore characterization of `I(X)=U(X)` and `U(X)=F(X)`.
- [ ] Check product formulas for all three relations.

## Reading list to check

- Cameron–Kumar, *Graphs on topological spaces*, [arXiv:2610.14783](https://arxiv.org/abs/2610.14783).
- Jorge Picado and Aleš Pultr, *Frames and Locales: Topology without Points* (Springer, 2012).
- Literature on **strong Hausdorff locales**, closure of the diagonal, and localic diagonal separation (bibliographic details to verify).
- Literature on **completely regular reflections** of locales and **functionally Hausdorff** separation.
