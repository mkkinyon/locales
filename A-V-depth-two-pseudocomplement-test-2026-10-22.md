# Pseudocomplement formula for depth-two rectangular bars (22 October 2026)

Let L be any frame, B ⊆ L×L, and D={(a,b):a∧b=0}. Write S=down(D∪B). Define F_B(a)=∨{v: (u,v)∈B, a≤u}, and G_B(b)=∨{u:(u,v)∈B,b≤v}. Then:
  V_B(a):=∨{b:(a,b)∈S}=a*∨F_B(a);
  H_B(b):=∨{a:(a,b)∈S}=b*∨G_B(b).
Proof: a disjoint leaf (a,b) is possible exactly when b≤a* (largest such disjoint open); B leaves are those under one (u,v) with a≤u, hence b≤v. The down-closure introduces no other cases.

EXACT depth-two H→V criterion:
  ∨{a: a*∨F_B(a)=1}=1.
EXACT depth-two V→H criterion:
  ∨{b: b*∨G_B(b)=1}=1.
These are not equivalent in general for unsymmetric B. No assertion that being a rectangular bar forces either condition in arbitrary L. For an arbitrary bar, diagonal cover ∨_B(u∧v)=1 is necessary but not sufficient for barhood outside positive classes.

A useful B-specific sufficient condition: suppose a chain {c_i}⊆L has join 1, each c_i=u_i∧v_i for a rectangle (u_i,v_i)∈B, and for each i the tail rectangles with c_j≥c_i have second-coordinate join 1 (e.g. a cofinal increasing chain of overlaps). Then F_B(c_i)=1, so H→V depth2. This generalizes the chain-frame construction to particular bars in arbitrary frames.

Remaining goal: find an actual B bar with both displayed joins <1, or prove a universal implication from barhood. Need distinguish localic barhood from pointwise covering: the latter alone is insufficient when the localic square is nonspatial.
