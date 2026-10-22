# Focused verification of Claude's three new coherent/compact claims (21 October 2026)

Source: user-supplied Claude Opus 5.5 blind referee report, specifically §§2.2, 2.3, 2.6, 3.5, 9.1, 9.2. Fresh mathematical scrutiny in conversation; use attribution and do not assert publication priority.

## V1. Coherent fitted mirror identity: VERIFIED (classical BPI)

For coherent X, fit(I)=D∘D as genuine sublocales. Put B=K(O(Y)). For a filter F of compact opens, intersection O(f) is presented by Idl(B/θ_F), where a θ_F b iff a∧f=b∧f for some f∈F. Universal property checked: any frame quotient sending F to top factors through the quotient, because its images of a,b agree whenever a θ_F b. This quotient is coherent/spatial under BPI; points are those belonging to all f∈F. Compactness of 1 reduces fit(I) and D to such filtered compact-open intersections. Pullbacks to coherent X³ preserve compact-open presentation; D12∩D23 is coherent and spatial with ordinary points composing D_pt. Image of a spatial subspace A under f is the spatial sublocale S_(f(A)), via kernel of open pullback. Spectral patch compactness yields ↑I_pt=D_pt∘D_pt. Both sides are S_(↑I_pt). Thus equality holds. Records V=fit(I)=D² and Hochster point-dual counterpart of U=c(D)=I².

## V2. Compact U=I²: VERIFIED conditional on standard proper projection theorem

For compact X, projection π:X³=(X₁×X₃)×X₂→X² is proper; its right adjoint π_* preserves directed joins (Vermeulen, Proper Maps of Locales, JPAA 92 (1994)). Composable I pair source is C(e), e=I12 complement joined I23 complement. π-image of this closed sublocale is C(π_*e). Express e as directed join of finite joins of disjoint rectangle generators. Finite rectangle lemma for coproduct computes π_* of each finite piece as join of base rectangles s⊠v where s∧t=0, v∧u=0 and t∨u=1; hence s*∨v*=1. So π_*e≤d_U, giving U⊆I². Universal I²⊆U gives equality. Consequently for all compact locales I=U iff I internally transitive. This argument is point-free and does not assume coherent/spatial.

## V3. Compact locally compact sober T1 noncoherent counterexample: VERIFIED strict inequality

Space X: two disjoint infinite discrete sets N1,N2 and α,β,γ, with neighborhoods α+cofinite N1, β+cofinite (N1∪N2), γ+cofinite N2. Is compact and locally compact (basic neighborhoods compact); T1; sober (irreducible closed subsets are singleton); not coherent because two compact opens α+N1, β+N1∪N2 intersect in noncompact N1. Every α-neighborhood and γ-neighborhood have closures containing β, so (α,γ)∈U_pt.

For D nucleus ν, define p(q)=∨_{δ*w=1}(w→q), so p²(0)≤ν(0). Covers {X\{b},{b}} and analogous singleton separating covers imply p(0) contains (α,b), (a,γ), (a,b) for a∈N1,b∈N2. Let w0 be square-union for cover {X\{γ},X\{α}}. Any rectangular neighborhood N of (α,γ) intersects w0 in N\{(α,γ)}, all contained in p(0). Thus (α,γ)∈(w0→p(0))⊆p²(0)⊆ν(0), so (α,γ)∉c(D)_pt. Hence c(D)⊊U as localic sublocales, even for compact locally compact sober T1 X. No coherence. Claude's extra assertion c(D)=I not independently verified here and must remain separate.

## Corrective items and implications

- Previous note labeling coherent fit(I)=D² OPEN should be superseded with this verification.
- The false proof inference that closed image of spatial source has exactly its point-image needs replacement by the verified spatial-subspace image lemma plus closedness of the concrete point-image.
- Separate compact U=I² from coherent c(D)=U; the latter fails even for compact locally compact sober T1 locales.
- New V=fit(I)=D² merits comparison under Hochster duality and coproducts; avoid assuming it is a functorial sublocale duality outside coherent spectral setting.
- Standard proper-projection theorem and BPI should be cited explicitly. Literary novelty and claim c(D)=I in counterexample remain unverified.
