# Universal three-stage infinitary interchange on algebraic frames

22 October 2026.

THEOREM. Let L be any algebraic frame (each a∈L is join of its compact subelements) and S⊆L×L be any lower set. Write H and V for one-step closures under all horizontal and vertical joins. Then
  C(S)=H(V(H(S)))=V(H(V(S))).
In particular for every bar (even arbitrary starting leaf family), the root has an H-V-H separation tree of depth≤3. This includes all coherent frames without needing spatiality or compactness of top. It also holds for all algebraic noncoherent frames.

Proof. Set R=V(H(S)). An elementary finite interchange holds on every frame: R is V-closed and finitely H-closed. To prove this, write h(b)=∨{a:(a,b)∈S}, an antitone map. The corresponding Φ(a)=∨{b:a≤h(b)} satisfies Φ(a∨c)=Φ(a)∧Φ(c); R={(a,b):b≤Φ(a)}. In particular, if (a,b),(c,b)∈R then (a∨c,b)∈R.

Let T=H(R), which is H-closed. Suppose (a,b_i)∈T for all i, and b=∨_i b_i. Fix compact k≤a. From (a,b_i)∈H(R) we get a=∨_j a_ij with (a_ij,b_i)∈R. As k compact, k≤finite join of a_ij, and R is finitely H-closed, so (k,b_i)∈R. As R is V-closed, (k,b)∈R. Finally a=∨{k compact:k≤a}, so (a,b)∈H(R)=T. Thus T is V-closed as well and equals C(S). Transposing the argument yields C(S)=V(H(V(S))).

This is a positive infinite interchange proof: the only needed finiteness is compactness of the basis elements k, not of every open or of top. NOTE: No claim for arbitrary nonalgebraic frames. No rank-four counterexample. Rank three is a sharp universal bound in the algebraic class only if one independently finds an algebraic frame example of rank three; the known rational-bridge example may not be algebraic, so do not claim sharpness in algebraic class.

COROLLARY. For a canonical rectangular bar B_w on any algebraic frame, (*) holds. Stronger: the full generated C-ideal has height≤3 normalization for ANY S.
