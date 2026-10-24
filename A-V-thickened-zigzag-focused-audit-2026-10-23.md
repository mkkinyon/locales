# Focused audit: almost-normal thickened-zigzag — 23 October 2026

## Scope and verdict

Independent focused re-read of A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md, checked against the frame coproduct separation-tree rules in A-V-separation-tree-normal-form-2026-10-22.md and the rank-two almost-normal theorem. **Central counterexample passes.** This is a limited internal audit, NOT a blind external referee report and NOT a novelty or publication-readiness claim.

Verified working result for the five-point zigzag P=(p<u, r<u, r<v, q<v):

  X(P) is countable, T0, noncompact, almost normal;
  I(X(P)) ⊊ V(X(P)) ⊊ U(X(P))=F(X(P));
  V(X(P)) is not closed.

The strict V⊊U conclusion relies on the separate rank-two theorem V2=U=F for almost-normal frames; its proof was examined at the level of the existing note, not re-refereed exhaustively here.

## Checks

1. **Irrational coordinates.** Select distinct irrational cosets alpha_p+Q, and enumerate each densely (indeed every tail dense). All alpha_(p,n) are distinct. Each ↑_B(p,n) is finite, and each ↓_B(p,n) is an infinite descending tail possibly with finitely many P-coordinates.

2. **Filter criterion.** For T⊆Q, alpha irrational,
  every G∈G_alpha meets T iff alpha∈cl_R int_R cl_R(T).
If alpha is outside cl int cl T, choose interval J about alpha disjoint from int cl T. Then T∩J is nowhere dense in R after shrinking to a smaller interval with closure inside J; subtract N=cl_R(T∩J')∩Q to construct a filter trace avoiding T. Conversely if alpha∈cl int cl T, every neighborhood J of alpha contains a nonempty subinterval on which T is dense; deleting any nowhere dense N cannot remove all of T there.

3. **Closure formula.** For open A with boundary upset H and rational trace T, b∈cl_X A iff ↑b∩H nonempty or some alpha_c with c∈↑b lies in Sigma(T). Necessity uses the finite collection ↑b to combine finitely many rejecting filter traces into a legitimate neighborhood missing A. Sufficiency follows from every neighborhood of b containing all ↑b and belonging to each G_alpha_c.

4. **Almost-normality.** If Sigma(T_A)=∅ then A⊆S and cl A=A; A clopen. Otherwise int cl(T_A) nonempty, meeting arbitrarily far-down attachment coordinates in every P-chain, forcing any open C⊇cl A to contain all B and hence be clopen. Thus for A≺C one endpoint is clopen, a valid interpolant. No product spatiality.

5. **H–V–H bar.** With A_b=↓_B b,A_c=↓_B c and no common-upper predecessor pair, define w=(e_b⊠1)∨(1⊠e_c). Root cover e_b plus neighborhoods U_a (a∈A_b); middle cover e_c plus V_(a,d) (d∈A_c), whose finite traces have closures avoiding attachment coordinates of ↑a; final split
  U_a = H_(a,d)∨E_(a,d)
where H has boundary ↑a and trace T_a\cl_R T' and E is isolated only with trace T_a∩cl_R T'. H is open, H∧V_(a,d)=0, and E⊆S⊆e_b. This is a valid three-level frame-coproduct certificate w∨d_I=1. Its point (b,c) lies outside O(w), hence outside V.

6. **Nonclosedness witness.** Put b=(p,0),c=(q,0),u0=(u,0),v0=(v,0),r0=(r,0). The lower pair (b,c) is barred. The higher (u0,v0) belongs to all bars because (r0,r0)≤(u0,v0). Yet (b,c)≤(u0,v0), violating downward specialization closure of any closed sublocale. Moreover u0,v0 have disjoint basic neighborhoods, so higher pair is outside I. Hence I⊊V nonclosed. Strict V⊊U follows since U is closed and contains V by AN1.

7. **Noncompactness.** For minimal p, the closed descending tail ↓(p,0) is covered in X by countably many basic neighborhoods with finite intersection with this tail, plus its open complement; no finite subcover.

## Secondary claims (§6)

B=P×omega^op is sober and locally compact: a principal upset is finite and compact; a nonempty irreducible closed directed lower subset has a greatest point by minimal-index/maximal-P-coordinate argument. X is sober because isolated s_t are clopen and irreducible closed subspaces of B are sober. X is scattered by minimal index + maximal P-coordinate isolation; finite products of scattered spaces are scattered. The localic square is spatial using the open S×S block, its complementary closed join of B×X and X×B, locally compact-factor spatiality, and stability of spatiality under joins of sublocales. For scattered spatial frames all sublocales are spatial (see Niefield–Rosenthal 1987, Picado–Pultr 2019, and Suarez 2022). Thus the additional claim V=V3 by point determination is credible and passes this proof-sketch check, but **its complete classification for arbitrary finite P was not independently rederived with the same thoroughness as the central bar witness**; preserve its working status.

One presentation improvement: the phrase 'T∩J is nowhere dense' when alpha lies outside Sigma needs the interval J to be chosen inside an open neighborhood missing cl int cl T and preferably a slightly smaller subinterval with closure contained there, so the nowhere-dense deletion is demonstrably global in R. This is an expository clarification, not a gap.

## Status and next priority

Central example: **passes focused internal audit**; external independent audit still welcome. Auxiliary global V=V3 and finite-P classification: **working / partial focused check**.

The current Project A priority returns to constructing a genuine fitted-rank jump V3 ⊋ V4 via a graph-density witness. High individual bar rank is not sufficient; require nonzero closed R meeting all rank≤3 bars densely while killed by a rank-4 bar. Do not confuse V_fin=V with individual finite-rank boundedness.

No Hochster duality conclusions are used: the thickened zigzag is noncoherent, so Hochster reversal is only analogy, not a functor available on this class.
