# Project A — Internal adversarial audit of the post-\(\mathcal V\) work

**24 October 2026. FOR INTERNAL USE. DO NOT SEND TO THE BLIND AUDITOR.**  
**Sources examined:** the October 24 repository notes on \(\mathcal H\), the upper/lower diamonds, the formal hull and ordinal examples; the October 21 focused three-claims verification; the October 23 almost-normal thickening and focused internal audit; and the standalone compact three-boundary-point note. We also checked the relevant standard spatial/scattered-sublocale theorem against Suarez (2022) and Ball–Picado–Pultr (2016).

## Executive assessment

**No decisive counterexample to the principal NEW calculations was found in this audit.** The elementary upper- and lower-diamond examples are especially persuasive. The central coherent Priestley theorem and the exact transfinite \(\omega+m\) stage computation remain the most valuable claims requiring genuinely independent expert examination. A number of proofs have been reorganized to make the point-set/localic distinctions explicit; *internally checked* must not be upgraded to *externally verified*.

Do **not** conflate four degrees of confidence:

1. **Old independent input:** the coherent identities \(\mathcal U=\operatorname{cl}(\mathcal D)=\mathcal I^2\), \(\mathcal V=\operatorname{fit}(\mathcal I)=\mathcal D^2\) and the compact strict \(\operatorname{cl}(\mathcal D)<\mathcal U\) example were the subject of earlier independent/referee reconciliation.
2. **Elementary new formal identities:** \(\mathcal W\vee\mathcal V\le\mathcal H\), \(T(\mathcal J)=\mathcal W\wedge\mathcal V\), the two comparable-side criteria, and the monotone deflationary \(\kappa\)-recursion are strongly supported by direct frame manipulations.
3. **New concrete examples:** the Priestley two rays and the compact three-boundary-point space have clean defining data and point-pair witnesses, but sublocale equalities rely on specific nontrivial representation theorems.
4. **Big conceptual claims:** the general coherent \(\mathcal H/\mathcal F\) graph-closure description, \(\mathcal H\) transitivity iff \(\mathcal F\), and exact \(\omega+m\) first stabilization have not yet passed an independent audit.

## Audit A — Formal lattice identities

### A1. \(\mathcal W\vee\mathcal V\le\mathcal H\)

Proof: every closed fitted sublocale containing \(\Delta\) contains \(\mathcal D=\operatorname{fit}\Delta\) then \(\mathcal W=\operatorname{cl}\mathcal D\), and contains \(\mathcal I=\operatorname{cl}\Delta\) then \(\mathcal V=\operatorname{fit}\mathcal I\). **Pass.** It does *not* imply \(\mathcal U\vee\mathcal V\le\mathcal H\) absent \(\mathcal W=\mathcal U\).

### A2. Lower-diamond equality criteria

\(T(\mathcal J)=\mathcal W\wedge\mathcal V\). If \(\mathcal V\le\mathcal U\), the right-hand meet \(\mathcal U\wedge\mathcal V\) equals \(\mathcal V\), hence equality iff \(\mathcal V\le\mathcal W\), or \(\operatorname{cl}\mathcal V=\mathcal W\) since \(\mathcal W\le\operatorname{cl}\mathcal V\). If \(\mathcal U\le\mathcal V\), then \(\mathcal W\le\mathcal U\le\mathcal V\), so equality iff \(\mathcal W=\mathcal U\). **Pass.** These are valuable exact reductions, but conditional upon a known comparison between \(\mathcal U\) and \(\mathcal V\).

### A3. The \(\kappa\) construction

\(\operatorname{Fix}_a\) is the fixed-point frame of the intersection of the open sublocales \(O(w)\) with \(a\vee w=1\), because a join of nuclei has precisely the common fixed points. The bottom of that frame is \(\kappa(a)\), and the closed hull of a sublocale whose frame-bottom is \(k\) is \(C(k)\). The order calculations give monotonicity \(a\le b\Rightarrow\kappa(a)\le\kappa(b)\), deflationarity \(\kappa(a)\le a\), and fixedness iff \(C(a)\) fitted. Transfinite descending iteration from \(d_{\mathcal I}\) reaches the largest fixed point below it, yielding the minimal closed fitted hull. **Pass subject to standard nucleus lattice facts.**

**Important caution:** At a limit ordinal, \(C(\bigwedge a_\beta)\) is the *closure* of the ordinary sublocale join \(\bigvee C(a_\beta)\). Arbitrary joins of closed sublocales need not themselves be closed. This cannot be silently replaced with the bare join.

## Audit B — Coherent Priestley graph calculation

### B1. The patch-closed-upset fittedness lemma

For coherent/spectral \(Z\), let \(S\subseteq P_{\rm patch}\) be patch-closed and an upward specialization set. For each point \(p\notin S\), compact Priestley separation yields a **compact-open upset** containing all of \(S\) while excluding \(p\). The compact opens containing \(S\) form a filter, whose intersection of open sublocales is a coherent/spatial sublocale via the compact-open quotient congruence. Its point set is \(S\). If \(S\) is also spectral-closed (patch-closed downset), its closed sublocale has the same points and coincides with it. This is the precise point-to-sublocale bridge on which the coherent \(\mathcal H\) theorem rests.

**Assessment: plausible, strongly supported, but HIGH-PRIORITY EXTERNAL CHECK.** The existence, compact-open cofinality, and the quotient's coherence/spatiality must be established rather than assuming arbitrary fitted sublocales of a spectral space are spatial. The latter blanket statement is false as a general proof strategy.

### B2. The general coherent descriptions of \(\mathcal H\) and \(\mathcal F\)

Once B1 is established: closed fitted relations correspond to patch-closed sets saturated in both directions of the product specialization order. Thus minimality gives the asserted \(\mathcal H\) point set. For \(\mathcal F\), a real map is exactly a patch-continuous map constant on comparable points; a patch-closed equivalence relation on compact Hausdorff patch \(P\) gives a compact Hausdorff quotient and real functions separating distinct classes. **The argument is structurally sound.** One must still justify that coherent product points form the ordinary product and that closed sublocales are determined by point sets.

**Transitivity corollary:** if \(\mathcal H\) is an internal equivalence relation, its point set is a patch-closed equivalence relation containing finite comparability paths; hence it contains \(\mathcal F\)'s point set, giving \(\mathcal H=\mathcal F\) because both are closed. Reverse direction clear. **Pass conditional on B1/B2.** No unwarranted assertion that pointwise transitivity implies internal transitivity is made; we use internal transitivity only to imply pointwise transitivity.

### B3. Two-ray Priestley construction

Order: every even ray vertex minimal and every odd vertex maximal; adjacent comparabilities only. The order relation is patch-closed, since the only limit of unbounded comparable pairs is \((t,t)\). Priestley clopen-upset separation works via finite principal upsets (ray vertices) and complements of finite principal downsets (\(t\)). The relation \(R=(A\cup\{t\})^2\cup(B\cup\{t\})^2\) is patch closed, upward/downward saturated, and spectral-closed because its complement is the spectral-open cross-ray union. B1 then proves \(R\) fitted. Closedness of \(\mathcal H\) and patch limits of \(A^2,B^2\) force all of \(R\), so \(\mathcal H=R\). The ordinary triple \((a_0,t,b_0)\) witnesses **internal** nontransitivity, since its endpoint image lies outside the closed relation.

All continuous reals are constant along each ray, then at the common patch limit, giving \(\mathcal F\) full. Coherent \(\mathcal U,\mathcal V\) point sets stay within the three comparability blocks. Their union is compact patch-closed; a compact-open upset containing this union and omitting \((a_0,t)\) yields a **genuine** sublocale strictness certificate. **Pass conditional on B1.**

### B4. Ordinal stages \(\omega+m\)

The finite-stage algebra \(S_{n+1}=\downarrow\uparrow S_n=\mathcal I\circ S_n\circ\mathcal I\) gives \(S_n=\mathcal I^{2n+1}\). At \(\omega\) the increasing union is the finite-path comparability equivalence and the new closed stage is its patch closure plus down-saturation. For the proposed infinite zigzag \(A\) converging to \(t_0\) of a finite alternating handle \(T=\{t_0,\dots,t_{2m}\}\), the limit introduces exactly \(A\times\{t_0\}\) and its transpose; the handle's \(\mathcal I\)-neighbors then expand two steps per successor. I separately enumerated the finite handle's common-upper neighborhoods for \(m=1,\dots,5\); the displayed expansion \(T_k\to T_{k+1}\) matches the formulas. **Pass conditionally; HIGH-PRIORITY EXTERNAL CHECK** of the Priestley representation and closure at \(\omega\), not just a finite graph simulation.

**Terminology:** \(\omega+m\) is the first stable stage of the *specified closed-stage schedule* \(c\circ f\) starting at \(\mathcal I\). This is not a schedule-independent closure ordinal.

## Audit C — The compact \(T_1\) upper-diamond example

The earlier three-limit-point space has the inseparability path \(\alpha-\beta-\gamma\). In a locally compact sober scattered \(T_1\) space with scattered spatial localic square, the rank-two bar missing a chosen **separable** pair and point-determination of every sublocale give \(\mathcal V=\mathcal I\). In a \(T_1\) space, the common-predecessor criterion makes \(\mathcal D\) diagonal on ordinary points, giving \(\mathcal D=\Delta\) under total spatiality. Therefore \(\mathcal W=\mathcal H=\mathcal I\). The Urysohn edge between \(\alpha,\gamma\) is supported by their neighborhoods' closures meeting at \(\beta\), whereas they have disjoint neighborhoods themselves. Every real function is constant across this 3-point path, and clopen isolated sheets separate other points: \(\mathcal U=\mathcal F\). **Pass subject to the standard scattered-sublocale theorem.**

Hence \(\mathcal U\vee\mathcal V\not\le\mathcal H\). The coherent zigzag gives the reverse noninclusion. No single space with *both* noninclusions is required to refute a universal comparison; a disjoint-union example would need an additional componentwise preservation proof.

## Audit D — The lower diamond

### D1. Finite seed computation

For \(P=\{p,q,t,x,y\}\) with \(p<t,p<x,q<t,q<y\), I recomputed common-upper and common-lower relations by exhaustive pair enumeration. They contain respectively 15 and 17 ordered pairs, and their two-step relations satisfy
\[
|\mathcal U(P)|=23,\quad |\mathcal V(P)|=25,\quad P^2\setminus\mathcal U(P)=\{(x,y),(y,x)\}.
\]
**Pass.** This is a useful seed for both noncompact thickening and the separate compact construction.

### D2. Almost-normal thickening: targeted concern

The new \(\mathcal W\) boundary-transfer proof argues that if \((s,t)\notin\mathcal U(P)\), finite principal boundary upsets and distinct irrational attachment coordinates give open basic neighborhoods with disjoint rational traces and no \(\mathcal D\)-point in their rectangle; their product rectangle therefore misses \(\operatorname{cl}(\mathcal D)\). Conversely, every \(\mathcal U(P)\)-pair lies below a boundary \(\mathcal D\)-pair, so is in \(\mathcal W\). **Plausible and internally consistent.**

**Unresolved dependencies requiring a fresh check:** exact topology of the rational/nowhere-dense filter, whether the localic square is actually spatial, whether *every* its sublocale is point-determined (scatteredness + sober representation), and the almost-normality proof. The earlier focused audit of the thickening is internal, not a new blind external check. Since the compact counterexample gives an independent and simpler proof of lower-diamond strictness, a flaw in the thickening would not by itself undo the principal strictness conclusion.

### D3. Compact three-boundary-point example

Topology: \(p\)-neighborhoods contain \(p,x\) and cofinite tails of both sheets; \(x\)-neighborhoods contain \(x\) and cofinite \(S_1\); \(y\)-neighborhoods contain \(y\) and cofinite \(S_2\). The basis intersections work; every sheet singleton is clopen. The space is compact, locally compact, first-countable, sober (finite boundary + isolated clopen sheets), and scattered. The compact opens \(\{p,x\}\cup S_1\cup S_2\) and \(\{y\}\cup S_2\) intersect in noncompact \(S_2\), verifying noncoherence.

The specialization relation on the nonisolated boundary is exactly \(p<x\). The fitted diagonal's point relation is common-predecessor: precisely \((p,x),(x,p)\) off the diagonal. Inseparability adds \((p,y),(y,p)\); \((x,y)\) is separable by \(\{x\}\cup S_1\) and \(\{y\}\cup S_2\). Their closures always meet at \(p\), placing \((x,y)\) in \(\mathcal U\); upward saturation of fitted \(\mathcal V\) from \((p,y)\) puts it in \(\mathcal V\). Continuous real functions identify \(p,x,y\). All other offdiagonal pairs are separated by clopen sheet singletons. The stated complete hierarchy follows once the scattered-sublocale representation applies to the localic square.

**Pass** under the cited standard results. The rectangle \((\{x\}\cup S_1)\boxtimes(\{y\}\cup S_2)\) misses *all* \(\mathcal D\) points, providing an actual open neighborhood excluding \((x,y)\) from \(\mathcal W\). That is stronger than merely saying \((x,y)\notin\mathcal D\).

The example is **not almost normal**, by the explicitly exhibited \(A\prec B\) with no interpolant. Do not claim compact almost-normal strictness.

## Audit E — Literature and proof hygiene

The key scattered-sublocale correspondence is indeed standard: Suarez, *On the relation between subspaces and sublocales*, J. Pure Appl. Algebra 226 (2022), 106851, and Ball–Picado–Pultr, *On an aspect of scatteredness in the point-free setting*, Portugaliae Math. 73 (2016), Proposition 5.3, state the relationship between scattered spaces and complete subspace/sublocale representation. A separate standard theorem identifies products of locally compact sober spaces with their spatial localic products. **Check the precise sobriety and product hypotheses in the final manuscript.**

No novelty search or claim has been completed for these new theorems. The independent referee should focus on *correctness*, especially on the fitted/spatial passage, rather than priority.

## Audit verdict and instructions for external packet

**Internal verdict:** The compact lower-diamond counterexample and the universal lattice identities have convincing direct proofs. The coherent \(\mathcal H\)-as-graph-closure theorem and \(\omega+m\) examples are credible and unusually fruitful but rest on a nontrivial coherent-fittedness lemma. The noncompact almost-normal example relies on the most accumulated technical dependencies. No decisive gap found; none of the working results should yet be labeled externally verified.

**Blind external packet must not contain:** this document, these confidence assessments, vulnerability rankings, prior reviewers' verdicts, or repository history that reveals the internal audit. It **should** contain independently checkable definitions, proofs and proof obligations, including the exact two-ray and handle topologies, full compact three-point argument, and a concise description of the optional noncompact thickening. Ask the external referee to issue separate pass/fail/repair verdicts and state which results survive if a particular lemma fails.