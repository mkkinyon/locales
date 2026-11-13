# Project A — Cohen × Arrieta: one-bit witness, diagonal structure, and section rigidity

**13 November 2026. Consolidated mathematical note.**

**Provenance and status:** The strict full fitted-diagonal product inequality and general closed-graph theorem in the [canonical original proof](ProjectA_Q_COHEN_ARRIETA_FULL_D_PRODUCT_NEGATIVE_2026-11-13.md) passed an [independent blind external audit](project-a/audits/2026-11-13/cohen-arrieta-fullD/EXTERNAL_REFEREE_REPORT_ORIGINAL.md), with a one-line regular-open containment repair incorporated there. The **one-bit witness** originated in the referee's [further suggestions](project-a/audits/2026-11-13/cohen-arrieta-fullD/EXTERNAL_REFEREE_FURTHER_SUGGESTIONS_ORIGINAL.txt). The strict \(\Delta\vee B\) inequality, strengthened weak-subfit binary rigidity, and countable-cover reduction below are **internally reconstructed and checked**, not independently blind-refereed. The detailed [reconciliation](ProjectA_Q_COHEN_ARRIETA_EXTERNAL_REFEREE_RECONCILIATION_AND_IDEAS_2026-11-13.md) retains the adopted/rejected idea inventory.

## 1. Setting and the regularized trace map

Let \(C=2^\omega\) be Cantor space and
\[
 K_n=\{x\in C:x_n=1,\ x_j=0\text{ for every }j>n\},
 \qquad
 Y=C\setminus\bigcup_{n\in\omega}K_n.
\]
Let \(A=Y\sqcup\omega\) have Arrieta's topology: a neighborhood of the attached point \(n\) contains \((V\cap Y)\cup\{n\}\) for a Cantor-open \(V\supseteq K_n\). Arrieta proves that \(A\) is strongly Hausdorff, so \(\Delta_A\subseteq A^2\) is a **closed sublocale**. Each nonempty Cantor cylinder meets \(K_n\) for every sufficiently large \(n\).

Write
\[
 r:\mathcal O(A)\to RO(C),\qquad
 r(u)=\operatorname{int}_C\operatorname{cl}_C(u\cap Y).
\]
This is a frame homomorphism **with regular-open joins**. Indeed restriction to \(\mathcal O(Y)\) is a frame map; since \(Y\) is dense in \(C\), regularization of a Cantor-open representative depends only on its \(Y\)-trace; this is the double-negation quotient.

For a cover \(\mathscr C\) of \(A\), set \(w_{\mathscr C}=\bigvee_{u\in\mathscr C}u\boxtimes u\in\mathcal O(A^2)\). The full fitted diagonal is
\[
 D(A)=\bigwedge_{\mathscr C\text{ cover}}O(w_{\mathscr C}).
\]
Thus two maps \(h,k:\mathcal O(A)\to M\) into a frame \(M\) yield a pair factoring through \(D(A)\) iff \(\bigvee_{u\in\mathscr C}h(u)\wedge k(u)=1_M\) for **every** cover \(\mathscr C\).

## 2. One-bit-flip lemma: full compatibility with zero equalizer

Let \(\tau:C\to C\) flip only bit \(0\). Put
\[
 M_0=RO(C),\qquad
 h_1(u)=r(u),\qquad k_1(u)=\tau^{-1}(r(u)).
\]
These are frame maps, corresponding to \(f_1,g_1:Z_C=\operatorname{Loc}(M_0)\to A\).

**Lemma 2.1.** The pair \((f_1,g_1)\) factors through **full** \(D(A)\), but its localic equalizer is zero.

**Proof — cover compatibility.** For all \(n\ge1\), \(\tau(K_n)=K_n\). Fix any \(A\)-cover \(\mathscr C\) and any nonempty Cantor cylinder \(R\). Choose \(n\ge1\) large with \(K_n\cap R\ne\varnothing\), and choose \(u\in\mathscr C\) containing the attached point \(n\). There is a Cantor-open \(V\supseteq K_n\) with \(V\cap Y\subseteq u\cap Y\). Because \(Y\) is dense,
\[
 V\subseteq\operatorname{int}\operatorname{cl}(u\cap Y)=r(u).
\]
If \(p\in K_n\cap R\), then \(p,\tau(p)\in V\), so the nonempty open set \(R\cap r(u)\cap\tau^{-1}r(u)\) contains \(p\). Every nonempty cylinder thus meets some matching open. Its join is \(1\) in \(RO(C)\), for **arbitrary** covers.

**Proof — equalizer.** Let \(a_0=(Y\cap[x_0=1])\cup\{0\}\), which is \(A\)-open. Then \(h_1(a_0)=[x_0=1]\), \(k_1(a_0)=[x_0=0]\), complementary clopens of \(C\). In the Boolean locale \(Z_C\), any equalizing sublocale must have zero Boolean support, so \(\operatorname{eq}(f_1,g_1)=0\). □

**Corollary 2.2.** By Arrieta's closed diagonal and the externally checked graph-cover theorem,
\[
 D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A)
\]
is already witnessed by **one Cohen generic bit-sequence and its one-bit flip**. This is an alternative proof of the externally reviewed inequality, not a new external audit of the simplification. The historical **all-bit flip** pair remains only finite-cover compatible; it does not contradict Lemma 2.1.

## 3. The independent-coordinate Booleanization and a strict new inclusion

Let \(P=C\times C\) and \(M=RO(P)\). The frame map
\[
 q:\mathcal O(A^2)\longrightarrow M,
 \quad
 q(u\boxtimes v)=\bigl(r(u)\times C\bigr)\wedge\bigl(C\times r(v)\bigr)
                =r(u)\times r(v)
\]
is **surjective**: clopen Cantor rectangles are in its image and join-generate \(RO(P)\). It is **dense**: every nonzero \(A^2\)-open contains a nonzero rectangle \(u\boxtimes v\), and every nonzero \(A\)-open meets dense \(Y\); hence \(q(u\boxtimes v)\ne0\). A dense surjective frame map onto a Boolean frame identifies that target with the double-negation quotient. Thus
\[
 \operatorname{Loc}(RO(C^2))\ \cong\ B(A^2).
\]
The independent-coordinate all-cover argument of the externally checked theorem therefore gives
\[
 \boxed{B(A^2)\le D(A).}
\]
In particular \(D(A)\) and \(D_2(A)\) are dense in \(A^2\):
\[
 \boxed{W(A)=W_2(A)=A^2, \qquad W=\operatorname{cl}D,\quad W_2=\operatorname{cl}D_2.}
\]

**Proposition 3.1 (new internal consequence).**
\[
 \boxed{\Delta_A\vee B(A^2)\subsetneq D(A).}
\]

**Proof.** The one-bit pair in §2 induces a surjective frame map
\(t^*:\mathcal O(A^2)\to RO(C)\): the values of the first coordinate on \(Y\cap R\), for clopen Cantor cylinders \(R\), generate \(RO(C)\). Hence \(t:Z_C\to A^2\) is a **sublocale embedding** with nonzero image \(S\). Lemma 2.1 gives \(S\le D(A)\) and \(S\wedge\Delta_A=0\).

Let \(\Gamma_\tau=\{(x,\tau x):x\in C\}\subseteq C^2\), a nowhere-dense closed graph. In \(\mathcal O(A^2)\), form
\[
 w=\bigvee_{\substack{R,S'\text{ clopen cylinders}\\
              (R\times S')\cap\Gamma_\tau=\varnothing}}
          (R\cap Y)\boxtimes(S'\cap Y).
\]
By construction \(t^*(w)=0\), so \(S\le C(w)\). But the regular-open join of the rectangles \(R\times S'\) in the displayed family is \(1_{RO(C^2)}\), since their union is \(C^2\setminus\Gamma_\tau\), dense. Thus \(q(w)=1\), giving \(B(A^2)\le O(w)\). Therefore \(S\wedge B(A^2)=0\). Finite distributivity of the sublocale lattice implies
\[
  S\wedge(\Delta_A\vee B(A^2))=0.
\]
As \(S\ne0\) and \(S\le D(A)\), the inclusion is strict. □

**Meaning:** The full fitted diagonal of Arrieta's locale contains nonzero non-diagonal sublocales **outside** the Booleanization of its whole square. This is stronger than the mere non-F-separatedness \(D(A)>\Delta_A\).

## 4. Binary section rigidity over weakly subfit bases

Recall that a locale \(Z\) is **weakly subfit** if for every nonzero \(v\in\mathcal O(Z)\), there is \(a<1_Z\) with \(a\vee v=1_Z\). Boolean and subfit locales are weakly subfit.

**Theorem 4.1 (new internally checked generalization).** Let \(Y\) be strongly Hausdorff and \(Z\) weakly subfit. For \(f,g:Z\to Y\), put \(s_f=(1_Z,f)\), \(s_g=(1_Z,g)\). Then
\[
 (s_f,s_g)\text{ factors through }D_2(Z\times Y)
       \quad\Longleftrightarrow\quad f=g.
\]
When \(f\ne g\), a **two-member product cover** suffices.

**Proof.** The equalizer \(E=\operatorname{eq}(f,g)\) is closed in \(Z\), say \(E=C_Z(v)\), because the diagonal of \(Y\) is closed. If \(f\ne g\), then \(v\ne0\), and weak subfitness supplies \(a<1_Z\) with \(a\vee v=1_Z\), equivalently \(E\le O_Z(a)\).

Let \(u_f,u_g\) be the open complements of the two closed graphs \(\Gamma_f,\Gamma_g\subseteq Z\times Y\). Their intersection \(\Gamma_f\wedge\Gamma_g\) is the graph of \(E\), hence lies in the open \(a\boxtimes1\). Consequently
\[
  \mathscr F=\bigl\{\,u_f\vee(a\boxtimes1),\quad u_g\,\bigr\}
\]
is an **open cover of \(Z\times Y\)**. Since \(s_f^*(u_f)=0\), \(s_g^*(u_g)=0\), and both sections pull \(a\boxtimes1\) back to \(a\), the finite-cover matching value is
\[
 \bigl(s_f^*(u_f\vee(a\boxtimes1))\wedge
       s_g^*(u_f\vee(a\boxtimes1))\bigr)
 \ \vee\
 \bigl(s_f^*(u_g)\wedge s_g^*(u_g)\bigr)
 =a<1.
\]
Thus the pair lies outside \(D_2(Z\times Y)\). The case \(f=g\) is the diagonal. □

For Boolean \(Z\), one may take \(a\) to be the clopen support of \(E\); the cover's matching value is exactly that support. The result is about **sections with common identity base map**, not an equality of entire sublocales of \((Z\times Y)^2\).

## 5. Countable-cover reduction for Cohen × Arrieta

**Lemma 5.1.** If \(\mathcal O(Z)\) is a ccc complete Boolean algebra and \(X\) has a countable frame basis, then \(Z\times X\) is a Lindelöf locale: every open cover has a countable subcover.

**Proof.** In a ccc complete Boolean algebra, any join \(\bigvee_{i\in I}b_i\) has a **countable subfamily with the same join**: take a maximal antichain of nonzero pieces below the \(b_i\), which must be countable. Refine the given product cover to basic rectangles \(b\boxtimes u\), and express each \(u\) as a join of elements of a fixed countable basis \(u_n\). Group all resulting rectangles according to \(n\). For each \(n\), select countably many Boolean coefficients whose join equals the original coefficient. The union of these choices over countably many \(n\) is countable and has the same join as the original rectangle cover. Selecting their parent cover members yields a countable subcover. □

For \(Z_C=\operatorname{Loc}(RO(C))\), the frame is ccc because \(C\) is second countable, and Arrieta's \(A\) is second countable because the \(K_n\) are finite and \(C\) has a countable clopen basis. Hence \(Z_C\times A\) is Lindelöf. The **full** fitted diagonal \(D(Z_C\times A)\) can therefore be tested using **countable** covers. This is a reduction of cover size, not a claim that \(D_2(Z_C\times A)\ne D(Z_C\times A)\).

## 6. Exact Q′ restart status

**Q′ (universally open):** Is
\[
  W_2(X)=W(X)
\]
for every locale \(X\)? Equivalently, does \(B(D_2(X))\le D(X)\) always hold? For each cover \(\mathscr C\), its weak defect
\[
  T_{\mathscr C}
   =D_2(X)\wedge C_{X^2}(w_{\mathscr C})
\]
may be nonzero without refuting Q′. The question is whether it can have **nonzero relative interior in \(D_2(X)\)**.

On Arrieta's \(A\), the all-bit-flip pair witnesses \(D_2(A)\ne D(A)\) via a countable cover, but §3 shows \(W_2(A)=W(A)=A^2\); the defect is necessarily nowhere dense in \(D_2(A)\). On \(Z_C\times A\), the full product failure uses a pair already **outside** the product \(D_2\), so it is likewise not a Q′ counterexample. The distinct universal question Q remains open as well.

**Research next:** Return to relative-density/relative-open tests **inside \(D_2(X)\)**. The two-apex and Cohen × Arrieta programmes supply verified positive controls and nonclosed obstructions, but as yet **no relatively open weak defect**. Do not promote the new internal corollaries above to an external certificate without a fresh audit.
