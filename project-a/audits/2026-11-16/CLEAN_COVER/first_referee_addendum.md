# Addendum to the independent blind referee report

**Project A — Clean-cover unbounded differentials**  
**16 November 2026**

These are additional mathematical observations made after completing the independent blind audit. They supplement the original report; neither changes its conclusion concerning the validity of the principal results.

## 1. A hidden suspension structure in the capped-path induction

Let \((X_r,E_r,C_r,z_r,b_r)\) be an avoiding-path datum of length \(r\), and put

\[
K_r=F_0(X_r\setminus\{b_r\}).
\]

Here the notation means the induced subcomplex of the filtration-zero order complex on the indicated deletion. Perform the capped extension to \(X_{r+1}\), adding \(u,v,y\), with new initial marked vertex \(u\).

Deleting \(u\) from the new filtration-zero complex gives

\[
\boxed{K_{r+1}=\bigl(v*F_0(X_r)\bigr)\cup(y*K_r).}
\]

The two pieces are cones and their intersection is exactly \(K_r\), since \(v\parallel y\). As the union is a simplicial homotopy pushout,

\[
\boxed{K_{r+1}\simeq\Sigma K_r.}
\]

There is also a useful statement for the entire filtration-zero complex. The link of the new minimal vertex \(u\) in \(F_0(X_{r+1})\) is \(y*K_r\): any filtration-zero simplex containing \(u\) must avoid \(b_r\), because \(u\prec b_r\) is marked. This link is a cone, so deleting \(u\) preserves homotopy type. Consequently,

\[
F_0(X_{r+1})\simeq K_{r+1}\simeq\Sigma K_r,
\]

and iteration gives

\[
\boxed{K_r\simeq\Sigma^{r-3}K_3\qquad(r\ge3).}
\]

The witness cycles behave exactly as this interpretation suggests. The induction produces

\[
z_{r+1}=(v-y)*z_r,
\]

which is the ordinary suspension cycle. Under the Mayer–Vietoris suspension isomorphism

\[
\widetilde H_r(K_{r+1};\mathbb Z)
\cong\widetilde H_{r-1}(K_r;\mathbb Z),
\]

its class corresponds, up to sign, to \([z_r]\). Thus the correction in Lemma 4.1 has a conceptual interpretation: **the capped-path construction suspends the filtration-zero homology class while adding one marked cover to the path**.

This provides an independent explanation for the persistence of nontrivial filtration-zero classes during the induction. The maximal-simplex certificate remains important for establishing *exactly how late* those classes survive in the filtration.

## 2. The penultimate filtration stage is a homotopy sphere

There is a general consequence of the terminal-simplex hypothesis. Suppose \(Q\) is contractible, \(m\ge3\), and the only simplex of weight \(m\) is the \(m\)-simplex \(\tau\). Then

\[
\Delta Q=F_{m-1}\cup\tau,
\qquad F_{m-1}\cap\tau=\partial\tau\cong S^{m-1}.
\]

The relative long exact sequence shows that the inclusion

\[
\partial\tau\longrightarrow F_{m-1}
\]

is an integral homology equivalence. Moreover, adjoining a cell of dimension at least three does not alter the fundamental group. Since \(Q\) is contractible, \(F_{m-1}\) is simply connected. The homological Whitehead theorem therefore upgrades the homology equivalence to a homotopy equivalence:

\[
\boxed{F_{m-1}\simeq S^{m-1}.}
\]

In particular, each relevant final filtration step attaches a single simplex to a homotopy sphere, making the resulting complex contractible.

This makes the long differentials geometrically transparent. The terminal step is simple; the interesting feature is the **early appearance of the sphere's fundamental homology class**:

- In the absolute construction, it originates in \(F_0\).
- In the relative construction, it originates in \(H_*(F_1,F_0)\).
- In both, the cover-count filtration can postpone its death arbitrarily far.

## 3. A concrete follow-up question about the seed

The suspension recurrence reduces the homotopy type of the recursively constructed filtration-zero complexes to one finite computation:

\[
K_3=F_0(X_3\setminus\{a\}).
\]

If \(K_3\simeq S^2\), then the recurrence would immediately give

\[
F_0(X_r)\simeq S^{r-1}\qquad(r\ge4).
\]

**The hypothesis \(K_3\simeq S^2\) has not yet been checked.** This is a proposed small calculation, not a theorem asserted here. Its resolution could sharpen the description of the entire example family. A broader possibility is to investigate whether the induction preserves a simple homotopy type at intermediate filtration stages, not merely at \(F_0\) and \(F_{r-1}\).

Of these suggestions, I would pursue the suspension structure first. It appears capable of replacing substantial chain-level bookkeeping with a conceptual topological description, without altering the conclusions of the original referee report.
