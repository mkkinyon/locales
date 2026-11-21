# Project A — graph extensions of the rectangular calculus: canonical post-referee account
## 21 November 2026 · positive chart algebra, negative graph probes, finite exceptions

**Independent audit and provenance.** [Independent blind referee report](project-a/audits/2026-11-21/GRAPH_CHART_RANK/INDEPENDENT_REFEREE_REPORT.md): **CORRECT WITH MINOR REPAIRS, CONDITIONAL ON (RC)**. The [separate referee addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md) provides the safe infinite-chart-rank example and finite-exception characterization. The input **(RC)** was independently reviewed in the *previous* [compact-Hausdorff rectangular-composition audit](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md), and was intentionally **not re-refereed** in the current audit. This note consolidates the results without treating the independent referee's addendum as part of the original submission. A separate [claim-by-claim reconciliation](ProjectA_GRAPH_EXTENSIONS_REFEREE_RECONCILIATION_2026-11-21.md) records the detailed audit status. No novelty/literature-priority claim.

**General hypotheses:** Classical locale theory, a compact Hausdorff spatial ambient G for the algebra, and ordinary subspaces generating sublocales. Localic relational composition means **actual pullback followed by image**, with diagrammatic ordering (first R then S). Finite joins only; no general infinitary distributivity is asserted.

### 1. Rectangular baseline and graph generators

For ordinary A,B⊆G, define
\[
p(A,B)=[A\times B]_{G^2},\qquad
q(A,B)=[A]_G\times_{\mathrm{Loc}}[B]_G.
\]
The first is the point-generated bipartite relation; the second is the full localic endpoint product. They may differ. The prior, separately reviewed **(RC)** states that for independent choices \(r=p(A,B)\) or \(q(A,B)\), \(s=p(C,D)\) or \(q(C,D)\),
\[
\boxed{r\circ s=
\begin{cases}
q(A,D),&[B]\wedge[C]\neq0,\\
0,&[B]\wedge[C]=0.
\end{cases}}
\tag{RC}
\]
If the middle overlap is nonzero but A or D is empty, the prescribed **outer** \(q(A,D)\) is itself zero. No "result is zero iff a middle overlap is zero" assertion is valid without nonempty outer endpoints.

Write \(\mathcal R_\vee(G)\) for finite joins of such rectangles, including 0. It is associative and closed under converse by (RC). Let \(\mathcal P_{\rm lc}(G)\) consist of finite joins of graphs of homeomorphisms between **locally closed** subspaces of G, allowing the empty partial map. Define
\[
\mathcal A_{\rm lc}(G)=
\{\text{finite joins of members of }\mathcal R_\vee(G)
\text{ and }\mathcal P_{\rm lc}(G)\}.
\]

### 2. The positive graph algebra: locally closed chart theorem

**Theorem 2.1 (independently checked, conditional on RC).** The class \(\mathcal A_{\rm lc}(G)\) is closed under localic relational composition, converse and finite joins, and is **associative and unital**; the unit is the full localic diagonal.

The two input identities, verified by the referee, are:

**Locally closed restriction:** If U⊆G is locally closed, for every ordinary B⊆G,
\[
\boxed{[B]\wedge U=[B\cap U].}\tag{LC}
\]
For q-rectangles the analogous product restriction is computed in Loc and does **not** assume the localic product is spatial.

**Partial homeomorphism action:** If \(h:U_h\xrightarrow{\sim}V_h\) is a homeomorphism between locally closed subspaces and \(t\in\{p,q\}\),
\[
\boxed{
t(A,B)\circ\Gamma_h=t(A,h(B\cap U_h)),\qquad
\Gamma_h\circ t(A,B)=t(h^{-1}(A\cap V_h),B).
}\tag{PH}
\]

Composition and inversion of locally closed partial homeomorphisms stay in that class: their overlap domain is locally closed in the original domain, and a locally closed subspace of a locally closed subspace is locally closed. Thus all binary generator products stay among p/q rectangles and partial graph generators.

**Proof of associativity, repaired zero case.** Check all eight types of triple letters R/H. RRR follows from (RC), yielding q of the two outer supports if **both** middle overlaps are nonzero and 0 otherwise, *allowing q to vanish if its outer support is empty*. The mixed cases RRH, HRR, RHH, HHR, HRH reduce by (PH) to the same partial coordinate restriction whichever side is multiplied first. HHH is ordinary composition of partial maps. The decisive case RHR reduces to the equivalence
\[
[h(B\cap U_h)]\wedge[C]\ne0
\Longleftrightarrow
[B]\wedge[h^{-1}(C\cap V_h)]\ne0
\]
by (LC) and transport across \(h:U_h\cong V_h\). Both bracketings then yield the same outer q-rectangle or 0. Finite-join distributivity of localic composition follows from finite-join preservation by sublocale pullback and by image as its adjoint; expand any triple of finite joins into generator triples. No infinite join interchange is used.

**Corollary 2.2 (local homeomorphisms).** For any local homeomorphism f:X→Y between compact Hausdorff spaces, finite open charts cover compact X, so Γ_f is a finite join of allowed partial-homeomorphism graphs in G=X⊔Y. Thus Γ_f and its converse belong to \(\mathcal A_{\rm lc}(G)\).

**Corollary 2.3 (rectangular ideal and word normal forms).** The subalgebra \(\mathcal R_\vee(G)\) is a converse-closed **two-sided ideal** of \(\mathcal A_{\rm lc}(G)\). A finite word in individual generators evaluates as follows: with no rectangular letters, it is a single partial-homeomorphism graph; with precisely one rectangle, it is a p/q rectangle of the same type (or 0); with at least two, it is a full q-rectangle (or 0). The statement is **about indexed words**, not a claim that any finite *join* simplifies to a single generator.

### 3. Graph-probe failure and two negative geometries

Let f:S→Y be a locale map with image J≤Y, B≤Y a sublocale, and singleton markers u,v. Put
\[
R=\{u\}\times B,\quad F=\Gamma_f^\smile,\quad T=S\times\{v\}.
\]
Then the genuine pullback/image calculation gives
\[
(R\circ F)\circ T\ne0\iff B\times_Y S\ne0,
\qquad
R\circ(F\circ T)\ne0\iff B\wedge J\ne0.
\tag{GP}
\]
Thus a graph-probe associator detects an **image-intersection without a corresponding nonzero pullback**. For a continuous compact-Hausdorff f:X→Y, selecting an ordinary subset E⊆X and B=[I], the necessary condition for safe adjunction becomes
\[
[E]\wedge f^{-1}([I])\ne0
\ \Longleftrightarrow\
[f(E)]\wedge[I]\ne0,
\tag{NR}
\]
for all selected E,I; the forward implication is automatic. This is **necessary, not sufficient**, for safe graph adjunction.

**Example 3.1 (globally open and proper projection).** With Y=Cantor and K infinite compact metric, take f:Y×K→Y the projection. It is globally open, proper and surjective. Choose a discrete ordinary selector \(E=\{(q_n,z_n)\}\) with distinct \(z_n\) forming a discrete subspace of K and \(q_n\) enumerating a countable dense Q⊂Y with dense complement I. The induced locale [E] is discrete; hence pulling [I] back to it is zero, although [f(E)]=[Q] meets [I] nontrivially (both are dense sublocales). The resulting point-generated triple
\[
R=\{u\}\times[I],\quad F=\Gamma_f^\smile,\quad T=[E]\times\{v\}
\]
satisfies
\[
\boxed{(R\circ F)\circ T=0\ne R\circ(F\circ T)=\{(u,v)\}.}
\tag{OP}
\]
Thus **global openness/properness is insufficient**; restricting to the selected induced spatial support loses the pullback-stability needed.

For this product projection with nonempty compact metrizable K, the algebra generated by \(\mathcal R_\vee(G)\) and Γ_f/its converse is associative **iff K is finite**: finite K gives a finite clopen-sheet decomposition; infinite K yields the above associator. The positive direction is conditional on (RC)/(ALG).

**Example 3.2 (Cantor-to-Cantor at most two-to-one).** Let Y=Cantor, choose pairwise disjoint compact nowhere-dense Cantor sets K_n with selected q_n∈K_n forming a dense Q⊂Y, and let
\[
X=(Y\times\{0\})\ \cup\ \bigcup_{n\ge1}(K_n\times\{1/n\}).
\]
Then X is itself Cantor space, and f=pr_Y|_X is a continuous proper surjection with fibers of size one or two, **not open**. The set E={(q_n,1/n)} is discrete in X but maps bijectively onto dense Q⊂Y, yielding the same graph-probe associator. Hence \(\rho_{\rm lc}(f)=\infty\): a finite family of partial-homeomorphic charts would map the discrete selector E into a finite union of discrete subsets of perfect Y, all nowhere dense, contradicting density of Q. The referee verified that this proof does **not** need Baire-category assumptions.

**Symmetric point-generated ghost edge.** Place the four blocks u,Y,X,v at successive clopen levels and symmetrize R,F,T together with the diagonal. The resulting single **reflexive symmetric point-generated** localic relation H has
\[
((H\circ H)\circ H)\wedge(\{u\}\times\{v\})=0,\qquad
(H\circ(H\circ H))\wedge(\{u\}\times\{v\})=\{(u,v)\},
\]
although its underlying ordinary graph has **no u–v path at any finite length**. The referee checked the clopen-level argument and the ordinary connectedness claim. This is an **imposed** graph on compact Hausdorff spaces, not an intrinsic Cameron–Kumar separation graph.

### 4. Selection-theorem positive boundary

**Theorem 4.1 (independently checked, graph consequence conditional on ALG).** Suppose f:X→Y is a continuous **open surjection**, X compact metrizable, Y compact metrizable and **zero-dimensional**, and
\[
N=\max_y|f^{-1}(y)|<\infty.
\]
Then f admits exactly N **locally closed homeomorphic graph charts** (rank is minimal):
\[
\boxed{\rho_{\rm lc}(f)=N.}\tag{SEL}
\]
**Proof.** Regard fibers as a lower-semicontinuous closed-valued multifunction on Y; openness is exactly the lower semicontinuity of the inverse-fiber multifunction. **Michael's zero-dimensional continuous-selection theorem** produces a continuous right inverse. Its image is closed in the source (an equalizer). Remove it: the residual source is open and **completely metrizable** (not necessarily complete in the inherited metric), the residual target is an open zero-dimensional metrizable, hence paracompact, space, and the restricted map stays open. Repeat: each step removes one point from each remaining fiber. The bound N terminates the process, and a fiber of size N forces at least N charts. Graphs of the charts compose safely by Theorem 2.1.

The referee points out that the **topological selection/section-removal theorem** holds more broadly with X completely metrizable, Y zero-dimensional metrizable, f open surjective, and a uniform finite fiber bound. However its **algebraic application** here is still within the compact-Hausdorff ambient hypothesis for (RC).

### 5. New addendum: safe graph of infinite chart rank

The referee's addendum shows that finite chart rank is **not necessary** for membership in the known associative algebra.

Let C=Cantor space and \(X=(C\times\{0\})\sqcup(C\times\{1\})\), Y=C, with
\[
f(y,0)=y,\qquad f(y,1)=c
\]
for one fixed c∈C. This is a continuous proper surjection of Cantor spaces, but f^-1(c) contains an entire Cantor sheet, so \(\rho_{\rm lc}(f)=\infty\). Nevertheless, writing h:C×{0}→Y for the identity sheet,
\[
\boxed{\Gamma_f=\Gamma_h\vee q(C\times\{1\},\{c\}).}\tag{A1}
\]
The second summand is **both** a point-generated and full localic rectangle because its target is a singleton. Thus Γ_f and its converse already lie in \(\mathcal A_{\rm lc}(G)\), so safe adjunction follows from ALG/RC.

Even any continuous **finite-image** map satisfies
\[
\Gamma_f=\bigvee_{y\in f(X)}q(f^{-1}(y),\{y\})\in\mathcal R_\vee(G).
\tag{A2}
\]
Hence infinite fibers alone have **no necessary relationship** with failure.

### 6. Finite-exception membership characterization (referee addendum)

**Theorem 6.1 (NEW ADDENDUM RESULT, independent of RC as a membership criterion).** For a continuous f:X→Y between compact Hausdorff spaces, G=X⊔Y, the following are equivalent:

1. \(\Gamma_f\in\mathcal A_{\rm lc}(G)\).
2. X can be covered by **finitely many** locally closed domains on which f is a homeomorphism onto a locally closed range, together with **finitely many ordinary subsets** on which f is constant.
3. There is a **finite set of exceptional target values** \(F\subseteq Y\) such that
\[
f|_{X\setminus f^{-1}(F)}:X\setminus f^{-1}(F)\longrightarrow Y\setminus F
\]
has finite locally closed partial-homeomorphism chart rank.

**Proof.** If the graph is a finite join of allowed p/q rectangular and partial-map graph generators, every summand is below \(\Gamma_f\). A nonzero rectangle A×B contained in the ordinary graph of a **single-valued** map must have B a singleton {y}; the rectangle is therefore q(A,{y})=p(A,{y}), a constant piece. Every partial-map graph summand is a restriction of f. All the resulting relations are point-generated; their finite join is the induced spatial sublocale of the union of their pairs, which must cover the ordinary graph. This gives (2). Collect the finitely many constant target values in F; restrict all other partial-map charts to the complements of their preimages, preserving locally closedness. This gives (3).

Conversely, cover the graph outside the finite exceptional set with finitely many partial-map graph charts and each exceptional fiber with the rectangle \(q(f^{-1}(y),\{y\})\). This gives (1). Every step concerns graph membership, so **(RC) is not used**. Its *associativity* consequence still depends on Theorem 2.1/RC.

**Finite-to-one corollary:** If all fibers of f are finite (not necessarily uniformly bounded), then every exceptional fiber is a finite union of singleton (closed) charts. Hence
\[
\boxed{
\Gamma_f\in\mathcal A_{\rm lc}(G)\quad\Longleftrightarrow\quad
\rho_{\rm lc}(f)<\infty.
}\tag{A3}
\]
For general f, finite chart rank can be infinite even when membership and associative adjunction hold: constant pieces account for the difference.

### 7. A quantitative reformulation (POST-ADDENDUM INTERNAL COROLLARY)

This **new inference was not submitted to or stated by the referee**. Define the **rectangular–chart generator number** \(\lambda(f)\) as the least number of individual permitted generators (each p/q rectangle or locally closed partial-homeomorphism graph) whose localic join is \(\Gamma_f\), with \(\lambda(f)=\infty\) if no finite representation exists. Put \(\rho_{\rm lc}(\varnothing)=0\), and let \(\rho_{\rm lc}\) for a map on a residual source mean the minimum number of locally closed homeomorphic charts covering that source, interpreted within the residual open source/target.

Then the addendum's argument yields the exact formula
\[
\boxed{
\lambda(f)=
\inf_{\substack{F\subseteq Y\\F\ \rm finite}}
\Bigl(
|F|+\rho_{\rm lc}\bigl(f|_{X\setminus f^{-1}(F)}\bigr)
\Bigr).
}\tag{MIX}
\]
**Proof.** For each finite F, cover the residual restriction by n charts and each exceptional fiber by one q-rectangle; this gives λ(f)≤|F|+n. Conversely, given a representation with m allowed generators, let F consist of the distinct target values of its nonzero rectangular summands. These are necessarily constant pieces. Replace each set of rectangles over one target value with **one full exceptional-fiber rectangle**, without leaving the graph, and restrict each graph chart off f^-1(F). The resulting residual map has chart rank at most m−r where r is the original number of nonzero rectangular summands; since |F|≤r, \(|F|+\rho_{\rm lc}(\text{residual})\le m\). Take minima. The infimum is over nonnegative integers, so when finite it is attained.

The formula records the exact price of two distinct **witness types**: partial injective charts and constant rectangular fibers. It may be a useful complexity invariant for graph presentations; it is **new provisional notation**, not a literature-established invariant, and still needs independent audit if promoted.

### 8. Remaining sharp research problem

The addendum emphatically **does not** claim that *every* graph which can be adjoined associatively must **belong to** the finite-join algebra \(\mathcal A_{\rm lc}(G)\). The surviving questions are:

1. **Finite-to-one necessity:** If f:X→Y is continuous finite-to-one between compact metrizable spaces and Γ_f,Γ_f^smile can be adjoined **associatively to the full rectangular algebra**, must \(\rho_{\rm lc}(f)<\infty\)? Equivalently by (A3), must Γ_f lie in \(\mathcal A_{\rm lc}(G)\)?
2. **Beyond known generators:** Can a functional graph of a compact Hausdorff map be safely adjoined without belonging to \(\mathcal A_{\rm lc}(G)\)? The graph-probe condition (NR) is necessary but has not been proved sufficient.
3. **Intrinsic Cameron–Kumar bridge:** Identify meaningful stable graph-presentation or witness invariants for actual specialization/inseparability/closure-meeting sublocales, rather than automatically transferring imposed Stone-graph phenomena to intrinsic separation graphs.

A next independent audit should focus on the optional quantitative corollary (MIX) only if it is to become a stated theorem. Otherwise the graph-extension phase may now be regarded as independently reviewed **conditional on the separately established (RC)**, with only the minor wording/categorical bookkeeping repairs described above.
