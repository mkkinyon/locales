# External blind referee packet — Unbounded integral differentials from clean cover insertions

**16 November 2026.** Self-contained mathematical claim and proposed proof; *independent audit requested*. The internal audit is deliberately excluded. This construction concerns a filtration of order complexes by newly inserted covers, not the earlier crosscut Čech spectral sequence.

## 1. Definitions and conventions

Let \(Q\) be a finite poset and let \(E\) be a set of covers of \(Q\). Put \(P=Q\setminus E\), meaning the strict order relation of \(P\) consists of all strict comparisons of \(Q\) except those in \(E\). Since an inequality with an intermediate element cannot be a cover, deletion of an arbitrary subset of the covers preserves transitivity. Thus \(E\) is a **clean Boolean insertion family**: every subset of \(E\) can independently be reinserted into \(P\).

Work with the integral simplicial chain complex \(C_*(\Delta Q;\mathbb Z)\). Write \([x_0,\ldots,x_k]\) for a chain with \(x_0<\cdots<x_k\) and its order orientation. Its **weight** is
\[
  \nu([x_0,\ldots,x_k])
  =|\{(a<b)\in E:\{a,b\}\subseteq\{x_0,\ldots,x_k\}\}|.
\]
Let \(F_p\subseteq\Delta Q\) be the subcomplex of simplices with \(\nu\le p\); \(F_0=\Delta P\). Monotonicity under faces is immediate. The **absolute** spectral sequence is associated to \(F_0\subseteq\cdots\subseteq F_{|E|}=\Delta Q\); the **relative** spectral sequence belongs to the filtered quotient complex \(C_*(\Delta Q,F_0;\mathbb Z)\). We use the homological convention
\[
 d_r:E^r_{p,q}\longrightarrow E^r_{p-r,q+r-1}.
\]

For chains \(A,B\) on pairwise comparable, disjoint blocks, \(A*B\) denotes their oriented simplicial join, with vertices of \(A\) preceding those of \(B\). In particular, for a cycle \(z\),
\[
 \partial((u-v)*C)=-(u-v)*\partial C,\qquad
 \partial(u*y*z)=(y-u)*z.
\]
The augmented-chain convention is used solely to make these usual cone identities transparent; all displayed witness chains have nonnegative degree.

## 2. A general nonvanishing certificate

**Lemma 2.1 (maximal-simplex certificate, absolute).** Suppose \(Q\) has exactly \(m\) marked covers, forming a chain of covers from a minimal to a maximal vertex. Suppose \(\Delta Q\) is contractible and an integral \(m\)-chain \(C\) has coefficient \(1\) on the marked-path simplex \(\tau\), with \(\partial C\in C_{m-1}(F_0)\). Then the absolute spectral sequence has a nonzero integral
\[
 d_m:E^m_{m,0}\longrightarrow E^m_{0,m-1}.
\]

*Proof.* All \(m\) marks can occur simultaneously only in \(\tau\), since successive marked comparisons are covers, the first marked vertex is minimal, and the last maximal. Thus \(\tau\) is the sole weight-\(m\) simplex, has dimension \(m\), and has no cofaces. In \(C(F_m,F_{m-1})\), it generates a copy of \(\mathbb Z\), and the chain \(C\) lifts it with boundary in \(F_0\), so its class survives to \(E^m\). Suppose its \(d_m\) vanished. Then \(\partial C\) would bound in \(F_{m-1}\) (equivalently, the associated filtration-zero class would be killed before page \(m\)): take \(B\in C_m(F_{m-1})\) with \(\partial B=\partial C\). The absolute \(m\)-cycle \(C-B\) has coefficient \(1\) on \(\tau\). Contractibility gives \(C-B=\partial D\), but no \((m+1)\)-simplex has \(\tau\) as a face. Contradiction. The same argument with a nonzero integer multiple proves the detected target class has infinite order. \(\square\)

**Lemma 2.2 (maximal-simplex certificate, relative).** Suppose \(Q\) has \(m\ge2\) marked covers forming a path from a minimal to a maximal vertex, and both \(\Delta Q\) and \(F_0\) are contractible. If an integral \(m\)-chain \(C\) has coefficient \(1\) on the unique weight-\(m\) simplex and \(\partial C\in C_{m-1}(F_1)\), then the spectral sequence of \((\Delta Q,F_0)\) has a nonzero integral
\[
 d_{m-1}:E^{m-1}_{m,0}\longrightarrow E^{m-1}_{1,m-2}.
\]

*Proof.* The top generator survives through page \(m-1\) because its lift has boundary in \(F_1\), and there are no terms in higher filtration. If \(d_{m-1}=0\), its boundary is trivial in \(H_{m-1}(F_{m-1},F_0)\): thus \(\partial C=\partial B+D_0\), with \(B\in C_m(F_{m-1})\) and \(D_0\in C_{m-1}(F_0)\). Hence \(C-B\) is a relative \(m\)-cycle in \((\Delta Q,F_0)\). Since both spaces are contractible, \(H_m(\Delta Q,F_0;\mathbb Z)=0\). Thus \(C-B=\partial D+K_0\) for \(D\in C_{m+1}(\Delta Q)\), \(K_0\in C_m(F_0)\). Comparing coefficients on the unique maximal top-weight simplex gives \(1=0\), because it has no coface and does not lie in \(F_0\). Contradiction. The same reasoning detects an element of infinite order. \(\square\)

The inference from a vanishing differential to a filling in \(F_{m-1}\) in each lemma is the standard finite-filtration interpretation: boundaries from all earlier pages are precisely the lower-filtration corrections being allowed. Equivalently, if \(\partial C\) represents a nonzero class in \(H_{m-1}(F_{m-1})\), respectively \(H_{m-1}(F_{m-1},F_0)\), it cannot die on an earlier page.

## 3. The nine-vertex integral seed

Let \(X_3\) have vertices \(a,b,c,d,e,f,h,i,x\), with Hasse covers
\[
\begin{array}{c}
a\prec d,x,\qquad b\prec c,d,\qquad x\prec c,e,\\
c\prec f,\qquad d\prec e,f,\qquad e,f\prec h,i.
\end{array}
\]
Here \(e,f\prec h,i\) means all four comparisons. Mark
\[
E_3=\{a\prec d,\ d\prec f,\ f\prec i\}.
\]
They are covers, lie on a path beginning at the minimal vertex \(a\) and ending at the maximal vertex \(i\), and therefore form a clean Boolean family.

On the original eight vertices \(a,b,c,d,e,f,h,i\) define the oriented \(3\)-chain
\[
\begin{aligned}
T={}&[b,d,f,h]+[a,d,e,h]-[a,d,e,i]-[a,c,f,i]\\
  &+[b,c,f,i]-[a,d,f,h]-[b,d,f,i]+[a,d,f,i].
\end{aligned}
\]
Direct expansion yields
\[
\begin{aligned}
\partial T={}&[a,c,f]-[a,c,i]-[a,e,h]+[a,e,i]+[a,f,h]\\
 &-[b,c,f]+[b,c,i]+[b,d,h]-[b,d,i]-[b,f,h]\\
 &+[d,e,h]-[d,e,i].
\end{aligned}
\tag{3.1}
\]
Every displayed triangle has weight zero. Write
\[
 t=[c,f]-[c,i]-[e,h]+[e,i]+[f,h],\qquad \partial t=0.
\]
The \(a\)-containing part of \(\partial T\) is \(a*t\). Since \(a<x\) and \(x\) lies below every vertex of \(t\), define
\[
\boxed{C_3=T+a*x*t.}
\]
Then
\[
\boxed{z_3:=\partial C_3=\partial T-a*t+x*t\in F_0,\quad
\text{and }z_3\text{ avoids }a.}
\tag{3.2}
\]
The tetrahedron \([a,d,f,i]\) occurs in \(C_3\) with coefficient \(1\), and is the unique simplex of weight three.

**Contractibility.** Put \(M=\{a,b,c,d,e,f,x\}\). Then \(X_3=M\oplus\{h,i\}\). Within \(M\), the strict lower set of \(e\) has order complex the path \(x-a-d-b\); hence the link of \(e\) is contractible. Deleting \(e\) preserves the homotopy type. The remaining poset has greatest element \(f\), so \(\Delta M\), and therefore \(\Delta X_3=\Delta M*S^0\), is contractible. Lemma 2.1 proves a nonzero integral absolute \(d_3\) already on nine vertices.

## 4. A capped-path extension lemma

Define an **avoiding-path datum of length \(r\)** to consist of a finite poset \(X\), marked covers forming a path \(b=x_0\prec\cdots\prec x_r\) from a minimal to a maximal element, a contractible \(\Delta X\), and an integral \(r\)-chain \(C\) having coefficient \(1\) on the path simplex, such that \(z=\partial C\in F_0\) and \(z\) has no simplex containing \(b\).

**Lemma 4.1 (three-vertex induction).** An avoiding-path datum of length \(r\) produces one of length \(r+1\), using three additional vertices.

*Construction.* First adjoin incomparable minima \(u,v\), both below every element of \(X\), and mark the new cover \(u\prec b\). Next adjoin \(y\) with
\[
u\prec y,\qquad y\prec q\ (q\in X\setminus\{b\}),
\qquad y\parallel b,\quad y\parallel v.
\tag{4.1}
\]
Keep all old relations. Because \(b\) is minimal in \(X\), these prescriptions define a partial order without introducing a relation \(y<b\). All old marked relations remain covers: \(u,v\) are below their lower endpoints, while \(y\) is either below the lower endpoint or incomparable with \(b\). The new marked relation \(u<b\) is also a cover because \(y\parallel b\). The marked path now runs from minimal \(u\) to the same maximal \(x_r\).

Define
\[
\boxed{C^+=(u-v)*C-u*y*z.}
\tag{4.2}
\]
The correction \(u*y*z\) is a well-defined integral chain in \(F_0\): its old-vertex simplices come from \(z\in F_0\), they avoid \(b\), and neither \(u<y\) nor any \(y<q\) is marked. Since \(\partial z=0\),
\[
\boxed{\partial C^+=(v-y)*z\in F_0.}
\tag{4.3}
\]
This boundary avoids \(u\). The coefficient of the new marked-path simplex \([u,b,x_1,\ldots,x_r]\) in \(C^+\) is still \(1\), because it comes from \(u*C\), while the correction has no \(b\).

The full complex of \(\{u,v\}\oplus X\) is the suspension of the contractible \(\Delta X\). The link of the added vertex \(y\) is
\[
\Delta(\{u\})*\Delta(X\setminus\{b\}),
\]
a cone with apex \(u\). Attaching the star of \(y\) therefore preserves the homotopy type, and the enlarged order complex is contractible. This establishes all hypotheses for length \(r+1\). \(\square\)

**Corollary 4.2 (absolute unboundedness).** For every integer \(k\ge3\), there is a clean Boolean cover-insertion family with a nonzero integral absolute \(d_k\). The capped data \(X_k\) have \(3k\) vertices and \(k\) marks. For \(k\ge4\), omitting the final cap gives an absolute witness with \(3k-1\) vertices and \(k\) marks. No minimality claim is made.

*Proof.* Apply Lemma 4.1 repeatedly to the nine-vertex seed and then Lemma 2.1. The one-step pre-cap poset is already contractible and carries the chain \((u-v)*C\) with boundary in \(F_0\). \(\square\)

## 5. Relative unboundedness

Let \((X,E,C,z,b)\) be an avoiding-path datum of length \(r\ge3\). Form the **uncapped** extension \(U=\{u,v\}\oplus X\), marking \(u\prec b\). Then form
\[
Q=\{s,t_0\}\oplus U,
\]
marking \(s\prec u\) as well. All \(m=r+2\) marked covers form one path from minimal \(s\) to the old maximal vertex \(x_r\).

Set
\[
S=(u-v)*C\in C_{r+1}(U),\qquad
\widehat S=(s-t_0)*S\in C_{r+2}(Q).
\]
We have \(\partial S=-(u-v)*z\). Because \(z\in F_0(X)\) avoids \(b\), the only possible marked comparison in \(\partial\widehat S\) is \(s<u\). Thus
\[
\boxed{\partial\widehat S\in C_{r+1}(F_1(Q)).}
\tag{5.1}
\]
The coefficient of \(\widehat S\) on the unique top-weight simplex \([s,u,b,x_1,\ldots,x_r]\) is \(1\).

The whole \(\Delta Q\) is contractible, being an iterated suspension of \(\Delta X\). We claim \(F_0(Q)\) is also contractible. Write \(K=F_0(U)\). The filtration-zero simplices involving \(t_0\) form the cone \(t_0*K\); those involving \(s\) form \(s*(K-u)\), where \(K-u\) is the induced subcomplex obtained by deleting vertex \(u\). Their intersection is \(K-u\), and
\[
K-u=v*F_0(X)
\]
is a cone. The union of two cones along a contractible common base is contractible. Consequently \(H_{r+2}(Q,F_0(Q);\mathbb Z)=0\).

Apply Lemma 2.2 with \(m=r+2\). We obtain a **nonzero integral relative**
\[
\boxed{d_{r+1}:E^{r+1}_{r+2,0}\longrightarrow E^{r+1}_{1,r}.}
\tag{5.2}
\]

**Theorem 5.1 (relative unboundedness).** For every \(k\ge4\), a finite clean Boolean cover-insertion cube has a nonzero integral relative \(d_k\). One such example has exactly \(3k+1\) vertices and \(k+1\) marked covers, all on one path. In addition, the earlier ten-vertex/four-cover construction gives relative \(d_3\). Thus arbitrarily late differentials occur even in this restricted class.

The same certificate arguments work over any nonzero commutative coefficient ring: they require only a unit coefficient on the unique maximal simplex and contractibility of the ambient complex (and of \(F_0\) in the relative case).

## 6. Independent computational sanity checks and limitations

Over \(\mathbb F_2\), ordinary filtered boundary-matrix reduction corroborates the following finite examples; these checks are not used to establish integrality:

| Type | Vertices | Marked covers | Positive-length barcode in relevant degree |
|---|---:|---:|---|
| absolute \(d_4\), pre-cap | 11 | 4 | degree 3, \([0,4)\) |
| relative \(d_4\), two added minima | 13 | 5 | degree 3, \([1,5)\) |
| absolute \(d_5\), next pre-cap | 14 | 5 | degree 4, \([0,5)\) |
| relative \(d_5\), two added minima | 16 | 6 | degree 5, \([1,6)\) |

All listed marked relations were explicitly checked to be covers in the finite models. These are examples, not asserted smallest examples. They concern the cover-count filtration on ordinary order complexes and should not be conflated with the different crosscut Čech spectral sequences elsewhere in Project A. The general theorem has not yet been externally audited; no priority or novelty claim is made.
