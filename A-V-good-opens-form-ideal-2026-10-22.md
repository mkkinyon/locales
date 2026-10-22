# Finite join closure of depth-three good opens

Date 2026-10-22.

Let L be any frame, h:L→L any ANTITONE map (in particular h_w(b)=b*∨r_w(b) for a rectangular bar). Define
  Phi(a)=∨{b∈L:a≤h(b)}
and G={a:Phi(a)=1}.

THEOREM: Phi sends finite joins to meets:
  Phi(0)=1, Phi(a∨c)=Phi(a)∧Phi(c).

Proof: E_a={b:a≤h(b)}. Antitonicity gives E_{a∨c}=E_a∩E_c, hence Phi(a∨c)≤Phi(a)∧Phi(c). Conversely, distributivity gives Phi(a)∧Phi(c)=∨_{b∈E_a,d∈E_c}(b∧d). For such b,d, h(b∧d)≥h(b)∨h(d)≥a∨c, so b∧d∈E_{a∨c}. Thus opposite inequality. Also 0≤h(b) for every b so Phi(0)=1.

COROLLARY: G is a (lattice) ideal of L: downward-closed, contains 0, closed under finite joins. Its join p=∨G is therefore a DIRECTED supremum. In particular, if k is a compact element of L with k≤p, then k≤g for some g∈G and hence k∈G. In an algebraic frame (join-dense compact elements), G is precisely the set of elements below p that can be certified from compact refinements, but the compact property alone does not imply arbitrary join closure of G.

The rank-three rational-bridge bar has p=1 but Phi(1)≠1 (since depth-two V→H fails), so Phi does NOT preserve all joins-to-meets, even for genuine bar polarities. This is the precise infinitary discontinuity obstructing reducing (*) to Phi(1)=1.

FURTHER: For any finite family a_1,...,a_n each admitting V→H certificates, their join also admits such a certificate, by taking vertical meets of the second-coordinate cover pieces and combining the horizontal leaf covers. The resulting rank remains 2. This is a nontrivial local proof normalization.

NOTE: For a *compact top* frame L, (*) implies Phi(1)=1, since compactness reduces the G-cover of top to finitely many g∈G and finite joins remain in G. But this is only a conditional implication, not a proof of (*) in compact locales.

No universal rank-three proof obtained; however G being directed sharply constrains a potential residual counterexample.
