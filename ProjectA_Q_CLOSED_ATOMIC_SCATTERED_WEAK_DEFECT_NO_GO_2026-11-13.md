# Project A / Q, Q′ — closed-atomic support obstruction and scattered-space positive class

**13 November 2026 (America/Denver). INTERNAL ADVERSARIAL AUDIT, not externally refereed.** This note audits the new scattered-space argument from the direct density programme. It is deliberately stated using an explicit **closed-atomic** frame condition: the literature has multiple nonidentical uses of “scattered locale.” For a **spatial** locale the ordinary topological scatteredness condition suffices.

## 0. Definitions

Let (L=\mathcal O(X)). For an (L)-cover (C\subseteq L), let (w_C=\bigvee_{c\in C}c\boxtimes c\in L\oplus L=\mathcal O(X^2)). Define
\[
D_2=\bigwedge_{F\text{ finite cover}}\mathfrak o(w_F),\qquad
D=\bigwedge_{C\text{ arbitrary cover}}\mathfrak o(w_C)
\]
in the sublocale coframe. Thus (D\le D_2). A pair (h,k:L\to M) of frame homomorphisms is *binary compatible* when
\[
h(u)\wedge k(u)\vee h(v)\wedge k(v)=1_M
\qquad\text{for every }u\vee v=1_L.
\]
Finite-cover compatibility implies binary compatibility.

We call (L) **closed-atomic** if for every (e<1_L), the interval frame ([e,1_L]\cong\mathcal O(\mathfrak c_X(e))) has an atom: some (a>e) with no element strictly between (e) and (a). Do not confuse this explicit property with other definitions of scattered frames/locales.

## 1. Exact one-coordinate obstruction

**Theorem 1.1 (atomless least closed supports of weak defects).** Let (L,M) be frames with (M\ne\{0\}). Suppose (h,k:L\to M) are binary compatible, but for some arbitrary (L)-cover (C),
\[
m_C=\bigvee_{c\in C}h(c)\wedge k(c)<1_M.\tag{1.1}
\]
Pass to the nontrivial quotient frame (M'=\uparrow m_C), whose quotient map is (q(t)=t\vee m_C). Write (h'=qh,k'=qk). Their (C)-matching value is (0_{M'}=m_C), and they remain binary compatible. Put
\[
e_h=\bigvee\{a\in L:h'(a)=0_{M'}\},\qquad
e_k=\bigvee\{a\in L:k'(a)=0_{M'}\}.
\]
Then **both** interval frames ([e_h,1]) and ([e_k,1]) are atomless.

*Proof for the first coordinate.* Rename (M',h',k') as (M,h,k), with (\bigvee_C h(c)\wedge k(c)=0_M). Let (e=e_h). The arbitrary-join property of (h) gives (h(e)=0_M), and
\[
h(t)=0_M\iff t\le e,\qquad h(t)=h(t\vee e).\tag{1.2}
\]
Since (M) is nontrivial and (h(1)=1_M), (e<1).

Suppose (a>e) is an atom of the interval ([e,1]). For every (c\in C) the element (a\wedge(c\vee e)\in[e,a]) equals either (e) or (a). Partition
\[
C_1=\{c\in C:a\le c\vee e\},\quad
C_0=\{c\in C:a\wedge(c\vee e)=e\},\quad
u=\bigvee C_1,\quad v=\bigvee C_0.
\]
Then (u\vee v=1), so \(\{u,v\}\) is a binary cover. From (1.2), (h(a)\ne0_M). For (c\in C_1), (h(a)\le h(c)); for (c\in C_0), (h(a)\wedge h(c)=0_M). Hence
\[
h(a)\le h(u),\qquad h(a)\wedge h(v)=0_M.\tag{1.3}
\]
Meet binary compatibility (1=h(u)\wedge k(u)\vee h(v)\wedge k(v)) with (h(a)). By (1.3),
\[
h(a)=h(a)\wedge k(u)
=\bigvee_{c\in C_1}\bigl(h(a)\wedge k(c)\bigr)=0_M,
\]
since (h(a)\le h(c)) for every (c\in C_1) and (h(c)\wedge k(c)=0_M) for each (c\in C). Contradiction. Thus ([e_h,1]) is atomless. Interchange (h,k) to obtain the second claim. □

**Audit note.** The proof works for an *arbitrary* target frame (M), including nonspatial and Boolean targets. The essential step is the infinitary distributive law (t\wedge\bigvee s_i=\bigvee(t\wedge s_i)), valid in every frame. No pointwise decomposition or choice of ordinary points occurs.

## 2. Scattered positive class

**Corollary 2.1.** If (L) is closed-atomic, every binary-compatible pair of frame maps (h,k:L\to M) respects every arbitrary (L)-cover. Consequently,
\[
\boxed{D_2(X)=D(X),\qquad W_2(X)=W(X).}\tag{2.1}
\]
*Proof.* Otherwise Theorem 1.1 constructs a nonzero closed quotient ([e_h,1]) lacking atoms, contradicting closed-atomicity. Maps into arbitrary frames classify morphisms into (X^2), and factoring through (D_2) (respectively (D)) is precisely finite-cover (respectively all-cover) compatibility. Thus equality of all such factorization predicates yields (D_2=D). Taking closures gives (W_2=W). □

**Corollary 2.2 (ordinary scattered spaces).** Suppose (X) is spatial and its sober point space is *topologically scattered*: every nonempty closed subspace has an isolated point. Then (L=\mathcal O(X)) is closed-atomic, because the singleton of an isolated point is an atom in the frame of opens of the corresponding nonempty closed subspace. Therefore (2.1) holds. No local compactness, regularity, metacompactness, Baire property, or spatiality of (X^2) or (W_2(X)) is required.

**Remark on the name.** Picado–Pultr, *Frames and Locales* (2012), VI §8.1, use “scattered space” in precisely the ordinary closed-subspace sense. Some locale-theoretic definitions of scatteredness refer instead to Boolean sublocales or complemented sublocales; **this note makes no assertion that those point-free notions coincide with closed-atomicity**.

## 3. Fixed-point strengthening, Q and Q′

Let (P=L\oplus L) and
\[
\Phi_2(d)=\bigvee_{F\text{ finite cover}}(w_F\to d),\qquad
\Phi(d)=\bigvee_{C\text{ arbitrary cover}}(w_C\to d).
\]
**Lemma 3.1.** If every finite-cover-compatible pair of frame maps into any target frame respects every arbitrary cover (in particular if (D_2=D)), then every (\Phi_2)-fixed (d\in P) is also (\Phi)-fixed.

*Proof.* Suppose (\Phi_2(d)=d) but (\Phi(d)>d). Choose a cover (C) for which (r=(w_C\to d)\nleq d). In the closed sublocale (Y=\mathfrak c_{X^2}(d)), the relatively open sublocale (E=\mathfrak o_Y(r)) is nonzero and its (C)-matching open vanishes. For each finite cover (F), (w_F|_Y) and hence (w_F|_E) are dense open: (w_F\to d=d). Pass from (\mathcal O(E)) to its nontrivial double-negation Booleanization (B(E)). Every dense open becomes top, whereas (w_C|_E=0) remains bottom. The coordinate maps (L\rightrightarrows\mathcal O(E)\to B(E)) therefore define a nontrivial finite-compatible but (C)-defective pair, contradiction. □

Thus under closed-atomicity, the **full and finite pre-nuclei have the same fixed points**, not necessarily the same pointwise values at one stage. In particular Q′ holds, and the rank-one Q implication holds whenever its finite-fixed premise (\Phi_2(z_1)=z_1) applies. **Do not claim unconditional one-step equality \(\Phi=\Phi_2\).**

## 4. Internal adversarial checks and limitations

1. **Target reduction valid.** (t\mapsto t\vee m_C) preserves arbitrary joins, finite meets, and top; the quotient is nontrivial precisely because (m_C<1_M). Bottom in (M') is (m_C), not original (0_M).
2. **Zero kernel principal.** The join (e_h) of all zero-mapped opens is again zero-mapped; conversely (h'(a)=0\iff a\le e_h). This justifies all comparisons in the closed-support interval.
3. **Atom partition exhaustive.** (a\wedge(c\vee e)\in[e,a]), so it is exactly (e) or (a). Even an infinite (C) yields a legitimate binary *coarsening* \(\{u,v\}\).
4. **No pointwise leap.** The proof uses arbitrary frame morphisms and does not assume generalized pairs arise from ordinary points.
5. **Sublocale passage.** Equality (D_2=D) follows from the same universal factorization property, not from coincidence of ordinary points.
6. **Not a necessity criterion.** Closed-atomicity is sufficient, not necessary: compact atomless spatial frames have (D_2=D) because all covers admit finite subcovers.
7. **Known weak-defect examples.** A Scott or Arrieta Boolean weak defect must have both coordinate least closed supports atomless; this is a new consistency test, not a claim that their entire source frames are atomless.
8. **One-step caveat.** The strong equality of fixed-point sets follows from Lemma 3.1; it does not establish \(\Phi(q)=\Phi_2(q)\) for arbitrary (q).

**Status:** This theorem and its consequences have passed the algebraic internal audit here, but have **not** been externally refereed or checked for originality. Universal Q and Q′ remain OPEN.
