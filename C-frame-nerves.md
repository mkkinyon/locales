# C — Frame-cover nerves and homotopy (backlog)

**Status:** ideas preserved, not active. Classical Čech nerves and Dowker duality predate this discussion; the possible research is in new comparisons and theorems, not in inventing the nerve.

## Nerves and overlap graphs

Given a cover `(u_i)_{i∈I}` in frame `L` with `⋁_i u_i=1`, define its nerve `N(u)` on vertex set `I`:
```text
finite nonempty σ ⊆ I is a simplex ⇔ ⋀_{i∈σ}u_i ≠ 0.
```
Its 1-skeleton is the overlap graph of the cover. Its clique complex contains the nerve; equality holds iff every finite family of pairwise overlapping members has nonzero total meet (finite Helly property).

In finite `T_0` Alexandrov spaces, choosing smallest neighborhoods `u_x=U_x` gives exactly Cameron–Kumar's inseparability complex.

## Pointless example; important caveat

The complete Boolean algebra `RO(S¹)` is atomless, hence its locale is pointless. Three regular-open arcs centered 120° apart, each of half-width 75°, join to 1, overlap pairwise, and have zero triple meet. Their nerve is the boundary of a triangle, hence its reduced `H_1` is `ℤ`.

**Crucial:** this *one cover* does not prove that the locale has the homotopy type of `S¹`; refine covers, possibly by disjoint families, to obtain an invariant. A nerve is a cover-dependent object.

## Nerves across refinements

Refinements induce simplicial maps between nerves, up to contiguity. Study the pro-homotopy/shape construction from all covers or suitable cofinal systems, and understand when the nerve of a selected cover suffices.

## Dowker

For two families `(a_i)_{i∈I}`, `(b_j)_{j∈J}` choose an incidence relation such as `iRj ⇔ b_j≤a_i`. Apply Dowker duality to its two complexes. With a suitable join-dense family of nonzero `b_j`, the complex on `I` is the meet-nerve of `(a_i)`, because `⋀_{i∈σ}a_i≠0` iff it dominates some nonzero `b_j`.

## Questions

1. Which frame properties force nerve = clique complex for a natural cofinal class of covers?
2. Which covers allow a nerve lemma recovering *localic* homotopy/shape?
3. Which Dowker constructions naturally extend the paper's two complexes?
4. Which homotopical invariants survive for purely pointless locales?

## References to check

- Cameron–Kumar, arXiv:2610.14783, especially §9.
- Dowker's theorem on two complexes of a relation.
- Čech homotopy, shape theory, point-free or topos-theoretic constructions.
