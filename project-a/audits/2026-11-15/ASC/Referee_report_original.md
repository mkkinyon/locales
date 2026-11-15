# Referee report — Project A, Question (A-SC)

Nov 14, 2026 · @Someone

## Verdict

**Correct.** The theorem holds as stated and the packet's proof is complete. I found no step that needs repair, only presentation issues and some available shortcuts.

I checked every numbered statement from first principles, including the parenthetical remarks and the lemmas that sound standard. The prompt asks for an error that survives the correctness of the spectral-retraction theorem. I looked for one at each place the prompt names and did not find one.

The proof rests on three facts about the construction and two about the input locales. All five hold.

| Fact | Where | Status |
| --- | --- | --- |
| A is a functor on all locale maps, so it preserves retracts | §2.1–2.2 | Correct |
| A of a coherent locale is coherent | §3.1 | Correct |
| A(U) = U² ∩ A(Y) for a sublocale U of Y | §5.2 | Correct, and true for every sublocale, not only open ones |
| A stably compact locale is a retract of a coherent one | §4.1 | Correct, in the right direction |
| A stably locally compact locale is open in a stably compact one | §5.1 | Correct |

Two checks against the statement itself also pass. For a regular locale X the relations force u₁ = u₂, so A(X) is the diagonal; for compact Hausdorff X this matches \[G\], since the specialization order is equality. For the Sierpiński locale, A(X) is the three-point sublocale of pairs x ≤ y.

## The five priority questions

All five get the answer yes. Each paragraph below gives the check that settles it.

### 1. Universal property and functoriality (§2.1)

Yes, A is a covariant functor on arbitrary locale maps. Since πᵢ ∘ (f × f) = f ∘ πᵢ, pulling vᵢ back along f × f gives (f\*v)ᵢ. The defining condition is a family of inequalities between inverse images, and any frame homomorphism preserves such a family.

The factorization through A(Y) is unique because A(Y) → Y² is monic. That gives identities and composites. I see no hidden problem in restricting f × f.

### 2. Ideal completion (§4.1)

Yes, σ and ι are frame homomorphisms with σι = 1, and X is the retract.

- **σ, joins.** σ is left adjoint to u ↦ ↓u, because ⋁I ≤ u exactly when I ⊆ ↓u. So it preserves all joins.
- **σ, meets.** The first equality in (4.2) is frame distributivity. The second holds because a ∧ b lies in I ∩ J. Top: σ(L) = 1.
- **ι, well defined.** {v : v ≪ u} contains 0, is a lower set, and is closed under binary joins.
- **ι, binary meets.** This is exactly stability, as (4.3) says.
- **ι, top.** ι(1) = {v : v ≪ 1} equals L exactly when 1 ≪ 1. This is the only use of compactness.
- **ι, joins.** The argument for (4.4) is right. The empty join is covered: ι(0) = {0}, and E always contains 0. Only continuity is used.
- **Direction.** σ = s\* with s: X → Y, and ι = r\* with r: Y → X. Then (r ∘ s)\* = s\* r\* = σι = 1, so r ∘ s = 1 on X.

### 3. Coherent base case (§3.1)

Yes, A(Y) is coherent. Ideal completion is left adjoint to the forgetful functor from frames to bounded distributive lattices. So it preserves coproducts, which gives (3.1), and coequalizers, which gives the quotient frame as Idl(D′).

Inequalities on arbitrary opens follow from the compact ones. Write u as a join of compact opens k. Each πᵢ\* preserves joins, so u₁ = ⋁k₁ ≤ ⋁k₂ = u₂.

### 4. Noncompact extension (§5)

Yes on all three points.

- **L⊤ is a compact stably continuous frame.** It is a frame: the one new case of distributivity is a family containing 1′, where both sides equal a. A directed set with join 1′ contains 1′, so every element is way below 1′. A directed set in L⊤ either contains 1′ or lies in L, which gives (5.1). Stability with target 1′ is trivial because u ∧ 1′ = u.
- **X is open in the lift.** The open sublocale given by the old top has frame ↓1, which is L.
- **(5.2) holds.** The proof uses only that j\* is surjective, so it holds for every sublocale. Openness matters only in Corollary 5.3.

### 5. Spatial conclusion (§2.3 and §6)

Yes to both parts. For the retract lemma: p\* is injective, a point of R separates p\*a from p\*b, and its composite with p separates a from b.

For the identification: let S be a spatial sublocale of any locale Z, with point set P. By (6.1) the congruence of S is “same trace on P”. That congruence is the intersection of the congruences of the points in P, which is the congruence of the join of those point sublocales. So S = \[P\] as sublocales, not just on points. For S = A(X), P = G by (1.3).

## Major issues

None. No step fails and no step leans on an unstated hypothesis.

These are the places I tried hardest to break, and why each holds.

- **Product of locales versus product of spaces.** The proof never treats X² as a space. Every step is a statement about frames or about maps into X².
- **Top preservation by ι.** It fails without compactness, and the packet uses it only for compact L.
- **Direction of the retraction.** X is the retract and the coherent locale is the ambient one, as needed for Lemma 2.3.
- **Directed sets through the new top.** A directed set in L⊤ that contains 1′ has 1′ as an upper element, so it cannot break a way-below relation between old elements.
- **Sublocale equality versus point sets.** §6 compares congruences, not point sets. The inference the packet warns against is not made.
- **Sublocales of spatial locales.** These need not be spatial. The proof only uses retracts and open sublocales, which are.

## Minor issues

None of these affects correctness. Each is a one-line fix.

| Where | Issue | Fix |
| --- | --- | --- |
| §1, statement | By §6, equation (1.4) is equivalent to “A(X) is spatial”, for every locale X. “In particular” undersells this. | State the equivalence in §1 and move the §6 lemma up front. |
| §2.3 | The diagram R → S → R displays the composite i ∘ p, an idempotent on R. The hypothesis is p ∘ i = 1 on S. | Draw S → R → S. |
| §4.1, (4.2) | The stated reason, closure of ideals under finite joins, is not what is used. | Cite frame distributivity for the first equality and lower sets for the second. |
| §4.1 | “σ preserves arbitrary joins” has no proof. Joins of ideals are not unions, so a reader may want one. | Note that σ is left adjoint to u ↦ ↓u. |
| §4.1 | “Each ι(u) is an ideal” has no proof. | Note 0 ≪ u and that v ≪ u, w ≪ u give v ∨ w ≪ u. |
| §5.1 | The proof never says why L⊤ is a frame. | Add the one distributivity case with 1′ in the family. |
| §5.2 | The hypothesis “open” is not used. | State the lemma for all sublocales. Use openness in 5.3 only. |
| §5.2 | g₁ and g₂ are not defined. | Say gᵢ = πᵢ ∘ g. |
| §5.3 | The open element is not named. | If a is the open of Y defining U, it is the image of a₁ ∧ a₂ in O(A(Y)). There a₁ ≤ a₂, so it is just a₁. |
| §6 | “The point map of a monomorphism is injective” is true but unused. | Delete it. |
| §6, (6.1) | u ∩ P is written for opens of a locale Z that need not be spatial. | Define it as the set of p in P with p\*(u) = 1. |
| §7, ref. 1 | The pointer is right: Vickers §1.2 states the retract fact. But his “stably locally compact” includes compactness. | See the terminology note below. |

## Presentation and misleading phrases

The one phrase likely to mislead is “stably locally compact”. The rest are small.

- **“Stably locally compact” means two things.** The packet uses it without compactness. Johnstone and Vickers use it with compactness: Vickers §1.2 asks way-below to respect all finite meets, including the empty one. Kawai notes the two names are synonyms in that tradition. So reference 1 proves the retract fact only for what the packet calls stably compact. That is all §4 needs, but §1 or §7 should say so.
- **A retraction cannot cover the noncompact case.** A retract of a compact locale is compact. One sentence saying this would explain why §5 exists.
- **K is reused.** In §3 it is the lattice of compact opens. In §4 it is the whole frame Idl(L), whose lattice of compact opens is L.
- **I is reused.** In §4 it names an ideal in (4.1)–(4.2) and an index set in (4.4).
- **“Bottom compactification” with frame L⊤.** The new top open corresponds to a new bottom point in the order (1.3). A sentence linking the two would help. “Lift” is the usual name.
- **“Already known in the coherent case” (§7).** It is unclear whether this means the literature or Project A. Reference 3 suggests the latter.
- **“Compact continuous two-arm diamond” (§7).** This example is not defined in the packet. The proof does not need it.
- **Status line.** It locates classical logic only in the spatiality of coherent locales. The case split on the new top in §5.1 is also classical. This matters only to a constructive reader.
- **f² and f × f.** §2.1 uses both for the same map.

## Simplifications

The proof admits a shorter form: three changes remove Lemma 5.1, shorten §4.1, and make §2 immediate.

### A(X) is the exponential by the Sierpiński locale

Opens of Z × S are pairs p ≤ q of opens of Z, where S is the Sierpiński locale. So maps Z × S → X are pairs of maps Z → X whose inverse images are ordered.

```latex
\mathrm{Loc}(Z,\mathcal A(X)) \;\cong\; \{(g_1,g_2) : g_1^*\le g_2^*\} \;\cong\; \mathrm{Loc}(Z\times\mathbb S,\,X)
```

Hence A(X) is X^S, the cotensor of X with the two-element chain. Lemma 2.1 is then immediate, and A preserves all limits. This also names the object: A(X) is the locale of specialization arrows in X.

### ι is left adjoint to σ

In any continuous frame the following holds for u in L and an ideal I.

```latex
\iota(u)\subseteq I \iff u\le\bigvee I
```

Left to right: u is the join of ι(u). Right to left: if v ≪ u ≤ ⋁I then v lies in I, because I is directed. So ι preserves all joins, which replaces the paragraph proving (4.4).

The chain ι ⊣ σ ⊣ ↓ also shows where each hypothesis enters. Continuity gives the adjunction and σι = 1. Stability gives binary meets. Compactness gives the top.

### The lift is not needed

For stably continuous L, compact or not, put W = ι(1) = {v : v ≪ 1}. W is an open of the coherent locale Y with frame Idl(L).

Then ι maps L into ↓W and preserves its top by definition. σ restricted to ↓W preserves top because ⋁W = 1. Both are frame homomorphisms and σι = 1.

So every stably locally compact X is a retract of an open sublocale W of a coherent locale. The compact case is W = Y. This removes Lemma 5.1 and its case analysis.

### The proof in four steps

1. A is a functor, and A(U) = U² ∩ A(Y) for every sublocale U of Y.
2. If Y is coherent then A(Y) is coherent, hence spatial.
3. X is a retract of an open sublocale W of a coherent Y. So A(X) is a retract of A(W), which is open in A(Y). Hence A(X) is spatial.
4. A spatial sublocale is the join of its points, and the points of A(X) are G.

## Generalizations and follow-up questions

The argument proves more than the packet claims, and it leaves one natural question open.

### Stronger statements the same proof gives

- **A preserves stable compactness.** A(X) is a retract of the coherent locale A(Y). A retract of a coherent locale is stably compact, which is the converse of Lemma 4.1. So A(X) is stably compact, not merely spatial.
- **A preserves stable local compactness.** A(X) is open in the stably compact A of the lift, and an open sublocale of a stably continuous frame is stably continuous. So A is an endofunctor of stably locally compact locales.
- **Iterates are spatial.** It follows that A(A(X)) and all higher iterates are spatial. These are the locales of commuting squares, cubes and so on in the specialization order.
- **Finite posets.** Replace the two-element chain by a finite poset P, with relations u\_p ≤ u\_q for p ≤ q in X^|P|. Functoriality, the coherent case and the sublocale formula go through unchanged. So the locale of monotone P-diagrams in X is spatial for stably locally compact X.

### A reframing of the general problem

Every frame L is a quotient of the coherent frame Idl(L), by I ↦ ⋁I. So every locale X is a sublocale of a coherent locale Y, and A(X) = X² ∩ A(Y) with A(Y) spatial.

The general question is therefore only about that intersection. The theorem says the intersection stays spatial when X sits in Y as a retract of an open.

### Open questions

1. **Does the theorem hold for all locally compact locales?** Without stability ι still preserves joins but not binary meets, so the retraction is gone. One data point: for the line with two origins, a direct calculation gives the diagonal, which is spatial.
2. **Is there a spatial X with A(X) not spatial?** For regular X, A(X) is the diagonal and so is a copy of X. A non-spatial regular X therefore has non-spatial A(X), but any spatial counterexample must be non-regular.
3. **Is the stronger statement constructive?** The retraction, the coherent case and the open-sublocale route above avoid points entirely. I expect “A preserves stable local compactness” to hold constructively, with classical logic used only for spatiality. I did not audit this line by line.
4. **How does A(X) relate to the patch?** For stably compact X the graph G is the closed order of the associated compact ordered space. Is A(X) recoverable from that closed sublocale of the patch squared, and does A commute with de Groot duality up to reversing the order?

### The regular case, for the record

If v is well inside u, then v\* ∨ u = 1. In A(X) the relation v\*₁ ≤ v\*₂ gives v₂ ∧ v\*₁ = 0.

```latex
v_2 \;=\; v_2\wedge(v^*_1\vee u_1) \;=\; (v_2\wedge v^*_1)\vee(v_2\wedge u_1) \;\le\; u_1
```

Taking the join over such v gives u₂ ≤ u₁. So A(X) is the equalizer of the two projections, which is the diagonal.

## Scope and limits of this audit

This was a blind hand check of the two files in the archive, under classical logic.

- **Independence.** I read only the prompt and the packet. I did not open the Project A repository or reference 3.
- **Method.** I re-derived every lemma by hand. No proof assistant was used. Finite test cases say nothing here, because every finite locale is coherent.
- **Reference 1.** Confirmed from the Birmingham portal copy: the paper is TCS 316 (2004), 259–296, and §1.2 states the retract fact. The author-hosted URL in §7 was not reachable from this session.
- **Reference 2.** The slides were not reachable, so “slide 8” is unconfirmed. Kawai’s companion paper states the same fact in its Section 3 and cites Johnstone for it.
- **Not checked.** §7 reports earlier tests on total orders, their products and the diamond. I did not check them, and the proof does not use them.
- **My own additions.** The simplifications and stronger statements above were checked by hand to the same standard as the packet. Items marked as expectations or questions were not. None has had a second reader.

### Sources

- [Vickers, Entailment systems for stably locally compact locales (preprint of TCS 316)](https://research.birmingham.ac.uk/files/2919664/StabCompEnt.pdf)
- [Kawai, Presenting de Groot duality of stably compact spaces (arXiv 1812.06480)](https://arxiv.org/pdf/1812.06480)
