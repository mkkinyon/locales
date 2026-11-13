# Project A — filtered-apex no-go theorems: regular arms and clopen-positive gluing

**13 November 2026. New bounded working theorems; adversarially reconstructed internally, not externally refereed.** Follow-up to [noncompact two-apex rational controls](ProjectA_Q_NONCOMPACT_TWO_APEX_FILTER_CONTROLS_2026-11-13.md). The earlier examples suggested testing intermediate tail densities. This note proves that **every** filtered three-apex space with regular Hausdorff arms is Q′-positive, regardless of intermediate tail behavior, and that replacing tail points by **clopen anti-Urysohn clouds** also cannot work. Neither Q nor Q′ is settled in general.

Standing definitions: for X, D,D₂ are full/finite fitted diagonals, W=cl D and W₂=cl D₂. Q′ for X means W(X)=W₂(X). A marked Q′ hole is a nonzero relatively open E_C=W₂(X)∧O(w_C→d), with d the Φ₂-fixed open defining W₂. The previously externally checked support theorem produces a nonzero closed K⊆X, a finite-compatible Boolean pair with a C-zero value on K, a **nonzero marked Q′ hole persisting on K**, and a jointly zero-reflecting pair h,k:O(K)→M.

## 1. The regular-patch exclusion on normalized supports

**Lemma 1.1 (repackaging earlier one-sided rigidity).** Let K be the least closed common coordinate support of the Booleanization of a genuine Q′ open hole. Then **no nonzero K-open V can lie inside a closed K-sublocale J that is compact or regular**.

Proof. Let e be the K-open complement of J and v the open defining V≤J, so v∧e=0. On the Boolean target component m=h(v), the first endpoint kills e and therefore factors through J. The compact/regular one-sided rigidity theorem says a finite-compatible pair with its first endpoint in J matches **every** cover. But the marked full cover C has matching value zero. Thus m=h(v)=0. Interchange h and k to get k(v)=0. Joint zero-reflection on the normalized support forces v=0, contradiction. This works for weak D₂>D normalization too; the *open-hole persistence* is used only later to contradict Q′ positivity of K. □

## 2. All regular Hausdorff filtered arms are Q′-positive

Fix a nonempty regular Hausdorff space T and nonempty decreasing open tails G₀⊇G₁⊇⋯ with ∩_n G_n=∅. Form the two-arm three-apex space

\[
X=X(T,G)=T_+\amalg T_-\amalg\{a,b,t\},
\quad
A_n=\{a\}\cup(G_n)_+,\ 
B_n=\{b\}\cup(G_n)_-,\ 
T_n=\{t\}\cup(G_n)_+\cup(G_n)_-.
\]

Ordinary arm opens and these apex neighbourhoods generate the topology. As proved in the previous note, X is sober and T₁; second countability follows when T is second countable.

**Theorem 2.1.** For **every** such regular Hausdorff T and any admissible tails G_n,

\[
\boxed{W(X(T,G))=W_2(X(T,G)).}
\]

In other words **this entire mixed-tail family is Q′-positive**, even though Φ₂(z)>z can occur.

**Proof.** Suppose Q′ fails. Apply the marked-hole support reduction to obtain a nonzero closed K⊆X with the same genuine Q′ defect and no regular or compact patch (Lemma 1.1). Let C_+=K∩T_+, C_-=K∩T_-. These are closed subsets of the regular Hausdorff space T (in their respective copies).

**Claim:** for every n, G_n∩C_+ is dense in C_+ (and analogously for C_-). Otherwise choose nonempty relatively open V⊆C_+ disjoint from G_n. Since the arm is open in X, V is nonzero open in K. Its K-closure J has no apex point: A_n∩K and T_n∩K are disjoint from V; B_n never meets the positive arm. It has no negative-arm point either. Thus J⊆C_+ and equals the closure in the regular space C_+. In particular J is a **regular closed sublocale of K** containing the nonzero open V. This contradicts Lemma 1.1. The same argument applies to C_-.

If both C_+ and C_- are empty, K is a nonempty finite T₁ subspace of {a,b,t}, hence compact, again contradicting Lemma 1.1. At least one arm C_± is therefore nonempty. Density of G_n∩C_± implies every t-neighbourhood T_n meets K, so t lies in the closure of K and, since K is closed in X, **t∈K**.

We show that t lies in the K-closure of **every nonempty K-open U**. First U must meet at least one C_±. Indeed if U contained only apex points, any apex present without its attached arm would be isolated in K and would itself form a nonzero compact closed patch, contrary to Lemma 1.1. And for any apex with an attached arm, every basic apex neighbourhood meets that arm because the G_n∩C_± are nonempty. Now U∩C_± is a nonempty relatively open subset of that arm; density gives U∩C_±∩G_n≠∅ for every n. Hence every T_n∩K meets U, and t∈cl_K U.

Thus every pair of nonzero opens of K has closures meeting at t: **z_K=0**. By the rank-zero identity Φ_K(0)=Φ_{2,K}(0)=z_K=0, both pre-nuclei already fix 0, and

\[
W(K)=W_2(K)=U(K)=K^2.
\]

But the marked-hole support theorem says this K still fails Q′. Contradiction. □

**Interpretation.** The dichotomy from the previous segment is exhaustive for regular Hausdorff arms *after normalized support reduction*: either some tail is not dense on that support, giving a forbidden regular patch, or all tails are dense there, making that support anti-Urysohn. We make **no assertion** that D₂=D always holds on X(T,G): anti-Urysohn supports may still carry weak nonclosed defects.

## 3. Arbitrarily many clopen positive pieces plus a positive remainder

**Theorem 3.1 (Q′ clopen-remainder gluing).** Let (e_i)_{i∈I} be an arbitrary family of **complemented opens** of a locale X. Assume each clopen sublocale X_i=O(e_i) is Q′-positive. Put e=∨_i e_i and K=C_X(e), the closed remainder. If K is also Q′-positive, then **X is Q′-positive**. No finite, disjoint or locally finite hypothesis on the family is imposed.

**Proof.** Suppose there is a nonzero relatively open Q′ hole E⊆W₂(X) disjoint from W(X). For each clopen e_i, the crossed strips e_i⊠e_i* and e_i*⊠e_i are far, so W₂(X)≤U(X) has zero intersection with them. On the chart e_i², closed heredity of D,D₂ and commutation of closure with **clopen** restriction give

\[
W_2(X)\wedge O(e_i\boxtimes e_i)=W_2(X_i),\qquad
W(X)\wedge O(e_i\boxtimes e_i)=W(X_i)
\]

as sublocales of the open chart square. Since W₂(X_i)=W(X_i), E misses the chart. Since W₂ has no crossed-strip part, E also misses e_i⊠1 and 1⊠e_i. Joining over all i gives E∧O(e⊠1)=E∧O(1⊠e)=0, hence E≤K².

Now B(E), the least dense Boolean sublocale of E, lies in D₂(X)∧K²=D₂(K) by closed heredity. Because B(E) is dense in E, this makes E≤W₂(K). Also E=W₂(X)∧O(ρ) for a marked cover residual ρ, so, using W₂(K)≤W₂(X)∧K², E is **relatively open in W₂(K)**. Since E is disjoint from the full fitted diagonal D(X), it is disjoint from D(K); relative openness then makes it disjoint from W(K). Therefore K has a genuine Q′ hole, contradicting its hypothesis. □

This is an **actual sublocale** gluing statement; the proof does not infer density after arbitrary closed restriction. The preservation of the marked open E is the essential step.

## 4. Nonregular Arrieta clouds still give a positive control

Let A be the second-countable, strongly Hausdorff, anti-Urysohn **noncompact** space from Arrieta's Example 4.5, with W(A)=W₂(A)=U(A)=A². Take T=⨿_{n∈ω}A_n and G_N=⨿_{n≥N}A_n; build X=X(T,G) as above.

- X is T₁, sober, countably based and noncompact. Each cloud A_{n,+}, A_{n,-} is **clopen** in X; it is noncompact and anti-Urysohn, so regular-arm rigidity is not applicable to the entire cloud.
- The finite cover F={T_+,T_-,A₀,B₀,T₀} and r=A₀⊠B₀ satisfy r∧w_F=(G₀)_+⊠(G₀)_-≤T_+⊠T_-≤z_X. The last inclusion holds because the cross-arm rectangle is a join of products of **disjoint clopen clouds**. Yet (a,b)∈r lies outside z_X because both apex-neighbourhood closures contain t. Thus Φ₂(z)>z and W₂<U.
- Every cloud is Q′-positive (anti-Urysohn implies W=W₂=U), and the closed complement of their union is the finite discrete apex subspace {a,b,t}, also Q′-positive. Theorem 3.1 therefore yields

\[
\boxed{W(X)=W_2(X)<U(X).}
\]

**Conclusion:** Even replacing the isolated tails by genuinely nonregular anti-Urysohn clouds does **not** create a Q′ counterexample **if the clouds remain clopen with a Q′-positive closed remainder**.

## 5. Remaining viable design space

The two no-go results rule out different kinds of easy repairs:

1. **Regular Hausdorff arms, however mixed the tails:** normalized bad supports become either regularly patchable or anti-Urysohn.
2. **Clopen Q′-positive clouds with Q′-positive closed remainder:** any purported open hole localizes to the remainder, where it is impossible.

Thus a serious next two-apex candidate needs an **inseparable, nonregular crowded core whose potentially bad support cannot be removed by clopen Q′-positive charts**, with tail adhesion selective enough that z is not identically zero. Stronger still, the desired witness must have **nonzero relatively open interior in W₂**, not just D₂>D.

A sensible next bounded test would use a **single nonregular arm with non-clopen, overlapping attached cores**, potentially modelled on Arrieta's construction, and compute cover squares on a genuinely mixed chart. This is only a research direction. The present work supplies no Q or Q′ counterexample, but closes a broad family of tempting construction attempts.

**Audit status:** Theorem 2.1 and Theorem 3.1 are internally checked working mathematics. Their dependencies (one-sided regular rigidity, marked Q′ hole persistence, clopen heredity and rank-zero identity) are independently corroborated in the 12–13 Nov blind referee cycle, but these new combinations have not had a separate external referee.
