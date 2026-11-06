# Project A — Mixed composition and the two-idempotent coherent relation calculus

6 November 2026. New research segment after the Q/Q' pause. **WORKING theorem package; finite-poset statements directly checked, coherent-localic extension uses the previously audited compact-open-filter / spectral sublocale machinery and still deserves a fresh adversarial review. No literature novelty claim.**

## 0. Setup

Let X be a coherent locale, P its spectral point space, and P_patch its compact Hausdorff Priestley patch. Order P by specialization, x≤y iff x∈cl{y}. Let I=cl Delta, D=fit Delta, J=I∨D, U=I∘I=cl D, V=D∘D=fit I, T(J)=U∧V, H the least closed-and-fitted diagonal hull. The equations involving U,V are the previously verified COHERENT theorems; the separate compact-localic U=I² theorem remains valid without coherence.

Define R=I∘D and R^smile=D∘I. The two are converses because I,D are symmetric.

## 1. Elementary poset calculation

For any poset P,

  x I y iff ∃u(x≤u≥y)
  x D y iff ∃v(x≥v≤y).

Then

  x R y iff ∃u,v (x≤u≥v≤y);
  x R^smile y iff ∃u,v(x≥v≤u≥y).

Equivalently,

  R=uparrow_second(I)=downarrow_first(D).

Here up_second enlarges only the second coordinate, down_first only the first. R is therefore the LEAST order distributor (downward in first coordinate and upward in second) containing J=I∪D; R^smile is the least oppositely oriented distributor containing J. This holds at the point-relation level for any poset.

Immediate comparisons:

  J⊆R∩R^smile⊆R,R^smile⊆R∪R^smile⊆U∩V.

The final inclusion follows because x≤u≥v≤y implies x I v I y and x D u D y; similarly for the converse.

## 2. Strictness: three finite coherent posets

(A) FOUR-FENCE: x<u>v<y. Then (x,y)∈R but (x,y)∉R^smile and (x,y)∉J. Consequently R≠R^smile and J<R. This witnesses noncommutativity.

(B) SIX-HEXAGON: x<u>v<y<u'>v'<x, only these six generating Hasse comparisons. Both alternating orientations connect x,y, so (x,y)∈R∩R^smile; no common upper/lower bound of x and y, so (x,y)∉J. Thus J<R∩R^smile.

(C) EIGHT-CYCLE: eight distinct points x,y,u,v,z,r,w,s with ONLY generating comparisons

  x<u, z<u, z<v, y<v;
  r<x, r<w, s<w, s<y.

The two internally disjoint four-edge paths x<u>z<v>y and x>r<w>s<y yield x I z I y and x D w D y. Hence (x,y)∈U∩V. However x,y have comparability-graph distance exactly four, so neither length-three mixed composition relates them. Thus R∨R^smile<U∧V.

All finite sublocales are point-determined here. Calculations independently checked with explicit transitive closure/relational product code for each poset; many randomly sampled finite posets support the general pointwise laws. No minimality claims for example sizes.

## 3. Comparability graph powers and two idempotents

Let A={(x,y):x≤y} and B=A^smile, regarded first as point relations. A²=A and B²=B. At the point level:

  I=AB, D=BA,
  R=ABA, R^smile=BAB,
  U=ABAB, V=BABA.

Let C_cmp=A∨B (reflexive comparability graph). Any walk of length n in C_cmp may be shortened whenever two consecutive steps have the same orientation. Thus

  C_cmp²=I∪D=J,
  C_cmp³=R∪R^smile,
  C_cmp⁴=U∪V.

Proof by reduction of length 2,3,4 paths to alternating arrow patterns. In particular

  J²=U∪V.

This uses only transitivity of A,B, reflexivity, and the coherence-specific identifications of U,V with the fourth alternating words.

## 4. Coherent-localic lift: working proof outline

For spectral P, specialization order is CLOSED in P_patch²; A,B and all fixed finite relational products are patch-closed because they are projections of closed sets in finite powers of compact Hausdorff P_patch. Patch-closed (proconstructible) subsets of spectral spaces are spectral and have spectral inclusions (standard Hochster theory).

The previously verified coherent compact-open-filter lemma identifies D with the spatial coherent spectral sublocale having point set D_P; I is closed and coherent. More generally the proconstructible point-subspaces A,B,I,D and their finite joins are coherent spectral sublocales. Fiber products of their spectral inclusions in the coherent category are coherent, spatial, and pointwise computed by the corresponding patch-closed conditions. Their localic image under the spectral projection π13 is represented by the patch-closed pointwise relational composite, because projections of patch-closed sets are patch-closed and spectral subspaces are sober.

**CONCLUSION (working coherent-localic theorem):** the entire two-idempotent table and graph-power identities in §3 hold as equalities of GENUINE sublocales, with relational composition the localic image of composable pairs. In particular:

  I∘D=ABA; D∘I=BAB;
  J²=U∨V;
  J ≤ (I D)∧(D I) ≤ I D,D I ≤ (I D)∨(D I) ≤ U∧V.

The finite examples in §2 show strictness at every principal stage.

**Audit priority:** independently check that coherent finite pullbacks and relational images of proconstructible subspaces agree with the claimed sublocale-level constructions (avoid illicit promotion from pointwise composition), especially the pullback of I12 and D23 and the relation C_cmp. The Hochster/proconstructible facts can be supported from standard spectral-space sources; this is a correctness dependency, not a priority assertion.

## 5. Hull interpretations, duality

Because J⊆R,R^smile⊆U∧V in coherent locales, and cl J=U, fit J=V, every S satisfying J⊆S⊆U∧V has exactly

  cl(S)=U, fit(S)=V.

In particular cl(R)=cl(R^smile)=U and fit(R)=fit(R^smile)=V. So composition distinguishes sublocales invisible to their separate closure and fitting hulls. Similarly T(S)=cl S∧fit S=U∧V throughout that interval.

Hochster order-duality exchanges A and B, so exchanges R=ABA and R^smile=BAB; their meet and join are self-dual at the point level (and via coherent presentations, under corresponding duality of the coherent relation calculus).

## 6. A new compositional recursion for H

For a coherent locale, H is already known (independently externally audited) to be the least PATCH-CLOSED coordinatewise comparability-saturated relation containing Delta.

Define on patch-closed point relations S⊆P²

  Theta(S)=C_cmp∘S∘C_cmp.

Theta preserves patch-closedness (compact order relations, spectral projection); it is monotone and inflationary. Theta(S)=S iff C_cmp∘S⊆S and S∘C_cmp⊆S, equivalently S is coordinatewise comparability-saturated. Transfinitely iterate

  S_0=Delta, S_(alpha+1)=Theta(S_alpha),
  S_lambda=patch_closure(⋃_(beta<lambda) S_beta).

The least fixed point is pt(H), and its coherent spectral sublocale IS H. For finite n,

  S_n=C_cmp^(2n), so
  S_1=J, S_2=U∨V, S_3=C_cmp^6, ...

At the first infinite stage S_omega=patch_closure(sim_c), where sim_c is finite comparability connectivity. This need NOT be stable: patch limit pairs may trigger new comparability propagation, as in the previous omega+m coherent examples. This is a new scheduling/interpretation of the same H hull, not a novelty claim about the already audited existence of H.

## 7. The next coherent-to-general questions

1. **Order distributor viewpoint:** Is there a point-free analogue of the specialization-order sublocale A outside coherent locales, sufficient to retain I=AB and D=BA? Beware that the patch spectral construction is specific to coherence.
2. **General relation comparisons:** For arbitrary locales do I∘D and D∘I lie in W∧V, in U∧V, or in H? The coherent proof uses proconstructible spatiality and does not establish these inclusions universally.
3. **Equality classes:** Characterize coherent P with R=R^smile, R=J, or R∨R^smile=U∧V. The finite witnesses exclude unconditional equalities.
4. **H vs composition:** Explore whether Theta gives shorter intrinsic formulas in special coherent families (e.g. normal, conormal, or bounded comparability diameter), without reopening isolated ordinal-height searches.

References: project files A-cross-hulls-composition-spectral-2026-10-22.md; A-Claude-three-claims-focused-verification-2026-10-21.md; A-postV-external-audit-reconciliation-2026-10-24.md; A-H-formal-hull-odd-powers-omega-plus-m-2026-10-24.md; standard facts on proconstructible subspaces of spectral spaces and localic Priestley duality.

## 8. All finite comparability powers reduce to TWO alternating words

The C²/C³/C⁴ identities are the first cases of an exact family; this is a short semigroup identity (not a priority/novelty claim).

**Proposition (finite relation algebra).** Let A,B be ANY two reflexive transitive relations on a set; write C=A∪B, I=AB, D=BA, R=ABA, R'=BAB. Then for each n≥1,

    C^(2n)   = (AB)^n ∪ (BA)^n = I^n ∪ D^n;
    C^(2n+1) = (ABA)^n ∪ (BAB)^n = R^n ∪ (R')^n.

Proof. Relational composition distributes over set-theoretic unions. Expand C^m into all length-m words in A,B. Since A²=A and B²=B, every word collapses to an alternating word of length ≤m. Because A and B are REFLEXIVE, any shorter alternating word lies inside one of the two fully alternating length-m words, by padding left/right with identity-containing A/B factors of the appropriate orientation. The two length-m alternating words themselves are present in the expansion, giving equality.

For coherent locales with A,B the specialization-order sublocales, the same identities hold in the proconstructible spectral relation calculus, SUBJECT TO the coherent-localic image/pullback audit flagged in §4.

**Application to H:** In §6, S_n=C_cmp^(2n)=I^n∨D^n for every finite n≥1, so the H-composition schedule has exact finite stages

    S1=I∨D=J;
    S2=I²∨D²=U∨V;
    S3=I³∨D³;
    ...
    Sω=patch_closure(⋃_{n≥1}(I^n∨D^n)).

This is a separate schedule from the prior *closed-stage* kappa recursion (whose stage n is I^(2n+1)); both stabilize at H, but finite stages must not be conflated.

The relation-algebra identity is verified independently by random finite-poset tests to exponent 11, in addition to the elementary proof.
