# CO-01 control: closed reflexive symmetric nonassociative cubes on a locally compact zero-dimensional Hausdorff locale

**11 November 2026. New internally checked independent strengthening of the older general nonassociativity example. NOT a counterexample for the fitted diagonal.** Supports the bounded [Arrieta cube program](ProjectA_nonc_coherent_return_Arrieta_cube_kickoff_2026-11-11.md) by ruling out shortcuts using Hausdorffness, local compactness or closedness of an *arbitrary* symmetric relation. Uses exactly the block construction of [associativity audit I](A-relational-composition-associativity-audit-I-2026-11-07.md) but upgrades the ambient locale dramatically. The result does not contradict the **compact-closed** associativity theorem, since the constructed locale is not compact.

## 1. Dense-discrete refinement of Cantor space

Let C be Cantor space, D⊊C a dense proper subset (e.g. nonzero finite-support binary sequences). Let E=D with discrete topology, Z=C with discrete topology, Y=C with its usual compact zero-dimensional Hausdorff topology. Write
\[
f:E\longrightarrow Y \quad(d\mapsto d),\qquad
g:Z\longrightarrow Y\quad(z\mapsto z).
\]
The map f is a **locale-surjection**: \(f^*:\mathcal O(C)\to\mathcal P(D)\) is injective because D dense. The map g is a locale-surjection as well.

**Exact fibre product.** In Loc,
\[
E\times_Y Z\cong E
\]
and the projection to Z is the discrete inclusion \(j:D_d\hookrightarrow C_d\), NOT a locale-surjection. Derivation by frames: the pushout of
\[
\mathcal O(C)\longrightarrow\mathcal P(D),\quad
\mathcal O(C)\longrightarrow\mathcal P(C)
\]
is \(\mathcal P(D)\). Given arbitrary frame maps \(\alpha:\mathcal P(D)\to M,\ \beta:\mathcal P(C)\to M\) agreeing on \(\mathcal O(C)\), for every c∈C the T1-open \(C\setminus\{c\}\) gives
\[
\alpha(D\setminus\{c\})=\beta(C\setminus\{c\}).
\]
A frame map on a powerset frame preserves Boolean complements, so by complement uniqueness in M,
\[
\beta(\{c\})=\alpha(D\cap\{c\}).
\]
Joining over c∈A⊆C gives \(\beta(A)=\alpha(A\cap D)\). Conversely \(\beta=\alpha\circ j^*\) clearly agrees on the base. Hence the stated pushout and fibre product. In particular f is NOT surjection-stable along the discrete refinement g.

## 2. A single symmetric reflexive closed relation

Let
\[
X=\{*\}\sqcup E\sqcup Y\sqcup Z
\]
be the **topological sum** of the four spaces. It is a zero-dimensional locally compact Hausdorff space, hence sober and its localic finite products agree with the ordinary topological products. Its frame is continuous, but X is not compact (E and Z are infinite discrete).

Inside X² let R be total on the *→E block, S the graph of f on E→Y, and T the converse graph of g on Y→Z. Form
\[
Q=\Delta_X\ \vee\ R\vee R^\smile\vee S\vee S^\smile\vee T\vee T^\smile.
\]
All summands are **closed** in the ordinary product X×X:
- Δ is closed because X Hausdorff;
- R is clopen on its clopen block *×E;
- graph(f) is closed in E_d×C because E is discrete and each singleton \(\{f(e)\}\) is closed in C;
- graph(g) and its converse are likewise closed in Z_d×C.
Finite union of closed sublocales is closed. Thus Q is one **closed, reflexive, symmetric** localic endorelation of X.

The four blocks form a chain *–E–Y–Z; each Q-edge moves at most one step. A threefold path from * to Z therefore must traverse those four blocks in that exact order. The two bracketings have distinct restrictions to the clopen endpoint block *×Z:
\[
\begin{aligned}
((Q\circ Q)\circ Q)|_{*\times Z}&=*\times Z
&&\text{since }\operatorname{im}(f)=Y,\\
(Q\circ(Q\circ Q))|_{*\times Z}&=*\times D
&&\text{since }E\times_Y Z\cong E
\text{ and }\operatorname{im}(j)=D\subsetneq Z.
\end{aligned}
\]
These are distinct closed (indeed clopen) sublocales of the discrete endpoint block. Hence
\[
\boxed{(Q\circ Q)\circ Q\ \ne\ Q\circ(Q\circ Q).}
\]

**Why not compact-closed theorem:** X is noncompact, so the projection of a closed relation from X³ need not be proper. In fact the image of the graph f from the infinite discrete space E is the full compact Cantor locale Y, a direct image-closure phenomenon that drives the associativity failure.

## 3. Scope, lesson for CO-01

The example settles a stronger ambient control than earlier general examples: even **locally compact, zero-dimensional, Hausdorff**, and even **closed** relation, plus reflexivity/symmetry, do not force the localic relation cube to associate. It **does not** show that the **actual fitted diagonal** \(\mathcal D_X\) has an associative failure; in this regular space its fitted diagonal is the ordinary diagonal. Arrieta's distinct original example Y and its exotic relation A remain the special problem. This control eliminates an argument based solely on spatiality, Hausdorffness, local compactness, or the closed nature of an arbitrary relation. It suggests that a proof of CO-01 must exploit A's precise Θ-admissible-cover congruence rather than ambient separation alone.

Status: short directly verified frame-pushout proof, **not independently audited**, not yet a literature-priority assertion.
