# Project A — What obstructs I=U ⇒ U=F? Candidate hypotheses and a perfect-quotient theorem

**19 October 2026. Status: new working positive criterion and hypothesis triage, internally argued, not externally refereed or priority checked.** Here X is a strongly locally compact sober **topological space** and I,U,F are the closed localic relations from [A-consolidated-theorems.md](A-consolidated-theorems.md), assumed I=U. We distinguish ordinary quotient maps from possible general localic coequalizers.

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

**Compactness of classes + closedness is a sufficient pairing; each by itself remains to be tested.** The old and new plank constructions have closed q but fail (a): the nontrivial classes A,B are noncompact. Therefore the criterion directly pinpoints one missing resource. This is **not** yet an intrinsically choice-free locale theorem.

## 3. Structural reformulations to test

- **Proper/perfect inseparability quotient** (topological terminology): a closed map with compact fibers. This is the proved criterion above. Intrinsically in locales, test properness of the two projections p_i:E→X or of the quotient map to the frame of E-invariant opens. Properness of p_i ought to imply appropriate compactness and closed saturation, but this must be verified against the point-free definition; do not automatically assert a categorical equivalent.
- **Saturated-open frame:** with p_i:E→X, define L_E={u∈O(X):p_1^*(u)=p_2^*(u)}, the opens saturated for E. It represents O(Q). Complete regularity of L_E (or normality + T1 of Q) suffices for E=F. Merely asking it to be functionally Hausdorff is **equivalent to the desired conclusion** rather than a new criterion; distinguish structural assumptions from restatements.
- **Stable continuity/stable algebraicity or local coherence:** compact elements of O(X) closed under finite meets (the algebraic specialization) or multiplicativity of ≪, as in stably continuous frames. The cofinite-cloud counterexample fails dramatically: choose disjoint compact-open T-neighborhoods K_0,K_1 of distinct points in A (e.g. K_i=(α,ω1]×{i} with i=0,1); set u_i=K_i∪S_A^N for the SAME cofinite tail. Then u_i are compact open in X but u_0∧u_1=S_A^N, an infinite discrete open, **not compact**. Thus stability is a genuine algebraic exclusion rather than a topological adornment. Unknown whether stable continuity + I=U forces U=F in general. **Caution:** known Keimel–Lawson/Goubault-Larrecq theorems imply a stably locally compact T1 space is Hausdorff; this makes the T1-only case formally trivial, but non-T1 continuous frames still warrant attention. See https://topology.lmf.cnrs.fr/weakly-hausdorff-spaces-and-locally-strongly-sober-spaces/ .
- **Compact saturation of compact neighborhoods:** test K compact ⇒ E[K] compact, plus closedness of saturation C closed⇒E[C] closed (the latter is q closed). As K={x} is compact, the former forces compact E-classes; combined with closedness, the theorem applies. A version using properness of the relation projections is more intrinsically localic.
- **Countable or local exhaustion properties:** X kω, weakly locally compact σ-compact, locally countable union of σ-compact opens, or paracompact. Already *proved sufficient* in the working notes via compact quotients/Tietze; they are useful landmarks but not the sharp local obstruction. One could ask for countable exhaustion of **E-saturated** compact patches instead of whole X, potentially strictly weaker.
- **Fitness or a suitably relative fitness/subfitness condition:** subfitness by itself fails (T1 example). Fitness is worth checking separately, but no proof has been made that the present example is or is not fit. Avoid assuming fitness implies ordinary regularity, or that T1 already implies fitness of a locale; it implies subfitness only.
- **One-step relative compact interpolation:** for algebraic L, test whether each far compact pair k,l (k*∨l*=1) admits some c∈L with k≺c≺l*. Our compact-open witnesses fail *even this one-step version*. It is strictly more elementary to check than a complete dyadic ≺≺ interpolation; do **not** assume that one step suffices for U=F without an additional iteration hypothesis.

## 4. Proposed order of investigation

**First:** derive an intrinsically localic properness theorem for E projections/quotients; this has a definite topological model and targets exactly the obstruction. **Second:** test stable continuity / multiplicative way-below, separating T1-trivial consequences from truly non-T1 possibilities. **Third:** test finite compact interpolation and fitness, with finite/Alexandrov and cofinite-cloud models. Only then explore set-theoretic/cardinal modifications of σ-compactness.

**Novelty caution:** proper/perfect quotients preserving local compactness and compact-class separation are classical techniques. The theorem above is a direct combination applied to the localic hierarchy; no priority claim is made.
