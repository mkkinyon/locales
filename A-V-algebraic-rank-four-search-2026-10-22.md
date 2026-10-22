# Algebraic search for rank four in rectangular C-ideal closures
Date 2026-10-22. Research checkpoint: exact rank-four algebraic test, NOT a rank-four example.

Let L be a frame, B⊆L×L, D={(a,b):a∧b=0}, and S=↓(D∪B). For any lower R⊆L×L set
  f_R(a)=∨{b∈L:(a,b)∈R},  g_R(b)=∨{a∈L:(a,b)∈R}.
Both maps are antitone (as a decreases, f_R(a) increases, etc). Horizontal and vertical one-step saturation can be defined algebraically by
  V(R)={(a,b):b≤f_R(a)}, H(R)={(a,b):a≤g_R(b)}.
They contain R and are lower; H and V are individually idempotent. For S=↓(D∪B):
  f_S(a)=a* ∨∨{v:(u,v)∈B,a≤u};
  g_S(b)=b* ∨∨{u:(u,v)∈B,b≤v}.
Define depth stage R_0=S and R_{n+1}=H(R_n)∪V(R_n). The union is lower (not in general H/V-closed). Then (a,b)∈R_n iff it admits a separation-tree certificate of edge-depth at most n. Induction uses the fact that a node can be covered horizontally or vertically by children with depth ≤n. In particular rank>3 is equivalent to (1,1)∉R_3. A rank exactly 4 bar needs (1,1)∈R_4\R_3.

For orientation-specific tests:
- depth 2 H→V: 1=∨{a:f_S(a)=1}; depth 2 V→H:1=∨{b:g_S(b)=1};
- depth 3 H→V→H: 1=∨{a:∨{b:a≤g_S(b)}=1}; transposed V→H→V swaps f,g.
- depth 4 H→V→H→V: take g_{V(S)}(b)=∨{a:b≤f_S(a)} and then require
  1=∨{a: ∨{b:a≤g_{V(S)}(b)}=1}.
  (Other orientation obtained by symmetry.)
All lower-depth trees automatically permitted by allowing trivial/flattened cover nodes. For full rigor, checks of mixed-direction children can be reduced by concatenating leaf and shorter subtrees into an alternating normal form.

Important caution: freely inventing antitone maps f,g does not construct a frame/bar. The starting maps must have the pseudocomplement form displayed above, and the resulting S must be downward closure of all disjointness rectangles together with B. Also one must independently verify B is a **bar**, i.e., (1,1) belongs to the transfinite C-ideal closure, not merely an ordinary pointwise cover.

The existing rational-bridge B_q has (1,1)∈R_3\R_2, by explicit H-V-H proof and depth-two lower bound. It supplies the first strict rank but does NOT automatically give a rank-raising operation. A possible path is a substitution lemma showing a new frame/bar has a residual R_n encoding R_{n-1} of the old frame; no such lemma has been verified.

Conclusion: no rank-four or arbitrary finite-rank construction proved here. This is an exact algebraic specification of what remains to construct.
