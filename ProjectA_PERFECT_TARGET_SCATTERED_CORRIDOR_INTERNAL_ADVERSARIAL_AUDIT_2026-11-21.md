# Project A — internal adversarial audit: scattered-fiber pseudo-isomorphisms over perfect Cantor spaces
## 21 November 2026 · Adversarial self-check, NOT an external referee verdict

**Sources:** [Perfect target, 1–2 fiber map, scattered-corridor algebra](ProjectA_PERFECT_TARGET_SCATTERED_CORRIDOR_SAFE_INFINITE_CHART_RANK_2026-11-21.md); [tensorized Cantor-to-Cantor version](ProjectA_PERFECT_SOURCE_TARGET_TENSORED_SCATTERED_PSEUDO_ISOMORPHISM_2026-11-21.md). **Imported, earlier separately externally audited:** [compact-Hausdorff p/q rectangular rule RC](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), [locally closed graph actions and algebra](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md), [finite-to-one graph membership iff finite chart rank](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md). **Published independent input:** Simmons/Picado–Pultr, T_D scatteredness gives every sublocale induced. No new originality/priority assertion.

### Executive provisional verdict

**PROVISIONALLY SOUND after focused challenges; independent audit recommended** before promotion. The new proof rests on a substantial localic generator lemma (SF/MAT) and an **actual** 15-element graph-composition semigroup in the image/pullback relation category. The tensorized version is stronger than the original: the **source and target are both Cantor spaces**, fibers have size 1 or 2, rank is infinite, and graph adjunction to the full rectangular algebra remains associative. None of this is asserted as covered by the previous referee reports.

### 1. Challenge: does "scattered K" force an arbitrary nonspatial W⊂Z×K to split into fibers?

**Claim:** \(W=\bigvee_{k\in K}W\wedge(Z\times\{k\})\) for compact Hausdorff Z, compact Hausdorff scattered K.

**Adversarial proof:** Let J be fiber join. If J≠W, compact-Hausdorff Z×K is regular/fit, so some ambient open O contains J but not W; F its closed complement; W'=W∧F≠0 by finite distributivity. Least closed support L=cl(W') is a nonempty compact closed subset of Z×K; W' is dense in L. The projection P=pr_K(L) is nonempty closed scattered. Choose k isolated in P and K-open V with V∩P={k}. Since L meets Z×V, density ensures W'∧(Z×V)≠0. But W' is supported in L, so this piece is supported inside Z×{k}, hence ≤J∧F=0, contradiction. **No point of W' is selected.**

The crucial **order-surjectivity check** for MAT: given fiber family (A_k), W=∨ A_k×{k} has k-slice exactly A_k because all other pieces lie in Z×[K\{k}], disjoint from Z×{k} by the published point-determination theorem for scattered K. Finite distributivity handles the final meet. Therefore Sub(Z×K)≅∏_k Sub(Z) as **complete lattices**. This is NOT the invalid claim that K is the *topological* disjoint union of its singleton points.

**Risk to watch externally:** this arbitrary-fiber-generation proof is the largest genuinely point-free new step. The fit-open-separator and least-closed-support density requirements should be independently checked, especially for W nonspatial.

### 2. Challenge: is the source "discrete D" enough after tensoring with perfect P?

Yes, since P×D is a topological/localic disjoint union of copies P; sublocales decompose over the discrete D-coordinate. For any compact Hausdorff Z, the map id_Z×id_P×b:P×D→P×K relabels each closed P×{b(d)} fiber, so its inverse-image and image sublocale operators are inverse **order isomorphisms**. No assumption that P is scattered is made; fibers carry arbitrary, possibly pointless sublocales of Z×P. The p rectangle formulas can be checked by restricting induced spatial p(A,B) to **closed target fibers** P×{k} and pulling back the fiber isomorphism; the q formulas use the full sublocale fiber decomposition. Both outputs preserve exactly p versus q.

**Caution:** ordinary g=id_P×b is NOT a locale isomorphism between P×D and P×K in general; only the operators on **sublocale lattices** are inverse. It is important not to deduce topological openness of g or a continuous inverse.

### 3. Challenge: do the graph and converse multiply to actual partial diagonals?

For γ=Γ_g, \(\gamma\circ\gamma^\smile\) is the image of \(U\times_V U\). On the D×D discrete index fibers, distinct d,d' map into disjoint **closed singleton K fibers** so their pullback is zero; for d=d', the pullback is diagonal P. Therefore the result is precisely \(\Delta_U\), without extra pointless off-diagonal support. Conversely \(\gamma^\smile\circ\gamma\) is the image of \(U\to V^2\) under the diagonal of V; since g is onto all **ordinary** points of spatial V, its image is the whole spatial closed diagonal \(\Delta_V\). This direction uses localic images, not an unjustified inverse locale map.

### 4. Challenge: is the claimed 15-element graph semigroup really closed?

Represent the three source/target sectors by **five abstract orbit labels**
\[
B_K,\ B_{\rm out},\ Y_K,\ Y_{\rm out},\ U_K.
\]
The homeomorphism h maps B_K↔Y_K and B_out↔Y_out; the pseudo-bijection g maps U_K↔Y_K. Take graphs, converse, total identity, and close ordinary partial-bijection composition. A separate **finite combinatorial calculation** finds exactly **15** partial maps:
\[
0,\Delta_G,\Delta_B,\Delta_Y,\Delta_U,\Delta_{K_B},\Delta_{K_Y},
h,h^{-1},g,g^{-1},b,b^{-1},t,t^{-1},
\]
where b=h^-1g:U→K_B and t=h|_{K_B}:K_B→K_Y. This calculation checks **only** the ordinary index semigroup, not the locale composition identities.

For localic multiplication, pairs containing only genuine locally closed homeomorphism graphs compose as usual. Pairs containing pseudo arrows reduce via a homeomorphism or to one of the two γ∘γ^smile identities above. No additional graph words or shifted supports emerge; products with sectors that do not meet vanish by disjointness. An external referee should inspect this case reduction, not regard the 15-element combinatorial enumeration as a proof by itself.

### 5. Challenge: can arbitrary rectangles be acted upon without losing nonspatial support?

For **p**, restricting induced [A×B] to an open U or closed V sector remains the induced spatial sublocale of the ordinary restriction. The pseudo pullback over U=P×D splits by D, and every component is an isomorphic spatial pullback from a fixed closed P×{k}; hence the output stays p of the transformed ordinary endpoint subsets.

For **q**, with nonspatial arbitrary [A]×[B], one must *not* replace it by its point-generated part. The actual product pullback to P×D or P×K decomposes as a family of arbitrary sublocales of (G×P), and pushing across g relabels **the whole family** by MAT. Thus q maps exactly to q, including pointless components. This is the essential reason the graph-action identity survives tensorization.

### 6. Challenge: RHR overlap tests and eight triple cases

For genuine partial homeo arrows h,t, prior referee already checked localic overlap transport. For pseudo arrows g,b, the overlaps are contained in open U=P×D and closed V=P×K. Their sublocale lattices are identified by the parameterized transport isomorphism; inverse image of point-generated support \([g(E)]\) equals \([E]\) for ordinary E⊂U, and inverse image commutes with the relevant meets because it is a lattice isomorphism. Hence the two RHR overlap tests are simultaneously nonzero/zero, with no need to select ordinary points of the possibly pointless P-fiber meets.

Other cases: RRR via separately refereed RC, allowing empty outer endpoints; HHH via actual graph semigroup multiplication; RRH/HRR via endpoint restriction after the same rectangular overlap; RHH/HHR via composition of the transformed ordinary endpoint subsets; HRH via independent outer-coordinate actions. Finite distributivity extends from individual generators to all finite joins.

### 7. Challenge: are the source and target really perfect Cantor and rank infinite?

Unparameterized source X=C×{0} plus isolated upper points is compact metrizable zero-dimensional; target C is Cantor. f has max two-point fibers and infinite chart rank because the upper discrete selector maps onto closed K=[0,ω^ω], which cannot be a finite union of discrete subsets.

After P=C product: \(\widetilde X=P\times X\) and \(\widetilde Y=P\times C\) remain compact metrizable zero-dimensional and are **perfect**, because every nonempty open set varies in the perfect P coordinate. Hence each is Cantor. F=id_P×f has same fiber bounds. Any finite locally closed homeomorphic chart cover for F restricts along a closed P-coordinate fiber {p}×X to a finite locally closed homeomorphic chart cover for f, contradiction. Thus rank∞. The addendum's finite-to-one graph membership equivalence places Γ_F **outside** the known locally closed-graph algebra, while the new 15-relation algebra places it safely inside a larger associative calculus.

### 8. Current research interpretation

If this proof survives external scrutiny, neither *perfect target* nor even *both perfect source and target* plus **uniform degree 2** rescues the necessity of finite locally closed chart rank. The substitute mechanism is **stable witness transport across a closed scattered index**, even while each fiber carries arbitrary nonspatial Cantor information. The next useful goal is to formulate **relative scattered-coordinate witness stability** independent of this specially engineered construction, or to find a map whose graph passes all NR tests but fails to adjoin associatively.

**Recommended external-audit priorities:** SF/MAT, preservation of q under pseudo transport, the graph-only semigroup composability calculation, the eight mixed generator cases, and restriction of a chart cover to a closed parameter fiber. Internal verdict is PROVISIONALLY POSITIVE, not a substitute for a blind referee.
