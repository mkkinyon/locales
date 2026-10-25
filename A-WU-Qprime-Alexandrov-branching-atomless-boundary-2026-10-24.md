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
