# Addendum to the independent referee report

**Project A: balanced witness transport and scattered-index localic matrix algebras**  
**21 November 2026**

This addendum records three further deductions that occurred to me *after* writing the independent report. They are additional mathematical observations, not revisions to its verdict. The claims below use the packet's conventions for genuine localic composition and its left-to-right order. None requires the imported rectangular rule (RC).

## 1. The entire relation calculus is insensitive to a scattered index topology

The packet's matrix theorem has a stronger conceptual consequence than the locally finite lifting theorem.

**Proposition (discrete-index comparison).** Let `P` be compact Hausdorff, `K` compact scattered Hausdorff, and `D` the *set* `|K|` equipped with the discrete topology. There are canonical complete-lattice isomorphisms

\[
 \mathsf T_n:\operatorname{Sub}((P\times K)^n)
   \xrightarrow{\ \cong\ }
   \operatorname{Sub}((P\times D)^n),\qquad n=1,2,3,
\]

obtained by retaining every `P^n`-sublocale indexed by a tuple of points of `K`. The induced identification of **all** localic relations (the case `n=2`) preserves:

1. arbitrary joins and meets of sublocales;
2. converse and the diagonal relation;
3. **genuine binary localic relational composition**:
   \[
     \mathsf T_2(R\circ_K S)
       =\mathsf T_2(R)\circ_D\mathsf T_2(S).
   \]

No associativity of unrestricted relation composition is asserted or needed here.

**Proof.** MATn supplies the coordinate descriptions on `P×K`. On `P×D` the same descriptions hold because the discrete-index space is a coproduct of its `P`-fibres (and similarly in powers). The descriptions are complete-lattice isomorphisms. In both spaces, the proof of MUL yields the *identical* formula

\[
 (R\circ S)_{ik}=\bigvee_{j\in |K|}(R_{ij}\circ_P S_{jk}).
\]

On the discrete side this follows directly by decomposing the composability sublocale into the open-and-closed triple-index summands, then applying the join-preserving image; compactness of `P×D` is unnecessary. Converse transposes blocks and diagonal has `Δ_P` in diagonal blocks. This proves each assertion. \(\square\)

Consequently, if `K_1` and `K_2` are **any two** compact scattered Hausdorff spaces whose underlying sets admit a bijection, their complete-lattice-valued localic relation magmas over a fixed `P` are isomorphic (the isomorphism depends on the selected index bijection). In particular, their **entire** genuine relation calculus—not just the finite-support part—cannot detect the topology on the scattered index.

**Compatibility with the packet's generators.** If ordinary subsets of `P×K` are carried to subsets of `P×D` fibre by fibre, the above isomorphism also carries

\[
 p(A,B)=[A\times B],\qquad q(A,B)=[A]\times_{\mathrm{Loc}}[B]
\]

to the corresponding `p` and `q` rectangles on `P×D`. On an `(i,j)` block these are, respectively, `[A_i×B_j]_{P^2}` and `[A_i]_P×_{\mathrm{Loc}}[B_j]_P`; both formulas are preserved under reindexing. Similarly, the point-generated monomial graph associated to `(σ,(h_i))` becomes the graph of the **continuous homeomorphism**

\[
 (p,i)\longmapsto(h_i(p),\sigma(i))
 \quad\text{on }P\times D.
\]

Thus GRP, ACT, and BAL for the full monomial graph group can alternatively be understood by transporting the *ordinary homeomorphism graph calculus on the discrete-index space* through this isomorphism. This gives a conceptual explanation for why discontinuity of `σ` in the compact scattered topology is harmless **as far as relational composition is concerned**.

**Important limit.** This is *not* a homeomorphism or locale isomorphism `P×K ≅ P×D`. It does not transport the distinction between open and closed sublocales or preserve topological closure. The preservation claims are about the **complete sublocale lattice and the specified binary relation operations**. If one uses RC after such a transport, it should be transported as an established identity, not silently re-invoked as a theorem requiring a compact ambient space on the generally noncompact discrete side.

## 2. One-sided finite matrix algebras and a sandwich associativity law

FINMAT imposes both row- and column-finiteness to obtain a converse-closed algebra. **Only one-sided finiteness is needed for associativity of a one-sided matrix algebra.** There is also a useful mixed result.

Let `A(P)` satisfy the algebraic hypotheses of Theorem 6.1. An `A(P)`-valued matrix means an arbitrary localic relation on `P×K` whose every `(i,j)` block belongs to `A(P)`, without any finiteness condition.

**Proposition (one-sided lifts).** The `A(P)`-valued **row-finite** matrices form a unital associative finite-join-distributive algebra under genuine localic composition. The analogous statement holds for **column-finite** matrices. Converse exchanges the two classes, and their intersection is precisely the converse-closed algebra `Mat_rcf(K,A(P))` of FINMAT.

Indeed, every `(i,k)` product entry is a finite join when the *left factor* is row-finite, and the product of row-finite matrices is row-finite. For three row-finite matrices, the fixed-start index paths of length two form a finite set; base associativity and finite distributivity allow rebracketing. The column version is dual.

**Proposition (finite-flank or sandwich associativity).** More generally, let `R,S,T` be arbitrary `A(P)`-valued relations. If **`R` is row-finite and `T` is column-finite**, with no finiteness restriction on the middle factor `S`, then

\[
 \boxed{(R\circ S)\circ T=R\circ(S\circ T).}
\]

For fixed outer indices `(i,ℓ)`, put

\[
 J_i=\{j:R_{ij}\ne0\},\qquad
 L_\ell=\{k:T_{k\ell}\ne0\}.
\]

Both sets are finite. MUL gives

\[
 \begin{aligned}
 ((R\circ S)\circ T)_{i\ell}
 &=\bigvee_{k\in L_\ell}\bigvee_{j\in J_i}
       (R_{ij}\circ_P S_{jk})\circ_P T_{k\ell}\\
 &=\bigvee_{j\in J_i}\bigvee_{k\in L_\ell}
       R_{ij}\circ_P(S_{jk}\circ_P T_{k\ell})\\
 &=(R\circ(S\circ T))_{i\ell}.
 \end{aligned}
\]

Every interchange above is **finite**. There is no assumption of infinitary distributivity and no claim that arbitrary `A(P)`-valued matrices are associative. MAT then upgrades equality of blocks to equality of genuine global localic relations.

This may be useful when a dense middle relation or a global rectangle prevents membership in the row-and-column-finite class. It isolates a larger collection of associative *triple configurations* without claiming a larger associative algebra.

## 3. Compactness of the parameter in MAT appears unnecessary

There is a small, potentially useful generalization of the atomic-index argument. Its proof reveals that one step in MAT uses more compactness than needed.

**Proposition (locally compact Hausdorff version of MAT).** Let `K` be a **locally compact Hausdorff** space. Then the following are equivalent:

1. `K` is scattered;
2. every sublocale of `K` is the join of its singleton fibres;
3. for **every locally compact Hausdorff** space `Z`, the genuine singleton-fibre map
   \[
   \operatorname{Sub}(Z\times K)
      \longrightarrow\prod_{k\in K}\operatorname{Sub}(Z)
   \]
   is a complete-lattice isomorphism, with inverse given by the join of the closed singleton-index fibres.

**Proof sketch.** SPLIT uses only the fact that singleton sectors are closed and their complements open; it does not require compactness. In the scattered direction, `Z×K` is locally compact Hausdorff, and therefore spatial and regular/fit. If the sum `J` of the singleton restrictions is properly below `W`, separate them by an open `O` as in MAT. The nonzero `W'=W∧(X\setminus O)` has a nonempty **ordinary closed** support `L` in the spatial product `X=Z×K`, and `W'` is locally dense in `L`.

Now take the **nonempty subset** `E=pr_K(L)⊆K`. It need **not** be closed: this is where the original argument invoked compactness. But scatteredness says that **every nonempty subset**, not just every closed subset, has an isolated point. Choose `k∈E` and an open `V⊆K` with `E∩V={k}`. The nonempty relatively open part `L∩(Z×V)` is contained in the `k`-sector and must meet the dense sublocale `W'` nontrivially. This contradicts `W'∧J=0`, exactly as in MAT.

For the converse, if `K` is non-scattered, its topology contains a nonempty closed perfect subspace `F` (close a nonempty subspace with no isolated points). Its nonzero least dense Booleanization is invisible to singleton fibres, again as in MAT. The implications `(3)⇒(2)` and SPLIT are unchanged. \(\square\)

The gain is not merely that `Z` may be noncompact: **`K` itself may be noncompact**, provided the spatial locally compact Hausdorff hypotheses are retained. Finite powers of such `K` are again scattered and locally compact Hausdorff, so the same sector method also suggests a locally compact version of MUL and the one-sided/locally finite lifts. I have not attempted to push the statement to arbitrary nonregular locales, where fitness or spatial closed supports would require a different argument.

## Overall suggestion

I would prioritize the **discrete-index comparison** as an explanatory corollary alongside MAT and MUL: it ties the graph-permutation construction, the matrix formula, and the original graph-theoretic motivation into one statement. The **finite-flank law** provides a straightforward strengthening of FINMAT. The **locally compact MAT extension** is a clean scope improvement worth recording, but need not delay consolidation of the compact-Hausdorff results.