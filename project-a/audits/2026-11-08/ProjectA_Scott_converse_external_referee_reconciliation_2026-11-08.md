# Project A — Reconciliation of the blind Scott-continuity referee report

**8 November 2026.** Source: `ProjectA_Scott_converse_EXTERNAL_referee_report_2026-11-08.md`, an independent blind external report on the 8 Nov packet. This is a post-referee **internal reconciliation**, not a second independent review; preserve the referee's report unchanged. No literature-priority claim.

## 1. Executive disposition

**Accept the referee's strengthened Theorem T′**, after independent reconstruction of the proof. The weak-local-compactness hypothesis of the previous Theorem T is unnecessary for the equivalence between Scott continuity and perfectness of the projection. Preserve weak local compactness for the **separate uniform compact-support condition T3**, where it is genuinely needed.

**Accept the packet's Theorem L** under classical Hofmann–Lawson and product-spatiality hypotheses; the referee confirms the representation and closed-Frobenius bridge. **Accept the natural strengthening L′ conditionally on spatiality of the localic product**, which is a standard sufficient setting for the same spatial argument. In general arbitrary locales, the converse is still OPEN.

The suggested upper-powerlocale proof for arbitrary locales (§7.2 of the referee report) remains a **conditional idea**, not a theorem, because properness of its generic relation projection K→P_U X was expressly left unverified. Likewise the §4 application to effective quotients was explicitly *not* comprehensively refereed.

Terminology: **directed families are nonempty** throughout (including when a projection is not onto).

## 2. Correct general topological theorem T′

Let X,Y be arbitrary topological spaces, E⊆X×Y closed, p_X,p_Y its projections, and

    r_E(U)=(p_Y)_* p_X^*(U)=int_Y(Y\E[X\U]).

Then the following are equivalent:

- (T1) r_E preserves nonempty directed joins.
- (T1top) for every nonempty directed family (U_i) of opens of X with ∪U_i=X, one has ∪r_E(U_i)=Y.
- (T2) p_Y:E→Y is closed with compact point-fibers.

The forward implications are *independently rechecked*:

**Compact fibers.** E_y is closed in X. If directed (U_i) covers E_y, then V_i=U_i∪(X\E_y) is a directed open cover of X. (T1top) gives some i with y∈r_E(V_i), whence E_y⊆V_i and therefore E_y⊆U_i. Directedness plus the arbitrary-cover-to-directed-finite-unions argument proves compactness of E_y.

**Closed projection.** Let H be closed in E, hence closed in X×Y, and y∉p_Y(H). Consider *all* pairs (A,B) of opens with y∈B and (A×B)∩H=∅. The A-components cover X: for each x, (x,y)∉H. Index finite collections F of these pairs, and U_F the union of their A-components. Then U_F is a nonempty directed open cover of X. (T1top) yields finite F with y∈r_E(U_F); on some open W∋y the E-points have first coordinate in U_F. Intersect W with the finitely many corresponding B-components to obtain an open neighborhood of y disjoint from p_Y(H). Thus p_Y(H) is closed. Choosing *all* rectangles avoids the modest implicit choice step in the referee's x-indexed presentation.

**Reverse.** A closed map with compact fibers has Scott-continuous f_* (for a nonempty directed family of opens), by fiber compactness and closedness formula f_*(V)=Y\f(Z\V). As p_X^* preserves arbitrary joins, r_E is Scott-continuous. No local compactness or relation axioms are involved.

The compactness of each fiber can also be read from T1top directly for arbitrary open covers: pass to the directed finite unions. The top-level directed-cover property is equivalent to full Scott continuity *under these hypotheses*, NOT as a claim about arbitrary locale relations.

## 3. Compact-support T3 is genuinely stronger without local compactness

T3: every y has an open neighborhood W and compact K⊆X with E∩(X×W)⊆K×W.

- T3⇒T2 whenever E is closed (tube lemma and closed fibers; no Hausdorffness).
- T2⇒T3 when X is **weakly locally compact**, by compact fibers plus a finite relatively-compact open cover and the closed-map formula for r_E.
- Without this source hypothesis T2 need not imply T3: X=Y=ℚ, E=Δ_ℚ (topological diagonal, closed), r_E=id and p_Y a homeomorphism, but T3 would give an open Q-neighborhood contained in a compact Q-subspace, contradicting non-local-compactness of ℚ.

Thus the earlier packet theorem and tube-lemma proof remain correct but **not optimal for T1⇔T2**.

## 4. The localic lift and limits

Under classical mathematics, let X,Y be spatial locales whose **localic product is spatial and identified with the topological product** of their point spaces; let E↪X×_loc Y be closed. The T′ correspondence, the right-adjoint closed-map formula, and the explicit co-Frobenius identity show

    (p_Y)_*p_X^* Scott-continuous  ⇔  p_Y:E→Y proper.

This is the referee's L′. Product spatiality is sufficient because all points of a localic product are coordinate pairs and rectangle opens generate the product frame; it is not asserted for arbitrary spatial locales. The original L (continuous O(X), Y=X) is a special case by Hofmann–Lawson and Isbell. The reverse implication works for all locales, constructively.

**No automatic collapse to functional equality:** Vermeulen's effectiveness and proper-quotient arguments, continuity of quotient, closed diagonal, and F=kernel-pair of complete regularization are separate dependencies. The external report intentionally left those out of primary review. Q06 must retain its independent provenance.

## 5. The proposed arbitrary-locale proof via upper powerlocale

The referee notes that r_E preserves finite meets, and its Scott continuity makes it a preframe morphism ΩX→ΩY, hence classifies a map φ:Y→P_U X. This is consistent with the established presentation of the upper powerlocale as the free frame on ΩX as a preframe (Vickers). Let K↪X×P_U X impose the inequalities □u≤u in the respective coordinates; by adjunction E is contained in (1_X×φ)^{-1}(K). E's closed inclusion into that pullback is proper. Therefore the proposed **unrestricted localic implication** follows *if* K→P_U X is proper.

The latter is precisely the referee's unchecked step §7.2(f). General claims about global points of P_U X representing compact fitted sublocales do **not by themselves prove** relative properness of the generic family. We have not verified the needed statement from a primary source. Retain **L\*** as OPEN; the proposed route as a **focused conjectural proof strategy**, not an E- or I-class theorem. The mechanism is potentially important enough to warrant a targeted, source-precise check, not wholesale launch of a new program.

## 6. Other findings, caveats and editorial fixes

1. **Directed = nonempty** must be explicit: for E=∅, Y≠∅, f_*∅=Y, so empty-join preservation would fail despite properness.
2. **Closedness of E is necessary** for the forward implication: X=one point, E=one point×A where A⊆Y is not closed; r_E is automatically Scott-continuous (on a two-element domain), while p_Y need not be closed.
3. **The referee's §6.4 semi-proper⇒proper observation** is valid for these projections in the spatial-product regime: if p_Y* is Scott-continuous, so is r_E, and the theorem supplies the missing Frobenius. It is false for arbitrary maps.
4. **The upper-powerlocale identification** supplies a conceptual explanation but needs a carefully cited geometric/fiberwise interpretation; no novelty claim.
5. **Literature priority** of T′/L′ has not been exhaustively checked. This is near the classical upper-Vietoris compact-valued multifunction and Bourbaki-properness theory; correctness and novelty are separate questions.
6. **Choice-free proof** of T′: use all admissible avoiding rectangles rather than a chosen rectangle for each x. L still uses classical spatiality/representation if proved by this route.

## 7. Status changes and next action

- **Q04**: change statement to **T′ with arbitrary topological X,Y**; status **E* (referee-origin strengthening, independently checked internally)**; keep the original weak-local-compactness proof as a valid special proof, not the canonical sharp statement.
- **Q04a/T3**: preserve as separate **weak-local-compactness-only equivalence**; referee checked, and the Q diagonal shows the hypothesis is necessary for this formulation.
- **Q05**: status **E (within the precise classical continuous-frame scope)**, plus optional L′ for spatial localic products, independent check of product identification; do not extend to all locales.
- **Q06**: no automatic promotion; referee §5 requested source-exactness of quotient background and declined deep review.
- **PR-01**: OPEN for arbitrary possibly pointless localic squares. Add *referee's upper-powerlocale conditional proof*, with exact missing step K→P_U X proper, as a **bounded pending-check**, not as a settled theorem.
- **CK-02**: marked checked by external blind referee for T/L, with T′ stronger. Keep source for revisions.

Suggested sequence: preserve the referee report; integrate these corrections into the ledger; then prepare the *independent* coherent-composition referee packet. If desired, a separate, strictly focused question can be sent to the original Scott referee asking whether properness of K→P_U X follows from a precise published theorem. This is not a prerequisite for the coherent-composition audit.