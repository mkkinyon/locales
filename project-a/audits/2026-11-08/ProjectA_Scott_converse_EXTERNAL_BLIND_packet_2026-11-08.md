# Project A — Scott-continuity converse for closed relations

**Technical packet for an independent, blind correctness audit — 8 November 2026**

This packet states the proposed theorems and supplies complete arguments for critical examination. **The arguments are claims under review, not certified results.** Only the two main theorems T and L, the equivalent compact-support criterion, and the asserted logical scope are primary audit targets. The final application to inseparability is included to explain why the theorem is relevant to Project A.

## 1. Motivation and conventions

Project A studies several localic binary relations in `X ×_loc X`. In particular, the *inseparability relation* is the closed diagonal hull

\[
\mathcal I_X=\operatorname{cl}(\Delta_X).
\]

A recurrent question is when the projections of this relation are **proper**. Properness permits application of quotient/effectiveness results for internal equivalence relations, once transitivity is independently known. But the directly available operator on the frame of opens is often only the composite

\[
 r_E=(p_2)_*p_1^*,
\]

and its Scott continuity is a priori weaker than Scott continuity of `(p_2)_*` on *all* opens of `E`.

The proposed converse identifies a class where this difficulty disappears. The theorem is **not** restricted to equivalence relations; in fact, the topological theorem allows relations between **different spaces**.

**Definitions.** For a continuous map `f:Z→Y`, write `f^*:O(Y)→O(Z)` for inverse image, and `f_*:O(Z)→O(Y)` for its order-right-adjoint:

\[
 f_*(V)=\bigcup\{W\in\mathcal O(Y):f^{-1}(W)\subseteq V\}.
\]

An order-preserving map between frames is **Scott-continuous** here if it preserves every directed join. A space `X` is **weakly locally compact** if for every `x∈X` there are an open `V` and compact `K⊆X` with `x∈V⊆K`; `K` need **not** be closed or Hausdorff. “Compact” has its ordinary finite-subcover meaning, with no separation axiom. A topological map is **closed with compact fibers** if it sends closed subsets to closed subsets and each point inverse-image is compact (including empty fibers).

For a locale map `f:Z→Y`, **proper** means, in the convention used here, that `f_*` preserves directed joins **and** satisfies the **closed Frobenius law**

\[
 f_*(v\vee f^*(w))=f_*(v)\vee w
 \quad(v\in\mathcal O(Z),\;w\in\mathcal O(Y)).
\]

The Scott-continuity condition alone is sometimes termed *semi-proper*, *lax proper*, or *perfect* in locale literature; please distinguish it from the stronger definition above.

## 2. The topological theorem

**Proposed Theorem T.** Let `X` be weakly locally compact, let `Y` be an arbitrary topological space, and let `E⊆X×Y` be closed. Give `E` the subspace topology and let `p_X:E→X`, `p_Y:E→Y` be the coordinate projections. Define

\[
 r_E(U)=(p_Y)_*p_X^*(U)
      =\operatorname{int}_Y\bigl(Y\setminus E[X\setminus U]\bigr)
 \quad(U\in\mathcal O(X)),
\]

where `E[C]={y∈Y:∃x∈C, (x,y)∈E}`.

Then the following are equivalent:

- **(T1)** `r_E` preserves directed joins.
- **(T2)** `p_Y:E→Y` is a closed map with compact fibers.

No assumption of sobriety, `T₀`, Hausdorffness, symmetry, reflexivity, or transitivity is intended.

### 2.1 Proposed proof of T1 ⇒ T2

**Cover and directed family.** Weak local compactness yields an open cover `(V_i)_{i∈I}` of `X` and compact subsets `K_i⊆X` such that `V_i⊆K_i`. For each finite `F⊆I`, put

\[
 U_F=\bigcup_{i\in F}V_i,\qquad K_F=\bigcup_{i\in F}K_i.
\]

The family `(U_F)` is directed, has union `X`, and each `K_F` is compact. Because the right adjoint takes top to top, and by Scott continuity,

\[
 Y=r_E(X)=\bigcup_{F\subseteq I\text{ finite}}r_E(U_F).
\]

For each finite `F` set `W_F=r_E(U_F)`, which is open in `Y`. Thus `(W_F)` covers `Y`.

**Uniform compact support.** By the defining adjunction,

\[
 p_Y^{-1}(W_F)\subseteq p_X^{-1}(U_F),
\]

or equivalently,

\[
 E\cap(X\times W_F)\subseteq U_F\times W_F\subseteq K_F\times W_F.\tag{2.1}
\]

In other words, every point of `Y` has an open neighborhood over which all elements of the relation have first coordinate in **one compact** subset of `X`.

**Closed projection.** Let `H⊆E` be closed in `E`. Because `E` is itself closed in `X×Y`, `H` is closed in `X×Y`. From (2.1),

\[
 p_Y(H)\cap W_F
  =\pi_Y\bigl(H\cap(K_F\times W_F)\bigr).
\]

The set inside the projection is closed in `K_F×W_F`; the compact-factor projection `K_F×W_F→W_F` is a closed map by the tube lemma, **without a Hausdorff assumption**. Hence `p_Y(H)∩W_F` is closed in `W_F`. As the `W_F`'s cover `Y`, `p_Y(H)` is closed in `Y`.

**Compact fibers.** For `y∈Y`, choose `F` with `y∈W_F`. Then its fiber

\[
 E_y=\{x\in X:(x,y)\in E\}
\]

lies inside `K_F` by (2.1) and is closed in `K_F` because `E` is closed in `X×Y`. Thus `E_y` is compact. This completes T1 ⇒ T2.

### 2.2 Proposed proof of T2 ⇒ T1

More generally, let `f:Z→Y` be a **continuous closed map with compact fibers**. For an open `V⊆Z`, closedness gives the formula

\[
 f_*(V)=Y\setminus f(Z\setminus V).\tag{2.2}
\]

Let `(V_j)_{j∈J}` be a directed collection of opens of `Z`. If `y∈f_*(⋃_j V_j)`, then the compact fiber `f^{-1}(y)` lies in `⋃_j V_j`. A finite subcover and directedness give an index `j` for which the entire fiber lies in `V_j`. By (2.2), `y∈f_*(V_j)`. Therefore

\[
 f_*\left(\bigcup_j V_j\right)=\bigcup_j f_*(V_j).
\]

Apply this to `p_Y`. Since `p_X^*` preserves arbitrary joins, its composition `r_E=(p_Y)_*p_X^*` preserves directed joins. This completes T2 ⇒ T1.

### 2.3 Optional sharper equivalence: local uniform compact support

A third condition is proposed, under the **same** hypotheses as Theorem T:

- **(T3)** For each `y∈Y` there exist an open neighborhood `W` of `y` and compact `K⊆X` satisfying
  \[
  E\cap(X\times W)\subseteq K\times W.
  \]

The proof of T1 ⇒ T2 actually produces T3. Conversely T3, together with closedness of `E`, implies that `p_Y` is closed with compact fibers by the same tube-lemma argument applied to an open cover by such neighborhoods. Thus T1, T2 and T3 are claimed equivalent under Theorem T's hypotheses. Please check that the compact support `K` need not be closed in `X`.

## 3. Passage to continuous locales

**Background principles requested for verification, under classical mathematics.** The proposed argument invokes:

- **(B1)** Hofmann–Lawson duality: if `L` is a continuous frame, the canonical topological space of its points is locally compact and sober and has `O(X_pt)≅L`. In particular `X_pt` is weakly locally compact.
- **(B2)** If `X_pt` is locally compact sober, the locale product `Loc(X_pt)×_loc Loc(X_pt)` agrees with the locale of the ordinary topological product `X_pt×_top X_pt`.
- **(B3)** Under the identification in B2, a *closed* sublocale of the product corresponds to an ordinary closed subspace; its projections correspond to the induced topological projections. The relevant point-space identifications and right adjoints on opens are respected.

These are standard background claims rather than consequences of T. Please inspect their exact scope, especially B2–B3.

**Proposed Theorem L.** Let `X` be a locale whose frame `L=O(X)` is continuous, and let `E ↪ X×_loc X` be **any closed sublocale**. Write `p_1,p_2:E⇉X` for its projections. Under classical logic and choice,

\[
\boxed{
 (p_2)_*p_1^*\text{ preserves directed joins}
 \quad\Longleftrightarrow\quad
 p_2\text{ is a proper locale map}.
}
\]

If `E` is symmetric, both coordinate projections are proper whenever the condition holds.

### 3.1 Proposed proof of L, forward direction

By B1–B3, the localic closed relation corresponds to a topologically closed relation in a product of locally compact sober spaces. Applying Theorem T gives: **the topological projection `p_2` is closed with compact fibers**.

For a continuous, topologically closed, compact-fibered map `f:Z→Y`, formula (2.2) establishes Scott continuity of `f_*` on **all** opens of `Z`. It remains to verify *closed Frobenius*. For opens `V⊆Z`, `W⊆Y`:

\[
\begin{aligned}
 f_*(V\cup f^{-1}W)
 &=Y\setminus f\bigl((Z\setminus V)\cap f^{-1}(Y\setminus W)\bigr)\\
 &=Y\setminus\bigl(f(Z\setminus V)\cap(Y\setminus W)\bigr)\\
 &=(Y\setminus f(Z\setminus V))\cup W\\
 &=f_*(V)\cup W.
\end{aligned}\tag{3.1}
\]

The second equality uses the set identity `f(A∩f^{-1}B)=f(A)∩B`, without any surjectivity hypothesis. Via B1–B3 this verifies the frame identity

\[
 (p_2)_*(v\vee p_2^*w)=(p_2)_*(v)\vee w.
\]

Therefore `p_2` is proper in the specified localic sense.

### 3.2 Proposed proof of L, reverse direction

By definition, if `p_2` is proper then `(p_2)_*` preserves directed joins. The inverse-image homomorphism `p_1^*` preserves **all** joins, so their composite preserves directed joins. No use of B1–B3 is needed here.

If `E` is symmetric, coordinate transposition induces a locale automorphism of `E` exchanging `p_1` and `p_2`, so the conclusion holds for both projections.

## 4. Project A corollary and interpretation (supplementary audit target)

Let `\mathcal I_X=cl(Δ_X)`. This relation is closed, reflexive and symmetric. In Project A, a separate purely frame-theoretic argument proves

\[
 \mathcal I_X\circ\mathcal I_X\subseteq\mathcal U_X,
\]

where `\mathcal U` is the Urysohn-inseparability sublocale. Thus `\mathcal I=\mathcal U` is a sufficient condition for `\mathcal I` to be internally transitive.

Assuming L, if `O(X)` is continuous, `\mathcal I` is internally transitive, and `r_\mathcal I` preserves directed joins, then **both projections of `\mathcal I` are proper**. Published proper-quotient/effectiveness results for a closed proper internal equivalence relation can then be applied. The resulting quotient is continuous and strongly Hausdorff; by classical locally compact Hausdorff representation it is completely regular, yielding

\[
 \mathcal I=\mathcal U=\mathcal F,
\]

where `\mathcal F` is the kernel pair of the completely regular reflection. This is **not claimed to follow solely from T**: it also needs Vermeulen's proper-effectiveness theorem, proper-quotient continuity, and the identification of `\mathcal F` with the completely regular reflection's kernel pair. Please flag any hidden assumption if inspecting this corollary, but prioritize T and L.

The converse from functional equality to Scott continuity is **not** claimed. Nor is the localic theorem claimed for arbitrary noncontinuous frames or closed relations without the stated hypotheses.

## 5. Sanity checks and terminology cautions (not substitutes for proof)

1. Closedness of `E` and weak local compactness of `X` play **different roles**: the first controls relative closedness within compact supports; the second supplies the directed compact-source exhaustion.
2. The codomain `Y` in T need not be locally compact, sober or Hausdorff.
3. `p_Y` need not be onto: an empty fiber is compact; the right adjoint sends `O(E)`'s top to `Y`'s top even in this case.
4. Scott continuity of `r_E` does **not** presuppose `r_E^2=r_E`. Idempotence may fail for relations that are internal equivalence relations unless further conditions are established.
5. Compactness of individual fibers **alone** does not imply Scott continuity of `r_E`; nor does closedness of the projection alone.
6. The term “perfect” in topology and in point-free literature is not uniform; all statements here use explicit properties instead.

## 6. External background references (optional; no Project A audits)

- J. Picado and A. Pultr, *Frames and Locales: Topology without Points* (2012), Hofmann–Lawson duality, including its Hofmann–Lawson duality theorem. The standard representation of continuous frames by locally compact sober spaces is the only role of that duality here.
- J. Picado and A. Pultr, *Notes on the product of locales*, *Mathematica Slovaca* **65** (2015), 247–264. DOI: `10.1515/ms-2015-0020`. Relevant to locally compact sober space/localic product comparison.
- J. J. C. Vermeulen, *Proper Maps of Locales*, *J. Pure Appl. Algebra* **92** (1994), 79–107. DOI: `10.1016/0022-4049(94)90047-7`. Its proper quotient/effectiveness theorem is **background only**, not a proof of T or L.
- G. Manuell, *Presenting Quotient Locales*, *Applied Categorical Structures* **31** (2023), article 28, DOI: `10.1007/s10485-023-09736-x`. Accessible journal page: https://link.springer.com/article/10.1007/s10485-023-09736-x . Its definition of proper maps is Scott continuity plus closed Frobenius.

**Reminder to referee:** Please evaluate the complete argument and assumptions independently. A precise negative or conditional verdict is as valuable as a positive one. This packet does not include any prior internal correctness assessment.