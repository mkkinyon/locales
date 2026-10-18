# B — Graphs on frame elements (backlog)

**Status:** ideas preserved, not active. Not a novelty claim.

For any frame `L`, define the *overlap graph* on `L\{0}`: two **distinct** elements `a,b` are adjacent iff `a∧b≠0`. The greatest element `1` is universal, so graph diameter alone is uninteresting; consider distinguished bases or omit the top vertex when appropriate.

## Double negation and recovery

Let `j(a)=a**=(a→0)→0`. The fixed-point frame `B(L)` is a complete Boolean algebra (joins in it are `j` of joins in `L`). Since `j` is a nucleus, preserves binary meets, and `j(c)=0⇔c=0`,
```text
a∧b≠0 ⇔ a**∧b**≠0.
```
Every nonzero `j`-class is a clique and adjacency between distinct classes depends only on their images in `B(L)`.

Write `N[a]` for the closed graph neighborhood of a nonzero vertex (it includes a itself). **Working proposition:**
```text
N[a] ⊆ N[b]  ⇔  a ≤ b**,
N[a] = N[b]  ⇔  a** = b**.
```
For the difficult direction, if `a≰b**`, then `c=a∧b*≠0`, and `c` lies in `N[a]` but not `N[b]`. Care is needed if `c=a` or `c=b`, but the use of **closed** neighborhoods handles it. The overlap graph thus recovers the poset of double-negation classes and their fiber sizes.

**Corollary (working):** if `L` is a complete Boolean algebra, the overlap graph determines its order via `a≤b ⇔ N[a]⊆N[b]`, hence determines `L` as a complete Boolean algebra.

**Literature caveat:** strongly adjacent to intersection and zero-divisor graph theory; search for known results before asserting novelty.

## Pointless example

`L=RO(ℝ)`, the complete Boolean algebra of regular open subsets of ℝ, is atomless, hence its locale has no points. Nevertheless the overlap graph is large and reconstructs `L`.

## Universality

**Working proposition:** every countable simple graph `(V,E)` embeds as an induced subgraph of the overlap graph of `RO(ℝ)`.

Choose pairwise disjoint nonzero Boolean elements `q_s` for all `s∈V⊔E`; for each vertex `v`, put
```text
a_v = q_v ∨ ⋁{q_e : e∈E, v∈e}.
```
Then the `a_v` are distinct and `a_u∧a_v=q_{uv}` for `uv∈E`, zero otherwise. This is an abstract realization; it does not control separation properties or other structure.

## Questions

1. Which informative **distinguished bases** yield graph invariants for nonspatial frames?
2. Can some graph classes characterize algebraic properties of frames?
3. Which reconstruction results survive outside Boolean frames?
4. Compare with established intersection/zero-divisor graph results.

## Link to Cameron–Kumar's finite case

For finite `T_0` Alexandrov spaces, points correspond to nonzero join-irreducible (equivalently completely join-prime) opens `U_x`, providing algebraic vertex sets. In arbitrary Alexandrov spaces use completely join-primes; in pointless locales they may be absent.
