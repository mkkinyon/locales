# Project A — internal adversarial audit: finite-cut and relative-density programme

**14 November 2026. INTERNAL ONLY. Do not include in first-pass blind external packet.**

## Scope and provenance

This audit begins *after* the previously internally audited closed-atomic/scattered weak-defect theorem. It reviews the newer results and proofs in:

1. `ProjectA_Q_RELATIVE_CHROMATIC_DENSITY_ALL_FINITE_FIXED_2026-11-13.md`;
2. `ProjectA_Q_SPATIAL_BAIRE_COUNTABLE_FINITE_TEST_DENSITY_2026-11-13.md`;
3. `ProjectA_Q_RELATIVE_BAIRE_INCIDENCE_PROFILES_POLISH_CONTROL_2026-11-13.md`;
4. `ProjectA_Q_BINARY_COVER_REDUCTION_CLOSED_RECTANGLE_BAIRE_2026-11-13.md`, including its later-added Scott example, fixed-point nontransfer and Boolean visibility criterion.

The closed-atomic theorem is also included in the **external** packet as an unaudited-by-outsiders prerequisite/control, but is not counted here as a new result. Neither Q nor Q′ has been proved or refuted.

## Verdict

**No fatal mathematical error found** in the four new notes after checking the arguments afresh, including the distinction between finite-cover density on an arbitrary closed relation and on the canonical `W₂`. The finite-cut identity received a fresh independent exhaustive Boolean check through eight indices (86,368 nonempty ordered support pairs), with zero failures. This is supporting evidence only; the finite distributive-lattice proof is decisive.

However, the claims have quite different levels of significance: the cut identity is a genuine new structural reduction for this programme; the Scott example is a sharp negative control; the Boolean visibility equivalence is **precisely a repackaging of Q′**; the chromatic/profile conditions are necessary but not sufficient. The external reviewer should independently check the following pressure points.

## Claim-by-claim hostile checks

### A. Finite matching-square cut identity

For a finite *cover* `F=(f_i)_(i=1)^n`, with `u_S=∨_(i∈S)f_i` and `v_S=∨_(i∉S)f_i`, the identity

\[
  w_F=\bigwedge_{S\subseteq[n]}\bigl((u_S\boxtimes u_S)\vee(v_S\boxtimes v_S)\bigr)
\]

is sound in the **frame of opens**, not merely on spatial points: writing `x_i=f_i⊠1`, `y_i=1⊠f_i`, finite distributivity reduces the assertion to a bounded distributive lattice identity under `∨x_i=∨y_i=1`. An evaluation to `2` yields nonempty supports `A,B`; a failed match `A∩B=∅` is witnessed by cut `S=A`. The restriction *finite* is necessary: arbitrary intersections and arbitrary distributive-lattice valuations cannot be interchanged naively. No use of spatiality is hidden.

**Corollaries checked:** `D_bin=D₂`; `Φ_bin(d)=d` iff `Φ₂(d)=d`. The latter follows because finite intersections of dense *open* sublocales are dense, not by an unjustified equality `(a∧b)→d=(a→d)∨(b→d)`. No equality of these two pre-nuclei at arbitrary inputs has been shown.

### B. Binary-cover failure as disjoint closed rectangles

For an ordinary spatial `X` and `u∪v=X`, the bad pairs of the binary matching square are `(X\v)×(X\u) ∪ (X\u)×(X\v)`. The closed sets are disjoint, and every disjoint closed pair comes from such a cover. A `Φ₂`-fixed closed relation `Y=C(d)` has every binary square dense. On any *relatively open*, *spatial*, *Baire* chart `E` inside `Y`, each failure locus is relatively closed nowhere dense, while every ordinary `C`-bad pair belongs to some such locus. No countability of that family follows; ordinary Baire category alone does **not** refute a hole. Crucial: the localic statement about `Y` need not have a point-set interpretation when it is nonspatial.

### C. Countable finite-test criterion

The proof correctly combines a countable family of dense opens on **spatial Baire `W₂`** with an explicitly assumed pointwise detection property. Each ordinary pair passing *every* finite cover passes any arbitrary cover `C`: partition `C` into opens containing its first endpoint and the rest, obtaining a binary coarsening that would fail at a `C`-bad pair. A countable frame has countably many finite covers; a cofinal finite-cover sequence also works. Neither a merely second-countable `X` nor localic Baire without spatiality supplies the needed countable pointwise detector. The point-finite corollary is correct and properly weaker than the earlier point-finite rigidity result.

### D. Chromatic and incidence-profile restrictions

The finite color block cover gives a matching square dense on every nonzero relatively open chart `V` of a `C`-hole. Same-index terms are zero there, so the off-diagonal monochromatic union is dense; the local cross-link graph must have infinite chromatic number. For any prescribed incidence set `S⊂I`, its first- or second-coordinate fiber is contained in the failure set of the binary cover obtained by coarsening `C` along `S`. That failure is closed nowhere dense on a spatial `E`. A countable range of profiles in a nonzero Baire chart is impossible. Countable-cover tails force infinite incidence in both coordinates on a dense `G_δ`.

**Ambiguity to repair editorially in later canonical note:** “the profile map has countable range on every ordinary point” should read “its range over all ordinary points under consideration is countable.” The theorem itself uses the correct, global-or-local meaning.

The Polish control `X=[ω]^ω` and disjoint-pairs `R` does realize all finite *color-coarsening* density requirements, not all ambient finite covers. The clopen binary cover `{c_n,X\c_n}` explicitly fails density. Do not upgrade this model into a Q′ candidate.

### E. Scott closed/Baire example and weak-vs-strong distinction

Take `X=P(ω)\{∅}` with Scott inclusion topology, `c_n={A:n∈A}` and `R={(A,B):A∩B=∅}`. The relative basic patches `R_(P,Q)` use disjoint finite nonempty `P,Q`; a nested-finite-condition fusion meets any countable list of dense opens of `R`. Hence `R` is Baire. A finite cover of `X` contains some member that covers infinitely many singleton points; upward closure gives two fresh **distinct** singleton generators and witnesses that member's square inside every `R_(P,Q)`. Thus every finite matching square is dense on `R`, but the countable `C` square vanishes identically. Applying the least dense Booleanization `B(R)` gives a genuine generalized finite-compatible, full-incompatible map pair and `D₂>D`.

**Do not conflate the three ambient objects**: `R` is a *closed* relation, `B(R)` is a sublocale of `D₂`, and the canonical `W₂` is the *whole square*. `R` is nowhere dense in the whole square because every Scott-basic product rectangle contains an overlapping pair. The diagonal is dense in the whole square because any two nonempty Scott opens meet. Consequently `d₀=0`, `W₂=W=X²`, so Q′ holds. The noncanonical open `d_R=w_C` is nevertheless finite-fixed (`Φ₂(d_R)=d_R`) and not full-fixed (`Φ(d_R)=1`). This refutes the **too-strong** assertion that every finite-fixed open must be full-fixed; it does **not** refute Q′. Underlying localic product/spatial interpretation must be checked explicitly by the external referee, although these Scott spaces are locally compact sober.

### F. Canonical Boolean visibility equivalence

For `Y=W₂=cl(D₂)`, `K_C=Y∧C(w_C)` and `A_C=D₂∧C(w_C)`, the following are equivalent: `w_C|Y` not dense; `K_C` contains a nonzero `Y`-open; `cl_Y(A_C)` has nonzero interior; a Boolean `B≤A_C` has closure with nonzero `Y`-interior. The potentially delicate step is from a nonzero `Y`-open `V≤K_C` to `B(V)≤D₂∧V`: density of `D₂` in `Y` restricts to density on **open** `V`, and `B(V)` is contained in every dense sublocale of `V`. The open qualifier cannot be replaced by an arbitrary closed `V` (the Scott countercontrol refutes that variant). Conversely the closedness of `K_C` carries any closure of `A_C` into `K_C`.

**Scope issue:** It is correct to test one cover `C` at a time: because a least dense Booleanization exists as a sublocale, individual dense matching-square opens jointly contain `B(D₂)`, so an arbitrary intersection of these opens remains dense as a *sublocale*, even though an intersection of ordinary point sets of dense opens might be empty. The external referee should check this localization and its relationship to `B(D₂)≤D`.

## Adversarial failure modes deliberately excluded

1. The proof does **not** equate a dense sublocale with an abundance of ordinary points; Booleanized weak defects can be pointless.
2. It does **not** assume localic products are point-set products in arbitrary nonspatial cases.
3. It does **not** use all `Φ₂`-fixed closed relations as if they were the canonical maximal `W₂`.
4. It does **not** deduce strong Q′ failure from `D₂>D`, even when the weak defect is dense in a noncanonical closed relation.
5. It does **not** claim Q/Q′ solved, or that the exact visibility condition improves logically on Q′.

## Handoff

The accompanying blind packet reproduces all main proofs, includes the reusable definitions/notation boilerplate (core + Q module), and asks for specific independent scrutiny of the steps above without disclosing this audit. External suggestions about detecting **relative openness inside canonical `W₂`**, or selecting a countable family of disjoint-closed-rectangle tests, are welcome but secondary to correctness.
