# Point-Free Topology — How much does the free homology sheaf remember?

**10 November 2026 · Final new research segment before targeted external audit.** Internally derived coalgebra argument and externally cited counterexample. **Not independently blind-refereed; not a literature-priority assertion.** Follows [the Stone-indexed face-poset canonical-equivalence construction](PointFree_Stone_indexed_pointed_face_posets_nonconstant_canonical_equivalences_2026-11-10.md). The existing audited chain/hull foundations live in [the corrected canonical note](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md).

## 0. Setting and question

Let S be a nonempty Stone space, and \(X_m(S)\) be the coherent Stone-indexed pointed face-poset construction based on a chosen minimal face of the finite poset \(P_m=F(\partial\Delta^{m+1})\). The previous **working** theorem gives *canonical* equivalences in the Stone-sheaf \(\infty\)-topos \(\mathscr H\),
\[
\mathbf C(X_m(S))\xrightarrow{\sim}\mathbf I(X_m(S)),
\quad
\mathbf C(X_m(S))\xrightarrow{\sim}\mathbf D(X_m(S)),
\]
with common realization \(\mathcal E_m(S)=h(S)_+\wedge\underline{S^m}\) and
\[
\widetilde{\mathcal H}_m(\mathcal E_m(S);\mathbb Z)
\cong M_S:=\mathbb Z[h(S)].
\]
For \(m\ge2\), \(\pi_m(\mathcal E_m(S))\cong M_S\) by the internal Hurewicz theorem, with previous positive \(\pi_i\) vanishing. For \(m=1\), this is the abelianization of the first homotopy group sheaf. We proved that \(M_S\) is a **nonconstant** abelian sheaf whenever S is infinite. Does the isomorphism class of \(M_S\) actually reconstruct the topology of S?

This note sharply separates **unmarked abelian sheaf**, **canonically marked generator map**, and **canonical cocommutative coalgebra**. The last two are extra data; the sheaf-homology functor by itself does not automatically supply the coalgebra.

## 1. A published counterexample: unmarked M_S does NOT reconstruct S

**Clausen–Scholze, *Condensed Mathematics and Complex Geometry* (Bonn–Copenhagen lectures, 2022), Lecture III, page 26, following Question 3.6** explicitly state: if T is obtained by identifying **two distinct points of the remainder** \(\beta\mathbb N\setminus\mathbb N\) in the Stone–Čech compactification S=\(\beta\mathbb N\), then
\[
\boxed{\mathbb Z[h(T)]\cong\mathbb Z[h(\beta\mathbb N)]}
\]
as *unmarked condensed abelian groups*. Source: https://people.mpim-bonn.mpg.de/scholze/Complex.pdf (text on actual printed page 26, PDF page index 25; independent authors' statement, proof not reproduced in the notes).

Both T and \(\beta\mathbb N\) are Stone spaces, but they are **not homeomorphic**. Indeed \(\beta\mathbb N\) is extremally disconnected. Let a,b be the identified distinct nonisolated remainder points. Pick clopen V containing a but not b. The open saturated set O=V\{a,b}=V\{a} has closure containing a, but its image in the quotient has closure containing the glued point t while no neighborhood of t is contained in that closure (there are points arbitrarily near b but outside V). Thus the closure of an open in T is not open; T is not extremally disconnected. Zero-dimensionality of T: every neighborhood of t pulls back to neighborhoods of both a and b, each containing clopen neighborhoods whose union is a saturated clopen neighborhood; away from t similarly. Both underlying sets have the same infinite cardinality.

**Conclusion:** Even the entire *isomorphism type of the nonconstant homology sheaf* M_S does not distinguish all Stone spaces S; and for m≥2 the same applies to the first nontrivial homotopy **sheaf as an abelian sheaf**. This does **not** establish that the full pointed homotopy objects \(\mathcal E_m(S)\) and \(\mathcal E_m(T)\) are equivalent; nonlinear higher homotopy operations could distinguish them. That stronger question remains open in this project.

**External-reliance caution:** The isomorphism \(\mathbb Z[h(T)]\cong\mathbb Z[h(\beta\mathbb N)]\) is quoted from Clausen–Scholze, not independently proved by us. A targeted referee may check the source/proof or accept the published assertion explicitly as a prerequisite.

## 2. Marked generators trivially but precisely remember S

The **canonical generator map** \(\eta_S:h(S)\to U(M_S)\) comes from the free abelian sheaf adjunction. Its pointwise image consists of basis vectors \([s]\). Retaining \((M_S,\eta_S)\) as a **marked** object retains the domain h(S); since sheafified Yoneda is fully faithful, the marked pair immediately determines S. This statement is easy and is *not* a reconstruction from the unmarked abelian object. It motivates looking for a less redundant algebraic structure.

## 3. Canonical diagonal coalgebra and group-like reconstruction

The free abelian functor is strong symmetric monoidal from the cartesian monoidal category of condensed sets to condensed abelian groups:
\[
\mathbb Z[A\times B]\cong\mathbb Z[A]\otimes\mathbb Z[B].
\]
Linearizing the diagonal \(h(S)\to h(S)\times h(S)\) and the terminal map \(h(S)\to1\) gives a **canonical cocommutative, counital coalgebra structure**
\[
\delta:M_S\longrightarrow M_S\otimes M_S\cong\mathbb Z[h(S\times S)],\quad
\epsilon:M_S\to\underline{\mathbb Z},
\]
with \(\delta([s])=[s]\otimes[s]\) and \(\epsilon([s])=1\).

For any test Stone space T, define the **group-like section set**
\[
G_S(T)=\{x\in M_S(T):\delta_T(x)=x\otimes x,\ \epsilon_T(x)=1\}.
\]
This is naturally a condensed set. The natural generator map \(\eta_S:h(S)\to M_S\) factors into G_S.

**Theorem (coalgebra reconstruction; internally checked).** For every Stone S,
\[
\boxed{G_S\cong h(S)}
\]
naturally in S. Consequently the functor
\[
\boxed{\mathrm{Stone}\longrightarrow\operatorname{Coalg}_{\mathrm{cocomm,counit}}(\mathrm{CondAb}),
\quad S\longmapsto(M_S,\delta,\epsilon)}
\]
is **fully faithful**. Isomorphism of these **coalgebras** therefore implies homeomorphism of the Stone spaces.

**Proof using finite quotients:** Write \(S=\varprojlim_i S_i\), with each S_i finite discrete. Let \(\rho_i:M_S\to\mathbb Z[S_i]\) be the canonical coalgebra maps.

For finite E and \(x=\sum_{e\in E}n_e[e]\in\mathbb Z[E]\), group-like means
\[
\sum_e n_e[e]\otimes[e]=\sum_{e,f}n_en_f[e]\otimes[f],\qquad \sum_e n_e=1.
\]
Comparing coefficients over \(\mathbb Z\) gives \(n_e=n_e^2\in\{0,1\}\), \(n_en_f=0\) for e≠f; exactly one coefficient is 1. Thus the group-like elements in the **constant** sheaf \(\mathbb Z[S_i]\) over a Stone test T are exactly locally constant maps \(T\to S_i\).

Given x∈G_S(T), its projections \(x_i=\rho_i(x)\) yield compatible continuous maps \(f_i:T\to S_i\), hence a unique continuous f:T→S. The free generator \([f]\in M_S(T)\) has the same projections. **Crucial injectivity:** Clausen–Scholze, op. cit., Proposition 3.3 (printed p.25, PDF page index 24), identify \(M_S\) as the union of finite-\(\ell^1\)-bounded profinite subsheaves
\[
M_S\cong\bigcup_{N>0}\varprojlim_i\mathbb Z[S_i]_{\ell^1\le N}\ \subseteq\ \varprojlim_i\mathbb Z[S_i].
\]
Thus \(M_S\to\varprojlim_i\mathbb Z[S_i]\) is a monomorphism of condensed sheaves, implying x=[f]. Conversely any f produces a group-like section [f]. So \(G_S(T)=\operatorname{Cont}(T,S)\) functorially for all tests T; Yoneda yields G_S≅h(S). QED.

**Full faithfulness:** A coalgebra morphism \(\phi:M_S\to M_T\) sends group-like elements to group-like elements, hence induces a morphism \(h(S)\to h(T)\), which by full faithfulness of h is a unique continuous map \(f:S\to T\). Since M_S is free as an abelian sheaf on h(S), \(\phi=\mathbb Z[h(f)]\), and this map automatically preserves the diagonal coalgebra and counit. Hence every coalgebra morphism arises from exactly one continuous map.

**Important conceptual caution:** Even though \(M_S\) has a *canonical* diagonal coalgebra supplied by its *presentation as a free object*, an unmarked isomorphism \(M_S\simeq M_T\) need not preserve these distinguished coalgebra structures. Clausen–Scholze's example means some unmarked isomorphism **cannot** preserve them. Nor have we constructed a natural coalgebra on \(\widetilde{\mathcal H}_m(\mathcal E_m(S))\) purely from the *unmarked homotopy type* of \(\mathcal E_m(S)\). The reconstruction theorem is about **enriched homology with the fiberwise diagonal/generator data retained**.

## 4. Synthesis and next audit

The same sheaf \(M_S=\mathbb Z[h(S)]\) can be regarded in three increasingly informative ways:

| Data | What is established about recovering S |
|---|---|
| Underlying group \(M_S(*)=\mathbb Z[S_{\rm set}]\) | Only sees cardinality of S, not topology. |
| Unmarked condensed abelian sheaf \(M_S\) | Detects infinitude vs finite via nonconstancy, but **does not distinguish all nonhomeomorphic Stone spaces** (Clausen–Scholze example). |
| Condensed cocommutative coalgebra \((M_S,\delta,\epsilon)\) | **Fully faithfully remembers S** as its sheaf of group-like elements. |

This resolves the originally posed **homology sheaf reconstruction** question at the correct levels of structure, without overclaiming that the unmarked full sheaf-homotopy object \(\mathcal E_m(S)\) is or is not a complete invariant of S.

**Audit recommendation:** This completes the requested final research segment. Now audit **all post-10 November chain/hull developments** as a package: (i) nonconstant two-apex suspension and augmentation-kernel sheaf; (ii) arbitrary-locale open-cover equations and patched D-side Čech codescent; (iii) ordinal-sum joins and \(\pi_m\) sheaves; (iv) pointed Stone-indexed face-poset gluing with canonical C=I=D; (v) the new coalgebra reconstruction and literature-sourced counterexample. Preserve the fact that previous independent auditors did **not** see or verify these after-audit deductions, and retain a separate internal audit and independently blind external packet.
