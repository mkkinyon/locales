# Point-Free Topology — Nonconstant canonical-equivalence examples from Stone-indexed pointed face posets

**10 November 2026 · NEW internally checked mathematics; not yet independently externally audited or literature-priority reviewed.** This addresses the next qualitative target proposed in [the mixed Čech / ordinal sum segment](PointFree_mixed_Cech_ordinal_sum_higher_nonconstant_homotopy_2026-11-10.md): produce a coherent locale with \(\mathbf C(X)\to\mathbf I(X)\) and \(\mathbf C(X)\to\mathbf D(X)\) **both canonical equivalences**, whose common sheaf realization is **genuinely nonconstant**. Earlier two-apex and ordinal-sum examples had \(\mathbf I(X)=\mathbf D(X)=1\), with nonconstant homotopy residing only in comparison obstructions. Here the common higher-hull object itself has nonconstant homotopy sheaves.

This note uses the independently blind-checked [canonical coherent chain/hull account](PointFree_coherent_chain_hulls_CANONICAL_2026-11-10.md), especially the finite face-poset crosscut criterion and the edgewise theorem on canonical arrows. Its new family construction and homology calculation are separately **working** and require an independent audit before promotion to the verified theorem ledger.

## 0. Conventions, ambient ∞-topos

Let X be coherent, \(K(X)\) the bounded distributive lattice of compact opens, and \(P_X\) its Priestley patch Stone space, ordered so spectral opens are specialization upsets: \(x\le y\) if every spectral open containing x contains y. Let \(\mathscr H_\kappa\) be a sufficiently large Stone-site sheaf ∞-topos with finite jointly surjective covering families **including the empty cover**, and h:Stone→\(\mathscr H_\kappa\) sheafified Yoneda. The constant-object functor from spaces is \(\underline{(-)}\).

Write \(\operatorname{Ch}_n(X)\hookrightarrow X^{n+1}\) for the coherent specialization chains, \(I_n(X)=\operatorname{cl}\Delta_{n+1}\) for the higher **closed** diagonal hull and \(D_n(X)=\operatorname{fit}\Delta_{n+1}\) for the higher fitted hull. By the audited coherent spectral description, \(I_n(X)\) is the actual proconstructible sublocale of tuples having a common **upper witness**, and \(D_n(X)\) likewise uses a common lower witness. Define \(\mathbf C(X),\mathbf I(X),\mathbf D(X)\) as the geometric realizations of their **patched, represented simplicial objects**. **Not** intrinsic localic shape. The independently refereed edgewise/rectangle theorem identifies the two canonical arrows \((\mathbf C(X)\to\mathbf I(X))\simeq(\mathbf C(X)\to\mathbf D(X))\) under \(\mathbf C(X)\) for every coherent X.

## 1. The Stone-indexed pointed-poset gluing

Fix a **finite nonempty poset P with a chosen minimal point v**, and a nonempty Stone space S. Define the set
\[
W_S(P,v)=\{v\}\ \sqcup\ (S\times(P\setminus\{v\})).
\]
Give it the disjoint-union Stone topology, with all the P\{v} labels finite/discrete. Define the partial order by:
- \((s,x)\le(t,y)\) for nonbasepoint coordinates iff \(s=t\) and \(x\le_P y\);
- \(v\le(s,x)\) iff \(v\le_P x\);
- no \((s,x)\le v\) with \(x\ne v\);
- reflexivity.

The minimality of v prevents any transitive comparison between different fibers: the only shared point is v, with nothing nontrivial below it. The order is closed: comparisons within a fiber are diagonal subsets of S×S multiplied by finite labels, and comparisons involving v are entire clopen S-strata. Priestley separation: for x≰y within the same fiber choose a clopen upscale ↑_P x (minus v) localized to a clopen V⊆S; for s≠t choose V with s∈V,t∉V; to separate v≰(s,x) choose the global clopen upset ↑v, and to separate (s,x)≰v choose a fiberwise localized upset. Thus W_S(P,v) is a compact ordered Priestley space and defines a coherent locale X_S(P,v).

**Explicit frame/algebra description.** Let B=Clop(S), K(P)=Ups(P) (finite bounded distributive lattice). The compact-open lattice is canonically the bounded-lattice pullback
\[
\boxed{
K(X_S(P,v))\cong
\mathrm{LC}(S,K(P))\times_{\mathrm{LC}(S,2)}2,
}
\]
where LC(S,K(P)) consists of continuous/locally constant functions S→finite discrete K(P), the first map sends f(s) to \(\mathbf 1_{\{v\in f(s)\}}\), and 2→LC(S,2) inserts constant functions. Equivalently a spectral compact open is an S-indexed locally constant choice of an upset of P with a *single common choice* whether to contain v. This is a **bounded distributive lattice** formula, allowing the construction to be given completely algebraically. For S=Cantor, B and K(X) are countable.

## 2. Actual simplicial Stone gluing for chain and upper hull

For all n≥0, let \(v_n=(v,\ldots,v)\) denote the constant n-simplex in the finite discrete simplicial sets \(\operatorname{Ch}_n(P)\) and \(I_n(P)\). There are **strictly natural isomorphisms of Stone locales**:
\[
\operatorname{Patch}\operatorname{Ch}_n(X_S(P,v))
\cong 1\sqcup\bigl(S\times(\operatorname{Ch}_n(P)\setminus\{v_n\})\bigr),
\]
\[
\operatorname{Patch}I_n(X_S(P,v))
\cong 1\sqcup\bigl(S\times(I_n(P)\setminus\{v_n\})\bigr).
\]
Proof for chains: if a chain has a coordinate other than v, all its non-v coordinates belong to one common s-fiber, because different fibers are incomparable and v is minimal. Proof for I_n: if a tuple has a common upper witness y≠v, y belongs to a unique s-fiber; every coordinate below y lies in this fiber or equals v. If y=v, all coordinates equal v. Conversely every finite-P tuple with common upper witness s-fiber gives such a tuple in X. All these are actual **proconstructible coherent sublocales**, point-determined after Patch in the audited coherent calculus. For any fixed tuple type with at least one non-v coordinate, the set of parameter s is a patch-clopen **copy of S inside the patch of the sublocale**; the basepoint type v_n is a clopen singleton. Therefore these point-set decompositions are homeomorphisms of the actual patch Stone locales. Simplicial faces/degeneracies either preserve the fiber parameter s or erase the last non-v coordinate and land at the unique collapsed basepoint; this proves strict simplicial naturality and compatibility with the canonical inclusion.

In each degree both objects are the **pushout of Stone spaces along a clopen coproduct summand**:
\[
\begin{array}{ccc}
S\times\{v_n\}&\longrightarrow&S\times\operatorname{Ch}_n(P)\\
\downarrow&&\downarrow\\
1&\longrightarrow&\operatorname{Patch}\operatorname{Ch}_n(X),
\end{array}
\quad
\begin{array}{ccc}
S\times\{v_n\}&\longrightarrow&S\times I_n(P)\\
\downarrow&&\downarrow\\
1&\longrightarrow&\operatorname{Patch}I_n(X).
\end{array}
\]
Because the identified component is **clopen**, h turns each into an actual pushout of sheaves (not an unsupported assertion that representables preserve arbitrary Stone colimits). Geometric realization preserves colimits, and product with h(S) preserves colimits (the \(\infty\)-topos is cartesian closed). The resulting canonical formulas, as **pointed sheaf objects**, are
\[
\boxed{
\mathbf C(X)\simeq1\amalg_{h(S)}
\bigl(h(S)\times\mathbf C(P)\bigr),\qquad
\mathbf I(X)\simeq1\amalg_{h(S)}
\bigl(h(S)\times\mathbf I(P)\bigr).
}
\]
Equivalently \(\mathbf C(X)\simeq h(S)_+\wedge\mathbf C(P)\) and similarly I, where A_+=A⊔1 is pointed and the smash is internal to \(\mathscr H_\kappa\). The canonical map C(X)→I(X) is **exactly** \(h(S)_+\wedge(\mathbf C(P)\to\mathbf I(P))\) with basepoint v.

**Theorem A (Stone-indexed transfer of canonical comparisons).** If the finite pointed poset (P,v) satisfies \(\mathbf C(P)\xrightarrow{\sim}\mathbf I(P)\) canonically, then the coherent X_S(P,v) satisfies
\[
\boxed{\mathbf C(X_S(P,v))\xrightarrow{\sim}\mathbf I(X_S(P,v))
\quad\text{and}\quad
\mathbf C(X_S(P,v))\xrightarrow{\sim}\mathbf D(X_S(P,v))}
\]
**via the canonical arrows** for every nonempty Stone S. The first follows because the pointed smash \(h(S)_+\wedge-\) preserves equivalences; the second is the independently audited coherent edgewise theorem. **Caution:** the D_n simplicial locales need not admit the same fiberwise gluing: different fibers can have a common *lower* witness v; the fitted-side equivalence is supplied by edgewise/Dowker, not by a false pointwise D gluing.

## 3. Concrete circle example and internal homology sheaf

Take \(P=P_1=F(\partial\Delta^2)\), the six-point face poset of a triangle boundary, with v one of its three minimal vertices. Cameron–Kumar's contractible-intersection criterion (with **canonical** strengthening as verified in the independent chain/hull audit) says
\(\mathbf C(P)\xrightarrow{\sim}\mathbf I(P)\xrightarrow{\sim}\mathbf D(P)\) in the appropriate canonical-arrow sense, and \(\mathbf C(P)\simeq\underline{S^1}\) as a **pointed** object. Precisely, the downsets of any subfamily of maximal edges intersect either in a singleton vertex (greatest point), a single principal downset, or the empty set.

Theorem A yields for all nonempty Stone S:
\[
\boxed{
\mathbf C(X_S(P_1,v))\simeq\mathbf I(X_S(P_1,v))
\simeq\mathbf D(X_S(P_1,v))
\simeq h(S)_+\wedge\underline{S^1},
}
\]
where the first two displayed equivalences are the **canonical inclusion maps**.

Let \(\mathbb Z[A]\) be the free abelian sheaf on A=h(S), i.e. the sheafification of T↦\(\mathbb Z[\mathrm{Cont}(T,S)]\), following Commelin–Scholze, *Lectures on Condensed Mathematics*, Prop. 2.5 (https://math.commelin.net/files/LTE.pdf). Because each simplicial degree is \(1\sqcup(S\times(\text{finite nonbasepoint simplices}))\), the pointed, reduced normalized chain complex is
\[
\widetilde C_*(\mathbf C(X);\mathbb Z)\simeq
\mathbb Z[h(S)]\otimes_{\mathbb Z}
\widetilde C_*(\operatorname{Ord}(P),v;\mathbb Z).
\]
The finite P chain complex is chain-homotopy equivalent to \(\mathbb Z[1]\), since \(\operatorname{Ord}(P)\simeq S^1\). Therefore
\[
\boxed{\widetilde{\mathcal H}_1(\mathbf C(X);\mathbb Z)
\cong\mathbb Z[h(S)],\qquad \widetilde{\mathcal H}_i=0\ (i\ne1).}
\]
The homology sheaf has no need for an augmentation kernel: this is a **bouquet** indexed by S, not a suspension of S whose first homology is the *reduced* free abelian sheaf \(\ker(\mathbb Z[h(S)]\to\mathbb Z)\).

**Explicit nonconstancy certificate:** If S is infinite, the element \([\mathrm{id}_S]\in\mathbb Z[h(S)](S)\) pulls back along each point \(s:1\to S\) to the distinct generator \([s]\in\mathbb Z[S_{\rm set}]\). A section over compact Stone S of a **constant** discrete abelian sheaf \(\underline G\) is a locally constant S→G and has finite image. Under any hypothetical sheaf isomorphism, evaluations at points would be identified by the same fixed isomorphism on 1, contradicting the infinite image of \([\mathrm{id}_S]\). Hence \(\mathbb Z[h(S)]\) is **not constant**. Since homology sheaves of constant sheaf-homotopy objects are constant, all three canonically equivalent realizations above are genuinely **nonconstant**.

The object \(h(S)_+\wedge\underline{S^1}\) is **connected**, since its 0-truncation is the pushout \(h(S)\leftarrow h(S)\to1\), which is terminal. Its fundamental-group sheaf cannot be constant: its abelianization is the nonconstant first homology sheaf \(\mathbb Z[h(S)]\). One may go further and identify it with the free group object on h(S) by the internal graph/free-groupoid construction; that identification is a plausible **separate working refinement**, not needed for the main theorem here.

**Not merely a product:** The earlier “cheap” nonconstant examples \(h(S)\times\underline{S^1}\) are disconnected as sheaf objects when S has multiple points; here the copies' basepoints are **identified**, so the total object is connected and its **first homology sheaf itself** is nonconstant.

## 4. Every positive homotopy degree, with canonical comparisons

Let \(m\ge1\), and take \(P_m=F(\partial\Delta^{m+1})\), the face poset of the boundary of an \((m+1)\)-simplex. Choose a vertex v, which is a **minimal** point. Its order complex is the barycentric subdivision of \(S^m\), and the canonical chain-to-upper-hull inclusion is an equivalence by the finite face-poset criterion (nonempty facet intersections are principal downsets with greatest point).

Apply Theorem A:
\[
\boxed{
\mathbf C(X_S(P_m,v))\xrightarrow{\sim}\mathbf I(X_S(P_m,v))
\quad\text{and}\quad
\mathbf C(X_S(P_m,v))\xrightarrow{\sim}\mathbf D(X_S(P_m,v)),
}
\]
with
\[
\boxed{
\mathbf C(X_S(P_m,v))\simeq h(S)_+\wedge\underline{S^m},\qquad
\widetilde{\mathcal H}_m(\mathbf C(X);\mathbb Z)\simeq\mathbb Z[h(S)].
}
\]
Other reduced homology sheaves vanish. For infinite Stone S, the shared homology object is nonconstant by the same \([\mathrm{id}_S]\) certificate.

For m≥2, the pointed object \(h(S)_+\wedge\underline{S^m}\) is internally (m−1)-connected: apply \(\tau_{\le m-1}\), which preserves homotopy colimits and finite products, to its defining pushout; the maps \(h(S)\to h(S)\times\tau_{\le m-1}\underline{S^m}=h(S)\) are equivalences and the resulting pushout is 1. Standard sheaf-internal Hurewicz therefore gives
\[
\boxed{
\pi_m\bigl(\mathbf C(X_S(P_m,v))\bigr)
\cong\mathbb Z[h(S)],\qquad \pi_i=0\ (1\le i<m).
}
\]
For m=1, the realization is connected and its \(\pi_1\) has nonconstant abelianization \(\mathbb Z[h(S)]\); no explicit free-group sheaf identification is required.

Thus **for every m≥1 there exists a coherent locale with both canonical comparisons equivalences but with nonconstant sheaf homotopy in degree m**. For m≥2, this can be taken to be the first nontrivial homotopy sheaf of a (m−1)-connected sheaf object. This is qualitatively different from previous two-apex and ordinal-sum suspensions whose higher hulls were terminal and whose interesting homotopy was solely an obstruction to the canonical maps.

## 5. Internal finite-combinatorial sanity checks

For S a finite discrete set of cardinality k=1,2,3, the resulting pointed poset X_S(P_1,v) has respectively 6,11,16 points. Exhaustive face enumeration of its order complex \(\operatorname{Ord}\), upper witness \(K_{\rm up}\), and lower witness \(K_{\rm low}\) gave F₂ Betti numbers
\[
\begin{array}{c|c|c|c}
k&\operatorname{Ord}&K_{\rm up}&K_{\rm low}\\\hline
1&(1,1)&(1,1,0)&(1,1,0)\\
2&(1,2)&(1,2,0)&(1,2,0,0,0)\\
3&(1,3)&(1,3,0)&(1,3,0,0,0,0,0)
\end{array}
\]
with **zero relative F₂ homology in every degree** for both canonical inclusions \(\operatorname{Ord}\hookrightarrow K_{\rm up},K_{\rm low}\) in all three cases. These are control computations only; the full infinite Stone/sheaf theorem follows from the simplicial pushout and finite-poset canonical comparison.

## 6. What is new, what is standard, and next checks

- **Standard background:** Priestley duality, finite face posets of simplicial spheres, (pointed) order-complex crosscut equivalence (Cameron–Kumar arXiv:2610.14783v1 §9 for abstract types; canonical-map strengthening in our audited work), smash/tensor in an ∞-topos, free abelian condensed sheaves (Commelin–Scholze), internal Hurewicz.
- **Specific working synthesis:** Stone-indexed gluing of a **minimal** vertex in a finite face poset, strict *degreewise* gluing of \(\operatorname{Ch}_n\) and actual \(I_n\) coherent sublocales, transfer of the **canonical** comparison, and an essential nonconstant homology sheaf in the **common** C=I=D realization. No literature-priority claim; new results NOT covered by previous blind packets.
- **Critical asymmetry:** D_n generally does not glue fiberwise because v can be a lower witness for tuples spanning different fibers, but the audited arrow-level edgewise theorem transfers equivalences to D after realization. The localic equality is established only for Ch_n and I_n.
- **Audit priorities:** (i) Priestley separation and actual coherent I_n pushout for every n; (ii) identifying the sheafification of the clopen-summand Stone pushout with its internal homotopy pushout; (iii) the *pointed* naturality of canonical finite comparison; (iv) reduced homology sheaf \(\mathbb Z[h(S)]\), especially the difference from the preceding suspension's \(\ker\varepsilon\); (v) internal connectivity/Hurewicz for m≥2; (vi) no comparison to intrinsic locale shape or literature priority.
- **Next optional step:** compute the free fundamental-group sheaf explicitly (possibly the internal free group sheaf on h(S)), and analyze whether different profinite S are remembered up to homeomorphism by the common realization's homotopy sheaves. Before a new broad exploratory branch, a short internal check of the free-group identification and a targeted audit of the marked proof steps would be appropriate.
