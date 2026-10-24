# Project A: cozero localization of normal U-residuals

23 October 2026. **Working theorem with direct sublocale proof; independent audit desirable.** Main purpose: attack the bi-dense closed-relation problem rather than recasting it. No unconditional proof/counterexample normal⇒V=U.

Notation L=O(X), Q=L⊕L, I=C(d_I), U=C(d_U), V=fit(I), D=fit(Δ), F real-function kernel equivalence. For normal L, U=F and exact closed-sublocale heredity of U follows from the localic Tietze extension theorem.

## 1. Universal cozero-square cover identity

Let {c_i} be ANY cover of 1 consisting of cozero elements; each c_i=f_i^*(R\{0}) for some locale map f_i:X→R.

**LEMMA A (all frames, no normality/spatiality):**
    1 = d_U ∨ ⋁_i(c_i⊠c_i)
in L⊕L.

Proof: U⊆F⊆K_(f_i) for every i. Let p1,p2:U→X be U's projections. Thus p1^*c_i=p2^*c_i in O(U). Hence
    (p1^*c_i)∧(p2^*c_i)=p1^*c_i.
Taking joins gives top_U because ⋁c_i=1_L. Therefore U⊆O(⋁_i c_i⊠c_i), which is equivalent to the displayed frame identity.

More generally use any cover by opens with equal pullbacks along the two projections U⇒X. In normal L, every element of the rho-fixed subframe is a join of cozero opens, so the same conclusion applies to rho-fixed-element covers. The latter structural identification is recorded separately in A-V-normal-pointfinite-buffer-and-bidense-pruning-2026-10-23.md.

## 2. Nonzero residuals localize to a cozero closure

Let L be normal and R a NONZERO CLOSED sublocale of X² with
    R⊆U(X),     R∩I(X)=0.
Put p1,p2:R→X.

For any cozero element c with p1^*c≠0, the agreement of the projections on c implies
    p1^*c=p2^*c≠0.
Thus the open sublocale
    R_c=R∩O(c⊠c)
is nonzero.

Let
    T_c=closure_X²(R_c).
Since R is CLOSED, 0≠T_c⊆R. Since R_c⊆O(c⊠c), and pure-rectangle pseudocomplements obey
    (c⊠c)*=(c*⊠1)∨(1⊠c*),
we have
    T_c⊆C(c*)×C(c*)=:Z_c².

Z_c=C(c*) is a CLOSED sublocale of the normal X, so it is normal. Localic Tietze yields EXACT closed-sublocale heredity
    U(Z_c)=(Z_c²)∩U(X).
Hence T_c is a nonzero CLOSED sublocale of U(Z_c). Functoriality of I gives I(Z_c)⊆(Z_c²)∩I(X); thus T_c∩I(Z_c)=0.

**LOCAL OBSTRUCTION THEOREM.** If there is a normal-frame counterexample R⊆U_X closed disjoint I_X, then each cozero c detected nontrivially by a projection of R produces another normal counterexample supported on the closed cozero closure C(c*).

In particular, if BOTH projections R→X are DENSE, then for **EVERY nonzero cozero c** we have p1^*c≠0 and a normal counterexample supported on Z_c. One dense projection suffices since p1^*c=p2^*c. This is much stronger than global strip-density.

Thus, in a bi-dense minimal residual, NO nonzero cozero c can have a closure Z_c belonging to ANY established positive class (compact normal, continuous normal, normal subfit, normal with spatial U, normal metacompact).

## 3. Local-to-global theorem along cozero covers

**THEOREM B.** Let L be normal and {c_i} a cozero cover of 1. Put Z_i=C(c_i*). If V(Z_i)=U(Z_i) for every i, then
    **V(X)=U(X)=F(X)**.
No assumption of spatiality, compactness, point-finiteness, or local compactness.

Proof. If V(X)≠U(X), choose bar w with w∨d_U<1. Put R=C(w∨d_U), a nonzero closed sublocale of U disjoint I. Since {c_i} covers 1, the opens p1^*c_i cover R; at least one i has p1^*c_i≠0. Apply §2 to obtain nonzero closed T_i⊆U(Z_i) disjoint I(Z_i), contradicting V(Z_i)=U(Z_i).

The statement also holds with D=U everywhere: if D(Z_i)=U(Z_i) on each closed cozero closure, then D(X)=U(X). The same argument uses a diagonal neighborhood w (not necessarily an I-bar), residual C(w∨d_U), and its disjointness from Δ_X. Under closed inclusions Δ_Z is the pullback of Δ_X, so the localized T_i contradicts D(Z_i)=U(Z_i).

The D assertion is STRICTLY stronger than the V assertion; do not infer the two properties equivalent in arbitrary normal frames.

## 4. A useful hereditary criterion

Combine Theorem B with the existing closed-sublocale pruning lemma: if every nonzero CLOSED sublocale Z of a normal X has SOME nonzero cozero element c∈O(Z) whose closure C_Z(c*) satisfies V=U, then V(X)=U(X).

Proof: a hypothetical counterexample can be pruned to a nonzero normal closed sublocale Z with a nonzero residual R whose projections are dense. Such Z must have a nonzero cozero c with good closure by hypothesis. Section 2 then constructs a nonzero closed residual within that good closure: contradiction.

This is stronger in form than requiring a cozero cover of X by good closed closures: it asks for only ONE good nonzero cozero patch in each nonzero closed quotient. The pruning reduction itself is in A-V-normal-pointfinite-buffer-and-bidense-pruning-2026-10-23.md and needs separate focused verification at limit ordinals. Treat this corollary as conditional on its accuracy.

## 5. Exact residual-map algebra

For any closed R=C(q)≤U (normal L, so U=F), the two induced frame maps f,g:L→O(R)=↑q satisfy:
- f(a)=q∨(a⊠1), g(a)=q∨(1⊠a);
- f(c)=g(c) for EVERY cozero c;
- for far a,b (a*∨b*=1), f(a)∧g(b)=0_R;
- R∩I=0 iff ⋁_{a∧b=0}f(a)∧g(b)=1_R (equivalently q∨d_I=1);
- p1,p2 dense iff for all a>0 in L, f(a)>0_R and g(a)>0_R, equivalently NO nonzero coordinate strip lies below q.

For a disjoint pair a∧b=0 and any t≺a, s≺b, one has
    f(t)∧g(b)=0_R,    f(a)∧g(s)=0_R,
because t*∨b*=1 and a*∨s*=1. Hence
    f(a)∧g(b) ≤ (f(ρ(a)))^* ∧ (g(ρ(b)))^*
in O(R).
Every disjoint-rectangle patch is orthogonal to the completely-regular cores of its two coordinate opens. A counterexample would need these singular patches to cover the WHOLE closed residual despite dense projections.

This last condition is a real restriction on the admissible frame maps, but it does NOT itself imply impossibility: in normal nonregular frames rho may vanish on large proper opens. The remaining missing step is to exploit that f,g arise from a CLOSED sublocale, not merely an open graph.

## 6. The scope and the next problem

The user's restricted dense-projection conjecture is effectively equivalent to the general normal⇒V=U question via the already recorded closed-sublocale pruning theorem. Therefore it cannot be considered an independent positive result or a reduction in logical difficulty.

The genuine new gain here is the LOCALIZATION THEOREM and its cozero-cover descent result, which forces any bi-dense residual to persist on EVERY nonzero cozero closure. A general normal locale need not have any suitable proper cozero patches (normal top-joinprime frames can have only constant real functions), so this does not settle the full conjecture.

A particularly interesting remaining case is normal frames with 1 finitely join-prime; then d_U=0 and U=F=whole, yet L may have a genuinely infinite cover by proper elements, and V=whole remains the substantive question. Every frame with join-prime top is normal automatically (a∨b=1 forces a=1 or b=1), so this is a clean test class. Infinite descending Alexandrov forks give positive examples, but the general nonalgebraic case remains open.

References: 
- Gutiérrez García, Kubiak, Picado, *Localic real functions: A general setting* (2009), and Gutiérrez García & Kubiak, *General insertion and extension theorems for localic real functions* (2011), for normal-frame Tietze.
- Picado–Pultr and Arrieta–Picado–Pultr for fitted diagonal and localic separation.
- A-V-normal-pointfinite-buffer-and-bidense-pruning-2026-10-23.md.
