# Higher meet-hull and sharp connectivity: source-grounded mathematical cold read
## 21 November 2026 · original fourth-audit ZIPs recovered

**Scope and status.** This is a *new focused internal adversarial read*, not a new blind external referee verdict. Sources reopened: user-supplied **C_BLIND_PACKET.md** (10 Nov, in \`C_Referee_Blind(1).zip\`), **AB_BLIND_PACKET.md** (10 Nov, in \`AB_Referee_Blind(1).zip\`), [corrected higher meet-hull canonical](PointFree_binary_meet_hull_CANONICAL_2026-11-11.md) §§0–3 and [fourth-audit final reconciliation](PointFree_audit4_FINAL_RECONCILIATION_2026-11-11.md). Exact C-P1–P6 and A/B-P1–P5 now tabulated in [premise trace](PointFree_ENDGAME_FOURTH_AUDIT_PREMISE_TRACE_2026-11-21.md). The mathematical results were post-verdict proposals **cross-checked by the opposite referee**. We have not freshly verified all of P1–P6 or the entire ∞-topos technology.

## I. The six-point adversarial calculation (fully independent finite check)

Let A={a₀,a₁}, B={b₀,b₁}, C={c₀,c₁} be three disjoint two-element sets. Define two six-element posets
\[
P=A_{\rm anti}\oplus B_{\rm anti}\oplus C_{\rm anti},\quad
Q=A_{\rm anti}\oplus (b_0<b_1)\oplus C_{\rm anti}.
\]
All elements of an earlier block lie below all elements of a later block.

- A finite ordered tuple has a **common upper witness** iff it contains **at most one distinct element of C**; it has a **common lower witness** iff it contains **at most one distinct element of A**. This follows because any non-maximal (resp. non-minimal) element is below a top C (resp. above a bottom A), whereas the two distinct extrema are incomparable with no common upper/lower. Both criteria are **independent of the order on B**. Thus all patched \(I_n\) and \(D_n\) spaces for P and Q, and all degreewise faces/degeneracies, coincide on the common **discrete patch** six-point set. The actual **spectral** order/topology differs; this is **not** an identification of sublocales of the same spectral localic ambient.
- The chain order complexes satisfy \(\mathrm{Ch}(P)\cong S^0*S^0*S^0\cong S^2\), while \(\mathrm{Ch}(Q)\cong S^0*\Delta^1*S^0\) is contractible.
- For \(M_n=I_n\cap D_n\), **inserting b₀** into any permitted tuple remains permitted: it neither adds a new top C nor a new bottom A. The simplicial **extra degeneracy** thus contracts both \(M_\bullet(P)\) and \(M_\bullet(Q)\). Therefore \(\mathbf M(P)\simeq\mathbf M(Q)\simeq1\).
- Independently enumerate nonempty finite-order-complex faces (an allowed simplex is an unordered subset admitting some compatible chain/witness): f-vectors
  \[
  f(\mathrm{Ch}(P))=(6,12,8),\quad
  f(\mathrm{Ch}(Q))=(6,13,12,4),\quad
  f(M(P))=f(M(Q))=(6,13,12,4).
  \]
  The actual lists of I,D,M permitted nonempty subsets agree across P/Q; M is a cone with apex b₀. This check uses elementary finite poset comparisons, *not* the general ∞-topos theorem.

**Conclusion:** This is a genuine small counterexample to recovering chain **2-type** from all patched higher I/D witness spaces. It also proves the **3-connectivity bound is impossible** in general for the chain→M comparison, assuming the general comparison is defined as in the canonical. The displayed 2-connectivity theorem is sharp already on this six-point input.

## II. The groupoid inverse check

Let the chain edge-path groupoid have arrows \([x,y]\) for \(x\le y\), inverse formal edges, degenerate edges as units, and triangles as relations. On an M-edge \((x,y)\), locally choose two simultaneous witnesses \(a\le x,y\le u\). Define
\[
\gamma(x,y)=[x,u][y,u]^{-1}.
\]
The chain triangles \((a,x,u)\), \((a,y,u)\) imply
\[
[x,u][y,u]^{-1}=[a,x]^{-1}[a,y].
\]
This equality works for **every** chosen lower a and upper u. For two witness pairs \((a_1,u_1),(a_2,u_2)\), insert the **mixed** witness \((a_1,u_2)\) to show the two definitions coincide on the **double pullback** of the Stone-surjective witness cover. This proves the proposed arrow **descends to the sheafified** chain groupoid without a globally continuous choice. On M₂ with common witnesses a,u, composition telescopes \(\gamma(x,y)\gamma(y,z)=\gamma(x,z)\); degeneracies map to identities. A chain edge x≤y has witnesses a=x,u=y and is fixed. Conversely \((x,y,u)\) is an M₂ triangle, giving \(\iota\gamma[x,y]=[x,y]\) in the meet groupoid. Thus the proposed functors are mutually inverse, natural **on the source category in which M₂ is preserved**.

**Adversarial boundary:** A map preserving just the binary I and D point relations can fail M₂ preservation, so there is **no** functoriality claim for arbitrary such maps. A binary **isomorphism** is stronger: original fourth-audit C6 reconstructs all patched I_n,D_n, and hence M_n, by compact extremal neighborhoods. C6's proof must be invoked with the **patch topology**, not just abstract graphs.

## III. The sheaf-theoretic 2-connectivity dependency

For each j≥0 form the coherent Priestley object
\[
E_j=\{(a_0,\ldots,a_j;x):a_i\le x\ \forall i\},
\]
where the a-coordinates have equality order and x carries the specialization order. The actual chain and upper-witness nerves on E_j map, degreewise in n, to Ch_n(X) and M_n(X) by **surjective Stone lower-witness projections**; for a tuple with one lower witness a the entire Čech family can take all a_i=a. Their Čech realizations, in the **specified** Stone-sheaf ∞-topos, give
\[
\mathbf C(X)\simeq|j\mapsto\mathbf C(E_j)|,\quad
\mathbf M(X)\simeq|j\mapsto\mathbf I(E_j)|.
\]
At j=0, the lower witness a gives a **simplicial extra degeneracy** on both sides; the map \(\mathbf C(E_0)\to\mathbf I(E_0)\) is an equivalence. For all j, the earlier upper-witness edge/triangle argument makes \(\mathbf C(E_j)\to\mathbf I(E_j)\) **1-connective**, hence at least 0-connective. Apply the standard **realization connectivity lemma**: if f_j is (n−j)-connective for 0≤j≤n, then |f| is n-connective. Here n=2: f₀ is equivalence, f₁ is 1-connective, f₂ is 0-connective. Hence \(\mathbf C\to\mathbf M\) is **2-connective**, meaning π₀ and π₁ isomorphisms and π₂ epimorphism.

**Unverified input explicitly preserved:** the nontrivial ambient work is (a) the **Čech descent** of surjective Stone covers in the precisely chosen site, (b) representing E_j as coherent Priestley spaces with the indicated ordered structure, and (c) the standard ∞-topos connectivity lemma. The original fourth audit accepted these **relative to P1–P6**, and the opposite referee checked the new connectivity argument. The present check verifies that the **displayed construction uses the premises in the claimed direction**, not that it independently re-proves all global site/realization technology. No hypercompleteness or intrinsic localic shape statement has been added.

## IV. Disposition

- **Finite sharpness witness: independently hand-reduced and enumerated in this cold read**; no counterexample to the repaired six-point calculation.
- **Chain↔M groupoid inverse and its witness descent: checked line-by-line at the level of the stated local Stone-surjection and triangle premises.**
- **General 2-connectivity: coherent conditional proof structure**; hinges on well-identified, previously accepted sheaf/Čech and realization-connectivity inputs rather than hidden point-set descent. Not a brand-new formal verification.
- **Original blind C and A/B premise lists: recovered and differentiated; documentation problem fully closed.**

**Recommended editorial use:** prefer the six-point P/Q calculation as the main illustrative *negative result* and the concise groupoid formula as the main *positive theorem*. Retain the precise \(\mathscr H_\kappa\) site in every statement. Do not collapse 1-type recovery and 2-connectivity into a false claim of 2-type reconstruction, or confuse coherent patched point-space equality with equality of localic embeddings across distinct spectral orders.
