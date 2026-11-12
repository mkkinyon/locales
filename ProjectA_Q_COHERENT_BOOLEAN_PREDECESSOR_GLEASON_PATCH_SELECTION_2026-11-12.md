> **12 NOV 2026 — UNIVERSAL BOUNDED-LATTICE PREDECESSOR STRENGTHENING (NEW INTERNAL).** The Gleason/patch argument in this note actually works for **EVERY** underlying bounded distributive lattice L of an arbitrary frame: finite-cover-compatible Boolean-valued h,k:L→M admit a BOUNDED LATTICE hom \(p_{\rm fin}:L→M\) with \(p_{\rm fin}(a)\le h(a)\wedge k(a)\). Use the spectral PRIME-FILTER spectrum of the whole bounded lattice L, rather than the coherent compact-element lattice K. The selected point filters need NOT be COMPLETELY prime; p_fin need NOT preserve arbitrary joins. A bad infinite cover C with zero matching forces \(p_{\rm fin}(c)=0\) for ALL c∈C but \(p_{\rm fin}(\bigvee C)=p_{\rm fin}(1)=1\): explicit infinitary join failure. In the COHERENT case here, the compact-element K and ideal-completion extension convert the selected K-lattice map to a full FRAME map. Thus the obstacle in rank-one Q lies exactly at FRAME join preservation, not at existence of any Boolean-valued prime lower selection. The same failure occurs on weak Scott D₂>D defects and does not itself settle Q. [Full universal theorem, proof and no-go](ProjectA_Q_BOOLEAN_PRIME_PREDECESSOR_SELECTION_INFINITE_JOIN_OBSTRUCTION_2026-11-12.md). Not externally audited or novelty-checked.

# Project A — Coherent frames: Boolean finite-compatible pairs admit common specialization predecessors (Gleason–patch selection)

**12 November 2026 — NEW INTERNAL working theorem, detailed proof and negative boundary. Not externally audited or literature-priority checked. Universal Question Q and Q′ still OPEN.** This is the next bounded test following [canonical generic-anchor selection on cofinite-apex, two-apex and continuous Scott examples](ProjectA_Q_BOOLEAN_GENERIC_ANCHORS_PREDECESSOR_TESTS_2026-11-12.md). It answers a significant structural question over coherent frames: **EVERY Boolean-valued finite-cover-compatible generalized pair, not only the canonical pair, admits a common generalized specialization predecessor.** The proof uses the classical Gleason theorem that Stonean compact Hausdorff spaces are projective, and the compact Hausdorff patch topology on spectral spaces. These external theorems are classical; the present application to the frame-diagonal setup is internal and not claimed novel.

References:
- Gleason projectivity theorem: https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/Topology/ExtremallyDisconnected.html or the treatment in https://perso.univ-rennes1.fr/bernard.le-stum/bernard.le-stum/Documents_files/CondensedBook.pdf
- Spectral patch topology: https://stacks.math.columbia.edu/download/topology.pdf, spectral spaces §23; also https://link.springer.com/article/10.1007/s00208-024-02952-3, §1.2.
- Dualities are used in classical Set with Boolean ultrafilter/choice, not claimed constructive.

## 0. Definitions and careful scope

Let L be a COHERENT frame: \(K=K(L)\) its sublattice of compact frame elements, with 0,1∈K; K is closed under finite joins/meets; and every \(a\in L\) is the join of compact elements below it. Thus \(L\cong\operatorname{Idl}(K)\). Let M be any nonzero COMPLETE BOOLEAN ALGEBRA, regarded as a locale frame.

Two frame maps h,k:L→M are finite-cover-compatible iff
\[
\boxed{\bigvee_{c\in F} h(c)\wedge k(c)=1_M\quad\text{for every finite frame cover F of L}.}
\tag{0.1}
\]
We ask whether a THIRD frame map p:L→M exists with
\[
\boxed{p(a)\le h(a)\wedge k(a)\quad(\forall a\in L),}
\tag{0.2}
\]
equivalently a generalized locale point p of X below both h,k in the specialization 2-order.

**Theorem 1.1 (coherent Boolean predecessor-selection).** Under the above hypotheses, (0.1) and (0.2) are EQUIVALENT. When they hold, h,k automatically match EVERY (possibly infinite) cover.

No predecessor is claimed for pairs with an ARBITRARY nonBoolean target frame; complete Boolean M is essential to the Stonean selection proof. The theorem is stronger *in witness structure* than the trivial fact that compact frames have D=D₂. It is NOT a proof of universal Q or Q′.

## 1. Boolean Stone representation and spectral patch-valued points

Let \(S=\mathrm{Stone}(M)\), the Stone space of M as a bounded Boolean algebra. Its clopens \(\operatorname{Clop}(S)\) are isomorphic to M. Because M is COMPLETE, S is EXTREMALLY DISCONNECTED (Stonean), hence projective in compact Hausdorff spaces by the Gleason theorem.

Let \(X=\operatorname{Spec}(K)\) with its standard spectral topology, so \(O(X)\cong L\) and its compact opens correspond to K. The **patch** topology on X is compact Hausdorff and ZERO-DIMENSIONAL; every compact open c∈K and its complement are clopen in the patch topology. The specialization order relation
\[
x\preceq y\iff\forall c\in K\ (x\in c\Longrightarrow y\in c)
\tag{1.1}
\]
is CLOSED in the patch product \(X_{\mathrm{patch}}\times X_{\mathrm{patch}}\): its complement is the union over compact c of the clopen conditions x∈c,y∉c.

Restrict h,k to bounded lattice maps \(K\to M\). Stone-Priestley/Hochster duality gives continuous **PATCH** maps
\[
\widehat h,\widehat k:S\to X_{\mathrm{patch}}
\tag{1.2}
\]
specified by
\[
s\in\widehat h^{-1}(c)\iff h(c)\in s,
\qquad
s\in\widehat k^{-1}(c)\iff k(c)\in s
\quad(c\in K),
\tag{1.3}
\]
where s is an ORDINARY Boolean ultrafilter of M. These maps are patch-continuous because the preimages of all compact-open generators c and their patch complements are clopen in S. **No assertion** is made that arbitrary frame elements a∈L pull back to the Stone clopen \(\widehat{h(a)}\): Boolean ultrafilters need not preserve infinite joins! This is the exact reason to use the COMPACT-OPEN lattice K.

## 2. Pointwise finite compatibility produces a common lower point

**Lemma 2.1.** If (0.1) holds, then for EVERY Stone point s∈S, the two spectral points \(x_s=\widehat h(s)\) and \(y_s=\widehat k(s)\) possess an ordinary point \(t_s\in X\) with
\[
t_s\preceq x_s,\qquad t_s\preceq y_s.
\tag{2.1}
\]

*Proof by finite compact refinement.* Suppose no such t_s exists. Then the ordinary closures \(\operatorname{cl}\{x_s\}\) and \(\operatorname{cl}\{y_s\}\) in X are DISJOINT: an element in their intersection is precisely a common specialization predecessor under the order convention (1.1). Consequently
\[
U=X\setminus\operatorname{cl}\{x_s\},\qquad
V=X\setminus\operatorname{cl}\{y_s\}
\]
form a TWO-ELEMENT open cover of X. Since X is coherent/spectral and compact opens form a basis, this cover has a FINITE refinement by compact opens \(c_1,\ldots,c_n\in K\) with \(\bigvee_jc_j=1\), and each c_j≤U or c_j≤V. Thus **no c_j contains BOTH x_s and y_s**.

By finite compatibility,
\[
1_M=\bigvee_{j=1}^n h(c_j)\wedge k(c_j).
\]
An ordinary ultrafilter s of the Boolean algebra M is prime for FINITE joins, so there is j with \(h(c_j)\wedge k(c_j)\in s\). By (1.3), x_s and y_s BOTH lie in c_j, contradiction. Therefore t_s exists. □

This use of finite compact refinements is CRUCCIALLY independent of whether s is a completely prime filter of M. It does NOT infer that ultrafilters preserve arbitrary joins, and it explains why the proof does not automatically extend from coherent frames to arbitrary compact frames.

## 3. Gleason projectivity selects the lower point continuously

Define the subset
\[
R=\{(s,t)\in S\times X_{\mathrm{patch}}:
t\preceq\widehat h(s),\ t\preceq\widehat k(s)\}.
\tag{3.1}
\]
By §1, R is CLOSED in a compact Hausdorff product, hence compact Hausdorff. By Lemma 2.1, the projection
\[
q:R\twoheadrightarrow S
\tag{3.2}
\]
is CONTINUOUS and SURJECTIVE.

Because S is extremally disconnected compact Hausdorff, the Gleason projectivity theorem supplies a continuous SECTION \(\sigma:S\to R\) of q. Define
\[
\widehat p=\pi_X\circ\sigma:S\to X_{\mathrm{patch}}.
\tag{3.3}
\]
Then \(\widehat p\) is patch-continuous, and for every s,
\[
\boxed{\widehat p(s)\preceq\widehat h(s),\widehat k(s).}
\tag{3.4}
\]
This is a **genuine continuous selection**, not a separate choice of t_s at each s: the projectivity theorem is what supplies continuity.

## 4. Extend the selected compact-open truth values to a frame homomorphism

For compact c∈K, the inverse image \(\widehat p^{-1}(c)\) is patch-open AND patch-closed in S, hence represents a unique Boolean element \(p(c)\in M\). Since inverse images preserve finite unions, intersections and 0,1, the resulting
\[
p_K:K\to M
\tag{4.1}
\]
is a bounded distributive lattice homomorphism.

Extend to the entire coherent frame L by
\[
\boxed{p(a)=\bigvee_{\substack{c\in K\\c\le a}}p_K(c).}
\tag{4.2}
\]
This is a FRAME homomorphism:
- for finite meets, use compact generation and \(p_K(c\wedge d)=p_K(c)\wedge p_K(d)\), with c∧d compact;
- for arbitrary joins, if compact c≤∨_i a_i, compactness of c produces finitely many compact subpieces d_j≤a_{i_j} with c≤∨_j d_j; since p_K preserves finite joins, \(p_K(c)≤∨_j p_K(d_j)\), proving preservation of the arbitrary join;
- p(1)=p_K(1)=1 because 1 is compact.

By (3.4), for every c∈K,
\[
\widehat p^{-1}(c)\subseteq\widehat h^{-1}(c)\cap\widehat k^{-1}(c),
\]
hence \(p_K(c)\le h(c)\wedge k(c)\). Taking joins over compact c≤a and using h,k frame homomorphisms yields (0.2) for every a∈L.

This proves the nontrivial direction of Theorem 1.1. Conversely, if p≤h,k then for ANY cover C, \(\bigvee_C h(c)\wedge k(c)\ge\bigvee_Cp(c)=1\). This proves full-cover compatibility and in particular (0.1). □

## 5. Consequences for canonical Booleanization and the specialization-span core

**Corollary 5.1.** For EVERY coherent frame L, let \(Y=\operatorname{Loc}(L)\). Then on the canonical Booleanization \(B(\mathcal D_2(Y))\) the two coordinate frame maps admit a GLOBAL predecessor. Thus
\[
\boxed{B(\mathcal D_2(Y))\le\Sigma(Y),\qquad
\operatorname{cl}\Sigma(Y)=\mathcal W_2(Y)=\mathcal W(Y).}
\tag{5.1}
\]
*Proof.* B(D₂(Y)) is Boolean and contained in D₂(Y), so its canonical coordinate maps match all finite covers. Apply Theorem 1.1 to them. Their induced pair factors through Σ(Y), giving the first inclusion. Since B(D₂) is dense in D₂ and W₂ is its closed hull, Σ is dense in W₂; conversely Σ⊆D⊆D₂. Equality of W and W₂ follows. This equality itself is unsurprising because every coherent frame is compact, but the inclusion \(B(D₂)\le\Sigma\) is extra structure. □

**Corollary 5.2 (global predecessor on B(U) for coherent frames with W₂=U).** If L is coherent AND \(W₂(Y)=U(Y)\), then the canonical pair on \(B(U(Y))\) has a global predecessor. In particular this includes the known coherent class where W=U; and the predecessor property is stronger than that closed-hull equality.

**Corollary 5.3 (product-transfer without selecting ordinary Y-points).** Any coherent Y automatically satisfies the stable span-density hypothesis \(\operatorname{cl}\Sigma(Y)=W₂(Y)\). Therefore the earlier pointfree product-transfer theorem applies over ANY base Z with W₂(Z)=I(Z), even if Z is pointless. In the coherent case Y is compact, so this product conclusion ALREADY follows from the earlier compact-fiber tube lemma; the new content is the global canonical Boolean selection, not a new product class.

## 6. Sharp boundary controls and remaining issue for Q

**Control A: noncompact upper-Alexandrov branching weak defect.** The nonempty finite-partial-binary-function upper-Alexandrov locale P from [the branching control](A-WU-Qprime-Alexandrov-branching-atomless-boundary-2026-10-24.md) has a frame generated by principal compact opens closed under finite meets, but 1 is NOT compact. It admits a Boolean target pair h,k matching EVERY finite cover but failing an infinite singleton-literal cover. Any predecessor p≤h,k would force matching of that infinite cover, impossible. Hence Theorem 1.1 CANNOT be extended to locally coherent NONCOMPACT frames using only finite-cover compatibility. This is an actual negative control and explains why compactness of the TOP is relevant in the coherent proof.

**Control B: compact noncoherent cofinite/two-apex spaces.** The compact cofinite-apex and compact two-apex T₁ examples from [the completed anchor tests](ProjectA_Q_BOOLEAN_GENERIC_ANCHORS_PREDECESSOR_TESTS_2026-11-12.md) are NONCOHERENT but have canonical Boolean predecessor selection on W₂ by a separate generic-anchor argument. Thus coherence is SUFFICIENT but NOT NECESSARY for canonical predecessor selection. It is NOT established here that every finite-compatible Boolean pair into those noncoherent compact frames admits a predecessor; this would be stronger than the canonical result and requires separate study.

**Remaining Q-related test.** To extend the theorem to noncoherent frames under the RANK-ONE assumption W₂=U, one would need a replacement for the patch-continuous Stone maps \(\widehat h,\widehat k:S(M)\to X_{\rm patch}\). For arbitrary opens a∈L, an ultrafilter of the complete Boolean M can contain \(h(\bigvee_i a_i)=\bigvee_i h(a_i)\) while containing NONE of the h(a_i), since Stone ultrafilters preserve only finite joins. This is the exact infinitary obstruction. The branch-Scott weak-defect control shows it is real without rank-one/open-hole hypotheses. Gleason projectivity alone cannot resolve it.

**Status:** new INTERNALLY CHECKED working theorem relying on classical Gleason projectivity and spectral duality; no external mathematical audit or comprehensive literature priority check. Q and Q′ universally OPEN.
