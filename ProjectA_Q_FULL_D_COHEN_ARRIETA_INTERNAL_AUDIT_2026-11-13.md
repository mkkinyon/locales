# Internal adversarial audit — Cohen × Arrieta full fitted-diagonal product failure

**13 November 2026. INTERNAL — do not provide to the blind referee before its independent verdict.**

## 1. Scope and verdict

Audited the newly proposed general closed-graph theorem and the explicit Cohen × Arrieta specialization, together with the predecessor finite-\(D_2\) example and the stated distinction from Q/Q′. Primary source: Igor Arrieta, *Localic separation and the duality between closedness and fittedness*, arXiv:2310.18522, especially §§2.5 and 4, Cor. 4.3, Prop. 4.4, Ex. 4.5.

**Verdict: PASS, subject to an independent adversarial review.** No fatal mathematical gap was found in the main strict product inequality

\[
D(Z_C\times A)\subsetneq\Delta_{Z_C}\times D(A).
\]

The general theorem also survives scrutiny: for a **strongly Hausdorff** locale \(Y\), the full \(D\)-product formula holds over *every* Boolean base iff \(D(Y)=\Delta_Y\). The negative direction produces **some** Boolean base; the separate explicit construction identifies Cohen for Arrieta. This is an internal proof review, not a formal verification, novelty check, or independent external certificate.

## 2. Adversarial checks, one by one

| Claim / attempted attack | Finding |
| --- | --- |
| Does “strongly Hausdorff” actually mean **localically closed diagonal**, not ordinary Hausdorffness? | **Yes.** Arrieta §2.5 identifies Isbell strong Hausdorff with a closed locale diagonal, and Cor. 4.3 gives it for the construction. Merely using ordinary Hausdorffness would be invalid. |
| Is \(D(Y)\not\le\Delta_Y\) enough to obtain nonzero off-diagonal \(E=D(Y)\wedge O(\delta_Y)\)? | **Yes**, because \(\Delta_Y=C(\delta_Y)\) is closed. A sublocale disjoint from its open complement factors through the closed sublocale. |
| Does Booleanization \(B(E)\) stay nonzero and yield maps \(f,g:B(E)\to Y\) that match **all** \(Y\)-covers? | **Yes.** Nonzero locales have nonzero double-negation sublocales. The map factors through the **full** fitted diagonal \(D(Y)\), whose defining cover squares are all met. |
| Does factorization through the open complement of \(\Delta_Y\) make the equalizer \(\operatorname{eq}(f,g)\) zero as a **sublocale**, not merely at ordinary points? | **Yes.** The equalizer is the pullback of \(\Delta_Y\), while the pair factors through its complementary open. |
| Are the graphs \(\Gamma_f,\Gamma_g\subseteq Z\times Y\) closed? | **Yes**, as pullbacks of the closed diagonal along \((f\pi_Z,\pi_Y)\), \((g\pi_Z,\pi_Y)\). The section images are these graphs. |
| Does empty equalizer force the two graph-complement opens to **cover**? | **Yes.** The meet of closed graphs is their pullback/equalizer. If \(\Gamma_f=C(u_f)\) and \(\Gamma_g=C(u_g)\), then \(C(u_f)\wedge C(u_g)=C(u_f\vee u_g)=0\), so \(u_f\vee u_g=1\). |
| Does the binary cover truly separate the two *product* sections? | **Yes.** \(s_f^*(u_f)=0\), \(s_g^*(u_g)=0\); hence each term in the binary matching join vanishes. But the pair has the same \(Z\)-coordinate and its \(Y\)-coordinates lie in \(D(Y)\). |
| Is the reverse inequality \(D(Z\times Y)\le\Delta_Z\times D(Y)\) justified? | **Yes.** Projection naturality gives \(D(Z\times Y)\le D(Z)\times D(Y)\), and \(D(Z)=\Delta_Z\) for Boolean locales (already independently checked in the project). |
| Is \(RO(2^\omega\times2^\omega)\) genuinely the Cohen Boolean algebra? | **Yes.** The Cantor square is homeomorphic to Cantor space; regular-open frames are consequently isomorphic complete Boolean algebras. |
| Is the “regularize the Cantor trace” construction a **frame map**? | **Yes**, with **regular-open** joins. If two Cantor opens have equal traces on dense \(Y\), their closures coincide; double negation preserves finite meets and takes arbitrary unions to joins in the regular-open frame. Thus \(O(Y)\to RO(C)\) exists and composes with \(O(A)\to O(Y)\). |
| Does the independent-coordinate pair match **all** Arrieta covers? | **Yes.** For any nonempty Cantor rectangle \(R\times S\), choose sufficiently large \(n\) with \(K_n\cap R\ne\varnothing\ne K_n\cap S\). A member \(u\) of the given \(A\)-cover contains \(n\), hence its \(Y\)-trace contains a neighbourhood of *all* \(K_n\). Its two regularized coordinate values have nonzero meet on a subrectangle of \(R\times S\). The join is dense in \(C^2\), therefore equals 1 in \(RO(C^2)\). |
| Is the equalizer of independent coordinate maps empty **locale-theoretically**? | **Yes.** Agreement on the opens \(a_n=(Y\cap[x_n=1])\cup\{n\}\) forces agreement of each coordinate bit. The equality clopens \(e_n\in RO(C^2)\) have complete Boolean meet \(\bigwedge_n e_n=\operatorname{int}\Delta_C=0\). In a Boolean locale every sublocale is open/closed, so the equalizer is zero. |
| Could the result contradict referee N3 or settle Q/Q′? | **No.** N3 concerns **closed** \(W,W_2,U\); this theorem concerns nonclosed \(D\). The separated pair fails a **binary product cover**, hence it is already **outside \(D_2(Z_C\times A)\)**. It is not a weak internal \(D_2\)-hole. |

## 3. Explicit repair/clarification recommendations

1. **State the frame-map factorization carefully.** Let \(q:O(C)\to RO(C^2)\) be regularization after inverse image of a coordinate projection. Because \(Y\subseteq C\) is dense, \(q\) factors uniquely through restriction \(O(C)\twoheadrightarrow O(Y)\). Do not use the ordinary union as the join in \(RO(C^2)\).
2. **Do not replace localic strong Hausdorffness by topological Hausdorffness.** The binary graph cover depends on *closed sublocales* of a localic product. This is the essential imported source hypothesis.
3. **Distinguish two Boolean pairs.** The earlier “coordinatewise complements” pair is only finite-compatible and yields \(D_2\)-product failure. The new **independent** coordinates are compatible with *all* covers and are indispensable for full-\(D\) failure.
4. **Distinguish three defects:** \(D_2(A)\setminus D(A)\), product failure \((\Delta_Z\times D(A))\setminus D(Z\times A)\), and the **internal** Q′ weak defect \(D_2(X)\wedge C(w_C)\). The new graph pair lies outside the product's \(D_2\); it is not a Q′ witness.
5. **Avoid false forcing-language shortcuts.** The proof uses the actual complete Boolean frame \(RO(C^2)\) and actual localic graphs. “Two new Cohen reals” is explanatory prose, not a substitute for frame equations.
6. **General theorem quantifiers:** “There exists *some* Boolean \(Z\)” follows abstractly for strongly Hausdorff non-F-separated \(Y\). “\(Z\) can be Cohen” is proved only for the explicit Arrieta choice.

The canonical repository proof already incorporates most of these distinctions. A concise insertion explaining the frame quotient and the complete Boolean meet would make the external packet self-contained.

## 4. Controls and negative tests

- **Finite \(D_2\) control:** The complementary-coordinate pair into \(RO(C)\) matches every finite Arrieta cover (one cover member contains infinitely many attached \(n\), hence has dense Cantor trace), but the countable cover \(\{a_n:n\in\omega\}\cup\{Y\cap[x_0=0]\}\) separates it. Its binary Cohen product splitting proves only \(D_2(Z_C\times A)\subsetneq\Delta_Z\times D_2(A)\). The full result does **not** rely on that pair.
- **Boolean bases with strong distributivity:** The earlier SD\(_\omega\) positive product theorem is consistent with this negative theorem; it supplies no distinct everywhere-D-compatible maps into Arrieta. A Cohen base does, and lacks SD\(_\omega\).
- **Pointed/discrete bases:** The abstract theorem does not claim that every Boolean base fails. Spatial Boolean bases are discrete and generally cannot carry the required nowhere-equal all-cover-compatible pair of ordinary points.
- **Nowhere-density viewpoint:** The intrinsic Q′ criterion remains \(B(D_2(X))\le D(X)\), equivalently each relatively closed \(D_2(X)\wedge C(w_C)\) is nowhere dense *in \(D_2(X)\)*. Product strictness alone does not test that criterion.

## 5. External audit priorities

The external referee should check independently and in order:

1. Categorical closed-graph theorem, especially all **sublocale** meets and complement joins.
2. Construction of the two frame maps into \(RO(C^2)\), including arbitrary joins.
3. All-cover compatibility by density of matching rectangles, and the source's K\(_n\) property.
4. Equalizer zero using the **complete** Boolean meet of equality clopens.
5. Whether the resulting pair really lies in \(\Delta_Z\times D(A)\) and fails a product **binary** cover.
6. Nonimplications for \(W,W_2,Q,Q′\) and the contrast with the \(D_2\) precursor.

**Disposition:** Keep the result in the working ledger as **internally audited, awaiting blind external review**. Do not alter the independently reviewed N3 closed-level theorem or mark Q/Q′ solved.

## 6. Source verification and a Boolean-sublocale detail

The primary arXiv PDF was rechecked on 13 November. Section 2.5 explicitly defines
strong Hausdorffness by a **closed diagonal** and Proposition 2.1(1)
records closed equalizers. Construction 4.2 gives the attached-point
topology, Corollary 4.3 preserves strong Hausdorffness, Example 4.5
is exactly the Cantor family \(K_n\), and Corollary 4.10 confirms that
this spatial locale is **not** F-separated. These were independently
checked against the source, not merely inferred from the project ledger.

For the equalizer argument, any nucleus \(j\) on a complete Boolean algebra
\(B\) has \(j(b)=b\vee a\), \(a=j(0)\). Indeed the reverse inequality
follows from
\(j(b)\wedge\neg b\le j(b)\wedge j(\neg b)=j(0)=a\).
Thus sublocales of the Cohen locale are represented by Boolean supports,
and agreement of two clopen bit values on the equalizer forces its support
under the corresponding equality clopen \(e_n\). This is stronger than
arguing only about ordinary points.
