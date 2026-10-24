# Project A — Lower diamond strict in an almost-normal noncoherent locale

24 October 2026. NEW INTERNALLY CHECKED WORKING RESULT; not yet externally audited. Extends the previously focused-internally-audited thickened-zigzag construction (A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md). It answers the remaining lower-diamond inclusion question negatively and gives a family-level boundary transfer theorem.

## 1. Statement

Let I=cl(Delta), D=fit(Delta), W=cl(D), V=fit(I), J=I∨D and T(J)=cl(J)∧fit(J)=W∧V. Then T(J)≤U∧V universally, with equality for coherent locales.

**THEOREM.** There is a countable, sober, scattered, noncompact almost-normal T0 space X, with spatial scattered localic square, such that
   **T(J)=W < U∧V=U=V=F.**
Thus the lower diamond is genuinely strict even though U and V coincide with the functional relation F.

**Universal criterion:** If U is fitted, I≤U implies V≤U, so U∧V=V. Since D≤V implies W≤cl(V), we have
  T(J)=U∧V iff V≤W iff cl(V)=W.
This applies in particular when the frame is almost normal (U=F then).

## 2. The five-point seed and its two zigzags

Take P={p,q,t,x,y} with ONLY the strict comparisons
   p<t, p<x, q<t, q<y.
The underlying comparability graph is connected. The finite Alexandrov relations satisfy
   V_P = P²,
   U_P = P² minus {(x,y),(y,x)}.
Indeed p,q have common upper t; every point of P lies above p or q, so every pair belongs to the UPWARD saturation of I_P. Conversely x,y are maximal and have no common lower, so (x,y) cannot belong to the DOWNWARD saturation of D_P.

## 3. The almost-normal thickening X(P)

Use the existing space X(P)=B⊔S, with
   B=P×omega^op, (s,n)≤(t,m) iff s≤_P t and n≥m;
   S={s_r:r rational}, each s_r clopen.
Choose distinct irrational attachment coordinates alpha_(s,n), with every tail of each fixed-s sequence dense in the real line. For each boundary b give neighborhoods whose B traces are its finite principal upset ↑b and whose rational traces contain finitely many intervals around alpha_c, c∈↑b, with possible nowhere-dense deletions. The full exact topology and proof of almost-normality are in the original construction note and its focused internal audit.

B is closed, locally compact, sober Alexandrov. X is sober and scattered, and its localic square Q=O(X)⊕O(X) is spatial: O(S×S) is discrete spatial, while its closed complement is the join of B×locX and X×locB, spatial by the locally compact factor theorem. The ordinary square X×X is scattered, and every sublocale of such a scattered spatial locale is spatial (Simmons/Niefield–Rosenthal). Consequently sublocale equality and disjointness can be tested by ordinary points IN THIS EXAMPLE.

## 4. Point lemma for D and calculation of W on B×B

For ANY topological Z, ordinary points of fit(Delta_Z) are exactly pairs (x,y) with a common specialization predecessor z≤x,y.

Proof: if such z exists, every diagonal-open contains (z,z) in a rectangle, hence also (x,y). Conversely, in the absence of a common predecessor, for each z choose an open O_z containing z but not both x,y. The family {O_z} covers Z, so w=∨_z(O_z⊠O_z) contains Delta as a genuine localic sublocale, yet misses (x,y). Thus the point pair is excluded by fit Delta.

In X(P), the D-point relation comprises boundary B×B pairs with a common lower bound, together with Δ_S; no mixed boundary/isolated pairs occur because S points are clopen.

**BOUNDARY TRANSFER THEOREM:**
For b=(s,n), c=(t,m)∈B,
   (b,c)∈pt(W_X) iff (s,t)∈U_P,
where U_P is the finite Alexandrov common-upper zigzag relation (downward saturation of common lower).

Proof, positive direction: (s,t)∈U_P means there are u≥s, v≥t and r≤u,v in P. The lifted boundary pair ((u,0),(v,0)) has common lower ((r,N)) for suitable N, hence lies in D_X. The original pair (b,c) is its specialization predecessor and belongs to the closure cl(D_X)=W_X.

Proof, negative direction: if (s,t)∉U_P, NO pair of boundary points u≥b,v≥c has a common lower. Also ↑b and ↑c are disjoint, since their intersection would witness I_P≤U_P. Those upsets are finite and their sets of distinct irrational attachments are disjoint; choose disjoint unions of rational intervals around the two finite attachment sets. The resulting open neighborhoods N_b,N_c have B traces ↑b,↑c and DISJOINT rational traces. The rectangle N_b×N_c contains no D points: not on B² by the U_P assumption, not on S² because only diagonal S points belong to D, and not mixed. Since D and the square are spatial, the corresponding open sublocale meets D trivially, so (b,c)∉cl(D)=W. This argument does NOT equate an arbitrary nonspatial sublocale to its point set.

In particular, let b=(x,0),c=(y,0). Since (x,y)∉U_P, we have
    **(b,c)∉pt(W_X)**.
Here ↑b={b}, ↑c={c}; the disjoint rational traces are particularly transparent.

## 5. V, U and F coincide in the selected example

Every boundary point (s,n) lies above a boundary predecessor (h,N) with h=p or h=q. Choose N large enough for two given boundary points b,c. The corresponding predecessor pair has common upper (t,0), where t is the seed's middle top point, and thus lies in I_X. Because V=fit(I) is a meet of OPEN sublocales, it is upward saturated on ordinary product points; therefore EVERY boundary pair lies in V.

Every continuous real-valued function on X is constant on the comparability-connected boundary B, because real points have equality specialization. As the s_r singletons are clopen, their characteristic functions distinguish each isolated rational point from every other point. Consequently the ordinary point set of F is EXACTLY
    B² ∪ Δ_S.
Since I≤V≤F and V contains ALL B² plus Δ_S, spatiality of all sublocales of Q yields
    **V=F.**

The frame of X(P) is almost normal, by the existing proof based on robust nowhere-dense rational filters. The previously established almost-normal theorem gives
    **U=F**.
Alternatively, this can be checked directly: the rational trace of every boundary neighborhood is dense in a nonempty real interval; for any two such traces the dense tails alpha_(s,n) find a boundary point (s,N) in both closures. Thus no boundary pair is far, while distinct clopen isolated points are far. Since U and F are closed sublocales of the spatial square they coincide.

Therefore U=V=F. Since W≤U=V, we have T(J)=W∧V=W and U∧V=F. The pair (b,c) above proves W<F, hence the strict inequality.

## 6. Interpretation, proof dependencies and open follow-ups

1. We have settled the arbitrary-locale equality T(J)=U∧V NEGATIVELY, even on almost-normal frames and with U=V=F.
2. For any finite P, the thickening transfers the finite Alexandrov U_P to W_X along B×B. The original thickening note independently proves that V_X on B×B transfers the UPWARD saturation of I_P, which is the finite Alexandrov V_P (via rank-three localic bars). Thus choosing any P with V_P not contained in U_P potentially yields a lower-diamond gap. The five-point P provides full V=U=F as an additional bonus.
3. This strengthens the substantive concern motivating V: outside coherence, cl(D) and U are truly different, and even agreement U=V does not force agreement of the formal cross-hulls.
4. The square-spatiality and scattered-sublocale steps are essential and should be separately rechecked by an external auditor before publication.
5. This example is NOT compact, coherent or T1; no claim of strictness under those additional constraints.
6. No literature novelty claim. The original topology has a focused INTERNAL audit; the specific lower-diamond transfer and strictness remain new internally checked results.
