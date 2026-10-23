# Compact irreducible cores yield depth-two uniformization under bounded character
22 October 2026.

Let L=O(X) frame and S=D∪B any lower starting rectangle relation whose tensor-open join is top in L⊕L. Let K↪X be a nonzero COMPACT IRREDUCIBLE sublocale. Irreducible here means if i*(u∨v)=1_K, then i*u=1_K or i*v=1_K, i.e. its neighborhood filter F_K is prime under finite joins. Since K is compact, F_K is completely prime under arbitrary joins: if i*(∨_j u_j)=1_K, compactness gives finite subcover and irreducibility picks one member. As usual, F_K is a filter under finite meets.

Assume the neighborhood filter F_K has a cofinal family (a_i)_{i∈I} with |I|≤κ, and 1_L is κ-compact (every ≤κ indexed open cover has a finite subcover).

THEOREM. Then K has an OPEN neighborhood a with a H→V tree of edge depth≤1 below (a,1), i.e.
  1 = ∨{v:(u,v)∈S, a≤u}.
Such a is an H→V-good first-coordinate open.

Proof of leaf fiber cover: Pull back the tensor open cover to K×X. By compact-first-coordinate tube theorem, (1_K,1_L) has a V→H proof with restricted leaves (i*u,v). For every second-coordinate open b in that proof's vertical root cover, there is a horizontal cover of 1_K by opens i*u_j from S with b≤v_j. Irreducibility and compactness imply ONE of those i*u_j=1_K. Hence some S-leaf (u_j,v_j) has u_j∈F_K and b≤v_j. Thus
  1=∨{v:(u,v)∈S,u∈F_K}.
For every such leaf choose some a_i∈F_K with a_i≤u. Let
 F_S(a)=∨{v:(u,v)∈S,a≤u}.
Then 1=∨_i F_S(a_i). Top κ-compactness extracts finitely many i_1,...,i_n for which 1=∨_{j=1}^n F_S(a_i_j). Put a=∧_{j=1}^n a_i_j∈F_K. Because a≤a_i_j, F_S(a)≥F_S(a_i_j) for all j, hence F_S(a)=1. This is a one-step V cover by original leaves, with a neighborhood of K.

GLOBAL COROLLARY. Suppose L has κ-compact top and a jointly covering family of compact irreducible sublocales K_t each of character ≤κ. Then EVERY rectangular bar has H→V proof of depth at most TWO: choose first-root H-cover by the good neighborhoods a_t and then vertical leaves. No local compactness/continuity assumption on L needed.

SPATIAL COROLLARY. If X is T1 or sober spatial, first-countable, and countably compact, then each point sublocale K={x} is compact irreducible, has countable neighborhood base, and these point sublocales jointly cover X (spatiality). Hence every rectangular bar on O(X) has rank≤2. More generally point character≤κ plus κ-compact top suffice. This strengthens the previous bounded-character compact-core result from rank3 to rank2 for point/irreducible cores.

The theorem uses a cover of the LOCALIC product, not an assertion of its spatiality. The pullback to K×X and compact-source tube theorem give the right second-coordinate coverage in any ambient locale. No all-frame universal depth-three claim.
