# Restricted graph-far candidate for arbitrary-locale V
22 October 2026. Working definition and first tests; no completeness assertion.

## Motivation and definition
U has an intrinsic far-open-rectangle definition, whereas V=fit(I) is defined via fitted hull. The dual-far closed-rectangle strip formula W was disproved for arbitrary locales by the countable Hausdorff rational-graph example; it succeeds if I is compact. Try augmenting dual-far strips by **closures of graphs of maps from open sublocales of X**. Restricting to graph maps avoids immediately admitting every closed off-I relation, which would be a tautological restatement of fit(I).

Let L=O(X), T=L⊕L, I=C(d_I). Given an open embedding i:U↪X and arbitrary locale map φ:U→X, let γ=(i,φ):U→X×loc X. Put
 q_φ=∨{a⊠b : i*(a)∧φ*(b)=0 in O(U)}.
Rectangles join-generate T, so q_φ is the largest γ*-annihilated open; S_φ=C(q_φ) is the closure of the image of γ. Declare φ **graph-far** if q_φ∨d_I=1, equivalently S_φ∧I=0.

Define W_gr = W ∧ ⋂_{φ graph-far}O(q_φ), where W=⋂_{dual-far strips s}O(s). Universally V⊆W_gr⊆W. Candidate conjecture W_gr=V for all X is **unproved**.

## Tests
1. Known countable Hausdorff counterexample: U=L_0 open left Q copy, φ(ℓ_t)=r_t right Q copy. Then γ is exactly rational graph map g, q_φ=q, and the independently audited cover q∨d_I=1 means φ is graph-far. The added O(q) is precisely the open neighborhood missing from strip-generated nucleus; hence W_gr⊆O(q). This removes the *specific witness* of V≠W, but does NOT prove W_gr=V even on this X.
2. If I is compact (in particular X compact or coherent), W=V, so V=W_gr=W automatically.

## Open problems
- Is W_gr=V universally? Most likely test with relations that are not closures of graphs of maps over open domains; need a concrete quotient witness.
- Does it hold for the existing countable Hausdorff X beyond merely eliminating q?
- Is requiring graph-far via q_φ∨d_I=1 conceptually useful, or can an intrinsic criterion be given in terms of map φ and separation in X?
- How restrictive is the open-domain graph family? Adding arbitrary two-leg spans γ:Y→X² risks trivializing the construction because any closed sublocale is its own domain; a controlled class (étale domains, local homeomorphisms, open embeddings) might work.
- Separation trees remain valid infinitary benchmark, with their independent conceptual motivation to be developed, not abandoned.
- Spatial-square criterion remains secondary research topic, independently interesting even though a strip counterexample exists.

## First stress test: symmetry defect and corrected bi-graph family (22 October)

The initial one-sided partial graph family need not be invariant under the flip τ of X×X: transpose of graph (i,φ) can fail to be a graph with *open-domain first projection*, unless φ has additional injectivity/openness conditions. Since V is symmetric, this is undesirable and makes a one-sided completeness claim unnatural.

**Symmetrized proposal.** For any open embedding i:U→X and locale map φ:U→X, let γ→=(i,φ), γ←=(φ,i), let q→,q← be largest opens annihilated by these maps, and include both O(q→) and O(q←) when q→∨d_I=1 (equivalently q←∨d_I=1, since flip τ fixes d_I). Define
 W_bgr = W ∧ ⋂_{φ graph-far}[O(q→)∧O(q←)].
Then τ(W_bgr)=W_bgr, V⊆W_bgr⊆W. If I is compact, all equal V. The rational graph counterexample's missing q is among the generators, so its original obstruction no longer survives.

**Exact completeness test.** Let G be the family of all dual-far strips and all forward/reverse graph-far opens. For j_bgr=∨^(Nuc T)_{u∈G}o_u, W_bgr=V iff no q≠1 satisfies q∨d_I=1 and u→q=q for every u∈G. This is the prior closed-sublocale obstruction theorem with enlarged generator family. A counterexample would be a nonzero closed sublocale R disjoint I for which every primitive remains dense. The original rational-graph S=C(q) is not such an obstruction because its own graph primitive O(q) has empty intersection with S.

**What has NOT been proved:** whether the enlarged family is complete in arbitrary locales, or even on the rational-bridge test space. Symmetry repair does not supply completeness. If graph closures of maps from open domains prove inadequate, possible next restriction class: local homeomorphisms/étale maps with multiple sheets; avoid allowing every closed sublocale as domain because that makes the formula tautological.

**Duality question reserved:** Graph-far neighborhoods look more like a fitted generating family than a literal dual of U's far open rectangles. No claim of true duality yet.

## Multivalued primitives: finite-branch redundancy, infinitary gap (22 Oct, continuation)

**Proposition (finite graph-image unions are redundant).** Let γ_i:U_i→X×_loc X be permitted forward/reverse open-domain graph maps and S_i=cl(im γ_i)=C(q_i), i=1,...,n. The closed hull of the union of images is S=∨_iS_i=C(∧_i q_i). If S∩I=0 then each S_i∩I=0, hence each γ_i is graph far. Its complementary open primitive is O(∧_i q_i)=∧_iO(q_i), already in the bi-graph generated meet. Therefore permitting relations that are finite unions of admissible graph images gives no new generator.

**Infinite branching is genuinely different.** For a family indexed by J, the **closure of the join of the S_i** is C(∧_{i∈J}q_i) (meet taken in frame); the raw infinite join of closed sublocales need not itself be closed. In either case, O(∧_i q_i) need not equal ∧_i O(q_i) for infinite J; finite intersection of open sublocales behaves differently from an infinite one. If the entire closed hull S is off I, each branch is graph far, yet O(∧_i q_i) may be a stronger neighborhood than the individual graph primitives collectively. This is a possible source of new power and parallels why finite rectangle joins were insufficient. Do not assert a strict inequality in our specific test space without construction.

**Controlled enlargement to test:** allow spans U←p−Y−φ→X with p a local homeomorphism (étale map) onto an open sublocale U⊆X, and use the closed image of (i∘p,φ):Y→X×X, including transpose. Graph far iff its closed image misses I. A finite open-sheet decomposition is redundant by the proposition; a genuinely infinite étale cover may introduce new neighborhoods. This remains non-tautological (not all closed relations are étale over a coordinate), symmetric after transposes, and works point-freely. Need check whether it strictly strengthens bi-graphs on the rational-bridge X or other controlled test frames.

**Central question still open:** Does the original bi-graph family already generate V? Neither an equality proof nor a counterexample obtained here. Infinitary-étale candidate is a fallback test, not promoted theorem.

## Étale-span reduction theorem (22 Oct 2026)

**Theorem.** Any étale span X←p−Y−φ→X, with p a local homeomorphism, can be covered by local sections V_i≅U_i⊆_open X, giving partial graph maps γ_i=(inclusion,φ_i). If q_i is the largest open killed by γ_i*, then the largest open killed by γ*=(p,φ)* equals q=∧_i q_i (meet IN frame T). Proof: γ*(t)=0 iff γ_i*(t)=0 for all i because V_i cover Y; equivalently t≤q_i for all i, iff t≤∧_i q_i. Conversely any set-indexed family of partial maps gives an étale span p:⊔U_i→X, with the same q=∧_i q_i. Transpose family also included. Thus the étale-generator proposal is **exactly** a scheme adding O(∧_i q_i) for arbitrary families of partial graphs for which d_I∨∧_i q_i=1.

Every individual branch is then graph far (q≤q_i), but collectively graph-far is a stronger condition and does not automatically follow from individual farness.

**Gluing redundancy:** If partial maps φ_i are restrictions of a single map φ:U→X with open domains U_i covering U, then ∧_i q_{φ_i}=q_φ; the étale generator is already in the original bi-graph family even for infinitely many branches. In particular, any étale decomposition of the rational-bridge homeomorphism φ:L_0→R_0 gives exactly the previously available q_φ=q. Thus merely replacing the rational graph by an infinite cover of its domain cannot strengthen the candidate.

**Genuine test target:** incompatible families of partial graphs, particularly infinitely many conflicting branches with jointly far closed hull. Finite families redundant; compatible infinite families redundant. We have NOT shown that any incompatible infinite family strictly enlarges the bi-graph nucleus for the rational-bridge space. We have NOT settled completeness of the original bi-graph formula.

## Explicit infinite incompatible étale family on rational-bridge X (22 Oct)

Strengthen sequence choices to irrational limits α_n,β_m with β_m−α_n∉Q for all n,m (possible recursively by avoiding countably many real values). Let C={0}∪{c_n:n∈N}, with distinct nonzero rational c_n→0. For each c∈C let φ_c:L_0→R_0 be φ_c(ℓ_t)=r_{t+c}; all domains equal open L_0 and maps disagree everywhere, hence they cannot glue.

The union of ordinary graph relations is F_C={(ℓ_t,r_{t+c}):t∈Q,c∈C}. This is closed in X×top X and disjoint Δ:
- in L_0×R_0 it is inverse image of closed compact C under (t,s)↦s−t;
- near (z_n,r_s), the possible left limiting shifts lie in α_n+C, a compact set of irrationals excluding rational s;
- near (ℓ_t,z_m), t+C is rational compact and misses irrational β_m;
- near (z_n,z_m), α_n+C is compact, disjoint from β_m by the choice β_m−α_n∉Q.
In every case compactness of C supplies uniform separation and a rectangle missing F_C.

For each c let q_c be largest element of T=O(X)⊕O(X) killed by its graph map; define q_C=∧_{c∈C}q_c. This is exactly the graph-null open of the étale span with domain ⨿_{c∈C}L_0. Let e=L_0∨R_0, Z=C(e) closed discrete. As before e⊠e≤q_C∨d_I: the 3 quadrants other than L_0⊠R_0 lie below **every** q_c, and L_0⊠R_0≤d_I. At each point with a Z coordinate, closedness of F_C yields a product-open rectangle disjoint from all graphs, whose frame element lies below q_C. The elementary boundary lemma yields **q_C∨d_I=1**. Hence the incompatible infinite étale family is collectively graph far.

For each finite proper C_0⊂C, q_C<∧_{c∈C_0}q_c: pick c∈C\C_0 and a point (ℓ_t,r_{t+c}) of its graph, which is outside the closed finite union of other graphs; a rectangle witnessing this lies below ∧_{c∈C_0}q_c but not q_C. Therefore the infinite family yields a *strictly new frame open compared with every finite subfamily*. This does **not** prove that its open nucleus is new relative to the nucleus generated by **all** individual bi-graph primitives; the latter comparison remains unresolved.

Potential limitation: Is O(q_C) already in W_bgr via other graph-far partial maps not among the translation family? Need an explicit W_bgr-fixed non-top element r with q_C→r>r, or a proof q_C is absorbed. Current construction alone does not resolve that.

## Translation family: a two-stage topological test (22 Oct, continuation)

Let C={0}∪{c_n:n≥1}⊂Q with distinct nonzero c_n→0; F_c={(ℓ_t,r_{t+c}):t∈Q} and F_C=⋃_{c∈C}F_c, closed in **ordinary** X×X by the previous construction. Let W_C=X²_top\\F_C and s_c=X²_top\\F_c (ordinary open graph complements). The nucleus operator P_top generated by the s_c satisfies **P_top²(W_C)=1**: each isolated shift c_n is isolated in parameter C, so difference-map preimage gives an open neighborhood N around every point of F_{c_n} with N∩F_C⊆F_{c_n}, hence F_{c_n}⊆s_{c_n}→W_C⊆P_top(W_C). Thus P_top(W_C)⊇X²_top\\F_0=s_0 and s_0→P_top(W_C)=1. This is not a proof that the **localic** bi-graph nucleus sends q_C to 1. The square X×_loc X is nonspatial; passing from ρ(P_local(q_C))=1 to P_local(q_C)=1 is invalid. Need a frame-level boundary or C-ideal argument for this remaining discrepancy.

The explicit family thus supplies evidence that infinite branching may be absorbed by existing graph nuclei, but only on the ordinary spatial comparison. This substantially reduces its value as a candidate strictness witness; all remaining obstruction would be localic/pointless.

## Resolution of the compact scattered translation-family test by localic difference map (22 Oct)

**Theorem (specific rational-bridge model with compact shift C={0}∪{c_n→0}):** The bi-graph prenucleus P_bgr satisfies P_bgr²(q_C)=1; therefore j_bgr(q_C)=1. The infinite, incompatible, collectively graph-far étale primitive O(q_C) adds **no new nucleus generator** in this test case. This is a localic proof, not a pointwise inference.

Proof. Let T=O(X)⊕O(X), b=L_0⊠R_0, and B=O(b)≅Q×_loc Q. Real subtraction restricts to localic difference map δ:B→R. For each rational c, the localic fiber δ^{-1}({c}) is the closed translation graph G_c in B, so the restriction of graph-null open q_c to b is
   b∧q_c = δ*(R\{c})   [as open elements of the localized frame ↓b].
Justification: Q→R is a sublocale embedding, products preserve such pullback embeddings, and δ fibers are pullbacks of the closed real graph of translation; the translation graph Q→Q×_loc Q is a closed embedding in B. The kernel open q_c restricts to the complementary open of this closed graph. Beware: for infinite C, b∧q_C=∧_c(b∧q_c), which need NOT equal δ*(R\C), because δ* need not preserve infinite meets.

For each isolated shift c_n choose an open real interval J_n with J_n∩C={c_n}. Since δ restricted to graph G_c is constant c, for c≠c_n,
   δ*(J_n) ≤ b∧q_c.
Therefore
   δ*(J_n)∧(b∧q_{c_n}) ≤ b∧q_C
and Heyting adjunction in ↓b gives
   δ*(J_n) ≤ (b∧q_{c_n}) →_b (b∧q_C)
                  = b∧(q_{c_n}→q_C)
                  ≤ b∧P_bgr(q_C).
Also δ*(R\C)≤b∧q_C, as it annihilates each shift graph. Since R\{0}=(R\C)∪⋃_n J_n, preserve joins to obtain
   b∧q_0=δ*(R\{0})≤b∧P_bgr(q_C).
By global Heyting adjunction,
   b∧q_0≤P_bgr(q_C) ⇒ b≤ q_0→P_bgr(q_C)≤P_bgr²(q_C).
The last inequality uses q_0 as a graph-far primitive and P_bgr² as next application.

Let e=L_0∨R_0. Three of four quadrant opens in e⊠e lie below q_C, because all translation graphs lie in L_0×R_0; the fourth is b, now ≤P_bgr²(q_C), so e⊠e≤P_bgr²(q_C).
F_C is closed ordinary off-diagonal (shown earlier), so for each pair with coordinate in Z=X\e closed discrete, a product-open rectangle misses F_C; its frame rectangle lies below q_C and hence below P_bgr²(q_C). Apply the elementary frame boundary lemma (from Claude external audit) to u=P_bgr²(q_C): conclude u=1.

**Scope:** The argument requires both the shift family having isolated points accumulating at one limit and its realization as closed translation fibers of δ with open parameter separation. Does not show that arbitrary infinite étale families are redundant, nor bi-graph completeness for arbitrary locales or for the rational-bridge locale. The individual graph-far opens q_c are valid in the strengthened rational-bridge construction because each graph closure misses I (same boundary argument used for collective q_C, and q_C≤q_c implies q_c∨d_I=1).
