> **21 NOV 2026 — SCATTERED TARGETS: UNIVERSAL POINT-COVER STABILITY AND A GRAPH-ALGEBRA DICHOTOMY (NEW INTERNAL THEOREMS).** The [Cantor–Bendixson proof and graph-extension note](ProjectA_SCATTERED_TARGET_UNIVERSAL_POINT_COVERS_AND_GRAPH_ALGEBRA_2026-11-21.md) proves that for any **scattered sober** space Y, its canonical discrete point cover is **pullback-stably surjective**—indeed *every pointwise-surjective locale map* to Y is stable, including after pointless base changes. Conversely for **Hausdorff** Y, stability of the canonical point cover characterizes scatteredness, via a nonzero pointless Booleanization of a perfect closed subspace. Hence every selected spatial image into a scattered Hausdorff target is automatically HSIS. Combining this with the earlier INTERNAL graph-extension criterion gives a classification: a compact Hausdorff target Y is **universally safe for adjoining graphs of all compact-Hausdorff surjections to the finite rectangular algebra iff Y is scattered**; the negative direction uses a globally **open/proper** projection with a discrete selected support over two disjoint dense subsets of a perfect compact closed kernel (Hewitt resolvability; Cantor-space elementary version for metric Y). Also proved: every pointwise-surjective selected map is stable under all **spatial** base changes, and full stable surjectivity equals **inclusion stability after all Cartesian product amplifications**. These claims are internal/unrefereed and the positive graph-algebra half depends on our earlier unrefereed sufficiency criterion. The original Level-2 versus Level-3 question for non-scattered targets remains open.

# Project A — is hereditary selected-image stability necessary?
## Two-colour closed supports, Booleanized tests, and a strict gap between probe levels
**21 November 2026 · NEW INTERNAL RESEARCH; NOT independently audited**

**Question:** The [compact-boundary-fiber graph algebra](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md) gives a sufficient hypothesis for adjoining the graph of a continuous compact-Hausdorff surjection to the finite point-generated/full rectangular calculus: for every point subset E of the source, the selected-image map \(e_E:[E]\to[f(E)]\) is a **pullback-stable locale-surjection** (HSIS). Is this condition **necessary**?

**Current verdict:** The global necessity problem is **not solved** here. We prove (i) an exact ordinary topological formulation of the necessary singleton-probe condition (NR), (ii) NR for a **fixed** E does *not* imply stable surjectivity of \(e_E\), and (iii) an intermediate, strong criterion using Booleanizations of compact closed supports, equivalent to surjectivity after all **sublocale inclusion** base changes. The implication from stability under all sublocale inclusions to full stability under **arbitrary locale maps** remains a separate unproved step. All work is in classical Loc; no literature priority claim.

### 1. Topological characterization of a nonzero localic meet

**Lemma 1.1 (two-colour compact-support criterion).** For ordinary subsets A,B of a compact Hausdorff space Y,
\[
\boxed{
[A]_Y\wedge[B]_Y\ne0
\quad\Longleftrightarrow\quad
\exists\,\varnothing\ne K\subseteq Y\text{ closed with }
\overline{A\cap K}^{\,K}=K=\overline{B\cap K}^{\,K}.
}\tag{TC}
\]

**Proof.** If W=[A]∧[B]≠0, take K to be the least ambient closed support of W in Y; K is nonempty compact Hausdorff and W is dense in K. If nonempty relatively open N⊆K missed A, choose relatively open N'⊆K with nonempty compact closure L⊆N. Then [A]≤Y\ L, since L closed disjoint from every generating ordinary point; hence W∧N'=0, contradicting density of W in K. The same argument works for B.

Conversely, if both selected sets are ordinarily dense in nonempty K, the restrictions to K of [A] and [B] are dense sublocales of K. Both contain the least dense sublocale \(\mathcal B(K)\ne0\), so their meet is nonzero. No ordinary *common point* of A and B is required.

**Corollary 1.2 (two-colour density lifting).** Let f:X→Y be continuous between compact Hausdorff spaces, E⊆X, B⊆Y, D=f(E). The graph-probe necessary condition
\[
[D]\wedge[B]\ne0 \Rightarrow [E]\wedge f^{-1}([B])\ne0
\tag{NR}
\]
is equivalent to the topological condition: whenever some nonempty closed K⊆Y has D∩K and B∩K separately dense, there exists a nonempty closed L⊆X for which E∩L and f^-1(B)∩L are separately dense.

This follows from Lemma 1.1 and the [automatic exact inverse-image lemma](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md):
\(
f^{-1}([B])=[f^{-1}B]
\)
for continuous compact-Hausdorff f. The converse lifting direction is automatic: f(L) is compact closed, and the images of the two dense selected traces are dense in f(L).

Thus NR has a purely ordinary topological, **two-colour closed-support lifting** interpretation, even though its cause is an actual pointless localic intersection.

### 2. A single selected image can pass every ordinary probe and still be unstable

Let Y=2^ℕ be Cantor space, and let D be its **underlying set with the discrete topology**. Form the Stone–Čech compactification X=βD; the set-theoretic identity D_discrete→Y extends to a continuous surjection f:X→Y. Let E=D⊆X, the open discrete ordinary selected subset.

Then \([E]_X=D_{\mathrm{disc}}\), \(f(E)=Y\), and the selected image map is the pointwise-surjective continuous map
\[
e_E:D_{\mathrm{disc}}\to Y.
\]

For **every ordinary** B⊆Y, \([Y]\wedge[B]=[B]\ne0\) iff B is nonempty; and the pullback of [B] to D_discrete is precisely the discrete locale on B, hence nonzero iff B is nonempty. Therefore **NR holds for this fixed E and every ordinary B**.

Nevertheless \(e_E\) is **not pullback-stable**. The least dense Booleanization \(\mathcal B(Y)\) is nonzero and has no ordinary points: since Cantor is perfect, each Y\{y} is a dense open sublocale, so \(\mathcal B(Y)\le Y\setminus\{y\}\) for each y. Thus
\[
\boxed{D_{\mathrm{disc}}\times_Y\mathcal B(Y)=0,\qquad \mathcal B(Y)\ne0.}\tag{BFAIL}
\]
Pullback along the **nonspatial** sublocale inclusion \(\mathcal B(Y)\hookrightarrow Y\) destroys surjectivity.

**Crucial qualification:** This does **not** refute the global all-selected-subsets HSIS necessity conjecture. If Q⊂D is chosen countable dense in Cantor with dense complement I, then the new selected subset E'=Q has \([f(E')]=[Q]\), \([Q]\wedge[I]\ne0\), but \([E']\wedge f^{-1}([I])=0\) because E' is discrete. So the **global** rectangular graph algebra already fails a singleton NR probe. The example separates *fixed-E* probe strength, not the full algebra's global condition.

### 3. A universal Booleanized-closed-support generator theorem

**Proposition 3.1 (internal, abstract fittedness argument).** Let Y be compact Hausdorff and V≤Y **any** sublocale (it need not be spatial). Put
\[
\mathscr K(V)=
\{\,\varnothing\ne K\subseteq Y\text{ ordinary closed}:
  \mathcal B(K)\le V\,\}.
\]
Then
\[
\boxed{V=\bigvee_{K\in\mathscr K(V)}\mathcal B(K).}\tag{BG}
\]

**Proof.** The right-hand side J is ≤V. If J<V, **fitness of the regular ambient locale Y** supplies an ambient open sublocale O with J≤O but V≰O. Let F be its complementary closed sublocale. Then W=V∧F is nonzero. Its least closed support K is nonempty and contained in F; W is dense in K. Therefore \(\mathcal B(K)\le W\le V\), so K∈\(\mathscr K(V)\) and \(\mathcal B(K)\le J\). But also \(\mathcal B(K)\le F\), contradicting J∧F=0. Thus J=V.

This is a general generation statement for **all** sublocales of a compact Hausdorff locale, not just full products of spatial supports. It is a direct consequence of fittedness and the existence of least closed supports; no Cantor graph, countability or metrizability is needed.

### 4. Stable surjectivity along ALL sublocale inclusions

Let \(e:S\to V\) be any locale map, with V a sublocale of compact Hausdorff Y.

Call \(e\) **sublocale-base-change surjective** if for every inclusion W↪V of a sublocale, the pullback \(S\times_V W\to W\) is surjective. This is weaker a priori than the usual **pullback-stable** surjection, which quantifies over *all* locale maps T→V, not only inclusions.

**Theorem 4.1 (closed Boolean test).** The following are equivalent:

(a) e is sublocale-base-change surjective;

(b) every nonzero sublocale \(0\ne W\le V\) has nonzero pullback \(S\times_VW\ne0\);

(c) for every \(K\in\mathscr K(V)\), the pullback \(S\times_V\mathcal B(K)\) is nonzero.

**Proof.** (a)⇒(b) immediate. For (b)⇒(a), fix W≤V. If the image J of the base-changed map \(S\times_VW\to W\) were proper, ambient fittedness of Y supplies an ambient open O with J≤O but W≰O. Let F be its complementary closed. Then W'=W∧F≠0, but \(S\times_V W'\) is zero because its map to W factors through J and J∧W'=0. Contradiction.

(b)⇒(c) immediate because B(K)≤V is nonzero for every K in the list. For (c)⇒(b), take any nonzero W≤V and let K be its least ambient closed support. Then \(\mathcal B(K)\le W\le V\); so K∈\(\mathscr K(V)\). The nonzero pullback of B(K) lies within the pullback of W. Thus W has nonzero pullback.

**Boundary:** (a) is **not asserted equivalent** to full pullback-stability under *arbitrary* locale base changes. All known examples in this project are compatible with such a potential equivalence for selected images, but the present proof establishes only the sublocale-inclusion version.

### 5. Three levels of witnesses / probes

For a fixed selected subset E⊆X and e_E:[E]→[f(E)]≤Y we now distinguish:

**Level 1 — ordinary point-generated probes (NR).** For all ordinary B⊆Y, the pullback of e_E along \([B]\wedge[f(E)]\) is nonzero whenever the intersection is nonzero. By (TC) this is the ordinary two-colour closed-support lifting condition. This is exactly what the **singleton-marker graph probes available in the referee's finite p/q rectangular algebra** directly test.

**Level 2 — all localic sublocale-inclusion probes.** By Theorem 4.1 these are equivalent to nonzero pullback tests along the Booleanized closed supports B(K). They include genuinely pointless witnesses. In the βD example Level 1 holds for E=D but Level 2 fails at B(Y).

**Level 3 — arbitrary locale base changes (HSIS).** This is the current sufficient hypothesis for adjoining the entire graph calculus in [the map extension theorem](ProjectA_COMPACT_BOUNDARY_FIBERS_SELECTED_IMAGE_STABILITY_2026-11-20.md). It implies Level 2, which implies Level 1. The Level 1→Level 2 implication fails **for fixed E**. Whether Level 2→Level 3 holds under relevant extra hypotheses and whether *global* Level 1 for all E implies Level 3 remain **open here**.

A useful refined research question is whether global associativity of the finite p/q rectangular algebra with \(\Gamma_f,\Gamma_f^\smile\) at least forces **Level 2 for every selected E**. This would require extracting nonspatial Boolean tests from compositions involving rectangles and graph factors, rather than just ordinary selected sets.

### 6. Relation to the original graph motivation and next work

The original Cameron–Kumar program studies graph paths and common-witness intersections on ordinary points. The referee's rectangular algebra replaces pointwise vertex overlap with overlap of spatial **sublocales**. The topological two-colour criterion explains when a pointless overlap becomes a new ordinary graph edge. The stronger Booleanized probe theorem separates what the ordinary graph can detect from what genuinely nonspatial sublocales detect.

A failure of global HSIS need **not** automatically furnish a nonassociative triple involving two point-generated rectangles. This is the precise gap in a proposed converse characterization. The next target should be a *selected-image map that is Level 2 but not Level 3*, or a proof that no such maps exist under compact-Hausdorff source/target hypotheses. A second possible target is to find a map that satisfies global Level 1 for every selected E but still fails Level 2, demonstrating that ordinary bipartite graph probes are intrinsically incomplete.

**Literature context:** General locale surjections need not be pullback-stable; open/proper surjections are stable. Vermeulen's Frobenius formula for complemented sublocale pullback, as recalled in Igor Arrieta, *On Joins of Complemented Sublocales*, §2.6, shows that ordinary surjections are automatically stable along complemented inclusions, underscoring why the essential tests above use **noncomplemented, often pointless** sublocales. This literature observation does not establish the missing Level 2→Level 3 implication.

**Audit status:** All statements are newly internally derived; the previous independently reviewed compact-Hausdorff finite rectangular calculus is imported as a prerequisite. The two-colour criterion, the βD fixed-E counterexample and the Booleanized closed-support generator/probe test should undergo an internal adversarial check before promotion.
