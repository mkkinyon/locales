# Universal depth-three: canonical polarity reduction and gap

Date 22 Oct 2026. NO proof of universal (*) or counterexample.

Let L be a frame, T=L⊕L, w∈T an open with d∨w=1. Define the antitone polar r_w:L^op→L by
  r_w(b)=∨{u∈L:u⊠b≤w}.
Because tensor rectangles preserve arbitrary joins in each variable, u⊠b≤w iff u≤r_w(b), and
  r_w(∨_i b_i)=∧_i r_w(b_i).
This is a complete Galois polarity: u≤r_w(b) iff b≤r_w^op(u), with r_w^op(u)=∨{v:u⊠v≤w}.

For the disjointness open d=∨_{u∧v=0}u⊠v,
  r_d(b)=b*.
Indeed if u⊠b≤d then applying the diagonal frame map μ:T→L gives u∧b=0, hence u≤b*. Conversely u≤b* implies u⊠b≤d.

For the canonical rectangular bar B_w, a horizontal leaf cover at fixed b exists exactly when
  a≤h_w(b):=b*∨r_w(b).
This follows by separate-join closure: the D leaves with fixed second coordinate b have first-coordinate join b*, and the w leaves have join r_w(b).

Define k_w(a)=∨{b:a≤b*∨r_w(b)}. A depth-three H-V-H certificate exists exactly when ∨{a:k_w(a)=1}=1.

Important polarity distinction:
  r_{d∨w}(b)=r_1(b)=1
but r_d(b)∨r_w(b)=b*∨r_w(b) need not be 1; rectangle right-adjoint r_- does NOT preserve binary join in the open parameter. The bar hypothesis d∨w=1 is thus a statement about a join of tensor opens that need not split uniformly at each fiber. The universal depth-three question asks whether a two-step spatial/frame cover repairs this uniformity defect everywhere.

Counterexample reduction: If ∨{a:k_w(a)=1}<1, symmetric meet s=w∧τ(w) also is a bar and its canonical leaf family is contained in B_w. Hence its H-V-H criterion fails as well; since s is symmetric, so does V-H-V. Universal H-V-H and unrestricted universal depth≤3 are therefore equivalent **for canonical bars**. This does not prove either.

Necessary diagonal consequence d∨w=1⇒∨{u∧v:u⊠v≤w}=1 (apply μ). It is weaker than any obvious fiberwise equation, and r_w's join-to-meet law does not overcome this gap.

Potential next: find a structural theorem classifying the possible complete polarities r_w arising from opens in L⊕L, then test whether covering d∨w=1 implies the depth-three covering identity. Do not claim universal depth three yet.
