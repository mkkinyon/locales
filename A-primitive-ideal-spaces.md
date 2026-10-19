> **DECISIVE UPDATE (18 October 2026):** The **unrestricted** continuous-frame implication is **false**. See [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md): adjoining two nonclosed isolated tags to disjoint nonnormally separable closed subsets of a locally compact Hausdorff space (explicitly the deleted Tychonoff plank) gives a locally compact sober space with **I=U⊊F**, even for a far pair of *compact opens*. This supersedes any unresolved-status or conjectural statement below. Positive conclusions under compactness, sigma-compactness/kω, paracompactness, or quotient hypotheses remain valid.

> **Subsequent progress (18 October 2026):** [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md) proves that for every kω-space, a transitive inseparability relation is already functional equivalence, since the quotient is normal Hausdorff. Hence the unrestricted continuous-frame implication is now established for **σ-compact locally compact sober spaces**, without a closed- or open-quotient assumption. This does not settle the general non-σ-compact case. See [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md) for the noncompact closed-buffer lemma and a counterexample to arbitrary one-step interpolation. For C*-algebra spectra, apply only after independently verifying the requisite σ-compactness/local-compactness hypotheses.

# A — Primitive ideal spaces: can they violate I=U ⇒ U=F?

**Research investigation, 18 October 2026.** This note studies established operator-algebra constructions. **Result:** no verified counterexample to the implication was found. There is, however, an explicit **nonunital positive example** with a non-open complete-regularization map and a non-locally-compact Glimm space; and a strong **closed-saturation criterion** for the positive implication. We record necessary conditions that narrow a possible operator-algebra counterexample. These operator-algebra results are from the cited sources, not claimed as ours.

## Terminology

For a C*-algebra A set X=Prim(A) with hull-kernel topology. The relations are:

- P∼Q: every neighborhood of P meets every neighborhood of Q (our **I**).
- P≈Q: every continuous bounded real function takes the same values on P,Q (our **F**; bounded and all real functions give the same relation by arctan).
- P U Q: no neighborhoods of P,Q have disjoint closures (our **U**, less studied in the cited C*-papers).

The **connecting order** Orc(A) is the maximal graph diameter of ∼-components, with singleton diameter declared to be 1. Thus

    Orc(A)=1  iff  ∼ is an equivalence relation.

The quotient by ≈, equipped with the completely regular topology, is Glimm(A). Under σ-unitality the quotient and completely regular topologies on Glimm(A) coincide. Our implication I=U⇒U=F, in this language, would be guaranteed by

    Orc(A)=1  ⇒  ∼ = ≈,

because E⊆U⊆F always. Conversely, **I=U is stricter than Orc(A)=1**: transitivity alone does not guarantee the ability to separate distinct components by neighborhoods with disjoint closures. Thus even an Orc=1, E≠F example would need this additional check before it answered our question.

## 1. What is known when Prim(A) is compact

For a unital A, Prim(A) is compact. Somerset, *The central Haagerup tensor product of a C*-algebra*, J. Operator Theory **37** (1997), 113–122, p. 120, recalls four equivalences for unital C*-algebras:

1. Orc(A)=1;
2. ∼ is an equivalence relation;
3. ∼=≈;
4. every Glimm ideal is 2-primal.

This agrees with our previously proved **compact-space theorem**. It eliminates **all unital algebras** as candidate counterexamples, even without assuming I=U: Orc=1 by itself suffices.

Source: [Somerset PDF](https://citeseerx.ist.psu.edu/document?doi=d33bcdb0b0f2bad12e433c3f3aae0061f2f29782&repid=rep1&type=pdf), p. 120.

## 2. A nonunital POSITIVE example: the motion group G3

Let GN=R^N⋊SO(N) and A_N=C*(GN).

Archbold–Kaniuth–Somerset, *Norms of inner derivations for multiplier algebras of C*-algebras and group C*-algebras, II*, *Advances in Mathematics* **280** (2015), 225–255, [arXiv:1504.07030](https://arxiv.org/pdf/1504.07030), §3, prove:

    Orc(A_N)=⌊N/2⌋   (Theorem 3.3(i)),

and identify its Glimm classes (Theorem 3.3(ii)):

- each P_{t,σ} for t>0 is a singleton Glimm class;
- all irreducible representations of SO(N), regarded as a closed subset of Prim(A_N), belong to **one** Glimm class.

They also prove in Theorem 3.3(iii) that the Glimm map φ_A is closed, and observe (immediately after the theorem) that Glimm(A_N) has no compact neighborhood at the distinguished ideal I0; hence Glimm(A_N) is **not locally compact**.

For N=3, floor(3/2)=1. Hence every two members of the exceptional Glimm class are directly inseparable; the other Glimm classes are singletons. Therefore

    I(Prim(A_3)) = F(Prim(A_3)),

and, from I⊆U⊆F,

    I=U=F.

Moreover the quotient map φ_A **cannot be open**: if it were, the quotient by an open inseparability equivalence of a locally compact space would be locally compact Hausdorff (our earlier open-quotient theorem), contradicting the authors' explicit observation that Glimm(A_3) is not locally compact. Thus this provides a noncompact, nonunital, second-countable primitive-spectrum example **showing the open-quotient hypothesis is not necessary**.

It is a particularly useful test case for our continuous-frame question, provided the spectral space is locally compact sober. For separable C*-algebras prime ideals are primitive, which gives sobriety of the primitive spectrum. The C*-algebra spectrum is locally compact in the neighborhood-basis-of-compact-sets sense used by the authors (see Lemma 4.2 on p. 9).

Also note Theorem 7.1 in the same source remarks that A_2 is the only quasi-standard member of this motion group family. Thus A_3 is an **Orc=1, non-quasi-standard** algebra for which I=U=F. It exhibits why **quasi-standard** is strictly stronger than just equality of the three relations.

The case N≥4 has Orc≥2, so its inseparability graph is not transitive. Such GN cannot satisfy I=U (our elementary transitivity lemma), and hence is not a counterexample.

## 3. A robust sufficient condition without compactness or open quotient

Archbold–Kaniuth–Somerset, [arXiv:1504.07030](https://arxiv.org/pdf/1504.07030), Proposition 4.3, is relevant. For σ-unital A, write C^1 for the union of all ∼-neighbors of points of a set C, and C^∞ for its entire ∼-component saturation. They establish:

    [C^∞ is closed for every closed C⊆Prim(A)]
        ⇔ [φ_A is closed AND every Glimm class is ∼-connected].

If Orc(A)=1, a ∼-component is already one ∼-class, so this gives:

**Corollary (proved).** Suppose A is σ-unital, Orc(A)=1, and **the ∼-saturation of every closed subset of Prim(A) is closed**. Then ∼=≈. Consequently I=U=F, **with no U hypothesis at all**.

Their proof uses a general separation lemma for **locally compact spaces** and **Lindelöf subsets** (Lemma 4.2), and then shows the quotient by component-equivalence is normal T1.

### Purely topological formulation

Let X be a locally compact, σ-compact topological space and suppose E=cl(Δ) is an equivalence relation. If E[C] is closed for every closed C⊆X (equivalently, q:X→X/E is a **closed quotient map**), then E=F as ordinary point relations.

**Proof sketch.** The quotient Q=X/E is T1 because E-classes are closed. Its quotient map q is closed by hypothesis. Given disjoint closed subsets B,C⊆Q, their inverse images B',C' are disjoint closed saturated subsets of X. They are Lindelöf since X is σ-compact and closed subsets of σ-compact spaces are σ-compact. Every E-neighbor of B' lies in B' (and similarly C'), so the locally compact Lindelöf separation lemma yields disjoint open neighborhoods U,V of B',C'. Since q is closed, every open neighborhood of a whole q-fiber contains a **saturated** open neighborhood of that fiber; refine U,V to disjoint saturated opens. Thus Q is normal and T1, hence completely regular. Its real functions distinguish inequivalent points and pull back to X. □

Reference for the lemma and proof: Archbold–Kaniuth–Somerset (2015), Lemma 4.2 and Proposition 4.3, pp. 9–10.

This is a more flexible positive theorem than the earlier **open quotient** result. It uses a **closed quotient** condition, which is frequently verifiable in ideal-space examples, even when quotient openness fails. In particular, A_3 above has a closed Glimm map by Theorem 3.3(iii).

## 4. What nonunital examples could still work?

The same 2015 paper explicitly warns (p. 9) that **in the noncompact case, Glimm classes can contain multiple ∼-components even when Orc(A)<∞**. This prevents extending the unital equivalence on purely formal grounds. However, the statement does **not** assert that this phenomenon occurs with **Orc(A)=1**, let alone that I=U.

A candidate counterexample must establish all three facts:

1. Orc(A)=1 (inseparability is transitive).
2. There is a Glimm class containing at least **two** inseparability classes, so ∼≠≈.
3. Every ∼-separable pair has open neighborhoods with **disjoint closures**, so I=U.

The third is absent from most operator-algebra papers and **cannot be inferred from Orc=1**.

Two further constraints emerge:

- By Proposition 4.3, such an A (if σ-unital) **must** have a closed subset C with **nonclosed** ∼-saturation. This is a concrete topological failure condition.
- Archbold–Somerset, *Spectral synthesis in the multiplier algebra of a C0(X)-algebra*, [arXiv:1210.3251](https://arxiv.org/pdf/1210.3251), Theorem 6.2, says that for an Orc-finite C*-algebra a ∼-component T either is an entire Glimm class on which the center Z(A) does not vanish, or else it is linked by inseparability to a primitive ideal **in the multiplier-algebra remainder** Prim(M(A))\Prim(A). Accordingly, **any proposed splitting of a Glimm class** necessarily occurs over a Glimm ideal containing Z(A), and the missing links are associated with points “at infinity” in the multiplier algebra.

This suggests searching in the nonunital/zero-center regime, and interpreting saturation failures through such boundary points rather than through the graph topology alone.

## 5. Discarded tempting examples

- GN for N≥4 (Orc≥2): **cannot satisfy I=U**, since I is nontransitive.
- GN for N=3 (Orc=1): **has I=U=F**, not a counterexample.
- Unital C*-algebras: compact result rules them out categorically.
- Archbold–Somerset, [arXiv:1210.3251](https://arxiv.org/pdf/1210.3251), Example 6.4(ii): constructed with **Orc(A)=∞**, not 1, so fails I=U; this is not the required example.
- Quasi-standard C*-algebras: the very definition is that inseparability is an **open equivalence**, which forces I=U=F by the open-quotient theorem.

## 6. Open outcome and next steps

**No counterexample has been verified.** There remains a genuine, sharply delimited question: can the multiplier-remainder alternative of Archbold–Somerset Theorem 6.2 occur for two different Orc=1 components inside one Glimm class, **while** every two components have disjoint-closure neighborhoods?

Possible next tests:
- Find a concrete **σ-unital, Orc=1, ∼≠≈** C*-algebra, if any; then calculate the Urysohn relation separately. This itself is a nontrivial question.
- Examine nonunital AF examples and Bratteli diagrams (Lazar–Somerset, [arXiv:1509.06140](https://arxiv.org/abs/1509.06140)), in which Glimm spaces are flexible. Their theorem by itself is **not** an Orc=1 construction.
- Investigate whether equality I=U implies closed saturation C↦C^1 for *locally compact sober spaces*. If yes, Proposition 4.3 would complete the proof under σ-compactness, and a separate argument might eliminate σ-compactness.
- Distinguish the **underlying pointwise** relations from full equality of **closed localic** sublocales. For locally compact sober spaces the representation and localic-product comparison ensure these agree.

## Primary sources

1. R. J. Archbold, E. Kaniuth and D. W. B. Somerset, *Norms of inner derivations for multiplier algebras of C*-algebras and group C*-algebras, II*, *Advances in Mathematics* **280** (2015), 225–255, [arXiv:1504.07030](https://arxiv.org/pdf/1504.07030): Theorem 3.3, Proposition 4.3, Lemma 4.2, Theorem 7.1.
2. R. J. Archbold and D. W. B. Somerset, *Spectral synthesis in the multiplier algebra of a C0(X)-algebra*, *Quarterly Journal of Mathematics* **65** (2014), 1–24, [arXiv:1210.3251](https://arxiv.org/pdf/1210.3251): Theorem 6.2, Example 6.4.
3. D. W. B. Somerset, *The central Haagerup tensor product of a C*-algebra*, *Journal of Operator Theory* **37** (1997), 113–122, p. 120, [preprint/PDF](https://citeseerx.ist.psu.edu/document?doi=d33bcdb0b0f2bad12e433c3f3aae0061f2f29782&repid=rep1&type=pdf).
4. R. J. Archbold and D. W. B. Somerset, *Quasi-standard C*-algebras*, *Mathematical Proceedings of the Cambridge Philosophical Society* **107** (1990), 349–360.
5. A. J. Lazar and D. W. B. Somerset, *Glimm spaces of separable C*-algebras*, *Journal of Functional Analysis* **270** (2016), 4466–4477, [arXiv:1509.06140](https://arxiv.org/abs/1509.06140).
