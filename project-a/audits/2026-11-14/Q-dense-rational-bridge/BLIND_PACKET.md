# Project A — BLIND audit packet: the dense-rational-bridge proposed counterexample to Q and Q′

**14 November 2026 · proposed result, NOT externally audited.** The following is a complete working argument submitted for independent adversarial review. The universal questions Q and Q′ have been open in this project; this packet **claims** a simultaneous negative answer, conditional on verification. An independent prompt accompanies this packet. The separate internal audit is intentionally excluded.

## 0. Project A notation and self-contained background

This opening is the task-relevant **CORE + separation + Q/Q′ modules**, adapted from the modular Project A audit introduction `ProjectA_EXTERNAL_AUDIT_PACKET_DEFINITIONS_BOILERPLATE_2026-11-13.md`. It is incorporated here rather than requiring the referee to follow a link. Unrelated hierarchy, composition, and classifying-anima modules are omitted.

### 0.1 Locales, products, sublocales

We work in classical set theory with choice. All products and squares are **localic**. For a locale X, O(X) denotes its frame of opens; a locale map f:T→X corresponds to a frame homomorphism f*:O(X)→O(T) preserving finite meets and arbitrary joins. For locales X,Y,
\[
X^2=X\times X,\qquad O(X\times Y)=O(X)\otimes O(Y),
\]
with \(a\boxtimes b\) the open rectangle. Thus \((f,g)^*(a\boxtimes b)=f^*a\wedge g^*b\).

The diagonal sublocale of X² is Δ_X. Sublocale inequalities mean inclusion. Meets and joins in the lattice of sublocales must not be conflated with frame operations. For \(w\in O(P)\), let \(O_P(w)\) be the open sublocale and \(C_P(w)\) its complementary closed sublocale; \(C_P(w)\) does **not** mean closure of O(w). Let \(\operatorname{cl}_P(S)\) denote the least closed sublocale containing S. A sublocale S≤P is dense if cl_P(S)=P.

The Booleanization \(B(P)\hookrightarrow P\) is the double-negation sublocale. Its frame is the fixed-point frame for the nucleus \(a\mapsto a^{**}\), with joins taken in that frame. It is the least dense sublocale of P. In particular, a dense open \(u\) has \(u^*=0\), hence \(u^{**}=1\); its inverse image along \(B(P)\hookrightarrow P\) is 1. The Booleanization of a nonzero locale is nonzero.

### 0.2 Cover squares; full and finite fitted diagonals

An open cover \(\mathscr C\) of X is any family with \(\bigvee\mathscr C=1\), not necessarily finite. Define
\[
w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c\in O(X^2).
\]
These opens are cofinal among open neighborhoods of the diagonal, and the **full** and **finite-cover** fitted diagonals are
\[
\boxed{
D(X)=\bigwedge_{\mathscr C\text{ cover}}O_{X^2}(w_{\mathscr C}),
\qquad
D_2(X)=\bigwedge_{\mathscr F\text{ finite cover}}O_{X^2}(w_{\mathscr F}).
}
\tag{0.1}
\]
The subscript 2 means *finite covers*, **not** a second iteration. Always Δ_X≤D(X)≤D₂(X).

Equivalently, a generalized pair \((f,g):T→X^2\) factors through D(X) exactly if
\[
\bigvee_{c\in\mathscr C}f^*(c)\wedge g^*(c)=1_{O(T)}
\quad\text{for every cover }\mathscr C,
\tag{0.2}
\]
and through D₂(X) if (0.2) holds for every **finite** cover. It factors through Δ_X iff f=g.

Let
\[
W(X)=\operatorname{cl}_{X^2}D(X),\qquad
W_2(X)=\operatorname{cl}_{X^2}D_2(X),\qquad
I(X)=\operatorname{cl}_{X^2}\Delta_X.
\tag{0.3}
\]
Thus I≤W≤W₂, all closed. A strict nonclosed difference D₂>D need **not** imply W₂>W.

### 0.3 Urysohn relation and the two questions

For a∈O(X), write a*=a→0 for its pseudocomplement. Define the Urysohn-style **closed** relation
\[
d_U=\bigvee_{a^*\vee b^*=1}a\boxtimes b,
\qquad U(X)=C_{X^2}(d_U).
\tag{0.4}
\]
The finite cover \(\{a^*,b^*\}\) shows D₂(X)≤U(X) for every locale: when a*∨b*=1, its cover square is disjoint from a⊠b. Because U is closed,
\[
\boxed{I(X)\le W(X)\le W_2(X)\le U(X).}
\tag{0.5}
\]
The **universal** questions under investigation are:

- **Q′:** Is W(X)=W₂(X) for every locale X?
- **Q:** Does W₂(X)=U(X) imply W(X)=U(X) for every locale X?

The project also writes these questions using cover operators \(\Phi,\Phi_2\); those operators are not needed in the proof below. The proposed example would answer **both** questions negatively. No priority/novelty claim is made.

### 0.4 Imports made explicit

We use two elementary locale facts, both open to audit:

1. **Regular base:** for a regular locale Z, \(D(Z)=D_2(Z)=U(Z)=\Delta_Z\). In particular the diagonal of ordinary ℝ is a closed sublocale of its localic square.
2. **Naturality:** for a locale map \(p:X→Z\), both fitted diagonals and their closed hulls lie in the pullbacks of their counterparts on Z; likewise \(U(X)\le(p\times p)^{-1}U(Z)\). For the fitted diagonal this follows by pulling back arbitrary/finite Z-covers to X-covers. For the hull, use that preimages of closed sublocales are closed.

These imply that for a map to regular Z, \(D(X),D_2(X),W(X),W_2(X),U(X)\) all lie in the **closed fiber square** \(F=X\times_ZX\subseteq X^2\).

## 1. The proposed topological space

Let Z=ℝ with its usual topology. Define a set
\[
X=S\sqcup T\sqcup H,
\quad S=\{s_x:x\in\mathbb R\},\quad
T=\{t_x:x\in\mathbb R\},\quad
H=\{b_q:q\in\mathbb Q\}.
\tag{1.1}
\]
S and T are **disjoint OPEN** subspaces, each with the usual real-line topology. For rational q, declare the following a basic neighborhood of b_q:
\[
N(q,\varepsilon)
=\{b_q\}
\cup\{s_x:q-\varepsilon<x<q\}
\cup\{t_x:q<x<q+\varepsilon\}
\qquad(\varepsilon>0).
\tag{1.2}
\]
The ordinary S-, T-opens together with all N(q,ε) constitute a basis. For distinct rational q,r, the intersection of their bridge neighborhoods contains only open pieces of S and T; thus the basis-intersection condition is satisfied.

Let
\[
p:X\longrightarrow\mathbb R,
\qquad p(s_x)=p(t_x)=x,\quad p(b_q)=q.
\tag{1.3}
\]
The restriction of p to S, T, or N(q,ε) is a homeomorphism onto an open interval. Hence **p is an open local homeomorphism**, or étale map. Every fiber is finite discrete:
\[
p^{-1}(x)=
\begin{cases}
\{s_x,t_x\},&x\notin\mathbb Q,\\
\{s_x,t_x,b_x\},&x\in\mathbb Q.
\end{cases}
\tag{1.4}
\]
Using rational intervals gives a countable basis. The space is T₁ (the points of each fiber are individually closed, and base-separated points are distinguishable). It is sober: the displayed open charts are sober copies of intervals of ℝ, and sobriety is local on open covers. The sobriety claim is a control, not needed for the frame-pair computation once X is replaced by the locale O(X).

For each q let \(N_q=\bigcup_{\varepsilon>0}N(q,\varepsilon)\), an open section mapped homeomorphically to ℝ. The infinite family
\[
\mathscr A=\{S,T\}\cup\{N_q:q\in\mathbb Q\}
\tag{1.5}
\]
is an X-open cover **by sections** of p. Its absence of a finite subcover is immediate from the infinitely many distinct b_q.

## 2. Key lemma: every finite cover has a dense common-member locus

For any open cover \(\mathscr C\) of X, define
\[
m_{\mathscr C}
=\bigvee_{c\in\mathscr C}s^*(c)\wedge t^*(c)
\quad\in O(\mathbb R).
\tag{2.1}
\]
Here s,t:ℝ→X are the two global sections.

**Lemma 2.1 (proposed; elementary topology).** For **every finite** X-open cover \(\mathscr F\), the open \(m_{\mathscr F}\) is dense in ℝ.

*Proof.* Let \(\mathscr F=\{c_1,\ldots,c_n\}\). If m_F were not dense, there would be a nonempty open interval I⊂ℝ with I∩m_F=∅. Write
\[
A_i=s^*(c_i)\cap I,\qquad B_i=t^*(c_i)\cap I.
\]
These are disjoint opens in I. For any rational q∈I, at least one c_i contains b_q. By (1.2), that c_i contains S-points throughout a sufficiently small left interval ending at q and T-points throughout a right interval starting at q. Hence q∈cl_I(A_i). Since B_i contains a right interval and A_i∩B_i=∅, q∉A_i; thus q∈∂_I A_i. Therefore
\[
\mathbb Q\cap I\subseteq\bigcup_{i=1}^n\partial_I A_i.
\tag{2.2}
\]
Each boundary of an OPEN subset of I is closed nowhere dense. A finite union of such sets cannot contain the dense subset ℚ∩I. Contradiction. □

**Important quantifiers:** This holds for arbitrary finite open covers of the entire X, not only covers consisting of our selected chart sections. It implies that the proposed local finite-cover separation criterion fails on every nonempty base open, not just on the whole ℝ.

## 3. A Booleanization-valued finite-compatible pair

Let \(\beta:B(\mathbb R)\hookrightarrow\mathbb R\) be the Booleanization. Its open frame is RO(ℝ), the complete Boolean algebra of regular-open subsets. The inverse-image quotient sends an open u to u** (with joins understood in RO(ℝ)). Since B(ℝ) is nonzero, the following two frame maps have a nonzero target:
\[
h=\beta^*\circ s^*,\qquad k=\beta^*\circ t^*
:O(X)\longrightarrow O(B(\mathbb R)).
\tag{3.1}
\]

For ANY finite X-cover F, Lemma 2.1 says m_F is dense, so m_F*=0 and \(\beta^*m_F=m_F^{**}=1\). Consequently
\[
\boxed{
\bigvee_{c\in\mathscr F}h(c)\wedge k(c)
=\beta^*m_{\mathscr F}=1.
}
\tag{3.2}
\]
The generalized pair \((h,k):B(\mathbb R)→X^2\) therefore factors through **D₂(X)**.

The two sections always differ, so the map lands in the fibered cross-chart
\[
J=S\times_{\mathbb R}T\ \cong\ \mathbb R
\quad\subseteq\quad F=X\times_{\mathbb R}X.
\tag{3.3}
\]
This chart is **open in F** (not claimed open in the whole X²) and lies in the ordinary open X²-rectangle S⊠T.

For the INFINITE cover A from (1.5), every member is a p-section, hence contains at most ONE of s_x,t_x for each x. Thus \(m_{\mathscr A}=0\), giving
\[
\bigvee_{c\in\mathscr A}h(c)\wedge k(c)=0,
\tag{3.4}
\]
so the same generalized pair does NOT factor through D(X).

In fact the Booleanization is dense in J. Its image is a **NONZERO dense sublocale of J contained in D₂(X)**. A concrete pointwise check: for every fixed x the binary open cover \(\{X\setminus\{s_x\},X\setminus\{t_x\}\}\) excludes the ordinary pair (s_x,t_x) from D₂. Hence the finite-compatible witness in J is genuinely point-free.

## 4. The full fitted diagonal equals Δ_X

**Lemma 4.1 (full open-atlas descent).** If a locale map p:X→Z has an arbitrary open cover by sublocales on which p is monic, and D(Z)=Δ_Z, then D(X)=Δ_X.

*Proof.* For any generalized pair (f,g):Y→D(X), pulling back all covers of Z shows pf=pg. Apply the square condition to the open monic atlas \(\{U_i\}\). The opens \(f^*U_i\wedge g^*U_i\) cover Y. On each such open both f,g land in U_i and have equal images under p, so f=g locally by monicity. Because equality of locale maps is local on the domain, f=g globally. Thus D(X)≤Δ_X, and the reverse inclusion is universal. □

Apply this to p:X→ℝ and the infinite section cover A. Regularity of ℝ gives D(ℝ)=Δ_ℝ, so
\[
\boxed{D(X)=\Delta_X,\qquad W(X)=I(X).}
\tag{4.1}
\]

S and T are disjoint OPEN subspaces of X. The open rectangle S⊠T is disjoint from Δ_X, hence also from its closure I(X). In particular,
\[
W(X)\wedge J=I(X)\wedge J=0.
\tag{4.2}
\]
But the nonzero Booleanization-valued generalized pair factors through D₂(X)∧J by (3.2)–(3.3). Therefore W₂(X)∧J≠0, whereas W(X)∧J=0:
\[
\boxed{W(X)<W_2(X).}
\tag{4.3}
\]
This is the claimed negative answer to Q′. It is a **closed-hull** separation, not merely D₂>D.

## 5. Proposed stronger calculation: W₂(X)=U(X)=F

**Lemma 5.1.** The fiber square \(F=X\times_{\mathbb R}X\) is a CLOSED, SPATIAL sublocale of X².

*Proof.* Since Δ_ℝ is closed, its pullback F along p×p is closed. For every pair of open section charts U_i,U_j from the atlas A, the fiber product \(U_i\times_{\mathbb R}U_j\) is OPEN in F and maps isomorphically to the intersection of their images in ℝ. These open, spatial charts cover F; thus F is spatial. □

**Lemma 5.2.** \(J=S\times_{\mathbb R}T\le W_2(X)\), and likewise the transposed chart \(J^\mathrm{op}=T\times_{\mathbb R}S\le W_2(X)\).

*Proof.* The pullback of the CLOSED sublocale W₂(X) along J→F is a closed sublocale of J. It contains the image of B(ℝ), which is dense in J by construction. Hence it is all J. Symmetry of D₂ and its closure gives the transposed containment. □

**Theorem 5.3 (proposed).** \(W_2(X)=U(X)=F\).

*Proof.* Naturality and the usual inclusions give \(W_2(X)\le U(X)\le F\). We show the closed sublocale W₂(X) contains **every ordinary point of F**.

For each irrational x, the fiber consists of s_x,t_x; its ordered pairs are diagonal or lie in J or J^op. For rational q, a third point b_q occurs. Besides these pairs, the new ordered pairs are (b_q,s_q), (s_q,b_q), (b_q,t_q), (t_q,b_q), and (b_q,b_q). The diagonal pair lies in I(X). Every neighborhood of b_q meets every neighborhood of s_q along the left-hand S-germ near q, so (b_q,s_q) and its reverse lie in I(X)=cl Δ_X. The right-hand T-germ gives the analogous assertion for b_q,t_q. Therefore all these points belong to I(X)≤W₂(X).

Thus every ordinary point of the SPATIAL locale F lies in the CLOSED sublocale W₂(X). Its complementary open in F must be zero, so W₂(X)=F. The sandwich W₂≤U≤F gives U(X)=F. □

Finally (4.1), (4.2), and Theorem 5.3 yield
\[
\boxed{
W(X)=I(X)\quad<\quad W_2(X)=U(X)=X\times_{\mathbb R}X.
}
\tag{5.1}
\]
This would refute Q as well: its antecedent W₂=U holds, but its conclusion W=U fails.

## 6. What the referee should challenge

The verdict is **NOT established by prior citations**; this is a newly proposed complete proof whose central claims must be independently tested. In particular:

1. Does the basis (1.2) genuinely make the infinite-bridge space étale/sober, with S and T OPEN and disjoint? Might some hidden identification force S and T to meet?
2. Does the proof that m_F is dense really apply to **all** finite covers, and is every open containing b_q forced to contain BOTH indicated one-sided germs?
3. Is the Booleanization-valued pair nonzero and does its frame-homomorphism computation correctly handle arbitrary joins versus double-negation closure?
4. Is the infinite section cover sufficient to give D(X)=Δ_X as a LOCALIC equality rather than equality only on ordinary points?
5. Does the nonzero D₂ witness land in the actual open rectangle S⊠T disjoint from I, securing W₂>W?
6. Does spatiality of F follow from the étale chart cover, and is it legitimate to deduce W₂=F from the containment of all ordinary F-points in a **closed** sublocale?

The claimed proof uses no unresolved universal theorem Q or Q′ as an input. It does not claim a literature-priority result. A successful first blind report should precede repository-wide status changes.
