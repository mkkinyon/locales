# Point-Free Topology — Mixed open/closed Čech descent, ordinal sums, and higher nonconstant sheaf homotopy

**10 November 2026 · NEW internally checked research segment; NOT externally blind-audited.** Continues [all-locale open-cover / coherent D-side codescent](PointFree_D_side_open_cover_Cech_descent_2026-11-10.md), [two-apex nonconstant suspension](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md), and the [canonical chain/hull theorem after two independently blind-reviewed phases](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md). No claim of literature priority. The finite-poset crosscut and type-level Dowker results are classical, including Cameron–Kumar §9. The novelty status of these particular sheaf/ordinal-sum formulations has not been investigated.

## 0. Notation and scope

All locales below are classical coherent locales. For a coherent X write K(X) for compact opens and P_X for its compact ordered Priestley patch space. The specialization order has spectral opens as upsets and closed sublocales as downsets. We use the sufficiently large finite-surjective-cover Stone sheaf \(\infty\)-topos \(\mathscr H_\kappa\) from the independently refereed canonical account, h for sheafified Yoneda, and \(\underline{(-)}\) for constant objects. Write
\[
\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet X)|,\quad
\mathbf I(X)=|h(\operatorname{Patch}I_\bullet X)|,\quad
\mathbf D(X)=|h(\operatorname{Patch}D_\bullet X)|.
\]
Statements are in **patched sheaf homotopy**, not intrinsic locale shape. A coherent X is assumed nonzero whenever choosing a spectral point (BPIT).

For A∈\(\mathscr H_\kappa\), define its **unreduced suspension** \(\Sigma A=1\amalg_A1\); in a general ∞-topos \(\Sigma^mA\) is iterated homotopy pushout. For A,B define \(A*B=\operatorname{hocolim}(A\leftarrow A\times B\to B)\), the **homotopy join**, not the product and not a pushout of unpatched locales.

## 1. Mixed two-cover chains and Čech codescent

**Proposition 1 (mixed grid).** Suppose X is coherent, with a finite closed-downset cover \(\{Z_i=C(c_i)\}_{i=1}^r\), \(\bigwedge_i c_i=0\), and a finite compact-open-upset cover \(\{U_j=O(u_j)\}_{j=1}^s\), \(\bigvee_j u_j=1\), with c_i,u_j compact opens for simplicity. Let \(W_{ij}=Z_i\cap U_j\), patch-clopen order-convex spectral sublocales. Then in every simplicial degree n
\[
\{\operatorname{Patch}\operatorname{Ch}_n(W_{ij})\to
\operatorname{Patch}\operatorname{Ch}_n(X)\}_{i,j}
\]
is finite jointly surjective. Indeed a chain \(x_0\le\cdots\le x_n\) lies in some Z_i containing x_n by downward closure, and some U_j containing x_0 by upward closure. Thus it lies in W_ij. All objects are actual coherent proconstructible spectral sublocales, so patch pointwise coverage proves genuine Stone coverage.

The **iterated Čech diagram** with (i_0,...,i_p) in the closed direction and (j_0,...,j_q) in the open direction, with cells
\[
\mathbf C(Z_{i_0}\cap\cdots\cap Z_{i_p}\cap
U_{j_0}\cap\cdots\cap U_{j_q}),
\]
has total realization \(\mathbf C(X)\). Proof: first apply finite effective Čech descent for the closed cover to each chain degree; apply the open cover on each closed-chart intersection (or vice versa); commute the three colimits (two Čech and one chain simplicial). All are finite joint Stone surjections and h preserves finite limits and coproducts. **Do not silently replace these Čech diagrams with multiplicity-free poset diagrams.**

**Caveat:** The mixed cells W_ij generally do **not** simultaneously cover either entire higher hull I_n or D_n. For the two-sided example below, (a,b) belongs to I_1 by upper witness p but cannot lie in any single W_ij, while (p,q) belongs to D_1 by lower witness a but lies in no W_ij. The **closed cover** descends the *ambient upper hull* and the **open cover** descends the *ambient lower hull*, separately. The mixed bicover statement is a theorem about the **chain** simplicial locale; it does not undo the independently audited failure of unpatched lower-witness projection descent.

## 2. Ordinal sums: arbitrary coherent locales

For nonempty coherent P,Q, define their **ordinal sum** \(P\oplus Q\) using the disjoint-union patch Stone space with original orders and all comparisons \(p<q\) for p∈P,q∈Q. It is Priestley: the order is closed; for noncomparabilities within P extend a clopen P-upset by all Q, within Q use the Q-upset itself, and Q does not lie below P, separated by Q as a clopen upset. Therefore it defines a coherent locale.

**Theorem 2 (ordinal-sum join and hull collapse).**
\[
\boxed{\mathbf C(P\oplus Q)\simeq\mathbf C(P)*\mathbf C(Q),\qquad
\mathbf I(P\oplus Q)\simeq\mathbf D(P\oplus Q)\simeq1.}
\]

**Proof of join formula:** In degree n, every chain in P⊕Q has a unique cut, consisting of an initial P-chain of length i+1 (possibly empty), followed by a Q-chain of length n-i (possibly empty). The cut index i∈{-1,...,n} is a finite patch-clopen partition of Ch_n(P⊕Q). Each piece is Ch_i(P)×Ch_(n-i-1)(Q), with Ch_(-1)=1 (the empty-chain convention). Thus \(\operatorname{Patch}\operatorname{Ch}_\bullet(P\oplus Q)\) is the strict **simplicial join** of the two chain nerves. Since h preserves finite coproducts/products and realization of simplicial joins identifies with the homotopy join in an ∞-topos (check objectwise in presheaf spaces, then sheafify), \(\mathbf C(P\oplus Q)\simeq\mathbf C(P)*\mathbf C(Q)\). The nerve-of-categorical-join fact is classical (Joyal's join, see Kapulkin dissertation §3.3.6–3.3.8 and standard simplicial topology).

**Independent direct proof of I,D collapse:** Choose spectral points p0∈P, q0∈Q. Inserting p0 into a common-upper tuple preserves the ambient upper-witness property: if any coordinate lies in Q, its original common upper bound lies in Q and also bounds p0; if all coordinates lie in P, *any* Q point bounds the enlarged tuple. Hence insertion of p0 is an extra degeneracy of I_•(P⊕Q), including a point at degree -1. Similarly insertion of q0 preserves common-lower witnesses of D_•: if any coordinate is in P, an original lower witness lies in P and is below q0; if all coordinates lie in Q, any point of P bounds them below together with q0. Because the higher hulls are actual coherent proconstructible sublocales and the inserting sources are spatial spectral, these factor as strict spectral/localic maps; the simplicial extra-degeneracy identities are coordinate identities. Thus each simplicial object realizes to 1 (even prior to Patch as a combinatorial contraction). No need to use the audited edgewise arrow theorem or either Čech descent to prove this collapse. This is a particularly good independent consistency check.

**Corollary:** For any nonzero coherent Z, adjoining a two-element incomparable **top layer** A gives \(\mathbf C(Z\oplus A)\simeq\Sigma\mathbf C(Z)\); adjoining a two-element incomparable **bottom layer** gives \(\mathbf C(A\oplus Z)\simeq\Sigma\mathbf C(Z)\). Here \(\mathbf C(A)=\underline{S^0}\) and \(\underline{S^0}*B\simeq\Sigma B\). In either case \(\mathbf I,\mathbf D\) are terminal. The suspension formula is alternatively a **direct Čech pushout** from respectively the finite closed downset cover by Z∪{p} and Z∪{q}, or the finite compact-open upset cover by {a}∪Z and {b}∪Z.

## 3. Two-sided suspension and genuine mixed codescent

For nonempty Stone S, take the three-layer ordinal sum
\[
X(S)=\{a,b\}\oplus S\oplus\{p,q\},
\]
with both endpoint layers two-element antichains, and every a,b below every s∈S below every p,q. Patch topology is the disjoint union of S and isolated endpoint points. It is Priestley; its compact-open lattice is the **ordinal sum of bounded distributive lattices**
\[
K(X(S))\cong \mathsf B_2\oplus\mathrm{Clop}(S)\oplus\mathsf B_2,
\]
where \(\mathsf B_2\) is the 4-element Boolean diamond and consecutive extreme elements are identified.

Closed downsets \(Z_p=X\setminus\{q\}\) and \(Z_q=X\setminus\{p\}\) cover X and have terminal chain nerves via greatest points p,q. Their intersection \(B=\{a,b\}\oplus S\) is itself covered by compact-open upsets \(B_a=\{a\}\oplus S\) and \(B_b=\{b\}\oplus S\), each having a least point, with intersection S. The two directions of Čech descent give
\[
\mathbf C(B)\simeq 1\amalg_{h(S)}1=\Sigma h(S),
\qquad
\boxed{\mathbf C(X(S))\simeq1\amalg_{\mathbf C(B)}1=\Sigma^2h(S).}
\]
Reversing the order of open and closed Čech calculations gives the same result. Explicitly the four mixed cells
\[
W_{a,p}=\{a\}\oplus S\oplus\{p\},\quad
W_{a,q},\ W_{b,p},\ W_{b,q}
\]
all have both least and greatest points, so their chain realizations are terminal. Every one-coordinate row/column intersection has a least or greatest point and realizes to 1, but the **double intersection** of all four is S, whose chain realization is \(h(S)\). Thus the obstruction occurs in bidegree (1,1) of the mixed Čech construction and becomes a *double suspension*. The two ways of iterating the homotopy pushouts agree by commutation of colimits; no orientation/sign claim on \(\pi_2\) is made here.

For the closed hull, the relative upper-hull objects on Z_p, Z_q and their overlap B are \(Z_p^{\bullet+1},Z_q^{\bullet+1},B^{\bullet+1}\), as p and q are ambient upper witnesses; all realize to 1 and give \(\mathbf I(X(S))\simeq1\). Dually the open cover U_a=X\setminus\{b\}, U_b=X\setminus\{a\} has ambient lower-hull objects \(U_a^{\bullet+1},U_b^{\bullet+1},(U_a\cap U_b)^{\bullet+1}\), all realizing to 1, so \(\mathbf D(X(S))\simeq1\), **independently and directly**. This also follows from the independent extra-degeneracy argument in §2.

**Main two-sided formula:**
\[
\boxed{\mathbf C(X(S))\simeq\Sigma^2h(S),\qquad
\mathbf I(X(S))\simeq\mathbf D(X(S))\simeq1.}
\]
The common homotopy cofibre of the canonical arrows is \(\Sigma^3h(S)\). For S=two discrete points, the finite six-point poset has \(\operatorname{Ord}\simeq S^2\) and both witness complexes contractible; this and m=3,4 layered finite examples were independently checked computationally by boundary-matrix ranks over \(\mathbf F_2\).

**Important contrast:** The mixed 2×2 cover cells cover \(\operatorname{Ch}_\bullet(X)\), but not the *whole* \(I_\bullet(X)\) or \(D_\bullet(X)\): \((a,b)\in I_1\) and \((p,q)\in D_1\) escape all cells. The upper/lower hull contractions use the separate appropriate one-sided cover, not the mixed chart nerve.

## 4. Arbitrarily high nonconstant homotopy sheaves

Let \(A\) denote the two-point equality-ordered coherent locale, \(\mathbf C(A)=\underline{S^0}\). For integers r,s≥1 and a nonempty Stone S, define a layered coherent locale
\[
X_{r,s}(S)=\underbrace{A\oplus\cdots\oplus A}_{r\text{ lower layers}}
\oplus S\oplus\underbrace{A\oplus\cdots\oplus A}_{s\text{ upper layers}}.
\]
By the ordinal-sum join theorem,
\[
\boxed{\mathbf C(X_{r,s}(S))\simeq\Sigma^{m}h(S),\quad
\mathbf I(X_{r,s}(S))\simeq\mathbf D(X_{r,s}(S))\simeq1,\quad m=r+s\ge2.}
\]
The compact-open lattice has an explicit finite ordinal-sum presentation
\(K(X_{r,s}(S))\cong(\mathsf B_2)^{\oplus s}\oplus\mathrm{Clop}(S)\oplus(\mathsf B_2)^{\oplus r}\), with the direction of layers reversed by the order/upset correspondence.

Let \(\mathcal K_S=\ker(\mathbb Z[h(S)]\overset{\varepsilon}\to\mathbb Z)\), where \(\mathbb Z[-]\) is the free abelian sheaf. For nonempty S, h(S)→1 is an effective epi. Therefore the unreduced m-fold suspension is (m−1)-connected for m≥2, and its only nonzero reduced integral homology sheaf is
\[
\widetilde{\mathcal H}_m(\mathbf C(X_{r,s}(S));\mathbb Z)\cong\mathcal K_S.
\]
The sheaf-internal Hurewicz theorem identifies the first nontrivial homotopy sheaf:
\[
\boxed{\pi_m(\mathbf C(X_{r,s}(S)))\cong\mathcal K_S,\quad \pi_i=0\ (1\le i<m).}
\]
A direct objectwise/sheaﬁfication check is also available: the presheaf before sheafification is T↦Σ^m Hom_Stone(T,S), a wedge of (|Hom(T,S)|−1) m-spheres after choosing a basepoint s0∈S, and the sheafified π_m is \(\mathcal K_S\). The constant-object functor is full and faithful on spaces, but for infinite S the **sheaf \(\mathcal K_S\) is nonconstant**, as proved in [the two-apex note](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md): its global section over S \([\mathrm{id}_S]-[\mathrm{const}_{s_0}]\) has infinitely many distinct point values, while every section of a constant discrete abelian sheaf over a compact Stone space has finite image.

Hence for **every degree m≥2**, an explicit coherent locale has an (m−1)-connected patched chain realization with **nonconstant m-th homotopy sheaf**, while both higher diagonal hull realizations are terminal. The common relative homotopy cofiber of the canonical arrows is \(\Sigma^{m+1}h(S)\), with nonconstant \((m+1)\)-th homotopy sheaf \(\mathcal K_S\). For finite |S|=k, the ordinary constant homotopy type is a wedge of k−1 copies of S^m. For infinite S, the topology of S is essential to the sheaf-valued homotopy object.

## 5. Verification, limitations, literature, and next bounded questions

**Independently checked combinatorially:** For S a finite equality-ordered set of k=1,2,3,4 points, the full two-sided order complex has mod-2 Betti numbers \(\beta_0=1,\beta_2=k-1\) and no other positive Betti numbers; both common-upper and common-lower witness complexes have trivial reduced homology. For a 2-point middle S with m=2,3,4 two-point layers, the chain nerves have \(\beta_m=1\) while both witness complexes have trivial reduced homology. These tests are sanity checks, not substitutes for the coherent-localic descent proofs.

**Limits:** No assertion of localic intrinsic shape; no unpatched witness-projection descent; the mixed grid does NOT provide a direct simultaneous hull cover; no universal size-independent equivalence of Stone sites; no literature-priority claim. The full sheaf nonconstancy and \(\pi_m\) calculations require independent audit before promotion to externally certified theorem ledger. The extra-degeneracy/localic factorization in the ordinal-sum theorem is an especially suitable check.

**Standard foundations:** Nerve of category join = simplicial join of nerves, and geometric realization takes simplicial join to join of spaces (Joyal, basic simplicial topology; see Kapulkin, *Joyal’s conjecture in homotopy type theory*, dissertation §3.3.6–3.3.8). Homology sheaf of internal suspension by Mayer–Vietoris and the sheaf-internal Hurewicz theorem are standard ∞-topos facts; we used only their concrete pointed connective cases.

**Next problems:**
1. Analyze the **two Čech suspensions' interchange**, and determine whether switching open/closed cover axes gives the expected sign on the first nonzero homotopy/homology sheaf (likely a Koszul sign, not yet checked).
2. Determine whether the sheaf \(\mathcal K_S\) or higher constructions distinguish nonhomeomorphic infinite Stone spaces with the same point cardinality, rather than merely finite versus infinite.
3. Test nonconstant sheaf information when the total comparison \(\mathbf C(X)\to\mathbf I(X),\mathbf D(X)\) **is an equivalence**, not merely when \(\mathbf I=\mathbf D=1\): our present layered examples deliberately put all the homotopy in the **obstruction**. This would be the next qualitatively different class of examples.
