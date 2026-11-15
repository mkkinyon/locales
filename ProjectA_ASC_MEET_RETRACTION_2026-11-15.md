# Project A — Semilattice retractions and nonstable LC-A tests

**Working research note · 15 November 2026.** All new claims below are **internally checked only**, not independently audited. This note supplements [the locally compact frontier note](ProjectA_ASC_LOCALLY_COMPACT_FRONTIER_2026-11-15.md). The general question (LC-A), whether \(\mathcal A(X)\) is spatial for every locally compact sober \(X\), remains open.

## 1. A pointfree monotonicity lemma

For locale maps \(f,g:T\to X\), write \(f\preceq g\) when \(f^*u\le g^*u\) for every \(u\in\mathcal O(X)\). The presented sublocale \(\mathcal A(X)\hookrightarrow X^2\) classifies pairs with \(f\preceq g\).

**Lemma.** If \(h:X^2\to Y\) is any locale map, it is monotone in each variable for this preorder: \(f\preceq g\) implies \(h(f,k)\preceq h(g,k)\), and similarly in the second variable.

*Proof.* An element \(h^*v\in \mathcal O(X^2)\) is a join of pure rectangles \(a_1\wedge b_2\). Replacing \(f^*a\) by \(g^*a\) weakly increases each corresponding term. This establishes the desired inequality for the inverse images of all \(v\). \(\square\)

## 2. Semilattice retraction principle

**Proposition.** Suppose a locale \(X\) has a locale map \(m:X^2\to X\) which is:

1. idempotent, \(m\circ\Delta=\mathrm{id}_X\); and
2. deflationary in both arguments for \(\preceq\): \(m\preceq\pi_1\) and \(m\preceq\pi_2\).

Then \(\mathcal A(X)\) is a locale **retract** of \(X^2\). Consequently, if \(X^2\) is spatial, so is \(\mathcal A(X)\).

*Proof.* Since \(m\preceq\pi_2\), the map \(r=(m,\pi_2):X^2\to X^2\) factors through the presented relation as \(\bar r:X^2\to\mathcal A(X)\).

Write \(i:\mathcal A(X)\hookrightarrow X^2\), and \(f=\pi_1 i,\ g=\pi_2 i\). By definition \(f\preceq g\). Monotonicity of \(m\) in the second argument, followed by idempotence, gives
\[
f=m(f,f)\preceq m(f,g).
\]
The deflationary inequality gives \(m(f,g)\preceq f\). Hence \(m(f,g)=f\) as locale maps (equality of all inverse-image homomorphisms). Thus \(i\bar r i=i\). Since \(i\) is monic, \(\bar r i=\mathrm{id}_{\mathcal A(X)}\), as required. A locale retract of a spatial locale is spatial: distinct opens of the retract remain distinct under the split monomorphism on frames and are distinguished by points of the larger locale. \(\square\)

**Dual version.** If \(j:X^2\to X\) is idempotent and **inflationary** (\(\pi_1\preceq j,\ \pi_2\preceq j\)), then \((\pi_1,j)\) similarly defines a retraction \(X^2\to\mathcal A(X)\).

For a locally compact sober topological **meet-semilattice** whose meet is continuous and whose semilattice order agrees with specialization, the hypotheses hold; the localic square is spatial. The dual statement applies to continuous join-semilattices.

These criteria involve the *actual presented sublocale*, not merely a continuous retraction of its point graph.

## 3. Nonstable Alexandrov example not covered by the local-coherence test

Let \(P=\{c,a,p\}\cup\{g_n:n\in\mathbb N\}\) with the following order and no further comparabilities:
\[
c<a<g_n,\qquad c<p<g_n\quad(n\ge0),\qquad g_{n+1}<g_n.
\]
Equip \(P\) with the Alexandrov upper-set topology.

- **Sober and locally compact.** Every directed subset has a greatest element: if it contains any \(g_n\), choose the one with least index; otherwise it is a directed subset of \(\{c,a,p\}\). Irreducible closed subsets in an Alexandrov space are directed lower sets, so each is the closure of its greatest element. Principal upper sets are compact opens and form a basis.
- **Not stably locally compact.** The compact saturated opens \(\uparrow a\) and \(\uparrow p\) have intersection \(\{g_n:n\in\mathbb N\}\). The ascending cover by \(\uparrow g_n=\{g_0,\dots,g_n\}\) has no finite subcover. Thus the intersection is noncompact.
- **Not locally covered by stable/coherent opens.** The only open containing the bottom element \(c\) is \(P\) itself. Since \(P\) is noncoherent, no open cover of \(P\) by coherent (or stably locally compact) subspaces can exist.
- **Nevertheless \(\mathcal A(P)\) is spatial.** The poset is a meet-semilattice: \(a\wedge p=c\), \(g_n\wedge g_m=g_{\max(n,m)}\), \(a\wedge g_n=a\), \(p\wedge g_n=p\), and meets with \(c\) equal \(c\). The meet is monotone and hence continuous for finite products of Alexandrov spaces. Its order agrees with specialization. Proposition 2 applies.

Therefore
\[
\boxed{\mathcal A(P)\text{ is spatial even though }P
\text{ is locally compact sober, nonstable, and has no stable open cover.}}
\]
This is a positive test independent of the open-cover test in the previous note.

## 4. The referee's noncoherent sequence-tree example is locally coherent

Let \(T=V\sqcup\{p_s:s\text{ finite}\}\) be the sequence-tree space in the [SC+ referee report](project-a/audits/2026-11-15/SCplus/Referee_report_original.md): \(V\) consists of finite and infinite sequences of naturals; for a finite sequence \(s\), \(C_s\) denotes its cone of extensions in \(V\); and
\[
N_{s,k}=\{p_s\}\cup\bigcup_{m>k}C_{s^\frown m}
\]
are compact open neighborhoods of \(p_s\).

The opens \(C_s\) and \(N_{s,k}\) cover \(T\). Each \(C_s\) has the compact-open basis of sub-cones \(C_t\) for \(t\) extending \(s\); finite intersections are empty or a cone.

Each \(N_{s,k}\) has a compact-open basis consisting of:
- \(N_{s,\ell}\) for \(\ell\ge k\);
- cones \(C_t\) with \(t\) extending \(s^\frown m\) for some \(m>k\).

Every \(N_{s,\ell}\) is compact: an open covering \(p_s\) contains a further tail \(N_{s,r}\), leaving only finitely many compact child cones. Intersections of these basis elements are again in the basis or empty. Thus each \(C_s\) and \(N_{s,k}\) is coherent (and sober, being open in \(T\)). By the open-cover lemma,
\[
\boxed{\mathcal A(T)\text{ is spatial}.}
\]
The referee's failure of *global* fittedness of a certain infinite saturated set in \(T\) is compatible with local coherence. It does not obstruct spatiality of \(\mathcal A(T)\).

## 5. A closed-point fiber obstruction

Let \(p:1\to X\) be a point and \(\mathrm{fit}_X([p])=\bigwedge_{p\in u}\mathfrak o(u)\) its fitted hull, the meet of all open sublocales containing it.

**Lemma.** The fiber of \(\mathcal A(X)\to X\) over \(p\), via the first projection, is canonically \(\mathrm{fit}_X([p])\).

*Proof.* For a map \(g:Z\to X\), the pair \((p!,g)\) belongs to the universal relation iff \(p^*u\le g^*u\) for every open \(u\). This precisely says \(g^*u=1\) for each \(u\) containing \(p\), the universal property of the intersection of the corresponding open sublocales. \(\square\)

If \(p\) is **closed**, \(\{p\}\hookrightarrow X\) is a closed sublocale. Hence its pullback along \(\mathcal A(X)\to X\) is closed in \(\mathcal A(X)\). Closed sublocales of spatial locales are spatial. Therefore:
\[
\boxed{\mathcal A(X)\text{ spatial}\Longrightarrow
\mathrm{fit}_X([p])\text{ spatial for every closed point }p.}
\]

This is a **necessary condition**, not a proposed equivalence. The currently tested examples do not violate it.

## 6. Point graph sobriety does not settle LC-A

For every sober topological space \(X\), its specialization graph
\[
G_{\le_X}=\{(x,y)\in X^2:x\le_X y\}
\]
with the subspace topology is itself sober.

*Proof.* Let \(H\subseteq G_{\le_X}\) be irreducible closed. The closures of its two coordinate projections are irreducible closed in \(X\), with generic points \(x,y\). For every open \(u\ni x\), some pair of \(H\) has first coordinate in \(u\), hence second coordinate in \(u\); thus \(y\in u\), proving \(x\le y\). Irreducibility of \(H\) also says that a basic rectangle \(u\times v\) meets \(H\) iff both coordinate inverse images meet \(H\), i.e. iff \((x,y)\in u\times v\). Thus the closure of \(H\) in \(X^2\) is \(\overline{\{(x,y)\}}\), and, since \(H\) is closed in the subspace graph, \(H=\overline{\{(x,y)\}}^{G_{\le_X}}\). Uniqueness follows from \(T_0\). \(\square\)

Thus any negative LC-A example would involve a nonspatial *locale thickening* of an already sober graph; nonsobriety of the graph cannot serve as the obstruction.

## Status and next search

- The stably locally compact theorem (A-SC) remains independently blind-refereed.
- All results in this note are **new internal deductions**, awaiting external audit if elevated.
- We now have two different families of positive nonstable controls: open-locally coherent spaces (including \(T\)) and spaces with continuous meet/join retractions (including \(P\), which cannot have a stable open cover).
- To challenge (LC-A), seek locally compact sober spaces lacking both mechanisms and, especially, test nonspatiality of fitted hulls of closed points or nonspatiality of an appropriate closed first-coordinate fiber.
- No general positive theorem or negative counterexample to (LC-A) is asserted.
