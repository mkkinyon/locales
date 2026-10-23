> **UPDATE (23 October 2026):** The question “almost normal ⇒ V closed?” posed below has been answered **negatively** by a countable noncompact almost-normal thickened-zigzag space. See [A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md](A-V-almost-normal-nonclosed-thickened-zigzag-counterexample-2026-10-23.md). The original discussion is retained as research history.

# Project A: a genuine I-D / U-V order duality and the almost-normal closedness question

23 October 2026. **Working research note, with elementary verified finite-order calculations; audit before a publication claim.**

## 1. Notation

For a locale X put Q=O(X×_locX). Let Δ be its diagonal sublocale,
  I=cl(Δ)=C(d_I), D=fit(Δ), V=fit(I),
  U=C(d_U), with d_I=⋁_{a∧b=0} a⊠b, d_U=⋁_{a*∨b*=1}a⊠b.

The symbols D and F follow the existing Project A convention: D=fit(Δ) is unrelated to the FUNCTIONAL relation F.

Define the opposite composite
  W=cl(D)=cl(fit(Δ)).
Since D⊆U (known point-free theorem) and U is closed, W⊆U. Also Δ⊆D and I=clΔ, so I⊆W. Meanwhile Δ⊆I implies D⊆V, giving
  I,D⊆V and I,D⊆W⊆U.
One always has I⊆U and I⊆V. There is no general inclusion between U and V or between W and V.

This identifies the *literal* complementary construction to V=fit(clΔ) as W=cl(fitΔ), not necessarily U. Their equality W=U holds for all Alexandrov locales, but is not asserted generally.

## 2. All four point relations on Alexandrov posets

Let P be a poset with upward-open Alexandrov topology, R={(x,y):x≤y}, R^op its converse. As point relations (and for finite P also ordinary localic relations):
  I(P) = R∘R^op  = {(x,y):∃t≥x,y},
  D(P) = R^op∘R = {(x,y):∃t≤x,y},
  U(P) = (R∘R^op)^2 = I(P)∘I(P),
  V(P) = (R^op∘R)^2 = D(P)∘D(P).

Justifications: I is open-inseparability, i.e. common upper bound. D=fit(Δ) is the least open up-set containing the point diagonal, i.e. common lower bound. U means ↓↑x meets ↓↑y, i.e. a length-four zigzag x≤u≥z≤v≥y. V=fit(I) is upward saturation of I, i.e. length-four zigzag x≥p≤t≥q≤y. The inclusions of open/closed sublocales in the Alexandrov square are determined by these point sets.

A further equality:
  U(P)=cl(D(P))
since the downward saturation of common-lower-bound pairs is exactly the length-four relation R R^op R R^op. Consequently W(P)=U(P).

## 3. Exact order duality

Replacing P by P^op interchanges R and R^op, so *as relations on the common underlying set P²*
  I(P)=D(P^op),   D(P)=I(P^op),
  U(P)=V(P^op),   V(P)=U(P^op).

For **finite** P these are exact Hochster order-duality correspondences (finite T0 Alexandrov spaces are spectral and their Hochster dual has the opposite specialization order). For infinite P this is elementary order reversal; no Hochster/spectral hypotheses are implied.

Consequences:
- V(P) closed iff U(P^op) fitted.
- V(P)=I(P) iff U(P^op)=D(P^op).
- U(P)=I(P) iff V(P^op)=D(P^op).
Thus the user's proposed dual of V=I, namely U=I, needs refinement: the literal dual is U=D, because I itself dualizes to D rather than remaining fixed.

## 4. Classification of two U questions for Alexandrov locales

Let P_i be the comparability-connected components of P and put E=⋃_i P_i², which is the point set of the functional relation F.

Since the closed relation U(P) is a lower set and contains all comparable point pairs, it is fitted iff its point set is also an upper set, hence iff U(P)=E=F(P).

Equivalently:
  U fitted ⇔ U=F ⇔ for every x,y in the same comparability component,
   ∃u≥x, v≥y, z≤u,v.
This is the condition of one length-four *upper–lower* zigzag connecting x to y.

Similarly the earlier Alexandrov result:
  V closed ⇔ V=F ⇔ for every x,y in same component,
    ∃p≤x,q≤y,t≥p,q.
This is the order-dual length-four *lower–upper* zigzag.

Moreover U(P)=I(P) iff I(P) is transitive (since U=I²). The transitivity of the common-upper-bound relation is equivalent to upward directedness of each comparability component, which is equivalent to I(P)=V(P). Thus
  **U=I ⇔ I=V ⇔ each comparability component is upward directed**
for all Alexandrov P. This is a same-space coincidence of equalities, NOT the literal transformation under P↦P^op.

## 5. Independent closedness/fittedness conditions: dual five-point zigzags

A. Let P_A have p<t, p<x, q<t, q<y (and no other strict order), connected. Every point lies above p or q; p and q have common upper bound t. Therefore all pairs belong to V(P_A), so V(P_A)=whole square, hence closed. But closure of ↑x={x} is {p,x} and closure of ↑y={y} is {q,y}, disjoint, so (x,y)∉U. The connected U is a nonempty proper closed down-set of P_A² and cannot be fitted (otherwise it would be clopen, forcing the whole connected square). Hence V closed does NOT imply U fitted.

B. Let P_B=P_A^op; equivalently, write p<u, r<u, r<v, q<v, connected. The point r lies in cl(↑x) for EVERY x∈P_B, so U(P_B)=whole square (fitted). But minimal p,q have no common upper bound; (p,q)∉V(P_B). The fitted open V is nonempty proper on the connected square and cannot be closed. Thus U fitted does NOT imply V closed.

Neither space is almost normal, so these two examples do NOT settle the almost-normal conjecture about V closed.

## 6. Almost-normal frames: one half of the duality holds unconditionally

Previously audited theorem AN1:
  ≺ interpolates (L almost normal) ⇒ d_U=d_2=d_F, and U=V_2=F.

Therefore **U is fitted on every almost-normal frame**, without spatiality. By monotonicity of fitting,
  U fitted ⇒ V=fit(I)⊆fit(U)=U.
In particular, in an almost-normal frame,
  U=I ⇒ I=V=U=F.
The converse I=V⇒U=I fails in Claude's almost-normal two-chain example, where I=V< U.

Almost-normality ⇒ V closed remains OPEN. No universal implication U fitted ⇒ V closed exists: Example B above supplies a finite counterexample without almost-normality.

A useful exact reduction: if j_V is the fitted nucleus of V and k=j_V(0), then d_U≤k≤d_I when L almost normal. The conjecture says j_V(x)=x∨k, or equivalently F_k=F_{d_I} for supplement filters F_a={w:a∨w=1}. The statement that U is fitted alone does not force this condition.

## 7. Relation to the actual duality literature

- Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024), 108785, arXiv:2310.18522. Its published duality concerns strong Hausdorffness/F-separatedness and the diagonal; our order-zigzag identities are independent elementary calculations, and no novelty over this literature is asserted.
- Arrieta–Picado–Pultr, *A New Diagonal Separation and its Relations with the Hausdorff Property*, Appl. Categ. Struct. 30 (2022), 247–263.
- Jakl–Suarez, *Canonical extensions via fitted sublocales*, Appl. Categ. Struct. 33 (2025), article 10. On fitted sublocales/closed filters.

## 8. Further separation: the functional relation F is always fitted

This fact does not require almost-normality. For each locale map f:X→R, the kernel-pair sublocale K_f=(f×f)^{-1}(Δ_R) is fitted: Δ_R is fitted in R×R (a regular/fit locale), and inverse images of sublocales preserve arbitrary meets and carry open sublocales to opens, hence preserve fitting presentations. Intersections of fitted sublocales remain fitted. Thus

    F=⋂_{f:X→R}K_f

is CLOSED by definition and FITTED for every locale. Under almost-normality U=F, giving an independent perspective on why U is fitted (the rank-two theorem supplies the stronger identification V2=U).

In Claude Fable's almost-normal two-chain example, the previously established working theorem says Q is spatial scattered and I=V is closed. The ordinary point relation of D=fitΔ is the common-specialization-predecessor relation, which there is exactly pt(I)=Z²∪Y²∪Δ_S. Since every sublocale of the scattered spatial Q is spatial, D=I. Consequently W=cl(D)=I < U. This is a **working counterexample** to the unrestricted identity W=U, even under almost-normality; it relies on the separate still-to-be-audited exact-V calculation in A-V-Claude-almost-normal-example-exact-V-equals-I-2026-10-23.md.

## 9. Compactness restriction and research priorities

On a COMPACT locale, the established compact-first-coordinate localic tube lemma gives every canonical rectangular bar a depth≤2 separation tree (A-V-compact-coordinate-local-tube-normalization-2026-10-22.md). Hence
  L compact and almost normal ⇒ V=V_2=U=F.
This covers coherent/spectral locales: they are NOT candidates for a negative answer to (7). The finite Hochster-order-duality calculation remains useful conceptually, but cannot manufacture a counterexample to (7) inside coherent frames.

1. Pursue (7) in NONCOMPACT almost-normal frames, particularly nonalgebraic continuous frames which are not Scott spaces of continuous dcpos, and noncontinuous nonsubfit frames with nontrivial specialization behavior.
2. Investigate whether the closed counterpart W=cl(D) has a useful coordinate formula and characterize when W=U. Equality holds on all Alexandrov locales; no universal equality is asserted.
3. Keep U fitted/U=I as complementary conditions, but distinguish the literal orderdual U=D. The fact U fitted follows from almost-normality does not prove V closed.
4. Check closure/fitting absorption for Q=L⊕L without relying on ordinary points of potentially nonspatial products.
