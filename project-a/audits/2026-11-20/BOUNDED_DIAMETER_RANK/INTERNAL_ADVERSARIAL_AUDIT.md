# Project A — internal adversarial audit
## Bounded ordinary diameter and unbounded localic relation-composition rank
**20 November 2026. This is the INTERNAL report. It is deliberately omitted from the blind external-referee ZIP.**

## Verdict (severity ranked)

**A. Exact diameter-two formula `rank(D̃_n)=2n+4`: accepted as internally proved, subject to independent examination of the standard finite-rectangular calculus.** The point-generation, quotient, upper bound, lower bound, and all-parenthesization assertions survived independent reconstruction. A finite support-state calculation for `n=0,…,5` gives ranks `4,6,8,10,12,14`. This calculation is a consistency check rather than a locale proof.

**B. Diameter-one clique-completion unboundedness: accepted as internally proved.** All ordinary graph components are cliques. Every generating point pair is contained in one of finitely many adjacent clopen blocks; sublocale pullback preserves finite joins, so no k-factor word crosses more than k indices, regardless of parenthesization. `n ≤ rank(H_n) ≤ 3n+4`. The exact value is not claimed.

**C. Earlier six-step nonassociative gadget proof: NOT accepted as written.** The old block calculation treated images such as `Γ_f^smile∘(X×X)` as the **whole** `Q×X` and `Q×Q`, without establishing the relevant product stability of the enumeration map `N→Q`. The localic product of spatial sublocales can be nonspatial. An image coming from discrete point-pairs can be smaller than the full localic product. Thus the claimed six-step equality and exact rank for that *unmodified* gadget need separate repair. No counterexample is asserted, only an unsupported enlargement.

**D. Repaired connected nonassociative gadget and hub attachment: accepted as internally supported.** Adding one singleton edge `q_0↔i_0` joins its two ordinary graph components while preserving a localic associator witness over the closed point `b×{*}`. The proof only needs the exact image `Q×{*}` of an explicit restricted two-step pullback; it does not need the full `Q×X` block. The graph has ordinary diameter ≤6, hence every sixfold word fills the *ambient spatial* square. The attached family has bounded ordinary component diameter ≤9, is point-generated, reflexive and symmetric, has terminal component quotient, is nonassociative, and satisfies

```
2n+4 ≤ rank(F_n) ≤ 3 max(2n+4,6).
```

The upper bound is not asserted to be optimal.

## 1. Checks on Isbell density and the primitive supports

Fix `Q_i` the eventually-zero binary sequences in Cantor space and `I_i` the complementary subspace. They are dense point-generated sublocales. Isbell's density theorem supplies a common nonzero sublocale `B(C_i)≤Q_i∧I_i`, despite their disjoint point sets. Since their points together exhaust a **spatial** Cantor locale, their join is full: `Q_i∨I_i=C_i`. These are two distinct facts; neither asserts that `Q_i,I_i` are complements.

The point-generated relation is a *finite join* of a spatial diagonal and spatial rectangles with singleton factor. Its **composites** may well contain nonspatial rectangles, which is not a violation of point-generation of the original relation.

## 2. Rectangular composition: check and crucial scope

For `A×B` followed by `C×E`, the actual pullback is `A×(B∧C)×E`, with image zero if the middle meet is zero. If that middle locale is nonzero, classical overtness makes its product projection onto `A×E` a surjection, hence the image is the entire rectangle. In classical metatheory every locale is overt; this is not a constructive theorem without an extra hypothesis.

Pullbacks of sublocales preserve **finite** joins, not arbitrary ones. This suffices because each base relation is a finite sum of primitive rectangles plus the diagonal. Expansion yields finite sums of rectangular chains. Multiplication of those rectangular chains is associative because its only tests are adjacent nonzero support intersections. The diagonal is a genuine two-sided unit. Therefore every bracketing agrees for this restricted relation algebra. We did **not** assume associativity of arbitrary image-defined localic relations.

## 3. Diameter-two exact lower bound

For `x∈Q_0` a rational point and `y∈I_n` an irrational point, the only possible first non-diagonal edge is `Q_0→a_0`, and the only possible last is `b_n→I_n`. The height assignment

```
h(a_i)=2i;  h(Q_i)=h(I_i)=2i+1;  h(b_i)=2i+2
```

is constant on nonzero intersections of the primitive support types. Every primitive edge, including the added `I_i↔a_{i+1}` and old `b_i↔a_{i+1}`, changes height by at most 1. It takes ≥`2n+2` middle primitive edges to move from `a_0` to `b_n`; with first and last, ≥`2n+4`.

A finite join of sublocales whose pullbacks to a point are all zero cannot contain that point, because pullback preserves finite joins. This justifies the lower bound at the level of **localic images**. It is not an inference that every image has only ordinary point witnesses.

## 4. Diameter-two upper bound

`a_i×a_{i+1}` is present at cost two by the nonzero pullback `Q_i∧I_i`. For `i<j`, reach `a_{i+1}` from any support in block `i` in ≤3 factors, advance to `a_j` in `2(j−i−1)` factors, reach any support in block `j` in ≤3 factors. This gives `2(j−i)+4≤2n+4`. Within one block all pairs take ≤4 factors; symmetry covers reversed order. All these are full **rectangular** inclusions, so `Q_i∨I_i=C_i` supplies the entire ambient square after taking the finite join. Reflexivity pads shorter words to a common length.

## 5. Independent symbolic computation

The accompanying optional script `05_support_rank_check.py` models exactly four support types per Cantor component (`Q,I,a,b`), declares `Q_i∧I_i≠0`, and performs finite-rectangular multiplication. The computational results are:

| n | diameter-3 candidate | diameter-2 candidate |
|---|---:|---:|
| 0 | 4 | 4 |
| 1 | 7 | 6 |
| 2 | 10 | 8 |
| 3 | 13 | 10 |
| 4 | 16 | 12 |
| 5 | 19 | 14 |

No script execution proves image stability; that comes from the overt-middle projection lemma above.

## 6. Diameter-one clique completion

Let `Z_i=C_i⊔{a_i}⊔{b_i}`. Each **ordinary** graph component of the original diameter-three relation meets at most `Z_{i-1}∪Z_i`. Its point-generated clique completion is contained in the finite clopen union of rectangles with `|i−j|≤1`. Thus a k-factor word lies in the union of clopen rectangles with `|i−j|≤k`, by a bracketing induction. A nonzero `Z_0×Z_n` is missed for `k<n`. On the other hand, the clique relation contains the original relation, whose `3n+4`-fold composite is full. The component quotient remains terminal. Result: `n≤rank(H_n)≤3n+4`.

This proof does **not** identify `H_n` with the join of entire products of rational sublocales; the clique is defined by ordinary point-pair generation precisely to preserve point-generation.

## 7. Connected nonassociative gadget: repair rather than import

The old gadget `X⊔Y⊔{b,r}` has `X=N∪{*}`, full `X×X`, graph `Γ_f` of `f:N→Q⊂Y`, `I↔b`, and `b↔r`. Add the single ordinary edge `q_0↔i_0` with `q_0∈Q`, `i_0∈I`. Then

```
(b,*)∈ D_*∘(D_*∘D_*),
(b,*)∉ (D_*∘D_*)∘D_*.
```

Here the **nonzero** first claim is checked using `Q×{*}≤D_*²`, obtained by restricting the actual first-two-edge pullback `Γ_f^smile×_X(X×X)` to `*` *before* taking the image. The resulting image is `Q×{*}`; composing `b×I` with it gives `b×{*}` since `I∧Q≠0`.

The **zero** claim is checked by the actual two-step block `(D_*²)_{b,X}=0`, using the coproduct decomposition `N×_Y I=0`. The added point bridge only creates a two-step `b→q_0`, not a `b→X` block. The last factor `D_*` has no incoming edge to `*` except from `X`, making the other bracketing zero on `b×{*}`.

The point bridge makes the ordinary graph connected with diameter ≤6. Any 6-factor bracketing contains every ordinary pair via padded length-6 paths. Because the **ambient** `G_*²` is spatial, its join of all point sublocales is the entire square. Hence every 6-factor bracketing is full. This is fundamentally different from inferring that the point-generated image of a discrete enumeration is `Q×Q`.

## 8. Hub attachment and universal lower bound

Attach the gadget at `r` to chain point `a_0`. A continuous retraction of the disjoint union to the chain collapses the gadget to `a_0`; its image on the relation is exactly the chain relation. Direct images obey the valid **lax** orientation

```
f_*(R∘S) ≤ f_*R ∘ f_*S,
```

as the genuine composability object maps into composable image edges. By induction, complete composition of the big relation would force complete composition of the chain relation, proving rank ≥`2n+4`.

For an upper bound take `m=max(2n+4,6)`. Any m-factor word contains both full original summand squares, by monotonicity. It contains the bridge by reflexivity. The particular triple `(W_m∘W_m)∘W_m` fills cross blocks, so length ≤`3m`. Ordinary component diameter remains bounded by 9; the associator witness is unchanged.

## 9. Scope and recommended external-audit priorities

**Primary external audit:** exact `2n+4` formula; rectangle lemma and finite-join use; cliquification block bound. **Secondary:** repaired nonassociative gadget and lax-collapse lower bound. Ask external referee to test each assertion independently, with no access to this report. Do not present the old six-step gadget's unverified rectangular block equality as an accepted lemma.

The attached blind packet is suitable for independent assessment. The earlier five-step minimality / six-step saturation of the *unmodified* gadget remains an open verification obligation; it is **not required** for the new unbounded families.