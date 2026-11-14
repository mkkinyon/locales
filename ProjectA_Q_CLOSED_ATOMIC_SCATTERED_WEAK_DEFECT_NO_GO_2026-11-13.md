# Project A / Q, Q′ — closed-atomic support obstruction; scattered-space positive class

**Originally internally audited on 13 November 2026; the theorem was independently blind-refereed on 14 November (no error found).** Published usages of “scattered locale” vary. The frame condition below is now identified precisely with the topology of a **scattered sober \(T_0\) space**; it is not a new wider point-free class. See §2.3.

## 0. Set-up and precise hypothesis

For \(L=\mathcal O(X)\) and an \(L\)-cover \(C\), put
\[
w_C=\bigvee_{c\in C}c\boxtimes c\in P=L\oplus L,
\qquad
D_2=\bigwedge_{F\text{ finite cover}}\mathfrak o(w_F),
\qquad
D=\bigwedge_{C\text{ arbitrary cover}}\mathfrak o(w_C)
\]
in the sublocale coframe, so \(D\le D_2\). Maps \(h,k:L\to M\) are *binary-cover compatible* if, for every \(u\vee v=1_L\),
\[
(h(u)\wedge k(u))\vee(h(v)\wedge k(v))=1_M. \tag{0.1}
\]
In particular, compatibility with every finite cover implies (0.1).

Call \(L\) **closed-atomic** when, for every \(e<1_L\), the interval frame
\(\mathcal O(\mathfrak c_X(e))\cong [e,1_L]\) has an atom \(a>e\).

## 1. Main obstruction, arbitrary targets

**Theorem 1.1 (atomless closed supports of defective coordinate maps).**
Let \(h,k:L\to M\) be binary-cover compatible maps into a nontrivial frame \(M\), and suppose some arbitrary cover \(C\) is defective:
\[
m_C=\bigvee_{c\in C}h(c)\wedge k(c)<1_M. \tag{1.1}
\]
Pass to the nontrivial quotient frame \(M'=\uparrow m_C\) via \(q(t)=t\vee m_C\), and set \(h'=qh,k'=qk\). The matching value of \(C\) is now \(0_{M'}=m_C\). The least closed supports of **both** coordinate maps \(h',k'\) have atomless frames of opens. Explicitly, if
\[
e_h=\bigvee\{a\in L:h'(a)=0_{M'}\},\qquad
e_k=\bigvee\{a\in L:k'(a)=0_{M'}\},
\]
then both \([e_h,1]\) and \([e_k,1]\) are atomless.

*Proof.* Rename \(M',h',k'\) as \(M,h,k\), so \(\bigvee_C h(c)\wedge k(c)=0_M\). Let \(e=e_h\). Since \(h\) preserves all joins,
\[
h(e)=0_M,\qquad h(t)=0_M\iff t\le e,\qquad h(t)=h(t\vee e). \tag{1.2}
\]
Also \(e<1_L\), since \(M\) is nontrivial and \(h(1_L)=1_M\).

Suppose \([e,1_L]\) has an atom \(a>e\). For every \(c\in C\),
\(a\wedge(c\vee e)\) lies in \([e,a]\), so it equals either \(e\) or \(a\).
Partition \(C=C_1\sqcup C_0\), where
\[
C_1=\{c:a\le c\vee e\},\qquad
C_0=\{c:a\wedge(c\vee e)=e\},
\qquad u=\bigvee C_1,\quad v=\bigvee C_0.
\]
The family \(C_1\) is **nonempty**, because
\[
a=a\wedge\bigvee_{c\in C}(c\vee e)
 =\bigvee_{c\in C}\bigl(a\wedge(c\vee e)\bigr)>e.
\]
Moreover \(u\vee v=1_L\), so \(\{u,v\}\) is a binary cover. By (1.2),
\(h(a)\neq0_M\), \(h(a)\le h(c)\) for all \(c\in C_1\), and
\(h(a)\wedge h(c)=0_M\) for all \(c\in C_0\). Thus
\[
h(a)\le h(u),\qquad h(a)\wedge h(v)=0_M. \tag{1.3}
\]
Meet the binary-cover identity (0.1) with \(h(a)\). By (1.3) and arbitrary distributivity in \(M\),
\[
h(a)=h(a)\wedge k(u)
=\bigvee_{c\in C_1}\bigl(h(a)\wedge k(c)\bigr)=0_M,
\]
since \(h(a)\le h(c)\) and \(h(c)\wedge k(c)=0_M\) for every \(c\in C_1\). Contradiction. The argument for \(e_k\) interchanges the coordinates. □

**Key point:** This is a *weak-defect* obstruction involving arbitrary, possibly nonspatial target frames. It is not restricted to ordinary pairs or relatively open holes.

## 2. Consequences for D, W and scattered spaces

**Corollary 2.1.** If \(L\) is closed-atomic, every binary-compatible pair into any frame matches every arbitrary cover. Therefore
\[
\boxed{D_2(X)=D(X),\qquad W_2(X)=W(X).} \tag{2.1}
\]
*Proof.* A defective pair would contradict closed-atomicity by Theorem 1.1. A locale map into \(X^2\), represented by a coordinate pair into its domain frame, factors through \(D_2\) exactly when it matches every finite cover, and through \(D\) when it matches every cover. Equality of these universal factorization conditions yields \(D_2=D\). Taking closures yields \(W_2=W\). □

**Corollary 2.2 (topologically scattered spatial locales).** Suppose \(X\) is spatial and the ordinary sober point space of \(X\) is scattered: **every nonempty closed subspace has an isolated point**. Then \(L\) is closed-atomic. Indeed each nonzero closed sublocale \(\mathfrak c(e)\) is represented by the corresponding nonempty closed point subspace, and an isolated singleton there is an atom of \([e,1]\). Consequently (2.1) holds, without local compactness, regularity, Baire assumptions, or spatiality of the *localic square* \(X^2\).

*Terminology/provenance:* The precise location of the scattered-space definition in Picado–Pultr, *Frames and Locales* (2012), VI §8.1, has **not** been checked against the book itself. We use the explicit topological definition in Corollary 2.2, and do not equate it with other uses of “scattered locale”.

### 2.3 Converse: every closed-atomic frame is spatial and scattered

**Proposition 2.3 (referee observation).** The following are equivalent for a frame \(L\):

1. Every proper closed interval frame \([e,1_L]\) has an atom.
2. \(L\cong\mathcal O(X)\) for a scattered sober \(T_0\) space \(X\).

*Proof.* (2)⇒(1) is Corollary 2.2. Conversely, let \(u\nleq v\) and put \(e=u\to v<1_L\). Choose an atom \(a>e\) in \([e,1]\) and set \(p=a\to e\). If \(x\nleq p\), then \(a\wedge x\nleq e\), so atomicity forces \(a\le x\vee e\). Therefore if \(x,y\nleq p\), we get \(a\le(x\vee e)\wedge(y\vee e)=(x\wedge y)\vee e\), hence \(x\wedge y\nleq p\). Thus \(p\) is a prime element of \(L\), defining a frame map \(L\to2\). Also \(v\le e\le p\) whereas \(u\nleq p\) (else \(a\wedge u\le e=u\to v\), yielding \(a\le u\to v=e\)). These points separate every \(u\nleq v\), so \(L\) is spatial. For each proper \(e\), an atom of \([e,1]\) is a nonempty minimal open of the corresponding closed point subspace; \(T_0\) then makes it an isolated singleton. Hence the space is scattered. A scattered \(T_0\) space is sober because every nonempty irreducible closed subspace has an isolated point, which must be its generic point. \(\square\)

The theorem gives a useful intrinsic test and a point-free proof, but the **class is exactly the familiar scattered \(T_0\) class**.

## 3. Full-versus-finite fixed points and Q/Q′

Write
\[
\Phi_2(d)=\bigvee_{F\text{ finite cover}}(w_F\to d),\qquad
\Phi(d)=\bigvee_{C\text{ arbitrary cover}}(w_C\to d).
\]
**Lemma 3.1 (sharpened).** \(D_2=D\) **if and only if** every \(\Phi_2\)-fixed open \(d\in P\) is also \(\Phi\)-fixed. This follows immediately from \(D_2=\operatorname{Fix}(\Phi_2)\) and \(D=\operatorname{Fix}(\Phi)\) as subsets of \(P\). The original independent Booleanization proof of the nontrivial direction is retained below.

*Proof.* If \(\Phi_2(d)=d\) but \(\Phi(d)>d\), choose \(C\) with
\(r=(w_C\to d)\nleq d\). The relatively open sublocale
\(E=\mathfrak o_{\mathfrak c_{X^2}(d)}(r)\) is nonzero and has \(w_C|_E=0\). For every finite cover \(F\), \(w_F\to d=d\), so \(w_F\) is dense open on \(\mathfrak c(d)\) and on \(E\). Compose the two coordinate maps \(L\rightrightarrows\mathcal O(E)\) with the canonical quotient to the **nontrivial double-negation Booleanization** \(B(E)\). Every finite-cover matching square becomes top (it was dense), while the \(C\)-square remains bottom. This constructs a finite-compatible, \(C\)-defective pair, contradicting \(D_2=D\). □

Thus in the closed-atomic class, the two pre-nuclei have the **same fixed points**, not necessarily the same value at each individual stage. In particular, **Q′** holds, and the rank-one **Q** implication holds under its specified finite-fixed premise \(\Phi_2(z_1)=z_1\). We do **not** assert the unconditional one-step identity \(\Phi=\Phi_2\).

## 4. Adversarial checks and limitations

1. **Closed quotient bottom:** In \(M'=\uparrow m_C\), the bottom is \(m_C\), not original \(0_M\); \(q(t)=t\vee m_C\) is a frame quotient preserving finite meets and arbitrary joins.
2. **Kernel support:** The zero kernel of any frame map is principal, generated by \(e_h\). Thus restriction to \([e_h,1]\) is legitimate even for nonspatial \(M\).
3. **Partition:** The two cases for \(a\wedge(c\vee e)\) are exhaustive because \(a\) is an atom. The first part \(C_1\) is nonempty because \(C\) covers, and \(u,v\) are genuine elements of \(L\).
4. **Infinite joins:** The final contradiction uses \(h(a)\wedge\bigvee_{C_1}k(c)=\bigvee_{C_1}(h(a)\wedge k(c))\), which holds in every frame.
5. **No pointwise substitution:** Equality \(D_2=D\) is justified by the universal property across all frame targets, not by an ordinary point-set argument.
6. **Not necessary:** Compact atomless spatial frames still satisfy \(D_2=D\), because every cover has a finite subcover; they need not be closed-atomic.
7. **Existing weak defects:** Any Scott or Arrieta weak finite/full defect must satisfy the **atomless normalized coordinate-support** obstruction. This is a test of candidate defects, not a claim that their source frames have no atoms.
8. **Rank-one caution:** The fixed-point lemma addresses Q under its premise; it does not assert \(\Phi(z_1)=z_1\) when \(\Phi_2(z_1)\neq z_1\).

**AUDIT STATUS (updated 14 November):** Original algebraic proof internally checked and independently blind-refereed (no error found); the converse spatial/scattered characterization above was supplied by that referee and checked internally. Literature originality has not been assessed. Universal Q and Q′ remain OPEN. See [reconciliation](ProjectA_Q_DENSITY_EXTERNAL_REFEREE_RECONCILIATION_AND_NEXT_STEPS_2026-11-14.md).
