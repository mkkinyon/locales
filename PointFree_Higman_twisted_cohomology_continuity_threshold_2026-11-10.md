# Point-Free Topology — Twisted-coefficient threshold for Stone-indexed Higman homotopy

**10 November 2026 · NEW internally checked research segment; NOT externally blind-audited.** This continues the [acyclic/aspherical nonconstant common-hull construction](PointFree_relative_chain_splitting_acyclic_aspherical_nonconstant_2026-11-10.md), whose canonical-equivalence input was independently audited in [the sheaf/Čech canonical account](PointFree_nonconstant_sheaf_Cech_CANONICAL_2026-11-10.md). We choose **twisted coefficients** as the current branch and explicitly preserve the alternative branch into the **original binary separation-relation hierarchy** in [the parked roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md). No priority/novelty claim: the Higman representation obstruction, duality, and Berstein–Schwarz class are classical/published.

## 0. Precise framework

Let H be Higman's infinite, acyclic, finitely presented, torsion-free group with no nontrivial finite quotients and a **finite aspherical 2-dimensional** standard presentation complex BH. Higman's group is a **duality group of dimension two** (Robert Bieri, *Homological Dimension of Discrete Groups*, 2nd ed., Chapter III §9.8, Example 5; https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bieri.pdf, printed p.167). Fix nonempty Stone S and the coherent **pointed-face-poset** locale \(X_H(S)\) from the previous audited construction, with both *canonical* comparisons \(\mathbf C\to\mathbf I,\mathbf C\to\mathbf D\) equivalences, and common object
\[
E_S\simeq h(S)_+\wedge\underline{BH}\simeq B\Pi_S .
\]
Here \(\Pi_S=\operatorname{Fr}_H(h(S))\) is the **internal free product of copies of the constant discrete group H indexed by the condensed set h(S)**; concretely it is the sheafification of the presheaf
\[
T\longmapsto *_{f\in\operatorname{Cont}(T,S)} H.
\]
At the terminal Stone point,
\[
\Pi_S(*)\cong *_{s\in S_{\mathrm{set}}}H,
\]
since this evaluation preserves relevant colimits. Choose a global point \(s_0\in S\). The **folding morphism** \(\rho:\Pi_S\to\underline H\) sends every indexed H-factor identically to H; the s0-factor inclusion \(i_{s_0}:\underline H\to\Pi_S\) is a section of ρ.

These are statements in the sufficiently large Stone finite-surjection sheaf ∞-topos after Patch, not intrinsic localic shape.

## 1. The finite-dimensional obstruction is stronger than ordinary acyclicity

**Published fact:** Higman H has no finite quotient. By Mal'cev's theorem, every finitely generated subgroup of GL_n(k), for any field k, is residually finite. Therefore **every** representation \(H\to GL_n(k)\) is trivial: its finitely generated image is a quotient of H and residually finite, hence has a nontrivial finite quotient unless trivial. This observation and the resulting vanishing of \(H^{>0}(H;M)\) for finite-dimensional and finitely generated-abelian coefficient modules are already made in Grant–Lupton–Oprea/Farber et al., *New lower bounds for the topological complexity of aspherical spaces*, §4 (https://doi.org/10.1016/j.topol.2015.04.005), and in standard accounts of Higman's group.

Any representation \(\Pi_S\to\underline{\mathrm{GL}_n(k)}\) is trivial too: by the indexed-free-product universal property, it corresponds to an internally continuous family of representations of H, and each is trivial. Thus **finite-dimensional monodromy with a globally fixed constant k^n fibre** cannot distinguish E_S from the point in positive twisted cohomology. More strongly, if M is a finitely generated abelian group, any H-action M factors through Aut(M) which has a faithful representation in a finite group times a finitely generated linear group; the no-finite-quotient argument makes it trivial. As H is acyclic, the resulting cohomology is zero in positive degree. The same conclusion holds on each ordinary fibre of \(\Pi_S(*)\), a free product of H factors.

**Do NOT claim that arbitrary finite-rank vector bundles in the ambient condensed topos are constant objects:** our argument applies to monodromy representations into a **fixed constant** GL_n(k) (or finite-rank coefficient group). Parametrized coefficient sheaves may have separate Stone-site phenomena.

## 2. Infinite augmentation-ideal coefficients detect group cohomology immediately

Let \(R=\mathbb Z[H]\), with left regular H action, and \(I=\ker(R\overset{\varepsilon}\to\mathbb Z)\). The augmentation exact sequence is
\[
0\longrightarrow I\longrightarrow R\overset{\varepsilon}\longrightarrow\mathbb Z\longrightarrow0.
\]
Define \(\beta_H:H\to I\) by
\[
\boxed{\beta_H(g)=g-1.}
\]
Then \(\beta_H(gh)=\beta_H(g)+g\beta_H(h)\), so this is a crossed homomorphism and determines the classical **Berstein–Schwarz class** \([\beta_H]\in H^1(H;I)\).

**Elementary nonvanishing proof:** If \(n\beta_H\) were a coboundary for some integer n, there would be m∈I with \(n(g-1)=gm-m\) for every g. Thus n−m∈R would be H-invariant. Since H is infinite, the left regular action on the finitely supported group ring has **no nonzero invariant element**. Hence n−m=0; applying augmentation yields n=0. In particular \([\beta_H]\) has infinite order. This is a detecting local system, and it must have infinite rank over Z: I has a basis g−1 for g≠1.

**Sharper classical result:** Bieri's proof that Higman H is a duality group of dimension 2 gives \(H^0(H;R)=H^1(H;R)=0\). The augmentation long exact sequence therefore supplies the exact calculation
\[
\boxed{H^1(H;I)\cong\mathbb Z}
\]
with generator \([\beta_H]\). It also implies \(H^2(H;R)\ne0\), the nonzero **dualizing module**. This is a second, degree-two detecting infinite-rank local system (the regular group ring R).

An even more natural degree-two obstruction is the cup square
\[
\boxed{\beta_H^2\ne0\in H^2(H;I\otimes_{\mathbb Z}I)}
\]
for the diagonal H-action on the tensor square. This follows from the **classical Berstein–Schwarz universality theorem**: for a group of finite cohomological dimension, \(\mathrm{cd}(H)=\max\{n:\beta_H^n\ne0\}\). Here cd(H)=2. Reference A. Dranishnikov, *On macroscopic dimension of universal coverings of closed manifolds*, Theorem 5.1 and Corollary 5.2 (https://pure.mpg.de/rest/items/item_3119915/component/file_3119916/content); also the Farber/Grant/Lupton/Oprea literature.

In the Stone-indexed object E_S, pull the local coefficient sheaf I or I⊗I back along the fold map \(E_S=B\Pi_S\to\underline{BH}\). The global s0-factor inclusion splits this fold. Therefore **both** the degree-one class \(\rho^*\beta_H\) and the degree-two class \(\rho^*(\beta_H^2)\) are nonzero: their restrictions along the s0 inclusion recover the respective nonzero H classes. These are honest **twisted-coefficient** detections of nontrivial homotopy that constant-coefficient homology and finite-dimensional field monodromy miss.

These two pulled-back classes by themselves need **not** distinguish E_S from E_T for distinct Stone S,T; they already exist for S a single point. To study topology of S, analyze **families of crossed homomorphisms**, as follows.

## 3. Internal first twisted-cohomology sheaf: exact calculation

The fold \(\rho:\Pi_S\to\underline H\) makes \(\underline I\) a \(\Pi_S\)-module: each indexed H-factor acts via the left regular H-action on I. Let
\[
\mathscr H^1_S:=\underline{\operatorname{Der}}(\Pi_S,\underline I)/
\underline{\operatorname{Inn}}(\Pi_S,\underline I)
\]
denote the **internal sheaf of degree-one group-cohomology classes** (the sheaf quotient of crossed derivations by principal derivations), equivalently degree-one internal cohomology of BΠ with the folded local coefficient module. This is NOT the same operation as first applying \((-) (*)\) to E_S and then computing ordinary group cohomology.

Set \(D=\operatorname{Der}(H,I)\) (an ordinary discrete abelian group). Since H is finitely presented, D is cut out by finitely many linear cocycle equations in I^4, so its *internal* constant sheaf is exactly the sheaf of H-derivations with values in \(\underline I\). The indexed free product's universal property identifies
\[
\underline{\operatorname{Der}}(\Pi_S,\underline I)
\cong(\underline D)^{h(S)}.
\]

**Compact-Stone exponential lemma.** For any discrete set/group D and compact Stone S,
\[
\boxed{(\underline D)^{h(S)}\cong
\underline{\operatorname{LC}(S,D)}}
\]
where LC(S,D) means *continuous locally constant functions* S→D_disc, endowed with the **discrete** topology on the function set before taking its constant sheaf. Proof: for any test Stone T, both sides have sections respectively \(\operatorname{Cont}(T\times S,D_{\rm disc})\) and \(\operatorname{Cont}(T,\operatorname{LC}(S,D)_{\rm disc})\). Every continuous T×S→D has finite image and its clopen fibers can be refined by finitely many **clopen rectangles**, so the slice function T→LC(S,D) is locally constant. Conversely a locally constant family of locally constant maps assembles to a continuous T×S→D. Naturality proves the claim.

By Bieri duality and §2, the map \(I\to D\) taking m to principal derivation \(\delta_m(g)=gm-m\) is injective (H has no nonzero invariant in I), and D/I≅Z with a **canonical splitting** n↦nβ_H. Hence
\[
D\cong I\oplus\mathbb Z.
\]

A principal \(\Pi_S\)-derivation comes from a *single* element of I, the same on **every** H-factor; under the last identification it is the **diagonal constant-function subgroup** \(I\subseteq\operatorname{LC}(S,I)\), with zero Z-component. Therefore
\[
\boxed{
\mathscr H^1_S\cong
\underline{\left(\operatorname{LC}(S,I)/I\right)
\oplus\operatorname{LC}(S,\mathbb Z)} .
}
\tag{★}
\]

This is an exact internal **sheaf** calculation in degree one. The formula has two natural components: variation of principal H-derivations between different S-factors, and locally constant integer multiples of the Berstein–Schwarz class on each factor.

**Explicit cocycles and an injection.** For every f∈LC(S,Z), define on an indexed generator (s,g) the crossed derivation
\[
d_f(s,g)=f(s)(g-1)\in I.
\]
Continuity of f makes this a morphism of sheaves; it extends uniquely to a crossed derivation \(\Pi_S\to\underline I\). Restriction to the factor s recovers f(s)β_H. If its class were principal, every f(s)β_H would be principal on H, forcing f=0 by §2. Thus the \(\operatorname{LC}(S,\mathbb Z)\) summand in (★) is embedded explicitly by cocycles.

**Surprising conclusion:** \(\mathscr H^1_S\) is actually a **CONSTANT sheaf**, despite E_S being nonconstant and despite the folded coefficient module detecting nontrivial cohomology. The abstract group \(\operatorname{LC}(S,D)\) depends on the Stone space, but this *unmarked first-cohomology sheaf* need not reconstruct its topology. The coefficient \(\underline I\) is constant as an abelian sheaf; its **monodromy is nontrivial**.

## 4. Internal cohomology is NOT cohomology after point evaluation

Since \(\Pi_S(*)\cong *_{s\in S_{\rm set}}H\), **ordinary** crossed derivations on the point-evaluated group can assign *arbitrary* H-derivations to each discrete factor, without any continuity in s. Consequently the previous calculation with products (rather than LC-functions) gives
\[
\boxed{
H^1\bigl(\Pi_S(*);I\bigr)
\cong
\bigl(I^{S_{\rm set}}/I\bigr)
\oplus\mathbb Z^{S_{\rm set}}.
}
\tag{★★}
\]
This can be much bigger than \(\mathscr H^1_S(*)\) from (★): evaluation at * does not generally commute with the **internal Hom/mapping-space operation** used to define cohomology, even though it does preserve the finite limits and colimits needed to form E_S itself.

For Cantor S, H and I are countable, and the Boolean algebra of clopens of S is countable. Hence LC(S,I) and LC(S,Z) are **countable** groups, so \(\mathscr H^1_S(*)\) is countable. But \(\mathbb Z^{S_{\rm set}}\) in (★★) has cardinality \(2^{2^{\aleph_0}}\). The disparity is real: sheaf-internal cocycles must vary **continuously** in S, while cocycles on the ordinary point-evaluated free product need not.

**Careful limitation:** The internal \(\mathscr H^1_S\) formula is a computation of a **sheaf of locally defined twisted cohomology classes**, not an assertion that all higher twisted cohomology is constant or that (★) alone detects nonconstancy of E_S. Indeed this first twisted-cohomology sheaf is constant. The homotopy object is separately known to be nonconstant by its \(\pi_1\) sheaf and the identity-section argument.

## 5. Research directions and provenance

**Positive results now available:**
- Acyclic coherent common-hull objects can be invisible to every ordinary constant-coefficient homology theory, all finite quotients, and all finite-dimensional constant-field monodromy (published Higman facts).
- Infinite-rank augmentation ideal I gives a **nonzero, explicit degree-one class**, and the regular module \(\mathbb Z[H]\), or I⊗I, gives a **nonzero degree-two class**. These transfer to the coherent E_S by the fold and its chosen-point section.
- Internal degree-one twisted cohomology of the fold coefficients is computable via clopen functions on S, with precise contrast to point-evaluated cohomology.

**Open next step in this chosen branch:** Find coefficient sheaves or local systems **depending essentially on h(S)** whose *twisted cohomology sheaves themselves* are nonconstant; our natural folded constant-underlying-I coefficients yield the constant sheaf (★). A candidate is the intrinsic augmentation ideal \(\mathcal I_{\Pi_S}=\ker(\mathbb Z[\Pi_S]\to\mathbb Z)\) with full \(\Pi_S\)-action; its first Berstein–Schwarz class is nonzero, but its full internal cohomology remains to be calculated. Another possibility is a local system induced from one S-indexed factor, though choosing an individual point may discard topology.

**Road not taken (PRESERVED):** What do the new sheaf homotopy invariants say about the **original binary separation hierarchy** \(\mathcal I,\mathcal D,\mathcal U,\mathcal V,\mathcal W,\mathcal H\)? The next branch has its own [explicit problem roadmap](PointFree_binary_relation_homotopy_feedback_ROADMAP_2026-11-10.md), including a concrete test of strict binary incomparability despite canonical C≃I≃D.

**Sources/past status:**
- Bieri, *Homological Dimension of Discrete Groups*, Chapter III §9.8, Example 5 (Higman is a duality group of dimension 2): https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bieri.pdf .
- Higman/Mal'cev and the finite-dimensional-obstruction observation: *New lower bounds for the topological complexity of aspherical spaces*, §4, https://doi.org/10.1016/j.topol.2015.04.005 .
- Dranishnikov, *On macroscopic dimension of universal coverings of closed manifolds*, Thm. 5.1/Cor. 5.2 (universal Berstein–Schwarz cup powers): https://pure.mpg.de/rest/items/item_3119915/component/file_3119916/content .
- Earlier third independent referee report and corrected account: [original blind report](audits/2026-11-10/postaudit-sheaf/Referee_report_original.md) and [reconciliation](PointFree_postaudit_sheaf_EXTERNAL_referee_reconciliation_2026-11-10.md).
- This **new internal twisted-coefficient segment** is NOT included in earlier audits, and no publication-priority claim is made.
