# Three-stage saturation is finitely closed in BOTH coordinates

Let L be any frame, S⊆L×L lower, H,V its coordinatewise arbitrary join closures. For each b let h(b)=∨{a:(a,b)∈S}, and Φ(a)=∨{b:a≤h(b)}. Since h antitone, Φ(a∨a')=Φ(a)∧Φ(a'). Define G_b={a:b≤Φ(a)}. Then G_b is a lattice ideal (lower and finite-join closed). Set p_b=∨G_b. We have
 T=H(V(H(S)))={(a,b):a≤p_b}.

NEW THEOREM: b↦p_b sends finite joins to meets:
 p_0=1, p_{b∨c}=p_b∧p_c.
Proof: G_{b∨c}=G_b∩G_c. For any ideals I,J in a frame, (∨I)∧(∨J)=∨(I∩J), because distribute meets into join and use x∧y∈I∩J. Therefore p_{b∨c}=∨G_b∩G_c=(∨G_b)∧(∨G_c).

Hence for ALL lower S and ALL frames, T=H(V(H(S))) is automatically closed under finite vertical joins, in addition to arbitrary horizontal joins. In particular any violation of full vertical closure of T is necessarily an infinite vertical cover. The earlier R=V(H(S)) is finitely horizontal closed; after next horizontal closure we get the dual finite closure in the remaining coordinate. This does NOT establish closure under arbitrary vertical joins, so no universal depth-three result follows yet.

For canonical bar S=D∪B_w, (*) means p_1=1. The full interchange law T V-closed is equivalent to p_{∨_i b_i}=∧_i p_{b_i} for ALL families. Finite families satisfy it automatically, even without barhood or disjointness. This pinpoints genuinely infinite *second-coordinate* joins as the sole possible obstruction after HVH.

NOTE: for a bar S, C(S)=L×L, so T=C(S) iff p_1=1. The full interchange normalization and the root-level conjecture coincide in the bar case.
