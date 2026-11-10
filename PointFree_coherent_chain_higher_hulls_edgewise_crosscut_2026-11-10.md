# Point-Free Topology — Coherent chain nerves, higher diagonal hulls, and an edgewise Dowker bridge

**10 November 2026. Working mathematics, internally checked but NOT externally audited.** This continues [finite-poset crosscut and chain-to-witness comparison](PointFree_finite_poset_crosscut_chain_witness_comparison_2026-11-10.md), using the audited coherent proconstructible calculus [canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md) and the [Dowker referee reconciliation](PointFree_Dowker_EXTERNAL_referee_reconciliation_2026-11-10.md). No priority claim. The twofold edgewise-subdivision mechanism is classical (Bökstedt–Hsiang–Madsen; see also Brown–Chan–Galatius–Payne, Cor. 3.9), but the specialization rectangle map below is our present deduction.

## 0. Conventions and the ambient homotopy theory

For coherent X put K=K(X), its bounded distributive lattice of compact opens, and let P=pt(X) with the patch Stone topology and specialization order x≤y iff every spectral open containing x contains y. A⊆X² is the genuine proconstructible specialization sublocale. Let
  C_n=Ch_n(X)={x_0≤...≤x_n}⊆X^(n+1),
  I_n=I^(n+1)(X)=cl Δ_(n+1),
  D_n=D^(n+1)(X)=fit Δ_(n+1).
All three are actual simplicial proconstructible spectral sublocales, and C_•↪I_•, C_•↪D_• are natural simplicial inclusions. For arbitrary locales the same inclusions remain true; coherence is used for proconstructibility and the patch interpretation.

Write \(\mathscr H_{\mathrm{St}}=\mathrm{Shv}_\infty(\mathrm{Stone}_\kappa,J_{\mathrm{fin\,joint\,surj}})\), where a suitable size universe is fixed and finite jointly surjective families are covers. Let h be sheafified Yoneda, and put
  bold C=|h(Patch C_•)|,  bold I=|h(Patch I_•)|,  bold D=|h(Patch D_•)|.
The independently audited patched Čech theorem gives equivalences
  bold I ←~ |h(Patch diag E_••(A))| ~→ bold D.
Do not assert an equivalence of original unpatched simplicial locales or of intrinsic shape(X).

## 1. Exact coherent compact-open presentations

Let T_n(K)=K ⊔ ... ⊔ K (n+1 copies, bounded distributive lattice coproduct). For k∈K denote its copy in coordinate j by k^(j). Then compact-open lattices of the three proconstructible sublocales are the following quotient lattices:
- Ch_n: impose k^(j)≤k^(j+1), for every k∈K, 0≤j<n.
- I_n: impose k_0^(0)∧...∧k_n^(n)=0 whenever k_0∧...∧k_n=0 in K.
- D_n: impose ∨_{u∈U}(u^(0)∧...∧u^(n))=1 for every finite cover U⊆K, ∨U=1.

Proof: Ch is presented by adjacent internal specialization inequalities. The I presentation is the largest closed sublocale of X^(n+1) where all rectangles with zero diagonal intersection vanish (the closed complement of their join). The D presentation is the meet of the open sublocales defined by the displayed finite compact-open cover equations, from the externally audited higher-diagonal cover reconstruction. As compact-open generators and relations, all define actual coherent spectral quotient sublocales; they are not assertions made solely from points.

**Finite approximation proposition.** Write K=filtered colim K_λ over its finite bounded distributive sublattices. Put P_λ=Spec(K_λ), a finite T0 locale. Since bounded distributive lattice coproducts preserve filtered colimits and every defining equation is finite and reflected by the inclusions K_λ↪K, for each n
  Ch_n(X) ≅ lim_λ Ch_n(P_λ),
  I_n(X) ≅ lim_λ I_n(P_λ),
  D_n(X) ≅ lim_λ D_n(P_λ)
as coherent locales, compatibly with all simplicial maps. The prime-filter extension theorem makes the spectral bonding maps P_μ→P_λ surjective. This is NOT a statement that geometric realization commutes with the inverse limits. It supplies, instead, canonical pro-simplicial sets/spaces of finite-stage chain and higher hull nerves. If the crosscut hypothesis holds at every stage of some cofinal diagram, both canonical maps are levelwise weak equivalences and thus give equivalences of those pro-spaces; no identification with intrinsic shape(X) is claimed.

## 2. Edgewise rectangle comparison: BOTH canonical maps have the same status

For any locale X, the twofold edgewise subdivision esd₂ Ch has nth term Ch_(2n+1), using the ordinal-sum functor ε([n])=[n]*[n]=[2n+1], ε(f)=f*f. There is a natural simplicial locale map
  F:esd₂ Ch_•(X) → diag E_••(A)
sending x_0≤...≤x_(2n+1) to
  (x_0,...,x_n; x_(n+1),...,x_(2n+1)).
All early coordinates lie below every later coordinate, so the map factors through the rectangle locale as a **genuine localic map**. Naturality in all face/degeneracy operators follows from ε(f)=f*f.

Let a,b:esd₂ Ch→Ch extract the first and second blocks, respectively. The composites with the two projections from diag E are exactly
  pr_I F=i_I∘a;    pr_D F=i_D∘b.
The standard edgewise-subdivision lemma says the geometric realizations of a,b are equivalences and both agree with the canonical subdivision equivalence after realization. More explicitly, ε^op is homotopy-final for geometric realizations and the maps induced by the two inclusions id⇒ε are the canonical colimit comparisons. (For simplicial sets this is the usual edgewise subdivision theorem; it extends to simplicial objects of an ∞-category with colimits.)

In the coherent patched Stone sheaf ∞-topos, the diagonal-vs-iterated-realization comparison and both patched Čech equivalences show that the two projection maps
  |h(Patch diag E)|→bold I,   |h(Patch diag E)|→bold D
are equivalences. The resulting triangle with apex bold C commutes up to a canonical homotopy.

**Theorem (working).** For any coherent X, in the patched sheaf ∞-topos, the canonical map bold C→bold I is an equivalence **if and only if** the canonical map bold C→bold D is an equivalence. The two maps correspond under the specific patched Dowker zigzag. This is stronger than mere abstract equivalence of bold I and bold D, and is a new bridge from the actual internal chain nerve to the localic Dowker rectangle.

This proof does **not** use or imply descent of the original unpatched lower-witness maps, which may fail even ordinary descent by the referee-origin counterexample.

## 3. A localic crosscut/good-cover sufficient criterion

Assume P=pt(X) has only finitely many maximal specialization points M (nonempty). For each nonempty finite S⊆M put
  B_S=⋂_{m∈S}↓m
regarded as a proconstructible spectral sublocale of X (patch closed, since order relation is patch closed). A compact ordered Stone space has a maximal point above every point: for ↑x, chains have upper bounds by compactness and closedness of the order, then Zorn. Hence P=⋃_{m∈M}↓m.

**Localic good-intersection criterion:** For every S with B_S nonempty, the object
  |h(Patch Ch_•(B_S))|
is terminal in \(\mathscr H_{\mathrm{St}}\) (internally contractible). It is enough that B_S possess a greatest specialization point g_S: the internal order category has terminal object g_S and its nerve has a contracting natural transformation. It is also enough that it possess a least point. For finite B_S the condition reduces to the familiar contractibility of its ordinary order complex, but for infinite B_S this is an actual sheaf-homotopical condition, not a statement about an ordinary point-set order complex.

**Theorem (working, coherent patched crosscut).** Under the above finite-maximal and good-intersection conditions, BOTH canonical maps
  bold C→bold I and bold C→bold D
are equivalences in \(\mathscr H_{\mathrm{St}}\).

**Proof of closed side.** For every simplicial degree n,
- Ch_n(P) is covered by the finite family of patched closed subspaces Ch_n(↓m), m∈M (a chain has a maximal upper bound).
- I_n(P) is covered by the finite family (↓m)^(n+1), m∈M (a common upper witness has a maximal extension).
Both covers are jointly surjective families of Stone maps, hence effective epimorphic after sheafification, *even though the original downsets need not be open sublocales*.

The r-fold Čech intersection of the first cover is a finite coproduct over (m_0,...,m_r)∈M^(r+1) of Ch_n(B_S), S={m_0,...,m_r}. The corresponding intersection of the second cover is the coproduct of (B_S)^(n+1). These are compatible with the inclusion of simplicial objects in n.

Realize first in n. By the assumption, |h(Patch Ch_•(B_S))| is terminal for nonempty B_S and initial for empty B_S. Meanwhile, for every nonempty Stone B_S the simplicial Stone object B_S^(•+1) is the Čech nerve of the cover B_S→1, so |h(B_S^(•+1))| is likewise terminal (and initial when empty). Each intersection-level map is therefore an equivalence. Taking finite coproducts and realizing the Čech nerves over r, which reconstruct bold C and bold I, proves that bold C→bold I is an equivalence. The edgewise bridge of §2 then implies bold C→bold D is an equivalence. QED.

**Order-dual alternative:** if P has finitely many minimal points and the chain nerve on each nonempty intersection of their principal upsets is internally contractible, the same Čech argument proves the D-side equivalence first (for a tuple with a common lower bound, extend it down to a minimal point); then the edgewise bridge supplies the I-side. This is not needed under the maximal criterion.

The conclusion is about patched representable-sheaf realizations. No assertion is made that ordinary spectral weak homotopy types or intrinsic locale shapes coincide.

## 4. Explicit genuinely infinite coherent circle example

Start with the 6-point face poset of a triangle boundary: minimal vertices v_1,v_2,v_3, maximal edges e_12,e_23,e_31; each v_i≤its two incident edges. Add countably many points a_1,a_2,... and a_∞ between v_1 and e_12:
  v_1<a_n<e_12 (all n),    v_1<a_∞<e_12,
with no additional comparisons except transitivity; the a_n are mutually incomparable and incomparable with a_∞.

Equip the set with Stone topology in which a_n→a_∞, while the original six points are isolated. This is a compact ordered zero-dimensional space. The order is closed: the only nonconstant limiting comparisons v_1<a_n and a_n<e_12 have their a_∞ limits included. It is Priestley: ↑v_1 (including every a_n,a_∞ and e_12,e_31) is clopen; ↑v_2,↑v_3 and the original isolated maximal points are clopen; ↑a_n={a_n,e_12} is clopen; and for each N the set {a_∞,a_n:n≥N,e_12} is a clopen upset separating a_∞ from any specified a_n. These separate all pairs x≰y.

The corresponding spectral topology of patch-open upsets defines an **infinite coherent locale** X. Its maximal points are exactly the three e_ij. Their principal downset intersections:
  ↓e_12 ∩ ↓e_23 = {v_2},
  ↓e_23 ∩ ↓e_31 = {v_3},
  ↓e_31 ∩ ↓e_12 = {v_1},
  ↓e_12 ∩ ↓e_23 ∩ ↓e_31 = ∅.
Every singleton maximal downset ↓e_ij has greatest element e_ij. Thus the good-intersection criterion applies.

The Čech intersection pattern is exactly the triangle boundary. Consequently, inside the patched Stone sheaf ∞-topos,
  |h(Patch Ch_•(X))| ≃ |h(Patch I_•(X))| ≃ |h(Patch D_•(X))| ≃ underline(S¹),
where underline(S¹) is the constant object on the ordinary homotopy type S¹. **The canonical maps** are equivalences, and the computation is not just a finite-poset restatement: the simplicial coherent locales contain infinitely many spectral points and a nonisolated patch point.

This does not determine the weak homotopy type of the original non-Hausdorff spectral topological space nor intrinsic shape of X.

## 5. Why finite maximal covers do not exist generally

The maximal-point subset of a coherent Priestley space need not be patch closed. Example: patch Stone space {a_1,a_2,...,a_∞,t} with a_n→a_∞, t isolated, and only nonreflexive relation a_∞<t. It is Priestley: {a_n} are clopen upsets; {t} is a clopen upset; and for a_∞≰a_n one may take {a_∞,t} plus a suitable cofinite tail of the a_k. Its maximal points are {a_n:n≥1}∪{t}, whose patch closure contains the nonmaximal a_∞. Therefore there is no general compact Stone sublocale of maximal points to support a literal extension of the finite-poset maximal crosscut argument.

## 6. Status, obstacles and next tasks

- The finite compact-open quotient presentations and cofiltered finite approximation are exact, algebraic and independent of any homotopy site.
- The edgewise rectangle construction and its induced correspondence of canonical chain-to-I and chain-to-D maps are a promising, nontrivial new working deduction. Verify formally (or seek a targeted external check) the edgewise realization comparison in the Stone sheaf ∞-topos, and the compatibility of the diagonal/iterated realization equivalence with the two projections. No priority claim.
- The finite-maximal localic crosscut criterion and the explicit infinite circle example depend on the edgewise bridge for the D-side, and on standard Čech descent for finite families of closed Stone embeddings for the I-side.
- Do not promote the stagewise pro-homotopy comparison to an intrinsic localic shape equivalence without further argument, and do not conflate the patched result with the unpatched descent problem.
- The general maximal-point subset need not be compact/patch-closed; the finite-max hypothesis is substantive. Explore intrinsic finite **principal-downset** presentations or relative versions over Stone bases, rather than proliferating rank constructions.

**References:** Priestley duality and Hochster finite spectral approximation; the coherent Project A composition theorem (8 Nov 2026); the independent Dowker reconciliation (10 Nov 2026); classical edgewise subdivision of simplicial sets (Bökstedt–Hsiang–Madsen) and Brown–Chan–Galatius–Payne on the two projection maps and realization; crosscut theorem / Quillen A; the original Cameron–Kumar *Graphs on Topological Spaces* (arXiv:2610.14783); no publication priority established.