# Two-map orthogonality test for the full rectangular bar identity
Date 22 October 2026.

Let L be any frame, T=L⊕L, d=∨{a⊠b:a∧b=0}, and w∈T. Let M be any frame and f,g:L→M frame homomorphisms satisfying the CROSS-ORTHOGONALITY condition
  a∧b=0 in L ⇒ f(a)∧g(b)=0 in M.
The coproduct map [f,g]:T→M sends d to 0. Therefore d∨w=1 implies
  [f,g](w)=∨_{u⊠v≤w} (f(u)∧g(v))=1_M.
This is strictly richer in form than diagonal evaluation f=g=id and captures arbitrary compatible pairs of locale maps (in the sense of disjointness relation). 

Conversely, if that displayed equality holds for all such M,f,g, it implies d∨w=1: take M=↑d, the frame of the closed sublocale C(d), and f(a)=d∨(a⊠1), g(b)=d∨(1⊠b). Then f,g are frame homomorphisms, and if a∧b=0, their meet is d (bottom of M), because a⊠b≤d. The image of w is d∨w. So all compatible pairs CHARACTERIZE the bar hypothesis exactly.

This is a useful rigorous way to retain the full bar strength lost under ordinary diagonal trace. It does NOT yet prove the special interchange inequality (*) or a depth bound; taking M=↑d is the universal tautological witness. To make progress one must construct a SPECIFIC compatible two-map target M from a hypothetical bad good-open ideal G or from noncontinuous approximation data, and show [f,g](w)<1. Merely invoking all M,f,g restates the bar condition.
