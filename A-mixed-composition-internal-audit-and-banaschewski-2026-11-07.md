# Project A — Banaschewski reading and internal adversarial audit of mixed composition

**7 November 2026. Internal audit verdict: principal negative transfer PASSES; EXTERNAL BLIND AUDIT STILL PENDING.** This is a post-source audit memo, not the source of the original proof or an independent referee report.

## Sources and distinctions

Read user-uploaded B. Banaschewski, *Singly generated frame extensions*, J. Pure Appl. Algebra 83 (1992) 1–21, especially Proposition 2.1 (free extension P={(a,b):a≤b}), Proposition 2.2/Definition 2.3 (defining congruences), Proposition 3.2 (epic condition), Definition 4.2 (separated = Isbell strong Hausdorff), Proposition 4.10 (for separated base L, L[c] separated iff inclusion epic), and Proposition A.6 (topological simple extensions, a DIFFERENT notion). Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024), 108785, DOI 10.1016/j.topol.2023.108785, **Corollary 4.10**, explicitly gives **SPATIAL** strongly Hausdorff, non-F-separated locales. His introduction warns Banaschewski's older strongly Hausdorff/non-fit simple extension examples are nevertheless F-separated; NONFIT cannot substitute for non-Fsep.

## The short independent frame proof

Let Y be strongly Hausdorff, not F-separated, L=O(Y), I_Y=C(d_I)=Δ_Y and D_Y>Δ_Y. Since

  d_I=join_{a∧b=0} a⊠b=join_a a⊠a*,

restriction to D_Y (a frame homomorphism) yields an open u with NONZERO T=D_Y∧O(u⊠u*). Let N=O(T)≠1, and let h,k:L→N be coordinate maps. Then h(u)=1, k(u*)=1, k(u)=0, and for every cover C of L,

  join_{a∈C} h(a)∧k(a)=1.

Take Banaschewski's free extension P={(a,b)∈L²:a≤b} and restrict to open (u,1). The resulting singly-generated frame

  M={(a,b):a≤u, a≤b},   top=(u,1),

has base injection η(a)=(a∧u,a), and new generator c=(0,1), satisfying c∨η(u)=1. Every (a,b) is η(a)∨(η(b)∧c).

Three frame homomorphisms M→N are

  F0(a,b)=h(a),    F1(a,b)=h(b),    G1(a,b)=k(b).

F0 PRESERVES TOP because h(u)=1. We have F0≤F1, so (F0,F1) factors through I_M (disjoint-pair test). For any cover {(a_i,b_i)} of M, the b_i cover 1 in L, and hence join_i F1(a_i,b_i)∧G1(a_i,b_i)=1, so (F1,G1) factors through D_M.

The kernel pair K of the base projection r:X_M→Y is CLOSED because Δ_Y is closed. Since K contains Δ_M, I_M≤K. Put w=c_1∨η(u)_2. On K the base coordinates coincide, so w=c_1∨η(u)_1=1; thus V_M=fit(I_M)≤O(w). But on the endpoint pair (F0,G1), w evaluates to F0(c)∨G1(η(u))=h(0)∨k(u)=0. Because N is nontrivial, the composable-pair sublocale has a genuine NONZERO generalized-point source violating w. Therefore

  **I_M∘D_M NOT≤V_M.**

No ordinary points or spatiality assumptions on the witness T were used.

## Further audited claims

* By taking converses, D_M∘I_M NOT≤V_M.
* Since I_M≤D_M and D_M≤O(w), the same triple proves D_M∘D_M NOT≤D_M; the fitted diagonal is nontransitive.
* For this particular M, generalized maps with equal base have meet/join Sierpinski predicate values and hence common lower/upper specializations, so K=A_M B_M=B_M A_M; the sH base implies I_M=K, and then D_M=V_M=fit(K). This is valid but is NOT NEEDED for the main proof.
* For a strongly Hausdorff base Y, F-separatedness iff for ALL u the associated X_u has I D≤V, iff for ALL u its D is transitive. If Δ_Y is also fitted, K is fitted and one-predicate meet/join forces I=D=K; if not, the above construction gives a bad u.
* By Arrieta (2024), Y can be SPATIAL. O(Y)⊕3=P is spatial whenever Y is spatial (evaluation at S=0 and S=1 jointly distinguishes frame elements), and the open X_u is spatial. Thus the negative theorem can be witnessed by a spatial locale.

## Independent Banaschewski consistency check

For c=(0,1), η(a)∨c=(a∧u,1), η(a)∧c=(0,a). Banaschewski's defining congruences are therefore Θ={(a,b):a∧u=b∧u} and Φ=Δ_L. Since u≠0, Θ∨Φ=Θ is not the universal congruence. Proposition 3.2 gives NONEPIC extension, and Proposition 4.10 yields NONSEPARATED extension over a separated base, consistent with I_M=K>Δ_M.

## Adversarial audit details and scope

Checked: nonzero rectangle extraction through a JOIN-PRESERVING frame quotient (do not illicitly distribute arbitrary sublocale meets over joins); preservation of top by F0; EVERY cover test for (F1,G1); K closed; w|K=1; w(endpoint)=0 on nonzero source; passage to localic relational image. Found **no invalid implication** in the core transfer. The condition T≠0 does NOT imply any ordinary point exists.

Literature correction: our earlier Hausdorff gluing criterion is closely related to Arrieta (2024), Proposition 4.1, explicitly a generalization of Banaschewski (1992) Proposition A.6. Do NOT claim novelty for its spatial-multiplier form. Originality of the NEW mixed-composition transfer remains unverified. The earlier finite-generator/regular-base and proper-base-change working results were not fully reaudited in this segment.

**Decision:** request an independent BLIND audit of the main frame construction, the source existence statement, the kernel-pair refinement, and the exact F-separatedness equivalence. Blind auditors should not see this internal verdict before writing their reports.

## 7 Nov 2026 addendum — Independent referee comparison and corrections

The blind external referee subsequently received the INTERNAL audit only after completing its own report. Both independently certified the headline negative theorem and spatial strengthening. The post-referee reconciliation is in [A-mixed-composition-external-audit-reconciliation-2026-11-07.md](A-mixed-composition-external-audit-reconciliation-2026-11-07.md).

Corrections to this internal record:
1. The assertion that D∘D⊄D is independent of the kernel-pair refinement was previously justified via I≤D, which was proven only in that refinement. The correct INDEPENDENT proof is F0≤F1 ⇒ (F0,F1)∈D by the ALL-cover criterion, using ⋁_i h(a_i)=h(u)=1 for every cover of the extension M.
2. The kernel-pair refinement was too compressed: sH(Y) proves I_X≤K; the reverse K≤I_X requires the common-upper construction (p∨q). K≤D_X requires common lower (p∧q), and A_X must be defined as an actual specialization-order SUBLOCALE, not merely an order on maps.
3. The former "contingency" about pullback stability of closed/fitted sublocales is discharged by standard pullback formulas and Arrieta (2024), Prop. 2.1.
4. Avoid "topological simple extension" for this X_u: Banaschewski's Appendix uses the term for a dense open extension with discrete remainder. Prefer "singly generated frame extension" or "Sierpinski gluing".
5. For Arrieta's SPATIAL Hausdorff base, T is necessarily POINTLESS (not just possibly pointless) and the ordinary-point zigzags satisfy the mixed inclusion. The localic image failure is genuinely point-free.

The blind referee also warned that image-defined localic relational composition may fail associativity in Loc; this does not affect the certified negative theorem, but does require a separate audit of earlier arbitrary-locale and coherent composition manipulations using associativity.

**Updated decision:** core theorem fully independently referee-verified; subsidiary claims verified after proof/exposition repairs; priority remains open. The historical text above is preserved for transparency.
