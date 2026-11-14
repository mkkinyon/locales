# Project A / Q′ — canonical spectral predecessor-lift no-go

**13 November 2026 (America/Denver); INTERNAL adversarial test of the spectral-envelope density programme. Not externally audited. Q and Q′ OPEN.**

This note corrects an over-optimistic interpretation of [the spectral-envelope/ghost-boundary note](ProjectA_Q_SPECTRAL_ENVELOPE_DENSE_COVER_GHOST_FRONTIER_2026-11-13.md). A finite-compatible lattice-prime pair \((P,Q)\) has a common prime-filter predecessor \(R\subseteq P\cap Q\); any **bad** C-pair has all such predecessors outside the dense open \(\widehat u_C\). But the **converse is false even in the exact canonical envelope**, and is false for a locale satisfying the strong identity \(D_2=D\):

> A pair may **match** C at its endpoints, while **every** common prime predecessor avoids C.

This destroys an attractive but unjustified equivalence between the bad-C locus and the image of the ghost-predecessor incidence relation. Category preservation of the latter is, at best, a stronger separate sufficient approach, not a characterization of Q′.

## 0. Distinct predicates

Let \(L=\mathcal O(X)\), and let \(\widehat X\) be the compact coherent locale with frame \(\operatorname{Idl}(L_{\mathrm{lat}})\). Prime filters \(P,Q\subseteq L_{\mathrm{lat}}\) are points of \(\widehat X\). They are *finite-compatible* iff some prime filter \(R\subseteq P\cap Q\) exists (classical prime ideal theorem).

For a frame cover C of X, put \(\widehat u_C=\bigvee_{c\in C}\downarrow c\), a dense open of \(\widehat X\), proper if C has no finite subcover. Distinguish

- **endpoint matching:** \(\exists c\in C:\ c\in P\cap Q\);
- **predecessor matching:** \(\exists R\subseteq P\cap Q\) a prime filter with \(R\cap C\ne\varnothing\).

Predecessor matching implies endpoint matching. The reverse fails.

## 1. Concrete canonical-envelope countercontrol

Let \(V=\{p,x,y\}\) be the finite upper-Alexandrov space with order
\[
p<x,\qquad p<y,\qquad x\parallel y.
\]
Its opens are \(0,\{x\},\{y\},\{x,y\},V\). In particular **the only open containing p is V**.

Put
\[
X=\coprod_{n\in\omega}V_n,\qquad
L=\mathcal O(X)=\prod_{n\in\omega}\mathcal O(V_n).
\]
Write
\[
e_n=V_n,\quad
A=\bigcup_n\{x_n\},\quad
B=\bigcup_n\{y_n\},\quad
m=A\vee B.
\]
All these are X-opens; \(A\wedge B=0\), whereas \(m\ne1\) because it omits the \(p_n\)'s.

Let
\[
\boxed{C=\{e_n:n\in\omega\}\cup\{m\}.} \tag{1.1}
\]
This is a genuine X-cover, since \(\bigvee_n e_n=1\); it has **no finite subcover** because only e_n covers p_n. Its associated \(\widehat u_C\) is therefore a **proper dense open** of the **canonical** \(\widehat X=\operatorname{Loc}(\operatorname{Idl}(L_{\rm lat}))\).

Choose any nonprincipal ultrafilter \(\mathscr U\) on \(\omega\) (classical ultrafilter lemma). For \(z\in\{p,x,y\}\), define
\[
P_z=\left\{a=(a_n)\in L:
\{n:z_n\in a_n\}\in\mathscr U\right\}. \tag{1.2}
\]
Each \(P_z\) is a bounded-distributive-lattice prime filter: finite unions/intersections of opens are evaluated coordinatewise, and \(\mathscr U\) is an ultrafilter.

**Proposition 1.1 (matched endpoints, only ghost predecessors).** The pair \(P_x,P_y\) has all three properties:

1. It is **finite-compatible**, since \(P_p\subseteq P_x\cap P_y\) is a common prime predecessor.
2. It **matches** the frame cover C, because \(m\in P_x\cap P_y\).
3. **No** common prime predecessor \(R\subseteq P_x\cap P_y\) meets C. Thus every common predecessor lies outside \(\widehat u_C\), in its closed nowhere-dense ghost boundary.

*Proof.* Any open containing p_n contains x_n,y_n; hence \(P_p\subseteq P_x\cap P_y\). Also \(m\) contains all x_n and y_n, so m belongs to both endpoint prime filters.

For each n the component open e_n belongs to neither P_x nor P_y: its truth set is the singleton \(\{n\}\notin\mathscr U\). Thus no common predecessor contains any e_n.

Suppose a common predecessor R contained m. Since m=A∨B and R is prime, it would contain A or B. But \(A\notin P_y\) and \(B\notin P_x\), contradicting \(R\subseteq P_x\cap P_y\). Therefore R contains no member of C. □

This establishes, in the **canonical envelope and for a true X-cover C**, the strict pointwise inclusion
\[
\boxed{\begin{aligned}
&\{(P,Q):\exists R\subseteq P\cap Q,\ R\cap C\ne\varnothing\}\\
&\hspace{25pt}\subsetneq
\{(P,Q):P,Q\text{ finite-compatible},\ P\cap Q\cap C\ne\varnothing\}.
\end{aligned}} \tag{1.3}
\]
The witness is \((P_x,P_y)\).

The filters \(P_z\) themselves are **not** completely prime (the genuine frame cover \(\{e_n\}\) has no member of \(P_z\)), so they are spectral-envelope ghost points, not ordinary locale points of X. That is expected and does not invalidate the test.

## 2. Crucial positive check: the underlying locale has D₂=D

**Proposition 2.1.**
\[
\boxed{D_2(X)=D(X),\qquad W_2(X)=W(X).} \tag{2.1}
\]

*Proof for arbitrary generalized pairs.* Let h,k:L→M respect all finite X-covers, and let C′ be any arbitrary X-cover. Each **clopen compact** component \(V_n\) is covered by some finite \(F_n\subseteq C′\). The family \(F_n\cup\{e_n^*\}\) covers X, because \(e_n\le\bigvee F_n\). Finite compatibility yields
\[
1=h(e_n^*)\wedge k(e_n^*)\ \vee\
\bigvee_{c\in F_n}h(c)\wedge k(c).
\]
Meet with h(e_n): the first term vanishes, so
\[
h(e_n)\le\bigvee_{c\in F_n}h(c)\wedge k(c)
\le\bigvee_{c\in C′}h(c)\wedge k(c).
\]
Finally \(\bigvee_n h(e_n)=h(1)=1\). Therefore C′ is respected. Since C′ was arbitrary, D₂=D, and closure equality follows. No spatiality assumption on M is used. □

So the failure in Proposition 1.1 is **not** an incipient counterexample to Q′. It occurs even though the full-vs-finite fitted diagonals coincide exactly. It demonstrates that “all predecessors are ghosts for C” is much weaker than “C is not matched at the endpoints.”

## 3. Adversarial impact on the density programme

The [preceding note](ProjectA_Q_SPECTRAL_ENVELOPE_DENSE_COVER_GHOST_FRONTIER_2026-11-13.md) validly showed:
\[
\text{Boolean bad-C pair}
\Longrightarrow
\text{all common prime predecessors lie in }\widehat X\setminus\widehat u_C.
\]
This is one-way. The present countercontrol proves that even
\[
\text{all common predecessors lie in }\widehat X\setminus\widehat u_C
\Longrightarrow
\text{bad-C pair}
\]
is **false**, in the canonical setting.

Consequently the image of the *ghost-predecessor incidence* is generally **larger** than the C-bad locus. Its nowhere-density is an unnecessarily strong target, and a putative proof that the predecessor-incidence projection is skeletal/category-preserving would not be an **equivalent** reformulation of Q′. The example does **not** itself settle whether any particular localic incidence projection is skeletal; it refutes the identification of its image with endpoint badness.

Any future spectral approach must track the actual **endpoint matching-square open**
\[
\widehat w_C=\bigvee_{c\in C}(\downarrow c)\boxtimes(\downarrow c)
\]
and its pullback/restriction to the finite-diagonal relation. A predecessor \(R\) need only witness finite compatibility; it need not witness a given infinitary C-match.

**Recommended next question:** Can one obtain *relative density of endpoint matching squares* using the canonical embedding \(X\hookrightarrow\widehat X\), without inserting a false predecessor-lifting step? The coverwise relative-tail and chromatic constraints remain useful tests, but neither currently supplies this density theorem.

**Status:** Direct prime-filter calculation and arbitrary-target finite-cover proof internally checked; no external audit. Q and Q′ OPEN.
