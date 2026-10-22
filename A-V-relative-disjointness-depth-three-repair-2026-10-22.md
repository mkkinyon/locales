# Three-level repair of relative-disjointness rectangles

Let L be any frame, w a canonical bar neighborhood, and G={g:Phi_w(g)=1}, p=∨G. Assume (x,b) satisfies x≤b*∨p. Then (x,b) admits a separation tree of edge depth≤3 with D and B_w leaves.

Proof: x=(x∧b*)∨∨_{g∈G}(x∧g). Root split horizontally. First child (x∧b*,b) is a D leaf. For each g∈G, the definition of Phi_w(g)=1 yields a V→H tree rooted (g,1) of depth≤2. Restrict first coordinates by x∧g and second by b, using distributivity, to derive a V→H tree rooted (x∧g,b) of depth≤2. Graft, getting depth≤3.

In the closed quotient M=↑p, a D leaf (πx,πb) requires x∧b≤p, equivalently x≤b→p. The repair lemma covers the stronger condition x≤b*∨p. Thus failure to repair by this direct construction is confined to the relative-pseudocomplement gap (b→p) vs (b*∨p). For noncomplemented p this gap exists for some b, but may or may not arise from actual quotient proof-tree leaves of a bar. Three-chain example L={0<t<1}, p=b=t, x=1: x≤b→p=1 while x≰b*∨p=t. This algebraic example does not assert rank>3.

No universal depth three result established.
