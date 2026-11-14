# Project A — density-phase external referee reconciliation and next steps

**14 November 2026.** Consolidation after an independent blind referee report, its chat addendum, and internal rechecks. **Universal Questions Q and Q′ remain OPEN.** The external referee reports no incorrect theorem in the density-phase packet; source-dependent historical asides were not reviewed. Their new mathematical suggestions, recorded below, are independently checked where indicated and **must not be misrepresented as separately externally refereed results**.

## 0. Audit record and hierarchy of confidence

Reviewed packet: [blind proof packet](ProjectA_Q_DENSITY_FINITECUT_EXTERNAL_BLIND_PACKET_2026-11-14.md), [blind prompt](ProjectA_Q_DENSITY_FINITECUT_EXTERNAL_BLIND_PROMPT_2026-11-14.md). Our earlier [internal audit](ProjectA_Q_DENSITY_FINITECUT_INTERNAL_ADVERSARIAL_AUDIT_2026-11-14.md) was withheld until the referee completed their first-pass report. The referee's response was submitted privately by the user. We reproduce no unattributed source claims here.

**Externally independently checked:** the relative monochromatic and profile restrictions; conditional spatial-Baire test criterion; finite-cut identity; binary-cover reduction; Polish and Scott countercontrols; fixed-point nontransfer; Boolean visibility equivalence; and the closed-atomic support theorem. The reviewer found no false theorem, but requested localic-product justifications and a repaired existential argument in the Scott check.

**New referee observations independently checked here but not externally refereed as standalone theorems:** the decider lemma, locally finite cover theorem, arbitrary-finite-family cut identity, fixed-point-set viewpoint, and binary/finite iteration estimate. The six-point Alexandrov example was checked independently in its order-theoretic form. The quasi-Polish observation is supported by the cited Heckmann and de Brecht results, but its usefulness toward Q′ is still unproven.

## 1. Finite-cut identity and fixed points: sharpened statement

For elements \((x_i)_{i=1}^n,(y_i)_{i=1}^n\) of **any distributive lattice**, put \(x_S=\bigvee_{i\in S}x_i\), \(y_S=\bigvee_{i\in S}y_i\). Then

\[
\boxed{\;
\bigvee_{i=1}^n(x_i\wedge y_i)
=\bigwedge_{S\subseteq[n]}
\left[(x_S\wedge y_S)\vee
(x_{S^c}\wedge y_{S^c})\right].
\;} \tag{1.1}
\]

This requires **no cover assumption**. In the usual two-valued evaluation, if either index support is empty then both sides vanish; if both are nonempty, the original proof applies, using \(S=A\) when \(A\cap B=\varnothing\).

Apply (1.1) with \(x_i=f_i\boxtimes1\), \(y_i=1\boxtimes f_i\) in \(P=\mathcal O(X^2)\). When the \(f_i\) form a finite **cover**, its cuts define genuine binary covers. Consequently \(D_{\mathrm{bin}}=D_2\). The cover condition is needed **here**, not in the algebraic identity.

There is also a simple universal explanation for Corollary 2.2. Regarding sublocales as fixed-point subsets of \(P\),

\[
D_{\mathrm{bin}}=\operatorname{Fix}(\Phi_{\mathrm{bin}}),\quad
D_2=\operatorname{Fix}(\Phi_2),\quad
D=\operatorname{Fix}(\Phi).
\tag{1.2}
\]

Thus the binary and finite operators have identical fixed-point sets (and identical stabilized nuclei), **not necessarily identical one-step values**. Similarly \(D_2=D\) if and only if all \(\Phi_2\)-fixed opens are \(\Phi\)-fixed. By contrast Q′ concerns only their **least** fixed opens above \(0\).

A quantitative bound, suggested in the chat addendum, also follows: with \(T=\Phi_{\mathrm{bin}}\),

\[
\boxed{T(d)\le\Phi_2(d)\le T^\omega(d)}.
\tag{1.3}
\]

Each finite-cover residual is a finite composition of binary-cover residuals, by (1.1) and \((u\wedge v)\to d=u\to(v\to d)\). The latter is bounded by some \(T^m(d)\), and one takes the join over finite covers. The inequality is pointwise; statements about *exact ordinal rank multiplication* need a separate theorem.

### 1.1 A strict six-point stagewise example

Let \(X\) be the finite Alexandrov poset on \(p,p_1,p_2,r,q,q_1\), with generating comparisons
\(p<p_1,\ p<p_2,\ r<p_2,\ r<q_1,\ q<q_1\).
In the square up-set frame put \(d=\{(p_2,q_1)\}\).

The finite cover \(F=\{\uparrow p,\uparrow r,\uparrow q\}\) has matching square meeting \(\uparrow(p,q)\) only at \((p_2,q_1)\). Hence \((p,q)\in(w_F\to d)\subseteq\Phi_2(d)\).

For a binary cover \(\{u,v\}\), if \((p,q)\in w_{\{u,v\}}\) then its residual cannot contain \((p,q)\), since \((p,q)\notin d\). Otherwise, after swapping \(u,v\), we must have \(p\in u\setminus v,\ q\in v\setminus u\). Avoiding a match at \((p_1,q_1)\) and \((p_2,q)\) forces \(q_1\notin u\) and \(p_2\notin v\). But \(r\in u\cup v\), and its upper bounds \(q_1,p_2\) make either requirement fail. Therefore \((p,q)\notin\Phi_{\mathrm{bin}}(d)\).

Thus \(\Phi_{\mathrm{bin}}(d)<\Phi_2(d)\) in a six-point spatial locale, even though (1.2) holds universally.

## 2. Decider lemma: common mechanism for weak-defect obstructions

Let \(h,k:L\to M\) be frame maps with \(M\neq0\), and let \(C=(c_i)_{i\in I}\) be a cover satisfying

\[
h(c_i)\wedge k(c_i)=0\quad(i\in I).
\]

Suppose \((h,k)\) matches every **binary coarsening** \(B_S=\{\bigvee_{i\in S}c_i,\bigvee_{i\notin S}c_i\}\).

Call \(b\in M\) a *decider* for \((h(c_i))\) when for each \(i\) either \(b\le h(c_i)\) or \(b\wedge h(c_i)=0\).

**Lemma 2.1 (no nonzero deciders).** No nonzero element of \(M\) decides \((h(c_i))\) or \((k(c_i))\).

*Proof.* If \(b\) is a decider, put \(S=\{i:b\le h(c_i)\}\), \(a_S=\bigvee_{i\in S}c_i\), \(b_S=\bigvee_{i\notin S}c_i\). Then

\[
b\wedge h(b_S)=0,\qquad
b\wedge k(a_S)=0
\]

by the defining dichotomy and \(h(c_i)\wedge k(c_i)=0\). Meeting the binary matching identity
\(h(a_S)\wedge k(a_S)\vee h(b_S)\wedge k(b_S)=1\)
with \(b\) therefore yields \(b=0\), contradiction. Swap coordinates for the other assertion. \(\square\)

This condenses the hyperconnected-patch eliminator, atomless closed-support obstruction, and (in spatial Baire settings) nowhere-dense incidence-pattern fibers. It does **not** by itself solve Q′: it only exploits coarsenings of the offending \(C\), so it holds for generalized **weak** defects as well as hypothetical open holes.

A direct point-free corollary: below every nonzero \(b\in M\), **infinitely many** \(h(c_i)\) and infinitely many \(k(c_i)\) have nonzero meet with \(b\). If only finitely many met \(b\), successively shrink \(b\) to decide each of that finite set; all remaining indices are already disjoint, contradicting Lemma 2.1.

## 3. Locally finite cover theorem (referee suggestion; independently checked)

**Theorem 3.1.** Let \(C\) be an open cover of \(X\). Suppose another open cover \(G\) of \(X\) has the property that every \(g\in G\) meets only finitely many members of \(C\). Then

\[
\boxed{D_2(X)\le O_{X^2}(w_C).}
\tag{3.1}
\]

*Proof.* Let \(h,k:L\to M\) match every finite \(L\)-cover and write \(m=\bigvee_{c\in C}h(c)\wedge k(c)\). For \(g\in G\), set
\(C_g=\{c\in C:g\wedge c\ne0\}\) and \(t_g=\bigvee(C\setminus C_g)\).
The family \(C_g\cup\{t_g\}\) is a **finite cover**, and \(g\wedge t_g=0\). Its matching identity, met with \(h(g)\), gives

\[
h(g)\le
\bigvee_{c\in C_g}h(c)\wedge k(c)
\le m.
\]

Since \(G\) covers, \(\bigvee_{g\in G}h(g)=1\le m\). Thus \(m=1\), proving (3.1) by the universal factorization property of \(D_2\). \(\square\)

**Corollary 3.2.** If every open cover of \(X\) admits a locally finite refinement (with this precise frame-theoretic meaning), then \(D_2=D\), and hence \(W_2=W\). No spatiality, separation, or Baire hypotheses are required.

This is stronger in hypotheses/conclusion in a different direction from the previously known spatial hereditary-Baire point-finite result, and is to be credited to the external referee pending a literature search. **No claim of novelty relative to the point-free paracompactness literature is made.**

## 4. Closed-atomic equals scattered-space frames

The external referee supplied the converse to the earlier spatial-scattered corollary. If every proper closed interval \([e,1]\) of \(L\) contains an atom, then \(L\) is spatial and its \(T_0\) point space is scattered.

Sketch of the separating-point argument: if \(u\nleq v\), set \(e=u\to v<1\), choose an atom \(a>e\), and let \(p=a\to e\). Then \(p\) is a completely prime element, \(v\le p\), and \(u\nleq p\); consequently the corresponding point separates \(u\) from \(v\). The atom condition on each interval becomes an isolated point in every nonempty closed subspace. Conversely, the earlier proof shows that spatial scattered spaces have atomic closed interval frames. Every scattered \(T_0\) space is sober, since an irreducible closed set containing an isolated point is the closure of that point.

Therefore the **closed-atomic condition is a frame characterization of the ordinary scattered \(T_0\) class**, not a newly discovered wider class of pointless locales. It remains a useful intrinsic proof tool. Distinguish this from alternative terminologies for “scattered locale”.

## 5. Corrections to the controls and visibility wording

- **Scott product:** In the example \(X=\mathcal P(\omega)\setminus\{\varnothing\}\) with Scott topology, every basic \(\uparrow P\) is compact open, so \(X\) is locally compact and sober. The localic square agrees with the topological product. Its closed sublocale \(R\) of disjoint pairs is therefore represented by the ordinary closed subspace, allowing the spatial Baire and finite-density arguments as written.
- **Scott has a finest cover:** \(C=\{c_n\}\) refines every open cover of \(X\): any cover member containing \(\{n\}\) contains all of \(c_n=\uparrow\{n\}\). Thus \(D=O(w_C)\) and \(W=U=X^2\) for an elementary reason. The example remains valid and important as a **negative control**, not as an example in the open regime of Q′.
- **Polish control:** The localic square of the Polish \(X=[\omega]^\omega\) is spatial; it is regular, so \(D_2=D=\Delta\) and \(W_2=W=U=\Delta\). The disjoint-pair closed relation lies outside \(W_2\).
- **Existential Scott correction:** The old phrase “the particular \(B(R)\) has nowhere-dense closure, hence condition (4) fails” is not logically sufficient by itself because (4) is existential. The valid justification is \(K_C=R\) itself is closed nowhere dense in \(W_2=X^2\), so no \(B\le A_C\le K_C\) can have closure with nonzero interior.
- **Visiblity is not a new constraint:** Proposition 6.1 remains an exact reformulation of Q′ at the **canonical** \(W_2\), not a solution.
- **Terminology:** \(D_2\) as fitted sublocale means *finite-cover tests*, not the second iterate. The proofs distinguish open complements \(C(w)\) from closure \(\operatorname{cl}S\).

## 6. Countably presented / quasi-Polish intermediate setting

By Heckmann's theorem, countably presented locales are spatial and correspond to quasi-Polish spaces (see de Brecht–Kawai, *On the commutativity of the powerspace constructions*, arXiv:1709.06226, §1, citing Heckmann). Quasi-Polish spaces are Baire (de Brecht, *A generalization of a theorem of Hurewicz for quasi-Polish spaces*, 2018). Countable products and open/closed subspaces preserve quasi-Polishness.

Thus if \(X\) has a countable frame presentation, its localic \(X^2\), the closed \(W_2(X)\), and any relatively open hole \(E\subseteq W_2\) are represented by quasi-Polish, hence Baire, spaces. Every \(X\)-cover has a countable subcover, since \(X\) is second countable and spatial. Hence **Parts II–III's Baire/spatial hypotheses become automatic** and any offending \(C\) can be reduced to a countable cover.

**Important unsolved gap:** Countable presentation does *not* imply the existence of a countable family of finite-cover tests detecting every \(C\)-bad pair. The bad loci are closed nowhere-dense, and second countability/Lindelöfness cannot select a countable subcover of an arbitrary cover by **closed** bad loci. No proof of Q′ for quasi-Polish spaces follows.

**Intermediate question (QP-Q′).** Is \(W_2(X)=W(X)\) for every quasi-Polish \(X\)? This is a concrete target at which our relative category method becomes automatically available. It remains open in this programme.

## 7. Remaining research priorities

1. **Canonical maximality, not an arbitrary finite-fixed relation:** the Scott closed/Baire control refutes any universal “finite-square density on a Baire closed relation implies C-density” proof. Require actual nonzero relative openness in \(W_2\).
2. **Arbitrary ambient binary covers:** coarsenings of \(C\) alone cannot distinguish weak/strong defects (decider lemma); the finite-cut reduction makes arbitrary binary ambient covers sufficient. Seek a geometric mechanism joining these tests inside the canonical \(W_2\).
3. **Concrete controls within the open regime:** favor a nonregular, noncompact locale without a finest cover, with \(W\ne U\) and finite closure beyond rank one. Reuse the existing Arrieta/two-apex and Cohen controls rather than rebuilding their solved cases; test whether a new construction genuinely evades the proven positive classes.
4. **Quasi-Polish Q′ as intermediate problem:** exploit automatically Baire open holes and countable bad covers; do **not** infer a countable separating family of finite covers without proof.
5. **Lower priority:** stagewise binary-vs-finite operator calculus (bound (1.3) and six-point strictness); possible topological reformulation of Q via \(\theta=U\). Both are useful for bookkeeping and countercontrol tests, but neither currently furnishes a density mechanism.
6. **Defer:** proposed “largest binary-local relation” certificate calculus until “binary-local” and the maximality claim are formally stated and proved; failed per-member mixing/gluing heuristics remain an inventory item.

No headline claim is asserted beyond the stated theorems and repairs. Q and Q′ remain open, and the next research segment should test an actual **canonical** density mechanism or candidate, not simply derive another necessary condition already shared by all weak defects.
