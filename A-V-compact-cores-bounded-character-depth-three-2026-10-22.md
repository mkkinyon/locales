# Bounded-character compact cores yield universal depth three
22 October 2026

Let L be a frame, w∈L⊕L a canonical bar with d∨w=1, h_w(b)=b*∨r_w(b), Φ_w(a)=∨{b:a≤h_w(b)}, G_w={a:Φ_w(a)=1}. Let K↪X be a compact sublocale with neighborhood filter F_K={u:i* u=1_K}. Compact-source tube theorem yields
  1=∨{b:h_w(b)∈F_K}.

Fix infinite cardinal κ. Assume:
(A) TOP κ-COMPACTNESS: every family (v_i)_{i∈I} of ≤κ opens of L with join1 has a FINITE subfamily with join1.
(B) CHARACTER OF K ≤κ: F_K has a cofinal family (a_i)_{i∈I}, |I|≤κ: each a_i∈F_K, and for every u∈F_K some a_i≤u.

THEOREM: Under (A)(B), K has an open neighborhood a∈G_w (i.e. Φ_w(a)=1 and i*(a)=1_K).

Proof: For every b with h_w(b)∈F_K, choose/there exists i with a_i≤h_w(b). Then b is among terms defining Φ_w(a_i). Thus
  1=∨_{b:h_w(b)∈F_K}b≤∨_iΦ_w(a_i).
By κ-compactness of top, some finite indices i_1,...,i_n satisfy ∨_{k=1}^nΦ_w(a_i_k)=1. Put a=∧_{k=1}^n a_i_k; filter closure gives a∈F_K. Since a≤a_i_k, antitonicity gives Φ_w(a)≥Φ_w(a_i_k) for each k, so Φ_w(a)=1.

GLOBAL COROLLARY: If a jointly covering family of compact sublocales K_j has character ≤κ and the top of L is κ-compact, then ∨G_w=1 for every bar w, hence universal H-V-H depth≤3 on L. If the join of the sublocales is X and K_j≤O(a_j) with good open neighborhoods, then ∨a_j=1 because their open join contains the sublocale join X.

SPATIAL COROLLARY: If X is a spatial T1 locale, countably compact (every countable open cover has a finite subcover), and first-countable (each point has countable neighborhood base), then the singleton sublocales are compact, their neighborhood filters have countable cofinal bases, and their join is X. Therefore every canonical rectangular bar has depth≤3. More generally replace countable by any infinite κ and first countability by point-character ≤κ with κ-compactness of the top.

The proof applies to arbitrary bar leaf families S=D∪B as well, since compact K fiber theorem holds with h_S(b)=∨{u:(u,b)∈S}. It therefore gives depth≤3 for arbitrary rectangular bars (not just canonical) subject to the stated frame conditions.

This is a genuinely different finite-uniformization principle from continuous-frame/compact-open basis: we trade a global approximation basis for limited-size open-cover compactness and small neighborhood character. No claim that all first-countable countably compact frames are noncontinuous; examples of independence should be separately verified.

CAUTION: This does not prove (*) for arbitrary frames, since infinite second-coordinate covers may have no small subcover or compact sublocale neighborhoods may have very large character. For K={0} in Q, F_K has countable cofinal basis but the top of O(Q) is not countably compact (the obvious increasing cover by bounded intervals has no finite subcover).

SOURCES: earlier internal compact-first-local-tube theorem A-V-compact-coordinate-local-tube-normalization-2026-10-22.md and compact-sublocale restriction A-V-compact-sublocale-filter-uniformization-2026-10-22.md.
