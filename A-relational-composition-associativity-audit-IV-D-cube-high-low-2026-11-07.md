# Project A — Associativity audit IV: exact high/low fitted diagonal, high-layer cube reduction, anti-Urysohn density

7 November 2026. **WORKING MATHEMATICAL SEGMENT; NOT EXTERNALLY AUDITED.** The desired yes/no statement for D_X^3 on the Arrieta–Banaschewski transfer X_u is STILL OPEN. Results here are strict sublocale equalities with categorical image qualifications, not an ordinary-point heuristic. Continues [associativity audit III](A-relational-composition-associativity-audit-III-transfer-2026-11-07.md) and relies for the input space on Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024), 108785, Example 4.5, Proposition 4.9, Corollary 4.10. Open-access publisher PDF at https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf .

## 1. Setup

Let Y be a strongly Hausdorff locale, L=O(Y), u∈L, U=O(u)⊆Y. Let X=X_u=O(u∨σ)⊆Y×S (σ nontrivial open of Sierpiński). Let r:X→Y, s:Y→X upper-layer section and c=s∘r:X→X. From audit III, c is OPEN idempotent, inflationary for localic specialization: x≤c x on all generalized points. Put

    F=D_X=fit Δ_X, G=D_Y, G_U=D_U.

Let H=O(σ)≅Y upper OPEN, and N=C(σ)≅U lower CLOSED. They are complementary sublocales, H∧N=0, H∨N=X. Hence their four coordinate blocks H×H, N×H, H×N, N×N join X²; finite distributivity of the lattice of sublocales permits testing equality of SUBLOCALES by their four restrictions.

**Important:** Neither N↪X nor mixed blocks with N are OPEN. Pullback of an arbitrary relational IMAGE along these embeddings need not preserve that image. Thus do not infer a matrix formula for F² or F³ merely by composing entries of the matrix in §2.

## 2. EXACT four-block formula for the *original fitted diagonal* F

**Theorem (all Y; no sH needed).** Pull back F=D_X along the four layer embeddings; one has:

     target low (U)    target high (Y)
source low  (U):   D_U        D_U [supported on U×U⊆U×Y]
source high (Y):   D_U        D_Y

For a mixed block, D_U is regarded as its image along U×U↪U×Y or Y×U.

**Proof via all frame covers.** O(X)=M_u(L)={(a,b)∈L²:a≤u,a≤b}, top=(u,1). A family {(a_i,b_i)} covers top iff ∨a_i=u and ∨b_i=1. For both points high (σ=1), each open evaluates as b_i, and the diagonal-cover test is exactly D_Y; every Y-cover lifts via η(b)=(b∧u,b). For both low (σ=0), each evaluates a_i, yielding exactly the D_U cover tests, since any U-cover {a_i≤u} extends to M-cover {(a_i,a_i)}∪{σ=(0,1)}.

For low first and high second, the X-cover {σ,η(u)} forces high coordinate's base u=1. For any U-cover {a_i} with join u, the X-cover {(a_i,a_i)}∪{σ} gives ∨ a_i(y)∧a_i(z)=1, hence the pair lies in D_U inside U×U. Conversely, if in D_U, for every X-cover, ∨ a_i(y)∧b_i(z)≥∨ a_i(y)∧a_i(z)=1 because a_i≤b_i. The high-low case is symmetric.

All tests are conducted on universal generalized points of the sliced relation, so they are equalities of localic SUBLOCALES, not merely point sets.

## 3. HIGH-LAYER RESTRICTION COMMUTES WITH COMPOSITION FOR c-STABLE RELATIONS

**Definition.** A relation R⊆X² is *c-upward-stable* if image((c×id)|R)≤R and image((id×c)|R)≤R. This is a property of genuine locale maps, not the (possibly unproved) abstract all-specialization distributor property A R=R=R A.

(i) Any FITTED R is c-upward-stable, because open predicates are monotone under x≤cx on arbitrary generalized points.

(ii) If R,S are c-upward-stable, then R∘S is c-upward-stable. Proof: on the actual composable-pair source E=R12∧S23, replacing an ENDPOINT by c preserves R,S. The endpoint map from E factors through R∘S; since E→R∘S is surjective, its image under the endpoint-c map is contained in R∘S. This is a direct image-factorization argument — do NOT infer it by lifting a generalized point of the image along an arbitrary map.

(iii) **HIGH-LAYER COMPOSITION LEMMA**: for any c-upward-stable R,S,

    (R∘S)|_(H×H) = (R|_(H×H)) ∘ (S|_(H×H)).

Proof: H×H↪X² is OPEN, so restricting the localic endpoint image along H×H commutes with image formation. On the resulting genuine composable-pair source with HIGH endpoints, replace the arbitrary middle generalized point y by cy∈H. c-stability of R in second coordinate and of S in first coordinate makes it a valid all-high path with same endpoints. Conversely every all-high path was a valid original path. These endpoint-preserving maps show the images agree.

Because R∘S is c-stable by (ii), this lemma iterates over ANY finite parenthesized word of fitted relations, even when the intermediate composite is NOT itself known to be fitted.

**Corollary:** For F=D_X, G=D_Y, and any parenthesization π of n≥1 copies,

    π(F,...,F)|_(H×H)=π(G,...,G).

In particular,

    ((F F)F)|_(H×H)=(G G)G,
    (F(F F))|_(H×H)=G(G G).

Therefore **if D_Y³ is nonassociative then D_X³ is nonassociative**. If D_Y³ is associative, the transfer problem MAY STILL fail in a block involving the closed lower layer; the converse is not claimed.

## 4. Why we cannot compose the four-block matrix naively

The block formula in §2 determines F itself because sublocale meets distribute over the finite block join. For F², computing the (low, high) restriction involves pulling an IMAGE along the CLOSED low endpoint N↪X. Such pullbacks need not preserve locale-surjections, which is precisely the mechanism behind nonassociativity (audit I).

Thus the seemingly natural formal matrix formula

    (F²)_(low,high)  ?= D_U∘D_Y

has NOT been justified, and MUST NOT be used without a new base-change proof. The high-high block is exceptional because H×H is OPEN and the upgrade y↦cy is available, yielding (F²)_(high,high)=D_Y² rigorously.

This is a structural localization of all remaining failure: once D_Y³ associates, an associativity defect in X can only occur in a lower-layer-involving block and must be caused by an intermediate image/sublocale pullback that is not stable across the CLOSED low embedding.

## 5. The actual ARRIETA base is anti-Urysohn; D_Y dense

Arrieta's published construction [Example 4.5 + Corollary 4.10] gives a SPATIAL, strongly Hausdorff, anti-Urysohn locale Y that is not F-separated. Here anti-Urysohn means that the closures of ANY two nonempty open subsets of the underlying space meet. Equivalently, for all nonzero a,b∈O(Y), a*∨b*≠1 (Arrieta Definition 4.6).

**Proposition (working):** For a spatial anti-Urysohn locale Y, EVERY open neighborhood w∈O(Y²) of Δ_Y is DENSE in Y².

Proof: Write w=∨_i v_i⊠t_i with δ*w=∨_i(v_i∧t_i)=1. Take arbitrary nonzero base rectangle a⊠b. Anti-Urysohn supplies an ordinary point p∈cl(a)∩cl(b). Choose i with p∈v_i∩t_i. Then a∧v_i and b∧t_i are nonzero, so (a⊠b)∧w contains the nonzero rectangle (a∧v_i)⊠(b∧t_i). Rectangles form a join-dense base of the product frame, so w is dense.

The Booleanization B(Y²) is contained in EVERY dense open sublocale. Therefore B(Y²)≤fit Δ_Y=D_Y, so D_Y is itself DENSE. Consequently,

    **W_Y=cl(D_Y)=Y².**

Also, since no nonzero pair a,b is far, the localic Urysohn relation has no nonzero excluded far rectangle:

    **U_Y=Y²**.

Thus in Arrieta's sH anti-Urysohn base, I_Y=Δ_Y but D_Y is a PROPER, DENSE fitted relation, while W_Y=U_Y=Y². The properness of D_Y follows from the published non-Fsep result and the presence of some proper open Δ-neighborhood (e.g. u⊠u* witness).

**Corollary for transfer X_u:** Its upper layer H≅Y is OPEN and DENSE: a nonzero M_u(L) element (a,b) has b≠0 and therefore meets σ. Since Y is anti-Urysohn, any two nonempty opens of X intersect H in nonempty opens whose closures meet, so X itself is anti-Urysohn (as a spatial locale). Hence

    **W_X=U_X=X²**.

Together with independently audited I_X=K and D_X=V_X, the transfer example's major hierarchy levels satisfy

    K=I_X ≤ D_X=V_X < W_X=U_X=X².

The strict D_X<W_X follows because D_X≤O(w) for an explicit proper diagonal neighborhood w used in the independently audited mixed-V counterexample.

The density calculation describes the background but **does not decide whether D_Y³ or D_X³ associates**: dense localic relations need not have surjective composition images.

## 6. The honest high-intermediate D³ path and the precise issue

From audit III, F² is the image of high-middle triples

    H2={(x,t,z): x F s(t), s(t) F z}⊆X×Y×X.

The honest D³ path image is the image of

    H3={(x,t,v,z): x F s(t), t G v, s(v) F z}⊆X×Y²×X.

Indeed middle points can be upgraded to c(middle) using fittedness; conversely the high-middle paths are actual F paths. Both bracketings of F³ CONTAIN im(H3→X²), but potentially exceed it because the intermediate image-surjection H2→F² is not known stable when pulled back along the appropriate projection of F. If both those pullbacks preserve surjectivity, then both bracketings equal the honest image and F³ associates.

The four-layer formula gives the relation data entering H3; the remaining difficulty is a precise IMAGE STABILITY problem, not an ordinary pointwise zigzag issue.

## 7. Status and next choice

**Established here as WORKING statements:** exact D_X four-block description; high-high restriction of any parenthesized D_X word = corresponding D_Y word; density of D_Y and D_X, and W=U=top in Arrieta's anti-Urysohn setting. **NOT resolved:** D_Y³ association; D_X³ association; arbitrary-X I/D associativity; whether source image H2→F² remains surjective under F projections. The earlier seven-of-eight associativity theorem for X_u remains unaffected.

Recommended next test: seek a characterization of surjection stability for the particular H2→F² map using the F cover formula and/or identify an explicit nonzero residual E from the published anti-Urysohn base. No implication from nontransitivity F²⊄F to nonassociativity is asserted. External adversarial audit recommended before extending categorical conclusions.
