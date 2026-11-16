# Independent blind referee report

**Manuscript:** *Unbounded integral differentials from clean cover insertions*  
**Date:** 16 November 2026  
**Material reviewed:** the blind instructions and the accompanying self-contained mathematical packet only. No internal audit or earlier working notes were consulted.

## Verdict

**The principal theorems are correct, subject to one definite error in the numerical sanity-check table and one unsupported historical/example claim.** I found no fatal mathematical error in the nine-vertex seed, the capped-path induction, the two maximal-simplex certificates, or the relative construction. In particular, the packet establishes nonzero **integral** absolute differentials (d_k) for every (k\ge 3), and nonzero **integral** relative differentials (d_k) for every (k\ge4). The claimed example sizes are consistent.

The error is in Section 6: the **13-vertex, five-cover relative (d_4) example has a barcode in homological degree 4, not degree 3**. Its interval is indeed \([1,5)\). This is forced by the bidegree in (5.2) and independently confirmed by boundary-matrix reduction.

The mention in Theorem 5.1 of an *earlier ten-vertex/four-cover relative (d_3)* example cannot be audited from this packet: that poset and its witness are not supplied. It does not enter the proof of relative unboundedness. I recommend supplying an explicit reference or appendix, or removing the sentence from this self-contained presentation.

The main recommendation is **mathematical acceptance after minor corrections and improved exposition**, not a claim of novelty or publication priority.

## 1. The filtered-poset setup

**Verified.** Deleting any subset of covers of a poset leaves a transitive strict relation. Indeed, if (a<b<c) survive, then (a<c) cannot have been removed, because it was not a cover in the original poset. Reinstating any subset of the deleted covers therefore gives a partial order. This proves the asserted Boolean independence without additional structural assumptions.

The weight of a simplex is monotone under passage to faces, so the (F_p) are simplicial subcomplexes. A marked path consisting of all (m) covers from a minimal vertex to a maximal vertex determines **exactly one** weight-(m) simplex, namely the simplex of the path vertices. Any extra vertex in a chain containing the whole path would lie below its initial vertex, above its terminal vertex, or strictly between two successive covered vertices, all impossible. Consequently the unique weight-(m) simplex is (m)-dimensional and has no coface.

I checked the deletion property directly for every subset of the marks in the seed (8 subsets), the capped (d_4) example (16 subsets), and the relative (d_4) and (d_5) examples (32 and 64 subsets respectively). All tests passed. These exhaustive small checks corroborate, but are not needed for, the general argument above.

## 2. The spectral-sequence certificates

**Both Lemmas 2.1 and 2.2 are correct.** The most delicate point is the claim that a zero higher differential forces the indicated lower-filtration filling. The claim is valid at the specified page; the packet could make it more explicit. Here is a concise alternative proof that simultaneously establishes nonvanishing over ℚ and infinite order.

### 2.1 Absolute certificate

Because \(Q=F_m\) contains exactly one simplex outside \(F_{m-1}\), namely an (m)-simplex \(\tau\), the relative chain complex \(C_*(Q,F_{m-1};\mathbb Z)\) is concentrated in degree (m) and has group \(\mathbb Z\) there. Thus

\[
H_m(Q,F_{m-1};\mathbb Z)\cong\mathbb Z.
\]

For (m\ge3) (indeed for (m\ge2)), contractibility of \(\Delta Q\) gives an isomorphism via the connecting map

\[
\delta:H_m(Q,F_{m-1};\mathbb Z)
\xrightarrow{\ \cong\ }H_{m-1}(F_{m-1};\mathbb Z).
\]

The chain (C) represents the generator associated with \(\tau\), so its image is \([\partial C]\). This image is nonzero and has infinite order. Since \(\partial C\in C_{m-1}(F_0)\), that class originates in filtration zero.

The source in \(E^m_{m,0}\) cannot be hit from higher filtration, and the given lift has zero differentials on pages (1,\ldots,m-1). The filtration-zero target at page (m) records the image of (H_{m-1}(F_0)) in (H_{m-1}(F_{m-1})): lower-page incoming boundaries account precisely for classes already killed in (F_{m-1}). The nonzero image \([\partial C]\) therefore gives a nonzero (d_m), with infinite-order target.

Equivalently, directly from the filtered-chain description of (E^m_{0,m-1}), vanishing would give \(B\in C_m(F_{m-1})\) with \(\partial B=\partial C\), contradicting the nonzero coefficient of \(\tau\) in the resulting absolute cycle. So the original proof is sound.

### 2.2 Relative certificate

In the relative case apply the long exact sequence of the triple

\[
F_0\subseteq F_{m-1}\subseteq Q.
\]

Since (Q) and (F_0) are contractible, \(H_j(Q,F_0;\mathbb Z)=0\) for all (j), and the connecting map is an isomorphism

\[
H_m(Q,F_{m-1};\mathbb Z)\cong\mathbb Z
\xrightarrow{\ \cong\ }
H_{m-1}(F_{m-1},F_0;\mathbb Z).
\]

Its generator maps to \([\partial C]\), now considered modulo (F_0), and hence has infinite order. The lift \(C\) has boundary in (F_1), so its top-filtration class survives pages (1,\ldots,m-2). The filtration-one class of its boundary cannot have been killed before page (m-1), because its image remains nonzero in \(H_{m-1}(F_{m-1},F_0)\). Therefore

\[
d_{m-1}:E^{m-1}_{m,0}\longrightarrow E^{m-1}_{1,m-2}
\]

is nonzero, again with an infinite-order target. The proof using an explicit (B) and (D_0) in the packet gives the same conclusion.

**Coefficient extension.** Both arguments remain valid over every nonzero commutative unital coefficient ring (R), because the final relative chain complex is simply (R) in degree (m), and (1_R\ne0\). This supports the last paragraph of Section 5. No universal-coefficient or torsion-free assumption is needed.

**Suggested edit:** Use the long-exact-sequence argument as the main justification for the certificates, retaining the coefficient-on-\(\tau\) proof as an elementary alternative. State expressly that, for this homological indexing, the target of (d_r) has total degree one less than the source.

## 3. Nine-vertex seed: exact audit

### 3.1 Hasse diagram and marked covers

The listed Hasse relations are consistent. After computing transitive closure and removing transitive edges, I recover exactly the listed covers. In particular

\[
a\prec d,\qquad d\prec f,\qquad f\prec i
\]

are all genuine covers; (a) is minimal and (i) maximal. The comparisons used in the eight simplices of (T) exist (notably (a<c) through (a<x<c)).

### 3.2 Boundary calculation

Expanding all eight oriented tetrahedra gives exactly (3.1). For clarity, the five terms containing (a) are

\[
a*t=[a,c,f]-[a,c,i]-[a,e,h]+[a,e,i]+[a,f,h],
\]

and the remaining terms are

\[
\begin{aligned}
w={}&-[b,c,f]+[b,c,i]+[b,d,h]-[b,d,i]-[b,f,h]\\
   &+[d,e,h]-[d,e,i].
\end{aligned}
\]

Hence \(\partial T=a*t+w\). Every one of these twelve triangles has weight zero. The boundary of the five-edge (1)-chain (t) vanishes term by term:

\[
\partial t=([f]-[c])-([i]-[c])-([h]-[e])+([i]-[e])+([h]-[f])=0.
\]

Both (a) and (x) lie below each vertex occurring in (t), with (a<x). Therefore (a*x*t) is a valid integral 3-chain and

\[
\partial(a*x*t)=x*t-a*t.
\]

It follows that

\[
z_3=\partial(T+a*x*t)=w+x*t.
\]

The resulting twelve triangles have weight zero and none contains (a). The coefficient of \([a,d,f,i]\) in (C_3) is (+1), and no other simplex has all three marked covers. **All sign and support checks pass over \(\mathbb Z\), not merely modulo two.**

### 3.3 Contractibility

In (M=\{a,b,c,d,e,f,x\}\), the strict lower interval of (e) consists of (x,a,d,b), whose order complex really is the path

\[
x-a-d-b.
\]

Because (e) is maximal in (M), its link in \(\Delta M\) is this contractible path. Deleting (e) therefore preserves homotopy type. The remaining poset has greatest element (f): even (x<f) holds, through (x<c<f). Thus \(\Delta M\) is contractible. Finally, both (h) and (i) lie above every vertex of (M), and (h\parallel i), so (X_3=M\oplus\{h,i\}) and \(\Delta X_3=\Delta M*S^0\) is contractible. **The base case is valid.**

## 4. Capped-path extension: exact audit

**The construction and all its invariants pass.** The most important points are the following.

1. **Partial order.** Adding (u,v) below all of (X) does not alter old comparabilities. Adding (u<y<q) for every (q\ne b) likewise creates no forbidden (y<b): such a forced comparison would require a vertex (q<b), whereas (b) is minimal. There is no relation between (y) and (v).

2. **Covers.** The old marked covers remain covers. Neither (u) nor (v) can lie between old vertices. The new (y) is below the lower endpoint of every old marked cover except those beginning at (b), where (y\parallel b); thus it cannot lie strictly between any marked pair. Finally, (u<b) remains a cover since (v\parallel u) and (y\parallel b). The marked path still starts at a minimal vertex and ends at the old maximal vertex.

3. **Correction chain.** Because (z) avoids (b), each old vertex in each simplex of (z) is above (y). Thus (u*y*z) is well defined. Its simplices have weight zero: the new marked relation is (u<b), and none of the other marked covers occurs in a simplex of (z). All of this is integral.

4. **Signs.** With \(\partial z=0\),

   \[
   \begin{aligned}
   \partial((u-v)*C)&=-(u-v)*z,\\
   \partial(u*y*z)&=(y-u)*z,
   \end{aligned}
   \]

   and so

   \[
   \partial\big((u-v)*C-u*y*z\big)=(v-y)*z.
   \]

   The last expression has weight zero and avoids the new initial vertex (u). The coefficient of the new path simplex is still (+1): it arises from (u*C), never from the correction (which avoids (b)).

5. **Contractibility.** Before adjoining (y), the order complex is \(S^0*\Delta X\), the suspension of a contractible complex. After adjoining (y), its link is precisely \(\{u\}*\Delta(X\setminus\{b\})\), a cone. Gluing the cone that is the closed star of (y) along its contractible link does not change homotopy type. The final complex is therefore contractible.

I also reconstructed the capped (r=4) and (r=5) posets computationally, checked their marked covers from their entire transitive closures, checked every simplex in (C^+), and verified the oriented identities coefficient by coefficient. All passed.

### Pre-cap variant

The intermediate poset \(U=\{u,v\}\oplus X\) is already contractible. Its chain \((u-v)*C\) has boundary \(-(u-v)*z\) of weight zero, since (z) avoids (b). Hence the pre-cap (3k-1) vertex absolute examples really do follow without requiring the (y)-vertex. This point is correct but deserves a separate two-sentence statement before the main corollary.

## 5. Relative construction

**Verified.** Writing \(S=(u-v)*C\), one obtains

\[
\partial S=-(u-v)*z
\]

and hence, with \(\widehat S=(s-t_0)*S\),

\[
\partial\widehat S=(s-t_0)*(u-v)*z.
\]

This is an especially useful expanded form of (5.1). There are four types of terms, prefixed by (su), (sv), (t_0u), and (t_0v). The **only possible mark** in these prefixes is (s<u); the mark (u<b) is absent because (z) avoids (b), and no old marks occur in (z). Thus \(\partial\widehat S\subseteq F_1\), with all signs correct.

The additional marked cover (s<u) is genuine: (t_0) is incomparable with (s,u), and (v) is incomparable with (u). The old marks remain covers after both layers of new minima. The top simplex has coefficient (+1) and is unique, by the path criterion.

Contractibility of \(\Delta Q\) follows from two suspensions. For (F_0(Q)), put \(K=F_0(U)\). The description

\[
F_0(Q)=(t_0*K)\cup(s*(K-u))
\]

is exact: the first cone contains every filtration-zero simplex not using (s), and the second every such simplex using (s) (necessarily avoiding (u)). Their intersection is (K-u). Further,

\[
K-u=v*F_0(X),
\]

since (v) is unmarked and below every old vertex. This intersection is contractible, and both pieces are cones. Thus (F_0(Q)) is contractible. Consequently the relative homology groups of the pair vanish, exactly as required by Lemma 2.2.

The bidegree formula is consistent:

\[
d_{r+1}:E^{r+1}_{r+2,0}\longrightarrow E^{r+1}_{1,r}.
\]

For (k=r+1), this is \(d_k:E^k_{k+1,0}\to E^k_{1,k-1}\); its target has **total homological degree (k)**. This observation explains the numerical typo in Section 6.

## 6. Independent finite computations and example counts

I independently implemented the seed and successive capped/uncapped extensions from the given cover relations, enumerated all strict chains, computed exact signed simplicial boundaries for the witness chains, and performed standard left-to-right filtered boundary-matrix reduction over \(\mathbb F_2\) (with the filtration-zero simplices omitted for relative homology). No internal computation files were used.

The four advertised barcode intervals were reproduced, with one homological-degree correction:

| Example | Vertices | Marks | Correct degree | Interval | Audit |
|---|---:|---:|---:|---|---|
| Absolute (d_4), pre-cap | 11 | 4 | 3 | \([0,4)\) | Confirmed |
| Relative (d_4), two extra minima | 13 | 5 | **4**, not 3 | \([1,5)\) | Numerical error in packet |
| Absolute (d_5), pre-cap | 14 | 5 | 4 | \([0,5)\) | Confirmed |
| Relative (d_5), two extra minima | 16 | 6 | 5 | \([1,6)\) | Confirmed |

Also obtained: absolute (d_3) on the nine-vertex seed, degree 2 with interval \([0,3)\); absolute (d_4) on the capped 12-vertex extension, degree 3 with interval \([0,4)\); and absolute (d_6) and relative (d_6) in the next small generated models. The mod-two calculations are independent corroboration only; the preceding chain and exact-sequence arguments establish integrality.

The formulas for the general sizes also check:

- Capped absolute (d_k): (9+3(k-3)=3k) vertices, (k) marks.
- Pre-cap absolute (d_k), (k\ge4): (3(k-1)+2=3k-1) vertices, (k) marks.
- Relative (d_k), (k\ge4): (3(k-1)+4=3k+1) vertices, (k+1) marks.

None of these checks establishes minimality, and the packet appropriately makes no minimality claim.

## 7. Issues, omissions, and presentation suggestions

### Actual error (minor, not fatal)

1. **Section 6, second table row:** replace “degree 3” with **“degree 4”** for the relative (d_4) barcode. The differential \(E^4_{5,0}\to E^4_{1,3}\) kills a class in homological degree 4. My independent reduction detects a single positive-length relative interval \([1,5)\), in degree 4, and none in degree 3 with that interval.

### Unverifiable assertion in this packet

2. **Theorem 5.1, ten-vertex/four-cover relative (d_3):** no Hasse diagram, chain witness, or citation is provided. This is not a disproof; it is **out of reach of a self-contained blind audit**. Include its construction or an exact reference, or move it out of the theorem. The theorem for every (k\ge4) is unaffected.

### Correct but potentially confusing

3. **The spectral-sequence page argument** is the most serious presentational bottleneck. The statement that a vanishing (d_m) yields a filling in (F_{m-1}) is correct, but a reader may initially worry about earlier incoming differentials and whether a boundary can be trivial on one page but nontrivial in homology. The long exact sequence of the final pair/triple above is a clean way to expose the mechanism. Alternately give a precise filtered-chain formula for the (p=0) or (p=1) target at the relevant page.

4. **Distinguish the roles of the cap and pre-cap:** the two new minima already give the absolute late differential; (y) is needed to restore the *avoidance* property for iteration. A short explanatory sentence before Lemma 4.1 would sharpen the conceptual picture.

5. **Use the expanded boundary \((s-t_0)*(u-v)*z\)** in the relative argument. It makes the (F_1) bound immediate and reduces the risk of confusing the new mark (s<u) with the old mark (u<b).

6. **Clarify “integral differential.”** The proof yields more than nonzero reduction modulo a prime: the displayed differential sends a generator to a class of infinite order (indeed a primitive class in the relevant image). That stronger point is worth stating plainly.

7. **Notation:** a reminder that (K-u) denotes induced deletion of vertex (u), not a chain-theoretic subtraction, would help. The distinction between the old initial vertex (b), the new minima (u,v), and the later minima (s,t_0) is otherwise clear.

### Unnecessary hypotheses / conceptual simplifications

8. The two certificate lemmas only need the following *terminal filtration* facts: a unique top-weight (m)-simplex with no coface; ambient homology vanishing in the two dimensions used by the long exact sequence; and a chain with its boundary in the indicated low filtration. “Marked covers form a minimal-to-maximal path” is an excellent **sufficient combinatorial condition**, but not essential to the abstract certificate. Likewise, full contractibility is stronger than needed for the absolute nonvanishing step. I would state the clean path condition as an easy-to-verify corollary of a more flexible maximal-simplex criterion if later generalizations are anticipated.

9. The seed calculation can be made easier to read by giving \(\partial T=a*t+w\) first, with the seven terms of (w) grouped by their first vertex, and then displaying (C_3=T+a*x*t). The current presentation is correct but asks the reader to identify the cancellation inside a long twelve-term expression.

10. The topological deletion proof is efficient and valid. Adding one phrase—“(e) is maximal in (M), so its link is exactly the strict lower-set complex”—would make it entirely transparent.

## 8. Mathematical context and antecedents

Long finite-filtration spectral-sequence differentials and their connection to long persistence intervals are standard in general filtered-complex theory; they are not new phenomena in themselves. For background see:

- A. Zomorodian and G. Carlsson, *Computing Persistent Homology*, **Discrete & Computational Geometry** 33 (2005), 249–274; [authors’ record](https://geometry.stanford.edu/lgl_2024/paper.php?id=zc-cph-05).
- [The Stacks Project, §12.24, “Spectral sequences: filtered complexes”](https://stacks.math.columbia.edu/tag/012K), for general filtration conventions and page machinery.
- *A new spectral sequence for homology of posets*, **Topology and its Applications** (2017); [journal abstract](https://www.sciencedirect.com/science/article/pii/S0166864116303182). This demonstrates prior spectral-sequence work on finite posets but uses a different filtration and does not establish the present particular cover-insertion construction.

I have **not identified an antecedent for the precise combination** of a clean Boolean family of inserted Hasse covers, the stated cover-count filtration, the integral maximal-simplex witnesses, and arbitrarily long nonzero differentials. This is not an assertion of novelty: the present review did not undertake an exhaustive priority search.

## 9. Final recommendation

The proof is substantially more robust than one might expect from its compact presentation. The integrality is established by explicit oriented chains and a topological obstruction, the induction retains exactly the property needed for iteration, and the relative construction has the necessary contractibility on both sides of the pair.

**No fatal error or unresolved mathematical gap was found in the main results.** Correct the degree in the Section 6 table, document or remove the separate (d_3) relative example, and consider replacing the certificate proofs with the long-exact-sequence formulation. On the supplied evidence, the stated absolute (d_k\ (k\ge3)\) and relative (d_k\ (k\ge4)\) theorems are valid over \(\mathbb Z\) (and indeed over any nonzero commutative unital coefficient ring).
