# Project A — a dense-set family behind the rational-bridge counterexample

**14 November 2026 · new INTERNAL corollary, not independently blind-refereed as a separate theorem.** This note generalizes the already audited [rational-bridge example](ProjectA_Q_DENSE_RATIONAL_BRIDGE_CANONICAL_2026-11-14.md) and identifies the precise condition making its finite-cover density lemma work. The case `E=ℚ` alone suffices to refute Q and Q′.

## Construction

For any subset \(E\subseteq\mathbb R\), let

\[
 X_E=S\sqcup T\sqcup\{b_e:e\in E\}
\]

with `S` and `T` disjoint open copies of ℝ and basic neighborhoods

\[
 N(e,\varepsilon)=\{b_e\}
 \cup\{s_x:e-\varepsilon<x<e\}
 \cup\{t_x:e<x<e+\varepsilon\}.
\]

The projection \(p:X_E\to\mathbb R\) identifying all three labels with their real parameter is étale. Every point has an open interval chart, so `X_E` is locally compact, sober and `T₁`. The bridge subset is a closed discrete subspace of `X_E`, so `X_E` is second countable **if and only if E is countable**.

For any X-open cover \(\mathscr C\), set \(m_{\mathscr C}=\bigvee_{c\in\mathscr C}s^*c\wedge t^*c\), an open of ℝ.

## Sharp finite-cover criterion

**Proposition (internal).** The following are equivalent:

1. `E` is dense in ℝ.
2. For **every finite open cover** \(\mathscr F\) of \(X_E\), the matching open \(m_{\mathscr F}\) is dense in ℝ.

*Proof of (1)⇒(2).* Suppose a finite cover \(\{c_1,\ldots,c_n\}\) has matching open disjoint from a nonempty interval `I`. As in the canonical proof, put \(A_i=s^*c_i\cap I\), \(B_i=t^*c_i\cap I\). They are disjoint opens. Every \(e\in E\cap I\) belongs to a bridge point covered by some \(c_i\); its one-sided section germs force \(e\in\partial_I A_i\). Thus

\[
 E\cap I\subseteq\bigcup_{i=1}^n\partial_I A_i.
\]

The right side is a finite union of nowhere-dense closed sets, contradicting the density of `E∩I` in `I`.

*Proof of (2)⇒(1).* If `E` is not dense, choose a nondegenerate compact interval \(K\subseteq\mathbb R\setminus\overline E\). Both \(s(K)\) and \(t(K)\) are closed in \(X_E\): they are closed in their own open sections, and no bridge point has parameter in `K` or can accumulate on them from outside `K`. They are disjoint. Hence

\[
 \mathscr F=\{X_E\setminus s(K),\ X_E\setminus t(K)\}
\]

is a binary open cover. For every \(x\in K\), neither cover member contains both \(s_x\) and \(t_x\). Therefore \(m_{\mathscr F}\cap\operatorname{int}(K)=\varnothing\), contrary to (2). □

## Corollary for Q and Q′

For **any dense E**, the section atlas \(\{S,T\}\cup\{N_e:e\in E\}\), where \(N_e=\bigcup_{\varepsilon>0}N(e,\varepsilon)\), gives `D(X_E)=Δ`. The density criterion and Isbell's theorem give \(B(J)\le D_2(X_E)\wedge J\), with \(J=S\times_{\mathbb R}T\cong\mathbb R\), hence \(J,J^{op}\le W_2\). The fiber square \(F=X_E\times_{\mathbb R}X_E\) is closed and spatial by its open section-chart cover; its remaining ordinary points are diagonal or bridge/section inseparable pairs, all in `I`. Therefore exactly as in the audited `E=ℚ` case,

\[
 \boxed{W(X_E)=I(X_E)<W_2(X_E)=U(X_E)=F.}
\]

The new step is only the replacement of the dense countable set `ℚ` by arbitrary dense `E`; every other proof ingredient is unchanged. **The equivalence of density and finite-cover matching is special to this family**, not proposed as an intrinsic characterization for arbitrary étale maps.

## Significance and boundary

The rational parameter set is not a delicate arithmetic feature: its sole role is **density**. Taking dense countable `E` preserves second countability; taking dense uncountable `E` yields further locally compact sober `T₁` counterexamples without second countability. When `E` is not dense, this *particular finite-cover-density mechanism* fails, but this alone does not prove Q or Q′ positive for `X_E`.

The construction illustrates a finite-to-full **descent failure**: an infinite monic section atlas proves full compatibility rigid, while every finite cover is forced by the dense branch set to match the two global sections on a dense base open. The least dense Boolean sublocale detects that residual matching, and its ambient closed hull is large. A natural next question is to axiomatize this mechanism for étale maps over more general regular bases and compare it against cover-theoretic positive hypotheses such as locally finite refinements.

