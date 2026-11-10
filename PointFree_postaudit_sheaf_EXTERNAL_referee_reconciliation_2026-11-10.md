# Point-Free Topology — Reconciliation of the A1–E3 blind sheaf-homotopy audit

**10 November 2026.** This is the *post-report* mathematical reconciliation, not the independently blind audit itself. Original sources are preserved **unaltered** at [audit archive](audits/2026-11-10/postaudit-sheaf/README.md): [blind prompt](audits/2026-11-10/postaudit-sheaf/BLIND_PROMPT.md), [technical packet](audits/2026-11-10/postaudit-sheaf/BLIND_PACKET.md), [referee report](audits/2026-11-10/postaudit-sheaf/Referee_report_original.md), and [separate internal audit](audits/2026-11-10/postaudit-sheaf/INTERNAL_AUDIT.md). The referee expressly worked from only the prompt and packet, not the internal audit.

## Executive disposition

**All fifteen claims A1–E3 survive, with three explicit proof repairs.** Referee: no fatal counterexample, three repairable gaps, eight minor issues, three literature issues, and three presentation issues. Its 10 detailed mathematical verifications include independently rederiving the nonconstant sheaf-homology calculation, actual open-cover localic identities, the simplicial ordinal-sum join, finite-face-poset comparisons, and the full faithfulness of diagonal coalgebra reconstruction.

**Audit scope:** The independent referee **accepted** the earlier canonical edgewise arrow equivalence C→I ≃ C→D as a previously audited premise; it did not reprove that older theorem. The referee gives independent D-side methods for the new concrete examples. Lurie/∞-topos machinery, Priestley duality and Joyal–Tierney were relied on as standard background and not exhaustively re-read. **Do not call this a formal verification, complete literature search, or priority result.**

**New post-report theorem:** The referee independently proposed, *after* checking submitted claims, an isomorphism of **free condensed GROUP sheaves** on the nonhomeomorphic Stone pair \(S=\beta\mathbb N\), \(T=\beta\mathbb N/(a\sim b)\). The accompanying explicit maps are verified in §4 below. This proves the stronger negative statement that even the **full unmarked pointed homotopy objects** \(h(S)_+\wedge\underline{S^m}\) and \(h(T)_+\wedge\underline{S^m}\) are equivalent for each m≥1. This theorem was **not part of claims A1–E3** and should be marked *referee-origin, internally independently rechecked*, not *blind-refereed*.

## 1. Required repairs to the submitted mathematics

**Issue 1 (B1, arbitrary locales):** The packet's §0 used only compact opens k to impose the chain specialization frame inequalities \(\pi_0^*k\le\pi_1^*k\), even though B1 claims a theorem for **every locale**. For a noncompact connected space such as \(\mathbb R\), there are no nonzero compact opens and the literal defined Ch₁ is \(X^2\). The squares of cover members of \(\mathbb R\) do not cover all of \(\mathbb R^2\), so **the B1 Ch-half is false under that literal definition**. Repair: for arbitrary locales impose the inequalities for **all opens \(u\in\mathcal O(X)\)**, or a join-generating frame base. For coherent X the compact-open version is equivalent. Then the actual Ch_n relations imply \(w_i=\pi_0^*(u_i)\), so the arbitrary-open-cover identity is proved as intended. **The D-half of B1 never had this problem**; it follows directly from the fitted diagonal definition for any locale. The earlier working note [D-side descent](PointFree_D_side_open_cover_Cech_descent_2026-11-10.md) already states all-open specialization equations; the ambiguity was reintroduced in the compact §0 of the external packet. Keep the original blind packet unchanged.

**Issue 2 (C2, simplicial join):** In each degree, the Priestley chain locale of \(P\oplus Q\) splits as a finite disjoint union of products of P-chains and Q-chains, with unique cut. To deduce the homotopy-join equivalence one must invoke the classical weak equivalence of simplicial join and the homotopy pushout \(K\leftarrow K\times L\to L\), applied objectwise in presheaves, then use sheafification preserving finite products and colimits. The referee supplies this four-step argument. Reference Lurie, *Higher Topos Theory*, Prop. 4.2.1.2 (cited as an appropriate comparison, with the standard space-level consequence). This is **a proof repair, not an additional hypothesis**.

**Issue 3 (C3/D3, internal Hurewicz):** A sheaf \(\infty\)-topos need not be hypercomplete. For a pointed internally \((m-1)\)-connected sheaf object Y, take an objectwise fibre of \(Y\to\tau_{\le m-1}Y\); sheafification is left exact, commutes with truncation, and sends this fibre to Y. Classical objectwise Hurewicz gives, after sheafifying, \(\pi_m(Y)\cong\widetilde{\mathcal H}_m(Y;\mathbb Z)\) for \(m\ge2\). For m=1 its counterpart is \(\pi_1(Y)^{ab}\cong\mathcal H_1(Y;\mathbb Z)\). A specified **global base point** is needed. This argument does not require hypercompleteness. The equality with \(\mathbb Z[h(S)]\) in the examples stands.

## 2. Other repairs and notation (issues 4–17)

- **I4:** The finite face-poset crosscut condition quantifies over **nonempty intersections** of maximal downsets. In \(F(\partial\Delta^{m+1})\) the intersection of *all* facets is empty and should not be required contractible.
- **I5:** To identify the two-apex suspension by Čech descent, first work at each simplicial degree: the pair of subsheaves is a union of subobjects, hence a pushout along their intersection; **then** realize. One cannot automatically replace a full Čech nerve with a binary pushout of potentially non-monomorphic realized maps.
- **I6:** Explicitly fix \(s_0\in S\), and say evaluation at the one-point Stone site object preserves sheafification and colimits, hence \(M_S(*)=\mathbb Z[S_{\mathrm{set}}]\).
- **I7:** Define SNC as **specialization-nerve contractibility** \(\mathbf C(U)\simeq1\); state the spectral extra-degeneracy proof for the greatest-point LB alternative; exclude \(u=0\) from nonempty-U claims.
- **I8:** Choose Stone_κ closed under **finite limits and finite coproducts**, not just products/coprod, so Čech pullbacks and cover stability are available.
- **I9:** All-locale B1 gives degreewise ordinary-localic open effective descent only. No patched or homotopy statement for infinite covers/noncoherent X. The earlier lower-witness projection E→D is **not** the open-chart map; define it with its separate older counterexample or remove the casual reference from a self-contained theorem.
- **I10:** The group-like construction G_S is an equalizer **subsheaf**, maps to finite quotient free groups preserve coalgebra structure, and group-likeness for finite quotient groups is tested pointwise in a constant discrete group sheaf.
- **I11:** For Priestley separation, insist on **every** \(x\nleq y\), not just pairs of incomparable points.
- **I12:** The packet's “Commelin–Scholze, Lectures on Condensed Mathematics, Proposition 2.5” is an erroneous mixed reference. Use **Peter Scholze, *Lectures on Condensed Mathematics* (2019 notes, work jointly with Dustin Clausen), Theorem 2.2 and proof**, current 2026 arXiv version arXiv:2605.03658. The original LTE.pdf link is not a reliable bibliography entry. The later Clausen–Scholze *Condensed Mathematics and Complex Geometry*, Lecture III Props. 3.3, 3.5 and Question 3.6, is correctly referenced.
- **I13:** The published \(\mathbb Z[\beta\mathbb N]\cong\mathbb Z[T]\) example is indeed on printed p.26, after Question 3.6, in [Clausen–Scholze](https://people.mpim-bonn.mpg.de/scholze/Complex.pdf). Their Prop. 3.3 (printed p.25) describes free condensed abelian groups through bounded finite-quotient stages. The source does not prove the example there; both the packet and referee give independent algebraic explanations.
- **I14:** Classify Rota/Folkman/Björner crosscut theory, Borsuk nerve lemma and McCord's finite spaces as background. Cameron–Kumar arXiv:2610.14783v1 §9 was compared **directly in the previous independent report**, although **this** referee could not open it; the previous verification remains in force.
- **I15–16:** Avoid overloaded S,P,A,K,O; distinguish unreduced \(\Sigma A=1\amalg_A1\) from reduced \(A_+\wedge S^m\). Explain \((m-1)\)-connected / m-connective indexing, and “unmarked” means the bare homotopy object or abelian sheaf without a distinguished coalgebra.
- **I17:** Strengthen E3's caveat *after* verifying the referee-origin post-audit group-sheaf argument: the diagonal coalgebra cannot be recovered functorially from the **unmarked pointed homotopy object** in the βN example. The coalgebra on M_S is not the reduced-diagonal homology comultiplication of the sphere-suspension object; the latter is primitive in bottom degree.

## 3. Independently verified main theorem package (original claims)

**A1–A3:** For nonempty Stone S, two incomparable upper apices give coherent X(S) with \(\mathbf C(X(S))\simeq1\amalg_{h(S)}1=\Sigma_{\mathrm{unred}}h(S)\) and \(\mathbf I(X(S))\simeq\mathbf D(X(S))\simeq1\); the augmentation-kernel homology sheaf \(\ker(\mathbb Z[h(S)]\to\mathbb Z)\) proves **nonconstancy iff S is infinite**.

**B1–B3:** For *all locales* the actual all-open chain relation and fitted diagonal hull obey the coordinatewise-common-open cover equations for arbitrary open covers. This gives ordinary localic degreewise open-chart descent (not automatically a homotopy theory of Loc). For coherent X and **finite compact-open covers**, Patch converts the charts to Stone-surjective Čech covers, so the canonical chain→D map descends compatibly with relative **ambient** lower hulls, not intrinsic D_n(U). The LB condition is equivalent to an ambient common lower point and to \(H_n^{X,\downarrow}(U)=U^{n+1}\) for all n; endpoint/LB+SNC local certificates are sound.

**C1–C3:** Mixed finite closed/open charts yield a two-direction Čech presentation of the **chain nerve** (not the entire I or D hull). For nonzero coherent P,Q, \(\mathbf C(P\oplus Q)\simeq\mathbf C(P)*\mathbf C(Q)\), while both higher hull realizations are terminal. Layered antichains around a Stone center produce \((m-1)\)-connected chain objects \(\Sigma^m h(S)\), m≥2, whose first nontrivial homotopy sheaf is the nonconstant augmentation kernel for infinite S.

**D1–D3:** For finite pointed poset (P,v) with **v minimal** and nonempty Stone S, the Stone-indexed wedge \(W_S(P,v)=\{v\}\sqcup S\times(P\setminus\{v\})\) is Priestley. Its patched **chain** and **upper-hull** simplicial locales glue fibrewise along the singleton constant-v simplex, yielding \(\mathbf C(W)\simeq h(S)_+\wedge\mathbf C(P)\) and \(\mathbf I(W)\simeq h(S)_+\wedge\mathbf I(P)\), and the **canonical** C→I arrow is the fiberwise smash of the finite comparison. C→D follows from the previously audited edgewise arrow equivalence. For \(P_m=F(\partial\Delta^{m+1})\), the canonical maps C→I and C→D are equivalences, their common realization is \(h(S)_+\wedge\underline{S^m}\), and its first nonzero homotopy sheaf (m≥2; abelianization for m=1) is the nonconstant **full free** abelian sheaf \(\mathbb Z[h(S)]\). Crucial warning: **D_n(W)** need not glue fibrewise due to cross-fiber lower witnesses; only realization-level equivalence was claimed.

**E1–E3:** Clausen–Scholze's βN example means unmarked \(\mathbb Z[h(S)]\) need not recover S. By the canonical diagonal and counit, \(\mathbb Z[h(S)]\) becomes a cocommutative counital **coalgebra** whose **group-like subsheaf** is h(S); this coalgebra-valued functor on Stone spaces is **fully faithful**. The coalgebra is **extra structure from the free generators**, not automatically intrinsic to the homotopy invariant.

## 4. Referee-origin post-report theorem: full unmarked homotopy fails reconstruction

**Provenance:** the following explicit nonabelian strengthening appears only in the *post-audit section* of the returned report. Its generator formulas have been independently checked in this reconciliation, including inverses and continuity. It was NOT covered by the referee's blind verdict on claims A1–E3; label **referee-origin, independently internally checked after receipt**.

Let S be a Stone space with distinct a,b∈S, let π:S→T=S/(a∼b), and choose a clopen V⊂S with a∈V and b∉V. Write \(\operatorname{Fr}(h(-))\) for the **free group object in sheaves of discrete groups** generated by a condensed set.

**Lemma F (referee-origin).** There is an isomorphism
\[
\boxed{\operatorname{Fr}(h(S))\cong
\operatorname{Fr}(h(T)\sqcup1)}
\]
as unmarked sheaves of groups.

**Explicit inverse maps.** Denote the new free generator in \(\operatorname{Fr}(h(T)\sqcup1)\) by t. Define homomorphisms on generators
\[
\Psi([x])=\begin{cases}
t[\pi x],&x\in V,\\
[\pi x],&x\notin V;
\end{cases}
\qquad
\Phi(t)=[a][b]^{-1},
\qquad
\Phi([\pi x])=\begin{cases}
[b][a]^{-1}[x],&x\in V,\\
[x],&x\notin V.
\end{cases}
\]
The last rule is well-defined over the quotient: \(\Phi([\pi a])=[b]=\Phi([\pi b])\), so it descends by the effective-epimorphic Stone quotient S→T. Both rules are continuous morphisms of condensed **sets** into the underlying free groups, since they are given by separate formulas on clopen pieces; adjunction extends them uniquely to condensed-group morphisms. Check the composites on generators:
- x∈V: \(\Phi\Psi([x])=([a][b]^{-1})([b][a]^{-1}[x])=[x]\); x∉V is immediate.
- \(\Psi\Phi(t)=(t[\pi a])[\pi b]^{-1}=t\).
- For x∈V, \(\Psi\Phi([\pi x])=[\pi b](t[\pi a])^{-1}t[\pi x]=[\pi x]\), and otherwise immediate.
The two morphisms are inverse. This is a genuinely **nonabelian**, not merely homological, refinement of the Clausen–Scholze βN example. The free group sheaf is the sheafification of R↦free group on \(\operatorname{Cont}(R,S)\).

**Stone–Čech consequence.** Take S=βN, and let a,b be distinct points of its remainder. Choose one isolated n∈N; S={n}⊔S′ with S′≅S. The quotient T={n}⊔T₁, where T₁≅S/(a′∼b′) for another pair of remainder points a′,b′ (transported across the homeomorphism S′≅S). Lemma F applied to S and the pair a′,b′ therefore gives
\[
\boxed{\operatorname{Fr}(h(\beta\mathbb N))\cong\operatorname{Fr}(h(T)).}
\]
(There is no natural/canonical equivalence asserted; this is an unmarked abstract isomorphism.)

**Full homotopy consequence.** For each condensed set A, the pointed object \(A_+\wedge\underline{S^1}\) is the **classifying object** \(B\operatorname{Fr}(A)\): objectwise it is a wedge of circles indexed by A(R), and sheafification is left exact and preserves finite products and colimits. Thus
\[
h(S)_+\wedge\underline{S^1}\simeq
B\operatorname{Fr}(h(S))
\simeq B\operatorname{Fr}(h(T))
\simeq h(T)_+\wedge\underline{S^1}.
\]
Suspending \(m-1\) additional times yields
\[
\boxed{
h(\beta\mathbb N)_+\wedge\underline{S^m}
\simeq h(T)_+\wedge\underline{S^m}
\quad\text{for EVERY }m\ge1.
}
\]
Therefore the actual **full unmarked homotopy objects** of the Stone-indexed face-poset coherent locales fail to reconstruct S in general. The underlying locales remain nonisomorphic because their Priestley minimal-point loci have respectively extremally disconnected and non-extremally-disconnected Stone components. **This does NOT change or invalidate** the original canonically equivalent C,I,D theorem; it limits reconstruction from the common unmarked target.

**Additional short justification for the referee's aside about unreduced suspensions.** The referee also asserts \(\Sigma_{\rm unred}h(S)\simeq\Sigma_{\rm unred}h(T)\) for this pair. A useful missing detail is that **both S and T absorb one isolated point**, and not only S. Partition N into at least three infinite sets; there is an infinite subset C⊆N whose closure βC is clopen and contains neither a nor b (each ultrafilter chooses at most one part). Then S=βC ⊔ β(N∖C), with a,b in the second component; the quotient T=βC ⊔ (β(N∖C)/(a∼b)). Since βC≅1⊔βC for countably infinite C, **the same homeomorphism proves** S≅1⊔S and T≅1⊔T, without moving the identified pair. Whenever X≅1⊔X, \(\Sigma_{\rm unred}h(X)\simeq h(X)_+\wedge\underline{S^1}=B\operatorname{Fr}(h(X))\). Thus Lemma F plus the βN isomorphism also identifies the corresponding *unreduced* suspension objects; iterated suspensions follow. This refinement remains separate from the 15 blind-checked claims.

**Stronger caution for the coalgebra theorem:** These equivalences do **not** intertwine the distinguished diagonal coalgebras on \(\mathbb Z[h(S)]\) and \(\mathbb Z[h(T)]\), since their group-like subsheaves would then be isomorphic, contrary to nonhomeomorphism. Thus the generator-diagonal coalgebra is **not determined by the unmarked pointed sheaf homotopy type**. The genuine reduced diagonal on the first nontrivial sphere homology is primitive; it is not the generator coalgebra.

## 5. Status, references and remaining research

**Now externally blind-checked after repairs:** A1–E3 of the Nov 10 post-audit packet. These depend on earlier audited coherent chain/higher-hull prerequisites; their underlying methods are mainly standard Priestley, crosscut, simplicial, \(\infty\)-topos, and condensed-mathematics machinery. Do not claim publication priority absent comprehensive literature check.

**New referee-origin internally rechecked, not independently blind certified:** Lemma F and nonhomeomorphic βN/T equivalences for *full unmarked* \(h(-)_+\wedge S^m\) and their unreduced suspensions. These may be suitable for a focused follow-up external verification but do not need to hold up the status correction for A1–E3.

**Remaining questions:** (i) identify possible *marked or enriched* homotopy structures intrinsically attached to the chain→hull comparison (rather than chosen free generators) which could recover S; (ii) characterize Stone spaces determined by their unmarked free **group** sheaf; (iii) examples with C≃I≃D whose common realization is nonconstant but not a suspension or pointed wedge of spheres; (iv) understand whether these sheaf-homotopy constructions have systematic relations back to the original binary separation hierarchy; (v) eventually perform the broader literature-priority investigation.

**Verified sources:** [Scholze, *Lectures on Condensed Mathematics*](https://www.math.uni-bonn.de/people/scholze/Condensed.pdf), theorem 2.2 and the symmetric monoidal free-abelian functor, and [Clausen–Scholze, *Condensed Mathematics and Complex Geometry*](https://people.mpim-bonn.mpg.de/scholze/Complex.pdf), printed pp.25–26, propositions 3.3/3.5 and example after Question 3.6 (the original PDF pages were checked directly). [Lurie, *Higher Topos Theory*](https://math.mit.edu/~lurie/papers/hitop.pdf) Prop. 4.2.1.2 compares simplicial join constructions; use only the appropriate weak-homotopy consequence.
