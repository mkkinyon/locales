# Locally compact one-stage residual gives universal FOUR-step separation
Date: 22 October 2026
Status: new theorem, elementary localic-sound proof in Hausdorff spatial locales.

Let X be Hausdorff, L=O(X), B⊆L×L a lower rectangular family with DIAGONAL COVER
  1=∨_{(u,v)∈B}u∧v.
(This is automatically true for any rectangular bar since diagonal Δ* annihilates d_I.)
Let D={(u,v):u∧v=0}, S=D∪B.
Define h_S(b)=∨{u:(u,b)∈S} and t_H=∨{b:h_S(b)=1}. Put F_H=X\t_H (closed).

LOCAL COMPACT SUPPORT LEMMA. Let o∈L be any open for which o∩F_H is contained in a COMPACT subset K⊆F_H. Then
   (1,o)∈H(V(H(S))).
Proof: For each x∈X choose diagonal B leaf (u_x,v_x) with x∈u_x∩v_x. K\v_x is compact, disjoint from x. Hausdorff point/compact separation gives opens U_x∋x, W_x⊇K\v_x with U_x∩W_x=∅. Put a_x=u_x∩U_x. Then a_x covers x; (a_x,v_x)∈B, (a_x,W_x)∈D. Also (1,t_H)∈V(H(S)) because t_H is the vertical join of b's with (1,b)∈H(S). Thus (a_x,o∧t_H)∈V(H(S)), while (a_x,o∧v_x) and (a_x,o∧W_x) belong already to S⊆V(H(S)). The second opens o∧t_H, o∧v_x, o∧W_x cover o: outside F_H, t_H covers o; on F_H∩o⊆K, v_x∨W_x covers K. So (a_x,o)∈V(H(S)). As the a_x cover X, (1,o)∈H(V(H(S))). QED.

MAIN THEOREM. If F_H is LOCALLY COMPACT as subspace of X, then
 (1,1)∈V(H(V(H(S)))).
Indeed for every y∈F_H choose an F_H-open neighborhood with compact closure K_y⊆F_H and lift to an ambient open o_y with y∈o_y and o_y∩F_H⊆K_y. Then local compact support lemma gives (1,o_y)∈H(V(H(S))). Also (1,t_H)∈V(H(S))⊆H(V(H(S))). The o_y's together with t_H cover X. One final vertical root join gives (1,1)∈V(H(V(H(S)))), orientation V-H-V-H, depth FOUR.

DUAL. Define t_V=∨{a:(a,1)∈V(S)}, F_V=X\t_V. If F_V locally compact, then (1,1)∈H(V(H(V(S)))), orientation H-V-H-V, depth≤4.

COROLLARY FOR NONREGULAR LOCUS. Every point of regularity belongs to BOTH t_H and t_V: for a diagonal bar leaf (u,v) at y, regular shrink b with cl b⊆u∩v yields (1,b)∈H(S) and (b,1)∈V(S). Thus F_H,F_V are CLOSED SUBSETS of the nonregular point locus N⊆X. If N is locally compact as a subspace (not necessarily closed, compact, or countably compact), then F_H and F_V, being relatively closed subsets of N, are locally compact. Hence every rectangular bar on X has both orientations of depth≤4.

SHARP OBSTRUCTION. If a Hausdorff rectangular bar requires depth≥5, then BOTH closed first-step residuals F_H,F_V have at least one point at which they are NOT locally compact. Moreover even if F_H not globally locally compact, the open locus of locally compact points of F_H, together with t_H, lies inside the third-stage second-coordinate cover t_3^V=∨{o:(1,o)∈H(V(H(S)))}. Thus any failure of V-H-V-H root must be concentrated over the closed nonlocally compact kernel of F_H (relative to F_H).

NO CLAIM of actual rank4 witness; the theorem is an upper bound. It is stronger than rank≤3 compact-residual result only in coverage (works for noncompact locally compact residual), though weaker in bound. It uses only diagonal cover, so provides localic barhood rather than presupposing it.

GENERALIZATION to initial κ-compact local residual and bound on character: if X Hausdorff of point-character ≤κ and F_H locally initially-κ-compact in the sense that each y has a relatively open F_H-neighborhood contained in an initially κ-compact K_y⊆F_H, the same proof works because a first-coordinate point x can be separated by disjoint opens from the closed initially κ-compact K_y\v_x, using the standard neighborhood-base / FIP lemma recorded in A-V-compact-exceptional-nonregular-locus-depth-three-2026-10-22.md. In first-countable X, 'locally countably compact' suffices. These are sufficient conditions only.

LIMITATION. This is not a universal depth-three theorem for arbitrary locally compact exceptional loci. Whether the 4-level bound is sharp, and whether any bar has orientation-rigid rank3, remain open.

NECESSARY MATHEMATICAL DETAIL: The rectangle (a_x,o∧t_H) belongs to V(H(S)) by downward closure from (1,t_H); it need NOT belong to H(S) directly. This is why the local support lemma yields a three-stage H-V-H certificate and the global theorem requires an extra vertical root stage.
