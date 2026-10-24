# Project A — Strongly exact filters, segment 2: the omega bar IS recovered by regular completion

24 October 2026. **Working mathematical theorem with complete frame-valid proof.** This is the second of the bounded 2–3-segment trial of strongly exact/regular filters. The result concerns the explicit two-generic-point negative example; it does NOT prove B_fin^{##}=B for that space, nor an intrinsic formula for V. It shows something genuinely positive that the first segment could not settle: the particular rank-omega bar q missing from strongly exact completion IS present in regular completion.

## 1. Setup

Let Y=⊔_{m≥1}Z_m be the countable disjoint sum of the iterated K-fans, with each Z_m clopen and carrying disjoint nonempty closed F_m,C_m and a finite-height bar
  w_m=(Z_m\C_m)⊠1 ∨1⊠(Z_m\F_m)
of exact rank m+1. Put C=⊔C_m, F=⊔F_m. Form X0=Y⊔{ell,r} with an old-open extension E(u)=u plus ell iff u meets C and plus r iff u meets F. Let
  a0=X0\(C∪{ell}), e0=X0\(F∪{r}),
  q=(a0⊠1)∨(1⊠e0).
This q is the maximum open missing the ordinary product point p=(ell,r), a bar of exact rank omega. The full filter of bars is B={v:d_I∨v=1}; the finite-rank bars form a filter B_fin. With supplement F^#={z:∀v∈F,z∨v=1}, the earlier first-segment proof established
  q∉SEcl(B_fin)
and left open whether q∈B_fin^{##}.

**THEOREM.**
  **q∈B_fin^{##}.**
Equivalently, for EVERY open z∈O(X0×locX0),
  [z∨v=1 for every finite-rank bar v] ⇒ z∨q=1.
So the regular closure DOES recover a bar excluded by strongly exact closure. This does NOT imply that it recovers ALL bars.

The argument generalizes from the K-fan sum to ANY clopen sum Y=⊔Z_m with disjoint nonempty closed C_m,F_m each having a FINITE-rank strip bar w_m, regardless of growth of ranks.

## 2. Local finite bars on Y vanishing on entire closed component rectangles

For each pair m,n, regard C_m and F_n as closed subsets of Y and set
  a_mn=Y\C_m, e_mn=Y\F_n,
  v_mn=(a_mn⊠1)∨(1⊠e_mn) in O(Y)⊕O(Y).

**LEMMA 1.** Each v_mn is a FINITE-rank bar and restricts to ZERO on the closed sublocale C_m×locF_n.

Proof: at a horizontal root, split first coordinate by a_mn and the clopen Z_m, whose join is Y. The a_mn child is a v_mn leaf. Under the Z_m child, split second by e_mn and the clopen Z_n, whose join is Y. The e_mn child is a v_mn leaf. For m≠n the remaining (Z_m,Z_n) is a D leaf, since the components are disjoint; depth≤2. For m=n, the remaining (Z_m,Z_m) admits the old finite bar tree for w_m, as the restriction of v_mm to Z_m² equals w_m. This gives depth≤m+3. On C_m×locF_n, a_mn and e_mn both pull back to zero, so v_mn pulls back to zero. QED.

## 3. Lifting an ARBITRARY finite bar from Y to a finite bar on X0

Let v be any finite-rank bar on Y. Set
   \widetilde v = q ∨ ⋁{E(u)⊠E(t):u⊠t≤v}.
The sum is in Q0=O(X0)⊕O(X0). Its restriction along h:O(X0)→O(Y) in both coordinates is
   (h⊕h)(\widetilde v)=w∨v,
where w=(Y\C)⊠1∨1⊠(Y\F) is the old omega strip.

**LEMMA 2.** \widetilde v is a bar of finite rank ≤rk(v)+2. Moreover \widetilde v restricts to v on the old closed sublocale C×locF (and hence on each C_m×locF_n).

Proof. Transport each node (u,t) in a finite v separation tree to (E(u),E(t)). E preserves all joins, so horizontal and vertical cover equalities lift. If (u,t) is a v rectangle leaf, then E(u)⊠E(t)≤\widetilde v by its defining join. If (u,t) is a disjointness leaf, use EXACTLY the previously checked H–V repair from the graphization lemma: split u=(u∩a)∨(u∩e), then under E(u∩e) split t=(t∩a)∨(t∩e), where a=Y\C and e=Y\F. The first and last q-null leaves lie under q≤\widetilde v and the cross leaf is genuine disjointness because E(u∩e) adds at most ell, while E(t∩a) adds at most r. This produces a finite tree with at most two additional depths. In the restriction to C×locF, the open q vanishes and the remaining lifted pure rectangles restrict exactly to the pure rectangles of v. QED.

In particular for every (m,n) put \widetilde v_mn as the lift of v_mn. Then \widetilde v_mn is a **finite-rank GLOBAL bar** on X0 and has ZERO restriction to the CLOSED sublocale C_m×locF_n.

## 4. Top reflection of the old closed block inside the generic closure

Put
   A=C∪{ell}=cl{ell}⊆X0,
   B=F∪{r}=cl{r}⊆X0.
The closed sublocale C(q) of the localic square is A×locB. Inside it lies the closed sublocale C×locF, with open complement
   e=( {ell}⊠1 )∨(1⊠{r})
in O(A×locB). Restriction to C×locF is the closed quotient determined by this e.

**LEMMA 3 (top-reflection).** For every t∈O(A×locB),
   t|_(C×locF)=1  ⇒  t=1.
This holds even if A×locB or C×locF is nonspatial.

Proof. Both C and F are nonempty ordinary spaces. Choose fixed c0∈C. For EACH f∈F, because t restricts to top on C×locF, the ordinary localic product point (c0,f) lies in t. Rectangle generators yield opens U_f⊆A and V_f⊆B with c0∈U_f,f∈V_f and U_f⊠V_f≤t. Any open U_f containing c0 also contains ell, so {ell}⊠V_f≤t. The opens V_f cover all f∈F, and each V_f also contains r, so their join is top_B. Thus {ell}⊠1≤t. Symmetrically, choose fixed f0∈F and vary c∈C to get 1⊠{r}≤t. Hence e≤t. Since restriction to the closed complement of e is top, the closed-quotient relation gives t∨e=1. Therefore t=1. QED.

This is an independent useful lemma about products of spaces with OPEN GENERIC POINTS whose closures include nonempty closed old bases.

## 5. Proving q lies in regular completion

Take any z∈B_fin^#. By definition,
   z∨\widetilde v_mn=1
for every m,n.

Restrict to the closed sublocale C_m×locF_n. Since \widetilde v_mn restricts to zero there, z restricts to top there.

The old closed C×locF decomposes as a topological/localic disjoint sum
   C×locF = ⊔_(m,n) (C_m×locF_n),
since the C_m and F_n are clopen in C and F respectively. Therefore z restricts to top on ALL of C×locF.

Restrict z further to C(q)=A×locB. Lemma 3 then implies z|_C(q)=1. Because C(q) is the closed complement of q in the sublocale sense,
   z∨q=1 in Q0.

This holds for all z∈B_fin^#, which by definition means
   **q∈B_fin^{##}.**
QED.

## 6. Consequences and remaining problem

The negative answer to Question A remains intact:
   q∉SEcl(B_fin)  but  q∈Regcl(B_fin).
The inclusion of closure operations is genuine on the explicit bar q. Regular completion is strictly more powerful than strongly exact completion in exactly the way anticipated in segment 1.

This is NOT an intrinsic description of V and NOT an equality B_fin^{##}=B. The latter requires testing EVERY bar, or equivalently proving that there is no nonzero CLOSED sublocale of V_fin disjoint from the old I=C(d). We have only ruled out nonzero closed sublocales contained in V_fin∩C(q), i.e. the residual removed specifically by q.

An intriguing possibility is that **B_fin^{##}=B** for the generic X0 even though V_fin≠V; then regular completion would be a genuine corrective completion operation, but one still defined using all finite-rank rectangle trees in Q0. It could also fail for a different bar. No theorem is claimed either way.

**Recommendation:** One further focused segment may test the full equality in this concrete example or seek a frame-internal description of double supplement using only the original L. If no concise criterion or non-tautological construction emerges, the time budget suggests pivoting back to the I,U,D,V,F relation hierarchy.
