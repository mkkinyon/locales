# Project A — Finite-cover fitting via clopen patching

> **STRENGTHENED IN CONSOLIDATION (24 Oct 2026):** The disjointness requirement on complemented patches in §1 is unnecessary. The proof works for **any covering family of complemented e_i**, each finitely covered by the given open cover. In §2 the base Y need only be **zero-dimensional**, not ultraparacompact: the compact-fiber tube cover can be refined by a possibly overlapping family of complemented opens. See [consolidated framework, §4](A-WU-Qprime-unified-synthesis-2026-10-24.md). Original working proof below retained as a special case for provenance.

24 October 2026. New **working** sufficient conditions for D=D2 and a noncompact test case. Internally verified, not independently audited; no originality claim.

## 1. Clopen-finite-subcover theorem

Call a frame L **clopen-finitely patchable** if for every cover C of 1 there is a partition 1=⋁_i e_i into pairwise disjoint complemented elements e_i, such that for each i a finite C_i⊆C satisfies e_i≤⋁C_i. The e_i may depend on C and need NOT be compact in L.

**Theorem (working).** If L is clopen-finitely patchable then D2=D.

Proof. Let h,k:L→M be a finite-cover-compatible pair. For each complemented e_i, the binary cover {e_i,e_i^c} forces h(e_i)=k(e_i)=m_i, by finite-cover compatibility and preservation of complements. The finite cover {e_i^c}∪C_i then gives

  1 = h(e_i^c)∧k(e_i^c) ∨ ⋁_{c∈C_i} h(c)∧k(c).

Meet with m_i to obtain m_i≤⋁_{c∈C_i} h(c)∧k(c). Joining over i,

  1 = ⋁_i m_i ≤ ⋁_{c∈C} h(c)∧k(c).

Therefore h,k respect every cover; the already-audited categorical characterization gives D2=D. Consequently W2=W, so both Q' and the focal Q hold in this class.

This is not subsumed by the earlier criterion '1 is covered by COMPACT complemented elements': the patching e_i need not be compact and may change with C. Nor does it require the compact closed neighborhood locus h_cc to cover X.

## 2. Compact-fiber product corollary

**Theorem (working).** Let Y be an ultraparacompact locale (every cover admits a disjoint clopen refinement), and K any compact locale. Then Y×K is clopen-finitely patchable; hence D2(Y×K)=D(Y×K).

Proof. For an arbitrary cover C of the localic product Y×K, compactness of K and the localic tube lemma yield a cover {v_j} of Y such that for each j the strip v_j×K is covered by a FINITE subfamily C_j of C. Ultraparacompactness refines {v_j} to a pairwise disjoint clopen cover {e_i} of Y, with e_i≤v_{j(i)}. Then {e_i×K} is a pairwise disjoint complemented open partition of Y×K and each piece is covered by the corresponding finite C_{j(i)}. Apply §1.

For topological spaces Y,K the tube step is elementary: each compact fiber {y}×K is covered by finitely many C-members; the tube lemma supplies v_y with v_y×K lying in their union. The pointfree proof uses the same compactness and the rectangle basis of the locale coproduct. No spatiality of the product is needed for the frame argument.

**Examples.** Y may be the Baire space N^N, whose second-countable zero-dimensional topology is ultraparacompact (take a countable clopen refinement of each cover and disjointize). The compact K factor may be non-Hausdorff. Unlike compact-closed patching, this works when the full product has no nonzero compact closed neighborhood.

## 3. Diagnostic noncompact product with no favorable strip locus

Let Y=N^N, the Baire space, and let K be the compact sober T1 two-apex space from the referee's corrected example: R⊔{p,q}, p having cofinite positive-tail neighborhoods and q cofinite negative-tail neighborhoods. Set X=Y×K.

Theorem §2 gives D2(X)=D(X), hence Q' for X. However h_hc(X)=0 because every nonempty product-open contains a rectangle V×U with V a nonempty Baire cylinder; V splits into two disjoint nonzero cylinders. Also h_cc(X)=0: if a compact closed sublocale F of X contained a nonempty product-open V×U, its compact image under projection to Y would contain nonempty V, impossible because no compact subset of Baire space has interior. Thus C(h_hc∨h_cc)=X is noncompact, so none of the previously found compact-remainder criteria detects the equality.

The localic square of X is spatial: the Baire self-product is spatial (complete metrizable/Polish; cf. Plewe 1996); the K self-product is locally compact sober; associativity and spatiality with a locally compact factor give X² ≅ Y²×K² as ordinary topological products. Then the closed point relation U(X) factors as

  U(X) = Delta_Y × U(K),

with product coordinates reordered. Since Y has no isolated points, Delta_Y has empty interior in Y². Therefore U(X) has empty ambient interior:

  cl(int U(X))=0,   G_X=U(X).

The Booleanization of O(U(X)) is atomless, because U(X) is spatially homeomorphic to Y×U(K) and every nonempty open rectangle in this product splits in the crowded Baire coordinate. Also U(X) is PROPER and W2(X)<U(X): pull back the binary cover {K\{p}, K\{q}}. Its square neighborhood excludes the nonempty relatively open portion Delta_Y×{(p,q),(q,p)} of U(X); since D2 lies inside that square open, its closed hull cannot cover this part. We DO NOT assert an explicit value for W(X) or strict I(X)<W(X): those need a separate product calculation.

This control has no hyperconnected or compact-closed strips, an atomless ENTIRE nonregular Urysohn relation G=U, and strict W<U, but still D2=D by a cover-patching mechanism distinct from those in our previous notes. It demonstrates that absence of compact closed neighborhoods and hyperconnected opens is far from enough to produce a Q' counterexample.

## 4. Caveat and next target

The theorem relies on a clopen partition where each cell is FINITELY covered by original members. It does not imply the locale itself is ultraparacompact, and products Y×K with K non-Hausdorff may fail ordinary ultraparacompactness. The theorem also gives D2=D, not a strict example W<W2. A Q' counterexample must fail this form of cover-patching, at least for one infinite diagonal cover.

The general questions remain open:

  Q': W=W2 universally?
  Q:  W2=U implies W=U universally?

Priority check needed. Standard topological definition of ultraparacompactness is a disjoint clopen refinement of every cover, e.g. pi-Base Property P000146; product spatiality caveats in Till Plewe (1996), 'Localic Products of Spaces'.
