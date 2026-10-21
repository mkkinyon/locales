# Project A — Eventual alternating closed-and-fitted hull of diagonal (21 Oct 2026)

**Working proof, not independently audited.** Let c and f denote closure and fitting on the lattice of sublocales of Y.

## 1. Universal construction

Define H_Y(S)=meet {R⊇S : c(R)=R=f(R)}. Common fixed points are stable under arbitrary meets, so H exists and is the join of the closure operators c and f in the complete lattice of closure operators. The fixed points of the composite cf (as well as fc) are exactly common fixed points: S≤f(S)≤cf(S), so cf(S)=S forces f(S)=S, and then c(S)=S. Transfinite iteration of cf or fc with joins at limit stages stabilizes at H(S), by the cardinal bound on the sublocale lattice. For diagonal Δ⊆X² write H=H_(X²)(Δ).

Because F is both closed and fitted and contains Δ,

    Δ ⊆ I,D ⊆ J=I∨D ⊆ H ⊆ F.

The hull H is intrinsically closed and fitted.

## 2. Finite Alexandrov theorem

**Theorem.** For finite poset P (upper-set topology),

    H(P)=F(P)=union over comparability components C of C×C.

Proof. For any subset S⊆P×P, c(S)=down(S) and f(S)=up(S), since all finite Alexandrov sublocales are spatial. A set is both down and up iff a union of undirected comparability components of the product poset. Those components are C×C' for comparability components C,C' of P, because one can move each coordinate along a comparability path while fixing the other. The ones intersecting the diagonal are exactly C×C. Every real-valued continuous function is constant on each C because the specialization order of real numbers is equality. Distinct components are clopen and may be assigned distinct real values, so F is exactly the displayed union.

## 3. Strict containment J<H

For the five-point zigzag 0<1>2<3>4, the comparability graph is connected, hence H=F=P². But 0 and 4 have no common upper or lower bound, so (0,4) lies in neither I nor D. Finite Alexandrov sublocales are spatial, so J=I∨D omits (0,4) and J<H. Thus J is NOT generally fixed under the closure operator T(S)=c(S)∧f(S), since T(J)=c(D)∧f(I)=P² in this example (indeed H=P² and any closed-and-fitted overrelation must contain it).

## 4. H need not equal F

In the previously verified sober, algebraic, arithmetic noncompact lower-point deleted-plank example, D=U⊊F. Because U is closed and coincides with fitted D, it is closed and fitted. Hence H≤U, while D=U≤H, yielding H=U⊊F. This refutes an unrestricted analogue of the finite theorem.

## 5. Next questions

When does H=F? Is H always a localic equivalence relation, or can transitivity fail? Can one characterize H or its stabilization ordinal directly from a frame coproduct? Compare H against closure-fitting cross-hulls and the fixed-point issue for J, with care on nuclei joins and arbitrary sublocale joins.
