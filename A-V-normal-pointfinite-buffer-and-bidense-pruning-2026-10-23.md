# Normality, shrinkable covers, rather-below buffers and bi-dense residuals

23 October 2026. **Working point-free research note.** Builds on A-V-normal-explicit-coproduct-nucleus-and-pointless-residual-2026-10-23.md. The general statement normal L => V=U remains unresolved. Assertions below are distinct from normal L => D=U.

Notation: L a frame, Q=L⊕L, a⊠b rectangles, d_I=⋁_{a∧b=0}a⊠b, d_U=⋁_{a*∨b*=1}a⊠b; I=C(d_I), D=fit(Δ), V=fit(I), U=C(d_U), F functional relation. Let a≺b mean a*∨b=1.

## 1. Source-backed pointfree shrinking

Ferreira–Picado, *On Point-Finiteness in Pointfree Topology*, Coimbra preprint 06–30 (2006), Proposition 5.7, https://www.mat.uc.pt/preprints/ps/p0630.pdf, recalls Dowker–Strauss's pointfree Lefschetz theorem: a frame is normal iff every point-finite cover is shrinkable. Their point-finiteness is slightly stronger than Dowker–Strauss's original definition; both suffice.

Here {b_i} is a shrinking of {a_i} iff ⋁b_i=1 and b_i≺a_i (that is b_i*∨a_i=1) for every i. Shrinking is coordinatewise refinement b_i≤a_i, so it preserves point-finiteness.

Earlier established elementary lemma:
If {c_i} is a cover admitting a **two-step** rather-below refinement r_j≺s_j≺c_{i(j)}, ⋁r_j=1, then
    d_U∨⋁_i(c_i⊠c_i)=1.
Proof: r_j⊠1≤r_j⊠s_j*∨r_j⊠c_{i(j)}; first rectangle is far since r_j*∨s_j**=1, second below corresponding square.

**THEOREM A (pointfree, no spatiality).** If L is normal and EVERY open cover admits a point-finite refinement, then
    D=V=U=F.
Proof: refine an arbitrary cover C to point-finite {b_j}, shrink to {s_j}≺b_j, shrink again to {r_j}≺s_j; both shrinkings stay point-finite. Apply two-step lemma, obtaining the universal square-cover condition for D=U. The universal inclusions D⊆V⊆U and normality U=F give collapse.

In particular normal metacompact frames in the pointfree point-finite-refinement sense, and normal paracompact frames, satisfy this equality. Need not be compact, continuous or spatial.

**LOCAL obstruction:** For normal L, if an individual diagonal-neighborhood w has a rectangle presentation w=⋁_i a_i⊠b_i whose diagonal cover c_i=a_i∧b_i admits a point-finite refinement, then U⊆O(w). A failure D≠U requires a diagonal neighborhood with no such refinement for ANY rectangle presentation, and a failure V≠U requires a BAR w with this property. Crucial: not every diagonal neighborhood is a bar (I may be larger than Δ).

## 2. A one-shrinking local tree absorption lemma

For w∈Q and b∈L put
    r_w(b)=⋁{u∈L:u⊠b≤w}.
The C-ideal property gives r_w(b)⊠b≤w.

**LEMMA B.** Suppose a≤b_i*∨r_w(b_i) for each member of a cover ⋁b_i=1. If the cover {b_i} is shrinkable, then
    a⊠1 ≤ w∨d_U.

Proof: choose c_i≺b_i covering 1. For each i,
    a⊠c_i ≤ (a∧b_i*)⊠c_i ∨(a∧r_w(b_i))⊠c_i.
The second is below w. The first is far because c_i*∨b_i**=1 and (a∧b_i*)*≥b_i**. Hence join over i.

**COROLLARY.** If L normal and an H–V–H rank≤3 bar tree for w has point-finite middle V-covers, then w∨d_U=1. Symmetrically V–H–V with point-finite middle H-covers. Any rank-three bar witnessing V≠U must have an unshrinkable middle cover in EVERY such certificate.

## 3. Normality supplies a rather-below BUFFER even without shrinking the middle cover

Define the rather-below core
    ρ(a)=⋁{t∈L:t≺a}.
For normal L, ≺ interpolates, and ρ is deflationary, monotone, idempotent and finite-meet preserving:
- ρ(a)≤a and monotonicity are immediate.
- Interpolation t≺s≺a gives t≺ρ(a), proving idempotence.
- If t≺a and u≺b then t∧u≺a∧b, since (t*∨a)∧(u*∨b)=1 implies (t∧u)*∨(a∧b)=1; distribute meets over joins for ρ(a∧b)=ρ(a)∧ρ(b).
Thus its fixed points form a unital subframe closed under ordinary joins and finite meets. Do not identify this with a named complete-regular reflection without a separate check.

**LEMMA C (buffered normality).** Let L be normal. If t≺a and
    a≤b*∨r_w(b),
then
    t⊠b≤w∨d_U.

Proof: t*∨b*∨r_w(b)=1. Normality's one-sided binary shrinking gives p≺b* with
    p∨t*∨r_w(b)=1.
Meet with t to obtain t≤p∨r_w(b). Now p⊠b≤d_U since p*∨b*=1, and r_w(b)⊠b≤w. Therefore t⊠b≤w∨d_U.

**COROLLARY.** If a≤b_i*∨r_w(b_i) for a cover ⋁b_i=1, then
    ρ(a)⊠1≤w∨d_U,
with NO shrinking assumption on {b_i}.
Indeed apply Lemma C to every t≺a and every b_i.

If a rank-three H–V–H bar has root H-cover {a_i}, the latter corollary gives
    (⋁_i ρ(a_i))⊠1≤w∨d_U.
In particular, the bar is U-large whenever ⋁_iρ(a_i)=1, regardless of any middle-cover shrinkability. Symmetric for V–H–V.

This is a genuinely different sufficient condition from pointfinite shrinking. A potential normal rank-three counterexample must defeat BOTH mechanisms: essential middle covers unshrinkable AND root regular cores insufficient.

## 4. Closed sublocale heredity of U under normality (Tietze)

Established localic Tietze extension theorem: Gutiérrez García, Kubiak, Picado, *Localic real functions: A general setting*, JPAA 213 (2009) 1064–1074, Theorem 8.4 and Proposition 8.3, asserts that on a normal frame EVERY real-valued continuous localic map on a closed sublocale extends to the ambient locale. Accessible article transcription: https://paperzz.com/doc/6826222/journal-of-pure-and-applied-algebra-localic-real ; see Thm 8.4, Prop 8.3.

Let i:Z=C(p)→X be a closed inclusion with L normal. Closed sublocales of normal locales are normal: in ↑p, for a∨b=1, normal disjoint witnesses in L descend via x↦x∨p. Therefore U(Z)=F(Z) and U(X)=F(X).

By Tietze every real map Z→R extends to X. Kernel pairs commute with pullback; intersection over all real maps therefore gives
    **U(Z)=(i×i)^(-1)U(X)**
as sublocales (no spatiality). This strengthens the general one-sided functoriality and applies to ANY closed sublocale of normal X.

## 5. Bi-dense-pointless minimal obstruction to normal V=U

Assume, provisionally, some normal L has V≠U. Choose a BAR w satisfying q=w∨d_U<1. Replace w by symmetric w∧τ(w); it stays a bar since I is symmetric and the residual C(q) stays nonzero. Write R=C(q)⊆U. By the previously established normal-point theorem, R is nonzero but pointless.

Define the good-strip open
    p=⋁{a∈L : a⊠1≤q}.
Since q symmetric, p⊠1 and 1⊠p lie under q. Thus
    R⊆C(p)×C(p).
If p>0, put Z=C(p), a proper closed sublocale. Z is normal; restriction w_Z of w is a bar because I(Z)⊆pullback I(X) by functoriality. Exact U heredity from §4 gives
    C_Z(w_Z∨d_U(Z))=R
as sublocales of X², in particular still nonzero.
Hence V(Z)≠U(Z).

Repeat the reduction within Z whenever its new good-strip open is nonzero. At a limit ordinal intersect the descending family of closed sublocales, which remains closed (C(∨p_α)). The ORIGINAL R is contained in the square of every stage, hence also in the limit square; Tietze and normality ensure the same nonzero residual remains. Strict decreases cannot run beyond the set-sized lattice of closed sublocales. Therefore there is a terminal normal closed sublocale Z and symmetric bar w_Z with a nonzero pointless residual R⊆U(Z) satisfying:
    a⊠1≤w_Z∨d_U(Z) ⇒ a=0,
and symmetrically 1⊠a≤w_Z∨d_U(Z) ⇒a=0.
Equivalently, BOTH coordinate projections R→Z are dense locale morphisms: inverse image of a nonzero open a is nonzero.

**REDUCTION THEOREM (conditional on a counterexample):** A failure of normal⇒V=U entails a normal locale Z with a nonzero pointless CLOSED subrelation R⊆U(Z), disjoint from the bar w_Z, whose two coordinate projections to Z are dense.

This does not solve the conjecture; it replaces an arbitrary residual by a bi-dense minimal obstruction. If one can show a normal locale admits no such R, the implication follows. Conversely a candidate counterexample must realize exactly such a relation after closed-localic pruning.

## 6. Status and provenance

- The shrinkability characterization is **published**, not new: Dowker–Strauss, refined in Ferreira–Picado (2006).
- The Tietze extension theorem is **published**: Gutiérrez García–Kubiak–Picado (2009).
- The deductions for D, V, U and the buffered local lemma, the regular core, and bi-dense pruning are project calculations, not claims of priority.
- IMPORTANT distinction: D=fit(Δ), V=fit(I), so all D=U conclusions are stronger than V=U. Also diagonal neighborhoods δ*w=1 need not be I-bars w∨d_I=1.
- General normal⇒V=U remains OPEN.
