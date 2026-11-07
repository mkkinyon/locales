> **7 Nov 2026 PRIORITY/TERMINOLOGY CORRECTION AFTER READING BANASCHEWSKI (1992):** The strongly Hausdorff OPEN/CLOSED gluing argument in §§1–2 is **not claimed novel**. Compare Banaschewski (1992), Proposition A.6, for topological simple Hausdorff extensions with discrete remainder, and Arrieta (2024), Proposition 4.1, extending this to closed remainders that are spatial multipliers. Our Z×loc X-spatial formulation may be differently scoped; no priority claim without comparison. Crucially, Banaschewski’s “topological simple extension” in the Appendix is NOT the frame “singly generated extension” of §§1–4. See [internal source review and audit](A-mixed-composition-internal-audit-and-banaschewski-2026-11-07.md).

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

## 7. Rational-open real line: explicit nonspatial cross-boundary I

Let X have underlying real line and topology generated by the USUAL real-line opens plus the additional open Q⊂R. The open U=Q has its usual regular topology; the closed complement Z=R\Q (irrationals) has its usual nonlocallycompact Baire topology. X is ordinary Hausdorff and nonregular.

Let B=RO(R_usual). For any X-open a define

    f(a)=reg_R(a∩Q),     g(a)=reg_R(a∩Z),

where reg_R(A)=int_R(cl_R(A)). Restrictions a∩Q and a∩Z are open in the respective dense subspaces, and reg_R sends opens of either dense subspace to RO(R) as a frame hom (its finite meet and arbitrary join preservation follow by representing a subspace-open as O∩dense and using the double-negation nucleus of O(R)).

Every a∈O(X) has form a=V∪(W∩Q), for usual open V,W⊆R. Thus g(a)=reg_R(V)≤reg_R(V∪W)=f(a). So g≤f as generalized points Loc(B)→X. In particular (f,g) factors through B_X=A_X^smile⊆I_X.

For e=Q we have f(e)=1 and g(e)=0, so (f,g) factors through U×loc Z, giving a NONZERO sublocale

    I_X∧(U×loc Z)≠0.

It is POINTLESS: ordinary rational/irrational pairs can be separated in X, and I has precisely inseparable pairs as ordinary points. Since it is CLOSED in U×loc Z, this also proves U×loc Z is NONSPATIAL; otherwise every nonzero closed sublocale would have a point.

This is a concrete test space in which the failure of the spatial-product hypothesis in §2 is REAL, not merely formal. However the pair (f,g) arises from COMPARABLE generalized points, hence by itself does not witness a mixed-composition failure.

## 8. A Sierpinski-fiber theorem: I=D=kernel pair

Let S be the Sierpinski locale with points 0<1. **Theorem (new working).** Let Y be ANY locale with diagonal Δ_Y BOTH CLOSED and FITTED. Suppose i:X↪Y×S is a sublocale EMBEDDING (i*:O(Y×S)→O(X) is surjective). Let r:X→Y be first projection, and let K=(r×r)^{-1}(Δ_Y)=X×_Y X. Then

    **I_X=D_X=K=A_X B_X=B_X A_X.**

Proof: Δ_Y closed/fitted implies K closed/fitted and contains Δ_X, so I_X,D_X≤K. Now work over the universal K-pair (f,g):K→X², so rf=rg=t:K→Y. Let e∈O(X) be the image of the nontrivial S-open and put u=f*e,v=g*e. Each open of Y×S is represented by a≤b in O(Y), its inverse image under (t,p):K→Y×S being

    F_p(a,b)=t*a∨(p∧t*b).

For fixed t, as a function of the parameter p, F_(u∧v)(w)=F_u(w)∧F_v(w) and F_(u∨v)(w)=F_u(w)∨F_v(w), for EVERY w∈O(Y×S), by finite distributivity. As both (t,u) and (t,v) factor through the sublocale X, F_u and F_v coequalize the kernel congruence of the quotient i*. The displayed identities show F_(u∧v) and F_(u∨v) coequalize it too; therefore both factor via i*:O(Y×S)↠O(X), yielding two generalized points h_min,h_max:K→X.

Because every X-open is i*(w) for some product open w, the same formulas show h_min≤f,g≤h_max in the canonical specialization order. Hence the universal pair K factors via B A (common lower h_min) and A B (common upper h_max), proving K≤B A∩A B. The universal order-composite bounds B A≤D and A B≤I give equality with K.

Since K is a KERNEL PAIR, K∘K=K, and since K is fitted, I_X∘D_X=K=V_X. Thus NO sublocale of Y×S as above can refute the mixed V inclusion, even if its diagonal hulls are nonspatial.

**Application to the rational-open real line:** Let Y=R_usual, regular and hence its diagonal closed/fitted; the map

    i:X→R_usual×S, x↦(x,chi_Q(x))

is a sublocale embedding, since the topology of X is generated by its two coordinate inverse images. The theorem gives I_X=D_X=K, where K is the kernel pair of the continuous identity map r:X→R_usual.

Because r is real-valued, F_X≤K; universally K=I_X≤U_X≤F_X, so

    **I_X=D_X=U_X=V_X=W_X=H_X=F_X=K**, with M,J also K.

The explicit Boolean pair in §7 shows K>Δ_X and K has a nonzero POINTLESS locally closed rational/irrational boundary part. In particular K is NONSPATIAL (a spatial K would have spatial open-then-closed sublocales). Thus D is nonspatial but D=B A; this demonstrates why nonspatiality of D alone does not produce mixed failure.

## 9. Sharpness: two Sierpinski factors can fail

The theorem fundamentally uses ONE Sierpinski coordinate. It does NOT extend to arbitrary sublocales X↪Y×S². Take Y=1, and X the 2-point DISCRETE subspace of S² consisting of its two incomparable points (1,0) and (0,1). The induced map O(S²)→O(X) is surjective, so X is a sublocale embedding. Its kernel pair over Y=1 is X², whereas since X is discrete, I_X=D_X=Δ_X. Thus the assertion I_X=D_X=kernel pair fails for two S factors. Meeting/joining two *vectors* of Sierpinski coordinates may violate the equations defining X.

## 10. Status and future tests

The ORIGINAL rational bridge is strongly Hausdorff by §2 (I=Δ, so R=D=V). The DIFFERENT rational-open real line is NOT strongly Hausdorff, and indeed has I=D=U=V=F>Δ by §§7–8. Both are controls, not counterexamples.

The promising remaining test must involve inseparability that is NOT fully explained by a single Sierpinski-coordinate fibre lattice, and simultaneously a fitted diagonal whose nonspatial part DOES NOT reduce to B A. A plausible modification involves two or more interacting open predicates (S²-like fibres), plus a nonlocallycompact boundary, but the elementary finite S² example only refutes the overly broad kernel-pair theorem and provides NO mixed-composition counterexample.

The unrestricted inclusion I D≤V remains OPEN; it is proved for compact I-proper projections, spatial D, and the Sierpinski-fiber class in this note. Do not claim the stronger inclusion settled by the negative controls. New theorems in §§2,8 unrefereed; verify frame quotient/evaluation and spatial-product restrictions independently.

## 11. Whole-hierarchy version over a functionally separated base

The Sierpinski-fiber theorem of §8 has an additional uniform corollary.

Suppose Y has Δ_Y closed and fitted AND F_Y=Δ_Y, i.e. its continuous real-valued functions jointly separate the locale diagonal. For any sublocale X↪Y×S with projection r:X→Y, §8 gives I_X=D_X=K=ker(r). Because every real-valued function f on Y yields f∘r on X,

    F_X≤(r×r)^-1(F_Y)=K.

The universal inclusions I_X⊆U_X⊆F_X and D_X⊆V_X⊆F_X give

    **I_X=D_X=U_X=V_X=W_X=H_X=F_X=K**,

and M_X=J_X=K as well. Thus the full collapse does NOT rely on having a single real-valued projection r:X→R; any functionally separated base Y suffices.

For the rational-open line the base is ordinary R, so this recovers §8's stated collapse.

**Caution:** Do not replace the exact assumption F_Y=Δ_Y by 'Y is regular' without citing/proving the corresponding functional-separation theorem in the localic sense. Complete regularity may supply it classically, but the exact hypothesis avoids implicit spatial or choice assumptions.

## 12. New conceptual boundary for a counterexample

The results now eliminate two distinct defect mechanisms:

(A) If the nonregular boundary attached to a regular open sheet is a closed locally compact sober locale, the gluing theorem forces I=Δ and mixed composition collapses trivially.

(B) If the structure is carried by a SINGLE added Sierpinski open predicate over a base whose diagonal is closed/fitted, the kernel-pair theorem forces D=B A and mixed inclusion holds, even though I and D may both be nonspatial.

Therefore a counterexample to I D≤V obtained by modifying rational/open-layered constructions must evade BOTH restrictions. A natural controlled next class is a sublocale of Y×S² (two interacting open predicates), where the Sierpinski fibre meet/join proof no longer automatically works. The antichain example in §9 demonstrates this loss of automatic fibre-lattice closure, but is itself finite/coherent and cannot refute mixed≤V.

A second route is to retain one open predicate but use a base Y whose diagonal is not both closed and fitted; that route reintroduces the original separation problem in the base and may be less informative.

## 13. Literature-priority checkpoint (not a verification of novelty)

The special embedding X↪Y×S is a singly generated extension of the frame O(Y): a new open predicate is adjoined to the base opens. Existing literature is relevant, notably B. Banaschewski, *Singly generated frame extensions*, J. Pure Appl. Algebra 83 (1992), 1–21, cited by Arrieta–Picado–Pultr, *A new diagonal separation and its relations with the Hausdorff property*, Appl. Categ. Struct. 30 (2022), 247–263. Their paper also discusses weak/almost homomorphisms and 'simple extensions'. The present theorem may be an instance or easy consequence of known extension theory. No claim of novelty is appropriate until those sources have been read directly. The concrete I=D=kernel pair proof above is self-contained at the level of frame quotients and localic specialization relations.
