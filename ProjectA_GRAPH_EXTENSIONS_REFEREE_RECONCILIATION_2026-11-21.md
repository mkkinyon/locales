# Project A — graph chart rank: external-vs-internal audit reconciliation
**21 November 2026 · Independently blind-refereed graph phase, with addendum**

## Sources, protocol and status

The [independent report](project-a/audits/2026-11-21/GRAPH_CHART_RANK/INDEPENDENT_REFEREE_REPORT.md) was produced from the blind packet without the [internal adversarial audit](ProjectA_GRAPH_CHART_RANK_INTERNAL_ADVERSARIAL_AUDIT_2026-11-21.md) or live repository. The [separate referee addendum](project-a/audits/2026-11-21/GRAPH_CHART_RANK/REFEREE_ADDENDUM.md) records discoveries after that review. Both are preserved in their own files. The independent verdict is **CORRECT WITH MINOR REPAIRS, CONDITIONAL ON THE IMPORTED (RC)**. That rectangular theorem was independently reviewed in the [prior compact-Hausdorff audit](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) but *not re-audited here*.

The [canonical post-referee theorem note](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md) is now the primary reference; the following comparison distinguishes the submitted, independently accepted, addendum-origin, and new post-addendum deductions.

## 1. Comparison with the internal audit

**Agreement:** Both audits accept the locally closed restriction [B]∧U=[B∩U], exact graph actions on **p and q** rectangles, closure of locally closed partial homeomorphism graphs under composition/converse, triple-generator associativity conditional on RC, finite-join extension, two-sided rectangular ideal, generator-word normal forms, the graph probe and its direction, open proper projection failure, finite/infinite compact metric projection-fiber dichotomy, at-most-two-to-one Cantor-to-Cantor negative map, infinite chart rank, symmetric ghost edge, and Michael zero-dimensional selection/section removal.

**External improvement beyond the internal audit:**
1. Explicit check of **all eight** rectangle/graph generator words RRR, RRH, RHR, RHH, HRR, HRH, HHR, HHH, with special emphasis on the localic overlap transport RHR.
2. Sharp wording correction: in RRR the product is q(A,F) when adjacent middle overlaps are nonzero, but **q(A,F) can itself be 0** if an outer support is empty; never assert the zero outcome occurs *iff* some middle overlap vanishes.
3. Explicit justification that finite-join preservation holds for sublocale pullbacks and localic images; no infinitary assertion.
4. Explicit reason that locally closed inclusions compose; no extension to arbitrary induced spatial subspaces.
5. Michael selection proof distinguishes the existence of a **compatible complete metric on an open subset** from completeness of the inherited subspace metric.
6. The topological section-removal theorem extends to **completely metrizable X and metrizable zero-dimensional Y**, with a uniform finite fiber bound; the localic algebra corollary keeps compact-Hausdorff hypotheses.

**External new adversarial test:** For a non-locally-closed partial identity h=id_Q on countable dense Q⊂Cantor, the false extension of the graph formula predicts R∘Γ_h=0 against a genuine localic meet [I]∧[Q]≠0 for I=Cantor\Q. This illustrates the sharp role of locally closed domains. It was not a retraction of any submitted claim, which kept that hypothesis.

## 2. Detailed claim ledger

| Claim | Independent verdict | Dependency/qualification |
|---|---|---|
| LC/LCR, localic restriction of point-generated and full rectangles | PASS | Separate open/closed pullbacks |
| PH, partial-homeomorphism action formulas | PASS | Actual graph pullback and isomorphism |
| H, closure of partial homeomorphism charts | PASS | Locally closed inclusions compose |
| ALG, associative finite-join chart/rectangle algebra | PASS conditional | Imported RC; repair empty-outer zero prose |
| LH, finite open chart cover for compact local homeomorphism | PASS | Compactness |
| IDEAL / NF, two-sided rectangle ideal and word types | PASS conditional | RC/ALG; allow 0 separately |
| GP / NR, singleton graph probe | PASS | Independently derived |
| OP, globally open proper projection negative graph | PASS | Discrete support selector |
| FIN, product-projection iff finite compact metric fiber | PASS conditional | Negative independent; positive via ALG |
| C2, at-most-two-to-one Cantor map | PASS | Proper/surjective, not open |
| RANK-NEG, infinite chart rank | PASS | Stronger: even arbitrary finite injective-chart cover impossible |
| SYM / SYM3, symmetric ghost edge | PASS | Clopen four-level support and ordinary path analysis |
| SEL, Michael zero-dimensional optimal chart rank | PASS | Published theorem, independently checked |
| G-SEL, algebra application | PASS conditional | ALG/RC |

No substantive retraction was requested.

## 3. Referee addendum: a correction to the research question, not to a theorem

The initial broad open question was whether finite locally closed partial-homeomorphism chart rank is **necessary** for a graph to be adjoined associatively to the full rectangular algebra. The addendum disproves that broad necessity.

**Safe infinite-chart-rank example (A1).** For X=(C×{0})⊔(C×{1}), Y=C and
\[
f(y,0)=y,\qquad f(y,1)=c
\]
the fiber over c contains a whole Cantor sheet, so chart rank is infinite. Yet its graph is Γ_h∨q(C×{1},{c}), a **finite join of a homeomorphic graph and a constant rectangle**, hence already belongs to the positive algebra. A continuous finite-image map is an even simpler safe infinite-rank example, because its graph is a finite join of constant rectangular pieces.

**Finite-exception criterion (A2/A3).** The addendum precisely characterizes membership of a continuous compact-Hausdorff functional graph in the **particular** algebra \(\mathcal A_{\rm lc}(X\amalg Y)\): a finite cover by partial homeomorphism charts **plus constant-function pieces**, equivalently a finite set of exceptional target values outside which only finitely many locally closed charts are required. If every fiber is finite, adding each exceptional preimage point as a singleton chart proves
\[
\Gamma_f\in\mathcal A_{\rm lc}\ \Longleftrightarrow\ \rho_{\rm lc}(f)<\infty.
\]

**Crucial logical distinction:** Membership in the known safe algebra **implies** safe adjunction. The addendum does *not* prove that *every* safely adjoining graph is already a member; the converse is open. Accordingly, the **finite-to-one necessity of chart rank under safe adjunction** remains open, even though necessity for membership is settled.

## 4. A new small post-addendum consequence

The [canonical note §7](ProjectA_GRAPH_EXTENSIONS_POSTREFEREE_CANONICAL_2026-11-21.md) defines a provisional rectangular–chart generator number \(\lambda(f)\), and from the addendum's proof derives
\[
\lambda(f)=\inf_{F\subseteq Y\ \mathrm{finite}}
\left(|F|+\rho_{\rm lc}(f|_{X\setminus f^{-1}(F)})\right).
\]
This is **not in the independent referee report or addendum**; it is a new, elementary **internal** quantitative deduction. Treat it as pending audit if used as a formal theorem later. The formula counts two kinds of witnesses—**partially invertible charts** and **exceptional constant-fiber rectangles**—and is useful for framing the next experiments.

## 5. Concrete post-audit research priority

The central natural question is now:

> For compact **finite-to-one** maps, can graphs be safely adjoined to the entire finite rectangular algebra without belonging to \(\mathcal A_{\rm lc}\)? Equivalently, does safety force finite locally closed chart rank under suitable compact metric hypotheses?

The graph-probe NR condition is necessary but not known sufficient. The two-to-one Cantor example violates it and is unsafe. The referee's safe infinite-rank example lies inside the known algebra because it contains a **constant rectangular component**, and therefore does not address finite-to-one necessity.

Secondary questions: the sharpness of the locally closed restriction for *open non-locally-closed* induced sublocales; graph-witness invariants bridging imposed Stone relations to intrinsic Cameron–Kumar specialization and separation graphs; generalized zero-dimensional selection outside compact metrizable settings.

**Consolidation status:** Report and addendum preserved separately; repaired zero-case and provenance recorded; externally reviewed graph phase complete **conditional on independently established RC**; canonical note and repository navigation updated. No claim that the new addendum replaces the earlier referee verdict.
