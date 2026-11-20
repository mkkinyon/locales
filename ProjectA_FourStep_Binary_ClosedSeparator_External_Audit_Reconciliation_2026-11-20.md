# Project A — binary closed-separator four-step theorem: external-audit reconciliation

**20 November 2026.** Disposition of the independent blind report dated 19 November 2026. The referee was given the binary closed-separator blind-audit ZIP from 19 November, without earlier internal or external reports.

## 1. Outcome and status

The referee's verdict was **valid with specific repairs and clarifications, subject to one substantive lemma being supplied in full**. The referee found no counterexample to

$$
(H\circ_XH)\circ_X(H\circ_XH)
=X\times_QX=\operatorname{EqHull}_X(H),
$$

and independently accepted the binary Cantor fusion, antichain-free strips, actual-pullback compositions, and direct fit/closed-separator contradiction.

The gap was in the **arbitrary-union defect** used to prove the special comparison $p^{-1}G\simeq G$. The candidate established local finiteness of each single-open defect $O\setminus r(O)$, then asserted the same for $r(\bigcup_iO_i)\setminus\bigcup_i r(O_i)$ without argument. The latter does **not** follow formally from the former. The referee supplied a Lebesgue-number compactness proof, and the revised canonical manuscript now contains it in §I.A, Lemma A, followed by a full localic-discreteness argument and Proposition B.

**Recorded status:** repaired, independently supported theorem, with no second external reading of the revised text. This is stronger than the original candidate status, but it does **not** certify the revised file as independently re-audited word for word.

## 2. Mathematical repair incorporated

For patch opens $O_i$ let $V=\bigcup_iO_i$, $W=r(V)$, $U=\bigcup_i r(O_i)$ and $F=W\setminus U$. Fix $x\in W$, relatively compact patch neighborhoods $\overline{N'}\subset N$, $\overline N\subset W$, and a finite subcover of $\overline N$ by the $O_i$. Choose its Lebesgue number $\delta>0$ and $\varepsilon=\operatorname{dist}(\overline{N'},P\setminus N)>0$.

Every sufficiently late strict edge has length $<\min(\varepsilon,\delta/3)$. The entire upper cone of each late minimal vertex in $N'$ is inside $N$ and has diameter $<\delta$, hence lies in a single $O_i$. That vertex belongs to $r(O_i)$ and not $F$. Nonminimal points of $W$ also belong to $U$. Therefore $F\cap N'$ consists of finitely many early minimal vertices. This gives relative patch local finiteness.

The complement $F$ is closed in the upper-open $W$. At each $v\in F$, the finite upper cone $\uparrow v$ has a patch neighborhood meeting $F$ only at $v$; taking its upper core produces an upper-open neighborhood isolating $v$ *within $F$*. Thus $F$ is a spatial discrete locale, not merely a point-set discrete family. Every nonzero sublocale of it has a point. A sublocale $S$ admitting none of these minimal-vertex points meets $F$ in zero.

That last assertion establishes arbitrary-join preservation of $\lambda r$, where $\lambda:\mathcal O(X)\to\mathcal O(S)$ is restriction. Finite-meet preservation is immediate. The resulting frame map provides a section of the patch comparison; the corresponding **single-open** discrete defect proves that every patch-open generator on $p^{-1}S$ agrees with an upper-open generator, proving surjectivity. The revised proof states these steps explicitly.

The referee emphasizes—and we retain—that the argument needs **uniform shrinking of all strict-edge lengths**. Merely knowing that individual fences are finite would not suffice.

## 3. Claim-by-claim disposition

| Module | Independent report | Action |
| --- | --- | --- |
| Coordinate selections, closed height-one order, forcing | Accepted | No theorem change |
| Completely prime nonordinary quotient point | Accepted | No theorem change |
| Exact fibre via positive *and negative* quotient-open tests | Accepted | Retain both tests |
| Finite-cutoff rigidity and coframe decomposition | Accepted | Retain localic embedding proof |
| Special patch-fibre comparison | Main omitted lemma | Add compactness/Lebesgue defect lemma, discrete-sublocale proof, full frame-isomorphism argument |
| Least support, Baire colour selection | Accepted | No theorem change |
| Binary Cantor graph without antichains | Accepted | Specify inherited anchor remains interior along its all-zero chain |
| Dense strips and actual image composition | Accepted | Identify patch projections and upper target maps |
| Fit/closed-separator contradiction | Accepted | Keep direct argument, no global graph generation |
| $0\ne\mathcal B(M)\le\Lambda$ | Accepted | Retain independent nonzero witness |
| Reflexivity, four-step assembly, equivalence hull | Accepted | Preserve fixed balanced bracketing |

The referee also suggested explaining that $\mathcal B(\Gamma)\ne0$ follows from nonemptiness of $\Gamma$ (not from a point of $\mathcal B(\Gamma)$), and distinguishing relative compactness in the cutoff proof. Both are editorial clarifications, not independent mathematical hypotheses.

## 4. Verification boundary

The audited statement is the **balanced four-step equality for this explicit finite-fence model**, not a general theorem about all point-generated localic relations. No claim of associativity, properness of the full patch counit, strict inequalities among intermediate powers, or minimality of four steps is being made. The original blind packet is archival; its proof text has not been rewritten retroactively.

For the definitive proof text, see [the repaired four-step theorem](ProjectA_FourStep_Short_Proof_Consolidated_2026-11-19.md), revised on 20 November, with its [exact-fibre/cutoff companion](ProjectA_FourStep_Fibre_Cutoff_Foundations_CANONICAL_2026-11-20.md). For exact provenance, preserve the full referee report verbatim under the audit archive.

## 5. Investigative handoff

With the defect repaired, the immediate foundational task is closed. The next mathematical phase can distinguish:

1. **Four-step effectiveness** (now supported) from **strictness or minimal step length** (not established here).
2. The explicit finite-fence mechanism from possible **structural sufficient conditions** for effectiveness in other locally compact or stably compact locales.
3. The point-generated component relation $H$ from the full kernel pair $K_q$, including what additional generic relations are forced by image composition.

These are directions, not assertions of new results.
