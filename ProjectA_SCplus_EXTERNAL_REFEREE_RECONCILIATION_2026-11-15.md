# Project A — SC+ independent referee reconciliation and status ledger

**15 November 2026.** This note compares the independently written blind report with the internal audit and identifies the changes made to the [canonical SC+ proof](ProjectA_SCplus_CANONICAL_2026-11-15.md). It is a **post-report reconciliation**, not part of the original blind packet. The referee did not receive the internal audit before producing their report. The historical [blind packet](ProjectA_SCplus_EXTERNAL_BLIND_PACKET_2026-11-15.md) is retained unchanged, alongside the [audit archive](project-a/audits/2026-11-15/SCplus/README.md).

## Verdict and scope

The referee independently checked the SC+ equivalence, saturation lemma, spatiality of \(\mathcal D\) and \(\mathcal M\), inseparability witness lemma, and the noncompact patch framework. **No fatal mathematical error was found.** They identified two presentation gaps requiring repair, a shorter proof, and examples showing that stability cannot be dropped. The work remains in **classical** locale theory, and none of the mathematical audits establishes publication originality.

For stably locally compact \(X\), we now record:
\[
\mathcal D=[\uparrow\Delta],\qquad
\mathcal M=[\{(x,y):\exists r,s,\ r\le x,y\le s\}],
\]
and
\[
\boxed{\mathcal S=\mathcal M\iff\text{every specialization interval is a chain}.}
\]
The **necessity** of the interval-chain condition is valid for all locales; the **sufficiency** fails already in some compact locally compact sober spaces that are noncoherent.

## Corrections incorporated in the canonical proof

1. **All diagonal neighborhoods, not only square covers.** The blind packet's proof of \(\mathcal A\le\mathcal D\) checked \(w_{\mathscr C}=\bigvee_c c\boxtimes c\) but did not justify that these opens are coinitial. Given arbitrary \(w=\bigvee_i a_i\boxtimes b_i\) containing the diagonal, the cover \(c_i=a_i\wedge b_i\) has \(w_{\mathscr C}\le w\). The canonical proof now says this explicitly.
2. **Noncompact patch/product scope.** A stably locally compact space can be embedded as the open upper (also open patch) part of the stably compact space obtained by adjoining a specialization bottom with only the whole space as neighborhood. This reduces patch/closed-order assertions and product stability to the compact setting. It is included to rule out a tacit global compactness assumption.
3. **Spatiality of \(\mathcal M\) simplified.** Applying the saturation lemma once gives \(\mathcal D=[\uparrow\Delta]\). Since \(\mathcal I\) is closed, \(\mathcal M=\mathcal I\wedge\mathcal D\) is **closed in the spatial locale \(\mathcal D\)**, hence spatial. There is no need to apply saturation again inside \(\mathcal I\). The identity \(\operatorname{fit}_{\mathcal I}\Delta=\mathcal M\) is retained as an optional useful equality.
4. **Points of induced sublocales.** In general \(\operatorname{pt}[B]\) need not equal \(B\). The proof now uses only that \(\mathcal M=[P]\) is the *least sublocale* containing \(P\), and that every member of \(P\) is a point of \(\mathcal S\) when the intervals are chains. This avoids assuming that \(\mathcal S\) is spatial.
5. **All-locale necessity.** The converse direction uses only the presence of an interval diamond as a point of \(\mathcal I\wedge\mathcal D\), and finite-join primeness of point sublocales. It does not require stability or compactness.
6. **Better controls.** The tent pospaces on \([-1,1]\) and \((-1,1)\) test the saturation lemma genuinely: \(\mathcal I=X^2\), while \(\mathcal M=\mathcal D\) is a proper spatial relation. The previously used escaping-witness sequence space was valid but did not test the key lemma because \(\mathcal M=\mathcal I\) there.

## Referee-origin boundary examples

- **\(X_1\)** (independently reported by the referee; basic argument reproduced in the canonical note): compact, locally compact, sober, not coherent; intervals are chains, yet \(\mathcal S\ne\mathcal M\). Its points are \(\bot,a,p,g_n\), with \(a\) and \(p\) inseparable, incomparable, and having the common lower bound \(\bot\). This is a **counterexample to extending SC+ by merely dropping stable compactness of intersections**.
- **\(T\)** (referee supplied): a locally compact sober noncoherent sequence-tree space with a saturated closed set \(C\) such that \([C]\) is **not fitted**. This blocks a universal extension of the saturation lemma. The full construction is in the report; we have not subjected this new example to a separate internal adversarial check, so it remains explicitly **referee-origin, pending independent project audit**.
- A one-point/topological fragment \(X_0=X_1\setminus\{\bot\}\) shows the pointwise formula \(j_C(w)=\bigvee_{u\supset C}(u\to w)\) can fail without coherence even when \([C]\) happens to remain fitted. This warns against confusing a failure of the pointwise interchange with failure of the corresponding nucleus join.

## Additional deductions and carefully bounded suggestions

- **Fitted diagonal separation.** In the stably locally compact class, \(\mathcal D=\Delta\iff T_1\iff\) Hausdorff. The proof follows from the common-lower-bound point formula and equality of the original and patch topologies when the specialization order is equality. This statement is limited to the present stable class; Arrieta–Picado–Pultr's general localic F-separation theory is subtler.
- **General saturation criterion, unverified.** The referee proposed an exact condition for all saturated \(C\) to yield fitted \([C]\), expressed in terms of closed \(G\), open \(V\), and \(\overline{N\cap G}\subseteq\downarrow(V\cap G)\) for some open \(N\) meeting \(G\). The referee explicitly described this as their own derivation and not a literature result. **Do not cite or use it as a theorem until rechecked.**
- **Potential priority overlap.** Literature on saturated sets, filters, and fitted sublocales (Jakl; Jakl–Suarez; Moshier–Pultr–Suarez), as well as the established fitted-diagonal work, must be consulted before originality claims for the saturation lemma.
- **Spatiality of \(\mathcal S\) remains open.** From \(\mathcal M\) being spatial it does *not* follow that \(\mathcal S\) is. The precise new question is (A-SC): does the oriented specialization sublocale \(\mathcal A\) equal the sublocale induced by its pointwise order graph? Neither the canonical proof nor the external audit resolves that question.

## Status of main claims

| Claim | Current status |
|---|---|
| All locales: \(\Delta\le\mathcal S\le\mathcal M\) | Accepted; open-neighborhood coinitiality repair incorporated |
| Saturated \(C\) in stably locally compact \(Z\) gives fitted \([C]\) | Internally and independently externally checked |
| \(\mathcal D=[\uparrow\Delta]\), \(\mathcal M\) spatial in stably locally compact \(X\) | Independently externally checked; shorter proof incorporated |
| Inseparability iff common upper bound in stably locally compact \(X\) | Internally and independently externally checked |
| SC+ iff interval chains | Independently externally checked in stated scope |
| SC+ necessary direction for all locales | Referee observation, direct proof incorporated |
| SC+ sufficiency for all locally compact sober spaces | **False** by \(X_1\) |
| Saturation lemma without coherence | **False** by referee's \(T\), awaiting separate project audit |
| General closed/downset criterion for fitted saturation | **Proposed, not project-audited** |
| (A-SC), \(\mathcal A=[G_\le]\) | **Open; next segment** |

## Repository and audit hygiene

The blind packet and internal audit are archived separately and unchanged. The canonical proof is the **current mathematical reading copy**. Dated master theorem ledgers and older open-problem records remain historical; their past statements about SC+ being open are superseded by this note. No files are deleted or rewritten for retrospective consistency. The main repository entry points carry a new top-of-file status pointer, so a reader need not find and reconcile historical status lines on their own.
