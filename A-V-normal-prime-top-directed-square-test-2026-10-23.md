# Project A — Join-prime top / ultraconnected normal locales: exact simplifications and directed-square theorem

23 October 2026. **Working bounded research segment; no proof or counterexample of the universal prime-top V=whole implication.** Follow-up to A-V-normal-cozero-localization-of-bidense-residuals-2026-10-23.md.

## 1. Prime top and ultraconnectedness

Let L be a nontrivial frame with 1 FINITELY join-prime:
   a∨b=1 ⇒ a=1 or b=1.
This means any two NONZERO CLOSED sublocales C(a),C(b) meet nontrivially, because C(a)∩C(b)=C(a∨b). In spatial topology it is the ultraconnected property (any two nonempty closed sets intersect). It is not the same as irreducibility/hyperconnectedness (0 meet-prime). It does NOT mean 1 is completely join-prime or compact.

Every such L is normal: a binary cover has a top term, so 0,1 are trivial normality witnesses. And any far pair a*∨b*=1 has a=0 or b=0. Thus
   d_U=0, U=C(0)=X², and F=X² since normality gives F=U.

A useful stronger direct observation: every frame map h:O(R)→L has range {0,1}. If h(u)<1 and t≺u in O(R), then h(t)*∨h(u)=1, so top join-primality implies h(t)*=1 and h(t)=0. Since O(R) regular, h(u)=∨_{t≺u}h(t)=0. Thus h(u)∈{0,1} for all u; h factors through the point of R associated to a constant real. Therefore there are NO nonzero proper real-function cozero opens, and the regular core operator ρ(a)=∨_{t≺a}t satisfies ρ(a)=0 for all a<1, ρ(1)=1. The cozero-localization and regular buffer methods provide NO proper patches in this class.

Target question:
  **(JP) 1_L finite join-prime ⇒ fit(C(d_I))=X² ?**
equivalently
  w∨d_I=1 ⇒ w=1  (all w∈L⊕L).
An even stronger question is whether D=fit(Δ)=X², i.e., whether δ*:L⊕L→L REFLECTS top.

The spatial point-set theorem: if a topological space is ultraconnected, every open neighborhood of its diagonal in the ORDINARY product is the whole product (proof from common specialization predecessor). This alone cannot establish the localic equality for nonspatial localic products.

## 2. A direct two-level C-ideal certificate for directed covers

**THEOREM (any frame).** If C⊆L is an UPWARD DIRECTED set with ∨C=1, then
    **∨_{c∈C}(c⊠c)=1** in L⊕L.

Proof: for each c∈C, its upper tail C_c={d∈C:c≤d} is cofinal, hence joins to 1. Therefore
    c⊠1=∨_{d∈C_c}(c⊠d)≤∨_{d∈C_c}(d⊠d).
Joining over c gives 1⊠1≤∨_c c⊠c. No topology/spatiality/normality.

More generally if an arbitrary cover C of L has a refinement D which is upward directed and still covers 1 (each d∈D lies below some c∈C), then ∨_{c∈C}c⊠c=1.

**Consequently:** if EVERY cover of L has an upward-directed refinement, then D=X², hence V=U=F=X². This is a strong sufficient condition, not shown equivalent to finite join-primality.

A further important local version: if w∈L⊕L satisfies δ*w=1, and some rectangular presentation of w gives a diagonal cover c_i=a_i∧b_i that has an upward-directed refinement, then w=1. (For any w, such a presentation exists, and c_i⊠c_i≤a_i⊠b_i≤w.)

**Obstruction:** A potential proper diagonal-neighborhood bar in a prime-top frame must have a diagonal cover without a directed refinement. This is a genuine infinitary issue, not a finite-join issue.

**COROLLARY (pointfree proof for all down-directed Alexandrov posets).** If P is downward-directed, the set K={↑p:p∈P} of principal upsets is upward-directed under inclusion: for any p,q choose r≤p,q, so ↑p∪↑q⊆↑r. It covers P. Given any cover C by upsets, for each p choose c∈C containing p; then ↑p⊆c. Hence the SAME directed family K refines every cover. The theorem gives D=whole in Up(P) using only the frame coproduct, not ordinary points or spatiality arguments.

**GENERAL COROLLARY.** If L has a directed join-dense family K of completely join-prime elements (k≤∨C implies k≤c for some c∈C), then K refines every cover, hence D=V=U=F=whole. No separate ultraconnectedness hypothesis needed; this property implies joinprime top because for any a∨b=1, the directed K forces one side top. This makes the directed-cover criterion a structural theorem covering all downward-directed Alexandrov examples.

## 3. Necessity of finite join-primality for a total fitted relation (normal case)

Suppose L is normal, a∨b=1, a<1,b<1. Then using normality choose u,v with
    a∨u=1=b∨v,   u∧v=0.
Define
    w=(a⊠1)∨(1⊠b).
Expand (a∨u)⊠(b∨v)=1:
all three mixed terms are ≤w and u⊠v≤d_I. Hence w∨d_I=1, i.e., w is a bar.
But w<1, since C(a)×C(b) is a nonzero closed sublocale of X² disjoint from O(w) (the product of two nonzero locales is nonzero). Consequently V≠whole.

Thus for NORMAL L,
    **V=whole ⇒ 1_L finitely join-prime**.
The converse is exactly open question (JP); so the prime-top case is not an incidental subclass but the entire outstanding issue of whether total functional equivalence necessarily forces total fitted inseparability.

In fact (for normal L) U=F=whole iff 1_L join-prime. The forward direction follows from normal pointfree Urysohn separation: proper binary cover a∨b=1 supplies disjoint nonzero closed sublocales C(a),C(b), and a nonconstant real-valued map separates them; its kernel pair is then proper. The backward direction is §1.

## 4. Possible product reduction and its exact scope

For L top join-prime, if the coproduct frame Q=L⊕L ALSO has join-prime top, then automatically JP holds: since d_I<1 (δ*d_I=0), any w∨d_I=1 forces w=1.

But it has **NOT** been proved that finite join-primality of top is preserved under coproducts of arbitrary frames. Spatial ultraconnected spaces have ultraconnected ordinary topological products; this does not settle localic products that may contain nonspatial closed residuals. Do not claim this preservation as a theorem.

A hypothetical JP counterexample would thus also refute this coproduct-stability assertion and, by previous normality reductions, furnish a nonzero pointless closed residual C(w) with bi-dense coordinate projections after closed-sublocale pruning.

## 5. Consequence for choosing the next attack

The prime-top case has no proper cozero opens and trivial regular core ρ on proper elements; previously promising normality tools are therefore ineffective. The two meaningful options are:
- settle the specific coproduct stability of join-prime top, or
- use the C-ideal calculus to study directed refinements versus truly non-directed infinite diagonal covers.

No unconditional outcome is claimed. Compare the standard topological ultraconnectedness discussion (e.g. Steen–Seebach, or *Encyclopedia of Mathematics* Connected components); the classical product fact does not constitute a point-free proof.
