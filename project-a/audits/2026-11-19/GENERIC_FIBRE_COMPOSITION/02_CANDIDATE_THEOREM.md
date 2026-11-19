# Candidate theorem: composition localized to a quotient-point fibre

**Mathematical status: candidate supplied for independent blind scrutiny.**

## 1. Data, conventions, and hypotheses

All relations are sublocales of (X\times X), with order by inclusion. The composite (R\circ_X S) is the **localic image** of the outer-coordinate map from the actual composability pullback (R\times_X S\to X^2), with convention ((x,y)\in R\), ((y,z)\in S\). In general, no associativity of this operation is assumed.

Let (q:X\to Q) be a locale map, and (K=X\times_QX\le X^2) its kernel-pair relation. Let (H\le K) be reflexive, (\Delta_X\le H), and fix a point (p:1\to Q). Define its **actual** fibre and the corresponding square by

\[
G=X\times_Q1,\qquad B=G\times G\le X^2,\qquad D=H\wedge B.
\]

Assume a family of **closed** sublocales (F_i\le X), each the pullback of a closed sublocale of (Q), with open complements (U_i=X\setminus F_i), such that:

\[
\boxed{G=\bigwedge_i U_i;}\tag{F}
\qquad
\boxed{K\wedge(F_i\times F_i)\le H\quad\text{for every }i.}\tag{C}
\]

The fibres and intersections here are in **Loc**. In particular (F) is a locale equality, not merely a statement that all ordinary points of (G) lie in each (U_i).

For (H\le R,S\le K), abbreviate (R_G=R\wedge B\) and (S_G=S\wedge B); they are localic relations on (G), containing (D), hence reflexive.

## 2. Decomposition lemma

**Lemma 2.1.** For every locale map (f:Y\to X),

\[
\boxed{Y=\bigl(\bigvee_i f^{-1}F_i\bigr)\vee f^{-1}G.}\tag{L}
\]

**Proposed proof.** Put (V=\bigvee_i f^{-1}F_i). Inverse image on sublocales preserves arbitrary meets and finite joins, in particular the complementary joins (F_i\vee U_i=X). Since the lattice of sublocales is a coframe,

\[
\begin{aligned}
V\vee f^{-1}G
&=V\vee\bigwedge_i f^{-1}U_i\\
&=\bigwedge_i(V\vee f^{-1}U_i)=Y.
\end{aligned}
\]

This uses the coframe law distributing a *fixed join* over an arbitrary meet. \(\square\)

## 3. Localization of binary composition

**Candidate theorem 3.1.** For all (H\le R,S\le K),

\[
\boxed{R\circ_XS=H\vee(R_G\circ_G S_G),}\tag{1}
\]

and

\[
\boxed{(R\circ_XS)\wedge B=R_G\circ_GS_G.}\tag{2}
\]

**Proposed proof.** Form the actual composability locale

\[
C_{R,S}=R\times_X S,
\]

and denote its middle-coordinate map by (\mu:C_{R,S}\to X) and its outer-coordinate map by (e:C_{R,S}\to X^2). Lemma 2.1 applied to (\mu) yields

\[
C_{R,S}
=\left(\bigvee_i\mu^{-1}F_i\right)\vee\mu^{-1}G.
\tag{3}
\]

The three quotient-coordinate maps (C_{R,S}\to Q) agree, because (R,S\le K).

1. **Cutoff middle.** Since each (F_i\le X) is pulled back from a closed sublocale of (Q), if the middle coordinate belongs to (F_i) then both outer coordinates belong to (F_i). The image of (\mu^{-1}F_i\) under (e) is therefore contained in

   \[
   K\wedge(F_i\times F_i)\le H.
   \tag{4}
   \]

2. **Generic middle.** If the middle coordinate belongs to (G), then both outer coordinates belong to (G), by the same equality of their quotient maps. Thus the actual pullbacks agree:

   \[
   \boxed{\mu^{-1}G\cong R_G\times_G S_G.}
   \tag{5}
   \]

   The image of this summand under (e), viewed in (B\le X^2), is exactly (R_G\circ_GS_G).

Since localic images preserve arbitrary joins of sublocales, (3)–(5) give

\[
R\circ_XS\le H\vee(R_G\circ_GS_G).
\]

The reverse inequality follows from (R_G\circ_GS_G\le R\circ_XS) and (H\le R\circ_XS). The latter follows from (H\le R), (\Delta_X\le S), and (H\circ_X\Delta_X=H). This proves (1).

Intersect (1) with (B), using finite distributivity in the sublocale lattice:

\[
\begin{aligned}
(R\circ_XS)\wedge B
&=(H\wedge B)\vee(R_G\circ_GS_G)\\
&=D\vee(R_G\circ_GS_G).
\end{aligned}
\]

Since (\Delta_G\le R_G) and (D\le S_G), the unit law gives (D\le R_G\circ_GS_G); hence (2). \(\square\)

## 4. The base-change question (19)

Set (T=H\circ_XH), (A=T\wedge B), and (D=H\wedge B). Theorem 3.1 with (R=S=H) gives

\[
\boxed{T=H\vee D^2,\qquad A=D^2:=D\circ_GD.}\tag{6}
\]

Let (C=H\times_XH), and factor its outer-coordinate map through its localic image:

\[
C\overset{e}{\twoheadrightarrow}T\hookrightarrow X^2.
\]

The quotient coordinates agree on both (C) and (T), so these locales map to (Q). Their fibres over (p) are respectively

\[
C\times_Q1\cong D\times_GD,
\qquad T\times_Q1\cong A.
\]

Consequently the base change (e_\infty:D\times_GD\to A) has image (D^2=A), by (6). **Candidate conclusion:**

\[
\boxed{e_\infty:D\times_GD\twoheadrightarrow A\text{ is a localic surjection}.}\tag{19}
\]

The proof does **not** claim that general localic surjections remain surjective under arbitrary base change; the special surjectivity is deduced from (F) and (C).

## 5. Interval isomorphism and bracketed powers

Assume, in addition, the kernel-pair decomposition

\[
\boxed{K=H\vee B.}\tag{K}
\]

There are proposed mutually inverse order isomorphisms

\[
\begin{aligned}
\Phi:[H,K]&\to[D,B],&\Phi(R)&=R\wedge B,\\
\Psi:[D,B]&\to[H,K],&\Psi(Z)&=H\vee Z.
\end{aligned}
\tag{7}
\]

Indeed, for (H\le R\le K),

\[
H\vee(R\wedge B)=(H\vee R)\wedge(H\vee B)=R,
\]

and for (D\le Z\le B),

\[
(H\vee Z)\wedge B=(H\wedge B)\vee Z=Z.
\]

By (2) this isomorphism preserves binary relational composition:

\[
\boxed{\Phi(R\circ_XS)=\Phi(R)\circ_G\Phi(S).}\tag{8}
\]

Thus for any *fixed full parenthesization* (w) of a finite product of copies of (H), evaluation of the same binary tree on (D) satisfies

\[
\boxed{w_X(H)=H\vee w_G(D),\qquad w_X(H)\wedge B=w_G(D).}\tag{9}
\]

Moreover, (R\) is transitive iff (R_G\) is transitive. If (H) is symmetric, then (7) respects converse and equivalence relations correspond. In that case the proposed hull formula is

\[
\boxed{\operatorname{EqHull}_X(H)=H\vee\operatorname{EqHull}_G(D).}\tag{10}
\]

The equivalence hulls here are least reflexive symmetric transitive sublocales; (K) and (B) are total upper bounds, respectively.

**Separate outstanding issue, not part of the present theorem:** The stronger four-step claim (D^2\circ_GD^2=B) requires an additional global Cantor-fusion argument. Neither (19) nor (1)–(10) alone establishes that equality.
