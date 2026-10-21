# A — Closure properties of the class I=U

**21 October 2026.** Working theorem/counterexample note. Not independently audited after compilation. Consult [A-coproduct-preservation-I-U.md](A-coproduct-preservation-I-U.md) for full point-free proof of coproduct preservation.

Let C={L frame : I(L)=U(L)}, with d_I=∨_{a∧b=0}a⊠b and d_U=∨_{a*∨b*=1}a⊠b in L⊕L.

| Operation | Preserves C? | Reason |
|---|---|---|
| Arbitrary frame products | YES | Correspond to localic disjoint unions; components clopen; both relations componentwise |
| Arbitrary frame coproducts | YES | Finite-support rectangle zero detection and transport of far covers (separate proof note) |
| Subframes | NO | O(Q)⊆P(Q) where Q finite Alexandrov and I(Q)≠U(Q), while P(Q) Boolean |
| Surjective frame quotients | NO | Q embeds in P obtained by adjoining a new top point; restriction O(P)↠O(Q), with I(P)=U(P) |

## Finite witness

Let Q={a,b,c,s,t} with covers a<s, b<s, b<t, c<t and no other strict comparisons beyond transitivity; use upper-set topology.

↑a={a,s} and ↑c={c,t} are disjoint, hence (a,c) is outside I. But b belongs to both closures cl(↑a) and cl(↑c), and hence every open neighborhood of a and of c has intersecting closures: (a,c)∈U. Therefore I(Q)≠U(Q). Since Q finite, the localic and pointwise relations can be identified here.

The Boolean P(Q) has I=U. O(Q) is a subframe of P(Q), giving failure under subframes.

Add a new top point ω to Q to form P. Every pair of nonempty opens of P meets at ω, so I(P)=U(P)=P×P. The inclusion Q↪P induces surjection O(P)→O(Q) by restriction; every nonempty upper set V⊆Q extends as V∪{ω}. Thus failure under surjective frame homomorphisms, even among finite coherent frames.

## Products

If L=∏_i L_i (frame product), its locale is the disjoint union of locales X_i. Mixed-component pairs are separated by complemented component opens (hence far). On each component both closed relations restrict to the corresponding relations of X_i. This proves I(L)=U(L) iff every factor has equality (ignoring degenerate-factor bookkeeping). The empty product case satisfies equality. A direct frame-theoretic proof can be added for publication.

## Coproducts

See [A-coproduct-preservation-I-U.md](A-coproduct-preservation-I-U.md) (committed 20 Oct 2026) for the detailed proof, including the degenerate factor edge case and arbitrary (possibly noncoherent) frames. Coherent corollary: conormal bounded distributive lattices are closed under arbitrary coproducts, using ideal completion/coherent-frame correspondence.

## Audit cautions

- The coproduct theorem is recorded as a **working proof**, not yet independently refereed.
- The topology/locale variance reverses products and coproducts.
- Quotient of *frames* corresponds to a sublocale, while *subframe* is an injective inverse-image embedding.
- Do not conflate closure of C under products/coproducts with closure under arbitrary colimits or limits.
