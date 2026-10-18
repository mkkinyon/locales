# A — The coherent implication: I = U forces F = I

**18 October 2026. Working proof; no priority claim.**

**Answer:** Yes. If L=O(X) is a coherent frame, then

    I(X)=U(X)  ⇒  I(X)=U(X)=F(X).

More generally, for an ordinary **compact topological space** T (no T0, T1, or sobriety assumption required), equality of the two **pointwise** relations (inseparability and Urysohn inseparability) implies equality with functional equivalence. The coherent-locale conclusion follows since its spatial spectral representation, as well as its finite product, faithfully represent opens and **closed sublocales**.

This supplies the answer to Question 6 in [A-coherent-conormality.md](A-coherent-conormality.md), and strengthens the earlier finite-Alexandrov observation. No assertion is made about arbitrary **compact nonspatial locales**, for which the argument below via ordinary points is insufficient.

## 1. General point-set lemma (elementary)

Let T be a topological space. Define on T:

    x I y  ⇔  every open neighborhood of x meets every open neighborhood of y;
    x U y  ⇔  for every open N∋x and M∋y, cl(N)∩cl(M) ≠ ∅;
    x F y  ⇔  f(x)=f(y) for every continuous f:T→R.

(Include reflexive pairs in all relations.)

**Lemma 1.** If I=U as binary relations on T, then I is an equivalence relation.

**Proof.** I is symmetric and reflexive. Suppose xIy and yIz but not xIz. The equality I=U implies not xUz, so there are opens A∋x and B∋z with cl(A)∩cl(B)=∅. From xIy we get y∈cl(A), and from yIz we get y∈cl(B), a contradiction. □

**Lemma 2.** If T is compact and E⊆T×T is a **closed equivalence relation**, then its ordinary topological quotient Q=T/E is compact Hausdorff.

**Proof.** The quotient is compact. The quotient map q:T→Q is closed: if C⊆T is closed, q^(-1)(q(C)) is the projection of E∩(T×C) onto the first coordinate, hence closed since T is compact and projection from a product with compact factor is closed (tube lemma).

Let A,B be distinct E-classes. They are disjoint closed subsets of T, hence compact. Since E is closed and A×B avoids E, the Wallace lemma (tube lemma twice and finite subcovers) yields neighborhoods V⊇A and W⊇B such that V×W avoids E. Because q is closed, the sets Q\q(T\V) and Q\q(T\W) are open neighborhoods of q(A) and q(B), respectively. They are disjoint, since their inverse images lie in V,W and V×W avoids E. Thus Q is Hausdorff. □

**Theorem 3 (compact-space implication).** If T is compact and I=U, then

    I=U=F.

**Proof.** By Lemma 1, E=I is an equivalence relation. The set I is the closure of the diagonal in the **ordinary** topological product T×T, so E is closed. Lemma 2 makes Q=T/E compact Hausdorff.

Every continuous f:T→R is constant on E-classes: if f(x)≠f(y), there are disjoint real neighborhoods of these values whose inverse images separate x,y, so not xIy. Thus E⊆F.

Conversely, if not xEy, then q(x)≠q(y) in compact Hausdorff Q. By normality/Urysohn's lemma, some g:Q→[0,1] distinguishes q(x),q(y). Then f=g∘q is continuous and separates x,y, so not xFy. Thus F⊆E, proving equality. □

**Observation:** The key input is compactness, which ensures the quotient by the closed equivalence relation is Hausdorff. This is **not** a general argument for noncompact spaces.

## 2. Coherent locales

Recall the setting: a coherent frame L is algebraic, with 1 compact and compact elements closed under finite meets. Under the usual prime-ideal theorem, it is spatial and represented by a spectral space T; compact-open subsets are exactly K(L). Such T is quasi-compact (= compact in the non-Hausdorff sense), locally compact, and sober.

Furthermore, for spectral spaces the locale product corresponds to the **ordinary topological product**; the product is again spectral (or use the locally compact factor theorem for frames of opens). Thus

    O(T×T) ≅ L⊗L.

The three localic relations I,U,F are **closed sublocales** of the product. Their corresponding underlying closed subsets of T×T agree with the pointwise relations I,U,F of §1. In a spatial locale, equality of these **closed** subsets implies equality of the corresponding closed sublocales (unlike arbitrary, non-closed sublocales).

**Corollary 4.** For coherent L,

    I(X)=U(X)  ⇒  I(X)=U(X)=F(X).

**Proof.** Equality of closed sublocales implies equality of the underlying point relations on spectral T. Since T is compact, Theorem 3 gives I(T)=F(T). As these relations are closed and O(T×T)=L⊗L, their equality on ordinary points implies equality as sublocales. □

Combined with the coherent conormality theorem already established:

**Corollary 5.** For coherent L,

    K(L) conormal  ⇒  I(X)=U(X)=F(X).

Equivalently, for coherent frames, **I=U automatically implies U=F**.

### Ring-theoretic version

For any commutative unital ring R with mp property (each prime ideal contains a unique minimal prime),

    I(Spec R)=U(Spec R)=F(Spec R).

This connects our earlier result with the existing **compact Hausdorff quotient** pSpec R of Spec R via the equivalence generated by inclusion of prime ideals, discussed by François Couchot, *Almost clean rings and arithmetical rings*, arXiv:0901.1744, Proposition 2.2 (itself citing an earlier source). The quotient pSpec R is Hausdorff when R is mp. The abstract closed-relation proof above avoids the need to invoke this specialized result.

## 3. What exactly this does and does not settle

- We have an **affirmative** answer for coherent frames, and an elementary stronger point-set lemma for **all compact spaces**.
- It does **not** settle the implication for arbitrary compact **nonspatial** locales; there the generalized-point/closed-kernel arguments would need to be formulated internally. The fact that the pointwise equivalence relation becomes transitive is not automatically an internal equivalence-relation theorem in Loc.
- It does **not** settle the implication for all algebraic frames: some algebraic frames have noncompact spectrum.
- The conormality characterization from the earlier note is sufficient for the compact spectral-space step, but the proof above is shorter and does **not** use any lattice-prime theory after spatiality and compactness are granted.
- The essential interest may now shift to the **continuous-frame** (core-compact locale) setting and to genuinely nonspatial examples.

## Literature checks

- Picado–Pultr, *Separation in Point-Free Topology* (2021), III.5 for the closure of the diagonal and V–VI for frame regularity and complete regularity.
- F. Couchot, *Almost clean rings and arithmetical rings*, arXiv:0901.1744, Proposition 2.2, [source](https://arxiv.org/pdf/0901.1744): pSpec(R) is Hausdorff for mp-rings; compactness is automatic as a quotient of Spec R.
- K. H. Hofmann and J. D. Lawson, *The spectral theory of distributive continuous lattices*, Transactions AMS **246** (1978), 285–310, on spectral representation of coherent/algebraic frames.
- P. Johnstone, *Stone Spaces* (1982), for coherent locales and spectral products.
