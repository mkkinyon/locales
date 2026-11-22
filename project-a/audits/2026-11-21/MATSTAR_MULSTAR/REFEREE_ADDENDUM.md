# Addendum to the independent MAT*/MUL* referee report

**Date:** 21 November 2026  
**Companion document:** `INDEPENDENT_REFEREE_REPORT.md`  
**Scope:** Additional mathematical observations arising from the submitted statements and their proofs. These are not claims of historical originality, and none changes the positive verdict on MAT*, MUL*, or FINMAT*.

## 1. MAT* is hereditary to *arbitrary subspaces* of an admissible index

The locally compact hypothesis in MAT* is sufficient, but the established theorem immediately yields examples **outside** the locally compact class, with no new transfinite induction.

**Proposition.** Let \(K\) be locally compact, scattered, and Hausdorff, and let \(B\subseteq K\) be **any topological subspace** (not necessarily open, closed, or locally compact). Then for every locale \(P\), singleton-sector restriction gives a complete-lattice isomorphism
\[
\operatorname{Sub}(P\times B)\ \cong\ \prod_{b\in B}\operatorname{Sub}(P).
\tag{A1}
\]
Moreover the genuine binary multiplication formula and the finite-support corollary hold with \(B\) in place of \(K\).

**Proof.** Since \(K\) is Hausdorff, \(B\) is Hausdorff (hence sober). The subspace inclusion \(B\hookrightarrow K\) induces a sublocale embedding, as does its pullback \(P\times B\hookrightarrow P\times K\). Sublocales of \(P\times B\) are precisely the sublocales of \(P\times K\) lying below \(P\times B\).

Under MAT* for \(K\), the sublocale \(P\times B\) has coefficient \(P\) at each \(b\in B\) and coefficient \(0\) at each \(k\notin B\). Indeed, these are the pullbacks of the subspace inclusion along the point-index sectors. Hence the order interval below \(P\times B\) is exactly
\[
\prod_{b\in B}\operatorname{Sub}(P)\times
\prod_{k\in K\setminus B}\{0\},
\]
which proves (A1). For multiplication, apply the same argument to the finite powers. Here one should check a small categorical point: the **localic** power of \(B\) embeds in the localic power of \(K\), and its point-index support is precisely \(B^n\); by MAT* for \(P=1\) on \(K^n\), it agrees with the subspace sublocale indexed by the ordinary topological \(B^n\). Thus the sector argument genuinely applies to the localic products used in composition. Repeating the MUL* image calculation proves the multiplication formula for \(B\); FINMAT* follows in turn. \(\square\)

This extension is genuinely broader than both the locally compact statement and the finite-Cantor–Bendixson-height weakening mentioned in the original report. For instance, take the compact scattered ordinal \(K=[0,\omega^\omega]\), and remove the points \(\omega,2\omega,3\omega,\ldots\). The resulting \(B\) is not locally compact at \(\omega^2\): every neighborhood there contains tails of sequences converging in \(K\) to removed points, so it cannot lie in a compact subspace of \(B\). Meanwhile \(B\) retains a tail with unbounded finite Cantor–Bendixson ranks. Nevertheless (A1) and its relation-composition consequences hold.

**Limit of the observation:** this does not prove MAT* for every scattered Hausdorff space; it proves it for spaces that embed as subspaces of a locally compact scattered Hausdorff space.

## 2. A general indexed formula for localic pullbacks and images

MUL* can be viewed as one instance of a more general *fiberwise pushforward* principle.

**Proposition.** Let \(P',P\) be arbitrary locales; let \(K',K\) be locally compact scattered Hausdorff spaces (or index spaces covered by §1); let \(f:P'\to P\) be any locale map and \(h:K'\to K\) any continuous map. Write \(F=f\times h\). For \(V\le P'\times K'\) and \(W\le P\times K\), MAT* identifies sublocale pullback and smallest-sublocale image with
\[
\boxed{\bigl(F^{-1}W\bigr)_{k'}
       = f^{-1}\bigl(W_{h(k')}\bigr),}
\tag{A2}
\]
\[
\boxed{\bigl(F_!V\bigr)_k
       = \bigvee_{\,k'\,:\,h(k')=k} f_!\bigl(V_{k'}\bigr).}
\tag{A3}
\]
Here \(f^{-1}\) means pullback of **sublocales**, \(f_!\) is the left-adjoint sublocale image, and an empty fiber gives the zero sublocale.

**Proof.** Formula (A2) follows from functoriality of pullback and the equality of maps
\[
(f\times h)\,i_{k'}=i_{h(k')}\,f
\]
for the singleton-sector inclusions. Formula (A3) then follows *formally by adjunction*: \(F_!V\le W\) if and only if \(V\le F^{-1}W\), if and only if, for every \(k'\),
\(f_!(V_{k'})\le W_{h(k')}\). Grouping these inequalities by \(k\) gives precisely (A3). Alternatively, use MAT* to decompose \(V\) into its sectors, then preserve their join under image and use functoriality of image. \(\square\)

In particular, take \(P'=P^3\), \(P=P^2\), \(K'=K^3\), \(K=K^2\), \(f=\pi_{13}^P\), and \(h(i,j,k)=(i,k)\). Then (A3) reads
\[
\bigl((\pi_{13})_!Q\bigr)_{ik}
   =\bigvee_j(\pi_{13}^P)_!(Q_{ijk}),
\]
which is exactly the image-assembly step in MUL*. The composability pullback still has to be taken **before** using this formula. This formulation isolates the category-theoretic content of MUL* and may be useful for other indexed relations and projections.

Neither (A2) nor (A3) assumes a general Beck–Chevalley law or stability of images under arbitrary base change.

## 3. Genuine composition is approximable by finite *index-sector truncations*

Although unrestricted localic relation composition need not preserve arbitrary joins in either argument, MUL* gives a particular **joint finite-truncation identity**.

For arbitrary \(R,S\le (P\times K)^2\) and finite \(F\subseteq K\), let \(R|_F\) and \(S|_F\) be the genuine sublocales whose matrices retain entries with both indices in \(F\) and have zero entries elsewhere. MAT* ensures that these are well-defined, and \(R=\bigvee_{F\Subset K}R|_F\), likewise for \(S\).

**Proposition.** Without any associativity or infinite-distributivity hypothesis on relations over \(P\),
\[
\boxed{
R\circ S
 =\bigvee_{F\Subset K}\bigl((R|_F)\circ(S|_F)\bigr).
}
\tag{A4}
\]

**Proof.** Take the \((i,k)\) coefficient of the right-hand side. By MAT*, arbitrary joins of matrices are computed coefficientwise. By MUL*, that coefficient equals
\[
\bigvee_{\substack{F\Subset K\\ i,k\in F}}
       \ \bigvee_{j\in F}(R_{ij}\circ_P S_{jk})
 =\bigvee_{j\in K}(R_{ij}\circ_P S_{jk}),
\]
since every triple \(i,j,k\) is contained in some finite \(F\). MUL* identifies this last expression with \((R\circ S)_{ik}\). Apply MAT* again to conclude (A4). \(\square\)

Equivalently, if \(e_F\) denotes the diagonal relation supported on the finite index set \(F\), then \(R|_F=(e_F\circ R)\circ e_F=e_F\circ(R\circ e_F)\). These particular sandwiches agree coefficientwise even when composition is not globally associative. Thus (A4) can be expressed using finite diagonal cutdowns.

**Caution:** (A4) is a special continuity property of the *coordinated sector truncations*; it **does not** imply that composition preserves arbitrary directed joins of unrelated sublocale relations.

## 4. One-sided finite-support variants of FINMAT*

The two support conditions in FINMAT* have different roles. Assuming the same finite-join-closed, composition-closed associative coefficient algebra \(A(P)\):

- **Row-finite** matrices alone form an associative unital finite-join algebra of genuine relations. Every fixed entry of a product is a finite join because the first factor has a finite row. Products remain row-finite, and fixed-length path expansions are finite from any starting index.
- **Column-finite** matrices alone have the analogous properties, with the finiteness argument read backward from the terminal index.
- **Converse** interchanges these two classes. Their intersection is the natural choice when one wants one algebra closed under converse as well as multiplication.

This is a small but potentially useful sharpening of FINMAT*: **column finiteness is not necessary for forward composition and associativity**, nor is row finiteness necessary for the dual statement. Both are needed for the stated symmetric sufficient hypothesis.

---

**Final comment.** Of these follow-ups, the hereditary index extension in §1 and the indexed image formula in §2 seem the most structurally useful. The finite-truncation identity in §3 may help when comparing a global relation calculation with finite-index computations. These results follow from MAT*/MUL* and the same sublocale-adjunction facts already audited; they do not require a new assumption on the parameter locale.