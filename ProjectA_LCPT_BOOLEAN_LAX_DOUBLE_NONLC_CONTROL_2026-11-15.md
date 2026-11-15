# Project A — Boolean lax double: compact sober T1, point-fitted, non-TU, but not locally compact

**15 November 2026 · New internal construction / detailed adversarial checks. NOT independently audited and NO priority claim.** A concrete test of the boundary in (LC-PT). The construction shows the **local compactness** hypothesis cannot simply be omitted from the question. The same mechanism also explains why forcing a generalized comparison over a pointless Boolean locale tends to destroy way-below approximation.

## 1. Construction

Let \(K=2^{\mathbb N}\) be the Cantor space, let \(H=\mathcal O(K)\), and let
\[
B=\operatorname{RO}(K)=\{u\in H:\neg\neg u=u\}
\]
be its complete Boolean frame of regular opens, with its own join \(\bigvee_B u_i=\neg\neg(\bigvee_H u_i)\). The double-negation nucleus yields a **surjective frame homomorphism**
\[
j:H\longrightarrow B,\qquad j(u)=\neg\neg u.
\]

Define
\[
\boxed{L=\{(u,v)\in H\times H:j(u)\le j(v)\}.}\tag{1.1}
\]
The lattice operations in L are **coordinatewise**: the inequality is preserved by arbitrary joins and finite meets because j is a frame map into B. Thus L is a frame. Write \(X\) for the corresponding locale.

Let \(e=(0,1)\in L\). The open \(O_X(e)\) has frame \(\downarrow e=\{(0,v):v\in H\}\cong H\), and its complementary closed sublocale has frame \(\uparrow e=\{(u,1):u\in H\}\cong H\). Thus X has two copies of K: one **open** (\(K_1\)) and one **closed** (\(K_0\)).

The frame projections \(L\twoheadrightarrow H\) identify the two inclusions \(K_i\hookrightarrow X\).

## 2. X is spatial, sober, T1, and compact

**Spatiality and sobriety.** The evaluations on \(K_0\sqcup K_1\) separate elements of L, since two distinct pairs differ in at least one coordinate and H is spatial. Therefore X is spatial, hence sober when represented as its space of points. In fact its points are **exactly** \(p_0,p_1\) for \(p\in K\): the point homomorphism sends e to either 0 or 1, thus factors through the complementary closed or open sublocale, both identified with K.

**T1.** Distinct points within each copy are separated in both directions by ordinary Cantor opens. For cross-copy points, \(e=(0,1)\) includes any \(p_1\) and excludes every \(q_0\). To separate \(p_0\) from \(q_1\), if \(p\ne q\), choose Cantor open u with \(p\in u\), \(q\notin u\), and use \((u,u)\in L\); if \(p=q\), use \((1,K\setminus\{p\})\in L\), allowed because K has no isolated points and \(j(K\setminus\{p\})=1\). Every point is therefore closed.

**Compactness.** If a family \((u_i,v_i)\) joins to \((1,1)\), then the two coordinate families cover compact K. Choose finite subfamilies covering K in the first and second coordinates and take their union. Hence \(1_L\) is compact: X is a compact locale and a compact sober T1 space.

**Caution:** compactness does **not** imply local compactness for nonregular locales; this difference is essential below.

## 3. Every point sublocale is fitted

For \(p_1\in K_1\), the point lies in the open regular/Hausdorff sublocale \(K_1\). Since one-point fittedness is local in open neighborhoods, \([p_1]\) is fitted in X.

For \(p_0\in K_0\), let \(S=\operatorname{fit}_X([p_0])\).

- Every open \((u,u)\) with \(p\in u\) is a neighborhood of \(p_0\). Restricted to the open sheet \(K_1\), the intersection of their open sublocales is the fitted hull of \([p_1]\) in K, namely \([p_1]\).
- The additional open \((1,K\setminus\{p\})\) also contains \(p_0\) but restricts to \(K_1\setminus\{p_1\}\) on the open sheet. Thus
  \[
  S\wedge K_1\le[p_1]\wedge(K_1\setminus\{p_1\})=0.
  \]
- The open and closed sheets jointly cover X, and the lattice of sublocales is a coframe. Consequently \(S\wedge K_1=0\) implies \(S\le K_0\).
- Restricting the full intersection of neighborhoods of \(p_0\) to the closed sheet \(K_0\) gives \(\operatorname{fit}_{K_0}([p_0])=[p_0]\), since K is regular and every Cantor open u extends to an X-open \((u,1)\).

Therefore \(S=[p_0]\). **Every point of X is fitted.**

## 4. X is not totally unordered

The two frame homomorphisms
\[
f^*,g^*:L\longrightarrow B,\qquad
f^*(u,v)=j(u),\quad g^*(u,v)=j(v)
\]
are well-defined since they are coordinate projections followed by frame homomorphism j. By (1.1), \(f^*\le g^*\) pointwise. They are distinct since
\[
f^*(e)=0,\qquad g^*(e)=1.
\]
Thus \(\boxed{X\text{ is not TU}}\). The domain B is nonzero and has no points (its complete Boolean algebra is atomless); this is an explicitly **pointless generalized comparison**, invisible in the ordinary specialization order of the T1 space X.

## 5. Why X is not locally compact: explicit way-below failure

Fix \(p\in K\) and a nonempty **clopen** neighborhood c of p. The element
\[
a=(c,c\setminus\{p\})\in L \tag{5.1}
\]
is valid because \(j(c)=j(c\setminus\{p\})=c\) (Cantor space is perfect).

**Claim.** If \(b=(u,v)\ll_L a\), then \(p\notin u\). Hence
\[
a\ne\bigvee\{b:b\ll_L a\}
\]
because the first coordinate of the right-hand side misses p, while that of a contains p. Therefore L is **not continuous** and X is **not locally compact**.

*Proof of claim.* Suppose \(b\ll_L a\) and \(p\in u\). Then \(b\le a\), so \(v\subseteq c\setminus\{p\}\), and (1.1) gives
\[
p\in u\subseteq j(u)\subseteq j(v)=\operatorname{int}\overline v.
\]
Thus v accumulates at p. Since K is compact metrizable, choose distinct \(q_n\in v\) tending to p. For each n put
\[
v_n=(c\setminus\{p\})\setminus\{q_k:k\ge n\}.
\]
The tail \(\{q_k:k\ge n\}\) is closed in \(c\setminus\{p\}\), and its closure in c is countable with no interior. Consequently each \(v_n\) is open and dense in c, so \(j(v_n)=c\). The sequence \(v_n\) is increasing with union \(c\setminus\{p\}\).

Hence the elements \(d_n=(c,v_n)\) all lie in L and satisfy
\[
d_1\le d_2\le\cdots,\qquad\bigvee_n d_n=a.
\]
Yet **no** \(d_n\) dominates b, because \(v\) contains every \(q_k\) whereas \(v_n\) excludes all \(q_k\) for \(k\ge n\). This contradicts \(b\ll a\). \(\square\)

This shows failure of local compactness at the **closed sheet** despite global compactness.

## 6. Internal adversarial checklist

1. **Frame condition:** j is a frame map into the Booleanized *quotient frame*, not a map preserving ordinary unions inside H. Both joins/finite meets are coordinatewise in L and the inequality remains valid.
2. **Extra sober points:** excluded by open/closed splitting at e. The frame itself is spatial because sheet evaluations separate its elements.
3. **T1:** the crucial cross-sheet separator is \((1,K\setminus\{p\})\), which uses **no isolated points** of K. For a finite discrete K the same construction instead has nontrivial ordinary specialization and fails point-fittedness.
4. **Fittedness:** checked as a sublocale equality, not merely setwise intersection of point neighborhoods. The coframe decomposition and regularity of K do the work.
5. **Non-TU:** a *genuine frame comparison* \(L\to B\), not a pair of ordinary points.
6. **Non-LC:** a specific open a and directed covering family defeat all way-below b with p in the first sheet; this explicitly avoids confusing **compactness with continuity**.
7. **Open question unchanged:** nothing here answers whether a **locally compact** sober T1, point-fitted non-TU example exists.

## 7. Implications for LC-PT

We now have a control construction satisfying
\[
\boxed{\text{compact, sober, T1, every point fitted, but not TU and not locally compact}.}
\]
It realizes the exact zero-fiber generalized-comparison pattern from the [zero-fiber obstruction note](ProjectA_LCPT_ZERO_FIBER_OBSTRUCTION_2026-11-15.md), over a crowded compact Hausdorff closed locus K. Its failure of local compactness happens precisely where dense open representatives of regular opens are needed.

**Next task:** identify whether the explicit way-below obstruction generalizes to *any* proposed point-fitted generalized-comparability witness over a locally compact sober T1 space, or whether there is a different construction that avoids it. Do not assume this example is a negative (LC-PT) answer.
