# Project A — Testing finite-branch shrinking: coframe proof, negative control, and compact m-apex stars

**9 November 2026 · Working mathematics, internally checked, not externally audited or priority checked.** This tests the finite-branch fittedness mechanism from [the abstract shrinking note](A-W-equals-H-abstract-finite-branch-shrinking-2026-11-09.md), independently of the deferred Q/Q′ questions. We distinguish a genuinely new application (finite star family) from a standard underlying lattice identity (coframe distributivity).

## 1. Shorter lattice proof: decreasing finite joins commute with meets

For any locale Z, its full sublocale lattice \(\operatorname{Sub}(Z)\) is a **coframe**, i.e. finite joins distribute over arbitrary meets. This is standard (Picado–Pultr, *Sublocale sets and sublocale lattices*, Archivum Mathematicum 42 (2006), 409–418). Consequently:

**Lemma 1.1.** In any coframe, for finitely many **decreasing** nets/sequences \(S_{j,n}\), \(1\le j\le m\),
\[
\boxed{
\bigwedge_n\Bigl(\bigvee_{j=1}^m S_{j,n}\Bigr)
=\bigvee_{j=1}^m\bigwedge_n S_{j,n}.
}
\tag{1.1}
\]
For two branches put \(T=\bigwedge_n(A_n\vee B_n)\). Fix k. Since \(A_n\le A_k\) for n≥k,
\[
T\le\bigwedge_{n\ge k}(A_k\vee B_n)
=A_k\vee\bigwedge_{n\ge k}B_n
=A_k\vee B_\infty.
\]
Meet over k and distribute again to get \(T\le A_\infty\vee B_\infty\); the reverse inequality is immediate. Induct on m. Directed-indexed version uses a common upper bound of k and n. **Finite m is essential**: countably many eventually-zero towers in the 2-element Boolean frame give \(\bigvee_j S_{j,n}=1\) for all n.

Since \(O(\bigvee_j r_j)=\bigvee_jO(r_j)\), (1.1) directly proves the finite-branch vanishing lemma from the preceding note:
\[
\bigwedge_n O\!\left(\bigvee_{j=1}^m r_{j,n}\right)
=\bigvee_{j=1}^m\bigwedge_n O(r_{j,n}).
\tag{1.2}
\]
No Boolean-valued generalized points are required for this step.

There is a second standard fact used in the abstract theorem: for **any** sublocale \(S\le Z\) and family of opens \(t_i\in\mathcal O(Z)\),
\[
\boxed{S\wedge O(\bigvee_i t_i)
=\bigvee_i\bigl(S\wedge O(t_i)\bigr).}
\tag{1.3}
\]
**Justification:** restrict the opens to the intrinsic locale S. The frame quotient \(q:\mathcal O(Z)\to\mathcal O(S)\) preserves arbitrary joins, and open sublocales of S respect these joins. Since the embedding \(\operatorname{Sub}(S)\hookrightarrow\operatorname{Sub}(Z)\) preserves joins, (1.3) follows. **Do not derive (1.3) from general frame distributivity of \(\operatorname{Sub}(Z)\)**; it is the special open-restriction identity.

Together, (1.1)–(1.3) give a **direct sublocale proof** of the previous all-frame shrinking theorem: if \(d=\bigvee_i t_i\) and, for each i, open neighborhoods \(w_{i,n}\) of C(d) satisfy
\(t_i\wedge w_{i,n}\le\bigvee_{j=1}^{m_i}r_{i,j,n}\), with finitely many decreasing branches and \(\bigwedge_n O(r_{i,j,n})=0\), then for \(S=\operatorname{fit}(C(d))\),
\[
S\wedge O(t_i)\le
\bigwedge_n O(t_i\wedge w_{i,n})
\le\bigwedge_n O\!\left(\bigvee_jr_{i,j,n}\right)=0.
\]
By (1.3), \(S\wedge O(d)=0\), so \(S=C(d)\). The explicit star-exhaustion condition \(r_{i,j,1}\le\bigvee_n r_{i,j,n}^*\) implies \(\bigwedge_nO(r_{i,j,n})=0\), by restricting to that sublocale and using \(\bigvee_n r_{i,j,n}^*=1\) there but every \(r_{i,j,n}=1\) there.

**Assessment:** the Boolean argument is legitimate, but the central finite-branch identity is *not a novel Boolean phenomenon*; it is a clean coframe fact. The new content of the W application lies in producing appropriate sector/neighborhood/vanishing data.

## 2. Control tests on previously audited examples

**Positive but degenerate: the compact scattered \(\alpha\)-\(\beta\)-\(\gamma\) T₁ example.** Its verified hierarchy is
\[
W=H=I<U=F.
\]
The functional residual \(F\wedge O(d_W)\) is the two-point clopen sublocale consisting of \((\alpha,\gamma)\) and its transpose. Inside F, W is clopen. Set the single sector to the relative open complement of W, take \(w=\mathcal W\) as an **open** sublocale of F containing W, and a single constant-zero branch. The shrinking criterion holds with width 1 and no genuine limit phenomenon. This test confirms the relative-envelope form but yields nothing beyond relative clopenness.

**Negative: the compact noncoherent T₀ \(p<x\), two-sheet example.** Its externally reviewed hierarchy contains
\[
W=I < U=V=H=F,
\]
and the ordinary pair \((x,y)\in H\setminus W\). Thus the fitted hull of W contains an actual point outside W. Every open neighborhood of W contains this point, so on any sector \(t_i\le d_W\) containing it, no shrinking neighborhoods can satisfy the finite-branch nullity required by the theorem. More explicitly: if the hypotheses held, the point would belong to every \(O(t_i\wedge w_{i,n})\), and (1.2) would force this intersection to vanish. The theorem correctly **refuses** this known negative instance. It is a check on discrimination, not a new obstruction.

## 3. A new family: m-ray, m-apex compact spaces (m finite, m≥2)

Let \(m\ge2\) be a finite integer. Let
\[
Y_m=\{o\}\ \cup\ \coprod_{i=1}^{m}R_i,
\qquad R_i=(0,\infty)\times\{i\},
\]
with the standard topology of a finite wedge of \(m\) half-rays, joined at the central point o. Adjoin \(m\) new points \(p_1,\ldots,p_m\). The topology on
\(X_m=Y_m\cup\{p_1,\ldots,p_m\}\) is generated by the open subsets of Y_m and the base neighborhoods
\[
N_i(F)=\{p_i\}\cup(R_i\setminus F),
\quad F\subset R_i\text{ finite}.
\tag{3.1}
\]
Equivalently: each p_i is a cofinite apex on **only** the ith ray; an o-neighborhood contains a small initial interval on every ray; and the ordinary points of each ray have their usual neighborhoods. Intersections of these bases are open, so this defines a topology. Set
\[
u_i=R_i\cup\{p_i\},\qquad
A_i=\overline{u_i}=R_i\cup\{o,p_i\}.
\tag{3.2}
\]
Each u_i is open, and A_i is closed.

**Topology checks.** X_m is compact: any open cover selects at each p_i an open set containing all but finitely many points of R_i; since m is finite, these m sets cover all but finitely many ray points and o, hence a finite subcover exists. X_m is T₁: all singleton complements are open. It is locally compact: a usual compact closed interval about a ray point, a finite truncated compact star about o, and the compact open N_i(F) about p_i supply compact neighborhoods. It is sober: the old Y_m is Hausdorff and open; any closed irreducible containing two old points is reducible by disjoint old opens, whereas a closed set containing at most one old point is finite, hence as a T₁ subspace discrete and reducible unless a singleton. X_m is noncoherent: any small real interval \(J\subset R_i\) contains **no** nonempty compact open subset of X_m (such a subset would be a compact clopen subset of connected noncompact R_i), so the compact opens do not form a basis. Because X_m is locally compact sober, its **localic** square is spatial and equals the ordinary product, and its closed sublocales are point-determined.

## 4. Compute U, W, F in the entire square

Define the closed relation
\[
K_m=\bigcup_{i=1}^{m}A_i\times A_i
\quad\text{(finite union of closed subsets of }X_m^2\text{).}
\tag{4.1}
\]
Let \(P_m=\{(p_i,p_j):i\ne j\}\).

**Claim 4.2 (Urysohn computation).**
\[
\boxed{\mathcal U(X_m)=K_m\ \cup\ P_m.}
\tag{4.2}
\]
This is an equality of **closed sublocales** of the spatial square, not just an unqualified point comparison.

*Proof.* For any two points in A_i, every pair of open neighborhoods has closures meeting at p_i: any nonempty ray-open set accumulates at p_i, o-neighborhoods contain initial ray segments, and p_i-neighborhoods contain p_i. For distinct p_i,p_j, closures of neighborhoods meet at o: each cofinite ray trace accumulates at o. Conversely, for points on distinct rays with at least one **ordinary** noncentral ray point, select for that ray point a bounded interval whose closure stays away from o. Its closure is contained in that ray and its own p_i. On the other side select an appropriate local neighborhood with closure in its own ray, o, and/or p_j, disjoint from the first closure. (When the other coordinate is also an ordinary ray point, take a small bounded interval there; when it is p_j, use N_j(F).) There are no further pairs. Since U is closed and the square spatial, its points determine it. □

The open \(\bigvee_i (u_i\boxtimes u_i)\) lies inside U and has closure K_m because \(\overline{u_i}=A_i\). The universal regular-core inclusion \(\operatorname{cl}(\operatorname{int}U)\le W\) gives
\[
K_m\le\mathcal W.
\tag{4.3}
\]

**Claim 4.3 (exclusion of cross-apex pairs).**
\[
\boxed{\mathcal W(X_m)=K_m.}
\tag{4.4}
\]

*Proof.* Fix i≠j and the **mixed open sector** \(t_{ij}=u_i\boxtimes u_j\). Formula (4.2) implies \(U\wedge O(t_{ij})\) is the one-point open sublocale \(\{(p_i,p_j)\}\) of U. Take the binary open cover
\[
\mathcal C_{ij}=\{X_m\setminus\{p_i\},\ X_m\setminus\{p_j\}\}.
\]
Its diagonal square-cover open \(w_{\mathcal C_{ij}}\) omits (p_i,p_j), so
\[
D\wedge O(t_{ij})\le
U\wedge O(t_{ij})\wedge O(w_{\mathcal C_{ij}})=0.
\]
Since D is dense in W and closure commutes with open restriction,
\(W\wedge O(t_{ij})=0\). The only U points outside K_m are the cross-apex pairs, each contained in its t_{ij}, so the **closed** W lies in closed K_m. Combine with (4.3). □

The complement of K_m has the exact open decomposition
\[
\boxed{d_{\mathcal W}=\bigvee_{i\ne j}(u_i\boxtimes u_j).}
\tag{4.5}
\]

**Claim 4.4 (F is total).** Every continuous real-valued function on X_m is constant. Continuity at p_i forces constancy on the entire ray R_i (a cofinite p_i-neighborhood meets every nonempty real interval), and continuity at o equates these ray constants. Hence
\[
\boxed{\mathcal F(X_m)=X_m^2.}
\tag{4.6}
\]

## 5. Finite-branch test on all mixed sectors

For i=1,...,m and n≥1 put
\[
a_{i,n}=(0,1/n)\times\{i\}\subset R_i,
\quad
C_{i,n}=\{p_i\}\cup([1/n,\infty)\times\{i\}).
\tag{5.1}
\]
The sets C_{i,n} are **closed** in X_m, and \(u_i\setminus C_{i,n}=a_{i,n}\). The closure formula is
\[
\overline{a_{i,n}}=
\{o,p_i\}\cup((0,1/n]\times\{i\}),
\qquad
\bigcap_n\overline{a_{i,n}}=\{o,p_i\}.
\tag{5.2}
\]
Therefore \(a_{i,1}\le\bigvee_n a_{i,n}^*\), which implies
\(\bigwedge_n O(a_{i,n})=0\). The coordinate branches \(a_{i,n}\boxtimes u_j\) and \(u_i\boxtimes a_{j,n}\) inherit Boolean-nullity, or one may apply the same star-test via the rectangle pseudocomplement identity.

For every ordered pair i≠j define the open W-neighborhood
\[
w_{ij,n}=X_m^2\setminus(C_{i,n}\times C_{j,n}).
\tag{5.3}
\]
Then
\[
w_{ij,n}\vee d_{\mathcal W}=1,\qquad
t_{ij}\wedge w_{ij,n}
=(a_{i,n}\boxtimes u_j)\vee(u_i\boxtimes a_{j,n}).
\tag{5.4}
\]
There are \(m(m-1)\) ordered mixed sectors; each is eliminated by **two** decreasing Boolean-null branches, uniformly in n.

The all-frame finite-branch shrinking theorem (or its direct coframe proof in §1) applies. Thus
\[
\boxed{\mathcal W(X_m)=\mathcal H(X_m)=K_m
\subsetneq \mathcal U(X_m)\subsetneq\mathcal F(X_m)=X_m^2
\qquad(m\ge2).}
\tag{5.5}
\]
Moreover, the **specific countable open family** yields an explicit fitted presentation:
\[
\boxed{
\mathcal W(X_m)
=
\bigcap_{\substack{i\ne j\\ n\ge1}}O(w_{ij,n}).
}
\tag{5.6}
\]
For finite m, the set of such pairs (i,j,n) is countable. To prove (5.6), the right-hand side contains W and, by the shrinking calculation, intersects every open sector O(t_{ij}) trivially; since the sectors cover O(d_W) it lies in the closed complement C(d_W)=W.

The example genuinely generalizes the 2-apex topology: for m=2, the old wedge of two positive rays is homeomorphic to the real line, with o identified with 0 and the two rays with positive and negative reals. For m≥3, the old star has a branch point of valence m, so it is not merely the same 2-apex space with renamed points.

**Additional strictness.** Since the square is spatial T₁, \(\operatorname{pt}(\mathcal V)=\operatorname{pt}(\mathcal I)\) (fitting a closed sublocale adds no ordinary points in a spatial T₁ space). For any ray point \(x\in R_i\), \((o,x)\in W\) because both lie in A_i, while \((o,x)\notin I\) because they admit disjoint old-star neighborhoods. Hence
\[
\boxed{\mathcal I\le\mathcal V\subsetneq\mathcal W=\mathcal H
\subsetneq\mathcal U\subsetneq\mathcal F.}
\tag{5.7}
\]
No claim I=V is made.

Also W is not open/clopen in F=whole square: any product neighborhood of (o,o) meets distinct-ray pairs outside K_m. Nor is d_W absolutely rather-below generated, since the diagonal obstruction would force W=U. Thus shrinking is again a genuinely different sufficient mechanism from relative clopenness or relative regular generation.

## 6. Summary of the tests and scope

| Test space | Known/derived W,H outcome | What finite-branch shrinking explains |
|---|---|---|
| Compact scattered T₁ α–β–γ | W=H=I<U=F (external audit) | Only a **width-one, degenerate** criterion inside F; recovers relative clopenness |
| Compact T₀ \(p<x\) with two sheets | W=I<H=U=F (external audit) | **Cannot** satisfy the criterion on the sector containing its ordinary H\\W witness |
| Compact 2-apex T₁ | W=H<U<F (internal earlier calculation) | **Two** shrinking branches, two mixed sectors |
| Compact finite m-apex T₁ (m≥3) | W=H<U<F (new working calculation) | Two branches on each of **m(m−1)** sectors; countable fitted presentation |

**Bottom line.** The general sufficient theorem survives nontrivial tests and controls arbitrarily large *finite* numbers of interacting mixed sectors. It also rejects a known negative example. Its basic finite-branch vanishing law is a standard coframe identity, and its novelty—if any—lies in how we apply that identity to the fittedness of W. No literature-priority claim or external correctness guarantee is made. No further forcing/Q′ programme is opened.
