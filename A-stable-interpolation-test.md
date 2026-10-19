# A — Stable interpolation attempt: a natural rounded relation fails

**18 October 2026. Status: a rigorous obstruction and a model interpolation, but no proof or counterexample to the full continuous-frame implication.** No novelty or priority claim. This follows [A-way-below-revisited.md](A-way-below-revisited.md), [A-continuous-frames.md](A-continuous-frames.md), and [A-closed-saturation.md](A-closed-saturation.md).

## 1. Target and proposed stable relation

For a frame L, use
- u≪a for the domain-theoretic way-below relation;
- a≺b for a*∨b=1 (the *rather below* relation);
- a≺≺b for the completely-below relation, equivalent to a dyadic scale a=c_0≺c_t≺c_1=b, with c_s≺c_t for s<t, and to the standard localic real-map separator. See Picado–Pultr (2021), VI.1.1 and VI.1.5.2.

Our continuous-frame criteria remain

    I=U  ⇔  (a∧b=0, u≪a, v≪b) ⇒ u≺v*;
    U=F  ⇔  (a*∨b*=1, u≪a, v≪b) ⇒ u≺≺v*.

The central unsolved task is to construct a **stable dyadic interpolation** from the first criterion, without assuming U=F.

A natural attempt is to introduce a "compactly rounded" rather-below relation:

    u ρ w  iff  ∃a∈L [u≪a and a≺w].

Clearly ρ⊆≺ by monotonicity of rather-below. If ρ were interpolative and uρw, we could use Picado–Pultr VI.1.1.1 to infer u≺≺w. Unfortunately, **ρ is not generally interpolative even in a space with I=U=F**.

## 2. Counterexample to ρ-interpolation

Take the split-real-line space X from [A-closed-saturation.md](A-closed-saturation.md):

    X=R ⊔ {e_n:n≥1},

where e_n is a duplicate of r_n=1/n. Ordinary real intervals are open, and at e_n basic neighborhoods are

    {e_n} ∪ (J\{r_n}),  J ordinary open interval containing r_n.

Let p:X→R identify e_n and r_n and fix the ordinary real points. This p is continuous, open, and has fibers equal to the inseparability classes. Thus

    I(X)=U(X)=F(X)=ker(p)

as point relations and, since X is locally compact sober, as closed localic relations.

Fix 0<ε<1/4, and define

    u=(-ε,ε)⊂R⊂X,
    a=(-2ε,2ε)⊂R⊂X,
    w=p^(-1)((-3ε,3ε)).

Then u≪a: the ordinary interval [-ε,ε] is a compact saturated subset of X lying inside a (and containing u). Also cl_X(a)⊆w: the closure includes the ordinary interval [-2ε,2ε] and exactly those e_n with r_n∈[-2ε,2ε]; all lie inside w. Hence a≺w and therefore uρw.

Suppose c∈O(X) with uρc and cρw. The first relation gives an open a_1 with u≪a_1≺c; thus

    cl_X(u) ⊆ cl_X(a_1) ⊆ c.

But cl_X(u) contains every e_n with 0<r_n<ε, an infinite subset of the family C={e_n:n≥1}. The family C is **closed and discrete** in X because X\C is the ordinary real line, which is open, and each e_n has a neighborhood meeting C only in e_n.

The second relation cρw gives c≪a_2 for some a_2≺w. Thus c is contained in a compact subset K of X (using the locally compact sober characterization of ≪). This is impossible: K∩C is a closed subset of compact K, hence compact, and it is discrete, hence finite. But c contains infinitely many e_n.

Therefore **no such c exists**:

    uρw, but there is no c with uρcρw.

This even disproves interpolation of ρ under the stronger hypothesis I=U=F.

### A general obstruction behind the example

For any topological X, if uρcρw then cl(u) is contained in a compact subset of X:

    uρc ⇒ cl(u)⊆c,
    cρw ⇒ c≪a_2 ⇒ c⊆K with K compact.

Thus every u with non-relatively-compact closure, yet uρw for some w, is an obstruction to interpolation of ρ. In non-Hausdorff locally compact spaces, u≪a does **not** imply cl(u) is compact. Compact containment and compact closure must never be silently identified.

This connects directly to the "escaping inseparable partners" diagnosed in [A-closed-saturation.md](A-closed-saturation.md).

## 3. Yet an ordinary ≺-dyadic scale exists here

The failure of ρ-interpolation does not say u is not completely below w. On the contrary, set

    c_0=u,
    c_t=p^(-1)((-r(t),r(t)))   for 0<t≤1,
    r(t)=ε+2εt.

Then c_1=w, and for all 0≤s<t≤1,

    cl_X(c_s)⊆c_t.

For s>0 this follows from continuity of p:

    cl_X(p^(-1)((-r(s),r(s))))
        ⊆ p^(-1)([-r(s),r(s)])
        ⊆ p^(-1)((-r(t),r(t))).

For s=0, cl_X(u)⊆p^(-1)([-ε,ε])⊆c_t. Thus c_s≺c_t for s<t, a dyadic (indeed real-indexed) interpolation witnessing

    u≺≺w.

Every intermediate c_t, t>0, contains all sufficiently large e_n and is **not relatively compact**. In other words, **there is a valid stable ≺-scale, but there cannot be one whose stages all belong to ρ**.

The analogous real-valued function is immediate: compose p with a continuous cutoff on R that is zero on [-ε,ε] and one off (-3ε,3ε).

## 4. What is and isn't learned

**Established:**
- The straightforward "relatively compact and far" interpolation relation ρ is **not interpolative**, even for locally compact sober spaces with I=U=F.
- The obstruction is precisely that compactly contained opens can have noncompact closures due to escaping inseparable partners.
- Genuine completely-below interpolation may require intermediate opens with noncompact closures, including entire stretches of inseparable partners.

**Not established:**
- No valid interpolation relation deduced from I=U has been identified.
- We have **not** shown that the implication I=U⇒U=F is true or false for all continuous frames.
- The failure of ρ is **not** a counterexample to the target implication, since this X satisfies I=U=F.

## 5. More promising reformulation of the task

Instead of demanding that every dyadic intermediate be relatively compact, try to construct open c_t for which

    c_0=u, c_1=v*, c_s≺c_t for s<t

using **E-saturated or quotient-adapted neighborhoods**. The split-real-line construction suggests that even when u is relatively compact, higher c_t may need to include all inseparable partners of u, possibly a noncompact set.

One can also study a *stabilized* relation with a globally E-saturated buffer:

    u [E-buffer] w  if there is an open G with cl(u)⊆G⊆w
                                and G is large enough to include relevant E-saturations.

This is only a proposal, **not** a theorem: existence and interpolation of such buffers need proof, and saturations of opens need not be open (see [A-continuous-compactness-question.md](A-continuous-compactness-question.md)).

The compact-space proof and its open-subspace inheritance from [A-way-below-revisited.md](A-way-below-revisited.md) remain available. A new general proof must handle the global interpolation directly, rather than incorrectly extracting compact supports from u≪a.
