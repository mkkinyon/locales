# A — Beyond one countable exhaustion: clopen kω decomposition and paracompactness

**18 October 2026. Status: working theorem with proof, not a claim of priority.** This continues [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md). The main point is to allow **arbitrarily many** countable compact exhaustions on disjoint clopen pieces, rather than forcing one globally countable exhaustion.

## 1. Definitions and the exact strengthening

For a topological space X, E=cl(Δ_X) in X×X is the (reflexive symmetric) inseparability relation. For x,y∈X, xEy precisely when every open neighborhood of x meets every open neighborhood of y. Functional equivalence F means f(x)=f(y) for every continuous f:X→R.

We always have I⊆U⊆F. If I=U, the relation E=I is an **equivalence relation** (proof in [A-coherent-implication.md](A-coherent-implication.md)). The following results assume only that E is transitive, which is formally **weaker** than I=U.

**Theorem A (topological sums of kω spaces).** Suppose

    X = ⨆_{α∈A} X_α

is an arbitrary topological disjoint sum, where each X_α is a **kω-space** (admitting a countable compact determining cover). If E=cl(Δ_X) is transitive, then

    X/E is normal Hausdorff,      E=F.

**Proof.** Distinct clopen summands have disjoint open neighborhoods, so E does not relate points from different summands. Thus E is the disjoint union of E_α=cl(Δ_{X_α}), with E_α equivalence on X_α. By the theorem of [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md), Q_α=X_α/E_α is normal Hausdorff. The global quotient is the topological disjoint union Q=⨆Q_α: each summand is E-saturated and clopen, and the quotient topology is final with respect to them. A disjoint union of normal Hausdorff spaces is normal Hausdorff (separate closed sets summand by summand). Hence continuous real functions on Q distinguish points, and pulling back via q:X→Q gives E=F. □

No compactness, local compactness, sobriety, Hausdorffness or restriction on the **cardinality** of A is required for this *point-set* theorem. For a conclusion involving closed localic relations, impose locally compact sobriety of X to ensure the spatial product comparison used in our previous notes.

## 2. Locally countable σ-compact open covers

Say a family of subsets {V_i:i∈J} is **locally countable** if every x∈X has a neighborhood meeting at most countably many members of the family. (Local finiteness is stronger.)

**Lemma B (cover decomposition).** Suppose X admits a **locally countable open cover by σ-compact open subspaces**:

    X=⋃_{i∈J} V_i,     each V_i open and σ-compact.

Then X is a topological disjoint union of **clopen σ-compact** subspaces.

**Proof.** Every compact K⊆X meets only countably many V_i. Indeed, cover K by finitely many neighborhoods, each of which meets at most countably many of the V_i.

Hence each σ-compact V_i=⋃_n K_{in} meets only countably many V_j. Form the intersection graph on J: i~j when V_i∩V_j≠∅. Every vertex has countable degree, so each connected component J_α is countable, being the union of its finite-distance spheres. Let

    X_α = ⋃_{i∈J_α} V_i.

These X_α are mutually disjoint, cover X, and are each open; their complements are unions of the other X_β and therefore also open. Since J_α is countable and each V_i σ-compact, X_α is σ-compact. □

**Theorem C (direct locally countable covering hypothesis).** Let X be **locally compact** and admit a locally countable open cover by σ-compact subspaces. If E is transitive, then

    X/E normal Hausdorff,       E=F.

**Proof.** Lemma B gives a clopen partition into σ-compact spaces X_α, each locally compact. Every locally compact σ-compact space is kω (proof in [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md)). Apply Theorem A. □

The covering condition is sufficient. We do **not claim** that it is a strictly weaker condition than paracompactness within the category of locally compact spaces, since that comparison depends on conventions and may collapse to an equivalence. The lemma is worthwhile because it isolates the **one cover** needed, without quantifying over all open covers.

## 3. Paracompactness implies the covering condition

**Paracompactness convention:** Every open cover has a *locally finite open refinement*. **No Hausdorff axiom is built into the definition.** This matters because our spaces are often non-Hausdorff; standard textbook statements sometimes define "paracompact" only for Hausdorff spaces.

**Lemma D (non-Hausdorff-safe decomposition).** If X is locally compact in the sense that every point has a compact neighborhood and X is paracompact in the preceding sense, then X is a topological disjoint union of clopen σ-compact subspaces.

**Proof.** Choose an open cover {U_x} such that each U_x lies in a compact neighborhood K_x. Take a locally finite *open* refinement {V_i}, with each V_i⊆K_i compact. Every V_i is σ-compact, being contained in K_i? **Careful:** an arbitrary subset of a compact set need not be σ-compact! Thus we do **not** assert V_i is σ-compact.

Instead form the intersection graph of the V_i. By local finiteness every compact K_i meets only finitely many V_j; hence V_i⊆K_i meets only finitely many V_j. Each graph component J_α is countable. Its union X_α=⋃_{i∈J_α}V_i is clopen (as in Lemma B). For each i∈J_α, **K_i∩X_α** is compact, being a closed subset of compact K_i, and lies in X_α. It contains V_i. Therefore

    X_α = ⋃_{i∈J_α} (K_i∩X_α),

a countable union of compact sets. No separation axiom or assertion that K_i is closed in X was used. □

This proof is stronger in scope than citing the familiar locally compact paracompact decomposition in its usual **Hausdorff** formulation. We have checked the only non-Hausdorff-sensitive point: K_i∩X_α is compact because X_α is **clopen**, not because compact subsets happen to be closed.

**Theorem E (main corollary).** Let X be locally compact and paracompact in the open-refinement sense. If E=clΔ_X is transitive, then

    X/E is normal Hausdorff,       E=F.

If, furthermore, X is sober, then its frame O(X) is continuous, its localic product agrees with the ordinary spatial product, and these conclusions imply the equality of closed localic relations:

    I(X)=U(X)  ⇒  I(X)=U(X)=F(X).

**Proof.** Apply Lemma D and Theorem A. The localized equivalence E=I passes to each clopen summand. The localic conclusion uses only locally compact sobriety and closedness of the relations, just as in [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md). □

**Corollary (stable interpolation).** Under Theorem E, if a,b are opens with disjoint closures and u≪a,v≪b, choose compact K,H with u⊆K⊆a,v⊆H⊆b. The quotient Q=X/E is normal Hausdorff, so the disjoint compact closed images q(K),q(H) admit a continuous [0,1]-separator. Its pullback to X yields a real separator of u and v and the explicit dyadic ≺-scale described in [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md), §2a. The intermediate opens need **not** be relatively compact.

## 4. Why this genuinely drops σ-compactness

An **uncountable disjoint union** of compact or locally compact σ-compact spaces is locally compact and paracompact, but it need not be σ-compact.

For example

    X = ⨆_{α<ω₁} X_0,

with X_0 the compact non-Hausdorff "two-arm" example in [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md) (I=U=F), is locally compact, sober, paracompact in the stated open-refinement sense, and not σ-compact. It satisfies I=U=F, even though each summand has a nontrivial inseparability class. An uncountable discrete space is a simpler example but would make the separation issue trivial.

A compact subset of a topological disjoint sum meets only finitely many summands (by the open summand cover), which proves the stated failure of σ-compactness.

The paracompact hypothesis is **not necessary**: the ordinal space [0,ω₁) is locally compact Hausdorff, non-σ-compact and not paracompact, but I=U=F=Δ simply because it is locally compact Hausdorff. Thus these results narrow the interesting counterexample regime but cannot characterize equality.

## 5. Relation to existing literature and remaining problem

Decomposing locally compact paracompact spaces into clopen σ-compact pieces is a familiar theorem, e.g. Dugundji, *Topology*, and lecture notes [Topology, Proposition 91](https://www.jku.at/fileadmin/gruppen/194/Lehre/Skripta_Jim/topology.pdf), p. 98. **Caution:** the latter reference explicitly uses a *Hausdorff* definition of paracompactness, so it is not a source for our non-Hausdorff generalization; the proof in §3 addresses that gap.

For kω topology, consult Franklin and Smith Thomas, [*A Survey of kω-spaces*](https://topology.nipissingu.ca/tp/reprints/v02/tp02105.pdf), *Topology Proceedings* **2** (1977), 111–124, and the prior detailed proof in [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md).

**Resolved positively:**
- arbitrary disjoint topological sums of kω spaces;
- locally compact spaces with a locally countable σ-compact open cover;
- locally compact paracompact spaces, with no Hausdorff requirement built into paracompactness;
- all locally compact σ-compact spaces (the previous theorem).

**Unresolved:** For *every* locally compact sober space X, does E=I transitive (or the stronger I=U) imply E=F? A counterexample would have to be more global than the lack of one countable exhaustion: it cannot be locally compact paracompact in the stated sense, or have the locally countable σ-compact open cover of Theorem C. The obstruction is still not identified, and **absence of paracompactness does not itself signal a counterexample**.

Possible next task: investigate countably compact but noncompact locally compact sober spaces, e.g. non-Hausdorff modifications of ordinal spaces, in which no clopen σ-compact decomposition is available. These are examples where the countable-stage Tietze method lacks a direct replacement.
