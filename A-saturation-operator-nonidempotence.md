# Project A — the inseparability saturation operator need not be idempotent

**20 October 2026 — independently checked correction following two external audits.** The elementary frame formula below is sound, but the inference “internal equivalence relation ⇒ idempotent saturation operator” appearing in an earlier version of [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md) was **false**. The stronger example here was supplied in the external Claude Opus 5.5 audit and checked in our subsequent reconciliation. No novelty claim.

## 1. Definition and what holds unconditionally

Let \(E\hookrightarrow X\times X\) be a **closed** reflexive symmetric localic relation, \(E=C(d_E)\), with projections \(p_1,p_2\) and \(L=\mathcal O(X)\). Define

\[
r_E(u)=(p_2)_*p_1^*(u)
=\bigvee\{v\in L:1\boxtimes v\le (u\boxtimes1)\vee d_E\}.
\]

Adjunction gives the formula for every locale. The map \(r_E\) is monotone, preserves **finite meets** (as a composite of a right adjoint and a frame homomorphism), and is **deflationary** because reflexivity makes \(\delta^*p_1^*=\delta^*p_2^*=\mathrm{id}\). Symmetry shows

\[
r_E(u)=u \quad\Longleftrightarrow\quad p_1^*(u)=p_2^*(u).
\]

Thus its fixed points are the \(E\)-invariant opens, even when \(r_E(u)\) itself is not invariant. In general \(r_E^2(u)\ne r_E(u)\).

If \(E\) is an internal equivalence relation **with proper projections**, Vermeulen's Lemma 5.2 supplies idempotence and his Proposition 5.5 identifies \(r_E=q^*q_*\) with the largest invariant open below \(u\). Properness also implies Scott continuity of \(r_E\). For the special relation \(I=\overline{\Delta_X}\), neither idempotence nor Scott continuity follows from \(I\) being transitive or from \(I=U=F\).

## 2. Countable algebraic sober counterexample with \(I=U=F\)

Let

\[
X=\{a,b\}\sqcup\{c_n,d_n:n\ge1\}.
\]

Define a topology by saying that \(O\subseteq X\) is open exactly when:

1. \(a\in O\implies b\in O\);
2. \(c_n\in O\implies d_n\in O\) for every \(n\);
3. \(a\in O\implies d_n\in O\) for all but finitely many \(n\).

These conditions are stable under unions and finite intersections, so define a topology. Useful compact open neighborhoods are \(\{b\}\), \(\{d_n\}\), \(\{c_n,d_n\}\), and

\[
K_N=\{a,b\}\cup\{d_n:n\ge N\}.
\]

Every open neighborhood of \(a\) contains some \(K_N\); all other points have compact open elementary neighborhoods. Each \(K_N\) is compact: any cover has a member containing \(a\), hence all but finitely many \(d_n\), and finitely many remaining points can be covered separately. Thus \(X\) has a compact-open basis; \(\mathcal O(X)\) is **algebraic**, and \(X\) is strongly locally compact.

Sobriety can be checked by irreducible closed sets: for any \(n\), the finite set \(\{c_n,d_n\}\) is a clopen component. An irreducible closed subset lies either in one such component or in the closed complement \(A_0=\{a,b\}\). Indeed, if it met a clopen component and its complement it would be reducible. If it met none of the clopen components it lies in \(A_0\). Each resulting two-point Sierpiński space is sober. Hence \(X\) is sober. (The union of the clopen components need not be closed; this does not affect the irreducibility argument.)

The ordinary inseparability classes are

\[
\{a,b\},\qquad\{c_n,d_n\}\ (n\ge1).
\]

Each pair is inseparable by specialization; **distinct classes are separated by opens with disjoint closures**. For instance, \(K_N\) and \(\{c_n,d_n\}\) have disjoint closures for \(N>n\), while \(\{b\}\) has closure \(\{a,b\}\) and is similarly separated from other classes. Thus \(I=U\) pointwise.

The quotient by these classes is the usual compact convergent sequence \(\omega+1\), with \(\{a,b\}\) as its limit and the other classes isolated. Therefore continuous real functions distinguish the classes, giving \(I=U=F\) pointwise, and as **closed localic relations** because \(X\) is strongly locally compact sober.

Now put

\[
u=\{a,b\}\cup\{d_n:n\ge1\}.
\]

The closed complement is \(C=\{c_n:n\ge1\}\). Its \(I\)-saturation is \(\bigcup_n\{c_n,d_n\}\), whose closure is \(\bigcup_n\{c_n,d_n\}\cup\{a\}\), **not containing \(b\)**. Consequently

\[
r_I(u)=\{b\},\qquad r_I^2(u)=\varnothing.
\]

In particular **\(I=\overline\Delta\), \(I=U=F\), finite \(I\)-classes, and a compact Hausdorff quotient do not force idempotence**. The quotient map is not closed.

## 3. Exact spatial criterion

For a topological space \(X\) and an **equivalence relation** \(E\), the localic operator on \(\mathcal O(X)\) (for the associated spatial relation, when the comparison is valid) has the point-set formula

\[
r_E(u)=\operatorname{int}(X\setminus E[X\setminus u])
      =X\setminus\overline{E[X\setminus u]}.
\]

The **interior is indispensable** unless closedness of saturation is known. Let \(C=X\setminus u\). A direct calculation gives

\[
r_E^2=r_E
\iff
\overline{E[C]}\text{ is \(E\)-saturated for every closed }C\subseteq X.
\]

Proof: let \(S=\overline{E[C]}\). Then \(r_E(u)=X\setminus S\), \(r_E^2(u)=X\setminus\overline{E[S]}\). Reflexivity gives \(S\subseteq E[S]\), so equality holds iff \(E[S]\subseteq S\), i.e. \(S\) saturated.

A **closed quotient** \(q:X\to X/E\) is a sufficient condition because all \(E[C]\) are closed and \(r_E=q^*q_*\). The converse fails in general. Proper relation projections are a stronger sufficient localic condition.

## 4. Independent Scott-continuity failure despite finite fibers

In the preceding space let

\[
u_N=X\setminus\{c_n:n\ge N\}.
\]

Each \(u_N\) is open and \(u_N\uparrow X\), but no \(r_I(u_N)\) contains \(a\): the saturation of its complement contains all \(d_n\), \(n\ge N\), whose closure contains \(a\). Thus

\[
r_I\left(\bigvee_Nu_N\right)=1
\ne\bigvee_Nr_I(u_N).
\]

This complements the deleted-plank *cofinite-cloud* example: there Scott continuity fails for a **closed quotient with noncompact fibers**. Here all fibers are finite, but the quotient is **not closed**.

For a closed ordinary quotient \(q\), **Scott continuity of \(q_*\)** is equivalent to compactness of every fiber. That is a special-case theorem, **not** a general converse from Scott continuity of \(r_I\) to localic properness of the projections.

## 5. What remains to test

The two external reviews concur on the major formal theorem: a closed internal equivalence relation with **proper projections** has a proper effective quotient (Vermeulen, 1994, Proposition 5.5 and Corollary 5.17), which for a **continuous** underlying frame is completely regular and gives \(I=U=F\) when \(E=I\).

Still unresolved here: whether Scott continuity of \(r_I\) alone forces properness of its projections for arbitrary locales; whether the combination **subfit + arithmetic** excludes the functional-separation obstruction. Stable continuity/arithmetic alone does *not*: see [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md).

## Sources and provenance

- The external Claude Opus 5.5 adversarial audit of 20 October 2026, Findings 1–2 (user-supplied report; text of example checked here).
- The independent ChatGPT High audit of 20 October 2026, which confirmed the general idempotence issue and the properness theorem.
- J. J. C. Vermeulen, *Proper Maps of Locales*, *Journal of Pure and Applied Algebra* **92** (1994), 79–107, Lemma 5.2, Proposition 5.5, Corollary 5.17.
- [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md), for the unchanged exact adjunction formula.
