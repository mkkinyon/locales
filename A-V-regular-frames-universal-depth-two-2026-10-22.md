# Regular frames force universal depth-two separation for every bar
Date: 22 October 2026.
Status: point-free proof, straightforward verification, no spatiality, compactness or continuity hypotheses.

Notation: L a frame, D={(a,b):a∧b=0}, B any lower family of rectangles such that d_I∨∨_{(u,v)∈B}u⊠v=1_(L⊕L). H,V horizontal/vertical join saturations. Rather-below c≺a means c*∨a=1, where c* is pseudocomplement.

THEOREM. If L is a regular frame (every a equals ∨{c:c≺a}), then (1,1)∈V(H(D∪B)). Hence every rectangular bar B on L has separation-tree rank at most TWO. No spatiality, compactness, continuity or finiteness is assumed. Applies, for example, to O(Q) and every regular nonlocally compact Tychonoff space; shows regularity defeats all higher ranks even when opens have no nontrivial compact approximants.

PROOF. The diagonal locale map Δ:X→X×locX induces Δ*:L⊕L→L taking u⊠v↦u∧v. Since Δ*(d_I)=0 and B is a bar,
  1=∨_{(u,v)∈B}(u∧v).
By regularity, for every u∧v, write it as join of c with c≺(u∧v). In particular c≤v and c*∨u=1. The initial relation S=D∪B has (u,c)∈S (since c≤v and B lower) and (c*,c)∈D. In the H-saturation, the horizontal join yields
  (1,c)∈H(S) because u∨c*=1.
The set of such c as (u,v) ranges over B covers 1, so one vertical root join gives (1,1)∈V(H(S)). This is a depth-two V→H tree with explicit labels.

LOCAL BAR-SPECIFIC CRITERION (even without regularity). Put
  ρ_B=∨_{(u,v)∈B} ∨{c:c≺(u∧v)}.
Then ρ_B≤∨{c:(1,c)∈H(S)}, and if ρ_B=1, the same depth-two proof works. More generally the open ρ_B supports a V→H root cover with good second-coordinate pieces; even when ρ_B<1 it gives explicit partial progress. This criterion uses only the diagonal leaf data.

CHECK. This does NOT contradict original rational-bridge exact-rank-three example: its frame O(X) cannot be regular, a conclusion now deduced by rank, independently of a separate direct topological regularity argument.

This is an additional universal depth-two class not subsumed by compact-top or Lindelöf P-space results. Do not overclaim converses: nonregular compact-top frames can also have universal depth-two bars (by earlier finite-rectangle theorem).

STRONGER FORM. The full bar equation is not needed: if a family B merely satisfies ∨_{(u,v)∈B}(u∧v)=1 in a regular frame, then the same V→H depth-two argument with D works. Consequently d_I∨∨_B(u⊠v)=1 follows from its diagonal pullback equality. This is an explicit constructive formulation of the closed-diagonal property in a regular locale, with separation-tree rank bound.
DUAL ORIENTATION. Apply the same argument to τ(B): a regular frame also yields (1,1)∈H(V(D∪B)). Thus both orientation-specific depth-two certificates are available for every such B.
