# Project A — Intrinsic meet and join of I and D (21 October 2026)

Working frame-theoretic results, valid for arbitrary locales. No novelty claim.

Let X be a locale, L=O(X), Q=L⊕L=O(X²), Δ⊆X² the diagonal, I=cl Δ=C(d_I), D=fit Δ, U=C(d_U). Define M=I∧D and J=I∨D as sublocales, not point-set intersections/unions in general.

## 1. A universal hull operator

For any sublocale S, put T(S)=cl(S)∧fit(S). Both cl and fit are extensive, monotone, idempotent hull operators. Since S⊆T(S)⊆cl S,fit S, one has cl(T(S))=cl S and fit(T(S))=fit S. Therefore T is extensive, monotone, idempotent, and is the largest sublocale R (not necessarily containing S) satisfying cl R=cl S and fit R=fit S: any R with those hulls lies inside both cl S and fit S.

Applied to Δ:

    cl(M)=I,  fit(M)=D.

Thus M is simultaneously closure-dense in I and fitting-dense in D. The condition M=Δ is meaningful without I=Δ or D=Δ.

## 2. Nuclei

Let NΔ={w∈Q:δ*(w)=1}. For closed C(d), nucleus is j_C(d)(q)=d∨q. For open O(w), nucleus j_O(w)(q)=w→q. Hence

    j_I(q)=d_I∨q,
    j_D=join_in_Nuc(Q){ (w→-) : w∈NΔ }.

The join of nuclei is not generally their pointwise join. Because sublocale inclusion reverses nuclei order:

    j_J(q)=(d_I∨q)∧j_D(q),
    j_M=j_I join_in_Nuc(Q) j_D.

Also M=C(d_I)∩⋂_{w∈NΔ}O(w), a meet of locally closed sublocales.

## 3. Cross-hull identities

    cl(J)=cl(D),  fit(J)=fit(I).

For cl: Δ⊆D implies I=clΔ⊆cl D, so cl(I∨D)=cl D. For fit: Δ⊆I implies D=fitΔ⊆fit I, so fit(I∨D)=fit I.

Both cl D and fit I contain J, but only cl D⊆U follows automatically from U closed and D⊆U. Do NOT conclude fit I⊆U without fittedness of U.

## 4. Future tests

Calculate comparison of J with cl D∧fit I; determine when M=Δ, J=U, or I=D. Study behavior of cl and fit under each other, and under Hochster duality in coherent frames. Use finite Priestley/Alexandrov examples to verify any conjectural identity, retaining point-free nucleus calculations for general claims.

Background: standard fact that sublocales form a coframe, nuclei a frame, and joins of nuclei need not be pointwise. See Picado–Pultr and literature on fitting and sublocale nuclei.
