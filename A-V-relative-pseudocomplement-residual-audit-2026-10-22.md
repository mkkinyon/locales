# Relative pseudocomplement audit for residual good-open quotient

Date 22 Oct 2026. NO proof of universal depth three.

Let L be a frame, w a canonical bar neighborhood, Φ_w(a)=∨{b:a≤b*∨r_w(b)}, and p=∨{a:Φ_w(a)=1}. For the closed quotient M=↑p, the relative pseudocomplement is (πb)^*_M=b→p.

Lemma: for any p in any frame L, the following are equivalent:
(i) p has an open complement;
(ii) b→p=p∨b* for all b in L.
Proof (i)→(ii): if p complemented, L≅↓p×↓p*, so componentwise Heyting implication to p equals p∨b*. For (ii)→(i), put b=p to get 1=p→p=p∨p*. Thus p complemented.

Hence the difference between quotient pseudocomplement and ordinary pseudocomplement modulo p is inescapable for any noncomplemented p, regardless of its definition as join of good opens. E.g. three-element frame {0<t<1}, p=t, b=t: b→p=1 whereas p∨b*=t.

Useful exact consequence of special definition p: if x∧b≤p then
  x∧b=∨{x∧b∧a: Φ_w(a)=1}.
This follows from p=join all good opens and distributivity. Every term is a good open because Φ is antitone. Thus each quotient disjointness rectangle (x,b) with x∧b≤p has its overlap in a join of good first-coordinate opens. But this does not cover x itself: in general x≰b*∨(x∧b). A proof of the missing step would require an additional frame identity not available (failure in Sierpinski frames).

For quotient b=p, (πb)^*=1_M whereas π(b*)=p∨p*, potentially <1_M. This is a special case of the inequality being strict. Note πb is the BOTTOM of M here; this alone is not a witness of new nontrivial quotient-good opens.

Conclusion: direct replacement b→p by p∨b* cannot work unless p is complemented. The good-open generation of p allows coverage of overlap-errors, but does not by itself lift whole relative disjointness leaves. No rank-four example or universal depth-three proof obtained.
