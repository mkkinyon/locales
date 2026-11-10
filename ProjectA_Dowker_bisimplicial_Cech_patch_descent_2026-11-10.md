# Project A — Bisimplicial Dowker comparison: Čech nerves, one-sided properness, and patch descent

**10 November 2026. Working research note; internally checked deductions, NOT externally audited; no literature-priority claim.**

**Context:** Follow-up to [Cameron–Kumar revisited](ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md) and the [coherent composition canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md). All composition/hull identifications are restricted to the coherent scope of those results. Our specialization convention is x≤y iff x lies in closure of {y}; spectral opens are upsets.

## 1. General localic bipartite construction

For any localic relation R↪X×Y, let E_{p,q}(R)↪X^{p+1}×Y^{q+1} (p,q≥0) be the meet of the (p+1)(q+1) inverse images of R, imposing every x_i R y_j. Write K_p=im(E_{p,0}→X^{p+1}) and L_q=im(E_{0,q}→Y^{q+1}). Coordinate deletion/repetition makes E bisimplicial and K,L simplicial.

**Čech lemma (all locales).** In Loc there are canonical isomorphisms

 E_{p,q} ≅ E_{p,0} ×_{K_p} ... ×_{K_p} E_{p,0} (q+1 copies),
 E_{p,q} ≅ E_{0,q} ×_{L_q} ... ×_{L_q} E_{0,q} (p+1 copies).

Proof: K_p↪X^{p+1} and L_q↪Y^{q+1} are sublocale inclusions. Fiber products over these inclusions agree with the fiber products over the ambient powers; the latter impose exactly the defining intersection of all pulled-back R conditions. Thus each row/column is the strict Čech nerve of the respective image-factorization map r_p:E_{p,0}→K_p or s_q:E_{0,q}→L_q. Both maps are surjective by definition of localic image, but arbitrary surjections of locales need not be effective descent, and their arbitrary base changes need not stay surjective.

## 2. Coherent specialization and proper rows

Suppose X is coherent spectral, P=pt(X), and R=A is the proconstructible oriented specialization relation (x≤y). The coherent higher-diagonal argument gives K_p=cl(Δ_{p+1})=:I^(p+1) and L_q=fit(Δ_{q+1})=:D^(q+1), as actual proconstructible sublocales. The patch point descriptions are the tuples admitting respectively a common upper or common lower bound. All E_{p,q}, K_p, L_q are proconstructible spectral locales.

**Proposition (proper rows).** Each r_p:E_{p,0}(A)→K_p(A) is a proper surjection of locales.

Proof: r_p is spectral, hence its right adjoint on frames preserves directed joins (perfectness). To show it is closed in Loc, let C be a closed sublocale of E_{p,0}. It is represented by a patch-closed downward-specialization-closed subset of the spectral points. Its image under r_p is patch closed, because the map is continuous for the compact Hausdorff patch topologies. It is also downward closed: if ((x_0,...,x_p),y) belongs to C and x'_i≤x_i for all i, then ((x'_0,...,x'_p),y)≤((x_0,...,x_p),y) belongs to C, and its projection is (x'_0,...,x'_p). A patch-closed downward closed subset of a spectral space is closed; by the coherent proconstructible image theorem, this also identifies the actual image sublocale as closed. Therefore r_p is a closed, perfect map, hence proper. Its surjectivity is definitional.

Vermeulen, *Proper maps of locales* (J. Pure Appl. Algebra 92 (1994)), Theorem 5.6, proves proper surjections are effective descent morphisms in Loc. Thus E_{p,•}→K_p is a proper effective-descent Čech nerve, for every p.

## 3. The opposite columns need not be open or proper

For s_q:E_{0,q}(A)→L_q, increasing y coordinates lifts by holding witness x fixed. For **finite Alexandrov** locales this means s_q is an open surjection, hence effective for descent by Joyal–Tierney. However it is neither generally proper nor generally open over all coherent locales.

**Nonproper finite example.** Let P={a,b,t}, a<t and b<t. In E_{0,0}=A, the principal closed downset of (a,t) maps under s_0 (second projection) onto {a,t}. This is not closed in P because b≤t. Hence s_0 fails closedness/properness.

**Nonopen coherent example (working explicit Priestley construction).** Take the patch space P to be three disjoint convergent sequences A={a_n:n≥1}∪{a_∞}, B={b_n:n≥1}∪{b_∞}, C={c_n:n≥1}∪{c_∞}, plus isolated d. Order P by the strict comparisons a_n<b_n,c_n (for each n), a_∞<b_∞,c_∞, d<b_∞,c_∞ and no others. The order is patch closed; P is Priestley: a finite a_n has a clopen upset {a_n,b_n,c_n}, a limit a_∞ has an upset consisting of tails of the three sequences including all limits, b_∞ and c_∞ have their respective clopen tails, finite b_n/c_n are maximal isolated points, and d has clopen upsets {d,b_∞,c_∞} plus sufficiently long b/c tails. These separate every noncomparable ordered pair. Thus the corresponding upper-set topology is spectral coherent.

Let U={d}∪B∪C, a patch-clopen upset/compact spectral open. In E_{0,1} impose x∈U for the witness x≤y_0,y_1, forming an open sublocale O. Its image under s_1 contains (b_∞,c_∞) by witness d, but excludes every (b_n,c_n), whose only lower witness is a_n∉U. Those pairs lie in L_1 (they possess the common lower a_n), and converge to (b_∞,c_∞) in the patch topology of L_1. Hence s_1(O) is not open, and s_1 is not an open locale map.

These examples defeat a symmetric argument using *open-or-proper* surjections in original spectral topology. They do not establish failure of effective descent for s_q; triquotiency or other special descent properties remain to be investigated.

## 4. A two-sided positive result after patching

**Proposition (patch Čech comparison).** More generally, let X,Y be coherent locales and R⊆X×Y be any proconstructible spectral relation. Then K_p(R), L_q(R), E_{p,q}(R) are all proconstructible spectral locales, and their patch locales are Stone. Furthermore, patching identifies BOTH Čech decompositions:

 Patch(E_{p,q}) ≅ Patch(E_{p,0}) ×_{Patch(K_p)} ... ×_{Patch(K_p)} Patch(E_{p,0}),

and dually over Patch(L_q).

Proof: all the relevant point sets are patch-closed subsets of finite products of compact Hausdorff patches. The images K,L are patch-closed by compactness, and the two fiber product descriptions give precisely the same patch-closed subset of the same finite product, with its subspace topology. This proves the identities of Stone locales.

Both Patch(r_p) and Patch(s_q) are surjections of Stone locales: they are onto on the patch point sets, and Stone locales are point-determined. Any continuous map of compact Hausdorff spaces is proper, so these are **proper surjections of locales in both directions**. Thus they are effective descent morphisms by Vermeulen.

**Dowker-type corollary (sheaf-theoretic patch invariant).** Let Shv∞(Stone,surj) be the ∞-topos of space-valued sheaves for the topology generated by surjections of Stone locales (choose a universe if necessary), and y the representable sheaf. Each patched Čech nerve presents its target as a geometric realization, giving a canonical equivalence

 | y(Patch K_•(R)) | ≃ | y(Patch L_•(R)) |

in that ∞-topos. Proof: the patched E_{p,q} form a bisimplicial object; row-wise Čech descent realizes to y(Patch K_p), and column-wise Čech descent realizes to y(Patch L_q). The two iterated colimits agree by Fubini for colimits. The topology is subcanonical because proper surjections are effective descent in Loc. This statement includes R=A, in which case K=I^(•+1), L=D^(•+1).

For finite posets, patch spaces are finite discrete; restricting to finite discrete objects returns the ordinary two simplicial sets of common-upper and common-lower witness tuples, so the argument reduces to classical Dowker homotopy equivalence.

**Scope warning.** This is a statement in a particular sheaf homotopy theory of **patched** spectral locales. It does NOT establish an equivalence of naive topological realizations of the original spectral simplicial locales, or an equivalence in a general homotopy theory of all locales. Patching changes topology, and the original column maps are not generally open/proper. Do not promote the comparison without a definition and verification of the intended localic homotopy invariant.

## 5. Audit and next bounded tasks

1. Independently verify the proper-map proof using Vermeulen's closed/perfect characterization, including the passage from spectral closed images to genuinely closed localic images.
2. Independently verify the convergent Priestley nonopen example; the finite nonproper example is elementary.
3. Formalize the Stone surjection sheaf site and the bisimplicial homotopy-colimit argument, checking size/subcanonicity and exact definition of the invariant.
4. Ask whether the unpatched s_q is triquotient or effective descent (Plewe 1997), or identify a counterexample. Avoid inferring anything from its going-up property alone.

**Bibliographic inputs:** Vermeulen (1994), *Proper maps of locales*; Plewe (1997), *Localic triquotient maps are effective descent maps*; Joyal–Tierney open-surjection descent theorem; standard Priestley/spectral topology; project coherent composition canonical proof (8 Nov 2026).