# Depth-two separation for ALL continuous dcpos

## Theorem
Let P be a continuous dcpo and L=O_sigma(P). For every rectangular bar B subset L x L (so d_I join join_B(a box b)=1 in L coproduct L), there is a horizontal-then-vertical separation tree of depth at most two.

## Proof
For each z in P put U_z={x in P:z way-below x}. In a continuous dcpo this is Scott open; the U_z cover P, and U_z is contained in upper(z). Fix z, and for each y in P evaluate the bar cover at product point (z,y). Some (a_y,b_y) in D union B contains that point, hence z in a_y and y in b_y. As a_y is Scott-open, it is upward closed, and U_z subset upper(z) subset a_y. Consequently (U_z,b_y) is a leaf (disjointness or B). The b_y cover P, thus their join is 1 by spatiality of the Scott frame. This yields a vertical split of (U_z,1). Finally U_z cover P, giving a horizontal split of (1,1). Proof uses product points only in the forward direction (frame top cover implies each point covered), not an assumption that the localic product is spatial.

## Scope
No downward-directedness, chain assumption, compactness, coherence, or finiteness of branching. Applies to continuous dcpos with compact common top, including domains with incompatible lower branches; also disjoint sums. Hence NO Scott-space of a continuous dcpo can exhibit a bar needing tree depth >2.

A natural extension is a general spatial space X possessing an open cover by U_z such that each U_z is contained in EVERY open neighborhood of a point z; these are supercompactly based / locally supercompact spaces. Their bars likewise have depth two. The Scott proof is a special case: U_z subset upper(z), and upper(z) is the intersection of neighborhoods of z in specialization order. The criterion does not require the Scott topology if this property holds.

This theorem is a reduction of bar proof complexity, NOT a proof that the resulting fitted-hull formula is genuinely dual to the far-rectangle definition of U. General depth-two collapse remains open for frames without such a local supercompact basis, including arbitrary nonspatial frames and non-core-compact spaces.
