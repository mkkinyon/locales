# A — Cornish/minimal-prime/annihilator literature ledger (21 October 2026)

**Status: exploratory identifications and eliminations; not an exhaustive literature review.** See [A-coherent-conormality.md](A-coherent-conormality.md), [A-equality-characterizations.md](A-equality-characterizations.md), [A-fitted-diagonal.md](A-fitted-diagonal.md).

## Firm coherent correspondence

For coherent L, I=U iff K(L) is conormal, equivalently Cornish-normal as a bounded distributive lattice (disjoint k,l admit annihilating compact witnesses covering 1). Cornish's unique-minimal-prime description is classical and not new. Main source: W. H. Cornish, *Normal lattices*, J. Austral. Math. Soc. **14** (1972), 200–215, DOI:10.1017/S1446788700010041.

## Direct whole-frame annihilator axioms are too strong

For any frame L, Ann_L(a)=↓a*. Hence Cornish-normality of the underlying bounded distributive lattice is equivalent to:
a∧b=0 ⇒ a*∨b*=1, equivalently the Stone identity a*∨a**=1.
This is strictly stronger than I=U: regular non-extremally-disconnected examples such as O(Cantor space) satisfy I=U but not Stone.

Cornish, *Annulets and α-ideals in a distributive lattice*, J. Austral. Math. Soc. **15** (1973): annulets Ann_D(a) form a sublattice of Id(D) under the ordinary ideal join precisely under Cornish normality. For D=L a complete frame, this again collapses to Stone. His α-ideals on L are ideals J closed under x↦x**; 'every principal ideal is an α-ideal' collapses to Booleanity.

The canonical set D_L={a:a≪1} is indeed a (possibly unbounded) distributive sublattice: meet closure follows by downward closure. But in compact frames D_L=L, so Cornish normality on D_L again fails for O(Cantor space) despite I=U. Do not claim D_L lacks meet closure; that was a transient mistake corrected in the conversation. Arbitrary generating sublattice tests are presentation-dependent (Cantor frame: clopens versus all opens).

## Minimal-prime terminology

- 'pmin' and 'mp' terminology gives the coherent minimal-prime connection; the full arbitrary-frame identification **fails** in at least one direction.
- For any sober T1 space, prime opens are complements of points, pairwise incomparable, hence O(X) is mp. The three-origin line example (a sees positive side, c negative side, b both) is T1, locally Hausdorff/sober, while a I b, b I c, a not I c and a U c. Thus mp does not imply I=U even for continuous spatial frames. The converse I=U⇒mp is **not settled**; deprioritized.
- Cozero-based PF-frames are not the same as the PF-quantale purity constructions; test exact definitions before claiming equivalences.
- Further optional reading: Bhattacharjee–Madinya–McGovern, *Algebraic Frames and Minimal Prime Elements*, Order (2026), DOI:10.1007/s11083-026-09734-3. This was identified as relevant but **not read deeply or matched to I=U**.

## Diagonal and fittedness direction (distinct track)

Existing [A-fitted-diagonal.md](A-fitted-diagonal.md) defines D=fit(Δ), and proves Δ⊆D⊆U with D and I generally incomparable. Its pointwise relation is the closure-meeting graph. Arrieta–Picado–Pultr (2022), *A New Diagonal Separation and Its Relations With the Hausdorff Property*, and Arrieta (2024), *Localic Separation and the Duality Between Closedness and Fittedness*, are **most directly relevant to D=U and D=Δ**, not automatically to I=U. Do not confuse project relation F with fitted-diagonal property (Fsep).

## Identification status / filter

**No verified conventional name for arbitrary-frame I=U.** Candidate must agree with conormality in coherent case, admit O(Cantor space), reject finite nonconormal Alexandrov witnesses and three-origin example, and have appropriate product/coproduct behavior. Consider literature comparisons provisional until primary theorem statements and counterexamples are audited. Avoid renaming the cp-ideal condition without mathematical benefit.

## Bhattacharjee–Madinya–McGovern (2026): CAB and subcompact elements

**Primary source examined (16-page user-supplied PDF):** P. Bhattacharjee, A. Madinya, W. Wm. McGovern, *Algebraic Frames and Minimal Prime Elements*, *Order* **43** (2026), article 20, DOI:10.1007/s11083-026-09734-3.

Their **compact absoluteness property (CAB)** for a prime element p in an algebraic frame L is

    p = ⋁ {c* : c∈K(L), c≰p}.

Lemma 2.3 gives its equivalent compact test: for each c∈K(L), exactly one of c≤p and c*≤p holds. Lemma 2.5 shows Cab(L)⊆Min(L). The classical Lemma on Ultrafilters (Theorem 2.1) establishes **Cab(L)=Min(L) for every algebraic frame satisfying FIP**, hence for every coherent frame. This property **does not imply I=U**, since finite coherent nonconormal examples (e.g. our five-point Alexandrov Q) satisfy CAB for all minimal primes but fail I=U. Do not conflate CAB with Cornish conormality.

The authors define the canonical lattice **s(L)** of finite meets of compact elements (Definition 2.7). It is a distributive sublattice of an algebraic frame even without FIP; s(L)=K(L) iff FIP holds. **Theorem 2.15** characterizes CAB minimal primes by maximality among subcompactly generated filters and equivalent pseudocomplement expressions. **Proposition 3.5** equates Cab(L)=Min(L) with hull-kernel topology finer than inverse topology on Min(L); **Corollary 3.8** then yields zero-dimensional Hausdorff Min(L). **Theorem 3.11** characterizes compactness of the inverse minimal-prime space by equality of maximal completely prime and maximal subcompactly generated filters. Sections 4.13, 4.17, 4.19 construct instructive poset examples distinguishing these conditions. Example 4.19 has an apparent heading/text mismatch: the construction yields Cab(L)=∅ rather than Cab(L)=Min(L).

**Relevance:** CAB is eliminated as an exact criterion; s(L) and subcompact filters are worth retaining as potential tools if algebraic non-FIP frames become relevant. No claim of independent publication-level audit of all the authors' proofs.

## Literature-search stopping decision (21 October 2026)

The systematic comparison of Cornish conormality, mp/pmin, PF variants, Stone/Baer annihilator axioms, annulets/α-ideals, CAB, and diagonal/fittedness terminology has found **no established named condition verified to coincide with I=U on all frames**. Together with the working closure results and explicit counterexamples, this is **substantial corroborating evidence that the precise arbitrary-frame condition has not been studied in the accessible literature we examined**. It is **not** a priority or novelty proof, and does not imply exhaustive coverage of obscure or unindexed sources. Revisit only if a new structural connection, reference, or mathematical result gives a concrete reason. The parallel D=U question belongs with fitted-diagonal literature; see A-fitted-diagonal.md.
