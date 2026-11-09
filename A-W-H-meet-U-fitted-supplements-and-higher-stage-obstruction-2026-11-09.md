# Project A — The intermediate relation H ∧ U: fitted supplements, barriers, and stage re-entry

**9 November 2026 · New internally checked working note.** The question is when \(\mathcal W=\mathcal H\wedge\mathcal U\), where \(\mathcal W=\operatorname{cl}(\operatorname{fit}\Delta)\), \(\mathcal H\) is the least simultaneously closed-and-fitted diagonal hull, and \(\mathcal U\) is the Urysohn closed relation. The finite-cover approximation questions Q/Q′ remain **deferred**. Antecedent examples and the formal hull calculus are from the externally corroborated October post-V hierarchy; newly derived conditions and examples here are not externally audited or originality-checked.

Let \(Q=\mathcal O(X)\oplus\mathcal O(X)\),
\[
d=d_{\mathcal W},\qquad u=d_{\mathcal U},\qquad
f=d_{\mathcal F},\qquad h=d_{\mathcal H}.
\]
We have \(f\le h\le d\), \(f\le u\le d\), and \(\mathcal W=C(d)\), \(\mathcal U=C(u)\), \(\mathcal H=C(h)\). The relation of interest is the **closed** sublocale
\[
\mathcal H\wedge\mathcal U=C(h\vee u),
\quad \mathcal W\le\mathcal H\wedge\mathcal U.
\]

## 1. Exact fitted-supplement theorem

**Theorem 1.1 (arbitrary locales).** The following are equivalent:

(i) \(\mathcal W=\mathcal H\wedge\mathcal U\).

(ii) There exists \(r\in Q\) with
\[
\boxed{r\le d,\quad d=u\vee r,\quad C(r)\text{ fitted}.}
\tag{1.1}
\]

(iii) There is a family \(r_i\le d\), possibly infinite, with each \(C(r_i)\) fitted, such that
\[
\boxed{d=u\vee\bigvee_i r_i.}\tag{1.2}
\]

*Proof.* If (ii), then W≤C(r), and the minimality of H among closed fitted superlocales of W gives H≤C(r). Therefore
\[
W\le H\wedge U\le C(r)\wedge C(u)=C(r\vee u)=C(d)=W.
\]
For (i)⇒(ii), take r=h; H=C(h) is fitted, r≤d, and C(d)=C(h∨u) implies d=h∨u. For (iii)⇒(ii), let r=∨r_i: C(r)=∧C(r_i) is closed and fitted, because **arbitrary meets** preserve both properties. (ii)⇒(iii) is a one-term family. □

The theorem is an **exact existence criterion**, not yet a simpler axiom. It is useful as a *certificate*: one may construct a fitted barrier C(r) larger than H, without computing H itself. The two extremal certificates are r=0 if W=U, and r=d if W=H.

**Relative version.** In the fitted functional envelope \(\mathcal F=C(f)\), one may require \(f\le r\le d\) and prove fittedness of \(C_{\mathcal F}(r)\) intrinsically in F. Because F is fitted in X², the relative fittedness transfers to the whole square. A sufficient test is relative regular generation:
\[
r=\bigvee\{c\ge f:(c\to f)\vee r=1\}.
\tag{1.3}
\]
If (1.3) and \(d=u\vee r\), then W=H∧U. One can replace (1.3) by the **finite-branch shrinking criterion within F**, as established in [the previous abstract note](A-W-equals-H-abstract-finite-branch-shrinking-2026-11-09.md).

**Caution: absolute regularity is too strong.** If r≤d, then C(r) contains Δ. The diagonal-neighborhood lemma of the [relative fitness note](A-W-equals-H-relative-fitness-functional-envelope-2026-11-09.md) proves
\[
\bigvee_{c\prec_Qr}c\le u.
\tag{1.4}
\]
Therefore if r is **absolutely** rather-below generated, r≤u. In a certificate \(d=u\vee r\), that forces d=u, i.e. W=U. To handle genuinely mixed W<U cases, relative regularity in F is the correct hypothesis, or use nonregular shrinking.

## 2. An intrinsic Boolean-valued obstruction without mentioning H

Define
\[
\mathscr R_d=\{r\in Q:\ r\le d,\ C(r)\text{ is fitted}\}.
\]
The largest member \(h=\bigvee\mathscr R_d\) is exactly \(d_H\), since
\[
H=\bigcap_{r\in\mathscr R_d}C(r)
=C\!\left(\bigvee\mathscr R_d\right).
\]
The equality uses that H itself is a closed fitted superlocale of W.

**Theorem 2.1.** The strict inequality \(W<H\wedge U\) holds iff there are a nontrivial complete Boolean frame B and a frame homomorphism \(g:Q\to B\) such that
\[
\boxed{
g(d)=1,\qquad g(u)=0,\qquad
g(r)=0\quad\text{for every }r\in\mathscr R_d.
}
\tag{2.1}
\]

*Proof.* The residual sublocale \(E=H\wedge U\wedge O(d)\) is nonzero precisely when W<H∧U, because W=C(d) is the complementary closed sublocale. If E≠0, its Booleanization gives a nontrivial frame homomorphism g sending d to top and sending u,h to bottom. Since r≤h for every r in \(\mathscr R_d\), this gives (2.1). Conversely (2.1) gives g(h)=g(∨r)=0, hence g factors through both closed sublocales C(h),C(u), as well as O(d), witnessing E≠0. □

Interpretation: failure requires a **Boolean-valued Urysohn pair outside W** that defeats *every fitted closed barrier* containing W. This is distinct from the earlier Boolean witness for W itself; this condition does not mention W₂.

## 3. Comparability reductions and relative hulls

If H≤U, then H∧U=H, so
\[
W=H\wedge U\iff W=H.
\]
If U≤H, then H∧U=U, so
\[
W=H\wedge U\iff W=U.
\]
If U is **fitted** (it is already closed and contains Δ), then H≤U, and the first condition applies. For coherent locales W=U always, so the second equality follows without fitting W.

Both H∧U and W are closed sublocales of U. Moreover H∧U is *fitted intrinsically in U*, as the restriction of the ambient fitted H. But it need not be the **least** closed-and-fitted sublocale of U containing W; ambient hull operations can leave U and later re-enter it. We must not collapse the problem to a relative fittedness test inside U without further hypotheses.

**Five-point stage re-entry control, for arbitrary closed S⊆U (not specifically W,U).** Let
\[
Z=\{a,s,b,t,c\},\quad a<s,\ b<s,\ b<t,\ c<t,
\]
upper Alexandrov, with no additional strict comparisons. Let \(S=C(d_S)=\{a\}\) and let the closed sublocale \(U_0=\{a,c\}\). Both are downsets. In finite Alexandrov posets, fitting is up-saturation and closing is down-saturation. Starting from S:
\[
S_0=\{a\},\qquad
S_1=\operatorname{cl}\operatorname{fit}(S_0)=\{a,s,b\},
\]
\[
S_2=\operatorname{cl}\operatorname{fit}(S_1)=Z.
\]
Yet \(S_0\cap U_0=S_1\cap U_0=\{a\}\), while \(S_2\cap U_0=\{a,c\}>\{a\}\). Thus even the **first closed fitted stage** may contribute nothing on restriction, while the second stage contributes a new point. This does *not* produce a counterexample for the special diagonal relations W and U, but prohibits an unproved one-step criterion in general.

At the frame level, the existing κ-iteration gives closed stages \(C(a_0),C(a_1),\ldots\), \(a_0=d\), \(a_{\alpha+1}=\kappa(a_\alpha)\), and \(a_\lambda=\bigwedge_{\beta<\lambda}a_\beta\). Its stable value is \(h\). Therefore the exact iterated test is
\[
\boxed{W=H\wedge U\iff d=u\vee a_\infty.}
\tag{3.1}
\]
It is not justified to replace \(a_\infty\) with \(a_1\). Also at limit stages \(u\vee\bigwedge_\beta a_\beta\) need not equal \(\bigwedge_\beta(u\vee a_\beta)\) in an arbitrary frame. The fitted-supplement certificate of §1 avoids this stage-by-stage verification entirely.

## 4. Direct-sum preservation and exact order-pattern tests

For a **finite** localic disjoint sum \(X=\coprod_{i=1}^n X_i\), the relations W,U,H restrict componentwise to the clopen diagonal blocks \(X_i^2\), and all their mixed-component blocks vanish. For W this was checked in [the Boolean W note](A-W-as-Boolean-cover-relation-and-lax-naturality-2026-11-09.md); for U mixed blocks are far; for H, each diagonal-component block is closed and fitted iff its intrinsic component relation is, and restriction/extension along clopen components is exact. Thus
\[
\boxed{W(X)=H(X)\wedge U(X)
\iff \forall i,\ W(X_i)=H(X_i)\wedge U(X_i).}
\tag{4.1}
\]
We only need finite sums for the following controls.

**Equality with strictness on BOTH sides and H,U incomparable in one locale.** Let P be the coherent five-point upper-Alexandrov fence \(m>a<k>b<n\) from the [coherent W=H study](A-W-equals-H-coherent-maximal-point-criterion-2026-11-09.md). It satisfies
\[
W(P)=U(P)<H(P)=F(P)=P^2.
\]
Let A be the compact noncoherent scattered T₁ \(\alpha\)-\(\beta\)-\(\gamma\) locale from the **externally audited** October post-V hierarchy:
\[
W(A)=H(A)<U(A)=F(A).
\]
For the compact disjoint sum X=P⊔A,
\[
\boxed{
W(X)=H(X)\wedge U(X),\quad
W(X)<H(X),\quad W(X)<U(X),\quad
H(X)\nleq U(X),\quad U(X)\nleq H(X).
}
\tag{4.2}
\]
These inequalities are witnessed in distinct clopen components; this is **not** an indecomposable example. The fitted supplement r can be chosen explicitly: on P² take r=0, on A² take r=d_W(A), and on both mixed blocks take r=1 (so its complementary closed relation has no mixed blocks). Then C(r) is closed fitted, r≤d_W(X), and \(d_W(X)=d_U(X)\vee r\).

**Genuinely strict new intermediate relation.** Let T be the compact noncoherent T₀ \(p<x\) two-sheet example from the same externally audited hierarchy, with
\[
W(T)<H(T)=U(T)=F(T).
\]
For the compact disjoint sum \(Y=P\sqcup A\sqcup T\), write \(G=H\wedge U\). Then
\[
\boxed{
W(Y)<G(Y)<H(Y),\qquad
W(Y)<G(Y)<U(Y),
}
\tag{4.3}
\]
and H(Y),U(Y) are incomparable. Strictness \(W<G\) occurs on T, \(G<H\) on P, \(G<U\) on A. Thus the meet is an **independent rung**: it can coincide with W even when W is strictly below both factors, or can be genuinely strictly intermediate below each factor. The construction is disconnected; existence of a compact *connected* or indecomposable example remains untested.

## 5. Pointless precursors in T₁ spaces

Suppose \(X^2\) is spatial and T₁ (as for locally compact sober T₁ spaces). If W<H∧U, then the **closed** spatial sublocales W and H∧U have distinct ordinary point relations, so there exists
\[
p\in \operatorname{pt}(H\wedge U)\setminus\operatorname{pt}(W).
\]
But the *first fitted hull* \(\operatorname{fit}(W)\) has exactly the same ordinary points as W: for each point q∉W, the open \(X^2\setminus\{q\}\) contains W and therefore excludes q from fit(W). Thus any new ordinary U-compatible point cannot arise in the **first fitting step**; it must emerge when closure is applied to a nonzero pointless fitted residual.

Indeed, because H>W, the first fitting step must be strictly larger than W (otherwise W would already be fitted). The residual
\[
E_1=\operatorname{fit}(W)\wedge O(d_W)
\]
is then nonzero and **pointless** by the earlier T₁ theorem. Later closed stages may turn the closure of this pointless precursor into new ordinary points.

**Sharpening.** Because fit(W)>W, its first **closed** hull (C_1=\operatorname{cl}(\operatorname{fit}(W))) is strictly larger than W. In the spatial square this guarantees some new **ordinary point already at the first closed stage**, although it need not lie in U. The additional U-compatible point witnessing (W<H\wedge U) may occur at a later successor or limit stage, as the 5-point general-closure control in §3 warns.

This gives a useful necessary mechanism for a T₁ counterexample to W=H∧U: **pointless precursor followed by the creation of ordinary points under closure, with eventual re-entry into the Urysohn relation**. Do not infer that a one-step test suffices or that this mechanism has been realized by a specific diagonal example.

## 6. Research directions constrained by the results

The most useful exact organizing principle is (1.1): find a closed fitted *supplement* to the Urysohn complement inside the W complement. The previous finite-branch shrinking theorem can certify fittedness of a supplement without certifying W itself. The κ-iteration shows where unrestricted one-step arguments could fail.

Potential bounded follow-ups:
- Identify a **non-disjoint-sum** noncoherent example with both W<H and W<U but W=H∧U; the direct-sum (4.2) proves no algebraic obstruction but does not settle connected geometry.
- Test a finite-branch barrier on the U-residual of an example where W is not fitted; this is more targeted than repeating proofs of W=H.
- In spatial T₁ examples, investigate whether a closure of the first pointless fitted residual can really introduce an ordinary point belonging to U outside W; do not embark on an unbounded counterexample search without a specific model.

**Status:** New working deductions, no external audit; existing theorem ledger remains unchanged; Q/Q′ remain deferred.
