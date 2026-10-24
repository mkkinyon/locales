# Project A — Strongly exact filters, the finite-bar filter, and a regular-completion test

24 October 2026. **First of a bounded trial (two or three mathematical segments) of strongly exact-filter methods for characterizing V=fit(I).** This document separates SOURCE FACTS (Jakl–Suarez 2025) from elementary NEW DEDUCTIONS within Project A. Main result: strongly exact completion of the finite-rank bar filter is provably insufficient, even in the new sober generic-point example; the stronger *regular* completion admits an exact closed-sublocale test and is the next falsifiable direction. No claim that this characterizes V intrinsically, and no result concerning general all-n stage strictness.

## 1. Literature definitions — SOURCE FACTS

Reference: T. Jakl and A. L. Suarez, *Canonical extensions via fitted sublocales*, Applied Categorical Structures 33, article 10 (2025), open full text https://link.springer.com/article/10.1007/s10485-025-09802-6 .

For a frame Q a filter F⊆Q is nonempty, upward closed, finite-meet closed. Their notation:
   su(F)=⋂_{f∈F}O(f);
   fi(S)={w∈Q:S⊆O(w)}.
Strongly exact filters are precisely the fixed points fi(su(F)); equivalently they are closed under all meets \bigwedge_i f_i for which ⋂_i O(f_i)=O(\bigwedge_i f_i). Theorem 6.2: the strongly exact filters (under REVERSE inclusion) correspond to fitted sublocales. Note their term "exact meet" is a different condition, not our finite separation-tree rank.

The closed filters are of form
   C_Q(z)={w∈Q:z∨w=1}=fi(C(z)).
Their equation (5.4.1) identifies C_Q(z) with the SUPPLEMENT in the coframe Filt(Q) of the principal filter ↑z. These closed filters are regular, exact and strongly exact. Proposition 5.7: regular filters are intersections of closed filters; Theorem 6.8: regular filters correspond to fittings of joins of closed sublocales.

## 2. The finite-bar family is an ordinary filter

Let L be arbitrary, Q=L⊕L, and d=d_I=⋁{a⊠b:a∧b=0}. Put
   B={w∈Q:w∨d=1};
   B_fin={w∈B:rk(w)<ω}.
Then B_fin is nonempty (1∈B_fin), upward closed (enlarging a bar can only add canonical rectangle leaves), and **closed under finite meets**:

Given finite separation trees of heights m,n for v and w, graft beneath every non-D v-leaf rectangle (a,b) a copy of the tree for w, restricted to (a,b). Horizontal/vertical covers restrict using frame distributivity; all new non-D leaves are below both v and w, hence below v∧w; original D leaves remain D. The resulting tree has finite height≤m+n, proving v∧w∈B_fin.

The full bar filter is a CLOSED filter:
   B=fi(I)=C_Q(d)={w:d∨w=1}.
Consequently B is already a REGULAR filter, not merely strongly exact. Its coframe supplement expression is
   B=(↑d)^#,
where, for any filter F,
   F^#={z∈Q: z∨f=1 for every f∈F}.
This is SOURCE Theorem 5.4.1 specialized to d (or immediate from definitions).

Thus *simply passing from bars to strongly exact filters does not simplify the problem*: it takes a previously known condition d∨w=1 and calls it a closed/regular filter.

## 3. An exact test for strongly exact completion

Write
   SEcl(F)=fi(su(F)).
It is the SMALLEST strongly exact filter (by ordinary inclusion) containing F, since fi∘su is an extensive idempotent closure on filters.

Our two fitted relations correspond to
   V=su(B),     V_fin=su(B_fin).
The Jakl–Suarez correspondence therefore gives
   V=V_fin   iff   SEcl(B_fin)=B.
This is a completely exact reformulation, but alone it is not an intrinsic characterization of V and gives no proof of equality.

The rank-omega generic-point counterexample proves the equality FAILS, with a stronger algebraic obstruction:

Let X0=Y⊔{ell,r} be the audited sober T0 construction, let Q0=O(X0)⊕O(X0), p=(ell,r), and let
   c={ell}⊠{r}>0.
Since the singletons {ell},{r} are open, c is the open point sublocale and p(v)=1 iff c≤v for any v∈Q0: if p(v)=1, some rectangle generator u⊠v'≤v contains p, and c≤u⊠v'.

The counterexample's restriction theorem says EVERY finite-rank bar v contains p. Therefore
   B_fin⊆↑c.
The principal filter ↑c is **closed under ALL meets in Q0**, hence strongly exact. Therefore
   **SEcl(B_fin)⊆↑c**.

The explicit two-rectangle rank-omega bar q=(a0⊠1)∨(1⊠e0) misses p, so q∧c=0 and q∉↑c, while q∈B. It follows
   **SEcl(B_fin) ⊊ B**.
This not only disproves naive strongly exact completion of finite bars; it shows even ALL ordinary arbitrary frame meets of finite bars cannot produce an open avoiding c. The obstruction is a COMMON NONZERO OPEN ATOM of the finite bars.

Do not infer B_fin itself is not strongly exact: the argument does NOT decide whether SEcl(B_fin)=B_fin.

## 4. A stronger completion: regular filters (NEW exact reduction)

Define F^#={z:∀f∈F, z∨f=1} as above. This is always a filter. Define
   Regcl(F)=F^{##}.
Then F⊆F^{##}, F^{##} is regular (a supplement), and it is the SMALLEST regular filter containing F (ordinary inclusion): if G=H^# is regular and F⊆G, then H⊆F^#, so F^{##}⊆H^#=G.

Because B is a regular filter containing B_fin,
   **B_fin⊆B_fin^{##}⊆B**.
This is a strictly STRONGER potential completion than SEcl(B_fin); the open-atom trap of §3 does not automatically survive regularization because ↑c need not be a regular filter.

The regularization criterion has a clean geometric form. Put S=su(F) and
   J_c(S)=⋁{C(z) : C(z)⊆S},
the join (in the complete lattice of sublocales) of all CLOSED sublocales contained in S. Then:
   z∈F^# iff C(z)⊆S,
since C(z)⊆O(f) iff z∨f=1 for each f∈F. Therefore
   **F^{##}=fi(J_c(S))**,
and
   **su(F^{##})=fit(J_c(S))**.

Consequently the precise REGULARIZATION TEST for our case is
   **B_fin^{##}=B**
iff
   **fit(J_c(V_fin))=V**.
This is an exact criterion, NOT an established equality. It asks whether the whole finite-stage fitted residual becomes indistinguishable from I after retaining only the closed sublocales contained in it and fitting again.

A falsification criterion is equally explicit: regularization FAILS iff there exists a nonzero closed sublocale R⊆V_fin and a proper bar q with R⊆C(q). Indeed R=C(z) with z∨v=1 for every finite bar v, and R⊆C(q) means z∨q<1. Then z∈B_fin^#, but q∉B_fin^{##} although q∈B. Conversely, if q∈B\B_fin^{##}, there is such z, giving nonzero R=C(z∨q)⊆V_fin∩C(q). (No point/spatiality hypothesis.)

This is the next focused test. Since I=C(d)⊆V_fin always, some closed sublocales of V_fin are automatic; the question is whether there are additional *closed residuals killed by full bars* but preserved by ALL finite bars. The generic-point obstruction is open, not closed: its closed hull intersects parts that finite bars may already remove. Thus the existing point witness does not immediately settle regularization in either direction.



## 4a. An additional exact computation: the point trap vanishes under REGULARIZATION

The regular route is genuinely different from strong exactness in the GENERIC-POINT EXAMPLE. Let c={ell}⊠{r} be the nonzero open singleton p=(ell,r). Choose any ordinary point y=(c_0,f_0), c_0∈C,f_0∈F. Every basic rectangle neighborhood of y contains p by construction; hence y∈cl{p}, y≠p.

CLAIM: (↑c)^#={1}, hence (↑c)^{##}=Q0 (the IMPROPER filter).

Proof: if z∨c=1, then y∈z, because c misses y. Since every open containing y contains p, we have p∈z and thus c≤z (the point p is OPEN). Therefore z∨c=z=1. Conversely 1 supplements c. Thus ↑c has no nontrivial supplement and its double supplement is all of Q0.

Consequently the containment B_fin⊆↑c, which completely blocks STRONGLY EXACT closure, supplies NO corresponding obstruction to REGULAR closure. The regular-filter operation destroys the very open-atom obstruction on which our negative Question A proof rests. This does NOT prove B_fin^{##}=B: that remains the focused test in §5.

The argument uses only ordinary points of the localic square and its rectangular join basis, not the spatiality of the whole square.

## 5. Assessment and disciplined next step

**Positive outcome of this segment:** exact filter-theoretic framework and a new principal-open obstruction; a precise regular-closure test that could conceivably recover V even where SE completion of finite bars fails.

**Negative outcome:** merely invoking Theorem 6.2 yields the tautology V=su(fi(I)). The FULL bar filter is already a single closed filter, a much smaller subclass than arbitrary strongly exact filters. No genuinely intrinsic formula for V in terms of operations solely in L has yet appeared.

**Next single test:** calculate or bound J_c(V_fin) in the simple two-generic-point example, and ask whether fit(J_c(V_fin))=V. If YES, seek a general regularization theorem; if NO, this route is likely exhausted and we should pivot after a final short segment. Avoid spending time on another isolated finite-rank example.

Reminder: **V is fitting of CLOSED INSEPARABILITY I=C(d)**, not fitting of actual diagonal Δ; notation distinction from D remains essential.
