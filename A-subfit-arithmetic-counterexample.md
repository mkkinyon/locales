# Project A — Subfitness AND arithmeticity do not force functional collapse

**20 October 2026, new working construction; not externally refereed and no priority claim.** This is a strengthened deleted-Tychonoff-plank example. Unlike the earlier *discrete*-cloud construction (algebraic and subfit but **not** arithmetic) and *two-tag* construction (arithmetic but **not** subfit), the new frame simultaneously satisfies **subfitness and arithmeticity** and still has

\[
\boxed{\mathcal I=\mathcal U\subsetneq\mathcal F.}
\]

The natural topological presentation is a **T1, locally compact, NONSOBER** space. Its **sobrification**, representing the *same frame*, is strongly locally compact, sober and non-T1. We explicitly analyze all new sobrification points: this step is essential to verify equality of the closed **localic** relations, rather than merely equality on the original points.

## 1. Topology: two cofinite clouds

Let T be a **locally compact, Hausdorff, zero-dimensional** space with a basis of compact open subsets, and let A,B⊆T be **disjoint nonempty closed** subsets that cannot be separated by disjoint T-open neighborhoods. Our concrete choice is the *deleted Tychonoff plank*

\[
T=([0,\omega_1]\times[0,\omega])\setminus\{(\omega_1,\omega)\},
\quad
A=\{\omega_1\}\times[0,\omega),
\quad
B=[0,\omega_1)\times\{\omega\}.
\]

T is locally compact Hausdorff with a compact-open basis. A and B are disjoint closed sets, and their standard nonnormality obstruction forbids disjoint open neighborhoods.

Choose pairwise disjoint countably infinite sets S_A,S_B disjoint from T. Set

\[
Y=T\sqcup S_A\sqcup S_B.
\]

Declare O⊆Y open iff:

1. V=O∩T is open in T;
2. each cloud portion O∩S_A and O∩S_B is either **empty** or **cofinite** in its own cloud;
3. if V∩A≠∅ then O∩S_A is cofinite; if V∩B≠∅ then O∩S_B is cofinite.

These conditions define a topology. Arbitrary unions of nonempty cofinite subsets are cofinite; finite intersections of nonempty cofinite subsets are cofinite, and the cloud requirements are stable under unions and finite intersections.

The old part T is **closed** in Y (because S_A∪S_B is open), and carries its original subspace topology. Each S_A,S_B is **open** in Y, with the ordinary infinite cofinite T1 topology.

## 2. The frame is subfit and arithmetic

**Proposition 2.1.** Y is T1, its frame L=O(Y) is **subfit**, and L is **algebraic** with compact elements closed under finite meets: an **arithmetic frame**.

**Proof of T1 and subfitness.** Every original t∈T has Y-open complement Y\{t}, since T is Hausdorff and all cloud points are included. For s∈S_A (or S_B), Y\{s} is open: its cloud portion is cofinite and all old T-points are allowed. Hence Y is T1. Its open frame is subfit: if opens u⊄v choose x∈u\v and take w=Y\{x}. Then u∨w=1 but v∨w≠1.

**Characterization of compact opens.** For every open O⊆Y,

\[
\boxed{O\text{ is a compact subspace}\iff O\cap T\text{ is compact in }T.}
\]

Indeed, O∩T is relatively closed in O because T is closed in Y, so the forward implication is immediate. Conversely, O is the union of O∩T and its two cloud portions; any **nonempty cofinite cloud portion is compact in the cofinite topology**, so if O∩T is compact then O is a finite union of compact subspaces.

**Compact-open basis.** Let t∈T and O∋t be open. Choose a compact open T-neighborhood K of t with K⊆O∩T. Shrink K to avoid the closed A (respectively B) if t is not in A (respectively B). Form

\[
P=K\cup D_A\cup D_B
\]

where D_A is O∩S_A if K meets A and is empty otherwise; define D_B analogously. This P is open by construction, contained in O, and compact by the preceding criterion. For s∈S_A or S_B, the nonempty cloud portion O∩S_A (respectively O∩S_B) is itself a compact open neighborhood contained in O. Therefore the compact opens form a basis; L is algebraic.

**Finite meets of compact elements.** Let P,Q be compact open subsets of Y. Then P∩T and Q∩T are compact **open** subsets of Hausdorff T. Their intersection is compact, because compact subsets of a Hausdorff space are closed. Hence

\[
(P\cap Q)\cap T=(P\cap T)\cap(Q\cap T)
\]

is compact. By the compact-open characterization, P∩Q is compact open. This proves **arithmeticity**. The space Y is not compact because its closed subspace T is not compact; consequently L is not coherent and the coherent-frame positive theorem is not contradicted. □

## 3. Explicit sobrification: exactly two additional points

The infinite cofinite cloud S_A is an irreducible non-singleton open subspace; Y is **not sober**. Let

\[
C_A=A\cup S_A,\qquad C_B=B\cup S_B.
\]

These are closed subsets of Y (their complements are respectively (T\A)∪S_B and (T\B)∪S_A, both open under the rules), and they are irreducible: every nonempty open that meets C_A contains a nonempty cofinite subset of S_A, so any two such opens meet inside C_A. Similarly for C_B. Neither C_A nor C_B is the closure of a point, since Y is T1.

**Proposition 3.1 (classification).** The nonempty irreducible closed subsets of Y are its singleton sets and the two sets C_A,C_B.

**Proof.** Let C be irreducible closed. If C meets S_A **infinitely**, then the closed-set description forces all S_A⊆C and A⊆C: indeed the complement Y\C has a cloud portion that can be only empty or cofinite, and cannot be cofinite if C meets S_A infinitely. If C also contained a point outside C_A, then the open S_A and an open neighborhood of that point disjoint from S_A would both meet C, contradicting irreducibility. Hence C=C_A. Similarly for infinite intersection with S_B.

If C meets both clouds only **finitely**, then each cloud point s∈C can be isolated *inside C* by an open cofinite subset of its own cloud excluding the other finitely many points of C in that cloud. A closed set C containing this cloud point and another point is reducible: another point has an open neighborhood omitting s (T1), so C has disjoint nonempty relatively open subsets (choose the first cloud neighborhood to meet C only in {s}). Thus an irreducible such C contains no cloud point unless it is that singleton. If it contains no cloud point, it is an irreducible closed subset of the closed Hausdorff space T, hence a singleton. □

It follows that the sober space \(X=\operatorname{sob}(Y)\) adds **exactly two points** \(\eta_A,\eta_B\), corresponding to C_A,C_B. The canonical frame map

\[
\mathcal O(Y)\cong\mathcal O(X)=L
\]

is an isomorphism, so arithmeticity and subfitness survive unchanged. X is strongly locally compact and sober because L is a continuous (indeed algebraic) frame, or by its explicit compact-open basis.

Write \(\widehat S_A=S_A\cup\{\eta_A\}\) and \(\widehat S_B=S_B\cup\{\eta_B\}\). An X-open set corresponding to O⊆Y includes \(\eta_A\) **iff** O∩S_A is nonempty, and similarly for B. Thus \(\widehat S_A,\widehat S_B\) are open compact subsets of X; their nonempty opens include the generic point and a cofinite portion of their respective clouds.

**Important:** X is NOT T1 (the new generic points are not closed). The correct claim is **subfitness of its frame**, inherited from the original T1 topological presentation. One must not conflate T1 of Y with T1 of X.

## 4. Exact pointwise and localic relations in X

For an X-open O, let V=O∩T. Denote by D_A,D_B the cloud portions, with each either empty or nonempty cofinite. The closure is explicitly

\[
\overline O^X
=\overline V^T
 \ \cup\begin{cases}
 A\cup\widehat S_A & D_A\ne\varnothing,\\
 \varnothing &D_A=\varnothing,
 \end{cases}
 \ \cup\begin{cases}
 B\cup\widehat S_B & D_B\ne\varnothing,\\
 \varnothing &D_B=\varnothing.
 \end{cases}
\]

Indeed, a cloud (or its generic point) has only cofinite-cloud neighborhoods, hence meets every nonempty cloud-open subset. Each t∈A (resp. B) has every neighborhood meeting the corresponding cofinite cloud, while points of T outside A (resp. B) can have neighborhoods avoiding that cloud. The old-part closure contribution is exactly cl_T(V).

Set

\[
\widehat A=A\cup\widehat S_A,\qquad
\widehat B=B\cup\widehat S_B.
\]

**Proposition 4.1.** The pointwise inseparability and Urysohn relations on the **sober** space X coincide. Their only nonsingleton equivalence classes are \(\widehat A,\widehat B\); all t∈T\(A∪B) are singleton classes.

**Proof.** Every open neighborhood of a point of \(\widehat A\) meets the corresponding cofinite cloud, and any two nonempty cofinite subsets intersect. Thus points of \(\widehat A\) are pairwise inseparable, and similarly for \(\widehat B\).

For two points belonging to different proposed classes we can choose neighborhoods with **disjoint closures**. Two points in different T-classes have T-open neighborhoods V,W with disjoint T-closures, and with closures avoiding whichever of A,B the given point does not belong to (use locally compact Hausdorff regularity and the disjointness/closedness of A,B); append the required cloud portions. The closure formula makes the resulting X-closures disjoint. A cloud or generic point of \(\widehat A\) has the X-open neighborhood \(\widehat S_A\), with closure \(\widehat A\); a point outside \(\widehat A\) has an X-open neighborhood whose closure avoids \(\widehat A\), using a T-neighborhood away from A or the disjoint cloud \(\widehat S_B\). The analogous argument applies to \(\widehat B\). Hence all pairs in different proposed classes are Urysohn-separated. Since I⊆U always, I=U pointwise. □

**Proposition 4.2.** \(\mathcal I(L)=\mathcal U(L)\subsetneq\mathcal F(L)\) as **closed sublocales** of \(X\times X\).

**Proof.** If f:X→R is continuous, it is constant on each I-class, hence has constant values α on A and β on B. If α≠β, f|T would continuously separate the disjoint closed sets A and B into disjoint real-open inverse images, impossible by choice of T,A,B. Hence for any a∈A,b∈B we have a F b.

By Proposition 4.1 the chosen a,b are Urysohn-separated, so a is NOT U-related to b. Thus I=U⊊F on ordinary points of **sober** X. Since X has a continuous frame, it is strongly locally compact and sober and its finite **localic products are spatial**, agreeing with ordinary topological products. All three of our localic relations are **closed sublocales**. They are determined by their point sets in the spatial product, so the asserted equality and strict inclusion hold **localically**. □

## 5. Compact-open witnesses and failure of even one interpolant

In the deleted plank choose α∈(0,ω1) and m∈N, and put

\[
K_A=(\alpha,\omega_1]\times\{0\},\qquad
K_B=\{0\}\times(m,\omega].
\]

These are disjoint compact open **clopen** subsets of T, with K_A∩A≠∅, K_B∩B≠∅, and K_A∩B=K_B∩A=∅. Put

\[
u=K_A\cup\widehat S_A,\qquad
v=K_B\cup\widehat S_B
\]

as opens of the sober space X (equivalently the corresponding original Y-opens). They are **compact open** by §2, and their closures are

\[
\overline u=K_A\cup\widehat A,\qquad
\overline v=K_B\cup\widehat B.
\]

These are disjoint; hence in L,

\[
u\ll u,\quad v\ll v,\quad u^*\vee v^*=1.
\]

If a frame element c satisfied \(u\prec c\prec v^*\), then in the sober spatial representation:

- \(\overline u\subseteq c\) gives \(A\subseteq c\cap T\);
- \(\overline c\subseteq X\setminus\overline v\) gives \(B\cap\overline_T(c\cap T)=\varnothing\).

Thus the T-open set c∩T contains A, while the disjoint T-open set \(T\setminus\overline_T(c\cap T)\) contains B, contradicting plank nonnormality. Therefore

\[
\boxed{\text{no }c\in L\text{ satisfies }u\prec c\prec v^*.}
\]

In particular \(u\not\prec\!\prec v^*\) even though u,v are **compact open** and have disjoint closures.

## 6. Interpretation, and what remains open

This example **disproves the conjunction**:

\[
\left.
\begin{array}{c}
L\text{ algebraic, arithmetic, subfit}\\
\mathcal I=\mathcal U
\end{array}
\right\}
\not\Longrightarrow \mathcal U=\mathcal F.
\]

It subsumes both earlier **individual hypothesis** tests, but only at the **frame/subfit** level. It does **not** construct a **T1 SOBER arithmetic** space with the same failure: the T1 precursor Y is necessarily nonsober because the cofinite clouds are irreducible. Its sobrification X remains a valid **spatial locale** and its open frame remains subfit, but X is not T1.

Thus the finer question **T1 + sobriety + arithmeticity** may still be worth investigating. Be careful: "subfit" is strictly weaker than pointwise T1 of the sober spectrum (the natural spectrum here has two extra nonclosed generic points).

Also open: exact priority of this cofinite-cloud method (infinite cofinite spaces and their generic sobrifications are standard) and the more general condition under which stable local compactness plus subfitness forces functional collapse **without** assuming algebraicity. The source counterexample needs an infinite, noncompact deleted-plank T; it does not contradict the positive theorem for **compact locales** or coherent frames.

## References / provenance

- Classical deleted Tychonoff plank and its inseparable disjoint closed edges (e.g. Steen–Seebach, *Counterexamples in Topology*).
- P. J. Cameron and V. Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783 (2026).
- J. Picado and A. Pultr, *Separation in Point-Free Topology* (2021), subfitness and continuous frame representation.
- G. Bezhanishvili, J. Madden, M. A. Moshier, M. Tressl and J. Walters-Wayland, *Subfitness in distributive (semi)lattices*, *Semigroup Forum* **110** (2025), 511–524, for recent background on subfitness of distributive lattices and compact-open semilattices. https://link.springer.com/article/10.1007/s00233-025-10506-5
- Our two antecedent examples: [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md) and [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md).

**Audit status:** complete working proof assembled, but **not externally audited**; novelty unverified. In particular the irreducible-closed-set classification, product spatiality and compact-open meet-stability should receive a skeptical independent check.
