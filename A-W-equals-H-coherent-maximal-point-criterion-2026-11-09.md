# Project A — When W = H? A coherent spectral maximal-point criterion

**9 November 2026 · New working deductions, not externally audited or priority checked.** We study \(\mathcal W=\operatorname{cl}(\operatorname{fit}\Delta)\) in its own right; the earlier finite-cover questions Q and Q′ remain **deferred**. The proof combines *externally corroborated antecedents* from the Oct 24 post-V audit with elementary finite-poset and spectral arguments; this combination and criterion have not yet been independently refereed.

## 0. Definitions and previous inputs

Let X be a locale, \(Q=\mathcal O(X)\oplus\mathcal O(X)\), \(\mathcal I=\operatorname{cl}\Delta\), \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal V=\operatorname{fit}\mathcal I\), \(\mathcal H\) the least sublocale containing Δ that is both closed and fitted, \(\mathcal U=C(d_{\mathcal U})\), and \(\mathcal F\) the real-functional equivalence relation.

Universally \(\mathcal W\le\mathcal H\le\mathcal F\), \(\mathcal W\le\mathcal U\le\mathcal F\), and
\[
\mathcal W=\mathcal H\quad\Longleftrightarrow\quad \mathcal W\text{ is fitted}. \tag{0.1}
\]
For a **coherent** locale X the previously established theory supplies:
(i) \(\mathcal W=\mathcal U\);
(ii) in the spectral point space P, *closed sublocale* C⊆X² is fitted iff its patch-closed point relation is **upward-closed under product specialization**;
(iii) \(\mathcal F\) is the least **patch-closed equivalence relation** on P containing comparability connectivity, and it is closed and fitted;
(iv) \(\mathcal U=\mathcal I\circ\mathcal I\), with genuine (pointwise) relation on spectral points given by two consecutive common-upper steps. The October post-V external audit checked (ii) and (iii); the coherent I²=U input is in the earlier coherent programme. We do not claim these established antecedents as new.

## 1. The coherent W=H collapse

**Theorem 1 (working).** Let X be coherent. The following are equivalent:
\[
\mathcal W=\mathcal H,\quad
\mathcal W\text{ fitted},\quad
\mathcal U\text{ fitted},\quad
\mathcal U=\mathcal F,\quad
\mathcal U\circ\mathcal U\le\mathcal U.
\tag{1.1}
\]
Consequently the first condition forces the entire equality
\[
\boxed{\mathcal W=\mathcal H=\mathcal U=\mathcal F.} \tag{1.2}
\]

**Proof.** Equation (0.1) and \(\mathcal W=\mathcal U\) identify the first three assertions.

If U is fitted, its patch-closed spectral point relation is both an upset and a downset in the product specialization order. It contains Δ. For any finite zigzag of specialization comparisons \(x=x_0\mathrel{\lessgtr}x_1\mathrel{\lessgtr}\cdots\mathrel{\lessgtr}x_n=y\), start with \((x,x)\in U\) and transport the **second coordinate** successively along the zigzag. Upward or downward saturation retains membership at each step; thus \((x,y)\in U\). U therefore contains comparability connectivity. It is patch-closed, so the previously established least-patch-closed-equivalence characterization of F gives \(F\le U\). Universal \(U\le F\) yields equality.

Conversely F is fitted, so U=F implies U fitted. Also F is transitive, so U=F implies U∘U≤U. Conversely, if U is transitive as a localic relation, its point relation is a patch-closed equivalence containing comparability pairs (because \(I\le U\) and comparable points belong to I). Minimality of F gives F≤U and hence equality. □

**Caution:** this coherent statement is **false without coherence**. The externally checked compact noncoherent T1 scattered α–β–γ example of the Oct 24 post-V audit has \(\mathcal W=\mathcal V=\mathcal H=\mathcal I<\mathcal U<\mathcal F\). Thus fitted W alone does not force functional collapse in arbitrary locales.

## 2. Point formulas in a spectral space

Let P be the spectral point space of a coherent frame, ordered by specialization, and write \(x\sim y\) if x,y belong to the same connected component of its **comparability graph** (a *finite* zigzag of comparisons). Put \(E=\{(x,y):x\sim y\}\).

**Lemma 2.1.** For spectral points:
\[
\begin{aligned}
(x,y)\in\operatorname{pt}(\mathcal I)
&\iff \exists u\in P,\ x\le u,\ y\le u,\\
(x,y)\in\operatorname{pt}(\mathcal U)
&\iff \exists u,v,z\in P:
x\le u,\quad y\le v,\quad z\le u,\ z\le v.
\end{aligned}
\tag{2.1}
\]
In particular, \(\operatorname{pt}(\mathcal U)\subseteq E\).

**Proof of I formula.** If x,y have a common upper u, their open neighborhoods intersect at u, so they are inseparable. Conversely, if every pair of opens containing x,y meet, consider *all compact-open neighborhoods* of x or y. Their finite intersections are nonempty, since finitely many x-neighborhoods and y-neighborhoods can be intersected separately. Compact opens are **patch-clopen**, and the patch topology is compact. Their entire intersection therefore contains a point u, lying in every open neighborhood of x and y. This means x≤u and y≤u.

**Proof of U formula.** Use the established coherent localic identity U=I∘I and its patch-compact spectral relational interpretation: a U-point is a pair connected by two I-edges through an intermediate z. Unfold both I-edges using the first formula. The inequalities show x and y are in the same finite comparability component (x≤u≥z≤v≥y). □

**Lemma 2.2 (maximal specializations).** Every x∈P lies below a maximal point of its comparability component.

**Proof.** Let C be a chain in \(\uparrow x\). Collect every compact-open neighborhood of every member of C. Any finite subcollection meets at one of the largest chain elements among their basepoints. All these neighborhoods are patch-clopen, so compactness of the patch topology produces a common point u lying in all of them; by the compact-open basis, u is an upper bound for C. Zorn's lemma gives a maximal m≥x, and it belongs to the same comparability component as x. □

## 3. Complete coherent maximal-point criterion

**Theorem 3 (new working criterion).** For a coherent locale X with spectral space P:
\[
\boxed{
\mathcal W=\mathcal H
\iff
\forall \text{ comparability components }C\subseteq P,\
\forall m,n\in\operatorname{Max}(C),\
\downarrow m\cap\downarrow n\ne\varnothing.
}
\tag{3.1}
\]
The criterion requires merely **pairwise** common lower bounds among maximal specializations; it does not require a single minimum of each component.

**Proof.** Suppose W=H. By Theorem 1, U=F; so any two maximal points m,n in the same component are U-related (F contains comparability connectivity). In the U point formula (2.1), maximality forces u=m,v=n. Hence there is z≤m,n.

Conversely, suppose the maximal-point condition. For any x∼y, choose maximals m≥x,n≥y using Lemma 2.2. Since maxima above comparable-component points stay in that component, the condition supplies z≤m,n. Formula (2.1) yields (x,y)∈pt(U). Thus E⊆pt(U). The reverse inclusion follows from Lemma 2.1, so
\[
\operatorname{pt}(U)=E.
\]
U is a **closed**, hence point-determined, sublocale of the coherent spectral square, and its point set is patch closed. As E is an equivalence relation, U is a patch-closed equivalence relation containing comparability connectivity. By the established minimality of F and the universal U≤F, U=F. Apply Theorem 1. □

**Consequences.** For coherent X, \(W=H\iff U\text{ transitive}\iff U=F\); the very concrete maximal-specialization criterion (3.1) identifies exactly which comparison geometry forces this. It is stronger than a finite-poset-only characterization.

## 4. Finite posets and a five-point fence

When P is finite with upper Alexandrov topology, all sublocales are point-determined, fitted sublocales are upsets, closed sublocales are downsets, and each comparability component is clopen. The localic equalities become:
\[
\operatorname{pt}(\mathcal D)
=\{(x,y):\downarrow x\cap\downarrow y\ne\varnothing\},
\]
\[
\operatorname{pt}(\mathcal W)=\operatorname{pt}(\mathcal U)
=\{(x,y):\exists u\ge x,v\ge y,\downarrow u\cap\downarrow v\ne\varnothing\},
\]
\[
\operatorname{pt}(\mathcal H)=\operatorname{pt}(\mathcal F)
=\bigcup_{C\in\pi_0(\mathrm{Comp}(P))} C\times C.
\tag{4.1}
\]
In particular (3.1) is a finite combinatorial test.

**Five-element fence.** Let \(P=\{m,a,k,b,n\}\) with comparabilities \(a<m,\ a<k,\ b<k,\ b<n\) and no others. Its comparability graph is the connected path m—a—k—b—n. The maximals m,k,n have common lowers pairwise *except* m,n. A direct calculation gives
\[
\boxed{
\operatorname{pt}(\mathcal W)
=\operatorname{pt}(\mathcal U)
=P^2\setminus\{(m,n),(n,m)\},
\qquad
\mathcal H=\mathcal F=P^2.
}
\tag{4.2}
\]
For example, a≤m, (a,n)∈U (extend a to k and use b≤k,n), while (m,n)∉U, explicitly exhibiting failure of upward saturation. It also shows that H=F (and transitivity of H) does **not** force W=H.

**Pairwise is weaker than a global minimum.** Take maxima m₁,m₂,m₃ and minima z₁₂,z₂₃,z₁₃, with zᵢⱼ below precisely mᵢ and mⱼ. This connected six-element poset has no common lower bound for *all* maximal elements, but any pair of maxima has one. Thus W=H=U=F=P². It is not necessary for a component to be rooted at a global minimum.

## 5. Point-free Boolean obstruction to W being fitted

Let L be **arbitrary**, \(Q=L\oplus L\), and \(d=d_{\mathcal W}\), so \(W=C(d)\). The open neighborhoods of this closed sublocale are precisely the \(O(w)\) with \(w\vee d=1_Q\) (proof: \(C(d)\le O(w)\iff w\vee d=1\), via complementary open/closed sublocales).

Write
\[
S_d=\operatorname{fit}(C(d))
=\bigcap_{\substack{w\in Q\\w\vee d=1}} O(w).
\]
This is a fitted superlocale of W.

**Proposition 5 (working, all frames).**
\[
\boxed{
W\ne H
\iff
\exists B\ne 0\ \text{complete Boolean frame},\
\exists g:Q\to B\ \text{frame map}:
\quad
g(d)=1_B,\quad
g(w)=1_B\text{ whenever }w\vee d=1_Q.
}
\tag{5.1}
\]
Equivalently g is induced by a pair \(h,k:L\to B\), and tests fitting of W directly without invoking W₂.

**Proof.** W=H iff W fitted iff \(S_d=W=C(d)\). If \(S_d\ne C(d)\), then \(S_d\wedge O(d)\ne0\), because the open and closed sublocales O(d),C(d) are complementary and sublocale finite join distributes over meet. Take its nonzero locale frame and quotient by double negation to a nonzero complete Boolean frame B; the induced g sends d and all w with w∨d=1 to top. Conversely such a g factors through \(S_d\wedge O(d)\), so this sublocale is nonzero and \(W\) is not fitted. □

This gives a useful geometric interpretation: failure of W=H is witnessed by a **Boolean-valued generalized pair lying in every open neighborhood of the closed W relation, yet lying entirely in its open complement**. In finite posets the witness can be an ordinary point (for the fence, (m,n)); in pointfree noncoherent settings the witness might be pointless.

## 6. First new research choices

- In **coherent locales**, (3.1) reduces the W=H question to maximal-specialization geometry. Explore whether this property is preserved by products, coproducts, sublocales, or suitable quotients; the finite case is an accessible testbed.
- In **arbitrary locales**, (5.1) is the closest intrinsic Boolean criterion we have. Seek a useful sufficient condition on the closed element \(d_{\mathcal W}\) weaker than the entire square being a fit frame. The positive theorem “if \(X^2\) is fit then W=H” was already externally checked in October.
- The compact noncoherent scattered T1 example \(\mathcal W=\mathcal H<\mathcal U<\mathcal F\) shows that coherent functional collapse cannot be asserted universally.

Keep the new results marked **working**, and do not reopen the deferred Q/Q′ search.


## 7. Preservation and non-heredity in the coherent class

Theorem 3 gives two short structural deductions.

**Theorem 7.1 (working).** For nonempty coherent locales \(X,Y\),
\[
\mathcal W(X\times Y)=\mathcal H(X\times Y)
\iff
\bigl(\mathcal W(X)=\mathcal H(X)\text{ and }\mathcal W(Y)=\mathcal H(Y)\bigr).
\tag{7.1}
\]
Furthermore, for arbitrary localic disjoint sums of coherent locales, \(\mathcal W=\mathcal H\) holds iff it holds on every component (with the empty/degenerate summands interpreted trivially).

**Proof for products.** Their spectral spaces are P,Q, and their product is the ordinary spectral product with coordinatewise specialization order and patch-product topology. Comparability-connected components of P×Q are precisely C×D, where C,D are components in P,Q: one direction follows by projecting comparison steps, and the other by moving one coordinate at a time while fixing the other. A point (p,q) is maximal in its component iff p,q are maximal in theirs. Two product maxima (m,n),(m′,n′) admit a common lower bound iff m,m′ have one in P and n,n′ have one in Q. Apply Theorem 3; the reverse implication uses a fixed maximal point in any nonempty component of the other factor. The disjoint-sum statement follows either from the same component criterion or from the exact clopen block decomposition for D,W,H; each summand is clopen and no connected comparability path crosses between summands. □

**Theorem 7.2 (working).** Among finite coherent locales, the property \(\mathcal W=\mathcal H\) is **neither open-hereditary nor closed-hereditary**.

**Proof.** Let P be the five-point fence in §4 with W(P)<H(P).

*Open restriction:* adjoin a new global bottom \(0\) below every element of P. Call the resulting poset P⁻. Every open cover of P⁻ contains the whole space (because it must contain 0), so \(D(P^-)=W(P^-)=H(P^-)=P^-{}^2\). The old P is the **open upper** subposet P⁻\\{0}; its intrinsic W is strictly below H.

*Closed restriction:* adjoin a new global top \(\infty\) above every element of P, obtaining P⁺. Every nonempty open of P⁺ contains \(\infty\), so \(I(P^+)=W(P^+)=U(P^+)=P^+{}^2\); the comparability graph is connected, hence \(H(P^+)=P^+{}^2\). The old P is the **closed lower** subposet P⁺\\{\infty\}, and again W(P)<H(P).

Thus neither type of sublocale inclusion preserves this equality, even with all frames finite coherent. □

These statements concern **preservation of the equality class**, not the previously established lax naturality of the W relation itself. Proper inclusions of the restricted W relation already occur on three-element forks.

## 8. Status and next question

The coherent W=H class is now sharply described by (3.1). A natural next question is how much of its *maximal-specialization geometry* can be meaningfully reconstructed for noncoherent locales, where point relations may miss pointless sublocales and W need not coincide with U. The Boolean obstruction (5.1) is an honest point-free starting point. No conjecture is opened merely on the basis of these examples.
