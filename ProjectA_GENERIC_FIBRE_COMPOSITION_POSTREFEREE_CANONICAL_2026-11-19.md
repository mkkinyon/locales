# Project A — generic-fibre composition localization (post-referee canonical note)

**19 November 2026. Positive independent blind audit; reconciled with referee report and addendum.**

This note supersedes the **verification status and exposition**, not the archived text, of the preliminary note *ProjectA_Generic_Fibre_Composition_Consolidated_2026-11-19.md*. The abstract theorem and its consequences have received an independent positive blind audit. The finite-fence geometric prerequisites have been checked in earlier separate reviews, although the latest referee did not independently reconstruct the complete long coordinate model. The global Cantor-fusion/four-step result remains **conditional**; it is logically separate from the theorem below.

## 1. Exact general hypotheses

Let $q:X\to Q$ be a locale map with kernel-pair relation

$$
K=X\times_Q X\le X^2.
$$

Let $H\le K$ be **reflexive**, meaning $\Delta_X\le H$. Fix a point $p:1\to Q$ and define its **actual localic fibre** and generic square

$$
G=X\times_Q1,\qquad B=G\times G\le X^2,\qquad D=H\wedge B.
$$

Assume a family of sublocales $F_i,U_i\le X$ such that:

1. Each $F_i$ is the pullback under $q$ of a sublocale of $Q$.
2. $F_i\vee U_i=X$ for every $i$.
3. $G=\bigwedge_iU_i$ **as a locale equality**.
4. The **cutoff rigidity** condition holds:

   $$
   K\wedge(F_i\times F_i)\le H\quad\text{for every }i.
   \tag{C}
   $$

Neither closedness of $F_i$ nor complementarity $F_i\wedge U_i=0$ is needed for the abstract theorem. In our explicit two-colour finite-fence model the $F_i$ *are* closed saturated finite-vertex cutoffs and the $U_i$ *are* their complementary opens; the stronger concrete hypotheses are useful for proving the four abstract conditions.

Composition $R\circ_X S$ always means the **localic image** of $R\times_X S\to X^2$ with the middle coordinate identified; it is not defined by a point-set existential formula. No associativity is assumed.

## 2. Two elementary consequences of the cutoff hypotheses

**Lemma 2.1 (complemented-cover decomposition).** For every locale map $f:Y\to X$,

$$
\boxed{Y=\left(\bigvee_i f^{-1}F_i\right)\vee f^{-1}G.}
\tag{L}
$$

**Proof.** Set $V=\bigvee_i f^{-1}F_i$. Sublocale pullback preserves arbitrary meets and finite joins. The sublocale lattice $\operatorname{Sub}(Y)$ is a coframe, hence

$$
\begin{aligned}
V\vee f^{-1}G
 &=V\vee\bigwedge_i f^{-1}U_i\\
 &=\bigwedge_i\left(V\vee f^{-1}U_i\right)=Y,
\end{aligned}
$$

since each factor contains $f^{-1}F_i\vee f^{-1}U_i=f^{-1}(F_i\vee U_i)=Y$. This is the valid coframe distributive law: a *fixed join* distributes over an arbitrary meet. $\square$

**Proposition 2.2 (automatic kernel decomposition).** The four hypotheses imply

$$
\boxed{K=H\vee B.}
\tag{K}
$$

**Proof.** Apply (L) to the second projection $\nu:K\to X$. Since the two coordinates of $K$ have equal composite with $q$, the quotient-pullback condition on $F_i$ yields

$$
\nu^{-1}F_i=K\wedge(F_i\times F_i)\le H.
$$

The same kernel-pair identity at the point $p$ gives

$$
\nu^{-1}G=G\times G=B.
$$

Thus $K\le H\vee B$. Conversely both $H$ and $B$ are contained in $K$. $\square$

**Referee improvement.** In the preliminary presentation, (K) was introduced again as an extra hypothesis for the interval correspondence. Proposition 2.2 shows that it is **automatic**, even under the weaker noncomplemented cutoff-cover assumptions above.

## 3. Localization of composition

For $H\le R,S\le K$, put $R_G=R\wedge B$ and $S_G=S\wedge B$, regarded as relations on $G$. These both contain $D$, and $\Delta_G\le D$.

**Theorem 3.1 (composition-localization theorem).** Under the hypotheses in §1, for every $H\le R,S\le K$,

$$
\boxed{R\circ_XS=H\vee(R_G\circ_GS_G)}
\tag{GL1}
$$

and

$$
\boxed{(R\circ_XS)\wedge B=R_G\circ_GS_G.}
\tag{GL2}
$$

**Proof.** Let $C_{R,S}=R\times_XS$ be the genuine localic composability pullback. Write $\mu:C_{R,S}\to X$ for its middle-coordinate map and $e:C_{R,S}\to X^2$ for its outer-coordinate map. Lemma 2.1 gives

$$
C_{R,S}
=\left(\bigvee_i\mu^{-1}F_i\right)\vee\mu^{-1}G.
\tag{3.1}
$$

All three coordinate maps from $C_{R,S}$ to $Q$ agree, since $R,S\le K$.

**Cutoff pieces.** Each $F_i$ comes from $Q$, so restricting the middle coordinate to $F_i$ forces the first and third coordinates into $F_i$ as well. The image of this piece therefore satisfies

$$
e[\mu^{-1}F_i]\le K\wedge(F_i\times F_i)\le H.
\tag{3.2}
$$

This is a localic kernel-pair statement, not an argument from ordinary points.

**Generic piece.** Let $r_R:R\to Q$ and $r_S:S\to Q$ be their common quotient-coordinate maps. Base-change associativity gives the following explicit identification:

$$
\begin{aligned}
\mu^{-1}G
&\cong C_{R,S}\times_Q1\\
&\cong(R\times_Q1)\times_{X\times_Q1}(S\times_Q1)\\
&\cong R_G\times_GS_G.
\end{aligned}
\tag{3.3}
$$

Here $R\times_Q1\cong R\wedge B$ because $R\le K$, and similarly for $S$. In particular, (3.3) identifies **the actual pullback before any image is taken**. Its outer image, as a sublocale of $B\le X^2$, is precisely $R_G\circ_GS_G$.

Localic images preserve arbitrary joins of sublocales. Taking the image of (3.1) and applying (3.2)–(3.3) gives

$$
R\circ_XS\le H\vee(R_G\circ_GS_G).
$$

The generic composite is contained in the global composite. Also
$H=H\circ_X\Delta_X\le R\circ_XS$, using $H\le R$ and $\Delta_X\le S$. These give the reverse inclusion, proving (GL1).

Because the sublocale lattice is distributive for **finite** operations,

$$
\begin{aligned}
(R\circ_XS)\wedge B
 &=(H\wedge B)\vee(R_G\circ_GS_G)\\
 &=D\vee(R_G\circ_GS_G).
\end{aligned}
$$

The second term contains $D$: for example,
$D=D\circ_G\Delta_G\le R_G\circ_GS_G$ since $D\le R_G$ and $\Delta_G\le S_G$. Therefore (GL2) follows. $\square$

**Typing note.** The interval $[H,K]$ is closed under composition: $H\le R\circ_XS$ by the unit argument just given, while $R\circ_XS\le K$ because its outer-coordinate map factors through the transitive kernel-pair relation $K$.

## 4. The special base-changed surjection (19)

Set $T=H\circ_XH$ and $A=T\wedge B$. Theorem 3.1 gives

$$
\boxed{T=H\vee D^2,\qquad A=D^2:=D\circ_GD.}
\tag{4.1}
$$

Let $C=H\times_XH$, and factor its outer-coordinate map through its localic image:

$$
C\overset{e}{\twoheadrightarrow}T\hookrightarrow X^2.
$$

All three quotient coordinates agree on $C$, and both quotient coordinates agree on $T\le K$. The same pullback calculation as (3.3) gives

$$
C\times_Q1\cong D\times_GD,
\qquad
T\times_Q1\cong A.
$$

Thus the base change $e_\infty:D\times_GD\to A$ has localic image $D\circ_GD$. By (4.1), that image is exactly the entire target $A$, so

$$
\boxed{e_\infty:D\times_GD\twoheadrightarrow A\quad\text{is surjective}.}
\tag{19}
$$

This is a **special image computation**, not a claim that arbitrary localic surjections remain surjective under base change.

## 5. The interval isomorphism, with composition and converse

By Proposition 2.2, $K=H\vee B$. Thus the assignments

$$
\begin{aligned}
\Phi:[H,K]&\longrightarrow[D,B],
&\Phi(R)&=R\wedge B,\\
\Psi:[D,B]&\longrightarrow[H,K],
&\Psi(Z)&=H\vee Z
\end{aligned}
\tag{5.1}
$$

are inverse order isomorphisms. Indeed, finite distributivity gives

$$
H\vee(R\wedge B)=(H\vee R)\wedge(H\vee B)=R
$$

for $H\le R\le K$, and

$$
(H\vee Z)\wedge B=(H\wedge B)\vee Z=D\vee Z=Z
$$

for $D\le Z\le B$.

By (GL2), this isomorphism preserves binary composition:

$$
\boxed{\Phi(R\circ_XS)=\Phi(R)\circ_G\Phi(S).}
\tag{5.2}
$$

Equivalently,

$$
\boxed{(H\vee Z)\circ_X(H\vee W)=H\vee(Z\circ_GW)}
\quad(D\le Z,W\le B).
\tag{5.3}
$$

If $H$ is symmetric, converse of relations is preserved and reflected as well, since $B$ is symmetric. The isomorphism therefore identifies the (possibly nonassociative) composition structures on the two complete lattice intervals.

**Corollary 5.1 (all fixed bracketings).** For any finite fully parenthesized composition word $w$ in copies of $H$, and the *same binary tree* $w_G$ evaluated at $D$,

$$
\boxed{w_X(H)=H\vee w_G(D),\qquad w_X(H)\wedge B=w_G(D).}
\tag{5.4}
$$

This is proved by induction on the binary tree; no associativity is inferred.

**Corollary 5.2 (transitivity and equivalence hulls).** For $R\in[H,K]$, transitivity of $R$ is equivalent to transitivity of $R_G$. If $H$ is symmetric, equivalence relations in $[H,K]$ correspond to equivalence relations in $[D,B]$, and

$$
\boxed{\operatorname{EqHull}_X(H)
=H\vee\operatorname{EqHull}_G(D).}
\tag{5.5}
$$

The full hull on the left lies in $K$, because $K$ is an equivalence relation containing $H$, and similarly the generic hull lies in $B$.

## 6. Additional conclusions from the referee's addendum

**Associativity reflection.** Since $\Phi$ is injective and preserves composition, for all $R,S,U\in[H,K]$ (using $U$ here to avoid confusion with $T=H\circ_XH$),

$$
\boxed{
(R\circ_XS)\circ_XU=R\circ_X(S\circ_XU)
\iff
(R_G\circ_GS_G)\circ_GU_G
=R_G\circ_G(S_G\circ_GU_G).
}
\tag{6.1}
$$

In particular, associativity holds throughout $[H,K]$ if and only if it holds throughout $[D,B]$. This reflects *each particular associativity defect*, not merely a universal associativity axiom.

**Balanced four-step equivalence.** With $T=H\circ_XH$,

$$
\boxed{
(D^2\circ_GD^2=B)
\iff
((H\circ_XH)\circ_X(H\circ_XH)=K).
}
\tag{6.2}
$$

Both expressions have the specified balanced four-factor bracketing. Equation (6.2) is a **reformulation** of the remaining geometric target, not a proof of either side.

**Transfinite squaring stages.** Define

$$
R_0=H,\quad R_{\alpha+1}=R_\alpha\circ_XR_\alpha,\quad
R_\lambda=\bigvee_{\alpha<\lambda}R_\alpha,
$$

and define $Z_\alpha$ by the same recursion with $Z_0=D$ and composition over $G$. The sequences are increasing because their terms contain the diagonal. Since an order isomorphism between complete lattice intervals preserves all joins, transfinite induction gives

$$
\boxed{\Phi(R_\alpha)=Z_\alpha\quad\text{for every ordinal }\alpha.}
\tag{6.3}
$$

Thus each equality $R_{\alpha+1}=R_\alpha$ holds exactly when $Z_{\alpha+1}=Z_\alpha$. Their first stabilization ordinal is the same, and the stable values are the corresponding transitive closures (equivalence hulls in the symmetric setting). Stabilization eventually occurs because the intervals are set-sized. This formal observation provides **no finite rank bound** and does not motivate pursuing ordinal constructions presently.

## 7. Finite-fence specialization and audit qualifications

In the concrete compact ordered interval, the closed component-saturated cutoffs $F_i$ meet the countable set of fence vertices in finitely many points, and their complements $U_i$ are quotient-open. The previously verified **exact point-fibre** lemma states $G=\bigwedge_iU_i$; its proof uses *both positive and negative quotient-open tests*. The previously verified **finite-cutoff rigidity** lemma asserts $K\wedge(F_i\times F_i)=H\wedge(F_i\times F_i)$.

The most delicate finite-cutoff proof is the one on $F_i=A\vee O$: $A$ is the finite union of nonsingleton components, whereas the singleton remainder $O$ need not be finite. Every relative open $W\subseteq O$ extends to a quotient-open via $P\setminus(F_i\setminus W)$, since $F_i\setminus W$ is compact and component-saturated. This proves that $q|_O$ is a **locale embedding**, so the kernel pair restricted to $O^2$ is $\Delta_O$. On the finite component block $A^2$, quotient opens separate distinct components, and the block is finite spatial, so the kernel pair is exactly the join of its finitely many component squares. Mixed blocks vanish using the quotient open $P\setminus A$. The resulting four-block argument establishes (C).

**Verification ledger**

| Statement | Present status |
| --- | --- |
| Abstract cutoff decomposition (L), automatic kernel decomposition (K) | Independently blind-refereed, positive |
| Composition localization (GL1–GL2), surjection (19) | Independently blind-refereed, positive |
| Interval isomorphism, fixed bracketings, transitivity, equivalence hulls | Independently blind-refereed, positive |
| Associativity reflection, balanced four-step equivalence, transfinite-stage correspondence | Referee's formal addendum; independently checked against the main theorem |
| Finite-fence exact fibre (F) and cutoff rigidity (C) | Previously independently audited; current referee checked proofs from declared geometric inputs |
| Complete explicit geometric coordinate construction | Outside scope of this particular blind audit; prior separate checks apply |
| $D^2\circ_GD^2=B$ and global four-step effectivity | **Still conditional on the separately qualified Cantor-fusion argument** |

### Audit archive

- [Independent blind referee report](project-a/audits/2026-11-19/GENERIC_FIBRE_COMPOSITION/INDEPENDENT_BLIND_REFEREE_REPORT.md)
- [Referee's additional mathematical observations](project-a/audits/2026-11-19/GENERIC_FIBRE_COMPOSITION/REFEREE_ADDENDUM.md)
- [Claim-by-claim reconciliation](project-a/audits/2026-11-19/GENERIC_FIBRE_COMPOSITION/POSTREFEREE_RECONCILIATION.md)
- [Archive index](project-a/audits/2026-11-19/GENERIC_FIBRE_COMPOSITION/README.md)

### Related project notes

- *ProjectA_FourStep_Effectivity_Consolidated_2026-11-19.md*: exact finite-fence hypotheses and cutoff proof.
- *ProjectA_Global_Generic_Square_SelfContained_2026-11-19.md*: separate conditional global Cantor-fusion argument.
- *ProjectA_General_Transitivity_Directed_Joins_2026-11-19.md*: nonuniversality of arbitrary localic surjective covers.

**Next problem:** establish, simplify, or refute the remaining global geometric step $D^2\circ_GD^2=B$. The present localization results do not supply that equality on their own.
