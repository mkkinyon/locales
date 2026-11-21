# Candidate C — what ordinary graph probes can and cannot detect

This appendix is *supplementary* to Candidates A and B. Please audit the claims, but do not infer that they settle HSIS necessity or the full Level-2-versus-Level-3 question.

## C.1. Two-colour compact closed supports

Let Y be compact Hausdorff and A,B⊆Y ordinary subsets. Then

\[
\boxed{[A]\wedge[B]\ne0\iff
\exists\ \varnothing\ne K\subseteq Y\text{ closed, with }A\cap K, B\cap K\text{ separately dense in }K.}\tag{TC}
\]

For the forward implication let W=[A]∧[B] and let K be its least ambient closed support. W is dense in K. If a nonempty relatively open part of K misses A, shrink it inside a compact closed L⊆K disjoint from A. Since [A]≤Y\L, W misses that relatively open part, contradicting density. Likewise for B. Conversely, when A∩K and B∩K are dense in nonempty K, both induced spatial sublocales restrict to dense sublocales of K and their meet contains the nonzero Booleanization B(K). Hence their meet is nonzero.

For continuous compact-Hausdorff f:X→Y, selected E⊆X and target B⊆Y, write D=f(E). In view of exact inverse images (INV) from file 03, the necessary singleton graph-probe condition

\[
[D]\wedge[B]\ne0\Longrightarrow[E]\wedge f^{-1}([B])\ne0\tag{NR}
\]

is equivalent to lifting every downstairs two-colour closed support to an upstairs nonempty closed support carrying separately dense traces of E and f^{-1}(B). The implication from upstairs to downstairs is automatic by compactness and continuity. The implication in (NR) is **not** stated sufficient for full pullback-stability.

## C.2. Strict fixed-E gap: spatial probes versus pointless probes

Take Cantor space Y and its underlying point set D with **discrete** topology. The continuous identity-on-points map D_discrete→Y extends over its Stone–Čech compactification X=βD to a compact-Hausdorff surjection f:X→Y. Choose selected E=D⊂X, so e_E:[E]→[f(E)] is just D_discrete→Y.

For every ordinary B⊆Y the map e_E has a nonzero pullback over [B] exactly when B is nonempty; this is because its source has one discrete singleton over every point of Y. Thus **all ordinary selected-support probes pass for this fixed E**.

But B(Y), the least dense Booleanization of perfect Cantor space, is nonzero and **pointless**. Its pullback along the discrete point map vanishes (each singleton fiber is zero):

\[
\boxed{D_{\mathrm{disc}}\times_Y\mathcal B(Y)=0\ne\mathcal B(Y).}\tag{FAIL}
\]

Therefore selected-image maps passing every ordinary probe need not be pullback-stable, **for a single fixed selected E**. This is NOT a counterexample to global HSIS necessity, because a smaller selected subset E'=Q⊂D, dense with dense complement I, fails an ordinary probe: [Q]∧[I]≠0, but [E'] pulls [I] back to zero.

## C.3. Booleanizations of closed supports generate every compact-Hausdorff sublocale

Let V≤Y with Y compact Hausdorff, and define

\[
\mathscr K(V)=\{K\subseteq Y:K\text{ nonempty closed and }\mathcal B(K)\le V\}.
\]

**Proposition C.3.**

\[
\boxed{V=\bigvee_{K\in\mathscr K(V)}\mathcal B(K).}\tag{BG}
\]

The right side J lies in V. If J<V, the fit ambient regular locale supplies an open O containing J but not V, with complementary closed F. Let W=V∧F≠0. Its least ambient closed support K⊆F is nonempty and W is dense in K, so B(K)≤W≤V and K is in the indexing family. But B(K)≤J∧F=0, contradiction.

Thus the Booleanizations B(K) are a complete set of nonzero support generators for *all* sublocales V, not only products of point-generated endpoint locales.

## C.4. Exact test for inclusion-base-change surjectivity

Let e:S→V with V≤compact Hausdorff Y. Consider:

(a) every sublocale inclusion W↪V pulls e back to a surjection;

(b) every nonzero W≤V has nonzero pullback S×_V W;

(c) for every K∈\mathscr K(V), S×_V B(K) is nonzero.

**Proposition C.4.** Conditions (a),(b),(c) are equivalent.

(a)⇒(b) immediate. For (b)⇒(a), fix W≤V; let J≤W be the image of its pulled-back map. If J<W, ambient fittedness gives open O with J≤O and W not ≤O, and a nonzero W'=W∧F where F is complementary closed. Since the pulled-back map factors through J, its base change to W' is zero, contrary to (b). For (b)⇒(c), each B(K) is nonzero. For (c)⇒(b), given nonzero W, take its least closed support K; B(K)≤W, hence its nonzero pullback lies within that of W.

This tests stability under **all sublocale inclusions**, not yet arbitrary base changes.

## C.5. Product-amplified inclusion tests

For any localic map e:S→V,

\[
\boxed{e\text{ is universally pullback-stably surjective}
\iff\forall T,\quad e\times\mathrm{id}_T:S\times T\to V\times T
\text{ is inclusion-base-change stable}.}\tag{AMP}
\]

Proof: the forward implication is immediate. Given arbitrary h:T→V, its graph embedding Γ_h:T↪V×T is a sublocale embedding. Pulling e×id_T back along Γ_h gives exactly S×_V T→T. The reverse implication follows. Thus a proof of Level 2⇒Level 3 for selected-image maps must also justify preservation of inclusion-stability under **arbitrary** Cartesian amplification.

## C.6. Unresolved scope and comparison questions

There are three genuinely different levels for a **fixed selected E**:

1. Ordinary graph probes using intersections with point-generated [B].
2. Pullback-surjectivity after **all sublocale inclusions**, equivalently nonzero Boolean-closed-support tests.
3. Full HSIS: surjectivity after all locale base changes.

The example in C.2 proves Level 1 need not imply Level 2 for a fixed E. It does **not** decide global Level 1 for every E ⇒ Level 3, nor Level 2 ⇒ Level 3, nor HSIS necessity for the full rectangular+map-graph algebra. The scattered-target theorem in file 02 says all three levels agree automatically for selected targets lying in a scattered Hausdorff space; therefore a separating example for the still-open implications must involve a non-scattered target and a nonspatial base-change locale.