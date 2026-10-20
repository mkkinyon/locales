# Project A — Subfitness does NOT rescue the continuous-frame implication

**19 October 2026 — working new construction, verified internally, NOT independently refereed.** This note responds to the strengthened question left open after the two-tag construction:

> Does I=U imply U=F for a **subfit continuous frame**?

**Answer: NO, even for an algebraic subfit frame.** The new example is the frame of opens of a **T1, strongly locally compact, sober** space. The older generic-tag example was not subfit; we replace each tag by a **cofinite sequence of isolated points converging to every point of its prescribed closed set**. The method is independent of purported priority, which has not been investigated for this new construction.

## 1. The double cofinite-cloud construction

Let T be a locally compact Hausdorff space with disjoint nonempty closed subsets A,B. Let S_A={a_n:n∈N} and S_B={b_n:n∈N} be disjoint countably infinite sets, disjoint from T. Put

    X = T ⊔ S_A ⊔ S_B.

Declare O⊆X open iff

1. V=O∩T is open in T;
2. if V∩A≠∅, then S_A\O is finite;
3. if V∩B≠∅, then S_B\O is finite.

No further restrictions. In particular, all points of S_A∪S_B are isolated. An equivalent description: every cofinite tail of S_A converges to **every** point of A, and every cofinite tail of S_B converges to **every** point of B, while T keeps its old subspace topology.

**Topology check.** Arbitrary unions preserve the conditions: if a union meets A then a constituent meets A and contains a cofinite S_A; similarly for B. Finite intersections preserve them, since the intersection of finitely many cofinite sets is cofinite. The empty and whole sets qualify.

## 2. T1, strong local compactness, sobriety, subfitness

**Proposition 2.1 (working).** X is T1, strongly locally compact, and sober. Thus O(X) is a continuous **subfit** frame in classical mathematics.

**Proof of T1.** For t∈T, the complement X\{t} is open: T\{t} is T-open, and all of S_A,S_B are included. For s∈S_A∪S_B, the complement X\{s} is open because deleting a single member preserves both cofinite conditions. Every singleton is closed.

**Proof of strong local compactness.** Let t∈T, O an arbitrary open neighborhood, V=O∩T. Choose a T-open W and a compact K⊆T with t∈W⊆K⊆V. Shrink W,K, when necessary, so they avoid whichever of A,B does not contain t. This is possible because A,B are disjoint closed and T is locally compact Hausdorff.

If t∈A, choose a cofinite tail S_A^N⊆O. Then W∪S_A^N is X-open and lies within H=K∪S_A^N⊆O. The set H is compact as a union of two compact subspaces K and {t}∪S_A^N: the latter is compact because **every neighborhood of t contains all but finitely many points of S_A**. The case t∈B is symmetric. If t∉A∪B, shrink K away from A∪B; then W is X-open and t∈W⊆K⊆O. At each added point the open singleton is compact. These compact neighborhoods lie *inside arbitrary given opens*, as needed for continuity of O(X).

**Proof of sobriety.** Every added singleton {s} is **clopen** in X (it is isolated and T1). If a nonempty irreducible closed C contains s, it cannot contain anything else, because {s} and its complement split C into two disjoint nonempty closed subsets otherwise. If C contains no added point, then C⊆T; T is closed in X, and any closed irreducible subset of Hausdorff T is a singleton. Therefore every nonempty irreducible closed set of X is the closure of a unique point: X is sober.

**Subfitness.** For any T1 space, O(X) is subfit: if opens U⊈V choose x∈U\V and W=X\{x}. Then U∪W=X whereas V∪W≠X. Equivalently every open sublocale is a join of closed sublocales (Picado–Pultr standard characterization).

## 3. Inseparability and Urysohn separation

We use points here; §4 explains why the results lift to **closed localic relations**.

**Closure formula.** For any subset Y⊆X, since every added point s is isolated,

    cl_X(Y)∩(S_A⊔S_B) = Y∩(S_A⊔S_B).

For the old points,

    cl_X(Y)∩T =
      cl_T(Y∩T)
      ∪ (A if Y∩S_A is infinite, otherwise ∅)
      ∪ (B if Y∩S_B is infinite, otherwise ∅).

Proof: every neighborhood of any point of A includes a cofinite S_A, and every point outside A has a neighborhood avoiding S_A (except points of B, handled separately); if the intersection with S_A is finite it can be omitted in a suitably late tail. Likewise B.

**Proposition 3.1 (working).** The inseparability equivalence classes are exactly A, B, and all singleton classes {t} for t∈T\(A∪B), plus {s} for s∈S_A∪S_B. Further **I=U** pointwise.

**Proof.** Any two neighborhoods of two points in A contain cofinite subsets of S_A and must intersect. Likewise B. All other distinct pairs have neighborhoods with disjoint closures. To see this for two points t,u of T in distinct proposed classes, use local compact Hausdorff regularity to choose T-open W_t,W_u with disjoint T-closures and with each T-closure avoiding the closed set A or B not containing that point. Adjoin an S_A cofinite tail to W_t iff t∈A, and analogously B, and likewise for W_u. The resulting X-open neighborhoods have disjoint closures by the displayed closure formula: each gains at most the entire corresponding A or B, and neither can meet the other neighborhood's T-closure. For an added point s and any other point z, take {s} and an open neighborhood of z omitting s. Since {s} is clopen, these two neighborhoods have disjoint closures. □

Thus I=U as point relations. Importantly, this is a **closed equivalence relation**, not necessarily the diagonal: A and B are generally infinite equivalence classes.

## 4. Functional indistinguishability and the localic lift

**Proposition 4.1 (working).** Let f:X→R be continuous. Then f is constant on A and separately on B. Conversely, if g:T→R is continuous and constant on A with value α and B with value β, then g extends continuously to X by taking value α on every point of S_A and β on every point of S_B.

**Proof.** All pairs in A (respectively B) are inseparable and continuous maps to Hausdorff spaces identify inseparable points. Conversely, for each real open interval J, g^{-1}(J) is T-open; if it meets A, α∈J and the extension's preimage contains **all** of S_A; similarly for B. Therefore the extension is continuous.

**Caution:** Restriction C(X,R)→C(T,R) is **not injective**. A continuous function on X may have nonconstant values on S_A converging to α and on S_B converging to β. The proposition asserts existence of constant extensions, not unique extensions. In fact continuous f correspond to g∈C(T,R) constant separately on A,B and two real sequences tending to the respective constants.

**Proposition 4.2 (working).** If A,B are not completely separated by a real continuous function on T, then each a∈A, b∈B satisfies

    a U̸ b,    but a F b.

**Proof.** Their X-open neighborhoods can be chosen with disjoint closures (§3). If some real map f:X→R distinguished a and b, f|T would be constant on A and on B with different constants, completely separating the two closed subsets in T; contradiction.

Conversely, if A,B are completely separated in T, extend a separator by Proposition 4.1. Every two points in distinct classes other than A,B are also separated by real maps: T is completely regular, so a T-point outside A∪B can be separated from the closed set A∪B and from any other prescribed different T-point by continuous [0,1] functions that vanish on A∪B, which extend as above; an added point s is clopen, so its characteristic function separates it from everything else. Thus the **exact F-equivalence classes** are the I/U-classes, except that when A,B are not completely separated, F merges the two classes A,B into one.

**Localic comparison.** X is strongly locally compact and sober. Hence the frame coproduct O(X)⊗O(X) is spatial and canonically O(X×X) for the usual product. The I,U,F are **closed** sublocales, so equality of the point relations implies equality of their localic closed sublocales. If A,B are not completely separated, the relation difference on points proves F strictly larger without invoking any localic product spatiality. Therefore

    I(X)=U(X) ⊊ F(X)

holds in the originally defined locale sense.

## 5. Algebraic strengthening and a compact-open obstruction

**Proposition 5.1 (working).** If T has a basis of **compact open subsets**, then so does X; therefore **O(X) is algebraic**, not merely continuous.

**Proof.** For t∈T\(A∪B), choose a compact open T-neighborhood K avoiding A∪B and contained in a given X-open O. Then K is compact open in X. For t∈A choose compact open K⊆O∩T containing t, disjoint from B, and append a cofinite tail S_A^N⊆O: the set K∪S_A^N is X-open, contained in O, and compact because K and {t}∪S_A^N are compact. Similarly for t∈B. At each new point s, {s} is compact open. Thus compact open X-neighborhoods form a basis.

**Explicit compact opens in the deleted plank.** Let

    T=([0,ω1]×[0,ω])\{(ω1,ω)},
    A={ω1}×[0,ω),      B=[0,ω1)×{ω}.

All intervals below are in the order topology. T is locally compact zero-dimensional with a compact-open basis. For any α<ω1 choose

    K_A=(α,ω1]×{0},       K_B={0}×(m,ω]    (m∈N),
    u=K_A∪S_A^N,          v=K_B∪S_B^M.

These K_A,K_B are compact clopen in T, disjoint from each other and respectively from B,A. Both u,v are **compact open in X** and their closures are disjoint:

    cl_X(u)=K_A∪A∪S_A^N,
    cl_X(v)=K_B∪B∪S_B^M.

(The displayed unions are understood as subsets of X and are closed under the closure formula.)

Therefore, in L=O(X),

    u≪u, v≪v,  u*∨v*=1,  but  u not≺≺v*.

**Even one interpolation fails.** Suppose there is a c∈L with u≺c≺v*. In spatial terms u≺c means cl_X(u)⊆c, so **A⊆c∩T**. The second inequality means cl_X(c)⊆X\cl_X(v), so **cl_T(c∩T)∩B=∅**. Thus the T-open sets c∩T (neighborhood of A) and T\cl_T(c∩T) (neighborhood of B) are disjoint, contrary to the plank's nonnormality. Hence no such c exists.

**Conclusion:** The subfitness hypothesis does not restore the desired implication even among **algebraic** frames, with an obstruction already witnessed by compact open elements. The example is noncoherent: since it is noncompact, 1 is not compact, so there is no conflict with our earlier coherent-frame positive theorem.

## 5½. Relation to non-Hausdorff cones: an explicit open quotient

A colleague's independent literature search recognized the original *single-tag* construction as an **adjunction of two non-Hausdorff cones**. This observation is correct, with the caveat that literature often uses the *opposite apex convention*.

For a closed set A, let C_+(A)=A⊔{p_A}, with the opens ∅ and U∪{p_A} for U open in A. Thus {p_A} is open and cl{p_A}=A∪{p_A}. Then the original two-tag X_old is the topological pushout

    X_old = T ∪_A C_+(A) ∪_B C_+(B).

The present new construction has an **exactly parallel pushout** presentation. Set C_ω(A)=A⊔S_A where S_A is countably infinite, each point of S_A is isolated, and U⊆C_ω(A) is open iff U∩A is open and whenever U∩A≠∅, U includes all but finitely many members of S_A. Then

    X_new = T ∪_A C_ω(A) ∪_B C_ω(B).

For A={a}, C_+(A) is the Sierpiński space (open apex) whereas C_ω(A) is the usual compact convergent sequence ω+1. For multiple a∈A the SAME sequence S_A converges to all points of A; this produces T1 inseparability without any nontrivial specialization order.

**Proposition (new→old open quotient).** There is a canonical **continuous open surjective quotient map**

    q:X_new→X_old

equal to the identity on T, mapping every s∈S_A to p_A and every s∈S_B to p_B.

**Proof.** For a subset W⊆X_old, the inverse image q^-1(W) is open in X_new iff W is open in X_old: restriction to T matches, and an entire cloud is included in q^-1(W) exactly when its tag belongs to W, so the cofinite implication is equivalent to the corresponding old one. Thus q is quotient (and continuous). If U is open in X_new, q(U)∩T=U∩T is T-open. If U∩T meets A, then U contains a cofinite tail S_A and q(U) contains p_A, similarly for B. Therefore q(U) is old-open: q is open. □

**The quotient map is not closed** whenever A is nonempty: each isolated cloud point s∈S_A is also closed (X_new is T1), but q({s})={p_A} is not closed in X_old, since cl_X_old({p_A})=A∪{p_A}.

The map q shows the new example is an **open, nonclosed T1 resolution** of the old tag topology. This is an exact topological relationship, not merely an analogy, but it does not claim a standard named construction.

**Terminology and history.** McCord, Barmak and Minian, and J. P. May discuss non-Hausdorff cones/suspensions or mapping cylinders, mostly with the opposite convention (apex closed, not open); see J. P. May, *Finite Spaces and Larger Contexts* (draft), §3.4, https://math.uchicago.edu/~may/FINITE/FINITEBOOK/FINITEBOOKCollatedDraft.pdf . This does not establish that our specific two-tag plank or cofinite-cloud nonnormality-to-function-separation construction was previously used. Furthermore, C_ω({a})=ω+1 is disconnected and not contractible, while C_+({a}) is contractible. Thus the homotopy-theoretic remarks about non-Hausdorff cones do **not** simply transfer to the cofinite-cloud construction.

## 5¾. Crowded algebraic subfit examples via a Cantor factor

**Proposition (stability of point relations).** For any topological space X and any completely regular Hausdorff Y, for R∈{I,U,F} regarded as relations on ordinary points,

    ((x,y),(x',y')) ∈ R(X×Y) ⇔ (x,x')∈R(X) and y=y'.

**Proof.** When y≠y', a continuous real function Y→R distinguishes y and y'; such a function also separates their neighborhoods by disjoint closures (because Y is completely regular Hausdorff). When y=y', I and U are reflected by slices: any basic product neighborhoods U×V,U'×V' have common second-coordinate point y; intersection (respectively intersection of closures) is nonempty iff the corresponding first-coordinate neighborhoods intersect (respectively have intersecting closures). Conversely, disjoint first-coordinate neighborhoods or neighborhoods with disjoint closures lift via products. For F, restrictions of continuous real functions X×Y→R to X×{y} are real functions on X, while any real function on X lifts along projection X×Y→X. □

Let C=2^N be the ordinary Cantor set, and let X be the cofinite-cloud counterexample constructed over the deleted Tychonoff plank. Put Z=X×C.

**Corollary (crowded strengthening).** Z is **T1, crowded (no isolated points), strongly locally compact, sober**, and O(Z) is **algebraic and subfit**, yet

    I(Z)=U(Z) ⊊ F(Z)

as closed localic relations.

**Proof.** T1 and absence of isolated points are immediate. Strong local compactness follows by taking compact neighborhoods inside basic open rectangles (finite products of compact sets are compact). For sobriety, if H⊆X×C is nonempty irreducible closed, its projection to Hausdorff C has irreducible closed closure and thus is contained in one singleton {c}; consequently H⊆X×{c}, where irreducible closed subsets are singletons because X is sober. Products of compact open bases give a compact open basis in Z, hence O(Z) is algebraic. T1 implies subfitness. The point-relation formula transfers I=U⊊F from X to Z: an F-but-not-U pair (a,b) in X gives ((a,c),(b,c)) for any c∈C. Because Z is strongly locally compact and sober, the localic product Z×Z agrees with the ordinary product and is spatial; closed localic relations are detected by point sets. □

**Compact open witnesses still work:** let u,v⊆X be the compact opens with u*∨v*=1 but no c satisfying u≺c≺v*. Choose nonempty clopen V⊆C and set U=u×V, W=v×V. Both are compact open, their closures are disjoint, hence U*∨W*=1, but they admit no intermediate open d with U≺d≺W*: slicing d at a point of V would yield c with u≺c≺v* (since closure in a closed slice is contained in the ambient closure). So the strong noninterpolation survives stabilization.

**Interpretation.** Isolated points are an optional *presentation device*, not an essential ingredient of this failure. This is a formal product stabilization, rather than an independent counterexample mechanism, and makes no new priority claim.

## 6. Conceptual significance and caveats

- This is a much sharper result than the original two-*tag* construction: **T1 itself**, not just subfitness, does not prevent the continuous-frame obstruction.
- The countably infinite isolated tails are used to force points of A to be mutually inseparable **without a common generic tag point**; in contrast to the tags, every new point is closed.
- The original nonnormality of T prevents any continuous real map from distinguishing A and B as classes, though they are Urysohn-separated **point by point** in X.
- The exact priority of this topology (a “cofinite cloud” attached to a closed set) and whether this result is implicit in established topology is **unexamined**. The proof is a new *working argument* and should receive an independent adversarial check before publication.
- Our prior coherent/compact/kω/paracompact positive theorems are unaffected. The plank is a closed subspace of X, hence X remains non-σ-compact and nonparacompact.
- **Caution regarding compactness:** The compact-open neighborhoods meeting A contain a cofinite tail S_A; they need **not** be closed, even though X is T1. This is why compact open witnesses do not automatically imply coherence or regularity.

## References

- P. J. Cameron and V. Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783 (2026).
- J. Picado and A. Pultr, *Separation in Point-Free Topology* (2021), especially subfitness and Hofmann–Lawson duality.
- C. H. Dowker and Dona Papert, *On Urysohn's Lemma* (1967), for completely separating disjoint closed subsets in a normal frame.
- Classical deleted Tychonoff plank, e.g. Steen–Seebach, *Counterexamples in Topology*.
- R. N. Ball, J. Picado, A. Pultr, *On an Aspect of Scatteredness in the Point-Free Setting*, *Portugaliae Mathematica* **73** (2016), 139–152, for the subfitness axiom and its meaning in ordinary topological spaces (https://ems.press/content/serial-article-files/44773).
