# Compact sublocale tube filters and a conditional lifting theorem
22 October 2026

Let L be a frame, w∈L⊕L with d∨w=1, h_w(b)=b*∨r_w(b), Φ_w(a)=∨{b:a≤h_w(b)}, and G_w={a:Φ_w(a)=1}. Let i:K↪X be a compact sublocale, with restriction i*:L→O(K).

THEOREM (compact-sublocale fiber cover). Then
    1=∨{b∈L:i*(h_w(b))=1_K}.
Proof. S=D∪B_w is a rectangular covering family in L⊕L. Apply i*⊕id to obtain a rectangular top cover of O(K)⊕L. The previously proved compact-first-coordinate tube normalization (K compact) gives a V→H certificate for (1_K,1_L) from the restricted leaf family. Therefore its second-coordinate root cover is exactly contained in {b:i*(h_w(b))=1_K}, which consequently joins to 1.

THEOREM (filter-uniformization sufficient condition). Let F_K={u∈L:i*(u)=1_K}, the neighborhood filter of K. Suppose some subfamily {b_j:j∈J} satisfies ∨_j b_j=1, h_w(b_j)∈F_K, and there exists a∈F_K with a≤h_w(b_j) for every j. Then Φ_w(a)=1, so a∈G_w and contains K. This is immediate from definition of Φ.

CARDINAL COROLLARY. Suppose 1_L has the λ-Lindelöf property: any cover of 1 has a subcover of cardinality <λ, and F_K is <λ-complete in the sense that any <λ family in F_K has a COMMON LOWER BOUND a∈F_K. Then K has a good open neighborhood. If compact sublocales satisfying these hypotheses jointly cover X as sublocales (i.e. X is their join), their good neighborhoods join to 1, and (*) holds. This generalizes the local proof pattern for Lindelöf P-spaces but is explicitly conditional and does not establish (*) in arbitrary frames.

STRUCTURAL OBSTRUCTION. F_K is Scott-open: if a directed family joins to u∈F_K, compactness of K implies some family member belongs to F_K. Scott openness is NOT closure under infinite meets. In particular a compact singleton in Q has neighborhood filter with no common open lower bound for the countable decreasing family (-1/n,1/n)∩Q. Therefore one cannot extract a common first-coordinate neighborhood from compactness of K alone.

PRINCIPAL-NEIGHBORHOOD NO-GO. If F_K has a least member a (i.e. K has a smallest open neighborhood a), then a is a compact OPEN element of L: if a≤∨_i u_i, the u_i cover K; K compact gives a finite subcover u_i covering K; since a is least neighborhood, a≤∨_{i in finite}u_i. Thus trying to upgrade the compact-sublocale theorem by assuming the neighborhood filter principal gives no genuinely weaker compactness class than the prior compact-open theorem.

STATUS. The compact-sublocale restriction itself gives strong uniform coverage of K on the second coordinate, but it does not produce a single open a∈G_w unless a COMMON NEIGHBORHOOD refinement is available. It is not known whether the bar equation forces such uniformization absent an auxiliary filter-completeness hypothesis. Universal depth 3 and rank≥4 examples remain unresolved.
