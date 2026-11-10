# Coherent localic chain nerves and nonconstant sheaf homotopy — corrected canonical post-audit account

**10 November 2026 · Corrected mathematical consolidation after a third independent blind audit.** This note supersedes the **proof status**, not the historical provenance, of five post-audit working notes:
[two-apex suspension](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md);
[open-cover/D-side descent](PointFree_D_side_open_cover_Cech_descent_2026-11-10.md);
[mixed Čech/ordinal sums](PointFree_mixed_Cech_ordinal_sum_higher_nonconstant_homotopy_2026-11-10.md);
[Stone-indexed pointed face posets](PointFree_Stone_indexed_pointed_face_posets_nonconstant_canonical_equivalences_2026-11-10.md);
[free condensed homology and coalgebra](PointFree_free_condensed_homology_coalgebra_reconstruction_2026-11-10.md).

**Audit status:** A1–E3 **externally checked after three explicit repairs**; see the [unaltered report](audits/2026-11-10/postaudit-sheaf/Referee_report_original.md) and [reconciliation](PointFree_postaudit_sheaf_EXTERNAL_referee_reconciliation_2026-11-10.md). The last section here contains a **referee-origin post-report theorem independently checked by us, NOT covered by the blind audit**. The earlier general **canonical arrow theorem** C→I ≃ C→D was explicitly treated as a premise, already checked by a separate previous audit. No general claim of literature priority; standard topological and categorical constructions are attributed.

## 0. Scope and fixed definitions

We use classical coherent locales \(X\), \(K(X)\) the bounded distributive lattice of compact opens, and the Priestley specialization convention \(x\le y\) iff every spectral open containing x also contains y. For coherent X, the specialization relation can be presented using compact opens. For **arbitrary locales**, define the localic specialization relation \(\operatorname{Sp}_X\hookrightarrow X^2\) by **every** \(u\in\mathcal O(X)\):
\[
\pi_0^*(u)\le\pi_1^*(u)
\qquad(u\in\mathcal O(X)).
\]
Equivalently it suffices to impose the inequalities on a join-generating frame base. **Do NOT define this using only compact opens when X is not coherent** (in \(\mathbb R\) they give the wrong relation). The associated simplicial localic chains are \(\operatorname{Ch}_n(X)=\{x_0\le\cdots\le x_n\}\), and higher diagonal hulls are \(I_n(X)=\operatorname{cl}\Delta_{n+1}\) and \(D_n(X)=\operatorname{fit}\Delta_{n+1}\). In coherent X their actual proconstructible spectral sublocales have tuples with common **upper** and **lower** witnesses, respectively.

Let \(\mathscr H_\kappa=\operatorname{Shv}_\infty(\operatorname{Stone}_\kappa,\mathrm{finite\ jointly\ surjective\ covers})\), including the empty family covering ∅ and all necessary **finite limits and finite coproducts**; choose κ sufficiently large for the coherent objects used (no asserted κ-independence). Let h denote sheafified Yoneda. Put
\[
\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet X)|,\quad
\mathbf I(X)=|h(\operatorname{Patch}I_\bullet X)|,\quad
\mathbf D(X)=|h(\operatorname{Patch}D_\bullet X)|.
\]
The valid **earlier audited canonical arrow comparison** says \((\mathbf C(X)\to\mathbf I(X))\simeq(\mathbf C(X)\to\mathbf D(X))\) under \(\mathbf C(X)\) for every coherent X. All current equivalences are **in this sheaf \(\infty\)-topos after Patch** and do **not** claim intrinsic localic shape or unpatched witness-projection descent.

Notation: for nonempty 0-truncated \(A\in\mathscr H_\kappa\), \(\Sigma_{\mathrm{unred}}A=1\amalg_A1\). The *reduced* suspension is \(A_+\wedge\underline{S^1}\) for \(A_+=A\amalg1\), and analogously \(A_+\wedge\underline{S^m}\). These are not the same object without a chosen component and a suitable splitting. For a coherent Z, **SNC** means \(\mathbf C(Z)\simeq1\).

## A. Nonconstant two-apex suspensions (externally checked)

For nonempty Stone S, form \(P(S)=S\sqcup\{p,q\}\) with p,q incomparable maxima and \(s<p,q\) for all s∈S; patch topology is disjoint-union Stone. This is Priestley and defines a coherent \(X(S)\), with compact opens
\[
K(X(S))=\{\emptyset,\{p\},\{q\}\}\cup\{U\cup\{p,q\}:U\in\operatorname{Clop}(S)\}.
\]

**Theorem A1–A3 (externally checked).**
\[
\boxed{\mathbf C(X(S))\simeq\Sigma_{\mathrm{unred}}h(S),\qquad
\mathbf I(X(S))\simeq\mathbf D(X(S))\simeq1.}
\]
The closed downsets \(Z_p=S\sqcup\{p\}\), \(Z_q=S\sqcup\{q\}\) cover X; each has a greatest point and terminal chain realization, while their intersection is equality-ordered S and \(\mathbf C(S)=h(S)\). **Proof repair:** first see in *each simplicial degree* that the two represented chain subobjects cover and their union is a pushout over the intersection; then commute the levelwise Čech colimit with geometric realization to obtain the homotopy pushout. For I_n, the two full tuples \(Z_p^{n+1},Z_q^{n+1}\) cover with intersection \(S^{n+1}\), three Čech nerves over 1. The earlier canonical arrow theorem gives D≃1; alternatively use the ordinal sum contraction in §C.

Let \(\mathbb Z[h(S)]\) be the free condensed abelian sheaf, with augmentation ε to \(\underline{\mathbb Z}\), and \(K_S=\ker\varepsilon\). Then \(\widetilde{\mathcal H}_1(\mathbf C(X(S));\mathbb Z)=K_S\) and other reduced homology vanishes. Evaluation at * preserves sheafification and all colimits because every Stone cover of * splits; thus \(\mathbb Z[h(S)](*)=\mathbb Z[S_{\rm set}]\). Choose \(s_0\in S\) and the section \([\operatorname{id}_S]-[\mathrm{const}_{s_0}]\in K_S(S)\); its point-values \([s]-[s_0]\) are distinct for infinite S. A section of a **constant discrete** group sheaf over compact Stone S is locally constant with finite image. Hence **\(\mathbf C(X(S))\) is constant iff S is finite**. The homotopy cofibres of both canonical maps are \(\Sigma_{\mathrm{unred}}^2h(S)\), with the shifted K_S.

## B. All-locale open-chart equations and coherent D-side Čech codescent (externally checked after definition repair)

**Theorem B1 (arbitrary locale and arbitrary open cover).** For **any** locale X, let \(\bigvee_{i\in I}u_i=1\) with no finiteness or compactness assumption, and \(w_i=\bigwedge_{j=0}^n\pi_j^*(u_i)\in\mathcal O(X^{n+1})\). Using the **all-opens** specialization sublocale as defined in §0,
\[
\boxed{\bigvee_i w_i|_{\operatorname{Ch}_n(X)}=1,\qquad
\bigvee_i w_i|_{D_n(X)}=1.}
\]
In Ch_n, \(w_i=\pi_0^*(u_i)\), hence their join is 1. In D_n, \(w=\bigvee_iw_i\) pulls back to 1 along the diagonal, so \(O(w)\) contains the diagonal and therefore contains the fitted hull. Thus ordinary localic **open chart** maps cover Ch_n and D_n levelwise; open surjections are effective descent maps for locales. **This is not unpatched descent of the unrelated common-lower witness projection**, and without coherence it is not a statement about patched sheaf homotopy. **Literal counterexample to the pre-repair packet definition:** \(\mathbb R\) has no nonzero compact opens, so compact-open-only frame equations impose no specialization inequality and give the false Ch₁=\(\mathbb R^2\).

**Theorem B2 (coherent).** Let compact opens \(u_1,\dots,u_r\) cover coherent X, and for nonempty J⊆[r] write \(U_J=O(\bigwedge_{j\in J}u_j)\). For the *relative ambient lower hull*
\[
H_n^{X,\downarrow}(U)=D_n(X)\cap U^{n+1}
\quad\text{(generally NOT }D_n(U)\text{)},
\]
the canonical \(\mathbf C(X)\to\mathbf D(X)\) is the geometric realization of the natural transformation of **full Čech intersection diagrams**
\[
\mathbf C(U_J)\longrightarrow
\mathbf R_X^\downarrow(U_J):=
|h(\operatorname{Patch}H_\bullet^{X,\downarrow}(U_J))|.
\]
If all nonempty-intersection local maps are equivalences, the global **canonical** comparison is one, as is C→I by the previously audited arrow theorem. An open-cover good-nerve formula holds if all nonempty U_J are SNC. Do not replace full indexed Čech diagrams with multiplicity-free naive poset diagrams.

**Theorem B3 (exact LB and certificates).** For nonempty compact-open U=O(u), \(K(U)\cong[0,u]_{K(X)}\). The condition
\[
(\mathrm{LB})_u:\quad
(u\nleq k_i\text{ for }i=1,\dots,t)\Longrightarrow
\bigvee_{i=1}^t k_i\ne1
\]
for finite nonempty compact opens k_i is equivalent to a point z∈X below **every** point of U (z need not lie in U), and equivalent to \(H_n^{X,\downarrow}(U)=U^{n+1}\) for all n. Proof by prime-ideal extension and proconstructible point determination. If U has a **greatest point**, appending it contracts both the chain and relative D-hull; if LB holds and U is **SNC**, the relative D-hull is the Čech nerve of U→1 and the chain realization is terminal. Thus appropriate finite open-cover local certificates imply canonical C→D and C→I equivalences. Exclude the empty U (u=0).

## C. Mixed descent, ordinal sums, and nonconstant higher relative obstructions (externally checked after join/Hurewicz repair)

**Theorem C1 (mixed cover).** A finite closed-downset cover \(Z_i\) and a finite compact-open-upset cover \(U_j\) of coherent X yield a two-direction Čech cover of each \(\operatorname{Ch}_n(X)\) by \(Z_i\cap U_j\): choose a Z containing the last vertex and a U containing the first. After Patch, the iterated Čech realizations calculate \(\mathbf C(X)\). **The mixed cells need not cover the entire I_n or D_n**; use one-sided relative ambient hull charts for those.

**Theorem C2 (ordinal sum).** For nonzero coherent P,Q, the disjoint-union Priestley ordinal sum P⊕Q places every point of P below every point of Q. It is Priestley and
\[
\boxed{\mathbf C(P\oplus Q)\simeq\mathbf C(P)*\mathbf C(Q),\qquad
\mathbf I(P\oplus Q)\simeq\mathbf D(P\oplus Q)\simeq1,}
\]
where \(A*B=\operatorname{hocolim}(A\leftarrow A\times B\to B)\).

**Required join step:** the strict simplicial nerve is the simplicial join, levelwise a coproduct of products of chains with a unique cut; the classical comparison of its realization with the homotopy join holds objectwise in presheaves and descends to sheaves because sheafification preserves finite products and colimits. Both upper and lower witness simplicial objects admit extra degeneracies by inserting respectively a chosen point of P or Q, and the corresponding strict localic maps factor through the coherent hulls. Thus their patched realizations are terminal.

**Theorem C3 (layered homotopy obstruction).** Let A be a two-point antichain and S a nonempty Stone space. For r,s≥1 put \(X_{r,s}(S)=A^{\oplus r}\oplus S\oplus A^{\oplus s}\), with \(m=r+s\ge2\). Then
\[
\mathbf C(X_{r,s}(S))\simeq\Sigma_{\mathrm{unred}}^m h(S),\quad
\mathbf I=\mathbf D=1,\quad
\widetilde{\mathcal H}_m\simeq K_S.
\]
For \(m\ge2\) the **globally pointed** object is (m−1)-connected and \(\pi_m\simeq K_S\) by **sheaf-internal Hurewicz**. Proof repair: take the objectwise fibre of Y→τ_{≤m−1}Y, use left exactness of sheafification and its commutation with truncation; apply ordinary Hurewicz objectwise and then sheafify. **No hypercompleteness is needed.**

## D. Canonically equivalent yet nonconstant realizations (externally checked after Hurewicz repair)

Let P be a finite poset with a chosen **minimal** point v and let S be nonempty Stone. Form the Priestley ordered Stone space
\[
W_S(P,v)=\{v\}\sqcup \bigl(S\times(P\setminus\{v\})\bigr),
\]
with only same-fibre comparisons (and the shared v below the corresponding fibre upsets). Minimality of v is essential for transitivity and Priestley separation.

**Theorem D1–D2 (Stone-indexed pointed gluing).** In every simplicial degree the actual **patched** chain and common-upper hull sublocales decompose as
\[
\operatorname{Patch}\operatorname{Ch}_n(W)
=1\sqcup\left(S\times(\operatorname{Ch}_n(P)\setminus\{v_n\})\right),
\quad
\operatorname{Patch}I_n(W)
=1\sqcup\left(S\times(I_n(P)\setminus\{v_n\})\right),
\]
where \(v_n\) is the constant n-simplex. These are strict natural simplicial isomorphisms. They exhibit pushouts along a **clopen coproduct summand**; sheafified Yoneda preserves these pushouts, and realization gives canonical pointed identifications
\[
\boxed{\mathbf C(W)\simeq h(S)_+\wedge\mathbf C(P),\qquad
\mathbf I(W)\simeq h(S)_+\wedge\mathbf I(P).}
\]
The **canonical** map C(W)→I(W) is the smash of the actual finite comparison. It is an equivalence whenever C(P)→I(P) is. By the previously audited edgewise theorem, C(W)→D(W) is then an equivalence as well. In contrast, **D_n(W) need not glue fibrewise**; different S-fibres can have a common lower witness v.

**Theorem D3 (every positive degree).** Take \(P_m=F(\partial\Delta^{m+1})\), the **nonempty** face poset of a simplicial m-sphere, and v a vertex. The required nonempty intersections of principal downsets of maximal facets have a greatest point, and the empty intersection is **excluded** from the crosscut hypothesis. Then both canonical comparisons are equivalences and
\[
\boxed{
\mathbf C(W_S(P_m,v))\simeq\mathbf I(W_S(P_m,v))
\simeq\mathbf D(W_S(P_m,v))
\simeq h(S)_+\wedge\underline{S^m},
}
\]
where the arrows of comparison C→I and C→D, not merely the targets, are equivalences. The reduced homology sheaf in degree m is the **full** free abelian sheaf \(M_S=\mathbb Z[h(S)]\), with all other reduced homology zero. For m≥2, \(\pi_m\simeq M_S\) as the first nontrivial homotopy sheaf (pointed at the global shared vertex); for m=1, \(\pi_1^{ab}\simeq M_S\). When S is infinite, the section \([\operatorname{id}_S]\in M_S(S)\) has infinitely many distinct point-values, proving M_S nonconstant, so the **common C=I=D realization is itself genuinely nonconstant**. No new assertion about intrinsic shape or publication priority.

## E. Limits of reconstruction and canonical coalgebra (externally checked)

**Theorem E1 (published obstruction, independently algebraically checked).** Clausen–Scholze, *Condensed Mathematics and Complex Geometry*, printed p.26 after Question 3.6, give S=βN and T=S/(a∼b), with distinct remainder points a,b, such that **S,T are nonhomeomorphic Stone spaces** but \(M_S\cong M_T\) as **bare condensed abelian group sheaves**. E.g. S is extremally disconnected and T is not. Thus unmarked homology alone cannot reconstruct S. The earlier packet did **not** claim anything about unmarked *full* homotopy objects at this stage; see §F for the later referee-origin improvement.

**Theorem E2–E3 (coalgebra reconstruction).** By the free-abelian symmetric monoidal identity \(M_S\otimes M_S\cong\mathbb Z[h(S\times S)]\), linearizing the diagonal and terminal map supplies a cocommutative counital **coalgebra**
\[
\delta([s])=[s]\otimes[s],\qquad \varepsilon([s])=1.
\]
Its group-like elements \(x\) satisfy \(\delta(x)=x\otimes x\), \(\varepsilon(x)=1\), and form a subsheaf G_S (an equalizer). In a finite free group \(\mathbb Z[E]\), coefficient comparison shows a group-like is one basis vector. For profinite S=lim S_i, the natural maps to \(\mathbb Z[S_i]\) are coalgebra morphisms; any group-like section projects to a compatible family of locally constant maps, hence f:R→S. The free condensed sheaf embeds in \(\lim\mathbb Z[S_i]\) by Clausen–Scholze Prop. 3.3 (or the referee's independent point-value detection argument), so the group-like section is \([f]\). Therefore
\[
\boxed{G_S\cong h(S),\qquad
S\longmapsto(M_S,\delta,\varepsilon)\text{ is fully faithful.}}
\]
The coalgebra is **extra data** from the free generating Stone sheaf, not an unmarked homology/homotopy invariant. Even the unmarked **full homotopy object** does not recover it in general, as shown by the next post-report theorem.

## F. Post-report theorem (separate referee-origin status): full homotopy cannot reconstruct S

**NOT blind-checked in A1–E3.** The referee's post-audit §1 proves a **nonabelian** counterpart of E1. It has been independently verified here *after* the report, in [reconciliation §4](PointFree_postaudit_sheaf_EXTERNAL_referee_reconciliation_2026-11-10.md). We retain separate provenance.

For Stone S, quotient π:S→T=S/(a∼b) of distinct points, and clopen V with a∈V,b∉V, the free condensed **group** sheaves satisfy
\[
\operatorname{Fr}(h(S))\cong\operatorname{Fr}(h(T)\sqcup1).
\]
The inverse maps, written on generators, are
\[
\begin{aligned}
\Psi([x])&=\begin{cases}t[\pi x],&x\in V\\ [\pi x],&x\notin V,\end{cases}\\
\Phi(t)&=[a][b]^{-1},\quad
\Phi([\pi x])=\begin{cases}[b][a]^{-1}[x],&x\in V\\[x],&x\notin V.\end{cases}
\end{aligned}
\]
The Φ formula descends because it sends the identified pair a,b to the same group element [b], and the two homomorphisms compose to the identity on each generator. For S=βN, choose an isolated n∈N and use the shift homeomorphism β(N\{n})≅βN to obtain
\[
\operatorname{Fr}(h(\beta N))\cong \operatorname{Fr}(h(\beta N/(a\sim b))).
\]
For any condensed set A, \(A_+\wedge\underline{S^1}\simeq B\operatorname{Fr}(A)\); it is the objectwise wedge of circles, classifying the free group sheaf. Suspending gives, **for each m≥1**,
\[
\boxed{h(\beta N)_+\wedge\underline{S^m}\simeq
h(\beta N/(a\sim b))_+\wedge\underline{S^m}.}
\]
So the **entire unmarked pointed chain/hull homotopy object**, not just its homology, can fail to distinguish nonhomeomorphic Stone parameter spaces. The underlying coherent locales from §D remain distinct.

Likewise the unreduced suspensions of this specific pair are equivalent: both Stone spaces absorb an isolated point. To see this also for the quotient, choose an infinite clopen βC component disjoint from the identified pair by partitioning N into three infinite pieces and choosing one outside both ultrafilters; βC≅1⊔βC. Then S≅1⊔S and T≅1⊔T with the pair unaffected, and \(\Sigma_{\rm unred}h(S)\simeq B\operatorname{Fr}(h(S))\), and similarly T.

**Consequence for coalgebras:** an equivalence of the unmarked homotopy objects does **not** induce an isomorphism of the distinguished generator coalgebras, for their group-like subsheaves are \(h(S)\), \(h(T)\), and S,T are not homeomorphic. The reduced diagonal on spherical homology is *primitive*, not the group-like coalgebra of freely generated coefficients. No conflict with E2–E3.

### Two further post-report refinements, with separate status

**Direct fitted-hull comparison in the pointed-fibre construction (referee Post-audit 2).** The D-side is not literally fibrewise level by level, but each \(D_n(W_S(P,v))\) splits as a Stone-subobject union
\[
F_n\ \cup\ U_v^{n+1},
\]
where \(F_n\) consists of the constant-v tuple and tuples lying in a single S-fibre with an internal P-lower witness, and \(U_v=\uparrow_Wv\). Their intersection is the pointed S-fibre gluing of \((\uparrow_Pv)^{n+1}\). Both the full Čech nerve \((U_v)^{\bullet+1}\) and the intersection simplicial object realize to 1. The F-part realizes to \(h(S)_+\wedge\mathbf D(P)\), so their homotopy pushout gives
\[
\boxed{\mathbf D(W_S(P,v))\simeq h(S)_+\wedge\mathbf D(P)}
\]
**compatibly with the canonical C→D map**. This yields a second, **direct D-side** proof of the D3 application without invoking the general edgewise theorem. It is **referee-origin, independently internally checked after the third audit**, not a sixteenth blind-refereed claim. In particular, the false *degreewise* equality \(D_n(W)\cong1\sqcup S\times(D_n(P)\setminus\{v_n\})\) is NOT being asserted.

**Full fundamental group in degree 1 (referee Post-audit 3).** The standard objectwise graph/free-group calculation and exact sheafification give
\[
h(S)_+\wedge\underline{S^1}\simeq B\operatorname{Fr}(h(S)),
\qquad
\boxed{\pi_1\simeq\operatorname{Fr}(h(S)),\quad \pi_j=0\ \ (j>1).}
\]
Thus D3's m=1 case can be strengthened from a statement about the abelianization of \(\pi_1\) to an exact identification of the **full** fundamental-group sheaf. For the **unreduced** suspension of h(S), a choice of global point \(s_0\) yields \(\pi_1\simeq\operatorname{Fr}(h(S))/\langle\!\langle[s_0]\rangle\!\rangle\). These are after-report deductions, not part of the blind certificate.

## Verification and forward boundary

- **Externally audited after repairs:** A1–E3, relying on earlier canonical coherent chain/hull premises already independently checked. Their proofs use classical choice/prime-filter theorem.
- **Referee-origin and independently internally checked *after receipt*:** §F full unmarked homotopy counterexample. An external focused check of it may be useful if it becomes a headline publication claim.
- **Not proved:** intrinsic localic shape, κ-independence, exhaustive literature/priority assessment, or an unpatched homotopy counterpart of arbitrary-open chart descent.
- **Further mathematical targets:** an example of canonical C=I=D with nonconstant common realization that is *not* an internal suspension or indexed wedge; reconstruction from canonical **marked** diagrams or enriched homotopy data; consequences for the original **binary localic separation hierarchy**.

## References

- P. J. Cameron and Vinod Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783v1 §9 (homotopy type statements; detailed comparison performed in the preceding independent audit).
- P. Scholze, *Lectures on Condensed Mathematics* (2019, jointly with Dustin Clausen), Thm. 2.2 and proof, [source](https://www.math.uni-bonn.de/people/scholze/Condensed.pdf); updated arXiv:2605.03658 (2026).
- D. Clausen and P. Scholze, *Condensed Mathematics and Complex Geometry*, Lecture III, Props. 3.3, 3.5 and example after Question 3.6, printed pp.25–26, [source](https://people.mpim-bonn.mpg.de/scholze/Complex.pdf); arXiv:2605.11731.
- J. Lurie, *Higher Topos Theory*, Prop. 4.2.1.2 and standard topos Čech/truncation results; classical crosscut (Rota/Folkman/Björner), nerve lemma, Joyal–Tierney effective localic descent.
