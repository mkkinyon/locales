# Project A — reusable definitions and notation for external audit packets

**Template, 13 November 2026.** This is a **copy-and-trim preamble**, not a stand-alone theorem or an assertion that every item is relevant to every audit. Its canonical home is the Point-free Topology repository. For an external referee, **paste the applicable sections into the actual packet**: a link to this file alone is not a substitute for defining notation in the packet. Remove irrelevant optional modules and all editorial instructions before submission.

The **core** below is intended for Project A's separation-relation / fitted-diagonal branch. Audits of coherent sheaves, classifying anima, crosscut nerves, or other branches need their **own additional definitions**; those symbols are not silently covered here.

---

## CORE — paste into nearly every separation-relation audit

### 1. Ambient conventions

We work in classical set theory with choice unless stated otherwise. All spaces called **locales** are objects of \(\mathbf{Loc}\), and \(\mathcal O(X)\) denotes the frame of opens of a locale \(X\). A locale map \(f:T\to X\) has an inverse-image frame homomorphism \(f^*:\mathcal O(X)\to\mathcal O(T)\), preserving finite meets and arbitrary joins.

All squares and products are **localic**, not automatically the locale of the ordinary point-set product. We write
\[
  X^2=X\times X,\qquad
  \mathcal O(X\times Y)=\mathcal O(X)\otimes\mathcal O(Y),
\]
and \(a\boxtimes b\) for the basic rectangle determined by frame elements \(a,b\). Thus for \(f,g:T\to X\),
\[
  (f,g)^*(a\boxtimes b)=f^*(a)\wedge g^*(b).
\]

The diagonal sublocale of \(X^2\) is \(\Delta_X\). Sublocale inequalities \(S\le T\) mean **inclusion of sublocales**; meets and joins of sublocales are not to be confused with the meet and join operations in the frame \(\mathcal O(X^2)\).

### 2. Open/closed sublocales, closure, and fitting

For an ambient locale \(P\) and \(w\in\mathcal O(P)\), denote by \(O_P(w)\) the open sublocale determined by \(w\), and by \(C_P(w)\) its complementary **closed sublocale**. These are complements in the sublocale lattice. Write \(O(w),C(w)\) when \(P\) is unambiguous. **The symbol \(C(w)\) does not mean the closure of the open \(O(w)\).**

For a sublocale \(S\subseteq P\), let \(\operatorname{cl}_P(S)\) be the least closed sublocale containing \(S\), and
\[
  \operatorname{fit}_P(S)
  =\bigwedge\{O_P(w):S\le O_P(w)\}
\]
its fitting (least fitted sublocale containing \(S\)). We omit ambient subscripts when clear. A sublocale \(S\) is **dense** in \(P\) if \(\operatorname{cl}_P(S)=P\). Its Booleanization \(B(P)\) is the double-negation sublocale, the least dense sublocale of \(P\).

### 3. Covers and diagonal cover squares

An **open cover** \(\mathscr C\) of \(X\) is a family in \(\mathcal O(X)\) with \(\bigvee\mathscr C=1\); it is not implicitly finite. Put
\[
  w_{\mathscr C}
    =\bigvee_{c\in\mathscr C}c\boxtimes c
    \in\mathcal O(X^2).
\]
The \(w_{\mathscr C}\) are cofinal among open neighbourhoods of \(\Delta_X\): if \(\Delta_X\le O(w)\), then \(w_{\mathscr C}\le w\) for some cover \(\mathscr C\). In particular,
\[
  D(X)=\operatorname{fit}(\Delta_X)
     =\bigwedge_{\mathscr C\text{ cover}}O(w_{\mathscr C}),\qquad
  D_2(X)=\bigwedge_{\mathscr F\text{ finite cover}}O(w_{\mathscr F}).
\]
Here \(D\) is the **full fitted diagonal**, whereas \(D_2\) uses only **finite** covers; the subscript 2 does **not** mean a second iteration.

Equivalently, \((f,g):T\to X^2\) factors through \(D(X)\) exactly when
\[
  \bigvee_{c\in\mathscr C} f^*(c)\wedge g^*(c)
    =1_{\mathcal O(T)}
  \quad\text{for every cover }\mathscr C.
\]
For \(D_2(X)\), test only finite covers. Factorization through \(\Delta_X\) means \(f=g\). Always \(\Delta_X\le D(X)\le D_2(X)\).

### 4. Closed hulls and separation terminology

Define the **closed hulls**
\[
  W(X)=\operatorname{cl}_{X^2}D(X),\qquad
  W_2(X)=\operatorname{cl}_{X^2}D_2(X).
\]
Thus \(W\le W_2\). Equality \(D=D_2\) is stronger than \(W=W_2\); a nonzero closed piece of \(D_2\) excluded by \(D\) does **not**, by itself, imply unequal closed hulls.

A locale is **F-separated** if its diagonal is fitted, equivalently \(D(X)=\Delta_X\). It is **strongly Hausdorff** (Isbell) if its **localic diagonal is a closed sublocale** of \(X^2\). Ordinary Hausdorffness of a point-set space must not be silently substituted for strong Hausdorffness of its locale.

---

## OPTIONAL MODULE A — inseparability, Urysohn relation, hierarchy

Paste this module when the relations \(I,U,V,M,J\), or the wider separation hierarchy enter the claims. Let \(L=\mathcal O(X)\), \(P=\mathcal O(X^2)\), and \(a^*=a\to0\) denote the pseudocomplement in \(L\). Define
\[
\begin{aligned}
  d_I&=\bigvee_{a\wedge b=0}a\boxtimes b,
       & I(X)&=C_P(d_I)=\operatorname{cl}(\Delta_X),\\
  d_U&=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
       & U(X)&=C_P(d_U),\\
  V(X)&=\operatorname{fit}(I(X)),
       & M(X)&=I(X)\wedge D(X),\\
  && J(X)&=I(X)\vee D(X).
\end{aligned}
\]
Here \(U\) is the **Urysohn-style closed relation**, and \(I\) is the closed inseparability relation. Established universal comparisons include
\[
  \Delta\le I\le V,\qquad D\le U.
\]
In general \(I,D\) and \(V,U\) need not be comparable. Do **not** infer a stronger inclusion from a suggestive Hasse diagram.

**If \(F,H\), higher separation-tree ranks, composition, or classifying-anima constructions are used:** insert their **exact task-specific definitions here** from the theorem under review. Their notation alone is not a definition, and the present template intentionally does not assert unstated formulas or associativity.

---

## OPTIONAL MODULE B — cover operators and Questions Q, Q′

**Paste whenever Q or Q′ is mentioned, including in a “what the result does not imply” section.** On \(P=\mathcal O(X^2)\), with Heyting implication \(\to\), put
\[
  \Phi(q)
   =\bigvee_{\mathscr C\text{ cover}}
      (w_{\mathscr C}\to q),\qquad
  \Phi_2(q)
   =\bigvee_{\mathscr F\text{ finite cover}}
      (w_{\mathscr F}\to q).
\]
The rank-zero element is
\[
  z=\Phi(0)=\Phi_2(0),\qquad U(X)=C_{X^2}(z).
\]
The finite-cover closed hull is \(W_2(X)=C_{X^2}(d)\), where \(d=\Phi_2^\infty(0)\) denotes the stabilized transfinite iteration from \(0\).

The two **universal open questions** (status as of 13 November 2026) are:

- **Q:** For every locale \(X\), does \(\Phi_2(z)=z\) imply \(\Phi(z)=z\)? Equivalently, does \(W_2(X)=U(X)\) imply \(W(X)=U(X)\)?
- **Q′:** For every locale \(X\), does \(W_2(X)=W(X)\)? Equivalently, is \(B(D_2(X))\le D(X)\) for every \(X\)?

Q′ would imply Q. Neither is known in general; an example with \(D_2(X)\ne D(X)\) alone disproves **neither** question.

For a full cover \(\mathscr C\), define the **weak defect**
\[
  T_{\mathscr C}
     =D_2(X)\wedge C_{X^2}(w_{\mathscr C}).
\]
This sublocale may be nonzero even if Q′ holds on \(X\). The relevant issue is whether \(T_{\mathscr C}\) has **nonzero relative interior in \(D_2(X)\)**. Equivalently, the Q′ criterion asks that every such relatively closed defect be **nowhere dense in \(D_2(X)\)**. Relative openness/density must be checked in \(D_2(X)\), not in \(X^2\) by ordinary points.

---

## OPTIONAL MODULE C — products and Boolean bases

When comparing relations on products, use the canonical rebracketing
\[
  (Z\times X)^2\cong Z^2\times X^2.
\]
Thus \(\Delta_Z\times D(X)\) is a sublocale of \((Z\times X)^2\) whose two \(Z\)-coordinates agree and whose \(X\)-coordinates lie in \(D(X)\).

A **Boolean locale** is a locale whose frame is a complete Boolean algebra. It need not be spatial or a discrete topological space. For a Boolean locale \(Z\), \(D(Z)=D_2(Z)=\Delta_Z\). The general projection comparison is
\[
  D(Z\times X)\le D(Z)\times D(X),
  \qquad
  D_2(Z\times X)\le D_2(Z)\times D_2(X).
\]
If \(Z\) is Boolean these upper bounds become \(\Delta_Z\times D(X)\) and \(\Delta_Z\times D_2(X)\).

A pair of maps into \(Z\times X\) with a common \(Z\)-component factors through \(\Delta_Z\times D(X)\) iff its two \(X\)-components match **all** \(X\)-covers. It need not factor through \(D(Z\times X)\): product covers are a separate requirement. Likewise a pair in \(\Delta_Z\times D(X)\) that fails a **binary product cover** lies **outside \(D_2(Z\times X)\)** and is not itself an internal Q′ weak defect of the product.

For closed-graph arguments, specify the source hypothesis that makes graphs of \(f:T\to X\) **closed sublocales** of \(T\times X\) (for example, a closed diagonal of \(X\)); distinguish actual sublocale intersections/equalizers from intersections of sets of ordinary points.

---

## OPTIONAL MODULE D — presentation and audit-provenance checklist

**Do not paste this editorial checklist verbatim into the blind mathematical packet.** Use it while assembling the prompt and packet.

- [ ] Define **every named question or relation used anywhere**, including background assertions, remarks, negative-scope statements, and the prompt itself.
- [ ] Specify the **ambient locale/frame** of each operation \(O(w),C(w),\operatorname{cl},\operatorname{fit},\wedge,\vee,\to\).
- [ ] Distinguish finite from arbitrary covers, \(D\) from \(D_2\), and nonclosed product defects from internal Q′ defects.
- [ ] Distinguish classical points/spatial products from sublocales/localic products.
- [ ] Import external results with author, source, exact statement/hypotheses, and theorem or section identifier; disclose whether full source verification was possible.
- [ ] Label each theorem **established / proposed / internally audited / externally checked**, without implying the number of readers is an independent proof count.
- [ ] State precisely what the referee is being asked to verify; include counterexample and source-check requests when useful.
- [ ] Keep the external referee's first reading **blind** to the internal audit, but disclose pertinent known imports and prior external mathematical results.
- [ ] Trim irrelevant optional modules. Ensure the final packet contains **no dangling symbol**, undefined Q/Q′, or reference that requires unprovided repository context.

**Maintenance rule:** Revise this template when notation changes, but preserve original submitted packets and blind reports as historical records. Each new packet must be checked against the current definitions and current status of the problem, not just copied automatically.
