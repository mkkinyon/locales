> **7 Nov 2026 — INDEPENDENT BLIND REFEREE REPORT ACCEPTED; ERRATA RECONCILED:** [Post-referee reconciliation with self-contained corrected frame proof](A-mixed-composition-external-audit-reconciliation-2026-11-07.md). External referee independently confirmed negative theorem, SPATIAL realization, nontransitivity, and F-separatedness characterization. Corrections: (i) prove F0 D F1 directly rather than invoking I≤D prematurely; (ii) define the specialization SUBLOCALE and explicitly prove K≤I,D in the kernel-pair refinement; (iii) explain that pullbacks preserve closed/fitted sublocales; (iv) avoid "topological simple extension" terminology; (v) note witness T is POINTLESS for the spatial input. Main theorem needs no associativity of localic composition. PRIORITY not fully checked. The external referee's further note that image-defined localic composition may fail associativity applies to EARLIER composition identities, not this single-composition theorem.

> **7 Nov 2026 — POST-BANASCHEWSKI INTERNAL AUDIT (PASS; EXTERNAL BLIND AUDIT PENDING):** [Detailed independent frame-proof audit and source reconciliation](A-mixed-composition-internal-audit-and-banaschewski-2026-11-07.md). Banaschewski (1992) Prop. 2.1 identifies M=O(O(u∨e)) as the singly generated frame {(a,b):a≤u, a≤b}, top (u,1), η(a)=(a∧u,a), c=(0,1). Given nonzero T=D_Y∧O(u⊠u*), frame maps h,k:L→O(T) satisfy h(u)=1,k(u)=0 and all-cover compatibility. The three FRAME homomorphisms F0(a,b)=h(a), F1(a,b)=h(b), G1(a,b)=k(b) witness F0 I F1 D G1. The open w=c_left∨η(u)_right contains I_M because I_M≤K=ker(X→Y) CLOSED, but w(F0,G1)=0. This proves I_M D_M⊄V_M with NO reliance on the more elaborate K=AB=BA equality, and no ordinary points. Arrieta (2024) Cor. 4.10 supplies a SPATIAL strongly Hausdorff non-Fsep base, hence the counterexample X can itself be SPATIAL. Banaschewski's Θ={(a,b):a∧u=b∧u}, Φ=Δ imply non-epi, and his Prop. 4.10 predicts nonseparated M (consistent). CAREFUL: Banaschewski Appendix A.6 concerns topological simple extensions, DIFFERENT from frame-single-generator extensions. His sH/nonfit examples are Fsep according to Arrieta (2024), and cannot replace Arrieta's newer existence source. Core proof internally PASS; external independent audit outstanding. Originality unverified.

# Project A — Mixed composition into V FAILS for arbitrary locales: simple-cover transfer of non-F-separatedness

7 November 2026. **NEW WORKING NEGATIVE THEOREM; internal adversarial checks completed; external audit and literature priority still required.** This document supersedes the previous project's “I∘D⊆V universally?” OPEN status. It uses the published existence of strongly Hausdorff but non-F-separated locales, per Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024), 108785; DOI 10.1016/j.topol.2023.108785, arXiv:2310.18522. Do not confuse “Property (F)” of that article with F-separatedness without checking their definitions. Banaschewski (1992), *Singly generated frame extensions*, JPAA 83, 1–21, is relevant to simple coverings; full article not yet checked.

## Notation

For a locale Y, I_Y=cl(Delta_Y)=C(d_I), D_Y=fit(Delta_Y), V_Y=fit(I_Y); I_X∘D_X is localic relational composition, as the image of E=I12∧D23↪X³ under π13. “Strongly Hausdorff” means I_Y=Delta_Y; “F-separated” means D_Y=Delta_Y. S is the Sierpinski locale, e its generating open, and an open sublocale O(a) consists of a part of an ambient locale where a is true.

A basic universal fact (from previous notes): for ANY locale map f:Y→X, the image (f×f)(D_Y) lies inside D_X. Proof: every open O(w) containing Delta_X pulls back along f×f to an open O((f×f)^*w) containing Delta_Y, hence contains D_Y.

## The local witness obtained from non-F-separatedness

Suppose Y is strongly Hausdorff but NOT F-separated:

    I_Y=Delta_Y < D_Y.

Since I_Y=C(d_I), and D_Y is not contained in C(d_I), the restriction of d_I to D_Y is nonzero. Write

    d_I = join_{a∧b=0} a⊠b.

Since the restriction O(Y²)→O(D_Y) is a frame homomorphism (preserves joins), there are nonzero DISJOINT opens u,v∈O(Y) with

    T := D_Y ∧ O(u⊠v) ≠ 0.

T may have NO points. Its universal pair map (y,z):T→Y² lies in D_Y, with y^*u=1, z^*v=1, z^*u=0.

## Transfer construction

Define

    X_u := O(u_1 ∨ e_2) ↪ Y×S,

where e is the nontrivial Sierpinski open and u the Y-open. Let r:X_u→Y be projection. There is a global section s1:Y→X_u, y↦(y,1), and a zero-Sierpinski section over the open O(u)↪Y, y↦(y,0).

Let K=X_u×_Y X_u, the localic kernel pair.

For clarity, let A_X⊆X² be the canonical specialization-order SUBLOCALE imposing f*(a)≤g*(a) for all a∈O(X) on generalized pairs f,g, and B_X=A_X^smile. (The words "canonical specialization relation" do not suffice without this sublocale definition.)

**Lemma (single-generator kernel calculation over an sH base).**

    I_Xu = K = A_Xu B_Xu = B_Xu A_Xu
    and
    D_Xu = V_Xu = fit(K).

Proof: Given ANY locale T' and f,g:T'→X_u with equal base map t:T'→Y, their Sierpinski opens p=f^*e and q=g^*e satisfy (t^*u)∨p=(t^*u)∨q=1. Distributivity gives (t^*u)∨(p∧q)=1 and (t^*u)∨(p∨q)=1, yielding h_- and h_+ over the same base with h_-≤f,g≤h_+. Evaluate on universal K-pair (T'=K), so K≤B A and K≤A B. Since Y is strongly Hausdorff, any specialization-comparable maps into X_u have equal Y-base coordinates: A_Y≤I_Y=Delta_Y. Thus A B,B A≤K. Consequently K=AB=BA. K is closed as inverse image of closed Delta_Y, and contains Delta_X; from AB≤I_X≤K obtain I_X=K. Since Delta≤BA=K≤D_X=fit Delta, fitting hulls give D_X=fit(K)=V_X.

In particular K≤D_X (because BA≤D), and K is an INTERNAL EQUIVALENCE RELATION.

## Open neighborhood of I and nonzero composable-pair witness

On X_u² define the open

    w=e_(first X-coordinate) ∨ u_(base of second X-coordinate).

Because the two base coordinates agree on K, and the defining equation u∨e=1 holds on X_u,

    w|_K=e_1∨u_1=1.

Therefore I_X=K≤O(w), so V_X=fit(I_X)≤O(w).

Now work over the NONZERO locale T=D_Y∧O(u⊠v) from above. Let y,z:T→Y be its universal coordinate maps. Define T-valued maps into X_u:

    x=(y,0), m=(y,1), n=(z,1).

All are valid: u(y)=1 for x; the e=1 coordinate makes the latter two valid. We have

    (x,m)∈K=I_X

because r(x)=r(m)=y. Moreover

    (m,n)∈D_X

because the global section s1:Y→X_u maps D_Y into D_X. Thus (x,m,n):T→X_u³ factors through E=I12∧D23.

But

    w(x,n)=e(x)∨u(n)=0∨0=0.

Since T≠0, E does not lie in O(w13), hence the image R=I_X∘D_X does NOT lie in O(w). As V_X≤O(w), we have

    **I_X∘D_X NOT⊆ V_X.**

Independently of the kernel-pair refinement, the same triple witnesses NONTRANSITIVITY of D_X: F0≤F1 gives (F0,F1)∈D_X by the arbitrary-cover criterion, since for every M-cover {(a_i,b_i)}, ⋁_i F0(a_i,b_i)∧F1(a_i,b_i)=⋁_i h(a_i)=h(u)=1. Also (F1,G1)∈D_X, yet the endpoint pair kills w and D_X≤O(w) (because w contains the diagonal). Thus

    D_X∘D_X NOT⊆ D_X,

although I_X=K is an internal equivalence relation. Since I,D symmetric, taking converses gives

    D_X∘I_X NOT⊆ V_X.

This is a FULL LOCALIC counterexample: no ordinary point of T needed, no assumption of spatiality of any localic product, and the obstruction is exhibited by an explicit map from NONZERO locale T into the composable-pair locale. It does not contradict the universal mixed⊆U inclusion.

## Universal characterization by singly generated Sierpinski gluings

**Corollary (WORKING equivalence).** For any strongly Hausdorff locale Y, the following are equivalent:

(i) Y is F-separated (D_Y=Delta_Y).

(ii) For EVERY u∈O(Y), writing X_u=O(u∨e)↪Y×S, we have I_Xu∘D_Xu⊆V_Xu.

(iii) For EVERY u∈O(Y), the fitted diagonal D_Xu is internally transitive.

Proof: (i)⇒(ii),(iii): Y has closed AND fitted diagonal, so the previously proved single-generator Sierpinski-fiber theorem gives I_Xu=D_Xu=K=ker(X_u→Y), which is fitted and transitive. Conversely, if (i) fails, the nonzero T witness provides u and X_u such that mixed⊄V and D_Xu²⊄D_Xu, contradicting both (ii) and (iii).

Thus the new negative result is not just existential: the entire obstruction is equivalent to F-separatedness of the strongly Hausdorff base, when tested on all one-predicate open extensions.

## Relation to previous positive theorems and the duality discussion

The preceding positive theorem says if Y has Δ_Y BOTH closed and fitted, then ANY sublocale X↪Y×S has I_X=D_X=ker r, hence mixed≤V. The negative construction requires an sH but non-Fsep base, where the base's fitted diagonal defect is transferred into the 1-fiber of X and composed with a nontrivial kernel-pair edge across S-fibers.

The new X_u is actually an OPEN sublocale of Y×S, showing that even an open singly generated frame extension suffices once the base lacks F-separatedness. The easy mixed≤U proof remains true universally; the strict cross-hull inequality W<U was a signal of duality asymmetry but NOT the actual counterexample mechanism. Here the failure is a precise fitting/composition non-distributivity with S=I_X, T=BA_X=K.

## Audit checklist

1. Verify Arrieta's published EXISTENCE statement with exact separation definitions (strongly Hausdorff = I=Delta, F-separated = D=Delta). Avoid confusing a named “Property (F)” with F-separatedness.
2. Verify T≠0 extraction from d_I|_{D_Y}≠0 and rectangle join. This is point-free and uses frame quotient preserving joins.
3. Verify the 1-generator universal K-pair common lower/upper operation and closedness of K.
4. Verify functoriality of fitted diagonal under s1; do not assume open or proper f.
5. Verify that w|_K=1 but w(x,n)=0 on NONZERO T; this is sufficient to refute localic IMAGE containment, without points.
6. Verify D_X^2⊄D_X from I_X≤D_X and I_X D_X⊄D_X.
7. Search priority: perhaps categorical kernel-pair/fitted-diagonal stability results have this characterization; Banaschewski's 1992 singly generated frame extensions should be read before claiming novelty.

**Verdict:** Negative solution is an internally checked WORKING theorem. Independent external blind audit should be requested before publication claim.

## Canonical single-open witness: disjoint v can be chosen as u*

The definition of d_I simplifies:

    d_I=join_{a∧b=0}a⊠b = join_{a∈O(Y)}a⊠a*.

For a∧b=0, b≤a*, hence a⊠b≤a⊠a*, while each (a,a*) is disjoint. Thus when D_Y>Delta_Y=C(d_I), there is some u with

    T_u=D_Y∧O(u⊠u*)≠0.

Its universal maps y,z satisfy y*u=1 and z*u*=1, hence z*u=0. The entire counterexample proof works taking v=u* instead of an independently chosen disjoint v. This presents the negative result as a genuinely **single-open-transfer theorem** from a sH but non-Fsep base, appropriate to comparison with singly generated frame extensions.

## Literature-source confirmation

The journal page of Arrieta (2024), DOI 10.1016/j.topol.2023.108785, explicitly states in its abstract that the strong Hausdorff property does NOT imply F-separatedness and that F-separated means 'fitted diagonal'. This is exactly the external existence theorem required by the construction; no auxiliary 'Property (F)' claim is used.

The journal page of Banaschewski (1992), DOI 10.1016/0022-4049(92)90101-K, confirms the article's title and its systematic study of frame extensions generated by one new element, including separation axioms. The full article still needs to be checked for priority; no proof claim here is attributed to it.
