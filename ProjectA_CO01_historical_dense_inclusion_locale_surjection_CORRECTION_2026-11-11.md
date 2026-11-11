# Important mathematical correction — dense set inclusion is NOT necessarily a locale-surjection

**11 November 2026. Identified during the independent re-audit associated with the positive Arrieta CO-01 theorem. This correction is firm and does not depend on the new theorem.**

Two earlier notes contain the invalid implication “D is dense in the topological space Y, therefore \(D_{\rm discrete}\to Y\) is a locale-surjection”:
- [Associativity audit I (7 Nov)](A-relational-composition-associativity-audit-I-2026-11-07.md), especially §1 and the resulting one-relation endorelation §7;
- [closed relation on a zero-dimensional locally compact Hausdorff locale (11 Nov)](ProjectA_CO01_closed_relation_nonassociativity_locally_compact_Hausdorff_2026-11-11.md), §1 and §2.

**Direct countercalculation.** Let C be Cantor, D⊊C a proper dense subset, and \(f:D_{\rm disc}\to C\) the inclusion. For p∈C\D, the two **distinct** opens \(C\) and \(C\setminus\{p\}\) have the **same** inverse image D. Thus \(f^*:\mathcal O(C)\to\mathcal P(D)\) is not injective. It follows that f is **not a locale-surjection**. The analogous cofinite example \(Y=\mathbb N\cup\{\infty\}\) also has distinct opens \(Y\) and \(Y\setminus\{\infty\}=\mathbb N\) with identical inverse images, so the inclusion \(\mathbb N_{\rm disc}\to Y\) fails to be a locale-surjection for the same reason.

Consequently **both purported nonassociativity constructions have an invalid key image calculation**. Neither specific example should be cited as a proved nonassociativity counterexample until independently replaced or repaired. The abstract fact that Loc is not a regular category and nonstable locale-surjections exist remains well-established, but these two particular explicit examples are NOT certified.

**What remains intact:** The independently checked/refereed mixed relation noncontainments in Project A are not derived from these concrete dense-inclusion images. The Arrieta Θ-cover nontransitivity theorem uses the explicit Boolean-valued generalized paths and not a false dense-inclusion surjection. The recent [CO-01 positive proof](ProjectA_CO01_Arrieta_square_saturates_remote_equivalence_PROOF_2026-11-11.md) uses an altogether different *genuine* locale-surjection: the composite
\[
(T\times V)_{\neg\neg}\hookrightarrow T\times V\to T
\]
with T Boolean. Its inverse image \(B=\mathcal O(T)\to\mathcal O((T\times V)_{\neg\neg})\) is literally injective because \(p^*:B\hookrightarrow\mathcal O(T\times V)\) has a point-section in V, and all its elements are complemented and thus fixed by double negation. This surjectivity must be independently audited, but it does not rely on density ⇒ surjectivity.

**Action:** Mark the earlier examples as withdrawn at their file headers and in the phase index. Do not claim this correction proves universal localic relation composition associative; it merely withdraws those particular advertised witnesses. If a general explicit nonassociativity example is needed later, design it using a **genuine** locale-surjection and independently check the pullback and endpoint image.
