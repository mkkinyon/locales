> **DECISIVE UPDATE (18 October 2026):** The **unrestricted** continuous-frame implication is **false**. See [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md): adjoining two nonclosed isolated tags to disjoint nonnormally separable closed subsets of a locally compact Hausdorff space (explicitly the deleted Tychonoff plank) gives a locally compact sober space with **I=U⊊F**, even for a far pair of *compact opens*. This supersedes any unresolved-status or conjectural statement below. Positive conclusions under compactness, sigma-compactness/kω, paracompactness, or quotient hypotheses remain valid.

> **Subsequent extension (18 October 2026):** The countable exhaustion can be dropped globally for locally compact spaces that are **paracompact in the non-Hausdorff open-refinement sense**. Such spaces decompose into arbitrarily many clopen sigma-compact pieces, to which the k-omega theorem below applies separately. A locally countable sigma-compact open cover is another sufficient hypothesis. Full proof: [A-beyond-countable-exhaustion.md](A-beyond-countable-exhaustion.md). The unrestricted case is **false**, as shown by the deleted-plank construction cited in the preceding update.

# A — Compact exhaustion and stable interpolation on kω spaces

**Research note, 18 October 2026.** Status: rigorous working proof of a positive implication for **locally compact σ-compact** spaces (more generally kω spaces), with no closed/open-saturation hypothesis. No priority claim: standard facts about kω direct limits of compact Hausdorff spaces already imply normality of the quotient. This note responds to the search for noncompact intermediate neighborhoods in [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md).

## 1. The topological theorem

Let X be a topological space and let E=cl(Δ_X)⊆X×X, the inseparability relation.

**Theorem 1 (proved, working).** Suppose X is a **kω space**: there are increasing compact subspaces K_1⊆K_2⊆⋯ with union X, and a subset A⊆X is closed iff each A∩K_n is closed in K_n. If E is an equivalence relation, then the quotient Q=X/E is **normal Hausdorff** (indeed admits continuous [0,1]-valued separation of any disjoint closed sets). Consequently

    E=F,

where F denotes equality of all continuous real-valued functions on X.

No sobriety or local compactness is required for this point-set result. In particular **the hypothesis E=U is stronger than necessary**: it implies transitivity of E, so it implies E=F under the kω hypothesis.

**Proof.** E is closed by definition. For each compact K⊆X the saturation E[K] is closed in X, by projection of the closed subset E∩(K×X) along the compact factor. Consequently q(K) is closed in the quotient Q.

Let Q_n=q(K_n). Each Q_n is closed in Q. If C is closed in K_n then C is compact, E[C] is closed in X, and q(C) is closed in Q. Hence the surjection

    q|K_n : K_n → Q_n

is a **closed quotient map**. It has kernel E∩(K_n×K_n), a closed equivalence relation on compact K_n. The quotient of a compact (not necessarily Hausdorff) topological space by a closed equivalence relation is compact Hausdorff. Thus Q_n is compact Hausdorff, with Q_n closed in Q_{n+1}.

The quotient Q has the **final topology of the sequence** (Q_n). Indeed, if V⊆Q has V∩Q_n open in Q_n for all n, then q^(-1)(V)∩K_n is open in K_n for every n, so q^(-1)(V) is open in X by the defining kω property; hence V is open in Q. The converse is automatic.

Thus Q is an increasing direct limit of compact Hausdorff subspaces with closed inclusions.

To prove Q normal, let C,D⊆Q be disjoint closed subsets. Choose a continuous f_1:Q_1→[0,1] with f_1(C∩Q_1)=0 and f_1(D∩Q_1)=1 (compact Hausdorff Q_1 is normal). Given f_n with these properties, the subset

    A_n = Q_n ∪ (C∩Q_{n+1}) ∪ (D∩Q_{n+1})

is closed in Q_{n+1}. Define g on A_n as f_n on Q_n, 0 on C∩Q_{n+1}, 1 on D∩Q_{n+1}. These agree on intersections and give a continuous function by the finite closed pasting lemma. Tietze's theorem extends g to continuous f_{n+1}:Q_{n+1}→[0,1]. The compatible f_n define f:Q→[0,1], continuous by the final topology, separating C and D. In particular Q is normal T1, hence functionally Hausdorff.

Finally, any continuous f:X→R is constant on E-related points, because distinct real values admit disjoint inverse-image neighborhoods in X. Such an f factors uniquely through q, and the separating functions on Q show that no larger pair lies in F. Hence E=F. □

**Reference/priority warning.** Normality of Hausdorff kω-spaces, and compatible extensions along increasing compact Hausdorff stages, are established topology (e.g. Franklin–Smith Thomas, *A survey of kω-spaces*, *Topology Proceedings* **2** (1977), 111–124; see also the construction in [MathOverflow/MSE discussion](https://math.stackexchange.com/questions/3687619/the-direct-limit-of-a-sequence-of-compact-normal-spaces-is-regular)). The present proof is included rather than assumed because we need the exact non-Hausdorff quotient hypotheses. We do not claim novelty.

## 2. Locally compact σ-compact spaces are kω

**Lemma 2 (proved; point-set).** Suppose X is **weakly locally compact**, meaning each point has at least one compact neighborhood, and σ-compact. Then X is kω. This does **not** imply that O(X) is a continuous frame.

**Proof.** Write X=⋃_n C_n with each C_n compact. Every compact C_n can be covered by finitely many open sets whose closures are not required to be compact but which lie in compact neighborhoods; taking the finite union of those compact neighborhoods gives compact L_n with C_n⊆int(L_n). Put

    K_n=L_1∪⋯∪L_n.

The K_n are compact and increasing, and their interiors cover X.

To show the weak topology property, suppose A⊆X has A∩K_n closed in K_n for every n. Let x∉A and choose n with x∈int(K_n). Since A∩K_n is closed in K_n, there is an ambient open neighborhood V of x with V∩K_n∩A=∅. The open neighborhood V∩int(K_n) of x misses A. Thus A is closed. □

**Corollary 3 (proved).** For every **locally compact σ-compact space** X,

    I(X)=U(X)  ⇒  I(X)=U(X)=F(X)

as point relations.

Indeed, I=U makes E=I transitive by [A-coherent-implication.md](A-coherent-implication.md), Lemma 1, and Theorem 1 yields E=F.

**Corollary 4 (closed localic relations; corrected).** If, moreover, X is **strongly locally compact and sober**, meaning every open neighborhood contains a compact neighborhood (equivalently, O(X) is continuous for sober X), then the point-set equality lifts to equality of the closed localic sublocales of Loc(X)×Loc(X). Here the localic product agrees with the ordinary spatial product. **Weak local compactness plus sobriety alone does not justify the lift.**

This settles the continuous-frame implication for σ-compact locally compact sober spaces without requiring quotient openness, quotient closedness, or properness of E-saturation.

## 2a. A genuine stable noncompact intermediate-neighborhood lemma

The proof of Theorem 1 gives more than separation of *points*.

**Corollary 4a (proved).** Let X be a kω-space and E⊆X×X a closed equivalence relation. If K,H⊆X are compact and E[K]∩E[H]=∅, then there exists an **E-invariant** continuous function

    f:X→[0,1],   f|K=0,   f|H=1.

**Proof.** By closed compact saturation, q(K),q(H) are disjoint *closed* subsets of the normal Hausdorff quotient Q=X/E. Separate them by a function g:Q→[0,1] with g|q(K)=0, g|q(H)=1; put f=g∘q. □

**Stable interpolation in the continuous-frame problem.** Let X be **strongly** locally compact σ-compact sober with I=U. Suppose a,b∈O(X) have disjoint closures, and u≪a, v≪b. Choose compact K,H with u⊆K⊆a and v⊆H⊆b. Since E=I is transitive and no point of a is E-related to a point of b, E[K]∩E[H]=∅. The corollary produces f=0 on u and f=1 on v.

For dyadic t∈(0,1), set

    c_0=u,   c_t=f^{-1}([0,t)),   c_1=v* = X\cl(v).

These are open in X and satisfy

    cl(c_s)⊆c_t whenever 0≤s<t≤1.

For s=0, use f=0 on u and continuity to obtain cl(u)⊆f^{-1}({0}); for 0<s<t<1, use cl(f^{-1}([0,s)))⊆f^{-1}([0,s]); for t=1, use f=1 on v, hence on cl(v). Therefore this is the desired **stable dyadic rather-below scale**.

**Crucial qualification:** The intermediate opens c_t need not be compactly contained; in the split-real-line example they cannot be. The countable compact exhaustion supplies **compatible separating functions**, not compact intermediate neighborhoods.

This is a genuine positive noncompact intermediate-neighborhood lemma with a clearly identified global hypothesis. Its extension to arbitrary non-kω spaces is **false** without additional hypotheses; the two-tag deleted-plank example supplies the counterexample.

## 3. The promised noncompact closed-buffer lemma

Let E=I be an equivalence relation on any topological space X. If u≪a in O(X), and X is locally compact sober, choose compact K with u⊆K⊆a. Since E[K] is closed, E-saturated and contains u,

    cl(E[cl(u)]) ⊆ E[K] ⊆ cl(a).

Indeed cl(u)⊆E[K] because E[K] is closed; equivalence gives E[cl(u)]⊆E[K]; and E[K]⊆cl(a) because every neighborhood of an E-partner of k∈K⊆a meets a. Hence for a,b with cl(a)∩cl(b)=∅ and u≪a,v≪b, there are **disjoint closed E-saturated, possibly noncompact buffers**

    E[K]⊆cl(a), E[H]⊆cl(b),

containing cl(u),cl(v), respectively.

These closed buffers are valuable but *not alone* an interpolation theorem: in general their open neighborhoods cannot be selected by a simple finite cover. In the σ-compact case, the kω/Tietze construction circumvents the need to build such nested open neighborhoods directly.

## 4. Limit of the result (historical investigation)

The unrestricted continuous-frame implication is now **refuted** by [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md). The following discusses the limitation of the compact-exhaustion method as it was understood before that construction.

Our proof uses a **countable exhaustion by compact subspaces** and compatible Tietze extensions. For a non-σ-compact space, there may be no such countable cofinal sequence. Naively extending along an uncountably long directed family of compact subsets is nontrivial: at limit stages there need not be a compact Hausdorff space containing all previous stages, and compatibility can fail without an independent extension mechanism.

**Subsequent resolution:** the general implication is indeed false. The deleted-plank construction shows exactly how a global obstruction can arise.

Further questions:
1. Can the kω/Tietze method be localized or extended using paracompactness, compactly generated coverings, or a different transfinite gluing principle?
2. Can we identify a smaller hypothesis than σ-compactness that ensures the quotient Q is functionally Hausdorff?
3. Are there locally compact sober spaces with E=I a closed equivalence but Q not functionally Hausdorff? Such an example must necessarily be **non-kω**.
4. Compare this construction with the primitive-ideal space setting: if σ-unitality implies suitable σ-compactness of Prim(A), then an Orc=1 counterexample there is ruled out independently of saturation closedness; verify the topological hypothesis before applying.

**Literature:** K. H. Hofmann and J. D. Lawson, continuous frames/locally compact sober representation; J. Picado and A. Pultr (2021), Chapter VI on complete-below scales; S. P. Franklin and B. V. Smith Thomas (1977), survey of kω-spaces; classical Tietze extension theorem.
