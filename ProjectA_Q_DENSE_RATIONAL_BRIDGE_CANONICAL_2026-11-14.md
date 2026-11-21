> **21 NOV 2026 — AFTER-AUDIT LITERATURE COROLLARY (NOT PART OF THE ORIGINAL BLIND PACKET).** Matthew de Brecht, *Quasi-Polish Spaces*, *Ann. Pure Appl. Logic* 164 (2013), 356–381, Theorem 44, proves that every **countably based locally compact sober** space is quasi-Polish. The X constructed below has all three properties, so the same externally reviewed example proves **Q and Q′ fail even for locally compact quasi-Polish T₁ spaces** (necessarily non-Hausdorff). This is a direct consequence of an established published theorem and the existing audited construction, not a new claim of independent priority. Source: https://arxiv.org/abs/1108.1445 ; precise theorem-number comparison https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=865 . Endgame source ledger: [focused counterexample and rank review](ProjectA_ENDGAME_COUNTEREXAMPLE_RANK_LITERATURE_FOCUSED_REVIEW_2026-11-21.md).

# Project A — canonical dense-rational-bridge counterexample to Q and Q′

**14 November 2026 · consolidated after independent blind audit and a separate internal audit.** The construction and its main conclusion have survived both reviews. The equivalence with the project's original cover-operator questions is checked in §1 below. This is a correctness record, **not** a claim of literature originality or priority.

## 0. The result

For a locale `X`, let `D(X)=fit(Δ_X)` be its full fitted diagonal, let `D₂(X)` be the intersection of diagonal cover squares over **finite** covers, and write

\[
 I(X)=\operatorname{cl}_{X^2}\Delta_X,\qquad
 W(X)=\operatorname{cl}_{X^2}D(X),\qquad
 W_2(X)=\operatorname{cl}_{X^2}D_2(X),
\]

with `U(X)` the closed Urysohn relation. In this document `X²` means the **localic** product.

**Theorem.** There is a second-countable, sober, locally compact, \(T_1\), non-Hausdorff space \(X\), admitting an étale map \(p:X\to\mathbb R\) with fibers of cardinality two or three, such that

\[
\boxed{D(X)=\Delta_X,\qquad
 W(X)=I(X)\;<\;W_2(X)=U(X)=X\times_{\mathbb R}X.}
\tag{T}
\]

Consequently both original universal questions fail:

- **Q′:** `W(X)=W₂(X)` for all locales is false.
- **Q:** `W₂(X)=U(X) ⇒ W(X)=U(X)` for all locales is false.

The strict difference in (T) concerns **closed hulls**; a mere `D₂≠D` would not have sufficed.

## 1. Exact correspondence with the original Φ, Φ₂ questions

Put \(P=\mathcal O(X^2)\). For an X-open cover \(\mathscr C\), set

\[
 w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c.
\]

The square opens \(w_{\mathscr C}\) are cofinal among all opens containing the diagonal. Consequently

\[
 D(X)=\bigwedge_{\mathscr C\text{ cover}}O(w_{\mathscr C}),\qquad
 D_2(X)=\bigwedge_{\mathscr F\text{ finite cover}}O(w_{\mathscr F}).
\tag{1.1}
\]

The original pre-nuclei are

\[
 \Phi(q)=\bigvee_{\mathscr C}(w_{\mathscr C}\to q),\qquad
 \Phi_2(q)=\bigvee_{\mathscr F\text{ finite}}(w_{\mathscr F}\to q).
\tag{1.2}
\]

The nucleus of the open sublocale `O(w)` is \(q\mapsto w\to q\). Since every such map is inflationary, a point \(q\in P\) is fixed by \(\Phi\) exactly when fixed by **every** \(w_{\mathscr C}\to-\). Thus the fixed-point frame of \(\Phi\) is the sublocale `D(X)` in (1.1), and similarly `Fix(Φ₂)` presents `D₂(X)`. The least fixed points above `0` are obtained by stabilized transfinite iteration. For any sublocale `S` with nucleus \(j_S\), its least closed hull is \(C(j_S(0))\). Therefore

\[
 \boxed{W(X)=C(\Phi^\infty(0)),\qquad
 W_2(X)=C(\Phi_2^\infty(0)).}
\tag{1.3}
\]

For completeness, the first-stage coincidence is

\[
 z:=\Phi(0)=\Phi_2(0)
 =d_U:=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
 \qquad U(X)=C(d_U).
\tag{1.4}
\]

Here `*` means pseudocomplement in `O(X)`. To see (1.4), any far rectangle \(a\boxtimes b\) with \(a^*\vee b^*=1\) is disjoint from the square of the **binary** cover \(\{a^*,b^*\}\); hence \(d_U\le\Phi_2(0)\). Conversely, if a basic rectangle \(a\boxtimes b\) lies in \(w_{\mathscr C}^*\), then for each \(c\in\mathscr C\), \((a\wedge c)\boxtimes(b\wedge c)=0\). The standard nonvanishing property of basic localic rectangles implies either \(a\wedge c=0\) or \(b\wedge c=0\). Partition the cover accordingly; its two joins are below \(a^*\) and \(b^*\), respectively. Thus \(a^*\vee b^*=1\), proving \(w_{\mathscr C}^*\le d_U\). Every open of a localic product is a join of basic rectangles, so \(\Phi(0)\le d_U\).

As `Φ` and `Φ₂` are monotone and inflationary, stabilization at their common first value `z` is equivalent to being fixed there:

\[
 \begin{aligned}
 \Phi_2(z)=z&\iff W_2(X)=U(X),\\
 \Phi(z)=z&\iff W(X)=U(X).
 \end{aligned}
\tag{1.5}
\]

This proves that the questions tested by (T) are **exactly** the project's earlier operator formulations, not substitutes. Also, `W=W₂` is equivalent to `D` being dense in `D₂`, hence by Isbell's density theorem to \(B(D_2)\le D\), as in the original Q′ criterion.

## 2. The space and the étale atlas

Let

\[
 X=S\sqcup T\sqcup H,
 \quad S=\{s_x:x\in\mathbb R\},\quad
 T=\{t_x:x\in\mathbb R\},\quad
 H=\{b_q:q\in\mathbb Q\}.
\tag{2.1}
\]

Declare `S` and `T` disjoint **open** copies of the ordinary real line. For each rational `q`, the basic neighborhoods of the new point \(b_q\) are

\[
 N(q,\varepsilon)=\{b_q\}\cup
 \{s_x:q-\varepsilon<x<q\}\cup
 \{t_x:q<x<q+\varepsilon\},\quad\varepsilon>0.
\tag{2.2}
\]

Together with ordinary opens in `S,T`, these sets form a basis: intersections of neighborhoods of distinct bridge points contain only open pieces of `S,T`. Define

\[
 p(s_x)=p(t_x)=x,\qquad p(b_q)=q.
\tag{2.3}
\]

The restrictions of `p` to `S`, `T` and each `N(q,ε)` are homeomorphisms onto open intervals. Thus `p` is an **open local homeomorphism**. Each fiber is discrete, with two points at irrational parameters and three at rational ones. Rational intervals and `N(q,1/n)` form a countable basis. Fibers are closed finite discrete subspaces, which gives `T₁`. Sobriety is local on open covers and every section chart is a sober interval; hence `X` is sober. Each point has such an interval chart, so `X` is locally compact. The pairs \((b_q,s_q)\) and \((b_q,t_q)\) are inseparable, so `X` is not Hausdorff.

For each rational `q`, the union \(N_q=\bigcup_{\varepsilon>0}N(q,\varepsilon)\) is an open section isomorphic to **all** of \(\mathbb R\). The open section cover

\[
 \mathscr A=\{S,T\}\cup\{N_q:q\in\mathbb Q\}
\tag{2.4}
\]

has no finite subcover: each \(b_q\) lies in precisely its own `N_q` among these atlas members.

Let \(F=X\times_{\mathbb R}X\) be the fiber square and

\[
 J=S\times_{\mathbb R}T\cong\mathbb R,
 \qquad J^{\mathrm{op}}=T\times_{\mathbb R}S\cong\mathbb R.
\tag{2.5}
\]

The map \((s,t):\mathbb R\to J\) is an isomorphism, with inverse `p∘pr₁`. `J` is **open in F**, and is the restriction to `F` of the ambient X²-open rectangle \(S\boxtimes T\). In particular it does not meet the diagonal.

## 3. Every finite cover has a dense matching locus

For any X-open cover \(\mathscr C\), let

\[
 m_{\mathscr C}
 =\bigvee_{c\in\mathscr C}s^*c\wedge t^*c
 \in\mathcal O(\mathbb R).
\tag{3.1}
\]

**Density lemma.** For **every finite** X-open cover \(\mathscr F\), the open \(m_{\mathscr F}\) is dense in \(\mathbb R\).

*Proof.* Write \(\mathscr F=\{c_1,\ldots,c_n\}\). If some nonempty interval `I` missed \(m_{\mathscr F}\), then the opens

\[
 A_i=s^*c_i\cap I,\qquad B_i=t^*c_i\cap I
\]

would be disjoint for every `i`. Given any rational \(q\in I\), choose `i` with \(b_q\in c_i\). By (2.2), \(A_i\) contains a left interval approaching `q` and \(B_i\) a right interval approaching `q`. Since \(A_i\cap B_i=\varnothing\), the point `q` belongs to the boundary \(\partial_I A_i\). Thus

\[
 \mathbb Q\cap I\subseteq\bigcup_{i=1}^n\partial_I A_i.
\]

Each boundary of an open subset of `I` is closed nowhere dense. A finite union of these cannot contain the dense set \(\mathbb Q\cap I\), a contradiction. □

The quantifier **all finite covers** is essential; for the countable atlas `A`, \(m_{\mathscr A}=0\), since each atlas member is a section and never contains both \(s_x,t_x\) at the same parameter.

## 4. Full-atlas descent: D(X)=Δ

The regular locale \(\mathbb R\) satisfies \(D(\mathbb R)=\Delta_{\mathbb R}\). Consider any generalized pair \((f,g):Y\to D(X)\). Pullback of every cover of \(\mathbb R\) gives \(pf=pg\). Applying the full-cover compatibility condition to `A` yields an open cover of `Y` by the opens \(f^*V\wedge g^*V\), one for each \(V\in\mathscr A\). There the two maps land in the **same** open p-section, and their p-images agree; hence they agree locally. Locale maps that agree on an open cover agree globally. Therefore

\[
 \boxed{D(X)=\Delta_X,\qquad W(X)=I(X).}
\tag{4.1}
\]

As `S` and `T` are disjoint ambient X-opens, the rectangle \(S\boxtimes T\) is disjoint from the diagonal and hence from its closure \(I(X)\). In particular

\[
 W(X)\wedge J=0.
\tag{4.2}
\]

## 5. Finite covers retain Boolean support: J≤W₂

The restriction of the open sublocale \(O_{X^2}(w_{\mathscr F})\) to `J` is exactly the open \(O_J(m_{\mathscr F})\) under the isomorphism \(J\cong\mathbb R\). Since `J` is an open sublocale of `F`, meeting with `J` commutes with arbitrary sublocale meets. Therefore

\[
 D_2(X)\wedge J
 =\bigwedge_{\mathscr F\text{ finite cover}}O_J(m_{\mathscr F}).
\tag{5.1}
\]

By the density lemma, each `m_F` is dense open in `J`. Isbell's density theorem says the **Booleanization \(B(J)\)** is contained in every dense sublocale of `J`. Therefore

\[
 \boxed{0\ne B(J)\le D_2(X)\wedge J.}
\tag{5.2}
\]

The Booleanization is dense in `J`; the closed sublocale \(W_2(X)\wedge J\) contains it. Thus \(J\le W_2(X)\). By symmetry, \(J^{\mathrm{op}}\le W_2(X)\).

An equivalent explicit generalized pair is \((s\beta,t\beta):B(\mathbb R)\to X^2\), where \(\beta:B(\mathbb R)\hookrightarrow\mathbb R\). Since \(m_{\mathscr F}^{**}=1\), it factors through every finite diagonal cover square, and its image in `J` is precisely `B(J)`. For the infinite atlas, its matching value is zero, so it does not factor through `D(X)`. This recovers the longer audited proof without replacing the more economical (5.1)–(5.2).

## 6. Closed-hull upgrade: W₂(X)=U(X)=F

The diagonal of \(\mathbb R\) is closed, so \(F\) is closed in the localic square \(X^2\). The open p-section charts \(V\times_{\mathbb R}V'\) cover `F` and are isomorphic to ordinary opens of \(\mathbb R\). Thus `F` is **spatial**, without assuming that arbitrary localic products are spatial. (Here `X` is also locally compact and sober, which independently identifies its localic square with the ordinary product.)

Naturality over the regular base, together with the universal comparison \(W_2\le U\), gives

\[
 W_2(X)\le U(X)\le F.
\tag{6.1}
\]

The **ordinary points** of `F` fall into three disjoint *sets*: the points of \(I(X)\), those of `J`, and those of \(J^{\mathrm{op}}\). This is **not** a coproduct decomposition of locales or spaces. Indeed, at rational `q`, the extra pairs \((b_q,s_q)\) and \((b_q,t_q)\), and their reverses, are inseparable pairs and therefore belong to \(I(X)=\operatorname{cl}\Delta_X\); all remaining non-diagonal pairs lie in `J` or `J^op`. So `W₂` contains every ordinary point of `F`, by (4.1), §5, and the universal \(I\le W_2\). Since `W₂` is **closed in the spatial locale F**, its complement in `F` has no points and hence is zero. Thus \(W_2(X)=F\), and (6.1) gives \(U(X)=F\).

Combining this with (4.2) proves the strict inequality and theorem (T).

**Independent U check.** If `a,b` are ordinary neighborhoods of \(s_x,t_x\), choose \(\varepsilon>0\) so that the two corresponding section intervals over \(I=(x-\varepsilon,x+\varepsilon)\) lie in `a,b`. Every rational \(q\in I\) has \(b_q\in\operatorname{cl}(a)\cap\operatorname{cl}(b)\): all its basic bridge neighborhoods meet both section intervals. Thus no neighborhoods of \(s_x,t_x\) have disjoint closures; the pair belongs to `U`. The same holds in the reverse orientation. All other `F`-points lie in `I≤U`, yielding `U=F` by spatiality. **Corrected range detail:** for \(s(I)\), bridge points \(b_q\) occur in the closure at least for \(q\in(x-\varepsilon,x+\varepsilon]\); for \(t(I)\), at least for \(q\in[x-\varepsilon,x+\varepsilon)\). Their intersection contains every rational in `I`. The independent referee's displayed narrower half-intervals did not themselves establish the claim for irrational `x`; this is the harmless correction.

## 7. Mechanism, positive boundaries, and audit status

The central mechanism has four logically distinct components:

1. An **infinite open section atlas** forces `D=Δ` by descent along monic charts.
2. The rational bridge set is sufficiently dense that **every finite X-cover** has a dense common-member locus for the two distinguished sections.
3. The least dense sublocale `B(J)` survives the **arbitrary meet** of these dense opens, despite no ordinary off-diagonal points of `D₂` in the `T₁` space.
4. The support lies in a genuinely **open chart of the closed fiber square**, so taking the ambient closed hull fills the chart, rather than losing the defect in a nowhere-dense closed relation.

In particular **local compactness, second countability, sobriety, and `T₁` individually and jointly do not imply Q or Q′**. This does not conflict with the earlier locally-finite-cover theorem: the countable atlas `A` cannot have a locally finite open refinement. Otherwise the locally finite refinement theorem would give `D₂≤O(w_A)`, contradicting (5.2) and \(m_A=0\). Thus this space is an explicit locally compact, second-countable, nonregular example where the relevant cover-refinement property fails.

Potential positive hypotheses to investigate are therefore **cover-theoretic** (locally finite refinements, appropriate paracompactness), **strong separation** (regular/normal conditions), or local conditions that guarantee the canonical finite-cover matching opens are not merely dense but can be forced to contain a full-cover matching square. A generic Baire assumption alone cannot rescue Q/Q′: the present example already has Baire real-line charts.

**Audit provenance:** The working construction, internal audit, blind prompt and full packet were dated 14 November 2026. The independent blind referee's report (received without access to the internal audit) found no fatal flaw, independently rederived all sixteen central statements, and proposed the shorter `J`-sublocale proof. The correspondence with `Φ,Φ₂` in §1 was explicitly checked **after** the report and was not in that referee's scope. The two small presentation corrections are recorded in the separate reconciliation. Source priority remains uninvestigated.

