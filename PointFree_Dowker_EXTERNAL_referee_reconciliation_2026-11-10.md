# Point-Free Topology Project — Dowker phase external-audit reconciliation

**10 November 2026.** Reconciliation of the independent blind report **“Referee report — Project A C Dowker and higher diagonal phase (blind audit)”** (Claude Fable 5.2, High). The report was prepared without access to [our internal audit](ProjectAC_Dowker_INTERNAL_AUDIT_2026-11-10.md). This reconciliation is a separate subsequent analysis; the referee's report must be retained verbatim. The older **Project A/C** identifiers are historical; the active research program is now one unified Point-Free Topology Project.

## 1. Verdict and provenance

The referee's executive assessment is **“Correct after stated repairs. No numbered claim is refuted.”** It lists **2 major, 4 minor, 7 presentational** items. This independently corroborates the all-locale higher-diagonal frame reconstruction, the bisimplicial Čech equalities, coherent graph-power and hull descriptions conditional on the separately audited spectral calculus, the coherent proper-row result, the frame-cover open-surjection result, and the natural simplicial span.

The internal audit had already flagged the dependence on actual localic images, the meaning of the sheaf ∞-topos statements, and the classical (rather than constructive) reading of nonzero locales over 1. The external report identified three **additional substantive improvements not found internally**: (a) the coherent witness maps fail even ordinary descent, (b) fixed-cover nonface closed tests are not simplicial without meet closure, and (c) the two ∞-topos sites must include **jointly** covering families for the claimed classical simplicial interpretation.

**Status convention:** independent referee review is not proof of publication priority; external acceptance is **after the repairs below**, and dependencies on the coherent proconstructible source remain explicit.

## 2. Referee-origin non-descent strengthening — independently rechecked

Let \(X\) be the countable coherent Priestley locale of the original nontriquotient example, \(q\ge1\), \(E=E_{0,q}(\mathcal A)\), \(B=\mathcal D^{(q+1)}(X)\), \(s=s_q:E\to B\). Take the base points
\[
  y=(d,\ldots,d),\quad y_n=(b_n,c,\ldots,c),\quad
  z=(b_\infty,c,\ldots,c).
\]
Each \(y_n\) has sole common-lower witness \(a\), whereas \(y\) has sole witness \(d\); \(y_n\to y\) in the spectral topology because \(y_n\to z\) in patch and \(y\le z\). Let \(N\hookrightarrow B\) be the spatial sublocale induced by \(\{y\}\cup\{y_n:n\ge1\}\). It is a non-discrete convergent-sequence locale; \(\{y_n\}\) are isolated opens, \(\{y\}\) is not open.

Set \(P=E\times_B N\) with projection \(g:P\to N\). The referee proves that \(P\) is the **discrete** locale on
\[
 T=\{(d;y)\}\cup\{(a;y_n):n\ge1\}.
\]
This conclusion is **not** inferred from its point set. In the frame quotient defining \(P\), write \(V=\bigvee_n\{y_n\}\subseteq B\), \(W=B\setminus\{y\}\), and let \(O\subseteq E\) be the open saying that the witness lies in \(X\setminus\{a\}\). The calculations from the original packet give
\[
 O\wedge s^*V=0,\qquad O\vee s^*W=1,
\]
and \(V|_N=W|_N\). Therefore the classes \(o=[O]\), \(c=[s^*V]\) are complementary in \(\mathcal O(P)\). The part below \(c\) is the powerset frame of the isolated points \((a;y_n)\); the part below \(o\) has only \(0,o\). In the latter, any E-open \(G\le O\) missing \((d;y)\) lies below \(s^*W\) and hence is identified with 0, while one containing \((d;y)\) covers jointly with \(s^*W\) and is identified with \(O\). Thus \(\mathcal O(P)\cong\mathcal P(T)\).

The map \(g\) is epic since \(g^*:\mathcal O(N)\to\mathcal P(T)\) is injective (N is spatial and g is point-bijective). It is monic: if two maps into the discrete \(P\) have the same composite with \(g\), their inverse images of every open singleton \(\{y_n\}\) agree; the complement of the join of these component opens determines the final component. It is not an isomorphism because \(\{y\}\) is not open in \(N\). Thus \(g\) is **monic and epic but not regular epic**. The regular-epi property is necessary for descent and stable under pullback for a descent morphism in a finitely complete category. We conclude:
\[
 \boxed{\forall q\ge1,\ s_q\text{ is not a descent morphism, hence not effective descent or triquotient.}}
\]
I independently checked the quotient-frame argument, monicity/epicity and the descent implication. The refutation uses the established coherent spectral representation of E and B, not merely pointwise calculations. **Provenance: referee-origin theorem, independently rechecked internally; NOT a prior author claim.**

The referee gives a **smaller witness** omitting \(c\): patch space \(\{a,d,b_\infty\}\cup\{b_n\}\), with strict order \(a<b_n\), \(a<b_\infty\), \(d<b_\infty\); take
\[
 y=(d,\ldots,d),\quad z=(b_\infty,\ldots,b_\infty),\quad
 y_n=(b_n,b_{n+1},\ldots,b_{n+1}).
\]
The witnesses are respectively \(\{d\},\{a,d,b_\infty\},\{a\}\). The same proof applies. The claimed Priestley property and limit/witness calculations have been rechecked. The original example remains a valid provenance-preserving proof source.

**Consequence for sheaves:** on any full pullback-closed site of locales containing the objects \(E,B,N\), equipped with a *subcanonical* topology, the representable \(h(s_q)\) cannot be an effective epimorphism; otherwise its pullback \(h(g)\) would be monic and effective epic, hence an isomorphism, contradicting fully faithful Yoneda. Thus the unpatched **specific Čech-descent proof** for the D-side cannot be salvaged by choosing a different subcanonical coverage containing these maps. This does not rule out an entirely different homotopy equivalence of the two simplicial localic hull systems.

## 3. Site repair and the real mathematical content

The patched and frame-cover equivalences are instances of the **internal Dowker lemma**: in any \(\infty\)-topos, a monic relation \(R\hookrightarrow X\times Y\) gives rectangle objects \(E_{p,q}\), effective images \(K_p,L_q\), and a canonical zigzag
\[
 |K_\bullet|\simeq|E_{\bullet,\bullet}|\simeq|L_\bullet|.
\]
Reason: each row/column of E is a Čech nerve of an effective epi, then commute colimits. This is a formal result, not a novel theorem of localic homotopy.

Two **explicit site choices** repair the older conditional wording:
1. **Patched coherent case:** a sufficiently large small skeleton of \(\kappa\)-small Stone locales with **finite jointly surjective covering families** (equivalently suitable compact-Hausdorff surjective copairing covers); taking \(\kappa\) strong-limit above the sizes of the data ensures closure of the constructions. For the patched proconstructible relation, each patched witness map is a cover; representables are sheaves because the covers satisfy effective descent.
2. **Unpatched frame-cover case:** \(\kappa\)-small locales with covering families whose copairing is an **open surjection**; allow arbitrary set-indexed families within the size bound. These are stable, subcanonical covers; each witness map from the open-cover construction is a cover.

In either case the site must contain the relevant pullbacks. A topology with **only singleton surjections** is insufficient to identify the sheaf represented by a discrete locale with the coproduct of its points. Open-surjection and proper-surjection theorems support **subcanonicity**; it is the **chosen coverage** that makes the represented maps effective epimorphisms.

A patched Stone statement recovers the usual pointwise Dowker theorem when appropriately evaluated, but an unpatched cover-nerve realization is only the **constant sheaf object** associated with that simplicial nerve. Do not assert without further work that this realizes intrinsic localic shape or that the constant-object functor is fully faithful. The singleton cover \((1)\) gives the terminal realized object for any nonzero X.

## 4. Closed nonface tests: the simplicial correction

For fixed indexed cover U, the closed tests \(C(b_U^{(n)})\hookrightarrow X^n\) are generally **not stable under coordinate repetition**, even though \(\mathcal I^{(n)}=\operatorname{cl}\Delta_n\) is. Referee's exact counterexample: discrete X=\{1,2,3\}, cover U=\{\{1,2\},\{2,3\},\{1,3\}\}. Every pair of members intersects, so \(b_U^{(2)}=0\), but the triple intersection vanishes. The repetition map \((x,y)\mapsto(x,y,y)\) pulls \(b_U^{(3)}\) back nontrivially at (1,3).

**Repair:** close U under finite meets and add 1. Then any coordinate repetition pulls a zero-intersection labelled rectangle back to another zero-intersection labelled rectangle; coordinate deletion follows by inserting a covering family. Thus the resulting closed test family is simplicial. Such meet-closed families are cofinal under concatenation followed by meet closure, so \(\mathcal I^{(\bullet+1)}\) has the claimed simplicial inverse-limit description **only with this qualification**. In contrast, the fitted tests \(O(w_U^{(\bullet+1)})=L_\bullet(R_U)\) are simplicial for every cover U.

The **degreewise** all-locale reconstruction theorems and the **degreewise** coherent finite-compact-open reductions are unaffected.

## 5. Remaining local repairs and publication scope

- **Proper coherent rows:** explain why changing base tuple \(\mathbf x\) downward while keeping upper witness y fixed stays in E, and justify the closed-locale identity for r via its closed spectral images. The referee checked both.
- **Nonopen coherent column example:** point-image nonopenness alone is not enough; add the Frobenius/left-adjoint argument, or note the stronger non-descent witness.
- **Priestley order-separation list:** add the clopen tails \(\{b_\infty\}\cup\{b_n:n\ge N\}\) separating \(b_\infty\) from c. The older example is sound after that addition.
- **All-locale specialization comparison (new referee observation):** for every locale, \(\Delta_{p+1}\le K_p(\mathcal A)\le \mathcal I^{(p+1)}\) and \(\Delta_{q+1}\le L_q(\mathcal A)\le\mathcal D^{(q+1)}\), so \(\operatorname{cl}K_p(\mathcal A)=\mathcal I^{(p+1)}\) and \(\operatorname{fit}L_q(\mathcal A)=\mathcal D^{(q+1)}\). Actual equality without hulls still needs coherence.
- **Size:** index covers by sets, not a proper class of all indexed families. For the closed hull fixed n, covers of at most n+1 opens suffice. For the fitted hull, set-indexed subfamilies of \(\mathcal O(X)\) suffice. The coherent reduction uses finite **compact opens**, not finite-cover cardinality alone.
- **Conventions/source:** state diagrammatic composition and degree indexing; distinguish original Brun–Fosse–Salbu Set proof from an internal-locale definition. For the ordered-tuple/complex comparison cite Brun–Fosse–Salbu Corollary 6.7. Preserve explicit classical-logic limitations, especially nonzero locale→1 open.
- **Antecedents worth checking at literature stage:** Arrieta–Picado–Pultr diagonal fitting and Arrieta's follow-up; Janelidze–Sobral and Clementino–Hofmann on finite-space descent; Brun–Salbu's earlier rectangle complex; Yoon on profunctors; localic shape. None justifies a priority verdict yet.

## 6. What is and is not now certified

**Independently corroborated, with local repairs:** the principal all-locale frame formulas and Čech identities; the simplicial hulls; coherent specialization graph powers and higher-hull identifications *relative to* the audited coherent prerequisites; proper upper-witness projections; the coherent nonopen/nontriquotient examples; patched and frame-cover two-sided descent *with repaired sites*; the cover-nerve point-free formulas and simplicial span.

**Referee-origin, rechecked:** non-descent of \(s_q\) for every q≥1 in the example; the smaller witness; the all-locale closure/fitting bounds on K,L; meet-closed repair for simplicial closed nonface tests.

**Not established:** a natural equivalence of the **unpatched** higher diagonal simplicial locales; intrinsic shape(X) recovered from one cover; a general localic nerve lemma; stability of geometric realization under the inverse limits; publication priority; general constructive statements beyond the classical assumptions; the referee-unchecked prerequisites on arbitrary localic composition.

The unified project may now progress under themes of separation/relational algebra, higher relations and nerves, and point-free homotopy/shape, without retaining A and C as separate scientific tracks. Keep original filenames, theorem identifiers and independent report verbatim as provenance.

## 7. Disposition / next action

Treat this phase as **externally reviewed subject to the listed repairs**. Preserve the blind report and internal audit as separate records; do not silently rewrite historical notes. Update an editorial theorem ledger or index with the corrections and provenance, then return to exploration only after the repaired canonical statement is available. In particular, cite the referee-origin non-descent result rather than relabeling it as our earlier nontriquotient theorem.