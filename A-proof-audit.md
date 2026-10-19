# Project A — Proof audit and risk register (first pass)

**18 October 2026.** This is an **adversarial first pass by the same assistant who developed the notes**, **not** a fresh independent referee report. "Checked" below means logical steps were re-examined, not that a second model/mathematician certified them. The [consolidated outline](A-consolidated-theorems.md) is the canonical current status. A standalone [cold-review brief](A-cold-review-packet.md) is prepared for a genuinely independent review.

## 0. Audit outcome

**No decisive counterexample to the principal deleted-plank / two-tag theorem found in this pass.** The construction's topology, local compactness, sobriety, pointwise I/U calculation, and functional obstruction were checked anew, including cases of points in A, B, and T\(A∪B). The classical nonnormality of the deleted plank is independently documented in standard topology references.

**No fundamental defect found in the kω quotient argument on this pass.** Crucial check: for compact K and *closed* E⊆X×X, E[K] is closed by compact projection, even when X is non-Hausdorff; hence q|K_n is a closed quotient map. The stage quotients q(K_n) are compact Hausdorff, and the extension proof uses the final topology. This requires the *kω determining-family* assumption, not mere countable covering by arbitrary compact sets.

**However, important parts remain unverified**, especially the locale-general finite-tensor closure lemma and the product/reflection comparison, and the novelty/priority claims. Do not circulate the notes as a referee-checked manuscript.

## 1. Individual proof obligations

### CRITICAL A. Closed localic relations and real-function reflection

**Source:** [A-equality-characterizations.md](A-equality-characterizations.md), §§1, 3–4; [A-hierarchy-first-results.md](A-hierarchy-first-results.md), §2.

**Claims:** d_F=⋁_{a≺≺b*}a⊠b; F is exactly the kernel pair of the completely regular reflection; F=Δ iff the canonical C(L)↪L is epi in Frm.

**First-pass:** the source's Picado–Pultr VI.1.5.2 and VI.2.2 statements are consistent with the manuscript formulas. A real map's opposite-interval rectangles generate the complement of its kernel pair; the image of evaluation into the product of reals generates C(L). Nevertheless, an independent reader should rederive the factorization in Frm/Loc and verify that the induced embedding Loc(C(L))→R^S is monic, without assuming frame epis are surjective.

**Status:** plausible, algebraically substantial, **needs independent category-theoretic audit**. Keep terminology distinct from (Fsep) fitted diagonals.

### CRITICAL B. The finite-rectangle lemma outside spatial locales

**Source:** [A-coherent-conormality.md](A-coherent-conormality.md), Lemmas 1.1–1.2, Theorem 2.1.

**Claim:** if a⊠b≤∨_{i=1}^n u_i⊠v_i and each u_i*∨v_i*=1, then a*∨b*=1, for **arbitrary locales**. Source proof asserts

    (a⊠b)*=(a*⊠1)∨(1⊠b*)

inside the frame coproduct, and uses diagonal pullback of finite closed-sublocale joins.

**First-pass:** for locally compact sober/spectral spaces the lemma follows indisputably by taking ordinary closures of rectangles and finite unions. For **arbitrary pointless locales**, the quoted tensor pseudocomplement identity and preservation steps must be verified explicitly using the cp-ideal description or another frame proof. This is a substantive unverified generality, especially because the algebraic-frame criterion is stated for all algebraic frames.

**Status:** **HIGH priority proof gap to certify**. If a direct general point-free proof fails, restrict Theorem C1 initially to coherent/spatial situations and distinguish algebraic generality as conjectural.

### CRITICAL C. The deleted-plank two-tag construction

**Source:** [A-continuous-counterexample-plank.md](A-continuous-counterexample-plank.md).

**Claim:** for locally compact Hausdorff T with closed disjoint A,B not separable by disjoint open neighborhoods, the tagged X is locally compact sober with I=U⊊F.

**Rechecked directly:**
1. The open-set condition is closed under unions/intersections; singleton tags are open; T is closed.
2. Formula for closures: for open O with V=O∩T,
       cl_X(O)∩T = cl_T(V) ∪ [A if p_A∈O] ∪ [B if p_B∈O],
   while a tag belongs to cl_X(O) exactly if it belongs to O.
3. Nontrivial inseparability classes: A∪{p_A}, B∪{p_B}; points outside these are singletons. Pairs in different classes can be given disjoint-closure opens using regularity and local shrinking in T; pairs of tags use their singleton opens.
4. At ordinary t∈A (resp. B), compact neighborhoods in T can be shrunk to avoid B (resp. A), then augmented by the forced tag, establishing compact containment in X. For tags the singleton itself is compact open.
5. A nonempty irreducible closed subset with a tag is the closure of that tag; if it has no tag, it is a singleton in Hausdorff T. This proves sobriety.
6. Every continuous X→R is constant on each E-class; a function distinguishing the tags would separate A,B in T, impossible.
7. The deleted plank's closed A,B are a standard nonnormality witness.

**Status:** **strongest current counterexample; passes first adversarial check**, but an independent review is still required. The tag space is **T0, not T1**. The open singletons are not closed.

### HIGH D. Localic passage from ordinary relations

**Sources:** all continuous/coherent notes.

The assertion "ordinary point relations coincide, therefore the closed localic sublocales coincide" needs:
1. the locale product to agree with the frame of opens of the ordinary topological product;
2. the product to be spatial;
3. all relations under comparison to be closed sublocales.

For locally compact sober X, the relevant core-compact spatial-product comparison is standard in classical topology/locale theory. It does **not** hold on an arbitrary spatial presentation. Every theorem invoking pointwise computations should restate the hypothesis, rather than letting it become implicit.

**Status:** sound in intended classical locally compact/spectral scope, **seek an exact textbook citation and prove the comparison once centrally**.

### HIGH E. Compact/kω quotient argument in non-Hausdorff spaces

**Sources:** [A-coherent-implication.md](A-coherent-implication.md), [A-kw-compact-exhaustion.md](A-kw-compact-exhaustion.md).

If E⊆X×X is a **closed equivalence relation** and X is compact (possibly non-Hausdorff), the quotient is compact Hausdorff: compact projection makes q closed and Wallace/tube lemmas separate disjoint compact fibers using E's closed complement. This proof must not silently assume X Hausdorff. For kω, q(K_n) are closed compact Hausdorff and form a determining sequence. Tietze extensions are compatible; the final topology yields a continuous global separator.

**Status:** convincing on first recheck. Verify the non-Hausdorff compact quotient lemma independently (do not cite the Hausdorff-only statement without additional proof).

### HIGH F. Paracompact decomposition without Hausdorffness

**Source:** [A-beyond-countable-exhaustion.md](A-beyond-countable-exhaustion.md).

The argument takes a locally finite open refinement by V_i⊆K_i (compact), forms its locally finite intersection graph, and groups countably many V_i per component into clopen X_α. **Important:** V_i itself need **not** be σ-compact. The proof correctly uses K_i∩X_α compact because X_α is clopen; this is the step that handles absence of Hausdorffness. Quotient is disjoint union of kω quotients.

**Status:** plausible and checked for the common "subset of compact is compact" fallacy (the source avoids it); independent inspection warranted.

### MEDIUM G. Coherent/conormal/mp-ring equivalences

**Source:** [A-coherent-conormality.md](A-coherent-conormality.md).

Check separately:
- compact-open criterion for I=U;
- lattice conormal witnesses from k*∨l*=1 using compactness of 1 and algebraicity;
- correspondence between prime ideals of K(O(Spec R)) and prime ideals of R, including **order direction**;
- U=F criterion using finite real-map gluing.

**Status:** mathematically plausible; **priority caution**: the prime/minimal-prime and mp-ring equivalences are established literature, and novelty is only the connection to the specific localic relations.

### MEDIUM H. Pointless strictness

**Source:** [A-hierarchy-first-results.md](A-hierarchy-first-results.md), §5.

Check the frame identity O(P×Y)≅monotone maps P→O(Y), preservation of all coproduct meets/joins, pullback along generalized points s_x:Y→P×Y, and the F argument that real maps agree along comparability components as maps **Y→R**. The choice Y with frame RO(R) is atomless complete Boolean, hence pointless classically.

**Status:** proof appears coherent but **a high-value independent point-free check**, since this is the main genuinely pointless illustration.

## 2. Documentation and mathematical scope corrections

1. **Historical status conflict.** README and old notes contain statements "the unrestricted continuous-frame implication remains open" from before the deleted-plank construction. Newer banner updates point to the counterexample, but the older prose remains. The consolidated outline is now authoritative; do not quote the old "open" text without its dated update. For a manuscript, remove contradictions altogether.
2. **Two different notions of compact.** An element compact in O(X) means its **open sublocale** is compact; a subset K⊆X compact need not be closed in non-Hausdorff X. Proofs must not infer compact closure from u≪a, or infer an arbitrary subset of a compact set is σ-compact.
3. **Topological versus localic equalities.** The localic claims depend on spatial products; only use the point calculations within a class where that comparison is proved.
4. **Historical conjecture defeated.** The relative stable-buffer lemma is false even for compact open starting elements; see the deleted-plank tags. Avoid presenting it as open.
5. **Frame epimorphisms.** Do not infer C(L)→L is surjective from epi, or F=Δ implies complete regularity.
6. **References/novelty.** Standard materials include Picado–Pultr (2021), Isbell strong Hausdorffness, conormal/mp-ring lattice theory, Tietze and kω topology, the deleted Tychonoff plank, and the point-set theory of nonnormal spaces. No comprehensive novelty search done yet.

## 3. Publication gate

Before treating these as publishable results, request a **genuinely independent** mathematical referee to (a) validate A1/A2, (b) prove or refute the arbitrary-locale finite rectangle lemma, (c) test the tagged counterexample with adversarial cases, (d) verify products in Loc and spatial passage, and (e) compare the intended main claims with literature.

A separate agent was **not available in the current session**, so this report is only an internal audit. The [cold-review packet](A-cold-review-packet.md) is ready for a fresh context or human reader.

## Addendum: an internal proof of the finite-rectangle identity (not independent review)

A second algebraic pass supplies a direct derivation of the identity flagged in §1B. Write Q=L⊗L. We invoke the **standard basic-rectangle lemma**:

    c⊠d = 0_Q  iff  c=0_L or d=0_L.

Every element of Q is a join of basic rectangles and

    (c⊠d)∧(a⊠b)=(c∧a)⊠(d∧b).

It follows that

    (a⊠b)*=(a*⊠1)∨(1⊠b*).                       (†)

Indeed the right side annihilates a⊠b. Conversely, if z∧(a⊠b)=0, express z as a join of rectangles c⊠d≤z. For each such rectangle, (c∧a)⊠(d∧b)=0. By the basic-rectangle lemma either c≤a* or d≤b*, so c⊠d is below the right side. Taking their join gives (†).

Now δ*(a⊠b)=a∧b for diagonal δ:X→X×X. Hence

    δ*((a⊠b)*)=a*∨b*.

For a rectangle r=a⊠b, its open-sublocale closure is C(r*). If

    a⊠b ≤ ⋁_{i=1}^n u_i⊠v_i,

taking closures gives

    C((a⊠b)*) ≤ ⋁_{i=1}^n C((u_i⊠v_i)*).

Finite joins of **closed** sublocales obey C(s)∨C(t)=C(s∧t), and inverse image preserves these finite joins because δ* preserves finite meets. Pulling back along δ yields

    C(a*∨b*) ≤ ⋁_{i=1}^n C(u_i*∨v_i*).

If each u_i*∨v_i*=1, the right side is empty. Therefore C(a*∨b*) is empty, hence a*∨b*=1, proving the **finite-rectangle lemma in arbitrary locales**, *provided* the standard basic-rectangle lemma is used as stated.

This closes the specific missing algebraic step **within our own reasoning**; it does not replace an independent review of the general coproduct facts. The arbitrary-locale tensor pseudocomplement identity should still be checked against a reputable published proof. For a published statement that nonzero basic rectangles satisfy componentwise order and do not vanish unless a factor does, see the frame coproduct preliminaries in T. Dube, *A note on weakly pseudocompact locales*, *Applied General Topology* **18** (2017), 131–143, §2.2.

**Revised risk:** the finite-rectangle lemma is now **internally proved conditional on a standard source-backed basic coproduct fact**, not merely extrapolated from spatial rectangles. It remains a suitable adversarial review target because the project heavily relies on it.
