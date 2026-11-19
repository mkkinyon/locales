# Project A — a nonzero mixed-colour two-step core

**18 November 2026. New proof candidate; direct internal check only.** This note answers the question left at the end of `ProjectA_MixedColour_TwoStep_Obstruction_2026-11-18.md`: whether the two-step component relation `T=H_G∘H_G` has *any* nonzero intersection with the generic cross-gap product. The answer is yes, and in fact its patch pullback contains the Booleanization of the whole mediator rectangle. Combined with the earlier closed-Cantor obstruction, this makes the two-step restriction **nonzero and proper**. The proof relies on the explicit finite-fence realization and previously independently audited descriptions of the generic patch fibres; the new two-step calculation has not been independently refereed.

## 1. Statement and notation

Let `P=[0,1]` carry the explicit compact height-one fence order. Let `X` be its upper locale, `p:P_patch→X` the patch map, `q:X→Q` the component quotient, and `G=q^{-1}([p_∞])` its generic fibre. Write

\[
H=H_G=[E_G],\quad T=H\circ H,\quad
G_P^*=G\wedge U_P,\quad G_Q^*=G\wedge U_Q,
\]

where `U_P` and `U_Q` are disjoint upper opens compactly inside the fixed geometric gaps, and `E_G` is the ordinary component-equivalence relation. All relations are sublocales, and composition uses the **actual image** of the composable-pair sublocale. Put

\[
\widehat H=(p\times p)^{-1}H,\quad
\widehat T=(p\times p)^{-1}T,\quad
F=(p\times p)^{-1}(G_P^*\times G_Q^*).
\]

In the *patch* product, abbreviate `U=U_P×U_Q` and `Y=U_P×M×U_Q`, where `M` is the middle compact Cantor antichain. Write `\mathcal B(V)` for the nonzero least dense sublocale of a nonempty locale `V` (Isbell's density theorem).

**Theorem (mixed two-step positive core).** Under the explicit finite-fence hypotheses,

\[
\boxed{0\ne\mathcal B(U_P\times U_Q)\le F\wedge\widehat T.}\tag{P1}
\]

Under the previously established patch-fibre comparison `F≅G_P^*×G_Q^*` and the earlier negative selected-Cantor witness, this yields

\[
\boxed{0<T\wedge(G_P^*\times G_Q^*)<G_P^*\times G_Q^*.}\tag{P2}
\]

**Moreover the middle term of (P2) is dense in the right-hand locale.** Thus the cross-gap two-step relation is a **proper dense sublocale of the generic cross-gap product**. Its patch pullback contains a dense sublocale on the entire patch cross-gap rectangle, while it still misses nonzero sublocales on closed Cantor rectangles inside *every* nonempty mediator rectangle.

## 2. Two endpoint-conditioned density lemmas

Define ordinary pair sets in the patch plane:

\[
R_P=\{(x,a_n):n\ge1,\ x\in V(P_n)\cap U_P\}
\subset U_P\times M,\tag{P3}
\]

\[
R_Q=\{(b_n,y):n\ge1,\ y\in V(Q_n)\cap U_Q\}
\subset M\times U_Q.\tag{P4}
\]

Each pair belongs to `E_G`: a fence vertex and the indicated middle endpoint of that **same** component are component equivalent. The endpoint sets `A={a_n}` and `B={b_n}` are disjoint, countable, and each dense in `M`.

**Lemma 1.** `R_P` is dense in the patch product `U_P×M`, and `R_Q` is dense in `M×U_Q`.

**Proof.** Given nonempty patch-open `O⊂U_P` and nonempty relatively open `V⊂M`, arbitrarily high indices `n` satisfy `a_n∈V`. For *every* sufficiently high such `n`, the monotone shrinking-mesh fence `P_n` has a vertex in `O`, since it spans the fixed gap containing `U_P`. Hence `R_P∩(O×V)≠∅`. Basic rectangles form a base. The argument for `Q` uses arbitrarily high indices with `b_n∈V` and its fixed gap. Importantly, this is **conditioned density**: the chosen fence has both its mediator vertex in `O` and its endpoint in `V`. Mere separate density of the vertex and endpoint sets would not suffice. ∎

## 3. The nonspatial composable-pair witness

In the patch triple `Y=U_P×M×U_Q`, let

\[
Z_{12}=Y\wedge(p^3)^{-1}(\pi_{12}^{-1}H),\qquad
Z_{23}=Y\wedge(p^3)^{-1}(\pi_{23}^{-1}H),\tag{P5}
\]

where the restriction notation simply means the inverse images of the two upper-localic relation sublocales along the maps `Y→X³`. The ordinary triples `R_P×U_Q` belong to `Z_{12}`, and `U_P×R_Q` belong to `Z_{23}`. By Lemma 1 these two ordinary triple sets are separately dense in `Y`. Consequently `Z_{12}` and `Z_{23}` are **dense sublocales of `Y`**. Isbell's density theorem gives

\[
\boxed{\mathcal B(Y)\le Z_{12}\wedge Z_{23}.}\tag{P6}
\]

This is the decisive point-free step. There is **no ordinary triple** satisfying both component-equivalence conditions with outer coordinates in the disjoint mediators: a `P`-fence and a `Q`-fence are distinct components, while neither can reach the other's mediator. Nevertheless, the two separately dense localic subrelations have a nonzero intersection containing the least dense sublocale of `Y`.

Let `Z=π₁₂^{-1}H∧π₂₃^{-1}H≤X³` be the *actual* composable-pair sublocale, and let `ρ:Y→U` forget the middle coordinate. Formula (P6) means that the composite `\mathcal B(Y)→Y→X³` factors through `Z`. Hence its outer-coordinate composite to `X²` factors through the localic image `T`.

The patch outer projection `ρ` is an **open surjection** since `M` is nonempty. Its image `ρ[\mathcal B(Y)]` is dense in `U`: for any nonempty patch-open `W⊂U`, `ρ^{-1}W` is nonempty open and meets the dense `\mathcal B(Y)`, so its image cannot miss `W`. Since the composite to `X²` factors through `T`, the patch image lies in `\widehat T`. By the minimality of Booleanization,

\[
\boxed{\mathcal B(U_P\times U_Q)
\le\rho[\mathcal B(Y)]\le\widehat T.}\tag{P7}
\]

No general associativity, no closed image-base-change law, and no claim about the ordinary point set of `Z` is involved.

## 4. The same Boolean core is generic

The previously audited patch-fibre formula identifies `p^{-1}(G)` with the meet of patch-open complements of compact patch-closed sets whose intersection with the full fence vertex set `E` is finite. The negative tests for quotient opens not containing `p_∞` are automatic on either mediator: those upper opens miss `E`, whereas `E_P` is dense in `U_P` and `E_Q` in `U_Q`.

For any patch-closed cutoff `C⊂P` meeting `E` finitely, the trace `C∩U_P` has empty relative interior, because every nonempty patch-open subset of `U_P` contains infinitely many `P`-fence vertices. Thus `(P\setminus C)∩U_P` is patch-open dense, and analogously on `U_Q`. Since Booleanization lies inside **every dense open sublocale**, these generic point tests imply

\[
\mathcal B(U_P)\le p^{-1}(G_P^*),\qquad
\mathcal B(U_Q)\le p^{-1}(G_Q^*).\tag{P8}
\]

The patch coordinate projections from `U=U_P×U_Q` are open surjections. Pulling back either dense coordinate sublocale therefore yields a dense sublocale of `U`, so each contains `\mathcal B(U)`. Their meet is precisely the patch generic product `F`, restricted to its mediator rectangle. Accordingly

\[
\boxed{\mathcal B(U_P\times U_Q)\le F.}\tag{P9}
\]

Combining (P7) and (P9) proves (P1). The Booleanization is nonzero since `U` is a nonempty locale.

## 5. Transfer and coexistence with the negative obstruction

The independently audited special-fibre comparison gives the isomorphism

\[
F\xrightarrow{\sim}G_P^*\times G_Q^*.
\]

Under this isomorphism the nonzero sublocale `\mathcal B(U)` of `F∧\widehat T` transfers to a nonzero sublocale of `T∧(G_P^*×G_Q^*)`. On the other hand, the separate negative result constructs a nonzero `S^-≤G_P^*×G_Q^*` with `S^-∧T=0`, so the latter meet is **proper**. This proves (P2).

It is also **dense** in the generic product: `\mathcal B(U)` is dense in `U` and lies in `F`. Therefore it is dense *relative to `F`*: any nonzero open of `F` is the restriction of some nonzero patch open of `U`, which meets `\mathcal B(U)` nontrivially. Hence `F∧\widehat T`, which contains `\mathcal B(U)`, is dense in `F`. The special-fibre isomorphism transports this relative density to the upper-localic meet `T∧(G_P^*×G_Q^*)`.

There is no contradiction between the positive and negative witnesses. The negative witness comes from the Booleanization of a closed nowhere-dense Cantor rectangle `D_P^-×D_Q^+⊂U`. The least dense sublocale `\mathcal B(U)` lies in the *dense open complement* of that rectangle and hence has zero meet with its sublocales. Thus the dense two-step core can coexist with nonzero closed-support pieces missed by two-step composition. The earlier result even provides such a missed piece inside every nonempty sub-mediator rectangle.

## 6. Internal adversarial audit and remaining limits

1. **Endpoint-conditioned density, not two independent density assertions.** A chosen `P_n` has `a_n∈V` *and* a vertex in `O`, because every sufficiently late `P_n` spans the whole `P` gap with shrinking mesh. The same statement is independently true for `Q_n`. No compatibility between the two endpoint sequences is asserted.
2. **No invented ordinary composable path.** The sets of point triples satisfying the first and second relation conditions are disjoint, but each is dense in `Y`. The intersection of their *sublocales* contains `\mathcal B(Y)`. This is a direct use of the least-dense-sublocale property, not of point-set intersection.
3. **Pullback and image typing.** The patch triple maps into the *upper* triple. (P6) supplies a map into its actual localic composability pullback, before taking the outer image. Then the *patch* outer projection gives a dense image in `U`, which lies in the inverse image of `T`. No image-base-change identity is assumed.
4. **Generic Booleanization.** The patch generic product includes `\mathcal B(U)`, not because it has ordinary generic points (it does not), but because each positive quotient-neighborhood trace is dense in the mediator and each negative quotient-open trace is empty. The product statement uses open-surjective patch coordinate projections.
5. **Strictness is imported from the separate obstruction.** We prove nonvanishing here; propriety depends on the earlier selected lower Cantors and their verified separation `\downarrow[0,.44]\cap\downarrow[.46,1]=\varnothing` in the explicit model. The one-step positive core does **not** weaken that argument.

**Verdict:** (P1)–(P2), including relative density and propriety, survive this internal audit as concrete conditional theorem candidates. The outstanding question is no longer whether the mixed cross-gap two-step meet vanishes: it is **how much beyond the common Boolean core** lies in `T∧(G_P^*×G_Q^*)`, and whether a conceptual intrinsic description of that proper dense sublocale is possible. Independent adversarial review of this new argument would be prudent at the next consolidation checkpoint, but no external packet is prepared here.

**Primary reference for the key mechanism:** Picado–Pultr, *Locales treated mostly in a covariant way* (chapter excerpt available at `https://www.mat.uc.pt/~picado/publicat/LLNchapter.pdf`), §5.6, Isbell's Density Theorem. It explicitly notes that sublocales induced by disjoint dense subspaces can have a nontrivial localic intersection.
