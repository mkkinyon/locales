# Fixed points of J: finite-poset characterization and coproduct failure

21 October 2026. Working independently derived proofs. General coherent/localic extension OPEN.

Let I be closure of diagonal, D fitted diagonal, J=I join D, and T(S)=cl S meet fit S. Universally T(J)=cl D meet fit I.

## Finite Alexandrov theorem

For finite poset P with upper-set topology, ordinary pair relations I={(x,y): common upper bound} and D={(x,y): common lower bound}. Closure and fitting of subsets of P squared are downclosure and upclosure. Then

    cl(D)=I composed I,
    fit(I)=D composed D,
    T(J)=(I composed I) intersect (D composed D).

Proof: (x,y) in down(D) iff there exist u>=x,v>=y,z<=u,v; equivalently x I z I y. Dually (x,y) in up(I) iff x D z D y. Since finite Alexandrov sublocales are spatial, J=I union D and T(J) fixed iff I squared intersect D squared = I union D. This characterization is combinatorial and order-dual invariant.

## Four-point failure

For zigzag poset 0<1>2<3, pair (0,3) has no common upper or lower bound, so is not in J. But 0 I 2 I 3 and 0 D 1 D 3, so (0,3) belongs to T(J). Hence J not fixed already on four points.

## Coproduct preservation FAILS even finite coherent

Let V be 3-point poset a<t, b<t, and V^vee its dual r>o<s (i.e. least point o below two incomparable maxima r,s). In V, I is full; in V^vee, D is full, so J is full and fixed in each. In the product P=V times V^vee, I_P=I_V times I_(V^vee) and D_P=D_V times D_(V^vee). Both I_P squared and D_P squared are full: in either 3-point V shape, I squared and D squared are full. Thus T(J_P)=P squared. But x=(a,r),y=(b,s) have no common upper or lower bound, so do not belong to J_P. Therefore J fixed is NOT preserved under binary frame coproducts, even for finite coherent factors. This does not contradict coherent coproduct preservation of the stronger I=U or D=U classes.

## Hochster duality and future scope

For finite P, reversal of order exchanges I and D, so leaves M=I meet D and J=I join D invariant on points; closure and fitting exchange, making T(J) and the alternating H invariant on points. Fixed-point property is order-dual invariant in this finite setting. General coherent relation-level version needs treatment of nonspatial sublocale joins.

Continue checking frame products (locale disjoint unions), closed/open inheritance, and whether compositions cl D and fit I agree with I squared and D squared under stronger hypotheses than finite spatiality. The latter equations are not asserted for arbitrary locales.
