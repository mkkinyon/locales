# Compact-top transpose absorption at stage three
Date 22 October 2026.

Let L be a frame with COMPACT top 1 (not necessarily a continuous frame), and S⊆L×L a symmetric lower relation. Define H,V separately coordinatewise join saturations, R=V(H(S)), T=H(R). The relation R is finitely H-closed for arbitrary S (proved in preceding notes).

THEOREM (root-fiber transpose absorption). For each b∈L,
  (1,b)∈T ⇒ (b,1)∈T.
Proof: (1,b)∈H(R) means 1=∨_i a_i with (a_i,b)∈R. Compactness of top selects finitely many whose join is 1. Finite H-closure of R then gives (1,b)∈R=V(H(S)). Transposition (since S symmetric) yields (b,1)∈H(V(S)). Since S⊆H(S), H(V(S))⊆H(V(H(S)))=T. Therefore (b,1)∈T.

For S=D∪B_w with symmetric bar w and top compact, define p=∨{a:(a,1)∈T} and q=∨{b:(1,b)∈T}. The theorem gives q≤p. From exact fourth-stage root criterion rank≤4 iff p∨q=1, one obtains: IF such a symmetric bar has rank≤4, then it already has rank≤3. Thus exact rank 4 is impossible on compact-top frames for symmetric bars. This does NOT prove universal depth 3 for arbitrary compact-top frames: a bar could hypothetically require rank≥5 (or transfinite).

Also for ANY S, if a is compact then (a,b)∈H(V(H(S))) ⇒ (a,b)∈V(H(S)), since the outer H-cover can be reduced to a finite one. This is a convenient general localization statement.

Caveat: This result is weaker than the continuous compact-top theorem (where rank≤2), but applies WITHOUT continuity to arbitrary compact-top frames.
