> **DECISIVE UPDATE (18 October 2026):** The **unrestricted** continuous-frame implication is **false**. See [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md): adjoining two nonclosed isolated tags to disjoint nonnormally separable closed subsets of a locally compact Hausdorff space (explicitly the deleted Tychonoff plank) gives a locally compact sober space with **I=U⊊F**, even for a far pair of *compact opens*. This supersedes any unresolved-status or conjectural statement below. Positive conclusions under compactness, sigma-compactness/kω, paracompactness, or quotient hypotheses remain valid.

# A — Noncompact intermediate-neighborhood lemmas: one positive result, two obstructions

**Research note, 18 October 2026.** Status: closed saturated noncompact buffers for genuine way-below pairs and elementary compact-pair separation proved; a strong proposed interpolation statement **disproved even in a compact, locally compact sober space with I=U=F**; no answer yet to the unrestricted continuous-frame implication. No originality claim. Background notes: [A-way-below-revisited.md](A-way-below-revisited.md), [A-stable-interpolation-test.md](A-stable-interpolation-test.md), [A-closed-saturation.md](A-closed-saturation.md).

Notation for a space X:

- xEy: no disjoint open neighborhoods; E=cl(Δ_X) inside X×X.
- xUy: no open neighborhoods with disjoint closures.
- xFy: all continuous real-valued maps agree.
- For K⊆X, E[K]={y:∃x∈K, xEy}.
- A≺B denotes cl(A)⊆B for opens A,B; in the frame O(X), equivalently A*∨B=1.
- A≺≺B denotes existence of a rational/dyadic ≺-interpolation scale, equivalently a continuous real function 0 on A and 1 on X\B.

The target remains: for continuous L, does I=U imply U=F? The **exact way-below tests** from [A-continuous-frames.md](A-continuous-frames.md) ask whether

    a*∨b*=1, u≪a, v≪b  ⇒  u≺≺v*.

The two parameters a,b matter greatly; **one must not replace this by** "u≺v*⇒u≺≺v*" for arbitrary u,v. That stronger statement is false even when I=U=F.

## 1. A positive compact-pair lemma (no global compactness)

**Lemma 1 (proved).** Let X be any topological space (not necessarily compact or sober), and let K,H⊆X be compact subsets. Assume that for every k∈K and h∈H, the pair (k,h) has open neighborhoods with disjoint closures. Then there are open A⊇K and B⊇H such that

    cl(A) ∩ cl(B) = ∅.

In particular, if I(X)=U(X), and E is the inseparability equivalence relation, it suffices to assume

    E[K]∩E[H]=∅.

**Proof.** For each k∈K and h∈H choose opens U_kh∋k, V_kh∋h with cl(U_kh)∩cl(V_kh)=∅. Fix k. Choose finitely many h_j such that H⊆⋃_j V_k,h_j, and put

    U_k=⋂_j U_k,h_j,     V_k=⋃_j V_k,h_j.

Then U_k is a neighborhood of k, V_k contains H, and cl(U_k)∩cl(V_k)=∅ (the latter uses finite union of closures). Choose finitely many k_i with K⊆⋃_i U_k_i and define

    A=⋃_i U_k_i,       B=⋂_i V_k_i.

Again, cl(A)∩cl(B)=∅. Empty K or H are trivial. □

**Corollary 2 (proved, genuinely noncompact buffers).** Under I=U and E[K]∩E[H]=∅, choose A,B as above. Then

    E[K]⊆cl(A),    E[H]⊆cl(B),

even if E[K] or E[H] is noncompact.

Indeed if k∈K⊆A and yEk, every neighborhood of y meets A, so y∈cl(A). Symmetrically for H.

This is a reasonable *weak noncompact-neighborhood lemma*: distinct E-saturations of compact cores admit **disjoint closed ambient buffers**, although those buffers need not be open neighborhoods of all partners, or themselves E-saturated.

No new continuous real-valued function follows from this lemma alone; further interpolation is required.


## 1a. The main positive result: closed, E-saturated, possibly noncompact buffers

**Lemma 2a (corrected scope, 20 October 2026).** Let E=cl(Δ_X) be an **equivalence relation** on a topological space X. Suppose **a compact K with u⊆K⊆a is given**, where u,a are opens. In particular such a K exists when X is **strongly locally compact** and u≪a. Then

    cl(E[cl(u)]) ⊆ E[K] ⊆ cl(a).

In particular E[K] is **closed and E-saturated**, and may be noncompact. There is no assumption that q:X→X/E is open or closed.

**Proof.** In a locally compact sober space, the way-below/compact-containment characterization gives compact K with u⊆K⊆a. More generally the same proof works whenever such a K has been supplied. Since E is closed in X×X, E[K] is closed: it is the image of E∩(K×X) under the projection K×X→X, a closed map for compact K (tube lemma). Because E is reflexive, u⊆K⊆E[K], and hence cl(u)⊆E[K]. Since E is transitive, E[cl(u)]⊆E[E[K]]=E[K]. Because E[K] is closed, its closure is also contained in E[K].

If zEk for some k∈K⊆a, every neighborhood of z meets a, so z∈cl(a). Thus E[K]⊆cl(a), proving the formula. □

**Corollary 2b.** If a,b are opens with cl(a)∩cl(b)=∅ and u≪a, v≪b, choose compact K,H with u⊆K⊆a and v⊆H⊆b. Then E[K], E[H] are **disjoint closed E-saturated subsets**, and

    cl(E[cl(u)]) ⊆ E[K] ⊆ cl(a),
    cl(E[cl(v)]) ⊆ E[H] ⊆ cl(b).

In particular,

    E[cl(u)] ⊆ v*,    E[cl(v)] ⊆ u*,

where v*=X\cl(v), u*=X\cl(u).

**Significance.** The necessary obstruction from §3 is **automatically absent for the specific way-below pairs relevant to the main conjecture**. The closed saturated envelopes E[K],E[H] can be noncompact; requiring compact intermediate buffers was precisely the mistake in the earlier ρ-interpolation attempt. There is nevertheless **no general proof that these closed saturated sets possess disjoint open neighborhoods** (much less neighborhoods with disjoint closures). That is the remaining promotion from *closed buffers* to *open interpolants*.

**Caveat on scope:** The compact-containment implication u≪a⇒∃ compact K with u⊆K⊆a is used here for locally compact sober spaces (equivalently, classical continuous frames), not for an arbitrary space X.

## 2. A compact counterexample to the naïve strong lemma

We give an explicit topology in which I=U=F while the rather-below relation is **not even one-step interpolative on an arbitrary far pair of opens**.

Let S={s_n}, T={t_n}, R={r_n} (n≥1) be three pairwise disjoint countable sets. Set

    X = {x,y} ∪ S ∪ T ∪ R.

Every point of S∪T∪R is isolated. Neighborhood bases of x and y are:

    X_{N,M}={x}∪{s_n:n≥N}∪{t_n:n≥M},
    Y_{N,M}={y}∪{s_n:n≥N}∪{r_n:n≥M}.

**Lemma 3 (verified).** This X is compact, T1, locally Hausdorff, sober, and locally compact in the strongest local compactness sense needed for a continuous frame. Its only distinct inseparable pair is (x,y), and

    I(X)=U(X)=F(X).

**Proof.** Every open cover contains a neighborhood of x and a neighborhood of y; together they cover all but finitely many isolated points. Hence compact. Each displayed basic neighborhood is itself compact (a finite union of convergent-sequence tails including the one limit point), and is Hausdorff as a subspace. Thus X has an open basis of compact Hausdorff subspaces, is T1 and locally Hausdorff, and consequently is sober. Every neighborhood of x meets every neighborhood of y in a tail of S; all other distinct pairs can be separated by clopen singletons. Therefore the only off-diagonal I- and U-related points are x and y. Finally the compact-space theorem [A-coherent-implication.md](A-coherent-implication.md) gives I=F (or check directly by continuous functions constant on {x,y}). □

Let

    u = T,    v = R,

both open. Their closures are

    cl(u)=T∪{x},    cl(v)=R∪{y},

which are disjoint. Hence

    u≺v*.

**Proposition 4 (counterexample).** There does **not** exist any open c with

    u≺c≺v*.

**Proof.** If u≺c, then cl(u)⊆c, so x∈c. Because xEy, every neighborhood of y meets c, giving y∈cl(c). But c≺v* would require cl(c)⊆v*=X\cl(v), which excludes y. Contradiction. □

Thus **even one interpolation stage fails** although I=U=F. In particular there is no continuous f:X→[0,1] with f|_u=0 and f|_v=1, since continuity and x∈cl(u), y∈cl(v) would force f(x)=0, f(y)=1, contradicting xEy.

This does **not** contradict the exact continuous-frame U=F criterion: u and v cannot arise simultaneously as way-below subopens of *far* larger opens a,b. Indeed, if u≪a, a compact subset K with T⊆K⊆a must contain x; otherwise {X\cl(T)}∪{{t_n}:n≥1} is an open cover of K without a finite subcover. Thus x∈a. Similarly, v≪b implies y∈b. Since xEy, opens a∋x and b∋y meet, so a∧b≠0, much less are they far.

**Lesson:** a compact frame, or even I=U=F, does not make ≺ an interpolative relation. The way-below buffers around the **original far pair** are essential and cannot be discarded mid-argument.

## 3. A precise necessary condition for any proposed intermediate

Suppose E is the inseparability relation and u,w are opens. If there is an intermediate c with

    u≺c≺w,

then necessarily

    E[cl(u)]⊆w.

**Proof.** From u≺c we get cl(u)⊆c. If z∈E[cl(u)], pick t∈cl(u)⊆c with zEt. Then every neighborhood of z meets c, so z∈cl(c)⊆w. □

This condition is **stronger** than cl(u)⊆w, and therefore stronger than u≺w. The two-arm space of §2 exhibits the failure:

    E[cl(u)] contains y, but y∉v*.

In the particular example, even the weaker proposed condition "there is an E-saturated open c with cl(u)⊆c⊆v*" fails, for the same reason.

We do **not** claim the necessary condition E[cl(u)]⊆w is sufficient in arbitrary spaces, nor even under I=U. Additional opening/interpolation hypotheses would be needed.

## 4. Why the compact-pair lemma cannot automatically iterate

In the continuous-frame test, way-below approximation supplies compact K⊆a and H⊆b with u⊆K, v⊆H. If a*∨b*=1, then no point of K is E-related to a point of H. Lemma 1 therefore supplies far open neighborhoods A,B of K,H.

But iteration would require replacing a compact core by a new one large enough to contain its E-partners. There are two independent obstacles:

1. **Escape to infinity:** even when K is compact, E[K] need not be contained in any compact set. The split-real-line example [A-closed-saturation.md](A-closed-saturation.md) gives such K, with E[K] containing infinitely many closed discrete duplicate points. Hence there is no globally compactly contained sequence of neighborhoods absorbing all E-partners. This also defeated the rounded relation ρ in [A-stable-interpolation-test.md](A-stable-interpolation-test.md).
2. **Different arms of an E-class:** as §2 shows, the closure of an open can meet one member of an E-class while avoiding another. Thus a putative intermediate neighborhood may be forced to include the whole class even when the available outer open omits part of it. This can obstruct **any** interpolation, even without compact containment.

For a first-stage interpolant c with u≺c≺w, the condition E[cl(u)]⊆w is an immediate, checkable obstruction. But this alone does not address the possibility of constructing intermediate c_t *only* for the special way-below pairs arising from two larger far opens; the counterexample of §2 specifically does **not** satisfy those stronger premises.

## 5. What a viable stable lemma would have to say

A precise but presently **unproved** candidate is:

> (**Relative stable-buffer conjecture.**) Let X be locally compact sober and suppose I(X)=U(X). Let a,b be opens with cl(a)∩cl(b)=∅, and let u≪a and v≪b. Then there exists a dyadic family c_t, t∈D∩[0,1], with c_0=u, c_1=v*, and cl(c_s)⊆c_t for s<t.

By the Picado–Pultr VI.1.1–1.5.2 characterization, this is **exactly** the sought implication I=U⇒U=F. It is not a separate theorem and must not be advertised as one.

A genuinely intermediate task, weaker than this full claim, is to seek a *pairwise compact-core enlargement rule* allowing noncompact intermediate opens while retaining a compact E-separated witness on the other side. At present we know only the static finite compact-pair lemma in §1, and there is no verified way to iterate it indefinitely.

Possible alternate route: investigate whether the special hypothesis u≪a, v≪b with cl(a)∩cl(b)=∅ forces the necessary compatibility

    E[cl(u)]⊆v*,

which would remove the obstruction of §3, though not prove existence of c. **This compatibility is established under compact-containment hypotheses in Corollary 2b above**; what remains unresolved is extending the resulting closed buffers to a dyadic chain of separating *open* neighborhoods. More generally, test whether stronger consequences involving E[cl(u)] can be obtained.

## 5a. Countable compact exhaustion succeeds globally

**Subsequent positive result:** [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md) proves that if X is a kω-space and E=cl(Δ_X) is an equivalence relation, then X/E is normal Hausdorff. In particular, if X is **weakly locally compact and σ-compact** as a point-set statement (and, for the full locale conclusion, **strongly locally compact and sober**), then

    I=U ⇒ I=U=F.

This bypasses a direct dyadic construction: compact quotients q(K_n) are compact Hausdorff, and a continuous separator on one q(K_n) extends consistently through the countable exhaustion by Tietze's theorem. The open question remains **only without** the kω/σ-compact restriction.

## 6. Research status

**Proved here:** compact E-separated subsets admit far neighborhoods (even with noncompact E-saturations); the first-interpolation necessary condition E[cl(u)]⊆w; an explicit compact locally compact sober example with I=U=F and a far pair that has no rather-below interpolant.

**Not proved:** the proposed stable lemma, or the implication I=U⇒U=F for every continuous frame.

The mathematical distinction is between **finite separation of compact E-separated cores** and **countably stable extension to an entire noncompact family of E-partners**. The former is elementary and survives all the examples; the latter is the unresolved challenge.
