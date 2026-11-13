# Project A — Q/Q′ post-referee reconciliation (13 November 2026)

**Current audited checkpoint (classical mathematics with choice).** This note supersedes the *status* and next-test predictions of [the 12 November Session 7→8 checkpoint](ProjectA_Q_SESSION8_CONSOLIDATION_2026-11-12.md), but does not rewrite its historical mathematics. The [blind packet](project-a/audits/2026-11-12/Q-postsession7/BLIND_PACKET.md), [independent referee report](project-a/audits/2026-11-12/Q-postsession7/EXTERNAL_BLIND_REFEREE_REPORT_2026-11-12.md), [source-check addendum](project-a/audits/2026-11-12/Q-postsession7/EXTERNAL_SOURCE_CHECK_ADDENDUM_2026-11-13.md), and [referee's further ideas](project-a/audits/2026-11-12/Q-postsession7/EXTERNAL_FURTHER_IDEAS_2026-11-13.txt) remain separate. See [current priorities](ProjectA_Q_POSTREFEREE_PRIORITIES_2026-11-13.md).

## 1. Questions, notation, and verdict

For a locale X, write L=O(X), P=O(X²), w_C=∨_{c∈C}(c⊠c) for an open cover C of X, and

\[
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]

The baseline rank-zero identity is z=Φ(0)=Φ₂(0); U=C(z). Let D,D₂ be the all-cover and finite-cover fitted diagonals, W=cl D, W₂=cl D₂. Let d=Φ₂^∞(0), so W₂=C(d).

- **Q:** Φ₂(z)=z implies Φ(z)=z, for every locale?
- **Q′:** W₂(X)=W(X), for every locale? Equivalently B(D₂(X))≤D(X) for every X. Q′ would imply Q.
- **Status:** **both OPEN**. Never infer a relatively open hole from a nonzero weak defect D₂∧C(w_C), infinite chromatic number, noncompact spectral contact, or a failure of nonclosed D₂ product preservation.

The blind referee found no false displayed theorem in sections A–G. The subsequent source check resolved all previously uncheckable shorthand from repository notes: canonical symmetric support K_E, intrinsic link graph Γ_E, clopen variants, and the original two-apex space. Final *referee verdict*: 26/26 claim groups correct, four subject to named imports. This is **not** a second independent audit of the referee-origin N2–N7, nor independent certification of the imported theorems. The source check confirms N1 repeats existing frontier Theorem 1.1, and N7(a) repeats an earlier fact about point sets.

Source correction: in Arrieta's 2024 example, Cor. 4.3 and Prop. 4.4 establish strong Hausdorffness and the anti-Urysohn property. Second countability follows by a separate countable-Cantor-base plus compact-K_n argument; W=W₂=U=A² follows from z_A=0 and Φ(0)=z, **not** from the cited paper's own relation computation.

## 2. Referee-origin results retained

### Boolean-base splitting: N3 (highest-impact new theorem)

For **every** Boolean locale Z with diagonal-complement open d_Z and **every** locale Y,

\[
\boxed{\Phi_{Z\times Y}(d_Z\boxtimes1)
=z_{Z\times Y}=(d_Z\boxtimes1)\vee(1\boxtimes z_Y).}
\]

Sketch. For any product cover C, test a basic rectangle R below w_C→(d_Z⊠1). Split its two Boolean base coefficients into the three off-diagonal pieces (already under d_Z⊠1) and the common coefficient m. For each c∈C, let α_c (resp. β_c) be the Boolean base support of c intersected with m⊠a (resp. m⊠b). The implication hypothesis gives α_c∧β_c=0. Refining each c by the complementary base opens α_c and ¬α_c yields a cover whose members miss one or the other designated product rectangle. Thus the two rectangles are far. The pure-rectangle pseudocomplement formula forces a*∨b*=1 on the common nonzero base piece, hence the residual rectangle lies under 1⊠z_Y. The reverse inclusion follows from Φ(0)=z_X and inflationarity.

**Corollary.** If Y is anti-Urysohn (z_Y=0), then

\[
\boxed{W(Z\times Y)=W_2(Z\times Y)=U(Z\times Y)=\Delta_Z\times Y^2.}
\]

In particular this applies to **Cohen Boolean Z_C × Arrieta A** with no distributivity and no bound on the basis of Y. This product is **Q-positive and Q′-positive**. Its previously advertised closed-level test is **settled**. The remaining **nonclosed** question is whether D(Z_C×A)=Δ_{Z_C}×D(A). N3 was re-derived twice by the referee and independently checked at proof-sketch level in Session 8; record it as *referee-derived, internally checked*, not as two external audits.

### N4: sharp nonclosed failure, Cohen × Scott

For B=Loc(RO(2^ω)) and S the upper-Alexandrov space of nonempty finite subsets of ω,

\[
\boxed{D_2(B\times S)\subsetneq\Delta_B\times D_2(S).}
\]

The referee constructs a binary product cover using the generic coordinate sets [x_n=e] and the Scott generators c_n, and frame maps h,k from O(S) to RO(2^ω×2^ω) with h(c_n)≤[x_n=1], k(c_n)≤[x_n=0]. Every infinite N⊆ω has ∨_{n∈N}h(c_n)=∨_{n∈N}k(c_n)=1. Thus every finite cover of S is matched by (h,k), while the displayed binary cover of B×S is matched to zero. This proves the strict inequality. It is compatible with N3: W₂(B×S)=U(B×S)=Δ_B×S² despite the nonclosed D₂ defect.

**Further-ideas strengthening, checked at the same algebraic level:** Replace the Boolean locale B as base by the **ordinary spatial Cantor space K=2^ω**, retaining the Booleanization T=Loc(RO(K×K)) as the domain of the generalized endpoints. Its projection T→K and the same H_n,K_n and binary cover give

\[
\boxed{D_2(K\times S)\subsetneq\Delta_K\times D_2(S).}
\]

This is not a contradiction of the spatial-base theorem (C.7): that theorem only transfers **closed hulls**, not D₂ itself. The spatial strengthening is a referee suggestion with an internally reconstructed proof, **not an additional blind-reviewed theorem**.

### N5: two refinements of Boolean-base transfer

For Y with a basis of cardinal ≤κ and κ infinite:

1. The finite fitted-diagonal formula D₂(Z×Y)=Δ_Z×D₂(Y) only needs **(κ,2)-distributivity** of the complete Boolean frame O(Z). For a finite product cover, each basis coefficient yields a **finite** labelled Boolean partition; each such partition is a finite refinement of binary partitions. The full D formula still uses the stronger **arbitrary-width** SDκ hypothesis.
2. If Y is an upper-Alexandrov locale, then **without any distributivity assumption on Z**, Δ_Z×D(Y)≤D(Z×Y). When D(Z)=Δ_Z, equality follows from naturality. Here D(Y)=O(w_{C₀}) for the *infinite, generally non-finite* minimal cover C₀={↑t}. **Do not infer D₂(Y)=D(Y).** Indeed the Scott pair in N4 is in D₂(S) but not D(S).

### N2, N6, N7, and earlier N1

- **N1 one-sided regular rigidity:** an independent rediscovery of the established frontier theorem; any frame target is allowed and binary covers suffice.
- **N2 tame-element criterion:** for an arbitrary cover C, q∈O(X²), x=w_C→q and locally-finite locus ℓ_C, if the tame base opens join to 1 (see the referee's precise definition), then x≤Φ₂²(q). In particular **regular** as well as compact tail remainder H_C=C(ℓ_C) gives this two-step inequality **for every q**, replacing the older regular-case Booleanization detour. The same method strengthens chromatic-frontier estimates.
- **N6:** a simpler countable compact sober T₁ two-apex example with W=W₂<U; the original repository two-apex construction was also verified by the source check. Keep both with provenance.
- **N7(a):** ordinary-point finite-cover compatibility implies full-cover compatibility; removes T₁ from the Cantor–Bendixson argument. The ordinary-point rigidity was already used in earlier notes.
- **N7(b):** Alexandrov locales satisfy W=U because their minimal cover's implication operator is already a nucleus. This does *not* assert D=D₂.

## 3. New exact coherent-envelope span formula (referee idea 4, reconstructed)

Let \widehat L=Idl(L_lat), \widehat X=Loc(\widehat L), with ε:\widehat L→L the union map and closed embedding i:X→\widehat X. Let Σ(\widehat X) denote the join of images of all generalized common-predecessor spans in \widehat X². Then

\[
\boxed{
W_2(X)=\operatorname{cl}_{X^2}
\bigl(\Sigma(\widehat X)\wedge X^2\bigr).
}
\]

**Proof that avoids illicit closure/restriction interchange.** The trace identity F.1 gives
D₂(X)=D(\widehat X)∧X². Since every common-predecessor span matches *all* covers, Σ(\widehat X)≤D(\widehat X); hence Σ(\widehat X)∧X²≤D₂(X). For the opposite **density** assertion, take the Booleanization T=B(D₂(X)); its frame M is complete Boolean. Both endpoint maps h,k:L→M match every finite cover. By the finite Boolean lower-selection theorem E.1 there exists a bounded-lattice homomorphism p_fin:L_lat→M with p_fin≤h,k. Extend it to the frame homomorphism

\[
\widehat p(J)=\bigvee_{a\in J}p_{\rm fin}(a),\qquad J\in\widehat L.
\]

Then \widehat p≤h∘ε,k∘ε. Thus the two endpoint maps T→\widehat X have a genuine common predecessor \widehat p, and their image lies in Σ(\widehat X) **and** in X². Therefore B(D₂(X))≤Σ(\widehat X)∧X². Since B(D₂(X)) is dense in D₂(X), both sublocales have closure W₂(X). QED.

This describes W₂ using **ghost-mediated** common predecessors in the coherent envelope, not predecessors in X. Arrieta's Σ(X)=Δ while W₂(X)=X² is therefore no contradiction. The proof uses E.1/F.1 as audited inputs; the derived formula is newly reconstructed here and should have a separate adversarial check before being called externally certified.

## 4. Corrections and dependencies to carry forward

1. Include the **exact symmetric support** K_E=C(e_E), where e_E=∨{a:h(a)=k(a)=0} for the Booleanization of a marked open hole, and the **intrinsic graph** Γ_E formed from E itself. The source-check addendum verifies the support restriction and marked-hole persistence; never assert rank-one stabilization is inherited by an arbitrary closed support.
2. State the compact-clopen-chart product theorem and separated-factor clopen-bundle theorem by their **actual hypotheses**; retain citations to their original notes. The blind packet only named them.
3. Compact-fibre tube-cover transfer C.3–C.5 uses the standard **directed-join preservation** of the right adjoint π_* for a compact fibre. Beck–Chevalley is not necessary for the finite rectangle formula as audited. The generalized-span transfer C.6 uses density of product images and openness of projections; state both.
4. Arrieta source attribution and the minor terms “U-linked”, T₁ on scattered support, and overly strict caution on sublocale preimage-meet preservation require the corrections listed in the blind report.
5. The Shoenfield/Boolean-valued transfer sketch in the further-ideas file **is not an established theorem**. Its internal/external product dictionary, complexity of membership in Φ and its iterates, and forcing stability of least fixed opens have not been proved. Do not state arbitrary Boolean-base W/W₂ product transfer or Q/Q′ forcing invariance as fact.
6. The de Bruijn–Erdős finite graph witness consequence is correct *conditional on* an already-proved locally infinite-chromatic support statement, but high-chromatic Kneser/Borsuk graph **realizability as cover-link graphs** has not been shown.

## 5. Next work

See [ordered problem list and referee-idea triage](ProjectA_Q_POSTREFEREE_PRIORITIES_2026-11-13.md). The first research target is a **noncompact, genuinely higher-rank modification of the compact two-apex example** aimed at a nonzero relatively open Q′ hole. A separate concrete target is D(Z_C×A). The high-risk forcing-absoluteness speculation is parked behind precise preliminary lemmas.

**Provenance:** The external blind report and source-check were independently produced before seeing the internal audit. N1 overlaps a preexisting theorem; N2–N7 were developed in the referee report; the Cantor strengthening and ghost-span formula are from the referee's subsequent idea list, with the latter's proof newly supplied here. Q and Q′ remain OPEN.
