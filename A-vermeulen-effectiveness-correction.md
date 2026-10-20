# Project A — Vermeulen resolves the proper-relation effectiveness question

**19 October 2026. Clean theorem memo for the forthcoming adversarial audit.** Corrects an earlier bibliography error. **Working corollary** (the cited Vermeulen effectiveness theorem itself is published). No novelty claim.

## 0. Correct primary source

J. J. C. Vermeulen, *Proper Maps of Locales*, **Journal of Pure and Applied Algebra** 92 (1994), 79–107, **Corollary 5.17**, p. 107. The scanned full-text index explicitly reads:

> "Closed proper equivalence relations (in particular closed equivalence relations on a compact locale) are effective."

https://core.ac.uk/download/pdf/82053693.pdf (search-indexed original scanned paper; downloading/opening the link was blocked with 403 in this research session). DOI: https://doi.org/10.1016/0022-4049(94)90047-7 .

**This is a theorem for arbitrary ambient locales**, NOT just compact ones. The compact parenthesis is merely an example. Karazeris–Tsamis, *Regular and Effective Regular Categories of Locales* (2020), Theorem 4.3, invokes precisely that compact special case; our earlier reading mistakenly narrowed the original theorem.

Vermeulen's **Corollary 5.14** is a different sufficient effectivity theorem for proper *weakly fitted* equivalence relations. For a **closed proper** relation we can and should invoke 5.17 without any weak-fitting claim.

See also G. Manuell, *Presenting Quotient Locales*, **Applied Categorical Structures** 31 (2023), article 28, §3, **Remark 3.8**: the coequalizer of a proper internal equivalence relation is a proper quotient and its frame is the fixed-point frame of the appropriate interior operator; https://link.springer.com/article/10.1007/s10485-023-09736-x .

## 1. The useful internal relation-composition lemma

Let L=O(X), with three closed relations I, U, F as in [A-consolidated-theorems.md](A-consolidated-theorems.md). For arbitrary locale X,

    I∘I ⊆ U.

**Frame proof:** On P=I_12∩I_23↪X³, for any a,b∈L satisfying a*∨b*=1, the defining disjoint-rectangle condition for I gives

    a_1 ∧ (a*)_2 = 0,     (b*)_2 ∧ b_3 = 0.

Therefore a_1∧b_3 = a_1∧[(a*)_2∨(b*)_2]∧b_3=0. So P→X² factors through U. This is a map-of-locales factorization; no spatial assumption is made.

In particular **I=U implies I is an internal equivalence relation** in Loc, since I is already reflexive and symmetric. The weaker assumption that I is independently transitive is enough for the principal theorem below.

## 2. Properness in the locale sense

For f:Y→Z, its inverse-image frame homomorphism f*:O(Z)→O(Y) has right adjoint f_*.

"Proper" means:

1. f_* preserves directed joins (Scott continuity);
2. f_*(u∨f*(v)) = f_*(u)∨v (closed Frobenius/co-Frobenius).

This should not be confused with the ordinary term "proper subrelation" or with some authors' "perfect/semi-proper" for Scott continuity alone.

## 3. Main theorem, continuous frames (working proof)

**Theorem.** In classical mathematics, let X be a locale with **continuous** frame O(X). Suppose that E=I(X)=clΔ_X is **transitive** and that its relation projections p_1,p_2:E⇉X are **proper** locale maps. Then

    I(X)=U(X)=F(X),

and the coequalizer q:X→Q=X/E is the **completely regular reflection** of X.

The hypothesis I=U suffices for transitivity by §1, but is not needed elsewhere.

**Proof.**

**(a) Effective proper quotient.** Because E is closed by definition, symmetric and reflexive, and by hypothesis transitive, it is a closed proper internal equivalence relation. By Vermeulen 5.17, E is the kernel pair of its coequalizer q:X→Q. By Vermeulen / Manuell, q is a proper surjection.

**(b) Q has closed diagonal.** Proper maps are stable under products and take closed sublocales to closed sublocales. Thus q×q:X²→Q² is proper and the image of the closed E↪X² is closed. Since qp_1=qp_2, that image is contained in Δ_Q. By reflexivity Δ_X⊆E and surjectivity of q, it contains Δ_Q. Therefore Δ_Q is closed. Thus Q is **strongly Hausdorff**, in the point-free closed-diagonal sense.

**(c) Proper quotients preserve continuity of frames.** Let L=O(X), B=O(Q). Because q is a locale surjection, q*:B→L is injective and its right adjoint q_* satisfies q_*q*=id_B. Since L is continuous and q_* preserves directed joins, for b∈B,

    b=q_*q*(b)=∨_{u≪q*(b)}q_*(u).

If u≪q*(b) then q_*(u)≪b. Indeed, given any directed join b≤∨_i b_i, apply q*: q*(b)≤∨_i q*(b_i), hence u≤q*(b_i) for some i; by adjunction and q_*q*=id, q_*(u)≤b_i. Thus B is continuous.

**(d) Q is completely regular (classical Hofmann–Lawson).** A continuous frame has a strongly locally compact sober point-space representation in ZFC, and its localic product is spatial. The closed diagonal of Q means the represented space is Hausdorff. Locally compact Hausdorff spaces are completely regular. Hence Q is a **completely regular locale**.

**(e) Identify the reflection and all three relations.** The closed diagonal kernel pair E=kerpair(q) contains Δ. Since E=I=clΔ, every real-valued map f:X→R has kerpair(f)⊇E and therefore coequalizes p_1,p_2. By the coequalizer property, each such f factors uniquely through q. Since Q is completely regular, its frame B is generated by pullbacks of real opens. Therefore q*B equals the largest completely regular subframe C(L) of L, and q is the completely regular reflection r_X.

By the prior intrinsic characterization F(X)=kerpair(r_X), we obtain

    I(X)=kerpair(q)=F(X).

The universal chain I⊆U⊆F then gives I=U=F. □

**Status caveats:** (i) The Vermeulen statement was confirmed from full-text *indexed scan* rather than a directly opened PDF (the source currently returns 403). Its literal Cor 5.17 wording is unambiguous; seek an independently accessible copy for the referee packet. (ii) The quotient's strong Hausdorff/continuity steps are reasoned here but have **not undergone a separate adversarial mathematical audit**. (iii) The proof of all facts used in §1 is independent of Vermeulen.

## 4. What happens without continuity?

Vermeulen's effectiveness does **not** need continuity: for *any* locale X and *any* closed proper internal equivalence E, q is a proper quotient with

    E=kerpair(q),   Δ_Q is closed.

But a **strongly Hausdorff** quotient Q need not be completely regular for an arbitrary locale. If E=I, all real maps X→R factor through q, and so F(X) is the kernel pair of the composite X→Q→Q_cr. The exact residual question is **complete regularity/functionally detecting the quotient**, not effectiveness.

This distinction is substantive: a proof of I=F without continuity must furnish some real-function separation or stronger quotient condition beyond strong Hausdorffness.

## 5. Saturated-open operator and nonproperness in our example

Set d_I=∨_{a∧b=0}a⊠b∈L⊗L. Then, whether or not I is an equivalence relation,

    r_I(u)=(p_2)_*p_1^*(u)
          =∨{v∈L:(1⊠v)≤(u⊠1)∨d_I}.

When I is an equivalence relation with proper projections, this is the proper quotient's interior operator q*q_*; its fixed points are B=O(Q). It is Scott-continuous.

In the cofinite-cloud deleted-plank X, I=U but nontrivial classes A,B are noncompact; its quotient is **closed** yet not proper. The increasing opens

    U_n=X\(A\{a_0,…,a_n}),    A={a_0,a_1,…},

satisfy ∨_n U_n=1, but no r_I(U_n) meets the class A; hence

    r_I(∨_n U_n)=1 ≠ ∨_n r_I(U_n).

This pins down **why the proper quotient proof cannot apply**: Scott continuity fails, while closedness does not. Nonproperness itself is NOT equivalent to I≠F; normal-base examples show the implication's conclusion can hold without properness.

## 6. Priority and next steps

- Vermeulen 1994 already solves the **unrestricted effectivity** problem for closed proper equivalence relations. Do **not** claim novelty for this.
- Our transitivity inclusion I∘I⊆U is elementary, with a Cameron–Kumar pointwise analogue. Its localic expression may already occur in diagonal separation literature.
- The properness/continuous-frame I=F collapse is an application of Vermeulen, Hofmann–Lawson and completely regular reflection, not yet priority-cleared as a stated corollary.
- **Next dedicated task should be an adversarial audit**, including the product-image argument, quotient operator, non-Hausdorff properness conventions, T1 cofinite-cloud example, and consistency with established positive coherent/compact theorems. In view of the just-corrected source mistake, this should precede new theorem hunting.
