# Project A — (LC-PT): maximal open TU locus and the perfect-core obstruction

**15 November 2026 · Internally checked, not independently audited.** A short structural reduction for the active question whether point-fittedness implies total unorderedness in locally compact sober \(T_1\) spaces. No novelty or priority claim. The result uses no local compactness.

## 1. TU is local on the target with respect to open covers

Write \(\mathcal A(X)\subseteq X^2\) for the oriented localic specialization relation, universally presented by \(a_1\le a_2\) for all opens a. Call X **totally unordered** (TU) when \(\mathcal A(X)=\Delta_X\).

**Open-cover lemma.** If a locale Y is covered by open sublocales \(Y_i\), all TU, then Y is TU.

*Proof.* Let \(f\le g:Z\to Y\) be a generalized comparable pair: \(f^*a\le g^*a\) for all opens a of Y. Let \(u_i\) represent \(Y_i\). The opens \(O_Z(f^*u_i)\) cover Z. On this open part, both f and g factor through \(Y_i\) (the implication for g follows from \(f^*u_i\le g^*u_i\)); their comparison therefore forces equality there. Equality on an open cover implies f=g globally. Thus \(\mathcal A(Y)=\Delta_Y\). \(\square\)

Hence the join of **all** open TU sublocales of X is itself TU. Denote it descriptively by \(U_{\mathrm{TU}}\) (not a new named member of the separation-relation hierarchy); its closed complement \(F_{\mathrm{TU}}\) is a canonical **non-TU core**.

## 2. Closed point excision recalled

For a point p closed in a locale Y, the [closed-point excision theorem](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md) gives
\[
Y\text{ TU}\quad\Longleftrightarrow\quad
Y\setminus\{p\}\text{ TU and }[p]=\operatorname{fit}_Y([p]).
\tag{2.1}
\]
Moreover, if p is fitted in X and lies in an open V⊆X, then p is fitted in V: its fitted hull in V is the restriction of its fitted hull in X.

## 3. Main perfect-core proposition

**Proposition.** Let X be a **\(T_1\) sober space** (or any spatial \(T_1\) locale where closed subspaces have their expected spatial meaning), and suppose every point sublocale of X is fitted. Then the closed complement \(F_{\mathrm{TU}}\) of the maximal open TU locus has **no isolated points**. Thus, if X is not TU, its non-TU core is a **nonempty closed dense-in-itself subspace**.

*Proof.* Suppose \(p\in F_{\mathrm{TU}}\) is isolated in that closed subspace. Choose an open neighborhood V of p in X with \(V\cap F_{\mathrm{TU}}=\{p\}\). Its complementary subspace within V is
\[
V\setminus\{p\}=V\cap U_{\mathrm{TU}},
\]
which is open in and hence TU as a sublocale of \(U_{\mathrm{TU}}\). Because X is \(T_1\), p is closed in V; because p is fitted in X, it is fitted in V. Closed-point excision (2.1) says V is TU. But V is an open sublocale of X containing p, and hence must lie in \(U_{\mathrm{TU}}\), contradicting \(p\in F_{\mathrm{TU}}\). \(\square\)

This statement has two deliberately different levels:

- For **arbitrary locales**, the maximal TU open exists by the open-cover lemma. Without a spatial \(T_1\) assumption, one cannot freely speak about isolated ordinary points of its closed complement or use closed-point excision at a nonclosed point.
- For **sober \(T_1\) spaces**, every nonempty closed non-TU core of a point-fitted X is crowded (has no isolated points). No assumption of stability, coherence, or local compactness enters this proof.

## 4. Consequences and relation to the scattered-remainder theorem

**Corollary 4.1.** Every **scattered sober \(T_1\)** space with all points fitted is TU. Indeed, any nonempty closed subset of a scattered space has an isolated point, which the proposition forbids for the non-TU core.

**Corollary 4.2.** If U⊆X is open and TU, X is sober \(T_1\), its closed complement F is scattered, and all points of F are fitted in X, then X is TU. To prove it, \(U\subseteq U_{\mathrm{TU}}\), so \(F_{\mathrm{TU}}\subseteq F\); the closed subspace \(F_{\mathrm{TU}}\) is scattered if F is, and every point of it is fitted, contradicting the proof of the proposition unless empty.

The previous [scattered closed-remainder theorem](ProjectA_LCPT_CLOSED_POINT_SCATTERED_EXCISION_2026-11-15.md) is **stronger in scope** because it does not require \(T_1\): it uses a transfinite constant-open-piece lemma for maps into scattered spatial locales. The present argument is more direct in the \(T_1\) setting that motivates (LC-PT).

**Concrete consequence for the active problem.** Any locally compact sober \(T_1\), point-fitted, non-TU counterexample must possess a **nonempty closed crowded non-TU core**. Merely attaching isolated singular points to a TU open part cannot produce one. The core can be the whole space, so the proposition does **not** imply the existence of any regular/TU open neighborhood.

## 5. Research next step

We should test whether local compactness imposes extra structure on this canonical closed crowded core. Two independent possible directions:

1. Find a local compactness argument producing a nonempty TU open part (or otherwise forcing an isolated point in the core) from point-fittedness; this would be a route toward positive (LC-PT).
2. Construct a locally compact sober \(T_1\), point-fitted space whose entire non-TU core is crowded, paying special attention to maps out of nonspatial test locales and Boolean witnesses.

A concrete [Boolean lax-double control](ProjectA_LCPT_BOOLEAN_LAX_DOUBLE_NONLC_CONTROL_2026-11-15.md) realizes a crowded closed non-TU core in a **compact** point-fitted T1 non-TU space, but fails local compactness by a direct way-below calculation. Thus the theorem alone decides neither the full (LC-PT) implication nor its locally compact boundary. Keep (A-DUAL) deferred and do not misidentify \(\mathcal A\vee\mathcal A^{op}\) with a new symbol: the latter is the pre-existing \(\mathcal S\); see [lower-hierarchy notation guide](ProjectA_LOWER_HIERARCHY_NOTATION_2026-11-15.md).
