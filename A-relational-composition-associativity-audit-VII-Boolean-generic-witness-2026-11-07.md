> **7 Nov 2026 — EXTENSION TO THREE PERMUTATIONS; NONTRANSITIVITY RESOLVED:** [Audit VIII, exact Boolean permutation relation and witness](A-relational-composition-associativity-audit-VIII-nontransitive-Arrieta-2026-11-07.md). The pairwise Boolean-generic construction in the present note was initially transitive within a chosen K_n-preserving homeomorphism orbit. Widening to arbitrary coordinate permutations of Cantor yields h=q,k=qσ*,ℓ=qτ* with hAk,kAℓ but h not Aℓ, proving **A²⊄A and D_Y²⊄D_Y even though Y is SPATIAL and STRONGLY HAUSDORFF**. General exact criterion: for homeomorphisms ρ,λ preserving the finite-support set D, h_ρ A h_λ iff the set of finite-support x with ρ(x),λ(x) sharing the SAME K_n is DENSE in Cantor. Thus the earlier suggestion that all Boolean-generic transformations are trapped in a transitive orbit is superseded (though the subgroup preserving every K_n itself is still a transitive orbit). A³ associativity remains UNRESOLVED.

# Project A — Associativity audit VII: explicit Boolean-generic offdiagonal witness in Arrieta Cantor surgery

**7 November 2026. NEW WORKING CONSTRUCTION; internally checked, not externally audited.** This is a substantial refinement of [audit VI's admissible-cover presentation](A-relational-composition-associativity-audit-VI-Arrieta-explicit-covers-2026-11-07.md). It produces an EXPLICIT pair of distinct frame homomorphisms related by the *global* fitted diagonal of Arrieta's space, using a concrete homeomorphism of the Cantor cube that preserves every finite replacement compactum K_n. It also provides a completely explicit nonzero Boolean-locale witness and a BASIC CYLINDER u for the independently audited negative I D⊄V transfer theorem. It does **not** resolve A³ associativity; in fact this automorphism orbit lies in a transitive subrelation of A.

## 1. Published source and base

Let C=2^N be Cantor cube, using coordinates 1,2,... . For n≥1 put

    K_n={x∈C:x_n=1, x_m=0 for all m>n}.

These are disjoint finite compacta, and ∪_n K_n is dense in C (indeed every infinite subfamily has dense union; Arrieta 2024 Prop. 4.4/Example 4.5). Put V=C\∪K_n, regular zero-dimensional spatial dense subspace of C. Let Y be the Arrieta topological extension Y=V⊔N with basis W∩V and {n}∪(W∩V) for Cantor-open W⊇K_n. By Arrieta Cor. 4.3 and Example 4.5, Y is spatial strongly Hausdorff. We do NOT use Arrieta's Property(F) argument in proving the new explicit D_Y>Δ_Y witness.

As in audit VI, define Θ(a)={n:∃Cantor-open W⊇K_n, W∩V⊆a}. A V-open cover C0={a_i} is admissible iff ∀n∃i with n∈Θ(a_i). Its global-diagonal-cover neighborhood is w_C0=∨_i a_i⊠a_i, and

    A=D_Y|V²=meet_{C0 admissible} O(w_C0).

## 2. A genuine nontrivial K_n-preserving Cantor homeomorphism

Let τ:C→C be the involutive continuous group automorphism on binary sequences

    τ(x)_1=x_1 XOR x_2,      τ(x)_j=x_j  (j≥2).

It is a homeomorphism (τ²=id), is nonidentity, fixes 0^∞, preserves the last-nonzero-coordinate position of every eventually zero NONZERO binary sequence, and hence

    **τ(K_n)=K_n for EVERY n**,
    **τ(V)=V**.

Check the n=1 case: x_2=0 on K_1 so x_1 is unchanged; n=2 has x_2=1, so x_1 flips while x_2 remains 1; n>2 highest 1 is unchanged. Every sequence with infinitely many ones is mapped to one with infinitely many ones.

## 3. The two Boolean-valued frame maps

Let B=RO(V) be the complete Boolean algebra of regular-open subsets, regarded as a FRAME, and let

    q:O(V)→B,   q(a)=a**,

the canonical double-negation frame SURJECTION; B joins are double-negation regularized unions. The locale T=Loc(B) is NONZERO and POINTLESS: V is crowded zero-dimensional, so B is ATOMLESS; an atomless complete Boolean algebra has no frame homomorphism to 2 (no completely prime ultrafilters).

Define

    h=q,              k=q∘τ_V* : O(V)→B,

where τ_V* sends a V-open a to τ^-1(a). Both are genuine frame homomorphisms.

**KEY ALL-COVER LEMMA:** For every Θ-admissible V-cover {a_i},

    **∨_i h(a_i)∧k(a_i)=1_B.**

Proof: By frame properties,
    ∨_i h(a_i)∧k(a_i)
      =q( ⋃_i [a_i∩τ^-1(a_i)] ).

Let H=⋃_i a_i∩τ^-1(a_i). Fix n. By admissibility choose i and a Cantor-open W_n⊇K_n with W_n∩V⊆a_i. Since τ(K_n)=K_n and τ(V)=V, the Cantor-open W_n∩τ^-1(W_n) contains ENTIRE K_n, and its V-trace lies in H. Hence H contains the V-trace of a Cantor-open neighborhood of EVERY K_n.

As ∪_n K_n is DENSE in C, the union of those neighborhoods is dense in C; its V-trace is dense in V. Therefore H is dense in V and q(H)=1_B. No finiteness assumption on the cover; the proof works for arbitrary index sets.

Thus the pair (h,k):T→V² factors through A=D_Y|V², using the full pointfree cover test.

## 4. Direct, explicit off-diagonal witness

Choose the V-clopen cylinder

    a={x∈V:x_1=1}.

Then τ^-1(a) differs from a on the nonempty clopen cylinder {x_2=1}∩V. Hence h(a)≠k(a); the two maps T→V are distinct and their A-related pair does NOT factor through Δ_V. This directly proves

    **A>Δ_V and D_Y>Δ_Y**,

independently of Arrieta's anti-Urysohn⇒failure Property(F) argument.

More concretely define

    b=h(a)∧k(a^c)
      = q(a∩τ^-1(a^c))
      = {x∈V: x_1=x_2=1},

a NONZERO V-clopen, where a^c=V\a. Let B_b=↓b be the nontrivial Boolean frame of the OPEN sublocale O_B(b)⊆Loc(B). Restrict h,k by taking b∧(-), giving genuine frame maps

    h_b,k_b:O(V)→B_b

such that

    h_b(a)=1_(B_b),   k_b(a^c)=1_(B_b),

and the universal admissible-cover condition still holds with top b. Therefore

    **D_Y∧O_Y(a⊠a^c)≠0**,

with both a,a^c viewed as Y-opens (since V↪Y is OPEN). The corresponding nonzero test locale has NO ordinary points.

This gives a VERY CONCRETE open u=a (a first-coordinate cylinder) for the independently refereed negative mixed I D⊄V transfer construction X_u=O(u∨σ)↪Y×S, rather than an abstract existence choice.

## 5. Orbit generalization, and what it does NOT establish

Let G be the group of Cantor homeomorphisms ρ preserving V and each K_n setwise. For any ρ,σ∈G, define h_ρ=q∘ρ_V* and h_σ=q∘σ_V*. For every admissible cover {a_i}, each a_i covering a neighborhood of K_n pulls back under both ρ,σ to neighborhoods of K_n; their intersection contains a neighborhood of K_n. Density of ∪K_n again gives

    (h_ρ,h_σ):Loc(B)→A.

Thus A contains a "complete" family of Boolean-valued generic pairs indexed by G. Their compositions inside this family remain A-related: if ρ,σ,λ∈G, then (h_ρ,h_λ) is already in A. Hence this construction ALONE gives no associativity counterexample: it is compatible with A transitive and therefore A³ associative. It shows instead that A's pointless excess is highly structured, not just an isolated defect.

## 6. Current precise research frontier

Combine audits V–VI:

    D_(X_u)³ associates iff D_Y³ associates iff A³ associates,

for a regular u≤V. §4 gives an explicit CYLINDER u and Boolean test source realizing mixed I D⊄V. The above homeomorphism orbit gives an explicit nonzero A\Δ witness, but no resolution of the A³ bracketing problem.

Possible next test: construct a generalized A-pair not arising from two K_n-preserving homeomorphisms, and check whether its failure of coherent composition with such orbit pairs makes (A²)A and A(A²) differ. This requires genuine localic image-pullback calculations, not pointwise data. Another option is to characterize A as a closure of the groupoid generated by all K_n-preserving homeomorphisms in the Booleanization, and test the resulting saturation. No equivalence is asserted.

**AUDIT FLAG:** All cited frame congruence identities, the kinematic XOR map, and the cover argument should be checked independently before publication; no priority claim.
