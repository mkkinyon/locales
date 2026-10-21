# Project A — Ordered-spectral description of U, Hochster dual, and I/D lattice operations

21 October 2026. Working proofs; standard Priestley theory used. Separate point relations from sublocale statements.

## Priestley description

Let X be spectral, with specialization x≤y iff x∈cl{y}; its compact Hausdorff patch topology and closed specialization order form a Priestley space. Compact-open sets of X are exactly patch-clopen upsets.

Lemma: for a compact-open K, cl_X(K)=down(K). Proof: down(K) is compact/patch closed as projection of the closed specialization relation intersected with X×K. It is a downset, hence closed for the spectral topology by Priestley separation. Any X-closed containing K must contain down(K).

Consequently, x not U_X y iff there exist patch-clopen upsets K,H containing x,y with down(K)∩down(H)=empty. Equivalently, x U_X y iff each such pair of neighborhoods contains points admitting a common lower specialization. For X^vee, reverse the order and interchange clopen upsets and downsets: x U_(X^vee) y iff every pair of clopen downsets K,H containing x,y has up(K)∩up(H) nonempty.

For comparison x I_X y iff x,y have a common upper specialization (patch-compactness argument), and x D_X y iff x,y have a common lower specialization. These point formulas exchange I and D under Hochster duality, but do not generally identify U_X with U_(X^vee).

## Five-point finite counterexample to U self-duality and U=I join D

Take upper-set topology of the five-point poset with strict relations 0<4, 2<4, 2<3, 1<3, and no others. Every nonempty upper set contains 3 or 4, whose downclosures meet at 2. Thus any two nonempty opens have intersecting closures; U_X is the full relation X×X.

However 0 and 1 have neither a common upper bound (up(0)={0,4}, up(1)={1,3}), nor a common lower bound (down(0)={0}, down(1)={1}). So (0,1) is in neither I_X nor D_X. For finite Alexandrov spaces, localic I and D are determined by ordinary points and their join is the union of the underlying subsets; hence I∨D is properly contained in U in this example.

In the Hochster dual poset, upsets correspond to original downsets. The dual-open singleton neighborhoods {0} and {1} have disjoint closures up_X({0})={0,4}, up_X({1})={1,3}. Thus (0,1) is not U_(X^vee), so U_X != U_(X^vee). This shows only noninvariance of U, not failure of the equality-properties duality.

The intersection I∧D need not equal the diagonal either: in the four-element diamond poset 0<a,b<t, the incomparable pair a,b admits both a common upper t and a common lower 0, so it belongs to I∩D beyond Δ.

## Research agenda

Study the localic meet I∧D (intersection of closed I with fitted D) and join I∨D (join of sublocales) beyond finite spatial examples. Both lie beneath U, but neither I∨D=U nor I∧D=Δ is universal. Potentially examine closure/fitted hull and relation compositions; avoid asserting that joins of arbitrary sublocales coincide with union of point sets. Explore how the finite spectral obstructions extend to coherent frames and whether the ordered patch characterization has direct locale-theoretic translation.

Novelty not verified: Priestley characterization is immediate from standard ordered spectral theory and project's U definition.
