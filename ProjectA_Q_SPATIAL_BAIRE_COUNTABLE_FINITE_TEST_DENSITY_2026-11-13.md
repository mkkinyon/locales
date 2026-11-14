# Project A / Q′ — spatial Baire plus countable finite-cover tests forces matching-square density

**13 November 2026 (America/Denver); NEW INTERNAL bounded sufficient criterion, not externally audited. Q/Q′ OPEN.** This is a direct, genuinely **relative Baire argument inside \(W_2\)**, complementing [localic chromatic density](ProjectA_Q_RELATIVE_CHROMATIC_DENSITY_ALL_FINITE_FIXED_2026-11-13.md) and the [canonical spectral predecessor-lifting no-go](ProjectA_Q_CANONICAL_SPECTRAL_PREDECESSOR_LIFT_NO_GO_2026-11-13.md). It deliberately does **not** assume that weak Boolean defects have ordinary points.

## 0. Set-up

Let \(L=\mathcal O(X)\), \(P=L\oplus L\), \(d_0=\Phi_2^\infty(0)\), and
\[
Y=W_2(X)=\mathfrak c_{X^2}(d_0).
\]
For any finite X-cover F put \(w_F=\bigvee_{f\in F} f\boxtimes f\). Since \(\Phi_2(d_0)=d_0\), the restricted open
\[
U_F=\mathfrak o_Y(w_F)
\]
is **dense** in Y, equivalently \(w_F\to d_0=d_0\). For an arbitrary X-cover C let \(U_C=\mathfrak o_Y(w_C)\). Q′ asserts that **every** \(U_C\) is dense in Y.

**Important hypothesis used below:** Y is a **spatial locale whose ordinary representing topological space is Baire**. The statement “Y is localic Baire” without spatiality does not suffice for the pointwise step.

## 1. Countable separator theorem

**Theorem 1.1 (countable finite-test Baire criterion).** Fix an arbitrary cover C of X. Suppose there is a **countable family of finite X-covers** \((F_n)_{n<\omega}\) with this pointwise detection property:

> For every *ordinary locale point* \(z:1\to Y\), if its endpoint pair \((x,y)\) does **not** lie in any common C-square \(c\boxtimes c\), then for some n it does **not** lie in \(w_{F_n}\).

Equivalently, as sets of ordinary Y-points,
\[
\boxed{\bigcap_{n<\omega}U_{F_n}\ \subseteq\ U_C.} \tag{1.1}
\]

Then
\[
\boxed{U_C\text{ is dense in }Y,\quad w_C\to d_0=d_0.} \tag{1.2}
\]
Thus C cannot witness a Q′ failure.

*Proof.* Every \(U_{F_n}\) is a dense **open** subset of the spatial Baire space Y. Their countable intersection is a dense \(G_\delta\) set \(G\subseteq Y\). By the assumed detection property \(G\subseteq U_C\). Hence the open \(U_C\) is topologically dense in Y. Because Y is spatial, this is precisely density of the corresponding open sublocale. □

This is not merely another support restriction: it constructs an actual **dense subset inside Y**, consisting of ordinary point-pairs that pass the selected finite-cover tests. The role of countability is to make the Baire theorem applicable. The hard step in applications is finding a countable test family that detects *all* C-bad ordinary Y-pairs.

**Corollary 1.2 (globally countable finite presentation).** If the finite-cover compatibility predicate on ordinary points of Y is captured by countably many finite covers \(F_n\)—i.e. every ordinary Y-pair respecting all F_n automatically respects **all finite X-covers**—then Q′ holds on X, provided Y is spatial Baire.

*Proof.* An ordinary point-pair respecting all finite X-covers respects **every** arbitrary cover C: otherwise partition C into the opens containing x and those not containing x; their two joins form a binary X-cover whose common-match value at (x,y) is zero. Thus the same countable family detects all C-bad pairs, and Theorem 1.1 applies cover by cover. □

In particular, if the entire frame L is **countable**, enumerate all finite X-covers to obtain a suitable family. More generally, a countably cofinal family of finite covers under refinement suffices. These are conditional examples; no claim that second countability of X alone gives such a cofinal family.

## 2. Countable point-finite covers: a second route to a known positive class

**Corollary 2.1 (countable, point-finite, spatial-Baire variant).** Suppose C=\(\{c_i:i<\omega\}\) is an **ordinarily point-finite** open cover of a spatial X, and Y=W₂ is spatial Baire. Then \(U_C\) is dense in Y.

*Proof.* For each finite \(S\subseteq\omega\), put
\[
a_S=\bigvee_{i\in S}c_i,\qquad b_S=\bigvee_{i\notin S}c_i.
\]
The two opens \(a_S,b_S\) form a binary X-cover. There are countably many such S. If an ordinary Y-point (x,y) is C-bad, let \(S=\{i:x\in c_i\}\), a **finite** set by point-finiteness. Then x belongs to \(a_S\) and not \(b_S\), while y belongs to \(b_S\) and not \(a_S\): C-badness ensures y belongs to no c_i with i∈S, and C being a cover ensures some other c_j contains y. Hence the binary cover \(\{a_S,b_S\}\) has no matching member at (x,y). These countably many binary covers meet Theorem 1.1's detection hypothesis. □

The earlier [hereditary-Baire point-finite rigidity theorem](ProjectA_Q_BAIRE_POINTFINITE_RIGIDITY_AND_FAR_REDUNDANCY_2026-11-12.md) proves the **stronger** \(D_2\le\mathfrak o(w_C)\) for *arbitrary cardinal* point-finite covers when X is hereditarily Baire and spatial, without requiring Y spatial Baire. Corollary 2.1 has **different hypotheses and a weaker conclusion**; it is not presented as a replacement or improvement of that theorem.

## 3. Why the extra spatiality cannot be omitted

A localic Baire theorem says the sublocale meet of countably many dense opens is dense. It does **not** produce ordinary points in the intersection when the locale is nonspatial. In the Q′ programme, dense pointless sublocales are a central possibility: Booleanizations of atomless locales can be dense yet have no ordinary locale points, and the branching Scott controls have \(D_2>D\) despite Q′ holding.

The proof of Theorem 1.1 has a precisely located non-pointfree step:
\[
\text{dense }G_\delta\text{ **of ordinary Y-points**}
\quad\Longrightarrow\quad
\text{pointwise binary-cover coarsening applies}.
\]
Without spatiality (or a replacement guaranteeing enough ordinary points in that particular intersection), that arrow is unavailable. The statement is therefore a **conditional spatial-Baire criterion**, not a universal proof of Q′.

The theorem also does **not** say that a countable basis of X yields countably cofinal finite covers, nor that W₂ is automatically spatial or Baire for all X.

## 4. Relation to local chromatic obstruction and research priority

A strong C-hole would produce a nonzero relatively open E⊂Y disjoint from \(U_C\). By [relative chromatic density](ProjectA_Q_RELATIVE_CHROMATIC_DENSITY_ALL_FINITE_FIXED_2026-11-13.md), every nonzero open chart V⊂E has an infinite-chromatic cross-link graph. The countable separator theorem supplies an *alternative* obstruction: in a spatial Baire Y, a **countable** family of finite-cover tests that separates all C-bad ordinary pairs makes such E impossible.

The actual open problem is to find **nontrivial classes** of frames/locales for which the C-bad pairs have a countable finite-test separating family, or to replace spatial Baire by a genuinely point-free density principle controlling the corresponding nonspatial Gδ intersection. These are actionable subproblems; no general result is claimed.

**Verification status:** internally checked pointwise Baire argument and binary coarsening; not externally audited. **Q and Q′ remain OPEN.**
