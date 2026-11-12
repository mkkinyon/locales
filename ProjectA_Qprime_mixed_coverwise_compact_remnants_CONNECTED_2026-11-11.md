# Project A — Q′: mixed rather-below/hyperconnected compact-remnant theorem and connected test

**11 November 2026. NEW INTERNAL working mathematics, NOT independently externally audited.** Bounded positive-class test requested on returning to the original noncoherent separation hierarchy. This note refines the [coverwise compact-remainder theorem](ProjectA_W2_coverwise_compact_remainder_and_local_atomic_obstruction_2026-11-11.md) and combines it with the earlier hyperconnected-strip equality, while keeping \(Q'\) and \(Q\) **OPEN**. The topology in §3 is a **connected, second-countable, sober, noncompact, nonregular** test showing that the combined criterion can hold even when neither ingredient alone has compact remainder, and even though \(\mathcal D_2>\mathcal D\). No novelty/priority claim.

## 0. Setup and imported facts

Let \(L=\mathcal O(X)\), \(Q=L\oplus L\); for a cover \(\mathcal C\) put \(w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c\). Write
\[
\mathcal D=\bigwedge_{\mathcal C}\mathfrak o(w_{\mathcal C}),\qquad
\mathcal D_2=\bigwedge_{\mathcal F\ \mathrm{finite\ cover}}\mathfrak o(w_{\mathcal F}),
\quad \mathcal W=\operatorname{cl}\mathcal D,\quad
\mathcal W_2=\operatorname{cl}\mathcal D_2=C(d_0).
\]
The finite-cover pre-nucleus \(\Phi_2(z)=\bigvee_{\mathcal F\ \mathrm{finite\ cover}}(w_{\mathcal F}\to z)\) satisfies \(\Phi_2(d_0)=d_0\). The full \(\Phi\)-closure of \(d_0\) yields \(d_{\mathcal W}\). In particular a \(Q'\) failure gives a cover \(\mathcal C\) and pure rectangle \(r=a\boxtimes b\) with
\[
r\not\le d_0,\quad r\wedge w_{\mathcal C}\le d_0,\quad
r\le\Phi(d_0)\le d_{\mathcal W}.
\tag{0.1}
\]
Such a cover has no finite subcover and a∧b=0 by the earlier exact disjoint-rectangle certificate; these two extras are not needed for the main proof.

For every cover define the **rather-below patch**
\[
t_{\mathcal C}=
\bigvee_{\substack{F\subseteq\mathcal C\\F\ \mathrm{finite}}}
\bigvee\{v\in L:v\prec\bigvee F\},\qquad v\prec u\iff v^*\vee u=1.
\tag{0.2}
\]
The previously reviewed *localized residual inequality* says
\[
r\wedge(t_{\mathcal C}\boxtimes1)\le d_0,\qquad
r\wedge(1\boxtimes t_{\mathcal C})\le d_0
\tag{0.3}
\]
for any r as in (0.1).

An open \(e\in L\) will be called **hull-sound on coordinate strips** if
\[
\boxed{
\mathcal W_2\wedge\mathfrak o(e\boxtimes1\vee1\boxtimes e)
=
\mathcal W\wedge\mathfrak o(e\boxtimes1\vee1\boxtimes e).
}
\tag{0.4}
\]
The earlier hyperconnected-strip theorem supplies such an e: the join \(h_{\rm hc}\) of all nonzero hyperconnected open sublocales. The compact-closed-neighborhood strip theorem supplies another (where stronger \(\mathcal D_2=\mathcal D\) holds). We do not silently promote these older theorem inputs to a fresh independent audit.

## 1. Mixed positive theorem

**Theorem 1.1 (coverwise compact remainder modulo sound strips).**
Fix a hull-sound open \(e\). Suppose that for every open cover \(\mathcal C\) of X, the closed sublocale
\[
\boxed{K_{\mathcal C}=\mathfrak c(t_{\mathcal C}\vee e)}
\tag{1.1}
\]
is compact. Then
\[
\boxed{\mathcal W=\mathcal W_2.}
\tag{1.2}
\]
It actually suffices, for every cover \(\mathcal C\), that there be some finite \(F_0\subseteq\mathcal C\) with
\[
t_{\mathcal C}\vee e\vee\bigvee F_0=1.
\tag{1.3}
\]

*Proof.* Suppose \(\mathcal W<\mathcal W_2\), and choose \(r,\mathcal C\) as in (0.1). Since \(r\le d_{\mathcal W}\), the open sublocale \(\mathfrak o(r)\) is disjoint from \(\mathcal W\). Equality (0.4) then gives
\[
\mathcal W_2\wedge\mathfrak o(r)\wedge
\mathfrak o(e\boxtimes1\vee1\boxtimes e)=0.
\]
Since \(\mathcal W_2=C(d_0)\), the criterion for a relatively open intersection with a closed sublocale to vanish is that its defining open be ≤d_0. Hence
\[
r\wedge(e\boxtimes1\vee1\boxtimes e)\le d_0.
\tag{1.4}
\]
Combining (1.4) and (0.3), and setting \(\ell=t_{\mathcal C}\vee e\), gives
\[
r\wedge(\ell\boxtimes1\vee1\boxtimes\ell)\le d_0,
\quad\text{in particular}\quad
r\wedge(\ell\boxtimes\ell)\le d_0.
\tag{1.5}
\]
By compactness of \(K_{\mathcal C}=C(\ell)\), the restriction of \(\mathcal C\) to \(K_{\mathcal C}\) has a finite subcover F_0. Equivalently \(\ell\vee\bigvee F_0=1\), so \(\{\ell\}\cup F_0\) is a **finite** cover of X. By (1.5) and \(r\wedge w_{\mathcal C}\le d_0\),
\[
r\wedge w_{\{\ell\}\cup F_0}
=r\wedge\big((\ell\boxtimes\ell)\vee w_{F_0}\big)
\le d_0.
\]
Consequently
\[
r\le(w_{\{\ell\}\cup F_0}\to d_0)\le\Phi_2(d_0)=d_0,
\]
contradicting (0.1). This proves (1.2). The last calculation uses only the finite-subcover alternative (1.3), establishing the sharper formulation. QED.

**Corollary 1.2 (canonical usable version).** For any locale X, let \(h_{\rm hc}\) be the join of its hyperconnected opens. If
\[
\boxed{
\mathfrak c(t_{\mathcal C}\vee h_{\rm hc})
\ \text{is compact for every cover }\mathcal C,
}
\tag{1.6}
\]
then \(Q'\) holds for X. More generally one may take \(e=h_{\rm hc}\vee h_{\rm cc}\), where \(h_{\rm cc}\) is the earlier compact-closed-neighborhood strip open.

**Scope comparison.** This combines two previously **separate mechanisms**: cover-dependent finite-cover localization and open hyperconnected-strip *closed-hull* equality. It does **not** force \(\mathcal D=\mathcal D_2\); §3 explicitly refutes that strengthening. It includes the previous coverwise compact-remnant theorem (e=0), and includes the fixed compact remainder theorem (if \(C(e)\) compact, then each \(C(t_{\mathcal C}\vee e)\) is a closed sublocale of compact \(C(e)\)). The combined criterion is not asserted necessary for Q′.

## 2. Additional refined obstruction

For a cover \(\mathcal C\) put \(\ell_{\mathcal C}=t_{\mathcal C}\vee e\) for any hull-sound e, and let
\[
J_{\mathcal C}^{e}
=
H_2\wedge\mathfrak c(p_1^*\ell_{\mathcal C})
\wedge\mathfrak c(p_2^*\ell_{\mathcal C}),
\quad
H_2=\mathcal W_2\wedge(\mathcal U\wedge\mathfrak o(d_{\mathcal U}^{**})).
\tag{2.1}
\]

**Proposition 2.1.** Any counterexample to Q′ supplies a cover \(\mathcal C\) without finite subcover and a nonzero relatively open
\[
E=\mathcal W_2\wedge\mathfrak o(r)\le J_{\mathcal C}^{e}
\]
with \(\mathcal D\wedge E=0\) and \(\mathcal D_2\wedge E\) dense in E. Thus, if **for every** cover C the Booleanization of \(J_{\mathcal C}^{e}\) is atomic (including zero), then Q′ holds.

*Proof.* The disjoint-rectangle certificate places E in H₂. Equations (0.3),(1.4) imply E is disjoint from both coordinate opens of \(\ell_{\mathcal C}\), hence lies in their closed complements. This gives \(E\le J_{\mathcal C}^e\) and, because \(E=\mathcal W_2\wedge\mathfrak o(r)\), E is relatively open there. The earlier residual argument gives \(\mathcal D\wedge E=0\) and density of \(\mathcal D_2\wedge E\). If \(B(J_{\mathcal C}^e)\) is atomic, then B(E) has a point, contained in D₂ by density and hence also in D by the established equality of their locale points, contradiction. QED.

The new J depends on the **same cover** and is smaller than the previous \(J_\mathcal C\), but no claim is made that this atomic criterion is equivalent to (1.6) or to the older atomic test on H₂.

## 3. A connected sober noncompact test with a real infinitary fitting defect

### 3.1 The two pieces and the boundary topology

Let \(Y=\ell^2\), a separable infinite-dimensional real Hilbert space with its norm topology. It is connected, regular, second countable, sober, and **nowhere locally compact**. Let
\[
S=\mathcal P(\mathbb N)\setminus\{\varnothing\}
\]
with the **Scott topology** under inclusion. Its basic opens are
\[
\uparrow F=\{A\in S:F\subseteq A\},
\quad F\subseteq\mathbb N\text{ finite nonempty}.
\]
Every nonempty Scott open contains the top element \(\mathbb N\), so S is hyperconnected. It is noncompact, covered by the \(\uparrow\{n\}\) with no finite subcover. It is second countable and sober (every irreducible Scott-closed subset is \(\downarrow A\) for a unique A, by the directed finite-subset argument). Its principal basic opens \(\uparrow F\) are compact, so S is locally compact, but not regular.

Take
\[
X=Y\ \sqcup\ S\ \sqcup\ \{p\}
\]
as a set. Declare Y and S to be **disjoint open subspaces** with their stated topologies, and give p the neighborhood basis
\[
N_{n,F}
=\{p\}\cup\{y\in Y:\|y\|>n\}\cup\uparrow F,
\qquad n\in\mathbb N,\quad \varnothing\ne F\subseteq\mathbb N\text{ finite}.
\tag{3.1}
\]
The intersection of two such neighborhoods contains and indeed equals \(N_{\max(n,m),F\cup G}\); intersections with Y- and S-opens are open, so (3.1) and the opens of Y and S define a topology.

### 3.2 Elementary topological checks

- **T₀ and second countable:** Y and S are T₀ with countable bases, and p has the countable neighborhood base (3.1). Y- or S-opens distinguish points of those pieces from p.
- **Connected:** \(p\in\overline Y\cap\overline S\), while \(\overline Y=Y\cup\{p\}\) and \(\overline S=S\cup\{p\}\). Both Y and S are connected, so both closures are connected; their union is X, with common point p.
- **Sober:** If an irreducible closed set F meets the open Y, its nonempty closed intersection with Y is irreducible in a Hausdorff space, hence a singleton {y}; it cannot meet S (disjoint opens), nor p (choose a bounded Y-neighborhood of y and an N_{n,F} with n larger than its norm). Thus F={y}. If F misses Y but meets S, its intersection with sober S is \(\downarrow A\) for a unique nonempty A⊆N. It may contain p only if A=N: if A≠N, choose i∉A and a p-neighborhood N_{n,{i}} disjoint from \(\downarrow A\), contradicting irreducibility. If A=N, closure of S forces p, and F=S∪{p}=\(\overline{\{\mathbb N\}}\). If F meets neither open piece it is {p}. Thus every nonempty irreducible closed set has a unique generic point.
- **Noncompact:** The closed subspace S∪{p} is not compact. Its open cover consisting of \(N_{1,\{0\}}\cap(S\cup\{p\})\) and \(\uparrow\{n\}\) for all n has no finite subcover, by singleton subsets \(\{m\}\) for m outside the finite index set and m≠0.
- **Nonregular and noncoherent:** The nonregular open Scott subspace S shows X is not regular; noncompactness implies its locale is not coherent.

The **hyperconnected-open union** of X is exactly
\[
h_{\rm hc}=S:
\]
S is hyperconnected; every nonempty open meeting Y contains two disjoint smaller nonzero Y-opens, hence cannot be hyperconnected, and every neighborhood of p meets Y.

In fact the earlier **compact-closed-neighborhood** open is \(h_{\rm cc}=0\). If a compact closed K in X contained any nonempty Y-open, it would contain a bounded closed Hilbert ball, which is a **noncompact closed subset of X**, contradiction. If K contained any nonempty S-open, then because S is hyperconnected and p lies in the closure of every nonempty S-open, it would contain the closed, noncompact subspace S∪{p}, again a contradiction. No nonempty open consists solely of p.

### 3.3 The mixed positive condition holds for *every cover*

Let \(\mathcal C\) be any cover of X. For each y∈Y choose c∈C containing y, and a small **bounded** metric ball e about y whose closed ball lies in c∩Y. This closed ball is also closed in X: a sufficiently large p-neighborhood N_{n,F} misses it, and S is open disjoint from it. Thus \(\operatorname{cl}_X(e)\subseteq c\), which in \(\mathcal O(X)\) says \(e^*\vee c=1\), i.e. \(e\prec c\). Consequently,
\[
Y\le t_{\mathcal C}
\quad\text{for every cover }\mathcal C.
\tag{3.2}
\]
Since \(h_{\rm hc}=S\), we have \(t_{\mathcal C}\vee h_{\rm hc}\supseteq Y\cup S=X\setminus\{p\}\), so
\[
\mathfrak c(t_{\mathcal C}\vee h_{\rm hc})\le\{p\}
\]
is a **compact closed sublocale** (zero or the singleton). Theorem 1.1 therefore gives
\[
\boxed{\mathcal W(X)=\mathcal W_2(X).}
\tag{3.3}
\]
No compactness of X or regularity of X was assumed.

### 3.4 There remains a genuine fitted-diagonal gap D<D₂

Use the compact Cantor space \(K=2^\mathbb N\) and complete Boolean frame \(B=\operatorname{RO}(K)\). For a Scott-open U⊆S define open sets of K
\[
\alpha_+(U)=
\bigcup_{\substack{F\subseteq\mathbb N\ \mathrm{finite\ nonempty}\\\uparrow F\subseteq U}}
\{z\in K:z(n)=1\text{ for all }n\in F\},
\]
\[
\alpha_-(U)=
\bigcup_{\substack{F\subseteq\mathbb N\ \mathrm{finite\ nonempty}\\\uparrow F\subseteq U}}
\{z\in K:z(n)=0\text{ for all }n\in F\}.
\tag{3.4}
\]
These preserve arbitrary joins and finite meets, as operations of opens: for joins, any finite F belongs to some member of a union cover of ↑F because that member contains the point F and is upward; for meets, cylinders with F and G intersect in the cylinder for F∪G. Their top images omit only the all-zero or all-one sequence, respectively, hence are **dense** in K. Composing with double-negation regularization \(j:\mathcal O(K)\to B\) produces frame maps
\[
h_+,h_-:\mathcal O(S)\to B,\qquad h_\pm(U)=j(\alpha_\pm(U)).
\tag{3.5}
\]
For any finite open cover \(U_1,\ldots,U_m\) of S, some U_i contains infinitely many singleton conditions {n}. Therefore α_+(U_i) contains infinitely many cylinders \([n=1]\) with dense union in K, and α_-(U_i) contains the opposite cylinders \([n=0]\), also with dense union. Thus \(h_+(U_i)=h_-(U_i)=1_B\), so the pair is compatible with every finite cover.

On the other hand the infinite cover \(\{\uparrow\{n\}:n\in\mathbb N\}\) of S gives
\[
h_+(\uparrow\{n\})=[n=1],\qquad
h_-(\uparrow\{n\})=[n=0],
\quad h_+(\uparrow\{n\})\wedge h_-(\uparrow\{n\})=0.
\tag{3.6}
\]
Hence \(\mathcal D_2(S)>\mathcal D(S)\).

Restrict opens of X to the **open sublocale S** and compose with h_±:
\[
H_\pm:\mathcal O(X)\xrightarrow{(-)|_S}\mathcal O(S)
\xrightarrow{h_\pm}B.
\tag{3.7}
\]
Every finite cover of X restricts to a finite cover of S, so (H_+,H_-) is finite-cover-compatible. However the genuine open cover
\[
\boxed{
\mathcal C^\star=\{Y,N_{1,\{0\}}\}\cup\{\uparrow\{n\}\subseteq S:n\in\mathbb N\}
}
\tag{3.8}
\]
is **not** fully compatible: \(H_\pm(Y)=0\), and each other member restricts to \(\uparrow\{0\}\) or \(\uparrow\{n\}\) on S, giving zero coordinate meet by (3.6). Therefore
\[
\boxed{\mathcal D(X)<\mathcal D_2(X)\quad\text{but}\quad
\mathcal W(X)=\mathcal W_2(X).}
\tag{3.9}
\]
The strict fitted-diagonal gap is witnessed by a genuinely **pointless Boolean-valued pair**, not by ordinary pairs of points.

### 3.5 Why the two older compact tests genuinely fail here

For the cover C* of (3.8), every finite subfamily has a proper restriction to S. Since S is hyperconnected, the pseudocomplement of **any nonzero S-open** is zero in \(\mathcal O(S)\). Therefore no open e meeting S (or containing p, since all p-neighborhoods meet S) can satisfy \(e\prec\bigvee F\) for a finite \(F\subseteq C^\star\). By (3.2),
\[
\boxed{t_{\mathcal C^\star}=Y.}
\tag{3.10}
\]
Its closed complement is S∪{p}, which is **noncompact**. Thus the previous coverwise theorem with e=0 does not apply. Meanwhile
\[
h_{\rm hc}=S,\qquad h_{\rm cc}=0,
\]
and the closed complement of \(h_{\rm hc}\vee h_{\rm cc}\) is \(Y\cup\{p\}\), also **noncompact**: a p-neighborhood removes only a bounded Hilbert ball; covering that ball requires infinitely many small metric balls (use the orthonormal basis). So the earlier **fixed** hyperconnected/compact-closed remainder criterion also does not apply.

The new mixed criterion combines the two:
\[
t_{\mathcal C}\vee h_{\rm hc}\supseteq X\setminus\{p\}
\quad\text{for every }\mathcal C,
\]
leaving the compact singleton {p}. This makes (3.9) a **connected, genuinely noncoherent control** in which the new condition has demonstrably more reach than either older compact-remnant hypothesis *alone*.

## 4. Audit notes and disposition

- **Proof dependencies:** (i) previously established \(\Phi_2(d_0)=d_0\), exact Q′ rectangular witness, and rather-below two-coordinate localization (independently checked in prior Q′ audit); (ii) the previously developed hyperconnected-strip equality \(W=W_2\) on \(h_{\rm hc}\)-strips (working result; its precise independent-audit history should be maintained, not silently upgraded); (iii) elementary topology of the space in §3.
- **New claims:** Theorem 1.1, its atomless \(J_{\mathcal C}^e\) refinement, and the connected example with an explicit strict \(\mathcal D<\mathcal D_2\) despite \(\mathcal W=\mathcal W_2\). All remain **INTERNAL**, even if foundational inputs have earlier review.
- **No overreach:** \(Q'\) and \(Q\) still OPEN in arbitrary frames. Neither local compactness nor countable basing alone gives \(t_{\mathcal C}\) a compact remainder: the Scott S in this example is second countable, sober, noncompact and locally compact, yet the basic singleton cover has \(t_{\mathcal C}=0\).
- **Why this does not solve Q′:** A hypothetical counterexample can have an infinitely noncompact cover-dependent remainder *outside* both the regular patches and the hyperconnected strips. The new theorem isolates that joint failure but does not eliminate it in every locale.
- **Next useful question:** whether an intrinsically described class of locales, beyond the constructed sufficient condition, forces all cover-dependent \(K_{\mathcal C}\) compact; or whether the canonical atomless pair on \(B(J_{\mathcal C}^{h_{\rm hc}})\) can be studied without multiplying forcing constructions.

**Status:** internally checked, not externally audited; no claim of publication novelty.
