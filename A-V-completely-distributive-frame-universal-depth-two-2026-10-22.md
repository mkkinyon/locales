# Completely distributive first factors force universal two-stage rectangular saturation

22 October 2026 — NEW THEOREM. A true strengthening of previous "join-dense completely join-prime basis" normalization; strictly improves in complete chains such as [0,1].

Let A,B be frames, S⊆A×B an arbitrary lower rectangular relation. H and V are the coordinatewise arbitrary join saturation operators, and C(S) denotes least lower relation containing S closed under both H and V (the coproduct-frame tensor closure).

For a complete lattice A define the totally-below relation c ◁ a iff for EVERY family {a_i} (not just directed), a≤∨_i a_i implies c≤a_i for some i. A is completely distributive iff every a is the join of its totally-below elements (Raney's characterization; valid for complete lattices).

THEOREM. If first-coordinate frame A is completely distributive, then
    C(S)=H(V(S)).
Thus whenever a⊠b≤∨_{(u,v)∈S}u⊠v in A⊕B, the pair (a,b) has a horizontal-root then vertical-child separation tree of depth≤2 with leaves from S. There is NO condition on B and NO disjointness or bar hypothesis on S. Dually, if B is completely distributive, C(S)=V(H(S)). For L completely distributive and S arbitrary in L×L, both orientations separately suffice, so EVERY rectangular bar has rank≤2.

PROOF. Put R=H(V(S)). R is H-closed by definition and lower. It remains to show V-closure. Suppose (a,b_i)∈R for i∈I. By membership in H(V(S)), for each i there is a horizontal cover a=∨_{j∈J_i}a_{ij} with (a_{ij},b_i)∈V(S). Let c ◁ a. For each i, total-below gives j_i∈J_i with c≤a_{ij_i}, hence (c,b_i)∈V(S). Since V(S) is V-closed, (c,∨_i b_i)∈V(S). Because A completely distributive, a=∨_{c◁a}c. Take the horizontal join of these pairs to get (a,∨_i b_i)∈H(V(S))=R. Thus R is both H- and V-closed. It contains S, so equals C(S). The tensor correspondence says (a,b)∈C(S) iff a⊠b≤∨_{S}u⊠v. Proof complete.

EXAMPLE WHICH IS NOT COVERED BY OLD SUFFICIENT CONDITIONS. L=[0,1] as a complete chain (join sup, meet min) is a frame and completely distributive (each a>0 is sup of c<a, and c<a is totally below a). It has NO nonzero completely join-prime elements: any c>0 is sup of a strictly increasing sequence c_n<c, and no c_n≥c. It has NO nonzero compact elements by the same argument (in particular 1 is not compact). It is NOT regular: for 0<a<1, every c>0 has c*=0, so no nonzero c≺a and regular approximation fails. Nonetheless every rectangular cover of L⊕B (arbitrary frame B) normalizes H→V in two stages, and every bar on L has rank≤2 in both orientations.

This theorem is stronger than regular-frame bar-specific depth2 in a different direction: completely distributive A controls all rectangular tensor covers, with arbitrary B, not merely bars or diagonal cover data. It is weaker in hypothesis than the earlier join-dense completely join-prime assumption but stronger than continuity (continuous only guarantees three levels).

Source for Raney characterization (distinct from the new two-stage theorem): Huth–Jung–Keimel, 'Linear types and approximation' §5.1, https://achimjungbham.github.io/pub/papers/Huth-Jung-Keimel-2000-Linear-types-and-approximation.pdf ; also Rosebrugh–Wood, TAC 13 (2004). Mathematical proof above self-contained once Raney's characterization is granted.

Important caution: C(S)=HV(S) for completely distributive FIRST factor A; for B completely distributive the orientation reverses, and in general complete distributivity of only ONE factor does not imply BOTH orientations. We do not assert any arbitrary-frame bar depth-three result, nor a rank-four construction.
