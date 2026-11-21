# Project A — compact-metric point-clique powers: pre-referee consolidation
**20 November 2026 · Repaired candidate for new blind external audit**

## 1. Why this is a new research phase

The [independently audited Stone clique-overlap rank theorem](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) gives arbitrarily large exact completion length even when each *ordinary* component is a clique. The independent referee's addendum established an overlap-graph completion theorem. It did **not** establish equality of intermediate localic powers under different parenthesizations.

The first fully localic threefold test on four overlap vertices was resolved positively in the [four-vertex note](ProjectA_CLIQUE_ASSOCIATIVITY_FOUR_VERTEX_TEST_2026-11-20.md), which was **internal post-referee work**. The next candidate obstruction, on five overlap vertices, reduced to three point-generated bipartite sublocales inside four disjoint Cantor blocks:
\[
R=[I_0\times Q_1],\qquad S=[I_1\times Q_2],\qquad T=[I_2\times Q_3].
\]
Their possible associator lies in a nonspatial outer localic rectangle, so agreement of ordinary point sets is insufficient.

The [working compact-metric saturation note](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_WORKING_2026-11-20.md) proposed a more general solution and received a [separate internal adversarial audit](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_INTERNAL_ADVERSARIAL_AUDIT_2026-11-20.md). That audit reported no fatal defect but required two proof expansions: a fully precise compact two-colour Cantor-graph fusion and the leaf-versus-composite binary-tree induction.

The [repaired theorem and complete proof](ProjectA_CLIQUE_COMPACT_METRIC_POWER_ASSOCIATIVITY_REPAIRED_CANDIDATE_2026-11-20.md) now incorporates both. It is the **authoritative candidate for external review**, not an externally certified theorem.

## 2. Candidate theorem (conditional on the submitted proof)

Let \(G\) be compact metrizable Hausdorff, let \(E_1,\ldots,E_m\) be finitely many nonempty ordinary point sets, and put
\[
U_i=[E_i]_G,\quad P_i=[E_i\times E_i]_{G^2},\quad H=\bigvee_iP_i.
\]
Let \(\Lambda\) be the finite graph on the component labels with \(i-j\) iff \(U_i\wedge U_j\neq0\) for distinct \(i,j\). The repaired candidate asserts that for every \(k\ge2\) and **every binary parenthesization** \(W_k\),
\[
\boxed{
W_k(H)=\bigvee_{\operatorname{dist}_{\Lambda}(i,j)\le k-1}U_i\times U_j.
}
\tag{PA}
\]
For disconnected \(\Lambda\), include only finite distances. The formula does not apply to \(k=1\): a spatial point-generated clique \(P_i\) may be strictly smaller than \(U_i^2\). Nor does (PA) imply associativity of arbitrary heterogeneous localic relations.

The first new test case becomes
\[
\boxed{(R\circ S)\circ T=I_0\times Q_3=R\circ(S\circ T).}
\tag{5V}
\]
This equality is **proposed at the full sublocale level**, including any nonspatial parts.

## 3. Proof dependency graph

1. **Rectangular calculus.** For sublocales \(A,B,C,D\), composition of \(A\times B\) with \(C\times D\) gives \(A\times D\) iff \(B\wedge C\ne0\), otherwise \(0\). In classical Loc, the nonzero middle locale is overt, so its terminal map is an **open surjection**, which is pullback-stable. No stability of arbitrary locale-surjections is invoked.
2. **Compact-metric graph generation (G).** The localic product of two point-generated endpoint sublocales is the join of their ordinary point-pair sublocale and Booleanizations of specially chosen compact Cantor graphs. It uses a fitted ambient open/closed separator, coordinate richness in the least compact closed support of an arbitrary nonzero sublocale, section thinness by **compact closed projections**, and a global two-colour Cantor fusion.
3. **Bipartite saturation (B).** Two point-generated bipartite relations with middle point sets each dense in one compact metric middle space compose to the **full** localic endpoint product. The graph generation lemma is used to recover nonspatial product material: pulling to \(\Gamma\times Y\) gives two dense sublocales; their meet contains \(\mathcal B(\Gamma\times Y)\); its image along an explicitly **open-surjective** projection contains \(\mathcal B(\Gamma)\).
4. **Overlap compact support.** For \(0\ne U_i\wedge U_j\), its least ambient closed support \(K\) is compact metric; \(E_i\cap K\) and \(E_j\cap K\) are both ordinarily dense in \(K\). Bipartite saturation gives \(P_i\circ P_j=U_i\times U_j\).
5. **All-bracketing induction.** At every binary-tree root, handle four cases explicitly: both children composite; left leaf; right leaf; two leaves. In one-leaf cases apply (B) with the least compact closed support \(K\) of the two adjacent support sublocales; do **not** assume any nontrivial product is spatial. An adjacent zero overlap forces the corresponding lowest-common-ancestor subtree to be zero.
6. **Finite expansion.** Expand \(H=\bigvee_iP_i\) over a finite set of indices. Nonzero index words correspond to overlap-graph walks with possible vertex repeats, producing (PA) for \(k\ge2\).

The steps are explained and proved in the repaired candidate itself; this roadmap does not replace that proof.

## 4. Audit status and preserved boundaries

| Claim | Current status |
|---|---|
| Previously refereed bounded-diameter exact rank and overlap-graph completion | Independent favorable audit (separate phase) |
| Four-vertex triple equality | Internally derived; no separate blind audit |
| Graph generation (G) | Internally audited favorably, proof expanded; **new blind audit pending** |
| Bipartite saturation (B) | Follows from (G); **new blind audit pending** |
| Five-vertex equality (5V) | Conditional on (B); **new blind audit pending** |
| General all-length formula (PA) | Conditional on full proof, **new blind audit pending** |
| Constructive, nonmetrizable, infinite-support generalizations | Not claimed |
| Original unrelated unmodified six-step nonassociative gadget | Still unverified; not used |

**The old working note and internal adversarial audit are preserved, not overwritten**. The repaired candidate is a new document. Its "proof" language does not mean that the pending external audit has already accepted it.

## 5. External audit handoff

The [blind audit archive](project-a/audits/2026-11-20/CLIQUE_POWER_ASSOCIATIVITY/README.md) provides the submitted reading order, independent referee prompt, candidate and supporting foundations. The user-facing ZIP contains these sources **without** the internal adversarial report, internal verdict, or this reconciliation.

Preferred independent referee question: identify any error in (G)—especially the least closed support, section thinness, fusion induction, and graph-restricted localic pullbacks—or determine whether the two-factor full-product lemma (B) and binary-tree formula (PA) follow. A negative result is as useful as a positive one.

**Next step:** await independent referee report before promoting (G), (B), or (PA) to the canonical verified theorem ledger. Meanwhile the previous Stone overlap-rank theorem remains valid regardless of the new audit verdict.
