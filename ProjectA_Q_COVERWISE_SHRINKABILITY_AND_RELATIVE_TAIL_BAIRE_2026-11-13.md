# Project A / Q and Q′ — coverwise finite shrinkability and dense-tail geometry *inside* the finite closure

**13 November 2026 (Denver date); new INTERNAL working lemmas, not externally audited.** These are a bounded continuation after [fixed-point compact/regular sector localization](ProjectA_Q_FIXED_POINT_COMPACT_REGULAR_SECTOR_LOCALIZATION_2026-11-13.md), in response to the proposal to study Baire-category **inside** \(D_2\) or its closure instead of merely the closed coordinate support. The results refine the obstruction but **do not prove Q or Q′**.

## 0. Notation and logical status

Let \(L=\mathcal O(X)\), \(P=L\oplus L=\mathcal O(X^2)\). For any cover \(C\subseteq L\) with \(\bigvee C=1\), put
\[
w_C=\bigvee_{c\in C}c\boxtimes c,\qquad
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
\Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]
Fix an **arbitrary** \(\Phi_2\)-fixed \(d\in P\): for each finite cover \(G\), \(w_G\to d=d\).
Write \(Y_d=\mathfrak c_{X^2}(d)\), whose frame is \(\uparrow d\). For each arbitrary cover \(C\), define
\[
\rho_{C,d}=w_C\to d\ge d,\qquad
E_{C,d}=\mathfrak o_{Y_d}(\rho_{C,d}).
\]
Then \(E_{C,d}\) is the **largest relatively open sublocale of \(Y_d\)** disjoint from the restriction of \(w_C\). It is zero exactly when \(w_C\to d=d\). For \(d=d_0=\Phi_2^\infty(0)\), \(Y_d=W_2=\operatorname{cl}D_2\), and \(Q′\) says all these \(E_{C,d_0}\) are zero. At rank one \(d=z_1=\Phi(0)=\Phi_2(0)\), the same test is relevant to Q when \(z_1\) is finite-fixed.

The notation \(u\prec a\) is the **rather-below / well-inside relation** in \(L\):
\[
u\prec a\quad\Longleftrightarrow\quad u^*\vee a=1,
\]
where \(u^*=u\to0\). This entails \(u\le a\), but is much stronger.

## 1. A cover-specific finite-shrinkability open

For an arbitrary cover \(C\), let
\[
\boxed{p_C=\bigvee\{u\in L:\exists F\subseteq C\text{ finite},\ u\prec\bigvee F\}.} \tag{1.1}
\]
The join need not itself be rather-below any finite subjoin.

**Theorem 1.1 (cover-specific one-sided exclusion).** For every \(\Phi_2\)-fixed \(d\) and every cover \(C\),
\[
\boxed{
(p_C\boxtimes1)\wedge(w_C\to d)\le d,\qquad
(1\boxtimes p_C)\wedge(w_C\to d)\le d.} \tag{1.2}
\]
Hence every marked relative-open hole \(E_{C,d}\) is contained in the closed square
\[
\boxed{E_{C,d}\le\mathfrak c_X(p_C)\times\mathfrak c_X(p_C).} \tag{1.3}
\]

*Proof.* Choose \(u\prec\bigvee F\) for a finite \(F\subseteq C\). The finite family \(G=F\cup\{u^*\}\) covers \(X\). Put \(r=(u\boxtimes1)\wedge(w_C\to d)\). We have \(r\wedge(u^*\boxtimes u^*)=0\), and for \(c\in F\),
\[
r\wedge(c\boxtimes c)\le (w_C\to d)\wedge w_C\le d.
\]
Thus \(r\wedge w_G\le d\), whence \(r\le w_G\to d=d\). Join over all such \(u\) and swap coordinates for the second half. Inside \(Y_d\), (1.2) says the marked hole has empty intersection with the open sectors \(p_C\boxtimes1\) and \(1\boxtimes p_C\), so it factors through their common closed complement (1.3). □

**Corollary 1.2.** If \(p_C=1\), then \(w_C\to d=d\) at **every** finite-fixed \(d\). Moreover \(D_2(X)\le\mathfrak o(w_C)\): otherwise the nonzero closed \(C\)-zero part of \(D_2\) would give a finite-compatible pair into a nonzero target with \(w_C=0\); Lemma 1.3 below would force its coordinate maps to annihilate \(p_C=1\), contradicting unitality. If \(p_C=1\) for **every** cover, then \(D_2=D\) (stronger than Q′).

The previous compact/regular closed-patch invariant \(p_X\) (join of ambient opens supported in globally closed compact/regular sublocales) satisfies
\[
\boxed{p_X\le p_C\quad\text{for every cover }C.} \tag{1.4}
\]
For a compact closed \(K=\mathfrak c(e)\) supporting \(u\), compactness yields finite \(F\subseteq C\) with \(e\vee\bigvee F=1\); since \(e\le u^*\), \(u\prec\bigvee F\). For regular \(K\), the original proof writes \(u=\bigvee_{c\in C,v\prec_K(e\vee c)}u\wedge v\) and supplies \(b\ge e\) with \(b\vee c=1\), \((u\wedge v)\wedge b=0\). Thus each \(u\wedge v\prec c\) *in \(X\)*. So (1.4) holds. In particular the new cover-specific closed core \(\mathfrak c(p_C)\) is no larger than the earlier universal \(\mathfrak c(p_X)\).

**Lemma 1.3 (normalizing kills all finite-shrinkability).** Let \(h,k:L\to M\) be frame homomorphisms into a nonzero frame \(M\), compatible with every finite cover, and suppose
\[
\bigvee_{c\in C}h(c)\wedge k(c)=0.
\]
Then
\[
\boxed{h(p_C)=k(p_C)=0.} \tag{1.5}
\]

*Proof.* Each summand \(h(c)\wedge k(c)\) vanishes. For \(u\prec\bigvee F\), finite-cover compatibility with \(G=F\cup\{u^*\}\) gives
\[
1=\bigl(h(u^*)\wedge k(u^*)\bigr)
 \vee\bigvee_{c\in F}h(c)\wedge k(c)
 =h(u^*)\wedge k(u^*).
\]
Consequently \(h(u^*)=k(u^*)=1\); since \(u\wedge u^*=0\), both \(h(u)\) and \(k(u)\) are zero. Preserve the defining join. □

In particular, if **either** coordinate map is zero-reflecting, then \(p_C=0\). This applies to any weak defect that factors through a **common** closed coordinate support on which at least one coordinate reflects zero. In particular, for the independently established symmetric marked Q′ hole, both coordinate maps separately reflect zero after the canonical closed-support reduction. A one-coordinate support reduction alone does **not** automatically make the other coordinate factor through the same closed sublocale. On that *reduced* locale \(K\), the **restricted** cover \(C_K\) therefore satisfies
\[
\boxed{p_{C_K}=0.} \tag{1.6}
\]
This is a stronger cover-dependent obstruction than simply having no compact/regular closed-supported open sector. However, it remains a **support** obstruction, not the required density statement.

Two elementary bookkeeping facts: finite covers have \(p_C=1\); if \(C'\) refines \(C\), then \(p_{C'}\le p_C\). Neither fact implies that \(p_C\) is complemented, dense, or regular.

## 2. A relative dense-tail theorem

For each **finite** subset \(F\subseteq C\), put
\[
t_F=\bigvee_{c\in C\setminus F}c.
\]
Then \(G_F=F\cup\{t_F\}\) is a finite cover of \(X\), so the restricted open \(w_{G_F}\vee d\) is **dense** in \(Y_d\):
\[
(w_{G_F}\vee d)\to_{\,\uparrow d}d
=(w_{G_F}\to d)=d. \tag{2.1}
\]

**Theorem 2.1 (dense tails *inside* any marked open hole).** For every cover \(C\), every \(\Phi_2\)-fixed \(d\), and every finite \(F\subseteq C\), the open
\[
\boxed{
E_{C,d}\wedge\mathfrak o_{Y_d}(t_F\boxtimes t_F)
\text{ is DENSE in }E_{C,d}.} \tag{2.2}
\]
At the same time
\[
E_{C,d}\wedge\mathfrak o_{Y_d}(c\boxtimes c)=0
\quad(c\in C). \tag{2.3}
\]

*Proof.* Let \(E=E_{C,d}\). By the definition \(\rho_{C,d}=w_C\to d\), the restriction of each \(c\boxtimes c\le w_C\) is zero on E. Consequently \(w_F\) restricts to zero on E. In the frame \(\mathcal O(E)\), the restriction of the dense open \(w_{G_F}=w_F\vee(t_F\boxtimes t_F)\) therefore equals the restriction of \(t_F\boxtimes t_F\). A dense open remains dense under restriction to an open sublocale, proving (2.2). Equation (2.3) was already used. □

This theorem is *different* from the Stone-target Baire lemma: the dense tails occur in the actual **relatively open marked hole \(E\) of \(Y_d\)**. It is nonetheless only a **necessary** condition for the existence of a hole.

When \(C=\{c_n:n<\omega\}\), put \(t_n=\bigvee_{m\ge n}c_m\). If \(E\ne0\), there is a descending sequence of dense opens
\[
E\wedge\mathfrak o(t_0\boxtimes t_0)\ \ge\
E\wedge\mathfrak o(t_1\boxtimes t_1)\ \ge\cdots \tag{2.4}
\]
inside E, although every individual same-index square \(c_n\boxtimes c_n\) vanishes there.

**Corollary 2.2 (conditional intrinsic Baire test, countable covers).** Suppose **every open sublocale of \(Y_d\) is Baire** in the localic sense. For a countable cover \(C\) define its tail-intersection sublocale
\[
T_{C,d}=\bigwedge_{n<\omega}\mathfrak o_{Y_d}(t_n\boxtimes t_n),
\]
where the meet is in the **sublocale lattice**, *not* the frame meet of the open elements. Then
\[
\boxed{E_{C,d}\le\operatorname{cl}_{Y_d}(T_{C,d}).} \tag{2.5}
\]
In particular, if \(T_{C,d}\) is nowhere dense in \(Y_d\), then \(E_{C,d}=0\).

*Proof.* If E is nonzero and Baire, the countable intersection of the dense opens (2.4) is dense in E. That intersection is \(E\wedge T_{C,d}\). Thus E lies in the closure of \(T_{C,d}\). If this closure has empty interior in \(Y_d\), the only open E it contains is zero. □

For \(d=d_0\), this gives a precise **sufficient test for Q′ on countable covers** involving relative density inside \(W_2\). A Lindelöf X reduces all-cover density to countable subcovers, if the stated Baire and tail conditions hold for each such countable subcover. The corollary does **not** assert that these tail intersections are always nowhere dense.

## 3. Concrete Scott control and adversarial limits

Take the completed branching Scott locale from the previous frontier tests:
\[
S=\{s:\omega\rightharpoonup 2:\operatorname{dom}s\ne\emptyset\},
\]
finite or infinite partial functions ordered by extension. The singleton-literal opens \(c_{n,i}=\uparrow\{n\mapsto i\}\) form a countable cover C of S.

**Claim 3.1.** This cover has \(p_C=0\). Given any nonzero Scott-open u, choose a finite condition s with \(\uparrow s\subseteq u\). For any finite F⊂C, choose a coordinate m outside the domains mentioned by F and s; the singleton condition \(p=\{m\mapsto0\}\) is outside \(\bigvee F\), but \(\uparrow p\cap u\ne\emptyset\) (extend s by p). Thus \(p\notin u^*\), showing \(u^*\vee\bigvee F\ne1\). No nonzero u is rather-below a finite subjoin. □

Moreover each \(t_n\) is Scott-dense in S, since any finite basic condition can be extended with a fresh literal from the tail. The product tail squares are dense in S². The existing calculations establish \(D_2(S)>D(S)\) but \(W_2(S)=W(S)=S²\), so **Q′ holds** there.

This is a decisive negative check on interpretation: **\(p_C=0\)** and **dense tail recurrence** can already occur together in a **Q′-positive** locale. Their conjunction is *not* evidence of a Q′ counterexample; the unsolved part is whether some tail-recurrent defect occupies a **nonzero relatively open patch** of \(W_2\).

The Baire corollary is also *conditional*. An intersection of countably many dense opens need not be an open sublocale, and emptiness of its set of ordinary points does **not** automatically make the intersection sublocale zero in a nonspatial setting.

## 4. Research decision

The earlier uniform closed core \(R_X\) can be refined to a cover-dependent core \(\mathfrak c_X(p_C)\), and the \(\Phi_2\)-fixed-point condition gives **dense finite-tail squares in every hypothetical marked hole**. This is a clean intrinsic formulation of the kind of recurrence a Q′ hole must support.

However the normalized weak Scott defect satisfies the corresponding shrinkability obstruction, and its tails are dense, even though Q′ holds. Do **not** treat another support reduction or tail recurrence alone as a proof of Q′.

The next actual target is the *interior of the closure of \(T_{C,d_0}\)* in \(W_2\) and how it interacts with the **individual** forbidden squares \(c_n^2\). Prove an exclusion principle for that interaction or construct an example where it persists as a relatively open region. Universal **Q/Q′ remain OPEN**.

**Verification status:** direct frame/sublocale calculations internally checked; not externally refereed.
