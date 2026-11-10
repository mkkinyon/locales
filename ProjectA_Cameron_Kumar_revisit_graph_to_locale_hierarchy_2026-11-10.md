# Project A — Returning to Cameron–Kumar: graph dictionary and refreshed relation hierarchy

**10 November 2026 · First revisitation segment.** Primary input: Peter J. Cameron and Vinod Kumar P. B., *Graphs on topological spaces*, arXiv:2610.14783v1, supplied as the original TeX source by the project owner. Specific sections used: §2 (specialization), §3 (five graphs and hierarchy), §4 (products), §6 (finite graph realization), §7 (finite equality classifications), and §8 (Dowker homotopy). We distinguish source theorems from new Project A deductions and future proposals. Existing Project A inputs are recorded in [the master ledger v1.9](ProjectA_master_theorem_ledger_v1_9_2026-11-09.md) and [coherent-composition canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md). This is a working conceptual note, NOT an independent audit or priority claim.

## 1. The original graph dictionary

The article treats simple (irreflexive) graphs but routinely passes to reflexive adjacency by allowing equality. On a topological space X its five graphs are:

| Original graph | Defining ordinary-point relation | Localic counterpart |
|---|---|---|
| Sp (specialization) | \(x\in\overline{\{y\}}\) or \(y\in\overline{\{x\}}\) | Proposed \(\mathcal S=\mathcal A\vee\mathcal A^\smile\) |
| Ins (inseparability) | No disjoint neighborhoods | \(\mathcal I=\operatorname{cl}\Delta\) |
| Cm (closure-meeting) | \(\overline{\{x\}}\cap\overline{\{y\}}\ne\varnothing\) | \(\mathcal D=\operatorname{fit}\Delta\), with ordinary point relation Cm |
| Ury (Urysohn) | No neighborhoods whose closures are disjoint | \(\mathcal U\) |
| Fun (functional) | Every continuous real map identifies x,y | \(\mathcal F\) |

**Convention warning.** Cameron–Kumar use \(x\le_{\mathrm{CK}}y\iff y\in\overline{\{x\}}\), with Alexandrov OPEN sets downsets. Project A uses \(x\le y\iff x\in\overline{\{y\}}\), with Alexandrov OPEN sets upsets. Consequently the labels "common upper" and "common lower" for Ins and Cm reverse. The underlying *topological* graph is unchanged. No claim that arbitrary sublocales are determined by ordinary points is made.

Cameron–Kumar Theorem 3.1 gives
\[
\mathrm{Sp}\subseteq\mathrm{Ins}\cap\mathrm{Cm},\quad
\mathrm{Ins}\cup\mathrm{Cm}\subseteq\mathrm{Ury}\subseteq\mathrm{Fun},
\quad \mathrm{Ins}^{[2]}\subseteq\mathrm{Ury},
\]
and \(\mathrm{Ins}^{[2]}=\mathrm{Ury}\) for Alexandrov spaces. Their §7 characterizes equalities on finite T0 spaces. Section 8 uses Dowker duality on witness complexes, a higher-dimensional structure beyond the binary graphs.

## 2. Restoring specialization as a genuine localic relation

For an **arbitrary** locale X, the canonical *oriented specialization* sublocale \(\mathcal A\hookrightarrow X^2\), already constructed in §4 of [the coherent-composition canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md), is the largest sublocale on which
\[
(\pi_1^*a)|_{\mathcal A}\le(\pi_2^*a)|_{\mathcal A}
\qquad\text{for all }a\in\mathcal O(X).
\tag{2.1}
\]
Put \(\mathcal B=\mathcal A^\smile\). **Provisional notation for discussion**:
\[
\boxed{\mathcal S:=\mathcal A\vee\mathcal B.}
\tag{2.2}
\]
It is reflexive and symmetric. On spectral points it is the reflexive comparability graph, and as a finite join of the two proconstructible spectral relations it is itself proconstructible; arbitrary locale comparability should be interpreted via the *actual sublocale* (2.2), not merely the ordinary points.

**Proposition 2.1 (new short all-locale deduction).**
\[
\boxed{\Delta\le\mathcal S\le\mathcal M=\mathcal I\wedge\mathcal D.}
\tag{2.3}
\]
*Proof.* On \(\mathcal A\), put \(a_1=\pi_1^*a\), \(a_2=\pi_2^*a\), so \(a_1\le a_2\). If \(a\wedge b=0\), then \(a_1\wedge b_2\le a_2\wedge b_2=0\). Hence the complement open of \(\mathcal I=C(d_I)\) vanishes on \(\mathcal A\), and \(\mathcal A\le\mathcal I\).

For any open cover \(\mathcal C\) of X, its diagonal square-cover open \(w_\mathcal C=\bigvee_{c\in\mathcal C}(c_1\wedge c_2)\) restricts on \(\mathcal A\) to \(\bigvee_{c\in\mathcal C}c_1=1\). Hence \(\mathcal A\le O(w_\mathcal C)\) for all covers, so \(\mathcal A\le\mathcal D=\operatorname{fit}\Delta\). The same argument with coordinates reversed gives \(\mathcal B\le\mathcal I,\mathcal D\). Therefore their join \(\mathcal S\) is below \(\mathcal M\). Reflexivity is clear. □

This is a *genuine* extension of the bottom of the Cameron–Kumar diamond: the meet \(\mathcal M\) is not in general the same as specialization.

**Proposition 2.1a (the two hulls of specialization).** For every locale,
\[
\boxed{\operatorname{cl}(\mathcal S)=\mathcal I,\qquad
\operatorname{fit}(\mathcal S)=\mathcal D.}
\tag{2.3a}
\]
*Proof.* Proposition 2.1 gives \(\Delta\le S\le I\) and \(\Delta\le S\le D\). Applying the monotone idempotent closure/fitting operators gives
\(I=\operatorname{cl}\Delta\le\operatorname{cl}S\le\operatorname{cl}I=I\), and
\(D=\operatorname{fit}\Delta\le\operatorname{fit}S\le\operatorname{fit}D=D\). □

**Consequently**
\[
\mathcal S\text{ closed}\iff \mathcal S=\mathcal I,\qquad
\mathcal S\text{ fitted}\iff \mathcal S=\mathcal D.
\]
This explains why the *two lower branches* of the original Cameron–Kumar graph hierarchy can be viewed as two distinct **localic hulls of specialization**, not merely as independent point-set conditions. It is a short formal deduction (indeed any R with \(\Delta\le R\le I\wedge D\) has the same two hulls).

For **finite** upper-Alexandrov posets the original Cameron–Kumar equality classification (§7) reads:
\[
\begin{aligned}
\mathcal S=\mathcal I&\iff\text{every principal downset }\downarrow p\text{ is a chain},\\
\mathcal S=\mathcal D&\iff\text{every principal upset }\uparrow p\text{ is a chain}.
\end{aligned}
\tag{2.3b}
\]
These are stronger conditions than the interval-chain property \(\mathcal S=\mathcal M\) below. In the five-point alternating fence every interval is a chain, so \(\mathcal S=\mathcal M\), while \(\mathcal S\) is neither closed nor fitted; this is a concrete check that the equality with M is a genuinely separate class.

**Proposition 2.2 (finite T0 classification, new deduction).** For a finite poset P in Project A's upper-Alexandrov convention,
\[
\boxed{\mathcal S(P)=\mathcal M(P)
\iff\text{ every order interval }[r,s]=\{x:r\le x\le s\}\text{ is a chain}.}
\tag{2.4}
\]
*Proof.* All sublocales of a finite Alexandrov locale are point-determined. Ordinary points of \(\mathcal I\) are pairs with a common upper bound, and of \(\mathcal D\) are pairs with a common lower bound. If x,y are in \(\mathcal M\), they belong to a common interval [r,s]. If each interval is a chain, they are comparable and hence in \(\mathcal S\). Conversely, if some interval contains incomparable x,y, they share r as lower bound and s as upper bound, hence belong to \(\mathcal M\setminus\mathcal S\). □

The four-point diamond \(0<a,b<1\) is the smallest obstruction, with \((a,b)\in\mathcal M\setminus\mathcal S\). The strict difference is not a pointless phenomenon: it occurs already at the elementary poset level.

**Relation to the source's equality theorem.** Cameron–Kumar §7 states: Sp=Ins iff all point closures are chains; Sp=Cm iff all least open neighborhoods are chains. Under our reversed order convention those two tests exchange "upper/lower." Formula (2.4) is the simultaneous **meet** version: every *interval* must be a chain. It is not a restatement that each principal upset or downset is a chain, which is a different (stronger) assertion.

## 3. Updated universal comparison diagram — core and systematic meet/join levels

The following diagram is a **universal inclusion diagram** for the named primary hulls plus natural meet/join nodes. Each line represents a guaranteed inclusion, not necessarily a strict one, and the diagram is *not asserted to settle all unresolved comparisons* or to encode every possible ordinal/rank approximation. Our new \(\mathcal S\) appears below \(\mathcal M\).

Here
\(\mathcal M=\mathcal I\wedge\mathcal D\),
\(\mathcal J=\mathcal I\vee\mathcal D\),
\(\mathcal T=\mathcal W\wedge\mathcal V=T(\mathcal J)\).
All other auxiliary nodes are spelled out by expressions instead of introducing permanent calligraphic symbols.

~~~mermaid
flowchart BT
  dlt["Δ"] --> S["S = A ∨ A˘"]
  S --> M["M = I ∧ D"]
  M --> I["I = cl(Δ)"]
  M --> D["D = fit(Δ)"]
  I --> J["J = I ∨ D"]
  D --> J
  J --> T["T(J) = W ∧ V"]
  T --> W["W = cl(D)"]
  T --> UV["U ∧ V"]
  W --> HU["H ∧ U"]
  W --> WV["W ∨ V"]
  UV --> V["V = fit(I)"]
  UV --> HU
  V --> WV
  WV --> H["H: least closed & fitted"]
  WV --> UvV["U ∨ V"]
  HU --> H
  HU --> U["U: Urysohn"]
  U --> UvV
  UvV --> HvU["H ∨ U"]
  H --> HvU
  HvU --> F["F: functional"]
~~~

**Checks on the non-obvious edges.** \(J\le W\wedge V\) since \(I,D\le W,V\). Because \(W\le U\), \(W\wedge V\le U\wedge V\), \(W\le H\wedge U\), and \(W\vee V\le U\vee V\). Because \(V\le H\), \(U\wedge V\le H\wedge U\) and \(W\vee V\le H\). All the remaining edges are meet/join definitions or the previously audited universal inclusions.

Caution: this organizes **order implications**, not a claim that nodes are distinct on every locale. Several important examples establish strictness, among them the externally reviewed connected strict diamond
\[
W=H\wedge U<H,U<H\vee U<F.
\]
In coherent locales \(W=U\), whereas noncoherent spaces can have \(W=H<U\), \(W<U=H\), and \(W=H\wedge U\) strict below both.

**Rank/finite-cover overlays (separate, to avoid falsely making them part of one chain).**
\[
D\le D_2\le W_2\le U,\qquad
W\le W_2\le U,
\tag{3.1}
\]
where \(D_2\) is the finite-cover fitted diagonal and \(W_2=\operatorname{cl}D_2\); both Q/Q′ involving W₂ are OPEN and DEFERRED.
\[
I\le V\le V_2\le C(d_2)\le F,\qquad U\le C(d_2),
\tag{3.2}
\]
where the V-n sublocales are rank-bounded fitted upper approximations and \(d_2\) is two-step far-apartness. Other formal iterates, alternation ranks, and relation composites must be recorded in a distinct **process/operation layer**, not silently placed at new inclusion nodes.

## 4. An original graph-equality collapse survives coherence, but not by formal logic alone

The source §7 proves for **finite** spaces that Ins=Cm forces Ury=Fun and all four relations coincide (once loops are adjoined). Our point-free translation gives a useful *precise contrast*.

For any locale, if \(I=D\), the common sublocale is simultaneously closed and fitted, hence automatically
\[
\boxed{I=D=V=W=H.}
\tag{4.1}
\]
However **nothing in this formal argument forces \(U=F\)** in arbitrary locales.

For **coherent** locales the earlier independently audited identity \(W=U\), together with the subsequently externally reviewed coherent implication \(W=H\Rightarrow U=F\), yields
\[
\boxed{I=D\Longrightarrow I=D=V=W=U=H=F.}
\tag{4.2}
\]
The converse classification is \(I=D\iff K(L)\) is both normal and conormal (using the separately checked coherent normality/conormality characterizations of \(D=U\) and \(I=U\)). This is a direct coherent generalization of the finite equality collapse; it needs *both* coherence and the known normal/conormal inputs.

Do not promote (4.1) into a universal \(U=F\) assertion.

## 5. A striking coherent graph-power calculation (NEW deduction)

Let \(\mathcal S=\mathcal A\vee\mathcal B\), where \(\mathcal A\) is the oriented localic specialization relation, \(\mathcal B=\mathcal A^\smile\). For **coherent** locales, the [canonical composition calculus](ProjectA_coherent_composition_canonical_proof_2026-11-08.md) proves that the proconstructible relations \(\mathcal A,\mathcal B,\mathcal I,\mathcal D,\mathcal U,\mathcal V\) are closed under the relevant finite joins and compositions; composition **associates and distributes over finite joins within that class**. It further gives
\[
\mathcal A^2=\mathcal A,\quad\mathcal B^2=\mathcal B,\quad
\mathcal A\mathcal B=\mathcal I,\quad \mathcal B\mathcal A=\mathcal D,\quad
\mathcal I^2=\mathcal U,\quad \mathcal D^2=\mathcal V.
\tag{5.1}
\]

**Theorem 5.1 (new short coherent consequence).**
\[
\boxed{\mathcal S^2=\mathcal J,\qquad
\mathcal S^4=\mathcal U\vee\mathcal V.}
\tag{5.2}
\]

*Proof.* Finite distributivity gives
\[
\mathcal S^2=(\mathcal A\vee\mathcal B)^2
=\mathcal A^2\vee\mathcal A\mathcal B
 \vee\mathcal B\mathcal A\vee\mathcal B^2
=\mathcal A\vee\mathcal B\vee\mathcal I\vee\mathcal D
=\mathcal I\vee\mathcal D=\mathcal J,
\]
because \(\mathcal S\le\mathcal I\wedge\mathcal D\). Then
\[
\mathcal S^4=\mathcal J^2
=(\mathcal I\vee\mathcal D)^2
=\mathcal I^2\vee\mathcal I\mathcal D
 \vee\mathcal D\mathcal I\vee\mathcal D^2.
\]
The [7 November mixed-composition referee](A-mixed-composition-external-audit-reconciliation-2026-11-07.md) established the general inequalities \(\mathcal I\mathcal D\le\mathcal U,\ \mathcal D\mathcal I\le\mathcal U\). Hence the right side is \(\mathcal U\vee\mathcal V\). □

This is **exact localic relational composition**, not just ordinary graph paths. It requires coherence for the distributivity/associativity and the \(I^2=U,D^2=V\) identities; it is NOT claimed for arbitrary locales. It was independently sanity-tested on all 407 naturally labeled posets of sizes 1–5 with order extending a fixed labeling (reflexive transitive suborders of the total order): no counterexample to either equality or the mixed inequalities.

**Graph interpretation.** For finite posets, \(\mathcal S^2\) is the reflexive two-step comparability graph, so \(J=I\vee D\) has a direct *graph-square* meaning. The upper pair \(U\vee V\) is the fourth power of the specialization graph, not an unrelated extra binary relation. The six-point zigzag from our earlier work has \(U\vee V<H=F\), so even fourth graph powers need not recover the closed-and-fitted hull. In coherent locales \(\mathcal H\) is the **patch-closed comparability-saturated completion** of the diagonal, whereas \(\mathcal S^n\) encodes finite graph-distance bounds; infinite paths and patch limits are genuinely relevant.

This brings Cameron–Kumar's path-length viewpoint back into the center of Project A. It also provides a natural test for any future attempt to define graph power analogues of \(\mathcal J\) or \(\mathcal U\vee\mathcal V\) beyond coherence: ordinary localic composition can fail to associate and need not distribute over sublocale joins, so **no unrestricted analogue is inferred**.

## 6. Reinterpretations and candidate directions, not yet new theorems

**The canonical specialization relation is the common source of I and D in coherent locales.** Our proven coherent formulas are
\[
\boxed{
I=A\circ B,\qquad D=B\circ A,\qquad B=A^\smile,
}
\tag{5.1}
\]
with order-convention/orientation as in the canonical proof. This directly echoes Cameron–Kumar §8: their inseparability and closure-meeting *complexes* arise from common witnesses in dual directions, and Dowker duality gives a homotopy equivalence. One potential direction is a **localic common-witness hyperrelation/nerve theory**, recognizing that binary composites may lose information about higher common-witness arity. No simplicial locale or pointfree Dowker equivalence is currently asserted.

**Graph realization.** Cameron–Kumar §6 characterizes finite realizable inseparability graphs by simplicial vertices and realizes every countable graph as part of an inseparability graph of a second-countable T₁ space (§4–5). A localic realization question must distinguish: (a) possible ordinary point graphs of spatial locales; (b) which actual reflexive symmetric sublocales are I,D,U,V,W,H, etc.; and (c) whether a chosen relation admits a cover/Boolean generalized-point presentation. Part (b) is genuinely different, because equal ordinary point graphs can conceal different pointless sublocales.

**Graph paths versus localic relational composition.** The source has \(\mathrm{Ins}^{[2]}\le\mathrm{Ury}\), exact for Alexandrov spaces. Project A proved the internal \(\mathcal I^2\le\mathcal U\), exact for coherent locales, while arbitrary localic composition need not associate. Therefore higher graph powers, distances, and connectivity cannot be imported without specifying parentheses and images.

**Homotopy and invariants.** Cameron–Kumar show that the clique complex of Sp recovers weak homotopy type for finite T0 spaces, and derive Dowker homotopy equivalences between the complexes of inseparable and closure-meeting families. The introduction of S supplies an intrinsic relation whose finite points recover Sp. It does NOT automatically supply a localic clique complex or prove the same homotopy theorem for locales.

## 7. Scope of this first reorientation

New content here is the **provisional notation S**, its all-frame placement \(S\le M\), the **exact hull identities** \(\operatorname{cl}S=I\) and \(\operatorname{fit}S=D\), the finite-poset interval criterion \(S=M\), and the coherent **graph-power identities** \(S^2=J\), \(S^4=U\vee V\). The source theorems on graphs, the coherent A/B composition formulas, and the existing W-phase hierarchy are inherited, with their corresponding source/audit provenance.

This note is a **refreshed diagram and motivational crosswalk**, not a complete new audit or an assertion that every relation-constructor comparison has been decided. The most natural *next bounded study* is to ask exactly how the Dowker common-witness picture interacts with pointfree relational composition, beginning with coherent locales where A/B are already under control, or alternatively revisit finite graph realizability in the language of actual sublocales. Either would return us to the paper's original mathematical purposes rather than extend the Hasse diagram for its own sake.
