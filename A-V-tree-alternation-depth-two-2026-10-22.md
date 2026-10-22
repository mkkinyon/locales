# Separation-tree alternation: failed interchange and a depth-two collapse
22 October 2026.

## Failure of naive cover interchange
To commute arbitrary horizontal/vertical split levels via choice functions requires complete distributivity:
  ∧_{i∈I}∨_{j∈J_i}b_ij = ∨_{f∈∏J_i}∧_{i∈I}b_{i,f(i)}.
Frames need not satisfy it. Explicit in L=O(R): U_n=(-∞,1/n), V_n=(-1/n,∞). Each U_n∨V_n=1, hence ∧_n(U_n∨V_n)=1. However for any choice f∈2^N, the intersection of chosen U_n or V_n has no open neighborhood of 0; therefore ∨_f∧_n W_{n,f(n)}=R\{0}≠1 (the all-U and all-V choices cover the negative and positive halves). This invalidates this particular depth-two normalization argument, but does NOT prove a strict alternation hierarchy.

## Positive rank-two theorem: supercompact basis
Let P⊆L be join-dense and consist of completely join-prime elements, i.e. p≤∨_i a_i implies p≤a_i for some i (including empty joins). Then **every rectangular bar B⊆L×L has a B-separation tree of depth at most 2**:
- root (1,1) split horizontally to (p,1), p∈P (since ∨P=1);
- split each (p,1) vertically to (p,q), q∈P (since ∨P=1);
- each (p,q) is a leaf justified by D or B.

Proof: For p∈P, the filter F_p={a∈L:p≤a} is completely prime, defining a point ε_p:L→2. Let ε_p×ε_q be the resulting localic-product point T=L⊕L→2. Since B is bar, 1=d_I∨b_B, so this point evaluates some rectangle from D or B to 1. A contributing D rectangle a⊠b has p≤a,q≤b,a∧b=0 and hence p∧q=0, making (p,q) a D-leaf. A contributing B rectangle a⊠b has p≤a,q≤b, making (p,q) a B-leaf. No point spatiality assumption on T necessary; we only use the specific canonical points coming from join-prime basis elements.

**Corollary:** Every frame of upsets O(P) of an arbitrary preorder P (Alexandrov frame) has the rank-two property, since principal upsets ↑x are completely join-prime and form a join-dense basis. The theorem applies to noncompact/noncoherent/non-ACC examples too.

This is a real simplification of the infinitary separation-tree formula (unlike mere flattening), but it does not settle general rank collapse. Note especially that O(R) lacks a join-dense completely join-prime basis; the displayed failure of complete distributivity is only an obstruction to the naive proof method, not a counterexample to depth-two bar completeness.

## Next
Need a frame L and explicit rectangular bar B forcing alternation depth ≥3, or prove a broader rank-reduction theorem using other structure. Search for an invariant of sets obtainable by rank-two H→V and V→H trees, and try to distinguish it from the full C-ideal closure. Do not claim rank hierarchy strict without explicit witness.
