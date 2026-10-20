> **SOURCE CORRECTION (19 October 2026):** Vermeulen, *Proper Maps of Locales* (1994), **Corollary 5.17**, proves that **closed proper equivalence relations are effective on arbitrary locales**—without assuming compactness of the ambient locale. The earlier restriction to compact locales was a misreading of a later paper's application. For a continuous L, proper projections of I=U yield a proper continuous strongly Hausdorff quotient; Vermeulen supplies I=kerpair(q), and complete regularity of the quotient gives **I=U=F** entirely locally. See [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md).

# Project A — Literature and priority review: first-pass source ledger

**Date:** 19 October 2026. **Status:** first-pass bibliographical survey, not an exhaustive search or a priority certification. This review is conducted while the other researcher reads Picado–Pultr (2021) independently. Results come from the specifically linked **published source texts, abstracts, or readily accessible public documents**, and are labeled accordingly. The provisional classifications below mean:

- **KNOWN**: close formal result/definition is explicitly present in a named source.
- **FORMAL CONSEQUENCE**: follows immediately from a known theorem or construction, although the source may not state our formulation.
- **CANDIDATE CONNECTION**: a source addresses essentially the same topic but exact equivalence has not been established.
- **NOT LOCATED**: no exact predecessor found by these targeted searches; **not** evidence of originality.

A useful guiding distinction is between a **pointwise graph identity**, a **closed/fitted localic relation**, and an **implication between frame properties**. They can have different priority assessments.

> **EXTERNAL AUDIT RECONCILIATION (20 October 2026):** The original Vermeulen 1994 article was supplied and examined directly; its **Corollary 5.17** settles effectiveness of closed proper equivalence relations for *all* locales. Two outside reviews confirmed the basic relation framework and the proper continuous collapse, and found a stronger counterexample to unconditional idempotence of r_I even when I=clΔ=U=F. The original two-tag deleted-plank example is **arithmetic** (so stable continuity alone fails), and the compact transitive-I theorem extends to **nonspatial compact locales** (using the standard compact Hausdorff locale theorem, whose precise primary citation is still to be supplied). Full editorial resolution and outstanding checks: [A-external-audits-reconciliation-2026-10-20.md](A-external-audits-reconciliation-2026-10-20.md); example proof: [A-saturation-operator-nonidempotence.md](A-saturation-operator-nonidempotence.md). **Neither review was strictly blind**, because the internal audit was included in both contexts.

**NEW WORKING CONSTRUCTION, PRIORITY UNEXAMINED (20 October 2026):** [A-subfit-arithmetic-counterexample.md](A-subfit-arithmetic-counterexample.md) combines subfitness and arithmeticity in a deleted-plank counterexample to I=U implies U=F, by attaching cofinite clouds and passing to sobrification. The positive boundary for **sober T1 arithmetic** spaces is zero-dimensionality (via the standard T1 spectral implies Stone theorem). No originality certification.

## 0. Major new synthesis: fitted diagonal recovers the fifth Cameron–Kumar graph

**Our construction:** D(X)=fit(Δ_X)⊆X×X, a fitted (generally nonclosed) sublocale.

**Exactly known graph:** Cameron–Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783 (posted 10 Oct 2026), Definition 3.1, calls

    Cm(X) = { (x,y) : cl{x}∩cl{y}≠∅ }

the **closure-meeting graph**, and Theorem 3.2 gives

    Sp⊆Ins∩Cm,      Ins∪Cm⊆Ury⊆Fun,

with Ins and Cm incomparable, plus the T1 nullity test for Cm. PDF: https://arxiv.org/pdf/2610.14783 .

**Pointwise equality proved in our notes:** For every space X and **original pair** (x,y), its induced locale point factors through D(X) iff every open cover of X contains an element containing both x,y. This is **equivalent to** cl{x}∩cl{y}≠∅: a common specialization z forces such a cover member, while if singleton closures are disjoint the cover {X\cl{x},X\cl{y}} defeats the condition.

**Classification: KNOWN pointwise graph, CANDIDATE point-free realization.** The graph-theoretic diamond, incomparability, and T1 interpretation are **already Cameron–Kumar's results**. Their identification with the **points of the fitted diagonal** is a natural new realization in our framework; no prior locale-theoretic formulation has been located yet. This makes our model a natural locale-level companion of **four of Cameron–Kumar's five** graphs (Ins, Cm, Ury, Fun), not an unrelated fourth relation. Their fifth graph, **specialization**, has *not yet* been represented as a separate localic relation in our notes and remains deferred. See [A-fitted-diagonal.md](A-fitted-diagonal.md).

**Important scope:** D(X) is generally nonclosed. Equality of the point relation with Cm(X) does not imply that full localic D has any specified representation by closed sublocales; Fsep is a stronger point-free axiom than pointwise T1.

## 1. Ordinary closure and fitting of the diagonal

**KNOWN.** Igor Arrieta, Jorge Picado, Aleš Pultr, *A New Diagonal Separation and Its Relations With the Hausdorff Property*, **Applied Categorical Structures** 30(2) (2022), 247–263, DOI 10.1007/s10485-021-09655-9; author preprint https://www.mat.uc.pt/preprints/ps/p2117.pdf .

- (Fsep) is exactly **the diagonal is fitted**, equivalently fit(Δ)=Δ.
- The paper gives Dowker–Strauss-type characterization using parallel frame homomorphisms and a characterization by almost frame homomorphisms.
- **Exact match for a preexisting diagonal test:** its Theorem **4.5** characterizes (Fsep) by the absence of distinct parallel frame maps h,k:L→M satisfying `∨_{c∈C} h(c)∧k(c)=1` for every cover C of L (their phrase is **respecting covers**). Theorem **4.6.1** gives the corresponding Dowker–Strauss characterization of (sH), our condition I=Δ, via behavior on disjoint pairs. **These are predecessors of the style of our parallel-map characterizations**; our equality tests I=U and U=F compare different annihilator conditions and should be assessed as relative variants, not an independent invention of the method.
- It is *not* our functional relation F despite the “F-separated” label.
- Our I=cl(Δ) is the standard strongly Hausdorff/Isbell diagonal-closure apparatus, not novel.

**KNOWN and especially close:** Igor Arrieta, *Localic Separation and the Duality Between Closedness and Fittedness*, **Topology and its Applications** 342 (2024), 108785, DOI 10.1016/j.topol.2023.108785. **Full published open-access PDF:** https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf .

- Introduction and §2.5 place ordinary closure and fitting of the diagonal in an explicit duality, identifying strongly Hausdorff vs F-separated locales and citing the 2022 paper.
- §2.4 writes the localic diagonal and its closure as c(d_L), with d_L=∨_{a∧b=0} a⊕b, **our d_I formula already present explicitly**.
- Proposition 2.1 treats equalizers and categorical closure under limits of both separated classes.
- Theorem/corollary in §4 gives strongly Hausdorff spatial locales that are *not* F-separated, separating the two point-free conditions.
- The cited precursor [9] is M. M. Clementino, J. Picado, A. Pultr, *The Other Closure and Complete Sublocales*, **Applied Categorical Structures** 26 (2018), 891–906, DOI 10.1007/s10485-018-9516-4. The paper has a **published correction** DOI 10.1007/s10485-018-9533-3 concerning its c-subfitness Theorem 5.3; use corrected versions when relevant.

**Interpretation:** I itself and fitted Δ are established; **our two-branch comparison D⊆U is not yet located as an explicit statement**. Its pointwise consequence Cm⊆Ury is already in Cameron–Kumar.

## 2. Very close source for the Urysohn relation: anti-Urysohn locales

**KNOWN, EXACT EXTREME CASE.** In the same Arrieta (2024) paper, **Definition 4.6** defines a locale L to be **anti-Urysohn** when for every nonzero a,b∈L one has

    a*∨b*≠1.

In our notation d_U=∨_{a*∨b*=1}a⊠b and U=C(d_U). Because a⊠b is nonzero iff both factors are nonzero, the published anti-Urysohn condition is **equivalent to**

    U(X)=X×X.

This is an **immediate translation of an existing definition**, not a new theorem; record the connection in the research notebook.

Arrieta's Proposition 4.8 and Construction 4.2/Example 4.5 use anti-Urysohn locales and spaces to separate localic properties. Underlying classical source: I. Juhász, L. Soukup, Z. Szentmiklóssy, *Anti-Urysohn spaces*, **Topology and its Applications** 213 (2016), 8–23 (Arrieta's ref. [16]).

**NOT LOCATED:** a published general definition of the specific **closed relation U=C(∨ far rectangles)**, as opposed to the property that U is total or diagonal. Search additionally for “Urysohn locale”, “farness”, “separated closed neighborhoods”, “Urysohn frame” and “Urysohn proximity”. A 2026 preprint called *On R1-Urysohn Spaces* (S. Jafari, preprint Oct 2 2026) defines a **different** condition; do **not** identify it with I=U merely from its name. It is recent and unrefereed.

## 3. Functional relation and completely regular reflection

**KNOWN UNDERLYING STRUCTURE / FORMAL CONSEQUENCE.** Picado–Pultr, *Separation in Point-Free Topology* (2021), Chapter VI, develops completely-below relations, cozero elements, and complete regularization by real-valued functions. In our notes, F is an intersection of kernels of all localic real maps and the kernel pair of the completely regular reflection r_X. The **kernel-pair equality is a formal categorical consequence** of the construction; no separate predecessor stating precisely this F symbol was located.

**Other underlying published treatment:** B. Banaschewski and C. R. A. Gilmour, *Cozero Bases of Frames*, **Journal of Pure and Applied Algebra** 157(1) (2001), 1–22, DOI 10.1016/S0022-4049(99)00167-X: cozero bases and completely regular frames. The article discusses the maximal cozero basis of completely regular frames. https://www.sciencedirect.com/science/article/pii/S002240499900167X .

**Caution:** cozero bases, completely regular reflection/coreflection, Stone–Čech coreflection and a frame epimorphism are related but distinct. We should not attribute our kernel-pair formulation to a source unless it actually states it.

## 3a. A definitive primary source for normality ⇒ U=F

**KNOWN theorem, not a new Project A result.** C. H. Dowker and Dona Papert, *On Urysohn's Lemma*, in *General Topology and its Relations to Modern Analysis and Algebra*, Proceedings of the Second Prague Topological Symposium (1966), Academia, Prague, **1967**, pp. 111–114, **Theorem 3**. Digital copy: https://dml.cz/dmlcz/700880 ; original PDF https://dml.cz/bitstream/handle/10338.dmlcz/700880/Toposym_02-1966-1_28.pdf . The catalog listing credits Dowker alone, but the original paper header and contemporary proceedings program name **Dowker and Papert**.

Picado–Pultr, *Separation in Point-Free Topology* (2021), p. 175, recover Urysohn's Lemma as a corollary of their point-free Katětov–Tong Insertion Theorem. As reported from the book: L is normal iff for every A∨B=1 there is a frame map h:L(R)→L such that

    h((−∞,0)∪(1,∞))=0;
    h((−∞,1))≤A;    h((0,∞))≤B.

(Equivalent statements reverse the roles of 0 and 1.)

**Direct rigorous translation:** Given a≺b, i.e. a*∨b=1, apply the lemma with A=a*, B=b. Since

    a∧h((−∞,1))=0,
    h((−∞,1))∨h((t,∞))=1     for t<1,

we have a≤h((t,∞)) for all 0<t<1. Also h((t,∞))≤h((0,∞))≤b. As t varies over rationals in (0,1), these opens form a nested *completely-below scale* (higher thresholds lie rather below lower thresholds because h preserves the frame-of-reals relations). Consequently a≺≺b.

**Established exact result:** J. Gutiérrez García and J. Picado, *On the Parallel Between Normality and Extremal Disconnectedness*, Coimbra preprint 13–04 (2013), **Remark 2.2**, https://www.mat.uc.pt/preprints/ps/p1304.pdf : in a normal frame, ≺ is interpolative and hence coincides with ≺≺ (classical dependent choice). Their proof shows a≺b implies a≺u≺b by one application of normality. Thus

    L normal ⇒ (∀ a,b, a≺b ⇔ a≺≺b).

Our U-generating far pair a*∨b*=1 is exactly a≺b*, so every U rectangle is an F rectangle. Combined with F⊇U always, this gives **U=F for every normal locale**. The *general equality U=F*, without the normality hypothesis, remains a separate question; do NOT claim equivalence to normality or attribute that to the papers.

**Classification: KNOWN core theorem; FORMAL CONSEQUENCE for Project A relation equality.**

## 4. Coherent frames: conormality / mp-rings / minimal primes

**KNOWN algebraic theorem.** W. H. Cornish, *Normal Lattices*, **Journal of the Australian Mathematical Society** 14 (1972), 200–215, DOI 10.1017/S1446788700010041. Cornish explicitly characterizes distributive lattices with the property “every prime ideal contains a unique minimal prime ideal” by a condition on annihilator ideals for disjoint elements. He uses **normal**, while later literature commonly uses **conormal** for this convention. Cambridge record: https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/normal-lattices/B71E90ADA1C98165B2EDD8C7B40BB289 .

**Exact modern citation:** George Georgescu, *Flat Topology on the Spectra of Quantales*, **Fuzzy Sets and Systems** 406 (2021), 22–41. Proposition **8.9** states conormality iff each prime ideal contains a unique minimal prime, Corollary **8.10** applies to coherent mp-quantales. DOI/source to verify for final bibliography; text accessible in indexed published-PDF extracts. Also Georgescu, *Lattices of Fractions and Flat Morphisms of Bounded Distributive Lattices* (2020), §6 / Proposition 6.1, for the same characterizations.

**Our result:** for coherent frame L,

    I(L)=U(L)  ⇔ K(L) conormal,

and for L=O(Spec R), this translates to the mp-ring condition. **Classification: FORMAL CONNECTION TO KNOWN ALGEBRA.** The conormality/prime/minimal-prime/mp-ring assertions are standard and must be cited, not offered as new algebra. The exact interpretation as equality of two localic closed subrelations may be new **as packaging**, but the intrinsic condition is established.

**NOT LOCATED:** the precise arbitrary-algebraic-frame rectangular equality test expressed in these same terms, or the parallel coherent U=F test; both may be formal consequences of the same elementary coproduct lemmas and of existing “well-inside/completely-inside” theory.

## 5. Positive compact, kω, σ-compact and paracompact results

**KNOWN point-set background.** Quotients of compact spaces by closed equivalence relations are compact Hausdorff under the standard hypotheses; the kω direct-limit and normality theorem is standard. A publicly accessible topology textbook *Topology Without Tears* lists “every Hausdorff kω-space is normal” explicitly as Chapter 10 exercise 5(iv): https://www.topologywithouttears.net/topbook.pdf . Earlier survey: S. P. Franklin and B. V. Smith Thomas, *A survey of kω-spaces*, **Topology Proceedings** 2 (1977), 111–124 (bibliographical reference from our own kω note; the primary text should be retrieved before claiming a precise theorem number).

**Especially close web proof (NOT an archival journal result).** A detailed Math.StackExchange answer to *Is R/~ a Hausdorff space if ... ?* contains the proposition that **a σ-locally-compact Hausdorff space modulo a closed equivalence relation has a normal Hausdorff quotient**. This overlaps our σ-compact quotient application; our theorem is stated for **arbitrary non-Hausdorff kω domains**, with explicit compact-stage compatibility. https://math.stackexchange.com/questions/2265141/is-mathbbr-mathord-sim-a-hausdorff-space-if-x-y-x-sim-y-is-a-c/2392314 . This web source is corroborative mathematical background, **not a substitute for a citeable journal or monograph**.

**KNOWN decomposition in Hausdorff setting.** Locally compact paracompact Hausdorff spaces decompose as disjoint sums of σ-compact pieces, familiar e.g. from Dugundji *Topology*. The non-Hausdorff variant of our notes uses the weaker “each point has some compact neighborhood” and a finite-degree refinement graph. Independently search whether Dugundji's proof extends exactly in that scope. A public MathOverflow answer cites Dugundji and gives a proof, but not the precise non-Hausdorff theorem: https://mathoverflow.net/questions/151026/locally-compact-space-that-is-not-topologically-complete .

**Verdict:** The tools, topological lemmas, and essential mechanism are classical. Our point-set combination is a careful adaptation rather than an established priority claim. The **closed-localic lifts** require **strong** local compactness and sobriety, per the independent referee correction.

## 6. The two-tag deleted-Tychonoff-plank counterexample

**KNOWN ingredients:** deleted Tychonoff plank = the standard locally compact Hausdorff nonnormal space; Arrieta (2024) explicitly cites the broader **simple-extension** tradition due to Bernhard Banaschewski. Exact references:

- B. Banaschewski, *Extensions of Topological Spaces*, **Canadian Mathematical Bulletin** 7(1) (1964), 1–22, https://geodesic.mathdoc.fr/articles/10.4153/CMB-1964-001-5/ .
- B. Banaschewski, *Singly Generated Frame Extensions*, **Journal of Pure and Applied Algebra** 83(1) (1992), 1–21, DOI 10.1016/0022-4049(92)90101-K, https://www.sciencedirect.com/science/article/pii/002240499290101K . Abstract mentions strong Hausdorffness and singly generated frame extensions.
- Arrieta (2024), Introduction and §4, builds non-Hausdorff/extension-related counterexamples for fitted-diagonal properties, drawing on this tradition, but **not the same two-tag nonnormality construction in the checked pages**.
- Standard plank source: e.g. the answer by Andreas Blass at https://mathoverflow.net/questions/53300/locally-compact-hausdorff-space-that-is-not-normal .

**NOT LOCATED:** an exact published **two-tag construction** from an arbitrary pair of closed nonnormally separable sets with the property I=U⊊F, or the stronger compact-open failure of completely-below interpolation. This is **not** a priority verdict. Search both topological extensions/gluing and C*-algebra/Glimm-space literature; relevant construction could have another name.

**Important novelty limit:** arbitrary regular non-functionally-Hausdorff spaces already show I=U=Δ⊊F for arbitrary locales; the distinctive result is failure **within continuous frames**, where regularity would force complete regularity.

**19 October provenance addendum (independent literature note supplied by researcher).** The original two-tag X_old is exactly the adjunction/pushout T∪_A C_+(A)∪_B C_+(B), where C_+(A)=A⊔{p_A} is the open-apex **non-Hausdorff cone** with opens ∅ and U∪{p_A} (U open in A). Careful: references such as J. P. May's *Finite Spaces and Larger Contexts*, §3.4, use the order-dual **closed-apex convention**. This is meaningful established construction background, **not evidence that the specific A/B nonnormality separation obstruction was previously proved**. The sharper T1 cofinite-cloud X_new is the parallel pushout with C_ω(A)=A⊔S_A (one discrete sequence converging to every a∈A); there is a canonical **open, surjective, nonclosed quotient** X_new→X_old collapsing the entire cloud S_A to p_A, similarly B. Detailed proof in [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md), §5½. In particular the literature's cone contractibility statements do not transfer: C_ω({a}) is a convergent sequence ω+1, not contractible.

## 7. One early-October 2026 near-name collision:## 6a. A sharper T1 / subfit / algebraic counterexample (19 October 2026)

**NEW WORKING CONSTRUCTION; NOT PRIORITY-CHECKED.** A replacement of the generic tags by two countably infinite discrete sets with cofinite-filter convergence to **every point** of the respective closed sets A,B gives a T1, strongly locally compact, sober X. T1 ⇒ O(X) subfit; if T has a compact-open basis, X also does, so O(X) is **algebraic**. It satisfies I=U⊊F, with far but not completely separated **compact open** witnesses; see [A-subfit-continuous-counterexample.md](A-subfit-continuous-counterexample.md). The deleted Tychonoff plank qualifies for T.

This settles negatively the further question whether *subfitness* restores I=U⇒U=F. The construction was derived in our own research discussion and has **not** undergone an external audit or historical priority check. Search terms: cofinite filter extensions, multi-limit convergent sequences, T1 non-Hausdorff spaces, nonnormal quotient spaces, primal/sober extensions.

 R1-Urysohn

S. Jafari, *On R1-Urysohn Spaces*, unrefereed preprint, posted 2 October 2026, https://www.preprints.org/manuscript/202610.0121 . It introduces a condition involving distinct singleton closures and **closures of certain disjoint neighborhoods**. Based on its published abstract, this is **not definitionally our I=U**, which only requires that any points separated by disjoint opens have *some neighborhoods with disjoint closures*. Do not equate them without a theorem. Historical R1/preregularity is weaker and also not definitionally our equality.

## 7b. Properness and effectiveness: an intrinsic computation (19 October 2026)

**Point-free result, all locales:** I∘I⊆U. Expanding a*∨b*=1 in the middle coordinate of a composable pair of I-arrows annihilates the two disjointness rectangles; hence I=U makes I an **internal equivalence relation** for all locales, not only continuous ones.

**Exact formula:** for I=C(d_I), the saturation operator is

    r_I(u)=(p_2)_*p_1^*(u)
          =∨{v∈L:1⊠v≤(u⊠1)∨d_I}.

It is the largest I-saturated open below u when I is an equivalence relation. Manuell (2023), Remark 3.8, establishes the proper quotient construction.

**Working continuous-frame effectiveness argument:** for strongly locally compact sober X and a **closed internal equivalence** E⊆X² with proper locale projections, each E-class is compact and E-saturations of closed sets are closed. The key specialization observation: closed reflexive E contains all specialization comparisons; ↑x is compact saturated and E[x]=p_1(p_2^-1(↑x)), while E[H]=↓E[H]. The non-Hausdorff characterization of properness controls compact saturated inverse images and downward closures of closed-set images. Hence the ordinary quotient X/E is perfect and Hausdorff, is also locally compact, and because it is sober it represents the localic coequalizer; E is its **kernel pair**. When E=I, the quotient is precisely the completely regular reflection, and I=U=F.

**Scope caution:** Exact correspondence between localic properness and the non-Hausdorff topological characterization should be verified against Johnstone/Vermeulen in the required sober scope; this is currently a working proof, **not externally refereed**. In arbitrary pointless locales, Vermeulen (1994) Corollary 5.17 **already proves effectiveness** for closed proper equivalence relations; Corollary 5.14 is a separate weak-fitting sufficient condition. Corollary 5.17 does establish unrestricted effectiveness for closed proper equivalence relations. Complete argument: [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md).

Sources: [Manuell 2023](https://link.springer.com/article/10.1007/s10485-023-09736-x), [Goubault-Larrecq on non-Hausdorff proper maps](https://topology.lmf.cnrs.fr/proper-maps-quasi-adjoints-and-the-smyth-hyperspace/), [Karazeris–Tsamis 2021](https://cahierstgdc.com/wp-content/uploads/2021/07/Karazeris-Tsamis_LXII-3.pdf).

## 8. Tentative claim-to-source ledger (non-exhaustive)## 7a. Proper equivalence relations and separation quotients

**KNOWN categorical machinery:** J. J. C. Vermeulen, *Proper Maps of Locales*, **JPAA** 92 (1994), 79–107 (DOI 10.1016/0022-4049(94)90047-7); Graham Manuell, *Presenting Quotient Locales*, **Applied Categorical Structures** 31 (2023), article 28, §2 and §3 (especially Remark 3.8), https://link.springer.com/article/10.1007/s10485-023-09736-x . Proper f means right adjoint f_* preserves **directed joins** and satisfies the **closed co-Frobenius law** f_*(u∨f^*v)=f_*u∨v. It is stronger than semi-proper (=Scott continuity alone), sometimes called perfect in the localic literature.

**FORMAL CONSEQUENCE, new synthesis for this project:** if a **closed internal equivalence** E↪X² has proper projections p_i, its coequalizer q:X→Q is proper (Manuell) and its diagonal Δ_Q is closed: the closed image (q×q)(E) equals Δ_Q because of reflexivity, coequalization and surjectivity. If X is continuous, the quotient Q is continuous by a short right-adjoint/way-below calculation. Under ZFC Q is thus completely regular. **Do not assume E is its kernel pair in arbitrary locales**; full equality E=F outside the spatial case needs separate effectivity verification. A separate purely topological theorem: for *any* closed equivalence relation E with perfect projections, X/E is Hausdorff; in strongly locally compact sober X with **E=I transitive**, this yields I=U=F as closed localic relations. Detailed proofs and caveat: [A-proper-inseparability-relations.md](A-proper-inseparability-relations.md).

**Priority:** quotient/proper descent techniques are existing literature; the special Project A formulation is not asserted new.



| Project A result | Closest identified source(s) | Present classification |
|---|---|---|
| I=cl Δ | Isbell strong Hausdorff; Arrieta 2024 §2.4 | **KNOWN** |
| fitted Δ and Fsep | Arrieta–Picado–Pultr 2022; Arrieta 2024 | **KNOWN** |
| points of D equal Cm | Cameron–Kumar 2026 Def 3.1 (Cm); fitting literature (D) | **KNOWN Cm graph; candidate new realization** |
| graph diamond and T1 test | Cameron–Kumar 2026 Thm 3.2 | **KNOWN** |
| arbitrary-locale U as closed sublocale | Arrieta 2024 Def 4.6 gives U=total extreme | **NOT LOCATED in full relation form** |
| anti-Urysohn ⇔ U=whole product | Arrieta 2024 Def 4.6 | **FORMAL CONSEQUENCE** |
| F=kernel pair of real-map reflection | Picado–Pultr 2021 VI; cozero bases | **FORMAL CONSEQUENCE** |
| exact frame equality tests | Standard coproduct and completely-below tools | **NOT LOCATED as stated** |
| I=U ⇔ conormal compact opens | Cornish 1972; Georgescu 2021 | **FORMAL CONNECTION** |
| Spec R ⇔ mp-ring | Cornish/Georgescu; mp-ring literature | **FORMAL CONNECTION** |
| compact closed quotient implication | classical compact decomposition theory | **KNOWN background** |
| kω/σ-compact positive implication | standard kω normality; close MSE proof | **KNOWN mechanism / careful adaptation** |
| paracompact positive implication | classical Dugundji decomposition | **KNOWN mechanism / scope extension to verify** |
| continuous-frame two-tag plank counterexample | plank + Banaschewski extension literature | **NOT LOCATED precisely** |
| pointless finite-poset×Boolean example | standard locales/coproduct | **NOT LOCATED precisely; likely easy construction** |

## 9. Next targeted literature steps, in priority order

1. **Read the original 2022 Arrieta–Picado–Pultr paper closely**, especially the parallel-map conditions; match these algebraically to ours for I, U, D.
2. Search more exhaustively for **closed sublocalic Urysohn relations** and name conventions, especially 2024 Arrieta Def 4.6 and surrounding references. Existing “anti-Urysohn” does **not** settle full relation equality criteria.
3. Compare **Banaschewski 1964/1992 simple extensions** with the two-tag example; abstracts alone do not establish priority.
4. Check original **Cornish 1972** and Georgescu's propositions for exact duality and any compact-open/frame formulation.
5. Get precise source references for **kω normality**, **paracompact decomposition** and the non-Hausdorff closed-equivalence quotient lemma, treating standard folklore carefully.
6. Assess the newly found **D–Cm** connection: check whether fitting-of-diagonal literature explicitly recovers the closure-meeting relation on points. Even if not stated, this is an elementary characterization, so do not overclaim originality.

This ledger is a **living research document**. Additional conclusions should be appended only with exact source links and a distinction between source-stated facts and our deductions.
