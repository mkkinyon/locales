# Project A / Q′ — Stone-space Baire diagnostic for Boolean fitting defects

**13 November 2026 — bounded intrinsic density investigation; internally checked, NOT externally audited.** This returns from Cohen × filtered-apex positive controls to the user's point-free category formulation: for each full cover C, \(D_2(X)\wedge C_{X^2}(w_C)\) should be nowhere dense in D₂(X) (equivalently Q′ on X). The result here is an EXACT classical Stone-space description of any Boolean fitting defect, followed by a NEGATIVE test: ordinary Baire category of the Stone representation alone cannot distinguish weak nowhere-dense defects from genuine Q′ open holes. Q/Q′ remain open.

## 0. Standing definitions

For locale X and frame L=O(X), each cover \(\mathscr C\) has square open \(w_{\mathscr C}=\bigvee_{c\in\mathscr C}c\boxtimes c\in O(X^2)\). The fitted diagonals D,D₂ use all/finite covers, respectively; W=cl D and W₂=cl D₂.

A **Boolean weak defect for C** is a nonzero complete Boolean algebra M with frame homomorphisms h,k:L→M satisfying
\[
\bigvee_{u\in F}h(u)\wedge k(u)=1_M
\quad\text{for every finite X-cover F},\tag{0.1}
\]
but
\[
\bigvee_{c\in C}h(c)\wedge k(c)=0_M.\tag{0.2}
\]
Any D₂>D failure admits such a defect by passing to the Booleanization of the nonzero closed C-zero quotient of D₂. A **strong Q′ hole** supplies such a pair specially as \(M=O(B(E_C))\) for a nonzero **relatively OPEN** E_C⊆W₂, with B(E_C)≤D₂ dense in E_C. The distinction is essential.

Let S=Stone(M), the compact Hausdorff extremally disconnected Stone space of the Boolean algebra M. For m∈M write \([m]=\{\eta\in S:m\in\eta\}\), a clopen.

## 1. The Stone split-incidence theorem

**Proposition 1.1.** Suppose C={c_n:n∈ω} is a **countable** X-cover, with h,k as (0.1)–(0.2). Let
\[
H_N=\bigcup_{n\ge N}[h(c_n)],\qquad
K_N=\bigcup_{n\ge N}[k(c_n)].
\]
Then each H_N and K_N is a DENSE OPEN subset of S. Consequently
\[
\boxed{\Omega=\bigcap_{N<\omega}(H_N\cap K_N)}
\tag{1.1}
\]
is a dense Gδ subset of S. For every ultrafilter \(\eta\in\Omega\), the two sets
\[
I_h(\eta)=\{n:h(c_n)\in\eta\},\qquad
I_k(\eta)=\{n:k(c_n)\in\eta\}
\]
are **disjoint and infinite**.

*Proof.* Equation (0.2) forces h(c_n)∧k(c_n)=0 for each n, so the two index sets are disjoint for EVERY η. Put \(v_N=\bigvee_{n\ge N}c_n\). The finite family \(\{c_0,\ldots,c_{N-1},v_N\}\) covers X. Every individual initial c_n matching value is zero, so (0.1) gives \(h(v_N)\wedge k(v_N)=1\), hence \(h(v_N)=k(v_N)=1\). Frame homomorphisms preserve the tail joins, giving
\[
\bigvee_{n\ge N}h(c_n)=\bigvee_{n\ge N}k(c_n)=1.
\]
For any family \(m_i\) in M, \(\bigvee m_i=1\) implies the union of Stone clopens [m_i] is **dense** (it may fail to be all S: Stone ultrafilter evaluation does not preserve infinite joins). Therefore H_N,K_N are dense open. Compact Hausdorff S is Baire, so Ω is dense Gδ, and membership in every tail union means both index sets are infinite. □

This is a category theorem about the **Stone space of the Boolean TARGET**, not a proof of category in D₂ or W₂.

## 2. Both Stone coordinates must be ghost points on T₁ locales

For any ultrafilter η∈S, evaluate the Boolean elements at η:
\[
h_\eta(a)=\mathbf1_{[h(a)]}(\eta),\quad
k_\eta(a)=\mathbf1_{[k(a)]}(\eta).
\]
These are bounded distributive-LATTICE maps L_lat→2; they preserve **finite** joins/meets but need not preserve arbitrary joins and hence need not be locale points of X.

**Proposition 2.1 (double-ghost obstruction).** Suppose x is an ordinary point of X whose point closure \(\overline{\{x\}}\) is compact. Under (0.1)–(0.2), **no** Stone ultrafilter η can have h_η equal to the ordinary point evaluation at x. The same statement holds for k_η. In particular, if X is a spatial T₁ locale, for every η∈S,
\[
\boxed{h_\eta\text{ and }k_\eta\text{ are BOTH non-completely-prime lattice filters}.}\tag{2.1}
\]

*Proof.* Let J=cl{x} be compact closed, and suppose h_η is the locale point x. Because C covers J, choose a finite F⊂C with \(J\subseteq\bigvee F\) as a sublocale. Write \(a\in L\) for the open complement of J. Then \(\{a\}\cup F\) is a finite X-cover, and h_η(a)=0 since x∈J. Apply the finite-cover matching identity (0.1) and evaluate at η, which is legitimate for **finite** Boolean joins/meets. It forces some c∈F with h(c),k(c)∈η. This contradicts (0.2), which makes every h(c)∧k(c)=0. The proof for k is symmetric. In T₁, each point closure is a compact singleton. □

The proof does NOT claim the maps h_η,k_η are frame maps. On the contrary, (2.1) shows why one cannot replace the Boolean locale Loc(M) by its spatial Stone spectrum and then invoke ordinary-point rigidity. The natural inclusion of clopens M into O(S) fails to preserve arbitrary joins: it takes the Boolean supremum to the **closure** of the union, not necessarily to the union.

## 3. Why this does NOT establish Q′

Both Propositions 1.1 and 2.1 hold for **any weak** D₂>D Boolean defect, whether or not a genuine OPEN W₂-hole exists.

The completed branching algebraic Scott domain \(S_0\) in the [frontier note](ProjectA_Qprime_FRONTIER_ONE_SIDED_RIGIDITY_EXIT_TREE_STOP_2026-11-12.md) is an explicit negative control: its two opposite Cantor regularization maps h₊,h₋ to RO(2^ω) satisfy finite-cover matching and fail the infinite singleton-literal cover. Their Stone spectra exhibit precisely the split-generic behavior above (indeed opposite literal labels at each coordinate). Yet
\[
\boxed{D_2(S_0)>D(S_0),\qquad W_2(S_0)=W(S_0)=S_0^2.}
\]
Thus the Boolean witness occupies only an **intrinsically nowhere-dense** portion of D₂; it is NOT the dense Booleanization of a nonzero W₂-open hole.

A strong Q′ hole has the extra inclusion/relative-openness datum
\[
B(E_C)\le D_2(X)\wedge E_C,
\quad
0\ne E_C\text{ OPEN inside }W_2(X),
\quad
E_C\wedge D(X)=0.
\]
This is not visible in the pointwise Stone combinatorics of h(c),k(c) alone. One must retain the location of this Boolean sublocale **inside the localic closed hull W₂**. Stone compactness/Baire category produces generic **ghost** pairs, not genuine X-points or a contradiction.

## 4. What the intrinsic programme should now ask

The explicit missing intermediate statement is a **relative-density/synchronization principle**: given a nonzero *open chart* E in W₂ and its dense canonical Boolean part B(E)≤D₂, show that for every X-cover C, some common-cover match is nonzero on E. It is invalid without the OPEN-chart hypothesis (Scott control). In frames, with \(d=d_{W₂}\), this is equivalent to the familiar pure-rectangle test
\[
\boxed{
\forall a,b\in O(X),\ \forall C:\quad
\bigl[\forall c\in C:\ (a\wedge c)\boxtimes(b\wedge c)\le d\bigr]
\Rightarrow a\boxtimes b\le d.
}\tag{4.1}
\]
This is **equivalent to Q′**, not a newly proved inequality: rectangles generate O(X²), and it says each full-cover square is dense in W₂=C(d).

The proposed next effort should isolate a NONTAUTOLOGICAL sufficient form of this synchronization principle that is closed under known marked-hole support reduction, and explicitly stress-test it against (i) Arrieta's anti-Urysohn space (no ordinary-point density in W₂) and (ii) the Scott weak-defect control (no OPEN hull defect). We should not treat double-ghost phenomena, nowhere Boolean distributivity, infinite graph chromaticity, or Baire generic incidence by themselves as evidence for or against universal Q′.

**Status:** Propositions 1.1–2.1 are elementary internally checked deductions; the final implication (4.1) is the preexisting open Q′ problem. No universal Q/Q′ result claimed.
