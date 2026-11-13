# Independent mathematical packet — Project A: products, Boolean selection, coherent envelope, and Q

**12 November 2026 · BLIND packet.** This is a self-contained statement of the main post-review deductions and the proposed proofs, not a referee verdict or novelty claim. Both Q and Q′ remain open. “Classical” means work in ordinary set theory with choice; no constructive generalization is claimed. In the formulas below, sublocale equalities mean **actual sublocales**, never merely equal point sets.

## A. Definitions and precise target

Let `X` be a locale, `L=O(X)` its frame, and `P=O(X²)=L⊕L`. Write `a⊠b` for the image of an elementary open rectangle. For an X-open cover `C⊆L` (`∨C=1`), define

\[
 w_C=\bigvee_{c\in C}c\boxtimes c,\qquad
 \Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\qquad
 \Phi_2(q)=\bigvee_{F\text{ finite cover}}(w_F\to q).
\]

The coverings refine each other, so `Φ,Φ₂` are monotone, inflationary finite-meet-preserving pre-nuclei. Let `D(X)` and `D₂(X)` be the fitted diagonal sublocales cut out by **all**, respectively **finite**, cover-square opens `O(w_C)`. Let `W=cl D`, `W₂=cl D₂`, `I=cl Δ`. Let `U=C(z)`, where

\[
 z=\bigvee_{a^*\vee b^*=1_L}a\boxtimes b.
\]

**Rank-zero identity** (baseline):
\[
\boxed{\Phi(0)=\Phi_2(0)=z.}\tag{A.1}
\]
Indeed, if a rectangle a⊠b lies in w_C*, then for every c∈C one has a∧c=0 or b∧c=0 by nonzero-product-rectangle positivity. Joining those c's on their two sides gives a*∨b*=1, hence the rectangle is far; conversely {a*,b*} is a finite cover annihilating any far rectangle. The joins of rectangles give (A.1).

Let `d=Φ₂^∞(0)` denote the least Φ₂-fixed element above 0. In the closed-sublocale notation `C(d)`, the baseline is `W₂=C(d)`; full iteration analogously gives W. In particular `W₂=U` iff `Φ₂(z)=z`. The two principal open problems are

\[
 \boxed{Q:\quad \Phi_2(z)=z\ \Longrightarrow\ \Phi(z)=z}\tag{A.2}
\]
for **each locale**, and
\[
 \boxed{Q':\quad W_2(X)=W(X)\text{ for every locale }X.}\tag{A.3}
\]
A positive universal Q′ would imply Q, not conversely. We do **not** assert either.

### A.1. Full-cover hole and its weak precursor

Fix an arbitrary X-cover C, let `ρ_C=w_C→d`, and let
\[
\boxed{E_C=W_2(X)\wedge O(\rho_C).}\tag{A.4}
\]
Since `d` is Φ₂-fixed, every finite cover square is dense in the closed W₂. The full-cover square for C fails to be dense precisely when E_C>0; thus Q′ fails iff some E_C is nonzero. When `W₂=U`, d=z and E_C is the corresponding **rank-one Q hole**. In contrast the **weak closed-relative fitting defect**
\[
 T_C=D_2(X)\wedge C_{X^2}(w_C)
\]
can be nonzero even if E_C=0. The earlier exact relationship is
\[
\boxed{E_C=\operatorname{int}_{W_2(X)}\operatorname{cl}_{X^2}(T_C).}\tag{A.5}
\]
The inclusion E_C≤closure follows because D₂ is dense in W₂ and E_C is relatively open; the converse follows because `cl T_C≤W₂∧C(w_C)` and the latter closed complement has relative interior E_C. The relative **openness** is the critical extra requirement throughout this packet.

## B. Local finiteization, chromaticity, and closed frontiers

### B.1. Locally finite covers give a one-step finite-cover bound

Call a cover C *locally finite* if there is a cover V such that for each v∈V only finitely many c∈C meet v. Fix arbitrary q∈P, set `x=w_C→q`. For v∈V let
\[
 F_v=\{c\in C:v\wedge c\ne0\},\quad
 t_v=\bigvee(C\setminus F_v).
\]
Then F_v is finite, `v∧t_v=0`, and F_v∪{t_v} is a finite X-cover. On the first-coordinate strip v⊠1, x meets the t_v-square trivially and meets every F_v-square only within q. Therefore
\[
 x\wedge(v\boxtimes1)\le(w_{F_v\cup\{t_v\}}\to q)\le\Phi_2(q).
\]
Joining v∈V proves
\[
\boxed{w_C\to q\le\Phi_2(q)\quad\text{for all q, if C locally finite.}}\tag{B.1}
\]
The same one-coordinate argument works without a globally locally finite cover on the locus
\[
\ell_C=\bigvee\{v:\#\{c\in C:v\wedge c\ne0\}<\infty\}
       =\bigvee_{F\subseteq_{fin}C}\left(\bigvee(C\setminus F)\right)^*.
\]
Thus `x∧(ℓ_C⊠1)≤Φ₂(q)` and symmetrically in the other coordinate. Put `H_C=C_X(ℓ_C)`; it is the closed intersection of the closures of all cofinite tails.

**Compact-remainder two-step theorem.** If H_C is compact then C restricts to a cover of H_C with a finite subcover F₀, equivalently `ℓ_C∨∨F₀=1`. For y=Φ₂(q), the finite cover `{ℓ_C}∪F₀` satisfies `x∧w_{ {ℓ_C}∪F₀}≤y`; hence
\[
\boxed{w_C\to q\le\Phi_2(\Phi_2(q))\quad(\forall q),\quad H_C\text{ compact}.}\tag{B.2}
\]
If `Φ₂(q)=q`, this is harmless already in one step. A separately claimed regular-H_C version uses a *one-sided compact/regular closed rigidity input*: a finite-compatible generalized pair whose first endpoint factors through a closed compact **or regular** sublocale already matches every cover. Please check that input and the deduction, rather than silently assuming it.

### B.2. Cross-link graph and chromatic frontier

Let d∈P, r=a⊠b satisfy `r∧w_C≤d`. Make a simple undirected graph Γ_r(C) on C: distinct c,c′ are adjacent iff
\[
 r\wedge((c\boxtimes c')\vee(c'\boxtimes c))\not\le d.
\]
Loops are absent by hypothesis. If Γ is k-colorable, each independent color class A_i has `r∧(∨A_i⊠∨A_i)≤d`. The k joins `∨A_i` form a **finite** X-cover, so `r≤Φ₂(d)`. More generally, for v meeting a finitely colorable induced graph on `I_C(v)={c:c∧v≠0}`, adjoin the disjoint co-tail `t_v=∨(C\I_C(v))` to the finitely many color-class unions. The same argument gives `r∧(v⊠1)≤Φ₂(d)`, and symmetrically. Write
\[
 \mathscr J_r=\{A\subseteq C:\chi(\Gamma_r[A])<\infty\},\quad
 \eta_{C,r}=\bigvee_{A\in\mathscr J_r}
                   \left(\bigvee(C\setminus A)\right)^*,
 \quad H^\chi_{C,r}=C_X(\eta_{C,r}).
\]
These yield
\[
\boxed{r\wedge(\eta_{C,r}\boxtimes1)\le\Phi_2(d),\qquad
r\wedge(1\boxtimes\eta_{C,r})\le\Phi_2(d).}\tag{B.3}
\]
If Hχ is **compact**, a finite C-subcover of Hχ gives `r≤Φ₂²(d)` by the same two-step construction. If d is Φ₂-fixed and Hχ is **regular** closed, the Booleanization of the nonzero open hole `C(d)∧O(r)` would have first coordinate supported in Hχ and would match the marked cover C to zero; the imported one-sided regular rigidity forbids this. Thus under its hypotheses a true finite-fixed hole forces Hχ to be neither compact nor regular. On the canonical least-closed-coordinate-support reduction it must be nowhere locally finitely chromatic.

### B.3. Baire and scattered-support refinements

A classical lemma: an ordinarily point-finite family of opens on a Baire space is locally finite on a dense open locus. For n, let F_n consist of points in at most n members; F_n is closed, and they cover the Baire space. In every nonempty open one of the F_n has a nonempty relatively open part; choose a maximal finite jointly intersecting subfamily there to find an open meeting only finitely many cover members.

If X is spatial and **every closed subspace is Baire**, suppose a finite-compatible generalized pair h,k fails a point-finite cover C. Restrict its target to the nonzero closed quotient killing C's matching value. Let `e_h=∨{a:h(a)=0}`, `K_h=C_X(e_h)` be the least closed support of the first map; h on `O(K_h)=↑e_h` reflects zero. On the Baire closed K_h, the restricted C has a nonempty open patch v meeting only finite F⊆C. With `t_F=∨(C\F)`, finite-cover compatibility of F∪{t_F} implies h(t_F)=k(t_F)=1. Lifting v to an X-open a with a∧t_F≤e_h forces h(a)=0, contradicting v≠0 and support reflection. Hence point-finite C is compatible with all finite-compatible generalized pairs. The derived metacompact positive class and the assertion that locally compact sober spaces are hereditarily Baire use standard topological hypotheses that should be checked.

For a **closed spatial T₁** coordinate support H, another claim removes isolated points transfinitely from any finite-compatible zero-C defect: if the first endpoint has nonzero image on an isolated singleton of a current derivative H^(α), restrict the Boolean/frame target to that component; the endpoint now factors through a **closed compact singleton**, contradicting one-sided compact rigidity. At successor stages kill all isolated opens; at limits use arbitrary-join preservation to kill the union of complements. The first endpoint therefore factors through the perfect kernel P(H); if that kernel is compact or regular, the one-sided rigidity forbids the defect. Applied to Hχ, this produces a perfect-kernel obstruction when Hχ has a spatial T₁ presentation. No theorem says all Hχ are spatial T₁.

## C. Universal U/I products and closed W transfer

### C.1. Pure-rectangle lemmas and U products

Work in classical Loc. Nonzero elementary open rectangles are nonzero products of nonzero localic opens, and the frame coproduct is generated under joins by such rectangles. Therefore
\[
\boxed{(a\boxtimes b)^*=(a^*\boxtimes1)\vee(1\boxtimes b^*).}\tag{C.1}
\]
If `(s⊠1)∨(1⊠t)=1` then s=1 or t=1: otherwise the product of the two nonzero closed complements would be nonzero and killed by this union. From (C.1), any two far X=Z×Y opens A,B have each pair of elementary rectangles `u_i⊠a_i≤A`, `v_j⊠b_j≤B` far in **at least one of Z, Y**. Their product-square lies in the complement-defining open of `U(Z)×U(Y)`. Together with naturality this proves
\[
\boxed{U(Z\times Y)=U(Z)\times U(Y),\qquad
I(Z\times Y)=I(Z)\times I(Y).}\tag{C.2}
\]
For I use `Δ_{Z×Y}=Δ_Z×Δ_Y` and `cl(A×B)=cl A×cl B`, the latter following by density on relatively open product rectangles. **No unrestricted W, W₂, D or D₂ product formula is asserted.**

### C.2. Compact fiber: no ordinary points needed

Let Y compact and `{u_i⊠v_i:i∈I}` cover Z×Y. The proposed tube-cover identity is
\[
\boxed{1_Z=
\bigvee_{F\subseteq_{fin}I:\ \bigvee_{i\in F}v_i=1_Y}
              \bigwedge_{i\in F}u_i.}\tag{C.3}
\]
Let π:Z×Y→Z be the projection; for compact Y it is proper. Use that π_* preserves directed joins and satisfies proper Beck–Chevalley. For a finite family F, a finite-distributive-subframe reduction of O(Z) identifies π_* of its finite union with `∨_{J⊆F,∨_{j∈J}v_j=1}∧_{j∈J}u_j`. The finite partial sums are directed and join 1, giving (C.3). **Referee: verify properness, Beck–Chevalley and finite reduction rather than taking them on trust.**

For an arbitrary open cover C of X=Z×Y, refine by a rectangle cover and apply (C.3). On each base patch `∧_{i∈F}u_i`, the finite Y-cover `{v_i:i∈F}` is matched by D(Y), so the fiber-diagonal pair over this base patch matches an X-cover square. Joining patches gives
\[
\boxed{\Delta_Z\times D(Y)\ \le\ D(Z\times Y).}\tag{C.4}
\]
If `W₂(Z)=I(Z)`, projection naturality supplies the opposite upper bound for W₂; closure of (C.4) and D=D₂ for compact Y give
\[
\boxed{W(Z\times Y)=W_2(Z\times Y)=I(Z)\times W(Y).}\tag{C.5}
\]
Clopen compact Y charts can be glued by open restriction in the closed U relation; this is a separate variant, not a claim about arbitrary non-open covers by sublocales.

### C.3. Generalized common-predecessor spans and the spatial-base route

For locale maps `p,f,g:T→Y`, write `p≼f,g` when `p*(a)≤f*(a)∧g*(a)` for every Y-open a. Such a span maps T into the full fitted diagonal D(Y): for each Y-cover C, `1=∨p*(c)≤∨f*(c)∧g*(c)`. More strongly, after product with arbitrary Z the maps `(id_Z×f,id_Z×g):Z×T→(Z×Y)²` match **all** Z×Y covers, by testing the comparable pullbacks on every rectangular generator. Let Σ(Y) be the join of images of all spans. Thus `Σ(Y)≤D(Y)`.

If `cl Σ(Y)=W₂(Y)` and `W₂(Z)=I(Z)`, these lifted spans have dense join in `Δ_Z×W₂(Y)`, so taking closure and applying projection naturality gives
\[
\boxed{W(Z\times Y)=W₂(Z\times Y)=I(Z)\times W₂(Y).}\tag{C.6}
\]
For a **spatial nonempty** Z with `W₂(Z)=Δ_Z`, each point z∈Z supplies a slice of D_ε(Y) in D_ε(Z×Y); point slices are dense in Z×W_ε(Y), so
\[
\boxed{W_ε(Z\times Y)=\Delta_Z\times W_ε(Y),\quad ε\in\{full,2\}.}\tag{C.7}
\]
If U(Z)=Δ_Z, (C.2) also gives U product, and Q/Q′ transfer and reflect. The method is *closed-hull* only; it does not imply D_ε multiplies for arbitrary spatial Z. An actual bad C on Z×Y restricts to bad fiber covers C_z for all z in some nonempty open base patch, sharing a nonzero Y-hole: pullback of implication is only lax, in the required direction. A variant glues product charts over a **clopen** cover of a spatial separated base.

**Essential no-go:** The imported Arrieta strongly Hausdorff, anti-Urysohn locale A has `I(A)=Δ_A` and `U(A)=W(A)=W₂(A)=A²`, yet its specialization-span core `Σ(A)=Δ_A`, since comparable generalized maps into a strongly Hausdorff locale coincide. Thus Σ-density is sufficient, not necessary, for full fitting density.

## D. Strongly distributive Boolean base: product D/D₂ without spatiality

Let M be a **complete Boolean algebra** satisfying **SDκ**: any family of at most κ partitions of 1, each with arbitrary many members, admits a common partition refinement. More precisely the nonzero common coordinate meets of cells join to 1. Put Z=Loc(M), and assume Y has a basis `(b_i)_{i∈I}` of open elements with `|I|≤κ`. We propose the **actual fitted-sublocale formulas**
\[
\boxed{D(Z\times Y)=\Delta_Z\times D(Y),\qquad
D_2(Z\times Y)=\Delta_Z\times D_2(Y).}\tag{D.1}
\]
Consequently W,W₂ multiply, and U multiplies by (C.2).

**Proof.** For any c∈O(Z×Y) and every i define
\[
 u_{c,i}=\bigvee\{m\in M:m\boxtimes b_i\le c\}.
\]
The rectangle basis yields the *canonical coefficient expansion* `c=∨_i(u_{c,i}⊠b_i)`. For an **arbitrary**, possibly uncountable product cover C, fix i and let `u_i=∨_{c∈C}u_{c,i}`. Choose a maximal Boolean partition P_i of 1 such that each cell lies either under ¬u_i or under one of the u_{c,i}, recording that c as a label. (Referee: check choice/maximal-antichain step.) By SDκ choose a common partition P refining every P_i. Fix nonzero m∈P. Whenever the i-cell chosen is not under ¬u_i it has a **label** `c_i∈C` with `m⊠b_i≤c_i`. Let J_m be the set of such indices. For all c, the expansion shows
\[
 (m\boxtimes1)\wedge c\le m\boxtimes\bigvee_{i\in J_m}b_i.
\]
C covers X; therefore `m⊠1≤m⊠∨_{J_m}b_i`. As m is nonzero, the elementary product nonzero test forces `∨_{J_m}b_i=1_Y`. Define
\[
 v_{c,m}=\bigvee\{b_i:i\in J_m,\ c_i=c\}.
\]
Then `∨_{c∈C}v_{c,m}=1_Y` and `m⊠v_{c,m}≤c` for every c. **If C is finite, only finitely many labels c occur:** hence `{v_{c,m}}` is a **finite** Y-cover even if the fiber basis is infinite. Thus the relative sublocale `Δ_Z×D_ε(Y)` matches the C-square on every Boolean base cell m, for ε full or finite. The partition cells cover Z, so the lower D_ε inclusion follows. For the reverse, projection naturality gives `D_ε(Z×Y)≤D_ε(Z)×D_ε(Y)`, and every Boolean frame satisfies `D(Z)=D₂(Z)=Δ_Z` because all opens are complemented. This proves (D.1).

**Concrete application to inspect, NOT an input to the algebraic proof.** Let P be σ-closed atomless forcing of countable partial functions on ω₁ into 2; M=RO(P) is complete atomless and satisfies SDω for **arbitrary-width countably many partitions**, by the standard σ-closed-forcing distributivity theorem. Thus Z=Loc(M) is nonzero and has no ordinary points. The Arrieta construction (Topology Appl. 342 (2024), 108785, Example 4.5) is asserted to give a *second-countable* strongly Hausdorff, anti-Urysohn, noncompact locale A with `W(A)=W₂(A)=U(A)=A²` but `Σ(A)=Δ_A`. If its countable-basis assertion and cited properties hold, (D.1) yields the completely pointless Q-positive example `Z×A` with W=W₂=U but no spanning predecessor core beyond Δ. Referee should independently verify the source example and basis assertion. The Cohen Boolean base RO(Cantor) **fails** SDω; its product with A is a deliberately open test, with no W or W₂ claim made here.

## E. Boolean finite-selection and its coherent frame upgrade

Let L be any frame; M a nonzero **complete Boolean** algebra; h,k:L→M be frame maps such that **every finite L-cover** F satisfies
\[
\bigvee_{c\in F}h(c)\wedge k(c)=1_M.\tag{E.1}
\]
**Claim E.1 (universal bounded-lattice lower selection).** There is a bounded distributive-lattice homomorphism `p_fin:L_lat→M` with `p_fin(a)≤h(a)∧k(a)` for all a. Preservation of *arbitrary* joins is NOT claimed.

**Proof sketch to verify.** Let S be the Stone space of M; since M complete, S is extremally disconnected compact Hausdorff. Let T be the spectrum of **finitely prime** filters of the bounded distributive lattice `L_lat`, with compact Hausdorff patch topology. Restriction of h,k gives patch-continuous maps `H,K:S→T`. At any Boolean ultrafilter s, the intersection H(s)∩K(s) meets **every finite cover** of 1 by (E.1) and finite primeness of s. Therefore the ideal generated by its complement is proper; a prime ideal extension provides a finite-prime filter `P_s⊆H(s)∩K(s)`. The relation
\[
R=\{(s,P):P\subseteq H(s)\cap K(s)\}\subseteq S\times T_{patch}
\]
is closed (a failure is seen by a patch-clopen lattice generator) and surjects onto S. By Gleason projectivity of compact extremally disconnected spaces there is a continuous section of R→S. The resulting patch-continuous selected filter map pulls each clopen compact-open generator of T back to a clopen in S, defining the bounded-lattice p_fin. Its pointwise inclusion gives the desired inequalities. **Do not confuse these filters with completely prime frame points of X.**

If a marked **infinite** cover C has matching value zero, each `h(c)∧k(c)=0`, and so *every* p_fin below both sends each c to zero, whereas p_fin(∨C)=p_fin(1)=1. This is an unavoidable failure of infinite join preservation.

**Claim E.2 (coherent upgrade).** If L is coherent and K(L) its bounded distributive lattice of compact elements, apply Claim E.1 to the restrictions of h,k on **K(L)**. The lattice map p_K:K(L)→M extends to
\[
\boxed{p(a)=\bigvee_{c\in K(L),\ c\le a}p_K(c).}\tag{E.2}
\]
Since `L=Idl(K(L))`, compact generation and finite subcovers of every compact inequality show that p preserves arbitrary joins and finite meets; hence p is a FRAME map, below both h,k. This yields a common generalized specialization predecessor on the Booleanization of D₂(X) for coherent X. Check precisely where coherence, completeness of M, and classical projectivity enter.

## F. Canonical coherent envelope and contact-core lemma

Let `L_lat` be the bounded distributive lattice underlying an arbitrary frame L. Set
\[
\widehat L=\operatorname{Idl}(L_{lat}),\quad
j(a)=\downarrow a,\quad
\varepsilon(J)=\bigvee_{x\in J}x.
\]
**Claim F.1.** `Lhat` is coherent; ε:Lhat→L preserves all joins and finite meets, is surjective, and is left adjoint to the principal ideal inclusion j (which is **only a bounded-lattice** homomorphism). Thus ε corresponds to a sublocale `i:X↪Xhat`. Each finite X-cover F lifts to a finite Xhat-cover of principal ideals, and each finite Xhat-cover restricts via ε to a finite X-cover. Because Xhat is compact, `D(Xhat)=D₂(Xhat)`. By **testing generalized endpoint pairs**, not by assuming pullback commutes with arbitrary sublocale meets, obtain
\[
\boxed{D_2(X)=D(\widehat X)\wedge X^2.}\tag{F.1}
\]
The associated W₂ is closure **inside X²** of the restricted D(Xhat). In general this closure cannot be pulled out across the arbitrary sublocale X²⊆Xhat².

For an X-cover C put `uhat_C=∨_{c∈C}j(c)` and let `R_C=C_Xhat(uhat_C)`. Since ideal joins are finitely generated, R_C>0 iff C has no finite subcover. Since ε(uhat_C)=1, `R_C∧X=0`. Any bounded-lattice p_fin extends to a genuine frame map `p_hat(J)=∨_{a∈J}p_fin(a)` on Lhat. If p_fin annihilates each c∈C, its selected generalized point of Xhat lands in the closed R_C, necessarily outside X.

**Claim F.2 (exact spectral ghost-contact equivalence).** For a,b∈L define the **closed contact core**
\[
K(a,b)=C_X(a^*\vee b^*)=\overline{O_X(a)}\wedge\overline{O_X(b)}.
\]
Let
\[
G_C(a,b)=R_C\wedge\overline{O_{\widehat X}(j(a))}
                 \wedge\overline{O_{\widehat X}(j(b))}.
\]
Then
\[
\boxed{G_C(a,b)>0\ \Longleftrightarrow\
 a^*\vee b^*\vee\bigvee F\ne1_L\quad\text{for every finite }F\subseteq C.}\tag{F.2}
\]
Indeed `(j(a))*=j(a*)`: an ideal J is disjoint from j(a) iff all its members are ≤a*. Thus G_C(a,b) is the closed complement of the ideal generated by `a*,b*` and C; it is nonzero iff that ideal is proper, i.e. iff no finite F has the displayed join 1. Equivalently C has no finite subcover on the closed K(a,b).

**Claim F.3 (localized finite-cover simulation, arbitrary input q).** If `G_C(a,b)=0`, select finite F⊆C with `a*∨b*∨∨F=1`, and form finite cover `H={a*,b*}∪F`. For any q∈O(X²), let `x=(a⊠b)∧(w_C→q)`. The starred squares in w_H miss x and each F-square meets it inside q. Therefore
\[
\boxed{(a\boxtimes b)\wedge(w_C\to q)\le\Phi_2(q).}\tag{F.3}
\]
A compact contact core K(a,b) guarantees G_C(a,b)=0 for every cover C. Thus under rank-one finite stabilization, any U-linked rectangle actually inside a full-cover Q-hole must have **noncompact** contact core and G_C>0. This is a **necessary**, not sufficient, obstruction.

## G. Countercontrols to overinterpretation

**G.1. Strong ghost contact without a Q hole.** Let B be the atomless Boolean locale with frame RO(Cantor), which is noncompact and pointless. Let P be the finite upper-Alexandrov fence with order `0<5>1<4>2<3` (covers are the indicated upsets). Earlier finite-Alexandrov calculations give `W(P)=W₂(P)=U(P)>I(P)` and the pair (0,4) U-linked. For `X=B×P`, compact-fiber transfer (C.5) and universal U products (C.2) yield
\[
 W(X)=W_2(X)=U(X)=\Delta_B\times U(P).
\]
Take `a=1_B×↑0`, `b=1_B×↑4`. They are disjoint and U-linked, but `K(a,b)=B×{1}≅B` is noncompact: `↑0={0,5}`, `↑4={4}`, `cl↑0={0,1,5}`, `cl↑4={1,2,4}`. Choose an infinite maximal Boolean antichain `{v_i}` of B with join 1 and let C consist of the X-opens `v_i×P`. No finite subfamily covers K; by (F.2), G_C(a,b)>0. Nevertheless `w_C→z=z` because X is Q-positive. Thus actual ghost-contact and U-linkage do NOT imply a relatively open hole.

**G.2. Weak infinitely chromatic Boolean defect without Q′ failure.** Let S be the Scott space of nonempty subsets of ω and let `c_n={A:n∈A}`; C={c_n} covers S. The complete Boolean algebra M=RO(Cantor) supports frame maps h,k:O(S)→M with `h(c_n)=[x_n=0]` and `k(c_n)=[x_n=1]`. All finite covers are matched but `∨_n h(c_n)∧k(c_n)=0`. The cross-link graph on C is K_ω, tail opens are dense, and a bounded-lattice predecessor must fail the infinite C-join; the coherent envelope has an external ghost. Yet S is hyperconnected and the previously established relation computation gives `W(S)=W₂(S)=U(S)=S²`. The Boolean defect is **weak**, with no nonzero relatively open full-cover hole. The existence and values of h,k should be checked using their Scott-domain definition, not merely the formal values on generators.

**G.3. Span selection not necessary.** The Arrieta strongly Hausdorff anti-Urysohn example satisfies `Σ(A)=Δ_A` and `W(A)=W₂(A)=U(A)=A²`, although ordinary/global predecessor selection fails on the off-diagonal. Thus predecessor-core density is a sufficient class, not a characterization.

**G.4. Q rank one not closed-hereditary.** If Y is the compact sober two-apex space with `W₂(Y)<U(Y)`, adjoin a generic point p by declaring X-opens to be ∅ and `{p}∪V` with V open in Y. The resulting X is sober hyperconnected, `z_X=0` and `Φ₂,X(z_X)=z_X`, while Y embeds as a closed subspace and its `Φ₂,Y(z_Y)>z_Y`. The claim is unrestricted closed nonheredity, not a T₁-ambient counterexample. A Q-hole's *marked open part* persists after its canonical least closed coordinate-support reduction, but **global** rank-one fixedness on the support is not asserted.

## H. Source map and explicit audit questions

The following are public working source notes. Treat each as a **source for checking**, not as an independent certificate. The suggested review order is D→E→F→C→B, then G and A. All under `https://github.com/mkkinyon/locales/blob/main/`:

- `ProjectA_Q_BOOLEAN_SIGMA_DISTRIBUTIVE_BASE_COUNTABLY_BASED_FIBER_EXACT_TRANSFER_2026-11-12.md` — D, the strong-SDκ theorem and Arrieta product.
- `ProjectA_Q_BOOLEAN_PRIME_PREDECESSOR_SELECTION_INFINITE_JOIN_OBSTRUCTION_2026-11-12.md`; `ProjectA_Q_COHERENT_BOOLEAN_PREDECESSOR_GLEASON_PATCH_SELECTION_2026-11-12.md` — E.
- `ProjectA_Q_COHERENT_ENVELOPE_FINITE_FITTING_AND_GHOST_BOUNDARY_2026-11-12.md`; `ProjectA_Q_SPECTRAL_GHOST_CONTACT_AND_COMPACT_CORE_LOCAL_FINITEIZATION_2026-11-12.md` — F and G.1.
- `ProjectA_Q_POINTFREE_PRODUCTS_URYSOHN_AND_COMPACT_FIBER_TRANSFER_2026-11-12.md`; `ProjectA_Q_GENERALIZED_SPECIALIZATION_SPANS_POINTFREE_FIBER_TRANSFER_2026-11-12.md`; `ProjectA_Q_SEPARATED_SPATIAL_FACTOR_FIBERWISE_CLOSED_HULL_TRANSFER_2026-11-12.md` — C.
- `ProjectA_Q_LOCAL_FINITE_COVERS_PRENUCLEUS_EXACT_INTERCHANGE_2026-11-12.md`; `ProjectA_Q_CHROMATIC_LOCAL_FINITE_AND_COMPACT_FRONTIERS_2026-11-12.md`; `ProjectA_Q_BAIRE_POINTFINITE_RIGIDITY_AND_FAR_REDUNDANCY_2026-11-12.md`; `ProjectA_Q_RANK_ONE_CANTOR_BENDIXSON_PERFECT_CHROMATIC_CORE_2026-11-12.md` — B.
- `ProjectA_Qprime_PRENUCLEUS_BOOLEAN_SUPPORT_IDEMPOTENT_CORE_2026-11-12.md` — A and marked-hole support; the prior historical blind audit has a corrigendum in its repository reconciliation, but please check A independently here.
- Published control: D. Arrieta, *Localic separation and the duality between closedness and fittedness*, **Topology and its Applications 342 (2024), 108785**, Example 4.5. Verify the topology, strong-Hausdorff/anti-U properties and *countable basis* as used in D/G.3.

**Principal adversarial questions:** Is (D.1) valid for arbitrary covers and genuinely about nonclosed D/D₂? Does (E.1) really force a continuous Stonean prime lower selection for arbitrary L, and is (E.2) a legitimate *frame* extension? Does (F.1) hold as actual localic sublocales without an illicit meet/pullback exchange? Is (F.3) valid for every q rather than just rank one? Are the ghost/contact and Scott controls correctly computed? Do B's chromatic/compact/regular and Baire claims have exactly the imported prerequisites they need? Is the relation formula from Arrieta correctly used? Does any claimed positive product contradict an earlier known negative control? Are there shorter or stronger valid formulations? The referee should report substantial gaps and counterexamples even if the overall program is unaffected.

**Final status:** Q and Q′ are not proved. The unresolved object is the **nonzero relatively open** part of a rank-one full-cover implication, not an abstract weak fitting defect or merely a prime point at infinity.