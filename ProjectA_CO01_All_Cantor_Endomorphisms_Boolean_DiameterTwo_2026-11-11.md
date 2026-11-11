# CO-01 substantial no-go theorem — all D/V-preserving continuous Cantor maps have Boolean A-diameter two

**11 November 2026. New internally checked theorem (fusion lemma + Baire category), NOT an associativity verdict or external audit.** Strengthens the [homeomorphism and coordinate-injection Boolean probes](ProjectA_CO01_coordinate_injections_two_hop_universal_2026-11-11.md), and is motivated by the [countable clopen endpoint criterion](ProjectA_CO01_regular_fit_topclass_countable_endpoint_tests_2026-11-11.md). It proves that **every Boolean-valued point induced from any continuous Cantor selfmap preserving D,V** admits an actual 2-edge path to any other such point, via a coordinate permutation. Accordingly none of these probes can expose failure of the Arrieta cube base-change surjection, even when the maps are nonlinear, many-to-one or noninvertible.

## 0. Set-up and precise family

Let \(C=2^{\mathbb N}\), \(D=\bigcup_{n\ge1}K_n=\{x:0<|\mathrm{supp}(x)|<\infty\}\), \(V=C\setminus D\), \(B=\mathrm{RO}(V)\), \(q:\mathcal O(V)\to B\). Let \(\mathscr T\) be the monoid of continuous maps \(f:C\to C\) with \(f(D)\subseteq D\) and \(f(V)\subseteq V\). Neither injectivity nor surjectivity is assumed. Each f restricts to a continuous f_V:V→V and yields the Boolean-valued generalized point
\[
h_f=q\circ f_V^*:\mathcal O(V)\longrightarrow B.
\]
The Θ-admissible-cover theorem (proved separately) says
\[
h_f\ A\ h_g\iff
\{d\in D:\max\operatorname{supp}f(d)=\max\operatorname{supp}g(d)\}
\ \text{is dense in }C.
\tag{0.1}
\]

## 1. Fusion lemma: images of one-bit perturbations have unbounded height somewhere in every cylinder

**Lemma.** For every f∈\(\mathscr T\) and every nonempty basic Cantor cylinder U, there is some d∈D∩U such that the sequence
\[
f(d+e_n),\quad n>\max(\mathrm{supp}(d))
\]
has **unbounded heights** \(\max\mathrm{supp}f(d+e_n)\). Here \(d+e_n\) means adjoining one new 1 outside the support of d.

**Proof by contradiction.** Assume every d∈D∩U has those heights bounded. Because f(d+e_n) are in D and D-points of height ≤m form a **finite** set, continuity \(f(d+e_n)\to f(d)\) forces the sequence to be eventually constant equal to f(d). Begin with some d₀∈D∩U. Given d_k∈D∩U, choose n_k larger than the support of d_k, greater than the cylinder depth and all previous n_j, and such that f(d_k+e_{n_k})=f(d_k). Put d_{k+1}=d_k+e_{n_k}. Then all d_k lie in U, all have equal f-value f(d₀), and they converge to an x∈C with **infinite support**. Thus x∈V, but continuity gives f(x)=f(d₀)∈D, contradicting f(V)⊆V. QED.

Note that this is a **uniform category-theoretic obstruction** to locally bounded output-height behavior on all finite-support one-bit extensions. It uses only continuity and preservation of the D/V partition.

## 2. Dense open conditions on the permutation group

Let \(\mathrm{Sym}(\mathbb N)\) carry its Polish pointwise-convergence topology. For f∈\(\mathscr T\) and a basic cylinder U, define
\[
\mathscr U(f,U)=
\bigcup_{d\in D\cap U}
\{\sigma\in\mathrm{Sym}(\mathbb N):
 \max\sigma(\mathrm{supp}d)=\max\mathrm{supp}f(d)\}.
\tag{2.1}
\]
It is **open**: for each d the displayed condition involves only the finite coordinates in supp(d).

It is **dense**: given a basic neighborhood of permutations specified by a finite partial bijection p, take d from the fusion lemma and vary a one-bit extension d+e_n for large n. Their f-image heights \(m_n\) are unbounded. Choose n outside dom(p), the original support of d and the specified input cylinder, with
\[
m_n>\max\big(\mathrm{ran}(p)\cup\{|\mathrm{supp}(d)|+|\mathrm{ran}(p)|+2\}\big).
\]
Extend p by setting \(\sigma(n)=m_n\). For each support position j of d not in dom(p), assign a distinct unused output less than m_n. There are enough such output indices by the lower bound on m_n; the preassigned outputs on supp(d) also lie below m_n. The resulting finite partial bijection extends to a full permutation σ, and for every such extension the maximum of σ(supp(d+e_n)) equals m_n, the height of f(d+e_n). Therefore the basic permutation neighborhood meets \(\mathscr U(f,U)\). QED.

## 3. The theorem, including countable common center

**Theorem.** For **every countable family** \(f_1,f_2,\ldots\in\mathscr T\), there exists a permutation σ∈Sym(N) such that
\[
\boxed{\quad h_{f_i}\ A\ h_\sigma\qquad\text{for every }i.\quad}
\tag{3.1}
\]
Indeed, intersect the countably many dense open conditions \(\mathscr U(f_i,U)\), over all i and all basic Cantor cylinders U, and invoke Baire. For each i, equality of maxima then occurs in every cylinder, hence the coincidence set is dense in C; (0.1) yields h_{f_i} A hσ.

**In particular**, for arbitrary f,g∈\(\mathscr T\),
\[
\boxed{\quad h_f\ A\ h_\sigma\ A\ h_g
\quad\text{with an actual shared Boolean-valued intermediate map }h_\sigma.\quad}
\tag{3.2}
\]
This extends the 7 Nov coordinate permutation theorem to **all** D/V-preserving continuous Cantor selfmaps. It also strengthens the coordinate-injection and coordinate-doubling special examples.

**Cubic source lift consequence.** Suppose a Boolean-valued triple \((h_f,h_g,h_k)\) factors through \(S_L=(A²)_{12}\cap A_{23}\). In particular \(h_g A h_k\). Choose σ from (3.2) for f,g. The quadruple \((h_f,h_\sigma,h_g,h_k)\) is a genuine point of \(E_4=A_{12}\cap A_{23}\cap A_{34}\) over **the same Boolean locale** \(\mathrm{Loc}(B)\), lifting that triple through the source comparison \(\ell:E_4\to S_L\). Reversal gives the analogous result for S_R. Consequently **no Boolean test triple whose coordinates all arise from \(\mathscr T\)** can witness failure of the pullback-stability comparison \(\ell\), nor endpoint asymmetry of the cube.

**Sharp scope:** A general Boolean-valued map \(h:\mathcal O(V)\to B\) need not be of the special form q∘f_V^* for a continuous f:C→C preserving D,V. This theorem does **not** assert that arbitrary Boolean-valued points or all generalized points of the intermediate image lift, and does not settle CO-01.

## 4. The entire Cantor-map Boolean family still does not determine Q on its own

Let \(G_{\mathscr T}=\bigvee_{f,g\in\mathscr T}\operatorname{im}(h_f,h_g)\subseteq Q\). The inclusion is **strict**, already because these Boolean generic tests miss ordinary diagonal points. Fix p∈V and let \(w_p=V²\setminus\{(p,p)\}\), an open of the regular (strongly Hausdorff) localic square. For any f∈\(\mathscr T\), the closed set \(f^{-1}(\{p\})\subseteq C\) is disjoint from dense D, hence nowhere dense. Thus for every f,g the pullback \((f,g)^{-1}(w_p)\) is dense open in V and q sends it to 1. All the images defining \(G_{\mathscr T}\) lie in \(\mathfrak o(w_p)\). But Q contains the ordinary diagonal point (p,p), so \(Q\not\subseteq\mathfrak o(w_p)\). Hence
\[
\boxed{G_{\mathscr T}\subsetneq Q.}\tag{4.1}
\]
This alone does **not** rule out the stronger, more relevant possible generation \(Q\stackrel?=\Delta_V\vee G_{\mathscr T}\), which is currently OPEN and would itself not automatically prove stability after pullback with A. The issue of nongeometric generalized points remains.

## 4. What to investigate next

The next concrete discriminating object is a **Boolean frame map not induced by any continuous D/V-preserving Cantor selfmap**, e.g. a suitably chosen non-geometric endomorphism/automorphism of \(\mathrm{RO}(V)\) composed with q, or a generalized point over a different nonspatial locale. Alternatively, attack the endpoint top-class predicate via the exact countable clopen \(\Theta\)-cover congruences without testing generalized points. Avoid expanding the current Baire proof to merely more coordinate maps: \(\mathscr T\) already contains all continuous partition-preserving maps and has universal 2-hop center at the Booleanized generalized points.
