# Project A — Q rank one: marked Urysohn locality under closed support, and failure of global closed heredity

**12 November 2026 — NEW INTERNAL EXACT LOCALITY COROLLARY + explicit negative control.** This segment returns directly to the far-rectangle formula after the Cantor–Bendixson/perfect chromatic-core investigation. **Both Q and Q′ remain open.** The main result is a *marked* rank-one stability theorem for the canonical open hole of a hypothetical Q counterexample; it does NOT say \(\Phi_2(z_1)=z_1\) is closed-hereditary. Indeed an explicit generic-point extension shows the latter is FALSE, even for a PERFECT closed \(T_1\) sublocale.

The marked result is mostly a precise new **corollary of the independently audited closed-support persistence** and the universal far-rectangle naturality; it must not be sold as a solution of Q. Its value is to identify the exact special far-geometry constraint inherited by the support despite nonheredity of the global condition.

## 0. The rank-one setup

Let \(L=O(X)\), \(Q_X=L\oplus L=O(X^2)\), \(w_C=\bigvee_{c\in C}c\boxtimes c\) for a frame cover C, and
\[
\Phi_X(q)=\bigvee_C(w_C\to q),\qquad
\Phi_{2,X}(q)=\bigvee_{F\text{ finite}}(w_F\to q).
\]
The Urysohn defining open is
\[
z_X=d_{\mathcal U(X)}
=\Phi_X(0)=\Phi_{2,X}(0)
=\bigvee_{\ a^*\vee b^*=1}a\boxtimes b.
\tag{0.1}
\]
Question Q is
\[
\boxed{\Phi_{2,X}(z_X)=z_X\Longrightarrow\Phi_X(z_X)=z_X.}
\tag{0.2}
\]

Assume **for the purpose of normalization** that X violates this implication. Then \(W_2(X)=U(X)=C_{X^2}(z_X)\), but \(W(X)<U(X)\). Choose a cover C with
\[
\rho=w_C\to z_X>z_X,\qquad
E=U(X)\wedge O_{X^2}(\rho)\ne0.
\tag{0.3}
\]
Choose the **least closed common coordinate support** \(K=C_X(e)\) of the nonzero E, as in [the externally audited support normalization](ProjectA_Qprime_PRENUCLEUS_BOOLEAN_SUPPORT_IDEMPOTENT_CORE_2026-11-12.md). In particular:
\[
E\le K^2,\qquad
W_2(K)\wedge O_{K^2}(\rho_K)=E,\qquad
W(K)\wedge O_{K^2}(\rho_K)=0,
\tag{0.4}
\]
where \(\rho_K=(i\times i)^*(\rho)\) and \(i:K\hookrightarrow X\) is the closed embedding. Its Booleanization B(E) is a finite-compatible generalized pair over K, with C|K matching value 0, and dense in E.

## 1. The Urysohn relation is functorial in the correct direction

**Lemma 1.1 (far rectangles restrict to far rectangles).** For any locale map \(f:Y\to X\),
\[
\boxed{\mathcal U(Y)\le(f\times f)^{-1}\mathcal U(X)}
\tag{1.1}
\]
as sublocales of Y².

*Proof.* For any a,b∈O(X) with \(a^*\vee b^*=1_X\), the inverse-image map preserves joins and finite meets, and
\[
f^*(a^*)\le(f^*a)^*,\qquad
f^*(b^*)\le(f^*b)^*.
\]
Hence \((f^*a)^*\vee(f^*b)^*=1_Y\). Thus pullback of every X-far rectangle is a Y-far rectangle; taking joins proves
\((f\times f)^*(z_X)\le z_Y\), equivalent to (1.1). QED.

For a closed inclusion K=C_X(e), identify
\[
Q_K=O(K^2)=\uparrow\varepsilon\subseteq Q_X,
\qquad
\varepsilon=(e\boxtimes1)\vee(1\boxtimes e),
\tag{1.2}
\]
with restriction map \(q:Q_X\to Q_K,\ q(t)=t\vee\varepsilon\). Then
\[
q(z_X)=z_X\vee\varepsilon\le z_K.
\tag{1.3}
\]

## 2. SAME marked rank-one hole survives exactly, including its FAR boundary

**Theorem 2.1 (marked Urysohn stabilization, NEW INTERNAL COROLLARY).** Under (0.3)–(0.4),
\[
\boxed{
E=
W_2(K)\wedge O_{K^2}(\rho_K)
=
\mathcal U(K)\wedge O_{K^2}(\rho_K)
=
(\mathcal U(X)\wedge K^2)\wedge O_{K^2}(\rho_K).
}
\tag{2.1}
\]

*Proof.* The independently audited exact support reduction gives the first equality. The universal inclusions \(W_2(K)\le U(K)\) and Lemma 1.1 give
\[
E\le U(K)\wedge O(\rho_K)
\le (U(X)\wedge K^2)\wedge O(\rho_K)
=E,
\]
because \(W_2(X)=U(X)\) and E is the original open hole. Thus all inclusions are equalities. NO assumption that \(W_2(K)=U(K)\) globally was used. □

This also proves that the extra Urysohn FAR separation created by passage to K is DISJOINT from the marked open hole: it can occur elsewhere in K², but cannot occur inside O(ρ_K).

**Frame form.** In the quotient frame \(Q_K=\uparrow\varepsilon\), equality of the closed restrictions in (2.1) is equivalent to
\[
\boxed{
z_K\wedge\rho_K
=(z_X\vee\varepsilon)\wedge\rho_K
=d_{W_2(K)}\wedge\rho_K.
}
\tag{2.2}
\]
By the independently audited exact closed-restriction pre-nucleus identity,
\[
z_K=\Phi_{2,K}(\varepsilon)=\Phi_{2,X}(\varepsilon)
\quad\text{(in the common upset \(\uparrow\varepsilon\))},
\]
and \(z_K\le\Phi_{2,K}(z_K)\le d_{W_2(K)}\). Therefore
\[
\boxed{
\rho_K\wedge\Phi_{2,K}(z_K)
=\rho_K\wedge z_K,
\qquad
\rho_K\le\Phi_K(z_K).
}
\tag{2.3}
\]
For the last inequality, use
\[
\rho_K\wedge w_{C|K}
=q(\rho\wedge w_C)\le q(z_X)\le z_K,
\]
so \(\rho_K\le w_{C|K}\to z_K\le\Phi_K(z_K)\).

**Interpretation:** After the canonical closed-support reduction, the finite pre-nucleus stays rank-one stabilized **ON THE SAME MARKED OPEN** \(\rho_K\), whereas the full pre-nucleus already swallows that entire open after one step. Thus the same hole is a first-step full-versus-finite Urysohn defect *locally*, even though the global finite rank-one equation may fail on K.

### 2.1 What the theorem does not claim

- No equality \(W_2(K)=U(K)\) globally; that is the false closed-heredity inference excluded by §3.
- No assertion that \(q(z_X)=z_K\) on ALL of K²; equality is only on the marked open rho_K.
- No assertion that K is minimal among all locales violating Q; only the least closed support of the marked E.
- No contradiction or proof of universal Q; this is a **precise inheritance and obstruction formula**, not a sufficient criterion for existence.

## 3. EXPLICIT perfect \(T_1\) closed-heredity countercontrol: adjoin one generic point

**Theorem 3.1 (rank-one stabilization is NOT closed-hereditary).** Let Y be any SOBER space, and construct
\[
X=Y\cup\{p\}
\]
with opens \(\varnothing\) and \(\{p\}\cup V\), \(V\in O(Y)\). Then:

1. X is sober and hyperconnected; Y is a CLOSED subspace with its ORIGINAL topology.
2. Every nonempty open of X contains p. Thus every nonzero open a has \(a^*=0\), so there are NO nonzero far rectangles and
\[
\boxed{z_X=0,\quad\mathcal U(X)=X^2,\quad
W(X)=W_2(X)=X^2,\quad
\Phi_{2,X}(0)=\Phi_{2,X}^2(0)=0.}
\tag{3.1}
\]
3. If Y is chosen as the compact sober **two-apex T₁** control from the October phase, then Y itself is **perfect** (has NO isolated points) and
\[
\boxed{\Phi_{2,Y}(z_Y)>z_Y,\qquad W_2(Y)<U(Y).}
\tag{3.2}
\]
Therefore global rank-one stabilization FAILS under the closed inclusion Y↪X, even though the ambient X stabilizes at rank zero.

*Proof of topology/sobriety.* The indicated opens form a topology. The closed sets are X and the old Y-closed subsets; X is irreducible with generic point p, and the other nonempty irreducible closed sets are precisely the old irreducible closed sets in Y, with their original generic points. Thus X is sober if Y is. Y is closed because {p} is open, and its induced opens are V.

*Proof of (3.1).* Because any two nonempty opens contain p, a nonzero open has pseudocomplement zero; (0.1) yields z_X=0. The full fitted diagonal is dense in X² by the universal regular-closed core theorem (U=X² is regular closed), so W=W₂=U=X²; in fact \(\Phi_X(0)=\Phi_{2,X}(0)=0\). Thus both pre-nuclei stabilize at zero.

*Proof of (3.2).* The compact two-apex Y=R∪{q_+,q_-} from October has the old R topology and two opposite cofinite ray-attachment neighborhoods. R is crowded and the two apices are nonisolated, so Y is perfect T₁, compact sober. Its Urysohn relation contains the two off-regular cross pairs whereas W₂(Y)=W(Y) is the regular-closed core, by the earlier working binary-cover calculation. Hence Φ₂,Y(z_Y)>z_Y. This is an imported explicit Y calculation, previously used in multiple audit packets.

**Algebraic nonheredity sharpened.** With \(e=\{p\}\in O(X)\) and ε the open complement of Y² as in (1.2), the exact closed-restriction identity gives
\[
\Phi_{2,X}(\varepsilon)=\Phi_{2,Y}(\varepsilon)=z_Y,\qquad
\Phi_{2,X}^2(\varepsilon)=\Phi_{2,Y}(z_Y)>z_Y.
\tag{3.3}
\]
But \(\Phi_{2,X}(0)=\Phi_{2,X}^2(0)=0\). Thus the finite pre-nucleus may stabilize after ONE step at bottom and FAIL to stabilize after one step at a CLOSED-SQUARE bottom ε, even when the corresponding closed sublocale Y is **perfect T₁**. This defeats a natural but invalid inductive path from X's rank-one equation to a closed support.

**Important separation-axiom qualification.** Although the CLOSED sublocale Y in Theorem 3.1 is perfect and T₁, the ambient X is **NOT T₁**: p is a generic point with closure all of X. Thus this construction disproves unrestricted CLOSED HEREDITY of rank-one fixedness, **not** closed heredity inside the subclass of sober T₁ ambient locales. The latter strengthening remains untested. Do not use this example to dismiss a possible T₁-specific hereditary theorem.

### 3.1 A useful limit of the far-generation method

The extreme example \(z_X=0\) while \(z_Y>0\) shows that **the special far-rectangle formula alone does not prevent arbitrarily large new far separation upon closed restriction**. The marked-hole rigidity of Theorem 2.1 uses the additional D₂-density and support conditions; it cannot be replaced with ordinary hereditary behavior of U. It also shows why simply assuming "the perfect chromatic frontier is \(T_1\)" does NOT allow us to restart Q inside that frontier.

## 4. Research decision / no moving target

The direct far-generation test yields a **positive exact local inheritance theorem (2.1)–(2.3)** and a **sharp negative global heredity control (3.1)–(3.3)**. Neither proves Q or Q′.

The remaining question is whether **local finite rank-one stabilization on a marked open E with full joint closed coordinate support** can force any **global** finite-stage behavior that would contradict the full first-step hole. The generic-point extension shows this cannot come merely from closed heredity, perfectness, or the abstract formula \(z=\bigvee_{\mathrm{far}}a\boxtimes b\); it must also use the open D₂-density of E and the linked-cover structure.

**Next bounded test** (if pursuing): attempt to prove that, under the *marked support conditions*, every new far separator of K outside the marked open can be reduced to a finite coarsening of the same bad cover. This is not claimed in the present segment, and a proof must engage the cover C rather than appeal only to T₁ or far generation. Avoid inventing further requirements for K without an explicit cover-level lemma.

**STATUS: NEW INTERNAL COROLLARIES / EXPLICIT CONTROL; NOT EXTERNALLY AUDITED. BOTH Q, Q′ OPEN.**
