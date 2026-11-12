# Project A — CO-01 external referee reconciliation and required repairs

**11 November 2026.** Independent external referee read the self-contained CO-01 prompt and technical packet and reported a **positive verdict, conditional on integrating two missing proof segments and minor clarifications**. The referee's full report was supplied in the project conversation; this note records mathematical conclusions and repairs, not the report verbatim. The referee did not independently inspect all GitHub background notes, and its comparison with Arrieta's original paper was to the arXiv version rather than a line-by-line journal-PDF comparison. These are provenance limits, not identified counterexamples.

## 1. Theorem/status after review

Notation: \(C=2^{\mathbb N}\), \(K_n\) the finite sets of nonzero binary sequences with last 1 at index \(n\), \(D=\bigcup_nK_n\), \(V=C\setminus D\). Let \(Y\) be the extension of \(V\) by the new discrete set \(\mathbb N\) in Arrieta's construction, \(A=\mathcal D_Y|_{V\times V}\), and
\[
Z=\bigwedge_{K\subseteq V\;\mathrm{compact}}\mathfrak o(V\setminus K),\qquad
R_\infty=\Delta_V\vee(Z\times Z).
\]

The external referee independently checked and accepted, with presentational repairs:
\[
\boxed{\Delta_V<A<A^2=R_\infty,\quad R_\infty^2=R_\infty,\quad
(A^2)A=A(A^2)=A^2.}
\]
Every fully parenthesized word of \(n\ge2\) copies of \(A\) equals \(R_\infty\). The referee also checked the **abstract closed-family remote decomposition**, in its stated generality for any set-indexed family of closed sublocales of any locale.

The whole-\(Y\) transfer is correct **but its proof in the packet omitted two lemmas**. The corrections below complete it:
\[
\mathcal D_Y=A\vee\Delta_{\mathbb N},\qquad
P_n(\mathcal D_Y)=R_\infty\vee\Delta_{\mathbb N}
\quad(n\ge2,\text{ any bracketing}),
\]
so \(\mathcal D_Y<\mathcal D_Y^2\) and the two cubic bracketings coincide. Relations on \(V\times V\) and \(\mathbb N\times\mathbb N\) are viewed inside \(Y^2\) via their canonical sublocale embeddings. No associativity of general relation composition is assumed.

**Ledger status:** E = independent referee check **with referee-supplied transfer repairs**, to be read together with this reconciliation and the original full proof. No claim of publication novelty, universal associativity, or a general nonassociativity counterexample is made.

## 2. First missing lemma: exact block decomposition

Write \(V=\mathfrak o(v)\) and \(N=\mathbb N=\mathfrak c(v)\) as complementary open and closed sublocales of \(Y\). Pullback of sublocales preserves finite joins and arbitrary meets. The coframe \(\mathcal S(Y^2)\) is a distributive lattice. Therefore
\[
Y^2=(V\times V)\vee(V\times N)\vee(N\times V)\vee(N\times N),
\]
and **every** sublocale of \(Y^2\) is the join of its four restrictions; neither part of the decomposition needs to be clopen.

The \(V^2\) restriction is \(A\) by definition. For each \(n\in N\), a two-member \(Y\)-cover
\[
\big\{(W\cap V)\cup\{n\},\ V\cup(N\setminus\{n\})\big\}
\]
with Cantor-open \(W\supseteq K_n\) forces the restriction of \(\mathcal D_Y\) to \(V\times\{n\}\) into \(\bigwedge_{W\supseteq K_n}\mathfrak o(W\cap V)\). By fitness of the compact Hausdorff Cantor locale and meet-preservation of sublocale pullback, this is \(V\wedge K_n\) inside \(C\), hence zero: it is a sublocale of the **finite discrete** \(K_n\), so if nonzero it would have a point, which cannot land in the disjoint subspace \(V\). By symmetry the opposite mixed fibres vanish. Since the opens \(V\times\{n\}\) cover \(V\times N\), an arbitrary sublocale \(S\) of this product satisfies \(S=\bigvee_n(S\wedge(V\times\{n\}))\). Thus both *entire* mixed blocks vanish. On \(N^2\), discreteness and Hausdorffness give the diagonal. Consequently
\[
\boxed{\mathcal D_Y=A\vee\Delta_N.}
\]
The open-cover gluing law just used is special to **open covers**; do not replace it by an unrestricted claim about infinite joins of sublocales.

## 3. Second missing lemma: composition preserves finite joins

For any locale map \(f\), inverse image on sublocales \(f^{-1}:\mathcal S(M)\to\mathcal S(L)\) is a **coframe homomorphism**, hence preserves arbitrary meets and finite joins. Image on sublocales is left adjoint to inverse image and preserves arbitrary joins. Both facts are standard (e.g. the survey in *Journal of Pure and Applied Algebra*, “On infinite variants of De Morgan law in locale theory”, §2).

Let \(R_1,R_2,S\) be relations. With \(E(R,S)=p_{12}^{-1}R\wedge p_{23}^{-1}S\), one obtains
\[
E(R_1\vee R_2,S)=E(R_1,S)\vee E(R_2,S),
\]
and the analogous equality in the second variable. Applying the endpoint-image functor yields
\[
(R_1\vee R_2)\circ S=(R_1\circ S)\vee(R_2\circ S),
\]
and likewise \(R\circ(S_1\vee S_2)=R\circ S_1\vee R\circ S_2\). **Only finite distributivity is claimed.**

For \(P,Q\le V^2\), therefore,
\[
(P\vee\Delta_N)\circ(Q\vee\Delta_N)
=(P\circ Q)\vee\Delta_N.
\]
Indeed, the two cross sources have incompatible middle coordinates in \(V\wedge N=0\), while \(\Delta_N^2=\Delta_N\). The \(P,Q\) path source lies in \(V^3\), and its localic image calculated there embeds as the same image in \(Y^2\) (a surjection followed by an embedding). Induction on the binary tree of any bracketing gives the transfer in §1.

## 4. Clarifications to insert in a canonical proof

- Classical logic throughout; the Stone-space version of the boundary lemma also invokes the Boolean prime ideal theorem.
- Fix permutation notation \(\operatorname{supp}(\widehat\pi d)=\pi(\operatorname{supp}d)\); choose the large index beyond all prescribed prefix images (e.g. \(n>m+2\) in the explicit \(\sigma,\tau\) computation).
- Say “the fitted diagonal **of Arrieta's space**,” not that Arrieta himself computed this diagonal. Use a dictionary: the present \(V,Y,Z\) are not Arrieta's letter choices; \(Z\) is our compact-remote **sublocale**.
- Explain that \(K\times V\) is spatial for \(K\) compact Hausdorff (or give the alternative frame-cover proof) when using rectangles around the compact diagonal.
- Every compact \(K\subseteq V\) has empty interior in \(V\), so \(V\setminus K\) is dense. Thus \(Z\) contains the Booleanization of \(V\) and is nonzero, but has no ordinary points (singletons are compact). Likewise \(A\) contains the Booleanization of \(V^2\).
- Call \(R_{\mathcal K}\) the “greatest \(\mathcal K\)-locally diagonal relation.” Its restriction to a closed \(K_i\) can be checked directly by finite distributivity without invoking image stability. Transitivity is proved independently using **closed** base change, not reassociation.
- Under closed base change, a surjection \(e\) remains surjective by the explicit frame map \(\uparrow c\to\uparrow e^*(c)\), \(x\vee c\mapsto e^*(x\vee c)\). Do not confuse a dense inclusion with a surjection.

## 5. Referee's optional ultrafilter-free improvement (not needed for original verdict)

The referee supplies a stronger substitute for the Stone/ultrafilter boundary lemma. If \(h:\mathcal O(V)\to B\) is a frame morphism to **any frame** \(B\), \(h(V\setminus K)=1\) for every compact \(K\subseteq V\), then for every \(b>0\) and \(N\) there exist \(n>N\) and \(d\in K_n\) such that
\[
b\wedge h(W\cap V)>0\qquad
\text{for every Cantor-clopen }W\ni d.
\]
Proof: if false, cover \(\bigcup_{n>N}K_n\) by clopens \(W_d\) for which \(b\wedge h(W_d\cap V)=0\); let \(O=\bigcup W_d\). The traces of clopens disjoint from the **finite** \(F=K_1\cup\cdots\cup K_N\) cover \(V\), so obtain a clopen \(W_0\cap F=\varnothing\) and \(b'>0\) with \(b'\le b\wedge h(W_0\cap V)\). The set \(K=W_0\setminus O\) is compact and contained in \(V\). By remoteness \(h(V\setminus K)=1\), whereas
\(V\setminus K=(V\setminus W_0)\cup(O\cap V)\); \(b'\) meets both inverse images in zero, contradiction.

The density-of-pulled-back-\(A\) argument consequently works for **arbitrary parameter locales**, though the final generic-middle projection is only known to be surjective in the proof when the parameter locale is Boolean. Treat this mild strengthening separately from the theorem externally audited as initially stated.

## 6. Remaining questions, status and research priority

1. **Classify \(A\wedge Z^2\):** Is the referee's sufficient common-\(K_n\) boundary condition necessary for arbitrary remote Boolean endpoints?
2. **Effectivity of \(R_\infty\):** Is this internal equivalence relation a kernel pair, and how can the quotient be described?
3. **Generalize saturation:** The referee expects \(A^2=R_\infty\) for Stone spaces with pairwise disjoint compact \(K_n\), dense complement, and eventually ubiquitous \(K_n\). This extension is **not part of the referee's theorem verdict** and needs its own proof. Transfer to the whole fitted diagonal additionally uses finite \(K_n\).
4. **General localic nonassociativity:** the older dense-inclusion counterexamples remain **withdrawn**; the present theorem does not replace them. Any future example must directly verify true surjectivity and its nonstable base change.

### Archival pointers

- [Original full working proof](ProjectA_CO01_Arrieta_square_saturates_remote_equivalence_PROOF_2026-11-11.md).
- [Original external referee prompt](ProjectA_CO01_Arrieta_square_positive_EXTERNAL_blind_prompt_2026-11-11.md).
- [Closed-family remote theorem](ProjectA_closed_family_remote_equivalence_general_theorem_2026-11-11.md).
- [Compact-local restriction](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md).
- [Exact original cover and block computation](A-relational-composition-associativity-audit-VI-Arrieta-explicit-covers-2026-11-07.md).
- [Boolean nontransitivity witness](A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md).
- [Withdrawn historical examples: correction](ProjectA_CO01_historical_dense_inclusion_locale_surjection_CORRECTION_2026-11-11.md).

**Editorial policy:** Preserve the original working and referee packet files as historical records. This note identifies the required proof repairs; it does not retroactively claim those steps were present in the submitted packet.
