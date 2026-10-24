# Project A — Unprioritized relational-hierarchy inventory (24 October 2026)

Purpose: collect genuinely deferred equality/inclusion/composition questions for Δ, I, D, U, V, F and the derived relations M=I∧D, J=I∨D, K=U∧V, N=U∨V, and H=least simultaneously closed-and-fitted hull of Δ. **UNORDERED; DO NOT INFER PRIORITIES.** The K and N symbols here are purely local placeholders; do not adopt them as permanent notation before discussion. Status below uses most recently superseding research notes; some working claims remain unaudited. Full source overview: A-research-status-index.md.

## Two prominent questions ALREADY answered negatively

(0a) **J=U∧V? NOT UNIVERSAL.** In coherent locales, U=cl(D) and V=fit(I), so U∧V=cl(J)∧fit(J)=T(J). The four-point zigzag 0<1>2<3 has J≠T(J): (0,3) belongs to both U,V but not J. The five-point alternating zigzag 0<1>2<3>4 is a second counterexample (J has 19 ordinary pairs, U∧V adds (0,3),(3,0),(1,4),(4,1)). **OPEN:** characterize equality, and determine in arbitrary locales whether T(J)=U∧V or strict T(J)⊊U∧V is possible.

(0b) **U∨V=F? NOT UNIVERSAL.** Six-point connected alternating zigzag 0<5>1<4>2<3 has F=H=P² but (0,3),(3,0) belong to neither U nor V; finite Alexandrov sublocales are spatial, so N=U∨V omits these pairs. **OPEN:** characterize N=F or N=H.

## Unprioritized inventory

- **M=Δ?** Not universal (diamond poset gives M⊋Δ). Characterize exact equality in arbitrary locales; assess whether M's closure/fitting identities cl(M)=I, fit(M)=D constrain it via new separation axioms.

- **I=D?** No general characterization; relate to simultaneous closedness/fittedness, and determine when equality forces collapses among J,U,V,F. Coherent special cases and finite order duality should be used as controls.

- **J=U, J=V, J=H, and J=U∧V?** Counterexamples exist to these as general identities; seek interesting equality conditions in coherent, normal, conormal, continuous, compact or other classes.

- **K=U∧V vs T(J)=cl(D)∧V.** Universal T(J)≤U∧V; coherent equality proved. Strictness for some arbitrary noncoherent locale not determined. Characterize when K is closed or fitted or itself a relation of known type.

- **N=U∨V vs H and F.** In coherent locales N≤H≤F, and finite zigzag has N⊊H=F. In arbitrary locales U≤H is not known universally because U need not equal cl(D). Determine order relations in noncoherent cases and equality criteria. U∨V=F fails generally.

- **T(S)=cl(S)∧fit(S) and the J fixed-point property.** T(J)=J fails on four-point fence; product preservation fails already for finite 3-point V and dual. Classify frames/locales with J=T(J); determine quotient/subframe/product behavior and localic meaning of a one-step hull.

- **Alternating hull H.** H is the least sublocale above Δ that is BOTH closed and fitted, obtained via transfinite alternating c,f; J≤H≤F. H=F is false (deleted-plank example H=U⊊F), while finite Alexandrov locales have H=F. Understand stabilization ordinals and whether H is always an INTERNAL equivalence relation (transitivity OPEN). Conditions H=N, H=U, H=F.

- **Cross-closure cl(D) vs U.** Universal cl(D)≤U; coherent equality cl(D)=U is established and externally checked; strict cl(D)⊊U occurs even in a compact noncoherent example. Classify equality beyond coherent locales and identify its pointfree obstruction.

- **Cross-fitting fit(U) vs F and other hulls.** U is closed; fit(U) is fitted and lies inside F (provided F is fitted and contains U). Available notes indicate fit(U)⊊F can occur, but the originally cited concrete Urysohn/nonfunctionally-Hausdorff witness still needs focused verification before treating that particular example as audited. Compare fit(U) with H and fit(cl(D)); examine whether new intermediate objects are natural.

- **Cross-closure cl(V).** V is fitted. Determine when it equals U, cl(D), H, or F, and when it is itself fitted. Work in full sublocale lattice rather than only point relations.

- **Composition of I,D and their hulls.** Coherent: U=I∘I=cl(D) and V=D∘D=fit(I), established with later focused verification; compact: U=I∘I. Arbitrary-frame/localic generalizations or counterexamples for U=I² and V=D² are open. Check cross-compositions I∘D,D∘I and their joins/meets/hulls where meaningful.

- **Transitivity/equivalence-relation properties.** General V-transitivity fails in many finite-poset examples or at least is not a universal axiom; characterize hypotheses. More sharply, D=U⇒U internally transitive is OPEN for arbitrary frames, proved for compact and continuous; H transitive OPEN. Earlier universal I∘U≤U and U∘I≤U arguments were WITHDRAWN, so do not use as facts.

- **I=U, I=V; D=U, D=V; U=V; U=F; V=F.** In coherent locales I=U iff I=V iff compact opens are conormal; D=U iff D=V iff compact opens are normal. These are not arbitrary-frame characterizations. Determine useful noncoherent conditions and interactions with I=D, J=M or J=K. U,V incomparable universally (both strict orders occur in finite examples).

- **Normality vs D=U in noncompact/noncontinuous frames.** Normal⇒D=U is established compactly and continuously, but remains OPEN for arbitrary frames. D=U does NOT imply normal outside compact; D=U does NOT imply U=F outside compact. The infinitary square-cover condition is the obstacle.

- **General case D=U⇒U equivalence** and relation quotients. The exact arbitrary frame triple-product inequality is recorded in A-D-U-transitivity-2026-10-21.md; current proof attempts leave a nonzero middle residual. Properness/effectiveness of I,U and quotient saturation can be revisited only with carefully stated hypotheses.

- **Stability of the relations and of their equality conditions.** Arbitrary disjoint-union blockwise behavior largely proved. For locale PRODUCTS (frame coproducts), coherent finite-product equalities have working proofs; arbitrary preservation of D=U and of cross-hull equalities remains open, while J=T(J) FAILS binary coproduct preservation. Analyze sublocales, quotient frames, dense embeddings and maps when relevant.

- **Hochster/Priestley duality beyond point relations.** In coherent/spectral settings order duality interchanges point relations I↔D and U↔V; M,J,H are order-dual invariant pointwise in finite Alexandrov cases. Work out correct localic/nucleus statements and limits of functoriality beyond spatial finite/coherent cases.

- **Intrinsic V formula (DEFERRED), dual-far strips and other generator classes.** Compact locales have an intrinsic dual-far strip formula; arbitrary noncompact strip formula is FALSE (rational-bridge counterexample). Graph-far/bi-graph proposals are incomplete, and étale multigraphs detect additional obstructions. Strongly exact completion of finite bars fails in the T0 counterexample, whereas regular completion succeeds there; universal B_fin^{##}=B OPEN. These are side tracks, not immediate relationship equalities.

- **Finite fitted-rank filtration (DEFERRED), not a hierarchy equality.** V2⊋V3 and V3⊋V4 have externally audited working examples; V_fin⊋V now established in a countable sober T0 and a countable T1 example. General all-n strictness or positive stabilization criteria remain possible topics, but user specifically chose not to pursue isolated n one at a time.

- **Scott continuity/properness converse of inseparability quotient (DEFERRED).** Continuous-frame version has a working theorem; unrestricted arbitrary-frame generalization open. Separate from the direct relation ordering questions.

## Universal identities to keep on the side of the diagram

  Δ ≤ M ≤ I,D ≤ J ≤ U,V ≤ F,
  M=I∧D,  J=I∨D,
  cl(M)=I, fit(M)=D,
  cl(J)=cl(D)≤U, fit(J)=fit(I)=V,
  T(J)=cl(D)∧V≤U∧V,
  J≤H≤F,  H closed and fitted,
  coherent: U∧V=T(J), and U,V≤H.
Known general strict examples: M>Δ, J<U∧V, U∨V<F, H<F, cl(D)<U. No comparison U vs V generally.

**Warning on notation:** A previously shared image was a reduced Hasse diagram, NOT the entire sublattice generated by these relations. Adding the candidate K=U∧V, N=U∨V, T(J), H, fit(U), cl(V) requires checking new comparabilities; it is not just adding more layers to a fixed chain.

## Relevant project notes

- A-I-D-meet-join-frame-theory-2026-10-21.md
- A-alternating-hull-diagonal-2026-10-21.md
- A-J-fixedpoint-compositions-coproduct-2026-10-21.md
- A-V-relation-hierarchy-duality-preservation-2026-10-21.md
- A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md
- A-cross-hulls-composition-spectral-2026-10-22.md
- A-Claude-three-claims-focused-verification-2026-10-21.md
- A-D-U-transitivity-2026-10-21.md
- A-noncompact-normality-D-U-2026-10-21.md
- A-coproduct-stability-D-U-2026-10-21.md
- A-V-regular-filter-spatial-square-rank-two-generation-2026-10-24.md
