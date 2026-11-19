# Project A — what constitutes a two-step middle support?

**18 November 2026. General localic lemma checked internally, accompanied by two compact-Hausdorff counterexamples. Not externally audited.** This note follows the mixed-colour positive/negative finite-fence tests. It distinguishes an exact *closed triple-support* criterion from the weaker overlap of middle images and from the stronger rectangular common-channel test.

## 1. Exact closed triple-support criterion

Let `X` be any locale, `H≤X×X` a localic relation, `T=H∘H` its image-defined square, and `A,B≤X` closed sublocales. In `Y=A×X×B` set

\[
L=Y\wedge\pi_{12}^{-1}H,\quad R=Y\wedge\pi_{23}^{-1}H,\quad P=L\wedge R.
\]

**Proposition 1.** The following are equivalent:

1. `T∧(A×B)≠0`;
2. `P≠0`;
3. some nonzero closed `C≤Y` makes `L∧C` and `R∧C` both dense in `C`;
4. some nonzero closed `C≤Y` has `B(C)≤L∧R` (Booleanization taken as sublocale of `C`).

**Proof.** Let `Z=π₁₂⁻¹H∧π₂₃⁻¹H≤X³` be the actual composable-pair locale and `f:Z→X²` the outer projection. The inverse image of the closed outer rectangle `A×B` is precisely `P`. If `T∧(A×B)=0`, pulling back along `f`, which factors through its image `T`, gives `P=0`. Conversely, if `P=0`, `f` has empty preimage of `A×B`, hence factors through its complementary *open* sublocale. Consequently its localic image `T` is disjoint from `A×B`. This proves 1⇔2 without any image/closed-base-change equality.

If `P≠0`, let `C=cl_Y(P)`. It is nonzero and closed, and `P` is dense in `C`; therefore each of `L∧C` and `R∧C` is dense in `C`. By Isbell's density theorem both contain the least dense sublocale `B(C)≠0`. This establishes 2⇒3⇒4⇒2. ∎

**Interpretation.** The criterion genuinely requires a closed *incidence correspondence* `C` in the triple product. It is not intrinsically a subset of the middle locale alone. The existence of `C` is equivalent to nonvanishing, but this alone does **not** give a join decomposition of `T` into such Boolean cores.

## 2. Overlap of projected middle images: necessary, not sufficient

Let `u:H∧(A×X)→X` and `v:H∧(X×B)→X` be the two middle projections, with image sublocales `M_u,M_v≤X`. If `P≠0`, its middle image is a nonzero sublocale of `M_u∧M_v`. Hence

\[
T\wedge(A\times B)\ne0\quad\Longrightarrow\quad M_u\wedge M_v\ne0.
\]

The converse fails even for a point-generated ordinary equivalence relation on a **compact Hausdorff** locale with perfect outer supports and two-element nonsingleton components.

**Counterexample 2 (incompatible clopen labels).** Take disjoint compact Cantor spaces `A,M,B`, and `X=A⊔M⊔B`. Partition dense open subsets of `A,B` into pairwise disjoint nonempty clopen pieces `(A_n),(B_m)`. In `M`, recursively choose mutually disjoint compact nowhere-dense Cantor sets `(K_n),(J_m)` so that the unions of each family are dense in `M`. (At stage `n`, choose one new Cantor of each colour inside the `n`th basic open of `M`, avoiding finitely many previously chosen nowhere-dense compacts.)

Select countable dense subsets of every `A_n,B_m,K_n,J_m`. Pair selected `A_n` points bijectively with selected `K_n` points, and selected `J_m` points with selected `B_m` points. Let `E` be the ordinary equivalence relation with these two-element classes and all other classes singleton, and `H=[E]` its point-generated localic relation.

Both middle images restricted to the clopen middle component `M` are dense, and therefore their intersection contains `B(M)≠0`. Nonetheless `P=0`: the left one-step restriction into `M` is supported over `⋃_n A_n` in the first coordinate and confines its middle coordinate to `K_n` over `A_n`; the right restriction is supported over `⋃_mB_m` in the third coordinate and confines the middle coordinate to `J_m` over `B_m`. Thus a composable pair must live in the open locale `⋃_{n,m}(A_n×M×B_m)`. On the `(n,m)` open-and-closed piece it is zero since `K_n∧J_m=0`. These pieces cover the open support, so `P=0` and Proposition 1 gives `T∧(A×B)=0`. There is no illegitimate distribution of meet over infinite sublocale joins: the proof restricts to the open coproduct pieces and uses each closed middle separation individually.

The lesson is that *which* outer label reaches a given middle piece matters. Dense individual projections discard this incidence information.

## 3. Rectangular common channels: sufficient, not necessary

The earlier positive lemma says that if ordinary one-step pair traces are dense in `A'×V` and `V×B'` for a common patch mediator `V`, then `B(A'×B')` is included in the patch two-step relation. The converse to this rectangular density test fails even in a compact Hausdorff two-element-class model.

**Counterexample 3 (a diagonal correspondence).** Take disjoint copies `A,M,B` of a Cantor space `K`, and disjoint dense subsets `D_0,D_1⊂K`. For each `t∈D_0`, make `{a_t,m_t}` a two-element equivalence class; for each `t∈D_1`, make `{m_t,b_t}` one; all other points are singletons. Put `H=[E]`. The closed triple diagonal

\[
C=\{(a_t,m_t,b_t):t\in K\}\cong K
\]

has a dense set of first-colour triples and a dense set of second-colour triples. Both one-step localic restrictions contain `B(C)`. The outer projection `C→Γ={(a_t,b_t):t∈K}` is a homeomorphism, so its nonzero Booleanization satisfies

\[
0\ne\mathcal B(\Gamma)\le(H\circ H)\wedge(A\times B).
\]

But the ordinary left incidence relation is contained in the closed graph `a_t↔m_t`, and the right in `m_t↔b_t`. For both pair traces to be dense in nonempty *rectangular spatial* products `A'×V` and `V×B'`, each rectangle must lie in the corresponding graph. This forces all three subspaces to be the same singleton `t`, which would require `t∈D_0∩D_1=∅`. Hence there is no rectangular common dense channel. The support `C` really is correlated.

## 4. A useful condition restoring the middle-image test

**Proposition 4.** Let `u:R→X`, `v:S→X` be any localic maps with images `M,N`. If **either** map is open or proper, then

\[
R\times_X S\ne0\quad\Longleftrightarrow\quad M\wedge N\ne0.
\]

**Proof.** Necessity follows by taking the middle image of the fibre product. Suppose `u` is open (respectively proper). Then `M` is an open (respectively closed) sublocale of `X`, and the induced `R→M` is an open (respectively proper) surjection, hence pullback-stably surjective. If `M∧N≠0`, then `v^{-1}M≠0`: otherwise `v` factors through the complementary closed (respectively open) sublocale, forcing `N∧M=0`. Pulling `R→M` back along `v^{-1}M→M` produces a surjection from `R×_X S` onto the nonzero locale `v^{-1}M`. The other orientation is symmetric. ∎

This lemma relies on the established pullback stability of open/proper *surjections*. It does **not** assert that the special finite-fence middle projections are open or proper; their point-generated, nonclosed incidence supports make that a separate and likely restrictive condition.

## 5. Status and next direction

The exact general criterion has survived these two contrasting tests. The desired *geometric* classification of the finite-fence mixed two-step sublocale remains open. A new constructive companion, `ProjectA_MixedColour_Correlated_Cantor_Supports_2026-11-18.md`, uses the fence's full-gap, endpoint-conditioned density to build **nonrectangular graph-shaped positive supports in that actual model**.

The next precise problem is whether the mixed-colour two-step restriction is generated as a **join** of Booleanizations of admissible closed incidence correspondences, and whether those correspondences admit a useful geometric/combinatorial parametrization. Neither assertion follows from Proposition 1 alone.

**Primary background:** Picado–Pultr, *Locales treated mostly in a covariant way*, §5.6 (Isbell density), `https://www.mat.uc.pt/~picado/publicat/LLNchapter.pdf`; Picado–Pultr–Tozzi, *II. Locales*, §5 (open/proper maps and stable surjections), `https://www.mat.uc.pt/~picado/publicat/Chapter2.pdf`.
