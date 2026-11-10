# Blind referee report — Project A, W-phase packet

Nov 9, 2026 · @Someone

No false statement and no fatal gap found: the product theorem P2 (arbitrary second factor) and the connected strict diamond (Z8) are both correct as stated. One proof step in C1 needs a stated repair, one inherited lemma is used without proof but is true, and one control example cannot be checked from the packet.

## Executive verdict

Every principal claim survives. In particular W(P × Y) = W(P) × W(Y) holds for finite P and an arbitrary locale Y, and the chain (Z8) holds on Z = P × Y with every strictness and the incomparability of H and U.

**Scope actually checked.** I checked every numbered claim, formula and parenthetical in §§0–9 by hand, as statements about sublocales rather than point sets. The finite-poset computations (C3, the dual fence, the two forks in B2, the stage-reentry control) were also recomputed by script. I saw only the prompt and the packet. The checking is careful hand verification, not a formalization.

**Findings by class.**

| Class | Items |
| --- | --- |
| (a) correct as written | General inclusions of §0; inputs S1, S3–S6; B1, B2; C2, C3; F1–F5; A2–A4; M1, M2; Claims S1, S2 of §6; stage-reentry control; P1–P4; Z1–Z8 and the fitted supplement; R1 |
| (b) correct, specific repair needed | C1, step "U fitted ⇒ U = F"; input S2 (hypothesis wording) |
| (c) unproved gap | None that stays open. The "regular-core inequality" and input S3 are used without proof; both are true and proved in the appendix |
| (d) false | None found |
| (e) unverified import | The "negative control" of §5, whose space is never defined, and the three-summand remark in §6 that depends on it |
| (f) presentation | Label collisions, undefined Cm(P), topology at the origin in M2, undefined U∘U, and others listed below |

**Three things the authors should know beyond correctness.**

1. The caution attached to (Z3) is unnecessary. Preimage of sublocales along any locale map preserves arbitrary meets, so P² × K is fitted whenever K is.
2. Z is an instance of a general principle. For finite P and any Y, the relations W, U and H are all multiplicative, so P × Y satisfies W = H∧U exactly when Y does. Z8 is correct, but the two defects still sit in separate factors.
3. A T₁ compact connected space with W < H exists, with a purely pointless witness. It is described under the research ideas and is my own computation, offered for checking.

Items 2 and 3 are referee additions. Their proofs are in the appendix and are not part of what I was asked to certify.

## The four priority dependencies

All four are correct. None infers a sublocale inclusion from point sets alone, and no infinite meet is pulled back without justification.

### 1. Two-apex space: W(Y) = K and W(Y) = H(Y) — class (a)

- **Topology.** Y is compact, T₁, sober, connected and locally compact. Each N₊(F) is compact open, which gives compact neighbourhoods at the apexes. Y is not coherent because a compact open set inside a bounded real interval would be clopen in ℝ.
- **(A2).** The closure of a small interval at x > 0 is the closed interval plus p₊, and cl N₊(F) = A₊. This gives U(Y) = K ∪ {(p₊,p₋), (p₋,p₊)} as a point set. U is closed in a spatial square, so the point computation is legitimate.
- **A point worth stating.** The origin 0 is U-related to every point of Y. K absorbs this because A₊ ∪ A₋ = Y.
- **K ≤ W.** This rests on cl(int U) ≤ W, which the packet does not prove. It holds in every locale; see Appendix A1. Here int U contains u₊² ∪ u₋², whose closure is K.
- **W ≤ K.** This step is pointfree. D ∧ O(u₊⊠u₋) lies inside U ∧ O(u₊⊠u₋), a closed sublocale of a spatial open sublocale with exactly one point. A one-point locale has only two sublocales, and the binary cover excludes the point from D. Hence u₊⊠u₋ ≤ d\_W.
- **(A3).** The identity is exact, the sets C\_n^± are closed, and each w\_{±,n} contains K. The point-set equality ⋂ cl(a\_n) = {0, p₊} becomes a sublocale statement only through F4: a₁ ≤ ⋁ a\_n\* = Y ∖ {0, p₊}. For the rectangle towers, (a\_n⊠u₋)\* ≥ a\_n\*⊠1, so F4 applies again.
- **Conclusion.** F5 makes K fitted, so W = H. Formula (A4) also holds: its right side contains W and meets each sector of d\_W in 0. F(Y) = Y² and the strict chain W = H = K < U < F are correct.

Answer to the first §10 question: yes, pointless sublocales are handled.

### 2. Finite-branch theorem F3–F5 — class (a)

- **F3** holds in any coframe and is used in the right direction. The nontrivial inequality is ⋀⋁ ≤ ⋁⋀; it needs monotone towers and finite joins distributing over arbitrary meets. The infinite-branch counterexample is right.
- **F4** is correct and does not need the tower to be decreasing. Direct proof: S = ⋀ O(r\_n) meets every O(r\_n\*) in 0, so S ≤ C(⋁ r\_n\*), while S ≤ O(r₁) ≤ O(⋁ r\_n\*).
- **F5** is correct for arbitrary frames, any number of sectors, and finite width in each sector. Only the zero case of (F5a) is used, and that case is immediate: S ∧ O(t\_i) = 0 for all i means S ≤ ⋂ C(t\_i) = C(d).
- The neighbourhoods w\_{i,n} need not decrease in n. Only the towers r\_{i,j,n} must.

### 3. P1 and the product theorem P2 — class (a)

- **P1** holds for every poset P and every frame M. For frame maps f on Up(P) and g on M, the map v ↦ ⋁\_p f(↑p) ∧ g(v\_p) is the unique common extension. It preserves binary meets because ↑p ∩ ↑q is the union of the ↑r with r ≥ p, q.
- **Sections.** Under the square identification, (c⊠c) has (p,q)-section c\_p ⊠ c\_q. This is what (P3) needs.
- **Upper inclusion.** B2 applies; preimage preserves opens, closed sublocales and all meets.
- **Lower inclusion.** The slice i\_s is the locale map (s, id), with frame map w ↦ w\_s. Joins in Up(P, M) are pointwise, so the t-slices of a cover do cover Y. The restricted slice then factors through every O(w\_C), hence through D(P × Y).
- **(P4).** The closure of the image of a locale map is C(e), with e the largest open sent to 0. That is a pointfree description, and the displayed monotone family is that largest open.
- **Finite join.** The join of the closed sublocales (↓s) × W(Y) is computed by a pointwise finite meet of complements. It equals cl Cm(P) × W(Y), and cl Cm(P) = W(P) = U(P).

Nothing here uses points of Y, compactness, or spatiality. Answer to §10: P2 is true for arbitrary Y, and (P4) is a genuine localic closure.

A shorter route exists. Every cover of P × Y is refined by a product cover, which gives the stronger D(P × Y) = D(P) × D(Y); see Appendix A3.

### 4. Fitted-hull propagation Z2 — class (a)

- B × K is C(x) with x\_s = d\_K on B and x\_s = 1 off B. So an open w contains B × K exactly when w\_s ∨ d\_K = 1 for s in B.
- Monotone sections and ↑B = P² then give w\_s ∨ d\_K = 1 for every s. So w contains P² × K.
- **(Z3)** is correct. In Up(P², M) the implication a → x has s-section ⋀ (a\_t → x\_t), the meet over t ≥ s. For constant a this collapses to a → x\_s because x is monotone.
- No spatiality of sublocales of Z² is used. Answer to §10: yes.
- Closedness of B is never used in the proof; only ↑B = P² is.

## Audit of the remaining claims

Everything outside the four priority items is correct except C1, which needs one added line. Classes follow the prompt: (a) correct, (b) repair needed, (c) gap, (d) false, (e) unverified import, (f) presentation.

| Item | Class | Comment |
| --- | --- | --- |
| §0 general inclusions | (a) | D = ⋂ O(w\_C) holds because the w\_C are coinitial among opens containing Δ. U ≤ F uses regularity of ℝ. F is closed and fitted because ℝ² is regular. |
| Input S1 | (a) | True. One locally compact factor already suffices. |
| Input S2 | (b) | True for the locale of a scattered space. "Spatial scattered locale" should say that. All-sublocales-spatial has a weaker exact condition (Niefield–Rosenthal). |
| Input S3 | (a) | Used in C1 without proof or reference. Proof in Appendix A2. Needs the prime ideal theorem. |
| Input S4 | (a) | pt D is the set of pairs with a common lower bound. It is patch-closed, so its closure is its down-set, which is (C2a). "I∘I" is composition of point relations. |
| Input S5 | (a) | Verified through the quotient of the patch space by the least closed equivalence. |
| Input S6 | (a) | C(a) ∨ C(b) = C(a ∧ b). |
| B1 | (a) | All three equivalences hold, as does the normalization h(a) = k(b) = 1. |
| B2 | (a) | Both fork examples confirmed by script. The "respectively" assignment (open for 0\<p,q; closed for p,q<1) is right. |
| C1 | (b) | The step "U fitted ⇒ U = F" is incomplete. Repair in the next section. |
| C2 | (a) | With C1 repaired: W = H iff U contains the finite-zigzag relation. The Zorn argument for maximal points is fine. |
| C3 and the dual fence | (a) | Confirmed by script, including ↑U(P) = P². |
| F1, F2 | (a) | F1 is the fitness axiom at one element. F2 is immediate from fit\_T(S) = T ∧ fit\_Z(S). |
| Regular generation inside F | (a) | x ≺ d gives a neighbourhood x\* of C(d) disjoint from x. Clopen inside F is indeed stronger. |
| "Absolute rather-below forces W = U" | (a) | For a⊠b ≤ x ≺ d\_W, apply the codiagonal to (a⊠b)\* ∨ d\_W = 1. Since (a⊠b)\* = a\*⊠1 ∨ 1⊠b\*, this gives a\* ∨ b\* = 1. |
| Pointless-residual observation | (a) | Needs sobriety, so that locale points are the ordinary points. |
| M1 (αβγ space) | (a) | A² is scattered, so sublocales are subsets, and T₁ makes every subset fitted. I, U, F computed as claimed. |
| Negative control (§5) | (e) | The space is not defined in the packet. |
| M2 (m-apex star) | (a) | Correct with the metric-star topology at the origin, which should be stated. |
| Claims S1, S2 (§6) | (a) | Both are short reformulations. h is the largest element of R\_d. |
| Stage-reentry control | (a) | Confirmed by script: {a}, {a,s,b}, P. |
| Disjoint-sum control | (a), (e) | The two-summand statement is correct. The three-summand remark depends on the negative control. |
| Topology of Z | (a) | Compact, connected, locally compact, sober, T₀. The projection argument for noncoherence is valid. |
| Z1, Z4–Z8, fitted supplement | (a) | Z5 may use points because U is closed in a spatial square. The three witnesses in (Z7) and (Z8) check. |
| R1 (§9) | (a) | Uses scatteredness of (P × A)² correctly. H(P × A) = H(P) × I(A) also follows from Appendix A4. |

## Concrete errors, omissions and presentation corrections

There is one incomplete proof step, two premises used without proof, and one example that cannot be checked. The rest is presentation.

### Mathematical repairs

1. **C1, "U fitted ⇒ U = F" (class b).** The earliest incomplete step is "the minimality of F yields U = F". Minimality of F applies to patch-closed equivalences, and the packet shows only that U contains the finite-zigzag relation \~. Repair: (C2a) gives U ⊆ \~, since x ≤ u ≥ z ≤ v ≥ y is a zigzag. So U = \~, which is then a patch-closed equivalence containing comparability, and F ≤ U follows.
2. **Regular-core inequality (used in A2 and M2).** The packet calls it established and gives no proof. It is true in every locale, in the sharper form d\_U ≤ d\_W ≤ d\_U\*\*. Appendix A1 has the proof; the packet should include one.
3. **Input S3.** C1 depends on it and the packet gives neither proof nor reference. Appendix A2 has a short proof.
4. **Negative control in §5 (class e).** "Boundary points p < x and y, and two infinite discrete sheets" does not determine a space. One natural reading does give W = I < H = U = V = F: x is a limit of N₁, y of N₂, and p lies in cl{x} with neighbourhoods cofinite on both sheets. That reading is my guess, so I certify nothing about it.
5. **U∘U ≤ U in C1.** Composition of sublocales is not defined in the packet. Read as composition of closed point relations it is fine in the coherent case. Say so.
6. **M2.** State the topology at the origin o. The claims need basic neighbourhoods of o to contain an initial segment of every ray.

### Statements stronger or weaker than warranted

- **(Z3) caution.** "Do not assume arbitrary sublocale meets pull back" suggests a risk that does not exist. Preimage is right adjoint to image, so it preserves every meet of sublocales. This is textbook material in Picado–Pultr, Chapter III.
- **Z2.** Drop "closed" from the hypothesis on B, or say it is not used.
- **P1.** It is not special to finite posets and should not read as new. It is the usual description of a product with an Alexandrov locale.
- **S1.** Local compactness of one factor is enough.
- **"Striking" connected example.** Z8 is correct. But by Appendix A4 it is forced: any finite P with W(P) < H(P) times any Y with W(Y) = H(Y) < U(Y) gives the same diamond. Connectedness comes for free from the factors. The H-defect lives entirely in P and the U-defect entirely in Y, as in the disjoint-sum control.
- **Prior literature.** The packet cites none. Locales with fit Δ = Δ are the F-separated locales of Arrieta, Picado and Pultr, and Arrieta's later paper studies the closed/fitted duality for the diagonal. The operator fit(−) appears as "the other closure" in Clementino, Picado and Pultr. D and I should be introduced with those names. I did not find W, V or H in the abstracts I could open; I have not searched full texts.

### Reader experience

- **Label collisions.** S1–S6 name standard inputs in §0 and S1, S2 name claims in §6. F1–F5 sit beside the relation F and the finite sets F of (A1) and M2. Q is both the frame L⊕L and the deferred problem. Y is a generic locale in B2 and §7 and the two-apex space in §4 and §8. Also overloaded: A and A±, B (Boolean frame, relation in Z2, B(D)), I (relation and index set), h (frame map in B1, d\_H in §6), K, and P (the fence versus an arbitrary finite poset).
- **Cm(P)** is used in §7 and §9 and never defined. It is D(P) from (C3).
- **Orientation.** State once that x ≤ y means x ∈ cl{y}, opens are up-sets and closed sets are down-sets. The packet is consistent with this throughout, including "common upper bound" for I and "common lower bound" for D.
- **Choice.** Inputs S3–S5 and Claims C1, C2 need the prime ideal theorem, and C2 also uses Zorn. B1, the F-claims, §§4–8 and the finite-poset results need no choice.
- **Where spatiality is used.** A2, M2 and Z5 use it only for closed sublocales and for a one-point sublocale. M1 and R1 use scatteredness for all sublocales. P2 and Z2 use neither. A one-line map of this would help.
- **"Locally compact"** should be glossed for non-Hausdorff spaces: every point has a neighbourhood base of compact sets.
- **F3 counterexample.** The two-element algebra shows the lattice identity fails. A sublocale instance is discrete ℕ with S\_{j,n} = {j} for n ≤ j and empty otherwise.
- **A2.** Say explicitly that F4 is what turns ⋂ cl(a\_n) = {0, p₊} into a statement about sublocales.

## Separate verdicts

### Finite-poset product theorem (P2)

Certified as stated: for every finite upper-Alexandrov poset P and every locale Y, W(P × Y) = W(P) × W(Y). The proof in the packet is complete and pointfree.

The strongest form I can certify is the following. The first line is the packet's claim in sharpened form; the other two are referee additions that the authors should check (Appendix A3, A4).

```latex
\begin{aligned}
\mathcal D(P\times Y)&=\mathcal D(P)\times\mathcal D(Y), &\mathcal W(P\times Y)&=\mathcal W(P)\times\mathcal W(Y),\\
\mathcal U(P\times Y)&=\mathcal U(P)\times\mathcal U(Y), &\mathcal H(P\times Y)&=\mathcal H(P)\times\mathcal H(Y).
\end{aligned}
```

### Connected example Z = P × Y

Certified as stated. Z is compact, connected, locally compact, sober, T₀ and not coherent. W(Z) = U(P) × K, H(Z) = P² × K and U(Z) = U(P) × U(Y), so W(Z) = H(Z) ∧ U(Z).

The three point witnesses are right: ((m,0),(n,0)) is in H only, ((k,p₊),(k,p₋)) is in U only, and ((m,p₊),(n,p₋)) is in neither. Chain (Z8) therefore holds, with H and U incomparable and F(Z) = Z². The explicit fitted supplement (d, u, r) satisfies the criterion of Claim S1.

The four dependencies each hold independently of the others, so no weaker fallback statement is needed. One caveat on strength: Z is a product of two one-sided defects and follows from the formulas above for any such pair of factors. It answers the question as posed, but it is not evidence of a new interaction between H and U.

## Optional research ideas (two)

Both concern product behaviour of W and the gap between W and H∧U. Neither touches Q or Q′.

### Idea 1. A product theorem for compact factors

**Claim to test.** For compact locales X and Y, D(X × Y) = D(X) × D(Y) and W(X × Y) = W(X) × W(Y).

**Why it is promising.** The only input is that every cover of X × Y is refined by a product cover. Appendix A3 derives this from compactness of X × Y and a finite identity for rectangles that holds in all frames. P2 is the case where one factor is finite and the other arbitrary.

**One-step test.** Compute W(Y × Y) for the two-apex Y directly, by the sector method of A3 and F5. The claim predicts K × K after reindexing, and then W = H there because H(Y × Y) ≤ H(Y) × H(Y). Any pair outside K × K that survives in W falsifies the claim.

**Discriminating question.** Is compactness needed? A falsifier is a single cover C of some X × Y with D(X) × D(Y) not below O(w\_C). Arbitrary sums of compact pieces do not provide one, since D decomposes over clopen sums.

### Idea 2. Can the diamond occur in a T₁ space?

**Background.** By Appendix A4 a finite T₀ factor never changes whether W = H∧U. So an example in which H and U interact must look elsewhere, and T₁ squares are the natural place: there W < H forces a pointless residual.

**A test space T.** Take Y and replace 0 by a point q. Let q be an ordinary endpoint of the positive ray and a cofinite apex of the negative ray: basic neighbourhoods are {q} ∪ (0, ε) ∪ ((−∞, 0) ∖ G) with G finite. T is compact, connected, T₁, sober and locally compact.

**What I computed (Appendix A5, unchecked by anyone else).**

```latex
\begin{aligned}
\mathcal W(T)&=(u_+\cup\{q\})^2\cup(u_-\cup\{q\})^2\\
&<\;\mathcal U(T)=\mathcal W(T)\cup(\{p_+\}\times u_-)\cup(u_-\times\{p_+\})\\
&<\;\mathcal H(T)=\mathcal F(T)=T^2 .
\end{aligned}
```

So W < H does occur in a T₁ space, witnessed only by a pointless sublocale, and F5 visibly fails there. But H ∧ U = U, so T is not a diamond.

**Sharp statement to test.** In a T₁ sober space with spatial square, W = U implies W is fitted. If true, every T₁ diamond must have W < U and W < H through interacting defects. If false, the counterexample summed with Y is a T₁ diamond.

**One-step test.** T does not contradict the statement, because W < U there: p₊ creates U-pairs on the closure of the residual. Remove that mechanism in one move and recompute: find a W-point whose neighbourhood traces on a d\_W sector are dense, in a space where no U-pair lies off W. Either the trace argument of A5 survives, giving a counterexample, or the regular-core sandwich blocks it.

## Appendix: arguments supplied by the referee

A1 and A2 close gaps in the packet. A3 to A5 are referee additions; they are checked by hand once and should be treated as claims for the authors to verify.

### A1. The regular-core sandwich

In every locale, cl(int U) ≤ W ≤ U. Equivalently:

```latex
d_{\mathcal U}\;\le\;d_{\mathcal W}\;\le\;d_{\mathcal U}^{**}.
```

1. Let o be an open of the square with o ∧ d\_U = 0, and fix a cover C.
2. Suppose a nonzero rectangle a⊠b ≤ o misses w\_C. Then each c in C has c ∧ a = 0 or c ∧ b = 0.
3. Join the members of each kind: g₁ ≤ a\*, g₂ ≤ b\*, and g₁ ∨ g₂ = 1. So a\* ∨ b\* = 1 and a⊠b ≤ d\_U, a contradiction.
4. Hence w\_C ∧ o is dense in o for every C. A meet of dense sublocales is dense, so D ∧ O(o) is dense in O(o).
5. Therefore W ≥ O(o). With o = d\_U\* this gives W ≥ C(d\_U\*\*).

The sandwich is not tight in general: Cantor space has W = U = Δ and int U empty.

### A2. Input S3

Let C be a closed sublocale of a coherent locale, with open complement d.

- **Fitted ⇒ up-set.** Points of a meet of sublocales are the intersection of the point sets, and an intersection of open sets is an up-set.
- **Up-set ⇒ fitted.** A patch-closed up-set is a filtered intersection of compact opens w\_i. Check (F1): given d ≰ b, pick a point y in d ∖ b and a compact open G with y ∈ G ⊆ d. G ∖ b is patch-closed and misses C, so by patch compactness it misses some w\_i. Then G ≤ w\_i → b and G ≰ b, so w\_i → b ≠ b, with w\_i ∨ d = 1.

### A3. Product covers, and D for products

1. **Lemma.** If a cover C of X × Y is refined by a product cover {a⊠b : a ∈ A, b ∈ B}, then D(X) × D(Y) ≤ O(w\_C). Reason: w\_A ⊗ w\_B is the diagonal-square open of the product cover, and it lies below w\_C.
2. **Consequence.** If every cover is so refined, D(X × Y) = D(X) × D(Y). The other inclusion is B2.
3. **From D to W.** A product of dense sublocale inclusions is dense, because a nonzero open contains a nonzero rectangle. So cl(S × T) = cl S × cl T, and W is multiplicative whenever D is.
4. **Finite P.** For a cover C of P × Y, each family {c\_p : c ∈ C} covers Y. Let B be the common refinement over the finitely many p, and A = {↑p}. Each ↑p⊠b lies in some c. This reproves P2.
5. **Compact X and Y (sketch).** Reduce C to finitely many rectangles a\_i⊠b\_i with join 1. For every set J of indices, either the a\_i with i in J cover X or the b\_i with i outside J cover Y. This holds because the pairs (x, y) with that property form a coproduct ideal containing the generators. Let 𝒥 be the sets J whose b\_i cover Y. Let A consist of the meets of the a\_i over i in J, one for each J in 𝒥. Let B consist of the meets of the b\_φ(J) over J in 𝒥, one for each choice function φ on 𝒥. Both cover, and each product piece lies in some a\_i⊠b\_i.

### A4. U and H with a finite factor

**U.** In Up(P, M) the pseudocomplement v\* has p-section (⋁ v\_q)\*, the join taken over q ≥ p. If (p, q) is not in U(P), the indicators of ↑p and ↑q have v\* ∨ v′\* = 1, so the (p, q)-section of d\_U is 1. If (p, q) is in U(P), pick z ≤ u, u′ with u ≥ p and u′ ≥ q. Evaluating v\* ∨ v′\* = 1 at z gives (v\_p)\* ∨ (v′\_q)\* = 1, and constant families give the reverse bound. So U(P × Y) = U(P) × U(Y) for every Y, with no spatiality.

**H.** H(P × Y) ≤ H(P) × H(Y) holds for all locales, since the right side is closed, fitted and contains the diagonal. For the converse write G = H(P × Y) = C(g), with slices G\_s = C(g\_s).

1. {s} × T ≤ G exactly when T ≤ G\_s. Slices decrease as s increases.
2. Any open w containing {s} × T has fit T ≤ O(w\_s) ≤ O(w\_{s′}) for s′ ≥ s. So fit({s} × T) contains {s′} × fit T.
3. G is fitted, so fit(G\_s) ≤ G\_{s′} ≤ G\_s. Each slice is fitted, and slices agree on comparable indices, hence on components of P².
4. Diagonal slices contain Δ\_Y, so they contain H(Y). H(P) is the union of the components of P² that meet the diagonal. So g\_s ≤ d\_{H(Y)} on H(P).

**Transparency.** For finite P, W(P) = U(P) ≤ H(P). Hence:

```latex
\mathcal W(P\times Y)=\mathcal U(P)\times\mathcal W(Y),\qquad (\mathcal H\wedge\mathcal U)(P\times Y)=\mathcal U(P)\times(\mathcal H\wedge\mathcal U)(Y).
```

So P × Y satisfies W = H∧U iff Y does. W < U on the product iff W(Y) < U(Y), and W < H iff W(P) < H(P) or W(Y) < H(Y).

### A5. The T₁ space T

T is (0, ∞) ∪ (−∞, 0) ∪ {p₊, p₋, q}. The rays and the apexes p± are as in Y, and q is as described under Idea 2. Write u± for the open ray with its apex.

- **Closures.** cl N₊(F) = u₊ ∪ {q}. cl N₋(G) = u₋ ∪ {q}. A small interval at x > 0 has closure the closed interval plus p₊. A small interval at y < 0 has closure the closed interval plus p₋ and q.
- **U(T).** The pairs outside U are exactly (0, ∞) × u₋ and its transpose. In particular (p₊, y) is in U for y < 0, through q.
- **W(T) from below.** int U contains u₊² ∪ u₋². By A1, W contains K₀ = (u₊ ∪ {q})² ∪ (u₋ ∪ {q})².
- **W(T) from above.** The cover {T ∖ {p₊}, u₊} has w\_C disjoint from {p₊} × u₋. So w\_C ∧ (u₊⊠u₋) ≤ d\_U, and D vanishes on u₊⊠u₋. Hence W = K₀ and d\_W = u₊⊠u₋ ∨ u₋⊠u₊.
- **W is not fitted.** Each (x, q) with x > 0 is in K₀. Any open w containing K₀ therefore contains a set I\_x × ((−∞, 0) ∖ F\_x), with I\_x an interval at x and F\_x finite. On the open quadrant t₀ = (0, ∞) × (−∞, 0), the complement of w has finite vertical fibres, so w is dense there. The meet of these dense opens is a nonzero pointless sublocale of fit(W) inside O(d\_W).
- **H(T).** H is closed and contains that dense sublocale of t₀, so it contains cl t₀ = (u₊ ∪ {q}) × (u₋ ∪ {q}). With the transpose and K₀ this is T². Every real function on T is constant, so F(T) = T² as well.

## Sources

These are published references, separate from the packet's assertions. None was needed to certify the packet's claims; they bear on input S2 and on prior literature.

| Reference | Used for | How I saw it |
| --- | --- | --- |
| [I. Arrieta, Localic separation and the duality between closedness and fittedness, arXiv:2310.18522](https://arxiv.org/abs/2310.18522v1) | F-separated locales (fitted diagonal); the closed/fitted duality for the diagonal | Abstract page opened |
| [I. Arrieta, J. Picado, A. Pultr, A new diagonal separation and its relations with the Hausdorff property, Appl. Categ. Structures 30 (2022) 247–263](https://doi.org/10.1007/s10485-021-09655-9) | Origin of F-separatedness | Search listing only; publisher page not reachable |
| [M. M. Clementino, J. Picado, A. Pultr, The other closure and complete sublocales, Appl. Categ. Structures 26 (2018)](https://doi.org/10.1007/s10485-018-9516-4) | fit(−) as a closure operator on sublocales | Search listing only; publisher page not reachable |
| [J. Picado, A. Pultr, Axiom T\_D and the Simmons sublocale theorem, Comment. Math. Univ. Carolin. 60 (2019) 541–551](https://www.dml.cz/handle/10338.dmlcz/147971) | Input S2: scatteredness and sublocales induced by subspaces | Record page opened |
| [A. L. Suarez, Revisiting the relation between subspaces and sublocales, arXiv:2010.05284](https://arxiv.org/pdf/2010.05284) | Input S2: Simmons' theorem for scattered spaces; the Niefield–Rosenthal condition for all sublocales to be spatial | Paper opened |
| J. Picado, A. Pultr, Frames and Locales: Topology without Points, Birkhäuser 2012, Chapter III | Preimage of sublocales preserves meets; density; open and closed sublocales | Cited from memory, not opened |

The finite-poset checks were run with a short script of my own; I can attach it on request.