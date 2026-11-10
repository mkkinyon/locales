# Project A — Post-referee reconciliation of the W-phase audit

**9 November 2026.** Prepared **after** receiving [the independent blind referee's original report](project-a/audits/2026-11-09/Wphase/Independent_Blind_Referee_Report_2026-11-09.md), and after comparing it with [the separate internal adversarial audit](project-a/audits/2026-11-09/Wphase/ProjectA_Wphase_INTERNAL_adversarial_audit_2026-11-09.md). The report was prepared using only the [blind prompt](project-a/audits/2026-11-09/Wphase/ProjectA_Wphase_EXTERNAL_BLIND_prompt_2026-11-09.md) and [technical packet](project-a/audits/2026-11-09/Wphase/ProjectA_Wphase_EXTERNAL_BLIND_packet_2026-11-09.md), **not** the internal audit. Preserve original report and packet unchanged. The finite-cover questions Q and Q′ remain **OPEN, DEFERRED**.

## 1. External verdict and coverage

The external referee reports **no false statement and no fatal gap** in the principal W-phase results. They specifically checked:
- the all-frame Boolean W witness theorem and lax naturality;
- the coherent W=H equivalences and maximal-specialization criterion;
- the relative-fitness and finite-branch shrinking results;
- the compact two-apex calculation W=H<U<F and the finite m-apex extension;
- fitted supplements and the W=H∧U criterion;
- the original finite-Alexandrov factor W-product theorem for **arbitrary** second-factor locale;
- the compact connected noncoherent strict diamond with W=H∧U < H,U < H∨U < F;
- the earlier scattered-factor special case.

The referee also independently recomputed finite-poset examples and inspected the genuinely localic steps in the two-apex and product proofs. This is **external corroboration of submitted claims**, not a mechanized formal proof or literature originality clearance.

Our internal audit independently passed the principal chain, correcting the "upset" vs **closed downset** miswording in the propagation lemma and adding the sectionwise Heyting-implication calculation. The external referee agreed with those repairs. The reviewer identified one further necessary proof repair C1 and two imported facts needing stated justification.

## 2. Required mathematical repairs

### (a) C1: U fitted ⇒ U=F in a coherent locale

The packet had argued that U fitted means its patch-closed point relation contains comparability connectivity, and then appealed to minimality of F. This appeal is incomplete **unless U is also an equivalence relation**.

**Repair:** In the coherent spectral point space, established identity U=I∘I and the common-upper description of I give, for every U-related pair x,y, a zigzag
\[
x\le a\ge z\le b\ge y.
\]
So \(\operatorname{pt}(U)\subseteq E\), where E is finite comparability connectivity. If U is fitted, its closed point relation is also upward and downward specialization-saturated, and contains Δ; moving the second coordinate along zigzags gives \(E\subseteq\operatorname{pt}(U)\). Hence \(\operatorname{pt}(U)=E\), now a patch-closed equivalence, so the previously audited minimality theorem yields F≤U and therefore U=F.

The equivalence involving **internal** localic transitivity can be justified without conflating localic composition with point-relation composition: internal transitivity implies point transitivity; point transitivity yields U=F by the coherent argument; F is a kernel-pair equivalence and thus internally transitive. Explicitly distinguish these steps.

### (b) Regular-core inequality

Include or link to the earlier proof that
\[
\boxed{d_U\le d_W\le d_U^{**},\quad
\operatorname{cl}(\operatorname{int}U)\le W\le U.}
\]
For any open \(o\le d_U^*\), every diagonal square-cover \(w_\mathcal C\) is dense in o: if a nonzero rectangle in o missed \(w_\mathcal C\), partition the cover members according to which rectangle-coordinate they miss, obtaining \(a^*\vee b^*=1\), contradicting the rectangle's lying outside \(d_U\). As the least dense Boolean sublocale lies in every dense open, D restricted to o is dense, and cl D contains o. The external referee's A1 supplies this argument. It was **already recorded** in the October and Q′ syntheses, but it should not remain a mysterious input in a self-contained W packet.

### (c) Coherent closed-fitted spectral criterion

Input S3 ("closed sublocale of coherent locale fitted iff its patch-closed point set is an upset") was inherited without proof. The referee supplies a prime-ideal-theorem/Priestley compactness proof in A2. Cite/record this input; clarify dependence on classical prime ideal theorem and Zorn where maximal specializations are taken.

### (d) Unchecked negative control is a packet omission, not a contradiction

The reviewer could not check the compact noncoherent T₀ p<x two-sheet control because the packet omitted its actual neighborhood bases. These exist in [the canonical source](A-lower-diamond-compact-three-point-working-note.md), §§Construction–The three relational levels, and were covered by the [24 October external post-V reconciliation](A-postV-external-audit-reconciliation-2026-10-24.md). For any future packet reproduce its full topology rather than ask the referee to guess.

### (e) Other fixes

- Input S2 must say **locale of a scattered space**, not ambiguously "spatial scattered locale"; do not claim all spatial locales have spatial sublocales.
- State that specialization order is \(x\le y\iff x\in\overline{\{y\}}\), so opens are upsets.
- Define \(C_P=\mathrm{Cm}(P)\) (pairs with a common lower specialization bound), and do not overload the labels S, F, Q, Y, I.
- Specify the **metric finite-star topology** at the origin in the multi-apex model.
- Clarify "U∘U" denotes internal localic composition in the headline theorem, while zigzag computations use point relations; explain the implication described in (a).
- Mark explicitly where spatiality of the **whole square** suffices (closed relations only) and where all sublocales are point-determined (scattered case).
- "Locally compact" in the non-Hausdorff examples requires compact-neighborhood bases, not an implicit Hausdorff argument.
- Do not claim the usual monotone-section presentation \(\mathcal O(P\times Y)\cong\mathrm{Up}(P,\mathcal O(Y))\) is new; its use in the W-product proof is the new part.
- The localic preimage operation preserves **arbitrary meets** of sublocales. The earlier caveat about possible failure of such pullback preservation was unnecessary. The explicit sectionwise fittedness proof is still useful for transparency.
- The B in fitted-propagation only needs full **upward saturation**; it is a closed downset in the actual application.

## 3. Referee's additional theorems: independent post-report tests

The report suggested three substantial additions, labeled **A3–A5**. These were NOT part of its own certificate. We separately checked them in [the technical note](ProjectA_Wphase_referee_additions_INDEPENDENT_checks_2026-11-09.md).

**A3: compact-factor D/W multiplicativity.** Internally corroborated (NOT externally certified by this blind audit):
\[
\boxed{D(X\times Y)=D(X)\times D(Y),\
W(X\times Y)=W(X)\times W(Y)}
\]
for compact locales X,Y. The proof uses finite rectangular covers and a locale-valid finite grid-refinement lemma; it is independent of point existence.

**A4: finite-Alexandrov U/H multiplicativity.** Internally corroborated (NOT externally certified by this blind audit):
\[
\boxed{U(P\times Y)=U(P)\times U(Y),\
H(P\times Y)=H(P)\times H(Y)}
\]
for finite upper-Alexandrov P and arbitrary Y. The U identity follows from the pseudocomplement's section formula; the H identity follows by comparing closed and fitted slices along specialization. Together with the already E-reviewed W product law, this yields, for **nonempty P**,
\[
\boxed{W(P\times Y)=H(P\times Y)\wedge U(P\times Y)
\iff W(Y)=H(Y)\wedge U(Y).}
\]
The referee had not explicitly excluded **P empty** from this reflection statement, where it plainly fails. Do so.

**A5: a compact connected T₁ W<H example.** Independently reconstructed from the referee's appendix, NOT part of the initial external certification. Let T have positive and negative open rays, cofinite apexes p+,p− along the respective rays, and a point q with basic neighborhoods
\[
\{q\}\cup(0,\varepsilon)\cup((-\infty,0)\setminus G),\quad G\text{ finite}.
\]
Put \(u_\pm\) for the ray with its own apex and \(A_\pm=u_\pm\cup\{q\}\). Then
\[
\boxed{
W(T)=A_+^2\cup A_-^2
<
U(T)=W(T)\cup(\{p_+\}\times u_-)\cup(u_-\times\{p_+\})
<
H(T)=F(T)=T^2.}
\]
The indispensable **pointfree** step is: every open neighborhood of W is dense on \(t_0=(0,\infty)\times(-\infty,0)\), because it contains every (x,q), x>0, and q-neighborhoods contain cofinally the negative ray. Hence the least dense Boolean sublocale B(t₀) lies in \(\operatorname{fit}(W)\wedge O(t_0)\), nonzero but pointless. Its closure equals \(\overline{t_0}=A_+\times A_-\), and together with the transpose and W fills T². The compactness, local compactness, connectedness, T₁, and sobriety were checked explicitly in the technical note.

This is the most conceptually important **new example** arising from the referee report: W<H can occur even in a connected compact locally compact sober T₁ space, with a genuinely pointless initial witness. It is a working post-referee result; do not silently call it externally audited.

## 4. Reassessing the connected strict diamond

The original connected compact example Z=P×Y was externally confirmed. The added A4 theorem sharpens its meaning: both strictness mechanisms are **factorwise**, one coming from the finite fence and one from the two-apex factor. Z is a genuine **connected, non-disjoint-sum** example as requested, but it does **not** demonstrate an intrinsically coupled defect in H and U.

This is a correction in *interpretation*, not a withdrawal of the theorem. Further searches for a genuinely coupled example would need to leave finite-Alexandrov factor transfer constructions behind.

## 5. Research triage and next actions

The external report offered two bounded ideas:

1. **Compact-product test.** Its underlying claim for *all compact factors* was checked via the finite grid lemma, and it survives as a working theorem; the direct Y×Y test is no longer necessary for that logical purpose. We do **not** assert arbitrary-product multiplicativity.
2. **T₁ test.** The referee's proposed T establishes W<H in a compact connected T₁ space; we independently checked it. It has H∧U=U>W, hence does not realize the desired intermediate equality. The larger question "T₁ + W=U ⇒ W fitted?" remains **unresolved**. There is no reason to start an unbounded counterexample search now.

The original package can be consolidated as E (externally corroborated) with the stated repairs. The referee additions A3–A5 are I (post-referee internally checked) and deserve a separate targeted audit if used as major standalone results.

**No change to Q/Q′: OPEN, DEFERRED.**
