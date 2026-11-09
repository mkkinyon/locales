# Project A — A frame-theoretic finite-branch shrinking criterion for W=H

**9 November 2026. Working internal mathematical segment; no external audit or literature-priority claim.** This abstracts the successful compact two-apex W=H argument from [the preceding working note](A-W-equals-H-compact-two-apex-telescope-2026-11-09.md). It is independent of the deferred finite-cover fitting questions Q/Q′. We avoid introducing a new named separation axiom; the result is a reusable sufficient theorem for fittedness of arbitrary closed sublocales.

Let A be a frame; for a∈A write O(a), C(a) for its open/closed sublocales; a* for pseudocomplement. Let B be a **nontrivial complete Boolean frame**. Every nonzero locale S has nonzero Booleanization B(S), and a frame map g:A→B factors through O(a) iff g(a)=1_B.

## 1. Boolean-null towers

Call a decreasing family \(r_1\ge r_2\ge\dots\) **Boolean-null** if every frame map g:A→B to a complete Boolean frame satisfies
\[
\bigwedge_{n\ge1}g(r_n)=0_B.
\tag{1.1}
\]

**Lemma 1.1 (equivalence).** A decreasing tower is Boolean-null iff
\[
\bigcap_{n\ge1}O(r_n)=0
\tag{1.2}
\]
as sublocales. Proof: if t=∧g(r_n)>0, localize B at t, producing a nonzero map that factors through all O(r_n), so their meet cannot be zero. Conversely, if the meet S is nonzero, take the frame map \(A\to\mathcal O(S)\to B(S)\), which sends each r_n to top, contradicting (1.1). No point/spatiality assumption is used.

**Lemma 1.2 (explicit star-exhaustion test).** If
\[
\boxed{r_1\le\bigvee_{n\ge1}r_n^*,}
\tag{1.3}
\]
then the tower is Boolean-null.

*Proof.* For any g:A→B put t=∧g(r_n). Since \(g(r_n^*)\le \neg g(r_n)\),
\[
t\le g(r_1)\le\bigvee_n g(r_n^*)\le\bigvee_n\neg g(r_n)=\neg t.
\]
Thus t=0. □

In a spatial X, (1.3) says \(r_1\cap\bigcap_n\overline{r_n}=\varnothing\). It is sufficient but not asserted necessary for (1.2).

The same definitions and conclusions work for a family indexed by an arbitrary **directed** set, with common indices for all branches. Countable sequences suffice for the main application.

## 2. Finite-branch lemma

**Lemma 2.1.** Let \(B\) be a complete Boolean algebra and let \(b_{j,n}\) (1≤j≤m, n≥1) be decreasing in n with \(\bigwedge_n b_{j,n}=0\) for each j. Then
\[
\boxed{\bigvee_{j=1}^m b_{j,n}\ne 1_B
\text{ for at least one }n.}
\tag{2.1}
\]

*Proof.* Induct on m. If \(m=1\), there is nothing to show. For m≥2 suppose every finite join is top and put \(c_n=\bigvee_{j=2}^m b_{j,n}\). Since \(\neg b_{1,n}\le c_n\le c_k\) for n≥k, taking \(\bigvee_{n\ge k}\) yields \(1\le c_k\). Thus every c_k=1, contradicting the induction hypothesis on the m−1 remaining decreasing zero-meet towers. □

**Corollary 2.2 (localic finite-branch vanishing).** If, for 1≤j≤m, the sequences \(r_{j,n}\in A\) are decreasing and \(\bigcap_n O(r_{j,n})=0\), then
\[
\boxed{\bigcap_{n\ge1}O\Bigl(\bigvee_{j=1}^m r_{j,n}\Bigr)=0.}
\tag{2.2}
\]
Indeed, if the left side were nonzero, Booleanize it: the resulting map g sends each \(\bigvee_j r_{j,n}\) to top, while Lemma 1.1 says each \(\bigwedge_n g(r_{j,n})=0\), contradicting Lemma 2.1.

**Finite width is essential.** In the two-element Boolean frame A={0,1}, put \(r_{j,n}=1\) for \(n\le j\), and \(0\) for \(n>j\), with j ranging over positive integers. For each fixed j this is a decreasing Boolean-null sequence satisfying even the star test (1.3), yet \(\bigvee_{j\ge1}r_{j,n}=1\) for every n. So (2.2) fails for infinitely many branches. The shared decreasing index is likewise essential: two sequences alternating 0 and 1, whose joins are always 1, show the failure without monotonicity.

The finite-branch lemma extends verbatim to arbitrary directed indexing, by taking the join of complements on a cofinal tail in the induction proof.

## 3. General fittedness theorem

**Theorem 3.1 (finite-branch neighborhood elimination).** Let Z be an arbitrary locale, A=O(Z), d∈A, and \(T=C(d)\). Suppose there is a (possibly infinite) family of open *sectors* \(t_i\in A\) such that
\[
d=\bigvee_{i\in I}t_i.
\tag{3.1}
\]
For each i, suppose there are:

1. a **finite integer** \(m_i\ge1\);
2. open neighborhoods \(w_{i,n}\in A\) of T, so \(w_{i,n}\vee d=1\) for each n;
3. for 1≤j≤m_i, decreasing **Boolean-null** towers \(r_{i,j,n}\in A\);

such that, for every n,
\[
\boxed{t_i\wedge w_{i,n}\le\bigvee_{j=1}^{m_i}r_{i,j,n}.}
\tag{3.2}
\]

Then **T is fitted**:
\[
\boxed{C(d)=\operatorname{fit}(C(d)).}
\tag{3.3}
\]

It is enough to replace "Boolean-null" by the checkable algebraic condition
\[
r_{i,j,1}\le\bigvee_n r_{i,j,n}^*
\qquad(i\in I,\ 1\le j\le m_i).
\tag{3.4}
\]
There is **no global bound** on the numbers \(m_i\), provided each is finite. The sectors need not be disjoint. Neither the frame nor Z must be coherent, compact, spatial, locally compact, regular, or even a product.

*Proof.* Set \(S=\operatorname{fit}(C(d))\), the intersection of all open sublocales O(w) with \(w\vee d=1\). Suppose S strictly contains C(d). Since C(d),O(d) are complementary, \(E=S\wedge O(d)\ne0\). Booleanize E to obtain a frame map \(g:A\to B\) into a nonzero complete Boolean algebra with \(g(d)=1\) and \(g(w_{i,n})=1\) for every i,n. By (3.1), \(1=\bigvee_i g(t_i)\), so choose an i with \(c=g(t_i)>0\). Localize the target at c, obtaining a complete Boolean frame \(B_c=\downarrow c\) and frame map \(h(x)=g(x)\wedge c\) satisfying \(h(t_i)=1_{B_c}\) and \(h(w_{i,n})=1_{B_c}\) for all n.

Apply h to (3.2):
\[
1_{B_c}=h(t_i\wedge w_{i,n})\le
\bigvee_{j=1}^{m_i}h(r_{i,j,n}),
\]
so the finite join is top for every n. Each \(h(r_{i,j,n})\) is decreasing and meets to zero by Boolean-nullity. This contradicts Lemma 2.1. Therefore E=0, S=C(d), proving fittedness. □

**Relation to the prior product-specific criterion.** In the [two-apex note](A-W-equals-H-compact-two-apex-telescope-2026-11-09.md), the sectors were the two mixed rectangles and the branches were \(a_n\boxtimes u_-\) and \(u_+\boxtimes b_n\) (and their transposes). Theorem 3.1 removes *all* reliance on rectangular or coordinate structure. It is a genuinely frame-theoretic sufficient condition, not merely a relabeling of the product proof.

## 4. Two-apex specialization and an explicit countable fitted presentation

Retain the exact compact two-apex notation:
\[
u_+=(0,\infty)\cup\{p\},\qquad
u_-=(-\infty,0)\cup\{q\},\qquad
d_{\mathcal W}=t_+\vee t_-,
\]
\[
t_+=u_+\boxtimes u_-,\quad t_-=u_-\boxtimes u_+,
\]
and \(a_n=(0,1/n), b_n=(-1/n,0)\).

For the positive-negative sector choose \(m_+=2\) and
\[
r_{+,1,n}=a_n\boxtimes u_-,\quad r_{+,2,n}=u_+\boxtimes b_n.
\tag{4.1}
\]
Take \(w_{+,n}=(X^2)\setminus(C_n^+\times C_n^-)\), where the closed sets \(C_n^\pm\) are defined in the preceding two-apex note. Then
\[
w_{+,n}\vee d_{\mathcal W}=1,\quad
t_+\wedge w_{+,n}=r_{+,1,n}\vee r_{+,2,n}.
\tag{4.2}
\]
Similarly transpose to obtain \(w_{-,n}\) and the two negative-positive branches.

**Check (3.4) in the square:** Since
\[
a_1\le\bigvee_n a_n^*,\qquad b_1\le\bigvee_n b_n^*
\]
in O(X), the rectangle pseudocomplement formula
\[
(a\boxtimes v)^*=(a^*\boxtimes1)\vee(1\boxtimes v^*)
\]
implies
\[
r_{+,1,1}\le\bigvee_n r_{+,1,n}^*,\quad
r_{+,2,1}\le\bigvee_n r_{+,2,n}^*.
\]
The transposed conditions are identical. So Theorem 3.1 yields \(\mathcal W=\mathcal H\).

**Stronger explicit statement.** The countable family of specific neighborhoods already presents W as a fitted intersection:
\[
\boxed{
\mathcal W
=
\bigcap_{n\ge1}O(w_{+,n})
\ \cap\
\bigcap_{n\ge1}O(w_{-,n}).
}
\tag{4.3}
\]
Proof: W is contained in each open sublocale. Conversely, put S on the right, and apply the same sector arguments to S instead of the full fit(W): S∧O(t_+)=S∧O(t_-)=0, so S≤C(d_W)=W. This is an **equality of localic sublocales**, not just equality of their ordinary point sets. It is stronger than the bare fittedness result and requires only countably many explicit neighborhoods.

The topology also makes the star test transparent:
\[
\bigcap_n\overline{a_n}=\{0,p\},\quad
\bigcap_n\overline{b_n}=\{0,q\}.
\]
Both limiting closed sets avoid the first corresponding open interval.

## 5. What the theorem does and does not give

1. Theorem 3.1 provides a **purely algebraic, checkable sufficient criterion** for a closed sublocale C(d) to be fitted. It has no product assumptions and permits an arbitrary number of sectors with individually finite branch-width.
2. It does **not** assert that every fitted closed sublocale admits such a countable or directed finite-branch presentation. Even the presence of a nontrivial countable shrinking basis of neighborhoods is a substantive condition.
3. The width restriction cannot be dropped: there is a direct counterexample in the two-element Boolean frame, §2.
4. It is strictly different from absolute regular generation \(d=\bigvee_{c\prec d}c\), which forces W=U if d=d_W. Our two-apex example satisfies the finite-branch criterion yet has W=H<U<F.
5. The proof remains valid for **arbitrary closed sublocales**, not just the diagonal-related W, so it may be useful elsewhere in pointfree topology. No literature novelty claim is made without a search.

**Research choice:** Rather than immediately seek a converse (which would risk a new open-ended approximation programme), first identify a second nontrivial W example where the finite-branch criterion works but relative clopenness in F fails. The two-apex locale already supplies one. The new criterion can also be applied to existing examples with several accumulating boundary sectors if such a need arises. Keep Q/Q′ deferred.


## 6. Relative finite-branch shrinking inside any fitted envelope

The criterion also **subsumes the earlier relative-clopen and relative-regular approach** when applied in an appropriate fitted superlocale.

**Corollary 6.1.** Suppose \(S=C_Z(d)\le T\le Z\), where T is a **fitted** sublocale of Z, and S is closed in T (automatic if S is closed in Z). If, in the frame \(\mathcal O(T)\), the defining open of S satisfies the finite-branch hypotheses of Theorem 3.1 (using pseudocomplements and bottom **relative to T**), then S is fitted in Z.

*Proof.* Theorem 3.1 makes S fitted as a sublocale of T. Since T is fitted in Z, the fitted-envelope lemma [proved in the relative-fitness note](A-W-equals-H-relative-fitness-functional-envelope-2026-11-09.md) lifts this fittedness to Z. □

For our particular relation take \(Z=X^2,\ T=\mathcal F\), \(S=\mathcal W\), with \(\mathcal O(\mathcal F)=\uparrow d_{\mathcal F}\). Thus **relative finite-branch shrinking in F suffices for W=H**; it need not force W=U. The previous relative-clopen criterion is the degenerate one-branch instance: if W is clopen in F, its complement in F is a single open neighborhood excluding the entire relative residual, and the branch can be taken to be the bottom open of F.

This unifies the two previous *types* of sufficient conditions—relative clopen splitting and two-sided infinitary shrinking—without claiming either is necessary.
