# Project A — Q′ on continuous Scott dcpos: regular-closed Urysohn relation and closed-hereditary collapse

**11 November 2026 · NEW INTERNAL theorem and explicit non-Alexandrov algebraic-domain control. NOT independently audited.** Testing the [closed counterexample self-reduction](ProjectA_Qprime_closed_remainder_HEREDITARY_REDUCTION_REGULAR_2026-11-11.md) in Scott locales of algebraic and continuous dcpos. The result is stronger than Q′: **\(\mathcal W=\mathcal W_2=\mathcal U\)** for the Scott locale of **every continuous dcpo**, and this property holds in every *closed sublocale*. The argument explains the mechanism: the common-specialization-predecessor relation is **open**, and its topological closure equals U. There is no assumption of global directedness, bottom element, compactness, metrizability, or Alexandrov topology. We distinguish dcpo continuity from mere continuity of a frame. Universal Q and Q′ remain OPEN.

## 0. Notation and classical topological assumptions

Let P be a continuous directed-complete partial order (a **continuous dcpo**). Write X=(P,σ(P)) for its Scott space and L=O(X). Its specialization order is the given dcpo order. Standard domain facts:
- Scott opens are upper sets;
- for every p∈P, \(\Uparrow p=\{x:p\ll x\}\) is Scott open, and \(\{\Uparrow p:p∈P\}\) is a basis (some may be empty); every x has at least one p≪x;
- X is **locally compact sober**, hence \(X\times_{\mathrm{Loc}}X\) agrees with the locale of the ordinary product topological space \(X\times X\), which is spatial.
The proof is in classical mathematics (ordinary points and choice); it is NOT a point-free proof for arbitrary frames satisfying a continuous-lattice condition. All sublocale equalities are nonetheless equalities of the actual localic closed relations, not just point-relations, by spatiality of the square and determination of closed sublocales by points.

Recall
\[
\mathcal D_X=\operatorname{fit}(\Delta_X),\qquad
\mathcal D_{2,X}=\bigwedge_{F\text{ finite cover}}\mathfrak o\!\left(\bigvee_{c\in F}c\boxtimes c\right),
\quad
\mathcal W_X=\operatorname{cl}\mathcal D_X,\quad \mathcal W_{2,X}=\operatorname{cl}\mathcal D_{2,X},
\]
and \(\mathcal U_X=C(d_{\mathcal U})\), where
\[
d_{\mathcal U}=
\bigvee_{\substack{a,b\in L\\a^*\vee b^*=1}}
a\boxtimes b.
\tag{0.1}
\]
Here \(a^*\vee b^*=1\) is, for this spatial X, exactly \(\overline a\cap\overline b=\varnothing\).

## 1. The open common-predecessor relation

Define the **common-lower relation** (ordinary point subset)
\[
C_P=\{(x,y)\in P^2:\exists z\in P,\ z\le x,y\}.
\tag{1.1}
\]
The way-below basis gives the exact expression
\[
\boxed{C_P=\bigcup_{p\in P}(\Uparrow p)\times(\Uparrow p).}
\tag{1.2}
\]
If (x,y)∈C_P choose z≤x,y and some p≪z (the nonempty way-below basis at z). Monotonicity gives p≪x,y. Conversely p≪x,y implies p≤x,y. Hence C_P is an **OPEN** subset of the ordinary product, represented by the open element
\[
c_P=\bigvee_{p\in P}(\Uparrow p)\boxtimes(\Uparrow p)
\quad\in L\oplus L.
\tag{1.3}
\]

**Lemma 1.1 (far rectangles are exactly those disjoint from C_P).** For arbitrary Scott opens a,b,
\[
\boxed{(a\times b)\cap C_P=\varnothing\iff
\overline a\cap\overline b=\varnothing.}
\tag{1.4}
\]
*Proof.* If x∈a, y∈b share a lower z, z lies in both closures since z≤x,y and Scott opens are upsets. Conversely if z∈cl a∩cl b, choose p≪z, so the Scott-open neighborhood \(\Uparrow p\ni z\) meets a and b. Choose x∈a∩\Uparrow p,y∈b∩\Uparrow p; both lie above p, giving (x,y)∈C_P∩(a×b). QED.

Since the localic product is spatial and rectangles join-generate its frame, (1.4) says precisely
\[
\boxed{d_{\mathcal U}=c_P^*}
\tag{1.5}
\]
(the largest open disjoint from the open c_P is its pseudocomplement; its rectangular generators are exactly the far rectangles). Thus
\[
\boxed{\mathcal U_X=C(d_{\mathcal U})=\operatorname{cl}(\mathfrak o(c_P))=\overline{C_P}.}
\tag{1.6}
\]
Since the closure of an **open** sublocale is regular closed, equivalently \(d_{\mathcal U}^{**}=d_{\mathcal U}\) by triple pseudocomplement, we get
\[
\boxed{\mathcal U_X=\operatorname{cl}(\operatorname{int}\mathcal U_X).}
\tag{1.7}
\]

## 2. Main theorem and direct proof using regular core

**Theorem 2.1 (Scott continuous-dcpo collapse).** For every continuous dcpo P,
\[
\boxed{\mathcal W_X=\mathcal W_{2,X}=\mathcal U_X=\overline{C_P}.}
\tag{2.1}
\]

*Proof.* The externally checked universal regular-core theorem for all frames gives
\[
\operatorname{cl}(\operatorname{int}\mathcal U_X)
\le\mathcal W_X\le\mathcal W_{2,X}\le\mathcal U_X.
\]
Apply (1.7); the outer terms coincide. QED.

**Independent geometric argument.** Every common-lower pair (x,y)∈C_P is a point of \(\mathcal D_X\): if z≤x,y, every open cover of X has a member containing z and thus, because opens are upward closed, containing both x,y. Hence the point of X² factors through every diagonal cover-open \(\mathfrak o(w_\mathcal C)\). The closed sublocale \(\mathcal W_X\) therefore contains the **topological closure** of C_P, because X² is spatial and closed sublocales are determined by their closed point sets. By (1.6), U≤W, and the universal W≤U supplies equality. This second proof does not use the regular-core inequality but does still rely on Scott-space spatiality of the **localic** square.

**Algebraic case.** Every algebraic dcpo is continuous. If K(P) denotes its compact elements, the open relation formula can be sharpened to
\[
C_P=\bigcup_{k\in K(P)}\uparrow k\times\uparrow k,
\tag{2.2}
\]
because \(\Uparrow k=\uparrow k\) for compact k and every x is a directed supremum of compact approximants. Therefore (2.1) holds for all algebraic dcpos, including those whose Scott topology is *not* Alexandrov.

## 3. CLOSED-hereditary positivity: the self-reduction has no place to start

**Lemma 3.1.** If F⊆P is Scott-closed and nonempty, then F, equipped with the induced order, is itself a **continuous dcpo**, and its Scott topology agrees with the subspace topology from P.

*Proof.* Since F is Scott-closed, it is a lower set closed under directed suprema. Hence every directed subset A⊆F has its supremum in F, so F is a dcpo.

Fix x∈F. The directed family \(B_x=\{p\in P:p\ll_P x\}\) has supremum x. Because F is a lower set, \(B_x\subseteq F\). Moreover p≪_P x implies p≪_F x: for a directed subset A of F, its supremum in F agrees with its supremum in P, and the defining implication for ≪_P applies. Thus every x is the directed supremum of elements way-below x *in F*, so F is continuous.

The induced topology is always no finer than the Scott topology of F: intersections of Scott-opens of P with F are upper and inaccessible by directed suprema in F. Conversely, let O be Scott-open in F and x∈O. The directed approximants \(B_x\) are inside F with supremum x, so some p≪_P x lies in O. Since O is upward-closed in F,
\[
x\in(\Uparrow_P p)\cap F\subseteq O.
\]
Hence every Scott-open of F is a union of restrictions of Scott-opens of P. The topologies agree. QED.

Every **closed sublocale** of the spatial locale X is the locale of a closed topological subspace F, and hence arises in this way. Apply Theorem 2.1 to F:

**Theorem 3.2 (closed-hereditarily Q′, in fact W=U).**
\[
\boxed{
\mathcal W(F)=\mathcal W_2(F)=\mathcal U(F)
\quad\text{for EVERY closed sublocale }F\hookrightarrow X.}
\tag{3.1}
\]
Empty F is trivial. Therefore the previous **closed-counterexample self-reduction** cannot produce a Q′ counterexample from any continuous-dcpo Scott locale, even after arbitrary iterations of passing to closed remainders.

**Caution:** This is not a claim that \(\mathcal W\) commutes with restriction to arbitrary closed sublocales of arbitrary spaces. We re-prove W=U afresh for each Scott-closed F using domain continuity.

## 4. An algebraic, non-Alexandrov dcpo with ALL old patches zero and D<D₂

Let
\[
P=\{\text{partial functions }s:\mathbb N\rightharpoonup\{0,1\},\ \operatorname{dom}(s)\ne\varnothing\}
\]
where **finite OR infinite domains** are allowed, ordered by extension. Directed unions of nonempty partial functions exist and remain nonempty, so P is a dcpo. Its compact elements are precisely nonempty **finite** partial functions; each element is the directed supremum of its finite restrictions, so P is algebraic.

Its Scott-open basis consists of \(\uparrow s\) for finite nonempty s; this is **not Alexandrov**: if x has infinite domain, its principal upset ↑x is not Scott open, since x is the supremum of its finite restrictions and no such restriction belongs to ↑x.

### 4.1 Complete lack of the prior easy patches

There is no nonzero hyperconnected open: every nonempty Scott open contains ↑s for finite s. Choose a fresh coordinate n∉dom(s); the extensions s∪{n↦0},s∪{n↦1} yield two disjoint nonzero principal Scott opens within ↑s. Hence
\[
\boxed{h_{\rm hc}=0.}
\tag{4.1}
\]

There is no nonzero compact-closed-neighborhood strip. For any finite s,
\[
\operatorname{cl}(\uparrow s)
=\{t\in P:t\text{ is compatible with }s\}
\tag{4.2}
\]
(the set is Scott-closed, and every t compatible with s has every Scott neighborhood meeting ↑s by combining a finite restriction of t with s). This closed subspace is **noncompact**: the cover \(\{\uparrow\ell_{n,b}:n\in\mathbb N,b\in2\}\), where \(\ell_{n,b}=\{n\mapsto b\}\), has no finite subcover even when restricted to cl↑s (choose a fresh singleton coordinate outside all listed coordinates and dom s). A compact closed sublocale containing a nonzero open must contain some ↑s and hence its noncompact closed hull, impossible. Thus
\[
\boxed{h_{\rm cc}=0.}
\tag{4.3}
\]

Let \(\mathcal C^\star=\{\uparrow\ell_{n,b}:n\in\mathbb N,b\in2\}\), which is an open cover of P with no finite subcover. For any finite \(F\subseteq\mathcal C^\star\) and nonzero Scott open e, select ↑s⊆e with s finite. Choose n fresh outside dom(s) and all coordinates occurring in F, and let t=ℓ_{n,0}. The point t lies in \(\operatorname{cl}e\) (as compatible with s) but not in \(c_F=\bigvee F\). Thus \(e^*\vee c_F\ne1\), i.e. \(e\not\prec c_F\). Therefore
\[
\boxed{t_{\mathcal C^\star}=0.}
\tag{4.4}
\]
The mixed cover-dependent closed remainder from the preceding programme is **all of P**, not compact, not regular, and not zero-dimensional. To substantiate the last two claims: for **any** nonzero Scott-open v⊆P and any basic open ↑s, choose a finite condition t with ↑t⊆v and a fresh singleton \(\ell_{n,0}\) compatible with t but outside ↑s. The singleton belongs to cl(v) but not to ↑s, so \(v\not\prec\uparrow s\); thus ↑s is not a join of rather-below opens and O(P) is nonregular. Further, every two nonzero Scott opens a,b have intersecting closures by the fresh-singleton/common-lower argument in §4.3; a nontrivial clopen a would give a pair a,a^c of nonzero opens with disjoint closures, impossible. Thus the only clopens are 0 and 1, so P is not zero-dimensional. The new closed-hereditary domain theorem nevertheless proves Q′ for P.

### 4.2 A *genuine* infinite-cover defect D₂>D

Let \(B=\operatorname{RO}(2^\mathbb N)\), the complete Boolean regular-open frame of Cantor space, and j:O(2^N)→B the double-negation quotient. For a finite nonempty binary partial function s let [s] be its Cantor cylinder and \(\bar s\) its bitwise complement on the same finite domain. For Scott-open U⊆P, define
\[
h_+(U)=j\!\left(\bigcup_{\substack{s\text{ finite nonempty}\\\uparrow s\subseteq U}}[s]\right),\qquad
h_-(U)=j\!\left(\bigcup_{\substack{s\text{ finite nonempty}\\\uparrow s\subseteq U}}[\bar s]\right).
\tag{4.5}
\]
These are frame maps. For arbitrary joins, any finite compact condition s in a union of Scott opens already lies in some one, and that open then contains ↑s. For finite meets, [s]∩[t]=[s∪t] when s,t are compatible and is empty otherwise; the same holds for complemented cylinders. Both top images equal 1.

For any **finite cover** \(U_1,\ldots,U_m\) of P, every singleton partial function ℓ_{n,b} belongs to some U_i, hence ↑ℓ_{n,b}⊆U_i. By infinite pigeonhole, one U_i contains infinitely many singleton partial functions on **distinct coordinates**. Its h_+ image includes infinitely many coordinate cylinders [n=b_n], whose union is dense in Cantor space, and its h_- image includes the opposite cylinders [n=1−b_n], also dense. Thus
\[
h_+(U_i)=h_-(U_i)=1_B,
\]
proving **finite-cover compatibility**.

For the **infinite cover** \(\mathcal C^\star\), each c=↑ℓ_{n,b} has
\[
h_+(c)=[n=b],\qquad h_-(c)=[n=1-b],
\quad h_+(c)\wedge h_-(c)=0.
\]
Therefore the pair is not compatible with C*, and
\[
\boxed{\mathcal D(P)<\mathcal D_2(P).}
\tag{4.6}
\]

### 4.3 But the Urysohn relation is the WHOLE square

For any nonempty Scott opens a,b choose finite s,t with ↑s⊆a and ↑t⊆b. Choose a fresh coordinate n outside dom(s)∪dom(t) and let p=ℓ_{n,0}. The (possibly incompatible) extensions s∪p and t∪p lie respectively in a,b and share the common lower p. Thus C_P is **dense** in the ordinary product P². By Theorem 2.1,
\[
\boxed{\mathcal W(P)=\mathcal W_2(P)=\mathcal U(P)=P^2.}
\tag{4.7}
\]
This control has **no** hyperconnected strips, **no** compact-closed patches, and a cover with \(t_\mathcal C=0\), *together with* a truly pointless finite-cover defect D₂>D, yet Q′ holds by the domain-theoretic regular-closedness mechanism. It is a genuine algebraic **dcpo**, not merely the older finite-condition branching **Alexandrov poset** (which was not directed-complete).

## 5. Generalization: a specialization-cone neighborhood condition

The argument of §1 uses a weaker topological hypothesis:

(**Cone-local property**) Let X be a **sober space with spatial localic square**. For every point z∈X, there is an ordinary open N_z containing z and a point p_z with
\[
N_z\subseteq\uparrow p_z
\]
in the specialization order (so *all* points of N_z share the lower specialization bound p_z). It is enough to have **one** such cone neighborhood at each z, not an entire basis.

Then the common-lower relation \(C_X=\{(x,y):\exists z\le x,y\}\) is open: if x,y share lower z, the cone neighborhood N_z contains both (open sets are upward and z≤x,y), so (x,y)∈N_z²⊆C_X. For opens a,b, if cl a∩cl b contains z, N_z meets a and b, giving a common-lower pair in a×b. The converse follows from specialization. Thus the open complement of cl C_X is precisely the far-rectangle join, whence
\[
\mathcal U_X=\operatorname{cl}(C_X)\quad\text{regular closed},\qquad
\mathcal W_X=\mathcal W_{2,X}=\mathcal U_X.
\tag{5.1}
\]
Every continuous dcpo Scott space has this cone-local property via N_z=\Uparrow p for some p≪z. The result also applies to other spatial/localic-square-spatial classes possessing such neighborhoods. **Do not silently assert this for arbitrary locales without points or arbitrary Scott dcpos without the cone-local property.**

## 6. Scope, comparisons, and audit priorities

1. **Algebraic dcpo versus algebraic frame:** An algebraic dcpo P has a Scott-open frame Oσ(P) which is algebraic, but the converse is false. For example, the compact T₁ two-apex space from our October W-phase control has a basis of **compact opens**, so its frame is algebraic/continuous, yet its Urysohn relation is **not regular closed** (\(\mathcal W=\mathcal W_2<\mathcal U\)). It is not the Scott space of a continuous dcpo: its T₁ specialization order is equality, whose Scott topology would be discrete. Thus Theorem 2.1 does **not** claim W=U for all algebraic or continuous *frames*.
2. **The regular-core mechanism is essential:** in the completed branching dcpo §4, the two old strips and rather-below patch are all zero, yet \(\mathcal U=P^2\) is regular closed. So the present positive result has not resolved the hard case of a **nonregular Urysohn boundary** coupled to a finite-cover defect.
3. **Full closure heredity is unclaimed:** the identity of fitted diagonals on closed sublocales is a separate previously proved result; the point here is that the closed K of a continuous dcpo Scott locale is itself a continuous dcpo Scott locale, and Theorem 2.1 can be applied anew. Do not assert cl(D(X))∩K²=cl(D(K)) in general.
4. **External precedents:** the continuity/way-below-basis and local compact sobriety are classical domain theory; the **relation identity and closed-hereditary implication** are internal project deductions, unrefereed and without originality assessment. See Gierz et al. *Continuous Lattices and Domains*, or Lawson/Hofmann–Lawson on continuous domains and spectra.
5. **Audit targets:** (a) equality \(c_P^*=d_{\mathcal U}\) rather than merely equality of their point complements; (b) locality/spatiality of the localic product; (c) inheritance of continuity and Scott topology on closed lower sets; (d) the double-negation Boolean frame-map proof for completed branching P; (e) compactness and rather-below claims in §4.

**Status: NEW INTERNAL proof and test, not independently audited. Q, Q′ remain OPEN in general.**
