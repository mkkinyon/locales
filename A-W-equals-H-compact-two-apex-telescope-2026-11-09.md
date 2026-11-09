# Project A — The compact two-apex locale has W = H < U < F

**9 November 2026. Internal working proof; no external audit or priority check.** We answer the targeted question left at the end of the preceding [relative-fitness note](A-W-equals-H-relative-fitness-functional-envelope-2026-11-09.md): is \(\mathcal W\) fitted in the compact two-apex \(T_1\) example? **Yes.** The proof is genuinely point-free, using a *two-sided shrinking argument* in a complete Boolean target. In particular, its W is fitted **without** being clopen or regularly generated in its functional envelope. Q/Q′ stay deferred.

## 1. The space and previously audited W/U calculation

Let \(X=\mathbb R\sqcup\{p,q\}\). The restriction to \(\mathbb R\) is the usual topology. Neighborhoods of p contain p and **all positive reals except finitely many**, and neighborhoods of q contain q and **all negative reals except finitely many**. Precisely, bases are
\[
N_p(F)=\{p\}\cup((0,\infty)\setminus F),\quad
N_q(G)=\{q\}\cup((-\infty,0)\setminus G),
\]
for finite \(F\subset(0,\infty)\), \(G\subset(-\infty,0)\). These sets are open because the finite punctures of the respective open real half-lines are open. This is the *cofinite-half-line*, **not tail**, interpretation. X is compact, locally compact, sober, T₁ and noncoherent. Its localic square is spatial and is the ordinary product.

Let
\[
u_+=(0,\infty)\cup\{p\},\quad
u_-=(-\infty,0)\cup\{q\}.
\]
These are disjoint opens. Their pseudocomplements in \(\mathcal O(X)\) are \(u_+^*=u_-\), \(u_-^*=u_+\), and \(u_+\vee u_-=X\setminus\{0\}\).

The October independent-review computation (confirmed again by the Nov 9 Q′ referee) is
\[
\mathcal W=K=A_+^2\cup A_-^2,\quad
A_+=[0,\infty)\cup\{p\},\quad
A_-=(-\infty,0]\cup\{q\},
\]
\[
\mathcal U=K\cup\{(p,q),(q,p)\}.
\]
Accordingly, for \(Q=\mathcal O(X\times X)\),
\[
\boxed{d_{\mathcal W}=(u_+\boxtimes u_-)\vee(u_-\boxtimes u_+).}\tag{1.1}
\]
We denote the disjoint open mixed sectors by \(T_{+-}=u_+\boxtimes u_-\), \(T_{-+}=u_-\boxtimes u_+\). Thus \(K=C(d_{\mathcal W})\). The two extra U points are relatively isolated in U but are **not** isolated in the square.

## 2. A vanishing pair of shrinking open sublocales

For n≥1 put
\[
a_n=(0,1/n)\subset X,\qquad b_n=(-1/n,0)\subset X.
\tag{2.1}
\]

**Lemma 2.1.** In the sublocale lattice of X,
\[
\boxed{\bigwedge_{n\ge1}O(a_n)=0
=\bigwedge_{n\ge1}O(b_n).}\tag{2.2}
\]

**Proof.** The closure of \(a_n\) in X is \([0,1/n]\cup\{p\}\): p lies in the closure of every infinite positive interval, and q does not. Therefore any sublocale S contained in every O(a_n) has its closure contained in every C(a_n*) and hence in the closed two-point sublocale \(\{0,p\}\). But \(O(a_1)\) meets \(\{0,p\}\) in zero, since a₁ excludes both points. Therefore S=0. The argument for b_n uses \([-1/n,0]\cup\{q\}\) and \(\{0,q\}\). This is an equality of sublocales, not just an empty intersection of their ordinary point sets. □

For a complete Boolean frame B, if \(h:\mathcal O(X)\to B\) is a frame map, define \(A_n=h(a_n)\). These form a decreasing sequence and satisfy
\[
\boxed{\bigwedge_n A_n=0_B.}\tag{2.3}
\]
Indeed, were \(t=\bigwedge_n A_n>0\), the composite \(h_t:\mathcal O(X)\to\downarrow t\), \(h_t(v)=h(v)\wedge t\), would be a frame map into a nontrivial complete Boolean frame sending **every a_n to its top**, hence factoring through \(\bigwedge_n O(a_n)=0\), contradiction. The same conclusion applies to \(B_n=k(b_n)\) for any frame map k.

**Lemma 2.2 (decreasing Boolean alternatives).** Let B be a complete Boolean algebra and \(A_n,B_n\in B\) be decreasing with \(\bigwedge_n A_n=\bigwedge_n B_n=0\). Then one cannot have \(A_n\vee B_n=1\) for all n.

**Proof.** If \(A_n\vee B_n=1\), then \(A_n^c\le B_n\). Fix m. For each n≥m, \(A_n^c\le B_n\le B_m\). Hence
\[
1=(\bigwedge_{n\ge m}A_n)^c=\bigvee_{n\ge m}A_n^c\le B_m.
\]
Thus \(B_m=1\) for every m, contradicting \(\bigwedge_m B_m=0\). □

## 3. A countable family of W-neighborhoods

Put
\[
C_n^+=[1/n,\infty)\cup\{p\},\qquad
C_n^-=(-\infty,-1/n]\cup\{q\}.
\tag{3.1}
\]
Both are CLOSED in X, since their complements
\[
X\setminus C_n^+=(-\infty,1/n)\cup\{q\},\quad
X\setminus C_n^-=(-1/n,\infty)\cup\{p\}
\]
are open in X.

The product \(C_n^+\times C_n^-\) is closed and lies inside \(T_{+-}\), so its open complement
\[
w_n=(X\times X)\setminus(C_n^+\times C_n^-)\tag{3.2}
\]
contains the closed relation \(K=\mathcal W\); in frame terms \(w_n\vee d_{\mathcal W}=1\). Consequently,
\[
\boxed{\operatorname{fit}(\mathcal W)\le O(w_n)\quad\text{for all n}.}
\tag{3.3}
\]

**Crucial sector identity.** As opens of \(X^2\),
\[
\boxed{
w_n\wedge T_{+-}
=
(a_n\boxtimes u_-)\vee(u_+\boxtimes b_n).
}
\tag{3.4}
\]
This follows because \(u_+\setminus C_n^+=a_n\), \(u_-\setminus C_n^-=b_n\), and the complement of a product rectangle is the union of the two coordinate-complement cylinders. No pointwise identification of *arbitrary sublocales* is involved.

There are symmetric neighborhoods \(w_n^\top\) obtained by interchanging coordinates, with
\[
w_n^\top\wedge T_{-+}=(b_n\boxtimes u_+)\vee(u_-\boxtimes a_n).
\tag{3.5}
\]

## 4. Main theorem — the W relation is fitted

**Theorem 4.1 (new working result).** For the compact two-apex locale X,
\[
\boxed{\mathcal H(X)=\mathcal W(X)
\subsetneq\mathcal U(X)\subsetneq\mathcal F(X)=X^2.}\tag{4.1}
\]

**Proof of W=H.** Put \(S=\operatorname{fit}(\mathcal W)\). Since \(C(d_{\mathcal W})=\mathcal W\subseteq S\), it suffices to show
\[
S\wedge O(d_{\mathcal W})=0.
\tag{4.2}
\]
Suppose not. By (1.1), at least one of \(S\wedge O(T_{+-})\), \(S\wedge O(T_{-+})\) is nonzero, because finite joins of open sublocales preserve the decomposition of O(d), and sublocale finite meets distribute over finite joins.

Take the first case. Booleanize the nonzero sublocale \(E=S\wedge O(T_{+-})\), obtaining a nontrivial complete Boolean frame B and a frame map \(g:Q\to B\) factoring through E. Let \(h,k:L\to B\) be its coordinate maps. Since E⊆O(T_{+-}),
\[
g(T_{+-})=h(u_+)\wedge k(u_-)=1_B,
\]
hence \(h(u_+)=k(u_-)=1_B\).

Since E⊆S⊆O(w_n), we have \(g(w_n)=1_B\). Using (3.4) and \(g(T_{+-})=1\),
\[
1_B=g(w_n\wedge T_{+-})
=h(a_n)\vee k(b_n),\qquad n\ge1.
\]
But the decreasing sequences \(h(a_n)\), \(k(b_n)\) both have Boolean meet zero by Lemma 2.1, contradicting Lemma 2.2. The second-sector case is symmetric via (3.5). Thus (4.2) holds and \(S=\mathcal W\), so \(\mathcal W=\mathcal H\). □

**Proof that F is the total relation.** Every continuous real-valued \(f:X\to\mathbb R\) is constant. Indeed, continuity at p forces f to equal f(p) on the whole positive half-line: otherwise continuity at a positive point gives a nonempty real interval on which f stays away from f(p), contradicting the cofinite-positive neighborhood of p. Likewise f is constant with value f(q) on the negative half-line. Continuity at 0 forces the two constants to agree with f(0). Thus all continuous real maps on X are constant, \(\mathcal F=X^2\). The strict \(\mathcal W<\mathcal U<\mathcal F\) follows from §1 and the existence of far mixed real pairs. □

**Status:** This proves \(\mathcal W=\mathcal H\), not \(\mathcal W=\mathcal U\). It does not re-open Q or Q′.

## 5. The genuinely different mechanism

Because \(\mathcal F=X^2\), the relative-clopen and relative-regular-generation criteria of the previous note reduce to **absolute** clopenness/regular generation in Q, and both FAIL:

- \(d_{\mathcal W}\) is not complemented: it is an open union of mixed sectors whose closure meets \((0,0)\in\mathcal W\).
- The previous diagonal obstruction says that \(\rho_Q(d_{\mathcal W})=d_{\mathcal W}\) would imply W=U, contradicting the strictness.

Thus the positive result \(\mathcal W=\mathcal H\) here cannot be explained by either relative regularity or relative clopenness in F. The new mechanism is the **two-sided shrinking cover**: any generalized pair living in the mixed sector and in every W-neighborhood would have to choose between two decreasing alternatives converging to zero, an impossibility in a complete Boolean target.

The example is *not scattered* (it contains the usual real line), and its square need not be assumed fit anywhere in the argument. It provides a comparatively simple compact T₁ noncoherent example with
\[
\boxed{\mathcal W=\mathcal H<\mathcal U<\mathcal F}
\]
and where the failure \(\mathcal U\nsubseteq\mathcal H\) is **not** an artifact of a finite discrete residual in F.

## 6. General two-sided shrinking criterion

A reusable sufficient condition for fittedness of a closed sublocale \(C(d)\) of a localic product \(X^2\) is the following special template.

Suppose \(d=t_1\vee t_2\), \(t_1\wedge t_2=0\), where \(t_i\) are opens of X². For each sector t_i, suppose there is a sequence of open neighborhoods \(w_{i,n}\) of C(d) such that
\[
w_{i,n}\wedge t_i
=(a_{i,n}\boxtimes v_i)\vee(u_i\boxtimes b_{i,n}),
\qquad
t_i=u_i\boxtimes v_i,
\]
where \(a_{i,n}\le u_i\) and \(b_{i,n}\le v_i\) are decreasing families, and
\[
\bigwedge_n O_X(a_{i,n})=0=\bigwedge_n O_X(b_{i,n}).
\]
Then C(d) is fitted. Indeed, a nonzero residual \(E=\operatorname{fit}C(d)\wedge O(t_i)\) would yield via Booleanization a pair h,k with \(h(u_i)=k(v_i)=1\) and \(h(a_{i,n})\vee k(b_{i,n})=1\) for every n. But both Boolean meets are zero, contradicting Lemma 2.2. This proves the general criterion without compactness, coherence, spatiality, or regularity assumptions, once the stipulated open-neighborhood identities hold.

**Caution:** This is a sufficient *template*, not a classification of fitted closed sublocales. It does not claim the two-sided shrinking equations can be found for arbitrary W.


## 7. A further strict comparison: V < W = H

Since \(X^2\) is spatial and T₁, any **ordinary point** z outside a closed sublocale C is omitted by the open neighborhood \(X^2\setminus\{z\}\) of C. Thus the fitted hull \(\operatorname{fit}(C)\) has **exactly the same ordinary points** as C, though it may contain extra pointless structure. Apply this to \(C=\mathcal I\):
\[
\operatorname{pt}(\mathcal V)=\operatorname{pt}(\mathcal I).
\]
For any real \(x>0\), the pair \((0,x)\) lies in \(\operatorname{pt}(\mathcal W)\) because both coordinates are in \(A_+\), but is **not** in \(\operatorname{pt}(\mathcal I)\), since 0 and x admit disjoint small real neighborhoods. Since the universal relation \(\mathcal V\le\mathcal H\) combines with our \(\mathcal H=\mathcal W\), this yields the strict comparison
\[
\boxed{
\mathcal I\le\mathcal V\subsetneq\mathcal W=\mathcal H
\subsetneq\mathcal U\subsetneq\mathcal F=X^2.
}
\tag{7.1}
\]
We do **not** assert \(\mathcal I=\mathcal V\), which would require a separate point-free fittedness calculation for I.

This is a useful strengthening: it realizes the strict upper-diamond relation \(\mathcal V<\mathcal W=\mathcal H\) **within a compact T₁ noncoherent space** where the further gaps \(\mathcal H<\mathcal U<\mathcal F\) are also strict.
