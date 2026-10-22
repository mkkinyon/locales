# Exact finite-depth tests for rectangular separation trees
22 October 2026. A negative search result, with an exact recursive test; no strict depth-two counterexample obtained.

Fix L, B, D={(a,b):a∧b=0}, and S=down(D∪B). Define R0=S. For n≥0 let H(Rn)={(a,b): a≤∨{x:(x,b)∈Rn}}, and V(Rn)={(a,b): b≤∨{y:(a,y)∈Rn}}; after taking downward closure as needed. These sets are exactly the labels admitting a proof of height ≤n+1 whose top step is horizontal (H) or vertical (V) relative to Rn. Define R_{n+1}=H(Rn)∪V(Rn), with lower closure; note union is not join-closed in general, which is why repeated stages matter. Then (1,1) belongs to R2 iff bar has a tree of height ≤2; to require an *alternating H→V or V→H* normal form use H(V(S)) ∪ V(H(S)), along with shallower trees. Because S is already lower, horizontal followed by horizontal can be flattened into a single H step, likewise V/V. So depth-two criterion is (1,1)∈ H(V(S)) ∪ V(H(S)), equivalently ∨{a:V0(a)=1}=1 or ∨{b:H0(b)=1}=1, with V0(a)=∨{b:(a,b)∈S} and H0(b)=∨{a:(a,b)∈S}.

Depth three has a similarly exact criterion using H(V(H(S))) or V(H(V(S))) plus lower-depth cases. Define h0(b)=∨{a:(a,b)∈S}. The labels (a,b) in H(S) are precisely a≤h0(b); a vertical split of (a,1) into horizontal-splittable children exists iff ∨{b: a≤h0(b)}=1. Thus root horizontal, vertical, horizontal of depth 3 exists iff
  ∨{a∈L: ∨{b∈L: a≤h0(b)}=1}=1.
The symmetric formula follows by exchanging coordinates. These tests are valid for any frame, and do not assume spatiality of X or the localic square.

WARNING: Existence of a bar still means transfinite closure of S reaches (1,1). Finding strict finite depth >2 requires exhibiting an explicit frame L, bar B, and verifying failure of both depth-two conditions, not merely formal configurations of arbitrary monotone h and v (which may not be realizable by lower(D∪B)).

Earlier rank-two positive classes: regular frames, frames with join-dense completely join-prime basis, compact spatial locales. A strict counterexample must avoid each. Candidate Scott chain attempts not resolved; do NOT record a counterexample or universal positive result.
