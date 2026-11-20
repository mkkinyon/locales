# Explicit finite-fence coordinates — geometric appendix for blind audit

**19 November 2026. Mathematical construction supplied for independent checking.**

## 1. Cantor sets and endpoints

Let

\[
\mathfrak C=\left\{\sum_{j\ge1}\frac{2\varepsilon_j}{3^j}:\varepsilon_j\in\{0,1\}\right\}
\subseteq[0,1]
\]

be the middle-thirds Cantor set. Use three affine copies

\[
K=.1+.1\mathfrak C\subset[.1,.2],\qquad
M=.4+.1\mathfrak C\subset[.4,.5],\qquad
L=.7+.1\mathfrak C\subset[.7,.8].\tag{C1}
\]

Let `C_0` consist of the points of `𝔠` with binary Cantor coding eventually zero and `C_1` the points with coding eventually one. These are disjoint, countable dense subsets of `𝔠`; the representation with ternary digits `0,2` is unique. Define

\[
A=.4+.1 C_0,\qquad B=.4+.1 C_1,\tag{C2}
\]

with arbitrary repetition-free enumerations `A={a_n:n≥1}`, `B={b_n:n≥1}`. Let `f(t)=t-.3` from `M` to `K`, and `g(t)=t+.3` from `M` to `L`. Thus the `P`-endpoints are `(f(a_n),a_n)` and the `Q`-endpoints `(b_n,g(b_n))`. All endpoints are distinct across all components; every nonempty relative Cantor open contains infinitely many endpoints of each colour.

The two fixed gaps are

\[
I_P=(.2,.4),\qquad I_Q=(.5,.7).\tag{C3}
\]

## 2. Recursive fence vertices and order

Fix an enumeration of `ℚ∩(0,1)`. Build the finite fences in the order `P_1,Q_1,P_2,Q_2,…`.

For an edge family with endpoints `u<v` as above and index `n`, let `V_old` be the **finite** set of vertices of earlier fences. Choose an even integer `N=2m≥2` sufficiently large that

\[
\Delta=(v-u)/N<1/(1000n).\tag{C4}
\]

Set `x_0=u`, `x_N=v`. For each `1≤j<N`, choose `x_j` to be the first rational in the fixed enumeration belonging to

\[
\bigl(u+(j-.1)\Delta,\;u+(j+.1)\Delta\bigr)
\setminus(K\cup M\cup L\cup V_{\mathrm{old}}).\tag{C5}
\]

Each band is a nonempty interval, and the excluded set is a closed nowhere-dense set together with finitely many points. These bands are pairwise disjoint and lie between the endpoints. Hence

\[
u=x_0<x_1<\cdots<x_N=v,\qquad
|x_{j+1}-x_j|<1.2\Delta<1/(800n)<1/n.\tag{C6}
\]

Interior vertices avoid the three Cantor sets and every earlier vertex; future endpoints are in the Cantor sets, and future interior choices avoid earlier vertices. Therefore all fences are pairwise vertex-disjoint.

Declare each even-index vertex `x_{2i}` **minimal**, each odd-index vertex `x_{2i+1}` **maximal**, and introduce exactly the strict comparisons

\[
x_{2i}<_{P}x_{2i+1},\qquad
x_{2i+2}<_{P}x_{2i+1}
\quad(0\le i<m).\tag{C7}
\]

Include equality on all of `[0,1]` and no other order pairs. Every strict edge points from a minimal vertex to a maximal vertex; thus the relation is reflexive, antisymmetric, and transitive with **no strict chain of length two**. Each finite fence is exactly one nonsingleton comparability component. Every other point of `[0,1]` is its own component.

Every fence is contained in the Euclidean interval between its endpoints (*segment confinement*).

## 3. Closed partial order and upper topology

The order is closed in the Euclidean square: away from the diagonal, any sequence of strict edges with indices tending to infinity is impossible, since their coordinate distances are bounded by `1/(800n)→0`. The finitely many remaining fence edges form a closed finite set. Therefore the order relation, including the diagonal, is closed.

Let `X` be the locale of upper-open subsets for this order. Standard compact-pospace duality makes `X` stably compact, with patch locale the original Euclidean `[0,1]`; write `p:P_patch→X` for the canonical continuous patch map. **Do not assume that `p` is proper** in the Vermeulen sense.

For Euclidean open `O⊂P`, its upper core

\[
r(O)=P\setminus\downarrow(P\setminus O)
=\{x:\uparrow x\subseteq O\}
\]

is upper-open and Euclidean-open (closedness of the order plus compactness of `P\setminus O`). Thus

\[
U_P=r((.25,.35)),\qquad U_Q=r((.55,.65))\tag{C8}
\]

are genuine nonempty upper opens, with Euclidean closures strictly inside the separate gaps. Nonemptiness follows because each displayed interval contains points outside the countable fence-vertex set, and such singleton points belong to the upper core.

## 4. Uniform traversal and forcing

Every `P_n` runs from `[.1,.2]` to `[.4,.5]` through the entire gap `I_P`, with consecutive Euclidean gaps below `1/(800n)`. Every point of `I_P` is therefore within that distance of some vertex of `P_n`. The same holds for every `Q_n` in `I_Q`; the even-position (minimal) vertices alone also become dense in each fixed gap as `n→∞`.

The uniform `1/800` bound is much smaller than the gap widths, so **every** `P_n`, including early ones, has a vertex in `I_P`, and every `Q_n` has a vertex in `I_Q`.

**Strong forcing lemma.** If `S⊂P` is Euclidean closed, component-saturated, and contains infinitely many distinct nonsingleton fence components, then it contains the whole fence-vertex set `E`.

**Proof.** One colour has infinitely many components. Suppose it is `P`. Their indices tend to infinity. Since all these components traverse `I_P` at mesh tending to zero, closedness of `S` gives `I_P⊂S`. Every `P_m` meets `I_P`; saturation therefore forces **every** `P_m⊂S`. In particular all `a_m∈S`, so density of `A` in `M` and closedness imply `M⊂S`. All `b_m∈M` are now in `S`, forcing every `Q_m⊂S` by saturation. Hence `E⊂S`. The other colour is symmetric, using `I_Q`, `B`, and then `A`. ∎

In particular, the saturation of *any* compact patch-closed `C⊂P` meeting `E` finitely is obtained by adding only finitely many complete fence components: it remains compact, patch-closed, and saturated.

## 5. Quotient point and generic opens

Let `Q` have as its frame of opens all **component-saturated upper opens** of `X`; denote the induced quotient map by `q:X→Q`. The point-generated relation `H_G=[E_G]` has two projections coequalized by `q`. Conversely a frame open equalizing those projections must be constant on each ordinary comparability component, so `q` is precisely their coequalizer.

Let

\[
\mathfrak p_\infty
=\{V\in\mathcal O(Q):q^{-1}V\cap E\ne\varnothing\}.\tag{C9}
\]

The forcing lemma implies that each member of `𝔭_∞` contains all but finitely many complete fences: its closed saturated complement cannot contain infinitely many fences without containing `E`, which would contradict its meeting `E`. Thus the intersection of any two members remains in `𝔭_∞`. Complete primality under joins is immediate because a union meets `E` iff some summand meets `E`.

Hence `𝔭_∞` defines a completely prime point `p_∞` of `Q`. A saturated quotient open contains `p_∞` **iff** it meets `E`; its closed saturated complement then meets `E` finitely. Conversely, an open missing `p_∞` contains **no** fence vertex.

For each ordinary point `x∈P`, its comparability component `C_x` is finite or a singleton, closed and saturated. The complementary quotient-open `P\setminus C_x` belongs to `𝔭_∞` but omits `x`, so `p_∞` is distinct from every ordinary quotient point. Ordinary points `q(x)` and `q(y)` coincide exactly when `x,y` lie in the same finite comparability component (or both equal the same singleton).

The nonspatial generic fibre to be used in the candidate proof is the pullback of the **point sublocale** `G=q^{-1}([p_∞])`. The formula for this fibre as an intersection of finite-cutoff complements is deliberately *not* assumed in this appendix; it is Lemma 1 of the new candidate theorem and should be independently audited.

## 6. Scope

The appendix gives concrete coordinates and proves their compact-pospace, forcing, traversal, quotient-point, and cutoff properties. It does not itself prove the nontrivial Booleanized Cantor-graph composition argument `G×G≤T∘T`: that result is supplied as a separate technical proof input.

For background on compact pospaces and stably compact upper topologies: Jung–Kegelmann–Moshier, *Stably compact spaces and closed relations*, Theorem 2.5, `https://www.brics.dk/NS/01/2/BRICS-NS-01-2.pdf`.
