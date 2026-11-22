# Opus endgame additions: closed-support overlap, weak/full equality, Rees rectangles, and étale fitted diagonals
## 21 November 2026 · independently proposed by Claude Opus 5.5 High; internal mathematical reconciliation

**Status:** The propositions below are **post-review mathematical suggestions**, not part of the recent seven-interface blind structural packet. Statements (E2)–(E4) are internally checked **conditional on the previously separately audited closed-support generation theorem (G′) and mixed rectangle composition rule (RC)**. (E5) is internally checked from the cover characterization/functoriality of the **fitted diagonal**; published antecedents, especially Arrieta/Picado–Pultr, have **not** been ruled out. Do not label any of these as original or automatically inherit E status from their inputs. Opus's uploaded original report is preserved in the conversation; this note summarizes the mathematics, not its entire editorial assessment.

## 1. Nonzero overlap has a point-set criterion (E2)

Let G be **compact Hausdorff**, \(B,C\subseteq G\), and \([B],[C]\) their induced point-generated spatial sublocales. Then
\[
\boxed{[B]\wedge[C]\ne0
\iff
\exists K\subseteq G\text{ nonempty closed}:\ 
B\cap K,\ C\cap K\text{ both dense in }K.}
\tag{Overlap}
\]
*Necessity:* for \(W=[B]\wedge[C]\ne0\), take its least ambient **closed support** \(K=\operatorname{cl}_G W\). The **single-factor** form of the compact closed-support lemma shows that the traces of B,C are dense in K.

*Sufficiency:* if both traces are dense in K, then their induced sublocales in K are dense. Isbell's least dense sublocale \(\mathcal B(K)\) is nonzero and lies in both. Embed K as a closed sublocale of G: \(\mathcal B(K)\le[B]\wedge[C]\).

**Remarks:** If G is scattered, every such K has an isolated point k and density forces \(k\in B\cap C\). Thus on **scattered compact Hausdorff G**, \([B]\wedge[C]\ne0\iff B\cap C\ne\varnothing\). In general the closed K can be perfect and B∩C empty (rationals/irrationals). The criterion uses **point sets** but makes an assertion about **genuine localic overlap**. It is an exact existential condition, not a claim of an algorithm deciding arbitrary subsets.

## 2. Exactly when point-generated and full rectangles coincide (E3)

Let X,Z be compact Hausdorff, A⊆X,D⊆Z, and put
\[
p=[A\times D]_{X\times Z},\qquad q=[A]_X\times_{\mathrm{Loc}}[D]_Z.
\]
Using the independently reviewed compact-closed-support generator theorem
\[
q=\bigvee_{K:\ (A\times Z)\cap K\text{ and }(X\times D)\cap K\text{ dense in }K}\mathcal B(K)
\quad\text{(all K nonempty closed),}
\tag{G′}
\]
we obtain
\[
\boxed{p=q\iff
\text{every such K also has }(A\times D)\cap K
\text{ dense in }K.}
\tag{Weak=Full}
\]

*If the extra density holds*, \(\mathcal B(K)\le[(A\times D)\cap K]\le p\) for every generator K, so \(q\le p\). The reverse inclusion p≤q always holds.

*Conversely*, if some eligible K has \((A\times D)\cap K\) **not dense**, choose a nonempty relatively open \(N=K\cap U\) disjoint from A×D, where U is an **ambient open** of X×Z. Since K is closed, the points of \((A\times D)\cap U\) all belong to the **ambient open complement** \((X\times Z)\setminus K\). The crucial localic step is that **restriction to an ambient open preserves point-generated joins**:
\[
p\wedge O(U)=[(A\times D)\cap U]\ \le\ O((X\times Z)\setminus K).
\]
Thus \(p\wedge O(U)\wedge K=0\). But \(\mathcal B(K)\le q\) and \(\mathcal B(K)\) is **dense in K**, so \(0\ne\mathcal B(K)\wedge O(U)\wedge K\le q\wedge O(U)\wedge K\). Therefore p≠q.

**Important qualification:** The argument does **not** use any invalid general identity \(p\wedge K=[(A\times D)\cap K]\) for an arbitrary **closed** K. It first restricts to the **ambient open U**, where point-generated joins can be restricted, and only **then** meets the closed K. This is the precise justification missing from the short version of Opus's proof.

Example: on the circle with A=D=the rational-rotation subgroup, take K the graph of an irrational rotation. Both coordinate traces are dense on K but \((A\times D)\cap K=\varnothing\). Hence \(p\ne q\). Equally, the graph \(K=\{(x,x/\sqrt2):x\in[0,1]\}\) gives q≠p for A=D=\(\mathbb Q\cap[0,1]\), where the trace intersection may contain only the origin. **Classical Johnstone–Sun** already gives weak/full distinctions and positive equality cases; this criterion is a potential reformulation, **not a priority claim**.

## 3. The generator semigroup is a Rees-matrix inflation (E4)

Let \(\Sigma^*(G)=\{[A]_G:A\subseteq G,\ [A]\ne0\}\), for compact Hausdorff G. Write \(T\bowtie U\) iff \(T\wedge U\ne0\), whose point-set criterion is (Overlap). For nonzero induced spatial S,T, the full product \(q(S,T)=S\times_{\mathrm{Loc}}T\) is nonzero. The first and second projection images recover S and T: thus **distinct ordered pairs of supports give distinct q-rectangles**.

By RC,
\[
q(S,T)\circ q(U,V)=
\begin{cases}
q(S,V)&T\bowtie U,\\0&\text{otherwise}.
\end{cases}
\tag{Rees}
\]
The semigroup consisting of nonzero q-rectangles and 0 is therefore the **combinatorial completely 0-simple Rees matrix semigroup**
\[
M^0(\{1\};\Sigma^*(G),\Sigma^*(G);\bowtie).
\]
The sandwich matrix \(\bowtie\) is reflexive, so it has no zero rows or columns. Its idempotents are the elements q(S,T) with \(T\bowtie S\).

More generally, for any nonzero point-generated rectangle p(A,B), its **projection images** are \([A],[B]\), so the assignment
\[
\varphi:p(A,B)\mapsto q([A],[B]),\qquad
\varphi:q(A,B)\mapsto q(A,B),\qquad\varphi(0)=0
\]
is well-defined **even if p and q presentations happen to coincide** (the projection supports are intrinsic). Formula RC gives \(rs=\varphi(r)\varphi(s)\) for *all two generators* r,s. Hence the **generator semigroup**, without finite joins, is an **inflation** of the Rees semigroup.

**Caveat:** The **finite-join algebra** \(\mathscr R_\vee(G)\) is a further join-constrained extension and is **not itself identified with a bare Rees semigroup**. In particular, an arbitrary join relation among full rectangles must be respected. This interpretation demotes the elementary B16 “unital iff finite” criterion to a useful corollary and puts clique powers into an established semigroup-theoretic framework. Compare Rees 1940/Clifford–Preston before publication.

## 4. Fitted diagonal separation ascends along étale maps (E5)

Let \(p:X\to Y\) be a **localic étale map**, i.e. a local homeomorphism in Loc. If \(\mathcal D(Y)=\Delta_Y\), then
\[
\boxed{\mathcal D(X)=\Delta_X.}
\tag{EtaleD}
\]
*Proof.* The preimage \((p\times p)^{-1}(\mathcal D(Y))\) is a **fitted** sublocale of \(X^2\), since fitted sublocales are meets of open sublocales and localic inverse image preserves such meets. It contains the diagonal, hence
\[
\mathcal D(X)=\operatorname{fit}\Delta_X
\ \le\ (p\times p)^{-1}(\mathcal D(Y)).
\]
Under \(\mathcal D(Y)=\Delta_Y\), any generalized pair \((f,g):Z\to\mathcal D(X)\) satisfies \(pf=pg\). An étale p admits an **open cover by sections** \(U_i\hookrightarrow X\) on which p is an isomorphism onto a Y-open. The definition of \(\mathcal D(X)\) through its all-cover diagonal squares applied to this cover ensures that Z is **covered by opens on which f and g land in the same section \(U_i\)**. There the equality pf=pg implies f=g, hence f=g globally. This proves \(\mathcal D(X)\le\Delta_X\), and the reverse inclusion is automatic. □

**Caveat:** The only nontrivial naturality used is \(\operatorname{fit}\Delta_X\le(p\times p)^{-1}(\operatorname{fit}\Delta_Y)\), justified above. A separate comparison to existing fitting-diagonal literature is needed before calling this new. This deduction isolates the **finite-cover Boolean obstruction** as the genuinely interesting part of the rational-bridge construction.

## 5. Remaining limits

- **E2–E3:** internally checked as written under compact Hausdorff hypotheses and conditional on the earlier externally accepted support theorem G′. The relation of (Weak=Full) to existing product-spatiality criteria is **not** determined.
- **E4:** checked as a structural interpretation of **generator multiplication**, not a classification of the join-algebra. Exactly the completely 0-simple semigroup terminology should be compared with standard Rees theorem sources.
- **E5:** checked using **localic** cover characterization; not a claim of a spatial-only result or a new separation axiom.
- **Not included:** Opus's speculative S1–S6, its proposal to reorganize the entire manuscript as two parts, the strong characterization “all genuinely pointfree phenomena reduce to Isbell” (which has interpretive exceptions), or the additional \(\omega\)-rank examples. These merit separate consideration, not automatic promotion.

See [the new arbitrary-parameter scattered matrix extension](ProjectA_OPUS_SCATTERED_ARBITRARY_PARAMETER_EXTENSION_2026-11-21.md) for E1 and [Opus review reconciliation](ProjectA_OPUS_ENDGAME_INDEPENDENT_REVIEW_RECONCILIATION_2026-11-21.md) for the global assessment and code limitations.
