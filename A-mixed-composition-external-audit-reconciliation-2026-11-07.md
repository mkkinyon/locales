# Project A — Post-referee reconciliation of the mixed-composition negative theorem

**7 November 2026.** This note reconciles the independent blind referee report `ProjectA_mixed_composition_EXTERNAL_BLIND_referee_report_2026-11-07.md` with its follow-up comparison `ProjectA_mixed_composition_EXTERNAL_vs_INTERNAL_audit_comparison_2026-11-07.md` and our [internal adversarial audit](A-mixed-composition-internal-audit-and-banaschewski-2026-11-07.md).

**Status:** the core negative transfer theorem and spatial strengthening have PASSED both independent and internal audits. The subsidiary kernel-pair theorem and F-separatedness characterization are CORRECT but need the explicit generalized-point lemma and reordered exposition below. Literature PRIORITY not certified; do not equate "no antecedent located" with "novel."

## 1. Central result certified independently

There exists a **spatial locale** X such that

    I_X∘D_X NOT≤ V_X=fit(I_X),

and both D_X∘I_X NOT≤V_X and D_X∘D_X NOT≤D_X can be obtained from the same witness. Arrieta (2024), Corollary 4.10, supplies a SPATIAL strongly Hausdorff but non-F-separated base Y; this is a published existence result, not reproved here.

Composition convention: R∘S is **diagrammatic** (first R then S) and means the image under π13 of R12∧S23↪X³. Here R12=π12^{-1}(R), etc. No ASSOCIATIVITY of arbitrary localic relational images is assumed in this proof.

### 1.1 Minimal frame proof — independent of the kernel-pair refinement

Let L=O(Y), I_Y=cl(Δ_Y)=Δ_Y and D_Y=fit(Δ_Y)≠Δ_Y. Since

    d_I=join_{a∧b=0}a⊠b=join_{a∈L} a⊠a*,

there is some u∈L for which T=D_Y∧O(u⊠u*) is NONZERO. Put N=O(T) (nontrivial frame). Its coordinate maps h,k:L→N satisfy

    h(u)=1,  k(u*)=1,  k(u)=0,
    join_{a∈C}h(a)∧k(a)=1 for EVERY cover C of 1.

Following Banaschewski (1992), Proposition 2.1, identify O(Y×S) with P={(a,b)∈L²:a≤b}. The extension

    X=O(u∨σ)⊆Y×S

has frame

    M=O(X)={(a,b)∈L²:a≤u,a≤b}, with top (u,1).

The embedded base is η(a)=(a∧u,a), and σ=(0,1) is the additional open, satisfying η(u)∨σ=1_M. Define three genuine FRAME maps M→N:

    F0(a,b)=h(a),   F1(a,b)=h(b),   G1(a,b)=k(b).

The fact h(u)=1 is essential for F0 to preserve top. Since F0≤F1 pointwise, the pair (F0,F1) factors through **both** I_X and D_X. The first assertion follows from the disjoint-rectangle test; the second directly from the cover criterion. For every cover {(a_i,b_i)} of (u,1),

    join_i F0(a_i,b_i)∧F1(a_i,b_i)=join_i h(a_i)=h(u)=1.

Likewise (F1,G1) factors through D_X since the b_i cover 1 and h,k satisfy every L-cover test. (This verifies D_X∘D_X failure without using I_X≤D_X.)

Let r:X→Y be the base projection and K=X×_Y X its kernel pair. Since Δ_Y is CLOSED, K is closed and contains Δ_X, hence I_X≤K. Set

    w=σ_1∨η(u)_2 ∈ O(X²).

On K the base coordinates agree, so w|_K=σ_1∨η(u)_1=1. Thus I_X≤O(w), V_X=fit I_X≤O(w); also D_X=fit Δ_X≤O(w), since O(w) contains Δ_X.

But the endpoint generalized pair (F0,G1) evaluates w to

    F0(σ)∨G1(η(u))=h(0)∨k(u)=0≠1_N.

The triple (F0,F1,G1) factors through I12∧D23 AND, separately, through D12∧D23. Its nonzero source T therefore witnesses both

    I_X∘D_X NOT≤ V_X,   D_X∘D_X NOT≤D_X.

Taking converses gives D_X∘I_X NOT≤V_X. The criterion used is: for a map p:W→Z, im(p)≤O(w) iff p*(w)=1; no point-set composition or spatiality of the triple product is being assumed.

### 1.2 Stronger structural theorem (separate from the minimal proof)

For EVERY strongly Hausdorff Y and u∈O(Y), let X_u=O(u∨σ) and r:X_u→Y. Then

    K=ker r = I_X = A_X∘B_X=B_X∘A_X,
    D_X=V_X=fit(K),

where A_X is the **sublocale** of X² obtained by imposing f*(a)≤g*(a) for all a∈O(X) on generalized points, and B_X=A_X^smile. The frame representation of maps into X_u is:

    f_{φ,p}(a,b)=φ(a)∨(φ(b)∧p),
    φ:L→N frame hom, p∈N, φ(u)∨p=1.

Over the universal K pair (same φ, parameters p,q), p∧q and p∨q both define maps because φ(u)∨(p∧q)=1 and φ(u)∨(p∨q)=1. They give common lower and upper specializations. Thus K≤B A and K≤A B. Universally B A≤D and A B≤I; and strong Hausdorffness of Y makes K closed, so I≤K. Also A,B≤K, hence their composites lie in K (a kernel pair is transitive). Therefore all of K,AB,BA,I coincide, and fitting gives D=fit(K)=V. Do not invoke associativity of arbitrary composites for these direct inclusions.

It follows that I_X=K is an internal EQUIVALENCE relation, even though D_X may be nontransitive.

### 1.3 Characterization

For any strongly Hausdorff Y, the following are equivalent:

1. Y is F-separated (D_Y=Δ_Y).
2. For **every** u∈O(Y), X_u satisfies I_Xu∘D_Xu≤V_Xu.
3. For **every** u∈O(Y), D_Xu is internally transitive.

If Y is F-separated, K is fitted as a pullback of Δ_Y and the preceding theorem gives I=D=V=K, so all conditions hold. Conversely, if Y is not F-separated, §1.1 constructs a u refuting both properties. The closed/fitted-pullback facts used here are standard: preimages of C(d) are C(f*d), and preimages of meets of open sublocales are meets of their open preimages.

## 2. Reconciliation of comparison D1–D9

- **D1 — genuine dependency omission, FIXED:** the direct arbitrary-cover calculation establishes (F0,F1)∈D, so nontransitivity no longer depends on §1.2.
- **D2 — essential missing argument, FIXED:** define the specialization SUBLOCALE A_X and give the common-upper/common-lower K-pair factorization; strong Hausdorffness alone supplied only I≤K.
- **D3 — contingency discharged:** preimages preserve closed and fitted sublocales, with the direct formulas in §1.3.
- **D4 — terminology correction:** call X_u a **singly generated frame extension**, an **open Sierpiński gluing**, or "Y with a closed copy of u adjoined." Do NOT call it a "topological simple extension" in the sense of Banaschewski Appendix A.6 (dense open subspace, discrete remainder).
- **D5 — stronger pointlessness observation:** for Arrieta's SPATIAL Hausdorff base Y, T=D_Y∧O(u⊠u*) is necessarily POINTLESS, since ordinary points of D_Y are diagonal while u∧u*=0. The induced point-set relational composition in X_u does lie inside the points of V_Xu: this negative theorem is **invisible on ordinary point sets**.
- **D6 — image step supplied:** the last paragraph of §1.1 explicitly invokes im(p)≤O(w) iff p*w=1.
- **D7 — notation/exposition:** define πij pullbacks, diagrammatic order, σ rather than Banaschewski's e=top, and the restriction notation; explain precisely where the base's two hypotheses enter.
- **D8 — OUTSIDE BLIND AUDIT:** Banaschewski Appendix A.6 and Arrieta 2024 Proposition 4.1 are priority/terminology evidence relevant to our earlier strong-Hausdorff gluing lemma, not evidence for novelty of the new mixed-composition transfer. Check hypotheses carefully before saying "subsumed."
- **D9 — OUTSIDE BLIND AUDIT:** earlier proper-base-change, distributor, finite-generator/regular-base, and coherent composition theorems were NOT covered by these audits; their status remains working pending separate audit.

## 3. Important NEW audit flag — association of localic relational composition

The external referee explicitly notes that relational composition formed with LOCALIC IMAGES of pullbacks need not be associative in general, because localic images are not always stable under pullback. The 7 Nov negative theorem needs only ONE binary composition and is completely unaffected.

Earlier project notes sometimes used associativity without a separate hypothesis (especially "A I D = I D" module/distributor identities and alternating-word semigroup calculations). **Do NOT automatically promote those computations from pointwise/spectral contexts to arbitrary locales.** They require a stand-alone categorical audit: either prove the relevant image pullback stability (for example in coherent spectral/proper cases) or replace associative rewrites by direct generic-point / explicit span arguments. No counterexample to any particular earlier formula is claimed here.

This associativity warning is mathematically material for the *broader composition programme* even though it is an expository convention for the negative theorem packet.

## 4. Literature and priority

Banaschewski (1992), Prop. 2.1 supplies the frame pair model; Props. 3.2 and 4.10 independently confirm X_u non-epic and not strongly Hausdorff for u≠0 over sH Y. His Appendix "simple extension" is DIFFERENT. Arrieta (2024), Cor. 4.10 supplies the spatial sH-but-not-Fsep base, and his Prop. 2.1 supplies the closed equalizer pullback property. The external referee found no antecedent to the **mixed composition negative transfer** in the sources it could access, but did not examine the full APP 2022 paper, Picado–Pultr monograph, or Arrieta thesis. **Priority therefore remains unresolved**; expository readiness is not originality.

## 5. Disposition

Accept the main negative theorem and its spatial strengthening as independently refereed (with a full proof now in §1.1); accept nontransitivity and the equivalence in §1.3 with the repaired proofs; update terminology in all future writeups. If preparing a manuscript, lead with the explicit witness or the F-separatedness characterization, explain why the witness is pointless, and include the source definitions and the composition/image lemma.

**Next audit target:** associativity or nonassociativity of localic image-defined relation composition and its impact on the earlier two-idempotent/coherent and arbitrary-locale module calculations. This is separate from the present certified result.
