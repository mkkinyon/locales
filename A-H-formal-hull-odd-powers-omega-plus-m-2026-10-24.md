# Formal hull H: coherent graph calculus and exact transfinite stages

24 October 2026. Working internally checked results; independent audit not yet requested.

Let Q=O(X)⊕O(X), d=d_I, I=C(d), D=fit(Delta), W=cl(D), V=fit(I), and H be the least simultaneously closed and fitted sublocale containing Delta.

Define kappa(a)=meet{x in Q: for all w with a∨w=1, w→x=x}. The fixed-point calculation for the open nuclei gives cl(fit(C(a)))=C(kappa(a)). Kappa is monotone and deflationary; kappa(a)=a exactly when C(a) is fitted.

Iterate a_0=d; a_(alpha+1)=kappa(a_alpha); at limit lambda put a_lambda=meet_{beta<lambda}a_beta. The decreasing chain eventually stabilizes at a_infty and H=C(a_infty). Indeed every closed fitted C(b) containing Delta has b≤d and kappa(b)=b, hence b≤a_alpha for all alpha; C(a_infty) is itself closed fitted and minimal.

At a limit the CLOSED stage is cl(join_{beta<lambda}C(a_beta)), not necessarily the bare sublocale join. The first closed stage after I is cl(V), containing W. Universally cl(W∨V)=cl(V) and fit(W∨V)=fit(W).

COHERENT GRAPH FORMULA: Let P be the spectral space of points with its Priestley patch topology and specialization order. Write up/down for product-order saturation and cl_p for patch closure. The ordinary point relations S_alpha of the successive closed stages satisfy
 S_0=I_pt (common upper bound);
 S_(alpha+1)=down(up(S_alpha));
 S_lambda=down(cl_p(union_{beta<lambda} S_beta)).
Each stage is patch-closed downward and represents the GENUINE spectral closed sublocale. This follows because fitting a patch-closed spectral closed sublocale gives the coherent fitted sublocale with point set up(S), and spectral closure is down(cl_p(-)).

Since down(up(R))=I_pt composed R composed I_pt, finite stages have
 S_n=I_pt^(2n+1), n finite.
Their union E is comparability-graph finite-path equivalence; S_omega=down(cl_p(E)).

The previously built two patch-convergent zigzag rays have exact first stabilization at omega: cl_p(E)=(A∪{t})² union (B∪{t})², already up/down saturated and equal H. The relation H there is nontransitive.

NEW FAMILY: For each m≥1, let A={a_0,a_1,...} be an infinite alternating zigzag; let T={t_0,...,t_(2m)} be a finite alternating zigzag t_0<t_1>t_2<t_3>...<t_(2m-1)>t_(2m); no comparisons A to T. On the patch set P=A∪T all points except t_0 are isolated, and cofinite A tails converge to t_0. This is compact zero-dimensional Priestley: isolated points have finite clopen principal upsets; t_0 is separated from y not above it by the clopen upset P\downarrow y (a finite downset). The order is patch-closed.

The finite comparability components are A and T, hence finite-path E=A²∪T². Its patch closure adds A×{t_0} and {t_0}×A. Since t_0 is minimal, this is already downward saturated. Put T_k={t_0,...,t_(2k)}. For k=0,...,m one obtains by induction:
 S_(omega+k)=A²∪T²∪(A×T_k)∪(T_k×A).
Indeed one I-step on the finite alternating handle grows T_k precisely to T_(k+1); all other blocks are already full, and there are no further patch limit points. Thus S_(omega+m)=P²=H but S_(omega+k)≠H for k<m. Every finite S_n also misses all A×T cross pairs. Therefore the first stabilization ordinal is EXACTLY omega+m.

This produces arbitrarily long finite tails beyond the first limit, even for COUNTABLE COHERENT SPECTRAL LOCALES. It measures the specified closed-stage cf iteration with closure at limit ordinals, not every alternate scheduling convention.

NEXT: independently audit Priestley fittedness/spatiality and the ordinal stage calculation; investigate whether nested patch limits yield omega·2, and whether a useful noncoherent formulation exists. No novelty claim.