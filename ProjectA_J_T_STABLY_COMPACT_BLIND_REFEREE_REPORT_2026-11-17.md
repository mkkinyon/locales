# Independent blind referee report: \(\mathcal J\), \(\mathcal T\), and comparability graphs

**17 November 2026**  
**Material reviewed:** `01_REFEREE_PROMPT.md` and `02_MATHEMATICAL_PACKET.md` in `ProjectA_J_T_STABLY_COMPACT_BLIND_AUDIT_2026-11-17.zip`.  
**Review conditions:** I read the prompt and mathematical packet without consulting earlier Project A audits, notes, or referee reports. I checked the cited literature separately and performed independent mathematical and finite-poset checks.

## 1. Executive verdict

**Overall: favorable, with modest clarifications recommended.** I found no false mathematical assertion or substantive gap in the claimed stably compact theorem, the graph bounds, the distance-four equivalence, or the examples. This is a positive verdict reached after adversarial checks, not a certification based on the packet's own proofs. The localic argument uses nontrivial results whose hypotheses and nomenclature deserve more explicit citation. The graph-only criterion (8) is correct, but its proof in the packet is too compressed at exactly the decisive point; I give a self-contained proof below.

| Claim | Verdict | Comments |
|---|---|---|
| Universal identities (2), \(\mathcal T=\mathbf T(\mathcal J)\) | **Correct** | Follow directly from monotonicity and idempotence of the two hulls. |
| Six perfect/spatial/stably compact sublocales (§2) | **Correct** | The chain through compact fitting, Scott-open filters, perfect nuclei, and spatiality is valid in classical locale theory. |
| Exact point formulas (4), including the join | **Correct; expand one justification** | Patch closedness and the sober-subspace/spatial-sublocale correspondence secure the finite union. |
| Spectral/coherent inheritance and duality (§2) | **Correct** | Clarify the two uses of “coherent”; duality compares different locales. |
| \(\mathcal J=G^2\), \(G^3\subseteq\mathcal T\subseteq G^4\) (5) | **Correct** | Valid for infinite specialization posets. |
| Diameter-two equivalence (6) | **Correct** | No finiteness or bounded-component-size assumption. |
| Alternating geodesics and graph-only test (7)–(8) | **Correct; replace the abbreviated converse** | A short nonnesting lemma proves (8) without finiteness. |
| Fence and eight-point examples (§3) | **Correct** | The eight-point example genuinely has distance four. |
| Doubled-origin circle (§4) | **Correct** | Gives the asserted compact, locally compact, sober, \(T_1\), non-stably-compact counterexample. |

I recommend **retaining the theorem** with a few additional sentences and precise citations, rather than downgrading it to a conjecture. I did not find an unresolved correctness issue in the present packet.

## 2. Localic foundations (§§1–2)

### 2.1. The product, diagonal, compactness, and perfectness

The product convention in §1 is correct: \(\mathcal O(X\times_{\mathrm{Loc}}X)\) is the **frame coproduct** \(\mathcal O(X)\oplus\mathcal O(X)\), not the direct product. The diagonal is a sublocale because its inverse-image homomorphism sends a basic rectangle to \(a\wedge b\), and is surjective. As a locale the diagonal is isomorphic to \(X\), so it is compact when \(X\) is compact.

Classically, locally compact locales are spatial and localic products with a locally compact factor agree with the corresponding ordinary topological products. In particular, the square of a stably compact locale is spatial, with underlying point space \(P\times P\), and is again stably compact. This is essential; the argument would not be legitimate for arbitrary spatial locales.

The closure \(\mathcal I=\operatorname{cl}\Delta\) is compact because it is a closed sublocale of compact \(Y\). The nontrivial fitting step is supported by Jakl–Suárez, **Theorem 6.11**, whose proof explicitly establishes that the fitting of a compact sublocale is compact. It follows that \(\mathcal D=\operatorname{fit}\Delta\) and \(\mathcal V=\operatorname{fit}\mathcal I\) are compact fitted sublocales.

Escardó's *regular-locally-compact coreflection*, **Lemma 2.1 and Corollary 2.2**, identify compact fitted sublocales with Scott-open neighborhood filters; **Lemma 5.1** proves that the associated fitted nucleus is perfect when the ambient locale is stably locally compact. Thus the perfectness claims for \(\mathcal D\) and \(\mathcal V\) are justified. The nuclei of \(\mathcal I\) and \(\mathcal W\) are closed nuclei \(u\mapsto a\vee u\), which preserve all joins.

The perfect nuclei form a **subframe** of the frame of nuclei (Escardó, *regular-locally-compact coreflection*, §2; *Properly injective spaces*, Lemma 3.1.8). Because the nucleus order is the reverse of sublocale inclusion, the finite **sublocale join** \(\mathcal J\) corresponds to a meet of perfect nuclei, and the finite **sublocale meet** \(\mathcal T\) corresponds to their join. Both operations preserve perfectness. This order reversal is handled correctly in the packet.

Finally, *Properly injective spaces*, **Theorem 3.1.4**, says that a perfect (there called *finitary*) sublocale of a spatial locale is spatial; its proof invokes Zorn's lemma. **Theorem 3.1.7** and **Remark 3.1.5** provide stable local compactness, spectrality, and compactness inheritance. Therefore all six proposed sublocales really are spatial and stably compact, and spectral when the ambient square is spectral. There is no unnoticed nonspatial residue here.

**Recommended clarification:** The word *coherent* appears in two related but different senses. Define *stably compact* topologically as sober, compact, locally compact, with finite intersections of compact **saturated** sets compact; reserve *spectral/coherent locale* for the compact-open-basis condition. State explicitly that the latter stronger hypothesis is used only for the final spectral inheritance assertion.

### 2.2. The patch-order calculation

Let \(Q=P^2\) with its specialization product order and compact Hausdorff patch topology. The specialization order is a closed subset of \(Q_{\mathrm{patch}}^2\); the topological product and patch product agree in the compact-pospace representation. The diagonal \(\delta\subseteq Q\) is patch closed.

More generally, if \(K\subseteq Q\) is patch closed, it is patch compact. The set

\[
\downarrow K=\{q:\exists k\in K,\ q\le k\}
\]

is the projection of a closed subset of the compact Hausdorff space \(Q_{\mathrm{patch}}\times K\). Consequently it is patch closed. It is also lower, so it is closed in the original upper topology by the compact-pospace representation. Conversely every ordinary closed set is lower for specialization, so every ordinary closed superset of \(K\) contains \(\downarrow K\). Hence

\[
\operatorname{cl}_{Q}(K)=\downarrow K.
\]

Likewise \(\uparrow K\) is patch closed, and the same holds after any finite alternation of upward and downward closure. This establishes the point-set closure calculations used in (4). A useful precise reference is Jung–Kegelmann–Moshier, **Theorem 2.5**, for the compact-pospace representation.

### 2.3. Fitting and the potentially dangerous finite join

For a **spatial** sublocale \(S\) of a spatial locale, its inclusion into an open sublocale \(\mathfrak o(U)\) is equivalent to inclusion of its point support in \(U\). The point set of \(\operatorname{fit}S\) is therefore the intersection of all open neighborhoods of the support, namely its specialization-upward saturation. Explicitly, for any subset \(A\) of a space,

\[
\bigcap\{U:U\text{ open},\ A\subseteq U\}=\uparrow A.
\]

The application is legitimate because \(\Delta\) and \(\mathcal I\) have already been shown spatial. Similarly, closed hulls of spatial sublocales correspond to ordinary closures of their supports. Thus the four individual supports \(\downarrow\delta\), \(\uparrow\delta\), \(\uparrow\downarrow\delta\), and \(\downarrow\uparrow\delta\) are correct.

The **join** \(\mathcal J=\mathcal I\vee\mathcal D\) merits an explicit argument. Put \(A=\operatorname{pt}(\mathcal I)=\downarrow\delta\) and \(B=\operatorname{pt}(\mathcal D)=\uparrow\delta\). Each is patch closed; so \(A\cup B\) is patch closed, and hence its induced original-topology subspace is stably compact and sober. By Escardó, *Properly injective spaces*, **Lemma 3.1.2**, sober subspaces of a sober space correspond **inclusion-preservingly** to spatial sublocales. Let \(K\) denote the sublocale associated with \(A\cup B\). It contains both \(\mathcal I\) and \(\mathcal D\), hence contains their join. Conversely the point set of their join contains \(A\cup B\); since the join is spatial, Lemma 3.1.2 again implies \(K\le\mathcal J\). Therefore

\[
\operatorname{pt}(\mathcal J)=A\cup B
\]

and no extra point or nonspatial structure has been introduced. This supplies the exact missing bridge between *patch-closed union* and *sublocale join*. It is consistent with the packet's proof, but worth stating rather than leaving implicit.

For a sublocale meet, points are exactly the intersection of the two point supports. The perfectness already established for \(\mathcal T\) ensures spatiality, so its point-support formula identifies the sublocale uniquely. Thus **every line of (4) holds as an equality of spatial sublocales** under the stated hypotheses.

### 2.4. Universal hull and duality

Equation (2) is immediate from \(\Delta\le\mathcal I,\mathcal D\). In fact \(\mathcal I=\operatorname{cl}\Delta\le\operatorname{cl}\mathcal D=\mathcal W\), so \(\operatorname{cl}(\mathcal I\vee\mathcal D)=\mathcal W\). Dually, \(\mathcal D=\operatorname{fit}\Delta\le\operatorname{fit}\mathcal I=\mathcal V\), so \(\operatorname{fit}(\mathcal I\vee\mathcal D)=\mathcal V\). The identity \(\mathbf T(\mathcal J)=\mathcal T\) follows. The use of *hull* is justified: \(\mathbf T\) is extensive, monotone, and idempotent.

The de Groot dual reverses the specialization order while retaining the patch space, so the point formulas exchange \(\mathcal I\) with \(\mathcal D\), and \(\mathcal V\) with \(\mathcal W\). The symmetric descriptions of \(\mathcal J\) and \(\mathcal T\) are retained. The caveat that the compared sublocales lie in **different** localic squares is both correct and important.

## 3. Graph-theoretic claims (§3)

### 3.1. Bounds and fixed points

Write \(x\sim y\) for two distinct comparable elements, with each vertex also connected to itself in the reflexive powers. For any poset, the relation “common upper bound or common lower bound” is exactly \(G^2\). Every comparability walk of length two either has two arrows in the same direction, in which case transitivity shortens it, or forms a peak or valley with the middle element as common upper or lower bound. The converse is immediate from the two-edge witness. Thus \(\mathcal J=G^2\) follows from (4).

The support of \(\mathcal V=\uparrow\downarrow\delta\) is described by a four-step walk of the form

\[
x\ge a\le z\ge b\le y,
\]

and \(\mathcal W=\downarrow\uparrow\delta\) by

\[
x\le a\ge z\le b\ge y.
\]

Thus \(\mathcal T\subseteq G^4\). Because \(\mathcal J\subseteq\mathcal T\), distances at most two are automatically included. At distance three, a geodesic cannot contain two consecutive arrows in the same direction (that would shorten it). It must alternate. Either alternating three-step orientation embeds into **both** four-step patterns by allowing a repeated endpoint or intermediate vertex. Hence \(G^3\subseteq\mathcal T\), proving (5).

For (6), if all components have diameter at most two, \(G^2\) contains all pairs within each component and so includes \(\mathcal T\). If some component has a pair at distance three or more, a geodesic between two suitably chosen vertices yields a pair at **exactly** distance three, hence in \(\mathcal T\setminus\mathcal J\). If a component has unbounded diameter, it still has such a pair; disconnected pairs at distance \(\infty\) play no role. This is correct without finiteness assumptions.

### 3.2. A complete proof of the distance-four formula (8)

I recommend replacing the paragraph following (8) with the following explicit lemma. It is simpler than a general nonnesting argument and avoids any reliance on finite-poset enumeration.

Fix \(d(x,y)=4\). Define \(A=A_{xy}\), \(B=B_{xy}\), and \(M(u)\) as in (7). Each \(u\in A\) belongs to a length-four geodesic from \(x\) to \(y\), so **\(M(u)\ne\varnothing\)**. All four-edge geodesics alternate orientation, since any two successive comparisons in the same direction would give a transitive shortcut. Further:

1. If \(u<x\), then every \(z\in M(u)\) satisfies \(u<z\); otherwise \(z<u<x\) would make \(x,z\) adjacent, contradicting \(d(x,z)=2\). If \(x<u\), then every \(z\in M(u)\) satisfies \(z<u\), by the dual argument.

2. Suppose \(u,r\in A\) are comparable and lie on the **same** side of \(x\). If \(u<r<x\), take \(z\in M(r)\). By (1), \(r<z\), so \(u<r<z\), and hence \(z\in M(u)\). Thus \(M(r)\subseteq M(u)\). If \(x<u<r\), take \(z\in M(u)\). By (1), \(z<u\), so \(z<u<r\), and hence \(z\in M(r)\). Thus \(M(u)\subseteq M(r)\). Interchanging \(u,r\) handles the remaining orders. **Comparable same-side vertices therefore have nested \(M\)-sets.**

3. Suppose \(u<x<r\), so \(u,r\) lie on **opposite** sides of \(x\). Then \(u<r\), hence \(u\sim r\). In fact **\(M(u)\cap M(r)=\varnothing\)**. For if \(z\) belonged to both, (1) would give \(u<z<r\). Extend the geodesic prefix \(x-u-z\) to a geodesic \(x-u-z-v-y\). Its alternating orientation is \(x>u<z>v<y\), so \(v<z<r\). But then \(x<r>v<y\) would be a comparability path of length three, contradicting \(d(x,y)=4\). As the two \(M\)-sets are nonempty, disjointness makes them nonnested.

Thus a comparable pair \(u,r\in A\) with nonnested \(M\)-sets must lie on opposite sides of \(x\), and conversely any opposite-side pair satisfies the graph condition. Such opposite-side first steps exist precisely when there are two length-four geodesics beginning in opposite specialization directions, which is precisely \((x,y)\in\mathcal V\cap\mathcal W\). This proves (8) **for arbitrary posets**, finite or infinite.

The explicit disjointness claim in (3) is a useful strengthening of the argument in the packet. It also makes clear why the test depends only on the **undirected** comparability graph.

### 3.3. Independent finite checks

I separately implemented the formulas for common bounds, the two four-step witness relations, graph distance, and criterion (8). I exhausted all posets admitting a fixed linear-extension labeling for \(2\le n\le6\) (every isomorphism class has such a labeling): respectively **2, 7, 40, 357, 4,824** transitively closed order matrices. Across the six-element cases there were **1,616 ordered distance-four pairs**; no failure of (5) or (8) appeared. I also performed random trials on orders of up to ten elements; no failure appeared. The proof in §3.2 is the reason to accept the infinite statement; the finite checks are independent safeguards against missed configurations.

### 3.4. Examples

- The four-point fence \(0<1>2<3\) has endpoint distance three. Hence \((0,3)\in\mathcal T\setminus\mathcal J\).
- A five-point alternating fence with a unique endpoint geodesic of length four has only one starting orientation, so its endpoints are outside \(\mathcal T\).
- In the eight-point example of §3, the two displayed paths are genuine geodesics: \(x>u<z>v<y\) and \(x<r>t<s>y\). No transitive consequence of the generating order relations shortens the distance between \(x\) and \(y\). Here \(A_{xy}=\{u,r\}\), \(B_{xy}=\{z,t\}\), \(M(u)=\{z\}\), and \(M(r)=\{t\}\), so (8) also recognizes the pair.

## 4. The non-stably-compact example (§4)

The doubled-origin circle is correctly described. The quotient of the disjoint union of two compact circles is compact. Each individual quotient point is closed because its inverse-image equivalence class is closed in the disjoint union, so the quotient is \(T_1\). Each point has a neighborhood homeomorphic to an open arc, including at each of the two origins (take the arc containing just that copy of the origin); thus the space is locally Hausdorff and locally compact.

It is also **sober**. More generally, in a locally Hausdorff \(T_1\) space, a nonempty irreducible closed set intersects some Hausdorff open neighborhood in a nonempty irreducible closed subset, necessarily a singleton; this nonempty relatively open singleton is dense in the original irreducible closed set, so \(T_1\) forces the latter to be that singleton. Thus each irreducible closed set has a unique generic point.

The two origins are not Hausdorff separable; hence the space is not Hausdorff. A stably compact \(T_1\) space must be Hausdorff: its specialization order is equality, so its original topology is the upper topology for the equality order on its compact Hausdorff patch. Therefore the doubled-origin circle is **not stably compact**.

Its specialization order is equality, and \(G^2=\delta\). Yet every neighborhood of \(o_0\) intersects every neighborhood of \(o_1\), so every basic neighborhood of \((o_0,o_1)\) in the ordinary product meets the diagonal. Hence \((o_0,o_1)\in\operatorname{pt}(\operatorname{cl}\Delta)\setminus G^2\), as asserted. Because this particular space is locally compact and sober, its ordinary product is indeed the localic product. The example genuinely defeats the graph formula under the weaker hypotheses.

## 5. Presentation and source recommendations

1. **Add Escardó, *Properly injective spaces*, Lemma 3.1.2, to the proof of the join formula.** This is the cleanest way to show that a patch-closed union gives exactly the *sublocale* join, not merely the expected union of points.
2. **Make “classical” explicit in the theorem statement**, not only in §1. Spatiality of locally compact locales and Escardó's Theorem 3.1.4 use choice. The proof is not intended to be constructive or valid internally in an arbitrary topos.
3. **Correctly distinguish `perfect` from related terminology.** In Escardó's *Properly injective spaces*, “finitary nucleus” means one preserving directed joins; in *regular-locally-compact coreflection*, the author calls it “perfect.” These usages match here. “Proper” is not uniformly synonymous across the literature.
4. **Cite the exact source bridge:** Jakl–Suárez, Theorem 6.11 (the compact fitting fact is written explicitly in its proof); Escardó *regular-locally-compact coreflection*, Lemma 2.1/Corollary 2.2 and Lemma 5.1; Escardó *Properly injective spaces*, Lemmas 3.1.2, 3.1.8, Theorems 3.1.4 and 3.1.7, and Remark 3.1.5; Jung–Kegelmann–Moshier, Theorem 2.5.
5. **Replace the last paragraph of the proof of (8)** with the three-part lemma in §3.2 above. In particular, state that opposite-side \(M\)-sets are *disjoint*, not merely nonnested, and explain the specific length-three shortcut \(x<r>v<y\).
6. **Spell out the spectral qualification** as “if \(X\) is spectral (equivalently its frame is coherent)”; distinguish this from “coherence” in the stably compact space definition.
7. **For the doubled-origin example**, one sentence explaining why the quotient is locally Hausdorff and sober removes possible doubts about a non-Hausdorff example meeting all the weaker hypotheses.
8. The cited Jung–Kegelmann–Moshier URL leads to the *full MFPS 2001 proceedings*, not a separate paper, although the paper is present there. A page range or a direct standalone citation would help a reader.

## 6. Further mathematical observations

These are suggestions, not corrections to the packet.

**(a) Every finite graph power is patch closed.** The undirected comparability relation \(G=\le\,\cup\,\ge\) is patch closed in \(P^2\). For each fixed finite \(k\), \(G^k\) is the projection of a patch-closed subset of the compact Hausdorff space \(P^{k+1}\), so is patch closed. Consequently all finite graph powers, not merely \(G^2\), determine perfect spatial sublocales of the localic square in the stably compact setting. This gives a canonical localic home for the entire finite-power filtration.

**(b) A stronger orientation-free conclusion.** The pair-supports of both \(\mathcal J\) and \(\mathcal T\) depend only on the abstract undirected comparability graph, not on a selected transitive orientation. For \(\mathcal T\), this follows by partitioning pairs into distances \(\le3\), \(4\), and \(\ge5\), and using (8) in the middle case. This is a statement about point supports; different orientations generally give different topologies and hence different ambient localic squares.

**(c) The sharpness of the sandwich can be stated more visibly.** The four-point fence proves that the lower bound \(\mathcal J\subseteq\mathcal T\) can be strict already at distance three; the five-point fence gives a distance-four pair outside \(\mathcal T\), while the eight-point example gives one inside. These examples exhibit the full combinatorial behavior claimed in (5).

**(d) A plausible next question** is to identify useful hypotheses strictly weaker than stable compactness under which the relevant sublocales remain spatial and the closure/fitting formulas remain order-theoretic. The doubled-origin example shows that compactness, sobriety, local compactness, and \(T_1\) *together* do not suffice. No extension beyond the stated stably compact framework has been established in this review.

## 7. Final disposition

**Safe to retain:** (1)–(8), including the actual-sublocale interpretation of (4)–(6), the de Groot duality statement, spectral inheritance, and the examples in §§3–4, under the explicitly classical and stably compact hypotheses.

**Needs editorial repair, not mathematical retraction:** the justification of the finite join's exact support; the final nonnesting/converse paragraph in the proof of (8); the distinction between topological coherence and a coherent/spectral frame; the statement of choice dependence and exact literature pointers.

**Unresolved correctness questions within the packet:** **none found**. The possibility of weakening stable compactness and the broader significance of the finite graph-power filtration remain open directions rather than gaps in the submitted argument.

### Literature actually checked

- Martín H. Escardó, *Properly injective spaces and function spaces*, [author PDF](https://martinescardo.github.io/papers/injective.pdf), specifically §3.1 and Lemmas 3.1.2, 3.1.8, Theorems 3.1.4, 3.1.7.
- Martín H. Escardó, *The regular-locally-compact coreflection of a stably locally compact locale*, [author PDF](https://www.cs.bham.ac.uk/~mhe/papers/patch-full.pdf), specifically §2 and Lemma 5.1.
- Tomáš Jakl and Anna Laura Suárez, *Canonical extensions via fitted sublocales*, *Applied Categorical Structures* **33** (2025), article 10, [journal version](https://link.springer.com/article/10.1007/s10485-025-09802-6), especially Proposition 6.9 and Theorem 6.11.
- Achim Jung, Mathias Kegelmann, and M. Andrew Moshier, *Stably compact spaces and closed relations*, MFPS 2001 preliminary proceedings, [proceedings PDF](https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf), especially §2.1, Theorem 2.5. The target article begins at PDF page 143 (printed page 133).
