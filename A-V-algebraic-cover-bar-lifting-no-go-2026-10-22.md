# Algebraic frame quotient presentation and failure of bar lifting
22 October 2026.

For any frame L, Down(L) (all lower subsets of underlying poset, ordered by inclusion) is an algebraic frame, with compact principal downsets ↓a. The evaluation ε:Down(L)→L, U↦∨U is a surjective frame homomorphism:
ε(⋃_i U_i)=∨_i ε(U_i), and ε(U∩V)=ε(U)∧ε(V), since every u∧v lies in U∩V and ε(U)∧ε(V)=∨_{u∈U,v∈V}(u∧v). ε(↓a)=a.
Moreover top of Down(L) is principal ↓1, hence compact.

COMPACT-TOP COROLLARY: In any continuous frame A whose top is compact, every rectangular bar B has a depth≤2 separation-tree proof: the general continuous-frame three-stage theorem gives a H→V→H certificate. The H-root cover of top has a finite subcover; its finite union is V→H-good by the finite-join ideal theorem, hence the root can be proved directly by V→H of depth 2. This works for arbitrary starting lower S with (1,1)∈C(S).

NO-GO ON LIFTING: Let B be any rectangular bar on L of exact rank 3 (e.g., the rational-bridge canonical graph bar). There cannot exist a rectangular bar Btilde on Down(L) such that all images of its leaf rectangles under ε×ε lie in the downward closure of D_L∪B, where Btilde leaves themselves are tested with D_Down(L). Indeed compact-top algebraic frame Down(L) gives a depth≤2 proof for Btilde. Mapping all labels by ε produces a depth≤2 proof downstairs, contradiction. More generally, no such compatible lift can exist from any continuous compact-top frame.

Consequently an attempt to prove universal depth three by lifting EVERY bar to a canonical algebraic-frame cover and descending the resulting tree must fail at the bar-lifting step, even though every frame has a surjective algebraic frame cover. The missing issue is lifting D disjointness and tensor bar openness, not frame quotient existence.

No proof of universal depth three for arbitrary frames; this is a precise limit on one candidate strategy.
