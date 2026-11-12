# Project A — Q′ accumulation-frontier test: one-sided rigidity and a thin noncompact forcing boundary

**12 November 2026 — bounded INTERNAL investigation, not externally audited or literature-priority checked.** This tests the "nowhere-dense atomless frontier" proposed by [distributed-suprema note](ProjectA_Qprime_DISTRIBUTED_SUPREMA_FIXED_RANK_FIBERS_EXACT_W_2026-11-12.md), in response to the caution that a prospective Q′ obstruction should not simply recede behind ever more exotic construction requirements.

**Results:**
1. A new **one-sided** point-free theorem: when K↪X is **closed compact OR closed regular**, \(\mathcal D_2(X)\cap(K\times X)=\mathcal D(X)\cap(K\times X)\). Regular K even forces all generalized finite-compatible pairs \((f,g)\) with \(f\) in K to satisfy \(f^*(c)\le g^*(c)\) for every ambient open c.
2. An explicit **nowhere-dense closed frontier** F inside a noncompact algebraic Scott dcpo A, with F itself noncompact, nonregular, and **atomless Booleanization**, and with an honest **\(\mathcal D_2(F)>\mathcal D(F)\)** defect. It is the ideal completion of a binary prefix tree with optional terminal exits, tensored with the completed branching Scott dcpo. Thus mere existence of such a frontier is NOT excluded by completeness, Baire category, local compactness, or atomlessness.
3. Nevertheless **\(\mathcal W(A)=\mathcal W_2(A)=\mathcal U(A)=A^2\)**, and the same equalities hold for F; actual common-predecessor pairs are dense. The frontier experiment fails to generate a Q′ discrepancy, even though its prescribed local infinitary defect exists.
4. **Research decision:** stop producing variants of the ranked-bridge/forcing-frontier family absent an independently checked exact *mixed* finite-cover certificate. Return to intrinsic Boolean residual/fixed-point analysis or external audit. Both Q and Q′ remain OPEN.

## 0. Fitted-diagonal conventions

For L=O(X), and a cover \(\mathcal C\) of 1, \(w_{\mathcal C}=\bigvee_{c\in\mathcal C}c\boxtimes c\). Let \(\mathcal D=\bigwedge_{\mathcal C}\mathfrak o(w_{\mathcal C})\), \(\mathcal D_2=\bigwedge_{\mathcal F\ \mathrm{finite}}\mathfrak o(w_{\mathcal F})\), \(\mathcal W=\mathrm{cl}\mathcal D\), \(\mathcal W_2=\mathrm{cl}\mathcal D_2\). All sublocale equalities use generalized pairs \(T\to X^2\), so the one-sided result below is point-free and not contingent on spatiality.

## 1. NEW: one-sided compact-or-regular closed-sublocale lemma

**Theorem 1.1.** Let \(i:K\hookrightarrow X\) be a **closed** sublocale. If \(K\) is **compact OR regular**, then
\[
\boxed{\mathcal D_2(X)\wedge(K\times X)
=\mathcal D(X)\wedge(K\times X)}
\tag{1.1}
\]
as sublocales of \(X^2\). Symmetrically \(\mathcal D_2(X)\wedge(X\times K)=\mathcal D(X)\wedge(X\times K)\).

Let \(\mathcal C\) be an arbitrary X-cover and \(f,g:T\to X\) an arbitrary generalized D₂ pair with f factoring through K. Write \(K=\mathfrak c(a)\), so \(f^*(a)=0\).

**Proof: compact case.** Compactness of K means some finite F⊆C restricts to a K-cover, equivalently \(a\vee\bigvee F=1_X\). The finite X-cover \(\{a\}\cup F\) has matching value
\[
1_T=f^*(a)\wedge g^*(a)\vee\bigvee_{c\in F}f^*(c)\wedge g^*(c)
=\bigvee_{c\in F}f^*(c)\wedge g^*(c)
\le\bigvee_{c\in\mathcal C}f^*(c)\wedge g^*(c).
\]
Thus the original pair is fully compatible.

**Proof: regular case, stronger inequality.** For each c∈O(X), take an element \(v\in O(K)\) with \(v\prec i^*c\) (i.e. \(v^*\vee i^*c=1_K\)). Choose any lift w∈O(X) of \(v^*\). Then \(a\vee w\vee c=1_X\), so finite compatibility for \(\{a,w,c\}\), met with \(f_K^*(v)\), annihilates the a and w terms, and yields
\[
f_K^*(v)\le f^*(c)\wedge g^*(c)\le g^*(c).
\]
Since K is regular, \(i^*c=\bigvee_{v\prec i^*c}v\). Hence
\[
\boxed{f^*(c)\le g^*(c)\quad\text{for ALL }c\in O(X).}
\tag{1.2}
\]
For every cover C, \(\bigvee_{c\in C}f^*(c)\wedge g^*(c)=\bigvee f^*(c)=1_T\), so the pair is fully compatible. The reverse containment D≤D₂ is tautological. Swap coordinates for the symmetric assertion. QED.

**Corollary 1.2 (one-sided frontier eliminator).** A \(\mathcal D_2\)-versus-\(\mathcal D\) defect cannot be supported in \(K\times X\) or \(X\times K\) when K is **globally closed compact/regular**. In particular a closed Cantor-like perfect atomless *regular* frontier is a nonstarter, even if the other endpoint lies outside it. The word globally is crucial: a frontier closed **only inside an open bridge sector** need not be closed in X, so the theorem cannot be applied without checking its embedding.

**Corollary 1.3 (single-frontier localized Q′ equality).** Suppose \(E\subseteq X^2\) is an **open sublocale** and \(\mathcal D_2(X)\wedge E\) is supported inside \(K\times X\), with K globally closed compact/regular. Then \(\mathcal W_2(X)\wedge E=\mathcal W(X)\wedge E\). Indeed D₂∧E≤K×X and
\[
\mathcal D_2\wedge E=\mathcal D_2\wedge E\wedge(K\times X)
=\mathcal D\wedge E\wedge(K\times X)=\mathcal D\wedge E.
\]
Closure inside the open E commutes with restriction of ambient closure, yielding equality of W₂ and W there. The same holds with the other coordinate restricted to K.

## 2. A noncompact, nonregular, atomless frontier WITH a finite/full fitting defect

Let \(S\) be the completed branching algebraic dcpo
\[
S=\{s:\omega\rightharpoonup2:\operatorname{dom}s\ne\emptyset\},
\]
where finite/infinite domains are allowed and order is extension. The earlier explicit Cantor-regular-open Boolean pair proves
\[
\boxed{\mathcal D_2(S)>\mathcal D(S),\quad
\mathcal W(S)=\mathcal W_2(S)=\mathcal U(S)=S^2.}
\tag{2.1}
\]
(The last equality follows directly because ordinary common-predecessor pairs are dense: two finite partial conditions can be extended by the same fresh singleton condition.)

Define an **exit-prefix dcpo** E. Its elements are all finite or infinite binary words (including the empty binary word \(\epsilon\)), together with **terminal exit words** \(w\dagger\) for every finite binary word w. Order is extension of prefixes, with exit words maximal. Every directed set has a supremum: the union of a chain of finite binary prefixes, possibly an infinite binary word, or a terminal exit already appearing in the set. Every finite binary word and every exit word is compact; hence E is an **algebraic** dcpo with least element \(\epsilon\), so its Scott space is compact.

Let
\[
H=\{\text{finite/infinite binary words, NO terminal marker }\dagger\}\subseteq E.
\]
It is a Scott-closed lower sub-dcpo, itself algebraic with bottom \(\epsilon\). Put
\[
T_n=\bigcup_{\substack{w\in2^{<\omega}\\|w|\ge n}}\{w\dagger\}.
\tag{2.2}
\]
Each T_n is Scott-open, since every exit word is a compact maximal point, and \(T_{n+1}\subseteq T_n\), with
\[
\boxed{\bigcap_nT_n=\varnothing.}
\tag{2.3}
\]

**Lemma 2.1 (exact closed frontier).**
\[
\boxed{\overline{T_n}^{\,E}=H\cup T_n,\qquad
\bigcap_n\overline{T_n}^{\,E}=H.}
\tag{2.4}
\]
*Proof.* Each exit word w† with |w|<n has the singleton open {w†}, disjoint from T_n, so it is outside the closure. Every binary word (finite/infinite) has a Scott neighborhood containing ↑u for some finite prefix u of that word; extend u by a long binary word w of length≥n and then exit at w†. This word belongs to T_n∩↑u. Hence all of H lies in cl T_n. There are no other points. Intersection yields H. QED.

H is **nowhere dense in E**: every nonempty Scott-open has some finite-prefix basic neighborhood and hence contains an exit word. Its closure is itself and its interior is empty.

Now form **the algebraic dcpo**
\[
A=S\times E,\qquad F=S\times H\subseteq A,
\tag{2.5}
\]
with the product Scott topology, which equals the ordinary product topology because both factors are continuous. Let \(U_n=S\times T_n\). Then
\[
\boxed{F=\bigcap_n\overline{U_n}^{\,A},\qquad
\bigcap_nU_n=\varnothing,\qquad
F\text{ is closed NOWHERE DENSE in }A.}
\tag{2.6}
\]
This is a *genuine nonempty closed accumulation frontier* of descending bridge-tail opens, but without any point of infinite exit rank.

**F is noncompact:** its continuous projection onto the noncompact S is surjective. It is **nonregular**: a closed slice \(S\times\{\epsilon\}\subseteq F\) is homeomorphic to S; if F were regular its closed sublocale would be regular, whereas S is nonregular. Its **Booleanization is atomless**: every nonzero open of F contains a basic product ↑s×V, with s finite. Choose a fresh coordinate n outside dom(s), then two disjoint nonempty opens ↑(s∪{n↦0})×V and ↑(s∪{n↦1})×V lie inside it. Their double-negation images remain nonzero and disjoint, so no nonzero regular open is an atom.

**F has a genuine finite/full fitted-diagonal gap:** the closed slice \(K=S\times\{\epsilon\}\) is homeomorphic to S. The Cantor Boolean pair from (2.1) composes with restriction of O(F)→O(K). Every finite F-cover restricts to a finite K-cover, so the pair is finite-cover-compatible, but the infinite singleton-literal cover of K lifts by adding the open complement of K. Hence
\[
\boxed{\mathcal D_2(F)>\mathcal D(F).}
\tag{2.7}
\]

**Yet the closed hulls agree and are total.** The common-predecessor relation in S is dense. E and H have a least element \(\epsilon\). Therefore, whenever s,t∈S share a predecessor p, *any* e,e'∈E share the predecessor \(\epsilon\), so the points (s,e),(t,e') share (p,\epsilon). Such pairs are dense in A² and in F². Every common-predecessor pair is a full D-point; by spatiality of the locally compact sober squares,
\[
\boxed{\mathcal W(A)=\mathcal W_2(A)=\mathcal U(A)=A^2,}
\quad
\boxed{\mathcal W(F)=\mathcal W_2(F)=\mathcal U(F)=F^2.}
\tag{2.8}
\]
The frontier therefore has **all of the desired thinness and intrinsic fitting pathology**, but not a Q′ discrepancy.

### 2.1 Why the frontier is not a construction of a Q′ mixed defect

The previous distributed-supremum Proposition 7.2 bounded \(\mathcal D_2\) on *a special mixed open* by one-coordinate closed frontiers **relative to open bridge sectors**. Our example constructs a frontier sector F with the strongest obvious intrinsic symptoms (noncompact, nonregular, atomless Boolean, and D₂>D), but the ambient A has a **dense common-predecessor relation**, which forces the FULL fitted diagonal to be dense already. There is thus no open mixed E with \(\mathcal D\wedge E=0\) and \(\mathcal D_2\wedge E\ne0\). This is an actual falsification of the tempting inference "such a frontier is nearly a Q′ counterexample."

Importantly, F is **closed in A**, not merely relatively closed inside a bridge wing. The one-sided theorem *does not apply to F itself* because F is neither regular nor compact; nevertheless the older **continuous Scott-domain collapse** still kills Q′ for F. Conversely a *regular* compact perfect Cantor frontier would have the one-sided theorem, so also cannot give the desired mixed defect. Both easy frontier versions are now excluded for distinct reasons.

## 3. Decision criterion: do not chase another receding frontier

The earlier working programme suggested “make the frontier perfect, atomless, nowhere dense” as the next goal. This experiment establishes:

- Perfect/atomless **regular or compact closed** frontier: one-sided fitting rigidity prevents any discrepancy.
- Noncompact **nonregular** atomless nowhere-dense closed frontier: such frontiers exist and can carry a true \(\mathcal D_2>\mathcal D\) defect, but the explicit algebraic example above satisfies \(\mathcal W=\mathcal W_2\) and **full D dense**.
- Relative-closed, not globally closed, frontiers remain logically possible, as do globally closed nonregular frontiers with different order-theoretic incidence. But no evidence yet that either can meet the **full** rectangular certificate for Q′.

**Decision:** The next work should **NOT** be another freely invented decorated bridge variant. To reopen a construction search, require an explicit cover C and a *relatively open part* E of \(\mathcal W_2\) on which
\[
\mathcal D_2\wedge E\ \text{is dense},\qquad \mathcal D\wedge E=0.
\]
Equivalently aim for the earlier exact frame criterion \(r\not\le d_{\mathcal W_2},\, r\wedge w_C\le d_{\mathcal W_2}\) with a disjoint rectangle r. Merely arranging a strange boundary or intrinsic D₂>D is not sufficient.

**Recommendation:** park the current geometric-construction route after this bounded negative test, and turn back to the *intrinsic* pre-nucleus/Boolean-residual criterion (or independent audit of the long chain of recent internal results). Universal Q and Q′ remain open. This recommendation is an explicit anti-drift discipline, not an assertion that Q′ must be true.

**STATUS: internally proved, not independently audited.**
