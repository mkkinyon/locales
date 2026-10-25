# Project A — Q': Alexandrov theorem and an atomless-boundary branching control

24 October 2026. Working results (internally checked, not independently audited or priority checked). This note continues the Q' investigation. Q': is W=cl(D) always equal to W2=cl(D2)?

## 1. Arbitrary Alexandrov locales have W=U

**Theorem (working).** Let P be any poset with the upper Alexandrov topology and L=O(P). Then W=W2=U. No finiteness, sobriety of the original presentation, coherence, or compactness assumed.

Proof. Every point x has least open neighborhood ↑x. In an Alexandrov square, the point Urysohn relation is

  (x,y)∈pt U iff cl(↑x)∩cl(↑y)≠empty

iff there are u≥x, v≥y and z≤u,v. The latter precisely means some Cm point (u,v) lies in the product neighborhood ↑x×↑y. Hence pt U=cl(Cm(P)) in P×P.

The locale represented by O(P) is locally compact (principal ↑x are compact opens). Its localic square is spatial with frame O(P×P); this remains valid if the presentation P is not sober, by replacing P with its sobrification. Thus point inclusions detect closed sublocale inclusions. Since W is closed and contains Cm(P), W contains cl Cm(P)=U, and W≤U universally. Hence W=W2=U.

Alternatively Cm(P) is itself an OPEN subset of P×P: common predecessor is preserved when each coordinate increases. So U=cl Cm is REGULAR CLOSED, and the universal regular-core theorem gives W=U. This means the Alexandrov theorem is a genuine noncompact extension of the finite case but does not reveal a new mechanism beyond regular-closedness.

## 2. A branching forcing poset with no favorable local neighborhoods

Let P=Fn(N,2)\{empty}, nonempty finite partial binary functions ordered by extension, with upper Alexandrov topology. Principal ↑s are compact opens and join-generate L=O(P). The cover

  C={↑{n↦b}:n∈N,b∈{0,1}}

has no finite subcover, so L is noncompact and algebraic.

No nonzero open is hyperconnected: every nonempty open contains ↑s, and a fresh coordinate n splits ↑s into the disjoint nonzero opens ↑(s∪{n↦0}) and ↑(s∪{n↦1}). Hence h_hc=0.

No compact closed sublocale has nonempty interior: if a compact closed subspace F contained ↑s, it would contain its CLOSED subspace cl(↑s), the set of nonempty finite conditions compatible with s. This latter closed subspace is noncompact: the singleton-literal cover C restricts to a cover with no finite subcover (choose a fresh literal outside any proposed finite list and outside dom(s)). Thus h_cc=0.

For any nonempty opens A,B choose s∈A,t∈B and a fresh coordinate n outside both domains. The conditions s∪{n↦0},t∪{n↦0} belong to A,B and have the common predecessor {n↦0}. Therefore cl A∩cl B≠empty, so d_U=0 and U=Q. The Alexandrov theorem gives W=W2=Q. The inseparability relation I is proper, since incompatible conditions have disjoint principal opens.

Yet D<D2. Let Cnt=2^N Cantor space, B=RO(Cnt). For s∈P set h(↑s)=[s] and k(↑s)=[flip(s)]; these extend to frame homomorphisms by U↦double-negation of ⋃_{s∈U}[s] and bitwise flip. For any finite open cover U_1,...,U_m of P, one U_j contains infinitely many distinct singleton conditions {n↦b}; the associated cylinders [n=b] and [n=1-b] have dense union, so h(U_j)=k(U_j)=1. Thus the pair is finite-cover-compatible. But every c=↑{n↦b} in C has h(c)∧k(c)=0. Hence arbitrary cover compatibility fails, proving D<D2.

This example has h_hc=h_cc=0, is noncompact, and has the strongest possible D2>D defect, yet Q' holds because U=whole. It rules out these individual obstructions as sufficient conditions.

## 3. Atomless NONREGULAR U boundary, D<D2, no useful local neighborhoods, but W=W2

Let Y be the **compact** T1 two-apex space from the external referee report: Y=R⊔{p,q}; p-neighborhoods contain p and all but finitely many positive reals, q-neighborhoods contain q and all but finitely many negative reals. Let

  A_+=[0,∞)∪{p},   A_-=(−∞,0]∪{q},
  K_Y=A_+²∪A_-².

Its Urysohn point relation is U(Y)=K_Y ∪ {(p,q),(q,p)}, with the two cross pairs relatively isolated in U(Y), and K_Y=cl(int U(Y))=W(Y)=W2(Y). The space Y is COMPACT.

Form the localic product X=P×Y, with P the infinite branching poset of §2 (or its sobrification). Both frames are locally compact and the product's frame is the frame of the ordinary topological product, so closed localic relations are detected by the displayed ordinary point sets.

Because U(P)=P² and U relations on such spatial products factor coordinatewise,

  U(X)=P²×U(Y),
  K_X=cl(int U(X))=P²×K_Y,
  G_X=U(X)∧O(d_U**)=P²×{(p,q),(q,p)}

(up to reordering of product coordinates). Here G_X is relatively CLOPEN in U(X).

Pull back the binary cover {Y\{p},Y\{q}} along X→Y. Its binary square neighborhood excludes exactly G_X inside U(X). Since D2(X) lies in that square neighborhood, D2(X)∧G_X=0; relative openness of G_X shows W2(X)∧G_X=0. Thus W2(X)≤K_X. The universal regular-core inclusion K_X≤W(X)≤W2(X) gives

  W(X)=W2(X)=K_X < U(X).

The strict D(X)<D2(X) is inherited from the finite-cover-compatible but not all-cover-compatible pair of §2: compose its maps L(P)→RO(Cnt) with inverse image along the continuous slice P→P×Y, s↦(s,y), for any y∈Y. A pulled-back literal cover fails, while finite-cover compatibility survives. I(X)<K_X because incompatible P-conditions can be paired with the same Y point, giving a K-related but I-distinguishable pair.

Just as for P, X has h_hc=0, since EVERY nonempty product-open contains a rectangle whose P-coordinate splits into two disjoint nonzero opens. It has h_cc=0: if a compact closed subspace F contained a basic ↑s×B, choose y∈B; F must contain cl(↑s)×{y}, whose projection to P is the noncompact CLOSED set cl(↑s). Projection of compact F to P would be compact; the closed subset cl(↑s) of that compact projection would have to be compact, a contradiction.

Thus C(h_hc∨h_cc)=X is noncompact. Nevertheless Q' holds.

**Atomlessness.** G_X is the disjoint union of two copies of P², and P² has no nonzero hyperconnected open. Hence B(O(G_X)) is ATOMLESS. Likewise W2(X)=P²×K_Y has no hyperconnected nonzero opens (split its P²-coordinate), so B(O(W2(X))) is ATOMLESS. Thus all previously listed necessary properties for a Q' counterexample can coexist while Q' remains TRUE.

The missing property is that W2 must itself meet the nonregular U boundary G. In this example one global BINARY cover eliminates the entire G.

## 4. Refined Q' obstruction: the residual boundary inside W2

Put d=d_U and K=C(d**)=cl(int U). Set

    H2 = W2 ∧ G,    G=U∧O(d**).

H2 is an OPEN sublocale of W2. Since K≤W≤W2 universally, a failure W<W2 yields a nonzero relatively open defect

    E = W2 ∧ O(d_W).

Indeed W=C(d_W) is closed. Also d_W≤d**, so E≤O(d**)∧W2=H2. D∧E=0, whereas D2∧E is dense in E because D2 is dense in W2 and E is open there.

**Atomic residual-boundary theorem (working).** If the Booleanization B(O(H2)) is atomic (spatial), then W=W2.

Proof by contradiction: take the nonzero open defect E⊆H2. An atomic Booleanization of H2 restricts to an atomic Booleanization of every nonzero OPEN E, so B(E) contains a point. The least dense sublocale B(E) is contained in D2∧E because D2 is dense in W2. Hence that point belongs to D2. However D and D2 have exactly the SAME points in arbitrary locales (binary vs arbitrary cover splitting of completely prime filters), so it belongs to D as well. This contradicts D∧E=0.

This is a sharper positive condition than requiring all of B(W2), or all of B(G), to be atomic; it tests only the part of the nonregular Urysohn boundary actually reached by finite-cover fitting's closed hull.

In particular H2=0 implies W=W2. Conversely any strict W<W2 requires H2≠0 and a nonzero ATOMLESS Boolean portion of H2.

## 5. Remaining target

Q': W=W2 universally? OPEN. Q: W2=U ⇒ W=U? OPEN. The branching/Cantor model realizes a genuinely infinitary D2>D defect on a locale with no hyperconnected or compact-closed-neighborhood strip; the two-apex product also supplies a nonzero atomless G. Still, its infinite-cover defect lives away from G and its binary test already kills G. A successful counterexample needs finite-cover compatibility that is dense INSIDE a nonzero open part of H2, but fails full-cover compatibility there. This is a coupling problem, not just accumulation of independent pathological components.
