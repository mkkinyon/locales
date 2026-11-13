# Project A — anti-Urysohn two-apex core reduction and Arrieta single-point test

**13 November 2026. New internally reconstructed working theorem; not yet independently refereed.** This continues the [regular-arm and clopen-gluing no-go work](ProjectA_Q_FILTERED_APEX_REGULAR_ARMS_AND_CLOPEN_GLUE_NO_GO_2026-11-13.md). It tests the first non-clopen, genuinely nonregular two-apex construction using Arrieta's [Construction 4.2 / Example 4.5](https://arxiv.org/pdf/2310.18522). The test again gives W=W₂<U, but through a **different, compact-persistent-contact** obstruction. Neither universal Q nor Q′ is settled.

## 1. Filtered two-arm model and persistent kernel

Let T be a sober spatial T₁ **anti-Urysohn** space (nonzero opens have intersecting closures). Choose nonempty decreasing T-open sets G₀⊇G₁⊇⋯ with ∩G_n=∅. Let X=X(T,G) consist of two disjoint open arms T_+,T_- and points a,b,t with basic neighbourhoods A_n={a}∪(G_n)_+, B_n={b}∪(G_n)_-, T_n={t}∪(G_n)_+∪(G_n)_-. As before X is sober T₁.

Define the closed **persistent-tail kernel**

\[
P=\bigcap_{n\in\omega}\overline{G_n}^{\,T}\subseteq T
\]

and let J_+=cl_X(T_+)=T_+∪{a,t}, J_-=cl_X(T_-)=T_-∪{b,t}. Define the closed residual subspace

\[
F=X\setminus\bigl((T_+\setminus P_+)\cup(T_-\setminus P_-)\bigr)
=P_+\cup P_-\cup\{a,b,t\}.
\]

Do **not** presume the localic square X² is spatial; the proof below uses actual open/closed sublocales and far rectangles.

## 2. Core-reduction theorem for all anti-Urysohn arms

**Theorem 2.1.** If F satisfies Q′, then X satisfies Q′:

\[
\boxed{W(F)=W_2(F)\quad\Longrightarrow\quad W(X)=W_2(X).}
\]

**In particular**, if P is compact, then F is compact (finite union of two compact P-copies and three singleton subspaces), so X satisfies Q′. The statement is also useful when P is noncompact but F is positive by a different theorem.

**Proof.**

**Step A: the full fitting closure already fills each same-arm sector.** As T is anti-Urysohn, z_T=0, hence W(T)=W₂(T)=U(T)=T² by the rank-zero identity. For an X-cover C, its restriction C|T_+ covers T_+. Therefore every generalized pair factoring through D(T_+) matches C, giving D(T_+)≤D(X)∧O(T_+²). Since D(T_+) is dense in T_+², the closed W(X) contains cl_{X²}(T_+²)=J_+². Likewise J_-²≤W(X).

**Step B: away from P the Urysohn relation has no cross-arm links.** Put R_+=T_+\setminus P_+, an open subset of X, and H_+=X\setminus J_+=T_-\cup\{b\}, also open. For any ordinary x∈R_+, some n has x∉cl_T G_n. Choose a T_+-open neighbourhood V_x of x with V_x∩G_n=∅. The closure of V_x in X lies entirely within T_+: the basic apex neighbourhoods A_n,T_n miss it, the other apex b and every negative-arm point have neighbourhoods disjoint from T_+. Meanwhile the closure of H_+ lies in J_- and so misses T_+. Therefore the rectangles V_x⊠H_+ are **far**, and since they cover R_+×H_+,

\[
R_+\boxtimes H_+\le z_X.
\]

Consequently U(X)=C(z_X), on the first-coordinate R_+ strip, has second coordinate in J_+; equivalently

\[
U(X)\wedge O(R_+\boxtimes1)\le J_+^2.
\]

The same statement holds with + and − interchanged. Both arguments are rectangle/open-sublocale arguments, not pointset calculations on X².

**Step C: an open Q′ hole is forced into the closed remainder F².** Suppose Q′ fails, and choose its nonzero symmetric relatively open hole E=W₂(X)∧O(w_C→d), with d the finite pre-nucleus fixed point. Because E∧W(X)=0, Step A gives E∧J_+²=E∧J_-²=0. Since E≤W₂(X)≤U(X), Step B gives E∧O(R_+⊠1)=E∧O(R_-⊠1)=0, and by coordinate symmetry the same on the second-coordinate strips. Thus E lies in the closed complement of those strips on both coordinates:

\[
\boxed{E\le F^2.}
\]

**Step D: the same marked open hole persists in F.** The Booleanization B(E) is dense in E, lies in D₂(X), and has both coordinate maps factoring through F because E≤F². Exact closed heredity gives B(E)≤D₂(F). Hence E≤W₂(F). Since W₂(F)≤W₂(X)∧F², the same E is relatively open in W₂(F); and because E is disjoint from D(X), it is disjoint from D(F), hence from W(F). This contradicts Q′-positivity of F. □

**Caution:** This does **not** say that every anti-Urysohn-arm filtered space is Q′-positive; if the closed F itself could fail Q′, the theorem would only transfer the defect to a smaller support. It is a **reduction theorem**, not a universal conclusion.

## 3. Arrieta's precise topology and a non-clopen rank test

Arrieta's Example 4.5 begins with the Cantor cube C=2^ω and pairwise disjoint finite closed sets

\[
K_n=\{x\in2^\omega:x_n=1,\ x_j=0\text{ for }j>n\}.
\]

Let Y=C\setminus\bigcup_n K_n, a dense Polish subspace of C. The resulting A=Y⊔ω has Y open and has basic neighbourhoods (U∩Y)∪{n} around n whenever U⊆C is open and K_n⊆U. Arrieta proves A Hausdorff, strongly Hausdorff and anti-Urysohn (Cor. 4.3, Prop. 4.4, Example 4.5); the project's rank-zero identity gives W(A)=W₂(A)=U(A)=A².

Fix one x_*∈K_m. Choose decreasing clopen Cantor cylinder neighbourhoods V_N of x_* with V₀=C and ∩_N V_N={x_*}. Define T=A and

\[
G_N=V_N\cap Y\quad\text{(as an A-open)},\qquad N\ge0.
\]

These are nonempty decreasing A-opens, G₀=Y and ∩G_N=∅, yielding a well-defined T₁ sober two-apex space X=X(A,G). Unlike the preceding clopen-cloud construction, the entire anti-Urysohn arm A is **not** cut into clopen component charts.

**Noncompactness.** The copy ω_+ of the added points inside A_+ is a closed infinite discrete subspace of X: it is disjoint from the open Y_+ and from all the new apex neighbourhoods (whose arm traces lie in Y), and the n-points form a discrete subspace in A. Hence X is noncompact.

**Finite-rank calculation.** Let F₀={T_+,T_-,A₀,B₀,T₀} and r=A₀⊠B₀. The only nonzero square contribution to r∧w_{F₀} is G₀^+⊠G₀^-=Y_+⊠Y_-.

For each y∈Y choose N with y∉V_N and a Y-open neighbourhood W_y contained in C\V_N. Its closure in X cannot meet a or t (on the positive arm) or b/t (on the negative), because the relevant apex neighbourhood with index N misses W_y; its closure remains in the corresponding arm. Thus every cross rectangle W_y^+⊠W_{y'}^- is far, and by join-generation

\[
Y_+\boxtimes Y_-\le z_X.
\]

On the other hand, every neighbourhood of a and b has t in its closure, so the point-pair (a,b) lies in r but not in z_X. Therefore

\[
\boxed{
r\le w_{F_0}\to z_X\le\Phi_{2,X}(z_X),\qquad
r\nleq z_X,
}
\]

and thus **Φ₂(z_X)>z_X and W₂(X)<U(X)**.

**Persistent kernel calculation.** For a Y-point y, y∈cl_A G_N iff y∈V_N. Hence no Y-point is in ∩_N cl_A G_N. For an attached point n∈ω,

\[
n\in\operatorname{cl}_A(G_N)
\iff K_n\cap V_N\ne\varnothing.
\]

Indeed an n-neighbourhood comes from a Cantor-open containing the entire compact K_n; it meets G_N exactly when every such Cantor neighbourhood does, equivalent to K_n meeting cl_C G_N=V_N. By nested compactness,

\[
n\in\bigcap_N\operatorname{cl}_A G_N
\iff K_n\cap\bigcap_N V_N\ne\varnothing
\iff x_*\in K_n
\iff n=m.
\]

Thus the persistent kernel is the **single point P={m}**. The closed remainder F in Theorem 2.1 is the five-point set {a,b,t,m_+,m_-}; its subspace topology is discrete because every new apex neighbourhood has arm trace in Y, disjoint from {m}, and {m} is isolated in the finite subspace of the n-points. In particular F is compact. Theorem 2.1 yields

\[
\boxed{W(X)=W_2(X)<U(X).}
\]

This is a noncompact, countably based, sober T₁ **nonregular-arm** control with nontrivial finite rank. It escapes the **regular-arm** and **clopen-cloud** no-go theorems, but not the new compact persistent-core reduction.

## 4. What would still be necessary for an actual two-apex test?

For anti-Urysohn arms, Theorem 2.1 shows a genuine Q′ counterexample would require that its **persistent-tail remainder F itself fail Q′**. Merely making P noncompact is not enough: it may be scattered or regular, or otherwise Q′-positive. For Arrieta's base construction, shrinking cylinders to a compact missing-point set tends to yield a finite/discrete positive remainder. Shrinking to a proper nowhere-dense Cantor subspace can yield a **noncompact self-similar Arrieta-type persistent core**, but if the tails avoid that core entirely, the apices become isolated there and F is a coproduct of already Q′-positive pieces.

Thus the missing genuinely new mechanism is a **noncompact, nonregular persistent kernel with nontrivial tail adhesion inside the kernel**, such that the induced closed remainder is not already known Q′-positive. The reduction explains exactly why apparent new rank-one geometry at the external apices alone cannot produce an open Q′ hole when the core is positive.

This is a productive **stop rule for the naive Arrieta attachment**, not an assertion that all possible higher-rank or nonspatial two-apex constructions are impossible. The original motivating Q and Q′ remain open; further attempts should not recycle single replaced-point or clopen-annulus tails without first defeating the persistent-core reduction.

**Provenance:** Arrieta's source is published; the new anti-Urysohn core-transfer proof and Arrieta-tail calculation are internally reconstructed here, with independently audited Q′ hole-persistence and cover calculus as named inputs. They have not themselves been externally audited.
