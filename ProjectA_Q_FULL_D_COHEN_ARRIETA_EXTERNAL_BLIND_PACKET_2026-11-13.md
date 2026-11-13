# Blind proof packet — full fitted-diagonal product over Cohen × Arrieta

**13 November 2026. Proposed new theorem and proof for independent review.** This packet is self-contained except for the explicitly named source facts about Arrieta's example and established elementary locale calculus. It contains **no internal audit or internal verdict**.

## A. Locale notation and exact target

For a locale `X`, let `O(X)` be its frame and `X²=X×X` its **localic** square. If `a,b∈O(X)`, write `a⊠b` for an elementary open rectangle. For an open cover `C⊆O(X)` with `∨C=1`, put

\[
w_C=\bigvee_{c\in C}c\boxtimes c.
\]

The full fitted diagonal `D(X)=fit(Δ_X)` is the **meet of the open sublocales** `O(w_C)` over all `X`-covers. The finite fitted diagonal `D₂(X)` is the corresponding meet over **finite** covers. Thus a pair of locale maps `h,k:T→X` factors through `D(X)` precisely when

\[
\bigvee_{c\in C}h^*(c)\wedge k^*(c)=1_{O(T)}
\quad\text{for every cover }C.
\tag{A.1}
\]

Replacing “every cover” by “finite cover” characterizes factorization through `D₂(X)`. Any pair factors through `Δ_X` iff `h=k`.

For a Boolean locale `Z` (its frame is a complete Boolean algebra), `D(Z)=D₂(Z)=Δ_Z`. Projection naturality gives

\[
D(Z\times X)\le D(Z)\times D(X)=\Delta_Z\times D(X).
\tag{A.2}
\]

The **main claim** is that (A.2) is strict for `X=A`, Arrieta's strongly Hausdorff anti-Urysohn example, when `Z=Z_C=Loc(RO(2^ω))`, the Cohen Boolean locale. A second proposed theorem explains the phenomenon for arbitrary strongly Hausdorff locales with a nonfitted diagonal.

**Important scope:** A prior independent result gives the *closed* formula

\[
W(Z_C\times A)=W_2(Z_C\times A)=U(Z_C\times A)
=\Delta_{Z_C}\times A^2.
\tag{A.3}
\]

The proposed failure of **nonclosed** `D` is consistent with (A.3). It is not presented as a solution to either universal Q or Q′.

## B. General closed-graph theorem (proposed)

Say a locale `Y` is **strongly Hausdorff** when its diagonal `Δ_Y` is a **closed sublocale** of `Y²` (Isbell strong Hausdorffness). It is **F-separated** when `D(Y)=Δ_Y` (its diagonal is fitted).

**Theorem B.1 (claim).** For a strongly Hausdorff locale `Y`, the following are equivalent:

1. `D(Y)=Δ_Y`.
2. For **every Boolean locale** `Z`, one has `D(Z×Y)=Δ_Z×D(Y)`.

If `D(Y)>Δ_Y`, a **nonzero Boolean** witness `Z` can be chosen so that strictness is witnessed by a **two-member open cover** of `Z×Y`.

**Proposed proof of (1) ⇒ (2).** By (A.2), `D(Z×Y)≤Δ_Z×Δ_Y=Δ_{Z×Y}`, and every fitted diagonal contains its diagonal.

**Proposed proof of (2) ⇒ (1), contrapositive.** Let `δ_Y` be the open complement of the closed diagonal, so `Δ_Y=C_{Y²}(δ_Y)`. If `D(Y)>Δ_Y`, the relatively open off-diagonal sublocale

\[
E=D(Y)\wedge O_{Y²}(\delta_Y)
\]

is nonzero. Let `Z=B(E)` be its nonzero Booleanization, and let `f,g:Z→Y` be the two coordinate maps of `Z→E→Y²`. Then `(f,g)` factors through `D(Y)`, hence satisfies **all** cover equations (A.1), and its equalizer is zero because it factors through the open complement of `Δ_Y`.

The two sections

\[
s_f=(1_Z,f),\qquad s_g=(1_Z,g):Z\to Z\times Y
\]

have graphs `Γ_f`, `Γ_g`. A graph into a strongly Hausdorff locale is the pullback of its closed diagonal, hence a **closed sublocale**. Their intersection is the equalizer of `f,g`, so is zero. The open complements `u_f=(Z×Y)\setminus Γ_f` and `u_g=(Z×Y)\setminus Γ_g` consequently cover `Z×Y`.

Yet `s_f^*(u_f)=0` and `s_g^*(u_g)=0`, so the pair `(s_f,s_g)` gives matching value zero for this binary cover, and does **not** factor through `D(Z×Y)`. It does factor through `Δ_Z×D(Y)`, by equal base coordinates and full `Y`-cover compatibility. Thus (A.2) is strict.

**Referee challenge B:** Check the Booleanization step, the implication `E>0`, the equalizer as an **actual pullback sublocale**, the closedness of graphs, the complement-cover inference, and the product-factorization direction. Ordinary-point disjointness is not sufficient.

## C. Primary-source facts for the Arrieta specialization

Primary reference: Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, arXiv:2310.18522 (published version in *Topology and its Applications*), §§2.5, 4; in particular Construction 4.2, Corollary 4.3, Proposition 4.4, Example 4.5.

Let `C=2^ω` be Cantor space and define pairwise disjoint **finite closed** subsets

\[
K_n=\{x\in C:x_n=1,\ x_j=0\ \text{for }j>n\}.
\]

Set `Y=C\setminus⋃_{n∈ω}K_n`, a dense Gδ. The Arrieta space `A=Y⊔ω` has the ordinary `Y`-opens and basic neighborhoods

\[
(V\cap Y)\cup\{n\},\quad V\subseteq C\text{ open and }K_n\subseteq V,
\]

at the attached point `n`. Arrieta proves that `A` is Hausdorff, **strongly Hausdorff in the localic sense**, and anti-Urysohn. In particular `Δ_A` is a closed sublocale of `A²`. The countable Cantor base and finiteness of each `K_n` give a countable base of `A`.

**Elementary property to check directly:** For any fixed nonempty basic Cantor cylinder `R`, the set `K_n` meets `R` for **all sufficiently large n**. Indeed one may prescribe `R`'s finite prefix, set the nth bit to 1, and all later bits to 0. Consequently every infinite subfamily of the K_n has dense union. An A-open containing the attached point `n` contains a Y-neighborhood of **all** K_n.

## D. An explicit *Cohen* Boolean source and two frame maps

Let `P=C×C`. Since `P≅C`, the complete Boolean algebra

\[
M=RO(P)
\]

is isomorphic to the Cohen Boolean algebra. Put `Z_C=Loc(M)`.

For an A-open `u`, choose a Cantor-open `V_u⊆C` whose trace on `Y` equals `u∩Y`. Define

\[
h(u)=ro_P(V_u\times C),\qquad
k(u)=ro_P(C\times V_u),
\tag{D.1}
\]

where `ro_P(V)=int_P(cl_P V)`, and joins in `M` are **regular-open joins**, not ordinary unions.

**Claim D.1.** These definitions are independent of the chosen `V_u` and yield **frame homomorphisms** `h,k:O(A)→M`. The intended justification is that equal traces on dense `Y` have equal `C`-closures; inverse image along coordinate projections followed by the double-negation quotient preserves finite meets and arbitrary joins *with the frame operations of* `RO(P)`; the map factors through restriction `O(A)→O(Y)`.

Let `f,g:Z_C→A` be the corresponding locale maps.

**Claim D.2 (the crucial *all-cover* lemma).** For **every** A-open cover `\mathcal C`,

\[
\boxed{\bigvee_{u\in\mathcal C}h(u)\wedge k(u)=1_M.}
\tag{D.2}
\]

Proposed proof: take an arbitrary nonempty basic rectangle `R×S` in `P=C²`. Choose n sufficiently large that K_n meets both R and S. Some member u of the A-cover contains n. Its Y-trace contains `(V∩Y)` for some Cantor-open `V⊇K_n`, hence intersects both R and S on nonempty Cantor-open pieces. Therefore `h(u)∧k(u)` meets `R×S` nontrivially. This holds for every basic rectangle, so the union of the matching opens is dense in P and their **join in RO(P)** is 1.

This must establish compatibility with **arbitrary** A-covers, not merely finite covers. Thus `(f,g):Z_C→A²` factors through `D(A)`.

**Claim D.3 (empty localic equalizer).** For each n let

\[
a_n=(Y\cap\{x:x_n=1\})\cup\{n\}.
\]

This is A-open because K_n lies inside the nth 1-cylinder. The elements `h(a_n)` and `k(a_n)` are the clopen P-opens detecting whether, respectively, the first or second Cantor coordinate has nth bit 1. Any equalizer sublocale of f,g lies in every clopen equality locus

\[
e_n=\{(x,y):x_n=y_n\}\in RO(P).
\]

But the **complete Boolean meet** is

\[
\bigwedge_n e_n=\operatorname{int}_P(\Delta_C)=0,
\tag{D.3}
\]

since the Cantor diagonal is nowhere dense. For precision, every nucleus
`j` on a complete Boolean algebra has the form `j(b)=b∨j(0)` (use
`j(b)∧j(¬b)=j(0)`); hence every sublocale of `Z_C` is clopen.
Restricting the coordinate-bit clopens to an equalizer forces its Boolean
support below each `e_n`. Therefore `eq(f,g)=0` as a **sublocale** of
the Boolean locale Z_C.

**Referee challenge D:** Check every factorization of (D.1), the localic interpretation of density in (D.2), whether `K_n` really meets *both* test cylinders for the same arbitrarily large n, the fact that the equalizer is constrained by all `e_n`, and the complete-Boolean-versus-point-set distinction in (D.3).

## E. The claimed binary Cohen × Arrieta counterexample

As `A` is strongly Hausdorff, the graphs of the maps `f,g` from §D are **closed** in `Z_C×A`. By D.3 their intersection is the zero sublocale. Let

\[
u_f=(Z_C\times A)\setminus\Gamma_f,\qquad
u_g=(Z_C\times A)\setminus\Gamma_g.
\]

These are opens and `u_f∨u_g=1`, so `{u_f,u_g}` is a **binary open cover**. The two sections `s_f=(1,f)` and `s_g=(1,g)` satisfy

\[
s_f^*(u_f)=0,\qquad s_g^*(u_g)=0.
\]

Thus this cover has matching value zero under `(s_f,s_g)`. On the other hand, the sections share their Z_C-coordinate and the pair `(f,g)` matches **every** A-cover by D.2. Therefore

\[
(s_f,s_g)\text{ factors through }\Delta_{Z_C}\times D(A),
\quad\text{but not through }D(Z_C\times A).
\]

The proposed conclusion is the strict **full** fitted-diagonal product inequality

\[
\boxed{D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A).}
\tag{E.1}
\]

**Referee challenge E:** Attempt to falsify the cover equation or the pullback squares. Be explicit whether any objection concerns an actual localic sublocale or only ordinary points. Confirm that (E.1) uses the same base `Z_C` as the Cohen Boolean algebra, not the arbitrary Boolean base granted by Theorem B.1.

## F. Control: a *different* finite-D₂ pair

For comparison only, take `M_0=RO(C)`, `h_0(u)=ro_C(V_u)` and `k_0(u)=σ^{-1}h_0(u)` where σ flips **every** Cantor bit. Any finite A-cover has a member containing infinitely many attached n, whose Y-trace is dense, so `h_0=k_0=1` on that member. Hence the pair matches every **finite** A-cover.

However, the countable A-cover consisting of the `a_n` from D.3 together with `a_*=Y∩{x:x_0=0}` satisfies

\[
h_0(a_n)\wedge k_0(a_n)=0,
\qquad h_0(a_*)\wedge k_0(a_*)=0.
\]

So this pair is **not** in full `D(A)`. A Boolean-color split produces a binary cover showing

\[
D_2(Z_C\times A)\subsetneq\Delta_{Z_C}\times D_2(A),
\]

as follows: `h₀(a₀)` and `k₀(a₀)` are **complementary clopens** in
`RO(C)`, so their equalizer is the zero sublocale. Since A has a closed
diagonal, the same disjoint-closed-graph argument from §B yields a
binary product cover that separates their two sections. The sections
nevertheless factor through `Δ_Z×D₂(A)`. (A previously explored
spatial-Cantor-base variant is not needed or independently established
by this packet.) The present full-D proof **must not use this
complementary-coordinate pair** in place of the independent-coordinate
pair of §D.

## G. Strict limits and further audit questions

1. The referee's older Boolean-base theorem gives the **closed-level** equality (A.3), notwithstanding (E.1). Hence neither universal **Q** (`W₂=U ⇒ W=U`) nor **Q′** (`W₂=W` for all locales) is disproved.
2. The pair witnessing (E.1) fails a **binary cover of Z_C×A**, so it already lies **outside D₂(Z_C×A)**. It is **not** a weak internal Q′ defect `D₂(X)∧C(w_C)`. Conflating a product relation difference with such an internal difference would be erroneous.
3. The general theorem does **not** claim Cohen is a witnessing base for every strongly Hausdorff non-F-separated locale. It claims only existence of some Boolean base, with an explicit Cohen specialization for Arrieta.
4. Does the general graph theorem admit a shorter or more conceptual proof? Does its converse require every stated hypothesis? Identify any simplification or extension, but distinguish it from what the packet proves.
5. Presentation: report any point at which the distinction between `Δ`, `D`, `D₂`, `W`, and `W₂`, or between ordinary and localic products, is insufficiently clear.

**Desired output:** An independent mathematical report with verdicts on B.1, D.1, D.2, D.3, E.1, and the separation from Q/Q′; exact repairs or counterexamples; source-verification limits; and any additional observations. Do not read an internal audit before submitting the independent report.
