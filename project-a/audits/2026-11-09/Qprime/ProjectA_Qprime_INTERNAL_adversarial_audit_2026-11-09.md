# Project A — Internal adversarial review of the Q′ programme

**9 November 2026 — INTERNAL ONLY. Do not transmit this file to the external blind referee.**

## Scope and decision

Review of the Q′ line of work from 24 October through 9 November 2026. Here
\(\mathcal D=\operatorname{fit}(\Delta)\), \(\mathcal D_2\) is finite-cover fitting,
\(\mathcal W=\operatorname{cl}(\mathcal D)\), and \(\mathcal W_2=\operatorname{cl}(\mathcal D_2)\).
The question \((Q')\), \(\mathcal W=\mathcal W_2\) for every frame, remains open.
The weaker \((Q)\), \(\mathcal W_2=\mathcal U\Rightarrow\mathcal W=\mathcal U\), remains open.

**Overall verdict:** There is a coherent, useful working programme here, but no
case for declaring the entire programme externally verified. The short new
structural lemmas pass the following internal mathematical checks. The long
forcing/gluing calculations need independent reconstruction, especially at
the precise frame-map and localic-closure steps. No fatal objection to the
short main lemmas was found in this pass. This is a targeted proof review,
not a claim to have mechanically verified every assertion in every dated note.

## I. Claims that survive targeted proof scrutiny

### I.1 Exact obstruction and algebraic preliminaries

The finite-cover neighborhoods \(w_F=\bigvee_{c\in F}c\boxtimes c\) are
closed under finite meets after passage to a common finite refinement.
The operators \(\Phi,\Phi_2\) are pre-nuclei, and the established frame-quotient
presentation gives \(\Phi_2(d_0)=d_0\) for \(d_0=d_{\mathcal W_2}\).
If \(\Phi(d_0)\not\le d_0\), extraction of a generating rectangle yields
\(r=a\boxtimes b\not\le d_0\) but \(r\wedge w_{\mathcal C}\le d_0\)
for some cover. The deduction \(a\wedge b=0\) uses
\(\Phi(d_0)\le d_{\mathcal W}\le d_{\mathcal I}\), followed by diagonal
inverse image. It is important not to replace this proof by an argument
about ordinary pairs of points. The cover necessarily lacks a finite subcover.

### I.2 Finite-color/chromatic obstruction

The finite-directed-family reduction is correct: if \(\mathcal C\) is a finite
union of directed subfamilies \(\mathcal C_j\), then
\(\bigvee_{c\in\mathcal C_j}c\boxtimes c=(\bigvee\mathcal C_j)\boxtimes(\bigvee\mathcal C_j)\).
The chromatic graph defined by cross products modulo \(d_0\) likewise has
infinite chromatic number for a genuine Q′ witness; otherwise the color-class
joins form a finite cover contradicting \(\Phi_2(d_0)=d_0\).

### I.3 Proper-over-regular theorem

For a locale map \(f:X\to Y\) with regular \(\mathcal O(Y)\) and directed-join
preserving \(f_*\), each cover of \(X\) is locally finitely covered *rather
below* using \(e=f^*(v)\) for \(v\prec f_*(\bigvee F)\). The counit
\(f^*f_*(\bigvee F)\le\bigvee F\) is in the correct direction.
The finite-cover compatibility lemma then proves \(\mathcal D_2(X)=\mathcal D(X)\).
This is a strong working theorem. Verify the convention identifying proper
locale maps with directed-join preservation in any polished statement, and
state any additional customary properness axioms separately rather than
silently weakening them.

### I.4 Local compact-complement theorem

For disjoint \(a,b\), compactness of the closed sublocale \(C(a\vee b)\)
yields a finite subfamily \(F\) with \(a\vee b\vee\bigvee F=1\). On the
rectangle \(a\boxtimes b\), the \(a^2,b^2\) terms vanish, proving
\(\mathcal D_2\wedge O(a\boxtimes b)=\mathcal D\wedge O(a\boxtimes b)\).
Open restriction commutes with relative closure, so the W/W₂ equality follows.

### I.5 Join-prime interface theorem

If \(a,b\) are disjoint and \(a\vee b\vee\bigvee_i n_i=1\) with all \(n_i\)
completely join-prime, then \(O(n_i\boxtimes n_i)\le\mathcal D\).
The two-color partition argument correctly proves density of \(\mathcal D\)
in \(\mathcal D_2\) on the mixed rectangle, hence local equality of W/W₂.
The hypothesis that each \(n_i\) is an element of the FRAME and completely
join-prime must not be confused with a merely prime point filter.

### I.6 Cover-dependent rather-below localization

For \(t_{\mathcal C}=\bigvee_{F\subseteq\mathcal C\;\mathrm{finite}}
\bigvee\{v:v\prec\bigvee F\}\), the finite cover \(\{v^*\}\cup F\)
yields \(r\wedge(t_{\mathcal C}\boxtimes1)\le d_0\) and the symmetric strip
inequality when \(r\wedge w_{\mathcal C}\le d_0\). In particular any
rectangular Q′ witness requires \(t_{\mathcal C}<1\). The result is
cover-dependent, not a class-wide separation axiom.

## II. Higher-risk assertions for the independent referee

1. **Frame maps to Boolean regular-open completions.** In the Scott/Cantor,
   branching, rational-filter, and perfect-tree examples, explicitly verify
   the proposed sectionwise maps preserve *arbitrary* joins and finite meets,
   including compatibility of overlapping cylinders; don't mistake a
   Boolean-algebra homomorphism for a frame homomorphism.
2. **Finite-cover color-class density.** The missing-center and denominator
   constructions rely on finite colorings of the rationals and Baire category.
   Verify that every target cylinder and every nonempty parameter interval
   admits two distinct labels in the same color, outside its finite support.
   For denominator labels, check removal of a finite set of denominators is
   locally finite, and check that the two labels can be chosen with distinct
   denominators.
3. **Localic versus spatial square.** All local equality assertions for
   \(\mathcal U\) and \(\mathcal W\) must be justified by coproduct-rectangle
   expansion or factorization, not only pointwise calculations. The
   two-stage disjoint-parameter refinement is essential.
4. **Sublocale density.** A nonzero \(\mathcal D_2\)-point in the atomless
   boundary, or a Boolean factorization that does not factor through
   \(\mathcal D\), does *not* imply a gap in their closures. The
   examples repeatedly demonstrate this; the referee should check
   every step claiming that \(\mathcal D\) remains dense.
5. **Perfect-tree Boolean completion.** The identification of the Boolean
   complement of a bit condition, and the existence of a nonzero perfect
   condition fixing all bits in an infinite set with infinite complement,
   are plausible but warrant an independent check. The conclusion proved is
   only that the *natural mirror pair* fails a two-element-cover test,
   not that all Sacks-style approaches are impossible.
6. **Topological representability.** Countable bases, closed discrete
   remainder, and soberification claims should be checked individually.
   The counterexample logic does not require every presenting space to be sober.

## III. Audit outcome by level

| Material | Present assessment | External task |
|---|---|---|
| Algebraic definition, fixed-point and rectangle certificate | Supported; earlier foundational audit provenance | Independently check the disjointness extraction and implications |
| Proper regular-base fitting theorem | Targeted internal proof PASS | High priority: reprove in full |
| Compact complement and join-prime local no-go theorems | Targeted internal proof PASS | High priority: reprove both |
| Cover-dependent remainder and chromatic graph | Targeted internal proof PASS | Check graph quantifiers and strips |
| Scott/Cantor original D₂>D example | Established working control | Verify maps and why W=W₂ |
| Rational/filter, forcing, repeated-denominator examples | Internally plausible but longer calculations | High priority: independently reconstruct at least one representative full example |
| Perfect-tree two-cover failure | Plausible negative test, NOT general theorem | Check target, two-cover and Boolean condition |
| Universal Q and Q′ | OPEN | Suggestions welcome, not demanded |

## IV. One strategic caution

The original rationale for an external audit should be to detect errors in a
proliferating set of working claims, not to recruit a referee into unbounded
counterexample search. Request at most a few *concrete* suggestions, explicitly
permit the answer “no useful suggestion”, and decide whether to test them
only after the mathematical report has been reconciled.

No theorem-ledger upgrade or final consolidation should be made on the
strength of this internal review alone. The original external Q/W foundational
report and its corrections remain separate historical sources; do not give
those reports or this internal file to the new blind referee.