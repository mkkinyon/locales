# Project A — reconciliation of the 20 October 2026 independent audits

**Status:** repository correction ledger, following independent reviews by **ChatGPT High** and **Claude Opus 5.5 Extra** and a source-by-source comparison. The user supplied both reports. Both reviewers received the internal foundational audit in the same context, so the reviews were **not strictly blind**; the external mathematical derivations and new examples were nevertheless checked independently during reconciliation. **No claim of priority.**

This ledger is a *change log*, not a replacement for the proof notes or for the full external reports.

## 1. Main results retained, with their logical status

1. **For all locales:** the rectangle pseudocomplement is \((a\boxtimes b)^*=(a^*\boxtimes1)\vee(1\boxtimes b^*)\). Finite farness, \(\Delta\subseteq I\subseteq U\subseteq F\), \(I\circ I\subseteq U\), and \(\mathcal F\) as the kernel pair of the completely regular reflection survive the audits. The functional relation's completely-below description relies on Picado–Pultr VI.1.5.2 and VI.2.2.
2. **Vermeulen's proper-relation theorem:** in *Proper Maps of Locales*, JPAA 92 (1994), Proposition 5.5 and **Corollary 5.17** (p. 107), a closed proper internal equivalence relation has a proper effective quotient, with **no ambient compactness requirement**. The original paper was uploaded and read directly; the earlier interpretation as only a compact-locale theorem was erroneous.
3. **Continuous-frame proper collapse:** for a continuous L, if I is a **transitive internal equivalence relation** and its two projections are proper locale maps, then I=U=F and the quotient is the completely regular reflection, using Vermeulen and classical Hofmann–Lawson. It suffices to assume I=U for transitivity, by the point-free composition lemma. This is an audited consequence of cited published machinery, **not** a new general proper-relation theorem.
4. **T1 algebraic subfit counterexample:** the cofinite-cloud deleted-plank space has a **continuous, algebraic, subfit** frame with I=U⊊F, compact-open separation/interpolation witnesses, and a crowded Cantor-product variant. Both external reviewers found no fatal error.
5. **Compact locale strengthening:** for **any compact locale** X (possibly pointless and not continuous), transitivity of I implies I=U=F. Closed relation projections are proper, Vermeulen's quotient is effective/compact with closed diagonal, and classical compact Hausdorff locale theory makes the quotient completely regular. This was overlooked by the original point-set proof. **Bibliography check pending:** locate the exact primary theorem compact Hausdorff locale ⇒ regular/completely regular (Vermeulen 1994 p. 96 cites his 1991 work).

## 2. One false core assertion, and the stronger counterexample

The exact operator formula

\[
r_I(u)=(p_2)_*p_1^*(u)
=\bigvee\{v:1\boxtimes v\le(u\boxtimes1)\vee d_I\}
\]

is valid for arbitrary locales. Its fixed points are the invariant opens when I is reflexive/symmetric. **False:** an internal equivalence relation, *even I=clΔ=U=F*, makes r_I idempotent. Properness of the projections **does** ensure idempotence and Scott continuity (Vermeulen Lemma 5.2).

Claude's countable **strongly locally compact sober algebraic** example with pair classes \(\{a,b\},\{c_n,d_n\}\) has \(I=U=F\), compact Hausdorff quotient \(\omega+1\), and an open \(u\) with

\[
r_I(u)=\{b\},\qquad r_I^2(u)=\varnothing.
\]

Every I-class is finite, but the quotient is **not closed**. By contrast, the deleted-plank cofinite-cloud quotient is closed but has **noncompact** fibers and non-Scott-continuous r. They are distinct failures of properness.

Full topology, proof, and a precise spatial idempotence criterion: [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md).

**Scope:** a general topological equivalence relation has \(r_E(u)=\operatorname{int}(X\setminus E[X\setminus u])\), with the interior essential unless the relevant saturations are closed. Scott continuity of \(r_I\) is not asserted equivalent to properness of the localic relation projections. The exact general-localic converse is still unproved here.

## 3. New arithmetic example and updated hypothesis candidates

The original **two-tag** deleted-plank topology has an **arithmetic frame**, provided the starting locally compact Hausdorff T has a compact-open basis (as the plank does). For any compact open V⊆X, V∩T is compact open in T because T is closed. The converse compactness implication also holds for opens with compact T-part since only finitely many tags are attached. Thus compact opens form a basis and are closed under finite meets; nevertheless I=U⊊F.

Hence **stable continuity/arithmeticity alone fails** as a repair. The two-tag frame is **not subfit**. The cofinite-cloud example is subfit but not arithmetic. **Subfitness plus arithmeticity together** remains a candidate, not a proved theorem or counterexample.

## 4. Corrected ancillary statements

- **Compact-buffer lemma:** The asserted inclusion \(E[K]\subseteq\overline a\) specifically needs **E=I=clΔ** (or an equivalent relation-to-closure hypothesis), not any closed equivalence E. Moreover \(u\ll a\) yields compact \(K\) with \(u\subseteq K\subseteq a\) only under **strong local compactness** or an explicit compact-containment assumption; weak local compactness alone does not suffice.
- **Paracompactness:** Locally compact σ-compact spaces are not necessarily paracompact under the project's open-refinement, non-Hausdorff definition. Counterexample: \(\mathbb N\) with opens \(\emptyset,[0,n],\mathbb N\) (strongly locally compact, sober, σ-compact; cover by finite initial segments has no locally finite refinement). Uncountable **disjoint sums of compact** spaces still supply the intended non-σ-compact paracompact examples. The separate paracompact decomposition proof remains.
- **Fitted diagonal:** For non-sober topological X, \(\mathcal O(X)\) has points of the **sobrification**, so not every locale point comes from an original point. The T1 criterion for the *original-point relation* D is correct; to identify **all** locale points with original points, assume X sober. Do not infer localic D=Δ from pointwise T1.
- **Three-point particular-point topology:** with the upper-set convention the poset is \(x<p>y\), **not** \(p<x,p<y\).
- **Pointless finite-poset product:** both directions of the isomorphism \(\mathcal O(P)\otimes B\cong\operatorname{Mon}(P,B)\) are made explicit in the hierarchy note.
- **Noncompact intermediate-neighborhood notes:** stale “unresolved” conjectures and an overstated “arbitrary topological spaces” lemma are marked as historical or corrected.
- **C*-algebra aside:** E=F is not asserted merely from Orc=1 without the other conditions of the cited operator-algebra result.
- **Primary Vermeulen access:** source is now directly available, not just a search-index quotation; stale “403” status statements have been superseded.

## 5. Reconciliation targets

Primary corrected files:

- [A-consolidated-theorems.md](A-consolidated-theorems.md) — authoritative theorem/status map.
- [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md) and [A-vermeulen-effectiveness-correction.md](A-vermeulen-effectiveness-correction.md) — corrected conditions for idempotence, properness and effectiveness.
- [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md) — new complete counterexample proof.
- [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md), [A-continuous-frames.md](A-continuous-frames.md), [A-obstruction-candidates.md](A-obstruction-candidates.md) — arithmetic example and compact-locale positive result.
- [A-fitted-diagonal.md](A-fitted-diagonal.md), [A-equality-characterizations.md](A-equality-characterizations.md), [A-beyond-countable-exhaustion.md](A-beyond-countable-exhaustion.md), [A-noncompact-intermediate-neighborhoods.md](A-noncompact-intermediate-neighborhoods.md), [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md), [A-stable-interpolation-test.md](A-stable-interpolation-test.md), [A-hierarchy-first-results.md](A-hierarchy-first-results.md), [A-closed-saturation.md](A-closed-saturation.md), [A-way-below-revisited.md](A-way-below-revisited.md) — scope fixes and superseded statuses.
- [A-literature-priority-review.md](A-literature-priority-review.md) and [README.md](README.md) — navigational and bibliographic reconciliation.

## 6. Remaining reservations (not hidden by the edits)

1. Retrieve and cite precisely the classical **compact Hausdorff locale ⇒ completely regular** theorem; the compact nonspatial strengthening is sound *conditional on* this standard result.
2. Claude's wider statements about Scott-continuity converses (e.g. for LCH relation spaces) were **not incorporated as theorems** here without a further independent proof.
3. The audits did not exhaustively examine all peripheral results on C*-algebra primitive spectra, \(k_\omega\)/paracompact stages, or the entire fitted-diagonal literature.
4. Priority of the two-tag and cofinite-cloud uses and of the Project A relation framework is not certified.
5. The user’s two independent reviews were not completely blind because the internal audit was included in each context; their new examples and cross-checks still materially improved reliability.

**Editorial principle:** historic exploratory notes are preserved with explicit “superseded” qualifications, rather than silently rewritten to suggest every conclusion was known on its original date.
