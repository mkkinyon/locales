# Project A — Assessment of external referee's response to criticisms

24 October 2026. Claude's follow-up is archived verbatim in [A-WU-external-referee-followup-response-2026-10-24.md](A-WU-external-referee-followup-response-2026-10-24.md). The analysis below is our independent reconciliation; it is not part of the referee's report.

**Verdict:** The repaired pure-rectangle lemma, cover-reduction lemmas and global hyperconnected-strip localization have been checked in detail and appear correct. The earlier two errors are conceded. The follow-up contains one minor erroneous sample computation for the six-point zigzag, described below, which does not affect its theorem.

## 1. Accepted rectangle lemma and preservation

Write Q=L⊕L, d_U the join of far rectangles, and Phi,Phi2 the all-cover and finite-cover pre-nuclei already defined in the audited WU notes. For a nonzero hyperconnected element a, define

    e_a=⋁{q∈L: a*∨q*=1}.

The referee's repaired identity is correct:

    d_U∧(a⊠1)=a⊠e_a,       e_a≤a*,

and for every 0<u≤a, u⊠v≤d_U iff v≤e_a. Proof: for each far rectangle p⊠q meeting a⊠1 nontrivially, hyperconnectedness gives (p∧a)*=a*, so q is one of the joinands of e_a. The reverse inequality is by the generators of d_U; injectivity of nonzero pure rectangles establishes the iff. Crucially e_a is not required to be far from a.

Call an element d∈Q strip-constant (H) if for every hyperconnected a there exists e with d∧(a⊠1)=a⊠e. The referee proves (H) is stable under joins and Phi2. The main step is sound: if a'=a∧p≠0 and p⊠q≤w_F→d for a finite cover F, partition F according to c∧a'≠0. Hyperconnectedness forces all remaining c to miss a itself, and on the first part d's strip-constancy upgrades inequalities on a'⊠q to a⊠q. A binary cover witnesses a⊠q≤Phi2(d). Hence the entire Phi2(d) restriction to a⊠1 is a pure rectangle. Starting at d_U and iterating yields (H) for d_W2.

**Cover reduction lemma (verified):** If d0 has (H) and is Phi2-fixed, d≥d0, and d,d0 agree on all hyperconnected strips, then Phi(d),d0 also agree on all such strips. The proof partitions an ARBITRARY cover C into c1=join{c:c∧a'≠0} and c2=join{c:c∧a'=0}, for a' nonzero below a. The binary neighborhood v(c1,c2) fixes d0, and the rectangle-divisibility argument yields a'⊠q≤d0 for each generator of Phi(d) on the strip. This correctly handles the infinite join where the original referee's argument failed.

## 2. Accepted universal localization theorem

Set h_L=join of all nonzero hyperconnected a∈L and o=h_L⊠1∨1⊠h_L. Starting from d_W2 (Phi2-fixed, strip-constant), transfinite iteration of Phi preserves equality of the hyperconnected-strip restrictions by the cover-reduction lemma. Its stable value is d_W. Coordinate symmetry gives

    d_W∧o=d_W2∧o,

equivalently

    W∩O(o)=W2∩O(o).

Thus any difference between W and W2 is confined to C(o)=C(h_L)×C(h_L). In particular, if h_L=1, then W=W2 universally, proving Q' and hence Q for this genuinely noncompact class.

This statement is about the CLOSED HULLS; it does not say D=D2. The earlier Scott/Cantor example demonstrates that distinction. A prospective failure of Q would have to occur simultaneously in the nonregular boundary G=U∧O(d_U**) and C(h_L)×C(h_L). Treat the localization as a new externally proposed result verified internally but not yet audited by a *second* independent agent.


## 3. Correction to example list: the six-point zigzag has TWO excluded points

For the six-point upper-Alexandrov poset P with relations

    0<5>1<4>2<3,

the nonempty hyperconnected open subsets are exactly {5}, {4}, {3}, and {0,5}; their union is h_P={0,3,4,5}. Therefore

    C(h_P) has ordinary point set {1,2},

NOT {1}, as the referee claims near the end of §2.3. At 1 the minimal open ↑1={1,4,5} contains disjoint open sets {4},{5}; at 2 the minimal open ↑2={2,3,4} contains disjoint {3},{4}; neither point admits a hyperconnected open neighborhood. Conversely ↑0={0,5}, ↑3={3}, ↑4={4}, ↑5={5} are hyperconnected.

For S×P (S the nonempty-powerset Scott space), the hyperconnected-coordinate locus is S×h_P, so the closed complement has ordinary point set S×{1,2}, not S×{1}. This is an example computation only; the general localization theorem is unaffected.

## 4. Boundary-local atomic corollary: why it is plausible

The final suggested improvement says that Q holds if the Booleanization of H=G∩C(o) is atomic. A direct justification is available and should accompany the statement. Suppose W2=U yet W<U. Since K=cl(int U)≤W and W,W2 agree on the open O(o), choose a nonzero relatively OPEN part E of U disjoint from D and contained in G∩C(o). (For example the U-open complement of W, which is a nonzero open sublocale of U, lies in both G and C(o).) As W2=U, D2∩E is dense in E. But D2 and D have the same ordinary points (for arbitrary locales), and D∩E=0. If B(O(H)) is atomic, every nonzero open sublocale E of H has atomic/spatial Booleanization; hence a dense D2∩E contains a point, contradiction. Thus the suggested corollary is supportable, but the proof must use the OPEN defect region E, rather than assume density restricts to the CLOSED sublocale H (which is generally false).

## 5. Research disposition

The main new theorem is worth recording as a genuine advance: a restriction on which parts of a locale can support differences W<W2, and an unrestricted positive theorem Q' for hyperconnected-open-covered frames. The six-point worked example needs correction but does not undermine any proof. It remains open whether Q' or Q holds for every locale. In subsequent work, the right territory is the simultaneous intersection of the nonregular Urysohn sector and the square of the closed complement of the hyperconnected-open locus. Avoid treating the repaired theorem as a universal proof of Q.
