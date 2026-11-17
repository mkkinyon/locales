# Project A — External-referee reconciliation: \(\mathcal J\), \(\mathcal T\), stably compact locales

**Date:** 17 November 2026  
**Sources:** Independent blind referee report and subsequent referee addendum, each dated 17 November 2026.  
**Disposition:** **Retain the main theorem; incorporate proof and reference clarifications; add separately identified graph consequences.**

This note documents the transition from the blind packet to the canonical theorem file
[`ProjectA_J_T_COMPARABILITY_GRAPH_STABLY_COMPACT_CANONICAL_2026-11-17.md`](ProjectA_J_T_COMPARABILITY_GRAPH_STABLY_COMPACT_CANONICAL_2026-11-17.md).
The report was independent of the earlier internal audit. Its favorable conclusion applies to the mathematical packet actually reviewed; the extra results in the addendum are *post-report* observations, not part of that blind verdict.

## 1. Referee findings and disposition

| Item | Referee verdict | Reconciliation |
|---|---|---|
| Universal hull identities \(\operatorname{cl}\mathcal J=\mathcal W\), \(\operatorname{fit}\mathcal J=\mathcal V\), \(\mathcal T=\mathbf T(\mathcal J)\) | Correct | Retained. |
| Perfectness, spatiality, and stable compactness of the six sublocales | Correct classically | Expanded the chain of cited theorems; made choice dependence and nucleus-order reversal explicit. |
| Exact support of the sublocale join \(\mathcal J\) | Correct, but proof needed an explicit bridge | Added patch-closed finite union, the associated sober subspace/spatial sublocale \(K\), and both inclusions \(\mathcal J\le K\le\mathcal J\). |
| Spectral/coherent inheritance | Correct | Distinguished *topological coherence* in stably compact spaces from a *coherent frame/spectral space*. |
| \(\mathcal J=G^2\), \(G^3\subseteq\mathcal T\subseteq G^4\), and the diameter-two criterion | Correct, including infinite posets | Retained with graph/localic distinctions. |
| Distance-four starting-orientation criterion and graph-only formula (8) | Correct, but decisive implication too compressed | Replaced with the referee's three-case argument for the nonempty \(M(u)\), comparable same-side nesting, and opposite-side disjointness. |
| Four-, five-, and eight-element examples; doubled-origin circle | Correct | Expanded quotient/local Hausdorff/sober explanation and bibliographic location. |
| Finiteness checks | Independent corroboration | Retained only as safeguards, not substitutes for proofs. |

No claim from the original theorem packet was retracted or reduced to a conjecture. The important **scope restriction** remains: in this presentation all six sublocales are identified with their point relations only after proving them **perfect and spatial**; the proof is classical and assumes a **stably compact locale**.

## 2. The two delicate repairs

### 2.1 The join really is the spatial union in this situation

Write \(Y=X\times_{\mathrm{Loc}}X\), \(P=\operatorname{pt}(X)\), \(\delta\subseteq P^2\), and
\[
A=\downarrow\delta=\operatorname{pt}(\mathcal I),\qquad
B=\uparrow\delta=\operatorname{pt}(\mathcal D).
\]
Both are patch closed in the compact-pospace representation, hence \(A\cup B\) is patch closed and determines a stably compact sober subspace of \(Y\). Let \(K\) be its spatial sublocale. Since both \(\mathcal I\) and \(\mathcal D\) have supports contained in \(A\cup B\), the sober-subspace/spatial-sublocale correspondence gives
\(\mathcal J=\mathcal I\vee\mathcal D\le K\).
The perfect-nucleus argument proves that \(\mathcal J\) itself is spatial; its point support contains \(A\cup B\), so the same inclusion-preserving correspondence gives \(K\le\mathcal J\). Therefore \(K=\mathcal J\), and
\[
\operatorname{pt}(\mathcal J)=\downarrow\delta\cup\uparrow\delta.
\]
**Avoid the invalid generalization** that arbitrary joins of spatial sublocales are set-theoretic unions on points.

### 2.2 The graph-only test is genuinely orientation-free

For \(d_G(x,y)=4\), let
\[
A_{xy}=\{u:d(x,u)=1,d(u,y)=3\},\quad
B_{xy}=\{z:d(x,z)=d(z,y)=2\},\quad
M(u)=N_G(u)\cap B_{xy}.
\]
Each \(M(u)\) is nonempty. A first step \(u<x\) forces \(u<z\) for every \(z\in M(u)\); a first step \(x<u\) forces \(z<u\). Comparable first steps on the **same** side of \(x\) have nested \(M\)-sets by transitivity. For first steps on **opposite** sides, \(u<x<r\), the sets are **disjoint**: if \(z\in M(u)\cap M(r)\), prolong \(x>u<z\) along a geodesic to \(x>u<z>v<y\). Then \(v<z<r\) yields the forbidden shortcut \(x<r>v<y\) of length three.

As the two sets are nonempty, this establishes equivalence between opposite-side geodesics and the nonnesting of \(M(u),M(r)\). The exact graph criterion is
\[
(x,y)\in\mathcal T\iff
\exists u,r\in A_{xy}: u\sim r,\ M(u)\not\subseteq M(r),\ M(r)\not\subseteq M(u).
\]
The proof works for **arbitrary posets**; finiteness is not used.

## 3. Results added *after* the blind report

The referee then supplied three further mathematical remarks. They have been checked for internal consistency and placed in a separately labeled subsection of the canonical note, **not** retrospectively counted as blind-audited theorems.

1. **Eight-vertex minimality.** If \(d_G(x,y)=4\) and \((x,y)\in\mathcal T\), opposite-start geodesics may be written
   \[
   x>u<z>v<y,\qquad x<r>t<s>y.
   \]
   Their six interior vertices are distinct: vertices at different distance levels from \(x\) cannot coincide; \(u\ne r\), \(v\ne s\) by order, while \(z=t\) would give the forbidden shortcut \(x<r>v<y\). Hence at least **eight** vertices are necessary, and the original eight-vertex example is cardinality-minimal (not asserted unique). Moreover \(u<x<r\) and \(v<y<s\) form **vertex-disjoint comparability triangles**.
2. **Triangle obstruction.** If the comparability graph has no pair of vertex-disjoint triangles, then no distance-four pair can lie in \(\mathcal T\). In view of \(G^3\subseteq\mathcal T\subseteq G^4\), this gives \(\mathcal T=G^3\). Sufficient cases include posets with at most seven vertices and posets of height at most two. The obstruction is not necessary.
3. **Transitivity, strictly on points.** If \(G\subseteq R\subseteq E_G\) for a reflexive symmetric relation \(R\), then \(R\) is transitive iff it equals the connected-component equivalence relation \(E_G\). Consequently \(\mathcal J\) is transitive on points iff \(\mathcal J=\mathcal T\) iff every comparability component has diameter at most two. Similarly, \(\mathcal T\) is transitive on points iff every component has diameter at most four and each distance-four pair passes the graph-only criterion. **Nothing here asserts transitivity with respect to localic relational composition or associativity of that operation.**

The main report also noted that each finite undirected comparability graph power \(G^k\) is patch closed (finite projection in the compact Hausdorff patch topology). Accordingly each has a canonical perfect spatial sublocale realization. This is a filtration of **point relations**; comparison with iterated *localic* relation composition remains open.

## 4. Remaining scope and promising work

- **Beyond stable compactness.** Compactness, local compactness, sobriety, and \(T_1\) together do not suffice: the doubled-origin circle already violates \(\mathcal I=G^2\). The precise hypotheses that make the six sublocales perfect/spatial and make their supports specialize-order-theoretic are unresolved.
- **Graph-power filtration.** Determine how much of \(G^k\) survives internally to localic relational composition, without presupposing associativity or equality of point supports with localic composites.
- **Distance-four fringe.** The two-disjoint-triangles obstruction is sufficient, not a characterization. Natural hereditary classes where the fringe is empty or nonempty may reveal further graph structure.
- **Terminology and hypotheses.** Preserve the distinction between the stably compact (topologically coherent) theorem and its spectral/coherent-locale corollary, and the use of classical choice in spatiality.

The recommended next action is to continue mathematical investigation from this stable audited foundation, not to seek a second audit of the same packet immediately. Any substantial new localic-composition claim would merit its own careful audit.

## 5. Sources

**Referee documents (preserved verbatim):**

- [`ProjectA_J_T_STABLY_COMPACT_BLIND_REFEREE_REPORT_2026-11-17.md`](ProjectA_J_T_STABLY_COMPACT_BLIND_REFEREE_REPORT_2026-11-17.md)
- [`ProjectA_J_T_STABLY_COMPACT_BLIND_REFEREE_ADDENDUM_2026-11-17.md`](ProjectA_J_T_STABLY_COMPACT_BLIND_REFEREE_ADDENDUM_2026-11-17.md)

Primary literature and precise theorem/lemma pointers are collected in §6 of the [canonical theorem note](ProjectA_J_T_COMPARABILITY_GRAPH_STABLY_COMPACT_CANONICAL_2026-11-17.md).
