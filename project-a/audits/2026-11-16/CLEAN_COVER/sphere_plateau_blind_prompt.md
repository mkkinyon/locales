# Independent blind audit request — Project A, sphere-plateau strengthening

**Date:** 16 November 2026  
**Subject:** Clean Boolean cover-insertion filtrations of finite posets: preterminal homotopy spheres and unit long differentials.

Please referee `BLIND_MATHEMATICAL_PACKET.md` **independently and adversarially**. An optional stand-alone `verify_seed_collapses.py` is supplied for reproducibility, but it does not replace a mathematical audit. All definitions, proofs, computations, asides, and asserted consequences are in scope.

## What is at stake

The underlying constructions were previously used to produce arbitrarily late **nonzero** integral spectral-sequence differentials. The present packet makes substantially stronger assertions: throughout the entire preterminal filtration, the absolute examples have the homotopy type of a sphere and all transition inclusions are homotopy equivalences; in the relative examples an analogous sphere appears at filtration one. It follows that the long integral differential is an **isomorphism** `Z -> Z` with coefficient `+1` or `-1`, rather than merely a nonzero integer map.

The decisive proposed mechanism is a simplicial-collapse induction on deletion subcomplexes. A correct seed calculation alone is not enough: the filtration compatibility and the relative construction must also survive scrutiny.

## Requested checks

1. **Foundations and seed:** Verify every marked relation is a cover, the prescribed capped extension is a poset, and the base order complex is contractible. Independently check the seed collapse certificates, their order, free-facet property, filtration weights, final octahedral boundary, and numerical data.
2. **Cap deletion:** Check that deleting the cap vertex induces an elementary simplicial collapse at *each* filtration level, preserving the weight of each paired simplex. Search for unlisted cofaces or problematic old/new comparisons.
3. **Deletion-filtration induction:** Check the exact formula for `B_{r+1,p}`, the relative lift of free-face collapses to the `y`-cone, and the subsequent `v`-cone collapses. In particular, examine the top step of the *old* filtration.
4. **Main preterminal assertion:** Check the formulas for `D_p` and `F_p(U)`, the pushout intersections, the case `p=1`, the naturality of the homotopy-equivalence statements as `p` varies, and the induction ranges. Distinguish actual collapses from homotopy equivalences.
5. **Relative assertion:** Verify the `Q`-filtration formula, `F_0(Q)` being contractible, the `D'_p` collapse, and the shift in sphere dimension and spectral-sequence page.
6. **Integral conclusion:** Check the precise `E^1` groups, bidegrees, and the claim that the only possible nontrivial differential is multiplication by `±1`, both absolutely and relatively. Do not infer an integral unit simply from nonvanishing modulo two.
7. **Scope and presentation:** Record first-reading confusions and any imprecise terminology, hidden hypotheses, inaccurate numerical data, overly strong statements, or simplifications. Suggest better formulations and independent proof routes where available.

Please clearly separate **established**, **repairable**, **unproved**, and **false** items, giving counterexamples or exact corrections when possible. If you find a serious problem, continue identifying which restricted claims remain valid rather than stopping at the first gap.

## Blindness

The packet intentionally omits prior referee reports, internal audits, and the research discussion that led to the result. Please assess the supplied mathematics on its own. You need not visit the GitHub repository. The optional script is provided as an audit target and a convenience; you may disregard it and verify the base directly.

