# Why finite-frame interchange tests cannot find a counterexample
Date 22 October 2026.

Let L be a frame with a join-dense subset P of completely join-prime elements (each p∈P satisfies p≤∨A ⇒ p≤a for some a∈A). Let S⊆L×L be ANY lower set, and let C(S) be its rectangular C-ideal closure (downward, arbitrary joins in each coordinate separately). Define H,V the one-step horizontal and vertical closure operators.

THEOREM: C(S)=H(V(S)). In particular H(V(H(S)))=H(V(S))=C(S), so the proposed general interchange law and the root-level universal HVH condition hold automatically for these frames, regardless of whether S=D∪B or S=I∪J.

Proof: H(V(S))⊆C(S) by closure. For the reverse, define the property P(a,b): for every p,q∈P with p≤a,q≤b there exists (u,v)∈S with p≤u,q≤v. Property P is lower and closed under horizontal/vertical joins: if (a,b) comes from a horizontal join and p≤∨a_i, complete join-primality chooses an index i; q≤b unchanged; similarly for vertical joins with q. P holds on S, so C(S) satisfies P.

If (a,b) has P, for each p∈P, p≤a and each q∈P, q≤b, choose leaf (u_pq,v_pq)∈S with p≤u_pq and q≤v_pq. By downward closure, (p,v_pq)∈S, and because b=∨_{q≤b}q≤∨_{q≤b}v_pq, (p,b)∈V(S). Now a=∨_{p≤a}p, hence (a,b)∈H(V(S)). Empty joins handled automatically. Therefore equality.

Every finite frame is a finite distributive lattice and has a join-dense family of join-irreducible elements, which are completely join-prime (finite distributivity plus finite lattice). Hence no finite-frame computation can produce a counterexample to universal depth-three or to general interchange, even for arbitrary lower relations.

BONUS: If L is a complete chain and I,J are rectangular C-ideals, then I∪J is itself a C-ideal. For each fixed second coordinate b the fibers of I,J are principal downsets (closed under arbitrary joins). Their union is the principal downset of the larger of their two maxima; likewise for fixed first coordinate. Therefore finite unions of rectangular C-ideals on chain frames require ZERO saturation steps. Infinite unions need not have this property.

Limitation: these results do not settle universal depth-three in arbitrary frames, since the rational-bridge X already supplies a rank-three (not rank-two) bar and its frame lacks an appropriate join-prime dense basis. The general interchange and special D∪B normalization remain open beyond this class.
