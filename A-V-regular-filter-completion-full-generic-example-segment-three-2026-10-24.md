# Project A — Strongly exact filter trial, segment 3: FULL regular completion in the generic-point counterexample

24 October 2026. **SUBSTANTIAL NEW WORKING THEOREM, proof below; not yet externally audited.** This is the third and scheduled final segment in a bounded trial of strongly exact/regular-filter methods for describing V=fit(I). In the countable sober T0 two-generic-point counterexample, although finite-rank bars do NOT strongly-exactly generate all bars, they DO generate all bars under double-supplement regularization. This is stronger than the previous segment (which recovered only the particular omega-rank bar q). It does not yield a general intrinsic characterization of V in the original frame L, and no general theorem for arbitrary locales is claimed.

## 1. Statement

For a locale X, let Q=O(X)⊕O(X), d=∨{u⊠v:u∧v=0}, and define
  B={v∈Q:d∨v=1},
  B_fin={v∈B: v has a finite-height rectangular separation tree}.
Both are filters, B is closed/regular, and B_fin⊆B.

For any filter F⊆Q, let F^#={z∈Q:∀v∈F,z∨v=1}. Its double supplement F^{##} is the least regular filter containing F.

**THEOREM (specific generic-point space).** Let Y=⊔_{m≥1}Z_m be the iterated K-fan sum, C=⊔C_m,F=⊔F_m, and X0=Y⊔{ell,r} with the two-generic-point topology. Then
   **B_fin^#=↑d**, and hence
   **B_fin^{##}=B**.
In contrast, the previously externally audited negative answer to Question A says
   SEcl(B_fin)⊊B and V_fin⊋V.
This shows the regular completion is STRICTLY stronger than strongly exact completion on this example, and it completely recovers the full closed bar filter.

## 2. Three geometric opens and the key frame inequality

Define closed pole sets A=C∪{ell}=cl{ell} and Bp=F∪{r}=cl{r}. (Write Bp to avoid confusing the pole set with the bar filter B.) Let
  a=X0\A=(Y\C)∪{r},
  e=X0\Bp=(Y\F)∪{ell},
  h=a∧e=Y\(C∪F).
The two generic-point null bars are
  q=(a⊠1)∨(1⊠e),
  τq=(1⊠a)∨(e⊠1).
They are bars of exact well-founded rank omega, by the transfer theorem, and the previous segment proved
   q∈B_fin^{##}.
Transposition (exchanging the two localic product coordinates) preserves d and finite rank, hence
   τq∈B_fin^{##}.

Let c≺u abbreviate c*∨u=1 in O(X0), and put
  d_sep=∨{c⊠f : c≺u, f≺v, u∧v=0}.
(The original project has called this 'regularized apartness'.)

**KEY FRAME INEQUALITY**
   **d∧q∧τq ≤ d_sep.**                 (2.1)

Proof of (2.1), first reduction. By distributivity of the localic tensor coproduct,
  q∧τq=(a⊠a)∨(h⊠1)∨(1⊠h)∨(e⊠e).
Consider ANY disjointness rectangle u⊠v, u∧v=0.

Since any open meeting F contains r, two disjoint opens CANNOT both meet Bp=F∪{r}. If u meets Bp, v is disjoint from Bp; hence v∧a≤h. Otherwise u∧a≤h. Thus
 (u⊠v)∧(a⊠a)≤(h⊠1)∨(1⊠h).
Analogously, since any open meeting C contains ell, 
 (u⊠v)∧(e⊠e)≤(h⊠1)∨(1⊠h).
Join over all disjoint rectangles u⊠v to obtain
  **d∧q∧τq≤d∧((h⊠1)∨(1⊠h)).**      (2.2)

The second reduction uses the regular clopen patch cover of h (§3):
  **d∧((h⊠1)∨(1⊠h))≤d_sep.**       (2.3)
Together these give (2.1).

All inequalities are in Q (the full frame coproduct). Ordinary points were used only to decide whether a given coordinate open meets a pole set, never to infer a coproduct-cover identity from a point-set product cover.

## 3. The regular clopen patch cover

**LEMMA.** h=Y\(C∪F) is the union of complemented (clopen) opens W⊆X0 whose induced frames O(W) are regular.

Proof by induction on the original fan levels.

Base Z_1=Q with K-topology and C_1=K={1/j}, F_1={0}: every x outside K∪{0} lies in a rational interval with irrational endpoints and closure in the usual real line disjoint from K∪{0}. This interval is clopen in the K-topology (usual rational clopen interval, with its complement usual open) and has ordinary rational topology, hence regular.

At each fan stage Z_(m+1), the new apex t belongs to C_(m+1) or F_(m+1). Every point of the complement of these closed color sets lies in a clopen old copy Z_m; lift the inductive regular clopen patch from that copy. The topological disjoint sum Y preserves these clopen patches.

Finally, any W⊆Y that is clopen in Y and DISJOINT from C∪F remains clopen in X0. It is open by the defining topology (no mandatory generic points because it meets neither C nor F). Its complement has old trace Y\W open and includes BOTH generic points ell,r, so satisfies both implication conditions. Therefore W is complemented in O(X0), with unchanged regular open frame. These W cover h. QED.

**LEMMA (local regular-apartness).** If W is a complemented open of X0 and O(W) regular, then
 d∧(W⊠1)≤d_sep,    d∧(1⊠W)≤d_sep.      (3.1)

Proof. Write W' for the complementary open. All cross rectangles W⊠W',W'⊠W belong to d_sep, because W≺W and W'≺W', with W∧W'=0. Within W⊠W, regularity of O(W) says each local disjointness rectangle is the join of subrectangles c⊠f with c≺_W u,f≺_W v and u∧v=0. Because W is complemented, relative rather-below lifts globally: for c,u≤W, if c*_W∨u=W then c*_X∨u=1 (the global pseudocomplement includes W'). Thus local regular-apartness generators belong to global d_sep. Decompose d∧(W⊠1) into its W⊠W and W⊠W' portions; same for the transposed strip. QED.

Join (3.1) over W in the clopen cover of h to get (2.3), hence the key inequality (2.1).

## 4. Every supplement of the finite bars contains the full disjointness open

Take an arbitrary z∈B_fin^#. Thus z∨v=1 for ALL finite-rank bars v.

**First:** d_sep≤z. For each generator c⊠f of d_sep, choose u,v with c≺u,f≺v,u∧v=0. The rank-two strip
   t_cf=(c*⊠1)∨(1⊠f*)
is a bar: horizontally cover first coordinate by c*,u (because c*∨u=1); beneath u vertically cover second by f*,v (because f*∨v=1); the (u,v) child is disjointness, other children are t_cf leaves. So t_cf∈B_fin. Also t_cf∧(c⊠f)=0. Since z∨t_cf=1,
   c⊠f=(c⊠f)∧(z∨t_cf)≤z.
Join all generators to obtain d_sep≤z.

**Second:** z∨q=1=z∨τq. This follows from q,τq∈B_fin^{##}, proved by a separate explicit finite-component-block calculation in [A-V-regular-filter-completion-omega-bar-segment-two-2026-10-24.md]. The transposed statement uses the coordinate swap, which preserves B_fin.

Now compute in Q:
  d = d∧(z∨q)∧(z∨τq)
    = (d∧z)∨(d∧q∧τq)
    ≤ z∨d_sep
    = z.
The second equality is ordinary finite distributivity in the frame Q. The inequality uses (2.1) and d_sep≤z.

Thus **every** z∈B_fin^# dominates d, proving
   B_fin^#⊆↑d.
Conversely if z≥d, then z∨v=1 for every bar v (since d∨v=1), so
   ↑d⊆B_fin^#.
Therefore
   **B_fin^#=↑d.**                    (4.1)

Taking one more supplement,
   **B_fin^{##}=(↑d)^#={v:d∨v=1}=B.**   (4.2)
QED.

## 5. Broader sufficient criterion and exact limitations

The proof identifies a modular sufficient criterion for REGULAR generation, even though it does not give an intrinsic formula in the original L.

**TWO-POLE SUFFICIENT CRITERION.** Suppose X admits two symmetric bars q,τq, and a chosen open h such that
 (i) q,τq∈B_fin^{##};
 (ii) d∧q∧τq≤d_sep,
where d_sep is regular-apartness generated by rather-below rectangles (and rank-two bars force d_sep≤every z∈B_fin^#).
Then **B_fin^#=↑d**, hence B_fin^{##}=B.

This is fully general for locales once (i)–(ii) are verified; the proof is §4. The current generic-point example satisfies them because h has a regular clopen cover and the generic pole sets are topologically hyperconnected with their generic points.

**Negative characterization verdict:** The equality B_fin^{##}=B is a real theorem for X0 but is NOT a non-tautological, arbitrary-locale characterization of V. The expression still requires Q=L⊕L, the full disjointness open d, and finite-rank rectangular C-ideal proof trees. The sufficient criterion also assumes hard-to-compute regular-generation hypotheses.

**Contrast with the earlier negative answer:** The equality of REGULAR closures coexists with inequality of STRONGLY EXACT closures:
  SEcl(B_fin) ⊊ B_fin^{##}=B.
Thus one must not mistake the failure of V_fin=V for failure of *all* algebraic completions.

**What remains open:** whether B_fin^{##}=B holds for every locale, whether some smaller intrinsic family can regular-generate B, and whether a dual-farness/regular-filter characterization of V can be expressed with simpler data of L alone. No assertion about all finite fitted stages or the D,U,F hierarchy is made here.

## 6. Research allocation decision

We agreed to limit this filter trial to two or three substantive segments and extend only if a substantial theorem emerged. This segment DOES yield a substantial theorem, namely complete regular-generation of B in the explicit counterexample and the modular two-pole sufficient criterion.

However, the original intrinsic-characterization ambition remains unmet. Rather than spend unbounded time on the same example, a productive OPTIONAL next step is to test the **universal** conjecture B_fin^{##}=B by searching for a general C-ideal/regular-filter induction. That is a genuinely new general question, not just a fourth rephrasing. Alternatively, pause the V characterization and return to the I,U,D,V,F hierarchy; the present note preserves the exact result for later use.

The present proof is internally checked, NOT externally audited. If used in a publication, request an independent targeted audit of (2.1), the clopen lifting of rather-below, and the preceding segment-2 top-reflection/finite-lift result.
