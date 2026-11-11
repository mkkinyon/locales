# CO-01 positive solution (working): Arrieta's fitted-diagonal square is the maximal compact-remote equivalence

**11 November 2026. NEW THEOREM WITH FULL INTERNAL ADVERSARIAL PROOF; NOT EXTERNALLY AUDITED.** This proves the desired cube associativity for the **particular spatial strongly Hausdorff, noncoherent** Arrieta example Y. The V×V block A is nontransitive, but \(A²\) is transitive and absorbs A on both sides. The proof uses a **genuinely locale-theoretic surjective generic-middle witness**, not ordinary points, finite cover approximations, or the earlier Cantor-map Baire family. It also corrects a separate **historical error** in older purported general nonassociativity examples (denseness of a subset is not locale-surjectivity); see the independent correction note.

Sources/dependencies:
- [Audit VIII: exact Θ-admissible-cover presentation and explicit nontransitivity](A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md)
- [Compact-local diagonal restrictions of all finite parenthesized powers](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md)
- [Abstract closed-family maximal equivalence theorem and Boolean probe conservativity](ProjectA_closed_family_remote_equivalence_general_theorem_2026-11-11.md)

## 0. Statement

Let \(C=2^{\mathbb N}\), \(K_n=\{d\in C:\operatorname{supp}(d)\ne\varnothing\text{ finite, }\max\operatorname{supp}(d)=n\}\), \(D=\bigcup_n K_n\), and \(V=C\setminus D\), with the inherited topological/regular localic structure. Let \(A=\mathcal D_Y|_{V\times V}\) denote Arrieta's exotic symmetric reflexive fitted relation. For \(a\in\mathcal O(V)\), \(\Theta(a)\ni n\) means there is a Cantor-open \(W\supseteq K_n\) with \(W\cap V\subseteq a\); a Θ-admissible cover \(\mathcal C\) of V has \(\bigcup_{a\in\mathcal C}\Theta(a)=\mathbb N\). The defining fitted relation is
\[
A=\bigwedge_{\mathcal C\;\Theta\text{-admissible}}
\mathfrak o(\gamma_\mathcal C),\qquad
\gamma_\mathcal C=\bigvee_{a\in\mathcal C}a_1\wedge a_2
\in\mathcal O(V²).
\tag{0.1}
\]

Define the **compact-remote sublocale**
\[
Z=\bigwedge_{K\subseteq V\text{ compact}}\mathfrak o(V\setminus K)
\]
and maximal compact-locally diagonal equivalence
\[
\mathscr R_\infty=\Delta_V\vee(Z\times Z).
\tag{0.2}
\]

**Theorem (CO-01, new).**
\[
\boxed{\ A\subsetneq A²=\mathscr R_\infty,\qquad
(A²)A=A(A²)=A²,\qquad
A²\circ A²=A².\ }
\tag{0.3}
\]
Every binary parenthesization of any word \(A^n\), \(n\ge2\), equals \(\mathscr R_\infty\); the nontrivial block of \(\mathcal D_Y\) therefore has an **associative cubic power**, although \(\mathcal D_Y\) itself is not transitive. By the established block diagonal decomposition \(\mathcal D_Y=\operatorname{diag}(A,\Delta_{\mathbb N})\), the same equalities of bracketed cubes hold for \(\mathcal D_Y\).

The strict A<A² is from the prior explicit Booleanized three-permutation nontransitivity witness, not from the new generic-middle proof.

## 1. Universal remote generalized points in Boolean frames

Let B be a **nontrivial complete Boolean algebra** and \(T=\operatorname{Loc}(B)\). Write \(S=\operatorname{Ult}(B)\), the ordinary Stone space of the underlying Boolean algebra. It is extremally disconnected (because B complete), but its ordinary points are **not** points of T unless their ultrafilters are completely prime.

Let \(f:T\to V\) be an arbitrary locale map **factoring through Z**, with frame morphism \(h=f^*:\mathcal O(V)\to B\). For every Cantor clopen W⊆C, \(W\cap V\) is complemented in O(V), so \(h(W\cap V)\) is a Boolean element of B. Stone duality yields a continuous map
\[
\widehat f:S\to C
\tag{1.1}
\]
characterized by
\[
\widehat f^{-1}(W)=\widehat{h(W\cap V)}\subseteq S
\qquad(W\text{ Cantor clopen}),
\tag{1.2}
\]
where a hat on a Boolean element denotes its corresponding clopen subset of S. No assumption that \(\widehat f(S)\subseteq V\) is made (and in fact it is generally false).

**Lemma 1 (cofinal finite-support heights).** For every nonempty clopen \(E\subseteq S\) and integer N, there exist \(n>N\) and \(s\in E\) with \(\widehat f(s)\in K_n\). Equivalently, the inverse image of \(\bigcup_{n>N}K_n\) is dense in S for every N.

*Proof.* First show \(P=\widehat f^{-1}(D)\) is dense in S. If a nonempty clopen E misses P, the compact set K=\(\widehat f(E)\) is contained in V. By remoteness \(h(V\setminus K)=1\). But the Cantor clopens W contained in C\K have traces W∩V covering V\K, and by (1.2) all their h-values have zero intersection with E. Since h preserves arbitrary joins, \(E\cap\widehat{h(V\setminus K)}=\varnothing\), contradiction.

Second, for every d∈D, the closed fibre \(\widehat f^{-1}(\{d\})\) has empty interior. Indeed C\{d} is open and its V-trace is the whole V; writing C\{d} as a union of Cantor clopens W, the traces W∩V cover V. Since h(V)=1, their h-values join to 1_B. If the fibre of d contained a nonempty clopen E, all these h-values would meet E trivially by (1.2), a contradiction. Thus the preimage of the **finite** set \(\bigcup_{n\le N}K_n\) is closed nowhere dense.

Given nonempty clopen E, choose a nonempty clopen \(E'\subseteq E\) avoiding that finite set of fibres. Density of P supplies \(s\in E'\cap P\), and then \(\widehat f(s)\in K_n\) for some n>N. QED.

**Caution:** This is a statement about a Stone-space *presentation* of an arbitrary Boolean-valued localic point. No preservation of the partition D/V by \(\widehat f\) is assumed or needed. This is stronger than the previous fixed-\(\operatorname{RO}(V)\) continuous-map fusion result.

## 2. Pullback of A along a remote Boolean point is dense

**Lemma 2 (one-sided generic density).** For \(f:T\to Z\subseteq V\) as above, the sublocale
\[
A_f=(f,\operatorname{id}_V)^{-1}(A)\subseteq T\times V
\tag{2.1}
\]
is **dense** in the product locale \(T\times V\). Likewise the inverse-image relation \(A^g=(\operatorname{id}_V,g)^{-1}(A)\) is dense for any \(g:T\to Z\).

*Proof.* Pullback of sublocales is right adjoint to the direct-image-on-sublocales operation (image of composition), so it preserves arbitrary meets. It also carries open sublocales to open sublocales. Therefore by (0.1),
\[
A_f=\bigwedge_{\mathcal C\ \Theta\text{-admissible}}
\mathfrak o(w_\mathcal C),\quad
w_\mathcal C=\bigvee_{a\in\mathcal C}h(a)\boxtimes a
\in\mathcal O(T\times V).
\tag{2.2}
\]
We show every w_C is a **dense open** element: \(w_C^*=0\). Since rectangles \(b\boxtimes v\), for b∈B, v∈O(V), join-generate O(T×V), it suffices to check each nonzero basic rectangle meets w_C nontrivially.

Fix b>0 and nonzero V-open v. Choose a Cantor cylinder U of finite depth m with \(\varnothing\ne U\cap V\subseteq v\). By Lemma 1 choose n>m and s in the clopen \(\hat b\subseteq S\) with \(\hat f(s)\in K_n\).

Θ-admissibility gives \(a\in\mathcal C\) and Cantor-open W⊇K_n with W∩V⊆a. Choose Cantor clopen W' with \(\hat f(s)\in W'\subseteq W\). The Boolean element \(b\wedge h(W'\cap V)\) is nonzero by (1.2), hence \(b\wedge h(a)>0\). Meanwhile K_n meets U because n>m and **all m-bit prefixes occur in K_n**; then W∩U is a nonempty Cantor-open and its V-trace lies in a∧v, so \(a\wedge v>0\). It follows that
\[
(b\boxtimes v)\wedge w_\mathcal C
\ge (b\wedge h(a))\boxtimes(v\wedge a)\ne0.
\]
The last rectangle is nonzero because its V-factor has an ordinary point, yielding a section of the projection to the nonzero Boolean factor. Thus \(w_\mathcal C\) is dense.

The Booleanization \((T\times V)_{\neg\neg}\) is contained in every dense open sublocale; therefore it is contained in their arbitrary meet A_f. In particular, A_f is dense. Symmetry of A gives the statement for A^g. QED.

**Key distinction:** density of a sublocale does **not** mean its inclusion is locale-surjective. We only use containment of Booleanization, not the invalid “dense map ⇒ surjection” inference in older general composition examples.

## 3. A canonical surjective family of two-step witnesses

**Lemma 3 (Booleanization of product projects surjectively onto Boolean factor).** Let T=Loc(B) for a nontrivial complete Boolean frame B, and let V be any locale with an ordinary point \(v_0:1\to V\). Put \(W=T\times V\), and let \(N=W_{\neg\neg}\) be its Booleanization sublocale. Then the composite
\[
N\hookrightarrow W\xrightarrow{p_T}T
\tag{3.1}
\]
is a **locale-surjection**.

*Proof.* The product projection has a section \(T\to W,\ t\mapsto(t,v_0)\), so \(p_T^*:B\to O(W)\) is injective. All elements of B are complemented; \(p_T^*\) preserves their complements, so all \(p_T^*(b)\) are complemented in O(W). Double negation fixes complemented elements, hence the composite
\[
B\xrightarrow{p_T^*}O(W)\xrightarrow{(-)^{**}}O(N)
\]
remains injective. This is precisely the inverse-image frame map of (3.1), establishing surjectivity. QED.

Now take **arbitrary** \(f,g:T\to Z\) over the same Boolean locale T. The locale of composable paths with those endpoints is the pullback of
\[
E_2=A_{12}\cap A_{23}\subseteq V^3
\]
along \(t=(f,g):T\to V²\). It identifies with
\[
E_{f,g}=A_f\cap A^g\subseteq T\times V.
\tag{3.2}
\]
By Lemma 2 both A_f and A^g contain the **same** Booleanization N of T×V, so N⊆E_{f,g}. Lemma 3 shows \(N\to T\) is a locale-surjection. Therefore \(E_{f,g}\to T\) is a locale-surjection.

Since the endpoint map \(E_{f,g}\to V²\) factors through the genuine **image** \(A²=\operatorname{im}(E_2\to V²)\), and surjectivity of \(E_{f,g}\to T\) means its inverse-image frame map is injective, the original endpoint pair \(t:T\to V²\) itself factors through \(A²\). Explicitly, every frame equation valid on A² holds on E_{f,g}, so its pullback under t is forced by the injective frame map from T into E_{f,g}. There is no use of pullback-stability of the image \(E_2\twoheadrightarrow A²\): the **new** covering map E_{f,g}→T was separately constructed by N and verified surjective.

We have proved:
\[
\boxed{
\text{Every map }\operatorname{Loc}(B)\to Z\times Z
\text{ from a nonzero complete Boolean frame factors through }A².
}
\tag{3.3}
\]

## 4. The saturation and cube theorem

**Boolean-probe conservativity (independently proved in the companion closed-family theorem):** arbitrary complete Boolean frames jointly detect inclusion of sublocales in Loc. If S⊄T, choose two frame elements identified on T but not on S, then a closed quotient of O(S) followed by Booleanization separating their images; this gives a complete Boolean-valued generalized point S→T contradiction. No fit/local compact/spatial hypothesis is required.

Apply this to S=Z²⊆V² and T=A². By (3.3):
\[
\boxed{Z\times Z\subseteq A².}\tag{4.1}
\]
Reflexivity of A gives Δ⊆A². Thus \(\mathscr R_\infty=\Delta\vee Z²\subseteq A²\).

The [compact-local diagonal theorem](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md) and the [maximal remote relation theorem](ProjectA_closed_family_remote_equivalence_general_theorem_2026-11-11.md) give the reverse inclusion \(A²\subseteq\mathscr R_\infty\). Hence
\[
\boxed{A²=\Delta_V\vee(Z\times Z)=\mathscr R_\infty.}\tag{4.2}
\]
The general remote theorem already proved \(\mathscr R_\infty^\smile=\mathscr R_\infty\) and \(\mathscr R_\infty²=\mathscr R_\infty\); moreover if Δ⊆A⊆\(\mathscr R_\infty\), then \(\mathscr R_\infty A=\mathscr R_\infty=A\mathscr R_\infty\) by monotonicity and reflexivity. Substituting (4.2) gives
\[
\boxed{(A²)A=A(A²)=A²=A² A².}
\tag{4.3}
\]
By induction on the two subword lengths at the root of any parenthesized binary product of n≥2 copies of A, the factors are either A or \(\mathscr R_\infty\); all three possibilities AA, A\(\mathscr R_\infty\), \(\mathscr R_\infty\)A, and \(\mathscr R_\infty²\) evaluate to \(\mathscr R_\infty\). Thus every parenthesization equals A². Because \(\mathcal D_Y\) has a block diagonal with this A and Δ_\mathbb N, the same cube associativity and length≥2 stabilization hold for \(\mathcal D_Y\) on Y.

## 5. Adversarial checklist and status

1. **Full arbitrary-cover quantification:** Lemma 2 treats every Θ-admissible cover, not merely finite or countable clopen covers. Its only input is the existence of one member containing a Cantor-open neighborhood of the *entire* K_n for each n.
2. **Stone representation of arbitrary Boolean frame maps:** \(\hat f\) comes from the complemented Cantor clopen cylinder values. It need not preserve D/V pointwise; the proof explicitly avoids this assumption.
3. **Remoteness:** critical for density of \(\hat f^{-1}(D)\). Without it a constant point f gives a graph-like, nondense pullback of A.
4. **Arbitrary meet pullback:** inverse image on sublocales is right adjoint to the image-of-composition direct image, hence preserves arbitrary meets. Open pullbacks are open.
5. **Double-negation step:** every dense open sublocale contains the least dense sublocale \(W_{\neg\neg}\), and this containment is stable under *arbitrary meets of dense opens* by the very definition of sublocale meet. One does not infer surjectivity from density.
6. **True locale-surjection:** Lemma 3 proves \((T\times V)_{\neg\neg}\twoheadrightarrow T\) by literal injectivity of the inverse-image frame map, using a point of V and complemented elements of B.
7. **Boolean conservativity:** complete Boolean frames of arbitrary (set) size, not just \(\operatorname{RO}(V)\) or a geometric Cantor-map class; this is what upgrades generic-middle witnesses to a localic sublocale inclusion.
8. **Upper bound:** uses actual compact-local diagonal equality for A² and the independently recorded general closed-family theorem; revisit these in a separate adversarial read before publication.
9. **Transitivity and parentheses:** no reassociation is assumed. \(\mathscr R_\infty²=\mathscr R_\infty\) is proved directly by preservation of compact-local diagonality and maximality. Absorption then uses only monotonicity and the diagonal unit.
10. **Historical issue:** an earlier claim that dense subsets \(D_{\rm disc}\to C\) are localic surjections is false; those particular general nonassociativity examples are withdrawn pending repair. This does not enter the positive CO-01 proof.

**Disposition:** CO-01 is **internally solved positively**, conditional only on the explicitly proved lemmas and already internally checked compact-local remote theorem. **No independent external audit yet**, and no prior theorem ledger status is upgraded until independent scrutiny of the complete proof, especially Boolean remoteness and the image-to-endpoint descent in §3.
