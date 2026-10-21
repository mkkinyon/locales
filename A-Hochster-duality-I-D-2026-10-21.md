# Project A — Hochster duality exchanges the two coherent equality conditions

**21 October 2026. Working theorem and proof, novelty unchecked.** Depends on independently reviewed coherent I=U iff compact lattice conormal, and compact-normality D=U iff compact lattice normal. Do not conflate frame normality with Cornish-normal/conormal.

## 1. Canonical coherent dual

For a coherent frame L let K=K(L), and set L^vee=Idl(K^op). Then K(L^vee)=K^op and (L^vee)^vee≅L. On classical spectral spaces X this is Hochster's inverse/dual spectral topology X^vee, whose compact opens are complements of compact opens of X. It reverses specialization.

**Theorem (working, direct):**

    I(L)=U(L) iff D(L^vee)=U(L^vee);
    D(L)=U(L) iff I(L^vee)=U(L^vee).

Proof: K conormal iff K^op normal and conversely. Apply the project's two coherent characterization theorems. This is an exact involutive exchange of the two *equality properties* within coherent frames. It does NOT assert U(X)=U(X^vee), or literal equality of sublocales from differently topologized products.

## 2. Relation-level pointwise duality

For spectral X adopt x≤y iff x lies in the closure of {y}. Then

    x D_X y iff x,y have a common lower bound;
    x I_X y iff x,y have a common upper bound.

The first is the already verified Cm description. To prove the second, I on ordinary points is equivalent to every open neighborhood of x meeting every open neighborhood of y. Restrict to compact-open neighborhoods (a basis). The family of all compact-open neighborhoods of x and of y has finite intersection property: finite intersections within each subfamily remain neighborhoods, and a neighborhood of x meets a neighborhood of y. In the compact Hausdorff patch topology, each compact open is clopen. Their full intersection contains z. Then z lies in all neighborhoods of x,y, so x≤z,y≤z. Conversely such z lies in each neighborhood of either point, giving I. Under Hochster duality the order reverses, so the *point relations* exchange:

    D_X = I_(X^vee),  I_X = D_(X^vee)

on the common set of spectral points.

**Caution:** Point relations are not arbitrary fitted sublocales. The main theorem is derived independently from the lattice normal/conormal characterizations.

## 3. Combined equality and limits of the analogy

Both I=U and D=U hold on a coherent L iff K is both normal and conormal. Equivalently (classically) every prime ideal of K contains a unique minimal prime and lies in a unique maximal prime. This includes non-Boolean examples such as spectra of nonfield local integral domains, so simultaneous equality does not force discreteness/Hausdorffness.

For a commutative ring R, the two equalities correspond respectively to mp and pm conditions; their conjunction is the simultaneous mp-and-pm condition, not a claim that R is a field or absolutely flat.

The construction is specific to coherent frames via K(L). It is not a general order dual on arbitrary frames: L^op need not be a frame, and Idl(K(L)^op) is unavailable without compact coherent generation. No automatic duality for the functional relation F is claimed. Open-/closed-heredity parallels may be shadows of this geometry but are not consequences of a functor carrying open sublocales to closed sublocales in general.

## 4. Research hypotheses

- Look for a single Priestley-space or bitopological formulation of both equalities, accounting for how U behaves (or fails to behave) under Hochster duality.
- Determine whether the two equivalence relations each induce canonical retractions to maximal/minimal spectra and if any useful compatibility holds when both properties hold.
- Compare with existing normal/conormal duality literature before claiming novelty. Standard Hochster and Priestley dualities themselves are classical.

**Bibliography to check:** Hochster inverse topology; Priestley duality; Cornish normality; De Marco–Orsatti pm-rings; existing compact-normality and conormality literature.
