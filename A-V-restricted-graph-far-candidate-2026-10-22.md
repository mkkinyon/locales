# Restricted graph-far candidate for arbitrary-locale V
22 October 2026. Working definition and first tests; no completeness assertion.

## Motivation and definition
U has an intrinsic far-open-rectangle definition, whereas V=fit(I) is defined via fitted hull. The dual-far closed-rectangle strip formula W was disproved for arbitrary locales by the countable Hausdorff rational-graph example; it succeeds if I is compact. Try augmenting dual-far strips by **closures of graphs of maps from open sublocales of X**. Restricting to graph maps avoids immediately admitting every closed off-I relation, which would be a tautological restatement of fit(I).

Let L=O(X), T=L⊕L, I=C(d_I). Given an open embedding i:U↪X and arbitrary locale map φ:U→X, let γ=(i,φ):U→X×loc X. Put
 q_φ=∨{a⊠b : i*(a)∧φ*(b)=0 in O(U)}.
Rectangles join-generate T, so q_φ is the largest γ*-annihilated open; S_φ=C(q_φ) is the closure of the image of γ. Declare φ **graph-far** if q_φ∨d_I=1, equivalently S_φ∧I=0.

Define W_gr = W ∧ ⋂_{φ graph-far}O(q_φ), where W=⋂_{dual-far strips s}O(s). Universally V⊆W_gr⊆W. Candidate conjecture W_gr=V for all X is **unproved**.

## Tests
1. Known countable Hausdorff counterexample: U=L_0 open left Q copy, φ(ℓ_t)=r_t right Q copy. Then γ is exactly rational graph map g, q_φ=q, and the independently audited cover q∨d_I=1 means φ is graph-far. The added O(q) is precisely the open neighborhood missing from strip-generated nucleus; hence W_gr⊆O(q). This removes the *specific witness* of V≠W, but does NOT prove W_gr=V even on this X.
2. If I is compact (in particular X compact or coherent), W=V, so V=W_gr=W automatically.

## Open problems
- Is W_gr=V universally? Most likely test with relations that are not closures of graphs of maps over open domains; need a concrete quotient witness.
- Does it hold for the existing countable Hausdorff X beyond merely eliminating q?
- Is requiring graph-far via q_φ∨d_I=1 conceptually useful, or can an intrinsic criterion be given in terms of map φ and separation in X?
- How restrictive is the open-domain graph family? Adding arbitrary two-leg spans γ:Y→X² risks trivializing the construction because any closed sublocale is its own domain; a controlled class (étale domains, local homeomorphisms, open embeddings) might work.
- Separation trees remain valid infinitary benchmark, with their independent conceptual motivation to be developed, not abandoned.
- Spatial-square criterion remains secondary research topic, independently interesting even though a strip counterexample exists.

## First stress test: symmetry defect and corrected bi-graph family (22 October)

The initial one-sided partial graph family need not be invariant under the flip τ of X×X: transpose of graph (i,φ) can fail to be a graph with *open-domain first projection*, unless φ has additional injectivity/openness conditions. Since V is symmetric, this is undesirable and makes a one-sided completeness claim unnatural.

**Symmetrized proposal.** For any open embedding i:U→X and locale map φ:U→X, let γ→=(i,φ), γ←=(φ,i), let q→,q← be largest opens annihilated by these maps, and include both O(q→) and O(q←) when q→∨d_I=1 (equivalently q←∨d_I=1, since flip τ fixes d_I). Define
 W_bgr = W ∧ ⋂_{φ graph-far}[O(q→)∧O(q←)].
Then τ(W_bgr)=W_bgr, V⊆W_bgr⊆W. If I is compact, all equal V. The rational graph counterexample's missing q is among the generators, so its original obstruction no longer survives.

**Exact completeness test.** Let G be the family of all dual-far strips and all forward/reverse graph-far opens. For j_bgr=∨^(Nuc T)_{u∈G}o_u, W_bgr=V iff no q≠1 satisfies q∨d_I=1 and u→q=q for every u∈G. This is the prior closed-sublocale obstruction theorem with enlarged generator family. A counterexample would be a nonzero closed sublocale R disjoint I for which every primitive remains dense. The original rational-graph S=C(q) is not such an obstruction because its own graph primitive O(q) has empty intersection with S.

**What has NOT been proved:** whether the enlarged family is complete in arbitrary locales, or even on the rational-bridge test space. Symmetry repair does not supply completeness. If graph closures of maps from open domains prove inadequate, possible next restriction class: local homeomorphisms/étale maps with multiple sheets; avoid allowing every closed sublocale as domain because that makes the formula tautological.

**Duality question reserved:** Graph-far neighborhoods look more like a fitted generating family than a literal dual of U's far open rectangles. No claim of true duality yet.

## Multivalued primitives: finite-branch redundancy, infinitary gap (22 Oct, continuation)

**Proposition (finite graph-image unions are redundant).** Let γ_i:U_i→X×_loc X be permitted forward/reverse open-domain graph maps and S_i=cl(im γ_i)=C(q_i), i=1,...,n. The closed hull of the union of images is S=∨_iS_i=C(∧_i q_i). If S∩I=0 then each S_i∩I=0, hence each γ_i is graph far. Its complementary open primitive is O(∧_i q_i)=∧_iO(q_i), already in the bi-graph generated meet. Therefore permitting relations that are finite unions of admissible graph images gives no new generator.

**Infinite branching is genuinely different.** For a family indexed by J, S=∨_{i∈J}C(q_i)=C(∧_{i∈J}q_i) (meet taken in frame), but O(∧_i q_i) need not equal ∧_i O(q_i) for infinite J; finite intersection of open sublocales behaves differently from an infinite one. If the entire closed hull S is off I, each branch is graph far, yet O(∧_i q_i) may be a stronger neighborhood than the individual graph primitives collectively. This is a possible source of new power and parallels why finite rectangle joins were insufficient. Do not assert a strict inequality in our specific test space without construction.

**Controlled enlargement to test:** allow spans U←p−Y−φ→X with p a local homeomorphism (étale map) onto an open sublocale U⊆X, and use the closed image of (i∘p,φ):Y→X×X, including transpose. Graph far iff its closed image misses I. A finite open-sheet decomposition is redundant by the proposition; a genuinely infinite étale cover may introduce new neighborhoods. This remains non-tautological (not all closed relations are étale over a coordinate), symmetric after transposes, and works point-freely. Need check whether it strictly strengthens bi-graphs on the rational-bridge X or other controlled test frames.

**Central question still open:** Does the original bi-graph family already generate V? Neither an equality proof nor a counterexample obtained here. Infinitary-étale candidate is a fallback test, not promoted theorem.
