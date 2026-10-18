# A — Three closed localic separation relations: first results

**Research note, 18 October 2026. Status:** proofs below are working mathematical arguments, intended for subsequent critical checking; no claim of priority or novelty. Source of the original five point-based graphs: P. J. Cameron and V. Kumar, *Graphs on topological spaces*, [arXiv:2610.14783](https://arxiv.org/abs/2610.14783). Background: Picado–Pultr (2021), *Separation in Point-Free Topology*, especially Chapter III §5 and Chapters IV, VI, VIII; Arrieta–Picado–Pultr (2022), [preprint](https://www.mat.uc.pt/preprints/ps/p2117.pdf).

## 1. Set-up: closed sublocales, not point sets

For a locale X, write L = O(X), and Q = O(X×X) = L⊗L (coproduct of frames). Basic rectangles are a⊠b. Write C(d) for the closed sublocale complementary to the open sublocale d∈Q; d≤e implies C(e)⊆C(d). The diagonal δ:X→X×X has δ*(a⊠b)=a∧b. Pseudocomplement is a*=a→0.

Define the *separation opens*:

    d_I = ⋁ {a⊠b : a∧b=0},
    d_U = ⋁ {a⊠b : a*∨b*=1}.

The corresponding localic relations are

    I(X) = C(d_I),        U(X) = C(d_U).

For every localic real-valued map f:X→R let K_f be the kernel pair, that is, the inverse image of the diagonal of R under (f×f). Put

    F(X) = ⋂_{f:X→R} K_f.

All three are **closed** sublocales of X×X. They are reflexive and symmetric; F is also an equivalence relation as the kernel pair of the product evaluation map X→R^{Hom(X,R)}. I and U need not be transitive.

Important nomenclature: do **not** call F(X) an “F-separated” condition! In Arrieta–Picado–Pultr (2022), (Fsep) means that the diagonal is **fitted** (intersection of open sublocales), a different concept.

For an ordinary space (on the ordinary pairs of points, with the usual qualifications about localic products), these give the diagonal-inclusive inseparability, Urysohn, and functional graph relations of Cameron–Kumar. The relation I(X) is **exactly the closure of the diagonal**. The condition I(X)=Δ_X is therefore Isbell's established strongly Hausdorff axiom (sH); see Picado–Pultr III.5.1–5.3, pp. 49–50. This condition is stronger than the conservative frame Hausdorff axiom (H), and (sH) need not hold for a classical Hausdorff space: loc. cit. III.6, IV.3.

## 2. Proposition: the hierarchy, entirely point-free

**Proposition 1 (working proof).** For every locale X,

    Δ_X ⊆ I(X) ⊆ U(X) ⊆ F(X).

**Proof.** For a,b∈L, if a*∨b*=1, distributivity gives
a∧b = (a∧b∧a*)∨(a∧b∧b*) = 0.
Therefore d_U≤d_I and hence I⊆U. Because δ*(d_I)=0, the diagonal factors through C(d_I), so Δ⊆I.

For the last inclusion, first recall that the off-diagonal of the ordinary (and localic) real line is the open

    (R×R)\Δ_R
      = ⋁_{r<s ∈ Q} [
             (-∞,r)⊠(s,∞)  ∨  (s,∞)⊠(-∞,r)
        ].

Let A=(-∞,r), B=(s,∞), r<s. In O(R), A*∨B*=1. For any frame homomorphism h, h(A*)≤h(A)*, so for a localic map f:X→R, (f*A)*∨(f*B)*=1. Every rectangle occurring in the pullback (f×f)*((R×R)\Δ_R) consequently occurs among the generators of d_U. Thus

    (f×f)*((R×R)\Δ_R) ≤ d_U,

so C(d_U)⊆K_f. Intersect over f to obtain U⊆F. Finally Δ⊆F because each K_f contains Δ. □

Here f* in formulas denotes the inverse-image frame homomorphism f^*, not a pseudocomplement.

**Useful explicit separation open for the functional relation:**

    d_F = ⋁_{f:X→R} ⋁_{r<s ∈ Q} [
        f^*((-∞,r))⊠f^*((s,∞))
        ∨ f^*((s,∞))⊠f^*((-∞,r))
    ].

Then F(X)=C(d_F), and the hierarchy is equivalent to d_F≤d_U≤d_I. This makes the entire construction frame-theoretic.

## 3. Proposition: preservation under arbitrary locale morphisms

**Proposition 2 (working proof).** For any localic map h:X→Y and R ∈ {I,U,F},

    R(X) ⊆ (h×h)^{-1}(R(Y)).

**Proof.** Equivalently (h×h)^*(d_R(Y))≤d_R(X). For I, h^* preserves zero meets. For U, if a*∨b*=1 in O(Y), then (h^*a)*∨(h^*b)*=1 in O(X) because h^*a*≤(h^*a)* and h^* preserves 1 and joins. For F, each real-valued map g:Y→R gives the map g∘h:X→R, and its off-diagonal generators are included in the join defining d_F(X). □

**Caution:** this is an inclusion, not an equality assertion; preservation under continuous maps is weaker than a formula for products.

## 4. A finite space with both strict inclusions

Let P be the seven-element poset with minimal elements a1,a2,a3,a4 and maximal elements b1,b2,b3. The only nontrivial order relations are

    a1 < b1 > a2 < b2 > a3 < b3 > a4.

Give P its **upper-set** Alexandrov topology. (This is an explicitly chosen order convention; Cameron–Kumar use the opposite specialization-order convention, with minimal neighborhoods denoted ↓x.) The smallest open containing x is ↑x, and the closure of an open set W is ↓W.

Because
- ↑a1={a1,b1}, ↑a3={a3,b2,b3}, and ↑a4={a4,b3},
- cl(↑a1)={a1,a2,b1},
- cl(↑a3)={a2,a3,a4,b2,b3}, and
- cl(↑a4)={a3,a4,b3},

we have the following pairs:

| Pair | I | U | F | Reason |
| --- | --- | --- | --- | --- |
| (a1,a3) | no | **yes** | yes | Smallest opens disjoint, their closures meet at a2 |
| (a1,a4) | no | **no** | **yes** | Even the smallest-open closures are disjoint; P is connected |

The F statement follows because any continuous P→R is constant on comparable points, hence on all of the connected zig-zag P. Since P is finite and sober and its localic product agrees with the finite-space product, these witnesses show

    I(P) ⊊ U(P) ⊊ F(P)

**as sublocales** (not just as pointwise set-theoretic relations).

This is consistent with Cameron–Kumar's result that for Alexandrov spaces U is the square of the inseparability graph and F is the connected-component relation.

## 5. A pointless locale with both inclusions strict

Here is an extension that does not rely on the existence of *any* points in the resulting locale.

**Theorem 3 (working proof).** Let P be a finite poset with its upper-set Alexandrov topology, let Y be any **nontrivial** locale, and let Z=P×Y. For each x∈P there is a locale map (generalized point) s_x:Y→Z defined by s_x=(constant x, id_Y). For each x,y, define t_xy=(s_x,s_y):Y→Z×Z. Then:

1. t_xy^{-1}(I(Z)) is all of Y iff ↑x∩↑y≠∅, and is the empty sublocale otherwise.
2. t_xy^{-1}(U(Z)) is all of Y iff cl(↑x)∩cl(↑y)≠∅, and is empty otherwise.
3. t_xy^{-1}(F(Z)) is all of Y iff x and y belong to the same comparability-connected component of P, and is empty otherwise.

In particular, for the seven-element P of §4 and *any nontrivial pointless locale Y*,

    I(P×Y) ⊊ U(P×Y) ⊊ F(P×Y).

Moreover P×Y is itself pointless, since any point 1→P×Y would project to a point 1→Y.

**Proof.** Write B=O(Y). The coproduct frame O(P×Y) identifies with the frame of monotone B-valued functions W:P→B, where x≤z implies W_x≤W_z. This identification sends an elementary rectangle U⊠b to W_x=b for x∈U, zero otherwise. To check the identification, every monotone W decomposes into the join

    W = ⋁_{x∈P} (↑x)⊠W_x,

and the same formula reconstructs each elementary rectangle, since U=⋃_{x∈U}↑x. All joins and finite meets are pointwise. In particular s_x^*(W)=W_x.

For (1), pullback of the separation open along t_xy gives

    t_xy^*(d_I(Z)) = ⋁_{W∧V=0} W_x∧V_y.

If z≥x,y, any term is zero because W_x∧V_y≤W_z∧V_z=0. If ↑x∩↑y=∅, take W=(↑x)⊠1_B and V=(↑y)⊠1_B. They have zero meet and W_x∧V_y=1_B. Therefore the pullback open is either 0 or 1 as claimed, and the inverse-image closed sublocale is respectively Y or empty.

For (2), similarly,

    t_xy^*(d_U(Z)) = ⋁_{W*∨V*=1} W_x∧V_y.

If cl(↑x)∩cl(↑y)≠∅, choose t∈P and z,z'∈P with t≤z, t≤z', x≤z, and y≤z'. Fix any W,V with W*∨V*=1 and put q=W_x∧V_y. We have q≤W_z and q≤V_z'. Since t≤z and t≤z', monotonicity and W*∧W=V*∧V=0 give

    q∧(W*)_t=0=q∧(V*)_t.

But (W*)_t∨(V*)_t=1_B, hence q=0. All generators therefore pull back to zero.

Conversely, if cl(↑x) and cl(↑y) are disjoint, then in O(P), (↑x)*∨(↑y)*=1. Pulling back the two opens via Z→P preserves this farness condition (as in Proposition 2). Thus W=(↑x)⊠1_B and V=(↑y)⊠1_B satisfy W*∨V*=1, while W_x∧V_y=1_B. This proves (2).

For (3), whenever ↑x∩↑y≠∅, (1) says t_xy factors through I(Z), hence through F(Z). Because F is the intersection of the real-map kernel pairs, for every localic f:Z→R this forces f∘s_x=f∘s_y as locale maps Y→R. Comparability implies inseparability, so equality holds along any comparability zig-zag, yielding the *whole* Y as pullback of F for x,y in the same component.

If x,y lie in different comparability components, choose a continuous g:P→R which has value 0 on the component of x and 1 on the component of y (components are clopen). Then f=g∘pr_P separates s_x,s_y identically over Y, so t_xy^{-1}(K_f) is empty, and t_xy^{-1}(F(Z)) is empty. □

**Concrete pointless choice.** Take Y to be the locale whose frame is RO(R), the complete Boolean algebra of regular open subsets of the real line. This is a nonzero atomless complete Boolean algebra, and its locale has no points (a completely prime filter of a complete Boolean algebra yields an atom). Thus the seven-point P times this Y is a **pointless example where both localic relation inclusions are strict**.

**Importance of the theorem:** no points of Z exist to serve as vertices, but generalized points s_x with domain Y still detect the separation hierarchy. This is an argument about sublocale inclusions, not a claim about ordinary point graphs on a nonspatial space.

## 6. Collapse of the upper relation for normal locales

**Proposition 4 (working proof).** If the frame O(X) is normal, then

    U(X) = F(X).

**Proof.** It suffices, given a,b∈L with a*∨b*=1, to show a⊠b≤d_F. Invoke the point-free Urysohn separation lemma for the cover a*,b* (Picado–Pultr 2021, VIII.4.4, p. 175). It supplies a frame homomorphism h:O(R)→L with

    h((-∞,1)) ≤ a*,        h((0,∞)) ≤ b*

(and an additional boundedness condition unnecessary here). Choose rationals 0<s<r<1. Because (-∞,1)∪(r,∞)=R and (0,∞)∪(-∞,s)=R, the two displayed inequalities imply

    a ≤ h((r,∞)),           b ≤ h((-∞,s)).

The two real intervals (r,∞) and (-∞,s) have disjoint closures, and their associated product rectangle occurs in d_F (see §2). Hence a⊠b≤d_F. Taking the join over all a,b with a*∨b*=1 gives d_U≤d_F; the reverse inequality is Proposition 1. Thus d_U=d_F, proving U=F. □

**Interpretation.** This is the relation-level analogue of the familiar fact that normality supplies separating real functions for disjoint closed sets. It is a deduction from the standard localic Urysohn lemma, **not** claimed to be a new separation theorem. This supplies a meaningful collapse result, in contrast to the strictness theorem above.

## 7. Existing literature and possible next research

Established sources:
- Picado–Pultr, *Separation in Point-Free Topology* (2021), III.5 (Isbell's (sH)), III.7 (modified product for conservative (H)), IV.2 (characterizations of strong Hausdorffness), VI (complete regularity), VIII.3–4 (localic real functions).
- Arrieta–Picado–Pultr, *A New Diagonal Separation and Its Relations with the Hausdorff Property*, *Applied Categorical Structures* 30 (2022), 247–263; [public preprint](https://www.mat.uc.pt/preprints/ps/p2117.pdf). Their *F-separated* means **fitted diagonal**, not our functional relation.
- Cameron–Kumar, *Graphs on topological spaces*, especially the hierarchy and Alexandrov-space graph-square theorem.

Open research questions, **not established facts**:
1. Is U(X) already standard under another name? Search beyond just papers containing the word “Urysohn”: proximity, nearness, entourage/farness and localic diagonal-closure literature.
2. How are equality I=U and equality U=F characterized by *intrinsic, comprehensible frame axioms*? They may behave differently from equalities of point graphs.
3. Determine if analogues of Cameron–Kumar's product/strong-product formulas hold for these **sublocales**. Proposition 2 only proves a one-sided naturality statement.
4. Characterize F as the kernel pair of a canonical (perhaps completely regular) reflection, and determine exactly when F=Δ. Do not confuse a point-separating family of functions with locale-theoretic monicity.
5. Examine localic relational composition: when (if ever) is U=I∘I? The analogous graph identity holds in Alexandrov spaces, but arbitrary-localic composition requires care.
6. Find examples with a stronger distinction than products with finite spaces, such as naturally occurring atomless locales, and analyze whether strictness can be characterized internally rather than with auxiliary generalized points.

**Next priorities:** (i) scrutinize Theorem 3 and record an alternative proof via frame coproduct generators, (ii) investigate the relation with the completely regular reflection, and (iii) formulate one useful theorem about equality or product behavior instead of accumulating only definitions.
