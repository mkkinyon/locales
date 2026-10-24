# Project A — Finite Cantor–Bendixson bridge height bounds graph-null bar rank

23 October 2026. A direct, uniformly-all-n corollary of the relative non-local-compactness derivative theorem, with precise hypotheses. No new strict fitted stage.

## Theorem

Let X be a topological space containing two disjoint open copies L_0,R_0 of the rational line Q. Let B=X\(L_0∪R_0), a CLOSED subset. Let g:Q→X×loc X be the rational index graph g(t)=(ell_t,r_t), and q its greatest g-null open. Assume:

(i) For every x∈X there is an open neighborhood a_x∋x such that a_x⊠a_x≤q and
   cl_R((a_x)_L) ∩ cl_R((a_x)_R) ∩ Q=∅.
These are graph-null self-neighborhoods whose two rational traces have NO COMMON RATIONAL point in their real closures. This is stronger than mere graph-nullness, and must not be suppressed.

(ii) The CLOSED boundary B has finite Cantor–Bendixson height h, i.e. B^(h)=∅ with B^(0)=B and B^(j+1)=(B^(j))' (relative nonisolated points, in the subspace B).

Then q is automatically a localic bar with
     **rk(q) ≤ 2h+2.**
If B^(h−1) is compact and h≥1, one obtains rk(q)≤2h+1.

## Proof

For any u⊆a_x define K_L(u)=cl_X(u)∩cl_X(u^L), where u^L=r[u_L] is the right-sheet copy of the first-left rational trace. This is precisely the one-stage bad second fiber for S=D∪B_q.

For ell_s∈L0, because L0 is open and disjoint from R0, ell_s∉cl_X(u^L). For r_s∈R0, r_s∈cl_X(u) iff s∈cl_Q(u_R), and r_s∈cl_X(u^L) iff s∈cl_Q(u_L). Since u⊆a_x, this would put s in the forbidden intersection cl_R((a_x)_R)∩cl_R((a_x)_L)∩Q. Hence
    K_L(u)⊆B for EVERY u⊆a_x.
This uses neither Hausdorffness nor product spatiality. Symmetrically the same holds for K_R(u).

For any closed subspace F⊆X, let D(F) be its non-locally-compact point locus. Every isolated point of F has the compact neighborhood {point}, hence D(F)⊆F' (relative derived set). If A⊆F is closed, its derived sets satisfy A'⊆F' and its nonlocal-compactness derivatives are closed; inductively
   D^j(B)⊆B^(j).
Therefore D^h(B)=∅ by (ii).

Apply the previously proved UNIFORM RELATIVE RANK THEOREM to a=a_x,b=X, controlling closed set F=B and bad fibers K_L(u)⊆B. Since D^h(B)=∅, the rooted rectangle (a_x,1) has an alternating V-first separation tree of depth at most 2h+1. The opens a_x cover X, so a horizontal root gives a tree of depth at most 2h+2, proving q∨d_I=1 in the frame coproduct.

If B^(h−1) compact then D^(h−1)(B)⊆B^(h−1) compact, giving relative rooted rank≤2h and global rank≤2h+1.

## Existing constructions

- The original closed-discrete rational bridge boundary has CB height h=1. The theorem gives q rank≤4 (the explicit stronger H–V–H certificate gives exact rank3). Its lower bridge neighborhoods can be chosen with disjoint rational-trace closures; the rational-sheet points have neighborhoods contained in one sheet.
- The externally audited two-index bridge boundary has CB height h=2. Every lower bridge is isolated in B, while each upper t_k is a limit of lower z_(k,m,l); the set of t_k is discrete in B. The interval conditions (the two real trace closures meet only at irrational gamma_(k,m),lambda_k) give hypothesis (i). The theorem gives q rank≤6; the dedicated certificate gives exact rank4. Thus this general theorem is a uniform structural bound, NOT a sharp restatement of those exact examples.

## Implications for the full fitted-rank program

If one tries to disprove V_fin=V with a rational graph-null bar on a space satisfying (i), the boundary B CANNOT have finite CB height; otherwise q is finite rank with a fixed uniform bound. A hereditary family q_J with arbitrarily large finite rank for each parameter interval requires either increasing/unbounded CB height in the boundary, or failure of the uniform separated-trace self-neighborhood hypothesis.

This singles out genuinely infinitary nonisolated-point geometry as a necessary ingredient for such a route to Question A. The converse is FALSE in general: a high boundary CB height does not force high bar rank, as the iterated fan examples and independent fitted-hull collapse phenomena emphasize. The theorem alone provides no rank-raising operator.

References: A-V-all-finite-ranks-frontier-nonlocal-compactness-derivative-2026-10-23.md; A-V-all-stage-compact-fiber-derivative-obstructions-2026-10-23.md.
