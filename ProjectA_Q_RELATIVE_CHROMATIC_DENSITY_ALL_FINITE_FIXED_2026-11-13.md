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
