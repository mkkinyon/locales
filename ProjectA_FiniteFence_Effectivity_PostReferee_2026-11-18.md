# Project A — finite-fence effectivity: post-referee status and blockwise route

**18 November 2026.** Companion/erratum to
*ProjectA_FiniteFence_EquivalenceHull_Theorem_2026-11-18.md*.

**Status:** The proposed equality

\[
  \operatorname{EqHull}(H_G)=\mathcal K_q
    =(H_G\circ H_G)\circ(H_G\circ H_G) \tag{E}
\]

is **unproved**. The blind external referee found an explicit counterexample
to one supporting lemma and an invalid application of proper-descent theory.
Neither finding is a counterexample to (E).

## 1. Independent referee findings

The external referee report and separate addendum, both dated 18 November 2026,
were read after the original theorem note was prepared. Their principal points:

| Item | Post-audit status |
|---|---|
| Finite-fence geometry, quotient and generic point | Essentially sound |
| (59)–(61), generic patch point fibre | Substantially verified; \(\Lambda_E\neq0\) via \(\mathcal B(\overline E)\le\Lambda_E\) |
| Cantor antichain-support/fusion lemma | Incomplete induction; no counterexample found |
| (62), Cantor-graph generation of \(\Lambda_E^2\) | Conditional on fusion and fittedness argument |
| Original dense-strip lemma (DS-P) | **False** for arbitrary compact antichains |
| Dense-strip lemma for perfect Cantor antichains | Repair available; proof below |
| (63), Cantor-graph inclusion | Proof route sound after graph-restricted fibre-product argument |
| (65a), saturated-avoidance support bound | Direct localic proof supplied by referee |
| (65), patch kernel-pair decomposition | Conditional on Cantor fusion |
| (64), (66), (67) | **Unproved**: the invoked proper-descent hypothesis fails |

### The explicit failure of the old dense-strip lemma

For any fixed \(k\), put \(d=f(a_k)\) and \(D=\{d\}\). Then \(D\cap E_P\)
is dense in \(D\), but \(q^{-1}q(d)\) is confined to the finite component
of \(d\). Therefore \(\mathcal B(D\times M)\not\le H_G\circ H_G\).
Perfection of \(D\), or the equivalent local condition of arbitrarily
late selected fence indices in every nonempty relatively open subset,
was an essential missing hypothesis.

### Perfect does not imply proper

The patch counit \(p:P\to X\) is **perfect**, but is not a closed map and
therefore is not a **proper map in Vermeulen's descent sense**. Indeed, an
odd-position maximal fence vertex \(v\) is patch-closed as a singleton, but
an adjacent minimal vertex \(u<v\) belongs to the upper-topology closure
of \(\{v\}\). The same problem affects \(p\times p\).
Thus Vermeulen's theorem on effective descent for proper surjections
cannot justify either

\[
  G\times G\le T\circ T \tag{64}
\]

or the global upper bound in

\[
  \mathcal K_q=(H_G\circ H_G)\circ(H_G\circ H_G). \tag{66}
\]

The exact missing ingredient is a *valid reflection* of the particular
patch sublocale inclusions through \(p\times p\), or a direct upper-localic
argument. No general reflection principle has been established here.

## 2. Corrected dense-strip lemma

Let \(D\subseteq P\) be a **perfect compact antichain**, with
\(D\cap E_P\) dense in \(D\). Let \(M\) be the middle Cantor locale,
and let \(U_P\) be a nonempty fixed upper-open sublocale of the geometric
gap between \(K\) and \(M\), met by all sufficiently fine \(P_n\).
Then

\[
 \boxed{\mathcal B(D\times M)\le T,\qquad
        \mathcal B(M\times D)\le T},\qquad T=H_G\circ H_G. \tag{DS'}
\]

The analogous statement holds for \(Q\)-fences with \(U_Q\).
The perfectness hypothesis may be replaced by the explicit local
unbounded-index condition.

**Proof.** Inside \(D\times U_P\) take the spatial trace of pairs
\((d,u)\) in a common \(P_n\), with \(d\in D\cap E_P\) and
\(u\in U_P\cap V(P_n)\). The trace is dense: every nonempty relatively
open part of perfect \(D\) contains selected vertices from arbitrarily late
fences, and the small-edge crossing condition makes each late fence meet
every prescribed nonempty open subset of the gap.

Similarly the spatial trace in \(U_P\times M\) of pairs \((u,a_n)\)
from a common \(P_n\) is dense, using the density of \(A\) in \(M\).
Both traces factor through \(H_G\). Their inverse images in
\(Z=D\times U_P\times M\) are dense because the relevant product
projections are open surjections. Their meet contains
\(\mathcal B(Z)\), so supplies a dense composable sublocale in the
localic pullback of the two copies of \(H_G\).

Project to \(D\times M\). The projection is open and surjective, and
the image of a dense sublocale along an open surjection is dense:
every nonzero target open has a nonzero preimage meeting the dense source.
Thus the composite image contains \(\mathcal B(D\times M)\), proving
the first inclusion. The second and \(Q\) versions follow by symmetry. \(\square\)

**Graph qualification for (63).** One must restrict the two strips to
\(\Gamma\times M\) *before* taking their composite image. The two
coordinate projections \(\Gamma\to D_1,D_2\) are homeomorphisms;
therefore both pulled-back Booleanized strips contain the Booleanization
of \(\Gamma\times M\). Projection along overt \(M\) then gives
\(\mathcal B(\Gamma)\le T\circ T\).
Density in the full \(D_1\times M\times D_2\) would not by itself
survive restriction to a nowhere-dense graph.

## 3. Patch support and generic-fibre strata

The referee gave a direct saturated-open proof of (65a): for disjoint
patch-closed \(D_1,D_2\), every closed \(A\subseteq D_1\) avoiding \(E\)
is component-saturated, and its open complement descends to \(Q\).
Testing the kernel-pair equality against this quotient open forces
\[
 \operatorname{Eq}(q\circ p)\wedge(D_1\times D_2)
 \le [E\cap D_1]_{D_1}\times[E\cap D_2]_{D_2}. \tag{65a}
\]
This is a localic support inequality, not just a statement about points.
The remaining upper-bound proof of (65) still depends on the unfinished
Cantor fusion lemma.

The addendum gives the useful inclusions
\[
 \mathcal B(K),\ \mathcal B(M),\ \mathcal B(L)\le\Lambda_E, \tag{A1}
\]
and the strict inequality
\[
 \mathcal B(\overline E)<\Lambda_E. \tag{A2}
\]
The three displayed nonzero sublocales are pairwise disjoint; each Cantor
set can be partitioned into arbitrarily many disjoint nonempty clopen
Cantor pieces with the same property. Also, for \(J_i\in\{K,M,L\}\),
\[
 0\ne\mathcal B(J_1)\times\mathcal B(J_2)
 \le\Lambda_E\times\Lambda_E. \tag{A3}
\]
These are inclusions of sublocales, not a claimed coproduct decomposition.

## 4. New blockwise conclusion without patch descent

**Proposition (Booleanized nine-block inclusion; conditional only on
the corrected dense-strip lemma).** For all \(J_1,J_2\in\{K,M,L\}\),
\[
 \boxed{\mathcal B(J_1\times J_2)\le T\circ T.} \tag{B1}
\]

**Proof.** Each of \(K,M,L\) is a perfect compact antichain with a
dense selected fence trace: \(f(A)\subset K\), \(A,B\subset M\), or
\(g(B)\subset L\). Apply (DS') in the appropriate colour to get
\[
 \mathcal B(J_1\times M)\le T,\qquad
 \mathcal B(M\times J_2)\le T.
\]
In \(Z=J_1\times M\times J_2\), inverse images of both dense strips
under open product projections remain dense. Their meet contains
\(\mathcal B(Z)\), which is a composable witness for \(T\circ T\).
The open surjection \(Z\to J_1\times J_2\) sends it to a dense sublocale,
containing \(\mathcal B(J_1\times J_2)\). \(\square\)

In particular,
\[
 \mathcal B(K\times L)\le T\circ T. \tag{B2}
\]

**Warning.** This does *not* establish
\(\mathcal B(K)\times\mathcal B(L)\le T\circ T\).
In general \(\mathcal B(K\times L)\le\mathcal B(K)\times\mathcal B(L)\);
the reverse inclusion cannot be assumed.

**Restricted patch reflection.** Every point of \(K,M,L\) is minimal
in the pospace. Each \(J\in\{K,M,L\}\) is consequently a patch-closed
lower set, hence a closed sublocale of \(X\); its induced upper
topology agrees with its Euclidean Cantor topology.
The patch counit restricted to \(J\) is therefore an isomorphism,
and so is its restriction to each \(J_1\times J_2\).
It follows that inclusion between sublocales **of these closed blocks**
is reflected by patch pullback, notwithstanding the failure of general
proper descent for \(p^2\).

**Update after the restricted \(K\times L\) internal audit.** A direct
quotient-open calculation, without (65) or proper descent, now gives
\[
 \mathcal K_q\wedge(K\times L)
  =(\Lambda_E\wedge K)\times(\Lambda_E\wedge L). \tag{B3}
\]
The corrected Cantor-graph/strip argument gives
\[
 \boxed{(\Lambda_E\wedge K)\times(\Lambda_E\wedge L)
       \le T\circ T.} \tag{B4}
\]
Together these imply
\(\mathcal K_q\wedge(K\times L)=(T\circ T)\wedge(K\times L)\).
The proof and a proposed extension to all nine Cantor blocks are recorded
in [the restricted-block theorem note](ProjectA_FiniteFence_Restricted_Blocks_2026-11-18.md).
This supersedes the *conditional* statuses of (B3) and (B4?) above,
but does **not** establish (E) on the geometric gaps.

## 5. Immediate research priorities

1. Adversarially test the proposed **nine-block formula (6?)** in the
   restricted-block note, especially the ordinary-support split when
   \(I=J\), and the two-colour localization when \(M\) occurs.
2. Determine what replaces invalid global proper descent, beginning
   with one coordinate in a geometric gap or fence interior.
3. Investigate whether the localic kernel-pair calculation can be
   propagated across the gap-to-Cantor and gap-to-gap rectangles
   using saturated-open tests.
   It may be preferable to prove inclusion directly in \(X^2\) by
   open/closed tests. General surjectivity of \(p\) is insufficient.

**Sources:** independent report
*ProjectA_FiniteFence_Effectivity_Independent_Referee_Report_2026-11-18.md*
and its separately authored
*ProjectA_FiniteFence_Effectivity_Referee_Addendum_2026-11-18.md*;
Escardó, *The regular-locally-compact coreflection*;
Vermeulen, *Proper maps of locales*, Theorem 5.6.


## 5. Later Session 9 development: pointless patch comparison and open cross-gap

A new companion note, `ProjectA_PatchFibre_CrossGap_Theorem_Note_2026-11-18.md`, consolidates a general **pointless patch-fibre isomorphism** `p^{-1}(S)≅S` for this shrinking finite-fence pospace (internally audited), and a **candidate exact cross-gap equality**

\[
 \mathcal K_q\wedge(U_P\times U_Q)
   =(T\circ T)\wedge(U_P\times U_Q)
   =G_P^*\times G_Q^*.
\]

The latter relies on a selected-coordinate richness lemma, a simultaneous antichain Cantor-graph fusion with finite-component reservations, corrected perfect-Cantor dense strips, and graph-restricted composition. A blind external audit is being requested. These claims use **no general proper descent** of the patch counit. The global equality `(E)` at the top of this status note **remains unproved**, even if the cross-gap result survives review.
