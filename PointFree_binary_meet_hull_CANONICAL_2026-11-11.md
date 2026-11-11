# Canonical addendum — binary relations, higher meet hull and chain 1-type

**11 November 2026. Fourth-audit corrected account.** All original packet C claims C1–C9 survived an independent blind review relative to previously audited premises P1–P6; the new **higher meet-hull groupoid and 2-connectivity theorems** were proposed by the C referee after its verdict and independently cross-checked by the A/B referee. Read alongside [fourth-audit final reconciliation](PointFree_audit4_FINAL_RECONCILIATION_2026-11-11.md) and [earlier canonical chain/hull account](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md). The original notes and reports are retained for provenance; no priority claim. The comparison objects live in the chosen sufficiently large patched Stone-sheaf \(\infty\)-topos \(\mathscr H_\kappa\), not automatically in intrinsic localic shape.

## 0. Conventions and scope

Let X be coherent with Priestley patch space V. Specialization \(x\le y\) means spectral opens are upsets. In arity n+1:
\[
\operatorname{Ch}_n(X)=\{(x_0,\ldots,x_n):x_0\le\cdots\le x_n\},\quad
I_n(X)=\{(x_i):\exists u,\ x_i\le u\ \forall i\},\quad
D_n(X)=\{(x_i):\exists a,\ a\le x_i\ \forall i\}.
\]
These are **patched Stone simplicial spaces** arising from actual proconstructible coherent localic subobjects. Write \(\mathbf C=|h(\mathrm{Ch}_\bullet)|\), \(\mathbf I=|h(I_\bullet)|\), \(\mathbf D=|h(D_\bullet)|\). Define the **higher meet hull**
\[
M_n(X)=I_n(X)\cap D_n(X),\qquad
\mathbf M(X)=|h(M_\bullet(X))|.
\]
The binary term \(M_1\) is the previously named \(\mathcal M=\mathcal I\cap\mathcal D\); unlike \(\mathcal M\), \(M_\bullet\) includes arities \(>2\). A tuple in M_n has a *simultaneous* common upper witness and a *simultaneous* common lower witness; pairwise bounds alone do not suffice.

All internal fundamental groupoids below have **object sheaf h(V)**. They are obtained by forming ordinary edge-path groupoids on simplicial presheaf sections and sheafifying the morphism presheaves. Their classifying objects are the 1-truncations of the realizations, under h(V). Surjective morphisms between Stone witness spaces give site covers; “locally choose a witness” means **after base change along such a surjective cover**, not an assertion of globally continuous choice. No hypercompleteness assumption.

## 1. The binary pair reconstructs all patched higher hulls

**Theorem (fourth-audit C6).** For coherent X the full simplicial patched \(I_\bullet\) is determined by the **binary I graph** together with V; similarly \(D_\bullet\) by the binary D graph. Put \(N_I(x)=\{y:x\mathcal I y\}\) and call a graph vertex z *simplicial* if \(N_I(z)\) is an I-clique. Then
\[
(x_0,\ldots,x_n)\in I_n
\iff
\exists z\,[N_I(z)\text{ is a clique and } x_i\in N_I(z)\ \forall i].
\tag{1.1}
\]
Indeed, maximal points exist above every point by compactness/Zorn on closed up-cones. A vertex has clique-neighborhood iff it lies below a **unique** maximal point m; in that case \(N_I(z)=\downarrow m\). Conversely each maximal m is simplicial and \(\downarrow m=N_I(m)\). Every common upper witness extends to a maximal one. The lower analogue recovers principal upsets of minimal points.

**Scope:** This is a homeomorphic reconstruction of closed subsets of patched powers and their simplicial operators; it is **not** an identification of localic relation embeddings across two differently ordered coherent locales. The finite upper-bound-graph/simplicial-vertex characterization has classical antecedents (McMorris–Zaslavsky and subsequent bound graph literature); the coherent Priestley-extension and its use here should be contextualized rather than claimed as new.

## 2. The higher meet hull presents the chain fundamental groupoid

**Theorem (referee C, independently cross-checked by A/B).**
\[
\boxed{\ \mathsf G_{\mathrm{Ch}}(X)\ \cong\ \mathsf G_M(X)\quad\text{over }h(V).\ }
\tag{2.1}
\]
The map is induced by the inclusion \(\mathrm{Ch}_\bullet\hookrightarrow M_\bullet\) and is **strictly compatible** with the maps to \(\mathsf G_I,\mathsf G_D\).

**Proof (including descent).** On a T-family of M-edges \((x,y)\), base-change along the Stone surjection
\[
W_1=\{(x,y;u,a):a\le x,y\le u\}\longrightarrow M_1.
\]
The pulled-back family has continuous witnesses u,a. Define an arrow in the sheafified chain edge-path groupoid by
\[
\gamma(x,y)=[x,u][y,u]^{-1}=[a,x]^{-1}[a,y].
\tag{2.2}
\]
The equality follows from the two chain triangles \((a,x,u),(a,y,u)\). On the double cover \(T'\times_T T'\), use the first **lower** witness a₁ with the second **upper** witness u₂ to identify both witness-based paths already in the presheaf edge-path groupoid:
\[
[x,u_1][y,u_1]^{-1}=[a_1,x]^{-1}[a_1,y]
=[x,u_2][y,u_2]^{-1}.
\]
Thus (2.2) descends uniquely to a morphism of arrow sheaves. For an M₂-triple \((x,y,z)\) choose a common upper u after a witness cover; then \(\gamma(x,y)\gamma(y,z)=\gamma(x,z)\), and degenerate edges go to identities. Hence \(\gamma:\mathsf G_M\to\mathsf G_{\mathrm{Ch}}\) is a functor identity on objects.

For a chain edge x≤y, choose u=y, a=x and obtain \(\gamma[x,y]=[x,y]\): \(\gamma\circ\iota=\mathrm{id}\). Conversely for an M-edge with a≤x,y≤u, the tuple \((x,y,u)\) is an M₂-simplex (u is its upper witness, a its lower), so in \(\mathsf G_M\), \([x,u][y,u]^{-1}=[x,y]\). This gives \(\iota\circ\gamma=\mathrm{id}\) locally and therefore globally. Compatibility with upper/lower comparison functors follows from strict commutation of simplicial inclusions. QED.

**Corollary (the sharp reconstruction theorem).** Any isomorphism of patched Stone spaces preserving the binary relations \((\mathcal I,\mathcal D)\) induces, by (1.1), an isomorphism of the higher meet simplicial objects and hence of **chain fundamental groupoids** over the common vertex sheaf, simultaneously compatible with both canonical comparison functors. In particular the chain 1-truncation comparison diagram is determined by the binary pair. This supersedes the longer C9 compact paired-extrema proof as preferred exposition (the earlier proof remains an independently reviewed alternative).

**Functoriality warning.** The construction of \(\mathsf G_M\) depends only on \(M_0,M_1,M_2\) and is natural for **patch-continuous maps preserving M₁ and M₂**. It is **not** functorial on arbitrary maps preserving only \(\mathcal I,\mathcal D\) as *binary* relations: those maps need not preserve M₂. A nine-point target with private upper and lower witnesses for each of the three pairs among p,q,r, and a map from a three-element chain to p,q,r, preserves both binary relations but sends its 2-simplex to no M₂-simplex; the triangle path becomes a nontrivial hexagon. Binary **isomorphisms** do recover and preserve all M_n by (1.1). There is no recovered spectral order, full chain nerve or intrinsic localic shape.

## 3. The chain-to-meet map is sharply 2-connective

**Theorem (referee C, independently checked by A/B).** For every coherent locale X,
\[
\boxed{\ \mathbf C(X)\longrightarrow\mathbf M(X)\text{ is 2-connective}.\ }
\tag{3.1}
\]
That is, it induces isomorphisms on \(\pi_0\) and \(\pi_1\) and an epimorphism on \(\pi_2\), locally at each basepoint. It need not be an equivalence of 2-types, or even injective on \(\pi_2\).

**Proof.** For each j≥0 let
\[
E_j=\{(a_0,\ldots,a_j;x)\in V^{j+2}:a_i\le x\ \forall i\},
\]
with equality of the \(a\)-tuple and specialization order on x. Each is a closed Priestley subspace of the product of the equality-ordered Stone space \(V^{j+1}\) and V. Its chain/upper simplicial spaces satisfy
\[
\operatorname{Ch}_n(E_j)=
\{(a_0,\ldots,a_j;x_0\le\cdots\le x_n):a_i\le x_0\},
\]
and
\[
I_n(E_j)=
\{(a_0,\ldots,a_j;x_0,\ldots,x_n):
 (x_0,\ldots,x_n)\in I_n(X),\ a_i\le x_k\ \forall i,k\}.
\]
For fixed n and varying j these are exactly the Čech nerves of **surjective Stone lower-witness projections** over \(\operatorname{Ch}_n(X)\) and \(M_n(X)\). Therefore
\[
\mathbf C(X)\simeq|j\mapsto\mathbf C(E_j)|,\qquad
\mathbf M(X)\simeq|j\mapsto\mathbf I(E_j)|,
\tag{3.2}
\]
and the realized map is the canonical map (3.1). At j=0, inserting the lower witness a defines an extra degeneracy on **both** chain and upper-hull nerves, over the common augmentation h(V), so \(\mathbf C(E_0)\to\mathbf I(E_0)\) is an equivalence. At every j, the upper-witness triangle calculation (a special case of the rectangle quotient C1) proves \(\mathbf C(E_j)\to\mathbf I(E_j)\) is 1-connective.

Use the **realization connectivity lemma in an \(\infty\)-topos**: if a map of simplicial objects \(f_j:A_j\to B_j\) is \((n-j)\)-connective for \(0\le j\le n\), then its realization is n-connective. One proof passes to the semisimplicial skeletal filtration and identifies the kth relative attachment with the pushout-product \(f_k\square(\partial\Delta^k\to1)\), an iterated codiagonal. Codiagonals increase connectivity by one in the (connective,truncated) factorization system, and the class of n-connective maps is closed under cobase change, composition and colimits. This argument is valid in any \(\infty\)-topos; it does not require hypercompleteness. For background in spaces see Ebert–Randal-Williams, *Semisimplicial spaces*, Lemma 2.4 (2019); for semisimplicial cofinality see [Kerodon §10.1.2](https://kerodon.net/tag/04R8).

Apply the lemma with n=2: f₀ is an equivalence, f₁ is 1-connective, and f₂ is at least 0-connective. This proves (3.1). QED.

**Sharpness.** For the six-point ordinal sum \(P=A_2\oplus A_2\oplus A_2\) of three two-antichains, \(\mathbf C(P)\simeq S^2\) while \(\mathbf M(P)\simeq1\). Thus the map is 2-connective but not 3-connective. The associated 2-type also includes π₁-action and k-invariant; no complete classification of missing 2-type data is claimed.

## 4. Other externally checked C results (record and repair guide)

The detailed proofs remain in the independently reviewed [binary rectangle and relative skeletal note](PointFree_binary_rectangle_pi1_relative_skeleton_2026-11-10.md), [triangle hierarchy/rank note](PointFree_binary_triangle_hierarchy_formal_hull_rank_2026-11-10.md), [fixed-pattern arbitrary obstruction note](PointFree_binary_fixed_hierarchy_arbitrary_comparison_obstruction_2026-11-10.md), and [fixed-hulls/unbounded-obstruction note](PointFree_binary_reconstruction_fixed_hulls_unbounded_obstructions_2026-11-10.md). Those working originals must be read with the following fourth-audit corrections:

- **C1:** both C→I and C→D induce the same identity-on-objects *sheafified normal subgroupoid quotient* killing four-edge upper/lower witness rectangle loops. Define the presheaf normal closure explicitly before sheafification. Least upper witness may be weakened to a common interpolant. The functors are 1-connective, and the stronger statement (3.1) concerns C→M, *not* C→I/D.
- **C2a,b:** the relative first skeletal module is a **cokernel** of a monomorphism \(R[\operatorname{Ch}_1]\to R[B_1]\); the degree-two witness triangles kill its first homology. For the S-indexed triangle, \(L_I=M_R^{12}\), \(L_D=M_R^{10}\oplus N_R^2\oplus Q_R^2\), with \(M_R=R[h(S)]\), \(N_R=R[h(S^2)]\), \(Q_R=\mathrm{coker}(M_R\to N_R)\) along the Stone diagonal. Note \(R\ne0\) for nonconstancy.
- **C3:** the explicitly displayed named hierarchy, not every possible relation word, has the established strict Hasse pattern; \(\mathcal U\) and \(\mathcal V\) are incomparable though equal-cardinality in finite approximants. Each nonshared label block is ∅, Δ_S or S². Closedness uses the monotone map folding one fibre onto another: cross-fibre membership entails same-fibre membership, excluding S²\Δ_S.
- **C4:** on \(W_S(P,v)\) with P finite connected and v minimal, the first fixed closed formal-hull stage is the eccentricity of v in the I-graph for |S|≥2. This rank varies arbitrarily while the canonical diagram stays fixed for the whiskered triangle examples.
- **C5:** reverse-face-poset spanning-tree gadgets realize arbitrary connected finite |K| in the chains but contract both hulls. When attached to the triangle **before** Stone-indexed gluing, they retain the *displayed* hierarchy and rank two, while canonical comparisons collapse \(h(S)_+\wedge|K|\). Acyclic K may yield nonequivalences with contractible homotopy cofibres. Do not claim all identities beyond the displayed diagram are fixed; in particular \(\mathcal M=\text{symmetric comparability}\) can fail for attached K.
- **C7:** finite poset flattening and duplicated-extrema arguments remain valid as a secondary proof of finite chain π₁ determination; (2.1) now supplies a simpler universal proof and makes the extra combinatorial construction optional.
- **C8a,b:** three-layer six-point middle antichain/chain examples have identical patched higher hulls but chain types S² and 1. The Cantor middle-layer construction retains the **same patched higher simplicial hulls**, exact rank two and fixed nonconstant hull targets while varying the first homological comparison obstruction through unbounded degrees. Equality here is **of patched simplicial closed subsets across different orders**, not identity of localic relation embeddings.
- **C9:** the paired-extrema proof is sound and historically useful but is no longer the preferred route. It used **only** the cross-coordinate inequalities on the auxiliary pairs; limit pairs need not be extremal or share equal cones. The direct meet-hull proof is cleaner and yields the strengthened exact functoriality boundary.
- **Literature:** acknowledge the classical finite upper-/lower-bound graph/simplicial-vertex characterization; the object-level Dowker equivalence \(I\simeq D\) is classical, while compatibility under the original chain object is the stronger previously audited edgewise arrow statement. No comprehensive priority search has been performed.

## 5. Status and further boundary

(1) The principal results C1–C9 were blind externally checked **relative to P1–P6** with the repairs recorded above. (2) The new groupoid theorem (2.1) and 2-connectivity theorem (3.1) received an independent cross-review; they were **not** part of the original blind C verdict. (3) The category of all binary-graph-preserving maps does **not** support the reconstructed groupoid functor, as shown by the nine-point counterexample. (4) Nothing asserts intrinsic localic shape, arbitrary-locale generality, all-site-size independence, or determination of chain homotopy beyond degree one. (5) The earlier full technical notes and fourth-audit reports remain essential provenance; this is a corrected theorem addendum, not their silent replacement.
