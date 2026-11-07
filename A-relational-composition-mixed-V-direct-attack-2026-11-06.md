# Project A — Direct attack on I∘D ⊆ V and the noncoherent duality gap

6 November 2026. New **WORKING** results/proof reductions. Do not claim unrestricted inclusion or counterexample. Not externally audited. Provenance: [arbitrary-locale specialization/composition note](A-relational-composition-arbitrary-locales-specialization-2026-11-06.md), [compact lower-diamond three-point note](A-lower-diamond-compact-three-point-working-note.md), [dual-farness compact and infinite note](A-dual-farness-compact-and-infinite-2026-10-21.md), [independently audited failure of unrestricted dual-far strip presentation](A-V-Claude-external-audit-reconciliation-2026-10-22.md).

L=O(X), Q=L⊕L; I=cl Delta, D=fit Delta, W=cl D, U=C(d_U), V=fit I. A=Sp_X↪X² is the standard generalized-point specialization order f≤g iff f*a≤g*a; B=A^smile. Write R=I∘D, R'=D∘I. We already proved universally R,R'≤U, and if p2:I→X proper then R,R'≤V.

## 1. The suspected asymmetry is genuine: R not≤ W even compactly

In the **compact noncoherent three-boundary-point lower-diamond example** X=S1⊔S2⊔{p,x,y} (S1,S2 infinite discrete, p<x, and cofinite S2 tails shared by p,y), the audited computation is

    W=I < U=V=F.

Ordinary points satisfy y I p and p D x (p≤x), but y not I x because {x}∪S1 and {y}∪S2 are disjoint opens. Therefore (y,x)∈I D but (y,x)∉W=I. The ordinary pair produces a genuine localic mixed-composition point, no nonspatiality assumption needed.

Thus the global R≤U theorem cannot be improved to R≤cl D=W, even for compact sober locally compact X. The fact U can exceed W is therefore a MATHEMATICALLY REAL part of the imperfect cross-hull duality. However R≤V DOES hold in this same compact example by properness, so the strictness U>W does NOT itself cause failure of the desired V-inclusion.

## 2. Direct binary argument for disjoint-supplement dual-far strips

Call s(k,h)=(k⊠1)∨(1⊠h). Suppose there exist a,b∈L with

    k∨a=1,   h∨b=1,   a∧b=0.

Then s(k,h) contains I (because 1=(k1∨a1)∧(h2∨b2)≤k1∨h2∨a1b2≤s12∨d_I). **NEW universal lemma:** R⊆O(s(k,h)).

Proof in E=I12∧D23⊆X³. From a∧b=0 the I12 condition gives a1∧b2=0. Since k1∨a1=1, deduce b2≤k1. The binary cover {h,b} of 1 gives (h2∧h3)∨(b2∧b3)=1 on D23. Hence 1≤h3∨b2≤h3∨k1 on E; thus E factors through O(k1∨h3). Converse R' obeys corresponding transposed statement.

Let V_sup = meet_{k∨a=h∨b=1,a∧b=0} O(s(k,h)). Then

    V≤V_sup and R,R'≤V_sup

for ALL locales. This is the closest literal dual of the easy U proof: both use just a BINARY open cover. But V_sup can exceed V because not all neighborhoods of I need be obtained from these special strips, and even general dual-far strips can lack disjoint supplements (Sorgenfrey plane).

For COMPACT X, two independently established results close both gaps: (i) dual far iff disjoint supplements, and (ii) V equals meet of ALL dual-far strips (compact I). This gives a second direct proof of R≤V for compact X, independently of proper Beck–Chevalley.

## 3. A new positive class: spatial fitted diagonal

The universal specialization relation gives B A≤D. Suppose **D is spatial as a locale**. Because Delta≤D and p1:D→X retracts along Delta:X→D, X is itself spatial: if two opens of X differ, their images under p1* differ in spatial D, so some point of D separates them and projects to a point of X.

For spatial X, a point (x,y) of D is exactly a closure-meeting pair: there exists an ordinary locale point z with z≤x and z≤y. Thus the point (x,y) factors through B A. A spatial sublocale is the join of its points, so D≤B A. Combining with B A≤D gives

    **D=B A whenever D is spatial.**

More generally ANY condition ensuring D=B A suffices for R≤V: I B=I because I closed, and V A=V because V fitted, hence

    I D=I B A=I A≤V A=V.

The other orientation follows by converse. In fact the same argument works for EVERY closed relation C in place of I: if D=B A then C D=C B A=C A≤fit(C) A=fit(C).

**Necessary conditions for a counterexample R⊄V:** D nonspatial, and D≠B A; moreover the p2 projection of I must be nonproper (by the preceding properness theorem). These are necessary, not sufficient.

## 4. Spatiality of the composable-pair source rules out failure

Let E=I12∧D23. It contains the triple diagonal, so if E is spatial, then X is spatial as a retract. For an ordinary point (x,y,z) of E, x I y and y D z. Choose t≤y,z witnessing D. Because I is CLOSED, x I y and t≤y imply x I t. As V is FITTED and contains I, t≤z implies x V z. Hence the map E→X² factors through V on ALL its points; spatiality of E lifts this to the genuine sublocale inclusion R≤V.

So **R⊄V requires the composable-pair locale E to be nonspatial**, in addition to D being nonspatial. This explains why finite/coherent and many locally compact spatial examples are unable to witness a failure.

Beware: in an arbitrary locale the set of ordinary image points need not equal the pointwise composite, because a localic image can have pointlike effects not lifted by points of the source. We use the spatiality of E explicitly, not a blanket point-image assumption.

## 5. A restricted diagonal base-change condition (stronger than target)

Let m:I×X→X², m(x,y,z)=(y,z), and n:I×X→X², n(x,y,z)=(x,z). For each w∈Q with I⊆O(w), put

    t_w=m_*(n^*w).

Always m^*t_w≤n^*w. If δ^*t_w=1 for every such w, then each O(t_w) contains Delta, so D≤O(t_w), and the pullback E=I12∧D23 lies in O(w13). Hence R≤V.

Properness of p2:I→X ensures this sufficient condition by proper Beck–Chevalley, but its validity may not follow from R≤V alone: do NOT treat it as an exact equivalence. It isolates the specific universal-neighborhood uniformity that the direct proof needs. Without properness the diagonal base-change equality need not hold for arbitrary maps. It could conceivably still hold for I specifically.

The unconditional inclusion R≤U avoids this interchange entirely: testing one far rectangle uses the binary cover {a*,b*}. That is a second, precise explanation of proof asymmetry.

## 6. A useful frame class: join-dense completely join-prime basis

Suppose L has a join-dense family P of completely join-prime opens. Put

    w0=⋁_{p∈P}p⊠p.

Then δ^*w0=1. If w=⋁_i a_i⊠b_i is any diagonal neighborhood, δ^*w=⋁_i(a_i∧b_i)=1. For each p∈P, complete join-primality gives p≤a_i∧b_i for some i, hence p⊠p≤w. Thus w0≤w, and

    **D=O(w0).**

For the spatial upper-Alexandrov locale O(P0) of a poset P0, its principal opens ↑x form a join-dense completely join-prime family and the localic square is spatial (Alexandrov locales are locally compact and soberified products are spatial). Thus D is OPEN and SPATIAL in all these examples. In particular, the infinitely branching Fn(N,2) example—although D2>D and h_hc=h_cc=0—cannot violate R≤V. This is a particularly useful control distinguishing finite-cover fitting defects from nonspatiality of D itself.

The general statement 'D=O(w0)' is frame-valid without spatiality; spatiality of D additionally requires the ambient square or this open sublocale to be spatial.

## 7. New disposition

**Question 1:** Is R≤V for EVERY locale? UNRESOLVED. Proved if I projection proper, or if D=BA (in particular D spatial), or if E=I12∧D23 spatial.

**Question 2:** The lack of duality is real but not the whole explanation. Already compactly R⊄W=cl D while R≤U∧V. The dual binary-cover proof works on disjoint-supplement strips, but noncompactly they may not generate fit I; moreover dual-far strips can lack such supplements. The actual universal target asks whether the extra pointless portion of D can propagate through I into an open neighborhood excluded by V.

**Next focused test:** Take a noncompact locale with a genuinely nonspatial fitted diagonal D and nonproper inseparability projection, not an Alexandrov/prime-generated locale. Examine directly the composable-pair sublocale E for a failure of a chosen open neighborhood of I. The earlier rational-bridge V-strip counterexample is a candidate source of the requisite infinitary neighborhoods, but no verified factorization of its graph obstruction through I D has been constructed. Do not promote that possibility to a counterexample.
