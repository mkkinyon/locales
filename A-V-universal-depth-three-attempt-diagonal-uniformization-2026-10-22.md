# Attempt at universal H-V-H depth-three theorem: diagonal trace and uniformization gap

22 October 2026. Status: **not proved**.

Let L be an arbitrary frame, T=L⊕L, d=∨_{a∧b=0}a⊠b, and B a rectangular bar d∨b_B=1 with b_B=∨_{(u,v)∈B}u⊠v.

The diagonal evaluation μ:T→L maps u⊠v to u∧v, and μ(d)=0. Therefore a NECESSARY condition for barhood is the diagonal cover

  1=∨_{(u,v)∈B}(u∧v).  (DC)

No converse is claimed.

Define h(b)=b*∨∨_{(u,v)∈B,b≤v}u, and k(a)=∨{b:a≤h(b)}. Then the exact depth-three H-V-H criterion is

  1=∨{a:k(a)=1}.   (*)

Elementary inequalities:

  k(a) ≥ a*∨∨_{(u,v)∈B,a≤u}v.

Proof: for b≤a*, a∧b=0 hence a≤b*≤h(b), so a*≤k(a). For any B rectangle (u,v) with a≤u, h(v)≥u≥a, so v≤k(a).

In particular if there is a B leaf (u,v) and a≤u with a*∨v=1, then k(a)=1. A sufficient, strong condition for (*) is

  1=∨{a: exists (u,v)∈B, a≤u, a*∨v=1}.

Regular frame argument: (DC) and regularity allow, for each (u,v), write u∧v=∨{a:a≺u∧v} (with a≺c iff a*∨c=1); each a≤u and a*∨v=1, hence (*) follows, actually yielding H-V depth two. This does not generalize to arbitrary L.

The attempted universal proof from (DC) fails precisely when no globally covering refinement a of diagonal rectangles satisfies k(a)=1; even the stronger single-leaf candidate is known to fail for rank-three rational-bridge examples (otherwise H-V depth two). One must use multiple varying b at each a to establish k(a)=1. No mechanism was found in the bare frame axioms to upgrade (DC) to (*).

Also note the subtlety: (*) is H-V-H, a stronger claim than unrestricted depth ≤3 (which allows V-H-V as an alternative). The two orientation-specific conditions are not proved equivalent for arbitrary bars.

Next mathematical goal: establish an exchange or uniformization lemma using the stronger localic bar identity d∨b_B=1 (not merely its diagonal trace), or build a frame counterexample. DO NOT cite this note as a proof of universal depth three.
