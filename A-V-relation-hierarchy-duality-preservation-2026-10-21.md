# Project A — The fitted companion V and its hierarchy, duality, operations

21 October 2026. Definitions and coherent theorems; novel observations working, independent audit desirable.

## Definition and universal order

For any locale X, V:=fit(I), where I=closure of diagonal, D=fitted diagonal, J=I∨D, M=I∧D, H=least sublocale above diagonal both closed and fitted, F=functional equivalence, U=Urysohn closed relation. Universal: Δ⊆M⊆J⊆V⊆F; also I⊆V, D⊆V. V=I iff I fitted. U and V are not in a fixed universal order. In coherent locales U=c(D)=I², V=f(I)=D²; consequently J⊆U∩V and U∨V⊆H⊆F.

## Hochster duality

For coherent spectral X and inverse topology X^vee, specialization order reverses and I_X(point)=D_Xvee(point), D_X(point)=I_Xvee(point). Therefore U_X(point)=V_Xvee(point), V_X(point)=U_Xvee(point), by U=I² and V=D². Under finite Alexandrov order reversal M,J,H point relations stay the same; for arbitrary coherent H, beware nonspatial sublocale hulls and nonfunctorial duality of sublocale lattices.

## Relations and examples

Five-point overlapping forks: minimal p,q, maxima a,b,c, p<a,b; q<b,c. U omits (a,c),(c,a), V is full, so U⊊V. Order dual gives V⊊U. Six-point connected zigzag 0<5>1<4>2<3: by direct pair enumeration |U|=|V|=32, U\V and V\U each comprise two ordered pairs, and (0,3),(3,0) are in neither. H=F=P² (connected finite poset), so U∨V⊊H. In finite posets U=I² and V=D², and H is comparability-component equivalence.

## Preservation results and constraints

1. Arbitrary locale disjoint unions (frame products): I,D,U,V,M,J,H,F restrict blockwise, with no off-diagonal pairs, as all hulls respect a clopen decomposition. Explicit pointwise finite check; a full point-free argument can use locale coproduct disjoint block decomposition and componentwise closure/fitting.
2. Binary locale products (binary frame coproducts) in coherent/spectral class: for X,Y, ordinary point relations satisfy I_(X×Y)=I_X×I_Y and D_(X×Y)=D_X×D_Y. Consequently U and V point relations are respective products using squared compositions. Since these coherent sublocales are spatial with compact-open filter presentations (for V) and closed (for U), this gives localic relation equality U_(X×Y)=U_X×U_Y and V_(X×Y)=V_X×V_Y, interpreting relation products via permutation X²×Y². Likewise I and D satisfy analogues in coherent case. Arbitrary (infinite) products not claimed.
3. Equality property V=I is the coherent conormal/I=U condition and hence stable under coherent frame coproducts (previous theorem). Equality V=D is the coherent normal/D=U condition and similarly stable under coherent frame coproducts.
4. The fixed-point condition J=T(J) is not stable under binary frame coproducts, by 3-point V and its dual. Hence no broad preservation claim for every condition in the menagerie.

## Exact coherent equality consequences

I=U iff I=V iff I is fitted iff I internally transitive iff K conormal.
D=U iff D=V iff D closed iff D internally transitive iff K normal.
For D=V equivalence use D²=V and reflexivity of D: D²=D iff transitivity; coherent characterized above.
No general fixed order between U and V, and H≠U∨V in general.

## Open agenda

- Investigate whether arbitrary disjoint-union and coherent finite-product assertions admit short intrinsic frame proofs; no unsupported infinite coproduct statements.
- Hochster duality of M,J,H and preservation of H under products; formal relation via Priestley bitopology.
- Is V internally transitive? Typically not; determine useful hypotheses. Relate V to F for broader frame classes.
- Audit 6-point relation enumeration and novel coherent preservation statements before promotion to publication.
