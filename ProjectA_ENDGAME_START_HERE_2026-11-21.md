# Point-free topology — start here

*A mathematical reading guide · current as of 21 November 2026*

## The question behind the project

Cameron and Kumar's [*Graphs on Topological Spaces*](https://arxiv.org/abs/2610.14783) prompted a question: **what becomes of separation graphs when we replace a topological space by a locale?**

For a locale \(X\), a binary relation is a **sublocale of the localic square** \(X\times_{\mathbf{Loc}}X\). That is not always captured by an ordinary set of point pairs. Indeed, three things can differ:

- an ordinary relation on the points of \(X\);
- the *point-generated* sublocale of \(X^2\) corresponding to that relation;
- a **genuine localic relation**, which may contain nonzero information invisible to every ordinary point.

This difference matters for closure, fitting, separation and—especially—**relational composition**. The project began with the point-free separation hierarchy and grew into two connected mathematical studies:

**Study I — Genuine binary localic relations.** When can we calculate with these relations? Three useful regimes emerge: **coherent/patch order**, **compact Hausdorff closed supports and Booleanization**, and **scattered-index matrix decompositions**. Outside restricted regimes, neither pointwise composition nor associative algebra rules are automatically valid.

**Study II — Higher simultaneous witnesses.** How much information is preserved by the binary graphs when we also consider common upper/lower witnesses, patched higher relations, and their simplicial realizations? Binary data with the appropriate patch structure can recover important **1-type** information; it does **not**, by itself, recover the **2-type**.

The goal of this archive has primarily been **mathematical understanding**. It is a proof-guided research record, not a claim that every deduction is new to the literature or ready for publication.

## Your reading route

**If you read only one document, read the [two-study mathematical account](ProjectA_ENDGAME_TWO_STUDIES_PROOF_GUIDED_ACCOUNT_2026-11-21.md).** It is the adopted exposition; it does not require following the historical A/B/C research branches or the chronological audit trail.

For a slow first reading, the following two sittings provide natural stopping points. There is no need to check every proof or citation on this first pass.

| Suggested sitting | Read | What to look for |
|---|---|---|
| **First: why point-free changes the answer** | [Main account](ProjectA_ENDGAME_TWO_STUDIES_PROOF_GUIDED_ACCOUNT_2026-11-21.md), **Study I, §§1–3** (through Example 4) | The five-point relation hierarchy; a closed-and-fitted hull that fails transitivity; the rational-bridge obstruction; a composite with no ordinary middle point |
| **Second: what can be calculated, and what cannot be recovered** | Main account, **Study I §§4–5**, **Study II §§6–7**, then **§§8–9** | Scattered-sector matrix multiplication; why its associativity needs restrictions; patched higher witnesses; the six-point 1-type/2-type boundary; final synthesis |

Two companions are particularly useful **alongside** the account rather than as prerequisites:

- [Five worked examples, with fuller computations](ProjectA_ENDGAME_COLD_READ_FIVE_EXAMPLES_2026-11-21.md). Open the corresponding example after encountering it in the main account. It is fine to read just the examples on a first pass.
- [Notation and assumptions](ProjectA_ENDGAME_NOTATION_AND_ASSUMPTIONS_2026-11-21.md). Keep this nearby as a reference when a relation symbol, ambient category, or imported result needs checking. It is not necessary to memorize the whole notation table before beginning.

**A good first-read question:** at each transition, ask *which part of the argument uses ordinary points, which part uses sublocales, and why the distinction matters*. This is more important initially than retaining every theorem number.

## The five examples — what each is there to teach

| Example in the main account | Point of the example |
|---|---|
| **1. Five-point fence** | The basic localic separation relations are already distinct in a manageable finite coherent space. |
| **2. Two convergent zigzag rays** | The least closed-and-fitted diagonal hull \(\mathcal H\) need **not** be transitive, even coherently. |
| **3. Rational bridge étale locale** | Finite-cover and unrestricted-cover constructions can agree on ordinary pairs yet differ as genuine sublocales. |
| **4. Disjoint rational/irrational middle sets** | Two relations can have **empty ordinary pointwise composite** but **full nonzero localic composite** because their middle supports meet pointlessly. |
| **5. Six-point witness comparison** | Higher patched binary witness data can recover the chain **fundamental groupoid**, but cannot in general recover the chain **2-type**. |

There is also a short \(P\times(\omega+1)\) example in Study I, §4, showing how the pointless middle-witness mechanism lives inside a **nonisolated closed scattered-index sector**. It connects the compact-support and matrix calculi without requiring you to learn a new general theory first.

## A small vocabulary to keep in view

Throughout, \(X^2\) means the **localic** product \(X\times_{\mathbf{Loc}}X\), not a direct product of frames. A few recurring relations are

\[
\begin{aligned}
\Delta&=\text{the diagonal of }X,\\
\mathcal I&=\operatorname{cl}\Delta
  &&\text{(inseparability)},\\
\mathcal D&=\operatorname{fit}\Delta
  &&\text{(fitted diagonal)},\\
\mathcal V&=\operatorname{fit}\mathcal I,\qquad
\mathcal W=\operatorname{cl}\mathcal D,\\
\mathcal H&=\text{least sublocale containing }\Delta
  \text{ that is both closed and fitted},\\
\mathcal U&=\text{Urysohn separation relation},\\
\mathcal F&=\text{functional equivalence relation}.
\end{aligned}
\]

In the compact Hausdorff part, \(p(A,B)=[A\times B]\) is the **point-generated** bipartite relation and \(q(A,B)=[A]\times_{\mathbf{Loc}}[B]\) is the **full localic rectangle**. In the higher-witness study, \(M_n=I_n\cap D_n\) denotes a *simultaneous* upper/lower witness construction; it should not be confused with a binary composition power.

The [full notation reference](ProjectA_ENDGAME_NOTATION_AND_ASSUMPTIONS_2026-11-21.md) gives exact definitions, conventions, and theorem-specific hypotheses.

Three cautions make almost the entire account easier to read:

1. **A spatial locale need not have only spatial sublocales.** A genuine composition may therefore create information unseen by ordinary pairs.
2. **Localic relation composition need not be associative in general.** The coherent, compact rectangular and finite-support matrix results are deliberately restricted positive calculi. Finite joins and arbitrary infinite joins must not be interchanged casually.
3. **The higher-homotopy conclusions live in a specified patched Stone-sheaf \(\infty\)-topos**, under explicit descent and connectivity inputs. They are not an unrestricted theorem about intrinsic localic shape.

## When you want to check a proof

The main account links directly to its canonical technical sources. For the three major calculi and the higher comparison, the most useful destinations are:

| Mathematical topic | Go to |
|---|---|
| Coherent patch-order relation composition | [Coherent composition canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md) |
| Nontransitive closed-fitted hull and rational bridge | [Zigzag proof](A-H-two-convergent-zigzag-rays-nontransitive-coherent-counterexample-2026-10-24.md) and [rational bridge canonical](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) |
| Compact Hausdorff \(p/q\) rectangles and clique powers | [Rectangular calculus](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md) and [Stone overlap-clique rank](ProjectA_STONE_CLIQUE_OVERLAP_RANK_CANONICAL_2026-11-20.md) |
| Arbitrary-parameter scattered-index decomposition | [MAT*/MUL*/FINMAT* canonical proof](ProjectA_MATSTAR_MULSTAR_POSTREFEREE_CANONICAL_2026-11-21.md) |
| Higher witness groupoids, 2-connectivity and gluing | [Binary meet-hull canonical](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md) and [relative gluing canonical](PointFree_relative_gluing_twisted_CANONICAL_2026-11-11.md) |

For a *dependency question*—“does this proof actually establish the step being used, or is it imported from a previous theorem?”—consult the [proof dependency atlas](ProjectA_ENDGAME_PROOF_DEPENDENCY_ATLAS_2026-11-21.md). For all exact hypotheses and current evidence grades, use the [47-group theorem ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md). You need neither document to follow the initial story.

## After the first reading

**To understand what remains unresolved:** [Open-frontier register](ProjectA_ENDGAME_OPEN_FRONTIERS_2026-11-21.md). Here “open” means **unresolved in our project**, not necessarily open in the published literature.

**To compare with prior work:** [Literature crosswalk](ProjectA_ENDGAME_LITERATURE_CROSSWALK_2026-11-21.md), including Cameron–Kumar, Isbell, Johnstone–Sun, Plewe and the established point-free separation literature. The project's exact novelty/priority has **not** been systematically certified.

**To inspect the research history or audit evidence:** [Archival handoff candidate](ProjectA_ENDGAME_ARCHIVAL_HANDOFF_CANDIDATE_2026-11-21.md) and [source-by-source provenance review](ProjectA_ENDGAME_SECOND_PASS_47_GROUP_PROVENANCE_2026-11-21.md). The historical A/B/C identifiers are filing and provenance labels, **not** reading chapters. The more detailed [original three-branch synthesis](ProjectA_ENDGAME_MATHEMATICAL_SYNTHESIS_2026-11-21.md) is retained as a record of the route by which the results were discovered.

Several mathematical claims were refined or independently checked *after* their first referee reports. In particular, the later [focused clique/rectangular audit](ProjectA_FINAL_FOCUSED_CLIQUE_UNITALITY_REFEREE_RECONCILIATION_2026-11-21.md) checked full-support generation, exact clique ranks, finite-overlap realizations and unitality. The [current ledger](ProjectA_ENDGAME_THEOREM_LEDGER_CURRENT_2026-11-21.md), rather than any old dated “pending” banner, determines their present status. Model-generated independent audits are evidence of careful checking, **not human peer review, formal verification, or a publication-priority certificate**.

The planned **25 November 2026** research stopping point is an organizational milestone, not a deadline to prove outstanding conjectures or a declaration that the archive has already been frozen.
