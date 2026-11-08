# Project A — Classification inventory and dependency audit: I = U, D = U, W = U

**Working consolidation, 7 November 2026.** Prepared as the next inventory installment following the independent associativity audit. This is a source-based critical reading of the repository and earlier external reports, **not** a new independent external referee report and **not** a priority determination. The text supersedes obsolete *status statements* in older chronological notes but leaves the original sources unchanged.

**Notation.** For a locale \(X\), \(L=\mathcal O(X)\), \(Q=L\oplus L\), \(a\boxtimes b\) is an open rectangle, \(\delta^*:Q\to L\) is the diagonal inverse-image, \(a^*\) is the pseudocomplement, and \(C(d)\) the closed complement of \(d\in Q\). Set
\[
 d_{\mathcal I}=\bigvee_{a\wedge b=0}a\boxtimes b=\bigvee_a a\boxtimes a^*,\qquad
 d_{\mathcal U}=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
 \quad\mathcal I=C(d_{\mathcal I}),\quad\mathcal U=C(d_{\mathcal U}),
\]
\[
\mathcal D=\operatorname{fit}(\Delta),\quad
\mathcal W=\operatorname{cl}(\mathcal D),\quad
\mathcal F=\bigwedge_{f:X\to\mathbb R}\ker(f).
\]
All these are **sublocales**, not merely pair relations on ordinary points. Frame normality and Cornish normal/conormal terminology require care (see §2).

## 0. Confidence convention

- **E:** a theorem within the scope of a favorable independent audit, with specified repairs taken into account. If the theorem was first supplied by the referee, record this as **E(referee-derived)** rather than implying a pre-existing independently checked project proof.
- **I:** an internally supported proof; a targeted independent check is still desirable.
- **W:** a working statement with a particular unresolved dependence.
- **O:** open. Distinguish *failure of a proof* from a counterexample.

A proof whose status depends on a standard imported theorem (for example, frame coproduct cp-ideals, compact-product properness, Isbell density, or Vermeulen effectiveness) retains that named dependency.

## 1. The class I = U: complete orthogonality rather than elementary farness

### 1.1 Exact arbitrary-frame tests

The single-generator formula
\[
 d_{\mathcal I}=\bigvee_{a\in L}a\boxtimes a^*
\]
gives the exact equality test
\[
 \boxed{\mathcal I=\mathcal U\iff(\forall a\in L)\ a\boxtimes a^*\le d_{\mathcal U}.}
\]
This is not the stronger elementwise statement \(a\wedge b=0\Rightarrow a^*\vee b^*=1\).

A useful relational version is **closure-nonexpansiveness**: a closed relation \(R=C(d_R)\) satisfies \(R\cap(O(a)\times O(a^*))=0\) for every \(a\) iff \(R\le\mathcal I\). Consequently
\[
 \boxed{\mathcal I=\mathcal U\iff\mathcal U\text{ is closure-nonexpansive on all opens}.}
\]
Proof audit: \(R\cap O(w)=0\) iff \(w\le d_R\), by the closed quotient \(Q\to\uparrow d_R\). No spatiality or relational composition is involved.

The cp-ideal description of \(L\oplus L\) yields a *tensor-free* criterion. Let \(\mathsf{Far}=\{(a,b):a^*\vee b^*=1\}\) and \(\mathsf{Disj}=\{(a,b):a\wedge b=0\}\). Generate the **least symmetric relation** containing \(\mathsf{Far}\) which is downward closed and closed under arbitrary joins in either coordinate separately, denoted \(\widehat{\mathsf{Far}}\). Then
\[
 \boxed{\mathcal I=\mathcal U\iff\widehat{\mathsf{Far}}=\mathsf{Disj}.}
\]
Equivalently the unary polar \(a^\diamond=\bigvee\{b:(a,b)\in\widehat{\mathsf{Far}}\}\) agrees with \(a^*\) for every \(a\). In any frame \(a^\diamond\le a^*\), \((\bigvee_i a_i)^\diamond=\bigwedge_i a_i^\diamond\), and \(a\le a^{\diamond\diamond}\). The cp-ideal identification is an **I**-level all-frame package, grounded in standard coproduct theory; it is an exact reformulation, not yet a conventional intrinsic axiom. Sources: [structural study](https://github.com/mkkinyon/locales/blob/main/A-I-equals-U-structural-study.md), [coherent conormality](https://github.com/mkkinyon/locales/blob/main/A-coherent-conormality.md).

### 1.2 Recognizable subclasses and scope

- **Algebraic frames**: \(\mathcal I=\mathcal U\) iff every pair of **compact** elements with zero meet is far. The necessity uses compact pure rectangles and the finite far-rectangle lemma; the converse uses compact generation. **E** for the compact-element argument as reviewed in the October 21 coherent/foundational reports.
- **Coherent frames**: iff \(K(L)\) is **conormal** as a bounded distributive lattice, equivalently (classically) each prime ideal contains a unique minimal prime. This is the familiar **mp** orientation for spectra of rings. **E**; priority belongs to existing distributive-lattice theory.
- **Frame–coframes**: iff \(L\) is extremally disconnected (\(a^*\vee a^{**}=1\) for all \(a\)). For fixed \(b\), coframe distributivity yields \((\bigvee_i a_i)^*\vee b^*=\bigwedge_i(a_i^*\vee b^*)\); hence the far relation already has the required infinitary closure. This covers **arbitrary**, not only finite, upper-Alexandrov spaces. **E** in the October 21 foundational recheck.
- **Regular frames** always have \(\mathcal I=\mathcal U=\Delta\). **E/standard**.
- **Continuous frames** (classical spatial Hofmann–Lawson setting): the way-below/far tests in the continuous-frame note give another characterization, with **spatial representation and relative-compactness dependencies**, not a proof for arbitrary choice-free locales. **I** for this broader characterization.

Important side issue: **\(\mathcal I=\mathcal U\) does not force \(\mathcal U=\mathcal F\) on general continuous locales.** The locally compact sober deleted-Tychonoff-plank constructions give \(\mathcal I=\mathcal U\subsetneq\mathcal F\), with stronger arithmetic/subfit versions recorded after the first example. Use the corrected, audited variant if a canonical example is needed; do not cite earlier “still open” language. In the coherent case, \(\mathcal I=\mathcal U\) does imply \(\mathcal U=\mathcal F\). For *compact arbitrary* locales, a stronger positive conclusion is argued using the proper/effective quotient theorem, but the current repository asks for a primary-source check of compact strongly Hausdorff \(\Rightarrow\) complete regularity; mark **I**, not an unconditional additional E entry. Sources: [continuous counterexample](https://github.com/mkkinyon/locales/blob/main/A-continuous-counterexample-plank.md), [proper inseparability](https://github.com/mkkinyon/locales/blob/main/A-proper-inseparability-relations.md).

### 1.3 Preservation and failure

\(\mathcal I=\mathcal U\) is **open-hereditary**, but not closed-hereditary. The open proof restricts the rectangle generators to \(\downarrow c\); the closed counterexample is \(\operatorname{Spec}k[x,y]\) versus its closed \(V(xy)\). Both claims were reviewed in October 21. It is preserved by **arbitrary frame coproducts** (all locales, no coherence assumption). The proof expands disjoint opens into finite-support coproduct meets; a single coordinate detects zero, and the factor's far-rectangle *cover*, transported by a frame map, suffices. This is **E with an explicit repair**: the nonvanishing of basic finite-support meets in an **infinite** coproduct needs the cp-ideal finite-support construction; induction on the number of factors alone is insufficient. It is also preserved by **arbitrary frame products**, corresponding to locale disjoint unions, with the locale extensivity proof stated rather than merely assumed. It is **not** preserved by arbitrary frame subframes or surjective frame quotients; a finite poset and the same poset with a new top give the witnesses. Sources: [coproduct proof](https://github.com/mkkinyon/locales/blob/main/A-coproduct-preservation-I-U.md), [closure properties](https://github.com/mkkinyon/locales/blob/main/A-closure-properties-I-U.md), October 21 [independent audit](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md).

### 1.4 Unresolved classification questions

A simpler **non-completion-based** formula for \(a^\diamond\) is not known here; neither is necessity of a far-grid refinement in arbitrary frames, nor an optimal ordinal bound on the cp-ideal completion. These are mathematically distinct from the solved coherent/algebraic cases. **O**, deferred; no new research search initiated in this inventory.

## 2. The class D = U: compact normality and unrestricted cover tests

For any open cover \(\mathcal C\) of \(1_L\), let
\[
 w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c.
\]
The family of such opens is cofinal (downward) among neighborhoods of \(\Delta\). Since \(\mathcal D\le\mathcal U=C(d_{\mathcal U})\), the **exact all-frame criterion** is
\[
 \boxed{\mathcal D=\mathcal U\iff
 (\forall\mathcal C,\ \bigvee\mathcal C=1)\quad d_{\mathcal U}\vee w_{\mathcal C}=1_Q.}
\]
This is a coverage identity in the *localic square*, not an ordinary-point assertion. **E** (October 21 audit).

**Compact normality theorem (E, referee-derived):** For a **compact frame** \(L\),
\[
 \boxed{\mathcal D=\mathcal U\iff L\text{ is normal}.}
\]
Here frame normality is \(a\vee b=1\Rightarrow\exists c,d\,(c\wedge d=0,\ a\vee c=1=b\vee d)\). One implication follows from shrinking every **finite** cover by normality; compactness reduces arbitrary covers to finite subcovers. The converse uses compactness of \(1_Q\), finite far rectangles and a finite-distributive-lattice/prime-filter construction producing normality witnesses. The independent referee wrote this proof; the later coherent referee provided another reconstruction. This theorem includes **pointless** compact locales, not merely coherent ones.

**Coherent consequence (E):** \(\mathcal D=\mathcal U\) iff \(K(L)\) is a **normal bounded distributive lattice**, equivalently every prime ideal lies in a unique maximal ideal (**pm** orientation). It is the order dual of the conormal/mp criterion for \(\mathcal I=\mathcal U\). Beware: Cornish used “normal” for a condition the project's Georgescu-based terminology calls *conormal*.

**Compact functional collapse:** \(\mathcal D=\mathcal U\Rightarrow\mathcal U=\mathcal F\) for compact frames, via normality and the established point-free Urysohn lemma. **E modulo that cited lemma**. There is a **continuous, noncompact counterexample** with \(\mathcal D=\mathcal U\subsetneq\mathcal F\), so this conclusion cannot be exported without compactness.

**Heredity:** \(\mathcal D=\mathcal U\) is **closed-hereditary** for arbitrary locales; \(\mathcal D(Z)=\mathcal D(X)\wedge Z^2\) for a closed sublocale \(Z\), and restriction of \(\mathcal U\) gives the requisite inclusion. It is **not open-hereditary**, already for finite posets. **E(referee-derived)**; preserve the corrected closed-sublocale pullback proof, which is not the same as unrestricted commutation of fitting with restriction to an *open* part (Arrieta's example shows the latter fails).

**Noncompact normality is a genuinely different question.** For a classically continuous **normal** frame, \(\mathcal D=\mathcal U=\mathcal F\) by local compactness/sobriety and ordinary point separation (**I**, with standard spatial-product dependency). For arbitrary noncompact frames, **normal \(\Rightarrow\mathcal D=\mathcal U\) remains O**: normality proves the displayed identity for *finite* covers, not for arbitrary infinite covers. The converse is false without compactness: regular nonnormal spaces have \(\mathcal D=\mathcal U=\Delta\) but need not be normal. Do not equate this question with the disproved unrestricted \(\mathcal D=\mathcal U\Rightarrow\mathcal U=\mathcal F\).

**Internal transitivity:** \(\mathcal D=\mathcal U\) implies \(\mathcal U\) is an internal equivalence relation in compact locales (then \(\mathcal U=\mathcal F\)) and classically continuous locales (direct topological proof plus spatiality). The all-frame implication remains **O**. An old putative universal absorption argument \(\mathcal I\circ\mathcal U\le\mathcal U\) was **withdrawn**: it mistakenly treated disjointness as farness. Do not use it. Source: [transitivity note](https://github.com/mkkinyon/locales/blob/main/A-D-U-transitivity-2026-10-21.md).

**Stability under operations:** Arbitrary coproducts of **coherent frames** satisfying \(\mathcal D=\mathcal U\) retain equality (normal compact-open lattices under spectral product); finite coproducts of **continuous** frames satisfying it also retain equality, with local-compact-sober product hypotheses. The unrestricted arbitrary-frame-coproduct question remains **O**. Source: [D-U coproduct study](https://github.com/mkkinyon/locales/blob/main/A-coproduct-stability-D-U-2026-10-21.md).

## 3. The class W = U: a genuine infinitary closure/fitting interchange

Let \(\mathscr B=\{w\in Q:\delta^*(w)=1\}\), the filter of diagonal neighborhoods. The repository establishes, for **every frame**, the highly useful identity
\[
 \boxed{d_{\mathcal U}=\bigvee_{w\in\mathscr B}w^*},\qquad
 \boxed{\mathcal U=\bigwedge_{w\in\mathscr B}\operatorname{cl}(O(w))}.
\]
Indeed \(w\) is bounded below by the square-open of the induced diagonal cover; a rectangle disjoint from \(w\) has far coordinates. Conversely, if \(a^*\vee b^*=1\), then \((a\boxtimes b)^*\in\mathscr B\). Consequently \(\mathcal W=\mathcal U\) is exactly the **specialized commutation**
\[
 \boxed{\operatorname{cl}\bigl(\bigwedge_{w\in\mathscr B}O(w)\bigr)
 =\bigwedge_{w\in\mathscr B}\operatorname{cl}(O(w))}.
\]
This is **not** an assertion that closure commutes with arbitrary intersections of sublocales.

### 3.1 Diagonal-neighborhood pre-nucleus

Define \(\Phi:Q\to Q\) by
\[
 \Phi(q)=\bigvee_{w\in\mathscr B}(w\to q).
\]
Because \(\mathscr B\) is a filter, \(\Phi\) is a **pre-nucleus** (monotone, inflationary, preserves finite meets). Its fixed elements form the frame of \(\mathcal D\), and its transfinite idempotent closure is the nucleus \(j_{\mathcal D}\). In particular,
\[
 \Phi(0)=d_{\mathcal U},\qquad j_{\mathcal D}(0)=d_{\mathcal W}.
\]
It follows that
\[
 \boxed{\mathcal W=\mathcal U\iff\Phi(d_{\mathcal U})=d_{\mathcal U}
 \iff (\forall w\in\mathscr B)\ (w\to d_{\mathcal U})=d_{\mathcal U}.}
\]
Equivalently, **every open neighborhood of the diagonal is dense when restricted to \(\mathcal U\)**. By Isbell's least dense sublocale \(\mathfrak B(\mathcal U)\), another equivalent condition is \(\mathfrak B(\mathcal U)\le\mathcal D\). These results are **E** as part of the October 24 externally reviewed W/U package, subject to the standard pre-nucleus/Isbell inputs. The full \(\Phi\) operator is essentially the **existing \(\kappa_L\) construction of Arrieta–Picado–Pultr (2022)**, not a new named operator. Sources: [nucleus criterion](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-nucleus-criterion-2026-10-24.md), [W/U reconciliation](https://github.com/mkkinyon/locales/blob/main/A-WU-external-audit-reconciliation-2026-10-24.md).

### 3.2 The binary versus infinitary distinction

For \(a\vee b=1\), write \(v(a,b)=a\boxtimes a\vee b\boxtimes b\). The identity
\[
 v(a,b)^*=a^*\boxtimes b^*\vee b^*\boxtimes a^*
\]
implies, in **all frames**, that
\[
 d_{\mathcal U}=\bigvee_{a\vee b=1}v(a,b)^*,\quad
 \mathcal U=\bigwedge_{a\vee b=1}\operatorname{cl}(O(v(a,b))).
\]
The **closures** of binary diagonal neighborhoods already recover \(\mathcal U\), but the **opens themselves** need not be shown to recover \(\mathcal D\) in arbitrary frames.

If \(L\) is **compact**, every diagonal neighborhood contains the square-open of a *finite* cover, and the finite-cut identity
\[
 \bigvee_{i=1}^n c_i\boxtimes c_i
 =\bigwedge_{S\subseteq\{1,\ldots,n\}}
 v\Bigl(\bigvee_{i\in S}c_i,\ \bigvee_{i\notin S}c_i\Bigr)
\]
reduces its fitted hull to binary cover neighborhoods. Thus in compact frames
\[
 \boxed{\mathcal W=\mathcal U\iff (\forall a\vee b=1)\quad v(a,b)\to d_{\mathcal U}=d_{\mathcal U}.}
\]
Contrast \(\mathcal D=\mathcal U\iff v(a,b)\vee d_{\mathcal U}=1\) (same compact hypothesis). The first asserts **density** inside \(\mathcal U\), the second **total coverage**. This distinction is mathematically central. The W/U referee approved the finite-filter package; note that binary testing \(\mathcal W=\mathcal U\) in an arbitrary **noncompact** frame remains an open reduction, not a theorem. Sources: [binary cover](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-binary-cover-reduction-2026-10-24.md), [external reconciliation](https://github.com/mkkinyon/locales/blob/main/A-WU-external-audit-reconciliation-2026-10-24.md).

### 3.3 The finite-cover intermediate D₂ and W₂

Let \(\mathcal D_2=\bigwedge_{\mathcal C\text{ finite cover}}O(w_{\mathcal C})\), equivalently the fitted sublocale generated by all binary square-cover neighborhoods; \(\mathcal W_2=\operatorname{cl}(\mathcal D_2)\). Then
\[
 \mathcal D\le\mathcal D_2,\qquad
 \mathcal W\le\mathcal W_2\le\mathcal U.
\]
The finite-cover operator
\[
 \Phi_2(q)=\bigvee_{\mathcal C\text{ finite cover}}(w_{\mathcal C}\to q)
\]
is a pre-nucleus (using the filter of opens generated by the finite square neighborhoods), with \(\Phi_2(0)=d_{\mathcal U}\), and
\[
 \boxed{\mathcal W_2=\mathcal U\iff\Phi_2(d_{\mathcal U})=d_{\mathcal U}.}
\]
For **compact** frames \(\mathcal D=\mathcal D_2\) and \(\mathcal W=\mathcal W_2\) automatically. The general implications
\[
 \boxed{\mathcal W_2=\mathcal U\ \Longrightarrow?\ \mathcal W=\mathcal U},
 \qquad
 \boxed{\mathcal W_2=\mathcal W\quad\text{for all }L?}
\]
remain **O**; the second is strictly stronger. Earlier examples distinguish \(\mathcal D<\mathcal D_2\) (a Scott/Cantor model) from \(\mathcal W<\mathcal W_2\) (no confirmed example). **Do not treat a strict fitted-hull distinction as evidence of a strict closure distinction.**

### 3.4 Known strictness and corrected examples

- **Coherent frames** satisfy \(\mathcal W=\mathcal U\), even when \(\mathcal D\ne\mathcal U\). This follows from the externally reviewed coherent equality \(\mathcal U=\operatorname{cl}(\mathcal D)\).
- **Noncoherent compact** examples satisfy \(\mathcal W<\mathcal U\); the externally audited post-V three-boundary-point example even has \(\mathcal W=\mathcal I<\mathcal U=\mathcal V=\mathcal F\).
- The **two-apex model** in the October 24 W/U follow-up has \(\mathcal I<\mathcal W=\mathcal W_2<\mathcal U\), with the nonregular boundary explicitly described. The repository subsequently corrected its topological status: it is **compact**, not noncompact. Keep the corrected classification and proof dependencies; this was a *post-referee* reconciliation of the referee's new example, so use **I(referee-informed)** rather than claiming blind certification of the exact refined chain.
- If the localic square is **fit**, then \(\mathcal D=\Delta\) and \(\mathcal W=\mathcal I\), so \(\mathcal W=\mathcal U\iff\mathcal I=\mathcal U\). Fitness of products is established background, not a new project theorem.

### 3.5 Referee findings not to promote

The W/U referee's **blanket** assertion that finite closed subsets of an Alexandrov space are regular closed is false, although the specific finite-poset conclusion for \(\mathcal U\) survives by a different proof. More importantly, its purported rectangle criterion for a hyperconnected coordinate \(u\boxtimes v\le d_{\mathcal U}\iff a^*\vee v^*=1\) is false: a rectangle can lie in a *join* of far rectangles without being far itself. The October 24 reconciliation supplies the counterexample and excludes the dependent obstruction conjecture. Do not silently re-import either claim into the inventory.

## 4. Comparative dependency table

| Question | Exact all-frame formulation | Familiar complete characterization | Preservation | Status / key obstruction |
|---|---|---|---|---|
| \(\mathcal I=\mathcal U\) | Orthogonality completion of far pairs equals disjointness | Coherent: conormal (mp); frame–coframe: extremally disconnected | All frame coproducts/products; open sublocales. Not general closed sublocales | Strongest general structure; cp-ideal representation is the main imported tool |
| \(\mathcal D=\mathcal U\) | \(d_{\mathcal U}\vee w_{\mathcal C}=1\) for **all** covers | Compact: normal; coherent: normal compact-open lattice (pm) | Closed sublocales; coherent coproducts. Not general opens | Normality for arbitrary noncompact frames and internal transitivity remain open |
| \(\mathcal W=\mathcal U\) | \(\Phi(d_{\mathcal U})=d_{\mathcal U}\): all diagonal opens dense in \(\mathcal U\) | Coherent: automatic; compact: binary-density test | No comparably broad arbitrary-frame classification | Infinitary full-vs-finite diagonal neighborhoods; \(\mathcal W_2\Rightarrow\mathcal W\) open |

**Universal implications:** \(\mathcal D=\mathcal U\Rightarrow\mathcal W=\mathcal U\); \(\mathcal W=\mathcal U\not\Rightarrow\mathcal D=\mathcal U\), already in finite coherent examples. Neither \(\mathcal I=\mathcal U\) nor \(\mathcal D=\mathcal U\) universally implies the other (finite forks and their duals). These are elementary consequences of the hierarchy and finite examples, not independent new theorems.

## 5. Proposed inventory entries and next editorial step

Suggested new rows (to be inserted in v0.4):

- **K1a (I):** all-frame \(\mathcal I=\mathcal U\) orthogonality completion and unary-polar characterization.
- **K1b (E):** open heredity, failure of closed heredity, arbitrary coproduct and product stability (with explicitly repaired infinite-family lemma).
- **K1c (E):** coherent conormal/mp, algebraic compact-element, frame–coframe extremal-disconnected criteria.
- **K2a (E):** all-cover diagonal-square criterion for \(\mathcal D=\mathcal U\).
- **K2b (E/referee-derived):** compact normality; coherent normal/pm; compact functional collapse.
- **K2c (E/referee-derived):** closed heredity of \(\mathcal D=\mathcal U\), open heredity fails.
- **K2d (I/O):** noncompact normal/continuous positive cases vs all-frame open questions, D=U transitivity, arbitrary coproduct preservation.
- **K3a (E):** all-frame \(\mathcal U=\bigwedge_{w\in\mathscr B}\operatorname{cl}(O(w))\), \(\Phi\)-fixedpoint and Isbell density tests for \(\mathcal W=\mathcal U\).
- **K3b (E):** binary generation of \(\mathcal U\) always and binary tests for \(\mathcal W=\mathcal U\) in compact locales.
- **K3c (E/O):** finite-cover \(\Phi_2\) calculus; \(\mathcal W_2=\mathcal U\Rightarrow\mathcal W=\mathcal U\) and \(\mathcal W_2=\mathcal W\) open.
- **K3d (E/I):** strict \(\mathcal W<\mathcal U\) examples and corrected compact two-apex example.

These entries are deliberately more granular than v0.3's six K-rows. **No mathematical search is initiated here.** The next inventory section should probably deal with the large \(\mathcal V\)-rank family separately, selecting only claims for which the final proof and the corresponding audit can be located.

## 6. Source index and claims not to recycle

Primary source notes: [structural I/U](https://github.com/mkkinyon/locales/blob/main/A-I-equals-U-structural-study.md), [I/U coproducts](https://github.com/mkkinyon/locales/blob/main/A-coproduct-preservation-I-U.md), [D/U covers](https://github.com/mkkinyon/locales/blob/main/A-D-equals-U-first-results-2026-10-21.md), [D/U transitivity](https://github.com/mkkinyon/locales/blob/main/A-D-U-transitivity-2026-10-21.md), [noncompact normality](https://github.com/mkkinyon/locales/blob/main/A-noncompact-normality-D-U-2026-10-21.md), [W/U nucleus](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-nucleus-criterion-2026-10-24.md), [W/U binary](https://github.com/mkkinyon/locales/blob/main/A-W-equals-U-binary-cover-reduction-2026-10-24.md). Audits and repairs: [October 21 reconciliation](https://github.com/mkkinyon/locales/blob/main/A-external-audit-reconciliation-2026-10-21.md), [October 24 W/U reconciliation](https://github.com/mkkinyon/locales/blob/main/A-WU-external-audit-reconciliation-2026-10-24.md), [October 24 post-V reconciliation](https://github.com/mkkinyon/locales/blob/main/A-postV-external-audit-reconciliation-2026-10-24.md).

**Superseded wording to eliminate in a future consolidated manuscript (without altering historical files):** “\(\mathcal D=\mathcal U\Rightarrow\mathcal U=\mathcal F\) open”; “normal frame implies \(\mathcal D=\mathcal U\) for all locales”; “arbitrary finite closed sets are regular closed”; “binary conditions define \(\mathcal D\) without compactness”; “\(\mathcal D_2>\mathcal D\) means \(\mathcal W_2>\mathcal W\)”; “the two-apex W/U witness is noncompact”; and the withdrawn universal \(\mathcal I\mathcal U\)-absorption argument.