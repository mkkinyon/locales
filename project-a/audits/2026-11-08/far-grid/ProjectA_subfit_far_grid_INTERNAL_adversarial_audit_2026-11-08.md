# Project A — Internal adversarial audit of the subfit far-grid counterexample

**8 November 2026 · INTERNAL ONLY — NOT FOR THE BLIND REFEREE**

## Verdict and scope

**PASS, conditional on external review for promotion to the master theorem ledger.** I independently rechecked the concrete topological and frame-theoretic argument in `ProjectA_subfit_far_grid_counterexample_working_2026-11-08.md`. I found **no fatal or major gap**. The counterexample is a frame of opens of a countable, second-countable \(T_1\) space, hence subfit; \(d_{\mathcal I}=d_{\mathcal U}\) as elements of the *actual frame coproduct*; a particular disjoint pair has no far grid. None of these conclusions uses the sobrification or an assumed spatial localic square.

This internal verdict does **not** imply external mathematical verification or novelty.

## 1. Independent topology test

There are four basic-open types:

- \(A_{i,F}=P_i\setminus F\), cofinite in the infinite \(P_i\);
- \(T_{i,t}=\{s_{i,t}\}\);
- \(R_{i,F,m}=\{r_i\}\cup A_{i,F}\cup S_{i,\ge m}\);
- \(N_n=\{q\}\cup\bigcup_{i\ge n} S_i\).

Every point belongs to a basic open. The nonobvious intersection identities are \(R_{i,F,m}\cap N_n=S_{i,\ge m}\) for \(i\ge n\), a union of singleton basics, and \(R_{i,F,m}\cap A_{i,G}=A_{i,F\cup G}\). Other within-block intersections are the same type with unioned finite exclusions or maximum tail index; distinct blocks are disjoint unless one member is an \(N_n\). Thus it **is** a basis, though not closed under intersections as a *set of individual basis elements*. This is a natural failure mode to test.

**T1 check (not merely T0):** Each \(s_{i,t}\) is isolated and its singleton is closed as well, because \(r_i\) has later-tail neighborhoods and \(q\) has \(N_{i+1}\); the remaining points have basics disjoint from that singleton. A point \(p_{i,k}\) is excluded from a neighborhood of \(r_i\) by including it in the finite exclusion set and from a neighborhood of any other point by the block structure; other cloud points use cofinite neighborhoods omitting it. An \(r_i\) is omitted by \(A_{i,F}\) at its cloud points, \(T\) at the \(s\)-points, and all \(N_n\) at \(q\). The point \(q\) occurs only in \(N\)-basics and can be omitted by basics at every other point. All singletons are closed. The elementary \(T_1\Rightarrow\mathcal O(X)\text{ subfit}\) argument with \(w=X\setminus\{x\}\) is exact.

## 2. Arbitrary-set closure test

Because each \(p_{i,k}\) has a cofinite neighborhood base in \(P_i\), it is in \(\overline E\) iff it is in \(E\) or \(E\cap P_i\) is infinite. Every \(s_{i,t}\) is isolated. At \(r_i\), neighborhoods consist of cofinite \(P_i\) and a sufficiently long \(S_i\)-tail, so **either** an infinite intersection of \(E\) with \(P_i\) **or** an infinite intersection with \(S_i\) forces adherence. Conversely if both intersections are finite, one finite exclusion and one sufficiently late tail miss them. At \(q\), every neighborhood contains all \(S_i\) for sufficiently large \(i\), so adherence means \(q\in E\) or \(E\) meets infinitely many distinct \(S_i\). These yield exactly (3.1).

Therefore \(\overline{A_{i,F}}=P_i\cup\{r_i\}\); \(\overline{T_{i,t}}=T_{i,t}\); \(\overline{R_{i,F,m}}=P_i\cup\{r_i\}\cup S_{i,\ge m}\); and \(\overline{N_n}=N_n\cup\{r_i:i\ge n\}\). Crucially, **no** \(q\) lies in the closures of a basic \(A\), \(T\), or \(R\); their intersection with only one \(S_i\) is not enough.

## 3. Exhaustiveness of the basis-pair table

There are \(\binom{4+1}{2}=10\) unordered type pairs. By taking intersections of the four displayed closures, one gets:

| Types | Disjoint exactly when | Far when disjoint? |
| --- | --- | --- |
| \(A_i,A_j\) | \(i\ne j\) (infinite cofinite sets intersect for \(i=j\)) | yes |
| \(A_i,T_{j,t}\) | always | yes |
| \(A_i,R_j\) | \(i\ne j\) | yes |
| \(A_i,N_n\) | always | **no iff \(i\ge n\)** |
| \(T_{i,t},T_{j,u}\) | unequal points | yes |
| \(T_{i,t},R_{j,m}\) | \(i\ne j\) or \(t<m\) | yes |
| \(T_{i,t},N_n\) | \(i<n\) | yes |
| \(R_i,R_j\) | \(i\ne j\) | yes |
| \(R_i,N_n\) | \(i<n\) | yes |
| \(N_n,N_m\) | never | vacuous |

The finite exclusions \(F,G\) cause **no additional disjointness** when the indices match: two cofinite subsets of the same infinite \(P_i\) always meet. This depends critically on \(P_i\) being infinite.

At the boundary \(i=n\), \(A_{i,F}\cap N_i=\varnothing\) but \(r_i\) belongs to both closures. The pairs \(T_{i,t},N_i\) and \(R_{i,F,m},N_i\) already intersect, as required.

## 4. Localic proof, no reliance on ordinary points of the square

Every exceptional \(A_{i,F},N_n\) with \(n\le i\) satisfies
\[
N_n=N_{i+1}\vee\bigvee_{j=n}^i\bigvee_{t\ge1}T_{j,t}.
\]
All right-hand terms are far from \(A_{i,F}\). Since \(u\boxtimes\bigvee v_t=\bigvee(u\boxtimes v_t)\) in \(L\oplus L\), each exceptional rectangle is below \(d_{\mathcal U}\), as is its transpose. Every disjoint pair \(u,v\) is a join of basic pairs disjoint across the grid; two more coordinatewise joins then give \(u\boxtimes v\le d_{\mathcal U}\). Thus \(d_{\mathcal I}\le d_{\mathcal U}\). Farness implies meet-zero, giving the reverse inequality. The equality is **in the coproduct** and therefore gives equality of closed sublocales \(C(d_{\mathcal I})=C(d_{\mathcal U})\).

In C-ideal language, the argument says the C-ideal generated by all far pairs contains every disjoint basic pair after one coordinatewise join, then contains each disjoint arbitrary pair after further coordinate joins. This is valid without assuming spatiality of \(X\times_{\mathrm{Loc}}X\).

## 5. Obstruction to arbitrary grids

Take \(a=\bigcup_iP_i\), \(b=N_1\). Both are open and disjoint. In any cover \(b=\bigvee b_\beta\), some \(b_{\beta_0}\) contains \(q\), hence \(N_n\subseteq b_{\beta_0}\) for some \(n\). Pick any \(i\ge n\). Since \(P_i\subseteq a=\bigvee a_\alpha\), some \(a_\alpha\) contains some \(p_{i,k}\); because it is open, it contains a **cofinite** subset of \(P_i\). Thus \(r_i\in\overline{a_\alpha}\) and \(r_i\in\overline{b_{\beta_0}}\). This contradicts \(a_\alpha^*\vee b_{\beta_0}^*=1\). No finite, countable, disjoint, basic or regularity restriction has been placed on the proposed refinements. The obstruction is genuinely universal.

**Important structural distinction:** all singleton cloud points are closed (T1), so the earlier proof's specialization relation \(r_i\in\overline{\{p_i\}}\) is absent. What survives is *nonempty open subsets* of the cofinite cloud having \(r_i\) in their closures.

## 6. Auxiliary claims and adversarial boundary checks

- **Not sober as the original T1 space.** \(F_i=P_i\cup\{r_i\}\) is closed (it is \(\overline{P_i}\)), irreducible because every nonempty open intersecting it has a cofinite trace on \(P_i\), and is not a point closure since the original space is T1. Correct.
- **Sobrification.** The frame \(\mathcal O(X^{\mathrm{sob}})\cong\mathcal O(X)\) is a standard fact; hence the exact frame and localic claims survive. Each \(B_i=P_i\cup S_i\cup\{r_i\}\) is clopen, as are the singletons \(T_{i,t}\). An irreducible closed set either lies in one block \(B_i\) or in \(\{q\}\), and inside a block either is an \(s\)-singleton or lies in \(F_i\). Within \(F_i\), closed irreducibles are the individual point closures and \(F_i\): every infinite subset of \(P_i\) is dense in \(F_i\), whereas every proper finite closed subset with at least two points is reducible in this T1 subspace. Hence precisely the countably many \(F_i\) are new. A countable base for the original space gives one for the soberification, since opens correspond under the canonical frame isomorphism.
- **Noncompact:** \(\{N_1\}\cup\{B_i:i\ge1\}\) covers \(X\) but no finite subfamily does, because \(p_{i,k},r_i\notin N_1\).
- **Not continuous:** For each \(n\), the directed \(D_F=N_{n+1}\cup F\), \(F\subseteq\bigcup_{j\le n}S_j\) finite, has union \(N_1\) but no member contains \(N_n\). So \(N_n\not\ll N_1\), and since every open containing \(q\) contains an \(N_n\), \(N_1\) cannot be the join of elements way-below it. Thus \(L\) is not continuous. An algebraic frame is continuous, and a coherent frame is compact, so neither class contains this \(L\).

No hidden use of sobriety or complete regularity was found. The proof does **not** produce a sober T1 counterexample, nor does it establish any stronger separation property.

## 7. Editorial corrections and limits

1. Spell out that \(A_{i,F}\) is a nonempty cofinite set; its intersection with any other cofinite cloud open is never empty. All ten case distinctions rely on this.
2. Explicitly distinguish the **T1 topological presentation** from the **sober locale** obtained by sobrification. They share the frame, but the soberification is generally not T1.
3. The proof of the main result does **not** need the auxiliary assertion that the soberification has only countably many new points. That assertion is correct but should not be overemphasized.
4. The external audit should independently check the topological closure criteria and the large-quantifier grid obstruction, as well as the 10-row list.
5. The claim is mathematical, not bibliographic: no literature-priority/novelty conclusion follows from the present review.

## 8. Disposition

**Internally accepted as a working counterexample; external blind audit pending.** If an independent referee confirms it, record that the subfit far-grid converse is false, with the stronger fact that there is a countable, second-countable T1 topological presentation. Do not reopen an escalating sequence of stronger assumptions merely because this counterexample exists; select the next Project A problem deliberately after external verification.