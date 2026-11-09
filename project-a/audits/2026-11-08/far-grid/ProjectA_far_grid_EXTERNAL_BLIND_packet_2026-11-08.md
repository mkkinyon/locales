# Project A — Candidate counterexample to the far-grid converse

**8 November 2026 · Self-contained technical packet for independent blind audit**

## 0. Definitions and question

Let L be a frame, and let Q=L⊕L denote its **frame coproduct** (dual to the localic square of X=Loc(L)). Write `a ⊠ b` for the pure rectangle obtained by meeting the two coproduct injections. The relevant standard identity is

\[
(\bigvee_i a_i)\boxtimes b=\bigvee_i(a_i\boxtimes b),\qquad
 a\boxtimes(\bigvee_j b_j)=\bigvee_j(a\boxtimes b_j).
\]

The pseudocomplement is `a*=a→0`. Define the opens of the square complementary to the two closed relations by

\[
d_{\mathcal I}=\bigvee_{a\wedge b=0}a\boxtimes b,\qquad
d_{\mathcal U}=\bigvee_{a^*\vee b^*=1}a\boxtimes b.
\]

Then `I=cl Δ=C(d_I)` and `U=C(d_U)`. Every far pair `a*∨b*=1` is disjoint, so `d_U≤d_I`. Hence `I=U` if and only if `d_I=d_U`.

The **far-grid property** says: for every disjoint `a,b∈L` there exist (arbitrarily indexed) join decompositions

\[
a=\bigvee_{\alpha}a_{\alpha},\qquad b=\bigvee_{\beta}b_{\beta},
\quad a_{\alpha}^*\vee b_{\beta}^*=1\text{ for all }\alpha,\beta.
\]

This is known to imply `I=U` by rectangular distributivity. The question for this audit is the converse, for *arbitrary frames*. The candidate below purports to refute it.

## 1. Candidate statement

There is a **countable, second-countable, sober** topological space X such that `I(O(X))=U(O(X))` as actual closed **localic** subrelations, but the far-grid property fails. The space is also claimed to be noncompact and not locally compact at one point. The second-countability claim follows from the displayed countable basis; it strengthens the original first-countability observation.

## 2. Construction and topological preliminaries

Let `N={1,2,…}` and take pairwise distinct points

\[
X=\{q\}\sqcup\{p_i,r_i:i\in\mathbb N\}
\sqcup\{s_{i,m}:i,m\in\mathbb N\}.
\]

Put `S_i={s_{i,m}:m∈N}`. Endow X with the topology having the following **proposed basis**:

1. `P_i={p_i}` and `T_{i,m}={s_{i,m}}`;
2. `R_{i,m}={r_i,p_i}∪{s_{i,t}:t≥m}`;
3. `N_n={q}∪⋃_{i≥n}S_i`.

The proposed neighborhood bases are P_i at p_i, T_{i,m} at s_{i,m}, `{R_{i,m}}_m` at r_i, and `{N_n}_n` at q. In particular `R_{i,m}∩R_{i,m'}=R_{i,max(m,m')}`, `N_n∩N_{n'}=N_{max(n,n')}`, and

\[
R_{i,m}\cap N_n=
\begin{cases}
\varnothing,&i<n,\\
\bigcup_{t\ge m}T_{i,t},&i\ge n.
\end{cases}
\]

The claimed closures of the basis opens are

\[
\begin{aligned}
\overline {P_i}&=P_i\cup\{r_i\},\\
\overline {T_{i,m}}&=T_{i,m},\\
\overline {R_{i,m}}&=R_{i,m},\\
\overline {N_n}&=N_n\cup\{r_i:i\ge n\}.
\end{aligned}
\tag{1}
\]

For L=O(X) the proposed elementary observation is

\[
u^*=X\setminus\overline u,
\qquad
u^*\vee v^*=1\iff\overline u\cap\overline v=\varnothing.
\tag{2}
\]

## 3. Candidate proof of localic I=U

Let Q=L⊕L, with d_I,d_U as above. We claim that for **every disjoint pair of basic opens** B,C, `B⊠C≤d_U`.

The following table attempts to exhaust all ten unordered basic-open type pairs; exchanges of factors are suppressed.

| Types | When disjoint | Whether far when disjoint |
|---|---|---|
| P_i,P_j | i≠j | yes |
| P_i,T_{j,t} | always | yes |
| P_i,R_{j,m} | i≠j | yes |
| P_i,N_n | always | yes for i<n; **exceptional** for i≥n |
| T_{i,t},T_{j,u} | (i,t)≠(j,u) | yes |
| T_{i,t},R_{j,m} | i≠j or (i=j and t<m) | yes |
| T_{i,t},N_n | i<n | yes |
| R_{i,m},R_{j,t} | i≠j | yes |
| R_{i,m},N_n | i<n | yes |
| N_n,N_{n'} | never | — |

Using (1), the sole claimed exception to farness among disjoint basic opens is `(P_i,N_n)` with i≥n (and its transpose): their closures meet at r_i. For these pairs, however,

\[
N_n=N_{i+1}\vee\bigvee_{j=n}^{i}\bigvee_{t\ge1}T_{j,t}
\qquad(i\ge n).
\tag{3}
\]

Every `P_i`–`N_{i+1}` pair and every `P_i`–`T_{j,t}` pair is far. By (3) and preservation of arbitrary joins in the second tensor coordinate,

\[
P_i\boxtimes N_n
=(P_i\boxtimes N_{i+1})
\vee\bigvee_{j=n}^{i}\bigvee_{t\ge1}(P_i\boxtimes T_{j,t})
\le d_{\mathcal U}.
\tag{4}
\]

Swapping coordinates handles the transpose.

For general opens `u,v∈L` with `u∧v=0`, write each as the union of all basic opens contained in it. Every pair B⊆u,C⊆v is disjoint. The previous argument and rectangular distributivity give

\[
u\boxtimes v
=\bigvee_{B\subseteq u}\bigvee_{C\subseteq v}(B\boxtimes C)
\le d_{\mathcal U}.
\]

Joining over disjoint u,v yields `d_I≤d_U`, hence **`d_I=d_U` and `I=U` as localic subrelations**. This is an argument in the frame coproduct, not an inference from equality on ordinary points of the topological product.

## 4. Candidate proof of failure of all far grids

Set

\[
a=\bigcup_{i\ge1}P_i,
\qquad b=N_1=\{q\}\cup\bigcup_{i\ge1}S_i.
\]

These are disjoint opens. Suppose

\[
a=\bigvee_{\alpha}a_{\alpha},\qquad b=\bigvee_{\beta}b_{\beta},
\quad a_{\alpha}^*\vee b_{\beta}^*=1
\quad\text{for all }\alpha,\beta.
\]

Since q∈b, there is a β₀ with q∈b_{β₀}, and thus some n with N_n⊆b_{β₀}. Choose any i≥n. Since p_i∈a, some α_i has p_i∈a_{α_i}. By (1), r_i∈cl(a_{α_i}) and r_i∈cl(b_{β₀}), contradicting (2). Thus no far grid exists for a,b.

## 5. Auxiliary topological claims

The displayed basis is countable, and is claimed to separate points (T0). To show sobriety, consider the blocks

\[
B_i=\{r_i,p_i\}\cup S_i=R_{i,1}.
\]

Each B_i is claimed to be clopen in X. Within B_i, every singleton `T_{i,m}` is clopen. If an irreducible closed subset F of B_i contains any s_{i,m}, it must be that singleton; otherwise F⊆{r_i,p_i}, whose only nonempty closed subsets are `{r_i}` and `{r_i,p_i}`, with generic points r_i and p_i. If an irreducible closed subset of X meets any B_i, clopenness forces it to be contained in B_i; otherwise it is `{q}`. Hence X is sober.

For noncompactness, `{N_1}∪{B_i:i≥1}` is an open cover with no finite subcover. The stronger non-local-compactness claim at q is based on: if compact K⊇N_n contains infinitely many r_i, the preceding cover restricted to K has no finite subcover; if it contains only finitely many r_i, pick i≥n with r_i∉K and cover K by N_{i+1}, all B_j for j≠i, P_i and all T_{i,m}. Since S_i⊆K, this cover also has no finite subcover.

## 6. Exact scope

The proposed negative result concerns the implication

\[
\mathcal I=\mathcal U\quad\Longrightarrow\quad\text{far-grid property}
\]

for arbitrary frames (indeed a specified O(X)). It does not purport to refute the implication on coherent, compact, continuous, or algebraic frames. No novelty or priority claim is asserted. The referee is asked to decide whether **every** technical claim in §§2–5 is sound and, independently, whether the central counterexample is correct even if ancillary properties require correction.