# Project A — Mixed composition into V: the rational-bridge test and a strongly Hausdorff gluing theorem

6 November 2026. **Working results, internally checked, not independent-audited; no priority claim.** Continues [the preceding direct attack](A-relational-composition-mixed-V-direct-attack-2026-11-06.md) and tests [the independently audited rational-bridge dual-far-strip counterexample](A-V-Claude-external-audit-reconciliation-2026-10-22.md). We use I=cl Δ, D=fit Δ, V=fit I, R=I∘D; localic products, not implicitly ordinary products.

## 1. Spatial-product restriction lemma for inseparability

Let X be the locale of a spatial Hausdorff topological space; let Z↪X be a sublocale represented by a spatial subspace Z, such that the localic product Z×loc X is spatial (and therefore its points carry the ordinary product topology). Then

    I_X ∧ (Z×loc X) = Δ_X ∧ (Z×loc X).

Indeed both restrictions are spatial sublocales of Z×loc X: I_X is CLOSED, hence its restriction is closed in the spatial product and so spatial; the diagonal restriction is the image of the spatial locale Z under the graph z↦(z,z), hence spatial. Their point sets coincide: for an ordinary pair (z,x), membership in I means the two points cannot be separated by disjoint X opens, which in a Hausdorff X means z=x. Spatial sublocales of a spatial ambient frame with the same point set coincide (each is generated as a sublocale by its points). This statement does not assume X×loc X itself spatial.

The same argument, with coordinates reversed, applies to X×loc Z. If Z is a locally compact sober space, then Z×loc X is the ordinary spatial topological product for any spatial X, a standard localic product theorem. A closed DISCRETE subspace Z is a particularly elementary case: Z×loc X is the coproduct of copies of X.

## 2. New strongly Hausdorff open/closed gluing criterion

**Theorem (working).** Suppose X is a spatial Hausdorff locale, U↪X an OPEN sublocale that is itself strongly Hausdorff (I_U=Δ_U), and Z=C(U) the complementary CLOSED sublocale. If Z×loc X is spatial, then

    **I_X=Δ_X**.

Proof. In the sublocale lattice of X², the sublocales U×loc X (open first-coordinate restriction) and Z×loc X (closed first-coordinate restriction) are complementary and jointly cover X². On the closed restriction Z×X, §1 says I_X equals Δ_X.

On U×X, restrict further to U×Z. This is an open sublocale of X×Z (with coordinates reversed), hence spatial because Z×X is spatial. It contains no I-point because X is Hausdorff and U∩Z=0. The restriction of I is CLOSED there, so has no points and must be 0. Therefore I_X∧(U×X) lies in the open U×U (complementary to U×Z inside U×X).

In U×U, the I relation of X is contained in the I relation of U: every disjoint pair of opens of U is a disjoint pair of opens of X because U is OPEN. Since I_U=Δ_U, this restriction lies in Δ_X.

Thus BOTH open and closed first-coordinate restrictions of I_X lie in Δ_X. The sublocale lattice is distributive under finite joins/meets, so I_X≤Δ_X, and the opposite inclusion holds by definition.

**Corollary.** If U is REGULAR and Z is locally compact sober, then X is strongly Hausdorff. This uses standard regular⇒strongly Hausdorff (Johnstone/Picado–Pultr) and locally compact factor⇒spatial localic product. No regularity assumption on X itself.

**Remark:** The spatiality/product assumption on Z is substantive. Merely knowing U is regular and X Hausdorff does NOT allow this conclusion for arbitrary nonlocallycompact Z: in that case Z×loc X may be nonspatial and the above point-determination argument breaks.

## 3. Original rational bridge is strongly Hausdorff

Original dual-far-strip counterexample X=L⊔R⊔Z consists of two OPEN copies of the rational line, L,R, and a CLOSED discrete countable set Z={z_n}, with attached rational tails near distinct irrational limits. X was proved Hausdorff, L⊔R is regular, and Z is discrete. Apply §2:

    **I_X=Δ_X**.

This is NEW information about that prior audited example; the prior counterexample to the unrestricted dual-far strip formula is unaffected because it only assumes the closed I relation and a graph-far open q. We DO NOT infer whether D_X=Δ_X: strong Hausdorff does NOT imply F-separated in general.

Since I_X=Δ_X,

    **I_X∘D_X=D_X=V_X**.

Furthermore q∨d_I=1 was proved in the audit, so q is an open neighborhood of I (and hence Δ); therefore D_X≤O(q). The proposed test residual

    E_q=I12∧D23∧C(q13)

is 0: I12=Δ12 reduces this to D13∧C(q13)=0. Thus the rational-bridge graph obstruction cannot be reached by mixed composition. This conclusively DISQUALIFIES the original candidate, not the universal problem.

## 4. Universal open localization of the mixed-composition defect

Let U↪X be an open sublocale satisfying the STRONG relative property

    I_X ∧ O(U⊠1) ≤ Δ_X.

Equivalently, on the part of I with its FIRST coordinate in U, both coordinates agree. For ANY relation T↪X², the composable-pair source I12∧T23 with first coordinate in U factors through Δ12∧T23, so its image in U×X lies in T. Conversely Δ≤I, so the image contains T. Localic images are stable under base change by OPEN embeddings, or equivalently this can be checked directly on each restricted source. Therefore

    **(I∘T)∧O(U⊠1) = T∧O(U⊠1)**.

In particular,

    **R∧O(U⊠1)=D∧O(U⊠1)≤V**.

For w open containing I, define E_w=I12∧D23∧C(w13) as before. Then

    E_w∧O(U_1)=0,

hence E_w≤C(U_1). Thus every possible mixed-composition defect must live over the CLOSED FIRST-COORDINATE complement of the largest open region on which I itself is diagonal. The converse-oriented relation D∘I has the transposed localization.

This is a stronger, practical construction screen than merely demanding D nonspatial: one must arrange that nonspatial D interacts with a genuine first-coordinate I-defect, not a regular open sheet where I is already the diagonal.

## 5. Necessary features for modifying the bridge

If a candidate is built from an open regular sublocale U and closed remainder Z in a Hausdorff spatial X, it cannot have nontrivial I unless Z×loc X is NONSPATIAL. In particular Z cannot be locally compact sober (including closed discrete or compact Hausdorff). A nonlocallycompact bridge boundary is necessary for this family of constructions, but is NOT sufficient.

The original rational-bridge dual-far witness q demonstrates infinitary fitted-neighborhood pathology, yet gives no mixed-composition failure because I=Δ. Any successful modification must first produce I>Δ (pointlessly, in a spatial Hausdorff X), and must make the E_w residual nonzero, not merely make a graph-null open w far from I.

## 6. Research status

Universal target **I∘D≤V** still OPEN. Previously established sufficient regimes: proper p2:I→X, D=B∘A (in particular D spatial), E=I12∧D23 spatial, and now all locales with I=Δ (rational bridge included). The gluing theorem is a structural no-go for a broad class of proposed Hausdorff bridge boundaries. The very explicit condition E_w≠0 is still the decisive witness for a counterexample; this segment proves E_q=0 for the obvious candidate.

No claim that the gluing criterion or its corollary is new to locale theory; compare separation/localic gluing literature before publication. Standard reference for regular locale⇒strongly Hausdorff: Johnstone *Stone Spaces*, III.1 and Picado–Pultr *Frames and Locales*, Ch. V; spatiality of locally compact-factor products standard.
