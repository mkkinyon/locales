# Project A — Q rank-one: hereditary-Baire point-finite rigidity and why far orthogonality adds nothing to the Boolean pair

**12 November 2026 — NEW INTERNAL algebraic consequence, not externally audited or priority checked.** This is the bounded continuation of [marked Urysohn locality](ProjectA_Q_MARKED_URYSOHN_LOCALITY_and_GENERIC_POINT_NONHEREDITY_2026-11-12.md) requested by the user. The test was whether full joint coordinate support and marked rank-one local stabilization add a **finite-cover constraint** beyond the existing chromatic obstruction. The precise outcome is twofold:

1. **Negative algebraic result:** the far-rectangle equations \(h(a)\wedge k(b)=0\) for \(a^*\vee b^*=1\) are ALREADY consequences of **binary-cover compatibility**. They supply NO extra constraint on a normalized Boolean pair, even with full joint coordinate support.
2. **Positive categorical/topological result:** on a **hereditarily Baire spatial locale** X, every ORDINARY POINT-FINITE open cover C is already respected by every generalized pair that respects all finite covers; thus no point-finite cover can contribute a new fixed-point inequality. Consequently every **locally compact sober metacompact space** satisfies the stronger \(\mathcal D_2=\mathcal D\). This extends our locally finite-cover theorem to point-finite refinements under a Baire hypothesis. It works for uncountable point-finite covers and arbitrary localic target frames. The underlying Baire category lemma is classical (McCoy and earlier references); no originality claim for that lemma.
3. For any nonzero normalized cover-hole support K that is Baire and spatial, the set of points of K belonging to **infinitely many** members of the inherited bad cover is a **dense \(G_\delta\)** (not merely a set intersecting every nonzero open). Thus a hypothetical Q-hole in locally compact sober X has generic infinite-incidence recurrence in its support.
4. This Baire argument **cannot simply replace "point-finite" by "pointwise finitely chromatic"**: a compact metrizable graph-incidence control below has every point's induced graph independent but every nonempty open meets an infinite-chromatic subfamily.

**Q and Q′ remain OPEN.** No new counterexample locale is claimed.

## 0. Notation

For L=O(X), \(Q=L\oplus L\), \(w_C=\bigvee_{c\in C}c\boxtimes c\),
\[
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q),\qquad
z_1=d_{\mathcal U}=\bigvee_{a^*\vee b^*=1}a\boxtimes b.
\]
Generalized coordinates h,k:L→M are **finite-compatible** when
\[
\bigvee_{c\in F}h(c)\wedge k(c)=1_M
\]
for EVERY finite frame cover F. We use the independently audited one-sided compact/regular rigidity and closed-support theory only for context; the central proof here is elementary and does NOT need those results.

An ordinary topological open cover C is **point-finite** if for each ordinary point x of X the set \(\{c\in C:x\in c\}\) is finite. This is NOT the old Dowker–Strauss point-finiteness condition for point-free covers. In particular the singleton-basic Scott cover of S=P(ω)\{∅} is NOT ordinarily point-finite (the point ω lies in every member), although it satisfies the old DS frame condition; thus the earlier weak fitting control does not challenge the new theorem.

## 1. Far orthogonality is binary-cover orthogonality

**Lemma 1.1 (no additional far constraint).** If h,k:L→M are compatible with every binary cover of L, then
\[
\boxed{h(a)\wedge k(b)=0_M\quad\text{whenever }a^*\vee b^*=1_L.}
\tag{1.1}
\]
Consequently \((h,k)\) annihilates the entire Urysohn defining open \(z_1\).

*Proof.* The pair {a*,b*} is a binary cover, so
\[
1=h(a^*)\wedge k(a^*)\vee h(b^*)\wedge k(b^*).
\]
Meet both sides with h(a)∧k(b). The first term vanishes because \(h(a)\wedge h(a^*)=0\); the second vanishes because \(k(b)\wedge k(b^*)=0\). QED.

This recovers the basic universal relation \(\mathcal D_2\le\mathcal U\), but highlights the **strategy limitation**: trying to extract a new restriction on the normalized Boolean witness merely by reusing the far-rectangle presentation is logically circular. The actual extra ingredient is that the defective Boolean pair is the least dense Boolean part of a NONZERO **RELATIVELY OPEN** Urysohn hole. Full joint closed coordinate support by itself does not manufacture a new far-separation constraint.

## 2. Classical Baire lemma, with a short independent proof

**Lemma 2.1 (point-finite open family is locally finite on a dense open locus).** Let Y be ANY Baire topological space, and \(\mathcal C\) a point-finite family of open subsets (a cover is not required). Define
\[
\ell_{\mathcal C}
=\bigcup\{V\subseteq Y:V\text{ open and meets only finitely many }c\in C\}.
\]
Then \(\ell_{\mathcal C}\) is a **dense open** subset of Y.

*Proof.* For n∈N set
\[
F_n=\{x\in Y:\#\{c\in C:x\in c\}\le n\}.
\]
The complement is the union of all intersections of n+1 DISTINCT members, hence F_n is CLOSED. Point-finiteness gives \(Y=\bigcup_n F_n\).

For any nonempty open V⊆Y, the Baire property gives n and a nonempty open W⊆V∩F_n. Among all finite families \(A\subseteq C\) whose intersection meets W in a nonempty OPEN set, choose one of maximal cardinality k≤n (k=0 if every member misses W). The nonempty open set \(W' = W\cap\bigcap_{c\in A}c\) cannot meet any member outside A; otherwise k would not be maximal. Thus W' meets at most k≤n members, so W'⊆ell_C and V intersects ell_C. Since V was arbitrary, ell_C is dense. □

This is the standard classical lemma; see e.g. R. A. McCoy, *A Filter Characterization of Regular Baire Spaces* (Proc. AMS 1973), Lemma 1, and standard treatments of the Baire property. For locally compact sober spaces, the Baire theorem goes back to Isbell (also presented in Keye Martin, *Topology Proceedings* 24, 1999, Theorem 2.32 and Corollary 2.33).

### 2.2 A first-coordinate least-closed-support proof (no joint support necessary)

For a frame map h:L→M, M nonzero, let
\[
e_h=\bigvee\{a\in L:h(a)=0\},\qquad K_h=\mathfrak c_X(e_h).
\tag{2.1}
\]
Since h preserves arbitrary joins, h(e_h)=0. The induced \(h_{K_h}:O(K_h)=\uparrow e_h\to M\) **reflects zero**:
\[
h_{K_h}(v)=0\iff v=0_{K_h}.
\tag{2.2}
\]
If h is unital into a nonzero M, K_h is nonzero. This is the one-coordinate analog of the independently audited least closed joint-support normal form.

## 3. Point-finite covers cannot hide a finite-compatible defect on hereditarily Baire spaces

**Theorem 3.1 (hereditary-Baire point-finite cover rigidity; NEW INTERNAL).** Suppose X is a SPATIAL locale such that **every closed topological subspace of X is Baire**. Let C be ANY ordinarily point-finite open cover of X (possibly uncountable). Then
\[
\boxed{\mathcal D_2(X)\le\mathfrak o_{X^2}(w_C).}
\tag{3.1}
\]
Equivalently, EVERY pair of frame maps \(h,k:O(X)\to M\), with M any frame, compatible with every finite X-cover, also matches C:
\[
\boxed{\bigvee_{c\in C}h(c)\wedge k(c)=1_M.}
\tag{3.2}
\]

*Proof.* Suppose the matching value u in (3.2) is <1_M. Restrict the target to the nonzero **closed** sublocale \(\mathfrak c_M(u)\), passing from M to the frame \(\uparrow u\), where matching C becomes bottom and finite-cover compatibility persists. Rename the resulting nonzero target M and its coordinates h,k. Thus
\[
\bigvee_{c\in C}h(c)\wedge k(c)=0_M.
\tag{3.3}
\]
Let \(K=K_h\) be the least closed support of the FIRST coordinate h from §2.2. It is a nonzero closed spatial sublocale; by hypothesis the represented closed subspace K is Baire. The restricted cover \(C_K=\{c|_K:c\in C\}\) is still ordinarily point-finite. Lemma 2.1 gives a nonempty K-open \(v\) meeting only finitely many C_K members; denote the corresponding original finite family by F⊆C.

Let \(t_F=\bigvee(C\setminus F)\). Because C covers 1, the family \(F\cup\{t_F\}\) is a FINITE X-cover. Since every individual C matching term vanishes by (3.3), finite compatibility gives
\[
1_M=h(t_F)\wedge k(t_F),\quad\text{hence }h(t_F)=k(t_F)=1_M.
\tag{3.4}
\]
Choose an ambient X-open a restricting to v on K. Because v meets no c|K outside F, \(a\wedge t_F\le e_h\). Therefore
\[
h(a)=h(a)\wedge h(t_F)=h(a\wedge t_F)=0_M.
\]
But \(h_K\) reflects zero and \(v\ne0_K\), contradiction. QED.

**Proof strength:** Only ONE coordinate's closed support was needed; no assumption of spatiality of the generalized target, the localic square, or of B(E). Spatiality/Baire are required only on X and its closed subspaces. **Do not** falsely claim both h and k factor through K_h; the proof uses ambient lifts and the finite cover \(F\cup\{t_F\}\).

**Corollary 3.2 (finite-fixed full-cover domination).** Under Theorem 3.1's hypotheses, for ANY point-finite cover C and ANY finite-fixed \(d\in Q\), \(\Phi_2(d)=d\),
\[
\boxed{w_C\to d=d.}
\tag{3.5}
\]
*Proof.* Otherwise \(E=\mathfrak c(d)\wedge\mathfrak o(w_C\to d)\) is a nonzero relatively OPEN hole. Since every finite cover square is dense in \(\mathfrak c(d)\), the least dense Boolean sublocale B(E) is a nonzero finite-cover-compatible pair assigning matching value zero to C. Theorem 3.1 forbids this. Inflationarity gives the reverse inequality. □

**Corollary 3.3 (metacompact hereditary-Baire positive class).** If X is hereditarily Baire and every open cover has an ORDINARY point-finite open refinement (topologically **metacompact**), then
\[
\boxed{\mathcal D_2(X)=\mathcal D(X),\quad
\mathcal W_2(X)=\mathcal W(X),\quad
Q,Q'\text{ hold on X}.}
\tag{3.6}
\]
For any cover C choose point-finite refinement D. Theorem 3.1 gives \(D_2\le O(w_D)\le O(w_C)\); meet over C.

**Corollary 3.4 (locally compact sober metacompact spaces).** Every locally compact sober space is completely (hereditarily) Baire: closed subspaces are locally compact sober and hence Baire (Isbell's theorem). Therefore every locally compact sober metacompact space satisfies (3.6).

**Careful distinction:** (3.5)–(3.6) do NOT assert \(\Phi=\Phi_2\) pointwise after a single step for a point-finite cover. They assert equality of FIXED POINTS / fitted sublocales (and therefore of transfinite closure nuclei). The stronger pointwise one-step identity was separately proved for **locally finite** covers, not for arbitrary point-finite covers.

## 4. A dense G_delta of infinite-incidence points on a normalized Baire support

**Proposition 4.1 (generic infinite incidence).** Let Y be a Baire spatial locale and C any open cover of Y with \(\ell_C=0_Y\) (NO nonzero open patch meets only finitely many C members). Then
\[
\boxed{
I_\infty(C)=\{x\in Y:\#\{c\in C:x\in c\}=\infty\}
}
\]
is a **dense \(G_\delta\)** subset of Y.

*Proof.* Define closed F_n as in Lemma 2.1. If any F_n had nonempty interior W, choose a maximal simultaneous finite intersection of ≤n cover members meeting W, as in the proof of Lemma 2.1; this would give a nonzero open locally finite patch, contrary to \(\ell_C=0\). Thus every F_n is closed NOWHERE DENSE. Its complement is open dense. Since Y is Baire,
\[
I_\infty(C)=Y\setminus\bigcup_n F_n
=\bigcap_n(Y\setminus F_n)
\]
is dense G_delta. □

**Rank-one consequence:** On any SPATIAL BAIRE closed support K of a canonical Q or Q′ marked hole, the previously proved exact \(\ell_{C_K}=0\) implies a comeager set of *ordinary points of K*, each lying in infinitely many members of the same inherited bad cover. In particular this holds for closed K inside a locally compact sober X. It is a genuine point-level recurrence statement about K, but **NOT a contradiction**: our completed-powerset Scott weak-fitting control satisfies precisely such recurrence while Q/Q′ hold.

## 5. An adversarial countercontrol to the naive chromatic substitution

The point-finite theorem is tempting to generalize by replacing
“each point belongs to finitely many C members”
with
“for each point x, the induced graph of C-members containing x is finitely chromatic.”
That Baire-localization step is FALSE for abstract graphs, even for a locally compact zero-dimensional metric space and a cover with NO finite subcover:

Let \(Z=\prod_{n=3}^{\infty}\{1,\ldots,n\}\), a compact zero-dimensional metrizable space, and let \(p=(1,1,\ldots)\). Put \(Y=Z\setminus\{p\}\), a locally compact Hausdorff Baire space. For each n≥3 and \(j=2,\ldots,n\) define the CLOPEN set
\[
c_{n,j}=\{x\in Y:x_n=j\}.
\]
The countable family C of all \(c_{n,j}\) covers Y: every x≠p has some non-1 coordinate. It has NO finite subcover, since any finite family can be avoided by choosing a different coordinate to differ from p.

Let \(\Gamma\) be the graph on C having **all edges between distinct vertices in the SAME n-block** and NO edges across different n. Thus
\[
\Gamma=\bigsqcup_{n\ge3}K_{n-1},\qquad\chi(\Gamma)=\infty.
\tag{5.1}
\]

For every point x∈Y, the subfamily \(I_C(x)=\{c_{n,x_n}:x_n\ne1\}\) contains at most ONE vertex in each n-block. Therefore its induced graph is independent:
\[
\boxed{\chi(\Gamma[I_C(x)])=1\quad\forall x\in Y.}
\tag{5.2}
\]
But for EVERY nonzero open V⊂Y, some basic cylinder W⊆V fixes only FINITELY many n-coordinates. For all other n, W meets EVERY c_{n,j}, j≥2. Hence Γ[I_C(V)] contains \(K_{n-1}\) for arbitrarily large n, and
\[
\boxed{\chi(\Gamma[I_C(V)])=\infty\quad\forall\,V\ne0.}
\tag{5.3}
\]
Thus the chromatically locally finite locus \(\eta_{\Gamma,C}=\bigvee\{V:\chi(\Gamma[I_C(V)])<\infty\}\) is ZERO, despite each point's incidence graph being 1-colorable and Y locally compact Baire.

**Scope:** This Γ is an *abstract graph* assigned to the cover, NOT claimed to be the cross-link graph of a finite-fixed closed localic relation. The example specifically refutes the proposed GENERALIZATION of the classical Baire point-finite lemma to “pointwise finite chromatic”. Additional geometric structure of actual Urysohn cross-link graphs might still give a stronger theorem; none is asserted here. It is a falsification test, not another Q counterexample.

## 6. Interpretation and next work discipline

1. The far-square generator formula contributes no NEW constraint on individual finite-compatible Boolean pairs: its annihilation is equivalent to a binary-cover calculation. Hence pair-level far orthogonality cannot, by itself, solve Q.
2. Hereditary Baire category DOES yield a fresh positive finite/full fitting equality for metacompact locales, including locally compact sober metacompact spaces, without assuming regularity or paracompactness.
3. When a nonzero marked support K is spatial Baire, cover incidence is generically INFINITE. This is an exact new point-level manifestation of the earlier \(\ell_C=0\).
4. The naive Baire extension from pointfinite incidence to pointwise finite **chromatic** incidence is FALSE, so the remaining Urysohn-specific problem must use the fact that G is the ACTUAL cross-link graph of a nonzero OPEN hole in the rank-one finite-fixed Urysohn relation. That is the precise outstanding nonformal ingredient.

**STATUS: new internal theorem/corollaries and negative control; no external mathematical audit or literature-priority check. Universal Q/Q′ remain OPEN.**
