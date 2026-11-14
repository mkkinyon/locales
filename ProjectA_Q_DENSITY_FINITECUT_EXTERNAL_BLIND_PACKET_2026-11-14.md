# Project A — external blind mathematical packet: density, finite cuts, Scott controls and Boolean visibility

**14 November 2026 — independent first reading requested.**

**Status:** Research-in-progress. The universal questions Q and Q′ below are **open**. The theorems and countercontrols in this packet have not been independently externally refereed. The proofs are included so no unpublished repository files need be obtained. The independent prompt is in the companion document; **the separate internal adversarial audit is excluded**.

This compilation deliberately distinguishes: (i) density inside a *relatively open* part of the **canonical** finite-cover closed hull \(W_2\); (ii) density on an arbitrary, possibly nowhere-dense **closed** relation; and (iii) a weak Boolean compatibility defect that may have no ordinary points.

## 0. Definitions and notation conventions

The following is the task-relevant, trimmed **CORE + Question Q/Q′ module** copied from our modular reusable introduction `ProjectA_EXTERNAL_AUDIT_PACKET_DEFINITIONS_BOILERPLATE_2026-11-13.md`. It is placed *inside* this packet so the definitions are not merely external hyperlinks.

### 1. Ambient conventions

We work in classical set theory with choice unless stated otherwise. All spaces called **locales** are objects of \(\mathbf{Loc}\), and \(\mathcal O(X)\) denotes the frame of opens of a locale \(X\). A locale map \(f:T\to X\) has an inverse-image frame homomorphism \(f^*:\mathcal O(X)\to\mathcal O(T)\), preserving finite meets and arbitrary joins.

All squares and products are **localic**, not automatically the locale of the ordinary point-set product. We write
\[
  X^2=X\times X,\qquad
  \mathcal O(X\times Y)=\mathcal O(X)\otimes\mathcal O(Y),
\]
and \(a\boxtimes b\) for the basic rectangle determined by frame elements \(a,b\). Thus for \(f,g:T\to X\),
\[
  (f,g)^*(a\boxtimes b)=f^*(a)\wedge g^*(b).
\]

The diagonal sublocale of \(X^2\) is \(\Delta_X\). Sublocale inequalities \(S\le T\) mean **inclusion of sublocales**; meets and joins of sublocales are not to be confused with the meet and join operations in the frame \(\mathcal O(X^2)\).

### 2. Open/closed sublocales, closure, and fitting

For an ambient locale \(P\) and \(w\in\mathcal O(P)\), denote by \(O_P(w)\) the open sublocale determined by \(w\), and by \(C_P(w)\) its complementary **closed sublocale**. These are complements in the sublocale lattice. Write \(O(w),C(w)\) when \(P\) is unambiguous. **The symbol \(C(w)\) does not mean the closure of the open \(O(w)\).**

For a sublocale \(S\subseteq P\), let \(\operatorname{cl}_P(S)\) be the least closed sublocale containing \(S\), and
\[
  \operatorname{fit}_P(S)
  =\bigwedge\{O_P(w):S\le O_P(w)\}
\]
its fitting (least fitted sublocale containing \(S\)). We omit ambient subscripts when clear. A sublocale \(S\) is **dense** in \(P\) if \(\operatorname{cl}_P(S)=P\). Its Booleanization \(B(P)\) is the double-negation sublocale, the least dense sublocale of \(P\).

### 3. Covers and diagonal cover squares

An **open cover** \(\mathscr C\) of \(X\) is a family in \(\mathcal O(X)\) with \(\bigvee\mathscr C=1\); it is not implicitly finite. Put
\[
  w_{\mathscr C}
    =\bigvee_{c\in\mathscr C}c\boxtimes c
    \in\mathcal O(X^2).
\]
The \(w_{\mathscr C}\) are cofinal among open neighbourhoods of \(\Delta_X\): if \(\Delta_X\le O(w)\), then \(w_{\mathscr C}\le w\) for some cover \(\mathscr C\). In particular,
\[
  D(X)=\operatorname{fit}(\Delta_X)
     =\bigwedge_{\mathscr C\text{ cover}}O(w_{\mathscr C}),\qquad
  D_2(X)=\bigwedge_{\mathscr F\text{ finite cover}}O(w_{\mathscr F}).
\]
Here \(D\) is the **full fitted diagonal**, whereas \(D_2\) uses only **finite** covers; the subscript 2 does **not** mean a second iteration.

Equivalently, \((f,g):T\to X^2\) factors through \(D(X)\) exactly when
\[
  \bigvee_{c\in\mathscr C} f^*(c)\wedge g^*(c)
    =1_{\mathcal O(T)}
  \quad\text{for every cover }\mathscr C.
\]
For \(D_2(X)\), test only finite covers. Factorization through \(\Delta_X\) means \(f=g\). Always \(\Delta_X\le D(X)\le D_2(X)\).

### 4. Closed hulls and separation terminology

Define the **closed hulls**
\[
  W(X)=\operatorname{cl}_{X^2}D(X),\qquad
  W_2(X)=\operatorname{cl}_{X^2}D_2(X).
\]
Thus \(W\le W_2\). Equality \(D=D_2\) is stronger than \(W=W_2\); a nonzero closed piece of \(D_2\) excluded by \(D\) does **not**, by itself, imply unequal closed hulls.

A locale is **F-separated** if its diagonal is fitted, equivalently \(D(X)=\Delta_X\). It is **strongly Hausdorff** (Isbell) if its **localic diagonal is a closed sublocale** of \(X^2\). Ordinary Hausdorffness of a point-set space must not be silently substituted for strong Hausdorffness of its locale.


### 5. Cover pre-nuclei, Q and Q′

On \(P=\mathcal O(X^2)\), with Heyting implication \(\to\), put
\[
  \Phi(q)
   =\bigvee_{\mathscr C\text{ cover}}
      (w_{\mathscr C}\to q),\qquad
  \Phi_2(q)
   =\bigvee_{\mathscr F\text{ finite cover}}
      (w_{\mathscr F}\to q).
\]
The rank-zero element is
\[
  z=\Phi(0)=\Phi_2(0),\qquad U(X)=C_{X^2}(z).
\]
The finite-cover closed hull is \(W_2(X)=C_{X^2}(d)\), where \(d=\Phi_2^\infty(0)\) denotes the stabilized transfinite iteration from \(0\).

The two **universal open questions** (status as of 13 November 2026) are:

- **Q:** For every locale \(X\), does \(\Phi_2(z)=z\) imply \(\Phi(z)=z\)? Equivalently, does \(W_2(X)=U(X)\) imply \(W(X)=U(X)\)?
- **Q′:** For every locale \(X\), does \(W_2(X)=W(X)\)? Equivalently, is \(B(D_2(X))\le D(X)\) for every \(X\)?

Q′ would imply Q. Neither is known in general; an example with \(D_2(X)\ne D(X)\) alone disproves **neither** question.

For a full cover \(\mathscr C\), define the **weak defect**
\[
  T_{\mathscr C}
     =D_2(X)\wedge C_{X^2}(w_{\mathscr C}).
\]
This sublocale may be nonzero even if Q′ holds on \(X\). The relevant issue is whether \(T_{\mathscr C}\) has **nonzero relative interior in \(D_2(X)\)**. Equivalently, the Q′ criterion asks that every such relatively closed defect be **nowhere dense in \(D_2(X)\)**. Relative openness/density must be checked in \(D_2(X)\), not in \(X^2\) by ordinary points.


## 0A. Hierarchy and exact logical status

For every \(X\), \(D\le D_2\) and \(W\le W_2\). The closed-atomic theorem in Appendix A gives a positive class with \(D=D_2\). Conversely, the Scott example of Part IV exhibits \(D\lt D_2\) but \(W=W_2=X^2\); it therefore demonstrates why a weak defect alone is not a negative answer to Q′. The same example shows there may be a **noncanonical** \(\Phi_2\)-fixed open that is not \(\Phi\)-fixed, even if Q′ holds; it is *not* legitimate to strengthen Q′ to equality of all fixed-point sets.

The four research notes reproduced below are dated 13 November. They are presented in the logical progression from necessary density conditions, through relative spatial Baire tests, to an exact finite-cut identity and a stronger Scott closed-relation test. Their section numbers are **local to each part**.

---

## I. Relative monochromatic density and local chromatic obstruction

# Project A / Q′ — locally infinite-chromatic endpoint squares on every finite-fixed marked hole

**13 November 2026 (America/Denver); INTERNAL bounded continuation, not externally audited. Q and Q′ OPEN.** After the [canonical spectral predecessor-lift no-go](ProjectA_Q_CANONICAL_SPECTRAL_PREDECESSOR_LIFT_NO_GO_2026-11-13.md), this note removes predecessor witnesses altogether and studies **endpoint matching squares directly inside the closed finite-cover hull**. It strengthens the locality of the previously known chromatic obstruction; no claim that infinite chromaticity alone resolves Q′.

## 0. Set-up

Let \(L=\mathcal O(X)\), \(P=L\oplus L=\mathcal O(X^2)\), and for each cover C of X let \(w_C=\bigvee_{c\in C}c\boxtimes c\). Let
\[
\Phi_2(q)=\bigvee_{F\text{ finite X-cover}}(w_F\to q).
\]
Take **any** \(d\in P\) fixed by \(\Phi_2\). Let \(Y=\mathfrak c_{X^2}(d)\), with \(\mathcal O(Y)=\uparrow d\). For a possibly infinite cover \(C=\{c_i:i\in I\}\), put
\[
\rho=w_C\to d,\qquad E=\mathfrak o_Y(\rho). \tag{0.1}
\]
Thus E is the largest Y-open disjoint from every diagonal-index square \(c_i\boxtimes c_i\). Q′ corresponds to \(d=d_0=\Phi_2^\infty(0)\), \(Y=W_2\), and asks E=0 for every C. Q rank-one corresponds to \(d=z_1\), provided \(\Phi_2(z_1)=z_1\).

Recall the finite-fixed dense-open identity: for any **finite cover** F, \(w_F\vee d\) is dense in Y, because \((w_F\to d)=d\).

For any nonzero open sublocale \(V\le E\), define an **undirected cross-link graph** \(\Gamma_V\) with vertex set I, with \(\{i,j\}\), \(i\ne j\), an edge precisely when
\[
\boxed{V\wedge\mathfrak o_Y\bigl((c_i\boxtimes c_j)\vee(c_j\boxtimes c_i)\bigr)\ne0.} \tag{0.2}
\]
This is a localic, *open-chart* definition: nonzero means a nonzero open sublocale of V, **not** existence of ordinary points.

## 1. Local infinite chromaticity as a density theorem

**Theorem 1.1 (monochromatic cross-rectangles are dense).** Let d be \(\Phi_2\)-fixed, C any X-cover, and E as in (0.1). For **every** nonzero open \(V\le E\) and **every** finite coloring \(\kappa:I\to\{1,\ldots,m\}\), the V-open
\[
\boxed{
\bigvee_{\substack{i\ne j\\\kappa(i)=\kappa(j)}}
\mathfrak o_V(c_i\boxtimes c_j)
\quad\text{is dense in }V.} \tag{1.1}
\]
Consequently
\[
\boxed{\chi(\Gamma_V)=\infty\quad\text{for every nonzero open }V\le E.} \tag{1.2}
\]

*Proof.* For each color \(\ell\) put \(b_\ell=\bigvee_{\kappa(i)=\ell}c_i\). Since C covers X, the **finite** family \(B=\{b_1,\ldots,b_m\}\) covers X. Hence its square open
\[
w_B=\bigvee_{\ell=1}^{m}b_\ell\boxtimes b_\ell
 =\bigvee_{\kappa(i)=\kappa(j)}c_i\boxtimes c_j \tag{1.3}
\]
is dense in Y, and its restriction to the Y-open V is dense in V.

On E and hence V, the terms with i=j vanish, since \(\rho\wedge(c_i\boxtimes c_i)\le d\). Therefore the restriction of (1.3) to V is **exactly** the open in (1.1), which must be dense.

If \(\Gamma_V\) admitted the finite coloring \(\kappa\), every monochromatic off-diagonal rectangle would restrict to zero on V by (0.2); their join would be zero, contradicting density in nonzero V. □

**Corollary 1.2 (concrete endpoint finite-coloring exclusion).** For any fixed d and cover C, if **each nonzero open chart** of the potential defect locus \(\mathfrak o_Y(w_C\to d)\) contains a nonzero subchart \(V\) on which the cross-link graph (0.2) has finite chromatic number, then the defect locus is zero. Equivalently, a single nonzero open C-hole would force **pervasive** infinite chromaticity on all its nonzero open subcharts.

For Q′, \(Y=W_2\), so this is a fully **relative** endpoint-density test. It neither projects a nowhere-dense spectral predecessor boundary nor replaces localic opens with ordinary pairs.


### 1.3 An elementary hyperconnected-patch eliminator

Call a nonzero locale H **hyperconnected** (irreducible) when any two nonzero opens of H meet nontrivially.

**Corollary 1.3.** A nonzero marked hole E for any \(\Phi_2\)-fixed d cannot contain a nonzero hyperconnected open sublocale. Consequently, if \(Y=\mathfrak c(d)\) has a **\(\pi\)-base of hyperconnected opens** (every nonzero open contains one), then \(\Phi(d)=d\). In particular, if \(W_2\) has such a \(\pi\)-base, Q′ holds for X. The rank-one analog applies when \(z_1\) is finite-fixed and \(\mathfrak c(z_1)\) has such a \(\pi\)-base.

*Direct proof using binary covers.* Suppose \(0\ne V\le E\) is hyperconnected. Restrict the two product projections to V, giving frame maps \(h,k:L\to\mathcal O(V)\). For each c∈C,
\[
h(c)\wedge k(c)=0_V,
\]
because V lies in the C-hole. Hyperconnectedness forces \(h(c)=0\) or \(k(c)=0\). Partition C into \(C_h=\{c:h(c)\ne0\}\) and its complement. Put \(u=\bigvee C_h\), \(v=\bigvee(C\setminus C_h)\); \(\{u,v\}\) is a binary X-cover. But \(k(u)=0\) and \(h(v)=0\), so its matching square restricts to **zero** on V, contradicting the density of every finite-cover square on the nonzero Y-open V. □

**Adversarial scope check.** This is a geometric rephrasing of an **already known atomlessness necessary condition**, not an independent route past it. For any locale E, “E has no nonzero hyperconnected open sublocale” is equivalent to “the double-negation Booleanization \(B(E)\) is atomless”: an atom of \(B(E)\) is represented by a nonzero hyperconnected open of E, and conversely any hyperconnected open has a two-element Booleanization. The original Boolean weak-defect argument already rules out atoms. The \(\pi\)-base corollary is a convenient sufficient condition to check **on \(W_2\)**, not evidence that the general case is solved.

## 2. The Boolean no-go and pointwise/local distinction

**Adversarial check A (no extra Boolean equation).** Any nonzero Boolean finite-cover-compatible pair \(h,k:L\to M\) with \(h(c_i)\wedge k(c_i)=0\) for all i also has an infinite-chromatic cross-link graph defined by nonzero Boolean values \(h(c_i)\wedge k(c_j)\vee h(c_j)\wedge k(c_i)\). Indeed the finite block cover B from (1.3) has matching value top while its diagonal-index terms vanish. So infinite chromaticity **on a Boolean weak defect**, by itself, is old information and **does not prove Q′**. The new emphasis in Theorem 1.1 is the **every-nonzero-open-subchart density** of the monochromatic union inside an actual marked E⊂W₂.

**Adversarial check B (ordinary points do not provide a local coloring).** If (x,y) is an ordinary pair in E for a spatial model of Y, then no c_i contains both x and y. At that one pair, the cross-incidence graph is bipartite between the disjoint index sets \(I_x=\{i:x\in c_i\}\) and \(I_y=\{i:y\in c_i\}\). This **pointwise** two-colorability does not imply a *single finite coloring* works on any nonzero neighborhood V. The earlier [hereditary-Baire point-finite/chromatic no-go note](ProjectA_Q_BAIRE_POINTFINITE_RIGIDITY_AND_FAR_REDUNDANCY_2026-11-12.md), §5, gives an abstract graph family that is pointwise 1-colorable but locally infinite-chromatic everywhere. The abstract graph was **not** claimed to arise from the specific endpoint cross-link relation (0.2), so there remains room to exploit the actual square geometry.

**Adversarial check C (Scott weak defects).** For the completed partial-function Scott locale, a Boolean weak finite/full defect exists and has the corresponding infinite chromatic obstruction, while \(W=W_2=X^2\) and there is **no nonzero marked open E**. Thus a closed weak defect does not test the open-chart hypothesis of Theorem 1.1.

## 3. Research decision

The most faithful graph-theoretic density question is now:

> **Endpoint local-coloring problem.** In the **special** geometry of the finite fitted-diagonal closure \(W_2(X)\), can a nonzero open chart whose every ordinary point-pair has two-colorable C-incidence nevertheless have \(\chi(\Gamma_V)=\infty\) on every nonzero subchart, while *all* same-index squares vanish?

An affirmative example would be a candidate for an actual Q′ hole only if finite-cover compatibility and **nonzero relatively open position** in W₂ are verified. A negative theorem for the actual cross-link graphs (not arbitrary abstract graphs) would prove Q′ for the corresponding class. This is not achieved here.

Do not replace the endpoint cross-link graph by a prime-predecessor graph: the canonical countable-V example shows those notions are inequivalent. Avoid presenting (1.1) as a new constraint beyond finite compatibility; its added value is precise **localic localization and density**.

**Status:** Direct frame/distributivity calculation internally checked; not externally audited. Universal Q/Q′ OPEN.


---

## II. Spatial Baire countable finite-test criterion

# Project A / Q′ — spatial Baire plus countable finite-cover tests forces matching-square density

**13 November 2026 (America/Denver); NEW INTERNAL bounded sufficient criterion, not externally audited. Q/Q′ OPEN.** This is a direct, genuinely **relative Baire argument inside \(W_2\)**, complementing [localic chromatic density](ProjectA_Q_RELATIVE_CHROMATIC_DENSITY_ALL_FINITE_FIXED_2026-11-13.md) and the [canonical spectral predecessor-lifting no-go](ProjectA_Q_CANONICAL_SPECTRAL_PREDECESSOR_LIFT_NO_GO_2026-11-13.md). It deliberately does **not** assume that weak Boolean defects have ordinary points.

## 0. Set-up

Let \(L=\mathcal O(X)\), \(P=L\oplus L\), \(d_0=\Phi_2^\infty(0)\), and
\[
Y=W_2(X)=\mathfrak c_{X^2}(d_0).
\]
For any finite X-cover F put \(w_F=\bigvee_{f\in F} f\boxtimes f\). Since \(\Phi_2(d_0)=d_0\), the restricted open
\[
U_F=\mathfrak o_Y(w_F)
\]
is **dense** in Y, equivalently \(w_F\to d_0=d_0\). For an arbitrary X-cover C let \(U_C=\mathfrak o_Y(w_C)\). Q′ asserts that **every** \(U_C\) is dense in Y.

**Important hypothesis used below:** Y is a **spatial locale whose ordinary representing topological space is Baire**. The statement “Y is localic Baire” without spatiality does not suffice for the pointwise step.

## 1. Countable separator theorem

**Theorem 1.1 (countable finite-test Baire criterion).** Fix an arbitrary cover C of X. Suppose there is a **countable family of finite X-covers** \((F_n)_{n<\omega}\) with this pointwise detection property:

> For every *ordinary locale point* \(z:1\to Y\), if its endpoint pair \((x,y)\) does **not** lie in any common C-square \(c\boxtimes c\), then for some n it does **not** lie in \(w_{F_n}\).

Equivalently, as sets of ordinary Y-points,
\[
\boxed{\bigcap_{n<\omega}U_{F_n}\ \subseteq\ U_C.} \tag{1.1}
\]

Then
\[
\boxed{U_C\text{ is dense in }Y,\quad w_C\to d_0=d_0.} \tag{1.2}
\]
Thus C cannot witness a Q′ failure.

*Proof.* Every \(U_{F_n}\) is a dense **open** subset of the spatial Baire space Y. Their countable intersection is a dense \(G_\delta\) set \(G\subseteq Y\). By the assumed detection property \(G\subseteq U_C\). Hence the open \(U_C\) is topologically dense in Y. Because Y is spatial, this is precisely density of the corresponding open sublocale. □

This is not merely another support restriction: it constructs an actual **dense subset inside Y**, consisting of ordinary point-pairs that pass the selected finite-cover tests. The role of countability is to make the Baire theorem applicable. The hard step in applications is finding a countable test family that detects *all* C-bad ordinary Y-pairs.

**Corollary 1.2 (globally countable finite presentation).** If the finite-cover compatibility predicate on ordinary points of Y is captured by countably many finite covers \(F_n\)—i.e. every ordinary Y-pair respecting all F_n automatically respects **all finite X-covers**—then Q′ holds on X, provided Y is spatial Baire.

*Proof.* An ordinary point-pair respecting all finite X-covers respects **every** arbitrary cover C: otherwise partition C into the opens containing x and those not containing x; their two joins form a binary X-cover whose common-match value at (x,y) is zero. Thus the same countable family detects all C-bad pairs, and Theorem 1.1 applies cover by cover. □

In particular, if the entire frame L is **countable**, enumerate all finite X-covers to obtain a suitable family. More generally, a countably cofinal family of finite covers under refinement suffices. These are conditional examples; no claim that second countability of X alone gives such a cofinal family.

## 2. Countable point-finite covers: a second route to a known positive class

**Corollary 2.1 (countable, point-finite, spatial-Baire variant).** Suppose C=\(\{c_i:i<\omega\}\) is an **ordinarily point-finite** open cover of a spatial X, and Y=W₂ is spatial Baire. Then \(U_C\) is dense in Y.

*Proof.* For each finite \(S\subseteq\omega\), put
\[
a_S=\bigvee_{i\in S}c_i,\qquad b_S=\bigvee_{i\notin S}c_i.
\]
The two opens \(a_S,b_S\) form a binary X-cover. There are countably many such S. If an ordinary Y-point (x,y) is C-bad, let \(S=\{i:x\in c_i\}\), a **finite** set by point-finiteness. Then x belongs to \(a_S\) and not \(b_S\), while y belongs to \(b_S\) and not \(a_S\): C-badness ensures y belongs to no c_i with i∈S, and C being a cover ensures some other c_j contains y. Hence the binary cover \(\{a_S,b_S\}\) has no matching member at (x,y). These countably many binary covers meet Theorem 1.1's detection hypothesis. □

The earlier [hereditary-Baire point-finite rigidity theorem](ProjectA_Q_BAIRE_POINTFINITE_RIGIDITY_AND_FAR_REDUNDANCY_2026-11-12.md) proves the **stronger** \(D_2\le\mathfrak o(w_C)\) for *arbitrary cardinal* point-finite covers when X is hereditarily Baire and spatial, without requiring Y spatial Baire. Corollary 2.1 has **different hypotheses and a weaker conclusion**; it is not presented as a replacement or improvement of that theorem.

## 3. Why the extra spatiality cannot be omitted

A localic Baire theorem says the sublocale meet of countably many dense opens is dense. It does **not** produce ordinary points in the intersection when the locale is nonspatial. In the Q′ programme, dense pointless sublocales are a central possibility: Booleanizations of atomless locales can be dense yet have no ordinary locale points, and the branching Scott controls have \(D_2>D\) despite Q′ holding.

The proof of Theorem 1.1 has a precisely located non-pointfree step:
\[
\text{dense }G_\delta\text{ **of ordinary Y-points**}
\quad\Longrightarrow\quad
\text{pointwise binary-cover coarsening applies}.
\]
Without spatiality (or a replacement guaranteeing enough ordinary points in that particular intersection), that arrow is unavailable. The statement is therefore a **conditional spatial-Baire criterion**, not a universal proof of Q′.

The theorem also does **not** say that a countable basis of X yields countably cofinal finite covers, nor that W₂ is automatically spatial or Baire for all X.

## 4. Relation to local chromatic obstruction and research priority

A strong C-hole would produce a nonzero relatively open E⊂Y disjoint from \(U_C\). By [relative chromatic density](ProjectA_Q_RELATIVE_CHROMATIC_DENSITY_ALL_FINITE_FIXED_2026-11-13.md), every nonzero open chart V⊂E has an infinite-chromatic cross-link graph. The countable separator theorem supplies an *alternative* obstruction: in a spatial Baire Y, a **countable** family of finite-cover tests that separates all C-bad ordinary pairs makes such E impossible.

The actual open problem is to find **nontrivial classes** of frames/locales for which the C-bad pairs have a countable finite-test separating family, or to replace spatial Baire by a genuinely point-free density principle controlling the corresponding nonspatial Gδ intersection. These are actionable subproblems; no general result is claimed.

**Verification status:** internally checked pointwise Baire argument and binary coarsening; not externally audited. **Q and Q′ remain OPEN.**


---

## III. Incidence-profile Baire restriction and Polish control

# Project A / Q′ — relative Baire incidence-profile obstruction and a Polish countercontrol

**13 November 2026 (America/Denver); NEW INTERNAL density segment, not externally audited. Universal Q/Q′ OPEN.** This builds on the [countable finite-test criterion](ProjectA_Q_SPATIAL_BAIRE_COUNTABLE_FINITE_TEST_DENSITY_2026-11-13.md), the [relative tail theorem](ProjectA_Q_COVERWISE_SHRINKABILITY_AND_RELATIVE_TAIL_BAIRE_2026-11-13.md), and the [closed-atomic weak-defect no-go](ProjectA_Q_CLOSED_ATOMIC_SCATTERED_WEAK_DEFECT_NO_GO_2026-11-13.md).

## 0. Setting and pointwise qualification

Let \(L=\mathcal O(X)\), \(P=L\oplus L\), \(d\in P\) with \(\Phi_2(d)=d\), and \(Y=\mathfrak c_{X^2}(d)\). Every finite-cover matching square \(w_F\) restricts to a dense open in \(Y\).

Fix an arbitrary indexed \(L\)-cover \(C=\{c_i:i\in I\}\). Let
\[
E=\mathfrak o_Y(w_C\to d)
\]
be the largest relatively open \(C\)-hole; thus \(w_C|_E=0\) and all finite-cover squares remain dense on \(E\). To apply **ordinary** Baire category below, assume \(E\) is **spatial and Baire as a topological space**. This follows if \(Y\) is spatial Baire and \(E\) is a nonzero open sublocale, but is not automatic for a general localic \(W_2\).

For a point \(z:1\to E\), write \((x_z,y_z)\) for its two endpoint points of \(X\). Define
\[
I_x=\{i\in I:x\in c_i\},\qquad I_y=\{i\in I:y\in c_i\}.
\]
Because \(C\) covers, each \(I_x,I_y\) is nonempty; because \(E\) is a \(C\)-hole, \(I_{x_z}\cap I_{y_z}=\varnothing\).

## 1. Individual profiles are nowhere dense, in each coordinate

For every \(S\subseteq I\) define
\[
a_S=\bigvee_{i\in S}c_i,\qquad b_S=\bigvee_{i\notin S}c_i,\qquad
F_S=\{a_S,b_S\}.
\]
This is a **binary \(X\)-cover**. Let \(U_S\) be its matching-square open in \(E\); it is dense open because \(d\) is finite-fixed. Consequently
\[
N_S=E\setminus U_S
\]
is a closed nowhere-dense subset of the spatial Baire space \(E\).

**Theorem 1.1 (category-small incidence-profile fibers).** For every \(S\subseteq I\), each of the sets
\[
\{z\in E:I_{x_z}=S\},\qquad \{z\in E:I_{y_z}=S\}
\]
is contained in \(N_S\), hence is nowhere dense in \(E\).

*Proof.* If \(I_x=S\), then \(x\in a_S\), \(x\notin b_S\). Since \(I_x\cap I_y=\varnothing\) and \(C\) covers, \(y\notin a_S\), \(y\in b_S\). Therefore \((x,y)\) matches neither member of the binary cover \(F_S\). The argument with the coordinates swapped is identical. □

**Corollary 1.2 (local uncountability).** For every nonempty open \(V\subseteq E\), the sets of first-coordinate and second-coordinate incidence profiles attained on \(V\) are **both uncountable**. More precisely, for every countable family \(\mathcal A\subseteq\mathcal P(I)\), the set
\[
\bigcap_{S\in\mathcal A}(U_S\cap V)
\]
is a dense \(G_\delta\) subset of \(V\), all of whose points have **neither coordinate profile in \(\mathcal A\)**.

*Proof.* Each \(U_S\cap V\) is dense open in \(V\), and nonempty open subspaces of Baire spaces are Baire. Any point with either profile \(S\) belongs to \(N_S\), so lies outside \(U_S\). Countable Baire intersection yields the conclusion. □

**Corollary 1.3 (bounded profile class).** Fix a cover \(C\) and suppose \(Y=W_2\) is spatial Baire. If the first endpoint incidence-profile map has countable range on every ordinary point of \(Y\) (or merely on some open neighborhood of each point of the putative \(C\)-hole), then \(C\) cannot witness failure of Q′. In particular, if the sober point space of \(X\) is **countable** and \(W_2(X)\) is spatial Baire, then Q′ holds for \(X\).

*Scope:* Countability of ordinary points of \(X\) alone does **not** imply that \(W_2\) is spatial Baire. No such automatic property is claimed.

## 2. Countable-cover generic two-sided infinite incidence

**Proposition 2.1.** Suppose \(C=\{c_n:n<\omega\}\), and \(E\ne0\) is spatial Baire as above. Then a dense \(G_\delta\) subset of \(E\) consists of point-pairs \((x,y)\) with
\[
I_x\cap I_y=\varnothing,\qquad |I_x|=|I_y|=\aleph_0.
\]

*Proof.* For each \(n\), put \(t_n=\bigvee_{i\ge n}c_i\). The finite family
\(\{c_0,\ldots,c_{n-1},t_n\}\) covers \(X\). Its matching square is dense open on \(E\), whereas each square \(c_i\boxtimes c_i\) vanishes on \(E\). Hence the **tail square** \(t_n\boxtimes t_n\) restricts to a dense open of \(E\). The countable intersection of these tail-square opens is dense \(G_\delta\). Every point pair therein meets a \(c_i\) with \(i\ge n\) in *both* coordinates for every \(n\); both profile sets are infinite. Disjointness holds throughout \(E\). □

This is a **two-sided** and **relative-to-the-open-hole** version of earlier infinite-incidence statements on closed coordinate supports. It remains conditional on spatial Baire \(E\).

## 3. Polish countercontrol: finite color density does not suffice

Take the Polish space \(X=[\omega]^\omega\) of all infinite subsets of \(\omega\), with the subspace topology from Cantor \(2^\omega\). Let
\[
c_i=\{A\in X:i\in A\}\qquad(i<\omega),\qquad C=\{c_i:i<\omega\}.
\]
Each \(c_i\) is clopen, and \(C\) covers \(X\). Let
\[
R=\{(A,B)\in X\times X:A\cap B=\varnothing\}.
\]
It is a **nonempty closed Polish**, hence Baire, subspace of \(X^2\). Its restriction of the same-index matching open \(w_C\) is zero.

For **every finite coloring** \(\kappa:\omega\to\{1,\dots,m\}\), form the corresponding finite cover
\[
b_\ell=\bigcup_{\kappa(i)=\ell}c_i,\qquad B_\kappa=\{b_1,\dots,b_m\}.
\]
Then \(w_{B_\kappa}|_R\) is dense open in \(R\). Indeed every basic nonempty open chart of \(R\) fixes only finitely many coordinates of \(A,B\). At least one color class is infinite; choose two fresh distinct indices \(i,j\) of that color, prescribe \(i\in A\) and \(j\in B\), and complete to disjoint infinite sets. The resulting pair lies in the chart and matches \(b_{\kappa(i)}\). This argument works in every smaller basic chart, establishing density.

Also every nonempty open chart of \(R\) has continuum many first- and second-coordinate incidence profiles; the incidence sets are simply \(A,B\), and the charts admit continuum many disjoint infinite completions. Thus **all** of the preceding Baire profile and monochromatic chromatic constraints are modeled.

**But \(R\) fails full finite-cover density.** For each \(n\), the clopen binary \(X\)-cover
\[
F_n=\{c_n,X\setminus c_n\}
\]
has matching open *not dense* in \(R\): the nonempty \(R\)-open chart \(n\in A,\ n\notin B\) misses both matching squares. In fact \(X\) is zero-dimensional Hausdorff and \(D_2(X)=\Delta_X\), so \(R\cap W_2(X)=\varnothing\). This is **not** a counterexample to Q′.

**Lesson:** Even a Polish Baire bad-\(C\) relation with maximal profile complexity and density of every finite **color coarsening of \(C\)** need not be compatible with all finite **ambient \(X\)-covers**. Future density arguments must exploit those ambient cover tests, or the special fact that a genuine defect is a **nonzero open chart inside \(W_2\)**.

## 4. Priority and audit scope

- **Positive conditional fact:** A genuine spatial Baire \(C\)-hole has no locally countable incidence-profile range in either coordinate. Countable bad covers have comeagre two-sided infinite incidence.
- **Negative control:** All finite-coloring density information, even strengthened by spatial Polish Baire geometry and continuum incidence complexity, is insufficient.
- **Next mathematical test:** Find a useful class of finite \(X\)-covers *not generated by coarsening \(C\)* that detects a hole from local incidence behavior, without automatically assuming regularity or clopen separation.
- **Closed-atomic gate:** Any **weak** defect already requires atomless least closed coordinate supports by the separately audited theorem.

**Status: internally checked direct topological and frame calculations; no external audit. Q/Q′ universally OPEN.**


---

## IV. Finite-cut identity, Scott closed/Baire control, canonical visibility

# Project A / Q′ — binary-cover reduction, finite cut identity and closed-rectangle category formulation

**13 November 2026 (America/Denver); INTERNAL proof segment, not externally refereed. Universal Q/Q′ OPEN.** This continues the [relative Baire incidence-profile programme](ProjectA_Q_RELATIVE_BAIRE_INCIDENCE_PROFILES_POLISH_CONTROL_2026-11-13.md). The main gain is a **point-free exact reduction of all finite-cover tests to binary-cover tests**. Thus the ambient tests missing from the Polish countercontrol can themselves be taken binary, but need not arise as coarsenings of the bad cover C.

## 0. Notation

Let \(L=\mathcal O(X)\), \(P=L\oplus L=\mathcal O(X^2)\), and \(w_F=\bigvee_{f\in F}f\boxtimes f\) for a finite family \(F\). For a finite indexed family \(F=(f_1,\dots,f_n)\) and any subset \(S\subseteq[n]\), let
\[
u_S=\bigvee_{i\in S}f_i,\qquad v_S=\bigvee_{i\notin S}f_i,\qquad
B_S=\{u_S,v_S\}.
\]
When \(F\) covers \(1_L\), every \(B_S\) is a binary \(L\)-cover.

## 1. Exact finite-cut identity

**Theorem 1.1 (finite matching-square cut identity).** For every **finite cover** \(F=(f_1,\dots,f_n)\) in any frame \(L\),
\[
\boxed{\quad
w_F=\bigwedge_{S\subseteq[n]}w_{B_S}
=\bigwedge_{S\subseteq[n]}\bigl((u_S\boxtimes u_S)\vee(v_S\boxtimes v_S)\bigr)
\quad} \tag{1.1}
\]
as **opens in \(P=L\oplus L\)**. No spatiality hypothesis is used. Repetitions or empty members of \(F\) cause no problem.

*Proof.* In \(P\), put \(x_i=f_i\boxtimes1\) and \(y_i=1\boxtimes f_i\). These satisfy \(\bigvee_i x_i=\bigvee_i y_i=1_P\). Equation (1.1) is a **finite bounded-distributive-lattice identity** in these variables. To verify it, work in the finite distributive sublattice they generate (finitely generated distributive lattices are finite), where distinct elements can be separated by a homomorphism to the two-element lattice.

Under any such \(0/1\)-valuation, let \(A=\{i:x_i=1\}\), \(B=\{i:y_i=1\}\); both are nonempty because the \(x_i\) and \(y_i\) each cover top. The left side \(w_F\) evaluates to \(1\) iff \(A\cap B\ne\varnothing\). Each binary cut \(w_{B_S}\) evaluates to \(1\) iff \(A,B\) both meet \(S\), or both meet \([n]\setminus S\).

If \(A\cap B\ne\varnothing\), every cut evaluates to \(1\). If \(A\cap B=\varnothing\), choose \(S=A\); then the \(S\)-side has no \(y_i=1\), while the complement has no \(x_i=1\), so this cut evaluates to \(0\). Hence the two sides of (1.1) agree under all \(0/1\)-valuations. They are equal in the finite distributive sublattice, and therefore in \(P\). □

**Independent sanity check:** The underlying finite Boolean truth-table condition was exhaustively checked for \(1\le n\le6\) (nonempty index-support pairs); there were zero counterexamples. The proof does not depend on the computation.

**Remark.** Equation (1.1) is an identity of **open elements**, not merely equality of ordinary point sets or of resulting sublocales. This is materially stronger than the spatial pointwise binary coarsening observation.

## 2. Consequences for D₂ and finite pre-nucleus fixed points

Let
\[
D_{\mathrm{bin}}=\bigwedge_{u\vee v=1_L}\mathfrak o\bigl((u\boxtimes u)\vee(v\boxtimes v)\bigr).
\]
**Corollary 2.1.** For every locale \(X\),
\[
\boxed{D_{\mathrm{bin}}=D_2.} \tag{2.1}
\]
Consequently, a pair of frame maps into **any** frame \(M\) matches all finite \(L\)-covers iff it matches all binary \(L\)-covers.

*Proof.* Each finite \(F\)-matching open is a finite meet of the matching opens of its binary coarsenings, by Theorem 1.1; factoring through every binary matching open therefore forces factoring through every finite one. The converse is immediate. □

Write
\[
\Phi_{\mathrm{bin}}(d)=\bigvee_{u\vee v=1_L}
\bigl(((u\boxtimes u)\vee(v\boxtimes v))\to d\bigr),
\qquad
\Phi_2(d)=\bigvee_{F\text{ finite cover}}(w_F\to d).
\]
**Corollary 2.2 (same fixed points).** For every \(d\in P\),
\[
\boxed{\Phi_{\mathrm{bin}}(d)=d\quad\Longleftrightarrow\quad\Phi_2(d)=d.} \tag{2.2}
\]
*Proof.* The forward hypothesis means every binary matching-square open restricts to a **dense** open in the closed locale \(Y=\mathfrak c(d)\). By (1.1), each finite \(w_F\) is a **finite meet** of such opens, hence also dense in \(Y\). Therefore \((w_F\to d)=d\) for all finite F. The reverse implication is immediate. □

**Critical qualification:** We do **not** assert equality of the one-step maps \(\Phi_{\mathrm{bin}}=\Phi_2\). In a general Heyting algebra the implication of a finite meet is not necessarily the join of the individual implications. Equation (2.2) is a statement about their **fixed-point sets**.

## 3. Geometric form in spatial X: disjoint closed rectangles

Suppose \(X\) is spatial, and let \(u,v\subseteq X\) be opens with \(u\cup v=X\). Define the disjoint closed sets
\[
A=X\setminus v,\qquad B=X\setminus u,\qquad A\cap B=\varnothing.
\]
A pair \((x,y)\) fails the matching square of \(\{u,v\}\) **precisely** if one coordinate belongs to \(A\) and the other to \(B\). Thus its pointwise bad locus is
\[
\boxed{(A\times B)\cup(B\times A).} \tag{3.1}
\]
Conversely every pair of disjoint closed subsets \(A,B\) arises from the binary cover \(u=X\setminus B,\ v=X\setminus A\).

For any \(\Phi_2\)-fixed \(d\), every binary-cover matching square is dense in \(Y=\mathfrak c(d)\). Hence if \(E\subseteq Y\) is a **spatial Baire relatively open C-hole**, then every closed-rectangle locus (3.1) intersects \(E\) in a **closed nowhere-dense** subset. Every ordinary point of \(E\) lies in *some* such locus, using the binary coarsening of C corresponding to its first-coordinate incidence set.

Thus the spatial Baire version of the remaining problem is precise:

> Can a nonzero relatively open subspace of the special closed relation \(W_2(X)\) be covered by these relative closed nowhere-dense **disjoint-closed-rectangle loci**, even though no countable subfamily can cover it?

Ordinary Baire category alone excludes **countable** subcovers, not arbitrary ones. The closed rectangles are not assumed to be open, and their associated covers are not restricted to coarsenings of the original C.

## 4. Checks, countercontrols and next priority

1. **Topological vs point-free:** The finite cut identity (1.1) is an algebraic distributive-lattice law, so it is valid even when the localic square is nonspatial. The rectangle picture (3.1) is explicitly only a point-set description in spatial X.
2. **Complemented-sector control:** The [Polish disjoint-infinite-subsets example](ProjectA_Q_RELATIVE_BAIRE_INCIDENCE_PROFILES_POLISH_CONTROL_2026-11-13.md) passes the binary tests obtained by coarsening C but fails unrelated binary covers \(\{c_n,X\setminus c_n\}\). It confirms that “arbitrary binary X-cover” is strictly richer than “binary coarsening of C.”
3. **Finite meet vs sublocale meet:** Identity (1.1) takes place in \(P\) itself. Passing to \(\mathfrak o(w)\) preserves these **finite meets**, so (2.1) is justified.
4. **No accidental one-step claim:** Equivalence (2.2) does not entail equality of \(\Phi_{\mathrm{bin}}\) and \(\Phi_2\) at arbitrary arguments.
5. **Closed-support gate:** By the independently checked [closed-atomic theorem](ProjectA_Q_CLOSED_ATOMIC_SCATTERED_WEAK_DEFECT_NO_GO_2026-11-13.md), any weak C-defect already has atomless least closed coordinate supports. Our remaining category problem concerns their possible *relatively open* manifestation.

**Research decision.** In the next test, concentrate on **arbitrary binary covers** and the way their disjoint closed rectangles sit in \(W_2\), rather than enumerating all finite covers or only coloring the offending C. The exact finite cut identity is suitable for the next external audit packet. Universal Q/Q′ remain OPEN.


## 5. Strong Scott closed/Baire countercontrol: *all* finite-cover squares dense, but C vanishes

There is a direct spatial Baire model showing that **even full finite-cover density on a closed relation is not enough**. Let
\[
X=\mathcal P(\omega)\setminus\{\varnothing\}
\]
with the Scott topology for inclusion. A basis consists of the opens \(\uparrow P=\{A:P\subseteq A\}\) for finite nonempty \(P\subseteq\omega\). The countable cover
\[
C=\{c_n:n\in\omega\},\qquad c_n=\{A:n\in A\},
\]
covers \(X\). Define the **closed** spatial relation
\[
R=\{(A,B)\in X^2:A\cap B=\varnothing\}=X^2\setminus w_C.
\]
It is nonempty, and \(w_C|_R=0\).

**Proposition 5.1.** The subspace \(R\) is Baire. For **every finite \(X\)-cover F**, its matching-square open \(w_F\) restricts to a **dense open in \(R\)**, despite \(w_C|_R=0\).

*Proof (Baire).* The relative topology of \(R\) has a basis of the nonempty patches
\[
R_{P,Q}=\{(A,B)\in R:P\subseteq A,\ Q\subseteq B\},
\]
where \(P,Q\) are finite, nonempty, disjoint subsets of \(\omega\). Given a sequence \(G_0,G_1,\ldots\) of dense open subsets of \(R\) and a nonempty basic patch, recursively refine to nested basic patches \(R_{P_n,Q_n}\subseteq G_n\), ensuring \(P_n\subseteq P_{n+1}\) and \(Q_n\subseteq Q_{n+1}\). This is possible because each dense open meets the previous basic patch, and a compatible finite extension can be taken around a point in the intersection. The unions \(P_\infty=\bigcup_nP_n\) and \(Q_\infty=\bigcup_nQ_n\) remain disjoint and nonempty, giving \((P_\infty,Q_\infty)\in R\cap\bigcap_nG_n\) inside the initial patch. Thus \(R\) is Baire.

*Proof (finite-cover density).* Let \(F\) be a finite cover of \(X\). For each \(n\in\omega\), the singleton point \(\{n\}\in X\) belongs to at least one \(f\in F\). By finite pigeonhole, **some single member \(f\in F\) contains \(\{n\}\) for infinitely many \(n\)**; write \(J\subseteq\omega\) for this infinite set. Scott opens are upward closed, so \(c_n\subseteq f\) for each \(n\in J\). Given any nonempty basic \(R_{P,Q}\), choose distinct fresh \(n,m\in J\setminus(P\cup Q)\). Then
\[
(A,B)=(P\cup\{n\},\,Q\cup\{m\})\in R_{P,Q}\cap(f\times f).
\]
Therefore \(w_F|_R\) is dense open. □

**Corollary 5.1A (genuine weak Boolean defect).** Pass from the nonzero frame \(\mathcal O(R)\) to its double-negation Booleanization \(B(R)\). Every \(w_F|_R\), \(F\) finite, is dense and therefore becomes top in \(B(R)\), whereas \(w_C|_R=0\). The two coordinate maps \(L\rightrightarrows B(R)\) thus give a **finite-cover-compatible but C-defective generalized pair**. In particular \(D_2(X)\ne D(X)\). This does not imply a nonzero *open* hole in \(W_2\).

**Proposition 5.2 (no open-hole interpretation).** The closed set \(R\) has **empty interior** in \(X^2\): any nonempty basic rectangle \((\uparrow P)\times(\uparrow Q)\) contains the overlapping pair \((P\cup Q,P\cup Q)\). Thus \(R\) is nowhere dense in the spatial topological square. In this Scott example the diagonal is dense in the square (every pair of nonempty Scott opens intersects), so the closure of the fitted diagonal is the whole square, \(W_2=X^2\), and \(R\) supplies **no nonzero relatively open C-hole**.

**Corollary 5.3 (sharp fixed-point nontransfer).** In this example put \(d_R=w_C\in P\), so \(R=\mathfrak c_{X^2}(d_R)\). Proposition 5.1 says
\[
\boxed{\Phi_2(d_R)=d_R, \qquad \Phi(d_R)=1_P>d_R,} \tag{5.1}
\]
the second equality holding since the \(C\)-term is \(w_C\to d_R=1_P\). By contrast, **every** arbitrary-cover matching square is dense in the **whole** \(X^2\): given any nonempty basic rectangle, choose a singleton \(\{n\}\) and one cover member containing it, and extend both coordinates by \(n\). Thus \(\Phi(0)=\Phi_2(0)=0\), so the canonical finite fixed point is \(d_0=0\), and Q′ holds: \(W_2=W=X^2\).

Therefore **Q′ does not imply that every \(\Phi_2\)-fixed open is \(\Phi\)-fixed**. Any proof scheme trying to establish that global fixed-point equality as an intermediate step toward Q′ is too strong. It must exploit **the canonical least fixed point \(d_0\)**, not an arbitrary finite-fixed closed relation.

**Adversarial conclusion.** The earlier Polish disjoint-infinite-set control failed unrelated finite covers. This Scott control is stronger: *all* finite \(X\)-cover squares are dense on a **Baire closed subspace**, yet the infinite \(C\)-square is zero there. The only missing hypothesis for a Q′ counterexample is precisely that the bad relation contains a **nonzero open of \(W_2\)**. Hence no proof based merely on “finite squares dense on a Baire relation” can work; the open placement inside \(W_2\) must be used. This is an elementary spatial manifestation of the already known weak-versus-strong Scott defect distinction, not a novel universal counterexample.


## 6. Exact Boolean visibility criterion at the **canonical** W₂ stage

The Scott nontransfer in §5 tells us to formulate the open-placement requirement precisely, rather than demand it at every finite-fixed \(d\). Let
\[
Y=W_2(X)=\overline{D_2(X)}^{\,X^2},\qquad
K_C=Y\wedge\mathfrak c_{X^2}(w_C),\qquad
A_C=D_2\wedge\mathfrak c_{X^2}(w_C).
\]
Here \(D_2\) is **dense** in \(Y\), \(K_C\) is **closed** in \(Y\), and \(A_C\le K_C\).

**Proposition 6.1 (weak defect becomes strong iff somewhere dense).** For a fixed cover \(C\), the following are equivalent:

1. \(C\) witnesses failure of Q′: \(w_C|_Y\) is **not** dense in \(Y\).
2. \(K_C\) contains a nonzero **open** sublocale of \(Y\).
3. \(\operatorname{int}_Y(\overline{A_C}^{\,Y})\ne0\).
4. There exists a **nonzero Boolean sublocale** \(B\le A_C\) whose closure in \(Y\) has nonzero interior.

*Proof.* (1)⇔(2) is the definition of density of an open in \(Y\): its closed complement has nonempty interior.

(2)⇒(3): Choose nonzero \(Y\)-open \(V\le K_C\). Since \(D_2\) is dense in \(Y\), \(D_2\wedge V\) is dense in \(V\). But \(D_2\wedge V\le A_C\), so \(\overline{A_C}^{\,Y}\) contains \(V\). Conversely, (3)⇒(2) because \(A_C\le K_C\) and \(K_C\) is closed in \(Y\).

(2)⇒(4): For nonzero \(Y\)-open \(V\le K_C\), let \(B(V)\) be its **least dense Boolean sublocale**. Since \(D_2\wedge V\) is dense in \(V\), minimality of \(B(V)\) gives
\[
0\ne B(V)\le D_2\wedge V\le A_C.
\]
As \(B(V)\) is dense in the nonzero \(Y\)-open \(V\), its closure in \(Y\) contains \(V\). Thus (4). Finally (4)⇒(3) is immediate. □

This is a **criterion, not a proof of Q′**. It states exactly what a generalized weak Boolean finite/full defect needs to become strong: its closure must acquire **nonzero interior in the canonical finite fitted-diagonal closure** \(W_2\). Neither being Baire as a closed subspace nor being somewhere dense in some *smaller* \(\Phi_2\)-fixed closed relation is enough.

**Scott verification.** In §5, \(B(R)\le A_C\) is a genuine weak defect. Its closure in \(Y=X^2\) is \(R\), which is **nowhere dense**. Hence condition (4) fails and Q′ holds. At the different finite-fixed closed relation \(R=\mathfrak c(w_C)\), the same Boolean sublocale is dense and witnesses \(\Phi(d_R)\ne d_R\). This juxtaposition is the exact reason the **canonical** qualifier in Proposition 6.1 is indispensable.

**Next step for external audit.** Check (1.1), Corollaries 2.1–2.2, the spatial closed-rectangle translation, the elementary Scott construction, and Proposition 6.1; then assess whether the criterion gives a viable route to proving *all* Boolean weak defects nowhere dense in \(W_2\), or merely restates Q′. We currently regard Proposition 6.1 as an **exact reformulation**, not an independent extra constraint.


---

## Appendix A. Closed-atomic/scattered weak-defect obstruction (proof of the earlier background theorem)

The following is the **proof-bearing part** of the earlier note, included for independent verification. Its separate internal-adversarial-check section is intentionally not reproduced in this blind first-reading packet. The proof's hypotheses, maps and corollaries are explicit.

# Project A / Q, Q′ — closed-atomic support obstruction; scattered-space positive class

**13 November 2026 (America/Denver); INTERNAL ADVERSARIAL AUDIT, not externally refereed.** The claim below is stated with an explicit **closed-atomic** frame condition. Published usages of “scattered locale” vary; only the standard *topological* scatteredness convention is used in the spatial corollary.

## 0. Set-up and precise hypothesis

For \(L=\mathcal O(X)\) and an \(L\)-cover \(C\), put
\[
w_C=\bigvee_{c\in C}c\boxtimes c\in P=L\oplus L,
\qquad
D_2=\bigwedge_{F\text{ finite cover}}\mathfrak o(w_F),
\qquad
D=\bigwedge_{C\text{ arbitrary cover}}\mathfrak o(w_C)
\]
in the sublocale coframe, so \(D\le D_2\). Maps \(h,k:L\to M\) are *binary-cover compatible* if, for every \(u\vee v=1_L\),
\[
(h(u)\wedge k(u))\vee(h(v)\wedge k(v))=1_M. \tag{0.1}
\]
In particular, compatibility with every finite cover implies (0.1).

Call \(L\) **closed-atomic** when, for every \(e<1_L\), the interval frame
\(\mathcal O(\mathfrak c_X(e))\cong [e,1_L]\) has an atom \(a>e\).

## 1. Main obstruction, arbitrary targets

**Theorem 1.1 (atomless closed supports of defective coordinate maps).**
Let \(h,k:L\to M\) be binary-cover compatible maps into a nontrivial frame \(M\), and suppose some arbitrary cover \(C\) is defective:
\[
m_C=\bigvee_{c\in C}h(c)\wedge k(c)<1_M. \tag{1.1}
\]
Pass to the nontrivial quotient frame \(M'=\uparrow m_C\) via \(q(t)=t\vee m_C\), and set \(h'=qh,k'=qk\). The matching value of \(C\) is now \(0_{M'}=m_C\). The least closed supports of **both** coordinate maps \(h',k'\) have atomless frames of opens. Explicitly, if
\[
e_h=\bigvee\{a\in L:h'(a)=0_{M'}\},\qquad
e_k=\bigvee\{a\in L:k'(a)=0_{M'}\},
\]
then both \([e_h,1]\) and \([e_k,1]\) are atomless.

*Proof.* Rename \(M',h',k'\) as \(M,h,k\), so \(\bigvee_C h(c)\wedge k(c)=0_M\). Let \(e=e_h\). Since \(h\) preserves all joins,
\[
h(e)=0_M,\qquad h(t)=0_M\iff t\le e,\qquad h(t)=h(t\vee e). \tag{1.2}
\]
Also \(e<1_L\), since \(M\) is nontrivial and \(h(1_L)=1_M\).

Suppose \([e,1_L]\) has an atom \(a>e\). For every \(c\in C\),
\(a\wedge(c\vee e)\) lies in \([e,a]\), so it equals either \(e\) or \(a\).
Partition \(C=C_1\sqcup C_0\), where
\[
C_1=\{c:a\le c\vee e\},\qquad
C_0=\{c:a\wedge(c\vee e)=e\},
\qquad u=\bigvee C_1,\quad v=\bigvee C_0.
\]
The family \(C_1\) is **nonempty**, because
\[
a=a\wedge\bigvee_{c\in C}(c\vee e)
 =\bigvee_{c\in C}\bigl(a\wedge(c\vee e)\bigr)>e.
\]
Moreover \(u\vee v=1_L\), so \(\{u,v\}\) is a binary cover. By (1.2),
\(h(a)\neq0_M\), \(h(a)\le h(c)\) for all \(c\in C_1\), and
\(h(a)\wedge h(c)=0_M\) for all \(c\in C_0\). Thus
\[
h(a)\le h(u),\qquad h(a)\wedge h(v)=0_M. \tag{1.3}
\]
Meet the binary-cover identity (0.1) with \(h(a)\). By (1.3) and arbitrary distributivity in \(M\),
\[
h(a)=h(a)\wedge k(u)
=\bigvee_{c\in C_1}\bigl(h(a)\wedge k(c)\bigr)=0_M,
\]
since \(h(a)\le h(c)\) and \(h(c)\wedge k(c)=0_M\) for every \(c\in C_1\). Contradiction. The argument for \(e_k\) interchanges the coordinates. □

**Key point:** This is a *weak-defect* obstruction involving arbitrary, possibly nonspatial target frames. It is not restricted to ordinary pairs or relatively open holes.

## 2. Consequences for D, W and scattered spaces

**Corollary 2.1.** If \(L\) is closed-atomic, every binary-compatible pair into any frame matches every arbitrary cover. Therefore
\[
\boxed{D_2(X)=D(X),\qquad W_2(X)=W(X).} \tag{2.1}
\]
*Proof.* A defective pair would contradict closed-atomicity by Theorem 1.1. A locale map into \(X^2\), represented by a coordinate pair into its domain frame, factors through \(D_2\) exactly when it matches every finite cover, and through \(D\) when it matches every cover. Equality of these universal factorization conditions yields \(D_2=D\). Taking closures yields \(W_2=W\). □

**Corollary 2.2 (topologically scattered spatial locales).** Suppose \(X\) is spatial and the ordinary sober point space of \(X\) is scattered: **every nonempty closed subspace has an isolated point**. Then \(L\) is closed-atomic. Indeed each nonzero closed sublocale \(\mathfrak c(e)\) is represented by the corresponding nonempty closed point subspace, and an isolated singleton there is an atom of \([e,1]\). Consequently (2.1) holds, without local compactness, regularity, Baire assumptions, or spatiality of the *localic square* \(X^2\).

*Terminology check:* Picado–Pultr, *Frames and Locales* (2012), VI §8.1, give this topological definition of scattered spaces. Other usages of “scattered locale” involve complemented or Boolean sublocales; **no identification with closed-atomicity is asserted here**.

## 3. Full-versus-finite fixed points and Q/Q′

Write
\[
\Phi_2(d)=\bigvee_{F\text{ finite cover}}(w_F\to d),\qquad
\Phi(d)=\bigvee_{C\text{ arbitrary cover}}(w_C\to d).
\]
**Lemma 3.1.** If \(D_2=D\), then **every \(\Phi_2\)-fixed open \(d\in P\) is also \(\Phi\)-fixed.**

*Proof.* If \(\Phi_2(d)=d\) but \(\Phi(d)>d\), choose \(C\) with
\(r=(w_C\to d)\nleq d\). The relatively open sublocale
\(E=\mathfrak o_{\mathfrak c_{X^2}(d)}(r)\) is nonzero and has \(w_C|_E=0\). For every finite cover \(F\), \(w_F\to d=d\), so \(w_F\) is dense open on \(\mathfrak c(d)\) and on \(E\). Compose the two coordinate maps \(L\rightrightarrows\mathcal O(E)\) with the canonical quotient to the **nontrivial double-negation Booleanization** \(B(E)\). Every finite-cover matching square becomes top (it was dense), while the \(C\)-square remains bottom. This constructs a finite-compatible, \(C\)-defective pair, contradicting \(D_2=D\). □

Thus in the closed-atomic class, the two pre-nuclei have the **same fixed points**, not necessarily the same value at each individual stage. In particular, **Q′** holds, and the rank-one **Q** implication holds under its specified finite-fixed premise \(\Phi_2(z_1)=z_1\). We do **not** assert the unconditional one-step identity \(\Phi=\Phi_2\).


---

## Appendix B. Exact audit questions and dependency checklist

Please follow the separate prompt. In addition to checking each proof on its own, verify the following dependency chain:

- Theorem I.1 only uses finite **color block** covers.
- Theorem II.1 assumes an actual **countable family of all-ambient finite X-cover tests** detecting C-bad ordinary points, plus **spatial Baire W₂**.
- Part III's Polish relation passes color block covers but **fails** other ambient finite covers.
- Part IV's cut identity **reduces all finite covers to binary ambient covers** without claiming those binary covers are coarsenings of C.
- Part IV's Scott relation passes **all** finite ambient covers and is Baire, but is **nowhere dense in W₂**; its Booleanization is a weak defect without a Q′ hole.
- The Boolean visibility criterion is stated at the **canonical** W₂, and its equivalence to Q′ is not asserted at arbitrary finite-fixed closed relations.

We ask for an adversarial report on correctness, missed hypotheses, source dependence, presentation ambiguities and possible simplifications or genuinely new routes to Q′. Report uncertainty explicitly.

