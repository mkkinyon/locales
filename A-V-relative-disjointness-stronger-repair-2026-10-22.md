# Strengthened depth-three repair and quotient residual gap
Date 2026-10-22.

Let w∈L⊕L be a canonical bar neighborhood, r_w(b)=∨{u:u⊠b≤w}, h_w(b)=b*∨r_w(b), G_w={a:Φ_w(a)=1}, p=∨G_w.

Lemma: If x≤h_w(b)∨p, then (x,b) has a D/B_w separation-tree proof of depth at most 3.

Proof: horizontally cover x by x∧b*, x∧r_w(b), and x∧g for g∈G_w. The first branch is D; the second is a B_w leaf because r_w(b)⊠b≤w (the rectangle operation preserves arbitrary first-coordinate joins); the third has a V→H tree of depth ≤2, by restricting a certificate for (g,1) to (x∧g,b). Thus total depth≤3.

In closed quotient ↑p, a disjointness leaf at (πx,πb) means x≤b→p. Thus lifting all such leaves with depth≤3 would follow from the additional inequality
  b→p ≤ b*∨r_w(b)∨p
for each b that actually appears. This is a concrete sufficient criterion, not known to follow from barhood or from the special definition p=∨G_w. It is strictly stronger than the overlap identity x∧b≤p; the three-chain frame demonstrates lack of Boolean splitting.

No universal depth-three proof or rank-four witness is obtained. Do not confuse depth-three repair of a SINGLE quotient leaf with no-overhead lifting of an entire quotient proof tree: grafting such repairs may increase the overall tree height.
