# Independent blind referee report

**Project A: generic-fibre composition localization**  
**Packet examined:** `ProjectA_Generic_Fibre_Composition_Localization_BLIND_AUDIT_2026-11-19.zip`  
**Date:** 19 November 2026

## Verdict

**Correct, conditional only on the finite-fence geometric inputs explicitly declared in the foundations appendix.** I find the abstract decomposition lemma and composition-localization theorem valid as stated. In particular, the genuine localic composability pullback over the generic fibre is identified correctly, and the localic image of the special base change in (19) is all of its target. The interval isomorphism, nonassociative fixed-bracket formulas, transitivity criterion, converse compatibility, and equivalence-hull formula also follow. The appendix gives convincing frame-level proofs of the finite-fence inputs from its declared geometric properties; I did not reconstruct the underlying long coordinate construction. I found **no fatal mathematical defect**. There are several worthwhile expository clarifications, especially in the finite-fence kernel-pair calculation, and one useful strengthening: the displayed extra hypothesis (K) is *already a consequence* of (F) and (C) in the abstract setting, not merely in the finite-fence example.

## Severity-ranked findings

### A. Fatal errors

**None identified.** The assertions (L), (1)–(10), and (19) survive the checks below. This is not a claim to have independently established the finite-fence coordinate geometry or the outstanding global four-step statement.

### B. Points deserving explicit proof or clarification

**1. [Important improvement, not a gap] (K) is redundant.**  
The argument of Appendix §4 applies *verbatim* to the abstract hypotheses. Let $\nu:K\to X$ be either coordinate projection. Lemma (L) gives

\[
K=\bigvee_i\nu^{-1}F_i\ \vee\ \nu^{-1}G.
\]

Because the two coordinates of $K=X\times_QX$ have the same composite with $q$, and $F_i$ is a pullback from $Q$,

\[
\nu^{-1}F_i=K\wedge(F_i\times F_i)\le H,
\qquad \nu^{-1}G=K\wedge B=B.
\]

The last equality follows by base-changing the kernel pair along the point $p$, so $B=G\times G\le K$. Thus $K\le H\vee B$; the reverse inclusion is immediate. Consequently **Theorem 3.1 can include all the conclusions of §5 without any additional (K) assumption**. It would improve the statement to incorporate this observation explicitly after Lemma 2.1.

**2. [Minor proof insertion] Make the two fibre-identification diagrams explicit.**  
For $C_{R,S}=R\times_XS$, the three quotient maps $C_{R,S}\to Q$ agree. Hence base change of $C_{R,S}\to Q$ along $p:1\to Q$ can be taken in the middle coordinate or in all three coordinates:

\[
\mu^{-1}G\;\cong\;C_{R,S}\times_Q1
\;\cong\;(R\times_Q1)\times_{X\times_Q1}(S\times_Q1)
\;\cong\;R_G\times_GS_G.
\]

Here $R\times_Q1\cong R\wedge B$, since $R\le K$, and similarly for $S$. This is the *actual locale pullback*, not a pointwise description. The same calculation with $R=S=H$ proves $C\times_Q1\cong D\times_GD$. Also $T\le K$, because the map $C\to X^2$ factors through $K$, so $T\times_Q1\cong T\wedge B=A$. These few words would make (5) and (19) especially transparent.

**3. [Minor proof insertion] Spell out the finite-fence separation on the finite part (A).**  
In Appendix Lemma C, let $A=\bigcup_j C_j$, a finite union of nonsingleton components. For two different $C_i,C_j$, the Euclidean-open saturated set $P\setminus C_i$ is a quotient open that contains the latter and excludes the former. Quotient opens are constant on each component. Thus the ordinary kernel-pair points in $A\times A$ are exactly the pairs in $\bigcup_j(C_j\times C_j)$. Because $A\times A$ and all its sublocales are finite spatial locales, this *pointwise calculation on this finite block* is sufficient to establish the localic equality

\[
K\wedge(A\times A)=\bigvee_j(C_j\times C_j)\le H.
\]

The transition from points to sublocales is legitimate **here because of finiteness**; emphasizing that qualifier will prevent confusion with the forbidden pointwise reasoning in the generic fibre.

**4. [Minor proof insertion] Explain precisely why the singleton remainder embeds.**  
In Lemma C, $A$ is a finite closed component-saturated set, so $O=F\setminus A$ is relatively open in $F$. Every relative open $W\subseteq O$ is therefore relatively Euclidean-open in $F$. Because every component of $O$ is a singleton, $W$ is component-saturated; consequently $F\setminus W$ is both Euclidean-compact and component-saturated. The quotient open $P\setminus(F\setminus W)$ restricts exactly to $W$ on $O$. This proves the required surjection of frames

\[
\mathcal O(Q)\twoheadrightarrow\mathcal O(O)
\]

and hence shows $q|_O$ is a locale embedding. The kernel pair on $O\times O$ is therefore $\Delta_O$. The mixed blocks vanish because $P\setminus A$ is a quotient open whose restrictions to $A$ and $O$ are respectively zero and top. Finally, since $F=A\vee O$ is a complementary closed/open decomposition, the four product blocks jointly cover $F\times F$. This completes the entirely localic argument for (C).

**5. [Minor bookkeeping] Record closure of $[H,K]$ under composition before using (8).**  
If $H\le R,S\le K$, then $H\le R\circ_X S$ by the diagonal unit law and monotonicity, and $R\circ_XS\le K$ because the outer-coordinate map of the composability locale factors through the kernel pair. Thus $R\circ_XS\in[H,K]$, making the left side of (8) well typed. This fact is used implicitly several times; one line would suffice.

### C. Independent checks of the principal argument

**6. [Verified] Complemented-cutoff decomposition (L).**  
Write $V=\bigvee_i f^{-1}F_i$. The sublocale lattice is a coframe and sublocale pullback preserves arbitrary meets and finite joins. Consequently

\[
V\vee f^{-1}G
=\bigwedge_i\bigl(V\vee f^{-1}U_i\bigr)=Y,
\]

because the (i)-th factor contains $f^{-1}F_i\vee f^{-1}U_i=Y$. The exact infinitary distributive law is used in the correct direction. This argument also accommodates an empty index family.

**7. [Verified] Localization (1) and (2).**  
Apply (L) to the middle-coordinate map $\mu:C_{R,S}\to X$. For a cutoff summand, equality of the quotient-coordinate maps and the fact that $F_i$ comes from (Q) ensure

\[
e[\mu^{-1}F_i]\le K\wedge(F_i\times F_i)\le H.
\]

For the generic summand, item 2 identifies the domain with $R_G\times_GS_G$, whose image in $B$ is precisely $R_G\circ_GS_G$. Localic images preserve arbitrary joins of sublocales, yielding the **upper** inclusion in (1). For the reverse, the generic image is plainly a sublocale of the full image, while

\[
H=H\circ_X\Delta_X\le R\circ_XS
\]

by $H\le R$ and $\Delta_X\le S$. This proves (1). As $R_G\circ_GS_G\le B$, finite distributivity gives

\[
(R\circ_XS)\wedge B=D\vee(R_G\circ_GS_G).
\]

The second summand contains (D): specifically, $D\le R_G$, $\Delta_G\le S_G$, so $D=D\circ_G\Delta_G\le R_G\circ_GS_G$. Hence (2). No unjustified assumption of stability of images under base change is made.

**8. [Verified] The special surjection (19).**  
Set $T=H\circ_XH$. Formula (2) says its actual fibre $A=T\wedge B$ is $D\circ_GD$. The base-changed map $e_\infty:C\times_Q1\to T\times_Q1$ is exactly the outer-coordinate map $D\times_GD\to A$, by item 2. Its image is $D\circ_GD=A$ *by definition of localic composition*. A locale map is surjective in the sense at issue exactly when its image sublocale is the whole codomain. Thus (19) follows. The argument is special to this image and does not infer pullback stability for arbitrary surjections.

**9. [Verified] Interval and algebraic consequences (7)–(10).**  
With (K)—which follows already from (F),(C) by item 1—coframe finite distributivity proves that $R\mapsto R\wedge B$ and $Z\mapsto H\vee Z$ are mutually inverse. Formula (8) is (2), once closure under composition is noted. An induction on the *binary tree*, not on an assumed associative product, proves both statements in (9) for every fixed bracketing. By the order isomorphism, $R\circ R\le R$ iff $R_G\circ R_G\le R_G$, proving the transitivity criterion. Converse commutes with joins and intersection with the symmetric square (B), and preserves (H) if (H) is symmetric. Finally, the equivalence hull of (H) in the whole relation lattice of (X) lies **inside (K)** because (K) itself is an equivalence relation containing (H); likewise the equivalence hull of (D) lies inside (B). The interval isomorphism therefore identifies the two least equivalence relations and proves (10). No associativity of localic composition is needed.

**10. [Verified relative to declared geometry] Finite-fence Lemma F.**  
The strong forcing property shows the Euclidean-compact saturated complement of each positive quotient open meets only finitely many nonsingleton fence components, hence belongs to $\mathscr F$. Thus every positive quotient open restricts to top on $N=\bigwedge_{F\in\mathscr F}U_F$. A negative quotient open is Euclidean-open and disjoint from (E), hence also disjoint from $\overline E=[0.1,0.8]$. Every point of it has a small Euclidean-open neighbourhood contained in a compact interval $F_x$ consisting solely of singleton components. Since $N\le U_{F_x}$, each such neighbourhood restricts to zero on (N); arbitrary joins give the same for the entire negative open. Hence $\mathcal O(Q)\to\mathcal O(N)$ agrees with the truth-value map for $p_\infty$ followed by the unique $\mathcal O(1)\to\mathcal O(N)$. The universal property of the fibre proves $N\le G$, and positive neighbourhoods give $G\le N$. This genuinely establishes an equality of locales, not just point sets.

## Dependency table

| Input or assertion | Audit status | Comment |
|---|---|---|
| Sublocale lattice is a coframe; pullback preserves arbitrary meets and finite joins; images preserve joins | Checked as standard locale-theoretic principles | Used in (L), (1), finite four-block argument |
| (F), (C) *as abstract hypotheses* | Taken as hypotheses | Suffice for (L), (1)–(10), (19); (K) follows |
| Genuine pullback identity (5) | Independently checked | Equality of quotient-coordinate maps; iterated base change |
| Images of cutoff and generic summands | Independently checked | No pointwise substitute or image-base-change assumption |
| Base-changed surjection (19) | Independently checked | Domain and target fibres identified; image $=A$ |
| Interval map, converse, bracketed powers, equivalence hull | Independently checked | Includes justification that the least hull remains below (K) |
| Strong forcing property and $\overline E=[0.1,0.8]$ in the coordinate model | Accepted as supplied geometric inputs | No independent reconstruction of the long finite-fence model |
| Existence of compact closed finite-fence components and singleton complement, spatiality of (X) | Accepted as the specified model data | Used to prove cutoff rigidity and diagonal inclusion |
| Lemma F (exact actual fibre) | Checked from supplied geometric inputs | Both positive and negative quotient-open tests needed |
| Lemma C (rigidity of cutoffs) | Checked from supplied geometric inputs | Requires the finite-block separation and frame-level embedding of (O) |
| (K) for the finite-fence model | Independently derived from (F),(C) | In fact abstractly redundant |
| Global Cantor-fusion or $D^2\circ_GD^2=B$ | **Not in scope; not verified** | No such implication from (19) is asserted |

## Optional generalization and presentation suggestions

1. **Weaker cutoff hypothesis.** The abstract argument never uses closedness *per se*. It suffices to have sublocales $F_i\le X$ pulled back from (Q), together with sublocales $U_i\le X$ satisfying $F_i\vee U_i=X$ and $G=\bigwedge_i U_i$, plus $K\wedge(F_i\times F_i)\le H$. Complementarity $F_i\wedge U_i=0$ is likewise unnecessary for the abstract algebraic proof, although it is natural and useful in the finite-fence construction. This is a genuine abstract strengthening, not needed to validate the candidate.
2. **Promote the abstract kernel decomposition.** Present $K=H\vee B$ as an immediate corollary of (L) and (C), before Theorem 3.1 or at the beginning of §5. The theorem can then state the interval correspondence without a new assumption.
3. **Name the image definition once in the base-change argument.** A parenthetical reminder that $e_\infty$ has image exactly $D\circ_GD$, whereas the target is identified with that image *by theorem (2)*, distinguishes this special surjectivity argument from the invalid general claim that surjections remain surjective under pullback.
4. **Retain the strict nonassociativity warning.** The fixed-parenthesization formulation of (9) is appropriate, and the packet correctly keeps the global four-step/Cantor-fusion claim separate.

## Final recommendation

I would accept the mathematical core of this packet, subject to adding the short explanations in findings 2–5. These are clarifications rather than missing new hypotheses. I especially recommend folding the automatically valid identity $K=H\vee B$ into the abstract theorem: it makes the result appreciably cleaner and stronger, and identifies the genuine hypotheses of the interval and equivalence-hull conclusions.
