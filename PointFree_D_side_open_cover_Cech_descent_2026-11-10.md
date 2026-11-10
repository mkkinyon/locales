# Point-Free Topology — Dual D-side Čech descent via all-locale open-cover equations

**10 November 2026 · NEW internally checked mathematical segment; NOT independently audited.** Prompted by the second independent referee's **post-report** suggestion #1, after its two-apex nonconstant-suspension suggestion #2 was pursued in [the previous working note](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md). This note proves a stronger all-locale and arbitrary-open-cover statement before specializing to coherent locales and the patched Stone-sheaf homotopy theory. No literature-priority claim. The original independently audited [canonical chain/hull account](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md) and the [two blind audit archives](audits/2026-11-10/README.md) remain the foundation. This new result has **not** been included in a blind referee packet.

## 0. Orientation and definitions

For an arbitrary locale X, put \(\Delta_{n+1}:X\to X^{n+1}\),
\[
\operatorname{Ch}_n(X)=\{x_0\le\dots\le x_n\}\hookrightarrow X^{n+1},
\quad D_n(X)=\operatorname{fit}(\Delta_{n+1})\hookrightarrow X^{n+1}.
\]
The specialization relation A is an actual localic relation presented by \(\pi_0^*a\le\pi_1^*a\) for every \(a\in\mathcal O(X)\). Thus the chain-nerve frame imposes \(\pi_0^*a\le\pi_j^*a\) for every j. Let \(U_i=O(u_i)\hookrightarrow X\) be an open sublocale. For any open U⊆X, define the **relative ambient lower hull**
\[
H_n^{X,\downarrow}(U):=D_n(X)\wedge U^{n+1}\hookrightarrow X^{n+1}.
\]
It can differ strictly from the intrinsic \(D_n(U)\). On the finite V-shaped poset \(z<a,\ z<b\), \(U=\{a,b\}\) is open, and \((a,b)\in H_1^{X,\downarrow}(U)\) by ambient witness z but \((a,b)\notin D_1(U)\).

## 1. The all-locale covering equation, with no coherence or compactness

**THEOREM A (new internally proved).** Let \(X\) be **any locale** and \(\{u_i\}_{i\in I}\subseteq\mathcal O(X)\) be an arbitrary (possibly infinite) open cover, \(\bigvee_i u_i=1\). For each n≥0 set \(w_i=\bigwedge_{j=0}^n\pi_j^*(u_i)\in\mathcal O(X^{n+1})\). Then
\[
\boxed{
\bigvee_i w_i|_{\operatorname{Ch}_n(X)}=1,\qquad
\bigvee_i w_i|_{D_n(X)}=1.
}
\]
Consequently the **open** sublocales \(\operatorname{Ch}_n(U_i)=\operatorname{Ch}_n(X)\wedge U_i^{n+1}\) and \(H_n^{X,\downarrow}(U_i)\) cover respectively \(\operatorname{Ch}_n(X)\) and \(D_n(X)\) in every simplicial degree. Every multiple intersection is \(\operatorname{Ch}_n(U_S)\), respectively \(H_n^{X,\downarrow}(U_S)\), with \(U_S=\bigcap_{i\in S}U_i=O(\bigwedge_{i\in S}u_i)\).

**Proof (pure frame/sublocale).** In Ch_n, the specialization inequalities give \(w_i=\pi_0^*u_i\), hence \(\bigvee_iw_i=\pi_0^*(\bigvee_i u_i)=1\). Put \(w=\bigvee_iw_i\) in \(\mathcal O(X^{n+1})\). Its diagonal pullback is \(\Delta^*(w)=\bigvee_i u_i=1\). Thus \(O(w)\) is an open sublocale containing \(\Delta_{n+1}\). By definition, the fitted hull \(D_n\), the intersection of all open sublocales containing \(\Delta\), lies in \(O(w)\), so \(w|_{D_n}=1\). All intersections follow from product and open-sublocale pullback. Every cover is natural with respect to face and degeneracy maps since all coordinates are required to lie in U. QED.

**Conceptual universal property:** The already audited all-locale fitted-hull frame formula
\[
D_n(X)=\bigwedge_{\bigvee U=1}
O\left(\bigvee_{u\in U}\bigwedge_{j=0}^n\pi_j^*u\right)
\]
means that D_n is **the greatest sublocale of X^(n+1)** on which *every open cover of X induces a cover by products of a common open member*. Thus the new descent theorem is the *cover-localization meaning of fitting*, not a pointwise spectral accident.

**Ordinary localic descent:** For each n the coproduct of open chart inclusions
\(\coprod_i\operatorname{Ch}_n(U_i)\to\operatorname{Ch}_n(X)\), respectively \(\coprod_iH_n^{X,\downarrow}(U_i)\to D_n(X)\), is an open surjection in **Loc**, hence effective descent for locales by Joyal–Tierney (see Reiterman–Tholen 1994 abstract / effective localic open descent). This is about the **open-chart maps**, NOT the independent referee's failed unpatched **lower-witness projection** \(s_q:E_{p,q}\to L_q\). Our statement gives **degreewise localic Čech gluing**, not an unpatched homotopy realization in Loc, for which no chosen ∞-homotopy model has been constructed.

## 2. Coherent finite compact-open specialization and patched homotopy

Suppose X is coherent and \(u_1,\ldots,u_r\in K(X)\) are compact opens with \(\bigvee_i u_i=1\). Then the open sublocales \(U_i=O(u_i)\) and each finite intersection \(U_S=O(\bigwedge_{i\in S}u_i)\) are coherent, and their patches are Stone and **patch-clopen** in Patch X. The relative hull objects are coherent proconstructible spectral, and the open-chart inclusions patch to finite jointly surjective Stone covers.

Let h be sheafified Yoneda into a sufficiently large Stone finite-surjective-cover sheaf ∞-topos H, including finite coproducts and the empty cover. Define
\[
\mathbf C(X)=|h(\operatorname{Patch}\operatorname{Ch}_\bullet(X))|,
\quad\mathbf D(X)=|h(\operatorname{Patch} D_\bullet(X))|.
\]
For each nonempty S⊆[r] define the realized relative ambient lower hull
\[
\mathbf R_X^\downarrow(U_S)=|h(\operatorname{Patch}H_\bullet^{X,\downarrow}(U_S))|.
\]

**THEOREM B (coherent patched dual codescent).** The canonical \(\mathbf C(X)\to\mathbf D(X)\) is the homotopy-colimit of the natural transformation between the **full indexed Čech diagrams**:
\[
\mathbf C(U_S)\longrightarrow\mathbf R_X^\downarrow(U_S).
\]
In particular, if for every nonempty S with U_S≠0 the local arrow is an equivalence, then the **canonical** global arrow \(\mathbf C(X)\to\mathbf D(X)\) is an equivalence. The already independently blind-checked edgewise theorem then implies \(\mathbf C(X)\to\mathbf I(X)\) is also an equivalence.

Proof: Theorem A supplies levelwise open covers. After Patch of the compact-open coherent charts, each family becomes a finite Stone jointly surjective cover, hence its indexed Čech nerve is effective in H. In each Čech degree the intersections are exactly Ch_n(U_S) and \(H_n^{X,\downarrow}(U_S)\). The diagrams are naturally compatible with the chain→D inclusion. Geometric realization in Čech degree commutes with realization in simplicial-chain degree, giving the result, as in the original closed-side codescent. No point-set-only equality of arbitrary sublocales is used. Do not replace the full Čech diagram with a naive poset-indexed colimit without multiplicities.

**Binary Mayer–Vietoris:** For compact-open U,V with U∪V=X,
\[
\mathbf C(U\cap V)\to\mathbf C(U),\quad\mathbf C(V)\to\mathbf C(X)
\]
forms a homotopy-pushout square; likewise replace C(U) by the realized **relative** lower hull R_X^↓(U). These are open-cover gluing statements, not descent of witness projections.

**Good open cover:** If all nonempty U_S are SNC (\(\mathbf C(U_S)\simeq1\)), the same Čech argument gives
\[
\mathbf C(X)\simeq\underline{|N_{\rm open}|},\qquad
N_{\rm open}=\{\varnothing\ne S\subseteq[r]:\bigwedge_{i\in S}u_i\ne0\}.
\]
This is the exact open-cover mirror of the finite closed-downset nerve lemma. If in addition all local relative D-side objects are terminal, the two canonical chain/hull maps are equivalences and each target has the same constant cover-nerve homotopy type.

## 3. Dual compact-open algebra and exact ambient lower-bound criterion

For a nonempty compact open U=O(u) in coherent X,
\[
K(U)\cong[0,u]_{K(X)}.
\]
The local endpoint alternatives are now **order reversed** from the closed-cover theorem:
- If the top u of [0,u] is **join-prime**, U has a **least** specialization point ℓ∈U. This yields \(\mathbf C(U)\simeq1\) and \(H_n^{X,\downarrow}(U)=U^{n+1}\), which realizes to 1.
- If the bottom 0 of [0,u] is **meet-prime**, U has a **greatest** specialization point g∈U. Then its chain nerve is terminal/conical, and the relative ambient **lower** hull is conical at g: for a tuple with lower witness z, adjoining g preserves z≤x_j≤g. Both realize to 1.

Define the **ambient lower-bound condition** for nonzero u∈K(X):
\[
\boxed{(\mathrm{LB})_u:\quad
u\nleq k_1,\ldots,u\nleq k_m
\ \Rightarrow\ k_1\vee\cdots\vee k_m\ne1,\quad m\ge1,~ k_i\in K(X).}
\]
This is a **join-centeredness** condition on the collection \(T^\downarrow_u=\{k\in K:u\nleq k\}\), the compact opens that fail to contain all of U.

**LEMMA C (LB exactness).** For a coherent X and nonempty compact open U=O(u), the following are equivalent:
(i) LB_u.
(ii) There exists a spectral point z∈X satisfying z≤x for **every** x∈U (z may be outside U).
(iii) For all n≥0, \(H_n^{X,\downarrow}(U)=U^{n+1}\) as actual proconstructible spectral sublocales.

Proof (i)⇒(ii): LB says the ideal generated by \(T^\downarrow_u\) is proper. Extend it to a prime ideal J⊂K, and let z be the point corresponding to the prime filter \(K\setminus J\). If z∈k but x∈U\setminus k, then u\nleq k, hence k∈J, contradiction. Therefore z≤x for every x∈U. (ii)⇒(iii): any tuple from U has ambient common lower witness z; equality of proconstructible coherent sublocales follows from patch-point determination. (iii)⇒(i): if u\nleq k_i, choose x_i∈U\setminus k_i (spectral spatiality), and apply (iii) at n=m-1 to obtain a common lower witness z. Because opens are upsets, z lies in no k_i, so \(\bigvee_i k_i\ne1\).

**THEOREM D (dual lower certificate).** Suppose \(u_1,\ldots,u_r\in K(X)\) cover X, \(\bigvee u_i=1\). For every nonzero finite intersection \(u_S=\bigwedge_{i\in S}u_i\), suppose either:
(A) U_S has a **greatest** specialization point, equivalently meet-prime bottom of [0,u_S], or
(B) LB_(u_S) holds and U_S is SNC (certified, e.g., by a finite compact-open good cover or a spectral specialization-zigzag contraction).
Then each \(\mathbf C(U_S)\to\mathbf R_X^\downarrow(U_S)\) is an equivalence, so the canonical global maps to **both** \(\mathbf D(X)\) and \(\mathbf I(X)\) are equivalences.

Explanation: Greatest g conically contracts both simplicial objects; LB+SNC makes relative D-hull into the Čech nerve \(U_S^{\bullet+1}\to1\) and contracts the chain nerve by the stated SNC hypothesis. Least-point alternative is included via LB+SNC, while greatest-point alternative may hold even without any ambient lower bound.

**Duality:** Taking the Priestley order reversal (Hochster dual) on coherent locales exchanges common upper and lower witnesses, sends K(X) to K(X)^{op}, and exchanges finite compact-clopen downset covers with finite compact-clopen upset covers; simplicial chain directions are reversed by the ordinal-order-reversal automorphism. The all-locale Theorem A, however, is stronger and does NOT require this duality or spectral points.

## 4. A direct D-side calculation of the nonconstant suspension

Let S be a nonempty Stone space. Form the Priestley space
\[
Y(S)=S\sqcup\{p,q\},\qquad p<s,\quad q<s\quad(s\in S),
\]
with p,q incomparable, S an equality-ordered antichain, p,q isolated in patch topology. This is the order reversal of the previous [two-apex example](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md). It is a coherent locale.

The two **compact-open upsets**
\[
U_p=S\sqcup\{p\},\qquad U_q=S\sqcup\{q\}
\]
cover Y and intersect at S. Each has **least** point p or q; their chain nerves realize to 1. On the intersection S, the chain realization is \(h(S)\). Therefore, by **open-cover Čech gluing**,
\[
\boxed{\mathbf C(Y(S))\simeq1\amalg_{h(S)}1=\Sigma_{\rm unred} h(S).}
\]
Every tuple in U_p (resp. U_q) has an *internal* common lower witness p (resp. q). Thus \(H_n^{Y,\downarrow}(U_p)=U_p^{n+1}\), similarly q. On S, every tuple has an **ambient** common lower witness p (or q), hence \(H_n^{Y,\downarrow}(S)=S^{n+1}\). Since S is nonempty, the Čech realizations of all three relative simplicial objects are 1. The D-side open-cover diagram therefore gives directly
\[
\boxed{\mathbf D(Y(S))\simeq1,\qquad\mathbf I(Y(S))\simeq1}
\]
(the latter by the previously audited canonical arrow theorem).

For **infinite** S, the previous internal computation of the homology sheaf applies: \(\widetilde{\mathcal H}_1(\mathbf C(Y(S));\mathbb Z)\cong\ker(\mathbb Z[h(S)]\to\mathbb Z)\) is nonconstant; the same nonconstant sheaf appears in degree 2 of the canonical relative homotopy cofibres \(\Sigma_{\rm unred}^2h(S)\). In particular the dual D-side calculation captures the same **genuine sheaf-theoretic obstruction** without deriving D from C→I and the edgewise equivalence.

**Why the local criterion does not apply to this example:** The common open chart S is not SNC when |S|>1, although its **relative D-hull** has terminal realization; thus the local comparison on the overlap is precisely the nontrivial map \(h(S)\to1\). Its failure glues into the global suspension. This is a concrete model for how the relative obstruction is assembled.

## 5. What the theorem proves and what it does not

- **Direct genuine all-locale mathematical advance:** The covering equations for \(\operatorname{Ch}_n\) and \(D_n\) under arbitrary open covers, and the associated degreewise open-locale effective descent. They are essentially formal consequences of the **definition of fitted hull**, so no literature-priority claim.
- **Coherent patched new working theorem:** finite compact-open D-side Čech **codescent of the canonical chain-to-D map**, its open-cover good nerve lemma, and dual lower-bound/endpoint/SNC algebraic certificates.
- **Direct test:** order-reversed two-apex locale Y(S) gives C=Σh(S), D=1; the nonconstancy of Σh(S) for infinite S was separately internally shown in [two-apex note](PointFree_two_apex_nonconstant_sheaf_suspension_2026-11-10.md), not yet independently referee-checked.
- **Distinguish two kinds of descent:** Every degreewise **open chart** family here is effective descent in Loc (Joyal–Tierney); the previously audited common-lower **witness projection** can fail descent. These are different maps.
- **No unwarranted extrapolation:** Open U_i with noncompact frame elements are not necessarily coherent/Stone under Patch, so the full all-locale theorem does not automatically yield a patched Stone-sheaf ∞-topos realization for such covers. The statement in coherent \(\mathscr H\) therefore requires a finite compact-open cover.
- **Future:** Compare the dual and original closed-cover criteria systematically; identify nonconstant families not immediately order-dual to each other; independently audit the all-locale open-cover proof and the nonconstant homology-sheaf argument together before promotion to the verified theorem ledger. The first referee's unpatched descent obstruction is unaffected.

**Literature:** Joyal–Tierney's effective descent theorem for open surjections of locales is stated in Reiterman–Tholen, *Effective descent maps of topological spaces*, Topology Appl. 57 (1994), abstract (https://www.sciencedirect.com/science/article/pii/0166864194900337); also discussed in the 2015 Pitts monads/lax descent paper (https://tcms.org.ge/Journals/ASETMJ/Volume8/Volume8_1/pdf/01%20-%20%5BTbilisi%20Mathematical%20Journal%5D%20Pitts%20monads%20and%20a%20lax%20descent%20theorem.pdf). Standard Priestley/Hochster duality and the audited fitted-diagonal cover presentation complete the ingredients.
