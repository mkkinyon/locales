# A — Does I = U imply U = F for all continuous frames?

**Status: open in our investigation as of 18 October 2026.** This note proves a positive result under an additional *open quotient* hypothesis, exhibits a sober compact example showing that openness does not follow from I=U, and identifies the precise obstruction to the earlier compactness proof. **We have neither a proof nor a counterexample to the unrestricted assertion.** No priority claim.

All statements below are in ordinary ZFC, under which a continuous frame is the frame of opens of a locally compact sober space (Hofmann–Lawson). Localic products agree with the ordinary product for such spaces, and our three relations are closed sublocales, so pointwise equality on X×X implies localic equality.

## 1. Transitivity of inseparability: no compactness needed

For a topological space X, write E for the relation that x and y have no disjoint open neighborhoods. Write U for the relation that x and y have no neighborhoods with disjoint closures.

**Proposition 1.** If E=U, then E is an equivalence relation.

**Proof.** If xEy and yEz but x is separable from z, the equality E=U gives open A∋x, B∋z with disjoint closures. Since xEy, y belongs to cl(A). Since yEz, y belongs to cl(B), contradiction. Reflexivity and symmetry are automatic. □

More generally, the compact-space proof in [A-coherent-implication.md](A-coherent-implication.md) needs only that E be an equivalence relation: E=cl(Δ) is closed, and a compact space modulo a closed equivalence relation is compact Hausdorff. Hence E=F for compact spaces whenever E is transitive, without explicitly assuming E=U first.

## 2. A positive theorem without compactness: open inseparability quotients

**Theorem 2 (proved, working).** Let X be a locally compact topological space in the strong/core-compact sense (and, for the frame application, sober). Suppose that the inseparability relation E is an equivalence relation and that its quotient map q:X→Q=X/E is **open** (equivalently, the E-saturation of every open subset of X is open). Then Q is locally compact Hausdorff, and

    E = U = F.

Consequently, the corresponding equality of the three **closed localic relations** holds on the continuous frame O(X).

**Proof.** E is the closure of the diagonal in X×X and is therefore closed. For distinct classes [x]≠[y], because (x,y)∉E there are open A∋x and B∋y with A×B disjoint from E. Hence q(A)∩q(B)=∅. As q is open, q(A),q(B) are disjoint open neighborhoods of the two quotient points. Thus Q is Hausdorff.

Since q is an open continuous surjection and X is locally compact, Q is locally compact: given y=q(x) and an open neighborhood W⊆Q, choose a compact neighborhood K of x contained in q^(-1)(W). The open neighborhood q(int K) of y lies in the compact set q(K)⊆W.

Being locally compact Hausdorff, Q is completely regular. Thus, for distinct E-classes of x,y, there is a continuous g:Q→[0,1] with g(q(x))≠g(q(y)). Therefore f=g∘q separates x,y. Conversely, every continuous real function on X is constant on E-related pairs, as separated real values would yield disjoint inverse-image neighborhoods. Hence E=F. Since E⊆U⊆F, we conclude E=U=F. □

**Comparison with literature.** In C*-algebra primitive ideal spaces, the condition that inseparability be an **open equivalence relation** is the established definition of *quasi-standard* C*-algebras (Archbold–Somerset, *Quasi-standard C*-algebras*, Math. Proc. Cambridge Philos. Soc. **107** (1990), 349–360). This makes the hypothesis independently natural, but it does not imply that the specific result is new.

## 3. Openness of the quotient does NOT follow from I = U

We give a very small **compact, sober, T1** counterexample to the tempting shortcut “I=U, therefore the inseparability quotient is open.”

Let S={s_n:n≥1} and T={t_n:n≥1} be disjoint countable sets, and let X={x,y} ⊔ S ⊔ T. All points of S∪T are isolated. A neighborhood basis at x is

    A_N = {x} ∪ {s_n:n≥N};

and a neighborhood basis at y is

    B_{N,M} = {y} ∪ {s_n:n≥N} ∪ {t_n:n≥M}.

These specify a compact space: any open cover contains a neighborhood of x and a neighborhood of y, and the union of those two covers all but finitely many points of S∪T. It is T1 because any one of x,y,s_n,t_n can be omitted from neighborhoods of the other points.

It is also sober. An irreducible closed subset containing an isolated point z and another point splits as {z}∪(F\{z}) into two proper closed subsets (since {z} is clopen). A closed subset of {x,y} with both points is reducible because both singletons are closed. Hence every nonempty irreducible closed subset is a singleton.

The only nontrivial inseparable pair is xEy, because every neighborhood of x and every neighborhood of y meets on a tail of S. Every other distinct pair is separated by a clopen singleton (if at least one is isolated). Thus E has exactly one nonsingleton class {x,y}. The Urysohn relation is the same: xUy, while any distinct pair involving an isolated point admits disjoint-closure neighborhoods. Hence

    I(X)=U(X).

Nevertheless q:X→X/E is **not open**. Take A_N, an open neighborhood of x. Its E-saturation is

    Sat_E(A_N) = {x,y} ∪ {s_n:n≥N},

which is not open, because every neighborhood of y contains all but finitely many t_n. Thus q(A_N) is not open.

By the compact theorem, F=I=U in this particular example; it is *not* a counterexample to the unrestricted implication. It only proves that the open-quotient hypothesis is independent of I=U, even within the compact continuous class.

## 4. Why the compact proof is insufficient in the general case

When I=U, E is a **closed equivalence relation**. On a compact space, the quotient by any closed equivalence relation is compact Hausdorff, yielding enough real functions to separate E-classes.

For locally compact but noncompact spaces:
- a closed equivalence relation need not have a closed or open quotient map;
- a quotient of a locally compact space need not be locally compact or Hausdorff;
- the real-valued functions on the quotient may fail to separate its points unless further structure is established.

The explicit sober example in §3 disproves the most direct attempt to prove quotient **openness** from I=U. It does not disprove some subtler route to complete functional separation.

## 5. Possible counterexamples and research directions

The **primitive ideal spectra of non-unital C*-algebras** are a potentially fruitful source of counterexamples. Operator algebra literature distinguishes (i) the graph of inseparability, (ii) the equivalence relation generated by that graph, and (iii) equality under all bounded continuous functions (Glimm equivalence). Noncompact primitive spectra can have Glimm equivalence classes containing multiple inseparability components even when the graph diameter is finite.

**However:** such a phenomenon does *not alone* give a counterexample to I=U ⇒ U=F, because one must separately verify U=I, i.e., that any point pair admitting disjoint open neighborhoods also admits neighborhoods with disjoint closures. We have **not** verified this extra condition for any candidate. Do not cite these C*-examples as counterexamples without that check.

Starting references:
- R. J. Archbold and D. W. B. Somerset, *Quasi-standard C*-algebras* (1990).
- R. J. Archbold and D. W. B. Somerset, *Separation properties in the primitive ideal space of a multiplier algebra* (2014).
- R. J. Archbold and collaborators, *Norms of inner derivations for multiplier algebras of C*-algebras and group C*-algebras*; see discussion around Proposition 4.3 on noncompact Glimm classes containing multiple inseparability components.
- G. Gierz et al., *Continuous Lattices and Domains*, and Hofmann–Lawson on continuous-frame spatiality.

**Precise unresolved question:** If X is a locally compact sober space and its two point-relations I and U agree, must every pair outside I be distinguished by a continuous real-valued function? Equivalently, for continuous L, does d_I=d_U imply d_U=d_F?

Theorem 2 establishes yes under the open-quotient hypothesis. The general case remains unsettled here.
