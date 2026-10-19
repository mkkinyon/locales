# A — Counterexample in a continuous frame: I=U does not imply U=F

**18 October 2026. Status: working proof, explicit counterexample; no priority claim.** This **settles negatively** the unrestricted continuous-frame question previously left open in [A-continuous-frames.md](A-continuous-frames.md), [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md), [A-beyond-countable-exhaustion.md](A-beyond-countable-exhaustion.md), and [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md). The counterexample is locally compact and sober; it uses the deleted Tychonoff plank, so genuinely uncountable global nonnormality drives the phenomenon.

## 1. General two-tag construction

Let T be a **locally compact Hausdorff** space, and let A,B⊆T be **disjoint closed** subsets. Form the set

    X = T ⊔ {p_A,p_B}.

Define the topology as follows: a subset O⊆X is open precisely if

    V=O∩T is open in T;
    if V∩A≠∅, then p_A∈O;
    if V∩B≠∅, then p_B∈O.

The tags p_A,p_B may be included independently when the corresponding requirement does not force them. In particular, each singleton {p_A},{p_B} is open.

These conditions define a topology: arbitrary unions and finite intersections preserve them. The subspace topology on T is its original topology, and T is **closed** in X since {p_A,p_B} is open.

For any open O of X, with V=O∩T, the following closure formula is useful:

    cl_X(O) ∩ T = cl_T(V)
                         ∪ (A if p_A∈O, otherwise ∅)
                         ∪ (B if p_B∈O, otherwise ∅);

and p_A∈cl_X(O) iff p_A∈O (likewise p_B), because the tag singletons are open. In particular,

    cl_X({p_A})=A∪{p_A},
    cl_X({p_B})=B∪{p_B}.

### Proposition 1.1: Local compactness and sobriety

**Proposition (proved).** X is a **locally compact, sober, T0** space. In particular O(X) is a **continuous frame** in classical mathematics.

**Proof of local compactness.** At a tag p_A or p_B, its singleton is a compact open neighborhood. Let t∈T and let O be any open neighborhood. Choose a T-open V containing t, with compact K in T satisfying t∈V⊆K⊆O∩T; additionally, shrink V and K to avoid A if t∉A, and to avoid B if t∉B (possible since A,B are disjoint closed and T is locally compact Hausdorff). Define

    N = V ∪ {p_A if t∈A} ∪ {p_B if t∈B},
    H = K ∪ {p_A if t∈A} ∪ {p_B if t∈B}.

The avoidance choices make N open in X; H is compact as a finite union of compact subsets, and t∈N⊆H⊆O. This proves the strong neighborhood-wise compact-containment version of local compactness.

**Proof of sobriety.** The space is T0: T is Hausdorff, tags are open singletons, and ordinary t∈T is distinguishable from each tag. Let C be a nonempty irreducible closed subset of X. If p_A∈C, the nonempty relatively open set {p_A} is dense in the irreducible space C, so C=cl_X({p_A})=A∪{p_A}. Similarly, if p_B∈C, then C=B∪{p_B} (and both tags cannot belong to one irreducible closed C). If C contains no tag, then C is a closed irreducible subset of the Hausdorff space T, hence a singleton. In every case it has a unique generic point. □

### Proposition 1.2: Exact inseparability and Urysohn relations

**Proposition (proved).** The nontrivial inseparability classes in X are precisely

    A∪{p_A} and B∪{p_B},

with every point of T\(A∪B) forming a singleton class, and

    I(X)=U(X)

as point relations.

**Proof of I classes.** Every open neighborhood of any a∈A contains p_A. Thus every a∈A is inseparable from p_A and from every other a'∈A. Similarly B∪{p_B}. Conversely, two T-points in different proposed classes admit disjoint T-open neighborhoods whose tag requirements do not introduce a common tag: use the Hausdorff property of T and the fact A,B are disjoint closed. The same applies to a tag versus any ordinary point outside its class; a tag itself has its open singleton neighborhood. Thus there are no other inseparable pairs.

**Proof of U=I.** We must show that every two **inequivalent** points have open neighborhoods with **disjoint closures**.

If the points are p_A and p_B, use their open singleton neighborhoods; their closures are disjoint since A∩B=∅.

For p_A versus t∈T\A, use {p_A} and a neighborhood of t derived from a T-open V with cl_T(V)∩A=∅. If t∈B, take O_t=V∪{p_B}, with cl_T(V) additionally chosen disjoint from A; otherwise take V disjoint from A∪B. By the closure formula, cl_X(O_t) avoids A∪{p_A}. The case with p_B is symmetric.

For inequivalent t,s∈T, local compactness and regularity of T permit choosing T-open V_t,V_s with disjoint closures, and with cl(V_t) avoiding any of A,B that do not contain t, and cl(V_s) avoiding any of A,B that do not contain s. Because the classes differ, the sets of required tags at t and s are disjoint. Put

    O_t=V_t∪{p_A if t∈A}∪{p_B if t∈B},
    O_s=V_s∪{p_A if s∈A}∪{p_B if s∈B}.

The tag-avoidance choices make these open, and their closures are disjoint by the closure formula. Thus inequivalent points are Urysohn-separated. Since I⊆U always, equality follows. □

**Important subtlety.** The closed sets A∪{p_A} and B∪{p_B} are disjoint; the open singleton tag neighborhoods have these two disjoint **closures**. This does *not* provide disjoint open neighborhoods of A and B **inside T**, since the tags' neighborhoods need not contain any other members of A or B. Thus the nonnormality of T is fully compatible with I=U on X.

### Proposition 1.3: When the functional relation is strictly larger

Every continuous map f:X→R is constant on A∪{p_A} and separately on B∪{p_B}, since a continuous map to a Hausdorff space is constant on inseparability classes.

Therefore if f(p_A)≠f(p_B), the restriction f|_T would be a continuous function taking distinct constant values on the disjoint closed sets A and B. Such a function would separate A and B by disjoint open neighborhoods in T.

**Proposition (proved).** If A and B cannot be separated by disjoint open neighborhoods in T, then

    p_A F p_B,   but p_A not U p_B,

so

    I(X)=U(X) ⊊ F(X).

This strictness is first a statement about ordinary pairs of points. Since X is locally compact sober, the canonical frame coproduct O(X)⊗O(X) agrees with the frame of opens of the ordinary product X×X; all our relations are **closed sublocales**. Thus the same strict inclusion holds for the original **localic relations**.

### Optional sharpening: functional equivalence of the two tags

The criterion is exact for the *particular pair* (p_A,p_B):

    p_A not F p_B ⇔ A and B are completely separated in T.

The reverse direction uses a continuous T→[0,1] taking values 0 on A and 1 on B; it extends continuously to X by assigning the corresponding values at p_A,p_B. Continuity is easily checked using the open-set definition (if f(t)=f(p_A) for every t∈A, a preimage neighborhood of a that meets A contains p_A automatically; likewise B).

Because T is locally compact Hausdorff (hence completely regular), one can also show:

    I(X)=U(X)=F(X)  ⇔  A,B are completely separated in T.

For the ⇐ implication, use a function separating A,B for their two tags; for a point t∈T\(A∪B) versus any other class, use continuous [0,1] functions vanishing on the closed set A∪B and distinguishing t, or use a suitable combination of such a function with the A/B separator. These extend to X (being constant separately on A and B). No other functional pairs arise. This supplies a precise embedding of the failure of normality of T into our separation-hierarchy problem.

## 1½. A cleaner structural description: function ring, quotient, and exact F classes

The following sharpening makes the obstruction almost formal once the topology has been checked. Throughout assume A,B are **nonempty**.

**Proposition (real maps).** Restriction to T is an isomorphism of rings

    C(X,R) ≅ {g∈C(T,R): g|A is constant, g|B is constant}.

**Proof.** Every a∈A is inseparable from p_A, so any continuous map from X to a Hausdorff space takes the same value on A∪{p_A}; likewise B∪{p_B}. Conversely, if g:T→R has values α on A and β on B, extend it by g(p_A)=α, g(p_B)=β. For an open interval W in R, g^{-1}(W)∩T is open; if it meets A, it includes p_A, and similarly for B. Thus the extension is continuous. The two constructions are inverse, and preserve ring operations. □

**Proposition (exact functional classes).** If A,B are completely separated in T, F=I=U. Otherwise the *only additional F-identifications* are those between the two classes

    E_A=A∪{p_A},    E_B=B∪{p_B}.

That is, if A and B are not completely separated, the F-equivalence classes are E_A∪E_B and the singletons {t}, t∈T\(A∪B). Equivalently, as **closed sublocales** of the spatial localic product,

    F = U ∪ (E_A×E_B) ∪ (E_B×E_A).

**Proof.** The real-map characterization shows that any g separates the classes E_A,E_B exactly when A,B are completely separated in T; otherwise all real maps give them the same value. For t∈T\(A∪B) and any other class, completely regularity of T gives a continuous g:T→[0,1] that is 1 at t and 0 on the closed set A∪B (and, when needed, another selected point s≠t). It extends to X. Thus no distinct classes other than E_A,E_B are functionally identified. The full relations are closed and X×X is spatial, so the point description yields the claimed equality of closed sublocales. □

**Proposition (the quotient is the double pinching of T).** Let E=I=U be the inseparability equivalence relation on points. Then

    Q=X/E ≅ T/(A∼one point, B∼a second point).

The restriction q_T:T→Q of the quotient map q:X→Q is itself a **closed quotient map**, and q:X→Q is **closed** as well.

**Proof.** The E-classes are E_A, E_B, and the remaining singletons. A subset W of the set of classes has q^{-1}(W) open in X iff its intersection V=q_T^{-1}(W) with T is open in T: one direction follows by restriction; conversely, V is saturated for the A/B collapsing and therefore contains either all or none of A and B. Adding p_A iff A⊆V, and p_B iff B⊆V, makes q^{-1}(W) open. This is precisely the standard quotient topology for T with A,B separately collapsed. For a closed C⊆X, its E-saturation adds at most E_A and E_B, each of which is closed in X, so E[C] is closed and q(C) is closed. The same argument in T proves q_T closed. □

All equivalence classes in T are closed, so **Q is T1**. If A,B have no disjoint open neighborhoods in T, then the two collapsed points of Q have no disjoint neighborhoods either, so **Q is not Hausdorff**. The map q:X→Q is nevertheless **closed**. This makes precise why a closed quotient of a strongly locally compact sober X need not yield a Hausdorff separation quotient.

A convenient summary of the whole two-tag mechanism is:

    pairwise Urysohn separation of E-classes in X
                  does not imply
    Hausdorff/functional separation of their images in Q.

**Corollary (normality detected by every two-tag extension).** For a locally compact Hausdorff T,

    T normal
      ⇔  for every disjoint nonempty closed A,B⊆T,
          the associated two-tag X has I=U=F.

This follows from the exact F-class proposition and the classical Urysohn lemma. This is just a reformulation, **not a proposed new normality theorem**.

**Additional facts.** If A,B are not completely separated, neither can be compact: every compact subset of a completely regular Hausdorff space is completely separated from a disjoint closed subset. Hence E_A and E_B are **noncompact closures of compact open singleton tags**. Also the frame O(X) is **not subfit**: take a={p_A}, b=0. If a∨w=1 for an open w, then w contains all of T (in particular A), forcing p_A∈w and hence w=1. Thus no w satisfies a∨w=1 while b∨w≠1. The relevance of imposing subfitness on future counterexamples is open.

## 2. The deleted Tychonoff plank gives explicit uncountable A,B

Take

    P=([0,ω₁] × [0,ω]) \ {(ω₁,ω)}

with the product order topology, where ω₁ is the first uncountable ordinal and ω is the first infinite ordinal.

P is an **open subspace of a compact Hausdorff space**, so is locally compact Hausdorff and sober. Define its "right edge" and "top edge":

    A={ω₁}×[0,ω),       B=[0,ω₁)×{ω}.

These subsets are closed in P and disjoint. They have **no disjoint open neighborhoods**, by the standard deleted-plank argument:

If V⊇A is open, then for each n<ω there is an ordinal α_n<ω₁ with

    (α_n,ω₁]×{n} ⊆ V.

Since a countable set of countable ordinals is bounded in ω₁, α=sup_n α_n<ω₁. Thus

    (α,ω₁]×[0,ω) ⊆ V.

Any open W containing B contains (β,ω) for β∈(α,ω₁), and consequently (β,n) for all sufficiently large finite n. Hence W intersects V, contradicting disjointness.

This is the standard nonnormality witness for the deleted Tychonoff plank. References: Steen–Seebach, *Counterexamples in Topology*; [MathOverflow discussion (Andreas Blass)](https://mathoverflow.net/questions/53300/locally-compact-hausdorff-space-that-is-not-normal); [Tychonoff plank](https://en.wikipedia.org/wiki/Tychonoff_plank). The exact elementary argument is included here.

Apply the two-tag construction to (P,A,B). Denote the result by X.

**Theorem 2.1 (proved, working).** X is locally compact, sober, noncompact, not σ-compact, and not paracompact, and

    I(X)=U(X) ⊊ F(X)

as closed localic relations. Equivalently, the **continuous frame** L=O(X) has I(L)=U(L)≠F(L).

**Non-σ-compactness and nonparacompactness.** P is a closed subspace of X. Its closed subset B is homeomorphic to [0,ω₁), which is not σ-compact; hence X cannot be σ-compact (a closed subspace of a σ-compact space is σ-compact). If X were paracompact in the open-refinement sense, its closed subspace P would be paracompact; since P is Hausdorff, regular, this would imply P normal, contradiction. Thus the example evades both previous positive theorems exactly as it must.

**Why the example is instructive.** Our earlier kω/σ-compact proof constructed real functions by extending through a *countable* family of compact Hausdorff quotients. In this X, A and B are closed noncompact, and their failure of normal separation exploits the regular uncountable cofinality of ω₁. The added points turn global nonnormality into a pairwise functional-separation obstruction that cannot be seen from any one compact neighborhood.

## 3. The failed stable-interpolation lemma, precisely located

Let u={p_A}, v={p_B}, and a=u, b=v. These are **compact opens**, hence

    u≪a, v≪b,

and

    a*∨b*=1,

since cl_X(a)=A∪{p_A}, cl_X(b)=B∪{p_B} are disjoint. But u and v are **not completely separated**, because f(p_A)=f(p_B) for every continuous f:X→R. In frame notation,

    u ≺ v*,        but u ⊀≺ v*.

Indeed, there cannot be **even one intermediate** c with

    u≺c≺v*.

For if u≺c, then cl(u)=A∪{p_A}⊆c, so c contains all of A as well as p_A. If c≺v*, then cl(c)⊆v*=X\(B∪{p_B}), so c is disjoint from B. Thus c∩P is an open neighborhood of A disjoint from B; and the stronger closure condition forces a neighborhood of B disjoint from c∩P, yielding disjoint open neighborhoods of A,B in P, contradicting nonnormality.

Even more directly, c≺v* implies cl(c) disjoint B; hence c is an open neighborhood of A and P\cl(c) is an open neighborhood of B, disjoint from c.

This is a **counterexample to the exact relative stable-buffer conjecture** in [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md), even with compact initial opens u,v and compact outer opens a,b. By the continuous-frame characterization, it is simultaneously a counterexample to the unrestricted implication I=U⇒U=F.

The two disjoint closed saturated buffers E[cl(u)]=A∪{p_A} and E[cl(v)]=B∪{p_B} already exist. What fails is **opening** the buffers while retaining disjointness: doing so would force normal separation of A,B.

## 4. What this resolves and what remains of interest

**Resolved negatively:** For arbitrary continuous frames, I=U does NOT imply U=F. Even transitivity of I does not force I=F.

**Previously proved positive subclasses remain valid:**
- compact continuous frames;
- coherent frames;
- locally compact σ-compact sober spaces (and more generally kω);
- locally compact paracompact sober spaces;
- locally compact sober spaces with an open inseparability quotient;
- locally compact σ-compact sober spaces with closed inseparability saturation (now subsumed by the σ-compact result).

**New general mechanism:** Every locally compact Hausdorff nonnormal T has closed A,B which are not completely separated, and the two-tag construction produces a locally compact sober continuous-frame counterexample. Conversely, for a fixed pair of closed A,B the two-tag X has equality of all three relations exactly when A,B are completely separated in T.

**Possible follow-up questions:**
1. Is there a recognizable, intrinsically frame-theoretic condition weaker than compactness or paracompactness that excludes the two-tag obstruction?
2. Does a related obstruction occur for continuous frames satisfying a separation axiom stronger than mere T0 sobriety or with no isolated open points?
3. Is this two-tag construction standard in the literature under another name (e.g. forcing inseparability classes with open generic points)? Do a priority/literature check before proposing publication.
4. Can the construction be modified to give a locally compact **T1** counterexample? The tags in this X are not closed, so the example is T0 sober but not T1. This is not required for the continuous-frame result, but would strengthen the topology.

## References

- P. J. Cameron and V. Kumar, *Graphs on topological spaces*, arXiv:2610.14783 (2026); pointwise relations motivating this project.
- J. Picado and A. Pultr, *Separation in Point-Free Topology*, Birkhäuser, 2021.
- Steen and Seebach, *Counterexamples in Topology* (deleted Tychonoff plank).
- [MathOverflow: A locally compact Hausdorff space that is not normal](https://mathoverflow.net/questions/53300/locally-compact-hausdorff-space-that-is-not-normal), answer by Andreas Blass.
- [Tychonoff plank overview](https://en.wikipedia.org/wiki/Tychonoff_plank).
