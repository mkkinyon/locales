# Locally compact boundary principle for localic-square bar covers
Date 22 October 2026.

THEOREM (pointwise-to-localic bar reflection across a locally compact boundary). Let X be a sober spatial locale, e∈L=O(X), and Z=C(e) the corresponding closed sublocale. Assume Z is locally compact (hence spatial and with localic products Z×locX and X×locZ spatial; the embedding of sober spaces into locales preserves binary products if one factor is locally compact, cf. Isbell 1981). Let d∈Q=L⊕L be any open (in applications d=d_I) and let w∈Q be another open. Suppose:
(A) e⊠e≤d∨w in Q;
(B) every ordinary point (x,y)∈X×topX lies in the pointwise open d∨w.
Then d∨w=1 in Q.

Proof: Put E=C(d∨w), closed sublocale of the localic square Q. By (A), E≤C(e⊠e). Closed-subspace calculation gives
  C(e⊠e)=C(e⊠1)∨C(1⊠e)=(Z×locX)∨(X×locZ).
Both factors on right are spatial as Z is locally compact sober and X spatial sober (product of a locally compact sober space with a sober space is spatial). The finite join of spatial sublocales is spatial: if A,B are spatial sublocales with nuclei j_A,j_B on Q, the nucleus of A∨B is pointwise meet j_A∧j_B, so the frame of A∨B embeds in O(A)×O(B) via both restriction maps; this gives sufficient points. Therefore C(e⊠e) is spatial. The closed sublocale E of it is spatial as well. By (B), E has no points, since points of the localic square are exactly pairs of points of X. Thus E=0, i.e., d∨w=1.

COROLLARY (graph-null criterion). Suppose X is sober, e=L_0∨R_0 consists of disjoint open components containing the two projections of a relation γ:Y→X×locX, and the graph-null open q is the largest γ*-annihilated open. Suppose e⊠e≤d_I∨q (true for the forward rational graph with left/right first/second coordinates as in our established proof), and every pair of X×topX outside the ordinary graph image has a rectangular neighborhood annihilated by γ*, while every point of the graph image is separated by disjoint opens of X. Then q∨d_I=1 provided Z=C(e) is locally compact. In particular one may replace discrete Z by a compact Hausdorff convergent-sequence space or Cantor space, IF the ordinary pointwise/closedness conditions are actually verified for the constructed X and relation.

IMPORTANT LIMITATION: Just declaring a nested bridge boundary Z compact does NOT ensure graph closedness or Hausdorffness of X. If the bridge attachment limits range densely over every rational interval while z_n→z_∞, each neighborhood of z_∞ may meet all rational intervals, obstructing Hausdorff separation from rational-copy points and causing new graph closure at mixed pairs. The localic lemma removes the original closed-discreteness assumption on the BOUNDARY PROOF, not the need to check ordinary graph closure and topological compatibility.

REFERENCE: Encyclopedia of Mathematics, 'Locale', notes preservation of spatial products if one sober factor locally compact; Isbell 'Product spaces in locales', Proc. Amer. Math. Soc. 81 (1981), 116–118.

This gives a new rigorous route to iterated-bridge rank tests with compact nondiscrete boundary, but it does not prove rank≥4 or universal depth three.
