# Coherent dual equivalences: fitted I and transitive D

21 October 2026. Working proof, spectral/classical, novelty unchecked.

## Theorem

For a coherent locale X,

I=U iff I is fitted iff I is internally transitive;
D=U iff D is closed iff D is internally transitive.

The previously proved coherent equality U=I composed I gives I=U iff I is transitive. The coherent equality U=cl D gives D=U iff D is closed.

For I=U implies I fitted: compact coherent case has I=U=F, where F (intersection of real-function kernel pairs) is fitted. Conversely, if I is fitted, its ordinary point relation is upward closed in the product specialization order. At any spectral point x, if u,v are maximal generalizations above x, then (x,x) in I and upward closure gives (u,v) in I. Common-upper-bound interpretation gives z above u,v, so maximality yields u=v. Every spectral point has at least one maximal generalization by patch compactness and the closed specialization order. Thus each point has a unique maximal generalization, equivalent to conormality of the compact-open lattice; hence coherent I=U.

For D=U implies D transitive: compact-normal theorem implies U=F, an internal equivalence relation. Conversely, if D is internally transitive, its ordinary point relation is transitive. If m,n are minimal specializations below x, then m D x D n, yielding m D n and a common lower bound z. Minimality gives m=n. Existence of minimal specializations is a spectral compactness fact. Unique minimal specialization is the pm/normal compact-open-lattice criterion, hence D=U.

These characterize internal transitivity, rather than only point transitivity, by necessity as well as sufficiency. The proof assumes classical spectral duality and choice, and does not assert arbitrary-frame generalization.

## Transitive closure of I is not generally contained in U

In finite poset with maxima a,b,c and minima p,q, p<a,b and q<b,c, one has a I p I b I q I c, so (a,c) belongs to the transitive closure of I. But {a} and {c} are open and their closures {p,a} and {q,c} are disjoint, so (a,c) not in U. Thus I squared=U for coherent frames does not imply the entire transitive closure of I is included in U.

**Correction:** An earlier chat response mistakenly proposed zigzag 0<1>2<3>4 as a counterexample. In that zigzag U is full, so the earlier example was wrong. Use the five-point overlapping forks described above.

## Duality

Under Hochster duality the coherent characterizations match: I fitted exchanges with D closed, and I transitive exchanges with D transitive (at level of equality properties via normal/conormal correspondence). No claim of a functorial duality of arbitrary sublocale lattices.
