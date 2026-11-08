# Project A — Internal reconciliation of the second Scott-continuity referee report

**8 November 2026.** Review of the user-supplied `ProjectA_Scott_converse_EXTERNAL_report2_universal_family_2026-11-08.md` (the **same external referee** as the first Scott-continuity report, not a second independent referee). The original external reports remain intact. This is an independent internal mathematical read of the new arguments, not a literature-priority certification or a fresh external blind review.

## 0. Disposition and exact theorem

**Provisional PASS — internally rechecked referee-origin theorem (`E*`)**, subject to an independent adversarial review before publication, especially of Lemma 2(b) and the mixed preframe/frame coverage presentation. No fatal mathematical error was found in this internal pass.

For **arbitrary locales** X,Y and a **closed sublocale** E↪X×Y, with projections p₁,p₂,

    r_E=(p₂)_* p₁*: O(X)→O(Y)

preserves **inhabited directed** joins **if and only if** p₂:E→Y is proper, i.e. (p₂)_* preserves inhabited directed joins and satisfies closed Frobenius. This is the referee's proposed **Theorem L*** (not our original Theorem L). It needs no continuity, sobriety, spatiality, compactness, or equivalence-relation axioms. In the constructive frame-theoretic setting, it uses the standard pullback stability of proper maps; that background theorem is independently documented in published locale literature.

Consequences: the original arbitrary-locale Scott-converse question PR-01 has a **working positive resolution**, not a published or separately refereed one. The topological theorem T′ and continuous-locale theorem L remain independently checked as before, but are now corollaries under additional spatiality assumptions.

## 1. Background checks — why the mixed frame presentation is legitimate

Let L=O(X), W=P_U X. The frame O(W) is presented by symbols □u with □1=1, □(u∧v)=□u∧□v, and □(∨↑u_i)=∨□u_i for **nonempty directed** families. Every open of W is a join of symbols □u; a preframe homomorphism L→O(Y) determines a locale map Y→W.

Coproduct O(X×W)=L⊕O(W) is presented by rectangles (s,v) standing for s⊕□v, with (i) arbitrary joins in s and (ii) inhabited directed joins in v. Both coverages are stable under binary meets: meet an (i)-cover using frame distributivity; meet an (ii)-cover using preservation of directed joins by meet with a fixed element. Johnstone's coverage theorem therefore gives **C-ideals** e⊆L×L, downward closed and closed under those two join rules. Principal ↓(s,v) are indeed C-ideals. In particular, (s,v)∈e iff s⊕□v≤e.

Write the v-section of e as ↓σ_e(v). Then σ_e is antitone and σ_e(∨↑v_i)=∧_i σ_e(v_i). Conversely any such σ gives a C-ideal. Meets are intersections. This representation is a legitimate change of coordinates and does not assume spatiality or Boolean distributivity.

**External background check:** Picado–Pultr–Tozzi, *Locales*, Chapter II, states that proper maps are pullback-stable, using preframes, and identifies the proper-map Frobenius condition. Vermeulen (1994) is the original cited primary source. The proof uses these published facts as inputs; it does not reprove proper base change.

## 2. Referee Lemma 1 — the universal family's nucleus

Define K⊆X×W by the inequalities (1⊕□u)|_K≤(u⊕1)|_K for every u∈L. The map

    k(e) = e^K = {(s,v) : (s∧v,v)∈e}

is a nucleus: downclosure and the arbitrary first-coordinate join rule follow directly; for the directed second-coordinate rule, if (s∧v_i,v_i)∈e for each i, directedness gives (s∧v_j,v_i)∈e for every i,j, first take the directed join in i, then the arbitrary join in j. Inflationarity, idempotence, and meet preservation are immediate.

As the referee shows, k imposes each required inequality, so its sublocale lies in K. Conversely, on K each generator s⊕□v is bounded by (s∧v)⊕□v; applying this to every generator of e^K shows k≤j_K. Thus k=j_K, with the order of nuclei carefully observed. Equivalent sections are

    σ_{k(e)}(v) = (v→σ_e(v)).

The corresponding right-adjoint formula is valid:

    (π_K)_*i_K^*(e) = Ψ(e) = ⋁{□u:(u,u)∈e}.

This follows since i_K^*(1⊕□u)≤i_K^*(e) iff (u,u)∈e, and the generators □u join-generate O(W).

## 3. Referee Lemma 2 — the delicate coverage-closure argument

This is the critical new step. Suppose G⊆L×L is a downset already closed under **all** first-coordinate joins, and that □(s∧v)≤V for all (s,v)∈G. Let C be the closure of G under downward closure, directed first-coordinate joins, and directed second-coordinate joins.

- The inequality P(s,v): □(s∧v)≤V is preserved by these **three** operations: both join rules give directed joins of the meets s∧v, so the preframe relation applies. It would NOT automatically survive a non-directed first-coordinate join.
- To show the full C-ideal closure needs no extra non-directed joins, perform two inductions. First fix a G-element and consider generated pairs that may be joined to it at any smaller second coordinate (`B''` in the report). This class contains G and is closed under the three operations. In the second-coordinate induction step, use v'∧v_i ↑ v' when v'≤∨↑v_i. This proves stability under joining one G-element to any C-element.
- Next repeat the induction with *both* elements in C (`B` in the report). The same step works because downclosure supplies (s',v'∧v_i)∈C. Thus C is closed under binary first-coordinate joins. Since (0,v)∈G for every v (the **empty** first-coordinate join is included), directed joins of finite joins yield arbitrary first-coordinate joins. Hence C is the entire C-ideal cl(G), and P holds throughout.

I verified the base and all three closure operations for both nested inductions. No use of excluded middle was detected. This lemma merits a *separate referee check* because its scope (arbitrary/inhabited directed joins in different coordinates) is subtle.

## 4. Theorem K — directed joins and Frobenius

Given a directed family of C-ideals (e_i), form its first-coordinate join-closed union G with section σ_G(v)=∨_iσ_{e_i}(v). For (s,v)∈G, the elements

    t_i=s∧v∧σ_{e_i}(v)

are directed with ∨t_i=s∧v, and (t_i,t_i)∈e_i. Therefore □(s∧v)=∨□t_i≤∨Ψ(e_i). Lemma 2 propagates this inequality to cl(G)=∨e_i. Thus Ψ preserves inhabited directed joins.

For Frobenius it suffices to check adjoining a generator 1⊕□d. The first-coordinate join-closed union of e and ↓(1,d) has sections

    σ_G(v)=σ_e(v)∨⋁_{(v≤d)}1.

For (s,v)∈G, put t=s∧v∧σ_e(v); then (t,t)∈e. Constructively,

    s∧v = t ∨ ⋁_{(v≤d)}(s∧v),

an **inhabited directed** join (the candidate summands are t and, when v≤d, s∧v). Its box lies below Ψ(e)∨□d. Lemma 2 gives the desired inequality for Ψ(e∨(1⊕□d)). Finite generator joins are handled iteratively, and arbitrary joins via directed finite joins plus the already-proved directed continuity. The reverse inequality is monotonicity and D≤Ψ(1⊕D). Hence Ψ satisfies full Frobenius.

A quotient-surjection observation (B5) then correctly descends Scott continuity of Ψ=(π_K)_*i_K^* to Scott continuity of (π_K)_*. The reported formula for K→W therefore establishes *both* defining clauses of properness.

## 5. Theorem L* — final descent to arbitrary closed relations

Given E=c(a)⊆X×Y, let r=(p₂)_*p₁*. It preserves finite meets automatically; when Scott-continuous it is a preframe morphism and determines φ:Y→W with φ^*(□u)=r(u).

Pull K⊆X×W back along id_X×φ. The resulting family E~⊆X×Y is the pullback of K→W along φ, so E~→Y is proper by stability under base change. Adjunction gives E⊆E~, because 1⊕r(u)≤(u⊕1)∨a holds for each u. Since E is closed in X×Y, its inclusion E↪E~ is the pullback of c(a) and hence a **closed**, therefore proper, inclusion. The composite E→E~→Y is p₂ and is proper. The converse follows immediately from Scott continuity of p₂*.

The pasting/base-change identifications and the closed-inclusion step check out. Neither reflexivity nor transitivity of E is involved. The construction can be read without asserting that K is literally a universal compact-family object (its explicit site definition suffices).

## 6. Small repairs, provenance and limits

1. State *inhabited directed* throughout; otherwise the claim fails for projections with empty fibers.
2. The proof is **constructive in ordinary impredicative locale/frame theory** conditional on the standard constructively valid stability theorem for proper maps. Avoid an unqualified predicative/foundation-independent claim.
3. Correctly distinguish the **same referee's follow-up proof** from a second blind verification. Its result should initially be `E*` (referee-origin, internally checked), not `E` in the sense of external verification of an independently prepared author proof. The original Scott topological and continuous-locale statements retain their earlier `E` statuses.
4. The novelty/priority of L* and of the explicit K nucleus has **not** been established. There may be antecedents in the upper powerlocale, fibrewise compactness, or perfect-map literature; do not claim originality.
5. The report's specialization-relation properness lemma (§8.5) looks correct by its diagonal adjunction formula, but it is supplementary and not part of the dependency chain for L*.
6. The first report's earlier *constructive concern* is overcome by the new **direct Frobenius proof**, not by assuming that compact fibers imply properness.
7. No new conclusion about complete regularity of strongly Hausdorff quotients follows from L* alone; the separate functional-separation problem PR-02 remains.

**Recommendation:** update Q05 with a separate entry for L* and the universal-family theorem; move PR-01 to the *provisionally resolved / independent verification* category. Before publication, seek an independent referee pass of the site presentation, Lemma 2(b), and Frobenius. Proceed with the previously planned coherent-composition audit separately; do not combine the two packets.

## Source ledger

- Original referee follow-up (user-provided): `ProjectA_Scott_converse_EXTERNAL_report2_universal_family_2026-11-08.md`, §§2–8.
- First Scott referee report (user-provided): `ProjectA_Scott_converse_EXTERNAL_referee_report_2026-11-08.md`.
- Project A first reconciliation: `ProjectA_Scott_converse_external_referee_reconciliation_2026-11-08.md`.
- J. J. C. Vermeulen, *Proper maps of locales*, JPAA 92 (1994), 79–107.
- J. Picado, A. Pultr and related edition, *Locales*, Chapter II, §5 (published proof/source statement for pullback stability of proper maps), https://www.mat.uc.pt/~picado/publicat/Chapter2.pdf .
- P. T. Johnstone, *Stone Spaces*, II.2.11–13, and *Sketches of an Elephant*, C3.2, C4.1; Johnstone–Vickers, *Preframe presentations present* (1991).