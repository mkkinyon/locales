# Project A — Internal adversarial audit of the unbounded clean-cover differential theorem

**16 November 2026.** Internal-only document. **Do not include in the blind referee packet.**

## Verdict

**Conditional internal acceptance after corrections to the theorem write-up.** The integral construction survives the attacks below. Its core is an explicit boundary identity plus an injectivity argument from a unique maximal simplex and contractibility. External independent verification remains important, particularly of the finite-filtration spectral-sequence lemma and the cap-poset construction.

The theorem is about the order-complex filtration by the number of final-poset marked cover comparisons present in a simplex; it is **not** the earlier crosscut Čech spectral sequence. No priority or minimality assertion is intended.

## Attack 1: Is this genuinely a clean Boolean family?

**Potential failure.** Deleting marked relations might violate transitivity, or adjoining a cap might make an old marked edge cease to be a cover.

**Check.** If \((a,b)\) is a cover, it cannot be the conclusion of a two-step chain \(a<c<b\). Therefore deletion of *any* subset of final covers preserves transitivity. The marked path is a subset of final covers. In the induction, two minima \(u,v\) are placed below all of \(X\), with \(u<b\) marked. The cap \(y\) lies above \(u\), below all of \(X-\{b\}\), and is incomparable with \(b,v\). Minimality of \(b\) makes these relations consistent. No cap is between \(u,b\), so \(u<b\) remains a cover. For an old marked cover \(p<q\), the new minima are below \(p\), and the cap is below \(p\) when \(p\ne b\), while it is incomparable with \(p=b\); thus no new intermediate vertex appears. **Pass.**

**Boundary case considered.** An old vertex lying below \(b\) would force \(y<b\) through transitivity and ruin the construction. The hypothesis that \(b\) is minimal is genuinely necessary here, and is preserved inductively.

## Attack 2: Does the weight define a simplicial filtration?

**Potential failure.** Removing a vertex from a chain can make previously non-adjacent endpoints consecutive, creating a new marked cover occurrence.

**Check.** The weight is defined by the presence of both endpoints of each *fixed marked cover in the final poset*, not by recomputing the cover graph of the face. Deleting vertices cannot add endpoints. Since a final cover has no intermediate vertex, the two definitions agree for every simplex containing the cover. **Pass.** The convention must stay explicit in the packet.

## Attack 3: Are the integral signs and base chain correct?

**Potential failure.** The original eight-tetrahedron chain could have an unaccounted face, or the cap correction could have the wrong sign.

**Independent symbolic check.** Expanded the oriented boundary of
\\[
T=[b,d,f,h]+[a,d,e,h]-[a,d,e,i]-[a,c,f,i]
  +[b,c,f,i]-[a,d,f,h]-[b,d,f,i]+[a,d,f,i].
\\]
It has precisely the twelve triangle terms displayed as equation (3.1) in the proof, with coefficients \(\pm1\). The 1-chain \(t=[c,f]-[c,i]-[e,h]+[e,i]+[f,h]\) satisfies \(\partial t=0\). Every simplex of \(\partial T\) has weight zero. The expanded boundary of \(T+a*x*t\) has exactly twelve triangles, no \(a\), and no marked pair; explicitly:
\\[
\\begin{aligned}
z_3={}&-[b,c,f]+[b,c,i]+[b,d,h]-[b,d,i]-[b,f,h]\\
&+[d,e,h]-[d,e,i]+[x,c,f]-[x,c,i]\\
&-[x,e,h]+[x,e,i]+[x,f,h].
\\end{aligned}
\\]
The coefficient on \([a,d,f,i]\) is \(1\). **Pass.**

## Attack 4: Is the nine-vertex seed contractible?

**Potential failure.** The “delete \(e\)” argument could require an unavailable order-theoretic beat point rather than merely a contractible link.

**Check.** In \(M=\{a,b,c,d,e,f,x\}\), the strict lower set of \(e\) is exactly \(\{a,b,d,x\}\) with edges \(x-a\), \(a-d\), \(d-b\); it is a tree. Since \(e\) is maximal in \(M\), this is precisely its link. Attaching or removing the star of a vertex along a contractible link preserves homotopy type (simplicial CW gluing). After removing \(e\), \(f\) is a greatest element. Thus \(\Delta M\) is contractible; \(X_3=M\oplus\{h,i\}\) is its suspension. **Pass.** No beat-point claim is needed.

## Attack 5: Does the induction's cap define a valid cone chain?

**Potential failure.** Some simplex of \(z\) might contain \(b\), or the cap might not be comparable with all its vertices, invalidating \(u*y*z\).

**Check.** The induction explicitly requires \(z\) to avoid \(b\). Every old vertex in such a simplex lies in \(X-\{b\}\), above \(y\), while \(u<y\). The correction lies in filtration zero: it introduces no old marked pair and never contains the new marked pair \(u,b\). Direct oriented-chain computation gives
\\[
\partial((u-v)*C-u*y*z)=(v-y)*z,
\\]
because \(\partial z=0\). This new boundary avoids \(u\). The correction cannot change the coefficient of the path simplex because it contains no \(b\). **Pass.**

## Attack 6: Is the capped complex contractible?

**Potential failure.** Adding \(y\) could introduce homology even though the preceding double-cone complex was contractible.

**Check.** The strict lower set of \(y\) is precisely \(\{u\}\). Its strict upper set is \(X-\{b\}\). Thus the link is \(\Delta\{u\}*\Delta(X-\{b\})\), a cone. Removing \(y\) is a homotopy equivalence. Without \(y\) the complex is \(\Delta\{u,v\}*\Delta X\), a suspension of contractible \(\Delta X\). **Pass.**

## Attack 7: Why do we obtain precisely \(d_r\), rather than an earlier or a hidden-zero differential?

**Potential failure.** Having a chain with boundary in \(F_0\) or \(F_1\) is not by itself enough: its source class might vanish earlier, or its target may have been killed by earlier differentials.

**Check.** All marked covers form a path from a minimal to a maximal vertex. A chain containing all marked pairs contains *all path vertices*; the cover condition forbids intermediate vertices and the extreme conditions forbid end extensions. Hence there is exactly one simplex at the top filtration level, of dimension equal to the number of marks; it is maximal. Its coefficient in the witness is \(1\). There are no incoming differentials from higher filtration. The boundary of the witness belongs to \(F_0\) in the absolute case, so every \(d_j\) with \(j<r\) vanishes on this source. If the page-\(r\) target vanished, its cycle would be a boundary already inside \(F_{r-1}\); subtracting that filling produces a nonzero absolute cycle with coefficient \(1\) on the maximal top simplex. Contractibility rules that out since no higher simplex can contain it in its boundary. **Pass.**

**Correction incorporated during audit.** The first draft called the target class “primitive” based only on injectivity of a \(\mathbb Z\)-connecting map. Injectivity by itself shows **infinite order**, not primitivity in an arbitrary integral homology group. The proof now uses the justified “infinite order” wording. The argument also works after reduction over any nonzero coefficient ring.

## Attack 8: Does the *relative* base \(F_0\) really contract?

**Potential failure.** Although the full poset is an ordinal suspension, the filtration-zero subcomplex has deleted comparisons and need not be a suspension of the original \(F_0\).

**Check.** Let \(U=\{u,v\}\oplus X\) mark \(u<b\), and \(Q=\{s,t_0\}\oplus U\) mark \(s<u\). Write \(K=F_0(U)\). Simplices containing \(t_0\) make the cone \(t_0*K\). Simplices containing \(s\) cannot contain \(u\), because \(s<u\) is marked; they form \(s*(K-u)\). Their intersection is exactly \(K-u\). Since \(v\) is unmarked and lies below all of \(X\),
\\[
K-u=v*F_0(X),
\\]
a cone. Consequently \(F_0(Q)\) is contractible. Both it and the full \(\Delta Q\) are nonempty and contractible, hence \(H_m(Q,F_0;\mathbb Z)=0\) for \(m>0\). **Pass.**

## Attack 9: Relative indexing and the long differential

**Potential failure.** Killing \(F_0\) could shift the page, giving a \(d_{r+2}\), or a disappearing class.

**Check.** With an avoiding-path datum of length \(r\), the two pairs of new minima add two covers, so the unique top simplex has weight and dimension \(m=r+2\). The relative witness has boundary in \(F_1\), not necessarily \(F_0\), so its first potentially nonzero differential is \(d_{m-1}=d_{r+1}\). The bidegrees are
\\[
E^{r+1}_{r+2,0}\longrightarrow E^{r+1}_{1,r}.
\\]
If its target class were zero in \(H_{m-1}(F_{m-1},F_0)\), subtract a relative filling to obtain an element of \(H_m(Q,F_0)=0\) with coefficient \(1\) on the unique maximal top simplex. This is impossible. **Pass.**

## Attack 10: Computation and generalization claims

**Check.** Independent \(\mathbb F_2\) boundary-matrix reduction on constructed posets finds the predicted positive-length intervals:

| Test | Simplices used | Interval |
|---|---:|---|
11-vertex absolute, four marks|305|degree 3: \([0,4)\)|
13-vertex relative, five marks|917 total order-complex simplices|degree 3: \([1,5)\)|
14-vertex absolute, five marks|1295|degree 4: \([0,5)\)|
16-vertex relative, six marks|1636 after removing \(F_0\) simplices|degree 5: \([1,6)\)|

The independently constructed examples pass an explicit “no intermediate element” test for each mark. The code is corroborative only, not an integral proof. The vertex count \(3k+1\) and mark count \(k+1\) for relative \(d_k\), \(k\ge4\), follow from the three-vertex cap induction plus four vertices for the two final layers. There is **no** claim of smallest examples, new numerical invariants for locales, or a collapse theorem for all other filtrations.

## Remaining external-audit priorities

1. Verify rigorously the spectral-sequence certificate in Lemmas 2.1–2.2, in particular the equivalence between a killed \(E^r\)-target and filling in the penultimate filtration level.
2. Recheck the poset consistency/cover preservation in the general cap extension, including edge cases with additional minima and extra comparabilities.
3. Independently check the seed chain, its oriented signs, and the complete list of filtration-zero faces.
4. Verify the homotopy-equivalence argument for deleting vertices with contractible links and the two-cone decomposition of relative \(F_0\).
5. Clarify whether any of the conclusions have known counterparts in filtered simplicial complexes/persistent homology, and avoid novelty claims.

**Disposition:** ready to send as a *blind* external audit packet after excluding this internal document.
