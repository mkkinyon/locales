# Project A — Hereditary local-rank criterion for fitted-stage jumps

Date: 23 October 2026. **New working lemma, direct complete proof.** This segment targets the genuine question V3 ⊋ V4, not merely individual rank-four bars.

## 1. Graph-null bars and restrictions

Let L=O(X), Q=L⊕L, d=d_I, and g:Y→X×locX any locale map. Define q=q_g=⋁{t∈Q:g*(t)=0}, the greatest g-null open. Assume q∨d=1 and Y is nonzero; then q<1. For each 0<k∈O(Y), let g_k:O(k)→X² denote the restriction of g to the open sublocale O(k), and set
    q_k=⋁{t∈Q:k∧g*(t)=0}.
Then q≤q_k<1, every q_k is a bar, and rank(q_k)≤rank(q) whenever finite, by monotonicity of canonical bar leaf families.

Let Phi_n be all bars with separation tree rank≤n, and let j_n=∨_{v∈Phi_n}o_v in Nuc(Q), o_v(t)=v→t.

## 2. Main exact hereditary-rank theorem

**THEOREM.** For any g and n, the following are equivalent:
  (A) every v∈Phi_n has dense inverse image g*v in O(Y): (g*v)*=0;
  (B) rank(q_k)>n for EVERY nonzero open k∈O(Y).

Proof (A⇒B): if rank(q_k)≤n then v=q_k is rank≤n bar, but k∧g*v=0 and k>0, so g*v cannot be dense.
Proof (B⇒A): if g*v is not dense, let k=(g*v)*>0. Then k∧g*v=0, so v≤q_k; since v is a bar of rank≤n, q_k is also one of rank≤n, contradiction.

The known graph-density witness argument proves (A)⇒j_n(q)=q, for ANY g: if t∧v≤q, then g*t∧g*v=0 and density gives g*t=0, hence t≤q.

For the reverse, assume the inverse-image opens of g form a *positive pseudobasis* of Y:
   (**PB**) for every k>0 in O(Y) there is t∈Q with 0<g*t≤k.
This holds in particular if g* is surjective, e.g. if g is a locale embedding, and for the rational parameter diagonal graph t↦(ell_t,r_t).

If j_n(q)=q and some v∈Phi_n has non-dense g*v, put k=(g*v)*>0. Choose t by PB with 0<g*t≤k. Then g*(t∧v)=0, so t∧v≤q, hence
   t≤v→q≤j_n(q)=q,
contradicting g*t>0. Thus j_n(q)=q⇒(A).

**EXACT CRITERION under PB:**
    j_n(q)=q
    ⇔ all rank≤n bars pull back densely
    ⇔ ∀ k>0, rank(q_k)>n.

When q has rank n+1, the criterion yields a fitted-stage jump
   V_n ⊋ V_(n+1)
iff EVERY nonzero open restriction q_k also has exact rank n+1 (since rank(q_k)≤n+1), under PB.

More generally, if Y has a basis B of nonzero opens, it suffices to test k∈B: for arbitrary k>0 choose basis b≤k; q_b≥q_k, so rank(q_b)≤rank(q_k). If rank(q_b)>n, then rank(q_k)>n. For Y=Q with ordinary rational topology, a countable rational interval basis suffices.

## 3. Why this is more than a reformulation of the original density proof

The original graph-density witness lemma required ∀v of rank≤n, density of g*v, quantifying over a huge and not readily parametrized class of bars. The new criterion replaces this by the **minimal rank of a single canonical null bar q_k for each open parameter restriction**, checkable over an explicit countable basis in the rational graph source. No point-set spatiality of X² is used.

**Known rational bridge recovered.** For the graph g(t)=(ell_t,r_t), source Y=Q, q_g has exact rank3. For every nonempty rational interval J, restricted null bar q_J still fails both rank-two orientations: every smaller rational interval inside J contains a bridge with left and right attaching sequences. Hence rank(q_J)>2; also q_J≥q_g gives rank≤3. Thus rank(q_J)=3 for all nonempty J. By the theorem,
    j_2(q_g)=q_g,  j_3(q_g)=1,
recovering V2⊋V3. The upper bound on restricted rank comes freely from q_J≥q_g, no fresh bar tree needed.

**Exact new target:** To obtain V3⊋V4 with a rational-parameter graph g, it suffices to build
   rank(q_g)=4
and prove for EVERY basic nonempty rational interval J,
   rank(q_{g|J})=4.
In particular a rank-four bar that becomes rank three on any parameter interval cannot work.

## 4. No-go for symmetric K-fan rank-four bars, generalized

If q is a bar and there exist finitely many rank≤n bars v_1,...,v_m such that
   v_1∧...∧v_m≤q,
then j_n(q)=1: composition of their open nuclei acts as
   (v_1∧...∧v_m)→q=1.
This strengthens the earlier finite-meet lemma, which stated equality rather than just ≤.

At the graph level, if g*q=0 and v_1∧...∧v_m≤q, then
   ⋀_i g*v_i=0.
Finite meets of dense opens are dense in ANY locale, so at least one g*v_i is NOT dense. By §2, there is some nonzero k with rank(q_k)≤n. Under PB, j_n(q_g)>q_g.

In the two-level K-fan exact-rank4 example,
   s=w∧τ(w),
where both w and τw are rank3 bars. Therefore s is completely absorbed by j_3. Moreover ANY graph g with g*s=0 and PB fails the hereditary-rank4 test: some nonzero parameter restriction is annihilated by either w or τw, a rank3 bar. This gives a parameter-local reason the rank-four syntactic complexity cannot witness V3⊋V4.

## 5. Strong geometric necessary condition in the Hausdorff case

Suppose X is Hausdorff and q_g has hereditary exact rank4. For every nonzero parameter open k, q_k is a bar of rank4. Let S_k=D∪B_(q_k), and define the one-stage horizontal/vertical good-open unions
   t_H(k)=∨{b∈O(X):(1,b)∈H(S_k)},
   t_V(k)=∨{a∈O(X):(a,1)∈V(S_k)}.
Their closed ordinary residuals F_H(k)=X\t_H(k), F_V(k)=X\t_V(k) must BOTH be NONCOMPACT: by the audited bar-specific compact-residual theorem, compact F_H(k) would yield a rank≤3 H-V-H tree, and compact F_V(k) a rank≤3 V-H-V tree. For first-countable Hausdorff X, both must fail COUNTABLE compactness by the stronger countably-compact-residual theorem.

Thus a hereditary rank-four graph requires **two noncompact irregularity reservoirs in EVERY nonempty parameter slice**. In particular the locally compact boundary full-interval rational-bridge setup, with rank3 upper bound even for arbitrary boundary topology, is excluded: its q_g and all restrictions have rank≤3.

## 6. Proposed construction test, NOT yet a construction

Search for a fused two-layer rational graph bridge, not a disjoint fan or finite meet of orientation-rigid bars. Require:
(i) an explicit localic bar q_g of height≤4;
(ii) every nonempty rational parameter interval J has both depth-three orientation tests fail for q_(g|J);
(iii) no rank3 bar with inverse image vanishing on any interval (equivalent to (ii));
(iv) a nonzero graph parameter source with PB, automatic for the usual diagonal rational graph.

A naive two-layer accumulation of dense bridge points cannot work if it destroys Hausdorffness or makes q_g fail barhood; see A-V-graph-parameter-thickening-rank-invariance and A-V-arbitrary-bridge-boundary-universal-rank-three notes.

**STATUS:** Strict fitted jump V3⊋V4 not established or ruled out; the new theorem is a workable local-rank test and a stronger screening condition for candidate constructions.
