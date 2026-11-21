# Independent blind referee report

**Project A: balanced witness transport and scattered-index localic matrix algebras**  
**21 November 2026**  
**Material examined:** `00_README_FIRST.md`, `01_REFEREE_PROMPT.md`, `02_BLIND_MATHEMATICAL_PACKET.md`, `03_DEPENDENCIES_AND_PROVENANCE.md`.  
**Scope:** Classical locales, genuine sublocale pullback and localic image; left-to-right relational composition. I have not consulted the authors' internal audits or earlier referee verdicts. The previously reviewed rectangular composition formula (RC) has been treated as an *assumption*, not independently re-proved.

## 1. Executive verdict

The central scattered-index and matrix theorems **survive the audit**. The apparent danger—interchanging an arbitrary join of sublocales with an unrelated pullback or meet—is avoided in the actual proofs. In particular, the argument for (MUL) decomposes the *already formed* composability sublocale and only then applies a join-preserving image. This is the correct order of operations.

I find **one literal edge-case counterexample** to the abstract group identification in Theorem 3.1: the stated quantifier allows an empty fibre space `P`. I also find **one incomplete assertion** in the ancillary graph-algebra part of Section 4: a coordinatewise lattice isomorphism alone does not establish the localic composition and rectangle-transport laws for partially defined graphs embedded in an unspecified ambient compact space. A precise, readily provable sufficient version is given below. Neither finding undermines the main nonempty-fibre wreath-product construction or the exact matrix lift.

| Claim | Disposition | Qualification |
|---|---|---|
| SPLIT, Lemma 2.1 | **Correct** | The infinite outside-fibre join is first bounded by *one* complementary open sublocale. |
| MAT, Theorem 2.2 | **Correct** | The fit/open separation and least-closed-support arguments work; the perfect-space sharpness sentence should say **nonempty** perfect. |
| MATn, Corollary 2.3 | **Correct** | Finite products of scattered spaces are scattered. |
| Balanced-witness Theorem 1.1 | **Correct conditional on RC, (G), (T), (O)** | All eight generator-triple types pass; finite joins only. |
| GRP, Theorem 3.1 | **Correct** as a localic multiplication law | The claimed *abstract wreath-product isomorphism* **needs `P ≠ ∅`**; as worded it is false for `P = ∅`. |
| ACT and BAL, Theorem 3.1 | **Correct** | Requires the full MAT/MATn sector decomposition; works for nonspatial `q`. |
| Resulting global-rectangle/monomial algebra | **Correct conditional on RC** | Also correct if the graph group is trivial in the empty-fibre case. |
| TWIST, Section 4: full sublocale-lattice transport | **Correct** | This is an order/lattice isomorphism, not a locale isomorphism or homeomorphism. |
| TWIST, Section 4: ensuing partial-graph criterion | **Unproved / needs a precise hypothesis** | The phrases “suitable locally closed sectors” and “remain inside the family” do not themselves specify the necessary pullback/image compatibility. A narrower sufficient theorem is supplied in §4. |
| MUL, Theorem 5.1 | **Correct** | Binary formula for **arbitrary** localic relations; no base associativity needed. |
| FINMAT, Theorem 6.1 | **Correct** | Row-and-column finiteness reduces every relevant calculation to *finite* joins. |
| PATH, Corollary 6.2 | **Correct** | As displayed, `n ≥ 1`; `n = 0` follows by the empty-walk convention. |
| Closed-edge and infinite-index illustrations | **Correct** | Their global union need not be closed; an explicit example is given in §5. |

## 2. Priority verification: atomic scattered indices

### 2.1. SPLIT: no illicit infinite distributivity (packet lines 93–100)

Write `F_k = Z × {k}` and `U_k = Z × (K \ {k})`. For an arbitrary family `(A_j)` and fixed `k`, put

\[
J=\bigvee_{j\ne k}(A_j\times\{j\}).
\]

Since each summand is below the **same open** `U_k`, so is `J`. Thus `J ∧ F_k = 0`. The whole join is `(A_k × {k}) ∨ J`, a **binary** join, and finite distributivity in the sublocale coframe gives

\[
[(A_k\times\{k\})\vee J]\wedge F_k=A_k\times\{k\}.
\]

This proves `Φ_Z Σ_Z = id` without distributing the meet with `F_k` over an infinite join. Every selected fibre of `W` is a sublocale of `W`, giving `Σ_Z Φ_Z(W) ≤ W`.

Nothing here needs scatteredness; in fact compactness is unnecessary for this particular argument provided `K` is `T_1` and the sectors are closed.

### 2.2. MAT: positive implication (packet lines 120–124)

The proof uses exactly the following structural facts, all valid for compact Hausdorff spatial locales:

1. The ambient product `X = Z × K` is regular, hence **fit**: any sublocale `J` is the meet of the open sublocales containing it. Therefore `W \nleq J` yields an open `O` with `J ≤ O` but `W \nleq O`.
2. For the complementary closed `F = X \setminus O`, `W' = W ∧ F` is nonzero. Indeed, `O ∨ F = X` and `O ∧ F = 0`; if `W ∧ F = 0`, finite distributivity would force `W ≤ O`.
3. The least closed support `L = cl_X(W')` is a **nonempty closed subspace** of the compact Hausdorff `X`, so is compact Hausdorff. It is the closure of `W'` in the localic sense.
4. The projection `P_0 = pr_K(L)` is nonempty and compact, hence closed in the Hausdorff `K`. If `K` is scattered, there are `k ∈ P_0` and an open `V ⊆ K` with `V ∩ P_0 = {k}`.
5. The open part `L ∧ (Z × V)` is nonzero: `L` is an ordinary nonempty closed subspace with a point projecting to `k`. Moreover `L ∧ (Z × V) ≤ Z × {k}`. The *density* of `W'` in its least closed support implies `W' ∧ (Z × V) ≠ 0`, hence `W' ∧ (Z × {k}) ≠ 0`.
6. But `W' ≤ W`, and by definition `W ∧ (Z × {k})` is a generating summand of `J = Σ_Z Φ_Z(W)`. Therefore `W' ∧ (Z × {k}) ≤ J ∧ F = 0`, contradiction.

The density implication in (5) is genuinely **localic**. For completeness: if a dense sublocale `D ≤ L` missed a nonzero relatively open `U ≤ L`, then `D` would lie in the complementary proper closed sublocale of `L`, contradicting `cl_L(D)=L`. No point of `W'` is selected, and none is needed.

**Verdict:** the separation step, the projection step, and the isolated-fibre step are sound; there is no concealed infinite meet/join interchange.

### 2.3. MAT: converse and sharpness (packet lines 118, 126)

If `K` is non-scattered, choose a nonempty subset without isolated points. Its closure `F` is still nonempty and has no isolated points: an isolated point of the closure would have to lie in the dense subset and be isolated there. Thus `F` is a nonempty closed perfect subspace.

The Booleanization `B(F)` is a **nonzero** least dense sublocale of `F`. For every `x ∈ F`, the open `F \ {x}` is dense in `F`. Minimality gives `B(F) ≤ F \ {x}`, and consequently `B(F) ∧ {x} = 0`. The sublocale is therefore invisible to all singleton sectors although it is nonzero. This disproves (ii), and taking `Z = 1` shows the necessity of scatteredness in (iii).

One tiny scope amendment is needed in line 126: **“If `K` is nonempty and perfect”**, rather than merely “if `K` is perfect.” The empty space is conventionally perfect but its Booleanization is zero.

### 2.4. Finite products (MATn, lines 128–134)

Let `A` be a nonempty subspace of `K × L` with `K,L` scattered. Choose an isolated point `k` in its projection onto `K`. In the nonempty fibre `A ∩ ({k}×L)`, choose a point `(k,l)` whose second coordinate is isolated in that fibre. Suitable product-open neighbourhoods then isolate `(k,l)` in `A`. Hence `K × L` is scattered, and induction covers finite powers. The compact Hausdorff hypothesis passes to finite products, so MAT applies to `P^n × K^n`, `n=1,2,3`.

## 3. Priority verification: genuine graph sectors, ACT, BAL and balanced witnesses

### 3.1. Why restricting a point-generated graph to a *closed* sector is safe

This observation should be added explicitly before the proof of Theorem 3.1. Let `X` be a compact Hausdorff space, `A ⊆ X`, and `F ⊆ X` closed. Because `[A]_X` is the induced sublocale *generated by the points of* `A`, it splits as the **binary** join

\[
[A]_X=[A\cap F]_X\vee[A\setminus F]_X.
\]

The second term lies in the complementary open `X \setminus F`. It follows by finite distributivity that

\[
\boxed{[A]_X\wedge F=[A\cap F]_X.}
\]

Thus a point-generated global graph cannot acquire an extra pointless component upon restriction to a closed `(i,j)` sector. Its restriction is exactly the induced graph of `h_i` when `j = σ(i)`, and zero otherwise. This resolves the most conspicuous possible pointwise/localic gap in lines 176–179. The argument depends crucially on the sector being closed; it is **not** a license to intersect arbitrary point-generated sublocales pointwise.

### 3.2. Graph composition (GRP, lines 176–180)

By MATn, the full composability sublocale in `G^3` is determined by its closed `(i,j,k)` sectors. Restriction to such a sector commutes with the indicated pullbacks (base change for a closed-sector inclusion). The component is zero unless

\[
j=\sigma(i),\qquad k=\tau(j).
\]

In that unique case the component is the graph locale of

\[
p\longmapsto\bigl(p,h_i(p),g_{\sigma(i)}(h_i(p))\bigr),
\]

which is homeomorphic to `P`; its localic image in the first and third coordinates is the graph of `g_{σ(i)} ∘ h_i`. Reconstruction across `(i,k)` sectors proves GRP. Similarly the transpose gives the graph of the inverse fibre permutation. The identity graph is the closed diagonal `Δ_G`.

This computation is **not** a replacement of localic composition by ordinary graph composition: the sectorwise fibre products and images are genuine localic ones, but they happen to be graphs of actual locale isomorphisms on `P`.

**Literal counterexample to the abstract isomorphism in line 160:** take `P=∅` and `K={0,1}` discrete. All the `H_{σ,h}` are the same zero relation (also `Δ_G`), so their group has **one** element. But `Homeo(P)^{|K|} ⋊ Sym(|K|) ≅ S_2` has two. Repair: add `P ≠ ∅` to the faithful wreath-product identification. The multiplication identity GRP itself remains valid for `P=∅`. When `P` is nonempty, distinct `(σ,(h_i))` have distinct point graphs, so the desired identification is faithful.

### 3.3. Full rectangle action (ACT, lines 181–183)

For each closed index `i`, the restriction of `[A]_G` is `[A_i]_P` by §3.1. Thus the `(i,j)` sector of `p_G(A,B)` is `p_P(A_i,B_j)`. For `q_G(A,B)=[A]_G × [B]_G`, localic base change along the two closed sector inclusions gives the **full localic product**

\[
(q_G(A,B))_{ij}=q_P(A_i,B_j).
\]

At the sole admissible middle index, composition with the graph of `h_j` acts on the second factor by the locale isomorphism `h_j`; therefore

\[
(id_P\times h_j)_!\bigl([A_i]_P\times[B_j]_P\bigr)
   =[A_i]_P\times[h_j(B_j)]_P.
\]

The product on the right is still the **full `q`-product**, even if nonspatial. For `p`, the image of the generated point graph gives exactly the point-generated rectangle. The symmetric calculation with `h_i^{-1}` proves the left action. The MAT reconstruction then yields ACT globally.

### 3.4. Balanced overlap (BAL, lines 169–183)

In MAT coordinates, a sublocale meet is computed coordinatewise. The `k`-coordinate of `[Θ(B)]_G` is `[h_{σ^{-1}(k)}(B_{σ^{-1}(k)})]_P`. Since each `h_i` induces an **isomorphism of full sublocale lattices**, it preserves meets and detects zero. Therefore a nonzero overlap in some output fibre is equivalent to a nonzero overlap in the corresponding inverse-transformed input fibre. BAL follows, even when the detected meet has no ordinary point.

For Example 3.2, the index permutation swapping `0` and `1` in a convergent sequence is discontinuous at `0`; nevertheless `σ^2=id`, and GRP gives `H∘H=Δ_G` as an actual localic relation. This example is valid.

### 3.5. Eight associativity checks (Theorem 1.1, lines 61–74)

Write `R_t(A,B)=t(A,B)`, where `t` is independently `p` or `q`, and put `m(B,C)` for the truth value of `[B]∧[C]≠0`.

| Type | Verification |
|---|---|
| **RRR** | Both bracketings give `q(A,F)` precisely when `m(B,C)` and `m(D,E)` hold (apart from the automatically zero outer-endpoint cases); otherwise zero. The intermediate `q` appears by RC. |
| **RRH** | Both sides use the same `m(B,C)` and then act by `h` only on the final outer endpoint `D`. |
| **RHR** | The left bracketing tests `m(h(B∩D_h),C)` and the right tests `m(B,h^{-1}(C∩E_h))`. These are equivalent **exactly by O**; both nonzero outputs are `q(A,D)`. |
| **RHH** | Both sides give the same subset `k(h(B∩D_h)∩D_k)=(k∘h)(B∩D_{k∘ h})`, preserving the rectangle type `t`. |
| **HRR** | Both sides transport the first outer endpoint backwards by `h` and use the same remaining middle test `m(B,C)`. |
| **HRH** | Both sides yield `t(h^{-1}(A∩E_h),k(B∩D_k))`, so there is no middle-overlap issue. |
| **HHR** | The two nested inverse-image restrictions equal the inverse image for the partial composite `k∘h`. |
| **HHH** | The exact graph-product rule G gives associative ordinary partial-map composition. |

The caution about vanishing outer endpoints is necessary but harmless: every relevant side then vanishes by T or RC. Inverse-image and direct-image identities for partial bijections have been checked on their *actual restricted domains*. The global unit is the identity graph, and converses exchange the rectangle endpoints and inverse the graph generators.

Since localic pullback on sublocale lattices preserves **finite** joins and localic image preserves joins, genuine relational composition distributes over finite joins. Thus the generator checks extend to the stated finite-join algebra. Products involving at least one rectangle stay rectangular; this establishes the two-sided ideal and the word normal forms. These conclusions remain **conditional on the imported RC formula**.

**A useful strengthening:** under G, T and RC, if all the generator triples associate, **O is also necessary** (provided `G` is nonempty). Apply RHR associativity to `q(G,B), Γ_h, q(C,G)`. The two bracketings equal `q(G,G)` or zero according to the two overlap tests. Since `q(G,G) ≠ 0`, the tests must agree. Thus O is not an arbitrary extra hypothesis: it is precisely the missing RHR obstruction within this setting. This does *not* claim to classify which graph families satisfy G and T.

## 4. Ancillary discrete-to-scattered transport: what is proved, and what needs specification

### 4.1. The full-lattice statement is correct

Since `D` is discrete,

\[
\operatorname{Sub}(Z\times P\times D)
 \cong \prod_{d\in D}\operatorname{Sub}(Z\times P).
\]

Since `K` is compact scattered and `Z × P` compact Hausdorff, MAT gives

\[
\operatorname{Sub}(Z\times P\times K)
 \cong \prod_{k\in K}\operatorname{Sub}(Z\times P).
\]

Reindex by the set bijection `b` and apply the complete-lattice automorphisms induced by `id_Z × h_d` in the respective coordinates. These operations define inverse **complete-lattice** isomorphisms, on genuinely nonspatial as well as spatial sublocales. In fact the direct-image/reindexing formula is

\[
(W_d)_{d\in D}\longmapsto
\bigl((id_Z\times h_{b^{-1}(k)})_!(W_{b^{-1}(k)})\bigr)_{k\in K}.
\]

The continuity and bijectivity of `g` are also correct. The inverse set function need not be continuous, and **the lattice isomorphism does not say `g` is a locale isomorphism**.

### 4.2. The further (G)/(T)/(O) conclusion is not fully specified

Section 4 next speaks of “suitable locally closed sectors” in a compact Hausdorff ambient space and says that when partial graph composites “remain inside the family of such transports,” G, T, O follow. This is **not a sufficiently precise theorem statement**: one must state exactly how the source and target sectors are embedded in the common ambient space, how their meets are calculated there, and why the **point-generated graph relations** implement the given lattice transfers under *genuine composability pullbacks and images*. An abstract isomorphism of the two complete sublocale lattices does not itself furnish those compatibilities.

I am not asserting a counterexample to a reasonably formulated locally closed-sector theorem. The supplied proof simply does not establish such a general theorem from the currently displayed hypotheses alone.

**A concrete sufficient replacement (provable by the Section 3/5 sector method).** Take one compact scattered Hausdorff index `K_*` and one nonempty compact Hausdorff fibre `P`. In `X=P×K_*`, allow *partial monomial maps* on arbitrary subsets `D,E⊆|K_*|`, with an ordinary index bijection `b:D→E` and homeomorphisms `h_d:P→P` on each nonzero fibre. Use the point-generated graphs as relations in `X²`. Then closed-sector decompositions show:

- Each graph has at most one nonzero block in a row and column, and that block is a locale-isomorphism graph.
- Products and converses of such graphs are the graphs of ordinary partial monomial composites/inverses; this verifies G for the entire family.
- Right and left multiplication on either global `p` or full global `q` rectangle give the obvious forward/restricted inverse image, verifying T.
- The MAT decomposition of `Sub(X)` and the fibre homeomorphisms establish O.

Hence the balanced-witness algebra follows, conditional on RC. This covers a **well-defined restricted subcase** of the proposed transport framework; embedding an independently supplied discrete-to-scattered pair into this common-index setup may require an explicit construction, and should not be silently assumed.

It may well be possible to prove a stronger theorem for arbitrary locally closed sectors using their actual pullback diagrams, but that is a **separate proof obligation**. I recommend isolating the lattice-transport proposition from this proposed graph-extension corollary.

## 5. Priority verification: MUL, FINMAT, PATH and examples

### 5.1. Exact arbitrary binary matrix multiplication (lines 214–236)

The argument is correct, but the order of its steps deserves explicit emphasis:

1. Form the *actual* localic composability object `Q = π₁₂⁻¹(R) ∧ π₂₃⁻¹(S)` in `G³`. Do **not** try to form it by distributing a pullback through the infinite sector join of `R` or `S`.
2. Apply MATn to `Q` **after** forming it: `Q = ∨_{i,j,k} Q_{ijk}`. Closed-sector base change identifies
   \[
   Q_{ijk}=\pi_{12,P}^{-1}(R_{ij})\wedge\pi_{23,P}^{-1}(S_{jk})
   \quad\text{inside }P^3.
   \]
3. The direct localic image along `π₁₃` is left adjoint to inverse image of sublocales, and so preserves arbitrary joins:
   \[
   \operatorname{im}_{\pi_{13}}(Q)
      =\bigvee_{i,j,k}\operatorname{im}_{\pi_{13}}(Q_{ijk}).
   \]
4. Every displayed image lies in the *specific closed* output sector `(i,k)` and there is exactly `R_{ij}∘_P S_{jk}`. Set
   \[
   T_{ik}=\bigvee_j(R_{ij}\circ_P S_{jk}).
   \]
   The previous equality expresses `im(Q)` literally as `Σ_{P²}((T_{ik}))`. Apply **SPLIT (`ΦΣ=id`)** to recover the `(i,k)` output sector. This last manoeuvre is preferable to an unjustified attempt to meet the infinite global join directly with the sector.

This proves MUL even if `∘_P` is nonassociative. It uses neither RC nor any binary infinite-join distributivity for relation composition.

### 5.2. Locally finite lift (lines 240–277)

At fixed `(i,k)`, only the finitely many intermediate indices in the support of row `i` of `R` contribute to MUL. Because `A(P)` is closed under finite joins and composition, the resulting entry is again in `A(P)`. Row-finite × row-finite is row-finite; column-finite × column-finite is column-finite. Thus the product remains row-and-column finite.

Finite joins preserve the support condition by finite union. Converse transposes indices and takes the fibre converse; this is why **both** row- and column-finiteness are required. The unit has `Δ_P` on diagonal sectors and zero elsewhere, hence one nonzero block per row and column.

For a triple product and fixed outer indices `(i,ℓ)`, both bracketings reduce to the finite double family

\[
\bigvee_{j\in \operatorname{supp}(R_{i,-})}
\ \bigvee_{k\in \operatorname{supp}(S_{j,-})}
 (R_{ij}\circ_P S_{jk})\circ_P T_{k\ell}
\]

or its rebracketed version. Finite distributivity and associativity **only in `A(P)`** identify them. MAT then identifies the global sublocales. No global associativity or infinitary distributivity is being smuggled in.

### 5.3. PATH (lines 279–287)

For fixed start `i₀`, there are finitely many length-`n` walks for every fixed finite `n`, since each visited vertex has finitely many outgoing edges. FINMAT and finite distributivity yield the stated induction. Each path label is the **genuine left-to-right localic composite in `P`**, not ordinary pointwise relational composition. The displayed formula covers `n≥1`; if “all finite powers” includes `R⁰`, add the identity/empty-walk convention.

### 5.4. Concrete nonclosed global union (lines 289–294)

The warning about nonclosed global matrices is real, not just hypothetical. For `P` any nonempty compact Hausdorff space and `K={0}∪{1/n:n≥1}`, put the **full closed block `P²`** in sector `(1/n,1/(n+1))` for each `n≥1`, and zero in every other sector, including `(0,0)`. This is a row-and-column-finite matrix of closed `P`-relations. Its underlying point set has points approaching each `(p,0;q,0)` in the missing `(0,0)` sector. Thus the global relation cannot be closed. Nevertheless all its powers are associative by FINMAT.

The note's bidirectional nearest-neighbour example is likewise row-and-column finite; graph isolation of `0` is distinct from topological isolation in `K`. The distinction between the two extension mechanisms is also correct: for infinite `K` and nonempty `P`, the global full `q(G,G)=G²` has infinitely many nonzero blocks in every row and every column, so is **not** in the row/column-finite class.

The illustrative closed-relation base algebra should continue to be stated with the intended compactness/proper-image hypotheses; for the actual compact Hausdorff `P` of the packet, the usual closed-subset/pullback/projection argument applies.

## 6. Presentation, qualification, and dependency comments

1. **Introduce the closed-sector restriction lemma** of §3.1 before GRP. It explains why the fact that `σ` may be discontinuous does not cause a ghost in an individual closed sector.
2. **Explicitly name the finite-limit/base-change property** in GRP and MUL. Sectorwise equality of pullbacks is a localic statement, not a consequence of an equality of ordinary point sets.
3. **In MUL, explicitly apply SPLIT in the last line.** This rules out the mistaken interpretation that one has distributed sector meet over an arbitrary image join.
4. **Say “nonempty `P`” in the wreath-product isomorphism**, and **“nonempty perfect `K`” in the Booleanization sharpness sentence**. The remaining empty-space cases are harmless.
5. **Separate the TWIST lattice theorem from the proposed graph corollary.** Supply an ambient-sector/pullback hypothesis and proof, or present it as a conjectural/conditional programme. Do not infer relational properties merely from an order isomorphism on sublocales.
6. **Keep `p` and `q` visibly distinct** when explaining transport. In ACT the `q`-sector remains the *full locale product*; replacing it with the induced point rectangle would be an error.
7. **“Group”** is justified for the set of monomial graphs because their restricted product is associative, although the surrounding arbitrary localic relation operation may not be.
8. **“Exact” in MUL** means binary equality for actual localic composition, not a claim that the entire relation algebra is associative or distributes over all infinite joins.
9. **“Ideal”** means a two-sided ideal under composition within the finite-join algebra (and a finite-join subalgebra), not an ideal for arbitrary joins among all localic relations.
10. **Dependency separation matters:** MAT, MATn, GRP, ACT, BAL, MUL, FINMAT and PATH do *not* depend on RC. The rectangle-rich associative algebra and Theorem 1.1 *do* depend on RC.

## 7. Additional mathematical observations

Two modest deductions seem worth recording.

**(a) O is an exact RHR obstruction in the proposed regime.** As established in §3.5, with G, T and RC, requiring the `RHR` generator triples to associate is equivalent to O whenever the ambient `G` is nonempty. This is a useful converse *within the sufficient mechanism*, without claiming a general classification.

**(b) For a one-point fibre `P=1`, the entire localic relation algebra on a compact scattered `K` becomes the ordinary set-theoretic relation algebra on `|K|`.** Indeed, MAT for `K²` identifies every sublocale relation with a subset of `|K|²`, and MUL specializes to Boolean matrix multiplication: `(R∘S)_{ik}=∨_j(R_{ij}∧S_{jk})`. Hence in this special case **all** localic relations associate, even without row/column finiteness. The obstruction in the general setting comes from the nontrivial `P`-fibre relation calculus, not from the scattered index itself.

Neither observation requires another new hypothesis beyond those explicitly given.

## 8. Final recommendation

I recommend **accepting SPLIT, MAT, MATn, GRP (as a multiplication law), ACT, BAL, MUL, FINMAT and PATH after the minor clarifications above**. The full rectangular/monomial associativity theorem is **accepted conditional on the imported RC**, as the prompt permits. The **literal abstract wreath-group identification needs `P≠∅`**; this is an edge-case correction rather than a substantive collapse. The **Section 4 partial-graph extrapolation should be separated out** until its ambient assumptions and pullback/image compatibility are stated precisely; its coordinatewise full-lattice transport is already justified.

The main technical achievement—an exact matrix formula for **actual** localic composition over compact scattered indices, followed by a genuinely associative locally finite lift from an associative fibre algebra—appears mathematically sound on this independent reading.