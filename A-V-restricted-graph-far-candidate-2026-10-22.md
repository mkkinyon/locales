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
