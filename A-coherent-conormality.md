# A — Compact-open tests for equality; conormality in coherent frames

**Working research note, 18 October 2026.** This is an attempt to replace the rectangular-saturation tests in [A-equality-characterizations.md](A-equality-characterizations.md) by familiar algebraic conditions. The results below use the standard frame coproduct and Picado–Pultr's *completely below* relation. Working proofs, not novelty claims; terminology of conormality and its prime-ideal characterization **predates this project**.

For a frame L=O(X), set Q=L⊗L=O(X×X). Let

    d_I = ⋁ {a⊠b : a∧b=0},
    d_U = ⋁ {a⊠b : a*∨b*=1},
    d_F = ⋁ {a⊠b : a≺≺b*}.

As before I=C(d_I), U=C(d_U), F=C(d_F), with d_F≤d_U≤d_I.

Throughout, *compact* means order-compact in the frame: k≤⋁S implies k≤⋁S_0 for some finite S_0⊆S. A frame is **algebraic** if its compact elements join-generate every element. It is **coherent** if, further, 1 is compact and compact elements are closed under finite meets. For coherent L the compact elements K(L) form a bounded distributive lattice.

## 1. The key finite-rectangle lemma

**Lemma 1.1 (working proof, arbitrary locales).** Suppose

    a⊠b ≤ ⋁_{i=1}^n u_i⊠v_i

and u_i*∨v_i*=1 for every i. Then a*∨b*=1.

**Proof via closed sublocales.** For any opens a,b, the closure of the rectangle a⊠b is

    cl(a⊠b) = cl(a) × cl(b)

as closed sublocales of X×X. Algebraically this says

    (a⊠b)* = (a*⊠1) ∨ (1⊠b*).

One way to check this formula is in the standard cp-ideal construction of the frame coproduct (Picado–Pultr 2021, Appendix A.8). An elementary rectangle c⊠d has zero meet with a⊠b iff c∧a=0 or d∧b=0: nonzero pure rectangles have nonzero tensor product. All elements of Q are joins of rectangles. Taking the join of the disjoint rectangles gives the displayed pseudocomplement identity.

The finite join of the closed sublocales cl(u_i⊠v_i) is closed. Taking closures of the hypothesized inequality yields

    cl(a)×cl(b) ⊆ ⋁_{i=1}^n (cl(u_i)×cl(v_i)).

Pull back along the diagonal δ:X→X×X. The left side becomes the closed sublocale cl(a)∩cl(b)=C(a*∨b*). The right side becomes a finite join of closed sublocales C(u_i*∨v_i*)=∅, because inverse image of a finite join of closed sublocales preserves that join. Thus C(a*∨b*) is empty, so a*∨b*=1. □

**Lemma 1.2.** If a and b are compact in L, then a⊠b is compact in Q.

**Reason.** The corresponding open sublocales a and b are compact locales, and their product is compact by the finite localic Tychonoff theorem. Their product is the open sublocale represented by a⊠b. (In the coherent case this also follows immediately by representing L as the opens of a spectral space: compact-open rectangles in a finite product are compact.)

**Consequence.** If a,b are compact and a⊠b≤d_U, then a*∨b*=1: compactness gives a *finite* subcover and Lemma 1.1 applies.

This is the essential step that was missing from the original rectangular-saturation criterion.

## 2. The algebraic-frame criterion for I=U

**Theorem 2.1 (working proof).** If L is algebraic, the following are equivalent:

1. I(X)=U(X).
2. Whenever k,l∈K(L) satisfy k∧l=0, they satisfy k*∨l*=1.
3. For every disjoint a,b∈L, the canonical compact-element decompositions

       a = ⋁{k∈K(L):k≤a},    b = ⋁{l∈K(L):l≤b}

   form a **far grid**: k*∨l*=1 for each k≤a and l≤b from these decompositions.

**Proof.** (1)⇒(2): If compact k∧l=0, then k⊠l≤d_I=d_U. By Lemmas 1.1–1.2, k*∨l*=1.

(2)⇒(3): For k≤a, l≤b, a∧b=0 gives k∧l=0; hence k,l are far.

(3)⇒(1): For arbitrary a∧b=0, write a,b as above and distribute ⊠ over joins:

    a⊠b = ⋁_{k≤a,l≤b; k,l compact} k⊠l ≤ d_U.

Thus d_I≤d_U; the reverse inclusion is automatic. □

**Scope caution:** L being *algebraic* is essential for the converse argument; merely imposing condition 2 on compact elements of an arbitrary frame says nothing if there are too few compact opens.

### A counterexample if compact generation is dropped

Let P be the seven-element finite Alexandrov space in [A-hierarchy-first-results.md](A-hierarchy-first-results.md), with I(P)⊊U(P). Take Z=P×ℝ with its ordinary topological product. It retains I(Z)⊊U(Z): choose the two finite witnesses (a1,a3) and the same real coordinate 0. But **Z has no nonempty compact open sets**. Indeed, the projection to ℝ of a nonempty compact open subset of P×ℝ would be a nonempty compact open subset of ℝ, impossible. Therefore condition 2 is vacuous for Z, but I≠U. This shows why compact generation cannot be omitted.

## 3. Coherent frames and conormal distributive lattices

Recall that a bounded distributive lattice K is **conormal** if

    ∀k,l∈K,   k∧l=0 ⇒
       ∃c,d∈K with k∧c=0, l∧d=0, c∨d=1.

This is sometimes called *dual normality*; beware conflicting normal/conormal terminology in older sources.

**Theorem 3.1 (working proof).** For every coherent frame L,

    I(X)=U(X)  ⇔  K(L) is conormal.

**Proof.** Theorem 2.1 says I=U iff k*∨l*=1 for all disjoint k,l∈K. If K is conormal, witnesses c,d∈K have c≤k*, d≤l*, c∨d=1; hence k*∨l*=1.

Conversely suppose k*∨l*=1. Since L is algebraic, k* and l* are joins of compact elements beneath them. Because 1∈K is compact, the covering 1=k*∨l* has a finite subcover by such compact elements. Join the compact elements associated with k* to obtain c∈K with c≤k*, and likewise obtain d≤l*. They satisfy c∨d=1 and are the required conormal witnesses. □

This is a **pure bounded-distributive-lattice criterion** involving only finite joins and meets. Unlike the general tensor saturation test, it is a familiar, extensively studied property.

Established literature: G. Georgescu, “Lattices of fractions and flat morphisms of bounded distributive lattices,” *Journal of Algebraic Hyperstructures and Logical Algebras* **1**(4) (2020), 1–19, DOI [10.29252/HATEF.JAHLA.1.4.1](https://doi.org/10.29252/HATEF.JAHLA.1.4.1), Proposition 6.1 (citing Cornish). It recalls the equivalences

    K conormal  ⇔  each prime ideal of K contains a unique minimal prime ideal
               ⇔  distinct minimal prime ideals are comaximal.

The *equivalence of our new relation equality with K-conormality* is the point of this note; conormality and its spectral interpretation are not new discoveries.

**Corollary 3.2.** For coherent L, I=U iff each prime ideal of K(L) contains a unique minimal prime ideal. This gives a spectral/prime-ideal characterization (standard classical prime-ideal theorem assumed).

**Corollary 3.3 (commutative algebra).** Let R be a commutative ring with 1, and X=Spec(R) with the Zariski topology. Since O(X) is coherent, with K=compact Zariski opens, one has

    I(X)=U(X) ⇔ every prime ideal of R contains exactly one minimal prime.

The right-hand side is the usual **mp-ring** condition. The identification follows from the order-preserving correspondence between ring primes and prime ideals of the distributive lattice of compact opens. The algebraic side has an extensive literature: Georgescu, “Flat topology on the spectra of quantales,” *Fuzzy Sets and Systems* **406** (2021), 22–41, Proposition 8.9 / Corollary 8.10; and later work on mp-rings/quantales.

*Example:* For R=k[x,y]/(xy), the prime (x,y) contains the two minimal primes (x),(y). Thus I(Spec R)≠U(Spec R). Geometrically D(x) and D(y) are disjoint compact opens whose closures are the two intersecting irreducible components.

*Example:* For any integral domain, the prime (0) is the unique minimal prime. Thus I(Spec R)=U(Spec R); here the spectrum is irreducible and the equality is unsurprising.

## 4. The upper equality U=F in the coherent case

There is a parallel exact criterion. We write k≺≺l* when k and l are **completely separated** in the frame; by Picado–Pultr (2021), VI.1.5.2, pp. 110–111, this is equivalent to the existence of a localic real function taking value 0 on the open k and 1 on the open l.

**Theorem 4.1 (working proof, classical mathematics).** For a coherent frame L, the following are equivalent:

1. U(X)=F(X).
2. For every compact k,l∈K(L),

       k*∨l*=1  ⇒  k≺≺l*.

3. Whenever a*∨b*=1, writing a,b as joins of compact elements beneath them produces a **completely separated grid**: each compact k≤a and l≤b satisfies k≺≺l*.

**Proof.** The implications (2)⇒(3)⇒(1) use only algebraic generation and the formula d_F=⋁_{p≺≺q*}p⊠q. Indeed, if a,b are far, so is every compact k≤a,l≤b. Thus k≺≺l*, and distributing ⊠ gives a⊠b≤d_F. Taking all far a,b proves d_U≤d_F, hence U=F.

For (1)⇒(2), suppose k,l compact and far. Then k⊠l≤d_U=d_F. By Lemma 1.2, finitely many completely separated rectangles u_i⊠v_i cover k⊠l. Under classical prime ideal theorem, every coherent locale has a **spatial spectral representation** X=Spec(K(L)), and its localic finite product is the ordinary spectral-space product. Thus in ordinary topological language

    k×l ⊆ ⋃_{i=1}^n (u_i×v_i).

For each i choose continuous f_i:X→[0,1] taking value 0 on u_i and 1 on v_i (Picado–Pultr VI.1.5.2, together with the cutoff construction). Set f=(f_1,…,f_n):X→[0,1]^n. For any x∈k,y∈l, some i satisfies f_i(x)=0, f_i(y)=1. Hence ||f(x)-f(y)||≥1. Consequently the closures of f(k) and f(l) in [0,1]^n are at distance at least 1. Their distance functions D_k,D_l satisfy D_k+D_l≥1 everywhere, and

    g(z) = D_k(z)/(D_k(z)+D_l(z))

is continuous, with g=0 on f(k) and g=1 on f(l). The composite g∘f separates k,l, proving k≺≺l*. (Empty k or l are trivial cases.) □

**Important precision.** The final implication is proved here using **spatiality of coherent locales and their finite products**, not from a general claim that finite completely-separated rectangle covers can be merged in an arbitrary nonspatial locale. A fully internal/localic version of the finite “distance separator” lemma remains to be checked. We do not export it beyond the coherent case without proof.

**Consequence.** Both equalities can therefore be decided for a coherent frame simply by examining pairs of compact elements:

    I=U:  disjoint compact pairs must be far;
    U=F:  far compact pairs must be completely separated.

In particular, **both** of the previously sufficient compact-grid tests are actually necessary and sufficient for coherent frames.

## 5. Relation to our original finite Alexandrov examples

In a finite frame every element is compact. Hence:

- I=U iff a∧b=0 ⇒ a*∨b*=1 for **all** a,b. This is the classical *extremal disconnectedness* identity a*∨a**=1 (put b=a*; the converse follows since a≤b* whenever a∧b=0).
- U=F iff a*∨b*=1 ⇒ a≺≺b* for all a,b.

This agrees with the earlier graph criteria in terms of inseparability components. In particular, in a finite Alexandrov frame I=U implies I=U=F. The same implication **holds for all coherent frames**, by the compact quotient theorem in [A-coherent-implication.md](A-coherent-implication.md).

## 6. Remaining work

1. Check how much of Theorems 2–4 is already implicit in existing literature on **conormal / mp-frames and lattices**, in particular Cornish and Georgescu. The standard conormal equivalence is known; claim no priority for the algebraic side.
2. Seek a *purely finite lattice-theoretic* description of the coherent upper criterion (k*∨l*=1 ⇒ k≺≺l*), perhaps involving clopen separators or reflection of the compact-open lattice.
3. Determine if a version of Theorem 4.1 holds for all **algebraic** frames (coherence was used here to invoke an unquestionably spatial spectral representation); identify precise hypotheses for any nonspatial extension.
4. Extend the compact-rectangle argument to **continuous frames** using the way-below relation. The needed relative finite-cover result for rectangles must be established and not merely assumed.
5. Identify naturally occurring nonspatial subclasses with enough compact or “compactly contained” opens to give meaningful criteria.
6. **RESOLVED (affirmatively):** coherent I=U forces I=U=F. See [A-coherent-implication.md](A-coherent-implication.md). The proof is more general: on any compact ordinary space, if the pointwise inseparability and Urysohn relations coincide, the resulting closed equivalence relation has a compact Hausdorff quotient, and hence equals functional equivalence. Coherence ensures this conclusion lifts to the closed sublocales of the spatial product.
