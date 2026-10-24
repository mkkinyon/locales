# Project A — Upper diamond fails outside coherence: a compact scattered T1 example

24 October 2026. **New focused working theorem with frame-valid proof, not independently externally audited.** Reexamines the previously independently audited compact noncoherent alpha–beta–gamma example for cl(D)<U, and computes ALL six relations plus the hull H. The key new observation is that its localic square is spatial/scattered, so the closed inseparability relation I is itself fitted. This resolves the unrestricted upper-diamond inclusion NEGATIVELY and verifies the previously undecided example-specific equality cl(D)=I.

## 1. General lemma: spatial scattered T1 localic square forces V=I

Let X be a T1 space such that its **LOCALIC square Q=O(X)⊕O(X)** is spatial, identifies with O(X×_top X), and its ordinary topological product X×X is scattered. Then:
  **D=Δ,  V=V_2=I,  H=I,  cl(D)=I.**

First, a spatial scattered frame has EVERY sublocale spatial (Simmons' scattered-sublocale theorem). An elementary weaker fact suffices: every nonzero sublocale has an ordinary point. Indeed, close any nonzero sublocale R to a nonempty closed subspace K; choose an isolated point p of K (scatteredness); R is dense in K and must meet its nonzero open singleton {p}; the only nonzero sublocale of a point is the point itself.

Point relation of I=C(d_I) is ordinary inseparability: pairs that admit no disjoint neighborhoods. For each separable pair x≠y, since T1, the opens
  A=X\{x}, B=X\{y}
exist. The two-strip open
  w_xy=(A⊠1)∨(1⊠B)
misses the ordinary product point (x,y), and is a genuine rank≤2 BAR: horizontally cover first coordinate by A and a neighborhood U∋x, and under U vertically cover second by B and a disjoint neighborhood V∋y; the (U,V) leaf is disjointness and the other two leaves are w_xy rectangles. Thus every product point outside I is omitted by some RANK-TWO open neighborhood O(w_xy) of I.

It follows that I⊆V_2 and pt(V_2)⊆pt(I). If V_2>I, then V_2∩O(d_I) is a nonzero sublocale: the sublocale lattice is distributive for finite meets and joins, while C(d_I),O(d_I) are complementary; the intersection would carry an ordinary point of V_2 outside I, contradiction. Hence V_2=I. Since I⊆V⊆V_2, V=I: the closed relation I is already FITTED. As H is the smallest closed-and-fitted sublocale containing Δ, and I=cl Δ is closed/fitted, H=I.

For D: in a T1 space every offdiagonal ordinary pair (x,y) is omitted by a diagonal-cover open w=(X\{x})⊠(X\{x})∨(X\{y})⊠(X\{y}), so pt(D)=pt(Δ). Spatiality of all sublocales implies D=Δ, hence cl(D)=I.

This lemma has no coherence or compactness hypothesis beyond spatial/scattered localic square; the conditions hold automatically if X is **locally compact, sober, T1 and scattered**: the localic square coincides with the ordinary product by the Isbell theorem (locally compact sober factor), and a finite topological product of scattered spaces is scattered (isolate a point of the first projection of any nonempty subset, then of the corresponding fiber).

Note on literature: the theorem "every sublocale of spatial scattered locale is spatial" is classical Simmons (see Suarez 2022 J. Pure Appl. Algebra 226 106851, and Ball–Picado–Pultr 2016). The universal rank≤2 witness for separable T1 point pairs is elementary and does not identify product points with all sublocales without the scattered premise.

## 2. The space

Let N1,N2 be two disjoint countably infinite discrete sets. Adjoin alpha,beta,gamma, and give all n∈N1∪N2 isolated singleton neighborhoods. Neighborhood bases at the three extra points are:
  alpha: {alpha}∪(N1\E), E finite;
  beta : {beta}∪((N1∪N2)\E), E finite;
  gamma: {gamma}∪(N2\E), E finite.
These generate a topology on X=N1∪N2∪{alpha,beta,gamma}.

Properties:
- X is T1 (each singleton closed), compact (union of three compact cofinite-tail neighborhoods plus finitely many leftover isolated points), locally compact (every displayed basic neighborhood is compact).
- X is scattered: any nonempty subset meeting N1∪N2 has an isolated element; a subset contained in the three-point T1 remainder is finite discrete. Scattered T1 implies sober by the isolated-point argument for irreducible closed subsets.
- X is NONCOHERENT: compact opens Ualpha={alpha}∪N1 and Ubeta={beta}∪(N1∪N2) have intersection N1, an infinite discrete NONCOMPACT open. Thus compact opens not meet-closed.
- Its localic square equals the ordinary topological product because X locally compact sober, and the product is scattered.

## 3. Exact pointwise I and U

All isolated n are clopen: {n} open and its complement open because tails can omit n. Therefore distinct pairs involving any n can be separated by far rectangles.

The alpha/beta neighborhoods always intersect in a cofinite subset of N1; beta/gamma neighborhoods always intersect in a cofinite subset of N2. Thus
  alpha I beta,  beta I gamma.
There are disjoint opens Ualpha={alpha}∪N1 and Ugamma={gamma}∪N2. Thus alpha NOT-I gamma.

For any alpha-neighborhood A and gamma-neighborhood B, beta belongs to cl_X(A)∩cl_X(B). Indeed beta-neighborhoods include cofinite tails of BOTH N1 and N2. Thus A*∨B*≠1 and alpha U gamma. Alpha/beta and beta/gamma already belong to U by I≤U.

If one coordinate is isolated n and the other is distinct, a clopen singleton around n and its complement give far neighborhoods, so those pairs are not U. Hence the ordinary point relations are precisely
  pt(I)=Δ ∪ {(alpha,beta),(beta,alpha),(beta,gamma),(gamma,beta)},
  pt(U)=Δ ∪ ({alpha,beta,gamma}²).
Here Δ includes all diagonal pairs, so the second formula means one three-point offdiagonal equivalence class and singleton classes for all n.

All real-valued continuous functions on X satisfy f(alpha)=f(beta)=f(gamma), by uniqueness of limits along N1 and N2, and the clopen singleton characteristic functions distinguish every n from each other and from alpha,beta,gamma. Thus
  pt(F)=pt(U).
Both F and U are CLOSED sublocales of the spatial product, and closed sublocales are determined by their ordinary closed point sets. Therefore
  **U=F** as genuine localic relations.

## 4. Complete hierarchy for this X

By §1,
  D=Δ,
  W=cl(D)=I,
  V=I,
  H=I.
By §3, I<U=F.
Also M=I∩D=Δ and J=I∨D=I.

Hence:
  **Δ=D=M ⊊ I=J=V=W=H ⊊ U=U∨V=F.**

Because alpha I beta and beta I gamma but alpha NOT-I gamma, H=I is NOT TRANSITIVE. The coherent two-patch-convergent-rays example from 24 October is a separate, stronger coherent nontransitivity witness, but the present example supplies a much SIMPLER general counterexample in compact locally compact sober T1 locales.

The verified compact general theorem U=I∘I is perfectly compatible: it fills the missing graph edge alpha–gamma by composition, whereas closed-and-fitted hull H leaves the already closed/fitted path graph I unchanged. This is a strong connection to the original Cameron–Kumar graph motivation.

## 5. Universal upper-diamond conclusion and correct formal replacement

Set W=cl(D)=cl(fit Δ), V=fit(I)=fit(cl Δ), H=least closed-and-fitted hull of Δ.

For EVERY locale:
  **W∨V≤H≤F**.
Proof: H contains Δ and is closed and fitted, so it contains D=fitΔ, then W=clD, and also contains I=clΔ, then V=fitI.

Moreover
  **H=Hull_closed&fitted(W∨V)**.
This is the universal formal 'upper diamond' with the correct pair of cross-hulls.

By contrast U is NOT generally the closure of D: in this example W=I<U, and H=I. Thus
  U∨V=U > H,
so **U∨V≤H fails**, even for compact, locally compact, sober, scattered T1 locales.

The reverse general comparison **H≤U∨V** also fails: in the already calculated connected finite six-point Alexandrov zigzag, H=F=P², while U∨V omits selected pairs (0,3),(3,0).

Therefore U∨V and H are UNIVERSALLY INCOMPARABLE as locale-constructors: each direction fails on a concrete locale. Combining the two examples by disjoint union, and using the working clopen-component restriction theorem for the relations, produces a single compact locale where neither inclusion holds.

This directly vindicates the user's clarification that V=fit(I) may not represent the intrinsic dual phenomenon of U beyond coherence. Replacing U by the literal cross-hull W gives a valid universal diamond, but need not recover the originally intended Urysohn relation.

## 6. Next research problems, no priority asserted beyond current cycle

- Understand H as a common closed/fitted completion of W∨V, now that U∨V cannot be assumed inside it.
- Seek useful hypotheses weaker than coherence guaranteeing U≤H, perhaps by examining the localic complement of closed fitted diagonal supersets. Simply imposing compactness or T1 is NOT sufficient.
- Ask whether U≤H can be characterized by a frame cover condition; e.g. for every closed fitted S=C(e) containing Δ, e≤d_U. This is exact but currently tautological.
- Retain the coherent graph-closure result H transitive iff H=F, but verify the separate Priestley proof externally before publication. The present noncoherent example shows transitivity failure needs no highly elaborate construction.
- Return to lower diamond U∧V vs T(J) after recording upper-diamond asymmetry. In this example U∧V=I=T(J), so it does not address noncoherent strictness of that lower-diamond comparison.

**References:**
- A-Claude-three-claims-focused-verification-2026-10-21.md for original compact noncoherent strict cl(D)<U, externally reviewed.
- A-fitted-diagonal.md for fitted diagonal and T1 ordinary point characterization.
- A-V-Claude-almost-normal-example-exact-V-equals-I-2026-10-23.md for related scattered-square spatial arguments.
- Isbell, "Product spaces in locales", Proc. Amer. Math. Soc. 81 (1981), 116–118.
- A. L. Suarez, "On the relation between subspaces and sublocales", J. Pure Appl. Algebra 226 (2022), 106851.
- Ball–Picado–Pultr, "On an aspect of scatteredness in the point-free setting", Portugaliae Mathematica 73 (2016), 139–152.
