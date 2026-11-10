# Project A — Dowker witness maps: triquotiency fails coherently in every positive degree

**10 November 2026. New internally checked working theorem; NOT externally audited.** Continuation of [bisimplicial Čech/patch descent](ProjectA_Dowker_bisimplicial_Cech_patch_descent_2026-11-10.md). Terminology: \(\mathcal A\) is the oriented specialization sublocale of a coherent locale \(X\), with \(x\le y\iff x\in\overline{\{y\}}\). Spectral opens are upward closed. \(s_q:E_{0,q}(\mathcal A)\to L_q(\mathcal A)=\mathcal D^{(q+1)}(X)\) forgets the common *lower* witness \(x\le y_i\).

## 1. Triquotient criterion

Plewe (1997) defines a localic triquotient assignment for \(f:E\to B\) as a map \(f_\#:\mathcal O(E)\to\mathcal O(B)\) preserving directed joins and satisfying

 \(f_\#(u\wedge f^*v)=f_\#(u)\wedge v,\qquad f_\#(u\vee f^*v)=f_\#(u)\vee v.\)

In particular \(f_\#0=0\), \(f_\#1=1\), and \(f_\#f^*=\mathrm{id}\). Such maps are effective descent and pullback-stable (Plewe's theorem). Plewe's filtered-inverse-limit preservation theorem includes compatibility hypotheses on stage assignments; do NOT invoke it merely from finite approximations.

## 2. Positive cases

- **All locales, \(q=0\)**: \(s_0:\mathcal A\to X\) has the diagonal section \(x\mapsto(x,x)\), hence is triquotient (take section inverse image as \(s_{0\#}\)).
- **Finite Alexandrov coherent locales, all \(q\)**: \(s_q\) is open surjective. If \((x,\mathbf y)\) is in \(E_{0,q}\) and \(\mathbf y'\ge\mathbf y\) coordinatewise, keep witness \(x\) to lift the generalization; finite upper-Alexandrov maps satisfying this are open. Such maps are localic triquotients.

## 3. Counterexample for every \(q\ge1\)

**Theorem (new).** There exists one countable coherent locale \(X\) for which *every* \(s_q\) (\(q\ge1\)) fails to be a localic triquotient.

**The Priestley space.** Let \(P=\{a,d,c,b_\infty\}\cup\{b_n:n\ge1\}\) with Stone topology where \(b_n\to b_\infty\) and \(a,d,c\) are isolated. The strict order consists exactly of

 \(a<b_n\ (n\ge1),\quad a<b_\infty,\quad a<c,\quad d<b_\infty,\quad d<c.\)

There are no further nonreflexive comparisons. This is a Priestley space: the order is patch closed, including the sole nonconstant limiting comparisons \((a,b_n)\to(a,b_\infty)\). Order-separating clopen upsets exist: the isolated maximal points \(b_n,c\), tails of the \(b_n\) including \(b_\infty\), the clopen upset \(\uparrow a=P\setminus\{d\}\), and the clopen upsets \(\{d,c,b_\infty\}\cup\{b_n:n\ge N\}\) for each \(N\). These separate every point pair \(x\nleq y\). Hence the topology of patch-open upsets is spectral, giving a coherent \(X\).

For \(q\ge1\), let \(B_q=L_q(\mathcal A)=\mathcal D^{(q+1)}(X)\). The coherent higher-diagonal hull theorem gives its patch point set as tuples with a common lower bound. Put

 \(y=(d,d,\ldots,d),\quad z=(b_\infty,c,\ldots,c),\quad y_n=(b_n,c,\ldots,c).\)

All belong to \(B_q\). In product order \(y\le z\); in patch topology \(y_n\to z\). Therefore \(y_n\to y\) in the spectral topology of \(B_q\). Witness fibers: the unique common lower witness of \(y\) is \(d\), while the unique common lower witness of each \(y_n\) is \(a\). (At \(z\), witnesses include both \(a,d\).)

Let \(U=P\setminus\{a\}=\{d,c,b_\infty\}\cup\{b_n:n\ge1\}\), a patch-clopen upset and thus a compact spectral open. Let \(O\subset E_{0,q}\) be the spectral open given by requiring witness \(x\in U\). Then \(O\) contains the *entire* fiber over \(y\), and misses the fibers over every \(y_n\).

**Purely localic contradiction.** In \(B_q\), the point \(y\) is minimal and patch-isolated, so the singleton \(\{y\}\) is a closed sublocale. Put \(W=B_q\setminus\{y\}\), its open complement. Since the fiber of \(y\) lies in \(O\),

 \(O\vee s_q^*(W)=1_{E_{0,q}}.\)

Suppose \(s_{q\#}\) is a triquotient assignment. Applying its second Frobenius identity gives

 \(1=s_{q\#}1=s_{q\#}(O)\vee W,\)

hence \(y\in s_{q\#}(O)\). For every \(n\), the singleton \(V_n=\{y_n\}\) is a compact spectral open of \(B_q\), since \(b_n,c\) are isolated maximal points. As \(O\wedge s_q^*V_n=0\), the first Frobenius identity implies

 \(s_{q\#}(O)\wedge V_n=s_{q\#}0=0.\)

Thus the spectral open \(s_{q\#}(O)\) contains \(y\) but none of the \(y_n\), impossible because \(y_n\to y\). QED.

The same construction witnesses failure of the *point-set* biquotient condition: the single open \(O\) covers the fiber over \(y\), but the image \(s_q(O)\) contains no neighborhood of \(y\). The localic proof is independent of any topological-to-localic implication.

### Boundary and interpretation

- Coherence, compactness, spatiality, and proconstructibility do not force the lower-witness maps to be triquotient.
- The higher-dimensional and patched Čech constructions remain valid.
- This does **not** by itself show that the maps fail to be effective descent in \(\mathbf{Loc}\), nor does it rule out all possible homotopy comparisons of unpatched simplicial locales.
- Plewe's filtered-limit theorem cannot be applied automatically to the finite spectral approximants because it requires compatible triquotient assignments or alternative conditions.
- The counterexample has only one convergent sequence, three isolated extra points, and works in all degrees \(q\ge1\).

## 4. Research disposition

The most direct hope for an *unpatched* proof of localic Dowker equivalence — proper row resolutions together with triquotient column resolutions — is false for coherent locales in general. A useful bounded positive next direction is to find structural hypotheses on \(X\) ensuring the common-lower witness projections are triquotient (e.g. finite Alexandrov, a continuous lower-witness section, or local proper/open witness selections). Otherwise keep the already proved patch-sheaf Dowker equivalence as the unconditional coherent result.

**Literature:** Till Plewe, *Localic triquotient maps are effective descent maps*, Math. Proc. Camb. Phil. Soc. 122 (1997), 17–43, DOI 10.1017/S0305004196001648; Vickers's formulation of the two Frobenius identities; coherent proconstructible calculus [canonical proof](ProjectA_coherent_composition_canonical_proof_2026-11-08.md). Novelty/prior art not checked.