# Project A — Relational associativity audit I: explicit failure and coherent repair

> **WITHDRAWN IMAGE ARGUMENT (11 November 2026).** The proof below incorrectly asserts that the inclusion of a proper topologically dense subset with the discrete topology is a **locale-surjection**. It is not: the whole target and the open complement of an omitted closed point have equal inverse images. The claimed **specific** nonassociative-relations example and deductions depending on that image identity are therefore **NOT established** by this file. Do not cite them as valid. See [precise correction](ProjectA_CO01_historical_dense_inclusion_locale_surjection_CORRECTION_2026-11-11.md). Other independently established results must be assessed on their own proofs.


7 November 2026. **Internally derived; categorical source cross-check performed.** The general nonassociativity is explicit; the coherent/proconstructible repair and compact-closed repair have proofs here, with external audit recommended for categorical details. This DOES NOT affect the independently refereed negative theorem I∘D⊄V (only one composition).

## 1. Convention, issue, and explicit example

Composition R∘S (diagrammatic order: first R then S) is the localic IMAGE of R×_B S→A×C for R⊆A×B, S⊆B×C. Unlike a regular category, Loc has surjections that fail pullback stability (Picado–Pultr–Tozzi, *Locales*, Chapter II p.86, https://www.mat.uc.pt/~picado/publicat/Chapter2.pdf). Cf. Paul Taylor, *Practical Foundations of Mathematics*, Lemma 5.8.6: general all-relation associativity requires regularity.

Let Y=N∪{∞} have topology {∅} ∪ {Y\F:F⊆N finite}. Put E=N_discrete and Z=(N∪{∞})_discrete. Let f:E→Y be inclusion, g:Z→Y underlying identity.

The localic f is SURJECTIVE: its frame inverse image O(Y)→P(N) restricts Y\F to N\F and is injective. Its pullback along g is NOT surjective: E×_Y Z≅E, with projection j:E→Z the inclusion omitting ∞.

Explicit pushout computation: Given frame maps α:P(N)→M and β:P(Z)→M agreeing on O(Y), equality on cofinite opens Y\{n}, followed by complement preservation for the powerset Boolean domains, gives α({n})=β({n}) for every n. Their join under α is 1; disjointness forces β({∞})=0. So β=α∘j*, and the Frm pushout of O(Y)→P(N), O(Y)→P(Z) is P(N).

Choose relations R:1→E total (R=E); S:E→Y graph(f); T:Y→Z the converse graph(g). Then

    R∘S=im(f)=Y,
    (R∘S)∘T=Z,
    S∘T=graph(j),
    R∘(S∘T)=im(j)=N⊊Z.

Thus **(R∘S)∘T≠R∘(S∘T)**, for relations given by actual sublocale embeddings. To make three ENDORELATIONS on one locale take X=1⊔E⊔Y⊔Z and support R,S,T only on successive clopen blocks. Finite localic coproducts are disjoint and stable, so the failure persists.

## 2. Precise obstruction and safe image criterion

Given R:A→B, S:B→C, T:C→D, let Q=R×_B S×_C T, F=im(Q→A×D). Universally

    F ≤ (R∘S)∘T,     F ≤ R∘(S∘T),

but no general comparison between bracketings.

Let e_RS:R×_B S→R∘S be the canonical localic surjection onto the image, and e_ST similarly. If the pullback of e_RS along its comparison with T remains surjective, then (R∘S)∘T=F. If the corresponding pullback of e_ST along R remains surjective, R∘(S∘T)=F. If BOTH hold then associative. OPEN and PROPER surjections are pullback-stable, giving useful sufficient conditions.

## 3. Coherent repair: proconstructible relations ARE associative

**Theorem (working categorical proof).** Let X be a coherent locale with spectral point space P. Proconstructible (patch-closed) spectral sublocales R⊆X² form an associative relation algebra under image-defined localic composition, with binary composite corresponding exactly to the ordinary point-set composite.

Proof. Coherent localic finite products/pullbacks along spectral maps correspond to spectral-space products/pullbacks (also see Dickmann–Schwartz–Tressl, *Spectral Spaces* 2019, Thm. 2.3.7). For patch-closed R_P,S_P⊆P², the composable triples E_P⊆P³ form a patch-closed (compact Hausdorff patch) subspace. π13(E_P) is patch-closed in P², since projections are patch-continuous and compact images in Hausdorff spaces are closed (ibid., Cor. 1.3.23). The map E_P→π13(E_P) is ONTO POINTS, therefore surjective as a locale map because π13(E_P) is spatial. Its localic image is precisely the proconstructible sublocale determined by π13(E_P). The same observation holds after any spectral base change, because the spectral fiber product is pointwise and the pullback map is still pointwise surjective onto a spatial spectral target. Hence composition is literally the point-set composite, and is associative. Finite joins correspond to finite unions of patch-closed subspaces, so ordinary finite distributivity applies.

**Consequence:** in coherent locales A,B (specialization orders), I (closed diagonal hull), and D (the earlier coherent proconstructible fitted diagonal) lie in this safe relation class. The associativity step of I=AB,D=BA,R=ABA,R'=BAB, finite C_cmp powers, and the finite stages of the H recursion is therefore justified. This audit addresses ASSOCIATIVITY, not all other dependencies in those results.

## 4. Compact-closed repair

**Proposition.** For any compact locale X, all CLOSED relations R,S,T⊆X² compose associatively and their binary composite is closed.

For closed R,S the composable-pair E_RS=R12∧S23 is closed in X³. Its projection to X² is PROPER (closed inclusion followed by projection discarding a compact factor), and its image is closed. The surjection E_RS→R∘S is proper, hence pullback-stable. Likewise for S,T. Therefore both bracketings equal the image of the four-coordinate composable-pair locale. This works without coherence, regularity or Hausdorffness of X. In particular powers of I=cl Δ are associative in every compact locale. This alone does not cover D=fit Δ, which need not be closed.

Similarly, OPEN relations with overt middle locales have open composable sources, open projections and pullback-stable open image-surjections; they compose associatively.

## 5. Impact ledger

**Safe without associativity:** Δ is two-sided unit; converse reverses binary composition; monotonicity; A²=A,B²=B by direct transitivity on generalized points; A∘C=C=C∘B for any CLOSED C, B∘F=F=F∘A for FITTED F, from direct coordinate monotonicity; universal I∘D≤U by binary far-cover proof; negative I∘D⊄V and D²⊄D from the independently refereed single-composition witness.

For arbitrary S, BOTH parenthesizations (A∘S)∘B and A∘(S∘B) are ≤cl(S), using only monotonicity and CLOSED module equalities; analogously both B,S,A parenthesizations are ≤fit(S). Never leave parentheses ambiguous in arbitrary Loc.

**Working but not established without further argument for arbitrary X:** A∘(I∘D)=I∘D=(I∘D)∘A, and the analogous B-distributor claim for D∘I, were previously derived by unqualified reassociation. Similarly, “A∘J∘A is the least distributor hull” needs a direct proof, not mere A²=A. One-step saturation can fail to be a fixed point when images are nonstable. No counterexample to these PARTICULAR assertions is yet claimed.

**Safe under the coherent spectral hypotheses:** ordinary two-idempotent and comparability graph relations, all finite alternating words and their finite joins. At ordinal limits, retain patch closure rather than bare union.

## 6. Next target

Investigate the special claimed all-locale saturation of R=I∘D under canonical specialization A. Either give a direct localic proof avoiding reassociation or find a counterexample. The independently audited negative mixed-composition example is an especially useful test. A second audit should explicitly review whether the proconstructible/localic identification is being used only for SPECTRAL maps and patch-closed sublocales.

Sources: Picado–Pultr–Tozzi, *Locales*, II.5 p.86; Taylor, *Practical Foundations*, Lemma 5.8.6; Dickmann–Schwartz–Tressl, *Spectral Spaces*, 2019, Cor. 1.3.23, Thm. 2.3.7; localic open/proper pullback-stability theorems.

## 7. RESPONSE TO THE SAME-LOCALE OBJECTION: ONE SYMMETRIC REFLEXIVE ENDORRELATION SUFFICES

A natural objection to §1 is that R,S,T initially lie between FOUR different locales, whereas the project studies endorelations on one locale X. This restriction does NOT save associativity; in fact even powers of ONE reflexive symmetric endorelation can be nonassociative.

Use precisely the locales of §1, and put

    X = 1 ⊔ E ⊔ Y ⊔ Z.

The frame is 2×P(N)×O(Y)×P(N∪{∞}). The four summands are CLOPEN sublocales of X, and the sixteen (source,target) pairs are clopen blocks of X². Loc is an extensive category: stable, disjoint finite coproducts; this can also be proved directly since the images of (1,0) and (0,1) under a frame homomorphism are complementary.

Let R be the total relation on the block 1×E; S the graph of f:E→Y; T the converse graph of g:Z→Y. Regard them as sublocales of X², supported on those individual blocks. Define ONE endorelation

    Q = Δ_X ∨ R ∨ R^smile ∨ S ∨ S^smile ∨ T ∨ T^smile.

Then Q=Q^smile and Δ_X≤Q. Because its support is confined to successive edges of the four-block undirected chain 1--E--Y--Z, and all on-block effects are just the diagonals, blockwise composition gives:

    (Q∘Q) |_(1×Y) = 1×Y      (because im f=Y);
    (Q∘Q) |_(E×Z) = graph(j) (because E×_Y Z≅E, j:N→Z);
    (Q∘Q) |_(1×Z) = 0       (no path of length ≤2).

Therefore on the SAME block 1×Z,

    ((Q∘Q)∘Q)|_(1×Z) = 1×Z,
    (Q∘(Q∘Q))|_(1×Z) = 1×N ⊊ 1×Z.

The left bracketing arises from 1→Y by Q² (im f=Y) followed by Y→Z (converse graph g). The right arises from 1→E by Q followed by E→Z by Q² (graph j); ∞ is missed. The added diagonals and converses do NOT create a new three-step route from 1 to Z, because each step changes the block by at most one along the chain. The unique three-step block itinerary is 1→E→Y→Z.

Thus

    **(Q∘Q)∘Q ≠ Q∘(Q∘Q)**

for a SINGLE REFLEXIVE SYMMETRIC relation Q⊆X² on one single frame L=O(X).

This is materially stronger than the original heterogeneous-relations example and matches the formal conditions reflexivity and symmetry shared by I and D. It does NOT show that any actual diagonal hull I_X or D_X has nonassociative powers; such special identities still require separate analysis.

**Source check:** Loc is extensive, e.g. *Free Doubly-Infinitary Distributive Categories are Cartesian Closed* (2026), §6.4.1, provides a direct proof from complementary idempotents of products of frames. The block calculation itself is elementary and follows from the same frame decomposition; no blanket pullback-stability of arbitrary image-surjections is invoked.

## 8. Updated audit focus

The minimal all-endorelation obstacle is settled NEGATIVELY, even under reflexivity/symmetry and even for ONE Q. Focus next on the PARTICULAR special relations A,B,I,D, where closedness, fittedness, and specialization monotonicity might enforce restricted association or module identities that general symmetric reflexive relations lack. Do not conflate the one-Q example with a counterexample to specific identities such as (I∘I)∘I=I∘(I∘I).
