> **PRIMARY SOURCE RETRIEVED (21 NOV):** The user supplied Johnstone–Sun's *Weak Products and Hausdorff Locales* (1988), full 21-page article; it has now been read. Its Cor. 1.12 identifies the weak product of spatial locales with the spatial topological product; **our \(p(A,B)\) is precisely this weak product, embedded in \(q(A,B)\), the full localic product**. Cor. 1.5 makes \(p\) dense in \(q\); Prop. 1.19 says \(\Omega(K)\) distributed iff Hausdorff K scattered, directly explaining another part of the scattered-coordinate boundary. Lemma 1.16 treats locally closed pullbacks. See [source-by-source reconciliation](ProjectA_ENDGAME_JOHNSTONE_SUN_WEAK_PRODUCTS_PRIMARY_SOURCE_2026-11-21.md). Earlier text below requesting this paper is **historical and superseded**; the 1988 work **does not itself prove** our mixed rectangular RC or the localic matrix formula MUL.

# Project A — endgame exact comparison: coherent patch calculus versus p/q rectangles
## 21 November 2026 · theorem-level literature reconciliation, Segment 3

**Scope:** Compare established published relation categories *at the level of objects, morphisms, identity, composition and admissible subobjects* with the corrected project [coherent proconstructible composition theorem](ProjectA_coherent_composition_canonical_proof_2026-11-08.md) and [compact-Hausdorff p/q theorem](ProjectA_CLIQUE_RECTANGULAR_CALCULUS_POSTREFEREE_CANONICAL_2026-11-20.md). This is not an originality assertion. All statements about actual Loc composition of our restricted classes use the **previously independently audited project results** as explicit premises.

## A. Coherent calculus: an exact patch/closed-relation equivalence

Let \(\mathsf{CohProRel}\) have coherent locales X as objects and the **proconstructible spectral** sublocales \(R\hookrightarrow X\times_{\mathrm{Loc}}Y\) as morphisms, with the genuine localic pullback/image composite. By the project's canonical Theorems A and B:
1. Each such R corresponds uniquely to a closed subset \(R_p\subseteq X_p\times Y_p\), where \(X_p\) is the compact Hausdorff zero-dimensional **patch** space of classical spectral points. The class contains **all** patch-closed relations, not just order-saturated ones. In particular \(\Delta_X\) is admitted.
2. Localic products of coherent locales are coherent; their point sets and patch structures correspond to the product of point sets/patch spaces. For R,S in the class the **actual** Loc image of the **actual** composability sublocale has point relation
\[
(R\circ_{\mathrm{Loc}}S)_p=R_p\circ_{\mathrm{set}}S_p.
\]
The latter is closed by compact Hausdorff projection of the closed composability set. Equality of points identifies the **proconstructible** sublocale, not an arbitrary sublocale.
3. Hence \(X\mapsto X_p,\ R\mapsto R_p\) defines a full and faithful functor into the ordinary category \(\mathsf{StoneClosedRel}\) of Stone spaces and **all closed set relations**. It is essentially surjective because a Stone space is itself a coherent spatial locale with its original topology equal to its patch topology.
4. Thus, classically,
\[
\boxed{\mathsf{CohProRel}\simeq \mathsf{StoneClosedRel},}
\]
also preserving converse, identity and finite joins in hom posets. This is a **project corollary**, newly emphasized at the endgame, *not separately blind-reviewed*. Associativity on the right is classical; the substantive Loc assertion is item 2, already audited.

**Priority implication:** One should no longer present abstract associativity of these relation categories as a stand-alone discovery. The part requiring an actual proof is that the full Loc image/pullback law **realizes** this classical Stone closed-relation algebra within the coherent locale world. The separate specialization/diagonal hull identities, including \(\mathcal I=\mathcal A\mathcal A^\smile,\ \mathcal D=\mathcal A^\smile\mathcal A\) and \(\mathcal S^2=\mathcal J,\ \mathcal S^4=\mathcal U\vee\mathcal V\), are the Project A-specific applications. Precise antecedents to these hull identities still need comparison.

**Sources:** Christopher Townsend, *Preframe Techniques in Constructive Locale Theory*, PhD 1996, Chapter 4, Theorems 4.2.1, 4.3.3, https://sjvickers.github.io/townsend.pdf ; Kurz–Moshier–Jung below; Borlido et al., *Filtral Pretoposes and Compact Hausdorff Locales* (2024).

### Categorical-image caveat: not a tautology from regularity of Spec

The category \(\mathbf{Spec}\) of spectral spaces with spectral maps does **not** automatically calculate categorical images as Loc does. Dickmann–Schwartz–Tressl, *Spectral Spaces* (2019), Ch. 5 §5.2, explicitly says monomorphisms are **injective** spectral maps, epimorphisms **surjective** ones. The continuous bijection
\[
f:\{0,1\}_{disc}\to\{0,1\}_{Sierpinski}
\]
on the underlying finite set is a **spectral** map, monic and epic in Spec, non-isomorphism. It is its own categorical mono/image whenever a mono image factorization is used, whereas in Loc its image is the **whole Sierpiński locale**, since the map of frames is injective. We do not assert that Spec is or isn't regular on the basis of this example; it suffices to show a *naively imported categorical image* may disagree with the localic one. The project's spectral-image lemma addresses this actual-operator issue.

## B. Hofmann–Nora spectral distributors are a different class

Hofmann–Nora, *Dualities for Modal Algebras from the Point of View of Triples*, https://sweet.ua.pt/dirk/artigos/2015/dualmodalg_revised.pdf , p.14 printed (=PDF p.13), explicitly defines \(\mathsf{SpecRel}\) as spectral relations \(R:X\to Y\) with a spectral map \(X\to VY\) to the lower Vietoris space, and proves the order-compatibility implication
\[
x\le x',\; x'Ry',\; y'\le y\implies xRy.
\]
The Kleisli identity on a spectral space is its **specialization order**, rather than the literal diagonal (except for discrete-order objects).

Our \(\mathsf{CohProRel}\) has **actual diagonal** as identity. On a two-element Sierpiński/chain, \(\Delta\) is a proconstructible sublocale but *does not* satisfy the displayed order-compatibility (take \(0<1\), \((1,1)\in\Delta\); then \((0,1)\) would be forced). Thus the categories are not simply two presentations of the same class. Even on Stone spaces with equality order, \(\mathsf{SpecRel}\) requires lower Vietoris continuity of the set-valued relation; arbitrary **closed** relations need not satisfy it (e.g. a singleton graph \(R=\{(x_0,*)\}\subseteq X\times1\) with \(x_0\) nonisolated has hit-locus \(\{x_0\}\), which is not open). Therefore avoid identifying their named \(\mathsf{StoneRel}\) with our \(\mathsf{StoneClosedRel}\) merely by notation.

Related source: Kurz–Moshier–Jung, *Stone Duality for Relations* (arXiv:1912.08418v2, published as chapter in *Samson Abramsky on Logic and Structure in Computer Science and Beyond* (2023), pp.159–215, DOI 10.1007/978-3-031-24117-8_5), https://arxiv.org/pdf/1912.08418 . In §5.2 Theorem 5.9 they extend Priestley duality to **weakening/order-compatible** relations via relational cospans/spans and exact squares. This is a powerful established precedent, but their category \(\mathsf{Pri}^{co}\) is not our unrestricted patch-closed relation category unless the order is discrete. Their §1 explicitly distinguishes relations as morphisms from multiary subsets, and the weakening condition is essential.

**Newly retrieved and directly inspected primary text:** Kurz–Moshier–Jung, *From Zero-Dimensional to Continuous Dualities: A Double-Categorical Account*, arXiv:2610.07695v1 (6 October 2026), full PDF https://borowiecki.dev/pdf/2610.07695 (original arXiv version shown on PDF, dated 7 October). It studies duality extended to a **double category** incorporating both maps and relations; **Theorem 4.6** gives Pri-relations/DL-relations duality, **Theorem 4.16** upgrades to double categories, and §6 studies idempotent splitting. It recovers the Stone-space category with **arbitrary closed relations as relational arrows** as the discrete-order case of the Priestley relational calculus. This is the especially close established *relational duality on the right-hand side* of our patched category equivalence.

**Variance/category warning:** **Corollary 5.3** says SubBA is dually equivalent to *Stone spaces equipped with a closed endorelation*, with corresponding relation-preserving **functional** morphisms: it is a result about **relational structures as objects**. It should **not** be quoted as a direct duality between SubBA and our category whose **morphisms themselves are arbitrary closed relations**. The latter relational-morphism-level comparison belongs to the relational/double-category theorem (Thm 4.16), restricted to Stone/Boolean algebras. Keeping these two readings separate is especially important for our final write-up. The 2026 preprint has now been read; **user retrieval is no longer needed**.

## C. p/q rectangles cannot be recovered from the closed hull

Let G compact Hausdorff, \(p(A,B)=[A\times B]_{G^2}\) and \(q(A,B)=[A]_G\times_{\mathrm{Loc}}[B]_G\), where p is point-generated spatial and q is the potentially nonspatial **full** product. Since \(p\le q\le\overline A\times\overline B\) and A×B is dense in the latter closed subset,
\[
\boxed{\operatorname{cl}p(A,B)=\operatorname{cl}q(A,B)=\overline A\times\overline B.}
\]
Thus the classical *closed-relation shadow* forgets p versus q. This includes cases where \(p\ne q\); the distinction is the canonical map from the **ordinary spatial product** of induced subspaces to their full **localic product**, governed by the classical theory of spatiality of localic products (Johnstone, Plewe).

**Closure fails to preserve even simple rectangular composition.** Take G=[0,1], \(R=G\times\{0\}\), \(S=(0,1]\times G\). As open/closed sublocale rectangles, their middle overlap is zero, hence \(R\circ S=0\); but \(\operatorname{cl}R=R\), \(\operatorname{cl}S=G^2\), so \((\operatorname{cl}R)\circ(\operatorname{cl}S)=G^2\ne0=\operatorname{cl}(R\circ S)\). This straightforward example proves closure is **not** a multiplicative map from the project's nonclosed rectangle semigroup to classical compact-Hausdorff closed relation composition. No nonspatiality is needed for this obstruction.

**Townsend comparison:** Townsend's 1996 PhD Chapter 4 Theorems 4.2.1 and 4.3.3 provide an explicit preframe formula for composition of **closed** localic relations and identify these morphisms with preframe maps. This is the known CHaus associative base. It does not encode p versus q via the *closed hull alone*, and cannot be applied mechanically to their nonclosed composites. It remains possible some richer **nucleus/preframe operator** encoding captures both—**not demonstrated**.

**de Vries/subordination comparison:** Bezhanishvili et al., *A Generalization of de Vries Duality to Closed Relations between Compact Hausdorff Spaces* (arXiv:2206.05711, published 2023), explicitly uses a category of **closed** relations and an allegory; see Definition 3.5 and Lemma 3.6. Their framework also cannot distinguish p and q by the common closed-relational shadow. Kurz–Moshier–Jung's 2021/2023 relational duality and Abbadini–Bezhanishvili–Carai's 2024 *Vietoris Endofunctor for Closed Relations and Its de Vries Dual* are crucial references but also use closed relations.

### Closest missing source: Johnstone–Sun weak product

P. T. Johnstone and Shuhao Sun, *Weak Products and Hausdorff Locales*, in Borceux (ed.), *Categorical Algebra and its Applications*, Lecture Notes in Mathematics **1348** (Springer, 1988), **173–193**. Bibliographic record/abstract https://research.monash.edu/en/publications/weak-products-and-hausdorff-locales/ . Their **weak symmetric monoidal product** recovers the *spatial product* of spatial locales and sits as a **dense sublocale** of the full localic product. This is plainly a close conceptual predecessor of the tension \(p(A,B)\le q(A,B)\), but one must not equate its weak product with **our induced point-generated sublocale inside a fixed compact Hausdorff ambient square** without inspecting the construction and embeddings. **Full original text not available in this segment**. Request user-provided PDF/scans if possible, rather than speculate.

Till Plewe, *Localic Products of Spaces* (1996), DOI 10.1112/plms/s3-73.3.642, is the principal direct background on spatial versus nonspatial products. It has been inspected from a primary copy earlier in this project; source comparisons are in the literature ledger. The abstract source of Johnstone–Sun is *not* a theorem-level substitute for reading their paper.

## D. Project composition consequences and revised editorial judgment

1. **Coherent theorem B** is an exact **realization** within Loc of a familiar Stone closed-relation category; its independent importance centers on proving that its actual Loc composition matches pointwise/patch composition, and on its diagonal-hull applications. No abstract-category novelty claim.
2. **RC and balanced witness** live genuinely beyond existing closed-only relations. An exact predecessor for the RC saturation theorem remains unlocated; absence is not a priority conclusion.
3. **MAT/MUL** carry arbitrary (possibly nonspatial) P-relations as matrix entries and describe **binary genuine Loc composition**, not just classical relational matrices. The known scatteredness theorem is an antecedent; the parameterized and genuine-image statements remain candidates for new synthesis, subject to continued literature checking.
4. **A refined publication concept** is not “localic relations are nonassociative,” nor “closed relations associate,” but “controlled, generally nonclosed localic relations form associative fragments; sometimes the entire binary calculus becomes a matrix operation without acquiring global associativity.”
5. For the final manuscript/literature reference, retain complete statements of \(\mathsf{SpecRel}\) vs \(\mathsf{CohProRel}\), the closure counterexample, and the new patch-category equivalence; do not claim a full category comparison that silently changes the notion of relation or identity.

## E. External access/provenance

**Directly inspected for this segment:**
- Townsend 1996 full thesis PDF, Chapter 4, especially Theorems 4.2.1, 4.3.3.
- Hofmann–Nora lower Vietoris spectral-relation definitions, printed p.14.
- Kurz–Moshier–Jung *Stone Duality for Relations*, arXiv:1912.08418v2, §1, §5.2, Theorem 5.9, and related text.
- Abbadini/Bezhanishvili/Carai adjacent abstracts and de Vries closed-relation arXiv:2206.05711 §3.
- Dickmann–Schwartz–Tressl, *Spectral Spaces*, Chapter 5 abstract explaining mono/epi classification.
- Johnstone–Sun 1988 bibliographic record and abstract, **not full text**.
- Kurz–Moshier–Jung 2026, arXiv:2610.07695v1, **full original 30-page PDF via public mirror**, especially §§4–6, Theorems 4.6/4.16, Corollary 5.3. Read directly after initially being unable to access it through arXiv.

**Requested user retrieval (if convenient):** Johnstone–Sun 1988, *Weak Products and Hausdorff Locales*, LNM 1348, pp.173–193 — highest priority for p/q conceptual overlap. Its original full text remains inaccessible here, although bibliographic record and abstract are available. **All other major source texts mentioned here are available**, including the newer Kurz–Moshier–Jung 2026 paper via a public full-text mirror.

**No priority or novelty conclusion is asserted.**
