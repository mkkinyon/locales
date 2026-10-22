# Local diagonal polarity law and postfixed opens

For any frame L and bar neighborhood w in L⊕L with d∨w=1, set r(b)=∨{u:u⊠b≤w} and Φ(a)=∨{b:a≤b*∨r(b)}.

Universal local diagonal polarity identity:
  a=∨_{b≤a}(b∧r(b)) for every a∈L.
Proof: bar implies diagonal μ(w)=1; μ(w)=∨_{u⊠v≤w}u∧v. For each a∧u∧v, set b=a∧v≤a, r(b)≥u, hence a∧u∧v≤b∧r(b). Conversely b∧r(b)≤a. In fact local law is equivalent to μ(w)=1, so it alone is NOT stronger than diagonal cover or equivalent to the bar condition.

For c_b=b∧r(b), one has Φ(c_b)≥b because c_b≤r(b)≤b*∨r(b). Since c_b≤b, we obtain c_b≤Φ(c_b). Hence
  ∨{c:c≤Φ(c)}=1.
This is an exact intermediate property of Φ forced by barhood: the postfixed-point opens of the antitone map Φ cover 1. (*) asks instead ∨{a:Φ(a)=1}=1. The former does NOT imply the latter for a general antitone map; an additional polarity/coproduct principle is needed.

One can also derive localized b-free inequality: every a is a join of opens c≤a with c≤Φ(c). The candidate bad residual p=∨{a:Φ(a)=1} need not contradict existence of postfixed pieces outside p; this is the remaining gap.

No universal depth-three proof and no rank-four counterexample obtained.
