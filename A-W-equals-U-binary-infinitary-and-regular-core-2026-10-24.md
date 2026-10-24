# Project A — Binary versus infinitary diagonal descent, and a universal regular-closed core

24 October 2026. **WORKING THEOREMS** newly derived after the binary-cover reduction. Internal algebraic checks completed; NOT independently audited or literature-priority checked. Complementary to [the first diagonal-filter note](A-W-equals-U-nucleus-criterion-2026-10-24.md) and [the compact binary-cover proof](A-W-equals-U-binary-cover-reduction-2026-10-24.md).

Conventions: Q=L⊕L, Delta diagonal sublocale, D=fit(Delta), W=cl(D)=C(d_W), U=C(d_U); a⊠b denotes a pure rectangle. B={w∈Q:δ*(w)=1}, v(a,b)=a⊠a∨b⊠b for a∨b=1.

## 1. Binary approximation and exact meaning of its fixed-point test

Define D_2=⋂_{a∨b=1}O(v(a,b)), W_2=cl(D_2), and Psi(q)=⋁_{a∨b=1}(v(a,b)→q). As in the first note, Psi is an inflationary monotone finite-meet-preserving pre-nucleus with fixed frame D_2. The binary-cover theorem gives

    Psi(0)=⋁_{a∨b=1}v(a,b)*=d_U.

Its full nuclear completion has bottom d_W2. Hence, for every locale (no compactness),

    W_2=U  ⇔  Psi(d_U)=d_U.

Always D≤D_2≤U, hence W≤W_2≤U. In compact locales D=D_2, so the binary criterion decides W=U. Outside compactness, proving W_2=U is not automatically enough.

## 2. Same points, possible pointless residual

For any locale X and any pair of *locale points* x,y (points of its sober point spectrum),

    (x,y)∈pt(D_2)  ⇔ cl{x}∩cl{y}≠∅ ⇔ (x,y)∈pt(D).

Proof: if z lies in both singleton closures, every open neighborhood of z contains both x,y, so every binary cover has a member containing both. If singleton closures are disjoint, X\cl{x} and X\cl{y} give a binary cover with no member containing both. A point of an open sublocale O(v(a,b)) is a pair belonging to one square, proving the claim.

**Pointlessness obstruction.** If D_2≠D, choose a diagonal-neighborhood w with D_2 not≤O(w). The closed complement C(w) has R=D_2∩C(w) nonzero (open and closed sublocales are complementary). Every ordinary point of D_2 belongs to D≤O(w), so R has NO ordinary points. Therefore:

    D_2≠D ⇒ D_2 contains a nonzero pointless sublocale.

If D_2 is spatial, then D_2=D, without a compactness hypothesis. In particular, whenever D_2 is spatial the binary density criterion Psi(d_U)=d_U is equivalent to W=U. This observation does not imply that D_2 is spatial merely because its ambient square is spatial.

## 3. General closure-intersection regular-core theorem

**THEOREM (arbitrary locale Y, arbitrary family of opens).** Let {w_i}⊆O(Y). Set

    S=⋂_i O(w_i),
    T=⋂_i cl(O(w_i))=C(d),  d=⋁_i w_i*,
    cl(S)=C(e).

Then

    d≤e≤d**,
    int(cl S)=int(T),
    cl(int(T))≤cl(S)≤T.

**Proof.** Each O(w_i)≤cl O(w_i) gives S≤T, hence d≤e. Put r=d**. For each i, w_i*≤d≤r. If z=w_i→r, then z∧w_i≤r, hence z∧r*≤w_i*≤r. Since z∧r*≤r* also, z∧r*=0 and z≤r**=r. Thus w_i→r=r. The frame of S consists of elements fixed by every w_i→-, so r lies in S; its least element e=j_S(0) satisfies e≤r. This proves d≤e≤d**. Taking pseudocomplements gives e*=d*; since int(C(a))=O(a*), interiors coincide. Finally cl(int T)=C(d**)≤C(e)=cl S≤C(d)=T.

Applied to the diagonal-cover family, S=D, T=U by the previous universal U theorem, so:

    d_U ≤ d_W ≤ d_U**,
    d_W*=d_U*,
    int(W)=int(U),
    cl(int U)≤W≤U.

**REGULAR-CLOSED SUFFICIENT CONDITION:** if d_U=d_U**, equivalently U=cl(int U), then W=U for every locale. No coherence, compactness, spatiality, fitness, or normality assumption.

**NOT NECESSARY:** take any perfect Hausdorff regular space (e.g. the ordinary real line). Then U=I=Delta and W=U, while int(Delta)=0 in the ordinary square, so U is not regular closed.

This general lemma may be established background in the theory of sublocale closure/fitting; check literature before claiming originality.

## 4. Infinite discrete space: finite basis fails, equality survives

Let X=N with its discrete topology. Its localic square is discrete Boolean, D=D_2=Delta and W=U=Delta. Yet the diagonal-neighborhood open w=⋁_{n∈N}{n}⊠{n}=Delta contains no finite meet of binary neighborhoods v(a_j,b_j): each n has one of only finitely many membership signatures relative to a_1,b_1,...,a_k,b_k, so distinct n,m have identical signature; then (n,m) belongs to every v(a_j,b_j), hence their meet is not contained in Delta.

Thus compactness is genuinely used in the finite *filter-basis* proof, even though the equality D=D_2 can persist noncompactly. In particular, absence of a finite binary neighborhood basis does NOT give a counterexample to the binary-density characterization.

## 5. Research agenda

1. Is there a noncompact locale satisfying W_2=U but W<U? Any example must have D_2≠D, hence a nonzero pointless residual in D_2 (the case D_2 spatial is excluded).
2. Classify useful hypotheses ensuring D_2 spatial or D_2=D beyond compactness (including noncompact sums, spatial-square/scattered examples).
3. Can regular-closedness of U be detected directly in L, rather than via d_U in Q? Test independence from coherence, using concrete examples.
4. Investigate whether the general closure-intersection theorem has a standard formulation in published closure/fitting duality. No new name until priority audit.
