# Project A — Explicit ideal-coproduct nucleus and pointfree normal residuals
23 October 2026. **Working theorem package; the general normal => V=U question is NOT resolved.** Builds on A-V-normal-compact-envelope-fitted-base-change-2026-10-23.md.

## 1. Canonical induced nucleus on the compact lattice coproduct

Let L be an arbitrary frame, and A its bounded distributive lattice reduct. Let
   B=A ⨿_{DLat} A
be the bounded distributive lattice coproduct. Elements t of B have representations as finite joins of pure rectangles a⊗b=ι_1(a)∧ι_2(b). Since ideal completion preserves coproducts,
   E(L)⊕E(L) ≅ Idl(B),       E(L)=Idl(A).

Let e:B→Q=L⊕L be the bounded lattice homomorphism sending a⊗b↦a⊠b. Its image JOIN-generates Q. The induced surjective frame map is
   ε:Idl(B)→Q,        ε(J)=∨_{t∈J}e(t).
The right adjoint is
   ρ(u)={t∈B:e(t)≤u},
an ideal of B. Hence the exact nucleus of the canonical inclusion X×X→Y×Y (X=L, Y=Idl(A)) is
   **j(J)={t∈B:e(t)≤∨_{s∈J}e(s)}.**
In particular the largest envelope open having precisely a specified downstairs restriction u is ρ(u).

This is explicit but not a finitary criterion: the only non-finitary term is the join in Q, whose full contents are resolved by the C-ideal calculus below.

## 2. Coordinatewise saturation computes j from A and the infinitary joins of L

For J∈Idl(B), define
  S_J={(a,b)∈L²:a⊗b∈J}.
It is a lower set, separately closed under FINITE joins in either coordinate. Let C_L(S_J) denote the least RECTANGULAR C-ideal of L² containing it (downset, separately closed under ARBITRARY joins). It can be calculated by transfinite alternation of horizontal and vertical join closures H,V: start S_0=S_J, take S_(α+1)=H(V(S_α)) (retaining S_α), take unions at limits, and stop at the first fixed stage. Equivalently allow H/V in either order at each stage; cardinality of L² bounds the stabilization stage.

The C-ideal presentation of Q gives
  **(a,b)∈C_L(S_J) ⇔ a⊠b≤ε(J)**.
Consequently
  **j(J)={ t∈B : t=∨_{i=1}^n(a_i⊗b_i), (a_i,b_i)∈C_L(S_J) for every i }.**
This is independent of the finite rectangle presentation of t.

In particular j(J) is computed by adding to a finitary ideal all finite rectangle expressions whose rectangles are forced by arbitrary horizontal/vertical joins in L. This identifies *exactly* where the compact normal envelope's finite calculus becomes infinitary on passing to L.

## 3. Normality and the still-open absorption implication

Let D_I,D_U∈Idl(B) be the ideals generated respectively by pure rectangles a⊗b with a∧b=0 and with a*∨b*=1 (pseudocomplements in L). These are exactly the separation opens d_I(Y), d_U(Y) of the compact envelope Y, as principal ideal rectangles generate any ideal rectangles. Their ε-images are d_I(X),d_U(X).

If L is normal, E(L) is compact normal and V(Y)=U(Y), so for every ideal J∈Idl(B) one has
  1_B∈J∨D_I  ⇒  1_B∈J∨D_U.             (FINITE ENVELOPE LAW)

The unrestricted normality question V(X)=U(X) is exactly the assertion that this implication remains valid after applying the specific nucleus j:
  **1_B∈j(J∨D_I) ⇒ 1_B∈j(J∨D_U)**
for every ideal J (equivalently every downstairs bar w=ε(J)).

The implication in the finite envelope is NOT by itself sufficient to prove the j-saturated implication. It is a genuine ideal-theoretic preservation problem for the nucleus in §1; the remaining difficulty is concentrated in non-finitary coordinatewise join derivations.

## 4. A pointfree necessary obstruction: every normal residual is pointless

Let L be normal and w∈Q satisfy w∨d_I=1. Put
   R_w=C(w∨d_U), a closed sublocale of Q contained in U=C(d_U).

**THEOREM.** R_w has NO points, independently of spatiality of L or Q.

Proof. If h:1→R_w were a point, its two coordinate projections give points x,y of locale X. Since h lies in U, (x,y) is Urysohn-inseparable. But h(w)=0 while δ^*(w)=1 (because δ^*(d_I)=0 and w∨d_I=1). If cl{x}∩cl{y} contained z, then (z,z)≤(x,y) in the specialization order of points of X²; the diagonal point (z,z) belongs to w, so openness of w would force (x,y)∈w: contradiction. Thus cl{x} and cl{y} are disjoint. Frame normality separates these two point-closed sublocales by neighborhoods with disjoint closures, contradicting their Urysohn-inseparability. Therefore no such point h exists.

In fact the same proof works if w is ANY open diagonal neighborhood, δ^*(w)=1, even without w∨d_I=1. In particular **pt(D)=pt(U)** for every normal locale, and the possible strictness D⊊U is invisible to points.

**Corollary.** If U is spatial as a locale, then
   **D=V=U=F**
for every normal L. This weakens the earlier sufficient assumption that the whole localic square Q is spatial: if a closed residual R_w⊆U were nonzero, then (as a closed sublocale of the spatial U) it would have a point, contradiction. Thus U⊆O(w) for every diagonal neighborhood w, proving U⊆D.

**Further localization:** If a normal frame were to refute V=U, some w bar would have nonzero R_w. Such R_w is (i) closed, (ii) pointless, (iii) contained in U, and (iv) disjoint from I, hence contained in O(d_I). This is stronger than 'ordinary points cannot witness the failure'.

## 5. Pull the hypothetical residual back to the spectral compact envelope

Take a normal L, the compact coherent normal envelope Y of §1, and its canonical dense sublocale X. For any downstairs w choose its maximal lift z=ρ(w)∈O(Y²). Then
  R_w=(X×X)∩C_Y(z∨d_U(Y))
as a pullback of closed sublocales: ε(z)=w and ε(d_U(Y))=d_U(X).

The ambient C_Y(z∨d_U(Y)) is a CLOSED sublocale of the spatial spectral U(Y), and therefore is a spatial spectral sublocale with patch-closed point set consisting of pairs of lattice-prime points related by U(Y).

If R_w is nonzero, the normal-point theorem in §4 implies the intersection with X² is NONZERO but has NO ordinary point. Thus a counterexample must involve a **nontrivial pointless pullback of an ordinary patch-closed relation in the coherent envelope**.

This description distinguishes the relevant phenomenon from the βN example, where an envelope residual may consist of free-ultrafilter pairs, but its intersection with N² is ZERO. Requiring a *nonzero* pointfree intersection is the genuinely new obstruction.

## 6. Useful no-go and agenda

The envelope law (finite ideals) does not automatically survive j-saturation; similarly a downstairs bar need not lift to an upstairs bar (e.g. the diagonal of an infinite discrete space inside βN). These facts rule out a two-line compactification proof.

Next attack: work with the explicit transfinite C_L-saturation of §2. Seek either (i) an induction principle for normal bounded lattice A that upgrades finite envelope absorption to its saturation j, or (ii) an explicit normal frame where a j-saturated ideal J reaches top with D_I but fails with D_U. It is essential that the normality of L, not just of A, be preserved when specifying the infinitary join structure.
