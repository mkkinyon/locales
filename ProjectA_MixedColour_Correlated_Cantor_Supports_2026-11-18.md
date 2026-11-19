# Project A — correlated Cantor supports for mixed-colour two-step composition

**18 November 2026. New conditional theorem candidate; internal checks only. Not externally audited.**  This supplements `ProjectA_MixedColour_TwoStep_Positive_Core_2026-11-18.md`. The objective is to test whether the positive mixed-colour two-step relation is supported only by *rectangular* common-middle density channels. It is not: the explicit finite-fence model also has nonzero Boolean witnesses supported on closed Cantor *graphs*.

## 1. A coordinate-injective two-colour Cantor lemma

**Lemma.** Let `Y=Y_1×Y_2×Y_3`, where each `Y_i` is a nonempty perfect metrizable space. Suppose `R,S⊂Y` are dense and `F_1⊂Y_1`, `F_3⊂Y_3` are countable sets avoided by both the first and third coordinates, respectively, of every point of `R∪S`. Within any nonempty open product box whose coordinate spaces contain compact perfect neighbourhoods, there is a compact Cantor set `C⊂Y` such that:

1. `C∩R` and `C∩S` are each dense in `C`;
2. all three coordinate projections `C→Y_i` are injective (hence homeomorphisms onto their compact images);
3. the first and third coordinate projections of `C` avoid `F_1,F_3`.

**Proof.** Choose a relatively compact initial product box with perfect coordinate neighbourhoods and enumerate the two forbidden coordinate sets. Construct nested binary families of compact product boxes `B_s`, with nonempty interiors, diameters tending uniformly to zero, and distinguished anchors `e_s∈R∪S` in the interiors. At every node retain `e_s` as the anchor of the zero-child. For the one-child choose a fresh anchor from `R` on even levels and `S` on odd levels, within the parent's interior but off the three coordinate hyperplanes through `e_s`. These hyperplanes are nowhere dense (perfectness of the factors), so the required dense set contains such an anchor. Choose the two children with disjoint *projections in each coordinate*, shrinking about the two anchors and avoiding the first `n` forbidden coordinate points at stage `n`; the anchors themselves avoid all forbidden points. All anchors persist along their all-zero descendant branches.

The limit `C=⋂_n⋃_{|s|=n}B_s` is Cantor: disjoint binary splitting gives perfectness and shrinking diameters gives compactness and zero-dimensionality. At each split the coordinate projections of siblings are disjoint, so each coordinate projection is injective on `C`. Every cylinder has descendants with new persistent `R`- and `S`-anchors, hence both traces are dense in `C`. Stagewise avoidance removes all forbidden first/third coordinates. ∎

**Scope of lemma.** Perfect metrizability alone does not supply compact neighbourhoods; the application is to an open product box in a product of compact metric Cantors and real intervals, where the displayed construction is legitimate. The stated initial-box qualification is essential.

## 2. Two dense triple colours in the explicit finite-fence model

Use notation of the positive-core note: `X` is the upper locale of the compact height-one ordered interval, `p` its patch map, `H=H_G=[E_G]`, `T=H∘H`, `M` the middle Cantor, and `U_P,U_Q` the two mediator gaps. Let `E_P^{min}⊂U_P` and `E_Q^{min}⊂U_Q` be the permitted minimal vertices of the respective fence colours. They are countable dense subsets of their gaps. Crucially, for every nonempty open `O⊂U_P`, every nonempty relative open `V⊂M`, and arbitrarily high `n`, some **minimal** `P_n` vertex lies in `O` while its same-fence endpoint `a_n` lies in `V`; similarly for `Q_m`, `b_m`, and `U_Q`. This follows from the endpoint density and monotone shrinking-mesh traversal already proved in the positive-core note.

Inside `Y=U_P×M×U_Q` define two countable sets of ordinary triples:

\[
\begin{aligned}
R_P&=\{(x,a_n,z):x\in V_{\min}(P_n)\cap U_P,\ z\in E_Q^{min}\},\\
R_Q&=\{(x,b_m,z):x\in E_P^{min},\ z\in V_{\min}(Q_m)\cap U_Q\}.
\end{aligned}\tag{1}
\]

Each is dense in `Y`: to meet an arbitrary nonempty basic box `O_P×V×O_Q`, use an endpoint-conditioned selected fence for the constrained pair of coordinates, and an independently selected permitted minimum for the remaining outer coordinate. Every triple of `R_P` satisfies the first ordinary component-equivalence condition `(x,a_n)∈E_G`; every triple of `R_Q` satisfies the second `(b_m,z)∈E_G`. No ordinary triple satisfies both conditions on the cross-gap box.

Both sets have first coordinate in `E_P^{min}` and third in `E_Q^{min}`. Take the forbidden first-coordinate set to be **all** fence vertices other than permitted `P` minima; take the forbidden third-coordinate set similarly for permitted `Q` minima. These are countable and avoided by the anchors.

## 3. Graph-supported positive witness

**Proposition (conditional, internally checked).** For any nonempty mediator opens `O_P⊂U_P` and `O_Q⊂U_Q` there are compact perfect lower-closed Cantor sets `D_P⊂O_P`, `D_Q⊂O_Q` and a homeomorphism `h:D_P→D_Q` such that, writing its patch-closed graph as `Γ_h⊂D_P×D_Q`,

\[
\boxed{0\ne\mathcal B(\Gamma_h)
\le (p\times p)^{-1}\bigl(T\wedge(G_P^*\times G_Q^*)\bigr).}\tag{2}
\]

The graph witness is disjoint from the ambient Boolean core and even from the Booleanization of its own outer Cantor product:

\[
\mathcal B(\Gamma_h)\wedge\mathcal B(U_P\times U_Q)=0,
\qquad
\mathcal B(\Gamma_h)\wedge\mathcal B(D_P\times D_Q)=0.\tag{3}
\]

**Proof.** Choose compactly contained outer intervals in the prescribed opens, and a nonempty clopen sub-Cantor of `M`; apply the preceding lemma to the dense sets `(1)` in their product. Let `C⊂Y` be the resulting Cantor, with outer coordinate images `D_P,D_Q` and middle image `D_M`. Since each coordinate projection of `C` is a homeomorphism onto its image, the outer projection maps `C` homeomorphically onto the graph `Γ_h` of the induced homeomorphism `D_P→D_Q`.

On the *patch triple*, let `L` and `R` be the pullbacks of the two upper-localic one-step constraints. Every `R_P` point belongs to `L`, and every `R_Q` point belongs to `R`. Their traces in `C` are dense by construction. Hence `L∧C` and `R∧C` are dense sublocales of `C`; by Isbell's density theorem,

\[
\mathcal B(C)\le L\wedge R\wedge C.\tag{4}
\]

Thus `B(C)→X³` factors through the **actual** upper-localic composable-pair sublocale, before its outer image. It follows that its image `B(Γ_h)` under the patch outer projection belongs to the patch inverse image of `T`. No base-change identity for arbitrary localic images is used.

For the generic-fibre inclusion, each outer Cantor projection contains a dense trace of allowed minimal fence vertices: the persistent anchors are dense in `C`, and coordinate projections are homeomorphisms. The construction excludes all other fence vertices from `D_P,D_Q`. All points of either Cantor are therefore minimal order points or singleton-comparability points, so both Cantors are patch-closed **lower** sets and hence closed sublocales of `X`. Every nonempty relatively open subset of either Cantor contains infinitely many fence vertices. A patch-closed quotient cutoff meeting the full vertex set finitely is thus nowhere dense on either Cantor; quotient opens not containing the generic point miss all these vertices. The same generic quotient-point tests as in the preceding notes give

\[
\mathcal B(D_P)\le p^{-1}(G_P^*),\qquad
\mathcal B(D_Q)\le p^{-1}(G_Q^*).
\]

As both outer maps `C→D_P,D_Q` are homeomorphisms, their inverse images of these generic sublocales are dense in `C`, hence contain `B(C)`. Transporting through the outer graph homeomorphism places `B(Γ_h)` in the patch generic product, proving `(2)`.

Finally `Γ_h` is a closed nowhere-dense subspace of `D_P×D_Q` (both Cantors are perfect), and it is closed nowhere dense in `U_P×U_Q`. Their least dense sublocales lie in the respective dense open complements of the graph, proving `(3)`. ∎

## 4. Interpretation and audit boundaries

- The graph `Γ_h` is a **patch** graph. We do **not** claim that it is closed or lower in the upper *square*. Its Booleanization transports to an upper-localic sublocale using the previously established isomorphism between the patch generic product and `G_P^*×G_Q^*`.
- The common closed support `C` is **nonrectangular**. The abstract necessary-and-sufficient criterion found subsequently says that nonvanishing of `(H∘H)∧(A×B)` for closed outer `A,B` is equivalent to existence of a nonzero closed triple support on which both one-step restrictions are dense. The present proof constructs such a support **in the patch triple** and then transfers its Booleanization into the upper composite; no assertion that the abstract upper-triple closed support is exactly `C` is made.
- The result does **not** prove that every nonzero two-step piece must have a graph support, or that a rectangular criterion cannot detect *nonvanishing* somewhere in the finite-fence model. It proves the stronger existence of correlated graph-shaped positive pieces not contained in the obvious product Booleanizations.
- Internal adversarial checklist: verify (i) endpoint-conditioned **minimal** vertex density, (ii) simultaneous forbidden-vertex avoidance and coordinate injectivity in the Cantor lemma, (iii) both localic density inclusions in `(4)`, (iv) the generic-fibre tests on the outer Cantors, and (v) the patch/upper typing at `(2)`. All have been checked in the argument, but none has received a separate external audit.

**Suggested next test:** Can the finite-fence two-step restriction be described as a join of Booleanizations of closed *incidence correspondences* (graphs and products being special cases), and if so, which correspondence families suffice? The abstract triple-support equivalence proves **existence** of an individual Boolean support whenever a closed outer rectangle is met; it does not by itself prove a **join decomposition** of the entire mixed two-step sublocale.
