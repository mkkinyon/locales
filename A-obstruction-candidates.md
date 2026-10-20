> **SOURCE CORRECTION (19 October 2026):** Vermeulen, *Proper Maps of Locales* (1994), **Corollary 5.17**, proves that **closed proper equivalence relations are effective on arbitrary locales**—without assuming compactness of the ambient locale. The earlier restriction to compact locales was a misreading of a later paper's application. For a continuous L, proper projections of I=U yield a proper continuous strongly Hausdorff quotient; Vermeulen supplies I=kerpair(q), and complete regularity of the quotient gives **I=U=F** entirely locally. See [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md).

# Project A — What obstructs I=U ⇒ U=F? Candidate hypotheses and a perfect-quotient theorem

> **STRONGER THEOREM (19 October 2026):** An arbitrary **closed equivalence relation** on a topological space whose projections are **perfect** (closed with compact fibers) has **Hausdorff quotient**, without using local compactness or Urysohn separation. Therefore for a strongly locally compact sober X with **transitive I=clΔ**, proper/perfect inseparability projections imply **I=U=F**. The hypothesis I=U is sufficient for transitivity but not otherwise needed. See [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md) for proof and a localic proper-quotient/closed-diagonal counterpart. This supersedes §2's extra I=U assumption.


**19 October 2026. Status: new working positive criterion and hypothesis triage, internally argued, not externally refereed or priority checked.** Here X is a strongly locally compact sober **topological space** and I,U,F are the closed localic relations from [A-consolidated-theorems.md](A-consolidated-theorems.md), assumed I=U. We distinguish ordinary quotient maps from possible general localic coequalizers.

> **Point-free transitivity update (19 October 2026):** A frame calculation now proves I∘I⊆U for *all* locales, hence I=U makes I an internal equivalence relation without assuming spatiality. The [proper-inseparability relation note](A-proper-inseparability-relations.md) also gives an intrinsic formula `r_I(u)=∨{v:1⊠v≤(u⊠1)∨d_I}` and a classical-ZFC **effectiveness theorem for closed proper equivalence relations on continuous locales** using compact saturated specialization classes. See the exact proof and imported proper-map correspondence there.

> **DECISIVE SUBFIT + ARITHMETIC UPDATE (20 October 2026, working):** The two properties **together** do not rescue I=U⇒U=F. Replace discrete plank clouds by **cofinite** clouds: the T1 nonsober precursor has an **arithmetic, algebraic, subfit** open frame; its sobrification adds two generic points but leaves the frame unchanged and satisfies **I=U⊊F** as closed localic relations. Full proof in [A-subfit-arithmetic-counterexample.md](A-subfit-arithmetic-counterexample.md). A **sober T1 arithmetic space**, by contrast, must be zero-dimensional and completely regular. Earlier candidate statements in this note are historical.

**NEW UPDATE (20 October 2026):** Subfit + arithmetic + I=U still does NOT imply I=F. Replacing the deleted-plank's discrete clouds by cofinite-topology clouds gives a T1 nonsober precursor with arithmetic subfit frame. Its sobrification is strongly locally compact sober and has I=U strictly below F. See [A-subfit-arithmetic-counterexample.md](A-subfit-arithmetic-counterexample.md). In contrast, any sober T1 arithmetic space is zero-dimensional and completely regular. Earlier questions in this note on the conjunction are superseded.

## 1. Conceptual translation: functional Hausdorffness of the inseparability quotient

Set E=I=U on points. It is an equivalence relation: symmetry/reflexivity are immediate; if xEy and yEz then for arbitrary open neighborhoods V∋x, W∋z, y∈cl(V)∩cl(W), so xUz, hence xEz.

Let Q=X/E, q:X→Q its topological quotient. By definition every continuous real-valued f:X→R is constant on E-classes and descends uniquely to a continuous f_bar:Q→R. Conversely every f_bar pulls back. Hence **as point relations**

    E=F ⇔ Q is functionally Hausdorff

(where functionally Hausdorff means any two distinct points are distinguished by some continuous R-valued map). For strongly locally compact sober X, localic products are spatial, so this pointwise test decides equality of our closed localic E and F. This exact reduction is useful but alone merely repackages the goal.

## 2. A nontrivial positive theorem: closed quotient with compact E-classes

**Theorem (working).** Suppose E=I=U on a strongly locally compact sober space X. If

(a) every E-equivalence class is compact (as a subspace of X), and

(b) the ordinary topological quotient map q:X→Q=X/E is **closed**,

then Q is **locally compact Hausdorff**, so

    I(X)=U(X)=F(X)

as closed localic relations.

**Proof of Hausdorffness.** Let C,D be distinct compact E-classes. For every x∈C,y∈D, because (x,y)∉U, choose open N_xy∋x and M_xy∋y whose closures are disjoint. Fix x. Finite compactness of D gives y_1,…,y_n such that D⊆⋃ M_xy_i. Put N_x=⋂ N_xy_i, M_x=⋃ M_xy_i. Then cl N_x∩cl M_x=∅ (closure of finite union is finite union). Finite compactness of C gives x_1,…,x_m such that C⊆⋃ N_x_j. Set N=⋃N_x_j, M=⋂M_x_j. Then C⊆N, D⊆M, cl N∩cl M=∅. Since q is closed, the sets

    N'=X\q^-1(q(X\N)),       M'=X\q^-1(q(X\M))

are open **saturated** neighborhoods of C,D and are contained in N,M. Their images are disjoint open neighborhoods of the two corresponding points of Q. Therefore Q Hausdorff.

**Proof of local compactness.** Fix z∈Q and K_z=q^-1(z), compact by (a). Strong local compactness of X gives for each x∈K_z an open neighborhood V_x and compact M_x with x∈V_x⊆M_x. By compactness of the fiber, finitely many V_x cover it; put V=finite union V_x and M=finite union M_x. Then M is compact, K_z⊆V⊆M. By closedness of q,

    W=Q\q(X\V)

is open and contains z. As q^-1(W)⊆V⊆M, one has W⊆q(M), a compact set. Thus Q locally compact. It is already Hausdorff, hence completely regular.

**Conclusion.** For two distinct E-classes, a real-valued map Q→R separates them. Pull it back to X. Hence E=F pointwise. As X×X is spatial and E,F are closed sublocales, equality holds localically. □

**Compactness of classes + closedness is sufficient; neither condition is sufficient alone for the properness method.** Closedness alone fails in both plank examples (noncompact classes). Compact classes alone do not force idempotence or properness: [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md) gives finite classes and a nonclosed quotient with I=U=F. Whether compact classes alone force I=F is a separate, unresolved question. The old and new plank constructions have closed q but fail (a): the nontrivial classes A,B are noncompact. Therefore the criterion directly pinpoints one missing resource. This is **not** yet an intrinsically choice-free locale theorem.

## 3. Structural reformulations to test

- **Proper/perfect inseparability quotient** (topological terminology): a closed map with compact fibers. This is the proved criterion above. Intrinsically in locales, test properness of the two projections p_i:E→X or of the quotient map to the frame of E-invariant opens. Properness of p_i ought to imply appropriate compactness and closed saturation, but this must be verified against the point-free definition; do not automatically assert a categorical equivalent.
- **Saturated-open frame:** with p_i:E→X, define L_E={u∈O(X):p_1^*(u)=p_2^*(u)}, the opens saturated for E. It represents O(Q). Complete regularity of L_E (or normality + T1 of Q) suffices for E=F. Merely asking it to be functionally Hausdorff is **equivalent to the desired conclusion** rather than a new criterion; distinguish structural assumptions from restatements.
- **Stable continuity/stable algebraicity or local coherence: SETTLED NEGATIVELY ALONE.** Compact elements closed under finite meets (the algebraic specialization), or multiplicativity of ≪, do **not** suffice for I=U⇒U=F: the **original two-tag deleted-plank construction has an arithmetic (algebraic, finite-meet-stable) frame**, although it is not subfit. The cofinite-cloud counterexample separately fails finite-meet stability dramatically: choose disjoint compact-open T-neighborhoods K_0,K_1 of distinct points in A (e.g. K_i=(α,ω1]×{i} with i=0,1); set u_i=K_i∪S_A^N for the SAME cofinite tail. Then u_i are compact open in X but u_0∧u_1=S_A^N, an infinite discrete open, **not compact**. Thus finite-meet stability excludes the **cofinite-cloud** mechanism but does **not** exclude the **two-tag** mechanism. The combined hypothesis **subfitness + stable continuity** remains untested. **Caution:** known Keimel–Lawson/Goubault-Larrecq theorems imply a stably locally compact T1 space is Hausdorff; this makes the T1-only case formally trivial, but non-T1 continuous frames still warrant attention. See https://topology.lmf.cnrs.fr/weakly-hausdorff-spaces-and-locally-strongly-sober-spaces/ .
- **Compact saturation of compact neighborhoods:** test K compact ⇒ E[K] compact, plus closedness of saturation C closed⇒E[C] closed (the latter is q closed). As K={x} is compact, the former forces compact E-classes; combined with closedness, the theorem applies. A version using properness of the relation projections is more intrinsically localic.
- **Countable or local exhaustion properties:** X kω, weakly locally compact σ-compact, locally countable union of σ-compact opens, or paracompact. Already *proved sufficient* in the working notes via compact quotients/Tietze; they are useful landmarks but not the sharp local obstruction. One could ask for countable exhaustion of **E-saturated** compact patches instead of whole X, potentially strictly weaker.
- **Fitness or a suitably relative fitness/subfitness condition:** subfitness by itself fails (T1 example). Fitness is worth checking separately, but no proof has been made that the present example is or is not fit. Avoid assuming fitness implies ordinary regularity, or that T1 already implies fitness of a locale; it implies subfitness only.
- **One-step relative compact interpolation:** for algebraic L, test whether each far compact pair k,l (k*∨l*=1) admits some c∈L with k≺c≺l*. Our compact-open witnesses fail *even this one-step version*. It is strictly more elementary to check than a complete dyadic ≺≺ interpolation; do **not** assume that one step suffices for U=F without an additional iteration hypothesis.

## 4. Proposed order of investigation

**First (resolved):** Vermeulen (1994), Cor. 5.17, gives effectiveness of closed proper internal equivalence relations; continuity of the quotient yields I=U=F. See [A-vermeulen-effectiveness-correction.md](A-vermeulen-effectiveness-correction.md). **Second (resolved negatively alone):** stable continuity/arithmeticity fails to imply the collapse, by the two-tag example. Test **subfit + arithmetic** instead. **Third (open):** test finite compact interpolation and fitness, with finite/Alexandrov and cofinite-cloud models. Also investigate idempotence/Scott continuity of r_I separately from complete regularity of the quotient; neither is equivalent to I=F. Only then explore set-theoretic/cardinal modifications of σ-compactness.

**Novelty caution:** proper/perfect quotients preserving local compactness and compact-class separation are classical techniques. The theorem above is a direct combination applied to the localic hierarchy; no priority claim is made.
