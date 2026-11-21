> **21 NOV 2026 — POSITIVE COMPLEMENT RESOLVED:** The [Michael-selection open finite-to-one theorem](ProjectA_OPEN_FINITE_TO_ONE_STONE_MAPS_SELECTION_THEOREM_2026-11-21.md) proves that every continuous open surjection from compact metrizable X onto compact metrizable **zero-dimensional** Y with fibers bounded by N has **exactly N locally closed homeomorphic sheet charts**, hence its graph lies in the internally derived associative algebra. The present two-to-one Cantor counterexample is **not open** and has infinite chart rank. Also, the finite-discrete-selector obstruction below requires only that Y be perfect Hausdorff, not Baire. Both assertions remain internal pending audit.

# Project A — finite fibers do not control localic graph associativity
## 21 November 2026 · Internally derived finite-chart-rank boundary

**Status:** New research segment; **not externally audited**. Builds on the [post-referee compact-Hausdorff rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and the [internally derived locally closed graph-algebra theorem and projection counterexample](ProjectA_GRAPH_LOCAL_HOMEOMORPHISM_POSITIVE_OPEN_PROPER_NEGATIVE_2026-11-20.md). The present note strengthens the previous infinite-fiber projection obstruction to a continuous surjection between **two Cantor spaces with fibers of size at most 2**, and isolates a purely topological "finite graph-chart rank" invariant. It does **not** settle the case of maps simultaneously *open* and *finite-to-one*.

### 1. Positive baseline: finite locally closed homeomorphic graph charts

For ordinary A,B in a compact Hausdorff ambient G set p(A,B)=[A×B], q(A,B)=[A]×_Loc[B]. The independently reviewed calculus states
\[
r(A,B)\circ s(C,D)=
\begin{cases}q(A,D),&[B]\wedge[C]\ne0,\\0,&[B]\wedge[C]=0,\end{cases}
\]
for r,s chosen independently from p,q. The subsequent **internal** graph extension argues that adjoining graphs of *locally closed partial homeomorphisms* retains finite-join associativity. In particular, if f:X→Y has a **finite locally closed graph-chart cover**
\[
X=U_1\cup\dots\cup U_m,\quad
f|_{U_i}:U_i\overset\cong\longrightarrow V_i,
\]
where each U_i⊂X and V_i⊂Y is locally closed, then
\[
\Gamma_f=\bigvee_{i=1}^m\Gamma_{f|U_i}
\]
and Γ_f,Γ_f^smile can be adjoined to the rectangular algebra without losing associativity. All inclusions are point-generated sublocales in the compact Hausdorff disjoint union G=X⊔Y.

A particularly transparent sufficient condition is a finite **closed injective** cover of X: if X=F_1∪...∪F_m with each F_i closed and f|F_i injective, then compact-to-Hausdorff implies each restriction is a homeomorphism onto its closed image, hence a permitted chart. This accommodates branching; one does **not** need f globally or locally to be a local homeomorphism.

Example: f:[−1,1]→[0,1], f(t)=t², is an **open proper surjection** with a branch at 0, but both restrictions to [−1,0] and [0,1] are homeomorphisms onto [0,1]. Thus its graph belongs to the positive finite-join algebra (after disjoint-union embedding), despite not being a local homeomorphism at 0.

Define the **locally closed chart rank**
\[
\rho_{\rm lc}(f)=\min\{m:\ f\text{ admits an }m\text{-piece locally closed partial-homeomorphism cover}\}
\]
and ∞ if no such finite m exists. This is **new provisional notation**, not literature nomenclature. Always
\[
\sup_{y\in Y}|f^{-1}(y)|\ \le\ \rho_{\rm lc}(f),
\]
since any chart covers at most one source point in each fiber. The comparison can be extremely strict.

### 2. A dense discrete selector gives a negative graph probe

**Lemma 2.1 (dense discrete selector obstruction; internal).** Suppose f:X→Y is continuous between compact Hausdorff spaces and Y has an ordinary dense set Q whose complement I=Y\Q is also dense. If there is an **ordinary discrete subspace** E⊂X such that f|E:E→Q is bijective, then the converse graph Γ_f^smile cannot be adjoined associatively to the entire compact-Hausdorff rectangular algebra.

**Proof.** The induced spatial sublocale [E] is discrete (homeomorphic to E). The localic image of f|[E] is the induced point-generated spatial sublocale [Q]. Its pullback along [I] is zero: every singleton component of [E] maps to some q∈Q not belonging to I; since the domain [E] is discrete, the entire pullback is zero. Yet [Q]∧[I]≠0, because both are dense sublocales of compact Hausdorff Y and contain its nonzero Booleanization.

Take clopen marker points u,v and typed endorelations on G={u}⊔Y⊔X⊔{v}:
\[
R=\{u\}\times[I],\quad F=\Gamma_f^\smile,\quad T=[E]\times\{v\}.
\]
Then
\[
(R\circ F)\circ T=0,\qquad R\circ(F\circ T)=\{(u,v)\}\ne0.
\]
This is the earlier exact graph-probe obstruction, now formulated as a general topological sufficient criterion. □

**Point-set subtlety:** E need not be closed in X, and its limit points can occur in X\ E. Only discreteness of E *in its subspace topology* is needed to ensure that [E] is discrete. Conversely f(E)=Q can be dense-in-itself and have dense complement.

### 3. A two-to-one Cantor-to-Cantor proper surjection with infinite chart rank

**Theorem 3.1 (INTERNAL).** There is a continuous, proper, surjective f:X→Y between spaces X,Y both homeomorphic to 2^ℕ such that:

1. Every fiber has size **one or two**.
2. There is a discrete E⊂X mapped bijectively onto an ordinary dense countable Q⊂Y whose complement I is dense.
3. The graph Γ_f, with the rectangular relations R,T in Lemma 2.1, gives a nonassociative triple of **point-generated** relations.
4. \(\rho_{\rm lc}(f)=\infty\).

**Construction and proof.** Let Y=2^ℕ and enumerate a countable clopen base by W_1,W_2,... with each W_n nonempty. Inductively choose nonempty compact closed nowhere-dense Cantor subsets K_n⊂Y such that K_n are pairwise disjoint and K_n∩W_n≠∅. At step n the finite union of earlier K_i is closed nowhere dense, so W_n minus that union contains a nonempty clopen cylinder; inside it choose an embedded nowhere-dense Cantor set K_n. Choose q_n∈K_n∩W_n. By disjointness, q_n are distinct; by the base enumeration, Q={q_n} is dense. Since Q is countable and Y has no isolated points, I=Y\Q is also dense.

Let
\[
S=\{0\}\cup\{1/n:n\ge1\}\subset[0,1],\qquad
X=(Y\times\{0\})\ \cup\ \bigcup_{n\ge1}(K_n\times\{1/n\})
\subseteq Y\times S.
\tag{X}
\]
X is **closed** in Y×S: any convergent sequence with heights eventually at a fixed positive level has its limit in that closed K_n-level; any sequence whose heights tend to zero has its limit in the full base Y×{0}. Thus X is compact metrizable and zero-dimensional. Every point of the base lies in a perfect Cantor copy, and every upper-level point lies in its own perfect Cantor K_n. Therefore X has **no isolated points**, hence X≅2^ℕ by the standard characterization of Cantor space.

Let f=pr_Y|X. The base sheet makes f surjective; compact Hausdorff makes it proper. Because the K_n are pairwise disjoint, every y has the base preimage (y,0) and at most one upper preimage (y,1/n). Thus 1≤|f^-1(y)|≤2. The upper level K_n×{1/n} is **clopen** in X (the height 1/n is isolated in S), but its image K_n is nowhere dense, so f is **not open**.

Take
\[
E=\{(q_n,1/n):n\ge1\}\subset X.
\]
Each E point is isolated within E by its clopen height level, so E is a **discrete ordinary subspace**. The map f|E is bijective onto Q. Apply Lemma 2.1 for the claimed nonassociativity.

To show \(\rho_{\rm lc}(f)=\infty\), use Lemma 4.1 below: the existence of a dense discrete selector E into a perfect Hausdorff Y precludes any finite cover of the graph by partial homeomorphisms. □

**Consequence:** Finite maximum fiber size does not control finite chart rank: here
\[
\max_y|f^{-1}(y)|=2,\qquad \rho_{\rm lc}(f)=\infty.
\]
This improves the previous product-projection example, where the negative graph had infinite fibers. It is already sharp with respect to multiplicity: a continuous *one-to-one* map from compact X into Hausdorff Y is a homeomorphism onto its closed image, so has \(\rho_{\rm lc}=1\) and is in the positive algebra.

### 4. Direct topological obstruction to finite chart rank

**Lemma 4.1 (Baire obstruction).** Let Y be a nonempty **perfect Hausdorff space** (in particular Cantor space), let Q⊂Y be dense, and let f:X→Y be any map admitting a discrete subset E⊂X with f|E:E→Q bijective. Then f cannot be covered by **finitely many partial homeomorphism charts**, even if no locally closed condition is imposed on their domains and ranges.

**Proof.** Suppose X=U_1∪...∪U_m and f|U_i is a homeomorphism onto its image V_i with the subspace topologies. Put E_i=E∩U_i and D_i=f(E_i)⊂Y. Because E is discrete, each E_i is discrete. The restriction of a homeomorphism implies D_i is discrete as a subspace of Y (since V_i has the subspace topology in Y).

**Claim:** If Y is perfect and D⊂Y is discrete, then its closure has empty interior. Otherwise, some nonempty open O⊂cl_Y(D) has D∩O nonempty and dense in O; no element of D∩O can be isolated *in D*, because every open neighborhood of it inside O contains an open set with another D point, since O has no isolated points. Contradiction. Thus cl_Y(D) is closed nowhere dense.

The sets D_1,...,D_m cover Q, so their closures cover cl_Y(Q)=Y. This is impossible because a finite union of closed nowhere-dense sets is nowhere dense in every topological space, whereas Q is dense in the nonempty space Y. **No Baire hypothesis is needed.** □

The lemma proves **directly from ordinary topology** that our Cantor-to-Cantor f has infinite chart rank; this does not rely on the localic algebra theorem. It also explains the obstruction intuitively: finitely many invertible graph sheets cannot take a discrete source selector onto an ordinarily dense set of a perfect Baire target.

### 5. First comparison: safe branching versus unsafe accumulation of branches

| Map f | Global properties | Chart rank | Algebraic status |
|---|---|---|---|
| Homeomorphism | Proper, open, 1-to-1 | 1 | Positive |
| t↦t², [−1,1]→[0,1] | Proper, open, ≤2-to-1, branched | ≤2 | Positive via two closed charts |
| Cantor two-shift | Proper, open, exactly 2-to-1 local homeomorphism | ≤2 | Positive via two clopen charts |
| New Cantor f (Theorem 3.1) | Proper, surjective, ≤2-to-1, **not open** | ∞ | Explicit negative |
| Cantor×K→Cantor, K infinite compact metric | Proper, open, infinite fibers | ∞ | Explicit negative from prior segment |

The last row is [the earlier exact finite/infinite fiber dichotomy](ProjectA_GRAPH_LOCAL_HOMEOMORPHISM_POSITIVE_OPEN_PROPER_NEGATIVE_2026-11-20.md). The new Cantor example separates **uniformly finite fiber degree** from **finite graph-chart rank**. Hence *neither properness alone nor uniform finite degree together with properness* can replace the finite-chart hypothesis.

The still-meaningful missing corner is: **open + proper + uniformly finite fibers**, but not necessarily a local homeomorphism. The finite branched fold t↦t² is safe, while our Cantor two-to-one example is not open. At this stage we neither prove all such maps safe nor exhibit an unsafe one. The boundary is a concrete next problem, not a concealed conclusion.

### 6. Graph-theoretic consequence and big picture

Place X and Y as clopen blocks together with markers u,v inside a single compact Hausdorff G, and set
\[
H=\Delta_G\vee R\vee R^\smile\vee F\vee F^\smile\vee T\vee T^\smile,
\]
where R,F,T come from Theorem 3.1. H is a **single point-generated reflexive symmetric** localic relation. The four-block levels force the only possible three-step u→v path to have type R,F,T. Thus the same bracket-dependent ghost edge occurs in H^3: the left-associated u→v sector vanishes while the right-associated sector is the singleton point pair (u,v). The ordinary graph itself has no u–v path at all because f(E)=Q and u is adjacent only to I=Y\Q.

This is not an example of a *canonical Cameron–Kumar separation graph* of X or Y: the underlying compact Hausdorff spaces have trivial intrinsic inseparability/Urysohn graphs. It is an **imposed graph** exhibiting a separation between ordinary graph connectivity and localic relational paths. The original motivation is preserved by making the two kinds of graph precise rather than identifying them.

**Next bounded options:** (i) test whether every open finite-to-one map of compact Stone spaces has finite *locally closed* chart rank or at least passes the graph-probe (NR); (ii) analyze the image/pullback defect by its **fibers**, using the dense discrete selector criterion; (iii) describe higher witness nerves for finite graph charts and see whether the exact localic walk algebra can be promoted from binary to simplicial data.

No external audit has yet reviewed this note. The known positive compact-Hausdorff rectangle calculus is referee-verified; the subsequent graph-chart extensions and Cantor two-to-one counterexample remain **internal**.
