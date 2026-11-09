# Project A — Subfit far-grid converse: a countable \(T_1\) counterexample

**8 November 2026 — Candidate theorem submitted for independent mathematical review.**

This note addresses the sharp question left by the externally audited failure of the unrestricted far-grid converse:

> If \(L\) is **subfit** and \(\mathcal I(L)=\mathcal U(L)\), must every disjoint pair \(a,b\in L\) admit join decompositions \(a=\bigvee_\alpha a_\alpha\), \(b=\bigvee_\beta b_\beta\), with \(a_\alpha^*\vee b_\beta^*=1\) for every \(\alpha,\beta\)?

**Claimed negative answer.** The example below is the frame of opens of a **countable, second-countable, \(T_1\)** space. The presenting \(T_1\) space is *not* sober, but its frame is subfit; passing to its soberification changes neither its frame nor any asserted localic statement. In fact, the soberification remains countable and second-countable.

No novelty or priority claim is made. The argument below is offered as a candidate proof for the referee to verify or refute.

## 1. Definitions

Write \(L=\mathcal O(X)\) and \(L\oplus L=\mathcal O(X\times_{\mathrm{Loc}}X)\). A *far pair* is a pair \(u,v\in L\) for which \(u^*\vee v^*=1\). In a topological representation, \(u^*=X\setminus\overline u\), so
\[
u\text{ far from }v \quad\Longleftrightarrow\quad
\overline u\cap\overline v=\varnothing.
\]

Let
\[
 d_{\mathcal I}=\bigvee_{u\wedge v=0}u\boxtimes v,\qquad
 d_{\mathcal U}=\bigvee_{u^*\vee v^*=1}u\boxtimes v
\]
in \(L\oplus L\), and \(\mathcal I=C(d_{\mathcal I})\), \(\mathcal U=C(d_{\mathcal U})\). We always have \(d_{\mathcal U}\le d_{\mathcal I}\). Rectangles preserve arbitrary coordinatewise joins:
\[
(\bigvee_\alpha u_\alpha)\boxtimes v
=\bigvee_\alpha(u_\alpha\boxtimes v),\qquad
u\boxtimes(\bigvee_\beta v_\beta)
=\bigvee_\beta(u\boxtimes v_\beta).
\]

A frame is **subfit** when \(u\not\le v\) implies the existence of \(w\) with \(u\vee w=1\), \(v\vee w\ne1\).

## 2. The space

For each \(i\ge1\), let
\[
P_i=\{p_{i,k}:k\ge1\},\qquad S_i=\{s_{i,t}:t\ge1\}
\]
be infinite countable sets, all disjoint. Set
\[
X=\{q\}\sqcup \{r_i:i\ge1\}
       \sqcup\bigsqcup_{i\ge1}(P_i\sqcup S_i).
\]
For finite \(F\subseteq P_i\) and \(m,n\ge1\), introduce the following sets:
\[
\begin{aligned}
A_{i,F}&=P_i\setminus F,\\
T_{i,t}&=\{s_{i,t}\},\\
R_{i,F,m}&=\{r_i\}\cup(P_i\setminus F)\cup
                       \{s_{i,t}:t\ge m\},\\
N_n&=\{q\}\cup\bigcup_{i\ge n}S_i.
\end{aligned}
\tag{2.1}
\]
These form a basis \(\mathscr B\). They cover \(X\). An intersection of two \(A\)-sets in one block is another \(A\)-set; an intersection of two \(R\)-sets in one block is another \(R\)-set; \(A_{i,F}\cap R_{i,G,m}=A_{i,F\cup G}\); and
\[
R_{i,F,m}\cap N_n=
\begin{cases}\varnothing & i<n,\\
\bigcup_{t\ge m}T_{i,t}&i\ge n.
\end{cases}
\]
Moreover, \(N_n\cap N_k=N_{\max(n,k)}\), and every other intersection is empty or a union of indicated singleton basics. Thus all intersections of basis members are unions of basis members, as required.

The basis is countable because each \(P_i\) has only countably many finite subsets. Thus \(X\) is countable and second-countable.

**\(T_1\).** Complements of all points are open. At a point \(r_i\), any prescribed cloud point \(p_{i,k}\) can be omitted using \(R_{i,\{p_{i,k}\},m}\); an \(s_{i,t}\) can be omitted by taking \(m>t\). At \(q\), any \(s_{i,t}\) is omitted using \(N_{i+1}\). All remaining cases follow from the disjoint blocks and the cofinite bases \(A_{i,F}\). Hence \(X\) is \(T_1\).

**Subfitness.** For opens \(u\not\subseteq v\), choose \(x\in u\setminus v\). The \(T_1\) property ensures \(w=X\setminus\{x\}\) is open and \(u\vee w=X\) while \(v\vee w=X\setminus\{x\}\ne X\). So \(L=\mathcal O(X)\) is subfit.

## 3. Closure calculations

The neighborhood bases give, for any \(E\subseteq X\),
\[
\begin{aligned}
p_{i,k}\in\overline E&\iff
     p_{i,k}\in E \text{ or } E\cap P_i\text{ is infinite},\\
s_{i,t}\in\overline E&\iff s_{i,t}\in E,\\
r_i\in\overline E&\iff r_i\in E\text{ or }E\cap P_i\text{ is infinite}
                         \text{ or }E\cap S_i\text{ is infinite},\\
q\in\overline E&\iff q\in E\text{ or }E\text{ meets }S_i
                                  \text{ for infinitely many }i.
\end{aligned}
\tag{3.1}
\]
The cofinite topology on \(P_i\) makes every infinite subset dense in \(P_i\); the tails in the \(R\)-neighborhoods detect infinite subsets of \(S_i\).

For the basic opens this yields:
\[
\begin{aligned}
\overline{A_{i,F}}&=P_i\cup\{r_i\},\\
\overline{T_{i,t}}&=T_{i,t},\\
\overline{R_{i,F,m}}&=P_i\cup\{r_i\}\cup\{s_{i,t}:t\ge m\},\\
\overline{N_n}&=N_n\cup\{r_i:i\ge n\}.
\end{aligned}
\tag{3.2}
\]

## 4. The complete basis-pair check

For each unordered pair of types, the following table records the condition for *disjointness*. Every disjoint pair in the table is far, **except the indicated \(A,N\) case**.

| Type pair | When disjoint | Are the disjoint pairs far? |
| --- | --- | --- |
| \(A_{i,F},A_{j,G}\) | \(i\ne j\) | Yes |
| \(A_{i,F},T_{j,t}\) | Always | Yes |
| \(A_{i,F},R_{j,G,m}\) | \(i\ne j\) | Yes |
| \(A_{i,F},N_n\) | Always | **No if \(i\ge n\)**; yes if \(i<n\) |
| \(T_{i,t},T_{j,u}\) | \((i,t)\ne(j,u)\) | Yes |
| \(T_{i,t},R_{j,F,m}\) | \(i\ne j\), or \(i=j,t<m\) | Yes |
| \(T_{i,t},N_n\) | \(i<n\) | Yes |
| \(R_{i,F,m},R_{j,G,k}\) | \(i\ne j\) | Yes |
| \(R_{i,F,m},N_n\) | \(i<n\) | Yes |
| \(N_n,N_m\) | Never | Vacuous |

Every entry follows by intersecting the closure formulas (3.2). In particular, \(\overline{A_{i,F}}\cap\overline{N_n}=\{r_i\}\) exactly when \(i\ge n\), despite \(A_{i,F}\cap N_n=\varnothing\).

For the exceptional pairs \(i\ge n\),
\[
N_n=N_{i+1}\;\vee\;\bigvee_{j=n}^{i}\bigvee_{t\ge1}T_{j,t}.
\tag{4.1}
\]
Every summand on the right is far from \(A_{i,F}\): the closure of \(N_{i+1}\) omits \(r_i\) and \(P_i\), while each \(T_{j,t}\) is closed and disjoint from \(\overline{A_{i,F}}\). Therefore
\[
A_{i,F}\boxtimes N_n
=A_{i,F}\boxtimes N_{i+1}\vee
  \bigvee_{j=n}^{i}\bigvee_t(A_{i,F}\boxtimes T_{j,t})
\le d_{\mathcal U}.
\tag{4.2}
\]
The transpose follows by symmetry. Consequently **every disjoint basic-open rectangle lies below \(d_{\mathcal U}\)**.

If \(u,v\in L\) are arbitrary disjoint opens, expand each as a join of basis members below it:
\[
u=\bigvee_{A\in\mathscr B,\ A\subseteq u}A,\qquad
v=\bigvee_{B\in\mathscr B,\ B\subseteq v}B.
\]
Each resulting pair \(A,B\) is disjoint, so (4.2) and the table give \(A\boxtimes B\le d_{\mathcal U}\). The join identities for rectangles yield \(u\boxtimes v\le d_{\mathcal U}\). Joining over all disjoint \(u,v\) gives \(d_{\mathcal I}\le d_{\mathcal U}\), hence
\[
\boxed{d_{\mathcal I}=d_{\mathcal U},\quad
        \mathcal I(L)=\mathcal U(L).}
\tag{4.3}
\]
This is a calculation in the **frame coproduct**, not an inference from equality on ordinary points.

## 5. Far-grid obstruction

Set
\[
a=\bigcup_{i\ge1}P_i,\qquad b=N_1.
\]
They are disjoint opens.

Assume \(a=\bigvee_\alpha a_\alpha\), \(b=\bigvee_\beta b_\beta\) and every \(a_\alpha,b_\beta\) is far.

Some \(b_{\beta_0}\) contains \(q\), so some \(N_n\subseteq b_{\beta_0}\). Fix \(i\ge n\). Since \(P_i\subseteq a\), there is \(\alpha_0\) such that \(a_{\alpha_0}\cap P_i\ne\varnothing\). Because \(a_{\alpha_0}\) is open, it contains a cofinite subset of \(P_i\); by (3.1),
\[
r_i\in\overline{a_{\alpha_0}}.
\]
Also \(r_i\in\overline{N_n}\subseteq\overline{b_{\beta_0}}\). This contradicts farness. No restrictions on the cardinalities, overlaps or order of the alleged refinement families were used.

Therefore \(L\) fails far grids despite being subfit and satisfying (4.3).

## 6. Boundary properties and soberification

The space \(X\) is **not sober**. For each \(i\),
\[
F_i=P_i\cup\{r_i\}
\]
is a non-singleton closed irreducible subset: every nonempty relatively open subset of \(F_i\) contains a cofinite subset of \(P_i\), and therefore any two such subsets intersect. Since \(X\) is \(T_1\), no point of \(X\) has closure \(F_i\). This is a *limitation of the original topological presentation*, not of the frame-theoretic counterexample.

The sobrification \(X^{\mathrm{sob}}\) has an isomorphic open frame, so remains a counterexample **as a sober locale** with subfit frame. In fact the sobrification remains countable: let \(B_i=P_i\cup S_i\cup\{r_i\}=R_{i,\varnothing,1}\). Each \(B_i\) is clopen, so any irreducible closed set meeting \(B_i\) is contained in that block. The singleton sets \(T_{i,t}\) are clopen. After excluding the \(s\)-points, a nonempty irreducible closed subset in \(F_i\) is either a singleton or all of \(F_i\), since every infinite subset of \(P_i\) has closure \(F_i\). Outside all blocks only \(\{q\}\) remains. Therefore the only additional irreducible closed sets are the countably many \(F_i\), one per \(i\). A countable base for \(X\) induces a countable base for its sobrification.

The space is noncompact, as witnessed by the cover \(\{N_1\}\cup\{B_i:i\ge1\}\), which has no finite subcover. Moreover \(L\) is **not continuous**. For fixed \(n\), the directed family
\[
D_F=N_{n+1}\cup F,\qquad
F\subseteq\bigcup_{j=1}^n S_j \text{ finite},
\]
has join \(N_1\) but no member contains \(N_n\) (the entire infinite set \(S_n\) is missing). Therefore \(N_n\not\ll N_1\) for any \(n\). Since every open containing \(q\) contains some \(N_n\), no way-below approximation to \(N_1\) can cover \(q\). Consequently \(L\) is not continuous, and therefore not algebraic or coherent.

The example does **not** settle a version requiring a **sober \(T_1\)** representation, nor any stronger Hausdorff or regularity assumption. It does settle the **subfit-frame** version exactly.

## 7. Items submitted for verification

The candidate proof rests on (i) the basis and the closure computations; (ii) all ten cases in the basis-pair table; (iii) the rectangular join identities in the actual frame coproduct; (iv) the universally quantified far-grid obstruction; and (v) the asserted topological boundary properties and soberification analysis. Please check each independently. A counterexample to any claim should identify the exact failing step. No theorem-ledger status is requested in this packet.

Historical context: the previous counterexample used isolated points \(p_i\), with \(r_i\in\overline{\{p_i\}}\), so the frame was not subfit. This modification replaces those points with cofinite clouds, ensuring \(X\) is \(T_1\), but retains the essential closure obstruction for *every nonempty open piece* of each cloud.