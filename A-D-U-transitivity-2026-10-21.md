# A — Transitivity of U under D=U (21 October 2026)

**Status:** positive theorem for continuous frames (direct checked proof); the arbitrary-frame implication OPEN. Do not infer internal transitivity from pointwise transitivity without spatiality of the composable-pair sublocale.

## Question

For locale X, with D=fit(Δ) and U=C(d_U), does D=U imply U∘U⊆U? U is reflexive and symmetric, so this would make U an internal equivalence relation.

## Theorem: continuous frames

For any classically continuous frame L=O(X), D=U implies U is an internal equivalence relation.

Proof: L continuous implies X locally compact sober, with localic finite products agreeing with ordinary topological products. For original points, x D y iff cl{x}∩cl{y}≠∅. If x D y and y D z, choose u∈cl{x}∩cl{y}, v∈cl{y}∩cl{z}. Every neighborhood of u and of v contains y, so u I v. Since I⊆U=D, obtain t∈cl{u}∩cl{v}, hence t∈cl{x}∩cl{z}. Thus D is pointwise transitive. In X³, the sublocale P=U_12∩U_23 is closed, hence spatial and point-determined. All its ordinary points (x,y,z) satisfy (x,z)∈U, so the coordinate map P→X² factors through the closed U. Therefore U∘U⊆U. Reflexivity and symmetry are universal. The same reasoning applies to a sober X whose localic triple product agrees with the ordinary spatial product.

**Not dependent on normality:** The recently verified noncompact algebraic/arithmetic lower-point plank has D=U⊊F, but U is nonetheless an internal equivalence relation by this theorem.

## Intrinsic exact test (any frame)

Put Q_3=O(X³) and d_{12}=∨_{a*∨b*=1}a_1∧b_2, d_{23}=∨_{a*∨b*=1}a_2∧b_3 (all joins in Q_3). The composable-pair locale P=U_12∩U_23 is the closed sublocale C(d_{12}∨d_{23}) of X³. Since the quotient frame of C(d) is ↑d, U∘U⊆U iff

    a_1∧b_3 ≤ d_{12}∨d_{23}

for every far pair a,b (a*∨b*=1). This inequality is independent of any spatiality hypothesis. It is the correct point-free target.

The established D=U open-cover criterion supplies identities d_U∨⋁_{c∈C}c⊠c=1 in Q_2 for every cover C, but no proof yet transports these identities to the above inequality in Q_3.

## Known cases and status

- Finite posets: D=U iff each comparability component has a least point, so U is the component equivalence.
- Compact locales: D=U ⇒ normal ⇒ U=F, a kernel pair, so transitive.
- Continuous frames: proved above without normality.
- Arbitrary frame: still open; a counterexample must be invisible to ordinary pointwise transitivity, i.e., exploit a nonspatial closed composable-pair locale or the corresponding frame quotient.

**Next mathematical test:** Can the arbitrary-cover identities for D=U be used directly on Q_3 to establish the inequality? Do not simply redo the pointwise proof or invoke a global quotient without properness.

## Correction and fittedness-plus-absorption test (21 October 2026)

**WITHDRAW the purported universal absorption proof I∘U⊆U, U∘I⊆U.** It incorrectly asserted that a rectangle arising from b*∧b=0 vanishes on U. The disjointness condition implies vanishing on I, not the larger U. The identity b**∨b*=1 needed for far separation fails in general. Therefore the absorption inclusions are at best UNPROVED here; neither should be used as a lemma. The earlier chat statement and any forward inferences based on it are superseded.

**Formal fittedness+absorption is insufficient for transitivity.** Let X be discrete on three points 0,1,2, so I=Δ. Let R contain the diagonal and symmetric edges 0–1 and 1–2, omitting 0–2. Every sublocale of X×X is clopen and fitted. R is reflexive, symmetric and closed/fitted; I∘R=R=R∘I, but R is not transitive. This does NOT refute D=U⇒U transitive, because R is not U(X). It refutes the proposed proof strategy using only formal fittedness and absorption.

**Status:** D=U⇒U internal equivalence remains OPEN for arbitrary frames, established for continuous and compact frames. Future work must use additional properties peculiar to U and D.
