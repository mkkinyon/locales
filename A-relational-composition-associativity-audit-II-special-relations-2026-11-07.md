# Project A — Associativity audit II: the special diagonal relations, and the Sierpiński-transfer family

7 November 2026. **WORKING internal theorem package**; direct frame and image calculations below; not independently externally audited. Read in conjunction with [associativity audit I](A-relational-composition-associativity-audit-I-2026-11-07.md) and the [independently refereed negative mixed-composition transfer](A-mixed-composition-external-audit-reconciliation-2026-11-07.md).

## 0. Precise question

All relations are sublocales of the SAME localic square X². Composition RS (diagrammatic order) means the image of R12∧S23↪X³ under π13. In Loc this need not associate: audit I constructs a SINGLE symmetric, reflexive endorelation Q on one X for which (QQ)Q≠Q(QQ). That general example does NOT arise as I_X=cl Δ or D_X=fit Δ, since it places edges across clopen blocks.

We seek special IDI versus I(DI), IID versus I(ID), etc., and stable specialization module actions.

## 1. Clopen coproduct blocking for diagonal hulls

For X=X1⊔X2 with clopen decomposition, the localic square decomposes into four CLOPEN blocks. The cross-block Xi×Xj, i≠j, is excluded from I_X by the disjoint open pair of clopen characteristic elements; it is excluded from D_X by the two-element clopen cover {e1,e2}. On the diagonal blocks, the restricted diagonal and its closure/fitting hulls agree with the respective I_Xi,D_Xi: the sublocale lattice splits over a finite clopen decomposition, and closure/fitting are computed componentwise. Thus

    I_X = I_X1 ⊔ I_X2,   D_X = D_X1 ⊔ D_X2

on the corresponding diagonal blocks. Their composites never jump between blocks. Therefore the one-Q arbitrary-relation nonassociativity example from audit I cannot realize I or D on that same clopen-coproduct locale. This is a STRUCTURAL difference, not a proof of associativity inside components.

## 2. Universal safe three-factor identities without association

Let A be canonical specialization-order sublocale, B=A^smile, I=cl Δ, D=fit Δ.

The direct generalized-point module identities (not using associativity) are

    A I=I=I B,      B D=D=D A.

Consequently BOTH bracketings of I B D agree:

    (I B) D=I D=I(B D).

Likewise BOTH bracketings of D A I agree:

    (D A)I=D I=D(A I).

Also both bracketings of A I B equal I, and of B D A equal D. These are tautologies from adjacent absorption; no global associativity law asserted.

If C is any closed relation and F fitted, the safe identities are (C B)F=C(B F)=C F and (F A)C=F(A C)=F C.

## 3. A base-change conservativity property

Call a locale map p:T→Y **stably surjection-conservative under pullback**, abbreviated (SC), when for every base change p_Z:T×_Y Z→Z and every surjective locale map f:E→Z, the pulled-back map

    E×_Z (T×_Y Z) → T×_Y Z

is again surjective (equivalently: its frame inverse-image is injective). The property is expressly stronger than p being a surjection or open, and is stable under arbitrary base change by definition. Every isomorphism and every open-embedding pullback satisfy (SC).

**Example (NEW):** For ANY locale Y and u∈O(Y), let S be Sierpiński with open generator σ and let

    X_u=O(u∨σ) ↪ Y×S,
    r_u:X_u→Y.

Then r_u has (SC). Proof: Banaschewski's two-coordinate frame presentation gives

    O(X_u)=M_u(L)={(a,b)∈L² : a≤u, a≤b},
    top=(u,1).

For any surj f:E→Y, f*:L→O(E) is injective. The pullback E×_Y X_u is X_(f*u) over E with frame

    M_(f*u)(O(E)) = {(α,β):α≤f*u, α≤β}.

The frame inverse image of the pullback projection is the COMPONENTWISE map

    M_u(L)→M_(f*u)(O(E)), (a,b)↦(f*a,f*b),

which is injective, because f* is. This proves pullback preserves surjectivity. Every base change of r_u along g:Z→Y is again of this exact form X_(g*u)→Z, so the argument proves the full (SC) condition.

**Careful distinction:** an arbitrary surjective locale map need not be pullback-stable; (SC) is a property of the MAP along which one pulls surjections, not a claim about surjections themselves.

## 4. Outer-relation associativity criterion

For composable relations R⊆A×B, S⊆B×C, T⊆C×D, let

    P=R×_B S×_C T,
    F=im(P→A×D)

be the honest four-coordinate path image. There are canonical inclusions

    F≤(RS)T,   F≤R(ST).

**Lemma (NEW).**
(a) If the FIRST projection t1:T→C has property (SC), then (RS)T=F.
(b) If the SECOND projection r2:R→B has property (SC), then R(ST)=F.

Proof of (a): the map e:R×_B S→RS is surjective by image factorization. The projection (RS)×_C T→RS is a base change of t1:T→C and therefore has (SC). Pulling e back along it gives a surjection

    P= (R×_B S)×_C T →(RS)×_C T.

Composing a map with a surjection does not alter its locale-theoretic image (on frames, injectivity of the surjection's inverse image ensures equal kernel congruences). Hence im(P→A×D)=im((RS)×_C T→A×D)=(RS)T. The proof of (b) is the same with the opposite bracketing.

**Corollary (general category-style statement in Loc).** Let K=ker(r:X→Y) be the kernel pair of any (SC) map r. Both projections K→X are base changes of r and thus have (SC). For EVERY relation S⊆X²,

    **(K S)K=K(S K)**,

and both are the honest four-path image of K12∧S23∧K34. This does NOT assume S closed/fitted or X coherent/compact.

Since K²=K (kernel pair is reflexive and transitive via the universal triple), the same condition also gives

    **(K K)S=K(K S)=K S**,
    **S(K K)=(S K)K=S K**,

for every S. The honest triple image of K K S equals KS: one inclusion by K²≤K, reverse by insertion of a diagonal K edge. Analogous for S K K.

## 5. Application to the NEGATIVE mixed-V example X_u

If Y is strongly Hausdorff, the externally refereed one-generator calculation says

    I_(X_u)=K=ker(r_u),
    D_(X_u)=V_(X_u)=fit(K),

where D can be nontransitive (indeed choose Arrieta's spatial sH/non-Fsep base and u detecting the defect). By §§3–4, for EVERY relation S on X_u,

    **(I S)I = I(S I).**

In particular

    **(I D)I = I(D I)**.

So the very spatial locale exhibiting I D⊄V and D²⊄D does NOT refute the three-factor associativity target IDI. This is a NONTRIVIAL POSITIVE RESULT for a noncoherent, noncompact, non-F-separated example.

Among the eight length-three words in I,D on this specific family, four are confirmed associative:

    III, IID, IDI, DII.

The proofs: III follows from K²=K; IID and DII from (K K)S=K(K S) and S(K K)=(S K)K; IDI from (K S)K=K(S K). The remaining words IDD, DID, DDI, DDD are **not settled** by this calculation. By symmetry/converse, associativity for IDD and DDI are equivalent; for DID and DDD it is equivalent to symmetry of the corresponding left-bracketed triple.

## 6. A salvaged HALF of the arbitrary-locale distributor calculation in the transfer family

The original all-locale claim A(I D)=I D=(I D)A was based on illicit general reassociation. In the transfer locale X_u, K=I is reflexive/transitive and has (SC) projections, so

    K(K S)=K S,   (S K)K=S K

for every S (from §4). Since Δ≤A≤K, monotonicity gives

    **A(I D)=I D**,
    **(D I)A=D I**.

These are direct, genuinely localic SATURATION identities without needing A itself to have (SC) projections.

We do **not** obtain the other two equations (I D)A=I D or A(D I)=D I from this argument; they remain to be separately tested. Nor does this prove A(I D)=I D for arbitrary X.

## 7. Safe regions and current frontier

Confirmed from prior audit I:
- for coherent X, patch-closed spectral relations associate (including A,B,I,D);
- for compact X, CLOSED relations associate (including all powers of I);
- if I=Δ (strong Hausdorff), EVERY length-three word involving at least one I associates trivially by the unit law, but DDD still needs checking. Dually if D=Δ (F-separated), every word involving D associates, but III may remain ambiguous. These cases must not be conflated with general associativity of the one surviving nontrivial relation.

Genuine unresolved directions:
- arbitrary X: (I D)I ?= I(D I);
- arbitrary X: (I I)D ?= I(I D);
- negative transfer X_u: IDD, DID, DDD (with D fitted and nontransitive) may provide a sharper counterexample to associativity;
- all-locale distributor saturation A(I D), (I D)A, and least A-saturated hull.

No assertion that nontransitivity D²⊄D entails nonassociativity of D³. No priority claims.

## 8. Distinctness of SC from properness, and the residual distributor question

Take the sH/non-Fsep base Y and u given by Arrieta's published spatial existence theorem and the independent mixed-composition audit. For X_u, the projection r_u is (SC) by the two-coordinate proof. However its kernel-pair projections K→X_u CANNOT be proper, since the previously proved proper-projection lemma would then give K∘D≤fit(K)=D, contradicting the independently refereed counterexample. Because properness is stable under pullback, r_u is itself NOT proper. Thus (SC) is a genuine route to restricted associativity beyond properness.

For S=D, §4 proves K(K D)=K D and (D K)K=D K. The specialization-order relation A satisfies Δ≤A≤K, so A(K D)=K D and (D K)A=D K. But these facts do NOT yield (K D)A=K D or A(D K)=D K; passage of A through an intermediate image remains subject to surjective-image base-change behavior. The original all-locale distributor claim should therefore stay UNPROVED, with only the indicated half-actions established for X_u.

## 9. Literal associativity tests by symmetry

For symmetric I,D, converse of a binary localic composite reverses factors, no associativity needed:

    ((I D) I)^smile = I (D I).

Thus the special associativity assertion (I D) I=I(D I) is EQUIVALENT to symmetry of the left-bracketed relation (I D) I. Similarly (D I) D and D(I D) are converses, as are (D D) D and D(D D). A genuine failure in any of these triple words would require an asymmetric *localic image after one intermediate image*, not an ordinary four-point zigzag (the honest four-path image is symmetric under reversal).

This reduction is useful for adversarial checking: proof of reflexivity/symmetry of the factors alone cannot establish symmetry of a bracketed 3-fold composite (audit I's one-Q counterexample is exactly of this type).
