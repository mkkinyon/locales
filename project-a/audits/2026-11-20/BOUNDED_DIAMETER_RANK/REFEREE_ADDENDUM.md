# Addendum to the independent referee report

**Project A: bounded ordinary diameter and unbounded localic-composition rank**  
**20 November 2026**  
**Subject:** exact rank of the point-generated clique completion, and a general overlap-graph lemma

## 1. A stronger conclusion: the clique-completion rank is exact

There is a substantial improvement to §5 of my independent referee report. I previously obtained

\[
n+2\le r(H_n)\le 2n+2
\]

for every bracketing, without resolving the precise rank when \(n>0\). In fact the **lower bound is always attained**:

> **Theorem.** For the point-generated clique completion \(H_n\) in §7 of `02_STONE_CHAIN_CANDIDATE.md`, every fully parenthesized word of length \(n+2\) equals \(G_n^2\), while no fully parenthesized word of smaller positive length equals \(G_n^2\). In particular,
>
> \[
> \boxed{r_{\mathrm{exists}}(H_n)=r_{\mathrm{all}}(H_n)=n+2\qquad(n\ge0).}
> \]
>
> This **does not** assert associativity of \(H_n\)-composition at shorter lengths.

The lower bound is already proved in §5 of the original referee report. Here is an independent upper-bound proof that uses no spatiality assumption on a product of two nontrivial spatial sublocales.

### Component notation

Let \(E_0,\ldots,E_{n+1}\) be the ordinary connected components of \(D_n\), indexed in chain order, and set

\[
U_j=[E_j]_{G_n},\qquad P_j=[E_j\times E_j]_{G_n^2},\qquad H_n=\bigvee_{j=0}^{n+1}P_j.
\]

Each \(U_j\) is spatial and point-generated, with points \(E_j\). Consecutive component sublocales have nonzero **localic** overlap:

\[
U_j\wedge U_{j+1}\ \supseteq\ Q_j\wedge I_j\ne0
\qquad (0\le j\le n).
\tag{A1}
\]

Ordinary point sets \(E_j\) and \(E_{j+1}\) are nevertheless disjoint.

### The useful induction

Take **any** finite index sequence \(j_1,\ldots,j_k\) satisfying

\[
U_{j_t}\wedge U_{j_{t+1}}\ne0\qquad(1\le t<k),
\tag{A2}
\]

and any full binary parenthesization \(T\) of the word

\[
P_{j_1}\circ P_{j_2}\circ\cdots\circ P_{j_k}.
\]

**Claim:** The resulting relation contains the singleton point edge \(\{x\}\times\{y\}\) for **every** \(x\in E_{j_1}\) and \(y\in E_{j_k}\).

We prove this by induction on the binary tree \(T\). For one leaf the statement is exactly the definition of \(P_j\). For a nontrivial tree, split the word between positions \(t\) and \(t+1\), writing its two subwords as \(L\) and \(R\). By induction, for a fixed point \(x\in E_{j_1}\), the left subword contains **all** point edges \((x,p)\) with \(p\in E_{j_t}\). Since the one-point-legged rectangle \(\{x\}\times U_{j_t}\cong U_{j_t}\) is spatial and point-generated, this gives the *whole* rectangle inclusion

\[
\{x\}\times U_{j_t}\le L.
\tag{A3}
\]

Similarly, fixing \(y\in E_{j_k}\), the right subword contains

\[
U_{j_{t+1}}\times\{y\}\le R.
\tag{A4}
\]

Using (A2) at the splitting position and the verified rectangular-composition lemma,

\[
(\{x\}\times U_{j_t})\circ(U_{j_{t+1}}\times\{y\})
=\{x\}\times\{y\}.
\]

By monotonicity, this edge belongs to \(L\circ R\). That completes the induction, **independently of the shape of the bracketing**.

Crucially, the induction asserts only the presence of all ordinary endpoint-pair edges in each subtree. It does *not* claim that a subtree contains \(U_{j_1}\times U_{j_k}\), which could require an unjustified spatiality assertion.

### Completion in exactly \(n+2\) factors

For arbitrary ordinary points \(x\in E_i\) and \(y\in E_j\), take the sequence of component indices along the path from \(i\) to \(j\) in

\[
0-1-\cdots-(n+1).
\]

It has \(|i-j|+1\le n+2\) vertices. Repeat an index as needed to make a sequence of **exactly \(n+2\)** vertices. Repetition is legitimate because every \(U_i\ne0\) meets itself nontrivially. This sequence satisfies (A2). The claim therefore supplies \((x,y)\) in the corresponding bracketed word of the \(P\)'s. Since \(P_i\le H_n\), monotonicity supplies \((x,y)\) in the prescribed, arbitrarily bracketed \((n+2)\)-factor word of \(H_n\).

Every ordinary point pair of \(G_n^2\) is present. Because the **ambient** \(G_n^2\) is spatial, the entire word equals \(G_n^2\). The lower bound \(k\ge n+2\) from §5 of the original report gives the claimed exact rank.

For orientation, the first cases are \(r(H_0)=2\), \(r(H_1)=3\), and \(r(H_2)=4\).

## 2. General overlap-graph principle

The proof gives a reusable criterion that does not depend on Cantor space.

> **Proposition (point-clique overlap bound).** Let \(G\) be a locale for which \(G^2\) is spatial. Let \(U_1,\ldots,U_m\le G\) be nonzero **spatial** sublocales whose ordinary points collectively exhaust the points of \(G\). Set
>
> \[
> P_i=\bigvee_{x,y\in\operatorname{pt}(U_i)}\{(x,y)\},
> \qquad H=\bigvee_{i=1}^m P_i.
> \]
>
> Form the **localic overlap graph** \(\Lambda\) on \(\{1,\ldots,m\}\), placing an edge \(i-j\) whenever \(U_i\wedge U_j\ne0\). If \(\Lambda\) is connected of ordinary graph diameter \(d\), then **every** fully parenthesized \((d+1)\)-factor word in \(H\) equals \(G^2\).
>
> If, in addition, there are indices \(s,t\) at graph distance \(d\) and ordinary points \(x\in U_s\), \(y\in U_t\) that belong to **no other** \(U_i\), then no word of fewer than \(d+1\) factors equals \(G^2\). Thus both completion ranks equal \(d+1\).

**Proof.** The upper bound is exactly the binary-tree induction in §1, applied to a shortest path of overlap-graph vertices between the supports containing prescribed endpoints; pad the path by repeating a vertex to reach \(d+1\) factors. For the lower bound, expand a word into the **finite** join of bracketed words in the \(P_i\)'s. The source and target of a nonzero such word are supported in its first and last \(U_i\). Moreover any consecutive pair of indices must have nonzero overlap: at the lowest common ancestor of the corresponding adjacent leaves, a zero overlap makes the genuine composability pullback zero. Therefore a summand containing \((x,y)\) would determine a walk from \(s\) to \(t\) of length at most \(k-1\). The private endpoint assumption forces its first and last indices to be \(s,t\), hence \(k-1\ge d\). Finally, a point cannot enter a finite join of sublocales without belonging to a summand. \(\square\)

For \(H_n\) the overlap graph is exactly the path on \(n+2\) vertices, and the ordinary points \(a_0\), \(b_n\) are private to its two endpoints. The general proposition therefore gives \(r(H_n)=n+2\) directly.

The distinction between *ordinary graph components* and *localic overlap of their induced sublocales* is fundamental. The ordinary components of \(H_n\) are disconnected from one another, and each is already a clique; nevertheless their induced sublocales form a connected overlap graph via **pointless** intersections. The latter graph, rather than the ordinary diameter of the former, controls the exact completion length in this construction.

## 3. Editorial consequence

I recommend replacing **both** the original candidate's estimate \(n\le r(H_n)\le3n+4\) and my original report's estimate \(n+2\le r(H_n)\le2n+2\) by the exact equality \(r(H_n)=n+2\), uniformly over all parenthesizations. The rectangular-composition lemma and Isbell-density input already present in the audit packet suffice. No additional locale-theoretic assumptions are required.

This improves, rather than changes, the positive audit verdict. It leaves open the more delicate issue of whether \(H_n\)-composition is associative at **shorter** lengths: equality of all bracketings once they are the full square does not imply general associativity.