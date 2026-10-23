# Exact fourth-stage root test for symmetric rectangular bars
22 October 2026.

Let L be any frame, w∈L⊕L with tau(w)=w and d∨w=1. Let S=D∪B_w (symmetric lower relation), H,V be one-round horizontal/vertical join closure. Define Φ(a)=∨{b:(a,b)∈H(S)}, and p_b=∨{a:b≤Φ(a)}. Then T=H(V(H(S)))={(a,b):a≤p_b}. In particular p=p_1 is the join of all H-V-H good first-coordinate opens, and rank≤3 iff p=1.

Let R_0=S and R_{n+1}=H(R_n)∪V(R_n), where each union is set-theoretic. Idempotence and inflationarity imply R_3=T ∪ tau(T): adjacent same-orientation covers flatten; R_3 consists of all rectangles admitting arbitrary height≤3 certificates. (For general non-symmetric S replace tau T by V H V S.)

Define q=∨{b∈L:p_b=1}. Then
  (1,1)∈V(R_3) iff p∨q=1.
Indeed eligible second opens b with (1,b)∈R_3 are precisely those with (1,b)∈T, equivalently p_b=1, or (1,b)∈tau T, equivalently (b,1)∈T, i.e. b≤p. Their join is q∨p. Since R_3 is symmetric, (1,1)∈H(R_3) iff (1,1)∈V(R_3). Therefore
  rank(S)≤4 iff p∨q=1.
And **rank(S)=4 iff p<1 and p∨q=1** (assuming S is a bar and minimum finite height convention).

The sets G={a:Φ(a)=1} and Q={b:p_b=1} are BOTH lattice ideals: G as finite-join interchange; Q because b↦p_b maps finite joins to meets. Hence both p,q are directed ideal joins. This formula is stronger than an arbitrary infinitary interchange statement and gives an exact rank-four algebraic test in any symmetric bar.

No proof that p∨q=1 follows from barhood. No rank-four example. Note that a rank-four tree can mix H-V-H and V-H-V subtrees; pure alternating four-stage formulas ALONE need not capture this mixture. This calculation explicitly accounts for mixed branches.

If w not symmetric, the R_3 decomposition is T_HVH ∪ T_VHV and no simple p∨q symmetric test; initial root orientation matters.
