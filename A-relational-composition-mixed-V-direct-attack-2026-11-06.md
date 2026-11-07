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

## 8. Exact pointless-residual certificate for SPATIAL X

This is a useful refinement of the necessity that E=I12∧D23 be nonspatial. Fix a spatial locale X, and for w∈Q satisfying d_I∨w=1 put

    E_w=I12 ∧ D23 ∧ C(w13) ⊆ X³.

Here C(w13) is the closed sublocale complementary to the open O(w13). Because pulling back a closed sublocale along E↪X³ gives the closed sublocale defined by w13|_E, it is nonzero precisely when the restriction w13|_E is not top.

**Proposition (working).** For any SPATIAL X,

    R=I D not≤ V
    iff
    ∃w∈Q with d_I∨w=1 and E_w≠0.

Moreover every such E_w is a **pointless locale**.

Proof: V=fit I is the meet of all O(w) containing I, i.e. the w with d_I∨w=1. Image relation R fails to lie in V iff for one such w, E fails to lie in O(w13), equivalently E_w is nonzero. Suppose E_w had a point. Its coordinate triple (x,y,z) consists of locale points of spatial X, with x I y and y D z. Spatiality of X and the cover characterization of D furnish a point t≤y,z. As I is closed, x I t, and V (fitted) contains (x,z) since (x,t)∈I and t≤z. Thus w(x,z)=1 because V≤O(w), contradicting C(w13). Hence E_w has no points.

This pinpoints the necessary pathological object for a SPATIAL counterexample: a nonzero pointless **locally closed composable-pair residual**, simultaneously lying in I12, D23, and outside a chosen I-neighborhood in the 13 coordinates. In particular neither a mere pointwise zigzag nor a failure of the properness-based uniform neighborhood condition is itself a counterexample.

For nonspatial X, the same algebraic iff remains true, but the proof of pointlessness cannot use the ordinary closure-meeting point formula without extra hypotheses, so do not claim the pointless conclusion there.

## 9. Distributor EXACTNESS also follows from D=B A

The condition D=B A yields more than mixed≤V: it restores the least-distributor formula from the coherent case, without assuming I=A B.

Indeed I B=I and A I=I by the closed-relation module lemma; thus

    R=I D=I B A=I A=A I A.

Since I≤J, one has A I A≤A J A. The reverse A J A≤R is universal from the distributor property of R and J≤R. Hence

    **R=A J A=I A**.

Dually,

    **R'=B J B=B I**.

Both equalities are VALID in arbitrary locales whenever D=B A (for example whenever D spatial). In particular, a counterexample to **either** (i) R≤V or (ii) R=A J A must have D≠B A. (This does NOT say the two potential failures are equivalent.)

This unifies the two outstanding arbitrary-locale questions: the extra part of the localic fitted diagonal beyond the specialization composite is the only possible source for either discrepancy.

## 10. Published stress test: sH not (Fsep) does not yield mixed failure

Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology and its Applications 342 (2024), 108785, https://arxiv.org/abs/2310.18522 (also open access DOI https://doi.org/10.1016/j.topol.2023.108785), explicitly constructs a strongly Hausdorff locale that is NOT F-separated. In our notation strong Hausdorff is I=Delta and Fsep is D=Delta.

For that published example:

    A=B=Delta (since A,B≤I=Delta),
    D>Delta=B A,
    V=fit I=fit Delta=D,
    I D=Delta D=D=V.

Thus the strictness D>B A, and nonspatiality of D, are genuinely realizable in the literature but do NOT suffice for the sought failure R⊄V. Nontrivial inseparability I must be coupled to the extra nonspatial D contribution. The published paper is supporting external context, not a source of the mixed-composition theorem and not a counterexample to it.

This also confirms mathematically that failure of D=B A alone cannot settle the second question R=A J A: since I=Delta, J=D and A J A=Delta D Delta=D=R in this test case.

## 11. Current strongest necessary conditions

For a SPATIAL locale X to refute I D≤V, it is necessary that all of the following hold:
(i) D≠B A, in particular D is nonspatial;
(ii) the projection p2:I→X is not proper;
(iii) E=I12∧D23 is nonspatial;
(iv) for some w containing I, the POINTLESS locally closed residual E_w=E∧C(w13) is nonzero.

Conditions (i)–(iv) are NOT sufficient. Condition (iv) is the exact failure certificate by §8, but the pointlessness follows from spatiality X, so unlike (i)–(iii) (iv) is equivalent to failure once w is quantified. A construction must COUPLE failure of strong Hausdorff/Fsep separation with nontrivial, nonproper inseparability; a direct product of unrelated examples should not be expected to achieve this automatically.

The primary literature test for (i), sH≠Fsep, is real and externally published; the remaining coupled construction is OPEN.

## 12. Exact fitting/composition reformulation, and a general proper-laxity theorem

This is the cleanest categorical answer to the asymmetry question. Universally Delta≤B A≤D=fit Delta, so

    **D=fit(B A).**

Also I B=I, I≤I A≤V (as I≤V, V A=V). Hence

    **fit(I B A)=fit(I A)=V.**

Therefore the outstanding question I D≤V is EXACTLY the specialized lax distributivity condition

    **I∘fit(B A) ⊆ fit(I∘B A).**

No coherence or spatiality used in this equivalence. It explains why replacing U by W=cl D does not resolve the duality problem: the missing operation is an interchange of FITTING with COMPOSITION, not merely a different name for U.

**General proper-laxity theorem (working).** For any locales X,Y,Z, relations S↪X×Y and T↪Y×Z, if p2:S→Y is PROPER then

    **S∘fit(T) ⊆ fit(S∘T).**

Proof. Let O(w)⊆X×Z contain S∘T. Consider P=S×Z, m:P→Y×Z induced by (p2,id_Z), and n:P→X×Z induced by (p1,id_Z). Since p2 is proper, m is proper, and t:=m_*(n^*w) is an open of Y×Z. Pull m back along the sublocale inclusion i_T:T↪Y×Z, whose pullback is E=S×_Y T. By proper Beck–Chevalley,

    i_T^*t = (E→T)_*[(n^*w)|_E] = (E→T)_*(1)=1,

because O(w) contains the image S∘T. Thus T⊆O(t), and fit(T)⊆O(t). By counit m^*t≤n^*w, on S×_Y fit(T) we have n^*w=1; hence S∘fit(T)⊆O(w). Since w was arbitrary, the desired inclusion follows.

The previously obtained result S∘D⊆fit S is the special case T=Delta, because S∘Delta=S and fit Delta=D. The new identity puts that lemma into a standard-looking relation-algebra pattern. Properness is only a sufficient hypothesis, not claimed necessary.

For S=I,T=B A, the theorem yields (8) under proper p2:I→X; since I is symmetric this covers both mixed orientations. The unrestricted open question is whether this ONE specialized laxity inequality remains true even when p2 is nonproper.

**Research test:** find a locale where fitting fails the general proper-laxity inequality for some NONPROPER relation S and T. Such a counterexample would NOT by itself settle our problem unless S=I,T=B A; however it could reveal how to engineer the required coupled defect.

## 13. General laxity really CAN fail without properness (elementary finite control)

Do not assume S∘fit T≤fit(S∘T) for arbitrary nonproper S; it is FALSE even for finite Alexandrov locales when S is not closed.

Let X=Z=1 and let Y={0<1} with upper Alexandrov opens. Take S↪X×Y=Y to be the open singleton {1}, and T↪Y×Z=Y to be the closed singleton {0}. The fitted hull of T is the entire Y (upward closure of 0), so S∘fit(T)=1. But S∘T=0 (no shared middle point), and fit(0)=0. Thus

    S∘fit(T) not≤fit(S∘T).

The second projection S→Y is not proper: its image {1} is not closed in Y. This finite example does NOT refute our original question, since S is not I and is not closed. It does show that a universal fitting/composition distributive law is untenable; a proof for S=I must use the closed, symmetric diagonal-generated structure of I, not merely formal fitting axioms.

In fact for the original S=I, compactness supplies properness automatically, so a genuine counterexample would require noncompact/nonproper behavior invisible in these finite tests.
