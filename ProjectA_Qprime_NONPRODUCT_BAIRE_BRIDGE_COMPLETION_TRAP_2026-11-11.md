# Project A — Q′ genuinely non-product order coupling: the Baire-completion trap

**11 November 2026 · NEW INTERNAL bounded research, NOT independently refereed and without literature priority check.** Requested after [the bridge-product transfer obstruction](ProjectA_Qprime_bridge_noncompact_product_TRANSFER_NO_GO_2026-11-11.md). We attempt a **non-product dcpo order construction**: replace the two discrete bridge wings of the three-limit/two-bridge example with **noncompact forcing domains**, indexed by their highest occupied coordinate block. The old finite bridge covers can be extended to finite covers, but their traces become dense Scott-open tails. This removes the **discrete tail-exhaustion** argument, yet a more fundamental **Baire-completion trap** makes ordinary full-fitted-diagonal points dense in the very mixed square we sought to preserve.

The concrete P is **noncompact, locally compact, sober, noncontinuous**, its open frame is algebraic but not coherent, and it has an honest **\(\mathcal D(P)<\mathcal D_2(P)\)** defect inherited from a *closed* branching subdomain. Nevertheless \(\mathcal W(P)=\mathcal W_2(P)=\mathcal U(P)=P^2\). Thus the non-product coupling still fails to produce a Q′ gap, for the opposite reason to the product no-go: it rescues the **full** fitted diagonal, not just the finite approximation. Q′ and Q remain open universally.

## 1. General obstruction: Baire bridge completion

For a dcpo P with Scott topology, let \(C_P=\{(s,t):\exists p\le s,t\}\). Every ordinary common-lower pair belongs to \(\operatorname{pt}\mathcal D(P)\): an open cover member containing p contains both endpoints, since Scott opens are upper sets.

**Lemma 1.1 (algebraic Scott Baire lemma; elementary proof).** If S is an algebraic dcpo and \(G_n\subseteq S\) is a countable family of Scott-open dense subsets, then \(\bigcap_nG_n\) is dense in S.

*Proof.* Every nonempty Scott-open contains some principal open ↑k with k compact. Given such k₀, inductively choose compact \(k_{n+1}\ge k_n\) with \(\uparrow k_{n+1}\subseteq \uparrow k_n\cap G_n\). Density ensures the latter Scott-open is nonempty, say it contains s. Algebraicity ensures s is the directed supremum of compacts below it, so a compact q≤s lies in that open; because k_n is compact below s, directedness of the compact approximants below s yields compact k_{n+1}≥q,k_n, still in the open. The supremum \(s_\infty=\sup_n k_n\) belongs to the original ↑k₀ and to every G_n. Hence the intersection meets every nonempty open. □*

This is a special case of the classical Baire/Choquet completeness theorem for continuous Scott domains, but it is supplied self-contained.

**Theorem 1.2 (Baire-completion bridge no-go).** Let P be a dcpo with Scott-open subspaces A,B, each homeomorphic (with Scott topology) to the Scott space of an algebraic dcpo. Suppose there are increasing chains
\[
u_0\le u_1\le\cdots,\quad v_0\le v_1\le\cdots,\quad
\sup_nu_n=\sup_nv_n=z
\]
and each bridge tail
\[
A_n=\{a\in A:u_n\le a\},\qquad
B_n=\{b\in B:v_n\le b\}
\]
is Scott-open and dense in A or B, respectively. Then the common-lower point relation \(C_P\) is dense in the ordinary product \(A\times B\): the sets \(G_A=\bigcap_nA_n\), \(G_B=\bigcap_nB_n\) are dense by Lemma 1.1 and every a∈G_A,b∈G_B satisfies \(z\le a,b\). Thus \(G_A\times G_B\subseteq C_P\).

If **the localic square of P is spatial**, this implies
\[
\boxed{\mathcal W(P)\wedge\mathfrak o(A\times B)=\mathfrak o(A\times B).}
\tag{1.1}
\]
In particular the original aim of preserving a mixed wing region disjoint from W is impossible if the wing opens are contained in the closure of this mixed algebraic-bridge open square. A standard sufficient condition for square spatiality is that the Scott space of P be locally compact sober.

**General version.** The proof requires only that A and B be **Baire topological spaces** (countable intersections of dense opens are dense). Continuous dcpo Scott spaces are Baire by classical Choquet completeness. The algebraic version above avoids this external theorem.

**Scope:** The theorem only forces full-fitted-diagonal *density in the indicated mixed open*; it does NOT prove Q′ universally for all noncontinuous Scott dcpos.

## 2. Explicit non-product decorated bridge dcpo

Let I=ω×ω, partitioned into countably many infinite blocks \(I_k=\{k\}\times\omega\). Let
\[
S=\{s:I\rightharpoonup\{0,1\}:\operatorname{dom}s\ne\varnothing\}
\]
with finite or infinite domains, ordered by extension. It is an algebraic dcpo with finite nonempty partial functions as compact basis. For n∈ω put
\[
T_n=\{s\in S:\exists(k,m)\in\operatorname{dom}s\text{ with }k\ge n+1\}.
\tag{2.1}
\]
Each T_n is Scott-open and dense: extend any finite condition by a fresh literal in a sufficiently high block. They are descending, and
\[
G=\bigcap_nT_n=\{s:\operatorname{dom}s\text{ visits arbitrarily high blocks}\}
\tag{2.2}
\]
is dense (extend any finite condition by one fresh literal in infinitely many blocks).

Construct P from disjoint copies \(A=\{A_s:s\in S\}\), \(B=\{B_s:s\in S\}\), four increasing chains \(x_i,y_i,u_i,v_i\), and three limit elements x,y,z. Their order is the **least partial order** containing:
1. within A and B, the extension orders \(A_s\le A_t\), \(B_s\le B_t\) when s⊆t;
2. \(x_i\le x,\ y_i\le y,\ u_i\le z,\ v_i\le z\), and the increasing chain orders;
3. \(x_i,u_i\le A_s\) iff s∈T_i, and \(y_i,v_i\le B_s\) iff s∈T_i;
4. for s∈G, \(x,z\le A_s\) and \(y,z\le B_s\), as necessitated by directed suprema of the corresponding chains.

Take the **transitive closure**, adding NO comparisons between A and B points. Observe that \(v_i\le A_s\) and \(u_i\le B_s\) are **also** induced when s∈G through z; these are part of the transitive closure and are not to be omitted when checking Scott openness or compactness.

**Lemma 2.1 (P is a dcpo).** Every directed subset D containing an A-point has D∩A cofinal in D, since all points above an A-point lie in A; its supremum is \(A_{\cup\{s:A_s\in D\}}\). Similarly for B. A directed D cannot meet both A and B. A directed D meeting neither is either eventually in one of the x- or y-chains, eventually in one of the u- or v-chains, or contains the relevant limit x,y,z as a greatest point; none of the incomparable chains can be directed together without an A/B upper point in D. Hence every directed D has a supremum.

**Lemma 2.2 (A and B are Scott-open copies of S).** Every directed set with supremum in A (or B) has a member in A (or B), by the cofinality argument. The relative Scott topology equals that of S since directed sets in A and B have the same suprema as in S. Thus the inclusions of A and B are open embeddings, and they are algebraic Scott spaces.

P is **not continuous**: the directed u- and v-chains share supremum z. A way-below p≪z would have to be below members of both chains, but no element is below members of both (check transitive closure: common lower points arise only ABOVE z in complete bridge conditions, never below u_i,v_j). Thus \(\{p:p\ll z\}=\varnothing\).

### 2.1 Compact-open basis and sobriety

Write
\[
X_n=\uparrow x_n
=\{x_i:i\ge n\}\cup\{x\}\cup\{A_s:s\in T_n\},
\quad
Y_n=\uparrow y_n
=\{y_i:i\ge n\}\cup\{y\}\cup\{B_s:s\in T_n\},
\tag{2.3}
\]
\[
Z_{n,m}=\{z\}\cup\{u_i:i\ge n\}\cup\{v_j:j\ge m\}
\cup\{A_s:s\in T_n\}\cup\{B_s:s\in T_m\}.
\tag{2.4}
\]
Together with basic principal Scott opens \(\uparrow A_f,\uparrow B_f\) for **finite nonempty** f∈S, these form a basis for the Scott topology. In particular:
- X_n,Y_n are Scott-open because the tails T_n are Scott-open and the only nontrivial convergences into x,y are their increasing chains;
- Z_{n,m} is Scott-open because of convergences along u and v and the Scott-openness of T_n,T_m on the bridge domains; any directed approximant to a G-point eventually lies in T_n or T_m and hence enters Z_{n,m};
- any Scott-open containing z contains some u_n and v_m, so contains Z_{n,m}; similarly at u_i or v_j, and at x/y use their chain approximants;
- every X_n is a **compact open** (any member of an open cover containing x_n, an element of X_n, contains all of X_n by upward closure); similarly Y_n. Every Z_{n,m} is compact: a cover member containing u_n contains the whole u-tail and A_Tn, and a member containing v_m contains the whole v-tail and B_Tm, so **two** members cover Z_{n,m}. Principal opens of finite A/B conditions are compact because finite conditions are compact in the algebraic Scott domain and their only possible directed approximants with sup in A/B are cofinal within that copy.
Therefore P is locally compact and its Scott-open frame is **algebraic**. It is NOT an algebraic *dcpo* because z has no way-below elements.

**Sobriety.** The open subspaces A and B are sober algebraic-domain Scott spaces. An irreducible closed F meeting A or B has F∩A or F∩B an irreducible closed subset of that sober open subspace; it therefore has a generic point a or b. Since a nonempty relatively open subset of irreducible F is dense in F, one gets F=cl_P{a} or cl_P{b}. If F meets neither open subspace, then it lies in the closed complement C=P\(A∪B). The induced topology on C is the topological sum of the x-chain-with-limit, the y-chain-with-limit, and the two u/v chains with common top z (restrictions of X_n,Y_n,Z_nm are precisely the natural Scott basics). Each summand is sober: in the two-chain z component a nonempty irreducible closed set containing z is cl{z}, while one not containing z must be a finite initial segment of a single chain, otherwise it admits two relatively disjoint nonempty opens. Therefore every nonempty irreducible closed F has a unique generic point. P is sober.

Hence the **localic square is spatial**, represented by the ordinary topological square P×P (locally compact sober product theorem).

### 2.2 Explicit noncompact open cover

Let
\[
A^{(0)}=\{A_s:s\text{ has at least one block-0 literal}\},\quad
B^{(0)}=\{B_s:s\text{ has at least one block-0 literal}\}.
\tag{2.5}
\]
These are open, being unions of Scott-open literal conditions.

The family
\[
\mathcal C=
\{X_0,Y_0,Z_{0,0}\}
\cup\{\uparrow A_\ell,\uparrow B_\ell:\ell\text{ a singleton binary literal in block }I_0\}
\tag{2.6}
\]
covers P. The first three opens cover the three limits, all four chains, and every bridge condition with a positive-block coordinate. The remaining conditions have domain entirely in block 0, and hence are covered by the corresponding literal principal opens. No finite subfamily covers: choose a block-0 singleton literal at a coordinate absent from the finitely many chosen literal opens. Its A-point is not in X_0,Y_0,Z_{0,0} or any chosen literal open. Thus P is **noncompact**.

The open frame is also **noncoherent**: X_0 and Z_{0,0} are compact opens, but their intersection is the open set \(\{A_s:s\in T_0\}\), which is not compact. The cover of this intersection by singleton literal principal opens for coordinates in positive blocks has no finite subcover (choose a fresh positive-block singleton). So compact elements are not meet-stable.

## 3. The old finite bridge covers can be retained, but their trace changes

Put
\[
\mathcal F_n=
\{X_0,Y_0,Z_{0,n},Z_{n,0},A^{(0)},B^{(0)}\}.
\tag{3.1}
\]
This is a **finite** Scott-open cover of P: every bridge s either has a positive-block literal (covered by X_0 or Y_0) or a block-0 literal (covered by A^{(0)} or B^{(0)}); the chains/limits are covered by the X,Y,Z opens.

Let \(M=X_0\times Y_0\) be the target mixed wing open, identified with the corresponding localic open rectangle. The squares of X_0 and Y_0 do not meet M because X_0,Y_0 are disjoint. The squares of A^(0) and B^(0) likewise do not meet M (one coordinate wing only). The Z squares have exact traces
\[
\boxed{
w_{\mathcal F_n}\wedge M
=(A_{T_0}\times B_{T_n})\ \cup\
(A_{T_n}\times B_{T_0}),
}
\tag{3.2}
\]
where \(A_{T_n}=\{A_s:s\in T_n\}\), \(B_{T_n}\) likewise. For n=0 the trace is all of \(A_{T_0}\times B_{T_0}\), a nonempty open sublocale of M. For each n the trace is **dense** in that open because T_n is dense open in S.

This is the critical difference from the original compact bridge dcpo: its trace lay in the discrete isolated-bridge product, and the countable intersection of discrete tail sets was empty; here the trace lies in **non-discrete Scott forcing domains**, and the completed tails have nonempty dense intersection.

In fact the problem is stronger than merely the failure of the old finite-cover argument.

## 4. Dense completed conditions rescue the FULL fitted diagonal

Let G=⋂T_n, dense in S by (2.2). For every s∈G, all u_n≤A_s and all v_n≤B_s. Directed completeness forces
\[
z\le A_s,\qquad z\le B_t\qquad(s,t\in G).
\tag{4.1}
\]
Thus every pair in \(A_G\times B_G\) shares the lower specialization bound z, so is an **ordinary point of the FULL fitted diagonal D(P)**, not merely of D₂.

Moreover \(\uparrow z\) is dense in **all of P**. Indeed any nonempty Scott open meets A or B: a chain point's open neighborhood contains T_n on an appropriate bridge wing, and any open within A or B contains finite conditions extendable to an unbounded-block s∈G. Every such completed bridge point lies above z; neighborhoods of z contain z itself. Therefore every nonempty open meets ↑z.

Consequently
\[
(\uparrow z)\times(\uparrow z)\subseteq\operatorname{pt}\mathcal D(P)
\]
is dense in the ordinary P×P. Spatiality of the localic square and closedness of W yield
\[
\boxed{\mathcal W(P)=\mathcal W_2(P)=\mathcal U(P)=P^2.}
\tag{4.2}
\]

In particular the **entire target mixed square M** lies in W and in the *interior* of U, as opposed to being disjoint from W in the original bridge example. The nonregular Urysohn defect on that rectangle has been completely destroyed, not merely shifted.

This is precisely the opposite failure from the product stabilization: in the product example the old finite cuts still excluded D₂ from M, while here the cuts are too weak and **full D** becomes dense in M.

## 5. Nevertheless there is a genuine infinitary D₂>D defect elsewhere

Let
\[
K=\{A_s:\operatorname{dom}s\subseteq I_0\}
\hookrightarrow P.
\tag{5.1}
\]
Then K is a **Scott-closed lower set** of P. Indeed, a point below A_s for s supported entirely in block 0 must itself be an A_t with nonempty t⊆s: no x/u/v/z chain point lies below such A_s because all chain-to-bridge comparisons require a positive-block coordinate. Directed suprema of elements of K are unions of block-0 conditions, hence remain in K.

Its induced Scott topology is that of the **completed nonempty binary partial-function domain on the countably infinite block I_0**. Our earlier verified Scott/Cantor construction gives
\[
\mathcal D(K)<\mathcal D_2(K).
\tag{5.2}
\]
For completeness, take \(B_0=\operatorname{RO}(2^{I_0})\) and on the Scott opens of K the two frame maps generated by finite-condition cylinders \([s]\) and their bitwise complements \([\bar s]\), followed by double negation. Every finite cover of K is compatible with both, by the infinitely many singleton-condition pigeonhole argument; the infinite singleton-literal cover has zero compatibility value.

Compose these maps with restriction along the **closed** inclusion \(i:K\hookrightarrow P\). The maps remain finite-cover compatible. The P-open family
\[
\{P\setminus K\}
\cup
\{\uparrow A_\ell:\ell\text{ a singleton literal in block }I_0\}
\tag{5.3}
\]
covers P; its restriction to K is precisely the incompatible literal cover, with the first member restricting to zero. Hence the composed generalized pair is **not fully cover compatible**, proving
\[
\boxed{\mathcal D(P)<\mathcal D_2(P).}
\tag{5.4}
\]
This also follows from the previously proved exact closed-sublocale restriction \(\mathcal D_\varepsilon(P)\wedge K^2=\mathcal D_\varepsilon(K)\).

Thus the new genuinely NON-PRODUCT Scott dcpo has
\[
\boxed{
P\text{ noncompact, sober, locally compact, noncontinuous, noncoherent};\
\mathcal D(P)<\mathcal D_2(P),\
\mathcal W(P)=\mathcal W_2(P)=\mathcal U(P)=P^2.
}
\tag{5.5}
\]

## 6. Why the finite-only alternative is not an escape

Suppose instead the bridge wing consists only of the **finite** partial binary conditions, with their upper-Alexandrov topology, and the dense tails T_n. Now the *ordinary* intersection ⋂T_n is empty because no finite condition visits arbitrarily high blocks. This may misleadingly suggest the Baire-completion trap has been evaded.

But a finite-condition upper-Alexandrov space is generally **not sober**. Its sobrification is the ideal completion \(\operatorname{Idl}(S_{\rm fin})\), whose points are directed lower sets of finite conditions. In the present case that is exactly the completed partial-function dcpo S, **including the unbounded-block conditions in G**. The frame of opens, and therefore ALL our localic fitted-diagonal and Urysohn constructions, are unchanged by passing to sobrification. Thus merely deleting the infinitely supported points from the *presentation* cannot delete their locale-theoretic effect.

This is the **sobrification trap** supplementing the Baire-completion trap: finite-condition point calculations risk overlooking precisely the complete generic objects that rescue the full diagonal when the locale is treated correctly. An honest counterexample must evade this mechanism in its **actual sober/locale representation**, not just among the chosen displayed points.

## 7. Outcome and next constraints

This bounded non-product test simultaneously:
- removes the compactness of the old bridge P;
- preserves finite bridge-cover families, but with dense non-discrete tail traces rather than vanishing discrete traces;
- introduces an actual infinitary \(\mathcal D_2>\mathcal D\) defect on a **closed** noncompact Scott subdomain;
- fails to create any Q′ gap because the *full* D becomes dense in the mixed wing and, indeed, throughout P.

**What it rules out:** for countably many bridge demands converging to a **single common supremum**, algebraic (or more generally Baire) Scott forcing wings with dense open tails cannot support a Q′ defect in the mixed wing. They inevitably contain dense completed bridge points above the common supremum. This is a PROVED no-go under the stated hypotheses, not a universal statement about arbitrary nonproduct couplings.

**The remaining design windows** are (i) a genuinely non-Baire bridge sector (possibly a noncontinuous Scott dcpo), and/or (ii) **distributed** boundary suprema instead of one common z, so a single completion cannot become a shared predecessor on a dense set; (iii) a coupling where finite witness traces are non-discrete but FULL diagonal witnesses are nevertheless nowhere dense in the specific finite residual. Neither option is presently realized by a Q′ counterexample.

**Status: NEW INTERNAL mathematics, not externally audited. Q and Q′ remain OPEN.**
