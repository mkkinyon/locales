> **20 NOV 2026 — REPAIRED SUBMISSION AVAILABLE:** The [self-contained repaired candidate](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_REPAIRED_CANDIDATE_2026-11-20.md) supersedes this working note *as the current proof for external review*: it expands the full two-colour Cantor fusion and all four induction splits. [Post-internal consolidation](ProjectA_CLIQUE_POWER_ASSOCIATIVITY_POST_INTERNAL_CONSOLIDATION_2026-11-20.md) · [blind handoff](project-a/audits/2026-11-20/CLIQUE_POWER_ASSOCIATIVITY/README.md). This original exploratory text is preserved for provenance. The new theorem remains **externally unverified**.

> **20 NOV 2026 — INTERNAL ADVERSARIAL AUDIT:** [Dedicated internal review](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_INTERNAL_ADVERSARIAL_AUDIT_2026-11-20.md) found no fatal error in (G), (B), (5V) or (PA), but requires the two-colour compact graph-fusion lemma and the leaf-versus-full-rectangle induction to be expanded before a blind external audit. This is *not* independent certification; the working status below remains in force.

# Project A — compact-metric point-clique power associativity
## New internal proof after five-vertex sector reduction · 20 November 2026

**Status:** NEW POST-REFEREE WORKING THEOREM. This note has **not** undergone an adversarial internal audit or independent blind review. It is NOT part of the verified 20 November referee verdict and should not be silently promoted to the canonical audited account. In particular the graph-generation/closed-annihilator lemma below is the central new proof obligation. Classical Loc throughout.

**Motivation:** The [four-vertex positive test](ProjectA_CLIQUE_ASSOCIATIVITY_FOUR_VERTEX_TEST_2026-11-20.md) left, for five overlap vertices, the comparison
\[
(R\circ S)\circ T\stackrel{?}=R\circ(S\circ T),\quad
R=[I_0\times Q_1],\ S=[I_1\times Q_2],\ T=[I_2\times Q_3]
\]
in the clopen outer block C_0×C_3. We prove both sides are **the entire** I_0×Q_3 by a twofold bipartite saturation lemma, and derive a more general power-associativity criterion.

### 1. A compact-metric graph-generation lemma

Let X,Z be compact metrizable Hausdorff spaces, with induced point-generated spatial sublocales A=[A_pts]≤X and D=[D_pts]≤Z. Put P_{A,D}=[A_pts×D_pts]≤X×Z. Let \(\mathscr G(A,D)\) consist of nonempty compact Cantor graphs \(\Gamma\subseteq X\times Z\), whose two coordinate projections are injective, such that:
- the points of Γ with first coordinate in A_pts are dense in Γ;
- the points of Γ with second coordinate in D_pts are dense in Γ.

Write \(\mathcal B(\Gamma)\) for the least dense (double-negation) sublocale of the closed graph Γ, viewed in X×Z.

**Lemma (closed-annihilator graph generation).**
\[
\boxed{A\times D
=P_{A,D}\vee\bigvee_{\Gamma\in\mathscr G(A,D)}\mathcal B(\Gamma).}\tag{G}
\]

**Proof candidate.** Each \(\mathcal B(\Gamma)\le A\times D\), because the pullback of A and of D to Γ contains, respectively, the dense selected point traces; both pullbacks are dense sublocales, so each contains \(\mathcal B(\Gamma)\). Also \(P_{A,D}\le A\times D\).

Set J equal to the RHS. If J<A×D, regularity/fittedness of the compact Hausdorff ambient product yields an **ambient open** O with J≤O and A×D not≤O. Let F be its closed complement, and set S=F∧(A×D)≠0. No ordinary point pair (a,d)∈A_pts×D_pts lies in F, because its point sublocale lies in P_{A,D}≤J and J∧F=0. Let C be the least ambient closed support of S. Then C is a nonempty compact metric closed subset of F, and S is dense in C.

**Selected-coordinate richness:** Every nonempty relatively open W⊂C contains an ordinary point whose first coordinate lies in A_pts, and likewise (possibly at another point) a point whose second coordinate lies in D_pts. Otherwise choose nonempty relatively open W' with compact closure inside W, and let K be the compact projection of cl_C(W') to X. This K is disjoint from A_pts; since A=[A_pts] is point-generated, A≤X\K. But S≤pr_X^{-1}A, while W' lies over K, forcing S∧W'=0, contradicting density in C. The second-coordinate argument is identical.

**Section thinness (correct closed-support proof):** Every fixed vertical/horizontal coordinate section of C is relatively closed nowhere dense. Suppose a nonempty relatively open W⊂C is contained in {x}×Z. Choose nonempty W' with compact closure cl_C(W')⊂W. If x∉A_pts, then A≤X\{x} and S∧W'=0. If x∈A_pts, let L=pr_Z(cl_C(W')), a compact closed subset of Z. Since cl_C(W')⊂F∩({x}×Z), and F contains **no** ordinary (a,d) with a∈A_pts,d∈D_pts, the closed set L is disjoint from D_pts. Point-generation then implies D≤Z\L. But W' lies in {x}×L, so S∧W'=0. Either case contradicts density of S in C. Horizontal sections are symmetric. **Do not argue that a nonzero sublocale of the spatial locale {x}×D has a point: that is false in general. The compact closed-projection test is essential.**

**Two-colour Cantor fusion:** Work inside nonempty relatively open rectangles of C. At each finite tree level choose, globally across its finitely many nodes, new anchors of each of the two types (first coordinate in A_pts, second coordinate in D_pts), avoiding all previously selected coordinate values. Richness and section thinness allow these choices because the forbidden finite union of coordinate sections is nowhere dense. Keep one inherited anchor in each node as the 0-child; give the two new anchors the 1- and 2-children. **Only after all anchors for the level are chosen**, choose all child closed product rectangles with disjoint first-coordinate projections and disjoint second-coordinate projections, small diameters, nested within the parent's interior, and with each anchor in the relative interior of its child rectangle. Use the 0-descendant chain to preserve each anchor. The intersection limit is a compact Cantor graph Γ⊂C, with both projections injective, dense first-A selected anchors and dense second-D selected anchors. Therefore Γ∈\(\mathscr G(A,D)\).

Its \(\mathcal B(\Gamma)\) is nonzero and lies in J∧F, a contradiction. This proves (G). **The construction uses compact metrizability/regularity and no assumed points of S.** QED candidate.

### 2. Dense complete-bipartite composition saturates its full localic product

Let X,Y,Z be compact metrizable Hausdorff spaces, A⊂X, D⊂Z arbitrary nonempty ordinary subsets, and B,C⊂Y **dense** ordinary subsets. Put the spatial point-generated bipartite sublocales
\[
R=[A\times B]_{X\times Y},\qquad S=[C\times D]_{Y\times Z},
\]
where we denote their induced support sublocales by the same letters in product expressions. Then
\[
\boxed{R\circ S=[A]_X\times[D]_Z.}\tag{B}
\]

**Proof candidate.** Source-target support gives ≤. For every a∈A,d∈D, R contains {a}×[B], S contains [C]×{d}, and [B]∧[C]≠0 by Isbell density. The rectangular rule supplies (a,d)∈R∘S, hence \(P_{A,D}\le R\circ S\).

For any Γ in the graph family of (G), consider the compact product Γ×Y. The maps to X×Y (first Γ-coordinate and middle Y) and Y×Z (middle Y and second Γ-coordinate) pull back R and S, respectively. The first pullback contains the ordinary point set \(\{(\gamma,y):\gamma_1\in A,\ y\in B\}\), dense in Γ×Y; the second contains \(\{(\gamma,y):\gamma_2\in D,\ y\in C\}\), also dense. Their **localic meet** is dense (both contain the least dense sublocale of Γ×Y). The composability condition therefore holds on a nonzero dense sublocale of Γ×Y. The projection Γ×Y→Γ is an **open surjection**, so the image of that dense sublocale is dense in Γ, contains \(\mathcal B(\Gamma)\), and factors through R∘S. Hence \(\mathcal B(\Gamma)\le R\circ S\). Formula (G) now forces [A]×[D]≤R∘S. QED candidate.

The conclusion also holds when either R or S is enlarged to its **full** endpoint support rectangle; monotonicity supplies the same lower bound and support supplies the upper bound.

### 3. Resolution of the five-vertex sector

Take four separate Cantor spaces C_0,C_1,C_2,C_3 and in each the dense rational/irrational induced spatial sublocales Q_i,I_i. In the five-vertex clique problem define
\[
R=[I_0\times Q_1],\quad S=[I_1\times Q_2],\quad T=[I_2\times Q_3].
\]
The intermediate Q_1 and I_1 are dense in C_1, so (B) gives
\[
R\circ S=I_0\times Q_2,\qquad S\circ T=I_1\times Q_3.
\]
Using (B) once more, with one factor enlarged to a full rectangle,
\[
\boxed{(R\circ S)\circ T=I_0\times Q_3=R\circ(S\circ T).}\tag{5V}
\]
This is **full localic** equality on the only previously unresolved C_0×C_3 sector, not merely equality of ordinary point pairs.

### 4. Extension to cliques on a compact metrizable locale

Let G be compact metrizable Hausdorff, with finitely many nonempty ordinary subsets E_i of its points, U_i=[E_i] and P_i=[E_i×E_i]≤G². Their finite localic overlap graph Λ has i–j as an edge when U_i∧U_j≠0. Set H=∨P_i.

**Proposed Theorem (all powers).** For every k≥2 and *every* fully parenthesized k-factor word W_k(H),
\[
\boxed{W_k(H)=\bigvee_{\operatorname{dist}_\Lambda(i,j)\le k-1} U_i\times U_j.}\tag{PA}
\]
In particular, all powers of H are independent of parenthesization, even if some U_i×U_j are nonspatial. At k=1, H is only the join of the **point-generated** cliques P_i, and need not equal ∨U_i².

**Proof plan/argument.** For U_i∧U_j≠0, let K be the least closed support of W=U_i∧U_j inside G. The sublocale W is dense in compact metric K. The selected coordinate-richness proof in (G), applied to W≤U_i and W≤U_j, shows \(E_i\cap K\) and \(E_j\cap K\) are both dense in K. (If they share a point, that gives an immediate bridge too.) Inside P_i and P_j lie the point-generated bipartite relations \([E_i\times(E_i\cap K)]\) and \([(E_j\cap K)\times E_j]\). Formula (B), with middle compact K and its two dense subsets, gives
\[
P_i\circ P_j=U_i\times U_j
\quad (U_i\wedge U_j\ne0).
\]
If U_i∧U_j=0 the composite vanishes by support. For a general indexed word P_{j_1}∘…∘P_{j_k}, induct on its binary tree: a subtree of length≥2 gives the **full** rectangle between its first and last support indices; a one-leaf subtree is the original P_i. If both child words have length≥2, use the rectangular rule. If one child is a leaf, use the same dense-bipartite lemma (B) after restricting the shared intermediate supports to the compact overlap K. This yields the full endpoint rectangle whenever all consecutive overlaps are nonzero. If one consecutive overlap is zero, the indexed word vanishes by the lowest-common-ancestor argument in the referee's report. The finite expansion of H gives (PA).

The theorem therefore resolves the clique **power** associativity problem in the compact metrizable setting, if the compact-metric graph-generation lemma (G) withstands adversarial scrutiny. It does **not** claim associativity for arbitrary different relations or outside compact metrizable locales.

### 5. Verification boundary and next step

**Current status: one internally developed proof chain, NOT independent certification.** The most important proof to attack is (G), especially:
(i) density of each selected coordinate trace in the least closed support of S=F∧(A×D), with A,D point-generated;
(ii) the finite-coordinate exclusion / two-colour Cantor fusion;
(iii) transport of the two dense pullbacks along the open product projection in (B).

If (G) and (B) survive, the original five-vertex nonassociativity search is **negative** and the entire compact-metric point-clique power sequence is explicitly computed by (PA). If a flaw appears, keep only the separately justified partial results; do not convert a proposed general theorem into a certified claim.

**Bibliographic background:** Isbell density; regular/fit sublocale separation; finite-join distributivity of pullback; image of dense sublocale under open surjection; point-generated supports. The Plewe/Johnstone nonspatial product warning remains relevant and is **not** circumvented by pretending these localic products are spatial.
