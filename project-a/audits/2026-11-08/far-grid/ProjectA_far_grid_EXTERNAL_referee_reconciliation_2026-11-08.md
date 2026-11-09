# Project A — Reconciliation of the blind referee report on the far-grid converse

**8 November 2026 | Post-referee assessment | Scope: the specific construction and its consequences**

## Disposition

**ACCEPT the central counterexample as externally verified.** The independent blind referee reconstructed the candidate topology, all ten types of basic-open pairs, the frame-coproduct calculation of \(d_{\mathcal I}=d_{\mathcal U}\), the universal failure of far-grid decompositions for a specified disjoint pair, and sobriety. Our internal audit had reached the same verdict. No fatal or major error was identified. This is a verdict about the definitions stated in the candidate packet; novelty and literature priority were not examined.

**Precise verified result.** There is a countable, second-countable, sober \(T_0\) space \(X\) such that \(L=\mathcal O(X)\) satisfies \(\mathcal I(L)=\mathcal U(L)\) as closed sublocales of \(\operatorname{Loc}(L)^2\), but there are disjoint opens \(a,b\) for which no decompositions \(a=\bigvee_\alpha a_\alpha\), \(b=\bigvee_\beta b_\beta\) have \(a_\alpha^*\vee b_\beta^*=1\) for all \(\alpha,\beta\).

## Construction and the decisive calculation

Let \(X=\{q\}\sqcup\{p_i,r_i:i\ge1\}\sqcup\{s_{i,m}:i,m\ge1\}\), and \(S_i=\{s_{i,m}:m\ge1\}\). Basic opens are \(P_i=\{p_i\}\), \(T_{i,m}=\{s_{i,m}\}\), \(R_{i,m}=\{r_i,p_i\}\cup\{s_{i,t}:t\ge m\}\) and \(N_n=\{q\}\cup\bigcup_{i\ge n}S_i\).

Their closures are \(\overline{P_i}=P_i\cup\{r_i\}\), \(\overline{T_{i,m}}=T_{i,m}\), \(\overline{R_{i,m}}=R_{i,m}\), and \(\overline{N_n}=N_n\cup\{r_i:i\ge n\}\). In the ten exhaustive unordered types of basic-open pairs, the only disjoint pairs that are *not far* are \((P_i,N_n)\) with \(i\ge n\), and transposes.

For such a pair,
\[
N_n=N_{i+1}\vee\bigvee_{j=n}^{i}\bigvee_{t\ge1}T_{j,t},
\]
and every summand on the right is far from \(P_i\). Consequently \(P_i\boxtimes N_n\le d_{\mathcal U}\) in the *actual frame coproduct* \(L\oplus L\). Expanding arbitrary disjoint opens into basic opens, and using preservation of joins in the two coordinates, gives \(d_{\mathcal I}\le d_{\mathcal U}\). The opposite inequality holds universally. Thus \(\mathcal I=\mathcal U\) as *localic* closed relations; no appeal to ordinary points of the localic square is made.

Take \(a=\bigcup_iP_i\) and \(b=N_1\). In any decomposition of \(b\), a piece containing \(q\) contains some \(N_n\), and hence has \(r_i\) in its closure for every \(i\ge n\). Any decomposition of \(a\) has a piece containing \(p_i\), whose closure contains \(r_i\). These two pieces cannot be far. The argument applies to arbitrarily indexed, overlapping or transfinite families of opens.

## New checks supplied by the referee, accepted

1. **Topology and sobriety.** Pairwise intersections of the given basics are unions of basics; in particular \(R_{i,m}\cap N_n\) is a tail of the isolated \(s_{i,t}\), *not* generally one basic open. The blocks \(B_i=R_{i,1}\) are clopen, and their irreducible closed subspaces are the closures of single points; the residual point is \(q\). \(T_0\) ensures unique generic points. Thus \(X\) is sober. The countable displayed basis makes it second-countable.
2. **No compact neighborhood of \(q\).** The referee checked the two cases depending on whether a neighborhood contains infinitely many \(r_i\). Noncompactness and non-local-compactness follow. A direct directed-family argument also shows \(\mathcal O(X)\) is not a continuous frame.
3. **Neither algebraic nor coherent.** No compact open contains \(q\), so the frame is not algebraic; \(X\) itself is not compact, so its frame is not coherent. The referee provided independent arguments.
4. **Not subfit.** For \(u=P_i\), \(v=0\), any open \(w\) satisfying \(u\vee w=1\) contains \(r_i\), hence contains \(P_i\), and therefore is all of \(X\). The subfitness separation test fails. In particular the example is neither fit nor regular; it is also not \(T_1\). This limits what the counterexample settles.
5. **The infinite tails really matter.** In the proposed collapsed one-point-per-block variant, the disjoint atomic opens \(\{p_i\}\) and \(\{s_i\}\) have intersecting closures and no possible far refinement; already \(\mathcal I=\mathcal U\) fails. This is a useful diagnostic, not a minimality theorem.

## Minor corrections and precision points

- **Join-stage count.** The report's introductory phrase that the *specific witness* \((a,N_1)\) needs “three alternating join closures (coordinate 2, then 2, then 1)” should be read with care. It is actually obtained from the far pairs with one second-coordinate join for each \((P_i,N_1)\), followed by a first-coordinate join over \(i\): **two successive join stages**. A general disjoint pair may require the preliminary exceptional-basic-pair stage plus the two basis-expansion stages, which explains the number three in the full proof. The main theorem is unaffected.
- **Scope of previously known positive results.** Our 20 October notes prove the far-grid criterion *sufficient* for \(\mathcal I=\mathcal U\), and mention positive converses in particular continuous/algebraic constructions. The available material does **not** certify a theorem that *every* coherent, continuous, or algebraic frame satisfying \(\mathcal I=\mathcal U\) has far grids. The referee expressly did not verify any such blanket converse. Do not mark these class-restricted questions closed.
- **Generalization caveat.** The non-subfit feature is intrinsic to **this** counterexample. It is not evidence that a subfit or \(T_1\) counterexample is impossible.
- **Presentation improvements.** In a canonical proof, add an explicit basis-axiom check and the pointwise closure criterion, explain why \(\operatorname{cl}\Delta=C(d_{\mathcal I})\), and state sobriety/non-local-compactness precisely. The referee identified no needed mathematical repair to the central proof.

## Research suggestions: not promoted to theorems

The referee suggests testing the converse for subfit/\(T_1\) frames, an intermediate “local far-grid” property, alternation depth of C-ideal derivations, and other C-ideal certificates. The observations about this particular example are valid, but broader claims were **not** checked. The user has asked for concrete, bounded problems and specifically wishes to avoid a prolonged hierarchy of renamed variants; we should not automatically begin an alternation-rank program.

The far-grid question is now **closed negatively in the unrestricted class**. The mathematical follow-up, if chosen, could be a *separate sharp question*: is the far-grid converse valid for subfit frames? Another independent direction is whether the far-grid property imposes additional identities on the named relations beyond \(\mathcal I=\mathcal U\); no such extra identity is established by this audit.

## Provenance and disposition

Original candidate: `ProjectA_far_grid_EXTERNAL_BLIND_packet_2026-11-08.md`; original independent blind report: `Referee report — far-grid converse counterexample.md`; internal audit: `ProjectA_far_grid_INTERNAL_adversarial_audit_2026-11-08.md`. The original referee report and blind packet are not modified. No claim of novelty or external literature priority is made. The **specific far-grid counterexample** merits status **E** (externally verified) in the next ledger revision. Other research suggestions retain open/unchecked status. No repository write was performed during this reconciliation.