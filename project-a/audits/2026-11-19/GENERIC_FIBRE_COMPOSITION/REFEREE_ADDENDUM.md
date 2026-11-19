# Addendum to the independent referee report

**Project A: generic-fibre composition localization**  
**19 November 2026**

These are additional mathematical observations, not qualifications of the favourable verdict in my original blind report. They follow formally from the verified theorem and were not explicitly mentioned there.

## 1. The generic fibre detects every associativity defect in the interval

Under (F) and (C), the correspondence

\[
\Phi:[H,K]\longrightarrow[D,B],\qquad \Phi(R)=R\wedge B
\]

is both an order isomorphism and an isomorphism for the *possibly nonassociative* binary composition operations. It therefore **reflects as well as preserves** every equation between bracketed compositions.

In particular, for all \(R,S,T\in[H,K]\),

\[
(R\circ_X S)\circ_X T=R\circ_X(S\circ_XT)
\]

if and only if

\[
(R_G\circ_G S_G)\circ_G T_G
=R_G\circ_G(S_G\circ_G T_G).
\]

The proof is simply to apply the injective map \(\Phi\) to both sides and use its composition law twice. Thus composition is associative **throughout** \([H,K]\) if and only if it is associative throughout \([D,B]\); more generally, any particular associator vanishes on one side exactly when the corresponding associator vanishes on the other.

For Project A, which has repeatedly encountered failures of associativity of image-defined localic composition, this offers a useful reduction. Any specific nonassociativity phenomenon among relations containing \(H\) and contained in \(K\) is wholly visible in the generic fibre, with no additional obstruction hidden in the finite-cutoff part.

## 2. A precise ambient reformulation of the four-step target

Write \(T=H\circ_XH\) and \(D^2=D\circ_GD\). Since

\[
\Phi(T)=D^2,\qquad \Phi(K)=B,
\]

the same principle yields the equivalence

\[
\boxed{
(D^2\circ_GD^2=B)
\quad\Longleftrightarrow\quad
((H\circ_XH)\circ_X(H\circ_XH)=K).
}
\]

Both expressions use the **balanced four-factor bracketing**. This equivalence does not assume associativity and, emphatically, proves neither equality. It does show that the outstanding global Cantor-fusion claim can be formulated either as saturation of the generic square by \(D^2\circ_GD^2\), or as saturation of the complete kernel pair by \(T\circ_XT\).

The second formulation may occasionally be more convenient geometrically, because the finite-cutoff part of \(K\) is already controlled by \(H\). The theorem shows that any remaining obstruction is exactly the generic one.

## 3. Transfinite closure ranks agree, not just the final hulls

The original report verified the equivalence-hull identity. One can sharpen it to a statement about **every stage and the first stabilization ordinal** of a natural closure process.

Starting with \(R_0=H\), define

\[
R_{\alpha+1}=R_\alpha\circ_XR_\alpha,\qquad
R_\lambda=\bigvee_{\alpha<\lambda}R_\alpha
\quad\text{for a limit ordinal }\lambda.
\]

Starting with \(Z_0=D\), define \(Z_\alpha\) by the identical recursion in \(G\). All iterates stay in the respective intervals. Reflexivity guarantees \(R_\alpha\le R_{\alpha+1}\) and \(Z_\alpha\le Z_{\alpha+1}\); composition is monotone.

Because an order isomorphism of complete lattices preserves arbitrary joins and \(\Phi\) preserves composition, transfinite induction gives

\[
\boxed{\Phi(R_\alpha)=Z_\alpha\quad\text{for every ordinal }\alpha.}
\]

In particular,

\[
R_{\alpha+1}=R_\alpha
\quad\Longleftrightarrow\quad
Z_{\alpha+1}=Z_\alpha.
\]

Therefore the first stabilization stage, whenever recorded as an ordinal, is *identical* on the ambient and generic sides. Stabilization must eventually occur by the usual cardinality argument for an increasing chain in a set-sized complete lattice. Its stable value is the least reflexive transitive relation containing the initial relation: every reflexive transitive upper bound contains all stages by induction, and a fixed point of squaring is transitive. If \(H\) is symmetric, all stages remain symmetric, so the stable value is the equivalence hull.

This is an exact rank correspondence, beyond the equality of the final hulls. It might be useful if Project A returns to the lengths of localic relation-closure processes. It does **not** imply any finite bound on those lengths.

## Closing assessment

Of these remarks, I regard **associativity reflection** as the most conceptually useful, and the **balanced four-step equivalence** as the most directly relevant to the current proof agenda. The transfinite observation is a formal corollary worth recording, though there is no need to pursue ordinal constructions unless they become relevant to a concrete question.
