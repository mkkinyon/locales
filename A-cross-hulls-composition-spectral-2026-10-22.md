# Cross-hulls and relation squares: spectral point identities

22 October 2026. Working theorem on ordinary points; **NOT** a general localic composition equality.

Let X be spectral with specialization x≤y iff x∈cl{y}. Define ordinary pair relations I(x,y) iff x,y have a common upper bound, and D(x,y) iff they have a common lower bound. In coherent locales these are the point sets of localic I and D, respectively.

## General poset algebra

For any poset P with coordinatewise order on P squared, down(D)=I composed I, and up(I)=D composed D. The first holds because x≤u, y≤v, z≤u,v iff x I z I y. The second is its order dual.

## Spectral topological theorem

For spectral X, the *ordinary topological* closure of point relation D in X squared equals I composed I, and intersection of all *ordinary open subsets* of X squared containing point relation I equals D composed D.

Proof of closure: specialization order is closed in compact Hausdorff patch square. I is projection of a patch-closed subspace of patch triple product, hence patch-closed. Its relational square I² is likewise patch-closed and is a downset, so is spectrally closed. By the poset algebra it is exactly down(D), which is the smallest specialization-downward set containing D, so equals spectral closure(D).

Proof of open saturation: I is patch-closed, and up(I)=D². If p not in up(I), then q not≤p for every q∈I. Priestley separation gives, for each q, a patch-clopen upper set containing q but excluding p. Patch compactness of I yields a finite union of these open upsets covering I but excluding p. Therefore intersection of all spectral opens containing I is exactly up(I).

**Scope caution:** These are point-set statements. They do NOT establish c(localic D)=localic I∘I or f(localic I)=localic D∘D, because fitted intersections and relational images can be nonspatial even when the ambient locale is coherent and spatial. The unrestricted localic identities remain OPEN; avoid confusing pointwise saturation with fitted sublocale hull.

## Intrinsic hull formulas

Let Q=O(X²), d_I=join over disjoint rectangles, and j_D the nucleus of fitted diagonal D. Closure of any sublocale S has nucleus q↦j_S(0)∨q, so c(D)=C(j_D(0)). Also f(I)=intersection of open O(w) over all w∈Q with d_I∨w=1; equivalently, its nucleus is join in Nuc(Q) of the open nuclei w→- over such w. These are always correct frame-level expressions but presently do not simplify to the relation-square composites.

## Next

Audit localic composition image mechanisms and search for an explicit counterexample or additional hypotheses (e.g. properness) that force pointwise relation-square identities to lift. Defer rather than promote spectral point calculations to locale equalities.

## Coherent-localic refinement (later segment)

**Proposition (compact locales):** I composed I is a CLOSED sublocale. Indeed P=I_12 intersect I_23 is closed in X cubed, and the coordinate projection X cubed to X squared is closed for compact X (properness of projection). Its image I composed I is therefore closed.

**Proposition (coherent locales):** I composed I is contained in cl(D). In spectral representation P is a closed, spatial sublocale of X cubed. Every point (x,y,z) of P maps to (x,z) in ordinary I composed I, which equals the ordinary topological closure of D's points by the preceding spectral theorem. This lies in the closed sublocale cl(D). Spatiality of P yields factorization of P to X squared through cl(D). Taking localic images gives the inclusion.

**NOT PROVED:** reverse cl(D) contained in I composed I. It would suffice to show D contained in I composed I, because the latter is closed. D can be a nonspatial fitted sublocale; its point set alone cannot establish that inclusion. Likewise no general coherent-localic equality fit(I)=D composed D established. These are live gaps, not counterexamples.
