> **12 NOV 2026 — POSTERIOR UPDATE: THE POINTLESS BOOLEAN × ARRIETA PRODUCT IS NOW COMPUTED FOR STRONGLY ω-DISTRIBUTIVE BOOLEAN BASES.** The "unknown W/W₂" status below was the state of the test BEFORE a new EXACT (nonclosed) fitted-diagonal product theorem. If Z=Loc(M) and M is STRONGLY COUNTABLY DISTRIBUTIVE (any countable family of arbitrary-cardinality Boolean partitions has common refinement), then because Arrieta's A is SECOND COUNTABLE,
\[
\boxed{D(Z\times A)=\Delta_Z\times D(A),\quad D₂(Z\times A)=\Delta_Z\times D₂(A),\quad W(Z\times A)=W₂(Z\times A)=U(Z\times A)=\Delta_Z\times A².}
\]
For example take M the complete Boolean algebra of σ-closed forcing of countable partial functions \(\omega_1\to2\), a NONZERO POINTLESS base. The product is strongly Hausdorff with empty regular U-core and Σ=Δ, but BOTH Q and Q′ hold, by Boolean partition finiteization; the span and regular-core methods do not prove this. **The original specific COHEN base** M=RO(Cantor) is NOT strongly ω-distributive; its X=Z×A product remains UNKNOWN (particularly \(\Phi_{2,X}(d_U)=d_U\)?). Do NOT interpret the posterior positive result as resolving the Cohen case or universal Q. The exact proof and κ-based generalization are in [Boolean-distributivity × fiber-basis theorem](ProjectA_Q_BOOLEAN_SIGMA_DISTRIBUTIVE_BASE_COUNTABLY_BASED_FIBER_EXACT_TRANSFER_2026-11-12.md). Internal only, pending external audit.

# Project A — Generalized predecessor spans: exact two-apex test, strongly Hausdorff anti-Urysohn no-go, and boundary-only repair

**12 November 2026. Internal mathematical audit segment; source-grounded Arrieta negative control. No claim of novelty, no external referee of the new deductions.** This answers the explicit next test in [the generalized specialization-span note](ProjectA_Q_GENERALIZED_SPECIALIZATION_SPANS_POINTFREE_FIBER_TRANSFER_2026-11-12.md): does the predecessor-span criterion capture **genuinely pointless fitted-diagonal density** in Q/Q′-positive but topologically nonregular examples?

**Answer: two different mechanisms.** The compact T₁ two-apex locale Y (where W=W₂<U) has \(\boxed{\operatorname{cl}\Sigma(Y)=W(Y)=W₂(Y)}\); indeed a SINGLE GLOBAL common predecessor exists for the two canonical coordinate maps on \(B(W₂(Y))\), assembled from the two apex points. However Arrieta's (2024) strongly Hausdorff ANTI-URYSOHN spatial locale A has \(\boxed{\operatorname{cl}\Sigma(A)=\Delta_A=I(A)\ll W(A)=W₂(A)=U(A)=A²}\), despite both Q and Q′ holding. Thus the span criterion is NOT NECESSARY for either equality, even with SPATIAL fibers and pointless fitting density. The correct proposed repair is to require span density only in the **off-inseparability NONREGULAR part** of W₂, because its regular-closed core is already inside W.

## 0. Established framework

Let \(L=O(X)\), \(\mathcal D=\operatorname{fit}\Delta\), \(\mathcal D_2\) the finite-cover fitted diagonal, \(\mathcal W=\operatorname{cl}\mathcal D\), \(\mathcal W_2=\operatorname{cl}\mathcal D_2\), \(\mathcal I=\operatorname{cl}\Delta\), \(\mathcal U\) Urysohn.

A generalized common-predecessor span consists of maps \(r,f,g:T\to X\) such that
\[
r^*(u)\le f^*(u)\wedge g^*(u)\quad \forall u\in O(X).
\]
Its image \((f,g)[T]\) lies in the FULL fitted diagonal \(\mathcal D(X)\) (previous universal span theorem). Let \(\Sigma(X)\) be the join of all these images. Hence
\[
\boxed{\Delta_X\le\Sigma(X)\le\mathcal D(X)\le\mathcal W(X)\le\mathcal W_2(X)\le\mathcal U(X).}
\tag{0.1}
\]

## 1. Generic-apex lemma: a nonspatial common predecessor on a square of a crowded open

**Theorem 1.1 (generic-dense apex span).** Let X be ANY locale, with an ordinary locale point \(p:1\to X\) and a NONZERO open \(v\in O(X)\). Assume
\[
\boxed{p^*(u)=1\implies u\wedge v\text{ is DENSE in }O_X(v)}
\tag{1.1}
\]
for every \(u\in O(X)\). Let \(T=B(O_{X²}(v\boxtimes v))\) be Isbell's least dense Boolean sublocale of the OPEN square v². Let \(f,g:T\to X\) be its two coordinate maps, and \(r:T\to X\) the constant map at p. Then
\[
\boxed{r\preceq f,\qquad r\preceq g,}
\qquad\boxed{T\le\Sigma(X).}
\tag{1.2}
\]
Consequently
\[
\boxed{\operatorname{cl}_{X²}(v\boxtimes v)\le\operatorname{cl}_{X²}\Sigma(X)\le\mathcal W(X).}
\tag{1.3}
\]
Here "cl(v⊠v)" means closure of the corresponding OPEN SUBLOCALE O(v⊠v), equal to C((v⊠v)^*).

*Proof.* If u omits p, then r^*(u)=0. If u contains p, the hypothesis makes u∧v dense in v; hence (u∧v)⊠v and v⊠(u∧v) are DENSE OPENS of the localic square v² (the product-of-dense-sublocales lemma from the preceding product note). By Isbell's density theorem, the least dense Boolean sublocale T of v² lies in each of these open squares. Thus f^*(u)=g^*(u)=1_T. This proves r^*(u)≤f^*(u)∧g^*(u) for all u. Therefore T is a span image and lies inside Σ. It is dense in the open v², proving the closure inequality. □

**Scope:** This is a theorem about generalized-point maps, NOT the ordinary point specialization order. The maps r≼f,g may be STRICT even though X is sober spatial T₁. The dense fitted-diagonal consequence itself often follows already from the universal REGULAR-CLOSED-CORE inclusion if v² lies in U; what is NEW HERE is the **explicit predecessor span** realizing that density.

## 2. The compact T₁ two-apex case: exact W₂-span density and a GLOBAL Boolean predecessor

Recall the VERIFIED October/November control \(X=\mathbb R\cup\{p,q\}\), whose p-neighborhoods contain p and all positive real points but finitely many, and q-neighborhoods analogously contain almost all negative reals. Let
\[
v_+=(0,\infty),\quad v_-=(-\infty,0),\qquad
A_+=[0,\infty)\cup\{p\},\quad A_-=(-\infty,0]\cup\{q\}.
\]
Our established relation calculation is
\[
\boxed{W(X)=W₂(X)=K=A_+²\cup A_-²<U(X)=K\cup\{(p,q),(q,p)\}.}
\tag{2.1}
\]
Here \(A_\pm=\operatorname{cl}_X(v_\pm)\), and closure of products commutes with products, hence
\[
\boxed{\operatorname{cl}(v_+²)=A_+²,\quad
\operatorname{cl}(v_-²)=A_-²,\quad
K=\operatorname{cl}(v_+²\vee v_-²).}
\tag{2.2}
\]
Every p-neighborhood has cofinite trace on the crowded v_+, so it meets v_+ densely. Similarly q and v_-. By Theorem 1.1, \(B(v_+²)\) and \(B(v_-²)\) are generalized predecessor span images, both contained in Σ(X). Their closures exhaust K. With Σ≤W=K we get
\[
\boxed{\operatorname{cl}_{X²}\Sigma(X)=K=W(X)=W₂(X).}
\tag{2.3}
\]
**This is exactly the test of Σ against the canonical W₂**, not against the larger U.

### 2.1 Explicit GLOBAL predecessor on B(K)

Let \(M=O(B(K))\), and \(h,k:O(X)\to M\) be the coordinate frame homomorphisms. Define
\[
m_+=h(v_+)\wedge k(v_+),\qquad
m_-=h(v_-)\wedge k(v_-).
\]
Because the two open squares v_+² and v_-² are disjoint, \(m_+\wedge m_-=0\). Their union is DENSE in K by (2.2); therefore the least dense Boolean sublocale B(K) lies inside that union, so
\[
\boxed{m_+\vee m_-=1_M.}
\tag{2.4}
\]
Define the frame map
\[
\boxed{
r^*(u)=
\bigl(m_+\wedge[p\in u]\,1_M\bigr)\vee
\bigl(m_-\wedge[q\in u]\,1_M\bigr).
}
\tag{2.5}
\]
The bracket is 1_M or 0_M according to the ordinary point test. Because \(m_\pm\) are disjoint and cover 1, the formula is a frame homomorphism (the disjoint sum of constant-point frame maps). Every p-neighborhood u restricts to a dense open of v_+; consequently on the Boolean piece m_+ the coordinate maps h(u),k(u) equal top m_+. Similarly q and m_-. Thus
\[
\boxed{r^*(u)\le h(u)\wedge k(u)\quad\forall u\in O(X).}
\tag{2.6}
\]
The STRONGEST Boolean-predecessor criterion from the preceding note therefore holds for this actual compact T₁ example, even though W₂<U and W₂ carries nontrivial pointless off-diagonal fitted density.

### 2.2 Why the predecessor CANNOT extend to all of U

The relatively OPEN Urysohn piece on the mixed sector
\[
u_+=(0,\infty)\cup\{p\},\quad u_-=(-\infty,0)\cup\{q\}
\]
is the single ordinary point \((p,q)\):
\[
\boxed{U(X)\wedge O(u_+\boxtimes u_-)=\{(p,q)\}.}
\tag{2.7}
\]
No nonzero generalized predecessor span can meet this piece. Indeed, if one did, restrict its source T to the nonzero open inverse image of the piece; f and g become the CONSTANT points p and q. For a generalized predecessor r≤f,g, the opens X\\{p} and X\\{q} (which cover X since p≠q and X is T₁) would both have r-pullback zero, contradicting \(r^*(1)=1\). Therefore Σ avoids the offdiagonal U-atom.

This shows exactly how the generalized predecessor mechanism recognizes K but NOT the two extra U points. It does not suggest an unrestricted Q proof: this X has \(\Phi₂(d_U)>d_U\), so the rank-one antecedent does not hold.

## 3. The decisive NEGATIVE control from Arrieta (2024)

**Source:** Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, *Topology and its Applications* **342** (2024), 108785, [publisher PDF (open access)](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf), especially Corollary 4.3, Proposition 4.4, Example 4.5, and Definition 4.6. We checked the published page 13 screenshot and full text; Arrieta supplies the SPATIAL, classically Hausdorff, STRONGLY HAUSDORFF, ANTI-URYSOHN example. **This example is literature, not ours.**

Let A be Arrieta's nontrivial locale from Example 4.5. Then:
- It is **strongly Hausdorff**, meaning \(\boxed{I(A)=\Delta_A}\) (localic diagonal closed).
- It is **anti-Urysohn**, meaning for nonzero opens \(u,v\), \(u^*\vee v^*\ne1\). Thus \(d_{U(A)}=0\) and \(\boxed{U(A)=A²}\).
- The universal regular-closed Urysohn core theorem implies \(\boxed{W(A)=W₂(A)=U(A)=A²}\): indeed U=A² is trivially REGULAR CLOSED.
- Nevertheless EVERY generalized common-predecessor span is DIAGONAL.

**Theorem 3.1 (strong Hausdorff forces span core = diagonal; new application of standard separation logic).** For ANY strongly Hausdorff locale A (not necessarily spatial), 
\[
\boxed{\Sigma(A)=\Delta_A.}
\tag{3.1}
\]
*Proof.* If p≼f,g:T→A then for any disjoint u,v∈O(A), \(p^*(u)\wedge f^*(v)\le f^*(u)\wedge f^*(v)=0\). Hence the pair (p,f) kills \(d_I=\bigvee_{u∧v=0}u\boxtimes v\), so factors through I(A)=Δ_A. Thus p=f. Likewise p=g. Therefore every span image lies in Δ, and Δ itself is the span \(T=A,p=f=g=\mathrm{id}\), giving equality. □

More generally, the same conclusion holds for any **totally unordered (TU)** locale in the sense of Isbell/Johnstone: any comparable parallel locale maps are equal. But TU is strictly a POINTFREE categorical axiom and must NOT be confused with ordinary spatial T₁. The two-apex example itself fails TU, as witnessed explicitly by r≺f on the Boolean source \(B(v_+²)\): r sends v_+ to 0, while f sends it to top.

Since Arrieta's A is nontrivial and its ordinary topology has many distinct points, \(\Delta_A\) is a PROPER closed sublocale of A². Combining the foregoing:
\[
\boxed{
\operatorname{cl}\Sigma(A)
=I(A)=\Delta_A
\quad\text{but}\quad
W(A)=W₂(A)=U(A)=A².}
\tag{3.2}
\]

**Verdict:** The proposed universal strengthening
\[
\boxed{\text{(false): }W(Y)=W₂(Y)\Rightarrow\operatorname{cl}\Sigma(Y)=W₂(Y)}
\]
fails as dramatically as possible, even for a SPATIAL classical Hausdorff locale. The FULL fitted diagonal D(A) is dense in all A² but its common-predecessor spans are confined to Δ_A. Thus a proof of Q or Q′ cannot consist of universally finding generalized common predecessors on the canonical Boolean W₂ witness, nor can the generalized-span product-transfer theorem remove its density hypothesis.

This is not a Q or Q′ COUNTEREXAMPLE: both equality questions hold on A via the regular-closed-core mechanism. It is a counterexample solely to an OVERSTRONG suggested proof method.

## 4. Repair: regular core + inseparability + generalized predecessor spans

The negative example suggests the correct SCOPE for span density: one need only use spans on the part of W₂ not already covered by the regular-closed core and I. Let
\[
K_{\mathrm{reg}}(X)=\operatorname{cl}(\operatorname{int}W₂(X)).
\]
The universal intersection-closure theorem from October yields
\[
\boxed{K_{\mathrm{reg}}(X)\le\operatorname{cl}(\operatorname{int}U(X))\le W(X).}
\tag{4.1}
\]
Of course I(X)≤W(X) and cl Σ(X)≤W(X).

**Proposition 4.1 (boundary-only predecessor sufficient criterion).** For ANY locale X,
\[
\boxed{
W₂(X)
\le I(X)\vee K_{\mathrm{reg}}(X)\vee\operatorname{cl}\Sigma(X)
\quad\Longrightarrow\quad W(X)=W₂(X).
}
\tag{4.2}
\]
*Proof.* Each of the three terms on the right lies below W(X), so the hypothesis gives W₂≤W; reverse inclusion universal. □

Under rank-one fixedness W₂=U, the same criterion proves Q, and only the NONREGULAR OFF-INSEPARABILITY sector \(G_\perp=U\wedge O(d_U^{**}\wedge d_I)\) could require span input. In the Arrieta example \(K_{\mathrm{reg}}=U=A²\), so the criterion is automatically satisfied even though Σ=Δ. In the compact two-apex example W₂=K is regular closed, so it is also automatically satisfied, though the explicit spans give a finer decomposition of its dense fitting.

**IMPORTANT HONESTY CHECK:** (4.2) is only a **sufficient criterion assembled from already known positive mechanisms**, not a new characterization. The Arrieta example shows the global Boolean-predecessor selection criterion is far too strong; restricting it to the exceptional boundary is necessary before using it in any attempted Q proof. NO proof is given that span images are dense on that boundary under finite rank-one stabilization. That remains open.

### 4.2 Nonregular Q-positive SUCCESS with genuinely nonzero exceptional boundary: Cantor or pointless Boolean base × finite fence

The two-apex test in §2 has W₂ regular closed; the Arrieta negative control in §3 has U regular closed. We must ALSO check a Q-positive locale with a NONZERO off-inseparability NONREGULAR sector, lest the specialization-span method appear to be only another form of the old regular-core argument.

Take P the finite upper-Alexandrov six-point fence \(0<5>1<4>2<3\), with
\[
\operatorname{cl}(\mathrm{Cm}(P))=W(P)=W₂(P)=U(P)>I(P).
\]
Let Z be EITHER ordinary Cantor space (SPATIAL, perfect and U-separated) OR the complete atomless Boolean locale \(B=\operatorname{Loc}(\operatorname{RO}(2^\omega))\) (POINTLESS, U-separated). Put Y=Z×P. For both bases, the earlier spatial-product or compact-fiber theorem gives
\[
\boxed{W(Y)=W₂(Y)=U(Y)=\Delta_Z\times U(P),\quad I(Y)=\Delta_Z\times I(P).}
\tag{4.2a}
\]
Since Z has no diagonal interior (Cantor is perfect; atomless Boolean proved below), \(\operatorname{int}U(Y)=0\), and \(G_\perp=U(Y)\wedge O(d_I)\ne0\) because U(P)>I(P). Thus **the entire nontrivial off-I sector is NONREGULAR** in the ambient square, yet Q holds.

Now for every ordinary common-predecessor pair (s,t)∈Cm(P), choose r∈P with r≤s,t, and use source T=Z with frame maps
\[
z\mapsto(z,r),\quad z\mapsto(z,s),\quad z\mapsto(z,t)
\]
from Z to Y. These form an ACTUAL generalized predecessor span. The image of the pair maps is \(\Delta_Z\times\{(s,t)\}\), and their joins are DENSE in \(\Delta_Z\times U(P)\) because Cm(P) is dense in U(P). Therefore
\[
\boxed{\operatorname{cl}\Sigma(Y)=W(Y)=W₂(Y)=U(Y)}
\tag{4.2b}
\]
with G_perp nonzero, even if the base Z (and hence Y) is ENTIRELY POINTLESS.

This is a genuine **positive** test of predecessor spans on the difficult nonregular off-I sector, unlike the merely regular-closed-core two-apex and Arrieta examples. It is not a NEW positive Q result (the product formulas already prove it), but it verifies that the method can handle exactly the right kind of geometry when the fiber has common-lower-bound specialization links.

### 4.3 A genuinely exposed rank-one test: pointless Boolean base × Arrieta's anti-Urysohn locale

Set \(Z=\operatorname{Loc}(\operatorname{RO}(2^\omega))\), a nonzero POINTLESS, atomless Boolean locale; let A be Arrieta's strongly Hausdorff anti-Urysohn locale. Put \(X=Z\times A\). We can PROVE all the following facts without knowing W(X) or W₂(X):

**Proposition 4.3 (pointfree rank-one stress test).**
\[
\boxed{
I(X)=\Delta_X,\quad
\Sigma(X)=\Delta_X,\quad
U(X)=\Delta_Z\times A²,\quad
\operatorname{int}_{X²}U(X)=0,\quad
U(X)>I(X).
}
\tag{4.3}
\]

*Proof.* Z is Boolean, so \(I(Z)=U(Z)=\Delta_Z\); A is strongly Hausdorff and anti-Urysohn, so \(I(A)=\Delta_A\), \(U(A)=A²\). The UNIVERSAL pointfree I/U product theorems give
\[
I(X)=\Delta_Z\times\Delta_A=\Delta_X,\qquad
U(X)=\Delta_Z\times A².
\]
Strong Hausdorffness of X implies Σ(X)=Δ_X by Theorem 3.1.

To show the interior is zero, first note that the diagonal \(\Delta_Z\) of an ATOMLESS Boolean locale has zero interior. For any nonzero pure rectangle \(a\boxtimes b\in O(Z²)\), either \(a\wedge b=0\), in which case it already misses Δ, or \(a\wedge b>0\), in which case split this element into two disjoint nonzero Boolean pieces \(c,d\le a\wedge b\), so \(0<c\boxtimes d\le a\boxtimes b\) is disjoint from Δ. Thus no nonzero pure rectangle lies under the diagonal, giving \(\operatorname{int}\Delta_Z=0\). The same rectangle argument in \(Z²\times A²\) shows \(\operatorname{int}(\Delta_Z\times A²)=0\). Finally A is ordinary Hausdorff with distinct points, hence has nonzero disjoint opens a,b, and the product \(\Delta_Z\times O_{A²}(a\boxtimes b)\) is nonzero inside U(X) but outside I(X). □

This is a **concrete off-inseparability entirely nonregular Urysohn sector** in a locale with no ordinary points. Neither the regular core nor any generalized predecessor spans can fill it, since
\[
\boxed{\operatorname{cl}(\operatorname{int}U(X))=0,\qquad
\operatorname{cl}\Sigma(X)=I(X)=\Delta_X.}
\]
There is NO claim that the sector lies in W₂(X): that is the **EXACT OPEN calculation**.

**Explicit rank-one test in the product frame.** Let \(Q_X=O(X²)\) and \(e=d_{\Delta_Z}\boxtimes1_{A²}=d_{U(X)}\). Then
\[
\boxed{W₂(X)=U(X)\iff\Phi_{2,X}(e)=e.}
\tag{4.4}
\]
The full question on this X is whether \(\Phi_X(e)=e\). We have NOT established either equality. If \(\Phi_{2,X}(e)=e\) but \(\Phi_X(e)>e\), this X would provide a Q counterexample; if both are fixed, it would give a genuinely POINTLESS example requiring a positive mechanism beyond the regular core and specialization spans. If \(\Phi_{2,X}(e)>e\), the original Q antecedent fails and the result would still test rank-one preservation under pointfree products.

**Discipline:** Arrieta's construction is an imported literature control, not a new candidate claimed to work; (4.3) is proved, (4.4) is an equivalent TARGET, and no rank-one result on X is asserted. This is a much sharper next test than continuing to pile necessary conditions onto generic Q holes.

## 5. Research decision

- **Two-apex success:** The generalized-span method is genuine; it recovers exactly the positive and negative cofinite-apex W₂ geometry, with explicit Boolean-valued comparable maps despite the T₁ property.
- **Arrieta no-go:** It does NOT capture all pointless fitted-diagonal density, even when W=W₂=U and the locale is spatial. Thus our proposed general pointfree noncompact-fiber product transfer still needs a method for unspanned, relatively open density.
- **Correct localization:** We should not expect a predecessor on all of B(U) or B(W₂); focus any future span criterion on the nonregular off-I sector where the regular core and I cannot already explain equality.
- **Next discriminating test:** Analyze whether Arrieta's strongly Hausdorff anti-Urysohn A, combined with a pointless separated base B, preserves W=W₂=U after product. The universal product formula gives \(U(B\times A)=\Delta_B\times A²\); the stable-span theorem offers NO lower bound beyond Δ_B×Δ_A. This is the precise gap left by the point-free noncompact-fiber program. If the product equality can be proved, it would require a new mechanism beyond both compact tube covers and generalized specialization spans.

**STATUS: internal new deductions; primary literature example sourced. No claim of universal Q/Q′ resolution.**
