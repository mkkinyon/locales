# Project A — Spectral ghost-contact supports and compact contact-core finiteization: a bounded test toward Q

**12 November 2026 — NEW INTERNAL working deductions, not independently audited and no literature-priority claim. Both Q and Q′ remain OPEN.**

**Motivation.** In the preceding coherent-envelope note [ProjectA_Q_COHERENT_ENVELOPE_FINITE_FITTING_AND_GHOST_BOUNDARY_2026-11-12.md](ProjectA_Q_COHERENT_ENVELOPE_FINITE_FITTING_AND_GHOST_BOUNDARY_2026-11-12.md) a Boolean finite-compatible pair with a bad full cover C admits a selected *prime* predecessor, which becomes a genuine locale map into a nonzero CLOSED spectral remainder R_C disjoint from X. Does this boundary constrain the NONZERO RELATIVE INTERIOR of a canonical Q-hole? We test one *open rectangle* rather than invent another global spectral invariant.

**Outcome.** An exact equivalence identifies which ordinary X-open rectangles the ghost boundary can touch: a contact core K(a,b) has no finite C-subcover precisely when the ghost remainder meets the closures of the two lifted opens. This gives a useful **finite-cover simulation for every pre-nucleus input q** whenever the contact core is compact. A hypothetical rank-one Q-hole must therefore have only **noncompact contact cores** on its linked disjoint rectangular patches. But this last condition occurs even in known Q-positive, entirely pointless noncompact examples, so the argument does NOT resolve Q; the spectral condition proves no further contradiction beyond a particular finite-cover obstruction. That is the bounded honest outcome of the test.

## 0. Notation

Let L=O(X) and \(P=L\oplus L=O(X²)\). For a frame cover C let
\[
w_C=\bigvee_{c\in C}c\boxtimes c,\qquad
\Phi(q)=\bigvee_{C\mathrm{\ cover}}(w_C\to q),\qquad
\Phi_2(q)=\bigvee_{F\mathrm{\ finite\ cover}}(w_F\to q).
\]
Let \(z_1=d_{\mathcal U(X)}=\Phi(0)=\Phi_2(0)\). The rank-one question Q is \(\Phi_2(z_1)=z_1\Rightarrow\Phi(z_1)=z_1\).

As before, let \(\widehat L=\operatorname{Idl}(L_{\rm lat})\), \(\widehat X=\operatorname{Loc}(\widehat L)\) be the coherent envelope, and \(j(a)=\downarrow a\in\widehat L\). For C define
\[
\widehat u_C=\bigvee_{c\in C}j(c),\quad
R_C=\mathfrak c_{\widehat X}(\widehat u_C).
\]
The closed contact core of a,b∈L is
\[
\boxed{K(a,b)=\mathfrak c_X(a^*\vee b^*)
=\operatorname{cl}_X\mathfrak o(a)\wedge\operatorname{cl}_X\mathfrak o(b).}
\tag{0.1}
\]
In ordinary spatial terms, its point set is \(\overline a\cap\overline b\). All following sublocale equations are localic; no spatiality is needed.

## 1. Exact ghost-contact equivalence

**Lemma 1.1 (principal-ideal pseudocomplement).** In \(\widehat L\),
\[
\boxed{j(a)^*=j(a^*).}
\tag{1.1}
\]
*Proof.* An ideal J has J∧j(a)=0_{\widehat L}=j(0) iff each x∈J satisfies x∧a=0, iff J⊆↓a*=j(a*). This characterizes the largest ideal disjoint from j(a). □

Define the closed spectral ghost-contact sublocale
\[
\boxed{G_C(a,b)=
R_C\wedge\operatorname{cl}_{\widehat X}\mathfrak o(j(a))
\wedge\operatorname{cl}_{\widehat X}\mathfrak o(j(b)).}
\tag{1.2}
\]

**Theorem 1.2 (ghost contact iff no finite contact-core cover).** For any L,a,b,C as above,
\[
\boxed{
G_C(a,b)\ne0
\iff
a^*\vee b^*\vee\bigvee F\ne1_L
\quad\text{for EVERY finite }F\subseteq C.
}
\tag{1.3}
\]
*Proof.* Closure of a principal open is the closed sublocale defined by its pseudocomplement. By (1.1) and closed-sublocale meet,
\[
G_C(a,b)=
\mathfrak c_{\widehat X}
\bigl(\widehat u_C\vee j(a^*)\vee j(b^*)\bigr).
\]
This is nonzero iff the displayed join of IDEALS is proper, i.e. its ideal does not contain the element 1_L. By the finite-join generation of ideal joins, this is equivalent to NO finite F⊂C satisfying \(a^*\vee b^*\vee\bigvee F=1_L\). □

**Equivalent locale formulation.** For e=a*∨b*, the restricted family C|K(a,b) is an open cover of the closed locale K(a,b)=c(e). Equation (1.3) says it has NO FINITE subcover. Thus G_C(a,b) detects a *specific contact-core compactness failure*, rather than a new kind of pointfree separation. A nonzero external ghost boundary alone need not have nonzero G_C(a,b), e.g. the discrete X=N control.

## 2. Compact contact cores finiteize EVERY full-cover pre-nucleus step on the rectangle

**Theorem 2.1 (local compact-contact simulation).** For arbitrary q∈P, cover C, and opens a,b with K(a,b) COMPACT,
\[
\boxed{
(a\boxtimes b)\wedge(w_C\to q)\le\Phi_2(q).
}
\tag{2.1}
\]

*Proof.* Since C|K(a,b) covers the compact closed locale K(a,b), there exists finite F⊂C such that
\[
\boxed{a^*\vee b^*\vee\bigvee F=1_L.}
\]
Hence \(H=\{a^*,b^*\}\cup F\) is a FINITE cover of X. Put x=(a⊠b)∧(w_C→q). Then
\[
x\wedge(a^*\boxtimes a^*)=0
\quad\text{and}\quad
x\wedge(b^*\boxtimes b^*)=0.
\]
For each c∈F⊂C,
\[
x\wedge(c\boxtimes c)\le(w_C\to q)\wedge w_C\le q.
\]
Therefore x∧w_H≤q, giving \(x\le(w_H\to q)\le\Phi_2(q)\). □

**Exact noncompact variant.** The same conclusion holds without compactness whenever THIS PARTICULAR cover C has a finite F satisfying \(a^*\vee b^*\vee\bigvee F=1\). By Theorem 1.2 this is exactly the condition \(G_C(a,b)=0\). Thus:
\[
\boxed{
G_C(a,b)=0
\Longrightarrow
(a\boxtimes b)\wedge(w_C\to q)\le\Phi_2(q),
\quad\text{ALL }q.
}
\tag{2.2}
\]
This is the promised precise bridge from the spectral remainder to *one finite-cover implication*. It is NOT the universal rank-one implication Q because G_C(a,b) can be nonzero.

**Monotonicity.** If a'≤a and b'≤b, then \(a'^*\ge a^*, b'^*\ge b^*\), so
\(K(a',b')\le K(a,b)\) as a CLOSED sublocale. Thus compactness of K(a,b) passes to all smaller rectangular patches (closed sublocales of compact locales are compact).

## 3. Consequences for a hypothetical rank-one Q-hole

Assume \(\Phi_2(z_1)=z_1\) but a cover C has \(\rho_C=w_C\to z_1\not\le z_1\). Since elementary rectangles join-generate P, choose a,b with
\[
r=a\boxtimes b\le\rho_C,\qquad
r\not\le z_1.
\tag{3.1}
\]
Since every cover square pulls back to 1 along the diagonal \(\delta:X\to X²\), while \(\delta^*z_1=0\),
\[
\delta^*\rho_C
\le(\delta^*w_C\to\delta^*z_1)
=(1\to0)=0,
\tag{3.2}
\]
so any rectangle r≤ρ has \(a\wedge b=0\). The condition \(r\not\le z_1\) says \(\mathcal U(X)\wedge\mathfrak o(r)\ne0\). Thus r is an actual **disjoint but U-linked rectangle** inside the canonical OPEN hole.

By (2.2), if G_C(a,b)=0 then r≤Φ₂(z_1)=z_1, contradiction. Hence:
\[
\boxed{
a\wedge b=0,\quad
r\wedge\mathcal U(X)\ne0,\quad
G_C(a,b)\ne0,\quad
K(a,b)\text{ is NONCOMPACT}.}
\tag{3.3}
\]
The same holds for EVERY further nonzero U-linked rectangular refinement inside rho_C, not just the selected r.

**Corollary 3.1 (compact-contact positive Q class).** If for every disjoint a,b with \(U(X)\wedge O(a\boxtimes b)\ne0\) the contact core K(a,b) is COMPACT, then Q HOLDS on X.

*Proof.* A hypothetical Q-hole produces an r satisfying (3.3), contradicting the assumed compactness. □

**Local version.** It suffices that the relatively open U-rectangle patches with compact K(a,b) be DENSE in the off-inseparability nonregular sector \(G_\perp\) previously identified as containing EVERY Q-hole. Indeed a nonzero relatively open hole meets a compact-core patch; refine to a nonzero U-rectangle lying inside both the hole and the patch. The contact core of the refinement is a closed sublocale of the original compact core, hence compact; Theorem 2.1 then contradicts finite stabilization. This is another sufficient positive criterion, NOT claimed necessary.

## 4. How the Boolean ghost map localizes on each open rectangle

Let h,k:L→M be any Boolean-valued finite-cover-compatible generalized pair with C matching zero. By the previous Gleason theorem, choose a bounded-lattice predecessor \(p_{\rm fin}\le h,k\) and its envelope extension \(\widehat p:\widehat L\to M\), landing in R_C.

For a,b∈L set \(m=h(a)\wedge k(b)\). If m>0, restrict the target Boolean locale to ↓m. On that piece
\[
h_m(a)=m,\quad k_m(b)=m,\quad
p_m(a^*)\le h_m(a^*)=0,\quad
p_m(b^*)\le k_m(b^*)=0.
\]
The marked C-values also vanish. By Lemma 1.1 the restricted envelope map factors through
\[
\boxed{\widehat p|_m:\operatorname{Loc}(\downarrow m)\to G_C(a,b).}
\tag{4.1}
\]
Thus \(G_C(a,b)\ne0\) whenever the pair gives a nonzero local Boolean value to the oriented rectangle a⊠b. The compact-contact finiteization theorem is exactly the corresponding frame-level obstruction to this situation.

For a genuine Q-hole \(E_C=U(X)\wedge O(\rho_C)>0\), its Booleanization B(E_C) is DENSE in the relatively open hole. Every nonzero U-linked rectangle inside rho_C meets B(E_C), so (4.1) holds on a NONZERO Boolean patch for every such rectangle. This is the strongest *new spectral interpretation* of the RELATIVE OPENNESS we have extracted: ghost-contact support occurs locally throughout the open hole.

**But caution:** The same ghost-localization argument holds for any nonzero OPEN portion of the canonical weak fitting-defect sublocale T_C (which need not be open in W₂); no contradiction follows merely from the existence of \(\widehat p|_m\). The original Q condition still asks whether such weak defects can be somewhere dense in U under rank-one stabilization.

## 5. An explicit Q-positive countercontrol to NECESSITY of compact contact

Let B be the complete atomless Boolean locale with frame RO(Cantor), so every nonzero clopen sublocale O_B(u) is NONCOMPACT. Let P be the finite six-point upper-Alexandrov fence
\[
0<5>1<4>2<3.
\]
The earlier internally computed relation formulas give
\(W(P)=W₂(P)=U(P)>I(P)\) and (0,4)∈U(P)\\I(P).
For \(X=B\times P\), the previous compact-fiber transfer gives
\[
\boxed{W(X)=W₂(X)=U(X)=\Delta_B\times U(P).}
\tag{5.1}
\]
So Q holds, and X is noncompact and has NO ordinary points.

Fix any nonzero u∈O(B). In X let
\[
a=u\boxtimes\uparrow0,\qquad b=u\boxtimes\uparrow4.
\]
Since ↑0={0,5} and ↑4={4}, \(a\wedge b=0\), and \(a\boxtimes b\) is genuinely U-linked via (0,4) and the nonzero B-diagonal over u. However the contact core is
\[
\boxed{
K(a,b)
=\overline a\cap\overline b
=u\times(\operatorname{cl}_P\uparrow0\cap\operatorname{cl}_P\uparrow4)
=u\times\{1\}.
}
\tag{5.2}
\]
The intersection in P is exactly {1}, since cl ↑0={0,1,5}, cl ↑4={1,2,4}. Consequently K(a,b)≅O_B(u), NONCOMPACT. Thus a noncompact contact core on a U-linked DISJOINT rectangle does occur in a Q-POSITIVE nonregular pointless locale.

**Explicit nonzero ghost contact with NO Q-hole (stronger control).** Fix u=1_B, and choose an INFINITE maximal antichain \(\{v_i:i\in I\}\) of nonzero Boolean elements of B with \(\bigvee_i v_i=1_B\); this is possible in an atomless COMPLETE Boolean algebra. Put
\[
C=\{v_i\boxtimes1_P:i\in I\},
\]
a genuine X-open cover. For a=1_B⊠↑0, b=1_B⊠↑4, the contact core is \(K(a,b)=B\times\{1\}\cong B\). The restrictions of the C-members to K form the antichain cover of B with NO finite subcover. Thus by Theorem 1.2,
\[
\boxed{G_C(a,b)\ne0}
\]
even though a⊠b is genuinely U-linked and disjoint. But \(W(X)=W₂(X)=U(X)\), so finite rank-one fixedness and full rank-one fixedness BOTH hold, and therefore \(\boxed{w_C\to z_1=z_1}\); in particular \(a\boxtimes b\not\le w_C\to z_1\). This falsifies the inference
"an actual U-linked disjoint rectangle PLUS a nonzero spectral ghost-contact implies a full-cover open hole." The contact obstruction is necessary for a hole but has no power to force the **relative openness** of a defect.

This does not disprove Corollary 3.1 (only sufficiency was claimed). It does show that the failure of contact compactness, or nonzero spectral ghost-contact for suitable infinite covers, is not alone a route to a counterexample. A Q proof cannot presume every U-linked patch has compact closure-contact.

## 6. Outcome and stop rule

**What worked:** The spectral ghost remainder has an EXACT rectangle contact criterion (1.3); if that ghost-contact vanishes, the corresponding full-cover pre-nucleus implication can be replaced by ONE FINITE-cover implication at EVERY input q, (2.2). Compactness of the closed contact core ensures this and yields a transparent Q-positive class.

**What did not work:** The coherent envelope did NOT convert a genuinely open rank-one hole into a contradiction. Ghost-contact is simply the spectral encoding of an old finite-cover obstruction: the inability of finitely many cover members to fill the meeting region of the two open closures. Our Q-positive B×P control shows noncompact off-inseparability contact cores are already plentiful in stable locales.

**Suggested mathematical next decision:** Do not keep adding spectral-contact support requirements to a hypothetical counterexample. The unproven part remains *why a weak fitting defect cannot be somewhere dense in the finite-stabilized Urysohn relation*. Either attempt to exploit relative openness using a different invariant (e.g. a direct frame residual law), or pause Q for an adversarial external audit of the considerable new post-referee material.

**STATUS:** New INTERNAL deductions only; no external audit; Q and Q′ OPEN.
