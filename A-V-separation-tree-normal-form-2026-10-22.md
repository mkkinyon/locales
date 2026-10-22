# Separation-tree normal form for rectangular bars
22 October 2026. Exact positive proof calculus for V; **normal form only, not yet a non-tautological simplification of fit(I)**.

Let L be any frame and R=L×L. Let D={(a,b):a∧b=0}. For B⊆R, define rectangular C-ideal closure ⟨D∪B⟩_C: lower set, separately join-closed in both coordinates. B is a rectangular bar iff (1,1)∈⟨D∪B⟩_C, equivalently (∨_{(a,b)∈B}a⊠b)∨d_I=1 in T=L⊕L.

**Definition:** A B-separation tree is a well-founded rooted tree with labels (a,b), root (1,1), with (i) D leaf if a∧b=0, (ii) B leaf if ∃(u,v)∈B, a≤u,b≤v, (iii) horizontal cover node (a,b) whose child labels are (a_i,b) with a=∨_i a_i, or (iv) vertical cover node with children (a,b_i) with b=∨_i b_i. Empty indexed joins allowed (yield only 0-coordinate labels, already D leaves).

**Completeness theorem:** B bar iff there exists B-separation tree. Let P be all labels having a well-founded B-proof tree (not just root). P contains D∪B, is lower since restriction of coordinate labels by (a',b')≤(a,b) can be propagated down every join via distributivity a'∧∨a_i=∨(a'∧a_i), and similarly second coordinate, and is separately join-closed by grafting roots. Hence ⟨D∪B⟩_C⊆P. Conversely well-founded induction on a tree's nodes proves all its labels are in ⟨D∪B⟩_C. Thus equality.

**Alternation normal form:** Given proof tree, recursively replace every horizontal child of a horizontal parent by all its children (and similarly vertical). Since ∨_i∨_j a_ij=∨_{i,j}a_ij, this retains labels and well-foundedness (flattening cannot create infinite branches; a path in a flattened tree expands to a path in original tree). Formal recursion on well-founded rank gives a tree with no adjacent same-axis internal nodes. Every cover may be chosen exact as in definition (an original inequality a≤∨a_i may be trimmed to a_i∧a). Roots of either orientation permitted.

**Rank:** define rank of leaf 0 and rank internal 1+sup(rank child), i.e. sup{rank(child)+1}; ranks can be transfinite. No proof that alternating trees admit a finite-rank uniform bound in arbitrary frames. If tree is finitely branching and well-founded, it is finite by König's lemma, so infinitely branching cover nodes are indispensable for genuinely infinitary witnesses. This does not itself prove a lower bound on the ranks necessary in concrete examples.

**Exact V formula:** V=∧_{B admitting alternating B-separation tree}O(∨_{(a,b)∈B}a⊠b). This follows from the bar theorem and the rectangular coproduct C-ideal presentation. The formula remains equivalent to indexing by all frame coproduct opens w with w∨d_I=1; it is a coordinate-only proof calculus, not yet a satisfactory structural dual of U. Next seek rank-reduction, canonical deterministic trees, or a proper subclass of trees complete for all L. A finite-rank collapse must be proved, not assumed.

**Caution:** horizontal/vertical labels describe *covers*, not necessarily disjoint partitions (frames need not be Boolean). In graph counterexamples the failure is not simply finite vs infinite branches, but iterated saturation by join operations. 
