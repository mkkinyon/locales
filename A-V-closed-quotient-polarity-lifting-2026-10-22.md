# Closed-quotient polarity and complemented lifting

Date: 22 Oct 2026. This note DOES NOT establish universal depth three.

Let L be a frame, p∈L, M=↑p the closed-quotient frame with π(x)=p∨x, and T=L⊕L. Set c_p=(p⊠1)∨(1⊠p). Standard product of closed sublocales identifies M⊕M with ↑c_p, and π⊕π carries w to w∨c_p. For the canonical rectangular polarity r_w(b)=∨{u:u⊠b≤w}, exact quotient formula:
 r_{bar w}(πb)=π(r_{w∨c_p}(b)).
Proof: πu⊠πb≤bar w iff u⊠b≤w∨c_p, using ↑c_p quotient.
Pseudocomplement in M is (πb)^*_M=b→p, since b→p≥p and it is independent of representative b modulo p. Hence
 h_{bar w}(πb)=(b→p)∨r_{w∨c_p}(b), viewed as element ≥p in L.
This displays TWO mechanisms that could create new good opens in a quotient: relative pseudocomplement, and strip-assisted rectangle membership. Neither is controlled by the inequality πΦ_w(a)≤Φ_barw(πa).

COMPLEMENTED CASE. Assume p complemented, e=p* and p∨e=1. Restriction identifies M with ↓e. For bar w, if a_bar∈M is good, let a∈↓e correspond to a_bar. Then a is good in L: for each quotient second open b_bar eligible with a_bar≤h_barw(b_bar), choose b≤e corresponding to b_bar. Restricting rectangular leaves inside e⊠e gives a≤h_w(b); this uses the coproduct restriction to complemented e blocks, and lifting of the canonical rectangle leaves. The eligible b cover e because a_bar is good in M. Also a∧p=0, hence a≤h_w(p) by a≤p*. Thus eligible second opens cover e∨p=1, proving Φ_w(a)=1. In particular quotient-good opens lift to good opens supported outside p; the issue in a genuinely noncomplemented closed quotient is essential.

The special p=∨{a:Φ_w(a)=1} need not be complemented; if p<1, ordinary topological density of p is no contradiction. It remains unknown whether any quotient-good open in ↑p lifts outside p when p is this special join. Such a theorem, together with enough quotient-good opens, would prove (*), but this note proves it only in the complemented case.
