# Project A — Associativity audit VIII: explicit Boolean triple proves the Arrieta fitted diagonal NONTRANSITIVE

7 November 2026. **NEW WORKING PROOF (internally checked, NOT externally audited).** This is a substantial positive result for the associated research program: Arrieta's spatial STRONGLY HAUSDORFF locale Y has a NONTRANSITIVE fitted diagonal D_Y. This is proved using three completely explicit coordinate permutations of the Cantor cube and all admissible cover tests. It does NOT settle the associativity of the cube D_Y^3, which still requires a second, image-instability argument. Earlier independent negative-transfer proof remains unaffected.

Literature basis: Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, Topology Appl. 342 (2024) 108785, Construction 4.2 and Example 4.5, pp. 12–14, open access https://pure-oai.bham.ac.uk/ws/portalfiles/portal/215992239/1-s2.0-S0166864123003784-main.pdf . Source explicitly defines K_n as finite-support nonzero binary sequences whose final 1 is at n, and Y as the topology attaching n to neighborhoods of the entire K_n.

## 1. Background and the exotic fitted relation A

Let C=2^N (coordinates n=1,2,...). Let D=∪_{n≥1}K_n be the countable DENSE subset of all nonzero finitely supported sequences. Put V=C\D (contains the zero sequence and all infinitely supported sequences). Form Arrieta's spatial, strongly Hausdorff locale Y=V⊔N with n-neighborhoods from the entire K_n.

For any a∈O(V), define Θ(a)={n:∃Cantor-open W⊇K_n with W∩V⊆a}. A cover C0={a_i} of V is **admissible** iff ∀n∃i with n∈Θ(a_i). The relation

    A := D_Y|_(V×V)
      = ∧_{C0 admissible} O(γ_C0),
    γ_C0 = ∨_{a∈C0}a_1∧a_2,

is fitted, symmetric and reflexive. Earlier audit VI proved D_Y has exact block form diag(A,Δ_N), while intrinsic D_V=Δ_V since V is regular. The ordinary points of A are exactly the diagonal points.

Let B=RO(V), the complete Boolean frame of regular opens, q:O(V)→B the double-negation frame surjection. Its locale Loc(B) is nonzero and pointless (B atomless). For any permutation π:N→N let π̂:C→C be the coordinate-permuting homeomorphism moving the 1-bit at index n to index π(n). It preserves D and V, and h_π:=q∘π̂_V^* is a frame hom O(V)→B.

For π,ρ, write

    H_(π,ρ)(C0)=⋃_{a∈C0}(π̂^-1(a)∩ρ̂^-1(a)) ⊆ V.

Then h_π A h_ρ iff for EVERY admissible C0, H_(π,ρ)(C0) is DENSE in V. This follows since q(H)=∨_a h_π(a)∧h_ρ(a) and q(H)=1 iff H is dense (in V).

## 2. Three explicit coordinate permutations

Define σ and τ as follows:

    σ swaps (2 4),(6 8),(10 12),...; fixes all other indices.
    τ(1)=2;
    τ(2m)=2m+2 for m≥1;
    τ(2m+1)=2m-1 for m≥1.

Both are genuine bijections N→N (τ has a single bi-infinite orbit ...→7→5→3→1→2→4→6→8→...). Define

    h=h_id=q,    k=h_σ,    ℓ=h_τ.

The crucial combinatorics:
(i) σ fixes arbitrarily large odd n;
(ii) σ(n)=τ(n)=n+2 at arbitrarily large n≡2 mod 4;
(iii) NO nonempty finite support S⊆N has max τ(S)=max S.
For (iii), if max S=n is EVEN, τ(n)=n+2>n. If max S=n is ODD, n∉τ({1,...,n}) since τ^-1(n)=n+2>n (also for n=1, τ^-1(1)=3). Therefore its image has maximum different from n. Equivalently, for ALL n:

    **τ̂(K_n)∩K_n=∅.**

## 3. ALL-COVER proof that h A k

Let C0={a_i} be ANY admissible cover and let B0 be ANY nonempty basic Cantor-clopen cylinder specified by the first m coordinates.

Choose a sufficiently large ODD n satisfying σ(n)=n and n>max(m,σ(1),...,σ(m)). Choose x∈K_n∩B0 with the prescribed first m bits, x_n=1 and all other bits after m zero. Then x and σ̂(x) BOTH lie in K_n.

Admissibility supplies some i with Cantor-open W⊇K_n and W∩V⊆a_i. By continuity of σ̂, the Cantor-open B0∩W∩σ̂^-1(W) contains x and is nonempty. Since V is DENSE in C, its V-trace is nonempty and lies in H_(id,σ)(C0). Thus H_(id,σ)(C0) meets EVERY basic Cantor cylinder, so is dense in V. Hence q(H)=1 and

    **h A k.**

This is an ALL-cover argument; x∈K_n is a convenient point in Cantor's complement D, NOT a point of V. The neighborhood trace on V supplies the frame inequality.

## 4. ALL-COVER proof that k A ℓ

For any admissible C0 and any nonempty basic cylinder B0 with first m coordinates prescribed, choose sufficiently large n≡2 mod 4, such that σ(n)=τ(n)=n+2 exceeds max of σ([1,m]) and τ([1,m]). Let x∈K_n∩B0 be the finite-support sequence with the prescribed prefix and only one further 1 at n. Then σ̂(x),τ̂(x) BOTH have final 1 at n+2; i.e. both belong to K_(n+2).

Admissibility yields some a_i covering a Cantor-open neighborhood W of the ENTIRE K_(n+2). The open B0∩σ̂^-1(W)∩τ̂^-1(W) contains x, hence has nonempty V-trace included in H_(σ,τ)(C0). Thus H dense, q(H)=1, and

    **k A ℓ.**

## 5. Explicit ADMISSIBLE cover separating h and ℓ

By §2(iii), the finite compact K_n and τ̂(K_n) are disjoint. Choose Cantor-CLOPEN W_n⊇K_n such that

    W_n∩τ̂^-1(W_n)=∅.

Such W_n exist: choose disjoint clopen neighborhoods O_n of K_n, P_n of τ̂(K_n), and take W_n=O_n∩τ̂^-1(P_n).

Let B0={x∈C:x_1=1,x_3=0}, a nonempty clopen cylinder. Because τ^-1(1)=3, one has (τ̂x)_1=x_3=0 for x∈B0. Thus B0 contains no τ̂-fixed point. For every p∈V:
- if p∈B0, choose a small Cantor-clopen neighborhood U_p of p satisfying U_p∩τ̂^-1(U_p)=∅ (possible because p≠τ̂p);
- if p∉B0, choose Cantor-clopen U_p of p contained in C\B0.

Consider

    C*={W_n∩V:n≥1} ∪ {U_p∩V:p∈V}.

This is an OPEN COVER of V (U_p cover V). It is Θ-ADMISSIBLE because each W_n is a neighborhood of the ENTIRE K_n. For each member a of C*, a∩τ̂^-1(a) misses B0∩V: this intersection is EMPTY for W_n; empty globally for U_p with p∈B0; and U_p∩B0=∅ if p∉B0. Therefore

    H_(id,τ)(C*)∩(B0∩V)=∅.

Since B0∩V is nonempty open, H_(id,τ)(C*) is NOT dense in V and q(H)≠1. Hence

    **h NOT A ℓ.**

Since V is second-countable one can replace the U_p family by a COUNTABLE subcover without changing this result.

## 6. Genuine localic nontransitivity

The three frame maps h,k,ℓ:O(V)→B define a map from NONZERO locale T=Loc(B) into V³. §§3–4 show it factors through E=A12∧A23; §5 shows its endpoint map does NOT factor through A because the admissible cover C* evaluates to q(H_(id,τ)(C*))<1_B.

Therefore the endpoint IMAGE A² contains this genuine generalized endpoint pair and does not lie in A:

    **A∘A NOT≤ A.**

By the block-diagonal formula D_Y=diag(A,Δ_N) from audit VI, this implies

    **D_Y∘D_Y NOT≤ D_Y.**

Thus there exists a **SPATIAL STRONGLY HAUSDORFF** locale with NONTRANSITIVE fitted diagonal. This strengthens the prior independently refereed Sierpiński-transfer example, which was not itself strongly Hausdorff.

This is NOT evidence that (A²)A≠A(A²): ordinary nontransitive symmetric relations can have associative composition, and the three maps above give one HONEST path, which belongs to BOTH bracketed three-factor images when extended to four honest maps.

## 7. Point-fiber theorem at ALL finite depths

**Proposition (working, independent of source Cantor details).** Suppose X is SPATIAL T1 and R⊆X² is a localic relation with

    R|_({p}×X)={p}×{p},   R|_(X×{p})={p}×{p}

for every ordinary p∈X. Then every parenthesized finite product P of copies of R has the same exact point-fiber identities. Proof by induction on the binary product: {p}×X↪X² is a CLOSED sublocale. Pullback of locale-surjections along CLOSED inclusions remains surjective (via the closed quotient ↑a frame restriction). Hence restriction of IMAGE(R'×_X S'→X²) to the closed left p-block equals image of its actual fiberwise path source. The R' left fiber forces the middle p, then the S' left fiber forces the endpoint p. Symmetric argument for right fibers. Reflexivity preserves the diagonal if R contains Δ.

For our A, the one-point fiber identity follows directly from the admissible covers {V\{p},b}, where b ranges over neighborhoods of p: the first member is Θ-admissible for ALL n (since p∉K_n), so the A-cover condition forces the other coordinate into every b; regularity V gives intersection {p}.

Consequently EVERY finite parenthesized power P of A has point set exactly Δ_V and is STRICTLY NONSPATIAL (as soon as P≥A>Δ_V). It is also DENSE (contains dense A), PROPER (ordinary offdiagonal pairs excluded) and REFLEXIVE.

## 8. The projection A→V fails the exact universal base-change preservation needed for automatic association

Let p1:A→V be projection. Form the discrete refinement f:V_d→V (V_d discrete on ALL ordinary points). Since V is spatial, f*:O(V)→P(V) is INJECTIVE, so f is a locale-surjection.

The pullback

    A×_V V_d ≅ ⊔_{p∈V} A_p ≅ V_d,

by the exact singleton-fiber property. Its map to A factors through Δ_V↪A and has image exactly Δ_V (f:V_d→V is surjective as a locale). Since A>Δ_V, this pullback map is NOT locale-surjective.

Thus **p1:A→V is NOT surjection-conservative (SC)** in the terminology of audit II. The same holds for p2 by symmetry, and for EVERY parenthesized power P of A since it has singleton point fibers and P>Δ.

Moreover p1:A→V is NEITHER OPEN NOR PROPER:
- If p1 were open, pick disjoint V-opens a,b with the nonzero open W=A∩O(a1∧b2), possible since A>Δ_V and Δ_V is CLOSED. The open map W→V would have a nonzero OPEN image contained in a; choose an ordinary point p of that open image (V spatial). The open surjection W→image, being stable under pullback, would have a nonzero fiber over p. But W_p≤A_p∧O(b)=0 because p∈a disjoint b: contradiction.
- If p1 were proper, its pairing with the other projection A→V would be proper as a map A→V² (graph into A×V is CLOSED because V strongly Hausdorff, followed by base change of proper p1). Since A↪V² is an embedding, this would make A a CLOSED sublocale. But A is DENSE and PROPER in V², contradiction.

The same arguments extend to ANY parenthesized finite P of A. So the standard OPEN/PROPER and SC image-stability sufficient conditions fail at EVERY depth. This diagnosis is useful but DOES NOT show nonassociativity of the specific cube A³.

## 9. EXACT frame-congruence test for the two cube bracketings

Let L=O(V), Q_n=L⊕...⊕L (n frame factors) and let G_ij be the frame congruence on Q_n generated by forcing γ_C^ij=1 for EVERY Θ-admissible cover C, where γ_C^ij=∨_{a∈C}a_i∧a_j.

The actual composable-pair locale E=A12∧A23 has

    O(E)=Q_3/(G_12∨G_23).

Let φ13:Q_2→O(E) be the frame map inserting the two variables at positions 1,3. Define K_2=ker φ13. Then the genuine IMAGE sublocale A² has frame

    O(A²)=Q_2/K_2.

There is now an EXACT algebraic criterion for the two cube bracketings:

    Left source  O((A²)_12 ∧ A_23) = Q_3/( K_(2,12) ∨ G_23 ),
    Right source O(A_12 ∧ (A²)_23) = Q_3/( G_12 ∨ K_(2,23) ),

where K_(2,12),K_(2,23) denote transported frame congruences generated by K_2 through corresponding coordinate embeddings Q_2→Q_3. Each bracketing's endpoint relation is the IMAGE of the respective 1,3 coordinate frame map Q_2→this quotient, hence determined by its KERNEL congruence.

Thus

    **(A²)A = A(A²) ⇔ endpoint KERNELS of these two quotient maps Q_2→(left/right sources) agree.**

This is a concrete frame-calculation target. The new nontransitivity witness proves γ_(C*)^{13}≠1 in Q_3/(G12∨G23), i.e. A² not≤A; but it does NOT compare the two enlarged triple-frame congruences. One must calculate additional identities on genuine image sublocales, not merely give another honest three- or four-point path.

## 10. Verdict and caution

**PROVED as WORKING (pending independent adversarial audit):**
1. D_Y is nontransitive even though Y is strongly Hausdorff and spatial;
2. the exotic A and every finite power have only diagonal ordinary points, are dense/proper/nonspatial, and have projections neither open nor proper nor SC;
3. exact Q_3/frame-congruence criterion for the remaining associativity test.

**UNRESOLVED:** whether (A²)A=A(A²); therefore D_Y³ and the selected transfer D_X³ remain unresolved. All source and pair constructions have been checked at the level of arbitrary admissible covers. No novelty or publication priority claimed.

Audit priorities: verify permutation maxima and construction of separating admissible cover C*; verify open/closed pullback-stability statement and frame congruence model for images; verify the p1 proper⇒A closed graph argument. A secondary test is whether the frame-congruence comparison can be sharpened by testing a specific γ_C or by exploiting countable Cantor cylinders.

## 11. EXACT combinatorial criterion for all Cantor homeomorphism-induced Boolean maps

The particular permutations σ,τ are instances of a more general test, which helps separate genuine localic phenomena from special choices of coordinates.

Let ρ,λ:C→C be ANY Cantor-cube homeomorphisms preserving D=∪K_n (hence also V) SETWISE. Define h_ρ=q∘ρ_V^*, h_λ=q∘λ_V^*:O(V)→B=RO(V). Define the SAME-CLASS coincidence set

    P_(ρ,λ) = {x∈D: ∃n≥1 with ρ(x)∈K_n and λ(x)∈K_n}.

**Theorem (new WORKING exact characterization):**

    **h_ρ A h_λ  ⇔  P_(ρ,λ) is DENSE in the Cantor cube C.**

**Sufficiency.** Fix any Θ-admissible cover C0 and any nonempty basic Cantor open B0. Pick x∈B0∩P. Then ρx,λx∈K_n for some n. The admissible cover has a member a containing the V-trace of an open Cantor-neighborhood W⊇K_n. Continuity gives a nonempty Cantor-open B0∩ρ^-1(W)∩λ^-1(W) containing x, whose V-trace is nonempty (V dense) and contained in H_(ρ,λ)(C0). So H is dense and q(H)=1; this holds for every admissible C0.

**Necessity.** Suppose P is NOT dense. Choose nonempty Cantor-CLOPEN B0 disjoint from P. The coincidence locus E={x:ρ(x)=λ(x)} is CLOSED and cannot have nonempty interior inside B0: if it contained an open O⊆B0, choose x∈O∩D (D dense); then ρx=λx lies in D, contradicting B0∩P=∅. Thus choose a nonempty clopen B⊆B0\E. Write F=(ρ,λ):C→C². Then compact F(B) is disjoint from the diagonal Δ_C and from K_n×K_n for EVERY n (if both coordinates lay in K_n, the input would lie in D since ρ and λ preserve V vs D, giving a point of P).

For each n, compactness and disjointness from K_n² supply a Cantor-CLOPEN neighborhood W_n⊇K_n such that

    F(B)∩(W_n×W_n)=∅.

One way to see it: the sets W×W, with W clopen neighborhoods of K_n, form a neighborhood basis of the closed K_n² in C²; if every such product met compact F(B), nested-compactness would force F(B)∩K_n²≠∅.

Similarly, since F(B) compact avoids Δ_C, for every target p∈C choose a Cantor-clopen neighborhood U_p of p with

    F(B)∩(U_p×U_p)=∅.

Compactness of C yields FINITELY many such U_1,...,U_m covering C. The V-cover

    C*={W_n∩V:n≥1} ∪ {U_i∩V:1≤i≤m}

is Θ-ADMISSIBLE (each W_n covers the whole K_n) and EVERY member a satisfies F(B)∩(a×a)=∅. Hence H_(ρ,λ)(C*)∩B=∅, so q(H)≠1 and h_ρ not A h_λ.

The resulting separating cover can be chosen COUNTABLE, consisting entirely of traces of Cantor-clopen sets: one W_n per compactum plus a FINITE supplementary clopen cover. This is a much sharper failure certificate than the uncountable-neighborhood cover initially used in §5.

**Permutational form.** If ρ,λ arise from coordinate permutations π,κ, then x∈D corresponds to a nonempty finite support S⊆N and

    x∈P_(ρ,λ)  ⇔  max π(S)=max κ(S).

Density of P is equivalent to the combinatorial condition:

    for every finite 0/1-prefix pattern, there exists a nonempty finite support S realizing the pattern with max π(S)=max κ(S).

Our explicit σ,τ satisfy this for pairs (id,σ) and (σ,τ), but NOT for (id,τ), since τ changes the maximum of every nonempty finite S. This gives an exact purely combinatorial proof of the Boolean-valued nontransitivity witness.

**Significance and limit.** We have identified a precise tolerance relation (reflexive, symmetric, NONTRANSITIVE) on the group of K_n-preserving *set D*-homeomorphisms as sampled by Boolean-valued generalized points. This does not establish nonassociativity of the localic relation cube A³: ordinary composition of this induced tolerance is associative by construction, and a cube discrepancy would require a nonstable intermediate localic image, not just a 3-map chain.
