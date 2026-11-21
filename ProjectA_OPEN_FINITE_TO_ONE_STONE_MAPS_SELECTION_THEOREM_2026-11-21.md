# Project A — open finite-to-one maps over zero-dimensional targets: exact finite chart rank
## 21 November 2026 · NEW INTERNAL corollary of Michael's selection theorem

**Audit/provenance:** New internal deduction based on the established *zero-dimensional Michael continuous-selection theorem* and the internally argued [locally closed partial-homeomorphism associative graph algebra](ProjectA_GRAPH_LOCAL_HOMEOMORPHISM_POSITIVE_OPEN_PROPER_NEGATIVE_2026-11-20.md). This is **not** contained in the independent referee's compact-Hausdorff rectangular report. It completes the open-plus-uniformly-finite-fiber corner for **compact metrizable, zero-dimensional target** maps. No unrestricted Stone/locale generalization, and no literature priority assertion.

### 1. The zero-dimensional selection theorem used

**Classical zero-dimensional selection theorem (Ernest Michael):** If Y is zero-dimensional paracompact, M is a completely metrizable space, and F:Y⇒M is lower semicontinuous with nonempty closed values, then F has a continuous selection s:Y→M. An accessible statement is given by Topology Proceedings 39 (2012), [A Note On Uniformly Continuous Selections For Multi-Valued Maps](https://topology.nipissingu.ca/tp/reprints/v39/tp39004.pdf), and in [Selections and representations of multifunctions in paracompact spaces](https://matwbn.icm.edu.pl/ksiazki/sm/sm102/sm10232.pdf). The theorem is a cited classical input, not newly proved here.

For an **open surjection** f:M→Y, the inverse-fiber multifunction F(y)=f^-1(y) is lower semicontinuous: for every open O⊆M, \(\{y:F(y)\cap O\ne\varnothing\}=f(O)\) is open in Y. If M is completely metrizable and Y is zero-dimensional paracompact, Michael therefore gives a continuous right inverse s:Y→M.

The image s(Y) is **closed in M**, since it is the equalizer of id_M and s∘f, and M is Hausdorff. Thus M\s(Y) is open and completely metrizable, and its image under f is open in Y.

### 2. Exact finite-chart theorem

**Theorem 2.1 (INTERNAL).** Let X be compact metrizable, Y be compact metrizable and zero-dimensional, and f:X→Y be a continuous **open surjection**. Assume every fiber is finite, with a *uniform bound*
\[
\boxed{N=\max_{y\in Y}|f^{-1}(y)|<\infty.}
\]
Then X is a disjoint union of **N locally closed** ordinary subspaces U_1,…,U_N such that each restriction
\[
f|_{U_i}:U_i\overset{\cong}{\longrightarrow}V_i
\]
is a homeomorphism onto an **open subspace V_i⊆Y**. Consequently the locally closed graph-chart rank is exactly the maximum fiber multiplicity:
\[
\boxed{\rho_{\rm lc}(f)=N.}\tag{RANK}
\]

**Proof.** Set X_1=X,Y_1=Y,f_1=f. Inductively assume X_i is open in X (hence completely metrizable) and Y_i=f(X_i) is open in Y (hence zero-dimensional and paracompact). The restriction f_i=f|X_i:X_i→Y_i is an open surjection. By the lower-semicontinuous-fiber observation and Michael's theorem, it has a continuous section s_i:Y_i→X_i. Its image U_i=s_i(Y_i) is closed in X_i and therefore **locally closed in X** (X_i open in X). The restriction f|U_i is a homeomorphism onto V_i=Y_i, which is open in Y.

Define X_{i+1}=X_i\U_i, open in X, and Y_{i+1}=f(X_{i+1}), open in Y. For each y for which the fiber remains nonempty, this stage removes exactly one preimage. Thus after N stages every fiber is exhausted, X_{N+1}=∅, and X is a disjoint union of the locally closed sections U_i.

Every injective chart covers **at most one** point in any fiber, yielding the universal lower bound \(\rho_{\rm lc}(f)\ge \sup_y|f^{-1}(y)|=N\). The displayed construction gives the reverse bound, proving equality. □

The proof uses only that each open X_i is completely metrizable (as an open subset of a compact metric X), and each open Y_i is zero-dimensional paracompact. It extends beyond compact spaces whenever an analogous uniform fiber bound and completeness/paracompactness hypotheses persist, but no such extension is asserted as a separate theorem.

### 3. Consequence for localic relational graph algebra (conditional on the INTERNAL graph extension)

Embed X and Y as clopen disjoint components of a compact Hausdorff G=X⊔Y. The graph of f is point-generated and decomposes as a **finite localic join**
\[
\Gamma_f=\bigvee_{i=1}^N\Gamma_{f|U_i}.
\]
Each summand is a graph of a locally closed partial homeomorphism between subspaces of G. By the previous **internally proved**, but not yet blind-refereed, associative algebra of point-generated and full rectangles mixed with locally closed partial homeomorphisms, adjoining **both** \(\Gamma_f\) and \(\Gamma_f^\smile\) preserves associativity for all finite-join/composition expressions.

**Important:** It is not generally true for an arbitrary finite-to-one f that \(\Gamma_f\) can be decomposed this way. **Openness** is the hypothesis allowing repeated Michael selections; **zero-dimensionality of the target** makes the multivalued selection theorem applicable. This is a different sufficient mechanism from the compact-Hausdorff referee's uniform rectangle saturation theorem.

### 4. Sharp contrast with the nonopen two-to-one Cantor construction

The [Cantor-to-Cantor two-to-one counterexample](ProjectA_FINITE_FIBRE_GRAPH_CHART_RANK_CANTOR_COUNTEREXAMPLE_2026-11-21.md) is a continuous **proper surjection** with at most two points in every fiber, but is **not open**; it has a discrete ordinary selector E⊂X mapping bijectively to a dense Q⊂Y with dense complement. This gives a graph-probe associator and forces \(\rho_{\rm lc}(f)=\infty\).

Theorem 2.1 says this cannot happen for a continuous **open** two-to-one surjection between compact metrizable spaces with zero-dimensional target: exactly **two** locally closed sheet charts exist. The max fiber cardinality by itself is not the correct invariant; for open maps into a zero-dimensional base, it becomes the exact chart rank. In a nonzero-dimensional base, finite-sheeted covering monodromy can force chart rank to exceed fiber degree (even when it stays finite), so no general equality is claimed.

### 5. Broader ramifications and remaining questions

For compact metric maps into Cantor space, the open-plus-finite-multiplicity corner is now positive, including maps that are **not** local homeomorphisms. This fills a gap left after the earlier positive two-to-one Cantor shift and the negative infinite-fiber open projection.

A particularly informative example of a **branched but positive** map is f:[−1,1]→[0,1], f(t)=t²: although its target is connected, its graph is a two-chart union of closed restricted homeomorphisms and thus lies in the positive algebra. Openness is therefore **sufficient in the zero-dimensional bounded-fiber case**, not generally necessary for a map to have a finite locally closed chart decomposition.

**Remaining concrete problems:**
1. Does the associative finite-join graph algebra result extend from finite locally closed partial homeomorphisms to more general *finite correspondences* under stable image conditions?
2. How far can zero-dimensional selection extend in **nonmetrizable Stone** settings; what extra paracompactness/completeness or frame-theoretic hypotheses replace Michael's theorem?
3. With **connected or positive-dimensional target**, find a tractable branched open finite-to-one map with provably infinite locally closed chart rank (or an exact upper bound for interesting classes).
4. Return to *intrinsic Cameron–Kumar* specialization/Ins/Cm/Ury graphs by asking when their **actual localic relations** admit finite witness presentations, rather than interpreting imposed graph calculations as intrinsic separation results.

**Recommended next mathematical action:** internal adversarial audit of the locally closed graph-action formulas (especially restriction p/q across locally closed sublocales) and the Michael-selection induction, then consider an external audit packet. The new positive and negative theorems together constitute a coherent bounded package.
