# Finite horizontal closure after VH and Noetherian normalization
22 October 2026.

Let L be any frame and S⊆L×L a lower set. Let H,V denote arbitrary horizontal/vertical join closures. Put R=V(H(S)).

THEOREM 1. R is vertically C-closed and closed under finite horizontal joins, for EVERY lower S.

Proof. For b∈L let g(b)=∨{u:(u,b)∈S}; then H(S)={(a,b):a≤g(b)}. The map g is antitone. Define Φ(a)=∨{b:a≤g(b)}. Then V(H(S))={(a,b):b≤Φ(a)}. Antitonicity gives Φ(a∨c)=Φ(a)∧Φ(c): the ≤ direction from eligible-set inclusion; for ≥ use b≤Φ(a), c≤Φ(c), distribute pairwise eligible witnesses b_i and c_j and their meets, since g(b_i∧c_j)≥g(b_i)∨g(c_j). Thus if (a,b),(c,b)∈R, b≤Φ(a)∧Φ(c)=Φ(a∨c), hence (a∨c,b)∈R. Vertical closure is by definition.

THEOREM 2. If L is a Noetherian frame, i.e. every element of L is compact (every cover of an element has a finite subcover), then for EVERY lower S, its rectangular C-ideal closure is exactly
  C(S)=V(H(S)).
Proof: in a Noetherian frame an arbitrary horizontal join a=∨a_i is a finite subjoin, by compactness of a. Since R=V(H(S)) is lower and closed under finite horizontal joins, it is fully H-closed. It is V-closed already, hence is a C-ideal containing S. The reverse inclusion is automatic. No spatiality, special D relation, or complete-prime basis needed.

Dual result H(V(S))=C(S) holds in Noetherian frames by swapping coordinates. Thus any rectangular bar on such a frame has depth≤2, even when its generator relation is arbitrary.

Caveat: the finite-join closure of R is a formal fact and DOES NOT establish universal depth three for arbitrary frames, since infinite horizontal joins need not reduce to finite ones. For any proposed universal interchange one must address precisely the potentially noncompact first coordinate. The rational bridge counterexample shows not all frames enjoy the stronger two-stage collapse.

The Noetherian result is a further class of frames with universal depth-two collapse. It is not a rank-four example or proof of universal (*).
