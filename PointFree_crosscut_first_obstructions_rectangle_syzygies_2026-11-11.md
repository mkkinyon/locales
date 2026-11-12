# Project A — First crosscut obstructions as rectangle and two-sided witness cycles

**11 November 2026. Bounded working continuation; internally checked, NOT independently audited.** This connects the [relative crosscut spectral sequences](PointFree_crosscut_relative_homology_spectral_sequence_2026-11-11.md), the [relative edge and triangle modules](PointFree_binary_rectangle_pi1_relative_skeleton_2026-11-10.md), and the independent fourth-audit [rectangle and meet-hull groupoid results](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md). We explicitly identify the lowest possible relative homology groups as **cokernels of crosscut-component maps** and exhibit their geometric cycle representatives. The one-sided cycle bounds the earlier rectangle loop; the two-sided cycle bounds an alternating 2-sphere. These are proofs about the actual **canonical comparisons**, not comparisons of abstract homotopy types. Classical relative Mayer–Vietoris theory is a major antecedent; no novelty or publication priority assertion.

## 0. Conventions and precise scope

Start with a finite nonempty poset P, an upper-cofinal crosscut U and a lower-coinitial crosscut L. Write
\[
\mathbf C=|\mathrm{Ch}_\bullet(P)|,\quad
\mathbf I=|I_\bullet(P)|,\quad
\mathbf M=|M_\bullet(P)|,\qquad M_n=I_n\cap D_n.
\]
These are realizations of the *ordered tuple nerves* (with degeneracies), not simply an unmarked comparison of abstract finite simplicial complexes. Let R be a commutative coefficient ring. In the finite case the crosscut resolutions are genuine double/triple Čech resolutions of the canonical simplicial inclusions, and the spectral sequences of the preceding note apply.

In §5 we give the internally coherent-sheaf version with **relative homology sheaves of the window realization**, never replacing them by groups of individual point-fibres.

## 1. Exact first obstruction presentation: upper crosscuts

Put \(F(u_0,\ldots,u_q)=\bigcap_i\downarrow u_i\). In the one-sided relative spectral sequence,
\[
E^1_{q,t}=\bigoplus_{(u_0,\ldots,u_q),\,F\ne\varnothing}^{\rm norm}
\widetilde H_{t-1}(\mathrm{Ord}(F);R),
\qquad E^1_{0,t}=E^1_{q,0}=0.
\]
At **total degree two**, only \((q,t)=(1,1)\) can contribute. Its outgoing \(d^1\) is zero, incoming \(d^1\) comes from \((2,1)\), and all \(d^r,r\ge2\) into or out of \((1,1)\) vanish for degree/zero-column reasons. The associated filtration of H_2 has only this single nonzero quotient. Therefore
\[
\boxed{\ 
H_2(\mathbf I,\mathbf C;R)\cong
\operatorname{coker}\left(
\bigoplus_{(u,v,w)}^{\mathrm{norm}}\widetilde H_0(F(u,v,w);R)
\xrightarrow{d_0-d_1+d_2}
\bigoplus_{(u,v)}^{\mathrm{norm}}\widetilde H_0(F(u,v);R)
\right).
\ }
\tag{1.1}
\]
Empty crosscuts contribute zero. Normalization removes **adjacent repetitions**, not all repeated parameters. This is an **exact** formula for the first potential homological obstruction, not merely a sufficient vanishing criterion. It depends on the chosen crosscut presentation, but its cokernel does not.

### Explicit representative: two witness triangles

Let \(x,y\in F(u,v)\). Consider the relative 2-chain
\[
T(x,y;u,v):=[x,y,u]-[x,y,v]\in C_2(I,\mathrm{Ch};R).
\tag{1.2}
\]
Both displayed triangles belong to \(I_2\), because u or v is a common upper witness. Their boundaries differ by **chain** edges:
\[
\partial T
=[y,u]-[x,u]-[y,v]+[x,v]
=-r(x,y;u,v),\quad
r=[x,u]-[y,u]+[y,v]-[x,v].
\tag{1.3}
\]
Thus T is a **relative cycle**, and its connecting image in \(H_1(\mathbf C;R)\) is the negative of the earlier rectangle loop.

The class depends only on \([x]-[y]\in\widetilde H_0(F(u,v);R)\): if x≤y (or y≤x), both relative triangles vanish up to the evident order/relative simplicial identities. For arbitrary z in F, the normalized 3-simplex identity
\[
\partial([x,y,z,u]-[x,y,z,v])
=T(y,z;u,v)-T(x,z;u,v)+T(x,y;u,v)
\tag{1.4}
\]
gives additivity in relative homology. A path of comparable vertices in F shows dependence only on connected components. The triple-parameter relations in (1.1) correspond to the alternating comparison of three possible witnesses; the canonical zigzag from the Čech total complex to the relative chain complex identifies its degree-two edge map with (1.2), up to the global orientation sign.

### Exactly what this detects in the rectangle groupoid

The independent rectangle-groupoid theorem identifies \(\pi_1(\mathbf I)\) as the quotient of \(\pi_1(\mathbf C)\) by the *normal* closure of these rectangle loops, componentwise and in the coherent setting locally/sheafwise. Abelianization gives
\[
\ker[H_1(\mathbf C;R)\to H_1(\mathbf I;R)]
=\langle [r(x,y;u,v)]\rangle_R.
\tag{1.5}
\]
The relative homology exact sequence yields
\[
\boxed{\
0\to\operatorname{coker}[H_2(\mathbf C;R)\to H_2(\mathbf I;R)]
\to H_2(\mathbf I,\mathbf C;R)
\xrightarrow{\partial}
\ker[H_1(\mathbf C;R)\to H_1(\mathbf I;R)]
\to0.
\ }
\tag{1.6}
\]
The map \(\partial\) is given on the crosscut generators by (1.3). **Crucial:** the full first relative group is not automatically the abelianized rectangle kernel; it can have the extra \(H_2(\mathbf I)\)-cokernel term. This prevents an unwarranted identification of a homological obstruction with a nonabelian \(\pi_1\) defect.

## 2. Exact first obstruction presentation: two-sided windows

Put \(F(a_\bullet;u_\bullet)=\bigcap_i\uparrow a_i\cap\bigcap_j\downarrow u_j\). The two-sided relative spectral sequence has
\[
E^1_{r,s,t}=
\bigoplus_{(a_\bullet;u_\bullet),\,F\ne\varnothing}^{\rm norm}
\widetilde H_{t-1}(\mathrm{Ord}(F);R).
\]
The \(r=0\) and \(s=0\) axes vanish because the corresponding windows have a least or greatest point; also \(t=0\) vanishes because every admitted window is nonempty.

At **total degree three**, only \((r,s,t)=(1,1,1)\) contributes. Its outgoing \(d^1\) lands on the zero axes; the only incoming first differentials are from \((2,1,1)\) and \((1,2,1)\). Higher differentials are excluded by the same degree/axis argument. Therefore
\[
\boxed{\
H_3(\mathbf M,\mathbf C;R)\cong
\operatorname{coker}\left[
\Big(\!\!\bigoplus_{(a,b,c;u,v)}\!\!
\widetilde H_0(F(a,b,c;u,v);R)\Big)
\oplus
\Big(\!\!\bigoplus_{(a,b;u,v,w)}\!\!
\widetilde H_0(F(a,b;u,v,w);R)\Big)
\longrightarrow
\bigoplus_{(a,b;u,v)}\widetilde H_0(F(a,b;u,v);R)
\right].
\ }
\tag{2.1}
\]
All sums in (2.1) are normalized in their own parameter directions; the map is the signed sum of deletion maps. **Only \(2\times2\) windows and their \(3\times2\)/\(2\times3\) compatibility relations appear.** The reduction is canonical as a consequence of the relative spectral sequence.

### Explicit representative: alternating witness tetrahedra

For \(a,b\le x,y\le u,v\), meaning each of a,b lies below both x,y and each of x,y lies below u,v, define
\[
W(x,y;a,b;u,v)
=[a,x,y,u]-[a,x,y,v]-[b,x,y,u]+[b,x,y,v]
\in C_3(M,\mathrm{Ch};R).
\tag{2.2}
\]
Every ordered quadruple is an \(M_3\)-simplex, with its indicated lower and upper witnesses. Direct calculation gives
\[
\partial W =
[a,x,u]-[a,y,u]-[a,x,v]+[a,y,v]
-[b,x,u]+[b,y,u]+[b,x,v]-[b,y,v].
\tag{2.3}
\]
Every displayed face is an actual specialization **chain** \(a_i\le x,y\le u_j\), hence \(\partial W=0\) in relative degree 2. Thus W defines a relative 3-cycle.

Its boundary in \(C_2(\mathbf C;R)\) is the alternating **eight-triangle cycle**
\[
z(x,y;a,b;u,v)=
\sum_{i,j\in\{0,1\}}(-1)^{i+j}
\big([a_i,x,u_j]-[a_i,y,u_j]\big).
\tag{2.4}
\]
The equality \(\partial z=0\) holds by cancellation of every kind of edge. If x,y are comparable, W vanishes relatively; the normalized 4-simplex identity
\[
\partial\sum_{i,j}(-1)^{i+j}[a_i,x,y,z,u_j]
=-W(y,z)+W(x,z)-W(x,y)
\tag{2.5}
\]
shows W depends only on the component difference \([x]-[y]\in\widetilde H_0\) of the window. Deleting one of three lower or upper witnesses gives the exact relations in (2.1). The induced map from the edge of the two-sided Čech total complex sends the generator to [W], up to total-complex orientation.

This is a genuine **second syzygy**: a relation among the witness-triangle relations, first visible after one more simplicial degree. It is why the two-sided comparison can preserve all 1-type data while killing a nonzero 2-sphere.

## 3. Relate both to the earlier first relative edge module

For B=I or M, let
\[
C_n^{\mathrm{rel}}(B)=
N_n(R[B_\bullet])\big/N_n(R[\operatorname{Ch}_\bullet]),
\qquad
L_B=C_1^{\mathrm{rel}}(B).
\]
All simplicial objects share their vertex space; therefore \(C_0^{rel}=0\). The earlier edge-module theorem gives
\[
\boxed{\ C_2^{rel}(B)\xrightarrow{d_2}L_B\longrightarrow0\quad\text{surjective}. }\tag{3.1}
\]
For every extra edge \((x,y)\) of I, pick a common upper witness u; the triangle (x,y,u) has the extra edge as its only nonchain boundary term. For an M-edge, the same triangle is in M since the edge has a common **lower** witness as well. No continuous witness choice is needed in the coherent case: the Stone witness cover is locally surjective, so the induced map of free-module sheaves is epi.

Now
\[
\boxed{\ H_2(\mathbf I,\mathbf C;R)
=\ker(d_2:C_2^{rel}(I)\to L_I)/\operatorname{im}d_3.}\tag{3.2}
\]
The crosscut description (1.1) is an alternate presentation of this same group, and the triangle differences (1.2) give explicit cycles in \(\ker d_2\). This makes clear why the *large* edge module \(L_I\) alone is not a homotopy obstruction.

For the two-sided meet, the independently checked 2-connectivity of \(\mathbf C\to\mathbf M\) implies \(H_2(\mathbf M,\mathbf C;R)=0\), i.e.
\[
\ker(d_2:C_2^{rel}(M)\to L_M)=\operatorname{im}d_3.
\tag{3.3}
\]
The next syzygy is
\[
\boxed{\ H_3(\mathbf M,\mathbf C;R)
=\ker(d_3:C_3^{rel}(M)\to C_2^{rel}(M))/\operatorname{im}d_4.}\tag{3.4}
\]
The alternating tetrahedra (2.2) are the universal *first candidate representatives* of these syzygies.

The relative homology LES in degree 3 is
\[
\boxed{\
0\to\operatorname{coker}[H_3(\mathbf C;R)\to H_3(\mathbf M;R)]
\to H_3(\mathbf M,\mathbf C;R)
\xrightarrow{\partial}
\ker[H_2(\mathbf C;R)\to H_2(\mathbf M;R)]
\to0.
\ }
\tag{3.5}
\]
Thus the first two-sided group measures 2-dimensional cycles **killed** by the meet hull, together with any new 3-dimensional homology **created** in that hull. It is not generally a fundamental-group defect: the chain-to-meet map already induces an isomorphism on the fundamental groupoid.

## 4. Controls: P2, P3, higher layered posets

**P2 = \(A_2\oplus A_2\).** Let the two minima be a,b and two maxima u,v. The chain nerve is a circle and I is contractible. \(F(u,v)=\{a,b\}\) is disconnected. The element
\[
T(a,b;u,v)=[a,b,u]-[a,b,v]
\]
generates \(H_2(\mathbf I,\mathbf C;\mathbb Z)\cong\mathbb Z\), and its boundary (1.3) is the fundamental rectangle loop of \(\mathbf C\simeq S^1\). This is a direct geometric realization of the first relative edge/triangle defect.

**P3 = \(A_2\oplus A_2\oplus A_2\).** Let a,b be the minima, x,y the two middle points, and u,v the maxima. The one-sided pairwise intersection \(F(u,v)=P_2\) is connected, so its first obstruction \(H_2(\mathbf I,\mathbf C)\) vanishes; its next nonzero group is \(H_3\cong\mathbb Z\), from \(\widetilde H_1(P_2)\). In contrast the two-sided \(2\times2\) window is \(\{x,y\}\cong S^0\). The explicit W from (2.2) satisfies \(\partial W=z\), and \(z\) is the alternating sum of the **eight oriented maximal chains** of P3. Its H_2 class is a generator of \(\widetilde H_2(\mathbf C;\mathbb Z)\cong\mathbb Z\); since M is contractible, \(W\) generates \(H_3(\mathbf M,\mathbf C;\mathbb Z)\cong\mathbb Z\). This computation directly exhibits the first sharp failure of 3-connectivity of the canonical chain-to-meet comparison.

**m≥4.** For \(P_m=(A_2)^{\oplus m}\) the critical 2×2 window has \(\mathrm{Ord}(P_{m-2})\simeq S^{m-3}\), hence \(\widetilde H_0=0\). Therefore the *first potential* two-sided obstruction H_3 vanishes for m≥4, while the first nonzero relative group moves to H_m≅Z. This agrees with the sharp connectivity ladder and verifies that the explicit tetrahedral class is a genuinely **low-degree** phenomenon, not a disguised general formula for all m.

### Canonical I/D duality versus unequal edge modules

The independently checked **edgewise Dowker comparison** identifies \(\mathbf I\) and \(\mathbf D\) in the undercategory of \(\mathbf C\): the triangle of canonical maps commutes up to the specified homotopy. Consequently their homotopy cofibres and **all** their relative homology groups/sheaves are canonically equivalent:
\[
H_k(\mathbf I,\mathbf C;R)\cong H_k(\mathbf D,\mathbf C;R)
\quad\text{for every }k.
\tag{4.1}
\]
This does **not** mean their first relative skeletal edge modules are isomorphic. In the previously independently checked Stone-indexed triangle wedge \(W_S(P,v)\), the explicitly endpoint-labelled modules are
\[
L_I\cong M_R^{\oplus12},\qquad
L_D\cong M_R^{\oplus10}\oplus N_R^{\oplus2}\oplus Q_R^{\oplus2},
\]
with \(M_R=R[h(S)]\), \(N_R=R[h(S^2)]\), and \(Q_R=\operatorname{coker}(M_R\to N_R)\). Yet **both canonical maps are equivalences**, so all the corresponding relative homology sheaves vanish. This is a useful check on the distinction between **edge-generation data** and the **actual crosscut obstruction** after witness triangles and higher simplices impose relations.

## 5. Coherent patched Stone-sheaf extension, with correct qualifications

Let X be coherent and let \(\mathscr H_\kappa\) be the established patched Stone-sheaf ∞-topos. Use the exact prior resolutions \(f_q:\mathcal F_q\to h(D_q)\) and \(g_{r,s}:\mathcal G_{r,s}\to h(R_{r,s})\). Apply the free R-module functor into connective derived R-module sheaves. The corresponding relative spectral sequences have E¹ terms
\[
K^I_{q,t}=\mathcal H_t(\operatorname{cofib}(R[\mathcal F_q]\to R[h(D_q)])),
\qquad
K^M_{r,s,t}=\mathcal H_t(\operatorname{cofib}(R[\mathcal G_{r,s}]\to R[h(R_{r,s})])).
\]
Here \(K^I_{0,t}=0\), \(K^M_{0,s,t}=K^M_{r,0,t}=0\), and **all t=0 rows vanish** because the relative window maps are 0-connective (effective epimorphisms). The same first-degree collapse therefore gives:
\[
\boxed{\
\mathcal H_2(\mathbf I,\mathbf C;R)
\cong\operatorname{coker}(K^I_{2,1}\xrightarrow{\sum(-1)^i d_i}K^I_{1,1}),
}\tag{5.1}
\]
\[
\boxed{\
\mathcal H_3(\mathbf M,\mathbf C;R)
\cong\operatorname{coker}\big(K^M_{2,1,1}\oplus K^M_{1,2,1}
\xrightarrow{d_L\pm d_U}K^M_{1,1,1}\big).
}\tag{5.2}
\]
The full derived/spectral machinery still has the model/site bookkeeping caveat from the preceding note; the **low-degree consequences themselves** are insensitive to higher convergence because there are no possible other entries or higher differentials in the stated total degrees.

The relative edge module \(L_I\) and relative meet-edge module \(L_M\) remain **free-module sheaf cokernels**, not sheaves freely indexed by a presumed patch-clopen complement of the chain relation. The explicit T and W are natural families over their genuine Stone witness-parametrizing spaces; their existence does not assert that every ordinary pointwise window component extends to a continuous family. In particular, an arbitrary coherent locale cannot replace these relative homology sheaves with direct sums over patch points or ordinary point-fibres.

## 6. What has and has not been proved

- **Proved internally:** the first obstruction presentations (1.1),(2.1), explicit relative T/W witnesses with boundary formulas (1.3),(2.3)–(2.4), edge/triangle module comparison (3.1)–(3.5), and the finite P2/P3 checks. Algebraic sign identities were checked separately by symbolic boundary expansion.
- **Previously checked independently:** fundamental groupoid quotient by rectangle loops; universal 2-connectivity and fundamental groupoid equivalence for C→M; these are dependencies, not external audits of T/W or the crosscut spectral sequences.
- **Not claimed:** the first crosscut group is *always equal* to the abelianized rectangle kernel; the low-degree homology controls nonabelian π1; or ordinary pointwise component groups compute internal coherent-sheaf obstructions. No novelty evaluation against all of classical relative Čech theory.
- **Natural next boundary:** use (5.1)–(5.2) on the old nonconstant S-indexed triangular family to distinguish genuinely **sheaf-parametrized component defects** from pure finite-poset components, or close this homotopy segment and return to one noncoherent binary relation question per the research-priority register.

**Status: new internal proof, not independently audited.**
