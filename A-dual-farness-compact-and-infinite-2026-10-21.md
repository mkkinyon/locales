# Dual-farness follow-up: compact closed complements and arbitrary frames
21 Oct 2026. Working mathematics; independently audit before manuscript.

## Finite witnesses under local compactness of closed complements

For arbitrary locale X and k,h∈O(X), define dual far by d_I∨(k⊠1)∨(1⊠h)=1. If closed sublocales C(k),C(h) are compact, then k,h dual far iff there are opens a,b with a∧b=0, k∨a=h∨b=1. This follows by restricting the disjoint-rectangle covering of I's complement to the compact closed product C(k)×C(h), extracting finitely many rectangles and applying the finite-rectangle lemma. Thus the compact frame theorem extends to cocompact opens of an arbitrary locale.

## Failure of finite witnesses in arbitrary frames

For a Hausdorff X, I=Δ and k,h are dual far iff the closed complements A=C(k),B=C(h) are disjoint. Disjoint-supplement witnesses are precisely disjoint open neighborhoods of A,B. In a Hausdorff nonnormal space such as the Sorgenfrey plane, choose disjoint closed non-open-separable A,B (rational and irrational points of the closed discrete anti-diagonal). Then dual far holds but no disjoint supplements exist. So compactness or compactness of closed complements cannot simply be dropped.

## Exact infinitary formulation

Always k,h dual far iff I∩(C(k)×C(h))=0 as sublocales, equivalent to the disjoint rectangles a⊠b, a∧b=0, covering the closed product C(k)×C(h). No finite subcover need exist. This is an exact coproduct-free-in-notation rectangular covering statement, but NOT a pair of lattice supplements. A useful intrinsic infinitary lattice criterion avoiding products remains open.

## Compact-locale strip formula

Define W=meet over all dual-far k,h of O((k⊠1)∨(1⊠h)). Universally V=fit(I)⊆W, because all strips contain I. Equality is established for coherent locales in preceding note.

For compact Hausdorff X, W=Δ=V. Given open diagonal neighborhood G, compact X²\G is covered by interiors of finitely many closed rectangles A×B disjoint from Δ (compact Hausdorff normality gives disjoint closed neighborhoods around every off-diagonal point). Complements of these rectangles are dual-far strips whose finite intersection is contained in G. This proves W⊆O(G) for every diagonal neighborhood and hence W⊆fit(Δ)=Δ.

For **general compact locales**, W=V is still UNRESOLVED by this segment. Key problem: special dual-far open strips need to be cofinal in the fitted-neighborhood meet, not just have exact individual separation witnesses. Compact three-limit-point noncoherent example from Claude audit is a recommended test. No assertion of equality beyond coherent and compact Hausdorff.

## RESOLUTION: compact sublocales have strip-generated fittings

**Theorem (all locales X,Y).** For any compact sublocale S of X×Y, fit(S) equals the intersection of all open strips O((k⊠1)∨(1⊠h)) containing S. Closedness of S, compactness of ambient factors, coherence and spatiality are not needed.

Proof. Let O(w) contain S. Write w=∨_i(a_i⊠b_i). Compactness of S selects a finite subcover w0=∨_{i=1}^n(a_i⊠b_i)≤w, still containing S. Set A_i=a_i⊠1, B_i=1⊠b_i. Finite distributivity in the frame gives w0=∨_i(A_i∧B_i)=∧_{σ∈{0,1}^n}(∨_{σ(i)=0}A_i∨∨_{σ(i)=1}B_i). Every factor is a strip sσ≥w0, so every such O(sσ) contains S. Their finite intersection O(∧sσ)=O(w0) lies in O(w). Hence the meet of all strips containing S lies in every O(w) containing S, exactly fit(S). The reverse inclusion is tautological.

**Corollary (compact locale X):** I=C(d_I) is compact because it is closed in compact X². Therefore V=fit(I)=meet_{k,h dual far} O((k⊠1)∨(1⊠h)), where dual far means d_I∨(k⊠1)∨(1⊠h)=1. Thus the compact strip formula formerly marked OPEN is now PROVED for arbitrary compact locales.

**Generalization:** The result holds whenever I itself is a compact sublocale, even if X is not compact. More generally fit(S) for compact S in any binary product is strip generated.

**Limit:** Without compactness of S, the finite extraction and CNF step do not directly apply. The previous nonnormal Hausdorff counterexample still shows that arbitrary-frame dual far need not have a single disjoint-supplement witness.

**Status correction:** Earlier paragraph marking arbitrary compact strip formula UNRESOLVED is superseded by this theorem.

## Noncompact arbitrary-locale push (21 Oct, subsequent segment)

**Infinite Alexandrov point theorem.** For every poset P with upper-set topology, define ordinary I by common upper bound. Intersect all open strips (K×P)∪(P×H) containing I, for K,H upper sets. This intersection is exactly ↑I=D∘D, no compactness. Given (x,y) outside ↑I choose K=P\↓x and H=P\↓y; their strip contains I and excludes (x,y). Reverse inclusion follows because strips are upper sets. This is a point-set result; not claimed as a sublocale equality for arbitrary infinite Alexandrov frames.

**T1 point-level warning.** For any T1 space and any relation S⊆X², the ordinary intersection of all open strips containing S has point set S: to exclude (x,y)∉S use strip ((X\{x})×X)∪(X×(X\{y})), whose complement is the closed singleton pair. Likewise ordinary intersection of all open neighborhoods of S is S. Hence pointwise testing cannot settle the localic strip equality in noncompact sober T1 spaces.

**Infinite-distributivity obstruction.** Compact-sublocale proof uses a finite rectangle subcover, then distributive DNF→CNF:
∨_{i=1}^n(A_i∧B_i)=∧_{σ∈{0,1}^n}(∨_{σ_i=0}A_i∨∨_{σ_i=1}B_i).
For arbitrary infinite joins the analogous formula is NOT a frame identity (would require a form of complete distributivity absent in general frames). A compact exhaustion of I does not automatically produce globally admissible strips; each strip must contain all of I. Therefore no general sublocale theorem has been proved by this route.

**Status:** Exact universal result V⊆W, with W=meet of dual-far strips, remains. Coherent / compact I equality as before. Arbitrary noncompact localic W=V unresolved. Need an explicitly nonspatial witness or a new point-free argument; do not infer from point equality.

## Nuclei-lattice reduction: exact arbitrary-frame test

Let Q=L⊕L and d=d_I. Put Φ={w∈Q:d∨w=1}, and Σ={s=(k⊠1)∨(1⊠h):d∨s=1}. For open nucleus o_w(q)=w→q, define

    j_V=∨^(Nuc Q)_{w∈Φ}o_w,
    j_W=∨^(Nuc Q)_{s∈Σ}o_s.

Universally j_W≤j_V, and W=V iff for every w∈Φ, j_W(w)=1. This follows from o_w≤j iff j(w)=1, and the fitted hull of I has exactly the neighborhood filter Φ.

For explicit transfinite saturation, let Σ^∧ contain finite meets of members of Σ (including 1) and define

    P(q)=∨_{s∈Σ^∧}(s→q).

Because open nuclei compose as o_s o_t=o_(s∧t), the family indexed by finite meets is directed in nucleus order. P is therefore a monotone inflationary finite-meet-preserving **prenucleus**, generally not idempotent. The transfinite pointwise iteration P^0=id, P^(α+1)=P∘P^α, P^λ(q)=∨_{α<λ}P^α(q), stabilizes at the nucleus j_W. Consequently:

    W=V iff every w with d∨w=1 satisfies P^∞(w)=1.

A counterexample needs such w with P^∞(w)≠1. A strong sufficient criterion is P(w)=1 for every w∈Φ; compactness of I gives an even stronger finite-strip-meet refinement s≤w, as previously proved. These criterion statements are exact in arbitrary frames and make no spatiality/coherence assumption. They do NOT settle W=V in general.

**Key caution:** joining open nuclei inside Nuc(Q) is not the same as a pointwise join. The latter is a prenucleus whose transfinite closure is the actual join.
