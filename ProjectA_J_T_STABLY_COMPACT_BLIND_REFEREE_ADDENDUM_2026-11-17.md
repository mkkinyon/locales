# Addendum to the independent blind referee report: three further graph-theoretic remarks

**17 November 2026**  
**Companion report:** `ProjectA_J_T_STABLY_COMPACT_BLIND_REFEREE_REPORT_2026-11-17.md`

These remarks arose *after* the report was completed. They use only the graph-theoretic consequences already proved there. In the stably compact setting the conclusions about \(\mathcal J\) and \(\mathcal T\) also describe the actual spatial perfect sublocales via their supports. The statements about transitivity below concern **ordinary binary relations on points**, not any unverified claim about localic relational composition.

## 1. Eight points are necessary for a nonempty distance-four fringe

**Proposition.** Let \(P\) be any poset and \(G\) its undirected comparability graph. If \(d_G(x,y)=4\) and \((x,y)\in\mathcal T\), then there are **two internally vertex-disjoint geodesics of length four** from \(x\) to \(y\). Consequently:

1. \(P\) contains at least **eight distinct elements**.
2. \(G\) contains **two vertex-disjoint triangles**, one containing \(x\), the other containing \(y\).
3. The packet's eight-element example is **minimal in cardinality** among posets with a distance-four pair belonging to \(\mathcal T\).

**Proof.** The alternating-orientation characterization from the packet supplies geodesics

\[
x>u<z>v<y,\qquad x<r>t<s>y.
\]

The first-step vertices \(u\ne r\), since one is below \(x\) and the other above it. Similarly \(v\ne s\), since one is below \(y\) and the other above it.

The middle vertices also differ: if \(z=t\), then \(v<z=t<r\), so

\[
x<r>v<y
\]

would be a three-edge comparability path, contradicting \(d_G(x,y)=4\). The vertices at distance one, two, and three from \(x\) cannot coincide across those different distance levels. Thus \(u,r,z,t,v,s\) are six distinct internal vertices, all different from \(x,y\). This gives at least eight vertices overall, and the two exhibited paths are internally disjoint.

Moreover \(u<x<r\), so \(u,x,r\) form a triangle in \(G\). Similarly \(v<y<s\) gives the triangle \(v,y,s\). These triangles are vertex-disjoint by the distance-level argument. The eight-element example in the packet realizes the configuration, proving sharpness. \(\square\)

**Comment.** This means that the appearance of exactly eight elements in the packet's example is not an accident. The example is a cardinality-minimal witness to the distance-four phenomenon, though I make no uniqueness claim for such examples.

## 2. A clean class in which \(\mathcal T=G^3\)

**Corollary.** If the comparability graph of \(P\) contains no pair of **vertex-disjoint triangles**, then

\[
\boxed{\mathcal T=G^3}
\]

as point relations. In particular this holds if the poset has height at most two (equivalently, if its comparability graph is triangle-free), or if \(|P|\le7\).

**Proof.** The theorem already gives \(G^3\subseteq\mathcal T\subseteq G^4\). By Proposition 1, a pair at distance exactly four in \(\mathcal T\) would force two vertex-disjoint triangles, contrary to the hypothesis. Thus there is no distance-four fringe. \(\square\)

The condition is sufficient, not necessary: a graph may contain disjoint triangles and yet have no distance-four pair in \(\mathcal T\). This observation may be useful for familiar classes of finite posets, and it gives an immediate explanation of why the five-point fence satisfies \(\mathcal T=G^3\) but not \(\mathcal T=G^4\).

## 3. Transitivity of \(\mathcal J\) and \(\mathcal T\) on points

Let \(E_G\) be the equivalence relation “belongs to the same connected component of \(G\).” A simple observation applies to any reflexive symmetric point relation \(R\) with

\[
G\subseteq R\subseteq E_G:
\]

**\(R\) is transitive if and only if \(R=E_G\).** Indeed, transitivity and containment of every edge force all finite graph paths to belong to \(R\); the converse is immediate.

Apply this to \(R=\mathcal J=G^2\). Using the diameter criterion from the packet gives the additional equivalence

\[
\boxed{
\mathcal J\text{ is transitive on points}
\ \Longleftrightarrow\
\mathcal J=\mathcal T
\ \Longleftrightarrow\
\text{every comparability component has diameter at most }2.}
\]

Thus the fixed-point criterion for \(\mathbf T\) can be described in familiar graph-theoretic language: **the two-step comparability relation is already an equivalence relation.**

Similarly, \(\mathcal T\) is transitive on points if and only if it fills every connected component. Equivalently, every component must have diameter at most four **and** every distance-four pair must satisfy criterion (8). The four-point fence illustrates that \(\mathcal J\) need not be transitive even when \(\mathcal T\) is: its graph has diameter three, so \(\mathcal T=E_G\) while \(\mathcal J\ne E_G\). The five-point fence shows that \(\mathcal T\) itself need not be transitive.

This last observation should be kept explicitly at the **point-relation level**. It does not assume associativity of localic relation composition or identify pointwise transitivity with a localic transitivity axiom.

## Final comment

Of these remarks, I consider the **eight-vertex minimality and the two vertex-disjoint triangles obstruction** the most interesting. They sharpen the packet's graph picture without altering the localic proofs, and they suggest that the eight-element construction is a natural small configuration rather than an arbitrary example.
