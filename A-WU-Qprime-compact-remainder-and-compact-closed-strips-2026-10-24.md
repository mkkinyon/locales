# Project A — Q': Compact remainder and compact-closed-neighborhood localization

24 October 2026. **New working mathematical deductions, checked internally, not externally audited or priority checked.** Builds on [Claude follow-up localization](A-WU-external-referee-followup-response-2026-10-24.md) and [our reconciliation](A-WU-referee-followup-reconciliation-2026-10-24.md).

Let L be a frame, Q=L⊕L, D=fit(Delta), D2=finite-cover fitting, W=cl(D)=C(d_W), W2=cl(D2)=C(d_W2), and Phi,Phi2 the full- and finite-square-cover pre-nuclei. We know d_W2≤d_W and d0:=d_W2 is Phi2-fixed.

## 1. Compact closed remainder of the hyperconnected locus

Let h_hc=join of all nonzero hyperconnected opens of L, and o_hc=h_hc⊠1∨1⊠h_hc. The previously audited referee theorem gives

    d_W∧o_hc=d_W2∧o_hc.

**Theorem (new working).** If the closed sublocale C(h_hc) is compact, then W=W2.

Proof. For every full open cover C, compactness in the quotient frame ↑h_hc supplies finitely many c_1,...,c_n∈C with h_hc∨c_1∨...∨c_n=1. Let F={h_hc,c_1,...,c_n}, a finite cover. For x≤w_C→d0, we have x≤Phi(d0)≤d_W, so

    x∧(h_hc⊠h_hc)≤d0,

by localization. Also x∧(c_i⊠c_i)≤x∧w_C≤d0. Thus x∧w_F≤d0, whence x≤w_F→d0≤Phi2(d0)=d0. Therefore Phi(d0)=d0 and d_W=d0.

In particular Q' can fail only if C(h_hc) is NONCOMPACT. This is stronger than merely requiring h_hc≠1.

## 2. A finite-cover basis on a compact-closed-neighborhood strip

Let k∈L with the closed sublocale C(k) compact. Let C be ANY open cover of 1. By compactness of C(k), choose c_1,...,c_n∈C such that

    k∨c_1∨...∨c_n=1.

The finite cover F={k,c_1,...,c_n} satisfies, on the open strip t=k*⊠1,

    t∧w_F ≤ t∧w_C,

because t∧(k⊠k)=0 and the c_i-squares are members of w_C. Thus for every full diagonal neighborhood, the restriction to O(t) contains the restriction of SOME finite diagonal neighborhood. Hence

    D∧O(k*⊠1)=D2∧O(k*⊠1),

and symmetrically for 1⊠k*. **Only one coordinate needs to lie in the interior of a compact closed sublocale.**

Put

    h_cc=join{k*: C(k) is compact},
    o_cc=h_cc⊠1∨1⊠h_cc.

Since the displayed strips cover O(o_cc), we obtain

    D∧O(o_cc)=D2∧O(o_cc).

Localic closure commutes with restriction to an OPEN sublocale (in the relative locale), so also

    W∧O(o_cc)=W2∧O(o_cc).

**Theorem (new working).** If h_cc=1 then D=D2, without global compactness or complemented compact generators. Topologically: a sober space with a basis of opens lying in compact CLOSED subsets satisfies equality of finite and arbitrary cover fittings.

## 3. Combined Q' localization and compactness

Let e=h_hc∨h_cc and o_e=e⊠1∨1⊠e. Combining Claude's strip result with §2,

    W∧O(o_e)=W2∧O(o_e).

Equivalently, discrepancies between their closed hulls are confined to C(e)×C(e).

**Combined theorem (new working).** If C(e) is compact, then W=W2.

Proof: repeat the argument of §1 replacing h_hc with e; agreement of W,W2 on O(o_e) supplies x∧(e⊠e)≤d0, while compactness of C(e) supplies finite c_i with e∨⋁c_i=1. The finite cover {e,c_i} forces x≤d0 for each x≤w_C→d0; therefore Phi(d0)=d0.

Consequently Q' may fail only if the closed remainder C(h_hc∨h_cc) is NONCOMPACT. If h_hc∨h_cc=1 then Q' holds automatically.

This theorem is only a sufficient condition. In particular, it does NOT assert Q' universally.

## 4. Correction: the referee's two-apex space is COMPACT

The earlier referee and reconciliation called X=R⊔{p,q}, with cofinite positive tails at p and cofinite negative tails at q, noncompact. That is FALSE. Any open cover contains a p-neighborhood covering all but finitely many positives and a q-neighborhood covering all but finitely many negatives; finitely many remaining exceptional points, including 0, finish the subcover. Thus X is compact. Its relations I<W=W2=cl(int U)<U and two-point boundary G remain valid; D=D2 follows from compactness.

A genuinely noncompact non-Hausdorff example with I<U and D=D2 is X×R: X is compact and R has compact closed interval neighborhoods, so for any (x,t) a compact closed neighborhood X×[t-1,t+1] exists. Thus h_cc=1 and D=D2. The product is noncompact because its projection onto R is surjective, and the I<U relation persists by coordinatewise product formulas.

## 5. Next tests

- Seek a locale with C(h_hc∨h_cc) genuinely noncompact and with nonregular Urysohn boundary. The necessary conditions are not sufficient.
- In general, Q' is equivalent to Phi(d_W2)=d_W2. A counterexample would require an infinite-cover diagonal descent defect not locally controllable by any compact closed neighborhood or hyperconnected open strip.
- Do not call the current structural class a named separation axiom before checking literature.

## 6. Isbell/atomic positive criterion for Q'

Let B(W2) denote the least dense Boolean sublocale of W2. Since D2 is dense in W2, Isbell density gives B(W2)≤D2.

**Proposition (working).** If B(W2) is spatial, equivalently its complete Boolean frame is atomic, then W=W2.

Proof. Every point of the spatial B(W2) factors through D2, hence through D because D and D2 have the same locale points (the binary-versus-arbitrary cover point test). Since B(W2) is the join of its points as a spatial sublocale, B(W2)≤D. But B(W2) is dense in W2, so W2≤cl D=W. The reverse inequality W≤W2 is universal.

Thus a counterexample to Q' requires not only a noncompact residual C(h_hc∨h_cc), but also a non-atomic Booleanization of W2 (at least one nonzero atomless component).

## 7. Stress test outside the covering criterion

Let S=P(N)\{empty} with Scott topology, and Y the compact two-apex space in §4. The product Z=S×Y is sober, locally compact, noncompact, with no nonzero hyperconnected open, so h_hc(Z)=0: every nonempty open contains a basic product A×B, and the Y-factor B can be split into two disjoint nonempty opens. Also h_cc(Z)=0: every nonempty A⊆S is dense, so any compact CLOSED subspace of Z containing a nonempty open rectangle contains S×{y} for some y. Its projection onto S would be all of S, contradicting noncompactness of S.

The Urysohn relation of Z is U(Z)=S²×U(Y). The regular-closed core is S²×K(Y), and the remaining open sector is S²×{(p,q),(q,p)}. The binary cover of Y by Y\{p},Y\{q} pulls back to Z and excludes this ENTIRE sector from D2(Z). Consequently W(Z)=W2(Z)=S²×K(Y).

This example meets the topological noncompact remainder conditions h_hc=h_cc=0 with G≠0 but still satisfies Q', showing the new conditions necessary for failure are far from sufficient. Note B(O(S²))=2 because S² is hyperconnected, so the Booleanization of the boundary sector is atomic; this provides a separate explanation through the earlier boundary-atomicity theorem. Do NOT claim that a noncompact Scott factor automatically creates an atomless Boolean boundary.
