# Addendum to referee report — Project A (LC-A): further mathematical comments

Nov 15, 2026 · @Someone

This addendum records four comments made after the referee report was finished. None changes the verdict: the packet's theorem (5.5) is correct. Section and equation numbers refer to the packet of 15 November 2026.

## 1. The question is the totally unordered axiom

A(X) = Δ\_X holds exactly when X is *totally unordered*, written (T\_U). That axiom requires any two locale maps f ≤ g into X to be equal. It goes back to Isbell and appears in Johnstone's *Stone Spaces*, III.1.5 ([Bannister, Def. 1.2](https://arxiv.org/pdf/2411.05967); [Arrieta, §2.3](https://arxiv.org/pdf/2310.18522)).

The equivalence is immediate. A(X) is the universal pair g₁ ≤ g₂, and Δ\_X is the equalizer of the two projections.

What follows from this identification:

- **Restatement of (LC-A) for T1 spaces.** For T1 sober X, \[G\_≤\] = Δ\_X. So (LC-A) asks whether local compactness implies (T\_U). Theorem (5.5) says the packet's X is compact, locally compact, sober and T1, but not (T\_U).
- **Lemma 4.1 overlaps a published result.** Arrieta's axiom (pt-fit) asks every point sublocale to be fitted, and his Proposition 3.10 proves (T\_U) implies (pt-fit) ([source](https://arxiv.org/pdf/2310.18522)). The packet's X fails (pt-fit) at p. Lemma 4.1 says slightly more, since it identifies the whole fiber.
- **The fiber has a known shape.** Arrieta's Remark 3.9(ii) adjoins a new top to a pointless locale to get (T\_1) without (pt-fit). By the formula in priority check 5 of the report, the frame of fit(\[p\]) is the frame of E with the new top X adjoined. The packet's X realizes that pattern inside a compact, locally compact space. This last observation is mine.
- **A Hausdorff non-(T\_U) space is already known.** Johnstone's Example III.1.5 refines the real line by the opens U ∪ (V ∩ ℚ), as recalled in Arrieta's Remark 3.3. It is not locally compact: locally compact Hausdorff implies regular, and regular implies (T\_U). The new content of the packet is therefore local compactness.
- **Sufficient conditions.** Fitness implies a fitted diagonal, and a fitted diagonal implies (T\_U) (Theorems 2.3 and 2.4 as recalled by Arrieta). So the diagonal of the packet's X is not fitted.

**Priority is unchecked.** I did not search for an existing locally compact T1 space that fails (T\_U). Johnstone III.1, Arrieta's thesis and the Picado–Pultr monograph on point-free separation are the places to look before any priority claim. The last title is from memory.

**A sharper next question.** For locally compact sober T1 spaces, is (pt-fit) equivalent to (T\_U)? In the §2 and §7 family it is. Points of K are fitted because K is regular, so (pt-fit) reduces to fit(\[p\]) = \[p\], which is E = 0.

## 2. The two projections are asymmetric

Fibers of the second projection ρ₂ are closures of points and are always spatial. Nonspatiality of A(X) can enter only through ρ₁, the fitted side.

The computation mirrors Lemma 4.1. A map (z, q!) factors through A(X) when z∗u ≤ (q!)∗u for all u. For q ∈ u this is automatic. For q ∉ u it says z∗u = 0, which is factoring through the closed sublocale c(u).

A meet of closed sublocales is closed, so the fiber is c(w), where w is the union of all opens missing q. That is the closure of \[q\]:

```latex
\mathcal A(X)\times_{X,\rho_2}[q]\;\cong\;\bigwedge_{q\notin u}\mathfrak c(u)\;=\;\overline{[q]},
\qquad
\mathcal A(X)\times_{X,\rho_1}[p]\;\cong\;\bigwedge_{p\in u}\mathfrak o(u)\;=\;\operatorname{fit}([p])
```

A closed sublocale of a spatial locale is spatial, so the left-hand fiber never causes trouble. This is the localic form of the fact that closures of points are harmless while saturations of points need not be. It also explains why the packet's obstruction sits over the first coordinate.

## 3. A shorter route to Lemma 3.3

A stably locally compact sober T1 space is Hausdorff. The packet's X is T1 and not Hausdorff, since every U\_F meets every nonempty open of K. So X is not stably locally compact, with no computation.

Proof of the general fact, in three steps:

1. Let Q be compact and z ∉ Q. By T1 and local compactness, the compact neighborhoods N of z intersect in {z}.
2. By coherence, the sets Q ∩ N are compact and form a filtered family. Their intersection is empty. Sobriety gives well-filteredness, so some Q ∩ N is already empty.
3. Hence compact sets are closed. For x ≠ y, take a compact neighborhood Q of x inside X ∖ {y}. The interior of Q and the complement of Q separate x from y.

The argument does not use compactness of X, so it is independent of the convention issue noted under Lemma 3.3 in the report.

One consequence for the project: among T1 spaces, (A-SC) covers only Hausdorff ones, where (T\_U) already follows from regularity. For T1 spaces, (LC-A) is therefore entirely a question about non-Hausdorff spaces.

## 4. The construction cannot be first-countable

No space of the §2 or §7 form that is first-countable at p can be a counterexample. The argument has three steps:

1. If the cofinite filter at p has a countable base K ∖ F\_n, then each K ∖ {x} contains some K ∖ F\_n. So x lies in some F\_n, and K is countable.
2. A countable locally compact Hausdorff space is scattered. A nonempty perfect subset would be a countable locally compact Hausdorff space without isolated points, contradicting the Baire category theorem.
3. For scattered K, A(X) = Δ\_X by the claim in the report's section "A sharper form of §7".

Step 3 rests on that claim, which is my own sketch and has not been independently reviewed.

**Open question.** Is there a second-countable, or even first-countable, locally compact sober space with A(X) nonspatial? Equivalently in the T1 case: a second-countable locally compact sober T1 space that fails (T\_U). I do not know the answer and did not search for it. Adjoining a single point with cofinite neighborhoods cannot produce one. A positive answer under second countability also seems possible, because countable meets of open sublocales are often spatial.

## Status of each comment

| Comment | Basis | Confidence |
| --- | --- | --- |
| 1. Identification with (T\_U) | Definition checked in two papers; equivalence is a one-line argument | High |
| 1. Lemma 4.1 versus Proposition 3.10 | Read from a summary of Arrieta's paper, not line by line | Statement confirmed; proof not compared |
| 1. Johnstone's example | Cited through Arrieta; I did not open *Stone Spaces* | Secondhand |
| 2. Fibers of ρ₂ | My own derivation, by hand | High; same method as Lemma 4.1 |
| 3. Stably locally compact T1 implies Hausdorff | My own proof, by hand | High; uses well-filteredness of sober spaces |
| 4. No first-countable example | My own argument | Depends on the unreviewed scattered claim |

Nothing here was machine-checked. The literature check was limited to the two papers below, and it was not a priority search.

## Sources

- [I. Arrieta, *Localic separation and the duality between closedness and fittedness*, arXiv:2310.18522](https://arxiv.org/pdf/2310.18522). Used for (T\_U), (pt-fit), Proposition 3.10, Remarks 3.3 and 3.9, and Theorems 2.3 and 2.4.
- [N. Bannister, *Locales as Spaces in Outer Models*, arXiv:2411.05967](https://arxiv.org/pdf/2411.05967). Used for Definition 1.2 of (T\_U) and its reference to Johnstone, *Stone Spaces*, III.1.5.
- [Referee report — Project A (LC-A) blind external audit](https://claude.ai/artifact/7eKWMsZnQCUV2B1b4xSmCC). The report this addendum extends.
