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
