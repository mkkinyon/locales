# Project A — INTERNAL ADVERSARIAL AUDIT: dense rational bridges and Questions Q, Q′

**14 November 2026. Internal examination only. NOT part of the blind referee packet.**

## Verdict and scope

**No fatal gap found in the proposed counterexample, subject to independent verification of the locale-theoretic steps.** An explicit second-countable sober T₁ étale space over ℝ appears to satisfy

\[
W(X)=I(X)<W_2(X)=U(X)=X\times_{\mathbb R}X.
\]

This would refute both the universal Q′ assertion \(W=W_2\) and the universal Q implication \(W_2=U\Rightarrow W=U\). The conclusion is potentially consequential; **do not treat it as externally certified**, and do not silently change the open-question status elsewhere in the repository before blind audit.

## 1. Adversarial reconstruction of the topology

Underlying set: two labelled lines \(S=\{s_x\}\), \(T=\{t_x\}\) and bridge points \(b_q\) for rational \(q\). The two lines are disjoint open copies of ℝ. Basic bridge neighborhoods are
\[
N(q,\varepsilon)=\{b_q\}\cup\{s_x:q-\varepsilon<x<q\}
\cup\{t_x:q<x<q+\varepsilon\}.
\]
The projection \(p(s_x)=p(t_x)=x\), \(p(b_q)=q\) restricts to a homeomorphism on S, T and each \(N(q,\varepsilon)\). Intersections of basic neighborhoods from different bridges consist solely of open portions of S and T. Thus this defines a topology and \(p\) is étale/open. The fiber over rational q is \(\{s_q,t_q,b_q\}\), otherwise \(\{s_x,t_x\}\), each discrete. Countable rational bases give second countability. T₁ follows by separating distinct points through their different fiber germs or base positions; individual bridge points are closed. Sobriety follows from the open cover by sober copies of ℝ: every nonempty open subspace of an irreducible closed set is dense in it, so its generic point in a sober chart is generic globally.

**Referee check:** Verify both the topology and the use of open-local sobriety directly. No unproved Hausdorffness is asserted.

## 2. Finite-cover density: alternative adversarial proofs

Let \(\mathscr F=\{c_1,\ldots,c_n\}\) be ANY finite open X-cover; set
\[
m_{\mathscr F}=\bigvee_i(s^*c_i\wedge t^*c_i)\in\mathcal O(\mathbb R).
\]

**Boundary proof.** If a nonempty interval J misses \(m_{\mathscr F}\), put \(A_i=s^*c_i\cap J\), \(B_i=t^*c_i\cap J\). These are disjoint opens. Every rational q∈J has b_q in some c_i, forcing a left interval near q into A_i and a right interval into B_i. Thus q belongs to the boundary \(\partial_J A_i\). The dense set \(\mathbb Q\cap J\) is covered by finitely many closed nowhere-dense boundaries, contradiction. Therefore every \(m_{\mathscr F}\) is dense open.

**Independent coloring proof.** Color q by some i with b_q∈c_i. A finite coloring of the dense rationals has a color dense on some nonempty subinterval of any prescribed interval. For that color, both s^*c_i and t^*c_i are open dense on the subinterval; they intersect. This again proves m_F dense.

**Referee check:** Quantifiers are critical: the claim holds for every *ambient finite open cover*, not merely a chosen chart cover.

## 3. Boolean-support generalized pair

Let \(\beta:B(\mathbb R)\hookrightarrow\mathbb R\) be the double-negation Booleanization. Its frame map sends any dense open u to 1, since \(u^*=0\Rightarrow u^{**}=1\). The Booleanization is nonzero. Form
\[
h=\beta^*s^*,\quad k=\beta^*t^*:\mathcal O(X)\to\operatorname{RO}(\mathbb R).
\]
For every finite cover \(\mathscr F\),
\[
\bigvee_{c\in\mathscr F}(h(c)\wedge k(c))
=\beta^*(m_{\mathscr F})=1.
\]
Hence the map \(B(\mathbb R)\to X^2\) factors through \(D_2(X)\) and its image lies in the pair chart \(J=S\times_{\mathbb R}T\cong\mathbb R\). It is nonzero, and B(ℝ) is dense in J.

For the **infinite** atlas \(\mathscr A=\{S,T,N_q:q\in\mathbb Q\}\) with \(N_q=\bigcup_{\varepsilon>0}N(q,\varepsilon)\), every member is a section and contains at most one of s_x,t_x for any x. Thus the corresponding common-member open is zero, proving this generalized pair does **not** factor through D(X). This last nonfactorization alone does NOT imply W≠W₂; closed-hull separation is checked separately.

**Referee check:** Confirm the double-negation quotient is a frame map with joins evaluated in RO(ℝ), and verify all pullbacks are LOCALIC.

## 4. Full diagonal and closed-hull separation

Regularity of ℝ gives \(D(\mathbb R)=\Delta_{\mathbb R}\). Any generalized pair in D(X) has equal p-components by naturality. The infinite section atlas square condition gives an open cover of its domain on which both components land in the same section, hence agree. Therefore D(X)=Δ_X and W(X)=I(X).

The rectangle \(S\boxtimes T\subset X^2\) is open and disjoint from Δ_X because S∩T=∅. Hence it is disjoint from I(X)=cl Δ_X. The nonzero Booleanization pair lies in D₂(X) and in this rectangle. Therefore W₂(X)>W(X), with no unsupported inference that closed hulls differ merely because D₂>D.

**Referee check:** Independently verify the naturality used above and the openness/disjointness of the ambient rectangle.

## 5. Stronger calculation W₂=U=F

Let \(F=X\times_{\mathbb R}X\). Since ℝ is regular, its diagonal is closed and \(W_2(X)\le U(X)\le F\) by naturality and the universal finite-cover/far inequality. F is spatial: it is covered by open sections \(U_i\times_{\mathbb R}U_j\cong p(U_i)\cap p(U_j)\), all spatial opens of ℝ.

The chart \(J=S\times_{\mathbb R}T\cong\mathbb R\) is OPEN IN F, not generally in X². Because W₂(X) is closed in F and contains the dense Booleanization B(J), its restriction to J is all J. The transposed chart is also contained in W₂ by symmetry.

At irrational base x, F has only diagonal points and the two S/T cross-pairs. At rational q it additionally has b_q; the pair (b_q,s_q) is inseparable because bridge neighborhoods meet S on the left, and (b_q,t_q) likewise on the right. Both and their transposes lie in I(X)≤W₂(X). Hence every ordinary point of F lies in the CLOSED sublocale W₂(X). Because F is spatial, W₂(X)=F. Sandwiching yields U(X)=F.

**Referee check:** The closedness of W₂ inside F, spatiality of F, and density of B(J) are indispensable. Do not replace these with pointwise equality of arbitrary sublocales.

## 6. Further consistency checks and reservations

- For any fixed x, the binary cover \(\{X\setminus\{s_x\},X\setminus\{t_x\}\}\) excludes the ordinary cross-pair (s_x,t_x), so the D₂ witness has no ordinary point on J. This is consistent with its nonzero Boolean-support content.
- On each finite discrete fiber, D₂=D=Δ. The nonzero open \(D_2(X)\cap J\) is invisible to all ordinary fibers, exactly the failure of (FD) predicted by the preceding descent theorem.
- The infinite closed discrete bridge set means X is noncompact; no contradiction with any compact positive theorem is asserted.
- Avoid claims about literature novelty, publication readiness, or other separation ranks until the basic counterexample is independently checked.
- The earlier Q′ residual reductions, if valid, should be checked for compatibility after the external audit rather than used as circular proof support here.

**Internal verdict:** The density argument, Booleanization witness, and upgrade to W₂=U=F appear logically coherent. All crucial imports have explicit statements in the blind packet. Recommend immediate independent, adversarial blind audit before updating theorem/status records.
