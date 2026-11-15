# Project A — SC+ theorem: blind mathematical packet

**15 November 2026. Proposed theorem and proof for independent review.**

This packet is self-contained. It does not reproduce any internal audit or claim originality. It works in classical locale theory; spatial statements may use ordinary sober spaces and classical choice.

## 1. Definitions and question

Let \(X\) be a locale with frame \(L=\mathcal O(X)\), and let \(Y=X\times X\) denote the **localic product**, with frame coproduct \(L\otimes L\). For \(a\in L\), write \(a_i=\pi_i^*(a)\). Let \(\Delta\hookrightarrow Y\) be the diagonal image sublocale.

- \(\mathcal I=\operatorname{cl}_Y(\Delta)\) is the *closed* inseparability sublocale. Its complementary open is \(d_I=\bigvee_{a\wedge b=0} a\boxtimes b\).
- \(\mathcal D=\operatorname{fit}_Y(\Delta)=\bigwedge\{O_Y(w):\Delta\le O_Y(w)\}\) is the *fitted diagonal*.
- \(\mathcal M=\mathcal I\wedge\mathcal D\).
- \(\mathcal A\hookrightarrow Y\) is the largest sublocale on which \(a_1\le a_2\) for every \(a\in L\). Its converse is \(\mathcal A^\smile\); define \(\mathcal S=\mathcal A\vee\mathcal A^\smile\).

The established all-locale inclusion is
\[
\Delta\le\mathcal S\le\mathcal M.
\tag{1.1}
\]
For reference, on \(\mathcal A\) one has \(a_1\le a_2\). If \(a\wedge b=0\), then \(a_1\wedge b_2=0\) on \(\mathcal A\), giving \(\mathcal A\le\mathcal I\). For every cover \(\mathscr C\) of \(X\), the diagonal square-cover open \(w_{\mathscr C}=\bigvee_{c\in\mathscr C}c_1\wedge c_2\) restricts to top on \(\mathcal A\), since \(c_1\le c_2\), giving \(\mathcal A\le\mathcal D\). The converse orientation is symmetric.

The specialization-order convention is \(x\le y\iff x\in\overline{\{y\}}\), so opens are upper sets. For a subset \(B\), \(\uparrow B\) denotes its specialization saturation. Write \([B]\hookrightarrow Z\) for the **spatial sublocale induced by a subspace** \(B\subseteq Z\) of a sober space \(Z\). In particular, \([B]\) is the smallest sublocale of \(Z\) containing the points in \(B\). Ordinary-point descriptions below must not be silently substituted for arbitrary localic relations.

**Question SC+.** Does the equivalence
\[
\mathcal S=\mathcal M\quad\Longleftrightarrow\quad
\text{every specialization interval }[r,s]\text{ is a chain}
\tag{SC+}
\]
hold for **stably locally compact** locales, with no assumption that \(X\) is compact?

The proposed answer is **yes**; the proof claims a stronger spatiality statement for \(\mathcal M\).

## 2. Background facts used: patch and ordered spaces

For a stably locally compact sober \(Z\):

1. Its patch topology is locally compact Hausdorff. The specialization order has closed graph in the patch product.
2. The original opens of \(Z\) are exactly its **patch-open upper subsets**.
3. Every compact saturated \(K\subseteq Z\) is compact in the patch topology.
4. Every point \(z\) of every ordinary open \(V\) has a compact saturated neighborhood \(K\) with \(z\in\operatorname{int}K\subseteq K\subseteq V\).

In the ordered-space description, the patch is a *properly locally compact pospace*: a locally compact Hausdorff pospace with closed order such that the upward closure of every compact subset remains compact. Conversely, the upper-open topology of such a pospace is stably locally compact. Finite products remain in this class. Closed subspaces of stably locally compact sober spaces are also stably locally compact: one can restrict patch-compact saturated neighborhoods and use their compact intersections, or work with closed order subspaces of the corresponding pospaces.

The primary references at the end identify the required patch results. The referee should independently verify their exact scope, especially the noncompact case.

## 3. Proposed saturation lemma

**Lemma 3.1.** If \(Z\) is stably locally compact sober and \(C\subseteq Z\) is saturated, then the spatial sublocale \([C]\) is **fitted**. Consequently, for every subspace \(B\subseteq Z\),
\[
\boxed{\operatorname{fit}_Z([B])=[\uparrow B].}
\tag{3.1}
\]

**Proposed proof.** The quotient nucleus of the subspace inclusion \(C\hookrightarrow Z\) is
\[
j_C(w)=\operatorname{int}_Z\bigl(w\cup(Z\setminus C)\bigr),
\qquad w\in\mathcal O(Z).
\]
We claim
\[
j_C(w)=\bigvee_{\substack{u\in\mathcal O(Z)\\ C\subseteq u}} (u\to w).
\tag{3.2}
\]
If \(u\) contains \(C\), then \(u\to w\le j_C(w)\), giving one inequality.

Conversely, suppose \(z\in j_C(w)\). There is an ordinary open \(V\ni z\) such that \(V\cap C\subseteq w\). Choose compact saturated \(K\) with \(z\in\operatorname{int}K\subseteq K\subseteq V\). Set \(F=K\setminus w\). Because \(K\) is compact in the patch topology and \(w\) is patch-open, \(F\) is patch-compact. The set
\[
\downarrow F=\{p\in Z:\exists q\in F,\ p\le q\}
\]
is patch-closed: the order graph is closed, and projection from the product with compact \(F\) is closed. Hence
\[
u=Z\setminus\downarrow F
\]
is patch-open and upward closed, and therefore an **ordinary open**. Since \(C\) is upper and disjoint from \(F\), one has \(C\subseteq u\). Since \(K\cap u\subseteq w\),
\[
z\in\operatorname{int}K\subseteq(u\to w).
\]
This proves (3.2), as the topology of \(Z\) is spatial.

For each such \(u\), the map \(j_u(w)=u\to w\) is the nucleus of the open sublocale \(O_Z(u)\). Let \(k=\bigvee_{C\subseteq u}j_u\) be their **join as nuclei**. Since each \(j_u\le j_C\), we have \(k\le j_C\). Conversely, (3.2) gives \(j_C(w)=\bigvee_u j_u(w)\le k(w)\) for every \(w\). Thus \(k=j_C\), showing that \([C]\) is the meet of its open supersublocales, i.e. fitted. Notice that this argument does **not** assume that arbitrary joins of nuclei are computed pointwise.

Now \([\uparrow B]\) is fitted and contains \([B]\). Conversely, every fitted sublocale containing \([B]\) has an upward-closed point set containing \(B\), hence contains \(\uparrow B\) and the spatial sublocale generated by those points. Therefore (3.1). \(\square\)

The hypothesis that \(C\) is *patch-closed* is **not** used. Fittedness should not be confused with perfectness (Scott continuity of the nucleus).

## 4. Proposed spatiality of \(\mathcal D\) and \(\mathcal M\)

**Proposition 4.1.** For every stably locally compact locale \(X\),
\[
\boxed{\mathcal D=[\uparrow_Y\Delta],\qquad
\mathcal M=[\uparrow_{\mathcal I}\Delta].}
\tag{4.1}
\]
In particular, both \(\mathcal D\) and \(\mathcal M\) are spatial.

**Proposed proof.** Since \(X\) is locally compact sober, its localic square is the spatial product \(Y\), and \(Y\) is stably locally compact. The diagonal image is a spatial sublocale, so Lemma 3.1 gives \(\mathcal D=\operatorname{fit}_Y\Delta=[\uparrow_Y\Delta]\).

Next, \(\mathcal I=\operatorname{cl}_Y\Delta\) is a closed spatial sublocale and is stably locally compact. Open sublocales of \(\mathcal I\) are restrictions of ambient opens in \(Y\). Since \(\Delta\le\mathcal I\), directly taking the defining meet over opens gives
\[
\boxed{\operatorname{fit}_{\mathcal I}(\Delta)
=\mathcal I\wedge\operatorname{fit}_Y(\Delta)
=\mathcal I\wedge\mathcal D=\mathcal M.}
\tag{4.2}
\]
Apply Lemma 3.1 inside \(\mathcal I\) to get the second equality in (4.1). \(\square\)

Since the order of \(Y\) is coordinatewise, \((x,y)\in\uparrow_Y\Delta\) iff \(x,y\) have a common lower bound. The order on the closed subspace \(\mathcal I\) is the restricted order. Thus \((x,y)\in\uparrow_{\mathcal I}\Delta\) iff \((x,y)\in\mathcal I\) and the pair has a common lower bound.

**Lemma 4.2 (point formula for \(\mathcal I\)).** In a stably locally compact sober space \(X\), two points are inseparable iff they have a common upper bound.

**Proposed proof.** A common upper bound belongs to every open neighborhood of either point, hence prevents separation. Conversely, suppose \(x,y\) are inseparable. Every pair of compact saturated neighborhoods \(K\ni x\), \(H\ni y\) has nonempty intersection, because their interiors are neighborhoods of the inseparable points. Finite intersections of compact saturated neighborhoods remain compact saturated neighborhoods, so this family of intersections has the finite-intersection property. Fix one such intersection as a patch-compact ambient set; all the other intersections are patch-closed. Compactness supplies a point in their total intersection. By local compactness, the intersection of all compact saturated neighborhoods of \(x\) is \(\uparrow x\), and similarly for \(y\). Hence \(\uparrow x\cap\uparrow y\ne\varnothing\). \(\square\)

Combining these results gives the actual **localic** formula
\[
\boxed{\mathcal M=
[\{(x,y):\exists r,s\in X\ \text{with }r\le x,y\le s\}].}
\tag{4.3}
\]

## 5. Proposed SC+ theorem

**Theorem 5.1 (SC+).** For every stably locally compact locale \(X\),
\[
\boxed{\mathcal S(X)=\mathcal M(X)
\iff \text{every interval }[r,s]=\{z:r\le z\le s\}
\text{ in the specialization order of }X\text{ is a chain}.}
\tag{5.1}
\]

**Proposed proof.** The points of \(\mathcal S\) are exactly the comparable pairs: a point factors through \(\mathcal A\) iff it satisfies every inequality \(a_1\le a_2\), equivalently the first coordinate is below the second, and similarly for \(\mathcal A^\smile\).

If all intervals are chains, the pairs \(x,y\) appearing in (4.3) are comparable. Thus \(\mathcal M\) and \(\mathcal S\) have the same points. By Proposition 4.1, **\(\mathcal M\) is spatial**, hence it is the smallest sublocale containing those points. Since \(\mathcal S\) contains them and \(\mathcal S\le\mathcal M\) by (1.1), equality follows.

Conversely, if \(r\le x,y\le s\) with \(x,y\) incomparable, (4.3) puts \((x,y)\) in \(\mathcal M\) but not in \(\mathcal S\), so the sublocales differ. \(\square\)

The minimal finite obstruction is the four-element diamond \(r<x,y<s\) with \(x\parallel y\). No compactness of \(X\) is assumed in the proposed proof.

## 6. Scope, cautions, and optional tests

- The theorem is intended for **stably locally compact** locales, including noncompact ones. Nothing here asserts SC+ for arbitrary locales.
- The claim that \(\mathcal D\) and \(\mathcal M\) are spatial does **not** assert they are generally perfect. In noncompact ordered patch examples, common-lower-bound witnesses can escape to infinity, making the point set of \(\mathcal D\) non-patch-closed.
- The proof of equality uses spatiality of \(\mathcal M\) only, not a claim that \(\mathcal S\) or arbitrary sublocales are point-determined.
- The equivalence in Lemma 4.2 needs the stability/coherence of compact saturated intersections. Mere local compactness would not justify the patch compactness argument.
- A useful test is a noncompact properly locally compact patch pospace consisting of two convergent sequences \(x_n\to x\), \(y_n\to y\), and discrete points \(z_n\) with \(z_n<x_n,y_n\) and no other strict comparisons. Here every order interval is a chain; the common-lower-bound pairs \((x_n,y_n)\) converge patchwise to \((x,y)\), which lacks a lower witness. The proposed theorem predicts \(\mathcal S=\mathcal M\) despite this failure of patch-closedness for the point set of \(\mathcal D\). Validate the topology and properties if using this control.

## 7. Primary background and project definitions

1. R. Tix, K. Keimel, G. Plotkin, *Semantic Domains for Combining Probability and Non-Determinism*, §1.5 and the paragraph following Proposition 1.8 on properly locally compact pospaces: https://www2.mathematik.tu-darmstadt.de/~logik/keimel/Papers/tkp4.pdf
2. T. Bice, C. Starling, *Hausdorff tight groupoids generalised*, *Semigroup Forum* **100** (2020), Proposition 2.32 on patch compactness of compact saturated sets: https://link.springer.com/article/10.1007/s00233-019-10027-y
3. M. H. Escardó, *On the regular-locally-compact coreflection of a stably locally compact locale*, *Journal of Pure and Applied Algebra* **157** (2001), for Scott-continuous nuclei, patch locales and perfect maps: https://www.cs.bham.ac.uk/~mhe/papers/patch-full.pdf
4. Project A, *Returning to Cameron–Kumar: graph dictionary and refreshed relation hierarchy* (10 November 2026), §§1–2, for the original definition of \(\mathcal S\) and its all-locale inclusion in \(\mathcal M\): https://github.com/mkkinyon/locales/blob/main/ProjectA_Cameron_Kumar_revisit_graph_to_locale_hierarchy_2026-11-10.md

**End of blind packet.**
