# Independent blind referee report — Project A, open/closed two-sheet theorem

**15 November 2026**

**Materials:** External blind prompt and packet dated 15 November 2026.

**Independence:** No internal audit or earlier referee report was consulted.

## Overall verdict

**Positive.** Claims 1–4 are correct as stated. The Cantor example gives the claimed failure of preservation of arbitrary joins. Neither compactness nor spatiality of the zero-dimensional locale \(K\) is needed, and source sublocales need not be closed.

| Claim | Verdict | Reason |
|---|---|---|
| (B2), cross-sheet relation | **Proved** | Correct on generalized points with arbitrary test locales. |
| (B4), arbitrary first-sheet source | **Proved** | Both the image lower bound and fitting upper bound are valid. |
| (B7), finite-join propagation | **Proved** | Uses coframe distributivity and saturation monotonicity only. |
| (B8), one-step theorem | **Proved** | Open/closed decomposition and ambient fitness are sound. |
| (C3), infinite-join failure | **Proved** | The Cantor remnant is nonzero but pointless. |

I found no false or unproved assertion in the packet. The editorial suggestions at the end are minor.

## 1. Preliminary and structural checks

The relation in (A1) is representable: for each \(a\in\mathcal O(X)\), the inequality \(f^*a\leq g^*a\) is the equalizer condition \(f^*a=f^*a\wedge g^*a\) between maps to the Sierpiński locale. Intersect these equalizer sublocales over all \(a\). The result satisfies (A1) for every test locale. Reflexivity is immediate; furthermore, if \(S\leq O_X(a)\), comparability of \((f,g)\) with \(f\) in \(S\) implies \(g^*a=1\). Thus the image in (A2) lies in every open containing \(S\), which proves (A3).

The diagonal hypothesis implies \((c,c)\in L\) for every \(c\in\mathcal O(K)\): write \(c\) as a join of complemented opens below it, then take the corresponding coordinatewise join. Also \((0,c)=e\wedge(c,c)\) and \((c,1)=e\vee(c,c)\) show directly that the open and closed sheets have frame \(\mathcal O(K)\).

The sublocales \(F=C_Z(e)\) and \(U=O_Z(e)\) satisfy \(F\wedge U=0\), \(F\vee U=Z\). In the distributive sublocale coframe, therefore, every sublocale \(G\) decomposes as

\[
G=(G\wedge F)\vee(G\wedge U). \tag{1}
\]

This is **finite** distributivity, even when \(G\) has no points.

## 2. Claim 1: the four blocks of specialization

Let \(E\) be an arbitrary locale, and consider \(f_0,g_0:E\to K\) representing a pair \(E\to F\times U\).

If the pair is comparable, every complemented \(d\) supplies \(f_0^*d\leq g_0^*d\), and its complement supplies \(f_0^*d^c\leq g_0^*d^c\). These are complementary pairs of opens of \(E\), so both inequalities are equalities. Since the complemented opens generate \(\mathcal O(K)\), we get \(f_0=g_0=h\). Comparison on all \((1,v)\in L\) then says \(h^*v=1\), precisely the condition that \(h\) factors through \(P\).

Conversely, take \(h:E\to P\), a global \((c,v)\in L\), and complemented \(d\leq c\). The coordinatewise identity is indeed

\[
((c,v)\wedge(d,d))\vee(d^c,d^c)
=(1,(v\wedge d)\vee d^c)
=(1,v\vee d^c).
\]

Since \(h:E\to P\), this gives \(h^*(v\vee d^c)=1\), hence \(h^*d\leq h^*v\). Joining over all complemented \(d\leq c\), and using preservation of arbitrary joins by \(h^*\), gives \(h^*c\leq h^*v\). Thus the pair is comparable. This proves (B2) as an equality of **sublocales**, not merely of point sets.

For pairs within the same sheet, complemented opens and their complements again force equality of the maps; reflexivity supplies the reverse inclusion. For the block \(U\times F\), comparison on \(e=(0,1)\) forces \(1\leq0\) in \(\mathcal O(E)\), so only the zero locale can serve as test domain. Thus this block is zero.

Consequently, the relation has precisely three potentially nonzero blocks: the diagonal on \(F\), the diagonal on \(U\), and the oriented diagonal of \(P\) from \(F\) to \(U\).

## 3. Claim 2: arbitrary first-sheet sublocales

Take **any** sublocale \(H\leq K\), and let \(T=\operatorname{fit}_Z(H_F)\). The diagonal part of \(\mathcal A(Z)\) contributes \(H_F\) to saturation. Its cross block, intersected with \(H_F\times U\), is \(\Delta_K(P\wedge H)\). Projection to the second factor has image exactly \((P\wedge H)_U\). Thus

\[
H_F\vee(P\wedge H)_U
\leq\operatorname{Sat}(H_F)\leq T. \tag{2}
\]

Every global open \((1,v)\in L\) contains \(H_F\). Meeting its upper-sheet traces gives \(T\wedge U\leq P_U\).

Every \(c\) satisfying \(H\leq O_K(c)\) supplies a diagonal global open \((c,c)\) containing \(H_F\). Its trace on either sheet is \(O_K(c)\). Since \(K\) is fit, meeting over all such \(c\) gives

\[
T\wedge F\leq H_F,\qquad T\wedge U\leq H_U.
\]

The first is equality because \(H_F\leq T\wedge F\). Combining the second with the previous bound and applying (1) gives

\[
T=(T\wedge F)\vee(T\wedge U)
\leq H_F\vee(P\wedge H)_U.
\]

This and (2) establish (B4). The proof uses arbitrary meets of sublocales and finite distributivity, but **never** distributes a finite meet over an arbitrary join in the sublocale coframe. It works for a pointless, nonclosed, noncompact \(H\) without change.

## 4. Claims 3–4: finite joins and all sources

For fitted \(R=\bigwedge_iO_i\) and \(S=\bigwedge_jV_j\), the coframe law gives

\[
R\vee S=\bigwedge_{i,j}(O_i\vee V_j).
\]

The joins \(O_i\vee V_j\) are open, so finite joins of fitted sublocales are fitted. Hence fitting preserves binary joins, and monotonicity of saturation proves (B7) exactly as written. No preservation of joins by saturation is assumed.

For arbitrary \(G\leq Z\), equation (1) gives \(G=H_F\vee C_U\). Because \(U\cong K\) is fit, \(C\) is a meet of open sublocales of \(U\). Every such open is open in \(Z\), since \(U\) itself is open; meets of sublocales below \(U\) agree in \(U\) and \(Z\). Hence \(C_U\) is fitted **in the ambient locale**, and (A3) gives \(\operatorname{Sat}(C_U)=C_U\).

By (B4) and (B7),

\[
\operatorname{Sat}(G)=\operatorname{fit}(G)
=G\vee(P\wedge H)_U.
\]

This proves (B8). Since fitting is idempotent, saturation is idempotent on every sublocale. Compactness and spatiality of \(K\) played no role.

## 5. Cantor consistency test

Here \(K\) is the compact perfect Cantor space, and \(L\) is defined by (C1).

**The frame \(L\).** Given an arbitrary coordinatewise join \((c,v)=\bigvee_i(c_i,v_i)\), its exceptional set \(D=c\setminus v\) is locally discrete: each \(x\in c\) has a neighborhood \(c_i\ni x\) on which \(D\cap c_i\subseteq c_i\setminus v_i\). Moreover \(D\) is relatively closed, as \(v\) is open. For a finite meet, the exceptional set is a finite union of relatively closed discrete sets restricted to \(c_1\cap c_2\), hence closed discrete. Thus \(L\) is a subframe with the required diagonal opens and \(e\).

**Why \(P\) is nonzero and pointless.** For \((1,v)\in L\), \(K\setminus v\) is a compact closed discrete space, hence finite. Conversely, every finite deletion occurs. Therefore

\[
P=\bigwedge_{p\in K}O_K(K\setminus\{p\}). \tag{3}
\]

Every punctured open is dense, since Cantor space has no isolated points. The Booleanization \(B_K\) lies in every dense sublocale: for a dense nucleus \(j\), one has \(j(a)\wedge a^*=0\), so \(j(a)\leq a^{**}\). Thus \(B_K\leq P\). The double-negation nucleus fixes \(0\) and \(K\neq0\), so \(B_K\neq0\); hence \(P\neq0\). But no point belongs to every punctured open, so **\(P\) has no points**. This verifies (C2) without relying on the previous referee.

**Ancillary assertions.** The frame \(L\) is spatial because distinct pairs of opens are distinguished by points in one of the two Cantor coordinates. Any point of \(Z\) sends \(e\) to either \(0\) or \(1\), and accordingly factors through \(F\) or \(U\); thus there are exactly the two sheets of points, and the resulting space is sober. It is \(T_1\): diagonal clopens separate different \(K\)-coordinates, \(e\) separates upper from lower, and \((d,d\setminus\{p\})\), with \(d\) clopen containing \(p\), separates \(p_F\) from \(p_U\) in the other direction.

Compactness follows by restricting an open cover to both compact copies of \(K\) and taking a finite subcover on each. Local compactness also holds. Upper points have compact-open neighborhoods \((0,d)\), and lower point \(p_F\) has a neighborhood basis of \((d,d)\) or \((d,d\setminus\{p\})\), with \(d\) clopen. The closed discrete exceptional set allows choosing these below any given neighborhood. The first kind is compact by clopenness. For the second kind, an open cover of \((d,d\setminus\{p\})\) has finitely many members covering compact \(d_F\); their upper coordinates miss only a closed discrete, hence finite, subset of compact \(d\). Finitely many further members cover the remaining upper points. Thus the second kind is compact.

**Failure of infinite joins.** Pointlessness gives \(P\wedge[p]=0\) for every point sublocale \([p]\). By (B4), each \([p_F]\) is fitted and fixed by saturation; upper-sheet points are fitted because \(U\) is open and fit. But \(\operatorname{fit}(F)=F\vee P_U>F\), while spatiality gives \(\bigvee_{p\in K}[p_F]=F\). Therefore

\[
\operatorname{Sat}\left(\bigvee_{p\in K}[p_F]\right)
=F\vee P_U\neq F
=\bigvee_{p\in K}\operatorname{Sat}([p_F]).
\]

This proves (C3). The mechanism is exactly the generally invalid infinite distributive law in the sublocale coframe:

\[
P\wedge\left(\bigvee_{p\in K}[p]\right)=P,
\qquad
\bigvee_{p\in K}(P\wedge[p])=0.
\]

It has no bearing on the *finite* coframe distributivity used in (B7).

## 6. Control cases and attempted falsification

* **Full product:** If \(L=\mathcal O(K)^2\), then \((1,0)\in L\), so \(P=0\); fitting and saturation are the identity on a disjoint sum of fit locales.
* **Upper triangular:** If \(L=\{(c,v):c\leq v\}\), then \(P=K\), and the upper sheet acquires exactly \(H_U\). With \(K\) a singleton, this is the three-element Sierpiński locale, the smallest nontrivial test.
* **Pointless, noncompact test:** A complete atomless Boolean algebra gives a zero-dimensional locale with no points. Taking the upper-triangular gluing gives \(P=K\), and the generalized-point argument remains valid; the theorem does not depend covertly on spatiality or compactness.
* **Role of zero-dimensionality:** Without it, the disjoint sum of Sierpiński locales already has non-diagonal same-sheet specialization. The complemented-open hypothesis is genuinely used.

No counterexample satisfying the packet's precise hypotheses emerged.

## 7. Presentation recommendations

1. State the three-block description of \(\mathcal A(Z)\) after (B2). It makes the one-step phenomenon intuitive.
2. Explain explicitly that the cross block restricted to \(H_F\times U\) is \(\Delta_K(P\wedge H)\), with second-projection image \((P\wedge H)_U\).
3. Add a sentence explaining why a sublocale fitted in the *open* sheet \(U\) is also fitted in the ambient \(Z\).
4. Highlight that the coframe law used in (B7) is finite-join/infinitary-meet distributivity, whereas (C3) demonstrates failure of the dual infinitary law.
5. Include the short Booleanization proof of \(P\neq0\) so the Cantor test is genuinely self-contained.
6. Explicitly define \(\Delta_K(P)\) as the image of \(P\hookrightarrow K\xrightarrow{\Delta_K}K\times K\), not the diagonal of the set of points of \(P\).

**Final recommendation:** Accept and consolidate (B2), (B4), (B7), (B8), and (C3). The mathematical argument is genuinely point-free and has the claimed generality.
