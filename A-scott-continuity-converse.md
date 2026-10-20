# Project A — A Scott-continuity converse for closed relations

**20 October 2026. New working theorem, direct proof; a response to the two external adversarial audits' question about converses to properness.** No source-priority claim. The proof below establishes more than the locally compact Hausdorff special case suggested in the Claude Opus 5.5 audit. This note distinguishes the ordinary topological theorem from its localic consequence.

## 1. The general topological theorem

**Theorem (working proof).** Let X be a **weakly locally compact** topological space (every point has some compact neighborhood), Y any topological space, and E⊆X×Y a **closed relation**. Let p_X,p_Y be its projections and define

    r_E(U)=(p_Y)_*p_X^*(U)
           =int_Y(Y\E[X\U]),      U∈O(X).

Then

    r_E preserves directed joins
        ⇔ p_Y:E→Y is a **perfect topological map**,
           i.e. continuous, closed and with compact point fibers.

No relation axioms (reflexivity, symmetry, transitivity), Hausdorffness, T0, or sobriety are required.

**Proof (⇒).** By weak local compactness, take a cover {V_i:i∈J} of X by open sets V_i each lying in a compact subset K_i⊆X. For finite F⊆J let

    U_F=⋃_{i∈F} V_i,     K_F=⋃_{i∈F}K_i.

The directed family U_F has join X. Since r_E(X)=Y and r_E preserves directed joins,

    Y=⋃_{F finite} W_F,     W_F:=r_E(U_F).

Each W_F is open in Y. From the defining adjunction p_Y^*(W_F)≤p_X^*(U_F), one obtains

    E∩(X×W_F)⊆U_F×W_F⊆K_F×W_F.

Thus E over W_F is **contained in a compact support K_F uniformly throughout W_F**. Because E is closed in X×Y, its restriction E_F:=E∩(X×W_F)=E∩(K_F×W_F) is closed in K_F×W_F. Projection K_F×W_F→W_F is closed by the tube lemma (compact K_F; **no Hausdorff assumption**). Hence for any closed H⊆E, the image p_Y(H)∩W_F is closed in W_F: H is closed in X×Y because E itself is closed, and its restriction to K_F×W_F is closed. Since the W_F cover Y, p_Y(H) is closed. Therefore p_Y is a closed map.

Also each fiber E_y (y∈W_F) is a closed subset of compact K_F: E closed implies the pullback along K_F→X×Y, x↦(x,y), is closed. Thus every fiber of p_Y is compact. This proves p_Y perfect.

**Proof (⇐).** If p_Y is closed, then for open V⊆E,

    (p_Y)_*(V)=Y\p_Y(E\V),

since the right side is open and is exactly the greatest open whose inverse image lies in V. Let V_j be a directed family of opens of E. If y∈(p_Y)_*(⋃V_j), its compact fiber is covered by ⋃V_j, hence is contained in some V_j by directedness. Thus (p_Y)_* preserves directed joins. Since p_X^* preserves all joins, so does r_E. □

**Two independent assumptions and why they are present:** The proof needs (i) **closedness of E** to make the restricted relation a closed subset of each compact-support product, and (ii) the existence of a **cover by opens contained in compact sets** in the *source coordinate* X. It is not asserted for arbitrary non-weakly-locally-compact spaces or for nonclosed relations. The target Y needs no assumptions.

## 2. Equivalent localic properness condition when X has a continuous frame

Let X be strongly locally compact and sober, and E↪X×X a **closed localic subrelation**. Classical Hofmann–Lawson duality gives this setting for **any continuous frame** L=O(X) under ZFC. The localic product X×X is spatial and agrees with the ordinary product; the closed sublocale E is the locale associated with an ordinary closed subspace.

For its relation projections p_1,p_2:E⇉X, the topological theorem yields:

    r_E=(p_2)_*p_1^* Scott-continuous
      ⇔ p_2 is a closed map with compact ordinary fibers.

A **closed topological map with compact fibers induces a proper locale map**, by a direct adjoint calculation: the topological p_{2*} preserves directed joins as proved in §1, and its closed Frobenius law is

    p_{2*}(V∪p_2^-1(W))
      = X\p_2((E\V)∩p_2^-1(X\W))
      = p_{2*}(V)∪W.

Conversely, if p_2 is a **proper locale map**, then (p_2)_* preserves directed joins, so r_E does as well.

**Corollary (continuous frames, classical):** for any closed localic subrelation E↪X×X of a **continuous locale** X,

    r_E Scott-continuous
       ⇔ p_2 is proper as a locale map.

If E is symmetric, the coordinate swap identifies the two projections, so **both** projections are proper. No transitivity of E is needed for this equivalence.

**Specializing to inseparability:** I=clΔ is closed and symmetric. Thus for a continuous frame L,

    r_I Scott-continuous
       ⇔ p_1,p_2:I⇉X are proper locale maps.

If I is also **transitive** (for example if I=U, by I∘I⊆U), Vermeulen's proper-effectiveness theorem and the continuity of the quotient yield

    I=U=F.

This is an **exact operator-theoretic criterion for properness in continuous frames**, not an equivalence for functional equality: Claude's countable example has I=U=F but r_I not Scott-continuous.

**Limitation:** This is not yet a choice-free internal-locale proof for arbitrary noncontinuous, possibly pointless frames. The reduction to topology uses classical spatiality/product comparison of continuous locales.

## 3. Better interpretation: local compact support, not just compact fibers

The key intermediate consequence of Scott continuity is a stronger neighborhood-wise property: for every open cover {V_i} of X and every y∈Y there are a finite F and an open neighborhood W∋y such that

    E∩(X×W) ⊆ (⋃_{i∈F}V_i)×W.

Conversely, if this **finite-cover local support** property holds for every open cover, then r preserves directed joins: given directed u_j with union u, if y∈r(u), choose neighborhood W∋y with E_W⊆u, apply the cover consisting of {u_j} together with X\u (the latter may not be open), so a direct converse requires using the localized domain u and refinement; the short converse used in the theorem instead proceeds through properness of p_Y. **Do not silently infer a general equivalence for arbitrary E or arbitrary X from the displayed finite-cover condition.**

Under weak local compactness, finite local support yields **compact local support K_F** and hence properness of the projection when the graph E is closed. This explains why closed-graph and Scott-continuity hypotheses complement each other.

## 4. Consequences for the examples and the hierarchy

- **Cofinite-cloud deleted plank:** its I quotient is **closed** but has noncompact classes; r_I fails Scott continuity by the explicit increasing opens in [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md), §2½.
- **Claude's countable nonidempotence example:** its I classes are finite, but its quotient is **not closed**; r_I fails Scott continuity. See [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md).
- **Any continuous-frame I with transitivity and Scott-continuous r_I:** the relation projections are proper and I=U=F. This strengthens the earlier one-way properness criterion to an **iff for properness**, without asserting an iff for functional separation.
- **Purely pointwise weak-local-compactness corollary:** if X is weakly locally compact, I=clΔ is transitive on points and r_I Scott-continuous, then the topological quotient by I is perfect and Hausdorff. It is weakly locally compact by a finite compact-fiber neighborhood argument, and a weakly locally compact Hausdorff space is locally compact Hausdorff, hence completely regular. Thus **I=U=F on ordinary points**. To infer equality of the **closed localic relations**, impose strong local compactness and sobriety/product spatiality as in §2.

## 5. Scope, literature and audit status

- This is a **direct new proof for our project**, not a priority claim. The result resembles the known upper-Vietoris/upper-hemicontinuity compact-valued correspondence criterion and classical tube-lemma/proper-map statements; an exact precedent has not been searched exhaustively.
- The proof extends the LCH converse asserted in the external Claude Opus 5.5 audit: it permits arbitrary weakly locally compact non-Hausdorff X, arbitrary Y, and closed **nonequivalence** relations E.
- The theorem is presently **working** and has not been subjected to a fresh external audit. The previous external reports vetted only the earlier directions and special cases.
- Definitions and localic properness: J. J. C. Vermeulen, *Proper Maps of Locales*, JPAA **92** (1994), 79–107. See also [A-vermeulen-effectiveness-correction.md](A-vermeulen-effectiveness-correction.md).
