# Project A — Effectivity of the remote equivalence: pinching a fitted sublocale

**11 November 2026. New INTERNAL theorem and proof; not independently externally audited.** This solves the previously open effectivity question for \(R_\infty=\Delta_V\vee(Z\times Z)\). The proof in fact works for the relation \(\Delta_X\vee(Z\times Z)\) for **every nonzero fitted sublocale \(Z\hookrightarrow X\)** of any locale \(X\), without spatiality, coherence, density, compactness, or local compactness. The zero case is separately immediate. No literature-priority verdict; compare Vermeulen's classical theorems for *closed proper* equivalence relations, which do not supply this proof.

## 0. Statement

Let \(L=\mathcal O(X)\), let \(z:Z\hookrightarrow X\) be a nonzero fitted sublocale with a specified presentation
\[
Z=\bigwedge_{i\in I}\mathfrak o(U_i),\qquad U_i\in L.
\tag{0.1}
\]
Write \(z^*:L\to \mathcal O(Z)\) for restriction, and define
\[
F_Z=\{a\in L:z^*(a)\in\{0_Z,1_Z\}\},\qquad
Q_Z=\operatorname{Loc}(F_Z).
\tag{0.2}
\]
Because \(Z\ne0\), \(\{0_Z,1_Z\}\) is the canonical two-element subframe of \(\mathcal O(Z)\). Its inverse image \(F_Z\) under the frame map \(z^*\) is a subframe of \(L\). Thus inclusion \(F_Z\hookrightarrow L\) determines a locale-surjection
\[
q_Z:X\twoheadrightarrow Q_Z.
\tag{0.3}
\]
Let
\[
R_Z=\Delta_X\vee(Z\times Z)\le X^2.
\tag{0.4}
\]

**Theorem (fitted pinching is effective, working).**
\[
\boxed{X\times_{Q_Z} X=R_Z.}
\tag{0.5}
\]
Moreover \(q_Z\) coequalizes the two projections of \(R_Z\) and is their **coequalizer**. Thus \(R_Z\) is an effective internal equivalence relation.

In particular, the earlier abstract **closed-family** relation \(R_{\mathcal K}=\Delta_X\vee(Z_{\mathcal K}\times Z_{\mathcal K})\), with \(Z_{\mathcal K}=\bigwedge_i\mathfrak o(X\setminus K_i)\) for any set-indexed family of closed sublocales \(K_i\subseteq X\), is effective. If \(Z_{\mathcal K}=0\), the relation is just \(\Delta_X\), the kernel pair of \(1_X\).

## 1. First inclusion and the universal candidate quotient

For any \(a\in F_Z\), the restrictions of \(a\) to both endpoint coordinates on \(Z\times Z\) are equal: each is the same scalar \(0_Z\) or \(1_Z\). Hence \(q_Z\circ z:Z\to Q_Z\) is a constant localic map. More precisely, the unique \(\eta:1\to Q_Z\) determined by \(\eta^*(a)=z^*(a)\in 2\) gives \(q_Z z=\eta\,!\). Uniqueness uses the injective frame map \(2\hookrightarrow\mathcal O(Z)\), valid because \(Z\ne0\).

The endpoints agree after \(q_Z\) on \(\Delta_X\) and on \(Z^2\). Thus
\[
R_Z\le X\times_{Q_Z}X.
\tag{1.1}
\]

## 2. Reverse inclusion, using arbitrary complete Boolean probes

Let \(H=X\times_{Q_Z}X\). By the general Boolean-probe conservativity lemma (proved and externally checked in the CO-01 closed-family investigation), to prove \(H\le R_Z\) it suffices to show every \(t:T=\operatorname{Loc}(B)\to H\), with \(B\) any nonzero complete Boolean frame, factors through \(R_Z\).

Such a map is a pair \(f,g:T\to X\) satisfying \(q_Zf=q_Zg\). Write \(h=f^*\), \(k=g^*:L\to B\). Every \(U_i\) has restriction \(z^*(U_i)=1_Z\), so \(U_i\in F_Z\), and therefore
\[
h(U_i)=k(U_i)=b_i\in B.
\tag{2.1}
\]
For each \(a\in L\), also \(U_i\vee a\in F_Z\), because \(z^*(U_i\vee a)=1_Z\). Thus
\[
b_i\vee h(a)=h(U_i\vee a)=k(U_i\vee a)=b_i\vee k(a).
\]
Meeting with \(\neg b_i\) in the Boolean frame B yields
\[
\neg b_i\wedge h(a)=\neg b_i\wedge k(a)\qquad(a\in L).
\tag{2.2}
\]
Set \(c=\bigvee_i\neg b_i\). Frame distributivity gives
\[
c\wedge h(a)=c\wedge k(a)\qquad(a\in L).
\tag{2.3}
\]
Consequently the two restricted maps from the clopen component \(T_c\) coincide; \((f,g)|_{T_c}\) factors through \(\Delta_X\).

On the complementary Boolean component \(T_{\neg c}\), we have \(\neg c\le b_i\) for every \(i\), so the restrictions of \(h(U_i)\) and \(k(U_i)\) are both top. Therefore both endpoint maps factor through each \(\mathfrak o(U_i)\) and hence their intersection \(Z\). Thus \((f,g)|_{T_{\neg c}\!}\) factors through \(Z\times Z\).

Since \(T\simeq T_c\sqcup T_{\neg c}\), the full pair \((f,g)\) factors through \(R_Z=\Delta_X\vee(Z\times Z)\). Boolean-probe conservativity gives
\[
H\le R_Z.
\tag{2.4}
\]
Combining (1.1), (2.4) proves (0.5), without any general base-change-stability or associativity claim.

## 3. Coequalizer property

**Lemma (constants detected on a nonzero locale).** Let \(Z\ne0\). If \(b\in \mathcal O(Z)\) and
\[
p_1^*(b)=p_2^*(b)\quad\text{in }\mathcal O(Z\times Z),
\]
then \(b=0_Z\) or \(b=1_Z\).

*Proof.* If \(b\ne0\), pull the equality back along the open sublocale \(\mathfrak o(b)\times Z\hookrightarrow Z\times Z\). The first coordinate becomes top. Therefore the pullback of \(b\) from the second coordinate is top. The projection \(\mathfrak o(b)\times Z\to Z\) is a **locale-surjection**: the terminal map \(\mathfrak o(b)\to1\) is an open surjection in classical locale theory (nonzero locale), and open surjections are pullback-stable. Injectivity of the projection's frame inverse-image forces \(b=1_Z\). QED.

Suppose \(u:X\to W\) coequalizes the two projections of \(R_Z\). For every \(v\in\mathcal O(W)\), put \(a=u^*(v)\). On \(Z\times Z\subseteq R_Z\), the endpoint restrictions agree, and the lemma implies \(z^*(a)\in\{0_Z,1_Z\}\). Thus \(u^*\) has image in \(F_Z\); as \(F_Z\hookrightarrow L\) is a subframe inclusion, \(u\) factors uniquely through \(q_Z\).

Conversely \(q_Z\) coequalizes \(R_Z\), so it is the required coequalizer. (Being a kernel pair alone would not, without this check, identify the universal quotient.)

## 4. The pushout interpretation: collapse Z to one point

Because \(Z\ne0\), the frame map \(2=\mathcal O(1)\to \mathcal O(Z)\) is injective. The frame pullback
\[
\mathcal O(X)\times_{\mathcal O(Z)}2
\]
identifies canonically with \(F_Z\). Taking opposites gives the **pushout square** in locales
\[
\begin{array}{ccc}
Z&\xrightarrow{z}&X\\
\big\downarrow&&\big\downarrow q_Z\\
1&\xrightarrow{\eta}&Q_Z.
\end{array}
\tag{4.1}
\]
Therefore \(Q_Z\) is literally the localic **pinching/collapse of \(Z\) to a point**, and the theorem says this particular pinching has no extra kernel-pair identifications when \(Z\) is fitted.

**Zero caution:** if \(Z=0\), the pushout \(X\sqcup_0 1\cong X\sqcup1\) is NOT the coequalizer of the diagonal. For \(Z=0\), use \(q=1_X\), \(R_Z=\Delta_X\). The pushout description and the identification \(F_Z=\mathcal O(X)\times_{\mathcal O(Z)}2\) thus require \(Z\ne0\).

## 5. Dense fitted Z: a hyperconnected generic-point quotient

Suppose in addition that \(Z\) is dense in X. Then \(z^*(a)=0_Z\) only for \(a=0_X\). Hence
\[
\boxed{F_Z=\{0_X\}\cup\mathcal N(Z),\qquad
\mathcal N(Z)=\{a\in\mathcal O(X):Z\le \mathfrak o(a)\}.}
\tag{5.1}
\]
This is **not** necessarily the frame of *all* dense opens of X: it is the smaller subframe of opens containing the **specific** dense fitted sublocale \(Z\), together with zero. The \(\mathcal N(Z)\) elements are a filter under finite meets and are closed under nonempty arbitrary joins.

Every pair of nonzero elements of \(F_Z\) meets in an element containing \(Z\ne0\). Thus \(Q_Z\) is **hyperconnected** (every nonempty open is dense). There is a canonical **generic point** \(\eta:1\to Q_Z\) whose inverse image sends every nonzero open to 1, and \(q_Z|_Z=\eta\,!\).

When \(X\) is spatial, \(Q_Z\) is also spatial: distinct elements of the subframe \(F_Z\hookrightarrow\mathcal O(X)\) are distinguished by some ordinary point of X. An explicit (possibly nonsober) space presenting \(Q_Z\) is
\[
\widehat X=X\sqcup\{\infty\}
\]
whose opens are \(\varnothing\) and \(\{\infty\}\cup a\) for \(a\in\mathcal N(Z)\); a subspace map \(q:X\to\widehat X\) with the original topology on X is continuous, but it **need not be a topological embedding** (the induced topology on the underlying X-points is generally much coarser). Sobrification of \(\widehat X\) gives the point space of \(Q_Z\). The locale-surjection q need **not** be surjective on ordinary points.

## 6. Specialization to the compact-remote sublocale of Arrieta's V

Let \(V=C\setminus D\) be the original Cantor-space complement, or the dense complement in the corroborated locally compact compact-cloud generalization. Let
\[
Z=\bigwedge_{K\subseteq V,\ K\text{ compact}}\mathfrak o(V\setminus K).
\]
All compact K have empty interior in V, so Z is nonzero and dense (contains the double-negation sublocale); Z has **no ordinary points**, since every singleton \(\{x\}\) is compact and disjoint from Z.

The quotient \(q:V\twoheadrightarrow Q_Z\) has
\[
\boxed{\mathcal O(Q_Z)=\{0\}\cup\{a\in\mathcal O(V):Z\le\mathfrak o(a)\}.}
\tag{6.1}
\]
Every cocompact open \(V\setminus K\) is in this frame; other open Z-neighborhoods can occur and **must not** be silently replaced by just the cocompact ones.

The map q is **injective on ordinary points of V**: if \(x\ne y\), the open \(V\setminus\{x\}\in F_Z\) contains y but not x. None of these ordinary points maps to the generic point \(\eta\), since \(q(x)\) omits \(V\setminus\{x\}\) while \(\eta\) lies in every nonzero Q-open. Yet q is a genuine **locale-surjection** by the injective frame inclusion (6.1). This is another clean example of surjectivity in Loc not implying surjectivity on ordinary points.

The new theorem gives
\[
\boxed{\kerpair(q)=\Delta_V\vee(Z\times Z)=R_\infty=A^2.}
\tag{6.2}
\]
The last equality is CO-01's externally checked (or subsequent nonblind-corrobated LCH) square-saturation theorem. Thus **the square of the nontransitive fitted diagonal is a genuine kernel pair**, hence an effective equivalence relation.

## 7. Adversarial caveats and research directions

1. **Classical setting:** the projection lemma and the Boolean-probe separation are used in ordinary classical locale theory. Do not infer a constructive internal theorem without checking positivity/overt hypotheses.
2. **No general Loc exactness claim:** the proof works because Z is fitted, and depends on the particular presentation (0.1). It does not imply arbitrary localic equivalence relations are effective.
3. **No claim that q is proper or open:** neither property was needed; the general closed-proper Vermeulen theorem is not being invoked.
4. **No claim that q is an ordinary quotient map of point spaces:** it is a coequalizer in Loc, with a spatial hyperconnected quotient potentially containing new points absent from the pointwise image of V.
5. **Literature priority not investigated fully:** fitted pinching may be known under a different name. The new theorem here is a *project-level deduction*, not a novelty claim.
6. **Next conceptual target:** analyze \(\mathcal N(Z)\) intrinsically for \(V\cong\mathbb N^{\mathbb N}\), compare \(Q_Z\) with standard generic-point / filter topologies, and determine how much of its sober point spectrum is exhausted by \(V\) plus \(\eta\).

**Status:** new internally proved positive solution of effectivity. Recommended focused adversarial audit (internal first) before adding to the externally certified ledger; retain the original closed-family theorem and compact-cloud notes unchanged and link to this result as a subsequent theorem.
