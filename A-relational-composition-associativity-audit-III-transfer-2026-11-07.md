# Project A — Associativity audit III: all three-letter I/D words except DDD associate in the transfer locale

**7 November 2026. WORKING internal mathematical proof, not independently externally audited.** Continues [audit II](A-relational-composition-associativity-audit-II-special-relations-2026-11-07.md) and the [independently refereed transfer theorem](A-mixed-composition-external-audit-reconciliation-2026-11-07.md).

## 1. Setup and an open idempotent ceiling map

Take ANY strongly Hausdorff locale Y with L=O(Y), any u∈L, and X=X_u=O(u∨σ)⊆Y×S, S=Sierpiński. Let r:X→Y be projection, s:Y→X its high-layer section, and c=s∘r:X→X. At the frame level

    M=O(X)={(a,b)∈L²:a≤u,a≤b}, top=(u,1);
    r*:L→M, a↦(a∧u,a);
    s*:M→L, (a,b)↦b;
    c*=r*∘s*, (a,b)↦(b∧u,b).

The left adjoint to r* is r_!(a,b)=b, satisfying Frobenius:
r_!(m∧r*(v))=r_!(m)∧v. Hence r is an OPEN locale map. The section s is the open embedding corresponding to the high Sierpiński layer σ=1 (O(σ)≅Y), so c=s r is OPEN, and c²=c. On ALL generalized points x:T→X, x≤c(x), since for each (a,b)∈M,

    x*(a,b)≤x*(b∧u,b)=x*c*(a,b).

Let K=X×_Y X; the independent transfer audit proves K=I_X, and D_X=fit K. On K, c(x)=c(y); and x K c(x) follows from r c=r. The projections of K are base changes of the OPEN map r, hence OPEN. Open maps preserve images under pullback (equivalently their base changes reflect locale surjections); this can also be proved directly from the componentwise frame presentation as in audit II, §3.

In this note F denotes an ARBITRARY FITTED relation in X²; ultimately put F=D_X. “Fitted” means intersection of open sublocales, so F is upward in BOTH generalized-point coordinates (monotonicity of opens), and preimages of F along locale maps remain fitted.

## 2. Exact K action on arbitrary fitted relations

**LEMMA.** For any fitted F⊆X²,

    **K∘F=(c×id)^-1 F,    F∘K=(id×c)^-1 F**.

Proof: On the generic composable-pair locale for K12∧F23, xKy and yFz. Then c x=c y and y≤c y. Upward specialization-stability of F gives F(c x,z). Therefore image(KF)≤(c×id)^-1 F. Conversely on the generic point of (c×id)^-1 F, the pair x K c x F z provides a lift to the composable-pair locale, proving reverse inclusion. The second equation is symmetric. These are sublocale/image equalities, not inferences from ordinary points.

**Consequences:** KF and FK are FITTED, since pullbacks of fitted relations are fitted. If F=D, R=I D and R'=D I are fitted despite the independently refereed strict R⊄V=D. Indeed D≤ID by reflexivity of I, so D<ID and R is a genuinely LARGER fitted relation than D in the selected negative-transfer example.

## 3. Middle insertion: both D I D bracketings equal D²

**THEOREM.** For any fitted F on X,

    **(F∘K)∘F=F∘(K∘F)=F∘F**.

Proof of first: use FK=(id×c)^-1 F from §2. On its composable-pair source with F, the generalized triple satisfies F(x,c y),F(y,z). Because y≤c y and F fitted, F(c y,z). Thus the triple directly supplies a witness for F² via middle c y, giving (FK)F≤F². Conversely F≤FK (K reflexive), so F²≤(FK)F. For second: the source of F(KF) is F(x,y),F(c y,z); since y≤cy, F(x,c y), giving a direct F² witness. Conversely F≤KF so F²≤F(KF). No image base-change theorem or associativity is used here.

Specialize F=D to obtain (D I)D=D(I D)=D²; this holds even though D²⊄D in the negative-transfer example. Inserting the K=I factor between two fitted relations has no effect on their two-step composite.

## 4. Outer insertion: I D D associates

**THEOREM.** For any fitted F on X,

    **(K F)F = K(F F) = (c×id)^-1(F F)**.

Proof of left equality with pullback: by §2, KF=(c×id)^-1F, so its composable-pair source with F is the pullback along the OPEN map c×id of E_FF=F12∧F23→X². Since open maps preserve images under pullback, its image is (c×id)^-1(F F).

For the other bracketing: the second projection K→X is OPEN; hence in K(F F), the intermediate surjection E_FF→FF stays surjective under the relevant pullback. Thus K(F F) is the endpoint image of the HONEST path source

    P={(x,y,m,z):xKy, yFm, mFz}.

Compare with the pullback path source

    Q={(x,m,z):F(c x,m),F(m,z)}.

Every generalized point of P maps to Q by forgetting y: since xKy, c x=c y and y≤c y, hence F(c x,m). Conversely a Q-point maps to P by choosing y=c x. These maps preserve endpoints and show the endpoint IMAGES coincide. Therefore K(F F)=im Q=(c×id)^-1(F F), as claimed.

By converse:

    **(F F)K = F(F K) = (id×c)^-1(F F)**.

For F=D, this establishes IDD and DDI associativity in the transfer family.

## 5. Seven of eight length-three words now associate

For Y strongly Hausdorff and X=X_u, I=K and F=D. Independent audit II gave associativity of III, IID, IDI, DII by open kernel-pair projections and K²=K. §§3–4 give DID, IDD and DDI.

    III yes
    IID yes
    IDI yes
    IDD yes
    DII yes
    DID yes, both bracketings equal D²
    DDI yes
    DDD UNRESOLVED.

The same true for the spatial negative-transfer X_u built from Arrieta's spatial sH/not-Fsep Y. Nontransitivity D²⊄D there DOES NOT imply nonassociativity DDD. Nothing here settles DDD.

## 6. Entire order-distributor claim restored in the transfer family

Assume Y is strongly Hausdorff so that A⊆K, with A the canonical specialization-order sublocale and B=A^smile. Every x has x A c x, since x≤cx. For fitted F,

    **A F=K F**:

one inclusion A≤K is trivial; for xKy Fz, x A c x Fz by §2, hence the reverse inclusion. Dually F B=F K.

In particular, I D=A D=(c×id)^-1D and D I=D B=(id×c)^-1D, BOTH fitted.

Put R=I D. Because R is fitted, R A=R (the direct fitted-module identity). Also A R=R: if x A y and R(y,z) means D(c y,z), then r x=r y (A≤K), so c x=c y and R(x,z). Reflexivity of A gives reverse inclusion. Thus

    **A R=R=R A**.

By converse, with R'=D I,

    **B R'=R'=R' B**.

Moreover I≤D in this family, hence J=I∨D=D. Directly D A=D (fitted-module law). Hence BOTH parentheses of the least-distributor expression agree:

    **(A J)A=A(J A)=A D=I D**.

Any A-left-and-right saturated relation S with J≤S contains A J=I D, so I D really IS the least A-A distributor containing J in the transfer family. This restores ALL distributor equations here that were left unproved in arbitrary locales after the associativity warning; it does not establish them for arbitrary X.

## 7. Abstract formulation, scope, and corrections

The key mechanisms work in any locale X equipped with an **OPEN, IDEMPOTENT, SPECIALIZATION-INFLATIONARY** endomap c:X→X, where K=ker c. Then the exact K/F formulas (§2), fitted middle insertion (§3), and open-pullback outer associativity (§4) apply to arbitrary fitted F. (Since c open, kernel projections are open as its pullbacks; c²=c gives xKcx.) This cleanly isolates the categorical mechanism, independent of the Sierpiński frame presentation.

For the actual transfer family, the open endomap c=s r is explicit. Notice that r is OPEN by the simple Frobenius calculation; audit II had used a more elaborate "surjection-conservativity" property to prove stable-image behavior, but here an ordinary standard open-locale-map hypothesis suffices.

The abstract theorem does NOT say arbitrary I_X equals ker(c), or that D_X is always fitted under some general relational image operation. It is a restricted result for a K-like factor and a fitted F.

**Remaining investigation:** DDD on X_u; arbitrary-X associativity of IDI/IID/IDD; arbitrary-X full A-distributor. Priority and external correctness audit for §§2–6 remain open.

Proof-audit checks: justify open-map image base change; verify left adjoint r_!(a,b)=b and Frobenius on M; check c²=c and x≤cx at the frame level; use the GENERIC POINT of each composable-pair sublocale rather than ordinary points; keep parenthesization explicit until equality is established.

## 8. Exact table of all three-letter words except FFF

In the abstract setting of §7 (open inflationary idempotent c, K=ker c, F fitted), write c1=c×id and c2=id×c. Both parenthesizations have identical results:

    KKK = K,
    KKF = c1^-1 F,
    KFK = (c×c)^-1 F,
    KFF = c1^-1(F²),
    FKK = c2^-1 F,
    FKF = F²,
    FFK = c2^-1(F²),
    FFF = UNDECIDED.

The new formula KFK=(c×c)^-1 F follows directly: in the source for (KF)K, one has F(c x,y), yKz. Since y≤c y=c z, fittedness gives F(c x,c z); conversely if F(c x,c z), choose y=c z. The alternative bracketing follows by symmetry. This gives a useful all-case normal form: only the genuinely self-composed fitted relation F³ might be nonassociative in such a locale.

## 9. Reduction of F² to high-intermediate witnesses

Let c=s r:X_u→X_u and F fitted (no extra assumption). Let E_FF⊆X³ be the composable-pair source, with generalized triple x F y F z. As y≤c y and F upward in both coordinates, such a triple yields x F c y F z. Conversely, every x F c y F z is already a valid F² witness using middle c y. Therefore **F² is the localic image of the high-intermediate source**

    H₂={(x,t,z)∈X×Y×X: x F s(t), s(t) F z}

under projection to (x,z).

For F=D_X, its restriction along s×s:Y²→X² is EXACTLY D_Y:
- D_Y≤(s×s)^-1(D_X) by preservation of fitted-diagonal relation under ANY locale map;
- reverse: for every cover C of O(Y), its image {r*(a):a∈C} is a cover of O(X), so a pair of high points in D_X satisfies the C test after applying s*, hence lies in D_Y.

Consequently, the HONEST four-coordinate witness image for D³ can be computed from two Y-valued high intermediates:

    {(x,t,v,z): x D_X s(t),   t D_Y v,   s(v) D_X z} ⊆ X×Y²×X.

Every honest D³ chain x D y D m D z upgrades both middle points to c y,c m; conversely every displayed path yields a D³ chain using s(t),s(v). The two bracketings of DDD each CONTAIN this honest endpoint image, but may contain more if the intermediate D²-image surjection becomes non-surjective under the next pullback. Thus this reduction is an exact normal form for the honest path image, NOT a proof that DDD associates.

This isolates the remaining obstruction to how images of the high-intermediate D_Y paths behave under base change along the X-to-Y mixed fitted slices. There is no obvious implication from D_Y non-F-separatedness to DDD nonassociativity.
