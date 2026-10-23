# Project A: almost-normal subfit frames have I = U = F = V = V2
23 October 2026. **Working deduction from published Picado–Pultr lemma; independent audit still requested.**

## Theorem

If L is an almost-normal and subfit frame, then

    d_I = d_2 = d_U = d_F,

hence, in sublocale order,

    I = U = F = V = V_2.

In particular this applies to the frame of opens of EVERY almost-normal T1 topological space, regardless of whether its localic square is spatial. It is stronger than the prior almost-normal theorem V_2=F and than all point-pair-only T1 deductions.

## Algebraic input (Picado–Pultr)

Picado and Pultr, *More on subfitness and fitness*, preprint 13-28 (2013), Proposition 3.4.3, https://www.mat.uc.pt/preprints/ps/p1328.pdf , prove:

    If L is almost normal and subfit, then
    a** = ⋁{c∈L : c≺a**}  for every a∈L.

Self-contained reconstruction: Let r=⋁{c:c≺a**}, and suppose a**≰r. By subfitness applied to (a**,r), choose z with a**∨z=1 but r∨z≠1. Since a** is double-negation-stable, almost-normality gives u,v with u∧v=0, a**∨u=1, z∨v=1. Then u≤v*, so a**∨v*=1 and v≺a**. Thus v≤r, forcing z∨r=1: contradiction.

**Source typo caution:** The displayed proof in the scanned preprint seems to write 'a∨c=1' rather than 'a**∨c=1' at this step. Applying subfitness to a** (as above) avoids this ambiguity. Verify if quoting a later published version.

## Proof of the new relation consequence

Let a,b∈L be disjoint, a∧b=0. The double-negation operator is a nucleus and preserves binary meets, so a**∧b**=(a∧b)**=0.

By the Picado–Pultr approximation formula,

    a**=⋁_{c≺a**}c,    b**=⋁_{f≺b**}f.

Thus in Q=L⊕L:

    a⊠b ≤ a**⊠b**
         = ⋁_{c≺a**, f≺b**}(c⊠f)
         ≤ d_2,

because a**∧b**=0, so each c⊠f appears in the two-step separated-apartness generators. Joining over all a∧b=0 gives d_I≤d_2. The reverse inequality d_2≤d_I holds in every frame, therefore d_I=d_2.

Almost-normality means ≺ interpolates, hence d_2=d_U=d_F by rational interpolation and the always-valid sandwich d_F≤d_2≤d_U. This proves equality of all apartness opens and of the closed sublocales I,U,F. The previously established rank-two annihilator theorem (or its simpler d_2=d_I corollary) now yields I=V=V_2 as well.

## T1 corollary

For a T1 space X, O(X) is subfit: if open a⊈b choose x∈a\b; put c=X\{x}, open. Then a∨c=X but b∨c=c≠X. So any almost-normal T1 space satisfies I=F=V_2=V exactly as LOCALIC sublocales, no spatiality of X×_locX needed.

This rules out almost-normal modifications of the countable Hausdorff rational-bridge counterexample even if its locale product is nonspatial. It also includes Hausdorff extremally disconnected ultrafilter examples and T1 cofinite spaces.

## Relative scope

The theorem does not show the implication almost normal ⇒ V=F for NONSUBFIT arbitrary frames. The continuous-Scott-domain theorem (A-V-almost-normal-continuous-Scott-collapse-2026-10-23.md) covers an independent nonsubfit class.

A weaker sufficient condition than subfitness is the displayed approximation property

    a** = ⋁{c:c≺a**} for every a;

together with interpolation it implies d_I=d_F. Thus failure of this almost-regularity condition is necessary for an almost-normal frame with V≠F.

## Audit priorities

- Check definition and use of subfitness, and Picado–Pultr Proposition 3.4.3's proof with a** versus a.
- Check double-negation nucleus finite-meet preservation.
- Check all double-indexed rectangle joins in frame coproduct Q.
- Check the implication c≺a**, f≺b**, a**∧b**=0 ⇒ c⊠f is among d_2 generators.
- Check that a T1 frame O(X) is subfit without additional sobriety assumption.
- Distinguish I=C(d_I) from the actual diagonal Delta and from D=fit(Delta).
