# A general localic theorem: maximal equivalence relation diagonal on prescribed closed sublocales

**11 November 2026 · internally checked working result, not independently refereed.** This abstracts and strengthens [the compact-remote Arrieta relation](ProjectA_CO01_compact_remote_maximal_equivalence_2026-11-11.md). Crucially, **no regularity, spatiality, compactness, or fit assumption is needed** for the general decomposition: complete Boolean frames jointly detect frame equations. This is a new deduction for our project, not a literature novelty claim.

## 1. Boolean frame-valued generalized points detect all sublocale inclusions

**Lemma 1 (Boolean quotient separation).** For every frame F and elements x,y∈F with \(x\nleq y\), there exist a nontrivial complete Boolean frame B and a frame morphism \(h:F\to B\) with \(h(x)\nleq h(y)\).

**Proof.** Take the closed frame quotient \(q_y:F\to\uparrow y\), \(t\mapsto t\vee y\). In the quotient frame, y is bottom, while x∨y is nonzero because x\nleq y. Compose with the double-negation quotient \(\nu:\uparrow y\to(\uparrow y)_{\neg\neg}=B\). The complete Boolean frame B is nontrivial and \(\nu(x\vee y)\ne0=\nu(y)\), since \(z\le\neg\neg z\) and double negation preserves bottom. QED.

**Corollary 2 (Boolean probe conservativity).** For sublocales \(S,T\hookrightarrow X\) of **any** locale X,
\[
S\le T\quad\iff\quad
\text{every locale map }\operatorname{Loc}(B)\to S
\text{ with B a nontrivial complete Boolean frame factors through }T.
\tag{1.1}
\]
**Proof.** If S⊄T, the congruence \(C_T\) on O(X) is not contained in \(C_S\). Choose x,y in \(C_T\setminus C_S\), so x,y agree in O(T) but their images \(\bar x,\bar y\) in O(S) differ. By Lemma 1, choose an appropriate Boolean quotient \(h:O(S)\to B\) separating \(\bar x,\bar y\). The corresponding Boolean-locale map to S cannot factor through T, since x,y are identified in T. QED.

*Important:* this does **not** mean the one fixed Boolean algebra RO(V), or any particular geometric family of B-valued maps, is conservative. The test ranges over all complete Boolean frames and all frame maps.

## 2. Abstract closed-family compact-remote decomposition

Let X be a locale and \(\mathcal K=\{K_i\hookrightarrow X:i\in I\}\) a set-indexed family of **closed sublocales**. Let \(U_i=X\setminus K_i\) be their open complements. Define
\[
Z_{\mathcal K}=\bigwedge_{i\in I}\mathfrak o(U_i)\hookrightarrow X,\qquad
R_{\mathcal K}=\Delta_X\vee(Z_{\mathcal K}\times Z_{\mathcal K})\hookrightarrow X².
\tag{2.1}
\]
Call a relation S⊆X² **\(\mathcal K\)-locally diagonal** if Δ⊆S and, for every i,
\[
S\cap(K_i\times X)=\Delta_{K_i}
=S\cap(X\times K_i),
\tag{2.2}
\]
with diagonal graph inclusions interpreted via K_i→X.

**Theorem 3 (remote decomposition, all locales).** Every \(\mathcal K\)-locally diagonal relation S satisfies
\[
\boxed{\quad S=\Delta_X\vee(S\cap(Z_{\mathcal K}\times Z_{\mathcal K}))
\ \le R_{\mathcal K}.\quad}
\tag{2.3}
\]

**Proof.** By Boolean conservativity it suffices to show any \(T=\operatorname{Loc}(B)\to S\), where B is a complete Boolean frame, factors through the right-hand join. Write f,g:T→X for the endpoint maps. Since K_i is closed, its pullback along f is a **closed sublocale of T**, hence a *clopen* sublocale of the Boolean locale T; let \(b_i^f\in B\) represent it. Likewise define \(b_i^g\). Put
\[
c=\bigvee_{i\in I}(b_i^f\vee b_i^g)\in B.
\]
On each Boolean clopen \(T_{b_i^f}\) or \(T_{b_i^g}\), (2.2) forces f=g. Complete distributivity of finite meets over arbitrary joins in B implies f=g on \(T_c\), so the restriction of the map to that piece factors through \(\Delta_X\).

On \(T_{\neg c}\), the pullbacks of *each* closed K_i along both endpoint maps are zero; equivalently both maps factor through the open complement \(\mathfrak o(U_i)\) for every i. They therefore factor through the intersection \(Z_{\mathcal K}\), and together with T→S through \(S\cap Z_{\mathcal K}²\).

The disjoint clopen decomposition \(T\simeq T_c\sqcup T_{\neg c}\) produces a map \(T\to\Delta_X\sqcup(S\cap Z_{\mathcal K}²)\), hence into its localic image/join. By Corollary 2, S is contained in this join; the converse is immediate. QED.

## 3. Greatest relation and its internal transitivity

**Theorem 4 (maximal closed-family equivalence).** \(R_{\mathcal K}\) is itself \(\mathcal K\)-locally diagonal, hence the **greatest** such relation. Moreover
\[
\boxed{\quad
R_{\mathcal K}^\smile=R_{\mathcal K},\quad
\Delta_X\le R_{\mathcal K},\quad
R_{\mathcal K}\circ R_{\mathcal K}=R_{\mathcal K}.
\quad}\tag{3.1}
\]
Thus \(R_{\mathcal K}\) is a (thin) **internal equivalence relation** in Loc, regardless of general nonassociativity of image-defined localic relational composition.

**Proof.** Every \(Z_{\mathcal K}\) lies inside each open complement of K_i, hence \(Z_{\mathcal K}\cap K_i=0\). Pullback along a closed inclusion preserves the image-surjection of a family of sublocales' coproduct onto their join: any locale-surjection is stable under base change along a closed sublocale. Consequently
\[
R_{\mathcal K}|_{K_i\times X}
=(\Delta_X|_{K_i\times X})\vee((Z_{\mathcal K}²)|_{K_i\times X})
=\Delta_{K_i}.
\]
The symmetric second-coordinate restriction is analogous.

If S,T are \(\mathcal K\)-locally diagonal, then their composite is as well: restrict the composable-pair locale to a first endpoint in K_i. The first S-edge forces its middle endpoint to equal the first; the T-edge forces the final endpoint equal to it. The surjection from this composable source onto S∘T stays surjective under base change to the **closed** sublocale K_i×X, so the composite's restriction is exactly Δ_{K_i}, and similarly in the second coordinate. Thus \(R_{\mathcal K}²\) is \(\mathcal K\)-locally diagonal. Maximality gives \(R_{\mathcal K}²\le R_{\mathcal K}\); the reverse follows from reflexivity and monotonicity. Symmetry is clear. The internal composition map is simply \((x,y,z)\mapsto(x,z)\), and its categorical associativity is strict by uniqueness through the mono R↪X². QED.

**Further consequence:** If Δ⊆S⊆R_{\mathcal K}, then
\[
R_{\mathcal K}\circ S=R_{\mathcal K}=S\circ R_{\mathcal K}
\tag{3.2}
\]
by monotonicity and R²=R. No unparenthesized association is used.

## 4. Arrieta specialization and exact CO-01 residual test

For \(X=V=C\setminus D\) with \(\mathcal K\) all ordinary compact subspaces K⊂V, this recovers the nonzero pointless \(Z\) and maximal \(\mathscr R_\infty\) of the companion note. The special [Arrieta compact-local diagonal theorem](ProjectA_CO01_compact_restriction_diagonal_all_powers_2026-11-11.md) says every parenthesized finite power P(A) has the required restrictions, so
\[
P(A)=\Delta_V\vee(P(A)\cap Z²)\le\mathscr R_\infty,\qquad \mathscr R_\infty²=\mathscr R_\infty.
\tag{4.1}
\]
Hence
\[
(A²)A=A(A²)\iff ((A²)A)\cap Z²=(A(A²))\cap Z².
\tag{4.2}
\]

**Stronger sufficient condition to settle CO-01 positively:**
\[
A²=\mathscr R_\infty.
\tag{4.3}
\]
If this holds then
\[
\mathscr R_\infty=A²\le(A²)A\le\mathscr R_\infty²=\mathscr R_\infty
\]
and symmetrically A(A²)=\(\mathscr R_\infty\). But (4.3) is an **unproved new test**, not a theorem. Equivalently, because Δ⊆A²≤\(\mathscr R_\infty=\Delta∨Z²\),
\[
A²=\mathscr R_\infty\quad\iff\quad Z²\le A².
\tag{4.4}
\]
Boolean conservativity reduces the latter to: every pair of **arbitrary complete Boolean frame-valued generalized points** into Z factors through A². The previous fusion/Baire theorem established actual A–A witnesses only for the special fixed Boolean domain RO(V) and Cantor D/V-preserving continuous-map coordinates, so it **does not** prove (4.4). A negative test would find a remote Boolean-valued pair failing the A² endpoint congruence; a positive test needs genuinely new methods beyond Cantor endomorphisms.

## 5. Mathematical scope, confidence, and audit targets

This abstract theorem assumes only that the family \(\{K_i\}\) consists of **closed sublocales**; no spatiality, regularity, coherence, compactness or fit axiom enters the proof. Its key ingredients are complete Boolean quotients separating frame elements and pullback-stability of locale-surjections under **closed** sublocale inclusions. Both are provided explicitly above. Verify these in any external audit before importing the theorem into the fully audited Project A ledger. It does not assert general image stability, associativity of all relations, or effectiveness of R as a kernel pair.

**Nontriviality:** in locally compact Hausdorff locales where the interiors of compact subspaces cover X, \(Z_{\mathcal K}=0\) and the only \(\mathcal K\)-locally diagonal reflexive relation is Δ. In Arrieta V, \(Z_{\mathcal K}\ne0\) because compact subspaces have nowhere dense interiors and its double-negation sublocale lies in Z. The construction is genuinely localic and can be nonzero with no ordinary points.

**Audit focus:** (i) Booleanization of closed quotient separates frame elements; (ii) arbitrary join \(c=\bigvee_i b_i\) in a complete Boolean frame permits gluing equalities from all clopen K_i-pieces; (iii) closed-base-change of image-surjections for composite and finite join; (iv) the “all closed K_i” abstraction avoids silently treating arbitrary nonclosed subspaces as closed; (v) separate the new (4.3) hypothesis from established absorption.
