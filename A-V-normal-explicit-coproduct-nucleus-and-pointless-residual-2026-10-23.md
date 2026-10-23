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

**PRECISE POINT/CLOSURE LEMMA (works even if L is not spatial).** Given ordinary locale points x,y:L→2, let p_x=∨{a∈L:x(a)=0} and p_y likewise. These are the largest opens missing x,y, and C(p_x),C(p_y) are the **localic** point closures. For ANY open w∈Q with δ*(w)=1 and (x,y)(w)=0, represent w=∨_i a_i⊠b_i. Each a_i∧b_i≤p_x∨p_y: since x(a_i)∧y(b_i)=0, either a_i≤p_x or b_i≤p_y. But ∨_i(a_i∧b_i)=δ*w=1, so p_x∨p_y=1. Conversely if p_x∨p_y=1, the open (p_x⊠1)∨(1⊠p_y) is a diagonal neighborhood excluding (x,y). Therefore:
  (x,y)∈pt(D) iff p_x∨p_y<1,
equivalently the LOCALIC closed point closures meet nontrivially. Do not replace this by intersection of their ordinary point sets on nonspatial L: their intersection could be nonzero and pointless.

**THEOREM.** For normal L, R_w has NO points, independently of spatiality of L or Q.

Proof. If h:1→R_w is a point, it gives points x,y∈pt(X). Since h(w)=0 and δ*w=1, the precise lemma above gives p_x∨p_y=1 in L. Normality of L provides c,d∈L with
  p_x∨c=1=p_y∨d,    c∧d=0.
Then x(c)=1=y(d), because x(p_x)=0 and y(p_y)=0. Moreover normality allows shrinking to c',d' neighborhoods of x,y whose **closures** are disjoint: apply the normal shrinking lemma to the disjoint closed sublocales C(p_x),C(p_y), or apply pointfree Urysohn's lemma for p_x∨p_y=1 to obtain a real map separating x and y. Hence (x,y)∉U=C(d_U), contradiction. This proves that R_w has no ordinary points.

The same argument gives pt(D)=pt(U) for every normal frame: U⊆O(w) on all ordinary points for each open diagonal neighborhood w, and D⊆U universally.

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

## 6. Prime-spectrum location of a hypothetical counterexample

Let L normal, and let J∈Idl(B) witness
  1_B∈j(J∨D_I),   1_B∉j(J∨D_U).
The latter j-saturated ideal is proper, hence extends to a prime ideal P of the bounded distributive lattice B (classical prime ideal theorem). By the bounded-distributive-lattice coproduct duality, P is a pair (ξ,η) of lattice-prime points of Y=Spec(A). Since D_U≤j(J∨D_U), this pair belongs to U(Y), and the maximal envelope open ρ(w∨d_U) misses it. If BOTH ξ and η were completely prime for the arbitrary joins of L, they would come from ordinary points of X and hence yield a point of the residual R_w. Section 4 excludes that. Thus at least one coordinate is a finitely prime but NOT completely prime filter of the frame L.

This does not by itself produce a counterexample: for discrete N⊆βN there are abundant such boundary prime pairs, yet every associated residual downstairs is zero. The extra task is to arrange a nonzero POINTLESS pullback from the compact spectral support.

## 7. Useful no-go and agenda

The envelope law (finite ideals) does not automatically survive j-saturation; similarly a downstairs bar need not lift to an upstairs bar (e.g. the diagonal of an infinite discrete space inside βN). These facts rule out a two-line compactification proof.

Next attack: work with the explicit transfinite C_L-saturation of §2. Seek either (i) an induction principle for normal bounded lattice A that upgrades finite envelope absorption to its saturation j, or (ii) an explicit normal frame where a j-saturated ideal J reaches top with D_I but fails with D_U. It is essential that the normality of L, not just of A, be preserved when specifying the infinitary join structure.
