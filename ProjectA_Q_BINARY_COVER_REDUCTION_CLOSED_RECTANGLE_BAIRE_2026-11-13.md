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
