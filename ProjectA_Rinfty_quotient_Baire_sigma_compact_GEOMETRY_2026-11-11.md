# Project A — Geometry of the fitted-pinching quotient: exact co-σ-compact topology

**11 November 2026. New internal theorem, NOT externally audited.** Bounded follow-up to [fitted pinching/effectivity](ProjectA_Rinfty_effectivity_fitted_pinching_THEOREM_2026-11-11.md). It determines the **entire** frame of opens and the **entire sober point space** of the quotient associated with the compact-remote sublocale of Baire space. The main compact-remote criterion is proved with an elementary transfinite locally-compact derivative in the Polish category. It agrees with the classical Hurewicz non-σ-compact/closed-Baire-subspace dichotomy but does not need to assume that theorem.

## 0. Setup and main result

Let \(V\) be a nonempty nowhere locally compact Polish space (our Cantor finite-support complement is homeomorphic to \(\omega^\omega\)). Define
\[
Z_V=\bigwedge_{K\subseteq V\ \mathrm{compact}}\mathfrak o(V\setminus K)\hookrightarrow V
\]
and
\[
q:V\twoheadrightarrow Q_Z,\qquad
\mathcal O(Q_Z)=\{0\}\cup\mathcal N(Z_V),\quad
\mathcal N(Z_V)=\{a\in\mathcal O(V):Z_V\le\mathfrak o(a)\}.
\]
The simplification uses density of \(Z_V\): every compact subset of \(V\) has empty interior, hence every \(V\setminus K\) is dense open and the Booleanization \(V_{\neg\neg}\le Z_V\ne0\).

**Theorem (exact quotient geometry, working).** For every closed \(F\subseteq V\),
\[
\boxed{Z_V\wedge F=0\ \Longleftrightarrow\ F\text{ is }\sigma\text{-compact}.}\tag{0.1}
\]
Consequently,
\[
\boxed{\mathcal O(Q_Z)=\{\varnothing\}\cup\{V\setminus F:F\subseteq V\text{ closed }\sigma\text{-compact}\}.}\tag{0.2}
\]
As a **sober topological space**, \(Q_Z\) is exactly
\[
\boxed{\widehat V=V\sqcup\{\infty\},\quad
\tau_{\widehat V}=\{\varnothing\}\cup\{\{\infty\}\cup(V\setminus F):
F\subseteq V\text{ closed }\sigma\text{-compact}\}.}\tag{0.3}
\]
There are **no additional sobrification points** beyond the unique new generic point \(\infty\).

These statements concern the ordinary *Polish* case (particularly Baire space) and do not claim an analogous σ-compact characterization for arbitrary locales or non-Polish topological spaces.

## 1. Reduction to closed Polish subspaces

For any closed \(F\subseteq V\), with embedding \(i:F\hookrightarrow V\), pullback of sublocales preserves arbitrary meets:
\[
i^{-1}(Z_V)
=\bigwedge_{K\subseteq V\ \mathrm{compact}}\mathfrak o_F(F\setminus(F\cap K))
=\bigwedge_{C\subseteq F\ \mathrm{compact}}\mathfrak o_F(F\setminus C)
=:Z_F.\tag{1.1}
\]
Indeed \(F\cap K\) is compact in F and every compact C of F is compact in V. As a sublocale, \(Z_V\wedge F\) identifies with \(Z_F\). Since \(F\) and \(\mathfrak o(V\setminus F)\) are complementary closed/open sublocales,
\[
\boxed{Z_V\le\mathfrak o(V\setminus F)\iff Z_F=0.}\tag{1.2}
\]
Thus the problem is to decide when the **compact-remote sublocale of an arbitrary Polish space F is zero**.

## 2. The locally compact derivative of a Polish space

For a closed subspace \(H\) of a Polish space, define
\[
\operatorname{LC}(H)=\bigcup\{U\subseteq H: U\text{ open in H and }\overline U^{\,H}\text{ compact}\}.
\]
This is the open set of locally compact points of H. Being locally compact and second countable, \(\operatorname{LC}(H)\) is **σ-compact**, as a subset of H and of the original Polish space.

Starting with \(F_0=F\), define by transfinite recursion
\[
F_{\alpha+1}=F_\alpha\setminus\operatorname{LC}(F_\alpha),\qquad
F_\lambda=\bigcap_{\beta<\lambda}F_\beta.
\tag{2.1}
\]
All \(F_\alpha\) are closed in F.

**Countable stabilization.** This process stabilizes at some countable ordinal \(\rho\): if \(F_\alpha\supsetneq F_{\alpha+1}\) for uncountably many stages, choose for each such stage a basic open set \(B_\alpha\) of F meeting \(F_\alpha\) but missing \(F_{\alpha+1}\). A single basis element cannot witness two distinct stages (for an earlier stage its successor still contains the later \(F_\alpha\)). That injects uncountably many stages into a countable basis, contradiction. Hence \(F_\rho=F_{\rho+1}\). Let
\[
H_F=F_\rho.
\tag{2.2}
\]
Then \(H_F\) is a **closed nowhere locally compact** subspace (or empty). Moreover
\[
F\setminus H_F=\bigcup_{\alpha<\rho}\operatorname{LC}(F_\alpha)
\tag{2.3}
\]
is σ-compact because \(\rho\) is countable and each removed piece is σ-compact.

If \(F\) itself is σ-compact, every closed \(H\subseteq F\) is σ-compact and Polish. By Baire category a nonempty such H is not nowhere locally compact: writing H as a countable union of compact subsets, at least one compact piece has nonempty relative interior, so H has a nonempty relatively compact open. Hence \(H_F=\varnothing\). Conversely if \(H_F=\varnothing\), (2.3) shows F is σ-compact. Thus
\[
\boxed{H_F=\varnothing\iff F\text{ is }\sigma\text{-compact}.}\tag{2.4}
\]

In fact \(H_F\) is the **largest closed nowhere locally compact subset** of F: if P is any such closed subset, it avoids the locally compact locus of F and, by induction, that of every \(F_\alpha\), hence \(P\subseteq H_F\).

## 3. The compact-remote sublocale lives exactly on this kernel

Write
\[
S=Z_F=\bigwedge_{K\subseteq F\ \mathrm{compact}}\mathfrak o_F(F\setminus K).
\]

**Upper support:** \(S\le H_F\) as sublocales of F. Inductively assume \(S\le F_\alpha\). For each relatively compact \(U\subseteq F_\alpha\), its closure K is compact in F, so \(S\cap\mathfrak o_{F_\alpha}(U)=0\). Since all such opens cover \(\operatorname{LC}(F_\alpha)\), the *open-cover gluing law* gives \(S\cap\mathfrak o_{F_\alpha}(\operatorname{LC}(F_\alpha))=0\), hence \(S\le F_{\alpha+1}\). At limits, \(S\le\bigwedge_{\alpha<\lambda}F_\alpha=F_\lambda\).

**Nonzero if the kernel is nonempty:** If \(H_F\ne\varnothing\), its nonzero Booleanization \(H_{F,\neg\neg}\) is dense in \(H_F\). For each compact K of F, \(K\cap H_F\) has **empty interior in** \(H_F\); otherwise \(H_F\) would have a relatively compact nonempty open, contradicting the definition of \(H_F\). Thus \(H_F\setminus K\) is dense open in \(H_F\), and contains \(H_{F,\neg\neg}\). The composite
\[
H_{F,\neg\neg}\hookrightarrow H_F\hookrightarrow F
\]
therefore factors through every \(\mathfrak o_F(F\setminus K)\), so through \(Z_F\). Hence \(Z_F\ne0\).

Together these give
\[
\boxed{Z_F=0\iff H_F=\varnothing\iff F\text{ is }\sigma\text{-compact}.}\tag{3.1}
\]
In fact the pullback of \(Z_F\) to \(H_F\) is \(Z_{H_F}\), and as \(Z_F\le H_F\) and the Booleanization of \(H_F\) lies in \(Z_F\), its **closed hull** satisfies
\[
\boxed{\operatorname{cl}_F(Z_F)=H_F.}\tag{3.2}
\]
Thus the closure of the pointfree compact-remote remainder recovers the *largest closed nowhere locally compact kernel* of an arbitrary Polish space.

**Alternative classical route:** One may use the Hurewicz theorem: a non-σ-compact Polish space contains a closed copy of \(\omega^\omega\), whose Booleanization is a nonzero sublocale avoiding every compact. The transfinite proof above is included to make the implication self-contained and to identify the canonical kernel.

## 4. All quotient opens

Combining (1.2) and (3.1), an ordinary V-open a is in \(\mathcal N(Z_V)\) exactly when its closed complement \(F=V\setminus a\) is σ-compact. Since \(Z_V\) is dense, no other nonzero opens lie in the quotient frame. This proves (0.2).

The family is visibly a topology/frame: it is closed under finite intersections because finite unions of closed σ-compact subsets are closed σ-compact; it is closed under arbitrary unions because the intersection of a nonempty family of closed σ-compact sets is a closed subset of any one member, hence σ-compact. The zero open is adjoined separately because \(V\) itself is non-σ-compact.

For a concrete Baire-space description, let \(V=\omega^\omega\). For \(b\in\omega^\omega\), the order interval
\[
[0,b]=\{x\in\omega^\omega:\forall n,\ x(n)\le b(n)\}
\]
is compact, and every compact subset of \(\omega^\omega\) lies in some \([0,b]\). Hence a closed F is σ-compact exactly when
\[
F\subseteq\bigcup_{m\in\omega}[0,b_m]
\quad\text{for some countable family }(b_m)_{m\in\omega}\subseteq\omega^\omega.
\tag{4.1}
\]
Equivalently the excluded closed set is **σ-bounded in pointwise order**, and the quotient's nonempty opens contain all sequences outside such a countable bounded family. This is an explicit combinatorial neighborhood test.

Examples of nonempty Q-opens:
- \(V\setminus\{x\}\), since a singleton is compact.
- \(V\setminus F\) for any compact Cantor copy F.
- \(V\setminus F\) for the closed noncompact discrete set \(F=\{(n,0,0,\ldots):n\in\omega\}\).
- Not, in general, a usual basic Baire cylinder \([s]\), since its complement contains a clopen copy of \(\omega^\omega\) and hence is not σ-compact.

## 5. The sober point space has exactly one new point

Define \(\widehat V=V\sqcup\{\infty\}\) with topology (0.3). It is \(T_0\): for distinct x,y∈V, the open complement of \(\{x\}\) separates them, and the corresponding \(\widehat V\)-open contains \(\infty\) but not x. The entire space is **irreducible**, since all its nonempty opens contain \(\infty\), and \(\overline{\{\infty\}}=\widehat V\).

Every **proper closed subset** of \(\widehat V\) is a closed σ-compact F⊂V. Its subspace topology from \(\widehat V\) is **exactly the original Polish topology on F**: for every ordinary relative closed C⊂F, C is closed in V and σ-compact (a closed subset of σ-compact F), so
\[
F\setminus C=F\cap\bigl(\{\infty\}\cup(V\setminus C)\bigr)
\]
is open in the induced topology. Conversely all induced opens are originally open.

Therefore each nonempty irreducible **proper** closed subset of \(\widehat V\) is a singleton (it is Hausdorff). The only additional irreducible closed subset is \(\widehat V\) itself, with unique generic point \(\infty\). Every nonempty irreducible closed subset has a **unique** generic point, proving \(\widehat V\) is **sober**.

The frame \(\mathcal O(\widehat V)\) is (0.2) by construction (send \(\{\infty\}\cup a\mapsto a\)). Consequently \(Q_Z\cong\operatorname{Loc}(\widehat V)\), not merely the locale of the sobrification of a potentially nonsober presentation. Its **entire point set** is \(V\sqcup\{\infty\}\).

The map of ordinary point spaces induced by \(q:V_{\rm original}\to Q_Z\) is the **set inclusion**
\[
x\longmapsto x\in\widehat V,
\]
continuous but not a topological embedding: the topology induced on V from \(\widehat V\) is the co-closed-σ-compact topology, far coarser than the original Polish topology. The image is dense, and q is a locale-surjection (inclusion of frames), but \(\infty\) is **not** in the pointwise image.

## 6. Compactness, separation and a useful universal characterization

- \(Q_Z\) is \(T_0\), **hyperconnected**, and has a generic point \(\infty\). It is **not \(T_1\)** (the generic point is not closed), hence neither Hausdorff nor regular.
- \(Q_Z\) is **Lindelöf**: given an open cover, choose one member \(U\) (all nonempty members contain \(\infty\)); its complement is a closed σ-compact F. The other members restrict to an ordinary open cover of F, so a countable subfamily covers F.
- \(Q_Z\) is **not compact**. Let \(F=\{x_n:n\in\omega\}\) be any infinite closed discrete subset of V. Its tails \(F_n=\{x_k:k\ge n\}\) are closed σ-compact nonempty with \(\bigcap_nF_n=\varnothing\). The increasing opens \(\{\infty\}\cup(V\setminus F_n)\) cover \(\widehat V\) but no finite subfamily does.
- Every proper closed subspace of \(\widehat V\) is a **σ-compact Polish space with its original topology**.
- The topology is characterized among one-point extensions of V by the condition that the nonempty opens are precisely the complements of original closed σ-compact subsets, together with the generic point. The new point is a literal generic point; it is not a compactification point.

## 7. Two further geometric consequences

**Not first countable at any point.** Suppose \(p\in\widehat V\) has a countable neighborhood base \(U_n=\{\infty\}\cup(V\setminus F_n)\) (after discarding any empty members), where every \(F_n\) is closed σ-compact. Then \(F=\bigcup_n F_n\) is σ-compact, so as \(V\cong\omega^\omega\) is not σ-compact, choose \(y\in V\setminus(F\cup\{p\})\) (interpret \(\{p\}\) as empty when \(p=\infty\)). Every \(U_n\) contains y, whereas the valid neighborhood \(\{\infty\}\cup(V\setminus\{y\})\) of p excludes y. No \(U_n\) lies in that neighborhood. Thus the quotient is Lindelöf and sober, but **nowhere first countable**.

**The remote sublocale is strictly larger than the Booleanization.** In Baire space, let
\[
F=\{x\in\omega^\omega:x(2n)=0\ \text{for every }n\}.
\]
This is a closed nowhere dense copy of \(\omega^\omega\), hence not σ-compact. Its open complement \(a=V\setminus F\) is dense, so \(V_{\neg\neg}\le\mathfrak o(a)\). But \(Z_V\not\le\mathfrak o(a)\) by (0.1). Since \(V_{\neg\neg}\le Z_V\), the inclusion is **strict**:
\[
\boxed{V_{\neg\neg}<Z_V.}
\]
This distinguishes the compact-remote generic sublocale from the minimal dense Booleanization, even though both are pointless.

## 8. Source and audit status

The result is new **internal** mathematical work. The classical Baire-category ingredient is standard. Hurewicz's theorem that non-σ-compact Polish spaces contain a closed copy of \(\omega^\omega\) independently corroborates the key σ-compactness dichotomy, but the canonical-derivative proof here is self-contained.

Read together with:
- [Effective fitted pinching and original quotient frame](ProjectA_Rinfty_effectivity_fitted_pinching_THEOREM_2026-11-11.md)
- [Externally corroborated locally compact compact-cloud generalization](ProjectA_CO01_Stone_and_LCH_saturation_GENERALIZATION_2026-11-11.md)
- [CO-01 original referee reconciliation](ProjectA_CO01_EXTERNAL_referee_reconciliation_2026-11-11.md)

**Status: I (internally proved), not audited.** No literature priority claim is made. This **closes the bounded geometry question** for the original Baire-space example: the open-neighborhood filter, all sober points, and important separation/covering properties are explicit. Further categorical properties (e.g. exact nature of the quotient map) may be studied separately, but are not needed for this segment.
