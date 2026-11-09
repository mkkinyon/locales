# Project A — Internal adversarial audit of the far-grid converse counterexample

**8 November 2026 | Internal-only report — do not include with the blind referee packet**

## Claim audited

For the frame of opens of a countable space with points q, p_i, r_i, s_{i,m} and basic opens P_i={p_i}, T_{i,m}={s_{i,m}}, R_{i,m}={r_i,p_i}∪{s_{i,t}:t≥m}, N_n={q}∪⋃_{i≥n}S_i, the claim is that I=U as closed sublocales of the localic square but that the far-grid property fails for a=⋃_i P_i and b=N_1. Ancillary claims: X is T0, sober, first-countable and non-locally-compact at q.

**Internal verdict: PASS.** No mathematical error found. The listed basic opens additionally form a countable base, so X is second-countable. External verification is still required before upgrading provenance.

## 1. Topology and closures — independently checked

The generating family is a basis: R_{i,m}∩R_{i,m'}=R_{i,max(m,m')}; N_n∩N_{n'}=N_{max(n,n')}; if i≥n then R_{i,m}∩N_n=⋃_{t≥m}{s_{i,t}}, otherwise empty. Intersections involving singletons either vanish or are that singleton. Every point lies in a member of the basis.

Each point has the following neighborhood basis:

- p_i and s_{i,m}: their singleton;
- r_i: R_{i,m}, m≥1;
- q: N_n, n≥1.

For arbitrary A⊆X one has p_i∈cl A iff p_i∈A; s_{i,m}∈cl A iff s_{i,m}∈A; r_i∈cl A iff every R_{i,m} meets A; q∈cl A iff every N_n meets A. These conditions give exactly

cl(P_i)=P_i∪{r_i}; cl(T_{i,m})=T_{i,m}; cl(R_{i,m})=R_{i,m}; cl(N_n)=N_n∪{r_i:i≥n}.

In particular, although a point s_{i,m} is isolated, it does *not* belong to the closure of a singleton p_i. The stated closure identities are correct.

## 2. Enumeration of basis pairs — independently checked

For basis types P_i, T_{i,m}, R_{i,m}, N_n, the complete ten unordered type pairs are PP, PT, PR, PN, TT, TR, TN, RR, RN, NN. These give exactly the ten rows of the working note. For every disjoint pair except PN with i≥n, the above closures are disjoint; the exceptional pair has common closure point r_i.

For i≥n, N_n=N_{i+1}∨⋁_{j=n}^i ⋁_{t≥1}T_{j,t}, and each summand is far from P_i. In particular, P_i⊠N_n≤d_U via *one* arbitrary-join decomposition in the second variable. Every disjoint basis rectangle lies below d_U.

## 3. Localic—not pointwise—equality

Every open u is the join of basis elements contained in u. Therefore for u∧v=0,

u⊠v=⋁_{B⊆u,C⊆v}(B⊠C)≤d_U.

This holds in the actual frame coproduct L⊕L because the two coproduct injections preserve arbitrary joins and the frame meet distributes over joins. Taking the join over all disjoint pairs gives d_I≤d_U. The other inequality follows from far ⇒ disjoint. Equality of d_I and d_U yields equality of the corresponding *closed sublocales*, not just their ordinary points.

No spatiality of the localic product is invoked, and no compactness/continuity assumption is hidden in this part of the proof.

## 4. Grid obstruction — independently checked

For a=⋃_iP_i and b=N_1, we have a∩b=∅. If b=⋁_β b_β then some b_β0 contains q (ordinary union of opens), so N_n⊆b_β0 for some n. For every i≥n choose a_αi containing p_i; then r_i is in both cl(a_αi) and cl(b_β0). Hence they are not far, contradicting the demanded grid. This uses only basic open-cover quantifiers, and the family of pieces is unrestricted; allowing arbitrarily many pieces does not help.

The argument even fixes a single b-piece and forces infinitely many violations (one for every sufficiently large i).

## 5. Auxiliary topological claims — independently checked

- The displayed basis is **countable**, hence X is second-countable and in particular first-countable. The topology is T0 since the neighborhood systems distinguish distinct points.
- B_i=R_{i,1}={r_i,p_i}∪S_i is clopen: complement points in other blocks have their own R/singleton neighborhoods, and q has N_{i+1}. Inside B_i each T_{i,m} is clopen; the complement is open around r_i via R_{i,m+1}. A nonempty irreducible closed subset of B_i containing a point s is that singleton. Otherwise it is contained in {r_i,p_i}, where the only nonempty closed subsets are {r_i} and {r_i,p_i}, with generic points r_i and p_i. Any irreducible closed F⊆X is contained in one clopen B_i if it meets it, or in the residual singleton {q}. Therefore X is sober.
- X is not compact: N_1 together with all B_i is an open cover with no finite subcover. X is not locally compact at q: if a compact K contains N_n and infinitely many r_i, the same cover of K fails to be finite; otherwise select i≥n with r_i∉K. Cover K by N_{i+1}, all B_j (j≠i), P_i and all singletons T_{i,m}; because S_i⊆K and none of the other members covers any point of S_i, this cover has no finite subcover. Thus no compact neighborhood of q exists.

## 6. Boundaries and limitations

The example refutes only the reverse implication (I=U ⇒ far-grid) for arbitrary frames and the indicated second-countable sober frame. It does not refute far-grid equivalence in compact/coherent/continuous/algebraic classes. It also does not settle what *other* relation identities far grids might imply, or establish novelty relative to locale/proximity literature. The argument is an internal proof and should be sent to an external referee *without* this audit.

**No ledger or repository changes made as part of this audit.**