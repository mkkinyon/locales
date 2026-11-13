# Project A — iterated persistent kernels in the filtered two-apex programme

**13 November 2026. Internally checked working note; not externally refereed.** Continuation of the [anti-Urysohn core-reduction and first Arrieta test](ProjectA_Q_ANTIURYSOHN_TWOAPEX_PERSISTENT_CORE_ARRIETA_TEST_2026-11-13.md). Both universal Q and Q′ remain open. This note tests **noncompact, nonregular kernels with nontrivial tail adhesion through infinitely many stages** and records a conditional exhaustion theorem.

## 1. Marked holes descend through closed kernel towers

Use the same notation X(T,G) with two open T-arms and apices a,b,t, tails G_n, and W=cl D, W₂=cl D₂. The preceding core-reduction theorem says: **when T is anti-Urysohn**, every nonzero relatively open Q′ hole E in W₂(X(T,G)) is supported on the closed residual

\[
F(P)=P_+\cup P_-\cup\{a,b,t\},\qquad
P=\bigcap_n\operatorname{cl}_T G_n.
\]

Moreover, the **same marked sublocale E** persists as a nonzero relatively open Q′ hole of F(P); the proof uses the dense Booleanization of E, exact closed heredity of D₂, and relative openness, *not* an unjustified closure-through-closed-restriction assertion.

This persistence can be iterated. Define a descending chain of closed arm subspaces, for successor ordinals and limits respectively,

\[
T_0=T,\qquad
T_{\alpha+1}=\bigcap_n
 \operatorname{cl}_{T_\alpha}(G_n\cap T_\alpha),
\qquad
T_\lambda=\bigcap_{\beta<\lambda}T_\beta.
\]

Put X_\alpha=(T_\alpha)_+\cup(T_\alpha)_-\cup\{a,b,t\} with the **subspace** topology from X; the apex tail trace at stage α is G_n∩T_\alpha. We only invoke the core theorem at stages where these traces are nonempty and T_\alpha is anti-Urysohn. At a limit λ, the closed X_\lambda is the intersection of the previous closed X_\beta. The corresponding product closed sublocales also intersect correctly:

\[
X_\lambda^2=\bigwedge_{\beta<\lambda}X_\beta^2
\quad\text{inside }X^2.
\]

If the same marked E is supported on every X_\beta², it is therefore supported on X_\lambda² and persists as a marked Q′ hole by the same exact closed-heredity argument. Consequently:

**Transfinite support-exhaustion lemma.** If all nonterminal stages permit the anti-Urysohn core reduction and the descending chain reaches a Q′-positive closed X_\alpha (including a compact one), then the starting X is Q′-positive. Neither a finite bound on the chain nor compactness of each intermediate kernel is needed.

## 2. A Baire/countable-base terminal criterion

**Theorem 2.1 (conditional exhaustion of anti-Urysohn kernel towers).**
Suppose T is second-countable, T₁ and sober, its closed subspaces are Baire, and T is anti-Urysohn. Let G_n be decreasing nonempty T-opens with empty intersection. Form T_\alpha as above. Suppose **every nonempty T_\alpha is anti-Urysohn**, at successors and limits. Then

\[
\boxed{W(X(T,G))=W_2(X(T,G)).}
\]

**Proof.** Each T_\alpha is closed in T, hence Baire. If it is nonempty and all traces G_n∩T_\alpha are nonempty, they form decreasing nonempty open sets with empty intersection. The closed set

\[
\bigcap_n\operatorname{cl}_{T_\alpha}(G_n\cap T_\alpha)
\]

has **empty interior** in T_\alpha: otherwise, on a nonempty open subspace of that interior, the traces would be countably many dense open sets with empty intersection, contrary to the Baire property. Thus T_{\alpha+1} is a proper nowhere-dense closed subset of T_\alpha.

There cannot be an ω₁-long sequence with proper successor inclusions in a second-countable T. Indeed choose for each strict step a basic T-open B_\alpha meeting T_\alpha but disjoint from the closed T_{\alpha+1}; these chosen basis elements are distinct because for β>α the set T_\beta lies inside T_{\alpha+1}. Therefore at some countable stage either T_\alpha is empty or some G_n∩T_\alpha is empty.

In the first case X_\alpha is the finite three-apex subspace, so Q′-positive. In the second case the three apices are isolated in X_\alpha (tails are decreasing) and the two arms are clopen copies of the anti-Urysohn T_\alpha. Hence X_\alpha is the finite clopen coproduct of Q′-positive components; it is Q′-positive. The transfinite support-exhaustion lemma propagates this back to X. □

**Meaning of the hypothesis.** This is **not** a theorem that all filtered Arrieta-arm examples are positive. A persistent closed kernel may cease to be anti-Urysohn. Nor is it a claim that every countably based sober T is completely Baire. For an attempted negative Q′ example in this Baire/second-countable anti-Urysohn model, some surviving persistent kernel must **fail** anti-Urysohnity before an ordinary positive terminal stage can be reached.

## 3. The Arrieta space is completely Baire

In Arrieta's [Example 4.5](https://arxiv.org/pdf/2310.18522), C=2^ω, K_k is the finite set of eventually-zero binary sequences whose last 1 is at k, Y=C\setminus\bigcup_k K_k is a dense Polish Gδ, and A=Y⊔ω has the attached-point topology. A is anti-Urysohn and nonregular.

Every closed H⊆A is Baire: O=H∩Y is closed in the Polish space Y and is open in H, hence Polish; H\O is a subset of the relatively discrete added-point set ω. Any nonempty H-open disjoint from O contains an isolated point of H, so O together with the isolated points of H is a **dense open Baire** subspace of H. Thus H is Baire. This confirms that Arrieta's A has the closed-hereditary Baire input of Theorem 2.1; the nonautomatic condition is anti-Urysohnity of *each* derived kernel.

## 4. An infinite noncompact self-similar kernel tower

Partition ω into countably many **infinite** pairwise disjoint sets I₁,I₂,… whose union is ω, with each complement of a finite union still infinite. For i≥0 define compact Cantor subspaces

\[
S_i=\{x\in2^\omega:x_j=0\text{ whenever }j\in I_1\cup\cdots\cup I_i\},
\quad S_0=C.
\]

Every finite-stage S_i is Cantor, S_{i+1} is closed nowhere dense in S_i, and S_\infty=\bigcap_iS_i=\{0^\omega\}. Put J_i=ω\setminus(I_1\cup\cdots\cup I_i), a countably infinite set.

For x≠0^\omega let r(x) be the **least block number** r for which some coordinate j∈I_r has x_j=1. Let m(x) be the least such j in I_{r(x)}. For n≥0 define

\[
U_n=\{x\in C\setminus\{0^\omega\}:m(x)\ge n\},
\qquad G_n=U_n\cap Y\subseteq A.
\]

**Openness check.** If x∈U_n and m(x)=j≥n, fix its finite prefix through j. Any y sharing this prefix either has first occupied block r(x), with first 1 there at j, or has a first occupied block of *smaller* index, whose first 1 must occur beyond j. In both cases m(y)≥n. Thus U_n is Cantor-open. The G_n are nonempty decreasing A-opens with empty intersection (every nonzero x has finite m(x), and 0^\omega is omitted from all).

For each finite i,

\[
\boxed{\bigcap_n
\operatorname{cl}_{S_i}(U_n\cap Y\cap S_i)=S_{i+1}.}
\]

Indeed a point in S_{i+1} can be approximated in S_i by setting a sufficiently late free bit of I_{i+1} to 1, choosing a Y-point in the resulting open cylinder; it lies in U_n. Conversely if x∈S_i\setminus S_{i+1}, its least 1 in block I_{i+1} occurs at some coordinate j; for n>j the relative cylinder x_j=1 in S_i is disjoint from U_n, hence x is outside that closure.

Now consider the attached points. For k∈J_i the intersection K_k∩S_i is nonempty and finite, while for k∉J_i it is empty. The closed subspace

\[
P_i=(Y\cap S_i)\cup J_i\subseteq A
\]

has precisely the Arrieta topology based on Cantor S_i with finite sets K_k∩S_i (k∈J_i). This uses the simple extension of a relative S_i-open neighbourhood of K_k∩S_i by the open complement C\setminus S_i to a C-open neighbourhood of all K_k. Reindexing the free coordinates gives **P_i≅A**, so every P_i is noncompact, nonregular, anti-Urysohn and Baire.

The finite-set compactness test for attached-point closure, combined with the displayed Cantor calculation, gives

\[
\boxed{\bigcap_n\operatorname{cl}_{P_i}(G_n\cap P_i)=P_{i+1}.}
\]

Thus every stage of the two-apex kernel descent is another genuinely noncompact, nonregular Arrieta two-apex space with nonempty, decreasing tail traces. There is **no** compact or regular kernel at any finite stage. Yet

\[
P_\infty=\bigcap_iP_i=\{0^\omega\},
\qquad
X_\infty=\{a,b,t,(0^\omega)_+,(0^\omega)_-\},
\]

a finite compact subspace. The transfinite support-exhaustion lemma (or Theorem 2.1) gives

\[
\boxed{W(X(A,G))=W_2(X(A,G)).}
\]

This is an **ω-deep control**: noncompact persistent cores and adhesion at every finite level still do not create an open Q′ hole.

**Rank caution:** We have *not* proved W₂<U for this ω-tower. The earlier finite-cover witness A₀⊠B₀ from the single-missing-point test no longer works automatically: G₀ has cross-arm patches with persistent contact at the first kernel. The conclusion of this section is exactly W=W₂, not a claimed inequality with U.

## 5. Programme assessment

The filtered two-apex search has now tested: regular arms with arbitrary tails; disjoint clopen anti-U clouds; one overlapping Arrieta arm with a compact first kernel; and **infinitely iterated** noncompact, nonregular, overlapping Arrieta cores. All are Q′-positive for distinct proved reasons. The last example refutes the idea that merely prolonging the noncompact persistent-core descent is sufficient.

**A remaining two-apex candidate must change mechanism**, not just depth. In the completely Baire second-countable anti-Urysohn-arm model, it must produce a first persistent kernel that fails anti-Urysohnity, or otherwise violate an explicit hypothesis of the exhaustion theorem, and must support a **relatively open W₂-hole** rather than a nonclosed difference D₂\D. This is a meaningful stopping point for the current *self-similar Arrieta/tail* programme. It is not a no-go theorem for all possible two-apex locales (especially nonspatial, non-Baire, or cores changing their separation type).

**Provenance.** The closed-heredity, marked-hole persistence, rank-zero, compact/regular rigidity and finite-cover foundations were previously independently audited. The transfinite synthesis, Baire criterion and ω-deep Arrieta example here are new internal arguments and warrant a separate adversarial audit before being treated as certified facts.
