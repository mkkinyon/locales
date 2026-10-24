# Project A — All-stage compact-fiber obstruction calculus

23 October 2026. **New working theorem with self-contained proof.** This strengthens the transposed-closure derivative and provides a uniform necessary condition for EVERY finite fitted-rank jump. It is not a construction of new strict stages and does not decide Question A.

## 1. Setup and exact derivative recursion

Let X be an ordinary topological space; L=O(X), Q=L⊕L. Let q∈Q be any BAR q∨d_I=1 and S its canonical lower leaf family: disjointness leaves plus q-rectangles. For opens u,v put
  K_L(u)=X\⋃{v:(u,v)∈S}, K_R(v)=X\⋃{u:(u,v)∈S}.
These are monotone, closed-set-valued functions.

For any monotone closed-valued K define
  (T K)(b)=X\⋃{a open:b∩K(a)=∅}.
Both monotonicity and closed-valuedness are preserved. The alternating proof-tree calculus gives
  (a,b)∈V(S) iff b∩K_L(a)=∅;
  (a,b)∈H(V(S)) iff a∩(T K_L)(b)=∅;
and analogues after arbitrarily many alternating levels. The right-first orientation starts with K_R.

For EVERY such K (no barhood hypothesis) T²K≤K, hence
  T^(k+2)K≤T^kK for all k≥0.
This splits the stages into descending even and odd chains.

## 2. Empty stalks at EVERY finite stage

**LEMMA (barhood forces empty local kernel stalks).** For each x∈X,
  ⋂_{a open, x∈a} K_L(a)=∅,
  ⋂_{a open, x∈a} (T K_L)(a)=∅.
The same holds starting from K_R. Consequently, for every k≥0,
  ⋂_{a∋x} (T^k K_L)(a)=∅,
  ⋂_{a∋x} (T^k K_R)(a)=∅.

Proof. Given x,y, evaluate q∨d_I=1 at the ordinary product point (x,y), getting a leaf rectangle (u,v) containing (x,y). Then y∉K_L(u), proving the first stalk identity; and v∩K_L(u)=∅, so u occurs in the union defining (T K_L)(v), hence x∉(T K_L)(v), proving the second, with the dummy variable relabeled. The other orientation is symmetric. Since even powers of T are below K, and odd powers below TK, all higher intersections vanish. No identification of Q with the ordinary product topology is needed.

## 3. Uniform all-stage compact-fiber theorem

**THEOREM.** Let X be FIRST-COUNTABLE and q any bar. Fix k≥0 and choose either the L or R closure kernel K. If
  (*_k) for EVERY x∈X there exists an open a∋x for which (T^k K)(a) is COUNTABLY COMPACT (as a subspace of X),
then q has a separation tree of depth at most k+2, in the orientation determined by K and parity k.

Proof. Fix x and choose a decreasing countable local base a_n at x with a_0 contained in the a given by (*_k). The closed sets F_n=(T^kK)(a_n) are decreasing, all closed in the countably compact F_0, and ⋂F_n=∅ by the empty-stalk lemma. Countable compactness forces F_n=∅ for some n. When k is even, emptiness gives (a_n,1) membership in the alternating depth-(k+1) family whose bottom step is V for K_L (or H for K_R); when k is odd it gives (1,a_n) membership in the alternating depth-(k+1) family. Cover X by all these a_n and prepend the opposite coordinate root. Thus total depth≤k+2, entirely in the rectangular C-ideal calculus.

**COROLLARY (closed noncompact obstruction locus).** Define
  B_k(K)=X\⋃{a open:(T^kK)(a) is countably compact}.
Then B_k(K) is CLOSED. If rk(q)>k+2 then BOTH B_k(K_L) and B_k(K_R) are NONEMPTY (otherwise the theorem supplies one successful orientation). Moreover
  B_(k+2)(K)⊆B_k(K)
since T^(k+2)K(a) is closed in T^kK(a), and closed subsets of countably compact spaces are countably compact. Hence TWO nested sequences of closed obstruction loci:
  B_0⊇B_2⊇B_4⊇⋯ and B_1⊇B_3⊇B_5⊇⋯,
for each orientation.

This is a uniform theorem about all finite n, not a finite list of special cases. It identifies necessary *persistent, non-countably-compact bad kernels* for strict high-rank bars.

## 4. Countable Hausdorff spaces: infinite closed-discrete witness reservoirs

If X is COUNTABLE, every countably compact subset of X is compact (a countable space is Lindelof). Therefore in our countable first-countable Hausdorff bridge spaces, B_k(K) is exactly the locus whose every neighborhood a has NONCOMPACT derivative fiber T^kK(a).

More concretely, any closed non-countably-compact F in a T1 space contains an infinite CLOSED DISCRETE subset. Take a countable open cover (U_n)_n of F with no finite subcover, and choose x_n∈F\⋃_{i≤n}U_i. After deleting any finite repetitions, each point of F has a neighborhood U_i meeting only the finitely many early x_n. Thus the chosen set is locally finite and (in T1) closed discrete.

Consequently, if a bar q has rk(q)>k+2 on a COUNTABLE FIRST-COUNTABLE HAUSDORFF X, for EACH orientation there is a point x such that for EVERY neighborhood a∋x the closed set (T^k K)(a) contains an infinite closed-discrete subset. These witnesses may change with a and k; the theorem neither forces a single persistent point nor proves strictness by itself.

## 5. Hereditary fitted stage interpretation

Suppose q=q_g is the graph-null bar for g:Y→X², and q_J is the null bar for the graph restricted to any nonzero parameter open J. Suppose X is countable first-countable Hausdorff and rk(q_J)>n for EVERY nonempty basic J. Put k=n−2 (for n≥2). By the theorem, for every J and EACH orientation there exists a point x_J^direction such that EVERY neighborhood a of x has derivative fiber (T^k K_J^direction)(a) NONCOMPACT and hence contains an infinite closed-discrete subset.

If in addition rk(q)≤n+1, graph density gives j_n(q)=q<1=j_(n+1)(q), hence strict V_n⊋V_(n+1). The universal compact-fiber result is a NECESSARY geometric filter on the candidate, not a proof of the rank lower bound; the exact T-rank criterion remains necessary to establish strictness.

For a hypothetical graph bar refuting Question A (hereditarily unbounded finite ranks), this noncompact-fiber condition must hold for every n and every nonempty J. The witness x may depend on n,J,orientation and shrinking neighborhoods. A construction that tries to keep one witness fixed typically violates the original barhood pairwise leaf condition (the super-anchor no-go).

## 6. What this rules out and what it does not

- If X is first-countable and countably compact, take k=0: each K(a) is a closed subset of countably compact X, so rk(q)≤2 for EVERY bar q. In Hausdorff spaces this is also a consequence of regularity, but here no Hausdorffness is required.
- If for some k all T^kK(a) are locally countably compact (each point has a neighborhood with countably compact derivative value), q has rank≤k+2.
- If the even or odd B_k loci become empty uniformly at a finite stage for EVERY bar on X, the fitted hierarchy stabilizes there (a sufficient, not necessary condition).
- Nonempty obstruction loci or infinite discrete reservoirs do NOT imply a rank lower bound. The derivative inequalities must still be checked.
- In general a nested family of nonempty B_k can have empty intersection on non-countably-compact X; there need not be any one point witnessing all ranks.

**STATUS:** all-stage theorem proved here. No strict V4>V5, all-n fitted-stage strictness, or negative resolution of V_fin=V has been established.
