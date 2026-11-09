# Project A — Noncompact interface gluing stress test for Q′

**8 November 2026 — internally checked working note; no external audit or novelty claim.** Q′ asks whether W=cl(D) always equals W2=cl(D2). Neither Q′ nor Q is settled here.

## 1. A compact-complement obstruction on a disjoint rectangle

Let L be a frame, Q=L⊕L, D=fit Δ, D2=finite-cover fitted diagonal, and let a,b∈L with a∧b=0. Assume the closed sublocale C(a∨b) is compact.

**Theorem.** In the open rectangle O(a⊠b), D and D2 agree:
\[
 D\wedge O(a\boxtimes b)=D_2\wedge O(a\boxtimes b).
\]
Their relative closures therefore agree there as well:
\[
 W\wedge O(a\boxtimes b)=W_2\wedge O(a\boxtimes b).
\]

**Proof.** For any cover C of 1, compactness of C(a∨b) supplies a finite F⊆C with a∨b∨∨F=1. The finite cover E={a,b}∪F has square neighborhood w_E=a⊠a∨b⊠b∨w_F. Putting r=a⊠b, disjointness gives r∧w_E=r∧w_F. Since D2≤O(w_E), it follows that D2∧O(r)≤O(w_F)≤O(w_C). This is valid for every cover C, so D2∧O(r)≤D. The reverse inclusion is automatic. Closure commutes with restriction to an open sublocale, giving the second assertion. □

**Corollary.** For an exact Q′ witness r=a⊠b with a∧b=0, r not≤d_W2 and r∧w_C≤d_W2, the closed complement C(a∨b) must be noncompact. In particular a gluing of two disjoint open sheets across a **single closed boundary point** cannot produce Q′ failure on the rectangle between the sheets.

## 2. Countably infinite boundary gluing

Let S=P(N)\{∅} with its standard Scott topology. For nonempty finite F⊆N put c_F={T∈S:F⊆T}; write c_n=c_{ {n} }. These compact opens form a basis and {c_n:n∈N} covers S. Each nonempty Scott open contains the greatest point N∈S.

Take disjoint copies A and B of S, and a countably infinite set of new points T={t_n:n∈N}. Set X=A⊔B⊔T. Declare a basis consisting of c_F^A, c_F^B, and
\[
N_n=\{t_n\}\cup c_n^A\cup c_n^B\qquad (n\in\mathbb N).
\]
This is a basis: intersections within either sheet are standard c_{F∪G}; N_n∩c_F^A=c_{F∪{n}}^A (similarly in B); for n≠m,
\[
N_n\cap N_m=c_{\{n,m\}}^A\cup c_{\{n,m\}}^B.
\]
All other intersections are empty or obvious. Both A and B are disjoint open subspaces. The closed remainder T=X\(A∪B) is infinite discrete: N_n∩T={t_n}. Thus its corresponding closed sublocale C(A∨B) is **noncompact**, so the compact-complement theorem does not exclude a witness on A⊠B.

Each c_F in its sheet is compact open, and N_n is the **least** neighborhood of t_n and hence compact open. The frame O(X) is algebraic, though X need not be sober (this is irrelevant to the localic calculation).

## 3. An infinite-cover failure with disjoint Boolean support

Let M=RO(2^N), a complete atomless Boolean frame. For each n let A_n={z:z_n=0} and B_n={z:z_n=1}, complementary clopen cylinders. There are established frame homomorphisms h0,k0:O(S)→M with h0(c_n)=A_n, k0(c_n)=B_n (see A-W-equals-U-infinite-cover-Boolean-witness-2026-10-24.md).

Restricting opens of X to the two sheets gives frame maps
\[
h(U)=h_0(U\cap A),\qquad k(U)=k_0(U\cap B)
\]
to M. If U1,…,Um is a finite cover of X, every t_n belongs to some U_{j(n)}, hence N_n⊆U_{j(n)}. By the infinite pigeonhole principle, one member U_j contains N_n for infinitely many n. Since the joins over any infinite set of coordinate cylinders A_n and B_n are both 1_M,
\[
h(U_j)=k(U_j)=1_M.
\]
Thus h,k are finite-cover compatible.

But the countable cover C={N_n:n∈N} covers X, whereas
\[
\bigvee_n h(N_n)\wedge k(N_n)
=\bigvee_n A_n\wedge B_n=0.
\]
Hence D2≠D. Moreover, with the disjoint opens a=A,b=B, we have h(a)=1_M and k(b)=1_M, so the difference is detected by a genuinely disjointly supported Boolean-valued map.

The cover C has maximal failure of rather-below localization:
\[
t_C=\bigvee_{F\subseteq C\ \text{finite}}\bigvee\{v:v\prec\bigvee F\}=0.
\]
Indeed, every nonempty open U⊆X meets each N_n (since any nonempty sheet-open contains the greatest point of that sheet, and each N_n contains both greatest points). Thus every t_n lies in cl(U). But the union of finitely many N_n omits all other t_m, so no nonzero v can have its closure contained in that union; hence no nonzero v is rather below it.

Thus this example escapes BOTH the compact-remainder and the cover-dependent regular-refinement obstructions, yet carries the desired infinitary Boolean witness.

## 4. Why W=W2=U nevertheless

Let x_A and x_B denote the greatest points N in the two copies of S. Every nonempty open of X contains at least one of these two points. Moreover, for every open cover of X, some member contains t_1 and therefore its least neighborhood N_1, containing **both** x_A and x_B.

Consequently all four pairs
\[
(x_A,x_A),\quad(x_A,x_B),\quad(x_B,x_A),\quad(x_B,x_B)
\]
are *full-cover-compatible points*, hence belong to D as points of the localic square. Every nonzero basic rectangle in Q contains one of these four point pairs. Rectangles join-generate Q, so D is dense in Q, and
\[
\boxed{W=W_2=U=X\times_{\mathrm{Loc}}X.}
\]
Indeed the equality for U also follows because every nonempty open has every t_n in its closure; thus no nonzero pair of opens is far, and d_U=0.

The example is not hyperconnected: A and B themselves are disjoint nonempty opens. Thus the failure is not simply that X is hyperconnected. Rather, its **two dense sheet-maxima are pairwise full-cover-compatible**, making D dense in the localic square.

## 5. Research interpretation

The exact Q′ witness requires (i) noncompact closed complement of its two disjoint opens, (ii) failure of rather-below finite localization for the offending cover, and (iii) an infinitary finite-cover-compatible Boolean defect. The construction achieves **all three**, but D remains dense because of a small family of actual full-cover-compatible point pairs. Noncompactness and Boolean defects alone are therefore not close to sufficient.

The remaining obstruction is to prevent these full-cover-compatible pairs from being dense **without** losing the finite-cover-compatible generalized Boolean pairs. A next construction should not simply add more boundary points with shared least neighborhoods: those restore the same pointwise density. No new separation relation or reformulated conjecture is being introduced.
