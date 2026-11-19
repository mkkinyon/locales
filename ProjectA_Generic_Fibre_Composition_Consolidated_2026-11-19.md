# Project A — generic-fibre localization of localic relation composition

**19 November 2026. Self-contained theorem note; internally adversarially checked, not yet independently audited.**

## 1. Result and verification boundary

In the two-colour finite-fence construction, let (q:X\to Q) be the component quotient, (K=K_q=X\times_QX), and (H\le K) the reflexive symmetric point-generated component relation. Let (p_\infty:1\to Q) be the generic point, (G=X\times_Q1) its actual localic fibre, and

\[
B=G\times G\le X\times X,\qquad D=H\wedge B.
\]

The main new conclusion is that, for all localic relations (R,S) with (H\le R,S\le K),

\[
\boxed{R\circ_XS=H\vee\bigl((R\wedge B)\circ_G(S\wedge B)\bigr),}
\tag{GL1}
\]

and therefore

\[
\boxed{(R\circ_XS)\wedge B=(R\wedge B)\circ_G(S\wedge B).}
\tag{GL2}
\]

Here composition is always defined as the localic image of the **actual composability pullback**; no associativity is assumed. The global generic-fibre identity for (T=H\circ_XH) follows:

\[
\boxed{T=H\vee D^2,\qquad A:=T\wedge B=D^2:=D\circ_GD.}
\tag{GL3}
\]

Consequently, the canonical base-changed image map

\[
\boxed{e_\infty:D\times_GD\longrightarrow A}
\tag{19}
\]

is a **surjection of locales**. This answers the previously open question (19) affirmatively, assuming the independently checked cutoff lemmas below. It is *not* an assertion of arbitrary base-change stability for localic surjections.

The exact point-fibre formula and finite-cutoff rigidity were checked by the independent 19 November referee in `ProjectA_FourStep_Effectivity_INDEPENDENT_BLIND_REFEREE_REPORT_2026-11-19.md`; the composition-localization argument in this note is **new and internally checked only**. The separate global Cantor-fusion statement yielding four-step effectivity remains *qualified/conditional*.

## 2. Abstract hypotheses

The proof applies in the following general setting, without reference to a particular Cantor set or finite-fence coordinate system.

* (q:X\to Q) is a locale map, (K=X\times_QX\le X^2) its kernel-pair relation.
* (p:1\to Q) is a point with fibre (G=X\times_Q1); put (B=G^2\le X^2).
* (H\le K) is a reflexive localic relation, so (\Delta_X\le H). Symmetry is not required until the equivalence-hull corollary.
* (F_i\le X) are closed sublocales **pulled back from closed sublocales of (Q)**, and (U_i=X\setminus F_i) are their complementary opens. They satisfy the exact localic formula

  \[
  \boxed{G=\bigwedge_i U_i.}\tag{F}
  \]

* Each cutoff is rigid:

  \[
  \boxed{K\wedge(F_i\times F_i)\le H.}\tag{C}
  \]

In the finite-fence model, (F_i) ranges over Euclidean-compact component-saturated closed sets containing finitely many fence vertices. Their quotient-pullback property, (F), and (C) are precisely the independently audited cutoff inputs. **Both positive and negative quotient-point tests** are needed for the proof of (F) in that model; merely intersecting positive neighbourhoods is not a generic point-fibre formula in arbitrary locales.

The assumption that (F_i) descends from (Q) is essential: it lets a cutoff condition on one coordinate of the kernel pair propagate to every coordinate.

## 3. Complemented-cutoff decomposition

**Lemma 3.1 (coframe decomposition).** For any locale map (f:Y\to X),

\[
\boxed{Y=\left(\bigvee_i f^{-1}F_i\right)\vee f^{-1}G.}\tag{L}
\]

**Proof.** Write (V=\bigvee_i f^{-1}F_i). Pullback of sublocales preserves arbitrary meets and finite joins, and takes complementary open/closed pairs to complementary pairs. Since the lattice of sublocales of (Y) is a coframe,

\[
\begin{aligned}
V\vee f^{-1}G
 &=V\vee\bigwedge_i f^{-1}U_i\\
 &=\bigwedge_i\bigl(V\vee f^{-1}U_i\bigr)\\
 &=Y,
\end{aligned}
\]

because (V\ge f^{-1}F_i) and (f^{-1}F_i\vee f^{-1}U_i=Y) for every (i). No unjustified interchange of an infinite join and a meet occurs. \(\square\)

## 4. Middle-coordinate localization theorem

For (H\le R,S\le K), write

\[
R_G=R\wedge B,\qquad S_G=S\wedge B.
\]

These are reflexive relations on (G), since (\Delta_G\le D\le R_G,S_G).

**Theorem 4.1 (composition localization).** Under the hypotheses in §2, equations (GL1) and (GL2) hold.

**Proof.** Form the genuine localic composability pullback

\[
C_{R,S}=R\times_X S
\]

with middle-coordinate map (\mu:C_{R,S}\to X) and outer-coordinate map (e:C_{R,S}\to X^2). By Lemma 3.1,

\[
C_{R,S}=\left(\bigvee_i\mu^{-1}F_i\right)\vee\mu^{-1}G.
\tag{4.1}
\]

**Cutoff part.** As (R,S\le K), all three quotient coordinates agree on (C_{R,S}). Since (F_i) is pulled back from (Q), the middle-coordinate restriction (\mu^{-1}F_i) forces **both outer coordinates into (F_i)**. Its image under (e) is therefore contained in

\[
K\wedge(F_i\times F_i)\le H.
\tag{4.2}
\]

This argument uses the localic kernel-pair identities; it does not reason only from ordinary points.

**Generic part.** The same quotient-coordinate equality implies that, when the middle coordinate lies in (G), both outer coordinates lie in (G). There is consequently an isomorphism of the actual composability pullbacks

\[
\boxed{\mu^{-1}G\cong R_G\times_G S_G.}
\tag{4.3}
\]

The image of this summand under (e) is exactly (R_G\circ_GS_G), embedded in (B\le X^2). This is an identification **before** taking the localic image, and does not assume that images commute with arbitrary base change.

Localic images preserve arbitrary joins of sublocales. Taking the outer images of (4.1), and using (4.2)–(4.3), yields

\[
R\circ_X S\le H\vee(R_G\circ_G S_G).
\]

For the opposite inclusion, (R_G\circ_G S_G\le R\circ_XS) by the inclusion of the generic composability locale. Further, (H\le R\circ_XS): for each (H\le R), compose with (\Delta_X\le S) and use the unit law (H\circ\Delta_X=H). Thus (GL1) holds.

Intersect (GL1) with (B). **Finite**, ordinary distributivity in the sublocale lattice gives

\[
\begin{aligned}
(R\circ_XS)\wedge B
 &=(H\wedge B)\vee(R_G\circ_G S_G)\\
 &=D\vee(R_G\circ_G S_G).
\end{aligned}
\]

Finally (D\le R_G\circ_GS_G), since (\Delta_G\le R_G) and (D\le S_G) (unit law). This proves (GL2). \(\square\)

## 5. The surjection (19)

Set (R=S=H) in Theorem 4.1 and let (T=H\circ_XH). Then

\[
T=H\vee(D\circ_GD),\qquad T\wedge B=D\circ_GD.
\]

Set (A=T\wedge B). By definition the composite (D\circ_GD) is the localic image of

\[
D\times_GD\longrightarrow G\times G.
\]

Because this image is **exactly** (A), the induced map (e_\infty:D\times_GD\to A) is surjective. Moreover, since (T\le K), the map (T\to Q) can be taken from either outer coordinate and its fibre at (p) is (A). Likewise the fibre of (H\times_XH\to Q) is (D\times_GD). Hence (e_\infty) is precisely the base change along (p) of the usual surjective image-factor map (H\times_XH\twoheadrightarrow T).

The conclusion is special to this cutoff-rigid situation. Nothing here proves that the original image-factor map is universally surjective.

## 6. The interval composition correspondence

The established residual decomposition of the kernel pair is

\[
\boxed{K=H\vee B.}\tag{K}
\]

Put (D=H\wedge B). The two assignments

\[
\begin{aligned}
\Phi:[H,K]&\longrightarrow[D,B],&\Phi(R)&=R\wedge B,\\
\Psi:[D,B]&\longrightarrow[H,K],&\Psi(Z)&=H\vee Z
\end{aligned}
\tag{6.1}
\]

are mutually inverse order isomorphisms. Indeed, if (H\le R\le K), then, by finite distributivity,

\[
H\vee(R\wedge B)=(H\vee R)\wedge(H\vee B)=R\wedge K=R.
\]

If (D\le Z\le B), then

\[
(H\vee Z)\wedge B=(H\wedge B)\vee Z=D\vee Z=Z.
\]

Theorem 4.1 adds preservation of relational composition:

\[
\boxed{\Phi(R\circ_XS)=\Phi(R)\circ_G\Phi(S).}\tag{6.2}
\]

The inverse correspondence is therefore composition-preserving as well:

\[
\boxed{(H\vee Z)\circ_X(H\vee W)=H\vee(Z\circ_GW)}
\qquad(D\le Z,W\le B).
\tag{6.3}
\]

No associativity is asserted. Since (H) and (B) are symmetric in the finite-fence application, the correspondence also preserves and reflects converse (taking the opposite relation).

**Corollary 6.1 (all finite bracketings).** If (w) is any fully parenthesized finite word in (H), and (w_G) is the *same binary tree* evaluated at (D), then

\[
\boxed{w_X(H)=H\vee w_G(D),\qquad w_X(H)\wedge B=w_G(D).}
\tag{6.4}
\]

For example, with (T=H^2) and fixed bracketing (T\circ_XT),

\[
T=H\vee D^2,\qquad
T\circ_X T=H\vee(D^2\circ_GD^2).
\]

**Corollary 6.2 (transitivity and equivalence hulls).** For (R\in[H,K]), (R\circ_XR\le R) iff (R_G\circ_GR_G\le R_G). In the symmetric setting, equivalence relations in ([H,K]) correspond exactly to equivalence relations in ([D,B]). Therefore

\[
\boxed{\operatorname{EqHull}_X(H)=H\vee\operatorname{EqHull}_G(D).}
\tag{6.5}
\]

The full equivalence hull on the left is contained in (K), because (K) is an equivalence relation containing (H); similarly, the generic hull lies in the total relation (B).

## 7. Internal adversarial audit and dependency ledger

1. **Correct fibre, not positive neighbourhoods alone.** The model-specific formula (F) was proved with both positive and negative quotient-open tests and independently checked. This note assumes (F) as a locale equality.
2. **Middle-coordinate propagation.** The cutoff (F_i) must descend from (Q). Mere closedness in (X), or a statement only about ordinary components, is insufficient for (4.2).
3. **Legitimate distributivity.** Lemma 3.1 uses the coframe law (V\vee\bigwedge_i W_i=\bigwedge_i(V\vee W_i)). The later intersection with (B) is a *finite* distributive calculation. No infinite-meet-over-join law is invoked.
4. **Image preservation.** Direct images of sublocales preserve arbitrary joins, as left adjoints of sublocale pullback. This is applied to (4.1), after decomposing the genuine composability pullback.
5. **Base-change issue.** Equation (4.3) is an isomorphism of pullbacks, not a claim about pulling back an image. The surjectivity of (e_\infty) is **deduced**, not assumed.
6. **Units and bracketing.** (H\) is reflexive. Unit laws justify (H\le R\circ S) and (D\le R_G\circ S_G). Every later iterate retains its specified binary parentheses.
7. **Lattice interval.** The order isomorphism (6.1) uses only the separately proved (K=H\vee B) and binary distributivity; its composition compatibility additionally uses the new theorem.

| Claim | Present status | Inputs |
| --- | --- | --- |
| Generic fibre (F) | Independently checked | Geometry and both quotient-point tests |
| Finite-cutoff rigidity (C) | Independently checked | Finite-vertex cutoff and localic quotient embedding |
| Kernel decomposition (K) | Independently checked | (F), (C), coframe lemma |
| Composition localization (GL1–GL2) | **New; internal audit only** | (F), (C), kernel-pair identities, standard sublocale algebra |
| (A=D^2) and surjection (19) | **New; internal audit only** | Composition localization |
| Interval composition equivalence and hull formula | **New; internal audit only** | (K), composition localization |
| (D^2\circ_GD^2=B) and global four-step effectivity | **Conditional / qualified external checks** | Separate global Cantor-fusion construction |

### Recommended independent review

Ask a blind referee to check, in particular, whether (4.3) and the image calculation from (4.1) are valid for arbitrary locales, whether the finite-cutoff image inclusion (4.2) needs an additional assumption beyond those stated, and whether (6.5) follows without an associativity hypothesis. Supply (F), (C), and (K) as separately audited inputs, but avoid disclosing the present internal checklist until after the independent report.

### Project references

- `ProjectA_FourStep_Effectivity_Consolidated_2026-11-19.md` — exact finite-fence assumptions, cutoff lemmas, kernel decomposition and verification boundary.
- `ProjectA_FourStep_Effectivity_INDEPENDENT_BLIND_REFEREE_REPORT_2026-11-19.md` and `ProjectA_FourStep_Effectivity_REFEREE_ADDENDUM_2026-11-19.md` — independent reviews of the cutoff and coframe inputs.
- `ProjectA_Global_Generic_Square_SelfContained_2026-11-19.md` — separate conditional global Cantor-fusion argument.
- T. Bayih, T. Dube and O. Ighedo, *On the Menger and almost Menger properties in locales*, **Applied General Topology** 22 (2021), §1.2, for standard coframe and image/pullback facts.
- I. Arrieta and A. L. Suárez, *The coframe of D-sublocales of a locale and the (T_D) duality*, §2, for the same sublocale calculus.
