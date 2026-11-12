# Project A — Strongly countably distributive Boolean bases: exact full/finite fitted-diagonal product formulas for countably based fibers

**12 November 2026 — NEW INTERNAL THEOREM; NOT EXTERNALLY AUDITED OR PRIORITY CHECKED.** Derived after the decisive Arrieta strongly Hausdorff anti-Urysohn no-go for generalized predecessor spans ([the preceding two-apex/Arrieta note](ProjectA_Q_SPECIALIZATION_SPAN_TWO_APEX_TEST_AND_ARRIETA_HAUSDORFF_NO_GO_2026-11-12.md)). This gives a positive answer to the POINTFREE PRODUCT TRANSFER question for a new class of noncompact, genuinely pointless cases even when \(\Sigma(Y)=\Delta_Y\) is FAR from dense in W₂(Y). More strongly, it computes the **NONCLOSED** full and finite fitted diagonals themselves, not just their closed hulls.

**Main theorem.** Let \(Z\) be a Boolean locale, with \(\mathcal O(Z)=M\) a COMPLETE Boolean algebra satisfying the **STRONG countable distributivity** property: EVERY countable family of partitions of \(1_M\), with arbitrary (not necessarily countable) numbers of parts, has a common partition refinement. Let Y be a locale with a COUNTABLE OPEN BASIS. Then
\[
\boxed{
\mathcal D(Z\times Y)=\Delta_Z\times\mathcal D(Y),\qquad
\mathcal D_2(Z\times Y)=\Delta_Z\times\mathcal D_2(Y);
}
\]
and
\[
\boxed{
\mathcal W(Z\times Y)=\Delta_Z\times\mathcal W(Y),\quad
\mathcal W_2(Z\times Y)=\Delta_Z\times\mathcal W_2(Y),\quad
\mathcal U(Z\times Y)=\Delta_Z\times\mathcal U(Y).
}
\]
No compactness, spatiality, local compactness, coherence, span density, or finite-subcover assumption on Y. For NONZERO Z, all three equality levels D=D₂, W=W₂, and W₂=U are preserved AND reflected. In particular Q and Q′ transfer and reflect.

The strong distributivity hypothesis is also called \((\omega,\infty)\)-distributivity; we state it **explicitly** rather than equivocating with weaker \((\omega,2)\)-distributivity or “no new reals” conventions. A standard reference is Jech, *Set Theory*, Ch. 15 (partition formulation of distributivity), https://fa.ewi.tudelft.nl/~hart/37/onderwijs/set_theory/Jech/15-applications_of_forcing.pdf, Lemma 15.37. A countably CLOSED dense forcing order yields this strong countable distributivity in its complete Boolean completion, e.g. \(2^{<\omega_1}\) with countable-length conditions (Hamkins discussion https://mathoverflow.net/questions/476589/countably-compact-boolean-algebras-versus-distributivity).

## 0. Boolean partition refinement and the countable basis

Let \(M\) be complete Boolean. A **partition of 1** means a set of pairwise disjoint nonzero \(m_i\in M\) with join 1.

**Definition (strong countable distributivity SDω).** For any countable sequence \((\mathcal P_n)_{n\in\omega}\) of partitions of 1 (each allowed to have arbitrary cardinality), the elements
\[
\mathcal P=\left\{\bigwedge_{n\in\omega}p_n:\ p_n\in\mathcal P_n,\quad\bigwedge_np_n\ne0\right\}
\tag{0.1}
\]
form a common refinement partition of 1: they are pairwise disjoint and have join 1. Equivalently
\[
1=\bigvee_{(p_n)\in\prod_n\mathcal P_n}\bigwedge_np_n.
\]
This is the ONLY distributivity hypothesis used below.

Let \(L=O(Y)\) have a countable join-generating basis \(\mathcal B=\{b_n:n\in\omega\}\), including zero if convenient; every v∈L is the join of the basis elements beneath it.

**Lemma 0.1 (canonical rectangle coefficients).** Every \(c\in O(Z\times Y)=M\oplus L\) has a representation
\[
\boxed{c=\bigvee_{n\in\omega}u_{c,n}\boxtimes b_n,\quad
u_{c,n}=\bigvee\{a\in M:a\boxtimes b_n\le c\}.}
\tag{0.2}
\]
*Proof.* The supremum defining u_{c,n} still satisfies \(u_{c,n}\boxtimes b_n\le c\) because the map \(a\mapsto a\boxtimes b_n\) preserves arbitrary joins. Rectangles join-generate the product frame; express each Y-coordinate open v of a rectangle beneath c as the join of its basis elements \(b_n\le v\), and collect coefficients for each n. □

## 1. The Boolean finiteization lemma for an ARBITRARY product cover

**Theorem 1.1 (Boolean partition localization, NEW).** For an ARBITRARY cover C⊆O(Z×Y), there is a Boolean partition \(\mathcal P\) of 1_M such that for EVERY nonzero cell m∈P, one can choose a Y-open cover
\[
\boxed{\mathcal V_m=\{v_{c,m}:c\in C\},\quad
\bigvee_{c\in C}v_{c,m}=1_Y,\qquad
m\boxtimes v_{c,m}\le c\quad(\forall c\in C).}
\tag{1.1}
\]
At MOST COUNTABLY many of the v_{c,m} are nonzero (and if C is FINITE the family is finite).

*Proof.* Let u_{c,n} be the coefficients (0.2). For every n put \(u_n=\bigvee_{c\in C}u_{c,n}\in M\). By standard maximal-antichain refinement in a complete Boolean algebra, choose a partition \(\mathcal P_n\) of 1 with each part either
- below \(u_n^c\), OR
- below some \(u_{c,n}\) and labeled by one such c.

That such a partition exists follows by choosing a maximal pairwise disjoint nonzero family refining the cover \(\{u_n^c\}\cup\{u_{c,n}:c\in C\}\) of 1, using classical choice.

By SDω choose a COMMON partition refinement \(\mathcal P\) for the countably many \(\mathcal P_n\). Fix m∈P, m≠0. For each n the containing \(\mathcal P_n\)-cell either lies below \(u_n^c\), in which case \(m\wedge u_{c,n}=0\) for ALL c, or lies below a selected \(u_{c_n,n}\), in which case \(m\boxtimes b_n\le c_n\). Let \(J_m\subseteq\omega\) be the selected n's, with respective c_n∈C.

Define \(v_{c,m}=\bigvee_{\{n\in J_m:c_n=c\}}b_n\). Then \(m\boxtimes v_{c,m}\le c\) for every c, and at most countably many v_{c,m} are nonzero. Moreover, for ALL c,
\[
(m\boxtimes1)\wedge c
=\bigvee_n(m\wedge u_{c,n})\boxtimes b_n
\le m\boxtimes\bigvee_{n\in J_m}b_n.
\]
Since C covers Z×Y, joining over c yields
\[
m\boxtimes1\le m\boxtimes\bigvee_{n\in J_m}b_n.
\]
For m≠0, \(m\boxtimes v=m\boxtimes1\Rightarrow v=1_Y\), because otherwise the NONZERO product of the open locale O_Z(m) with the nonzero closed complement C_Y(v) would be killed by the top but disjoint from the displayed rectangle. Therefore \(\bigvee_{n\in J_m}b_n=1_Y\), and hence \(\bigvee_c v_{c,m}=1_Y\). □

**IMPORTANT:** The proof localizes **arbitrary full covers C**, not only finite or countable covers, because the countable index n comes from the Y BASIS. The partitions \(\mathcal P_n\) can have UNCOUNTABLY many pieces, which explains why we genuinely need STRONG SDω, not merely a weak binary distribution hypothesis.

**A subtle difference between full and finite:** If C has k elements, J_m may still be infinite, but the selected b_n's are grouped by their ORIGINAL c label to form the k-element Y cover \(\{v_{c,m}:c\in C\}\). Hence finite X-covers ALWAYS yield finite Y-covers on each cell. Do NOT stop at a countable Y-cover in the finite case.

## 2. Exact full/finite fitted diagonal products

Write \(\epsilon\in\{\mathrm{all},2\}\).

**Theorem 2.1 (NONCLOSED fitted-diagonal product formula, NEW INTERNAL).** Under the hypotheses on Z and Y,
\[
\boxed{
\mathcal D_\epsilon(Z\times Y)
=\Delta_Z\times\mathcal D_\epsilon(Y).}
\tag{2.1}
\]

*Proof: lower bound.* Fix any X-cover C, finite when ε=2. Apply Theorem 1.1 to obtain \(\mathcal P\) and honest Y-covers \(\mathcal V_m\), finite whenever C finite. On the relative locale
\(\Delta_Z\times\mathcal D_\epsilon(Y)\cong Z\times\mathcal D_\epsilon(Y)\),
over the open base cell m, each inclusion \(m\boxtimes v_{c,m}\le c\) implies that the diagonal-square restriction of \(w_C^X\) dominates the relative pullback of
\[
w_{\mathcal V_m}^Y=\bigvee_{c\in C}v_{c,m}\boxtimes v_{c,m}.
\]
But \(\mathcal D_\epsilon(Y)\le O(w_{\mathcal V_m}^Y)\), because \(\mathcal V_m\) is a cover of the appropriate type. Hence \(w_C^X\) is TOP on \(m\times\mathcal D_\epsilon(Y)\). The m's cover 1_Z, so \(w_C^X\) is top on ALL of \(\Delta_Z\times\mathcal D_\epsilon(Y)\). Since C was arbitrary, the desired lower inclusion holds for the full or finite fitted diagonal.

*Proof: upper bound.* The full and finite fitted diagonals are LAX-NATURAL under projections: any generalized pair matching all (resp. finite) covers of Z×Y matches the pullbacks of all (resp. finite) covers of Z and Y. Hence
\[
\mathcal D_\epsilon(Z\times Y)
\le\mathcal D_\epsilon(Z)\times\mathcal D_\epsilon(Y).
\]
Because the frame M=O(Z) is BOOLEAN, each of its opens is complemented. Compatibility with the two-element cover \(\{u,\neg u\}\) forces equality of the coordinate maps on u for EVERY u∈M, so
\[
\mathcal D(Z)=\mathcal D_2(Z)=\Delta_Z.
\]
This gives the upper inclusion \(\mathcal D_\epsilon(X)\le\Delta_Z\times\mathcal D_\epsilon(Y)\). The two inclusions give equality. □

**Theorem 2.2 (closed hull and U formulas).**
Taking CLOSURES in (2.1) and using the previously proved closure-of-product identity and the fact that Δ_Z is already CLOSED gives
\[
\boxed{
\mathcal W(Z\times Y)=\Delta_Z\times\mathcal W(Y),\qquad
\mathcal W_2(Z\times Y)=\Delta_Z\times\mathcal W_2(Y).}
\tag{2.2}
\]
The unrestricted pointfree U product formula gives
\[
\boxed{\mathcal U(Z\times Y)=\Delta_Z\times\mathcal U(Y).}
\tag{2.3}
\]

**Corollary 2.3 (ALL equality levels reflected).** For NONZERO Z, multiplication with Z reflects and preserves the equality D=D₂, W=W₂, W₂=U (and also W=U). This follows by pulling back along the faithfully nonzero product factor, or by noting any strict inclusion of sublocales of Y² has a nonzero open/closed relative difference whose product with Z remains nonzero. In particular Q(X) iff Q(Y), and Q′(X) iff Q′(Y).

**No claims:** This theorem does not apply to the Cohen Boolean algebra RO(Cantor) (which is NOT countably distributive), to arbitrary uncountably based Y, or to general nonBoolean Z. Countably distributive is a strong assumption about the BOOLEAN BASE frame, not compactness of Z (indeed nontrivial atomless Z here is noncompact).

## 3. An entirely pointless NONREGULAR Urysohn example with NO predecessor spans off diagonal

Let \(P\) be the countably closed forcing of countable partial functions \(p:\omega_1\rightharpoonup\{0,1\}\), ordered by extension. The union of a decreasing countable chain of conditions is a condition, so P is σ-closed. Any condition splits by a fresh ordinal coordinate, so P is atomless. Let
\[
M=\operatorname{RO}(P),\qquad Z=\operatorname{Loc}(M).
\tag{3.1}
\]
The COMPLETE Boolean algebra M is atomless, hence Z has NO ordinary points, and is STRONGLY countably distributive because its forcing has a σ-closed dense subset (the conditions P). This is an established set-theoretic fact; see Jech and the references cited in the introduction. Z is nonzero and not compact.

Let A be Arrieta's spatial, strongly Hausdorff, ANTI-URYSOHN locale from Example 4.5, 2024, built from Cantor space by removing a countable family of compact sets K_n and adjoining n∈ω. A has a COUNTABLE OPEN BASIS: the traces of the countable clopen cylinder basis of Cantor on the remaining subspace, plus for each n the neighborhoods \(\{n\}\cup(V\cap Y)\) where V runs through finite unions of clopen cylinders covering K_n. Compactness of each K_n permits these to refine every basic n-neighborhood. Hence Theorem 2.1 applies to X=Z×A.

Arrieta gives
\[
I(A)=\Delta_A,\qquad U(A)=A²,\qquad W(A)=W₂(A)=A²
\]
(the last equality by our regular-closed U theorem). Therefore
\[
\boxed{
\begin{aligned}
D(X)&=\Delta_Z\times D(A),\quad
D_2(X)=\Delta_Z\times D_2(A),\\
W(X)&=W₂(X)=U(X)=\Delta_Z\times A²,\\
I(X)&=\Delta_Z\times\Delta_A=\Delta_X,\qquad
\Sigma(X)=\Delta_X.
\end{aligned}}
\tag{3.2}
\]
Moreover, the diagonal Δ_Z has ZERO ambient interior since M is atomless: no nonzero pure rectangle lies inside it, by splitting any nonzero common Boolean part into disjoint nonzero subparts. Therefore
\[
\boxed{
\operatorname{int}U(X)=0,\qquad
G_\perp(X)=U(X)\wedge O(d_{I(X)})\ne0.
}
\tag{3.3}
\]
The latter follows because A is ordinary Hausdorff with two distinct points, giving disjoint nonzero opens a,b, so Δ_Z×O(a⊠b) is a nonzero U-region outside I.

**THIS IS THE NEW POSITIVE MECHANISM.** X is ENTIRELY POINTLESS, is strongly Hausdorff, has \(\operatorname{int}U=0\), and has a NONZERO OFF-INSEPARABILITY Urysohn boundary where:
- the regular-closed-core mechanism supplies NOTHING;
- the predecessor-span core is ONLY Δ_X and supplies NOTHING off inseparability;
- Y=A is NONCOMPACT and ordinary-point predecessor lifts cannot work;
- the exact full/finite equality is proved by **strong Boolean countable distributivity plus a countable Y basis**.

It is a positive Q and Q′ example, NOT a counterexample. This is precisely the kind of nonregular pointfree fitting density left unexplained by the earlier two mechanisms.

**Comparison with the unresolved Cohen-base product.** If we instead choose the standard COHEN Boolean base \(M_C=RO(2^\omega)\), its complete Boolean algebra is atomless but FAILS countable distributivity. The U and I formulas still give exactly the same shapes \(\Delta_{Z_C}\times A²\) and Δ_X, with zero regular core and Σ=Δ, but Theorem 2.1 does NOT apply. We do NOT know whether W₂(X_C)=U(X_C), nor W(X_C). The contrast now isolates a genuine DISTRIBUTIVITY dependence in our proof rather than a merely formal obstacle.

## 4. Other controls and bounded research target

- **Finite or compact Y:** the earlier compact-fiber theorem works over arbitrary Z, so the present theorem is most interesting for NONCOMPACT countably based Y. For general Y it can be strictly stronger than either compact-fiber or span-density criteria.
- **Nonempty-powerset Scott Y:** This Y is COUNTABLY BASED and has weak \(D₂>D\) but \(W=W₂=U=Y²\). Thus for any nonzero SDω Boolean Z the exact transfer formula PRESERVES the weak D₂>D gap, rather than erroneously collapsing it. The method is compatible with the previous Scott countercontrols.
- **Arrieta A:** We have no assertion D(A)=D₂(A); the product formulas reflect whichever equality is actually true. We use only the verified W(A)=W₂(A)=U(A).
- **Forcing set-theory caveat:** Do NOT replace SDω by arbitrary interpretations of “σ-distributive”; strong common refinement of countably MANY ARBITRARY-cardinality partitions is the exact hypothesis. The counterpoint Cohen RO algebra fails even the 2-partition countable distributivity test. Nontrivial complete atomless Boolean SDω algebras exist in ZFC via σ-closed forcing.

**NEXT CONCRETE TEST:** Determine whether for Cohen Boolean \(Z_C\) and Arrieta's fixed SECOND-COUNTABLE anti-Urysohn A, the second-stage equation
\[
\boxed{\Phi_{2,Z_C\times A}(d_U)=d_U,\quad
d_U=d_{\Delta_{Z_C}}\boxtimes1_{A²}}
\tag{4.1}
\]
holds. This is a sharp discrimination between σ-distributivity (where W=W₂=U is NOW PROVED) and a Cohen base (where neither W=W₂ nor W₂=U has been established). The finite-cover failure could arise from countably many Boolean coefficient partitions lacking a common refinement. It MUST NOT be inferred from the absence of a common refinement alone. If the rank-one equation holds for Cohen but full stabilization fails, this would refute Q; no such failure is asserted. If it fails already at the finite stage, the product is simply another W₂<U control.

**STATUS: NEW INTERNAL proof of a substantive exact product theorem and positive pointfree example; not externally refereed or checked for priority. Universal Q/Q′ remain OPEN.**
