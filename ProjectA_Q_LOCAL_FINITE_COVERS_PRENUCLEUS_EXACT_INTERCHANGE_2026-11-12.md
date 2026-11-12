# Project A — Locally finite covers: exact full/finite pre-nucleus interchange

**12 November 2026 — NEW INTERNAL theorem; not independently audited or priority checked.** Derived during the bounded rank-one Q chromatic-filter investigation. This is stronger than merely proving \(\mathcal D_2=\mathcal D\) for frames with locally finite cover refinements: **EVERY locally finite diagonal-cover implication is pointwise bounded by \(\Phi_2\) at ALL inputs q**, and **\(\Phi=\Phi_2\) pointwise on frames with locally finite refinements of every cover**. Moreover, the full-cover hole of a finite-fixed element is forced into the closed product of the cover's **nowhere-locally-finite locus**, a new precise support restriction.

Terminology: a frame cover \(\mathcal C\) is **locally finite** if there is another cover \(\mathcal V\) such that, for every \(v\in\mathcal V\), the set \(\{c\in\mathcal C:v\wedge c\ne0\}\) is finite. This is exactly the standard point-free definition (e.g. Picado–Pultr, *Frames and Locales*, Ch. IX, or earlier nearness-frame literature). A frame whose every cover has a locally finite refinement meets the usual frame-theoretic paracompactness cover condition, although terminology for *paracompact locale* sometimes also imposes regularity. **No regularity is assumed here.**

Let L=O(X), Q=L⊕L, \(w_C=\bigvee_{c\in C}c\boxtimes c\), and
\[
\Phi(q)=\bigvee_{C\text{ cover}}(w_C\to q),\quad
\Phi_2(q)=\bigvee_{F\text{ FINITE cover}}(w_F\to q).
\]

## 1. The exact pointwise domination theorem

**Theorem 1.1 (locally finite cover one-step simulation).** For EVERY frame L, frame element q∈Q, and locally finite OPEN COVER C of L,
\[
\boxed{w_C\to q\ \le\ \Phi_2(q).}
\tag{1.1}
\]

*Proof.* Choose a cover V **finitizing** C. For each v∈V, let
\[
F_v=\{c\in C:v\wedge c\ne0\},\qquad
t_v=\bigvee_{c\in C\setminus F_v}c.
\]
F_v is finite; \(v\wedge t_v=0\); and \(\{t_v\}\cup F_v\) is a FINITE cover of L.

Set \(x=w_C\to q\), so \(x\wedge w_C\le q\). For every v∈V,
\[
(x\wedge(v\boxtimes1))\wedge(t_v\boxtimes t_v)=0
\]
because \(v\wedge t_v=0\). For c∈F_v,
\[
(x\wedge(v\boxtimes1))\wedge(c\boxtimes c)\le x\wedge w_C\le q.
\]
Hence
\[
x\wedge(v\boxtimes1)\le
w_{\{t_v\}\cup F_v}\to q
\le\Phi_2(q).
\]
Since \(\bigvee_{v\in V}(v\boxtimes1)=1_Q\), joining gives \(x\le\Phi_2(q)\). QED.

**Corollary 1.2 (locally finite covers generate NO new pre-nucleus step).** Let
\[
\Phi_{\rm lf}(q)=
\bigvee_{C\text{ locally finite cover}}(w_C\to q).
\]
Then for every frame L and every q,
\[
\boxed{\Phi_{\rm lf}(q)=\Phi_2(q).}
\tag{1.2}
\]
Proof: every finite cover is locally finite; Theorem 1.1 gives the reverse inequality.

**Corollary 1.3 (paracompact-cover frames).** Suppose EVERY open cover of L admits a locally finite open refinement. Then for EVERY q∈Q,
\[
\boxed{\Phi(q)=\Phi_2(q).}
\tag{1.3}
\]
In particular
\[
\boxed{\mathcal D(L)=\mathcal D_2(L),\quad
\mathcal W(L)=\mathcal W_2(L),}
\]
and Question Q and Q′ both hold.

*Proof.* For arbitrary C choose locally finite refinement D. Then \(w_D\le w_C\), hence
\[
w_C\to q\le w_D\to q\le\Phi_2(q).
\]
Join over all C and use the reverse tautological inequality. Equal pre-nuclei have identical fixed sublocales, giving D=D₂ and W=W₂. QED.

This is stronger than the generalized-pair **locally finite cover principle**: for ANY frame maps h,k into ANY target M respecting all finite covers, a locally finite cover C is automatically respected. That too has a direct proof: for each finitizer v use the finite cover \(\{t_v\}\cup F_v\), meet its compatibility equation with h(v), kill the t_v term, and join over v.

## 2. The open locus of local finiteness of ONE bad cover

For any (not necessarily locally finite) cover C define
\[
\boxed{
\ell_C=\bigvee\{v\in L:\#\{c\in C:v\wedge c\ne0\}<\infty\}.
}
\tag{2.1}
\]
The set of qualifying v is **downward closed** but not necessarily closed under arbitrary joins; its join is the **largest open locus covered by locally finite patches**, not necessarily itself meeting only finitely many members.

**Theorem 2.1 (coordinate-strip localization).** For every q∈Q,
\[
\boxed{
(w_C\to q)\wedge(\ell_C\boxtimes1)\le\Phi_2(q),\qquad
(w_C\to q)\wedge(1\boxtimes\ell_C)\le\Phi_2(q).
}
\tag{2.2}
\]
*Proof.* For each individual v in the join (2.1), the proof of Theorem 1.1 gives the needed inequality directly for \(x\wedge(v\boxtimes1)\), with no assumption that all such v cover 1. Join these inequalities over v. The second is symmetric. □

If q=d is **finite-fixed**, \(\Phi_2(d)=d\), then for the relative full-cover hole
\[
E_C=C(d)\wedge O(w_C\to d)
\]
we get
\[
\boxed{E_C\wedge O((\ell_C\boxtimes1)\vee(1\boxtimes\ell_C))=0.}
\tag{2.3}
\]
Thus a genuine hole has BOTH coordinates supported inside the **closed complement of the locally finite locus** \(\mathfrak c_X(\ell_C)\). This is a new coordinate-support restriction, distinct from the earlier rather-below patch \(t_C\).

**Theorem 2.2 (normalized bad-cover saturation).** If a nonzero hole E_C exists and we pass to its least closed common coordinate support \(K\) via the independently reviewed pre-nucleus support theorem, the restricted bad cover \(C_K\) satisfies
\[
\boxed{\ell_{C_K}^{\,K}=0_K}
\tag{2.4}
\]
as well as the earlier \(t_{C_K}^{\,K}=0_K\). Equivalently,
\[
\boxed{\text{EVERY nonzero open of K meets INFINITELY MANY members of }C_K.}
\tag{2.5}
\]
*Proof.* Apply (2.3) inside K to its own nonzero canonical cover-hole E′, which contains the original marked E. Or apply the direct local implication calculation to the original E and use joint zero-reflection of its coordinate maps: every locally finite patch v on K has both images zero, hence v=0_K. □

Since \(\ell_C\le e_C\), where e_C is the largest open killed by both coordinates of the canonical hole, this also **sharpens** the original support reduction:
\[
\boxed{t_C\vee\ell_C\le e_C,\qquad
K_C\le\mathfrak c_X(t_C\vee\ell_C).}
\tag{2.6}
\]
The normalized counterexample therefore has no rather-below finite patches and no nonzero locally finite patches for the same cover.

## 3. Relation to Question Q and the chromatic obstruction

Put \(d=z_1=d_{\mathcal U}\). If finite stabilization \(\Phi_2(z_1)=z_1\) holds, then every arbitrary bad cover must fail local finiteness on the full coordinate support of its open hole, by (2.3)–(2.5). In particular **no cover with a locally finite refinement can witness a rank-one hole**, even on its least closed support.

This is stronger than saying “the cover has no finite subcover.” Infinite locally finite covers are ubiquitous in ordinary topology; ALL of them are harmless for the full-versus-finite diagonal pre-nucleus. A Q counterexample must use a genuinely **non-locally-finite-coverable** obstruction on an open part of the off-inseparability nonregular boundary \(G_\perp\).

The referee's cross-link graph and the new chromatic remainder theorem [the sharp gadget and chromatic-filter note](ProjectA_Q_RANK_ONE_SHARP_CHROMATIC_GADGET_AND_REMAINDER_FILTER_2026-11-12.md) supply independent additional constraints: infinite chromaticity, a proper chromatic ideal, and dense tail squares after removal of any finitely colorable subfamily. The local finiteness locus inequality (2.2), unlike those graph conditions, directly compares the **pre-nucleus values at EVERY input**, giving a structural positive class.

## 4. Bounded next tests, and limitations

- The theorem does NOT show every cover admits a locally finite refinement, nor that rank-one finite stabilization forces such refinements.
- **Correct terminology:** point-free paracompactness is often defined by the locally finite cover-refinement property (Picado–Pultr, Ch. IX). Other conventions require regularity. No novelty is claimed for the definition, and the relation between this pre-nucleus lemma and published cover-calculus results needs a separate priority check.
- The Scott powerset control \(S=\mathcal P(\omega)\setminus\{\varnothing\}\), with \(\mathcal C=\{\uparrow\{n\}:n\in\omega\}\), has \(\ell_C=0\) and a weak \(\mathcal D_2>\mathcal D\) defect, but \(\mathcal U=S^2=\mathcal W=\mathcal W_2\). Hence **\(\ell_C=0\) is NOT sufficient for Q failure**, even when accompanied by complete-graph chromatic complexity on a Boolean witness. More specifically, S has a COUNTABLE Scott basis, so it is **Lindelöf**, but it has NO locally finite refinement of the displayed cover. Indeed every nonempty Scott-open contains the greatest point \(\omega\); thus every nonzero v meets EVERY nonzero open cover member. Consequently every locally finite open cover of S is actually FINITE, while the singleton-basic cover has NO finite subcover. This verifies directly that the locally finite refinement hypothesis is substantially stronger than the Lindelöf property absent regularity. Beware of references saying 'Lindelöf locales are paracompact' under conventions which assume regularity.
- The next useful Q-specific problem is whether, on the rank-one exceptional sector \(G_\perp\), finite stabilization \(\Phi_2(z_1)=z_1\) can force a locally finite refinement of the cover **relative to some nonzero open part of \(G_\perp\)**, or an equivalent finite-cover simulation. No such general principle is proved here.

**STATUS: internal proof, not independently refereed. Universal Q/Q′ still open.**
