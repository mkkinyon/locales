# Project A — internal adversarial audit of (LC-PT) discrete-defect gluing

**15 November 2026 · Formal internal self-audit completed, before independent blind review.** This audit is separate from, and must **not** be supplied with, the blind external packet. It rechecks the candidate from first principles, including attempts to find a countercover, a join-closure failure, a non-fitted point, or a contradiction with audited (A-SC). It is not independent external verification and makes no novelty claim.

**Audit target:** [the complete proposed construction](ProjectA_LCPT_DISCRETE_DEFECT_GLUE_COUNTEREXAMPLE_2026-11-15.md). The proposed central statement is: there is a compact locally compact sober T1 locale with all points fitted but \(\mathcal A\ne\Delta\).

## Summary verdict

**No mathematical defect found in the central counterexample during the formal internal adversarial audit.** All nine claims below admit direct proofs. The example is algebraic (compact-open generated) but **not coherent/stably locally compact**. Its point-fitting verification uses sublocale meets. The original apparent contradiction with (A-SC) disappears at the meet of two compact opens. The result should remain **internally verified, external audit pending**, not canonically promoted yet.

The proof's few needed repairs are editorial/structural: explicitly show regularization is a frame quotient into RO(K); display a second generalized-map proof of fittedness; prove countability claims separately; emphasize that relative discreteness may be infinite near a boundary; and remove internal-review cues from the blind packet.

## A1. Arbitrary joins: PASS

Let \(S_i=c_i\setminus v_i\), relatively closed discrete in the open \(c_i\subseteq K\). For \(c=\bigcup c_i\), \(v=\bigcup v_i\), \(S=c\setminus v\) is closed **in c** because v is open in K. Given p∈S, some c_i contains p, and \(S\cap c_i\subseteq S_i\). Thus an open neighborhood in c_i isolating p from S_i isolates it from S. The proof applies to arbitrary index sets, including non-directed families. The empty join is (∅,∅).

**Attempted failure:** defects S_i may accumulate at the boundary of c_i; this is allowed. They cannot newly accumulate at a point p of S within c, because such a p belongs to some c_i and is isolated there.

## A2. Binary meets: PASS

The defect of the meet is \([(c_1\setminus v_1)\cap c_2]\cup[(c_2\setminus v_2)\cap c_1]\), a finite union of relatively closed discrete subsets of \(c_1\cap c_2\). Such finite unions remain relatively closed discrete. Top and bottom are (K,K) and (∅,∅), respectively. Coordinatewise operations therefore make L a frame.

## A3. Ordinary points, spatiality, sobriety, T1: PASS

Set \(e=(\varnothing,K)\). Both coordinate projections L→O(K) are frame homomorphisms, and evaluation gives the two families of ordinary points. For any frame point \(h:L\to2\), h(e) is 0 or 1; if 0, h(a)=h(a∨e) factors through the closed-sheet quotient O(F)≅O(K); if 1, h(a)=h(a∧e) factors through O(U)≅O(K). Thus there are no third-kind points. Coordinate evaluations separate distinct \((c,v)\) and hence L is spatial; the point space is its sober spectrum. Point complements are respectively \((K\setminus\{p\},K)\) and \((K,K\setminus\{p\})\), so T1 holds.

**Attempted failure:** a potentially new sobrification point arising from a nonprincipal filter is excluded by the dichotomy h(e)=0/1 and sobriety of each K sheet.

## A4. Compactness and compact-open local basis: PASS

Both sheets are compact as subspaces isomorphic to K, so their union X is compact. An additional direct frame proof uses the first-coordinate finite subcover and finitely many residual points. For a clopen d and finite S⊆d, the element \(b_{d,S}=(d,d\setminus S)\) is compact: from an arbitrary cover choose finitely many terms whose first coordinates cover d. Their aggregate defect intersect d is **closed discrete in compact d**, hence finite. Finitely many further members cover all its points outside S. The elements (∅,d) are compact because d is compact in U.

At an F-point p of a target open (c,v), either p∈v (choose d⊂c∩v) or p∈c\setminus v (choose d⊂c isolating p from the relatively discrete defect). These yield \(b_{d,\{p\}}\le(c,v)\). At a U-point use (∅,d). Thus compact opens form a basis, the frame is algebraic/continuous, and X is locally compact.

**Attempted failure:** an infinite relative defect in an open c may accumulate outside c, but the compactness argument intersects a defect with a *clopen compact d contained in c_** (the finite union of first coordinates). That intersection is finite. No compactness assertion was made for arbitrary opens.

## A5. Failure of stable local compactness: PASS

Both \(e=(\varnothing,K)\) and \(b_p=(K,K\setminus\{p\})\) are compact opens. Their meet is \((\varnothing,K\setminus\{p\})\), which admits a cover by the (0,d) with clopen d⊂K\setminus\{p\}, with no finite subcover because p is nonisolated. Thus compact elements are not meet-stable. In an algebraic frame this witnesses failure of stable continuity and explains why independently blind-refereed (A-SC) is inapplicable.

## A6. Fitted points: PASS, with independent second proof

U-sheet points are fitted: for each p, the meet of the open sublocales (∅,d), with clopen d∋p, is the point sublocale in U and hence X.

For p_F, put \(b_{p,d}=(d,d\setminus\{p\})\) and \(T=\bigwedge_{d\ni p}O_X(b_{p,d})\). The restriction to U is \(\bigwedge O_U(d\setminus\{p\})=0\): each is below O_U(K\setminus\{p\}), while the meet of O_U(d) over clopen d∋p is the *closed point* [p] (the clopens are also closed sublocales), disjoint from O_U(K\setminus\{p\}). As U and F are complementary sublocales, T∧U=0 implies T≤F. Restrict to F to get \(T=\bigwedge O_F(d)=[p_F]\). These b-neighborhoods are cofinal, so the meet of **all** p_F-neighborhoods is [p_F].

**Independent generalized-map cross-check:** Let h:E→X land in every \(O_X(b_{p,d})\). On the open of E where h lands in U, the induced map to K would have to land in each O_K(d\setminus\{p\}); their sublocale meet is zero. Therefore that open of E is zero and h factors through F. It then lands in all clopen neighborhoods d of p in F≅K, so it factors through the point p_F. This proves point-fitting without any inference from an intersection of ordinary points.

**Most sensitive audit point:** the open and closed complements satisfy \(O_X(e)\vee C_X(e)=X\) and \(O_X(e)\wedge C_X(e)=0\) in the distributive sublocale lattice; the conclusion T≤F uses that fact. This should be verified by the independent referee.

## A7. Nontrivial generalized comparison: PASS

The double-negation nucleus \(j(c)=\operatorname{int}\overline c\) is a *frame homomorphism into the quotient frame* RO(K), whose joins are regularizations of unions (not necessarily ordinary unions). Therefore composing j with the two frame coordinate projections yields frame maps f*,g*:L→RO(K). The relative discrete defect has empty interior in c because K is perfect; equivalently, c∩v is dense in c and c⊆cl(v), whence j(c)≤j(v). On e, f*(e)=0 and g*(e)=1. Since RO(K) is nontrivial, f and g are distinct maps from a nonzero locale, with f≤g. This proves \(\mathcal A(X)\ne\Delta_X\).

RO(K) is atomless since K is perfect zero-dimensional Hausdorff, so this nonzero source is pointless; the comparison is invisible to ordinary specialization points.

## A8. Stronger zero-fiber / maximal-TU-core claim: PASS

For any open a=(c,v) meeting F, c≠∅, hence j(c)≠0. Restrict the Boolean source to its nonzero open O(j(c)); then both f and g land inside O_X(a), remain comparable, and still disagree on e. So every such open is nonTU. All opens contained in U are TU since K Hausdorff. Thus \(U_{\mathrm{TU}}=U\), \(F_{\mathrm{TU}}=F\cong K\), a crowded closed core. The normalized defect E_e supports the Boolean witness, and its fibers over all F-points vanish by A6.

## A9. Countability claims: PASS

At p_F the \(b_{p,d}\), with d drawn from a countable clopen local base of Cantor K, are cofinal; at p_U use (∅,d). Thus X is first-countable. Suppose X had a countable base. For every p∈K a basis member B_p containing p_F yet not p_U must exist, forcing p into the relative defect of B_p. Each defect is a discrete subspace of the second-countable K and hence countable. Countably many basis defects cannot cover the uncountable K. So X is not second-countable.

## Editorial repairs and status

1. The original source note should be read with the above second proof of fitting, and explicit confirmation of which frame carries the RO(K) joins.
2. The blind packet must be self-contained and omit pointers to prior internal evaluations; it should request independent verdicts on A1–A7 first, and A8–A9 separately.
3. Do not mark (LC-PT) settled or canonical before the external report. Do not give the referee this internal audit; release only the prompt and revised blind packet.
4. Literature priority and possible abstract analogues remain unchecked. If the audit passes, the second-countable variant is a natural follow-up, not a theorem.
