# Project A — Clean cover insertions, sphere plateaux, and filtration shifts

**Canonical consolidation — 16 November 2026.**

**Status.** The seed, capped/uncapped induction, sphere-plateau theorems, actual inclusion equivalences, and integral unit differentials have passed independent blind external review. The individual-stage *crosspolytope collapse* was supplied with a proof in the second referee report and has been checked in this consolidation; it was an addition to, not a hypothesis of, the audited packet. The repeatable shift operation and the two-parameter family arose in a **post-report referee addendum** and have been checked internally, but **not separately blind-audited**. The whole-spectral-sequence shift in §8 is a further internal deduction. No novelty, minimality, or priority claim is made.

This work concerns the weight filtration of **ordinary order complexes of finite posets**. It is not a calculation of the crosscut Čech spectral sequences considered elsewhere in Project A.

## 1. The clean Boolean cover setting

Let \(Q\) be a finite poset and \(E\) a set of covers of \(Q\). Delete from its strict order relation the comparisons in \(E\), and call the resulting poset \(P=Q\setminus E\). Deleting *any* subset of the covers preserves transitivity: if \(x<y<z\), then \(x<z\) was not a cover and is not deleted. Thus the comparisons in \(E\) may be reinserted independently; they form a **clean Boolean insertion family**.

For a chain simplex \(\sigma\) of \(\Delta Q\), let

\[
\nu(\sigma)=\#\{(x\prec y)\in E:\{x,y\}\subseteq\sigma\},
\qquad F_p(Q)=\{\sigma\in\Delta Q:\nu(\sigma)\le p\}.
\]

This is a simplicial filtration, with \(F_0(Q)=\Delta P\). All homology is integral unless stated otherwise; \(d_s:E^s_{p,q}\to E^s_{p-s,q+s-1}\) is the homological convention. We distinguish the reduced absolute sequence from the relative sequence of \((\Delta Q,F_0(Q))\), and use *elementary simplicial collapse* (\(\searrow\)) more restrictively than *homotopy equivalence* (\(\simeq\)). Cones and joins below include the empty base simplex, so an apex itself is a vertex.

An important general observation is that if the \(m\) marked covers form a saturated path from a minimal to a maximal element, there is **exactly one simplex of weight \(m\)**: its \(m+1\) path vertices. It has dimension \(m\) and no coface, since no vertex can be inserted between successive covers or beyond either endpoint.

## 2. Main theorem, including the parameterized form

**Theorem 2.1 (capped absolute family; externally audited).** For each \(r\ge3\) there is a poset \(X_r\) with \(3r\) vertices and \(r\) marked covers on one minimal-to-maximal path. The full \(\Delta X_r\) is contractible. Its filtration satisfies

\[
F_p(X_r)\simeq S^{r-1}\quad(0\le p<r),\qquad F_r(X_r)=\Delta X_r\simeq *,
\]

and every **actual inclusion** \(F_{p-1}(X_r)\hookrightarrow F_p(X_r)\) for \(1\le p<r\) is a homotopy equivalence. Every individual preterminal stage simplicially collapses onto the boundary of the \(r\)-dimensional crosspolytope. The reduced absolute spectral sequence has just two nonzero \(E^1\) terms,

\[
\widetilde E^1_{0,r-1}\cong\mathbb Z,\qquad
\widetilde E^1_{r,0}\cong\mathbb Z,
\]

and the sole differential is the **unit** \(d_r:\mathbb Z\xrightarrow{\pm1}\mathbb Z\). Thus its only reduced persistent interval is \([0,r)\) in degree \(r-1\).

For \(r\ge4\), an **uncapped** version \(U_r\) has \(3r-1\) vertices with the same homotopy plateau and integral differential. At the induction step we write \(U_{r+1}=\{u,v\}\oplus X_r\), before adjoining the cap.

**Theorem 2.2 (relative family; externally audited).** For \(m\ge5\) there is a poset \(Q_m\) with \(3m-2\) vertices, \(m\) marked covers, and **collapsible** \(F_0(Q_m)\), such that

\[
F_p(Q_m)\simeq S^{m-1}\ (1\le p<m),\qquad F_m(Q_m)\simeq *,
\]

with actual successive plateau inclusions homotopy equivalences. Each sphere stage collapses onto the boundary of the \(m\)-dimensional crosspolytope. The relative spectral sequence of \((\Delta Q_m,F_0(Q_m))\) has just \(E^1_{1,m-2}=\mathbb Z\) and \(E^1_{m,0}=\mathbb Z\); its sole differential is \(d_{m-1}=\pm1\). The interval is \([1,m)\) in degree \(m-1\).

**Theorem 2.3 (independent birth and length; post-report, internally checked).** For every pair of integers \(d\ge4\) and \(k\ge0\) there is a clean Boolean insertion family \(Y_{d,k}\) with

\[
|E|=d+k,\qquad |Y_{d,k}|=3d+2k-1
\]

such that

\[
\begin{array}{c|c}
\text{filtration stage}&\text{homotopy type}\\\hline
0\le p<k&*\ \text{(indeed collapsible)}\\
k\le p<k+d&S^{d+k-1}\\
p=k+d&*.
\end{array}
\]

All successive inclusions **within** the pre-birth and sphere-plateau ranges are homotopy equivalences; individual sphere stages collapse onto crosspolytope boundaries. The reduced absolute \(E^1\)-page consists precisely of

\[
\widetilde E^1_{k,d-1}=\mathbb Z,\qquad
\widetilde E^1_{k+d,0}=\mathbb Z,
\]

and its only differential is \(d_d=\pm1\). Its only reduced persistence interval is \([k,k+d)\), in homological degree \(d+k-1\). The cases \(k=0,1\) are the uncapped absolute and the two-minimum relative examples, respectively. In the latter case the reduced absolute and \(F_0\)-relative sequences agree beyond the zero column because \(F_0\) is collapsible.

**Boundary of the claim.** This method does not supply all \([k,k+3)\) with \(k>0\), even though the capped seed gives \([0,3)\). The earlier ten-vertex/four-cover relative \(d_3\) example was mentioned in an exploratory note without sufficient data for blind verification. It is **not** included in any theorem here. No optimal size or classification is asserted.

## 3. Seed \(X_3\): exact finite certificate

Take vertices \(a,b,c,d,e,f,h,i,x\) and Hasse covers

\[
a\prec d,x;\quad b\prec c,d;\quad x\prec c,e;\quad
c\prec f;\quad d\prec e,f;\quad e,f\prec h,i,
\]

where the last clause means four covers. Mark \(a\prec d\), \(d\prec f\), \(f\prec i\), with initial marked vertex \(b_3=a\). All three marks are actual covers. The subposet \(M=\{a,b,c,d,e,f,x\}\) is contractible: the lower link of \(e\) is the path \(x-a-d-b\), while \(M-e\) has greatest element \(f\). Moreover \(X_3=M\oplus\{h,i\}\), so \(\Delta X_3\simeq *\).

Put \(A_{r,p}=F_p(X_r)\) and \(B_{r,p}=F_p(X_r-b_r)\), with inherited marks. The following **ordered elementary-collapse certificates** establish the seed plateau (the letters in a simplex name denote a vertex *set*, not an order):

| Collapse | Facet/free-face pairs, in order |
|---|---|
| \(A_{3,2}\searrow A_{3,1}\) | `(adfh,adf) (bdfi,dfi)` |
| \(A_{3,1}\searrow A_{3,0}\) | `(acfix,acfi) (adeh,adh) (adei,ade) (adi,ad) (afix,afi) (bdfh,dfh) (bcfi,bfi) (cfix,cfi) (bdf,df) (fix,fi)` |
| \(B_{3,2}\searrow B_{3,1}\) | `(bdfi,dfi)` |
| \(B_{3,1}\searrow B_{3,0}\) | `(bdfh,dfh) (bcfi,bfi) (cfix,cfi) (bdf,df) (fix,fi)` |

The simplex counts at \(p=0,1,2\) are \(76,96,100\) for \(A_3\), and \(50,60,62\) for \(B_3\). The latter has \(f\)-vector \((8,20,18,4)\) at zero. Twelve further free pairs,

```
(bdeh,deh) (bcfh,bfh) (bdei,dei) (cfhx,fhx)
(bde,de)   (bcf,bf)   (bdh,dh)   (cfh,fh)
(bdi,di)   (cfx,fx)   (bd,d)     (cf,f)
```

collapse \(B_{3,0}\) to the octahedral sphere

\[
S^0_{\{b,x\}}*S^0_{\{c,e\}}*S^0_{\{h,i\}}\cong S^2,
\]

with eight facets `bch beh bci bei chx ehx cix eix`. The link of \(a\) in \(A_{3,0}\) is a cone with apex \(x\), so \(A_{3,0}\searrow B_{3,0}\). The seed verifier in the audit archive checks every listed pair as a *free face at the moment of removal*, not just a codimension-one face.

An independent integral chain witness, useful for the original nonvanishing route, is

\[
\begin{aligned}
T={}&[b,d,f,h]+[a,d,e,h]-[a,d,e,i]-[a,c,f,i]\\
&+[b,c,f,i]-[a,d,f,h]-[b,d,f,i]+[a,d,f,i],\\
t={}&[c,f]-[c,i]-[e,h]+[e,i]+[f,h],\\
C_3={}&T+a*x*t.
\end{aligned}
\]

Here \(\partial t=0\), \(z_3=\partial C_3\in C_2(F_0)\) avoids \(a\), and the coefficient of the unique maximal-weight simplex \([a,d,f,i]\) is \(+1\). The original proof and first external blind referee independently expanded the signs.

## 4. Recursive capped construction and deletion collapses

Given \(X_r\), with minimal initial marked vertex \(b=b_r\), adjoin two incomparable minima \(u,v\) below all of \(X_r\), mark \(u\prec b\), and let \(U=\{u,v\}\oplus X_r\). Then adjoin an unmarked cap \(y\) with

\[
u\prec y\prec q\quad(q\in X_r-b),\qquad y\parallel b,v,
\]

and set \(X_{r+1}=U\cup\{y\}\), \(b_{r+1}=u\). Minimality of \(b\) ensures these prescriptions define a poset. The old marked covers remain covers; \(u\prec b\) is a cover because \(y\parallel b\). The full \(\Delta U=S^0*\Delta X_r\) is contractible, and the cap link \(\operatorname{lk}(y)=u*\Delta(X_r-b)\) is conical, so \(\Delta X_{r+1}\simeq *\).

**Filtered cap collapse.** At every level, \(F_p(X_{r+1})\searrow F_p(U)\): remove pairs \((u*y*\sigma,y*\sigma)\), for \(\sigma\in\Delta(X_r-b)\) in descending dimension. The pair has equal marked weight because it avoids \(b\). Cofaces involving \(b\) or \(v\) do not exist. These are legitimate free-face pairs even for the empty \(\sigma\), which gives \((uy,y)\). The inclusions \(F_p(U)\hookrightarrow F_p(X_{r+1})\) commute *strictly* with the filtration maps and are homotopy equivalences; no naturality of chosen collapse retractions is assumed.

Deleting the new initial marked vertex gives an exact cone decomposition

\[
B_{r+1,p}=(v*A_{r,p})\cup(y*B_{r,p}),\qquad
(v*A_{r,p})\cap(y*B_{r,p})=B_{r,p}.
\tag{4.1}
\]

To collapse \(B_{r+1,p}\) onto \(B_{r+1,p-1}\), first lift each old deletion pair \((\beta,\alpha)\) to \((y*\beta,y*\alpha)\) inside the \(y\)-cone. Then pair \((v*\sigma,\sigma)\) for old simplices \(\sigma\) of **exact weight \(p\)** in descending dimension. The second matching has no surviving \(y\)-coface, since that cone has already dropped to weight \(p-1\). The exceptional old terminal index is harmless: deleting \(b_r\) deletes its unique incident marked cover, hence \(B_{r,r}=B_{r,r-1}\), so the first matching is empty and the second still works. Consequently

\[
B_{r+1,p}\searrow B_{r+1,p-1}\quad(1\le p\le r).
\tag{4.2}
\]

At zero, (4.1) is two cones along \(B_{r,0}\), so \(B_{r+1,0}\simeq\Sigma B_{r,0}\), and hence it is a sphere \(S^r\). Finally the link of \(u\) in \(A_{r+1,0}\) is the cone \(y*B_{r,0}\), giving \(A_{r+1,0}\searrow B_{r+1,0}\).

## 5. Actual inclusion equivalences and sphere models

The essential point is that two stages being spheres does **not** itself imply that their inclusion is a homotopy equivalence. For the uncapped \(U\), put

\[
D_0=B_{r,0},\qquad D_p=A_{r,p-1}\cup B_{r,p}\quad(p\ge1).
\]

Separating simplices with initial new vertex \(v\) or \(u\), and counting the extra mark \(u\prec b\), gives exactly

\[
F_p(U)=(v*A_{r,p})\cup(u*D_p),\qquad
(v*A_{r,p})\cap(u*D_p)=D_p.
\tag{5.1}
\]

Since \(A_{r,p-1}\cap B_{r,p}=B_{r,p-1}\), the weight-\(p\) pairs in the collapse \(B_{r,p}\searrow B_{r,p-1}\) stay free after adjoining \(A_{r,p-1}\). Therefore

\[
D_p\searrow A_{r,p-1}\quad(p\ge1).
\tag{5.2}
\]

The **first** inclusion \(D_0\hookrightarrow D_1\) is a homotopy equivalence via \(B_{r,0}\hookrightarrow A_{r,0}\hookrightarrow D_1\). For \(2\le p\le r\), compare \(D_{p-1}\hookrightarrow D_p\) with \(A_{r,p-2}\hookrightarrow A_{r,p-1}\) in their strictly commuting inclusion square; the vertical arrows are equivalences by (5.2) and the top arrow by induction. Two-out-of-three gives the bottom equivalence.

Each union in (5.1) is a homotopy pushout of two **simplicial cones** along \(D_p\). Every inclusion of subcomplexes is a cofibration. The two cone maps at successive levels are equivalences because each cone is contractible, and the intersection map is an equivalence by the preceding argument. The gluing lemma then proves that the **actual** \(F_{p-1}(U)\hookrightarrow F_p(U)\) is an equivalence for \(1\le p\le r\). The commuting cap-inclusion squares transfer this result to \(X_{r+1}\), completing Theorem 2.1.

The referee also supplied a stronger, short **cone-reduction lemma**. For finite simplicial \(D\subseteq A\), and distinct new incomparable apices \(u,v\),

\[
K=(v*A)\cup(u*D)\ \searrow\ (v*D)\cup(u*D)=S^0*D.
\tag{5.3}
\]

Indeed pair \((v*\sigma,\sigma)\) for every \(\sigma\in A\setminus D\), descending in dimension: there is no \(u\)-coface because \(\sigma\notin D\); all larger other cofaces have already been removed. Elementary collapses lift under simplicial suspension. Apply (5.3) to (4.1) and (5.1), then (4.2), (5.2), and the octahedral seed: every deletion stage and every preterminal capped or uncapped stage **simplicially collapses onto a standard crosspolytope boundary**. This is an *individual-stage* statement and does **not** replace the inclusion-equivalence proof.

## 6. The two-minimum relative example

Take the uncapped \(U=\{u,v\}\oplus X_r\) and adjoin two incomparable minima \(s,t\) below every vertex of \(U\), marking \(s\prec u\), to obtain \(Q_m=\{s,t\}\oplus U\), \(m=r+2\). Let

\[
D'_p=F_{p-1}(U)\cup F_p(U-u)\quad(p\ge1),\qquad U-u=v*X_r.
\]

Then

\[
F_p(Q_m)=(t*F_p(U))\cup(s*D'_p),\quad
(t*F_p(U))\cap(s*D'_p)=D'_p.
\tag{6.1}
\]

For old \(X_r\)-simplices \(\sigma\) of exact weight \(p\), pairing \((v*\sigma,\sigma)\) in descending dimension yields \(D'_p\searrow F_{p-1}(U)\). Formula (5.3) therefore gives actual individual-stage collapses

\[
F_p(Q_m)\searrow S^0*F_{p-1}(U),\quad 1\le p<m.
\tag{6.2}
\]

Inclusion squares, this retraction to \(F_{p-1}(U)\), and the cone gluing lemma prove actual plateau inclusions are homotopy equivalences. At zero, \(\operatorname{lk}_{F_0(Q_m)}(s)=v*A_{r,0}\) is a cone: delete \(s\), leaving the cone \(t*F_0(U)\). Hence \(F_0(Q_m)\) is **collapsible**. The full \(\Delta Q_m\) is a suspension of the contractible \(\Delta U\). This proves Theorem 2.2, including the crosspolytope refinement.

## 7. Repeatable shift and two-parameter realization

**Lemma 7.1 (post-referee shift; internally checked).** Let \(Y\) have a marked cover starting at a minimal vertex \(b\). Suppose \(Y-b=\{c\}\oplus W\), where the new cone minimum \(c\) has **no incident marked edge**. Let \(T(Y)=\{s,t\}\oplus Y\), with one new mark \(s\prec b\). Then, for \(p\ge1\),

\[
F_p(TY)\searrow S^0_{s,t}*F_{p-1}(Y),
\tag{7.1}
\]

and \(F_0(TY)\) is collapsible. The inclusion \(F_p(TY)\hookrightarrow F_{p+1}(TY)\) is a homotopy equivalence whenever the old \(F_{p-1}(Y)\hookrightarrow F_p(Y)\) is one. Moreover \(T(Y)-s=\{t\}\oplus Y\), with \(t\) unmarked, so the hypothesis is preserved and \(T\) can be iterated indefinitely.

*Proof.* Write \(A_p=F_p(Y)\), \(B_p=F_p(Y-b)=c*F_p(W)\), and \(D_p=A_{p-1}\cup B_p\). Then

\[
F_p(TY)=(t*A_p)\cup(s*D_p),\qquad (t*A_p)\cap(s*D_p)=D_p.
\]

The cone with unmarked apex \(c\) gives \(B_p\searrow B_{p-1}\) by weight-exactly-\(p\) pairs \((c*\sigma,\sigma)\) in descending dimension. These pairs remain free when \(A_{p-1}\) is adjoined, and so \(D_p\searrow A_{p-1}\). Apply (5.3), followed by the suspended latter collapse, to obtain (7.1). At \(p=0\), delete \(s\) using its conical link \(B_0\) and then collapse \(t*A_0\) to \(t\). The inclusion assertion follows from natural commuting squares \(A_{p-1}\hookrightarrow D_p\) and the cofibrant homotopy-pushout gluing lemma, exactly as in §5. \(\square\)

To deduce Theorem 2.3, start with the uncapped extension \(U_{d}=\{u,v\}\oplus X_{d-1}\), \(d\ge4\). It has \(d\) marks, \(3d-1\) vertices and sphere plateau \(S^{d-1}\) at \(p=0,\ldots,d-1\), followed by a contractible terminal stage. It satisfies \(U_d-u=\{v\}\oplus X_{d-1}\). Put \(Y_{d,k}=T^k(U_d)\). Each iteration adds two vertices and one mark, suspends the preceding sphere stage and shifts its birth one filtration step. The pre-birth stages are collapsible by induction because suspension preserves collapses; the terminal complex remains contractible. Their actual inclusions are equivalences by two-out-of-three (between contractible complexes) and Lemma 7.1. This yields all stated dimensions, counts, and interval endpoints.

## 8. Shift of the *entire* spectral sequence (new internal deduction)

The individual-stage collapses in Lemma 7.1 have a useful **nested** target. Define a simplicial subfiltration of \(F_\bullet(TY)\) by

\[
G_0=\{t\},\qquad G_p=S^0_{s,t}*F_{p-1}(Y)\quad(p\ge1).
\]

By the concrete pairings in Lemma 7.1, \(F_p(TY)\searrow G_p\) at **each** level, including \(p=0\). The maps \(G_p\hookrightarrow F_p(TY)\) commute strictly with all filtration inclusions: the chosen collapse *retractions* need not commute, and none are used. The long exact sequences of successive pairs therefore imply that the inclusion of filtered simplicial chain complexes \(C_*(G_\bullet)\hookrightarrow C_*(F_\bullet(TY))\) is an \(E^1\)-isomorphism, hence an isomorphism on every subsequent page.

The filtration \(G\) is the reduced simplicial suspension of the old filtration, shifted one filtration index (with the base point \(G_0=\{t\}\)). Using augmented reduced chains to make the suspension and \(p=0\) conventions precise, this yields **natural integral isomorphisms**

\[
\boxed{\widetilde E^s_{p+1,q}(T(Y))\cong
\widetilde E^s_{p,q}(Y),\quad p\ge0,\ s\ge1,}
\tag{8.1}
\]

compatible with all differentials. More precisely, the isomorphism raises the filtration index and total homological degree by one, and leaves \(q\) and the differential page \(s\) unchanged. Column zero of the new reduced absolute sequence vanishes. Accordingly all torsion, higher-page extension patterns **at the associated-graded spectral-sequence level**, and differential coefficients are preserved. On the persistence side,

\[
\widetilde H_j(F_{p+1}(TY);\mathbb Z)
\cong\widetilde H_{j-1}(F_p(Y);\mathbb Z),\quad p\ge0,
\]

naturally for the filtration maps; all \(\widetilde H_j(F_0(TY))\) vanish. This is stronger than the single-interval construction. It is an **internally derived corollary**, not a claim passed to the earlier blind referees, and it should be independently checked before being promoted to audited status.

## 9. Why the differential is an integral unit

For \(X_r\), each intermediate pair has zero relative homology because the inclusion is a homotopy equivalence. The initial reduced \(H_{r-1}(F_0)\) is \(\mathbb Z\). The final pair \((F_r,F_{r-1})\), with contractible \(F_r\) and \(F_{r-1}\simeq S^{r-1}\), has exactly \(H_r\cong\mathbb Z\). This gives precisely the two claimed \(E^1\) groups. Their only possible connecting map has page \(r\); reduced convergence to zero forces it to be an isomorphism, necessarily \(\pm1\).

For \(Q_m\), the same reasoning relative to the collapsible \(F_0\) puts \(\mathbb Z\) at \((1,m-2)\) and \((m,0)\), forcing unit \(d_{m-1}\). Finally for \(Y_{d,k}\) all intermediate relative groups vanish, with just \(\mathbb Z\) at \((k,d-1)\) and \((d+k,0)\); contractible abutment forces unit \(d_d\). For \(k=0\) we are using reduced absolute chains. In unreduced absolute homology the connected examples have an additional permanent \(H_0\cong\mathbb Z\) at \((0,0)\); it is not a competing long differential.

The uniqueness of the maximal marked simplex gives an equivalent chain-level argument. But the preceding rank-one and vanishing-abutment proof establishes *integral primitivity*, not just nonvanishing modulo two. The unit remains a unit after extension of coefficients to any nonzero commutative ring.

## 10. Provenance, sanity checks, and limitations

| Item | Evidence and status |
|---|---|
| Nine-vertex seed, original integral witness, capped/uncapped unboundedness | Internally adversarially audited; first independent blind referee accepted the construction, correcting one historical numerical label. |
| Exact collapse certificates, sphere plateaux, actual inclusion equivalences, unit absolute and relative differentials | Second independent blind referee **accepted** the self-contained proof and verified the finite seed script. |
| Every individual sphere stage collapses to a crosspolytope boundary | Additional proposition and proof supplied in the second referee report; verified here, but not part of the original submitted theorem statement. |
| Repeatable \(T(Y)\), arbitrary birth time \(k\), independent length \(d\ge4\) | Post-report referee addendum; independently reasoned about and checked in small examples; **no separate blind adversarial audit**. |
| Entire reduced spectral-sequence shift, (8.1) | Further internal filtered-subcomplex argument in this consolidation; **not externally audited**. |

The first referee corrected the \(13\)-vertex relative \(d_4\) barcode: it is \([1,5)\) in **degree 4**, not degree 3. That correction has been applied throughout this canonical statement. The second referee independently enumerated and computed mod-two homology for \(X_3,X_4,X_5,Q_5,Q_6\), corroborating the predicted plateaux and the vanishing of intermediate successive-pair homology. As an additional check of the shift addendum, \((d,k)=(4,2)\) yields \(15\) vertices, \(6\) marks, with a single \(H_5\) interval \([2,6)\) over \(\mathbb F_2\); these computations are **corroboration**, not the source of the integral theorem.

The filtration belongs to one fixed poset and counts marks *jointly present in a chain*. It should not be conflated with (i) the whole Boolean diagram of intermediate posets as a simplicial filtration, (ii) arbitrary cover selections without the required geometry, or (iii) the project's crosscut Čech spectral sequences. No claim is made that every possible barcode is realizable, that the sizes here are smallest, or that the constructions give universal behavior of localic relations.

**Next bounded questions.** (a) Independently audit the repeatable shift and (8.1) together, if they become central to further work; a third review of the already checked sphere plateau is unnecessary. (b) Test whether the missing \(d=3,k>0\) shift cases have a different clean realization, without invoking the unaudited ten-vertex example. (c) Search for a conceptual relation between this chain-complex construction and the graph/crosscut side of Project A; do not presume that the filtration is already a localic invariant.

**Companion primary records.** The audit archive `project-a/audits/2026-11-16/CLEAN_COVER/` preserves the two blind packets, original reports and addenda, an internal adversarial audit, and executable seed checks. Those dated records remain the sources for exact original assertions and chronology; this note is the **current mathematical statement**.
