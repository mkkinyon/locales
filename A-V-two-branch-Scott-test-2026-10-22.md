# Two-branch Scott domain: structural test (2026-10-22)

Let P=(A⊔B)∪{⊤} where A,B are distinct copies of (0,1), each ordered by usual order, and every point lies below ⊤; points in opposite branches are incomparable. Directed subsets have suprema: a directed set involving both branches contains ⊤, and each separate branch has its real supremum or ⊤. The domain is a dcpo (indeed continuous, with branch points approximated from below).

Every nonempty Scott open U must contain ⊤, and Scott inaccessibility along directed chains approaching ⊤ forces U to contain final segments of BOTH branches. Conversely any U_{r,s}={⊤} ∪{a_t:t>r}∪{b_t:t>s}, with 0≤r,s<1, is Scott open, as is ∅. Thus L=O_sigma(P) is {0}∪{U_{r,s}:r,s∈[0,1)} with order U_{r,s}≤U_{r',s'} iff r≥r',s≥s'. Its nonempty opens pairwise intersect, so disjoint rectangles D consist only of zero-coordinate rectangles and d_I=0. Consequently a rectangular bar B here is simply a family with ∨_{(a,b)∈B}a⊠b=1.

The space is noncompact: U_{1/n,1/n} increases to X and no finite subfamily covers. It is nonregular: no nonempty opens are disjoint and not every proper nonzero open is well-inside 1. There is no nonzero completely join-prime open: each U_{r,s} is the join of a sequence U_{r+eps_n,s+eps_n} with eps_n↓0 and each member proper below it.

This avoids all previously proved depth-two criteria. HOWEVER these facts do not supply a bar failing the exact depth-two tests. In the threshold notation, a proposed B must be shown to satisfy full coproduct cover, not merely cover ordinary pairs. Depth 2 H→V iff ∨{a:∨{b:(a,b)∈down(B)}=1}=1; likewise V→H in reverse. No such failure has been demonstrated; do not claim a strict rank example.

A simple high-density family B={(u,u):u<1} with ∨u=1 is NOT a counterexample: directedness of nonzero opens ensures ∨_u u⊠u=1 and its tails admit depth-two certificates. Need a subtler bar or a universal collapse theorem.

A caveat in reasoning with opens: a generic product-point cover need not imply 1 in the localic product; use the rectangular C-ideal calculus for barhood.
